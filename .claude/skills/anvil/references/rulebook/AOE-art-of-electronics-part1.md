# The Art of Electronics (3rd ed.), part 1 of 4 — Anvil rulebook

## 0. Citation

P. Horowitz and W. Hill, *The Art of Electronics*, 3rd ed. Cambridge, U.K. / New York, NY, USA: Cambridge University Press, 2015 (first ed. 1980, second ed. 1989). ISBN 978-0-521-80926-9 (hardback). www.cambridge.org/9780521809269.

BOOKTAG: AOE. This file is **part 1 of 4** (source text lines 1–19000 of `refs-text/Paul_Horowitz_Winfield_Hill_The_Art_of_Electronics_2015_Camb.txt`, 75,879 lines; finished through the end of §5.10.1 at line 19365 because Table 5.5 straddles the boundary). Rule ids AOE-1001 … AOE-1345 (345 rules). Parts 2–4 use AOE-2001…, AOE-3001…, AOE-4001….

**Chapters covered by this extraction (read in order):**
- Front matter: contents, list of tables, prefaces to the 1st/2nd/3rd editions, legal notices (lines 1–3167; orientation only, no rules).
- Ch.1 Foundations (pp.1–70): voltage/current/resistance, dividers, Thevenin, zeners, signals and decibels, capacitors and RC circuits, inductors and transformers, diodes/rectifiers/clamps/inductive kick, impedance and reactance, RC and LC filters, an AM radio, switches, relays, connectors, indicators, variable components, markings and SMT.
- Ch.2 Bipolar Transistors (pp.71–130): switches, followers, current sources, CE amplifiers, Ebers–Moll rules of thumb, mirrors, differential amplifiers, push-pull, Darlington/Sziklai, bootstrapping, paralleling/ballasting, Miller effect, negative feedback, example circuits, review.
- Ch.3 Field-Effect Transistors (pp.131–222): FET characteristics and spreads, JFET sources/amplifiers/followers/variable resistors, gate current, analog switches and their limitations, CMOS logic, power MOSFETs (gate charge, ratings, body diode, ESD, paralleling, thermal runaway), IGBTs/thyristors, depletion-mode circuits, Tables 3.1–3.8, review.
- Ch.4 Operational Amplifiers (pp.223–291): golden rules, basic circuits, cautions, smorgasbord (boosters, regulator, comparators, Schmitt, rectifiers, oscillator), op-amp limitations and their effects, peak detector/S-H/clamp/integrator/differentiator, single-supply operation, capacitive loads, rail splitters, typical circuits, frequency compensation, Tables 4.1–4.2b, review.
- Ch.5 Precision Circuits, §5.1–§5.10.1 (pp.292–322): error budgets, the precision millivoltmeter, unspecified parameters, autonulling amplifier error budget, component errors (resistors, hold capacitor leakage and dielectric absorption, nulling switch), amplifier input errors (Z_in, I_B, V_os, CMRR, PSRR), output errors (slew, settling, crossover, output impedance, gain error, gain nonlinearity, phase error and active compensation), RRIO pitfalls, choosing a precision op-amp (Tables 5.1–5.5).

**Not read in this part (with reason):** Ch.5 from §5.10.2 onward, Chapters 6–15, Appendices A–P and the index — outside the assigned line range (lines 19000–75879 are assigned to parts 2–4). Within the range nothing was skipped except the end-of-chapter "Additional Exercises" (problem sets; skimmed for embedded data only) and the pure-math complex-number derivation in §1.7.3–1.7.4 (results kept).

**Notation / OCR conventions.** The OCR renders micro as "m", "j", "/i", "|j" and ohm as "Q", "£2", "O", "fi"; values were converted to SI from context (uA, uV, uF = micro-units; ohm, kohm, Mohm). "C" after a number = degrees Celsius. "rtHz" = square root of hertz. Cells marked "(as read)" or "OCR-reconstructed" came from scrambled table columns and should be verified against the printed book before being used as hard limits. Page numbers are the printed page numbers (p.NNN).

## 1. Design rules

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| AOE-1001 | components | Chip-component size codes: the 4-digit inch code gives each dimension in units of 0.010 in (0.25 mm); the metric code uses units of 0.1 mm, sometimes without saying so. 0805 (inch) = 2.0 x 1.25 mm = 80 x 50 mil = "2012" metric; 0402 inch = 1005 metric; 0201 inch = 0603 metric; 01005 inch = 0402 metric = 0.4 x 0.2 mm (0.016 x 0.008 in). Height is specified separately. State inch vs metric explicitly on every footprint/BOM line | inch code AABB: L = 0.254*AA mm, W = 0.254*BB mm; metric code: L = 0.1*AA mm, W = 0.1*BB mm | package code, code system | SMT passives; footprint/BOM consistency | inspect | p.4 fn7; p.65 Fig 1.132 | high |
| AOE-1002 | derating | The generic RN55D 1% metal-film axial resistor is rated 1/8 W in its MIL-spec RN55 grade but 1/4 W in its CMF-55 industrial grade; derate against the conservative (MIL) rating when the grade is unknown | P_rated(RN55) = 0.125 W; P_rated(CMF-55) = 0.25 W | resistor grade | axial metal-film resistors | review | p.4 fn8 | high |
| AOE-1003 | components | Resistor catalog ranges: 0.0002 ohm to 1e12 ohm; standard power ratings 1/8 W to 250 W; tolerances 0.005 % to 20 %. Common film types come 1 ohm to 10 Mohm in 5 %, 2 %, 1 %; the 1 % series has 96 values/decade, the 2 % and 5 % series 24 values/decade | E96 = 96 values/decade (1 %); E24 = 24 values/decade (2 %, 5 %) | tolerance class, value | resistor value selection | inspect | p.4-5 box "Resistors"; App. C | high |
| AOE-1004 | components | Trim a resistor by combination: to trim DOWN, choose the next standard value above target and parallel a much larger resistor (100x in parallel lowers the value by 1 % with only 0.01 % error); to trim UP, choose a value below target and add a much smaller series resistor | R_eff = R*Rp/(R+Rp) ~ R*(1 - R/Rp); R_eff = R + Rs | target, available values | fixed-value trimming | calc | p.6 Shortcut #1, fn10 | high |
| AOE-1005 | components | Do not design to many significant figures: resistors are typically +/-5 % or +/-1 %, capacitors +/-10 % or +/-5 %, transistor parameters often known only to a factor of 2. A good design is insensitive to the precise values of its components (run tolerance corners) | tol_R = 1-5 %; tol_C = 5-10 %; transistor params within x2 | component tolerances | all analog design | sim | p.6 | high |
| AOE-1006 | derating | Resistor dissipation P = I*V = I^2*R = V^2/R must not exceed the (derated) rating. Example: no resistor > 1k can exceed 1/4 W across a 15 V supply (225 mW max) | P = V^2/R <= P_rated_derated | V across R, I, R | every resistor | calc | p.6 §1.2.2C, Ex.1.5 | high |
| AOE-1007 | components | Millman's theorem for passive summing networks: Vout = sum(Vi*Gi)/sum(Gi), Gi = 1/Ri | Vout = (sum Vi/Ri)/(sum 1/Ri) | Vi, Ri | resistive summing/averaging nodes | calc | p.6 fn11 | high |
| AOE-1008 | components | Unloaded divider Vout = Vin*R2/(R1+R2). Thevenin equivalent: VTh = Vin*R2/(R1+R2), RTh = R1*R2/(R1+R2). A divider is a poor ("soft") voltage source; loaded output = VTh*RL/(RL+RTh). Example: 10k-10k from 30 V = 15 V behind 5k | eq 1.6, 1.8, 1.9 | R1, R2, RL, Vin | resistive dividers used as bias/reference | calc | p.7-11 §1.2.3, 1.2.5 | high |
| AOE-1009 | power | Battery source models: 9 V alkaline ~ ideal 9 V in series with 3 ohm, ~3 A short-circuit (kills the battery in minutes). D cell: 1.5 V, ~0.25 ohm series resistance, ~10,000 W*s energy; at end of life ~1.0 V with several ohms | Rs(9 V alkaline) = 3 ohm; Rs(D) = 0.25 ohm fresh, several ohm at EOL; E(D) ~ 1e4 J | battery type, load current | battery-powered designs (droop at peak load, EOL) | calc | p.8-9 §1.2.4 | high |
| AOE-1010 | test | Meter loading: DMMs present 10 Mohm to 1000 Mohm on voltage ranges (some 1e9 ohm on 0.2 V and 2 V ranges but only 1e7 ohm on higher ranges - read the spec); a VOM is 20,000 ohm/V (50 uA movement). Compute the reading error with the divider equation. Current ranges impose a 0.1-0.25 V burden at full scale | Vread = VTh*Rin/(Rin + RTh); burden = 0.1-0.25 V at full scale | meter Rin per range, node RTh | bench measurements, test procedures | calc | p.10 box "Multimeters" | high |
| AOE-1011 | test | Never put an ammeter (or ohmmeter) directly across a voltage source such as a wall plug to "measure its current" - leading cause of blown meters | n/a | test procedure | bring-up/test instructions | review | p.10 box | high |
| AOE-1012 | components | Avoid circuit loading: make the load resistance large compared with the source (Thevenin) resistance of what drives it. Exceptions: a current source (high internal R) should drive a relatively low-R load; transmission lines/RF must be matched (R_load = R_internal = Z0) to prevent reflection and loss | V_out/V_oc = RL/(RL + Rs); target RL >> Rs | RL, Rs | every interstage connection | calc | p.11 §1.2.5A, fn15; p.69 Review G | high |
| AOE-1013 | matching | Maximum power transfer to a load occurs at R_load = R_source; ordinary signal circuits are instead designed with R_load >> R_source | P_load max at RL = Rs | RL, Rs | power/RF matching | calc | p.11-12 §1.2.5B | high |
| AOE-1014 | power | Zener shunt regulator small-signal behavior is a divider with the zener's dynamic resistance: dVout = dVin*Rdyn/(R + Rdyn) = Rdyn*dIz. Worked example: 1N4733 (5.1 V, 1 W), Vin 15-20 V, R = 300 ohm -> Iz(max) = (20-5.1)/300 = 50 mA; Rdyn(max) = 7.0 ohm at 50 mA; Iz falls to 33 mA at 15 V; dIz = 17 mA gives dVout = 0.12 V | dVout = Rdyn*dIz; Iz = (Vin - Vz)/R - I_load | Vin range, R, Vz, Rdyn, I_load | zener regulators/references | calc | p.12-13 §1.2.6A, Fig 1.16 | high |
| AOE-1015 | components | Zener dynamic resistance varies roughly inversely with current. Example: Rdyn = 10 ohm at 10 mA for a 5 V zener, so a 10 % current change gives 10 mV (0.2 %) | Rdyn ~ k/Iz | Iz | zener bias-point choice | calc | p.12-13 §1.2.6A | high |
| AOE-1016 | components | Avoid low-voltage zeners (e.g., 3.3 V; low end of 1N5221-67): poor voltage constancy vs current. Zeners near 6 V (5.6 V 1N5232B, 6.2 V 1N5234B) have admirably steep curves. For low voltages use a two-terminal IC reference (e.g., LM385-1.2/-2.5): Rdyn < 1 ohm even at 0.1 mA, tempco better than 0.01 %/C | if Vz < ~5 V prefer IC reference; ref Rdyn < 1 ohm at 0.1 mA; TC < 0.01 %/C | Vz | voltage references | review | p.13, Fig 1.17 | high |
| AOE-1017 | components | A zener regulates better when fed from a current source (incremental R = infinity) than from a resistor | dVout -> 0 as R_feed -> infinity | bias method | zener references | review | p.13 | high |
| AOE-1018 | components | LED series resistor sizing: R = (Vsupply - V_LED)/I_LED. Example: red LED behaves like a 1.6 V zener; from a 5 V comparator pull-down path, 5 mA -> R = 3.4 V/5 mA = 680 ohm | R = (Vs - Vf - V_driver)/I_LED | Vs, Vf, I_LED | LED indicators | calc | p.13 §1.2.7 | high |
| AOE-1019 | components | LED forward drops: 1.5-2 V for red, orange and some green; 3.6 V for blue and high-brightness green (white = blue + phosphor). 2-10 mA gives adequate indicator brightness | Vf(red/orange) = 1.5-2 V; Vf(blue) = 3.6 V; I = 2-10 mA | LED color, supply | indicator headroom at minimum supply | calc | p.62 §1.9.4B | high |
| AOE-1020 | components | NTC thermistor sensitivity about -4 %/C (example 10 kohm at 25 C) | dR/R ~ -0.04 per C | thermistor | temperature sensing/limit circuits | calc | p.13 Fig 1.18 | high |
| AOE-1021 | components | Compare ratios (sensor divider vs reference divider from the same supply) so a threshold is insensitive to supply voltage; add hysteresis so the comparator is decisive | threshold set by ratio only | topology | comparator/threshold circuits | review | p.13 §1.2.7 | high |
| AOE-1022 | requirements | Sinewave amplitude conventions: Vrms = A/sqrt(2) = 0.707*A; Vpp = 2*A; unstated sinewave amplitude usually means rms. US mains 115 V rms, 60 Hz = 163 V amplitude = 325 Vpp. P = Vrms^2/R for any waveform. Average-responding meters are calibrated for sinewaves (Vrms = 1.11*Vavg); use a true-rms meter for other waveforms | Vrms = 0.707 A; Vpk(115 Vrms) = 163 V | waveform | amplitude specs; mains peak voltage | calc | p.14 §1.3.2, fn18; p.68 Review B | high |
| AOE-1023 | requirements | Decibels: dB = 10*log10(P2/P1) = 20*log10(A2/A1); 2x amplitude = +6 dB, 10x = +20 dB, 3 dB = 2x power. References: 0 dBV = 1 V rms; 0 dBm = 1 mW into the assumed Z (50 ohm RF -> 0.22 V rms; 600 ohm audio -> 0.78 V rms); 0 dB SPL = 20 uPa rms; -30 dBm = 1 uW; +3 dBV = 1.4 V rms. Always state the 0 dB reference | eq 1.11, 1.12 | levels, reference Z | specifications | calc | p.15 §1.3.2A; p.68 | high |
| AOE-1024 | timing | Rise time is defined as the 10 %-90 % transition time; typical circuit edges range from a few ns to a few us | tr = t(90 %) - t(10 %) | waveform | timing specs, scope measurements | measure | p.16 §1.3.3D, Fig 1.24 | high |
| AOE-1025 | hw-fw | 74LVC logic at +3.3 V: output levels typically 0 V and 3.3 V, input decision threshold 1.5 V; actual outputs can be as much as 0.4 V from ground or +3.3 V without malfunction | VOL <= 0.4 V; VOH >= 2.9 V; Vth = 1.5 V | logic family, supply | digital interfacing margins | inspect | p.17 §1.3.4 | high |
| AOE-1026 | rf | Sinewave frequencies up to ~2 GHz and above require special transmission-line techniques; beyond that (microwaves) lumped wired circuits are impractical and waveguides/striplines are used | f >~ 2 GHz -> transmission-line design | frequency | RF layout method | review | p.14 §1.3.1 | high |
| AOE-1027 | components | Parallel-plate capacitance C = 8.85e-14*er*A/d farads with A in cm^2 and d in cm (d << plate size); 1 cm^2 plates 1 mm apart give < 1 pF. Dielectric constants: air 1, polypropylene 2.1, polyester 3.1, C0G ceramic 45, X7R ceramic 3000 | C[F] = 8.85e-14*er*A[cm^2]/d[cm] | er, A, d | parasitic/plate capacitance estimates | calc | p.18 eq 1.14, fn21 | high |
| AOE-1028 | components | Capacitor current I = C*dV/dt (1 A into 1 F = 1 V/s; 1 mA into 1 uF = 1000 V/s; a 10 ms, 1 mA pulse raises 1 uF by 10 V). Stored energy U = 0.5*C*V^2 joules | I = C dV/dt; U = 0.5 C V^2 | C, V, I, t | inrush, ramp, hold-up energy | calc | p.19 eq 1.15, 1.16 | high |
| AOE-1029 | decoupling | Bypass capacitors are usually omitted from schematics (including this book's) but must never be omitted from the actual circuit: bypass every dc supply rail to ground with one or more capacitors; 0.1 uF to 10 uF are common, non-critical values | C_bypass = 0.1-10 uF on every rail/IC supply pin | IC supply pins | every IC/rail | inspect | p.19 fn22; p.25 item (c) | high |
| AOE-1030 | components | Capacitor dielectric selection: ceramic and polyester for most non-critical uses; polycarbonate, polystyrene, polypropylene, Teflon or glass for demanding applications; tantalum where greater capacitance is needed; aluminum electrolytics for power-supply filtering | mapping application -> dielectric | application class | capacitor selection | review | p.20-21 §1.4.1 | high |
| AOE-1031 | components | Capacitors in parallel add (C = C1 + C2 + ...); in series 1/C = 1/C1 + 1/C2 + ...; for two: C = C1*C2/(C1 + C2) | eq 1.17, 1.18 | Ci | capacitor networks | calc | p.21 §1.4.1A | high |
| AOE-1032 | timing | RC step response: discharge V = V0*exp(-t/RC); charge Vout = Vf*(1 - exp(-t/RC)); time to reach V: t = RC*ln(Vf/(Vf - V)); 50 % at 0.7 RC; 10-90 % rise time = 2.2 RC; within 1 % (>99 %) after 5 RC ("5RC rule"). A 1 uF across 1.0k has tau = 1 ms | eq 1.20-1.22 | R, C | timers, delays, settling | calc | p.21-23 §1.4.2 | high |
| AOE-1033 | timing | RC delay into logic: drive the RC from a buffer (low source resistance) so the input is not loaded, and account for the receiving gate threshold deviating from Vdd/2 - it changes the delay and output pulse width. Avoid relying on such RC tricks where possible | t_d = RC*ln(Vdd/(Vdd - Vth)); = 0.7 RC at Vth = Vdd/2 | R, C, Vth min/max | RC delay/edge circuits | calc | p.23 §1.4.2D, Fig 1.37 | medium |
| AOE-1034 | timing | RC timer with comparator reference at 1/e (37 %) of the supply: the comparator switches after exactly one time constant (1 minute timer with ~6 Mohm nearest standard value) | t = RC when Vref = Vs/e | R, C, Vref | RC timers | calc | p.23-24 Fig 1.38 | high |
| AOE-1035 | protection | Connecting a discharged capacitor directly across a supply draws a large transient (I = C dV/dt with dt -> 0); add a series resistor: in the timer example it limits peak to a modest 50 mA while still charging > 99 % in 5 RC (0.05 s) | I_pk = Vs/R_series; t_charge ~ 5*R_series*C | Vs, R, C | capacitor charge paths, pushbuttons, hot-plug | calc | p.24-25 note (a) | high |
| AOE-1036 | components | The comparator used in Ch.1 examples drives loads up to ~20 mA; its output bounces as a slow exponential crosses the reference unless hysteresis (positive feedback) is added | I_out <= ~20 mA; hysteresis required for slow inputs | comparator, input slew | comparator outputs | review | p.23-25 note (b) | high |
| AOE-1037 | timing | Passive RC differentiator Vout ~ RC*dVin/dt holds only if omega*RC << 1 for the highest frequency present (RC < 1/omega), and R must not load the source (at an edge the source sees R). Passive RC integrator holds only if the lowest signal frequency is well above f3dB (RC large, Vout << Vin) | omega_max*RC << 1 (diff); omega_min*RC >> 1 (int) | R, C, signal band | passive differentiators/integrators | calc | p.25-27; p.51 §1.7.10 | high |
| AOE-1038 | emc | Differentiated spikes on a signal line indicate capacitive coupling from a nearby square wave: first suspect a missing resistor termination; otherwise reduce the victim's source resistance or reduce the coupling capacitance. A square wave that looks differentiated on a scope usually means a broken connection (often at the probe) forming a tiny C with the scope input R | n/a | observed waveform | debug/bring-up | review | p.26 §1.4.3A, Fig 1.45 | high |
| AOE-1039 | components | Constant-current ramp: V(t) = (I/C)*t until the current source reaches its compliance limit (then it stops ramping). 1 mA into 1 uF reaches 10 V in 10 ms | V = I*t/C; V_max = compliance | I, C, compliance | ramp/sawtooth generators, timers | calc | p.27 §1.4.4A, Ex.1.18 | high |
| AOE-1040 | components | Real capacitors have series resistance (frequency dependent), series inductance, frequency-dependent parallel resistance, and dielectric absorption (after charging to V0, holding, then shorting, the voltage drifts back toward V0) | n/a | application | S/H, integrators, timers, precision | review | p.28 §1.4.5 | high |
| AOE-1041 | magnetics | Inductor: V = L*dI/dt (1 V across 1 H ramps 1 A/s); stored energy U = 0.5*L*I^2; inductance of a coil of fixed geometry is proportional to turns^2 | eq 1.23, 1.24 | L, I, V | switchers, chokes | calc | p.28 | high |
| AOE-1042 | magnetics | Wheeler's formula for a single-layer air-core coil: L ~ K*d^2*n^2/(18*d + 40*l) microhenry, d = diameter, l = length, n = turns, K = 1.0 for inches or 2.54 for cm; accurate to 1 % for l > 0.4*d | L[uH] = K d^2 n^2/(18d + 40l) | d, l, n | air-core coil design | calc | p.28-29 | high |
| AOE-1043 | magnetics | Volt-second balance: in steady state the average voltage across an inductor is zero (else its current rises without limit). Hence a synchronous buck switched at 50 % duty gives Vout = Vin/2 and the reversed (boost) connection gives Vout = 2*Vin | <V_L> = 0; Vout = D*Vin (buck) | duty, Vin | switching converters | calc | p.29-30 §1.5.1A, Fig 1.52 | high |
| AOE-1044 | magnetics | Transformers: voltage scales with turns ratio n, current with 1/n, impedance with n^2; little primary current if secondary unloaded (magnetizing inductance - so no dc transformer); leakage inductance gives load-dependent drop and degrades fast edges. Instrument power transformers: secondaries 10-50 V at 0.1-5 A; power-conversion transformers run 50 kHz-1 MHz; LF and HF transformers are not interchangeable | Z_sec/Z_pri = n^2 | n, frequency | transformer selection | review | p.30-31 §1.5.2 | high |
| AOE-1045 | components | Silicon signal diode (1N4148): ~0.6 V forward at 10 mA; forward drop 0.5-0.8 V in general; reverse leakage in the nA range; reverse breakdown (PIV) 75 V. Never drive a non-zener diode into reverse breakdown | V_F ~ 0.6 V @ 10 mA; V_R(max) < PIV | diode type, currents | all diode applications | calc | p.31 §1.6.1, Fig 1.55 | high |
| AOE-1046 | components | Schottky diodes have lower forward voltage and zero reverse-recovery time but more capacitance than junction diodes (and higher leakage - Table 1.1) | see Table 1.1 | diode type | rectifier/clamp/detector selection | review | p.32 Table 1.1 note b | high |
| AOE-1047 | power | Capacitor-input rectifier ripple (constant-current load approximation, conservative): dVpp = I_load/(f*C) half-wave; dVpp = I_load/(2*f*C) full-wave, f = line frequency (full-wave ripple at 2f, 120 Hz on 60 Hz mains). Choose R_load*C >> 1/f | dV = I/(f C) (HW); I/(2 f C) (FW) | I_load, C, f_line | unregulated dc supplies | calc | p.32-33 §1.6.3A eq 1.25 | high |
| AOE-1048 | power | Design the reservoir capacitor for worst case: supply capacitors have typical tolerances of 20 % or more; the most common load (a voltage regulator) is a constant-current, not resistive, load | C_min = 0.8*C_nom (or worse) | C tolerance | unregulated supplies | calc | p.33 §1.6.3A | high |
| AOE-1049 | power | A full-wave bridge puts two diode drops in series with the input (significant for low-voltage supplies). Packaged bridges: smallest 1 A average with 100-600 V (or 1000 V) breakdown; large ones 25 A or more | V_dc,pk = V_sec,pk - 2*V_F | V_sec, V_F | rectifier design | calc | p.32-33 §1.6.2, 1.6.4A | high |
| AOE-1050 | magnetics | Center-tapped full-wave rectifier uses each half-secondary only half the time, so for equal dc output power the transformer needs sqrt(2) = 1.4 x the current rating of a bridge rectifier (2 x winding I^2R heating) | I_rating(CT) = 1.41 x I_rating(bridge) | topology | rectifier transformer sizing | calc | p.33-34 §1.6.4B | high |
| AOE-1051 | power | Brute-force capacitor filtering is poor: bulky/expensive capacitors, very short conduction angle raises I^2R heating, and output still tracks line and load. Better: enough C to reduce ripple to ~10 % of the dc voltage, then an active (linear or switching) feedback regulator | ripple_pp ~ 0.1*Vdc before regulator | ripple, Vdc | linear supplies | calc | p.34-35 §1.6.5 | high |
| AOE-1052 | components | A diode signal rectifier gives no output for signals below ~0.6 Vpp; use a Schottky (hot-carrier) diode (~0.25 V drop) or pre-bias the rectifier to its threshold with a matched diode, which also tracks the drop's temperature change | V_sig,pp > V_F | V_sig | small-signal rectifiers/detectors | calc | p.35-36 §1.6.6A, Fig 1.70 | high |
| AOE-1053 | power | Diode-OR battery backup: example RTC ICs (NXP PCF8563, Seiko S-35390A) run 1.8-5.5 V at ~0.25 uA -> ~1e6 h (a hundred years) from a CR2032 coin cell | life[h] = capacity[Ah]/I_standby[A] | I_standby, cell capacity | backup power domains | calc | p.36 Fig 1.71 | high |
| AOE-1054 | protection | Diode clamp design: the series resistor limits clamp current but adds its value to the signal's Thevenin source resistance (compromise); the opposite excursion must not exceed the diode's reverse breakdown (-75 V for 1N4148). Diode clamps are standard on all CMOS logic inputs to survive static discharge in handling | I_clamp = (Vin - V_clamp - V_F)/R_s <= diode/pin rating | Vin extremes, R_s | input clamps | calc | p.36 §1.6.6C, Fig 1.72 | high |
| AOE-1055 | protection | A clamp referenced to a divider needs a stiff reference: the divider's Thevenin resistance must be small compared with the series resistor. Use a transistor/op-amp buffer (few ohms) or bypass the lower leg: 15 uF makes a 1k-leg divider look < 10 ohm above 1 kHz (no help at dc) | R_Th,ref << R_series | R_Th, R_s, frequency | clamps to derived rails | calc | p.36-37 Figs 1.73-1.76 | high |
| AOE-1056 | protection | Back-to-back diode limiter (+/-0.6 V) is a common high-gain amplifier input protection: an amplifier with gain 1000 on +/-15 V saturates unless its input stays within +/-15 mV | Vin_max = V_sat/G | G, supplies | amplifier input protection | calc | p.37 §1.6.6D | high |
| AOE-1057 | components | Silicon diode forward drop decreases ~2 mV/C; cancel it with a matched diode at the same temperature (whose bias current exceeds the maximum signal current) | dV_F/dT ~ -2 mV/C | temperature range | log converters, rectifiers, bias | calc | p.38 §1.6.6E | high |
| AOE-1058 | protection | Inductive kick: interrupting inductor current with no path forces the switch terminal up until something breaks down (~1000 V across contacts; destroys transistors; radiates interference). Put a diode across every dc-driven inductive load (relay coil etc.); the diode must carry an initial current equal to the steady inductor current (1N4004 is fine for nearly all cases) | I_D,pk = I_L; V_switch = Vsupply + V_F | I_L, Vsupply | dc relays, solenoids, motors | inspect | p.38-39 §1.6.7, Figs 1.83-1.84 | high |
| AOE-1059 | protection | Where the inductor current must decay quickly (fast relays, actuators, shutters, magnet coils) use a resistor across the inductor with Vsupply + I*R below the switch's maximum voltage, or a zener/voltage clamp, which gives a linear ramp-down (fastest for a given maximum voltage) | Vsupply + I_L*R < V_sw,max; t_decay(zener) = L*I_L/V_Z | I_L, L, V_max | fast-release inductive loads | calc | p.39 | high |
| AOE-1060 | protection | Ac-driven inductive loads (transformers, ac relays) cannot use a diode (it conducts on alternate half-cycles); use an RC snubber (typical values Fig 1.85) or a bidirectional TVS/MOV. Every instrument running from the ac line should include a snubber (power transformer is inductive); its capacitor must be rated for across-the-line service | snubber present; C class = across-the-line | load type | ac-line equipment | inspect | p.39 Fig 1.85, fn33 | high |
| AOE-1061 | protection | Include a transient suppressor across the ac power-line terminals, with appropriate fusing: bidirectional TVS zener or MOV (available 10 V to 1000 V, transient currents up to thousands of A) | TVS/MOV + fuse at mains entry | mains input | line-powered equipment | inspect | p.39 §1.6.7 | high |
| AOE-1062 | power | Charging a capacitor from a voltage source through a resistor loses half the energy in the resistor (50 % efficiency); resonant LC charging is lossless (ideal parts) and charges to 2*Vin in a half-cycle of f = 1/(2*pi*sqrt(LC)); a series diode ends the cycle | eta_RC = 50 %; V_final = 2 Vin; t_f = pi*sqrt(LC) | L, C, Vin | flashlamp/strobe/HV charging | calc | p.39-40 §1.6.8, Fig 1.86 | high |
| AOE-1063 | components | Reactance: Xc = 1/(2*pi*f*C), XL = 2*pi*f*L; impedances Zc = -j/(omega*C), ZL = j*omega*L, ZR = R. Examples: 1 uF = 2653 ohm at 60 Hz and 0.16 ohm at 1 MHz; 1 uF across 115 V rms, 60 Hz draws 43.4 mA rms (61 mA peak) with zero average power | eq 1.26, 1.29, 1.32 | f, C, L | all ac analysis | calc | p.41-45 | high |
| AOE-1064 | power | Average power in reactive circuits P = Re(V*conj(I)) with rms phasors; power factor = cos(phase angle), 0 (purely reactive) to 1 (resistive); a series capacitor C = 1/(omega^2*L) brings a series RL to unity power factor | eq 1.34; PF = cos(phi) | V, I | ac power, mains loads | calc | p.47-48 §1.7.6 | high |
| AOE-1065 | filter | Single-pole RC filter: f3dB = 1/(2*pi*R*C). Lowpass gain = 1/sqrt(1 + (omega*R*C)^2); highpass gain = omega*R*C/sqrt(1 + (omega*R*C)^2). At f3dB gain = 0.707 (-3 dB, not -6 dB) and phase 45 deg; asymptotic rolloff -6 dB/octave = -20 dB/decade; phase within ~6 deg of its asymptote at 0.1*f3dB and 10*f3dB | eq 1.35, 1.36 | R, C, f | RC filters | calc | p.49-51 §1.7.8-1.7.9, Fig 1.104 | high |
| AOE-1066 | filter | Worst-case impedances of a simple RC lowpass or highpass are both R (minimum input impedance = R, maximum output impedance = R). Design rule: drive the filter from a source impedance small vs R and load it with >= 10 x R. Example: amplifier with 100 ohm output -> R = 1k, load >= 10k | R >> Z_source; Z_load >= 10*R | Z_source, R, Z_load | passive RC filter design | calc | p.44 §1.7.1D, Ex.1.23 | high |
| AOE-1067 | filter | DC-blocking (coupling) capacitor: place the highpass corner below all frequencies of interest. Audio 20 Hz-20 kHz: choose f_min ~ 5 Hz -> RC = 1/(2*pi*5) ~ 30 ms; R = 10 kohm, C = 3.3 uF; the next stage's input R must be >> 10 k and the driver must drive 10 k | RC >= 1/(2*pi*f_min) | signal band, R | ac coupling | calc | p.43 §1.7.1C, Fig 1.93 | high |
| AOE-1068 | filter | Coupling pulses through a blocking capacitor: require tau = RC >> T (pulse duration); droop ~ T/tau, followed by a comparable overshoot at the next transition | droop = T/(RC) | T, R, C | ac-coupled pulses/clocks/data | calc | p.43 | high |
| AOE-1069 | filter | Cascading identical passive RC sections does not multiply their responses - each stage loads the previous. Make each successive section much higher impedance than the preceding one, or buffer between stages (transistor/op-amp, active filter) | Z_(k+1) >> Z_k (use the 10x rule of AOE-1066) | section impedances | multi-pole passive filters | calc | p.52 §1.7.13 | medium |
| AOE-1070 | filter | Filter order: each RC pole adds 6 dB/octave (20 dB/decade): 2 sections 12 dB/octave, 3 sections 18 dB/octave ("n-pole filter") | slope = -6*n dB/octave | n | filter order selection | calc | p.52 §1.7.13 | high |
| AOE-1071 | filter | LC resonance f0 = 1/(2*pi*sqrt(L*C)). A parallel LC ("tank") has infinite ideal impedance at f0 (bandpass when driven through R; higher driving impedance = sharper peak); a series LC has zero ideal impedance at f0 (trap/notch). Q = f0/BW(-3 dB); parallel RLC: Q = omega0*R*C = R/Xc = R/XL; series RLC: Q = omega0*L/R = XL/R. A Q-spoiling resistor may be added deliberately | eq 1.37; Q formulas fn46, fn48 | L, C, R | tuned circuits, traps | calc | p.52-53 §1.7.14 | high |
| AOE-1072 | filter | Resonator ringdown after a step or pulse: voltage falls to 1/e (37 %) in Q/pi cycles (2Q radians); stored energy falls to 1/e (61 % in amplitude) in Q/(2*pi) cycles (Q radians) | t(V -> 1/e) = Q/(pi*f0) | Q, f0 | tuned-circuit transients, Q measurement | measure | p.54 §1.7.14 | high |
| AOE-1073 | filter | A real series LC trap has a nonzero minimum impedance at resonance, usually dominated by the inductor's losses (ESR) | Z_min = ESR_L + ESR_C | component ESR | notch/trap filters | review | p.53 Fig 1.108 | high |
| AOE-1074 | filter | A single RC lowpass with 1 MHz "cutoff" (1 kohm, 160 pF) hardly cuts anything off below 2 MHz; for anti-alias or steep filtering use an LC ladder (the example: 3 inductors + 4 capacitors cutting off at 1.0 MHz) or an active filter | compare swept responses | filter spec | anti-alias filters | sim | p.54 §1.7.15, Figs 1.111-1.112 | high |
| AOE-1075 | filter | Prefer capacitors over inductors for RC/RL-style filters (inductors are bulkier, costlier, less ideal). Exception: ferrite beads / RF chokes on interconnects raise impedance at very high frequencies and prevent parasitic oscillations without the series resistance an RC would add | n/a | filter/stability need | HF stability, supply filtering | review | p.51 §1.7.11 | high |
| AOE-1076 | decoupling | Bypass capacitor criterion: its impedance at the lowest signal frequency must be small compared with the impedance of the element it bypasses | 1/(2*pi*f_min*C) << R_bypassed | f_min, R | emitter/reference/rail bypassing | calc | p.54-55 §1.7.16A | high |
| AOE-1077 | rf | AM envelope detector: choose R1*C2 long compared with the carrier period (~1 us) but short compared with the period of the highest audio frequency (~200 us) | T_carrier << R1*C2 << T_audio,min | f_carrier, f_audio,max | envelope/peak detectors | calc | p.55 §1.8 | high |
| AOE-1078 | test | Probe/cable capacitance loads circuits: BNC coax ~30 pF/ft; ordinary scope probe ~10 pF - a bare coax on a tuned node detunes it; use a proper probe | C_coax ~ 30 pF/ft; C_probe ~ 10 pF | node impedance | measuring tuned or high-Z nodes | review | p.56 §1.8 | high |
| AOE-1079 | components | Switch ratings: a small toggle might be rated 150 V, 5 A. Inductive loads drastically reduce switch life (arcing at turn-off). For low-level signals use switches designed for "dry switching" (gold-plated contacts); ordinary contacts rely on load current to clean oxides and become noisy/intermittent | V, I <= rating; gold contacts for low-level signals | load type, level | switch selection | review | p.58 §1.9.1E, fn50 | high |
| AOE-1080 | components | Rotary switches: shorting (make-before-break) types prevent an open input between positions; non-shorting (break-before-make) types are required when the switched lines must never be connected to each other. Toggle and momentary switches are always break-before-make | n/a | circuit requirement | switch selection | review | p.58 §1.9.1A-C | high |
| AOE-1081 | components | Rotary encoders provide typically 16-200 pulse pairs per revolution; optical types cost more but last indefinitely (mechanical-contact types wear) | 16-200 pulse pairs/rev | UI requirement | user controls | review | p.58 §1.9.1C | high |
| AOE-1082 | components | Relays: coil voltages 3-115 V ac or dc; reed and mercury-wetted relays for ~1 ms operation. SSRs (LED-driven semiconductor switch) have no contact bounce and switch ac smartly (turn on at zero voltage, off at zero current). Use relays mainly for remote and high-voltage/high-current switching where complete isolation is needed | t_op(reed) ~ 1 ms | isolation need, load | relay/SSR selection | review | p.59 §1.9.2 | high |
| AOE-1083 | connectors | Connectors are usually the most unreliable part of any equipment. Avoid connectors that cannot tolerate being dropped (miniature hexagon) or lack a secure locking mechanism (Jones 300 series). Two-part PCB connectors (e.g., VME) are more reliable than card-edge connectors (15 to 100+ gold-plated contacts) | n/a | connector choice | interconnect selection | review | p.59-61 §1.9.3 | high |
| AOE-1084 | connectors | BOM blacklist ("Components Hall of Infamy"): low-value wirewound pots, UHF connectors, electrical tape, Cinch-type connectors, microphone connectors, hexagon connectors, slide switches, cheap (non-screw-machined) IC sockets, type-F connectors, open-element trimmer pots, phono (RCA) connectors (signal mates before shield; both contacts tend to make poor contact) | none of listed parts in BOM | BOM | parts selection | inspect | p.60-63 Fig 1.126 | high |
| AOE-1085 | components | Resist using many trimmers - use good design instead. Never use a pot as a precise resistor (less stable than 1 % resistors, poor resolution); if a settable precise value is needed, use a 1 % (or better) fixed resistor supplying most of the value in series with a small trimmer (e.g., 23.4k = 22.6k 1 % + 2k trimmer) or a series string of precision resistors | R_fixed ~ 0.9-0.97 of R_total | R target, adjust range | calibration adjustments | calc | p.63 §1.9.5A | high |
| AOE-1086 | components | Digital potentiometers (resistor chain + switches) offer up to 1024 steps, single or dual, some nonvolatile (retain setting without power). Variable capacitors are limited to small values (up to ~1000 pF); variable (slug) inductors typically tune 2:1 | steps <= 1024; C_var <= ~1000 pF; L tuning 2:1 | adjust need | digital trim, RF tuning | review | p.63-64 §1.9.5 | high |
| AOE-1087 | test | Variac (autotransformer): typically 0-135 V ac from a 115 V line, 1-20 A; use it to verify worst-case performance vs line voltage. WARNING: output is not isolated from the power line | Vout 0-135 V | line range to test | line-variation testing | review | p.64 §1.9.5D | high |
| AOE-1088 | assembly | Marking ambiguities: a capacitor "470" may be 470 pF (integer) or 47 x 10^0 = 47 pF (exponent notation); a "K" suffix means +/-10 % tolerance; 4-digit date codes (yyww) masquerade as part numbers; tiny SMT parts carry only vendor codes (LMV981: SOT23 "A78A", SC70 "A77", microSMD "A"). Verify by reel label/BOM, not by markings | n/a | incoming parts | incoming inspection, rework | inspect | p.64-65 Fig 1.130 | high |
| AOE-1089 | components | BJT current gain beta (hFE) is not a good parameter: typically ~100 (review: ~150), it varies 50-250 between specimens of one type (a 3:1 spread or more), with further 3:1 spreads vs collector current and vs temperature; datasheet typical-beta curves have production spreads of +100 %/-50 %. A circuit that depends on a particular value of beta is a bad circuit | design must work for beta_min..beta_max (e.g., 0.5x..2x typ) | beta range | every BJT circuit | sim | p.72 §2.1.1; p.74 Fig 2.4 caption; p.126 Review C | high |
| AOE-1090 | derating | BJT maximum ratings Ic, Ib, VCE (and reverse VBE, power dissipation Ic*VCE, temperature) must not be exceeded; forward VBE above ~0.6-0.8 V draws enormous current (never apply an arbitrary voltage across B-E) | Ic <= Ic_max; VCE <= VCEO; P = Ic*VCE <= P_derated | Ic, VCE, VBE | every BJT | calc | p.72 §2.1.1 rules 2-3 | high |
| AOE-1091 | components | Saturated switch: typical VCE(sat) 0.05-0.2 V (review: 25-200 mV). Overdrive the base: base current ~1/10 of maximum collector current is common (the lamp example used 9.4 mA where 1.0 mA barely sufficed). Extra drive is needed because beta drops at low VCE, for incandescent lamps (cold resistance 5-10x lower), and for high-speed switching | Ib >= Ic_max/10 (typical practice); Ib >> Ic/beta_min | Ic_max, beta_min | BJT saturated switches | calc | p.73-74 §2.2.1; p.126 Review D | high |
| AOE-1092 | components | Add a base pull-down resistor (e.g., 10k) so the base sits at ground when the drive is open; a few-pF "speed-up" capacitor across the base resistor improves high-speed switching | R_BE ~ 10k (0.06 mA); C_speedup = a few pF | drive circuit | BJT switches | inspect | p.74 §2.2.1, fn6 | high |
| AOE-1093 | protection | If a switched load can swing below ground (ac-driven or inductive), add a diode in series with the collector (or reverse diode to ground) to prevent collector-base conduction; for inductive loads always add a suppression diode across the load (or R, RC, zener clamp for faster turn-off) - otherwise the collector exceeds its C-E breakdown | clamp present; V_C,peak < BV_CEO | load type | BJT/MOSFET low-side switches | inspect | p.74-75 §2.2.1 cautions 2-3, Fig 2.6 | high |
| AOE-1094 | components | Mechanical switch contacts bounce, making and breaking the circuit a few dozen times in the first few ms after actuation; route only dc control levels through front-panel cables/switches ("remote cold switching") rather than signals (capacitive pickup, degradation) | bounce duration ~ few ms | switch inputs | UI inputs, firmware debounce | review | p.75 §2.2.1 | high |
| AOE-1095 | components | LED drive with saturated npn: choose I_LED for brightness (e.g., 5 mA), R_C = (Vsupply - V_F(LED) - V_CE(sat))/I_LED, then choose R_B for saturation assuming a conservatively low beta (beta >= 25 is safe for a 2N3904). Never switch a voltage directly across an LED (steep I-V: 5 V across an LED blows it out). LED V_F 1.5-3.5 V; high-efficiency indicators look fine at a few mA, dazzling at 10-20 mA | R_B = (V_drive - 0.6)/(I_LED/25) or less | V_drive, Vsupply, V_F, I_LED | LED drivers from logic | calc | p.76 §2.2.2A, Fig 2.9 | high |
| AOE-1096 | components | High-side pnp switch driven via npn level shifter: pnp base pull-up (R3) keeps it off; the npn sinks pnp base current. Example: 3.3 kohm from 15 V gives ~4 mA base drive, enough for ~200 mA loads (beta > 50). The pull-up must not be too small: with 100 ohm the npn's available collector current could not develop the pnp's VBE and it would never switch | I_B(pnp) = I_C(npn) - 0.6/R3 >= I_load/beta_min | R2, R3, loads | high-side switching | calc | p.77 Fig 2.10, fn12 | high |
| AOE-1097 | protection | Capacitively-coupled base drive can pull a base negative by ~the supply swing: BJT base-emitter reverse breakdown is often as little as 6 V; reverse breakdown permanently degrades beta (and noise). The pulse circuit of Fig 2.11 must not run from more than +7 V for this reason (a common oversight). Add a protective diode (Fig 2.19) or inter-emitter resistor | V_EB(reverse) < V_EBO (~6 V) | coupling path, swing | pulse circuits, followers, diff-amp inputs | calc | p.77 fn13; p.82 Fig 2.19; p.104 | high |
| AOE-1098 | timing | Transistor one-shot (Fig 2.11): output pulse width ~ 0.63*R*C (C charging from -4.4 V toward +5 V until VBE ~ 0.6 V); such discrete pulsers are neither accurate nor stable - prefer a dedicated timer/pulse IC | T_pulse = 0.63*R3*C1 (example 63 us with RC = 100 us) | R, C, supply | pulse generation | calc | p.77-78 Ex.2.2; p.128 Review L | high |
| AOE-1099 | timing | Slow input edges crossing a switching threshold must go through a Schmitt trigger (hysteresis). Example discrete Schmitt thresholds ~+700 mV and ~+800 mV (emitter resistor carries 5 mA vs 10 mA). Good practice favors dedicated comparator ICs | hysteresis = V_T+ - V_T- > noise_pp | input slew, noise | slow/noisy logic inputs | review | p.78-79 Fig 2.13; p.128 Review M | high |
| AOE-1100 | components | Emitter follower: V_E = V_B - 0.6 V (0.6-0.7 V less). Input impedance Z_in = (beta + 1)*Z_load; output impedance Z_out = Z_source/(beta + 1) + r_e. Keep Z_out(source) << Z_in(load): a factor of 10 is a comfortable rule of thumb | eq 2.2-2.4; Z_source <= Z_load/10 | beta, R_s, R_L | followers, buffers, interstage | calc | p.79-80 §2.2.3A-B; p.93 §2.3.3 | high |
| AOE-1101 | components | Emitter follower drives current in one direction only: an npn follower sources through the transistor but sinks only through its emitter resistor; its small-signal output impedance is low but its large-signal sinking impedance is as large as R_E - low small-signal Zout does not imply large output current. Fixes: smaller R_E (more dissipation), pnp (if signals are one-sided), or push-pull | I_sink,max = (V_out - V_EE)/R_E | R_E, V_EE, load | followers, regulators driving loads with their own supplies | calc | p.81 Figs 2.17-2.18 | high |
| AOE-1102 | power | A regulated supply whose output is an emitter follower cannot sink current forced into it by a load that contains other supplies/sources | reverse current -> output rises | load topology | multi-supply systems | review | p.81-82 | high |
| AOE-1103 | power | Zener shunt regulator worst-case design: (Vin(min) - Vz)/R > Iout(max) so some zener current always flows; zener dissipation P_Z = [(Vin - Vout)/R - Iout]*Vz, worst case at Vin(max) and Iout(min); include component tolerances and line limits. Shunt regulators need a high-power zener for widely varying loads; not adjustable; moderate ripple/regulation | R <= (Vin_min - Vz)/(Iout_max + Iz_min); P_Z,max = ((Vin_max - Vz)/R - Iout_min)*Vz | Vin range, Iout range, Vz | zener regulators | calc | p.82 §2.2.4, Fig 2.20 | high |
| AOE-1104 | power | Zener + emitter-follower regulator: zener current becomes nearly independent of load and zener dissipation drops by up to beta. Add collector resistor Rc for momentary short-circuit protection, sized so its drop at the highest normal load current is less than the drop across R (transistor must not saturate). Reduce ripple by RC-filtering the zener bias with RC >> 1/f_ripple | I_short = Vin/Rc; Rc*I_max < V_R; RC >> 1/f_ripple | loads, Vin | simple pass-transistor regulators | calc | p.82-83 Figs 2.21-2.22 | high |
| AOE-1105 | components | Emitter-follower biasing: place the quiescent point for maximum symmetrical swing (V_E = 0.5*Vcc single-supply); make the bias divider stiff: R1 parallel R2 <= (1/10)*beta*R_E (divider current large compared with base current). Always provide a dc path for base bias current (with capacitive input on split supplies add R_B to ground ~ beta*R_E/10) | R1*R2/(R1+R2) <= 0.1*beta_min*R_E | beta_min, R_E | all BJT bias networks | calc | p.83-84 §2.2.5, Fig 2.27 | high |
| AOE-1106 | components | Emitter-follower design example (audio 20 Hz-20 kHz, Vcc = +15 V, Iq = 1 mA): V_E = 7.5 V; R_E = 7.5k; V_B = 8.1 V (R1:R2 = 1:1.17); R1 parallel R2 <= 75k -> R1 = 130k, R2 = 150k; C1 >= 0.15 uF into ~63k; C2 >= 1.0 uF into load >= R_E; with two cascaded highpass sections raise them to avoid 6 dB loss at 20 Hz: C1 = 0.47 uF, C2 = 3.3 uF (E6 values). Output impedance with 10k source ~87 ohm, ~110 ohm including r_e | worked example | Vcc, Iq, band | ac-coupled followers | calc | p.84 §2.2.5A | high |
| AOE-1107 | components | Never bias a transistor with a base resistor from Vcc computed from an assumed beta ("Don't do this!", Fig 2.28). Use voltage biasing from a stiff divider plus emitter resistor: in the design example a beta change 100 -> 200 moves V_E by only 0.35 V (5 %) | dV_E/V_E small for beta 2x | bias topology | BJT bias review | review | p.85 §2.2.5C | high |
| AOE-1108 | components | Cascading a pnp follower and an npn follower (equal emitter resistors, split supplies) approximately cancels the VBE offsets; cancellation is imperfect because VBE depends on collector current and transistor size | V_out ~ V_in (mV-level residual) | | dc-offset-free followers | review | p.85 §2.2.5D, Fig 2.29 | high |
| AOE-1109 | components | Resistor-plus-voltage current source approximates constant current only while V_load << V (dissipation-hungry, not programmable). For a current constant to x % over load range V_L, the source voltage must be ~ V_L/(x/100) | I = V/R; error ~ V_load/V | V, V_load range | simple current sources | calc | p.85-86 §2.2.6A, Ex.2.9 | medium |
| AOE-1110 | components | BJT current source/sink: Ic ~ (V_B - 0.6 V)/R_E, independent of V_C while the transistor is not saturated (V_C > V_E + 0.2 V). Bias the base from a divider stiff vs beta*R_E, a zener, a two-terminal reference (LM385), forward-biased diodes, or a red LED (~1.6 V = three diodes) | eq 2.5 | V_B, R_E | current sources | calc | p.86 §2.2.6B-C, fn19 | high |
| AOE-1111 | components | Current-source compliance: from near saturation (V_C ~ V_E + 0.2 V; e.g., +1.1 V or +5.1 V in the examples) up to the supply; loads containing their own supplies may carry the collector beyond the rails - then check V_CE <= BV_CEO and P = Ic*V_CE (and SOA for power transistors) | V_E + 0.2 <= V_C <= Vcc; V_CE <= BV_CEO; Ic*V_CE <= P_max | V_E, Vcc, load | current sources | calc | p.86 §2.2.6D | high |
| AOE-1112 | components | Common-emitter amplifier with emitter degeneration: gain = -R_C/(R_E + r_e) ~ -R_C/R_E; Z_in = R1 parallel R2 parallel beta*(R_E + r_e); Z_out ~ R_C (collector impedance is megohms). Input coupling C > 1/(2*pi*f*(R1 parallel R2)). Example: R_C = 10k, R_E = 1.0k, Ic = 1 mA: gain -10, Z_in ~ 8k, 0.1 uF -> 200 Hz corner | eq 2.6 | R_C, R_E, Ic, beta | CE amplifiers | calc | p.87-88 §2.2.7, Fig 2.35 | high |
| AOE-1113 | components | Unity-gain phase splitter: set quiescent collector at 0.75*Vcc for maximum symmetrical swing at both outputs; load both outputs with equal (or very high) impedances to keep gain symmetry. RC phase shifter driven by it: phi = 2*arctan(omega*R*C), constant amplitude; its load impedance should be large vs R_C and R_E | V_C,q = 0.75 Vcc; phi = 2 atan(omega R C) | loads | phase splitters/shifters | calc | p.88-89 §2.2.8, Figs 2.36-2.38 | high |
| AOE-1114 | components | Ebers-Moll: Ic = Is(T)*(exp(VBE/VT) - 1); VT = kT/q = 25.3 mV at 20 C (~25 mV at 25 C); Is ~ 1e-15 A for a small-signal transistor (2N3904), ~1e11 x smaller than Ic; beta "constant" 20-1000 depending on type, Ic, VCE, T. Collector current is set by VBE (accurately, nanoamps to milliamps), not by base current | eq 2.8-2.11 | VBE, Is, T | BJT analysis, log circuits, mirrors | calc | p.91 §2.3.1 | high |
| AOE-1115 | components | VBE rules of thumb: +60 mV (58.2 mV at room T) per decade of Ic; Ic doubles per +18 mV; +4 % per mV; dVBE = VT*ln(Ic2/Ic1) (0.25 mV per % of current ratio) | Ic = Ic0*exp(dV[mV]/25) | Ic ratio | mirrors, ballasting, matching | calc | p.91-92 §2.3.2A; p.102 Fig 2.62 | high |
| AOE-1116 | components | Intrinsic emitter resistance r_e = VT/Ic = 25/Ic(mA) ohms (25 ohm at 1 mA, 2.5 ohm at 10 mA); transconductance gm = Ic/VT = 1/r_e = 40*Ic(mA) mS. r_e is in series with the emitter in all circuits: limits grounded-emitter gain, makes follower gain < 1, sets follower minimum output impedance | eq 2.12, 2.13 | Ic | small-signal BJT design | calc | p.92 §2.3.2B | high |
| AOE-1117 | thermal | VBE at constant Ic falls ~2.1 mV/C (roughly proportional to 1/T_abs); at constant VBE, Ic rises ~9 %/C (doubles per 8 C, x10 per 30 C, i.e., 8.4 %/C = 2.1 mV/25 mV). gm at fixed Ic falls ~0.34 %/C at 25 C | dVBE/dT = -2.1 mV/C; dIc/Ic = +8.4-9 %/C at fixed VBE | T range | bias stability, paralleling, thermal runaway | calc | p.92 §2.3.2C; p.112 fn58; p.127 Review I | high |
| AOE-1118 | components | Early effect: dVBE = -eta*dVCE with eta ~ 1e-4 to 1e-5 (2N5088: 1.3e-4 -> 1.3 mV per 10 V); equivalently Ic = Ic0*(1 + VCE/VA), Early voltage VA typically 50-500 V; collector output resistance r_o = VA/Ic; pnp and high-beta parts tend to low VA (2N5087: VA = 55 V, eta = 4e-4 -> 4 mV shift or +17 % Ic for a 10 V change at fixed VBE). Limits single-stage gain, current-source/mirror output resistance | eq 2.14, 2.15; eta = 1/(VA + VCE) | VA, dVCE | current sources, mirrors, high-gain stages | calc | p.92-93 §2.3.2D, fn30-31; p.127 Review J | high |
| AOE-1119 | components | Emitter-follower gain Gv = R_L/(r_e + R_L) (e.g., 1 mA, 1k load -> 0.976); output impedance = r_e + R_s/(beta + 1) (R_s = 1k, Ic = 1 mA, beta = 100 -> 35 ohm). Above f_T/beta the follower's output impedance rises with frequency (looks inductive) - a capacitive load can ring or oscillate | Gv = R_L*gm/(1 + R_L*gm) | r_e, R_L, R_s | followers driving cables/capacitive loads | calc | p.93 §2.3.3, fn33 | high |
| AOE-1120 | components | Avoid the grounded-emitter (R_E = 0) amplifier except inside overall negative feedback: gain -R_C/r_e = -Ic*R_C/VT (-400 at 1 mA with 10k) varies with instantaneous Ic (distortion), Z_in = beta*r_e = 25*beta/Ic(mA) ohm is low and nonlinear, and bias is thermally unstable | Gv = -V_drop/VT | Ic, R_C | amplifier topology review | review | p.93-96 §2.3.4A | high |
| AOE-1121 | components | Grounded-emitter distortion estimate: peak fractional gain change dG/G ~ dVout/V_drop (V_drop = quiescent drop across R_C); waveform distortion ~1/3 of that. With external emitter resistor it is reduced by VT/(VT + Ie*R_E). Measured (+10 V, V_drop = 5 V): 0.7 % at 0.1 V and 6.6 % at 1 V output amplitude; with R_E dropping 0.25 V (10x predicted reduction): 0.08 % and 0.74 % | dG/G = (dVout/V_drop)*VT/(VT + Ie*R_E) | V_drop, swing, Ie*R_E | CE stage linearity | calc | p.94-95 §2.3.4A.1 | high |
| AOE-1122 | thermal | A base-voltage-biased grounded-emitter stage biased with collector at half supply saturates for an 8 C temperature rise (Ic x10 per 30 C). A 60 mV VBE uncertainty between transistor batches gives a 10x Ic error. Never bias by applying a computed VBE | dT_sat ~ 8 C | bias method | bias review | calc | p.96 §2.3.4A.3, Ex.2.13; p.129 Review Q | high |
| AOE-1123 | components | Stable CE biasing: make the dc emitter voltage large compared with VBE drift - use (bypassed) emitter resistance ~0.1*R_C ("one-tenth of the collector resistance is a good guideline"); base divider impedance ~1/10 of dc impedance looking into base. Gain-of-50 counter-example: V_E = 0.175 V -> a 20 C rise raises Ic ~25 % | R_E,dc ~ 0.1*R_C; V_E >> 2.1 mV/C * dT | R_C, dT | CE amplifier biasing | calc | p.96-97 §2.3.5A, Figs 2.48-2.50 | high |
| AOE-1124 | decoupling | Emitter bypass capacitor: its impedance at the lowest signal frequency must be small compared with r_e (+ any unbypassed emitter resistance), not R_E (e.g., 25 ohm at 650 Hz in the example); signal and dc paths may be split (Fig 2.51) so gain can be changed without changing bias | 1/(2*pi*f_min*C_E) << r_e + R_E,unbypassed | f_min, r_e | CE amplifiers | calc | p.96-97 Figs 2.48-2.51 | high |
| AOE-1125 | components | Matched-transistor biasing (monolithic dual) or dc feedback stabilizes a high-gain CE stage. Collector-to-base 10:1 divider feedback puts V_C ~ 11*VBE ~ 7 V but drifts ~1 V with ambient and lowers input impedance by the stage gain (to ~200 ohm in the example). Cascaded RC sections in bias/bootstrap networks can cause peaking or instability unless RC products differ | V_C = VBE*(1 + R1/R2) | divider, gain | CE bias with feedback | calc | p.97-98 Figs 2.52-2.54, fn39 | high |
| AOE-1126 | components | Grounded-emitter stage biased at 0.5*Vcc has small-signal gain G = 20*Vcc (Vcc in volts) independent of quiescent current (-400 at 20 V). A differential amplifier's maximum differential gain (R_E = 0) is 20 x the voltage (V) across its collector resistor; its maximum CMRR (R_E = 0) is 20 x the voltage across the tail resistor | G = 20*Vcc; G_diff,max = 20*V_RC; CMRR_max = 20*V_Rtail | Vcc, V_RC, V_tail | gain budgeting | calc | p.98, p.103; p.128-129 Review Q | high |
| AOE-1127 | components | Active (current-source or current-mirror) collector loads give single-stage gains of 1000-5000+ (limited by Early effect) but only into a very high-impedance load (follower, FET, op-amp) and only inside an overall dc feedback loop or as a comparator | G up to ~VA/VT | load impedance | high-gain stages | review | p.98-99; p.105 §2.3.8C | high |
| AOE-1128 | rf | Tuned (LC) collector load: high gain at resonance, low impedance at dc, rejects out-of-band signals and distortion; output swing can reach 2*Vcc pp; transformer coupling possible (example: 100 kHz, 1.0 mH, 6.2k across LC for Q = 10) | Q = R_p/X at f0 | L, C, R_p | narrowband RF amplifiers | calc | p.99 Ex.2.16 | high |
| AOE-1129 | components | Current mirror (Widlar): compliance to within a few tenths of a volt of the rail; program with a resistor, e.g., (15 V - 0.6 V)/14.4k = 1 mA. Requires matched (monolithic) transistors - 1 mV VBE mismatch = 4 % current error (matched pairs like DMMT3904/3906 matched to 1 mV). Early effect makes output vary ~25 % over the compliance range; base currents give ~2 % error at beta = 100 | I_out = I_P*(1 +/- 4 %/mV mismatch) | V_out range, matching | current mirrors | calc | p.101-102 §2.3.7, fn42; p.128 Review P | high |
| AOE-1130 | components | Improve mirrors with emitter degeneration resistors dropping at least a few tenths of a volt (ineffective over a wide programming-current range), or a Wilson mirror (cascode fixes Q1 VCE; equal-beta Q3 cancels base-current error); with R_E, choose Ic*R_E ~ 100 mV or more to suppress VBE-mismatch error. Unequal R_E ratio gives a ratio mirror (correct for dVBE = VT*ln(ratio)) | Ic*R_E >= 100 mV | R_E, Ic | precision mirrors | calc | p.101-102 Figs 2.60-2.62 | high |
| AOE-1131 | components | Differential (long-tailed pair) amplifier: G_diff = R_C/(2*(r_e + R_E)) (single-ended output); G_CM = -R_C/(2*R_tail + R_E); CMRR ~ R_tail/(r_e + R_E). Differential gains of a few hundred are possible; R_E typically <= 100 ohm or omitted. Example (100 uA per side, R_E = 1.0k): G_diff = 10, input impedance ~250k (drops to ~50k with R_E removed, gain 50) | formulas | R_C, R_E, R_tail, Ic | diff amps | calc | p.103 §2.3.8, Fig 2.64 | high |
| AOE-1132 | components | Replace the diff-amp tail resistor with a current source: CMRR ~100,000:1 (100 dB) at dc with an LM394 matched pair; common-mode input range limited below by the current source's compliance and above by the collectors' quiescent voltage (-3.5 V to +3 V in the example). A tail reference equal to the bandgap (~1.23 V) makes the tail current PTAT and cancels the gain's temperature dependence | CMRR = 100 dB (example) | tail design | precision diff amps | calc | p.104 §2.3.8A, Fig 2.65 | high |
| AOE-1133 | protection | Differential pairs without inter-emitter resistors are destroyed by differential inputs above ~6 V (B-E reverse breakdown); an inter-emitter resistor limits the current but beta/noise may still degrade and input impedance collapses during reverse conduction; clamp the inputs | V_diff,max < ~6 V (unless clamped) | input range | diff-amp and op-amp inputs | calc | p.104 §2.3.8A | high |
| AOE-1134 | components | A differential pair makes a good single-ended dc amplifier (ground one input): VBE temperature drift cancels; accuracy is limited only by VBE and tempco mismatch - e.g., MAT12 monolithic pair drift 0.15 uV/C typical. The grounded-inverting-input connection also avoids Miller effect at the driven input | drift = mismatch only | pair matching | dc amplifiers | review | p.104-105 §2.3.8B, Fig 2.66 | high |
| AOE-1135 | thermal | Datasheet "Pdiss max" (with case at 25 C) = (150 C - 25 C)/R_thJC is specsmanship. Real allowable dissipation: P = (Tj[your-max] - T_amb)/(R_thJC + R_thCS + R_thSA), which is much lower, especially if you are careful with Tj max (e.g., 100 C) | P_real = (Tj_max_design - T_amb)/(theta_JC + theta_CS + theta_SA) | Tj_max (design), T_amb, thetas | every power semiconductor | calc | p.106 Table 2.2 notes (c),(h) | high |
| AOE-1136 | power | Class-A single-ended follower output needs quiescent current >= peak load current: a 10 W / 8 ohm amplifier on +/-15 V dissipates 55 W in the transistor and 110 W in the emitter resistor (165 W quiescent). Use push-pull (class-B/AB) instead; a class-B push-pull stage dissipates < 10 W per transistor at 10 W output | I_q >= I_L,peak | P_out, R_L, supplies | power output stages | calc | p.106-107 Figs 2.68-2.69 | high |
| AOE-1137 | power | Push-pull crossover distortion: bias the output pair into slight conduction with diodes (class-AB). Base bias resistors must supply peak base current: +/-20 V, 8 ohm, 10 W -> peak base 13.5 V, peak load 1.6 A, beta 50 (power transistors have lower beta) -> 32 mA -> ~220 ohm | R_bias = (Vcc - V_B,peak)/(I_L,peak/beta_min) | supplies, P_out, R_L, beta_min | push-pull stages | calc | p.107 §2.4.1A, Fig 2.71 | high |
| AOE-1138 | thermal | Class-AB thermal stability: add small emitter resistors (a few ohms or less) carrying a few tenths of a volt at quiescent current, and thermally couple the bias diodes (preferably diode-connected transistors or a VBE multiplier) to the output devices/heatsink. With ~1 diode drop across the emitter resistors a 30 C rise (-63 mV VBE) raises quiescent current ~50 %; with no emitter resistors it rises x10 (1000 %) - thermal runaway risk. Typical quiescent current ~100 mA for an audio power amplifier | dIq/Iq ~ 63 mV/V(R_E) per 30 C | V across R_E, coupling | class-AB output stages | calc | p.108 §2.4.1B, Fig 2.72 | high |
| AOE-1139 | power | Class-D (switching) amplifiers: switch at >= 10x the highest signal frequency and remove the carrier with an LC lowpass; very efficient and no thermal runaway, but beware HF noise emission, switching feedthrough and limited linearity (example TPA3123: 250 kHz, 20 W per channel) | f_sw >= 10*f_signal,max | f_signal | audio/power amplifiers | review | p.109 §2.4.1C, Fig 2.73 | high |
| AOE-1140 | components | Darlington: beta = beta1*beta2; VBE = 2 x normal; VCE(sat) >= one diode drop; slow turn-off. Put a resistor across the output transistor's B-E: leakage*R < a diode drop and R must not steal much base current; typically a few hundred ohms (power) or a few kohm (small-signal). Examples: MJH6284 beta 1000 typ at 10 A; TIP142 beta 4000 typ at 5 A; MPSA14 beta >= 10,000 at 10 mA, 20,000 at 100 mA, 30 V, no internal resistor | beta = b1*b2; I_leak*R_BE < 0.6 V | leakage, drive | Darlington use | calc | p.109-110 §2.4.2, Figs 2.74-2.76 | high |
| AOE-1141 | components | Sziklai (complementary Darlington) is generally preferred over Darlington for linear stages: single VBE drop, stabilized by output-transistor base resistor R_B. If R_B current (at VBE) = 25 % of the output base current at peak, the driver current ranges only 5:1, so its VBE varies only VT*ln5 = 40 mV over full output swing. Also cannot saturate below a diode drop | V_BE variation = VT*ln(I_max/I_min) | R_B sizing | push-pull output stages | calc | p.110-111 §2.4.2A, Figs 2.77-2.78 | high |
| AOE-1142 | components | Superbeta and matched pairs: 2N5962 minimum beta 450 from 10 uA to 10 mA; LM394/MAT-01 npn pairs with VBE matched to a fraction of a mV (50 uV best grades) and beta matched ~1 %; MAT-03 pnp pair; superbeta-input op-amps (LT1008, LT1012) reach ~50 pA bias current | as stated | matching need | low-level/matched amplifiers | review | p.111 §2.4.2B | high |
| AOE-1143 | components | Bootstrapping a follower's bias network (bias divider fed through series R3 whose lower end is driven by the emitter via C2): effective R3 at signal frequencies = R3/(1 - A) = R3*(1 + R_L/r_e), typically ~100x, so input impedance becomes dominated by the base impedance. Bootstrapping a collector load (driving a follower) makes an approximate current-source load: higher gain and full base drive at the top of the swing | R_eff = R3/(1 - A) | follower gain A | high-Zin biasing, driver stages | calc | p.111-112 §2.4.3, Fig 2.80 | high |
| AOE-1144 | thermal | Paralleled BJTs need emitter-ballast resistors: VBE of "identical" parts spreads (17 mV over 100 adjacent reel parts measured; assume ~100 mV worst case incl. replacements) and 60 mV = 10x current; hot devices hog current (+8.4 %/C). Choose ballast drop 300-500 mV (at least a few tenths V) at the high end of the operating current; or use active ballasting (sense transistors) or MOSFETs | V(R_E) at I_max = 0.3-0.5 V | I_max per device | paralleled power BJTs | calc | p.112-113 §2.4.4, Figs 2.81-2.82 | high |
| AOE-1145 | components | Junction capacitances matter: at 100 MHz a typical 5 pF junction is only 320 ohm. Output pole f = 1/(2*pi*R_L*C_L); input pole with source R_s and C_be; f_T is where beta falls to 1 (base current robbed by C_be). Speed up by lowering source impedances and load capacitances and raising drive currents | f = 1/(2*pi*R*C) | R_L, C_L, R_s, C_in | HF/switching design | calc | p.113-114 §2.4.5A | high |
| AOE-1146 | components | Miller effect: collector-base feedback capacitance appears at the input as C_cb*(Gv + 1); a typical 4 pF can look like several hundred pF to ground. Cures: drive from a low source impedance (emitter follower), differential pair with no collector resistor on the input side, cascode (fixed-bias upper transistor a few volts above the lower emitter), or grounded-base stage | C_in,eff = C_cb*(1 + Gv) | Gv, C_cb, R_s | wideband amplifiers | calc | p.114 §2.4.5B, Fig 2.84 | high |
| AOE-1147 | control-loop | Negative feedback: closed-loop gain G = A/(1 + A*B); A = open-loop gain, A*B = loop gain, 1 + A*B = desensitivity. Gain variations are reduced by 1 + A*B: dG/G = (1/(1 + AB))*dA/A. Example: A from 1000 to 10,000 with B = 0.1 -> G 9.90 to 9.99 (+/-10 dB open loop -> +/-0.04 dB). Nonlinearities are reduced the same way. Require AB >> 1 (open-loop gain >> closed-loop gain) | eq 2.16, 2.17 | A, B | any feedback amplifier | calc | p.117-118 §2.5.2-2.5.3A | high |
| AOE-1148 | control-loop | Feedback and impedances: series (voltage-subtracting) feedback multiplies input impedance by (1 + AB) (100k native, A = 1e4, 99:1 divider -> ~10 Mohm, gain 99); shunt (current) feedback gives Z_in = R_i parallel R_f/(1 + A). Sampling output voltage divides output impedance by (1 + AB); sampling output current multiplies it by (1 + AB); general case: Blackman Z_out = R_o*(1 + (AB)_sc)/(1 + (AB)_oc). Inverting amp gain = -A*(1 - B)/(1 + A*B) -> -R2/R1 | formulas | A, B, R_i, R_o | feedback amplifier design | calc | p.118-120 §2.5.3B-D | high |
| AOE-1149 | control-loop | Include feedback-network loading in the open-loop gain A (both output loading and input-network effect); the formulas assume a unidirectional beta network | A_eff = A with network attached | network impedances | feedback analysis | calc | p.120 §2.5.4A | high |
| AOE-1150 | control-loop | Stability criterion: oscillation occurs if the loop phase shift reaches 180 deg at the frequency where loop gain AB = 1; feedback-network lag makes it worse. A 90 deg open-loop lag is benign: A = -100j, B = 0.1 gives abs(G) = 9.95 with ~6 deg lag (0.5 % gain error vs 9 % for a real A = 100). Op-amps have ~90 deg lag from ~10 Hz to ~1 MHz or more | phase(AB) > -180 deg where abs(AB) = 1 | loop gain/phase | all feedback loops | sim | p.120-121 §2.5.4B | high |
| AOE-1151 | control-loop | Small-signal closed-loop output impedance does not mean large-signal drive: in the Fig 2.91 feedback amplifier Z_out = 0.3 ohm (loop gain 70) yet the 5 ohm emitter resistors limit a 4 ohm load to ~10 Vpp | V_out,max set by large-signal limits | R_E, load | feedback power stages | calc | p.122 §2.5.5B | high |
| AOE-1152 | components | With BJT input stages (bias currents ~uA, e.g., 4 uA -> 0.4 V across 100k), make the dc resistances seen by both inputs equal; consider Darlington/superbeta inputs | R_dc(+in) = R_dc(-in) | I_B, R_bias | discrete/op-amp inputs | calc | p.122 §2.5.5A | high |
| AOE-1153 | power | Feedback regulator design checks: bias the reference zener from the regulated output (constant current) but verify the circuit starts up; a compensation capacitor is usually needed to prevent oscillation, particularly if the output is capacitively bypassed (as it should be) | start-up verified; loop stable with C_out | topology | discrete regulators | sim | p.123 §2.6.1, Fig 2.93 | high |
| AOE-1154 | protection | Add a current-sense resistor + protection transistor that steals base drive when output current exceeds the limit (example: ~6 A for a 50 W heater driver); add a little positive feedback so an on/off heater snaps cleanly (Schmitt action) | I_limit = 0.6 V/R_sense | I_limit | power drivers, heaters | calc | p.123 §2.6.2, Fig 2.94 | high |
| AOE-1155 | components | FET drain-current model: linear region ID = 2*k*[(VGS - Vth)*VDS - VDS^2/2]; saturation ID = k*(VGS - Vth)^2 with VDS(sat) ~ VGS - Vth. Linear-region resistance is inversely proportional to gate drive; saturation current is proportional to gate drive squared. Vth is found by extrapolating a sqrt(ID) vs VGS plot (not the datasheet VGS(th)) | eq 3.1, 3.2 | k, Vth, VGS, VDS | FET biasing/switch analysis | calc | p.137-138 §3.1.4, Fig 3.13-3.14 | high |
| AOE-1156 | components | Datasheet VGS(th) (MOSFET) is specified at a tiny drain current (typically 0.25 mA) and ranges 0.5-5 V; JFET VGS(off)/Vp typically -1 to -5 V (defined at ~10 nA). It takes considerably more gate voltage than VGS(th) to turn a MOSFET fully on - check RDS(on) at your actual VGS (IRF7470: VGS(th) = 2 V max at 0.25 mA, but RDS(on) = 30 mohm max only at VGS = 2.8 V). For low-voltage logic use parts with RDS(on) specified at logic levels (e.g., FDS6574A 9 mohm max at 1.8 V) | require RDS(on) spec at VGS <= V_drive,min | VGS drive, datasheet points | MOSFET switch selection | review | p.136-137 §3.1.3; p.193-194 §3.5.3 | high |
| AOE-1157 | components | FET manufacturing spread (typical): IDSS/ID(on) 1 mA-500 A, spread x5; RDS(on) 0.001 ohm-10k, x5; gm at 1 mA 500-3000 uS, x5; JFET Vp 0.5-10 V, spread 5 V; MOSFET VGS(th) 0.5-5 V, spread 2 V; BVDS(off) 6-1000 V; BVGS(off) 6-125 V. Compare BJT VBE spread 0.63-0.83 V (2N7000 VGS(th) spec 0.8-3 V at 1 mA) | see Table 2.9 | device type | FET bias design | review | p.139 §3.1.5 table | high |
| AOE-1158 | components | FET VGS matching is poor: off-the-shelf BJTs spread ~25 mV in VBE; MOSFET datasheet spreads 1-2 V (within one batch typically several hundred mV, best ~50 mV); JFET 2N5457-59 VGS at 1 mA spreads ~1 V within a type (BJT 10-20 mV). Measure actual parts if matching matters; use monolithic matched pairs. Best matched JFET pair 0.5 mV / 5 uV/C max vs BJT 25 uV / 0.3 uV/C | spread figures as stated | matching need | FET diff pairs, paralleling | measure | p.139-140 §3.1.5A, Fig 3.17, fn14-15 | high |
| AOE-1159 | components | Op-amp input current by technology (typical): JFET LF411/412 50 pA; CMOS TLC272 1 pA; LMC6042 2 fA; bipolar LM324 45 nA; superbeta/bias-cancelled BJT ~25 pA. FET input current is leakage that doubles every 10 C (rises exponentially); BJT bias current is flat or falls slightly with temperature - FET-input parts can exceed BJT parts at elevated temperature | I_leak(T) = I_leak(25C)*2^((T-25)/10) | T_max, source impedance | op-amp selection for high-Z sources | calc | p.140 fn16; p.163 §3.2.8A, Fig 3.48 | high |
| AOE-1160 | thermal | FET scale factor k ~ T^-3/2 and Vth tempco 2-5 mV/C: at high currents ID has a negative tempco (self-ballasting), at small currents a positive tempco, with a zero-tempco current in between (used in FET op-amps). Vertical power MOSFETs in linear service run in the positive-tempco region | sign(dID/dT) depends on ID vs I_ZTC | ID, device | paralleling, bias stability | review | p.138 §3.1.4, Fig 3.14 | high |
| AOE-1161 | esd | MOSFET gates are insulated by oxide < a wavelength thick: typical power MOSFET VGS max +/-20 V (+/-20 to +/-30 V), less for small IC MOSFETs; a single gate breakdown is irreversible; MOSFETs can be destroyed "literally by touching" (ESD) | V_GS <= VGS_max always (incl. transients) | gate drive, transients | every MOSFET gate | inspect | p.134 §3.1.2B; p.221 Review T | high |
| AOE-1162 | components | A MOSFET gate holds its last voltage on its capacitance (gate current << 1 pA): a floating gate can stay on, off, or half-on for hours. Never leave a gate undriven - add a gate-source pull-down (100k-1M) especially when the gate is driven from another board (also guarantees OFF when disconnected/unpowered) | R_GS = 100k-1M on off-board-driven gates | gate source | MOSFET switches | inspect | p.132 fn2; p.199-200 §3.5.4G | high |
| AOE-1163 | components | p-channel FETs have poorer performance than n-channel (lower hole mobility): higher threshold, higher Ron, lower saturation current; a "complementary" p part is built larger, so it has more capacitance and gate charge and costs more (FQP9P25 vs FQP9N25: Ron 0.62 vs 0.42 ohm, Crss 27 vs 15 pF, Ciss 910 vs 540 pF, Qg 29 vs 15.5 nC, $0.97 vs $0.74) but slightly better R_thJC (1.04 vs 1.39 C/W) | compare datasheets | polarity | switch topology choice | review | p.134 fn5-6; p.202 §3.5.5 | high |
| AOE-1164 | components | FET as analog switch: the effective source is whichever terminal is farther from the active drain supply; to guarantee OFF, drive an n-channel gate more negative than the most negative signal (by >= abs(VGS(off)) for JFETs); to guarantee low Ron, drive the gate several volts more positive than the most positive signal | V_G,off < V_sig,min - margin; V_G,on > V_sig,max + several V | signal range | FET signal switches | calc | p.133, 136 §3.1.3; p.220 Review N | high |
| AOE-1165 | components | JFET gate is a diode: an n-channel JFET gate conducts at about +0.5-0.6 V forward relative to the channel; operate it reverse biased (JFETs are always depletion mode) | V_GS < +0.5 V (n-ch) | V_GS | JFET circuits | calc | p.134-135 §3.1.2B | high |
| AOE-1166 | components | JFET families graded by IDSS still spread 5:1 or more; switching JFETs may specify only IDSS(min) (J110: >= 10 mA; a sample measured 122 mA). JFET gm varies ~10:1 between types at the same current; small-signal FETs typically ~10 mS at a few mA vs BJT 40 mS at 1 mA (200 mS at 5 mA). Within one family, gm at a given ID is predictable to ~+/-20 % even when VGS varies widely | design for worst-case IDSS, gm | IDSS, gm range | JFET amplifiers, sources | review | p.141-142 §3.2.1; p.147 fn27; p.169 §3.3.3A | high |
| AOE-1167 | components | FET transconductance: gm = 2*k*(VGS - Vth) = 2*sqrt(k*ID) in the quadratic region, so gm/gm0 = sqrt(ID/ID0); in the subthreshold region ID = I0*exp(VGS/(n*VT)) with n ~1.05-3 (JFETs ~BJT-like) so gm = ID/(n*VT). From datasheet limits you can bound gm at your ID by sqrt scaling from gm(at IDSS) | eq 3.5, 3.6, 3.12 | ID, IDSS, gm(IDSS) | FET gain estimation | calc | p.147 §3.2.3A; p.166-168 §3.3.1C, 3.3.3 | high |
| AOE-1168 | components | Common-source amplifier gain G = gm*R_D (RD in parallel with r_o = 1/gos: G = gm*RD/(1 + gos*RD)); with unbypassed source resistor G = -R_D/(R_S + 1/gm). Size R_D so the drain stays >= 1-2 V (2.5 V in the example) above the source at the maximum specified IDSS. Example BF862 (gm 45 mS at IDSS 10-25 mA): G ~ 13; at 2 mA (gm ~20 mS, R_S = 200 ohm) G ~ -8 | eq 3.3, 3.13 | gm, RD, RS, gos | JFET/MOSFET amplifiers | calc | p.148 §3.2.3B, Fig 3.29; p.167 §3.3.2A | high |
| AOE-1169 | components | JFET self-biased current source/sink: I = abs(VGS)/R for I < IDSS; predictability is poor (2:1 range typical even with a source resistor); a JFET source varies ~5 % over 5-20 V drain range at IDSS (~2 % with source R); even trimmed, ~5 % over temperature and load; op-amp/transistor current sources hold better than 0.5 %. Prefer BJT current sinks (Fig 3.26) or pre-sorted parts for predictable current | I = -VGS/RS | IDSS spread, RS | JFET current sources | calc | p.143-146 §3.2.2 | high |
| AOE-1170 | components | Current-regulator diodes (JFET with gate tied to source, e.g., 1N5283-1N5314): 0.22-4.7 mA, +/-10 % tolerance, tempco +/-0.4 %/C, minimum voltage 1-2.5 V, maximum 100 V, regulation 5 % typ, impedance ~1 Mohm (1 mA part); a 1N5294 (0.75 mA) held current to ~145 V breakdown and reached full current at < 1.5 V | as stated | I, V range | two-terminal current sources | review | p.142-143 §3.2.2, Fig 3.22 | high |
| AOE-1171 | thermal | Worked dissipation check (JFET pull-down for a +/-12 V follower, +/-10 V into 2k): a resistive pull-down would need R_E < 400 ohm (365 ohm) and ~33 mA quiescent (~400 mW each in transistor and resistor) plus poor linearity; a 2N5486 at IDSS = 20 mA would dissipate 440 mW (too much for TO-92/SOT-23 without heatsink); with R_S = 140 ohm the sink ranges 5.7-9.5 mA, worst-case 220 mW each - within a TO-92's 350 mW at 25 C ambient | P = I*V_max per device <= package rating (TO-92 350 mW @ 25 C) | I range, V swing | small-transistor dissipation | calc | p.144-145 §3.2.2B, Fig 3.24-3.25 | high |
| AOE-1172 | components | JFET cascode (upper JFET with larger IDSS, gate tied to lower source) clamps the current-source/amplifier VDS: raises output impedance (kills gos/"Early" effect), kills Miller effect, and keeps VDS low to avoid impact-ionization gate current; highly recommended even when bandwidth is not an issue | cascode present when VDS > ~5 V or high Zout needed | topology | JFET sources, amplifiers, followers | review | p.145-146 Fig 3.27; p.148 §3.2.3C; p.153 | high |
| AOE-1173 | components | LM334 programmable current source: I ~ 0.067 V/R_set, operates down to ~1 V drop, effective capacitance ~10 pF, ~$0.50 - a predictable source-pulldown for JFET stages independent of VGS | I = 0.067/R_set | R_set | bias current sources | calc | p.149 Fig 3.30B, fn35 | high |
| AOE-1174 | components | Hybrid JFET + op-amp amplifier: keep the feedback bottom resistor R_g < 1/gm (so open-loop gain is not reduced) and small enough that its Johnson noise is insignificant vs the JFET's e_n (< ~25 ohm for ~1 nV/rtHz): ~10 ohm chosen; loop gain ~50 (G_OL ~2500, G_CL = 50). A small compensation capacitor removes peaking (5 dB at 16 MHz uncompensated -> 0.1 dB); 10-20 pF input shunt tames peaking for ~1k sources | R_g < 1/gm; e_n,Rg << e_n,JFET | gm, e_n | low-noise wideband amplifiers | calc | p.151-152 §3.2.3E, Figs 3.34-3.35 | high |
| AOE-1175 | components | Monolithic JFET pairs "tightly matched" on JFET scale still mismatch up to +/-20 mV (LSK389: ~100x a good BJT pair); with gain 50 that is 1 V output offset - provide an offset trim with range for the worst case | V_os,out = G*dVGS,max | G, pair spec | dc-coupled JFET diff stages | calc | p.154 §3.2.4A | high |
| AOE-1176 | components | Put a ~50 ohm resistor in series with an op-amp output that drives cables/capacitive loads: ensures stability into capacitive loads and back-terminates 50 ohm coax | R_series = 50 ohm | load | op-amp outputs to cables | inspect | p.154 §3.2.4A | high |
| AOE-1177 | components | FET source follower: gain G = gm*R_L/(1 + gm*R_L) (with gos: G = 1/(1 + 1/(gm*RL) + 1/Gmax)); output impedance = 1/gm (few hundred ohm at a few mA; e.g., gm 1.9 mS -> 525 ohm, 345 ohm with 1k load vs BJT 16 ohm at 1.6 mA; gain only 0.66 into 1k). Need gm*RL and Gmax both > 100 for < 1 % gain error; else use current-sink load, cascode, or BJT gm-enhancer | eq 3.7, 3.8, 3.14 | gm, RL, Gmax | FET buffers | calc | p.157-158 §3.2.6C-E; p.167 §3.3.2B | high |
| AOE-1178 | components | FET source followers have unpredictable dc offset (VGS). For zero offset use a monolithic matched pair with the second JFET as current sink (equal source resistors), plus cascodes to hold VDS constant; a gos ~100 uS pair with 10 V VDS mismatch gives ~60 mV offset (dV = dVDS/Gmax). Measured distortion (LSK389 followers, 1-5 V rms): resistor pull-down 0.02-0.14 % (0.25 V offset); matched current-sink 20 dB lower (~10 mV offset); + cascode another 20 dB | offset ~ dVGS + dVDS/Gmax | pair matching, VDS | precision JFET buffers | calc | p.158-161 Figs 3.43-3.45, fn49 | high |
| AOE-1179 | protection | Protect JFET/MOSFET gates against reverse breakdown with a series resistor and low-leakage clamp diode (e.g., 1N3595, or a BJT B-C junction); large series R adds Johnson noise - a depletion-mode MOSFET current limiter avoids this. Depletion MOSFETs (to 1000 V) need gate protection against >+/-20 V both polarities | I_clamp = (V_fault - V_rail)/R_prot | fault V, noise budget | high-Z input buffers | calc | p.160 Fig 3.43F | high |
| AOE-1180 | components | Bootstrap/guard to fight input capacitance: follower bandwidth with high source impedance f3dB ~ 1/(2*pi*R_s*C_in), C_in = C_rss + C_stray + (1 - Gv)*C_iss; bootstrapping the drain cuts C_rss ~5x; drive a cable's inner shield ("guard") from the follower output to cancel cable capacitance | eq as stated | R_s, capacitances | high-impedance sensor inputs | calc | p.157 §3.2.6D; p.160 | high |
| AOE-1181 | components | FET voltage-controlled resistor: r_DS ~ 1/[2*k*(VGS - Vth)] = r0*(VG0 - Vth)/(VG - Vth); r_DS(linear) = 1/gm(saturation). Nonlinearity ~2 % for VDS < 0.1*(VGS - Vth), ~10 % at 0.25*(VGS - Vth); keep the signal across it small (< ~200 mV in AGC). Linearize by adding VDS/2 to the gate with an equal-resistor divider (e.g., 2 x 100k) - enables e.g. 0.0002 % distortion AGC | eq 3.9-3.11 | VGS, Vth, V_sig | AGC, attenuators | calc | p.161-162 §3.2.7, Figs 3.46-3.47 | high |
| AOE-1182 | components | JFET impact-ionization gate current: gate leakage stays near I_GSS until drain-gate voltage reaches ~25 % of BV_GSS, then rises exponentially (proportional to ID, up to uA) - a BF862 follower at 1 mA from a 20 V supply is useless as a high-Z buffer. Datasheet I_GSS is measured at VDS = 0, ID = 0. Cures: low V_DG (low supply or cascode), p-channel JFET, or MOSFET | V_DG < 0.25*BV_GSS (and < ~5 V for lowest leakage) | V_DG, ID | JFET inputs, followers | calc | p.163-164 §3.2.8B, Fig 3.49; p.157 §3.2.6D | high |
| AOE-1183 | components | FET input capacitance dominates at high frequency: 5 pF at 1 MHz is ~30k shunt, so a 100k-source FET amplifier does not look like 1e12 ohm at signal frequencies; use low impedances (50 ohm) or tuned LC to resonate out capacitance | Z = 1/(2*pi*f*C_in) | f, C_in, R_s | high-Z wideband inputs | calc | p.164 §3.2.8C | high |
| AOE-1184 | components | MOSFET gate drive for switching: switching time ~ Q_g/I_gate (or Q_gd/I for the output transition alone). Examples: IRF740 (Qg ~40 nC) from 4000-series CMOS at ~1 mA -> ~40-50 us; ~2 A needed for 25 ns. IRF1405 Qg ~100 nC -> 10 A for 10 ns (Qgd = 62 nC -> 6.2 A). 2N7000 driven through 10k from 5 V -> ~2 us edges (datasheet 10 ns assumes 25 ohm source) | t_sw = Q_g/I_drive | Q_g, Q_gd, I_drive | MOSFET switch timing | calc | p.164-165 Fig 3.50, fn54; p.198 §3.5.4B, fn91 | high |
| AOE-1185 | protection | Dynamic gate currents (C*dV/dt through C_rss) can be forced back into the driving logic output, possibly causing SCR latchup: add a series gate resistor between logic and a power MOSFET gate | R_gate in series (tens of ohm to ~1k by speed need) | driver type | logic-driven power MOSFETs | inspect | p.164-165; p.193 §3.5.3 | high |
| AOE-1186 | components | JFET operating regions: exponential subthreshold (JFETs track exp(VGS/(n*VT)) with n ~1.05 down to pA), quadratic above; JFETs work at 10 pA but with tiny bandwidth (2N5457 f_T ~140 Hz at 10 pA; f_T = gm/(2*pi*C_in)) - current-starved designs are slow | f_T = gm/(2*pi*C_in) | ID, C_in | micropower FET circuits | calc | p.166 §3.3.1C, fn58 | high |
| AOE-1187 | components | Low-frequency noise: MOSFETs are inherently noisy at low frequencies, by as much as 40 dB vs BJTs and JFETs (2N7000 vs 2N3904 and 2N5457) - do not use MOSFETs for low-level audio/LF inputs (power MOSFETs are fine as output stages) | e_n(MOSFET, LF) up to +40 dB | signal level, band | low-level analog front ends | review | p.170-171 §3.3.6, Fig 3.58 | high |
| AOE-1188 | components | JFET capacitances are a few pF (Ciss > Crss; both fall with reverse bias; datasheet curves are for a family, not correlated with IDSS - treat as rough). Power MOSFET capacitances are nonlinear and rise sharply at low VDS; datasheet Crss is usually given at VDS = 25 V - use the capacitance-vs-VDS plots | C(V) from plots | V_DS range | switching/HF analysis | review | p.170 §3.3.5; p.197 Fig 3.100; p.221 Review S | high |
| AOE-1189 | components | nMOS analog switch: R_off > 10,000 Mohm, R_on 20-200 ohm (switch-intended FETs). With gate driven 0/+15 V it passes 0 to ~+10 V; for +/-10 V signals drive the gate -15/+15 V with body at -15 V. Load the switch output with 1k-100k to reduce off-state capacitive feedthrough (compromise with R_on attenuation/nonlinearity), or use an SPDT (series + shunt) configuration | R_load = 1k-100k | signal range, R_on | discrete/IC analog switches | calc | p.171-172 §3.4.1 | high |
| AOE-1190 | components | CMOS analog switches (parallel n + p MOSFETs) pass signals rail to rail; DG211-family parts accept logic-level control (LOW 0 V, HIGH > 2.4 V), handle +/-15 V signals (4000-series only +/-7.5 V), R_on <= 25 ohm in some members; low-voltage parts reach < 1 ohm. R_on rises at low supply voltage, peaking at mid-supply, and can open-circuit near VDD/2 when supply is too low (enhancement FETs need 5-10 V VGS for low R_on) | R_on(V_sig, V_supply) per datasheet | supply, signal range | analog switch selection | review | p.172, 177 §3.4.1A, 3.4.2B, Fig 3.68 | high |
| AOE-1191 | components | JFET analog switches keep R_on constant with signal level (gate follows source); signals within abs(VGS(off)) of the negative gate-drive level turn the switch back on (stay further away); more rugged than CMOS (no fragile protection network) but high charge injection. Drive JFET gates from open-collector comparators powered from +5 V/-18 V to handle +/-12 V signals | V_sig,min > V_gate,off + abs(VGS(off)) + margin | signal range | JFET switches | calc | p.172-173 §3.4.1B, Figs 3.62-3.64 | high |
| AOE-1192 | protection | Never drive CMOS analog switch (or any CMOS IC) inputs more than a diode drop beyond the supply rails: the input clamp network conducts and SCR latchup can be triggered by ~20 mA or more. Apply supplies before signals with drive capability, or put series diodes in the supply lines; or use fault-protected parts (MAX4508: +/-30 V, 300 ohm; AD7510DI: 25 V beyond rails, 75 ohm; MAX4506/07 signal-line protectors: +/-36 V, 50-100 ohm, 20 pF; ADG465) | V_in within [V- - 0.3, V+ + 0.3]; I_inj < ~20 mA | power sequencing, fault V | analog/digital CMOS inputs | inspect | p.174-175 §3.4.2A, Figs 3.66-3.67 | high |
| AOE-1193 | components | Analog-switch ranges: "standard" +/-15 V signals; mid-voltage +/-7.5 V (or 0-15 V); low-voltage +/-3 V (0-6 V). CMOS switches operate to both rails with specified R_on; JFET SW06 does not reach the positive rail | V_sig within switch class range | signal swing | switch selection | review | p.174 §3.4.2A | high |
| AOE-1194 | components | R_on vs charge injection/capacitance tradeoff: switches with very low R_on (0.25 ohm, flatness 0.03 ohm) have large capacitance (up to ~300 pF) and charge injection. For low distortion into moderate loads choose good R_on flatness (DG408/09 flat within ~10 %) and accept higher R_on. Better: place the switch where its R_on doesn't matter (e.g., selecting a divider tap into a high-Z op-amp input) | R_on in series with gain resistor = error term | topology | gain switching, muxes | review | p.177-178 Fig 3.71, 3.84 | high |
| AOE-1195 | components | Analog switch bandwidth: high-voltage switches (R_on 20-200 ohm) with stray/protection capacitance limit to ~10 MHz or less (example 300 ohm with 22 pF out -> 24 MHz); low-voltage parts do better (ADG719: 2.5 ohm, 27 pF, 400 MHz); RF switches (ADG918/919) usable to 2 GHz (-3 dB at 4 GHz); buffered video muxes (AD8174: 270 MHz at G = 1-2, 55 MHz at G = 10) | f3dB = 1/(2*pi*R_on*C_out) | R_on, C | signal-path switches | calc | p.178 §3.4.2C, Fig 3.72 | high |
| AOE-1196 | crosstalk | OFF-switch feedthrough via C_DS rises with frequency and load impedance (1 pF = 5k at 30 MHz -> -40 dB into 50 ohm; much worse into 10k). Cures: cascade two switches (doubles dB attenuation), series-shunt SPDT, or T-switch. Channel-to-channel crosstalk via C_DD/C_SS (~0.5 pF): use low impedances (50 ohm) and don't put more than one critical signal on one chip | feedthrough ~ R_L/X_CDS | C_DS, R_L, f | multiplexed/switched analog paths | calc | p.178-180 §3.4.2D, Figs 3.73-3.77 | high |
| AOE-1197 | components | Break-before-make vs make-before-break: most CMOS SPDT switches are BBM (sources never momentarily connected); gain-selecting feedback networks need MBB (e.g., ADG620 vs BBM ADG619) so the loop never opens. Some parts (4066) may momentarily short the input to ground during transitions | switch type per circuit | topology | feedback gain switching | review | p.179-180 §3.4.2D-E | high |
| AOE-1198 | components | Charge injection: Q = C_gc*dV_gate (C_gc ~5 pF typical); it depends only on the total gate swing, not its rise time (slowing spreads the glitch, same area). 30 pC = 3 mV step on 0.01 uF. Glitch is smallest when the switch is driven from a low-impedance source; well-balanced CMOS switches partly cancel; lower-R_on switches inject more. Place mux switches at the lower-impedance node | dV = Q_inj/C_load | Q_inj, C_hold | S/H, switched filters, muxes | calc | p.180-181 §3.4.2E, Figs 3.78-3.81 | high |
| AOE-1199 | filter | Switched RC filter: switching resistors via a mux gives selectable corners (binary-weighted conductances give n x f_min steps, e.g., 199n Hz with 80k and 10 nF); switching capacitors limits stopband attenuation to R_on/R_series; buffer the high output impedance | f3dB = n*G_min/(2*pi*C) | R, C | programmable filters | calc | p.182 Figs 3.82-3.83, fn76 | high |
| AOE-1200 | components | Sample-and-hold: buffer the hold capacitor with a FET-input follower; the input buffer must supply C*dV/dt to track (peak I = C*2*pi*f*V_pk). Integrated S/H example AD783: settles to 0.01 % in 0.25 us, droop < 0.02 uV/us | I_pk = C_hold*2*pi*f*V_pk | C_hold, f, V | ADC front ends | calc | p.183 §3.4.3C, Ex.3.10 | high |
| AOE-1201 | components | Digital potentiometers: 32-1024 steps (256 most popular), 1-6 channels, serial or up/down control, linear or log taper, ~$1; the internal switch R_on appears in series with the wiper | R_wiper = R_on | resolution, taper | digital trims/volume | review | p.184 §3.4.3E | high |
| AOE-1202 | components | Avoid high-impedance (resistor pull-up) logic outputs: with 10k pull-up the rising edge is ~200 ns (vs 2 ns active pull-down) and the node picks up capacitively coupled noise; use push-pull (CMOS) outputs | t_r ~ 2.2*R_pull*C_stray | R_pull, C | logic/open-drain outputs | calc | p.185 Fig 3.89 | high |
| AOE-1203 | power | CMOS logic is not zero power: dynamic current I = C*V*f charging load/internal capacitance, plus shoot-through ("class-A") current when an input sits between the rails (slow edges) | I_dyn = C*VDD*f | C_load, f, VDD | power budgets | calc | p.186 Figs 3.92-3.93 | high |
| AOE-1204 | thermal | Power MOSFETs: no second breakdown - SOA limited by dissipation (vs BJT +9 %/C current hogging). Big ranges: VDSS 12 V-4.5 kV (n), to 500 V (p); RDS(on) down to ~0.8 mohm; up to 1000 A / 1000 W; Crss up to ~2000 pF, Ciss up to ~20,000 pF. Headline current/power assume 25 C case and Tj to 175 C with RDS(on) quoted at Tj = 25 C - unrealistic for continuous switching | derate: see AOE-1206 | datasheet | power MOSFET selection | review | p.187 §3.5.1B; p.192 §3.5.2 | high |
| AOE-1205 | thermal | Paralleling power MOSFETs: as saturated SWITCHES - yes, directly (positive R_on tempco shares current), but give each its own series gate resistor (a few to a few tens of ohms; ferrite beads help) to prevent oscillation. In LINEAR service - no: they run in the positive-tempco region; add source ballast resistors dropping ~1 V (a volt or two conservatively; a few tenths of a volt only for matched same-batch parts) at operating current, or active ballast (0.1 ohm sense + diff pair, ~100 mV); or use lateral MOSFETs (2SK1058/2SJ162) | V(R_S) = 1-2 V at I_op (linear); R_G = few-tens ohm each (switch) | mode, I_op | parallel MOSFET designs | calc | p.192 §3.5.1B; p.212-213 §3.6.3, Fig 3.117, fn113-115 | high |
| AOE-1206 | derating | Datasheet ID(max) = sqrt(dT_JC/(R_thJC*R_DS(on)@175C)) with T_C = 25 C and dT_JC = 150 C ("manifestly impossible"); may also be package (bond-wire) limited. Use a lower continuous ID/P: e.g., the book's tables use conservative ID at T_C = 70 C; design Tj well below 175 C | ID_design << ID(max,datasheet); use ID at T_C = 70 C | R_thJC, R_DS(on)(T) | power MOSFET current rating | calc | p.199 §3.5.4D; p.188-189 Table 3.4 notes (b),(y),(z); p.221 Review R | high |
| AOE-1207 | thermal | R_DS(on) at temperature: datasheet typ values are at Tj = 25 C; if hot multiply by ~1.5 (Table 3.4a) - 1.5-2x for low-voltage parts, 2.2-3.5x for high-voltage parts. Rule of thumb m = 2 for MOSFETs rated to 100 V, m = 2.5 above (to 1 kV). Junction temperature Tj ~ T_A + I^2*m*R_on(25C)*R_thJA | eq 3.15 | I, R_on(25C), R_thJA, T_A | MOSFET switch thermal check | calc | p.188-189 Table 3.4 note (r); p.216 §3.6.4B | high |
| AOE-1208 | thermal | Thermal runaway in a saturated MOSFET switch: since R_on rises with Tj, plot P = I^2*R_on(Tj) against heatsink removal (Tj - T_A)/R_thJA; if the lines don't intersect the switch runs away. Assume a hotter ambient (racks, weather). Better to cut R_on (bigger/parallel parts) than pile on heatsink: IRF3205 at 50 A dissipates 25-40 W; FDB8832 (2.3 mohm max at 25 C) dissipates 5.8 W typ (9 W max at 150 C) | equilibrium exists where I^2*R_on(Tj) = (Tj - T_A)/R_thJA | I, R_on(T), R_thJA, T_A | power switch heatsinking | calc | p.215-216 §3.6.4B, Fig 3.120 | high |
| AOE-1209 | power | Switching losses: gate drive loss P = Q_g*V_GS*f; drain capacitive loss P = C_oss*V_DS^2*f (as printed) - significant at high switching frequencies. Low gate drive current lengthens transitions, increasing V*I*dt loss and permitting oscillation during the slow transition | P_gate = Qg*VGS*f; P_Coss = Coss*VDS^2*f | Qg, Coss, V, f | switching converters, PWM drivers | calc | p.197-199 §3.5.4A-C; p.189 Table 3.4b notes (s),(s2) | medium |
| AOE-1210 | components | Power MOSFET body diode: body is tied to source, so there is always a drain-source diode - the MOSFET cannot block reverse drain voltage beyond a diode drop (no bipolar analog switching, no bipolar integrator reset). The body diode has reverse-recovery snap-off; add a Schottky across D-S (effective below ~60 V) or choose soft-recovery-diode MOSFETs where inductive current commutates | V_DS(reverse) <= V_F | topology | bridges, synchronous switches | review | p.199 §3.5.4E, fn93 | high |
| AOE-1211 | components | Gate-source breakdown (typically +/-20 V) is far below drain ratings: never drive a MOSFET gate directly from another MOSFET's (or BJT switch's) drain swing on high-voltage rails. For a high-side p-channel switch use an npn current sink into a gate resistor (limits VGS to I*R, works unchanged at 12/24/48 V) or a zener clamp | VGS = I_sink*R_GS <= 20 V | V_supply | high-side pMOS drivers | calc | p.199 §3.5.4F; p.194, 203 Figs 3.96C, 3.106 | high |
| AOE-1212 | esd | MOSFET gate protection: series gate resistor ~1k (if speed allows), especially when the gate signal comes from another board; optional clamp diodes to rails or a zener downstream (adds capacitance). A damaged gate shows substantial dc gate current and may conduct when it should be off | R_series ~ 1k (slow paths) | speed need | MOSFET gates | inspect | p.199 §3.5.4G, fn94-95 | high |
| AOE-1213 | esd | ESD handling: human body model (HBM) = 100 pF + 1.5k (2.5 kV -> 1.7 A peak, 150 ns); machine model up to 6 A; charged-device model 6 A, 2 ns. MOS ICs typically survive 2 kV HBM; external-interface parts (RS-232/422/485 "E" versions) 15 kV. Even 1 kV HBM into a 1100 pF gate -> ~80 V > 20 V rating. Use conductive foam/bags, grounded irons and benches, wrist straps, antistatic floors/clothing, humidity control and ionizers; small-geometry unprotected MOSFETs are most vulnerable | HBM rating >= 2 kV (15 kV for external interfaces) | exposure | handling, interface design | inspect | p.200-201 §3.5.4H, fn97-98 | high |
| AOE-1214 | components | MOSFET vs BJT switches: ON MOSFET is a resistance (drop -> 0 at low current); at 6-10 A, 0-100 V the MOSFET saturates better (IRFZ34E 0.25/0.43 V at 25/125 C vs TIP42A 1.5/1.7 V; IRF540N 0.44/1.0 V vs TIP142 Darlington 3.0/3.8 V) and needs no base current (BJT needs Ib ~ Ic/10, up to ~1 A). Above 300-400 V IGBTs excel (STGP10NC60 1.75/1.65 V at 10 A). Figure of merit for fast switching: capacitance x saturation voltage | compare V_sat at 125 C | I, V class | power switch technology choice | review | p.201-202 §3.5.5 table | high |
| AOE-1215 | power | Always add short-circuit current limiting to power switches feeding supplies/loads (a slipped scope probe; the inrush of an uncharged bypass capacitor). Under a shorted output the pass device dissipates V_in*I_lim - use foldback limiting or a thermally protected switch (PROFET/protected MOSFET) rather than just a big heatsink | P_fault = V_in*I_lim <= SOA | V_in, I_lim | load switches | calc | p.203 §3.5.6A | high |
| AOE-1216 | components | n-channel high-side switches need gate drive ~10 V above the input supply (high-side driver IC with charge pump, e.g., LM9061 with VDS(on) sensing + delay for inrush, or integrated PROFET such as BTS555 up to 165 A); generally preferred to p-channel for better characteristics/variety. MOSFET gate driver ICs (e.g., TC4420: logic threshold < 2.4 V, 4.5-18 V, +/-6 A, ~25 ns) make fast switching easy (~$1) | V_G = V_supply + ~10 V | topology | high-side/power switching | review | p.194 §3.5.3, Fig 3.97; p.203 Fig 3.106E | high |
| AOE-1217 | components | Floating MOSFET switch via photovoltaic optocoupler (~8 V floating from 10 mA LED, only ~20 uA output): switching time t = Q_g/I, e.g., 25 nC/3 uA = 8.3 ms without buffers, ~40 us with a beta~200 BJT push-pull buffer (then limited by the opto's ~100 us on / ~350 us off). Back-to-back n-MOSFETs switch either polarity; unprotected. Gate-drive optocouplers (ACPL-W343: 3 A, 40 ns, 2 kV isolation) need a 15-30 V isolated supply | t = Qg/(beta*I_opto) | Qg, I_opto | isolated switches | calc | p.204-206 §3.5.6B, Fig 3.107 | high |
| AOE-1218 | components | MOSFET switch tradeoff: R_on spans ~100,000:1 over a ~100:1 voltage-rating range (R_on rises roughly as V_rating^2; literature exponents 1.6-2.5, lower end more accurate); higher-current parts have more C_oss, C_iss and gate charge (use R_on*C_oss as figure of merit); very high-voltage parts are expensive (4.5 kV ~$22). A higher-VDSS part may give lower C_oss or more power capability than the minimum-voltage part | R_on ~ V_rating^(1.6..2.5) | V, I, speed | switch selection | review | p.205 §3.5.6B; p.207 §3.5.7A, fn109 | high |
| AOE-1219 | components | Relay drive: coil rated voltage/current (example 5 V, 185 mA = 27 ohm; must-operate 3.75 V, must-release 0.5 V). Overdrive momentarily for faster closure (12 V for ~0.1 s then hold at rated 5 V); a resistor in series with the flyback diode (allowing ~20 V) speeds release. Marginal coil voltage holds contacts with reduced force and shortens relay life | V_coil >= V_must-operate (worst case) | coil spec | relay drivers | calc | p.194-195 Fig 3.98B, fn84; p.207 | high |
| AOE-1220 | hw-fw | Remote/computer-controlled supplies need a hardware DISABLE (manual and external) so outputs stay safe while the controller crashes or boots | disable path independent of MCU | control architecture | programmable sources, actuators | review | p.195 Fig 3.98C | high |
| AOE-1221 | power | Battery on/off control: flip-flop pass-switch circuits should draw zero (leakage only) current when off; debounce the pushbutton (~100 ms charging time constant); 9 V alkaline ~500 mAh, ~9.4 V fresh, ~6 V at end of life (1 V/cell), 5.4 V very old (0.9 V/cell). A 1 uA standby drain corresponds to ~50-year life on 500 mAh | life = C_batt/I_standby | I_standby, C_batt | battery instruments | calc | p.195-196 Fig 3.99, fn85-86 | high |
| AOE-1222 | thermal | Allowable switch current from heatsink capability: I = sqrt(P/R_on) using R_on at operating temperature (e.g., SUP75P05: 8 mohm, ~10 mohm at 75 C, ~1 W at 10 A with 10 V gate drive) | I_max = sqrt(P_allow/R_on(T)) | P_allow, R_on(T) | load switches | calc | p.196 fn87 | high |
| AOE-1223 | components | Push-pull MOSFET drivers (e.g., piezo/transformer drivers): add diodes across the series gate resistors for rapid turn-off to prevent conduction overlap (shoot-through) of the power transistors | turn-off faster than turn-on | gate network | bridge/push-pull drivers | inspect | p.207 Fig 3.109 | high |
| AOE-1224 | components | IGBT: MOSFET input + bipolar output; cannot saturate below ~VBE; no intrinsic reverse diode (reverse rating may be only ~20 V) - use parts with an anti-parallel diode (-D suffix) for inductive loads; ratings to 1200 V/100 A discrete, modules > 1000 A. At 1000 V class an IGBT (IRG4PH50S: 1.2 V at 15 A, 25-150 C) beats a MOSFET (IRFPG50: 1.5 ohm/4 ohm -> 23 V/60 V at 15 A). IGBTs are primarily for > 300 V and < 100 kHz | V_ON,IGBT ~ 1-3 V | V, I, f_sw | high-voltage switching | review | p.207-208 §3.5.7A; p.222 Review Z | high |
| AOE-1225 | protection | IGBT/high-power switch short-circuit protection is mandatory (50 A from 1000 V = 50 kW -> destroyed in ms): desaturation detection - shut off drive if V_CE has not fallen to a few volts ~5 us after turn-on | t_desat ~ 5 us | V_bus, I_load | IGBT/MOSFET bridges | review | p.208 §3.5.7A | high |
| AOE-1226 | components | Thyristors (SCR, triac): triggered by a few mA of gate current, stay on until the anode current falls to zero; ratings 1 A to thousands of A, 50 V to many kV; used in phase-control dimmers | I_gate ~ few mA | load | ac power control | review | p.208 §3.5.7B | high |
| AOE-1227 | components | Capacitive-load linear drive: slewing C at dV/dt needs I = C*dV/dt both ways (10,000 pF at 2 V/us = 20 mA) - a resistor pull-up/pull-down can't sink/source it; use a push-pull (totem-pole) stage and a current-source (depletion MOSFET) load instead of a power resistor | I = C*dV/dt | C_load, slew | piezo, HV amplifiers | calc | p.209 §3.6.1, Fig 3.111 | high |
| AOE-1228 | protection | Robust input protection with depletion-mode MOSFETs: a back-to-back pair in series with the input (plus clamp diodes to the rails) looks like ~1.7k (2 x R_on) normally but limits fault current to ~I_DSS (~2 mA) for inputs to +/-500 V, avoiding the ~100k series resistor (bandwidth/noise penalty) a resistive limiter would need | I_fault = I_DSS | V_fault, I_DSS | instrument inputs exposed to mains | calc | p.210-211 §3.6.2A, Fig 3.112 | high |
| AOE-1229 | protection | Discharge high-voltage storage capacitors promptly when power is removed (bleeder sized for ~10 s). A plain bleeder on 200 uF at 400 V needs ~50k and wastes > 3 W; a depletion-mode MOSFET held off by an auxiliary rail while powered (e.g., DN3545: 450 V, I_DSS >= 200 mA, ~$0.75) discharges only when unpowered. Offline switcher bulk caps sit at 170 V, 340 V or ~400 V (PFC) | tau_bleed ~ 10 s; P_bleeder = V^2/R | C, V | line-powered supplies | calc | p.211 §3.6.2B, Fig 3.113 | high |
| AOE-1230 | power | Extend a low-voltage regulator's input range with a depletion-mode MOSFET follower ahead of it (e.g., IXTP08N50: VGS -2 to -4 V keeps regulator input 2-4 V above output; to 500 V input) plus a current-limit resistor; watch dissipation | P_Q1 = (V_in - V_reg,in)*I | V_in, I | HV-input regulators | calc | p.211-212 Fig 3.114 | high |
| AOE-1231 | thermal | Class-AB push-pull thermal stability: BJT and vertical-MOSFET outputs (positive ID tempco at the operating current) need a tracking bias generator thermally coupled to the heatsink plus small emitter/source resistors; lateral MOSFETs (2SK1058/2SJ162, 160 V, 7 A, R_on ~1 ohm) have negative tempco above ~100 mA and can be biased at fixed VGS near that zero-tempco point (~100 mA) | I_q near zero-TC point | device type | audio power stages | review | p.213-215 §3.6.4A, Figs 3.118-3.119 | high |
| AOE-1232 | components | Second breakdown: BJT SOA is limited by local thermal instability beyond simple P = V*I; MOSFETs do not suffer it. For both, max current and power limits are higher for short pulses - use datasheet SOA and transient thermal impedance curves | operate inside SOA(t_pulse) | V, I, t_pulse | power stages, linear pass devices | review | p.216 §3.6.4C, Fig 3.95 | high |
| AOE-1233 | components | JFET/transistor light switch using a photoresistor divider on a MOSFET gate (10k light -> 10M dark) is imprecise but adequate; add positive feedback (e.g., 10M) for hysteresis so the relay snaps on and is not held with marginal coil voltage; MOSFET dissipates while in its linear region | hysteresis present | sensor divider | slow analog threshold switches | review | p.206-207 Fig 3.108 | high |
| AOE-1234 | components | Op-amp basic gains: inverting G = -R2/R1 with Z_in = R1 (virtual ground); noninverting G = 1 + R2/R1 with Z_in ~ infinite (1e12 ohm JFET, > 1e8 ohm BJT); follower G = 1. Golden rules (output drives inputs to equal voltage; inputs draw no current) hold only while the op-amp is in its active region (not saturated) and feedback is negative | eq 4.1, 4.2 | R1, R2 | op-amp gain stages | calc | p.225-227 §4.2.1-4.2.3 | high |
| AOE-1235 | components | There must always be dc feedback around an op-amp (else it saturates): e.g., a series C between output and inverting input is not allowed, integrators need a reset switch or a parallel feedback resistor; a capacitor in series with the ground leg of a noninverting gain divider (G -> 1 at dc) is allowed | dc path output -> inverting input exists | topology | every op-amp circuit | inspect | p.232 §4.2.7 | high |
| AOE-1236 | components | AC-coupled op-amp inputs need a dc return to ground for input bias current (e.g., resistor to ground at the noninverting input); for ac-only amplifiers roll the gain off to unity at dc (capacitor in series with R1) to cut offset effects - example 17 Hz corner with R1 = 2.0k (large C); or trim offset / raise impedances (T-network) | R_bias to ground; C_R1 >= 1/(2*pi*f_L*R1) | f_L, R1 | ac amplifiers | calc | p.226 Fig 4.7 | high |
| AOE-1237 | components | Prefer the inverting configuration when input impedance allows: it puts less demand on the op-amp (no common-mode swing), gives better performance, and its virtual ground sums several signals without interaction | n/a | source impedance | amplifier topology | review | p.227 §4.2.2 | high |
| AOE-1238 | components | Difference amplifier (4 resistors): gain R2/R1, CMRR set directly by resistor matching (~60 dB with +/-0.1 % resistors); use precision arrays (e.g., BI 664: 0.1 % accuracy, 0.05 % ratio tracking, +/-5 ppm/C; best Vishay: 0.001 % ratio, +/-0.1 ppm/C) or integrated difference amps (INA105A ratio match < 0.01 %, < 5 ppm/C; INA106 G = 10; INA117/AD629 inputs to +/-200 V) | CMRR ~ 60 dB at 0.1 % mismatch | resistor matching | difference amps | calc | p.227 §4.2.4, fn2; p.288 Review D | high |
| AOE-1239 | components | Op-amp current source with floating load: I = Vin/R; compliance Vcc - Vin (normal) and Vin - Vee (reverse). Floating the whole supply to ground the load is tricky: transformer interwinding capacitance injects 60 Hz currents that can exceed uA-level outputs (batteries solve it) | I = Vin/R | V range | op-amp current sources | calc | p.228 §4.2.5; p.232 | high |
| AOE-1240 | components | Op-amp + transistor current source for grounded loads: I = (Vcc - Vin)/R, no VBE error; BJT base current is an error (use Darlington or MOSFET). The op-amp inputs sit near the positive rail at low currents - use an op-amp whose common-mode range includes V+ (datasheet permission; LF411 degraded there) or power it from a higher rail. Power MOSFETs' large capacitance needs a gate R-C network to prevent oscillation | I = (Vcc - Vin)/R | V_CM range | current sources | review | p.228-229 Figs 4.12-4.13 | high |
| AOE-1241 | components | Op-amp current sources degrade with frequency: output impedance ~ R_o*f_T/f (R_o ~100 ohm open-loop), dropping to R_o at f_T; slew-rate limit makes it look like a shunt capacitance C_eff = I_out/S (10 mA with 1 V/us -> 10 nF). Howland sources need exactly matched resistor ratios, are limited by op-amp CMRR and small resistor/compliance, and drop to a few hundred ohms at HF | Z_out(f) = R_o*f_T/f; C_eff = I/S | f_T, S, I | precision/fast current sources | calc | p.228 fn3; p.230 §4.2.5B; p.250, 254 §4.4.4 | high |
| AOE-1242 | components | Op-amp integrator: Vout = -(1/RC)*integral(Vin dt) (R = 1M, C = 0.1 uF: 1 V -> -10 V/s); it has no dc feedback, so bias current and offset make it ramp: add a reset switch (JFET or CMOS) or a feedback resistor R_f (integration stops below f = 1/(2*pi*R_f*C)) | eq 4.3; dVout/dt = -Vin/(R*C) | R, C | integrators, ramp generators | calc | p.230-231 §4.2.6, Fig 4.18 | high |
| AOE-1243 | components | Integrator drift: bias current alone ramps the output at I_B/C; with a voltage input the offset adds an equivalent current V_os/R; choose the op-amp with minimum I_E = I_B + V_os/R (OP27E: 40 nA -> +/-0.4 V/s with 0.1 uF; LMC6041A: 4 pA but 3 mV -> 3 nA at 1M; OP97E: 0.1 nA + 25 uV/1M = 0.125 nA). Larger R reduces the V_os contribution | dVout/dt = (I_B + V_os/R)/C | I_B, V_os, R, C | integrators, charge amps | calc | p.257-259 §4.5.5, Fig 4.65 | high |
| AOE-1244 | components | FET reset-switch leakage can dominate integrator error (SD210: 10 nA max vs LMC6001A op-amp 25 fA and 1e13 ohm capacitor leakage) - use the T-configuration (series switches with the middle node grounded through R when off) so the summing-node switch sees ~0 V; choose Teflon/polystyrene/polypropylene hold capacitors (measured polypropylene time constant > 1e9 s) | I_leak(switch) << I_B | switch leakage | precision integrators, S/H | review | p.259-260 §4.5.6, Fig 4.67, fn34 | high |
| AOE-1245 | decoupling | Op-amp supply bypass capacitors are mandatory (op-amps have gain at RF where rail inductance causes instability); one pair of capacitors can serve nearby op-amps. Multiple bypass caps with wiring inductance resonate (25 nH with 0.01 uF -> 10 MHz, X = 1.6 ohm, impedance peak Q x higher): add a lossy bypass (small electrolytic, ESR ~0.5 ohm or more) to damp | f_res = 1/(2*pi*sqrt(L*C)); damping ESR ~ 0.5 ohm | L_wiring, C | every op-amp board | inspect | p.232 §4.2.7, fn7 | high |
| AOE-1246 | protection | Op-amp differential input limit can be as small as +/-0.5 V (some bipolar) to ~5 V; exceeding it draws large input current and degrades/destroys the part. Max input voltages are also bounded (LF411: +/-15 V, not beyond the negative supply) | V_diff <= spec; V_in within abs-max | input range | op-amp inputs (comparator use!) | inspect | p.232 §4.2.7; p.246 §4.4.1F-G | high |
| AOE-1247 | components | Bootstrapped op-amp follower bias (resistor string with C to output) raises ac input impedance; low-frequency rolloff ~10 Hz at 12 dB/octave below; may peak - tame with 1-10k in series with the bootstrap capacitor. FET-input op-amps usually make bootstrapping unnecessary (10 Mohm+ bias resistors fine) | R_bias(FET) >= 10 Mohm OK | I_B | high-Z ac inputs | review | p.233 Fig 4.21, fn9 | high |
| AOE-1248 | components | Transimpedance (current-to-voltage) amplifier: Vout = -I_in*R_f (1 Mohm -> 1 V/uA), holding a photodiode at virtual ground. Always add a small capacitor across R_f: detector capacitance with R_f adds lagging phase that can cause oscillation/ringing | Vout = -I*R_f; C_f across R_f | C_det, R_f, f_T | photodiode amplifiers | calc | p.233 §4.3.1C, Fig 4.22-4.23 | high |
| AOE-1249 | components | Output power booster inside the loop: take feedback from the booster output (cures push-pull crossover at low frequency); integrated buffers (LT1010, BUF633/4: ~200 mA, 20-100 MHz, protected) are fine inside the loop only if the driving op-amp has significantly less bandwidth - substituting a faster op-amp into a working boosted circuit can make it oscillate. Crossover still degrades at HF (slew, loop gain) - bias the stage class-AB | f_T(buffer) >> f_T(op-amp) | bandwidths | op-amp power stages | review | p.234-235 §4.3.1E, fn10-11 | high |
| AOE-1250 | power | Op-amp linear regulator: use a rail-to-rail-output op-amp so the pass Darlington can run with low headroom (with an LF411 allow another 1.5-2 V); bias the reference from the output only after checking start-up; always include output current limiting; add a compensation capacitor so the loop stays stable when the output is capacitively bypassed. Beware LT1637-type "over-the-top" input bias rising ~100x near the positive rail | headroom = V_CE(sat,pass) + op-amp swing loss | V_in min | discrete regulators | review | p.235-236 §4.3.1F, fn12 | high |
| AOE-1251 | components | Comparators: an op-amp without feedback can be a comparator but dedicated comparator ICs are faster and allow independent output levels; comparators are uncompensated and must not be used as op-amps (with feedback they oscillate); open-collector outputs need a pull-up small enough for full swing including the hysteresis resistor's load | R_pullup accounts for R_hyst load | output type | threshold detectors | review | p.236 §4.3.2A; p.269 §4.6.6 | high |
| AOE-1252 | components | Schmitt trigger design: set threshold with divider R1-R2 (or a single resistor to ground for thresholds near 0 V), then choose feedback R3 so hysteresis = output swing x (R1 parallel R2)/(R1 parallel R2 + R3) (example thresholds 4.76 V and 5.0 V); optional 10-100 pF speed-up capacitor across R3; offset resistor to V- centers thresholds about ground | dV_hyst = V_swing*R_p/(R_p + R3), R_p = R1*R2/(R1 + R2) | swing, R | comparator inputs | calc | p.237 §4.3.2B, Fig 4.32 | high |
| AOE-1253 | protection | Op-amp driving a BJT switch: op-amps on dual rails swing beyond the ~-6 V base-emitter breakdown - add a reverse diode at the base (omit if V- >= -5 V) and a base resistor; use a Darlington above ~1 A, or better an n-MOSFET (no resistor/diode needed). Add a flyback diode for inductive loads | V_BE,rev < 6 V | op-amp swing | power switching from op-amps | inspect | p.238 Fig 4.35 | high |
| AOE-1254 | components | Active rectifiers/clamps/peak detectors are slew-limited: recovering from negative saturation takes ~(V_out - V-)/S (LF411 at 15 V/us on +/-15 V: ~1 us glitch). Improved circuits clamp the op-amp output so it swings only ~2 diode drops (~1.2 V) through zero, cutting the glitch > 10x; choose high slew-rate op-amps | t_recover ~ dV_swing/SR | SR, swing | precision rectifiers, clamps, peak detectors | calc | p.238-239 Figs 4.36-4.38; p.254-257 | high |
| AOE-1255 | timing | Triangle-wave oscillator (integrator + noninverting Schmitt with rail-to-rail output): f = R3/(4*R1*C1*R2), independent of supply; amplitude set by R2/R3 (changing it changes f). The Schmitt must be noninverting or the circuit latches up. Avoid "algebraic circuit design" as a substitute for understanding | eq 4.4 | R1, R2, R3, C1 | function generators | calc | p.239-240 §4.3.3, Fig 4.39 | high |
| AOE-1256 | hw-fw | Ratiometric design: make both the charging current and the comparison threshold proportional to the same supply so timing/frequency cancels supply variation (pulse-width generator with timer threshold 2/3 V+; VCO where f depends only on V_in/V_ref) | output independent of V_supply | topology | timers, sensors, ADC references | review | p.241 §4.3.5; p.267 §4.6.4 | high |
| AOE-1257 | test | JFET pinch-off / MOSFET threshold tester: servo the gate with an op-amp so the source sits at virtual ground with a fixed pull-down current (10M to -10 V = 1 uA); add ~100k series gate resistor for plug-in protection plus a small feedback capacitor for stability; the op-amp input current must be << test current (JFET-input op-amp). VGS(off) test currents vary by maker (1 nA most common, then 1 uA, 10 nA, 0.5 nA) | I_test = V/R_pulldown | test current | component screening/matching | calc | p.240-241 §4.3.4, Fig 4.40 | high |
| AOE-1258 | filter | Sallen-Key 2nd-order lowpass: rolls off -12 dB/octave with a sharper knee than cascaded RC; Butterworth example C1 = 10 nF, C2 = 2 nF, R1 = 12.7k, R2 = 100k (Chebyshev 0.1/0.5 dB variants are peakier). Unity-gain amplifier may be op-amp follower, buffer IC or emitter follower | 2nd order, -40 dB/decade | R, C | anti-alias/smoothing filters | sim | p.241-242 §4.3.6, Fig 4.42, fn17 | high |
| AOE-1259 | components | Input offset voltage: typical ~1 mV (JFET LF411: 0.8 mV typ, 2 mV max, 7 uV/C typ, 20 uV/C max), precision parts ~10 uV (OP177A: 10 uV max, 0.1 uV/C max, 0.2 uV/month), zero-drift/chopper parts <= 5 uV untrimmed. Output error from V_os = (1 + R2/R1)*V_os (noninverting gain, even in an inverting stage): gain-100 inverter with LF411 -> up to +/-0.2 V. Fixes: unity dc gain, trim, lower-V_os op-amp | dVout = (1 + R2/R1)*V_os | V_os, gain | dc amplifiers | calc | p.244 §4.4.1A-B; p.251-252 §4.4.2D | high |
| AOE-1260 | components | Input bias current error: an inverting stage with grounded input produces V_out = I_B*R2 (NE5534 with I_B = 2 uA, R1 = 10k, R2 = 1M -> 1.98 V; LF411 -> 0.2 mV). Fixes: use FET/superbeta/bias-cancelled op-amps (OP177 < 2 nA, LT1012 25 pA, LF411 50 pA, TLC270 1 pA), balance the dc resistance seen by both inputs (e.g., 91k = 100k parallel 1M), keep network resistances small (1k-100k); residual error = G_dc*I_os*R (I_os ~ I_B/2 to I_B/20) | dVout = I_B*R2 (unbalanced); G*I_os*R_s (balanced) | I_B, I_os, R | dc amplifiers | calc | p.244 §4.4.1C-D; p.252 §4.4.2E-F, Fig 4.55 | high |
| AOE-1261 | components | Op-amp bias current ranges: BJT tens of nA (OP27 15 nA), JFET tens of pA (LF411 50 pA typ, 200 pA max, 4 nA at 70 C), MOSFET <= 1 pA; extremes LT1012 25 pA (BJT), OPA129 0.03 pA, LMC6041 0.002 pA; very fast BJT op-amps microamps (THS4011/21 3 uA). With the LF412's 200 pA max you can tolerate ~5 Mohm source/network resistance before a 1 mV error | V_err = I_B*R | I_B, R | op-amp selection | calc | p.244 §4.4.1C | high |
| AOE-1262 | components | Common-mode input range must be respected: LF411 on +/-15 V guarantees +/-11 V; driving it to the negative rail causes phase reversal and output saturation. LM358/LM324 reverse phase for inputs > 400 mV below V- (LT1013/1014 fix it). "Single-supply" parts include V- (typ to -0.3 V); rail-to-rail input parts include both rails but compromise offset, output impedance, supply current | V_CM within spec at all times incl. faults | V_CM | op-amp inputs | inspect | p.245-246 §4.4.1F, fn22; p.265 §4.6.3 | high |
| AOE-1263 | components | Output swing and drive: classic op-amps (LF411) swing to within ~1-2 V of each rail (~2 V into >= 1k); current limit typically ~+/-20-25 mA (I_lim = VBE/R); swing falls for low load R; max output current drops ~25 % at Tj = 125 C. CMOS rail-to-rail outputs (LMC6041) reach within ~1 mV of the rails at 10 uA (output R ~80-100 ohm). Datasheet curves can be wrong - measure | V_out range from datasheet vs I_load | load R, supply | output headroom | calc | p.246-247 §4.4.1H, Figs 4.44-4.46; p.290 Review M | high |
| AOE-1264 | components | Open-loop output impedance ~40 ohm (LF411) to ~100 ohm typical, up to several kohm for low-power/rail-to-rail outputs - these need high loop gain for low closed-loop Z_out. Closed-loop Z_out rises ~linearly with frequency (inductive: L_out ~ r_o*G_CL/(2*pi*f_T)), reaching r_o at loop gain 1 (LT1055: r_o ~60 ohm); with a capacitive load this forms a series resonance | Z_out = r_o/(1 + AB); L_out = r_o*G_CL/(2*pi*f_T) | r_o, f_T, G_CL | driving capacitive loads, current sources | calc | p.246-247 §4.4.1I; p.250 Fig 4.53 | high |
| AOE-1265 | components | Gain/bandwidth: dc open-loop gain 1e5-1e6 (100-120 dB; precision parts to 1e7), falling 6 dB/octave from ~10 Hz (LF411) to unity at f_T (GBW) 0.1-10 MHz typical (LF411: gain 100 at 40 kHz, f_T 4 MHz). Closed-loop bandwidth BW_CL ~ f_T/G_CL; the response is -3 dB (not -6) where abs(A) = 1/B because A ~ j*f_T/f | BW_CL = f_T/G_CL | f_T, G_CL | bandwidth budgeting | calc | p.247 §4.4.1J, Fig 4.47; p.249-250 §4.4.2A; p.290 Review N | high |
| AOE-1266 | components | Don't use a faster op-amp than needed: higher f_T/slew costs supply current, often higher bias current (fast BJT inputs > 1 uA), and makes the circuit more prone to oscillate (e.g., supply current < 1 uA parts have f_T ~10 kHz; LMC6442: 10 uA, f_T 10 kHz, 0.004 V/us) | f_T only as needed | BW need | op-amp selection | review | p.247 §4.4.1J; p.273 §4.7 | high |
| AOE-1267 | components | Slew rate: an undistorted sinewave of amplitude A at frequency f needs SR >= 2*pi*f*A (peak slope at zero crossings); full-power swing App <= SR/(pi*f). LF411: 15 V/us; low-power parts < 1 V/us; fast parts hundreds to 5000 V/us. Slew is specified in unity gain with a full-swing step (large overdrive) - small inputs (~10 mV) slew much slower. In conventional BJT op-amps slew rate is limited by bandwidth: S = 0.32*f_T (as printed, fn25; units not stated) | SR_min = 2*pi*f*A (eq 4.6) | A, f, SR | large-signal/fast circuits | calc | p.248 §4.4.1K, Figs 4.48-4.49; p.251 §4.4.2B, Fig 4.54 | high |
| AOE-1268 | components | Precision layout/thermal: keep op-amp loads above ~10k and avoid large output currents in precision stages - output-stage dissipation creates on-chip thermal gradients that shift input offset | R_load >= 10k (precision) | load | precision amplifiers | review | p.248 §4.4.1L; p.251 §4.4.2C | high |
| AOE-1269 | components | Supply limits: LF411 +/-5 to +/-18 V; many low-voltage CMOS op-amps are limited to 10 V or even 5 V total supply (e.g., MAX951: 2.7-7 V - can't run directly from a 9 V battery). Classes: low-voltage ~6 V max (down to ~2 V); high-voltage 36 V total (min 5-10 V); mid 10-15 V; true HV to hundreds of volts. Quiescent-microamp parts still draw whatever the load takes | V_total within [V_min, V_max] incl. fresh battery | supply | op-amp selection | inspect | p.248-249 §4.4.1M; p.280; p.290 Review M | high |
| AOE-1270 | components | Feedback resistor values with general-purpose op-amps are typically 2k-100k: low enough that bias currents and stray-capacitance phase shifts/pickup are small, high enough not to load the output | R_feedback = 2k-100k | op-amp type | resistor sizing | review | p.253 §4.4.2G | high |
| AOE-1271 | components | Millivoltmeter lesson (+/-10 mV full scale, 1 %, 10 Mohm input): LF411 fails (2 mV offset, 20 uV/C drift -> 200 uV per 10 C, 200 pA x 10M = 2 mV with open input). Need V_os < 100 uV and I_B < 10 pA, e.g., precision CMOS OPA336 (125 uV, 10 pA) or chopper LTC1050C (< 5 uV, < 0.05 uV/C, < 50 pA). Prefer designs needing no manual calibration in production | V_os + I_B*R_in + TCV_os*dT < 1 % FS | V_os, I_B, drift, R_in | precision dc front ends | calc | p.243, 253-254 §4.4.3 | high |
| AOE-1272 | components | Peak detector: droop = I_B/C (LM358 with 1 uF: 0.04 V/s typ, 0.5 V/s worst); maximum follow rate = I_out/C (20 mA into 1 uF = 0.02 V/us); choose C to balance. TLC2272 + 0.01 uF: 0.0001 V/s droop, 2 V/us. Use low-leakage diodes (FJH1100 < 1 pA @ 20 V, PAD5, diode-connected 2N4417) and a FET-input follower; beware dielectric absorption (a tantalum charged to 10 V recovers ~1 V after a brief short). Reset with a MOSFET/CMOS switch plus small series R | droop = I_B/C; slew = I_out/C | I_B, I_out, C | peak detectors, S/H | calc | p.254-255 §4.5.1, fn29 | high |
| AOE-1273 | components | Sample-and-hold: droop = I_leakage/C; switch R_on with C limits tracking bandwidth; the input buffer must supply C*dV/dt and have enough slew; the op-amp driving C must be stable into that capacitive load (e.g., C-load-stable LT1457 to 0.01 uF). Integrated S/H: LF398 (~$1.25); AD783 acquisition 0.4 us to 0.01 % for a 5 V step | droop = I_leak/C; f3dB = 1/(2*pi*R_on*C) | C, R_on, I_leak | ADC front ends | calc | p.256 §4.5.2, Fig 4.60 | high |
| AOE-1274 | components | T-network feedback (e.g., 100k-100k with a divider) simulates a very large feedback resistor (10 Mohm) without stray-capacitance problems, but in a transresistance stage it multiplies the output offset (100 x V_os vs V_os for a real 10M) | V_out,offset = V_os*(T-network gain) | network | high-gain/transresistance stages | calc | p.259 Fig 4.66 | high |
| AOE-1275 | components | Differentiator Vout = -R*C*dVin/dt is noisy and usually unstable: add series input resistor R1 and feedback capacitor C2; minimum R1 = 0.5*sqrt(R2/(C1*f_T)) (as printed), C2 ~ C1*R1/R2 as a starting point; above 1/(2*pi*R1*C1) it becomes an integrator | eq 4.7; R1_min = 0.5*sqrt(R2/(C1*f_T)) | R2, C1, f_T | differentiators | calc | p.260 §4.5.7, Figs 4.68-4.69 | medium |
| AOE-1276 | power | Op-amps run from any split or asymmetric supply within the total rating; unregulated rails are often acceptable thanks to PSRR (LF411: 90 dB typ). With a single supply, bias signals at a reference (e.g., V+/2) - a conventional op-amp can't swing to its rails (LF411: within ~1.5 V; not specified below 10 V total) and no op-amp can swing its output beyond the rails | V_sig within [V- + margin, V+ - margin] | supply, swing | single-supply analog | review | p.261-262 §4.6-4.6.1 | high |
| AOE-1277 | power | Single-supply references: divider to V+/2 per stage, or one common bypassed reference (buffer it with a follower if dc/signal currents flow in it); an IC reference can hold it a fixed voltage from one rail. Add dc-return resistors at ac-coupled input/output connectors so no dc appears there (prevents clicks/pops on connection). Example: 12 V supply, V_ref = 6 V -> ~9 Vpp swing, 40 dB audio amp | V_ref bypassed; R to ground at connectors | stages | single-supply audio/sensor | inspect | p.262 §4.6.1A, Figs 4.71-4.72 | high |
| AOE-1278 | power | Rail splitter (op-amp follower creating mid-supply "ground"): the required output bypass capacitor plus op-amp output resistance makes a lagging phase inside the loop -> oscillation or ringing, even with "C-load-stable" parts (LT1097 shows an output-impedance bump and ringing). Fixes: small series damping resistor (a few ohms; 5 ohm largely removes the bump), split fast/slow feedback (e.g., 2.7 ohm, 10k, 2.7 nF), or overcompensate. Integrated TLE2425/2426: < 0.2 mA, stable with >= 0.33 uF, +/-20 mA | R_damp ~ 2.7-5 ohm | C_bypass, r_o | battery split supplies | sim | p.262-264 §4.6.1B, Figs 4.73-4.77 | high |
| AOE-1279 | components | Capacitive loads destabilize op-amps: RG-58 coax is ~100 pF/m, so a 2 m cable adds ~200 pF - enough to make an LF411 follower oscillate (8 ft of cable does). Cures: 25-100 ohm series output resistor outside the loop (50 ohm = matched source for 50 ohm cable); split feedback (fast from op-amp output, slow from load); raise closed-loop gain; choose a part with a stability-vs-C_L guarantee (LMC6482 plot); or add a higher-f_T unity-gain buffer (with 50-100 ohm at its input, maybe a rolloff cap) | R_iso = 25-100 ohm; C_cable = 100 pF/m | C_load | op-amp outputs to connectors/cables | inspect | p.264-265 §4.6.2, Figs 4.78-4.79 | high |
| AOE-1280 | components | Don't assume an op-amp output reaches the negative rail just by adding an external current sink - the internal driver may not allow it; look for explicit datasheet permission. Single-supply/RRO parts use common-source/common-emitter output devices; RRIO inputs use parallel n- and p-type input pairs | datasheet guarantee | op-amp type | single-supply output swings | review | p.266 §4.6.3B | high |
| AOE-1281 | power | Battery budget must include load currents, not just op-amp quiescent current: a 10 uA photometer driving a 500 uA meter runs a 9 V battery (~500 mAh) ~1 month instead of 40,000 h; < 20 uA continuous drain gives nearly full shelf life (years) for 9 V (500 mAh) and AA (2500 mAh) cells; alkaline cells end life at ~1.0 V (9 V battery ~6 V) | life = C_batt/(I_q + I_load,avg) | currents, capacity | battery instruments | calc | p.265-266 §4.6.3A; p.276 §4.8.2 | high |
| AOE-1282 | components | VCO/integrator dynamic range near zero input is limited by V_os (and I_B through the resistor network): f_max/f_min ~ V_ref/V_os (5 V/60 uV -> ~100,000:1; ~50,000:1 including I_B). Choose resistor values small enough that V_os, not I_B*R, dominates | DR = V_ref/(V_os + I_B*R_eq) | V_os, I_B, V_ref | VCOs, V-to-F, integrators | calc | p.267-268 §4.6.4 | high |
| AOE-1283 | assembly | Surface-mount parts shrink boards (SOT-23 + 0603 VCO board = 22 % of the through-hole version, 4.5x smaller) and perform better (lower parasitic inductance); many new high-performance ICs are SMT-only, so plan for PCB prototypes or adapters | area_SMT ~ 0.22 x area_TH | package choice | prototyping/layout | review | p.268-269 §4.6.5, Fig 4.84 | high |
| AOE-1284 | protection | Line-voltage zero-crossing detector input protection: large series resistor (47k, 3 W, power rating set by max rms input) plus diodes to rails allows +/-350 V (150 V rms) inputs; a divider keeps the comparator input above its -0.3 V phase-reversal limit (LM393); modern comparators (LT1671, MAX989) avoid phase reversal. Speed-up capacitors larger than a few pF can themselves cause phase reversal | P_R = V_rms^2/R_series; V_in(comp) > -0.3 V | V_in max | mains sensing | calc | p.269-270 §4.6.6, Fig 4.85 | high |
| AOE-1285 | components | Transient (capacitive-only) hysteresis puts both thresholds at 0 V for a time constant tau = C*R (e.g., 0.1 uF for 0.5 ms at 60 Hz) but assumes a minimum input slew and a maximum crossing frequency | tau = C1*R6 | f, slew | zero-crossing detectors | calc | p.270 | high |
| AOE-1286 | process | Parts get discontinued (obsolescence, low demand, lost designs, new test lines, manufacturer failure - e.g., HA4925, HA2705, MAX402, SSS-4404; OPA627 was unavailable ~1 year). Check lifecycle status and second sources before production; fall-backs are redesign or a plug-in daughterboard emulation | lifecycle = active, >= 2 sources for critical parts | BOM | release/sustaining | review | p.273 box "Here Yesterday, Gone Today" | high |
| AOE-1287 | protection | Lab amplifier input protection: series R + clamp diodes to the rails lets inputs reach +/-150 V; the series R with input + diode + wiring capacitance (~12 pF) forms a lowpass (300 kHz here) - for wideband use smaller R, ~47 pF across it, or low-capacitance diodes (1N3595, PAD5). Use op-amps free of phase reversal when inputs may go > 0.3 V below V- (OPA627 is) | f3dB = 1/(2*pi*R_prot*C_in) >> BW | R_prot, C_in | instrument inputs | calc | p.274-275 §4.8.1 | high |
| AOE-1288 | components | Buffer inside an op-amp loop adds lag: OPA627 (f_T 16 MHz, 75 deg phase margin) + LT1010 (~50 deg extra lag) is near instability; fix with a small cap (4.7 pF) directly around the op-amp so its local loop rolls to unity at ~1 MHz where the buffer adds < 5 deg | PM_total = PM_opamp - lag_buffer(f_c) > ~45 deg | f_T, buffer phase | composite amplifiers | calc | p.275-276 §4.8.1 | high |
| AOE-1289 | test | Stuck-node tracing: inject a dc current (e.g., 10 mA) and measure the voltage drop along the trace with a floating high-gain microvolt meter; a 0.010 in wide, 1 oz (0.0013 in) PCB trace is ~53 mohm/in, so 10 mA gives ~530 uV/in toward the short | R_trace = 53 mohm/in (10 mil, 1 oz) | trace width/weight | board debug | measure | p.276 §4.8.2 | high |
| AOE-1290 | components | Current-shunt sensing: use a 4-terminal (Kelvin) shunt (e.g., 0.0005 ohm, 50 mV at 100 A); a differential amplifier rejects ground-lead drops; return the op-amp's negative supply to the more negative shunt end so the input common mode never goes below V-. Offset sets the low end: 1 % at 10 % of full scale (5 mV) needs V_os <= 50 uV; LM358A (3 mV) needs trimming, LT1006 80 uV, LT1077A 40 uV, chopper LTC1050C 5 uV gives 1 % at 1 % FS (10,000:1). High-side sensing keeps grounds common | V_os <= error*V_sense,min | V_shunt, accuracy | current measurement | calc | p.277-278 §4.8.3, Fig 4.91 | high |
| AOE-1291 | components | Current divider (two resistors from a current source into a virtual ground) is only as accurate as the virtual ground: V_os of 3 mV against a 10 mV signal is a 30 % error; a two-step (transresistance then integrator) design is ~3 % | error = V_os/V_signal | V_os, V_signal | photocurrent scaling | calc | p.279 §4.8.4C | high |
| AOE-1292 | control-loop | Stability criterion: open-loop (loop) phase shift must be < 180 deg where loop gain = 1; the follower (B = 1) is the worst case. Internally compensated op-amps use a dominant pole (1-20 Hz) placed so unity gain falls at the next natural pole: ~45 deg phase margin worst case (PM = 180 - (90 + 45)); Miller compensation keeps the unity-gain crossing fixed despite gain spread | PM = 180 deg - abs(phase(AB)) at abs(AB) = 1 | phase response | feedback amplifiers | sim | p.280-283 §4.9.1-4.9.2A, Figs 4.96-4.101 | high |
| AOE-1293 | control-loop | Decompensated/uncompensated op-amps are stable only above a minimum closed-loop gain (OP37: G >= 5, f_T 63 MHz, 17 V/us vs OP27 8 MHz, 2.8 V/us; THS4021/22: G >= 10, > 1 GHz vs THS4011 300 MHz) - worth using for high-gain, wide-bandwidth stages. Low closed-loop gain is MORE prone to oscillation than high gain (feedback divider attenuates the loop) | G_CL >= G_min(datasheet) | G_CL | op-amp selection | review | p.283 §4.9.2B; p.285 §4.9.3A | high |
| AOE-1294 | control-loop | Pole-zero compensation: place a zero at the amplifier's second pole and adjust the first pole so the response reaches unity at the third pole (pole splitting moves the second pole up); datasheets often give the R and C values | f_zero = f_p2 | poles | externally compensated amps | review | p.284 §4.9.2C, Fig 4.103 | high |
| AOE-1295 | control-loop | Feedback-network frequency response matters: plot LOOP gain; the ideal closed-loop gain curve should intersect the open-loop gain curve with a slope difference of 6 dB/octave, and never as much as 12 dB/octave. A few pF across the feedback resistor restores 6 dB/octave closure; differentiators (rising closed-loop gain) must be rolled off; integrators are inherently stable | slope difference at intersection = 6 dB/oct (< 12) | Bode plot | all op-amp feedback networks | sim | p.284 §4.9.3, Fig 4.104; p.291 Review O | high |
| AOE-1296 | control-loop | Loops through transformers/reactive loads (e.g., precision 60 Hz, 115 V source): take high-frequency feedback (above ~3 kHz) from the transformer's driven low-voltage side and low-frequency feedback from an isolated output-sensing winding; overcompensate the op-amp (e.g., LT1097 overcomp pin) and keep loop gain modest for inductive loads. Result: output regulation improved from 10 % to 0.2 % vs load, distortion well below 1 % | split HF/LF feedback | phase shifts | transformer-coupled drivers | sim | p.285-286 §4.9.3B, Figs 4.105-4.106 | high |
| AOE-1297 | protection | Power output stages need fault protection sized for the short-circuit case: simple collector resistors or base-robbing current limiting still leave full supply voltage across the transistors at the limit current (much higher dissipation than normal) - use foldback limiting or conservative heatsinking; keep a resistor bridging the push-pull crossover region (Darlington dead zone ~4 VBE ~2.5 V) so the loop never opens | P_short = V_supply*I_limit | V_supply, I_lim | power amplifiers | calc | p.286 §4.9.3B points | high |
| AOE-1298 | control-loop | Motorboating: several ac-coupled stages inside one feedback loop accumulate leading phase shift at low frequency (45 deg per coupling network at its corner, approaching 90 deg below) and can oscillate at very low frequency; prefer dc coupling or widely separated coupling corners | total LF phase lead < 180 deg where loop gain >= 1 | coupling corners | ac-coupled feedback amps | review | p.287 §4.9.3C | high |
| AOE-1299 | components | Op-amp noise/input parameters (review): e_n ~1 nV/rtHz (low-noise BJT) to >= 100 nV/rtHz (micropower); i_n = sqrt(2*q*I_B) for most op-amps (0.1 fA/rtHz CMOS to 1 pA/rtHz wideband BJT; not for bias-compensated BJTs); noise resistance r_n = e_n/i_n - above source impedance r_n current noise dominates | i_n = sqrt(2 q I_B); r_n = e_n/i_n | I_B, e_n, R_s | low-noise op-amp choice | calc | p.289-290 Review L | high |
| AOE-1300 | components | Integrated power/HV op-amps and buffers cover what discrete boosters would: outputs to 10 A (OPA541) or more (25 A+), supplies to 1 kV (PA97 900 V); they need current-limit set resistors and serious heatsinking ("provided you can get the heat out") | see Table 2.22 | V, I needs | piezo/servo/HV drivers | review | p.272-273 Table 4.2b | high |
| AOE-1301 | requirements | Precision vs dynamic range are different requirements: a 5-digit DMM is precise (0.01 %) and wide-range; a decade amplifier/reference may be precise with little dynamic range; a 6-decade log amp or 10,000:1 coulombmeter may be wide-range at only 1-5 % accuracy. Wide-dynamic-range designs must trim input offsets carefully to stay proportional near zero | specify accuracy and range separately | spec | analog front-end requirements | review | p.292-293 §5.1.1 | high |
| AOE-1302 | requirements | Build an error budget: tally every error source (component tolerances, op-amp input errors, output errors, drifts vs time/temperature/supply) - a few 0.01 % resistors are wasted if an offset current times source resistance gives 10 mV. Strict worst-case adds guaranteed maxima as unsigned magnitudes (e.g., 18 x 1 % gain resistors -> +/-18 %); the pragmatic alternative relies on component and final testing | E_total(worst) = sum abs(E_i) | error sources | precision designs | calc | p.293 §5.1.2; p.295-296 §5.3 | high |
| AOE-1303 | requirements | Specify zero error and scale error separately: e.g., a 10 mV full-scale meter may accept +/-5 % scale error but must read 0 within 1 % of full scale (0.1 mV) with input shorted or open. With 10 Mohm input, zero error = V_os + I_B*R_in, so each of V_os <= 100 uV and I_B <= 10 pA (10 pA x 10M = 0.1 mV) individually | V_err = V_os + I_B*R_in <= 1 % FS | V_os, I_B, R_in | meters, sensor front ends | calc | p.293-294 §5.2.1-5.2.2 | high |
| AOE-1304 | power | Battery-powered analog must work to end-of-life cell voltage: alkaline cells are quoted at 1.0 V or 0.9 V per cell, so a 2-cell design must run down to +1.8 V total supply (and single-supply op-amps must reach 0 V at input and output) | V_supply,min = n_cells x 0.9 V | cell count | battery instruments | calc | p.293 §5.2.1 | high |
| AOE-1305 | components | Current-sensing feedback with a precision sense resistor (0.1 % 100 ohm parts are commonplace, ~$0.20) makes a meter's accuracy independent of the meter's coil resistance; route the input common directly to the low side of the sense resistor (Kelvin connection - essential for small sense resistors, 4-wire shunts); split feedback (R at LF, C at HF) with an inductive meter load; series output resistor limits off-scale meter current | Kelvin sense on R_s | R_s, wiring R | precision current sensing | inspect | p.294 §5.2.2, Fig 5.1, fn2 | high |
| AOE-1306 | protection | Low-voltage leakage of protection diodes is rarely specified but matters: 1N914/1N4148 look like ~10 Mohm at low voltage; 1N3595 ~10,000 Mohm below 10 mV; PAD-1/PAD-5 are low leakage; a diode-connected low-leakage JFET (PN4117, gate = anode) or an npn junction works; BFT25 collector-base leaks < 10 fA reverse, < 40 fA forward to 50 mV. Clamp leakage at full-scale input must stay << the input-current budget (e.g., < 10 pA) | I_leak(V_FS) << I_budget | clamp device | high-impedance input protection | measure | p.294-295 Fig 5.2, fn3-4 | high |
| AOE-1307 | components | Op-amp input current rises with temperature: CMOS/JFET "bias" current is leakage doubling every 10 C, so a 1 pA (25 C) part is 50 pA at 85 C (AD8603); check the budget at the maximum operating temperature, not 25 C. Manufacturers' worst-case leakage limits may be lazy (LPV521 max/typ = 100:1) | I_B(T) = I_B(25)*2^((T - 25)/10) | T_max | high-Z precision inputs | calc | p.295 §5.2.2, fn6 | high |
| AOE-1308 | components | Auto-zero (chopper) op-amps have excellent offset but relatively high input current - into 10 Mohm it can dominate (MAX9617: 1.4 % offset; ISL28133: 3 %); low-voltage precision CMOS op-amps (AD8603: 50 uV, 1 pA max) may be the better fit | I_B*R_source vs V_os | R_source | chopper selection | calc | p.295 §5.2.2, fn5 | high |
| AOE-1309 | process | Unspecified or poorly specified parameters: read datasheets creatively (worst-case leakage limits often reflect ATE test limits), measure the parameter yourself (show it is orders below budget), set up incoming inspection, or validate at subassembly/final test. Example: 200 x 4000B CMOS ICs at 0.04 uA typ, 10 uA max -> 7 mAh/year typical vs 17.5 Ah worst case; testing subcircuits' quiescent current found only handling-damaged parts. Keithley electrometers use in-house-qualified JFETs run at 0.55 V drain voltage (not in any datasheet) | test to budget when worst-case is infeasible | parameter, budget | precision/ultra-low-power designs | measure | p.296-297 §5.3A | high |
| AOE-1310 | components | Strain-gauge bridge example: 350 ohm bridge, sensitivity 2 mV/V -> +/-10 mV full scale on a +2.5 V common-mode level when excited with +5 V; needs an instrumentation amplifier front end (high CMRR); a precision ADC-based (digital) nulling scheme is an attractive alternative to all-analog | V_FS = S*V_exc (S = 2 mV/V) | S, V_exc | bridge sensors | calc | p.297 §5.4, fn10 | high |
| AOE-1311 | requirements | Error budget example targets (autonull amplifier, referred to input): input drift <= 10 uV (temperature and supply) and nulled drift < 1 uV/min. Static offsets of tens of uV are irrelevant in a nulling instrument; only drifts with time and temperature matter | drift_RTI <= 10 uV; droop < 1 uV/min | budget | nulling/chopper systems | calc | p.298-299 §5.5-5.5.1 | high |
| AOE-1312 | requirements | Error budget items come from (a) datasheet specs ("knowns"), (b) estimates of poorly specified parameters ("known unknowns"), and (c) effects you don't realize matter ("unknown unknowns") - e.g., femtoamp measurements drifting after the enclosure is opened (surface charge on Teflon wiring), panel meters deflected by static on the glass | budget includes margin for (b), (c) | experience | precision budgets | review | p.299 §5.5, fn12 | high |
| AOE-1313 | components | Component specs to budget: initial accuracy, stability with time, tempco, voltage coefficient, dielectric absorption/memory, temperature cycling, soldering, shock/vibration, short-term overload, moisture - the sum of other effects can exceed the initial tolerance | total drift = sum of listed shifts | component datasheet | precision resistors/caps | review | p.299-300 §5.6 | high |
| AOE-1314 | components | RN55C 1 % metal film: tempco 50 ppm/C (-55 to +175 C); soldering/temperature/load cycling 0.25 %; shock and vibration 0.1 %; moisture 0.5 %. 5 % carbon composition (Allen-Bradley CB): 3.3 % over 25-85 C; soldering/load cycling +4 %/-6 %; shock/vibration +/-2 %; moisture +6 % - never hand-select carbon parts "within 1 %" for precision | dR/R per effect as listed | resistor family | precision resistor selection | review | p.300 §5.6 | high |
| AOE-1315 | components | Ultra-precise resistors: Susumu RG SMT to 0.02 %, 5 ppm/C; Vishay MPM thin-film networks 0.05 % absolute, 0.01 % matched, 25 ppm/C absolute, 2 ppm/C tracking; Vishay Bulk Metal Foil 0.005 % absolute, 0.001 % matched, 0.2 ppm/C absolute, 0.1 ppm/C tracking. Use 0.1 % in gain-setting networks; 1 % metal film is fine where absolute accuracy is irrelevant (offset attenuators) | tolerance/TC per grade | accuracy need | gain/ratio networks | review | p.300 §5.6-5.6.1 | high |
| AOE-1316 | components | Hold/integrating capacitor leakage: at microfarad values film capacitors (polystyrene, polypropylene, polyester) leak least; polypropylene often specified at 10,000-100,000 Mohm*uF (2.2 uF -> 22-220 Gohm). Even 100 Gohm leaks 100 pA at 10 V (droop ~3 mV/min at the example's output) - cancel first-order leakage with a resistor feeding current proportional to the capacitor voltage (assume ~10 % of worst-case leakage remains) | R_leak = (Mohm*uF rating)/C; I = V/R_leak | C, rating, V | S/H, integrators, nulling | calc | p.300 §5.6.2A | high |
| AOE-1317 | components | Dielectric absorption ("memory"): Teflon is best; polystyrene and polypropylene film are generally the best practical choice; C0G ceramic can be excellent but varies by brand; avoid electrolytics/high-K ceramics for analog hold. (Measured: capacitors held at +10 V for a day, shorted 10 s, then open-circuited, recover part of the voltage) | DA ranking PTFE > PS/PP > C0G(brand) >> others | dielectric | S/H, integrators, peak detectors | measure | p.300-301 §5.6.2B, Fig 5.4 | high |
| AOE-1318 | components | For ultra-low-leakage analog switching a small shielded reed relay can beat semiconductor switches: Coto 9202-12 (12 V, 18 mA coil) R_off >= 1e12 ohm (1e13 typ), C_off < 1 pF, R_on < 0.15 ohm. Coil-to-contact capacitance (0.2 pF) injects Q = C*dV_coil = 2.4 pC -> 1.1 uV on 2.2 uF | Q = C_couple*dV_control; dV = Q/C_hold | C_couple, dV, C_hold | nulling/S-H switches | calc | p.301 §5.6.3 | high |
| AOE-1319 | components | MOSFET switch channel leakage (~1 nA) and gate charge injection (~100 pC) can wreck a hold circuit; mitigate with a series MOSFET pair whose downstream device has all four terminals at 0 V when off, and a large enough hold capacitor; JFET alternative: I_D(off) ~0.1 pA, C_rss ~0.3 pF | droop = I_leak/C; dV = Q_inj/C | I_leak, Q_inj, C | S/H switch design | calc | p.301 §5.6.3, Fig 5.5 | high |
| AOE-1320 | components | Op-amp input impedance rarely matters: feedback bootstraps it (OPA277P: 100 Mohm differential -> 250,000 Mohm common-mode; OPA129: 1e13/1e15 ohm FET). Example: 100 Mohm differential input vs (1M feedback / loop gain) = 10 ohm drive -> 1 part in 1e5 error; source impedances to 25 Mohm cause < 0.01 % gain error | error ~ Z_drive/Z_in,diff | loop gain | precision amplifiers | calc | p.301-302 §5.7.1; p.306-307 §5.7.6 | high |
| AOE-1321 | components | Low-input-current op-amp choices (25 C): OPA277P 0.5/1 nA with 20 uV max, 0.15 uV/C; LT1012AC 25/100 pA, 25 uV; AD706 50/200 pA; OPA124PB 0.35/1 pA, 250 uV, 2 uV/C; OPA129B 30 fA/0.1 pA, 2 mV, 10 uV/C; MAX9945 50 fA, 5 mV; LMP7721 3/20 fA, 150 uV; LMC6001A 10/25 fA, 350 uV. FET parts trade 4-20x worse offset drift (MOSFETs also drift with time) for input current | see Table 2.25 | I_B, V_os, drift | electrometer/high-Z inputs | review | p.302-303 §5.7.2, Table 5.3 | high |
| AOE-1322 | components | Balancing dc source resistances at both inputs makes I_os (not I_B) the error term - but it gains nothing for bias-compensated op-amps, whose residual I_B and I_os are comparable | balance only for non-compensated BJT inputs | op-amp type | precision dc stages | review | p.303 §5.7.2 | high |
| AOE-1323 | thermal | FET op-amp input current depends on chip temperature: LF412 at 6.5 mA max on +/-15 V dissipates 195 mW; in DIP-8 (R_thJA = 115 C/W) that is a 22 C rise, quadrupling I_B (200 pA max -> ~800 pA) - significant only for source impedances > ~1 Mohm vs its ~1 mV offset. LT1057 (JFET, ~3 pA at 25 C) reaches ~100 pA at 75 C, exceeding superbeta LT1012 | dT_chip = P_diss*R_thJA; I_B x 2 per 10 C | P_diss, R_th | FET-input precision circuits | calc | p.303 §5.7.2A, fn15, Fig 5.6 | high |
| AOE-1324 | components | Input bias current can vary strongly with common-mode voltage, especially in rail-to-rail-input op-amps (BJT RRI parts reverse I_B polarity abruptly at the input-pair crossover); datasheets often list I_B only at 0 V/mid-supply - check the I_B-vs-V_CM curve. Cascode-input parts (OPA129, OPA627) are flat; LMP7721 is 20 fA max | I_B(V_CM) from curves | V_CM range, R_source | RRI op-amp selection | review | p.304 §5.7.2B, Fig 5.7 | high |
| AOE-1325 | components | Offset voltage: precision op-amps 10s of uV worst case (OPA277P +/-20 uV max, 0.2 uV/C max drift; CMOS MAX4236A also 20 uV but ~12x worse drift); jellybeans (LF412) 2-5 mV. Prefer inherently low-V_os parts over trimming: low initial offset correlates with low drift; trimmers take space, need adjustment, drift; offset-adjust unbalance degrades drift and CMRR; trimmed offset drifts more with temperature | choose V_os(max) meeting budget untrimmed | budget | precision op-amp selection | review | p.304-305 §5.7.3, Fig 5.8 | high |
| AOE-1326 | components | If a precision op-amp must be trimmed, don't use the maker's full-range null network (far too much range, adjustment too critical to hold); use a narrow-range external trim, e.g., +/-50 uV linear in pot rotation (R11 = 33 ohm, R12 = 10M from a +/-15 V pot) injected into the feedback network (inverting and noninverting versions, Fig 5.9) | trim range ~ +/-(2-5) x V_os(max) | V_os(max) | offset trimming | calc | p.305 §5.7.3, Fig 5.9 | high |
| AOE-1327 | thermal | Keep precision op-amp loads >= 10k: self-heating from driving low-impedance loads shifts offset (example: 5 mW at 7.5 V, R_thJA ~0.15 C/mW -> 0.8 C rise -> 0.12 uV with 0.15 uV/C drift); at the uV level also control thermal gradients from nearby heat sources and thermal EMFs at dissimilar-metal junctions. A unity-gain power buffer inside the loop keeps heat out of the precision op-amp | dV_os = TCV_os*P*R_thJA; R_load >= 10k | load, drift | uV-level circuits | calc | p.305 §5.7.3; p.306 §5.7.6; p.312 §5.8.4 | high |
| AOE-1328 | components | Datasheet test conditions matter: an op-amp headlined "Low offset voltage: 65 uV max" (AD8615) guarantees it only at V_CM = 0.5 V and 3.0 V (V_S = 3.5 V) - elsewhere V_os can be far larger. Read the footnotes | spec valid only at stated conditions | datasheet | all parameter checks | review | p.305 §5.7.3, Fig 5.10 | high |
| AOE-1329 | components | CMRR converts common-mode level into an offset; an inverting stage is insensitive to op-amp CMRR (constant V_CM), a noninverting stage is not. For small differential signals on large dc levels use high-CMRR parts/configurations (OPA277: 130 dB min dc vs LF411 70 dB) or an instrumentation amplifier | dV_os = dV_CM/CMRR | V_CM swing, CMRR | differential/bridge measurements | calc | p.305-306 §5.7.4 | high |
| AOE-1330 | power | PSRR is referred to the input: OPA277 126 dB -> 1 V supply change = 0.5 uV input error; PSRR falls with frequency roughly like open-loop gain (OPA277 negative rail: 95 dB at 60 Hz, 50 dB at 10 kHz) - 120 Hz ripple on unregulated rails can matter; PSRR differs between + and - rails; often specified at G = 1 and worse at higher gain (some op-amps even show gain from a rail to the output) | V_err = dV_supply/PSRR | ripple, PSRR(f) | precision supply design | calc | p.306 §5.7.5 | high |
| AOE-1331 | components | Instrumentation amplifier front end example (LT1167A, G = 100): offset 40 uV, 0.3 uV/C, 0.28 uVpp noise (0.1-10 Hz), CMRR >= 120 dB, gain accuracy 0.08 %, 50 ppm/C gain tempco, I_B 0.35 nA max; for single-ended inputs protect with ~470 ohm series plus low-leakage clamp diodes. OPA277 bias (1 nA max) costs 1 uV per kohm of source impedance; a FET-input part (OPA627B, $35, 5 pA) costs ~3 uV per 4 C lab ambient drift - use FET inputs only above ~10 kohm source impedance | V_err = I_B*R_s vs TCV_os*dT | R_source, dT | precision front-end choice | calc | p.306-307 §5.7.6, fn17 | high |
| AOE-1332 | components | Slew-rate consequences: full-power swing Vpp <= S/(pi*f); a circuit demanding substantial slew operates with a large differential input error (BJT inputs need ~60 mV to reach full slew, JFET/MOSFET ~1 V) - distortion in "precise" circuits. Classic BJT-input compensated op-amps: S ~ 0.3*f_T; enhancement factor m = S/f_T: LT1007 1.0, OP275/285 8, LF411 12, TLE2141 25, LT1210 (CFB) 55, LT1315 220 | S = m*f_T | S, f_T | fast/large-signal precision | calc | p.307-308 §5.8.1, Figs 5.11-5.13 | high |
| AOE-1333 | timing | Settling-time estimate: closed-loop bandwidth f3dB = f_T/G_CL, time constant tau ~ G_CL/(2*pi*f_T), settling ~5-10 tau (e.g., TLE2414, f_T 5.9 MHz, inverting G = 2 -> tau = 54 ns, ~378 ns to 0.1 % vs 340 ns datasheet). It is a lower bound: check the slew-limited time; phase-response wiggles cause ringing; fast settling to 1 % doesn't imply fast settling to 0.01 % (long tails); rely on a manufacturer settling spec | tau = G_CL/(2*pi*f_T); t_s ~ 7*tau (0.1 %) | f_T, G_CL, accuracy | ADC drivers, DAC outputs | calc | p.308-309 §5.8.2, Figs 5.14-5.16 | high |
| AOE-1334 | timing | Single-pole (RC) settling to within fraction eps of final value takes t = tau*ln(1/eps): 1 % -> 4.6 tau, 0.1 % -> 6.9 tau, 0.01 % -> 9.2 tau | t_settle = RC*ln(1/eps) | tau, eps | filter/driver settling | calc | p.309 Fig 5.15 (derived) | medium |
| AOE-1335 | components | Crossover distortion: op-amps with unbiased push-pull outputs (LM324/358) show class-B distortion, worse at higher frequencies where loop gain falls; class-AB-biased parts (LT1013) are far better; audio-grade parts (LT1028, AD797, LME49710) reach < 0.0001 % (claimed) over 20 Hz-20 kHz; LT1028 e_n = 1.7 nV/rtHz max at 10 Hz. High-voltage op-amps win below ~10 kHz, low-voltage above ~200 kHz | distortion vs f per datasheet | application | audio/precision op-amp choice | review | p.309-310 §5.8.3, Figs 5.18-5.19 | high |
| AOE-1336 | components | Open-loop output impedance is highest near zero output (output devices at lowest current), rises at high frequency and sometimes at very low frequency (thermal/internal feedback); some op-amps are a few hundred ohms open loop, so effects are not negligible at modest loop gain and contribute to capacitive-load instability | Z_out,CL = Z_ol/(1 + AB) | Z_ol(f), loop gain | output stage behavior | review | p.310 §5.8.3, Figs 5.20-5.21 | high |
| AOE-1337 | components | Gain error from finite loop gain: eps = 1/(1 + A*B) (G = A/(1 + AB)); vs frequency eps(f) ~ 1/(1 + B*f_T/f) - work from the datasheet GBW and dc gain. LF411 (106 dB) at G = 1000: 0.5 % at dc and ~10 % at 500 Hz (its gain falls 6 dB/oct above ~20 Hz); OPA277 has 140 dB dc gain | eps = 1/(1 + A*B); eps(f) = 1/(1 + B*f_T/f) | A, B, f_T, f | precision gain stages | calc | p.312 §5.8.5, Fig 5.22 | high |
| AOE-1338 | components | Gain nonlinearity (low frequency, 4 kohm load, Pease AN-1485): LM8262 12 ppm (crossover), LF411 1.4 ppm (poor layout, thermal), LMC6482 1.1 ppm, LM358 1 ppm (asymmetric output), LF412 0.3 ppm, LMC6062 0.2 ppm, LMP2012 (auto-zero) 0.2 ppm, LM4562 0.025 ppm (G_OL = 1e7). Linearity depends on intrinsic output-stage symmetry and thermal layout, not just loop gain; unloaded nonlinearity is far smaller | ppm per datasheet/test | load | precision/ADC-driver op-amp choice | measure | p.312-314 §5.8.6, Figs 5.23-5.24 | high |
| AOE-1339 | components | Phase error of an op-amp stage: phi ~ -f/f_c radians (x57.3 for degrees), f_c = f_T/G_CL (use GBW); a single pole gives ~6 deg at f_c/10 and ~0.6 deg at f_c/100. Fixes: more bandwidth, an RC zero in feedback (needs tuning and tracks temperature poorly), two cascaded lower-gain stages, or active compensation with a matched dual op-amp: phi ~ -(f/f_c)^3 radians (small angles) | phi = -f/f_c; active: -(f/f_c)^3 | f, f_T, G_CL | video, interferometry, phase-sensitive paths | calc | p.314-315 §5.8.7, Figs 5.25-5.27 | high |
| AOE-1340 | components | Active phase compensation requires matched op-amp bandwidths (monolithic duals/quads match f_T to ~0.1 % typically, 1.5 % outlier; between specimens +/-20 %); it adds ~+3 dB peaking where the phase error is 45 deg (+0.1 dB at 0.1*f_T/G); low gains peak more (~7 dB at G = 2 for LF412; C_c = 1/(2*pi*f_T*R) cuts it to ~4 dB at 3x phase error) and may be unstable below G ~5 | f_T matching <= 1-2 % (same package) | op-amp pair | active compensation | sim | p.314-315 fn20-22 | high |
| AOE-1341 | components | Rail-to-rail-input op-amps with complementary input pairs show input-current and offset-voltage steps where control passes between pairs (V_os shifts near either rail, unpredictable in sign); distortion rises (OPA350: +17 dB when a 3 Vpp follower signal enters the crossover region). Remedies: use an inverting configuration (constant V_CM - "use an inverting configuration, unless you can't"), a ground-sensing RRO part if full RRI isn't needed, or single-pair charge-pump RRI parts (OPA36x "zero-crossover", AD8505/ADA4505, MAX4162, MAX4126) | keep V_CM out of crossover region | V_CM swing | RRI op-amp application | review | p.316 §5.9.1, Figs 5.28-5.31 | high |
| AOE-1342 | components | Rail-to-rail outputs are common-source/common-emitter push-pull stages with inherently high output impedance: loop gain depends on load resistance (LMC6482), capacitive loads cause large phase shift; open-loop Z_out may rise at low frequency. RRO distortion is typically 20-40 dB worse than conventional outputs; Monticelli class-AA outputs (OPA365 -114 dB, OPA1641 -126 dB harmonic distortion) fix much of this | check A_OL vs R_L and C_L stability | load | RRO op-amp application | review | p.316-319 §5.9.2, Figs 5.32-5.35 | high |
| AOE-1343 | components | "Rail-to-rail" BJT outputs don't reach the last few mV: LT6003 not within 10 mV of the negative rail; LT1077 saturates to 3 mV unloaded, 0.1 mV with a 5k pull-down; CMOS AD8616/AD8691 < 0.1 mV unloaded - check this when driving a single-supply ADC whose range goes to ground | V_OL(spec) <= ADC zero-scale error budget | output spec, load | ADC drivers | calc | p.317-318 §5.9.2B | high |
| AOE-1344 | components | Precision op-amp selection trends: BJT inputs give lowest offset, drift and voltage noise (e_n falls with rising bias current); FET inputs give lowest input current and current noise; low-voltage CMOS (factory-trimmed MAX4236A, OPA376; power-up auto-zero TLC4501A) now challenge JFETs. Chopper/auto-zero ("zero-drift") amplifiers have the smallest offset and drift (~+/-1 uV, ~+/-0.05 uV/C) but with caveats (§5.11: noise, input current, glitches) | choose per dominant error term | budget | precision op-amp selection | review | p.319-322 §5.10-5.10.1 | high |
| AOE-1345 | components | Chopper current-noise specs in parentheses in Table 5.5 should not be relied upon - measured values are often 5x-100x larger; guaranteed V_os specs may apply only over a restricted common-mode range (e.g., V_EE + 14 V < V_CM < V_CC - 0.7 V for one part) | derate chopper i_n 5-100x | datasheet notes | chopper selection, high-Z sources | review | p.321 Table 5.5 notes (e),(o) | high |

## 2. Formulas & tables (numbers)

### 2.1 Chapter 1 formulas (Foundations)

| quantity | formula (ASCII) | symbols / units | source |
|---|---|---|---|
| Ohm's law, power | V = I*R; P = I*V = I^2*R = V^2/R | V volts, I amps, R ohms, P watts | p.4-6 eq 1.1, 1.2 |
| series / parallel R | R = R1 + R2; R = R1*R2/(R1 + R2); G = 1/R, G_total = sum G_i | ohm, siemens | p.5-6 eq 1.3, 1.4 |
| Millman | Vout = sum(V_i*G_i)/sum(G_i) | G_i = 1/R_i | p.6 fn11 |
| divider | Vout = Vin*R2/(R1 + R2) | | p.7 eq 1.6 |
| Thevenin | V_Th = V_open-circuit; R_Th = V_oc/I_sc; divider: V_Th = Vin*R2/(R1+R2), R_Th = R1*R2/(R1+R2) | | p.9 eq 1.7-1.9 |
| Norton | I_N = I_sc; R_N = V_oc/I_sc | | p.69 |
| zener small-signal | dVout = dVin*R_dyn/(R + R_dyn) | R series feed resistor, R_dyn zener dynamic resistance | p.12 |
| sinewave | V = A*sin(2*pi*f*t + phi); omega = 2*pi*f; Vrms = A/sqrt(2); Vpp = 2A | | p.14 eq 1.10 |
| decibels | dB = 10*log10(P2/P1) = 20*log10(A2/A1) | | p.15 eq 1.11, 1.12 |
| capacitor | Q = C*V; I = C*dV/dt; U = 0.5*C*V^2 | C farads, U joules | p.18-19 eq 1.13-1.16 |
| parallel plate | C = 8.85e-14*er*A/d | C farads, A cm^2, d cm | p.18 eq 1.14 |
| caps series/parallel | C = C1 + C2 + ...; 1/C = 1/C1 + 1/C2 + ... | | p.21 eq 1.17, 1.18 |
| RC discharge / charge | V = V0*exp(-t/RC); Vout = Vf*(1 - exp(-t/RC)); t = RC*ln(Vf/(Vf - V)) | RC seconds | p.21-22 eq 1.19-1.22 |
| RC milestones | 50 % at 0.7RC; 10-90 % = 2.2RC; > 99 % at 5RC | | p.22-23 |
| inductor | V = L*dI/dt; U = 0.5*L*I^2 | L henrys | p.28 eq 1.23, 1.24 |
| Wheeler (air-core solenoid) | L[uH] = K*d^2*n^2/(18*d + 40*l); K = 1.0 (inch) or 2.54 (cm); +/-1 % for l > 0.4d | d diameter, l length, n turns | p.28-29 |
| ripple (cap-input rectifier) | dV = I_load/(f*C) half-wave; dV = I_load/(2*f*C) full-wave | f line frequency (Hz) | p.33 eq 1.25 |
| reactance | Xc = 1/(omega*C) = 1/(2*pi*f*C); XL = omega*L | ohms | p.42-44 eq 1.26, 1.29 |
| impedance | Z_R = R; Z_C = -j/(omega*C); Z_L = j*omega*L; series Z = Z1 + Z2 + ...; parallel 1/Z = 1/Z1 + 1/Z2 + ... | | p.46 eq 1.30-1.32 |
| ac power | P = Re(V*conj(I)) = Re(conj(V)*I) (rms phasors); PF = cos(phi) | | p.47 eq 1.34 |
| series RC power | P = V0^2*R/(R^2 + 1/(omega^2*C^2)) | | p.47 |
| RC highpass | Vout/Vin = 2*pi*f*R*C/sqrt(1 + (2*pi*f*R*C)^2); f3dB = 1/(2*pi*R*C) | | p.49 eq 1.35 |
| RC lowpass | Vout/Vin = 1/sqrt(1 + omega^2*R^2*C^2); f3dB = 1/(2*pi*R*C) | | p.50 eq 1.36 |
| LC resonance | f0 = 1/(2*pi*sqrt(L*C)); Q = f0/BW_3dB; parallel RLC Q = omega0*R*C = R/X; series RLC Q = omega0*L/R = X/R | | p.52-53 eq 1.37 |
| ringdown | V to 1/e in Q/pi cycles; energy to 1/e in Q/(2*pi) cycles | | p.54 |

### 2.2 RC lowpass phase shift vs frequency (Figure 1.104 inset)

| f/f3dB | phase = -atan(f/f3dB) |
|---|---|
| 0 | 0 deg |
| 0.1 | -5.7 deg |
| 0.2 | -11.3 deg |
| 0.25 | -14 deg |
| 0.5 | -26.5 deg |
| 1.0 | -45 deg |

Source: p.50 Fig 1.104. Rule of thumb: within ~6 deg of the asymptote (0 or -90 deg) one decade away from f3dB.

### 2.3 Decibel reference levels (p.15, p.68)

| reference | definition | equivalent |
|---|---|---|
| 0 dBV | 1 V rms | - |
| 0 dBm (RF, 50 ohm) | 1 mW into 50 ohm | 0.22 V rms |
| 0 dBm (audio, 600 ohm) | 1 mW into 600 ohm | 0.78 V rms |
| 0 dB SPL | 20 uPa rms | 2e-10 atm |
| -30 dBm | 1 uW | - |
| +3 dBV | 1.4 V rms | 2 V peak, 4 Vpp |

### 2.4 Table 1.1 Representative Diodes (p.32)

| part | type | V_R max (V) | I_R typ at 25 C (A @ V) | V_F (mV) @ I_F | capacitance (pF @ V_R) | SMT p/n | comment |
|---|---|---|---|---|---|---|---|
| PAD5 | silicon | 45 | 0.25 pA @ 20 V | 800 @ 1 mA | 0.5 pF @ 5 V | SSTPAD5 | metal + glass can (ultra-low leakage) |
| 1N4148 | silicon | 75 | 10 nA @ 20 V | 750 @ 10 mA | 0.9 pF @ 0 V | 1N4148W | jellybean signal diode |
| 1N4007 | silicon | 1000 | 50 nA @ 800 V | 0.8 V @ 250 mA | 12 pF @ 10 V | DL4007 | 1N4004 = lower-V version |
| 1N5406 | silicon | 600 | <10 uA @ 600 V (OCR "<10 mA") | 1.0 V @ 10 A (as printed) | 18 pF @ 10 V | none | heat removed through leads |
| 1N6263 | Schottky | 60 | 7 nA @ 20 V | 400 @ 1 mA | 0.6 pF @ 10 V | 1N6263W | see also 1N5711 |
| 1N5819 | Schottky | 40 | 10 uA @ 32 V (OCR "10 mA") | 400 @ 1000 mA | 150 pF @ 1 V | 1N5819HW | jellybean power Schottky |
| 1N5822 | Schottky | 40 | 40 uA @ 32 V | 480 @ 3000 mA | 450 pF @ 1 V | none | - |
| MBRP40045 | Schottky | 45 | 500 (uA or mA; OCR ambiguous) @ 40 V | 540 @ 400 A | 3500 pF @ 10 V | "you jest!" | Moby dual Schottky |

Notes (as printed): (a) SMT = surface-mount technology; (b) Schottky diodes have lower forward voltage and zero reverse-recovery time, but more capacitance. OCR renders "u" as "m" in several cells; values flagged above are OCR-ambiguous.

### 2.5 Chip-size codes (p.4 fn7, p.65 Fig 1.132)

| inch code | metric code | size |
|---|---|---|
| 01005 | 0402 | 0.4 x 0.2 mm (0.016 x 0.008 in) |
| 0201 | 0603 | 0.6 x 0.3 mm |
| 0402 | 1005 | 1.0 x 0.5 mm |
| 0603 | 1608 | 1.6 x 0.8 mm (derived from code rule) |
| 0805 | 2012 | 2.0 x 1.25 mm (80 x 50 mil) |
| 1206 | 3216 | 3.2 x 1.6 mm (derived from code rule) |

### 2.6 Chapter 2 BJT formulas

| quantity | formula (ASCII) | notes | source |
|---|---|---|---|
| current gain | Ic = hFE*Ib = beta*Ib | beta 50-250 spread within a type; never design on it | p.72 eq 2.1 |
| Ebers-Moll | Ic = Is(T)*(exp(VBE/VT) - 1) ~ Is*exp(VBE/VT) | Is ~ 1e-15 A (2N3904) | p.91 eq 2.8-2.11 |
| thermal voltage | VT = k*T/q = 25.3 mV at 20 C | k = 1.38e-23 J/K, q = 1.60e-19 C | p.91 eq 2.10 |
| VBE per decade | dVBE = VT*ln(10) = 58.2 mV (~60 mV/decade); x2 per 18 mV; 4 %/mV | | p.91-92 |
| r_e | r_e = VT/Ic = 25/Ic[mA] ohm | 25 ohm at 1 mA | p.92 eq 2.12 |
| gm | gm = Ic/VT = 1/r_e = 40*Ic[mA] mS | | p.92 eq 2.13 |
| VBE tempco | -2.1 mV/C at constant Ic; Ic +9 %/C at constant VBE | x10 per 30 C | p.92 §2.3.2C |
| Early | dVBE = -eta*dVCE, eta = 1e-4 to 1e-5; Ic = Ic0*(1 + VCE/VA), VA = 50-500 V; eta = 1/(VA + VCE); r_o = VA/Ic | | p.92-93 eq 2.14, 2.15 |
| follower | V_E = V_B - 0.6; Z_in = (beta+1)*Z_load; Z_out = Z_s/(beta+1) + r_e; Gv = R_L/(r_e + R_L) | | p.79-80, 93 eq 2.2-2.4 |
| current source | Ic = (V_B - 0.6)/R_E, compliance V_C > V_E + 0.2 V | | p.86 eq 2.5 |
| CE amp (degenerated) | Gv = -R_C/(R_E + r_e); Z_in = R1 parallel R2 parallel beta*(R_E + r_e); Z_out ~ R_C | | p.88, 93 eq 2.6 |
| grounded-emitter gain at 0.5 Vcc bias | G = 20*Vcc (volts) | independent of Ic | p.98, p.128 |
| distortion (CE) | dG/G ~ (dVout/V_drop)*VT/(VT + Ie*R_E); waveform distortion ~ 1/3 of this | | p.94-95 |
| differential pair | G_diff = R_C/(2*(r_e + R_E)); G_CM = -R_C/(2*R_tail + R_E); CMRR ~ R_tail/(r_e + R_E) | max G_diff = 20*V(R_C); max CMRR = 20*V(R_tail) | p.103 |
| bootstrap | R_eff = R3/(1 - A) = R3*(1 + R_L/r_e) | | p.112 |
| Miller | C_in,eff = C_cb*(Gv + 1) | | p.114 |
| feedback | G = A/(1 + A*B); dG/G = (dA/A)/(1 + A*B); Z_in(series) = (1 + AB)*R_i; Z_in(shunt) = R_i parallel R_f/(1 + A); Z_out(V-sense) = R_o/(1 + AB); Z_out(I-sense) = R_o*(1 + AB); Blackman Z_out = R_o*(1 + (AB)_sc)/(1 + (AB)_oc); inverting G = -A*(1 - B)/(1 + AB) | B = R1/(R1 + R2) | p.117-120 eq 2.16, 2.17 |
| phase shifter | phi = 2*arctan(omega*R*C) | constant amplitude | p.89 Fig 2.38 |
| power device dissipation | P_real = (Tj_design - T_amb)/(theta_JC + theta_CS + theta_SA); datasheet P_max = (150 - 25)/theta_JC | "specsmanship" | p.106 Table 2.2 notes |

### 2.7 Table 2.1 Representative Bipolar Transistors (p.74) - partial transcription

OCR scrambled the VCEO / Ic(max) / hFE@mA / Ccb columns (values interleaved across rows); only part numbers, f_T and comments are transcribed with confidence. Consult the printed table or datasheets for ratings.

| npn TO-92 | npn SOT-23 | pnp TO-92 | pnp SOT-23 | f_T (MHz) | comment |
|---|---|---|---|---|---|
| 2N3904 | MMBT3904 | 2N3906 | MMBT3906 | 300 | jellybean |
| 2N4401 | MMBT4401 | 2N4403 | MMBT4403 | 300 | '2222 and '2907 dies |
| BC337 | BC817 | BC327 | BC807 | 150 | jellybean |
| 2N5089 | MMBT5089 | 2N5087 | MMBT5087 | 350 | high beta |
| BC547C | BC847C | BC557C | BC857C | 150 | jellybean (note b: lower-beta -A/-B suffixes; low-noise BC850/BC860) |
| MPSA14 | MMBTA14 | MPSA64 | MMBTA64 | 125 | Darlington (30 V, hFE ~10000 @ 50 mA as printed) |
| ZTX618 | FMMT618 | ZTX718 | FMMT718 | 120 | high Ic, small package |
| PN2369 | MMBT2369 | 2N5771 | MMBT5771 | 500 | fast switch, gold doped |
| 2N5550 | MMBT5550 | 2N5401 | MMBT5401 | 100 | SOT-223 available |
| MPSA42 | MMBTA42 | MPSA92 | MMBTA92 | 50 | HV small signal (VCEO 300 V) |
| MPS5179 | BFS17 | MPSH81 | MMBTH81 | 900 | RF amplifier |
| - | BFR93C | - | BFT93C | 4000 | RF amp (note c: also BFR25A, BFT25A) |
| TIP142 | - | TIP147 | - | low | TO-220 Darlington (100 V, 10 A, hFE > 1000 @ 5 A) |

### 2.8 Table 2.2 Bipolar Power Transistors (p.106) - ratings columns (hFE/f_T columns OCR-scrambled, omitted)

| NPN | PNP | case | VCEO max (V) | Ic max (A) | Pdiss max (W, case 25 C) | R_thJC (C/W) |
|---|---|---|---|---|---|---|
| BD139 | BD140 | TO-126 | 80 | 1.5 | 12.5 | 10 |
| 2N3055 | 2N2955 | TO-3 | 60 | 15 | 115 | 1.5 |
| 2N6292 | 2N6107 | TO-220 | 70 | 7 | 40 | 3.1 |
| TIP31C | TIP32C | TO-220 | 100 | 3 | 40 | 3.1 |
| TIP33C | TIP34C | TO-218 | 100 | 10 | 80 | 1.6 |
| TIP35C | TIP36C | TO-218 | 100 | 25 | 125 | 1.0 |
| MJ15015 | MJ15016 | TO-3 | 120 | 15 | 180 | 1.0 |
| MJE15030 | MJE15031 | TO-220 | 150 | 8 | 50 | 2.5 |
| MJE15032 | MJE15033 | TO-220 | 250 | 8 | 50 | 2.5 |
| 2SC5200 | 2SA1943 | TO-264 | 230 | 17 (as printed) | 150 | 0.8 |
| 2SC5242 | 2SA1962 | TO-3P | 250 | same as above | same | same |
| MJE340 | MJE350 | TO-126 | 300 | 0.5 | 20 | 6 |
| TIP47 | MJE5730 | TO-220 | 250 | 1 | 40 | 3.1 |
| TIP50 | MJE5731A | TO-220 | 400 | same as above | same | same |
| MJE13007 | MJE5852 | TO-220 | 400 (VCES 700 V blocking) | 8 | 80 | 1.6 |
| Darlington: MJD112 | MJD117 | DPak | 100 | 2 | 20 | 6.3 (hFE 1000 min, 2000 typ @ 2 A; f_T 25 MHz) |
| TIP122 | TIP127 | TO-220 | 100 | 5 | 65 | 1.9 (hFE 1000 @ 3 A) |
| TIP142 | TIP147 | TO-218 | 100 | 10 | 125 | 1.0 (hFE 1000 @ 5 A) |
| MJ11015 | MJ11016 | TO-3 | 120 | 30 | 200 | 0.9 (hFE 1000 @ 20 A; f_T 4 MHz) |
| MJ11032 | MJ11033 | TO-3 | 120 | 50 | 300 | 0.6 (hFE 1000 @ 25 A) |
| MJH11019 | MJH11020 | TO-218 | 200 (150 V and 250 V versions exist) | 15 | 150 | 0.8 (hFE 400 @ 10 A; f_T 3 MHz) |

Table notes (p.106): (b) with case at 25 C; (c) Pdiss(reality) = (Tj[your-max-value] - T_amb)/(R_thJC + R_thCS + R_thSA), much lower than the "spec," especially with a careful Tj max such as 100 C; (h) Pdiss(max) = (150 C - 25 C)/R_thJC is classic datasheet specsmanship. Consistency check: the Pdiss column equals ~125 C/R_thJC for Tj(max) = 150 C parts.

### 2.9 FET characteristics: manufacturing spread (p.139, §3.1.5)

| characteristic | available range | spread (same type) |
|---|---|---|
| IDSS, ID(on) | 1 mA to 500 A | x5 |
| RDS(on) | 0.001 ohm to 10k | x5 |
| gm @ 1 mA | 500-3000 uS | x5 |
| Vp (JFETs) | 0.5-10 V | 5 V |
| VGS(th) (MOSFETs) | 0.5-5 V | 2 V |
| BV_DS(off) | 6-1000 V | - |
| BV_GS(off) | 6-125 V | - |

Comparison anchors: 2N7000 VGS(th) spec 0.8-3 V at ID = 1 mA vs small npn VBE 0.63-0.83 V at Ic = 1 mA; 2N5457-59 measured VGS at 1 mA spreads ~1 V within a type vs 10-20 mV for BJTs (Fig 3.17).

### 2.10 FET formulas (Ch.3)

| quantity | formula (ASCII) | source |
|---|---|---|
| linear region | ID = 2*k*[(VGS - Vth)*VDS - VDS^2/2] | p.137 eq 3.1 |
| saturation region | ID = k*(VGS - Vth)^2; VDS(sat) ~ VGS - Vth | p.137 eq 3.2, 3.4 |
| CS amplifier | G = gm*RD (ideal); G = gm*RD/(1 + gos*RD) with output conductance; G = -RD/(RS + 1/gm) degenerated | p.146-148 eq 3.3; p.167 eq 3.13 |
| transconductance | gm = 2*k*(VGS - Vth) = 2*sqrt(k*ID); gm/gm0 = sqrt(ID/ID0) | p.147 eq 3.5, 3.6 |
| subthreshold | ID = I0*exp(VGS/(n*VT)), n ~ 1.05 (JFET) to 3; gm = ID/(n*VT) | p.166-168 eq 3.12 |
| source follower | G = gm*RL/(1 + gm*RL); r_out = 1/gm; with gos: G = 1/(1 + 1/(gm*RL) + 1/Gmax), Gmax = gm/gos | p.157 eq 3.7, 3.8; p.167 eq 3.14 |
| follower input capacitance | C_in = C_rss + C_stray + (1 - Gv)*C_iss | p.157 |
| variable resistor | r_DS ~ 1/[2*k*(VGS - Vth)]; r_DS = r0*(VG0 - Vth)/(VG - Vth); r_DS(lin) = 1/gm(sat) | p.161 eq 3.9-3.11 |
| f_T | f_T = gm/(2*pi*C_in) | p.166 fn58 |
| charge injection | Q = C_gc*[V_G(finish) - V_G(start)]; dV = Q/C_load | p.180 |
| switching time | t = Q_g/I_gate (Q_gd/I for output transition) | p.165 fn54; p.198 fn91 |
| switching losses | P_gate = Q_g*V_GS*f; P_Coss = C_oss*V_DS^2*f (as printed) | p.189 notes (s),(s2); p.199 |
| MOSFET ID(max) (datasheet) | ID(max) = sqrt(dT_JC/(R_thJC*R_DS(on)@Tjmax)), dT_JC = 150 C | p.199 §3.5.4D |
| hot MOSFET junction | Tj ~ T_A + I^2*m*R_on(25C)*R_thJA; m = 2 (<= 100 V), 2.5 (> 100 V) | p.216 eq 3.15 |
| heatsink-limited current | I = sqrt(P/R_on) | p.196 fn87 |
| gate leakage vs T | doubles every 10 C | p.163 |

### 2.11 Table 3.1 JFET mini-table (p.141) - n-channel; measured values at ID = 1 mA, VDS = 5 V

| part | IDSS (mA) | VGS(off) min (V) | VGS(off) max (V) | VGS @1 mA meas (V) | gm @1 mA meas (mS) | Gmax (V/V) | Crss typ (pF) | Ron typ (ohm) |
|---|---|---|---|---|---|---|---|---|
| 2N5484 | 1-5 | -0.3 | -3 | -0.73 | 2.3 | 180 | 1 | - |
| 2N5485 | 4-10 | -0.4 | -4 | -1.7 | 2.1 | 110 | 1 | - |
| 2N5486 | 8-20 | -2 | -6 | -2.4 | 2.1 | 50 | 1 | - |
| 2N5457 | 1-5 | -0.5 | -6 | -0.81 | 2.0 | 200 | 1.5 | - |
| 2N5458 | 2-9 | -1 | -7 | -2.3 | 2.3 | 170 | 1.5 | - |
| 2N5459 | 4-16 | -2 | -8 | -2.8 | 2.0 | 100 | 1.5 | - |
| BF862 | 10-25 | -0.3 | -1.2 | -0.40 | 12 | 250 | 1.9 | - |
| J309 | 12-30 | -1 | -4 | -1.6 | 4.2 | 300 | 2 | 50 (as printed) |
| J310 | 24-60 | -2 | -6.5 | -3.0 | 4.3 | 100 | 2 | 50 (as printed) |
| J113 | 2 min | -0.5 | -3 | -1.5 | 5.7 | 140 | 3 | 50 |
| J112 | 5 min | -1 | -5 | -3.3 | 5 | 100 | 3 | 30 |
| PN4393 | 5-30 | -0.5 | -3 | -0.83 | 6.2 | 100 | 3.5 | 100 |
| PN4392 | 25-75 | -2 | -5 | -2.6 | 5.4 | 130 | 3.5 | 60 |
| LSK170B | 6-12 | -0.2 | -2 | -0.09 | 11 | 160 | 5 | - |
| J110 | 10 min | -0.5 | -4 | -1.2 | 6.1 | 220 | 8 | 18 |
| J107 | 100 min | -0.5 | -4.5 | -2.6 | 8.2 | 340 | 35 | 8 |
| J105 | 500 min | -4.5 | -10 | -8.7 | 6.4 | 60 | 35 | 3 |
| IF3601 | 30 min | -0.04 | -3 | -0.24 | 27 | 1400 | 300 | - |

Notes: Gmax = gm/gos = maximum grounded-source gain into a current-source load, proportional to VDS (values at VDS = 5 V), roughly constant with ID. Crss/Ron columns reconstructed from OCR order (18 value pairs for 18 rows); verify against printed table. IF3601: e_n ~0.3 nV/rtHz with ~300 pF capacitance (p.142).

### 2.12 Current-regulator diodes 1N5283-1N5314 (p.143)

| characteristic | value |
|---|---|
| currents available | 0.22-4.7 mA |
| tolerance | +/-10 % |
| temperature coefficient | +/-0.4 %/C |
| voltage range | 1-2.5 V min, 100 V max |
| current regulation | 5 % typical |
| impedance | 1 Mohm typ (1 mA device) |

### 2.13 Table 3.2 Selected fast JFET-input op-amps (p.155)

| part | supply range (V) | Isupply typ (mA) | Ibias typ 25 C (pA) | e_n 1 kHz (nV/rtHz) | GBW typ (MHz) | slew typ (V/us) | cost qty 25 ($) |
|---|---|---|---|---|---|---|---|
| OPA604A | 9-50 | 5 | 50 | 10 | 20 | 25 | 2.93 |
| OPA827A | 8-40 | 5 | 15 | 4 | 22 | 28 | 9.00 |
| ADA4637 | 9-36 | 7 | 1 | 6 | 80 (decomp, G >= 7) | 170 | 10.12 |
| OPA656 | 9-13 | 14 | 2 | 7 (Cin 2.8 pF) | 230 | 290 | 5.59 |
| OPA657 | 9-13 | 14 | 2 | 7 | 1600 (decomp, G >= 7) | 700 | 10.01 |
| ADA4817 | 5-10.6 | 19 | 2 | 4 (Cin 1.5 pF) | 1050 | 870 | 4.93 |

### 2.14 Table 3.3 Analog switches (p.176) - partial (R_on typ at stated supply; Q_inj and C columns OCR-reconstructed)

| part | category | split supply (+/-V) | single supply (+V) | R_on typ (ohm) @ supply | Q_inj (pC) | C (pF) | comment |
|---|---|---|---|---|---|---|---|
| MAX4800-02 | HV 8:1 | - | 40-100 (as printed) | 22 @ +/-100 | 600 | 36 | really HV (Supertex HV2203) |
| MAX326-27 | HV | 5-18 | 10-30 | 1500 @ +/-15 | 2 | 6 | low leakage (1 pA typ) |
| MAX4508-09 | HV mux | 4.5-20 | 9-36 | 300 @ +/-15 | 2 | 28/22 | fault protected 0 V to +/-30 V |
| MAX354-55 | HV mux | 4.5-18 | 4.5-36 | 285 @ +/-15 | 80 | 28/14 | fault protected 0 V to +/-25 V |
| DG508-09 | HV mux | 5-20 | 10-36 | 180 @ +/-15 | 2 | 18/11 | low leakage |
| ADG1211-13 | HV | 5-15 | 10-? | 120 @ +/-15 | 0.3 | 2.6 | low C, low Q_inj |
| ADG1221-23 | HV | 5-16.5 | 5-16.5 | 120 @ +/-15 | 0.1 | 3 | low, flat Q_inj |
| AD7510-12DI | HV | 5-15 | - | 75 @ +/-15 | 30 | 17 | 0 V rails, +/-25 V fault |
| SW06 | HV JFET | 12-18 | - | 60 @ +/-15 | - | 15 | JFET, flat R_on |
| DG441-42 | HV | 4.5-22 | 5-24 | 50 @ +/-15 | 2 | 16 | 1 uA/supply |
| DG211-12 | HV | 4.5-22 | 5-22 | 45 @ +/-15 | 1 | 16 | also ADG211-12 |
| DG408-09 | HV mux | 5-20 | 5-30 | 40 @ +/-15 | 20 | 37/25 | also ADG408-09 |
| ADG417-19 | HV | 5-20 | 5-20 | 25 @ +/-15 | 3 | 30 | also DG417-19 |
| MAX317-19 | HV | 4.5-20 | 10-30 | 20 @ +/-15 | 3 | 30 | - |
| DG411-13 | HV | 4.5-20 | 10-30 | 17 @ +/-15 | 5 | 35 | also ADG411-13 |
| DG447-48 | HV | 4.5-20 | 7-36 | 13 @ +/-15 | 10 | 30 | - |
| ADG5412-13 | HV | 9-22 | 9-40 | 10 @ +/-15 | 240 | 60 | no latchup; 8 kV HBM ESD |
| DG467-68 | HV | 4.5-20 | 7-36 | 5 @ +/-15 | 21 | 76 | also ADG467-68 |
| DG4051-53 | mid mux | 2.5-5 | 2.7-12 | 66 @ +/-5 | 0.25 | 3.4 | - |
| 74HC4051-53 | mid mux | 2.5-5 | 2-10.5 | 40 @ +/-5 | 5 | 25 | - |
| MAX4541-44 | mid | - | 2.7-12 | 30 @ +5 | 1 | 13/20 | - |
| ISL5120-23 | mid | - | 2.7-12 | 19 @ +5 | 3 | 28 | - |
| ADG619/620 | mid SPDT | 2.7-5.5 | 2.7-5.5 | 7 @ +5 | 6 | 95 | ADG620 = make-before-break |
| ADG708-09 | LV mux | 2.5 | 1.8-5.5 | 3 @ +5 | 3 | 96/48 | - |
| ADG719 | LV SPDT | - | 1.8-5.5 | 2.5 @ +5 | - | 27 | 400 MHz (text) |
| MAX4624-25 | LV | - | 1.8-5.5 | 0.65 @ +5 | 65 | 100 | - |
| ADG884 | LV | - | 1.8-5.5 | 0.3 @ +5 | 125 | 300 | 0.4 ohm at +3 V; 400 mA |
| ISL43L110-11 | LV | - | 1.1-4.7 | 0.25 @ +3 | 72 | 160 | lowest R_on |
| MAX4565-67 | T-switch RF | 2.7-6 | 2.7-12 | 46 @ +/-5 | - | - | -3 dB @ 350 MHz, -90 dB xtalk @ 10 MHz |
| ADG918-19 | RF | - | 1.65-2.75 | - | - | - | -3 dB at 4 GHz, -30 dB xtalk at 4 GHz |
| AD75019 | 16x16 crosspoint | 4.5-12 | 9-25 | 150 @ +/-12 | - | - | - |

Notes (as printed): all CMOS except SW06; logic: T = TTL thresholds, VL = external logic supply, V+ = "CMOS" threshold depending on supply; SPDT are break-before-make unless noted.

### 2.15 Table 3.4a Small n-channel MOSFETs to 250 V (p.188) - n-channel column

| part | pkg | VDSS (V) | P_DC (W) | ID guideline (A) | RDS(on) max @ VGS | Qg (nC) | Ciss (pF) | cost ($, qty 100) |
|---|---|---|---|---|---|---|---|---|
| ZVN4424 | TO-92 | 240 | 0.7 | 0.3 | 4.3 ohm @ 2.5 V | 8 | 110 | 0.85 |
| BSP89 | SOT-223 | 240 | 1.5 | 0.4 | 2.8 ohm @ 10 V | - | 100 | 0.48 |
| ZVNL120 | TO-92 | 200 | 0.7 | 0.2 | 6 ohm @ 3 V | 2 | 55 | 0.53 |
| BS107A | TO-92 | 200 | 0.4 | 0.2 | 5 ohm @ 10 V | - | 60 | 0.31 |
| FQT4N20L | SOT-223 | 200 | 2.2 | 0.7 | 1.0 ohm @ 4.5 V | 4 | 240 | 0.34 |
| FQT7N10L | SOT-223 | 100 | 2 | 1.2 | 300 mohm @ 5 V | 4.6 | 220 | 0.37 |
| ZXMN10A08E | SOT-23 | 100 | 1.1 | 0.6 | 200 mohm @ 10 V | 7.8 | 500 | 0.57 |
| VN10KN3 | TO-92 | 60 | 0.7 | 0.2 | 6.6 ohm @ 5 V | 1.1 | 48 | 0.18 |
| 2N7000 | TO-92 | 60 | 0.4 | 0.2 | 2.5 ohm @ 5 V | 1 | 20 | 0.17 |
| 2N7002 | SOT-23 | 60 | 0.2 | 0.1 | 2.5 ohm @ 4.5 V | 0.9 | 20 | 0.16 |
| NDS7002A | SOT-23 | 60 | 0.36 | 0.20 | 1.3 ohm @ 4.5 V | 0.8 | 80 | 0.27 |
| BSS138 | SOT-23 | 50 | 0.36 | 0.25 | 1.0 ohm @ 4.5 V | 0.95 | 27 | 0.15 |
| ZVN2106A | TO-92 | 60 | 0.7 | 0.3 | 800 mohm @ 10 V | 1.5 | 75 | 0.49 |
| ZVN4306A | TO-92 | 60 | 0.85 | 1.0 | 320 mohm @ 5 V | 3.5 | 350 | 1.11 |
| NDT3055 | SOT-223 | 60 | 3 | 1.7 | 84 mohm @ 10 V | 9 | 250 | 0.34 |
| IRF7470 | SO-8 | 40 | 1.0 | 7 | 10 mohm @ 4.5 V | 29 | 3400 | 0.76 |
| FDV303N | SOT-23 | 25 | 0.35 | 0.4 | 330 mohm @ 2.7 V | 1.1 | 50 | 0.23 |
| IRLML2030 | SOT-23 | 30 | 1.3 | 0.9 | 123 mohm @ 4.5 V | 1 | 110 | 0.25 |
| FDN337N | SOT-23 | 30 | 0.5 | 1.3 (z) | 70 mohm @ 2.5 V | 4.2 | 300 | 0.16 |
| NTR4170N | SOT-23 | 30 | 0.8 | 2 | 50 mohm @ 4.5 V | 4.8 | 430 | 0.12 |
| IRLML0030 | SOT-23 | 30 | 1.3 | 2 (u) | 33 mohm @ 4.5 V | 2.6 | 380 | 0.18 |
| IRF7807Z | SO-8 | 30 | 2.5 | 10 | 14.5 mohm @ 4.5 V | 7.2 | 770 | 0.61 |
| FDS8817NZ | SO-8 | 30 | 2.5 | 10 | 7 mohm @ 4.5 V | 17 | 1800 | 0.75 |
| FDG327NZ | SC70-6 | 20 | 0.42 | 1.2 | 90 mohm @ 1.8 V | 2.1 | 410 | 0.40 |
| IRLML2502 | SOT-23 | 20 | 1.25 | 1.25 | 50 mohm @ 2.5 V | 5 | 740 | 0.30 |
| Si2312CDS | SOT-23 | 20 | 0.8 | 2 (u) | 35 mohm @ 1.8 V | 3.8 | 870 | 0.28 |
| IRF6201 | SO-8 | 20 | 2.5 | 15 | 2.1 mohm @ 2.5 V | 130 | 8600 | 1.06 |

Table notes (p.188): (c) Pdiss for T_case = 25 C; (r) RDS typ for Tj = 25 C, multiply by 1.5 if hot; (s) total gate charge to VGS, switching loss = Qg*VGS*f; (u) with 6 cm^2 PCB copper; (v) with 0.4 cm^2 PCB copper; (y) ID is a guideline conservative estimate, saturated switch at VGS, T_case = 70 C; (z) with 2-5 cm^2 PCB copper, add heatsink for higher current. Usage: R_thJC = 125 C/P_D and Tj = T_A + P_D*(R_thJC + R_th,heatsink path). The p-channel column of Table 3.4a and the numeric columns of Table 3.4b (n-channel 55 V-4.5 kV) were too OCR-scrambled to transcribe; Table 3.4b notes: RDS(on) hot scaling 1.5-2x (low-V) or 2.2-3.5x (high-V); ID(max) at T_C = 25 C "manifestly impossible"; part-number scheme e.g. 10N60 = 10 A, n-channel, 600 V; SiC MOSFETs have lower capacitance but need higher gate voltage; 500 V parts largely superseded by 600 V; older large-die parts often better for linear power dissipation.

### 2.16 BJT-MOSFET-IGBT switch comparison (p.202, §3.5.5)

| class | part | type | V_sat @25 C (V) | V_sat @125 C (V) | C_rb (pF) | price ($) |
|---|---|---|---|---|---|---|
| 60 V, 0.5 A | 2N4401 | npn | 0.75 | 0.8 | 8 | 0.06 |
| 60 V, 0.5 A | 2N7000 | nMOS | 0.6 | 0.95 | 25 | 0.09 |
| 60 V, 6 A | TIP42A | pnp (as printed "N") | 1.5 | 1.7 | 50 | 0.63 |
| 60 V, 6 A | IRFZ34E | nMOS | 0.25 | 0.43 | 50 | 1.03 |
| 100 V, 10 A | TIP142 | Darlington | 3.0 | 3.8 | low | 1.11 |
| 100 V, 10 A | IRF540N | nMOS | 0.44 | 1.0 | 40 | 0.98 |
| 400 V, 10 A | 2N6547 | npn | 1.5 | 2.5 | 125 | 2.89 |
| 400 V, 10 A | FQA30N40 | nMOS | 1.4 | 3.2 | 60 | 3.85 |
| 600 V, 10 A | STGP10NC60 | IGBT | 1.75 | 1.65 | 12 | 0.86 |

Conditions: Ib = Ic/10 (Ic/250 for Darlington), VGS = 10 V.

### 2.17 1 kV-class switch comparison (p.208, §3.5.7A)

| type | part | V_max | I_max dc / pulse | R_on typ 25 C / 150 C | V_ON @15 A 25 C / 150 C |
|---|---|---|---|---|---|
| MOSFET | IRFPG50 | 1000 V | 6.1 A / 24 A | 1.5 ohm / 4 ohm | 23 V / 60 V |
| IGBT | IRG4PH50S | 1200 V | 57 A / 114 A | - | 1.2 V / 1.2 V |
| BJT | TT2202 | 1500 V | 10 A / 25 A | - | 1 V / 1 V (at 8 A) |

All ~$5, TO-247, input capacitance 2.8-3.6 nF, driven at +15 V.

### 2.18 Typical electrostatic voltages (p.200, adapted from Motorola Power MOSFET Data Book)

| action | 10-20 % humidity (V) | 65-90 % humidity (V) |
|---|---|---|
| walk on carpet | 35,000 | 1,500 |
| walk on vinyl floor | 12,000 | 250 |
| work at bench | 6,000 | 100 |
| handle vinyl envelope | 7,000 | 600 |
| pick up poly bag | 20,000 | 1,200 |
| shift position on foam chair | 18,000 | 1,500 |

ESD models: HBM = 100 pF + 1.5 kohm (2.5 kV -> 1.7 A peak, 150 ns); machine model several cycles of 12 kHz up to 6 A; CDM 6 A, 2 ns pulses (p.200 fn97).

### 2.19 Table 3.7 JFETs (p.217) - key columns (OCR-reconstructed; BV_GSS, IDSS range, IDSS measured, R_on, VGS(off) range)

| part | ch | BV_GSS (V) | IDSS min-max (mA) | IDSS meas (mA) | R_on max (ohm) | VGS(off) min to max (V) |
|---|---|---|---|---|---|---|
| PN4117 | N | 40 | 0.03-0.09 | 0.07 | - | -0.6 to -1.8 |
| PN4118 | N | 40 | 0.08-0.24 | 0.20 | - | -1 to -3 |
| PN4119 | N | 40 | 0.20-0.60 | 0.30 | - | -2 to -6 |
| 2N5457 | N | 25 | 1-5 | 3.5 | - | -0.5 to -6 |
| 2N5458 | N | 25 | 2-9 | 4.1 | - | -1 to -7 |
| 2N5459 | N | 25 | 4-16 | 9.9 | - | -2 to -8 |
| 2N5460 | P | 25 | 1-5 | 3.4 | - | +0.75 to +6 |
| 2N5461 | P | 25 | 2-9 | 2.7 | - | +1 to +7.5 |
| 2N5462 | P | 25 | 4-16 | 5.9 | - | +1.8 to +9 |
| MMBF4416 | N | 30 | 5-15 | 5.9 | - | to -6 |
| 2N5484 | N | 25 | 1-5 | 3.3 | - | -0.3 to -3 |
| 2N5485 | N | 25 | 4-10 | 6.6 | - | -0.5 to -4 |
| 2N5486 | N | 25 | 8-20 | 14 | - | -2 to -6 |
| 2SK170BL | N | 40 | 6-12 | 6.1 | - | -0.2 to -1.5 |
| LSK170B | N | 40 | 6-12 | 7.6 | - | -0.2 to -2 |
| LSK170C | N | 40 | 10-20 | 13 | - | -0.2 to -2 |
| BF861B | N | 25 | 6-15 | 8 | - | -0.5 to -1.5 |
| BF545C | N | 30 | 12-25 | 19 | - | -3.2 to -7.8 |
| BF862 | N | 20 | 10-25 | 12 | - | -0.3 to -1.2 |
| PF5103 | N | 40 | 10-40 | 19 | 30 | -1.2 to -2.7 |
| PN4391 | N | 40 | 50-150 | 115 | 30 | -4 to -10 |
| PN4392 | N | 40 | 25-75 | 38 | 60 | -2 to -5 |
| PN4393 | N | 40 | 5-30 | 16 | 100 | -0.5 to -3 |
| J105 | N | 25 | >= 500 | - | 3 | -4.5 to -10 |
| J106 | N | 25 | >= 200 | - | 6 | -2 to -6 |
| J107 | N | 25 | >= 100 | - | 8 | -0.5 to -4.5 |
| J108 | N | 25 | >= 80 | 325 | 8 | -3 to -10 |
| J109 | N | 25 | >= 40 | 201 | 12 | -2 to -6 |
| J110 | N | 25 | >= 10 | 122 | 18 | -0.5 to -4 |
| J111 | N | 35 | >= 20 | 115 | 30 | -3 to -10 |
| J112 | N | 35 | >= 5 | 47 | 50 | -1 to -5 |
| J113 | N | 35 | >= 2 | 21 | 100 | -0.5 to -3 |
| J174 | P | 30 | 20-135 | 26 | 85 | +5 to +10 |
| J175 | P | 30 | 7-60 | 13 | 125 | +3 to +6 |
| J176 | P | 30 | 2-25 | 6.1 | 250 | +1 to +4 |
| J177 | P | 30 | 1.5-20 | 4.2 | 300 | +0.8 to +2.5 |
| J308 | N | 25 | 12-60 | 35 | - | -1 to -6.5 |
| J309 | N | 25 | 12-30 | 23 | - | -1 to -4 |
| J310 | N | 25 | 24-60 | 39 | - | -2 to -6.5 |
| LSK389A (dual) | N | 40 | 2.6-6.5 | - | - | -0.15 to -2 |
| LSK389B (dual) | N | 40 | 6-12 | - | - | -0.15 to -2 |
| LSK389C (dual) | N | 40 | 10-20 | - | - | -0.15 to -2 |

Table notes: VGS(off) usually specified at ID = 1 nA or 10 nA (sometimes 10 pA or 200 pA for J105-J113 switches); all JFETs appear source/drain symmetric; Gmax = gm/gos measured at ID = 1 mA, VDS = 5 V; gos = gm/Gmax.

### 2.20 Table 3.8 Low-side MOSFET gate drivers (p.218) - partial (supply range, peak output, typical speed)

| part | mfr | V_min-V_max (V) | I_pk (A) | speed typ (ns) |
|---|---|---|---|---|
| TC4426-28 | Microchip | 4.5-18 | 1.5 | 55 |
| TC4423-25 | Microchip | 4.5-18 | 3 | 70 |
| TC4420/29 | Microchip | 4.5-18 | 6 | 80 |
| TC4421-22 | Microchip | 4.5-18 | 9 | 85 |
| FAN3111 | Fairchild | 4.5-18 | 1 | 20 |
| FAN3100C/T | Fairchild | 4.5-18 | 2 | 20 |
| FAN3121-22 | Fairchild | 4.5-18 | 9 | 21 |
| MAX17600-05 | Maxim | 4-14 | 4 | 15 |
| MAX5048A/B | Maxim | 4-12.6 | 7.6 sink / 1.3 source | 18 |
| UCC27517 | TI | 4.7-20 | 4 | 17 |
| UCC27523-26 | TI | 4.7-20 | 5 | 17 |
| LM5114 | TI | 4-12.6 | 7.6 sink / 1.3 source | 16 |
| MC34151 | ON | 6.5-18 | 1.5 | 50 |
| IR2121 | IR | 12-18 | 1 source / 2 sink | 200 |
| UC3708 | TI | 5-35 | 3 | 37 |
| IXDD604 | IXYS | 4.5-35 | 4 | 40 |
| IXDD614 | IXYS | 4.5-35 | 14 | 70 |
| IXDD630 | IXYS | 10-35 | 30 | 65 |
| ZXGD3002-04 | Diodes | 20/40 | 9/5 | 11 |

Notes: speed into C_load at V_S = 12 V (load column not reliably recovered); 37xxx = 0-70 C, 27xxx = -40 to 105 C; all except ZXGD3000-series swing (nearly) rail to rail.

### 2.21 Table 4.1 Op-amp parameters: typical ("jellybean") vs best available per parameter ("premium") (p.245)

| parameter | BJT jellybean | BJT premium | JFET jellybean | JFET premium | CMOS jellybean | CMOS premium | units |
|---|---|---|---|---|---|---|---|
| V_os (max) | 3 | 0.025 | 2 | 0.1 | 2 | 0.1 | mV |
| TCV_os (max) | 5 | 0.1 | 20 | 1 | 10 | 3 | uV/C |
| I_B (typ, 25 C) | 50 nA | 25 pA | 50 pA | 40 fA | 1 pA | 2 fA | - |
| e_n (typ, 1 kHz) | 10 | 1 | 20 | 3 | 30 | 7 | nV/rtHz |
| f_T (typ) | 2 | 2000 | 5 | 400 | 2 | 10 | MHz |
| SR (typ) | 2 | 4000 | 15 | 300 | 5 | 10 | V/us |
| V_s min (total) | 5 | 1.5 | 10 | 5 | 2 | 1 | V |
| V_s max (total) | 36 | 44 | 36 | 36 | 15 | 15 | V |

Premium values are the best available for each individual parameter; no single op-amp has all premium values ("engineering is the art of compromise").

### 2.22 Table 4.2b Monolithic power and high-voltage op-amps (p.272) - partial (OCR-reconstructed; verify)

| part | mfr | total supply min-max (V) | I_Q typ (mA) | f_T (MHz) | slew (V/us) | I_out max (A) |
|---|---|---|---|---|---|---|
| AD8010 | Analog | 10-12.6 | 16 | 230 | 800 | 0.2 |
| LM6171 | TI | 5-36 | 2.5 | 100 | 3000 | 0.12 |
| LTC2057HV | LTC | 4.8-65 | 0.8 | 1.5 | 0.45 | 0.02 |
| ADA4700 | Analog | 10-100 | 1.7 | 3.5 | 20 | 0.03 |
| OPA445 | TI | 20-100 | 4.2 | 2 | 10 | 0.015 |
| OPA454 | TI | 10-100 | 3.2 | 2.5 | 13 | 0.12 |
| LTC6090 | LTC | 9.5-140 | 2.8 | 12 | 21 | 0.05 |
| THS3120 | TI | 9-33 | 7 | 130 | 900 | 0.47 |
| LT1210 | LTC | 8-36 | 35 | 35 | 900 | 2 (CFB) |
| L272 | - | 4-40 | 8 | 0.35 | 1 | 1 |
| LM1875 | TI | 16-60 | 70 | 5.5 | 8 | 4 |
| OPA548 | TI | 8-60 | 17 | 1 | 10 | 3 |
| OPA549 | TI | 8-60 | 26 | 0.9 | 9 | 8 |
| OPA541 | TI | 20-80 | 20 | 2 | 10 | 10 |
| LM3886 | TI | 18-84 | 50 | 8 | 19 | 11.5 |
| PA340 | Apex | 20-350 | 2.2 | 10 | 32 | 0.06 |
| PA90 | Apex | 30-400 | 10 | 100 | 300 | 0.2 |
| PA98 | Apex | 30-450 | 21 | 100 | 1000 | 0.2 |
| PA97 | Apex | 100-900 | 0.6 | 1 | 8 | 0.01 |

Notes (p.272): Pdiss with case at 50 C based on R_thJC; (n) "provided you can get the heat out of the package"; Apex parts are hybrids (unit prices ~$176-272). Table 4.2a (representative op-amps) columns were too OCR-scrambled to transcribe; its comment column names: LM358/324 single-supply jellybean; LT1013/1014 precision single-supply; LMC6482 CMOS jellybean; LMC6041/42 micropower; TLV2401 pico-power (operates to Vcc + 5 V); LF411/412 JFET; LF347B low-cost JFET; OPA727/OPA376 e-trim CMOS; OPA129 electrometer; LT1012 low-I_B bipolar; LTC1050 chopper; LT1637 over-the-top (Vin to V_EE + 44 V); LT1097 C-load stable, comp pin; OPA177 improved OP-07; OPA277 improved OP-27; LM6132 early RRIO; AD797 low distortion/low noise; OPA627 low-noise JFET; OPA657 fast JFET; OPA454 high voltage; THS4011 fast VFB.

### 2.23 Op-amp formulas (Ch.4)

| quantity | formula (ASCII) | source |
|---|---|---|
| inverting gain | G = -R2/R1; Z_in = R1 | p.225 eq 4.1 |
| noninverting gain | G = 1 + R2/R1 | p.226 eq 4.2 |
| closed-loop (finite A) | G = A/(1 + A*B), B = R1/(R1 + R2); inverting G = -A*(1 - B)/(1 + A*B) | p.250-251 eq 4.5 |
| integrator | Vout = -(1/(R*C))*integral(Vin dt); ramp dV/dt = -Vin/(R*C) or -I/C | p.230 eq 4.3 |
| integrator drift | dVout/dt = (I_B + V_os/R)/C | p.258 |
| differentiator | Vout = -R*C*dVin/dt | p.260 eq 4.7 |
| triangle oscillator | f = R3/(4*R1*C1*R2) | p.240 eq 4.4 |
| slew rate | SR_min = 2*pi*f*A; App_max = SR/(pi*f) | p.251 eq 4.6 |
| closed-loop bandwidth | BW_CL ~ f_T/G_CL; A(f) ~ j*f_T/f | p.250 fn26; p.290 |
| output impedance | Z_out = r_o/(1 + AB); L_out ~ r_o*G_CL/(2*pi*f_T) | p.250 Fig 4.53 |
| current source Z_out | Z_out(f) ~ R_o*f_T/f; C_eff = I_out/SR | p.254 §4.4.4 |
| offset error | dVout = (1 + R2/R1)*V_os | p.251 |
| bias-current error | dVout = I_B*R2 (unbalanced); G*I_os*R_source (balanced) | p.252 |
| peak detector | droop = I_B/C; follow rate = I_out/C | p.255 |
| Schmitt hysteresis | dV = V_swing*R_p/(R_p + R3), R_p = R1 parallel R2 | p.237 |
| current noise | i_n = sqrt(2*q*I_B); r_n = e_n/i_n | p.290 |

### 2.24 Table 5.1 Millivoltmeter candidate op-amps (p.296) - need V_os <= 100 uV, I_B <= 10 pA, V_S min <= 1.8 V

| part | input | V_os typ / max (uV) | I_bias typ / max (pA) | output | V_S total min-max (V) | I_S typ (uA) | price ($, 100 pc) | note |
|---|---|---|---|---|---|---|---|---|
| uA741 | BJT | 2000 / 6000 | 80k / 500k | 1.5 V from rails | 10-40 | 1500 | 0.27 | old HV BJT |
| LF411 | JFET | 800 / 2000 | 50 / 200 | 1.5 V from rails | 10-40 | 1800 | 0.88 | HV JFET |
| LM358A | BJT | 2000 / 3000 | 45k / 100k | 0 to V+ - 1.2 V | 3-32 | 500 | 0.21 | old HV single-supply |
| LPV521 | CMOS | 100 / 1000 | 0.01 / 1 | R-R | 1.8-5.5 | 0.5 | 1.05 | low-bias LV RRIO |
| OPA336 | CMOS | 60 / 125 | 1 / 10 | R-R | 2.3-5.5 | 20 | 1.70 | Ch.4 "solution" |
| ADA4051 | CMOS AZ | 2 / 17 | 5 / 50 | R-R | 1.8-5 | 15 | 2.20 | LV auto-zero RRIO |
| LTC6078 | CMOS | 7 / 25 | 0.2 / 1 | R-R | 2.7-5.5 | 110 | 1.75 | dual, low-I_B low-V_os |
| AD8603 | CMOS | 12 / 50 | 0.2 / 1 | R-R | 1.8-5 | 40 | 1.40 | chosen; I_B 50 pA max at 85 C |
| circuit limit | - | <= 100 | <= 10 | 0 to anything | 1.8 to > 3.6 | - | - | each term budgeted |

### 2.25 Table 5.3 Eight low-input-current op-amps (p.303)

| part | type | V_total (V) | I_Q (uA) | I_in typ / max @25 C (pA) | V_os max (uV) | TCV_os typ / max (uV/C) |
|---|---|---|---|---|---|---|
| OPA277P | bipolar | 10-36 | 790 | 500 / 1000 | 20 | 0.1 / 0.15 |
| LT1012AC | superbeta | 8-40 | 370 | 25 / 100 | 25 | 0.2 / 0.6 |
| AD706 | superbeta | 4-36 | 750 | 50 / 200 | 100 | 0.2 / 1.5 |
| OPA124PB | JFET | 10-36 | 2500 | 0.35 / 1 | 250 | 1 / 2 |
| OPA129B | JFET | 10-36 | 1200 | 0.03 / 0.1 | 2000 | 3 / 10 |
| MAX9945 | MOSFET | 4.8-40 | 400 | 0.05 / - | 5000 | 2 / - |
| LMP7721 | CMOS LV | 1.8-6 | 1300 | 0.003 / 0.02 | 150 | 1.5 / 4 |
| LMC6001A | CMOS LV | 5-16 | 450 | 0.01 / 0.025 | 350 | 2.5 / 10 |

### 2.26 Table 5.2 Representative precision op-amps (p.302) - reconstructed

| part | type | supply (V) | I_Q/amp (mA) | I_B typ / max | V_os typ / max (uV) | drift typ (uV/C) | CMRR min (dB) | e_n 1 kHz (nV/rtHz) | GBW (MHz) | slew (V/us) | comment |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LT1077A | BJT | 2.2-44 | 0.05 | 7 / 9 nA | 9 / 40 | 0.4 | 97 | 27 | 0.23 | 0.08 | single-supply |
| LT1013 | BJT | 3.4-44 | 0.35 | 12 / 20 nA | 40 / 150 | 0.4 | 100 | 22 | 0.7 | 0.4 | single-supply |
| OPA277P | BJT | 4-36 | 0.79 | 0.5 / 1 nA | 10 / 20 | 0.1 | 130 | 8 | 1 | 0.8 | improved OP-27 |
| LT1012AC | superbeta | 8-40 | 0.37 | 25 pA / 0.1 nA | 8 / 25 | 0.2 | 114 | 14 | 0.5 | 0.2 | comp pin |
| LT1677 | BJT | 3-44 | 2.8 | 2 / 20 nA | 20 / 60 | 0.4 | 109 | 3.2 | 7.2 | 2.5 | or AD8675 (0.5 nA) |
| LT1468 | BJT | 7-36 | 3.9 | 3 / 10 nA | 30 / 75 | 0.7 | 96 | 5 | 90 | 23 | 0.7 ppm distortion |
| LF412A (not precision) | JFET | 12-44 | 1.8 | 50 / 200 pA | 500 / 1000 | - | 80 | 25 | 4 | 15 | comparison |
| OPA827 | JFET | 8-40 | 4.8 | 15 / 50 pA | 75 / 150 | 1.5 | 104 | 3.8 | 22 | 28 | 0.25 uVpp 0.1-10 Hz |
| LMC6482A (not precision) | CMOS | 3-16 | 0.5 | 0.02 / 4 pA | 110 / 750 | 1 | 70 | 37 | 1.5 | 1.3 | comparison |
| MAX4236A | CMOS | 2.4-6 | 0.35 | 1 / 500 pA (as read) | 5 / 20 | 0.6 | 84 | 14 | 1.7 | 0.3 | shdn; '37 decomp |
| OPA376 | CMOS | 2.2-7 | 0.76 | 0.2 / 10 pA | 5 / 25 | 0.26 | 76 | 7.5 | 5.5 | 2 | e-trim |
| AD8628 | CMOS auto-zero | 2.7-6 | 0.85 | 30 / 100 pA | 1 / 5 | 0.002 | 120 | 22 | 2.5 | 1 | SOIC-8, SOT23-5 |

### 2.27 Table 5.4 Representative high-speed op-amps (p.310) - partial, reconstructed

| part | type | supply (V) | I_Q (mA) | I_in typ | V_os typ / max (mV) | e_n (nV/rtHz) | GBW (MHz) | slew (V/us) | I_out (mA) | comment |
|---|---|---|---|---|---|---|---|---|---|---|
| LT1468 | BJT | 7-36 | 3.9 | 3 nA | 0.03 / 0.08 | 5 | 90 | 23 | 22 | 0.7 ppm distortion |
| LT1360 | BJT | 5-36 | 4 | 0.3 uA (as read) | 0.3 / 1 | 9 | 50 | 800 | 34 | C-load stable |
| LM6171 | BJT | 5-36 | 2.5 | 1 uA | 1.5 / 3 | 12 | 100 | 3600 | 90 | VFB+CFB |
| OPA604A | JFET | 9-50 | 5.3 | 50 pA | 1 / 5 | 10 | 20 | 25 | 36 | 3 ppm distortion |
| OPA827A | JFET | 8-40 | 4.8 | 15 pA | 0.08 / 0.15 | 3.8 | 22 | 28 | 30 | quiet, accurate |
| ADA4637 | JFET | 9-36 | 7.0 | 1 pA | 0.12 / 0.3 | 6.1 | 80 | 170 | 45 | decomp G > 7 |
| LMH6723 | BJT LV | 4.5-13 | 1 | 2 uA | 1 / 3 | 4.3 | 370 | 600 | 110 | CFB |
| ADA4851 | BJT LV | 3-12.6 | 2.5 | 2.2 uA | 0.6 / 3.4 | 10 | 125 | 200 | 85 | shdn |
| LT1818 | BJT LV | 4-12.6 | 9 | 2 uA | 0.2 / 1.5 | 6 | 400 | 2500 | 70 | VFB+CFB |
| LT6200 | BJT LV | 3-12.6 | 16.5 | 10 uA | 0.2 / 1.2 | 0.95 | 165 | 50 | 70 | 1 % distortion at 50 MHz |
| LT6200-10 | BJT LV | 3-12.6 | 16.5 | 10 uA | 0.2 / 1.2 | 0.95 | 1600 | 450 | 70 | fastest RRIO (decomp) |
| OPA656 | JFET LV | 9-13 | 14 | 2 pA | 0.25 / 1.8 | 7 | 230 | 290 | 50 | low e_n*C_in noise |
| ADA4817 | JFET LV | 5-10.6 | 19 | 2 pA | 0.4 / 2 | 4 | 1050 | 870 | 70 | lowest e_n*C_in |
| AD8616 | CMOS | 2.7-6 | 1.7 | 0.2 pA | 0.02 / 0.06 | 7 | 24 | 12 | 150 | - |
| LMP7717 | CMOS | 1.8-6 | 1.15 | 0.05 pA | 0.01 / 0.15 | 6.2 | 88 | 28 | 15 sink / 47 source | decomp G > 10 |
| OPA350 | CMOS | 2.5-7 | 5.2 | 0.5 pA | 0.15 / 0.5 | 7 | 38 | 22 | 40 | 6 ppm distortion |

### 2.28 Autonulling amplifier error budget (Fig 5.3), worst case at 25 C referred to input (p.299)

| stage | item | value |
|---|---|---|
| x100 in-amp LT1167A | offset / noise 0.1-10 Hz / temperature / supply / I_os x R_s | 40 uV / 0.28 uVpp typ / 0.3 uV/C / 28 nV per 100 mV / 0.11 uV per 350 ohm |
| x10 gain OPA277 | offset / temperature / time / supply / bias / load heating | 0.5 uV / 10 nV/C / 2 nV/month typ / 1 nV per 100 mV / 0.3 uV / 5 nV (5 mW, 0.1 C/mW) |
| output amp OPA277 | offset / temperature / time / supply / bias / load heating | 50 nV / 1 nV/C / 0.2 nV/month / 0.1 nV per 100 mV / 30 nV / 5 nV (1k load) |
| hold amp OPA129 | offset tempco / supply / capacitor droop / charge transfer | 10 nV/C / 10 nV per 100 mV / 0.4 uV/min / 1.1 nV |
| current errors into C1 | cap leakage max uncompensated / typical compensated / U4 input / nulled V_os/R10 / relay OFF leakage / PCB leakage | 100 pA / 10 pA / 0.25 pA / 0.1 pA / 10 pA (1 pA typ) / 5.0 pA |

### 2.29 Resistor stability comparison (p.300)

| effect | RN55C 1 % metal film | Allen-Bradley CB 5 % carbon composition |
|---|---|---|
| tempco | 50 ppm/C (-55 to +175 C) | 3.3 % over 25-85 C |
| soldering / temperature / load cycling | 0.25 % | +4 %, -6 % |
| shock and vibration | 0.1 % | +/-2 % |
| moisture | 0.5 % | +6 % |

Precision grades: Susumu RG to 0.02 %, 5 ppm/C; Vishay MPM 0.05 % abs, 0.01 % match, 25 ppm/C abs, 2 ppm/C tracking; Vishay Bulk Metal Foil 0.005 % abs, 0.001 % match, 0.2 ppm/C abs, 0.1 ppm/C tracking.

### 2.30 Low-frequency gain nonlinearity, 4 kohm load (p.314, after Pease AN-1485)

| part | class | nonlinearity | cause/comment |
|---|---|---|---|
| LM8262 | HV BJT (+/-10 V) | 12 ppm | crossover distortion |
| LM358 | HV BJT | 1 ppm | asymmetric output stage |
| LF411 | HV BJT/JFET | 1.4 ppm | poor layout - thermal |
| LF412 | HV JFET | 0.3 ppm | better layout |
| LM4562 | HV BJT | 0.025 ppm | pro-audio, G_OL = 1e7 |
| LMC6482 | CMOS RRO (+/-4 V) | 1.1 ppm | jellybean |
| LMC6062 | CMOS RRO | 0.2 ppm | precision |
| LMP2012 | CMOS auto-zero (+/-2 V) | 0.2 ppm | precision |

### 2.31 Phase shift vs frequency, G = 10 (p.315); f_T0 = op-amp GBW

| f | single stage G = 10 | 2 stages G = sqrt(10) each | active compensation | single stage, f_T = 10*f_T0 |
|---|---|---|---|---|
| 0.001 f_T0 | -0.57 deg | -0.36 deg | -0.00006 deg | -0.057 deg (computed; OCR "-0.006") |
| 0.003 f_T0 | -1.7 deg | -1.1 deg | -0.0015 deg | -0.17 deg |
| 0.01 f_T0 | -5.7 deg | -3.6 deg | -0.06 deg | -0.57 deg |
| 0.03 f_T0 | -17.2 deg | -10.9 deg | -1.5 deg | -1.7 deg |
| 0.1 f_T0 | -45 deg | (not legible) | -45 deg | -5.7 deg |

### 2.32 Table 5.5 "Seven" precision op-amps, HV bipolar and superbeta sections (p.320) - reconstructed; this table straddles the part-1/part-2 boundary (file lines 18845-19353)

| part | supply (V) | I_Q (mA) | I_B typ / max | V_os typ / max (uV) | drift typ / max (uV/C) | CMRR min (dB) | noise 0.1-10 Hz (uVpp) | e_n 1 kHz (nV/rtHz) | i_n 1 kHz (fA/rtHz) | GBW (MHz) | slew (V/us) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LT1077A | 2.2-44 | 0.05 | 7 / 9 nA | 9 / 40 | 0.4 / 1.6 | 97 | 0.5 | 27 | 65 | 0.23 | 0.08 |
| LT1490A | 2.5-44 | 0.04 | 1 / 8 nA | 110 / 500 | 2 / 4 | 84 | 1 | 50 | 15 | 0.2 | 0.07 |
| AD8622A | 4-36 | 0.22 | 45 / 200 nA (as read) | 10 / 125 | 0.5 / 1.2 | 125 | 0.2 | 11 | 150 | 0.56 | 0.48 |
| LT1013 | 3.4-44 | 0.35 | 12 / 20 nA | 40 / 150 | 0.4 / 2 | 100 | 0.55 | 22 | 70 | 0.7 | 0.4 |
| OPA277 | 4-36 | 0.79 | 0.5 / 1 nA | 10 / 20 | 0.1 / 0.15 | 130 | 0.22 | 8 | 200 | 1 | 0.8 |
| TLE2141A | 4-44 | 3.5 | 0.7 / 1.5 uA | 175 / 500 | 1.7 / - | 85 | 0.5 | 10.5 | 1900 | 5.9 | 45 |
| LT1677 | 3-44 | 2.8 | 2 / 20 nA | 20 / 60 | 0.4 / 2 | 109 | 0.09 | 3.2 | 1200 | 7.2 | 2.5 |
| AD8675 | 9-36 | 2.5 | 0.5 / 2 nA | 10 / 75 | 0.2 / 0.6 | 114 | 0.1 | 2.8 | 300 | 10 | 2.5 |
| OPA2209 | 4.5-40 | 2.2 | 1 / 4.5 nA | 35 / 150 | 1 / 3 | 120 | 0.13 | 2.2 | 500 | 18 | 6.4 |
| LT1007 | 4-44 | 2.7 | 10 / 35 nA | 10 / 25 | 0.2 / 0.6 | 117 | 0.06 | 2.5 | 400 | 8 | 2.5 |
| ADA4004 | 9-36 | 2.2 | 40 / 90 nA | 40 / 125 | 0.7 / 1 | 110 | 0.15 | 1.8 | 3500 | 12 | 2.7 |
| AD8597 | 9-36 | 4.8 | 40 / 210 nA | 10 / 120 | 0.8 / 2.2 | 120 | 0.08 | 1.1 | 4300 | 10 | 16 |
| LT1028A | 8-44 | 7.4 | 25 / 90 nA | 10 / 40 | 0.2 / 0.8 | 108 | 0.04 | 0.85 | 4700 | 75 | 15 |
| LT6010A (superbeta) | 2.7-40 | 0.14 | 20 / 110 pA | 10 / 35 | 0.2 / 0.8 | 107 | 0.4 | 14 | 100 | 0.35 | 0.11 |
| LT1012AC (superbeta) | 2.4-40 | 0.37 | 25 / 100 pA | 8 / 25 | 0.2 / 0.6 | 114 | 0.5 | 14 | (20) | 0.5 | 0.2 |
| OP97E (superbeta) | 4.5-40 | 0.40 | 30 / 100 pA | 10 / 25 | 0.2 / 0.6 | 114 | 0.5 | 14 | (20) | 0.9 | 0.2 |
| AD706 (superbeta) | 4-36 | 0.8 | 50 / 200 pA | 30 / 100 | 0.2 / 1.5 | 106 | 0.5 | 15 | 50 | 0.8 | - |
| LT1884A (superbeta) | 3.5-40 | 0.85 | 150 / 400 pA | 25 / 50 | 0.3 / 0.8 | 114 | 0.4 | 9.5 | 50 | 2 | 0.9 |

Table 5.5 note (o): values in parentheses should not be relied upon; measured values are often 5x-100x larger (Ch.8). The JFET, CMOS and chopper sections of Table 5.5 were too scrambled to transcribe reliably (part 2 covers them from line 19000).

## 3. Mechanizable checks

Each check lists: inputs (columns, units) -> formula -> pass criterion -> margin definition -> source rows. Thresholds quoted as "book" come directly from the text; thresholds marked "user" must be supplied by the design spec (the book gives no number).

- `CHECK-resistor-power`: R (ohm), V_across (V) or I (A), P_rated (W), grade (RN55/CMF55/...), derate k (user, 0<k<=1) -> P = V^2/R or I^2*R; use MIL RN55 rating (1/8 W) when grade unknown for RN55-size parts -> pass P <= k*P_rated -> margin = 1 - P/(k*P_rated) -> AOE-1002, AOE-1006.
- `CHECK-divider-loading`: R1, R2, R_load (ohm), V_in (V) -> R_Th = R1*R2/(R1+R2); V_loaded = V_in*R2/(R1+R2)*R_load/(R_load+R_Th) -> pass R_load >= 10*R_Th (book "factor of 10 is a comfortable rule of thumb") -> margin = R_load/(10*R_Th) - 1 -> AOE-1008, AOE-1012, AOE-1100.
- `CHECK-rc-filter-interface`: R (ohm), Z_source,max (ohm), Z_load,min (ohm) -> worst-case filter input and output impedance = R -> pass Z_source <= R/10 and Z_load >= 10*R (book example: 100 ohm source, R = 1k, load >= 10k) -> margin = min(R/(10*Z_source), Z_load/(10*R)) - 1 -> AOE-1066, AOE-1069.
- `CHECK-coupling-corner`: R_load_seen (ohm), C (F), f_min (Hz) -> f3dB = 1/(2*pi*R*C); for n cascaded coupling networks total loss at f_min = product of individual responses -> pass f3dB <= f_min/4 (book example 5 Hz for 20 Hz band) and total loss at f_min <= user dB -> margin = f_min/(4*f3dB) - 1 -> AOE-1067, AOE-1106, AOE-1236.
- `CHECK-pulse-droop`: T_pulse (s), R (ohm), C (F), droop_max (fraction, user) -> droop = T/(R*C) -> pass droop <= droop_max -> margin = droop_max/droop - 1 -> AOE-1068.
- `CHECK-rectifier-ripple`: I_load,max (A), f_line (Hz), C_nom (F), C_tol (default 0.2 per book), topology (HW=1, FW=2), V_sec,pk (V), V_F (V), V_needed,min (V) -> C_min = C_nom*(1 - C_tol); dV = I/(k*f*C_min); V_trough = V_sec,pk - n_diodes*V_F - dV -> pass V_trough >= V_needed,min and dV <= ripple_max (user; book suggests ~10 % of Vdc before a regulator) -> margin = (V_trough - V_needed,min)/V_needed,min -> AOE-1047, AOE-1048, AOE-1049, AOE-1051.
- `CHECK-zener-shunt`: V_in,min/max, V_Z, R, I_out,min/max, I_Z,min (A), P_Z,rated (W), k_derate (user), R_dyn -> I_Z,lo = (V_in,min - V_Z)/R - I_out,max; P_Z = ((V_in,max - V_Z)/R - I_out,min)*V_Z; dV_out = R_dyn*(I_Z,hi - I_Z,lo) -> pass I_Z,lo >= I_Z,min and P_Z <= k*P_Z,rated -> margin = min(I_Z,lo/I_Z,min, k*P_rated/P_Z) - 1 -> AOE-1014, AOE-1103, AOE-1104.
- `CHECK-led-drive`: V_s,min/max, V_F,min/max, V_CE(sat), R, I_target -> I_min = (V_s,min - V_F,max - V_CE)/R; I_max = (V_s,max - V_F,min - V_CE)/R -> pass 2 mA <= I_min and I_max <= LED I_F,max; P_R = I_max^2*R within resistor rating -> margin on each bound -> AOE-1018, AOE-1019, AOE-1095.
- `CHECK-inductive-clamp`: for each switched load with L>0: clamp type (diode/R/zener/TVS/RC), I_L (A), V_supply, V_clamp, V_switch,max -> pass clamp present AND I_clamp,rated >= I_L AND V_switch,max >= V_supply + V_clamp (+ V_F); ac-driven inductive loads must not use a plain diode -> margin = V_switch,max/(V_supply + V_clamp) - 1 -> AOE-1058, AOE-1059, AOE-1060, AOE-1093.
- `CHECK-bjt-switch-drive`: I_C,max (A), beta_min, I_B (A) -> pass I_B >= I_C,max/10 (book "common practice") or I_B >= 2*I_C,max/beta_min (user choice) -> margin = I_B*beta_min/I_C,max - 1 -> AOE-1091, AOE-1095, AOE-1096.
- `CHECK-bjt-reverse-vbe`: for each BJT: max reverse V_EB over all transients (V), V_EBO (V, default 6) -> pass V_EB,rev <= V_EBO - 1 V margin (user) or protective diode present -> margin = V_EBO/V_EB,rev - 1 -> AOE-1097, AOE-1133, AOE-1253.
- `CHECK-bias-stiffness`: R1, R2 (ohm), beta_min, R_E (ohm) -> R_div = R1*R2/(R1+R2) -> pass R_div <= 0.1*beta_min*R_E -> margin = 0.1*beta_min*R_E/R_div - 1 -> AOE-1105, AOE-1123.
- `CHECK-bias-thermal`: V_E,dc (V), dT (C, operating range) -> dIc/Ic ~ 2.1 mV/C*dT/V_E -> pass dIc/Ic <= user limit (book: V_E = 0.175 V gives 25 % per 20 C - fail) -> AOE-1117, AOE-1122, AOE-1123.
- `CHECK-no-beta-bias`: topology flag "base resistor from supply sets Ic via assumed beta" -> fail if present -> AOE-1107.
- `CHECK-ballast`: n_parallel, I_max per device (A), R_E or R_S (ohm), mode (switch/linear), device (BJT/MOSFET) -> V_ballast = I_max*R -> pass BJT: V_ballast >= 0.3 V (book 300-500 mV); MOSFET linear: V_ballast >= 1 V (book "a volt or two"); MOSFET switch: R_S not required but R_gate per device present -> margin = V_ballast/V_req - 1 -> AOE-1144, AOE-1205.
- `CHECK-junction-temp`: P (W), T_amb (C), theta_JC, theta_CS, theta_SA (C/W), Tj_design (user; book suggests ~100 C for care) -> Tj = T_amb + P*(theta_JC + theta_CS + theta_SA) -> pass Tj <= Tj_design -> margin = (Tj_design - Tj)/(Tj_design - T_amb) -> AOE-1135, AOE-1206.
- `CHECK-mosfet-switch-thermal`: I_rms (A), R_on(25C) (ohm), V_rating (V), theta_JA (C/W), T_A (C) -> m = 2 (V_rating <= 100 V) else 2.5; Tj = T_A + I^2*m*R_on*theta_JA; runaway iteration: Tj(n+1) = T_A + I^2*R_on(Tj(n))*theta_JA with R_on(T) linearized between 25 C and m at 150 C -> pass converges and Tj <= Tj_design -> margin = (Tj_design - Tj)/Tj_design -> AOE-1207, AOE-1208, AOE-1222.
- `CHECK-mosfet-gate`: V_GS,drive,min/max (V), V_GS,abs-max (V, default 20), V_GS at which R_DS(on) is specified (V), gate from off-board (bool), R_GS pull-down (ohm) -> pass V_GS,drive,max <= V_GS,abs-max, V_GS,drive,min >= V_GS(R_on spec), and (off-board -> 100k <= R_GS <= 1M present) -> AOE-1156, AOE-1161, AOE-1162, AOE-1211.
- `CHECK-mosfet-switch-speed`: Q_g, Q_gd (C), I_gate (A), V_GS (V), f_sw (Hz), t_target (s) -> t_sw = Q_gd/I_gate; P_gate = Q_g*V_GS*f; P_Coss = C_oss*V_DS^2*f -> pass t_sw <= t_target -> margin = t_target/t_sw - 1 -> AOE-1184, AOE-1209.
- `CHECK-mosfet-current-derate`: I_op (A), datasheet ID(25 C case) (A), R_thJC, R_on(Tj_max) -> ID_realistic = sqrt((Tj_design - T_C)/(R_thJC*R_on(T))) -> pass I_op <= ID_realistic -> margin = ID_realistic/I_op - 1 -> AOE-1206.
- `CHECK-cmos-input-range`: for each CMOS/analog-switch pin: V_in,min/max incl. faults (V), V+/V- (V), series R (ohm), fault-protected (bool) -> I_inj = max(V_in - V+ - 0.3, V- - 0.3 - V_in, 0)/R -> pass fault-protected OR I_inj < 20 mA (book latch-up trigger ~20 mA; user may tighten) and power-sequencing rule satisfied -> AOE-1054, AOE-1192.
- `CHECK-charge-injection`: Q_inj (C) or C_gc*dV_gate, C_load (F), error budget (V) -> dV = Q/C -> pass dV <= budget -> AOE-1198, AOE-1318.
- `CHECK-switch-bandwidth`: R_on (ohm), C_out (F), f_max (Hz) -> f3dB = 1/(2*pi*R_on*C) -> pass f3dB >= 10*f_max (user factor) -> AOE-1195.
- `CHECK-opamp-bandwidth-gain-error`: f_T (Hz), A_ol,dc, G_CL (noninverting gain), f_max (Hz), eps_max -> B = 1/G_CL; eps(f) = 1/(1 + B*min(A_ol,dc, f_T/f)) -> pass eps(f_max) <= eps_max -> margin = eps_max/eps - 1 -> AOE-1265, AOE-1337.
- `CHECK-opamp-slew`: V_pk (V), f_max (Hz), SR (V/s), m (user margin, e.g. 2) -> SR_req = 2*pi*f*V_pk -> pass SR >= m*SR_req -> margin = SR/SR_req - 1 -> AOE-1267, AOE-1332.
- `CHECK-opamp-swing`: V+ , V- (V), required V_out,min/max (V), datasheet headroom at I_load (V) -> pass V_out range inside [V- + h-, V+ - h+] -> AOE-1263, AOE-1343.
- `CHECK-opamp-cm-range`: V_CM,min/max (V) vs datasheet range; RRI crossover band (V) -> pass inside range and (RRI part -> V_CM excursion avoids crossover or inverting configuration used) -> AOE-1262, AOE-1341.
- `CHECK-opamp-diff-input`: max |V+ - V-| during overload/comparator use (V) vs datasheet limit (may be 0.5 V) -> pass <= limit -> AOE-1246.
- `CHECK-dc-error-budget`: V_os,max, TCV_os, dT, I_B,max(T_max), I_os, R2, R1, R_source, R_balance flag, bias-compensated flag -> err_out = (1 + R2/R1)*(V_os + TCV_os*dT) + (balanced ? G*I_os*R : I_B*R2) with I_B(T) = I_B(25)*2^((T-25)/10) for FET inputs -> pass err_out <= budget -> margin = budget/err_out - 1 -> AOE-1259, AOE-1260, AOE-1303, AOE-1307, AOE-1322.
- `CHECK-integrator-drift`: I_B (A), V_os (V), R (ohm), C (F), allowed ramp (V/s) -> ramp = (I_B + V_os/R)/C -> pass ramp <= allowed -> AOE-1243.
- `CHECK-hold-droop`: I_B, I_switch,leak, I_cap,leak (= V/R_leak with R_leak = rating(Mohm*uF)/C), I_pcb (A), C (F) -> droop = sum(I)/C -> pass <= budget -> AOE-1272, AOE-1273, AOE-1316, AOE-1319.
- `CHECK-cap-load-stability`: C_load (F) = C_cable (100 pF/m for RG-58) + C_input, op-amp stable-C limit (F), R_iso (ohm) -> pass C_load <= limit OR R_iso in [25, 100] ohm outside loop OR split feedback present -> AOE-1279, AOE-1278.
- `CHECK-tia-comp`: transimpedance stage with C_det > 0 -> pass feedback capacitor across R_f present -> AOE-1248.
- `CHECK-bypass`: for every IC supply pin: bypass capacitor to ground present (0.1-10 uF book range) and, for multiple parallel bypass caps on long rails, a lossy (ESR ~0.5 ohm) damping capacitor present -> AOE-1029, AOE-1245.
- `CHECK-schmitt`: V_swing (V), R1, R2, R3 (ohm), noise_pp (V) -> dV_hyst = V_swing*R_p/(R_p + R3) -> pass dV_hyst > noise_pp (user factor) -> AOE-1252, AOE-1099.
- `CHECK-battery-life`: C_batt (Ah), I_Q (A), I_load,avg (A), required life (h), n_cells -> life = C/(I_Q + I_load); V_min = n*0.9 V -> pass life >= required and all ICs operate at V_min -> AOE-1053, AOE-1281, AOE-1304.
- `CHECK-settling`: G_CL, f_T (Hz), eps, step V (V), SR (V/s), t_budget (s) -> t_s = G_CL/(2*pi*f_T)*ln(1/eps) + dV/SR (if slew-limited) -> pass t_s <= t_budget (treat as lower bound; require datasheet settling spec for final) -> AOE-1333, AOE-1334.
- `CHECK-phase-error`: f (Hz), f_T, G_CL, phi_max (deg) -> phi = 57.3*f*G_CL/f_T (active compensation: 57.3*(f*G_CL/f_T)^3) -> pass phi <= phi_max -> AOE-1339, AOE-1340.
- `CHECK-lc-resonance`: L (H), C (F), R (ohm), topology (parallel/series) -> f0 = 1/(2*pi*sqrt(L*C)); Q = R*sqrt(C/L) (parallel) or sqrt(L/C)/R (series) -> compare with spec f0 +/- tolerance -> AOE-1071, AOE-1072.
- `CHECK-follower-sink`: emitter follower output, V_out,min (V), V_EE (V), R_E (ohm), I_load,sink,max (A) -> I_sink,avail = (V_out,min - V_EE)/R_E -> pass I_sink,avail >= I_load,sink -> AOE-1101.
- `CHECK-short-circuit-dissipation`: V_in (V), I_limit (A), SOA/thermal limit (W) -> P = V_in*I_limit -> pass P within SOA for fault duration -> AOE-1215, AOE-1297, AOE-1225.
- `CHECK-hv-bleed`: C (F), V (V), bleeder R or depletion MOSFET (bool) -> tau = R*C; P = V^2/R -> pass tau <= 10 s (book) -> AOE-1229.
- `CHECK-bom-blacklist`: BOM categories/MPNs -> fail on Hall-of-Infamy items (UHF, type-F, phono/RCA, hexagon, Cinch-type, microphone connectors; slide switches; open-element trimmers; low-value wirewound pots; non-screw-machined IC sockets; electrical tape) -> AOE-1084.
- `CHECK-footprint-code`: package code string + declared system (inch/metric) -> pass when explicit and dimensions consistent with the code rule -> AOE-1001.
- `CHECK-lifecycle`: BOM lifecycle status and number of sources per critical part -> pass all active, >= 2 sources for critical ICs (user policy) -> AOE-1286.
- `CHECK-ratiometric`: timing/threshold circuits flagged "depends on supply" -> suggest ratiometric topology when both terms scale with same rail -> AOE-1021, AOE-1256.
## 4. Verification procedures & plots

| # | property | simulation / test | x-axis | y-axis | sweep / corners | good looks like / pass | source rows |
|---|---|---|---|---|---|---|---|
| V1 | RC/LC filter response incl. real source and load | ngspice .ac with actual Z_source and Z_load | log f (0.01 f3dB to 100 f3dB) | gain (dB) and phase (deg) | R, C at tolerance corners; load min/max | -3 dB and -45 deg (single pole) at f3dB = 1/(2 pi RC); -20 dB/decade per pole; loaded response within spec (loading shifts corner) | AOE-1065, 1066, 1069, 1070, 1074 |
| V2 | Step response / settling | .tran step input | time (0 to 10 tau) | Vout (and error on log scale) | R, C tolerance; op-amp f_T min | 10-90 % = 2.2 RC; within eps after tau*ln(1/eps); op-amp stage: no ringing beyond spec; settle to 0.01 % checked separately from 1 % | AOE-1032, 1333, 1334 |
| V3 | Rectifier ripple and diode stress | .tran over >= 10 line cycles | time | V_out, I_diode | V_line min/max, I_load max, C_min (-20 %) | ripple_pp <= spec and trough above regulator dropout; I_diode,pk within rating | AOE-1047, 1048, 1051 |
| V4 | Zener / shunt regulator line & load regulation | .dc sweep V_in and I_load | V_in (and I_load) | V_out, I_Z, P_Z | V_in min-max, I_load 0-max, T | I_Z >= I_Z,min everywhere; P_Z <= derated; dV_out as predicted by R_dyn | AOE-1014, 1103, 1104 |
| V5 | Inductive turn-off transient | .tran switch opening with coil model (L, R) | time (us-ms) | V_switch node, I_L | clamp type (diode/R/zener) | peak V_switch < V_rating with margin; decay time as required (zener fastest) | AOE-1058, 1059, 1060, 1093 |
| V6 | BJT bias robustness | .op and .dc temp sweep | beta (min..max) and temperature (-40..+85 C) | I_C, V_C, V_E | beta 0.5x-2x typ; VBE -2.1 mV/C | Q-point stays in active region (V_CE > ~1 V) at all corners; no saturation for +8 C (grounded-emitter trap) | AOE-1089, 1105, 1107, 1122, 1123 |
| V7 | Class-AB quiescent current vs temperature | .op at T steps; electro-thermal if available | output-device temperature | I_Q | T +0..+30 C over ambient; bias diodes coupled/uncoupled | I_Q rise bounded (~50 % per 30 C with ~1 VBE across R_E), no runaway | AOE-1138, 1231 |
| V8 | Crossover distortion | .tran sine + .four, or measure THD | output amplitude, frequency | THD (%) | load R min, f up to 20 kHz or f_max | THD below spec; feedback from booster output; no dead zone | AOE-1137, 1249, 1335 |
| V9 | Feedback loop stability (phase margin) | loop-gain .ac (break loop with large L/C or Middlebrook injection) | log f | loop gain (dB), phase (deg) | C_load 0 to max (cable 100 pF/m), gain settings incl. lowest G, op-amp f_T +/- | phase margin >= ~45 deg at unity loop gain; closure slope difference 6 dB/oct (never 12) | AOE-1150, 1279, 1292, 1295 |
| V10 | Closed-loop peaking / ringing with capacitive load | .ac and .tran small-signal step | log f / time | gain (dB) / Vout | C_load sweep (0, 100 pF, 1 nF, 10 nF); R_iso values | no peaking > ~1-3 dB; overshoot small; with R_iso 25-100 ohm or split feedback, ringing gone | AOE-1278, 1279, 1288 |
| V11 | Output impedance vs frequency | .ac current injection into output | log f | abs(Z_out) (ohm) | loop gain settings, load | rises ~linearly (inductive) as predicted r_o*G/(f_T/f); rail-splitter bump damped | AOE-1264, 1278, 1336 |
| V12 | Full-power bandwidth / slew | .tran large sine at increasing f | frequency | max undistorted Vpp | SR min | Vpp >= S/(pi f) at f_max with margin; no slew-induced distortion | AOE-1267, 1332 |
| V13 | DC error budget over temperature | .op Monte Carlo on V_os, I_B, I_os, resistor tolerances; temp sweep | temperature | output error (uV RTI) | V_os, I_B at max; I_B x2 per 10 C for FET inputs | total error <= budget at T_max | AOE-1259, 1260, 1302, 1303, 1307, 1325 |
| V14 | Integrator drift | .tran long (s) with input grounded | time | V_out | I_B max, V_os max, R | ramp <= (I_B + V_os/R)/C budget; reset works | AOE-1242, 1243, 1244 |
| V15 | Peak detector / S-H behaviour | .tran pulse input | time | V_hold | C, I_B, switch leakage, op-amp I_out, R_on | droop = I/C within budget; follow rate I_out/C adequate; pedestal (Q_inj/C) within budget | AOE-1198, 1272, 1273, 1316, 1318 |
| V16 | MOSFET switching (gate-charge / Miller plateau) | .tran with constant-current gate drive or real driver | time (or gate charge nC) | V_GS, V_DS, I_D | gate current, load | Miller plateau duration = Q_gd/I_g; switching time and loss as budgeted; no oscillation (series gate R per device) | AOE-1184, 1205, 1209 |
| V17 | MOSFET thermal equilibrium / runaway | spreadsheet or electro-thermal sim | junction temperature | P(Tj) = I^2*R_on(Tj) and heatsink line (Tj - T_A)/R_thJA | T_A worst case (rack), I max | curves intersect below Tj_design; no-intersection = runaway | AOE-1207, 1208 |
| V18 | Analog switch characterization | .dc and .ac | V_signal; log f | R_on; off-isolation (dB); crosstalk (dB) | supply voltage min/max; R_load | R_on flat enough for distortion spec; isolation/crosstalk above spec at f_max | AOE-1189, 1190, 1194, 1195, 1196 |
| V19 | Current-source compliance | .dc sweep load voltage | V_load | I_out | full compliance range, temperature | I_out within tolerance to the compliance limit; no breakdown/dissipation violation | AOE-1110, 1111, 1129, 1169, 1239 |
| V20 | Gain nonlinearity (Pease test) | measured: x-y of amplified input error vs output (Fig 5.23) | output voltage | input error (uV) | rated load | best-fit straight line; deviation/full swing within ppm budget | AOE-1338 |
| V21 | Phase error | .ac | log f | phase deviation (deg) | G_CL, f_T min/max; active compensation f_T mismatch +/-10 % | phi <= spec over band (f/f_c or (f/f_c)^3) | AOE-1339, 1340 |
| V22 | RRI crossover | .dc sweep V_CM (and measured) | V_CM | V_os, I_B | op-amp samples | no step in V_os/I_B within signal range, or inverting configuration used | AOE-1324, 1341 |
| V23 | Input fault protection | .tran/.dc fault injection | fault voltage (e.g., +/-150 V, +/-350 V, mains) | pin voltage, clamp current, dissipation | power on/off (sequencing) | pin within rails +/-0.3 V; injection < latch-up limit; resistor power OK | AOE-1054, 1192, 1228, 1284, 1287 |
| V24 | Supply current / battery life | bench measurement of each state | operating state | supply current | min/max V_batt, temperature | computed life >= requirement at V_min = n x 0.9 V | AOE-1281, 1304, 1309 |
| V25 | ESD robustness | HBM zap test (100 pF + 1.5 kohm) | test voltage | pass/fail, leakage shift | 2 kV internal, 15 kV external interfaces | no degradation (MOSFET gate leakage unchanged) | AOE-1161, 1213 |
| V26 | Dielectric absorption of hold capacitors | measured: charge to 10 V for a day, short 10 s, open, log voltage vs time | log time | recovered voltage | candidate dielectrics | recovered fraction below budget (PTFE/PS/PP best) | AOE-1317 |
## 5. Pitfalls, failure modes, review checklist

- [ ] Bypass capacitors omitted from the schematic are also omitted from the board - every IC rail has one (p.19 fn22, p.232).
- [ ] Unit-less capacitor values on schematics ("470" = 470 pF or 47 pF?) resolved in the BOM (p.19 fn23, p.64-65).
- [ ] 1N4148 used where reverse voltage can exceed 75 V PIV (p.31, p.36).
- [ ] Diode clamp series resistor sized for fault current and power (47k 3 W for mains-level inputs) (p.36, p.269).
- [ ] Every relay coil / solenoid / motor switched by a transistor has a flyback path; ac inductive loads use RC snubber or TVS/MOV, not a diode (p.38-39, p.75).
- [ ] Mains-connected equipment has a TVS/MOV with fusing at the entry and an across-the-line-rated snubber capacitor (p.39).
- [ ] Voltage-divider "references" loaded by clamps/biasing: Thevenin R << load (or buffered/bypassed) (p.36-37).
- [ ] Cascaded passive RC sections designed with the same impedance level (loading) (p.52).
- [ ] Coupling-capacitor corners placed below the band, accounting for several cascaded corners (p.84, p.287 motorboating).
- [ ] Probe/cable capacitance (coax 30 pF/ft, ~100 pF/m) considered at high-Z or tuned nodes and op-amp outputs (p.56, p.264).
- [ ] Low-level signal switches have gold "dry-switching" contacts (p.58).
- [ ] BOM free of Hall-of-Infamy parts (UHF, type-F, phono, hexagon, Cinch, microphone connectors; slide switches; open-element trimmers; cheap IC sockets) (p.63 Fig 1.126).
- [ ] No trimmer used as a precision resistor; trim ranges narrow (p.63, p.305).
- [ ] Variac used for line-variation tests is not isolated - use an isolation transformer where needed (p.64).
- [ ] Date codes not mistaken for part numbers at incoming inspection (p.65).
- [ ] No BJT bias depends on an assumed beta ("Don't do this!") (p.85).
- [ ] No grounded-emitter stage without overall feedback (distortion, 8 C saturation) (p.94-96).
- [ ] Capacitively coupled BJT bases cannot be driven into B-E reverse breakdown (~6 V) - pulse circuits above +7 V, op-amp-driven switches on split rails (p.77 fn13, p.82, p.238).
- [ ] Differential pairs / op-amp inputs protected against > ~6 V (or datasheet limit, as low as 0.5 V) differential (p.104, p.232, p.246).
- [ ] Emitter-follower sink capability (via R_E) sufficient for the load; regulator outputs not back-driven by other supplies (p.81-82).
- [ ] Regulators with output-derived reference bias verified to start up (p.123, p.236).
- [ ] Every power switch/regulator has current limiting and survives a shorted output (P = V_in*I_lim) (p.203, p.236, p.286).
- [ ] Paralleled BJTs have emitter ballast (0.3-0.5 V); paralleled MOSFETs in linear service have source ballast (~1-2 V) or active balancing; switching MOSFETs each have their own gate resistor (p.112-113, p.192, p.212-213).
- [ ] Datasheet ID(max)/Pdiss at T_C = 25 C not used as design values; R_DS(on) scaled for hot junction (x1.5-3.5) (p.106, p.188-189, p.199, p.216).
- [ ] MOSFET gates never float; off-board gates have 100k-1M pull-downs and ~1k series resistors (p.132, p.199-200).
- [ ] MOSFET gate never driven beyond +/-20 V (e.g., from another device's drain swing on high rails) (p.199, p.203).
- [ ] VGS(th) "logic level" claims checked against R_DS(on) spec at the actual drive voltage (p.193-194).
- [ ] Gate drive current adequate (Q_g/I); CMOS logic not driving large MOSFETs directly (latch-up risk) (p.164-165, p.198).
- [ ] Power MOSFET body diode considered (no bipolar blocking; reverse-recovery snap) (p.199).
- [ ] Handling: ESD-safe workstation, conductive packaging, wrist straps; winter humidity (p.200-201).
- [ ] JFET inputs not operated at high drain-gate voltage (impact ionization, uA gate current); cascode used (p.163-164).
- [ ] FET-input leakage evaluated at maximum chip temperature (x2 per 10 C) (p.163, p.295, p.303).
- [ ] MOSFETs not used in low-level low-frequency front ends (1/f noise up to 40 dB worse) (p.170).
- [ ] CMOS inputs never driven beyond the rails before supplies are up (power sequencing) (p.174-175).
- [ ] Analog switch R_on flatness, charge injection and off-isolation budgeted; BBM vs MBB chosen correctly for gain-switching loops (p.177-181).
- [ ] Op-amp common-mode range respected, including at the negative rail (LF411 phase reversal; LM358 > 400 mV below V-) (p.245).
- [ ] Op-amp output swing headroom checked at the load current (not rail-to-rail unless specified) (p.246-247).
- [ ] Capacitive loads (cables!) isolated or split-feedback used; rail-splitter output damped (p.263-265).
- [ ] Transimpedance stages have a feedback capacitor (p.233).
- [ ] Differentiators rolled off; integrators have dc feedback or reset (p.230-231, p.260).
- [ ] Faster op-amp substitution in a working boosted/composite loop re-verified for stability (p.235 fn10).
- [ ] Decompensated op-amps used only above their minimum closed-loop gain (p.283).
- [ ] Offset/bias-current error computed with noninverting gain (1 + R2/R1) and at T_max (p.251-252).
- [ ] Datasheet parameters used only under their stated test conditions (e.g., V_os guaranteed only at specific V_CM) (p.305).
- [ ] RRI op-amps kept out of input-stage crossover, or inverting configuration used (p.316).
- [ ] RRO "rail-to-rail" claims checked (last few mV, high Z_out, load-dependent gain) when driving ADCs to ground (p.316-318).
- [ ] Precision op-amps loaded >= 10k and kept cool (buffer inside loop) (p.305, p.312).
- [ ] Error budget includes known unknowns (unspecified leakages) with measurements/qualification (p.296-297, p.299).
- [ ] Hold capacitors are PTFE/PS/PP (dielectric absorption) with leakage budgeted (p.300-301).
- [ ] Battery life computed with load currents and end-of-life voltage (0.9-1.0 V/cell) (p.266, p.276, p.293).
- [ ] Critical parts checked for discontinuation risk / second source (p.273).
## 6. Standards referenced

The book cites few formal standards in this range; the following are named, with what they govern here.

| standard / convention | edition / clause | what it governs (as used in the text) | page |
|---|---|---|---|
| EIA E6 preferred values (20 %) | - | capacitor/resistor value series used in examples (e.g., 0.47 uF, 3.3 uF) and Fig 1.100B reactance chart | p.49 Fig 1.100B; p.84 fn18 |
| EIA E24 / E96 preferred values | App. C | 2 %/5 % resistors: 24 values per decade; 1 %: 96 values per decade; nearest standard values used in designs | p.5; p.24; p.239 |
| MIL-spec RN55 resistor grade | - | RN55D 1 % metal film rated 1/8 W (vs 1/4 W CMF-55 industrial) | p.4 fn8 |
| RN55C metal-film stability specs | - | 50 ppm/C, 0.25 % soldering/cycling, 0.1 % shock/vibration, 0.5 % moisture | p.300 |
| MIL-C-5015 ("MS") circular connectors | - | rugged multipin circular connector family | p.61 Fig 1.124 |
| IEC power-cord connector | - | three-wire line-cord inlet | p.61 |
| VME (VersaModule Eurocard) connector | - | two-part PCB/backplane connector (more reliable than card edge) | p.61 |
| "Across-the-line" capacitor rating (safety class, see §9.5.1) | - | capacitors used in RC snubbers across the ac line | p.39 fn33 |
| Human-body model (HBM) ESD | 100 pF + 1.5 kohm | ESD tolerance rating of MOS ICs (typ 2 kV; interface parts 15 kV); machine model (up to 6 A, 12 kHz ringing) and charged-device model (6 A, 2 ns) also named | p.200-201 fn97 |
| RS-232 / RS-422 / RS-485 interface ICs | "E" suffix parts | +/-15 kV ESD-rated line drivers/receivers; RS-232C charge-pump drivers | p.184, p.201 |
| TTL / CMOS logic thresholds | family datasheets | 74LVC at 3.3 V: 1.5 V threshold, outputs within 0.4 V of rails; TTL HIGH may be as low as 2.4 V; logic-level MOSFET-driver inputs < 2.4 V | p.17, p.192 fn82, p.194 |
| SPICE (Ebers-Moll, Gummel-Poon models) | - | transistor simulation; power-MOSFET models "nearly useless" in subthreshold region | p.93 fn32; p.168 fn61 |
| Kelvin (4-terminal) connection | - | current-shunt sensing independent of lead/bond resistance | p.277; p.294 fn2 |
## 7. Process / lifecycle guidance

The book is a circuit-design text, not a product-development text; the process items below are the ones it states explicitly in this range.

| stage | activity | deliverable | exit criterion | source |
|---|---|---|---|---|
| design (precision analog) | Build an error budget covering components, amplifier input errors and output errors, drifts vs time/temperature/supply; decide strict worst-case vs tested (pragmatic) basis | error-budget table (knowns, known unknowns, margin for unknown unknowns) | every term quantified; total within spec at worst case or covered by a test plan | p.293, p.295-299 (AOE-1302, 1311, 1312) |
| design (component choice) | Prefer parts whose datasheet guarantees meet the budget untrimmed; avoid manual trims in production | selected-parts list with guaranteed specs at operating temperature | no production calibration step unless justified | p.254, p.304-305 (AOE-1271, 1325) |
| design (unspecified parameters) | Measure poorly specified parameters (diode leakage at mV, JFET gate leakage at low V_DS, CMOS quiescent current) or qualify a source in-house | measurement report / qualified-source record | parameter shown orders of magnitude below budget, or incoming test defined | p.296-297 (AOE-1306, 1309) |
| sourcing | Check lifecycle status and second sources; plan for discontinuation (redesign or plug-in emulation board) | BOM risk review | critical parts active and second-sourced | p.273 (AOE-1286) |
| manufacturing | ESD-controlled handling of MOS devices (conductive packaging, grounded irons/benches, wrist straps, humidity control, ionizers, trained workers) | ESD control plan | failure rates monitored (they rise in winter) | p.200 (AOE-1213) |
| test (subassembly / final) | Validate aggregate behaviour when worst-case datasheet limits can't be met (e.g., quiescent-current test of CMOS subcircuits) | test procedure + limits | modules outside limit rejected (found handling damage) | p.296-297 (AOE-1309) |
| test (line variation) | Verify worst-case performance vs mains voltage with a Variac (non-isolated!) | line-variation test record | performance in spec from low to high line | p.64 (AOE-1087) |
| prototyping | Plan PCB-based prototypes (SMT-only parts) or SMT adapters | prototype PCB | board area/performance as expected | p.65-66, p.268-269 (AOE-1283) |
## 8. Coverage log

| file lines | content | status |
|---|---|---|
| 1-3167 | title page, contents (all chapters), list of tables, prefaces (1st/2nd/3rd eds), legal notices | read for orientation; no rules |
| 3168-3595 | §1.1-1.2 voltage, current, resistors (box), dividers, sources, Thevenin, multimeters (box), zener small-signal R, "It's too hot!" | read fully |
| 3595-3768 | §1.3 signals, dB references, logic levels, signal/pulse/function generators | read fully |
| 3768-4222 | §1.4 capacitors, RC circuits, time-delay and "one minute" timer, differentiators, integrators, imperfections | read fully |
| 4222-4333 | §1.5 inductors, Wheeler's formula, buck/boost preview, transformers | read fully |
| 4333-4742 | §1.6 diodes (Table 1.1), rectification, ripple, rectifier configurations, regulators, clamps, limiters, log converter, inductive kick, resonant charging | read fully |
| 4742-5404 | §1.7-1.8 reactance, complex impedance, power factor, RC high/lowpass, phasors, poles, resonant circuits, LC filters, bypassing, AM radio | read fully; complex-algebra derivation (§1.7.3-1.7.4) kept as results only |
| 5404-5660 | §1.9-1.10 switches, relays, connectors, indicators, variable components, markings, SMT | read fully |
| 5661-5746 | Ch.1 additional exercises and review | exercises skimmed (no new data except x10 probe numbers); review read |
| 5747-7870 | Ch.2 §2.1-2.6 (Table 2.1, Table 2.2) | read fully; Table 2.1 numeric columns and Table 2.2 hFE/f_T columns OCR-scrambled (partially transcribed) |
| 7871-7989 | Ch.2 additional exercises and review | exercises skimmed; review read |
| 7990-9489 | Ch.3 §3.1-3.3 (Table 3.1, current-regulator diodes, Table 3.2) | read fully |
| 9489-10420 | Ch.3 §3.4 FET switches (Table 3.3 analog switches) | read fully; Table 3.3 reconstructed partially from OCR order |
| 10420-11354 | §3.5.1 and Tables 3.4a/3.4b (MOSFET tables) | read; Table 3.4a n-channel column transcribed; p-channel column and all of Table 3.4b numerics too scrambled - only notes transcribed |
| 11355-12136 | §3.5.2-3.5.7 power MOSFET switching, cautions, ESD, BJT/MOSFET/IGBT comparisons, circuit examples, IGBTs, thyristors (Table 3.5) | read fully; Table 3.5 numbers not transcribed (column alignment unclear) |
| 12137-12592 | §3.6 linear MOSFET applications, depletion-mode circuits (Table 3.6), paralleling, thermal runaway | read fully; Table 3.6 not transcribed (scrambled) |
| 12593-13526 | Table 3.7 JFETs, Table 3.8 gate drivers | read; key columns reconstructed |
| 13527-13595 | Ch.3 review | read |
| 13596-15320 | Ch.4 §4.1-4.6 (Table 4.1) | read fully |
| 15321-16277 | Table 4.2a (representative op-amps), Table 4.2b (power/HV op-amps) | read; 4.2a too scrambled (comments only), 4.2b partially reconstructed |
| 16277-16947 | §4.7-4.9 other amplifier types, "Here yesterday, gone today" box, typical circuits, frequency compensation | read fully |
| 16948-17149 | Ch.4 additional exercises and review | exercises skimmed; review read |
| 17150-19365 | Ch.5 §5.1-§5.10.1 (Tables 5.1-5.5) | read fully; stopped at the start of §5.10.2 (line 19365) because Table 5.5 straddles line 19000; Table 5.5 JFET/CMOS/chopper rows too scrambled to transcribe (part 2 overlap) |

**Extraction limitations.**
- Figures are not in the text; rules depending on graphs quote captions and the numeric anchors in the prose (e.g., Fig 1.104 phase table, Fig 3.120 thermal runaway, Fig 5.12 slew vs input).
- OCR noise: micro/ohm glyphs, split words ("in v e rtin g"), and interleaved table columns. Every tabulated value marked "(as read)", "reconstructed" or "OCR-ambiguous" should be verified before use as a hard limit; derived values are tagged conf = medium.
- Several multi-column tables (2.1, 3.3, 3.4a p-channel, 3.4b, 3.5, 3.6, 4.2a, 5.5 lower sections) could not be reconstructed reliably; only their notes/comments were extracted.
- Rule count: 345 (AOE-1001 ... AOE-1345). Chapters 6-15 and appendices are handled by parts 2-4.
