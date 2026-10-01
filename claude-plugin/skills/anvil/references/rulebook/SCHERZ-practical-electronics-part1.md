# Practical Electronics for Inventors, 4th ed. (Part 1: Ch.1-7) — Anvil rulebook

## 0. Citation

P. Scherz and S. Monk, *Practical Electronics for Inventors*, 4th ed. New York, NY, USA: McGraw-Hill Education, 2016 (copyright 2016, 2013, 2007, 2000; LCCN 2016932853). ISBN 978-1-25-958754-2 (MHID 1-25-958754-1). Technical editors M. Margolis and C. Fitzer.

BOOKTAG: SCHERZ. Source text: `refs-text/Practical_Electronics_for_Inventors_Paul_Scherz_Simon_Monk_2.txt` (56,820 lines). This extraction is part 1 of 2: file lines 1-28484 (assigned range 1-28400, extended to the end of §7.4.6, which closes ~84 lines later). Rule ids in this part: SCHERZ-1001 to SCHERZ-1309.

**Chapters covered by this extraction (read in order):**
- Front matter, copyright/ISBN page, full table of contents, preface (file lines 1-2424)
- Ch.1 Introduction to Electronics (pp.1-3) - overview only, no rules
- Ch.2 Theory (pp.5-251): current, voltage, resistance/resistivity, heat and thermal resistance, wire gauges, grounds, resistor networks, sources, meters, batteries, Kirchhoff/Thevenin/Norton, ac and RMS, mains power, capacitors, inductors, complex impedance, ac power and power factor, resonance/Q/bandwidth, decibels, input/output impedance, passive filters and attenuators, transients, Fourier, SPICE
- Ch.3 Basic Electronic Circuit Components (pp.253-399): wires/cables/connectors and transmission lines, batteries, switches, relays, resistors, capacitors, inductors, transformers, fuses and circuit breakers
- Ch.4 Semiconductors (pp.401-493): diodes and rectifiers, zeners, varactor/PIN, BJTs, JFETs, MOSFETs, IGBTs, UJT/PUT, thyristors (SCR, SCS, triac, diac), transient suppressors (TVS, MOV, MLV, Surgector, PolySwitch, avalanche), IC packages
- Ch.5 Optoelectronics (pp.495-524): lamps, LEDs, laser diodes, photoresistors, photodiodes, solar cells, phototransistors, photothyristors, optoisolators, optical fibre
- Ch.6 Sensors (pp.525-550): accuracy/calibration, temperature, proximity/touch, motion/force/pressure, chemical, light/radiation/magnetic/sound, GPS
- Ch.7 Hands-on Electronics §7.1-§7.4.6 (pp.551-590): safety, ESD, schematics, prototyping, PCB making, construction hardware, soldering, enclosures, multimeters, oscilloscopes (through "Measuring Things with Scopes")

**Not read in this part (outside the assigned range - covered by the part-2 extraction):** Ch.7 §7.4.7 Scope Applications through §7.5.23 (pp.590-634), Ch.8 Operational Amplifiers through Ch.17 Modular Electronics, Appendices A-C, Index.

**Notation.** ASCII only: "u" = micro, "ohm", "degC", "//" in text marks a parallel combination, sqrt(), ln() natural log, log10(). Values are transcribed exactly; where the book's own arithmetic or labels are inconsistent the cell says "as printed" and the issue is listed in §5. Where the text extraction scrambled a table's columns or dropped a square-root sign, the value was reconstructed and cross-checked against the book's worked examples and tagged `medium`.

**Confidence tags:** `high` = number/formula stated explicitly in the text; `medium` = derived from a stated relation, reconstructed from a scrambled table, or read from a figure caption; `low` = qualitative guidance quantified by the extractor (used only for a few check thresholds, flagged in §3).

## 1. Design rules

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| SCHERZ-1001 | power | Generalized power law: power into any two-terminal load is P = V*I regardless of load type; use I = P/V to size supply/current budget. Example: 12 V device rated 100 W draws 8.3 A; 1.5 V flashlight at 0.1 A = 0.15 W | P[W] = V[V]*I[A]; I = P/V | V, I or P | any load, dc or rms ac | calc | §2.3.2 p.14-15, Eq.2.3 | high |
| SCHERZ-1002 | thermal | Only a purely resistive (ohmic) element converts all input power to heat: P = V^2/R = I^2*R (Joule/I2R loss). Do not compute heat from P = V*I of a black-box load that does useful work (motor, lamp, speaker); treating a load as a resistor is an analysis trick, not a heat estimate | P_heat = I^2*R = V^2/R (resistor only) | R, I or V | heat budgets for resistors, wires, internal resistances | calc | §2.7 p.32-33, Eq.2.10 | high |
| SCHERZ-1003 | materials | Conductor resistance from geometry: R = rho*L/A (A = cross-section). Worked: 1 m rods, 2 mm dia (L/A = 3.18e5 1/m): Cu 5.48e-3 ohm, brass 2.23e-2 ohm, stainless 2.31e-1 ohm, graphite 11.1 ohm; at 0.2 A loss = Cu 2.2e-4 W, brass 8.9e-4 W, steel 9.2e-3 W, graphite 0.44 W | R[ohm] = rho[ohm*m]*L[m]/A[m^2] | rho (Table 2.2), L, A | dc, uniform conductor | calc | §2.5.2 p.25, Eq.2.5/2.7; example p.33-34 | high |
| SCHERZ-1004 | materials | Metal resistivity rises linearly with temperature within a range: rho = rho0*[1 + alpha*(T - T0)]; copper alpha = 0.0039 /degC (Table 2.2). Semiconductors have negative alpha (Si -0.075, Ge -0.048, carbon -0.0005 /degC) | rho = rho0*(1 + alpha*(T-T0)) | rho0 at T0, alpha, T | metals within linear range | calc | §2.5.2 p.26-27, Eq.2.8, Table 2.2 | high |
| SCHERZ-1005 | thermal | Thermal resistance of a slab: R_th = L/(k*A) = lambda*L/A; heat flow P_heat = dT/R_th (thermal Ohm's law: dT ~ V, P ~ I, R_th ~ R). Layers in series add; parallel paths combine like resistors | R_th[degC/W] = L/(k*A); P[W] = dT[degC]/R_th | L, A, k or lambda (Table 2.4) | steady state, 1-D conduction | calc | §2.8 p.35-37, Eq.2.12-2.14 | high |
| SCHERZ-1006 | thermal | Stacked-layer hot-spot estimate (worked): thin-film resistor dissipating 2 W over 0.1 x 0.2 in (100 W/in^2) on 0.025 in alumina (lambda 2.13 degC*in/W) -> 5.3 degC, 0.002 in silicone grease (lambda 46) -> 9.2 degC, 0.125 in aluminum (lambda 0.23) -> 2.9 degC; total 17.4 degC above an 80 degC plane -> ~100 degC max. Thin grease layer dominates the stack. Neglecting lateral spreading makes this conservative | dT_i = lambda_i*L_i*P/A (lambda in degC*in/W, L in in, A in in^2); T_max = T_plane + sum(dT_i) | P, A, layer lambda/thickness | 1-D, no spreading (conservative) | calc | §2.8.1 p.38, Fig.2.25, Table 2.4 | high |
| SCHERZ-1007 | derating | Select every component (resistors, capacitors, transformers, transistors, motors) with a power rating 2 to 3 or more times the maximum power it is expected to dissipate. Where self-heating would shift a parameter, choose a part with a lower temperature coefficient (TC) | P_rated >= 2..3 * P_diss_max | P_diss_max, P_rated, TC | all dissipating parts | calc | §2.8.1 p.38 | high |
| SCHERZ-1008 | current-carrying | Wire-size selection: compute I_max = P_max/V at the maximum load power and pick the AWG whose current capacity (Table 2.5) >= I_max; the conservative choice is a larger size. Worked: 5 W at 12 V -> 0.42 A -> 22 AWG (0.914 A) works, 18 AWG (2.32 A) conservative; 10 ohm heater on 120 VAC -> 1440 W, 12 A -> 10 AWG (14.834 A) supports it, 8 AWG safer | I_capacity(AWG) >= I_max | P_max, V, AWG | copper, single conductor; Table 2.5 values | calc | §2.9 p.39-40, Table 2.5 | high |
| SCHERZ-1009 | current-carrying | Wire voltage drop can be ignored only for short runs (10 ft example); for long runs compute drop from Table 2.5 ohms/1000 ft at 25 degC over the full current loop | V_drop = I*R_per_ft*L_loop | I, AWG, loop length | long cable runs, low-voltage supplies | calc | §2.9 p.40, Table 2.5 | medium |
| SCHERZ-1010 | current-carrying | Exceeding a wire's current capacity raises current density until the lattice heating reaches the fusing point (wire meltdown); smaller AWG number = larger diameter = more current capacity | I <= I_capacity(AWG) | AWG, I | copper wire | calc | §2.9 p.39 | high |
| SCHERZ-1011 | protection | Never place a bare wire directly across a source: 120 V mains trips the branch breaker (typically 10 A or 15 A) with sparking/melting; a good dc supply trips an internal breaker/fuse, a poor one is damaged; a battery short heats and may rupture the battery | fault current >> breaker rating (10/15 A) | source type | bench and mains wiring | review | §2.9 p.40 | high |
| SCHERZ-1012 | esd | Air breakdown field ~3 MV/m between plane electrodes (1 cm gap ~30 kV); a sharp point or thin wire concentrates the field and drops breakdown to a few kV (corona). Discharge types: corona, spark, brush | E_breakdown ~ 3e6 V/m (plane); few kV at points | gap, electrode shape, V | dry air, sea level | calc | §2.5 Table 2.3 p.27-28 | high |
| SCHERZ-1013 | esd | Human ESD perception: few people notice discharges below ~1000 V; most feel an unpleasant effect ~2000 V; almost everyone complains above 3000 V (so a discharge a person does not feel can still be ~1 kV) | perception ~1-3 kV | none | walking on carpet with insulated shoes | review | §2.5 Table 2.3 p.28 | high |
| SCHERZ-1014 | grounding | Earth ground: a rod driven into the earth to a depth of 8 ft or more, wired to the mains breaker-box ground bar and carried to outlets by a green-insulated or bare copper conductor in the same cable as hot and neutral | rod depth >= 8 ft | installation | mains-powered equipment | inspect | §2.10.1 p.42, Fig.2.29 | high |
| SCHERZ-1015 | grounding | A bench dc supply's output is floating until a jumper ties its negative terminal to the ground (chassis/earth) terminal; a load connected between + and the GND terminal of a floating supply has no return path and draws zero current | load must connect + to - (floating) or - jumpered to GND (grounded) | supply wiring | 3-terminal bench supplies | inspect | §2.10.1 p.43-44, Fig.2.31 | high |
| SCHERZ-1016 | grounding | Split supply from two supplies: tie the + supply's negative terminal to the - supply's positive terminal to form the common return; tying that common to earth is optional and generally neither helps nor hinders | common = V+(-) tied to V-(+) | supply wiring | +/- rail circuits (audio, op-amps) | inspect | §2.10.1 p.44-45, Fig.2.32 | high |
| SCHERZ-1017 | compliance | Connect metal chassis/cabinets to protective earth through the 3-wire power cord so a fault that makes the chassis "hot" drives current to ground rather than through a person (dc/safety ground); the same system normally doubles as RF ground (low-impedance path for stray RF) | chassis-to-PE resistance ~0 ohm | chassis bond, cord | mains-powered metal-enclosure equipment | measure | §2.10.1 p.43-44 | high |
| SCHERZ-1018 | materials | Aluminum conductors oxidize badly, degrading contacts and limiting current to small channels; aluminum home wiring produced fire hazards. Prefer copper for current-carrying terminations | copper over aluminum at terminations | conductor material | power wiring, terminations | review | §2.5.2 p.26 | high |
| SCHERZ-1019 | compliance | When a metal enclosure/chassis is used as a return in high-voltage equipment, leakage paths can raise it to a high voltage relative to earthed objects (pipes); wire the chassis to earth ground so both sit at the same potential. Electrical codes require appliance frames (washers, dryers) to be earthed | chassis-to-earth bond ~0 ohm | enclosure, PE bond | mains/HV equipment with metal enclosures | measure | §2.10.3 p.47, Fig.2.35a-b | high |
| SCHERZ-1020 | grounding | Several separated ground points form ground loops: a measurement referenced to the wrong ground reads VS + VG (VG = ground-to-ground potential from ground-line impedance). Use a single-point ground or, where impractical (>= ~10 grounds), a ground bus | error = VG | ground topology | measurement/signal grounds | review | §2.10.3 p.47-48, Fig.2.35c-d | high |
| SCHERZ-1021 | grounding | A ground bus (bus bar on breadboard/proto board or etched PCB bus) must be a heavy, low-resistance conductor able to carry the SUM of all load currents back to the supply, run along the board; tie every circuit ground directly to it with secure joints (good solder, tight wrap, correct wire gauge in breadboard sockets) - intermittent contacts cause noise | I_bus_rating >= sum(I_load) | load currents, bus size | prototype and PCB ground returns | calc | §2.10.3 p.48, Fig.2.35e | high |
| SCHERZ-1022 | grounding | Mixed-signal devices: keep analog and digital grounds separate and join them at ONE single point (typically near the supply/system reference). Constant ground current makes a dc offset (I*R); switching/slewing currents through ground R, L, C produce high-frequency noise voltage in local circuits | single tie point AGND-DGND | ground net topology | boards with analog + digital circuitry | inspect | §2.10.3 p.48 | high |
| SCHERZ-1023 | derating | Resistor power: standard general-purpose ratings 1/8, 1/4, 1/2 and 1 W; power resistors 2 W to several hundred W. Rule of thumb: select a rating at least twice the maximum anticipated dissipation. Worked: 100 ohm across 12 V dissipates 1.44 W - a 2 W part works, 3 W is safer | P_rated >= 2*P_max; P = V^2/R = I^2*R | V or I, R | all resistors | calc | §2.12.1 p.51 | high |
| SCHERZ-1024 | components | Maximum voltage a resistor can take within its power rating: V_max = sqrt(P_rated*R). For 1 W parts: 2 ohm 1.4 V, 100 ohm 10.0 V, 3 kohm 54.7 V, 68 kohm 260.7 V, 1 Mohm 1000 V (high-value parts are then usually limited by their element voltage rating instead) | V_max = sqrt(P*R) | P_rated, R | dc or rms | calc | §2.12.1 p.52, Example 4 | high |
| SCHERZ-1025 | power | Unloaded voltage divider: Vout = Vin*R2/(R1+R2); valid only when the load draws practically no current (e.g. 10 Mohm IC input). Design: pick R2, then R1 = R2*(Vin - Vout)/Vout; worked 9 V -> 5 V with R2 = 10 kohm gives R1 = 8 kohm. Keep divider current low enough to avoid needless loss | Vout = Vin*R2/(R1+R2) | Vin, Vout, R2, R_load | R_load >> R2 | calc | §2.12.3 p.56-57, Fig.2.44 | high |
| SCHERZ-1026 | power | Loaded divider "10 percent rule": choose bleeder current I2 = 0.10*I_load; R2 = V_load/I2 (round to a standard value, then recompute I2); R1 = (Vin - V_load)/(I2 + I_load). Worked: 10 V supply, 3 V load at 9.1 mA -> I2 = 0.91 mA, R2 = 3297 -> 3300 ohm, I1 = 10.0 mA, R1 = 700 ohm; P_R1 = 70 mW, P_R2 = 3 mW -> 1/4 W parts suffice | I_bleed = 0.1*I_load | Vin, V_load, I_load | resistive dividers feeding a fixed load | calc | §2.12.3 p.57-58 | high |
| SCHERZ-1027 | power | Multi-tap divider: bleeder current = 10 % of the TOTAL of all load currents; bottom (bleeder) resistor = lowest tap voltage/I_bleed; each higher resistor carries the bleeder plus all loads below it: R_k = (V_k - V_k-1)/(I_bleed + sum loads below). Worked (100 V source): loads 75 V/30 mA, 50 V/10 mA, 25 V/10 mA -> I_bleed 5 mA, R4 5000, R3 1667 (1.68 k), R2 1000, R1 455 ohm. Bipolar taps: put ground between resistors (+50 V/50 mA, +25 V/10 mA, -25 V/100 mA -> I_bleed 16 mA, R4 1562, R3 446, R2 379, R1 216 ohm) | I_bleed = 0.1*sum(I_load) | tap voltages, load currents | resistive multi-output dividers | calc | §2.12.5 p.61-62, Fig.2.49-2.50 | high |
| SCHERZ-1028 | power | Voltage dividers are unregulated: any change in a load's resistance or in the supply changes every tap. Do not use a divider where loads vary or draw considerable current - use an active regulator (voltage-regulator IC) | divider only for fixed, light loads | load variation | supply rails | review | §2.12.5 p.62 | high |
| SCHERZ-1029 | power | Real voltage source = ideal source + series rs: V_T = Vs*Rload/(Rload + rs). rs can be ignored when Rload >= 1000*rs. Bench dc supply source resistance is usually small but can be as high as 600 ohm - always set the supply voltage with the load connected and recheck as components are added/removed | Rload/rs >= 1000 for negligible droop | Vs, rs, Rload | any source feeding a load | measure | §2.13 p.63-64, Fig.2.52 | high |
| SCHERZ-1030 | power | Real current source = ideal source with shunt rs: I_T = Is*rs/(Rload + rs). A resistive current source (high V in series with high R) gives I = V/R when R >> Rload: 1 kV + 1 Mohm holds 1 mA within 1 % over 0-10 V (0 < Rload < 10 kohm), i.e. R_series/Rload_max = 100 | error ~ Rload/R_series | Is, rs, Rload | current sources/limiters | calc | §2.13 p.64-65, Fig.2.53-2.54 | high |
| SCHERZ-1031 | test | Meter loading: ideal voltmeter Rin = infinite (real: several hundred Mohm as printed); ideal ammeter Rin = 0 (real: fractions of an ohm); real ohmmeter internal resistance fractions of an ohm. Error grows as circuit resistance approaches the meter's internal resistance - read the instrument manual for its internal resistances | R_circuit << R_voltmeter; R_circuit >> R_ammeter | meter specs, circuit R | dc/ac bench measurement | measure | §2.14 p.65-66, Fig.2.55-2.56 | high |
| SCHERZ-1032 | power | Battery combinations: series adds voltage; parallel adds capacity (run time) and divides internal resistance (cells of 0.2 ohm in parallel -> 0.04 ohm Thevenin in the book's example). Parallel only cells of identical voltage and chemistry, all fresh | R_int_total = r/n (n parallel) | cell V, chemistry, r | battery packs | review | §2.15 p.67, Fig.2.58; §2.19 p.80, Fig.2.76 | high |
| SCHERZ-1033 | protection | Short-circuit current is limited only by source internal resistance plus wiring; there is usually still plenty of current to do damage. Size the fuse so the fault current clearly exceeds its rating (worked: full short with 3 ohm internal resistance -> 4 A through a 1 A fuse -> fuse blows; battery internal resistance 0.2 ohm below 3 A rising to 2 ohm in a short -> 6 A -> fuse blows). Protection devices: fuses, transient voltage suppressors, circuit breakers | I_fault = V/(r_int + r_wiring) >> I_fuse | V, r_int, fuse rating | battery and supply circuits | calc | §2.16 p.68-69, Fig.2.60-2.61 | medium |
| SCHERZ-1034 | derating | AC ratings: V_peak = 1.414*V_rms, V_rms = 0.707*V_peak (sine); AC voltages are RMS unless stated. US mains 120 VAC 60 Hz = 170 V peak; Europe/many countries 240 VAC 50 Hz. Convert to the basis of the component rating before comparing (e.g. 10.00 VAC across a capacitor = 14.14 V peak) | V_peak = sqrt(2)*V_rms | V_rms, rating basis | sinusoidal ac | calc | §2.21 p.89-90, Eq.2.28-2.29, Fig.2.87 | high |
| SCHERZ-1035 | components | Resistor dissipation on ac: P = V_rms^2/R = I_rms^2*R (purely resistive only). Worked: across 120 VAC, 100 ohm -> 144 W (needs a power resistor/heater), 1 kohm -> 14.4 W, 10 kohm -> 1.44 W, 100 kohm -> 0.14 W; a 20 Vpp generator (7.1 Vrms) needs >= 400 ohm for a 1/8 W resistor | R_min = V_rms^2/P_rated | V_rms or Vpp, P_rated | resistive loads on ac | calc | §2.21 p.90-91, Examples 1 and 5 | high |
| SCHERZ-1036 | test | Many DMMs measure the peak and display a sine-equivalent RMS; analog meters measure half-wave average scaled to RMS. For non-sinusoidal waveforms use a true-RMS meter (which also includes any dc component). Know the meter's measurement basis before applying conversion factors | use true-RMS for non-sine | meter type, waveform | ac measurements | measure | §2.21 p.91-92, Fig.2.89 | high |
| SCHERZ-1037 | compliance | US residential mains: split phase, hot-to-hot 240 V, neutral-to-hot 120 V (nominal; e.g. 117 V). Colors: black = hot (A and B phase), white = neutral, green or bare = ground. Neutral bar and ground bar are bonded only in the main service panel; subpanels keep them separate and receive a ground wire (or conduit); a subpanel in another building gets its own ground rod. Balance A- and B-phase loads; 240 V loads use double-pole breakers; 120/240 V appliances use 4-wire cable | N-G bond only at main panel | installation | US building wiring (regional practice varies; consult local inspector) | inspect | §2.22 p.92-94, Fig.2.90 | high |
| SCHERZ-1038 | components | Commercial capacitors span 1 pF to 4700 uF; preferred first two digits are 10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82, 100 (e.g. 27 pF, 100 pF, 0.01 uF, 4.7 uF, 680 uF) | value mantissa in {10,12,15,18,22,27,33,39,47,56,68,82} | C value | BOM value selection | inspect | §2.23 p.96 | high |
| SCHERZ-1039 | components | Parallel-plate capacitance: C = k*eps0*A*(n-1)/d, eps0 = 8.85e-12 F/m, n = number of interleaved plates; k ranges from 1.00059 (air, 1 atm) to over 1e5 (some ceramics). Worked: 2 plates of 4 cm^2, 0.15 mm paper (k = 3.0) -> 70.8 pF | C[F] = 8.85e-12*k*A[m^2]*(n-1)/d[m] | k, A, d, n | parallel plates, fringing neglected | calc | §2.23.1 p.97-98, Eq.2.35-2.37 | high |
| SCHERZ-1040 | components | Electrolytic capacitors are polarized: the (-) lead is marked (some SMD parts mark +). Except special nonpolarized types, do not use them in ac applications; an ac signal superimposed on dc is acceptable provided the peak voltage does not exceed the capacitor's maximum dc voltage rating | V_dc + V_ac_pk <= V_rated; no polarity reversal | V_dc, V_ac_pk, polarity | aluminum electrolytics | calc | §2.23.2 p.99 | high |
| SCHERZ-1041 | derating | Capacitor voltage rating: dielectric withstanding voltage (dwv, V per mil at a specified temperature) is a material limit; the dc working voltage (dcwv) includes temperature and safety margin and is the rating to design to. For ac signals the peak must not exceed the dcwv | V_peak <= dcwv | V_peak, dcwv | all capacitors | calc | §2.23.3 p.100 | high |
| SCHERZ-1042 | compliance | Never connect a capacitor across an ac power line unless it is designed (ac-line rated) for it - most dc-rated capacitors may short the line | ac-line rated part required | capacitor rating | mains-connected capacitors | inspect | §2.23.3 p.100 | high |
| SCHERZ-1043 | materials | Gas-gap breakdown: air spark voltage ~100 kV/cm for gaps as narrow as 0.005 cm, falling to "30 kV/mm" (as printed; ~30 kV/cm is consistent with the 3 MV/m of Table 2.3) for gaps as wide as 10 cm; breakdown also depends on electrode shape, pressure, humidity, temperature. Points/sharp edges break down at lower voltage - buff/round HV edges. Solid-dielectric capacitors are permanently damaged by breakdown (short, possibly explosion); gas-dielectric ones can be reused | E_bd ~ 30-100 kV/cm (air) | gap, electrode shape | HV gaps, air capacitors | calc | §2.23.3 p.100 | medium |
| SCHERZ-1044 | components | Capacitor i-v relation: I = C*dV/dt; V = (1/C)*integral(I dt); with constant current V = I*t/C. Worked: 10 uF charged at 50 mA reaches 0.05 V at 10 us, 50 V at 10 ms, 5000 V at 1 s (a typical capacitor won't survive); 47 uF driven by a 10 V/10 ms ramp draws 47 mA. Check V(t_max) against the rating | V = I*t/C <= V_rated | I, t, C | capacitors fed by current sources/ramps | calc | §2.23.5 p.102-105, Eq.2.40-2.41 | high |
| SCHERZ-1045 | power | A voltage step applied across a capacitor draws a current limited only by the series resistance (source internal R + capacitor internal R): I_peak = V/R_series, decaying exponentially; an ideal capacitor would need infinite current, so voltage across a real capacitor cannot change abruptly (inrush) | I_peak = V/R_series | V, R_series | switch-on of capacitive loads | calc | §2.23.5 p.103, Fig.2.98 | high |
| SCHERZ-1046 | components | Charge sharing: connecting a charged C1 (V0) across an uncharged C2 gives V = C1*V0/(C1 + C2). Worked: 1000 uF at 10 V shared with 470 uF -> 6.8 V on both | V = C1*V0/(C1+C2) | C1, C2, V0 | switched capacitor banks | calc | §2.23 p.97, Fig.2.94 | high |
| SCHERZ-1047 | compliance | A charged capacitor keeps its charge after the source is removed; leakage alone takes from a few seconds to several hours to discharge it, and earthing one plate does NOT discharge it. Discharge by connecting the plates together before handling | V_residual measured ~0 before handling | C, leakage | energy-storage capacitors | measure | §2.23 p.95-96, Fig.2.92 | high |
| SCHERZ-1048 | components | Energy stored in a capacitor: E = (1/2)*C*V^2 (ideal capacitor dissipates none). Worked: 1000 uF at 5 V stores 0.0125 J | E[J] = 0.5*C[F]*V[V]^2 | C, V | energy storage, hold-up, safety energy | calc | §2.23.7 p.105, Eq.2.42 | high |
| SCHERZ-1049 | timing | RC charging: V_C = Vs*(1 - e^(-t/RC)), I = (Vs/R)*e^(-t/RC), tau = RC; V_C = 63.2 % at 1 tau, 86.5 % at 2 tau, 95 % at 3 tau, 99.24 % at 5 tau ("fully charged"). Time to a threshold: t = -RC*ln((Vs - V_C)/Vs). Worked: IC trigger at 3.4 V from 5 V after 5 s with C = 10 uF -> R = 4.38e5 ohm | t = -R*C*ln((Vs-Vth)/Vs) | Vs, Vth, R, C | RC timing networks (timers, oscillators, delays) | calc | §2.23.8 p.105-107, Eq.2.43, Fig.2.101 | high |
| SCHERZ-1050 | protection | Capacitor discharge: V_C = Vs*e^(-t/RC); after 1 tau V_C = 36.8 % (printed "37.8 percent"); after 5 tau the capacitor is considered fully discharged (0.76 % left). Size high-voltage supply bleeders from t = 5*R*C: 100 uF shunted by 100 kohm needs 50 s after power-off | t_safe = 5*R_bleed*C | R_bleed, C, required discharge time | HV/filter capacitor bleeders | calc | §2.23.8 p.107-108, Eq.2.44, Fig.2.103 | high |
| SCHERZ-1051 | components | Parallel capacitors: C_tot = C1 + C2 + ...; the safe voltage of a parallel group is the LOWEST individual voltage rating. Put the voltage rating next to each capacitor symbol on the schematic; when missing, derive it from the expected node voltage | V_max_group = min(V_rated_i) | C_i, V_rated_i | capacitor banks | inspect | §2.23.10 p.108-109, Eq.2.45 | high |
| SCHERZ-1052 | components | Series capacitors: 1/C_tot = 1/C1 + 1/C2 + ... (C_tot < smallest); voltage ratings add but the voltage divides inversely to capacitance: V_i = (C_tot/C_i)*V_in - check that no individual rating is exceeded | V_i = V_in*C_tot/C_i <= V_rated_i | C_i, V_in | series stacks for higher voltage | calc | §2.23.11 p.109, Eq.2.46, Fig.2.104 | high |
| SCHERZ-1053 | components | Series capacitor stacks for high voltage: connect an equalizing resistor across each capacitor, about 100 ohm per volt of supply voltage, with sufficient power rating. Real leakage resistance can dominate the division - the capacitor with the highest parallel (leakage) resistance takes the highest voltage | R_eq ~ 100 ohm/V * V_supply; P_R = V_i^2/R_eq | V_supply, leakage | series electrolytic/film stacks | calc | §2.23.11 p.109-110 | high |
| SCHERZ-1054 | components | Capacitive reactance X_C = 1/(2*pi*f*C); falls with frequency (short at HF, open at dc); reactance dissipates no average power. Worked: 220 pF at 10 MHz = 72.3 ohm; 470 pF = 45.2 ohm at 7.5 MHz, 22.5 ohm at 15 MHz | X_C[ohm] = 1/(2*pi*f[Hz]*C[F]) | f, C | ideal capacitor, below self-resonance | calc | §2.23.13 p.111-112, Eq.2.47 | high |
| SCHERZ-1055 | decoupling | Real capacitors have parasitic R and L and self-resonate: at the self-resonant frequency the capacitive and inductive reactances cancel, leaving only the internal resistance; the impedance-vs-frequency curve departs from 1/(2*pi*f*C) - use the part's real impedance curve/SRF for the frequency of interest | use Z(f) of real part; f_use vs SRF | C, ESL, ESR, f | bypass/decoupling and RF capacitors | sim | §2.23.13 p.112, Fig.2.107b | medium |
| SCHERZ-1056 | components | Capacitive divider: Vout = Vin*C1/(C1 + C2) with the series element C1 in the numerator (opposite of a resistive divider); output is independent of frequency, but if the capacitances are small (high reactance at the frequency of interest) the output current capability is very low | Vout = Vin*C1/(C1+C2) | C1 (series), C2 (shunt) | ac or dc after settling | calc | §2.23.14 p.113, Fig.2.108 | medium |
| SCHERZ-1057 | components | Quality factor Q = X/R (reactance over total loss resistance). Good ceramic and mica capacitors reach Q of 1200 or more; small ceramic trimmers may have Q too small to ignore; microwave capacitors can be 10 or less at 10 GHz or higher | Q = X/R | X, R_loss | resonant/RF circuits | review | §2.23.15 p.113, Eq.2.48 | high |
| SCHERZ-1058 | emc | Ferrite beads (chokes) threaded over a wire/cable add inductance only over a limited range, typically RF; slip them over cables from notorious RF radiators (computers, dimmers, fluorescent lights, motors) so RF is absorbed as heat, and on cables entering receiving equipment to keep external RF out | bead on cable at RF source/receiver entry | cable list | RF interference suppression | inspect | §2.24.4 p.123, Fig.2.121 | high |
| SCHERZ-1059 | magnetics | Radio inductors often use air cores to avoid hysteresis and eddy-current core losses. Slug tuning: a ferrite/powdered-iron slug raises L; a brass (conductive, mu_r ~ 1) slug lowers L because eddy currents exclude flux from the coil centre | air core for RF; slug material sets tuning direction | frequency, core | RF coils, tunable inductors | review | §2.24.4 p.123 | high |
| SCHERZ-1060 | magnetics | Solenoid inductance L = mu*N^2*A/l (mu0 = 4*pi*1e-7 T*m/A); L scales with N^2 - to double L use sqrt(2) = 1.41x the turns (~40 % more), not 2x. Worked: 10 cm long, 0.5 cm radius, 1000 turns on a plastic form -> 1 mH | L[H] = mu0*mu_r*N^2*A[m^2]/l[m] | N, A, l, mu_r | long solenoid, core unsaturated | calc | §2.24.6 p.130-131, Eq.2.52-2.54 | high |
| SCHERZ-1061 | magnetics | Single-layer air-core coil (Fig.2.129): L(uH) = d^2*N^2/(18*d + 40*l), d = coil diameter (in), l = length (in); design N = sqrt(L*(18*d + 40*l))/d. Worked: 0.5 in form, 38 turns at 22 turns/in (l = 1.73 in) -> 4.62 uH; 8 uH on a 1 in x 0.75 in form -> 19.6 (use 20) turns at 26.1 turns/in -> #17 enameled wire or smaller; wind the turns then adjust spacing to a uniform 0.75 in | L[uH] = d^2*N^2/(18d+40l) | d, l (in), N | air-core solenoids | calc | §2.24.6 p.132, Fig.2.129 | high |
| SCHERZ-1062 | magnetics | Energy stored in an inductor: E = (1/2)*L*I^2 (a real inductor also loses a little to winding resistance) | E[J] = 0.5*L[H]*I[A]^2 | L, I | inductors, flyback energy | calc | §2.24.7 p.133, Eq.2.55 | high |
| SCHERZ-1063 | magnetics | Magnetic-core permeability varies with field (winding current) and temperature; at saturation mu_r drops to near 1 and hysteresis losses rise. Do not run a core inductor into saturation: lower the current, use a larger core, change the number of turns, use a lower-permeability core, or use a core with an air gap | I_peak < I_sat | I_peak, I_sat, core | iron/ferrite/powdered-iron inductors and transformers | calc | §2.24.8 p.135-136, Fig.2.132 | high |
| SCHERZ-1064 | magnetics | Eddy currents in conductive cores (steel) are resistive losses, higher in low-resistivity material: laminate steel cores with insulating varnish/shellac sheets. Ferrite resistivity is 10-1,000 ohm*cm (Mn-Zn) and 1e5-1e7 ohm*cm (Ni-Zn), so eddy losses are small - the reason ferrites are used at higher frequency; powdered iron limits eddy paths to particle size | laminate or use ferrite/powder at HF | core resistivity, f | power transformers, HF inductors | review | §2.24.8 p.134-135, Fig.2.131 | high |
| SCHERZ-1065 | magnetics | Core selection by frequency (Table 2.9): air core - mu_r 1, no saturation, low L, usable to ~1 GHz; iron core - mu ~1000x air, L depends on current (saturates), chiefly power supplies, laminate against eddy currents, significant hysteresis loss, limited to power-line and audio frequencies up to ~15,000 Hz, laminated iron useless at RF; powdered iron - low mu, RF up to VHF (slug-tuned), toroids self-shielding; ferrite - mu 20 to >10,000 (Ni-Zn low, Mn-Zn high), RF chokes and wideband transformers, non-conductive | laminated iron f <= ~15 kHz; air <= ~1 GHz | f, L, current | inductor/transformer core choice | review | §2.24.8 p.137, Table 2.9 | high |
| SCHERZ-1066 | magnetics | Toroid turns from inductance index AL. Powdered iron (AL in uH per 100 turns): L(uH) = AL*N^2/10,000, N = 100*sqrt(L_uH/AL). Ferrite (AL in mH per 1000 turns): L(mH) = AL*N^2/1,000,000, N = 1000*sqrt(L_mH/AL). Worked: T-12-2 (AL 20), 100 turns -> 20 uH; AL 36, 19.0 uH -> 72.6 turns; FT-50-61 (AL 68), 50 turns -> 0.17 (book prints uH; by its own formula the unit is mH); AL 188, 2.2 mH -> 108 turns | see formula | AL, N or L | single-layer toroids | calc | §2.24.8 p.137-138, Fig.2.133, Examples 5-8 | high |
| SCHERZ-1067 | protection | Inductive kick: V_L = L*dI/dt, averaged V = L*dI/dt. Worked: 1 H with current falling 0.60 -> 0.20 A gives -0.4 V over 1 s, -4 V over 100 ms, -40 V over 10 ms, -400 V over 1 ms (ideal instantaneous break -> infinite). Turning off inductive circuits can produce dangerously high voltages and arcing that need special handling (clamps/snubbers) | V = L*dI/dt | L, dI, dt | relay coils, solenoids, motors, any switched inductance | calc | §2.24.9 p.139-141, Example 11, Fig.2.135 | high |
| SCHERZ-1068 | magnetics | Model a real inductor as ideal L in series with its dc resistance R_DC; for high-frequency work add parallel (inter-turn) capacitance and parallel resistance for core losses. Core losses can make an inductor behave like a resistor and inter-turn capacitance can make it behave like a capacitor | L + R_DC (+ C_par, R_core) | datasheet L, R_DC, SRF | circuit models, simulation | sim | §2.24.8 p.136; §2.24.9 p.141, Fig.2.135d | high |
| SCHERZ-1069 | timing | RL time constant tau = L/R. Energizing: I = (Vs/R)*(1 - e^(-t/tau)), V_R = Vs*(1 - e^(-t/tau)), V_L = Vs*e^(-t/tau); t = -tau*ln(V_L/Vs). Deenergizing: I = (Vs/R)*e^(-t/tau) | tau = L/R | L, R, Vs | RL switching transients | calc | §2.24.4 p.125-126; §2.24.10 p.142, Fig.2.136 | high |
| SCHERZ-1070 | timing | An RL circuit's current is considered at full value after five time constants: t = 5*tau = 5*L/R. Worked: 10 mH with 10 ohm -> 5.0 ms; 1.0 H with 10 ohm -> 0.5 s (final current unchanged, only slower) | t_settle = 5*L/R | L, R | RL energize/deenergize | calc | §2.24.10 p.143, Example 13, Fig.2.137 | high |
| SCHERZ-1071 | protection | Opening a switch in an inductive circuit induces a voltage many times the applied voltage; the result is a spark/arc at the contacts, and with large L and high current the contacts can burn or melt. Suppress with an RC snubber (capacitor and resistor in series) across the contacts; protect transistor switches driving relays/solenoids with a small power diode reverse-connected across the coil | snubber across contacts / flyback diode across coil | load inductance, switch type | switched relays, solenoids, motors | inspect | §2.24.11 p.144, Fig.2.138 | high |
| SCHERZ-1072 | protection | Inductive switching spikes as high as a couple hundred volts occur even with relatively small supply voltages when relays, solenoids and motors are switched by mechanical or transistor switches; they cause arcing, contact degradation and damage to transistors/ICs. Fit a diode across the relay coil as the "pressure release" path | spike up to ~200 V at low supply V | coil, driver | inductive loads | inspect | §2.24.12 p.147, Fig.2.141 | high |
| SCHERZ-1073 | timing | RL (or RC) network driven by a square wave fully energizes/deenergizes within each half period only if 5*tau <= T/2 (tau <= T/10). Worked at 1 kHz (T = 1 ms), R = 10 ohm: L = 0.1 mH (tau 1 % of T) slightly rounded edges; 1 mH (tau 10 % of T) 5*tau equals the half period; 10 mH (tau = T) ramps look linear; 1 H (tau = 100*T) practically linear | tau <= T/10 for full settling | L, R (or C), f | pulse circuits, inductive loads under PWM | calc | §2.24.11 p.146, Fig.2.140 | medium |
| SCHERZ-1074 | rf | Straight-wire (parasitic) inductance: L(uH) = 0.00508*b*[ln(2b/a) - 0.75], a = wire radius (in), b = length (in); at VHF (30-300 MHz) and above the 0.75 tends to 1 as f -> infinity. Worked: #18 wire (0.0403 in dia) 4 in long = 0.106 uH -> 6.6 ohm at 10 MHz but 200 ohm at 300 MHz. Keep component leads as short as possible at VHF and above; model lead inductance in series with the component | L[uH] = 0.00508*b*(ln(2b/a)-0.75) | a, b (in), f | nonmagnetic wire in free space | calc | §2.24.13 p.147-148, Eq.2.56 | high |
| SCHERZ-1075 | magnetics | Coefficient of coupling between coils: air-core coils can reach 0.6-0.7 when one is wound over the other, much less when separated; near 100 % only on a closed magnetic core (transformers). Mutual inductance also injects unwanted voltages into circuits from neighbouring components, inductive loads and high-current ac cables | k_air <= 0.6-0.7 (overwound) | coil geometry | coupled coils, layout of magnetics | review | §2.24.14 p.148-149, Fig.2.143 | high |
| SCHERZ-1076 | crosstalk | Parallel-wire cables couple pulses magnetically and capacitively; the magnetic field of a changing current falls as the square of distance, so separating signal-carrying lines reduces inductive coupling; lines not well shielded and filtered stay susceptible. A long scope-probe ground lead picks up external magnetic interference as displayed noise | coupling ~ 1/d^2 | spacing, shielding | cables, probe grounding | review | §2.24.15 p.149 | high |
| SCHERZ-1077 | protection | Nearby or even distant lightning and heavy motorized equipment induce voltage spikes on ac/dc power lines and ground conductors that migrate into sensitive circuitry; equipment left plugged in during storms or near poorly filtered heavy equipment is at risk - provide transient suppression and filtering on power entry | TVS/filter at power entry | environment | mains-connected equipment | review | §2.24.15 p.149 | medium |
| SCHERZ-1078 | magnetics | Inductors combine like resistors (series sum, parallel reciprocal sum; two in parallel L1*L2/(L1+L2)) only when the coils are separated enough that neither is in the other's field (no mutual coupling) | L_series = sum(L_i) if k = 0 | L_i, spacing | discrete inductors | calc | §2.24.16 p.149-150, Eq.2.57-2.58 | high |
| SCHERZ-1079 | components | Inductive reactance X_L = 2*pi*f*L (current lags voltage by 90 deg). Worked: 100 uH = 0.075 ohm at 120 Hz, 9425 ohm at 15 MHz; 100 ohm at 100 MHz needs 0.16 uH; 1 uH reaches 2000 ohm at 318.3 MHz | X_L[ohm] = 2*pi*f[Hz]*L[H] | f, L | ideal inductor below self-resonance | calc | §2.24.17-2.24.18 p.150-153, Eq.2.59 | high |
| SCHERZ-1080 | magnetics | Real inductor = series L + R_DC with parallel C_P (distributed inter-turn/lead capacitance) and parallel R_P (core losses, derived from the self-resonant frequency and Q). Below self-resonance the reactance is inductive; above it the part is capacitive. Datasheets give R_DC (e.g. 1900-series 100 uH, R_DC = 0.0065 ohm); use the full model for critical HF filters (RF receivers) | operate below SRF | L, R_DC, C_P, SRF, Q | RF/HF inductors | sim | §2.24.19 p.153-154, Fig.2.147-2.148 | high |
| SCHERZ-1081 | magnetics | Inductor losses: winding resistance (size the wire for the anticipated current), skin effect (ac current crowds into a thinner surface layer as frequency rises) and core losses in conductive cores (iron, ferrite, brass) | wire sized for I_rms; account for skin effect at HF | I, f, core | inductor design/selection | review | §2.24.19 p.154 | high |
| SCHERZ-1082 | magnetics | Inductor quality factor Q = 2*pi*f*L/R_DC; inductor Q rarely approaches capacitor Q (quality ceramics >= 1200). Some circuits need the highest Q available, others a specific, possibly low, Q | Q_L = 2*pi*f*L/R_DC | f, L, R_DC | resonant circuits, filters | calc | §2.24.20 p.154 | high |
| SCHERZ-1083 | components | Inductive divider (inductors not on a common core, no mutual inductance): ac output ratio set by the inductances (Vout = Vin*L2/(L1+L2)) and independent of frequency; at dc it splits by winding resistances. If the reactances are not high at the operating frequency the shunt element L2 draws very large current | Vout/Vin = L2/(L1+L2) | L1, L2, f | ac dividers | calc | §2.24.20 p.155, Fig.2.149 | medium |
| SCHERZ-1084 | power | AC power bookkeeping: apparent power VA = I_rms*V_rms (volt-amperes); real power P = I_rms^2*R (watts, only resistance consumes); reactive power VAR = I_rms^2*X (never watts); VA = sqrt(P^2 + VAR^2); power factor PF = P/VA = cos(phi); reactive factor RF = VAR/VA = sin(phi). Worked: 12 VAC, 60 Hz into 50 ohm + 265 mH (X_L = j100 ohm): Z = 112 ohm at 63.4 deg, I = 0.107 A, VA = 1.284, P = 0.572 W, VAR = 1.145, PF = 0.45 lagging | PF = P/VA = cos(phi) | V_rms, I_rms, phi or R, X | sinusoidal steady state | calc | §2.27-2.28 p.173-179, Eq.2.74-2.80, Fig.2.167 | high |
| SCHERZ-1085 | power | Report power factor with "leading" or "lagging" - the number alone is insufficient: many dc-to-ac power inverters can safely operate loads with large net reactance of one sign but only a small reactance of the opposite sign | PF + sign (leading/lagging) | load reactance sign | inverter/UPS loads | review | §2.28.1 p.178 | high |
| SCHERZ-1086 | derating | Size ac components (transformers, inductors) on apparent power (VA), not real power: a transformer feeding a purely reactive load must still supply the full voltage and current, and winding I^2*R heats it. Inductors and transformers carry a volt-amp rating as their safe overheating limit | VA_rating >= V_rms*I_rms | load V, I | transformers, chokes on reactive loads | calc | §2.28.1 p.179; §2.28 p.184 | high |
| SCHERZ-1087 | derating | Near resonance, series L-C voltages and parallel L-C branch currents greatly exceed the source values. Worked: 1.00 VAC at 1 kHz into 25 mH + 1 uF + 1 ohm -> 67.4 V across L and 68.3 V across C (VAR ~29 VA each vs 0.18 W real); 10 VAC at 2893.7 Hz across 2.2 mH // 5.5 uF -> 1.0 A in C vs 0.75 A from source. Rate L and C for the circulating voltage/current, not the source value | V_L = I*X_L, V_C = I*X_C vs ratings | L, C, R, f | resonant/tuned circuits, filters | calc | §2.27.3 p.176; Examples 4-6 p.179-184 | high |
| SCHERZ-1088 | filter | LC resonance: f0 = 1/(2*pi*sqrt(L*C)) for both series and parallel LC. Series LC impedance -> 0 at f0 (current limited only by circuit resistance); ideal parallel LC impedance -> infinity (line current -> 0, circulating current between L and C). Worked: 5.0 uH with 35 pF -> 12 MHz; 21.1 MHz with 2.00 uH needs C = 28.5 pF; 100 uH with 62.5 nF -> 63,663 Hz (X_L = X_C = 40 ohm) | f0[Hz] = 1/(2*pi*sqrt(L[H]*C[F])) | L, C | tuned circuits; formulas adequate within component tolerances | calc | §2.30 p.188-191, Fig.2.176-2.177 | high |
| SCHERZ-1089 | filter | Series RLC at resonance: I = Vs/R (10 VAC, 5 ohm -> 2 A) and V, I in phase; unloaded Q_U = X_L0/R = omega0*L/R = (1/R)*sqrt(L/C) (40 ohm/5 ohm = 8; R = 10, 20, 50 ohm -> Q = 4, 2, 0.8; R = 2 ohm -> Q = 20). In HF tuned circuits the inductor's loss resistance dominates, so the inductor Q largely sets circuit Q | Q_U = omega0*L/R | L, C, R | series-resonant circuits | calc | §2.30.1-2.30.2 p.191-194, Fig.2.178-2.179 | high |
| SCHERZ-1090 | filter | Resonant bandwidth between half-power (-3 dB, 0.707 current) points: BW = f0/Q_U (curves approximately symmetrical for Q >= 10); equivalently Q_U = f0/BW. Worked: Q_U = 8 -> 12,500 Hz BW at 100 kHz, 125,000 Hz at 1 MHz; 7.75 MHz with 775 kHz BW -> Q_U = 10.0; loss 4 ohm with 200 ohm reactances -> Q 50, with 20 ohm -> Q 5 | BW[Hz] = f0/Q | f0, Q | Q >= 10 for symmetric approximation | calc | §2.30.3 p.194-196, Eq.2.81 | high |
| SCHERZ-1091 | derating | Reactive voltage in a series-resonant circuit: V_C = X_C*I, V_L = X_L*I; for Q > 10, V_X ~= Q_U*V_S. Worked: 10 VAC source, X = 40 ohm, I = 2 A -> 80 VAC (113 V peak) across L and C. High-Q circuits handling significant power (antenna couplers) can arc from reactive voltage even when the source voltage is well within component ratings - rate L and C for Q*V_S | V_X = Q_U*V_S (Q > 10) | Q, V_S | series-resonant, tuned output networks | calc | §2.30.4 p.195, Eq.2.82 | high |
| SCHERZ-1092 | filter | Capacitor leakage appears as a parallel resistance R_P; convert to series ESR before adding to coil resistance: R_S = X_C^2/R_P = 1/(R_P*(2*pi*f*C)^2). Worked: 10.0 pF with 9,000 ohm leakage at 40.0 MHz -> 17.6 ohm. Capacitor losses are insignificant below ~30 MHz but can reduce Q at VHF (30-300 MHz); combined with skin-effect rise of coil resistance they can seriously reduce Q | R_S = 1/(R_P*(2*pi*f*C)^2) | R_P, C, f | tuned circuits at VHF | calc | §2.30.5 p.195-196, Eq.2.83 | high |
| SCHERZ-1093 | filter | Parallel-resonant (antiresonant/"rejector") RLC with coil resistance R_S: for Q >= 10 replace R_S by the parallel "dynamic resistance" R_P = X_L^2/R_S = Q_U*X_L, which is the circuit impedance at resonance; the distinct resonant points (X_L = X_C, minimum current, unity PF) converge within about 1 % for Q > 10. Worked: 5.0 uH, 50 pF, 10.5 ohm -> f0 = 10.07 MHz, X_L = 316 ohm, Q_U = 30, Z = R_P = 9510 ohm | Z_res = Q_U*X_L = X_L^2/R_S | L, C, R_S | parallel tank circuits, Q >= 10 | calc | §2.30.6 p.196-199, Eq.2.84-2.85, Fig.2.180-2.182 | high |
| SCHERZ-1094 | derating | Circulating current in a parallel-resonant circuit: I_cir ~= Q_U*I_line (Q >= 10). Worked: Q 30 with 1 mA line current -> 30 mA (10 VAC across 316 ohm reactances -> 32 mA each); Q 100 with 50 mA line current -> 5 A. Circulating current can heat components and waste power - rate L and C for the circulating current, not the line current | I_cir = Q_U*I_line | Q, I_line | parallel tanks, high-Q tuned circuits | calc | §2.30.6 p.201-202, Eq.2.86 | high |
| SCHERZ-1095 | filter | Below ~30 MHz most tuned-circuit loss is in the inductor coil; adding turns raises reactance faster than coil resistance, so high-Q applications use large inductances. A resonant circuit loaded by a parallel resistance that dissipates >= 10x the internal L-C loss has Q_LOAD = R_LOAD/X (4000 ohm across 316 ohm reactances -> Q 13); low-resistance loads (a few kohm) need low-reactance elements (large C, small L) for reasonable Q | Q_LOAD = R_LOAD/X | R_LOAD, X | loaded tank circuits | calc | §2.30.7 p.202-203, Eq.2.87, Fig.2.185 | high |
| SCHERZ-1096 | filter | Widening a parallel-resonant circuit's bandwidth with a parallel load resistor: required Q_LOAD = f0/BW; since Z = Q*X, add R_par so the net impedance equals Q_LOAD*X. Worked: 14.0 MHz, want 400 kHz BW (Q 35) from Q_U 70 with 350 ohm reactances: Z 24,500 ohm -> 12,250 ohm, so add 24,500 ohm in parallel (also consider bandpass shape) | R_par such that R_P // R_par = Q_LOAD*X | f0, BW, Q_U, X | bandwidth trimming of tanks | calc | §2.30.7 p.203-204 | high |
| SCHERZ-1097 | requirements | Decibels: dB = 10*log10(P1/P0); dB = 20*log10(V1/V0) = 20*log10(I1/I0) valid only when the impedance is the same for both values. Power x2 = 3.01 dB, x4 = 6.02 dB, x8 = 12.04 dB; halving = -3.01 dB. Worked: 1 W -> 50 W = 17.00 dB. Absolute references: dBm (1 mW; 2e-13 mW = -127 dBm), dBW (1 W), dBd (dipole), dBi (isotropic), dBV (1 V), dB SPL (20 uPa) | dB = 10*log10(P1/P0) | P or V ratio, impedances | gain/attenuation specs | calc | §2.31 p.204-207, Eq.2.88-2.90, Table 2.12 | high |
| SCHERZ-1098 | requirements | Impedance bridging rule of thumb: a device's input impedance should be at least 10 times the output impedance of the source driving it (equivalently source Z_out <= 1/10 of load Z_in) so the input does not load the signal down substantially. Typical values: speaker 4 or 8 ohm; op-amp input 1-10 Mohm (nA input current); hi-fi preamp inputs 1 Mohm (radio), 500 kohm (CD), 100 kohm (tape); a decent lab supply has output impedance in the milliohm range, a battery more | Z_in >= 10*Z_out | Z_out(source), Z_in(load) | voltage-mode signal and supply interfaces | calc | §2.32.1-2.32.2 p.207-209, Fig.2.186-2.188 | high |
| SCHERZ-1099 | requirements | Compute Z_in = V_in/I_in with the actual load attached (e.g. divider Z_in = R1 + R2 // R_load); compute Z_out as the Thevenin impedance by shorting the source and removing the load (divider Z_out = R1 // R2). Both are frequency dependent when reactances are present (below ~1 kHz "input/output resistance" often suffices) | Z_out = Z_TH | circuit | any stage-to-stage interface | calc | §2.32 p.207-209, Fig.2.187-2.188 | high |
| SCHERZ-1100 | filter | First-order RC/RL filters: cutoff (-3 dB, 1/sqrt(2)) f_c = 1/(2*pi*R*C) (RC) or R/(2*pi*L) (RL); low-pass output lags 45 deg at f_c tending to 90 deg; high-pass leads 90 deg at LF, 45 deg at f_c. Worked: RC LP 50 ohm/0.1 uF -> 31,831 Hz; RL LP 500 ohm/160 mH -> 497 Hz; RC HP 10 kohm/0.1 uF -> 159 Hz; RL HP 1600 ohm/25 mH -> 10,186 Hz | f_c = 1/(2*pi*R*C); f_c = R/(2*pi*L) | R, C or L | unloaded first-order sections | calc | §2.33.1 p.210-218, Fig.2.189-2.195 | high |
| SCHERZ-1101 | filter | Loading a first-order filter: with load R_L, replace R by R' = R // R_L. RC low-pass: gain K = R'/R < 1 and f_c rises; RC high-pass: f_c rises; RL low-pass: f_c falls (omega_c = (R//R_L)/L), gain unaffected; RL high-pass: gain R'/R and f_c falls. The shift vanishes when R_L >> Z_out,max = R (condition for good voltage coupling). Z_in,min = R and Z_out,max = R for these sections | R_L >> R | R, R_L | passive filter stages driving loads | calc | §2.33.1 p.212-218, Fig.2.192-2.193 | high |
| SCHERZ-1102 | filter | Series-RLC bandpass loaded by R_LOAD: use R_T = R // R_LOAD in Q = X_L0/R_T; BW = f0/Q; f1,2 = f0 -/+ BW/2. Worked: 50 mH, 120 nF, R 500 ohm with 60 ohm load -> R_T 54 ohm, f0 2055 Hz, Q 12, BW 172 Hz, f1 1969 Hz, f2 2141 Hz. Notch (R1 in series with L-C-R_coil branch): 150 mH, 470 pF, R1 1000 ohm -> f0 18,960 Hz, Q 18, BW 1053 Hz, 18,430-19,490 Hz | Q = 2*pi*f0*L/R_T | L, C, R, R_LOAD | passive bandpass/notch | calc | §2.33.1 p.219-221, Fig.2.196-2.197 | high |
| SCHERZ-1103 | filter | Resistive attenuator between source and load: H = R2/(R1 + R2) unloaded; with source R_S and load R_L the source sees Z_in = R1 + R2 // R_L and the load sees Z_out = R2 // (R1 + R_S). Worked: R_S 1 ohm, R1 100 ohm, R2 3300 ohm, R_L 330 ohm, V_S 10 VAC -> Z_in 400 ohm, Z_out 98 ohm, V_TH 9.7 VAC, V_L 7.48 VAC | V_L = V_TH*R_L/(Z_TH + R_L) | R_S, R1, R2, R_L | frequency-independent attenuation | calc | §2.33.2 p.221-222, Fig.2.198 | high |
| SCHERZ-1104 | filter | Compensated attenuator: stray capacitance eventually makes a resistive divider act as a low- or high-pass filter; shunt each resistor with a capacitor so that R1*C1 = R2*C2 and attenuation becomes frequency independent (make one capacitor variable to trim strays). Used at oscilloscope inputs to raise input resistance and lower input capacitance at the cost of sensitivity | R1*C1 = R2*C2 | R1, R2, C1, C2 | wideband dividers, probe/scope inputs | measure | §2.33.2 p.222-223, Eq.2.91, Fig.2.199 | high |
| SCHERZ-1105 | timing | Transient initial conditions: a resistor's voltage/current can step instantly; a capacitor's voltage cannot change abruptly (an initially discharged capacitor acts as a short, I(0) = V_S/R); an inductor's current cannot change abruptly. Worked RL: 10 V, 10 ohm, 1 mH -> I = 1.0*(1 - e^(-10,000 t)) A | V_C(0+) = V_C(0-); I_L(0+) = I_L(0-) | circuit | switching transients | calc | §2.34 p.223-225, Fig.2.200-2.202 | high |
| SCHERZ-1106 | control-loop | Series RLC (capacitor pre-charged, then switched) damping regimes: overdamped if R^2 > 4L/C; critically damped if R^2 = 4L/C (R = 2*sqrt(L/C)); underdamped if R^2 < 4L/C, ringing at omega = sqrt(1/(LC) - R^2/(4L^2)) ~= 1/sqrt(LC) with envelope e^(-R*t/(2L)) (I = V0/(omega*L)*e^(-Rt/2L)*sin(omega*t)). For R^2 >> 4L/C the current rises in ~L/R to ~V0/R then decays with RC. Critical damping is hard to hold - a small change in R (or temperature) moves the circuit off it | R_crit = 2*sqrt(L/C) | R, L, C | LC filters, snubbers, input networks | calc | §2.34.1 p.231-235, Eq.2.92-2.97, Fig.2.210-2.212 | high |
| SCHERZ-1107 | emc | Spectral content of periodic/pulse waveforms: a waveform with half-wave symmetry (50 % square wave) contains only odd harmonics, V(t) = (4*V0/pi)*sum(sin(n*omega0*t)/n, n odd); unequal high/low times add even harmonics; an odd function has no dc component (a0/2 = average). A single rectangular pulse of width tau has abs(V(omega)) = 2*V0*sin(omega*tau/2)/omega with most of its spectrum within about 1/tau of zero - shorter pulses spread energy to higher frequency | harmonic n amplitude = 4*V0/(n*pi) (square) | V0, duty, tau | clock/PWM harmonics, EMC estimates | calc | §2.35-2.36 p.235-244, Eq.2.98-2.106, Fig.2.214-2.218 | high |
| SCHERZ-1108 | process | Simulation limits: SPICE results are only as accurate as the device models (often simplified); simulations are free of noise, crosstalk and interference unless you model them; SPICE is not a good predictor of component failure; simulators "can lie" when parameters are not understood. A simulation is not a prototype substitute - the breadboard gives the final answer | sim + prototype measurement both required | models, parasitics | all simulated designs | review | §2.37.2 p.249; §2.1 p.5 | high |
| SCHERZ-1109 | current-carrying | Allowable current from the B&S copper wire table (Table 3.1, 20 degC) must be reduced by 30 percent for rubber-insulated wire. Solid-core wire suits breadboards (does not fray) but snaps after repeated flexing | I_allow(rubber) = 0.7*I_table | AWG, insulation | hook-up and chassis wiring | calc | §3.1.1 p.253 | high |
| SCHERZ-1110 | current-carrying | Size copper hook-up/chassis wire from Table 3.1 (AWG 1-37: diameter, ohms/1000 ft, ohms/km, current-carrying capacity, nearest SWG). The tabulated capacity corresponds to ~700 circular mils per ampere (e.g. AWG 10: 10,383.61 CM/14.834 A; AWG 20: 1024 CM/1.463 A) | I_cap[A] ~= CM_area/700 | AWG | bare/enamel copper, B&S gauge, 20 degC; reduce 30 % for rubber insulation | calc | §3.1.1 p.253-255, Table 3.1 | medium |
| SCHERZ-1111 | cables | Stranded and braided conductors conduct better at ac than solid wire of the same diameter (greater total surface area vs skin effect) and survive flexing; solid-core wire snaps after repeated flexing (use it for breadboards). Braid doubles as an electromagnetic shield/return (coax) | stranded for flexing/HF runs | wire construction | hook-up wiring, cables | inspect | §3.1.1 p.253-254; §3.1.5 p.262 | high |
| SCHERZ-1112 | cables | Cable impedance classes: twin lead ("300-ohm line", stranded conductors) for antenna-receiver feed; unbalanced coax Z0 ~50 to 100 ohm (braid = return, geometry limits inductive/capacitive effects and external magnetic interference); balanced coax/shielded pair - shield is not a signal conductor, only a shield (foil shield tied to a drain/ground wire); CAT5 = four twisted pairs | Z0: twin lead 300 ohm, coax 50-100 ohm | cable type | signal/RF cabling | review | §3.1.2 p.256-258, Fig.3.3-3.4 | high |
| SCHERZ-1113 | connectors | Connector application limits stated in the text: coaxial dc barrel ("power") connectors carry low-voltage dc between 3 and 15 V; D-connectors carry up to 50 contacts (solder-cup); phone plugs have a 1-1/4 in (31.8 mm) barrel (3.5 mm and 2.5 mm versions common) for low-voltage, low-current audio; crimp connectors are colour-coded by the wire size they accept and suit dc connections broken repeatedly; alligator clips are temporary test leads only; 117 V plugs come polarized/unpolarized, with or without ground | dc barrel 3-15 V; D-sub <= 50 contacts | connector type, V, I | connector selection | inspect | §3.1.3 p.256-260, Fig.3.5 | high |
| SCHERZ-1114 | current-carrying | Skin effect raises ac resistance: R_ac/R_dc (Table 3.2) = 6.9 (AWG 22), 10.9 (18), 17.6 (14), 27.6 (10) at 1 MHz; 21.7/34.5/55.7/87.3 at 10 MHz; 68.6/109/176/276 at 100 MHz; 217/345/557/873 at 1 GHz. Reduce it with stranded wire (more surface) | R_ac = R_dc*ratio(AWG, f) | AWG, f | round copper wire at RF | calc | §3.1.5 p.262-263, Table 3.2 | high |
| SCHERZ-1115 | transmission-line | Cable characteristic impedance Z0 = sqrt(L'/C') from per-unit-length inductance and capacitance (Z0 is real - the line looks resistive). Worked: 21.0 pF/ft and 0.112 uH/ft -> 73 ohm | Z0[ohm] = sqrt(L'[H/ft]/C'[F/ft]) | L', C' (datasheet) | lossless line model | calc | §3.1.5 p.263-265, Fig.3.10-3.13, Table 3.4 | high |
| SCHERZ-1116 | transmission-line | Geometry formulas: coax Z0 = (138/sqrt(k))*log10(b/a), L = (mu0/(2*pi))*ln(b/a) H/m, C = 2*pi*eps0*k/ln(b/a) F/m (a = inner-conductor radius, b = shield inner radius); parallel wire Z0 = (276/sqrt(k))*log10(D/a), L = (mu0/pi)*ln(D/a), C = pi*eps0*k/ln(D/a) (D = centre spacing, a = wire radius); mu0 = 1.256e-6 H/m, eps0 = 8.85e-12 F/m. Worked: RG-58/U a = 0.032 in, b = 0.116 in, polyethylene k = 2.3 -> 51 ohm; parallel wire a = 0.0127 in, D = 0.270 in, k = 2.3 -> 242 ohm | see formula | a, b or D, k | coax and twin line | calc | §3.1.5 p.264-266, Fig.3.12, Fig.3.14-3.15 | high |
| SCHERZ-1117 | termination | A line terminated in a load unequal to Z0 reflects part of the signal (inverted if Z_L > Z0). VSWR = V_rms,max/V_rms,min = Z0/R_L or R_L/Z0 (whichever >= 1) = (V_F + V_R)/(V_F - V_R); reflected power % = ((VSWR - 1)/(VSWR + 1))^2 * 100 %, absorbed = 100 % - reflected. Worked: 50 ohm line into 200 ohm -> VSWR 4:1, 36 % reflected, 64 % absorbed; VSWR 1 = properly terminated | P_refl = ((S-1)/(S+1))^2 | Z0, R_L | resistive loads on transmission lines | calc | §3.1.5 p.266-269, Fig.3.16-3.18 | high |
| SCHERZ-1118 | termination | Impedance matching is needed only at high frequency: when the signal wavelength is much larger than the cable length no matching is required. Instruments/video gear typically match 50 ohm coax; TV antenna inputs match 300 ohm twin lead, so matching is already handled there | match when cable length not << lambda | f, cable length, v | cabling decisions | calc | §3.1.5 p.269 | high |
| SCHERZ-1119 | matching | Resistive L-pad between purely resistive impedances Z1 > Z2: shunt/series values RB = Z2/sqrt(1 - Z2/Z1), RA = Z1*Z2/RB; the pad has inherent insertion loss = 10*log10((P_pad + P_load)/P_load). Speaker L-pads come in 4, 8, 16 ohm; T and Pi pads are alternatives (Pi in amplifiers, T in transmatches) | RB = Z2/sqrt(1-Z2/Z1); RA = Z1*Z2/RB | Z1, Z2 | audio and RF resistive matching | calc | §3.1.5 p.270, Fig.3.19 | high |
| SCHERZ-1120 | matching | Matching transformer: turns ratio Np/Ns = sqrt(Z0/Z_L) (square-root sign lost in the text extraction; consistent with the worked example). Worked: 800 ohm line to 8 ohm load -> ratio 10 (e.g. 10:1 or 20:2) | Np/Ns = sqrt(Z0/Z_L) | Z0, Z_L | transformer matching | calc | §3.1.5 p.270, Fig.3.20 | medium |
| SCHERZ-1121 | matching | Broadband transmission-line transformer (a few turns of miniature coax or twisted pair on a ferrite core, e.g. Z0 to 4*Z0) avoids conventional-transformer resonances and gives less than 1 dB loss from 0.1 to 500 MHz | loss < 1 dB, 0.1-500 MHz | impedance ratio | RF broadband matching | review | §3.1.5 p.270, Fig.3.21 | high |
| SCHERZ-1122 | matching | Quarter-wave matching section: insert a lambda/4 length of line with Z_sec = sqrt(Z0*Z_L); lambda = v/f, v = c/sqrt(k), c = 3.0e8 m/s (square roots lost in extraction). Worked: 50 ohm cable (k = 1) to 200 ohm load at 100 MHz -> lambda = 3 m, section 0.75 m long of 100 ohm line. Stubs (open/short) can cancel standing waves but need handbook graphs | Z_sec = sqrt(Z0*Z_L); l = c/(4*f*sqrt(k)) | Z0, Z_L, f, k | narrowband RF matching | calc | §3.1.5 p.270-271, Fig.3.22-3.23 | medium |
| SCHERZ-1123 | components | Primary-cell chemistry selection: carbon-zinc (1.5 V, falls during service) - intermittent low-power only, leakage-prone, poor shelf life especially hot; never leave in expensive equipment, avoid standby and wide-temperature use. Zinc-chloride - ~50 % more capacity, better at low temperature, moderate intermittent use. Alkaline (1.5 V) - lower internal resistance until end of life, long shelf life, but high-drain devices (digital cameras) greatly shorten its life | choose by duty cycle and drain | load profile, temperature, storage | primary-battery products | review | §3.2.3 p.275, Table 3.5 | high |
| SCHERZ-1124 | components | Lithium primary (Li-MnO2): nominal 3.0 V, almost flat discharge, very low self-discharge (shelf life up to 10 years), low internal resistance, good at low and high temperature - suited to low-drain long-life loads (smoke detectors, data retention, pacemakers, watches, calculators) | V_nom = 3.0 V | load, life | long-life primary | review | §3.2.3 p.275-276 | high |
| SCHERZ-1125 | components | Lithium-iron disulfide AA (1.5 V "voltage-compatible", not rechargeable, ~66 % of alkaline weight) wins under heavy load (>260 % of alkaline run time) but the advantage can reverse at light load: 20 mA -> 122 h vs alkaline 135 h; 1 A -> 2.1 h vs 0.8 h. Pick chemistry from the actual load current | runtime(chem, I_load) | I_load | AA-format primaries | calc | §3.2.3 p.276 | high |
| SCHERZ-1126 | components | Button cells: mercury (zinc-mercuric oxide) 1.35 V, very flat, near-constant internal resistance (suits voltage references); silver oxide slightly over 1.5 V, flat, >90 % charge after 5 years storage (NaOH watch types: low-drain continuous ~5 years; KOH types: low drain with periodic high pulses ~2 years); zinc-air 1.45 V, runs ~60 days once the seal is removed, moderately low internal resistance, not for heavy or pulsed discharge, best when capacity is used within a few weeks | V_nom: Hg 1.35, AgO ~1.5, Zn-air 1.45 | load profile | coin/button-cell products | review | §3.2.3 p.276-277, Fig.3.27, Table 3.5 | high |
| SCHERZ-1127 | components | Sealed lead-acid (gel): operated at low potential so never fully charged -> lowest energy density of sealed secondaries (~30 Wh/kg) but cheapest; lowest self-discharge (~5 %/month); no memory; prefers shallow cycling; 8-16 h full recharge; must be stored charged (discharged storage causes sulfation). Lead-acid charging uses voltage limiting (NiCd/NiMH use current limiting) - follow the maker's charge directions; flooded cells must stay upright and gas. Sizes 2, 4, 6, 8, 12 V; 1 to several thousand Ah | V_cell 2.0 V; store charged | charger type, storage | backup/UPS, stationary storage | review | §3.2.4 p.279-280, Table 3.6 | high |
| SCHERZ-1128 | components | NiCd: 1.2 V/cell average (vs 1.5 V alkaline; most energy delivered above 1.0 V/cell) - equipment needing four or more alkaline cells may not work on NiCd; self-discharge in 2-3 months; memory effect -> unsuitable for shallow cycling or float charging, best deep-cycled; ~1000 cycles; charge with a constant-current charger observing heat, wattage and polarity; safe extended-period charge rate is C/10 (10 h) | I_charge_extended <= C/10 | cell count, V_min of load | NiCd packs | calc | §3.2.4 p.280-281, Table 3.6 | high |
| SCHERZ-1129 | components | NiMH: 1.2 V/cell (derate designs built for 1.5 V cells), 30-40 % more energy density than NiCd, self-discharge 2-3 months, slight memory; best load current 0.2C-0.5C; charging generates significant heat and needs a special algorithm with trickle charge and temperature sensing; regular full discharge prevents crystalline formation. Typical capacities: AAA 1000, AA 2300, C 5000, D 8500, 9 V 250 mAh | I_load 0.2C-0.5C | capacity, I_load | NiMH packs | calc | §3.2.4 p.281; §3.2.5 p.288 | high |
| SCHERZ-1130 | components | Li-ion: no memory, ~6 %/month self-discharge, cannot be trickle or float charged, ages even unused, and must carry built-in protection against over-discharge and overcharge (smart pack). Charging is voltage-limited: typical protection threshold 4.30 V/cell; temperature sensing disconnects the charger if internal temperature approaches 90 degC (194 degF); a mechanical pressure switch permanently opens on overpressure. At 1C initial current charge takes ~3 h; charge is complete when the voltage has reached the upper threshold and the current has fallen and levelled at ~3 % of nominal charge current; raising charge current barely shortens charge time | V_cell_max 4.30 V; T_cutoff ~90 degC; I_term ~0.03*I_chg | charger design, pack protection | Li-ion cells/packs | review | §3.2.4 p.281-282 | high |
| SCHERZ-1131 | components | Li-polymer: cells as thin as 1 mm; dry-polymer electrolyte has high internal resistance and cannot deliver current bursts (conductivity improves with temperature); commercial gelled hybrids behave like Li-ion and use the same charge algorithm, 1-3 h typical charge | burst current limited (dry) | I_peak | thin packs | review | §3.2.4 p.282-283 | high |
| SCHERZ-1132 | components | NiZn: 1.65 V nominal, >0.4 V/cell above NiCd - a 19.2 V NiZn pack replaces a 14.4 V NiCd pack with 25 % less cell space and 45 % lower impedance; full recharge < 2 h (80 % in 1 h). NiFe: 1.4 V open circuit, ~1.2 V under discharge, tolerates overcharge, over-discharge and long discharged storage, 30-80 year life (lead-acid ~5 years), but heavy and high self-discharge | V_nom NiZn 1.65 V; NiFe 1.4 V | pack voltage | power tools, long-life stationary | review | §3.2.4 p.283, Table 3.6 | high |
| SCHERZ-1133 | components | Rechargeable alkaline-manganese (RAM): capacity can fall 50 % after only 8 cycles; light-duty shallow cycling only; lower nominal voltage than primary alkaline; up to 10 years standby. Charge only with a RAM-specific charger - standard chargers may make them explode | RAM-specific charger | charger | low-cost rechargeable | inspect | §3.2.4 p.285 | high |
| SCHERZ-1134 | components | Supercapacitors: aqueous electrolyte limits a cell to 1 V (low internal resistance); organic allows 2-3 V (higher resistance); series strings of more than three or four cells need voltage balancing. Values 0.22 F to several F; energy ~1/5-1/10 of an electrochemical battery (~1/10 of NiMH). Voltage falls linearly to 0 V, so only part of the charge is usable: a 6 V system cutting off at 4.5 V uses only the first quarter. Self-discharge: organic types can fall to 30 % in ~10 h; longer-retention types 85 % at 10 days, 65 % at 30 days, 40 % at 60 days | usable charge fraction = (V_max - V_cut)/V_max; balance if n_series > 3 | C, V_max, V_cut, n | backup/hold-up storage | calc | §3.2.4 p.285-286 | high |
| SCHERZ-1135 | power | Supercapacitor in parallel with a battery (with provision to limit the inrush current at switch-on) supplies pulsed load current, smoothing battery current, extending runtime and battery life; main uses are memory backup and RTC standby. Virtually unlimited cycle life; low-impedance types charge within seconds; a simple voltage-limiting charger compensates self-discharge | inrush limiting required | pulse load profile | battery + supercap buffering | review | §3.2.4 p.286 | high |
| SCHERZ-1136 | power | Battery runtime estimate: t = capacity/I_load (1800 mAh at 120 mA -> 15 h, ideal). Real runtime is shorter at higher currents (internal resistance): use the maker's discharge curves (voltage vs time at the load current) and Peukert's equation (printed "Peurkert") | t[h] = C[mAh]/I[mA] (ideal) | capacity, I_load | battery life budgets | calc | §3.2.5 p.287-289 | high |
| SCHERZ-1137 | power | C-rate: 1C draws a current equal to the rated capacity for 1 h (1000 mAh -> 1000 mA); t = 1 h/C-rate: 5C 0.2 h, 2C 0.5 h, 0.5C 2 h, 0.2C 5 h, 0.05C 20 h. Most portable batteries except lead-acid are rated at 1C; at large C values capacity falls below nominal | I = C_rate*capacity; t = 1 h/C_rate | capacity, I | charge/discharge rating | calc | §3.2.5 p.288-289 | high |
| SCHERZ-1138 | power | Battery internal resistance divides with the load: V_load = V_oc*R_load/(R_in + R_load); R_in rises with discharge (AA alkaline 0.15 ohm fresh -> 0.75 ohm at 90 % discharged); high-R_in batteries perform poorly on high-current pulses. Typical R_in: 9 V zinc-carbon 35 ohm, 9 V lithium 16-18 ohm, 9 V alkaline 1-2 ohm, AA alkaline 0.15 ohm (0.30 at 50 %), AA NiMH 0.02 ohm (0.04 at 50 %), D alkaline 0.1 ohm, D NiCd 0.009 ohm, D SLA 0.006 ohm, AC13 zinc-air 5 ohm, 76 silver 10 ohm, 675 mercury 10 ohm (check specific datasheets) | V_load = V_oc*R_L/(R_in+R_L) | V_oc, R_in (end-of-life), R_L or I | battery-powered loads, pulse loads | calc | §3.2.6 p.289-290, Fig.3.32 | high |
| SCHERZ-1139 | components | Relay family limits: mechanical relays typically 2-15 A with 10-100 ms switching; reed relays 500 mA-1 A with 0.2-2 ms; solid-state relays from a few uA up to 100 A with 1-100 ns switching (as printed). Reed and solid-state relays are usually limited to SPST and tend to be damaged by power surges | I_contact <= family rating | load current, speed | relay selection | review | §3.4 p.295-296 | high |
| SCHERZ-1140 | components | Typical relay coil data: dc mechanical relays 6, 12, 24 V dc with ~40, 160, 650 ohm coils; ac relays 110 and 240 V ac with ~3400 and 13,600 ohm; miniature relays 5, 6, 9, 12, 24 V dc with 50-3000 ohm; reed relays 5, 6, 12, 24 V dc with ~250-2000 ohm. Size the coil driver for I = V_coil/R_coil | I_coil = V/R_coil | V_coil, R_coil | relay driver design | calc | §3.4.1 p.297 | high |
| SCHERZ-1141 | components | Drive a relay coil within +/-25 % of its specified control voltage: too much damages or destroys the coil; too little may not trip it or makes it act erratically (flip back and forth) | abs(V_coil - V_rated) <= 0.25*V_rated | V_drive, V_rated | all electromechanical relays | calc | §3.4.2 p.298 | high |
| SCHERZ-1142 | components | A dc-coil relay fed with ac chatters (the armature flips with each polarity reversal) - use an ac-coil relay on ac. Latching relays hold their state after the control pulse is removed and need a separate pulse to reset | coil type matches drive | coil type, drive | relay selection | inspect | §3.4 p.296 | high |
| SCHERZ-1143 | protection | Relay-coil turn-off spikes can reach ~1000 V, zapping switches, transistors and people and hammering the contacts. DC coil: reverse-biased diode across the coil whose peak current rating >= the coil current before interruption (1N4004 is a good general-purpose choice). AC coil: a diode (or anti-parallel diodes) cannot be used; put a series RC across the coil - R = 100 ohm, C = 0.05 uF works for most small line-powered loads - with R and C rated for a transient current as large as the coil current and C rated for ac line voltage; bidirectional TVS or MOV are alternatives | I_diode_pk >= I_coil; AC: R 100 ohm + C 0.05 uF | coil current, supply type | relay, solenoid, transformer coils | inspect | §3.4.2-3.4.3 p.298-299, Fig.3.45-3.46 | high |
| SCHERZ-1144 | components | Solid-state relays: ac types use an opto-isolator with zero-crossing detection and a triac (switch near 0 V in the cycle); dc types use a MOSFET or IGBT. The opto input needs only a couple of mA and isolates control from load | I_control ~ few mA | load type (ac/dc) | SSR selection | review | §3.4.1 p.297 | high |
| SCHERZ-1145 | components | Resistor markings: 4-band = digit, digit, multiplier, tolerance (no 4th band = +/-20 %); 5-band precision = 3 digits, multiplier, tolerance (wider gap before tolerance band); military 5th band = reliability (% change per 1000 h: brown 1 %, red 0.1 %, orange 0.01 %, yellow 0.001 %); SMD 3-digit = 2 significant + multiplier with "R" as decimal point (1R0 = 1.0 ohm) and a tolerance letter suffix when tighter than ~+/-2 % (F = +/-1 %); SMD 4-digit precision = 3 significant + multiplier | per code | marking | BOM/assembly inspection | inspect | §3.5.3 p.304-305, Fig.3.52 | high |
| SCHERZ-1146 | compliance | White or blue resistor bodies mark nonflammable or fusible resistors; never replace one with an ordinary resistor - it may create a fire hazard under fault | same-type replacement only | body colour, BOM | service/rework of consumer equipment | inspect | §3.5.3 p.305 | high |
| SCHERZ-1147 | derating | Resistor voltage rating: maximum dc or RMS voltage at specified ambient; relates to power by V = sqrt(P*R). Critical resistance R_crit = V_rated^2/P_rated: below it the power rating limits, above it the voltage rating limits. 1/2 W and some 1 W resistors are rated only 250-350 V; for high voltage use e.g. 1 W (continuous, 1000 V surge) or 2 W, 750 V rated parts | V_applied <= min(sqrt(P_rated*R), V_rated) | R, P_rated, V_rated | high-value/high-voltage resistors, HV dividers | calc | §3.5.4 p.306-307 | high |
| SCHERZ-1148 | components | Resistor tolerance (at 25 degC, no load): typical 1, 2, 5, 10, 20 %. Carbon composition 5-20 %; carbon film 1-5 %; metal film ~1 %; precision metal film to 0.1 %; wirewound 1-5 %; precision wirewound +/-0.005 %; foil 0.0005 %. 5 % is adequate for most general-purpose use | R in [R_nom*(1-tol), R_nom*(1+tol)] | tolerance, technology | worst-case analysis | calc | §3.5.4 p.307 | high |
| SCHERZ-1149 | derating | Resistor power rating applies at +25 degC; above that follow the maker's linear derating curve from the full-rated-load temperature to the maximum no-load temperature (which is also the maximum storage temperature). Resistance recovers after 30-40 degC excursions, but a resistor too hot to touch may be permanently damaged - be conservative | P_allow(T) = P_rated*(T_max0 - T)/(T_max0 - T_full) above T_full | T_ambient, derating curve | all resistors above rated ambient | calc | §3.5.4 p.307-308, Fig.3.54 | high |
| SCHERZ-1150 | derating | Standard resistor power ratings: 1/16, 1/10, 1/8, 1/4, 1/2, 1, 2, 5, 10, 15, 25, 50, 100, 200, 250, 300 W; select 2 to 4 times the calculated dissipation. For grouped/enclosed/fan-cooled/pulsed/high-altitude parts multiply the dissipation by the Fig.3.55 factors: worked example - four resistors each dissipating 115 W, 2 in surface-to-surface, totally enclosed, 50 degC ambient -> factors 2.0 x 1.2 x 1.1 = 2.64 -> 304 W free-air rating each | P_rating >= 2..4*P_calc; P_free_air = P*prod(F_i) | P, grouping, enclosure, T_amb | power resistor selection | calc | §3.5.4 p.308-309, Fig.3.55 | high |
| SCHERZ-1151 | components | Temperature coefficient of resistance: dR/R = TC[ppm/degC]*dT*1e-6; 100 ppm/degC = 0.1 % per 10 degC, 1 % per 100 degC. Worked: 1000 ohm, +200 ppm/degC, 27 -> 50 degC -> +4600 ppm -> 1004.6 ohm. Available TCs span +/-1 to +/-6700 ppm/degC; metal film 50-100; precision film 20, 10, 5, 2 ppm/degC (0.01 % accuracy); carbon film negative, around -500 to -800 ppm/degC (also quoted 100-200 ppm on p.316) - do not substitute carbon film for metal film; carbon composition high TC - avoid in stable precision circuits; buy matched-TC sets where ratio tracking matters | dR = R*TC*dT/1e6 | TC, dT (self-heating + ambient) | precision/stable circuits, dividers | calc | §3.5.4 p.308-310; §3.5.5 p.315-316 | high |
| SCHERZ-1152 | components | Resistor frequency response: useful frequency range ends where the impedance differs from R by more than the tolerance. Low-reactance designs reach < 1 uH (500 ohm) and < 0.8 pF (1 Mohm); fast-rise resistors <= 20 ns. Wirewounds are worst (a 20 ns pulse may be missed entirely; foil reproduces it); film resistors hold constant impedance to ~100 MHz then fall; smaller diameter is better; HF resistors have length/diameter 4:1 to 10:1 | abs(Z(f)-R)/R <= tol | f, technology | pulse/RF/fast circuits | review | §3.5.4 p.310-311, Fig.3.56 | high |
| SCHERZ-1153 | components | Johnson (thermal) noise: V_rms = sqrt(4*k*R*T*df), k = 1.38e-23 J/K, T in K, df in Hz; identical for equal-value resistors of any material - only a lower resistance reduces it, so avoid e.g. 10 Mohm resistors in amplifier input stages | V_n = sqrt(4kTR*B) | R, T, bandwidth | low-level analog inputs | calc | §3.5.4 p.311-312 | high |
| SCHERZ-1154 | components | Excess (current/contact) noise is 1/f and grows with current; current noise ~ sqrt(current); it exists in carbon composition, carbon film, metal oxide and metal film but not wirewound. Noise index NI = 20*log10(noise V/dc V) in uV/V; band noise V_rms = V_dc*10^(NI/20)*[log10(f2/f1)] (a square root on the log term appears lost in extraction). Reduce with low current and a larger power rating (a 2 W carbon-composition part beats a 1/2 W one). Quietest to noisiest: precision wirewound, precision film, metal oxide, carbon film, carbon composition. Carbon pots (e.g. 1 Mohm volume) are major noise sources - use conductive plastic, lowest practical value, largest practical rating | minimize I_dc and use larger P rating | technology, I_dc | low-noise amplifier stages | review | §3.5.4 p.312-313 | medium |
| SCHERZ-1155 | components | Shot noise rises with average dc current - keep dc current low in first/low-level amplifier stages and use wirewound or metal-film resistors there (not wirewound in HF amplifiers, because of inductance) | low I_dc in first stage | I_dc, f | preamp/first stages | review | §3.5.4 p.312 | high |
| SCHERZ-1156 | components | Voltage coefficient of resistance (carbon composition and carbon film): VC = 100*(R1 - R2)/(R2*(V1 - V2)) %/V, with R1 at rated voltage V1 and R2 at 10 % of rated voltage V2 | VC[%/V] per formula | R at two voltages | HV dividers with carbon parts | calc | §3.5.4 p.313 | high |
| SCHERZ-1157 | reliability | Resistor stability: wirewound and bulk-metal best, composition least stable. Operate critical resistors with limited temperature rise and load; wide and rapid temperature cycling shifts resistance (and can destroy the part); humidity swells insulation and shifts value. Reliability is quoted as MTBF or failure rate per 1000 h; a typical temperature rating is full load to +85 degC derated to no load at +145 degC, ranges e.g. -55 to +275 degC | limit dT and load on critical R | thermal cycling, humidity | precision/long-life designs | review | §3.5.4 p.313 | high |
| SCHERZ-1158 | components | Resistor classes: general-purpose - initial variation ~5 %, up to ~20 % change at full rated power, high TC and noise; power resistors - ~5 % operational stability acceptable (film types more stable at high frequency and reach higher values than wirewound); precision - low voltage/power coefficients, excellent temperature/time stability, low noise and reactance | budget up to 20 % drift for general-purpose at full power | class | worst-case budgets | calc | §3.5.5 p.314 | high |
| SCHERZ-1159 | components | Precision wirewound: TC as low as 3 ppm/degC, tolerance to 0.005 %, -55 to +200 degC range (max operating 145 degC), life 10,000 h at rated temperature and load with ~0.10 % change. Inductive at low frequency and capacitive higher (low-Q resonance) - unsuitable above 50 kHz; reserve for precision dc (measuring equipment, regulator references); "HS" windings cut inductance | f_use <= 50 kHz | f, accuracy | precision dc references | review | §3.5.5 p.314-315 | high |
| SCHERZ-1160 | thermal | Chassis-mount (aluminium-housed) power wirewound resistors reach about five times their free-air power rating only when bolted to a metal plate/chassis heat sink | P_rating(mounted) ~ 5x free-air, requires heat sink | mounting | power resistor installation | inspect | §3.5.5 p.315 | high |
| SCHERZ-1161 | components | Carbon composition: tolerance 5-20 %, typically rated ~70 degC for 1/8-2 W, end-to-end shunt capacitance noticeable near 100 kHz for values above 0.3 Mohm, low noise above ~1 Mohm. Its bulk element survives short heavy overloads without flashover, whereas a metal-film spiral can arc and destroy itself - use carbon composition as the series resistor when discharging a high-voltage capacitor. Metal film is best for microsecond rise times/MHz | carbon comp for HV discharge/surge | overload energy | surge/discharge resistors | review | §3.5.5 p.315-317 | high |
| SCHERZ-1162 | components | Surge capability by technology: thin film (< 1 um NiCr) has limited surge capability; thick film (~12 um RuO2) exceeds thin film by one to two orders of magnitude; metal-oxide (flameproof, blue or white body) is ideal for pulse power, snubbers and current limiting (0.5-5 W, +/-1 to +/-5 %, ~+/-300 ppm/degC); cement resistors 1-20 W, ~5 %, ~300 ppm/degC; bulk-metal foil to 0.005 % and 0.2 ppm/degC; chip arrays 1 %/5 %, 50-200 ppm/degC | pulse loads: thick film/metal oxide/carbon comp | pulse energy | snubbers, inrush, pulse | review | §3.5.5 p.317-319 | high |
| SCHERZ-1163 | protection | Fuse resistors open-circuit on a surge or fault (energy to melt and vaporize the element); they run hotter than normal resistors, and their fusing point depends strongly on mounting and heat transfer (long pulses are hard to predict) - many mount in fuse clips for accurate fusing; fast- and slow-burn types exist | fusing verified in the actual mounting | mounting, pulse duration | overload protection (chargers, TVs, fans) | measure | §3.5.5 p.318-319 | high |
| SCHERZ-1164 | components | Potentiometer ratings: the power rating assumes dissipation spread over the whole element - if only a quarter of the element carries the rated power the pot fails quickly; a constant voltage between wiper and one end with the setting turned down exceeds the wiper current rating; some trimmers are not rated for any significant dc wiper current (even 1 mA causes electromigration -> open or noisy wiper) | P_element_fraction and I_wiper within rating | configuration, setting range | pots/trimmers carrying current | calc | §3.5.7 p.324 | high |
| SCHERZ-1165 | components | Potentiometer selection: single-turn ~270 deg; multiturn 10 or 20 turns (settability can be 2-4x worse than a single-turn pot); use log (audio) taper for volume (a linear pot squeezes the useful range into the first ~60 deg); cheap log pots are two-slope with the break near 50 % rotation; best pots keep hop-on/hop-off resistance below ~1 % of total. Taper codes: modern Asian A = log, B = linear; older A = linear, C = log/audio, F = antilog | taper code verified against supplier convention | taper, code | user controls, trimming | inspect | §3.5.6-3.5.7 p.320-323 | high |
| SCHERZ-1166 | derating | Capacitor ac rating: peak ac must not exceed the dc working voltage, i.e. V_rms <= 0.707*DCWV unless otherwise specified; many types need further derating as frequency increases | V_rms <= 0.707*DCWV | V_rms, DCWV, f | capacitors with ac stress | calc | §3.6.7 p.329-330 | high |
| SCHERZ-1167 | components | Capacitor leakage: electrolytics leak 5-20 nA per uF - not suited for storage, sample-hold or high-frequency coupling; polypropylene/polystyrene film insulation resistance typically > 1e6 Mohm. Insulation resistance is specified in Mohm*uF: R_leak = (Mohm*uF)/C(uF) | I_leak(elec) = 5..20 nA/uF * C | C, type | hold/timing/coupling capacitors | calc | §3.6.7 p.330, p.332 | high |
| SCHERZ-1168 | components | ESR lumps all capacitor losses at one frequency: ESR = X_C/Q = X_C*DF; loss P = I_rms^2*ESR. High ESR heats and degrades a capacitor carrying large ac/ripple current (power supplies, high-current filters, RF); low-ESR types include mica and film. Also check I_rms (maximum ripple current at a given frequency) and I_peak (non-repetitive pulses at 25 degC) | P = I_rms^2*ESR; I_rms <= rating | ESR or DF, X_C, I_rms | filter, decoupling, snubber capacitors | calc | §3.6.7 p.330-332 | high |
| SCHERZ-1169 | decoupling | ESL: rolled electrolytic, paper and plastic-film capacitors act more like inductors than capacitors above a few MHz - poor for HF decoupling; use monolithic (multilayer) ceramic for HF decoupling (very low series inductance), accepting that ceramics can be microphonic and some self-resonate with high Q; disc ceramics are often quite inductive. Lead length and construction set the self-resonant frequency, which (impedance minimum = ESR) is the practical upper frequency limit | f_use < SRF | ESL, lead length, type | supply decoupling of fast analog/digital parts | review | §3.6.7 p.331-332, Fig.3.65 | high |
| SCHERZ-1170 | components | Dielectric absorption (charge memory) ruins sample-hold and integrator accuracy: monolithic ceramics have considerable DA (unsuitable as hold capacitors); low-DA choices (printed < 0.01 %) are polyester, polypropylene and Teflon, with polystyrene also low. Timing and sample-hold capacitors need high IR, relatively low ESR, low DA and stable capacitance; never use electrolytics for sample-hold (leakage) | low DA, high IR for S/H | DA, IR | sample-hold, integrators, timing | review | §3.6.7 p.331-332; §3.6.10 p.347-348 | high |
| SCHERZ-1171 | components | Ceramic dielectric temperature behaviour: NPO/C0G is 0 +/- 30 ppm/degC; dC = C*TC*dT/1e6 (1000 pF, +10 degC -> +/-0.3 pF) - use for filters, tuning, timing, oscillators and high-Q work. Class-2 EIA code: first letter = low-temperature limit (X -55, Y -30, Z +10 degC), digit = high limit (5 +85, 7 +125 degC), last letter = maximum change (V +22/-82 %, U +22/-56 %, T +22/-33 %, S +/-22 %, R +/-15 %, P +/-10 %, F +/-7.5 %, E +/-4.7 %); X7R 1000 pF can be 850-1150 pF, and class-2 parts also vary with ac/dc operating voltage and frequency. HiK types (e.g. Z5U-class) only for coupling/bypass - use the lowest-K material available | C_worst = C*(1 +/- tol)*(1 +/- dC_temp) | dielectric code, dT | ceramic capacitor selection | calc | §3.6.8 p.335-337, Table 3.7 | high |
| SCHERZ-1172 | components | Aluminium electrolytics (0.1 uF-1 F, 4-450 V, tolerance +100/-10 %): leak, drift and are inductive - low-frequency use only (ripple filters, audio coupling, LF bypass); they explode if the working voltage is exceeded or polarity is reversed; no ac across them (except nonpolar types); peak of ac + dc <= rating; not for HF coupling; do not use where the dc potential is well below the working voltage | V_dc + V_ac_pk <= WV; no reverse bias | V, polarity | bulk filtering | inspect | §3.6.8 p.334, Table 3.7 | high |
| SCHERZ-1173 | components | Tantalum electrolytics (6.3-50 V, 0.01-1000 uF, +/-20 %): polarized; smaller, more stable, lower leakage and inductance than aluminium, but lower maximum voltage and capacitance and easily damaged by current spikes - use mainly in analog/signal circuits free of high current spikes; act inductive above a few MHz; not for storage or HF coupling; not where dc is well below working voltage | avoid high surge currents | surge current, V | decoupling/filtering at low-moderate frequency | review | §3.6.8 p.334-335, Table 3.7 | high |
| SCHERZ-1174 | components | Film capacitors: polyester (Mylar) 50-600 V, 0.001-10 uF, +/-10 %, DA 0.5 %, high IR - coupling/storage, audio, moderate HF; polypropylene 100-600 V, 0.001-0.47 uF, +/-5 %, DA 0.05 %, most stable below 100 kHz - snubbing, timing, noise suppression; polystyrene 30-600 V, 100 pF-0.027 uF, DA 0.05 %, -55 to +70 degC, coiled (inductive) so only up to several hundred kHz, and permanently changes value if ever exposed much above 70 degC; metallized film self-heals (clearing) but has higher DF, lower IR, lower maximum current and ac-voltage-frequency capability - use film/foil types for large-signal ac | type per application | V, C, f, T | coupling, timing, snubbers | review | §3.6.8 p.335-340, Table 3.7 | high |
| SCHERZ-1175 | components | Specialty capacitors: silver mica (50-500 V, 1 pF-0.09 uF, +/-1 %/+/-5 %) very stable - resonant circuits, HF filters, HV; multilayer glass (50-2000 V, 0.5 pF-0.01 uF, -75 to +200 degC) for military/high-reliability RF; vacuum (3-60 kV, 1-5000 pF) for RF transmitters; oil-filled (1-300 kV, 100 pF-5000 uF) for high-voltage, high-current, hot duty; trimmer colour code yellow 1-5 pF, beige 2-10 pF, brown 6-20 pF, red 10-40 pF, purple 10-60 pF, black 12-100 pF | range per type | V, C, f | RF/HV capacitor selection | review | §3.6.8 p.333-341, Table 3.7 | high |
| SCHERZ-1176 | components | Supercapacitors (0.022-50 F; 2.3, 5.5, 11 V ratings; typical 3.5 and 5.5 V for 3.3 V/5 V backup): high ESR - not recommended for ripple absorption in dc power supplies; ~1/10 the energy of a low-density battery but ~10x the power; can hold low-dissipation CMOS memory for several months; state of charge is simply its voltage; can be stored fully discharged and charged quickly | not for ripple filtering | ESR, V rating | backup, pulse buffering | review | §3.6.8 p.339-341, Table 3.7 | high |
| SCHERZ-1177 | decoupling | Bypass rule of thumb: the bypass capacitor's impedance should be 10 percent of the input impedance of the circuit element it bypasses (at the frequency to be removed) | X_C(f) <= 0.1*Z_in | f, C, Z_in | bypassing noise/ripple around a stage | calc | §3.6.9 p.344, Fig.3.68 | high |
| SCHERZ-1178 | decoupling | Logic switching transients: TTL/CMOS output stages momentarily conduct both transistors, drawing transient supply currents as high as 100 mA; propagating through a real (R, L, C) distribution system they create 10-100 mV spikes, and a whole bus switching at once adds up to ~500 mV - treat supply and distribution as non-ideal | spike 10-100 mV per device, ~500 mV bus | I_transient, distribution Z | digital logic supplies | measure | §3.6.9 p.345 | high |
| SCHERZ-1179 | decoupling | Decoupling counts: one 0.1 uF ceramic per digital IC; two 0.1 uF ceramics per analog IC (one on each supply when +/- rails are used); one 1 uF tantalum per eight ICs or per IC row; bypass capacitors on power connectors; on power leads to another board or long wire, a 0.01 uF or 0.001 uF capacitor at both ends | N_0.1uF >= 1 per digital IC, 2 per analog IC; >= 1 x 1 uF per 8 ICs | IC list | board-level decoupling | inspect | §3.6.9 p.345 | high |
| SCHERZ-1180 | decoupling | Decoupling placement: as close as possible to the IC, between its power pin and ground pin, on wide PC tracks, routed device -> capacitor -> power planes; capacitor lead length < 1.5 mm (a little wire has enough inductance to resonate with the capacitor); surface-mount parts eliminate lead inductance | lead length < 1.5 mm | layout | every decoupling capacitor | inspect | §3.6.9 p.346 | high |
| SCHERZ-1181 | decoupling | Decoupling value vs frequency: the higher the ripple frequency the smaller the capacitor; 0.01-0.1 uF parts (self-resonant ~10-100 MHz) handle HF transients; for very high frequencies parallel a large and a small value (e.g. 0.01 uF + 100 pF); for complex ripple stack values, e.g. 1 uF (bus-transient dips), 0.1 uF (mid) and 0.001 uF (HF). Local decoupling spans 100 pF-1 uF; a 1 uF part may be shared by several ICs if each has less than 10 cm of reasonably wide track to it | share bulk C only within 10 cm | f_noise, SRF, distance | decoupling networks | calc | §3.6.9 p.346, Fig.3.69 | high |
| SCHERZ-1182 | decoupling | Decoupling capacitor type: aluminium electrolytics are not good for HF decoupling; a 1 uF tantalum suits lower-frequency decoupling; monolithic ceramic (especially SMD) is excellent for HF (low ESL, good frequency response); polyester/polypropylene are acceptable with short leads. (The text says "avoid capacitors with low ESR, high inductance, and high dissipation factor" - "low ESR" reads as a misprint for high ESR) | ceramic for HF, tantalum for LF bulk | type, f | decoupling | review | §3.6.9 p.346-347 | medium |
| SCHERZ-1183 | power | Capacitor-input rectifier filter: ripple factor = V_ripple,rms/V_dc; a practical target is ~0.05, typically needing 1000 uF or more (parallel capacitors to get more). Worked: full-wave bridge, 1000 uF, 100 ohm load -> 0.34 VAC (1.17 Vpp) ripple, ripple factor 0.00251; a half-wave rectifier doubles the ripple (Problem 7: 12.92 Vdc, 2.35 Vpp, 0.68 Vrms, ripple factor 0.0526). Select filter capacitors on ESR, voltage and ripple-current rating (electrolytics; oil-filled for HV high current); usually follow with a regulator | ripple factor <= ~0.05 | C, R_load, f, rectifier type | unregulated dc supplies | calc | §3.6.11 p.348-349, Fig.3.73-3.74; §3.6.14 p.355 | high |
| SCHERZ-1184 | protection | Contact arc suppression: glow discharge develops at ~320 V across a ~0.0003 in gap; arc discharge occurs at ~0.5 MV/cm. Size the RC snubber across the contacts so the contact voltage stays below 300 V, the rate of rise below 1 V/us and the current below the contact material's minimum arcing current; the series R limits capacitor-discharge inrush on closing - with open-contact voltage I_load*R <= supply voltage, R_max = R_load. Typical parts: 0.1-1 uF polypropylene film/foil or metallized film rated 200-630 V, with a 22-1000 ohm, 1/4-2 W carbon resistor (kV oil-filled capacitors for HV). For ac relays the RC can go across the load/coil. RC networks are bipolar, barely affect relay timing, draw no current and damp EMI | V_contact < 300 V; dV/dt < 1 V/us; R <= R_load | I_load, V_supply, contact material | switched inductive loads | calc | §3.6.12 p.350-352, Fig.3.77 | high |
| SCHERZ-1185 | timing | RC relaxation oscillator with a Schmitt inverter (74HCT14 at 5 V): the capacitor charges until ~1.7 V (input reads HIGH, output goes LOW) and discharges to ~0.9 V (output returns HIGH); frequency is set by RC. Capacitors: polypropylene, polyester, polystyrene (below a few hundred kHz) or electrolytic at low frequency | swing 0.9-1.7 V | R, C | simple clock sources | calc | §3.6.10 p.347, Fig.3.71 | medium |
| SCHERZ-1186 | components | Inductor tolerance letters: F = +/-1 %, G = +/-2 %, H = +/-3 %, J = +/-5 %, K = +/-10 %, L = +/-15 % (some military L = +/-20 %), M = +/-20 % | per letter | marking | BOM inspection | inspect | §3.7.7 p.361 | high |
| SCHERZ-1187 | magnetics | Inductor current ratings: incremental current = dc bias giving a 5 % inductance drop (mostly ferrite; powdered iron saturates softly); I_DC(max) = continuous current for the maximum temperature rise at maximum rated ambient (use RMS for low-frequency currents); saturation current = dc bias for a specified drop, commonly 10 % or 20 % - design energy-storage inductors to the 10 % point for ferrite and the 20 % point for powdered iron. Air cores do not saturate | I_peak <= I_sat(10 % ferrite / 20 % powdered iron); I_rms <= I_DC | I_peak, I_rms, core | SMPS and filter inductors | calc | §3.7.7 p.361-362 | high |
| SCHERZ-1188 | magnetics | Inductor self-resonance: distributed winding capacitance resonates with L; at SRF the part is purely resistive, high impedance and Q = 0; above SRF it is capacitive. Q = X_L/R_E must be quoted at a test frequency (ideally 2*pi*f*L/R_DC). Also check inductance and resistance temperature coefficients (ppm), Curie temperature, B_sat and radiated field (EMI) | f_use << SRF | SRF, Q, f | RF and filter inductors | review | §3.7.7 p.362-363 | high |
| SCHERZ-1189 | magnetics | Inductor selection (Tables 3.8-3.9): RF/resonance - low L, low I_DC, very high SRF, very high Q, low R_DC; filters - high L, high I_DC, very low R_DC; SMPS/dc-dc - high I_DC, medium SRF, low Q, low R_DC. Use shielded, toroid or pot-core parts where magnetic coupling/EMI matters (toroids self-shield and reject induced noise); molded inductors typically > 50 kHz; wideband RF chokes give 20-500 ohm over 1.0-400 MHz (current limited by #22/#24 AWG wire); ferrite antenna rods: mu 800 for 100 kHz-1 MHz, 125 for 550 kHz-1.6 MHz, 40 for ~30 MHz, 20 for ~150 MHz | per table | application | inductor part selection | review | §3.7.8 p.363-367, Table 3.8-3.9 | medium |
| SCHERZ-1190 | emc | Common-mode chokes (ferrite core) attenuate noise present on both conductors of a pair (SMPS line filters, power lines, speaker leads, cable interference); a differential-mode filter (e.g. 75 ohm coax high-pass) is ineffective against common-mode signals | CM choke for CM noise | noise mode | cable/power entry filtering | review | §3.7.8 p.366-367; §3.7.10 p.369, Fig.3.91 | high |
| SCHERZ-1191 | emc | PCB EMI layout rules (Vishay Dale note): no slit apertures (e.g. a ground plane divided into two); wide power tracks; stripline signal tracks with ground and power planes; lay out HF/RF tracks first and keep them short; no track stubs (reflections, harmonics); guard ring and ground fill around sensitive components; connect to ground at a single point; separate power planes over a common ground; route adjacent layers orthogonally; no loop tracks; no floating copper (connect it to ground) | inspection checklist | layout | PCB design | inspect | §3.7.11 p.373-374, Fig.3.95a-e | high |
| SCHERZ-1192 | emc | Power/filtering EMI rules: avoid loops in supply lines; decouple supply lines at local boundaries; place the highest-speed circuits closest to the power supply and the slowest farthest; isolate individual systems on both power and signal lines; put bias and pull-up/down parts close to the driver/bias points; use common-mode chokes; put decoupling capacitors close to chip supply pins | inspection checklist | layout, floorplan | PCB power distribution | inspect | §3.7.11 p.373-374, Fig.3.95g-l | high |
| SCHERZ-1193 | magnetics | Ideal transformer relations: V_S = V_P*(N_S/N_P); I_P = I_S*(N_S/N_P); Z_P = Z_S*(N_P/N_S)^2; N_P/N_S = sqrt(Z_P/Z_S). Worked: 200:1200 turns on 120 VAC -> 720 VAC (reversed -> 20 VAC); 180:1260 turns delivering 0.10 A -> 0.7 A primary; 500:1000 turns with 2000 ohm load -> 500 ohm reflected; 1:3 step-up -> voltage 1:3, current 3:1, impedance 1:9; reflected impedance keeps the load's phase angle | see formulas | turns, V, I, Z | low-frequency iron-core transformers, k ~ 1 | calc | §3.8.1 p.375-382, Eq.3.1-3.5 | high |
| SCHERZ-1194 | magnetics | Transformer efficiency: P_S = n*P_P with n < 1 (real transformers ~65-99 %); worked: 100 W out at 75 % efficiency needs 133 W in. Efficiency peaks at the rated output; exceeding rated power melts wire or breaks insulation, and even a purely reactive load heats windings and core, so never exceed the VA rating | P_P = P_S/n; VA_load <= VA_rated | P_S, n, VA | power transformers | calc | §3.8.1 p.378-380, Eq.3.3 | high |
| SCHERZ-1195 | magnetics | Either winding can serve as primary only if it has enough turns (inductance) to support the applied voltage without excessive magnetizing current, and insulation rated for the voltage present. Under load, leakage reactance and winding resistance make the secondary voltage lower than the turns ratio predicts; stray inter-winding/turn capacitance matters at RF (resonance near light loads) | V_S(load) < V_P*N_S/N_P | winding ratings | reverse/unusual transformer use | review | §3.8.1 p.376, p.384-385, Fig.3.105 | high |
| SCHERZ-1196 | magnetics | Transformer precautions: (1) never apply a voltage greatly in excess of a winding's rating (120 VAC into a secondary to get 1200 VAC at the primary -> insulation failure, smoke); (2) never let significant dc flow through a winding not designed for it; (3) never operate outside the maker's frequency range - a 60 Hz transformer driven at 20 Hz draws too much magnetizing current and runs dangerously hot | V <= rating; I_dc ~ 0 unless rated; f within spec | V, I_dc, f | all transformers | review | §3.8.1 p.385 | high |
| SCHERZ-1197 | magnetics | Transformer construction by frequency: laminated silicon-steel EI cores for power and audio; core-type construction (windings on separate legs) to minimize primary-secondary capacitance or for a very-high-voltage winding; powdered iron above mains frequency up to several kHz; ferrite from a few tens of kHz to ~1 MHz. Toroidal transformers: ~95 % efficient, about half the size and weight of EI, less mechanical hum, lower off-load (standby) losses. Use Litz wire for kHz-range windings (skin effect) | core per frequency band | f, power | transformer selection | review | §3.8.2 p.385-387, Fig.3.106-3.107 | high |
| SCHERZ-1198 | emc | Transformer shielding: an electrostatic (Faraday) shield between windings removes inter-winding capacitance (isolation transformers often have two isolated Faraday shields to divert HF noise to ground; wider separation lowers coupling); a magnetic shield keeps outside fields from inducing currents and stops the transformer radiating | Faraday shield for noise isolation | noise coupling path | line/isolation transformers | review | §3.8.2 p.386; §3.8.4 p.390 | high |
| SCHERZ-1199 | compliance | Autotransformers and Variacs share one winding and provide NO isolation (the common section carries the difference of line and load currents). When working on ungrounded "hot chassis" equipment, put an isolation transformer BEFORE the Variac, never after it. Lowering the line to ~85 V with a Variac reduces fault current when troubleshooting equipment that blows fuses | isolation transformer upstream of Variac | bench setup | line-powered troubleshooting | inspect | §3.8.3 p.387-389, Fig.3.109 | high |
| SCHERZ-1200 | compliance | Use a 1:1 isolation transformer whenever you work on non-grounded equipment with no input isolation (e.g. switch-mode power supplies): its secondary is not referenced to earth, so touching one lead while grounded passes no current (home neutral and ground are bonded at the main panel, so touching hot while grounded is potentially fatal) | isolation when servicing non-isolated gear | equipment type | bench safety | inspect | §3.8.4 p.389-390, Fig.3.111 | high |
| SCHERZ-1201 | components | Audio transformers work best from 20 Hz to 20 kHz, have a maximum input level beyond which they distort, and cannot step a signal up by more than about 25 dB - above that use an active preamp. Pulse transformers need very low leakage inductance and distributed capacitance, high open-circuit inductance and (for power pulses) low coupling capacitance. Broadband ferrite toroid transformers give dc isolation and serve AM (530-1550 kHz), shortwave (to ~20 MHz) and up to ~200 MHz | audio gain <= ~25 dB | f, gain, pulse shape | signal transformers | review | §3.8.5 p.391-392 | high |
| SCHERZ-1202 | test | Current transformers are specified by current ratio (e.g. 400:5, 2000:5); supply-metering types drive 5 A full-scale meters; the measured cable passes once through the toroid as the primary | I_sec = I_pri*(ratio) | ratio | current measurement | calc | §3.8.6 p.393, Fig.3.117 | high |
| SCHERZ-1203 | power | Transformer secondary sizing for rectifier supplies: dual complementary (bifilar) and full-wave bridge: V_AC = 0.8*(V_DC + 2), I_AC = 1.8*I_DC; full-wave centre tap: V_AC = 1.7*(V_DC + 1), I_AC = 1.2*I_DC (one diode drop per half cycle; good for high-current low-voltage); avoid the half-wave rectifier with a transformer - inefficient and polarizes/saturates the core in one direction. Example: 120 V to 18V-0-18V centre-tap transformer feeds a +/-12 V regulated supply | V_AC, I_AC per formula | V_DC, I_DC, topology | linear dc supplies | calc | §3.8.6 p.394-395, Fig.3.120-3.121 | high |
| SCHERZ-1204 | power | A multi-tap transformer's total load must not exceed its rated output (a 100 W landscape transformer drives at most ten 10 W or five 20 W lamps; overload dims the lamps); use the higher tap (14 V for 12 V lamps) to make up for voltage drop on long cable runs | sum(P_load) <= P_rated | loads, cable drop | low-voltage ac distribution | calc | §3.8.6 p.394, Fig.3.119 | high |
| SCHERZ-1205 | matching | Audio impedance matching: maximum power transfers when the load equals the source's Thevenin impedance; a 500 ohm output into an 8 ohm speaker needs N_P/N_S = sqrt(500/8) = 7.906:1 (Example 6 gives 8). Modern hi-fi amplifiers instead have output impedance of 0.1 ohm or less (<< 8 ohm speaker) for efficient transfer and good voice-coil damping | N_P/N_S = sqrt(Z_P/Z_S) | Z_source, Z_load | audio output stages, transducer loading | calc | §3.8.1 p.381; §3.8.6 p.396, Fig.3.122 | high |
| SCHERZ-1206 | protection | Branch breakers (typically 15 A) protect the building wiring, not the equipment: a device fault that raises an internal current from 0.1 A to 10 A multiplies dissipation 10,000x (P = I^2*R) without tripping the breaker - every line-powered device needs its own properly rated fuse | per-device fuse required | device current | all mains-powered products | inspect | §3.9 p.397 | high |
| SCHERZ-1207 | protection | Fuse selection: rate the fuse about 50 % above the expected nominal current (allows for normal variation and the rating's decline with age). Fast-acting fuses open on a brief surge; time-lag (slow-blow) fuses take ~1 s and are used for large turn-on currents (motors, inductive loads) | I_fuse ~= 1.5*I_nominal | I_nominal, inrush | fuse sizing | calc | §3.9 p.397 | high |
| SCHERZ-1208 | compliance | On 120 V ac line power the fuse/breaker goes in the hot (black) line, ahead of the protected device; a fuse in the neutral (white) leaves full line voltage inside after it blows. Breakers for 240 V appliances interrupt all the supply conductors (printed: "fuses on all three input wires") | fuse in hot, upstream | wiring | mains inputs | inspect | §3.9 p.397, Fig.3.124 | high |
| SCHERZ-1209 | protection | Fuse families: glass/ceramic cartridges 1/4 x 1-1/4 in or 5 x 20 mm, ~1/4-20 A, 32/125/250 V, fast or time-lag; automotive blade fuses (fast) 3-30 A at 32 and 36 V, colour-coded violet 3 A, pink 4 A, tan 5 A, red 10 A, blue 15 A, yellow 20 A, white 25 A, green 30 A; subminiature PCB fuses 0.05-10 A; cartridge fuses - ferrule contact up to 60 A, knife-blade 60 A and above; circuit breakers - main-line 15-20 A, small ones down to 1 A, thermal auto- or manual-reset | V_fuse_rating >= circuit V; family per current | I, V, mounting | fuse/breaker selection | inspect | §3.9.1 p.398-399, Fig.3.125 | high |
| SCHERZ-1210 | components | Diode forward threshold rules of thumb: silicon p-n ~0.6 V (actual 0.6-1.7 V), germanium ~0.2 V (0.2-0.4 V), Schottky ~0.4 V average (0.15-0.9 V). Germanium diodes become unreliable above 85 degC ("worthless") and leak more when hot | V_F per technology; Ge T_j <= 85 degC | diode type, T | diode selection, headroom budgets | calc | §4.2.1-4.2.2 p.408-409; Table 4.3 p.428 | high |
| SCHERZ-1211 | derating | Never exceed a diode's peak forward current I_O(max) (junction meltdown) or its peak inverse voltage (PIV). In rectifiers PIV and current rating are the primary specs: the peak reverse voltage must be smaller than PIV and the peak current smaller than I_O(max); keep operating current around 75 % of the maximum for safety (1N4002 rated 1 A on 11.4 V -> 15 ohm minimum load rather than 11.4 ohm) | V_R,pk < PIV; I_F <= 0.75*I_O(max) | V_R,pk, I_F, ratings | all rectifier/steering diodes | calc | §4.2.2 p.409; §4.2.4 p.411; §4.2.11 Problem 1 p.427 | high |
| SCHERZ-1212 | components | Diode selection specs: PIV, I_O(max), response time t_R, reverse leakage I_R(max), max forward drop V_F(max). Fast/low-voltage work is governed by t_R and V_F; signal/switching ("fast recovery") diodes trade junction strength for low capacitance; Schottky diodes switch in ~10 ns with very low capacitance and low V_F - RF detection, low-voltage rectification, clamps and cooler power rectifiers | per application | t_R, V_F, C_j | diode selection | review | §4.2.3-4.2.4 p.409-411, Table 4.1 | high |
| SCHERZ-1213 | power | Series-diode voltage reference: n silicon diodes give ~n*0.6 V (three -> 1.8 V), stiffer than a resistor drop; series resistor R_S = (V_in - V_out)/I, with resistor and diode power ratings checked (P = I*V). Use a zener regulator or regulator IC for critical/higher-power rails | R_S = (V_in - V_out)/I | V_in, n, I | crude low-voltage references, level droppers | calc | §4.2.5 p.412, Fig.4.15-4.16 | medium |
| SCHERZ-1214 | protection | Reverse-polarity protection: a mechanical block (keyed holder/connector) is best. A series diode must carry the full load current and costs ~0.6 V (less with a Schottky), shortening battery run time; a shunt diode (for high-output-impedance batteries such as alkaline, or with a fuse) avoids the drop but draws high current from a reversed battery, so rate it for that current; special ICs/transistor circuits give near-zero-drop protection | series: I_F >= I_load; shunt: I_F >= I_reverse_fault | battery type, I_load | battery/dc-jack inputs | review | §4.2.5 p.412-413, Fig.4.17 | high |
| SCHERZ-1215 | protection | Fly-back diodes: switching off an inductive load (relay coil, motor) produces spikes of hundreds or thousands of volts. Place a rectifier (1N4001, 1N4002) or Schottky (1N5818, clamps ~0.4 V) across the coil; it does nothing at turn-on. Add a second diode across the driver transistor when needed; on voltage regulators add protection diodes output-to-input and ground-to-output so load spikes cannot drive the output | diode across every switched inductance | load inductance, driver | relays, motors, regulators | inspect | §4.2.5 p.413-414, Fig.4.18 | high |
| SCHERZ-1216 | power | Half-wave rectifier: diode PIV must exceed the peak ac voltage (1.4 x V_rms); with a capacitor filter and little or no load it rises to 2.8 x V_rms | PIV > 2.8*V_rms (cap filter) | V_rms, filter | half-wave supplies | calc | §4.2.5 p.415, Fig.4.20 | high |
| SCHERZ-1217 | power | Full-wave centre-tap rectifier (V_rms = half-secondary voltage): average output 0.9 x V_rms (resistive/choke-input), peak 1.4 x V_rms with a capacitor-input filter; each diode sees PIV = 2.8 x V_rms regardless of load and carries half the load current; ripple at twice line frequency needs less filtering | PIV_diode > 2.8*V_rms; I_diode = I_load/2 | V_rms (half winding), I_load | centre-tap supplies | calc | §4.2.5 p.415, Fig.4.20 | high |
| SCHERZ-1218 | power | Full-wave bridge: at least 1.2 V lost (two diode drops per half cycle); average output 0.9 x V_rms (resistive/choke-input), up to 1.4 x V_rms with a capacitor filter and light load; each diode PIV > 1.4 x V_rms; transformer utilization factor 1 (centre tap 0.5). The centre tap is preferred for high-current low-voltage supplies (one diode drop); half-wave is rarely used at 60 Hz except bias supplies but is common in forward and flyback SMPS | PIV_diode > 1.4*V_rms; V_out,pk = 1.4*V_rms - 1.2 V | V_rms, I_load | bridge supplies | calc | §4.2.5 p.416-417 | high |
| SCHERZ-1219 | power | Voltage multipliers: half-wave doubler charges C1 to 1.4 x V_rms and C2 to 2.8 x V_rms (no load); full-wave doubler outputs 2.8 x V_rms no-load with effective filter C = C1 in series with C2, and needs series resistors R1, R2 sized from transformer voltage and diode surge rating because the capacitors look like a short at switch-on; diode PIV 2.8 x V_rms. Triplers/quadruplers use 20-50 uF capacitors rated above V_in(peak), 2x, 3x, 4x V_in(peak) for C1..C4 (the printed RMS equivalents 0.7/1.4/2.1/2.8 V_rms are half the peak multiples - use the peak values); outputs approach exact multiples only at low current and high capacitance | V_Cn_rating > n*V_in,pk | V_in, I_load | HV low-current supplies | calc | §4.2.5 p.416-417, Fig.4.21-4.22 | medium |
| SCHERZ-1220 | power | Diode-OR battery backup costs one diode drop on the battery path (0.6 V silicon, 0.4 V Schottky), limiting the usable battery voltage; better designs use a comparator-controlled low-resistance transistor switchover (dedicated ICs) | V_batt,min_usable = V_load,min + V_F | V_F, V_load,min | wall-adapter + battery products | calc | §4.2.5 p.418, Fig.4.24 | high |
| SCHERZ-1221 | termination | Schottky-diode termination: clamp diodes from the line end to V_CC and to ground limit overshoot and undershoot from reflections without having to match the line impedance - useful where the characteristic impedance is unknown or variable; it maintains signal integrity and saves power versus resistive termination | diodes to V_CC and GND at receiver | line Z unknown/variable | digital clock/data lines | inspect | §4.2.5 p.419, Fig.4.26 | high |
| SCHERZ-1222 | components | Zener diodes: breakdown V_Z from 1.8 to 200 V (e.g. 1N5225B = 3.0 V, 1N4733A = 5.1 V, 1N4739A = 9.1 V), power ratings ~0.25-50 W, ~0.6 V forward. Families (Table 4.2): 500 mW axial 1N52xxB, 1 W 1N47xxA, 5 W 1N53xxB; SMD 200 mW BZX84Cxx/MMBZ52xxB, 500 mW BZT52Cxx/ZMM52xxB, 1 W SMAZxx/ZM47xxA | V_Z, P_Z per family | V_Z, P | zener selection | inspect | §4.2.6 p.420-422, Table 4.2 | high |
| SCHERZ-1223 | power | Zener shunt regulator: R_S = (V_in,min - V_Z)/(I_Z,min + I_L,max); P_R = (V_in,max - V_Z)^2/R_S; P_Z,max = V_Z*(V_in,max - V_Z)/R_S (all current in the zener when the load is removed). Worked: 8.2 V at 10-50 mA from 12 V +/-10 % with I_Z,min = 10 mA -> R_S = 43 ohm, P_R = 0.58 W, P_Z = 0.95 W. Zener regulators are temperature dependent; use a linear regulator IC for critical rails | see formulas | V_in range, V_Z, I_Z,min, I_L range | simple shunt regulators | calc | §4.2.6 p.421, Fig.4.29; §4.2.11 Problem 3 p.427 | high |
| SCHERZ-1224 | protection | Zener crowbar overvoltage protection: zener across the input after a fuse, V_Z slightly above the maximum voltage the load can tolerate; on overvoltage (wrong wall adapter) it conducts until the fuse blows. Choose fast or slow fuse by load sensitivity and rate fuse V/I for the application; TVSs and varistors are the cheaper modern alternative | V_Z just above V_load,max; fuse upstream | V_load,max, fuse | dc input jacks | inspect | §4.2.7 p.424, Fig.4.35 | high |
| SCHERZ-1225 | protection | Opposing zeners (or one bidirectional TVS) across a dc supply output clip transients: breakdown voltage must be greater than the supply voltage but smaller than the maximum allowable transient voltage | V_supply < V_BR < V_transient,max | V_supply, V_max | supply outputs | calc | §4.2.7 p.423, Fig.4.32 | high |
| SCHERZ-1226 | rf | Varactor diodes: capacitance from a few pF to over 100 pF, falling as reverse bias rises; maximum reverse voltage from a few volts to ~100 V. The tuning bias must be free of noise (filter capacitors, RC filter) or the oscillator frequency shifts/becomes unstable; dual common-anode types act as two series capacitors | clean bias (filtered) | C range, V_R | VCO/FM tuning | review | §4.2.8 p.424-425, Fig.4.38-4.39 | high |
| SCHERZ-1227 | rf | PIN diodes as RF switches: with high dc forward bias the RF resistance is often less than 1 ohm; with small bias it is kilohms; used as transmit/receive switches from 100 MHz upward; feed bias through an RF choke with a capacitor to ground for clean dc | R_on < 1 ohm (high bias) | bias current, f | RF switching | review | §4.2.9 p.426, Fig.4.40 | high |
| SCHERZ-1228 | components | FET vs BJT: MOSFET gate input impedance >= 1e14 ohm, JFET ~1e9-1e10 ohm (gate current in the pA range), but FET transconductance is much lower than a BJT's at the same current (up to ~100x), so FET amplifiers have lower gain and more nonlinearity - use FET stages only where very high input impedance/low input current is required | FET only for high-Z inputs | source impedance, gain need | amplifier input stages | review | §4.3.1 p.429; §4.3.3 p.450, p.457; §4.3.4 p.459 | high |
| SCHERZ-1229 | components | BJT operating rules: for npn the collector must be at least a few tenths of a volt above the emitter; V_BE = +0.6 V (npn) or -0.6 V (pnp) for conduction; in the active region I_C = h_FE*I_B, I_E = I_C + I_B = (h_FE + 1)*I_B ~= I_C; typical h_FE 10-500. Formulas outside the characteristic-curve bounds give impossible answers | I_C = h_FE*I_B (active only) | V_B, V_E, V_C | BJT bias analysis | calc | §4.3.2 p.432-434, Fig.4.46-4.48 | high |
| SCHERZ-1230 | components | h_FE is not a good design parameter: it can vary from ~50 to 500 within one transistor family and changes with collector current, V_CE and temperature - never build circuits that depend on a specific h_FE (bias from resistor ratios and emitter degeneration instead) | design at h_FE,min, insensitive to h_FE | h_FE spread | all BJT circuits | review | §4.3.2 p.444 | high |
| SCHERZ-1231 | components | BJT intrinsic emitter (trans)resistance r_tr ~= 0.026 V/I_E (26 ohm at 1 mA, 52 ohm at 0.5 mA, 520 ohm at 50 uA); it depends on temperature and emitter current and can dominate gain in un-degenerated stages | r_tr[ohm] = 0.026/I_E[A] | I_E | small-signal gain | calc | §4.3.2 p.434-435, p.440 | high |
| SCHERZ-1232 | components | BJT switch: base current I_B = (V_drive - 0.6 V)/R_B; I_C = h_FE*I_B holds only while the collector stays above V_E + ~0.6 V (load drop not too large); a large base pull-down (e.g. 10 kohm) keeps the transistor off. BJT current source: I_C = (V_B - 0.6 V)/R_E with V_B from a divider (20 V, 14 k/1.2 k -> 1.6 V, R_E 1 k -> 1 mA) or a zener (8.7 V, R_E 10 k -> 0.81 mA) | I_C = (V_B - 0.6)/R_E | V_B, R_E | switches and current sources | calc | §4.3.2 p.437-438, Fig.4.52-4.54 | high |
| SCHERZ-1233 | components | Emitter follower: R_in ~= h_FE*R_E, R_out ~= R_S/h_FE (in parallel with R_E), A_V ~= 1; the output follows the input 0.6 V lower and clips when V_B falls below 0.6 V unless biased | R_in = h_FE*R_E; R_out = R_S/h_FE | h_FE, R_E, R_S | buffers | calc | §4.3.2 p.438, Fig.4.55 | high |
| SCHERZ-1234 | components | Common-collector amplifier design: pick I_Q; V_E = V_CC/2 (maximum symmetric swing); R_E = (V_CC/2)/I_Q; V_B = V_E + 0.6 V (R1 ~= R2); R1 // R2 <= (1/10)*R_in(base),dc with R_in(base),dc = h_FE*R_E; R_in(base),ac = h_FE*(R_E // R_load); C1 = 1/(2*pi*f_3dB*R_in), C2 = 1/(2*pi*f_3dB*R_load). Worked: V_CC 10 V, 3 kohm load, h_FE 100, 100 Hz -> I_Q 1 mA, R_E 5 kohm, R1 = R2 = 100 kohm, R_in(base),ac 190 kohm, R_in 40 kohm, C1 0.04 uF, C2 0.5 uF | R1//R2 <= 0.1*h_FE*R_E | V_CC, I_Q, h_FE, R_load, f_3dB | ac-coupled followers | calc | §4.3.2 p.439-440, Fig.4.56 | high |
| SCHERZ-1235 | components | Common-emitter amplifier design: R_C = (V_CC/2)/I_Q (V_C centred); R_E = 1 V/I_Q (V_E ~ 1 V for temperature stability); V_B = V_E + 0.6 V; R1:R2 from the divider with R1 // R2 <= (1/10)*h_FE*R_E; gain = -R_C/(r_tr + R_E // R3) with R_E bypassed by C2. Worked: gain -100, f_3dB 100 Hz, I_Q 1 mA, h_FE 100, V_CC 20 V -> R_C 10 kohm, R_E 1 kohm, R2 10 kohm, R1 110 kohm (ratio 11.5), R3 74 ohm, R_in 5 kohm, C1 0.32 uF, C2 16 uF. Without R_E the gain -R_C/r_tr (-192 at 0.5 mA, 10 kohm) is temperature-unstable | gain = -R_C/(r_tr + R_E//R3) | V_CC, I_Q, gain, f_3dB | voltage-gain stages | calc | §4.3.2 p.440-442, Fig.4.57-4.58 | high |
| SCHERZ-1236 | components | Darlington pair: h_FE = h_FE1*h_FE2, V_BE ~= 1.2 V (two drops), slower switching; used for high current and high-input-impedance stages | V_BE = 1.2 V | h_FE1, h_FE2 | high-gain switches | calc | §4.3.2 p.443, Fig.4.60 | high |
| SCHERZ-1237 | components | BJT family limits: small-signal - h_FE 10-500, I_C(max) ~80-600 mA, 1-300 MHz; small switching - h_FE 10-200, I_C 10-1000 mA, switching 10-2000 MHz; RF - up to ~2000 MHz, I_C 10-600 mA; power - 10-300 W, 1-100 MHz, I_C 1-100 A with the collector tied to the metal tab (heat sink) | per family | I_C, f, P | transistor selection | review | §4.3.2 p.443, Fig.4.61 | high |
| SCHERZ-1238 | protection | Every BJT has maximum I_C, BV_CBO, BV_CEO, V_EBO and P_D ratings; exceeding them destroys it. Guard V_EB with a diode from emitter to base (reverse polarity), BV_CBO with a diode in series with the collector, and BV_CEO with an inductive load by a diode across the load | ratings not exceeded | I_C, V_CE, V_CB, V_EB, P | BJT circuits with negative swings or inductive loads | review | §4.3.2 p.444-445, Fig.4.62 | high |
| SCHERZ-1239 | test | Bulk/unmarked small transistors may mix pinouts and even npn/pnp polarities - identify with a cross-reference catalog or a DMM transistor tester (reports polarity, pinout ebc/cbe and h_FE) before use | verify pinout/polarity | part source | prototyping, incoming inspection | measure | §4.3.2 p.445 | high |
| SCHERZ-1240 | components | Differential pair: gain = R_C/r_tr (worked: I_Q 50 uA per side, R_C 100 kohm, R_E 100 kohm to -10 V -> r_tr 520 ohm, gain 192); it rejects noise common to both inputs regardless of frequency (quality = CMRR). A push-pull complementary follower has crossover distortion near I_C = 0. Current mirrors need matched transistors (add a helper transistor for multiple outputs so a saturated output does not steal base current) | gain = R_C/r_tr | I_Q, R_C | differential receivers, output stages | calc | §4.3.2 p.446-447, Fig.4.64-4.67 | high |
| SCHERZ-1241 | components | JFET relations: active region I_D = I_DSS*(1 - V_GS/V_GS,off)^2; g_m0 = 2*I_DSS/abs(V_GS,off); g_m = g_m0*(1 - V_GS/V_GS,off) = g_m0*sqrt(I_D/I_DSS); R_DS = 1/g_m. Typical: I_DSS 1 mA-1 A, V_GS,off -0.5 to -10 V (n-ch; +0.5 to +10 V p-ch), R_DS,on 10-1000 ohm, BV_DS 6-50 V, g_m at 1 mA 500-3000 umho. Worked: I_DSS 12 mA, V_GS,off -4 V, V_GS -2 V -> 3.0 mA, g_m 3000 umho, R_DS 333 ohm; self-bias with R_S 1 kohm and I_DSS 8 mA -> V_GS -2 V, I_D 2 mA | I_D = I_DSS*(1 - V_GS/V_GS,off)^2 | I_DSS, V_GS,off (datasheet) | JFET bias/analysis | calc | §4.3.3 p.451-454, Fig.4.73-4.76 | high |
| SCHERZ-1242 | components | JFET circuits: a gate-to-source-shorted JFET current source delivers I_DSS, which is unpredictable part to part - add a source resistor to set/adjust it (still less stable than BJT or op-amp sources); a source follower has gain R_S*g_m/(1 + R_S*g_m), output impedance 1/g_m and an unpredictable dc offset (poorly controlled V_GS) - improve with a matched dual-JFET current-source load. As a voltage-controlled resistor keep V_DS small compared with abs(V_GS,off) and abs(V_GS) < abs(V_GS,off); AGC gain = 1 + R_F/R_DS(on): R_F 29 kohm with R_DS(on) 1 kohm -> 30:1 range | gain_SF = R_S*g_m/(1+R_S*g_m) | I_DSS spread, V_DS | JFET sources, followers, VCRs | calc | §4.3.3 p.455-457, Fig.4.78-4.82 | high |
| SCHERZ-1243 | esd | MOSFET gate oxide is extremely fragile: gate-channel capacitance is only a few pF, so a person charged to a few thousand volts (walking across carpet) can blow a hole through the insulator. Eliminate static at the work area (Ch.7 ESD guidelines); not all MOSFETs have built-in gate protection | ESD-safe handling for MOS parts | device type | assembly, rework, bench | inspect | §4.3.4 p.459-460, p.465 | high |
| SCHERZ-1244 | components | Enhancement MOSFET relations: active I_D = k*(V_GS - V_GS,th)^2 with k = I_D,on/(V_GS,on - V_GS,th)^2; g_m = 2k*(V_GS - V_GS,th) = 2*sqrt(k*I_D); R_DS = 1/g_m; R_DS2 = R_DS1*(V_G1 - V_GS,th)/(V_G2 - V_GS,th). Typical: I_D,on 1 mA-1 A, R_DS(on) 1 ohm-10 kohm, V_GS,th 0.5-10 V, BV_DS and BV_GS 6-50 V. Worked: V_GS,th 2 V with 12 mA at 4 V -> k 3000 umho/V, g_m 12,000 umho, R_DS 83 ohm; common source (k 1000 umho/V, V_GS 5 V) -> 9 mA, R_D 1100 ohm centres V_D at 10 V from 20 V, gain = g_m*R_D = 6.6; depletion common source gain = g_m0*R_D (5000 umho x 1 kohm = 5) | I_D = k*(V_GS - V_GS,th)^2 | k, V_GS,th | MOSFET bias/analysis | calc | §4.3.4 p.462-465, Fig.4.91-4.95 | high |
| SCHERZ-1245 | components | MOSFET practice: hold a separate body terminal at a non-conducting voltage (to the source, or more negative than the source for n-channel / more positive for p-channel) - body bias shifts V_GS,th; a 1 Mohm gate-to-ground self-bias resistor compensates leakage (its drop is negligible with nA-pA gate leakage); select on breakdown voltages, I_D,max, R_DS(on),max, power dissipation, switching speed and ESD protection. An op-amp servoing a MOSFET gate makes a current source I_load = V_in/R_S with < 1 % error | selection checklist | ratings | MOSFET switches/sources | review | §4.3.4 p.464-466, Fig.4.96, Fig.4.99 | high |
| SCHERZ-1246 | timing | UJT: triggers at V_trig = eta*V_B2 with intrinsic standoff ratio eta = R_B1/(R_B1 + R_B2) (0-1, typically ~0.5; interbase resistance a few kohm); relaxation oscillator f = 1/(R_E*C_E*ln[1/(1 - eta)]) - R_E 100 kohm, C_E 0.1 uF, eta 0.61 -> ~106 Hz; typical ratings I_E 50 mA, V_BB 35-55 V, P_D 300-500 mW. A PUT fires at V_A = V_G + 0.7 V with V_G = V+*R2/(R1 + R2) and conducts with ~1 V anode-cathode | f = 1/(R*C*ln(1/(1-eta))) | eta, R_E, C_E | timers, relaxation oscillators | calc | §4.3.6 p.468-472, Fig.4.107-4.113 | high |
| SCHERZ-1247 | components | SCR: latches on after a gate trigger and stays on until the anode current is removed (below holding current I_H) or reversed. Key specs V_T, I_GT, V_GT, I_H, P_GM, V_DRM, I_DRM, V_RRM, I_RRM (2N6401: V_DRM 100 V, I_DRM/I_RRM 2.0 mA, V_T 1.7 V, I_GT 5.0/30 mA, V_GT 0.7/1.5 V, I_H 6.0/40 mA, P_GM 5 W). Classes: low-current <= 1 A/100 V, medium <= 10 A/100 V, high-current up to several thousand amps and volts (built-in heat sinks) | gate drive >= I_GT,max, V_GT,max; V_peak < V_DRM | load I, V | SCR switching/phase control | calc | §4.4.2 p.473-476, Table 4.7 | high |
| SCHERZ-1248 | components | Silicon-controlled switch (SCS): turn-off 1-10 us versus 5-30 us for an SCR, maximum anode current 100-300 mA, dissipation 100-500 mW; switched on and off by pulses on its anode or cathode gate | I_A <= 100-300 mA | I, timing | low-power latching switches | review | §4.4.3 p.476-477 | high |
| SCHERZ-1249 | components | Triac: bidirectional; turns off at the next zero crossing after gate drive is removed. Low-current triacs <= 1 A/several hundred volts, medium-current up to 40 A/a few thousand volts (less than high-current SCRs). Specs I_T,RMS, I_GT, V_GT, I_H, P_GM, I_surge (NTE5600: 4.0 A, 30 mA, 2.5 V, V_F 2.0 V, I_H 30 mA, surge 30 A). Trigger through a diac for reliable firing over temperature; add an RC snubber for motor loads (100 ohm 1/2 W + 0.22 uF 200 V in the controller example) | I_T,RMS rating >= load I_rms | load, triggering | ac power control | calc | §4.4.4 p.477-480, Fig.4.124-4.127, Table 4.8 | high |
| SCHERZ-1250 | components | Diacs/four-layer diodes switch when the voltage reaches breakover (no gate): NTE6411 diac V_BO 40 V, I_BO max 100 uA, I_pulse 2 A, V_switch 6 V, P_D 250 mW. Dimmer example: 1 kohm + 500 kohm pot charging 0.1 uF 50 V; full-wave phase control shown for loads < 1500 W; characterize a diac by adjusting the 100 kohm test pot until it fires once per half cycle | V_BO from datasheet | V_BO | triac triggering, phase control | measure | §4.4.4-4.4.5 p.479-482, Fig.4.126-4.130, Table 4.9 | medium |
| SCHERZ-1251 | protection | Transient environment: switching off inductive loads can produce spikes exceeding 1000 V lasting 50 ns to over 100 ms; ESD can reach 40,000 V (humidity dependent); nearby lightning induces 300 V or more on long signal lines; line transients range from microseconds to milliseconds and up to 10,000 V; logic switching dips supply rails. Protect power inputs, I/O and data lines, not just supply outputs | design for these levels | environment | all products with external wiring | review | §4.5.1 p.482-483; Fig.4.132 p.486 | high |
| SCHERZ-1252 | protection | Transient-suppressor selection (Table 4.10): bypass capacitors (logic 0.01-0.22 uF, power 0.1 uF and up) for low-power rail cleaning; zeners - low energy, tend to fail open; TVS diodes - fast, calibrated low clamp, fail short, higher capacitance; MOVs - more energy, fail short, moderate/high capacitance; multilayer varistors - 3-70 V systems, fast, SMD; Surgectors - thyristor crowbar with follow-on current; avalanche diodes - sub-ns, ~50 pF, low surge; gas discharge/spark gaps - up to ~20,000 A, pA leakage, slow; PolySwitches - resettable overcurrent | device per energy/speed/capacitance | transient energy, line speed | protection design | review | §4.5.2 p.483-484, Table 4.10 | high |
| SCHERZ-1253 | protection | TVS diode selection: V_RWM (stand-off) equal to or slightly above the normal operating voltage (for ac use the peak: 1.4 x V_rms <= V_RWM); V_BR is ~10 % above V_RWM (measured at I_T = 1 or 10 mA); clamping voltage V_C is typically 35-40 % above V_BR (~60 % above V_RWM) and must stay below what the protected circuit can survive; I_PP >= maximum expected transient current; watch junction capacitance on high-speed lines. Discrete ranges: V_RWM 2.8-440 V, V_BR 5.3-484 V (e.g. V_BR/V_RWM 12.4/11.1, 15.2/13.6, 190/171 V). Put a fuse in the line in most power applications | V_RWM >= V_op,pk; V_C < V_damage; I_PP >= I_transient | V_op, V_damage, I_transient, C_J | power, I/O, data line protection | calc | §4.5.2 p.484-486, Fig.4.131-4.132 | high |
| SCHERZ-1254 | protection | MOV use: connect across the mains input with a series fuse and/or filter inductor; energy rating in joules trades power for time (60 J = 60 W for 1 s = 600 W for 0.1 s = 6 kW for 10 ms = 60 kW for 1 ms) but MOVs cannot handle continuous average dissipation; they fail short (fuse them and place them so a fractured part cannot damage others) and wear out (leakage and breakdown drift with each absorbed surge). Ratings: V_M(DC) = 1.4 x V_M(AC); W_TM for a single 10/1000 us impulse; V_NOM at 1 mA; C_p <= 100 pF (small) to thousands of pF at 1 MHz. Design: steady-state voltage rating, transient energy, peak current, dissipation, then clamping | V_M(AC) >= V_line,rms,max; W_TM >= transient energy | line V, surge energy | mains input protection | calc | §4.5.2 p.487-489, Fig.4.133-4.134 | high |
| SCHERZ-1255 | protection | TVS diode vs varistor: TVS diodes have better clamp ratios, 1-5 ns response and no wear-out mechanism; MOVs absorb more energy per footprint but respond in 5-200 ns (package/lead inductance - keep leads short) with 75-20,000 pF capacitance. Multilayer varistors (SMD, 3.5-68 V operating) respond in < 1 ns and survive many thousands of strikes at full rated peak current; with an effective dielectric constant ~800 they also act as filter capacitors | TVS for fast/precise clamp; MOV for energy | speed, energy, capacitance | protection device choice | review | §4.5.2 p.488 | high |
| SCHERZ-1256 | protection | PolySwitch (resettable polymer PTC fuse): choose a trip current slightly above the rated current of the protected device (e.g. a speaker: I = sqrt(P/R), 8 ohm 5 W -> ~0.79 A, derived); once tripped it stays high-resistance while voltage remains (holding current) and resets only after power is removed and it cools. Avalanche diodes: breakdown available above 4000 V, rated by clamp V_BR and energy (J or I^2*t), non-destructive if not overheated, generate RF noise | I_trip slightly > I_rated | I_rated | speakers, motors, battery packs, supplies | calc | §4.5.2 p.490-491, Fig.4.136 | medium |
| SCHERZ-1257 | assembly | IC package pitches (Table 4.11): DIL 2.54 mm (8, 14, 16, 20, 24, 40 pins), SO/SOIC/SOP 1.27 mm, MSOP/SSOP 0.65 mm, SOT 0.65 mm, TQFP 0.8 mm (pins on four sides), TQFN 0.4-0.65 mm (no leads; pads under body). Pitches down to 0.5 mm are not really intended for hand soldering - prototype in DIL or SO, then move to the smaller package | pitch >= 0.65 mm for hand assembly | package | prototype vs production assembly | inspect | §4.6.1 p.492-493, Table 4.11 | high |
| SCHERZ-1258 | components | LED current-limit resistor: R_S = (V_IN - V_LED)/I_LED; LED light output is directly proportional to forward current (drive LEDs by current). If the recommended I_LED is unknown assume ~20 mA. Typical V_LED: 1.7 V standard red, 1.9 V high-brightness low-current red, 2 V orange and yellow, 2.1 V green, 3.4-3.6 V bright white and most blue, 6 V for 430 nm blue; use at least 3 V supply for the low-voltage LEDs, 4.5 V for 3.4 V types, 6 V for 430 nm blue. A 1 kohm pot in series gives brightness control | R_S = (V_IN - V_LED)/I_LED | V_IN, V_LED, I_LED | indicator/illumination LEDs | calc | §5.3.3 p.503-505, Fig.5.10a | high |
| SCHERZ-1259 | components | LED ratings: typical power dissipation 100 mW, operating temperature -40 to +85 degC, pulse current 100 mA, spectral width 20-40 nm (< 40 nm at 90 % peak); visible indicator LEDs ~1.8 V max forward voltage at 10-30 mA; IR LEDs 880-940 nm with 0.50 mW/20 mA to 8.0 mW/50 mA output and V_F from 1.60 V at 20 mA to 2.0 V at 100 mA, narrower viewing angle; LEDs switch on at 0.6-2.2 V | I_F <= rating; P <= ~100 mW | I_F, V_F | LED selection | review | §5.3.2-5.3.3 p.499-504, Table 5.1 | high |
| SCHERZ-1260 | thermal | High-power LEDs (forward currents of hundreds of mA to more than 1 A) generate a lot of heat and must be mounted on a heat sink to prevent thermal destruction | heat sink mandatory | I_F, P | illumination LEDs | inspect | §5.3.3 p.503 | high |
| SCHERZ-1261 | components | Do not put LEDs in parallel without individual dropping resistors - they become more conductive as they warm, giving unstable current sharing; a series string may share one resistor (use the sum of the forward drops as V_LED), and parallel strings each need their own resistor. Keep the total LED drop to no more than 80 % of the supply voltage for stable, predictable current | sum(V_F) <= 0.8*V_supply; 1 resistor per parallel branch | topology, V_F, V_supply | LED arrays | inspect | §5.3.4 p.505, Fig.5.10d-e | high |
| SCHERZ-1262 | power | LED from the ac line (capacitive dropper): 0.47 uF (5640 ohm at 60 Hz) gives ~20 mA half-wave (10 mA average); a series resistor limits worst-case inrush to ~150 mA, falling below 30 mA within ~1 ms; a diode (or reversed LED) in anti-parallel carries the negative half cycle and limits LED reverse voltage; the capacitor must be nonpolarized and rated 200 V or more. White-LED nightlight variant: 0.47 uF + 180 ohm + bridge + filter capacitor + 15 V zener for four 3.4 V white LEDs (13.6 V) | X_C = 1/(2*pi*f*C); I ~ V_line/X_C | C, R, line V/f | line-powered indicators | calc | §5.3.4 p.505, Fig.5.10b-c | high |
| SCHERZ-1263 | components | Blinking LEDs (internal IC, 1-6 flashes per second) need no series resistor but must stay within their recommended supply - 3 to 9 V is a safe range; a zener in reverse parallel provides overvoltage protection | 3 V <= V_supply <= 9 V | V_supply | flashers | calc | §5.3.2 p.501; §5.3.4 p.505, Fig.5.10j | high |
| SCHERZ-1264 | compliance | Laser diodes: never look into the beam or a specular reflection; they are extremely ESD sensitive (use grounding straps and grounded equipment). Typical optical output 1-5 mW for low-power parts (visible 3-5 mW typical; CD 780 nm up to 5 mW at the chip, 0.3-1 mW at the disc; read-write drives ~30 mW); high-power arrays reach 100 W or more. The beam is divergent and astigmatic (e.g. 10 x 30 deg, aspect ratio 3:1) with ~1 nm spectral width (LED ~40 nm) | eye and ESD precautions | P_o, lambda | laser products | review | §5.3.5 p.506-508, p.511 | high |
| SCHERZ-1265 | protection | Laser-diode drive: never drive one without a proper driver (a lab power supply gives inadequate protection). Constant-current (ACC) drive without temperature control lets optical output rise as the diode cools, possibly past its maximum; constant-power (APC, monitor-photodiode feedback) drive still needs an absolute current limit because an inadequate heat sink leads to thermal runaway. Drive current must never overshoot - exceeding maximum optical output even for a nanosecond damages the facet mirror coatings; drivers need slow-start, capacitive filtering and transient suppression | I_limit absolute; no overshoot | driver topology, heat sink | laser diode circuits | review | §5.3.5 p.508-509 | high |
| SCHERZ-1266 | bringup | Laser-diode bring-up: start with the supply current limit at 20-25 mA (a 100 ohm series resistor limits to ~85 mA); set the operating current (e.g. 50-60 mA) first on a dummy load of three ordinary diodes; never put a switch or relay between driver and diode; intermittent contacts in the photodiode feedback loop (or a pot wiper lifting) usually destroy the diode; measure optical power with an optical power meter or calibrated photodiode, including lens losses, because above threshold a small current increase gives a large power increase; heat-sink with non-silicone compound; clean windows with a cotton swab and ethanol | I_start 20-25 mA | I_op, P_o,max | laser diode prototypes | measure | §5.3.5 p.509-510, Fig.5.12 | high |
| SCHERZ-1267 | components | Laser modules and pointers are heavily filtered and can be modulated only at a few hertz - unsuitable for optical communication. Key laser-diode specs: threshold current I_th, operating current I_op, voltage V_op, maximum optical power P_o, monitor current I_m, photodiode dark current, reverse voltages V_R(LD)/V_R(PD), aspect ratio, astigmatism, divergence (FWHM), polarization ratio (> 100:1 near maximum power), slope efficiency, 10-90 % rise time | per datasheet | application | laser selection | review | §5.3.5 p.510-512 | medium |
| SCHERZ-1268 | components | Photoresistors (LDRs): dark resistance in megohms, falling to a few hundred ohms when illuminated; respond in milliseconds but take seconds to return to dark resistance; CdS responds best at 400-800 nm, PbS in the infrared. Read through a divider into a microcontroller ADC; relay examples use R1 ~1 kohm (light-activated) or 100 kohm (dark-activated) with a 6-9 V, 500 ohm relay | recovery ~seconds | light level, speed | light/dark switches | review | §5.4 p.512-514, Fig.5.15 | high |
| SCHERZ-1269 | components | Photodiodes: nearly linear light-to-current response; in photoconductive (reverse-biased) mode dark current is in the nA range and output current is larger; larger active area means slower response. Example NTE3033 (IR): V_R 30 V, dark current 50 nA max, light current 35 uA min, 100 mW, rise time 50 ns, 65 deg, 900 nm peak | I_dark ~ nA | area, speed | light meters, IR data links | review | §5.5 p.514-516, Table 5.2 | high |
| SCHERZ-1270 | power | Solar cells: 0.45-0.5 V open circuit per silicon cell, up to ~0.1 A in bright light, ~20 ms response; series for voltage, parallel for current. Charger example: nine cells (4.5 V) minus a 0.6 V blocking diode charge two NiCd cells - the diode stops the batteries discharging through the cells in darkness; add a series resistor so the NiCd safe charge rate is not exceeded | V_oc ~0.5 V/cell; I <= 0.1 A/cell | cells, battery | solar charging | calc | §5.6 p.516-517, Fig.5.21 | high |
| SCHERZ-1271 | components | Phototransistors: dark current in the nA range; photodarlingtons are more sensitive but slower; three-lead parts allow base bias. Examples: NTE3031 npn - BV 30 V, I_C 40 mA, dark 100 nA at 10 V, light current 1 mA min, 150 mW, 6 us; NTE3036 Darlington - 50 V, 250 mA, 100 nA, 12 mA, 250 mW, 151 us. Follow with a power transistor to switch relays; a 100 kohm pot sets sensitivity | speed vs sensitivity trade | speed, I_C | light-activated switching, IR receivers, tachometers | review | §5.7 p.517-520, Table 5.3, Fig.5.26 | high |
| SCHERZ-1272 | components | Optoisolators: closed pairs give galvanic isolation and level shifting (LED side ~1 kohm from 5 V; phototransistor pull-up 4.7 kohm to 5-12 V; inverting or non-inverting output); slotted interrupters for presence, bounce-free switching and vibration; reflective pairs for object detection and tachometers. Add a power transistor when the phototransistor cannot switch the load. Zero-crossing opto-triacs (MOC3041) switch on only at the zero crossing and drive a power triac on 110 V ac with minimal current surges. LASCRs latch until anode polarity reverses or power is removed | isolation barrier per design | isolation need, load | isolated I/O, SSRs | review | §5.8-5.9 p.521-523, Fig.5.30-5.33 | high |
| SCHERZ-1273 | components | Optical fibre: single-mode fibre (core 8-10.5 um, cladding 125 um) carries ~50 Gb/s over hundreds of miles; in multimode fibre different path lengths limit bandwidth (worse with larger cores). Laser diodes for telecom (coherent light travels better), LEDs for low-cost links such as consumer digital audio | per link budget | distance, rate | optical data links | review | §5.10 p.524 | high |
| SCHERZ-1274 | requirements | Specify sensors by accuracy, not displayed precision: a scale reading 85.7 kg for a true 92.1 kg (~10 % error) is precise but inaccurate. Digital sensors are quantized - 8 bits = 1 in 256, 12 bits = 1 in 4096 (the book's "12-bit ... 0 to 1023" is a 10-bit range). Remember the observer effect (measuring disturbs the measurand, e.g. a tyre gauge releasing air) | accuracy spec separate from resolution | sensor spec | sensor requirements | review | §6.1.1-6.1.2 p.525-526 | high |
| SCHERZ-1275 | process | Calibration strategy: in low-cost mass-produced products avoid per-unit calibration (prohibitively expensive) and choose factory-calibrated IC sensors (calibration stored in on-chip ROM); in specialized high-value equipment calibrate each sensor against a standard of known accuracy (itself calibrated against a more accurate standard) and store raw-to-actual pairs in a lookup table with linear interpolation between entries | calibration plan per cost class | product class | sensor subsystems | review | §6.1.3 p.526-528, Fig.6.3 | high |
| SCHERZ-1276 | hw-fw | For analog sensors choose a microcontroller with a built-in ADC (a discrete ADC is "to be avoided"), or a sensor with an integrated ADC/digital interface that connects directly to a data port | built-in ADC preferred | MCU choice | sensor interfacing | review | §6.1 p.527, Fig.6.2 | medium |
| SCHERZ-1277 | components | NTC thermistors are strongly nonlinear (a linear approximation over 0-100 degC gives considerable error). Beta model: 1/T = (1/beta)*ln(R/R0) + 1/T0 (T in kelvin, T0 usually 25 degC), R = R0*e^(beta*(1/T - 1/T0)); Steinhart-Hart 1/T = A + B*ln(R) + C*ln^3(R) with the maker's constants. In a divider with R1 = R0 below the NTC: V_out = V_in*R1/(R1 + R). Worked: 4.7 kohm, beta 3977, 5 V -> 2.5 V at 25 degC, 1.15 V at 0 degC. Typical thermistor range -40 to +125 degC, ~+/-1 degC | V_out(T) per formula | R0, beta, R1, V_in | temperature sensing | calc | §6.2.1 p.529-531, Eq.6.1-6.5, Table 6.1 | high |
| SCHERZ-1278 | components | Thermocouples: the Seebeck voltage depends on the metal pair; measure the cold-junction temperature too (e.g. with a thermistor) and linearize with the maker's tables or a fifth-order polynomial. Chromel-alumel covers -200 to +1350 degC at 41 uV/degC (~+/-3 degC typical); the lead wires are part of the sensor and it measures a temperature difference | V ~ 41 uV/degC (chromel-alumel) | junction types, CJC | high-temperature sensing | calc | §6.2.2 p.531-532, Table 6.1 | high |
| SCHERZ-1279 | components | Platinum RTDs: typically 100 ohm at 0 degC with 0.003925 ohm/ohm/degC (0-100 degC), so 139.25 ohm at 100 degC; approximately linear over ~100 degC; usable -260 to 800 degC; ~+/-1 degC, accurate but expensive with slow response | R = R0*(1 + 0.003925*T) | T | precision temperature | calc | §6.2.3 p.532, Table 6.1 | high |
| SCHERZ-1280 | components | Temperature ICs: TMP36 (2.7-5.5 V, 0.1 uF bypass) outputs 10 mV/degC, T = 100*V_out - 50, -40 to +125 degC, +/-2 degC; DS18B20 1-Wire (3.0-5.5 V, 4.7 kohm pull-up on DQ) +/-0.5 degC over -55 to +125 degC, digital so it tolerates long leads and noise ("works accurately or not at all"); in parasitic-power (two-wire) mode the MCU must drive a MOSFET strong pull-up under strict timing | T[degC] = 100*V_out - 50 (TMP36) | sensor choice | board and remote temperature | calc | §6.2.4-6.2.5 p.532-534, Fig.6.8-6.9 | high |
| SCHERZ-1281 | components | Infrared thermometers use the Stefan-Boltzmann law j* = sigma*T^4 (sigma = 5.6704e-8 J s^-1 m^-2 K^-4); MLX90614 covers -70 to 380 degC and MLX90616 up to 1030 degC, ~+/-0.5 degC, with integrated low-noise amplifier and ADC | j* = sigma*T^4 | T range | non-contact temperature | review | §6.2.6 p.534-535, Table 6.1 | high |
| SCHERZ-1282 | components | Four-wire resistive touch screen: drive one layer's opposite edges to 0 V and 5 V and read the other layer with a high-input-impedance ADC (several Mohm, so track resistance is negligible) - voltage is proportional to position; swap roles for the other axis | ADC R_in >> screen R | ADC, sequencing | touch interfaces | review | §6.3.1 p.535-536, Fig.6.11 | high |
| SCHERZ-1283 | components | Ultrasonic ranging: distance = v*t/2 (340 m/s, 10 ms round trip -> 1.7 m); speed of sound in dry air is 331 m/s at 0 degC and 346 m/s at 25 degC (4.5 % change), so compensate temperature (also pressure, humidity); range up to ~5 m depending on target size and reflectivity (Table 6.2: 150 mm-6 m, +/-25 mm) | d = v*t/2; v(T) | t, T | distance measurement | calc | §6.3.2 p.536-537, Table 6.2 | high |
| SCHERZ-1284 | components | IR reflective distance sensors (e.g. Sharp GP2Y0A21YK): nonlinear analog output, ambiguous below ~5 cm - mount recessed so objects cannot come closer; convert with a lookup table; 100-800 mm, +/-10 mm, sensitive to target IR reflectivity; slotted optical sensors only detect presence | min distance >= ~5 cm | distance range | proximity/ranging | inspect | §6.3.3 p.537-538, Fig.6.14, Table 6.2 | high |
| SCHERZ-1285 | components | Capacitive proximity/touch with two GPIOs and a 1 Mohm resistor: time the RC delay between the send and receive pins; senses through glass and plastic up to ~30 cm but detects only conductive objects with a resistive link to earth | range 0-30 cm | plate, R | button replacement | review | §6.3.4 p.539-540, Fig.6.15, Table 6.2 | high |
| SCHERZ-1286 | components | PIR motion modules with an open-collector output need a pull-up (10 kohm to V_in) to give a digital level; MEMS accelerometers sense a = k*(x - x0)/m via a capacitive divider and usually integrate 3 axes, ADC and I2C (e.g. MMA8452Q), also giving orientation from gravity | pull-up on open collector | output type | motion sensing | inspect | §6.4.1-6.4.2 p.540-542, Fig.6.17-6.19 | high |
| SCHERZ-1287 | components | Rotation sensing (Table 6.3): potentiometer 2-5 deg accuracy with end stops (~300 deg); low-cost quadrature encoder ~12 pulses/rev (30 deg); optical quadrature encoders up to 200 pulses/rev (2 deg) and 30,000 rpm; direction from the order of A/B transitions; absolute encoders output Gray code (one bit changes per step; 3-bit 000, 001, 011, 010, 110, 111, 101, 100; 4-bit ~22 deg) | resolution = 360/PPR | PPR, rpm | angle/speed sensing | calc | §6.4.3 p.542-543, Fig.6.20-6.21, Table 6.3 | high |
| SCHERZ-1288 | components | Flow sensing: paddle/cup rotors with Hall or optical pulse pickup (pulse frequency proportional to speed); hot-wire (current needed to hold temperature); ultrasonic transit-time (no moving parts, very geometry dependent); ultrasonic or laser Doppler (need particles in the fluid; laser accurate but expensive) | method per fluid | fluid, geometry | flow metering | review | §6.4.4 p.543-544, Table 6.4 | high |
| SCHERZ-1289 | components | Force and vibration: force-sensitive resistors are usually not very accurate; strain gauges change resistance with tension/compression; load cells bond two or more gauges to a deformable block with temperature compensation for accurate force; piezoelectric vibration/shock sensors drift - place 10 Mohm in parallel with them | 10 Mohm across piezo | sensor type | force/shock sensing | inspect | §6.4.5-6.4.7 p.544-545 | high |
| SCHERZ-1290 | components | Integrated environmental sensors: MPX2010 0-10 kPa differential (temperature compensated, factory calibrated); KP125 40-115 kPa absolute (+/-1.2 kPa, altimeter/barometer); MQ-4 methane from 200 ppm (heater ~5 V drawing a few tens of mA, read via a divider); capacitive humidity ICs +/-1-2 % (laser-calibrated); Geiger-Muller tubes need 400-500 V with a 10 Mohm anode resistor (thin mica end window for alpha) | per datasheet ranges | measurand | environmental sensing | review | §6.4.8-6.6.2 p.545-548, Table 6.5 | high |
| SCHERZ-1291 | components | Hall-effect sensing: V_H = -I*B/(n*e*d); switch types report magnet presence, linear types give output proportional to B; unlike a pickup coil (signal shrinks as the magnet slows) a Hall sensor detects static fields at any speed; most integrate amplification or a serial interface | V_H = -I*B/(n*e*d) | B, I | position/speed/current sensing | review | §6.6.3 p.548-549, Fig.6.28 | high |
| SCHERZ-1292 | compliance | Shock physiology (50-60 Hz, hand to foot): ~10 mA tingle; above 10 mA a person may freeze to the conductor; GFCIs trip at ~5-10 mA; 20-100 mA may be fatal; 100 mA-1 A is the deadliest range; above 1 A the heart makes a single contraction and tissue heating is severe. Body resistance ranges from ~1 Mohm (dry callused palm) to ~100 ohm (thin wet palm), 70-100 ohm across the chest; hand-to-hand current is most lethal, hand-to-foot ~20 % mortality | I_body = V/R_body | V, R_body | user-accessible voltages | calc | §7.1.1 p.551-552 | high |
| SCHERZ-1293 | compliance | Hazardous energy in equipment: microwave ovens run 5000 V or more with more than 1 A momentarily available; CRTs carry 35 kV and hold charge; line-connected circuits (SMPS, TVs) have internal grounds several hundred volts above earth - service them through an isolation transformer (a Variac is not isolated); SMPS, flash and strobe capacitors hold a lethal charge long after power is removed (even disposable cameras) | isolation + discharge before service | equipment type | servicing and design reviews | review | §7.1.1 p.552-554 | high |
| SCHERZ-1294 | compliance | Discharge large filter/energy-storage capacitors before touching with a 2 W or larger resistor of 100-500 ohm per volt (200 V capacitor -> 20-100 kohm), monitoring the voltage and verifying zero with a meter; a screwdriver short may damage the capacitor; large capacitors can keep a lethal charge for days and even 5-10 V parts can be dangerous | R = 100..500 ohm/V * V_cap; P >= 2 W | V_cap | service/test procedures | calc | §7.1.1 p.553, Tip 3 | high |
| SCHERZ-1295 | compliance | Bench safety practice: work unpowered where possible; one hand in a pocket when probing live; three-wire cords on line-powered HV test instruments; insulated probes with all but the last 1/16 in of tip taped; clip the reference first so only one hand probes; stand on rubber/wood; GFCIs do not protect against shocks from inside line-connected devices (and may nuisance-trip on scope-probe grounds); fuses and breakers are too slow to protect people; never assume a chassis is ground | procedure checklist | bench setup | lab work on mains equipment | inspect | §7.1.1 p.553-554, Tips 1-15 | high |
| SCHERZ-1296 | compliance | Line-powered builds: enclose all wiring in a metal box bonded to the power-cord ground (wire from the box's inner surface to the ground conductor, screw plus solder) or an insulated plastic enclosure; fit a rubber grommet where the ac cord passes through metal; rate every ac-connected component for the line | PE bond + grommet + rated parts | enclosure | mains-powered products | inspect | §7.1.1 p.554, Tips 16-18 | high |
| SCHERZ-1297 | esd | Static sources: walking on carpet ~1000 V, handling a polyethylene bag 300 V or more, combing hair up to 2500 V (worse at low humidity). Vulnerability: extremely - MOS transistors and ICs, JFETs, laser diodes, microwave transistors, metal-film resistors; moderately - CMOS ICs, LS and Schottky TTL, Schottky diodes, linear ICs; somewhat - TTL, small-signal diodes/transistors, piezo crystals; not vulnerable - capacitors, carbon-composite resistors, inductors | handling class per part | BOM | assembly and handling | review | §7.1.2 p.555 | high |
| SCHERZ-1298 | esd | ESD handling: keep sensitive parts in their original packs, conductive containers or conductive foam; do not touch leads; discharge yourself on grounded metal first; keep clothing away from parts; ground tabletops and soldering irons (or use a battery iron); wear a grounded wrist strap; never insert or remove an ESD-sensitive component with power applied | ESD procedure | part class | assembly, rework | inspect | §7.1.3 p.555-556 | high |
| SCHERZ-1299 | process | Schematic conventions: inputs left, outputs right, positive supplies at top, ground at bottom; keep functional groups separate; give every part a reference designator plus exact value/type and power rating where relevant (resistors, capacitors, relays, speakers); pin numbers outside IC symbols, part names inside; sketch expected waveforms at key nodes; show supply pins if confusion is possible; junction dots for connections (plain crossings are not connected); title block with circuit name, designer, date and revision list; before building check for missing values, polarities and power ratings; use CAD electrical rule checks (unconnected leads) | schematic review checklist | schematic | every design | inspect | §7.2.1 p.556-557, Fig.7.1 | high |
| SCHERZ-1300 | assembly | Prototype platforms: solderless breadboard on 0.100 in pitch accepting 22 AWG (0.015-0.032 in, 0.38-0.81 mm) wire, outer rows for supplies and the centre gap for DIPs; perforated board (0.100-0.200 in spacing, 0.042 in holes) only for simple noncritical circuits (jumpers act as antennas); wire-wrap with 30, 28 or 26 AWG, ~7 turns per post, suits multi-IC logic; a custom PCB is essential for high-speed logic (controlled microstrip geometry, precise placement against crosstalk) and sensitive low-level amplifiers (short, direct traces) | PCB for high-speed/low-level | circuit type | prototyping choices | review | §7.2.3-7.2.4 p.558-562, Fig.7.2-7.5 | high |
| SCHERZ-1301 | fab | PCB fabrication: typical board 1/16 in fire-resistant epoxy-glass; quick-turn services (from ~1 USD per board for ten, 1-2 weeks) are automated and will not check your design - pass DRC before submitting; send Gerbers (GTL/GBL top/bottom copper, GTS/GBS solder stop, GTO/GBO silkscreen, TXT drill) or a native .brd; two-layer boards come with vias, silkscreen and solder mask; large copper areas tied to GND form a ground plane (and reduce etchant use in home etching) | DRC clean before release | Gerber set | prototype PCB release | inspect | §7.2.5 p.562-567, Table 7.1 | high |
| SCHERZ-1302 | dfm | Board layout for assembly and service: place ICs and resistors in rows, all oriented the same way; keep a ~2 mm border for card lifters, guides and standoffs; bring power and I/O to the board edge through edge, D-sub or barrier connectors or binding posts; avoid heavy components on the board (drop damage); mark polarity next to diodes and electrolytics; label IC pins, test points, trimmer functions, inputs/outputs, indicators and supply terminals; in multi-board systems put each functional group on its own board; use IC sockets only where replacement is likely (too many sockets hurt reliability) | 2 mm edge keep-out; polarity marks | layout | PCB layout review | inspect | §7.2.5-7.2.6 p.567 | high |
| SCHERZ-1303 | thermal | Heat sinking and enclosure cooling: fasten heat sinks with screw and washer plus silicone grease; orient fins vertically; place major heat producers toward the back, heat-sunk through the back panel; mount boards vertically for ventilation; consider a blower fan above ~10 W of dissipation, otherwise vent holes top and bottom | fan if P > ~10 W | P_total, layout | enclosure thermal design | review | §7.2.6 p.568; §7.2.9 p.569-570, Fig.7.13 | high |
| SCHERZ-1304 | solder | Hand soldering: clean surfaces of oil, silicone, wax and grease (solvent, steel wool, fine sandpaper); use a 25-40 W iron for PCBs with a freshly tinned tip; heat the joint and let solder flow to it (do not melt solder first); inspect for spatter bridges and sound joints; heat-sink sensitive leads with pliers or clips; lead-free solder is required for consumer electronics under the EU RoHS directive; desolder with a suction tool or wick | iron 25-40 W | process | hand assembly/rework | inspect | §7.2.7-7.2.8 p.568-569 | high |
| SCHERZ-1305 | mechanical | Enclosures: aluminium boxes for high-voltage circuits (ground the box), plastic for low voltage; support boards on standoffs; ac cord through a strain relief and grommet; frequently used controls, displays and inputs on the front panel, seldom-used switches and fuses on the back | layout rules | enclosure | product packaging | inspect | §7.2.9 p.569-570, Fig.7.13 | high |
| SCHERZ-1306 | test | Multimeter choice: a DMM resolves ~1 part in 1000 versus ~1 in 100 for an analog VOM (which has ~3 % more reading error), but an analog meter stays readable in electrical noise where a DMM may blank; ac ranges display RMS on a sine basis; measure current in series (break the circuit) and resistance only with power removed | meter per task | signal, noise | bench measurement | measure | §7.3 p.571-573, Fig.7.15-7.18 | high |
| SCHERZ-1307 | test | Meter loading error: analog ammeter ~2 kohm, voltmeter ~100 kohm and ohmmeter ~50 ohm internal resistance. Worked: 2 kohm ammeter in an 8 kohm loop reads 40 uA for 50 uA (20 % error); 100 kohm voltmeter across 100 kohm of a 100 k/100 k divider reads 6.67 V for 10 V (33 %); 50 ohm ohmmeter on 200 ohm reads 250 ohm (25 %). Keep ammeter resistance <= 1/20 of the circuit Thevenin resistance and voltmeter resistance >= 20x it to hold error below 5 % (or correct for the known internal resistance) | R_V >= 20*R_TH; R_A <= R_TH/20 | R_meter, R_TH | bench measurement | calc | §7.3.4 p.574-575, Fig.7.23-7.25 | high |
| SCHERZ-1308 | test | Oscilloscopes measure voltage only; measure current across a precision 1 ohm shunt (small enough not to disturb the circuit) rated at least 2 ohm x I_max^2 watts (twice I^2*R; 0.5 A -> 1/2 W); other quantities through transducers | P_shunt >= 2*R*I_max^2 | I_max | current probing | calc | §7.4 p.576; §7.4.6 p.588-589, Fig.7.40-7.41 | high |
| SCHERZ-1309 | test | Scope practice: compensate probes on the CAL output (1 kHz, 0.1 Vpp square wave); trigger coupling AC (10 Hz to >35 MHz), DC (dc to >35 MHz), LF REJ (dc blocked, <10 kHz attenuated - stable triggering with 60 Hz hum), HF REJ (>100 kHz attenuated); DC AUTO sweep for dc and low-amplitude signals, SINGLE for non-repetitive events; set the GND reference before dc readings; for phase use short, equal-length, similar cables (mismatch adds phase shift at HF), phase = displacement x 360 deg/period (8 cm period -> 45 deg/cm; 2 cm -> 90 deg) | phase = d*360/T | probe, trigger setup | bench verification | measure | §7.4.5-7.4.6 p.583-590, Fig.7.34-7.43 | high |

## 2. Formulas & tables (numbers)

### T-SCHERZ-2.2 Electrical and thermal properties of materials (Table 2.2, p.26)

Extraction note: the source table is column-scrambled; values below were re-associated by column order and checked against the book's own worked example (brass 7.0e-8, stainless 7.2e-7, graphite 3.5e-5, copper 1.72e-8 ohm*m on p.34). Temperature-coefficient and thermal-conductivity cells for Au, Pt, Pb, stainless and the semiconductors are partly missing in the extraction; only cells with an unambiguous mapping are given.

| material | resistivity rho (ohm*m) | conductivity sigma (1/(ohm*m)) | temp. coeff. alpha (1/degC) | thermal conductivity k (W/(cm*degC)) | thermal resistivity (cm*degC/W) |
|---|---|---|---|---|---|
| Aluminum | 2.82e-8 | 3.55e7 | 0.0039 | 2.165 | 0.462 |
| Gold | 2.44e-8 | 4.10e7 | n/a in extraction | 2.913 | 0.343 |
| Silver | 1.59e-8 | 6.29e7 | 0.0038 | 4.173 | 0.240 |
| Copper | 1.72e-8 | 5.81e7 | 0.0039 | 3.937 | 0.254 |
| Iron | 10.0e-8 | 1.0e7 | 0.0050 | 0.669 | 1.495 |
| Tungsten | 5.6e-8 | 1.8e7 | 0.0045 | 1.969 | 0.508 |
| Platinum | 10.6e-8 | 1.0e7 | 0.003927 | - | - |
| Lead | 0.22e-6 | 4.54e6 | - | 0.343 (mapping medium) | 2.915 (mapping medium) |
| Steel (stainless) | 0.72e-6 | 1.39e6 | - | 0.148 ("(312)") | 6.757 |
| Nichrome | 100e-8 | 0.1e7 | 0.0004 | - | - |
| Manganin | 44e-8 | 0.23e7 | 0.00001 | - | - |
| Brass | 7e-8 | 1.4e7 | 0.002 | 1.22 | 0.820 |
| Carbon (graphite) | 3.5e-5 | 2.9e4 | -0.0005 | - | - |
| Germanium | 0.46 | 2.2 | -0.048 | 0.591 (Ge or GaAs; mapping low) | 1.692 |
| Silicon | 640 | 3.5e-3 (as printed) | -0.075 | 1.457 (pure) | 0.686 |
| Gallium arsenide | not in extraction | - | - | - | - |
| Glass | 1e10 - 1e14 | 1e-14 - 1e-10 | - | - | - |
| Neoprene rubber | 1e9 | 1e-9 | - | - | - |
| Quartz (fused) | 75e16 | 1e-16 (as printed) | - | - | - |
| Sulfur | 1e15 | 1e-15 | - | - | - |
| Teflon | 1e14 | 1e-14 | - | - | - |

Resistivity classes (§2.6 p.28): conductor ~1e-8 ohm*m; good insulator ~1e14 ohm*m; semiconductor 1e-5 to 1e3 ohm*m (temperature dependent). Band gaps: Si 1.1 eV, Ge 0.7 eV, diamond 6 eV (p.30).

### T-SCHERZ-2.3 Resistivity of special media (Table 2.3, p.27-28)

| medium | resistivity (ohm*m) | notes |
|---|---|---|
| Pure (distilled) water | 2.5e5 | ion conduction; measured ~20e6 ohm/cm between electrodes in a bucket |
| Saltwater | ~0.2 | 1 g NaCl adds ~2e22 ions; below 1 ohm per meter |
| Human skin | ~5.0e5 | varies with moisture and salt |
| Air | insulator | breakdown ~3 MV/m plane electrodes; 1 cm gap ~30 kV; point electrode a few kV; 5-10 ion pairs/s/cm at sea level |
| Vacuum | perfect insulator | conduction only via thermionic, field (MV/cm), secondary or photoelectric emission |

### T-SCHERZ-2.4 Thermal resistivities lambda (Table 2.4, p.36), units degC*in/W (divide by 39 for degC*m/W)

Reconstructed from a three-column-pair layout; verified against the book's example (alumina 2.13, silicone grease 46, aluminum 0.23).

| material | lambda | material | lambda | material | lambda |
|---|---|---|---|---|---|
| Diamond | 0.06 | Lead | 1.14 | Quartz | 27.6 |
| Silver | 0.10 | Indium | 2.1 | Glass (774) | 34.8 |
| Copper | 0.11 | Boron nitride | 1.24 | Silicon grease | 46 |
| Gold | 0.13 | Alumina ceramic | 2.13 | Water | 63 |
| Aluminum | 0.23 | Kovar | 2.34 | Mica | 80 |
| Beryllia ceramic | 0.24 | Silicon carbide | 2.3 | Polyethylene | 120 |
| Molybdenum | 0.27 | Steel (300) | 2.4 | Nylon | 190 |
| Brass | 0.34 | Nichrome | 3.00 | Silicon rubber | 190 |
| Silicon | 0.47 | Carbon | 5.7 | Teflon | 190 |
| Platinum | 0.54 | Ferrite | 6.3 | P.P.O. | 205 |
| Tin | 0.60 | Pyroceram | 11.7 | Polystyrene | 380 |
| Nickel | 0.61 | Epoxy (high conductivity) | 24 | Mylar | 1040 |
| Tin solder | 0.78 | - | - | Air | 2280 |

Thermal/electrical analogy (p.37): k [W/(m*degC)] ~ sigma; lambda [m*degC/W] ~ rho; R_th [degC/W] ~ R; P_heat [W] ~ I; dT [degC] ~ V; heat source ~ current source.

Worked example (p.37): 0.1 m of #12 copper (d = 2.053 mm, A = 3.31e-6 m^2, k = 390 W/(m*degC)) -> R_th = 77.4 degC/W; assuming ~10 W of a 25 W soldering iron actually enters the wire, dT = 774 degC, hot end ~799 degC over 25 degC ambient (steady state).

### T-SCHERZ-2.5 Copper wire specifications, bare and enamel-coated (Table 2.5, p.39)

1 mil = 0.001 in = 0.0254 mm; circular mil (CM) = area of a 1-mil-diameter circle; CM area = (diameter in mils)^2.

| AWG | diameter (mils) | area (CM) | feet per pound, bare | ohms per 1000 ft, 25 degC | current capacity (A) |
|---|---|---|---|---|---|
| 4 | 204.3 | 41738.49 | 7.918 | 0.2485 | 59.626 |
| 8 | 128.5 | 16512.25 | 25.24 | 0.7925 | 18.696 |
| 10 | 101.9 | 10383.61 | 31.82 | 0.9987 | 14.834 |
| 12 | 80.8 | 6528.64 | 50.61 | 1.5880 | 9.327 |
| 14 | 64.1 | 4108.81 | 80.39 | 2.5240 | 5.870 |
| 18 | 40.3 | 1624.09 | 203.5 | 6.3860 | 2.320 |
| 20 | 32 | 1024.00 | 222.7 | 10.1280 | 1.463 |
| 22 | 25.3 | 640.09 | 516.3 | 16.2000 | 0.914 |
| 24 | 20.1 | 404.01 | 817.7 | 25.6700 | 0.577 |
| 28 | 12.6 | 158.76 | 2081 | 65.3100 | 0.227 |
| 32 | 8.0 | 64.00 | 5163 | 162.0000 | 0.091 |
| 40 | 3.1 | 9.61 | 34364 | 1079.0000 | 0.014 |

(Values transcribed exactly as printed; some cells, e.g. AWG 8 ohms/1000 ft and AWG 20 feet/lb, deviate from standard AWG tables - use the Sec. 3.1 table where they differ.)

### T-SCHERZ-2.2.1 Typical load currents ("Currents in perspective", §2.2.1 p.9)

| load | current |
|---|---|
| 100 W lightbulb | ~1 A |
| microwave oven | 8 - 13 A |
| laptop computer | 2 - 3 A |
| electric fan | 1 A |
| television | 1 - 3 A |
| toaster | 7 - 10 A |
| fluorescent light | 1 - 2 A |
| radio/stereo | 1 - 4 A |
| typical LED | 20 mA |
| smartphone accessing web | ~200 mA |
| advanced low-power microchip | a few uA down to several pA |
| automobile starter | ~200 A |
| lightning strike | ~1000 A |
| current sufficient to induce cardiac/respiratory arrest | ~100 mA to 1 A |

### T-SCHERZ-2.12 Resistive-network formulas (§2.12-2.19, p.50-80)

| quantity | formula | source |
|---|---|---|
| Ohm's law | V = I*R | Eq.2.15 p.50 |
| Ohm's power law | P = I*V = V^2/R = I^2*R | Eq.2.16 p.50 |
| Parallel | 1/R_tot = 1/R1 + 1/R2 + ...; two resistors R1*R2/(R1+R2); R_tot < smallest R | Eq.2.17-2.18 p.53 |
| Series | R_tot = R1 + R2 + ... | Eq.2.19 p.55 |
| Voltage divider | V1 = Vin*R1/(R1+R2); V2 = Vin*R2/(R1+R2) | p.56 |
| Current divider (two branches) | I1 = Iin*R2/(R1+R2) | Fig.2.41 p.52-54 |
| KVL | sum of voltage changes around any closed loop = 0 (linear and nonlinear elements) | Eq.2.20 p.70 |
| KCL | sum I_in = sum I_out at any junction | Eq.2.21 p.71 |
| Superposition | branch current = sum of currents from each source with others zeroed (V sources shorted, I sources opened); linear circuits only | §2.18 p.74-75 |
| Thevenin | V_TH = open-circuit voltage; R_TH = resistance with sources zeroed; I_load = V_TH/(R_TH + R_load) | §2.19.1 p.76-77 |
| Norton | I_N = short-circuit current; R_N = R_TH; V_TH = I_N*R_TH | §2.19.2 p.77-78 |
| Real voltage source | V_T = Vs*Rload/(Rload + rs) | §2.13 p.64 |
| Real current source | I_T = Is*rs/(Rload + rs) | §2.13 p.64 |

Typical resistor values run 1 ohm to 10,000,000 ohm (§2.12 p.51).

### T-SCHERZ-2.87 AC conversion factors, sinusoid (Fig.2.87, p.90)

| from | to | multiply by |
|---|---|---|
| peak | peak-to-peak | 2 |
| peak-to-peak | peak | 0.5 |
| peak | RMS | 1/sqrt(2) = 0.7071 |
| RMS | peak | sqrt(2) = 1.4142 |
| peak-to-peak | RMS | 1/(2*sqrt(2)) = 0.35355 |
| RMS | peak-to-peak | 2*sqrt(2) = 2.828 |
| peak | average* | 2/pi = 0.6366 |
| average* | peak | pi/2 = 1.5708 |
| RMS | average* | 2*sqrt(2)/pi = 0.9003 |
| average* | RMS | pi/(2*sqrt(2)) = 1.1107 |

*average over half a cycle. f = 1/T (Eq.2.22); 60 Hz -> T = 0.0167 s; T = 2 ns -> 500 MHz.

### T-SCHERZ-2.89 Waveform conversion matrix (Fig.2.89, p.92)

Read: if the row quantity = 1.00, the column gives the other quantity.

| waveform | known = 1.00 | half-wave average | RMS | peak | peak-to-peak |
|---|---|---|---|---|---|
| sine | half-wave average | 1.00 | 1.11 | 1.567 (as printed; exact 1.5708) | 3.14 |
| sine | RMS | 0.90 | 1.00 | 1.414 | 2.828 |
| sine | peak | 0.637 | 0.707 | 1.00 | 2.00 |
| sine | peak-to-peak | 0.318 | 0.354 | 0.50 | 1.00 |
| square | any of avg/RMS/peak | 1.00 | 1.00 | 1.00 | 2.00 |
| triangle/sawtooth | half-wave average | 1.00 | 1.15 | 2.00 | 4.00 |
| triangle/sawtooth | RMS | 0.87 | 1.00 | 1.73 | 3.46 |
| triangle/sawtooth | peak | 0.50 | 0.578 | 1.00 | 2.00 |
| triangle/sawtooth | peak-to-peak | 0.25 | 0.289 | 0.50 | 1.00 |

(Square-wave row is sparse in the extraction: average = RMS = peak, peak-to-peak = 2 x peak.)

### T-SCHERZ-2.23 Capacitor fundamentals (§2.23, p.94-105)

| item | value / formula | source |
|---|---|---|
| capacitance | C = Q/V (F = C/V) | Eq.2.32 p.96 |
| parallel plate | C = k*eps0*A/d; multi-plate C = k*eps0*A*(n-1)/d | Eq.2.35-2.37 p.98 |
| eps0 | 8.85e-12 C^2/(N*m^2) (F/m) | Eq.2.34 p.98 |
| dielectric constant range | 1.00059 (air, 1 atm) to > 1e5 (some ceramics) | p.98 |
| current | I = C*dV/dt | Eq.2.40 p.102 |
| voltage | V = (1/C)*integral(I dt) | Eq.2.41 p.102 |
| commercial range | 1 pF to 4700 uF | p.96 |
| preferred mantissas | 10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82, 100 | p.96 |
| air spark voltage | ~100 kV/cm (0.005 cm gap) to "30 kV/mm" as printed (10 cm gap) | p.100 |

### T-SCHERZ-2.43 RC / RL exponential milestones (§2.23.8 p.106-108)

| time | charging (% of Vs) | discharging (% of Vs remaining) |
|---|---|---|
| 1 tau | 63.2 | 36.8 (printed 37.8) |
| 2 tau | 86.5 | 13.5 (derived) |
| 3 tau | 95 | 5 (derived) |
| 5 tau | 99.24 ("fully charged") | 0.76 ("fully discharged") |

tau = R*C (RC) or L/R (RL). Book graphs: charging R = 10 kohm, C = 100 uF (Fig.2.101); discharging R = 3 kohm, C = 0.1 uF (Fig.2.103); RL R = 100 ohm, L = 20 mH (Fig.2.136).

### T-SCHERZ-2.7 Typical characteristics of commercial inductors (Table 2.7, p.130)

Transcribed as printed; several min/max entries may carry a u/m prefix ambiguity from the source (e.g. ferrite ring 10 mH-20 mH) - verify against print before relying on them.

| core type | minimum L | maximum L | adjustable? | high current? | frequency limit |
|---|---|---|---|---|---|
| Air core, self-supporting | 20 nH | 1 mH | Yes | Yes | 1 GHz |
| Air core, on former | 20 nH | 100 mH | No | Yes | 500 MHz |
| Slug tuned open winding | 100 nH | 1 mH | Yes | No | 500 MHz |
| Ferrite ring | 10 mH | 20 mH | No | No | 500 MHz |
| RM ferrite core | 20 mH | 0.3 H | Yes | No | 1 MHz |
| EC or ETD ferrite core | 50 mH | 1 H | No | Yes | 1 MHz |
| Iron | 1 H | 50 H | No | Yes | 10 kHz |

Commercial inductors range from fractions of a nanohenry to about 50 H (p.130).

### T-SCHERZ-2.8 Permeability of various materials (Table 2.8, p.134-135)

| material | approx. max permeability (H/m) | approx. max relative permeability | typical application (column mapping medium) |
|---|---|---|---|
| Air | 1.257e-6 | 1 | RF |
| Ferrite U60 | 1.00e-5 | 8 | UHF chokes |
| Ferrite M33 | 9.42e-4 | 750 | resonant circuits |
| Ferrite N41 | 3.77e-3 | 3000 | power circuits |
| Iron (99.8 % pure) | 6.28e-3 | 5000 | - |
| Ferrite T38 | 1.26e-2 | 10,000 | broadband transformers |
| 45 Permalloy | 3.14e-2 | 25,000 | - |
| Silicon GO steel (printed "Silicon 60 steel") | 5.03e-2 | 40,000 | dynamos, transformers |
| 78 Permalloy | 0.126 | 100,000 | - |
| Supermalloy | 1.26 | 1,000,000 | recording heads |

Example (p.134): air core 50 lines/in^2 vs iron core 40,000 lines/in^2 -> mu_r = 800. A core can magnify field strength by up to ~1000 (p.117).

### T-SCHERZ-2.9 Inductor core comparison (Table 2.9, p.137) and toroid formulas (Fig.2.133, p.138)

| core | mu_r / notes | saturation | eddy/hysteresis | frequency range | use |
|---|---|---|---|---|---|
| Air | 1; low L only | none | none | to ~1 GHz | RF |
| Iron (laminated) | ~1000x air | yes - L depends on current | high eddy (laminate), significant hysteresis, both rise fast with f | power line and audio to ~15,000 Hz; useless at RF | power-supply equipment |
| Powdered iron | low (binder) | - | eddy greatly reduced | RF up to VHF | slug-tuned coils; self-shielding toroids; AL in uH/100 turns |
| Ferrite (Ni-Zn low mu, Mn-Zn high mu) | 20 to >10,000 | - | non-conductive, immune to eddy currents | RF | RF chokes, wideband transformers; AL in mH/1000 turns |

| toroid type | inductance | turns |
|---|---|---|
| powdered iron (AL uH/100 turns) | L(uH) = AL*N^2/10,000 | N = 100*sqrt(L_uH/AL) |
| ferrite (AL mH/1000 turns) | L(mH) = AL*N^2/1,000,000 | N = 1000*sqrt(L_mH/AL) |

Ferrite resistivity: Mn-Zn 10-1,000 ohm*cm; Ni-Zn 1e5-1e7 ohm*cm (p.135).

### T-SCHERZ-2.27 Complex impedance toolkit (§2.26-2.29, p.159-187)

| element / law | expression |
|---|---|
| resistor | Z_R = R (V and I in phase) |
| capacitor | Z_C = -j/(omega*C) = (1/(omega*C)) at -90 deg (current leads voltage by 90 deg) |
| inductor | Z_L = j*omega*L = omega*L at +90 deg (current lags voltage by 90 deg) |
| ac Ohm's law | V(omega) = I(omega)*Z(omega) (Eq.2.69) |
| series | Z_tot = Z1 + Z2 + ... (Eq.2.70) |
| parallel | 1/Z_tot = sum(1/Z_i); two: Z1*Z2/(Z1+Z2) (Eq.2.71-2.72) |
| magnitude/phase | abs(Z) = sqrt(Re^2 + Im^2); arg(Z) = atan(Im/Re) (Eq.2.66) |
| reciprocal | 1/(A + jB) = (A - jB)/(A^2 + B^2) |
| ac Thevenin | V_TH = open-circuit phasor voltage; Z_TH = impedance with sources shorted (§2.29 p.186) |

Worked examples (RMS values):

| circuit | source | components | result |
|---|---|---|---|
| series RL (Fig.2.167) | 12 VAC, 60 Hz | R 50 ohm, L 265 mH (X_L j100) | Z 112 ohm at 63.4 deg; I 0.107 A lag 63.4 deg; V_R 5.35 V; V_L 10.7 V; 1.284 VA, 0.572 W, 1.145 VAR, PF 0.45 lagging |
| series LC (Fig.2.170) | 10 VAC, 127,323 Hz | L 100 uH (j80), C 62.5 nF (-j20) | Z j60 ohm; I 0.167 A lag 90 deg; V_L 13.36 V (> source); V_C 3.34 V; PF 0 |
| parallel LC (Fig.2.171) | 10 VAC, 2893.7 Hz | L 2.2 mH (j40), C 5.5 uF (-j10) | Z -j13.33 ohm; I_S 0.750 A; I_L 0.25 A; I_C 1.0 A (> source); 7.50 VA; PF 0 leading |
| series LCR (Fig.2.172) | 1.00 VAC, 1000 Hz | L 25 mH (j157.1), C 1 uF (-j159.2), R 1.0 ohm | Z 2.33 ohm at -64.5 deg; I 0.429 A; V_L 67.40 V; V_C 68.30 V; 0.18 W; VAR_L 28.91, VAR_C 29.30; PF 0.43 leading |
| parallel LCR (Fig.2.173) | 12.0 VAC, 600 Hz | L 1.061 mH (j4), C 66.3 uF (-j4), R 10 ohm | Z 10 ohm (resonant); I_S 1.20 A; I_L = I_C = 3.00 A; 14.4 W; PF 1 |

### T-SCHERZ-2.11 Performance of parallel-resonant circuits (Table 2.11, p.200)

A. High vs low Q

| property | high-Q circuit | low-Q circuit |
|---|---|---|
| selectivity | high | low |
| bandwidth | narrow | wide |
| impedance | high | low |
| line current | low | high |
| circulating current | high | low |

B. Off-resonance, constant L and C

| property | above resonance | below resonance |
|---|---|---|
| inductive reactance | increases | decreases |
| capacitive reactance | decreases | increases |
| circuit resistance | same* | same* |
| circuit impedance | decreases | decreases |
| line current | increases | increases |
| circulating current | decreases | decreases |
| circuit behaviour | capacitive | inductive |

*True near resonance; far from resonance skin effect in the inductor alters resistive losses.

Resonance formulas (§2.30): f0 = 1/(2*pi*sqrt(LC)); Q_U = X/R = (1/R)*sqrt(L/C); BW = f0/Q; V_X ~= Q*V_S (series, Q > 10); R_P = X_L^2/R_S = Q*X_L (parallel dynamic resistance); I_cir ~= Q*I_line (parallel, Q >= 10); Q_LOAD = R_LOAD/X; R_S(cap leakage) = 1/(R_P*(2*pi*f*C)^2).

### T-SCHERZ-2.12 Decibels and power ratios (Table 2.12, p.206)

| dB | P2/P1 | V2/V1 or I2/I1* |
|---|---|---|
| 120 | 1e12 | 1e6 |
| 60 | 1e6 | 1e3 |
| 20 | 1e2 | 10.0 |
| 10 | 10.00 | 3.162 |
| 6.0206 | 4.0000 | 2.0000 |
| 3.0103 | 2.0000 | 1.4142 |
| 1 | 1.259 | 1.122 |
| 0 | 1.000 | 1.000 |
| -1 | 0.7943 | 0.8913 |
| -3.0103 | 0.5000 | 0.7071 |
| -6.0206 | 0.2500 | 0.5000 |
| -10 | 0.1000 | 0.3162 |
| -20 | 1e-2 | 0.1000 |
| -60 | 1e-6 | 1e-3 |
| -120 | 1e-12 | 1e-6 |

*Voltage and current ratios hold only if the impedance remains the same. Human hearing spans ~1e-12 to 1 W/m^2 sound intensity (p.204).

### T-SCHERZ-2.33 First-order filter and attenuator formulas (§2.33, p.210-223)

| network | transfer function | f_c | Z_in (min) | Z_out (max) | loading effect (R' = R//R_L) |
|---|---|---|---|---|---|
| RC low-pass | 1/(1 + j*omega*R*C) | 1/(2*pi*RC) | R + 1/(j*omega*C) (R) | R // 1/(j*omega*C) (R) | gain R'/R, f_c up |
| RL low-pass | 1/(1 + j*omega*L/R) | R/(2*pi*L) | R + j*omega*L (R) | R // j*omega*L (R) | f_c down (R'/L), gain unchanged |
| RC high-pass | j*omega*tau/(1 + j*omega*tau) | 1/(2*pi*RC) | R + 1/(j*omega*C) (R) | R // 1/(j*omega*C) (R) | f_c up |
| RL high-pass | j*omega*L/(R + j*omega*L) | R/(2*pi*L) | R + j*omega*L (R) | R // j*omega*L (R) | gain R'/R, f_c down |
| series RLC bandpass | R/(R + j(omega*L - 1/(omega*C))) | f0 = 1/(2*pi*sqrt(LC)), BW = f0/Q | - | - | use R_T = R//R_LOAD |
| resistive attenuator | R2/(R1+R2) | flat | R1 + R2//R_L | R2//(R1+R_S) | - |
| compensated attenuator | R2/(R1+R2) at all f | flat if R1*C1 = R2*C2 | - | - | - |

### T-SCHERZ-2.34 Transient response summary (§2.34, p.225-235)

| circuit | current | resistor voltage | reactive-element voltage |
|---|---|---|---|
| RC charging | I = (Vs/R)*e^(-t/RC) | V_R = Vs*e^(-t/RC) | V_C = Vs*(1 - e^(-t/RC)) |
| RC discharging | I = (Vs/R)*e^(-t/RC) | V_R = Vs*e^(-t/RC) | V_C = Vs*e^(-t/RC) |
| RL energizing | I = (Vs/R)*(1 - e^(-Rt/L)) | V_R = Vs*(1 - e^(-Rt/L)) | V_L = Vs*e^(-Rt/L) |
| RL deenergizing | I = (Vs/R)*e^(-Rt/L) | V_R = Vs*e^(-Rt/L) | V_L = -Vs*e^(-Rt/L) |
| series RLC, C precharged to V0 | I = V0/((a1 - a2)*L)*(e^(a1 t) - e^(a2 t)), a1,2 = -R/(2L) +/- sqrt(R^2/(4L^2) - 1/(LC)) | - | - |
| RC driven by +/-V0 square wave (steady state, 0 < t < T/2) | - | - | V_C = V0 - 2*V0*e^(-t/RC)/(1 + e^(-T/(2RC))) |

Forced-response rules (p.228): resistor V and I step instantly; capacitor voltage cannot change instantly (acts as a constant-voltage source/short at the switching instant); inductor current cannot change instantly.

Worked transient values (p.226-230): C at 24 V discharging through 10 + 20 ohm -> 0.800 A at t = 0+, 0.573 A after 1 ms (RC = 3 ms), V_R2 = 11.46 V; RL energizing 24 V/8 ohm with 1.3 1/s rate -> 0.99 A at 0.3 s.

### T-SCHERZ-2.35 Fourier facts (§2.35-2.36, p.235-244)

| waveform | series / transform | note |
|---|---|---|
| general periodic | V(t) = a0/2 + sum(a_n cos(n*w0*t) + b_n sin(n*w0*t)); w0 = 2*pi/T | a0/2 = average (dc) |
| square wave +/-V0, 50 % | (4*V0/pi)*sum_{n odd} sin(n*w0*t)/n | half-wave symmetric -> odd harmonics only |
| rectangular pulse V0, width tau | V(w) = 2*V0*sin(w*tau/2)/w | most energy within ~1/tau of zero |
| any linear network | I(w) = V(w)/Z(w) (Eq.2.107), then inverse transform | spectrum analyzer displays abs(V(w)) |

### T-SCHERZ-3.1 Copper wire specifications, bare and enamel-coated, B&S gauge, 20 degC (Table 3.1, p.254-255)

1 mil = 2.54e-5 m. Reduce allowable current 30 % for rubber-insulated wire (p.253).

| AWG | dia (mils) | dia (mm) | ohms/1000 ft | ohms/km | current capacity (A) | nearest British SWG |
|---|---|---|---|---|---|---|
| 1 | 289.3 | 7.35 | 0.1239 | 0.41 | 119.564 | 1 |
| 2 | 257.6 | 6.54 | 0.1563 | 0.51 | 94.797 | 2 |
| 3 | 229.4 | 5.83 | 0.1971 | 0.65 | 75.178 | 4 |
| 4 | 204.3 | 5.19 | 0.2485 | 0.82 | 59.626 | 5 |
| 5 | 181.9 | 4.62 | 0.3134 | 1.03 | 47.268 | 6 |
| 6 | 162.0 | 4.12 | 0.3952 | 1.30 | 37.491 | 7 |
| 7 | 144.3 | 3.67 | 0.4981 | 1.63 | 29.746 | 8 |
| 8 | 128.5 | 3.26 | 0.6281 | 2.06 | 23.589 | 9 |
| 9 | 114.4 | 2.91 | 0.7925 | 2.60 | 18.696 | 11 |
| 10 | 101.9 | 2.59 | 0.9987 | 3.28 | 14.834 | 12 |
| 11 | 90.7 | 2.31 | 1.2610 | 4.13 | 11.752 | 13 |
| 12 | 80.8 | 2.05 | 1.5880 | 5.21 | 9.327 | 13 |
| 13 | 72.0 | 1.83 | 2.0010 | 6.57 | 7.406 | 15 |
| 14 | 64.1 | 1.63 | 2.5240 | 8.29 | 5.870 | 15 |
| 15 | 57.1 | 1.45 | 3.1810 | 10.45 | 4.658 | 16 |
| 16 | 50.8 | 1.29 | 4.0180 | 13.17 | 3.687 | 17 |
| 17 | 45.3 | 1.15 | 5.0540 | 16.61 | 2.932 | 18 |
| 18 | 40.3 | 1.02 | 6.3860 | 20.95 | 2.320 | 19 |
| 19 | 35.9 | 0.91 | 8.0460 | 26.42 | 1.841 | 20 |
| 20 | 32.0 | 0.81 | 10.1280 | 33.31 | 1.463 | 21 |
| 21 | 28.5 | 0.72 | 12.7700 | 42.00 | 1.160 | 22 |
| 22 | 25.3 | 0.64 | 16.2000 | 52.96 | 0.914 | 22 |
| 23 | 22.6 | 0.57 | 20.3000 | 66.79 | 0.730 | 24 |
| 24 | 20.1 | 0.51 | 25.6700 | 84.22 | 0.577 | 24 |
| 25 | 17.9 | 0.46 | 32.3700 | 106.20 | 0.458 | 26 |
| 26 | 15.9 | 0.41 | 41.0200 | 133.90 | 0.361 | 27 |
| 27 | 14.2 | 0.36 | 51.4400 | 168.90 | 0.288 | 28 |
| 28 | 12.6 | 0.32 | 65.3100 | 212.90 | 0.227 | 29 |
| 29 | 11.3 | 0.29 | 81.2100 | 268.50 | 0.182 | 31 |
| 30 | 10.0 | 0.26 | 103.7100 | 338.60 | 0.143 | 33 |
| 31 | 8.9 | 0.23 | 130.9000 | 426.90 | 0.113 | 34 |
| 32 | 8.0 | 0.20 | 162.0000 | 538.30 | 0.091 | 35 |
| 33 | 7.1 | 0.18 | 205.7000 | 678.80 | 0.072 | 36 |
| 34 | 6.3 | 0.16 | 261.3000 | 856.00 | 0.057 | 37 |
| 35 | 5.6 | 0.14 | 330.7000 | 1079.00 | 0.045 | 38 |
| 36 | 5.0 | 0.13 | 414.8000 | 1361.00 | 0.036 | 39 |
| 37 | 4.5 | 0.11 | 512.1000 | 1716.00 | 0.029 | 40 |

Cross-check: Table 2.5's "AWG 8" row carries this table's AWG 9 resistance/current (0.7925 ohm/kft, 18.696 A) - prefer Table 3.1. Magnet wire for coils is typically 22-30 AWG, varnish insulated (p.256).

### T-SCHERZ-3.2 AC/DC resistance ratio vs frequency (Table 3.2, p.263)

| AWG | 1e6 Hz | 1e7 Hz | 1e8 Hz | 1e9 Hz |
|---|---|---|---|---|
| 22 | 6.9 | 21.7 | 68.6 | 217 |
| 18 | 10.9 | 34.5 | 109 | 345 |
| 14 | 17.6 | 55.7 | 176 | 557 |
| 10 | 27.6 | 87.3 | 276 | 873 |

### T-SCHERZ-3.3 Common dielectrics (Table 3.3, p.264)

| material | dielectric constant k |
|---|---|
| Air | 1.0 |
| Pyrex glass | 4.8 |
| Mica | 5.4 |
| Paper | 3.0 |
| Polyethylene | 2.3 |
| Polystyrene | 5.1-5.9 (as printed; out of line with usual polystyrene values - verify against print) |
| Quartz | 3.8 |
| Teflon | 2.1 |

### T-SCHERZ-3.4 Transmission-line constants per foot (Table 3.4, p.265)

| cable | capacitance (pF/ft) | inductance (uH/ft) | Z0 (ohm) |
|---|---|---|---|
| RG-8A/U | 29.5 | 0.083 | 53 |
| RG-11A/U | 20.5 | 0.115 | 75 |
| RG-59A/U | 21.0 | 0.112 | 73 |
| 214-023 | 20.0 | 0.107 | 73 |
| 214-076 | 3.9 | 0.351 | 300 |

(The book's Example 1 assigns 21.0 pF/ft, 0.112 uH/ft -> 73 ohm to RG-11AU, which matches the RG-59A/U row.)

Transmission-line formulas (Fig.3.12): coax Z0 = 138/sqrt(k)*log10(b/a); twin line Z0 = 276/sqrt(k)*log10(D/a); VSWR and reflected power per SCHERZ-1117; quarter-wave Z_sec = sqrt(Z0*Z_L); transformer Np/Ns = sqrt(Z0/Z_L).

### T-SCHERZ-3.5 Primary battery comparison (Table 3.5, p.278; Fig.3.27 p.274)

Internal-resistance, maximum-discharge-rate and cost columns are scrambled in the extraction and are not transcribed; use the chemistry rules (SCHERZ-1123..1126).

| chemistry | common name | nominal cell V | pros/cons | typical applications |
|---|---|---|---|---|
| Carbon-zinc | standard-duty | 1.5 | low cost, many sizes; terminal voltage drops steadily | radios, toys, general-purpose |
| Zinc-chloride | heavy-duty | 1.5 | low cost at higher discharge rates and low temperature; voltage still drops | motor-driven portables, clocks, remote controls |
| Alkaline zinc-manganese dioxide | alkaline | 1.5 | better for high continuous or pulsed loads and low temperature; voltage drops | photoflash, shavers, digital cameras, handheld transceivers, CD players |
| Lithium-manganese dioxide | lithium | 3.0 | high energy density, very low self-discharge, good temperature tolerance | watches, calculators, cameras, DMMs, test instruments |
| Zinc-mercuric oxide | mercury cell | 1.35 | high energy density, very flat discharge, good at higher temperature | calculators, pagers, hearing aids, watches, instruments |
| Zinc-silver oxide | silver oxide cell | 1.5 | very high energy density, very flat discharge, reasonable at low temperature | calculators, pagers, hearing aids, watches, instruments |
| Zinc-oxygen | zinc air cell | 1.45 | high energy density, very light, flat discharge; needs air access | hearing aids, pagers |

Button/coin families (Fig.3.27): lithium 1.55-6 V, dia 0.460-0.965 in, thickness 0.079-0.990 in, 60-250 mAh, IEC CRxxxx/BRxxxx; zinc air 1.15-1.4 V, 70-600 mAh, ZAxxx; mercury 1.35-5.6 V, dia 0.5-0.695 in, thickness 0.135-0.845 in, 80-1000 mAh; silver oxide 1.55-6 V, dia 0.267-0.610 in, thickness printed "0.81-0.210 in", 15-250 mAh, IEC SRxx.

### T-SCHERZ-3.6 Rechargeable battery comparison (Table 3.6, p.284; column alignment reconstructed, medium)

| chemistry | nominal cell V | energy density (Wh/kg) | cycle life | charge time | max discharge rate | cost | pros/cons | applications |
|---|---|---|---|---|---|---|---|---|
| Sealed lead-acid | 2.0 | low (30) | long (shallow cycles) | 8-16 h | medium (0.2 C) | low | low cost, low self-discharge, happy float charging, prefers shallow cycling | emergency lighting, alarms, solar, wheelchairs |
| Rechargeable alkaline-manganese | 1.5 | high (75 initial) | short to medium | 2-6 h (pulsed) | medium (0.3 C) | low | low cost, low self-discharge, no memory, short cycle life | portable lighting, toys, radios, test instruments |
| NiCd | 1.2 | medium (40-60) | long (deep cycles) | 14-16 h (0.1 C) or < 2 h with care (1 C) | high (> 2 C) | medium | prefer deep cycling, good pulse capacity; memory effect, fairly high self-discharge, environmentally unfriendly | portable tools, models, data loggers, camcorders, transceivers |
| NiMH | 1.2 | high (60-80) | medium | 2-4 h | medium (0.2-0.5 C) | medium | very compact; some memory, high self-discharge | RC vehicles, cordless phones, players, power tools |
| NiZn | 1.65 | high (> 170) | medium to high | 1-2 h | - | medium | low cost, green, twice NiCd energy density | power tools, UPS, scooters |
| NiFe | 1.4 | high (> 200) as printed (text calls NiFe energy density low) | extremely long | long | - | low | incredibly long life up to 80 years, environmentally friendly | forklifts and SLA-like uses needing longevity |
| Li-ion/LiPo | 3.6 | very high (> 100) | medium | 3-4 h (1 C - 0.03 C) | med/high (< 1 C) | high | very compact, low maintenance, low self-discharge; needs great care charging | phones, notebooks, cameras |

### T-SCHERZ-3.2.6 Typical battery internal resistance (p.290)

| battery | internal resistance |
|---|---|
| 9 V zinc carbon | 35 ohm |
| 9 V lithium | 16 to 18 ohm |
| 9 V alkaline | 1 to 2 ohm |
| AA alkaline | 0.15 ohm (0.30 ohm at 50 % discharge; ~0.1 ohm quoted p.289; 0.75 ohm at 90 % discharge) |
| AA NiMH | 0.02 ohm (0.04 ohm at 50 % discharge) |
| D alkaline | 0.1 ohm |
| D NiCd | 0.009 ohm |
| D SLA | 0.006 ohm |
| AC13 zinc air | 5 ohm |
| 76 silver | 10 ohm |
| 675 mercury | 10 ohm |

Typical NiMH capacities (p.288): AAA 1000 mAh, AA 2300 mAh, C 5000 mAh, D 8500 mAh, 9 V 250 mAh.
Supercapacitor retention (p.286): organic electrolyte down to 30 % in ~10 h; long-retention types 85 % at 10 days, 65 % at 30 days, 40 % at 60 days.

### T-SCHERZ-3.4 Relay families and coils (§3.4, p.295-297)

| relay type | contact current | switching time | coil (typical) | notes |
|---|---|---|---|---|
| Mechanical (dc coil) | 2-15 A | 10-100 ms | 6 / 12 / 24 V dc ~ 40 / 160 / 650 ohm | many contact forms (SPST...DPDT), latching versions |
| Mechanical (ac coil) | 2-15 A | 10-100 ms | 110 / 240 V ac ~ 3400 / 13,600 ohm | dc coil on ac chatters |
| Miniature | lower-level | - | 5, 6, 9, 12, 24 V dc; 50-3000 ohm | dc actuated, may switch ac |
| Reed | 500 mA-1 A | 0.2-2 ms | 5, 6, 12, 24 V dc; ~250-2000 ohm | dry or mercury-wetted, SPST, surge-sensitive |
| Solid-state | few uA to 100 A | 1-100 ns (as printed) | opto input ~ a couple of mA | ac: zero-cross + triac; dc: MOSFET/IGBT; SPST, surge-sensitive |

Coil drive window: +/-25 % of rated control voltage. Suppression: dc coil - reverse diode (1N4004); ac coil - series RC 100 ohm + 0.05 uF (line-rated C), or bidirectional TVS/MOV.

### T-SCHERZ-3.5 Resistor technologies (compiled from §3.5.4-3.5.5, p.306-319)

| technology | tolerance | TC (ppm/degC) | other limits / notes |
|---|---|---|---|
| Carbon composition | 5-20 % | high | ~70 degC rating, 1/8-2 W; shunt C noticeable ~100 kHz above 0.3 Mohm; survives surges (HV discharge) |
| Carbon film | 1-5 % | negative, ~ -500 to -800 (also quoted 100-200) | noisy, voltage coefficient; good frequency response |
| Metal film | ~1 % (precision 0.1 %, 0.01 %) | 50-100 (precision 20, 10, 5, 2) | best for us rise/MHz; SMD |
| Metal oxide (flameproof) | +/-1 to +/-5 % | ~+/-300 | 0.5-5 W; pulse power, snubbers |
| Thin film (<1 um NiCr) | very tight | low | limited surge |
| Thick film (~12 um RuO2) | good | - | surge 10-100x thin film |
| Precision wirewound | to 0.005 % | as low as 3 | <= 50 kHz; 10,000 h life, 0.10 % drift; max operating 145 degC |
| Power wirewound | 1-5 % | varies | most power/volume; chassis-mount ~5x rating on heat sink |
| Bulk-metal foil | 0.005 % (0.0005 % quoted) | 0.2 | excellent frequency response |
| Chip arrays | 1 %, 5 % | 50-200 | SIP/DIP/SMD |
| Cement | ~5 % | ~300 | 1-20 W+, flame resistant |

Standard power ratings (W): 1/16, 1/10, 1/8, 1/4, 1/2, 1, 2, 5, 10, 15, 25, 50, 100, 200, 250, 300. Voltage-rating examples: 1/2 W and some 1 W: 250-350 V; HV types 1 W (1000 V surge), 2 W (750 V).

Fig.3.55 power-rating multiplier example: enclosure (total) 2.0 x grouping (4 at 2 in) 1.2 x ambient 50 degC 1.1 x others 1 = 2.64.

### T-SCHERZ-3.7 Capacitor comparison (Table 3.7, p.336-339; column alignment reconstructed - medium)

| type | WVDC | capacitance | DA | std tolerance | IR (Mohm*uF) <1 uF / >1 uF | freq. response (1-10) / max f | temp range | DF @1 kHz max | stability 1000 h dC | use |
|---|---|---|---|---|---|---|---|---|---|---|
| Multilayer ceramic NPO | 25-200 V | 1 pF-0.01 uF | 0.6 % | +/-1 % (F), 2 % (G), 5 % (J), 10 % (K) | 1e5 / NA | 9 / 100 MHz | -55 to +125 degC | 0.1 % | 0.1 % | HF decoupling into GHz, HF SMPS; avoid in S/H, integrators |
| Multilayer ceramic stable (X7R class) | 25-200 V | 220 pF-0.47 uF | 2.5 % | +/-5 % (J), 10 % (K), 20 % (M) | 1e5 / 2500 | 8 / 10 MHz | -55 to +125 degC | 2.5 % | 10 % | coupling/dc blocking, supply bypass |
| Multilayer ceramic HiK | 25-100 V | 0.25 pF-22 uF (as printed) | NA | +80/-20 % (Z), +/-20 % (M) | 1e4 / 1e3 | 8 / 10 MHz | +10 to +85 degC and -55 to +85 degC | 4.0 % | 20 % | dc blocking, supply bypass only; use lowest K |
| Ceramic disc (NPO/stable/HiK) | 50-10,000 V | 1 pF-0.1 uF | as multilayer | as multilayer | as multilayer | 8 | -55 to +85 degC | 0.1-4.0 % | as multilayer | coupling/bypass; inductive with long leads |
| Polystyrene | 30-600 V | 100 pF-0.027 uF | 0.05 % | +/-5 % (printed "+/-65 %") | 1e6 | 6 / NA | -55 to +70 degC | 0.1 % | 2 % | filters/timing <= several hundred kHz; coupling/storage |
| Polypropylene film | 100-600 V | 0.001-0.47 uF | 0.05 % | +/-5 % | 1e5 / NA | 6 / NA | see note | see note | see note | coupling, storage, snubbing, timing, noise suppression |
| Metallized polypropylene | 100-1250 V | 47 pF-10 uF | 0.05 % | +/-5 % (J), 10 % (K), 20 % (M) | 1e5 / NA | 6 / NA | see note | see note | see note | SMPS, snubbing, audio, timing |
| Polyester film (Mylar) | 50-600 V | 0.001-10 uF | 0.5 % | +/-10 % | 1e4 / 1e3 | 6 / NA | see note | see note | see note | coupling/storage, audio, oscillators |
| Metallized polyester | 63-1250 V | 470 pF-22 uF | 0.5 % | +/-5/10/20 % | 1e4 / 1e3 | 6 / NA | see note | see note | see note | general purpose, SMPS, bypass, EMI suppression |
| Mica | 50-500 V | 1 pF-0.09 uF | 0.3-0.7 % | +/-1 %, +/-5 % | 1e2 (as printed) | 7 / 100 MHz | -55 to +125 degC | 0.1 % | 0.1 % | resonant circuits, HF filters, HV |
| Multilayer glass | 50-2000 V | 0.5 pF-0.01 uF | 0.05 % | +/-1 %, +/-5 % | 1e5 | 9 | -75 to +200 degC | 0.2 % | 0.5 % | military, RF, S/H, high temperature |
| Aluminium electrolytic | 4-450 V | 0.1 uF-1 F | high | +100/-10 % | NA / 100 | 2 / NA | -40 to +85 degC | 8 % at 120 Hz | 10 % | ripple filters, LF bypass, audio |
| Tantalum electrolytic | 6.3-50 V | 0.01-1000 uF | high | +/-20 % | 1e2 / 10 | 5 / 0.002 MHz (as printed) | -55 to +125 degC | 8-24 % | 10 % | dc blocking, bypass, decoupling, timing at LF |
| Double-layer supercapacitor | 2.3, 5.5, 11 V | 0.022-50 F | - | - | NA | NA | -40 to +70 degC | NA | NA | backup, actuators; not for ripple (high ESR) |

Note: for the four film rows the extraction lists (freq, temp, DF, stability) as {6, -55/+85 degC, 0.35 %, 3 %}, {6, -55/+105 degC, 0.05 %, 2 %}, {6, -55/+125 degC, 2 %, 10 %}, {6, -55/+125 degC, 0.8 %, NA}; row assignment is uncertain - verify in print.

### T-SCHERZ-3.6.8 Ceramic class-2 EIA temperature code (p.336)

| position | code -> meaning |
|---|---|
| 1st (low temp) | X = -55 degC, Y = -30 degC, Z = +10 degC |
| 2nd (high temp) | 5 = +85 degC, 7 = +125 degC |
| 3rd (max dC) | V = +22/-82 %, U = +22/-56 %, T = +22/-33 %, S = +/-22 %, R = +/-15 %, P = +/-10 %, F = +/-7.5 %, E = +/-4.7 % |

NPO/C0G: 0 +/- 30 ppm/degC (others: N030 (SIG), N150 (P2G)). Trimmer colours: yellow 1-5 pF, beige 2-10 pF, brown 6-20 pF, red 10-40 pF, purple 10-60 pF, black 12-100 pF.

### T-SCHERZ-3.8 Inductor characteristics by application (Table 3.8, p.363; alignment medium; * = application dependent)

| application | inductance | max dc current | SRF | Q | dc resistance |
|---|---|---|---|---|---|
| High-frequency (RF), resonance | low | low | very high | very high | low |
| EM coupling | high | * | high | low | very low |
| Filter circuits | high | high | high | low | very low |
| SMPS, dc/dc converters | * | high | medium | low | low |

Inductor tolerance letters: F 1 %, G 2 %, H 3 %, J 5 %, K 10 %, L 15 % (mil 20 %), M 20 %. Saturation spec points: 5 % (incremental), 10 % (ferrite), 20 % (powdered iron). Ferrite antenna rods: mu 800 -> 100 kHz-1 MHz; 125 -> 550 kHz-1.6 MHz; 40 -> ~30 MHz; 20 -> ~150 MHz. Wideband RF chokes: 20-500 ohm over 1.0-400 MHz. Reactance examples (p.360): 1 H at 60 Hz = 377 ohm; 10 uH at 20 MHz = 1257 ohm.

### T-SCHERZ-3.8 Transformer formulas and rectifier sizing (§3.8, p.375-396)

| relation | formula | worked example |
|---|---|---|
| voltage | V_S = V_P*N_S/N_P | 200:1200, 120 VAC -> 720 VAC |
| current | I_P = I_S*N_S/N_P | 180:1260, 0.10 A -> 0.7 A |
| efficiency | P_S = n*P_P (n ~ 0.65-0.99) | 100 W out at 75 % -> 133 W in |
| impedance | Z_P = Z_S*(N_P/N_S)^2 | 500:1000, 2000 ohm -> 500 ohm |
| matching | N_P/N_S = sqrt(Z_P/Z_S) | 500 ohm to 8 ohm -> 7.906 |
| ratio set | 1:3 turns -> V 1:3, I 3:1, Z 1:9 | - |

| rectifier/transformer scheme | secondary V_AC | secondary I_AC | notes |
|---|---|---|---|
| dual complementary (bifilar) | 0.8*(V_DC + 2) | 1.8*I_DC | balanced +/- outputs with common return |
| full-wave bridge | 0.8*(V_DC + 2) | 1.8*I_DC | most efficient use of secondary; best for HV |
| full-wave centre tap | 1.7*(V_DC + 1) | 1.2*I_DC | one diode drop; high current low voltage |
| half-wave | avoid | - | core polarizes and saturates in one direction |

Core vs frequency: laminated silicon steel (power/audio); powdered iron (above mains to several kHz); ferrite (tens of kHz to ~1 MHz; toroids used from a few hundred Hz into UHF). Toroid vs EI: ~95 % efficiency, ~1/2 size and weight, less hum, lower standby loss.

### T-SCHERZ-3.9 Fuse and breaker families (§3.9.1, p.398-399)

| family | size / form | current | voltage | notes |
|---|---|---|---|---|
| glass/ceramic cartridge | 1/4 x 1-1/4 in, 5 x 20 mm | ~1/4-20 A | 32, 125, 250 V | fast or time-lag |
| automotive blade | plastic blade | 3-30 A | 32, 36 V | fast; violet 3, pink 4, tan 5, red 10, blue 15, yellow 20, white 25, green 30 A |
| subminiature | wire leads (PCB) | 0.05-10 A | - | miniature circuits |
| cartridge, ferrule | paper-wrapped | up to 60 A | - | main/subpanel 240 V loads |
| cartridge, knife-blade | paper-wrapped | 60 A and higher | - | - |
| circuit breakers | rocker/push-button | main-line 15-20 A, small to 1 A | - | thermal auto-reset or manual reset |

Fuse rating rule: ~1.5x expected nominal current; time-lag ~1 s for inrush loads.

### T-SCHERZ-4.1 Selection of popular diodes (Table 4.1, p.411)

| device | type | PIV (V) | I_O max | I_R max | I_FSM | V_F max (V) |
|---|---|---|---|---|---|---|
| 1N34A | signal (Ge) | 60 | 8.5 mA | 15 uA (mapping medium) | - | 1.0 |
| 1N67A | signal (Ge) | 100 | 4.0 mA | 5 uA (mapping medium) | - | 1.0 |
| 1N191 | signal (Ge) | 90 | 5.0 mA | - | - | 1.0 |
| 1N914 | fast switch | 90 | 75 mA | 25 nA | see note | 0.8 |
| 1N4148 | signal | 75 | 10 mA | 25 nA | see note | 1.0 |
| 1N4445 | signal | 100 | 100 mA | 50 nA | see note | 1.0 |
| 1N4001 | rectifier | 50 | 1 A | 0.03 mA | 30 A | 1.1 |
| 1N4002 | rectifier | 100 | 1 A | 0.03 mA | 30 A | 1.1 |
| 1N4003 | rectifier | 200 | 1 A | 0.03 mA | 30 A | 1.1 |
| 1N4004 | rectifier | 400 | 1 A | 0.03 mA | 30 A | 1.1 |
| 1N4007 | rectifier | 1000 | 1 A | 0.03 mA | 30 A | 1.1 |
| 1N5002 | rectifier | 200 | 3 A | 500 uA | 200 A | - |
| 1N5006 | rectifier | 600 | 3 A | 500 uA | 200 A | - |
| 1N5008 | rectifier | 1000 | 3 A | 500 uA | 200 A | - |
| 1N5817 | Schottky | 20 | 1 A | 1 mA (mapping medium) | 25 A | 0.75 or 0.90 (see note) |
| 1N5818 | Schottky | 30 | 1 A | - | 25 A | see note |
| 1N5819 | Schottky | 40 | 1 A | - | 25 A | see note |
| 1N5822 | Schottky | 40 | 3 A | - | - | - |
| 1N6263 | Schottky | 70 | 15 mA | - | 50 mA | 0.41 |
| 5052-2823 | Schottky | 8 | 1 mA | 100 nA (mapping medium) | 10 mA | 0.34 |

Note: the extraction lists one I_FSM of 450 mA among the signal diodes and V_F values 0.75 and 0.90 among the 1N581x/1N5822 group without a recoverable row assignment - verify in print.

### T-SCHERZ-4.2 Zener part numbers by voltage (Table 4.2, p.422; axial families)

| V_Z (V) | 500 mW | 1 W | 5 W |
|---|---|---|---|
| 2.4 | 1N5221B | - | - |
| 2.7 | 1N5222B | - | - |
| 3.0 | 1N5225B | - | - |
| 3.3 | 1N5226B | 1N4728A | 1N5333B |
| 3.6 | 1N5227B | 1N4729A | 1N5334B |
| 3.9 | 1N5228B | 1N4730A | 1N5335B |
| 4.3 | 1N5229B | 1N4731A | 1N5336B |
| 4.7 | 1N5230B | 1N4732A | 1N5337B |
| 5.1 | 1N5231B | 1N4733A | 1N5338B |
| 5.6 | 1N5232B | 1N4734A | 1N5339B |
| 6.0 | 1N5233B | - | 1N5340B |
| 6.2 | 1N5234B | 1N4735A | 1N5341B |
| 6.8 | 1N5235B | 1N4736A | 1N5342B |
| 7.5 | 1N5236B | 1N4737A | 1N5343B |
| 8.2 | 1N5237B | 1N4738A | 1N5344B |
| 8.7 | 1N5238B | - | 1N5345B |
| 9.1 | 1N5239B | 1N4739A | 1N5346B |
| 10 | 1N5240B | 1N4740A | 1N5347B |
| 11 | 1N5241B | 1N4741A | 1N5348B |
| 12 | 1N5242B | 1N4742A | 1N5349B |
| 13 | 1N5243B | 1N4743A | 1N5350B |
| 14 | 1N5244B | - | 1N5351B |
| 15 | 1N5245B | 1N4744A | 1N5352B |
| 16 | 1N5246B | 1N4745A | 1N5353B |
| 17 | 1N5247B | - | 1N5354B |
| 18 | 1N5248B | 1N4746A | 1N5355B |
| 19 | 1N5249B | - | 1N5356B |
| 20 | 1N5250B | 1N4747A | 1N5357B |
| 22 | 1N5251B | 1N4748A | 1N5358B |
| 24 | 1N5252B | 1N4749A | 1N5359B |
| 25 | 1N5253B | - | 1N5360B |
| 27 | 1N5254B | 1N4750A | 1N5361B |
| 28 | 1N5255B | - | 1N5362B |
| 30 | 1N5256B | 1N4751A | 1N5363B |
| 33 | 1N5257B | 1N4752A | 1N5364B |
| 36 | 1N5258B | 1N4753A | 1N5365B |
| 39 | 1N5259B | 1N4754A | 1N5366B |
| 43 | 1N5260B | 1N4755A | 1N5367B |
| 47 | 1N5261B | 1N4756A | 1N5368B |
| 51 | 1N5262B | 1N4757A | 1N5369B |
| 56 | 1N5263B | 1N4758A | 1N5370B |
| 60 | 1N5264B | - | 1N5371B |
| 62 | 1N5265B | 1N4759A | 1N5372B |
| 68 | 1N5266B | 1N4760A | 1N5373B |
| 75 | 1N5267B | 1N4761A | 1N5374B |
| 82 | 1N5268B | 1N4762A | 1N5375B |
| 87 | 1N5269B | - | - |
| 91 | 1N5270B | 1N4763A | 1N5377B |
| 100 | 1N5271B | 1N4764A | 1N5378B |

SMD equivalents follow the same numbering: 200 mW BZX84CxVy / MMBZ52xxB, 500 mW BZT52CxVy / ZMM52xxB, 1 W SMAZxx / ZM47xxA.

### T-SCHERZ-4.2.5 Rectifier and multiplier relations (§4.2.5, p.415-417; V_rms = secondary, half-secondary for centre tap)

| circuit | average out (resistive/choke) | peak out (cap filter, light load) | diode PIV | diode current | notes |
|---|---|---|---|---|---|
| half-wave | - | 1.4 V_rms | > 1.4 V_rms; up to 2.8 V_rms with cap | I_load | core polarization with transformer; bias supplies, SMPS |
| full-wave centre tap | 0.9 V_rms | 1.4 V_rms | 2.8 V_rms | I_load/2 | utilization 0.5; one diode drop |
| full-wave bridge | 0.9 V_rms | 1.4 V_rms (minus >= 1.2 V) | > 1.4 V_rms | I_load/2 | utilization 1; two diode drops |
| half-wave doubler | - | 2.8 V_rms (C1 at 1.4, C2 at 2.8) | 2.8 V_rms | - | ripple like half-wave |
| full-wave doubler | - | 2.8 V_rms | 2.8 V_rms | - | C_eff = C1 series C2; surge resistors |
| tripler / quadrupler | - | 3x / 4x V_in,pk | - | - | caps 20-50 uF rated > n*V_in,pk |

### T-SCHERZ-4.3 Transistor and FET formula summary (§4.3, p.429-472)

| device | relation | typical values |
|---|---|---|
| BJT | I_C = h_FE*I_B; I_E = (h_FE+1)*I_B; V_BE = 0.6 V; r_tr = 0.026/I_E | h_FE 10-500 (50-500 spread in a family) |
| Darlington | h_FE = h_FE1*h_FE2; V_BE = 1.2 V | - |
| emitter follower | R_in = h_FE*R_E; R_out = R_S/h_FE; A_V ~ 1 | - |
| common emitter | A_V = -R_C/(r_tr + R_E) (bypassed: r_tr + R3) | V_E ~ 1 V, V_C ~ V_CC/2 |
| JFET | I_D = I_DSS*(1 - V_GS/V_GS,off)^2; g_m0 = 2*I_DSS/abs(V_GS,off) | I_DSS 1 mA-1 A; V_GS,off -0.5..-10 V; R_DS,on 10-1000 ohm; BV_DS 6-50 V; g_m(1 mA) 500-3000 umho |
| depletion MOSFET | same as JFET | same ranges |
| enhancement MOSFET | I_D = k*(V_GS - V_GS,th)^2; g_m = 2*sqrt(k*I_D) | I_D,on 1 mA-1 A; R_DS(on) 1 ohm-10 kohm; V_GS,th 0.5-10 V; BV 6-50 V |
| source follower | A_V = R_S*g_m/(1 + R_S*g_m); Z_out = 1/g_m | - |
| UJT | V_trig = eta*V_B2; f = 1/(R_E*C_E*ln(1/(1-eta))) | eta ~0.5; I_E 50 mA; V_BB 35-55 V; 300-500 mW |

BJT families (p.443): small signal (h_FE 10-500, 80-600 mA, 1-300 MHz); small switching (10-200, 10-1000 mA, 10-2000 MHz); RF (to ~2000 MHz, 10-600 mA); power (10-300 W, 1-100 MHz, 1-100 A).

JFET examples (Table 4.5, p.458): 2N5457 n-ch BV_GS 25 V, I_DSS 1-5 mA, V_GS,off -0.5 to -6 V, g_m 3000 umho, C_iss 7 pF, C_rss 3 pF; 2N5460 p-ch 40 V, 1-5 mA, 1 to 6 V, 3000 umho, 7 pF, 2 pF; 2N5045 matched n-ch pair 50 V, 0.5-8 mA, -0.5 to -4.5 V, 3500 umho, 6 pF, 2 pF.

### T-SCHERZ-4.4 Thyristor examples (Tables 4.7-4.9, p.476-481)

| part | type | key ratings |
|---|---|---|
| 2N6401 | SCR | V_DRM 100 V; I_DRM 2.0 mA; I_RRM 2.0 mA; V_T 1.7 V; I_GT 5.0/30 mA; V_GT 0.7/1.5 V; I_H 6.0/40 mA; P_GM 5 W |
| NTE5600 | triac | I_T,RMS 4.0 A; I_GT 30 mA; V_GT 2.5 V; V_F(on) 2.0 V; I_H 30 mA; I_surge 30 A |
| NTE6411 | diac | V_BO 40 V; I_BO 100 uA; I_pulse 2 A; V_switch 6 V; P_D 250 mW |

Classes: SCR low <= 1 A/100 V, medium <= 10 A/100 V, high to thousands of A/V; SCS 100-300 mA, 100-500 mW, turn-off 1-10 us (SCR 5-30 us); triac low <= 1 A/several hundred V, medium <= 40 A/few thousand V.

### T-SCHERZ-4.10 Transient suppressor comparison (Table 4.10, p.483-484)

| device | application | advantages | disadvantages |
|---|---|---|---|
| bypass capacitor (logic 0.01-0.22 uF; power >= 0.1 uF) | low-power, snubbers, logic rail decoupling | low cost, fast, bipolar | uneven suppression, may fail unpredictably |
| zener diode | low-energy clamping, high-speed data lines | low cost, fast, calibrated clamp | low energy, tends to fail open |
| TVS diode | low-voltage, low-energy, modest frequency | fast (1-5 ns), calibrated low clamp; fails short | high capacitance, low energy, costlier than zener/MOV |
| MOV | most low-moderate frequency circuits, all V/I levels | low cost, bidirectional, more total energy; fails short | moderate-high capacitance (75-20,000 pF), 5-200 ns, wear-out |
| multilayer varistor | 3-70 V systems (3.5-68 V operating), modest frequency | fast (< 1 ns), compact, SMD, many strikes | costlier, high capacitance |
| Surgector | crowbar for moderate-high energy/frequency, data lines | sharp clamp | cost, follow-on current |
| avalanche diode | low-voltage high-speed logic (types to > 4000 V) | sub-ns, ~50 pF | low surge capability, RF noise |
| gas discharge/spark gap | very high energy | up to ~20,000 A, pA leakage | cost, slow |
| PolySwitch | overcurrent (speakers, motors, supplies, packs) | resettable, low cost | needs cool-down to reset |

TVS relations (p.484-485): V_BR ~ 1.1 V_RWM; V_C ~ 1.35-1.4 V_BR ~ 1.6 V_RWM; for ac V_RWM >= 1.4 V_rms. MOV relations (p.487-489): V_M(DC) = 1.4 V_M(AC); energy E = P*t (60 J: 60 W/1 s, 600 W/0.1 s, 6 kW/10 ms, 60 kW/1 ms); W_TM at 10/1000 us.

### T-SCHERZ-4.11 IC packages (Table 4.11, p.493)

| package | long name | pitch (mm) | notes |
|---|---|---|---|
| DIL | dual in-line | 2.54 | 8-40 pins |
| SO/SOIC/SOP | small outline IC | 1.27 | - |
| MSOP/SSOP | mini/shrink small outline | 0.65 | - |
| SOT | small outline transistor | 0.65 | - |
| TQFP | thin quad flat pack | 0.8 | pins on four sides |
| TQFN | thin quad flat no leads | 0.4-0.65 | no pins; pads underneath |

### T-SCHERZ-5.1 LED characteristics (Table 5.1, p.503-504; 5 mm LEDs, V_F at 20 mA)

| wavelength | colour | V_F (V) | intensity | material |
|---|---|---|---|---|
| 940 nm | infrared | 1.5 | 16 mW @ 50 mA | GaAlAs/GaAs |
| 880 nm | infrared | 1.7 | 18 mW @ 50 mA | GaAlAs/GaAs |
| 850 nm | infrared | 1.7 | 26 mW @ 50 mA | GaAlAs/GaAs |
| 660 nm | ultra red | 1.5-1.8 | 200 mcd @ 50 mA | GaAlAs/GaAs |
| 635 nm | high-eff. red | 2.0 | 200 mcd @ 20 mA | GaAsP/GaP |
| 633 nm | super red | 2.2 | 3500 mcd | InGaAlP |
| 620 nm | super orange | 2.2 | 4500 mcd | InGaAlP |
| 612 nm | super orange | 2.2 | 6500 mcd | InGaAlP |
| 605 nm | orange | 2.1 | 160 mcd | GaAsP/GaP |
| 595 nm | super yellow | 2.2 | 5500 mcd | InGaAlP |
| 592 nm | super pure yellow | 2.1 | 7000 mcd | InGaAlP |
| 585 nm | yellow | 2.1 | 100 mcd | GaAsP/GaP |
| 574 nm | super lime yellow | 2.4 | 1000 mcd | InGaAlP |
| 570 nm | super lime green | 2.0 | 1000 mcd | InGaAlP |
| 565 nm | high-efficiency green | 2.1 | 200 mcd | GaP/GaP |
| 560 nm | super pure green | 2.1 | 350 mcd | InGaAlP |
| 555 nm | pure green | 2.1 | 80 mcd | GaP/GaP |
| 525 nm | aqua green | 3.5 | 10,000 mcd | SiC/GaN |
| 505 nm | blue green | 3.5 | 2000 mcd | SiC/GaN |
| 470 nm | super blue | 3.6 | 3000 mcd | SiC/GaN |
| 430 nm | ultra blue | 3.8 (text says 6 V for 430 nm blue) | 100 mcd | SiC/GaN |
| 370-400 nm | UV | 3.9 | NA | GaN |
| 4500 K | "incandescent" white | 3.6 | 2000 mcd | SiC/GaN |
| 6500 K | pale white | 3.6 | 4000 mcd | SiC/GaN |
| 8000 K | cool white | 3.6 | 6000 mcd | SiC/GaN |

Typical other LED ratings (p.504): 100 mW dissipation, -40 to +85 degC, 100 mA pulse, 20-40 nm spectral width. Indicator colours (p.501): green ~565, yellow ~585, orange ~615, red ~650 nm.

### T-SCHERZ-5.x Photodetector and emitter examples (Tables 5.2-5.3, p.516-519; §5.3.5-5.6)

| part/device | key figures |
|---|---|
| NTE3033 IR photodiode | V_R 30 V; dark 50 nA max; light 35 uA min; 100 mW; t_r 50 ns; 65 deg; 900 nm |
| NTE3031 npn phototransistor | BV 30 V (V_CEO); I_C 40 mA; dark 100 nA at 10 V; light 1 mA min; 150 mW; 6 us |
| NTE3036 photodarlington | 50 V; 250 mA; dark 100 nA; light 12 mA min; 250 mW; 151 us |
| silicon solar cell | 0.45-0.5 V open circuit; up to ~0.1 A bright light; ~20 ms response |
| photoresistor (CdS) | MOhm dark to a few hundred ohm lit; ms response, seconds recovery; 400-800 nm |
| laser diode (typical) | 1-5 mW (visible 3-5 mW); CD 780 nm up to 5 mW chip / 0.3-1 mW at disc; RW ~30 mW; arrays >= 100 W; ~1 nm linewidth; divergence e.g. 10 x 30 deg |
| single-mode fibre | core 8-10.5 um; cladding 125 um; ~50 Gb/s over hundreds of miles |

### T-SCHERZ-6.1 Temperature sensors (Table 6.1, p.535; accuracy without individual calibration)

| sensor | typical range (degC) | accuracy (+/- degC) | pros | cons | applications |
|---|---|---|---|---|---|
| thermistor | -40 to 125 | 1 | low cost | nonlinear | ambient temperature |
| thermocouple | -200 to 1350 | 3 | low cost, wide range | lead is part of the sensor; measures a difference (needs CJC) | industrial, furnaces |
| RTD | -260 to 800 | 1 | accurate, good linearity | expensive, slow response | - |
| analog IC (TMP36) | -40 to 125 | 2 | simple to interface | costlier than thermistor | thermostats, digital thermometers |
| digital IC (DS18B20) | -55 to 125 | 0.5 | simple with MCUs, accurate | costlier than thermistor | thermostats, remote sensing |
| IR thermometer (MLX90614 / MLX90616) | -70 to 380 / up to 1030 | 0.5 | no contact | costlier than contact sensors | medical, industrial |

Relations: Beta model R = R0*exp(beta*(1/T - 1/T0)); Pt RTD R = 100*(1 + 0.003925*T) ohm; TMP36 T = 100*V_out - 50; chromel-alumel 41 uV/degC; Stefan-Boltzmann j* = 5.6704e-8*T^4.

### T-SCHERZ-6.2 Distance, rotation and pressure sensors (Tables 6.2, 6.3, 6.5, p.540-545)

| sensor | range | accuracy | notes |
|---|---|---|---|
| ultrasonic | 150 mm-6 m | 25 mm | v = 331 m/s (0 degC) to 346 m/s (25 degC); d = v*t/2 |
| optical reflective | 100-800 mm | 10 mm | ambiguous below ~5 cm; reflectivity dependent |
| optical slotted | presence only | - | low cost |
| capacitive | 0-30 cm | - | conductive, earthed objects only |
| potentiometer (rotation) | ~300 deg (end stops) | 2-5 deg | absolute angle |
| quadrature encoder, low cost | continuous | 30 deg (~12 PPR) | relative |
| quadrature encoder, optical | continuous | 2 deg (up to 200 PPR, 30,000 rpm) | relative, high speed |
| absolute encoder (4-bit) | continuous | 22 deg | Gray code |
| MPX2010 pressure | 0-10 kPa differential | - | temperature compensated, factory calibrated |
| KP125 pressure | 40-115 kPa absolute | 1.2 kPa | altimeter, barometer |

### T-SCHERZ-7.1 Shock, ESD and measurement reference data (§7.1-7.4, p.551-590)

| item | value |
|---|---|
| 50-60 Hz body current, hand to foot | 10 mA tingle; >10 mA may freeze; 20-100 mA may be fatal; 100 mA-1 A deadliest; >1 A single heart contraction |
| GFCI trip | ~5-10 mA |
| body resistance | ~1 Mohm dry callused palm; ~100 ohm thin wet palm; 70-100 ohm across chest |
| hazardous sources | microwave oven >= 5000 V, > 1 A momentary; CRT 35 kV |
| capacitor discharge resistor | 100-500 ohm per volt, >= 2 W |
| static voltages | carpet ~1000 V; polyethylene bag >= 300 V; combing hair up to 2500 V |
| meter internal resistance (analog) | ammeter ~2 kohm; voltmeter ~100 kohm; ohmmeter ~50 ohm |
| meter loading rule | R_V >= 20*R_TH, R_A <= R_TH/20 -> error < 5 % |
| scope CAL output | 1 kHz, 0.1 Vpp square wave |
| trigger coupling | AC 10 Hz->35 MHz; DC dc->35 MHz; LF REJ <10 kHz attenuated; HF REJ >100 kHz attenuated |
| scope current shunt | 1 ohm precision, P >= 2*R*I_max^2 |
| breadboard | 0.100 in pitch; 22 AWG; 0.38-0.81 mm wire |
| wire-wrap | 30/28/26 AWG; ~7 turns |
| PCB soldering iron | 25-40 W |

### T-SCHERZ-7.1b Gerber file set (Table 7.1, p.566)

| file | contents |
|---|---|
| .GTL | top copper |
| .GBL | bottom copper |
| .GTS | solder stop mask, top |
| .GBS | solder stop mask, bottom |
| .GTO | silkscreen, top |
| .GBO | silkscreen, bottom |
| .TXT | drill |

## 3. Mechanizable checks

`CHECK-power-derating`: inputs per part (P_diss_max W, P_rated W) -> ratio = P_rated/P_diss_max -> pass if ratio >= 2 (book: "two to three or more times") -> margin = ratio/2 - 1 -> SCHERZ-1007.

`CHECK-wire-ampacity`: inputs per conductor (AWG, I_max A) -> I_cap = Table 2.5 current capacity(AWG) -> pass if I_cap >= I_max -> margin = I_cap/I_max - 1 -> SCHERZ-1008, SCHERZ-1010.

`CHECK-wire-drop`: inputs (AWG, one-way length ft, I A, V_supply V, allowed drop %) -> R = ohms_per_1000ft(AWG)/1000 * 2 * length -> V_drop = I*R -> pass if V_drop/V_supply <= allowed % -> margin = allowed - actual -> SCHERZ-1009 (Table 2.5).

`CHECK-conductor-resistance`: inputs (material, length m, cross-section m^2, T degC) -> R = rho(T0)*(1+alpha*(T-25))*L/A using Table 2.2 -> report R and I^2*R loss at I_max -> SCHERZ-1003, SCHERZ-1004.

`CHECK-thermal-stack`: inputs (P W, footprint area, list of layers {material lambda, thickness}, T_reference degC, T_max_rated degC) -> T_hot = T_ref + P*sum(lambda_i*t_i)/A -> pass if T_hot <= T_max_rated -> margin = T_max_rated - T_hot (degC) -> SCHERZ-1005, SCHERZ-1006, Table 2.4.

`CHECK-air-gap-breakdown`: inputs (gap mm, peak voltage V, electrode shape) -> V_bd = 3 kV/mm * gap for plane electrodes; flag sharp-point electrodes (breakdown only a few kV) -> pass if V_peak < V_bd -> SCHERZ-1012 (coarse physics bound, not a safety-standard clearance).

`CHECK-resistor-power`: inputs per resistor (R ohm, V_across V or I A, P_rated W) -> P = V^2/R or I^2*R (use V_rms for ac) -> pass if P_rated >= 2*P -> margin = P_rated/(2*P) - 1 -> SCHERZ-1023, SCHERZ-1035, SCHERZ-1007.

`CHECK-resistor-voltage-limit`: inputs (R, P_rated, V_applied) -> V_max = sqrt(P_rated*R) -> pass if V_applied <= V_max (and <= element voltage rating when given) -> SCHERZ-1024.

`CHECK-divider-loading`: inputs (Vin, R1, R2, R_load or I_load, V_target, tolerance %) -> V_out = Vin*(R2//R_load)/(R1 + R2//R_load); bleeder ratio = (V_out/R2)/I_load -> pass if |V_out - V_target|/V_target <= tolerance AND bleeder ratio >= 0.1 -> SCHERZ-1025, SCHERZ-1026, SCHERZ-1027.

`CHECK-source-droop`: inputs (Vs, rs, R_load) -> V_T = Vs*R_load/(R_load+rs) -> pass if R_load/rs >= 1000 (negligible) else report droop % -> SCHERZ-1029.

`CHECK-ac-peak-vs-rating`: inputs (V_dc, V_ac_rms or V_ac_pk, V_rated_dcwv) -> V_pk = V_dc + sqrt(2)*V_ac_rms -> pass if V_pk <= dcwv -> margin = dcwv/V_pk - 1 -> SCHERZ-1034, SCHERZ-1041.

`CHECK-electrolytic-bias`: inputs (V_dc, V_ac_pk, dcwv, polarity marking) -> pass if V_dc - V_ac_pk >= 0 (no reversal; medium, inferred from polarity requirement) AND V_dc + V_ac_pk <= dcwv -> SCHERZ-1040.

`CHECK-cap-constant-current`: inputs (I A, t_max s, C F, V_rated) -> V = I*t_max/C -> pass if V <= V_rated -> SCHERZ-1044.

`CHECK-cap-inrush`: inputs (V_step, R_source, ESR, I_limit of source/switch/fuse) -> I_peak = V_step/(R_source + ESR) -> pass if I_peak <= I_limit -> SCHERZ-1045.

`CHECK-rc-timing`: inputs (R, C, Vs, V_threshold, t_required, R_tol %, C_tol %) -> t = -R*C*ln((Vs - V_th)/Vs) evaluated at tolerance corners -> pass if [t_min, t_max] within spec window -> SCHERZ-1049.

`CHECK-bleeder-discharge`: inputs (C, R_bleed, V_bus, t_safe_required) -> t5 = 5*R_bleed*C; P_bleed = V_bus^2/R_bleed -> pass if t5 <= t_safe_required AND bleeder P_rated >= 2*P_bleed -> SCHERZ-1050, SCHERZ-1023.

`CHECK-parallel-cap-rating`: inputs (list of parallel caps with V_rated, node V_peak) -> pass if min(V_rated) >= V_peak -> SCHERZ-1051.

`CHECK-series-cap-balance`: inputs (C_i, V_rated_i, V_in, R_eq_i optional) -> V_i = V_in*C_tot/C_i (or by R_eq division when equalizers fitted) -> pass if all V_i <= V_rated_i; if no equalizers, flag; recommend R_eq ~ 100 ohm/V * V_in with P = V_i^2/R_eq derated 2x -> SCHERZ-1052, SCHERZ-1053.

`CHECK-inductor-saturation`: inputs (I_dc, ripple current dI_pp, I_sat datasheet) -> I_peak = I_dc + dI_pp/2 at worst-case load -> pass if I_peak < I_sat -> margin = I_sat/I_peak - 1 -> SCHERZ-1063.

`CHECK-inductive-kick`: inputs (L, I_on, switch turn-off time t_off, switch V_max, clamp present?) -> V_kick = L*I_on/t_off -> pass if clamp present OR V_supply + V_kick <= V_max of switch -> SCHERZ-1067.

`CHECK-toroid-turns`: inputs (L_target, AL, core family) -> N from Fig.2.133 formula, rounded up -> report N and achieved L -> SCHERZ-1066.

`CHECK-coil-wheeler`: inputs (d in, l in, N) -> L(uH) = d^2*N^2/(18d+40l) -> compare to target within tolerance -> SCHERZ-1061.

`CHECK-core-frequency`: inputs (core type, f_operating) -> pass if f_operating <= limit (laminated iron ~15 kHz; Table 2.7 frequency limits) -> SCHERZ-1065.

`CHECK-flyback-clamp`: inputs (netlist: every inductive load - relay coil, solenoid, motor, transformer primary - and its switching element) -> pass if a flyback diode, snubber or TVS is connected across the coil or the switch -> SCHERZ-1071, SCHERZ-1072, SCHERZ-1067.

`CHECK-ac-power-factor`: inputs (V_rms, I_rms, phi or R and X) -> VA = V*I, P = I^2*R, VAR = I^2*X, PF = P/VA with sign -> report; pass if source/inverter PF limits (with sign) are met -> SCHERZ-1084, SCHERZ-1085.

`CHECK-transformer-va`: inputs (transformer VA rating, secondary V_rms, load I_rms incl. reactive) -> VA_load = V_rms*I_rms -> pass if VA_rating >= VA_load (apply SCHERZ-1007 2x margin for dissipation-limited parts) -> SCHERZ-1086.

`CHECK-resonant-stress`: inputs (L, C, R, source V_rms, f range) -> I = V/abs(Z), V_L = I*omega*L, V_C = I/(omega*C) across the f range -> pass if max V_C <= C rating/sqrt(2) (peak basis) and I <= inductor rating -> SCHERZ-1087, SCHERZ-1034.

`CHECK-lead-inductance`: inputs (lead/trace length b in, radius a in, f_max, circuit impedance Z_ckt) -> L = 0.00508*b*(ln(2b/a)-0.75) uH; X = 2*pi*f_max*L -> flag if X > 10 % of Z_ckt (threshold is an Anvil choice, low) -> SCHERZ-1074.

`CHECK-pulse-settling`: inputs (tau = RC or L/R, f_pulse) -> pass if 5*tau <= 1/(2*f) -> SCHERZ-1073.

`CHECK-resonant-tank`: inputs (L, C, R_S coil, R_leak cap, R_load, f) -> f0, X = 2*pi*f0*L, R_S_total = R_S + 1/(R_leak*(2*pi*f0*C)^2), Q_U = X/R_S_total, R_P = Q_U*X, Q_L = (R_P//R_load)/X, BW = f0/Q_L -> pass if f0 and BW within spec -> SCHERZ-1088..1096.

`CHECK-tank-component-stress`: inputs (Q, V_S, I_line, component ratings) -> series: V_X = Q*V_S (Q > 10); parallel: I_cir = Q*I_line -> pass if V_X*sqrt(2) <= cap/inductor voltage rating and I_cir <= current rating -> SCHERZ-1091, SCHERZ-1094.

`CHECK-impedance-bridging`: inputs per interface (Z_out source, Z_in load, over the band) -> ratio = Z_in/Z_out -> pass if ratio >= 10 at all frequencies of interest -> margin = ratio/10 - 1 -> SCHERZ-1098.

`CHECK-filter-loading`: inputs (R, C or L, R_L, target f_c, tolerance) -> R' = R//R_L; f_c_loaded; gain = R'/R -> pass if |f_c_loaded - target| within tolerance and gain loss acceptable; warn if R_L < 10*R -> SCHERZ-1100, SCHERZ-1101.

`CHECK-compensated-divider`: inputs (R1, C1, R2, C2, tolerance %) -> pass if |R1*C1 - R2*C2|/(R2*C2) <= tolerance -> SCHERZ-1104.

`CHECK-db-consistency`: inputs (gain spec in dB, V ratios, impedances) -> flag any 20*log voltage ratio used across different impedances -> SCHERZ-1097.

`CHECK-rlc-damping`: inputs (R, L, C, overshoot allowed?) -> R_crit = 2*sqrt(L/C); zeta = R/R_crit -> classify over/critical/under; pass if zeta >= 1 where no ringing is allowed (or zeta >= spec) -> SCHERZ-1106.

`CHECK-clock-harmonics`: inputs (V0, f0, duty, rise time or pulse width tau, f_limit of concern) -> odd-harmonic amplitudes 4*V0/(n*pi) for 50 % duty; flag even harmonics when duty != 50 %; energy bandwidth ~1/tau -> report harmonics falling in regulated/sensitive bands -> SCHERZ-1107.

`CHECK-wire-derate-insulation`: inputs (AWG, insulation type, I) -> I_allow = Table 3.1 value * (0.7 if rubber-insulated) -> pass if I <= I_allow -> SCHERZ-1109.

`CHECK-wire-ampacity-t31`: inputs (AWG, I_max A, insulation) -> I_cap from Table 3.1 x 0.7 if rubber -> pass if I_cap >= I_max -> SCHERZ-1110, SCHERZ-1109.

`CHECK-skin-effect`: inputs (AWG in {22,18,14,10}, f, R_dc) -> R_ac = R_dc*ratio interpolated log-log from Table 3.2 -> report I^2*R_ac loss -> SCHERZ-1114.

`CHECK-line-z0`: inputs (geometry a, b or D, k; or L', C') -> Z0 per SCHERZ-1115/1116 -> pass if |Z0 - Z_target|/Z_target <= tolerance -> SCHERZ-1115, SCHERZ-1116.

`CHECK-vswr`: inputs (Z0, R_L) -> VSWR = max(Z0/R_L, R_L/Z0); P_refl % = ((VSWR-1)/(VSWR+1))^2*100 -> pass if VSWR <= spec (e.g. 1.5 or 2, spec-defined) -> SCHERZ-1117.

`CHECK-needs-matching`: inputs (f_max, cable length l, k) -> lambda = c/(sqrt(k)*f_max) -> flag "matching required" when l > lambda/10 (the /10 threshold is an Anvil choice; the book says "much larger", low) -> SCHERZ-1118.

`CHECK-battery-runtime`: inputs (capacity mAh, I_avg mA, I_peak, derating from discharge curve or Peukert exponent) -> t = capacity_eff/I_avg -> pass if t >= required runtime -> SCHERZ-1136, SCHERZ-1137.

`CHECK-battery-droop`: inputs (V_oc per cell, n_series, R_in end-of-life per cell, I_peak, V_min of load) -> V_load = n*V_oc - I_peak*n*R_in -> pass if V_load >= V_min -> SCHERZ-1138.

`CHECK-cell-substitution`: inputs (design cell count n, load V_min, chemistry) -> end-of-discharge V = n*1.0 V (NiCd/NiMH: most energy above 1.0 V/cell) vs alkaline design -> pass if n*1.0 >= V_min -> SCHERZ-1128, SCHERZ-1129 (medium).

`CHECK-liion-charger`: inputs (charger CV setpoint per cell, termination current fraction, thermal cutoff, float/trickle enabled?, pack protection present?) -> pass if setpoint <= 4.30 V/cell protection threshold, termination ~0.03*I_chg, thermal disconnect <= 90 degC, no trickle/float, protection circuit present -> SCHERZ-1130.

`CHECK-supercap-bank`: inputs (C per cell, V_cell_rated, n_series, V_max, V_cut, balancing present?) -> usable fraction = (V_max - V_cut)/V_max (constant current); energy = 0.5*C_bank*(V_max^2 - V_cut^2) -> pass if energy >= hold-up requirement AND (n_series <= 3 OR balancing present) -> SCHERZ-1134 (energy formula from SCHERZ-1048).

`CHECK-relay-coil-window`: inputs (V_drive min/max, V_coil_rated) -> pass if 0.75*V_rated <= V_drive <= 1.25*V_rated at all supply corners -> SCHERZ-1141.

`CHECK-relay-suppression`: inputs (coil type ac/dc, suppression part, I_coil = V/R_coil, diode I_FSM/I_F) -> dc: pass if reverse diode present with peak current rating >= I_coil; ac: pass if RC (or TVS/MOV) present with C rated for line voltage -> SCHERZ-1143.

`CHECK-resistor-voltage-critical`: inputs (R, P_rated, V_rated, V_applied incl. surges) -> R_crit = V_rated^2/P_rated; limit = sqrt(P_rated*R) if R < R_crit else V_rated -> pass if V_applied <= limit -> SCHERZ-1147.

`CHECK-resistor-ambient-derate`: inputs (P_diss, P_rated, T_ambient, T_full_load, T_zero_load) -> P_allow = P_rated if T <= T_full else P_rated*(T_zero - T)/(T_zero - T_full) -> pass if P_allow >= 2*P_diss (book: 2-4x) -> SCHERZ-1149, SCHERZ-1150.

`CHECK-resistor-group-factor`: inputs (P per resistor, enclosure, grouping, cooling, ambient, altitude, pulse factors) -> P_free_air_required = P*prod(F) -> pass if P_rated >= P_free_air_required -> SCHERZ-1150.

`CHECK-resistor-drift-budget`: inputs (tolerance, TC, dT_self + dT_amb, load-life drift) -> dR_total = tol + TC*dT*1e-6 + drift -> pass if within circuit error budget; flag carbon comp/carbon film in precision nets -> SCHERZ-1148, SCHERZ-1151, SCHERZ-1158.

`CHECK-johnson-noise`: inputs (R, T K, bandwidth Hz, signal level) -> V_n = sqrt(4*1.38e-23*T*R*B) -> pass if SNR >= spec -> SCHERZ-1153.

`CHECK-pot-wiper`: inputs (pot R, configuration, min setting fraction, applied V) -> I_wiper = V/(R*fraction); P_element = V^2/(R*fraction) -> pass if I_wiper <= wiper rating and P_element <= P_rated*fraction -> SCHERZ-1164.

`CHECK-cap-ripple-current`: inputs (I_rms at f, ESR or DF, I_rms rating at f) -> P = I_rms^2*ESR -> pass if I_rms <= rating -> SCHERZ-1168.

`CHECK-cap-class2-worstcase`: inputs (C_nom, tolerance, dielectric code, T range, dc bias derating from datasheet) -> C_min = C_nom*(1 - tol)*(1 - dC_code) -> pass if C_min >= C_required -> SCHERZ-1171.

`CHECK-hold-cap-droop`: inputs (C, type, hold time t, allowed droop dV) -> I_leak = (5..20 nA/uF)*C for electrolytics or V/(IR/C) for film -> dV = I_leak*t/C -> pass if dV <= allowed; fail any electrolytic or ceramic (DA) in S/H -> SCHERZ-1167, SCHERZ-1170.

`CHECK-decoupling-count`: inputs (IC list with type digital/analog and rails, capacitor list with net and value) -> pass if each digital IC has >= 1 x 0.1 uF ceramic, each analog IC >= 1 per rail (2 total), and >= 1 x 1 uF per 8 ICs -> SCHERZ-1179.

`CHECK-decoupling-placement`: inputs (capacitor-to-pin distance, lead/via length, shared bulk-cap distance) -> pass if lead/connection length < 1.5 mm and shared 1 uF within 10 cm of each served IC -> SCHERZ-1180, SCHERZ-1181.

`CHECK-bypass-impedance`: inputs (C, ESL, f_noise, Z_in of stage) -> X = |1/(2*pi*f*C) - 2*pi*f*ESL| -> pass if X <= 0.1*Z_in and f_noise < SRF -> SCHERZ-1177, SCHERZ-1169.

`CHECK-contact-snubber`: inputs (I_load, V_supply, R_load, snubber R and C, C voltage rating) -> dV/dt = I_load/C -> pass if dV/dt <= 1 V/us (C[uF] >= I_load[A], derived), R <= R_load, peak contact V < 300 V and C rating >= peak -> SCHERZ-1184.

`CHECK-ripple-factor`: inputs (V_dc, V_ripple_rms) -> RF = V_r,rms/V_dc -> pass if RF <= 0.05 (or spec) -> SCHERZ-1183.

`CHECK-inductor-isat-point`: inputs (I_peak, datasheet I_sat with its % drop, core material) -> pass if I_peak <= I_sat(10 % drop) for ferrite or I_sat(20 %) for powdered iron, and I_rms <= I_DC -> SCHERZ-1187.

`CHECK-transformer-ratio`: inputs (V_P, N_P, N_S or ratio, load I_S, efficiency n, VA rating) -> V_S = V_P*N_S/N_P; I_P = I_S*(N_S/N_P)/n; VA = V_S*I_S -> pass if VA <= VA_rated and winding voltages within ratings -> SCHERZ-1193, SCHERZ-1194.

`CHECK-transformer-operating-limits`: inputs (applied V per winding, dc current per winding, f) -> pass if V <= rated, dc current ~0 unless winding rated, f within datasheet range (flag 50/60 Hz parts below rated f) -> SCHERZ-1196.

`CHECK-rectifier-secondary`: inputs (topology, V_DC, I_DC, transformer V_AC, I_AC ratings) -> required V_AC, I_AC per T-SCHERZ-3.8 -> pass if transformer rating >= required; fail half-wave with transformer -> SCHERZ-1203.

`CHECK-fuse-rating`: inputs (I_nominal, inrush profile, fuse rating, fuse type, fuse voltage rating, circuit voltage, position hot/neutral) -> pass if 1.4*I_nom <= I_fuse <= fault-clearing limit (target ~1.5x), time-lag where inrush present, V_fuse >= circuit V, fuse in hot line upstream -> SCHERZ-1206, SCHERZ-1207, SCHERZ-1208, SCHERZ-1033.

`CHECK-bench-isolation`: inputs (equipment grounded?, input isolation?, bench chain order) -> pass if non-isolated/hot-chassis equipment is fed through an isolation transformer placed upstream of any Variac -> SCHERZ-1199, SCHERZ-1200.

`CHECK-diode-piv-topology`: inputs (topology, V_rms secondary, filter type, diode PIV, margin) -> required PIV = 2.8*V_rms (half-wave with cap, centre tap, doublers) or 1.4*V_rms (bridge) -> pass if PIV_rated >= required*margin -> SCHERZ-1216..1219.

`CHECK-diode-current-derate`: inputs (I_F avg, I_F peak/surge at turn-on, I_O(max), I_FSM) -> pass if I_F,avg <= 0.75*I_O(max) and turn-on surge <= I_FSM -> SCHERZ-1211, Table 4.1.

`CHECK-zener-regulator`: inputs (V_in min/max, V_Z, I_Z,min, I_L min/max, R_S, P ratings) -> R_S,max = (V_in,min - V_Z)/(I_Z,min + I_L,max); P_R = (V_in,max - V_Z)^2/R_S; P_Z = V_Z*(V_in,max - V_Z)/R_S -> pass if R_S <= R_S,max and ratings >= 2x computed (SCHERZ-1007) -> SCHERZ-1223.

`CHECK-bjt-bias-hfe-independent`: inputs (R1, R2, R_E, h_FE,min) -> pass if R1//R2 <= 0.1*h_FE,min*R_E (divider stiff at minimum gain) and V_E >= ~1 V where temperature stability is needed -> SCHERZ-1230, SCHERZ-1234, SCHERZ-1235.

`CHECK-bjt-switch-drive`: inputs (I_C load, h_FE,min, V_drive, R_B) -> I_B = (V_drive - 0.6)/R_B -> pass if h_FE,min*I_B >= I_C (overdrive factor is an Anvil choice; book gives the active-region relation only) -> SCHERZ-1232, SCHERZ-1230.

`CHECK-bjt-abs-max`: inputs (worst-case I_C, V_CE, V_CB, V_EB, P_D vs datasheet) -> pass if all below ratings; require protection diodes where V_EB reverse or inductive loads exist -> SCHERZ-1238.

`CHECK-tvs-selection`: inputs (V_op,dc or V_rms, V_damage of protected node, I_transient, line data rate/C budget, TVS V_RWM, V_BR, V_C@I_PP, I_PP, C_J) -> pass if V_RWM >= V_op (1.4*V_rms for ac), V_C < V_damage, I_PP >= I_transient, C_J within budget -> SCHERZ-1253.

`CHECK-mov-selection`: inputs (V_line,rms max, surge energy J, peak current, MOV V_M(AC), W_TM, I_PK, fuse present) -> pass if V_M(AC) >= V_line,rms,max, W_TM >= energy, I_PK >= peak current and a series fuse is present -> SCHERZ-1254.

`CHECK-scr-triac-gate-drive`: inputs (gate drive current/voltage at worst temperature, I_GT,max, V_GT,max, load current, I_H) -> pass if drive >= I_GT,max and V_GT,max, and minimum load current > I_H when latching is required -> SCHERZ-1247, SCHERZ-1249.

`CHECK-hand-solder-pitch`: inputs (package pitch, assembly method) -> flag pitch <= 0.5 mm for hand assembly -> SCHERZ-1257.

`CHECK-led-string`: inputs (V_supply min/max, LED V_F per string, n in series, I_target, R_S, R_S power rating, topology) -> I = (V_supply - n*V_F)/R_S at corners; P_R = I^2*R_S -> pass if I <= I_rating, P_rated >= 2*P_R (SCHERZ-1007), n*V_F <= 0.8*V_supply,min and every parallel branch has its own resistor -> SCHERZ-1258, SCHERZ-1261.

`CHECK-led-thermal`: inputs (I_F, V_F, heat sink present?) -> P = I_F*V_F -> pass if P <= ~100 mW for standard LEDs, else a heat sink is required (high-power LEDs) -> SCHERZ-1259, SCHERZ-1260.

`CHECK-capacitive-dropper`: inputs (line V_rms, f, C, R_series, C voltage rating, C polarized?) -> X_C = 1/(2*pi*f*C); I ~ V/X_C; inrush = V_pk/R_series -> pass if C nonpolarized and rated >= 200 V (120 V line), inrush <= ~150 mA, LED current within rating -> SCHERZ-1262.

`CHECK-laser-driver`: inputs (driver type ACC/APC, absolute current limit present?, soft-start?, switch/relay in LD path?, heat sink?) -> pass if an absolute current limit and soft start exist, no switch/relay in the laser path and a heat sink is fitted -> SCHERZ-1265, SCHERZ-1266.

`CHECK-thermistor-divider`: inputs (R0, beta, T0, R1, V_in, ADC bits, T range) -> V_out(T) = V_in*R1/(R1 + R0*exp(beta*(1/T - 1/T0))); counts/degC = dV_out/dT * 2^bits/V_ref -> pass if resolution meets requirement across range -> SCHERZ-1277, SCHERZ-1274.

`CHECK-ultrasonic-temp-error`: inputs (T range, assumed v) -> error = |v(T)/v_assumed - 1| using 331 m/s at 0 degC and 346 m/s at 25 degC (linear, derived) -> pass if within accuracy spec or temperature compensation present -> SCHERZ-1283.

`CHECK-sensor-calibration-plan`: inputs (unit cost class, sensor factory-calibrated?, per-unit calibration step?) -> flag per-unit calibration on low-cost volume products and uncalibrated sensors on precision products -> SCHERZ-1275.

`CHECK-meter-loading`: inputs (meter type and internal resistance, circuit Thevenin resistance) -> pass if R_V >= 20*R_TH (voltage) or R_A <= R_TH/20 (current) -> SCHERZ-1307, SCHERZ-1031.

`CHECK-scope-shunt`: inputs (R_shunt, I_max, P_rating) -> pass if P_rating >= 2*R_shunt*I_max^2 -> SCHERZ-1308.

`CHECK-cap-discharge-tool`: inputs (V_cap, discharge resistor R, P rating) -> pass if 100*V_cap <= R <= 500*V_cap and P >= 2 W (and >= V^2/R peak consideration) -> SCHERZ-1294.

`CHECK-schematic-hygiene`: inputs (netlist/BOM) -> pass if every part has a designator and value, power-handling parts have power ratings, polarized parts show polarity, title block has name/designer/date/revision, and ERC reports no unconnected pins -> SCHERZ-1299.

`CHECK-board-edge-keepout`: inputs (component courtyards, board outline) -> pass if all parts are >= 2 mm from the edge (except edge connectors) and I/O/power connectors sit on an edge -> SCHERZ-1302.

`CHECK-enclosure-bonding`: inputs (enclosure material, PE bond present, grommet/strain relief at cord entry) -> pass if metal enclosures are bonded to the power-cord ground and cord entries have grommet + strain relief -> SCHERZ-1296, SCHERZ-1305, SCHERZ-1017.

## 4. Verification procedures & plots

- Common-ground verification (§2.10.1 p.43): with all instruments plugged into grounded outlets, measure resistance between the ground terminals of any two instruments; a properly grounded setup reads ~0 ohm (slightly more for internal resistance).
- Black-box power (§2.7 p.31-33): measure V across and I into the device (voltmeter + ammeter, or wattmeter) -> P = V*I; heat equals P only if the device is purely resistive.
- Thevenin/Norton characterization (§2.19 p.76-78): measure open-circuit voltage (V_TH) and short-circuit current (I_N) at the port, or R_TH with sources replaced by shorts; R_TH = V_TH/I_N. Good: loaded voltage matches V_TH*R_L/(R_TH+R_L).
- Supply set-point (§2.13 p.64): adjust bench supply voltage with the load connected; recheck after adding/removing components.
- Meter-loading check (§2.14 p.66): compare circuit node resistance to the meter's input resistance before trusting a reading; error rises as they approach each other.
- RMS measurement (§2.21 p.91-92): use a true-RMS meter for non-sinusoidal waveforms; for a sine, cross-check against peak/average readings via Fig.2.89 factors.
- Capacitor charge/discharge (§2.23.5 p.103, Fig.2.98): scope V_C and I_C at switch closure; good = current peaks at V/R_series and decays exponentially while V_C rises exponentially to the applied voltage.
- RC timing (§2.23.8 p.106-107, Fig.2.101/2.103): scope V_C vs time after a step; x = time (0-5 tau), y = V_C/Vs; good = 63.2 % at t = tau, 99.24 % at 5 tau; for discharge 0.76 % at 5 tau.
- RL energizing (§2.24.10 p.142, Fig.2.136): scope inductor current (sense resistor) vs time; good = exponential rise to Vs/R with tau = L/R.
- Inductive turn-off (§2.24.9 p.140-141): scope the voltage across the opening switch at turn-off; good = clamped transient well below switch/contact rating; bad = kV-level spike/arcing.
- Capacitor impedance vs frequency (Fig.2.107b p.112): sweep |Z| vs f (log-log); good = follows 1/(2*pi*f*C) below SRF, minimum ~ESR at SRF.
- Inductance vs bias current (§2.24.8 p.135-136): measure L while stepping dc bias; good = flat L below I_sat, falling sharply at saturation.
- RL square-wave response (§2.24.11 p.146, Fig.2.140): drive 0-5 V square wave through R-L; plot V_R and V_L vs time over several periods for tau/T = 0.01, 0.1, 1, 100; good (full settling) when 5*tau <= T/2.
- Inductive turn-off spike (§2.24.12 p.147): scope transistor collector/switch voltage at turn-off with and without the coil diode; pass = spike clamped to ~supply + diode drop.
- AC power (§2.28 p.176-179): measure V_rms, I_rms and the V-I phase angle (dual-channel scope with current sense); compute VA, P, VAR, PF; good = VA^2 = P^2 + VAR^2 and PF sign as expected.
- Inductor impedance vs frequency (Fig.2.147-2.148 p.152-154): sweep |Z| of the real inductor; good = linear rise (inductive) below SRF, peak at SRF, capacitive fall above.
- Resonance sweep (Fig.2.176-2.180 p.188-199): sweep source frequency across f0; plot |I| (series) or |Z| (parallel) vs log f; read f0 at peak/dip and BW at the 0.707 (-3 dB) points; good = Q = f0/BW matches design, symmetric for Q >= 10.
- Parallel tank tuning (§2.30.6 p.198): tune for minimum line current with a current meter; for Q > 10 this lands within ~1 % of X_L = X_C and introduces negligible phase angle.
- Filter response (Fig.2.189-2.197 p.210-221): Bode plot attenuation (dB) and phase vs log f, unloaded and with the real load; good = -3 dB and 45 deg at f_c; loaded curve shows predicted gain drop/shift.
- Compensated attenuator (§2.33.2 p.222-223): apply a square wave and adjust the trimmer capacitor for a flat top (no overshoot/rounding) - the same procedure as scope-probe compensation.
- Series RLC step response (Fig.2.210-2.212 p.233-235): x = time, y = current (or V_C); overdamped = single hump, critically damped = fastest return without crossing zero, underdamped = decaying oscillation at ~1/(2*pi*sqrt(LC)); verify R vs 2*sqrt(L/C).
- Square-wave harmonic content (Fig.2.215 p.239; §2.36 p.245): spectrum analyzer or FFT of the waveform; good = odd harmonics falling as 1/n for 50 % duty; even harmonics appear when duty deviates.
- Simulation vs bench (§2.37.2 p.249): after SPICE, build and measure the breadboard; treat the measurement as authoritative; add noise/crosstalk/parasitic models where they matter.
- Battery discharge characterization (§3.2.5 p.287-289): discharge at the product's load current(s) and at the rated C-rate; plot terminal voltage vs time (and vs delivered mAh); read runtime to the equipment cut-off voltage; good = runtime >= requirement with margin at end-of-life internal resistance.
- Internal resistance (§3.2.6 p.289, Fig.3.32): measure V_oc with a high-impedance voltmeter, then V_L under a known load; R_in = (V_oc - V_L)/I_L; repeat at 50 % and 90 % discharge.
- Li-ion charge profile (§3.2.4 p.282): log voltage, current and cell temperature during charge; good = constant-current phase then voltage-limited phase terminating when current levels at ~3 % of charge current; temperature stays well below the ~90 degC cut-off.
- VSWR (§3.1.5 p.268-269, Fig.3.17): measure V_max/V_min along the line or forward/reflected power; good = VSWR near 1.
- Cable Z0 (§3.1.5 p.265): measure C/ft and L/ft (LCR meter on a known length) and compute sqrt(L/C).
- Relay coil turn-off (§3.4.2 p.298): scope the driver collector/switch at coil release with and without suppression; good = spike clamped near supply + diode drop (dc) or damped by RC (ac); bad = hundreds of volts (up to ~1000 V).
- Resistor pulse/surge qualification (§3.5.5 p.316-318): apply the worst-case pulse (energy, duration) and measure resistance shift; good = shift within tolerance, no flashover.
- Capacitor impedance vs frequency (Fig.3.65 Graph A p.332): sweep |Z| log-log; read SRF at the minimum (= ESR); good = SRF above the decoupling band of interest.
- Decoupling effectiveness (§3.6.9 p.345): scope V_CC at the IC pins with a short ground spring during worst-case switching (whole bus toggling); good = spikes well below the 10-100 mV per device / ~500 mV bus levels quoted, within logic noise margin.
- Ripple (§3.6.11 p.348-349): scope ac-coupled at the filter capacitor under full load; record Vpp and Vrms; ripple factor = Vrms/Vdc <= 0.05.
- Contact snubber (§3.6.12 p.350-352): scope voltage across opening contacts; pass = peak < 300 V and rise rate < 1 V/us.
- Inductor bias sweep (§3.7.7 p.361-362): measure L vs dc bias; mark 5 %, 10 %, 20 % drop points; good = operating peak current below the relevant point.
- Transformer regulation (§3.8.1 p.384-385): measure secondary voltage at no load and at rated load; compare with turns ratio; good = loaded drop consistent with datasheet regulation, temperature rise within rating at rated VA.
- Magnetizing current (§3.8.1 p.376, p.385): measure no-load primary current at rated voltage and frequency; a transformer fed below its rated frequency shows excessive magnetizing current and heating.
- Fuse coordination (§3.9 p.397): apply nominal load and the worst-case inrush; confirm the fuse does not open; apply the fault case and confirm it clears before the protected parts overheat.
- Rectifier/diode stress (§4.2.5 p.415-417): scope the reverse voltage across each diode at maximum line and no load; good = peak below PIV with margin; measure diode case temperature at full load.
- Zener regulator (§4.2.6 p.421): step the input over V_in,min..V_in,max and the load over I_L,min..I_L,max; plot V_out; good = regulation held with I_Z >= I_Z,min at (V_in,min, I_L,max) and zener dissipation within rating at (V_in,max, no load).
- BJT/FET amplifier Q-point and response (§4.3.2 p.439-442): measure V_E, V_C (target V_C ~ V_CC/2, V_E ~ 1 V) with transistors of low and high h_FE; Bode plot gain vs log f with the real load; good = gain within spec and -3 dB at the design f_3dB.
- JFET characterization (§4.3.3 p.451-453): curve-trace I_D vs V_DS for several V_GS; extract I_DSS and V_GS,off before finalizing source resistors (spread is large).
- TVS/MOV clamp (§4.5.2 p.484-489): apply the specified surge (e.g. 10/1000 us for MOV energy) and record the clamped voltage vs time; good = V_C below the protected part's limit; for MOVs re-measure V_NOM and leakage after repeated surges (wear-out).
- Phase control (§4.4.4 p.479-481): scope load voltage vs time over a half cycle while sweeping the control pot; good = smooth conduction-angle change, reliable firing every half cycle (diac triggering).
- LED drive (§5.3.3-5.3.4 p.503-505): measure LED current with a series ammeter at minimum and maximum supply and at operating temperature; for parallel strings measure each branch; good = within rating and branches balanced.
- Laser L-I curve (§5.3.5 p.510-511): with a calibrated optical power meter, sweep drive current slowly from zero; plot optical power vs current; identify threshold I_th and slope efficiency; good = operating point below P_o(max) with margin at the coldest operating temperature (ACC) and no current overshoot at power-up (scope the drive current during turn-on).
- Thermistor/RTD calibration (§6.1.3 p.527-528): record raw ADC readings at reference temperatures (e.g. calibrated oven, 0 degC and 100 degC points); build/verify the lookup table; plot error vs temperature; good = within accuracy spec over the range.
- Ultrasonic ranging vs temperature (§6.3.2 p.537): measure a fixed target distance at several ambient temperatures; good = error within spec after compensation.
- Meter loading (§7.3.4 p.574-575): compare readings with two meters of different input resistance, or compute error from known internal resistance; good = < 5 % disagreement.
- Probe compensation and phase (§7.4.5-7.4.6 p.583-590): connect the probe to the 1 kHz CAL square wave and adjust for a flat top; for phase, use matched cables, dual trace, and compute phase from displacement.

## 5. Pitfalls, failure modes, review checklist

- Powering a load from a bench supply's + and GND (earth) terminals without jumpering - to GND: zero current, no return path (§2.10.1 p.44, Fig.2.31).
- Inferring heat dissipation from V*I of a load that does mechanical/optical/acoustic work (§2.7 p.33).
- A thin interface layer (e.g. 0.002 in silicone grease) can contribute more temperature rise than the thick ceramic and metal layers combined - specify thin, void-free thermal interfaces (§2.8.1 p.38 example).
- Aluminum terminations: oxide raises contact resistance; historical fire hazard in home wiring (§2.5.2 p.26).
- Body current of ~100 mA to 1 A is sufficient to induce cardiac/respiratory arrest (§2.2.1 p.9).
- Shorting a battery: internal resistance limits current but heats the cell, drains it and can rupture it (§2.9 p.40).
- The earth-ground symbol is used loosely (0 V reference, generic return, true earth); use distinct earth, chassis, analog and digital ground symbols and state what each means (§2.10.1-2.10.2 p.45-46, Fig.2.33-2.34).
- A floating chassis tied to circuit return (not earthed) is a potential shock hazard (§2.10.3 p.49, Fig.2.36d).
- Using an earth (mains PE) conductor as a current return is unwise (§2.10.1 p.45).
- Breadboard ground connections with wrong wire gauge or loose sockets give intermittent contact and noise (§2.10.3 p.48).
- Parallel batteries of different voltage/chemistry or age cause problems (§2.15 p.67).
- Short circuits are commonly caused by wire crossing, insulation failure, solder splatter; opens by lead separation or burned-out parts (§2.16 p.68).
- Mains work: in many places modifications must be done or checked by a certified electrician; switch the main breaker off; tag the breaker you are working on (§2.22 p.94).
- Do not apply a constant current to a capacitor indefinitely - voltage ramps without limit (10 uF at 50 mA reaches 5000 V in 1 s) (§2.23.6 p.104).
- Stray capacitance between runs/leads couples circuits; keep capacitor leads short and group components to avoid capacitive coupling; high-impedance circuits are most affected and stray C in parallel bypasses high-frequency signal (§2.23.9 p.108).
- Ideal L/C equations predict infinite current/voltage at steps; always include source/ESR/R_DC in transient calculations (§2.23.5 p.103; §2.24.9 p.140-141).
- Capacitor voltage rating often missing from schematics - derive it from the node voltage (§2.23.10 p.109).
- Book arithmetic/unit slips to watch: Example 7 prints 0.17 uH where its own AL formula gives mH (p.138); discharge "37.8 percent" at 1 tau (exact 36.8 %) (p.108).
- Adding reactive voltages or powers arithmetically ignores phase: 5.35 V + 10.70 V = 16.05 V "exceeds" a 12 V source; 0.572 W + 1.145 VAR is not 1.284 VA - use phasors or VA = sqrt(P^2 + VAR^2) (§2.27.3 p.175; §2.28 p.177-178).
- A long scope ground lead picks up magnetic interference that appears as signal noise (§2.24.15 p.149).
- Equipment left plugged in during electrical storms can take induced spikes via power and ground conductors (§2.24.15 p.149).
- Using XL = XC as the resonance of a lossy parallel RLC: minimum current (antiresonance) is at a different frequency unless Q > 10 (§2.30.6 p.197-198, Fig.2.181).
- Quoting voltage-ratio dB between points of different impedance (20*log V ratio is only a power ratio when impedances match) (§2.31 p.205-206).
- Ignoring load resistance when computing a passive filter's cutoff or a bandpass Q (load in parallel lowers Q) (§2.33.1 p.213-219).
- Trusting a simulation that lacks noise, crosstalk, interference or failure mechanisms (SPICE omits them unless modeled) (§2.37.2 p.249).
- Designing for exact critical damping - drift in R or temperature makes it under- or overdamped (§2.34.1 p.233).
- Carbon-zinc cells left in expensive equipment leak (§3.2.3 p.275).
- Charging rechargeable alkaline (RAM) cells in a standard charger may cause an explosion (§3.2.4 p.285).
- Storing SLA batteries discharged causes sulfation (§3.2.4 p.280).
- NiCd on float charge or shallow cycling suffers memory effect (§3.2.4 p.281).
- Li-ion cannot be trickle/float charged; unprotected packs are a safety risk on over-charge/over-discharge (§3.2.4 p.281-282).
- Substituting 1.2 V NiCd/NiMH cells for 1.5 V alkaline in equipment needing four or more cells may fail (§3.2.4 p.280-281).
- Supercapacitor strings of more than 3-4 cells without voltage balancing over-voltage individual cells (§3.2.4 p.286).
- Book table inconsistencies: Table 2.5 AWG 8 row; Table 3.4 vs Example 1 (RG-11A/U); polystyrene k in Table 3.3; NiFe energy density in Table 3.6 vs text.
- Replacing a blue/white (fusible/nonflammable) resistor with an ordinary one (§3.5.3 p.305).
- Swapping a drifty carbon-film resistor (hundreds of ppm/degC, negative TC) for a metal-film part (§3.5.4 p.310; §3.5.5 p.316).
- Potentiometer taper codes: modern A = log, B = linear; older A = linear, C = log - check the supplier's convention (§3.5.7 p.323).
- Running a pot's rated power through a fraction of its element, or dc wiper current through a trimmer not rated for it (§3.5.7 p.324).
- Polystyrene capacitors heated much above 70 degC (e.g. by soldering) change value permanently (§3.6.8 p.340).
- Reverse-polarized or over-voltaged aluminium electrolytics explode (§3.6.8 p.334).
- Tantalum capacitors exposed to current spikes fail (§3.6.8 p.334).
- HiK/class-2 ceramics used in timing, filter or tuned circuits; monolithic ceramics (high DA) used as sample-hold capacitors (§3.6.7-3.6.8 p.331-337).
- Supercapacitors used for ripple absorption (high ESR) (§3.6.8 p.341).
- DC-coil relay driven from ac chatters; a diode across an ac relay coil does not work (§3.4 p.296-298).
- Book misprints to watch: "avoid capacitors with low ESR" for decoupling (p.346, read high ESR); S/H caption "use capacitors with high ESR" (p.348); snubber resistor called a "capacitor" (p.352); SSR switching time 1-100 ns (p.295, as printed).
- Driving a transformer secondary to "get" a higher primary voltage - insulation failure (§3.8.1 p.385).
- Running a 60 Hz transformer at 20 Hz (or with dc in a winding) - overheating from magnetizing current (§3.8.1 p.385).
- Using a Variac or autotransformer as if it were isolating; putting the isolation transformer after the Variac (§3.8.3 p.388).
- Relying on the building's 15 A breaker to protect an instrument or product (§3.9 p.397).
- Fuse in the neutral: the device stays live after the fuse blows (§3.9 p.397).
- Designing to a specific h_FE (spread 50-500 in one family) (§4.3.2 p.444).
- Germanium diodes above 85 degC (§4.2.1 p.409).
- A series reverse-protection diode silently steals ~0.6 V of battery life; a shunt diode on a low-impedance battery draws a huge current (§4.2.5 p.413).
- Fly-back diodes do not help at turn-on; relay drivers need them anyway (§4.2.5 p.413).
- Zener regulators drift with temperature; do not use for critical references (§4.2.6 p.421).
- JFET I_DSS and V_GS,off vary widely part to part - self-biased current sources are unpredictable (§4.3.3 p.455).
- Handling MOSFETs without static control destroys gate oxide (§4.3.4 p.465).
- Triggering a triac without a diac can be unreliable over temperature (§4.4.5 p.481).
- MOVs wear out and fail short - always fuse them; zeners fail open and leave circuits unprotected (§4.5.2 p.488).
- Using RMS instead of peak when choosing TVS/MOV working voltage on ac lines (§4.5.2 p.485, p.489).
- Book misprints to watch: "1N5281B" as a 5.1 V zener (p.423; the 5.1 V part in Table 4.2 is 1N5231B); multiplier capacitor RMS equivalents (p.417); "ZMM52330B" in Table 4.2.
- LEDs paralleled on one resistor hog current as they warm (§5.3.4 p.505).
- Running LED strings close to the supply voltage (> 80 %) makes current unpredictable (§5.3.4 p.505).
- Driving laser diodes from a bench supply, through a switch/relay, or with intermittent feedback connections destroys them (§5.3.5 p.508-510).
- Laser modules/pointers cannot be modulated faster than a few hertz (§5.3.5 p.510).
- Photoresistors take seconds to recover their dark resistance (§5.4.2 p.513).
- Linearizing an NTC thermistor over 0-100 degC gives considerable error (§6.2.1 p.529).
- IR reflective distance sensors are ambiguous below ~5 cm (§6.3.3 p.538).
- GFCIs do not protect against shock from inside line-connected equipment; fuses/breakers do not protect people (§7.1.1 p.554).
- Too many IC sockets reduce reliability (§7.2.6 p.567).
- Perfboard jumpers act as antennas and pick up noise (§7.2.4 p.559).
- Book errors to avoid copying: Fig.7.39 gives Vrms = 8.5 V for a 12 Vpp sine (correct: 12/(2*sqrt(2)) = 4.24 V) (p.588); "Vrms = 0.707 Vpeak-to-peak" (p.572; should be V_peak); "12-bit ADC ... 0 to 1023" (p.528; 12-bit is 0-4095); the ohmmeter rule "at least 20 times the Thevenin resistance" (p.575) contradicts the 50 ohm example (an ohmmeter's series resistance should be << the measured R); 430 nm blue "6 V" in text vs 3.8 V in Table 5.1.

## 6. Standards referenced

| standard | edition/year | what it governs (clause/table where given) | source |
|---|---|---|---|
| RoHS (EU Restriction of Hazardous Substances Directive) | no edition given | lead banned in consumer electronics -> lead-free solders | §7.2.7 p.568 |
| American Wire Gauge (AWG) / Brown & Sharpe (B&S) gauge | - | copper wire sizes, resistance, current capacity | §2.9 p.39; §3.1.1 p.253-255 |
| British Standard Wire Gauge (SWG) | - | nearest SWG equivalents in Table 3.1 | §3.1.1 p.254-255 |
| IEC battery designations (CRxxxx, BRxxxx lithium; SRxx silver oxide) | - | button/coin cell labelling | §3.2.2 p.274 |
| EIA capacitor temperature-characteristic codes (C0G/NPO, N030 (SIG), N150 (P2G), X7R and letter/number class-2 code) | - | ceramic capacitor temperature coefficient/change | §3.6.8 p.335-336 |
| Military-spec resistor reliability band | - | % resistance change per 1000 h (brown 1 %, red 0.1 %, orange 0.01 %, yellow 0.001 %) | §3.5.3 p.304 |
| Electrical codes (appliance frame earthing) | not named | washers/dryers and metal frames must be earthed | §2.10.3 p.47 |
| National mains practice (US split phase 120/240 V; 240 V/50 Hz elsewhere) | - | neutral-ground bonding only at main panel; colour codes | §2.22 p.92-94 |
| GFCI (ground fault circuit interrupter) | - | trips at ~5-10 mA ground current | §7.1.1 p.552 |
| 10/1000 us impulse current waveform | - | MOV transient energy rating W_TM | §4.5.2 p.489 |
| 1-Wire bus (DS18B20) | - | multi-drop digital sensor bus with 4.7 kohm pull-up, parasitic power | §6.2.5 p.533-534 |
| I2C serial interface | - | accelerometer (MMA8452Q) data interface | §6.4.2 p.542 |
| Gerber (RS-274X implied, not named) file set | - | PCB fabrication data (GTL/GBL/GTS/GBS/GTO/GBO/TXT) | §7.2.5 p.566 |
| RG-8A/U, RG-11A/U, RG-58/U, RG-59A/U coax designations; CAT5 | - | cable impedance and construction | §3.1.2 p.257; §3.1.5 p.265 |

## 7. Process / lifecycle guidance

The book is not a product-development text; Ch.7 gives a construction flow, captured here.

| stage | activity | deliverable | exit criterion | source |
|---|---|---|---|---|
| schematic capture | draw schematic with conventions, values, power ratings, polarities, title block; run CAD ERC | reviewed schematic | no missing values/polarities/ratings; ERC clean | §7.2.1 p.556-557 |
| simulation | model the circuit (SPICE-based simulator) and iterate values | simulated operating points/waveforms | behaviour as intended; remember models omit noise, crosstalk and failures | §7.2.2 p.558; §2.37.2 p.249 |
| breadboard prototype | build on solderless breadboard (0.1 in pitch, 22 AWG) | working prototype | measured behaviour matches intent (breadboard is the final answer) | §7.2.3 p.558-559 |
| final circuit | perfboard (noncritical), wire-wrap (multi-IC logic) or custom PCB (high-speed, low-level analog); layout rules (rows, 2 mm border, edge I/O, polarity/labels) | assembled board | DRC clean, Gerbers released, board assembled and inspected | §7.2.4-7.2.6 p.559-567 |
| enclosure | metal (grounded, HV) or plastic box; standoffs; strain relief/grommet; controls front, fuses back; cooling (fan > ~10 W) | enclosed product | safety bonding and cooling verified | §7.2.9 p.569-570 |
| troubleshooting | follow the troubleshooting flowchart (Fig.7.14) with meters and scope | working unit | faults cleared | §7.2.11 p.570-571 |

## 8. Coverage log

- Lines 1-2424: front matter, copyright/ISBN page, full table of contents (Ch.1-17, App. A-C), preface, acknowledgments - read for orientation.
- Lines 2425-2646: Ch.1 Introduction (pp.1-3) - read; no rules (overview flowchart only).
- Lines 2647-3733: Ch.2 §2.1-2.10.1 (pp.5-45) - read. Skipped as non-design content: Table 2.1 (Fermi energy/velocity, work function) and the free-electron/quantum conduction narrative (§2.4, pp.18-23), band-theory narrative (§2.6).
- Table 2.2 and Table 2.4 are column-scrambled in the text extraction and were reconstructed (see table notes).
- Lines 3733-5780: Ch.2 §2.10.1 (end) through §2.23.6 (pp.45-105) read in full. Skipped: Kirchhoff determinant/Cramer's rule derivation (§2.17 p.72-73, pure math), superposition proof. Table 2.6 (types of ground symbols, p.46) is a figure-only table absent from the extraction. The "standard resistor values table in the front matter" referenced on p.58 is not present in the text file.
- Lines 5780-7178: Ch.2 §2.23.6 (end) through §2.24.10 (pp.105-142) read in full. Skipped: electromagnetism narrative (§2.24.1-2.24.3 physics of fields, Faraday's law derivation), water analogy (§2.24.5). Table 2.7 has possible u/m prefix ambiguities (flagged). Fig.2.129 (air-core formula set) and Fig.2.133 (toroid core tables T-12-2, FT-50-61) are figures - only the formulas/values used in the prose examples are captured.
- Lines 7178-9475: Ch.2 §2.24.10 (end) through §2.29 (pp.142-187) read. Skipped as pure math: §2.25 differential-equation modeling (p.155-158), §2.26 complex-number arithmetic (Table 2.10, p.159-164), phasor derivations in §2.27.1-2.27.2. Fig.2.149 (inductive divider formula) is figure-only; the formula is given from the standard divider relation (medium).
- Lines 9475-12671: Ch.2 §2.29 (end) through §2.34 first examples (pp.187-225) read in full. Skipped as pure math: transfer-function algebra of each filter (retained results only), differential-equation solution steps in §2.34.
- Lines 12671-14301: Ch.2 §2.34 (remaining examples), §2.34.1 series RLC, §2.35 Fourier series, §2.36 nonperiodic sources, §2.37 SPICE (pp.225-251) read. Skipped: Fourier-coefficient derivations, SPICE history and nodal-matrix derivation (§2.37.1), CircuitLab tutorial screenshots (§2.37.3; only the ~1.6 kHz crossover observation, figure-dependent). Fig.2.216 (table of Fourier series for common waveforms) is a figure absent from the extraction.
- Chapter 2 complete (lines 2647-14301).
- Lines 14302-16416: Ch.3 §3.1 wires, cables, connectors, high-frequency effects (pp.253-271); §3.2 batteries (pp.271-290); start of §3.3 switches (pp.290-294) read. Figures (connector drawings Fig.3.5, symbols Fig.3.6) are drawings only. Table 3.5 internal-resistance/discharge-rate/cost columns scrambled - not transcribed. Several square-root signs are lost in the extraction (quarter-wave, transformer turns ratio, v = c/sqrt(k)); restored where the book's own worked examples confirm them (tagged medium).
- Lines 16416-18264: Ch.3 §3.3.4 switch applications (end), §3.4 relays, §3.5 resistors, §3.6 capacitors, §3.7 inductors, §3.8 opening (pp.294-375) read in full. Figures with formulas not in the text: Fig.3.52 (colour-code table), Fig.3.55 (power-rating factor chart - only the worked example factors are available), Fig.3.66 (capacitor label codes), Fig.3.67/3.68 (coupling/bypass formulas), Fig.3.74 (ripple equations), Fig.3.77 (contact-material arc table), Fig.3.85 (inductor construction formulas), Fig.3.90 (inductor codes). Table 3.7 is heavily scrambled; film-row ratings uncertain (flagged). Skipped: §3.6.14 problems except where they add numbers.
- Lines 18264-18872: Ch.3 §3.8 transformers (pp.375-396) and §3.9 fuses/breakers (pp.397-399) read in full. Phase-dot explanation and gearbox analogy read, not extracted. Chapter 3 complete (lines 14302-18872).
- Lines 18873-24537: Ch.4 Semiconductors (pp.401-493) read in full: semiconductor physics narrative (§4.1, not extracted), diodes and applications (§4.2), transistors BJT/JFET/MOSFET/IGBT/UJT/PUT (§4.3), thyristors (§4.4), transient suppressors (§4.5), IC packages (§4.6). Skipped as non-design content: water analogies, "how it works" band narratives, diode ROM and logic-gate toy circuits, multivibrator narratives. Table 4.1 columns I_R/I_FSM/V_F are partly unassigned in the extraction (flagged).
- Lines 24538-25605: Ch.5 Optoelectronics (pp.495-524) read in full: photon/spectrum narrative and lamp types (not extracted beyond LED/laser/photodetector data), LEDs, laser diodes, photoresistors, photodiodes, solar cells, phototransistors, photothyristors, optoisolators, optical fibre.
- Lines 25606-26849: Ch.6 Sensors (pp.525-550) read in full. GPS (§6.7) and sound-level (§6.6.4) sections are descriptive only.
- Lines 26850-28484: Ch.7 Hands-on Electronics §7.1 safety through §7.4.6 "Measuring Things with Scopes" (pp.551-590) read; the assigned stop line 28400 falls inside §7.4.6, which was finished (ends ~line 28484, p.590). Oscilloscope CRT/"how scopes work" and knob-by-knob control descriptions (§7.4.1-7.4.5) were read; only quantitative/procedural content extracted. Fig.7.14 (troubleshooting flowchart) is a figure absent from the text.
- Not read (other agent's range): §7.4.7 Scope Applications onward (line ~28485 to end of book).

- Totals: 309 rules (SCHERZ-1001 to SCHERZ-1309), assembled from 11 scratch parts.
