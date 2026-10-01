# Fundamentals of Power Electronics (3rd ed.), part 2 — Anvil rulebook

## 0. Citation

R. W. Erickson and D. Maksimović, *Fundamentals of Power Electronics*, 3rd ed. Cham, Switzerland: Springer Nature Switzerland AG, 2020. ISBN 978-3-030-43879-1 (print), ISBN 978-3-030-43881-4 (eBook), doi:10.1007/978-3-030-43881-4.

Chapters covered by THIS extraction (source text lines 34280–68610; part 1 = ERICKSON-power-electronics-part1.md, ids ERICKSON-1001…1199, covers Chs.1–12 and §13.1–13.3 through p.525):
- Part IV Advanced Modeling, Analysis, and Control Techniques: Ch.13 remainder (§13.3 from p.525, §13.4 closed-loop regulator, §13.5); Ch.14 Circuit Averaging, Averaged Switch Modeling, and Simulation; Ch.15 Equivalent Circuit Modeling of the Discontinuous Conduction Mode; Ch.16 Extra Element Theorems (EET, n-EET); Ch.17 Input Filter Design; Ch.18 Current-Programmed Control (incl. sampled-data model, DCM CPM, average current-mode control); Ch.19 Digital Control of Switched-Mode Power Converters.
- Part V Modern Rectifiers and Power System Harmonics: Ch.20 Power and Harmonics in Nonsinusoidal Systems; Ch.21 Pulse-Width Modulated Rectifiers (PFC).
- Part VI Resonant Converters: Ch.22 Resonant Conversion; Ch.23 Soft Switching.
- Appendix A RMS Values of Commonly Observed Converter Waveforms; Appendix B Magnetics Design Tables (pot, EE, EC, ETD, PQ core data; AWG data).

Chapters NOT read by this extraction: none within the assigned range. Index (pp.1071–) skipped per brief; reference list (pp.1051–1070) scanned only for cited standards. Magnetics theory and the Kg/Kgfe design procedures (Chs.10–12) are in the part-1 rulebook; this part supplies the Appendix-B core/AWG tables those procedures need.

## 1. Design rules

Notation (author's): D = duty cycle, D' = 1 − D, Ts = 1/fs, Vg = input voltage, V = output voltage, R = load, M = V/Vg. Ripple symbols ΔiL, Δv are PEAK (half peak-to-peak) values. T = loop gain, fc = crossover frequency, φm = phase margin. Ids ERICKSON-2001… (part 1 of this book used ERICKSON-1001…1199 for Chs.1–13.3).

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| ERICKSON-2001 | control-loop | Feedback theorem: any closed-loop gain splits into an ideal gain G∞ (loop gain → ∞, error nulled) and a direct-forward-transmission gain G0 (loop gain → 0), weighted by T | G = G∞·T/(1+T) + G0·1/(1+T); reciprocity T = G0·Tn/G∞ (Tn = null loop gain) | G∞, G0, T | Any linear feedback circuit (op-amp compensator, closed-loop converter) | calc | §13.2; Eq.(13.1), (13.65), (13.75) p.525–528 | high |
| ERICKSON-2002 | control-loop | Crossover of a loop gain with dc gain T0 and two low-frequency poles f1, f4 (−40 dB/dec region) | fc = sqrt(T0·f1·f4); example T0 = 33000 (90.7 dB), f1 = 10 Hz, f4 = 1.9 kHz → fc = 25.2 kHz | T0, f1, f4 | Valid when fc lies above both poles and below the next zero | calc | §13.3 Eq.(13.69)–(13.70) p.526 | high |
| ERICKSON-2003 | control-loop | Closed-loop peaking from phase margin (op-amp PD example): φm = 14.2° gives closed-loop pole Q = 4 (12 dB) at fc | Q = sqrt(cos φm)/sin φm; φm = 14.2° → Q = 4 ⇒ 12 dB | φm | Second-order closed-loop approximation at fc (Eq. 9.41) | calc | §13.3 Eq.(13.71)–(13.74) p.527 | high |
| ERICKSON-2004 | control-loop | An op-amp compensator deviates from its ideal (virtual-ground) transfer function G∞ above the op-amp circuit's own crossover; its internal resonance there can add extra converter crossovers and cut converter phase margin. Keep the op-amp-circuit crossover well above the converter loop fc; op-amp circuit fc scales with op-amp unity-gain frequency | Example: op-amp fGBW = 1 MHz → PD circuit fc = 25 kHz (Q = 4 resonance); fGBW = 4 MHz → PD circuit fc = 100 kHz | fGBW, compensator gain, converter fc | PD/PID compensators built on real op amps (finite GBW, Ro) | sim | §13.3 p.528; Key pt 3 p.540 | high |
| ERICKSON-2005 | control-loop | A transconductance (gm) "error amplifier" in a PWM controller IC is not a low-Zout op amp; the compensator gain then depends on gm, which varies with process/temperature — design so G ≈ G∞ for the full gm range, or the regulator can oscillate | Example spread: gm_min = 100 μA/V to gm_max = 1 mA/V | gm range, compensator R/C | PI/PID compensators built on OTA error amps in PWM controller ICs | sim | §13 Problem 13.3 p.541–543 | medium |
| ERICKSON-2006 | control-loop | Closed-loop buck regulator (feedback-theorem form): ideal reference gain set by divider; line-to-output and output impedance reduced by 1/(1+T) below fc and equal to open-loop values above fc | G∞r(0) = (R1 + R2 + R4)/R4; Gg = M·He/(1+T); Zo = (Zout ∥ Z1)/(1+T) ≈ Zout/(1+T) when Zout << Z1; G∞g = 0; Z∞o = 0 | R1, R2, R4, T, Zout | Voltage-mode CCM buck with op-amp PID; Z1 = R1 + (R2 ∥ 1/(sC2)) | calc | §13.4 Eq.(13.84), (13.103)–(13.104) p.530–539 | high |
| ERICKSON-2007 | control-loop | Worked closed-loop buck regulator values (reference design for sim regression) | L = 50 μH, C = 500 μF, R = 3 Ω, Vg = 28 V, V = 15 V; Vref = 5 V, VM = 4 V, R1 = 11 kΩ, R2 = 85 kΩ, R3 = 120 kΩ, R4 = 47 kΩ, C2 = 1.1 nF, C3 = 2.7 nF; loop crossover (bandwidth) 5 kHz | — | Example of §9.5.4 / Fig.15.29 | sim | §13.4 p.532 | high |
| ERICKSON-2008 | control-loop | Direct forward transmission of the reference through the feedback divider G0r = Zout/(Zout + Z1) is negligible below fs/2; Gr follows G∞r from dc to the loop bandwidth | G0r = Zout/(Zout + Z1) | Zout, Z1 | Voltage-mode regulator | sim | §13.4 Eq.(13.88) p.531–532 | high |
| ERICKSON-2009 | control-loop | Output-impedance spec check (problem spec): closed-loop output impedance magnitude below a limit over a band | example spec abs(Zo) < 0.2 Ω for 0–20 kHz | Zo(f) | Problem 13.8 / 9.8 specification | sim | §13 Problem 13.8 p.545 | medium |
| ERICKSON-2010 | control-loop | CCM two-switch averaged switch model (transistor port 1, diode port 2): same for buck, boost, buck–boost, SEPIC, Ćuk; large-signal <v1> = (d'/d)<v2>, <i2> = (d'/d)<i1>; small-signal adds sources (V1/(D·D'))·d̂ and (I2/(D·D'))·d̂ with ideal D':D transformer | v1 = (D'/D)·v2 − d̂·V1/(D·D'); i2 = (D'/D)·i1 − d̂·I2/(D·D') | D, V1, I2 | Valid for frequencies sufficiently below fs and small inductor-current / capacitor-voltage ripple (invalid for large ripple / DCM) | sim | §14.1.2–14.1.3 Eq.(14.7)–(14.14), Fig.14.4 p.551–554 | high |
| ERICKSON-2011 | power | Indirect vs direct power: buck and boost pass part of their power directly (dc conduction loss only); buck–boost, SEPIC, Ćuk and all transformer-isolated converters process 100% indirect power (inversion + rectification: dc conduction + magnetics ac loss + switching loss), so expect lower efficiency for higher indirect-power fraction | Indirect power = −<ṽ1·ĩ1> (ac power at fs and harmonics); topology screen: prefer lower indirect fraction for efficiency | topology, M | Topology selection / efficiency estimation | review | §14.1.4 Eq.(14.22), (14.30) p.555–558 | high |
| ERICKSON-2012 | control-loop | Buck and boost switch networks with common-ground ports give simpler equivalent (identical-prediction) averaged models: buck = 1:D transformer + sources I2·d̂ (input) and V1·d̂ (output); boost = D':1 transformer + sources V·d̂ and I·d̂ | Buck: <i1> = d·<i2>, <v2> = d·<v1>; I1 + î1 = D(I2 + î2) + I2·d̂; V2 + v̂2 = D(V1 + v̂1) + V1·d̂. Boost: <v1> = d'·<v2>, <i2> = d'·<i1> | D, V1, I2, V, I | CCM, small ripple (ripple small or linear in time) | sim | §14.2 Eq.(14.33)–(14.38), Figs.14.13–14.17 p.561–566 | high |
| ERICKSON-2013 | process | Design verification by simulation must be worst-case: sweep production tolerances, temperature and aging of component parameters and iterate until worst-case behaviour meets spec (or yield/reliability is acceptable) | Worst-case / yield analysis over parameter ranges | component tolerance, temperature, aging ranges | All converter design verification | sim | §14.3 p.566–567 | high |
| ERICKSON-2014 | process | Pick the simulation model level by task: detailed device models (vendor libraries + package/board parasitics, time steps of a few ns or less) only for switching transitions, switching loss and instantaneous stress over short intervals; ideal/piecewise-linear switch models (e.g. PLECS, SIMPLIS) for ripple, stress and transients over many cycles; averaged models for efficiency, dc operating point, stability, large-signal transients and small-signal ac (ac sweeps are only possible on averaged models) | Detailed-model time step ≤ a few ns | task type | Converter simulation planning | review | §14.3 items 1–3 p.567; §14.3.5 p.578 | high |
| ERICKSON-2015 | control-loop | SPICE CCM averaged switch subcircuit CCM1 (general two-switch network; nodes 1 transistor+, 2 transistor−, 3 diode cathode, 4 diode anode, 5 duty input 0–1 V) | `.subckt CCM1 1 2 3 4 5` / `Et 1 2 value={(1-v(5))*v(3,4)/v(5)}` / `Gd 4 3 value={(1-v(5))*i(Et)/v(5)}` / `.ends` | d = v(5) | Ideal switches, CCM only, no transformer; with an isolation transformer divide the right-hand sides by the turns ratio | sim | §14.3.1 Eq.(14.39)–(14.40), Fig.14.18 p.568–569 | high |
| ERICKSON-2016 | control-loop | Averaged switch models have a discontinuity at d = 0: clamp the duty input | 0 < Dmin ≤ d ≤ 1 (example sweeps start at D = 0.1) | d | CCM1/CCM2 subcircuits | sim | §14.3.1 p.568; §14.3.4 p.573 | high |
| ERICKSON-2017 | power | Averaged switch model with conduction losses (general two-switch network): transistor Ron and diode VD, RD reflect into port 1 as a duty-dependent resistance plus a shifted source | <v1> = (Ron/d + d'·RD/d^2)·<i1> + (d'/d)·(<v2> + VD); <i2> = (d'/d)·<i1> | Ron (Ω), VD (V), RD (Ω), d | CCM, small inductor ripple | sim | §14.3.2–14.3.3 Eq.(14.46)–(14.49), Fig.14.20 p.570–571 | high |
| ERICKSON-2018 | power | SPICE subcircuit CCM2 (conduction losses) | `.subckt CCM2 1 2 3 4 5` `+params: Ron=0 VD=0 RD=0` / `Er 1 1x value={i(Et)*(Ron+(1-v(5))*RD/v(5))/v(5)}` / `Et 1x 2 value={(1-v(5))*(v(3,4)+VD)/v(5)}` / `Gd 4 3 value={(1-v(5))*i(Et)/v(5)}` / `.ends` | Ron, VD, RD | CCM only, no transformer | sim | §14.3.3 Fig.14.22 p.573 | high |
| ERICKSON-2019 | power | A fixed diode-drop VD model gives physically impossible polarities, losses and efficiency when the converter runs in DCM or at low duty cycle where VD is comparable to or larger than V; do not trust CCM2 there | Restrict CCM2 efficiency sweeps to CCM and D ≥ ~0.1 | VD, V, mode | Averaged loss simulation | sim | §14.3.3 p.572; §14.3.4 p.573 | high |
| ERICKSON-2020 | power | SEPIC efficiency-vs-D behaviour: η falls at low D (VD comparable to V) and at high D (currents rise, conduction loss); V and η → 0 as D → 1; use the family of η(D) curves vs Ron to select the MOSFET Ron for a required V and η | Example: Vg = 50 V, L1 = 800 μH (RL1 = 0.5 Ω), L2 = 100 μH (RL2 = 0.1 Ω), C1 = C2 = 100 μF, Rload = 50 Ω, VD = 0.8 V, RD = 0.05 Ω, Ron = 0 / 0.5 / 1 Ω; `.dc lin Vc 0.1 1 0.01`, `.step lin PARAM Ron 0 1 0.5` | Ron, VD, RL, D | CCM SEPIC | sim | §14.3.4 Figs.14.23–14.24 p.573–575 | high (curves: graph) |
| ERICKSON-2021 | power | Start-up transients expose components to much higher current than steady state; include soft-start (duty ramped slowly from zero) and verify start-up stress by transient simulation | Example buck–boost: Vg = 15 V, L = 15 μH, RL = 0.1 Ω, C = 50 μF, R = 20 Ω, fs = 100 kHz, D = 0.8; inductor start-up current on a 0–60 A axis (graph) vs ≈15 A ideal steady state | L, C, R, D, soft-start ramp | Any converter power-up | sim | §14.3.5 Figs.14.25–14.28 p.576–578 | medium |
| ERICKSON-2022 | process | Switch-level SPICE model setup used for transient verification (simple models: no switching-loss prediction) | `.model switch vswitch(Ron=0.05 Roff=10meg Von=6V Voff=4V)`; `.model diode d(Is=1e-12)`; pulse 0–10 V, tr = tf = 100 ns, tp = 7.9 μs, Ts = 10 μs → D = (tp + 0.5(tr + tf))/Ts = 0.8; `.tran 1u 1.2m 0m 1u uic` | tp, tr, tf, Ts | Switching-circuit simulation; cannot be used to examine switching transitions or switching loss | sim | §14.3.5 Fig.14.26 p.576–577 | high |
| ERICKSON-2023 | power | Diode reverse-recovery charge model form used for averaged loss simulation (problem data) | Qr = kq·sqrt(I1); example kq = 100 nC/A^(1/2), tr = 100 ns (constant), Vg = 100 V, D = 0.5, fs = 100 kHz, RL = 0.1 Ω, ILOAD 1–10 A | kq, I1, tr | Boost converter with diode stored-charge switching loss (Problem 14.11) | sim | §14 Problem 14.11 p.582–583 | medium |
| ERICKSON-2024 | power | DCM averaging: inductor volt-second balance holds at all times (not only in equilibrium), so inductor dynamics drop out of the low-frequency model; DCM converters have reduced-order (essentially single-pole) dynamics | <vL>Ts ≈ 0 at all times | mode | DCM, modulation frequency << fs | review | §15.1 Eq.(15.6) p.588 | high |
| ERICKSON-2025 | power | DCM peak inductor (switch) current of buck–boost-type switch network | ipk = vg·d1·Ts/L | vg (V), d1, Ts (s), L (H) | DCM, d1 = transistor duty cycle | calc | §15.2 Eq.(15.7) p.589 | high |
| ERICKSON-2026 | power | Loss-free resistor (LFR) model of any DCM two-switch network: transistor port is an effective resistance Re, diode port a dependent power source P = <v1>^2/Re | Buck, boost, buck–boost: Re = 2L/(d^2·Ts); Ćuk, SEPIC: Re = 2(L1∥L2)/(d^2·Ts); <i1> = <v1>/Re; <i2>·<v2> = <v1>^2/Re | L (H), d, Ts (s) | DCM, lossless switch network; also valid with ac (rms) waveforms | calc | §15.2 Eq.(15.20)–(15.24), (15.37)–(15.38) p.592–598 | high |
| ERICKSON-2027 | power | Average DCM transistor current is NOT d·<iL>: compute from the actual triangular pulse | <i1> = d1^2·Ts·<v1>/(2L); <i2> = d1^2·Ts·<v1>^2/(2L·<v2>) | d1, Ts, L, v1, v2 | DCM (large ripple) | calc | §15.2 Eq.(15.14), (15.21) p.591–592 | high |
| ERICKSON-2028 | power | DCM steady-state output of any LFR-modelled converter with resistive load: equate input and output power | V = ± Vg·sqrt(R/Re); buck–boost: V = −Vg·D/sqrt(K), K = 2L/(R·Ts); rms form: Vrms = Vg,rms·sqrt(R/Re) | R, Re, D, K | DCM, resistive load; polarity from topology | calc | §15.2 Eq.(15.30)–(15.36) p.597–598 | high |
| ERICKSON-2029 | power | Ideal power source (DCM diode port) must never be short-circuited (infinite current) nor open-circuited (infinite voltage): a DCM converter needs a load able to absorb P or the output voltage rises without limit; series/parallel power sources add; reflection through any transformer turns ratio leaves P unchanged | Operating point = intersection of load i–v curve and v·i = P | P, load curve | DCM (and any lossless 2-port with load-independent port-1 quantities) | review | §15.2 p.594–595, Figs.15.8–15.10 | high |
| ERICKSON-2030 | power | CCM/DCM boundary for buck, boost, buck–boost, Ćuk, SEPIC in LFR terms | CCM if I > Icrit, DCM if I < Icrit; Icrit = ((1 − D)/D)·Vg/Re(D) | I (A), D, Vg, Re | Ideal basic converters, resistive load | calc | §15.2 Eq.(15.39)–(15.40) p.598 | high |
| ERICKSON-2031 | power | SEPIC CCM condition expressed as load resistance (worked example) | CCM if R < 2(L1∥L2)/((1 − D)^2·Ts); example L1 = 500 μH, L2 = 100 μH (L1∥L2 = 83.3 μH), D = 0.4, fs = 100 kHz → R < 46 Ω | L1, L2, D, fs, R | CCM SEPIC, losses neglected (V/Vg ≈ D/(1 − D)) | calc | §15.4.1 Eq.(15.69)–(15.71) p.611–612 | high |
| ERICKSON-2032 | control-loop | DCM small-signal switch parameters (Table 15.2) for control-loop models | General two-switch: r1 = Re, g1 = 0, j1 = 2V1/(D·Re), r2 = M^2·Re, g2 = 2/(M·Re), j2 = 2V1/(D·M·Re). Buck network: r1 = Re, g1 = −1/Re, j1 = 2(1 − M)V1/(D·Re), r2 = M^2·Re, g2 = (2 − M)/(M·Re), j2 = 2(1 − M)V1/(D·M·Re). Boost network: r1 = (M − 1)^2·Re/M^2, g1 = −1/((M − 1)^2·Re), j1 = 2M·V1/(D(M − 1)Re), r2 = (M − 1)^2·Re, g2 = (2M − 1)/((M − 1)^2·Re), j2 = 2V1/(D(M − 1)Re) | Re, M, V1, D | DCM, low-frequency (L shorted) model | calc | §15.3 Table 15.2 p.604 | high (buck/boost g1 signs re-derived from Eq.(15.20)–(15.21)) |
| ERICKSON-2033 | control-loop | DCM control-to-output and line-to-output transfer functions are single-pole (Table 15.3) | Gvd = Gd0/(1 + s/ωp), Gvg = Gg0/(1 + s/ωp), Gg0 = M. Buck: Gd0 = (2V/D)(1 − M)/(2 − M), ωp = (2 − M)/((1 − M)RC). Boost: Gd0 = (2V/D)(M − 1)/(2M − 1), ωp = (2M − 1)/((M − 1)RC). Buck–boost: Gd0 = V/D, ωp = 2/(RC) | V, D, M, R, C | DCM, resistive load, inductor dynamics neglected | calc | §15.3 Eq.(15.57)–(15.60), Table 15.3 p.605–607 | high |
| ERICKSON-2034 | control-loop | Worked DCM boost Gvd example (regression anchor) | R = 12 Ω, L = 5 μH, C = 470 μF, fs = 100 kHz, V = 36 V, I = 3 A, Vg = 24 V → P = I(V − Vg) = 36 W, Re = Vg^2/P = 16 Ω, D = sqrt(2L/(Re·Ts)) = 0.25, Gd0 = 72 V (37 dBV), fp = 112 Hz; accurate model adds pole f2 = 64 kHz and RHP zero fz = 127 kHz; extra phase lag visible from f2/10 = 6.4 kHz | — | DCM boost | sim | §15.3.1 Eq.(15.61)–(15.65), Fig.15.22 p.607–608 | high |
| ERICKSON-2035 | control-loop | DCM high-frequency pole (PWM sampling + equivalent hold of the inductor-current response): always above ≈ fs/3, usually negligible; DCM RHP-zero effect lasts only a fraction of Ts and has essentially no impact on loop design | f2 = fs/(π·D2); buck f2 = M·fs/(π·D·(1 − M)); boost f2 = (M − 1)·fs/(π·D); buck–boost f2 = abs(M)·fs/(π·D); Gic(s) ≈ ((m1 + m2)·D2·Ts/VM)/(1 + s/ω2) | fs, D, D2, M | DCM, first-order Padé approximation of e^(−s·D2·Ts) | calc | §15.5 Eq.(15.90)–(15.93), Table 15.4 p.620–621 | high |
| ERICKSON-2036 | control-loop | Effective switch conversion ratio μ unifies CCM/DCM averaged models: use CCM formulas with d replaced by μ; μ = larger of the CCM and DCM values; unloaded converter → μ = 1 and V = Vg·M(1) | μ = max(d, 1/(1 + Re·<i1>/<v2>)), Re = 2L/(d^2·Ts) | d, Re, i1, v2 | Two-switch PWM converters in CCM or DCM | sim | §15.4 Eq.(15.66)–(15.68) p.608–610 | high |
| ERICKSON-2037 | control-loop | SPICE combined CCM/DCM averaged switch subcircuit CCM-DCM1 (for dc, ac and transient) | `.subckt CCM-DCM1 1 2 3 4 5` `+ params: L=100u fs=1E5` / `Et 1 2 value={(1-v(u))*v(3,4)/v(u)}` / `Gd 4 3 value={(1-v(u))*i(Et)/v(u)}` / `Ga 0 a value={MAX(i(Et),0)}` / `Va a b` / `Ra b 0 1k` / `Eu u 0 table {MAX(v(5), v(5)*v(5)/(v(5)*v(5)+2*L*fs*i(Va)/v(3,4)))} (0 0) (1 1)` / `.ends`; L parameter = the DCM-relevant inductance (SEPIC/Ćuk: L1∥L2) | L, fs | Ideal switches, no transformer (modify for isolated converters); auxiliary Ga/Va/Ra forces correct current polarities | sim | §15.4 Fig.15.25 p.610–611 | high |
| ERICKSON-2038 | control-loop | Loop design must be verified at light load where the converter enters DCM: crossover and line rejection degrade drastically even though dc operating points look alike | Buck regulator example (Vg = 28 V, V = 15 V, L = 50 μH, C = 500 μF, fs = 100 kHz): R = 3 Ω (CCM, D = 0.543) fc = 5.3 kHz, φm = 47° (design 5 kHz / 52°); R = 25 Ω (DCM, D = 0.508) fc = 390 Hz, φm = 55°; closed-loop Gvg at 100 Hz = 0.012 (−38 dB) at 3 Ω vs 0.02 (−34 dB) at 25 Ω | R range, mode | Any converter whose load range spans CCM and DCM | sim | §15.4.2 Eq.(15.83)–(15.84), Figs.15.30–15.31 p.616–617 | high |
| ERICKSON-2039 | control-loop | CCM vs DCM SEPIC control-to-output responses differ qualitatively at nearly equal dc points (R = 40 Ω CCM: 4th order, two high-Q complex pole pairs, complex zero pair, RHP zero toward 50 kHz; R = 50 Ω DCM: dominant low-frequency pole + closely spaced complex poles/zeros): design compensation for both | Example Vg = 120 V, L1 = 500 μH (0.1 Ω), L2 = 100 μH (0.02 Ω), C1 = 47 μF, C2 = 200 μF, D = 0.4, fs = 100 kHz; `.ac` 5 Hz–50 kHz, 201 points/decade | R, mode | SEPIC or other higher-order converters | sim | §15.4.1 Fig.15.26–15.28 p.611–614 | high (responses: graph) |
| ERICKSON-2040 | control-loop | PWM model for averaged simulation: duty = input/VM with hard limits (practical PWM ICs have Dmax < 1) | `Epwm value={LIMIT(0.25*vx, 0.1, 0.9)}` for VM = 4 V → Dmin = 0.1, Dmax = 0.9 | VM, Dmin, Dmax | Averaged closed-loop simulation | sim | §15.4.2 Eq.(15.72), Fig.15.29 p.614–615 | high |
| ERICKSON-2041 | control-loop | Help SPICE dc-operating-point convergence in high-dc-gain feedback loops with .nodeset on expected node voltages (output, op-amp input, duty ≈ V/Vg) | Example `.nodeset v(3)=15 v(5)=5 v(6)=4.144 v(8)=0.536` | expected V, Vref, D | Closed-loop averaged simulation | sim | §15.4.2 p.616 | high |
| ERICKSON-2042 | control-loop | Simulated loop-gain measurement: inject vz between the compensator output (low Zout, op amp) and the PWM input (very high Zin); T = −v̂y/v̂x with ac amplitude 1 | T(s) = v̂y/v̂x (Fig.15.29: T = −v(6)/v(7)) | injection node impedances | Voltage-injection method of §9.6.1 applied in SPICE | sim | §15.4.2 Eq.(15.82) p.616 | high |
| ERICKSON-2043 | control-loop | PID compensator of the buck regulator example: component-to-pole/zero mapping and values | GcmH = R3/(R1 + R2); fz = 1/(2π·R2·C2); fL = 1/(2π·R3·C3); fp = 1/(2π·(R1∥R2)·C2); design: GcmH = 3.7·(1/3) = 1.23, fz = 1.7 kHz, fL = 500 Hz, fp = 14.5 kHz → C2 = 1.1 nF, R2 = 85 kΩ, R1 = 11 kΩ, R3 = 120 kΩ, C3 = 2.7 nF, R4 = 47 kΩ (sets V = 15 V with Vref = 5 V); LM324 op amp | R1..R4, C2, C3 | Op-amp PID around voltage-mode buck | calc | §15.4.2 Eq.(15.74)–(15.81) p.615 | high (book prints "C3 = 2.7 kΩ", typo for nF) |
| ERICKSON-2044 | control-loop | Load-step verification: closed-loop regulator should show a small, well-damped deviation; open loop shows large undershoot and long lightly damped ringing | Example: iLOAD 1.5 A → 5 A at t = 0.1 ms: closed-loop output drop ≈ 0.2 V, fast well-damped recovery | load step, V | Voltage regulators | sim | §15.4.2 Fig.15.32 p.617–618 | high |
| ERICKSON-2045 | control-loop | Extra Element Theorem (EET): adding impedance Z at a port multiplies the original transfer function by a correction factor built from the port's null impedance ZN (output nulled) and driving-point impedance ZD (input zeroed) | Port originally open: G = G(Z→∞)·(1 + ZN/Z)/(1 + ZD/Z). Port originally shorted: G = G(Z→0)·(1 + Z/ZN)/(1 + Z/ZD). Reciprocity: G(Z→∞)/G(Z→0) = ZD/ZN | ZN, ZD, Z | Any linear circuit; ZN may be negative or have RHP poles/zeros (not a passive impedance) | calc | §16.1 Eq.(16.2)–(16.4), (16.26) p.626–631 | high |
| ERICKSON-2046 | control-loop | An added/parasitic element can be ignored where the impedance inequalities hold; quantitative margins for the correction-factor error | Open-port case: abs(Z) >> abs(ZN) and abs(Z) >> abs(ZD); shorted-port case: abs(Z) << abs(ZN), abs(ZD). abs(Z/ZN) (or Z/ZD) < −20 dB → deviation < ±1 dB and < ±7°; < −10 dB → < ±3.5 dB and < ±20° (any phase) | Z, ZN, ZD vs f | Graphical check over the frequency band of interest | calc | §16.1.3 Eq.(16.27)–(16.28), Figs.16.6–16.9 p.631–632 | high |
| ERICKSON-2047 | components | Capacitor ESR adds a zero and reduces filter Q; ESR loss Irms^2·Resr heats the capacitor and can cause failure | Zero at ωz = 1/(Resr·C); exact G = (1 + s·C·Resr)/(1 + s(L/R + Resr·C) + s^2·L·C·(R + Resr)/R); Q reduced by factor (1 + Resr/abs(ZD(f0))) | Resr (Ω), C, L, R, Irms | L–C output filters | calc | §16.2.2 Eq.(16.39)–(16.43) p.637–639 | high |
| ERICKSON-2048 | filter | Worked ESR example (regression anchor) | L = 100 μH, C = 1 μF, R = 100 Ω, Resr = 2 Ω: f0 = 15.9 kHz, R0 = 10 Ω, Q = 10; abs(ZD(f0)) ≈ 1 Ω → EET estimate Q ≈ 10/3 = 3.33; exact Q = 3.37, f0 → 15.8 kHz | — | Second-order LC low-pass | calc | §16.2.2 Eq.(16.42)–(16.43), Fig.16.16 p.639 | high |
| ERICKSON-2049 | control-loop | SEPIC Gvd = effective buck–boost Gvd−bb (C1 open) × EET correction factor for C1; Gvd−bb parameters | Gd0 = Vg/D'^2; ωo = 1/sqrt(C2·(L2 + (D/D')^2·L1)); Qo = R·sqrt(C2/(L2 + (D/D')^2·L1)); RHP zero ωz = (D'/D)^2·R/L1; low-frequency asymptote of ZN and ZD = s(L1 + L2) | Vg, D, L1, L2, C2, R | CCM SEPIC small-signal | calc | §16.2.3 Eq.(16.44)–(16.48), (16.53)–(16.59) p.640–644 | medium (OCR-reconstructed; checked against the book's 711 Hz / Q 4.9 / 4.5 kHz numbers) |
| ERICKSON-2050 | control-loop | SEPIC internal (C1) resonance: where abs(1/(ωC1)) ≈ abs(ZN), abs(ZD) with ≈180° relative phase, the correction factor adds two high-Q poles and two RHP zeros (−360°), making crossover above that frequency problematic | Example Vg = 18 V, V = 24 V, fs = 100 kHz, L1 = 100 μH, L2 = 50 μH, C1 = 22 μF, C2 = 220 μF, R = 5 Ω: Gvd−bb fo = 711 Hz, Qo = 4.9, RHP zero 4.5 kHz; C1 resonance at 3–4 kHz; Gvd = Gvd−bb below ≈2 kHz, Gvd−bb·(ZN/ZD) above ≈6 kHz; high-frequency phase −270° − 360° | L1, L2, C1, C2 | CCM SEPIC (also Ćuk) | sim | §16.2.4 Figs.16.21–16.22 p.644–647 | high |
| ERICKSON-2051 | control-loop | Damp the SEPIC C1 resonance with an Rb–Cb branch across C1: Rb must dominate Z where abs(Z) ≈ abs(ZN), abs(ZD); Cb blocks dc (no dc loss in Rb) and needs abs(1/(ωCb)) << Rb there | Example C1 = 22 μF, Rb = 2 Ω, Cb = 100 μF → Z phase ≈ −45° at ≈2 kHz; correction-factor Qs reduced, RHP zeros move to LHP, Gvd ≈ Gvd−bb; problem guidance: Cb = 10·C1, Rb centred on the resonance | C1, Rb, Cb | SEPIC/Ćuk energy-transfer capacitor | sim | §16.2.4 Eq.(16.61), Figs.16.23–16.26 p.647–648; Problem 16.2(d) p.670 | high |
| ERICKSON-2052 | filter | n-EET (dc-referenced): write any transfer function as Gdc·(1 + a1 s + …)/(1 + b1 s + …) with b1 = Σ Li/Ri + Σ Ri·Ci, where Ri = resistance seen at port i with all other reactive elements in dc state (L short, C open); higher terms reuse lower-order R's with already-used ports set to HF state (L open, C short); numerator R's found with the output nulled; add a dummy resistor if an intermediate coefficient is 0 (undamped resonance, 0·∞) | Example R1–L–C–R2: G = (R2/(R1 + R2))/(1 + s(L/(R1 + R2) + (R1∥R2)·C) + s^2·L·C·R2/(R1 + R2)) | circuit topology | Linear passive networks (filters, damping networks, compensators) | calc | §16.3 Eq.(16.62)–(16.73); §16.5.2 Eq.(16.104)–(16.106) p.648–668 | high |
| ERICKSON-2053 | filter | Two-section L–C filter (L1, shunt C1, L2, shunt C2, load R): four poles, no zeros, −80 dB/decade high-frequency slope | G(s) = 1/(1 + s(L1 + L2)/R + s^2(L1(C1 + C2) + L2·C2) + s^3·L1·L2·C1/R + s^4·L1·L2·C1·C2) | L1, L2, C1, C2, R | Undamped two-stage LC with resistive load | calc | §16.4.1 Eq.(16.77), Table 16.1 p.654–657 | high |
| ERICKSON-2054 | filter | Bridge-T filter (R1, R2 series; C1 shunt at mid node; C2 bridging input–output; R3 load): two poles, two zeros, unity HF gain | Gdc = R3/(R1 + R2 + R3); N(s) = 1 + s·C2(R1 + R2) + s^2·C1·C2·R1·R2; D(s) = 1 + s[C1·(R1∥(R2 + R3)) + C2·(R3∥(R1 + R2))] + s^2·C1·C2·(R1∥R2)·(R3∥(R1 + R2)) | R1, R2, R3, C1, C2 | As drawn in Fig.16.35 | calc | §16.4.2 Eq.(16.78)–(16.89) p.658–661 | medium (s^2 denominator term assembled from the stated RDa-b, RDb) |
| ERICKSON-2055 | filter | Output impedance of an L–C filter with R–L1 damping branch in parallel with L2 (reference gain R via frequency inversion) | Z(s) = sL2·(1 + sL1/R)/(1 + s(L1 + L2)/R + s^2·L2·C + s^3·L1·L2·C/R); approx. Z ≈ R·(1 + sL1/R)/((1 + R/(sL2))·(1 + s/(Q·ω0) + (s/ω0)^2)), ω0 = 1/sqrt(L1·C) (asymptotic approximation for the book's assumed values; relation between L1 and L2 lost in OCR) | R, L1, L2, C | Input-filter output impedance (Rf–Lb parallel damping); exact form Eq.(16.102) | calc | §16.5.1 Eq.(16.92), (16.101)–(16.102) p.662–667 | high (exact) / medium (approx.) |
| ERICKSON-2056 | emc | Buck (pulsating) input-current harmonic amplitudes; the input filter attenuates each harmonic by abs(H(jkω)) | ig(t) = D·I + Σk (2I/(kπ))·sin(kπD)·cos(kωt); filtered: iin(t) = H(0)·D·I + Σk abs(H(jkω))·(2I/(kπ))·sin(kπD)·cos(kωt + ∠H(jkω)) | I (A), D, fs | Ideal square pulse; real harmonics also raised by diode reverse-recovery spike and finite switching slopes | calc | §17.1.1 Eq.(17.1)–(17.2) p.675–676 | high |
| ERICKSON-2057 | emc | Conducted-EMI input filter attenuation target: several-ampere dc input current gives ≈1 A rms fundamental; regulations typically limit harmonics to 10–100 μA, so input filters typically need ≥ 80 dB attenuation at fs | Required attenuation (dB) = 20·log10(I_harmonic,rms / I_limit,rms); typical ≥ 80 dB; problem specs use 10 μA rms limit, 80–100 dB at fs | harmonic rms, limit | Switching converters on regulated supply lines | calc | §17.1.1 p.676; Problems 17.1–17.2, 17.4 p.721–722 | high |
| ERICKSON-2058 | emc | Conducted-susceptibility requirements force damping of input-filter resonances so input transients do not excite excessive filter/converter voltages or currents | Damped filter (peak abs(Zo) bounded, Qf ≈ 1) | — | Systems with conducted-susceptibility specs | review | §17.1.1 p.676; §17.4 p.693 | high |
| ERICKSON-2059 | control-loop | An undamped L–C input filter adds a complex pole pair and a complex RHP-zero pair to Gvd at its resonance ff (−360° extra phase; −540° high-frequency asymptote for a buck): if loop crossover fc is near or above ff, phase margin goes negative → oscillation | Worked example: D = 0.5, L = 100 μH, C = 100 μF, R = 3 Ω, Vg = 30 V, Lf = 330 μH, Cf = 470 μF → ff = 400 Hz, R0f = 0.84 Ω | ff, fc | Voltage-mode CCM converters with input filters | sim | §17.1.2 Fig.17.4 p.678; §17.3.1 p.688–691 | high |
| ERICKSON-2060 | control-loop | Effect of an input filter with output impedance Zo on converter transfer functions (EET) | Gvd' = Gvd·(1 + Zo/ZN)/(1 + Zo/ZD); Zout' = Zout·(1 + Zo/Ze)/(1 + Zo/ZD); ZN = −e(s)/j(s) (input impedance under ideal output regulation, generally negative); ZD = Zei/M^2 (open-loop input impedance, d̂ = 0); Ze = converter input impedance with output shorted | Zo(f), canonical e, j, Zei, M | CCM, canonical model | calc | §17.2.1 Eq.(17.4)–(17.14) p.679–682 | high |
| ERICKSON-2061 | control-loop | Ideal closed-loop regulator input port is a constant-power sink with negative incremental resistance; loading an undamped L–C filter with it forms a negative-resistance oscillator | vg·ig = Pload; r_in = −R/M^2 (M = V/Vg) | R, M | Well-regulated closed-loop converters (dc asymptote of Zi) | calc | §17.2.2 Eq.(17.15)–(17.17), Fig.17.10 p.682–684 | high |
| ERICKSON-2062 | filter | Input-filter design criteria impedances for basic CCM converters (Table 17.1) | Buck: ZN = −R/D^2; ZD = (R/D^2)·(1 + sL/R + s^2·L·C)/(1 + sRC); Ze = sL/D^2. Boost: ZN = −D'^2·R·(1 − sL/(D'^2·R)); ZD = D'^2·R·(1 + sL/(D'^2·R) + s^2·L·C/D'^2)/(1 + sRC); Ze = sL. Buck–boost: ZN = −(D'^2·R/D^2)·(1 − sDL/(D'^2·R)); ZD = (D'^2·R/D^2)·(1 + sL/(D'^2·R) + s^2·L·C/D'^2)/(1 + sRC); Ze = sL/D^2 | R, D, L, C | Voltage-mode CCM, ideal elements | calc | §17.2.3 Table 17.1 p.684 | high |
| ERICKSON-2063 | filter | Input-filter design inequalities: Gvd (loop gain) unchanged if the filter output impedance is well below ZN and ZD at all frequencies; open-loop output impedance unchanged if also well below Ze | abs(Zo) << abs(ZN) and abs(Zo) << abs(ZD) (Gvd); abs(Zo) << abs(Ze) and abs(Zo) << abs(ZD) (Zout); design margins used in problems: abs(Zo) < 0.2–0.4 × min(abs(ZN), abs(ZD)) for all f | Zo(f), ZN(f), ZD(f), Ze(f) | All converter input filters; use worst-case R/D^2 (heaviest load, lowest/highest line) | calc | §17.2.3 Eq.(17.19)–(17.20) p.684–685; Problems 17.4, 17.5, 17.11 p.722–723 | high |
| ERICKSON-2064 | filter | Buck example impedance anchors: ZN = −R/D^2 dc asymptote; ZD series resonance at f0 with magnitude R0/(D^2·Q) | R/D^2 = 12 Ω; f0 = 1/(2π·sqrt(L·C)) = 1.6 kHz; R0/D^2 = sqrt(L/C)/D^2 = 4 Ω; Q = R·sqrt(C/L) = 3 → abs(ZD(f0)) = 1.33 Ω; ff = 1/(2π·sqrt(Lf·Cf)) = 400 Hz; R0f = sqrt(Lf/Cf) = 0.84 Ω | L, C, R, D, Lf, Cf | Buck example of Fig.17.11 | calc | §17.3.1 Eq.(17.21)–(17.31), Fig.17.16 p.686–689 | high |
| ERICKSON-2065 | filter | Do not place the input-filter resonance ff at the converter output-filter resonance f0; separate them widely (ZD has its minimum at f0) | ff far from f0 (example ff = 400 Hz vs f0 = 1.6 kHz; two-stage example ff1 = 10.8 kHz) | ff, f0 | Input filter design | calc | §17.3.1 p.689; §17.4.5 p.701 | high (qualitative spacing: low) |
| ERICKSON-2066 | filter | Damping choices: Rf across Cf dissipates Vg^2/Rf (exceeds load power when Rf << R/D^2) — impractical; Rf across Lf degrades HF roll-off from −40 to −20 dB/decade; practical: Rf in series with dc-blocking Cb across Cf, with abs(1/(2π·ff·Cb)) << Rf | Example: Rf = 1 Ω (<< 12 Ω), Cb = 4700 μF → 1/(2π·ff·Cb) = 0.084 Ω; peak abs(Zo) ≈ Rf | Rf, Cb, ff, Vg | Single-section L–C input filter | calc | §17.3.2 Eq.(17.32), Figs.17.19–17.21 p.691–692 | high |
| ERICKSON-2067 | filter | Optimal Rf–Cb parallel damping (minimum Cb for a required peak output impedance) | n = Cb/Cf; fm = ff·sqrt(2/(2 + n)); abs(Zo)mm = R0f·sqrt(2(2 + n))/n; Qopt = Rf/R0f = sqrt((2 + n)(4 + 3n)/(2n^2·(4 + n))); required n = (R0f^2/abs(Zo)mm^2)·(1 + sqrt(1 + 4·abs(Zo)mm^2/R0f^2)); ff = 1/(2π·sqrt(Lf·Cf)), R0f = sqrt(Lf/Cf) | Lf, Cf, abs(Zo)mm target | Single section, Fig.17.23a; HF attenuation unaffected by Cb | calc | §17.4.1 Eq.(17.33)–(17.38) p.694–696 | high (Zmm and n forms verified against the book's n = 2.5, Rf = 0.67 Ω) |
| ERICKSON-2068 | filter | Worked optimal Rf–Cb design (regression anchor) | Lf = 330 μH, Cf = 470 μF, R0f = 0.84 Ω, target abs(Zo)mm = 1 Ω → n = 2.5, Cb = n·Cf ≈ 1200 μF (¼ of the ad-hoc 4700 μF), Rf = 0.67 Ω; peak at fm slightly below ff | — | Buck input filter example | calc | §17.4.1 Eq.(17.37)–(17.38), Fig.17.25 p.695–696 | high |
| ERICKSON-2069 | filter | Rf–Cb damping lets Cb be an electrolytic/tantalum (its ESR is in series with Rf); Rf–Lb schemes can be smaller; large Cb is undesirable with ac input | — | capacitor technology, input type | Input filter damping selection | review | §17.4.1 p.696 | high |
| ERICKSON-2070 | filter | Optimal Rf–Lb parallel damping (Rf in series with Lb, both across Lf): cheap (Lb small, carries ~no dc; Rf can be Lb's ESR at ff) but degrades HF attenuation | n = Lb/Lf; Qopt = Rf/R0f = sqrt(n(3 + 4n)(1 + 2n)/(2(1 + 4n))); fm = ff·sqrt((1 + 2n)/(2n)); abs(Zo)mm = R0f·sqrt(2n(1 + 2n)); HF attenuation degraded by Lf/(Lf∥Lb) = 1 + 1/n; e.g. 6 dB degradation (n = 1) → abs(Zo)mm = sqrt(6)·R0f; n = 0.5 → 9.5 dB loss, abs(Zo)mm = sqrt(2)·R0f; n = 0.516 → Qopt = 0.93 | Lf, Cf, Lb | Single section, Fig.17.23b | calc | §17.4.2 Eq.(17.39)–(17.43), Figs.17.24, 17.26 p.694–698 | high |
| ERICKSON-2071 | filter | Optimal Rf–Lb series damping (Rf in series with Lf, bypass Lb across Rf): HF attenuation unaffected, but both inductors carry full dc; peak impedance cannot go below sqrt(2)·R0f (then redesign Lf, Cf to lower R0f) | fm = ff·sqrt((2 + n)/(2(1 + n))); abs(Zo)mm = R0f·sqrt(2(1 + n)(2 + n))/n; Qopt = R0f/Rf = ((1 + n)/n)·sqrt(2(1 + n)(4 + n)/((2 + n)(4 + 3n))); abs(Zo)mm ≥ sqrt(2)·R0f | Lf, Cf, Lb (n = Lb/Lf assumed) | Single section, Fig.17.23c | calc | §17.4.3 Eq.(17.44)–(17.46) p.698 | medium (radicals and n definition reconstructed from OCR; limit sqrt(2)·R0f stated) |
| ERICKSON-2072 | filter | Cascaded filter sections: adding a section (output impedance Za) ahead of an existing filter leaves its output impedance unchanged if Za is well below the existing filter's input impedance with output shorted (ZN1) and open (ZD1); stagger-tune (section nearest the converter has the lower resonance and gives more attenuation) | Zo' = Zo·(1 + Za/ZN1)/(1 + Za/ZD1); require abs(Za) << abs(ZN1), abs(Za) << abs(ZD1) | Za, ZN1, ZD1 | Multi-section input filters (smaller total L, C than single stage) | calc | §17.4.4 Eq.(17.47)–(17.50) p.699–700 | high |
| ERICKSON-2073 | filter | Section resonance from required HF attenuation of a 2-pole section with Rf–Lb damping | ff = f_spec / sqrt(A), A = required attenuation (ratio) at f_spec including the (1 + 1/n) damping penalty; L = R0f/(2π·ff); C = 1/(2π·ff·R0f); R0f = abs(Zo)mm/sqrt(2n(1 + 2n)) | f_spec, A, n, abs(Zo)mm | −40 dB/decade sections | calc | §17.4.5 Eq.(17.51)–(17.58) p.700–703 | high |
| ERICKSON-2074 | filter | Worked two-stage input filter (80 dB at 250 kHz, buck example; regression anchor) | Section 1 (converter side): 45 dB + 9.5 dB = 54.5 dB (533×) → ff1 = 10.8 kHz, abs(Zo)mm = 3 Ω, n = 0.5 → R0f1 = 2.12 Ω, L1 = 31.2 μH, C1 = 6.9 μF, n1·L1 = 15.6 μH, R1 = 1.9 Ω, peak at 15.3 kHz. Section 2: 35 dB + 9.5 dB = 44.5 dB (169×) → ff2 = 19.25 kHz, peak 27.2 kHz, Za mm = 1 Ω → R0f2 = 0.71 Ω, L2 = 5.8 μH, C2 = 11.7 μF, n2·L2 = 2.9 μH, R2 = 0.65 Ω; overall peak Zo ≈ 10 dBΩ (≈3 Ω), no resonances; single-stage equivalent needs Lf = 330 μH, Cf = 470 μF, Cb = 1200 μF, Rf = 0.67 Ω | — | Buck input filter | sim | §17.4.5 Figs.17.28–17.32 p.700–705 | high |
| ERICKSON-2075 | control-loop | Impedance inequalities are conservative design criteria, not the stability boundary: stability must be judged on the modified loop gain T' (with Gvd'), or on the minor loop gain Tm = Zo/Zi with Nyquist (multiple crossovers possible) | Stable example: Lf = 31 μH, Cf = 47 μF, Rf = 1.7 Ω, Cb = 29 μF (filter resonance ≈4 kHz, output filter 1 kHz): three crossovers, PM reduced but positive. Unstable: Rf = 5.2 Ω, Cb = 8 μF → Zo exceeds ZN, ZD at 4 kHz, extra −360°, negative PM at fc = 7 kHz | T', Tm | Closed-loop regulator + input filter (buck of §9.5.4) | sim | §17.5.1 Figs.17.34–17.39 p.706–710 | high |
| ERICKSON-2076 | control-loop | Closed-loop input impedance Zi follows ZN (negative, −R/M^2, phase −180°) where T is large and ZD (passive) where T is small; Zi has an RHP pole at fnd (not itself unstable) and may dip below ZN, ZD near fc; closed-loop audiosusceptibility with filter = Hi·Gvg/(1 + Zo/Zi) | Yi = Yi∞·T/(1 + T) + Yi0/(1 + T); Yi∞ = −j/e (buck: −M^2/R); Yi0 = M^2/Zei | T, ZN, ZD | CCM voltage-mode regulators | calc | §17.5.2 Eq.(17.60)–(17.76), Fig.17.45 p.711–718 | high |
| ERICKSON-2077 | control-loop | Minor-loop stability with an Rf-damped input filter: Tm peaks at Rf·M^2/R at ff; keeping Rf/(R/M^2) < 1 (damping resistance below the negative input resistance magnitude) removes Nyquist encirclements of −1 | abs(Tm(ff)) = Rf·M^2/R < 1 | Rf, M, R | Input filter with resistive damping, well-regulated converter | calc | §17.5.2 Figs.17.46–17.48 p.718–720 | high |
| ERICKSON-2078 | control-loop | Current-programmed (peak current-mode, CPM) control: removes the inductor pole from the control-to-output response (pole moves near fs), so wide-bandwidth voltage loops need no lead network; limiting the control signal ic gives cycle-by-cycle transistor current limiting | Pmax protection: clamp ic(max) so switch turns off whenever is ≥ ic(max) | ic clamp, switch rating | CPM controllers (buck, boost, buck–boost, isolated) | review | Ch.18 intro p.725–726 | high |
| ERICKSON-2079 | control-loop | CPM in full-bridge/push-pull isolated converters corrects volt-second imbalance (transformer dc bias) automatically; do NOT put a dc-blocking capacitor in series with the primary of a CPM full bridge (destabilizes); avoid CPM for half-bridge isolated buck | — | topology | Transformer-isolated CPM converters | review | Ch.18 intro p.726–727 | high |
| ERICKSON-2080 | control-loop | CPM noise susceptibility: lightly filter the sensed switch current to remove the diode-recovery turn-on spike and use a leading-edge blanking interval; blanking sets a minimum achievable duty cycle | Dmin ≥ t_blank/Ts | t_blank, Ts | CPM controllers | review | Ch.18 intro p.727 | high (formula: medium) |
| ERICKSON-2081 | control-loop | CPM inductor-current slopes (for ramp and model design) | Buck: m1 = (vg − v)/L, m2 = v/L. Boost: m1 = vg/L, m2 = (v − vg)/L. Buck–boost: m1 = vg/L, m2 = −v/L (magnitude abs(v)/L). Steady state: M2/M1 = D/D' | vg, v, L | CCM | calc | §18.2 Eq.(18.30), (18.35) p.738–739 | high |
| ERICKSON-2082 | control-loop | Subharmonic (period-doubling) instability of CPM without slope compensation for D > 0.5, independent of topology | Perturbation per cycle: îL(nTs) = îL(0)·α^n, α = −D/D'; stable iff abs(α) < 1 ⇔ D < 0.5. Example boost Vg = 20 V: V = 50 V → D = 0.6, α = −1.5 (−1.5, +2.25, −3.375 × îL(0)); V = 30 V → D = 1/3, α = −0.5 | D | CCM peak-current control, no ramp | calc | §18.2 Eq.(18.40)–(18.47), Figs.18.17–18.18 p.740–742 | high |
| ERICKSON-2083 | control-loop | Slope compensation (artificial ramp ma added to sensed current): stability condition and characteristic value | α = −(m2 − ma)/(m1 + ma) = −(1 − ma/m2)/(D'/D + ma/m2); stable iff abs(α) < 1 | m1, m2, ma, D | CCM CPM | calc | §18.2 Eq.(18.52)–(18.56) p.742–744 | high |
| ERICKSON-2084 | control-loop | Slope-compensation design values: ma = m2/2 is the minimum giving stability for all 0 ≤ D < 1 (α = −1 at D = 1) and also nulls the buck line-to-output gain; ma = m2 gives α = 0 (deadbeat: perturbation removed in one period); use m2 at the regulated output (known V) | ma ≥ 0.5·m2 (general); ma = m2 (deadbeat) | m2 | Buck/buck–boost voltage regulators (m2 = V/L known) | calc | §18.2 Eq.(18.57)–(18.58) p.744–745; Key pt 2 p.798 | high |
| ERICKSON-2085 | control-loop | Noise: without a ramp and with small current ripple, small noise in ic or is gives large duty jitter (high modulator gain); with poor layout/grounding, use a ramp amplitude substantially greater than the inductor ripple | ma·Ts >> ripple when noise significant (qualitative) | noise level, ripple | CPM controllers | measure | §18.2 Fig.18.22 p.745–746 | low |
| ERICKSON-2086 | control-loop | Simple CPM model (iL ≈ ic): buck is a current source into the output (Gvc = R ∥ 1/(sC), Gvg = 0), input port is a power sink with negative incremental resistance −R/D^2; CPM keeps transfer-function zeros (boost/buck–boost RHP zero unchanged), removes one pole, dc gains become load-dependent | Buck: Gvc = R/(1 + sRC). Boost: Gvc = (D'R/2)(1 − sL/(D'^2·R))/(1 + sRC/2); Gvg = (1/(2D'))/(1 + sRC/2). Buck–boost: Gvc = −(D'R/(1 + D))(1 − sDL/(D'^2·R))/(1 + sRC/(1 + D)); Gvg = −(D^2/(1 − D^2))/(1 + sRC/(1 + D)); Zout = (R/(1 + D))/(1 + sRC/(1 + D)) | D, R, L, C | Small ripple, stable current loop | calc | §18.1 Eq.(18.11)–(18.15), (18.28)–(18.29), Tables 18.1, 18.3–18.5 p.732–760 | high |
| ERICKSON-2087 | control-loop | Simple CPM two-port parameters (Table 18.1) | Buck: g1 = D/R, f1 = D(1 + sL/R), r1 = −R/D^2, g2 = 0, f2 = 1, r2 = ∞. Boost: g1 = 0, f1 = 1, r1 = ∞, g2 = 1/(D'R), f2 = D'(1 − sL/(D'^2·R)), r2 = R | D, R, L | CCM, simple model | calc | §18.1 Table 18.1 p.732 | high (buck–boost row not transcribed: OCR ambiguous) |
| ERICKSON-2088 | control-loop | Accurate CPM relation between average inductor current and control (Tan–Middlebrook, trapezoidal averaging at the modulating edge) | <iL> = ic − ma·d·Ts − (m1 + m2)·d·d'·Ts/2 | ic, ma, m1, m2, d, Ts | CCM CPM | calc | §18.3.1 Eq.(18.63)–(18.67) p.747–748 | high |
| ERICKSON-2089 | control-loop | Accurate CPM small-signal controller gains (Table 18.2) | d̂ = Fm(îc − îL − Fg·v̂g − Fv·v̂); Fm = 1/((Ma + (M1 − M2)/2)·Ts); Buck: Fg = D·D'·Ts/(2L), Fv = 0; Boost: Fg = 0, Fv = D·D'·Ts/(2L); Buck–boost: Fg = D·D'·Ts/(2L), Fv = −D·D'·Ts/(2L). Ma ≥ M2/2 gives finite positive Fm for any D; Ma = 0 → Fm → ∞ at D = 0.5, negative (positive feedback) for D > 0.5 | Ma, M1, M2, D, L, Ts | CCM CPM | calc | §18.3.2 Eq.(18.73)–(18.74), Table 18.2 p.749; §18.4.1 p.754 | high |
| ERICKSON-2090 | control-loop | CPM transfer functions from duty-cycle transfer functions (general single-inductor CCM) | Ti = Fm(Gid + Fv·Gvd); Gvc = Fm·Gvd/(1 + Ti); Gvg−cpm = (Gvg − Fm·Fg·Gvd + Fm(Gvg·Gid − Gig·Gvd))/(1 + Ti); limits: Fm → ∞ gives Gvd/Gid; small Fm (large ramp) degenerates to duty control Fm·Gvd | Gvd, Gid, Gvg, Gig, Fm, Fg, Fv | CCM CPM | calc | §18.4 Eq.(18.79)–(18.96) p.753–755 | high |
| ERICKSON-2091 | control-loop | CPM buck accurate control-to-output (two low-Q poles) and line rejection | Gc0 = (V/D)·Fm/(1 + Fm·V/(D·R)); ωc = (1/sqrt(LC))·sqrt(1 + Fm·V/(D·R)); Qc = R·sqrt(C/L)·sqrt(1 + Fm·V/(D·R))/(1 + R·C·Fm·V/(D·L)); fp1 = Qc·fc ≈ 1/(2πRC) (large Fm); fhf = fc/Qc ≈ Fm·V/(2π·D·L); Gg0 = D·(1 − Fm·Fg·V/D^2)/(1 + Fm·V/(D·R)) = D·((2Ma − M2)/(2Ma + M1 − M2))/(1 + Fm·V/(D·R)) → 0 at Ma = M2/2 | V, D, R, L, C, Fm, Fg, Ma | CCM CPM buck | calc | §18.4.2 Eq.(18.106)–(18.119), Table 18.3 p.756–759 | high |
| ERICKSON-2092 | control-loop | CPM current-loop high-frequency pole (averaged model = 1st-order Padé of sampled-data model) | fhf = (fs/π)·(M1 + M2)/(2Ma + M1 − M2) = (fs/π)/(1 + 2D(Ma/M2 − 1)) = ((1 − α)/(1 + α))·fs/π; typically near or above fs | fs, D, Ma/M2 | CCM CPM | calc | §18.4.2 Eq.(18.114); §18.7.1–18.7.2 Eq.(18.157)–(18.171) p.757–777 | high |
| ERICKSON-2093 | control-loop | Sampled-data CPM control-to-current response and its 2nd-order approximation (predicts fs/2 peaking and instability) | Gic(z) = (1 − α)/(1 − α·z^−1); Gic(s) = ((1 − α)/(1 − α·e^(−sTs)))·(1 − e^(−sTs))/(s·Ts); 2nd order: Gic ≈ 1/(1 + s/(Qhf·ωs/2) + (s/(ωs/2))^2), ωs/2 = π·fs, Qhf = (2/π)(1 − α)/(1 + α) = (2/π)/(1 − 2D + 2D·Ma/M2); Qhf → ∞ at α = −1 (stability boundary) | α, D, Ma/M2, fs | CCM CPM | calc | §18.7.1, §18.7.3 Eq.(18.165)–(18.175) p.775–778 | high |
| ERICKSON-2094 | control-loop | Extend the averaged CPM model to capture fs/2 dynamics by giving Fm a pole | Fm → Fm/(1 + s/ωx), fx = (π^2/4)·(1 − 2D + 2D·Ma/M2)·fs | D, Ma/M2, fs | CCM CPM small-signal/simulation models | calc | §18.7.3 Eq.(18.176)–(18.177) p.779 | medium (exponent on π lost in OCR; re-derived by matching Eq.(18.173)) |
| ERICKSON-2095 | control-loop | Sampled-data example: small ramp gives current-loop peaking near fs/2; large ramp lowers current-loop bandwidth; 1st-order (averaged) model is valid to ≈ fs/5 at Ma = 0.5·M2 and fails for small ramps | Buck fs = 100 kHz, D = 0.5, Vg = 10 V, V = 5 V, L = 5 μH, M1 = M2 = 1 A/μs: Ma/M2 = 0.1 → α = −0.82, peaking at 50 kHz, 1st-order pole predicted at 3.2·fs (poor); Ma = 0 → infinite peak at fs/2; Ma/M2 = 5 → roll-off at lower frequency | Ma/M2 | CCM CPM | sim | §18.7.1–18.7.2 Figs.18.42–18.43 p.776–778 | high |
| ERICKSON-2096 | control-loop | CPM buck with input filter: ZN−cpm = −R/D^2 and, for practical ramps (Ma = M2/2 exactly, or large Fm), ZD−cpm ≈ −R/D^2 too — the input filter output impedance must stay well below R/D^2 at all frequencies; very large Ma makes ZD−cpm revert to the duty-control ZD | abs(Zo) << R/D^2 (all f); Fm·Fg·D·Vg = D^2 at Ma = M2/2 | R, D, Ma | CCM CPM buck + input filter | calc | §18.4.4 Eq.(18.120)–(18.134) p.760–763 | high |
| ERICKSON-2097 | control-loop | Closed-loop input admittance of a CPM converter with outer voltage loop Tv (for input-filter / source-impedance stability via Tm = Zo/Zi) | Yi = (1/ZN−cpm)·Tv/(1 + Tv) + (1/ZD−cpm)/(1 + Tv) | Tv, ZN−cpm, ZD−cpm | CPM regulators on non-ideal sources | calc | §18.6.1 Eq.(18.147) p.770 | high |
| ERICKSON-2098 | control-loop | SPICE averaged CPM subcircuit equations (CCM and combined CCM/DCM) | CCM: d = 2(<vc> − Rf·<iL>)/((Rf/(L·fs))·(<v1> + <v2>)·d' + 2Va); Va = ma·Ts·Rf; m1 = <v1>/L, m2 = <v2>/L. CCM/DCM: d2 = min(1 − d, ipk/(m2·Ts)); d = 2(<vc>·(d + d2) − Rf·<iL>)/((Rf/(L·fs))·(<v1> + <v2>)·d2·(d + d2) + 2Va·(d + d2)) | vc, Rf, iL, v1, v2, L, fs, Va | Use with CCM-DCM1 averaged switch | sim | §18.5.1–18.5.2 Eq.(18.135)–(18.145) p.764–766 | high (CCM/DCM form: medium, OCR-flattened) |
| ERICKSON-2099 | control-loop | CPM vs duty control (simulation example): CPM Gvc single dominant pole (≈−90° over a wide band) vs high-Q LC pair; CPM line rejection > 30 dB better; CPM output impedance higher at low frequency (R ∥ CPM output resistance) but without LC peaking, same HF asymptote | Buck Vg = 12 V, L = 35 μH, RL = 0.05 Ω, C = 100 μF, R = 10 Ω, fs = 200 kHz, Rf = 1 Ω, Va = 0.6 V, Vc = 1.4 V → D = 0.676, V = 8.1 V, IL = 0.81 A | — | CCM CPM buck | sim | §18.5.3 Figs.18.32–18.35 p.766–769 | high |
| ERICKSON-2100 | control-loop | Outer voltage loop around CPM converter: PI compensator suffices; gain for crossover fcv and phase margin | Tv = H·Gcv·Gvc/Rf; Gcv = Gcm(1 + ωzv/s); Gcm = Rf·fcv/(H·Gc0·fp1); φv = tan^−1(fcv/fzv) − tan^−1(fcv/fhf) (fp1 << fcv) | Rf, H, Gc0, fp1, fhf, fcv, fzv | CCM CPM with fzv < fcv < fhf | calc | §18.6.2 Eq.(18.146)–(18.153) p.770–772 | high |
| ERICKSON-2101 | control-loop | Worked CPM voltage-loop design (regression anchor) | Vref = 3 V, H = 0.375 (V = 8 V), D = 0.67, IL = 0.8 A, Ma/M2 = 0.525, Fm = 3.2 A^−1, Fg = 0.016 Ω^−1, Fv = 0 → Gc0 = 7.92 Ω (18 dBΩ), fc = 5.9 kHz, Qc = 0.034, fp1 = 201 Hz, fhf = 174 kHz; fcv = 40 kHz = fs/5 → Gcm = 67.1; fzv = fcv/3 → φv = 72° − 13° = 59° | — | CPM buck of Fig.18.32 | calc | §18.6.2 Eq.(18.148)–(18.153) p.770–772 | high |
| ERICKSON-2102 | control-loop | CPM in DCM: transistor port = power sink, diode port = power source; no subharmonic instability (current starts at zero), but DCM CPM buck with ma = 0 has a low-frequency instability for M > 2/3 (two equilibria with resistive load); fix with ma > 0.086·m2 or voltage feedback | ic = (m1 + ma)·d1·Ts; P = (1/2)·L·ic^2·fs/(1 + ma/m1)^2; buck–boost V = Ic·sqrt(R·L·fs/2)/(1 + Ma/M1); stable ranges with ma = 0: buck 0 ≤ M < 2/3, boost and buck–boost 0 ≤ D ≤ 1 | L, ic, fs, ma, m1, M | DCM CPM | calc | §18.8 Eq.(18.178)–(18.194), Table 18.6 p.780–784 | high |
| ERICKSON-2103 | control-loop | CPM DCM steady-state conversion and CCM/DCM boundary (Table 18.6) | Buck: M = (Pload − P)/Pload, Icrit = (1/2)(Ic − M·ma·Ts). Boost: M = Pload/(Pload − P), Icrit = (1/(2M))·(Ic − ((M − 1)/M)·ma·Ts). Buck–boost: Pload = P (depends on load). CCM if abs(I) > abs(Icrit) | P, Pload, Ic, ma, Ts, M | CPM, resistive load | calc | §18.8 Eq.(18.195), Table 18.6 p.784 | high (buck) / medium (boost Icrit re-derived; OCR garbled) |
| ERICKSON-2104 | control-loop | Average current-mode (ACM) control: PI(+pole) current loop around a duty-controlled converter; stable at any duty cycle without slope compensation, better noise immunity, direct average-current control (chargers, LED drivers, PFC, grid inverters), but clamping vc limits only AVERAGE current — add separate cycle-by-cycle peak-current protection | Ti = Rf·Gci·Gid/VM; Gic = (1/Rf)·Ti/(1 + Ti); Gvc (inner loop closed) = (Gvd/(Rf·Gid))·Ti/(1 + Ti) ≈ Gvd/(Rf·Gid) for f << fci; Tv = H·Gcv·Gvc | Rf, Gci, VM, Gid, Gvd | ACM controlled converters | calc | §18.9 Eq.(18.198)–(18.204) p.786–790 | high |
| ERICKSON-2105 | control-loop | ACM current-loop compensator design | Gci = Gcm(1 + ωz/s)/(1 + s/ωp); HF asymptote of uncompensated loop (boost) abs(Tiu) = Rf·V/(L·ω·VM) → Gcm = L·ωci·VM/(Rf·V); φm = tan^−1(fci/fz) − tan^−1(fci/fp); fz < fci < fp (example fz = fci/2.5, fp = 2.5·fci → 46°) | L, V, VM, Rf, fci | ACM boost (similar for others) | calc | §18.9.2 Eq.(18.208)–(18.213) p.793–794 | high |
| ERICKSON-2106 | control-loop | Worked ACM boost PFC-class design (regression anchor) | Vg = 170 V, V = 400 V, Pout = 2 kW (R = 80 Ω), fs = 100 kHz, VM = 4 V, Rf = 0.25 Ω, Vref = 3 V, H = 0.0075; D = 0.575, I = 11.8 A, Vc = 2.94 V; Gid0 = 2V/(D'^2·R) = 55.4 A (34.9 dBA), fzi = 1/(πRC) = 121 Hz, fo = D'/(2π·sqrt(LC)) = 745 Hz, Q = D'R·sqrt(C/L) = 12.4; Tiu0 = 3.46 (10.8 dB); fci = 10 kHz (fs/10): Gcm = 0.63, fz = 4 kHz, fp = 25 kHz, φm = 46°; voltage loop fcv = 1 kHz: Gvc ≈ (D'R/(2Rf))(1 − s/ωzRHP)/(1 + s/ωzi), fzRHP = D'^2·R/(2πL) = 9.2 kHz, Gvm = 2π·fcv·C·Rf/(D'·H) = 16.4, fzv = fcv/3 = 333 Hz, φmv ≈ 72°; implied L ≈ 250 μH, C ≈ 33 μF | — | ACM boost | calc | §18.9.2 Eq.(18.205)–(18.218) p.791–797 | high (L, C back-computed: medium) |
| ERICKSON-2107 | control-loop | Design the ACM two-loop system inner loop first (fci ≈ fs/10), then outer voltage loop well below (fcv << fci, e.g. fci/10) using the inner-closed Gvc | fcv << fci << fs | fs, fci, fcv | Cascaded current/voltage loops | review | §18.9.1–18.9.2 p.790–797 | high |
| ERICKSON-2108 | hw-fw | Digital control loop: sample the A/D synchronously with switching (usually once per period, fsampling = fs); only frequencies up to the Nyquist frequency fs/2 are meaningful; content above fs/2 aliases | fsampling = k·fs, typical k = 1 | fs | Digitally controlled SMPS | review | §19.1 Eq.(19.1); §19.1.2 p.806–811 | high |
| ERICKSON-2109 | hw-fw | A/D resolution needed for a dc regulation tolerance: the zero-error bin width qA/D sets how well V is regulated | qA/D = VFS/2^nA/D; need qA/D < 2·(allowed ± error at the A/D input, i.e. H·ΔV); nA/D > log2(VFS/qA/D). Example ±0.25% of Vref = 1 V (±2.5 mV) → qA/D < 5 mV; VFS = 2 V → nA/D ≥ 9 bits | VFS, H, tolerance | Digital voltage-mode regulators; "window" A/Ds centred on Vref reduce bits needed | calc | §19.1.1 Eq.(19.2)–(19.3) p.807 | high |
| ERICKSON-2110 | hw-fw | DPWM resolution needed for output-voltage positioning, and counter-based clock requirement | qDPWM = 1/2^nDPWM; qDPWM·Ts = Tclk; buck ΔV = qDPWM·Vg; ΔV/V = 1/(2^nDPWM·M). Example 0.1% with M = 0.2 → 13 bits → fclk = 2^13·fs = 8192·fs; fs = 1 MHz → 122 ps, 8.192 GHz (use delay-line/hybrid DPWM or ΔΣ instead) | nDPWM, M, fs | Counter-based DPWM; general M(D) needs dV/dD | calc | §19.1.1 Eq.(19.4)–(19.8) p.808–809 | high |
| ERICKSON-2111 | hw-fw | Counter-based DPWM bits available from a given clock (derived from Eq.19.5) | nDPWM = floor(log2(fclk/fs)); e.g. fclk = 120 MHz: fs = 100 kHz → 10 bits, 250 kHz → 8 bits, 1 MHz → 6 bits | fclk, fs | Trailing-edge counter DPWM (Problem 19.1 setting) | calc | §19.1.1 Eq.(19.5); Problem 19.1 p.838 | medium |
| ERICKSON-2112 | hw-fw | Sampling the output voltage (with switching ripple) once per period gives a dc regulation error ≤ ripple amplitude (aliasing); sample away from switching transitions; add analog anti-alias LPF or oversample and filter digitally | abs(Ve − ve[n]) ≤ ripple amplitude | ripple, sampling instant | Digital loops sampling at fs | review | §19.1.2 p.810–811 | high |
| ERICKSON-2113 | control-loop | Digital loop delay and its phase penalty (magnitude unaffected) | td = tctrl + tmod; tmod = D·Ts (trailing-edge), (1 − D)·Ts (leading-edge), Ts/2 (dual-edge); ∠Gdelay = −ω·td (rad) = −360°·f·td | tctrl, D, Ts, fc | Regularly sampled DPWM (Table 19.1) | calc | §19.1.2 Eq.(19.11)–(19.14), Table 19.1 p.811–812 | high |
| ERICKSON-2114 | control-loop | Delay budget example: fs = 1 MHz buck, fc = 100 kHz, analog PM 52° → td = 0.36 μs (D·Ts, tctrl ≈ 0): PM 39°; td = 0.86 μs (tctrl = Ts/2): PM 21°; td = 1.36 μs (tctrl = Ts): PM 3° — include td in the design and add phase lead | PM_digital = PM_analog − 360°·fc·td | fc, td | Wide-bandwidth digital loops | calc | §19.3 Fig.19.10 p.822–823 | high |
| ERICKSON-2115 | firmware | Discrete-time integrators (coefficients for firmware) | Trapezoidal: vc[n] = vc[n − 1] + ωo·Ts·(ve[n] + ve[n − 1])/2, Gcd = (ωo·Ts/2)(z + 1)/(z − 1) (exact −90° phase; magnitude ≈ analog for f << fs/π; zero magnitude at fs/2, 3fs/2 …). Backward Euler: vc[n] = vc[n − 1] + ωo·Ts·ve[n − 1], Gcd = ωo·Ts/(z − 1). Forward Euler: vc[n] = vc[n − 1] + ωo·Ts·ve[n], Gcd = ωo·Ts·z/(z − 1) | ωo, Ts | Digital PI/PID integral term | calc | §19.2.1–19.2.2 Eq.(19.19)–(19.33), Table 19.2 p.813–816 | high |
| ERICKSON-2116 | firmware | Continuous-to-discrete compensator mapping: bilinear (Tustin), with prewarp at the crossover to preserve fc and phase margin; MATLAB c2d(Gc,Ts,'tustin') / c2d(Gc,Ts,'prewarp',wprewarp) | s → (2/Ts)(z − 1)/(z + 1); prewarp: s → kprewarp·(2/Ts)(z − 1)/(z + 1), kprewarp = (ωpw·Ts/2)/tan(ωpw·Ts/2); fprewarp = fc | Gc(s), Ts, fc | Digital compensator design; jω axis → unit circle, s = 0 → z = 1 | calc | §19.2.3 Eq.(19.35)–(19.49), Table 19.3 p.817–821; §19.3.1 Eq.(19.59) p.824 | high |
| ERICKSON-2117 | firmware | Low-frequency analog poles/zeros map close to z = 1 (roundoff/word-length sensitivity) | PI: Gcd ≈ Gc∞·(z − (1 − ωL·Ts))/(z − 1) for ωL·Ts/2 << 1; example Gc∞ = 1, fL = 20 kHz, fs = 1 MHz → Gcd = 1.063(z − 0.8743)/(z − 1); PD example Gc0 = 1, fz = 100 kHz, fp = 400 kHz, fs = 1 MHz → 2.329(z − 0.5219)/(z + 0.1137) (phase error near fs/2 → use prewarp at sqrt(fz·fp) = 200 kHz) | fL, fs | Fixed-point implementations | calc | §19.2.3 Eq.(19.40)–(19.45) p.818–819 | high |
| ERICKSON-2118 | firmware | Digital PID from analog PID (Gcm, fL, fz, fp1) via prewarped bilinear map | Gcd(z) = Gd(z − zL)(z − zz)/((z − 1)(z − zp)); a = tan(π·fpw/fs); zL = (1 − a·fL/fpw)/(1 + a·fL/fpw); zz = (1 − a·fz/fpw)/(1 + a·fz/fpw); zp = (1 − a·fp1/fpw)/(1 + a·fp1/fpw); Gd = Gcm·(fp1/fz)·(1 + a·fL/fpw)(1 + a·fz/fpw)/(1 + a·fp1/fpw) | Gcm, fL, fz, fp1, fpw, fs | Drop the analog HF pole fp2 from Gc; put it in the analog anti-alias filter H(s) | calc | §19.2.3 Eq.(19.50)–(19.54) p.820–821 | high (Gd verified: book's 27.3898 with Gcm = 5.2375 from its script) |
| ERICKSON-2119 | firmware | Choosing fp1 = fpw/tan(π·fpw/fs) makes zp = 0 and gives the textbook KP/KI/KD form; parallel-form gains from the cascade form | Gcd = KP + KI/(1 − z^−1) + KD(1 − z^−1)/(1 − zp·z^−1); KI = Gd(1 − zL)(1 − zz)/(1 − zp); KD = Gd(zL − zp)(zz − zp)/(1 − zp)^2; KP = Gd(zL + zz − zp − (2 − zp)·zL·zz)/(1 − zp)^2; KI = lim(z→1)(z − 1)·Gcd(z) | Gd, zL, zz, zp | Digital PID realization | calc | §19.4.1 Eq.(19.65)–(19.69), (19.80) p.829–835 | high (KP denominator re-derived; lost in OCR) |
| ERICKSON-2120 | firmware | Difference equations for firmware/HDL, with anti-windup limiter on the integrator (clamp vc to the DPWM range, 0–1 for VM = 1) and word lengths chosen to avoid overflow | Cascade: u1 = Gd·ve[n]; u2 = u1 − zL·u1[n−1]; u3 = u2 − zz·u2[n−1]; u4 = u3 + zp·u4[n−1]; vc[n] = u4 + vc[n−1] (limited). Parallel: up = KP·ve; ui = KI·ve + ui[n−1] (limited); ud1 = KD(ve − ve[n−1]); ud = ud1 + zp·ud[n−1]; vc = up + ui + ud | coefficients | Digital PID | review | §19.4.1 Eq.(19.64), (19.67), Figs.19.14–19.15 p.828–829 | high |
| ERICKSON-2121 | control-loop | Digital compensator design procedure: (1) Tud = H·Gvd·e^(−s·td) with anti-alias pole in H; (2) analog design without HF roll-off poles, adding extra lead equal to 360°·fc·td; (3) map with prewarp at fc; (4) verify Td(jω) = H·Gvd·e^(−s·td)·Gcd(e^(jωTs)) (no ZOH term); (5) realize | Worked: Vg = 5 V, V = 1.8 V, L = 1 μH (Rs = 30 mΩ), C = 200 μF (Resr = 0.8 mΩ), fs = 1 MHz, 0–5 A: Gd0 = 5 V, fesr = 1 MHz, f0 = 11.3 kHz, Q = 2.3; fc = 100 kHz, PM 52°; td = 0.36 μs adds −13° → lead 65°: fL = 8 kHz, fz = 22 kHz, fp1 = 450 kHz, Gcm = sqrt(fz/fp1)·(fc/f0)^2/Vg = 3.5 V^−1 → Gcd = 31.7593(z − 0.9493)(z − 0.8654)/((z − 1)(z + 0.1881)); H pole fp2 = 1 MHz | — | Digital voltage-mode buck (POL) | sim | §19.3.1–19.3.2 Eq.(19.55)–(19.63), Figs.19.11–19.13 p.822–827 | high |
| ERICKSON-2122 | hw-fw | No-limit-cycle necessary conditions (integral action required): DPWM step seen at the A/D input smaller than one A/D LSB, and integral gain bounded | Gd0·H0·qDPWM < qA/D; 0 < KI < 1/(Gd0·H0); Gd0 = dc control-to-output gain (buck: Vg). Example (Vg = 5 V, H0 = 1): qA/D = 4 mV with 10-bit DPWM → Vg·H0·qDPWM = 4.9 mV > 4 mV → limit cycling; 12-bit → 1.2 mV → settles; limit-cycle amplitude ≈ qA/D | Gd0, H0, qDPWM, qA/D, KI | Digitally controlled converters; conditions necessary, not sufficient | calc | §19.4.2 Eq.(19.70)–(19.80), Figs.19.16–19.20 p.830–836 | high |
| ERICKSON-2123 | hw-fw | Raising effective DPWM resolution: delay-line or hybrid DPWM avoids GHz clocks; 2nd-order error-feedback ΔΣ between compensator and DPWM adds ≈6–7 bits for a 7–10-bit hardware DPWM (better with dual-edge DPWM); window-flash A/D around Vref (3 levels with 2 comparators) suffices in some loops | n_eff ≈ nDPWM + 6…7 bits (ΔΣ) | nDPWM, fs | High-frequency digital PWM | review | §19.4.2 Fig.19.21 p.836–838 | high |
| ERICKSON-2124 | compliance | Average power in nonsinusoidal systems flows only at frequencies present in BOTH voltage and current | Pav = V0·I0 + Σn (Vn·In/2)·cos(φn − θn) (Vn, In peak amplitudes). Example v = 1.2cos(ωt) + 0.33cos(3ωt) + 0.2cos(5ωt), i = 0.6cos(ωt + 30°) + 0.1cos(5ωt + 45°) + 0.1cos(7ωt + 60°) → Pav = 0.32 | Fourier coefficients of v, i | Periodic waveforms (per phase for balanced 3-phase) | calc | §20.1 Eq.(20.6)–(20.9) p.851–853 | high |
| ERICKSON-2125 | compliance | RMS from Fourier components: harmonics always raise rms (series I^2·R loss) without adding power when the voltage is sinusoidal | rms = sqrt(V0^2 + Σn Vn^2/2); series loss = Irms^2·Rseries; shunt loss = Vrms^2/Rshunt | Fourier coefficients | Any periodic waveform | calc | §20.2 Eq.(20.10)–(20.14) p.853 | high |
| ERICKSON-2126 | compliance | Power factor = P/(Vrms·Irms); with a sinusoidal voltage it factors into distortion factor × displacement factor; distortion factor from THD | PF = P/(Vrms·Irms); PF = DF·cos(φ1 − θ1); DF = I1,rms/Irms = 1/sqrt(1 + THD^2) (no dc); THD = sqrt(Σn≥2 In^2)/I1; examples: 10% third harmonic → DF = 99.5%, 20% → 98%, 33% → 95%; resistive (Ohm's-law) load → PF = 1 for any voltage harmonics | I1, In, φ1 − θ1 | Single-phase or per-phase | calc | §20.3 Eq.(20.15)–(20.26), Fig.20.5 p.854–856 | high |
| ERICKSON-2127 | compliance | Conventional capacitor-input (peak-detection) rectifier line current: DF typically 55–65% (PF similar), large low-order harmonics | Typical spectrum (% of fundamental): h3 91, h5 73, h7 52, h9 32, h11 19, h13 15, h15 15, h17 13, h19 9; THD = 136%, DF = 59% | — | Single-phase peak-detection rectifier | measure | §20.3.2 Figs.20.6–20.7 p.856–857 | high (spectrum: graph values) |
| ERICKSON-2128 | compliance | Available dc power from a branch circuit is limited by PF: size PFC vs peak-detection front ends against the outlet rating | Pdc = Vac·(0.8·Ibreaker)·PF·η; 120 V / 15 A outlet, 80% breaker derating: PF 0.55, η 0.98 → 776 W; PF 0.99, η 0.93 → 1325 W | Vac, Ibreaker, PF, η | Plug-in equipment (North American 120 V / 15 A example) | calc | §20.3.2 Eq.(20.27)–(20.28) p.857 | high |
| ERICKSON-2129 | compliance | Apparent power (VA = Vrms·Irms) rates transformers etc.; complex power and PF for purely sinusoidal waveforms only | S = V·I* = P + jQ; abs(S) = Vrms·Irms (VA); PF = P/abs(S) = cos(φ1 − θ1) only when both v and i are sinusoidal | V, I phasors | Sinusoidal systems | calc | §20.4 Eq.(20.29)–(20.30) p.858 | high |
| ERICKSON-2130 | compliance | Three-phase four-wire: for balanced nonlinear loads the dc and triplen harmonics add in the neutral (others cancel) — neutral conductor can be overloaded | in,rms = 3·sqrt(I0^2 + Σk=3,6,9… Ik^2/2); example 20% third harmonic → neutral rms = 0.6·I1/sqrt(2) = 60% of line rms (line rms ≈ I1/sqrt(2)·sqrt(1.04)) | Ik per phase | Balanced loads, 4-wire wye | calc | §20.5.1 Eq.(20.33)–(20.36) p.859–861 | high |
| ERICKSON-2131 | compliance | Three-phase three-wire (wye without neutral, or delta): balanced loads cannot draw triplen or dc line currents (a neutral-shift voltage appears; in delta, triplen currents circulate inside the delta); unbalanced loads can | Line current triplen = 0 (balanced) | load balance | 3-wire systems | review | §20.5.2 p.861–862 | high |
| ERICKSON-2132 | components | Power-factor-correction (and filter) capacitors absorb harmonic currents (their impedance falls with f); rms current rises without a voltage increase → ESR heating, premature aging/failure; verify capacitor rms current rating includes harmonics | Nameplate: Vrms = Irms/(2π·f·C), kVAR = Irms^2/(2π·f·C) (sinusoidal); loss = Irms^2·ESR with Irms = sqrt(Σ In,rms^2) | C, ESR, harmonic currents | AC-side capacitors | calc | §20.5.3 Eq.(20.37)–(20.38) p.862–863 | high |
| ERICKSON-2133 | power | Ideal (unity-PF) rectifier = loss-free resistor: ac port emulates Re, dc port is a power source; Re must vary slowly vs the line (fast Re changes create harmonics) | iac = vac/Re; Pav = Vac,rms^2/Re = VM^2/(2Re); dc-side current i(t) = (VM^2/(2V·Re))(1 − cos 2ωt), I = VM^2/(2V·Re); resistive load: Vrms = Vac,rms·sqrt(R/Re) | VM, Re, V | Single-phase PFC rectifiers, any topology | calc | §21.1–21.2 Eq.(21.1)–(21.17) p.868–872 | high |
| ERICKSON-2134 | power | Boost PFC requirements and CCM/DCM boundary along the line cycle | V ≥ VM; d(t) = 1 − vg(t)/V (CCM); CCM at instant t if Re < 2L/(Ts·(1 − vg(t)/V)); CCM over the whole cycle if Re < 2L/Ts; DCM over the whole cycle if Re > 2L/(Ts·(1 − VM/V)); normalized: CCM if jg > mg(1 − mg), mg = vg/V, jg = 2L·ig/(V·Ts) (boundary max 0.25 at mg = 0.5) | Re, L, Ts, V, VM | Boost PFC | calc | §21.2.1 Eq.(21.18)–(21.34), Fig.21.6 p.872–875 | high |
| ERICKSON-2135 | power | Open-loop DCM boost PFC (constant d) is only an approximate resistor emulator: harmonic content set by (1 − vg/V); keep V well above VM and design L so DCM holds at max power; overload into CCM near the peak gives current spikes | L < (1 − VM/V)·Re/(2fs), Re = VM^2/(2P); example 120 Vrms 50 Hz (VM = 170 V), V = 300 V, P ≤ 120 W, fs = 100 kHz → L < 260 μH, chosen 200 μH (C = 150 μF): at 100 W h3 = 16.6%, THD = 16.7%, 2f ripple ≈ 8 V p-p; overload 180 W (R = 500 Ω) → CCM near peak, THD = 71% | L, V, VM, P, fs | DCM boost PFC | sim | §21.2.2 Eq.(21.35)–(21.37), Figs.21.8–21.11 p.876–878 | high |
| ERICKSON-2136 | power | DCM flyback (also buck–boost, SEPIC, Ćuk) at constant d and fs is a natural loss-free resistor → simple low-power PFC with inherent inrush limiting and isolation; must stay DCM at max power and minimum line | Re = 2n^2·L/(D^2·Ts) (Fig.21.13; n:1 = primary:secondary, L consistent with secondary-referred magnetizing inductance); DCM if D < 1/(1 + VM/(n·V)); D = (2nV/VM)·sqrt(L/(R·Ts)); L < Lcrit−min = Rmin·Ts/(4(1 + nV/VM−min)^2) | n, L, Ts, Rmin, VM−min, V | DCM flyback PFC with input EMI filter (pulsating input current, high peak currents) | calc | §21.2.3 Eq.(21.38)–(21.44) p.878–880 | high (L referral inferred from Eq.21.42 consistency: medium) |
| ERICKSON-2137 | power | Average current control with multiplier: emulated resistance and power set by vcontrol; with input-voltage feedforward (kv·x·y/z^2, z = peak VM) power becomes independent of line amplitude (peak-detector ripple adds some line-current distortion) | Re = Rs/(kx·vcontrol); vref1 = kv·vcontrol·vg/VM^2 → Pav = kv·vcontrol/(2Rs) | Rs, kx, kv, vcontrol | Average-current-mode PFC (CCM or DCM; avoids CPM crossover distortion) | calc | §21.3.1 Eq.(21.45)–(21.53), Figs.21.14–21.18 p.881–885 | high |
| ERICKSON-2138 | control-loop | Boost PFC current-loop plant is linear even with large line-frequency variation (as long as v̂ << V); other topologies (buck–boost, SEPIC, Ćuk) are nonlinear/time-varying and quasi-static design is not guaranteed | ig(s) = (V/(sL))·d(s) + (1/(sL))·vg(s) | V, L | Inner current loop design of PFC | calc | §21.3.1 Eq.(21.54)–(21.59) p.885–886 | high |
| ERICKSON-2139 | power | CPM boost PFC: minimum stabilizing ramp and distortion; to keep THD low operate deep in CCM (Re << Rbase = 2L/Ts) and use no more ramp than needed; narrow-range designs reach 5–10% THD, universal-input CPM 20–50% at maximum line unless the reference is biased | ma(min) = V/(2L); CCM <ig> = ic − (1 − vg/V)(ma + vg/(2L))·Ts; CCM if ic > (Ts·V/L)(ma·L/V + vg/V)(1 − vg/V) | V, L, Ts, Re, ma | CPM boost PFC | calc | §21.3.2 Eq.(21.60)–(21.64), Figs.21.21–21.22 p.886–889 | high (CCM <ig> form re-derived; OCR garbled) |
| ERICKSON-2140 | power | Critical-conduction-mode (boundary, constant on-time) boost PFC: natural resistor emulation, popular below several hundred watts; switching frequency varies over the line cycle — size L and V for an acceptable fs range; higher peak current and more EMI filtering | Re = 2L/ton; ton = 4L·P/VM^2; fs(t) = (VM^2/(4L·P))(1 − (VM/V)·abs(sin ωt)); fs,max = VM^2/(4L·P) (zero crossing); fs,min = (VM^2/(4L·P))(1 − VM/V) (line peak) | L, P, VM, V | CrM boost PFC | calc | §21.3.3 Eq.(21.65)–(21.73) p.889–892 | high |
| ERICKSON-2141 | power | Nonlinear-carrier (NLC) charge control of CCM boost PFC: senses only switch current (current transformer), no multiplier, no input V/I sensing, no slope compensation; crossover distortion only in DCM near zero crossings (less than CPM) — feasible for universal input | Parabolic carrier vc(t) = vcontrol·(t/Ts)(1 − t/Ts); Re = <v>/(n·Ci·fs·vcontrol) | n, Ci, fs, vcontrol | CCM boost PFC | calc | §21.3.4 Eq.(21.74)–(21.84) p.892–894 | high |
| ERICKSON-2142 | power | Single-phase PFC needs a bulk energy-storage capacitor whose voltage is allowed to vary (second-harmonic power); size its 2f ripple and the hold-up requirement | pac(t) = (VM^2/(2Re))(1 − cos 2ωt); 2ΔvC(p-p) ≈ Pload/(ω·C·VC,rms) (ω = line rad/s); exact vC(t) = VC,rms·sqrt(1 − (Pload/(ω·C·VC,rms^2))·sin 2ωt); hold-up: typically one missing line cycle (20 ms at 50 Hz), C must keep vC above the dc–dc converter's minimum input at the end | Pload, C, VC, f_line | Single-phase PFC + dc–dc systems | calc | §21.4.1 Eq.(21.85)–(21.94) p.895–900 | high |
| ERICKSON-2143 | power | Boost PFC cannot limit start-up inrush into the bulk capacitor (diode conducts while v < vg even at d = 0): add inrush-limiting circuitry; buck–boost-type PFCs limit inrush at the cost of higher switch stress | — | topology | PFC front ends | review | §21.4.1 p.897; §21.5.2 p.908 | high |
| ERICKSON-2144 | control-loop | Outer (bulk-voltage) loop must have small gain at 2×line frequency (low bandwidth); fast outer loops distort the line current (limit: THD → ∞, PF → 0 for perfectly constant vC) | Loop gain at 2f_line << 1 | T_outer(2f_line) | PFC voltage loop | sim | §21.4.1 Eq.(21.89), Fig.21.32 p.898–899; §21.4.2 p.900 | high (numeric margin: low) |
| ERICKSON-2145 | control-loop | PFC outer-loop small-signal model (averaged over half line period): single pole | v̂/v̂control = j2·(R∥r2)/(1 + sC(R∥r2)); v̂/v̂g,rms = g2·(R∥r2)/(1 + sC(R∥r2)). Table 21.1: ACC + feedforward g2 = 0, j2 = Pav/(V·Vcontrol), r2 = V^2/Pav; CPM g2 = 2Pav/(V·Vg,rms), j2 = Pav/(V·Vcontrol), r2 = V^2/Pav; NLC boost g2 = 2Pav/(V·Vg,rms), j2 = Pav/(V·Vcontrol), r2 = V^2/(2Pav); CrM boost g2 = 2Pav/(V·Vg,rms), j2 = Pav/(V·ton), r2 = V^2/Pav; DCM buck–boost/flyback/SEPIC/Ćuk g2 = 2Pav/(V·Vg,rms), j2 = 2Pav/(V·D), r2 = V^2/Pav | Pav, V, Vg,rms, Vcontrol, C, R | Frequencies well below line frequency | calc | §21.4.2 Eq.(21.95)–(21.106), Table 21.1 p.900–904 | high |
| ERICKSON-2146 | control-loop | With a downstream regulated dc–dc converter (constant-power load, R = −V^2/Pav) the PFC voltage-loop plant becomes an integrator (R∥r2 → open) for all controllers except NLC | v̂/v̂control = j2/(sC); v̂/v̂g,rms = g2/(sC) | j2, g2, C | PFC + dc–dc systems | calc | §21.4.2 Eq.(21.107)–(21.109) p.904–905 | high |
| ERICKSON-2147 | power | RMS of PWM-rectifier waveforms by double averaging (switching period, then line period); sin^n integrals | Irms^2 = <<i^2>Ts>Tac; (1/π)∫0..π sin^n θ dθ = 2/π (n = 1), 1/2 (2), 4/(3π) (3), 3/8 (4), 16/(15π) (5), 15/48 (6) | waveform | fs >> f_line | calc | §21.5 Eq.(21.110)–(21.121), Table 21.2 p.905–907 | high |
| ERICKSON-2148 | power | CCM boost PFC current stresses (ripple neglected); transistor rms is minimized with V as close as possible to VM (0.39·Iac,rms at V = VM) | IQrms = Iac,rms·sqrt(1 − (8/(3π))·VM/V); IDrms = Iac,rms·sqrt((8/(3π))·VM/V) (0.92·Iac,rms at V = VM); IQav = Iac,rms·(2sqrt2/π)(1 − π·VM/(8V)); IDav = Idc = Iac,rms·VM/(sqrt2·V); inductor rms = Iac,rms, avg = (2sqrt2/π)·Iac,rms; peak (L, Q, D) = sqrt2·Iac,rms | Iac,rms, VM, V | CCM boost PFC | calc | §21.5.1 Eq.(21.122)–(21.126), Table 21.3 p.907–909 | high |
| ERICKSON-2149 | power | CCM SEPIC / flyback PFC stresses (higher than boost; buy inrush control and V < VM) | Nonisolated SEPIC: IQrms = Iac,rms·sqrt(1 + (8/(3π))VM/V), IC1,rms = Iac,rms·sqrt((8/(3π))VM/V), IL2,rms = Iac,rms·(VM/V)·sqrt(3/2), IDrms = Idc·sqrt(3/2 + (16/(3π))V/VM); peaks: Q sqrt2·Iac,rms(1 + VM/V), D 2Idc(1 + V/VM), switch voltage VM + V. Flyback (n:1, input L1–C1): IQrms = Iac,rms·sqrt(1 + (8/(3π))VM/(nV)), IC1,rms = Iac,rms·sqrt((8/(3π))VM/(nV)), IDrms = Idc·sqrt(3/2 + (16/(3π))nV/VM); Iac,rms/Idc = sqrt2·V/VM | Iac,rms, Idc, VM, V, n | CCM, ripple neglected | calc | §21.5 Table 21.3 p.909 | high |
| ERICKSON-2150 | power | Worked PFC topology comparison (1 kW, 240 Vrms in, 380 V out; regression anchor) | Boost: Iac,rms = 4.2 A, IQrms = 2 A, IDrms = 3.6 A, blocking 380 V; at 120 Vrms: 6.6 A, 5.1 A. Nonisolated SEPIC: IQrms = 5.5 A, peak switch voltage 719 V, IDrms = 4.85 A; at 120 V: 9.8 A, 6.1 A. Isolated SEPIC 42 V/23.8 A, 4:1: transformer rms 5.5 A pri / 36.4 A sec, transistor 6.9 A; at 120 V: 7.7 A, 42.5 A, 11.4 A | — | Single-phase PFC topology selection | calc | §21.5.2 p.908–910 | high |
| ERICKSON-2151 | power | CCM boost PFC efficiency including MOSFET Ron (conduction loss only) | d(t) = (V − vg)/(V − vg·Ron/Re); η = (1 − Ron/Re)·F(a), a = (VM/V)(Ron/Re); F(a) = (2/(π·a^2))·(−2a − π + (4·asin(a) + 2·acos(a))/sqrt(1 − a^2)) ≈ 1 + 0.862a + 0.78a^2 (within 0.1% for abs(a) ≤ 0.15; ±2% without a^2 term); 90–95% achievable even with Ron = 0.2·Re when VM ≈ V | Ron, Re, VM, V | CCM boost PFC; DCM near zero crossings and dynamics neglected | calc | §21.6 Eq.(21.127)–(21.146), Figs.21.40–21.41 p.910–916 | high (F(a) grouping verified by small-a expansion) |
| ERICKSON-2152 | power | Worked PFC MOSFET selection for efficiency (regression anchor) | 390 V, 500 W, 120 Vrms, η = 95% (MOSFET loss only): Pin = 526 W, Re = Vg,rms^2/Pin = 27.4 Ω, VM/V = 0.435 → Ron/Re ≈ 0.077 → Ron ≤ 2.11 Ω; rms shortcut: Iac,rms = 4.38 A, IQrms = 3.48 A → Ron ≤ (Pin − Pout)/IQrms^2 ≈ 2.17 Ω | — | CCM boost PFC | calc | §21.6.4 Eq.(21.147)–(21.152) p.916–917 | high (book's Eq.21.152 prints 4.38 A in the denominator; 2.17 Ω follows from IQrms = 3.48 A) |
| ERICKSON-2153 | power | Three-phase ideal rectifier delivers constant instantaneous power (no bulk low-frequency storage needed); six-switch boost rectifier needs V above the peak line-to-line voltage | ptot = (3/2)·VM^2/Re (constant); sinusoidal PWM d = D0 + (Dm/2)·sin(ωt − φ − k·120°): V = 2VM/Dm = (2/sqrt3)·VL,pk/Dm = 1.15·VL,pk/Dm, Dm ≤ 1 → V ≥ 1.15·VL,pk; triplen-injection modulation allows V = VL,pk (effective index 1.15) | VM, VL,pk, Dm | 3-phase boost (VSI-type) rectifier; non-pulsating input currents, bidirectional power | calc | §21.7 Eq.(21.153)–(21.164), Fig.21.46 p.917–922 | high |
| ERICKSON-2154 | power | Active harmonic corrector (six-switch bridge in parallel with a nonlinear load) needs less silicon than a full PWM rectifier only when load THD is moderate; if the diode rectifier runs in DCM with large THD, replace it with the CCM boost rectifier | kVA(corrector) ∝ load harmonic currents | load THD | 3-phase harmonic mitigation | review | §21.7 Fig.21.47 p.922 | high (qualitative) |
| ERICKSON-2155 | compliance | Universal-input rectifier ac range to design for | 100 Vrms (Japan) to 260 Vrms (Western Australia), 50 or 60 Hz; problem specs use 90–270 Vrms | Vac range | Worldwide single-phase products | review | §21.4.1 p.897; Problems 21.5, 21.10 p.925–927 | high |
| ERICKSON-2156 | power | Resonant converter trade-off: ZVS/ZCS cuts switching loss (allows higher fs; ZVS also removes device-capacitance ringing EMI) but tanks are hard to optimize over wide load/line ranges, circulating currents hurt light-load efficiency, and quasi-sinusoidal peaks raise conduction and tank-inductor loss | — | load range, Vin range | Choosing resonant vs PWM | review | Ch.22 intro p.936 | high |
| ERICKSON-2157 | power | Sinusoidal (first-harmonic) approximation of the square-wave bridge | vs1 peak = (4/π)·Vg; dc input current Ig = (2/π)·Is1·cos(φs) | Vg, Is1, φs | Tank Q high and fs near resonance; inaccurate at low Q or near/in DCM | calc | §22.1.1 Eq.(22.1)–(22.4) p.938–939 | high |
| ERICKSON-2158 | power | Rectifier + capacitive output filter (series-type) loads the tank with Re; conversion ratio = tank transfer magnitude | Re = (8/π^2)·R = 0.8106·R; VR1 = (4/π)·V; I = (2/π)·IR1; M = V/Vg = abs(H(jωs)) (H evaluated with Re) | R, H(jω) | Series resonant and similar dc–dc converters, 1:1 transformer | calc | §22.1.2–22.1.4 Eq.(22.8)–(22.16) p.940–943 | high |
| ERICKSON-2159 | power | Series resonant converter (SRC) conversion ratio (first harmonic): M ≤ 1, equals 1 at resonance, peakier at heavy load (higher Qe) | M = 1/sqrt(1 + Qe^2·(1/F − F)^2); F = fs/f0; f0 = 1/(2π·sqrt(LC)); R0 = sqrt(L/C); Qe = R0/Re | L, C, R, fs | Valid above resonance and just below; fails for fs << f0 (e.g. fs = f0/3 excites the tank with the 3rd harmonic) and at low Q | calc | §22.2.1 Eq.(22.17)–(22.19) p.944–946 | high |
| ERICKSON-2160 | power | SRC subharmonic modes: when n·fs ≈ f0 (n odd) the tank rings at the nth harmonic; avoid (lower output/efficiency, risk of large-signal instability) | M ≈ abs(H(j·n·ωs))/n (n·fs near f0, high Qe) | n, fs, f0 | SRC below resonance | calc | §22.2.2 Eq.(22.20)–(22.21), Fig.22.18 p.946–947 | high |
| ERICKSON-2161 | power | Parallel resonant converter (PRC, inductive output filter): step-up or step-down; at resonance M = R/R0; ideal output current limited below Vg/R0 | Re = (π^2/8)·R = 1.2337·R; VR1 = (π/2)·V; M = (8/π^2)·abs(H(jωs)) = (8/π^2)/sqrt((1 − F^2)^2 + (F/Qe)^2), Qe = Re/R0; peak M slightly below f0 | L, C, R, fs | PRC, first-harmonic approximation | calc | §22.2.3 Eq.(22.22)–(22.32) p.947–950 | high |
| ERICKSON-2162 | power | ZCS (below resonance, capacitive tank, conduction sequence Q1–D1–Q2–D2): turn-off lossless but turn-on is hard (diode reverse recovery + Coss energy lost) → little benefit for MOSFETs; useful for IGBT tail loss and SCR commutation | — | fs vs f0 | Bridge resonant converters | review | §22.3.1 p.951–954; Key pt 5 p.988 | high |
| ERICKSON-2163 | power | ZVS (above resonance, inductive tank, sequence D1–Q1–D2–Q2): turn-on lossless (slow body diodes OK, no Qrr or Coss loss); add dead time and leg capacitance (MOSFET Coss usually sufficient; IGBTs need substantial external C) so turn-off is also near-lossless | Transistor gated on while its antiparallel diode conducts; dead time long enough for is(Ts/2) to swing the leg capacitance to the opposite rail | dead time, Cleg, is at switching | Preferred for MOSFET/diode converters (Key pt 4) | review | §22.3.2 Fig.22.29 p.954–956 | high |
| ERICKSON-2164 | power | Resonant inverter output characteristic is an ellipse; matched load gives maximum power | (V/Voc)^2 + (I/Isc)^2 = 1; Voc = abs(H∞)·Vs1; Isc = Voc/abs(Zo0); matched load R = abs(Zo0) → V = Voc/sqrt2, I = Isc/sqrt2 | H∞, Zo0, Vs1 | Lossless (purely reactive) tank; also dc–dc with Re | calc | §22.4.1 Eq.(22.33)–(22.44), Fig.22.32 p.958–960 | high |
| ERICKSON-2165 | power | Transistor current vs load (Theorem 22.1): abs(Zi) varies monotonically between Zi0 (load shorted) and Zi∞ (load open); for good light-load efficiency operate where abs(Zi∞) > abs(Zi0) (fs < fm for parallel/LCC tanks); SRC has Zi∞ = ∞ so switch current tracks load | abs(Zi)^2 = abs(Zi0)^2·(1 + R^2/abs(Zo0)^2)/(1 + R^2/abs(Zo∞)^2); fm where abs(Zi0) = abs(Zi∞) (Xs = −Xp/2) | Zi0, Zi∞, fs | Lossless tanks | calc | §22.4.2 Eq.(22.45)–(22.49), Figs.22.33–22.36 p.960–964 | high |
| ERICKSON-2166 | power | ZVS/ZCS boundary (Theorem 22.2): ZVS if Zi inductive; if Zi0 and Zi∞ are both inductive → ZVS for all loads; both capacitive → ZCS for all loads; mixed → boundary at Rcrit; ZVS at matched load needs abs(Zi∞) > abs(Zi0) when ZVS at short-circuit and ZCS at open-circuit | Rcrit = abs(Zo0)·sqrt(−Zi∞/Zi0) = sqrt(abs(Zo0·Zo∞)) = abs(Xp)·sqrt(−Xs/(Xs + Xp)) | Xs, Xp (tank branch reactances) | Ignores device output capacitance (necessary, not sufficient, for ZVS) | calc | §22.4.3 Eq.(22.53)–(22.59), (22.83); Key pt 7 p.965–975, 988 | high (book's case list 1–4 has sign typos; rule follows the ZVS = inductive definition) |
| ERICKSON-2167 | power | LCC tank characteristic frequencies and ZVS regions | f0 = 1/(2π·sqrt(L·Cs)) (short-circuit); f∞ = 1/(2π·sqrt(L·(Cs∥Cp))) (open; Cs∥Cp = Cs·Cp/(Cs + Cp)); fm = 1/(2π·sqrt(L·(Cs∥2Cp))); fs < f0: ZCS all loads; fs > f∞: ZVS all loads; f0 < fs < f∞: ZVS for R < Rcrit; Rcrit = abs(Zo0) at fm; design window f0 < fs < fm (ZVS at matched/short, low circulating current, ZVS lost at light load) | L, Cs, Cp | LCC inverters/converters | calc | §22.4.2–22.4.3 Eq.(22.50)–(22.52), Fig.22.38 p.963–967 | high |
| ERICKSON-2168 | power | LCC tank synthesis from output-ellipse specs | H∞ = Voc/Vs1; Isc = I/sqrt(1 − (V/Voc)^2); abs(Zo0) = Voc/Isc; jXp = Zo0/(1 − H∞) → Cp = (H∞ − 1)/(ωs·abs(Zo0)); Xs = Xp(1 − H∞)/H∞; L = (Xs + 1/(ωs·Cs))/ωs (Cs free); Rcrit = abs(Zo0)/sqrt(abs(1 − H∞)) | Vg, Voc, V, I, fs | LCC with purely reactive tank | calc | §22.4.4 Eq.(22.60)–(22.72) p.967–971 | high |
| ERICKSON-2169 | power | Worked LCC inverter design (regression anchor) | fs = 100 kHz, Vg = 160 V, Voc = 400 V pk, nominal 150 Vrms at 25 W: H∞ = 1.96; V = 212 V, I = 0.236 A, Rnom = 900 Ω; Isc = 0.278 A; Vmat = 283 V, Imat = 0.196 A, abs(Zo0) = 1439 Ω; Xp ≈ −1493…−1499 Ω → Cp ≈ 1.06 nF; Xs = 733 Ω; Cs → ∞: L = 1.17 mH; Cs = Cp: L = 3.5 mH; Cs = 3Cp = 3.2 nF: L = 1.96 mH, f∞ = 127 kHz, fm = 100.6 kHz, f0 = 64 kHz; Rcrit = 1466 Ω (ZVS at 900 Ω); Zi∞ = −j760 Ω → open-circuit Is1 = 0.268 A; short-circuit Is1 = 0.278 A | — | LCC inverter | calc | §22.4.4 Eq.(22.60)–(22.76) p.967–971 | high (book prints "1.96 μH" and "Cp = 1 nF"; values recomputed: 1.96 mH, 1.06 nF) |
| ERICKSON-2170 | power | LLC tank (series C, Ls; shunt Lp, often transformer leakage/magnetizing; C also blocks dc for transformer volt-second balance): frequency regions | f0 = 1/(2π·sqrt(Ls·C)) (short-circuit) > f∞ = 1/(2π·sqrt((Ls + Lp)·C)) (open); fs < f∞: ZCS all loads; fs > f0: ZVS all loads and tank current scales with load (M < 1, SRC-like); f∞ < fs < f0: ZVS at light load (R > Rcrit), ZCS at heavy load; Rcrit = Ro0·(n·F/sqrt(1 + n))·sqrt((1 − F^2/(1 + n))/(F^2 − 1)), Ro0 = sqrt(Ls/C), n = Lp/Ls, F = fs/f∞; near f∞ boost-type gain, large at light load; fs > fm: tank current falls with load | Ls, Lp, C, fs | LLC dc–dc (off-line adapters) | calc | §22.4.5 Eq.(22.77)–(22.80), Figs.22.40–22.44 p.972–975 | high (Rcrit form re-derived from Eq.(22.83)) |
| ERICKSON-2171 | power | General first-harmonic solution for series/parallel/LCC/LLC tanks via branch reactances (Table 22.1) | Series: Xs = ωL − 1/(ωC), Xp = ∞; Parallel: Xs = ωL, Xp = −1/(ωC); LCC: Xs = ωL − 1/(ωCs), Xp = −1/(ωCp); LLC: Xs = ωLs − 1/(ωC), Xp = ωLp. H∞ = Xp/(Xp + Xs); Zo0 = j·Xs·Xp/(Xs + Xp) = j·Xs·H∞; output ellipse (M/a)^2 + (J/b)^2 = 1 with M = Vout/Vin, J = Iout·R0/Vin, a = abs(H∞), b = R0/abs(Xs); control characteristic M = 1/sqrt(1/a^2 + (Qe/b)^2), Qe = R0/Re (series tank: a = 1) | L, C values, fs, Re | All four basic tanks | calc | §22.4.6 Eq.(22.81)–(22.86), Table 22.1 p.973–976 | high |
| ERICKSON-2172 | power | Exact SRC (transformer 1:n): mode index and bounds | k: f0/(k + 1) < fs < f0/k; ξ = k + (1 + (−1)^k)/2; M = V/(n·Vg), J = I·n·R0/Vg, γ = ω0·Ts/2 = π/F; CCM ellipse M^2·ξ^2·sin^2(γ/2) + (1/ξ^2)(J·γ/2 + (−1)^k)^2·cos^2(γ/2) = 1; 0 ≤ M ≤ 1/ξ; mode test: k = INT(1/F), k1 = INT(1/2 + sqrt(1/4 + Q·π/(2F))), Q = n^2·R0/R; CCM if k1 > k else type-k1 DCM | F, Q, n | Ideal SRC, state-plane exact results | calc | §22.5.1 Eq.(22.87)–(22.93), (22.100)–(22.102) p.977–982 | high (CCM ellipse: medium, OCR-flattened) |
| ERICKSON-2173 | power | SRC discontinuous modes: odd k DCM gives M = 1/k (uncontrollable; unloaded SRC below resonance sits in k = 1 DCM with M = 1); even k DCM is a current source (gyrator) J = 2k/γ for 1/(k + 1) < M < 1/(k − 1); only k = 0 CCM exists above resonance (M falls monotonically with fs, rises at light load); below resonance only k = 1 CCM and k = 2 DCM are well behaved — avoid higher modes | Odd-k DCM range 2(k − 1)/γ < J < 2(k + 1)/γ; k = 2 DCM used at tens of kW | F, J, M | Ideal SRC | calc | §22.5.1 Eq.(22.94)–(22.99), Figs.22.47–22.53 p.979–983 | high |
| ERICKSON-2174 | power | Exact PRC characteristics: CCM output nearly elliptical; at F = 1 current source J = 1; above resonance J < 1 (I < Vg/(n·R0)); DCM (all rectifiers conducting, tank C clamped to 0) at heavy load | CCM: M = (2/γ)(φ − sin(φ)/cos(γ/2)), φ = ∓acos(cos(γ/2) + J·sin(γ/2)) (− above, + below resonance); DCM if J > Jcrit(γ) = −(1/2)·sin(γ) + sqrt(sin^2(γ/2) + (1/4)·sin^2(γ)); Q = R/(n^2·R0), J = M/Q | γ = π/F, J | Ideal PRC, F > 0.5 | calc | §22.5.2 Eq.(22.103)–(22.107), Figs.22.56–22.57 p.983–988 | medium (OCR-flattened; Jcrit(π) = 1 consistency-checked) |
| ERICKSON-2175 | power | Soft switching trades switching loss for conduction loss (resonant elements need large ripple): evaluate total efficiency, not just switching loss | Compare Psw saved vs added conduction/tank loss | loss budget | All soft-switching choices | calc | Ch.23 intro p.995 | high (qualitative) |
| ERICKSON-2176 | power | Diode turn-off switching energy: hard switching and ZCS both lose ≈ Vg·Qr (ZCS: energy parked in the series inductor, later dissipated; lower Qr from reduced di/dt); ZCS also raises diode peak inverse voltage (Lr–Cj ringing); ZVS diode turn-off has negligible loss and needs no snubber — preferred | Hard: WD = Vg·Qr + tr·Vg·I (lost in transistor); ZCS: WD = Vg·Qr | Vg, Qr, tr, I | Diode reverse recovery | calc | §23.1.1 Eq.(23.1)–(23.2) p.996–999 | high |
| ERICKSON-2177 | protection | R–C snubber across a ringing diode (series L with diode Cj, e.g. transformer leakage + secondary rectifier): R damps, C blocks the off-state dc; snubber dissipation per cycle typically exceeds WD | — | L, Cj | Hard-switched/ZCS rectifiers | measure | §23.1.1 Fig.23.3 p.999 | high (qualitative) |
| ERICKSON-2178 | power | Hard-switched MOSFET: turn-off near-lossless with a fast gate driver (Cds holds v ≈ 0); dominant losses are at turn-on (diode recovery + Coss energy); ZCS does not remove Coss loss (little benefit for MOSFETs); ZVS removes both and makes the body diode ZVS (improves reliability); for IGBTs ZVS removes diode-recovery loss but tail loss remains | — | device type | Switch-loss mechanism review | review | §23.1.2–23.1.3 p.1000–1003 | high |
| ERICKSON-2179 | protection | Dissipative RCD voltage-clamp snubber for flyback leakage inductance: size Rs from the leakage energy at the desired clamp voltage (Cs large); MOSFET peak = Vg + Vs (ideal reflected value D·Vg/D' otherwise exceeded by Ll–Cds ringing) | Vs^2/Rs ≈ (1/2)·Ll·i^2·fs (i = primary current at turn-off) → Rs ≈ 2·Vs^2/(Ll·i^2·fs); Vds,pk = Vg + Vs | Ll, i, fs, Vs | First-estimate design of flyback clamp | calc | §23.1.2 Eq.(23.3), Fig.23.6 p.1001–1002 | high |
| ERICKSON-2180 | power | Half-wave ZCS quasi-resonant switch: μ replaces d in CCM PWM formulas (buck M = μ, boost M = 1/(1 − μ)); ZCS requires Js ≤ 1; μ depends strongly on load (via Js) | f0 = 1/(2π·sqrt(Lr·Cr)) > fs; R0 = sqrt(Lr/Cr); Js = I2·R0/V1; F = fs/f0; μ = F·P½(Js), P½(Js) = (1/(2π))·(Js/2 + π + asin(Js) + (1 + sqrt(1 − Js^2))/Js); max-F limit μ ≤ 1 − Js·F/(4π); buck: ZCS for I ≤ Vg/R0, 0 ≤ V ≤ Vg − F·I·R0/(4π); boost: Js = Ig·R0/V, Ig = I/(1 − μ) | Lr, Cr, fs, V1, I2 | ZCS QRS, filter ripple small | calc | §23.2.1–23.2.2 Eq.(23.4)–(23.54) p.1003–1014 | high |
| ERICKSON-2181 | power | ZCS QRS subinterval anchors (for waveform/stress checks) | α = Js (rad, ω0·t); peak tank/transistor current I1pk = I2 + V1/R0 (≥ 2·I2 since Js ≤ 1); β = π + asin(Js) (half-wave) or 2π − asin(Js) (full-wave); Vc1 = V1(1 + sqrt(1 − Js^2)) (half) or V1(1 − sqrt(1 − Js^2)) (full); δ = Vc1/(I2·R0); switching-period limit 2π/F ≥ α + β + δ | Js, V1, I2, R0 | ZCS QRS | calc | §23.2.1 Eq.(23.13)–(23.31), (23.55)–(23.56) p.1006–1014 | high |
| ERICKSON-2182 | power | Full-wave ZCS QRS: μ ≈ F (voltage-source-like, nearly load independent → small fs range for regulation) but poor light-load efficiency (circulating tank current) and D1 recovered-charge ringing | μ = F·P1(Js), P1(Js) = (1/(2π))(Js/2 + 2π − asin(Js) + (1 − sqrt(1 − Js^2))/Js) within 4% of 1 (→ 0.96 as Js → 1) | F, Js | ZCS QRS, full wave | calc | §23.2.3 Eq.(23.57)–(23.60) p.1014–1015 | high |
| ERICKSON-2183 | power | ZCS QRS device stresses and suitability: D2 switches ZVS (good), Q1/D1 ZCS (fine for SCR/IGBT; poor for MOSFETs: Coss loss); peak transistor voltage = V1 (as PWM); half-wave adds series-diode drop | I1pk ≥ 2·I2; Vpk = V1 | — | ZCS QRS selection | review | §23.3 p.1016–1017 | high |
| ERICKSON-2184 | power | Identify a resonant-switch type: open all low-frequency filter inductors, short all dc sources and filter capacitors; the remaining network classifies the cell (ZCS QRS, ZVS QRS, MRS, QSW) | — | schematic | Topology review | inspect | §23.3 p.1016; Figs.23.22–23.28 | high |
| ERICKSON-2185 | power | ZVS quasi-resonant switch: Q1/D1 ZVS, D2 ZCS; ZVS only at heavy load (Js ≥ 1); transistor voltage stress rises with load | Half-wave μ = 1 − F·P½(1/Js); full-wave μ = 1 − F·P1(1/Js); ZVS if Js ≥ 1; Vpk = (1 + Js)·V1 (5:1 load range → 2× to 6× V1); Ipk = I2 | Js, V1, F | ZVS QRS (higher Vds rating → higher Ron) | calc | §23.3.1 Eq.(23.61)–(23.64) p.1017–1018 | high |
| ERICKSON-2186 | power | ZVS multiresonant switch (Cs across switch, Cd across diode, Lr): all devices ZVS, low EMI; typical 5:1 load design | Design point: 0.4 ≤ μ ≤ 0.6, F(max) = 1.0, J(max) = 1.4, Cd/Cs = 3 → Vpk ≈ 2.8·V1, Ipk ≈ 2·I2; smaller Cd/Cs shrinks the ZVS region; f0 = 1/(2π·sqrt(L·Ct)), R0 = sqrt(L/Ct), J = I2·R0/V1 (Ct = the MRS tank capacitance symbol of Eq.23.65, not defined further in the text) | Cd/Cs, F, J | ZVS MRS | calc | §23.3.2 Eq.(23.65), Fig.23.27 p.1019–1020 | high |
| ERICKSON-2187 | power | Quasi-square-wave switches: ZCS-QSW keeps PWM peak current but raises peak voltage (0 ≤ μ ≤ 0.5); ZVS-QSW keeps PWM peak voltage, all devices ZVS, higher peak current (inductor current reverses), ZVS only for 0.5 ≤ μ ≤ 1 (single switch); a synchronous-rectifier version runs constant frequency with μ ≈ D and ZVS toward μ → 0 (e.g. F = 0.5) | f0 = 1/(2π·sqrt(Lr·Cr)), R0 = sqrt(Lr/Cr), F = fs/f0, J = I2·R0/V1 | μ, F, J | QSW buck/VRM-type converters | review | §23.3.3 Figs.23.28–23.35 p.1020–1025 | high |
| ERICKSON-2188 | power | Phase-shifted ZVT full bridge: conversion ratio and ZVS conditions | M = V/Vg = n·φ, φ = (t1 − t0)/(Ts/2) (transitions neglected); active-to-passive leg (Q3/Q4) always ZVS (ic = nI; dv/dt = nI/(2Cleg)); passive-to-active leg (Q1/Q2) ZVS only if Lc stores enough energy: (1/2)·Lc·ic^2 ≥ (1/2)(Cleg1 + Cleg2)·Vg^2, typically lost at light load (remedy: larger magnetizing current); ic reverses at slope Vg/Lc between −nI and +nI (no power transfer: effective duty loss ≈ 2nI·Lc/Vg per half period) | n, Lc, Cleg, I, Vg | Phase-shift full bridge with commutating inductor | calc | §23.4.1 Eq.(23.67)–(23.68), Figs.23.36–23.38 p.1025–1029 | high (energy inequality and duty-loss time: medium, derived from the prose/figure) |
| ERICKSON-2189 | protection | ZVT full bridge secondary rectifiers turn off with ZCS and ring (Lc with diode Coss), peaking well above 2n·Vg: add voltage-clamp snubbers on the secondary diodes | Vdiode,pk > 2n·Vg without clamp | Lc, Cj | Phase-shift ZVS bridges | measure | §23.4.1 p.1028 | high |
| ERICKSON-2190 | power | Active-clamp snubber (Cs + auxiliary MOSFET, complementary gating with dead time) on forward/flyback: recycles leakage energy, MOSFETs ZVS (secondary diodes ZCS), clamps Q1 at the minimum volt-second-balancing voltage, and resets the forward transformer so D > 50% is allowed | Vs = (D/D')·Vg; forward: Q1 peak = Vg + Vs = Vg/D' | D, Vg | Forward/flyback converters with wide input range | calc | §23.4.2 Eq.(23.69), Figs.23.39–23.40 p.1029–1031 | high (Q1 peak = Vg/D' derived: medium) |
| ERICKSON-2191 | power | Auxiliary resonant commutated pole (ARCP): ZVS for inverter legs without circulating current (Lr current only near commutation); gate the main switch at the start of interval 3 (late gating loses ZVS); optional current boost (iboost) guarantees ZVS but adds conduction loss and can lower efficiency | — | Lr, Cds, iboost | Voltage-source inverter legs (IGBT) | review | §23.4.3 Figs.23.41–23.42 p.1031–1033 | high |
| ERICKSON-2192 | current-carrying | RMS of common converter current waveforms (for copper, MOSFET, capacitor and fuse sizing) | DC: I. DC + linear ripple (±Δi): I·sqrt(1 + (1/3)(Δi/I)^2). Square wave ±Ipk: Ipk. Sine: Ipk/sqrt2. Pulse (height Ipk, duty D): Ipk·sqrt(D). Pulse with linear ripple: I·sqrt(D)·sqrt(1 + (1/3)(Δi/I)^2). Triangle rising D1·Ts and falling D2·Ts: Ipk·sqrt((D1 + D2)/3). Sawtooth over D1·Ts: Ipk·sqrt(D1/3). Zero-mean triangle ±Δi: Δi/sqrt3. Center-tapped bridge winding: (1/2)·Ipk·sqrt(1 + D). Stepped: sqrt(D1·I1^2 + D2·I2^2 + …) | I, Δi, Ipk, D | Periodic waveforms (Δi = peak ripple) | calc | App.A.1 Eq.(A.1)–(A.11) p.1037–1040 | high |
| ERICKSON-2193 | current-carrying | Piecewise RMS: split a waveform into segments of duty Dk and sum contributions | rms = sqrt(Σ Dk·uk); constant: uk = I1^2; triangular (0→I1): uk = I1^2/3; trapezoidal (I1→I2): uk = (I1^2 + I1·I2 + I2^2)/3; sinusoid half/full period: uk = Ipk^2/2; partial sinusoid θ1→θ2 (rad, < half period): uk = (Ipk^2/2)·(1 − sin(θ2 − θ1)·cos(θ2 + θ1)/(θ2 − θ1)) | segment shapes | Arbitrary piecewise waveforms | calc | App.A.2 Eq.(A.12)–(A.17) p.1040–1041 | high |
| ERICKSON-2194 | current-carrying | Short diode-recovery current spikes dominate switch rms: include them in conduction-loss estimates | Example Ts = 10 μs: 0→20 A in 0.2 μs, 20 A for 0.2 μs, 20→2 A in 0.1 μs, 2 A for 5 μs, 2→0 A in 0.2 μs → rms = 3.76 A (≈ 2.0 A without the spike) | segment data | Hard-switched transistor with freewheeling-diode Qrr | calc | App.A Example Eq.(A.18) p.1042 | high |
| ERICKSON-2195 | magnetics | Core geometrical constants used for core selection (tabulated in App. B): Kg for copper-loss/Bmax-limited inductors (Kg method, Ch.11), Kgfe for total (core + copper) loss–limited transformers/ac inductors (Ch.12) | Kg = Ac^2·WA/MLT (cm^5); Kgfe = WA·Ac^(2(1 − 1/β))·u(β)/(MLT·lm^(2/β)) (cm^x); Pfe = Kfe·Bmax^β; u(β) = [(β/2)^(−β/(β + 2)) + (β/2)^(2/(β + 2))]^(−(β + 2)/β); u(2.7) = 0.305 (±≈5% over 2.6 ≤ β ≤ 2.8); modern ferrites β ≈ 2.6–2.8; tables use β = 2.7 | Ac, WA, MLT, lm, β | Ferrite core selection; WA = single-section bobbin winding area | calc | App.B Eq.(B.1)–(B.4) p.1043 | high |
| ERICKSON-2196 | thermal | Core thermal resistance Rth (App. B) = approximate centre-leg-to-ambient temperature rise per watt of TOTAL (core + copper) loss, natural convection; forced air or unusual loss distribution changes it | ΔT ≈ Rth·(Pfe + Pcu); e.g. pot 2213: 38 °C/W; EC41: 16.5 °C/W; ETD39: 15 °C/W; ETD49: 11 °C/W | Rth, Ptot | Manufacturer data where published | calc | App.B p.1043–1047 | high |
| ERICKSON-2197 | magnetics | Wire selection data: AWG bare area and resistance per length (App. B.6) for Kg/Kgfe designs; the diameter column is larger than the bare conductor (appears to include insulation) | Rwire = ρ-per-length(AWG)·MLT·n; e.g. AWG 20: 5.188e-3 cm^2, 332.3e-6 Ω/cm; AWG 30: 0.5067e-3 cm^2, 3402.2e-6 Ω/cm | AWG, MLT, turns | Copper at the book's reference temperature (not stated) | calc | App.B.6 p.1049–1050 | high (insulation note: low) |
| ERICKSON-2198 | control-loop | CPM slope compensation is set by a fixed ramp ma while m2 = V/L moves with inductor tolerance (and losses shift the stability boundary): verify stability and the Gvg null (ma = 0.5·m2) at worst-case L, Vg and load | Example spec: L = 100 μH ± 10%, fs = 100 kHz, V = 15 V, Iload 2–4 A, Vg 22–32 V → find worst-case Gvg(0) | L tolerance, ma, V | CPM buck regulators | calc | §18 Problems 18.1(c), 18.5 p.799–800 | medium (problem setting) |
| ERICKSON-2199 | hw-fw | Size the A/D input range (Vref, sensing gain H0) so the converter does not saturate for output excursions of at least ±10% around nominal during transients, then maximize resolution within that window (window A/D: number of bins = window/qA/D) | A/D span ≥ H0·(1.2·V) window (±10%); ΔV(zero-error bin) = qA/D/H0 | VFS, nA/D, V, H0 | Digital voltage loops | calc | §19 Problems 19.4–19.5 p.839 | medium (problem specification) |
| ERICKSON-2200 | power | Universal-input boost PFC power-stage sizing criteria used in the book's design problem: inductor ripple Δig ≤ 20% of the instantaneous low-frequency current at the line peak under worst case; bulk-capacitor 2f ripple ≤ 5 V p-p; evaluate efficiency at both 90 Vrms and 270 Vrms with Rl, Ron, VF and switching-loss terms | Example: 90–270 Vrms, 385 V, 1000 W, fs = 100 kHz; losses RL = 0.1 Ω, Ron = 0.4 Ω, VF = 1.5 V, switching loss ≈ ig^2·0.25 Ω | Vac range, P, fs | Boost PFC design | calc | §21 Problem 21.10 p.927–928 | medium (problem specification) |

## 2. Formulas & tables (numbers)

### 2.1 Table 15.1 — CCM vs DCM conversion ratios in loss-free-resistor form (p.600)
Re = 2L/(D^2·Ts) for buck, boost, buck–boost; Re = 2(L1∥L2)/(D^2·Ts) for Ćuk and SEPIC. DCM when I < Icrit = ((1 − D)/D)·Vg/Re(D).

| Converter | M, CCM | M, DCM |
|---|---|---|
| Buck | D | 2/(1 + sqrt(1 + 4Re/R)) |
| Boost | 1/(1 − D) | (1 + sqrt(1 + 4R/Re))/2 |
| Buck–boost, Ćuk | −D/(1 − D) | −sqrt(R/Re) |
| SEPIC | D/(1 − D) | sqrt(R/Re) |

### 2.2 Table 15.2 — Small-signal DCM switch-network parameters (p.604)
Two-port: î1 = v̂1/r1 + j1·d̂ + g1·v̂2; î2 = −v̂2/r2 + j2·d̂ + g2·v̂1. M = V2/V1 of the network as defined in Figs.15.11a/15.21.

| Switch network | g1 | j1 | r1 | g2 | j2 | r2 |
|---|---|---|---|---|---|---|
| General two-switch (Fig.15.11a) | 0 | 2V1/(D·Re) | Re | 2/(M·Re) | 2V1/(D·M·Re) | M^2·Re |
| Buck (Fig.15.21a) | −1/Re | 2(1 − M)V1/(D·Re) | Re | (2 − M)/(M·Re) | 2(1 − M)V1/(D·M·Re) | M^2·Re |
| Boost (Fig.15.21b) | −1/((M − 1)^2·Re) | 2M·V1/(D(M − 1)Re) | (M − 1)^2·Re/M^2 | (2M − 1)/((M − 1)^2·Re) | 2V1/(D(M − 1)Re) | (M − 1)^2·Re |

(Buck and boost g1 signs re-derived by differentiating Eq.(15.20)–(15.21); the OCR lost the minus signs. conf = medium for those two cells.)

### 2.3 Tables 15.3 / 15.4 — DCM transfer-function salient features (p.607, p.621)
Gvd = Gd0/(1 + s/ωp); Gvg = Gg0/(1 + s/ωp) with Gg0 = M; high-frequency pole f2 = fs/(π·D2).

| Converter | Gd0 | ωp | f2 (HF pole) |
|---|---|---|---|
| Buck | (2V/D)·(1 − M)/(2 − M) | (2 − M)/((1 − M)·R·C) | M·fs/(π·D·(1 − M)) |
| Boost | (2V/D)·(M − 1)/(2M − 1) | (2M − 1)/((M − 1)·R·C) | (M − 1)·fs/(π·D) |
| Buck–boost | V/D | 2/(R·C) | abs(M)·fs/(π·D) |

### 2.4 Table 17.1 — Input-filter design impedances, CCM voltage mode (p.684)

| Converter | ZN(s) | ZD(s) | Ze(s) |
|---|---|---|---|
| Buck | −R/D^2 | (R/D^2)·(1 + sL/R + s^2·LC)/(1 + sRC) | sL/D^2 |
| Boost | −D'^2·R·(1 − sL/(D'^2·R)) | D'^2·R·(1 + sL/(D'^2·R) + s^2·LC/D'^2)/(1 + sRC) | sL |
| Buck–boost | −(D'^2·R/D^2)·(1 − sDL/(D'^2·R)) | (D'^2·R/D^2)·(1 + sL/(D'^2·R) + s^2·LC/D'^2)/(1 + sRC) | sL/D^2 |

Design criteria: abs(Zo) << abs(ZN), abs(Zo) << abs(ZD) (Gvd, loop gain unchanged); abs(Zo) << abs(Ze), abs(Zo) << abs(ZD) (output impedance unchanged).

### 2.5 Optimally damped single-section L–C input filters (§17.4, p.694–698)
ff = 1/(2π·sqrt(Lf·Cf)), R0f = sqrt(Lf/Cf); abs(Zo)mm = peak filter output impedance at the optimum.

| Damping | n | Qopt | fm (peak freq.) | abs(Zo)mm | Notes |
|---|---|---|---|---|---|
| Rf–Cb parallel (Rf + Cb across Cf) | Cb/Cf | Rf/R0f = sqrt((2 + n)(4 + 3n)/(2n^2(4 + n))) | ff·sqrt(2/(2 + n)) | R0f·sqrt(2(2 + n))/n | HF attenuation unchanged; n = (R0f^2/Zmm^2)(1 + sqrt(1 + 4Zmm^2/R0f^2)) |
| Rf–Lb parallel (Rf + Lb across Lf) | Lb/Lf | Rf/R0f = sqrt(n(3 + 4n)(1 + 2n)/(2(1 + 4n))) | ff·sqrt((1 + 2n)/(2n)) | R0f·sqrt(2n(1 + 2n)) | HF attenuation degraded by (1 + 1/n) |
| Rf–Lb series (Rf in series with Lf, Lb bypass) | Lb/Lf (assumed) | R0f/Rf = ((1 + n)/n)·sqrt(2(1 + n)(4 + n)/((2 + n)(4 + 3n))) | ff·sqrt((2 + n)/(2(1 + n))) | R0f·sqrt(2(1 + n)(2 + n))/n (≥ sqrt2·R0f) | Both inductors carry dc (conf medium: OCR) |

Worked values: Rf–Cb: R0f = 0.84 Ω, Zmm = 1 Ω → n = 2.5, Cb ≈ 1200 μF (Cf = 470 μF, Lf = 330 μH), Rf = 0.67 Ω. Rf–Lb (n = 0.5): Zmm = sqrt2·R0f, Qopt = 0.913, fm = sqrt2·ff, 9.5 dB HF penalty; n = 0.516 → Qopt = 0.93.

### 2.6 Table 18.1 — Simple CPM two-port model parameters (p.732)
î1 = v̂g/r1 + f1·îc + g1·v̂; output: î = g2·v̂g + f2·îc − v̂/r2 (Fig.18.6).

| Converter | g1 | f1 | r1 | g2 | f2 | r2 |
|---|---|---|---|---|---|---|
| Buck | D/R | D(1 + sL/R) | −R/D^2 | 0 | 1 | ∞ |
| Boost | 0 | 1 | ∞ | 1/(D'R) | D'(1 − sL/(D'^2·R)) | R |

(Buck–boost row not reproduced: OCR ambiguous; use the transfer functions of rule ERICKSON-2086.)

### 2.7 Table 18.2 — Accurate CPM controller gains (p.749)
d̂ = Fm(îc − îL − Fg·v̂g − Fv·v̂); Fm = 1/((Ma + (M1 − M2)/2)·Ts).

| Converter | Fg | Fv | m1, m2 (CCM) |
|---|---|---|---|
| Buck | D·D'·Ts/(2L) | 0 | (vg − v)/L, v/L |
| Boost | 0 | D·D'·Ts/(2L) | vg/L, (v − vg)/L |
| Buck–boost | D·D'·Ts/(2L) | −D·D'·Ts/(2L) | vg/L, −v/L |

Slope-compensation reference values: α = −(m2 − ma)/(m1 + ma); ma = 0 → unstable for D > 0.5; ma = m2/2 → stable for all D, buck Gvg(0) = 0; ma = m2 → α = 0 (deadbeat). fhf = (fs/π)/(1 + 2D(Ma/M2 − 1)); Qhf = (2/π)/(1 − 2D + 2D·Ma/M2) at fs/2.

### 2.8 Table 18.6 — Steady-state DCM current-programmed characteristics (p.784)
P = (1/2)·L·Ic^2·fs/(1 + Ma/M1)^2; Pload = V·I.

| Converter | M | Icrit | Stable range with ma = 0 |
|---|---|---|---|
| Buck | (Pload − P)/Pload | (1/2)(Ic − M·ma·Ts) | 0 ≤ M < 2/3 (ma > 0.086·m2 or voltage feedback extends to all D) |
| Boost | Pload/(Pload − P) | (1/(2M))(Ic − ((M − 1)/M)·ma·Ts) (re-derived) | 0 ≤ D ≤ 1 |
| Buck–boost | depends on load: Pload = P | per Table 18.6 (OCR garbled) | 0 ≤ D ≤ 1 |

### 2.9 Tables 19.1–19.3 — Digital control building blocks (p.811–821)

| Item | Value |
|---|---|
| Trailing-edge DPWM delay tmod | D·Ts |
| Leading-edge DPWM delay | (1 − D)·Ts |
| Dual-edge (triangle) DPWM delay | Ts/2 |
| Loop delay | td = tctrl + tmod; phase = −ω·td |
| Trapezoidal integrator | Gcd = (ωo·Ts/2)(z + 1)/(z − 1) |
| Backward Euler integrator | Gcd = ωo·Ts/(z − 1) |
| Forward Euler integrator | Gcd = ωo·Ts·z/(z − 1) |
| Bilinear (Tustin) | s → (2/Ts)(z − 1)/(z + 1); MATLAB c2d(Gc,Ts,'tustin') |
| Tustin with prewarp | s → kprewarp·(2/Ts)(z − 1)/(z + 1), kprewarp = (ωpw·Ts/2)/tan(ωpw·Ts/2); c2d(Gc,Ts,'prewarp',wprewarp) |
| A/D LSB | qA/D = VFS/2^nA/D |
| DPWM LSB | qDPWM = 1/2^nDPWM; counter DPWM: fclk = 2^nDPWM·fs |
| No-limit-cycle conditions | Gd0·H0·qDPWM < qA/D; 0 < KI < 1/(Gd0·H0); KI = lim(z→1)(z − 1)·Gcd(z) |

### 2.10 Table 21.1 — PFC outer-loop small-signal parameters (p.904)
v̂/v̂control = j2·(R∥r2)/(1 + sC(R∥r2)); v̂/v̂g,rms = g2·(R∥r2)/(1 + sC(R∥r2)).

| Controller | g2 | j2 | r2 |
|---|---|---|---|
| Average current control with feedforward | 0 | Pav/(V·Vcontrol) | V^2/Pav |
| Current-programmed | 2Pav/(V·Vg,rms) | Pav/(V·Vcontrol) | V^2/Pav |
| Nonlinear-carrier charge control (boost) | 2Pav/(V·Vg,rms) | Pav/(V·Vcontrol) | V^2/(2Pav) |
| Boost, critical conduction mode (control = ton) | 2Pav/(V·Vg,rms) | Pav/(V·ton) | V^2/Pav |
| DCM buck–boost, flyback, SEPIC, Ćuk (control = D) | 2Pav/(V·Vg,rms) | 2Pav/(V·D) | V^2/Pav |

### 2.11 Table 21.2 — (1/π)∫0..π sin^n(θ) dθ (p.907)

| n | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| value | 2/π | 1/2 | 4/(3π) | 3/8 | 16/(15π) | 15/48 |

### 2.12 Table 21.3 — PWM-rectifier (PFC) current stresses, CCM, switching ripple neglected (p.909)
Iac,rms/Idc = sqrt2·V/VM; ac input VM·sin(ωt), dc output V; flyback/isolated SEPIC with n:1 transformer.

| Converter / element | rms | average | peak |
|---|---|---|---|
| Boost: transistor | Iac,rms·sqrt(1 − (8/(3π))·VM/V) | Iac,rms·(2sqrt2/π)(1 − π·VM/(8V)) | sqrt2·Iac,rms |
| Boost: diode | Idc·sqrt((16/(3π))·V/VM) | Idc | 2·Idc·V/VM (= sqrt2·Iac,rms) |
| Boost: inductor | Iac,rms | (2sqrt2/π)·Iac,rms | sqrt2·Iac,rms |
| Flyback: transistor, xfmr primary | Iac,rms·sqrt(1 + (8/(3π))·VM/(nV)) | (2sqrt2/π)·Iac,rms | sqrt2·Iac,rms·(1 + VM/(nV)) |
| Flyback: L1 (input filter) | Iac,rms | (2sqrt2/π)·Iac,rms | sqrt2·Iac,rms |
| Flyback: C1 (input filter) | Iac,rms·sqrt((8/(3π))·VM/(nV)) | 0 | sqrt2·Iac,rms·max(1, VM/(nV)) |
| Flyback: diode, xfmr secondary | Idc·sqrt(3/2 + (16/(3π))·nV/VM) | Idc | 2·Idc·(1 + nV/VM) |
| SEPIC (nonisolated): transistor | Iac,rms·sqrt(1 + (8/(3π))·VM/V) | (2sqrt2/π)·Iac,rms | sqrt2·Iac,rms·(1 + VM/V) |
| SEPIC: L1 | Iac,rms | (2sqrt2/π)·Iac,rms | sqrt2·Iac,rms |
| SEPIC: C1 | Iac,rms·sqrt((8/(3π))·VM/V) | 0 | sqrt2·Iac,rms·max(1, VM/V) |
| SEPIC: L2 | Iac,rms·(VM/V)·sqrt(3/2) | Iac,rms·VM/(sqrt2·V) | sqrt2·Iac,rms·VM/V |
| SEPIC: diode | Idc·sqrt(3/2 + (16/(3π))·V/VM) | Idc | 2·Idc·(1 + V/VM) |
| Isolated SEPIC: transistor | Iac,rms·sqrt(1 + (8/(3π))·VM/(nV)) | (2sqrt2/π)·Iac,rms | sqrt2·Iac,rms·(1 + VM/(nV)) |
| Isolated SEPIC: C1, xfmr primary | Iac,rms·sqrt((8/(3π))·VM/(nV)) | 0 | sqrt2·Iac,rms·max(1, VM/(nV)) |
| Isolated SEPIC: diode, xfmr secondary | Idc·sqrt(3/2 + (16/(3π))·nV/VM) | Idc | 2·Idc·(1 + nV/VM) |

(Column assignment reconstructed from a flattened table; boost rows verified against Eq.(21.122)–(21.126); the others: conf = medium.)

### 2.13 Fig.20.7 — Typical single-phase peak-detection rectifier line-current spectrum (p.857)

| Harmonic | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 | 19 |
|---|---|---|---|---|---|---|---|---|---|---|
| % of fundamental | 100 | 91 | 73 | 52 | 32 | 19 | 15 | 15 | 13 | 9 |

THD = 136%, distortion factor = 59% (graph values; DF typically 55–65%). DF = 1/sqrt(1 + THD^2): THD 10% → 99.5%, 20% → 98%, 33% → 95%.

### 2.14 Table 22.1 — Tank branch reactances and first-harmonic results (p.975–976)

| Tank | Xs (series branch) | Xp (shunt branch) |
|---|---|---|
| Series | ωL − 1/(ωC) | ∞ |
| Parallel | ωL | −1/(ωC) |
| LCC | ωL − 1/(ωCs) | −1/(ωCp) |
| LLC | ωLs − 1/(ωC) | ωLp |

Zi0 = j·Xs; Zi∞ = j(Xs + Xp); H∞ = Xp/(Xp + Xs); Zo0 = j·Xs·Xp/(Xs + Xp); Rcrit = abs(Xp)·sqrt(−Xs/(Xs + Xp)); fm where Xs = −Xp/2; (M/a)^2 + (J/b)^2 = 1 with a = abs(H∞), b = R0/abs(Xs); M = 1/sqrt(1/a^2 + (Qe/b)^2), Qe = R0/Re.

Rectifier loading constants: capacitive-filter rectifier Re = 8R/π^2 = 0.8106·R (M = abs(H)); inductive-filter rectifier Re = π^2·R/8 = 1.2337·R (M = (8/π^2)·abs(H)); square-wave bridge fundamental = (4/π)·Vg.

### 2.15 Appendix A — RMS values of common converter waveforms (p.1037–1041)

| Waveform | rms |
|---|---|
| DC | I |
| DC + linear ripple (peak Δi) | I·sqrt(1 + (1/3)(Δi/I)^2) |
| Square wave ±Ipk | Ipk |
| Sine | Ipk/sqrt2 |
| Pulse, duty D | Ipk·sqrt(D) |
| Pulse with linear ripple | I·sqrt(D)·sqrt(1 + (1/3)(Δi/I)^2) |
| Triangle, rise D1·Ts, fall D2·Ts | Ipk·sqrt((D1 + D2)/3) |
| Sawtooth over D1·Ts | Ipk·sqrt(D1/3) |
| Zero-mean triangle, peak Δi | Δi/sqrt3 |
| Center-tapped bridge winding | (1/2)·Ipk·sqrt(1 + D) |
| General stepped | sqrt(D1·I1^2 + D2·I2^2 + …) |
| Piecewise segment contributions uk (rms = sqrt(Σ Dk·uk)) | constant I1^2; triangle I1^2/3; trapezoid (I1^2 + I1·I2 + I2^2)/3; half/full sine Ipk^2/2; partial sine (Ipk^2/2)(1 − sin(θ2 − θ1)·cos(θ2 + θ1)/(θ2 − θ1)) |

### 2.16 Appendix B.1 — Pot core data (p.1044)
Kgfe tabulated for β = 2.7. Rth = centre-leg-to-ambient °C per W of total loss (blank = not published).

| Core (AH, mm) | Kg (cm^5) | Kgfe (cm^x) | Ac (cm^2) | WA (cm^2) | MLT (cm) | lm (cm) | Rth (°C/W) | Weight (g) |
|---|---|---|---|---|---|---|---|---|
| 704 | 0.738e-6 | 1.61e-6 | 0.070 | 0.22e-3 | 1.46 | 1.0 | — | 0.5 |
| 905 | 0.183e-3 | 256e-6 | 0.101 | 0.034 | 1.90 | 1.26 | — | 1.0 |
| 1107 | 0.667e-3 | 554e-6 | 0.167 | 0.055 | 2.30 | 1.55 | — | 1.8 |
| 1408 | 2.107e-3 | 1.1e-3 | 0.251 | 0.097 | 2.90 | 2.00 | 100 | 3.2 |
| 1811 | 9.45e-3 | 2.6e-3 | 0.433 | 0.187 | 3.71 | 2.60 | 60 | 7.3 |
| 2213 | 27.1e-3 | 4.9e-3 | 0.635 | 0.297 | 4.42 | 3.15 | 38 | 13 |
| 2616 | 69.1e-3 | 8.2e-3 | 0.948 | 0.406 | 5.28 | 3.75 | 30 | 20 |
| 3019 | 0.180 | 14.2e-3 | 1.38 | 0.587 | 6.20 | 4.50 | 23 | 34 |
| 3622 | 0.411 | 21.7e-3 | 2.02 | 0.748 | 7.42 | 5.30 | 19 | 57 |
| 4229 | 1.15 | 41.1e-3 | 2.66 | 1.40 | 8.60 | 6.81 | 13.5 | 104 |

### 2.17 Appendix B.2 — EE core data (p.1045)

| Core | Kg (cm^5) | Kgfe (cm^x) | Ac (cm^2) | WA (cm^2) | MLT (cm) | lm (cm) | Weight (g) |
|---|---|---|---|---|---|---|---|
| EE12 | 0.731e-3 | 0.458e-3 | 0.14 | 0.085 | 2.28 | 2.7 | 2.34 |
| EE16 | 2.02e-3 | 0.842e-3 | 0.19 | 0.190 | 3.40 | 3.45 | 3.29 |
| EE19 | 4.07e-3 | 1.3e-3 | 0.23 | 0.284 | 3.69 | 3.94 | 4.83 |
| EE22 | 8.26e-3 | 1.8e-3 | 0.41 | 0.196 | 3.99 | 3.96 | 8.81 |
| EE30 | 85.7e-3 | 6.7e-3 | 1.09 | 0.476 | 6.60 | 5.77 | 32.4 |
| EE40 | 0.209 | 11.8e-3 | 1.27 | 1.10 | 8.50 | 7.70 | 50.3 |
| EE50 | 0.909 | 28.4e-3 | 2.26 | 1.78 | 10.0 | 9.58 | 116 |
| EE60 | 1.38 | 36.4e-3 | 2.47 | 2.89 | 12.8 | 11.0 | 135 |
| EE70/68/19 | 5.06 | 75.9e-3 | 3.24 | 6.75 | 14.0 | 18.0 | 280 |

### 2.18 Appendix B.3 — EC core data (p.1046)

| Core | Kg (cm^5) | Kgfe (cm^x) | Ac (cm^2) | WA (cm^2) | MLT (cm) | lm (cm) | Rth (°C/W) | Weight (g) |
|---|---|---|---|---|---|---|---|---|
| EC35 | 0.131 | 9.9e-3 | 0.843 | 0.975 | 5.30 | 7.74 | 18.5 | 35.5 |
| EC41 | 0.374 | 19.5e-3 | 1.21 | 1.35 | 5.30 | 8.93 | 16.5 | 57.0 |
| EC52 | 0.914 | 31.7e-3 | 1.80 | 2.12 | 7.50 | 10.5 | 11.0 | 111 |
| EC70 | 2.84 | 56.2e-3 | 2.79 | 4.71 | 12.9 | 14.4 | 7.5 | 256 |

### 2.19 Appendix B.4 — ETD core data (p.1047)

| Core | Kg (cm^5) | Kgfe (cm^x) | Ac (cm^2) | WA (cm^2) | MLT (cm) | lm (cm) | Rth (°C/W) | Weight (g) |
|---|---|---|---|---|---|---|---|---|
| ETD29 | 0.0978 | 8.5e-3 | 0.76 | 0.903 | 5.33 | 7.20 | — | 30 |
| ETD34 | 0.193 | 13.1e-3 | 0.97 | 1.23 | 6.00 | 7.86 | 19 | 40 |
| ETD39 | 0.397 | 19.8e-3 | 1.25 | 1.74 | 6.86 | 9.21 | 15 | 60 |
| ETD44 | 0.846 | 30.4e-3 | 1.74 | 2.13 | 7.62 | 10.3 | 12 | 94 |
| ETD49 | 1.42 | 41.0e-3 | 2.11 | 2.71 | 8.51 | 11.4 | 11 | 124 |

(The ETD Rth/weight columns were flattened into 9 numbers; assignment ETD29 = weight only is inferred. conf = medium for those two columns.)

### 2.20 Appendix B.5 — PQ core data (p.1048)

| Core (A1/2D) | Kg (cm^5) | Kgfe (cm^x) | Ac (cm^2) | WA (cm^2) | MLT (cm) | lm (cm) | Weight (g) |
|---|---|---|---|---|---|---|---|
| PQ20/16 | 22.4e-3 | 3.7e-3 | 0.62 | 0.256 | 4.4 | 3.74 | 13 |
| PQ20/20 | 33.6e-3 | 4.8e-3 | 0.62 | 0.384 | 4.4 | 4.54 | 15 |
| PQ26/20 | 83.9e-3 | 7.2e-3 | 1.19 | 0.333 | 5.62 | 4.63 | 31 |
| PQ26/25 | 0.125 | 9.4e-3 | 1.18 | 0.503 | 5.62 | 5.55 | 36 |
| PQ32/20 | 0.203 | 11.7e-3 | 1.70 | 0.471 | 6.71 | 5.55 | 42 |
| PQ32/30 | 0.384 | 18.6e-3 | 1.61 | 0.995 | 6.71 | 7.46 | 55 |
| PQ35/35 | 0.820 | 30.4e-3 | 1.96 | 1.61 | 7.52 | 8.79 | 73 |
| PQ40/40 | 1.20 | 39.1e-3 | 2.01 | 2.50 | 8.39 | 10.2 | 95 |

All Kg entries of 2.16–2.20 were cross-checked against Kg = Ac^2·WA/MLT (agreement ≤ 0.5%).

### 2.21 Appendix B.6 — American Wire Gauge data (p.1049–1050), as printed

| AWG | Bare area (1e-3 cm^2) | Resistance (1e-6 Ω/cm) | Diameter (cm) |
|---|---|---|---|
| 0000 | 1072.3 | 1.608 | 1.168 |
| 000 | 850.3 | 2.027 | 1.040 |
| 00 | 674.2 | 2.557 | 0.927 |
| 0 | 534.8 | 3.224 | 0.825 |
| 1 | 424.1 | 4.065 | 0.735 |
| 2 | 336.3 | 5.128 | 0.654 |
| 3 | 266.7 | 6.463 | 0.583 |
| 4 | 211.5 | 8.153 | 0.519 |
| 5 | 167.7 | 10.28 | 0.462 |
| 6 | 133.0 | 13.0 | 0.411 |
| 7 | 105.5 | 16.3 | 0.366 |
| 8 | 83.67 | 20.6 | 0.326 |
| 9 | 66.32 | 26.0 | 0.291 |
| 10 | 52.41 | 32.9 | 0.267 |
| 11 | 41.60 | 41.37 | 0.238 |
| 12 | 33.08 | 52.09 | 0.213 |
| 13 | 26.26 | 69.64 | 0.190 |
| 14 | 20.02 | 82.80 | 0.171 |
| 15 | 16.51 | 104.3 | 0.153 |
| 16 | 13.07 | 131.8 | 0.137 |
| 17 | 10.39 | 165.8 | 0.122 |
| 18 | 8.228 | 209.5 | 0.109 |
| 19 | 6.531 | 263.9 | 0.0948 |
| 20 | 5.188 | 332.3 | 0.0874 |
| 21 | 4.116 | 418.9 | 0.0785 |
| 22 | 3.243 | 531.4 | 0.0701 |
| 23 | 2.508 | 666.0 | 0.0632 |
| 24 | 2.047 | 842.1 | 0.0566 |
| 25 | 1.623 | 1062.0 | 0.0505 |
| 26 | 1.280 | 1345.0 | 0.0452 |
| 27 | 1.021 | 1687.6 | 0.0409 |
| 28 | 0.8046 | 2142.7 | 0.0366 |
| 29 | 0.6470 | 2664.3 | 0.0330 |
| 30 | 0.5067 | 3402.2 | 0.0294 |
| 31 | 0.4013 | 4294.6 | 0.0267 |
| 32 | 0.3242 | 5314.9 | 0.0241 |
| 33 | 0.2554 | 6748.6 | 0.0236 |
| 34 | 0.2011 | 8572.8 | 0.0191 |
| 35 | 0.1589 | 10849 | 0.0170 |
| 36 | 0.1266 | 13608 | 0.0152 |
| 37 | 0.1026 | 16801 | 0.0140 |
| 38 | 0.08107 | 21266 | 0.0124 |
| 39 | 0.06207 | 27775 | 0.0109 |
| 40 | 0.04869 | 35400 | 0.0096 |
| 41 | 0.03972 | 43405 | 0.00863 |
| 42 | 0.03166 | 54429 | 0.00762 |
| 43 | 0.02452 | 70308 | 0.00685 |
| 44 | 0.0202 | 85072 | 0.00635 |

Printed-value anomalies (reproduced, not corrected): AWG 13 resistance 69.64 and AWG 14 area 20.02 break the smooth ≈1.26×/gauge progression; AWG 33 diameter 0.0236 is out of sequence. The diameter column exceeds the bare-copper diameter (e.g. AWG 44 bare ≈ 0.0051 cm vs 0.00635 cm printed), so it appears to be an insulated (film) diameter — use it for window-fill estimates, not for skin-depth ratios without checking.

### 2.22 Worked-example regression anchors (for Anvil simulation tests)

| Example | Inputs | Book results | Source |
|---|---|---|---|
| Op-amp PD circuit loop | T0 = 33000, f1 = 10 Hz, f4 = 1.9 kHz, f3 = 100 kHz | fc = 25.2 kHz, φm = 14.2°, Q = 4 (12 dB) | §13.3 p.526–527 |
| Voltage-mode buck regulator | 28 V → 15 V, L = 50 μH, C = 500 μF, R = 3 Ω, fs = 100 kHz, VM = 4 V, PID R1 = 11 kΩ, R2 = 85 kΩ, R3 = 120 kΩ, R4 = 47 kΩ, C2 = 1.1 nF, C3 = 2.7 nF | CCM fc = 5.3 kHz, φm = 47°; at R = 25 Ω (DCM) fc = 390 Hz, φm = 55°; Gvg(100 Hz) = −38 dB / −34 dB | §15.4.2 p.614–617 |
| DCM boost Gvd | 24 V → 36 V, 3 A, L = 5 μH, C = 470 μF, R = 12 Ω, fs = 100 kHz | Re = 16 Ω, D = 0.25, Gd0 = 72 V, fp = 112 Hz, f2 = 64 kHz, fz = 127 kHz | §15.3.1 p.607–608 |
| SEPIC damping | 18 V → 24 V, L1 = 100 μH, L2 = 50 μH, C1 = 22 μF, C2 = 220 μF, R = 5 Ω | fo = 711 Hz, Qo = 4.9, RHP zero 4.5 kHz; damping Rb = 2 Ω, Cb = 100 μF | §16.2.4 p.644–648 |
| Input filter (buck) | Lf = 330 μH, Cf = 470 μF, L = 100 μH, C = 100 μF, R = 3 Ω, D = 0.5 | ff = 400 Hz, R0f = 0.84 Ω, f0 = 1.6 kHz, R/D^2 = 12 Ω; optimal Rf = 0.67 Ω, Cb = 1200 μF | §17.3–17.4 p.685–696 |
| Two-stage input filter | 80 dB at 250 kHz | L1 = 31.2 μH, C1 = 6.9 μF, n1L1 = 15.6 μH, R1 = 1.9 Ω; L2 = 5.8 μH, C2 = 11.7 μF, n2L2 = 2.9 μH, R2 = 0.65 Ω | §17.4.5 p.700–705 |
| CPM buck voltage loop | Vg = 12 V, L = 35 μH, C = 100 μF, R = 10 Ω, fs = 200 kHz, Rf = 1 Ω, Va = 0.6 V, H = 0.375 | Gc0 = 7.92 Ω, fp1 = 201 Hz, fhf = 174 kHz; PI Gcm = 67.1, fzv = fcv/3, fcv = 40 kHz, φv = 59° | §18.6.2 p.770–772 |
| ACM boost | 170 V → 400 V, 2 kW, fs = 100 kHz, Rf = 0.25 Ω, VM = 4 V, H = 0.0075 | Gcm = 0.63, fz = 4 kHz, fp = 25 kHz, φm = 46° at fci = 10 kHz; Gvm = 16.4, fzv = 333 Hz, φmv = 72° at fcv = 1 kHz | §18.9.2 p.791–797 |
| Digital POL buck | 5 V → 1.8 V, L = 1 μH (30 mΩ), C = 200 μF (0.8 mΩ), fs = 1 MHz | Gcd = 31.7593(z − 0.9493)(z − 0.8654)/((z − 1)(z + 0.1881)), fc = 100 kHz, φm ≈ 52° with td = 0.36 μs | §19.3.2 p.824–826 |
| DCM boost PFC | 120 Vrms/50 Hz → 300 V, L = 200 μH, C = 150 μF, fs = 100 kHz | 100 W: THD 16.7%, h3 16.6%, 2f ripple ≈ 8 V p-p; 180 W: THD 71% | §21.2.2 p.876–878 |
| Boost PFC efficiency | 120 Vrms → 390 V, 500 W, η = 95% | Re = 27.4 Ω, Ron ≤ 2.11 Ω | §21.6.4 p.916–917 |
| LCC inverter | fs = 100 kHz, Vg = 160 V, Voc = 400 V, 150 Vrms at 25 W | Cp ≈ 1.06 nF, Xs = 733 Ω, Rcrit = 1466 Ω; Cs = 3.2 nF → L = 1.96 mH | §22.4.4 p.967–971 |

## 3. Mechanizable checks

Units: V, A, Ω, H, F, Hz, s unless stated. "margin" is reported as a ratio or dB so Anvil can rank designs. Source rows refer to section 1 ids.

`CHECK-dcm-mode-lfr`: inputs (topology, D, Vg, I, L or L1∥L2, fs) → Re = 2L/(D^2/fs); Icrit = ((1 − D)/D)·Vg/Re → mode = CCM if I > Icrit else DCM → margin = I/Icrit (report per load corner; any corner in DCM triggers the DCM small-signal checks) → ERICKSON-2026, 2030, 2031.

`CHECK-dcm-plant`: inputs (topology, V, D, M, R, C, fs) → Gd0, ωp from Table 15.3; f2 = fs/(π·D2) (Table 15.4) → pass if loop crossover fc ≤ f2/10 (phase lag of the HF pole starts ≈ f2/10) → margin = f2/(10·fc) → ERICKSON-2033, 2034, 2035 (the f2/10 criterion is the book's observation in the boost example: conf medium).

`CHECK-light-load-loop`: inputs (loop-gain sims at max load and at min load) → fc, φm at each → pass if φm ≥ project target at every load and the DCM-load fc still meets the transient/line-rejection spec → margin = min φm − target → ERICKSON-2038, 2039.

`CHECK-eet-ignore-element`: inputs (Z(f), ZN(f), ZD(f), port type) → ratio in the correction factor: element replacing an open port → rN = abs(ZN/Z), rD = abs(ZD/Z); element replacing a short → rN = abs(Z/ZN), rD = abs(Z/ZD) → pass class A (deviation < ±1 dB, < ±7°) if 20·log10(max(rN, rD)) ≤ −20 dB at all f in band; class B (< ±3.5 dB, < ±20°) if ≤ −10 dB → margin = −20·log10(max(rN, rD)) dB → ERICKSON-2045, 2046.

`CHECK-input-filter-impedance`: inputs (Zo(f) of the EMI filter from netlist/AC sim; converter ZN, ZD, Ze from Table 17.1 at worst-case R (full load), D (both line extremes)) → r(f) = abs(Zo)/min(abs(ZN), abs(ZD)); rZe(f) = abs(Zo)/abs(Ze) → pass if max_f r(f) ≤ k (k = 0.2–0.4 as in the book's problem specs; default 0.3) and, if Zout must be preserved, max_f rZe ≤ k → margin = 20·log10(k/max r) dB → ERICKSON-2060, 2062, 2063, 2064.

`CHECK-input-filter-attenuation`: inputs (I, D, fs, H(f) of filter, harmonic limit Ilim per harmonic) → I_k = (2I/(kπ))·abs(sin(kπD))·abs(H(j·2π·k·fs)) (peak; rms = I_k/sqrt2) for k = 1…K → pass if all I_k,rms ≤ Ilim → margin = 20·log10(Ilim/max I_k,rms) → ERICKSON-2056, 2057.

`CHECK-input-filter-damping-design`: inputs (Lf, Cf, target Zmm, scheme) → ff, R0f; Rf–Cb: n = (R0f^2/Zmm^2)(1 + sqrt(1 + 4Zmm^2/R0f^2)), Cb = n·Cf, Rf = R0f·sqrt((2 + n)(4 + 3n)/(2n^2(4 + n))); Rf–Lb: solve Zmm = R0f·sqrt(2n(1 + 2n)) for n, Lb = n·Lf, Rf = R0f·sqrt(n(3 + 4n)(1 + 2n)/(2(1 + 4n))), HF penalty 20·log10(1 + 1/n) dB → pass if chosen parts are within the project's component tolerance of these values and the HF-penalized attenuation still meets CHECK-input-filter-attenuation → ERICKSON-2067, 2068, 2070, 2071.

`CHECK-input-filter-minor-loop`: inputs (Rf, R, M) → Tm_peak = Rf·M^2/R → pass if Tm_peak < 1 (no RHP poles from Zo/Zi for a resistively damped single section; confirm with Nyquist of Tm = Zo/Zi when multiple crossovers) → margin = 1/Tm_peak → ERICKSON-2061, 2075, 2076, 2077.

`CHECK-cascaded-filter-interaction`: inputs (Za(f) of added section, ZN1(f) = Zin of existing filter with output shorted, ZD1(f) = with output open) → r = abs(Za)/min(abs(ZN1), abs(ZD1)) → pass if max r ≤ k (default 0.3) or, where r ≈ 1, phase difference ∠Za − ∠ZD1 ≤ 90° (then Zo decreases) → ERICKSON-2072, 2074.

`CHECK-cpm-subharmonic`: inputs (topology, Vg range, V, L_min…L_max (tolerance), Ts, ma) → per corner m1, m2 (Table 18.2 slopes), α = −(m2 − ma)/(m1 + ma) → pass if abs(α) < 1 at every corner; recommended ma ≥ 0.5·m2(max) → margin = 1 − max abs(α); also report Qhf = (2/π)(1 − α)/(1 + α) (fs/2 peaking indicator) → ERICKSON-2082, 2083, 2084, 2093, 2198.

`CHECK-cpm-dcm-buck`: inputs (M, ma, m2) → fail if converter can enter DCM with M ≥ 2/3 and ma ≤ 0.086·m2 without outer voltage feedback → ERICKSON-2102.

`CHECK-cpm-voltage-loop`: inputs (Fm, V, D, R, L, C, fs, H, Rf, fcv, fzv) → Gc0, ωc, Qc (Table 18.3), fp1 = Qc·fc, fhf = fc/Qc; Gcm = Rf·fcv/(H·Gc0·fp1); φv = atan(fcv/fzv) − atan(fcv/fhf) → pass if φv ≥ target and fcv ≤ fs/5 (the averaged CPM model is shown valid to ≈ fs/5 at Ma = 0.5·M2) → ERICKSON-2091, 2095, 2100, 2101.

`CHECK-acm-current-loop`: inputs (L, V, VM, Rf, fci, fz, fp, fs) → Gcm = L·2π·fci·VM/(Rf·V); φm = atan(fci/fz) − atan(fci/fp) → pass if φm ≥ target (book example 46°) and fci ≤ fs/10 and fcv ≤ fci/10 → ERICKSON-2104, 2105, 2106, 2107.

`CHECK-digital-adc`: inputs (VFS, nA/D, H, V, tolerance ±ΔV) → qA/D = VFS/2^nA/D → pass if qA/D ≤ 2·H·ΔV and the A/D span covers H·V·(1 ± 0.1) → margin = 2·H·ΔV/qA/D → ERICKSON-2109, 2199.

`CHECK-digital-dpwm`: inputs (nDPWM, M(D) or dV/dD, fs, fclk, positioning spec p) → ΔV/V = qDPWM·(dV/dD)/V (buck: 1/(2^n·M)); counter clock need fclk = 2^n·fs → pass if ΔV/V ≤ p and fclk ≤ available clock (else require delay-line/hybrid/ΔΣ) → ERICKSON-2110, 2111, 2123.

`CHECK-limit-cycle`: inputs (Gd0 (buck: Vg), H0, qDPWM, qA/D, KI or Gcd(z)) → KI = lim(z→1)(z − 1)·Gcd(z) → pass if Gd0·H0·qDPWM < qA/D and 0 < KI < 1/(Gd0·H0) → margins = qA/D/(Gd0·H0·qDPWM), 1/(Gd0·H0·KI) → ERICKSON-2122.

`CHECK-digital-delay-margin`: inputs (fc, φm_analog, tctrl, D, Ts, modulator type) → td = tctrl + {D·Ts, (1 − D)·Ts, Ts/2}; φm_digital = φm_analog − 360·fc·td → pass if φm_digital ≥ target → ERICKSON-2113, 2114, 2121.

`CHECK-pid-mapping`: inputs (Gcm, fL, fz, fp1, fpw = fc, fs) → a = tan(π·fpw/fs); zL, zz, zp, Gd per ERICKSON-2118 → pass if the digital loop gain Td crosses 0 dB at the analog design fc and its phase margin equals the analog margin minus 360·fc·td (within a project tolerance); flag zL, zz, zp lying very close to z = 1 (word-length/roundoff risk) → ERICKSON-2116, 2117, 2118.

`CHECK-power-factor`: inputs (I_n harmonic rms or peak list, φ1 − θ1) → THD = sqrt(Σn≥2 In^2)/I1; DF = 1/sqrt(1 + THD^2); PF = DF·cos(φ1 − θ1) → pass if PF ≥ spec and each In ≤ applicable limit → ERICKSON-2124, 2125, 2126, 2127.

`CHECK-branch-circuit-power`: inputs (Vac, Ibreaker, derating = 0.8, PF, η) → Pdc,max = Vac·derating·Ibreaker·PF·η → pass if Pload ≤ Pdc,max → margin = Pdc,max/Pload → ERICKSON-2128.

`CHECK-neutral-current`: inputs (per-phase harmonic currents Ik (peak), I0) → in,rms = 3·sqrt(I0^2 + Σk triplen Ik^2/2) → pass if in,rms ≤ neutral ampacity → ERICKSON-2130.

`CHECK-pfc-ccm-dcm-map`: inputs (VM, V, L, fs, P) → Re = VM^2/(2P); CCM whole cycle if Re < 2L·fs; DCM whole cycle if Re > 2L·fs/(1 − VM/V); report the line-angle band in DCM → pass per chosen control law (ACM: any; CPM/NLC: minimize DCM band; open-loop DCM boost: DCM whole cycle at Pmax) → ERICKSON-2134, 2135, 2139, 2141.

`CHECK-pfc-flyback-dcm`: inputs (Rmin, Ts, n, V, VM,min) → Lcrit = Rmin·Ts/(4(1 + nV/VM,min)^2) → pass if L < Lcrit → margin = Lcrit/L → ERICKSON-2136.

`CHECK-pfc-crm-frequency`: inputs (VM range, V, L, P range) → fs,max = VM^2/(4LP), fs,min = fs,max·(1 − VM/V) over all corners → pass if within [f_allowed_min, f_allowed_max] → ERICKSON-2140.

`CHECK-pfc-bulk-capacitor`: inputs (Pload, C, VC, f_line, ripple spec, t_hold, Vmin of downstream converter) → 2ΔvC ≈ Pload/(2π·f_line·C·VC) ≤ spec; hold-up: (1/2)·C·(VC,min_ripple^2 − Vmin^2) ≥ Pload·t_hold (t_hold typically one line cycle, 20 ms at 50 Hz) → ERICKSON-2142 (hold-up energy inequality derived from the book's prose: conf medium).

`CHECK-pfc-device-stress`: inputs (topology, Iac,rms, Idc, VM, V, n) → rms/avg/peak per Table 21.3 → pass if each ≤ device rating × derating → ERICKSON-2148, 2149, 2150.

`CHECK-pfc-efficiency`: inputs (Ron, Re, VM, V) → a = (VM/V)(Ron/Re); η = (1 − Ron/Re)·F(a) (closed form of ERICKSON-2151) → pass if η ≥ target (conduction only; add other losses separately) → ERICKSON-2151, 2152.

`CHECK-pfc-outer-loop`: inputs (controller type, Pav, V, Vcontrol, Vg,rms, C, R or constant-power load, compensator) → plant from Table 21.1 (integrator j2/(sC) for constant-power loads except NLC) → pass if loop gain at 2·f_line is small enough for the harmonic budget (project threshold) and φm ≥ target → ERICKSON-2144, 2145, 2146 (numeric threshold is a project choice: conf low).

`CHECK-resonant-gain`: inputs (tank type, element values, R, rectifier/filter type, fs) → Re (0.8106·R or 1.2337·R), Xs, Xp, H → M = abs(H) (cap filter) or (8/π^2)·abs(H) (inductor filter) → pass if M(fs_min…fs_max) covers the required V/Vg range at all loads → ERICKSON-2158, 2159, 2161, 2171.

`CHECK-resonant-validity`: inputs (fs, f0, Qe) → flag if fs < f0/2 for SRC (subharmonic/DCM region; first-harmonic model invalid) or Qe small (low-Q inaccuracy) → ERICKSON-2159, 2160, 2172, 2173.

`CHECK-resonant-zvs`: inputs (Xs(fs), Xp(fs), load range Rmin…Rmax, or LLC n, F) → Zi0 = jXs, Zi∞ = j(Xs + Xp); both inductive → ZVS all loads; both capacitive → ZCS all loads; mixed → Rcrit = abs(Xp)·sqrt(−Xs/(Xs + Xp)); LCC-type (Zi0 inductive): ZVS for R < Rcrit; LLC-type (Zi∞ inductive): ZVS for R > Rcrit → pass if the whole load range lies in the ZVS region (or accept documented ZCS region) → ERICKSON-2166, 2167, 2170.

`CHECK-resonant-light-load-current`: inputs (Zi0, Zi∞ at fs, Vs1) → Is1(open) = Vs1/abs(Zi∞), Is1(short) = Vs1/abs(Zi0) → pass if Is1(open) ≤ Is1(short)·k (k user; the book's LCC example gives 0.268 A vs 0.278 A) → ERICKSON-2165, 2169.

`CHECK-zcs-qrs`: inputs (V1, I2 range, Lr, Cr, fs) → R0, Js = I2·R0/V1, F → pass if Js ≤ 1 at max load (ZCS) and μ ≤ 1 − Js·F/(4π); report I1pk = I2 + V1/R0 → ERICKSON-2180, 2181, 2182.

`CHECK-zvs-qrs`: inputs (V1, I2 range, Lr, Cr) → Js range → pass if Js ≥ 1 at min load (ZVS) and (1 + Js,max)·V1 ≤ Vds rating → ERICKSON-2185.

`CHECK-zvt-bridge-zvs`: inputs (Lc, n, I range, Cleg1 + Cleg2, Vg, magnetizing current iM) → ic = n·I − iM → pass if (1/2)·Lc·ic^2 ≥ (1/2)(Cleg1 + Cleg2)·Vg^2 at min load (passive-to-active leg) → margin = energy ratio; report duty loss 2·n·I·Lc/Vg per half period → ERICKSON-2188 (conf medium).

`CHECK-rcd-clamp`: inputs (Ll, i_pk at turn-off, fs, desired Vs, Vg, Vds rating) → Rs = 2·Vs^2/(Ll·i_pk^2·fs); P_Rs = Vs^2/Rs; Vds,pk = Vg + Vs → pass if Vds,pk ≤ derated Vds rating and Rs power rating ≥ P_Rs → ERICKSON-2179.

`CHECK-active-clamp`: inputs (Vg range, D range) → Vs = D·Vg/(1 − D); forward Vds,pk = Vg/(1 − D) → pass if ≤ derated rating at the worst (Vg, D) pair → ERICKSON-2190.

`CHECK-rms-piecewise`: inputs (list of segments: shape, duration, I1, I2) → rms = sqrt(Σ Dk·uk) with uk per Appendix A → used by every conduction-loss check → ERICKSON-2192, 2193, 2194.

`CHECK-core-temperature`: inputs (core type → Rth from App. B, Pfe + Pcu) → ΔT = Rth·(Pfe + Pcu) → pass if Tamb + ΔT ≤ Tmax (natural convection; Rth only where published) → ERICKSON-2196.

`CHECK-core-lookup`: inputs (required Kg or Kgfe from part-1 magnetics rules) → choose the smallest core in App. B tables with Kg (or Kgfe) ≥ required; return Ac, WA, MLT, lm → pass if a core exists in the chosen family → ERICKSON-2195 (+ part-1 ERICKSON-1176…1197).

`CHECK-winding-resistance`: inputs (AWG, n turns, MLT) → R = n·MLT·ρ(AWG) (ρ in Ω/cm from App. B.6) and wire area vs Ku·WA/n → ERICKSON-2197.

`CHECK-averaged-model-validity`: inputs (simulation corner: mode, D, V, VD) → flag CCM2/VD-based averaged results when D < 0.1, mode = DCM, or V ≲ several·VD → ERICKSON-2016, 2019.

`CHECK-opamp-compensator-gbw`: inputs (op-amp fGBW, compensator ideal G∞, converter fc) → op-amp-circuit loop crossover (e.g. fc,op ≈ sqrt(T0·f1·f4) for the PD example) and its Q → pass if fc,op well above converter fc and Qop small (ratio reported; the book shows 1 MHz → 25 kHz with Q = 4) → ERICKSON-2002, 2003, 2004 (threshold is a project choice: conf low).

## 4. Verification procedures & plots

| # | Property | Setup / stimulus | Plot (x / y) | Sweep / corners | What good looks like / pass | Source |
|---|---|---|---|---|---|---|
| V1 | CCM dc conversion and efficiency vs duty | Averaged switch subcircuit CCM2 (Ron, VD, RD, winding R) in SPICE, `.dc` on duty source | D (0.1–1) / V/Vg and η | `.step` Ron (e.g. 0, 0.5, 1 Ω); D from 0.1 (avoid d = 0 discontinuity) | Smooth M(D); η falls at low D (VD ≈ V) and at high D (conduction); choose Ron where η meets target at the operating D | §14.3.4 Figs.14.23–14.24 p.573–575 |
| V2 | Start-up stress | Switching-level SPICE (vswitch Ron/Roff, diode Is) or averaged CCM2 model, `.tran … uic` from zero state | t / iL(t), v(t) | With and without soft-start ramp; Vg max | Averaged model overlays the switching model's low-frequency envelope; peak iL, v within ratings; soft-start removes the overshoot | §14.3.5 Figs.14.26–14.28 p.576–578 |
| V3 | Control-to-output across CCM/DCM | CCM-DCM1 subcircuit, `.ac` with d̂ = 1 source, 5 Hz–50 kHz, 201 pts/decade | f / abs(Gvd) dB, ∠Gvd | Load R stepped across the mode boundary (e.g. SEPIC R = 40 Ω CCM vs 50 Ω DCM) | Compensation stable for both families of curves (CCM: resonant poles/RHP zeros; DCM: dominant single pole) | §15.4.1 Figs.15.27–15.28 p.611–614 |
| V4 | Loop gain and closed-loop rejection over load | Closed-loop averaged model (CCM-DCM1 + LIMIT PWM 0.1–0.9 + op-amp PID), voltage injection vz between compensator output and PWM input, `.nodeset` for convergence | f / abs(T), ∠T; f / abs(Gvg) open vs closed | Heavy load (CCM) and light load (DCM); line and component tolerances | fc and φm meet targets at all loads (example: 5.3 kHz/47° CCM, 390 Hz/55° DCM); closed-loop Gvg reduced by 1/(1 + T) below fc | §15.4.2 Figs.15.29–15.31 p.614–617 |
| V5 | Load-step response | Same closed-loop averaged model, load current step (e.g. 1.5 A → 5 A) | t / v(t), iLOAD(t) | Open loop (fixed d) vs closed loop | Closed loop: small (≈0.2 V in example) well-damped dip; open loop shows large undershoot and long ringing | §15.4.2 Fig.15.32 p.617–618 |
| V6 | Parasitic/extra-element impact | Compute or simulate ZN (output nulled) and ZD (input zeroed) at the element port; overlay abs(Z) | f / abs(Z), abs(ZN), abs(ZD) (dBΩ) and phases | Element value tolerance | ≥ 20 dB separation → < ±1 dB/±7° change; where curves meet with ≈180° relative phase expect resonant poles/RHP zeros | §16.1.3 Figs.16.6–16.9, 16.16, 16.21 p.631–648 |
| V7 | Input-filter compliance (impedance) | AC sim of filter output impedance Zo (source shorted); analytic or simulated ZN, ZD, Ze of converter | f / abs(Zo), abs(ZN), abs(ZD), abs(Ze) in dBΩ | Worst-case load (R/D^2 smallest), line extremes, filter tolerances | abs(Zo) below all three curves with margin (book problems: ≤ 0.2–0.4×); no undamped peak | §17.2–17.4 Figs.17.13, 17.16, 17.21, 17.29–17.30 |
| V8 | Input-filter attenuation | AC sim of filter transfer H = iin/ig | f / abs(H) dB | Filter tolerances | Attenuation at fs and harmonics ≥ requirement (e.g. 80 dB at 250 kHz example) | §17.4.5 Fig.17.31 p.704 |
| V9 | Loop gain with input filter (stability boundary) | Loop gain with filter included (modified Gvd) or minor loop Tm = Zo/Zi (Nyquist) | f / abs(T), ∠T with and without filter; Nyquist of Tm | Filter damping variants (e.g. Rf = 1.7 Ω/Cb = 29 μF vs Rf = 5.2 Ω/Cb = 8 μF) | Phase margin positive at every crossover; no −1 encirclement by Tm | §17.5 Figs.17.34–17.39, 17.46–17.48 p.706–720 |
| V10 | Closed-loop input impedance | Feedback-theorem construction Yi = Yi∞·T/(1 + T) + Yi0/(1 + T) or AC sim of closed-loop regulator input | f / abs(Zi), ∠Zi | Load, line | Zi → −R/M^2 (∠ −180°) below fc, → ZD above fc; compare with Zo of the source/filter | §17.5.2 Fig.17.45 p.716–717; §18.6.1 Eq.(18.147) |
| V11 | CPM subharmonic stability | Switching-level transient with peak-current controller; perturb iL | t / iL(t) cycle-by-cycle | D across 0.5; ramp ma = 0, 0.5·m2, m2; L tolerance | Perturbation decays by α per cycle (abs(α) < 1); no period doubling | §18.2 Figs.18.17–18.21 p.741–744 |
| V12 | CPM control-to-current (high frequency) | Sampled-data Gic(s) = ((1 − α)/(1 − α·e^(−sTs)))·(1 − e^(−sTs))/(sTs), or switching-model AC by small-signal injection | f (to fs/2) / abs(Gic), ∠Gic | Ma/M2 = 0.1, 0.5, 1, 5 | No large peaking at fs/2 (small ramp → peak); first-order averaged model acceptable to ≈fs/5 at Ma = 0.5·M2 | §18.7 Figs.18.42–18.44 p.776–779 |
| V13 | CPM vs duty-control comparison | Averaged CPM subcircuit (Rf, fs, L, Va) + CCM-DCM1 | f / abs(Gvc) vs abs(Gvd); abs(Gvg); abs(Zout) | Operating point (e.g. Vc = 1.4 V → D = 0.676) | Gvc ≈ single pole (≈ −90° wide band); Gvg ≥ 30 dB lower; Zout higher at LF without LC peak | §18.5.3 Figs.18.32–18.35 p.766–769 |
| V14 | ACM current and voltage loops | Block-diagram or averaged model; Ti = Rf·Gci·Gid/VM; Gvc with inner loop closed | f / abs(Ti), ∠Ti; abs(Gic); abs(Tv) | Line (VM), load | fci ≈ fs/10 with φm ≈ 45° or more; Gic ≈ 1/Rf below fci (peaking consistent with φm); fcv << fci | §18.9.2 Figs.18.59–18.64 p.793–797 |
| V15 | Digital loop gain | Td(jω) = H·Gvd·e^(−jω·td)·Gcd(e^(jωTs)) (MATLAB/python: c2d with 'prewarp' at fc; plant with IODelay) | f (to fs/2) / abs(Td), ∠Td vs analog T | td = D·Ts, D·Ts + Ts/2, D·Ts + Ts | Same fc as analog; φm reduced by 360·fc·td — redesign lead so digital φm meets target | §19.3 Figs.19.10–19.12 p.822–826 |
| V16 | Quantization / limit cycling | Time-domain sim with A/D (qA/D) and DPWM (nDPWM) quantizers, integral compensator | t / vc[n], v(t) after a load step (e.g. 2.5 A → 5 A) | nDPWM = 10 vs 12 (qA/D = 4 mV) | Converges to a fixed point inside the zero-error bin (no persistent oscillation); limit-cycle amplitude ≈ qA/D if conditions violated | §19.4.2 Figs.19.18–19.19 p.833–834 |
| V17 | PFC line-current quality | Long transient to steady state, then FFT of iac over one line cycle | harmonic number / % of fundamental; t / iac, v | Load (nominal and overload), line (min/max) | THD and each harmonic within limit (example DCM boost: THD 16.7% at 100 W; overload into CCM → 71%) | §21.2.2 Figs.21.9–21.11 p.877–878 |
| V18 | PFC CCM/DCM map and current shape | Plot static input characteristic jg vs mg with desired resistor line | mg = vg/V / jg = 2L·ig/(V·Ts) | Re/Rbase values, ramp ma | Line reasonably linear through origin; DCM band near zero crossings small | §21.2.1 Fig.21.6; §21.3.2 Figs.21.21–21.22 |
| V19 | PFC bulk-voltage ripple and hold-up | Transient with constant-power dc–dc load; line dropout of one cycle | t / vC(t), iac(t) | Pmax, line min | 2f ripple ≈ P/(ω·C·VC) p-p; vC stays above downstream minimum through the hold-up interval | §21.4.1 Eq.(21.93)–(21.94), Fig.21.28 |
| V20 | PFC efficiency vs line | η(VM/V) curves for Ron/Re family (Eq.21.145) plus other losses | VM/V / η | Ron/Re = 0.05…0.2; line extremes | η target met at minimum line (worst case) | §21.6 Fig.21.41 p.916 |
| V21 | Resonant converter control plane | First-harmonic M(F) or exact SRC/PRC characteristics | F = fs/f0 / M = V/Vg | Q (load) family; e.g. LLC Lp = 5Ls | Required M reachable within fs limits at all loads; avoid subharmonic/odd-DCM regions (SRC fs < f0/2) | §22.2 Figs.22.16–22.18, 22.44, 22.49–22.50, 22.57 |
| V22 | Resonant output ellipse and ZVS boundary | Voc, Isc, Zo0 from tank; overlay load lines | abs(i) / abs(v) (ellipse) with R lines; f / abs(Zi0), abs(Zi∞) and Rcrit(f) | Load range; frequency range | Operating points inside ZVS region (R < Rcrit for LCC-type, R > Rcrit for LLC-type); abs(Zi∞) > abs(Zi0) for good light-load efficiency | §22.4 Figs.22.32–22.38, 22.42–22.43 |
| V23 | Soft-switching confirmation (bench/switching sim) | Vds, id of each switch around transitions (dead time, leg capacitance) | t (ns) / vds(t), id(t) | Min and max load, line extremes | vds reaches 0 (body diode conducts) before gate turn-on; no hard-turn-on current spike; diode voltages clamped (ZVT secondary, flyback leakage) | §22.3; §23.1; §23.4 Figs.23.7, 23.29, 23.38, 23.40 |
| V24 | RMS current check from measured waveform | Scope capture of switch current; piecewise segmentation | segment table / rms | Include recovery spike | rms with spike vs without (example 3.76 A vs 2.0 A) used in conduction-loss budget | App.A Example p.1042 |

## 5. Pitfalls, failure modes, review checklist

- [ ] Op-amp compensator designed with the ideal virtual-ground formula but the op amp's finite GBW puts a high-Q resonance near the converter band (1 MHz GBW → PD circuit crossover 25 kHz, Q = 4) — check the op-amp loop. (§13.3 p.528)
- [ ] PWM-controller "op amp" is actually a transconductance amplifier with gm spread 100 μA/V–1 mA/V — compensator gain and zero move; lab oscillation. (Problem 13.3 p.541–543)
- [ ] Averaged-switch SPICE models run at d = 0 (division by zero) — clamp duty to Dmin > 0 (book sweeps from 0.1). (§14.3.1 p.568)
- [ ] Fixed-VD diode model used in DCM or at low duty where VD ≈ V — physically impossible efficiency/polarities. (§14.3.3 p.572)
- [ ] No soft-start: start-up inductor current far above steady state. (§14.3.5 p.578)
- [ ] Switch-level SPICE with ideal vswitch/diode used to predict switching loss — it cannot. (§14.3.5 p.576)
- [ ] Averaged CCM model used where ripple is large (DCM) — use the loss-free-resistor model or CCM-DCM1. (§14.1.4 p.558; §15.2)
- [ ] DCM average transistor current computed as d·<iL> — wrong; use d^2·Ts·v1/(2L). (§15.2 p.591)
- [ ] DCM converter left unloaded (power source into open circuit) — output voltage rises without bound. (§15.2 p.594)
- [ ] Loop only verified at full load; at light load (DCM) crossover collapsed from 5.3 kHz to 390 Hz and line rejection worsened. (§15.4.2 p.616–617)
- [ ] SPICE .op fails to converge in a high-gain loop — add .nodeset for V, Vref node, duty. (§15.4.2 p.616)
- [ ] Capacitor ESR ignored: adds a zero at 1/(2π·Resr·C), lowers Q, and Irms^2·ESR heating can fail the capacitor. (§16.2.2 p.637)
- [ ] SEPIC/Ćuk crossover placed above the C1 internal resonance (≈3–4 kHz in example) without Rb–Cb damping — −360° extra phase. (§16.2.4 p.644–647)
- [ ] Rb–Cb damping without dc block (Cb) or with Cb impedance not << Rb at the resonance — damping ineffective or lossy. (§16.2.4 p.647)
- [ ] Input EMI filter added after the loop was designed — undamped filter adds complex RHP zeros and −360°; regulator oscillates when fc ≥ ff. (§17.1.2 p.678)
- [ ] Input-filter resonance ff placed at (or near) the converter output-filter resonance f0 where ZD dips. (§17.3.1 p.689)
- [ ] Damping resistor placed directly across Cf — dissipates Vg^2/Rf, more than the load power. (§17.3.2 p.691)
- [ ] Damping resistor placed directly across Lf — HF roll-off degrades from −40 to −20 dB/decade. (§17.3.2 p.691)
- [ ] Filter checked only against ZN (negative resistance) but not ZD and Ze — output impedance or loop gain still disturbed. (§17.2.3 p.684–685)
- [ ] Impedance inequalities treated as the stability boundary — confirm with modified loop gain or Nyquist of Tm = Zo/Zi (multiple crossovers possible). (§17.5.1 p.708)
- [ ] Cascaded filter sections tuned to the same frequency — interaction peaks; stagger-tune (section nearest the converter lowest). (§17.4.4–17.4.5 p.700–702)
- [ ] Constant-power (negative-resistance) loading ignored when a regulated converter is fed from a long line/battery with inductance. (§17.2.2 p.682–684)
- [ ] CPM without slope compensation at D > 0.5 — period doubling/chaos; also check D at min line and with inductance tolerance. (§18.2 p.740–741; Problem 18.5)
- [ ] CPM current sense unfiltered/no blanking — diode-recovery spike resets the latch; blanking limits minimum duty. (Ch.18 intro p.727)
- [ ] Large sensing noise with tiny ramp — duty jitter; increase ramp above ripple. (§18.2 p.745–746)
- [ ] CPM full bridge with a series dc-blocking capacitor, or CPM half-bridge isolated buck — destabilizes. (Ch.18 intro p.727)
- [ ] ACM clamp on vc assumed to protect switches — it limits only average current; add cycle-by-cycle peak limit. (§18.9 p.789)
- [ ] Averaged CPM model trusted near fs/2 with small ramp — sampled-data peaking/instability not predicted; use Qhf or the Fm/(1 + s/ωx) extension. (§18.7 p.773–779)
- [ ] DCM CPM buck with ma = 0 and M > 2/3 — low-frequency instability (two equilibria). (§18.8 p.784)
- [ ] Digital loop delay (A/D + compute + modulator) not budgeted — phase cost 360°·fc·td: 13° for 0.36 μs, 31° for 0.86 μs, 49° for 1.36 μs at fc = 100 kHz. (§19.3 p.822–823)
- [ ] Analog HF roll-off pole mapped into the digital compensator instead of the anti-alias filter. (§19.2.3 p.820–821)
- [ ] Bilinear mapping without prewarp for corners near fs/2 — phase error at crossover. (§19.2.3 p.819–820)
- [ ] Integrator without anti-windup limit (vc must stay within DPWM range 0–1). (§19.4.1 p.828)
- [ ] DPWM LSB (Gd0·H0·qDPWM) ≥ A/D LSB, or KI ≥ 1/(Gd0·H0) — no equilibrium, limit cycling. (§19.4.2 p.832–835)
- [ ] Sampling the output at switching edges — aliasing noise into the dc regulation error. (§19.1.2 p.810–811)
- [ ] Counter DPWM resolution assumed without checking fclk = 2^n·fs (13 bits at 1 MHz needs 8.192 GHz). (§19.1.1 p.809)
- [ ] Power factor treated as cos φ when currents are distorted — use DF × displacement factor. (§20.3.2 p.855)
- [ ] Neutral conductor sized like the phase conductors with nonlinear balanced loads — triplen harmonics add (20% h3 → 60% neutral current). (§20.5.1 p.860–861)
- [ ] PF-correction capacitors rated only on nameplate kVAR — harmonic currents raise rms and ESR heating. (§20.5.3 p.862–863)
- [ ] Boost PFC output set below the peak line voltage (V < VM) — cannot shape current. (§21.2.1 p.872)
- [ ] Boost PFC without inrush limiting — uncontrolled capacitor charging current through the boost diode. (§21.4.1 p.897; §21.5.2 p.908)
- [ ] PFC voltage loop too fast (gain at 2·f_line) — line-current distortion. (§21.4.1 p.898–899)
- [ ] Open-loop DCM boost/flyback PFC overloaded into CCM near the line peak — THD jumps (16.7% → 71%). (§21.2.2 p.877)
- [ ] CPM PFC designed at one line voltage — universal input gives 20–50% THD at high line. (§21.3.2 p.888–889)
- [ ] CrM PFC switching frequency range not checked — fs spans VM^2/(4LP) down to that×(1 − VM/V). (§21.3.3 p.891)
- [ ] PFC voltage-loop plant modeled as a single pole with a constant-power downstream converter — it is an integrator (except NLC). (§21.4.2 p.904–905)
- [ ] SRC operated far below resonance — subharmonic and odd-DCM modes (uncontrollable M = 1/k); first-harmonic model invalid. (§22.2.1–22.2.2 p.946–947; §22.5.1 p.979)
- [ ] Resonant tank chosen where abs(Zi∞) < abs(Zi0) (parallel/LCC above fm) — large circulating current at light load. (§22.4.2 p.961)
- [ ] ZCS operation (below resonance) chosen for MOSFET bridges — hard turn-on (Qrr, Coss) remains; prefer ZVS. (§22.3.1 p.953–954)
- [ ] ZVS bridge without dead time/leg capacitance at turn-off (IGBTs need external C). (§22.3.2 p.955)
- [ ] LLC operated between f∞ and f0 at heavy load (R < Rcrit) — ZCS instead of ZVS. (§22.4.5 p.972)
- [ ] ZCS diode turn-off in resonant/ZCS cells — ringing raises peak inverse voltage; snubber or ZVS alternative. (§23.1.1 p.999)
- [ ] Flyback leakage ringing without clamp — Vds exceeds D·Vg/D' + Vg. (§23.1.2 p.1001)
- [ ] ZVS quasi-resonant switch over a wide load range — Vpk = (1 + Js)·V1 up to 6× for 5:1 load; ZVS lost at light load. (§23.3.1 p.1018)
- [ ] ZCS quasi-resonant switch at loads with Js > 1 — ZCS lost; peak current ≥ 2× load current. (§23.2.1 p.1008; §23.3 p.1016)
- [ ] Phase-shift ZVT bridge at light load — passive-to-active leg loses ZVS unless Lc energy (or magnetizing current) suffices; secondary diodes ring above 2n·Vg. (§23.4.1 p.1028)
- [ ] ARCP main switch gated late — ringing continues and ZVS is lost; current boost adds conduction loss. (§23.4.3 p.1033)
- [ ] Switch rms computed without the diode-recovery spike (3.76 A vs 2.0 A in example). (App.A p.1042)
- [ ] Core temperature estimated from Rth under forced air or unusual loss distribution — Rth values are natural-convection centre-leg estimates. (App.B p.1043)
- [ ] AWG table values used blindly — printed anomalies at AWG 13 (resistance), 14 (area), 33 (diameter); diameter column is not bare copper. (App.B.6 p.1049–1050)

## 6. Standards referenced

The chapters in this range cite regulations only generically (conducted-EMI limits, §17.1.1; "several international standards" limiting line-current harmonics, Ch.20 intro and §21.2.1) and give no clause or table numbers. The only standard-type documents identified in the bibliography for this range are:

| Standard / document | Edition / year | Clause / table | What it governs (as used in the book) | Where cited |
|---|---|---|---|---|
| MIL-HDBK-241B, "Design guide for electromagnetic interference (EMI) reduction in power supplies", U.S. Department of Defense | April 1981 | not given | Conducted-EMI reduction / input-filter design guidance for switching power supplies | Ref.[144], cited in §17.1.1 p.676 (limits on switching-harmonic currents injected into the source) |
| EMC Directive 89/336/EEC (via C. Marsham, "The Guide to the EMC Directive 89/336/EEC", IEEE Press) | 1992 guide | not given | European EMC compliance framework for conducted emissions | Ref.[145], cited in §17.1.1 p.676 |
| (unnamed) utility/equipment line-current harmonic standards | — | — | Limits on ac line-current harmonic magnitudes for motor drives, ballasts, office-equipment supplies | Ch.20 intro p.849; §21.2.1 p.875 (no specific standard named) |

Numerical requirement quoted in the text (not tied to a named standard): harmonic currents typically limited to 10–100 μA → ≥ 80 dB input-filter attenuation (§17.1.1 p.676).

## 7. Process / lifecycle guidance

This book is an analysis/design text, not a product-lifecycle text. The design-flow guidance it does give, as stage → activity → deliverable → exit criterion:

| Stage | Activity | Deliverable | Exit criterion | Source |
|---|---|---|---|---|
| Power-stage design | Choose topology (indirect-power fraction, stresses, inrush), size L, C, devices from rms tables | Power-stage schematic + stress table | Device rms/peak within ratings at worst-case line/load (Table 21.3, App. A) | §14.1.4; §21.5; App.A |
| Averaged modeling | Replace switches with CCM/CCM-DCM/CPM averaged subcircuits; ac sweeps | Bode plots of Gvd/Gvc, Gvg, Zout over load | Plant understood at all loads incl. DCM | §14.3; §15.4; §18.5 |
| Controller design | Compensator per Ch.9 (analog) or map to z-domain with delay (digital) | Compensator values / z-coefficients | fc, φm targets met at all corners (incl. light load, digital delay) | §15.4.2; §18.6; §19.3 |
| Input-filter design | Filter for EMI attenuation, then damp/optimize against ZN, ZD, Ze | Filter schematic + Zo plot | Attenuation met and abs(Zo) well below ZN, ZD (, Ze); loop gain with filter still stable | §17.2–17.5 |
| Design verification | Worst-case/tolerance/temperature/aging simulation; start-up and load-step transients | Worst-case report | Specs met under all expected parameter ranges; iterate until yield acceptable | §14.3 p.566–567; §15.4.2 p.618 |
| Implementation (digital) | Realize cascade/parallel PID with anti-windup; choose A/D, DPWM resolution | Firmware/HDL + resolution budget | No-limit-cycle conditions met; word lengths avoid overflow | §19.4 |

## 8. Coverage log

Source file: refs-text/Erickson_Maksimovic_Fundamentals_of_Power_Electronics_2020.txt (68,610 lines). Assigned range: lines 34300–68610 (from §13.3 p.525). Reading started at line 34280 (20-line overlap with part 1) after orienting on the front matter / TOC (lines 1–130, read in 60–70-line chunks because TOC lines reach 3,300 characters).

Read in order with the Read tool (chunks of 1,000–1,300 lines; no chunk was truncated):

| lines | content | rule ids |
|---|---|---|
| 34280–35551 | §13.3 op-amp PD example (from p.525), §13.4 closed-loop buck regulator via feedback theorem, §13.5 key points, Problems 13.1–13.9 | 2001–2009 |
| 35552–37310 | Ch.14 circuit averaging, averaged switch models, indirect power, CCM1/CCM2 SPICE subcircuits, SEPIC and buck–boost simulation examples, Problems 14.1–14.11 | 2010–2023 |
| 37311–40089 | Ch.15 DCM dynamics, loss-free resistor, Tables 15.1–15.4, CCM-DCM1 subcircuit, SEPIC and buck regulator simulations, high-frequency DCM dynamics, Problems 15.1–15.7 | 2024–2044 |
| 40090–43835 | Ch.16 EET (basic result, derivation, impedance inequalities), ESR and SEPIC examples, SEPIC damping, n-EET, two-section and bridge-T filters, frequency inversion, Problems 16.1–16.8 | 2045–2055 |
| 43836–46382 | Ch.17 conducted EMI, modified transfer functions, Table 17.1, buck example, damping, optimal Rf–Cb / Rf–Lb damping, cascaded sections, two-stage example, stability via modified loop gain and minor loop Tm, Problems 17.1–17.11 | 2056–2077 |
| 46383–52335 | Ch.18 CPM simple model, D > 0.5 oscillation and slope compensation, accurate model (Tables 18.2–18.5), CPM with input filter, CPM simulation subcircuit, voltage loop design, sampled-data model, DCM CPM (Table 18.6), average current-mode control and boost example, Problems 18.1–18.12 | 2078–2107, 2198 |
| 52336–54498 | Ch.19 digital control: A/D and DPWM quantization, delays, z-transform, integrators, Tustin/prewarp mapping, design example, realization, quantization/limit cycles, ΔΣ DPWM, Problems 19.1–19.10 | 2108–2123, 2199 |
| 54499–55638 | Ch.20 average power, rms, power factor, THD, peak-detection rectifier, three-phase harmonics, PFC capacitors, Problems 20.1–20.6 | 2124–2132 |
| 55639–60645 | Ch.21 ideal rectifier, boost/DCM boost/DCM flyback PFC, ACC/CPM/CrM/NLC control, energy storage, outer-loop model, rms stresses (Tables 21.2–21.3), efficiency with Ron, three-phase rectifiers, Problems 21.1–21.16 | 2133–2155, 2200 |
| 60646–64628 | Ch.22 sinusoidal approximation, SRC/PRC, subharmonics, ZCS/ZVS, output ellipse, Theorems 22.1–22.2, LCC and LLC examples, Table 22.1, exact SRC/PRC characteristics, Problems 22.1–22.11 | 2156–2174 |
| 64629–67214 | Ch.23 soft-switching mechanisms of diodes/MOSFETs/IGBTs, ZCS quasi-resonant switch (half/full wave), ZVS QRS, multiresonant, quasi-square-wave, ZVT full bridge, active clamp, ARCP, Problems 23.1–23.7 | 2175–2191 |
| 67215–67590 | Appendix A rms formulas and piecewise example | 2192–2194 |
| 67591–67976 | Appendix B Kg/Kgfe definitions, pot/EE/EC/ETD/PQ core tables, AWG table | 2195–2197 |
| 67977–68610 | References (scanned with grep for standards/regulations) and index (skipped) | — |

Rule count: 200 rules, ERICKSON-2001 … ERICKSON-2200 (2198–2200 are addenda drawn from problem statements, appended after the appendix rows).

Skipped / summarized (with reason):
- End-of-chapter problems: read; transcribed only where they state design margins or specifications usable as checks (13.3, 13.8, 14.11, 16.2, 17.1–17.11, 18.1, 18.5, 19.1, 19.4–19.5, 21.10) — tagged medium.
- Long derivations summarized as results only: feedback-theorem and EET derivations, n-EET coefficient tables (16.1, 16.3, 16.4 procedures), sampled-data derivation of Gic, SRC/PRC state-plane solutions, ZCS QRS subinterval algebra.
- Index skipped per brief; references scanned only for standards (section 6).

Extraction limitations:
- Figures are not in the text; graph-derived items (Figs.14.24, 14.28, 15.28, 16.21–16.26, 17.24–17.26, 18.42–18.44, 19.10, 19.18–19.19, 20.7, 21.9–21.11, 21.41, 22.44, 22.49–22.57, 23.16, 23.19, 23.27, 23.32, 23.35) are represented by captions and the numeric anchors stated in the prose.
- OCR flattened fractions, primes (D'), square roots and minus signs. Reconstructed items (tagged medium) were re-derived and, where the book gives numbers, checked numerically with a scratch script (all pass): Table 15.2 buck/boost g1 signs; SEPIC Gvd−bb parameters (711 Hz, Q 4.9, 4.5 kHz reproduced); optimal-damping radicals (n = 2.5, Rf = 0.67 Ω; R0f1 = 2.12 Ω, R1 = 1.9 Ω reproduced); boost-PFC F(a) closed form (matches numeric integral; fit within 0.1% for a ≤ 0.15); digital PID prewarp mapping (zL, zz, zp, Gd reproduced); LCC design numbers; all Appendix-B Kg entries vs Ac^2·WA/MLT (worst mismatch 0.32%); u(2.7) = 0.305; Appendix-A example 3.76 A.
- Items whose OCR could not be fully recovered are described with that caveat: Table 18.1 buck–boost row, Table 18.6 buck–boost Icrit, exact PRC equations (Eq.22.103–22.106), Rf–Lb series-damping Qopt, ETD Rth/weight column assignment, Table 21.3 non-boost rows.
- Book typos/inconsistencies noted and not propagated: "C3 = 2.7 kΩ" (nF, §15.4.2); Eq.(21.152) prints 4.38 A instead of IQrms = 3.48 A in the denominator; LCC example "L = 1.96 μH" (mH) and "Cp = 1 nF"/"Xp = −1499 Ω" vs 1.06 nF/−1493 Ω; digital example "Gcm = 5.45" while the book's own script (and its z-coefficients) use 5.2375; Theorem 22.2 case list and one §22.4.3 sentence swap ZVS/ZCS phases; §21.4.1 says a 100 μF/100 V capacitor stores 1 J (½CV² = 0.5 J) — not used; §21.4.2 states R∥r2 = r2/2 for NLC, inconsistent with the tabulated r2 = V^2/(2Pav) — rule 2146 only states that NLC keeps a finite pole.
- No explicit standard clause numbers exist in this range (section 6 lists the only standard-type references found).
