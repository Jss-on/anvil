# Practical Electronics for Inventors, 4th ed. (Scherz & Monk) - part 2 of 2 - Anvil rulebook

## 0. Citation

[1] P. Scherz and S. Monk, *Practical Electronics for Inventors*, 4th ed. New York, NY, USA: McGraw-Hill Education, 2016. ISBN 978-1-25-958754-2 (MHID 1-25-958754-1); LCCN 2016932853.

**Chapters covered by THIS extraction (part 2, source-text lines ~28259-55306):**
- Ch. 7 Hands-on Electronics - from §7.4.6 "Measuring Things with Scopes" (p.586) to §7.5.23 (p.633); the trigger-coupling tail of §7.4.5 (p.585-586) was also read.
- Ch. 8 Operational Amplifiers (p.635-662)
- Ch. 9 Filters (p.663-682)
- Ch. 10 Oscillators and Timers (p.683-698)
- Ch. 11 Voltage Regulators and Power Supplies (p.699-716)
- Ch. 12 Digital Electronics (p.717-841)
- Ch. 13 Microcontrollers (p.843-895)
- Ch. 14 Programmable Logic (p.897-931)
- Ch. 15 Motors (p.933-946)
- Ch. 16 Audio Electronics (p.947-961)
- Ch. 17 Modular Electronics (p.963-971)
- Appendix A Power Distribution and Home Wiring (p.973-978); Appendix B Error Analysis (p.979-982); Appendix C Useful Facts and Formulas (p.983-988, math only)

**NOT read in this extraction:** Ch. 1-6 and Ch. 7 §7.1-§7.4.5 (assigned to the part-1 extraction, source lines 1-28400); the Index (p.989 ff., skipped per brief).

**Conventions:** rule ids SCHERZ-2001 ... SCHERZ-2287. `conf`: high = number/formula stated in the text; medium = derived from a stated relation, read from a graph, or an OCR-reconstructed/recomputed value; low = qualitative guidance quantified or OCR-garbled. In formulas `\|\|` means "in parallel with"; units are SI unless the book used another unit. Page numbers are the printed page numbers. Several printed-example errors found while checking arithmetic are listed as ERRATA items in §5.

## 1. Design rules

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| SCHERZ-2001 | test | Measure current with a scope via a small series shunt (precision 1 ohm) so circuit operation is not disturbed; shunt power rating must be at least 2 ohm x Imax^2 | P_rating(W) >= 2(ohm) * Imax(A)^2 (i.e. 2x the I^2*R of a 1-ohm shunt); I = V_shunt/R | Imax (A), R_shunt (ohm) | Scope current measurement; example Imax = 0.5 A -> >= 1/2 W | calc | p.589 §7.4.6, Fig. 7.40 | high |
| SCHERZ-2002 | test | Two-channel phase measurement: phase factor = 360 deg / on-screen period; phase difference = horizontal offset x phase factor; probe cables must be short, equal length, same type | theta_f(deg/div) = 360/T_R(div); phi(deg) = phi_div * theta_f; e.g. 8 div period -> 45 deg/div; 2 div offset -> 90 deg | T_R (div), phi_div (div) | Unequal cables add phase error at high frequency | measure | p.590, Fig. 7.43 | high |
| SCHERZ-2003 | test | Pulse-response metrics are defined on the output pulse: rise 10->90 %, fall 90->10 %, width between 50 % points, delay from t=0 to 10 %, tilt and overshoot as percentages | tilt% = A/B*100; overshoot% = C/D*100 (A = droop of top, B = pulse top amplitude, C = excess above input top, D = input top amplitude) | scope captures of input/output pulse | Any pulse/step verification | measure | p.591, Fig. 7.45 | high |
| SCHERZ-2004 | test | Reflection impedance check with pulse generator + 50-ohm reference coax: reflected pulse is inverted when the load under test is lower than the line impedance, not inverted when higher | Z from Vout and Vreflect (printed formula OCR-garbled: "Z = 50 ohm - 1 2 Vout / Vreflect"; do not use without the printed book) | Vout, Vreflect (V) | 50-ohm source and reference cable | measure | p.592 §7.4.8, Fig. 7.46 | low |
| SCHERZ-2005 | esd | ESD bench: grounded dissipative mats + wrist strap containing a series 1 Mohm resistor; never ground yourself directly; one separate ground wire per mat/strap run to a common ground point; rubber mats on concrete must be antistatic | R_wriststrap = 1 Mohm series | bench layout | Handling sensitive ICs | inspect | p.595, Fig. 7.52 | high |
| SCHERZ-2006 | test | Verify every instrument chassis/ground post is actually at earth potential with an ohmmeter before use (do not assume 3-wire cords are fault-free) | R(earth to chassis) ~ 0 ohm | ohmmeter reading | Lab setup; also prevents ground loops | measure | p.595 §7.5.1 | low |
| SCHERZ-2007 | test | Bench DMM for serious work: >= 5-digit resolution, autorange lockout, input impedance > 10,000 Mohm held up to ~20 V; 10-Mohm-input meters load high-impedance nodes; use 4-wire resistance mode to remove lead resistance | Rin > 10 Gohm (<= 20 V) preferred; Rin = 10 Mohm typical | node source impedance | Loading error ~ Rsource/Rin | review | p.596 §7.5.3 | high |
| SCHERZ-2008 | test | Scope minimum: >= 2 channels and >= 100 MHz bandwidth even for slow amplifier circuits (to catch high-frequency oscillation) | BW >= 100 MHz; channels >= 2 | scope spec | General bench | review | p.598 §7.5.5 | high |
| SCHERZ-2009 | test | Scope bandwidth vs signal: >= 3-5x the fundamental for frequency/timing measurements; > 10x for accurate amplitude; capturing the 5th harmonic of a square wave needs 5x (100 MHz square -> 500 MHz scope and probe); beyond BW, attenuation > -3 dB and rise time degrades | BW >= 3..5*f0 (frequency); BW >= 10*f0 (amplitude); BW >= n*f0 to see nth harmonic | f0 (Hz) | Fig. 7.56: 50 MHz square on 20/100/500 MHz scopes | calc | p.598-600, Fig. 7.56 | high |
| SCHERZ-2010 | test | Digitizing scope sample rate must be >= 4x real-time bandwidth with sin(x)/x reconstruction, >= 10x without, to prevent aliasing; also check memory depth | fs >= 4*BW (reconstruction) ; fs >= 10*BW (none) | fs (S/s), BW (Hz) | Digital storage scopes | calc | p.599 | high |
| SCHERZ-2011 | test | Crystal/RF frequency verification needs a frequency counter; a scope's frequency reading has ~5 % or worse error | scope error >= 5 %; counter 0-250 MHz class | required accuracy | Crystal oscillators, RF | measure | p.608 §7.5.8 | high |
| SCHERZ-2012 | test | Never extend a probe cable with coax (typ. 100 pF/m loads the node and resonates, causing reflections) except 50-ohm probe into 50-ohm scope | C_coax ~ 100 pF/m | cable length (m) | 1-Mohm scope systems | review | p.601 §7.5.6 | high |
| SCHERZ-2013 | test | Probe loading: below 1 MHz the probe input resistance dominates loading; above 1 MHz the probe input capacitance dominates (Xc of tip falls with f, limiting BW and slowing edges) | f < 1 MHz -> R_in; f > 1 MHz -> C_in | f, R_in, C_in | Passive probes | calc | p.601-602 | high |
| SCHERZ-2014 | test | Match probe to scope input: 1-Mohm probes on 1-Mohm inputs, 50-ohm probes on 50-ohm inputs; a 10X probe presents 10 Mohm on a 1-Mohm input and 500 ohm on a 50-ohm input | Rin_total = k*Rscope for kX probe | probe X factor, scope Rin | Passive probes | review | p.602 | high |
| SCHERZ-2015 | test | Typical 1-Mohm scope input capacitance is 20 pF (range 5-100 pF); choose a probe whose compensation range covers the scope Cin, then trim; trimming cannot fix a Cin outside the probe's range | Cin_scope in probe comp range | Cin (pF) | Passive probe selection | review | p.602 | high |
| SCHERZ-2016 | test | Passive 10X probe: 9-Mohm tip + 1-Mohm scope = 10:1; bandwidth ~60-300 MHz vs 1X ~4-34 MHz; ~10x less capacitance; for signals < 500 V; 1X/10X rated ~400-500 V max, 100X ~1.4 kV, 1000X ~20 kV; switching 1X/10X changes bandwidth | V_meas <= 400-500 V (1X/10X) | signal amplitude, f | 1-Mohm/20-pF scope | review | p.602-605, Table 7.2, Fig. 7.58(a) | high |
| SCHERZ-2017 | test | Low-impedance (Z0) divider probe: tip resistor 450 ohm (10:1) or 950 ohm (20:1) into 50-ohm input, < 1 pF, GHz bandwidth, rise time <= 100 ps; only for < 50 V and nodes tolerant of heavy resistive loading; scope needs 50-ohm input | V < 50 V; Rload = 500 or 1000 ohm | node drive capability | ECL, 50-ohm lines, propagation-delay tests | review | p.603, 605, Table 7.2 | high |
| SCHERZ-2018 | test | High-voltage passive probe for > 500 V (example tip 500 Mohm); dedicated HV probes for > 2.5 kV (P6015A: 20 kV rms dc, 40 kV pulses, 75 MHz) | V > 500 V -> HV probe | V_peak | Line/SMPS/HV work | review | p.603, Fig. 7.58(d) | high |
| SCHERZ-2019 | test | Active FET probe for > 500 MHz or high-impedance nodes: ~1 pF, BW 500 MHz-4 GHz (to 6 GHz), source resistance 0-10 kohm; dynamic range +/-0.6 to +/-10 V; absolute max +/-40 V; ESD-sensitive | abs(V) <= 40 V abs max | V, f, Rsource | Ground-lead length less critical | review | p.604, 606, Fig. 7.58(b) | high |
| SCHERZ-2020 | test | Floating/differential measurements need a differential probe (CMRR ~3000:1 at 1 MHz; modern 1 GHz BW, 60 dB CMRR at 1 MHz falling to 30 dB at 1 GHz); scope A-B math with two probes is inadequate at HF or near noise level (skew, poor CMR) | CMRR >= 60 dB @ 1 MHz | f, signal amplitude | e.g. across a collector resistor, SMPS nodes | review | p.604, 606 | high |
| SCHERZ-2021 | test | Current probes: transformer (ac-only) types cover a few hundred Hz to ~1 GHz; Hall + transformer types cover dc to ~50 MHz | ac: ~100s Hz-1 GHz; Hall: dc-50 MHz | f range, dc content | Noninvasive current measurement | review | p.606-607 | high |
| SCHERZ-2022 | test | Compensate attenuating probes on the scope's 1-10 kHz square calibrator: trim for flat tops with no overshoot or rounding; recheck on every channel change or tip-adapter change | cal square 1-10 kHz; flat top | scope display | 10X/100X probes; critical for rise/fall-time measurements | measure | p.607 | high |
| SCHERZ-2023 | test | Keep passive-probe ground leads short and never lengthen them (lead inductance + probe C rings); do not substitute soldered wire stubs for probe tips - even 1 inch of wire changes impedance significantly at high frequency | lead stub < 1 in | probe setup | HF / fast-edge measurements | inspect | p.601, 607 | high |
| SCHERZ-2024 | test | Bench function generator: sine/square/triangle with upper frequency preferably > 5 MHz; phone-app generators cover ~50 Hz-20 kHz with uncalibrated amplitude (measure with scope) | f_max > 5 MHz | test plan | General bench | review | p.607 §7.5.7 | high |
| SCHERZ-2025 | test | Use a 1:1 isolation transformer (typ. 200 VA) before probing line-powered equipment without input isolation (SMPS, TVs, hot chassis); a scope ground on the SMPS bulk-capacitor negative ("floating ground", one diode drop from hot) blows a bridge diode and vaporizes the probe | isolation xfmr >= 200 VA typical | equipment topology | Some TV chassis sit 80-90 V above earth | inspect | p.611-613, Fig. 7.63-7.64 | high |
| SCHERZ-2026 | test | Variac is not isolating: put the isolation transformer before (never after) the Variac; output common must be neutral; 2 A Variac suffices (5 A better); ramp repaired line equipment up gradually (troubleshoot ~85 V) to limit fault current | I_variac >= 2 A | load current | Line-powered troubleshooting | review | p.613-614, Fig. 7.65 | high |
| SCHERZ-2027 | test | Resistance decade box: 1/2-W metal-film resistors; 0.1-ohm decade wirewound (inductive; avoid in HF circuits); commercial R/C/L boxes accuracy ~1 % or better | tol <= 1 % | - | Prototype value tuning | review | p.614-615, Fig. 7.66-7.67 | high |
| SCHERZ-2028 | components | Capacitor dielectric by value decade (substitution-box practice): mica for 100-900 pF, polystyrene 0.001-0.009 uF, polycarbonate 0.01-0.9 uF, polyester 1-9 uF, tantalum/electrolytic >= 10 uF (observe polarity); air-dielectric trimmers for high-precision low values | see Table S2-7.1 | C value | General-purpose selection guidance | review | p.616 §7.5.14 | high |
| SCHERZ-2029 | components | Use 1/2-W 1 % metal-film resistors above 1 ohm; below 1 ohm use wirewound or resistance wire, but wirewound is inductive at high frequency | R >= 1 ohm: metal film 1 %; R < 1 ohm: wirewound (not HF) | R, f | Precision/prototype resistors | review | p.616 | high |
| SCHERZ-2030 | solder | Iron wattage: 25-40 W pencil iron for most work; 15 W for very small components/pads; 50 W for very large joints; never use large irons or solder guns on PCBs (only e.g. >= 14 AWG stranded wire to aluminum chassis) | P_iron = 25-40 W general; 15 W fine; 50 W large | joint size | Hand soldering | review | p.618 §7.5.16 | high |
| SCHERZ-2031 | solder | Chisel tip 0.05-0.08 in across the spade for general work; smaller tips for SMD/small pads; an under-temperature iron needs long dwell and delaminates pads/traces and overheats parts | tip width 0.05-0.08 in | pad size | Hand soldering | inspect | p.618 | high |
| SCHERZ-2032 | esd | Use a grounded-tip (ESD-safe) soldering iron for static-sensitive devices; use an antistatic desoldering pump (ordinary pumps generate high voltage by friction) | tip grounded | device ESD class | Static-sensitive parts | inspect | p.618, 620 | high |
| SCHERZ-2033 | solder | Tin-lead alloys: 60/40 (SN60) general work, 63/37 (SN63) for small heat-sensitive parts and PCB pads; melting point quoted 361 F for both; 62/36/2 (Sn/Pb/Ag) also used | T_melt = 361 F (183 C) | alloy | Leaded hand soldering | review | p.618-619 | high |
| SCHERZ-2034 | solder | Iron set-point: ~330 C (625 F) for traditional leaded solder; ~400 C (750 F) for lead-free; use a flux pen when a joint will not flow | T_tip = 330 C (SnPb), 400 C (Pb-free) | alloy | Hand soldering | review | p.619 | high |
| SCHERZ-2035 | solder | Use only mild rosin flux (rosin-core or rosin flux); never acid-core/corrosive or conductive fluxes; remove residue with defluxer / isopropyl alcohol (water if water-soluble) to avoid low-resistance paths between pads | flux class = rosin (mild) | flux type | Electronics assembly | inspect | p.619 | high |
| SCHERZ-2036 | solder | Solder wire diameter: 0.020 in/0.508 mm (25 ga) or smaller for small pads and hand SMD; 0.031 in/0.79 mm (21 ga) all-round PCB work; 0.040 in/1 mm (19 ga) or larger only for >= 14 AWG wire, terminals, chassis - too much solder for PCBs (bridging) | d = 0.020 / 0.031 / 0.040 in by joint class | joint class | Hand soldering | review | p.619 | high |
| SCHERZ-2037 | assembly | Solderless breadboards accept leads of 0.3-0.8 mm (20-30 AWG); not for RF circuits (strip capacitance) and not for currents above ~100 mA | I <= ~100 mA; lead 0.3-0.8 mm | current, frequency | Prototyping | review | p.621 §7.5.17 | high |
| SCHERZ-2038 | assembly | Perforated prototyping boards use 0.1-in hole pitch; SMD-to-SIP adapters (Surfboards) convert SMD footprints to 0.100-in centers for breadboard use | pitch = 0.1 in | - | Prototyping | inspect | p.622 | high |
| SCHERZ-2039 | cables | Hookup wire stock: 16, 22 and 24 AWG cover most needs; breadboard jumpers from solid 22 AWG; flexible jumpers from 22/24 AWG stranded with 0.156-in crimp sockets on 0.100-in headers; ribbon cable 28 AWG; twisted pair 24 AWG; wire-wrap 30 AWG Kynar (larger wire for higher current); magnet wire 22-30 AWG | AWG per use | application | Prototype wiring | review | p.624-625 §7.5.19 | high |
| SCHERZ-2040 | assembly | Heat-shrink tubing: common shrink ratio 2:1 (also 3:1); standard pre-shrink IDs 3/64, 1/16, 3/32, 1/8, 3/16, 1/4, 5/16, 3/8, 1/2, 5/8, 3/4, 1, 2, 3, 4 in; choose so shrunk ID grips the bundle | ID_shrunk = ID/ratio | bundle OD | Wire/terminal insulation | inspect | p.625 | high |
| SCHERZ-2041 | assembly | Hand tools ranges: strippers 10-18 AWG and 16-26 AWG; general crimper ~10-22 AWG with insulated/non-insulated sections; D-sub crimper 14-26 AWG | - | wire gauge | Harness/prototype | review | p.622-623 §7.5.18 | high |
| SCHERZ-2042 | reliability | Outdoor low-voltage wire-nut splices: apply antioxidant joint compound before closing to prevent corrosion under moisture | - | environment | Outdoor wiring | inspect | p.626 | low |
| SCHERZ-2043 | bringup | Use circuit chiller (freeze spray) to localize intermittent components, cold solder joints, PCB cracks and oxidized junctions | - | intermittent fault | Troubleshooting | measure | p.626 | low |
| SCHERZ-2044 | test | SPICE simulation becomes unreliable above ~100 MHz; use RF design tools/models beyond that | f_sim_SPICE <= ~100 MHz | highest signal frequency | Circuit simulation | review | p.630 §7.5.22 (NI Multisim entry) | medium |
| SCHERZ-2045 | components | Real op-amp parameter ranges for first-order modeling: open-loop gain 1e4-1e6 (80-120 dB) at dc; input resistance ~1e6 ohm (bipolar) to 1e12 ohm (JFET); output resistance 10-1000 ohm; input current pA (JFET, MOSFET down to a few tenths of pA) to nA (bipolar) | Ao = 1e4..1e6; Rin = 1e6..1e12 ohm; Rout = 10..1000 ohm | op-amp type | Ideal-model sanity bounds | review | p.638, 645-646 §8.3, §8.6 | high |
| SCHERZ-2046 | control-loop | Negative-feedback gain formulas (ideal rules: V+ = V-, no input current): inverting G = -R2/R1 (R1 = R2 -> unity inverter); noninverting G = 1 + R2/R1; follower G = 1 | G_inv = -R2/R1; G_ni = 1 + R2/R1 | R1, R2 (ohm) | Examples: 10k/100k -> -10; 1k/10k -> 11 | calc/sim | p.640-641, Fig. 8.11-8.12 | high |
| SCHERZ-2047 | components | Bias-current compensation resistor from +input to ground equal to the dc resistance seen by -input: inverting amp R1\|\|R2; noninverting set R1\|\|R2 = Rsource; follower Rf = Rsource; summer = parallel of all input R (and feedback); integrator = Rin\|\|R_dc-feedback; differentiator = Rf. Needed with bipolar (nA) op amps, unnecessary with FET (pA) | Rcomp = R1*R2/(R1+R2); uncompensated error Vout_err = Ibias*(R1\|\|R2)*(R2/R1) | R1, R2, Ibias | e.g. R1 = 10k, R2 = 100k -> Rcomp = 9.1k | calc | p.640-644, 651, Fig. 8.26 | high |
| SCHERZ-2048 | control-loop | Inverting summing amplifier output | Vout = -(R3/R1*V1 + R3/R2*V2); R1 = R2 = R3 -> Vout = -(V1+V2); add inverting stage for positive sum | V1, V2, R1-R3 | Ideal op amp | calc | p.642, Fig. 8.13 | high |
| SCHERZ-2049 | control-loop | Difference amplifier (matched R1/R2 pairs on both inputs) | Vout = (R2/R1)*(V2 - V1); R1 = R2 -> V2 - V1 | V1, V2, R1, R2 | Resistor matching sets CMRR | calc | p.642, Fig. 8.14 | high |
| SCHERZ-2050 | control-loop | Integrator must have a large resistor across the capacitor for dc feedback (otherwise output drifts from offset/bias even with input grounded) | Vout = -(1/(R*C)) * integral(Vin dt); example Rin = 10k, C = 1 uF, R_dc = 10 Mohm | R, C, R_dc | Plus bias comp Rin\|\|R_dc | sim | p.643, Fig. 8.15 | high |
| SCHERZ-2051 | control-loop | Practical differentiator: add series input resistor and feedback capacitor to roll off high-frequency noise gain and cancel the 90-deg loop lag; above the roll-off it becomes an integrator | Vout = -R*C*dVin/dt; example C = 0.1 uF, R = 100k, R_in = 1k, C_f = 100 pF | R, C, R_in, C_f | Pure RC differentiator is noise-prone and may oscillate | sim | p.643-644, Fig. 8.16 | high |
| SCHERZ-2052 | control-loop | Op-amp comparator with positive feedback (R1 input, R2 feedback) has thresholds set by saturation voltage and R1/R2 | +/-VT = +/-Vsat*R1/R2; Vh = +VT - (-VT); example Vsat = 15 V, R1 = 10k, R2 = 100k -> +/-1.5 V, Vh = 3 V | Vsat, R1, R2 | Dual-supply op amp | calc | p.644-645, Fig. 8.17 | high |
| SCHERZ-2053 | components | JFET-input op amps can phase-invert (feedback becomes positive, latch-up) when input common-mode approaches the negative supply; restrict common-mode range or use bipolar input | Vcm > Vneg + (datasheet CM limit) | Vcm_min | JFET op amps | calc | p.646 | high |
| SCHERZ-2054 | components | Programmable (Iset) op amps trade quiescent current against slew rate, GBW, bias current and noise (roughly proportional to Iset); supply current settable from a few uA to a few mA; LM4250 runs from 1 V | Iq = few uA..few mA | Iset resistor | Battery-powered analog | review | p.646, Fig. 8.20 | high |
| SCHERZ-2055 | components | Single-supply op amps accept inputs down to the negative rail (ground) but the output cannot go negative - not usable for ac-coupled signals without a mid-supply bias | Vout >= 0 V | signal polarity | Single-supply designs | review | p.647, Fig. 8.21 | high |
| SCHERZ-2056 | components | LM386 audio amp: gain internally 20, raise to 200 with R-C across pins 1-8; drives 8-ohm speaker; single supply +4 to +12 V. LM383: 3.5-A power amp for 4-ohm load (or two 8-ohm in parallel), thermal shutdown, needs heat sink | G = 20..200; Vs = 4..12 V (LM386) | gain, load, supply | Audio band 20-20,000 Hz | review | p.647, Fig. 8.22 | high |
| SCHERZ-2057 | components | Slew rate limits large fast swings: 741 0.5 V/us vs HA2539 600 V/us; check full-power bandwidth | SR >= 2*pi*f*Vpeak (sine; derived from slew-rate definition) | f (Hz), Vpeak (V), SR (V/us) | Sine output | calc | p.648 §8.7 | medium |
| SCHERZ-2058 | control-loop | Unity-gain frequency fT typically ~1 MHz (1-10 MHz); open-loop gain falls 20 dB/dec above fB; closed-loop bandwidth widens as gain drops (Fig. 8.27: fT = 1 MHz, G = 100 -> ~10 kHz, G = 10 -> ~100 kHz) | f_CL ~ fT/G_CL (graph-derived) | fT (Hz), G_CL | Internally compensated op amp | calc | p.648, 652, Fig. 8.27 | medium |
| SCHERZ-2059 | control-loop | Stability: if internal phase shift reaches 180 deg while loop gain > 1 (open-loop slope steeper than 40-60 dB/dec near fT) the amp oscillates; use internally compensated op amps or the datasheet RC compensation network | phase(A*beta) < 180 deg at \|A*beta\| = 1 | open-loop Bode | Uncompensated op amps | sim | p.652, Fig. 8.27 | high |
| SCHERZ-2060 | power | Single-supply ac-coupled amplifier with conventional op amp: bias noninverting input at Vs/2 with equal divider (e.g. 56k/56k) for maximum symmetric swing; input and output coupling capacitors sized from the -3 dB frequency; stay within op-amp minimum supply, output swing and input common-mode range | Vbias = Vs/2; C1 = 1/(2*pi*f3dB*R1); C3 = 1/(2*pi*f3dB*Rload) | Vs, f3dB, R1, Rload | Audio example: C1 1 uF, C3 10 uF, R3 10k, R4 100k | calc | p.649-650, Fig. 8.24 | high |
| SCHERZ-2061 | protection | Never reverse op-amp supply leads; add a series diode in the negative supply lead for reverse-polarity protection | series diode in -Vs | schematic | Op-amp supplies | inspect | p.650, Fig. 8.25 | high |
| SCHERZ-2062 | decoupling | Bypass each op-amp supply pin to ground with 0.1-uF disk (ceramic) or 1.0-uF tantalum; keep supply leads short and direct to prevent oscillation/noise | C_byp = 0.1 uF ceramic or 1 uF tantalum per rail | schematic, layout | All op amps | inspect | p.650, Fig. 8.25 | high |
| SCHERZ-2063 | protection | Inputs must never exceed the rails by more than 0.7 V (including signal present before power-up) or internal current reversal shorts the supplies (destructive latch-up); clamp at-risk inputs to the rails with fast low-Vf Schottky diodes plus series current-limit resistors (diode leakage adds error) | -Vs - 0.7 V <= Vin <= +Vs + 0.7 V | Vin range incl. power sequencing | Bipolar and JFET op amps | calc | p.650-651, Fig. 8.25 | high |
| SCHERZ-2064 | test | Offset-null trim: pot (10k in Fig. 8.26) across the offset-null pins, wiper to the more negative supply; short inputs and adjust until output ~0 V | Vout -> 0 | - | 741-style op amps; offset typically uV to mV | measure | p.651, Fig. 8.26 | high |
| SCHERZ-2065 | components | Do not use comparator ICs with negative feedback or as linear amplifiers (not frequency compensated); they have higher slew rate/lower delay; open-collector output needs a pull-up of a few hundred to a few thousand ohms (1k typical), large enough to limit dissipation, small enough to drive the load | Rpull-up ~ 100s ohm..few kohm | load current, supply | Comparator ICs (e.g. LT1011) | review | p.652-653, Fig. 8.29 | high |
| SCHERZ-2066 | components | Not all op amps work as comparators with a grounded negative supply; prefer a dedicated comparator IC for single-supply comparison | - | op-amp datasheet | Single-supply comparators | review | p.653 | high |
| SCHERZ-2067 | control-loop | Add hysteresis (positive feedback) to any comparator watching a slowly varying or noisy signal near its threshold to stop output chatter | Vh > peak noise at threshold (low: quantified from text intent) | noise amplitude | Comparators | sim | p.654 §8.13 | low |
| SCHERZ-2068 | control-loop | Inverting comparator with hysteresis (R1 from Vs to +in, R2 +in to gnd, R3 feedback from output): design procedure | Vref1 = Vs*R2*(R1+R3)/(R1R2+R1R3+R2R3); Vref2 = Vs*R2*R3/(R1R2+R1R3+R2R3); dVref = Vs*R1*R2/(R1R2+R1R3+R2R3); design: n = dVref/Vref2, R1 = n*R3, R2 = (R1\|\|R3)/((Vs/Vref1) - 1) | Vref1, Vref2, Vs, R3 | Example Vref1 = 6 V, Vref2 = 5 V, Vs = 15 V, Rload 100k, Rpull-up 3k, R3 1M -> n = 0.2, R1 = 200k, R2 = 111k | calc | p.654-655, Fig. 8.30 | high |
| SCHERZ-2069 | control-loop | Hysteresis loading rule: pull-up must be much lighter than the load and the feedback resistor larger than the pull-up (heavier loading lowers Voh and shrinks hysteresis) | Rpull-up < Rload; R_fb > Rpull-up | Rpull-up, Rload, R_fb | Open-collector comparators | calc | p.655 | high |
| SCHERZ-2070 | control-loop | Noninverting comparator with hysteresis (R1 input-to-+in, R2 feedback): thresholds and design | Vin1 = Vref*(R1+R2)/R2; Vin2 = (Vref*(R1+R2) - Vcc*R1)/R2; dVin = Vcc*R1/R2; design R1/R2 = dVin/Vcc, Vref = Vin1/(1 + R1/R2) | Vin1, Vin2, Vcc | Example Vin1 = 8 V, Vin2 = 6 V, Vcc = 10 V, Rpull-up 1k, R2 1M -> R1 = 200k, Vref = 6.7 V | calc | p.655, Fig. 8.31 | high |
| SCHERZ-2071 | control-loop | Window comparator: two open-collector comparators wire-ORed with one pull-up (1k to +5 V); output high only for Vref,low < Vin < Vref,high | example window 3.5-6.5 V | Vref_low, Vref_high | Single-supply quad (LM3302) or dual comparators | sim | p.656, Fig. 8.33 | high |
| SCHERZ-2072 | control-loop | Three-op-amp instrumentation amplifier gain; the two R1 must be matched; Rg alone sets gain; prefer integrated in-amp with trimmed resistors for CMRR | G = (1 + 2*R1/Rg)*(R3/R2); Rg open -> G = R3/R2 (unity if R3 = R2) | R1, Rg, R2, R3 | ECG-type small differential signals | calc | p.657, Fig. 8.35 | high |
| SCHERZ-2073 | hw-fw | Comparator-to-logic interface: open-collector pull-up 10k to +5 V for TTL inputs; 100k to +3..15 V for CMOS inputs | Rpu = 10k (TTL), 100k (CMOS) | logic family | Comparator outputs | inspect | p.658, Fig. 8.38 | high |
| SCHERZ-2074 | components | Op-amp driving a bipolar power switch: base resistor (~1k) plus a diode protecting the transistor from reverse base-emitter breakdown when the op-amp output swings negative; use transistor with proper power rating (or power MOSFET) | R_base ~ 1k; reverse-BE diode | load current | Split-supply op amp drivers | inspect | p.658, Fig. 8.36 | medium |
| SCHERZ-2075 | control-loop | Op-amp power booster: complementary push-pull pair inside the feedback loop; at high speed add bias network to limit crossover distortion (feedback removes most at low speed) | - | f, load | Bipolar output swing boost | sim | p.658, Fig. 8.39 | medium |
| SCHERZ-2076 | control-loop | Op-amp voltage-to-current converter (load in feedback path) | Iout = Vin/R2; Vout = Vin*(RL + R2)/R2 (must stay within output swing) | Vin, R2, RL | Floating load | calc | p.658, Fig. 8.40 | high |
| SCHERZ-2077 | control-loop | Precision current sink (op amp + JFET + bipolar): Iload = Vin/R2; accurate only for Iload > JFET IDS(on) and Vin > 0; size pass transistor power for the load; Darlington acceptable if its base current error is tolerable | Iload = Vin/R2; P_Q = Vce*Iload | Vin, R2, Vce | Precision current sources | calc | p.659 | high |
| SCHERZ-2078 | control-loop | Transimpedance (current-to-voltage) amplifier for photodiodes/photoresistors/phototransistors | Vout = Iin*RF (e.g. RF = 100k) | Iin, RF | Light sensors | calc | p.659, Fig. 8.41 | high |
| SCHERZ-2079 | protection | Crowbar overvoltage protection: comparator compares a divided rail against a zener reference (6 V rail -> 3 V at +in vs 3-V zener) and fires an SCR across the rail to blow the fuse/breaker; reset by interrupting SCR current | trip when k*Vrail > Vz | Vrail, divider k, Vz | Protect sensitive loads from supply surges | sim | p.660, Fig. 8.42 | high |
| SCHERZ-2080 | control-loop | Digitally programmable gain: CMOS quad bilateral switch (4066, +5 to +18 V) selects feedback resistors of an inverting amp; closed switches put resistors in parallel | G = -(Ra\|\|Rb\|\|...)/R1 for closed switches | switch states, R | Include switch on-resistance in gain error | calc | p.660, Fig. 8.43 | high |
| SCHERZ-2081 | components | Sample-and-hold: hold capacitor on a buffer with low input bias current (FET op amp); use Teflon, polyethylene or polycarbonate hold capacitors; droop set by leakage | droop dV/dt = I_leak/C_hold | I_leak, C | S/H, ADC front ends | calc | p.661, Fig. 8.44 | high |
| SCHERZ-2082 | control-loop | Peak detector: diode + hold capacitor (1 uF example) + buffer; add a second op amp around the diode to cancel its ~0.6-V drop; provide reset switch/FET; smaller C responds faster | V_hold = Vpeak (active) or Vpeak - 0.6 V (passive) | C, reset | Envelope/peak capture | sim | p.661, Fig. 8.45 | high |
| SCHERZ-2083 | control-loop | Active (precision) rectifier rectifies signals below one diode drop (down to 0 V); passive diode loses ~0.6 V and cannot rectify < 0.6 V; output inverted - add buffer/inverting buffer | Vout = -Vin for Vin > 0, 0 for Vin < 0 (R1 = R2 = 10k) | Vin amplitude | Small-signal rectification | sim | p.662, Fig. 8.47 | high |
| SCHERZ-2084 | protection | Zener clipper in op-amp feedback limits output to the zener breakdown voltage (both polarities with back-to-back zeners) - overload limiter or sine-to-square converter | \|Vout\| <= BVz | BVz | Audio overload limiting | sim | p.662, Fig. 8.46 | high |
| SCHERZ-2085 | filter | Technology choice by frequency: passive RLC filters are practical from ~100 Hz to ~300 MHz (below: huge L/C; above: parasitics); active (op-amp RC) filters work down to ~0 Hz and give gain but become unreliable above ~100 kHz (op-amp bandwidth/slew); use passive filters at RF | passive: 100 Hz <= f <= 300 MHz; active: f <= ~100 kHz | filter corner/stop frequencies | General filter architecture | review | p.664 §9 intro | high |
| SCHERZ-2086 | filter | Filter band definitions: cutoff = -3 dB (half power, 1/sqrt(2) voltage); passband = <= 3 dB attenuation; bandpass center is the geometric mean of the -3 dB points, arithmetic mean acceptable only when f2/f1 < 1.1 | f0 = sqrt(f1*f2); if f2/f1 < 1.1: f0 ~ (f1+f2)/2; Q_bp = f0/(f2 - f1) | f1, f2 (Hz) | Bandpass/notch specification | calc | p.665 §9.1 | high |
| SCHERZ-2087 | filter | First-order RC/RL sections and single LC resonators roll off only 6 dB/octave beyond the -3 dB point; use them only when unwanted signals are far from cutoff | fc = 1/(2*pi*R*C); fc = R/(2*pi*L); f0 = 1/(2*pi*sqrt(L*C)); slope 6 dB/oct | R, L, C | Basic filters (Fig. 9.3) | calc | p.665-666, Fig. 9.3 | high |
| SCHERZ-2088 | filter | Filter order from requirement: compute steepness factor As, then pick the lowest Butterworth order whose normalized curve (Fig. 9.6) meets the stop-band attenuation at As rad/s; Butterworth ultimate slope n x 6 dB/octave | LP: As = fs/f3dB; HP: As = f3dB/fs; slope -> 6n dB/oct (n = 3 -> 18 dB/oct) | f3dB, fs, A_stop (dB) | Examples: As = 3, -25 dB -> n = 3; As = 3.3, -45 dB -> n = 5; As = 4, -60 dB -> n = 5; As = 3.3, -50 dB -> n = 5; As = 3.3, -30 dB -> n = 3; book also picks n = 3 for -20 dB at As = 1.88 and 1.7, which exact Butterworth math does not meet (see Table S2-9.3) | calc | p.667-668, 671, 676-679, Fig. 9.6 | high |
| SCHERZ-2089 | filter | Response family choice: Butterworth = maximally flat passband, rounded knee, least tolerance-sensitive; Chebyshev = steepest transition but passband ripple (0.1/0.5 dB) growing with order and more tolerance-sensitive; Bessel = constant group delay (no delay distortion of multi-frequency/modulated signals) but slowest roll-off; delay distortion of Butterworth/Chebyshev grows with order | - | signal type (waveform fidelity vs selectivity) | Pulse/modulated signals -> Bessel | review | p.670 §9.4 | high |
| SCHERZ-2090 | filter | Passive LC ladder topology: equal source/load -> either (pi preferred, fewer inductors); RL > Rs -> T network; RL < Rs -> pi network; for high-pass designs start from a T low-pass prototype so the transformed HP has fewer inductors | - | Rs, RL | Passive LC ladders | review | p.668, 671 | high |
| SCHERZ-2091 | filter | Passive LC scaling from normalized (1 ohm, 1 rad/s) Butterworth table values | L_actual = RL*L_table/(2*pi*f3dB); C_actual = C_table/(2*pi*f3dB*RL) | table values, RL (ohm), f3dB (Hz) | Example LP f3dB = 3 kHz, 50 ohm, n = 3: L2 = 5.3 mH, C1 = C3 = 1.06 uF | calc | p.669, Table 9.1, Fig. 9.8-9.9 | high |
| SCHERZ-2092 | filter | Low-pass -> high-pass transformation of normalized prototype: each L becomes C = 1/L, each C becomes L = 1/C, then frequency/impedance scale | C_hp = 1/L_lp; L_hp = 1/C_lp | normalized values | Example HP f3dB = 1 kHz, -45 dB at 300 Hz, 50 ohm, n = 5: C1 = C5 = 5.1 uF, C3 = 1.6 uF, L2 = L4 = 4.9 mH | calc | p.670-671, Fig. 9.10 | high |
| SCHERZ-2093 | filter | Bandpass/notch class: wide-band if f2/f1 > 1.5 (cascade LP and HP; for notch, sum LP and HP outputs); narrow-band if f2/f1 < 1.5 (transform method, or dedicated narrow-band circuit) | f2/f1 > 1.5 -> wide; < 1.5 -> narrow | f1, f2 | Passive and active | calc | p.672, 678, 680 | high |
| SCHERZ-2094 | filter | Narrow-band passive bandpass: design LP prototype with f3dB = BW = f2 - f1 and stop frequency from the tightest geometric stop-band pair; scale by 2*pi*BW; then resonate each branch at f0 (series C with each L, parallel L with each C) | fa*fb = f0^2; As = (stop-band BW)/(3-dB BW); L_par = 1/((2*pi*f0)^2*C); C_ser = 1/((2*pi*f0)^2*L) | f1, f2, stop freqs, RL | Example f1 = 900, f2 = 1100 Hz, -20 dB at 800/1200 Hz, 50 ohm: f0 = 995 Hz, As = 375/200 = 1.88, n = 3, C = 15.92 uF, L = 79.6 mH, L_par = 1.61 mH, C_ser = 0.32 uF | calc | p.672-674, Fig. 9.12 | high |
| SCHERZ-2095 | filter | Narrow-band passive notch: same procedure with a high-pass prototype scaled to BW, As = (3-dB BW)/(stop-band BW), then resonate branches at f0 | As = BW3dB/BWstop; component resonance at f0 | f1, f2, stop freqs, RL | Example f1 = 800, f2 = 1200 Hz, -20 dB at 900/1100 Hz, 600 ohm: f0 = 980 Hz, As = 400/227 = 1.7, n = 3, L1 = L3 = 0.24 H, C2 = 0.33 uF, C_ser = 0.11 uF, L_par = 80 mH | calc | p.674-675, Fig. 9.13 | high |
| SCHERZ-2096 | filter | Active Butterworth (unity-gain 2-pole/3-pole sections, normalized 1-ohm resistors): cascade sections from Table 9.2 and scale; choose impedance factor Z (typically 10 kohm) to get practical values | C_actual = C_table/(Z*2*pi*f3dB); R_actual = Z*R_table | table values, f3dB, Z | Example LP f3dB = 100 Hz, -60 dB at 400 Hz, n = 5, Z = 10k: 3-pole 0.28/0.22/0.07 uF + 2-pole 0.52/0.05 uF, all R = 10k | calc | p.676-677, Table 9.2, Fig. 9.14-9.15 | high |
| SCHERZ-2097 | filter | Active low-pass -> high-pass transform: replace each normalized R with C = 1/R (F) and each C with R = 1/C (ohm), then scale with Z | C_hp = 1/R_lp; R_hp = 1/C_lp | normalized values | Example HP f3dB = 1 kHz, -50 dB at 300 Hz, n = 5, Z = 10k: R = 5.7k, 7.4k, 23.7k; 3.1k, 32.4k; C = 1/(Z*2*pi*1000) = 15.9 nF (figure prints 0.16 uF - see pitfalls) | calc | p.677-678, Fig. 9.16-9.17 | high |
| SCHERZ-2098 | filter | Wide-band active bandpass = cascade of active LP (upper corner) and HP (lower corner) sections designed separately | each section As from its own corner | f1, f2, stop specs | Example 1-3 kHz, -30 dB at 300 Hz and 10 kHz: n = 3 each, Z = 10k: LP caps 18 nF, 7.38 nF, 1.07 nF; HP caps 15.9 nF, R 2820, 7180, 49.4k | calc | p.678-679, Fig. 9.18 | high |
| SCHERZ-2099 | filter | Narrow-band active bandpass (multiple-feedback, equal C): design equations; R2 may be a trimmer for tuning | Q = f0/(f2 - f1); R1 = Q/(2*pi*f0*C); R2 = R1/(2*Q^2 - 1); R3 = 2*R1 | f0, BW, C | f2/f1 < 1.5; printed example arithmetic inconsistent (see pitfalls) | calc | p.679-680, Fig. 9.19 | high |
| SCHERZ-2100 | filter | Twin-T passive notch gives a deep null but Q of only 1/4; for higher Q use the bootstrapped active notch: R1 = 1/(2*pi*f0*C), feedback divider K = (4Q - 1)/(4Q) with a trim pot | Q_twinT = 1/4; R1 = 1/(2*pi*f0*C); K = (4Q-1)/(4Q) | f0, BW, C, R | Example f0 = 2 kHz, BW = 100 Hz -> Q = 20; C = 0.01 uF, R = 10k -> R1 = 7961 ohm, K = 0.9875 | calc | p.680-681, Fig. 9.21-9.22 | high |
| SCHERZ-2101 | filter | Wide-band active notch: sum a low-pass (lower corner) and a high-pass (upper corner) with an inverting summer, R = 10k typical | - | f1, f2 | Example -3 dB at 500 and 5000 Hz, -15 dB at 1000 and 2500 Hz | calc | p.680, Fig. 9.20 | high |
| SCHERZ-2102 | filter | State-variable filter IC (AF100/AF150) gives LP, HP, BP, notch simultaneously with gain; LP gain = -R1/Rin, HP gain = -R2/Rin; Q per manufacturer formulas | G_LP = -R1/Rin; G_HP = -R2/Rin | R1, R2, Rin | 2nd-order sections cascaded for higher order | calc | p.681-682, Fig. 9.23 | high |
| SCHERZ-2103 | filter | Switched-capacitor filter (MF5): corner set by clock; gains set by resistors; MF4 (4th-order) and MF6 (6th-order) Butterworth LP need only a clock | f0 = (fclk/50)*sqrt(R2/R4); Q = (R3/R2)*sqrt(R2/R4); G_LP = -R4/R1; G_BP = -R3/R1; G_HP = -R2/R1 (radicals inferred from OCR-garbled text) | fclk, R1-R4 | Digitally tunable filters | calc | p.682, Fig. 9.24 | medium |
| SCHERZ-2104 | filter | Switched-capacitor filters inject clock feedthrough of about 10-25 mV at fclk into the output; add a simple RC post-filter | V_clk_noise ~ 10-25 mV | fclk, signal band | SC filter outputs | measure | p.682 | high |
| SCHERZ-2105 | timing | Op-amp square-wave relaxation oscillator with R2 = R3 (thresholds +/-Vsat/2) | T = 2.2*R1*C (f = 1/(2.2*R1*C)); VT = Vsat*R3/(R2+R3) = +/-7.5 V at +/-15 V | R1, C, R2, R3 | Example R2 = R3 = 15k, C = 100 uF | calc | p.684, Fig. 10.2 | high |
| SCHERZ-2106 | timing | PUT sawtooth generator (integrator + 2N6027 PUT reset): frequency set by Vref, R3, C and PUT peak voltage (typ. PUT drop 0.5 V) | f = (Vref/(R3*C)) * 1/(Vp - 0.5 V); example f = 45 Hz (R3 = 20k, C = 0.2 uF) | Vref, R3, C, Vp | Diodes stabilize Vref adjustment; amplitude set by R4 | calc | p.684-685, Fig. 10.3 | high |
| SCHERZ-2107 | timing | Dual-op-amp triangle/square generator (integrator + hysteresis comparator); Vsat is ~1 V below the supply | VT = Vsat*(R2/R3) (printed OCR "Vsat (R3 - R2)"); T = 4*VT*R1*C/Vsat | R1, R2, R3, C, Vsat | Example C = 0.1 uF, R1 = R2 = 10k, R3 = 100k, +/-15 V | calc | p.685, Fig. 10.4 | medium |
| SCHERZ-2108 | timing | UJT relaxation oscillator | f = 1/(RE*CE*ln(1/(1 - eta))), eta (intrinsic standoff) ~ 0.5 | RE, CE, eta | Example R = 100k, C = 0.2 uF, 10 V, 100-ohm base resistors | calc | p.685-686, Fig. 10.5 | high |
| SCHERZ-2109 | timing | Schmitt-trigger inverter RC oscillator: on/off times set by RC and the positive/negative-going thresholds (e.g. 1.7 V and 0.9 V at 5 V CMOS) - thresholds vary by part, so frequency tolerance is poor | t = R*C*ln(...) of thresholds | R, C, VT+, VT- | Simple clocks | measure | p.686, Fig. 10.5 | medium |
| SCHERZ-2110 | timing | Two-CMOS-inverter RC oscillator (4-18 V supply) | f = 1/(4*R*C*ln 2) ~ 1/(2.8*R*C); example R = 100k, C = 200 pF | R, C | CMOS inverters | calc | p.686, Fig. 10.5 | high |
| SCHERZ-2111 | timing | 555 electrical limits: output sinks/sources ~200 mA; Voh ~ VCC - 1.5 V, Vol ~ 0.1 V; thresholds 1/3 and 2/3 VCC; bipolar VCC 4.5-16 V (CMOS versions down to ~1 V); reset (pin 4) active low | Iout <= 200 mA; Voh = VCC - 1.5 V | load current, VCC | Bipolar 555 (NE/SN555) | calc | p.687, Fig. 10.6 | high |
| SCHERZ-2112 | timing | 555 astable timing (R1 VCC-to-pin 7, R2 pin 7-to-pins 6/2, C1 to ground) | t_low = 0.693*R2*C1; t_high = 0.693*(R1+R2)*C1; f = 1.44/((R1 + 2*R2)*C1); duty = t_high/(t_high + t_low) (always > 0.5) | R1, R2, C1 | Example VCC 6 V, R1 10k, R2 20k, C1 680 nF -> 9.4 ms / 14.1 ms, 42 Hz, duty 0.6 | calc | p.688, Fig. 10.7 | high |
| SCHERZ-2113 | timing | 555 timing component limits for reliable operation (astable and monostable) | 10 kohm <= R <= 14 Mohm; 100 pF <= C <= 1000 uF | R, C | 555 timers | calc | p.688, 690 | high |
| SCHERZ-2114 | timing | 555 duty cycle < 50 %: diode across R2 so C1 charges through R1 only; then make R1 < R2 | t_high = 0.693*R1*C1; t_low = 0.693*R2*C1 | R1, R2, C1 | Example R1 10k, R2 47k, C1 1 uF -> 6.9 ms / 32.5 ms, 25 Hz, duty 0.18 | calc | p.688-689, Fig. 10.8 | high |
| SCHERZ-2115 | timing | 555 monostable: trigger pin 2 held high by 10k pull-up and pulsed below 1/3 VCC; output pulse width | t_width = 1.10*R1*C1; example R1 15k, C1 1 uF -> 16.5 ms | R1, C1 | One-shot / delay timer (also relay delay t_delay = 1.10*R1*C1) | calc | p.689-691, Fig. 10.9-10.12 | high |
| SCHERZ-2116 | decoupling | 555 false-trigger prevention: pin 5 (control) to ground through 0.01 uF; add >= 0.1 uF directly across pins 8-1 when the supply lead is long or the timer misbehaves | C_pin5 = 0.01 uF; C_8-1 >= 0.1 uF | schematic/layout | All 555 designs | inspect | p.687, 691 (Practical Tip) | high |
| SCHERZ-2117 | components | CMOS 555 (part number contains C: ICL7555, TLC555, LMC555) beats bipolar 555 on supply voltage/current, trigger current and speed, but not on output current (e.g. ICL7555 source 4 mA / sink 25 mA vs 200 mA bipolar) | see Table S2-10.1 | load current, supply | Timer selection | review | p.690, Table 10.1 | high |
| SCHERZ-2118 | protection | 555 driving a relay: add diodes to suppress relay switching surges that damage the 555 and relay contacts (output ~10.5 V at VCC = 12 V; use 6-9 V low-ohm relay) | flyback diode across coil + series diode | relay coil | Delay timer | inspect | p.691, Fig. 10.12 | high |
| SCHERZ-2119 | timing | NE566 VCO: frequency set by R1, C1 and control voltage on pin 5; control voltage and R1 must stay in range | f = 2*(VCC - Vin)/(R1*C1*VCC); 0.75*VCC <= VC <= VCC; 2 kohm < R1 < 20 kohm | VCC, Vin, R1, C1 | Example VCC 12 V, R1 10k, C1 0.001 uF | calc | p.692, Fig. 10.14 | high |
| SCHERZ-2120 | timing | Wien-bridge oscillator: oscillates at f0 with noninverting gain exactly 3 (R3/R4 = 2); lower gain stops oscillation, higher gain saturates - use amplitude control (back-to-back zeners, e.g. 1N4739 9.1 V, across part of the negative-feedback resistor) | f0 = 1/(2*pi*R*C); R3/R4 = 2 (gain = 3) | R, C, R3, R4 | Example R = 100k, C = 318-1590 pF ganged -> 1-5 kHz | calc | p.693, Fig. 10.15 | high |
| SCHERZ-2121 | timing | LC oscillators reach ~500 MHz but are unwieldy at audio frequencies; op-amp amplifiers become unreliable above ~100 kHz - use a transistor amplifier (special RF transistors to ~2000 MHz) with phase correction for the inverting stage | f_LC <= ~500 MHz; op-amp oscillator <= ~100 kHz | target frequency | Sinusoidal oscillators | review | p.693-694 | high |
| SCHERZ-2122 | timing | Hartley oscillator (tapped inductor) frequency | f = 1/(2*pi*sqrt(LT*CT)); LT = L1 + L2 | L1, L2, CT | JFET or bipolar; RFC in supply feed | calc | p.695, Fig. 10.17 | high |
| SCHERZ-2123 | timing | Colpitts oscillator (capacitive divider) frequency; better stability than Hartley | f = 1/(2*pi*sqrt(L*Ceff)); Ceff = C1*C2/(C1+C2) (tank caps; C3 = 500 pF, C4 = 5000 pF, L = 20 mH in example) | L, tank caps | Permeability- or capacitor-tuned tank | calc | p.695-696, Fig. 10.18 | high |
| SCHERZ-2124 | timing | Clapp oscillator: make C1, C2 >> CT so strays are swamped and frequency is set almost entirely by LT, CT (exceptional stability) | Ceff = 1/(1/C1 + 1/C2 + 1/CT) ~ CT; f = 1/(2*pi*sqrt(LT*Ceff)) | LT, CT, C1, C2 | Stable LC VFOs | calc | p.696, Fig. 10.19 | high |
| SCHERZ-2125 | timing | Frequency stability by oscillator class: crystal 0.01-0.001 %; LC ~0.01 % at best; RC ~0.1 %; crystal Q ~100,000 vs LC Q of a few hundred | stability: XO 1e-4..1e-5; LC 1e-4; RC 1e-3 | required accuracy | Oscillator selection | review | p.696 §10.6 | high |
| SCHERZ-2126 | timing | Crystal equivalent circuit (motional L1, C1, R1 with holder C0): series resonance fs = impedance minimum (R1 only), parallel resonance fp = impedance maximum | 1 MHz: L1 = 3.5 H, C1 = 0.007 pF, R1 = 340 ohm, C0 = 3 pF; 10 MHz fund.: L1 = 9.8 mH, C1 = 0.026 pF, R1 = 7 ohm, C0 = 6.3 pF | crystal model | Crystal oscillator simulation | sim | p.697, Fig. 10.20 | high |
| SCHERZ-2127 | timing | Crystal cut/type: fundamental crystals ~10 kHz-30 MHz; overtone crystals (odd multiples: 3rd, 5th, 9th...) up to a few hundred MHz; order series-mode vs parallel-mode to match the circuit | f_fund <= 30 MHz; overtone = odd n x f_fund | target frequency | Crystal selection | review | p.697, Fig. 10.21 | high |
| SCHERZ-2128 | timing | Standard crystal frequencies 100 kHz, 1, 2, 4, 5, 8, 10 MHz; packaged oscillator modules 1, 2, 4, 5, 6, 10, 16, 24, 25, 50, 64 MHz | - | clock plan | Prefer standard values | review | p.697-698 | high |
| SCHERZ-2129 | timing | Crystal oscillator topologies: Pierce (JFET, crystal series-resonant drain-gate feedback), Colpitts (crystal parallel-resonant), CMOS-inverter (series-resonant, e.g. 10M bias resistor, 1-20 MHz) | - | circuit | 1-20 MHz typical | review | p.698, Fig. 10.22 | medium |
| SCHERZ-2130 | hw-fw | Where only a square wave is needed, a small 8-pin microcontroller with internal clock can replace a 555 with fewer external parts; arbitrary waveforms via stored table + DAC | - | - | Timer replacement | review | p.698 §10.7 | low |
| SCHERZ-2131 | power | Do not run sensitive (e.g. digital IC) circuits from an unregulated transformer-rectifier-capacitor supply: line spikes pass through and the output droops with load; add a regulator with a 0.1-uF output bypass | regulated rail required for logic | supply topology | Linear supplies | review | p.699-700, Fig. 11.1-11.2 | high |
| SCHERZ-2132 | power | 78xx/79xx fixed regulators: outputs 5, 6, 8, 10, 12, 15, 18, 24 V (79xx negative); max 1.5 A only when properly heat-sunk; SMD versions (SOT-89) have lower current - check datasheet; input cap 1-10 uF, output cap 0.01-0.1 uF | Iout <= 1.5 A (TO-220, heat-sunk); Cin = 1-10 uF; Cout = 0.01-0.1 uF | Iload, package | Fixed linear rails | calc | p.701, Fig. 11.4 | high |
| SCHERZ-2133 | power | LM317 adjustable regulator output (1.25-V reference between OUT and ADJ): Vin up to 37 V, 1.5 A, output 1.25-37 V; LM337 negative -1.2 to -37 V, 1.5 A (input -1.5 to -38 V); TL783 1-125 V, 700 mA; Cin ~0.1 uF if far from the source, Cout >= 0.1 uF | Vout = 1.25 V*(1 + R2/R1) (LM337: -1.25 V*(1 + R2/R1)) | R1, R2, Vin | Adjustable linear rails | calc | p.702, Fig. 11.5 | high |
| SCHERZ-2134 | power | Linear regulator headroom: 78xx and LM317 need input at least 2 V above output (p.702); the 7805 example uses >= 3 V (8 V in for 5 V out) (p.708); LDO types (e.g. LM2940) need as little as 0.5 V and run cooler | Vin_min >= Vout + 2 V (use 3 V for 7805 per p.708); LDO: Vout + 0.5 V | Vin_min at ripple trough, Vout | Linear regulators | calc | p.702, 708 | high |
| SCHERZ-2135 | power | Transformer secondary selection: not much higher than needed (excess is dissipated in the regulator) but the rectified, rippled minimum must stay >= regulator minimum input (typically 2-3 V above output) after the rectifier drop (typically 1-2 V); e.g. 12-V secondary for a 5-V/7805 supply | V_sec_peak - V_rect(1-2 V) - Vripple_pk >= Vout + 2..3 V | V_sec, rectifier type, ripple | Transformer-input linear supplies | calc | p.703, 708 | high |
| SCHERZ-2136 | components | Rectifier ratings: check current, PIV and surge; typical rectifier diodes 1-25 A, PIV 50-1000 V, surge 30-400 A; Schottky rectifiers < 0.4 V drop but much lower breakdown | I_F >= I_load (avg) with margin; PIV >= reverse peak; I_FSM >= inrush | I_avg, V_rev_peak, inrush | Supply rectifiers | calc | p.704 §11.4 | high |
| SCHERZ-2137 | components | Common rectifier parts: 1N4001-1N4007 1 A, 0.9 V; 1N5059-1N5062 2 A, 1.0 V; 1N5624-1N5627 5 A, 1.0 V; 1N1183A-90A 40 A, 0.9 V; bridges 3N246-3N252 1 A, 0.9 V and 3N253-3N259 2 A, 0.85 V | see Table S2-11.1 | current | Part selection | review | p.704 | high |
| SCHERZ-2138 | protection | Put a reverse diode across a linear regulator (output to input) so a slowly discharging output capacitance cannot reverse-bias the regulator at power-off; protect with a line fuse (1.5 A in the examples) | diode OUT->IN (1N4004/1N5400 class) | output capacitance vs input | 78xx/79xx/LM317 supplies | inspect | p.704-706, Fig. 11.9-11.10 | high |
| SCHERZ-2139 | power | Dual-polarity LM317/LM337 bench supply: 48 VAC CT (24-0-24) transformer is the practical upper limit (regulator max input and 35-VDC bulk capacitors); film bypass caps across electrolytics; 10-uF ADJ bypass raises ripple rejection 65 -> 80 dB | V_sec_CT <= 48 VAC (24-0-24); bulk caps >= 35 VDC | transformer, cap rating | +/-1.2-35 V, up to 1.5 A | calc | p.705-706, Fig. 11.10a | high |
| SCHERZ-2140 | power | Supply tolerance targets: digital 5-V rails vary no more than 5 % (0.25 V); logic typically has >= 200 mV noise margin; small-signal analog may need < 1 % | dV/V <= 5 % (logic); <= 1 % (sensitive analog) | rail spec | Supply requirements | calc | p.707 §11.6 | high |
| SCHERZ-2141 | power | Capacitor-input filter ripple, 60-Hz full-wave: capacitor discharges ~5 ms of each 8.3-ms period (3.3 ms charging); linearized ripple | I = C*dV/dt; Vripple(rms) = 0.0024 s * IL/Cf (Vpp ~ 2*sqrt(3)*Vrms, triangle approx.; OCR prints "Vpp = 2 Vrms") | IL (A), Cf (F) | Examples: 4700 uF, 1.0 A -> 510 mV rms; 4700 uF, 1.5 A -> 760 mV rms | calc | p.707-709, Fig. 11.12 | high |
| SCHERZ-2142 | power | Size bulk capacitance for the regulator, not for zero ripple: large electrolytics have 5-20 % (or worse) tolerance; rely on regulator ripple rejection (7805 ~60 dB -> /1000; LM317 ~65 dB, ~80 dB with 10-uF ADJ bypass -> /10,000) | Vout_ripple = Vin_ripple * 10^(-RR/20) | Vin_ripple, RR (dB) | Examples: 510 mV -> 0.51 mV (7805); 760 mV -> 0.076 mV (LM317 + bypass) | calc | p.708-709, Fig. 11.13 | high |
| SCHERZ-2143 | emc | Put an ac line filter (LC) before the transformer to block line HF interference/spikes and reduce supply RF emission; add a bidirectional transient suppressor (TVS) across the line | - | - | Line-powered supplies | inspect | p.709, Fig. 11.14 | high |
| SCHERZ-2144 | protection | Output overvoltage protection for regulator failure: SCR crowbar (e.g. 5.6-V zener on a 5-V rail fires when rail exceeds Vz + 0.6 V; latches until power removed) or zener + power-transistor clamp (no latch, immune to spike false-trips) | V_trip = Vz + 0.6 V | Vrail, Vz | Regulated supplies | calc | p.710, Fig. 11.15 | high |
| SCHERZ-2145 | protection | Bleeder resistor across the unregulated filter capacitor (1 kohm, 1/2 W suits most) to discharge it at power-off; RC snubber across the transformer primary (100 ohm + 0.1 uF, 1 kV) against turn-off inductive transients | R_bleed = 1k, 1/2 W; snubber 100 ohm + 0.1 uF/1 kV | V_cap | Transformer supplies | inspect | p.710, Fig. 11.16 | high |
| SCHERZ-2146 | power | Efficiency: linear regulated supplies typically < 50 %; switchers > 85 %, with step-down, step-up and inverting options and possible off-line operation | eta_linear < 50 %; eta_switcher > 85 % | Pin, Pout | Topology choice | calc | p.710 §11.8 | high |
| SCHERZ-2147 | power | Simple buck module: LM2575 (fixed/adjustable) 5 V at 1.0 A from 7-40 V dc with 100-uF input cap, 330-uH inductor, 1N5819 Schottky catch diode, 330-uF output cap; higher switching frequency permits smaller inductors | Vin = 7-40 V; L = 330 uH; Cin = 100 uF; Cout = 330 uF | Vin, Iload | LM2575 buck | calc | p.713, Fig. 11.22 | high |
| SCHERZ-2148 | power | Off-line SMPS: rectified 120 V ac gives ~160 V dc with no isolation; isolate with a high-frequency transformer as the storage element and a transformer or optoisolator in the feedback path (e.g. 65-kHz switching) | Vdc ~ 160 V from 120 V ac | line voltage | Off-line converters | review | p.713-714, Fig. 11.23 | high |
| SCHERZ-2149 | power | Power density: 500-W switcher ~640 in^3 vs ~1520 in^3 linear; ~0.9 W/in^3 switching vs ~0.4 W/in^3 linear | W/in^3: 0.9 (SMPS), 0.4 (linear) | P_out | Enclosure volume estimate | calc | p.714 | high |
| SCHERZ-2150 | power | Switcher output carries switching ripple of tens of mV (normally below the ~200-mV logic noise margin); add a high-current LC low-pass post-filter for sensitive loads | V_ripple_sw ~ tens of mV | load sensitivity | SMPS outputs | measure | p.714 | high |
| SCHERZ-2151 | power | Commercial supply packages and power ranges: small modules (~2.5 x 3.5 x 1 in) linear 1-10 W, switching 10-25 W; open-frame linear 10-200 W, switching 20-400 W; enclosed linear 10-800 W, switching 20-1500 W; modules/open-frame need user-supplied fuses, switches, filters | see Table S2-11.3 | P_out | Buy-vs-build | review | p.714-715 | high |
| SCHERZ-2152 | connectors | Wall adapters: typical +3, +5, +6, +7.5, +9, +12, +15 V; 6.3-mm barrel plug usually center (inner) positive in consumer gear, but often center negative in musical equipment (guitar pedals) - verify polarity and add reverse protection | - | adapter polarity | External dc input | inspect | p.715 | high |
| SCHERZ-2153 | power | Dc-jack with shorting (switched) contact disconnects the battery when an external adapter is plugged in | - | - | Battery + adapter products | inspect | p.707, Fig. 11.11 | medium |
| SCHERZ-2154 | mechanical | Power supply construction: transformer bolted to the metal enclosure toward the rear; fuse, switch, binding posts at the rear; boards on standoffs; heat-sink regulators; vent holes; ground the enclosure; line cord through grommet strain relief; insulate every exposed 120-V connection with heat-shrink | - | enclosure layout | Line-powered equipment | inspect | p.716, Fig. 11.28 | high |
| SCHERZ-2155 | power | Constant-current source from a fixed regulator: resistor from OUT to GND pin sets load current (used for LEDs/lamps, incl. high-power LEDs) | IL = Vreg/R1 | Vreg, R1 | 78xx as current regulator | calc | p.703, Fig. 11.6 | high |
| SCHERZ-2156 | protection | Regulator fed from a 12-V car battery: series 1N4002 diode for reverse-polarity protection, Cin 1-10 uF, Cout 0.1 uF | - | - | Automotive-powered devices | inspect | p.702, Fig. 11.6 | high |
| SCHERZ-2157 | hw-fw | Architecture choice: if a logic design needs more than about three logic ICs, use a microcontroller (small MCUs cost < $1) or, where speed matters, an FPGA; software logic is slower than gate logic | n_logic_ICs > 3 -> MCU/FPGA | IC count, speed need | Discrete logic designs | review | p.717, 752-753 | medium |
| SCHERZ-2158 | components | Logic input/output levels must be taken from the family datasheet; book values: generic TTL-type high 2.4-5 V, low 0-0.8 V; 74HC @ 5 V: VIH(min) 3.5 V, VIL(max) 1.0 V, VOH(min) 4.4 V, VOL(max) 0.1 V (Fig. 12.52); CMOS 4000B @ 5 V: inputs high 3.3-5 V, low 0-1.7 V, outputs 4.9-5 V / 0-0.1 V; 4000B general: VIH >= 2/3 VDD, VIL <= 1/3 VDD, supply 3-18 V | see Table S2-12.1 | family, VCC | p.727 also prints 74HC input high 2.5-5 V / low 0-2.1 V, inconsistent with Fig. 12.52 | review | p.718, 727, 754-755, Fig. 12.52 | high |
| SCHERZ-2159 | timing | Interface compatibility / noise margin between driver and receiver | NM_H = VOH(min,driver) - VIH(min,receiver) >= 0; NM_L = VIL(max,receiver) - VOL(max,driver) >= 0 (74HC-74HC: 0.9 V each) | VOH, VOL, VIH, VIL | Mixed families (use 74HCT/ACT for TTL-level drivers) | calc | p.755-756, Fig. 12.52 | medium |
| SCHERZ-2160 | components | 74HC family runs from 2-6 V (5 V standard); 74HCT = TTL-compatible input levels; 74AC approaches 74F speed, 74ACT TTL-compatible; 4000B is slower and more ESD-susceptible | VCC(74HC) = 2..6 V | VCC, speed | Logic family selection | review | p.727, 754-755 | high |
| SCHERZ-2161 | components | Fanout: number of same-family inputs one output can drive | fanout = min(IOL/IIL, IOH/IIH); ~50 for 74HC | IOL, IOH, IIL, IIH | Same-family loads | calc | p.756 §12.4.3 | high |
| SCHERZ-2162 | decoupling | Place a 0.01-0.1 uF multilayer ceramic capacitor (voltage rating > 5 V) directly across VCC-GND of each logic IC, as close as possible; minimum one per 5-10 gates or one per 5 counter/register ICs | C = 0.01-0.1 uF MLCC per IC | IC list, layout | Logic supply-current spikes cause false triggering and EMI | inspect | p.756 §12.5.1 | high |
| SCHERZ-2163 | hw-fw | Never leave logic inputs floating: unused inputs of a used AND/NAND tied high, of a used OR/NOR tied low; flip-flop PRE/CLR tied to their inactive level (active-low -> pulled high); all inputs of unused CMOS gates grounded (floating CMOS inputs cause shoot-through current, excess supply drain, damage) | no floating inputs | netlist | CMOS and TTL | inspect | p.757, 763, Fig. 12.54 | high |
| SCHERZ-2164 | protection | Never drive CMOS inputs while the IC's supply is removed (input protection diodes are damaged); in RC reset circuits with CMOS Schmitt inputs use a discharge diode plus series resistor (e.g. 1N4001 + 330 ohm) | Vin <= VDD + diode drop at all times | power sequencing | CMOS inputs from other powered domains | review | p.757, 778, Fig. 12.85 | high |
| SCHERZ-2165 | test | Logic probe capability: single pulses as narrow as ~10 ns, pulse trains to ~100 MHz; probe powered from circuit (5-15 V); logic pulser 1 pps or 500 pps | t_pulse >= 10 ns; f <= 100 MHz | signal | Digital bring-up | measure | p.757-758, Fig. 12.55 | high |
| SCHERZ-2166 | hw-fw | Mechanical switch contacts bounce, typically for no more than 50 ms; debounce with an SR latch on an SPDT switch (10k pull-ups, e.g. 74LS279A) or, with a microcontroller, in software (free) | t_bounce <= ~50 ms (debounce window >= 50 ms) | switch type | Switch inputs | measure | p.760-761, 763, Fig. 12.57 | high |
| SCHERZ-2167 | timing | Flip-flop timing: inputs stable at least one setup time before the active edge (typ. ~20 ns; 7474 20 ns; 74LS76 min 20 ns); hold time typically 0 ns; clock-to-Q tPLH/tPHL ~20 ns; respect fmax, minimum clock high/low widths and preset/clear pulse widths from the datasheet | t_data_valid_before_edge >= ts; >= th after | ts, th, tpd, fmax, tW | Synchronous logic | calc | p.766, 773-774, Fig. 12.78 | high |
| SCHERZ-2168 | timing | Ripple counters accumulate flip-flop delays (standard TTL ~30 ns per stage; 4 stages = 120 ns at the MSB); use synchronous counters (common clock) for high-frequency or timing-critical designs; cascading via ripple-clock outputs is not truly synchronous - use common clock plus TC/CET enable | t_MSB = n * tpd_FF | n stages, tpd | Counters | calc | p.772, 780, 785 | high |
| SCHERZ-2169 | timing | Gate a clock with an asynchronous external control only through a synchronizer (edge-triggered D flip-flop clocked by the system clock) to avoid shortened (runt) clock pulses | - | control source | Clock enable from switches/async logic | review | p.767, Fig. 12.68 | high |
| SCHERZ-2170 | timing | Avoid pulse-triggered (master-slave) JK flip-flops where the clock stays high for long intervals: they "ones-catch" glitches on J/K; use edge-triggered flip-flops | - | clock duty/width | Sequential logic | review | p.769-770 | high |
| SCHERZ-2171 | timing | Gate/RC clock generators (Fig. 12.79): two 74HC04 inverters f = 1/(R1*C) with R2 = 10*R1 (100k/1M/0.01 uF); hysteresis version f ~ 1/(1.2*R1*C1), R3 = 10*R2, R2 = 10*R1, C1 = 100*C2; gated 4011 NAND oscillator up to ~2 MHz; 74LS00 SR-latch oscillator (1k) 1 Hz-10 MHz for 10 pF-50 uF; 555 + JK toggle gives 50 % duty; 74S124 VCO 0.1 Hz-100 MHz vs Cext (VCC 5 V, Vfreq = VRNG = 2 V); use crystal (CMOS inverters, 100k, 100 pF) when stability is needed | as listed | R, C | Logic clocks | calc | p.774-775, Fig. 12.79 | high |
| SCHERZ-2172 | timing | 74121 nonretriggerable one-shot: pulse width; keep tw <= ~28 s (R = 40k, C = 1000 uF) for reliable operation; use the Schmitt B input for slow or noisy triggers; triggers during the pulse are ignored | tw = Rext*Cext*ln 2; 28.8k x 0.01 uF -> 200 us | Rext, Cext | One-shots | calc | p.776, Fig. 12.80 | high |
| SCHERZ-2173 | timing | 74123 retriggerable one-shot pulse width (valid for Cext > 1000 pF; below use datasheet graphs); retrigger extends the pulse by tw | tw = 0.28*Rext*Cext*(1 + 0.7/Rext) (formula as printed; Rext unit not stated) | Rext, Cext | One-shots | calc | p.776, Fig. 12.80 | high |
| SCHERZ-2174 | timing | 555 monostable used as logic one-shot | tw = 1.1*R1*C1; 18.2k x 0.001 uF -> ~20 us | R1, C1 | Fig. 12.82 | calc | p.777 | high |
| SCHERZ-2175 | hw-fw | Power-up clear: hold active-low CLR below the release threshold (74LS76 releases at >= 2.0 V) long enough; RC reaches 63 % (3.15 V at 5 V) at t = RC; example R = 1k, C = 0.001 uF -> ~1 us; more ICs on the clear line shorten the low time (use larger C); improved circuit: Schmitt inverter (74HC14) with 10k/10 uF, 1N4001 discharge diode, 330-ohm series (omit for TTL) | V_C(t) = VCC*(1 - exp(-t/RC)); t_hold ~ RC | R, C, V_release | Sequential logic reset | calc | p.777-778, Fig. 12.84-12.85 | high |
| SCHERZ-2176 | hw-fw | Pull-up sizing: high-level input current must not pull the node below VIH(min); dissipation when the switch closes; 10k works in most applications | Vin = VCC - IIH*R >= VIH(min); PD = VCC^2/R; 74LS (IIH ~20 uA) with 10k -> 4.80 V, 2.5 mW | VCC, IIH, VIH(min), R | Switch inputs | calc | p.779, Fig. 12.86 | high |
| SCHERZ-2177 | hw-fw | Pull-down sizing: low-level input current must not raise the node above VIL(max); typical 100 ohm-1 kohm for TTL-type inputs; watch dissipation when the switch closes | Vin = IIL*R <= VIL(max); PD = VCC^2/R; 74LS (IIL = 400 uA) with 500 ohm -> 0.20 V (< 0.8 V), 50 mW | IIL, VIL(max), R | Switch inputs | calc | p.779-780, Fig. 12.86 | high |
| SCHERZ-2178 | hw-fw | Analog-to-logic threshold interfaces: comparator (open-collector + pull-up) or op amp; op amp driving CMOS needs a series current-limit resistor and clamp diodes when the op-amp supply exceeds the logic supply (open-collector LM339 needs none); op amp driving TTL via transistor stage with base-emitter reverse-protection diode | V_logic_in within [GND - 0.x, VDD + 0.x] | supplies | Sensor thresholds into logic/MCU pins | inspect | p.799-800, Fig. 12.112 | high |
| SCHERZ-2179 | components | LM34 outputs 10 mV/degF; LM35 outputs 10 mV/degC (threshold for 75 degC = 750 mV) | Vout = 10 mV/deg * T | T | Analog temperature sensors | calc | p.800 | high |
| SCHERZ-2180 | hw-fw | Driving loads from logic: compare load current with the gate's source/sink rating; otherwise use a transistor/MOSFET stage; relays need a power MOSFET plus flyback diode; open-collector gates sink ~10x a standard gate (check rating); use an optocoupler when the load has a separate ground/needs isolation | I_load <= I_OH/I_OL(max) else buffer | I_load, gate ratings | LEDs, relays, buzzers | calc | p.800-801, Fig. 12.113 | high |
| SCHERZ-2181 | components | Analog switches: 4066B single 3-15 V supply, switches signals within +/-7.5 V, ~700 mW max dissipation; AH0014D DPDT +/-10 V (separate analog +/- and digital supplies); DG302A +/-10 V, switching to 15 ns | V_signal within switch range | signal range, supply | Analog switching | calc | p.802, Fig. 12.114 | high |
| SCHERZ-2182 | components | 4051B analog mux: analog I/O must stay between VEE and VDD (VSS grounded); for +/-5 V signals set VEE = -5 V, VDD = +5 V; digital 3-15 V; analog to +/-15 V; INH high disconnects all channels | VEE <= V_analog <= VDD | signal range | Analog multiplexing | calc | p.802-803, Fig. 12.115 | high |
| SCHERZ-2183 | hw-fw | Converter resolution and full scale | LSB = FS/2^n (8-bit, 15 V -> 0.058 V; 18-bit -> 0.000058 V); max output = (2^n - 1)/2^n * Vref (8-bit: 255/256 Vref) | n bits, FS | ADC/DAC selection | calc | p.804, 807-808 | high |
| SCHERZ-2184 | components | Binary-weighted resistor DACs are impractical beyond a few bits (8-bit from R = 100k needs R/128 = 0.78125 kohm and tight tolerances); use an R-2R ladder (only R and 2R) | Vout = -Vref*RF/Rin (weighted); R-2R branch currents I/2, I/4, I/8, I/16 with I = Vref/R; Vout = -Isum*RF | Vref, R, RF, code | Example R-2R: 5 V, 10k -> 500 uA; code 0101 -> 156.25 uA; RF 20k -> -3.125 V | calc | p.805-807, Fig. 12.117-12.119 | high |
| SCHERZ-2185 | components | DAC0808 8-bit current DAC: set Iref = 2 mA with +10 V and 5 kohm (another 5 kohm from -Vref to ground); output current and op-amp I-to-V; in multiplying mode keep reference current 16 uA-4 mA | Iout = Iref*code/256 (FS 1.99 mA, step 0.0078 mA); Vout = Iout*Rf (5k -> 9.95 V FS, 38.9 mV step) | Iref, code, Rf | DAC0808 | calc | p.808-809, Fig. 12.121 | high |
| SCHERZ-2186 | hw-fw | Ratiometric transducers (pots, strain gauges, pressure sensors): use the transducer's excitation as the converter reference (multiplying DAC/ratiometric ADC) so supply variations cancel | code = f(Vsig/Vref) independent of excitation | reference routing | Bridge/pot sensors | review | p.807 | high |
| SCHERZ-2187 | hw-fw | DAC/ADC data coding: unipolar uses straight binary; bipolar uses offset binary or 2's complement - firmware must match | - | converter mode | Firmware/hardware interface | review | p.807, Fig. 12.120 | high |
| SCHERZ-2188 | hw-fw | Successive-approximation ADCs convert in ~10-300 us; add a sample-and-hold if the input can change during conversion; discrete ADC ICs are largely replaced by MCU ADCs (12-bit or more) except for very high speed | t_conv = 10-300 us; dV/dt * t_conv < 1 LSB (else S/H) | f_signal, t_conv | ADC front ends | calc | p.811-812, Fig. 12.124 | high |
| SCHERZ-2189 | hw-fw | Flash ADC: reference ladder divides Vref into 2^n levels (3-bit, 5 V -> 0.625 V per step with 1-kohm ladder), comparators feed a priority encoder | step = Vref/2^n | n, Vref | High-speed ADC | calc | p.812-813, Fig. 12.125 | high |
| SCHERZ-2190 | components | 7-segment drivers: 7447/74LS47 active-low open-collector outputs for common-anode displays (7 x 330-ohm series at 5 V); 74HC4511 active-high for common-cathode; MM5450 serial driver has 34 outputs sinking up to 15 mA each | R_seg = 330 ohm @ 5 V (example); I_seg <= 15 mA (MM5450) | display type | LED displays | inspect | p.745, 813-815, Fig. 12.38, 12.128 | high |
| SCHERZ-2191 | hw-fw | Multiplex multi-digit LED displays: shared segment lines and one enabled digit at a time, refreshed fast enough to look continuous (4-digit 7-segment: 11 lines vs 32 non-multiplexed); an MCU can drive segments directly | lines = segs + digits (mux) vs segs*digits + digits | digits | LED displays | calc | p.787, 815, Fig. 12.129 | high |
| SCHERZ-2192 | components | LCDs: passive (need ambient light, mW/cm^2, or a backlight that costs power); switching 40-100 ms, slower when cold; must be driven with ac (square wave on backplane, XOR segment drive) because dc causes electrochemical degradation; drive frequency ~25 Hz to a couple hundred Hz; supertwist (270 deg) improves contrast/viewing angle | f_drive = 25-~200 Hz; Vdc_avg ~ 0 | drive scheme | Segment LCDs | review | p.815-818, Fig. 12.132 | high |
| SCHERZ-2193 | hw-fw | HD44780 character LCD: 14-pin interface (D0-D7, RS, R/W, E, VDD +5 V, VSS, VEE contrast via pot, e.g. 5k); 8-bit or 4-bit (D4-D7) transfer; data latched on E high-to-low; powers up in 8-bit mode with display off - send Function Set (e.g. 0011 1000: 2 lines, 8-bit, 5x7) and Display On (0000 1111); 80 display locations, line 2 starts at 40H; 8 CGRAM user characters are volatile (reload from nonvolatile memory); formats 8/16/20/24/32/40 columns x 1/2/4 rows | - | firmware init | Character LCD modules | review | p.822-828, Fig. 12.139-12.142 | high |
| SCHERZ-2194 | reliability | Nonvolatile memory endurance: EEPROM ~100,000 write cycles (slow writes); EPROM a couple hundred reprogram cycles (UV erase ~20 min, ~12-V programming); NOVRAM ~10,000 store cycles; battery-backed SRAM ~10 years (lithium); use SRAM for frequent writes | writes_per_day * 365 * life_years <= endurance | write rate, life | Data logging, settings | calc | p.833-838 | high |
| SCHERZ-2195 | hw-fw | Memory addressing: n address lines address 2^n locations; 1K = 1024; kB = 8 x kbit; read the organization (a "64K" part may be 8K x 8, 16K x 4 ...) | locations = 2^n | address lines | Memory selection | calc | p.830-831, Table 12.2 | high |
| SCHERZ-2196 | timing | ROM/semiconductor memory access time ~10 ns to a couple hundred ns (address-valid to data-valid) | t_access = 10-200+ ns | technology | Bus timing | calc | p.831-832, Fig. 12.145 | high |
| SCHERZ-2197 | timing | Simple DRAM cells must be refreshed every 2 ms or sooner (all rows; RAS-only refresh preferred); modern DRAMs integrate refresh | t_refresh <= 2 ms (example device) | - | DRAM | review | p.839-840 | high |
| SCHERZ-2198 | cost | Mask ROM needs a > $1,000 mask; worthwhile only for volumes above a couple thousand units with no future updates | NRE > $1,000; volume > ~2,000 | volume, update need | Production memory choice | calc | p.832-833 | high |
| SCHERZ-2199 | hw-fw | Serial (I2C) EEPROMs (24xx): SDA/SCL bus, A0-A2 device-address pins for multiple devices, WP write-protect pin; serial protocol protects stored data from runaway-processor writes | - | bus address plan | Nonvolatile storage | inspect | p.835-836, Fig. 12.147 | high |
| SCHERZ-2200 | hw-fw | Mains-derived 60-Hz timebase: 12.6-V transformer, 1k + 3.9-V zener (1N748) clamp to keep the Schmitt input (74LS14: VT+ ~1.7 V, VT- ~0.9 V; out ~0.2/3.4 V) within rating; /6 -> 10 Hz, /10 -> 1 Hz; for 50-Hz mains use /5 | f_out = f_line/N | line frequency | Real-time counting | calc | p.788, Fig. 12.95 | high |
| SCHERZ-2201 | hw-fw | LED on a 5-V logic output: series resistor ~300-330 ohm in the book's examples (source or sink) | R ~ 300-330 ohm @ 5 V | VCC, LED current | Indicator LEDs | calc | p.745, 767, 772 | medium |
| SCHERZ-2202 | hw-fw | Expand MCU outputs with serial-in/parallel-out shift registers (e.g. 74164 feeding an output latch such as 74HCT273) so all outputs update simultaneously | - | pin budget | LED/driver expansion | review | p.792, 796, Fig. 12.109 | medium |
| SCHERZ-2203 | hw-fw | Devices sharing a data bus must have three-state outputs, disabled (high-Z) when not driving | - | bus netlist | Buses | inspect | p.764, 795 | high |
| SCHERZ-2204 | timing | 74160/74163-type synchronous counters: change CEP/CET (high-to-low) and PE/MR (low-to-high) only while CP is high | - | control timing | Synchronous counters | review | p.786, Fig. 12.93 | high |
| SCHERZ-2205 | timing | An n-flip-flop ring counter has n states; an n-flip-flop Johnson counter has 2n states (4-bit Johnson -> 8 states) | states = n (ring), 2n (Johnson) | n | Sequencers | calc | p.791-792 | high |
| SCHERZ-2206 | hw-fw | ATtiny85 resources/limits: 8 kB flash, 256 B SRAM, 512 B EEPROM; 2.7-5.5 V at <= 10 MHz; ~300 uA at 1 MHz; ~0.1 uA in power-down waiting for watchdog; internal oscillator is inaccurate - sacrifice two I/O pins for a crystal when timing matters; costs ~$1 | Vcc 2.7-5.5 V @ f <= 10 MHz; I = 300 uA @ 1 MHz; 0.1 uA power-down | Vcc, fclk, timing accuracy | 3-V lithium cell or 2 x AA operation | calc | p.845-846, 848 | high |
| SCHERZ-2207 | hw-fw | Minimal MCU circuit: 100-nF decoupling across VCC-GND, RESET pulled up through a resistor (10k), not hard-wired, so the programmer can pull RESET low; include the 6-pin ICSP header on development PCBs | C_dec = 100 nF; R_reset = 10k | schematic | AVR ATtiny/ATmega | inspect | p.846, 848, Fig. 13.3 | high |
| SCHERZ-2208 | hw-fw | PIC16C5x needs a crystal or ceramic resonator on OSC1/OSC2; 5 MIPS at 20 MHz; on-chip RC watchdog runs without external parts and can reset a sleeping or hung controller; PIC16C56 1024 words / PIC16C57 2048 words program memory | MIPS = fclk/4 (5 MIPS @ 20 MHz) | fclk | PIC16C5x | review | p.849-850 | high |
| SCHERZ-2209 | hw-fw | BASIC Stamp II I/O limits: each pin sources 20 mA / sinks 25 mA; each group of 8 pins (P0-P7, P8-P15) sources 40 mA / sinks 50 mA total; on-board 5-V regulator accepts >5 V to 15 V and supplies <= 50 mA to external circuits; brownout reset chip holds the PIC in reset during low supply; 2048-byte program EEPROM (~500-600 PBASIC lines); I/O like 74HCT | I_pin <= 20 mA source / 25 mA sink; I_group <= 40/50 mA; I_ext <= 50 mA | loads, Vin | BSII modules | calc | p.852-854 | high |
| SCHERZ-2210 | hw-fw | Use a supply supervisor/brownout reset so the MCU is held in reset whenever the supply is below its operating minimum (weak battery, power-up) | reset while Vcc < Vmin | Vcc ramp | All MCU designs | inspect | p.853 | high |
| SCHERZ-2211 | hw-fw | Low-power modes: BSII NAP/SLEEP reduce consumption to ~50 uA (no loads); NAP duration = 2^period x 18 ms; SLEEP 1-65,535 s | I_sleep ~ 50 uA | duty cycle | Battery budgets | calc | p.858, Table 13.1 | high |
| SCHERZ-2212 | hw-fw | RC servo command: pulse 1000-2000 us repeated about every 20 ms (must be refreshed to hold position); 1500 us = center (stop for continuous-rotation servos, e.g. 1300 us one direction, 1700 us the other); stop point varies with production tolerance - provide a trim | t_pulse = 1.0-2.0 ms; T_frame ~ 20 ms | servo spec | Hobby servos | measure | p.859-860, 862 | high |
| SCHERZ-2213 | hw-fw | IR proximity sensing: modulate the IR LED at the receiver-module carrier (38 kHz, 50 % duty) to reject ambient/incandescent IR; a slow MCU sees only a fraction of the pulses (BSII ~4000 instructions/s saw ~10-20 of 38,000) | f_mod = receiver carrier (38 kHz) | receiver module | IR obstacle detection | measure | p.860 | high |
| SCHERZ-2214 | hw-fw | DSP on MCUs: ordinary 8-bit ADC/CPU gives only low-quality audio DSP; use DSP-oriented parts (e.g. dsPIC: 16-bit, 40 MHz, 2 kB RAM) for real-time filtering/FFT | - | sample rate, algorithm | Audio DSP | review | p.862-863 | medium |
| SCHERZ-2215 | hw-fw | Arduino board resources: Uno (ATmega328) 14 digital + 6 analog I/O, 32 kB flash, 2 kB SRAM, 1 kB EEPROM, dc jack 7-12 V or USB auto-select; Mega 2560: 54 digital + 16 analog, 4 UARTs, 256 kB flash, 8 kB SRAM, 4 kB EEPROM; Lilypad: 16 kB flash, 1 kB SRAM, 512 B EEPROM, 8 MHz; Uno I2C on A4/A5, UART on D0/D1 | see Table S2-13.1 | pin/memory budget | Arduino-based prototypes | review | p.864-866, Table 13.3 | high |
| SCHERZ-2216 | hw-fw | Stacking shields: verify no two shields use the same pins (jumpers on some shields allow reassignment); display shields usually do not pass headers through | pin sets disjoint | shield pin maps | Arduino shields | inspect | p.867 | high |
| SCHERZ-2217 | hw-fw | Arduino core limits: analogRead returns 0-1023 for 0 V to Vref (5 V; 3.3 V boards 3.3 V); analogWrite duty 0-255 only on PWM pins 3, 5, 6, 9, 10, 11 (Uno); millis() wraps after ~50 days, micros() after ~70 minutes; delayMicroseconds valid ~3 us to ~16 ms; attachInterrupt(1) = D3 on Uno | ADC 10-bit; PWM 8-bit | timing, pins | Arduino firmware | review | p.868-869, Table 13.6 | high |
| SCHERZ-2218 | hw-fw | Moving from Arduino board to product PCB: the ATmega328 (as the IDE expects) needs an external crystal or ceramic resonator and normally a voltage regulator; keep only the Uno features the product needs | - | BOM | Arduino-to-custom-PCB transition | review | p.872, Fig. 13.13-13.14 | high |
| SCHERZ-2219 | hw-fw | Switch input pull-ups: normally-open switch - 1 kohm (5 mA only while pressed; some use 270 ohm) for noise immunity; normally-closed switch - use a high value (10k) because current flows continuously; internal AVR pull-ups are 20-40 kohm - use external pull-ups in noisy environments or with long leads | R_pu = 1k (N.O.), 10k (N.C.); R_internal = 20-40k | switch type, lead length | MCU switch inputs | calc | p.874-875, Fig. 13.15 | high |
| SCHERZ-2220 | hw-fw | Multiple buttons on one ADC input via resistor ladder: decode with bands, not exact values (resistor tolerance, supply variation); Freetronics example (2k pull-up; 330, 620, 1k, 3k3): RIGHT 0.00 V (0), UP 0.71 V (145), DOWN 1.61 V (329), LEFT 2.47 V (505), SELECT 3.62 V (741) at 10 bits | band = nominal +/- tolerance; bands must not overlap | ladder values | Button ladders | calc | p.875-876, Fig. 13.16 | high |
| SCHERZ-2221 | hw-fw | Matrix keypads: scan by driving columns and reading rows; rows need pull-ups (internal or external); use an existing keypad library | - | matrix size | 4 x 3 keypad | review | p.876, Fig. 13.17 | high |
| SCHERZ-2222 | firmware | Debounce in software: act on the first transition, ignore further transitions for a debounce period (example 100 ms) using a timestamp when the MCU has other tasks | t_debounce ~ 100 ms (example) | bounce time | MCU switch inputs | review | p.877-878, Fig. 13.18 | high |
| SCHERZ-2223 | protection | Scaling a high voltage into an MCU ADC: resistor divider plus zener clamp at the pin; example 10 kohm/1 kohm (1:11) with 5.1-V zener measures 0-50 V (not 55 V, because the zener starts conducting below 5.1 V and spoils linearity) | V_pin = V_in * R2/(R1+R2); V_in_max = V_ref*(R1+R2)/R2 derated for zener knee | V_in range, V_ref | ADC inputs | calc | p.878-879, Fig. 13.20 | high |
| SCHERZ-2224 | firmware | Implement thermostat-type switching in firmware with hysteresis rather than in hardware (example setpoint 20 deg, +/-2 deg hysteresis) | on if T < SP - h; off if T > SP + h | SP, h | Control loops in firmware | review | p.879 | high |
| SCHERZ-2225 | derating | MCU pin drive: most MCUs reliably source/sink only ~20 mA per output; Arduino (ATmega) allows 40 mA per pin and 200 mA per chip absolute max - derate by 25 % for production; use transistors/MOSFETs for relays, high-power LEDs, speakers | I_pin <= 20 mA typical; ATmega I_pin <= 40 mA, I_chip <= 200 mA (x0.75 for production: 30 mA, 150 mA) | load currents | MCU outputs | calc | p.879-880 | high |
| SCHERZ-2226 | components | MOSFET low-side switch from a logic pin: choose a logic-level MOSFET with gate threshold well below the drive voltage (a 6-V-threshold part will not turn on from 5 V); add a ~1-kohm gate resistor to limit the gate-capacitance inrush on the MCU pin | V_GS(th) << V_logic; R_gate ~ 1k | V_GS(th), V_logic | MCU-driven loads | calc | p.880-881, Fig. 13.22 | high |
| SCHERZ-2227 | protection | Relays and other inductive loads (motors) driven from MCUs: almost all relays need > 50 mA (except some reed relays) so use a transistor, and always put a reverse-biased diode across the coil | I_coil > 50 mA -> transistor; flyback diode across coil | coil current | Relays, dc motors | inspect | p.881, Fig. 13.23 | high |
| SCHERZ-2228 | control-loop | Motor speed by PWM through a transistor driver (buffer such as 74HC07 optional with robust MCU outputs); direction via H-bridge - integrated H-bridge ICs (e.g. TB6612FNG) for motor currents below a couple of amps, often with thermal shutdown | I_motor < ~2 A -> integrated H-bridge | motor current | DC motors | review | p.881-882, Fig. 13.24-13.25 | high |
| SCHERZ-2229 | hw-fw | Sound from MCUs: MCU ADCs typically sample above 10 kHz (primitive DSP); piezo can be driven directly from a pin; an 8-ohm loudspeaker needs a transistor stage (check collector current); PWM carrier is in the audio band, so generate sine waves with an R-2R DAC (e.g. R = 5k, 2R = 10k; 4 bits = 16 levels) or a DAC IC | fs_ADC > 10 kHz; I_C = V/8 ohm | load type | Audio I/O | calc | p.883-884, Fig. 13.28-13.29 | high |
| SCHERZ-2230 | hw-fw | 1-Wire bus: devices run at 5 V or 3.3 V (match the MCU or risk damage); 4.7-kohm pull-up; parasitic power mode (device GND and Vdd tied) needs only data + ground; up to 255 devices, each with a 64-bit ROM ID; bit 0 = 60 us low pulse, bit 1 = 15 us; reset pulse >= 480 us; DS18B20 conversion wait 750 ms, 0.0625 degC/LSB | R_pu = 4.7k; t_reset >= 480 us; t_conv = 750 ms | bus voltage, device count | DS18B20 etc. | calc | p.885-887, Fig. 13.30 | high |
| SCHERZ-2231 | hw-fw | I2C (TWI): open-drain SDA/SCL with pull-ups (4.7 kohm in the example), 5 V or 3.3 V, up to 400 kbit/s; multiple masters allowed; remote I2C sensors need 4 wires (2 data + 2 power) | f_SCL <= 400 kHz (book); R_pu = 4.7k (example) | bus voltage, speed | I2C buses | calc | p.888-889, Fig. 13.32-13.33 | high |
| SCHERZ-2232 | hw-fw | SPI: SCLK, MOSI, MISO plus one dedicated slave-select line per slave; single master; up to 80 Mbit/s; bit order is not defined by the standard - match each device; SPI doubles as the ICSP port on ATmega/ATtiny | n_SS lines = n_slaves; f <= 80 Mbit/s | slaves, speed | SPI buses | review | p.890-891, Fig. 13.34 | high |
| SCHERZ-2233 | hw-fw | TTL serial (UART) is point-to-point (Tx/Rx crossed) at logic levels, not RS-232 bipolar levels; both ends must use the same baud rate and framing (almost always 8N1, LSB first); standard rates 110 ... 9600 (common default) ... 115200, 128000, 256000; 1200 is about the slowest in common use and many TTL devices do not reach 115200; baud includes start/stop bits | throughput = baud * 8/10 (8N1) (derived) | baud, framing | UART links | calc | p.891-892, Fig. 13.35 | high |
| SCHERZ-2234 | hw-fw | 5-V <-> 3.3-V level conversion: unidirectional lines (UART, SPI) - 3.3-V output into a 5-V input can connect directly (5-V MCU reads > ~2.5 V as high); 5-V output into a 3.3-V input needs a divider (1.8 kohm / 2.2 kohm in Fig. 13.36); bidirectional open-drain lines (I2C, 1-Wire) need a level-shifter IC (TXS0102, MAX3372, PCA9509, PCA9306); many 3.3-V parts are not 5-V tolerant | V_div = 5 V * R_bot/(R_top + R_bot) (2.75 V with 2.2k to ground, derived) | Voh, Vih, abs max | Mixed-voltage systems (also 1.8 V) | calc | p.892-893, Fig. 13.36-13.37 | high |
| SCHERZ-2235 | hw-fw | 7-segment/common-anode/cathode displays: one current-limiting resistor per segment, never a single resistor in the common lead (brightness would vary with number of lit segments); switch digit commons in multiplexed displays with transistors (up to 8 LED currents) | one R per segment | display wiring | LED displays | inspect | p.893-894, Fig. 13.38-13.39 | high |
| SCHERZ-2236 | hw-fw | Charlieplexing: n tri-state pins drive n^2 - n LEDs (4 pins -> 12, 10 pins -> 90); duty cycle falls as LED count grows (dimming); raising peak current compensates but a frozen MCU can then burn out LEDs | N_LED = n^2 - n; duty ~ 1/N_steps | n pins | LED matrices | calc | p.894-895, Table 13.9 | high |
| SCHERZ-2237 | hw-fw | RGB LED color/brightness: control each die with PWM (more linear than analog current control) | duty 0-100 % per channel | - | RGB LEDs | review | p.895 | high |
| SCHERZ-2238 | process | Prototype with interpreter/boot-loader platforms (Stamp, Arduino) for quick iteration; for volume production remove the interpreter/external EEPROM or the dev board and program the bare MCU (compiled code) | - | volume | MCU product development | review | p.862, 872 | medium |
| SCHERZ-2239 | hw-fw | Programmable-logic choice: FPGAs (LUT-based, ~200,000 to several million logic blocks, 6-input LUT = 64 x 1 ROM) for large/fast logic; CPLDs (sum-of-products macrocells, successors of PALs) for the equivalent of a few gates; FPGAs also prototype ASICs | - | logic size, speed | Replacing discrete logic | review | p.897-900 §14.1-14.2 | high |
| SCHERZ-2240 | hw-fw | FPGA configuration is volatile: it is loaded from external (SPI) EEPROM/flash at power-up, typically in < 200 ms - outputs are not valid until configuration completes; FPGA I/O blocks source/sink only a few tens of mA | t_config < ~200 ms; I_IO ~ tens of mA | power-up sequencing, loads | FPGA designs | review | p.900 | high |
| SCHERZ-2241 | hw-fw | FPGA constraints: map every top-level port to a pin (LOC) and enable internal pull-ups for push-button inputs; a non-clock pin driving a clock net (e.g. push button) needs CLOCK_DEDICATED_ROUTE = FALSE (ISE); port name "OUT" is reserved in ISE | - | constraints file | Xilinx ISE / Spartan-3A | inspect | p.909-911, 914 | high |
| SCHERZ-2242 | hw-fw | Push-button-clocked logic bounces (counters skip values) - debounce any mechanical input used as a clock | - | clock source | FPGA/CPLD inputs | measure | p.914 | high |
| SCHERZ-2243 | test | Verify HDL modules in simulation with a test fixture (clock/reset stimulus, e.g. 10-ns half-period clock, 100-ns initial reset settle) before loading hardware | - | testbench | FPGA flow | sim | p.928-931, Fig. 14.31-14.33 | high |
| SCHERZ-2244 | hw-fw | Multiplexed 7-segment display from an FPGA: divide the board clock to a digit-refresh tick (Elbert V2: 12 MHz / 12,000 = 1 kHz) and enable one digit at a time through transistors (active-low PNP digit drivers on Elbert V2) | f_tick = f_clk/N; per-digit refresh = f_tick/n_digits | clock, digits | FPGA display drivers | calc | p.924-927 | high |
| SCHERZ-2245 | components | Brushed dc motors: typically 3000-8000 rpm at a rated voltage of 1.5-24 V; below ~50 % of rated voltage the motor usually stalls; > ~30 % above rated voltage risks overheating; loaded/stall current can be 1000 % or more of no-load current - size drivers and supplies for stall current (measure it with an ammeter if not specified) | 0.5*V_rated < V_applied < 1.3*V_rated; I_driver >= I_stall | V_rated, I_stall | Brushed dc motors | calc | p.933-934 §15.1 | high |
| SCHERZ-2246 | power | Control dc-motor speed by PWM (UJT/SCR, gate oscillator + power MOSFET, 555 in low-duty mode + MOSFET, or MCU PWM), not with a series potentiometer or linear transistor (both burn power as heat and can fail) | 555 motor PWM: t_high = 0.693*R1*C, t_low = 0.693*R2*C (diode pins 7-6) | duty, f_PWM | DC motor speed control | review | p.934-935, Fig. 15.2-15.3 | high |
| SCHERZ-2247 | protection | Motor direction: DPDT switch/relay (relay coil with flyback diode, e.g. 1N4004), complementary Darlington push-pull (TIP102/TIP107, split supply), or H-bridge with flyback diodes (e.g. 1N4001) - never drive both H-bridge inputs at once (shoot-through shorts the supply); add input logic (XOR) interlock | no simultaneous forward/reverse | input logic | H-bridges | inspect | p.935-936, 942-943, Fig. 15.4-15.5, 15.10 | high |
| SCHERZ-2248 | components | H-bridge / motor-driver ICs: LMD18200 3 A, 12-55 V, TTL/CMOS inputs, built-in clamp diodes, short-circuit protection, thermal warning; L293 dual H-bridge up to 1 A per winding at up to 36 V; L298 up to 2 A per winding; L293D cheaper, lower current | I_winding <= 1 A (L293), 2 A (L298), 3 A (LMD18200) | motor current, voltage | Motor/stepper drivers | calc | p.936, 943 | high |
| SCHERZ-2249 | components | RC servo: rotation limited to ~180 or 210 deg; 1.5-ms pulse = neutral; pulse range brand-dependent (e.g. 1-2 ms or 1.25-1.75 ms for full travel); frame period 20-30 ms; supply commonly 4.8 V (some ~6.0 V); current varies with servo power | t = 1.0-2.0 ms; T = 20-30 ms; V = 4.8-6.0 V | servo model | RC servos | measure | p.936-938, Fig. 15.6 | high |
| SCHERZ-2250 | timing | 555 servo driver (Fig. 15.6): pulse width set by R1 + R2 (pot), frame by R3 | t_high = 0.693*(R1 + R2)*C; t_low = 0.693*R3*C; R1 4.3k, R2 5k pot, R3 68k, C 0.33 uF -> ~1.0-2.1 ms high, ~15.6 ms low (derived) | R1-R3, C | Servo testers | calc | p.937-938, Fig. 15.6 | high |
| SCHERZ-2251 | compliance | RC model radio bands (US, as printed): 50 frequencies in the 72-MHz band (channels 11-60) reserved for aircraft, no license needed; 50-MHz band with an amateur licence; 27-MHz band legal for any model (surface or air) | - | band, vehicle type | RC control links | review | p.938 | high |
| SCHERZ-2252 | components | Continuous-rotation servo conversion: remove pot feedback, free the gear stop, replace the pot with a fixed divider set to the neutral resistance (measure old pot); >1.5 ms turns one way, <1.5 ms the other | - | - | Servo drive motors | measure | p.938 | high |
| SCHERZ-2253 | components | Stepper step angles range 0.72-90 deg per step; common general-purpose 15 and 30 deg; steppers give high torque at low speed but lower top speed than dc motors | step = 360/steps_per_rev | resolution | Stepper selection | review | p.938-939 | high |
| SCHERZ-2254 | control-loop | Unipolar stepper drive sequences: single (wave) stepping; power stepping (two phases on) gives ~1.4x torque for 2x power; half stepping (alternate 1 and 2 phases) halves the step angle (30 -> 15 deg) | T_power ~ 1.4*T_single; P_power = 2*P_single | sequence | Unipolar steppers | calc | p.939-941, Fig. 15.8 | high |
| SCHERZ-2255 | components | Bipolar steppers need an H-bridge per coil (polarity reversal) but give a better size-to-torque ratio; universal (8-lead) steppers: windings in parallel -> unipolar, in series -> bipolar | n_H-bridges = n_coil_pairs | stepper type | Stepper drivers | review | p.941, Fig. 15.8 | high |
| SCHERZ-2256 | protection | Stepper coil drivers: buffer (7407) between translator and power Darlington (TIP120/TIP110, ~470 ohm-1k base resistor) to protect logic from motor supply (5-24 V) on transistor breakdown; flyback diodes on every winding (unipolar needs diodes on both sides of the center tap, e.g. 1N4001); ULN2003 (7 Darlingtons with diodes) or MC1414 arrays | V_motor 5-24 V; flyback per coil | driver netlist | Stepper drivers | inspect | p.941-942, Fig. 15.9 | high |
| SCHERZ-2257 | components | SAA1027 stepper controller (classic): supply 9.5-18 V; logic inputs high >= 7.5 V, low <= 4.5 V (not 5-V logic compatible); outputs up to 500 mA; RX resistor sets driver base current; newer ICs or MCU libraries are preferred | VIH >= 7.5 V; VIL <= 4.5 V; I_out <= 500 mA | supply, logic levels | Four-phase steppers | calc | p.944-945, Fig. 15.13 | high |
| SCHERZ-2258 | test | Identify unknown steppers: 4 leads -> bipolar; 5 -> unipolar with common center tap; 6 -> unipolar with separate taps; 8 -> universal; shaft spins freely -> variable reluctance, cogging -> permanent magnet; ohmmeter: same-winding pairs read low (R center-tap to end, 2R end to end), different windings infinite | lead count; R vs 2R | ohmmeter readings | Stepper bring-up | measure | p.945-946, Fig. 15.14 | high |
| SCHERZ-2259 | requirements | Human hearing: ~20-20,000 Hz, most sensitive 1-2 kHz; intensity range 1e-12 to 1 W/m^2 (0-120 dB); intensity falls as 1/r^2 | dB = 10*log10(I/I0), I0 = 1e-12 W/m^2 | I (W/m^2), r | Audio product specs | calc | p.947-948, Fig. 16.1 | high |
| SCHERZ-2260 | components | Microphone types: dynamic (rugged, low impedance, no bias, wide temperature range); condenser (needs polarizing supply, e.g. +9 V via 1-2 kohm, 0.1-uF coupling, plus very-low-noise high-impedance amplifier); electret (internal FET needs +1.5 to +10 V through a 1-10 kohm resistor; 10-uF output coupling) | V_bias(electret) = 1.5-10 V via 1-10k | mic type | Audio inputs | inspect | p.949-950, Fig. 16.3-16.5 | high |
| SCHERZ-2261 | requirements | Microphone bandwidth: speech needs ~100-3000 Hz; hi-fi ~20-20,000 Hz; sensitivity quoted in dB re 1 dyn/cm^2 | BW_speech = 100-3000 Hz; BW_hifi = 20-20k Hz | application | Mic selection | review | p.950 §16.3 | high |
| SCHERZ-2262 | matching | Microphone impedance classes: low < 600 ohm, medium 600-10,000 ohm, high > 10,000 ohm; connect low-impedance sources to higher-impedance inputs (bridging: load >= 10 x source); high-Z source into low-Z input loses signal | Z_load >= 10*Z_source | Z_source, Z_load | Audio interconnects | calc | p.951 | high |
| SCHERZ-2263 | matching | Audio bridging loss: equal source and load impedances cost ~6 dB; loss of 6 dB or less is acceptable for most applications; for current-mode signals the source impedance should exceed the load; RF circuits need true matching | loss(dB) = 20*log10(Rload/(Rload + Rsource)) >= -6 dB | Rsource, Rload | Voltage-mode interconnects | calc | p.955-956 §16.7 | high |
| SCHERZ-2264 | components | Use audio-grade op amps (high slew rate, high GBW, high input impedance, low distortion, very low input noise) rather than 741-class parts for complex audio (e.g. AD797, NE5532/5534, OP-27, LT1115, LM833, OPA134/2134, LM4562) | - | signal quality needs | Audio paths | review | p.951 | medium |
| SCHERZ-2265 | control-loop | Audio inverting amp: G = -R2/R1, Zin ~ R1 (e.g. 10k/100k, 10-uF input coupling); noninverting: G = 1 + R2/R1, Zin ~ bias resistor (R3 dual supply / R4 single supply); single-supply versions bias the + input at V/2 with equal resistors of 10-100 kohm (56k shown), bypass the bias node, and ac-couple the output with C = 1/(2*pi*fc*RL) | Vbias = V/2; 10k <= R_bias <= 100k; C_out = 1/(2*pi*fc*RL) | R, fc, RL | Audio gain stages | calc | p.951-952, Fig. 16.6-16.7 | high |
| SCHERZ-2266 | power | Class-D (PWM) audio amplifiers: compare the signal with a triangle carrier (simulation example: 10-kHz triangle, 1-kHz sine), switch power MOSFETs, then low-pass filter the output to remove the carrier; very efficient (hundreds of W to kW); quality varies (e.g. NCP2704, LX1720, XMA2012 2 x 3 W modules) | f_carrier >> f_audio; output LPF required | carrier frequency | Power amplifiers | sim | p.952-954, Fig. 16.8-16.9 | high |
| SCHERZ-2267 | emc | Hum reduction in audio amplifiers: maximize supply smoothing capacitance, keep PCB tracks and wires short, use screened (shielded) cable with the screen grounded, avoid earth (ground) loops | - | layout, cabling | Audio equipment (60-Hz hum) | inspect | p.954, 967 | high |
| SCHERZ-2268 | components | Loudspeaker loading: treat the speaker as its nominal impedance; I = Vout/Z; paralleled speakers lower the load (2 x 8 ohm = 4 ohm; 2 x 4 ohm = 2 ohm) and raise amplifier current; padding with a series power resistor (4 + 4 = 8 ohm) degrades sound; impedance-matching transformers are costly | I = Vout/Z_spk; Z_par = Z/n | Z_spk, n | Amplifier-speaker matching | calc | p.956, Fig. 16.12 | high |
| SCHERZ-2269 | components | Driver bands: woofers < ~200 Hz; midrange ~500-3000 Hz; tweeters above midrange; full-range drivers ~100-15,000 Hz (inferior to multi-way systems) | - | band | Speaker systems | review | p.957 | high |
| SCHERZ-2270 | filter | First-order passive crossover (Fig. 16.13): values from the -3-dB points and nominal driver impedances; practical 2-way example at 1.8 kHz for 8-ohm drivers: tweeter C 8 uF + L 0.57 mH + R 2 ohm, woofer L 0.65 mH + R 7 ohm + C 8 uF (18 x 12 x 8-in fiberboard box); active crossovers (before the power amp) e.g. ~600 Hz, 18 dB/octave with LF356 | C1 = 1/(2*pi*f2*Rt); L1 = Rm/(2*pi*f2); C2 = 1/(2*pi*f1*Rm); L2 = Rw/(2*pi*f1) | f1, f2, Rt, Rm, Rw | Speaker crossovers | calc | p.957-958, Fig. 16.13-16.15 | high |
| SCHERZ-2271 | components | LM386 low-power amp: gain 20 (200 with 10 uF across pins 1-8); inputs ground-referenced, output self-biased to Vs/2; 220-uF output coupling cap and 10-ohm + 0.1-uF output network into 8 ohm; supply printed as +4 to +15 V on p.959 but +4 to +12 V in Fig. 16.16 and p.647 - use the datasheet | G = 20..200; Vs 4-12 V (conservative) | gain, supply | Small speakers | inspect | p.959, Fig. 16.16 | high |
| SCHERZ-2272 | components | LM383 power amp: drives 4 ohm (or two 8 ohm in parallel); thermal shutdown; needs a heat sink to avoid shutting down below rated power; 8-W circuit on +5 to +20 V with 2000-uF output coupling and 2.2-ohm + 0.2-uF output network; two in bridge for 16 W | Z_load >= 4 ohm; heat sink required | load, supply | Power audio | inspect | p.959, Fig. 16.17 | high |
| SCHERZ-2273 | hw-fw | Buzzers from logic: drive through a transistor with ~1k base resistor (active-high or active-low variants); series resistor (e.g. 100k pot) for volume; tone generators: 555 astable, UJT or complementary-transistor oscillators into 8-ohm speakers (add an amplifier to boost the 555 output) | R_base ~ 1k | buzzer current | Audible alerts | inspect | p.960-961, Fig. 16.19-16.21 | medium |
| SCHERZ-2274 | process | Before designing complex functions from discrete parts, check for a dedicated IC or module (examples: HT9200 DTMF, TDA7052 1-W and TDA2003 10-W audio amps, L298 2 x 2-A H-bridge, S202T01F 2-A 600-V SSR, MAX1551 Li-polymer charger, L297 stepper controller, MAX6958 I2C LED driver, LM3914 10-LED bar graph, LM3404 1-A constant-current LED driver, DS1302 RTC, 24C1024 I2C EEPROM, SST25VF010A 1-Mbit SPI flash) | - | function list | Architecture/BOM reduction | review | p.963-964, Table 17.1 | high |
| SCHERZ-2275 | rf | RF design needs critical PCB layout - prefer ready-made RF modules (soldered or socketed) for 433/315-MHz links, Bluetooth, Wi-Fi, XBee-footprint radios, GSM/GPRS modems, GPS | - | RF function | RF subsystems | review | p.964-967, Table 17.2 | high |
| SCHERZ-2276 | rf | 433/315-MHz ASK modules: low cost and power; data rate usually <= 8 kb/s (2 kb/s common); range about 100 yards outdoors, much less indoors; separate TX/RX (one-way links) | R_b <= 8 kb/s; range ~100 yd | data rate, range | Remote control, sensors | calc | p.966-967, Fig. 17.1 | high |
| SCHERZ-2277 | hw-fw | Bluetooth modules are typically 3.3-V parts; use a level-converting carrier to interface 5-V TTL serial; XBee-socket modules act as transparent serial links; GSM/GPRS modems are commanded over serial | V_module = 3.3 V | host logic level | Wireless modules | inspect | p.967 | high |
| SCHERZ-2278 | process | Prototype with breakout boards/modules (SMD pins broken out to 0.1-in, often with decoupling, regulator, level conversion), then move to a final design without the module | pitch 0.1 in | - | Prototyping | review | p.963-964 | medium |
| SCHERZ-2279 | requirements | US service voltages (nominal, vary by region): homes 240/120 V single-phase 3-wire (center-tapped); industry 480/277 V 3-phase 4-wire Y, 208/120 V 3-phase 4-wire Y, 240/120 V 3-phase 4-wire delta (center-tapped), 240 V 3-phase 3-wire delta; distribution chain 10 kV generation -> 220 kV transmission -> 66/33 kV -> 16/4 kV local | V_home = 120/240 V, 60 Hz | region | Mains-powered product input range | review | p.973-974, Fig. A.1 | high |
| SCHERZ-2280 | protection | On a 240/120-V center-tapped delta service the third ("stinger", wild) leg is 187 V to neutral; connecting a 120-V load across it destroys the load | V_stinger = 187 V | service type | Industrial installs | inspect | p.974, Fig. A.1 | high |
| SCHERZ-2281 | power | Three-phase relations: Y connection line voltage = sqrt(3) x phase voltage (OCR prints "about 3 times"), line currents 30 deg from line voltages, balanced load -> no neutral current; delta: phase voltage = line voltage, line current = sqrt(3) x phase current | V_L = sqrt(3)*V_P (Y); I_L = sqrt(3)*I_P (delta) | V_P, I_P | 3-phase supplies | calc | p.974-975, Fig. A.3-A.4 | high |
| SCHERZ-2282 | power | Sine RMS relation used for mains ratings | Vrms = 0.707*V0 (V0/sqrt(2)) | V0 | AC ratings | calc | p.974, Fig. A.2 | high |
| SCHERZ-2283 | compliance | US home wiring conventions: hot conductors black (second hot of a 240-V circuit red), neutral white, ground green or bare; 120 V hot-to-neutral, 240 V hot-to-hot; neutral and ground bars bonded only in the main service panel, never in subpanels (subpanel gets a ground wire from the main panel, or its own ground rod in a separate building); single-pole breakers for 120 V, double-pole for 240 V; 120/240-V appliances need 4-wire cable; balance loads between the A and B phases; practices vary locally - check with the electrical inspector | - | installation | Line-powered products and bench wiring | inspect | p.976-977, Fig. A.5 | high |
| SCHERZ-2284 | requirements | International mains: US 120 V/60 Hz homes (208/120-V 3-phase industry); most other countries 230 V/50 Hz single-phase and 415 V 3-phase; a 120-V/60-Hz device may be damaged on 230 V; a step-down converter does not fix the 50-Hz difference (most devices tolerate it, frequency-dependent ones may not) - design universal-input supplies for export products | see Table S2-A.1 | target markets | Export products | review | p.977-978, Fig. A.6 | high |
| SCHERZ-2285 | test | Quote every measurement with its uncertainty; error sources: real variation of the quantity (e.g. temperature coefficients), instrument error (calibration, input impedance), human reading error (graphical scope ~5 %) | relative error = dx/x; percent = 100*dx/x; tolerance -> dx = x*tol (3300 ohm 5 % -> +/-165 ohm, 3135-3465 ohm) | x, dx, tol | Test reports | calc | p.979-980 §B.1 | high |
| SCHERZ-2286 | test | Error propagation: sums/differences add absolute errors (worst case) or in quadrature (independent Gaussian); products/quotients add relative errors (worst case) or in quadrature; powers multiply relative error by the exponent; general case dR = sum(df/dxi * dxi); avoid measuring a small difference of two large quantities (relative error explodes) | dz = sqrt(dx^2 + dy^2) (sum); dz/z = sqrt(sum((dxi/xi)^2)) (product); dz/z = n*dx/x (power) | measured values and errors | Measurement planning | calc | p.980-982 §B.2 | high |
| SCHERZ-2287 | test | Worked propagation examples: 6.24 V +/- 0.01 V + 14.3 V +/- 0.2 V = 20.5 V +/- 0.2 V; 1.256 A +/- 0.005 A through 180 ohm 5 % -> 226 V +/- 11 V | as shown | - | Uncertainty examples | calc | p.982 | high |

## 2. Formulas & tables (numbers)

### S2-7 Test equipment and hand assembly (Ch. 7, §7.4.6-7.5.23)

**Table S2-7.1 Oscilloscope probe classes (Table 7.2, Fig. 7.58, p.602-606)**

| Probe | Input R / C | Attenuation | Bandwidth | Voltage limit | Notes |
|---|---|---|---|---|---|
| 1X passive | 1 Mohm scope / high C | 1:1 | ~4-34 MHz | ~400-500 V | heaviest capacitive loading |
| 10X passive | 9 Mohm tip + 1 Mohm scope = 10 Mohm; ~1/10 the C of 1X | 10:1 | ~60-300 MHz | < 500 V (400-500 V rating) | compensate on 1-10 kHz cal square |
| 100X / 1000X passive | - | 100:1 / 1000:1 | lower than 10X | ~1.4 kV / ~20 kV | |
| Low-Z (Z0) divider | 450 ohm (10:1) or 950 ohm (20:1) tip into 50 ohm; < 1 pF | 10:1 / 20:1 | GHz range, rise <= 100 ps | < 50 V | needs 50-ohm scope input; heavy resistive load |
| HV passive | e.g. 500 Mohm tip | selectable | lower | > 500 V; P6015A 20 kV rms dc, 40 kV pulse, 75 MHz | |
| Active FET | very high R, ~1 pF | - | 500 MHz-4 GHz (to 6 GHz) | +/-0.6 to +/-10 V range, +/-40 V abs max | source R 0-10 kohm; ESD sensitive |
| Active differential | - | - | ~1 GHz | limited range | CMRR 3000:1 @ 1 MHz; 60 dB @ 1 MHz -> 30 dB @ 1 GHz |
| Current (transformer) | - | - | few hundred Hz - ~1 GHz | - | ac only |
| Current (Hall + transformer) | - | - | dc - ~50 MHz | - | |

**Table S2-7.2 Scope bandwidth / sampling rules (p.598-600)**

| Quantity | Rule |
|---|---|
| Frequency / timing measurement | BW >= 3-5 x fundamental |
| Amplitude measurement | BW >= 10 x frequency |
| See nth harmonic | BW >= n x f0 (5th harmonic of 100 MHz -> 500 MHz) |
| Sample rate (with reconstruction) | fs >= 4 x BW |
| Sample rate (no reconstruction) | fs >= 10 x BW |
| Coax probe-extension capacitance | ~100 pF/m |
| Typical 1-Mohm scope input C | 20 pF (5-100 pF range) |
| Scope frequency accuracy | ~5 % or worse (use a counter) |

**Table S2-7.3 Capacitor dielectric by value range (substitution box, p.616)**

| Range | Dielectric |
|---|---|
| 10-150 pF (variable) | plastic-film or air tuning capacitor |
| 100-900 pF | mica |
| 0.001-0.009 uF | polystyrene |
| 0.01-0.9 uF | polycarbonate |
| 1-9 uF | polyester |
| >= 10 uF | tantalum or aluminum electrolytic (polarized) |

**Table S2-7.4 Hand-soldering parameters (p.618-619)**

| Item | Value |
|---|---|
| Iron, general | 25-40 W pencil |
| Iron, very small pads | 15 W |
| Iron, very large joints | 50 W |
| Chisel tip width, general | 0.05-0.08 in |
| Tip temperature, SnPb | ~330 C (625 F) |
| Tip temperature, lead-free | ~400 C (750 F) |
| 60/40 and 63/37 melting point (as printed) | 361 F |
| Solder wire 25 ga | 0.020 in / 0.508 mm - small pads, hand SMD |
| Solder wire 21 ga | 0.031 in / 0.79 mm - general PCB |
| Solder wire 19 ga | 0.040 in / 1 mm - >= 14 AWG wire, terminals, chassis |

**Formulas (scope, §7.4.6)**
- V = (divisions) x (VOLT/DIV); T = (divisions) x (SEC/DIV); f = 1/T. Example Fig. 7.39: 6 div x 2 V/div = 12 Vpp; 4 div x 10 ms = 40 ms -> 25 Hz.
- Phase factor theta_f = 360 deg / T_R(div); phase = phi(div) x theta_f.
- Shunt current I = V/R; shunt rating P >= 2 ohm x Imax^2 (1-ohm shunt).
- Tilt % = A/B x 100; overshoot % = C/D x 100 (Fig. 7.45).

### S2-8 Operational amplifiers and comparators (Ch. 8)

**Table S2-8.1 Sample op-amp specifications (Table 8.1, p.649)** (GAIN MIN header OCR reads "(mA)"; values are open-loop gain in dB)

| Type | Part | Supply min-max (V) | Supply current (mA) | Vos typ / max (mV) | Ibias max (nA) | Ios max (nA) | Slew typ (V/us) | fT typ (MHz) | CMRR min (dB) | Gain min (dB) | Iout max (mA) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Bipolar | 741C | 10-36 | 2.8 | 2 / 6 | 500 | 200 | 0.5 | 1.2 | 70 | 86 | 20 |
| MOSFET | CA3420A | 2-22 | 1 | 2 / 5 | 0.005 | 0.004 | 0.5 | 0.5 | 60 | 86 | 2 |
| JFET | LF411 | 10-36 | 3.4 | 0.8 / 2 | 0.2 | 0.1 | 15 | 4 | 70 | 88 | 30 |
| Bipolar precision | LM10 | 1-45 | 0.4 | 0.3 / 2 | 20 | 0.7 | 0.12 | 0.1 | 93 | 102 | 20 |

**Table S2-8.2 Op-amp input technology comparison (p.646)**

| Property | Bipolar | JFET | MOSFET |
|---|---|---|---|
| Input bias current | nA | low pA | down to a few tenths of pA |
| Input resistance | ~1e6 ohm | ~1e12 ohm | - |
| Offset voltage | low | medium | medium to high |
| Offset drift | low | medium | medium |
| Bias matching | excellent | fair | fair |
| Bias vs temperature | low | fair | fair |
| Special hazard | needs bias-comp resistor | phase inversion near negative rail | - |

**Other op-amp numbers:** open-loop gain 1e4-1e6 (80-120 dB), gain in dB = 20 log10(A); fT typically ~1 MHz (1-10 MHz); Rout 10-1000 ohm; 741 slew 0.5 V/us, HA2539 600 V/us; input clamp limit rails +/-0.7 V; bypass 0.1 uF ceramic or 1 uF tantalum; comparator pull-up few hundred ohm to few kohm; logic pull-ups 10k (TTL), 100k (CMOS); audio band 20-20,000 Hz (p.638-658).

**Formula sheet (Ch. 8)**
- Open loop: Vout = Ao*(V+ - V-); with negative feedback V+ = V- (rule 4).
- Inverting: G = -R2/R1; noninverting: G = 1 + R2/R1; summer: Vout = -Rf*sum(Vi/Ri); difference: Vout = (R2/R1)(V2 - V1).
- Integrator: Vout = -(1/RC) integral(Vin dt); differentiator: Vout = -RC dVin/dt.
- Bias compensation: Rcom = R1*R2/(R1+R2).
- Op-amp hysteresis comparator: VT = +/-Vsat*R1/R2; Vh = 2*Vsat*R1/R2.
- Inverting comparator w/ hysteresis: Vref1 = Vs*R2(R1+R3)/(R1R2+R1R3+R2R3); Vref2 = Vs*R2R3/(R1R2+R1R3+R2R3); dVref = Vs*R1R2/(R1R2+R1R3+R2R3).
- Noninverting comparator w/ hysteresis: Vin1 = Vref(R1+R2)/R2; Vin2 = (Vref(R1+R2) - Vcc*R1)/R2; dVin = Vcc*R1/R2.
- In-amp: G = (1 + 2R1/Rg)(R3/R2).
- V-to-I: Iout = Vin/R2; transimpedance: Vout = Iin*RF; precision sink: Iload = Vin/R2.
- Single-supply coupling: C = 1/(2*pi*f3dB*R).

### S2-9 Filters (Ch. 9)

**Table S2-9.1 Butterworth normalized passive LC low-pass values (Table 9.1, p.669)** - 1-ohm load, -3 dB at 1 rad/s, units H and F; pi row labels RS, C1, L2, C3, L4, C5, L6, C7; T row labels {1/RS}, {L1}, {C2}, {L3}, {C4}, {L5}, {C6}, {L7}.

| n | RS | C1 {L1} | L2 {C2} | C3 {L3} | L4 {C4} | C5 {L5} | L6 {C6} | C7 {L7} |
|---|---|---|---|---|---|---|---|---|
| 2 | 1.000 | 1.4142 | 1.4142 | | | | | |
| 3 | 1.000 | 1.0000 | 2.0000 | 1.0000 | | | | |
| 4 | 1.000 | 0.7654 | 1.8478 | 1.8478 | 0.7654 | | | |
| 5 | 1.000 | 0.6180 | 1.6180 | 2.0000 | 1.6180 | 0.6180 | | |
| 6 | 1.000 | 0.5176 | 1.4142 | 1.9319 | 1.9319 | 1.4142 | 0.5176 | |
| 7 | 1.000 | 0.4450 | 1.2470 | 1.8019 | 2.0000 | 1.8019 | 1.2470 | 0.4450 |

Scaling: L = RL*L_table/(2*pi*f3dB); C = C_table/(2*pi*f3dB*RL). (Table title printed as "Butterworth Active Filter Low-Pass Values", but it is the passive LC ladder table.)

**Table S2-9.2 Butterworth normalized active low-pass values (Table 9.2, p.676)** - unity-gain sections, all R = 1 ohm; 2-pole section uses C1, C2; 3-pole uses C1, C2, C3.

| Order n | Sections | Section | C1 | C2 | C3 |
|---|---|---|---|---|---|
| 2 | 1 | 2-pole | 1.414 | 0.7071 | |
| 3 | 1 | 3-pole | 3.546 | 1.392 | 0.2024 |
| 4 | 2 | 2-pole | 1.082 | 0.9241 | |
| | | 2-pole | 2.613 | 0.3825 | |
| 5 | 2 | 3-pole | 1.753 | 1.354 | 0.4214 |
| | | 2-pole | 3.235 | 0.3090 | |
| 6 | 3 | 2-pole | 1.035 | 0.9660 | |
| | | 2-pole | 1.414 | 0.7071 | |
| | | 2-pole | 3.863 | 0.2588 | |
| 7 | 3 | 3-pole | 1.531 | 1.336 | 0.4885 |
| | | 2-pole | 1.604 | 0.6235 | |
| | | 2-pole | 4.493 | 0.2225 | |
| 8 | 4 | 2-pole | 1.020 | 0.9809 | |
| | | 2-pole | 1.202 | 0.8313 | |
| | | 2-pole | 2.000 | 0.5557 | |
| | | 2-pole | 5.758 | 0.1950 | |

Scaling: C = C_table/(Z*2*pi*f3dB); R = Z*R_table (Z typically 10 kohm). High-pass: R_hp = 1/C_table, C_hp = 1/R_table (=1 F) then scale. Fig. 9.18 shows C3 = 0.2020 for n = 3 (table: 0.2024).

**Table S2-9.3 Butterworth order selection read from Fig. 9.6 (worked examples, p.667-679)** (graph-derived, conf medium)

| As (normalized stop freq, rad/s) | Required stop attenuation | Order n chosen in book | Exact Butterworth A(n) = 10log10(1+As^2n) (recomputed) |
|---|---|---|---|
| 1.7 | >= 20 dB (figure annotates -15 dB) | 3 | 14.0 dB - does NOT meet 20 dB (n = 5 gives 23.1 dB) |
| 1.88 | >= 20 dB (figure annotates -15 dB) | 3 | 16.5 dB - does NOT meet 20 dB (n = 4 gives 21.9 dB) |
| 3 | >= 25 dB | 3 | 28.6 dB |
| 3.3 | >= 30 dB | 3 | 31.1 dB |
| 3.3 | >= 45 dB | 5 | 51.9 dB |
| 3.3 | >= 50 dB | 5 | 51.9 dB |
| 4 | >= 60 dB | 5 | 60.2 dB |

Butterworth asymptote: 6n dB/octave (20n dB/decade). The recomputed column uses the standard Butterworth magnitude, which the book does not print (conf medium).

**Filter formulas (Ch. 9)**
- f0 = sqrt(f1*f2); f0 ~ (f1+f2)/2 when f2/f1 < 1.1; Q_bp = f0/(f2 - f1); notch Q = f0/BW (p.680; p.665 prints (f2 - f1)/f0).
- RC: fc = 1/(2*pi*RC); RL: fc = R/(2*pi*L); LC: f0 = 1/(2*pi*sqrt(LC)).
- LP As = fs/f3dB; HP As = f3dB/fs; narrow BP As = BW_stop/BW_3dB with fa*fb = f0^2 (take tighter pair); notch As = BW_3dB/BW_stop.
- Resonating elements: L_par = 1/((2*pi*f0)^2*C); C_ser = 1/((2*pi*f0)^2*L).
- MFB narrow BP: R1 = Q/(2*pi*f0*C); R2 = R1/(2Q^2 - 1); R3 = 2R1.
- Active notch: R1 = 1/(2*pi*f0*C); K = (4Q - 1)/(4Q).
- MF5: f0 = (fclk/50)*sqrt(R2/R4); Q = (R3/R2)*sqrt(R2/R4); gains -R4/R1 (LP), -R3/R1 (BP), -R2/R1 (HP).

### S2-10 Oscillators and timers (Ch. 10)

**Table S2-10.1 Sample 555 specifications (Table 10.1, p.690)** (reconstructed from column-scrambled OCR; "-" = not given)

| Type | Supply min (V) | Supply max (V) | Supply current typ @5 V (uA) | max (uA) | Trig/thresh current typ (nA) | max (nA) | Typ. max frequency (MHz) | Iout source (mA) | Iout sink (mA) |
|---|---|---|---|---|---|---|---|---|---|
| SN555 (bipolar) | 4.5 | 18 | 3000 | 5000 | 100 | 500 | 0.5 | 200 | 200 |
| ICL7555 (CMOS) | 2 | 18 | 60 | 300 | - | 10 | 1 | 4 | 25 |
| TLC555 (CMOS) | 2 | 18 | 170 | - | 0.01 | - | 2.1 | 10 | 100 |
| LMC555 (CMOS) | 1.5 | 15 | 100 | 250 | 0.01 | - | 3 | - | - |
| NE555 (bipolar) | 4.5 | 15 | - | 6000 | - | - | - | - | 200 |

**Table S2-10.2 Oscillator stability and Q (p.696)**

| Class | Frequency stability | Resonator Q |
|---|---|---|
| RC relaxation | ~0.1 % | - |
| LC | ~0.01 % at best | a few hundred |
| Crystal | 0.01-0.001 % | ~100,000 |

**Table S2-10.3 Crystal equivalent-circuit values (p.697)**

| Crystal | L1 | C1 | R1 | C0 |
|---|---|---|---|---|
| 1 MHz | 3.5 H | 0.007 pF | 340 ohm | 3 pF |
| 10 MHz fundamental | 9.8 mH | 0.026 pF | 7 ohm | 6.3 pF |

Crystal ranges: fundamental ~10 kHz-30 MHz; overtone to a few hundred MHz (e.g. 15 MHz fund -> 45 MHz 3rd, 75 MHz 5th, 135 MHz 9th overtone).

**Timing formulas (Ch. 10)**
- Op-amp relaxation (R2 = R3): T = 2.2*R1*C.
- Triangle/square: T = 4*VT*R1*C/Vsat.
- UJT: f = 1/(RE*CE*ln(1/(1-eta))), eta ~ 0.5.
- CMOS 2-inverter: f = 1/(4RC ln2) ~ 1/(2.8RC).
- 555 astable: t_low = 0.693 R2 C1; t_high = 0.693 (R1+R2) C1; f = 1.44/((R1+2R2)C1); with diode across R2: t_high = 0.693 R1 C1.
- 555 monostable: t = 1.10 R1 C1. Component window 10 kohm-14 Mohm, 100 pF-1000 uF.
- NE566: f = 2(VCC - Vin)/(R1 C1 VCC), 0.75 VCC <= VC <= VCC, 2k < R1 < 20k.
- Wien: f0 = 1/(2*pi*RC), gain 3. LC tank: f = 1/(2*pi*sqrt(LC)); Colpitts Ceff = C1C2/(C1+C2); Clapp Ceff = 1/(1/C1+1/C2+1/CT).

### S2-11 Regulators and power supplies (Ch. 11)

**Table S2-11.1 Rectifiers (p.704)**

| Part series | Type | Current (A) | Forward drop (V) |
|---|---|---|---|
| 1N4001-1N4007 | diode | 1 | 0.9 |
| 1N5059-1N5062 | diode | 2 | 1.0 |
| 1N5624-1N5627 | diode | 5 | 1.0 |
| 1N1183A-1N1190A | diode | 40 | 0.9 |
| Schottky | diode | - | < 0.4 (lower breakdown) |
| 3N246-3N252 | bridge | 1 | 0.9 |
| 3N253-3N259 | bridge | 2 | 0.85 |
| Typical rectifier range | - | 1-25 | PIV 50-1000 V, surge 30-400 A |

**Table S2-11.2 Linear regulators (p.701-702, 708-709)**

| Part | Output | Max current | Input limit | Headroom | Ripple rejection |
|---|---|---|---|---|---|
| 78xx | +5, 6, 8, 10, 12, 15, 18, 24 V | 1.5 A (heat-sunk) | - | >= 2 V (p.702); 3 V used for 7805 (p.708) | ~60 dB (7805) |
| 79xx | negative fixed | 1.5 A | - | - | - |
| LM317 | 1.25-37 V | 1.5 A | 37 V | >= 2 V | ~65 dB; ~80 dB with 10-uF ADJ bypass |
| LM337 | -1.2 to -37 V | 1.5 A | -1.5 to -38 V in | - | - |
| TL783 | 1-125 V | 700 mA | - | - | - |
| LM2940 (LDO) | fixed | - | - | ~0.5 V | - |

**Table S2-11.3 Commercial supply packages (p.714-715)**

| Package | Linear power | Switching power | Notes |
|---|---|---|---|
| Small module (~2.5 x 3.5 x 1 in) | 1-10 W | 10-25 W | +5, +/-10, +/-15 V; user adds fuse/switch/filter |
| Open frame | 10-200 W | 20-400 W | user adds fuse/switch/filter |
| Enclosed | 10-800 W | 20-1500 W | |
| Wall adapter | - | typ. 12 V 2 A for < $10 | +3, 5, 6, 7.5, 9, 12, 15 V; 6.3-mm plug |

**Supply formulas (Ch. 11)**
- LM317: Vout = 1.25 V (1 + R2/R1); LM337: Vout = -1.25 V (1 + R2/R1).
- Ripple: I = C dV/dt; full-wave 60 Hz period 8.3 ms (discharge ~5 ms, charge ~3.3 ms); Vripple(rms) = 0.0024 s x IL/Cf.
- Regulator ripple rejection: Vout/Vin = 10^(-RR/20) (60 dB -> 1/1000; 80 dB -> 1/10,000).
- 12.6 V rms secondary -> 17.8 V peak (p.709); 12.6 V CT -> 8.9 V peak after rectification (p.704).
- Crowbar trip Vz + 0.6 V; current regulator IL = Vreg/R1.
- Efficiency: linear < 50 %; switcher > 85 %; density 0.4 vs 0.9 W/in^3.

### S2-12 Digital electronics (Ch. 12)

**Table S2-12.1 Logic levels quoted in the book**

| Family / condition | VIH | VIL | VOH | VOL | Supply | Source |
|---|---|---|---|---|---|---|
| Generic example | 2.4-5 V | 0-0.8 V | - | - | 5 V | p.718 |
| 74HC @ 5 V (Fig. 12.52) | >= 3.5 V | <= 1.0 V | >= 4.4 V | <= 0.1 V | 2-6 V | p.727, 755 |
| 74HC @ 5 V (prose, inconsistent) | 2.5-5 V | 0-2.1 V | - | - | - | p.727 |
| CMOS 4000B @ 5 V | 3.3-5 V | 0-1.7 V | 4.9-5 V | 0-0.1 V | - | p.727 |
| CMOS 4000B general | >= 2/3 VDD | <= 1/3 VDD | - | - | 3-18 V | p.754 |
| 74LS (pull-up/down examples) | - | ~0.8 V max | - | - | 5 V; IIH ~20 uA, IIL ~400 uA | p.779-780 |
| 74LS14 Schmitt (@ 5 V) | VT+ ~1.7 V | VT- ~0.9 V | ~3.4 V | ~0.2 V | 5 V | p.788 |

Derived noise margins (74HC-74HC, Fig. 12.52): NM_H = 4.4 - 3.5 = 0.9 V; NM_L = 1.0 - 0.1 = 0.9 V (conf medium). Fanout 74HC ~50 (p.756). Supply-rail noise budget for logic: 200-mV noise margin (p.707).

**Table S2-12.2 Flip-flop / one-shot timing numbers**

| Parameter | Value | Source |
|---|---|---|
| Setup time ts (typical; 7474; 74LS76 min) | ~20 ns | p.766, 773-774 |
| Hold time th (most flip-flops) | 0 ns | p.774 |
| tPLH / tPHL (typical flip-flop) | ~20 ns | p.774 |
| Standard TTL flip-flop propagation delay | 30 ns (4-stage ripple = 120 ns) | p.772 |
| Switch bounce duration | typically <= 50 ms | p.761 |
| Logic probe min pulse / max train | ~10 ns / ~100 MHz | p.758 |
| 74121 tw | Rext*Cext*ln 2 (max ~28 s) | p.776 |
| 74123 tw (Cext > 1000 pF) | 0.28*Rext*Cext*(1 + 0.7/Rext) | p.776 |
| Power-up clear release (74LS76) | CLR >= 2.0 V | p.778 |
| SAR ADC conversion | ~10-300 us | p.811 |
| LCD switching time | 40-100 ms | p.816 |
| LCD ac drive frequency | ~25 Hz to a couple hundred Hz | p.817 |
| Memory access time | ~10 ns to a couple hundred ns | p.832 |
| DRAM refresh (example device) | every 2 ms or sooner | p.839 |

**Table S2-12.3 Clock generators (Fig. 12.79, p.775)**

| Circuit | Frequency relation | Values / range |
|---|---|---|
| 2 x 74HC04 RC | f = 1/(R1*C), R2 = 10*R1 | R1 100k, R2 1M, C 0.01 uF |
| 74HC04 with hysteresis | f ~ 1/(1.2*R1*C1), R3 = 10*R2, R2 = 10*R1, C1 = 100*C2 | - |
| 4011 gated NAND RC | - | up to ~2 MHz; R1 1M, R2 100k, C 0.01 uF |
| 74LS00 SR latch RC (1k) | - | 1 Hz < f < 10 MHz; 10 pF < C < 50 uF |
| CMOS crystal (74HC04) | crystal f0 | R 100k, C 100 pF |
| 555 + 74LS76 toggle | tLOW = 0.693*R2*C; tHI = 0.693*R1*C; toggle -> 50 % | - |
| 74S124 VCO | f vs Cext graph | 0.1 Hz-100 MHz (Cext 1e-12..1e-2 F), VCC 5 V, Vfreq = VRNG = 2 V |

**Table S2-12.4 Memory technologies (p.832-840)**

| Technology | Volatile | Endurance / retention | Program / erase |
|---|---|---|---|
| Mask ROM | no | permanent | mask > $1,000; economical > ~2,000 units |
| PROM | no | one-time | fuse blow ~21 V pulses (obsolete) |
| EPROM | no | charge retained decades; a couple hundred reprogram cycles | ~12 V programming; UV erase ~20 min |
| EEPROM | no | ~100,000 write cycles; slow writes | byte-selective electrical erase |
| Flash | no | fast write/erase | block or word erase |
| SRAM | yes | unlimited | - |
| Battery-backed SRAM | no (battery) | ~10 years (lithium) | - |
| NOVRAM | no | ~10,000 store cycles | SRAM + shadow EEPROM |
| DRAM | yes | refresh <= 2 ms (example) | - |

**Table S2-12.5 Address lines vs locations (Table 12.2, p.830-831)** - n lines -> 2^n locations: 8 -> 256; 9 -> 512; 10 -> 1,024 (1K); 11 -> 2,048; 12 -> 4,096; 13 -> 8,192; 14 -> 16,384; 15 -> 32,768; 16 -> 65,536 (64K); 17 -> 131,072; 18 -> 262,144; 19 -> 524,288 (printed "540 K"; = 512K); 20 -> 1,048,576 (1M); 21 -> 2M; 22 -> 4M; 23 -> 8M; 24 -> 16M; 25 -> 33,554,432 (32M).

**Converter / interface formulas (Ch. 12)**
- LSB = FS/2^n; FS output = (2^n - 1)/2^n x Vref.
- Weighted DAC: Vout = -Vref*RF/Rin; R-2R: I = Vref/R, bit currents I/2 ... I/2^n, Vout = -Isum*RF.
- DAC0808: Iout = Iref*code/256; Vout = Iout*Rf.
- Pull-up: Vin = VCC - IIH*R; pull-down: Vin = IIL*R; PD = VCC^2/R.
- Fanout = min(IOL/IIL, IOH/IIH).
- Power-up RC: V = VCC(1 - e^(-t/RC)), 63 % at t = RC, ~100 % at 5RC.
- LM35: 10 mV/degC; LM34: 10 mV/degF.

### S2-13 Microcontrollers and interfacing (Ch. 13)

**Table S2-13.1 Microcontroller / board resources quoted**

| Device / board | Flash / program | SRAM | EEPROM | Clock / supply | I/O limits | Source |
|---|---|---|---|---|---|---|
| ATtiny85 | 8 kB | 256 B | 512 B | 2.7-5.5 V @ <= 10 MHz; 300 uA @ 1 MHz; 0.1 uA power-down | 6 I/O (PB0-PB5) | p.845-846 |
| PIC16C56 / PIC16C57 | 1024 / 2048 words | 32 B direct (bank-switched more) | - | 20 MHz -> 5 MIPS; crystal/ceramic resonator required | 12 / 20 I/O | p.849-850 |
| BASIC Stamp II (PIC16C57) | 2048 B EEPROM (~500-600 lines) | - | shared | 5 V regulator in >5-15 V, 50 mA out; ~3-4 MIPS PBASIC; sleep ~50 uA | 20 mA src / 25 mA sink per pin; 40/50 mA per 8-pin group | p.852-858 |
| dsPIC | - | 2 kB | - | 16-bit, 40 MHz | - | p.863 |
| Arduino Uno (ATmega328) | 32 kB | 2 kB | 1 kB | 7-12 V dc jack or USB | 14 digital + 6 analog; 40 mA/pin, 200 mA/chip abs max (derate 25 %) | p.864-866, 879 |
| Arduino Mega 2560 | 256 kB | 8 kB | 4 kB | - | 54 digital + 16 analog, 4 UARTs | Table 13.3 |
| Arduino Lilypad | 16 kB | 1 kB | 512 B | 8 MHz | 14 digital + 6 analog | Table 13.3 |
| Ardumoto shield | - | - | - | - | dual H-bridge, up to 2 A per channel | Table 13.5 |

**Table S2-13.2 Serial buses (p.885-892)**

| Bus | Wires | Speed | Topology | Electrical | Notes |
|---|---|---|---|---|---|
| 1-Wire | 1 data + GND (parasitic) | slow; bit 0 = 60 us, bit 1 = 15 us, reset >= 480 us | multi-drop, up to 255 devices, 64-bit IDs | 5 V or 3.3 V, 4.7-kohm pull-up | DS18B20 750-ms conversion, 0.0625 degC/LSB |
| I2C (TWI) | SDA, SCL (+ power) | up to 400 kbit/s | multi-master bus, addressed | open-drain, pull-ups (4.7 kohm example), 5 V or 3.3 V | level-shift with TXS0102/MAX3372/PCA9509/PCA9306 |
| SPI | SCLK, MOSI, MISO, SS per slave | up to 80 Mbit/s | single master, SS per slave | push-pull | bit order device-specific; ICSP on AVR |
| TTL serial (UART) | Tx, Rx | 110-256000 baud (9600 common) | point-to-point | logic levels (not RS-232) | 8N1, LSB first |

Standard baud rates: 110, 300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 38400, 57600, 115200, 128000, 256000 (p.891).

**Interface formulas (Ch. 13)**
- Divider scaling: V_pin = V_in*R2/(R1+R2); 10k/1k -> 1:11 (0-50 V usable with 5.1-V zener clamp).
- Charlieplexing: N_LED = n^2 - n.
- Servo: 1.0-2.0 ms pulse per ~20 ms frame; 1.5 ms center.
- Button ladder (Freetronics, 10-bit): 0, 145, 329, 505, 741 counts for 0.00, 0.71, 1.61, 2.47, 3.62 V.
- MCU pin current: ~20 mA general; ATmega 40 mA/pin, 200 mA/chip (x0.75 production).

### S2-14/15 Programmable logic and motors (Ch. 14-15)

**Table S2-15.1 Motor / driver numbers**

| Item | Value | Source |
|---|---|---|
| DC motor speed / rated voltage | 3000-8000 rpm at 1.5-24 V | p.933 |
| DC motor stall threshold | < ~50 % of rated voltage | p.934 |
| DC motor overheat threshold | > ~30 % above rated voltage | p.934 |
| Loaded vs no-load current | up to 1000 % or more | p.934 |
| RC servo travel | ~180 or 210 deg | p.937 |
| RC servo pulse / frame | 1-2 ms (1.5 ms neutral; some 1.25-1.75 ms) / 20-30 ms | p.937 |
| RC servo supply | 4.8 V (some ~6.0 V) | p.937-938 |
| Stepper step angle | 0.72-90 deg; common 15, 30 deg | p.938 |
| Power stepping | ~1.4x torque, 2x power | p.941 |
| L293 | 1 A per winding, up to 36 V | p.943 |
| L298 | 2 A per winding | p.943 |
| LMD18200 | 3 A, 12-55 V, internal diodes, thermal warning | p.936, 943 |
| SAA1027 | 9.5-18 V; VIH >= 7.5 V, VIL <= 4.5 V; 500 mA out | p.945 |
| Stepper driver supply (examples) | 5-24 V (Vmotor) | p.942 |
| RC radio bands (US) | 72 MHz ch 11-60 aircraft (no licence); 50 MHz (ham); 27 MHz any model | p.938 |

**Table S2-15.2 Stepper lead identification (p.945-946, Fig. 15.14)**

| Leads | Type | Ohmmeter signature |
|---|---|---|
| 4 | bipolar | two pairs of low R; infinite between pairs |
| 5 | unipolar, common center tap | tap-to-end R, end-to-end 2R |
| 6 | unipolar, separate taps | two 3-wire groups: R (tap-end), 2R (end-end) |
| 8 | universal | four independent windings |
| free-spinning shaft | variable reluctance | - |
| cogging shaft | permanent magnet | - |

**Unipolar sequences (Fig. 15.8, 1a 1b 2a 2b):** single stepping 1000, 0010, 0100, 0001; power stepping 1001, 1010, 0110, 0101; half stepping 1000, 1010, 0010, 0110, 0100, 0101, 0001, 1001.

**FPGA numbers (Ch. 14):** 200,000 to several million logic blocks; 6-input LUT = 64 x 1 ROM; configuration load < ~200 ms; I/O a few tens of mA; Xilinx + Altera ~90 % of market; Elbert V2: XC3S50A (TQG144), 16-MB SPI flash, 12-MHz clock (P129), 39 user I/O (p.899-902, 926).

### S2-16/17 Audio and modules (Ch. 16-17)

**Table S2-16.1 Audio reference numbers**

| Quantity | Value | Source |
|---|---|---|
| Hearing range / peak sensitivity | 20-20,000 Hz / 1-2 kHz | p.947 |
| Intensity range | 1e-12 to 1 W/m^2 (0-120 dB), I0 = 1e-12 W/m^2 | p.947-948 |
| Middle C | 261.6 Hz (harmonics n x f0) | p.948 |
| Speech mic bandwidth | 100-3000 Hz | p.950 |
| Hi-fi mic bandwidth | 20-20,000 Hz | p.950 |
| Mic impedance classes | low < 600 ohm; medium 600-10,000 ohm; high > 10,000 ohm | p.951 |
| Bridging rule | Z_load >= 10 x Z_source; equal Z -> ~6 dB loss; <= 6 dB loss acceptable | p.951, 955-956 |
| Electret bias | +1.5 to +10 V via 1-10 kohm | p.950 |
| Woofer / midrange / tweeter | < 200 Hz / 500-3000 Hz / above midrange | p.957 |
| Full-range driver | 100-15,000 Hz | p.957 |
| Single-supply bias resistors | 10-100 kohm (equal, V/2) | p.952 |
| LM386 | gain 20-200; +4-12 V (fig) / +4-15 V (text); 8 ohm | p.647, 959 |
| LM383 | 4 ohm (or 2 x 8 ohm); +5-20 V; 8 W (16 W bridged); heat sink required | p.647, 959 |

**Table S2-17.1 RF module characteristics (p.966-967)**

| Module | Data rate | Range | Notes |
|---|---|---|---|
| 433/315-MHz TX/RX | <= 8 kb/s (2 kb/s common) | ~100 yards (less indoors) | one-way; low power |
| Bluetooth | serial | - | 3.3-V modules; level shifting for 5 V |
| XBee / XRF | transparent serial | medium (XBee Pro long) | standard socket |
| GSM/GPRS | SMS/GPRS | cellular | serial AT-style commands |

**Audio formulas (Ch. 16)**
- dB = 10 log10(I/I0); intensity ~ 1/r^2.
- Bridging loss = 20 log10(Rload/(Rload + Rsource)).
- Speaker current I = V/Z; n equal speakers in parallel Z/n.
- Crossover: C1 = 1/(2*pi*f2*Rt); L1 = Rm/(2*pi*f2); C2 = 1/(2*pi*f1*Rm); L2 = Rw/(2*pi*f1).
- Output coupling C = 1/(2*pi*fc*RL).

### S2-A/B/C Appendices

**Table S2-A.1 Single-phase mains by country (Fig. A.6, p.978)** - transcribed in OCR order; verify against a current authoritative source before use (e.g. Egypt printed as 60 Hz).

| Country | Voltage (V) | Frequency (Hz) | Plug types |
|---|---|---|---|
| Australia | 240 | 50 | I |
| Belgium | 230 | 50 | C, E |
| Brazil | 110/220 | 60 | A, B, C, D, G |
| Canada | 120 | 60 | A, B |
| Chile | 220 | 50 | C, L |
| China | 220 | 50 | I |
| Congo | 230 | 50 | C, E |
| Costa Rica | 120 | 60 | A, B |
| Egypt | 220 | 60 (as printed) | C |
| France | 230 | 50 | C, E, F |
| Germany | 230 | 50 | F |
| Hong Kong | 230 | 50 | D, G |
| India | 230 | 50 | C, D |
| Iraq | 220 | 50 | C, D, G |
| Italy | 127/220 | 50 | F, L |
| Japan | 100 | 50/60 | A, B |
| Korea | 110/220 | 60 | A, B, D, G, I, K |
| Mexico | 127 | 60 | A |
| Netherlands | 230 | 50 | C, E |
| Norway | 230 | 50 | C, F |
| Philippines | 110/220 | 60 | A, B, C, E, F, I |
| Russia & former Soviet Republics | 220 | 50 | C, F |
| Spain | 127/220 | 50 | C, E |
| Switzerland | 220 | 50 | C, E, J |
| Taiwan | 110 | 60 | A, B, I |
| US | 120 | 60 | A, B |
| United Kingdom | 230 | 50 | G |

**Table S2-A.2 US power distribution (Fig. A.1, p.974)**

| Service | Configuration | Voltages |
|---|---|---|
| Homes | 1-phase, 3-wire, center tap grounded | 120 V (hot-neutral), 240 V (hot-hot) |
| Industry | 3-phase Y, 4-wire | 480 V line / 277 V phase |
| Industry | 3-phase Y, 4-wire | 208 V line / 120 V phase |
| Industry | 3-phase delta, 4-wire, center-tapped | 240 V line; 120 V to neutral on two legs; stinger leg 187 V (not used) |
| Industry | 3-phase delta, 3-wire | 240 V |
| Generation / transmission / regional / local | - | 10 kV / 220 kV / 66 or 33 kV / 16 or 4 kV |

**Uncertainty formulas (Appendix B, p.980-982)**
- A + B, A - B: +/- sqrt(a^2 + b^2); A + B + C: +/- sqrt(a^2 + b^2 + c^2).
- A x B, A/B: +/- (result) x sqrt((a/A)^2 + (b/B)^2); A x B x C: add (c/C)^2 term.
- A^B (printed item 7): +/- A^B x B x (b/B) (as printed; OCR ambiguous).
- Worst case: add absolute (sum) or relative (product) errors linearly.

**Unit prefixes (Appendix C.2, p.983):** T 1e12, G 1e9, M 1e6, k 1e3, c 1e-2, m 1e-3, u 1e-6, n 1e-9, p 1e-12. 1 rad = 57.296 deg; 1 deg = 0.017453 rad (text reads "0.17453"); f = 1/T = omega/(2*pi) (p.984-985).

## 3. Mechanizable checks

Each check lists: inputs (columns, units) → formula → pass criterion → margin definition → source rows. Where a tolerance is not given by the book it is marked as Anvil's choice.

- `CHECK-scope-bandwidth`: inputs (f0_Hz, scope_BW_Hz, measurement ∈ {freq, amplitude}, harmonic_n) → required = 3*f0 (freq; 5*f0 preferred), 10*f0 (amplitude), n*f0 (harmonic) → pass if scope_BW >= required → margin = scope_BW/required - 1 → SCHERZ-2009.
- `CHECK-scope-sample-rate`: inputs (fs_Sps, BW_Hz, reconstruction bool) → ratio = fs/BW → pass if ratio >= 4 (reconstruction) else >= 10 → margin = ratio/limit - 1 → SCHERZ-2010.
- `CHECK-shunt-rating`: inputs (R_shunt_ohm, I_max_A, P_rating_W) → need = 2*R*I_max^2 (book: 2 ohm x I^2 for a 1-ohm shunt) → pass if P_rating >= need → margin = P_rating/need - 1 → SCHERZ-2001.
- `CHECK-probe-voltage`: inputs (V_peak_V, probe_type) → limit = 400 V (1X/10X conservative), 1.4 kV (100X), 20 kV (1000X), 50 V (Z0), 40 V (active) → pass if V_peak <= limit → SCHERZ-2016..2019.
- `CHECK-opamp-bias-comp`: inputs (R1_ohm, R2_ohm, R_plus_ohm, op_amp_input_type) → target = R1*R2/(R1+R2) (inverting) → pass if input_type ∈ {JFET, MOSFET} or |R_plus - target|/target <= 0.1 (tolerance is Anvil's choice, not the book's) → margin = 0.1 - |err| → SCHERZ-2047.
- `CHECK-opamp-input-rails`: inputs (Vin_min, Vin_max, Vneg, Vpos, powered_before_signal bool) → pass if Vin_min >= Vneg - 0.7 and Vin_max <= Vpos + 0.7 and powered_before_signal (or Schottky clamps present) → margin = min(Vin_min - (Vneg - 0.7), (Vpos + 0.7) - Vin_max) → SCHERZ-2063.
- `CHECK-opamp-gbw`: inputs (G_closed, f_signal_max, fT) → f_CL = fT/|G| (non-inverting noise gain) → pass if f_CL >= f_signal_max (Anvil may require 10x) → margin = f_CL/f_signal_max - 1 → SCHERZ-2058 (graph-derived).
- `CHECK-opamp-slew`: inputs (f_max_Hz, Vpeak_V, SR_V_per_us) → need = 2*pi*f*Vpeak/1e6 → pass if SR >= need → margin = SR/need - 1 → SCHERZ-2057.
- `CHECK-opamp-decoupling`: inputs (per op-amp supply pin list of attached caps) → pass if each rail pin has >= 0.1 uF ceramic or >= 1 uF tantalum to ground → SCHERZ-2062.
- `CHECK-comparator-hysteresis-inv`: inputs (Vs, R1, R2, R3, Vref1_target, Vref2_target) → compute Vref1, Vref2 via SCHERZ-2068 formulas → pass if |computed - target| <= resistor-tolerance-induced error → margin in V → SCHERZ-2068.
- `CHECK-comparator-hysteresis-noninv`: inputs (Vcc, Vref, R1, R2, Vin1_target, Vin2_target) → Vin1 = Vref(R1+R2)/R2; Vin2 = (Vref(R1+R2) - Vcc*R1)/R2 → pass within tolerance → SCHERZ-2070.
- `CHECK-comparator-loading`: inputs (R_pullup, R_load, R_feedback) → pass if R_pullup < R_load and R_feedback > R_pullup → SCHERZ-2069.
- `CHECK-single-supply-bias`: inputs (Vs, R_top, R_bot, C_in, R_in, C_out, R_load, f3dB) → pass if |R_bot/(R_top+R_bot) - 0.5| small and C_in >= 1/(2*pi*f3dB*R_in) and C_out >= 1/(2*pi*f3dB*R_load) → margin = C/C_min - 1 → SCHERZ-2060.
- `CHECK-inamp-gain`: inputs (R1, Rg, R2, R3, G_target) → G = (1 + 2R1/Rg)(R3/R2) → pass if |G - G_target|/G_target <= tol → SCHERZ-2072.

- `CHECK-filter-technology`: inputs (f_corner_Hz, f_stop_Hz, topology ∈ {passive, active}) → pass if active and f_corner <= 100e3 (and f_stop <= 100e3) or passive and 100 <= f_corner <= 300e6 → SCHERZ-2085.
- `CHECK-butterworth-order`: inputs (type ∈ {LP, HP}, f3dB, fs, A_stop_dB, n) → As = fs/f3dB (LP) or f3dB/fs (HP); A(n) = 10*log10(1 + As^(2n)) (standard Butterworth magnitude, not printed in the book - cross-check against Fig. 9.6 examples in Table S2-9.3) → pass if A(n) >= A_stop_dB → margin = A(n) - A_stop_dB (dB) → SCHERZ-2088.
- `CHECK-lc-ladder-scaling`: inputs (n, topology, RL, f3dB, L_list, C_list) → expected L = RL*L_table/(2*pi*f3dB), C = C_table/(2*pi*f3dB*RL) from Table S2-9.1 → pass if each part within its tolerance of expected → SCHERZ-2091.
- `CHECK-active-filter-scaling`: inputs (n, Z, f3dB, C_list, R_list) → expected C = C_table/(Z*2*pi*f3dB) (Table S2-9.2), R = Z → pass within tolerance → SCHERZ-2096.
- `CHECK-bandpass-class`: inputs (f1, f2) → ratio = f2/f1 → wide if > 1.5 else narrow; flag if design method mismatches → SCHERZ-2093.
- `CHECK-mfb-bandpass`: inputs (f0, BW, C, R1, R2, R3) → Q = f0/BW; R1e = Q/(2*pi*f0*C); R2e = R1e/(2Q^2 - 1); R3e = 2R1e → pass if parts within tolerance (R2 trimmable) → SCHERZ-2099.
- `CHECK-active-notch`: inputs (f0, BW, C, R1, K) → R1e = 1/(2*pi*f0*C); Ke = (4Q-1)/(4Q) → pass within tolerance → SCHERZ-2100.
- `CHECK-sc-filter-clock`: inputs (fclk, f_signal_max, post_RC_fc) → pass if post-filter RC present with fc between f_signal_max and fclk (clock feedthrough 10-25 mV) → SCHERZ-2104.

- `CHECK-555-astable`: inputs (R1_ohm, R2_ohm, C1_F, diode_across_R2 bool, f_target, duty_target) → t_high = 0.693*(R1 + (0 if diode else R2))*C1; t_low = 0.693*R2*C1; f = 1/(t_high + t_low); duty = t_high/(t_high+t_low) → pass if |f - f_target|/f_target <= tol and |duty - duty_target| <= tol and (diode or duty_target > 0.5) → SCHERZ-2112, 2114.
- `CHECK-555-component-window`: inputs (R list, C list) → pass if all 10e3 <= R <= 14e6 and 100e-12 <= C <= 1000e-6 → margin = min ratio to nearest bound → SCHERZ-2113.
- `CHECK-555-monostable`: inputs (R1, C1, t_target) → t = 1.10*R1*C1 → pass within tol → SCHERZ-2115.
- `CHECK-555-output-load`: inputs (part, I_load_source_mA, I_load_sink_mA) → limits from Table S2-10.1 (bipolar 200 mA; ICL7555 4/25 mA; TLC555 10/100 mA) → pass if loads <= limits → margin = limit/load - 1 → SCHERZ-2111, 2117.
- `CHECK-555-decoupling`: inputs (pin5_cap_F, pin8_pin1_cap_F) → pass if pin5_cap ~ 0.01 uF present and pin8-1 cap >= 0.1 uF → SCHERZ-2116.
- `CHECK-566-range`: inputs (VCC, VC, R1) → pass if 0.75*VCC <= VC <= VCC and 2e3 < R1 < 20e3 → SCHERZ-2119.
- `CHECK-wien-gain`: inputs (R3, R4, amplitude_control bool) → pass if |R3/R4 - 2| <= tol and amplitude_control → SCHERZ-2120.
- `CHECK-oscillator-class`: inputs (required_stability_ppm, f_target, topology) → RC ~1000 ppm, LC ~100 ppm, crystal 10-100 ppm; pass if topology stability <= required; flag op-amp oscillators > 100 kHz and LC at audio → SCHERZ-2121, 2125.
- `CHECK-crystal-type`: inputs (f_target, crystal_mode) → pass if fundamental and f <= 30 MHz, or overtone and f is an odd multiple of an available fundamental → SCHERZ-2127.

- `CHECK-linear-headroom`: inputs (V_sec_rms, rectifier ∈ {bridge, CT-fullwave, half}, V_rect_drop (1-2 V), IL, Cf, Vout, headroom_req (2 V general / 3 V 7805 / 0.5 V LDO)) → Vpk = 1.414*V_sec_rms - V_rect_drop; Vpp_ripple = IL*5e-3/Cf (book: ~5 ms discharge per 8.3-ms full-wave 60-Hz period; use 8.33e-3 for a conservative bound); Vmin = Vpk - Vpp_ripple → pass if Vmin >= Vout + headroom_req → margin = Vmin - (Vout + headroom_req) (V) → SCHERZ-2134, 2135, 2141.
- `CHECK-ripple-rms`: inputs (IL_A, Cf_F) → Vr_rms = 0.0024*IL/Cf → compare against rail spec after regulator: Vout_ripple = Vr_rms*10^(-RR/20) → pass if Vout_ripple <= spec (5 % of rail for logic, 1 % for analog) → SCHERZ-2140, 2141, 2142.
- `CHECK-regulator-dissipation`: inputs (Vin_avg, Vout, IL) → P = (Vin_avg - Vout)*IL → feed to thermal check; flag if 78xx IL > 1.5 A or no heat sink when P above package free-air rating (datasheet) → SCHERZ-2132.
- `CHECK-lm317-vout`: inputs (R1, R2, Vout_target) → Vout = 1.25*(1 + R2/R1) → pass within tolerance; Vin <= 37 V → SCHERZ-2133.
- `CHECK-rectifier-rating`: inputs (I_avg, V_rev_peak, I_inrush, diode I_F, PIV, I_FSM) → pass if I_F >= I_avg (with derating), PIV >= V_rev_peak, I_FSM >= I_inrush → SCHERZ-2136.
- `CHECK-bulk-cap-voltage`: inputs (V_sec_rms, cap_rating_V) → pass if cap_rating >= 1.414*V_sec_rms*(1 + line tolerance) (book: 24-0-24 VAC limit with 35-V caps) → SCHERZ-2139.
- `CHECK-supply-protection`: inputs (schematic flags: fuse, reverse diode across regulator, bleeder on HV caps, crowbar/clamp, line filter) → pass if each required element present for the supply class → SCHERZ-2138, 2143-2145.
- `CHECK-efficiency-topology`: inputs (Vin, Vout, Iout, topology) → eta_linear = Vout/Vin (upper bound) → flag linear when eta < 0.5 and dissipation exceeds thermal budget; suggest switcher (> 85 %) → SCHERZ-2146.

- `CHECK-logic-level-compat`: inputs per net (driver VOH_min, VOL_max; receiver VIH_min, VIL_max) → NM_H = VOH_min - VIH_min; NM_L = VIL_max - VOL_max → pass if both >= 0 (Anvil may require >= 0.2 V, the book's supply-noise budget) → margin = min(NM_H, NM_L) → SCHERZ-2158, 2159.
- `CHECK-fanout`: inputs (driver IOL, IOH; list of receiver IIL, IIH) → pass if sum(IIL) <= IOL and sum(IIH) <= IOH → margin = min(IOL/sum IIL, IOH/sum IIH) - 1 → SCHERZ-2161.
- `CHECK-logic-decoupling`: inputs (IC list with gate counts, caps adjacent to each IC VCC pin) → pass if every IC has a 0.01-0.1 uF MLCC at its VCC pin (book minimum: one per 5-10 gates / per 5 counter or register ICs) → SCHERZ-2162.
- `CHECK-unused-inputs`: inputs (netlist pins with function type) → fail on any floating logic input; unused AND/NAND inputs must be high, OR/NOR low, unused CMOS gate inputs grounded, active-low async inputs pulled high → SCHERZ-2163.
- `CHECK-pullup`: inputs (VCC, R, IIH_max, VIH_min, P_budget) → Vin = VCC - IIH*R; PD = VCC^2/R → pass if Vin >= VIH_min and PD <= P_budget → margin = Vin - VIH_min → SCHERZ-2176.
- `CHECK-pulldown`: inputs (VCC, R, IIL_max, VIL_max, P_budget) → Vin = IIL*R; PD = VCC^2/R → pass if Vin <= VIL_max and PD <= P_budget → margin = VIL_max - Vin → SCHERZ-2177.
- `CHECK-setup-hold`: inputs per flip-flop (t_data_arrival relative to clock edge, ts, th) → pass if data stable from edge - ts to edge + th → margin = slack (ns) → SCHERZ-2167.
- `CHECK-ripple-delay`: inputs (n_stages, tpd_ns, clock period, sampling point) → t_total = n*tpd → pass if t_total < time before outputs are sampled (else require synchronous counter) → SCHERZ-2168.
- `CHECK-power-on-reset`: inputs (R, C, VCC, V_release, t_required, n_loads) → t_hold = -R*C*ln(1 - V_release/VCC) → pass if t_hold >= t_required (book: RC ~ t_required) → SCHERZ-2175.
- `CHECK-debounce-window`: inputs (debounce_time_ms or latch present) → pass if SR-latch debounce present or firmware window >= 50 ms (book bounce bound) → SCHERZ-2166.
- `CHECK-adc-resolution`: inputs (FS_V, n_bits, required_resolution_V) → LSB = FS/2^n → pass if LSB <= required → margin = required/LSB - 1 → SCHERZ-2183.
- `CHECK-adc-sample-hold`: inputs (signal max slope dV/dt, t_conv, LSB) → pass if dV/dt * t_conv < LSB or S/H present → SCHERZ-2188.
- `CHECK-analog-switch-range`: inputs (part, V_signal_min, V_signal_max, supplies) → pass if within switch/mux analog range (4066B +/-7.5 V on 15 V; 4051B VEE..VDD) → SCHERZ-2181, 2182.
- `CHECK-logic-load-drive`: inputs (I_load, gate IOL/IOH, load type) → pass if I_load within gate rating or buffered; relay loads require flyback diode → SCHERZ-2180.
- `CHECK-lcd-drive`: inputs (drive waveform dc component, f_drive) → pass if dc average ~0 and 25 Hz <= f_drive <= ~200 Hz → SCHERZ-2192.
- `CHECK-nvm-endurance`: inputs (writes_per_day, life_years, technology) → total = writes_per_day*365*life_years → pass if total <= endurance (EEPROM 1e5, NOVRAM store 1e4, EPROM ~2e2) → margin = endurance/total - 1 → SCHERZ-2194.
- `CHECK-display-mux`: inputs (digits, segments) → lines_mux = segments + digits; lines_direct = segments*digits + digits → report pin savings; with MCU pins available compare → SCHERZ-2191.

- `CHECK-mcu-pin-current`: inputs (per pin I_source/I_sink mA, per group/chip totals, part limits) → pass if each pin <= limit (20 mA generic; ATmega 40 mA x 0.75 = 30 mA production) and chip total <= 200 mA x 0.75 = 150 mA (BSII: 20/25 mA per pin, 40/50 mA per 8-pin group) → margin = limit/actual - 1 → SCHERZ-2209, 2225.
- `CHECK-mcu-supply-window`: inputs (Vcc_min, Vcc_max, fclk, part) → ATtiny85 pass if 2.7 <= Vcc <= 5.5 V and fclk <= 10 MHz → SCHERZ-2206.
- `CHECK-reset-network`: inputs (RESET net) → pass if RESET has pull-up resistor (not direct tie) and ICSP header present on dev boards; brownout/supervisor present → SCHERZ-2207, 2210.
- `CHECK-mosfet-logic-level`: inputs (V_logic, V_GS(th)_max, Rds_on at V_logic, gate resistor) → pass if V_GS(th)_max well below V_logic (datasheet Rds_on specified at V_logic) and R_gate ~1k present → SCHERZ-2226.
- `CHECK-inductive-flyback`: inputs (load type, driver) → fail if relay/motor/solenoid driven without flyback diode or with I_coil > pin limit and no transistor → SCHERZ-2227.
- `CHECK-adc-divider-clamp`: inputs (V_in_max, R1, R2, V_ref, clamp_zener_V) → V_pin_max = V_in_max*R2/(R1+R2) → pass if V_pin_max <= V_ref and clamp present with V_z >= V_ref (book: allow margin below zener knee) → margin = V_ref - V_pin_max → SCHERZ-2223.
- `CHECK-button-ladder`: inputs (R_pullup, ladder resistors, tolerance %, Vcc, ADC bits) → compute min/max code per button → pass if bands do not overlap → SCHERZ-2220.
- `CHECK-i2c-pullup`: inputs (bus voltage, R_pullup, f_SCL, bus capacitance) → pass if pull-ups present on SDA and SCL, f_SCL <= 400 kHz (book limit), and rise time within spec (datasheet) → SCHERZ-2231.
- `CHECK-level-shift`: inputs per net (driver VOH, receiver VIH, receiver abs max, bidirectional bool) → fail if VOH > receiver abs max without divider/shifter; fail if bidirectional open-drain crossing domains without level-shifter IC → SCHERZ-2234.
- `CHECK-uart-config`: inputs (baud_A, baud_B, framing_A, framing_B, logic levels) → pass if identical and both TTL (or both RS-232 through transceiver) → SCHERZ-2233.
- `CHECK-spi-select`: inputs (n_slaves, n_SS_lines, bit order per device) → pass if n_SS_lines >= n_slaves and firmware bit order matches each device → SCHERZ-2232.
- `CHECK-1wire`: inputs (bus voltage vs device voltage, pull-up value, device count) → pass if voltages match, pull-up present (4.7k), count <= 255 → SCHERZ-2230.
- `CHECK-servo-signal`: inputs (pulse_min_us, pulse_max_us, frame_ms) → pass if 1000 <= pulses <= 2000 and frame ~20 ms, with trim for center → SCHERZ-2212.
- `CHECK-led-resistor-per-segment`: inputs (display netlist) → fail if a single resistor is in the common lead of a multi-segment display → SCHERZ-2235.
- `CHECK-charlieplex`: inputs (n_pins, n_LEDs, refresh_Hz, I_peak) → pass if n_LEDs <= n^2 - n; duty = 1/steps; flag if I_peak exceeds LED continuous rating (burn-out risk on firmware hang) → SCHERZ-2236.

- `CHECK-motor-voltage-window`: inputs (V_rated, V_applied_min, V_applied_max) → pass if V_applied_min > 0.5*V_rated and V_applied_max < 1.3*V_rated → margin = min(V_min/0.5V_rated, 1.3V_rated/V_max) - 1 → SCHERZ-2245.
- `CHECK-motor-driver-current`: inputs (I_stall (or 10 x I_no_load if unknown), driver I_max) → pass if driver I_max >= I_stall (L293 1 A, L298 2 A, LMD18200 3 A per winding) → margin = I_max/I_stall - 1 → SCHERZ-2245, 2248.
- `CHECK-hbridge-interlock`: inputs (H-bridge input logic) → fail if forward and reverse inputs can be high simultaneously (no XOR/logic interlock, no driver-IC protection) → SCHERZ-2247.
- `CHECK-motor-flyback`: inputs (each motor/stepper/relay winding, diode list) → fail if any inductive winding lacks a clamp/flyback path (unipolar: both halves) → SCHERZ-2247, 2256.
- `CHECK-servo-pulse`: inputs (t_min_ms, t_max_ms, frame_ms, V_supply) → pass if 1.0 <= t <= 2.0 ms (or servo datasheet), 20 <= frame <= 30 ms, 4.8 <= V <= 6.0 V → SCHERZ-2249.
- `CHECK-stepper-driver-count`: inputs (stepper type, coil pairs, H-bridges) → bipolar requires one H-bridge per coil pair → SCHERZ-2255.
- `CHECK-saa1027-levels`: inputs (logic VOH, VOL, supply) → pass if VOH >= 7.5 V, VOL <= 4.5 V, 9.5 <= supply <= 18 V → SCHERZ-2257.
- `CHECK-fpga-startup`: inputs (t_config_ms, downstream devices requiring defined levels at power-up) → flag outputs needing pull-ups/pull-downs during the < ~200 ms configuration window → SCHERZ-2240.

- `CHECK-audio-bridging`: inputs (Z_source, Z_load per interconnect) → loss_dB = 20*log10(Z_load/(Z_load + Z_source)) → pass if Z_load >= 10*Z_source (strict) or loss >= -6 dB (acceptable) → margin = Z_load/(10*Z_source) - 1 → SCHERZ-2262, 2263.
- `CHECK-mic-bandwidth`: inputs (application ∈ {speech, hifi}, mic f_low, f_high) → pass if mic covers 100-3000 Hz (speech) or 20-20,000 Hz (hi-fi) → SCHERZ-2261.
- `CHECK-electret-bias`: inputs (V_bias, R_bias) → pass if 1.5 <= V_bias <= 10 V and 1k <= R_bias <= 10k → SCHERZ-2260.
- `CHECK-speaker-load`: inputs (amp minimum load Z, speaker Z list, wiring series/parallel) → Z_eff computed → pass if Z_eff >= amp minimum (LM383 4 ohm, LM386 8 ohm) → margin = Z_eff/Z_min - 1 → SCHERZ-2268, 2271, 2272.
- `CHECK-crossover`: inputs (f1, f2, Rt, Rm, Rw, C1, L1, C2, L2) → expected per SCHERZ-2270 formulas → pass within tolerance → SCHERZ-2270.
- `CHECK-single-supply-audio-bias`: inputs (R3, R4, V+, C_out, RL, fc) → pass if R3 = R4 in 10k-100k and C_out >= 1/(2*pi*fc*RL) → SCHERZ-2265.
- `CHECK-rf-link-budget-lite`: inputs (module type, required data rate, required range, indoor bool) → pass if 433/315-MHz data rate <= 8 kb/s and range <= ~100 yd (derate indoors) → SCHERZ-2276.

- `CHECK-mains-input-range`: inputs (target markets list, supply input range V_min..V_max, f range) → required = union of market voltages/frequencies (Table S2-A.1: 100-240 V, 50/60 Hz) → pass if product input range covers all targets → SCHERZ-2284.
- `CHECK-three-phase`: inputs (config ∈ {Y, delta}, V_phase or V_line, I) → V_L = sqrt(3)*V_P (Y); I_L = sqrt(3)*I_P (delta) → used for load/breaker sizing → SCHERZ-2281.
- `CHECK-measurement-uncertainty`: inputs (measured values, uncertainties, formula) → propagate per Appendix B (quadrature for independent errors, linear for worst case) → pass if result uncertainty <= required accuracy; flag differences of nearly equal quantities → SCHERZ-2286.
- `CHECK-tolerance-range`: inputs (nominal, tolerance %) → range = nominal*(1 +/- tol) → used in worst-case corner generation → SCHERZ-2285.

## 4. Verification procedures & plots

### Ch. 7 bench measurement procedures

- **VP-SCOPE-SETUP (p.586-588):** start with power off, focus/gain/intensity lowest, sweep EXT, positions mid; power on, center beam, recurrent sweep > 100 Hz. Before measuring set input to GND and fix the 0-V reference line; do not touch vertical position afterwards (offset error). Readout: divisions x VOLT/DIV, divisions x SEC/DIV.
- **VP-SCOPE-TRIGGER (p.585-586):** AC trigger coupling works ~10 Hz to > 35 MHz; LF REJ attenuates < 10 kHz (use when trigger has 60-Hz hum); HF REJ attenuates > 100 kHz (noise, or trigger on modulation envelope); DC coupling for very low-frequency signals.
- **VP-CURRENT-SHUNT (p.588-589, Fig. 7.40-7.41):** series 1-ohm precision shunt rated >= 2 ohm x Imax^2; volts across shunt = amps; read dc, ac RMS and dc+ac effective current from the trace.
- **VP-PHASE (p.589-590, Fig. 7.42-7.43):** DUAL mode, equalize amplitudes, measure period T_R in divisions, phase factor 360/T_R, multiply by peak-to-peak horizontal offset. Pass: repeatable within 1 minor division; cables equal length.
- **VP-PULSE (p.591, Fig. 7.45):** apply square pulse; measure tr (10-90 %), tf (90-10 %), tw (50-50 %), td (t0 to 10 %), tilt % and overshoot %; x-axis time, y-axis volts; good = values inside spec.
- **VP-REFLECTION (p.592, Fig. 7.46):** pulse generator (50 ohm) -> 50-ohm reference coax -> DUT; observe incident and reflected pulse; inverted reflection = DUT impedance below 50 ohm.
- **VP-DIGITAL-TIMING (p.593, Fig. 7.47-7.51):** CH1 = clock/reference, CH2 = output; use INV + ADD to compare amplitudes, measure propagation delay td between edges, verify divide-by-2/4 relationships and logic states of gate inputs/outputs.
- **VP-PROBE-COMP (p.607):** probe on scope 1-10 kHz calibrator; trim to flat top (no overshoot, no rounding); repeat per channel and per tip adapter; run scope self-cal if available.
- **VP-POT-NOISE (p.591, Fig. 7.44):** drive pot ends with dc, watch wiper on scope while rotating; clean line = good; noise bursts = bad contact (rule out cable noise first).

### Ch. 8 op-amp / comparator verification

- **VP-OPAMP-BODE (p.652, Fig. 8.27):** AC sweep 1 Hz-10 MHz, log x = frequency, y = gain (dB) and phase (deg), open-loop and closed-loop (G = 10, 100). Good: open-loop 80-120 dB flat to fB then -20 dB/dec to fT (~1 MHz); closed-loop flat to ~fT/G; phase margin exists (phase shift < 180 deg where loop gain = 1). Fail: slope 40-60 dB/dec near crossover (unstable region).
- **VP-OPAMP-OFFSET (p.651):** short inputs (or ground input), measure Vout dc; trim null pot to ~0 V; with bipolar op amps compare Vout with and without Rcom = R1\|\|R2.
- **VP-COMPARATOR-HYST (p.654-656, Fig. 8.30-8.33):** slow triangle sweep across both thresholds; x = Vin, y = Vout (XY mode) shows hysteresis loop; pass: upper/lower trip points = design (e.g. 6.0/5.0 V; 8.0/6.0 V) and no chatter with noise added at threshold.
- **VP-WINDOW (p.656):** sweep Vin 0 -> above window; output high only between Vref,low and Vref,high (3.5-6.5 V example).
- **VP-LATCHUP (p.650-651):** power-sequencing test: apply input signal before and after rails; verify clamp current limited and inputs never beyond rails +/-0.7 V.
- **VP-INTEGRATOR-DRIFT (p.643):** ground input, log Vout vs time; pass: bounded (dc feedback resistor present), no rail-to-rail drift.
- **VP-SH-DROOP (p.661):** sample known dc, open switch, measure droop rate dV/dt over hold interval; compare with I_leak/C.

### Ch. 9 filter verification

- **VP-FILTER-BODE (p.664-668, Fig. 9.2, 9.4, 9.6):** ngspice AC sweep with the real source/load resistances (Rs = RL = 50 or 600 ohm in the examples); x = frequency (log, from 0.1*f3dB to 10*fs), y = Vout/Vin in dB (normalize passband to 0 dB). Pass: -3 dB (+/- tolerance) at f3dB (f1, f2 for BP/notch), attenuation >= spec at fs; Butterworth passband monotonic; Chebyshev ripple <= specified (0.1/0.5 dB). Corners: component tolerance Monte Carlo (Chebyshev more sensitive).
- **VP-FILTER-GROUP-DELAY (p.670):** plot group delay vs frequency; Bessel should be flat across passband; flag Butterworth/Chebyshev delay variation for pulse/modulated signals.
- **VP-FILTER-STEP (p.670):** transient step response (overshoot/ringing) for pulse-fidelity applications; Bessel minimal overshoot.
- **VP-NOTCH-DEPTH (p.680-681):** sweep through f0 with fine resolution; measure null depth and -3 dB points; trim pot (K) / R2 for centering.
- **VP-SC-FILTER-NOISE (p.682):** FFT of output; clock component 10-25 mV at fclk before RC post-filter; verify post-filter suppression.

### Ch. 10 oscillator / timer verification

- **VP-555-ASTABLE (p.688, Fig. 10.7):** transient sim/scope of V(C1) and Vout; x = time, y = volts; good: V(C1) ramps between 1/3 VCC and 2/3 VCC (2 V and 4 V at 6 V), Vout ~ VCC - 1.5 V high / 0.1 V low, t_high/t_low per formula. Corners: VCC min/max, C1 tolerance, R tolerance.
- **VP-555-MONO (p.690, Fig. 10.10):** apply negative trigger < 1/3 VCC; measure output pulse width = 1.10 R1C1 (16.5 ms example); check no retrigger/false trigger with pin-5 cap present.
- **VP-OSC-STARTUP (p.694):** transient from power-on (no initial condition) - oscillator must self-start from noise within a few cycles and settle to stable amplitude (Wien/LC with amplitude limit); x = time, y = Vout envelope.
- **VP-OSC-FREQ (p.608, 696):** measure frequency with a counter (scope error ~5 %); for crystal oscillators log frequency vs temperature/supply; pass: within crystal stability class (0.01-0.001 %).
- **VP-WIEN-DISTORTION (p.693):** FFT of output; low distortion requires gain held at 3 by amplitude control; flag clipping (gain > 3) or decay (gain < 3).

### Ch. 11 power-supply verification

- **VP-RIPPLE (p.707-709, Fig. 11.12):** transient sim of transformer + rectifier + Cf + regulator at max load and low line; plot V(Cf) and Vout vs time over >= 10 line cycles; measure Vpp ripple on Cf (expect ~ IL*t_discharge/C) and at the regulator output (expect reduction by ripple-rejection dB). Pass: V(Cf) trough >= Vout + headroom; output ripple within rail spec.
- **VP-LOAD-REG (p.700):** sweep load 0 -> Imax; plot Vout vs I; unregulated supplies droop, regulated stays within tolerance.
- **VP-LINE-TRANSIENT (p.700, 709):** inject line spike; verify regulator/line filter/TVS keep output within spec.
- **VP-POWER-OFF (p.704-706, 710):** power-off transient with output capacitance larger than input capacitance; verify regulator never reverse-biased (protection diode) and bulk cap discharges through bleeder within safe time.
- **VP-CROWBAR (p.710):** raise rail slowly; crowbar must fire at Vz + 0.6 V and hold until power cycled; clamp must limit without latching.
- **VP-SWITCHER-RIPPLE (p.714):** scope output with short ground spring; switching ripple tens of mV; verify below 200-mV logic noise margin or add LC post-filter.
- **VP-POLARITY (p.715):** verify barrel-jack center polarity against product label; apply reversed adapter and confirm protection.

### Ch. 12 digital verification

- **VP-LOGIC-TIMING (p.773-774, Fig. 12.78):** digital timing diagram / mixed-signal sim: x = time (ns), traces CLK, D/J/K, Q; annotate ts, th, tPLH, tPHL; pass: all data transitions outside [edge - ts, edge + th]; clock pulse widths >= tW(min); fclk <= fmax.
- **VP-RIPPLE-SKEW (p.772):** scope/sim counter outputs Q0-Q3 on one clock edge; measure staggered transitions (n x tpd); pass if decode logic samples after settling or counter is synchronous.
- **VP-POWER-ON-RESET (p.777-778, Fig. 12.84-12.85):** transient VCC ramp; plot VCC, V(C), CLR; pass: CLR stays below release threshold (2.0 V for 74LS76) for >= required time and releases cleanly (Schmitt version) with no chatter; repeat with fast power cycling (diode discharge).
- **VP-SWITCH-BOUNCE (p.760-761, Fig. 12.57):** scope switch node with single-shot trigger; capture bounce train (typically < 50 ms); verify debounced output has exactly one transition.
- **VP-PULLUP (p.779, Fig. 12.86):** sweep R; plot Vin vs R (switch open) against VIH(min), PD vs R (switch closed); choose R in the window.
- **VP-ADC (p.811-812):** apply slow ramp and static points; plot code vs Vin (staircase), error vs Vin (<= +/-1/2 LSB ideal); SAR example: 3.8652 V input error 29.360 % after first bit, 0.051 % after 8 bits.
- **VP-DAC (p.807-809):** step through all codes; plot Vout vs code; check FS = (2^n - 1)/2^n x Vref, monotonicity, LSB step (e.g. DAC0808 38.9 mV with 5k).
- **VP-LCD-INIT (p.825-828):** logic-analyzer capture of RS, R/W, E, D7-D4: Function Set, Display On, Clear, character writes; data valid before E falling edge; verify 4-bit two-nibble sequence.
- **VP-LOGIC-PROBE (p.757-758):** static high/low checks; MEMORY mode to catch single pulses >= 10 ns; pulser (1 or 500 pps) to stimulate counters.

### Ch. 13 microcontroller verification

- **VP-MCU-CURRENT (p.846):** measure supply current at the chosen clock (ATtiny85 ~300 uA @ 1 MHz) and in power-down (0.1 uA) with a series shunt/DMM; x = clock/mode, y = current; pass vs battery-life budget.
- **VP-SERVO-PWM (p.859-860):** scope servo control pin: pulse width 1.0-2.0 ms (1.5 ms center) every ~20 ms; verify continuous refresh and trim so a continuous-rotation servo stops at "center".
- **VP-DEBOUNCE (p.877, Fig. 13.18):** scope raw switch pin (single-shot trigger) to measure bounce; log firmware button events while pressing repeatedly; pass: exactly one event per press.
- **VP-BUTTON-LADDER (p.875-876):** read ADC code for each button at Vcc min/max with tolerance-corner resistors; pass: codes stay inside decode bands, bands disjoint.
- **VP-ADC-SCALING (p.878-879):** sweep 0-50 V into the 1:11 divider; plot code vs Vin; confirm linearity up to 50 V and clamp action above (zener knee).
- **VP-BUS-DECODE (p.885-892):** logic-analyzer/protocol decode of 1-Wire (reset >= 480 us, 60/15-us slots), I2C (start/stop, ACK, <= 400 kHz), SPI (SS per slave, CPOL/CPHA/bit order), UART (8N1 at configured baud); pass: decoded bytes match expected.
- **VP-LEVEL-SHIFT (p.892-893):** scope both sides of each shifted line; verify 3.3-V side never exceeds its abs max and logic-high thresholds met on both sides.
- **VP-DISPLAY-MUX (p.893-895):** scope digit-common and segment lines; verify refresh rate is flicker-free and per-LED peak current within rating; for Charlieplexing verify tri-state pattern (Table 13.9).

### Ch. 14-15 verification

- **VP-FPGA-SIM (p.928-931):** behavioral simulation with a test fixture: CLK toggled every 10 ns, reset pulse, 100-ns settle; waveform view of bus Q[3:0]; pass: counts/sequences as specified before programming hardware.
- **VP-MOTOR-STALL (p.934):** ammeter in series; slowly load shaft until stall; record stall current (can exceed 10x no-load); x = load torque, y = current/speed.
- **VP-MOTOR-PWM (p.934-935):** scope gate drive and motor current (current probe) at several duty cycles; plot speed vs duty; check MOSFET temperature and flyback clamping at turn-off.
- **VP-HBRIDGE (p.936, 943):** drive forward/reverse/both-inputs; pass: interlock prevents both-on; no supply current spike at direction change.
- **VP-SERVO (p.937-938):** scope 555/MCU output: pulse 1.0-2.0 ms at 20-30 ms frame; measure shaft angle vs pulse width for the specific brand.
- **VP-STEPPER (p.939-945):** logic-analyzer capture of phase outputs for single/power/half stepping; check step count vs rotation angle; measure coil current and clamp voltage at turn-off; pass: no missed steps at target step rate.
- **VP-STEPPER-ID (p.945-946):** ohmmeter matrix across leads; classify per Table S2-15.2; confirm by stepping.

### Ch. 16-17 audio / module verification

- **VP-AUDIO-FREQ (p.950-952):** AC sweep 10 Hz-100 kHz of preamp/amp chain with actual source and load impedances; plot gain (dB) vs log f; pass: flat (within spec) over 100-3000 Hz (speech) or 20-20,000 Hz (hi-fi), -3 dB corners from coupling caps where designed.
- **VP-CLASS-D (p.953, Fig. 16.9):** transient sim of comparator PWM (triangle carrier vs sine) and output LC filter; plot V(sig), V(tri), V(PWM), filtered output; FFT output: carrier suppressed, THD within spec.
- **VP-HUM (p.954):** short input, FFT the output; check 60-Hz (50-Hz) and harmonics level; compare with supply smoothing capacitance increased and screened wiring.
- **VP-CROSSOVER (p.957-958):** sweep the network into resistive driver models (Rt, Rm, Rw); plot each driver's response; pass: -3 dB crossings at f1/f2 and flat summed response.
- **VP-SPEAKER-LOAD (p.956):** measure amplifier output current at full power into the intended speaker combination; confirm load >= amplifier minimum; check LM383 heat-sink temperature below thermal shutdown.
- **VP-RF-RANGE (p.966-967):** field test 433/315-MHz link: packet error rate vs distance outdoors and indoors at the chosen bit rate (<= 8 kb/s).

## 5. Pitfalls, failure modes, review checklist

### Ch. 7 bench / assembly pitfalls

- [ ] Fig. 7.39 prints Vrms = Vpp/sqrt(2) = 8.5 V for a 12-Vpp sine; the correct sine relation is Vrms = Vpp/(2*sqrt(2)) = 4.24 V - do not copy the figure's formula (p.588; conf medium, arithmetic check).
- [ ] Scope ground clipped to the primary side (bulk-cap negative) of an off-line SMPS without an isolation transformer blows a bridge diode and vaporizes the probe tip (p.612-613).
- [ ] A Variac is an autotransformer and gives no isolation; isolation transformer must precede it (p.613).
- [ ] Some TV chassis float 80-90 V above earth; connecting scope ground creates a ground loop/short (p.612).
- [ ] 10-Mohm DMM input loads high-impedance nodes; use > 10 Gohm input or account for divider error (p.596).
- [ ] Long probe ground lead -> ringing (decaying sinusoid on pulse edges) that is not in the circuit (p.601).
- [ ] Probe switched 1X<->10X changes bandwidth as well as scale (p.604).
- [ ] Extending a probe with ordinary coax (100 pF/m) causes capacitive loading and reflections (p.601).
- [ ] Two-probe A-B "differential" measurement is invalid at high frequency or near noise level (skew, low CMRR) (p.606).
- [ ] Breadboard used for RF or > 100 mA circuits (p.621).
- [ ] Acid-core or conductive flux on electronics; flux residue left on board (low-resistance leakage paths) (p.619).
- [ ] Solder gun / large iron on a PCB -> pad/trace delamination (p.618).
- [ ] Wrist strap without 1-Mohm series resistor (shock hazard) (p.595).
- [ ] Wirewound resistors (including < 1-ohm decade values) used in HF circuits - inductive (p.615-616).

### Ch. 8 op-amp / comparator pitfalls

- [ ] Op-amp supply leads reversed (no series protection diode) (p.650).
- [ ] Op-amp input can exceed a rail by > 0.7 V, or signal can arrive before the op amp is powered -> destructive latch-up (p.650-651).
- [ ] No 0.1-uF / 1-uF bypass at op-amp supply pins, long supply wires -> oscillation/noise (p.650).
- [ ] Bipolar op amp with large feedback resistors and no bias-compensation resistor -> output offset = Ibias*(R1\|\|R2)*(R2/R1) (p.651).
- [ ] JFET op amp with input common-mode near the negative rail -> phase inversion/latch-up (p.646).
- [ ] Integrator without a dc feedback resistor across C -> drifts to a rail (p.643).
- [ ] Bare RC differentiator (no input R / feedback C) -> noise and instability (p.643-644).
- [ ] Single-supply op amp used for ac-coupled signal without mid-supply bias -> negative half clipped (p.647, 649).
- [ ] Comparator IC wrapped with negative feedback / used as linear amp -> unstable (p.653).
- [ ] Open-collector comparator output with no pull-up resistor (p.653).
- [ ] Comparator without hysteresis on slow/noisy input -> output chatter (p.654).
- [ ] Hysteresis comparator pull-up heavier than load or feedback resistor smaller than pull-up -> reduced hysteresis (p.655).
- [ ] General op amp used as comparator with grounded negative supply where the part does not support it (p.653).
- [ ] Uncompensated op amp used at low closed-loop gain without datasheet compensation network (p.652).
- [ ] Passive diode rectifier/peak detector used for signals near or below 0.6 V (p.661-662).
- [ ] Sample-and-hold with bipolar-input buffer or leaky (e.g. ceramic/electrolytic) hold capacitor -> droop (p.661).

### Ch. 9 filter pitfalls and printed errata

- [ ] Active op-amp filter specified with corner/stop frequencies above ~100 kHz (op-amp GBW/slew limits) - use passive LC (p.664).
- [ ] Passive LC filter designed without accounting for real source and load impedances (p.664, 669).
- [ ] Narrow-band bandpass (f2/f1 < 1.5) attempted by cascading LP and HP sections (p.672).
- [ ] Butterworth/Chebyshev filter used on pulse/modulated signal where delay distortion matters - use Bessel (p.670).
- [ ] Chebyshev design built with loose-tolerance parts (more sensitive than Butterworth) (p.670).
- [ ] Switched-capacitor filter output used without an RC post-filter for clock feedthrough (10-25 mV) (p.682).
- [ ] ERRATA Fig. 9.17 (p.678): final active high-pass capacitors print as 0.16 uF; the book's own scaling rule C = 1/(Z*2*pi*f3dB) with Z = 10k, f3dB = 1 kHz gives 15.9 nF (matches the 15.9 nF HP caps in Fig. 9.18) - use 0.016 uF (conf medium, recomputed).
- [ ] ERRATA Fig. 9.19 (p.679-680): with Q = 50, C = 0.01 uF, f0 = 2 kHz the printed formulas give R1 = 398 kohm, R2 = 79.6 ohm, R3 = 796 kohm; the printed 79.6k/400/159k correspond to Q = 10 - recompute before use (conf medium).
- [ ] ERRATA p.675: notch-resonating formulas print (2*pi*400 Hz)^2, but the printed results (0.11 uF, 80 mH) require f0 = 980 Hz - use f0 (conf medium, recomputed).
- [ ] ERRATA p.673/675 narrow-band BP and notch examples pick n = 3 for ">= -20 dB" at As = 1.88 / 1.7; exact Butterworth gives only 16.5 / 14.0 dB (the figures annotate -15 dB) - for a true 20-dB spec use n = 4 / n = 5 (conf medium, recomputed).
- [ ] p.665 defines notch Q = (f2 - f1)/f0 while p.680 uses Q = f0/BW; use Q = f0/BW for design formulas (p.680-681).

### Ch. 10 oscillator / timer pitfalls

- [ ] 555 pin 5 left floating (no 0.01-uF cap) -> false triggering (p.691).
- [ ] 555 with long supply leads and no 0.1-uF cap across pins 8-1 (p.691).
- [ ] Basic 555 astable expected to give duty < 50 % without the diode across R2 (p.688).
- [ ] 555 timing R outside 10 kohm-14 Mohm or C outside 100 pF-1000 uF (p.688, 690).
- [ ] CMOS 555 (ICL7555: 4 mA source) asked to drive loads sized for a bipolar 555 (200 mA) (Table 10.1).
- [ ] 555 driving relay coil without surge diodes (p.691).
- [ ] Wien-bridge gain not held at exactly 3 (no amplitude control) -> saturates or stops (p.693).
- [ ] Op-amp-based oscillator above ~100 kHz; LC oscillator at audio frequencies (p.693-694).
- [ ] RC oscillator used where < 0.1 % frequency stability is required - use a crystal (p.696).
- [ ] Fundamental-mode crystal specified above ~30 MHz (use overtone) (p.697).
- [ ] 555 astable example p.688 prints t_low as both 9.6 ms and 9.4 ms; 0.693 x 20k x 680 nF = 9.4 ms (conf medium).

### Ch. 11 power-supply pitfalls

- [ ] Logic powered from an unregulated supply (spikes, load droop) (p.700).
- [ ] 78xx/LM317 expected to deliver 1.5 A without adequate heat sinking; SMD (SOT-89) version assumed to match TO-220 current (p.701).
- [ ] Regulator input trough (after rectifier drop 1-2 V and ripple) below Vout + 2-3 V (p.702-703, 708).
- [ ] Transformer secondary much higher than needed -> regulator overheats (p.703).
- [ ] No reverse diode across regulator when output capacitance can hold charge longer than input (p.704).
- [ ] Bulk electrolytic sized assuming nominal value (tolerance 5-20 % or worse) (p.708).
- [ ] LM317 ADJ pin not bypassed (10 uF) where extra 15 dB ripple rejection is needed (p.709).
- [ ] Transformer secondary > 48 VAC CT with 35-V bulk capacitors / regulator input limit (p.706).
- [ ] No bleeder on high-voltage filter capacitor; no primary snubber (p.710).
- [ ] Crowbar used where supply spikes would false-trip and latch - consider clamp (p.710).
- [ ] Off-line switcher designed without isolation (~160 V dc bus on 120 V line) (p.714).
- [ ] Barrel-jack polarity assumed (consumer center-positive vs musical-gear center-negative) (p.715).
- [ ] Exposed 120-V connections inside enclosure not insulated; enclosure not grounded; line cord without strain relief (p.716).
- [ ] Text p.709 refers to the "LM319" in the ripple example; the part discussed is the LM317 (typo).

### Ch. 12 digital pitfalls and printed errata

- [ ] Floating inputs (unused gate inputs, unused CMOS gates, PRE/CLR left open) (p.757).
- [ ] Logic IC without a local 0.01-0.1 uF MLCC across VCC-GND (p.756).
- [ ] CMOS inputs driven while the CMOS IC is unpowered (p.757).
- [ ] 74HC driven by TTL-level (VOH ~2.4 V) outputs - use 74HCT/ACT (p.755).
- [ ] Mechanical switch into an edge-sensitive input without debounce (bounce up to ~50 ms) (p.761).
- [ ] Data changing within one setup time (~20 ns) of the active clock edge (p.766, 773).
- [ ] Ripple counter outputs decoded before all stages settle (n x ~30 ns) (p.772).
- [ ] Asynchronous enable gating a clock without a synchronizer -> runt pulses (p.767).
- [ ] Master-slave JK with long clock-high intervals -> ones-catching (p.770).
- [ ] Power-up clear RC shared by many ICs without enlarging C (low time shrinks) (p.778).
- [ ] Pull-down sized like a pull-up (TTL IIL ~400 uA needs 100 ohm-1 kohm) (p.780).
- [ ] Op amp on a higher supply driving CMOS logic without series resistor and clamp diodes (p.800).
- [ ] Relay/lamp driven directly from a gate output, or relay without flyback diode (p.800-801).
- [ ] Analog signal outside 4051B VEE..VDD or 4066B +/-7.5 V range (p.802-803).
- [ ] ADC input changing faster than 1 LSB per conversion time without sample-and-hold (p.812).
- [ ] LCD driven with dc (electrochemical degradation); LCD update rate expected faster than 40-100 ms or at low temperature (p.816-817).
- [ ] HD44780 module written before Function Set / Display On after power-up; user CGRAM characters expected to survive power-off (p.825, 828).
- [ ] EEPROM used for high-rate logging beyond ~100,000 writes (p.836).
- [ ] ERRATA p.779: prose computes PD = (5 V)^2/10k = "25 mW"; correct value 2.5 mW (Fig. 12.86 shows 2.5 mW).
- [ ] ERRATA Table 12.2 (p.831): 2^19 = 524,288 printed as "540 K"; correct 512 K.
- [ ] ERRATA p.727 vs Fig. 12.52: 74HC input thresholds printed as 2.5 V/2.1 V in prose but 3.5 V/1.0 V in the figure - use the datasheet.

### Ch. 13 microcontroller pitfalls and printed errata

- [ ] RESET tied directly to VCC (programmer cannot pull it low); no ICSP header on development PCB (p.846, 848).
- [ ] No brownout/supervisor reset - MCU runs erratically on sagging battery (p.853).
- [ ] Internal RC oscillator used where timing accuracy matters (serial baud, clocks) (p.846).
- [ ] ATmega328 taken off-board without a crystal/resonator and regulator (p.872).
- [ ] Pin current above ~20 mA (or ATmega 40 mA/pin, 200 mA/chip absolute limits without 25 % production derating) (p.879-880).
- [ ] Non-logic-level MOSFET (e.g. 6-V threshold) driven from 5-V/3.3-V pin; no gate resistor (p.880-881).
- [ ] Relay or motor on an MCU pin without transistor and flyback diode (p.881).
- [ ] Internal 20-40 kohm pull-ups relied on with long switch leads or in noisy environments (p.875).
- [ ] Normally-closed switch with a low-value pull-up (continuous current) (p.874).
- [ ] Button ladder decoded with exact ADC values instead of bands (p.876).
- [ ] 5-V output driven into a non-5-V-tolerant 3.3-V input without divider; bidirectional I2C/1-Wire crossing voltage domains with only resistors (p.892-893).
- [ ] 1-Wire device voltage (5 V vs 3.3 V) not matched to MCU (p.885).
- [ ] UART ends configured with different baud/framing; RS-232 levels connected directly to MCU pins (p.891).
- [ ] SPI device bit order assumed (not defined by standard) (p.891).
- [ ] Single resistor in the common lead of a 7-segment display (p.893).
- [ ] Charlieplexed/multiplexed LEDs overdriven for brightness with no protection against firmware hang (p.895).
- [ ] 8-ohm speaker driven straight from a pin (p.884).
- [ ] ERRATA p.878 debounce code: condition "lastKeyPressTime > timeNow + debouncePeriod" is never true (lastKeyPressTime starts at 0 and timeNow only grows); intended test is timeNow > lastKeyPressTime + debouncePeriod (conf medium).
- [ ] ERRATA Table 13.6 (p.869): example delayMicroseconds(100000) exceeds the stated ~16-ms maximum for that function.

### Ch. 14-15 pitfalls and printed errata

- [ ] FPGA outputs assumed valid immediately at power-up (configuration load up to ~200 ms) (p.900).
- [ ] FPGA I/O driving loads beyond a few tens of mA (p.900).
- [ ] Mechanical button used as an FPGA clock without debounce (p.914).
- [ ] DC motor speed controlled with a series pot or linear transistor (heat, meltdown) (p.934).
- [ ] Motor driver sized for no-load current instead of stall current (loaded current up to 10x+) (p.934).
- [ ] Motor run below ~50 % (stalls) or above ~130 % (overheats) of rated voltage (p.933-934).
- [ ] H-bridge with both inputs able to go high (shoot-through) (p.936, 943).
- [ ] Stepper/motor windings without flyback diodes; unipolar driver missing diodes on one side of the center tap (p.941-942).
- [ ] Bipolar stepper driven with a unipolar (single-transistor-per-phase) driver (p.941).
- [ ] 5-V logic driving an SAA1027 (needs >= 7.5 V high) (p.945).
- [ ] Servo control pulses not refreshed every 20-30 ms; pulse range assumed identical across servo brands (p.937).
- [ ] ERRATA p.937: servo wire colours printed as "power (usually black), ground (usually red)" - the common convention is red = power, black (or brown) = ground; verify against the servo datasheet (conf medium).
- [ ] ERRATA p.926: prose says the prescaler divides 12 MHz to "a 100-Hz refresh clock", but the code (12,000 count) yields 1 kHz as its comment states.

### Ch. 16-17 audio / module pitfalls

- [ ] High-impedance microphone into a low-impedance input (large voltage loss) (p.951, 955-956).
- [ ] 741-class op amp in a demanding audio path (distortion, noise) (p.951).
- [ ] Single-supply audio stage without V/2 bias or without output coupling capacitor (dc passed to next stage) (p.952).
- [ ] Class-D output without carrier low-pass filter (p.954).
- [ ] Long unscreened audio wiring, ground loops, thin supply smoothing -> 60-Hz hum (p.954, 967).
- [ ] Paralleled speakers dropping load below amplifier minimum (e.g. two 4-ohm on an 8-ohm-rated LM386) (p.956, 959).
- [ ] LM383 without adequate heat sink (thermal shutdown below rated power) (p.959).
- [ ] Discrete RF design where a pre-built module would avoid layout-critical work (p.964-966).
- [ ] 3.3-V Bluetooth module wired directly to 5-V TTL serial (p.967).
- [ ] 433/315-MHz link specified above ~8 kb/s or beyond ~100 yards (less indoors) (p.967).
- [ ] ERRATA p.959 vs Fig. 16.16/p.647: LM386 supply printed as +4 to +15 V and +4 to +12 V - use datasheet limits.

### Appendix pitfalls

- [ ] 120-V load connected across the 187-V stinger leg of a center-tapped delta service (p.974).
- [ ] Neutral and ground bonded in a subpanel (p.976).
- [ ] 120-V-only product shipped to 230-V/50-Hz markets; converter assumed to fix frequency (p.977-978).
- [ ] Measurement reported without uncertainty; test designed around the small difference of two large measured values (p.979-981).
- [ ] ERRATA p.975: Y-connection line voltage printed as "about 3 times" the phase voltage (radical lost in OCR/print) - the relation is sqrt(3).
- [ ] ERRATA p.984: 1 deg reads as 0.17453 rad in the text (print or OCR); correct 0.017453 rad.

## 6. Standards referenced

The book (part 2 range) cites no formal standards documents by number or edition; the following interface/regulatory standards are referenced by name.

| Standard / specification | Edition / clause given | What it governs (as used in the book) | Page |
|---|---|---|---|
| RS-232 | none | Bipolar-voltage serial port (PC COM port; bench instruments; BASIC Stamp programming); not directly MCU-compatible - MCUs use TTL-level serial | p.598, 608, 853, 891 |
| TTL serial (UART framing) | none | Point-to-point Tx/Rx, 8N1, LSB first, standard baud rates 110-256000 | p.891-892 |
| I2C / TWI | none | Two-wire open-drain bus with pull-ups, up to 400 kbit/s, 5 V or 3.3 V, multi-master | p.888-889 |
| SPI | none (bit order not defined by the standard) | 4-wire synchronous bus, up to 80 Mbit/s, one SS per slave; ICSP on AVR | p.890-891 |
| 1-Wire (Dallas Semiconductor) | none | Single-wire bus, parasitic power, 64-bit IDs, 60/15-us slots, >= 480-us reset | p.885-887 |
| USB / USB 2.0 | none | MCU programming and board interfaces | p.844, 865, 901 |
| HPIB (GPIB) | none | Instrument interface (Agilent 33120A) | p.608 |
| ASCII | none | 7-bit character code (128 codes; 00-1F control, 20-7F printing); 8th bit parity/special | p.723-724, Tables 12.2-12.3 |
| ICSP (in-circuit serial programming) | none | 6-pin programming header (AVR) | p.848 |
| X-10 | none | Powerline control codes (PBASIC XOUT) | p.858, Table 13.1 |
| DTMF | none | Telephone touch tones (PBASIC DTMFOUT; HT9200 IC) | p.858, 964 |
| FCC RC allocations (US) | none | 72-MHz band channels 11-60 for model aircraft (no licence); 50 MHz with amateur licence; 27 MHz any model | p.938 |
| Bluetooth, Wi-Fi, XBee (Digi, proprietary socket), GSM/GPRS/SMS, MIDI, CAN | none | Module-level wireless/data interfaces | p.965-968 |
| SIMM (30/72-pin), DIMM (168-pin SDRAM; 240-pin DDR3), SODIMM; EDO, SDRAM, DDR, RDRAM | none | Computer memory module formats and DRAM technologies | p.840-841 |
| Verilog, VHDL | none | Hardware description languages (VHDL strongly typed, favored in aerospace/defence) | p.914-931 |
| Mains plug types A-L | none | Plug designations per country (Fig. A.6) | p.978 |
| NM-B (indoor), UF-B (outdoor) cable; RG-59, RG-11 coax; CAT5 | none | Wire/cable types for the lab stock | p.624 |
| Local electrical code / inspector | none | Home wiring practice varies by region; consult the inspector | p.976-977 |

## 7. Process / lifecycle guidance

The book is not a product-development text; the part-2 range contains only the following stage guidance.

| Stage | Activity | Deliverable | Exit criterion | Source |
|---|---|---|---|---|
| Architecture | Check for a dedicated IC or module before designing from discrete parts; if > ~3 logic ICs are needed use an MCU (or FPGA/CPLD for speed) | block diagram with part choices | no function built discretely where an IC/module exists | p.717, 753, 897, 963 (SCHERZ-2157, 2274) |
| Prototype | Build with dev boards, breakout boards, shields, interpreter/boot-loader MCUs (BASIC Stamp, Arduino); keep an ICSP header on development PCBs | working proof of concept | function demonstrated; firmware iterated in small chunks | p.848, 862, 964 (SCHERZ-2207, 2238, 2278) |
| Pre-hardware verification (programmable logic) | Simulate HDL modules with a test fixture | simulation waveforms | outputs match expected sequence | p.928-931 (SCHERZ-2243) |
| Design for production | Remove the dev board/interpreter/external EEPROM; program the bare MCU (add crystal/resonator and regulator); replace EPROM with mask ROM only above a couple thousand units without updates; FPGAs may prototype an ASIC for very large runs | custom PCB + BOM | only needed features retained; mask/NRE justified by volume | p.832-834, 862, 872, 900 (SCHERZ-2198, 2218, 2238) |
| Enclosure / power-supply build | Transformer on chassis at rear, fuse/switch/binding posts at rear, boards on standoffs, heat-sunk regulators, vents, grounded enclosure, grommet strain relief, insulated 120-V connections | assembled supply | inspection checklist SCHERZ-2154 passes | p.716 |
| Bench test setup | Calibrated instruments with adequate bandwidth, compensated probes, isolation transformer for line-powered DUTs; state measurement uncertainty | test plan and results with uncertainties | instrument/probe checks (SCHERZ-2007..2026) and uncertainty propagation (SCHERZ-2285..2287) complete | p.586-616, 979-982 |
| Buying used test equipment | Verify working order and recent calibration; ask for an inspection period | calibrated instrument | calibration certificate/inspection passed | p.596 |

## 8. Coverage log

Source text: Practical_Electronics_for_Inventors_Paul_Scherz_Simon_Monk_2.txt (56,820 lines). This extraction = part 2 (lines ~28259-55306; index 55307-56820 skipped). Front matter / TOC (lines 1-2420) read for orientation.

| Lines | Content | Status |
|---|---|---|
| 1-2420 | Front matter, TOC, preface | read (orientation only) |
| 28200-29164 | Ch. 7 §7.4.5 (tail, trigger coupling) - §7.5.23 (scope measurements, lab equipment, probes, soldering, prototyping, tools, CAD, workbench) | read; started at §7.4.6 boundary (line 28259) to overlap part 1 slightly; supplier/catalog lists, CAD product blurbs and workbench plans (Fig. 7.78) not mined (no design numbers) |
| 29165-32125 | Ch. 8 Operational Amplifiers (§8.1-8.18) | read fully; water analogy (§8.1) and internal-schematic prose not mined; Table 8.1 reconstructed from column-scrambled OCR (column order verified by row count) |
| 32126-34635 | Ch. 9 Filters (§9.1-9.9) | read fully; transfer-function theory prose not mined; response graphs (Fig. 9.5-9.6) not in text - order choices taken from worked examples; four printed-example inconsistencies recomputed and flagged in §5 |
| 34636-36237 | Ch. 10 Oscillators and Timers (§10.1-10.7) | read fully; Table 10.1 reconstructed from scrambled OCR; 555 frequency-vs-RC graph (Fig. 10.7) not transcribable |
| 36238-37320 | Ch. 11 Voltage Regulators and Power Supplies (§11.1-11.11) | read fully; switcher block-diagram prose summarized only where numeric; battery-charger figure values (Fig. 11.6) partly OCR-garbled, not mined |
| 37321-48501 | Ch. 12 Digital Electronics (§12.1-12.11) | read fully; number systems, Boolean algebra, Karnaugh maps, ASCII tables, gate/counter/shift-register pinouts and truth tables read but not mined (no design limits); LCD physics prose summarized to its checkable limits; Fig. 12.139 (HD44780 instruction set) and Fig. 12.141 address maps not in text |
| 48502-50434 | Ch. 13 Microcontrollers (§13.1-13.5) | read fully; PBASIC language/instruction tables, robot program listings and Arduino library tables read, only hardware-relevant limits mined; Fig. 13.21-13.29 schematics (transistor/MOSFET drivers, sound, DAC) not in text - values taken from prose |
| 50435-50990 | Ch. 14 Programmable Logic (§14.1-14.11) | read fully; ISE tool walkthrough screens and Verilog syntax tutorial not mined beyond constraints/simulation/startup rules |
| 50991-52345 | Ch. 15 Motors (§15.1-15.9) | read fully; stepper physical-model prose summarized as sequences/tables |
| 52346-53584 | Ch. 16 Audio Electronics (§16.1-16.12) | read fully; Fourier/timbre prose not mined; miscellaneous circuit figures (Fig. 16.19-16.22) only partially legible - generic driver rules only |
| 53585-53782 | Ch. 17 Modular Electronics (§17.1-17.4) | read fully; supplier SKUs and .NET Gadgeteer/open-source-hardware lists not mined |
| 53783-54374 | Appendix A Power Distribution and Home Wiring | read fully; Fig. A.6 country table transcribed in OCR order (column alignment unverifiable) |
| 54375-54594 | Appendix B Error Analysis | read fully |
| 54595-55306 | Appendix C Useful Facts and Formulas | read; pure math reference (algebra, trig, calculus) not mined except unit prefixes/angle conversion |
| 55307-56820 | Index | skipped (per brief) |

**Skipped content (by rule of the brief):** exercises (none in range), pure-math derivations (Appendix C, Boolean-algebra proofs), historical/marketing prose (catalog supplier lists, CAD product blurbs, ISE installation walkthrough, open-source-hardware history).

**Extraction limitations:**
- Figures are absent from the text layer: values that live only in schematics (e.g. Fig. 13.21-13.29, 16.19-16.22) or graphs (Fig. 9.6 Butterworth attenuation curves, Fig. 10.7 555 frequency chart, Fig. 12.86 pull-up curves) were taken only where the prose restates them; graph-derived rows are conf medium.
- Multi-column tables (Tables 8.1, 10.1, A.6) were emitted by the PDF extractor column-by-column; they were reconstructed by counting entries per column. Table 8.1 "GAIN MIN" header reads "(mA)" in OCR; values are dB.
- Several formulas lost radicals or fraction bars in OCR (e.g. sqrt(3) in three-phase, MF5 f0 radical, TDR impedance formula p.592); reconstructed ones are conf medium, unrecoverable ones conf low and flagged.
- Arithmetic of worked examples was re-checked; inconsistencies (Fig. 7.39 Vrms, Fig. 9.17 capacitor value, Fig. 9.19 resistor values, notch resonating frequency p.675, Butterworth order for As = 1.7/1.88, pull-up dissipation p.779, Table 12.2 "540 K", debounce code p.878, delayMicroseconds example, servo wire colours, prescaler description p.926, degree-to-radian constant) are listed as ERRATA in §5 rather than silently corrected in §1.
- Rules total: 287 (SCHERZ-2001 ... SCHERZ-2287).
