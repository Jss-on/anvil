#!/usr/bin/env python3
"""Cited design-rule calculations from the Anvil rulebook, evaluated as a gate check.

`design/rules.tsv` rows name a calculation, its inputs and the pass criterion; every calculation
carries the rulebook identifiers (BOOKTAG-nnn) it implements so the audit report can cite the
source. Numbers here are transcriptions of the cited references; keep them in sync with
references/rulebook/*.md. Standard library only.
"""
from __future__ import annotations

import math
from pathlib import Path

from anvil import DETAILS, compare, number, table, traces

# --- physical constants -------------------------------------------------------------------------
RHO_CU_20C = 1.724e-8          # ohm*m, annealed copper at 20 C (Brooks & Adam; Wilson)
ALPHA_CU = 0.00393             # 1/K temperature coefficient of copper resistivity
MU0 = 4e-7 * math.pi
C0 = 299_792_458.0             # m/s
OZ_TO_MM = 0.0347              # 1 oz/ft^2 copper ~ 34.7 um (35 um nominal)
MIL = 0.0254                   # mm

# IPC-2221 Table 6-1 electrical conductor spacing (mm). Columns: voltage range upper bound (V, peak)
# then classes B1 internal, B2 external uncoated sea level, B3 external uncoated >3050 m,
# B4 external polymer coated, A5 external conformal coated, A6 external component lead uncoated,
# A7 external component lead conformal coated. Above 500 V add the listed mm per volt.
# Rows <= 100 V cross-checked against Mitzner et al. Table 6.8 ("after IPC-2221B", mils: internal 2/2/4/4,
# bare 4/4/24/24, soldermask-only 2/2/5/5, conformal 5/5/5/5). Rows > 100 V: verify against the licensed standard.
IPC2221_TABLE_6_1 = [
    (15,   0.05, 0.10, 0.10, 0.05, 0.13, 0.13, 0.13),
    (30,   0.05, 0.10, 0.10, 0.05, 0.13, 0.25, 0.13),
    (50,   0.10, 0.60, 0.60, 0.13, 0.13, 0.40, 0.13),
    (100,  0.10, 0.60, 1.50, 0.13, 0.13, 0.50, 0.13),
    (150,  0.20, 0.60, 3.20, 0.40, 0.40, 0.80, 0.40),
    (170,  0.20, 1.25, 3.20, 0.40, 0.40, 0.80, 0.40),
    (250,  0.20, 1.25, 6.40, 0.40, 0.40, 0.80, 0.40),
    (300,  0.20, 1.25, 12.5, 0.40, 0.40, 0.80, 0.80),
    (500,  0.25, 2.50, 12.5, 0.80, 0.80, 1.50, 0.80),
]
IPC2221_ABOVE_500_MM_PER_V = dict(B1=0.0025, B2=0.005, B3=0.025, B4=0.00305, A5=0.00305, A6=0.00305, A7=0.00305)
IPC2221_COLUMNS = ["B1", "B2", "B3", "B4", "A5", "A6", "A7"]


def f(value, name, minimum=None, positive=False):
    """Parse one numeric input with a clear error naming the field."""
    try:
        return float(number(value, minimum=minimum, positive=positive))
    except ValueError as error:
        raise ValueError(f"{name}: {error}") from None


# --- current carrying / copper ------------------------------------------------------------------
def trace_current_ipc2221(width_mm, thickness_oz, delta_t_c, layer="external"):
    """IPC-2221 conductor sizing: I = k * dT^0.44 * A^0.725, A in mil^2 (k = 0.048 external, 0.024 internal).
    Conservative legacy chart; IPC-2152 and Brooks & Adam give higher capacity for most geometries.
    Sources: IPC2221 §6.2 (Fig. 6-4 curves fitted), BROOKS ch.2, COOMBS ch.22."""
    width_mil = f(width_mm, "width_mm", positive=True) / MIL
    thickness_mil = f(thickness_oz, "thickness_oz", positive=True) * 1.378
    area = width_mil * thickness_mil
    k = 0.048 if layer == "external" else 0.024
    current = k * f(delta_t_c, "delta_t_c", positive=True) ** 0.44 * area ** 0.725
    return dict(value=current, units="A", area_mil2=area, k=k)


def trace_temp_rise_ipc2221(current_a, width_mm, thickness_oz, layer="external"):
    """Inverse of trace_current_ipc2221: dT = (I / (k * A^0.725))^(1/0.44). Sources as above."""
    width_mil = f(width_mm, "width_mm", positive=True) / MIL
    area = width_mil * f(thickness_oz, "thickness_oz", positive=True) * 1.378
    k = 0.048 if layer == "external" else 0.024
    rise = (f(current_a, "current_a", positive=True) / (k * area ** 0.725)) ** (1 / 0.44)
    return dict(value=rise, units="C", area_mil2=area)


# Brooks & Adam Table 5.1 / App. D fits of IPC-2152 internal data: copper oz -> (K(width_mil), a, b, c).
IPC2152_INTERNAL = {0.5: (lambda w: 130 if w <= 20 else 125 if w <= 50 else 110, 2.0, -1.10, -1.52),
                    1.0: (lambda w: 200, 1.9, -1.10, -1.52),
                    2.0: (lambda w: 300, 2.0, -1.15, -1.52),
                    3.0: (lambda w: 429 if w >= 50 else 368, 1.9, -1.10, -1.52)}


def trace_rise_ipc2152(current_a, width_mm, thickness_mm=0.035, layer="external"):
    """IPC-2152-based temperature rise of a lone trace in still air (no planes: worst case; real boards with
    planes/adjacent copper run cooler, BROOKS-066). External: dT = 215.3 I^2 W^-1.15 Th^-1; internal:
    dT = K I^a W^b Th^c by copper weight (W, Th in mil). Anchors: 40 mil x 1.5 mil at 4 A -> 33.5 C;
    600 mil x 0.65 mil at 15 A -> 47.5 C. Sources: BROOKS-046, BROOKS-048, BROOKS-096, BROOKS-122, Table 5.1, App. D."""
    amps = f(current_a, "current_a", minimum=0)
    w_mil = f(width_mm, "width_mm", positive=True) / MIL
    th_mil = f(thickness_mm, "thickness_mm", positive=True) / MIL
    if layer == "external":
        rise = 215.3 * amps ** 2 * w_mil ** -1.15 * th_mil ** -1.0
    else:
        oz = min(IPC2152_INTERNAL, key=lambda k: abs(k - th_mil / 1.35))  # 1 oz ~ 1.35 mil (Brooks)
        k, a, b, c = IPC2152_INTERNAL[oz]
        rise = k(w_mil) * amps ** a * w_mil ** b * th_mil ** c
    return dict(value=rise, units="C", width_mil=w_mil, thickness_mil=th_mil)


def via_group_adequacy(trace_width_mm, trace_thickness_mm, vias, drill_mm, plating_mm=0.020):
    """Vias run at the trace temperature when the trace copper area is <= ~2x the group's barrel area
    (Brooks: equality at A_trace = 1.5-2.0 A_via; parallel vias share current within ~20 %).
    value = 2 * A_vias / A_trace (>= 1 adequate). A_via = pi (r^2 - (r - th)^2), minimum plating.
    Sources: BROOKS-077, BROOKS-079, BROOKS-081, BROOKS-085, BROOKS-094."""
    r = f(drill_mm, "drill_mm", positive=True) / 2
    th = min(f(plating_mm, "plating_mm", positive=True), r)
    a_via = math.pi * (r * r - (r - th) ** 2) * f(vias, "vias", positive=True)
    a_trace = f(trace_width_mm, "trace_width_mm", positive=True) * f(trace_thickness_mm, "trace_thickness_mm", positive=True)
    return dict(value=2 * a_via / a_trace, units="ratio", via_area_mm2=a_via, trace_area_mm2=a_trace)


def trace_resistance(width_mm, thickness_oz, length_mm, temp_c=20):
    """R = rho(T) * L / (w * t), rho(T) = rho20 * (1 + alpha (T - 20)). Sources: BROOKS ch.1, WILSON ch.1."""
    rho = RHO_CU_20C * (1 + ALPHA_CU * (f(temp_c, "temp_c") - 20))
    area = f(width_mm, "width_mm", positive=True) * 1e-3 * f(thickness_oz, "thickness_oz", positive=True) * OZ_TO_MM * 1e-3
    resistance = rho * f(length_mm, "length_mm", positive=True) * 1e-3 / area
    return dict(value=resistance, units="ohm", rho_ohm_m=rho, area_m2=area)


def via_barrel_equivalent_width(drill_mm, plating_um=25):
    """Via barrel copper cross-section expressed as the external trace width (1 oz) with equal area.
    A via carries at least the current of a trace with the same copper cross-section (BROOKS ch.5).
    Plating 20/25 um are the IPC-6012 Class 2/3 minimum averages (IPC6012 Table 3-2)."""
    drill = f(drill_mm, "drill_mm", positive=True)
    plating = f(plating_um, "plating_um", positive=True) * 1e-3
    area_mm2 = math.pi * ((drill / 2 + plating) ** 2 - (drill / 2) ** 2)
    return dict(value=area_mm2 / OZ_TO_MM, units="mm", barrel_area_mm2=area_mm2)


def fusing_current_preece(diameter_mm):
    """Preece fusing current for copper wire: I = 10244 * d^1.5 (d in inch). Source: BROOKS ch.6."""
    d_in = f(diameter_mm, "diameter_mm", positive=True) / 25.4
    return dict(value=10244 * d_in ** 1.5, units="A")


def fusing_time_onderdonk(current_a, area_mm2, ambient_c=20, melt_c=1083):
    """Onderdonk (adiabatic): 33.5 (I/A)^2 t = log10((T_melt - Ta)/(234 + Ta) + 1), A in circular mils.
    Book check: 15 mil x 0.65 mil (9.75 mil^2) at 6 A -> 0.09 s. Real PCB traces fuse 1.5-6x later (cooling);
    never use this to claim a trace survives a slow overload. Sources: BROOKS-100..110, eq.(12.2)/(G.22)."""
    area_cmil = f(area_mm2, "area_mm2", positive=True) / 5.067e-4
    ambient = f(ambient_c, "ambient_c")
    rise = f(melt_c, "melt_c") - ambient
    seconds = (area_cmil / f(current_a, "current_a", positive=True)) ** 2 * math.log10(rise / (234 + ambient) + 1) / 33.5
    return dict(value=seconds, units="s", area_cmil=area_cmil)


def skin_depth(frequency_hz, rho_ohm_m=RHO_CU_20C, mu_r=1):
    """delta = sqrt(rho / (pi f mu)). Copper: ~66 um at 1 MHz, 2.1 um at 1 GHz. Sources: BOGATIN ch.6, POZAR ch.1."""
    depth = math.sqrt(f(rho_ohm_m, "rho_ohm_m", positive=True) / (math.pi * f(frequency_hz, "frequency_hz", positive=True) * MU0 * f(mu_r, "mu_r", positive=True)))
    return dict(value=depth * 1e6, units="um")


# --- spacing / safety -----------------------------------------------------------------------------
def clearance_ipc2221(voltage_v, condition="B2"):
    """Minimum conductor spacing from IPC-2221 Table 6-1 for the peak voltage and application class
    (B1 internal, B2/B3 external uncoated at sea level / above 3050 m, B4 external polymer coated,
    A5 conformal coated, A6/A7 component leads). Product-safety standards (IEC 62368-1/60601/61010)
    override this generic board table. Source: IPC2221 §6.3 Table 6-1 (as reproduced in MITZ ch.2, WILSON ch.2)."""
    voltage = f(voltage_v, "voltage_v", minimum=0)
    column = IPC2221_COLUMNS.index(condition.upper()) + 1 if condition.upper() in IPC2221_COLUMNS else None
    if column is None:
        raise ValueError(f"condition must be one of {IPC2221_COLUMNS}")
    for row in IPC2221_TABLE_6_1:
        if voltage <= row[0]:
            return dict(value=row[column], units="mm", band=f"<= {row[0]} V")
    above = IPC2221_TABLE_6_1[-1][column] + (voltage - 500) * IPC2221_ABOVE_500_MM_PER_V[condition.upper()]
    return dict(value=above, units="mm", band="> 500 V")


def clearance_margin(actual_mm, voltage_v, condition="B2"):
    """Actual spacing minus the IPC-2221 Table 6-1 requirement (positive = compliant)."""
    required = clearance_ipc2221(voltage_v, condition)["value"]
    return dict(value=f(actual_mm, "actual_mm", minimum=0) - required, units="mm", required_mm=required)


# --- transmission lines / signal integrity ---------------------------------------------------------
def microstrip_z0(width_mm, height_mm, er, thickness_oz=1):
    """IPC-2141 microstrip approximation: Z0 = 87/sqrt(er+1.41) * ln(5.98 h / (0.8 w + t)); valid for 0.1 < w/h < 2.0,
    1 < er < 15. Use a field solver for impedance-controlled production stackups. Sources: HALL00 ch.3, BOGATIN ch.7, MITZ ch.16."""
    w, h, t = f(width_mm, "width_mm", positive=True), f(height_mm, "height_mm", positive=True), f(thickness_oz, "thickness_oz", positive=True) * OZ_TO_MM
    e = f(er, "er", positive=True)
    z0 = 87 / math.sqrt(e + 1.41) * math.log(5.98 * h / (0.8 * w + t))
    eff = (e + 1) / 2 + (e - 1) / 2 / math.sqrt(1 + 12 * h / w)
    return dict(value=z0, units="ohm", er_eff=eff, delay_ps_per_mm=math.sqrt(eff) / C0 * 1e9, w_over_h=w / h)


def stripline_z0(width_mm, height_mm, er, thickness_oz=1):
    """IPC-2141 symmetric stripline: Z0 = 60/sqrt(er) * ln(4 b / (0.67 pi (0.8 w + t))), b = plane-to-plane spacing,
    valid for w/b < 0.35, t/b < 0.25. Sources: HALL00 ch.3, BOGATIN ch.7."""
    w, b, t = f(width_mm, "width_mm", positive=True), f(height_mm, "height_mm", positive=True), f(thickness_oz, "thickness_oz", positive=True) * OZ_TO_MM
    e = f(er, "er", positive=True)
    z0 = 60 / math.sqrt(e) * math.log(4 * b / (0.67 * math.pi * (0.8 * w + t)))
    return dict(value=z0, units="ohm", delay_ps_per_mm=math.sqrt(e) / C0 * 1e9)


def bandwidth_from_risetime(rise_time_ns):
    """BW = 0.35 / t_r (10-90 % rise time). Sources: BOGATIN ch.2 rule of thumb, JOHNSON93 ch.1 (knee f = 0.5/t_r)."""
    tr = f(rise_time_ns, "rise_time_ns", positive=True)
    return dict(value=0.35 / tr, units="GHz", knee_ghz=0.5 / tr)


def critical_length(rise_time_ns, er_eff=3.2, fraction=6):
    """A trace needs transmission-line treatment when its delay exceeds t_r / fraction (fraction 6 for
    reflections to be negligible; 2-3 for the classic 'long line' boundary). Sources: BOGATIN ch.8, JOHNSON93 ch.4."""
    tr = f(rise_time_ns, "rise_time_ns", positive=True)
    velocity_mm_per_ns = C0 / math.sqrt(f(er_eff, "er_eff", positive=True)) * 1e-6
    return dict(value=tr / f(fraction, "fraction", positive=True) * velocity_mm_per_ns, units="mm", velocity_mm_per_ns=velocity_mm_per_ns)


def crosstalk_ratio(spacing_mm, height_mm):
    """Near-end crosstalk saturation estimate for coupled microstrip: NEXT ~ 1 / (1 + (s/h)^2).
    Design rule: s >= 3 h keeps NEXT below ~10 %. Sources: BOGATIN ch.10, HALL00 ch.4 (approximation)."""
    ratio = 1 / (1 + (f(spacing_mm, "spacing_mm", positive=True) / f(height_mm, "height_mm", positive=True)) ** 2)
    return dict(value=ratio * 100, units="%")


# --- power delivery -------------------------------------------------------------------------------
def pdn_target_impedance(rail_v, ripple_pct, transient_a):
    """Z_target = (V * ripple%) / dI. Sources: BOGATIN ch.13, RITCHEY ch.on PDN, ARCH ch.5."""
    z = f(rail_v, "rail_v", positive=True) * f(ripple_pct, "ripple_pct", positive=True) / 100 / f(transient_a, "transient_a", positive=True)
    return dict(value=z * 1e3, units="mohm")


def capacitor_srf(capacitance_nf, esl_nh):
    """Self-resonant frequency f = 1 / (2 pi sqrt(L C)); above it the capacitor is an inductor. Sources: BOGATIN ch.13, BOWICK ch.1."""
    srf = 1 / (2 * math.pi * math.sqrt(f(capacitance_nf, "capacitance_nf", positive=True) * 1e-9 * f(esl_nh, "esl_nh", positive=True) * 1e-9))
    return dict(value=srf / 1e6, units="MHz")


def bias_current(supply_v, device_v, resistance_ohm):
    """Current set by a series resistor from a supply into a fixed-voltage device (Darlington gain block, LED):
    I = (Vs - Vd) / R, with the resistor dissipating I^2 R. Sources: AOE-3330, SCHERZ ch.4, WILSON ch.3."""
    i = (f(supply_v, "supply_v") - f(device_v, "device_v", minimum=0)) / f(resistance_ohm, "resistance_ohm", positive=True)
    return dict(value=i * 1e3, units="mA", resistor_w=i * i * f(resistance_ohm, "resistance_ohm", positive=True))


def inductor_reactance(inductance_nh, frequency_mhz):
    """X_L = 2 pi f L: an RF choke must stay far above the line impedance at every operating frequency (AOE-3330;
    below its self-resonance, which the vendor model must confirm)."""
    return dict(value=2 * math.pi * f(frequency_mhz, "frequency_mhz", positive=True) * 1e6 * f(inductance_nh, "inductance_nh", positive=True) * 1e-9, units="ohm")


def capacitor_reactance(capacitance_pf, frequency_mhz, esl_nh=None):
    """X_C = 1 / (2 pi f C), or with the body ESL the series |2 pi f L - 1 / (2 pi f C)| (above its self-resonance
    a capacitor is an inductor: ARCH-067): a DC block or RF bypass must be a small fraction of the line impedance
    across the band (AOE-3330)."""
    w = 2 * math.pi * f(frequency_mhz, "frequency_mhz", positive=True) * 1e6
    x = 1 / (w * f(capacitance_pf, "capacitance_pf", positive=True) * 1e-12)
    if esl_nh is not None:
        x = abs(w * f(esl_nh, "esl_nh", minimum=0) * 1e-9 - x)
    return dict(value=x, units="ohm")


def decoupling_count(target_mohm, esl_nh, frequency_mhz):
    """Number of identical capacitors in parallel so that their mounted inductance meets Z_target at f:
    n = 2 pi f L / Z_target (inductive region). Sources: BOGATIN ch.13, HALL00 ch.5."""
    n = 2 * math.pi * f(frequency_mhz, "frequency_mhz", positive=True) * 1e6 * f(esl_nh, "esl_nh", positive=True) * 1e-9 / (f(target_mohm, "target_mohm", positive=True) * 1e-3)
    return dict(value=math.ceil(n), units="count", exact=n)


def plane_capacitance(area_mm2, spacing_mm, er=4.4):
    """C = er e0 A / d for a power/ground plane pair (e0 = 8.854e-12 F/m). Sources: HALL00 ch.5, RITCHEY."""
    c = f(er, "er", positive=True) * 8.854e-12 * f(area_mm2, "area_mm2", positive=True) * 1e-6 / (f(spacing_mm, "spacing_mm", positive=True) * 1e-3)
    return dict(value=c * 1e9, units="nF")


# --- switching converters ------------------------------------------------------------------------
def buck_ripple(vin_v, vout_v, iout_a, fsw_khz, l_uh, c_uf, esr_mohm=0):
    """CCM buck: D = Vout/Vin, dI = (Vin - Vout) D / (f L), dV = dI/(8 f C) + dI*ESR, L_crit = (Vin-Vout) D / (2 f Iout).
    Sources: ERICKSON ch.2, PRESSMAN ch.1."""
    vin, vout, iout = f(vin_v, "vin_v", positive=True), f(vout_v, "vout_v", positive=True), f(iout_a, "iout_a", positive=True)
    fsw, l, c = f(fsw_khz, "fsw_khz", positive=True) * 1e3, f(l_uh, "l_uh", positive=True) * 1e-6, f(c_uf, "c_uf", positive=True) * 1e-6
    d = vout / vin
    di = (vin - vout) * d / (fsw * l)
    dv = di / (8 * fsw * c) + di * f(esr_mohm, "esr_mohm", minimum=0) * 1e-3
    return dict(value=dv * 1e3, units="mV", duty=d, ripple_current_a=di, ripple_ratio=di / iout, l_crit_uh=(vin - vout) * d / (2 * fsw * iout) * 1e6,
                switch_peak_a=iout + di / 2, ccm=iout > di / 2)


def boost_ripple(vin_v, vout_v, iout_a, fsw_khz, l_uh, c_uf):
    """CCM boost: D = 1 - Vin/Vout, dI = Vin D / (f L), dV = Iout D / (f C), input current Iin = Iout/(1-D).
    RHP zero f_z = (1-D)^2 R / (2 pi L). Sources: ERICKSON ch.2 & ch.8, PRESSMAN ch.1."""
    vin, vout, iout = f(vin_v, "vin_v", positive=True), f(vout_v, "vout_v", positive=True), f(iout_a, "iout_a", positive=True)
    fsw, l, c = f(fsw_khz, "fsw_khz", positive=True) * 1e3, f(l_uh, "l_uh", positive=True) * 1e-6, f(c_uf, "c_uf", positive=True) * 1e-6
    d = 1 - vin / vout
    di = vin * d / (fsw * l)
    dv = iout * d / (fsw * c)
    r = vout / iout
    return dict(value=dv * 1e3, units="mV", duty=d, ripple_current_a=di, iin_avg_a=iout / (1 - d), rhp_zero_khz=(1 - d) ** 2 * r / (2 * math.pi * l) / 1e3)


def linear_regulator_dissipation(vin_v, vout_v, iout_a, theta_ja_c_per_w, ta_c=25, tj_max_c=125):
    """P = (Vin - Vout) Iout, Tj = Ta + P theta_JA; value = Tj margin below Tj,max. Sources: AOE ch.9, SCHERZ ch.11, WILSON ch.9."""
    p = (f(vin_v, "vin_v") - f(vout_v, "vout_v")) * f(iout_a, "iout_a", minimum=0)
    tj = f(ta_c, "ta_c") + p * f(theta_ja_c_per_w, "theta_ja_c_per_w", positive=True)
    return dict(value=f(tj_max_c, "tj_max_c") - tj, units="C", power_w=p, tj_c=tj)


def junction_temperature(power_w, theta_ja_c_per_w, ta_c=25):
    """Tj = Ta + P * theta_JA. Sources: AOE ch.9, WILSON ch.9."""
    tj = f(ta_c, "ta_c") + f(power_w, "power_w", minimum=0) * f(theta_ja_c_per_w, "theta_ja_c_per_w", positive=True)
    return dict(value=tj, units="C")


def derating_ratio(applied, rated):
    """Applied / rated stress ratio in percent (compare against the project's derating policy). Sources: WILSON ch.4, SCHERZ ch.3."""
    return dict(value=f(applied, "applied", minimum=0) / f(rated, "rated", positive=True) * 100, units="%")


# --- EMC ------------------------------------------------------------------------------------------
def loop_radiation(current_ma, frequency_mhz, area_cm2, distance_m=3):
    """Differential-mode (loop) far-field estimate: E = 1.316e-14 * I * f^2 * A / d (SI units), reported in dBuV/m.
    Sources: PAUL ch.8, WILLIAMS ch.11 (loop radiation), ARCH ch.2."""
    e = 1.316e-14 * f(current_ma, "current_ma", minimum=0) * 1e-3 * (f(frequency_mhz, "frequency_mhz", positive=True) * 1e6) ** 2 * f(area_cm2, "area_cm2", minimum=0) * 1e-4 / f(distance_m, "distance_m", positive=True)
    return dict(value=20 * math.log10(max(e, 1e-12) * 1e6), units="dBuV/m", e_v_per_m=e)


def common_mode_radiation(current_ua, frequency_mhz, length_m, distance_m=3):
    """Common-mode cable radiation: E = 1.257e-6 * I * f * L / d (SI units), reported in dBuV/m. Sources: PAUL ch.8, WILLIAMS ch.11."""
    e = 1.257e-6 * f(current_ua, "current_ua", minimum=0) * 1e-6 * f(frequency_mhz, "frequency_mhz", positive=True) * 1e6 * f(length_m, "length_m", positive=True) / f(distance_m, "distance_m", positive=True)
    return dict(value=20 * math.log10(max(e, 1e-12) * 1e6), units="dBuV/m", e_v_per_m=e)


def slot_shielding(slot_length_mm, frequency_mhz):
    """Shielding effectiveness of a slot: SE = 20 log10(lambda / (2 L)) dB (0 dB at L = lambda/2). Sources: PAUL ch.10, WILLIAMS ch.14, ARCH ch.9."""
    wavelength = C0 / (f(frequency_mhz, "frequency_mhz", positive=True) * 1e6)
    ratio = wavelength / (2 * f(slot_length_mm, "slot_length_mm", positive=True) * 1e-3)
    return dict(value=20 * math.log10(ratio) if ratio > 1 else 0.0, units="dB", wavelength_mm=wavelength * 1e3)


def harmonic_envelope(amplitude_v, period_us, pulse_us, rise_ns, frequency_mhz):
    """Trapezoidal pulse spectral envelope: 2 A tau/T flat to f1 = 1/(pi tau), -20 dB/dec to f2 = 1/(pi t_r), -40 dB/dec beyond.
    Returns the envelope amplitude (dBuV) at the requested frequency. Sources: PAUL ch.3, WILLIAMS ch.11."""
    a, t, tau, tr = f(amplitude_v, "amplitude_v", positive=True), f(period_us, "period_us", positive=True) * 1e-6, f(pulse_us, "pulse_us", positive=True) * 1e-6, f(rise_ns, "rise_ns", positive=True) * 1e-9
    freq = f(frequency_mhz, "frequency_mhz", positive=True) * 1e6
    f1, f2 = 1 / (math.pi * tau), 1 / (math.pi * tr)
    level = 2 * a * tau / t
    if freq > f1:
        level *= f1 / freq
    if freq > f2:
        level *= f2 / freq
    return dict(value=20 * math.log10(level * 1e6), units="dBuV", f1_mhz=f1 / 1e6, f2_mhz=f2 / 1e6)


# --- interfaces / digital -------------------------------------------------------------------------
def i2c_pullup(vdd_v, bus_capacitance_pf, rise_time_ns=300, vol_v=0.4, iol_ma=3):
    """I2C pull-up window: R_min = (VDD - VOL)/IOL, R_max = t_r / (0.8473 C_b). Returns R_max - R_min (positive = feasible window).
    Sources: AOE ch.14, WHITE (bus wiring), SCHERZ ch.13; constants from the I2C-bus specification."""
    rmin = (f(vdd_v, "vdd_v", positive=True) - f(vol_v, "vol_v", minimum=0)) / (f(iol_ma, "iol_ma", positive=True) * 1e-3)
    rmax = f(rise_time_ns, "rise_time_ns", positive=True) * 1e-9 / (0.8473 * f(bus_capacitance_pf, "bus_capacitance_pf", positive=True) * 1e-12)
    return dict(value=rmax - rmin, units="ohm", r_min_ohm=rmin, r_max_ohm=rmax)


def rc_time_constant(resistance_ohm, capacitance_nf):
    """tau = R C; 10-90 % rise = 2.2 tau. Sources: JOHNSON93 ch.2, AOE ch.1."""
    tau = f(resistance_ohm, "resistance_ohm", positive=True) * f(capacitance_nf, "capacitance_nf", positive=True) * 1e-9
    return dict(value=tau * 1e9, units="ns", rise_10_90_ns=2.2 * tau * 1e9)


def adc_snr_ideal(bits):
    """SNR = 6.02 N + 1.76 dB for an ideal N-bit converter. Sources: AOE ch.13."""
    return dict(value=6.02 * f(bits, "bits", positive=True) + 1.76, units="dB")


# --- RF -------------------------------------------------------------------------------------------
def return_loss(z_load_ohm, z0_ohm=50):
    """Gamma = (ZL - Z0)/(ZL + Z0); RL = -20 log10|Gamma|; VSWR = (1+|G|)/(1-|G|). Sources: POZAR ch.2, BOWICK ch.4."""
    zl, z0 = f(z_load_ohm, "z_load_ohm", positive=True), f(z0_ohm, "z0_ohm", positive=True)
    gamma = abs((zl - z0) / (zl + z0))
    return dict(value=-20 * math.log10(gamma) if gamma > 0 else 99.0, units="dB", vswr=(1 + gamma) / (1 - gamma) if gamma < 1 else float("inf"), gamma=gamma)


def friis_link_margin(pt_dbm, gt_dbi, gr_dbi, frequency_mhz, distance_m, sensitivity_dbm):
    """Pr = Pt + Gt + Gr - FSPL, FSPL = 20 log10(4 pi d / lambda); value = Pr - sensitivity. Sources: POZAR ch.14, BALANIS ch.2."""
    wavelength = C0 / (f(frequency_mhz, "frequency_mhz", positive=True) * 1e6)
    fspl = 20 * math.log10(4 * math.pi * f(distance_m, "distance_m", positive=True) / wavelength)
    pr = f(pt_dbm, "pt_dbm") + f(gt_dbi, "gt_dbi") + f(gr_dbi, "gr_dbi") - fspl
    return dict(value=pr - f(sensitivity_dbm, "sensitivity_dbm"), units="dB", fspl_db=fspl, pr_dbm=pr)


def cascade_noise_figure(nf_db_list, gain_db_list):
    """Friis cascade: F = F1 + (F2-1)/G1 + (F3-1)/(G1 G2) ... Inputs are comma-separated dB lists. Sources: POZAR ch.10, BOWICK ch.6."""
    nfs = [10 ** (float(x) / 10) for x in str(nf_db_list).split(",")]
    gains = [10 ** (float(x) / 10) for x in str(gain_db_list).split(",")]
    total, running = nfs[0], 1.0
    for nf, g in zip(nfs[1:], gains):
        running *= g
        total += (nf - 1) / running
    return dict(value=10 * math.log10(total), units="dB")


def patch_antenna(frequency_ghz, er, height_mm):
    """Rectangular microstrip patch: W = c/(2f) sqrt(2/(er+1)); er_eff; dL = 0.412 h (er_eff+0.3)(W/h+0.264)/((er_eff-0.258)(W/h+0.8));
    L = c/(2 f sqrt(er_eff)) - 2 dL. Source: BALANIS ch.14 (design procedure)."""
    fr, e, h = f(frequency_ghz, "frequency_ghz", positive=True) * 1e9, f(er, "er", positive=True), f(height_mm, "height_mm", positive=True) * 1e-3
    w = C0 / (2 * fr) * math.sqrt(2 / (e + 1))
    eff = (e + 1) / 2 + (e - 1) / 2 / math.sqrt(1 + 12 * h / w)
    dl = 0.412 * h * (eff + 0.3) * (w / h + 0.264) / ((eff - 0.258) * (w / h + 0.8))
    length = C0 / (2 * fr * math.sqrt(eff)) - 2 * dl
    return dict(value=length * 1e3, units="mm", width_mm=w * 1e3, er_eff=eff, delta_l_mm=dl * 1e3)


def far_field_distance(largest_dimension_mm, frequency_mhz):
    """Far-field boundary R >= 2 D^2 / lambda (also R >> D, R >> lambda). Source: BALANIS ch.2."""
    wavelength = C0 / (f(frequency_mhz, "frequency_mhz", positive=True) * 1e6)
    d = f(largest_dimension_mm, "largest_dimension_mm", positive=True) * 1e-3
    return dict(value=2 * d * d / wavelength, units="m", wavelength_m=wavelength)


# --- mechanical / materials -------------------------------------------------------------------------
def mass_from_volume(volume_mm3, density_g_cm3):
    """m = rho V. Densities: PLA 1.24, PETG 1.27, ABS 1.04, PC 1.20, Nylon 1.14, Al 6061 2.70, FR-4 1.85, Cu 8.96 g/cm^3 (COOMBS materials tables; datasheets govern)."""
    return dict(value=f(volume_mm3, "volume_mm3", minimum=0) * 1e-3 * f(density_g_cm3, "density_g_cm3", positive=True), units="g")


def cantilever_deflection(load_n, length_mm, width_mm, thickness_mm, modulus_gpa):
    """Tip deflection of a rectangular cantilever: d = F L^3 / (3 E I), I = w t^3 / 12; also returns max bending stress 6FL/(w t^2).
    Elementary beam theory (engineering reference; confirm against the actual material datasheet and geometry)."""
    load, length = f(load_n, "load_n", minimum=0), f(length_mm, "length_mm", positive=True) * 1e-3
    width, thickness = f(width_mm, "width_mm", positive=True) * 1e-3, f(thickness_mm, "thickness_mm", positive=True) * 1e-3
    modulus = f(modulus_gpa, "modulus_gpa", positive=True) * 1e9
    inertia = width * thickness ** 3 / 12
    deflection = load * length ** 3 / (3 * modulus * inertia)
    stress = 6 * load * length / (width * thickness ** 2)
    return dict(value=deflection * 1e3, units="mm", stress_mpa=stress / 1e6)


def thermal_resistance_plate(thickness_mm, area_mm2, conductivity_w_mk):
    """Conduction through a plate: R = t / (k A). FR-4 k ~ 0.3 W/mK, copper 385-400 W/mK, aluminum ~ 200 W/mK (COOMBS materials)."""
    r = f(thickness_mm, "thickness_mm", positive=True) * 1e-3 / (f(conductivity_w_mk, "conductivity_w_mk", positive=True) * f(area_mm2, "area_mm2", positive=True) * 1e-6)
    return dict(value=r, units="C/W")


def thermal_via_array(count, drill_mm, plating_um, board_thickness_mm):
    """Thermal resistance of n plated vias in parallel: R = t / (n k_Cu A_barrel), k_Cu = 385 W/mK. Sources: BROOKS ch.5 (via thermal), COOMBS ch.on thermal."""
    area = via_barrel_equivalent_width(drill_mm, plating_um)["barrel_area_mm2"] * 1e-6
    r = f(board_thickness_mm, "board_thickness_mm", positive=True) * 1e-3 / (f(count, "count", positive=True) * 385 * area)
    return dict(value=r, units="C/W", barrel_area_mm2=area * 1e6)


CHECKS = {name: fn for name, fn in globals().items() if callable(fn) and not name.startswith("_")
          and fn.__module__ == __name__ and name not in {"f", "evaluate", "calc", "describe"}}


def describe(check):
    fn = CHECKS.get(check)
    if not fn:
        raise ValueError(f"unknown check {check}; available: {', '.join(sorted(CHECKS))}")
    params = fn.__code__.co_varnames[: fn.__code__.co_argcount]
    defaults = fn.__defaults__ or ()
    required = params[: len(params) - len(defaults)]
    return fn, params, required, dict(zip(params[len(required):], defaults))


def parse_inputs(text):
    inputs = {}
    for item in [x for x in str(text).replace(",", ";").split(";") if x.strip()] if "=" in str(text) else []:
        key, value = item.split("=", 1)
        inputs[key.strip()] = value.strip()
    return inputs


def run_check(check, inputs):
    fn, params, required, defaults = describe(check)
    missing = [p for p in required if p not in inputs]
    if missing:
        raise ValueError(f"{check}: missing inputs {missing}")
    unknown = [k for k in inputs if k not in params]
    if unknown:
        raise ValueError(f"{check}: unknown inputs {unknown}; accepts {list(params)}")
    result = fn(**inputs)
    result["check"] = check
    result["source"] = (fn.__doc__ or "").strip().splitlines()[-1] if fn.__doc__ else ""
    return result


def calc(check, inputs):
    """Ad-hoc calculation for the design loop; prints outputs and the citation line."""
    result = run_check(check, inputs)
    doc = (CHECKS[check].__doc__ or "").strip()
    lines = [f"{check}: {result['value']:.6g} {result['units']}"]
    lines += [f"  {k} = {v:.6g}" if isinstance(v, float) else f"  {k} = {v}" for k, v in result.items() if k not in {"value", "units", "check", "source"}]
    lines.append("  " + doc.replace("\n", "\n  "))
    return "\n".join(lines)


def evaluate(directory):
    """design/rules.tsv: id, check, inputs (k=v;k=v), op, limit, units, traces, source."""
    directory = Path(directory).resolve()
    rows = table(directory / "rules.tsv", ("id", "check", "inputs", "op", "limit", "units", "traces", "source"))
    assert len({r["id"] for r in rows}) == len(rows), "duplicate rule ids"
    passed = 0
    for row in rows:
        traces(row["traces"])
        result = run_check(row["check"], parse_inputs(row["inputs"]))
        if row["units"] != "-" and row["units"] != result["units"]:
            raise ValueError(f"{row['id']}: units {row['units']} differ from the calculation's {result['units']}")
        ok, margin = compare(f"{result['value']:.9g}", row["op"], row["limit"])
        passed += ok
        extras = " ".join(f"{k}={v:.4g}" if isinstance(v, float) else f"{k}={v}" for k, v in result.items() if k not in {"value", "units", "check", "source"})
        DETAILS.append(f"{row['id']}: {result['value']:.6g} {result['units']} margin={margin} {'PASS' if ok else 'FAIL'}")
        DETAILS.append(f"  {row['check']}({row['inputs']}) {extras} cites={row['source']}")
    return f"RULES: {passed}/{len(rows)}", passed == len(rows)
