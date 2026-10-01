# Switching Power Supply Design (3rd ed.) — Anvil rulebook, PART 2 (Ch. 7 §7.6 to end, Ch. 8-17, Appendix)

## 0. Citation

[1] A. I. Pressman, K. Billings, and T. Morey, *Switching Power Supply Design*, 3rd ed. New York, NY, USA: McGraw-Hill, 2009. ISBN 978-0-07-159432-5 (eBook; MHID 0-07-159432-9); print edition ISBN 978-0-07-148272-1 (MHID 0-07-148272-5).

Extraction source: text file lines 9000–17886 (end). Part 1 (lines 1–9000: Ch. 1–6 and Ch. 7 §7.1–7.5) is extracted by a separate agent.

Chapters covered by THIS extraction:
- Ch. 7 Transformers and Magnetic Design — §7.6 to end (Area Product method; signal, common-mode, series-mode and rod-core line-filter inductors; chokes with DC bias; choke materials; gapped-ferrite, Kool Mu toroid, iron-powder/Kool Mu E-core and swinging-choke design examples)
- Ch. 8 Bipolar Power Transistor Base Drive Circuits (complete)
- Ch. 9 MOSFET and IGBT Power Transistors and Gate Drive Requirements (complete)
- Ch. 10 Magnetic-Amplifier Postregulators (complete)
- Ch. 11 Turn-On/Turn-Off Switching Losses and Load-Line-Shaping Snubbers (complete)
- Ch. 12 Feedback Loop Stabilization (complete)
- Ch. 13 Resonant Converters (complete)
- Ch. 14 Typical Waveforms for Switching Power Supplies (complete)
- Ch. 15 Power Factor and Power Factor Correction (complete)
- Ch. 16 Electronic Ballasts (complete)
- Ch. 17 Low-Input-Voltage Regulators for Laptop Computers and Portable Electronics (complete)
- Appendix (symbols, units, conversion factors); Bibliography (scanned for standards and measurement references)

Chapters NOT read here: Ch. 1–6 and Ch. 7 §7.1–7.5 (assigned to the part-1 agent; lines 8960–8999, the tail of §7.5.6 proximity effect, were read only for context and not mined). Index (lines 16854–17886) skipped — not rule content.

ID scheme: `PRESSMAN-2NNN` (leading 2 = part 2), range PRESSMAN-2001 … PRESSMAN-2270. Page citations use the printed page numbers from the running headers (p.338–p.795), plus section numbers.

Units convention: the author mixes CGS (gauss, oersted, maxwell, cm, circular mils) and SI; formulas are transcribed in the units the author used (stated per row). Conversions: 1 T = 10^4 G, 1 Oe = 79.5 A/m, 1 CM = 5.07e-6 cm^2 (T-2.33/T-2.34). "After Pressman", "TIP" and "~K.B." notes are Billings' third-edition updates and are cited like the main text.

## 1. Design rules

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| PRESSMAN-2001 | magnetics | Area product (AP) figure of merit of a core = effective centre-pole area x one winding window area; indicates transformer power rating and optimum choke core size, also predicts surface area, temperature rise, turns, inductance. | AP = Ae * Aw (cm^4); Ae = effective centre-pole area (cm^2); Aw = one window of an E core (cm^2) | Ae, Aw (cm^2) | E cores: use ONE window. For bobbin-wound parts use the bobbin internal winding area Awb (conservative), both bobbin sections included | calc | p.339, §7.6.1 | high |
| PRESSMAN-2002 | magnetics | When a bobbin is used, compute AP with the bobbin's internal winding area (Awb), not the core window; the bobbin reduces effective AP (EC35: 1.3 cm^4 core -> 1.1 cm^4 with bobbin). | AP = Ae * Awb (cm^4) | Ae (cm^2), Awb (cm^2) | bobbin-wound E cores | calc | p.345-348, §7.6.5.1, Fig. 7.14/7.16 | high |
| PRESSMAN-2003 | magnetics | Inductance of a winding scales with N^2 of the single-turn Al value; normalize any manufacturer Al quoted per 100 or 1000 turns down to one turn first. | Ln = N^2 * Al1 ; Al1 = Aln / N^2 (n = turns at which Aln was quoted, typically 100 or 1000) | N, Al (H/turn^2) | signal-level and CM inductors with no significant DC bias (ungapped or maker-gapped cores; Al includes any gap) | calc | p.340-341, §7.6.3 | high |
| PRESSMAN-2004 | emc | Common-mode line-filter inductor: use the highest-permeability core available (typically > 5,000 mu), preferably a gapless toroid; line-frequency (or DC) current is bucked out by the anti-phase windings so no gap is needed and saturation is not a concern. | mu_i > 5000 | core mu_i | CM chokes with two identical, tightly coupled windings, equal turns, anti-phase for differential current | inspect | p.341-343, §7.6.4.1-7.6.4.2 | high |
| PRESSMAN-2005 | emc | CM choke windings: two identical single-layer windings with insulation between windings and to core to meet safety creepage; multiple layers not recommended because extra inter-winding capacitance lowers self-resonant frequency. | layers = 1 per winding (recommended) | winding layout | toroidal CM chokes in off-line SMPS input filters | inspect | p.343, §7.6.4.2 | high |
| PRESSMAN-2006 | current-carrying | CM choke copper can run at high current density because core loss is negligible and an open single-layer winding cools well. | J = 700 to 1000 A/cm^2 (rms line current) | I_rms (A), wire area (cm^2) | single-layer toroidal CM chokes | calc | p.343, §7.6.4.2 | high |
| PRESSMAN-2007 | emc | CM inductance for noise: the two windings act in parallel for common-mode noise, so effective turns = turns of ONE winding. | L_cm = N_one_winding^2 * Al1 | N, Al1 | CM choke | calc | p.344, §7.6.4.2 | high |
| PRESSMAN-2008 | emc | Final CM choke inductance / Y-capacitor values must be set by measuring conducted RFI with a spectrum analyzer on the final-standard build (including chassis/box, heat sinks, switching devices and mounting hardware); adjust C1/C2 within limits, else use a larger core. | — | conducted-emission scan | prototype stage; patient-connected medical supplies have stringent ground-return (leakage) current limits that cap C1/C2, so expect much larger CM chokes | measure | p.344, §7.6.4.2 TIP | high |
| PRESSMAN-2009 | emc | E-core CM chokes: expect far lower and more variable inductance than a toroid because the mated halves leave an unavoidable small gap; a 5000-perm material may lose as much as 60% permeability in E-core form (lapped, matched-pair cores assembled clean retain more). | mu_eff >= 0.4 * mu_i (worst case, 5000-perm material) | mu_i | two-piece E cores, CM chokes | calc | p.344, §7.6.4.3 TIP | high |
| PRESSMAN-2010 | thermal | Winding dissipation limit from thermal resistance of the wound part: Rth from AP (Fig. 7.14, free air, 25 C ambient) at the chosen temperature rise. | Wcu = dT / Rth (W); example EC35 with bobbin AP = 1.1 cm^4, dT = 30 C -> Rth = 20 C/W -> Wcu = 1.5 W | AP (cm^4), dT (C) | standard fully wound E cores, free air, 25 C ambient; core loss assumed zero (CM chokes) | calc | p.347-348, §7.6.5.2, Fig. 7.14 (graph) | high |
| PRESSMAN-2011 | magnetics | Maximum winding resistance from permitted copper loss and rms current. | Rw = Wcu / I_rms^2 ; example 1.5 W / (5 A)^2 = 60 mOhm total (2 x 30 mOhm for a CM choke) | Wcu (W), I_rms (A) | 60 Hz CM filter at 5 A rms | calc | p.348, §7.6.5.3 | high |
| PRESSMAN-2012 | magnetics | Round magnet wire packing factor (copper fraction of usable window) is typically 60%. | Acu = 0.6 * Aw | Aw (cm^2) | round magnet wire, allowing for wire insulation and round-wire voids | calc | p.349-350, §7.6.5.5 | high |
| PRESSMAN-2013 | magnetics | Full-bobbin turns for a target winding resistance: resistance of a fully wound bobbin rises as N^2 (doubling turns halves each wire's area). | Rx = rho * MLT / Acu ; N = (Rw / Rx)^(1/2) ; Acu_wire = Acu / N. Example: rho(70 C) = 1.9 uOhm*cm, MLT = 5.02 cm, Acu = 0.18 cm^2 -> Rx = 53 uOhm; Rw = 30 mOhm -> N = 24; Acu_wire = 0.0075 cm^2 (18-19 AWG) | rho (Ohm*cm), MLT (cm), Acu (cm^2), Rw (Ohm) | fully filled bobbin, one winding section | calc | p.351-352, §7.6.5.5 | high |
| PRESSMAN-2014 | magnetics | Winding resistance from length and wire table. | Rcu = N * MLT(cm) * (Ohm/cm of wire at temperature). Example 24 * 5.02 * 0.00024 = 29 mOhm per half (18 AWG) | N, MLT (cm), Ohm/cm | any winding | calc | p.352, §7.6.5.5 | high |
| PRESSMAN-2015 | materials | AWG step rule: +3 AWG halves copper area (two 18 AWG = one 15 AWG; two 20 AWG = one 17 AWG). | A(AWG+3) = A(AWG)/2 | AWG | whole AWG table | calc | p.346-349, Table 7.9 note, §7.6.5.4 TIP | high |
| PRESSMAN-2016 | magnetics | Series-mode (differential) line inductor L2 must not saturate at the peak line (or peak rectifier-pulse) current; with capacitive-input rectifiers measure the actual peak current, compute peak flux density, and provide a 30% safety margin for component and line-impedance variation. | I_design >= 1.3 * I_peak_measured ; B_pk(I_design) < B_sat | I_peak (A), core B-H data | off-line capacitive-input rectifier; in DC/DC use max DC current; design L2 as a choke (Section 7.7) using peak forced AC current in place of DC | measure/calc | p.353, §7.6.6 TIP | high |
| PRESSMAN-2017 | magnetics | Use a simple open rod-core (ferrite or iron powder rod, spool, bobbin core, or axial ferrite bead) for series-mode filter inductors below about 50 uH; it will not saturate. | 5 uH <= L <= 50 uH -> rod core acceptable | L (uH) | series-mode RFI filter inductors | review | p.353, §7.6.6-7.6.6.1 | high |
| PRESSMAN-2018 | emc | Rod-core RFI inductor self-resonance is raised by spacing turns and insulating the wire from the rod: 1 in x 5/16 in ferrite rod, 15 turns close-packed 17 AWG -> SRF 4 MHz; 15 spaced turns of 20 AWG over 10-mil Mylar -> SRF 6.5 MHz (Fig. 7.17c caption says 6 MHz). Above SRF the inductor is capacitive and noise bypasses it. | f_SRF = 1/(2*pi*sqrt(L*C_iw)); keep f_noise_max < f_SRF | L, C_iw | RFI filter inductors | measure (impedance/phase vs f) | p.354-356, §7.6.6.2, Fig. 7.17 | high |
| PRESSMAN-2019 | magnetics | Rod-core inductors with length/diameter >= 3:1: effective permeability is set by geometry, almost independent of core initial permeability (Fig. 7.18); the large external air path prevents saturation even of high-mu ferrite rods at large DC. | L/d >= 3 -> mu_eff ~ f(L/d) only | rod L/d, mu_i | iron powder chart, applies to high-mu ferrite rods with little error | calc | p.356-357, §7.6.6.3, Fig. 7.18 (graph) | medium |
| PRESSMAN-2020 | current-carrying | Rod-core choke wire current density. | J = 600 to 1000 A/cm^2 | I (A), wire area | rod-core RF chokes (low HF flux swing, low core loss) | calc | p.356, §7.6.6.3 | high |
| PRESSMAN-2021 | magnetics | Magnetizing force in a wound core (CGS). | H = 0.4*pi*N*I / le (oersted); N turns, I (A), le magnetic path length (cm) | N, I (A), le (cm) | DC bias -> Hdc proportional to Idc | calc | p.361, §7.7.3 | high |
| PRESSMAN-2022 | magnetics | Choke inductance from flux-density slope; with material slope (working permeability) fixed, L can only be raised by more centre-pole area (larger core) since N is limited by DC saturation (H rises with N). | L = N * Ae * dB / dI (L in H with Ae in m^2; author lists Ae in mm^2 which gives uH) | N, Ae, dB (T), dI (A) | chokes near saturation: adding turns drives core deeper into saturation | calc | p.362, §7.7.4 | medium |
| PRESSMAN-2023 | magnetics | Core size for a choke is set by the energy storage number. | W = 0.5 * L * I^2 (J) | L (H), I (A, peak/DC bias) | chokes with large DC bias | calc | p.362, §7.7.4 | high |
| PRESSMAN-2024 | magnetics | An ungapped ferrite core saturates (zero incremental permeability, near-zero inductance) at modest DC bias; chokes need either a gapped ferrite or a low-permeability (distributed-gap) powder core. Powder cores support larger dB at the same Hdc (more stored energy, more ripple) but have larger B-H loop area (more core loss per unit dB and f); use iron powder where core loss allows because it costs less. | — | Hdc, material | single-ended DC-biased chokes | review | p.359-361, §7.7.2, Fig. 7.20 | high |
| PRESSMAN-2025 | magnetics | AC flux-density swing in a choke is fixed by applied volt-seconds only (independent of core material, gap, permeability, or DC bias). | dB = V_L * t / (N * Ae) ; dB (T), V_L (V), t (us), Ae (mm^2) | V_L, t, N, Ae | buck: V_L = Vout + V_diode during toff (or Vin - Vout during ton); boost: V_L = Vin during ton | calc | p.364-366, §7.7.5-7.7.6 | high |
| PRESSMAN-2026 | magnetics | Choke saturation margin must cover DC-bias flux plus half the AC swing (plus any over-current). Near saturation there is no back-emf and current rises limited only by winding resistance. | B_dc(I_max_incl_overcurrent) + dB/2 < B_sat | Bdc (T), dB (T), Bsat (T) | all DC-biased chokes | calc | p.365, §7.7.5 TIP; p.371, §7.8.6 | high |
| PRESSMAN-2027 | magnetics | Impending choke saturation shows as a sudden current spike near the positive peak of the triangular ripple waveform (curved B-H slope curves the ripple ramp). | ripple ramp must stay linear up to I_pk | inductor current waveform | CCM chokes | measure (current probe) | p.365, §7.7.5 | high |
| PRESSMAN-2028 | magnetics | An air gap (or lower permeability) reduces the DC-induced flux Bdc only; it does NOT change the AC swing dB nor the material saturation flux density Bsat (it raises the H needed to saturate). | — | — | gapped ferrite and powder cores | review | p.366-367, §7.7.6; p.389 TIP | high |
| PRESSMAN-2029 | thermal | The author's choke/transformer temperature-rise charts assume free air, 45% convection + 55% radiation cooling at emissivity 0.95; always verify the final temperature in the working prototype (layout, airflow, neighbours). | — | — | Figs 7.14, 7.29, 7.32-7.34, 7.37 | measure | p.367, §7.7.7; p.383 | high |
| PRESSMAN-2030 | materials | Typical saturation flux density by choke material family (median, from Fig. 7.22): ferrite ~0.35 T; MPP 0.65-0.8 T; Kool Mu ~1.0 T; iron powder > 1.2 T; High Flux 1.5 T. Bsat is material-specific and nearly independent of the permeability grade. | Bsat: ferrite 0.35 T, MPP 0.65-0.8 T, Kool Mu 1.0 T, iron powder >1.2 T, High Flux 1.5 T | material | general guidance; check maker data | calc | p.370, §7.8.4; p.389, §7.10.2, Fig. 7.22 (graph) | high |
| PRESSMAN-2031 | materials | Typical core loss density at 100 mT peak (200 mT p-p), 50 kHz: gapped ferrite ~30 mW/cm^3; MPP ~100; Kool Mu ~200; iron powder > 2000 mW/cm^3 (65:1 spread). High Bsat materials have the highest loss. | Pv(100 mT pk, 50 kHz): ferrite 30, MPP 100, Kool Mu 200, Fe powder >2000 mW/cm^3 | material, dB, f | generalized trend; use maker curves for design | calc | p.370-371, §7.8.5; p.389, §7.10.3, Fig. 7.23 (graph) | high |
| PRESSMAN-2032 | magnetics | Maker core-loss curves assume push-pull (symmetrical) excitation with peak B = half the p-p swing. For first-quadrant (buck/boost choke, flyback) parts the worked examples enter the chart with B_pk = dB/2 (DC flux adds no first-order loss). The figure notes alternatively say enter with dB and divide the indicated loss by 2. | B_chart = dB_pp / 2 (worked-example method) | dB_pp (T), maker Pv(B,f) curve | single-ended chokes; DC flux ignored for loss | calc | p.371 TIP, p.384-386 TIP, Fig. 7.30, Fig. 7.35 notes | medium |
| PRESSMAN-2033 | magnetics | Gapped ferrite keeps nearly constant permeability with rising H and then saturates abruptly: select an air gap with a good safety margin so saturation does not occur at maximum current plus a reasonable over-current. Powder cores lose permeability progressively and still hold some inductance in transients (better over-current margin). | — | I_max, I_overcurrent, B-H data | choke core choice | calc/review | p.371, §7.8.6; p.393, §7.10.7 | high |
| PRESSMAN-2034 | magnetics | Powder permeability "swings" with DC bias; higher-mu grades roll off at lower H. Kool Mu toroids at 100 Oe: 90-mu grade retains only 25% of initial mu (~22.5 mu effective), 26-mu grade retains > 80% (~20 mu) — working inductance nearly equal. Always correct Al for Hdc (Fig. 7.25) and iterate turns. | mu_eff(H) = mu_i * k(H); at 100 Oe: k(90mu)=0.25, k(26mu)>0.80 | Hdc (Oe), grade | Kool Mu toroids; iron powder similar | calc | p.372-373, §7.8.7, Fig. 7.25 (graph) | high |
| PRESSMAN-2035 | reliability | Iron powder cores age (binder-related) faster than other powders at high temperature, notably above 90 C; check maker high-temperature aging data and keep the design well inside the temperature limit. | T_core <= 90 C unless maker aging data supports higher | core hot-spot temp (C) | iron powder chokes | review | p.374, §7.8.8; p.394, §7.10.9 TIP | high |
| PRESSMAN-2036 | magnetics | Material choice by AC stress: low AC stress (60 Hz line chokes, small ripple, low f) -> copper-loss limited -> high-mu iron powder or gapped Si-iron laminations (high Bsat, few turns). High AC stress (high-V, high-f regulators, boost PFC chokes) -> core-loss limited -> MPP, Kool Mu, gapped ferrite. In between: compute both losses and iterate; Kool Mu loss is nearly constant across its mu range. | — | dI/Idc, f, Vt | chokes | calc | p.368-369, §7.8.1-7.8.3; p.391-393, §7.10.4-7.10.6; p.374, §7.8.10 | high |
| PRESSMAN-2037 | magnetics | Toroids cannot practically be gapped (not for gapped-ferrite designs); MPP only in toroids (at time of writing); E cores, C cores and blocks suit many-turn and high-current (copper strip) windings. | — | core shape | choke core geometry | review | p.374, §7.8.9; p.393-394, §7.10.8 | high |
| PRESSMAN-2038 | magnetics | Gapped-ferrite choke: the gap swamps core reluctance (ferrite mu 2000-6000), so initial permeability of the ferrite barely matters; no advantage in buying costly high-mu low-loss ferrite for gapped chokes. Typical effective permeability for chokes 10-500 mu. | mu_eff = 10 to 500 (choke range) | — | gapped ferrite chokes | review | p.378 TIP, p.387, p.394, §7.10.9 | high |
| PRESSMAN-2039 | magnetics | Buck choke inductance for a target p-p ripple, computed from the off-time (output held constant by loop). | L = (Vout + Vd) * toff / dI_pp ; ton = T * Vout/Vin. Example: 25 V->5 V, 25 kHz (T = 40 us): ton = 8 us, toff = 32 us, V_L = 5.6 V, dI = 2 A (20% of 10 A) -> L = 87 uH (use 90 uH) | Vin, Vout, Vd, f, dI | CCM buck at max Vin, full load | calc | p.376-377, §7.9.2 | high |
| PRESSMAN-2040 | magnetics | Gapped-ferrite E-core choke nomogram (Fig. 7.26) basis: 20 C ambient, 30 C rise, Bm = 250 mT, copper packing factor 0.6, AP from bobbin window. Example 10 A / 90 uH -> AP ~ 1.5 cm^4 -> EC41 (AP 2.4) chosen over EC35 (1.3). | Bmax = 250 mT (ferrite choke design limit) | I (A), L (uH) | gapped ferrite E cores | calc | p.375-378, §7.9.1-7.9.3, Fig. 7.26 (graph) | high |
| PRESSMAN-2041 | magnetics | Minimum turns so the choke does not exceed Bmax at peak current. | N_min = L * I_max * 10^4 / (B_max * Ae) ; L (H), I_max (A), B_max (T), Ae (cm^2 in the worked numbers; text labels mm^2). Example: 90e-6 * 11 * 1e4 / (0.25 * 1.06) = 37 turns | L, I_max = Idc + dI/2, B_max, Ae | gapped ferrite choke | calc | p.378, §7.9.4 | high |
| PRESSMAN-2042 | magnetics | Total air-gap length for a gapped-ferrite choke (gap reluctance dominant, fringing neglected). | g = mu0 * mu_r * N^2 * Ae / L (SI: m, m^2, H); mu0 = 4*pi*1e-7, mu_r = 1. Example N = 37, Ae = 1.06 cm^2, L = 90 uH -> g = 2.0 mm total (0.078 in) = 1 mm butt gap per leg set | N, Ae, L | adjust empirically for fringing and neglected core mu | calc | p.378-380, §7.9.5 | high |
| PRESSMAN-2043 | emc | Confine the gap to the centre pole to minimize external field; a butt gap across all legs is acceptable when ripple is small. A copper screen (band) around the gapped region reduces radiated EMI and fringing. With large AC stress, fringing causes eddy/skin hot spots in wire near the gap; spreading the gap (butt gap across core) reduces hot spots. | butt gap per leg = g_total/2 | — | gapped ferrite E cores | inspect | p.379-380, §7.9.5 TIP, Fig. 7.27 | high |
| PRESSMAN-2044 | magnetics | Choke wire selection: fill the bobbin completely with the required turns using the largest wire that fits (minimum DC copper loss, skin/proximity negligible at small ripple). Exception: PFC chokes with significant HF ripple — include skin effect. Multiple thinner strands of equal area ease winding and improve packing. | d = (Aw * Ku / N)^(1/2) ; d (mm), Aw (mm^2), Ku = 0.6 round wire. Example EC41: Aw = 138 mm^2, N = 37 -> d = 1.5 mm (15 AWG) | Aw, Ku, N | E-core bobbins | calc | p.380-382, §7.9.6-7.9.7, Fig. 7.28 | high |
| PRESSMAN-2045 | magnetics | Copper resistance temperature coefficient: about +0.43%/C above the 20 C value; resistance is 34% higher at 100 C. Compute copper loss at working temperature; measure DC resistance after winding (winding stress and packing vary). | R(T) = R20 * (1 + 0.0043*(T - 20)) ; R100 = 1.34 * R20 | R20 (Ohm), T (C) | copper windings | calc/measure | p.382, §7.9.8 | high |
| PRESSMAN-2046 | magnetics | Winding length from mean bobbin diameter; choke copper loss from DC current when ripple is small. | MLT = pi * d_b ; l_w = MLT * N ; P_cu = I_dc^2 * R_c. Example EC41: d_b = 2 cm, N = 37 -> l_w = 233 cm; 14 AWG 83-110 uOhm/cm (20-100 C) -> Rc = 19.3-25.8 mOhm -> P = 1.9-2.6 W at 10 A | d_b (cm), N, Ohm/cm, I_dc | chokes with small ripple | calc | p.382-383, §7.9.8-7.9.9 | high |
| PRESSMAN-2047 | thermal | Area-product temperature-rise prediction for wound E cores (Fig. 7.29): AP -> wound surface area; total dissipation + surface area -> rise. Example EC41 with bobbin (AP ~1.6 cm^4) -> 42 cm^2; 2.6 W -> ~40 C rise (exceeds 30 C target because bobbin reduced window). | dT = f(P_total, A_surface) (graph); A_surface = f(AP) | AP (cm^4), P_total (W) | free air, "scrapless" E core geometry | calc | p.383-384, §7.9.10, Fig. 7.29 (graph) | medium |
| PRESSMAN-2048 | magnetics | Verify ferrite choke core loss after copper design: example Bac = 5.6 V * 32 us / (37 * 71 mm^2) = 68 mT (680 G) p-p -> 340 G chart peak; ferrite at 20 kHz < 2 mW/cm^3; EC41 10.8 cm^3 -> < 22 mW (negligible). Ferrite core loss is usually negligible for chokes except at high frequency / large ripple; ALWAYS compute core loss for iron powder and add to copper loss. (Book uses Ae = 71 mm^2 here vs 1.06 cm^2 for turns and 1.21 cm^2 in Table 7.10 — inconsistent source numbers.) | P_core = Pv(B_chart, f) * Ve | dB, f, Ve (cm^3) | gapped ferrite vs iron powder chokes | calc | p.384-387, §7.9.11, Fig. 7.30 | high |
| PRESSMAN-2049 | materials | Core loss density at 700 G peak (1400 G p-p), 50 kHz, by material (Fig. 7.31): ferrite type P (mu_r 2500): 100 mW/cm^3; MPP 14 mu and Kool Mu 60 mu: 500; MPP 60 mu: 1100; iron powder #2 (10 mu): 2100; #34 (33 mu): 5000; #60 (60 mu): 10,000 mW/cm^3. Within a powder family higher mu = higher loss (exceptions exist). | see table T-2.4 | material, grade | 50 kHz, 70 mT peak | calc | p.390-391, §7.10.3, Fig. 7.31 | high |
| PRESSMAN-2050 | magnetics | Energy storage number for choke core sizing (charts use mJ and mH). | W = 0.5 * L * I^2 ; W (mJ), L (mH), I = mean DC load current (A). Examples: 1.2 mH, 10 A -> 60 mJ; 0.666 mH, 10 A -> 33.3 mJ | L, I_dc | continuous-mode chokes and flyback cores | calc | p.395-396, §7.11.2; p.406, §7.12.2.2 | high |
| PRESSMAN-2051 | magnetics | Core size from energy storage via AP chart with temperature rise as parameter (Kool Mu toroids Fig. 7.32, 20-60 C; standard E cores Fig. 7.37). Example: 60 mJ at 40 C rise -> AP 28 cm^4 -> 77868 toroid (AP 31.8). Where core loss is expected to be significant, select from a lower temperature-rise line (e.g. 30 C instead of 40 C) to leave margin: 33.3 mJ -> AP 14 cm^4 -> E220 (AP 14.2). | AP_required = f(W, dT) (graph); pick next larger standard core | W (mJ), dT (C) | toroids and E cores differ (E-core surface slightly larger for same AP -> slightly lower rise) | calc | p.396-397, §7.11.3.2; p.406-407, §7.12.2.3, Figs. 7.32, 7.37 (graph) | medium |
| PRESSMAN-2052 | magnetics | Powder-core turns are iterative: N = sqrt(L/Al) at initial mu, then compute Hdc = 0.4*pi*N*I/MPL, derate Al by the permeability-vs-H curve and recompute N; repeat until converged. Example 77868 #26 Kool Mu: Al = 30 mH/1000 turns (30 nH/turn^2) -> N = 200; Hdc = 0.4*pi*200*10/20 = 126 Oe -> mu falls to 85% -> Al = 25.5 nH -> N must increase (book's printed 69/70 turns does not follow from its own inputs). | N_k+1 = sqrt(L / (Al0 * k(H(N_k)))) ; H (Oe) = 0.4*pi*N*I/MPL(cm) | L, Al0, I, MPL, k(H) curve | powder cores (Kool Mu, MPP, iron powder) | calc | p.397-399, §7.11.3.3-7.11.3.5, Fig. 7.25 | medium |
| PRESSMAN-2053 | magnetics | Toroid round-wire fill factor 40% (leaves ~30% of inner diameter free for the winding shuttle). | A_wire = 0.4 * Aw / N | Aw (cm^2), N | toroidal chokes | calc | p.399-400, §7.11.3.6 TIP | high |
| PRESSMAN-2054 | thermal | Temperature rise by surface energy density (Fig. 7.33): total loss / wound surface area -> rise, with ambient as parameter. Example 8 W / 203 cm^2 = 0.039 W/cm^2 -> 31 C rise from 25 C ambient; AP method (Fig. 7.34, toroids): AP 31.8 cm^4, 8 W -> 30 C. | psi = P_total / A_surface (W/cm^2); dT = f(psi) (graph) | P (W), A_surface (cm^2) | free air | calc | p.400-401, §7.11.3.8-7.11.3.9, Figs. 7.33-7.34 (graph) | medium |
| PRESSMAN-2055 | magnetics | Core-loss check for a Kool Mu buck choke: Bac = 5.6 V * 32 us / (70 * 177 mm^2) = 14.6 mT (146 G) p-p -> 73 G chart peak -> < 10 mW/cm^3 at 50 kHz: negligible (a cheaper, lossier iron powder could be used). | Bac = e * toff / (N * Ae) (T; e V, toff us, Ae mm^2) | e, toff, N, Ae | copper-loss-limited toroid | calc | p.401-403, §7.11.3.10, Fig. 7.35 | high |
| PRESSMAN-2056 | magnetics | Boost choke inductance for p-p ripple from on-time. Example: Vin 100 V, Vout 200 V, 50 kHz, D = 50%, ton = 10 us, dI = 1.5 A (15% of 10 A) -> L = 100 * 10e-6 / 1.5 = 0.666 mH. Boost/PFC chokes see high AC stress -> core-loss limited. | L = Vin * ton / dI_pp | Vin, ton, dI | CCM boost | calc | p.404-405, §7.12.2.1 | high |
| PRESSMAN-2057 | magnetics | Iron powder mix correction of catalogue Al: E220 reference Al (#26) = 275 nH/N^2; #40 factor 0.87 -> 240 nH/N^2 -> N = sqrt(0.666e-3/240e-9) = 53 turns. | Al_mix = Al_#26 * k_mix (k_#40 = 0.87) | Al_ref, k_mix | Micrometals iron powder E cores | calc | p.407, §7.12.2.4, Table 7.12 | high |
| PRESSMAN-2058 | magnetics | Core-loss-limited boost choke on #40 iron powder E220 (worked example): Bac = 100 V * 10 us / (53 * 360 mm^2) = 52.4 mT (524 G); #40 loss at 524 G, 50 kHz = 600 mW/cm^3 (push-pull chart) -> 300 mW/cm^3 single-ended; core loss = 47.7 cm^3 * 0.300 W/cm^3 (book prints 13.4 W; product = 14.3 W) vs copper 2.5 W -> not an optimum design. | P_core = Ve * Pv_chart(B, f) / 2 (single-ended) | V, ton, N, Ae, Ve, Pv curve | iron powder, high AC stress (boost/PFC) | calc | p.409-411, §7.12.2.5, Fig. 7.39 | high |
| PRESSMAN-2059 | magnetics | Optimum choke efficiency is reached when copper loss ~ core loss. If core loss dominates, prefer a lower-permeability, lower-loss mix at the same inductance (raises N, lowers dB and material loss density) rather than just adding turns on the same mix (which over-sizes L and may exceed temperature limits). | P_cu ~= P_core (optimum) | P_cu, P_core | powder-core chokes | calc | p.411-413, §7.12.2.7-7.12.3.4 | high |
| PRESSMAN-2060 | magnetics | Fully wound bobbin: winding resistance scales with the square of the turns ratio when the window stays full. | R2 = R1 * (N2/N1)^2 ; example (69/52)^2 * 0.025 = 0.044 Ohm | R1, N1, N2 | window completely filled in both designs | calc | p.413, §7.12.3.3 | high |
| PRESSMAN-2061 | magnetics | #8 iron powder E220 redesign (worked example): Al = 275 nH * 0.51 = 140 nH/N^2 -> N = 69; Bac = 100*10/(69*360) = 40 mT (400 G); #8 at 400 G, 50 kHz = 190 mW/cm^3 -> 95 single-ended -> 4.53 W core; copper 4.4 W; total 8.9 W -> ~47 C (toroid chart) -> ~40 C for E core: meets 40 C spec, optimum efficiency. | k_#8 = 0.51 of #26 Al | — | 100 V -> 200 V boost, 10 A, 50 kHz, 15% ripple | calc | p.412-413, §7.12.3 | high |
| PRESSMAN-2062 | thermal | An E core has about 15% more surface area than a toroid of the same area product, so its temperature rise is about 15% lower for the same dissipation (use toroid AP chart Fig. 7.34, then x 0.85 for E cores). | dT_E ~= 0.85 * dT_toroid(AP, P) | AP, P_total | free-air chokes | calc | p.413, §7.12.3.4; p.416, §7.12.4.8 | high |
| PRESSMAN-2063 | magnetics | E-core bobbin round-wire fill factor ranges from a perfect (unrealistic) 87% down to 40% depending on construction/insulation; realistic mean 60% (the swinging-choke example uses ~70%). | Ku = 0.6 typical (0.4-0.87 range) | construction | E-core bobbins | calc | p.411, §7.12.2.6; p.420, §7.13.2.5 | high |
| PRESSMAN-2064 | magnetics | With high AC ripple stress use several strands of thinner wire (same total copper area) instead of one large conductor, for skin effect and windability (11-12 AWG is hard to wind on a 55 mm E core). | — | ripple, f | boost/PFC chokes | inspect | p.411, §7.12.2.6; p.416, §7.12.4.6 | high |
| PRESSMAN-2065 | magnetics | Kool Mu: core loss nearly constant across permeability grades, so pick the highest-mu grade available for the core size to minimize turns and copper loss; correct Al for DC bias (#60 at 55 Oe -> 70% of initial). | N = sqrt(L / (Al0 * k(Hdc))) | L, Al0, Hdc | Kool Mu E cores | calc | p.414-415, §7.12.4.2-7.12.4.4 | high |
| PRESSMAN-2066 | magnetics | Kool Mu 5528E #60 boost choke (worked example, same spec as #40/#8 designs): Al0 = 219 nH -> N = 55 -> Hdc = 0.4*pi*55*10/12.5 = 55 Oe -> 153 nH -> N = 66; Bac = 100*10/(66*350) = 43.3 mT (433 G); 60 mW/cm^3 push-pull -> 30 single-ended -> 1.3 W core; 12 AWG (0.037 cm^2, 5.22 mOhm/m), 708 cm -> 0.037 Ohm -> 3.7 W; total 5 W -> 35 C toroid chart -> ~30 C E core. Smaller core and lower total loss than the iron powder designs; copper-loss limited. | — | — | 100 V -> 200 V, 10 A, 50 kHz, dI = 1.5 A | calc | p.413-417, §7.12.4 | high |
| PRESSMAN-2067 | magnetics | Swinging choke: design with a high-mu powder so the working point at full load lies on the curved part of the mu(H) curve; inductance rises at light load, extending the CCM range and reducing light-load ripple. Penalties: more turns, larger core, higher copper loss, smaller saturation margin. | N = H_design * MPL / (0.4*pi*I_full) ; L(I) = N^2 * Al0 * k(H(I)) | H_design (Oe), MPL (cm), I_full (A), k(H) curve | Kool Mu E cores (Fig. 7.40): at 100 Oe, 90-mu keeps 32%, 26-mu keeps > 87% of initial mu | calc | p.417-419, §7.13.1-7.13.2.3 | high |
| PRESSMAN-2068 | magnetics | Swinging choke worked example: 10 A, 1 mH, 40 C -> W = 50 mJ -> AP 16 -> 5530E (AP 15.9, MPL 12.3 cm, MLT 12.4 cm, Awb 3.8 cm^2, Ae 4.17 cm^2, Al0 = 261 nH #60). At 100 Oe/10 A mu = 52% -> N = 98 -> Al = 136 nH -> L = 1.33 mH at 10 A; at 20 A (200 Oe) mu = 25% -> 0.65 mH; at 2 A mu = 100% -> 2.5 mH (5:1 swing). 70% fill -> 13 AWG; 1215 cm, 0.007 Ohm/m -> 0.085 Ohm -> 8.5 W; Rth (Fig. 7.14, AP 16) ~ 4.6 C/W -> 39 C rise; Bac = 5.6*32/(98*417) = 4.38 mT -> < 1 mW/cm^3 (negligible). | L_swing_ratio = k(H_light)/k(H_full) | — | buck 25 V -> 5 V, 25 kHz | calc | p.418-421, §7.13.2 | high |
| PRESSMAN-2069 | components | Bipolar switch base drive must keep the LOWEST-beta device saturated at the highest collector current it must carry (Vce(sat) typically 0.5-3.0 V at max current, min input, lowest beta); size base current to bottom Vce to 0.5-1.0 V at the PEAK of the Ic ramp at max output power and min Vin (critical for DCM flybacks, high peak/average). | Ib_on >= Ic_pk / beta_min | Ic_pk (A), beta_min | bipolar power switches | calc | p.424-425, §8.2.1 | high |
| PRESSMAN-2070 | derating | Allow a 4:1 production spread in bipolar beta: data-sheet Ic-Vce curves are for a typical device; assume beta_min = beta_typ/2 and beta_max = 2*beta_typ. | beta_min = 0.5*beta_typ ; beta_max = 2*beta_typ | beta_typ | bipolar transistors | calc | p.424, §8.2.1, Fig. 8.1 | high |
| PRESSMAN-2071 | components | Avoid bipolar overdrive during the on-time in switching service (it lengthens storage time); use a Baker clamp. (Not a problem in linear regulators.) | — | — | switching applications | review | p.424, §8.2.1 After Pressman | high |
| PRESSMAN-2072 | components | Turn-on base current spike Ib1 of about 2-3x the on-time average, lasting about 2-3% of the minimum on-time, speeds collector current rise. With overdrive factor k the target Ic is reached in t = tau_a * ln(k/(k-1)): k = 2 -> 0.69 tau_a, k = 3 -> 0.4 tau_a (vs 3 tau_a to within 5% with k = 1). Compute overdrive for the nominal-beta device (a 2x-nominal-beta part then sees k = 4). | Ib1_spike = 2-3 x Ib_avg ; t_spike = 0.02-0.03 x ton_min | ton_min, Ib | bipolar turn-on | calc | p.425-426, §8.2.2, Fig. 8.2 | high |
| PRESSMAN-2073 | components | Provide a reverse base current spike Ib2 at turn-off to sweep stored base charge: reduces storage time, allows higher fsw and cuts the turn-off dissipation spike (interval where Ic stays at peak while Vce leaves saturation). Maker switching-time curves use Ic/Ib1 and Ic/Ib2 of 5-10. | Ic/Ib2 = 5-10 (data-sheet test range) | Ib2 | bipolar turn-off | review/measure | p.427, §8.2.3, Fig. 8.3 | high |
| PRESSMAN-2074 | derating | Bipolar Vce ratings: Vceo (base open at turn-off, lowest) < Vcer (50-100 Ohm base-emitter resistor) < Vcev (highest). Vcev applies only if the drive applies -1 to -5 V reverse base bias at turn-off lasting at least as long as the leakage-inductance spike. | V_ce_peak <= Vceo (no reverse bias) or <= Vcev (with -1..-5 V bias for the spike duration) | V_ce_peak incl. leakage spike | bipolar switches | calc/measure | p.427-429, §8.2.4, Fig. 8.4 | high |
| PRESSMAN-2075 | reliability | Reverse-bias SOA (RBSOA): the turn-off Ic-Vce locus must never cross the boundary — even a single crossing may destroy the transistor (current crowding, local hot spots). With -1 to -5 V reverse bias the larger Vcev boundary applies; with Vbe = 0 a smaller boundary applies. | locus(Ic, Vce) inside RBSOA at all times | turn-off Ic-Vce trajectory | bipolar switches | measure (Vce vs Ic X-Y) | p.430, Fig. 8.4 | high |
| PRESSMAN-2076 | power | Drive efficiency: derive high base current through a voltage step-down/current step-up drive transformer from the housekeeping rail, not directly from a low-voltage source. Example 2N6836 (15 A, Vcev 850 V, min gain 5 at 15 A -> 3 A base) from a 6 V source at 80% duty = 14.4 W (unacceptable); a 10:1 transformer delivers 3 A to the base for 300 mA from the housekeeping supply. | P_drive = V_src * Ib * D ; I_primary = Ib * Ns/Np | V_src, Ib, D, Np/Ns | bipolar base drive | calc | p.429-431, §8.2.6, §8.3 | high |
| PRESSMAN-2077 | components | Transformer-coupled base drive: turns ratio 10 or more; secondary delivers about 1 to 1.8 V to the base; primary fed from 12-18 V housekeeping supply; also crosses the isolation boundary (PWM on output common, switch on input common). | Np/Ns >= 10 (typical) ; Vs = 1-1.8 V | — | off-line bipolar supplies | review | p.430-431, §8.3 | high |
| PRESSMAN-2078 | components | Without Baker clamping a hard-saturated fast bipolar has forward-biased B-C junction (2N6836 at Ic = 10 A, forced beta 5, Tj = 100 C: Vce ~0.2 V, Vbe ~0.9 V -> 0.7 V forward bias) and 3 us storage time. A Baker clamp limits B-C forward bias to 0.2-0.4 V and cuts storage time by 5-10x, working over a 4:1 beta spread. | V_BC_forward <= 0.4 V | Vbe, Vce | bipolar switches | measure | p.431, §8.3, Fig. 8.5 | high |
| PRESSMAN-2079 | components | Baker clamp diode D3 (collector) must be a high-voltage fast-recovery diode rated for 2x supply voltage plus leakage spike (forward converter); series base diode D2 is fast-recovery but sees only ~0.8 V reverse. Example MUR450 (450 V, 3 A, 75 ns) for D3 and MUR405 (50 V, 4 A, 35 ns) for D2. Add reach-around diode D1 across D2 to allow reverse base current. | V_RRM(D3) >= 2*Vdc_max + V_leakage_spike | Vdc_max, spike | Baker-clamped bipolar in forward converter | calc | p.433-434, §8.3.1 | high |
| PRESSMAN-2080 | components | Baker clamp raises Vce(on) to about 1 V (vs 0.2-0.5 V unclamped): more conduction loss but more than offset by reduced turn-off switching loss. Worst-case check: I1 = 3.5 A, max-beta Q needs 0.5 A, D2 rise 0.61 V (100 C, 0.5 A), D3 drop 0.95 V (3 A, 100 C) -> B-C forward bias 0.34 V (acceptable). | V_BC = V_D3(I3) - V_D2(Ib) must stay < ~0.4 V | diode Vf at corner currents/temps | Baker clamp | calc | p.434, §8.3.1, Table 8.1 | high |
| PRESSMAN-2081 | components | Transformer-driven Baker clamp primary voltage and current limit (Fig. 8.7): keep Vpt well below Vh so R1 acts as a near-constant current source against temperature drift of Vs. | Vs = Vbe(Q2) + V_D2 = 1.0 + 0.75 = 1.75 V ; Vpt = (Np/Ns)*Vs + Vce(Q1) ~= (Np/Ns)*1.75 + 1.0 (Eq. 8.1) ; Ip = (Vh - (Np/Ns)*Vs - 1.0)/R1 (Eq. 8.2) ; dIpn/Ipn = 5*dVs/(Vh - 9.75) for Np/Ns = 5 (Eq. 8.3) ; R1 = 5.25/Ipn for Vh = 15 V (Eq. 8.4b) | Vh, Np/Ns, Vs, dVs | dVs = 0.1 V and 10% current tolerance -> Vh = 14.75 ~ 15 V | calc | p.435-437, §8.3.2.1 | high |
| PRESSMAN-2082 | components | Reverse base current from drive-transformer flyback: pick primary magnetizing inductance so magnetizing current ramps to Ipn/2 at end of on-time, making reverse base current equal to the forward base current just before turn-off; clamp the base negative with two series diodes (~ -1.6 V) so residual transformer energy cannot over-drive the base-emitter junction in reverse. | Ipm = (Vpt - 1)*ton/Lm = Ipn/2 ; V_base_clamp ~ -1.6 V (2 diodes) | Vpt, ton_min, Lm | transformer-coupled base drive | calc | p.437-439, §8.3.2.2-8.3.2.3, Fig. 8.8 | high |
| PRESSMAN-2083 | components | Worked example (Baker-clamp drive, 500 W forward, 115 VAC): Vdc_min = 0.85*160 = 136 V; Ipft = 3.13*Po/Vdc_min = 11.5 A (Eq. 2.28); 2N6836 beta_min 7 at 11.5 A -> Ib = 1.64 A; Np/Ns = 5 -> 0.328 A; R1 = 5.25/(2*0.328) = 8.0 Ohm; 50 kHz, ton_max = 0.8*T/2 = 8 us, ton_min (+/-10% line) = 6.4 us; Lm = (Np/Ns)*Vs*ton_min/0.328 = 171 uH; Ferroxcube 1408PA3C8 pot core Al = 315 mH/1000 T -> Np = 1000*sqrt(0.171/315) = 23 -> 25 turns, Ns = 5; 8.2 At < 12 At saturation knee; Q1 peak 656 mA -> 2N2222A. | Lm = (Np/Ns)*Vs*ton_min / Ipm | — | — | calc | p.439-440, §8.3.2.4, Fig. 8.9 | high |
| PRESSMAN-2084 | magnetics | Drive-transformer core saturation check: magnetizing ampere-turns must stay below the core's saturation knee (1408 pot core, Al = 315: knee ~12 At). | Ipm * Np < At_knee | Ipm, Np, Al-vs-At curve | small pot-core gate/base drive transformers | calc | p.440, §8.3.2.4, Fig. 8.9 (graph) | high |
| PRESSMAN-2085 | components | Centre-tapped-secondary "transformer Baker clamp" (Fig. 8.10): Vce = 2*Vbe - V_D3 ~ 1.0 V = Vbe (no B-C forward bias), one diode fewer, no reach-around diode; Vs ~1.0 V instead of 1.75 V allows ~2x turns ratio, halving primary current. Example: Np/Ns1 = 10, Vce(Q1) = 0.5 V -> Vpt = 10.5 V, Vh = 15.75 V, primary load 164 mA, R1 = 5.25/0.328 = 16 Ohm, Lm = 10*6.4us/0.164 = 390 uH -> 35 T; use Np = 40, Ns1 = Ns2 = 4 (avoid half turns on pot cores) -> Lm 509 uH, Ipm 126 mA, reverse base 1.26 A, 5.04 At. | Vce(Q2) = VNs1 + VNs2 - V_D3 = 2*Vbe - V_D3 | — | bipolar base drive | calc | p.440-442, §8.3.3 | high |
| PRESSMAN-2086 | components | Avoid half turns on pot-core windings (odd undesirable effects); round to whole turns and recompute Lm and magnetizing current. | turns integer | — | pot cores | inspect | p.442, §8.3.3.1 | high |
| PRESSMAN-2087 | components | Darlington output stage is inherently Baker clamped, but IC Darlingtons show 3-4 us storage time from the saturating driver transistor; for less storage use discrete driver (UHF device) + output transistor; most IC Darlingtons include a reach-around diode for reverse base current. | t_s(IC Darlington) up to 3-4 us | — | Darlington switches | review | p.442-443, §8.3.4, Fig. 8.11 | high |
| PRESSMAN-2088 | components | Proportional base drive (Fig. 8.12) for collector currents above 5-8 A: current-transformer feedback gives base current proportional to collector current (never overdriven at light load), low drive dissipation. Design: Nb/Nc = beta_min (typically 5-10) (Eq. 8.5); Np = Vh*Nb/2 for a 2 V negative turn-off pulse (Eq. 8.6); Nc = 1 turn; I1 = Ic*Nc/Np (Eq. 8.7b); R1 = (Vh/Ic)*(Np/Nc) (Eq. 8.8b); C1 = 4*(Ic/Vh)*(Nc/Np)*toff (Eq. 8.9b), toff ~0.30 us for high-current bipolars; recharge C1 to within 5% of Vh: 3*R1*C1 <= minimum Q1 off-time (else add emitter-follower recharge, Fig. 8.13); Lp = ton_min / (2*(1/R1 + C1/ton_min)) (Eq. 8.11). | see formulas | Ic_max, beta_min, Vh, toff, ton_min | bipolar Ic > 5-8 A; requires well-defined gain selection (high-gain parts can be overdriven) | calc | p.443-450, §8.3.5.1-8.3.5.4 | high |
| PRESSMAN-2089 | components | Proportional drive worked example: 12 A collector, 145 V min DC -> Po = 12*145/3.13 = 556 W; beta_min 6 -> Nb/Nc = 6 (Nc = 1, Nb = 6); Vh = 12 V -> Np/Nb = 6 -> Np = 36; I1 = 0.33 A; R1 = 36 Ohm; toff 0.3 us -> C1 = 0.033 uF; 50 kHz, ton = 10 us -> Lp = 162 uH -> Al = (1000/36)^2 * 0.162 = 125 mH/1000 T -> 1408PA3C8-100 (Al 100) acceptable. | — | — | forward converter, 115 VAC off-line | calc | p.449-450, §8.3.5.5 | high |
| PRESSMAN-2090 | components | Wood base drive (Fig. 8.14): drive-transformer secondary ~4 V (about 5 V when a blocking diode D3 is added for SG3524 drive); R1 limits base current for lowest-beta device at max Ic; C1-charged auxiliary transistor pulls base to about -2 to -3 V at dead time for fast turn-off. | R1 = (Vs - Vbe)/Ib_max = (Vs - 1)*beta_min/Ic_max (Eq. 8.12) | Vs, beta_min, Ic_max | up to 1000 W off-line (Wood), bridges and push-pull | calc | p.450-453, §8.3.6 | high |
| PRESSMAN-2091 | components | Driving a base transformer directly from UC3525A outputs: output drivers drop about 2 V at 200 mA; for Vbe = 1 V and 10:1 gain the primary sees 10 V; keep ~6 V across the primary current-limit resistor (Vh = 20 V) for near-constant current: R1 = 6/0.2 = 30 Ohm -> 2 A base current. Scheme shorts the base at turn-off (no reverse bias, so Vcev not available) and gives the same base current at all loads (overdrive and long turn-off at light load). | R1 = V_R1 / I_p,limit | driver drop, Vh | half bridge / push-pull bipolar drive | calc | p.453-454, §8.3.6, Fig. 8.15 | high |
| PRESSMAN-2092 | components | DC-coupled totem-pole base drive (Fig. 8.17): 2N2222A/2N2907A emitter-follower totem pole sources/sinks up to 800 mA (300 MHz devices); 3.3 V zener + capacitor gives about -3 V turn-off bias; base current = (Vh - Vce(Q2) - Vbe(Q4) - VZ1)/R2. | Ib = (Vh - Vce - Vbe - Vz)/R2 | Vh, Vz = 3.3 V | low/medium power bipolar | calc | p.454-455, §8.3.6 | high |
| PRESSMAN-2093 | components | Large power MOSFETs present several nF of effective gate capacitance (IGBTs > 1 nF, and lower Miller effect at high voltage); gate drive design for large devices is demanding despite negligible DC gate current (nA at 10 V). | C_g,eff: MOSFET several nF; IGBT > 1 nF | Ciss, Crss | power MOSFET/IGBT | calc | p.459, §9.1.3; p.464, §9.2.3 | high |
| PRESSMAN-2094 | emc | Fit a series gate resistor near the MOSFET/IGBT gate terminal to reduce noise pickup and parasitic oscillation; high-impedance gates are vulnerable to capacitively injected noise despite the ~2.5 V threshold. In high-voltage/high-power stages apply a few volts of negative gate bias during the off period (important for IGBTs against latch-up). | R_g at gate pin; V_gs,off = -few V (HV/HP) | layout | FET/IGBT gate drive | inspect | p.461, §9.2.1 After Pressman | high |
| PRESSMAN-2095 | components | Vgs = 10 V drives a MOSFET onto its rds slope; more gate voltage barely lowers Vds unless near maximum rated current. To get Vds(on) ~1 V at Id choose a device whose continuous rating is about 3-5x Id (rds is inversely proportional to current rating). | Id_rating >= 3 to 5 x Id_operating (for Vds(on) ~ 1 V) | Id, rds | MOSFET switch selection | calc | p.463, §9.2.2 | high |
| PRESSMAN-2096 | power | MOSFET conduction loss = Id*Vds*(ton/T); switching loss is often negligible because turn-off is so fast, so MOSFETs can run with Vds(on) up to 2-3 V (vs <= 1 V customary for bipolars, whose on-loss is only 1/2-1/3 of total). Example: MTM7N45 (rds 0.8 Ohm) at 7 A, 10 V gate -> Vds = 7 V -> 49 W (unacceptable); MTM15N40 (0.4 Ohm) -> 2.5 V at 7 A. | P_on = Id * Vds(on) * ton/T ; Vds(on) <= 2-3 V | Id, rds(Tj), D | hard-switched MOSFET | calc | p.463-464, §9.2.2 | high |
| PRESSMAN-2097 | components | Gate drive current = charge of Ciss plus Miller current through Crss (which swings Vdc + 10 V). Miller current can be up to ~10x the Ciss current. | I1 = Ciss * 10 V / tr (Eq. 9.1) ; I2 = Crss * (Vdc + 10) / tr (Eq. 9.2) ; Ig = I1 + I2. Example: MTM7N45, Ciss 1800 pF, Crss 150 pF, Vdc 178 V, tr 50 ns -> I1 = 360 mA, I2 = 564 mA, Ig = 0.924 A (same for turn-off) | Ciss, Crss, Vdc, tr | 10 V gate swing | calc | p.464-466, §9.2.3, Fig. 9.4 | high |
| PRESSMAN-2098 | components | Effective MOSFET input capacitance including Miller multiplication. Example MTH15N20 on a 48 V telecom bus (38-60 V): Cin = 2000 + (70/10)*200 = 3400 pF -> 0.68 A to swing 10 V in 50 ns (may exceed max gate drive current of some devices). | Cin = Ciss + ((Vdc_max + 10)/10) * Crss ; Ig = Cin * 10 V / tr | Ciss, Crss, Vdc_max, tr | low-voltage devices: higher Ciss, lower Crss, less Miller | calc | p.466, §9.2.3 | high |
| PRESSMAN-2099 | emc | Do not switch faster than needed: short drain di/dt and dV/dt cause L*di/dt spikes on ground/supply rails and C*dV/dt current into adjacent nodes; respect device di/dt and dV/dt limits (exceeding them can lock up an IGBT). | di/dt <= device limit ; dV/dt <= device limit | tr, tf, L_stray, C_couple | MOSFET/IGBT | measure | p.467, §9.2.4 | high |
| PRESSMAN-2100 | components | Drain current switches only while the gate crosses from threshold (~2.5 V) to VgI (~5-7 V for full current); 0-2.5 V is pure delay. Hence gate 10-V transition time can be 2-3x the desired drain current transition time, and gate-current estimates from full 10 V swing are 1/2-1/3 of what fast drain edges need. Example: 0-10 V gate in 50 ns -> 2.5 A drain rise in (2.5/10)*50 = 12.5 ns. | t_Id ~= t_gate * (VgI - Vth)/10 V | t_gate, Vth, VgI | MOSFET transfer curve | calc | p.467-468, §9.2.4, Fig. 9.5 | high |
| PRESSMAN-2101 | components | Place gate clamp diodes/zener at the DRIVE end of the series gate resistor (away from the gate pin) and the gate resistor near the gate terminal; manufacturers specify a minimum gate resistor, typically 5-50 Ohm; larger series resistors can allow HF oscillation via drain-gate feedback. | R_g = 5 to 50 Ohm (typ. maker minimum) | R_g | MOSFET/IGBT gate drive | inspect | p.467, §9.2.4; p.485, §9.2.12; p.494 (IGBT) | high |
| PRESSMAN-2102 | components | Gate drivers must actively source AND sink >= 200 mA. A unidirectional PWM output (SG1524: 200 mA source or sink, not both) with only an emitter pull-down resistor turns the MOSFET off too slowly: 1800 + (180/10)*150 = 4500 pF with 200 Ohm -> 3RC = 2.7 us (book prints 270 us) — unusable above ~100 kHz. Use a totem pole (2N2222A/2N2907A: 800 mA, ~60 ns) or a chip with totem-pole outputs (UC1525A). | I_source, I_sink >= 200 mA ; t_fall ~ 3 * R_pd * C_in,eff | R_pd, C_in,eff | PWM-chip-driven MOSFETs | calc | p.468-471, §9.2.5, Fig. 9.6 | high |
| PRESSMAN-2103 | components | Gate-drive transformer fed between UC1525A totem-pole outputs (pins 11, 14): outputs sit ~2 V from rails; for +/-10 V across the primary use Vh ~ 14 V. Two isolated secondaries drive high/low bridge FETs; dead time shorts both outputs to ground. | Vh ~= V_primary + 4 V (2 V per output stage) | V_primary | half/full bridge, push-pull | calc | p.471-472, §9.2.5, Fig. 9.7 | high |
| PRESSMAN-2104 | reliability | MOSFET switching SOA is a rectangle bounded by Idm (pulsed, 2-3x continuous Id) and V(br)dss (plus Tj max); no secondary breakdown (positive rds tempco disperses hot spots); crossing the boundary for more than 1 us during turn-on or turn-off may destroy the device. Bipolar hot spots from current crowding exceed 200 C at failure. | Id_pk <= Idm ; Vds_pk <= V(br)dss (for tr, tf < 1 us) | Id_pk, Vds_pk | MOSFET switching trajectories | measure | p.473-474, §9.2.6, Fig. 9.8 | high |
| PRESSMAN-2105 | derating | MOSFET rds(on) rises with temperature and more so for higher-voltage parts: a 400 V MOSFET at 100 C has 1.6x its 25 C rds. Data-sheet rds is at 25 C case. | rds(100 C) = 1.6 * rds(25 C) (400 V class) | rds25, Vdss class | use Fig. 9.10 for other voltage classes | calc | p.474-475, p.479, Figs. 9.9-9.10 | high |
| PRESSMAN-2106 | components | MOSFET gate threshold Vgsth: specified at Ids = 1 mA or 0.25 mA with Vds = Vgs (maker-dependent); 2:1 production spread; falls ~5% per 25 C rise; drops toward zero under radiation (negative gate bias required to hold off). Turn-on delay shrinks with temperature; switching speed itself is nearly temperature independent. | dVth/Vth = -5% per +25 C | Vgsth, Tj | MOSFETs (radiation: out of scope) | calc | p.475-477, §9.2.7-9.2.8, Figs. 9.11-9.12 | high |
| PRESSMAN-2107 | derating | MOSFET maximum junction temperature 150 C; good design practice derates to 105 C (military) or at most 125 C. Reliability drops typically 50% for each 10 C rise. | Tj_max_design <= 105-125 C (abs max 150 C) | Tj | power MOSFETs | calc | p.478-479, §9.2.9, Fig. 9.14 | high |
| PRESSMAN-2108 | components | Data-sheet continuous Id is a 100%-duty rating at Tc = 100 C reaching Tj = 150 C; it is only a figure of merit, not a selection criterion for switching use. | Id = 50 / (Vds(on)@150C * Rth_jc) | Vds(on), Rth_jc | comparison only | calc | p.478, §9.2.9 | high |
| PRESSMAN-2109 | components | MOSFET selection method 1: pick rds so the on-drop at the flat-topped equivalent primary current is <= 2% of minimum supply voltage (rds taken at operating temperature). Example 150 W forward, Vdc 136-184 V: Ipft = 3.13*150/136 = 3.45 A; Von <= 0.02*136 = 2.72 V -> rds <= 0.79 Ohm at 100 C -> <= 0.49 Ohm at 25 C (x1/1.6). | Ipft * rds(Tj) <= 0.02 * Vdc_min | Ipft (Eqs. 2.9, 2.28, 3.1, 3.7), Vdc_min | push-pull, forward, half/full bridge | calc | p.479, §9.2.9, Table 9.1 | high |
| PRESSMAN-2110 | thermal | MOSFET selection method 2: set a junction temperature for reliability (e.g. 100 C) and a small junction-to-case rise (e.g. 5 C), neglect AC switching loss. Forward converter with ton_max = 0.8*T/2: Irms = Ip*sqrt(ton/T) = 0.632*Ip. Example Ip = 3.45 A, Rth_jc = 0.83 C/W -> rds <= 1.26 Ohm at 100 C (0.78 Ohm at 25 C). | rds(Tj) = dT_jc / (Irms^2 * Rth_jc) ; Irms = 0.632*Ip (D = 0.4) | dT_jc, Irms, Rth_jc | hard-switched forward converter | calc | p.479-480, §9.2.9 | high |
| PRESSMAN-2111 | thermal | Paralleled MOSFETs: static sharing is set by rds; the positive rds tempco alone does not protect the hottest device across separate packages. Mount paralleled devices as close as possible on the same heat sink (or use multi-die packages); match rds as a last resort. | — | layout, rds spread | paralleled discrete MOSFETs | inspect | p.480-481, §9.2.10 | high |
| PRESSMAN-2112 | components | Dynamic current sharing in paralleled MOSFETs requires matched transconductance curves at It/n per device (threshold match not essential) and a symmetrical layout: equal gate-driver-to-gate lead lengths, equal source-to-common-point lengths, common point taken directly to the ground bus and housekeeping negative rail; add 10-20 Ohm resistors or ferrite beads in series with each gate against oscillation. | R_g,each = 10-20 Ohm (or ferrite bead) ; gfs matched at It/n | n, It, gfs curves | parallel MOSFETs | inspect/measure | p.481-482, §9.2.10, Figs. 9.15-9.16 | high |
| PRESSMAN-2113 | magnetics | MOSFET push-pull reduces flux-imbalance (no storage time; positive rds tempco gives negative feedback); designers have used conventional MOSFET push-pull with acceptable flux imbalance up to 150 W. Residual imbalance can be trimmed with a select-at-test gate resistor on the higher-current side (not acceptable where SAT is prohibited, e.g. some military programs); current-mode control eliminates the problem. | P_out <= 150 W for voltage-mode MOSFET push-pull without extra flux-balance measures (experience) | P_out | push-pull | review/measure | p.483-484, §9.2.11, Fig. 9.17 | medium |
| PRESSMAN-2114 | protection | MOSFET gate-source maximum is typically +/-20 V; at fast turn-off Miller coupling can spike the gate: example Vds step 372 V (2 x 186 V forward converter) * Crss/(Crss + Ciss) = 372*150/1950 = 29 V > 20 V. Shunt gate-source with an 18 V zener (fitted at the driver end of a 5-50 Ohm gate resistor per maker guidance). | V_spike = dVds * Crss/(Crss + Ciss) < 20 V ; clamp Vz = 18 V | dVds, Ciss, Crss | high-voltage MOSFET switches | calc | p.484-485, §9.2.12 | high |
| PRESSMAN-2115 | components | MOSFET body diode: forward current and reverse voltage ratings similar to the MOSFET; recovery faster than a standard rectifier but slower than discrete fast-recovery types. Harmless in bridges where dead time separates diode conduction from reverse voltage; where reverse voltage must be supported immediately after forward current (resonant converters, highly inductive/motor loads) add a series blocking diode in the drain and an external fast anti-parallel diode (Fig. 9.19), unless the device has a fully specified fast body diode (post mid-1990s parts). | — | body-diode trr, topology | resonant, motor drives | review | p.485-487, §9.2.13, Figs. 9.18-9.19 | high |
| PRESSMAN-2116 | derating | IGBT blocking voltage: the highest voltage the IGBT must block should not exceed 80% of VCES. | V_CE,pk <= 0.8 * VCES | V_CE,pk incl. spikes | IGBTs | calc | p.488, §9.3.1 item 2 | high |
| PRESSMAN-2117 | components | IGBT type choice: PT (punch-through, N+ buffer) = faster, lower switching energy, tail quenched, often not short-circuit rated, slightly negative VCE(on) tempco, hard to make above 600 V (some fast 1200 V PT exist), little reverse blocking; NPT = slower, more rugged, short-circuit rated, more avalanche energy, positive VCE(on) tempco (parallels easily). SMPS (no short-circuit need, high fsw) -> PT; motor drives (short-circuit withstand, low fsw) -> NPT. | — | fsw, short-circuit need | IGBTs | review | p.488-492, §9.3.1-9.3.3.4 | high |
| PRESSMAN-2118 | components | IGBT current sizing: soft-switching — start from IC2 (continuous at max die temperature); hard switching — use the data-sheet usable-frequency vs collector-current curve (Fig. 9.30), correcting for differences between test and application conditions. IC1/IC2 exclude switching loss and must be derated with case/heat-sink temperature. | — | Ic, fsw, Tc | IGBTs | calc | p.488, p.494-495, §9.3.5, Fig. 9.22 | high |
| PRESSMAN-2119 | reliability | IGBT latch-up (parasitic PNPN thyristor; gate loses control): static latch-up from excessive current/local heating, dynamic latch-up from high turn-off dv/dt with excessive current (limits SOA). Avoided by staying within max current and SOA ratings; stray inductances, gate resistor and poor layout drive dv/dt, overshoot and ringing. | Ic <= ICM, locus within RBSOA/SSOA | Ic, dv/dt | IGBTs | measure | p.492-493, §9.3.3.5 | high |
| PRESSMAN-2120 | components | IGBT temperature behaviour: turn-on speed/loss essentially temperature independent (but external diode reverse recovery rises with temperature, raising Eon2); NPT turn-off loss roughly constant; PT turn-off slows and loss rises with temperature (small, starts low). | — | Tj | IGBTs | review | p.493, §9.3.3.6; p.502 | high |
| PRESSMAN-2121 | components | IGBT gate transients: VGEM is the pulsed gate-emitter limit (gate oxide); if measured gate ringing exceeds VGEM, reduce stray inductance (minimize gate-drive loop area) and/or increase gate resistance; connect any clamp zener between driver and gate resistor, not at the gate pin; negative gate drive is optional (speed, dv/dt-induced turn-on immunity). | V_GE,ring,pk < VGEM | measured VGE | IGBT gate drive | measure | p.494, §9.3.5 | high |
| PRESSMAN-2122 | components | IGBT ICM (pulsed) keeps operation below the transfer-curve linear-region knee (above it VCE and loss rise sharply -> destruction) and avoids burnout/latch-up; staying within ICM alone does not guarantee Tj <= Tj max (depends on pulse width, spacing, VCE(on), shape). | Ic_pk <= ICM AND Tj(pulse) <= Tj_max | Ic_pk, ZthJC | IGBTs | calc | p.496-497, §9.3.5, Fig. 9.23 | high |
| PRESSMAN-2123 | components | ILM = clamped inductive current the IGBT can hard-switch without a snubber (maker conditions: Tc, Rg, clamp voltage); RBSOA = max current vs voltage at turn-off; SSOA = RBSOA at full VCES; FBSOA (turn-on) usually much larger and often unlisted. Within these ratings no snubber, minimum Rg or dv/dt limit is needed for reliability. | I_off <= ILM ; (Ic, Vce) inside RBSOA | turn-off Ic, Vce | IGBTs, hard switching | calc/measure | p.497, §9.3.5 | high |
| PRESSMAN-2124 | components | Avalanche (UIS) energy rating EAS: energy of stray/leakage inductance dumped into the device when ringing exceeds breakdown. Do not intentionally operate an IGBT in avalanche without thorough testing. | E_AS = 0.5 * L * Ic^2 ; E_leak = 0.5 * L_leak * I_pk^2 <= EAS | L_leak, I_pk | avalanche-rated IGBTs/MOSFETs | calc | p.497-498, §9.3.5 | high |
| PRESSMAN-2125 | thermal | Device maximum dissipation (infinite heat sink, case at 25 C) and steady-state junction temperature. | PD = (TJ(max) - 25 C) / RthJC ; TJ = TC + P_loss * RthJC ; P_loss = switching + conduction (+ leakage, usually ignored) | TJmax, RthJC, TC, P_loss | IGBTs (applies to all power semis) | calc | p.498, p.505, §9.3.5, §9.3.8, Fig. 9.28 | high |
| PRESSMAN-2126 | reliability | Rule of thumb for thermally induced failure mechanisms: every 10 C reduction in junction temperature below the upper limit doubles device life. | life ~ 2^((Tj_max - Tj)/10) | Tj | IGBTs/power semis | calc | p.498, §9.3.5 | medium |
| PRESSMAN-2127 | components | IGBT static parameter temperature behaviour: BVCES rises ~10% from 25 C to 150 C; VGE(th) tempco ~ -12 mV/C (same as MOSFET); leakage ICES rises with temperature (leakage loss = ICES*VCE); VCE(on) tempco positive for NPT, slightly negative for PT and becomes positive at higher current. | dBVCES = +10% (25->150 C) ; dVGE(th)/dT = -12 mV/C | Tj | IGBTs | calc | p.498-499, §9.3.6 | high |
| PRESSMAN-2128 | components | IGBT capacitances and gate charge: Cies = CGE + CGC; Coes = CCE + CGC (matters for resonance in soft switching); Cres = CGC (Miller, governs voltage rise/fall). Gate charge measured per JEDEC 24-2; use QG (not capacitance) for drive design. Plateau voltage VGEP rises with collector current (not temperature): replacing a HV MOSFET with an IGBT, a 10-12 V drive may switch slowly/incompletely at high current — raise gate drive. | Cies = CGE + CGC ; Coes = CCE + CGC ; Cres = CGC ; I_g = QG / t_sw | QG, VGEP(Ic) | IGBT gate drive | calc | p.499-502, §9.3.7, Figs. 9.24-9.26 | high |
| PRESSMAN-2129 | power | Scale data-sheet IGBT switching energies linearly with application voltage (e.g. tested at 400 V, used at 300 V -> x 300/400); switching energy rises with gate resistance and with stray emitter inductance; data-sheet values are representative only. | E_app = E_ds * V_app / V_test ; P_sw = (Eon + Eoff) * fsw | E_ds, V_test, V_app, fsw | IGBTs | calc | p.502-503, §9.3.7, Fig. 9.31 | high |
| PRESSMAN-2130 | components | IGBT switching time definitions: td(on) = 10% VGE rise to 10% Ic rise; td(off) = 90% VGE fall to 90% Ic fall; tr = 10-90% Ic; tf = 90-10% Ic. | — | — | data-sheet interpretation / measurement | measure | p.503, §9.3.7 | high |
| PRESSMAN-2131 | protection | IGBT over-current protection by desaturation: limit maximum gate voltage (the IGBT current self-limits at a given VGE) and turn the drive off when VCE starts to rise under a transient over-current; not effective for MOSFETs (drain current insensitive to Vgs when fully on). | trip when VCE(on) rises above normal envelope while gate is high | VCE sense | IGBTs | measure | p.503, §9.3.7, Fig. 9.27 | high |
| PRESSMAN-2132 | thermal | Use transient thermal impedance ZthJC (Fig. 9.29) for pulsed junction temperature; back-to-back hard-switching transients without cooling time can overheat the die even at small duty; nonrectangular pulses need piecewise-linear approximation. | Tj_pk = Tc + P_pk * ZthJC(tp, D) | P_pk, tp, D | IGBTs, hard switching | calc | p.505-506, §9.3.8 | high |
| PRESSMAN-2133 | components | Minimum pulse-width / max frequency guideline (APT): total switching time td(on) + tr + td(off) + tf must be no more than 5% of the switching period. | (td_on + tr + td_off + tf) <= 0.05 * T_sw -> f_max = 0.05 / t_sw,total | td_on, tr, td_off, tf (s) | hard-switched IGBTs | calc | p.507, §9.3.8 | high |
| PRESSMAN-2134 | power | Open-loop slave outputs of a master-regulated multi-output forward/push-pull track line changes but not load: cross regulation (slave change due to master load change) may be as high as +/-8%; if the master or a slave inductor goes discontinuous, the slave voltage may change by up to 50%. Coupled output chokes (all secondaries on one core) improve cross regulation and widen the current range. | dVslave(cross) up to +/-8% ; up to 50% if any inductor enters DCM | I_min vs critical current of each inductor | multi-output forward/push-pull | calc/measure | p.511-512, §10.1 | high |
| PRESSMAN-2135 | power | Slave output voltages can only be set in coarse steps (integer turns; volts/turn proportional to switching frequency, so steps get coarser at higher f) and to within a few percent. Loads needing better than 1% line/load regulation need a postregulator. | dV_step = V/turn = Vs / Ns | Ns, Vs, f | slave outputs | calc | p.512, §10.1 | high |
| PRESSMAN-2136 | power | Postregulator choice: linear IC regulator up to ~1.5 A (headroom 2-3 V; 1 A x 3 V = 3 W; low-dropout 0.5-1.0 V types cost more); buck postregulator above ~1.5 A with slave set ~4 V above output (adds RFI, may beat with main fsw unless synchronized); magnetic-amplifier postregulator preferred above 1.5 A and credible below. | P_lin = I_o * V_headroom ; V_slave >= Vo + 4 V (buck postreg) | Io, headroom | slave outputs | calc | p.512-513, §10.2 | high |
| PRESSMAN-2137 | magnetics | Mag-amp (saturable reactor) postregulator output: the MA blocks the front part tb of each secondary pulse th and fires for tf; the slave secondary must be dimensioned above the required output since the MA can only reduce the pulse width. | Vos = (Vsp - V_D1) * tf / T ~= (Vsp - 1) * tf / T (Eq. 10.2) ; tf = th - tb (Eq. 10.3) ; Vom ~= [(Vdc - 1)*Nsm/Np - 1] * th/T (Eq. 10.1b) | Vsp, tf, T | forward converter slave outputs | calc | p.514-515, §10.3, Fig. 10.1 | high |
| PRESSMAN-2138 | magnetics | Mag-amp blocking time from Faraday's law (CGS). | tb = Nm * Ae * (Bs - B1) * 1e-8 / Vsp (Eq. 10.4); Nm turns, Ae (cm^2), Bs, B1 (G), Vsp (V), tb (s). SI form (TIP): td(us) = N * dB(T) * Ae(mm^2) / Vs | Nm, Ae, Bs, B1, Vsp | square-loop core MA | calc | p.517-520, §10.3.1-10.3.2 | high |
| PRESSMAN-2139 | magnetics | Mag-amp shutdown capability: to force the slave to zero, reset to -Bs; size Nm*Ae so the full-loop blocking time exceeds the maximum on-time. Error amp and reset transistor must then be powered from a source that is always present (not the slave itself). | tb_max = Nm * Ae * 2*Bs * 1e-8 / Vsp >= ton_max | Nm, Ae, Bs, Vsp, ton_max | shutdown-capable mag-amps | calc | p.521-522, §10.3.4 | high |
| PRESSMAN-2140 | magnetics | Mag-amp core loss: regulation-only operation traverses a minor loop typically about 1/4 of the major-loop area (low loss); full shutdown operation traverses the whole -Bs..+Bs loop — compute loss from maker loss vs total flux excursion curves. | P_core(minor) ~ 0.25 * P_core(major) (typical) | flux excursion | Toshiba MB/MA, Metglas, Permalloy | calc | p.522, §10.3.4; p.529, §10.3.6 | medium |
| PRESSMAN-2141 | magnetics | Set-type (leading-edge) mag-amps need high-permeability metallic square-loop cores (high HF loss); reset-type (trailing-edge) can use low-loss ferrite for very high frequency. | — | fsw | mag-amp type selection | review | p.522, §10.3.4 TIP | high |
| PRESSMAN-2142 | materials | Square Permalloy 80 (79% Ni, 17% Fe, 4% Mo) tape thickness vs frequency: 1-mil tape up to 50 kHz; 1/2-mil for 50-100 kHz; above 100 kHz use amorphous (Metglas 2714A, Toshiba MA/MB, Vitrovac 6025). For regulation-only minor-loop operation the higher-loss 1-mil tape may be used above 50 kHz. Available tapes 0.5, 1, 2, 4, 6, 14 mil. | f <= 50 kHz: 1 mil ; 50-100 kHz: 0.5 mil ; > 100 kHz: amorphous | fsw | mag-amp cores | review | p.522-525, §10.3.5 | high |
| PRESSMAN-2143 | materials | Mag-amp core must have a very square loop (saturated permeability ~1, i.e. air-core impedance) — otherwise the MA drops voltage during firing and switches slowly. Coercive force rises with frequency while Bs stays fixed (loss rises). Toshiba Bs: MA 6500 G, MB 6000 G; MB coercive force at 100 kHz = 0.18 Oe. | — | loop squareness, Hc(f) | mag-amp cores | review | p.522-529, §10.3.5, Fig. 10.6 | high |
| PRESSMAN-2144 | thermal | Mag-amp temperature: core-to-case-surface differential about 15 C; Square Permalloy Curie temperature 460 C so the limit is usually the wire temperature rating or required efficiency. Core weight from area x path length x density (Permalloy 8.75 g/cm^3; MA/MB 8.0 g/cm^3: W/lb = 56.8 x W/cm^3). | T_core ~= T_case_surface + 15 C | P_core, Rth (Fig. 7.4, Fig. 10.12) | toroidal mag-amp cores | calc | p.523-527, §10.3.5 | high |
| PRESSMAN-2145 | magnetics | Forward converter maximum on-time: with reset turns Nr = Np the absolute maximum is 0.5T; design Nsm so the master output is reached at ton = 0.4T at minimum Vdc, leaving 0.1T guard band for transient line dips (core must always reset). | D_max,design = 0.4 (Nr = Np) ; D_abs = 0.5 | Nr/Np, Vdc_min | single-ended forward converter | calc | p.534-536, §10.3.7 | high |
| PRESSMAN-2146 | magnetics | Mag-amp postregulator worked example (100 kHz forward, 15 V / 10 A slave): of the 4 us secondary pulse at min Vdc choose tf = 3 us, tb = 1 us -> Vsp = 15*10/3 + 1 = 51 V; turns sized to block 51 V for the full 4 us (shutdown) using the full 2*Bs swing: Toshiba MB 21x14x4.5 (Ae 0.118 cm^2, Bs 6000 G) -> N = 51*4e-6/(0.118*12000*1e-8) = 14 turns; Irms = 10*sqrt(3/10) = 5.48 A -> 2739 CM at 500 CM/A -> 2 x No. 19 (2580 CM) in one layer (inner periphery 1.73 in holds 44 turns of 0.0391 in wire); full-loop loss 1 W (1400 maxwell = 12000 G) -> 40 C rise. | N = Vsp * t_block / (Ae * 2*Bs * 1e-8) | Vsp, t_block, Ae, Bs | — | calc | p.536-539, §10.3.7, Figs. 10.9, 10.12, 10.13 | high |
| PRESSMAN-2147 | magnetics | Choose the mag-amp core with the largest iron area that fits: fewest turns for the required volt-seconds and lowest residual (air-core) inductance when saturated. | minimize Nm for Vsp*t_block | Ae | mag-amp | review | p.537, §10.3.7 | high |
| PRESSMAN-2148 | current-carrying | Classic wire sizing rule used by Pressman: 500 circular mils per rms ampere. | A_wire(CM) >= 500 * I_rms | I_rms | transformer/mag-amp windings at low f (at HF check skin/proximity, see Dowell) | calc | p.539, §10.3.7 | high |
| PRESSMAN-2149 | control-loop | Mag-amp gain = output current / coercive (reset) current; the control current flows while the load diode is reverse-biased so it does not have to buck out load ampere-turns (unlike a series saturable reactor). Example MB 21x14x4.5: Hc = 0.18 Oe at 100 kHz, lp = 5.5 cm, Nm = 14 -> Ic = 56.3 mA -> gain 10/0.056 = 178. | Ic = Hc * lp / (0.4*pi*Nm) ; Gain = Io / Ic | Hc (Oe), lp (cm), Nm, Io | mag-amp postregulators | calc | p.539-540, §10.3.8 | high |
| PRESSMAN-2150 | power | Mag-amps on full-wave (push-pull/half-bridge) outputs carry primary magnetizing current during dead time — the simple two-core circuit has serious problems (see Jamerson & Chen). | — | — | symmetrical topologies | review | p.540, §10.3.9 | high |
| PRESSMAN-2151 | control-loop | Mag-amp PWM/error amplifier (Dulskis & Estey): on-time set by control-winding bias of reset level B0; senses output ground and drives input-ground switches without a housekeeping supply; robust at high temperature. Worked build: 40 kHz, +/-8 V square wave drive; cores 1/4-mil Square Permalloy on 0.290 OD x 0.16 ID x 0.175 in bobbins; gate windings 40 T No. 35; control winding 250 T No. 37. | ton = Ng * Ae * (Bs - B0) * 1e-8 / 1.6 V | Ng, Ae, Bs, B0 | isolated low-part-count regulators | calc | p.540-544, §10.4, Figs. 10.15-10.16 | high |
| PRESSMAN-2152 | power | Switch turn-off overlap (V x I) loss dominates switching loss in transformer/inductor-in-series topologies; for bipolars the transition lasts 0.2-2 us and switching loss is a prime limit above 50 kHz. Transformer leakage inductance makes turn-on loss small; a buck has large overlap loss at both turn-on (into conducting freewheel diode) and turn-off. | P_sw = f * integral(V*I dt) over transitions | tr, tf, V, I, f | hard-switched converters | calc/measure | p.545-546, §11.1 | high |
| PRESSMAN-2153 | power | MOSFET turn-on loss from output capacitance charged to 2*Vdc (forward converter) is dumped in the channel each cycle; any snubber capacitance adds to it. | P_Coss = 0.5 * Co * (2*Vdc)^2 / T | Co (F), Vdc (V), T (s) | forward converter MOSFET (drain swings to 2Vdc) | calc | p.546, §11.1 | high |
| PRESSMAN-2154 | power | Unsnubbed turn-off loss estimate (voltage rises instantly to 2Vdc while current falls linearly in tf): example 150 W forward, Vdc 136-184 V, Ip = 3.13*150/136 = 3.45 A, tf = 0.3 us (2x the 0.15 us data-sheet value as worst case), 100 kHz -> 368*3.45/2 = 635 W during tf -> 19 W average (may be ~50% more because current hangs at peak before falling). | P_off = (2*Vdc*Ip/2) * tf / T | Vdc_max, Ip, tf, T | no snubber | calc | p.547-548, §11.2, Fig. 11.1b | high |
| PRESSMAN-2155 | derating | Use twice the data-sheet nominal current fall time as the worst-case tf in switching-loss and snubber calculations. | tf_wc = 2 * tf_datasheet | tf_ds | bipolar (2N6836 example) | calc | p.548, §11.2 | high |
| PRESSMAN-2156 | protection | RCD turn-off snubber capacitor: assume half of Ip is diverted into C1 and let the collector reach 2Vdc in the same time tf the current falls to zero. | C1 = (Ip/2) * tf / (2*Vdc) (Eq. 11.3). Example: (3.45/2)*0.3e-6/(2*184) = 0.0014 uF | Ip, tf, Vdc_max | forward converter, RCD snubber to ground | calc | p.550-551, §11.4-11.5 | high |
| PRESSMAN-2157 | protection | RCD snubber resistor: discharge C1 to within 5% in the minimum on-time. | 3 * R1 * C1 = ton(min) (Eq. 11.1). Example: ton_max = 0.8*T/2 = 4 us at 100 kHz; +/-15% line -> ton_min = 4/1.3 ~ 3 us -> R1 = 3e-6/(3*0.0014e-6) = 714 Ohm | ton_min, C1 | RCD snubber | calc | p.549, p.551, §11.3, §11.5 | high |
| PRESSMAN-2158 | thermal | RCD snubber resistor dissipation equals C1's stored energy per cycle and is independent of R1 (reducing R1 does not reduce its loss). Worked example: 9.5 W in R1 while transistor loss falls from 19 W to 3.2 W. | P_R1 = 0.5 * C1 * (2*Vdc)^2 / T (Eq. 11.2; printed with Vdc^2, worked example uses 2Vdc) ; example 0.5*0.0014e-6*368^2/10e-6 = 9.5 W | C1, Vdc_max, T | snubber returned to ground (cap charges to 2Vdc) | calc | p.549-552, §11.3, §11.5 | high |
| PRESSMAN-2159 | power | Transistor overlap dissipation with RCD snubber (best-case timing: current Ip/2 falls to zero as voltage reaches 2Vdc). | P_Q1 = (Ip/2) * (2*Vdc) * tf / (6*T) (Eq. 11.4). Example: 1.725*368*0.3e-6/(6*10e-6) = 3.2 W | Ip, Vdc, tf, T | RCD-snubbed switch | calc | p.551-552, §11.4-11.5 | high |
| PRESSMAN-2160 | thermal | If the switch case runs too warm, increase snubber C1 (moves dissipation into R1, which is far less failure-prone than the transistor). | — | case temperature | RCD snubbers | measure | p.552, §11.5 | high |
| PRESSMAN-2161 | protection | Return the RCD snubber to the positive supply rail rather than ground: capacitor voltage stress falls from 2Vdc to Vdc. | V_C1,max = Vdc (rail-returned) vs 2*Vdc (ground-returned) | Vdc | RCD snubber | inspect | p.552-553, §11.5.1, Fig. 11.3 | high |
| PRESSMAN-2162 | derating | Power resistors are derated by a factor of 2: a 10 W snubber dissipation needs a 20 W resistor (large, heats neighbours) — above 50 kHz off-line RCD snubbers often reach 10 W or more, motivating non-dissipative snubbers. | P_rating >= 2 * P_dissipated | P_diss | power resistors | calc | p.553, §11.6 | high |
| PRESSMAN-2163 | protection | Non-dissipative (LC + diodes) snubber: C1 sized as for RCD to slow dV/dt; L1 chosen so the full ring period is somewhat less than the minimum on-time; energy returns to the input bus via resonant ring (high-Q L1). | fr = 1/(2*pi*sqrt(L1*C1)) ; 2*pi*sqrt(L1*C1) < ton(min) | C1, ton_min | forward converters > 50 kHz | calc | p.553-555, §11.6, Fig. 11.4 | high |
| PRESSMAN-2164 | protection | Leakage-inductance turn-off spike above 2Vdc is set by half the peak current into the characteristic impedance of leakage inductance and snubber capacitor; increasing C1 lowers the spike. Example: Ll = 15 uH (100 kHz transformer), C1 = 0.0014 uF -> sqrt(Ll/C1) = 103 Ohm -> 1.725 A * 103 = 178 V -> peak 2*184 + 178 = 547 V. | V_spike = (Ip/2) * sqrt(Ll / C1) ; V_pk = 2*Vdc + V_spike | Ip, Ll, C1, Vdc_max | forward converter with Np = Nr | calc | p.555-557, §11.7, Fig. 11.6 | high |
| PRESSMAN-2165 | reliability | Load-line shaping: the turn-off locus (horizontal at ~Ip/2 out to the spike peak) must stay inside RBSOA; 2N6836 at 1.73 A / 547 V is inside RBSOA with 5 V reverse base bias but outside without reverse bias (secondary breakdown). Increase C1 above Eq. 11.3 if needed to shrink the spike; higher power needs larger C1. | (Ip/2, 2*Vdc + V_spike) inside RBSOA | Ip, V_pk, RBSOA | bipolar switches | calc/measure | p.555-558, §11.7, Fig. 11.5 | high |
| PRESSMAN-2166 | protection | Transformer lossless snubber (Fig. 11.7): a small 1:1 transformer with very low leakage, sized for the maximum off-state volt-seconds, clamps the switch at 2Vdc and returns leakage energy to Vdc; lets the RCD C1 be much smaller. | V_ce,max = 2*Vdc (clamped) | T1 volt-seconds, leakage | forward converter | review | p.558-559, §11.8 | high |
| PRESSMAN-2167 | test | Optimize snubber components by measuring the actual switching-edge dissipation with a scope's real-time V x I multiplication. | — | V, I probes | snubber tuning | measure | p.550, §11.4 TIP | high |
| PRESSMAN-2168 | control-loop | Stability criterion 1 (phase margin): at the crossover frequency Fco (open-loop gain = 0 dB) total open-loop phase shift, including the 180 deg of the negative-feedback inversion, must be less than 360 deg; the shortfall is the phase margin. Usual practice: design for 35-45 deg to cover worst-case component variation; the author designs for 45 deg (Fig. 12.4: "at least 45 deg"). | PM = 360 deg - phase_total(Fco) >= 45 deg (min 35 deg) | open-loop phase at Fco | voltage-mode PWM loops | calc/measure | p.563, §12.2.1; p.567, §12.2.2; Fig. 12.4 | high |
| PRESSMAN-2169 | control-loop | Stability criterion 2 (gain slope): the total open-loop gain should pass through Fco at a -1 slope (-20 dB/decade); a -2 slope region has rapidly changing phase. Not absolute, but insurance against overlooked phase-shift elements. | slope of loop-gain magnitude at Fco = -20 dB/dec | Bode gain | all loops | calc | p.567, §12.2.2, Fig. 12.4 | high |
| PRESSMAN-2170 | control-loop | Crossover frequency choice: sampling theory requires Fco < fsw/2, and in practice much lower to avoid large switching-frequency ripple at the output; fix Fco at 1/4 to 1/5 of the switching frequency (examples use fsw/5). | Fco = fsw/5 to fsw/4 ; Fco < fsw/2 (absolute) | fsw | PWM converters | calc | p.572, §12.3; Fig. 12.4 | high |
| PRESSMAN-2171 | control-loop | Output LC filter: flat gain up to Fo, then -2 slope (-40 dB/dec); phase 90 deg at Fo. Damping ratio k2 = Ro/sqrt(Lo/Co): k2 = 1 critically damped (tiny bump); k2 > 1 underdamped (high resonant bump; for Ro >= 5*sqrt(Lo/Co) phase already ~170 deg at 1.5*Fo); k2 = 0.1 heavily overdamped reaches -2 slope only near 20*Fo. Design for the critically damped curve, then check light load (resonant bump). | Fo = 1/(2*pi*sqrt(Lo*Co)) ; Z0 = sqrt(Lo/Co) | Lo, Co, Ro | buck-derived converters (Ro = load resistance here) | calc | p.565-568, §12.2.2-12.2.3, Fig. 12.3 | high |
| PRESSMAN-2172 | control-loop | Output capacitor ESR zero: the LC gain slope breaks from -2 to -1 where Xc = Resr. For aluminum electrolytics over a large range of values/voltages, Resr*Co is roughly constant at 65e-6 s, giving Fesr ~ 2.4-2.5 kHz. | Fesr = 1/(2*pi*Resr*Co) ; Resr*Co ~= 65e-6 s (Al electrolytic) -> Fesr ~= 2450 Hz | Resr, Co | aluminum electrolytic output caps (author's catalogue survey) | calc | p.569-570, §12.2.3; p.583, §12.9; p.585, §12.10 | high |
| PRESSMAN-2173 | control-loop | PWM modulator gain (voltage mode, 3 V triangle, max half-period on-time): gain from EA output to average voltage at inductor input; frequency independent. | Gm = 0.5 * (Vsp - 1) / 3 (Eq. 12.1) ; generally Gm = V_av,max / V_ramp,pp | Vsp (V), V_ramp (V) | push-pull/forward/bridge PWM chips with 0-3 V ramp | calc | p.570, §12.2.4 | high |
| PRESSMAN-2174 | control-loop | Output sampling divider gain = Vref/Vo (2.5 V reference, 5 V output -> R1 = R2 -> -6 dB). Open-loop gain excluding EA: Gt = G_LC + Gm + Gs (dB add). | Gs = 20*log10(Vref/Vo) | Vref, Vo | — | calc | p.571, §12.2.4-12.2.5, Fig. 12.6 | high |
| PRESSMAN-2175 | control-loop | Loop shaping procedure: (1) set Fco; (2) set EA gain at Fco equal and opposite to Gt(Fco) in dB; (3) give the EA the slope that makes the total slope -1 at Fco (horizontal EA if Gt is -1 there; +1 EA if Gt is -2); (4) place zeros/poles (K factor) for the desired phase margin; add low-frequency gain (zero) for 120 Hz ripple rejection and high-frequency rolloff (pole) for noise spikes. | G_EA(Fco) (dB) = -Gt(Fco) (dB) | Gt(Fco), slope | voltage-mode | calc | p.572-575, §12.3, Fig. 12.6-12.8 | high |
| PRESSMAN-2176 | control-loop | Zero/pole slope rules: a zero adds +1 to gain slope, a pole adds -1; double zero/pole adds +/-2; the pole at the origin sets the frequency where the integrator gain line crosses 0 dB. Phase lead of a zero at F: atan(F/Fz); phase lag of a pole: atan(F/Fp). | theta_zero = atan(F/Fz) ; theta_pole = -atan(F/Fp) | Fz, Fp, F | Bode asymptotes | calc | p.576-579, §12.5, §12.7, Fig. 12.10 | high |
| PRESSMAN-2177 | control-loop | Type 2 error amplifier (Venable): pole at origin, one zero, one pole (R1 input; R2 + C1 in series, shunted by C2, in feedback). Used when the output capacitor ESR puts Fco on the -1 slope of the LC curve (Fesr < Fco). Midband gain R2/R1. | G(s) = (1 + s*R2*C1) / (s*R1*(C1 + C2)*(1 + s*R2*C2)) (Eq. 12.4, C2 << C1) ; Fpo = 1/(2*pi*R1*(C1+C2)) ; Fz = 1/(2*pi*R2*C1) ; Fp = 1/(2*pi*R2*C2) ; G_mid = R2/R1 | R1, R2, C1, C2 | voltage-mode forward/buck with ESR | calc | p.578-579, §12.6, Fig. 12.7b | high |
| PRESSMAN-2178 | control-loop | K factor (Venable): place Fz and Fp symmetrically about Fco; wider spacing = more phase margin but less 120 Hz gain (Fz too low) and more HF noise gain (Fp too high). | K = Fco/Fz = Fp/Fco ; Type 2 lag = 270 - atan(K) + atan(1/K) deg (Eq. 12.7) -> K = 2: 233; 3: 216; 4: 208; 5: 202; 6: 198; 10: 191 deg (Table 12.1) | K | Type 2 EA | calc | p.574, p.579-580, §12.3, §12.7, Table 12.1 | high |
| PRESSMAN-2179 | control-loop | Phase lag of an LC filter with ESR zero at Fco (modulator phase neglected). | theta_LC = 180 - atan(Fco/Fesr) deg (Eq. 12.8), e.g. Fco/Fesr = 1: 135; 2: 116; 4: 104; 8: 97.1; 10: 95.7 deg (Table 12.2) | Fco, Fesr | LC output filter with ESR (above Fo) | calc | p.580-581, §12.8, Table 12.2 | high |
| PRESSMAN-2180 | control-loop | Type 2 design example (forward, 5 V/10 A, Io_min 1 A, 100 kHz, 50 mV p-p): Lo = 3*Vo*T/Io = 15 uH (Eq. 2.47); Co = 65e-6*dI/Vor = 65e-6*2/0.05 = 2600 uF (Eq. 2.48, dI = 2*Io_min); Fo = 806 Hz; Fesr = 2500 Hz; Gm = 0.5*(11-1)/3 = 1.67 (+4.5 dB), Gs = -6 dB -> -1.5 dB; Fco = 20 kHz where Gt = -40 dB -> EA +40 dB (R1 = 1 k, R2 = 100 k); LC lag 97 deg -> EA may lag 218 deg (K ~ 3); choose K = 4 (208 deg) -> PM 55 deg; Fz = 5 kHz -> C1 = 318 pF; Fp = 80 kHz -> C2 = 20 pF. | PM = 360 - (theta_EA + theta_LC) | — | — | calc | p.582-585, §12.9, Figs. 12.12-12.13 | high |
| PRESSMAN-2181 | control-loop | Type 3 error amplifier: pole at origin, double zero, double pole. Required when the output capacitor has (near) zero ESR so the LC curve is still at -2 slope at Fco: EA needs a +1 slope at Fco. Set Fz1 = Fz2 and Fp1 = Fp2. | G(s) = -(1+s*R2*C1)*(1+s*(R1+R3)*C3) / (s*R1*(C1+C2)*(1+s*R3*C3)*(1+s*R2*C1*C2/(C1+C2))) (Eq. 12.10) ; Fpo = 1/(2*pi*R1*(C1+C2)) ; Fz1 = 1/(2*pi*R2*C1) ; Fz2 = 1/(2*pi*(R1+R3)*C3) ~ 1/(2*pi*R1*C3) ; Fp1 ~ 1/(2*pi*R2*C2) ; Fp2 = 1/(2*pi*R3*C3) (Eqs. 12.11-12.15) | R1, R2, R3, C1, C2, C3 | voltage-mode with zero-ESR caps (R1 >> R3, C1 >> C2) | calc | p.585-590, §12.10-12.12, Fig. 12.15 | high |
| PRESSMAN-2182 | control-loop | Type 3 phase lag vs K; LC lag with no ESR zero is 180 deg, so the EA must lag no more than 315 - 180 = 135 deg for 45 deg PM (K ~ 5). | Type 3 lag = 270 - 2*atan(K) + 2*atan(1/K) deg (Eq. 12.9): K = 2: 196; 3: 164; 4: 146; 5: 136; 6: 128 deg (Table 12.3) | K | Type 3 EA | calc | p.587-588, §12.11, Table 12.3 | high |
| PRESSMAN-2183 | control-loop | Type 3 design example (forward, 5 V/10 A, Io_min 1 A, 50 kHz, < 20 mV, zero-ESR 2600 uF): Lo = 30 uH; Fo = 570 Hz; Gm + Gs = -1.5 dB; Fco = 10 kHz where LC loss = -50 dB -> EA +50 dB at 10 kHz on a +1 slope; K = 5 -> Fz = 2 kHz, Fp = 50 kHz; R1 = 1 k; EA gain at Fz = +37 dB (70.8) -> R2 = 70.8 k; C1 = 1/(2*pi*R2*Fz) = 0.011 uF; C2 = 1/(2*pi*R2*Fp) = 45 pF; C3 = 1/(2*pi*R1*Fz) = 0.08 uF; R3 = 1/(2*pi*C3*Fp) = 40 Ohm. | R2 = R1 * 10^(G_EA(Fz)/20) | — | — | calc | p.590-593, §12.13-12.14, Fig. 12.16 | high |
| PRESSMAN-2184 | control-loop | Conditional stability: if open-loop phase reaches 360 deg at a frequency where gain > 0 dB (typically near the LC corner at light load), a momentary gain drop (turn-on, line transient) can start sustained oscillation. Remedy: add phase boost (a zero) at the LC corner frequency with a capacitor across the upper resistor of the output sampling divider. | phase(f) must not reach 360 deg where loop-gain magnitude T(f) > 0 dB, esp. near Fo at light load | Bode at min load | voltage-mode with LC output | calc/measure | p.593-595, §12.15, Fig. 12.17 | high |
| PRESSMAN-2185 | control-loop | DCM flyback small-signal plant (EA output -> Vo): single pole set by load and output capacitor (not an LC double pole), plus ESR zero; low-frequency gain proportional to Vdc and sqrt(Ro). Derived for 80% efficiency and a 0-3 V PWM ramp (Ton = Vea*T/3). | Vo/Vea = (Vdc/3) * sqrt(0.4 * Ro * T / Lp) (Eq. 12.19) ; Fp = 1/(2*pi*Ro*Co) (Eq. 12.20) ; Fesr = 1/(2*pi*Rc*Co) | Vdc, Ro (load), T, Lp, Co, Rc (ESR) | discontinuous-mode flyback | calc | p.595-597, §12.16, Fig. 12.18 | high |
| PRESSMAN-2186 | control-loop | DCM flyback: evaluate all four combinations of Vdc(min/max) and Ro(min/max); the loop must not cross at a -2 slope at any. Test carefully for stability at minimum load current (maximum Ro), where the plant gain is lowest and crossover may move onto the -1 slope of the plant. Maximum output-circuit lag is 90 deg (usually far less with ESR zero), so phase margin is rarely a problem. | check (Vdc_min, Vdc_max) x (Ro_min, Ro_max) | Vdc, Ro range | DCM flyback | calc/measure | p.597-602, §12.16-12.18 | high |
| PRESSMAN-2187 | control-loop | DCM flyback compensation (Type 2): at Ro_min put Fco (fsw/5) usually on the flat part after the ESR zero, so EA slope at Fco = -1; place the EA pole (P3) somewhat below Fesr; zero about a decade below the pole (not critical). Worked example (5 V, 10 A nom/1 A min, 38-60 V, 50 kHz, Lp = 56.6 uH, Co = 5000 uF, Rc = 0.012 Ohm): Ro = 0.5 Ohm -> +12.8 dB, pole 63.7 Hz, Fesr 2500 Hz; Fco = 10 kHz, plant -19 dB -> EA +19 dB; EA pole 1 kHz, zero 300 Hz; R1 = 1 k, R2 = 79 k, C2 = 2000 pF, C1 = 6700 pF; Ro = 5 Ohm -> +23 dB, pole 6.4 Hz, new Fco 3.2 kHz; PM at Ro = 0.5 Ohm: plant lag 13.6 deg + EA 266 deg = 280 deg -> 80 deg. | theta_plant = atan(Fco/Fp) - atan(Fco/Fesr) ; theta_EA = 270 - atan(Fco/Fz) + atan(Fco/Fp_EA) | — | — | calc | p.599-602, §12.17-12.18, Fig. 12.19 | high |
| PRESSMAN-2188 | filter | Flyback output spike from ESR: at switch turn-off the peak secondary current flows into the output capacitor ESR (66 A x 0.03 Ohm = 2 V for 2000 uF). Reduce by raising Co (ESR roughly inversely proportional to Co: 5000 uF -> 0.012 Ohm -> 0.79 V) and add a small LC post-filter (outside the loop's influence). | V_spike = I_sec,pk * Resr ; Resr ~ 1/Co | I_sec,pk, Resr | DCM flyback output | calc | p.600, §12.18 | high |
| PRESSMAN-2189 | control-loop | Transconductance error amplifiers (1524/1525/1526 family): G = gm*Zo; unloaded open-loop gain +80 dB with a pole at 300 Hz; gm nominal 2 mA/V (Ro = 500 k, 50 k, 30 k -> gains 1000, 100, 60). Type 2 shape with a shunt network to ground: R1 in series with C1, shunted by C2: Fz = 1/(2*pi*R1*C1), Fp = 1/(2*pi*R1*C2), midband gm*R1. | G = gm * Zo ; G_mid = gm * R1 | gm, R1, C1, C2 | 1524/1525-family PWM chips | calc | p.602-604, §12.19, Fig. 12.20 | high |
| PRESSMAN-2190 | control-loop | Chip transconductance EA output can source/sink only 100 uA; to slew the full 3 V ramp range quickly, the compensation resistor must be >= 30 kOhm (else sluggish line/load response). If the required midband gain needs R1 < 30 k, set R1 = 30 k and increase the output filter loss at Fco (lower LC corner by more L or C), or use an external op-amp EA into the chip's EA output pin. | R1 >= 3 V / 100 uA = 30 kOhm | I_EA,max, V_ramp | 1524/1525-family | calc | p.604-605, §12.19 | high |
| PRESSMAN-2191 | power | Hard-switched MOSFET turn-on loss from output capacitance becomes very important above ~1 MHz (significant from 500 kHz to 1 MHz); dissipative RCD snubbers only move loss to the resistor, and non-dissipative snubbers are troublesome above 200 kHz — beyond these limits use resonant (ZCS/ZVS) techniques. | P_Coss = 0.5 * C * Vmax^2 / T | C_oss, Vmax, fsw | high-frequency converters | calc | p.607-608, §13.1-13.2; p.625, §13.5.6 | high |
| PRESSMAN-2192 | power | Resonant converters: ZCS (switch turned on/off at current zero of a resonant sine) eliminates turn-off overlap loss; ZVS makes the MOSFET output capacitance part of the resonant tank so its energy returns to the bus. Reported efficiencies 80-97% and DC/DC power densities above 50 W/in^3 (usually needing an external cold plate not counted in the density). | eta = 80-97% (reported) | — | resonant topologies | review | p.608, §13.2 | high |
| PRESSMAN-2193 | power | Resonant converters carry higher peak transistor currents than square-wave PWM for the same power (most have sine currents 3-4x the PWM square-wave amplitude) and may impose larger voltage stress; they cope poorly with large line/load changes and are tolerance-sensitive. Example: resonant forward at 15 W, 120 V has 1.5 A peak vs Ip = 3.13*15/120 = 0.39 A for a PWM forward (which fits a smaller 1811 pot core at 150 kHz, 19.4 W). | I_pk,resonant ~ 3-4 x I_pk,PWM | Po, Vdc | topology selection | calc | p.609, §13.2; p.614, §13.3.1; p.627, §13.6 | high |
| PRESSMAN-2194 | power | Resonant forward converter (DCM, ZCS, parallel-loaded): resonance between leakage (plus added) inductance and the secondary capacitor reflected to the primary. MOSFET on-time must exceed one resonant half period and be less than a full period (turn off during the reverse half-cycle while the anti-parallel diode conducts). Output regulated by varying switching frequency (Fs down when Vdc up or load down). | Fr = 1/(2*pi*sqrt(Lr * Cr * (Ns/Np)^2)) (Eq. 13.1) ; 0.5/Fr < t_on < 1/Fr | Lr, Cr, Ns/Np | discontinuous resonant forward | calc | p.609-611, §13.3, Fig. 13.1 | high |
| PRESSMAN-2195 | magnetics | Resonant forward worked data (Lee & Liu): 32 W (5.2 V, 6.2 A), 150 V input, 856 kHz, 10:1 transformer; resonant half period 0.2 us (Fr = 2.5 MHz); 0.15 uF secondary cap reflects as 0.0015 uF -> Lr = 1/(4*pi^2*Fr^2*C) = 2.7 uH. Such small Lr is dominated by wiring/leakage spread; add discrete inductance to make Lr production-insensitive (lowers max fsw; raising Lr/Cr lowers the achievable peak current ~ 1/sqrt(Lr/Cr)). Minimum spacing between pulses must allow full core reset (reflected-C ring back to zero). | Lr = 1/(4*pi^2*Fr^2*Cr_reflected) ; Cr_reflected = Cs * (Ns/Np)^2 | Fr, Cs, turns ratio | resonant forward | calc | p.612-614, §13.3.1, Fig. 13.2 | high |
| PRESSMAN-2196 | hw-fw | Variable-frequency regulation can be unacceptable: computer systems often require the supply switching frequency synchronized to a submultiple of the system clock; CRT displays need it phase-locked to the horizontal line rate (otherwise "herringbone" interference). | f_sw = f_clock / n (synchronized) | clock, sync requirement | resonant/variable-frequency supplies | review | p.611-612, §13.3 | high |
| PRESSMAN-2197 | control-loop | CCM resonant converters regulate by moving fsw along one side of the resonant curve (above resonance ARM or below BRM); if tolerances or transients move operation across the resonant peak, the loop feedback polarity reverses (positive feedback). Ensure the lowest operating frequency at minimum Vdc and minimum Q never crosses the peak over all LC tolerances; a fixed minimum-frequency clamp is impractical because the peak shifts with production spread. Steigerwald prefers ARM. | f_sw,min(Vdc_min, Q_min) > f_peak,max(LC tolerance) (ARM) | L, C tolerance, Q range | CCM SRC/PRC/LCC | calc | p.614-616, §13.4.1; p.620-623, §13.5.3-13.5.5 | high |
| PRESSMAN-2198 | power | Half-bridge resonant AC gain (fundamental approximation, Steigerwald). SRC (load in series, capacitive output filter, no output inductor; good for high-voltage outputs, good light-load efficiency, cannot regulate at no/light load). PRC (load across Cr, needs large output inductor; for low-voltage high-current, regulates to no load, but circulating current and poor light-load efficiency; not inherently short-circuit proof). | SRC: Vo/Vin = 1/(1 + j*(Xl/Rac - Xc/Rac)), Rac = 8*RL/pi^2, Q = wo*L/RL (Eq. 13.2) ; PRC: Vo/Vin = 1/(1 - Xl/Xc + j*Xl/Rac), Rac = pi^2*RL/8, Q = RL/(wo*L) (Eq. 13.3) | L, C, RL (reflected), f | CCM half bridges | calc | p.616-622, §13.5.1-13.5.4, Figs. 13.5-13.7 | high |
| PRESSMAN-2199 | power | SRC regulation example (Fig. 13.6): Q = 2 at normalized f 1.3 gives gain 0.6; Q = 5 needs f ~1.15; Q = 1 needs ~1.62 — frequency range grows as Q falls; at open circuit regulation is impossible. PRC (Fig. 13.7): Q = 2 at 1.1 -> Q = 5 at ~1.23; a sudden load removal near the peak at low Q can drive the output dangerously high before the loop corrects. | — | Q, fn | SRC/PRC | calc | p.620-621, §13.5.3-13.5.4 | high |
| PRESSMAN-2200 | power | LCC (series-parallel) resonant converter combines SRC light-load efficiency with PRC no-load regulation; Steigerwald's best compromise is Cp = Cs (Cp >> Cs brings PRC light-load inefficiency). | NVodc/(0.5*Vin) = (8/pi^2) / (1 + Cp/Cs - w^2*L*Cp + j*Qs*(w/ws - ws/w)) ; Qs = Xl/Rl, ws = 1/sqrt(L*Cs) ; Cp = Cs recommended | L, Cs, Cp, Rl | CCM half-bridge LCC | calc | p.622-623, §13.5.5, Fig. 13.8 | high |
| PRESSMAN-2201 | power | ZVS half bridge (Jovanovic, Tabisz, Lee): MOSFET output capacitances C1, C2 are part of the resonant circuit; during the dead time the rectifiers short the secondary and the stored energy rings through the resonant L back to the bus, so the next switch turns on at zero voltage and the capacitor slows the turning-off switch's voltage rise. | — | L, Coss | ZVS half bridge (CCM) | review | p.623-626, §13.5.6, Figs. 13.9-13.10 | high |
| PRESSMAN-2202 | process | Resonant-converter adoption checklist (author): compare with 200-300 kHz PWM power density; is +3-6% efficiency worth complexity and limited line/load range; will production units need per-unit tuning; does higher peak sine current (3-4x) negate the RFI advantage (di/dt at zero crossing proportional to peak); will users accept variable frequency; DCM is more predictable than CCM. | efficiency gain 3-6% (typical claim) | — | architecture review | review | p.627-628, §13.6 | high |
| PRESSMAN-2203 | test | Forward converter drain current verification: current at the centre of the ramp-on-a-step should equal the flat-topped equivalent Ipft; peak current stays constant as Vdc changes (only pulse width changes). Measured: 80 W at Vdc = 38 V -> 6.57 A, matched on scope. | Ipft = 3.12 to 3.13 * Po / Vdc_min (Eq. 2.28) | Po, Vdc | forward converter, CCM output inductors | measure | p.633, §14.2.1, Fig. 14.2 | high |
| PRESSMAN-2204 | magnetics | Forward converter on-time at low line should be close to 80% of a half period (design value); integer rounding of secondary turns (4.5 -> 5) raises secondary voltage and shortens on-time. | ton(Vdc_min) ~= 0.8 * T/2 | Ns rounding | forward converter | measure | p.634-635, §14.2.1 | high |
| PRESSMAN-2205 | protection | Measured leakage spikes (125 kHz, 100 W forward, 48 V telecom): 21% above 2Vdc at Vdc = 60 V and 64% above 2Vdc at 38 V at 80% load; smaller at 40% load. After the spike the drain sits at 2Vdc until reset volt-seconds equal set volt-seconds, then falls to Vdc. | V_ds: 2*Vdc during reset until Vdc*ton = (2Vdc - Vdc)*t_reset | Vdc, ton | forward converter with Nr = Np | measure | p.635, §14.2.1 | high |
| PRESSMAN-2206 | magnetics | 125 kHz forward converter reached 87% average efficiency (38-60 V, 80% load) at 1600 G peak with Ferroxcube 3F3, core rise < 25 C; not achievable with higher-loss 3C8; larger 3F3 cores at 125 kHz would need 1400 or even 1200 G. At 40% load efficiency averaged 90%. | Bpk = 1600 G (3F3, 125 kHz, small core) | material, f, core size | ferrite forward transformers | measure | p.635, §14.2.1-14.2.2 | high |
| PRESSMAN-2207 | power | Turn-off overlap loss exceeds turn-on overlap loss in transformer-coupled converters (leakage inductance makes Vds fall fast and Id rise slowly at turn-on; at turn-off Id holds at peak while Vds rises to 2Vdc). Measured (125 kHz forward, 48 V): 2.18 W turn-off vs 1.4 W turn-on. | P_off > P_on | V, I waveforms | forward converter | measure | p.635-638, §14.2.3, Fig. 14.4 | high |
| PRESSMAN-2208 | test | Output inductor ripple check: dI = (V_L,on) * ton / L; example (16 - 5 V) * 2.4 us / 17 uH = 1.55 A calculated vs 1.4 A measured. Push-pull 5 V output: L1 = (7.5 - 5 V) * 1.45 us / 1.8 A = 2.0 uH measured vs 1.8 uH from 5 turns on MPP 55120 (Al = 72 mH/1000 T). | L = (Vcathode - Vo) * dt / di | Vcathode, Vo, ton, di | buck-derived output filters | measure | p.638-639, §14.2.5; p.656, §14.3.11 | high |
| PRESSMAN-2209 | magnetics | Practical switching frequency ceiling (author's 85 W, 48 V push-pull): above ~200 kHz transformer and output filter size gains shrink rapidly while core and copper losses rise sharply — questionable trade. | f_sw <= ~200 kHz (PWM, ferrite, ~100 W class) | f, P | conventional PWM transformers | review | p.641, §14.3 | medium |
| PRESSMAN-2210 | magnetics | Push-pull flux-imbalance check: alternate transformer centre-tap current pulses must have equal amplitude; with MOSFETs (no storage time) and equal gate pulse widths no imbalance was seen without any rds matching. | I_pk(Q1) = I_pk(Q2) | centre-tap current | MOSFET push-pull | measure | p.642, §14.3.1, Fig. 14.9 | high |
| PRESSMAN-2211 | magnetics | Leakage inductance is small at high frequency (few turns, good coupling) and further reduced by sandwiching secondaries between the two half primaries: measured spike only ~5 V above 2Vdc (85 W) and ~20 V above 2Vdc at 112 W, 200 kHz. | — | winding order | push-pull transformers | inspect/measure | p.642, p.644, §14.3.1-14.3.2 | high |
| PRESSMAN-2212 | test | A clamp-on current probe in a push-pull transformer centre tap gives false absolute current (probe core cannot reset during the short dead time): 2.4 A read vs 4.4 A true; 700 mA read vs 15 A true at light load. Measure in the drain lead or across a source sense resistor. | — | probe placement | push-pull, short dead time | measure | p.642-644, §14.3.1, §14.3.4, §14.3.9 | high |
| PRESSMAN-2213 | magnetics | Push-pull dead time: core flux stays locked at +/-Bmax (not remanence ~100 G) because primary magnetizing current transfers by flyback action into a half secondary; drains sit at Vdc during dead time. If flux fell to remanence the next half cycle would swing to 100 G + 2*Bmax and saturate. | — | — | push-pull / bridge | review | p.644-647, §14.3.2 | high |
| PRESSMAN-2214 | test | Output ripple measurement: use a differential probe with good HF common-mode rejection (MOSFET edges produce CM ringing above 50 MHz); remove the probe ground lead and use the ground ring at the point; test whether noise is CM by shorting the probe tip to its shortest ground lead at the output return — if the reading persists it is common-mode. Measured 5 V ripple+noise ~80 mV p-p. Suppress CM noise with an output CM filter/balun; typical CM injection points are switch-to-chassis heat-sink mounts. | — | probe setup | all SMPS outputs | measure | p.647-649, §14.3.5 TIP | high |
| PRESSMAN-2215 | power | Master-regulated multi-output: rectifier-cathode (pre-LC) waveforms must have steep sides and no dead-time bumps/ledges; extra volt-second area on the master makes the loop shorten on-time and drops the slave outputs (23 V slave: 23.74 V at full load vs 21.52 V at 1/5 load with a dead-time ledge). | — | cathode waveform | forward/push-pull slaves | measure | p.649-650, §14.3.5; p.652-655, §14.3.8 | high |
| PRESSMAN-2216 | emc | Output rectifier ringing at switch turn-on (off-going diode capacitance with output inductor; amplitude set by reverse recovery and load current) causes RFI, over-voltage stress and dissipation: fit RC snubbers across each output rectifier. | — | diode trr, Cj | output rectifiers | measure | p.650, §14.3.6, Fig. 14.11-14.12 | high |
| PRESSMAN-2217 | power | Best-case MOSFET turn-off overlap (current starts falling as voltage starts rising, both complete together): energy-average over tf = Imax*Vmax/6; example 4.2 A x 85 V / 6 = 59.5 W over a ~40-45 ns fall -> 0.48 W averaged over the 5 us period. | P_sw = (Imax*Vmax/6) * tf / T | Imax, Vmax, tf, T | fast MOSFET turn-off | calc | p.650, §14.3.7 | high |
| PRESSMAN-2218 | magnetics | Push-pull magnetizing current vs minimum load: if the magnetizing current reflected into the master secondary exceeds the master output inductor current (gap too large, core halves separated, or load below spec minimum), the rectifier cathodes unclamp in dead time (bump), slave voltages drop, and in the extreme spurious "double turn-on" and erratic/oscillating loop behaviour occur. | I_o,min(master) > I_mag * (Np/Ns_master) | I_mag, Np/Ns, I_o,min | push-pull/bridge with slaves | calc/measure | p.652-659, §14.3.8, §14.3.15, Fig. 14.16 | high |
| PRESSMAN-2219 | emc | Fit RC snubbers across each half primary of a push-pull to suppress high-frequency ringing throughout the dead time (it worsens RFI and shifts slave voltages like the dead-time ledge). | — | — | push-pull | measure | p.659-660, §14.3.17, Fig. 14.17 | high |
| PRESSMAN-2220 | power | Measured push-pull (200 kHz, 85 W rated, 1600 G): efficiency > 81.9% at full load (3-4% more available with larger wire / lower Bpk); ~80% at 1/5 load (worst 78.7% at 59.8 V); at 15% overload > 83% with transformer rise 54 C; at 112 W > 86% with 65 C rise. | — | — | reference data | measure | p.644, p.652, p.659, §14.3 | high |
| PRESSMAN-2221 | power | Single-ended DCM flyback is the simplest topology up to ~60 W; above 60 W its RCD snubber dissipation of leakage energy becomes significant — use the double-ended flyback (returns leakage energy to the bus) above 60-75 W. | P_o <= 60 W (single-ended) ; > 60-75 W -> double-ended | Po | flyback selection | review | p.660-661, §14.4.1 | high |
| PRESSMAN-2222 | protection | Flyback RCD snubber capacitor: at turn-off all primary current transfers to the snubber capacitor until leakage energy is absorbed; C2 must be large enough to keep the spike safe but not so large that R dissipation is excessive. After the spike the drain sits at Vdc + (Np/Ns)*(Vo + VD) until reset volt-seconds equal set volt-seconds. | P_R = 0.5 * C2 * Vpeak^2 / T ; E_leak = 0.5 * L_leak * Ip^2 ; V_ds,flat = Vdc + (Np/Ns)*(Vo + VD) | C2, Vpeak, Lleak, Ip | single-ended flyback | calc/measure | p.662, §14.4.2; p.665-666, §14.4.4 | high |
| PRESSMAN-2223 | power | Multi-output flyback slave voltage depends on master load: master secondary leakage diverts current into the slave rectifier right after turn-off, peak-charging the slave through a pedestal (20 V -> 28 V pedestal as master current rose 2.08 A -> 6.58 A). Remedy: minimize secondary leakage inductances; add a small series inductor in the slave secondary. | — | leakage, master current range | multi-output flybacks | measure | p.662-665, §14.4.3, Fig. 14.21 | high |
| PRESSMAN-2224 | power | Power factor = cos(phase angle) for sinusoidal waveforms; real power = apparent power (Vrms*Irms) x PF. Capacitor-input rectifiers draw narrow, fast-edged current pulses near the voltage peak (larger C -> narrower, higher peak and rms) causing high rms current, filter-capacitor heating/reduced reliability, distribution losses and RFI. PFC forces line current to track the (haversine) line voltage. | P = Vrms * Irms * PF ; PF = cos(x) (sinusoidal) | Vrms, Irms, phase | off-line supplies | calc/measure | p.669-672, §15.1-15.2, Figs. 15.1-15.2 | high |
| PRESSMAN-2225 | power | Boost PFC: remove the bulk capacitor after the bridge (use only a small capacitor) so the rectified voltage is a haversine; a CCM boost converter modulates on-time to keep Vo constant slightly above the line peak while an inner current loop forces the line current to follow a reference haversine (multiplier mixes voltage-error and line reference). | Vo = Vin / (1 - Ton/T) (Eq. 15.1) ; Vo > sqrt(2)*Vrms,max | Vin(t), Ton, T | boost PFC front ends | calc | p.673-676, §15.3, Fig. 15.3-15.4 | high |
| PRESSMAN-2226 | power | CCM boost (large L1) gives small switching ripple on the line current (sum of switch and diode ramp-on-step currents), unlike DCM/critical-conduction boost whose large triangular ramps generate more switching noise. A small capacitor across the current sense resistor suppresses narrow switching spikes on the sensed half-sinusoid. | — | L1 | PFC mode choice | review | p.676-678, §15.3.1, Fig. 15.5 | high |
| PRESSMAN-2227 | control-loop | CCM boost load-current regulation needs a few switching cycles of current build-up with Vo briefly displaced, so the output-voltage error amplifier bandwidth must be kept low (also to minimize line-current harmonic distortion: low gain beyond the 3rd line harmonic). PFC has a fast wide-band inner current loop and a slow outer voltage loop. | f_BW,voltage << line frequency harmonics (low gain beyond 3rd harmonic) | loop BW | boost PFC | calc/measure | p.679-680, §15.3.3; p.690-691, §15.4.9 | high |
| PRESSMAN-2228 | power | PFC does not improve the power supply's own efficiency: extra components normally increase internal loss and temperature rise; savings are in external RFI filters, lines and distribution. A true wattmeter shows higher real input power for the PFC unit. | P_loss(PFC unit) > P_loss(uncorrected) | — | expectation setting | review | p.681, §15.3.3 After Pressman | high |
| PRESSMAN-2229 | power | UC3854 PFC output-power setting: choose peak sensed line current from minimum-line power; select Rs for ~1 V peak drop at low line, max load (not less than 1 V); multiplier output current limit fixed by R14 (up to 0.5 mA, usually 0.25 mA); R2 matches Rs drop at max current (R3 = R2 for drift). Example 250 W, 90 Vrms min, E = 0.85: Irms = 3.27 A, Ip1 = 4.61 A, Rs = 1/4.61 = 0.22 -> 0.25 Ohm, R14 = 3.75/0.00025 = 15 k, R2 = 4.61*0.25/0.00025 = 4.61 k. | Po = E * Vrms * 0.707 * Ip1 (Eq. 15.2) ; Rs = 1 V / Ip1 (Eq. 15.3) ; Ipmd = 3.75/R14 (Eq. 15.4) ; R2 = Ip1*Rs/Ipmd (Eq. 15.5) | Po, Vrms_min, E | UC3854 designs | calc | p.685-687, §15.4.4, Fig. 15.9 | high |
| PRESSMAN-2230 | power | UC3854 switching frequency: Fs = 1.25/(R14*C11) (R14 in Ohm, C11 in F); usable to somewhat above 200 kHz, generally ~100 kHz. | Fs = 1.25 / (R14 * Ct) (Eq. 15.6) | R14, Ct | UC3854 | calc | p.681, p.687, §15.4.1, §15.4.5 | high |
| PRESSMAN-2231 | magnetics | CCM boost PFC inductor: sized at minimum line and maximum power for a chosen p-p ripple at the sine peak (author: dI = 20% of the peak line current); set Vo 10% above the peak at maximum line. For Vrms 90-250 V: Ton(max) = T*(1 - 1.1^-1 * 90/250) = 0.673 T. Example 250 W, 100 kHz, E = 0.85 -> L1 = 928 uH. | L1 = 1.41*Vrms_min*Ton/dI (Eq. 15.7) ; Ip1 = 1.41*Po/(E*Vrms_min) (Eq. 15.8) ; dI = 0.2*Ip1 = 0.282*Po/(E*Vrms_min) (Eq. 15.9) ; L1 = 5.0*Vrms_min^2*E*Ton/Po (Eq. 15.10) ; Ton = T*(1 - Vp/Vo) (Eq. 15.11) ; L1 = 3.37*Vrms_min^2*T*E/Po (Eq. 15.14, 90-250 V range) | Vrms_min, Vrms_max, Po, E, T | CCM boost PFC | calc | p.687-688, §15.4.6 | high |
| PRESSMAN-2232 | power | PFC boost output voltage: set nominal Vo at least 10% above the line peak at maximum rms input (250 Vrms -> 388 V); it is loosely regulated (low voltage-loop bandwidth) — assume minimum ~370 V for downstream design. Downstream converter: half bridge below ~600 W, full bridge above. | Vo,nom >= 1.1 * 1.41 * Vrms_max | Vrms_max | boost PFC + DC/DC | calc | p.688-689, §15.4.7 | high |
| PRESSMAN-2233 | power | Bulk capacitor hold-up: size Co to keep the DC/DC input above Vmhu for the hold-up time Thu (often specified 30 ms) from the minimum operating Vo; choose Vmhu 60-80 V below Vo and design the DC/DC transformer so on-time at Vmhu is still only 80% of a half period. Example: Vo = 370 V, Vmhu = 300 V, 30 ms, Pc = 250 W, Ec = 0.85 -> Iav = 0.88 A -> Co = 378 uF (use 390 uF). | Co = Iav * Thu / (Vo - Vmhu) (Eq. 15.15) ; Iav = 2*Pc / (Ec*(Vo + Vmhu)) (Eq. 15.16) ; Vo - Vmhu = 60-80 V | Pc, Ec, Vo, Vmhu, Thu | PFC bulk / off-line bulk caps | calc | p.688-690, §15.4.7, Fig. 15.10 | high |
| PRESSMAN-2234 | components | PFC bulk capacitor ripple current: the boost diode current contains the DC load current plus a 120 Hz component with peak equal to the DC current, which flows in Co. Example 250 W, 388 V, 85% -> Idc = 0.76 A -> 0.54 A rms rating. | I_ripple,rms(Co) = 0.707 * Idc (120 Hz) | Idc | boost PFC output capacitor | calc | p.690, §15.4.7 | high |
| PRESSMAN-2235 | protection | UC3854 peak current limit: level-shift network from the 7.5 V reference; limit at I1p where Rs*I1p = IR4*R4, IR4 = 7.5/R5. Example R5 = 10 k (0.75 mA); limit 5.5 A (vs 4.61 A peak) with Rs = 0.25 -> R4 = 1.8 k. | R4 = Rs * I1p / IR4 (Eq. 15.17) ; IR4 = 7.5 V / R5 | Rs, I1p, R5 | UC3854 | calc | p.690, §15.4.8 | high |
| PRESSMAN-2236 | control-loop | UC3854 inner current amplifier EA2 is a Type 2 amplifier: zero Fz = 1/(2*pi*R6*C15), pole Fp = 1/(2*pi*R6*C13), pole at origin 1/(2*pi*R3*(C13 + C15)). | as stated | R6, R3, C13, C15 | UC3854 | calc | p.691, §15.4.9 | high |
| PRESSMAN-2237 | power | Critical-conduction (boundary-mode) PFC (MC34261): fixed on-time, variable off-time, current falls to zero before each turn-on (zero-current turn-on, larger ramps, more noise). Both boundary- and CCM-controller vendors claim PF > 0.99. Peak switch current is twice the peak line current. | Toff = Ton * Vin / (Vo - Vin) (Eq. 15.18) ; Ipkt = 2.82*Po/(E*Vrms_min) (Eq. 15.19) ; L = Vrms_min^2 * Ton * E / (2*Po) (Eq. 15.20) | Vin(t), Vo, Po, E, Ton | boundary-mode boost PFC (85-265 Vac) | calc | p.691-696, §15.5, §15.5.3, Fig. 15.12 | high |
| PRESSMAN-2238 | emc | Boundary-mode PFC frequency varies widely with line and within each haversine (wide spectrum RFI/EMI risk). Example 80 W, 92-138 Vrms, E = 0.95, Ton = 10 us -> L = 500 uH, Ipkt = 2.59 A; Vo = 245 V (50 V above 195 V high-line peak): 48 kHz at low-line peak, 20 kHz at high-line peak, 99 kHz near the 10 deg point. Keep large inductances (> 1 mH that must not saturate above 2 A) out — they are big and expensive; a low boost voltage stretches off-time (low frequency), a high boost voltage raises switch stress and diode recovery loss. | f_sw = 1/(Ton + Toff(Vin(t))) | Ton, Vo, Vin range | MC34261-type controllers | calc | p.695-696, §15.5.3 | high |
| PRESSMAN-2239 | power | MC34261 sensing and multiplier: R9 = Vcs/Ipkt with Vcs = 0.5 V (92-138 Vrms) -> 0.19 Ohm for 2.58 A; multiplier input (pin 3) must stay below 3 V to avoid haversine distortion — set VM = 3.0 V at the high-line peak: R3 = 0.016*R7 (138 V), start with R7 ~ 1 MOhm and trim R3 for lowest line-current distortion. | R9 = 0.5 V / Ipkt ; VM,pk = 1.41*Vac*R3/(R3 + R7) <= 3 V | Ipkt, Vac_max | MC34261 | calc/measure | p.693, p.696-697, §15.5.1, §15.5.4 | high |
| PRESSMAN-2240 | power | Fluorescent lamps have negative incremental resistance: they need a current-limiting ballast impedance and cannot be driven from a low-impedance voltage source (runaway). | — | lamp V-I | discharge lamps | review | p.699-700, §16.1 | high |
| PRESSMAN-2241 | power | High-frequency (> 20 kHz) lamp drive: efficacy rises with frequency up to ~20 kHz then levels off (~14% gain); no flicker/restrike at zero crossings; above 20 kHz the ionized gas does not recombine. Electronic ballast replacing magnetic cut fixture power 227 W -> 87 W for the same light (1-year payback); total power-cost reduction typically 20-25%. Fluorescent 75 lm/W (90-100 lm/W newest with electronic ballasts) vs incandescent 18 lm/W. | f_lamp > 20 kHz | f | electronic ballasts | review | p.701-703, §16.1; p.709-711, §16.3.2, Figs. 16.2, 16.9 | high |
| PRESSMAN-2242 | power | Lamp current crest factor (peak/rms) should be low: high crest factors (typical of 60 Hz magnetic ballasts) give poor lamp efficiency; a perfect sine is 1.41. | CF = I_pk / I_rms (sine = 1.41) | lamp current | ballasts | measure | p.710, §16.3.2 | high |
| PRESSMAN-2243 | power | Ballast impedance sets lamp operating current; lamp power = Vop*Iop (V and I in phase at HF). Striking voltage: use manufacturer nominal Vns (usually at 50 F) with ~10% extra to start the hardest lamp; ANSI specifies Vop and Iop per lamp type. Capacitor ballast value from its reactance. Running above ANSI rating raises light output but shortens life; running at rated watts but non-rated current may also shorten life. | Iop = (Vns - Vop)/Xb (Eq. 16.1) ; Pin = Vop*Iop (Eq. 16.2) ; Xb = 1/(2*pi*f*CbT) (Eq. 16.3) ; Vns_design >= 1.1 * Vns,nom | Vns, Vop, Iop, f | capacitor-ballasted fluorescent lamps | calc | p.711-712, §16.3.3, Figs. 16.10-16.11 | high |
| PRESSMAN-2244 | compliance | Lamp ballasts must include power factor correction meeting IEC555-2 (limits input line harmonic content) and meet EMI/RFI limits of FCC CFR 47 Part 18. | PFC per IEC555-2 ; EMI per FCC CFR 47 Part 18 | — | electronic ballasts (as stated at time of writing) | review | p.715, §16.4 | high |
| PRESSMAN-2245 | power | Ballast inverter topology: push-pull for 120 VAC, half bridge for 220/230 VAC; self-resonant LC oscillators (20-50 kHz) rather than fixed-frequency PWM. Current-fed variants: extra inductor(s), higher off-state stress, but clean sine waves, tolerate open/short lamps indefinitely and drive several lamps in parallel. Voltage-fed variants: lower voltage stress but start-up current transients 5-10x operating current (depends on Q), single lamp, harder to make reliable. Author prefers current-fed given cheap high-voltage transistors. | I_startup(voltage-fed) = 5-10 x I_op | topology | electronic ballasts | review | p.715-718, §16.5-16.6; p.737-740, §16.7 | high |
| PRESSMAN-2246 | derating | Sinusoidal/alternating base drive gives automatic reverse bias in the off half cycle, allowing a bipolar to use its Vcev rating (100-300 V above Vceo, with 2-5 V negative base bias) instead of Vceo. | V_ce,off <= Vcev only if reverse base bias of 2-5 V present | base drive waveform | self-oscillating ballasts | review | p.716, §16.5 | high |
| PRESSMAN-2247 | derating | Current-fed push-pull voltage stress: centre tap is a full-wave rectified sine of peak (pi/2)*Vdc; the off transistor sees pi*Vdc. 120 VAC +15% -> 195 V peak; PFC ~20 V above -> Vdc ~205 V -> transistor must sustain pi*205 = 644 V. Current-fed half bridge: (pi/2)*Vdc (400 V -> 628 V, 700 V parts); voltage-fed push-pull: 2*Vdc; voltage-fed half bridge: Vdc. Current-fed push-pull on 400 V (230 VAC) would need pi*400 = 1257 V — use the half bridge. | V_ce,pk: CF push-pull = pi*Vdc ; CF half bridge = (pi/2)*Vdc ; VF push-pull = 2*Vdc ; VF half bridge = Vdc | Vdc, topology | resonant ballast inverters | calc | p.720-721, §16.6.2; p.738-742, §16.7-16.9 | high |
| PRESSMAN-2248 | power | Current-fed push-pull ballast design: ballast capacitor from striking/operating voltages; average collector current from lamp power. Example 2 x 40 W, E = 0.9, Vdc = 205 V -> Icav = 434 mA. | I_lamp,rms = (0.707*Vns - V_l,rms)*(2*pi*fr*C4) (Eq. 16.4) ; Icav = 2*P_lamp/(E*Vdc) (Eq. 16.5) | Vns, Vl, fr, P_lamp, E, Vdc | current-fed parallel-resonant push-pull | calc | p.720-721, §16.6.1-16.6.2 | high |
| PRESSMAN-2249 | magnetics | Current-feed inductor LCF: choose so its current ripple is a small fraction (author: +/-20%, 0.4 x 434 mA = 174 mA p-p) of Icav; LCF = volt-second area between centre-tap waveform and Vdc (~800e-6 V*s) / dI -> 4.6 mH, use ~4.0 mH; design core for ~2x normal current (turn-on transients); inductor ripple frequency = 2x oscillation frequency (50 kHz for 25 kHz). | LCF = (integral of V_L dt) / dI (Eq. 16.6) ; N = 1000*sqrt(L(mH)/Al(mH/1000T)) (Eq. 16.7) ; Bm = (V*s area)*1e8/(N*Ae) (Eq. 16.8) ; Hm = 0.4*pi*N*I/lm (Eq. 16.9), I = 2*Icav | V*s area, dI, Al, Ae, lm | current-fed ballast | calc | p.721-724, §16.6.3-16.6.4 | high |
| PRESSMAN-2250 | magnetics | Core choice for a 4 mH current-feed choke (50 kHz ripple, 1000 G loss comparison, Table 16.1): MPP $14.00 / 180 mW/cm^3; Kool Mu $4.20 / 300; gapped ferrite 3C85 (3019 pot, two halves) $2.20 / 30; Micrometals #26 $0.34 / 2000. Result: Kool Mu 77439 (172 T, 85 mW, OD 1.84 in), Micrometals 250-26 (129 T, 855 mW, OD 2.5 in), ferrite 3019 pot with 35-mil gap (138 T, NImax 138 At < 170 At cliff, 423 G, ~5 mW/cm^3 x 6.19 cm^3 = 31 mW). 2616 pot fails (NImax at or beyond cliff). Recover inductance falloff by raising turns by the square root of the falloff. | NI_max < NI_cliff (gapped ferrite) ; N_new = N * sqrt(1/(1 - falloff)) | Al vs gap, cliff At | low-ripple chokes | calc | p.722-729, §16.6.4, Tables 16.1-16.5 | high |
| PRESSMAN-2251 | current-carrying | Ballast coil sizing at 500 circular mils per rms ampere: 434 mA -> 217 CM -> #26 (253 CM); check turns per layer and layers against bobbin width/height; skin effect negligible at 50 kHz for small AC ripple. | A(CM) = 500 * I_rms | I_rms | low-ripple chokes | calc | p.729, §16.6.5 | high |
| PRESSMAN-2252 | magnetics | Parallel-resonant ballast transformer: primary carries the circulating tank current, not just load current — compute I = V_tank,rms/(2*pi*f*Lt). Lt is limited by resonance with Ct = C1 + reflected ballast caps; keep C1 about equal to the reflected ballast capacitance so frequency shift between unlit, one-lamp and two-lamp states stays moderate; turns ratio Ns/(2Np) > 1 gives no advantage. Example 25 kHz, Vop 101 V, Iop 430 mA, Vs 455 V: Xb = 823 Ohm, Cb = 0.0077 uF, Ct = 0.03 uF, Lt = 1.35 -> 1.5 mH, tank current 1.93 A rms (vs 0.41 A load-based) -> E21 core too small; ETD44 / 783E608 fit. | Lt = 1/(4*pi^2*Fr^2*Ct) (Eq. 16.11) ; I_prim = V_rms/(2*pi*f*Lt) | Ct, Fr, V_tank | current-fed parallel-resonant ballasts | calc | p.729-736, §16.6.6, Tables 16.6-16.7 | high |
| PRESSMAN-2253 | magnetics | Resonant ballast transformer primary turns from half-period volt-seconds of a half sinusoid (CGS): Np = (2/pi)*Vp*(T/2)*1e8/(Ae*dB), with dB = 2*Bm; author uses Bm = 2000 G at 25 kHz with 3F3/type P ferrite (75 mW/cm^3 at 2000 G, 25 kHz). Example Vp = 322 V, T/2 = 20 us, Ae = 1.49 cm^2, dB = 4000 G -> 69 turns per half primary. | Np = (integral_0^pi V dt)*1e8/(Ae*2*Bm) (Eq. 16.10) | Vp, T, Ae, Bm | sinusoidal-drive transformers | calc | p.730-731, §16.6.6, Fig. 16.18 | high |
| PRESSMAN-2254 | compliance | VDE safety requirements may forbid using the full bobbin width on EE cores (creepage margins), increasing layers and core size; triple-insulated wire can allow full width. Toroids give a longer winding length (pi x ID) so fewer layers (often two), almost no proximity loss and wider spacing between high-voltage turns (less arcing); powder toroids come in only 5-6 discrete Al values unless custom-gapped. | — | winding layout | mains transformers | review | p.737, §16.6.7 | high |
| PRESSMAN-2255 | power | Voltage-fed series-resonant ballast: before the lamp lights RL is high so Q = w*RL*C1 is high and the equivalent series resistance RL/Q^2 (Q >> 1) is tiny — turn-on currents 5-10x normal can pull transistors out of saturation and over-stress the lamp; a series current transformer (proportional base drive with NA/NS = beta_min) adds impedance and ensures base drive. Resonance shifts from 1/(2*pi*sqrt(Lr*Ce)) (Cr, C1 in series) to 1/(2*pi*sqrt(Lr*Cr)) once the lamp shorts C1. | Z_AB = RL/Q^2 + 1/(j*w*C1) for Q >> 1 (Eq. 16.12) ; Q = w*RL*C1 | RL, C1, w | voltage-fed ballasts | calc | p.738-743, §16.7, §16.9, Figs. 16.21, 16.23 | high |
| PRESSMAN-2256 | power | 230 VAC ballast front end: +/-15% line peak = 1.15*1.41*230 = 373 V; PFC boosts to ~400 V. 120 VAC: 195 V peak, PFC ~205 V. | Vdc(PFC) ~= 1.41*1.15*Vac_nom + ~20-30 V | Vac | ballasts with boost PFC | calc | p.740, §16.8 | high |
| PRESSMAN-2257 | power | Integrated low-input-voltage regulators (internal power switch, non-isolated): 60-500 kHz (to 1 MHz), 0.5-100 W, efficiency 80-95%; boost input from 3 V (two cells) to 60 V, buck 4-60 V; externally only L, C, diode and 3-5 resistors. | eta = 80-95% | — | battery/portable, point-of-load | review | p.747-748, §17.1-17.2 | high |
| PRESSMAN-2258 | control-loop | A current-mode boost stabilized for CCM remains stable when light load pushes it into DCM (LTC practice). Current-sense amplifier gain (LT1170: x6) raises the ramp slope without a larger (lossier) sense resistor; a larger comparator signal improves noise immunity (noise on a shallow slope resets the latch early and makes the output unstable). | — | — | current-mode IC boosts | review | p.749-751, §17.3, §17.3.1 | high |
| PRESSMAN-2259 | power | LT1170 boost (100 kHz, 5 A switch, Vin 3-40 V per text / 3-60 V per Table 17.1, switch 65-75 V): Vc (EA output) spans 0.9-2.0 V and is clamped at 2 V to limit peak switch current; clamp Vc lower through a Schottky to a regulated voltage to reduce the current limit, chosen at maximum duty (minimum Vin) from thermal limits. Feedback divider with 1.24 k from FB to ground (1 mA) gives Vo = 1.24 + 0.001*R1. | Vo = Vref + (Vref/R2)*R1 = 1.24 + 0.001*R1 (R2 = 1.24 k) | R1, R2, Vref = 1.24 V | LT1170 family | calc | p.753, §17.3.1 | high |
| PRESSMAN-2260 | test | LT1170 5->12 V test circuit reference performance: 4-8 V line change -> +0.02 V (82 mA, DCM, 84% at 1.2 W) and +0.06 V (823 mA, CCM, worst 81%); 10:1 load change at 5 V in -> 0.03 V; in CCM on-time is constant with load while the step of the ramp-on-step changes; DCM entry shortens on-time. L1 50 uH (18 T #20 on MPP 55930), C 1000 uF, D MBR340P. | — | — | reference data for boost verification | measure | p.753-756, §17.3.2, Figs. 17.3-17.5 | high |
| PRESSMAN-2261 | thermal | IC switching regulator dissipation must be computed early: switch loss = Isw*Vcesat*D plus control-circuit loss = Vin*Iq; derate the 100 C absolute maximum to ~90 C. Example LT1170, 5 A peak, 5 -> 15 V (D = 0.67): Vcesat 0.8 V at 5 A, 100 C -> 2.7 W; Iq = 0.006 + 5*0.0015 + (5/40)*0.66 = 0.096 A -> 0.70 W; total 3.4 W; theta_jc = 2 C/W -> case 85 C; 50 C ambient -> heat sink <= (85-50)/3.4 = 10.3 C/W (larger than the TO-220 package). The heat sink, not the switch current rating, sets the usable peak current. | P_sw = Isw*Vcesat*D ; Iq = 0.006 + 0.0015*Isw + Isw*D/40 (LT1170, beta 40) ; theta_sa = (Tc_max - Ta)/P_tot | Isw, Vcesat, D, Vin, theta_jc, Ta | integrated-switch regulators | calc | p.756-758, §17.3.3, Fig. 17.6 | high |
| PRESSMAN-2262 | power | Inverting and negative-rail relations using IC boost/buck chips (volt-second balance on L1): negative-to-positive or positive-to-negative inverter Vo = -Vin/(T/Ton - 1) = -Vin*Ton/(T - Ton) (Eq. 17.1); negative boost Vo = -Vin/(1 - Ton/T) (Eq. 17.2); boost/buck-based feedback level shifting (current mirror or diode-capacitor sample) adds Vbe/beta/diode-mismatch output errors. | Eqs. 17.1-17.2, 17.4 | Vin, Ton, T | LT1170/LT1074 alternative configurations | calc | p.759-763, p.770-772, §17.3.4, §17.3.8 | high |
| PRESSMAN-2263 | magnetics | Boost inductor to stay continuous down to minimum load: minimum CCM input current Idc_min usually set at 10% of maximum-power input current. Example 5 -> 12 V (Ton = 0.59T at 100 kHz), Idc_min = 0.1 x 2.3 A -> 64 uH (50 uH used; value only sets the CCM boundary). DCM gives poorer load regulation (10-30 mV shift) and more input ripple. | L = Vin_min*(Vo - Vin_min)*T/(2*Vo*Idc_min) (Eq. 17.3) ; Ton = T*(Vo - Vin)/Vo | Vin_min, Vo, T, Idc_min | IC boost regulators | calc | p.764-765, §17.3.6.1 | high |
| PRESSMAN-2264 | filter | Boost output ripple is dominated by ESR because the capacitor alone supplies load current during on-time and receives Io*Vo/Vin during off-time: p-p ripple = ESR*Io*(1 + Vo/Vin) (= 4*Io*ESR for Vo/Vin = 3). Empirical ESR (LTC AN19): Mallory VPR ESR = 200e-6/(C*V^0.6); Sprague 673D/674D ESR = 400e-6/(C*V^0.6) (C in F, V rated volts). Example 5 -> 15 V, 25 W (1.66 A), 200 uF/25 V VPR -> 0.145 Ohm -> 0.963 V p-p. Remedies: lower-ESR (tantalum), more/paralleled capacitors, or a small post LC filter; verify capacitor ripple-current rating (boost capacitor carries full load current each on-time). | V_ripple,pp = Io*ESR*(1 + Vo/Vin) ; ESR ~ k/(C*V^0.6), k = 200e-6 (VPR) or 400e-6 (673D/674D) | Io, Vo/Vin, C, V_rated | boost output capacitors | calc | p.765-766, §17.3.6.2 | high |
| PRESSMAN-2265 | thermal | Boost output diode (usually Schottky, second largest dissipator): P = 0.5 V x average input current during off-time. | P_D = 0.5 * Iin_max * Toff/T = 0.5 * (Pin/Vin_min) * Toff/T | Pin, Vin_min, D | boost regulators | calc | p.767, §17.3.6.3 | high |
| PRESSMAN-2266 | thermal | LT1074 buck thermal example (24 V -> 15 V, 5 A, 100 kHz, triple Darlington 2.2 V drop at 5 A): D = 15/22 = 0.68; switch 2.2*5*0.68 = 7.5 W; control Iin = 0.007 + 0.005*D + 2*Io*Ts*F (Ts = 0.06 us) -> 1.7 W; total 9.2 W; theta_jc 2.5 C/W -> case 71 C for 90 C junction; heat sink rise 21 C at 50 C ambient -> 5.5 x 4.5 in finned sink — no size advantage from the integrated switch. Prefer low-Rds external-MOSFET controllers (LT1142/1143/1148/1149/1430) or single-transistor bootstrapped switches (LT1376: 0.5 V at 1.5 A vs 1.7 V LT1074, 1.25 V LT1076). | P_sw = Vce*Io*D ; P_cc = Vin_min*(0.007 + 0.005*D + 2*Io*Ts*F) | Io, Vce, D, Ts, F | integrated buck regulators | calc | p.773-775, §17.3.8.3, §17.3.9.1 | high |
| PRESSMAN-2267 | power | Synchronous buck with low-Rds P-MOSFET switch and N-MOSFET freewheel (LTC1148) reaches ~95% efficiency; constant off-time, variable frequency. Variable frequency is acceptable in portable equipment without nearby sensitive systems, but synchronized fixed frequency is preferred where RFI pickup by displays/computers matters (unsynchronized noise has a wider spectrum). | Vo = Vin*ton/T = Vin*(1 - f*toff) (Eqs. 17.5-17.6) ; f = (1 - Vo/Vin)/toff (Eq. 17.7) | Vin, Vo, toff | constant off-time bucks | calc | p.775-779, §17.3.9.2-17.3.9.3 | high |
| PRESSMAN-2268 | power | LTC1148 component sizing: sense threshold varies -0.025 to -0.15 V; use 0.100 V max for tolerance; inductor sized for the CCM threshold at the 0.025 V minimum bias; off-time capacitor from ~0.25 mA discharge over ~3 V (text prints 0.0025). Burst mode stops switching at light load for high light-load efficiency. | Rsense = 0.100/Imax (Eq. 17.8) ; L = Vo*toff/(0.025/Rsense) (Eq. 17.9) ; Ct = I*toff/dV (~0.25 mA * toff / 3 V) | Imax, Vo, toff | LTC1148 | calc | p.780-781, §17.3.9.3-17.3.9.6 | medium |
| PRESSMAN-2269 | control-loop | Empirical loop compensation (LTC AN19): inject a ~10% AC-coupled step load (~50 Hz square wave) through a large capacitor, view the output (switching ripple filtered) on a scope; start with series RC on the EA output (Vc pin) of C = 2 uF, R = 1 k (stable but large, slow overshoot); reduce C stepwise until overshoot shrinks, then raise R to remove the reverse-polarity ring; add a small shunt capacitor Vc-to-ground if HF noise spikes appear (series RC alone gives a zero but no HF pole). | start: R3 = 1 kOhm, C2 = 2 uF ; step = ~10% of load at ~50 Hz | step response | IC current-mode regulators | measure | p.783-787, §17.3.12, Fig. 17.15 | high |
| PRESSMAN-2270 | power | Conventional slave outputs regulate to only +/-5-8% against load and up to 50% if an inductor goes discontinuous; volts per turn at high frequency may be 2-3 V/turn, so slaves cannot be set finely. Distributed power alternative: bus a semi-regulated +20 to +25 V and generate each rail with point-of-load IC buck regulators (or boost/inverters from +5 V for low power); prefer a high bus bucked down; a +5 V bus only makes sense for 5 V currents over 10-100 A. With only secondary regulation the primary can run at a fixed ~85% of a half period with peak-rectified capacitor-filtered secondary (no optocoupler/isolated feedback). Benefits: simpler transformer, easier VDE compliance, late changes and added rails without transformer redesign; costs: double conversion, somewhat more dissipation. | E/N = Ae*(dB/ton)*1e-8 (CGS) ; POL input range 3:1 | bus voltage, currents | multi-output system architecture | review | p.787-791, §17.5, Fig. 17.17 | high |

## 2. Formulas & tables (numbers)

### F-2.0 Key formula index (all symbols defined; units as used by the author)
| # | quantity | formula | units / notes | source |
|---|---|---|---|---|
| F1 | Area product | AP = Ae * Aw (Awb for bobbin) | cm^4; one E-core window | p.339, p.347 |
| F2 | Inductance from Al | L = N^2 * Al1 ; Al1 = Aln/N^2 | Al1 in H/turn^2 | p.340-341 |
| F3 | Magnetizing force | H = 0.4*pi*N*I/le | Oe; le cm | p.361, p.399 |
| F4 | AC flux swing | dB = V*t/(N*Ae) | T; V volts, t us, Ae mm^2 | p.364, p.366 |
| F5 | Choke inductance (slope) | L = N*Ae*dB/dI | H with Ae in m^2 | p.362 |
| F6 | Energy storage number | W = 0.5*L*I^2 | mJ with mH, A | p.395 |
| F7 | Minimum turns (Bmax) | N_min = L*I_max*1e4/(B_max*Ae) | L H, I A, B T, Ae cm^2 | p.378 |
| F8 | Gap length | g = mu0*mu_r*N^2*Ae/L | SI (m, m^2, H); butt gap/leg = g/2 | p.378-379 |
| F9 | Full-bobbin wire diameter | d = (Aw*Ku/N)^0.5 | mm, mm^2; Ku = 0.6 (bobbin), 0.4 (toroid) | p.381, p.399 |
| F10 | Full-bobbin resistance | Rx = rho*MLT/Acu ; N = (Rw/Rx)^0.5 ; R2 = R1*(N2/N1)^2 | rho(70 C) = 1.9 uOhm*cm | p.351-352, p.413 |
| F11 | Copper tempco | R(T) = R20*(1 + 0.0043*(T-20)) | +34% at 100 C | p.382 |
| F12 | Thermal-resistance rise | dT = P*Rth ; Wcu = dT/Rth | C, W, C/W | p.347-348 |
| F13 | Surface power density | psi = P/A_surface -> dT (chart) | W/cm^2 | p.400 |
| F14 | Single-ended core loss | P_core = Pv(B_chart = dB/2, f) * Ve | W; Ve cm^3 | p.384-386 |
| F15 | Bipolar overdrive rise | t = tau_a * ln(k/(k-1)) | k = overdrive factor (text: 0.69, 0.4 tau_a) | p.425-426 (medium: fit to text values) |
| F16 | Baker drive primary current | Ip = (Vh - (Np/Ns)*Vs - 1)/R1 | Eq. 8.2 | p.436 |
| F17 | Proportional drive | Nb/Nc = beta_min ; Np = Vh*Nb/2 ; R1 = (Vh/Ic)*(Np/Nc) ; C1 = 4*(Ic/Vh)*(Nc/Np)*toff ; Lp = ton_min/(2*(1/R1 + C1/ton_min)) | Eqs. 8.5-8.11 | p.446-450 |
| F18 | MOSFET gate current | Ig = Ciss*10/tr + Crss*(Vdc+10)/tr ; Cin = Ciss + ((Vdc+10)/10)*Crss | A, F, V, s | p.465-466 |
| F19 | Miller gate spike | V = dVds * Crss/(Crss + Ciss) | must be < 20 V | p.485 |
| F20 | MOSFET rds selection | Ipft*rds(Tj) <= 0.02*Vdc_min ; rds(Tj) = dTjc/(Irms^2*Rth_jc) | Ipft = 3.13*Po/Vdc_min (forward) | p.479-480 |
| F21 | Device dissipation limits | PD = (TJmax - 25)/RthJC ; TJ = TC + P*RthJC | C, W | p.498, p.505 |
| F22 | IGBT switching energy scaling | E = E_ds*V_app/V_test ; t_sw,total <= 0.05*T | — | p.502, p.507 |
| F23 | Mag-amp blocking time | tb = Nm*Ae*(Bs - B1)*1e-8/Vsp | s; cm^2; G | p.519-520 |
| F24 | Mag-amp output | Vos = (Vsp - 1)*tf/T ; tf = th - tb | — | p.514 |
| F25 | Mag-amp gain | Ic = Hc*lp/(0.4*pi*Nm) ; G = Io/Ic | — | p.539 |
| F26 | RCD snubber | C1 = (Ip/2)*tf/(2*Vdc) ; 3*R1*C1 = ton_min ; P_R1 = 0.5*C1*(2*Vdc)^2/T ; P_Q = (Ip/2)*(2*Vdc)*tf/(6*T) | Eqs. 11.1-11.4 | p.549-551 |
| F27 | Leakage spike | V_spike = (Ip/2)*sqrt(Ll/C1) ; V_pk = 2*Vdc + V_spike | — | p.557 |
| F28 | LC filter | Fo = 1/(2*pi*sqrt(Lo*Co)) ; Fesr = 1/(2*pi*Resr*Co) ; Resr*Co ~ 65e-6 s (Al elec.) | Hz | p.565-570, p.583 |
| F29 | PWM gain | Gm = 0.5*(Vsp - 1)/3 (3 V ramp) | V/V | p.570 |
| F30 | Type 2 EA | G = (1+s*R2*C1)/(s*R1*(C1+C2)*(1+s*R2*C2)) ; Fz = 1/(2*pi*R2*C1) ; Fp = 1/(2*pi*R2*C2) | — | p.578-579 |
| F31 | Type 2 lag | 270 - atan(K) + atan(1/K) | deg | p.580 |
| F32 | LC + ESR lag | 180 - atan(Fco/Fesr) | deg | p.581 |
| F33 | Type 3 EA | G = -(1+s*R2*C1)(1+s*(R1+R3)*C3)/(s*R1*(C1+C2)*(1+s*R3*C3)*(1+s*R2*C1*C2/(C1+C2))) | — | p.588-589 |
| F34 | Type 3 lag | 270 - 2*atan(K) + 2*atan(1/K) | deg | p.587 |
| F35 | DCM flyback plant | Vo/Vea = (Vdc/3)*sqrt(0.4*Ro*T/Lp) ; Fp = 1/(2*pi*Ro*Co) | 80% eff., 3 V ramp | p.596-597 |
| F36 | Transconductance EA | G = gm*Zo ; R >= 3 V/100 uA = 30 k | gm = 2 mA/V (1524/25) | p.602-604 |
| F37 | Resonant forward | Fr = 1/(2*pi*sqrt(Lr*Cr*(Ns/Np)^2)) | Hz | p.609 |
| F38 | SRC / PRC gain | SRC: 1/(1 + j*(Xl - Xc)/Rac), Rac = 8*RL/pi^2 ; PRC: 1/(1 - Xl/Xc + j*Xl/Rac), Rac = pi^2*RL/8 | fundamental approx. | p.619 |
| F39 | LCC gain | NVodc/(0.5*Vin) = (8/pi^2)/(1 + Cp/Cs - w^2*L*Cp + j*Qs*(w/ws - ws/w)) | Cp = Cs best compromise | p.623 |
| F40 | Boost PFC | Vo = Vin/(1 - Ton/T) ; L1 = 1.41*Vrms_min*Ton/dI ; L1 = 3.37*Vrms_min^2*T*E/Po (90-250 V, 20% ripple) | — | p.673, p.687-688 |
| F41 | PFC hold-up | Co = Iav*Thu/(Vo - Vmhu) ; Iav = 2*Pc/(Ec*(Vo + Vmhu)) ; I_ripple(Co) = 0.707*Idc | — | p.689-690 |
| F42 | Boundary-mode PFC | Toff = Ton*Vin/(Vo - Vin) ; Ipkt = 2.82*Po/(E*Vrms) ; L = Vrms^2*Ton*E/(2*Po) | — | p.694-695 |
| F43 | Ballast | Iop = (Vns - Vop)/Xb ; Xb = 1/(2*pi*f*Cb) ; Icav = 2*P_lamp/(E*Vdc) ; Lt = 1/(4*pi^2*Fr^2*Ct) | — | p.711-733 |
| F44 | Boost CCM boundary / ripple | L = Vin_min*(Vo - Vin_min)*T/(2*Vo*Idc_min) ; Vpp = Io*ESR*(1 + Vo/Vin) ; ESR ~ 200e-6/(C*V^0.6) (VPR) | — | p.765-766 |
| F45 | IC regulator heat sink | theta_sa = (Tc_max - Ta)/P_tot ; P_sw = Isw*Vcesat*D | — | p.757-758 |
| F46 | Constant off-time buck | f = (1 - Vo/Vin)/toff | — | p.779 |
### T-2.1 Magnet wire table, AWG 10-41, heavy insulation (Table 7.9, p.346-347)
Current column = rating at a typical design current density of 450 A/cm^2 (choke and transformer windings). +3 AWG halves copper area.

| AWG | Cu dia (cm) | Cu area (cm^2) | dia over insulation (cm) | area over insulation (cm^2) | Ohm/cm @20 C | Ohm/cm @100 C | A @ 450 A/cm^2 |
|---|---|---|---|---|---|---|---|
| 10 | .259 | .052620 | .273 | .058572 | .000033 | .000044 | 23.679 |
| 11 | .231 | .041729 | .244 | .046738 | .000041 | .000055 | 18.778 |
| 12 | .205 | .033092 | .218 | .037309 | .000052 | .000070 | 14.892 |
| 13 | .183 | .026243 | .195 | .029793 | .000066 | .000088 | 11.809 |
| 14 | .163 | .020811 | .174 | .023800 | .000083 | .000111 | 9.365 |
| 15 | .145 | .016504 | .156 | .019021 | .000104 | .000140 | 7.427 |
| 16 | .129 | .013088 | .139 | .015207 | .000132 | .000176 | 5.890 |
| 17 | .115 | .010379 | .124 | .012164 | .000166 | .000222 | 4.671 |
| 18 | .102 | .008231 | .111 | .009735 | .000209 | .000280 | 3.704 |
| 19 | .091 | .006527 | .100 | .007794 | .000264 | .000353 | 2.937 |
| 20 | .081 | .005176 | .089 | .006244 | .000333 | .000445 | 2.329 |
| 21 | .072 | .004105 | .080 | .005004 | .000420 | .000561 | 1.847 |
| 22 | .064 | .003255 | .071 | .004013 | .000530 | .000708 | 1.465 |
| 23 | .057 | .002582 | .064 | .003221 | .000668 | .000892 | 1.162 |
| 24 | .051 | .002047 | .057 | .002586 | .000842 | .001125 | .921 |
| 25 | .045 | .001624 | .051 | .002078 | .001062 | .001419 | .731 |
| 26 | .040 | .001287 | .046 | .001671 | .001339 | .001789 | .579 |
| 27 | .036 | .001021 | .041 | .001344 | .001689 | .002256 | .459 |
| 28 | .032 | .000810 | .037 | .001083 | .002129 | .002845 | .364 |
| 29 | .029 | .000642 | .033 | .000872 | .002685 | .003587 | .289 |
| 30 | .025 | .000509 | .030 | .000704 | .003386 | .004523 | .229 |
| 31 | .023 | .000404 | .027 | .000568 | .004269 | .005704 | .182 |
| 32 | .020 | .000320 | .024 | .000459 | .005384 | .007192 | .144 |
| 33 | .018 | .000254 | .022 | .000371 | .006789 | .009070 | .114 |
| 34 | .016 | .000201 | .020 | .000300 | .008560 | .011437 | .091 |
| 35 | .014 | .000160 | .018 | .000243 | .010795 | .014422 | .072 |
| 36 | .013 | .000127 | .016 | .000197 | .013612 | .018186 | .057 |
| 37 | .011 | .000100 | .014 | .000160 | .017165 | .022932 | .045 |
| 38 | .010 | .000080 | .013 | .000130 | .021644 | .028917 | .036 |
| 39 | .009 | .000063 | .012 | .000106 | .027293 | .036464 | .028 |
| 40 | .008 | .000050 | .010 | .000086 | .034417 | .045981 | .023 |
| 41 | .007 | .000040 | .009 | .000070 | .043399 | .057982 | .018 |

### T-2.2 Magnetics constants used in Ch. 7 design examples
| quantity | value | condition | source |
|---|---|---|---|
| Copper bulk resistivity | 1.9 uOhm*cm | 70 C | p.351, §7.6.5.5 |
| Round magnet wire packing factor | 0.6 (60%) | copper fraction of usable window | p.349, §7.6.5.5 |
| Flux density units | 1 T = 10,000 G = 10 kG; 1 mT = 10 G | — | p.360, §7.7.2 |
| Magnetizing force | H = 0.4*pi*N*I/le (Oe, le in cm) | CGS | p.361, §7.7.3 |
| EC35 E core AP | 1.3 cm^4 (core), 1.1 cm^4 (with bobbin) | — | p.348, Fig. 7.14 |
| EC35 wound Rth | 20 C/W | 30 C rise, 25 C ambient, free air | p.348, Fig. 7.14 |
| EC35 bobbin | usable window per side 30 mm^2; mean dia 1.6 cm; MLT 5.02 cm | two-section bobbin | p.350, §7.6.5.5 |
| CM choke J | 700-1000 A/cm^2 | single-layer toroid | p.343 |
| Rod choke J | 600-1000 A/cm^2 | rod core | p.356 |
| Transformer/choke design J (table basis) | 450 A/cm^2 | Table 7.9 current column | p.346 |

### T-2.3 Standard ferrite E and EC cores for choke design (Table 7.10, p.385)
Ae = effective centre-pole area; Awb = effective bobbin winding window; AP = area product; MPL = magnetic path length; MLT = mean length per turn; Volume = core volume.

| core type | size | Ae (cm^2) | Awb (cm^2) | AP (cm^4) | MPL (cm) | MLT (cm) | volume (cm^3) |
|---|---|---|---|---|---|---|---|
| E 100 | 100/27 | 7.38 | 9.75 | 72 | 27.4 | 14.8 | 202 |
| E 80 | 80/20 | 3.92 | 10.2 | 40 | 18.4 | 11.9 | 72.3 |
| F 11 | 72/19 | 3.68 | 5.44 | 20 | 13.7 | 11.5 | 50.3 |
| Din 5525 | 55/25 | 4.20 | 3.15 | 13.2 | 12.3 | 8.9 | 52.0 |
| Din 5521 | 55/21 | 3.53 | 3.15 | 11.12 | 12.4 | 8.5 | 44.0 |
| E 60 | 60/16 | 2.48 | 3.51 | 8.7 | 11.0 | 9.0 | 27.2 |
| E 175 | 56/19 | 3.37 | 2.08 | 7.0 | 10.7 | 8.5 | 36.0 |
| Din 4220 | 42/20 | 2.33 | 2.18 | 5.0 | 9.7 | 8.4 | 22.7 |
| Din 4215 | 42/15 | 1.78 | 2.18 | 3.9 | 9.7 | 7.5 | 17.3 |
| E 1625 | 47/15 | 2.34 | 1.64 | 3.83 | 8.9 | 6.5 | 20.8 |
| E core | 42/9 | 1.07 | 2.24 | 2.40 | 9.8 | 5.8 | 10.5 |
| E 121 | 40/12 | 1.49 | 1.33 | 1.98 | 7.7 | 6.1 | 11.5 |
| E 1375 | 34/9 | 0.87 | 1.31 | 1.14 | 6.9 | 5.2 | 5.6 |
| E 2627 | 31/9 | 0.83 | 0.85 | 0.70 | 6.2 | 4.6 | 5.1 |
| Din 307 | 30/7 | 0.60 | 0.99 | 0.59 | 6.7 | 4.0 | 4.0 |
| E 2425 | 25/6 | 0.74 | 0.60 | 0.45 | 7.3 | 3.8 | 3.0 |
| EC 35 | 34/9 | 0.84 | 1.55 | 1.3 | 7.74 | 5 | 6.5 |
| EC 41 | 40/11 | 1.21 | 2.0 | 2.4 | 8.93 | 6 | 10.8 |
| EC 52 | 52/13 | 1.80 | 3.0 | 5.4 | 10.5 | 7.3 | 18.8 |
| EC 70 | 70/16 | 2.79 | 6.38 | 17.8 | 14.4 | 9.5 | 40.1 |

### T-2.4 Core loss density vs material at 700 G peak (1400 G p-p), 50 kHz (§7.10.3, Fig. 7.31, p.391)
| material | relative permeability mu_r | loss (mW/cm^3) |
|---|---|---|
| Ferrite type P | 2500 | 100 |
| MPP 14 mu_r and Kool Mu | 60 | 500 |
| MPP 60 mu_r | 60 | 1100 |
| Iron powder #2 | 10 | 2100 |
| Iron powder #34 | 33 | 5000 |
| Iron powder #60 | 60 | 10,000 |

### T-2.5 Choke material comparison summary (§7.8.4-7.8.5, §7.10.2-7.10.3, Figs. 7.22-7.23)
| material | Bsat (T) | loss at 100 mT pk / 200 mT p-p, 50 kHz (mW/cm^3) | relative cost | forms |
|---|---|---|---|---|
| Ferrite (gapped, mu ~60 in chart) | ~0.35 | ~30 | high (after MPP) | many shapes; toroids not gappable |
| MPP (79% Ni) | 0.65-0.8 | ~100 (3x ferrite) | highest | toroids only (at time of writing) |
| Kool Mu | ~1.0 | ~200 (6x ferrite) | low-variable | toroid, E, C, block |
| Iron powder | > 1.2 | > 2000 (65x ferrite) | lowest | toroid, E, C, block; ages > 90 C |
| High Flux | 1.5 | (not given) | — | — |

### T-2.6 Kool Mu toroidal cores for chokes (Table 7.11, p.398)
MLT at 40% fill. Al in mH per 1000 turns (= nH/turn^2).

| core | size | Ae (cm^2) | Aw (cm^2) | AP (cm^4) | MPL (cm) | MLT (cm) | volume (cm^3) | Al #26 | Al #60 |
|---|---|---|---|---|---|---|---|---|---|
| 77908 | 79/17 | 2.27 | 18 | 40.8 | 20 | 7.5 | 45.3 | 37 | — |
| 77868 | 79/14 | 1.77 | 18 | 31.8 | 20 | 6.9 | 34.7 | 30 | — |
| 77110 | 58/15 | 1.44 | 9.5 | 13.7 | 14.3 | 6.2 | 20.7 | 33 | 75 |
| 77716 | 52/14 | 1.25 | 7.5 | 9.38 | 12.7 | 5.8 | 15.9 | 32 | 73 |
| 77090 | 47/16 | 1.34 | 6.1 | 8.19 | 11.6 | 5.9 | 15.6 | 37 | 86 |
| 77076 | 37/11 | 0.68 | 3.6 | 2.47 | 9.0 | 4.3 | 6.1 | 24 | 56 |
| 77071 | 34/11 | 0.67 | 2.9 | 1.97 | 8.1 | 4.3 | 5.5 | 28 | 61 |
| 77894 | 28/12 | 0.65 | 1.6 | 1.02 | 6.35 | 4.1 | 4.1 | 32 | 75 |
| 77351 | 24/10 | 0.39 | 1.5 | 0.58 | 5.88 | 3.34 | 2.3 | 22 | 51 |
| 77206 | 21/7 | 0.23 | 1.1 | 0.26 | 5.09 | 2.64 | 1.2 | 14 | 32 |
| 77120 | 17/7 | 0.19 | 0.7 | 0.14 | 4.11 | 2.44 | 0.79 | 15 | 35 |

Worked-example surface area: 77868 wound at 40% fill = 203 cm^2 (p.400).

### T-2.7 Iron powder E cores for chokes (Table 7.12, p.408, courtesy Micrometals)
MLT at 40% fill; Al in nH/N^2. (Row parse from a run-together OCR line; E162 Al#2 value "105" looks inconsistent with the ~3.5:1 #40/#2 ratio of other rows — verify against maker data.)

| core | size | Ae (cm^2) | Aw (cm^2) | AP (cm^4) | MPL (cm) | MLT (cm) | volume (cm^3) | Al #40 | Al #2 |
|---|---|---|---|---|---|---|---|---|---|
| E 450 | 114/35 | 12.2 | 12.7 | 155 | 22.9 | 22.8 | 280 | 480 | 132 |
| E 305 | 77/31 | 7.5 | 8.1 | 60 | 18.5 | 16.3 | 139 | 339 | — |
| E 305 | 77/23 | 5.6 | 8.1 | 45 | 18.5 | 15.5 | 104 | 255 | 75 |
| E 220 | 56/21 | 3.6 | 4.1 | 14 (text: 14.2) | 13.2 | 11.5 | 47.7 | 240 | 69 |
| E 225 | 57/19 | 3.58 | 2.87 | 10 | 11.5 | 11.4 | 40.8 | 290 | 76 |
| E 168 | 43/20 | 2.41 | 2.87 | 6.9 | 10.4 | 8.85 | 24.6 | 196 | 55 |
| E 187 | 47/16 | 2.48 | 1.93 | 4.8 | 9.5 | 9.50 | 23.3 | 240 | — |
| E 162 | 41/13 | 1.61 | 1.7 | 2.7 | 8.4 | 8.26 | 13.6 | 175 | 105 (?) |
| E 137 | 35/10 | 0.91 | 1.55 | 1.4 | 7.4 | 6.99 | 6.72 | 113 | 32 |
| E 118 | 30/7 | 0.49 | 1.27 | 0.63 | 7.14 | 5.38 | 4.60 | 80 | — |
| E 100 | 25/6 | 0.43 | 0.806 | 0.32 | 5.08 | 5.08 | 2.05 | 81 | 21 |

Mix correction used in text: Al(#40) = 0.87 x Al(#26); E220 Al(#26) = 275 nH/N^2 (p.407).

### T-2.8 Winding fill (packing) factors used in Ch. 7
| winding | factor | source |
|---|---|---|
| Round magnet wire on bobbin (E core) | 0.6 | p.349, p.375, p.382 |
| Round wire on toroid (shuttle clearance, ~30% of ID left free) | 0.4 | p.399-400 |

### T-2.9 Kool Mu powder E cores for chokes (Table 7.13, p.414; caption says "Iron Powder E Cores ... Micrometals" but text and part numbers identify Kool Mu E cores)
MLT at 40% fill. Al in mH per 1000 turns (= nH/N^2). Text confirms single Al values of 5530E (261) and 5528E (219) are #60 material. Header labels the second Al column "#40" but its values exceed the first column (higher-mu grade?) — verify against maker data. Text uses MPL 12.5 cm and MLT 10.73 cm for 5528E (table: 12.3 / 11.6).

| core | size | Ae (cm^2) | Awb (cm^2) | AP (cm^4) | MPL (cm) | MLT (cm) | volume (cm^3) | Al col 1 (#60 per text) | Al col 2 |
|---|---|---|---|---|---|---|---|---|---|
| 8020E | 80/20 | 3.89 | 11.2 | 43.3 | 18.5 | 15.8 | 72.1 | 190 | — |
| 6527E | 65/27 | 5.40 | 5.4 | 29.0 | 14.7 | 14.18 | 79.4 | — | — |
| 7228E | 72/19 | 3.68 | 6.0 | 22.2 | 13.7 | 14.38 | 50.3 | — | — |
| 5530E | 55/25 | 4.17 | 3.8 | 15.9 | 12.3 | 12.4 | 51.4 | 261 | — |
| 5528E | 55/20 | 3.50 | 3.8 | 13.3 | 12.3 | 11.6 | 43.1 | 219 | — |
| 4022E | 43/20 | 2.37 | 2.8 | 6.60 | 9.84 | 10.1 | 23.3 | 194 | 281 |
| 4020E | 43/15 | 1.83 | 2.8 | 5.10 | 9.84 | 9.2 | 18.0 | 150 | 217 |
| 4017E | 43/11 | 1.28 | 2.8 | 3.56 | 9.84 | 8.26 | 12.6 | 105 | 151 |
| 4317E | 41/12 | 1.52 | 1.64 | 2.49 | 7.75 | 8.16 | 11.8 | 163 | 234 |
| 3515E | 35/9 | 0.84 | 1.52 | 1.28 | 6.94 | 6.86 | 5.83 | 102 | 146 |
| 3007E | 30/7 | 0.60 | 1.25 | 0.75 | 6.56 | 5.36 | 3.94 | 71 | 92 |
| 2510E | 25/6 | 0.38 | 0.78 | 0.30 | 4.85 | 5.00 | 1.87 | 70 | 100 |
| 1808E | 19/5 | 0.23 | 0.52 | 0.117 | 4.10 | 3.78 | 0.914 | 48 | 69 |
| 1207E | 13/4 | 0.13 | 0.23 | 0.030 | 2.96 | 2.48 | 0.385 | — | — |

### T-2.10 Iron powder mix Al correction factors vs #26 reference (Micrometals, §7.12, p.407, p.412)
| mix | factor on #26 Al | E220 Al (nH/N^2) |
|---|---|---|
| #26 (reference) | 1.00 | 275 |
| #40 | 0.87 | 240 |
| #8 | 0.51 | 140 |

### T-2.11 Powder-core permeability retention vs DC magnetizing force (anchors quoted in text)
| material / grade | H (Oe) | mu / mu_initial | source |
|---|---|---|---|
| Kool Mu toroid 90 mu | 100 | 0.25 | p.372, Fig. 7.25 |
| Kool Mu toroid 26 mu | 100 | > 0.80 | p.372, Fig. 7.25 |
| Kool Mu toroid #26 (77868) | 126 | 0.85 | p.399 |
| Kool Mu E core 90 mu | 100 | 0.32 | p.418, Fig. 7.40 |
| Kool Mu E core 26 mu | 100 | > 0.87 | p.418, Fig. 7.40 |
| Kool Mu E core #60 (5528E) | 55 | 0.70 | p.415 |
| Kool Mu E core #60 (5530E) | 100 | 0.52 | p.419 |
| Kool Mu E core #60 (5530E) | 200 | 0.25 | p.420 |
| Kool Mu E core #60 (5530E) | ~2 A bias (low H) | 1.00 | p.420 |

### T-2.12 Worked choke designs, Ch. 7 (summary of numbers)
| design | spec | core | N | wire | P_cu (W) | P_core (W) | dT (C) | source |
|---|---|---|---|---|---|---|---|---|
| Gapped ferrite buck choke | 25 V->5 V, 10 A, 25 kHz, 2 A p-p, 30 C | EC41, g = 2 mm total | 37 | 14-16 AWG (nomogram) / 15 AWG (calc) | 1.9-2.6 | < 0.022 | ~40 | §7.9 |
| Kool Mu toroid buck choke | 10 A, 1.2 mH, 40 C | 77868 #26 | 200 initial (book: 70) | 17 AWG (book) | 8 | negligible (< 10 mW/cm^3) | 30-31 | §7.11 |
| #40 iron powder boost choke | 100->200 V, 10 A, 50 kHz, 1.5 A p-p | E220 #40 | 53 | 11 AWG | 2.5 | 13.4 (book) | not acceptable | §7.12.2 |
| #8 iron powder boost choke | same | E220 #8 | 69 | — | 4.4 | 4.53 | ~40 (E core) | §7.12.3 |
| Kool Mu #60 boost choke | same | 5528E #60 | 66 | 12 AWG | 3.7 | 1.3 | ~30 (E core) | §7.12.4 |
| Swinging choke (Kool Mu #60) | 10 A, 1 mH, 40 C | 5530E #60 | 98 | 13 AWG | 8.5 | negligible | 39 | §7.13 |
| CM line filter choke | 5 A rms 60 Hz, 30 C | EC35 (AP 1.1 with bobbin) | 2 x 24-28 | 17-18 AWG | 1.5 | ~0 | 30 | §7.6.5 |

### T-2.13 Ultra-fast diode forward voltages for Baker clamp (Table 8.1, p.434)
| If (A) | MUR450 Vf 25 C (V) | MUR450 Vf 100 C (V) | MUR405 Vf 25 C (V) | MUR405 Vf 100 C (V) |
|---|---|---|---|---|
| 0.5 | 0.89 | 0.75 | 0.71 | 0.61 |
| 1.0 | 0.93 | 0.80 | 0.74 | 0.65 |
| 2.0 | 1.01 | 0.90 | 0.78 | 0.70 |
| 3.0 | 1.10 | 0.95 | 0.80 | 0.73 |
MUR450: 450 V, 3 A, 75 ns; MUR405: 50 V, 4 A, 35 ns (p.433).

### T-2.14 Bipolar base drive constants (Ch. 8)
| quantity | value | source |
|---|---|---|
| Beta production spread | 4:1 (min = typ/2, max = 2*typ) | p.424 |
| Vce(sat) at max current, lowest beta | 0.5-3.0 V (target 0.5-1.0 V at Ic ramp peak) | p.424-425 |
| Turn-on spike | 2-3 x average Ib, 2-3% of ton_min | p.425 |
| Overdrive rise time | k = 2: 0.69 tau_a; k = 3: 0.4 tau_a; k = 1: 3 tau_a to 95% | p.425-426 |
| Reverse base bias for Vcev | -1 to -5 V, for at least the leakage spike duration | p.429 |
| Vcer base-emitter resistor | 50-100 Ohm | p.429 |
| Baker clamp B-C forward bias | 0.2-0.4 V; storage time reduced 5-10x | p.431 |
| Baker-clamped Vce(on) | ~1 V | p.434 |
| 2N6836 | 15 A, 450 V Vceo, 850 V Vcev; beta_min 5 at 15 A, 8 at 10 A | p.430, p.439 |
| Unclamped storage time, 2N6836 (10 A, Bf = 5, 100 C) | 3 us | p.431 |
| IC Darlington storage | 3-4 us | p.442 |
| High-current bipolar turn-off time toff | 0.30 us | p.448 |
| Proportional drive Nb/Nc | = beta_min (5-10 for Ic > 5-8 A) | p.446 |
| Turn-off pulse at base (proportional drive) | -2 V | p.446 |
| UC3525 output driver drop | ~2 V at 200 mA | p.453 |
| Ferroxcube 1408PA3C8 pot core | Al = 315 mH/1000 T (also -100 grade: Al 100); dia 0.551 in, h 0.328 in; knee ~12 At | p.440, p.450 |
| Forward converter peak primary current | Ipft = 3.13*Po/Vdc_min (Eq. 2.28, used in Ch. 8) | p.439, p.449 |

### T-2.15 MOSFET/IGBT examples and constants (Ch. 9)
| item | value | source |
|---|---|---|
| MTM7N45 | 7 A, 450 V, rds 0.8 Ohm, Ciss 1800 pF, Crss 150 pF, Vth ~2.5 V | p.461-466 |
| MTM15N40 | 15 A, 400 V, rds 0.4 Ohm | p.464 |
| MTH15N20 | 15 A, 200 V, Ciss 2000 pF, Crss 200 pF | p.466 |
| MTH7N45 (Table 9.1) | Id 7 A, Vdss 450 V, rds 0.8 Ohm at 25 C | p.479 |
| MTH13N45 (Table 9.1) | Id 13 A, Vdss 450 V, rds 0.4 Ohm at 25 C | p.479 |
| Telecom 48 V bus | 38 V min, 60 V max | p.466 |
| 115 VAC +/-10% max rectified | 1.1 x 115 x 1.414 = 178 V | p.465 |
| Vgs(on) standard | 10 V | p.463 |
| Gate threshold / full-current gate voltage | ~2.5 V / ~5-7 V (MTM7N45) | p.461, p.468 |
| Max Vgs | +/-20 V (typ.); clamp zener 18 V | p.484-485 |
| Maker minimum gate resistor | 5-50 Ohm | p.467, p.485 |
| Paralleled FET gate resistor | 10-20 Ohm or ferrite bead | p.482 |
| Idm vs Id | Idm = 2-3 x Id | p.473 |
| rds(100 C)/rds(25 C), 400 V MOSFET | 1.6 | p.479 |
| Vgsth tempco | -5% per 25 C (MOSFET); IGBT VGE(th) -12 mV/C | p.475, p.499 |
| MOSFET Tj max / design | 150 C / 105-125 C | p.478 |
| Reliability vs temperature | -50% per +10 C (MOSFET, p.479); life x2 per -10 C (IGBT, p.498) | p.479, p.498 |
| Rth_jc typical (TO-3-class 7-13 A 450 V) | 0.83 C/W | p.480 |
| SG1524 output | 200 mA source OR sink | p.469 |
| 2N2222A / 2N2907A totem pole | 800 mA, ~60 ns rise, 300 MHz | p.469, p.455 |
| UC1525A output stage drop | ~2 V each side at 200 mA | p.472 |
| IGBT VCE max operating | <= 0.8 x VCES | p.488 |
| IGBT BVCES tempco | +10% from 25 C to 150 C | p.498 |
| IGBT switching-time budget (APT) | total switching time <= 5% of period | p.507 |
| Push-pull MOSFET practical power without flux-balance fix | up to 150 W | p.483 |

### T-2.16 Mag-amp square-loop core materials (Ch. 10)
| material | composition / type | Bs | use / frequency | density | notes | source |
|---|---|---|---|---|---|---|
| Square Permalloy 80 (4-79 Moly-permalloy, Square Mu 79, Hy Ra 80) | 79% Ni, 17% Fe, 4% Mo, tape wound | — | 1-mil tape <= 50 kHz; 1/2-mil 50-100 kHz | 8.75 g/cm^3 | Curie 460 C; tapes 0.5/1/2/4/6/14 mil | p.522-524 |
| Metglas 2714A (Allied Signal; Magnetics Inc. cores) | amorphous | — | > 100 kHz | — | ~ Toshiba MB losses, Hc, squareness | p.525-526 |
| Toshiba MB | amorphous | 6000 G | > 100 kHz | 8.0 g/cm^3 | Hc = 0.18 Oe at 100 kHz | p.529, p.539 |
| Toshiba MA | amorphous | 6500 G | between 1/2-mil Permalloy and MB | 8.0 g/cm^3 | W/lb = 56.8 x W/cm^3 | p.525-529 |
| Vitrovac 6025 (Vacuumschmelze) | amorphous | — | HF | — | permeability up to 2 x 10^6 | p.525 |

### T-2.17 Toshiba MB mag-amp cores used in text (Figs. 10.9-10.11, p.534-536)
| core | Ae (cm^2) | lp (cm) | note |
|---|---|---|---|
| MB 21 x 14 x 4.5 | 0.118 | 5.5 | full-loop (1400 maxwell / 12000 G) loss 1 W -> 40 C rise (Fig. 10.12) |
| MB 18 x 12 x 4.5 | 0.101 | — | — |
| MB 15 x 10 x 4.5 | 0.0843 | — | — |

### T-2.18 Postregulator selection thresholds (§10.2)
| output current | recommended | notes |
|---|---|---|
| <= 1.5 A | linear IC (TO-220) | headroom 2-3 V (LDO 0.5-1 V at higher cost) |
| > 1.5 A | mag-amp (preferred) or buck | buck: slave >= Vout + 4 V; synchronize to avoid beats |

### T-2.19 Type 2 error-amplifier phase lag vs K (Table 12.1, p.580; Eq. 12.7: lag = 270 - atan(K) + atan(1/K))
| K = Fco/Fz = Fp/Fco | 2 | 3 | 4 | 5 | 6 | 10 |
|---|---|---|---|---|---|---|
| EA lag (deg) | 233 | 216 | 208 | 202 | 198 | 191 |

### T-2.20 LC filter phase lag at Fco with ESR zero (Table 12.2, p.581; Eq. 12.8: lag = 180 - atan(Fco/Fesr))
| Fco/Fesr | 0.25 | 0.50 | 0.75 | 1.0 | 1.2 | 1.4 | 1.6 | 1.8 | 2.0 | 2.5 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| lag (deg) | 166 | 153 | 143 | 135 | 130 | 126 | 122 | 119 | 116 | 112 | 108 | 104 | 101 | 99.5 | 98.1 | 97.1 | 96.3 | 95.7 |

### T-2.21 Type 3 error-amplifier phase lag vs K (Table 12.3, p.588; Eq. 12.9: lag = 270 - 2*atan(K) + 2*atan(1/K))
| K | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| EA lag (deg) | 196 | 164 | 146 | 136 | 128 |

### T-2.22 Loop-design constants (Ch. 12)
| quantity | value | source |
|---|---|---|
| Phase margin target | 45 deg (35-45 deg usual worst-case practice) | p.563, p.567 |
| Crossover | fsw/5 to fsw/4 (< fsw/2 absolute) | p.572 |
| Gain slope at crossover | -1 (-20 dB/dec) | p.567 |
| Al electrolytic Resr*Co | 65e-6 s (Fesr ~ 2.5 kHz) | p.583, p.585 |
| PWM ramp | 0-3 V triangle (SG1524-type), max D = 0.5 per output | p.570 |
| Reference voltage | 2.5 V (5 V output -> divider -6 dB) | p.571 |
| Transconductance EA (1524/1525) | gm = 2 mA/V, unloaded +80 dB, pole 300 Hz, internal 100 pF, output +/-100 uA -> R >= 30 k | p.603-604 |
| Output LC filter design (Eq. 2.47/2.48) | Lo = 3*Vo*T/Io_nom ; Co = 65e-6 * dI / Vor, dI = 2*Io_min | p.582 |

### T-2.23 Cost/loss comparison of choke core materials (Table 16.1, p.724)
| core type | cost (500 qty), $ | core loss at 1000 G, 50 kHz (mW/cm^3) |
|---|---|---|
| MPP | 14.00 | 180 |
| Kool Mu | 4.20 | 300 |
| Gapped ferrite 3C85 (two halves, 3019 pot) | 2.20 | 30 |
| Micrometals #26 iron powder | 0.34 | 2000 |

### T-2.24 Kool Mu toroids for a 4 mH current-feed inductor, I = 2 x 434 mA (Table 16.2, p.726)
| core | Al (mH/1000 T) | N | Ae (cm^2) | Bm (G) | lm (cm) | Hm (Oe) | L falloff (%) | loss (mW/cm^3) | volume (cm^3) | total loss (mW) |
|---|---|---|---|---|---|---|---|---|---|---|
| 77110 | 75 | 231 | 1.44 | 121 | 14.3 | 17.6 | 8 | 4 | 20.6 | 84 |
| 77214 | 94 | 206 | 1.44 | 136 | 14.3 | 15.7 | 11 | 5 | 20.6 | 103 |
| 77094 | 107 | 193 | 1.34 | 159 | 11.6 | 18.5 | 13 | 8 | 15.6 | 125 |
| 77439 | 135 | 172 | 1.99 | 117 | 10.74 | 17.4 | 9 | 4 | 21.3 | 85 |

### T-2.25 Micrometals #26 toroids for the same inductor (Table 16.3, p.726)
| core | Al (mH/1000 T) | N | Ae (cm^2) | Bm (G) | lm (cm) | Hm (Oe) | L falloff (%) | loss (mW/cm^3) | volume (cm^3) | total loss (mW) |
|---|---|---|---|---|---|---|---|---|---|---|
| 225-26B | 160 | 158 | 2.59 | 98 | 14 | 12.3 | 10 | 17 | 38 | 646 |
| 250-26 | 242 | 129 | 3.84 | 81 | 15 | 9.38 | 6 | 15 | 57 | 855 |
| 157-26 | 100 | 200 | 1.06 | 190 | 10 | 21.8 | 20 | 60 | 11 | 660 |
| 175-26 | 105 | 195 | 1.34 | 154 | 11 | 19.3 | 18.0 | 40 | 15 | 600 |

### T-2.26 Gapped ferrite pot cores for the same inductor at 1 A (Table 16.4, p.728)
| core (Philips) | Al (mH/1000 T) | gap (mil) | N | NImax (At) | cliff point (At) | verdict |
|---|---|---|---|---|---|---|
| 2616 | 170 | 32 | 153 | 153 | 129 | fails (NI > cliff) |
| 2616 | 100 | 64 | 200 | 200 | 200 | marginal (at cliff) |
| 3019 | 500 | 11 | 89 | 89 | 60 | fails |
| 3019 | 210 | 35 | 138 | 138 | 170 | OK: Ae 1.38 cm^2, 423 G, ~5 mW/cm^3, 6.19 cm^3 -> 31 mW |
(Row pairing of the Al/gap/cliff columns is reconstructed from a run-together OCR table and the text on p.727-729.)

### T-2.27 Contending current-feed inductor cores (Table 16.5, p.729)
| core | cost (500 qty), $ | total core loss (mW) | OD (in) | height (in) |
|---|---|---|---|---|
| Kool Mu 77439 | 4.20 | 85 | 1.84 | 0.71 |
| Micrometals 250-26 | 0.34 | 850 | 2.5 | 1.00 |
| Ferrite pot 3019 | 2.20 | 31 | 1.18 | 0.74 |

### T-2.28 E21 transformer coil options (Table 16.6, p.735) — bobbin 0.734 in wide x 0.256 in high
| wire # | area (CM) | diameter (in) | turns/width | layers/height |
|---|---|---|---|---|
| 20 | 1020 | 0.0351 | 20 | 7 |
| 21 | 812 | 0.0314 | 23 | 8 |

### T-2.29 Candidate cores for current-fed ballast transformer T1, Lt = 1.5 mH, Ct = 0.03 uF, Bm = 2000 G (Table 16.7, p.736)
| parameter | E625 | 783E608 | ETD44 |
|---|---|---|---|
| Ae (cm^2) | 2.34 | 1.81 | 1.74 |
| Bm (G) | 2000 | 2000 | 2000 |
| Np (turns per half primary) | 43 | 56 | 58 |
| Al (mH/1000 T) | 203 | 120 | 111 |
| gap (mil) | 72 | 110 | 120 |
| bobbin width / height (in) | 0.85 / 0.251 | 1.024 / 0.270 | 1.165 / 0.283 |
| turns/width #20 | 24 | 29 | 33 |
| full primary layers | 4 | 4 | 4 |
| layers/height #20 | 7 | 7 | 8 |
| core loss at 2000 G, 25 kHz (mW/cm^3) | 80 | 80 | 80 |
| core volume (cm^3) | 20.8 | 17.8 | 18.0 |
| total core loss (W) | 1.66 | 1.42 | 1.44 |
| secondary turns (2Np) / turns per layer #24 / layers | 86 / 37 / 3 | 112 / 45 / 3 | 116 / 51 / 3 |
| primary + secondary height (in) / remaining (in) | 0.208 / 0.043 (marginal) | 0.208 / 0.062 | 0.208 / 0.075 (preferred) |

### T-2.30 Ballast inverter off-state transistor voltage stress (Ch. 16)
| topology | peak off-state stress | example |
|---|---|---|
| Current-fed push-pull | pi x Vdc | 205 V -> 644 V (120 VAC) |
| Voltage-fed push-pull | 2 x Vdc | 205 V -> > 410 V |
| Current-fed parallel-resonant half bridge | (pi/2) x Vdc | 400 V -> 628 V (230 VAC; 700 V parts) |
| Voltage-fed series-resonant half bridge | Vdc | 400 V |

### T-2.31 Linear Technology high-power boost regulators (Table 17.1, p.764)
| part | Vin min (V) | Vin max (V) | switch V max (V) | frequency (kHz) | switch current max (A) | switch resistance (Ohm) |
|---|---|---|---|---|---|---|
| LT1170 | 3.0 | 60 | 75 | 100 | 5 | 0.15 |
| LT1172 | 3.0 | 60 | 65 | 100 | 1.25 | 0.60 |
| LT1171HV | 3.0 | 60 | 75 | 100 | 2.5 | 0.30 |
| LT1270 | 3.5 | 30 | 60 | 60 | 8.0 | 0.12 |
| LT1270A | 3.5 | 30 | 60 | 60 | 10.0 | 0.12 |
| LT1268 | 3.5 | 30 | 60 | 150 | 7.5 | 0.12 |
| LT1373 | 2.4 | 30 | 35 | 250 | 1.5 | 0.50 |
| LT1372 | 2.4 | 30 | 35 | 500 | 1.5 | 0.50 |
| LT1371 | 2.4 | 30 | 35 | 500 | 3.0 | 0.25 |
| LT1377 | 2.4 | 30 | 35 | 1000 | 1.5 | 0.50 |

### T-2.32 IC regulator thermal and component constants (Ch. 17)
| item | value | source |
|---|---|---|
| LT1170 reference | 1.24 V (FB-to-ground 1.24 k -> 1 mA divider) | p.753 |
| LT1170 Vc range / clamp | 0.9-2.0 V / 2 V | p.753 |
| LT1170 Vcesat | 0.8 V at 5 A, 100 C | p.757 |
| LT1170 theta_jc (TO-220) | 2 C/W | p.757 |
| LT1170 quiescent model | Iq = 6 mA + 0.0015*Isw + Isw*D/40 | p.757 |
| LT regulator abs max / design Tj | 100 C / ~90 C | p.757 |
| LT1074 switch drop (triple Darlington) | 2.2 V at 5 A; 1.7 V at 1.5 A; LT1076 1.25 V; LT1376 0.5 V at 1.5 A | p.772-775 |
| LT1074 control current | 7 mA + 5 mA*D + 2*Io*Ts*F, Ts = 0.06 us | p.774 |
| LTC1148 sense threshold | -0.025 to -0.15 V (design 0.100 V) | p.780-781 |
| Boost CCM boundary | Idc_min = 10% of max-power input current | p.765 |
| Empirical ESR (Mallory VPR / Sprague 673D-674D) | 200e-6/(C*V^0.6) / 400e-6/(C*V^0.6) Ohm | p.766 |
| Loop-tuning start values (LTC AN19) | R = 1 k, C = 2 uF, step load ~10% at ~50 Hz | p.783 |

### T-2.33 Magnetic unit conversions (Appendix Table A.1, p.795)
| quantity | CGS/EMU unit | MKS unit | CGS -> MKS multiply by | MKS -> CGS multiply by |
|---|---|---|---|---|
| Flux | maxwell | weber | 1e-8 | 1e8 |
| Flux density | gauss | tesla | 1e-4 | 1e4 |
| Flux density | gauss | millitesla | 1e-1 | 1e1 |
| Flux density | gauss | weber/m^2 | 1e-4 | 1e4 |
| Magnetic field intensity | oersted | ampere-turns/m | 79.5 | 1.26e-2 |
Also: 1 Oe = 1000/(4*pi) A/m (Appendix quantity table, p.794); flux (maxwell) = flux density (G) x core area (cm^2) (p.793).

### T-2.34 Other conversion factors (Appendix Table A.2, p.795)
| from A | to B | A -> B multiply by | B -> A multiply by |
|---|---|---|---|
| circular mils | square inches | 7.85e-7 | 1.27e6 |
| circular mils | square centimeters | 5.07e-6 | 1.98e5 |

### T-2.35 Symbols used by the author (Appendix, p.793)
| symbol | meaning (author's usual unit) |
|---|---|
| Ab | winding area of a core bobbin (in^2) |
| Ae | effective core area (cm^2) |
| AL (Al) | inductance of core (mH per 1000 turns) |
| Br | remanence flux density (flux density at 0 Oe) |
| Bs | saturation flux density |
| DCMA | current density in wire (circular mils per rms ampere) |
| lm | effective magnetic path length (cm) |
| phi | flux (maxwells = gauss x cm^2) |

## 3. Mechanizable checks

Conventions: angles in degrees, frequencies in Hz, SI units unless stated. "margin" is (limit - value)/limit unless stated; negative margin = fail. Tolerance bands marked (author-quantified: low) are this extraction's quantification of qualitative text.

#### A. Loop / compensation table checks (input: one row per operating corner)

`CHECK-crossover-vs-fsw`: inputs fsw (Hz), fco (Hz) -> r = fco/fsw -> pass if r <= 0.25 (author practice fsw/4 to fsw/5); hard fail if r >= 0.5 (sampling limit) -> margin = (0.25*fsw - fco)/(0.25*fsw) -> PRESSMAN-2170.

`CHECK-phase-margin`: inputs phase_total_at_fco (deg, total open-loop lag including the 180 deg inversion) OR (theta_EA, theta_plant) -> PM = 360 - phase_total (= 360 - theta_EA - theta_plant) -> pass PM >= 45; warn 35 <= PM < 45; fail PM < 35 -> margin = PM - 45 (deg) -> PRESSMAN-2168, 2180, 2187.

`CHECK-gain-slope-at-crossover`: inputs |T| (dB) at fco/2 and 2*fco -> slope = (G(2fco) - G(fco/2))/log10(4) (dB/dec) -> pass if -30 <= slope <= -10 (i.e. -1 slope +/-0.5; author-quantified: low) ; fail if slope <= -30 (approaching -2) -> margin = min(slope + 30, -10 - slope) -> PRESSMAN-2169.

`CHECK-esr-zero-location`: inputs Resr (Ohm; if blank and cap_type = Al electrolytic use Resr = 65e-6/Co), Co (F), fco -> Fesr = 1/(2*pi*Resr*Co); theta_LC = 180 - atan(fco/Fesr) -> required EA = "Type 2" if Fesr < fco, else "Type 3" -> pass if chosen EA type matches required -> margin = log10(fco/Fesr) (decades; positive favours Type 2) -> PRESSMAN-2172, 2177, 2179, 2181.

`CHECK-type2-pm-from-K`: inputs K, fco, Fesr -> theta_EA = 270 - atan(K) + atan(1/K); theta_LC = 180 - atan(fco/Fesr); PM = 360 - theta_EA - theta_LC -> pass PM >= 45 -> margin = PM - 45 -> PRESSMAN-2178, 2179, 2180 (Table 12.1/12.2).

`CHECK-type3-pm-from-K`: inputs K, (Fesr optional; default none -> theta_LC = 180) -> theta_EA = 270 - 2*atan(K) + 2*atan(1/K); PM = 360 - theta_EA - theta_LC -> pass PM >= 45 (needs K >= ~5 with zero ESR) -> margin = PM - 45 -> PRESSMAN-2182, 2183.

`CHECK-type2-network-consistency`: inputs R1, R2, C1, C2, fco, K_target, Gt_at_fco (dB, plant+modulator+divider) -> Fz = 1/(2*pi*R2*C1); Fp = 1/(2*pi*R2*C2); G_mid = 20*log10(R2/R1) -> pass if |fco/Fz - K|/K <= 0.1 and |Fp/fco - K|/K <= 0.1 (author-quantified: low) and |G_mid + Gt_at_fco| <= 1 dB -> margin = worst normalized deviation -> PRESSMAN-2175, 2177, 2180.

`CHECK-type3-network-consistency`: inputs R1, R2, R3, C1, C2, C3, fco, K_target -> Fz1 = 1/(2*pi*R2*C1); Fz2 = 1/(2*pi*(R1+R3)*C3); Fp1 = 1/(2*pi*R2*C1*C2/(C1+C2)); Fp2 = 1/(2*pi*R3*C3) -> pass if Fz1/Fz2 and Fp1/Fp2 within 0.9-1.1 and fco/Fz ~ Fp/fco ~ K within 10% (author-quantified: low) -> PRESSMAN-2181, 2183.

`CHECK-pwm-modulator-gain`: inputs Vsp (V), V_ramp_pp (V, default 3), Dmax_per_output (default 0.5), Vref, Vo -> Gm = Dmax*(Vsp - 1)/V_ramp (Eq. 12.1 generalized; medium); Gs = 20*log10(Vref/Vo) -> reported (dB) for Gt construction -> PRESSMAN-2173, 2174.

`CHECK-lc-light-load-damping`: inputs Lo, Co, Ro_max (light-load resistance), phase-boost zero present (bool) -> Fo = 1/(2*pi*sqrt(Lo*Co)); k2 = Ro_max/sqrt(Lo/Co) -> warn if k2 > 1 (underdamped: resonant bump / conditional-stability risk) and no phase-boost zero near Fo (cap across upper divider resistor) -> margin = 1 - k2 -> PRESSMAN-2171, 2184.

`CHECK-dcm-flyback-corners`: inputs Vdc_min, Vdc_max, Ro_min, Ro_max, T, Lp, Co, Rc, V_ramp (default 3 V), efficiency (default 0.8), EA transfer (Fz, Fp, G_mid) -> for each of 4 corners: Gdc = (Vdc/V_ramp)*sqrt(2*eta*Ro*T/Lp) (author form with eta = 0.8: sqrt(0.4*Ro*T/Lp); generalization medium); Fp = 1/(2*pi*Ro*Co); Fesr = 1/(2*pi*Rc*Co); compute fco and slope of total gain -> pass if every corner crosses at -1 slope with PM >= 45 -> report worst corner (expected: Ro_max) -> PRESSMAN-2185, 2186, 2187.

`CHECK-rhpz-flag`: inputs topology in {boost, flyback, buck-boost, forward, buck}, conduction_mode in {CCM, DCM}, fco, f_RHPZ (user-supplied; this book gives no formula) -> if CCM and boost-derived (boost, flyback, buck-boost): require f_RHPZ given and fco well below it (book: "roll off at a frequency well below the RHP-zero"; no numeric ratio given) else flag "RHP zero not assessed" ; DCM -> pass (no RHP zero) -> PRESSMAN-2185 note; part-1 §1.4 / Ch. 4 of the book (qualitative). conf low.

`CHECK-transconductance-ea-resistor`: inputs R_comp (Ohm), I_EA_max (A, default 100e-6), V_ramp (V, default 3) -> R_min = V_ramp/I_EA_max -> pass R_comp >= R_min (30 kOhm) -> margin = R_comp/R_min - 1 -> PRESSMAN-2190.

`CHECK-resonant-peak-crossing`: inputs f_sw_min_operating (at Vdc_min, Q_min), f_peak_nominal, LC tolerance (fractional, e.g. L_tol, C_tol), mode = ARM -> f_peak_max = f_peak_nominal/sqrt((1 - L_tol)*(1 - C_tol)) -> pass if f_sw_min_operating > f_peak_max -> margin = f_sw_min/f_peak_max - 1 -> PRESSMAN-2197 (tolerance formula: medium).

#### B. Magnetics table checks (input: one row per wound component)

`CHECK-choke-peak-flux`: inputs L (H), Idc (A), dI_pp (A), I_overcurrent (A, optional), N, Ae (m^2), material -> I_pk = max(Idc + dI_pp/2, I_overcurrent); B_pk = L*I_pk/(N*Ae) (gapped core, linear) -> limit = 0.25 T for gapped-ferrite choke design (Fig. 7.26 basis) else material Bsat (ferrite 0.35, MPP 0.65, Kool Mu 1.0, iron powder 1.2, High Flux 1.5 T) -> pass B_pk <= limit -> margin = (limit - B_pk)/limit -> PRESSMAN-2026, 2030, 2040, 2041.

`CHECK-powder-core-bias-rolloff`: inputs N, Idc, MPL (cm), Al0, k(H) table (mu fraction vs Oe), L_required -> H = 0.4*pi*N*Idc/MPL; L_bias = N^2*Al0*k(H) -> pass L_bias >= L_required -> margin = L_bias/L_required - 1 -> PRESSMAN-2034, 2052, 2065 (Table T-2.11 anchors).

`CHECK-ac-flux-and-core-loss`: inputs V_L (V), t (us), N, Ae (mm^2), f, Ve (cm^3), single_ended (bool), Pv(B,f) curve -> dB = V_L*t/(N*Ae); B_chart = dB/2 if single_ended else dB/2 (peak of symmetric swing); P_core = Pv(B_chart, f)*Ve -> reported; feeds temperature check -> PRESSMAN-2025, 2032, 2048.

`CHECK-gap-length`: inputs N, Ae (m^2), L (H), gap_total_design (m) -> g_req = 4*pi*1e-7*N^2*Ae/L -> pass if |gap_design - g_req|/g_req <= 0.2 (fringing adjustment expected; author-quantified: low) -> also report butt gap per leg = g_req/2 -> PRESSMAN-2042.

`CHECK-winding-fill`: inputs N_i, A_wire_insulated_i (per winding, cm^2), Aw (cm^2), core_type -> Ku_limit = 0.6 (bobbin E core) or 0.4 (toroid) -> fill = sum(N_i*A_wire_i)/Aw -> pass fill <= Ku_limit -> margin = (Ku_limit - fill)/Ku_limit -> PRESSMAN-2012, 2053, 2063.

`CHECK-current-density`: inputs I_rms (A), A_cu (cm^2) or CM, application -> J = I_rms/A_cu (A/cm^2) or CM/A = CM/I_rms -> limits: transformer/choke table 450 A/cm^2; CM choke single-layer 700-1000 A/cm^2; rod choke 600-1000 A/cm^2; classic 500 CM/A (>= 500 CM per A) -> pass J <= limit (or CM/A >= 500) -> margin = limit/J - 1 -> PRESSMAN-2006, 2020, 2148, T-2.1.

`CHECK-copper-loss-hot`: inputs N, MLT (cm), Ohm_per_cm_20C, I_rms (A), T_hot (C) -> R20 = N*MLT*Ohm_per_cm; R_hot = R20*(1 + 0.0043*(T_hot - 20)); P_cu = I_rms^2*R_hot -> reported -> PRESSMAN-2045, 2046.

`CHECK-wound-part-temp-rise`: inputs P_cu, P_core (W), Rth (C/W, from AP chart or measured) OR A_surface (cm^2) with psi->dT curve, core_type, dT_spec (C) -> dT = (P_cu + P_core)*Rth (x 0.85 if an E core is evaluated with the toroid AP chart) -> pass dT <= dT_spec -> margin = (dT_spec - dT)/dT_spec -> PRESSMAN-2010, 2047, 2054, 2062.

`CHECK-loss-balance`: inputs P_cu, P_core -> ratio = P_core/P_cu -> advisory: optimum near 1; flag "core-loss limited: try lower-mu/lower-loss mix" if ratio > 2, "copper-loss limited: try higher-mu grade" if ratio < 0.5 (thresholds author-quantified: low) -> PRESSMAN-2059, 2066.

`CHECK-iron-powder-temperature`: inputs material, T_core_max (C), maker_aging_rated (bool) -> pass if material != iron powder or T_core_max <= 90 or maker_aging_rated -> margin = 90 - T_core_max -> PRESSMAN-2035.

`CHECK-series-mode-choke-peak`: inputs I_peak_measured (A), I_design (A) -> pass I_design >= 1.3*I_peak_measured -> margin = I_design/(1.3*I_peak_measured) - 1 -> PRESSMAN-2016.

`CHECK-drive-transformer-knee`: inputs I_mag_pk (A), Np, At_knee -> pass I_mag_pk*Np < At_knee -> margin = 1 - I_mag_pk*Np/At_knee -> PRESSMAN-2084, 2085.

`CHECK-forward-max-duty`: inputs ton_max_at_Vdc_min (s), T (s), Nr/Np -> D = ton/T -> limit 0.4 for Nr = Np (0.5 absolute) -> pass D <= 0.4 -> margin = 0.4 - D -> PRESSMAN-2145, 2204.

`CHECK-magamp-turns`: inputs Vsp (V), t_block (s; full on-time for shutdown capability), Ae (cm^2), Bs (G), N -> N_req = Vsp*t_block/(Ae*2*Bs*1e-8) -> pass N >= N_req -> margin = N/N_req - 1 -> PRESSMAN-2139, 2146.

`CHECK-pushpull-min-load`: inputs I_mag_pk (A, primary), Np/Ns_master, Io_min_master (A) -> I_reflected = I_mag_pk*Np/Ns -> pass Io_min_master > I_reflected -> margin = Io_min/I_reflected - 1 -> PRESSMAN-2218.

#### C. Power-stage, device and thermal checks

`CHECK-rcd-snubber`: inputs Ip (A), tf (s, use 2x data sheet), Vdc_max, ton_min, fsw, L_leak (H), C1_chosen, R1_chosen, R_rating (W), V_device_rating (V) -> C1_min = (Ip/2)*tf/(2*Vdc_max); R1 = ton_min/(3*C1); P_R1 = 0.5*C1*(2*Vdc_max)^2*fsw; V_pk = 2*Vdc_max + (Ip/2)*sqrt(L_leak/C1) -> pass C1 >= C1_min, 3*R1*C1 <= ton_min, R_rating >= 2*P_R1, V_pk <= V_device_rating -> margin = min of individual margins -> PRESSMAN-2155-2158, 2162, 2164.

`CHECK-mosfet-gate-drive`: inputs Ciss, Crss (F), Vdc_max, dVg (V, default 10), t_r (s), I_driver_source, I_driver_sink -> Ig = Ciss*dVg/tr + Crss*(Vdc_max + dVg)/tr -> pass min(I_source, I_sink) >= Ig -> margin = I_driver/Ig - 1 -> PRESSMAN-2097, 2098, 2102.

`CHECK-miller-gate-spike`: inputs dVds (V; e.g. 2*Vdc_max), Crss, Ciss, Vgs_max (default 20), zener_present -> V_spike = dVds*Crss/(Crss + Ciss) -> pass V_spike < Vgs_max or zener_present -> margin = Vgs_max - V_spike -> PRESSMAN-2114.

`CHECK-mosfet-rds-2pct`: inputs Ipft (A), rds25 (Ohm), k_T (default 1.6 at 100 C, 400 V class), Vdc_min -> V_on = Ipft*rds25*k_T -> pass V_on <= 0.02*Vdc_min -> margin = 1 - V_on/(0.02*Vdc_min) -> PRESSMAN-2105, 2109.

`CHECK-junction-temperature`: inputs P_loss (W), RthJC, Tc (C) (or Ta + P*(RthCS + RthSA)), device_class -> Tj = Tc + P*RthJC -> limits: MOSFET design 105-125 C (abs 150), IC regulator ~90 C, else TJmax -> pass Tj <= limit -> margin = limit - Tj -> PRESSMAN-2107, 2125, 2261.

`CHECK-heatsink-required`: inputs P_tot, Tc_max (= Tj_limit - P_sw*RthJC), Ta -> theta_SA_req = (Tc_max - Ta)/P_tot -> pass theta_SA_actual <= theta_SA_req -> margin = theta_SA_req/theta_SA_actual - 1 -> PRESSMAN-2261, 2266.

`CHECK-igbt-voltage-derating`: inputs V_CE_pk (incl. spikes), VCES -> pass V_CE_pk <= 0.8*VCES -> margin = 1 - V_CE_pk/(0.8*VCES) -> PRESSMAN-2116.

`CHECK-igbt-switching-time-budget`: inputs td_on, tr, td_off, tf (s), fsw -> t_tot = sum -> pass t_tot <= 0.05/fsw -> margin = 1 - t_tot*fsw/0.05 -> PRESSMAN-2133.

`CHECK-bipolar-base-drive`: inputs Ic_pk (A), beta_typ, Ib_on (A), reverse_bias_V (V), V_ce_pk, Vceo, Vcev -> beta_min = beta_typ/2; pass Ib_on >= Ic_pk/beta_min; V_limit = Vcev if -5 <= reverse_bias_V <= -1 else Vceo; pass V_ce_pk <= V_limit -> margins -> PRESSMAN-2069, 2070, 2074.

`CHECK-ballast-switch-stress`: inputs topology, Vdc, V_rating -> V_off = pi*Vdc (current-fed push-pull), 2*Vdc (voltage-fed push-pull), (pi/2)*Vdc (current-fed half bridge), Vdc (voltage-fed half bridge) -> pass V_off <= V_rating -> margin = 1 - V_off/V_rating -> PRESSMAN-2247.

`CHECK-postregulator-choice`: inputs Io (A), V_in_slave, Vo -> if Io <= 1.5 A: linear OK with P_lin = Io*(V_in_slave - Vo) reported; else recommend mag-amp or buck (V_in_slave >= Vo + 4 V for buck) -> PRESSMAN-2136.

#### D. PFC / input / output capacitor checks

`CHECK-pfc-output-voltage`: inputs Vrms_max, Vo_nom -> pass Vo_nom >= 1.1*1.414*Vrms_max -> margin = Vo_nom/(1.1*1.414*Vrms_max) - 1 -> PRESSMAN-2232.

`CHECK-pfc-boost-inductor`: inputs Vrms_min, Vrms_max, Po, E, fsw, ripple_fraction (default 0.2), Vo, L_actual -> Ip1 = 1.414*Po/(E*Vrms_min); dI = ripple_fraction*Ip1; Ton = T*(1 - 1.414*Vrms_min/Vo); L_req = 1.414*Vrms_min*Ton/dI -> pass L_actual >= L_req -> margin = L_actual/L_req - 1 -> PRESSMAN-2231.

`CHECK-holdup-capacitor`: inputs Pc, Ec, Vo_min, V_mhu, T_hu (default 0.030 s), Co_actual (with -tolerance) -> Iav = 2*Pc/(Ec*(Vo_min + V_mhu)); Co_req = Iav*T_hu/(Vo_min - V_mhu) -> pass Co_actual_min >= Co_req and 60 <= Vo_min - V_mhu <= 80 V (advisory) -> margin = Co_actual_min/Co_req - 1 -> PRESSMAN-2233.

`CHECK-pfc-cap-ripple-current`: inputs Idc (A, boost output DC current), I_ripple_rating_120Hz (A rms) -> I_req = 0.707*Idc -> pass rating >= I_req -> margin = rating/I_req - 1 -> PRESSMAN-2234.

`CHECK-boost-ccm-boundary`: inputs Vin_min, Vo, T, I_in_max, L_actual -> Idc_min = 0.1*I_in_max; L_req = Vin_min*(Vo - Vin_min)*T/(2*Vo*Idc_min) -> pass L_actual >= L_req (else DCM above 10% load: poorer load regulation, more input ripple) -> margin = L_actual/L_req - 1 -> PRESSMAN-2263.

`CHECK-boost-output-ripple`: inputs Io, Vo, Vin_min, ESR (Ohm; or estimate 200e-6/(C*V^0.6) for Mallory VPR), V_ripple_spec -> Vpp = Io*ESR*(1 + Vo/Vin_min) -> pass Vpp <= spec -> margin = 1 - Vpp/spec -> PRESSMAN-2264.

`CHECK-output-lc-forward`: inputs Vo, T, Io_nom, Io_min, V_ripple_spec, Co_actual, Lo_actual -> Lo_req = 3*Vo*T/Io_nom (Eq. 2.47, keeps CCM to Io_nom/10); Co_req = 65e-6*(2*Io_min)/V_ripple_spec (Eq. 2.48, Al electrolytic) -> pass Lo_actual >= Lo_req and Co_actual >= Co_req -> PRESSMAN-2180 (Eqs. from part-1 §2.3.11 as used in Ch. 12).

## 4. Verification procedures & plots

| # | property | plot / test (x-axis; y-axis) | sweep / corners | what good looks like / pass | setup notes | source |
|---|---|---|---|---|---|---|
| V1 | Loop stability (voltage mode) | Bode: log f (10 Hz to fsw/2); open-loop gain (dB) and phase (deg), with asymptotic Gt (LC + modulator + divider), EA curve and total | Vin min/max x load min/max (light load exposes LC resonant bump) | total gain crosses 0 dB at fsw/5-fsw/4 with -20 dB/dec slope; PM >= 45 deg; no 360 deg phase point with gain > 0 dB near the LC corner (conditional stability) | break loop at EA inverting input (point B) and inject; draw asymptotes per Figs. 12.6, 12.13, 12.16; bibliography cites Middlebrook loop-gain measurement (1975) and HP AN59/AN157 | §12.2-12.15, Figs. 12.4-12.17 |
| V2 | DCM flyback stability | Bode as V1, plant curves for Ro_min and Ro_max overlaid (Fig. 12.19 style) | all four (Vdc, Ro) corners | -1 slope at each crossover; PM typically ~80 deg; check min load (max Ro) most carefully | as V1 | §12.16-12.18 |
| V3 | Transient response / empirical compensation | scope: output voltage deviation vs time for a step load | ~10% AC-coupled step at ~50 Hz on top of nominal load; Vin min/max | minimal overshoot, fast monotonic recovery, no reverse-polarity ring; tune series RC on EA output (start 2 uF / 1 k) | filter switching ripple from the display; large coupling capacitor for the step load | §17.3.12, Fig. 17.15 |
| V4 | Choke inductance vs bias / swing | L (H) vs Idc (A) (or mu% vs H Oe) | 0 to 2 x rated current | L at full load >= design; swinging choke ratio as designed (example 2.5 mH at 2 A -> 1.33 mH at 10 A -> 0.65 mH at 20 A) | LCR meter with DC bias or ripple-slope method | §7.8.7, §7.13, Figs. 7.25, 7.40 |
| V5 | Choke saturation margin | current probe: inductor current vs time over a switching period | max load + over-current, Vin max | linear ramps; no current spike/curvature near the ripple peak | DC-coupled current probe | §7.7.5 |
| V6 | Inductor value check | inductor current ramp: compute L = V_L*dt/di | nominal | within tolerance of design (examples: 1.55 A calc vs 1.4 A meas; 2.0 uH vs 1.8 uH) | measure V at rectifier cathode and ramp di | §14.2.5, §14.3.11 |
| V7 | Magnetics temperature rise | thermocouple temperature rise vs time to steady state | max load, max ambient, final enclosure/airflow | dT <= spec (30-40 C typical targets); matches chart prediction within layout effects | charts assume free air, 45% convection / 55% radiation, emissivity 0.95; measure in the working prototype | §7.7.7, §7.9.10, §7.11.3.8 |
| V8 | Core loss sanity | predicted P_core from dB (single-ended: B_chart = dB/2) and maker Pv curve; compare with calorimetric/temperature | Vin extremes (dB max) | ferrite chokes negligible; iron powder must be counted | maker curves assume symmetric (push-pull) excitation | §7.9.11, §7.12.2.5 |
| V9 | Switch turn-off locus (RBSOA / SSOA) | X-Y plot Ic (or Id) vs Vce (Vds) through turn-off | max load, Vin max (largest spike), with and without reverse base bias | locus inside RBSOA (bipolar) or Idm x Vdss rectangle (MOSFET, < 1 us); spike (Ip/2)*sqrt(Ll/C1) above 2Vdc | current probe + HV differential probe, deskewed | §8.2.4, §9.2.6, §11.7, Figs. 8.4, 9.8, 11.5 |
| V10 | Switching loss / snubber optimization | scope math V x I vs time over turn-on and turn-off; energy per edge | Vin min/nom/max; 40/80/100% load | turn-off loss reduced (example 19 W -> 3.2 W); snubber R dissipation acceptable (<= half resistor rating) | real-time V x I multiplying scope; case temperature check | §11.4 TIP, §11.5, §14.2.3 |
| V11 | Drain/collector waveforms vs line | Vds and Id vs time at min/nom/max Vin, 80% and 40% load | 3 line x 2 load | ramp-on-step current; centre-of-ramp current = 3.13*Po/Vdc_min; constant peak current vs Vin; leakage spike small; reset plateau at 2Vdc then Vdc | Figs. 14.2-14.3 | §14.2.1-14.2.2 |
| V12 | Push-pull flux balance | centre-tap (or both drain) current pulses vs time | all line/load corners | alternate pulses equal amplitude | use drain-lead current probe or source resistor for absolute values (centre-tap probe misreads in short dead time) | §14.3.1, §14.3.4 |
| V13 | Multi-output cross regulation | rectifier-cathode voltage (before LC) vs time + slave DC voltages table | master and slave loads min/max; Vin corners | steep edges, no dead-time ledge/bump; slave within spec; no apparent double turn-on | detect magnetizing-current-induced ledge at light master load | §14.3.5, §14.3.8, §14.3.15 |
| V14 | Output ripple and noise | output voltage (mV p-p) vs time | full load, Vin corners | differential ripple within spec; CM noise identified separately | differential probe with good HF CMRR (CM ringing > 50 MHz); probe tip shorted to ground lead at return rail to identify CM noise | §14.3.5 TIP |
| V15 | Rectifier / primary ringing | rectifier cathode and drain voltage during dead time | full and light load | ringing damped by RC snubbers across rectifiers and half primaries | — | §14.3.6, §14.3.17 |
| V16 | Conducted EMI | spectrum of line-conducted noise (dBuV vs f) | final build incl. chassis, heat sinks, mounting hardware | below applicable (FCC) limits with margin; adjust Y caps within leakage limits, else larger CM choke | spectrum analyzer + LISN (LISN implied) | §7.6.4.2 TIP |
| V17 | RFI inductor self-resonance | impedance magnitude and phase vs frequency | 100 kHz-30 MHz | SRF above the highest noise frequency to be rejected (example 4 MHz close-wound vs 6.5 MHz spaced) | impedance analyzer | §7.6.6.2, Fig. 7.17 |
| V18 | PFC line current quality | line current and voltage vs time over a line cycle; PF and harmonics | Vrms min/max, full and light load | current follows haversine in phase; PF > 0.99 claimed by controller vendors; low 3rd harmonic | true wattmeter for input power (PFC unit shows higher real input power than uncorrected unit) | §15.3-15.5 |
| V19 | Hold-up time | bulk voltage vs time after AC removal | AC removed at minimum Vo, full load | DC/DC outputs in spec for >= T_hu (often 30 ms) until V_mhu | trigger at line-cycle worst phase | §15.4.7, Fig. 15.10 |
| V20 | Resonant converter operating point | normalized gain vs normalized frequency with Q family (Figs. 13.6-13.8, 13.10) | Vdc min/max, load min/max, L and C tolerance extremes | operation stays on one side of the resonant peak (ARM) at all corners; required frequency range practical | — | §13.4-13.5 |
| V21 | Mag-amp regulation | slave output vs load; MA voltage showing blocking tb and firing tf | Vdc min/max, slave load range, shutdown command | tf adjusts to hold output; full shutdown achievable; core temperature within wire rating | — | §10.3 |
| V22 | Ballast start-up | lamp/transistor current vs time at turn-on; lamp current crest factor | cold lamp, one-lamp-open, both lamps | start current within device ratings (voltage-fed 5-10x normal); crest factor near 1.41 | — | §16.3.2, §16.7, §16.9 |
| V23 | Efficiency vs load and line | efficiency (%) vs load (20-115%) at each Vin | Vin min/nom/max | reference points: 125 kHz forward 87% (80% load), 90% (40% load); 200 kHz push-pull > 81.9% full load, ~80% at 1/5 load | transformer temperature rise recorded (54 C at 115% load, 65 C at 112 W) | §14.2-14.3 |
| V24 | IC regulator thermal | junction/case temperature vs load; computed P_tot breakdown | Vin_min (max duty), max load, 50 C ambient | Tj <= ~90 C; heat sink theta_SA <= (Tc_max - Ta)/P_tot | — | §17.3.3, §17.3.8.3 |

## 5. Pitfalls, failure modes, review checklist

### 5.1 Magnetics (Ch. 7 §7.6-7.13)
- [ ] Al value normalized to one turn before computing N (maker may quote Al for 100 or 1000 turns). (p.341, §7.6.3 TIP)
- [ ] CM choke on a two-piece E core: inductance budget allows up to 60% permeability loss vs toroid; matched lapped halves kept together and assembled clean. (p.344, §7.6.4.3)
- [ ] Pile-wound / multi-layer CM choke: check self-resonant frequency; high inter-winding C lets HF noise bypass the choke — rely on series-mode L2 for HF. (p.343, p.345 TIP)
- [ ] Series-mode input inductor checked for saturation at the measured peak rectifier-pulse current with 30% margin. (p.353 TIP)
- [ ] Patient-connected medical supply: Y-capacitors limited by leakage-current limits -> larger CM choke planned. (p.344)
- [ ] Choke saturation check includes Bdc at max load + over-current + dB/2. (p.365, p.371)
- [ ] Gapped ferrite choke has explicit gap margin against abrupt saturation at over-current. (p.371, p.393)
- [ ] Core-loss chart use for single-ended chokes: halve (do not use push-pull loss directly). (p.384-386)
- [ ] Iron powder choke core loss computed explicitly and added to copper loss before temperature check (never assumed negligible). (p.387)
- [ ] Iron powder core temperature stays within maker aging limits (deterioration noted above 90 C). (p.394)
- [ ] Copper loss computed at hot resistance (+0.43%/C; +34% at 100 C) and measured after winding. (p.382)
- [ ] Gap placed in centre pole or copper flux band fitted where radiated field matters; high-AC chokes checked for fringing hot spots near gap. (p.379-380)
- [ ] Temperature rise from nomograms (free air) re-measured on the working prototype in its enclosure/layout. (p.367, p.383)
- [ ] High-ripple (boost/PFC) chokes use stranded/multi-strand wire, skin effect evaluated. (p.380, p.411)
- [ ] Book-number sanity: several Ch. 7 worked examples contain unit/arithmetic slips (Ae = 71 mm^2 vs 1.06 cm^2 in §7.9; 200 vs 70 turns in §7.11; 17 AWG area; 13.4 W vs 14.3 W in §7.12.2). Recompute rather than copy. (p.378-411)

### 5.2 Switch drive (Ch. 8-9)
- [ ] Bipolar base drive sized for beta_min = beta_typ/2 at the Ic ramp PEAK (min Vin, max load), not for average current. (p.424-425)
- [ ] Bipolar Vce stress compared with Vceo unless the drive guarantees -1 to -5 V reverse base bias for the whole leakage spike (then Vcev). (p.427-429)
- [ ] Turn-off Ic-Vce locus checked against RBSOA — a single crossing can destroy a bipolar. (p.430)
- [ ] Baker clamp collector diode rated >= 2 x Vdc_max + leakage spike and fast recovery. (p.433)
- [ ] Base-drive transformer magnetizing ampere-turns below core knee. (p.440)
- [ ] Fixed (non-proportional) base drive checked for overdrive / long storage at minimum load. (p.454)
- [ ] MOSFET gate driver actively sinks current (no resistor-only pull-down on a unidirectional PWM output). (p.469)
- [ ] Gate drive current budget includes Miller current Crss*(Vdc+10)/tr — often larger than the Ciss current. (p.466)
- [ ] Gate-source zener (e.g. 18 V) present on high-voltage MOSFETs where Crss/(Crss+Ciss) x dVds can exceed 20 V; zener at driver side of gate resistor. (p.485)
- [ ] Series gate resistor physically at the gate pin; ferrite bead / 10-20 Ohm per paralleled device. (p.461, p.482)
- [ ] Paralleled MOSFETs: symmetrical gate/source layout, common heat sink, transconductance matched at It/n. (p.481-482)
- [ ] rds taken at hot junction temperature (x1.6 at 100 C for 400 V parts) in loss/selection calculations. (p.479)
- [ ] MOSFET Id data-sheet rating not used as the switching-duty current limit. (p.478)
- [ ] Body diode recovery acceptable for the topology (resonant / inductive loads may need series blocking + external fast diode). (p.486)
- [ ] IGBT replacing a MOSFET: gate drive voltage adequate for the plateau voltage at max current. (p.501)
- [ ] IGBT gate ringing measured below VGEM; if not, cut gate-loop area or raise Rg. (p.494)
- [ ] IGBT stays within ICM, ILM/RBSOA; not operated in avalanche intentionally. (p.496-497)
- [ ] IGBT switching loss scaled from data-sheet test voltage to application voltage; includes diode recovery temperature effect. (p.502)
- [ ] Switching-time sum <= 5% of switching period (IGBT frequency ceiling). (p.507)
- [ ] Book-number sanity: §9.2.5 prints 270 us for a 3RC of 2.7 us; §9.2.9 "0.4% duty" means 40%. (p.466, p.480)

### 5.3 Postregulators, snubbers, loops, resonant, waveforms, PFC, ballasts, IC regulators (Ch. 10-17)
- [ ] Slave outputs: every output inductor stays continuous at its minimum load (else up to 50% slave voltage error); cross regulation budget up to +/-8%. (p.511-512, p.787)
- [ ] Mag-amp shutdown design powers its error amp/reset transistor from a rail that stays up when the slave is shut down. (p.522)
- [ ] Mag-amp reset transistor: error amplifier not driven into saturation when the blocking diode stops collector current (circuit refinement needed). (p.521 TIP)
- [ ] Mag-amps on push-pull/half-bridge outputs checked for magnetizing-current conduction during dead time. (p.540)
- [ ] Forward converter designed for 0.4T max on-time (Nr = Np) to leave 0.1T reset guard for line dips. (p.536)
- [ ] RCD snubber: resistor value not "reduced to cut its dissipation" (loss is independent of R); resistor rated 2x dissipation; snubber returned to +rail where possible. (p.552-553)
- [ ] Snubber capacitor large enough that leakage spike keeps the turn-off locus inside RBSOA (not just sized for dV/dt). (p.557-558)
- [ ] Loop: Fco not above fsw/4; -1 slope at crossover; PM >= 45 deg at all line/load corners. (p.563-572)
- [ ] Zero-ESR output capacitors (ceramic/low-ESR) paired with a Type 3 (not Type 2) error amplifier. (p.585-586)
- [ ] Aluminum electrolytic ESR zero assumed at ~2.5 kHz only when no data (Resr*Co ~ 65 us) — verify with actual capacitor. (p.583)
- [ ] Light-load LC resonance checked for conditional stability; phase-boost capacitor across the upper divider resistor considered. (p.593-595)
- [ ] DCM flyback loop verified at minimum load (maximum Ro). (p.602)
- [ ] Chip transconductance EA: compensation resistor >= 30 kOhm (100 uA output limit), else external op-amp. (p.604)
- [ ] CCM boost/flyback: RHP zero considered — crossover well below it (this book gives no formula; see part-1 §1.4, Ch. 4). (grep: part-1 lines 1266-1278)
- [ ] Resonant CCM converter never crosses to the wrong side of the resonant peak over L/C tolerances and transients; no reliance on a fixed minimum-frequency clamp. (p.616, p.622-623)
- [ ] Resonant converter small resonant inductance (few uH) made production-insensitive (discrete L added) and verified over wiring variations. (p.612-614)
- [ ] Variable-frequency supply acceptable to the system (sync to clock / display line rate not required). (p.611-612, p.777)
- [ ] Current probe placement: drain lead or sense resistor, not push-pull centre tap, for absolute current. (p.642-644)
- [ ] Output ripple measured with differential probe / ground ring; CM noise not mistaken for ripple. (p.647-649)
- [ ] Push-pull minimum load exceeds reflected magnetizing current; transformer gap and core-half mating controlled in production. (p.652-659)
- [ ] Output rectifiers and push-pull half primaries have RC snubbers against ringing. (p.650, p.659)
- [ ] Single-ended flyback limited to ~60 W (double-ended above 60-75 W). (p.660-661)
- [ ] Multi-output flyback slave voltage verified across master load range (secondary leakage pedestal). (p.662-665)
- [ ] PFC: efficiency/thermal budget includes the extra PFC stage loss (PFC unit dissipates more than uncorrected). (p.681)
- [ ] PFC output voltage >= 10% above peak of maximum line; voltage loop bandwidth low (gain low beyond 3rd line harmonic). (p.688, p.691)
- [ ] PFC bulk capacitor checked for hold-up (T_hu, V_mhu) AND 120 Hz ripple current = 0.707 x Idc. (p.689-690)
- [ ] Boundary-mode PFC: switching-frequency spread (e.g. 20-99 kHz) considered for EMI filter design. (p.696)
- [ ] MC34261-type multiplier input <= 3 V at high-line peak. (p.693, p.697)
- [ ] Ballast: voltage-fed topologies checked for 5-10x start-up current; current-fed transistor rated for pi x Vdc (push-pull) or (pi/2) x Vdc (half bridge). (p.717, p.720-742)
- [ ] Parallel-resonant ballast transformer wire sized for circulating tank current, not load current. (p.732-733)
- [ ] VDE creepage: bobbin width usage restricted (or triple-insulated wire) accounted for in core size. (p.737, p.790)
- [ ] IC switching regulator heat sink computed from switch + control dissipation at minimum Vin (max duty); do not assume the peak switch-current rating is usable. (p.756-758, p.773-774)
- [ ] Boost output capacitor ripple-current rating verified (it supplies full load current every on-time). (p.766)
- [ ] Book-number sanity: §17.3.8.3 prints "25 C/W" but calculates with 2.5 C/W; §17.3.9.3 prints 0.0025 A for the ~0.25 mA timing current; §16.6.2 prints (2/pi)Vdc where (pi/2)Vdc is meant. (p.721, p.774, p.780)

## 6. Standards referenced

| standard | edition/year | clause/table | what it governs | page |
|---|---|---|---|---|
| FCC conducted-mode RFI limits | — | — | input line filter (CM L1 + Y caps, series-mode L2 + X caps) must meet them for direct-off-line SMPS | p.341, §7.6.4 |
| IEC Publications 133, 133A, 431, 431A, 647 | — | — | ferrite core dimension standards (cited as Ref. 7, via ANSI) | p.421, Ch. 7 refs |
| MMPA PC100 | — | — | Standard specifications for ferrite pot cores | p.421, Ch. 7 refs |
| MMPA UE 1300 | — | — | Standard specifications for ferrite U, E and I cores | p.421, Ch. 7 refs |
| Safety agency insulation / creepage (unnamed) | — | — | insulation between CM choke windings and winding-to-core | p.343, §7.6.4.2 |
| JEDEC standard 24-2 | — | — | method for measuring gate charge (QGE, QGC, QG) of MOS-gated devices | p.501, §9.3.7 |
| Military junction temperature derating (unnamed spec) | — | — | power semiconductor Tj design limit 105 C | p.478, §9.2.9 |
| IEC555-2 | as cited (predecessor of IEC 61000-3-2; the book does not name 61000-3-2) | — | limits harmonic content of input line current; lamp ballasts required to have PFC meeting it | p.715, §16.4 |
| FCC CFR 47 Part 18 | — | Part 18 | EMI/RFI limits for electronic ballasts | p.715, §16.4 |
| ANSI Fluorescent Lamp Specifications | — | per lamp type | sets lamp operating voltage Vop and current Iop (and wattage) for ballast design | p.712, §16.3.3, Fig. 16.11 |
| VDE safety specifications | — | — | creepage/insulation: may prohibit use of full bobbin width (triple-insulated wire may permit), fewer secondaries eases compliance; foil width limits (part-1 note) | p.737, §16.6.7; p.790, §17.5 |
| Military programs (unnamed) | — | — | some prohibit empirical "select at test" components | p.484, §9.2.11 |
| LTC Application Note 19 (Nelson & Williams) | — | — | empirical loop stabilization by step-load response; empirical ESR formulas | p.766, p.783, §17.3.6.2, §17.3.12 |
| Unitrode Application Note U-125 (de Silva) | — | — | UC3854 PFC design basis | p.681, p.697 |
| APT Application Note APT0201 (Dodge & Hess, 2002) | — | — | IGBT selection; total switching time <= 5% of period | p.487, p.507, p.509 |

## 7. Process / lifecycle guidance

The book is a design text, not a product-lifecycle text; only the process guidance it states explicitly is listed.

| stage | activity | deliverable | exit criterion | source |
|---|---|---|---|---|
| Architecture | Choose topology/regulation scheme: PWM vs resonant (resonant only if the +3-6% efficiency justifies complexity, tolerance sensitivity, variable frequency); conventional slaves vs distributed POL regulation (high bus ~20-25 V bucked down) | topology decision record | answers to the six §13.6 questions; frequency-sync requirement settled | p.627-628, §13.6; p.787-791, §17.5 |
| Architecture | Decide PFC need (mandatory for some off-line products, e.g. ballasts per IEC555-2) and downstream converter (half bridge < 600 W, full bridge above) | PFC front-end spec (Vo, hold-up) | Vo >= 1.1 x line peak; hold-up time defined (often 30 ms) | p.681, p.688-689, p.715 |
| Detailed design | Magnetics by chart/nomogram + iteration (AP -> turns -> gap/mu correction -> wire -> losses -> temperature) | magnetics design sheet per part | predicted dT within spec with core + copper loss | §7.6-7.13 |
| Detailed design | Loop compensation from Bode asymptotes (Fco, slope, K factor) | compensation network values + Bode plot | PM >= 45 deg, -1 slope, at all corners | §12 |
| Prototype | Measure conducted EMI on the final-standard build (chassis, heat sinks, hardware) before fixing CM choke / Y caps | EMI scan report | limits met with margin; medical leakage limits respected | p.344 |
| Prototype | Measure temperatures of wound parts and semiconductors in the real layout/enclosure (free-air charts are only predictions) | thermal test report | rises within spec | p.367, p.383, p.387 |
| Prototype | Stability test at all line/load corners (DCM flyback especially at minimum load); step-load transient check | loop/transient test report | no oscillation, PM >= 45 deg, clean step response | p.602, p.783-786 |
| Production | Avoid select-at-test trims (field replacement without test equipment; drift; some military programs forbid); control transformer gap/core mating and resonant L/C tolerances | production test spec | units interchangeable without per-unit tuning | p.484, p.614, p.652-659, p.627 |

## 8. Coverage log

- Lines 1–350 (front matter, TOC, preface) read for orientation; chapter line map built from "C H A P T E R" markers (Ch. 7 starts 6871, Ch. 8 10645, Ch. 9 11305, Ch. 10 11882, Ch. 11 12344, Ch. 12 12565, Ch. 13 13540, Ch. 14 13827, Ch. 15 14105, Ch. 16 14748, Ch. 17 15695, Appendix 16422, Bibliography 16678, Index 16854).
- Lines 8960–8999 read for context only (tail of §7.5.6 Dowell proximity effect — part-1 territory, not mined).
- Lines 9000–16853 read sequentially in full with the Read tool (chunks of 180–450 lines; no truncation reported): Ch. 7 §7.6–7.13 (9000–10644), Ch. 8 (10645–11304), Ch. 9 (11305–11881), Ch. 10 (11882–12343), Ch. 11 (12344–12564), Ch. 12 (12565–13539), Ch. 13 (13540–13826), Ch. 14 (13827–14104), Ch. 15 (14105–14747), Ch. 16 (14748–15694), Ch. 17 (15695–16421), Appendix (16422–16677), Bibliography (16678–16853).
- Lines 16854–17886 (Index) skipped after confirming the file tail is index only.
- Skipped as non-rule content: market/history narrative (fluorescent lamp market, amorphous-metal history, Paschen/arc physics beyond numeric anchors), references lists (standards/app-notes extracted), and the algebra of §12.6 (result kept).
- Output: 270 design rules (PRESSMAN-2001 … 2270), 35 numbered tables (T-2.1 … T-2.35) plus formula index F-2.0 (46 formulas), 47 mechanizable checks, 24 verification procedures, ~70 checklist items, standards list, process table.
- Figures are not in the text. Rules depending on nomograms/curves (Figs. 7.14, 7.15, 7.18, 7.22–7.26, 7.28–7.40; 8.4, 8.5, 8.9; 9.8–9.14, 9.22–9.32; 10.5–10.12; 11.5; 12.3, 12.13, 12.16, 12.19, 12.20; 13.6–13.10; 14.x photos; 15.x; 16.2, 16.10–16.20; 17.6, 17.13–17.16) carry only the numeric anchors quoted in the prose and are tagged "graph"/conf=medium where the value is chart-derived.
- OCR/format limitations: several tables were run together and were reconstructed (Tables 7.10, 7.11, 7.12, 7.13, 16.2–16.4, 16.7, 17.1) — ambiguous cells are flagged (Table 7.12 E162 Al#2; Table 7.13 second Al column; Table 16.4 row pairing). Many equations lost superscripts and fraction bars; they were rebuilt from the worked numbers and the stated symbol definitions (checked arithmetically).
- Source inconsistencies found and flagged rather than copied: §7.9 uses Ae = 1.06 cm^2 for turns and 71 mm^2 for core loss (Table 7.10 lists 1.21 cm^2); §7.11 initial N = 200 but continues with 70 turns and wire areas that do not match Table 7.9; §7.12.2.5 prints 13.4 W for 47.7 cm^3 x 0.300 W/cm^3 (= 14.3 W); §9.2.5 prints 270 us for a 2.7 us 3RC; §9.2.9 "0.4% duty" (40%); Eq. 11.2 printed with Vdc^2 but applied with (2Vdc)^2; §16.6.2 prints (2/pi)Vdc for the (pi/2)Vdc centre-tap peak; §17.3.8.3 prints 25 C/W but uses 2.5 C/W; §17.3.9.3 prints 0.0025 for the ~0.25 mA timing current.
- Topics requested in the task but not present (quantitatively) in this range: right-half-plane-zero formula (Ch. 12 does not derive it; qualitative treatment is in part-1 §1.4/Ch. 4 — CHECK-rhpz-flag therefore requires an externally supplied f_RHPZ); current-mode slope compensation (Ch. 5, part-1 range); IEC 61000-3-2 (the book cites only its predecessor IEC555-2, in Ch. 16); SMPS EMI-filter attenuation design equations (only line-filter inductor design in §7.6 and qualitative EMI practice are given).
