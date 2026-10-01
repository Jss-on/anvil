# Fundamentals of Power Electronics (3rd ed.), part 1 — Anvil rulebook

## 0. Citation

R. W. Erickson and D. Maksimović, *Fundamentals of Power Electronics*, 3rd ed. Cham, Switzerland: Springer Nature Switzerland AG, 2020. ISBN 978-3-030-43879-1 (print), ISBN 978-3-030-43881-4 (eBook), doi:10.1007/978-3-030-43881-4. (1st ed. © Springer Science+Business Media Dordrecht 1997; 2nd ed. © Kluwer Academic Publishers 2001.)

Chapters covered by THIS extraction (source text lines 1–34300):
- Front matter and table of contents (orientation).
- Part I Converters in Equilibrium: Ch.1 Introduction; Ch.2 Principles of Steady-State Converter Analysis; Ch.3 Steady-State Equivalent Circuit Modeling, Losses, and Efficiency; Ch.4 Switch Realization; Ch.5 The Discontinuous Conduction Mode; Ch.6 Converter Circuits.
- Part II Converter Dynamics and Control: Ch.7 AC Equivalent Circuit Modeling; Ch.8 Converter Transfer Functions; Ch.9 Controller Design.
- Part III Magnetics: Ch.10 Basic Magnetics Theory; Ch.11 Inductor Design; Ch.12 Transformer Design.
- Part IV (partial): Ch.13 Techniques of Design-Oriented Analysis: The Feedback Theorem, §13.1–13.3 (through printed p.525).

Chapters NOT read by this extraction (assigned to the part-2 extraction, source lines 34301–68610): remainder of §13.3, §13.4–13.5; Ch.14 Circuit Averaging, Averaged Switch Modeling, and Simulation; Ch.15 DCM equivalent-circuit modeling; Ch.16 Extra Element Theorems; Ch.17 Input Filter Design; Ch.18 Current-Programmed Control; Ch.19 Digital Control; Ch.20 Power and Harmonics in Nonsinusoidal Systems; Ch.21 PWM Rectifiers; Ch.22 Resonant Conversion; Ch.23 Soft Switching; Appendix A (rms values of waveforms), Appendix B (magnetics design tables, AWG), references, index.

## 1. Design rules

Notation (author's, used throughout): D = duty cycle (fraction of Ts that the switch is in position 1 / transistor on), D' = 1 − D, Ts = 1/fs switching period, Vg = dc input voltage, V = dc output voltage, I = dc inductor current, R = load resistance. **Erickson's ripple symbols are PEAK (peak-to-average) values: ΔiL and Δv are HALF the peak-to-peak ripple** (p-p = 2ΔiL, 2Δv). M(D) = V/Vg. CCM = continuous conduction mode, DCM = discontinuous conduction mode.

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| ERICKSON-1001 | power | Converter efficiency definition | η = Pout/Pin; Ploss = Pin − Pout | Pout, Pin (W) | Any power converter | calc | §1.1 Eq.(1.1) p.2 | high |
| ERICKSON-1002 | thermal | Converter quality factor Q = output power per watt of loss; for a fixed cooling capacity (max Ploss) the max output power scales with Q, so raise η to raise Pout | Q = Pout/Ploss = η/(1 − η); e.g. η = 90% → Ploss = 11% of Pout, Pout/Ploss = 9 | η | Thermal/cooling budget sizing; max Pout usually set by cooling system's heat removal | calc | §1.1 Eq.(1.2), Fig.1.3 p.2–3 | high |
| ERICKSON-1003 | power | Dissipative (voltage-divider / series-pass linear) regulation loses ≈ (Vg − V)·I; linear series-pass regulators are used today only at a few watts | Ploss ≈ (Vg − V)·Iout; example Vg = 100 V, V = 50 V, I = 10 A → Ploss ≈ 500 W, Pin ≈ 1000 W, η ≈ 50% | Vg, V, Iout | Linear regulator vs switcher selection; "generally find modern application only at low power levels of a few watts" | calc | §1.1 Fig.1.7 p.4 | high |
| ERICKSON-1004 | power | DC component of the switch output (buck switch node) equals duty cycle × input | Vs = <vs> = (1/Ts)·∫0..Ts vs dt = D·Vg; 0 ≤ D ≤ 1 | D, Vg | Ideal SPDT switch, periodic | calc | §1.1 Eq.(1.3); §2.1 Eq.(2.2) p.16 | high |
| ERICKSON-1005 | filter | PWM output low-pass filter corner frequency must be much lower than the switching frequency so only the dc component of vs(t) reaches the load | f0 = 1/(2π·sqrt(L·C)) << fs (text gives no numeric factor) | L, C, fs | Buck-type LC output filter | calc | §1.1 p.6; §2.1 p.16 | high |
| ERICKSON-1006 | power | Typical switching-frequency range | fs = 1/Ts generally 1 kHz – 1 MHz, set by semiconductor switching speed; laptop/portable dc–dc typically several hundred kHz | fs | General guidance (Si devices) | review | §2.1 p.15; §1.2 p.8 | high |
| ERICKSON-1007 | power | Ideal CCM dc conversion ratios of the basic converters | buck M = D; boost M = 1/(1 − D); buck–boost M = −D/(1 − D); Ćuk M = −D/(1 − D) (full list in §2 table) | D | Ideal, CCM, steady state | calc | Fig.2.5 p.17; Eq.(2.35) p.27; Eq.(2.53), Fig.2.23 p.33 | high |
| ERICKSON-1008 | power | Output switching ripple specification example (computer supply) | 3.3 V output: ripple normally required < a few tens of mV, i.e. < 1% of V | V, Δv_pp | Typical requirement quoted for a computer power supply | measure | §2.2 p.19 | high |
| ERICKSON-1009 | power | Small-ripple (linear-ripple) approximation is valid only for inductor currents and capacitor voltages (continuous state variables) and only when ripple << dc value and Ts << circuit natural time constants; never apply it to switch voltage, switch current or inductor voltage | v(t) ≈ V when abs(v_ripple) << V; iL(t) ≈ I when ΔiL << I | ripple, dc value | All steady-state PWM analysis in this rulebook | review | §2.2 Eq.(2.5)–(2.6) p.19; Key pt 3 p.37 | high |
| ERICKSON-1010 | power | Inductor volt-second balance: in periodic steady state the average inductor voltage is zero (net flux-linkage over Ts = 0); use it to solve dc voltages of any converter | <vL> = (1/Ts)·∫0..Ts vL(t) dt = 0 | vL(t) per subinterval | Any converter in equilibrium | calc | §2.2 Eq.(2.19)–(2.20) p.23 | high |
| ERICKSON-1011 | power | Capacitor charge (amp-second) balance: in steady state the average capacitor current is zero; use it to solve dc inductor currents | <iC> = (1/Ts)·∫0..Ts iC(t) dt = 0 | iC(t) per subinterval | Any converter in equilibrium | calc | §2.2 Eq.(2.27) p.24 | high |
| ERICKSON-1012 | power | Buck inductor current ripple (peak, = half p-p) | ΔiL = (Vg − V)·D·Ts/(2·L)  [A]; peak inductor/switch current = I + ΔiL | Vg, V (V), D, Ts (s), L (H) | Buck, CCM, small ripple | calc | §2.2 Eq.(2.15) p.21 | high |
| ERICKSON-1013 | magnetics | Buck inductance selection for a target peak ripple | L = (Vg − V)·D·Ts/(2·ΔiL)  [H] | Vg, V, D, Ts, ΔiL | Buck, CCM | calc | §2.2 Eq.(2.16) p.22 | high |
| ERICKSON-1014 | power | Typical inductor-ripple design target: peak ripple ΔiL = 10–20% of the full-load dc current; larger ripple increases peak currents, size and cost of inductor and semiconductors | 0.10 ≤ ΔiL/I_fullload ≤ 0.20 | ΔiL, I | CCM filter inductors (buck-type); typical, not a hard limit | calc | §2.2 p.21 | high |
| ERICKSON-1015 | derating | Semiconductor devices carry the inductor peak current; device current ratings must be specified from the peak, not the average | I_switch,pk = I + ΔiL | I, ΔiL | All converters | calc | §2.2 p.21 | high |
| ERICKSON-1016 | power | Boost steady state: output and inductor (= input) dc current | V = Vg/D'; I = V/(D'·R) = Vg/(D'^2·R) | Vg, D, R | Boost, ideal, CCM | calc | §2.3 Eq.(2.34)–(2.39) p.27–28 | high |
| ERICKSON-1017 | power | Boost inductor current ripple (peak) | ΔiL = Vg·D·Ts/(2·L) → L = Vg·D·Ts/(2·ΔiL) | Vg, D, Ts, L | Boost, CCM | calc | §2.3 Eq.(2.43) p.29 | high |
| ERICKSON-1018 | power | Boost output voltage ripple (pulsating capacitor current; capacitor alone supplies load during DTs) | Δv = V·D·Ts/(2·R·C) → C = V·D·Ts/(2·R·Δv) | V, D, Ts, R, C | Boost, CCM; ESR ripple not included | calc | §2.3 Eq.(2.47) p.29 | high |
| ERICKSON-1019 | power | Boost efficiency falls rapidly at high duty cycle because inductor current Vg/(D'^2 R) grows without bound as D → 1 | avoid operating near D → 1 | D | Boost with any loss elements | review | §2.3 p.28 | high |
| ERICKSON-1020 | power | Ćuk converter dc quantities | V1 = Vg/D'; V2 = −(D/D')·Vg; I1 = (D/D')^2·Vg/R; I2 = −(D/D')·Vg/R | Vg, D, R | Ćuk, ideal, CCM (V1 = coupling cap voltage) | calc | §2.4 Eq.(2.53) p.33 | high |
| ERICKSON-1021 | power | Ćuk ripple magnitudes (peak) for L1, L2, C1 selection | Δi1 = Vg·D·Ts/(2·L1); Δi2 = Vg·D·Ts/(2·L2); Δv1 = Vg·D^2·Ts/(2·D'·R·C1) | Vg, D, Ts, R, L1, L2, C1 | Ćuk, CCM | calc | §2.4 Eq.(2.57) p.34 | high |
| ERICKSON-1022 | filter | Output-voltage ripple of a two-pole LC output filter (buck, Ćuk output) from charge q in positive half of the triangular capacitor current | Δv = ΔiL·Ts/(8·C) (peak; p-p = 2Δv) → C = ΔiL·Ts/(8·Δv); add ESR ripple separately | ΔiL, Ts, C | Requires abs(Z_C(fs)) << R so all ripple current flows in C; triangular iL ripple | calc | §2.5 Eq.(2.58)–(2.60) p.36 | high |
| ERICKSON-1023 | power | In converters whose output capacitor (or an inductor) sees a non-pulsating waveform, the small-ripple approximation predicts zero ripple — compute that element's ripple from the inductor current ripple (charge) or capacitor voltage ripple (flux linkage) instead | use ERICKSON-1022 / ERICKSON-1024 | — | Buck output, Ćuk output, LC input filters | review | §2.5 p.35; Key pt 7 p.38 | high |
| ERICKSON-1024 | filter | Input-filter inductor current ripple when it sees the triangular ripple of the input-filter capacitor (dual of Eq.2.60, flux linkage λ = L·2Δi, λ = Δv·Ts/4) | Δi_L1 = Δv_C1·Ts/(8·L1) | Δv_C1, Ts, L1 | Two-pole LC input filter on a pulsating-input converter; linear capacitor ripple | calc | §2.5 Fig.2.27 p.37 (derivation left to reader) | medium |
| ERICKSON-1025 | power | DC transformer model: in equilibrium an ideal converter behaves as a lossless dc transformer of turns ratio M(D); relations hold only in dc steady state (not during transients) | V = M(D)·Vg; Ig = M(D)·I; Vg·Ig = V·I | M(D), Vg, I | Ideal CCM converter | calc | §3.1 Eq.(3.1)–(3.4) p.43–44 | high |
| ERICKSON-1026 | power | For ideal PWM converters in CCM with equal numbers of independent inductors and capacitors, M is a function of D only and independent of load | M = M(D) | — | CCM only (DCM M depends on load, see ERICKSON-1073…1086) | review | §3.1 p.44 | high |
| ERICKSON-1027 | power | A source resistance R1 in front of a converter appears at the output multiplied by M^2 | V = M(D)·V1·R/(R + M^2(D)·R1) | V1, R1, M, R | DC transformer model | calc | §3.1 Eq.(3.5) p.46 | high |
| ERICKSON-1028 | power | Boost with inductor winding resistance RL: conversion ratio, current, efficiency | V/Vg = (1/D')·1/(1 + RL/(D'^2·R)); I = [Vg/(D'^2·R)]·1/(1 + RL/(D'^2·R)); η = 1/(1 + RL/(D'^2·R)) | D, RL, R, Vg | Boost, CCM, only copper loss | calc | §3.2–3.3 Eq.(3.14), (3.19), (3.23) p.48–52 | high |
| ERICKSON-1029 | power | Inductor DCR caps the maximum boost ratio: with RL/R = 0.02 the maximum V/Vg ≈ 3.5; V/Vg = 5 requires RL < 1% of R. Analytic peak of Eq.(3.14) at D' = sqrt(RL/R) | M_max = 0.5·sqrt(R/RL) (at D' = sqrt(RL/R)) | RL, R | Boost with copper loss only | calc | §3.2 Fig.3.9 p.49 (analytic max derived) | medium |
| ERICKSON-1030 | power | At D → 1 a boost with RL delivers V → 0 and η → 0, dissipating ≈ Vg^2/RL in the winding — duty-cycle limit/clamp needed | P_RL → Vg^2/RL at D = 1 | Vg, RL | Boost | review | §3.2 p.48–49 | high |
| ERICKSON-1031 | power | For high boost efficiency keep inductor resistance much smaller than the load resistance referred to the primary of the dc transformer; easier at low D | RL << D'^2·R | RL, R, D | Boost | calc | §3.3.4 p.52–53 | high |
| ERICKSON-1032 | power | Buck with winding resistance: dc model is a 1:D dc transformer plus RL; input current is the average of the pulsating input current | VC = D·Vg·R/(R + RL); Ig = D·IL | D, Vg, RL, R | Buck, CCM (Fig.3.21) | calc | §3.4 Eq.(3.24)–(3.26), Fig.3.21 p.54–56 | medium |
| ERICKSON-1033 | components | Semiconductor conduction-loss models: MOSFET (and BJT) ≈ on-resistance Ron; diode, IGBT, thyristor ≈ forward voltage source VD plus on-resistance RD (RD may be omitted when modelling one operating point) | v_on = I·Ron (MOSFET); v_on = VD + I·RD (diode/IGBT/SCR) | Ron, VD, RD | Averaged dc loss modelling | calc | §3.5 p.56 | high |
| ERICKSON-1034 | power | Boost with RL, MOSFET Ron, diode VD+RD: conversion ratio and efficiency | V/Vg = (1/D')·(1 − D'·VD/Vg)/(1 + (RL + D·Ron + D'·RD)/(D'^2·R)); η = (1 − D'·VD/Vg)/(1 + (RL + D·Ron + D'·RD)/(D'^2·R)) | D, Vg, R, RL, Ron, VD, RD | Boost, CCM, small ripple | calc | §3.5 Eq.(3.33)–(3.35) p.58–59 | high |
| ERICKSON-1035 | power | Boost high-efficiency conditions | Vg/D' >> VD AND D'^2·R >> RL + D·Ron + D'·RD | as above | Boost | calc | §3.5 Eq.(3.36) p.59 | high |
| ERICKSON-1036 | power | Duty-weighted conduction loss: a device conducting for fraction D of Ts dissipates D·I^2·Ron (MOSFET) or D'·(VD·I + I^2·RD) (diode conducting D'Ts); model element values D·Ron, D'·RD, D'·VD | P_Q = D·I^2·Ron; P_D = D'·I·VD + D'·I^2·RD | D, I, Ron, VD, RD | Small inductor ripple | calc | §3.5 p.59 | high |
| ERICKSON-1037 | power | Ripple correction for conduction loss (Table 3.1, buck MOSFET): the averaged model underestimates loss by the rms factor | Irms = I·sqrt(D)·sqrt(1 + (ΔiL/I)^2/3); loss = D·I^2·Ron·(1 + (ΔiL/I)^2/3); ΔiL = 0.1I → ×1.0033 loss (rms ×1.00167); ΔiL = I → ×1.3333 loss (rms ×1.155) | ΔiL/I, D, I, Ron | Triangular ripple on dc; general formula derived from the table | calc | §3.5 Table 3.1, Fig.3.29 p.60 | medium |
| ERICKSON-1038 | power | Resistive loss must be computed from rms current, P = Irms^2·R; averaged (dc) models give correct losses only when ripple is small | P_R = Irms^2·R | Irms, R | Loss budgeting | calc | §3.5 p.59–60 | high |
| ERICKSON-1039 | components | Realize each SPST switch from its operating quadrant over ALL intended operating points: blocks +v and conducts +i → transistor (BJT/IGBT/MOSFET); blocks −v and conducts +i → diode (e.g. buck: Q blocks +Vg, diode blocks −Vg; needs Vg > 0 and iL > 0) | compare sign(v_off), sign(i_on) of each switch | switch off-state voltage, on-state current | All PWM converters | review | §4.1.1 p.69–72; Key pts 1–2 p.126 | high |
| ERICKSON-1040 | components | Two-/four-quadrant switches: current-bidirectional = transistor + antiparallel diode (inverters, bidirectional chargers); voltage-bidirectional = transistor + series diode (blocks −v up to diode rating, +v up to transistor rating; SCR is inherently this type); four-quadrant = back-to-back or antiparallel pairs (matrix converters) | — | required quadrants | Inverters, bidirectional dc–dc, cycloconverters | review | §4.1.2–4.1.4 p.72–77 | high |
| ERICKSON-1041 | components | MOSFET body diode is slower than the channel; if it conducts, its reverse recovery causes high peak currents that some MOSFETs are not rated for (failure, parasitic-BJT latch-up). Either add external series + antiparallel fast diodes (Fig.4.10b) or use MOSFETs rated for fast-recovery body-diode conduction at rated current, and budget the body-diode recovery switching loss | — | body-diode rating, Qrr | Half-bridges, synchronous rectifiers, inverters | review | §4.1.2 p.72–73; §4.4.1 p.101 | high |
| ERICKSON-1042 | power | Half-bridge from ± Vg supplies (Fig.4.11): output vs duty; switches must block 2Vg; sinusoidal PWM duty law | v0 = (2D − 1)·Vg; iL = (2D − 1)·Vg/R; V_block = 2·Vg; D(t) = 0.5 + Dm·sin(ωt), Dm < 0.5 | D, Vg, R | Two-quadrant (current-bidirectional) switches required | calc | §4.1.2 Eq.(4.1)–(4.3) p.73–74 | high |
| ERICKSON-1043 | power | Synchronous rectifier replaces the freewheeling diode; its loss Irms^2·Ron can be lowered by a larger die, whereas diode conduction loss (VF·I) is fixed by junction potential and is "easily the largest source of loss" in sub-3.3 V supplies | P_SR = Irms^2·Ron vs P_D = VF·I_D,avg | Ron, Irms, VF | Low-voltage, high-current outputs; Q2 driven with complement of Q1 | calc | §4.1.5 p.78–79 | high |
| ERICKSON-1044 | components | Device-class tradeoff: majority-carrier devices (MOSFET, Schottky) switch fast (capacitance charging) but Ron/VF rise quickly with breakdown voltage; minority-carrier devices (BJT, IGBT, SCR, GTO) give low drop at high voltage but switch slowly (stored charge) → majority carriers at lower voltage/higher fs | — | V rating, fs | Device selection | review | §4.2.1 p.79–80; Key pts 5–6 p.127 | high |
| ERICKSON-1045 | components | Voltage-class device map: Si MOSFET device of choice up to ≈600 V (typical switching times < 100 ns); above 600 V IGBT historically preferred; SiC MOSFET for > 600 V (600 V–10 kV); GaN FETs at ≤ 600–650 V; Si superjunction MOSFETs best at 500–800 V; BJT displaced by MOSFET (≤ 600 V) and IGBT (≥ 600 V) | — | V_rating | Technology selection | review | §4.4.1 p.103; §4.4.2 p.103–106; §4.5.1 p.115 | high |
| ERICKSON-1046 | power | Hard-switched clamped-inductive-load transistor loss (piecewise-linear edges; voltage and current do not change simultaneously, peak instantaneous power Vg·iL) | W_off = 0.5·Vg·iL·(t2 − t0); W_on = 0.5·Vg·iL·t_on; P_sw = (W_on + W_off)·fs | Vg, iL, edge times, fs | Ideal diode, no Coss/Qr (add ERICKSON-1052/1059) | calc | §4.2.2 Eq.(4.5)–(4.6) p.82 | high |
| ERICKSON-1047 | components | Diode reverse-recovery metrics: tr (t0→t4), recovered charge Qr (area of negative current); peak reverse current may be several times Ion; Qr falls when turn-off di/dt is reduced; softness S = (t4 − t2)/(t2 − t0) — soft diodes (large S) lower dv/dt and EMI, snappy diodes (small S) the opposite | S = (t4 − t2)/(t2 − t0) | tr, Qr, di/dt | p–n rectifiers | measure | §4.3.1 Eq.(4.11) p.87 | high |
| ERICKSON-1048 | components | Rectifier class selection: standard-recovery rectifiers are for 50/60 Hz only (tr unspecified); converters need fast- or ultrafast-recovery parts (tr, Qr specified); Schottky has negligible stored charge (model by junction capacitance) | — | tr, Qr | Diode choice | review | §4.3.2 p.88 | high |
| ERICKSON-1049 | components | Si Schottky: lowest VF at ratings ≤ 45 V; very few ≥ 100 V; reverse leakage much higher than p–n. SiC Schottky (600–1700 V available) have far lower Qr, so efficiency improves despite larger VF | — | V_rating | Diode choice | review | §4.2.1 p.80; §4.3.2 p.89 | high |
| ERICKSON-1050 | components | Paralleling: positive-tempco devices (MOSFET; IGBT near rated current) share current and parallel easily (IGBT with modest current derating); negative-tempco devices (diodes, BJTs, thyristors) hog current — require matched parts, common thermal substrate and/or external balancing | — | device type | Parallel devices | review | §4.3.2 p.89; §4.4.1 p.101; §4.5.2 p.119 | high |
| ERICKSON-1051 | power | Diode reverse recovery shortens the effective power-stage duty cycle | D = Dc − tr/Ts | Dc, tr, Ts | Buck with p–n diode, softness S = 0 | calc | §4.3.3 Eq.(4.12) p.90 | high |
| ERICKSON-1052 | power | Diode-recovery-induced switching loss, buck: average input current, loss, efficiency | Ig = D·IL + tr·IL/Ts + Qr/Ts; P_sw = Vg·(Qr + IL·tr)·fs; η = 1/(1 + fs·(tr/D + Qr·R/(D^2·Vg))) | Vg, IL, Qr, tr, fs, D, R | S = 0: loss in transistor; S > 0: shared diode/transistor. Example (Fig.4.39): Vg = 24 V, fs = 100 kHz, R = 15 Ω, Qr = 0.75 μC, tr = 75 ns → η → 0 as D → 0 (light output, fixed switching loss) | calc | §4.3.3 Eq.(4.16)–(4.23) p.92–93 | high |
| ERICKSON-1053 | power | Diode-recovery-induced switching loss, boost with RL: loss appears as an extra load across the output | P_sw = V·(tr·IL + Qr)/Ts; η = (V/Vg)·(D' − Qr/(Ts·IL) − tr/Ts); IL = [Vg/(D'^2·R) + Qr/(Ts·D')]/[1 − tr/(D'·Ts) + RL/(D'^2·R)] | V, Vg, IL, Qr, tr, Ts, D, R, RL | Example (Fig.4.46): fs = 100 kHz, Vg = 24 V, R = 15 Ω, RL = 0.15 Ω, Qr = 1 μC, tr = 50 ns → η slightly < 93% as D → 0; at D = 0 pass-through (no switching) η jumps to copper-loss-only curve | calc | §4.3.4 Eq.(4.32)–(4.37) p.97–98 | high |
| ERICKSON-1054 | power | Boost conversion ratio with diode recovery and RL (reconstructed from OCR, verified by re-derivation from Fig.4.44 model) | M = (1/D')·[1 − (Qr/Ts)·RL/(D'·Vg·(1 − tr/(D'·Ts)))] / [1 + RL/(D'^2·R·(1 − tr/(D'·Ts)))] | as above | Effect on M most pronounced at high D | calc | §4.3.4 Eq.(4.33), Fig.4.45 p.97–98 | medium |
| ERICKSON-1055 | components | Si power MOSFET gate levels: Vth typically 3 V; on-state for VGS > 6–7 V; drive to 12 or 15 V to minimize drop; logic-level parts are on at 5 V; p-channel parts inferior to n-channel | VGS_drive ≥ 10 V (standard) or ≥ 5 V (logic-level) | VGS | Si MOSFETs (not GaN, see ERICKSON-1068) | review | §4.4.1 p.101 | high |
| ERICKSON-1056 | components | Select MOSFETs on Ron/conduction loss, not rated average current (they usually run somewhat below rated average current); datasheet Ron is typical at 25°C and rises significantly at elevated temperature — evaluate at operating Tj | P_cond = Irms^2·Ron(Tj) | Ron(Tj), Irms | MOSFET selection | calc | §4.4.1 p.103 | high |
| ERICKSON-1057 | components | MOSFET figure of merit Ron·Qg (lower = higher efficiency). Qg = charge to raise VGS 0 → specified value (typically 10 V) at a specified off-state VDS (typically 80% of rated VDS); Qg = Qgs + Qgd; switching di/dt set by Cgs charging, dv/dt by Cgd charging | FOM = Ron·Qg | Ron, Qg | Device comparison (Tables 4.2, 4.4, 4.5) | calc | §4.4.1 p.102–103 | high |
| ERICKSON-1058 | components | MOSFET Cds and Cgd are strongly nonlinear (inverse-square-root of voltage; can vary by orders of magnitude); Cgs ≈ linear | Cds(vds) = C0/sqrt(1 + vds/V0); vds >> V0: Cds ≈ C0·sqrt(V0/vds) | C0, V0 | Loss and dv/dt estimates | calc | §4.4.1 Eq.(4.38)–(4.39) p.102–103 | high |
| ERICKSON-1059 | power | Capacitive turn-on loss: energy in transistor output capacitance and diode junction capacitance is dissipated in the transistor at every hard turn-on; typically significant above ≈100 V; gate-drive charging loss is of the same type | W_C = 0.5·(Cds + Cj)·Vg^2 (linear caps); P = W_C·fs | Cds, Cj, Vg, fs | Hard-switched PWM | calc | §4.6.1 Eq.(4.41)–(4.42) p.122–123 | high |
| ERICKSON-1060 | power | Stored energy of a nonlinear (∝ 1/sqrt(v)) MOSFET Cds: equivalent to a linear capacitor of 4/3·Cds(VDS) | W_Cds = (2/3)·Cds(VDS)·VDS^2 | Cds at VDS, VDS | Eq.(4.39) capacitance law | calc | §4.6.1 Eq.(4.43)–(4.44) p.123–124 | high |
| ERICKSON-1061 | power | Series inductance (transformer leakage, package, interconnect) stores energy that is lost at every turn-off and causes turn-off voltage overshoot; significant in high-current and transformer-isolated converters | W_L = 0.5·L·I^2 per turn-off; P = W_L·fs | L_series, I_off, fs | — | calc | §4.6.1 Eq.(4.41) p.122–124 | high |
| ERICKSON-1062 | power | Diode stored charge in an L–C–diode loop leaves energy V2·Qr in the inductor, which rings with C and is dissipated in parasitics (loss with no active switch). Ringing that decays before the end of Ts indicates switching loss | W = 0.5·L·iL(t3)^2 = V2·Qr | V2, Qr | Rectifier/converter diode commutation | calc | §4.6.2 Eq.(4.45)–(4.49) p.125–126 | high |
| ERICKSON-1063 | power | Loss vs switching frequency and practical fs limit: total loss rises linearly with f; the critical frequency where switching loss equals conduction + fixed loss is a rough upper limit on practical fs | Ploss = Pcond + Pfixed + Wtot·fsw; Wtot = Won + Woff + WD + WC + WL + ...; fcrit = (Pcond + Pfixed)/Wtot | Pcond, Pfixed, Wtot | Full-load efficiency vs fs (Fig.4.77) | calc | §4.6.3 Eq.(4.50)–(4.53) p.126 | high |
| ERICKSON-1064 | components | IGBT characteristics: ratings 600–6500 V readily available; VF typically 2–4 V; turn-off current tail → typical turn-off 0.5–5 μs; switching loss limits conventional PWM IGBT converters to roughly 1–30 kHz; negligible reverse-blocking capability; modern parts latch-up free and need minimal snubbing | fs_IGBT ≈ 1–30 kHz | V, fs | IGBT selection | review | §4.5.2 p.115–119 | high |
| ERICKSON-1065 | components | BJT base drive (legacy): large IB1 pulse at turn-on, compromise IBon, large negative IB2 at turn-off (IB2 = 0 → very long storage/fall via recombination); IB1/IB2 limited by emitter current focusing (hot spots, thermal runaway) — may need snubbers; off-state voltage must not exceed BVCEO (text prints "BVCBO", an evident misprint repeated from the preceding definition) | — | IB1, IB2, VCE,off | Power BJTs | review | §4.5.1 p.112–115 | medium |
| ERICKSON-1066 | components | SCR/GTO: after anode current zero crossing wait the turn-off time tq before reapplying forward voltage and limit the reapplied dv/dt (retriggering); limit turn-on di/dt (cathode current focusing, hot spots); GTO turn-off gain 2–5 (several hundred A of negative gate current to turn off 1000 A); SCRs 5000–7000 V, several kA | I_G,off ≈ I_A/(2…5) | tq, dv/dt, di/dt | Thyristor converters | review | §4.5.3 p.119–122 | high |
| ERICKSON-1067 | components | SiC MOSFET: body diode VF 3–4 V, trr several tens of ns → turn the MOSFET on (synchronous rectification) for reverse conduction; oxide reliability compromised above 175°C, limiting Tj (bulk could reach ≈300°C, packaging lower); SiC beats Si only above 600 V ratings | Tj_max ≤ 175°C (oxide) | Tj, V_rating | SiC MOSFET use | review | §4.4.2 p.105 | high |
| ERICKSON-1068 | components | Enhancement-mode GaN HEMT: gate is a diode — limit on-state gate current; typical on-state VGS 3–5 V (vendor-specific); no body diode but reverse-conducts when vds ≤ −Vth (≈4 V drop at VGS = 0); cannot block negative voltage (current-bidirectional two-quadrant); no reverse recovery; Qg ≈ an order of magnitude below a comparable Si SJ MOSFET | VGS_on = 3–5 V | VGS, gate current | GaN FET drive and dead-time design | review | §4.4.2 p.106–107, Table 4.5 | high |
| ERICKSON-1069 | power | Half-bridge high-side drive: driver referenced to switch node through a level shifter; bootstrap capacitor Cboot charges through Dboot only while the low-side FET conducts → the low-side FET must turn on periodically to refresh Cboot; Cboot voltage must stay above the driver UVLO threshold; UVLO holds both FETs off during 12 V supply start-up | V_Cboot > V_UVLO; max on-time of Q1 limited by Cboot droop | Cboot, UVLO | Synchronous buck, half-bridge inverters | review | §4.4.3 p.107–108 | high |
| ERICKSON-1070 | power | Shoot-through prevention: high- and low-side FETs must never conduct simultaneously, not even for a few ns; a dead-time generator inserts td (break-before-make) at both edges; during td the body diode conducts and must then reverse-recover, inducing turn-on loss in the other FET; Cds energy of both FETs is dissipated in the turning-on FET | td > 0 at every edge; vgs(off FET) < Vth before the other FET turns on | td, Vth, gate waveforms | Synchronous half-bridges | sim | §4.4.3 p.108–110 | high |
| ERICKSON-1071 | power | Gate-driver Thevenin resistance from its peak-current rating | Rthev = V_drive/I_pk (e.g. 12 V, 1 A driver → 12 Ω) | V_drive, I_pk | First-order driver model | calc | §4.4.3 p.109 | high |
| ERICKSON-1072 | power | dv/dt (Miller) induced turn-on of the off FET: switch-node rise injects igd = Cgd·dvs/dt into its gate; vgs must stay < Vth throughout the opposite FET's turn-on, else oscillation and extra loss. Remedy: series gate resistor Rg1 on the high-side FET with antiparallel diode Dg1 (slows turn-on only, not turn-off); add Rg2/Dg2 on the low side if iL can reverse | vgs,peak ≈ Cgd·(dvs/dt)·Rthev < Vth (first-order) | Cgd, dvs/dt, Rthev, Vth | Synchronous buck / half-bridge | sim | §4.4.3 p.110–111, Fig.4.58 | medium |
| ERICKSON-1073 | power | DCM occurs in converters with current- or voltage-unidirectional switches when an inductor-current (or capacitor-voltage) ripple is large enough to reverse the switch current (voltage) polarity — typically at light load. In DCM M becomes load-dependent, output impedance rises, control can be lost at no load, and dynamics change | DCM ⇔ ripple > dc component at the diode | I, ΔiL | Any diode-rectified PWM converter; must be checked at minimum load | calc | Ch.5 intro p.135; Key pts 1, 5 p.153–154 | high |
| ERICKSON-1074 | power | CCM/DCM boundary test for buck, boost, buck–boost (I and ΔiL computed with CCM formulas) | CCM if I > ΔiL; DCM if I < ΔiL | I, ΔiL (peak) | Diode-rectified single-inductor converters | calc | §5.1 Eq.(5.3); §5.3 Eq.(5.30) p.138, 146 | high |
| ERICKSON-1075 | power | Dimensionless load parameter K and mode boundary | K = 2L/(R·Ts); CCM if K > Kcrit(D) (R < Rcrit(D)); DCM if K < Kcrit(D) (R > Rcrit(D)); for nonlinear loads use R = V/I | L, R, Ts, D | Table 5.1 converters | calc | §5.1 Eq.(5.6)–(5.8), Table 5.1 p.138–140 | high |
| ERICKSON-1076 | power | Buck mode boundary | Kcrit = 1 − D (max 1); Rcrit = 2L/((1 − D)·Ts); if R < 2L/Ts (K > 1) CCM at all D | L, R, Ts, D | Buck with diode | calc | Eq.(5.5)–(5.7), Fig.5.5, Table 5.1 p.138–140 | high |
| ERICKSON-1077 | power | Boost mode boundary: Kcrit peaks at 4/27 at D = 1/3; boost is always CCM near D = 0 and D = 1 | Kcrit = D·(1 − D)^2; max 4/27; Rcrit = 2L/(D·(1 − D)^2·Ts); min Rcrit = 27·L/(2·Ts); K > 4/27 → CCM for all D | L, R, Ts, D | Boost with diode | calc | §5.3 Eq.(5.32)–(5.33), Fig.5.13, Table 5.1 p.146–147 | high |
| ERICKSON-1078 | power | Buck–boost mode boundary | Kcrit = (1 − D)^2 (max 1); Rcrit = 2L/((1 − D)^2·Ts); min Rcrit = 2L/Ts | L, R, Ts, D | Buck–boost (and flyback with turns ratio generalization) | calc | Table 5.1 p.140 | high |
| ERICKSON-1079 | power | Buck DCM conversion ratio, diode duty and peak current; DCM raises V above D·Vg and M → 1 at no load (K → 0) | M = 2/(1 + sqrt(1 + 4K/D^2)); D2 = K·M/D; i_pk = (Vg − V)·D·Ts/L | D, K, Vg, V, L, Ts | K < Kcrit | calc | §5.2 Eq.(5.23), (5.28)–(5.29), Table 5.2 p.144–153 | high |
| ERICKSON-1080 | power | Boost DCM conversion ratio (nearly linear in D), diode duty, peak current | M = (1 + sqrt(1 + 4D^2/K))/2 ≈ 1/2 + D/sqrt(K); D2 = K·M/D; i_pk = Vg·D·Ts/L | D, K, Vg, L, Ts | K < Kcrit | calc | §5.3 Eq.(5.44), (5.52)–(5.54), Table 5.2 p.150–153 | high |
| ERICKSON-1081 | power | Buck–boost DCM conversion ratio (linear, slope 1/sqrt(K)) and diode duty | M = −D/sqrt(K); D2 = sqrt(K) | D, K | K < Kcrit | calc | Table 5.2, Fig.5.20 p.153 | high |
| ERICKSON-1082 | power | DCM analysis: output capacitor ripple must still be small and may be neglected, but inductor current ripple must NOT be neglected; volt-second and charge balance always hold in steady state | — | — | DCM steady-state analysis | review | §5.2 p.140–141; Key pt 4 p.153 | high |
| ERICKSON-1083 | power | DCM third subinterval shows parasitic ringing of L with semiconductor capacitances; usually little influence on steady-state behaviour (but is a switching-loss/EMI indicator, see ERICKSON-1062) | — | — | DCM waveforms | measure | §5.2 p.142 | high |
| ERICKSON-1084 | power | DCM-by-design margin: when a converter must stay in DCM at all operating points, choose L so that K is no greater than 75% of Kcrit at every operating point (worst-case Vg and load) | K_max ≤ 0.75·Kcrit(D) over all (Vg, Pload) | L, R_min, Ts, D range | DCM designs (e.g. DCM boost 18–36 V → 48 V, 5–100 W, 150 kHz example) | calc | Problem 5.17 p.160 | high |
| ERICKSON-1085 | power | Light-load efficiency: gate-drive power and much of switching loss scale with fs, not load, so for sleep-mode loads reduce fs in proportion to load current (e.g. DCM constant on-time, variable off-time control) | P_sw ∝ fs; choose fs ∝ I_load at light load | fs, I_load | Battery-powered portable converters | review | Problem 5.18 p.160 | medium |
| ERICKSON-1086 | power | A synchronous-rectified converter with complementary drive has current-bidirectional switches, so it does not enter DCM at light load: the inductor current simply goes negative (forced CCM, M stays = D) | — | — | Synchronous buck/boost | review | Key pt 1 p.153 with §4.1.5 p.78 (Problem 5.3) | medium |
| ERICKSON-1087 | power | Cascade of converters driven by the same D multiplies ratios; buck+boost cascade reduces to the non-inverting buck–boost M = D/(1 − D) (steps down for D < 0.5, up for D > 0.5); inverting buck–boost = buck·boost with inductor reversal M = −D/(1 − D) and inherits pulsating input (buck) AND pulsating output (boost) current; Ćuk (boost→buck) inherits NON-pulsating input and output currents | M = M1(D)·M2(D) | M1, M2, D | Topology selection for EMI/filter needs | calc | §6.1.2 Eq.(6.6)–(6.10) p.166–169 | high |
| ERICKSON-1088 | power | Differential load connection gives bipolar/ac output: two bucks with complementary duty form the H-bridge; 3-phase load across three converters: common-mode dc bias cancels in phase voltages; current-source (boost-type) inverter normally needs a cascaded buck at its dc input to reduce voltage | V = V1 − V2; H-bridge V = (2D − 1)·Vg; Vn = (V1 + V2 + V3)/3; Van = V1 − Vn | D, Vg | Inverters, servo amplifiers | calc | §6.1.4 Eq.(6.11)–(6.15) p.170–174 | high |
| ERICKSON-1089 | power | Ćuk and SEPIC keep the MOSFET source at ground (simplified gate drive); SEPIC and inverse-SEPIC give non-inverting buck–boost M = D/D'; "buck²" (one transistor, three diodes) gives M = D^2 for large step-down or wide operating range | M_SEPIC = D/(1 − D); M_buck2 = D^2 | D | Topology selection | review | §6.2 p.177–178, Fig.6.16 | high |
| ERICKSON-1090 | magnetics | Transformer model for converter analysis: ideal multi-winding transformer plus magnetizing inductance LM (referred to primary) in parallel; leakage inductances in series with windings; magnetizing current iM is independent of the load (primary) current | v1/n1 = v2/n2 = v3/n3; 0 = n1·i1' + n2·i2 + n3·i3; v1 = LM·diM/dt | n_k, LM | All isolated converters | review | §6.3 Eq.(6.16)–(6.17) p.179–181 | high |
| ERICKSON-1091 | magnetics | Transformer (magnetizing inductance) volt-second balance: the average winding voltage must be zero in steady state; any dc component ratchets iM up each cycle until the core saturates, LM collapses and the windings are effectively shorted | <v1> = (1/Ts)·∫0..Ts v1 dt = 0 (over 2Ts for bridge/push-pull); iM(t) − iM(0) = (1/LM)·∫ v1 dt | v1(t), LM | All transformer-isolated converters | sim | §6.3 Eq.(6.18)–(6.19) p.181 | high |
| ERICKSON-1092 | magnetics | Magnetizing inductance must be large enough that iM << reflected load current (abs(Z_LM) large over the operating frequency range) for near-ideal transformer behaviour (not applicable to flyback, where LM is the energy-storage inductor) | iM,pk << I_load·n | LM, Vg, D, Ts | Forward, bridge, push-pull, Ćuk transformers | calc | §6.3 p.180–181 | high |
| ERICKSON-1093 | magnetics | Leakage inductance causes switching loss, increased peak transistor voltage (ringing above the ideal clamp value) and degraded cross-regulation of auxiliary outputs | V_pk,actual > V_pk,ideal | L_leak | Isolated converters | measure | §6.3 p.181; §6.3.2 p.191; §6.3.4 p.198 | high |
| ERICKSON-1094 | power | Isolation design: transformer size/weight scale inversely with frequency, so place the transformer inside the converter at fs; pick the turns ratio to minimize device voltage/current stress when a large step-up/down is needed; with multiple outputs only one output is regulated — allow wider tolerance on auxiliaries (cross regulation) | — | fs, n, outputs | Off-line and multi-output supplies | review | §6.3 p.178–179 | high |
| ERICKSON-1095 | power | Full-bridge isolated buck: CCM ratio, duty range, transformer frequency and diode current split in the freewheel interval; antiparallel diodes clamp transistor peak voltage to Vg | V = n·D·Vg, 0 ≤ D < 1; transformer at fs/2; freewheel: iD5 = i/2 − iM/(2n), iD6 = i/2 + iM/(2n) | n, D, Vg, iM | Typically used ≥ ≈750 W; full B–H loop usable (flux swing usually core-loss limited); centre-tapped secondary poorly utilized | calc | §6.3.1 Eq.(6.20)–(6.28) p.181–185 | high |
| ERICKSON-1096 | magnetics | Bridge/push-pull flux walking: small imbalances in device drops or switching times put dc volt-seconds on the primary → saturation. Remedies: dc-blocking capacitor in series with the primary (duty-cycle control), or current-programmed control (then omit the series capacitor). Push-pull with duty-cycle-only control is not recommended | V_dc,primary → 0 | device mismatch | Full-bridge, push-pull | review | §6.3.1 p.184; §6.3.3 p.193 | high |
| ERICKSON-1097 | power | Bridge-leg shoot-through: transistors of the same leg (Q1/Q2) must never conduct simultaneously (shorts Vg, current spike, low efficiency, failure) — add delay between turn-off and the next turn-on | dead time > 0 | gate timing | Full/half bridges | sim | §6.3.1 p.185 | high |
| ERICKSON-1098 | power | Half-bridge isolated buck: half the full-bridge primary voltage, so for the same output transistor currents double; used at lower power; Cb holds 0.5·Vg; transistor peak clamped to Vg; Ca may be omitted; current-programmed control generally does not work with the half-bridge | V = 0.5·n·D·Vg; V_Cb = 0.5·Vg; I_Q ≈ 2× full-bridge | n, D, Vg | Lower-power bridge designs | calc | §6.3.1 Eq.(6.29) p.185–186 | high |
| ERICKSON-1099 | power | Single-transistor forward converter: output ratio, reset interval and maximum duty; magnetizing inductance must reset to zero (DCM) every cycle or the core saturates | V = (n3/n1)·D·Vg; D2 = (n2/n1)·D; D ≤ 1/(1 + n2/n1) (D ≤ 0.5 for n1 = n2) | n1, n2, n3, D, Vg | CCM output inductor | calc | §6.3.2 Eq.(6.30)–(6.36) p.189–191 | high |
| ERICKSON-1100 | derating | Forward-converter transistor peak voltage during reset; lowering n2/n1 raises Dmax but raises this stress; add leakage-ringing margin | vQ1,max = Vg·(1 + n1/n2) (= 2·Vg for n1 = n2), plus leakage-inductance ringing | Vg, n1, n2 | Single-transistor forward | calc | §6.3.2 Eq.(6.37) p.191 | high |
| ERICKSON-1101 | power | Two-transistor forward: D < 0.5; transistor blocking clamped to Vg by D1/D2; power level similar to half-bridge. Forward transformer: windings best utilized (no centre taps), only half the B–H loop but flux swing is core-loss-limited so core utilization matches bridges; nonpulsating output current suits high output currents | V_Q,pk = Vg; D < 0.5 | Vg, D | Forward converters | review | §6.3.2 p.187, 191–192 | high |
| ERICKSON-1102 | power | Push-pull isolated buck: suited to low input voltage (only one transistor in series with the source → low primary conduction loss; D up to ≈1 allows lower n and transistor current); prone to transformer saturation → use current-programmed control | V = n·D·Vg, 0 ≤ D < 1 | n, D, Vg | Low-Vg isolated supplies | calc | §6.3.3 Eq.(6.38) p.192–193 | high |
| ERICKSON-1103 | power | Flyback (isolated buck–boost) CCM: conversion ratio, primary-referred magnetizing current, input current and transistor stress; very low parts count (each extra output = winding + diode + capacitor) but high transistor stress and poor cross-regulation; typical 50–100 W and HV supplies | M = n·D/D'; I_M = n·V/(D'·R); Ig = D·I_M; V_Q,pk = Vg + V/n (+ leakage ringing) | n, D, V, R, Vg | Flyback transformer = two-winding inductor (dc magnetizing current, ≤ half B–H loop). DCM → smaller transformer but higher peak currents; CCM → larger LM, lower peaks | calc | §6.3.4 Eq.(6.43)–(6.47) p.197–198 | high |
| ERICKSON-1104 | power | Transformer-isolated boost (full-bridge current-fed): ratio and transistor stress; transformer imbalance is not catastrophic because L limits current; push-pull version transistors block twice the reflected voltage | M = n/D'; V_Q = V/n = Vg/D' (full-bridge); V_Q = 2V/n (push-pull) (+ leakage ringing) | n, D, V | HV supplies, low-harmonic rectifiers | calc | §6.3.5 Eq.(6.48)–(6.49) p.200–201 | high |
| ERICKSON-1105 | power | Isolated SEPIC / isolated Ćuk: ratio and transistor stress; SEPIC transformer rms currents exceed the flyback's (primary also carries i1 during D'Ts); Ćuk series capacitors keep dc off the transformer (full B–H loop, negligible LM energy storage, no centre taps); typical several hundred W and low-harmonic rectifiers | M = n·D/D'; V_Q = Vg/D' (+ leakage ringing) | n, D, Vg | Isolated SEPIC/Ćuk | calc | §6.3.6 Eq.(6.50) p.201–202 | high |
| ERICKSON-1106 | power | Forward converter with auxiliary reset source Vr on reset winding n2 (derived from the Eq.6.30 volt-second balance, Problem 6.9): minimum reset voltage and resulting transistor peak voltage; lets Dmax exceed 0.5 and reduces stress over wide Vg | Vr,min = (n2/n1)·Vg·D/(1 − D); V_Q1,pk = Vg + (n1/n2)·Vr = Vg/(1 − D) at Vr,min | Vg, D, n1, n2 | Wide-input forward (e.g. 127–380 V in, 12 V/480 W example) | calc | Problem 6.9 p.208–209 (derived) | medium |
| ERICKSON-1107 | magnetics | General magnetic reset condition (generalizes Eq.6.30–6.34, also current-sense transformers of Problem 6.8): reset volt-seconds available in the off-time must at least equal the set volt-seconds; keep the magnetizing current in DCM and much smaller than the sensed/load current | V_set·D ≤ V_reset·(1 − D) → D_max = V_reset/(V_set + V_reset) | V_set, V_reset, D | Forward, current-sense transformers, reset windings, Zener/RCD resets | calc | §6.3.2 Eq.(6.30)–(6.34); Problem 6.8 p.207–208 | medium |
| ERICKSON-1108 | power | Switch utilization (defined only in words in this edition): output power divided by total transistor voltage-and-current stress; higher utilization → higher efficiency and lower cost; isolated converters with wide Vg/Pload variation utilize switches worse than nonisolated single-operating-point converters; use spreadsheets for topology trade studies | U = Pout / Σ_transistors (V_stress·I_stress) | V_pk, I per transistor, Pout | Topology comparison; stress measures not specified in this text (2nd-ed. table absent) | calc | Ch.6 intro p.163–164 | low |
| ERICKSON-1109 | control-loop | Averaged-model bandwidth limit: the Ts moving-average operator has Gav(jω) = sin(ωTs/2)/(ωTs/2) — unity gain and zero phase at low frequency, nulls at fs and harmonics, substantial attenuation above ≈ fs/3 — so averaged models may not accurately predict dynamics above ≈ fs/3 | Gav(jω) = sin(ωTs/2)/(ωTs/2); trust averaged sim/models for f < ≈ fs/3 | fs | Averaged (non-switching) simulation and loop design | sim | §7.2.3 Eq.(7.20)–(7.22), Fig.7.10 p.224 | high |
| ERICKSON-1110 | control-loop | Small-signal model validity: perturbations small relative to quiescent values; modulation frequency << fs; circuit natural frequencies sufficiently slower than fs; modulation harmonics become significant as ωm → ωs or modulation depth Dm → D | abs(v̂g) << Vg; abs(d̂) << D; abs(î) << abs(I); abs(v̂) << abs(V) | ac amplitudes, fs | Linearized converter models, ac sweeps | sim | §7.1 p.215–218; §7.2.6 Eq.(7.33) p.228 | high |
| ERICKSON-1111 | control-loop | Large-signal averaged CCM model (basis of averaged simulation), buck–boost example: averaged inductor/capacitor laws hold with no extra terms | L·d<i>/dt = <vL>; C·d<v>/dt = <iC>; buck–boost: L·d<i>/dt = d·<vg> + d'·<v>; C·d<v>/dt = −d'·<i> − <v>/R; <ig> = d·<i> | d(t), vg, L, C, R | CCM, small ripple | sim | §7.2.1–7.2.5 Eq.(7.13), (7.14), (7.29) p.222–227 | high |
| ERICKSON-1112 | control-loop | Small-signal CCM buck–boost equations (form reused for other converters with M changes) | L·dî/dt = D·v̂g + D'·v̂ + (Vg − V)·d̂; C·dv̂/dt = −D'·î − v̂/R + I·d̂; îg = D·î + I·d̂ | D, Vg, V, I, L, C, R | CCM | sim | §7.2.7 Eq.(7.44) p.230 | high |
| ERICKSON-1113 | control-loop | Nonlinear load in the small-signal model: use the incremental resistance at the operating point (dc solution uses the actual characteristic) | 1/R = df(v)/dv at v = V | load i–v curve | CPL/LED/battery-type loads | calc | §7.2.8 Eq.(7.52)–(7.55) p.233 | high |
| ERICKSON-1114 | control-loop | Loss elements in averaged models: MOSFET Ron appears as effective series resistance D·Ron in the inductor loop (flyback example); boost output-capacitor ESR RC adds effective series resistance D·D'·(R‖RC) (ESR loss from the ac capacitor current) plus new dynamics; with ESR the output voltage steps by iL·(R‖RC) at each diode turn-on/off — apply small-ripple only to the ideal-capacitor voltage vC | R_eff,Q = D·Ron; R_eff,ESR = D·D'·(R·RC/(R + RC)) | Ron, RC, R, D | CCM | calc | §7.2.10 p.241; §7.5.5 Eq.(7.154), Fig.7.51 p.265–269 | high |
| ERICKSON-1115 | control-loop | Pulse-width modulator gain (comparator + sawtooth of peak-to-peak VM, minimum 0) | d = vc/VM for 0 ≤ vc ≤ VM; D = Vc/VM; d̂/v̂c = 1/VM | VM | Voltage-mode PWM | calc | §7.3 Eq.(7.82)–(7.85) p.243–244 | high |
| ERICKSON-1116 | control-loop | PWM sampling constraint: the modulator samples vc once per period (at the modulated edge), so control-loop bandwidth must be sufficiently less than the Nyquist rate fs/2; avoid significant switching-frequency ripple in vc (poor noise immunity, altered modulator gain) | f_crossover << fs/2 | fc, fs, ripple on vc | All PWM loops (analog and digital) | review | §7.3 p.244–245 | high |
| ERICKSON-1117 | control-loop | Canonical model of any CCM PWM dc–dc converter: e(s)·d̂ and j(s)·d̂ sources, ideal 1:M(D) transformer, effective LC low-pass He(s) loaded by R | Gvg(s) = M(D)·He(s); Gvd(s) = e(s)·M(D)·He(s); Zout(s) = Zeo(s)‖R | e, j, M, He | CCM converters; nonlinear load → incremental R | calc | §7.4.1 Eq.(7.86)–(7.88) p.247 | high |
| ERICKSON-1118 | control-loop | Canonical model parameters for ideal buck, boost, buck–boost (Table 7.1; isolated versions: include turns ratio) | buck: M = D, Le = L, e = V/D^2, j = V/R; boost: M = 1/D', Le = L/D'^2, e = V·(1 − s·L/(D'^2·R)), j = V/(D'^2·R); buck–boost: M = −D/D', Le = L/D'^2, e = −(V/D^2)·(1 − s·D·L/(D'^2·R)), j = −V/(D'^2·R) | D, L, R, V | CCM, single L and C | calc | §7.4.3 Table 7.1 p.251 | high |
| ERICKSON-1119 | control-loop | In boost and buck–boost the effective filter inductance is L/D'^2, so resonant frequency, Q and impedances move with the operating point — design/verify loops at all (Vg, load) corners | Le = L/D'^2 | L, D | Boost-type converters | sim | §7.4.2 p.250 | high |
| ERICKSON-1120 | control-loop | State-space averaging (mechanizable for any CCM converter whose subinterval state equations K·dx/dt = Ai·x + Bi·u, y = Ci·x + Ei·u can be written) | A = D·A1 + D'·A2 (same for B, C, E); X = −A^-1·B·U; Y = (−C·A^-1·B + E)·U; K·dx̂/dt = A·x̂ + B·û + {(A1 − A2)·X + (B1 − B2)·U}·d̂; ŷ = C·x̂ + E·û + {(C1 − C2)·X + (E1 − E2)·U}·d̂ | subinterval matrices, D, U | Natural frequencies and input variations << fs | sim | §7.5.2 Eq.(7.104)–(7.110) p.255–256 | high |
| ERICKSON-1121 | control-loop | Decibel conventions for Bode plots: dimensioned quantities must be normalized to a stated base before taking dB (dBΩ with Rbase = 1 Ω; converter input harmonic currents in dBμA, 60 dBμA = 1 mA); a magnitude varying as (f/f0)^n has slope 20n dB/decade (≈ 6n dB/octave) | G_dB = 20·log10(abs(G)); Z_dB = 20·log10(abs(Z)/Rbase) | G, Z, Rbase | All Bode/impedance plots and EMI current spectra | calc | §8.1 Eq.(8.3)–(8.6), Table 8.1 p.280 | high |
| ERICKSON-1122 | control-loop | Single real pole (LHP) response anchors for asymptote-based plotting | abs(G) = −3 dB at f0, −1 dB at f0/2 and 2f0; phase −45° at f0; phase asymptote 0° below f0/10, −90° above 10·f0, slope −45°/decade between, max error 5.7° at the breaks | f0 | Poles/zeros of any transfer function (zero: mirror signs) | calc | §8.1.1–8.1.2 Eq.(8.23)–(8.31), Figs.8.7–8.12 p.283–287 | high |
| ERICKSON-1123 | control-loop | Right-half-plane zero: magnitude of an LHP zero (+20 dB/decade) but phase of a pole (0 → −90°); indistinguishable by magnitude alone; step response initially moves the wrong way | G(s) = 1 − s/ωz; phase = −atan(ω/ωz) | ωz | Boost, buck–boost, flyback control-to-output | review | §8.1.3 Eq.(8.32)–(8.34) p.288; §8.2.3 p.316–317 | high |
| ERICKSON-1124 | control-loop | Quadratic pole normalized form, Q definition and peaking: magnitude at f0 equals exactly Q; poles are real for Q ≤ 0.5, complex (peaking) for Q > 0.5; phase asymptote from 10^(−1/(2Q))·f0 to 10^(1/(2Q))·f0 with slope −180·Q degrees/decade | G(s) = 1/(1 + s/(Q·ω0) + (s/ω0)^2); Q = 1/(2ζ); abs(G(jω0)) = Q; Q = 2π·(peak stored energy)/(energy dissipated per cycle) | ω0, Q | Two-pole filters, converter Gvd/Gvg | calc | §8.1.6 Eq.(8.57)–(8.69) p.294–297 | high |
| ERICKSON-1125 | filter | Loaded LC low-pass (series L, C parallel with R) resonance and Q | f0 = 1/(2π·sqrt(L·C)); Q = R·sqrt(C/L) = R/R0 with R0 = sqrt(L/C) (characteristic impedance) | L, C, R | Buck output filter; canonical-model filters | calc | §8.1.6 Eq.(8.61) p.295; §8.4 Eq.(8.180)–(8.182) p.328 | high |
| ERICKSON-1126 | control-loop | Low-Q approximation: for Q << 0.5 the quadratic splits into real poles at Q·f0 and f0/Q (within 10% for Q ≤ 0.3); for the loaded LC filter these are R/L and 1/(RC) | ω1 ≈ Q·ω0 = R/L; ω2 ≈ ω0/Q = 1/(R·C); exact: ω1 = Q·ω0/F(Q), ω2 = ω0·F(Q)/Q, F(Q) = (1 + sqrt(1 − 4Q^2))/2 | Q, ω0 | Q ≤ 0.3 for 10% accuracy (Fig.8.26 caption prints "Q < 3" — typo; F(0.3) = 0.9 confirms 0.3) | calc | §8.1.7 Eq.(8.74)–(8.81) p.300–301; Key pt 6 p.336 | high |
| ERICKSON-1127 | control-loop | High-Q approximation: a resonance damped by two elements has composite Q ≈ inverse sum of the individual Qs (e.g. load R and capacitor ESR RC); within 10% when Q1·Q2 > 5 | Q ≈ Qload‖QC = 1/(1/Qload + 1/QC); Qload = R/R0; QC = R0/RC; R0 = sqrt(L/C); exact ωe = ω0/FH, Qe = (Qload‖QC)·FH, FH = sqrt(1 + 1/(Qload·QC)) | R, RC, L, C | Qload >> 1 and QC >> 1 | calc | §8.1.8 Eq.(8.82)–(8.96) p.301–304; Key pt 7 p.336 | medium |
| ERICKSON-1128 | control-loop | Approximate factoring of an nth-order denominator P(s) = 1 + a1·s + … + an·s^n with well-separated real roots (justify numerically); leave pairs that are not separated in quadratic form | τ1 ≈ a1, τ2 ≈ a2/a1, …, τn ≈ an/a(n−1), valid if abs(a1) >> abs(a2/a1) >> … >> abs(an/a(n−1)) | coefficients a_k | Design-oriented pole estimates (e.g. damped EMI filter) | calc | §8.1.9 Eq.(8.97)–(8.110) p.304–306 | high |
| ERICKSON-1129 | control-loop | CCM small-signal transfer-function forms of buck, boost, buck–boost (salient features in §2 Table 8.2); isolated versions: multiply Gvg by the turns ratio, otherwise same (symmetric bridge transformer and vg-reset forward transformer add negligible dynamics) | Gvd = Gd0·(1 − s/ωz)/(1 + s/(Q·ω0) + (s/ω0)^2); Gvg = Gg0/(1 + s/(Q·ω0) + (s/ω0)^2) | D, V, L, C, R | Ideal CCM converters | calc | §8.2.2 Eq.(8.147)–(8.148), Table 8.2 p.315 | high |
| ERICKSON-1130 | control-loop | Buck–boost worked example anchors: D = 0.6, R = 10 Ω, Vg = 30 V, L = 160 μH, C = 160 μF → Gg0 = 1.5 (3.5 dB), abs(Gd0) = 187.5 V (45.5 dBV), f0 = 400 Hz, Q = 4 (12 dB), RHP zero fz = 2.65 kHz (inversion adds 180°) | f0 = D'/(2π·sqrt(LC)); Q = D'·R·sqrt(C/L); fz = D'^2·R/(2π·D·L) | as listed | Use as a unit test for a transfer-function calculator | calc | §8.2.1 Eq.(8.145)–(8.146), Fig.8.35 p.313–314 | high |
| ERICKSON-1131 | control-loop | RHP-zero limitation: boost/buck–boost (CCM) output initially moves opposite to the final value after a duty step; this makes adequate phase margin hard to obtain with wide-bandwidth single-loop voltage-mode control — keep loop crossover well below fz (text gives no numeric factor) | f_c << fz_RHP | fz, fc | CCM boost, buck–boost, flyback | calc | §8.2.3 p.316–317 | high |
| ERICKSON-1132 | control-loop | Graphical ("algebra on the graph") impedance construction: series combination → take the LARGER asymptote; parallel combination → take the SMALLER; corner frequencies where asymptotes intersect; exact value at a resonance set by the resistor | series RLC: Q = R0/R; parallel RLC: Q = R/R0; R0 = sqrt(L/C); at ω0 abs(Z) = R | R, L, C | Hand/automated asymptote plots | calc | §8.3.1–8.3.4 Eq.(8.154)–(8.176) p.318–325 | high |
| ERICKSON-1133 | control-loop | Voltage-divider transfer function from impedances: H = Z2/(Z1 + Z2) = Zout/Z1 (Zout = Z1‖Z2); for the LC filter H(jω0) = R/R0 = Q | H = Zout/Z1 | Z1, Z2 | Filters, Gvd construction | calc | §8.3.5 Eq.(8.177)–(8.179) p.325–327 | high |
| ERICKSON-1134 | control-loop | Buck converter impedances and transfer functions: Zout = sL‖R‖1/(sC) (inductive at LF, capacitive at HF, = R at f0, Q = R/R0 → high Q / lightly damped at light load); Zin = (1/D^2)·(sL + R‖1/(sC)), abs(Zin(f0)) ≈ R0^2/(D^2·R); Gvd = Vg·Zout/Z1 (LF asymptote Vg, HF asymptote Vg/(ω^2·L·C)); Gvg = D·Zout/Z1 | f0 = 1/(2π·sqrt(LC)); Q = R/R0 | Vg, D, L, C, R | Ideal CCM buck | calc | §8.4 Eq.(8.180)–(8.191) p.327–331 | high |
| ERICKSON-1135 | test | Transfer-function measurement: use a network (frequency-response) analyzer — its narrowband tracking voltmeter is essential with switching ripple/noise; inject via a dc-blocking capacitor, set the operating point with a bias adjustment; blocking cap, bias network and injection amplitude do not affect the measured ratio v̂y/v̂x | G(s) = v̂y/v̂x | — | Loop/plant/impedance measurements on prototypes | measure | §8.5 Eq.(8.192)–(8.194), Figs.8.60–8.62 p.332–334 | high |
| ERICKSON-1136 | test | Small-impedance measurement error: with grounded injection and probe returns the analyzer reads Z + Zprobe‖Zrz; requires Z >> Zprobe‖Zrz, practical lower limit a few tens–hundreds of mΩ. Insert an isolation transformer (turns ratio n for matching) in the injection path to measure much smaller impedances | Z_meas = Z + Zprobe‖Zrz; need Z >> Zprobe‖Zrz | Zprobe, Zrz | Output impedance / PDN / capacitor measurements | measure | §8.5 Eq.(8.195)–(8.196), Fig.8.63 p.334–336 | high |
| ERICKSON-1137 | process | Design-oriented engineering process for converters: (1) define specifications, (2) propose circuit, (3) model (vendor data for components), (4) design-oriented analysis to choose element values, (5) verify model against a laboratory prototype and refine, (6) worst-case / yield analysis (simulation), (7) iterate until worst-case meets spec | — | — | Every power-stage design | review | Ch.8 intro p.277 | high |
| ERICKSON-1138 | components | Capacitor loss (dielectric loss, contact and foil resistance) is modelled by an equivalent series resistance ESR; high-dielectric-constant types (electrolytic, tantalum, some MLCC) typically have relatively high ESR; ESR adds output ripple and a zero at 1/(2π·RC·C) | f_ESR = 1/(2π·ESR·C) | ESR, C | Output-capacitor selection and loop modelling | calc | Problem 8.22 p.345; §2.5 p.37; Fig.9.8 p.357 | medium |
| ERICKSON-1139 | control-loop | Closed-loop regulator relations with loop gain T = H·Gc·Gvd/VM: reference, line and load disturbances | v̂ = v̂ref·(1/H)·T/(1 + T) + v̂g·Gvg/(1 + T) − îload·Zout/(1 + T) | H, Gc, Gvd, VM, Gvg, Zout | Voltage-mode PWM regulator | calc | §9.2 Eq.(9.1)–(9.6) p.350–352 | high |
| ERICKSON-1140 | control-loop | Feedback reduces disturbance transfer functions and output impedance by 1/(1 + T) ≈ 1/abs(T) below crossover and has essentially no effect above crossover; crossover fc (abs(T) = 1) is the regulator bandwidth | abs(closed-loop) ≈ abs(open-loop)/abs(T) for f < fc; ≈ open-loop for f > fc | T(f) | Line ripple, output impedance, load-step design | calc | §9.3 Eq.(9.11)–(9.17) p.354–358 | high |
| ERICKSON-1141 | control-loop | DC set-point accuracy depends only on H(0) and Vref when T(0) is large: use precision resistors for the sensor divider and an accurate reference; forward-path gains (compensator, PWM, power stage) need not be tight | V = (Vref/H(0))·T(0)/(1 + T(0)) ≈ Vref/H(0) | Vref, H(0), T(0) | Output voltage accuracy budget | calc | §9.2.2 Eq.(9.9) p.353 | high |
| ERICKSON-1142 | control-loop | Loop-gain requirement for line-ripple rejection: to attenuate the line-to-output transfer function by a factor k at the ripple frequency need abs(T) ≥ k there; a typical good design has abs(T) ≥ 20 dB at 120 Hz (or 100 Hz) | abs(T(f_ripple)) ≥ k (e.g. 20 → 26 dB); design target ≥ 20 dB at 2×f_line | Gvg, ripple spec | Off-line and rectified-input converters | calc | §9.3 p.355; §9.5 item 2 p.377 | high |
| ERICKSON-1143 | control-loop | Phase-margin test: φm = 180° + ∠T(j2πfc) must be positive for stability; valid only with a single crossover and no RHP poles in T — otherwise use the Nyquist criterion (count encirclements of −1: N = Z − P; indent the contour around integrator poles) | φm = 180° + ∠T(j2π·fc) > 0 | T(jω) | All loops; multiple crossovers → Nyquist | sim | §9.4.1–9.4.2 Eq.(9.21)–(9.26) p.359–369 | high |
| ERICKSON-1144 | control-loop | Phase margin ↔ closed-loop Q (for T ≈ integrator + one pole, or −40 dB/decade + one zero, near crossover): real closed-loop poles (Q ≤ 0.5) need φm ≥ 76°; Q = 1 needs φm = 52° | Q = sqrt(cos φm)/sin φm; φm = atan(sqrt((1 + sqrt(1 + 4Q^4))/(2Q^4))) | φm | Not valid with ≥3 poles near fc | calc | §9.4.3 Eq.(9.39)–(9.41), Fig.9.25 p.370–373 | high |
| ERICKSON-1145 | control-loop | Closed-loop step response vs Q: overshoot peak = 1 + exp(−π/sqrt(4Q^2 − 1)) for Q > 0.5 (Q = 1 → 16.3%, Q = 2 → 44.4%, large Q → 100%); Q = 0.5 (critically damped, f2 = 4·f0): 82% at t = 1/(2fc), 98.6% at t = 1/fc; overshoot is usually unacceptable in power supplies (a 3.3 V rail must not overshoot to 5–6 V) → often require Q ≤ 0.5, i.e. φm ≥ 76° | overshoot = exp(−π/sqrt(4Q^2 − 1)) | Q, fc | Start-up and reference steps | sim | §9.4.4 Eq.(9.42)–(9.46), Fig.9.26 p.373–375 | high |
| ERICKSON-1146 | control-loop | Load-step response of a closed-loop output impedance approximated as parallel RLC (characteristic impedance R0, resonance fc, Q): peak deviation ≈ I0·R0·Q (slightly less) for Q < 0.5, ≈ 0.368·I0·R0 at Q = 0.5, → I0·R0 as Q → ∞ | ΔV_pk ≈ I0·R0·Q (Q < 0.5); 0.368·I0·R0 (Q = 0.5); ≤ I0·R0 | I0, R0, Q | Load-transient budgeting | calc | §9.4.5 Eq.(9.47)–(9.50), Fig.9.27 p.375–376 | high |
| ERICKSON-1147 | control-loop | Crossover-frequency limit: compensator must have poles below fs to keep switching harmonics out of the PWM; this typically restricts fc to less than ≈10% of fs (design example uses fc = fs/20); also respect op-amp gain-bandwidth | fc < ≈0.1·fs | fc, fs, op-amp GBW | Voltage-mode PWM loops | calc | §9.5.1 p.377; §9.5.4 p.387 | high |
| ERICKSON-1148 | control-loop | Lead (PD) compensator sizing for phase boost θ at crossover fc (max phase at geometric mean of zero and pole); unity gain at fc (to keep fc) requires Gc0 = sqrt(fz/fp) | Gc = Gc0·(1 + s/ωz)/(1 + s/ωp); fφmax = sqrt(fz·fp); fz = fc·sqrt((1 − sin θ)/(1 + sin θ)); fp = fc·sqrt((1 + sin θ)/(1 − sin θ)); θ = atan((sqrt(fp/fz) − sqrt(fz/fp))/2) | fc, θ | Two-pole plants (buck voltage mode) | calc | §9.5.1 Eq.(9.53)–(9.58), Fig.9.29 p.378–379 | high |
| ERICKSON-1149 | control-loop | Lag (PI) compensator: inverted zero at fL sufficiently below fc keeps phase margin and drives dc error to zero; for a single-pole plant choose high-frequency gain for the desired crossover | Gc = Gc∞·(1 + ωL/s); fc ≈ Tu0·Gc∞·f0 → Gc∞ = fc/(Tu0·f0); design example uses fL = fc/10 | Tu0, f0, fc | PI / PID loops | calc | §9.5.2 Eq.(9.59)–(9.63) p.380–382 | high |
| ERICKSON-1150 | control-loop | PID compensator structure: inverted zero fL (integral), zero fz (phase lead), high-frequency poles fp1, fp2 (roll-off, keep switching ripple out of PWM); choose fL, fz < fc < fp1, fp2 | Gc = Gcm·(1 + ωL/s)·(1 + s/ωz)/((1 + s/ωp1)·(1 + s/ωp2)) | fL, fz, fc, fp1, fp2 | Voltage-mode regulators | calc | §9.5.3 Eq.(9.64), Fig.9.34 p.382–383 | high |
| ERICKSON-1151 | control-loop | Worked buck design (unit-test anchors): Vg = 28 V, V = 15 V, 5 A (R = 3 Ω), L = 50 μH, C = 500 μF, fs = 100 kHz, VM = 4 V, Vref = 5 V → H = 1/3, D = 0.536, Vc = 2.14 V, Gd0 = 28 V, f0 = 1 kHz, Q0 = 9.5 (19.5 dB), Tu0 = 2.33 (7.4 dB), uncompensated fc ≈ 1.8 kHz with φm < 5°; PD for fc = 5 kHz, φm = 52°: fz = 1.7 kHz, fp = 14.5 kHz, Gc0 = 3.7 (11.3 dB), T(0) = 8.6 (18.7 dB); 1 V at 100 Hz on vg → 0.062 V (PD) → 12 mV with fL = 500 Hz (−32.7 dB) | Gc0 = (fc/f0)^2·(1/Tu0)·sqrt(fz/fp) | as listed | Use as regression test for a compensator-design routine | calc | §9.5.4 Eq.(9.65)–(9.82) p.383–392 | high |
| ERICKSON-1152 | test | Loop-gain measurement by breaking the loop is impractical (dc bias drift, error-amp saturation with high dc gain, loading error Tm = T·(1 + Z1/Z2)); use voltage or current injection without breaking the loop so the circuit sets its own operating point | Tm = T·(1 + Z1/Z2) | Z1 (source), Z2 (load) at the injection point | Prototype loop verification | measure | §9.6 Eq.(9.83)–(9.87) p.392–393 | high |
| ERICKSON-1153 | test | Voltage-injection validity: Tv = T·(1 + Z1/Z2) + Z1/Z2 ≈ T provided abs(Z1) << abs(Z2) AND abs(T) >> abs(Z1/Z2); discard data where abs(T) < abs(Z1/Z2). Current injection (dual): Ti ≈ T provided abs(Z2) << abs(Z1) and abs(T) >> abs(Z2/Z1). Injection source impedance does not matter. Example: op-amp output 50 Ω driving 500 Ω → error 0.83 dB at high T, data invalid below −20 dB | Tv = T·(1 + Z1/Z2) + Z1/Z2 | Z1, Z2, T | Choose injection point (e.g. low-Z source → high-Z input) | measure | §9.6.1–9.6.2 Eq.(9.88)–(9.100) p.394–397 | high |
| ERICKSON-1154 | test | Measuring an unstable loop: add series resistance Rext at the voltage-injection point (bypass with Lext to keep dc bias) to lower loop gain and stabilize; the measured Tv still approximates the original unstable T | Tv unaffected by Zs = Rs + Rext | Rext, Lext | Debugging oscillating prototypes | measure | §9.6.3 Fig.9.53 p.397–398 | high |
| ERICKSON-1155 | magnetics | Basic magnetic relations (MKS): Faraday, Ampere, material law; relative permeability of core materials typically 10^3–10^5 | v = n·dΦ/dt = n·Ac·dB/dt; H·lm = n·i; B = μr·μ0·H; μ0 = 4π·10^-7 H/m; Φ = B·Ac | n, Ac, lm, μr | Lumped magnetic analysis | calc | §10.1.1 Eq.(10.4)–(10.14) p.410–414 | high |
| ERICKSON-1156 | magnetics | Typical saturation flux densities by material (use for Bmax limits) | iron laminations / silicon steel 1–2 T (text also 1.5–2 T); powdered iron & molypermalloy 0.5–1 T (§10.1) / 0.6–0.8 T (§10.3); amorphous alloys 0.6–1.5 T; ferrite 0.25–0.5 T | material | Bmax must stay below Bsat with margin at worst-case peak current / volt-seconds | review | §10.1.1 p.412; §10.3.1 p.424–425 | high |
| ERICKSON-1157 | magnetics | Ungapped inductor: inductance and saturation current (device approaches a short circuit above Isat) | L = μ·n^2·Ac/lm; Isat = Bsat·lm/(μ·n) | μ, n, Ac, lm, Bsat | No air gap; hysteresis neglected | calc | §10.1.1 Eq.(10.16)–(10.21) p.415 | high |
| ERICKSON-1158 | magnetics | Magnetic-circuit (reluctance) model; gapped inductor inductance and saturation current. A gap with Rg > Rc makes L insensitive to core μ (temperature/operating point) and raises Isat at the cost of lower L | R = l/(μ·Ac); Rc = lc/(μ·Ac); Rg = lg/(μ0·Ac); L = n^2/(Rc + Rg); Isat = Bsat·Ac·(Rc + Rg)/n | n, lc, lg, Ac, μ, Bsat | Filter inductors, flyback transformers (fringing neglected) | calc | §10.1.2 Eq.(10.25)–(10.33) p.416–418 | high |
| ERICKSON-1159 | magnetics | Magnetizing inductance and current of a transformer (referred to primary); magnetizing current makes winding-current ratio deviate from turns ratio | LM = n1^2/R; iM = i1 + (n2/n1)·i2 | n1, n2, R | Two-winding transformers | calc | §10.2.2 Eq.(10.41)–(10.44) p.420 | high |
| ERICKSON-1160 | magnetics | Transformer saturation is set by applied volt-seconds, not by load current; fix by more primary turns or larger Ac — an air gap does NOT help (only lowers LM and raises iM) | B(t) = (1/(n1·Ac))·∫ v1 dt; λ1 = ∫ v1 dt over the positive portion; total flux-density swing = λ1/(n1·Ac), peak ac ΔB = λ1/(2·n1·Ac) (Fig.10.46) | λ1, n1, Ac | Conventional (non-flyback) transformers | calc | §10.2.2 Eq.(10.45)–(10.47) p.421; Key pt 7 p.450 | high |
| ERICKSON-1161 | magnetics | Leakage/coupled-inductor terminal model: mutual, self inductances, effective turns ratio and coupling coefficient; low-voltage transformers with k > 0.99 are quite feasible | L12 = n1·n2/R = (n2/n1)·LM; L11 = Ll1 + (n1/n2)·L12; L22 = Ll2 + (n2/n1)·L12; ne = sqrt(L22/L11); k = L12/sqrt(L11·L22), 0 ≤ k ≤ 1 | measured L11, L22, L12 | Two-winding magnetics | measure | §10.2.3 Eq.(10.48)–(10.52) p.422–423 | high |
| ERICKSON-1162 | magnetics | Hysteresis loss = core volume × B–H loop area × frequency (loop size independent of f → loss ∝ f); core eddy-current loss ∝ f^2 (faster than f^2 in power ferrites) | P_H = f·Ac·lm·∮H dB | f, Ac, lm, loop | Core-loss reasoning | calc | §10.3.1 Eq.(10.53)–(10.56) p.423–424 | high |
| ERICKSON-1163 | magnetics | Core-material tradeoff (Bsat vs core loss): silicon steel (1.5–2 T, high loss, laminated) for filter inductors and low-frequency transformers; powdered iron / MPP (0.6–0.8 T, distributed gap, low μ) for kHz transformers and 100 kHz filter inductors; amorphous (0.6–1.5 T, low hysteresis); MnZn ferrite (0.25–0.5 T, high resistivity) for 10 kHz–1 MHz inductors/transformers; NiZn ferrite for higher frequencies | — | fs, application | Material selection | review | §10.3.1 p.424–425; Key pt 8 p.450 | high |
| ERICKSON-1164 | magnetics | Steinmetz-type core-loss model fitted to vendor data; β typically 2.6–2.8 for ferrites in their intended range; Kfe rises rapidly with frequency (fit Kfe0·f^ξ or a 4th-order polynomial) | Pfe = Kfe·(ΔB)^β·Ac·lm (ΔB = peak ac flux density) | Kfe, β, ΔB, Ac·lm | Sinusoidal-excitation data; see [96] for non-sinusoidal | calc | §10.3.1 Eq.(10.57), Fig.10.20 p.425 | high |
| ERICKSON-1165 | magnetics | Low-frequency copper loss and winding resistance; copper resistivity 1.724·10^-6 Ω·cm at room temperature (soft-annealed), 2.3·10^-6 Ω·cm at 100°C | Pcu = Irms^2·R; R = ρ·lb/Aw = ρ·n·MLT/Aw | ρ(T), n, MLT, Aw, Irms | Use hot resistivity for worst case | calc | §10.3.2 Eq.(10.58)–(10.60) p.426 | high |
| ERICKSON-1166 | magnetics | Skin (penetration) depth; copper at 100°C; d/δ = 1 for AWG #40 at ≈500 kHz and for AWG #22 at ≈10 kHz | δ = sqrt(ρ/(π·μ·f)); copper, 100°C: δ = 7.5/sqrt(f) cm (f in Hz) | ρ, f | Wire/foil sizing | calc | §10.4.1 Eq.(10.61)–(10.62), Fig.10.23 p.427–428 | high |
| ERICKSON-1167 | magnetics | Proximity effect in a thick-foil (h >> δ) M-layer non-interleaved winding: loss of layer m and total loss factor — copper loss compounds rapidly with layer count | Rac = (h/δ)·Rdc; Pm = I^2·((m − 1)^2 + m^2)·(h/δ)·Rdc; FR = P/Pdc = (1/3)·(h/δ)·(2M^2 + 1) | h, δ, M, Rdc | h >> δ foil layers, simple geometry | calc | §10.4.1 Eq.(10.63)–(10.69) p.429–430 | high |
| ERICKSON-1168 | magnetics | Round-wire layer → equivalent foil (Dowell): equivalent thickness, porosity, effective ϕ (typical porosity 0.8 for round wire spanning the bobbin) | h = sqrt(π/4)·d; η = sqrt(π/4)·n·d/lw; δ' = δ/sqrt(η); ϕ = h/δ' = sqrt(η)·sqrt(π/4)·d/δ | d, n, lw (layer width), δ | Layers of round conductors | calc | §10.4.3 Eq.(10.71)–(10.74) p.433 | medium |
| ERICKSON-1169 | magnetics | Dowell layer loss for sinusoidal current with surface MMFs F(0), F(h) (in phase): define m = F(h)/(F(h) − F(0)) (swap ends so m ≥ 0.5 for plotting) | P = I^2·Rdc·ϕ·Q'(ϕ, m); Q' = (2m^2 − 2m + 1)·G1(ϕ) − 4m(m − 1)·G2(ϕ); G1 = (sinh 2ϕ + sin 2ϕ)/(cosh 2ϕ − cos 2ϕ); G2 = (sinh ϕ·cos ϕ + cosh ϕ·sin ϕ)/(cosh 2ϕ − cos 2ϕ); large ϕ: Q' → m^2 + (m − 1)^2 | ϕ, m, I, Rdc | Coaxial solenoidal windings, fields parallel to layers | calc | §10.4.4 Eq.(10.75)–(10.83), Figs.10.31–10.32 p.434–436; §10.4.6 Eq.(10.89) p.439 | high |
| ERICKSON-1170 | magnetics | Total AC-resistance factor of an M-layer (per winding) non-interleaved transformer; minimum loss for sinusoidal current at ϕ near or somewhat below 1 | FR = ϕ·[G1(ϕ) + (2/3)·(M^2 − 1)·(G1(ϕ) − 2·G2(ϕ))]; P/Pdc,ϕ=1 = FR/ϕ | ϕ, M | Sinusoidal currents | calc | §10.4.5 Eq.(10.84)–(10.88), Figs.10.34–10.35 p.436–438 | high |
| ERICKSON-1171 | magnetics | Interleave primary and secondary layers to cut proximity loss: fully interleaved layers operate at m = 1 (use M = 1 curves); minimum at ϕ = π/2, loss nearly constant for ϕ ≥ 1 and ≈ the dc loss at ϕ = 1. Interleaving does little when winding currents are out of phase (flyback, SEPIC transformers). Minimize layer count, maximize layer width, keep copper away from high-MMF regions | m = 1 per layer when fully interleaved | winding order | In-phase currents (forward, bridge) | calc | §10.4.6 p.438–440 | high |
| ERICKSON-1172 | magnetics | Litz wire: strands must be sufficiently smaller than one skin depth in diameter and fully transposed; costs more and lowers fill factor; the bundle itself is multi-layer | d_strand << δ | δ, strand d | HF windings | review | §10.4.6 p.440–441 | high |
| ERICKSON-1173 | magnetics | PWM winding-current harmonics raise proximity loss: harmonic j sees ϕj = sqrt(j)·ϕ1; exclude the dc component from proximity calculations (including it is significantly pessimistic); with high THD and several layers keep ϕ1 much less than 1 or interleave | I0 = D·Ipk; Ij = (sqrt(2)·Ipk/(j·π))·sin(j·π·D) (rms); Pcu = I0^2·Rdc + FH·FR·I1^2·Rdc; FH = Σ Pj/P1 → 1 + THD^2 for small ϕ1; THD = sqrt(Σ_{j≥2} Ij^2)/I1 = 48% (D = 0.5), 76% (D = 0.3), 191% (D = 0.1) | D, Ipk, ϕ1, M | Forward-type rectangular winding currents | calc | §10.4.7 Eq.(10.94)–(10.101), Fig.10.39 p.441–443 | high |
| ERICKSON-1174 | magnetics | Device-type loss regime (sets the design method): filter inductor & coupled inductor — minor B–H loop, core loss usually negligible, proximity negligible, Bmax limited by saturation, copper loss dominates (Kg method); ac inductor & conventional transformer — large ac flux, Bmax limited by core loss, proximity significant, choose ΔB to minimize total loss (Kgfe method); flyback transformer — gapped, DCM → core loss significant (limit ΔB), CCM → saturation-limited, proximity typically significant | — | device type, mode | Magnetics design flow selection | review | §10.5 p.444–450 | high |
| ERICKSON-1175 | magnetics | Coupled inductors: filter inductors whose winding voltages are proportional (multi-output forward, SEPIC, Ćuk) can share one core; ripple distribution is set by leakage inductances, and by proper turns ratio/gaps the ripple in one winding can be driven to zero | net core H ∝ n1·i1 + n2·i2 | n1/n2, gaps | Converters with proportional inductor voltages | calc | §10.5.4 Eq.(10.105) p.448; Problem 10.4 p.453–454 | high |
| ERICKSON-1176 | magnetics | Filter-inductor design constraints (gap-dominated magnetic circuit, Rc << Rg; core and proximity losses neglected, copper loss dominant) | n·Imax = Bmax·lg/μ0; L = μ0·Ac·n^2/lg; Ku·WA ≥ n·AW; R = ρ·n·MLT/AW; Pcu = Irms^2·R | L, Imax, Bmax, R, Ku | DC-biased filter inductors | calc | §11.1 Eq.(11.1)–(11.13) p.460–463 | high |
| ERICKSON-1177 | magnetics | Window fill factor Ku (copper area / window area): typical 0.5 simple low-voltage inductor; 0.25–0.3 off-line transformer; 0.05–0.2 high-voltage (several kV) transformer; 0.65 low-voltage foil transformer/inductor. Round-wire packing alone costs a factor 0.7–0.55; insulation ratio 0.95–0.65 | Ku per above | construction | Magnetics sizing | review | §11.1.3 p.462 | high |
| ERICKSON-1178 | magnetics | Kg core-size criterion for filter inductors (cm units) | Kg = Ac^2·WA/MLT ≥ ρ·L^2·Imax^2/(Bmax^2·R·Ku) × 10^8  [cm^5] (ρ in Ω·cm, L in H, Imax in A, Bmax in T, R in Ω; Ac, WA in cm^2, MLT in cm) | ρ, L, Imax, Bmax, R, Ku | Copper-loss-limited, saturation-limited designs | calc | §11.1.5–11.2 Eq.(11.14)–(11.16) p.463–464 | high |
| ERICKSON-1179 | magnetics | Kg-method turns, gap, AL, wire and resistance (first pass; fringing raises L so a somewhat longer gap is needed) | n = L·Imax·10^4/(Bmax·Ac); lg = μ0·Ac·n^2·10^-4/L [m]; AL = 10·Bmax^2·Ac^2/(L·Imax^2) [mH/1000 turns]; AW ≤ Ku·WA/n [cm^2]; R = ρ·n·MLT/AW [Ω] | L, Imax, Bmax, Ac, WA, MLT, Ku | First-pass filter inductor | calc | §11.2 Eq.(11.17)–(11.21) p.464–465 | high |
| ERICKSON-1180 | magnetics | Kg sensitivities: larger L or Imax → larger core; higher Bmax (high-Bsat material) → smaller core; allowing more winding resistance → smaller core but higher temperature rise; iron (Ac) can be traded for copper (WA) at constant Kg | Kg ∝ L^2·Imax^2/(Bmax^2·R) | — | Core selection | review | §11.1.5 p.463–464 | high |
| ERICKSON-1181 | magnetics | Optimal window-area allocation among windings minimizes total low-frequency copper loss: allocate in proportion to apparent power (ampere-turns) | αm = Vm·Im/Σ Vj·Ij = nm·Im/Σ nj·Ij; Pcu,min = ρ·MLT·(Σ nj·Ij)^2/(WA·Ku) | nj, Ij (rms) | Multi-winding magnetics | calc | §11.3.1 Eq.(11.23)–(11.36) p.465–468 | high |
| ERICKSON-1182 | magnetics | Full-bridge centre-tapped-secondary transformer rms currents and optimal window split (D = 0.75 → 40% primary, 30% each secondary half) | I1 = (n2/n1)·I·sqrt(D); I2 = I3 = 0.5·I·sqrt(1 + D); α1 = 1/(1 + sqrt((1 + D)/D)); α2 = α3 = 0.5/(1 + sqrt(D/(1 + D))); Pcu = ρ·MLT·n2^2·I^2·(1 + 2D + 2·sqrt(D·(1 + D)))/(WA·Ku) | D, I, n1, n2 | Buck-derived bridge transformers | calc | §11.3.1 Eq.(11.37)–(11.42) p.468–470 | high |
| ERICKSON-1183 | magnetics | Coupled-inductor / flyback-transformer Kg method (air gap; core and proximity loss not included) | iM = i1 + Σ (nj/n1)·ij; n1·IM,max = Bmax·lg/μ0; LM = μ0·Ac·n1^2/lg; Itot = Σ (nj/n1)·Ij; Kg ≥ ρ·LM^2·Itot^2·IM,max^2·10^8/(Bmax^2·Pcu·Ku) [cm^5]; lg = μ0·LM·IM,max^2·10^4/(Bmax^2·Ac) [m]; n1 = LM·IM,max·10^4/(Bmax·Ac); αj = nj·Ij/(n1·Itot); Awj ≤ αj·Ku·WA/nj | LM, IM,max, Itot, Bmax, Pcu, Ku | Coupled inductors, flyback and SEPIC transformers | calc | §11.3.2–11.3.3 Eq.(11.43)–(11.57) p.470–473 | high |
| ERICKSON-1184 | magnetics | Worked coupled-inductor example (unit-test anchors): two-output forward 28 V/4 A + 12 V/2 A, D = 0.35, fs = 200 kHz, ΔiM = 20% of IM → IM = 4.86 A, LM = 47 μH, IM,max = 5.83 A; Pcu = 0.75 W, Bmax = 0.25 T, Ku = 0.4 → Kg ≥ 16·10^-3 cm^5; PQ 20/16 (Kg 22.4·10^-3 cm^5, Ac 0.62 cm^2, WA 0.256 cm^2, MLT 4.4 cm) → lg = 0.52 mm, n1 = 17.6 → 17, n2 = 7.54 → 7, α1 = 0.8235, α2 = 0.1695, AWG #21 / #24 | LM = V1·D'·Ts/(2·ΔiM) | as listed | Regression test for a magnetics tool | calc | §11.4.1 Eq.(11.58)–(11.68) p.474–476 | high |
| ERICKSON-1185 | magnetics | Worked CCM flyback-transformer example: Vg = 200 V → 20 V/5 A, fs = 150 kHz, D = 0.4, n2/n1 = 0.15, ΔiM = 20%, Pcu = 1.5 W, Ku = 0.3, Bmax = 0.25 T → IM = 1.25 A, IM,max = 1.5 A, LM = 1.07 mH, I1 = 0.796 A, I2 = 6.50 A, Itot = 1.77 A, Kg ≥ 0.049 cm^5 → EE30 (Kg 0.0857 cm^5; Ac 1.09 cm^2, WA 0.476 cm^2, MLT 6.6 cm, lm 5.77 cm), lg = 0.44 mm, n1 = 59, n2 = 9, α 0.45/0.55, AWG #28/#19; ΔB = 0.041 T, core loss 0.04 W/cm^3 → 0.25 W (< 1.5 W copper: neglecting core loss is often warranted for CCM ferrite designs) | ΔB = Vg·D·Ts·10^4/(2·n1·Ac); LM = Vg·D·Ts/(2·ΔiM) | as listed | Regression test | calc | §11.4.2 Eq.(11.69)–(11.90) p.476–481 | high |
| ERICKSON-1186 | magnetics | Flyback winding rms currents with magnetizing ripple — secondary rms is NOT turns ratio × primary rms | I1 = IM·sqrt(D)·sqrt(1 + (ΔiM/IM)^2/3); I2 = (n1/n2)·IM·sqrt(D')·sqrt(1 + (ΔiM/IM)^2/3) | IM, ΔiM, D, n1/n2 | CCM flyback | calc | §11.4.2 Eq.(11.73)–(11.74) p.478 (OCR prints sqrt(D) for I2; D' verified numerically: 6.50 A) | medium |
| ERICKSON-1187 | magnetics | Core-loss-limited transformer: peak ac flux density from applied volt-seconds; more turns → lower core loss, more copper loss; a dc flux bias (forward converter) does not significantly change core loss unless near saturation | ΔB = λ1/(2·n1·Ac); n1 = λ1/(2·ΔB·Ac); Pfe = Kfe·ΔB^β·Ac·lm (β ≈ 2.6 ferrite, 2–3 others) | λ1, n1, Ac, Kfe, β | Transformers, ac inductors | calc | §12.1.1–12.1.2 Eq.(12.1)–(12.4) p.486–487 | high |
| ERICKSON-1188 | magnetics | Copper loss vs ΔB and loss-minimizing flux density (optimum is where dPfe/dΔB = −dPcu/dΔB, NOT where Pfe = Pcu; derived consequence: at the optimum Pcu = (β/2)·Pfe) | Pcu = (ρ·λ1^2·Itot^2/(4·Ku))·(MLT/(WA·Ac^2))·ΔB^-2; ΔBopt = [10^8·(ρ·λ1^2·Itot^2/(2·Ku))·(MLT/(WA·Ac^3·lm))·(1/(β·Kfe))]^(1/(β+2)) (cm units) | ρ, λ1, Itot, Ku, core geometry, Kfe, β | Proximity loss via ρeff = ρ·Pcu/Pdc | calc | §12.1.3–12.1.5 Eq.(12.5)–(12.13), (12.20) p.487–491 | high |
| ERICKSON-1189 | magnetics | Kgfe core-size criterion for core-loss-limited magnetics (Kgfe varies ≤ ±5% for β = 2.6–2.8; tables at β = 2.7) | Kgfe = WA·Ac^(2(β−1)/β)/(MLT·lm^(2/β))·[(β/2)^(−β/(β+2)) + (β/2)^(2/(β+2))]^(−(β+2)/β); require Kgfe ≥ ρ·λ1^2·Itot^2·Kfe^(2/β)·10^8/(4·Ku·Ptot^((β+2)/β)) | λ1, Itot, Ku, Ptot, Kfe, β | Transformers (ac inductor: replace 4 with 2 and Itot with I) | calc | §12.1.5–12.2 Eq.(12.15)–(12.19) p.489–490 | high |
| ERICKSON-1190 | magnetics | Kgfe procedure checks: after ΔBopt verify ΔB (+ any dc bias) is below Bsat with margin — otherwise use a higher-loss material or the Kg (Bmax-specified) method; turns n1 = λ1·10^4/(2·ΔB·Ac); allocate windows by αj; iterate with ρeff = ρcu·Pcu/Pdc when proximity loss is significant; model estimates LM = μ·n1^2·Ac/lm, iM,pk = λ1/(2·LM), Rj = ρ·nj·MLT/Awj | as listed | — | Transformer first-pass design | calc | §12.2.1 Eq.(12.20)–(12.24) p.491–492 | high |
| ERICKSON-1191 | magnetics | Worked isolated-Ćuk transformer example: Vg = 25 V (4 A in), 5 V/20 A, D = 0.5, fs = 200 kHz, n = 5, Kfe = 24.7 W/(T^β·cm^3), β = 2.6, Ku = 0.5, Ptot = 0.25 W → λ1 = 62.5 V·μs, I1 = 4 A, I2 = 20 A, Itot = 8 A, Kgfe ≥ 0.00295 → 2213 pot core (Kgfe 0.0049 at β = 2.7, 0.0047 at 2.6), ΔB = 0.0858 T (Bsat ≈ 0.35 T), n1 = 5.74, n2 = 1.15, α = 0.5/0.5 → AWG #16 / #9 (single #9 turn impractical: use interleaved foil, Litz or parallel strands) | — | as listed | Regression test | calc | §12.3.1 Eq.(12.25)–(12.34) p.492–495 | high |
| ERICKSON-1192 | magnetics | Transformer size vs switching frequency: size falls with fs (λ1 ∝ Ts) until Kfe growth forces ΔB down; for the Ćuk example (P material, Ptot < 0.25 W) the smallest pot core occurs at ≈250 kHz; reported ferrite optima range from several hundred kHz to several MHz | optimum fs where d(Kgfe_required)/df = 0 | Kfe(f) | Frequency selection | calc | §12.3.1 Fig.12.7 p.495–496; Problem 12.4 p.504–505 | high |
| ERICKSON-1193 | magnetics | Worked multi-output full-bridge transformer: 160 V in, 5 V/100 A + 15 V/15 A, D = 0.75, fs = 150 kHz (transformer 75 kHz), 110:5:15, Kfe = 7.6, β = 2.6, Ku = 0.25, Ptot = 4 W (≈0.5% of load) → λ1 = 800 V·μs, I1 = 5.7 A, I2 = 66.1 A, I3 = 9.9 A, Itot = 14.4 A, Kgfe ≥ 0.00937 → EE40 (ΔBopt 0.23 T, n1 = 13.7); rounding to 22:1:3 gives ΔB = 0.143 T, Pfe = 0.47 W, Pcu = 5.4 W, Ptot = 5.9 W (fails) → EE50 (Kgfe 0.0284) with n1 = 22: ΔB = 0.08 T, Pfe = 0.23 W, Pcu = 3.89 W, Ptot = 4.12 W; α = 0.396/0.209/0.094 → AWG #19, #8, #16. Lesson: re-check losses after turns round-off | — | as listed | Regression test | calc | §12.3.2 Eq.(12.35)–(12.52) p.496–499 | high |
| ERICKSON-1194 | magnetics | AC inductor with significant core loss (gapped): design equations | ΔB = λ·10^4/(2·n·Ac); Pcu = ρ·n^2·MLT·I^2/(Ku·WA); Kgfe ≥ ρ·λ^2·I^2·Kfe^(2/β)·10^8/(2·Ku·Ptot^((β+2)/β)); ΔBopt = [10^8·(ρ·λ^2·I^2/(2·Ku))·(MLT/(WA·Ac^3·lm))·(1/(β·Kfe))]^(1/(β+2)); lg = μ0·Ac·n^2·10^-4/L [m]; AL = 10^9·L/n^2 [mH/1000 turns]; Aw ≤ Ku·WA/n | λ, I (rms), L | Resonant-tank and ac inductors | calc | §12.4 Eq.(12.53)–(12.65) p.500–502 | high |
| ERICKSON-1195 | magnetics | Saturation check for an inductor carrying dc plus large ac: if Bmax nears Bsat, redesign with the Kg (filter-inductor) method at lower flux density | Bmax = ΔB + L·Idc·10^4/(n·Ac) < Bsat | ΔB, L, Idc, n, Ac | AC inductors with dc bias | calc | §12.4.2 Eq.(12.63) p.501 | high |
| ERICKSON-1196 | derating | Flux-density and thermal margins used in the book's design problems: Bmax no greater than 75% of the hot saturation flux density (ferrite ≈0.3 T at 120°C → Bmax ≤ 0.225 T); evaluate copper loss at 100°C; transformer Ku ≈ 0.35 vs 0.5 for inductors to leave room for inter-winding insulation | Bmax ≤ 0.75·Bsat(T_hot) | Bsat(T), Ku | Ferrite magnetics | calc | Problem 12.1 p.502–503 | high |
| ERICKSON-1197 | thermal | Magnetic-component temperature rise is approximately proportional to its total loss (weak dependence on loss distribution) — allows designing to a temperature-rise limit instead of a loss limit | ΔT = Rth·Ptot (Rth of the core in the given environment; EC-core values in Appendix B.3) | Rth, Ptot | Ferrite transformers/inductors | calc | Problem 12.5 p.505 | medium |
| ERICKSON-1198 | control-loop | Middlebrook feedback theorem (null double injection) for analysing real loops without idealized blocks: inject immediately after a source proportional to the error signal with no parallel forward path; then G = G∞·T/(1 + T) + G0/(1 + T), with T = uy/ux (input zeroed), G∞ = uo/ui with uy nulled (ideal/virtual-ground gain), G0 = uo/ui with ux nulled (direct transmission / open-loop disturbance path), reciprocity Tn = G∞·T/G0 (solve any three) | G = G∞·(1 + 1/Tn)/(1 + 1/T) | G∞, G0, T, Tn | Closed-loop regulators, op-amp compensators | calc | §13.2 Eq.(13.1)–(13.6), (13.39)–(13.42) p.510–518 | high |
| ERICKSON-1199 | control-loop | Op-amp lead (PD) compensator: input network R1 ‖ (R2 + 1/(sC)), feedback R3 (ideal op amp); example R1 = R3 = 1.6 kΩ, R2 = 16 Ω, C = 0.1 μF → 0 dB, zero 1 kHz, pole 100 kHz (suits fc ≈ 10 kHz). Check real op-amp effects (example model: 100 dB dc gain, 10 Hz pole → 1 MHz unity-gain, Ro = 50 Ω, RL = 100 Ω; direct transmission G0 = 0.0103, −39.7 dB) with the feedback theorem | G∞ = −(R3/R1)·(1 + s·(R1 + R2)·C)/(1 + s·R2·C); f_z = 1/(2π·(R1 + R2)·C); f_p = 1/(2π·R2·C) | R1, R2, R3, C | Analog compensators; finite GBW results continue beyond this extraction range | calc | §13.3 Eq.(13.43)–(13.59) p.519–524 | high |


## 2. Formulas & tables (numbers)

### 2.1 Steady-state CCM relations of the basic converters (ideal elements, small ripple)
Ripple values are PEAK (half of peak-to-peak), as in the book. Sources: Ch.2 Eqs.(2.15),(2.35)–(2.47),(2.53),(2.57),(2.60); Ch.6 §6.2 (conversion ratios of the "short list").

| converter | M(D) = V/Vg | dc inductor current(s) | inductor ripple ΔiL (peak) | output-cap ripple Δv (peak) | source |
|---|---|---|---|---|---|
| buck | D | I = V/R | (Vg − V)·D·Ts/(2L) = Vg·D·D'·Ts/(2L) | ΔiL·Ts/(8C) (two-pole filter) | Eq.(2.15),(2.60) |
| boost | 1/D' | I = V/(D'R) = Vg/(D'^2 R) | Vg·D·Ts/(2L) | V·D·Ts/(2RC) | Eq.(2.35),(2.39),(2.43),(2.47) |
| buck–boost (inverting) | −D/D' | see Ch.6 rows | Vg·D·Ts/(2L) (applied voltage Vg during DTs) | V·D·Ts/(2RC) (magnitude; pulsating output) | Fig.2.5; ripple forms derived like boost (medium) |
| Ćuk | −D/D' | I1 = (D/D')^2·Vg/R ; I2 = −(D/D')·Vg/R | Δi1 = Vg·D·Ts/(2L1); Δi2 = Vg·D·Ts/(2L2) | Δv1 (C1) = Vg·D^2·Ts/(2·D'·R·C1); output: Δi2·Ts/(8C2) | Eq.(2.53),(2.57) |

Buck–boost row ripple expressions are derived by the same method as Eqs.(2.43),(2.47) (book leaves them as Problem 2.1): conf = medium.

### 2.2 Effect of inductor current ripple on MOSFET conduction loss (buck) — Table 3.1, p.60

| inductor current ripple | MOSFET rms current | average power loss in Ron |
|---|---|---|
| (a) Δi = 0 | I·sqrt(D) | D·I^2·Ron |
| (b) Δi = 0.1·I | (1.00167)·I·sqrt(D) | (1.0033)·D·I^2·Ron |
| (c) Δi = I | (1.155)·I·sqrt(D) | (1.3333)·D·I^2·Ron |

### 2.3 Boost converter with inductor copper loss (Fig.3.9 / Fig.3.15 anchors, p.49, p.53)
- V/Vg = (1/D')·1/(1 + RL/(D'^2 R)); η = 1/(1 + RL/(D'^2 R)). Curves plotted for RL/R = 0, 0.01, 0.02, 0.05, 0.1 (Fig.3.9) and 0.002, 0.01, 0.02, 0.05, 0.1 (Fig.3.15).
- Anchor stated in text: RL/R = 0.02 → max V/Vg ≈ 3.5; V/Vg = 5 needs RL/R < 0.01.
- Derived closed form (medium): max of V/Vg is 0.5·sqrt(R/RL) at D' = sqrt(RL/R); at that point η = 50%.
### 2.4 Table 4.1 — Characteristics of several commercial power rectifier diodes (p.89)

| class | part number | rated max voltage | rated average current | VF (typical) | tr (max) |
|---|---|---|---|---|---|
| fast recovery | 1N3913 | 400 V | 30 A | 1.1 V | 400 ns |
| fast recovery | SD453N2S20PC (as printed) | 2500 V | 400 A | 2.2 V | 3 μs |
| ultrafast recovery | MUR815 | 150 V | 8 A | 0.975 V | 35 ns |
| ultrafast recovery | RHRD660 | 600 V | 6 A | 1.7 V | 35 ns |
| ultrafast recovery | RHRU100120 | 1200 V | 100 A | 2.6 V | 60 ns |
| Schottky | MBR6030L | 30 V | 60 A | 0.48 V | — |
| Schottky | 444CNQ045 | 45 V | 440 A | 0.69 V | — |
| Schottky | 30CPQ150 | 150 V | 30 A | 1.19 V | — |
| SiC Schottky | C4D10120E | 1200 V | 10 A | 1.8 V | — |
| SiC Schottky | C3D3060F | 600 V | 3 A | 1.7 V | — |

### 2.5 Table 4.2 — Characteristics of several commercial n-channel power MOSFETs (p.103)
Ron typical at 25°C; Qg typical (to 10 V gate, at ≈80% rated VDS per the book's definition).

| part number | rated max voltage | rated average current | Ron | Qg (typical) |
|---|---|---|---|---|
| SiSS64DN | 30 V | 40 A | 2.1 mΩ | 21 nC |
| CSD18512Q5B | 40 V | 100 A | 1.3 mΩ | 75 nC |
| NTMFS6H800N | 80 V | 203 A | 1.8 mΩ | 85 nC |
| IXFH80N25X3 | 250 V | 80 A | 13 mΩ | 83 nC |
| IPL60R065P7 (superjunction) | 650 V | 41 A | 53 mΩ | 67 nC |

### 2.6 Table 4.3 — Comparison of power semiconductor materials (p.104; book ref [42])

| material | bandgap (eV) | electron mobility μn (cm^2/V·s) | relative permittivity εs | critical field Ec (V/cm) | thermal conductivity (W/m·K) |
|---|---|---|---|---|---|
| Si | 1.1 | 1350 | 11.8 | 3·10^5 | 150 |
| SiC (4H) | 3.26 | 720 | 10 | 2·10^6 | 450 |
| GaN | 3.44 | 1500–2000 (2DEG, HEMT) | 9 | 3.3·10^6 | 130 |

Specific on-resistance of a majority-carrier drift region (Eq.4.40): A·Ron is proportional to VB^2/(μn·εs·Ec^3), with a process constant k (OCR does not preserve whether k multiplies or divides). Stated consequence: an order-of-magnitude increase in Ec gives three orders of magnitude lower Ron at the same breakdown voltage (p.104). Text also quotes Si ≈ 1.1 eV, SiC ≈ 3.2 eV, GaN 3.4 eV (p.80).

### 2.7 Table 4.4 — Characteristics of several commercial SiC MOSFETs (p.105)

| part number | rated max voltage | rated average current | Ron | Qg (typical) |
|---|---|---|---|---|
| C3M0030090K | 900 V | 63 A | 30 mΩ | 87 nC |
| C3M0075120K | 1200 V | 30 A | 75 mΩ | 51 nC |
| C2M0045170D | 1700 V | 72 A | 45 mΩ | 188 nC |
| SCT3022AL | 650 V | 93 A | 22 mΩ | 133 nC |
| CPM3-0900-0010A | 900 V | 196 A | 10 mΩ | 68 nC |

### 2.8 Table 4.5 — Comparison of Si superjunction MOSFET and GaN FET (p.107)

| parameter | Si SJ MOSFET | GaN FET |
|---|---|---|
| voltage rating | 650 V | 650 V |
| Ron, 25–150°C | 24–60 mΩ | 25–50 mΩ |
| Qg at VDS = 400 V | 123 nC (10 V gate) | 12 nC (6 V gate) |
| VSD (reverse conduction, VGS = 0) | 0.8 V | 4 V |
| Qrr | 8.7 μC | — (none) |
| trr | 440 ns | — (none) |

### 2.9 Table 4.6 — Characteristics of several commercial IGBTs (p.119)

| class | part number | rated max voltage | rated average current | VF (typical) | tf (typical) |
|---|---|---|---|---|---|
| single-chip | HGTP12N60A4 | 600 V | 23 A | 2.0 V | 70 ns |
| single-chip | HGTG32N60E2 | 600 V | 32 A | 2.4 V | 0.62 μs |
| single-chip | HGTG30N120D2 | 1200 V | 30 A | 3.2 V | 0.58 μs |
| multiple-chip module | CM400HA-12E | 600 V | 400 A | 2.7 V | 0.3 μs |
| multiple-chip module | CM300HA-24E | 1200 V | 300 A | 2.7 V | 0.3 μs |
| multiple-chip module | CM800HA-34H | 1700 V | 800 A | 3.3 V | 0.6 μs |
| high-voltage module | CM800HB-50H | 2500 V | 800 A | 3.15 V | 1.0 μs |
| high-voltage module | CM600HB-90H | 4500 V | 900 A | 3.3 V | 1.2 μs |

### 2.10 Switching-loss energy terms (Ch.4)

| mechanism | energy per switching period | where dissipated | source |
|---|---|---|---|
| hard turn-off, clamped inductive load | W_off = 0.5·Vg·iL·(t_fall_total) | transistor | Eq.(4.5) |
| hard turn-on, clamped inductive load | W_on = 0.5·Vg·iL·t_on | transistor | §4.2.2 p.82 |
| diode reverse recovery (buck) | W_D = Vg·(Qr + IL·tr) | transistor (S = 0), shared if S > 0 | Eq.(4.19) |
| diode reverse recovery (boost) | W_D = V·(Qr + IL·tr) | transistor + diode | Eq.(4.32) |
| linear output/junction capacitances | W_C = 0.5·(Cds + Cj)·Vg^2 | transistor at turn-on | Eq.(4.42) |
| nonlinear Cds (∝ 1/sqrt(v)) | W_Cds = (2/3)·Cds(VDS)·VDS^2 | transistor at turn-on | Eq.(4.44) |
| series (leakage/package) inductance | W_L = 0.5·L·I^2 | transistor at turn-off (+ overvoltage) | Eq.(4.41) |
| diode stored charge ringing in L–C | W = V2·Qr | parasitic resistances | Eq.(4.49) |
| total → power | P_sw = Wtot·fsw; Ploss = Pcond + Pfixed + Wtot·fsw; fcrit = (Pcond + Pfixed)/Wtot | — | Eq.(4.50)–(4.53) |
### 2.11 Tables 5.1 / 5.2 — CCM–DCM boundaries and DCM conversion ratios (p.140, p.153); K = 2L/(R·Ts)
DCM occurs for K < Kcrit (equivalently R > Rcrit).

| converter | Kcrit(D) | max Kcrit over 0 ≤ D ≤ 1 | Rcrit(D) | min Rcrit | CCM M(D) | DCM M(D,K) | DCM D2(D,K) |
|---|---|---|---|---|---|---|---|
| buck | 1 − D | 1 | 2L/((1 − D)·Ts) | 2L/Ts | D | 2/(1 + sqrt(1 + 4K/D^2)) | K·M/D |
| boost | D·(1 − D)^2 | 4/27 (at D = 1/3) | 2L/(D·(1 − D)^2·Ts) | 27L/(2Ts) | 1/(1 − D) | (1 + sqrt(1 + 4D^2/K))/2 | K·M/D |
| buck–boost | (1 − D)^2 | 1 | 2L/((1 − D)^2·Ts) | 2L/Ts | −D/(1 − D) | −D/sqrt(K) | sqrt(K) |

DCM peak inductor currents: buck i_pk = (Vg − V)·D·Ts/L (Eq.5.23); boost i_pk = Vg·D·Ts/L (Eq.5.44); buck–boost i_pk = Vg·D·Ts/L (same first-subinterval slope; medium). Boost DCM approximation M ≈ 1/2 + D/sqrt(K) (Eq.5.54). Buck and boost DCM curves are asymptotic to the buck–boost line of slope 1/sqrt(K) and to M = 1 (Fig.5.20).

### 2.12 Figs.6.15–6.16 — Conversion ratios of the "short list" of converters (CCM, ideal)
OCR drops minus signs in the figure text; forms below are the standard ones consistent with the figure plots (conf medium for #6–#8).

| # | converter | M(D) = V/Vg | notes (text) |
|---|---|---|---|
| 1 | buck | D | pulsating input current |
| 2 | boost | 1/(1 − D) | pulsating output current |
| 3 | buck–boost | −D/(1 − D) | pulsating input and output current |
| 4 | noninverting buck–boost | D/(1 − D) | from buck–boost cascade |
| 5 | bridge (H-bridge) | 2D − 1 | bipolar output |
| 6 | Watkins–Johnson | (2D − 1)/D | bipolar, nonlinear M(D), ground-referenced load, two current-bidirectional switches |
| 7 | current-fed bridge | 1/(2D − 1) | inverse of #5, ac input → dc output |
| 8 | inverse of Watkins–Johnson | D/(2D − 1) | inverse of #6 |
| 2-L #1 | Ćuk | −D/(1 − D) | nonpulsating input and output currents, grounded MOSFET source |
| 2-L #2 | SEPIC | D/(1 − D) | grounded MOSFET source |
| 2-L #3 | inverse SEPIC | D/(1 − D) | |
| 2-L #4 | buck² | D^2 | one transistor + three diodes; large step-down |

### 2.13 Transformer-isolated converters — ratios, duty limits and ideal switch voltage stress (compiled from §6.3 text; "+ringing" = additional leakage-inductance overshoot the book says is observed in practice)
This 3rd-edition text does NOT contain the 2nd edition's switch-stress/utilization comparison table; the stresses below are the values stated in the §6.3 prose.

| converter | M(D) (CCM) | duty range | transistor peak voltage (ideal) | transformer excitation | typical power (text) | source |
|---|---|---|---|---|---|---|
| full-bridge isolated buck (1:n:n CT secondary) | n·D | 0 ≤ D < 1 | Vg (clamped by antiparallel diodes) | bipolar, at fs/2 | ≥ ≈750 W | Eq.(6.28) p.184–185 |
| half-bridge isolated buck | 0.5·n·D | 0 ≤ D < 1 | Vg (clamped) | bipolar, at fs/2, ±0.5·Vg | lower than full bridge; transistor current 2× | Eq.(6.29) p.186 |
| single-transistor forward (n1:n2:n3) | (n3/n1)·D | D ≤ 1/(1 + n2/n1) (0.5 for n1 = n2) | Vg·(1 + n1/n2) (2Vg for n1 = n2) + ringing | unipolar, reset while off (LM in DCM) | below bridge levels | Eq.(6.34)–(6.37) p.190–191 |
| two-transistor forward (1:n) | n·D | D < 0.5 | Vg (clamped by D1, D2) | unipolar | similar to half-bridge | p.191–192 |
| push-pull isolated buck (1:n) | n·D | 0 ≤ D < 1 | not stated in this text | bipolar, at fs/2 | low-Vg applications | Eq.(6.38) p.192 |
| flyback (1:n) | n·D/(1 − D) | 0 ≤ D < 1 | Vg + V/n + ringing | unipolar dc magnetizing current (energy storage) | 50–100 W; HV supplies | Eq.(6.44) p.197; p.198 |
| full-bridge isolated boost (1:n) | n/(1 − D) | 0 ≤ D < 1 | V/n = Vg/(1 − D) + ringing | bipolar | HV supplies, PFC rectifiers | Eq.(6.49) p.200–201 |
| push-pull isolated boost | n/(1 − D) | 0 ≤ D < 1 | 2V/n + ringing | bipolar | — | p.201 |
| isolated SEPIC (1:n) | n·D/(1 − D) | 0 ≤ D < 1 | Vg/(1 − D) + ringing | LM stores energy (like flyback) + transformer action | several hundred W | Eq.(6.50) p.201 |
| isolated Ćuk (1:n) | n·D/(1 − D) | 0 ≤ D < 1 | Vg/(1 − D) + ringing | no dc (series capacitors), full B–H loop | several hundred W | p.202 |
### 2.14 Table 7.1 — Canonical model parameters, ideal CCM converters (p.251)
Canonical model: e(s)·d̂ voltage source and j(s)·d̂ current source at the input, ideal 1:M(D) transformer, effective low-pass filter Le–C loaded by R. Gvg = M·He(s); Gvd = e(s)·M·He(s).

| converter | M(D) | Le | e(s) | j(s) |
|---|---|---|---|---|
| buck | D | L | V/D^2 | V/R |
| boost | 1/D' | L/D'^2 | V·(1 − s·L/(D'^2·R)) | V/(D'^2·R) |
| buck–boost | −D/D' | L/D'^2 | −(V/D^2)·(1 − s·D·L/(D'^2·R)) | −V/(D'^2·R) |

PWM modulator (§7.3): d̂ = v̂c/VM (VM = sawtooth peak-to-peak).

### 2.15 Table 8.2 — Salient features of the small-signal CCM transfer functions (p.315)
Gvd(s) = Gd0·(1 − s/ωz)/(1 + s/(Q·ω0) + (s/ω0)^2); Gvg(s) = Gg0/(1 + s/(Q·ω0) + (s/ω0)^2).

| converter | Gg0 | Gd0 | ω0 | Q | ωz (RHP) |
|---|---|---|---|---|---|
| buck | D | V/D | 1/sqrt(L·C) | R·sqrt(C/L) | ∞ (none) |
| boost | 1/D' | V/D' | D'/sqrt(L·C) | D'·R·sqrt(C/L) | D'^2·R/L |
| buck–boost | −D/D' | V/(D·D') | D'/sqrt(L·C) | D'·R·sqrt(C/L) | D'^2·R/(D·L) |

Worked example (§8.2.1, Eq.8.145–8.146): buck–boost D = 0.6, R = 10 Ω, Vg = 30 V, L = 160 μH, C = 160 μF → Gg0 = 1.5 (3.5 dB), abs(Gd0) = 187.5 V (45.5 dBV), f0 = 400 Hz, Q = 4 (12 dB), fz = 2.65 kHz; phase-asymptote breaks 10^(∓1/2Q)·f0 = 300 Hz / 533 Hz.

### 2.16 Bode-plot approximation anchors (§8.1)

| item | value | source |
|---|---|---|
| single pole deviation from asymptote | −3 dB at f0; −1 dB at f0/2 and 2f0 | Eq.(8.24), Fig.8.7 |
| single pole phase asymptote | breaks f0/10 and 10f0, −45°/decade, 5.7° error at breaks (alternative exact-slope breaks f0/4.81, 4.81f0) | Eq.(8.27)–(8.28) |
| quadratic pole magnitude at f0 | exactly Q (Q_dB above/below asymptote) | Eq.(8.65) |
| quadratic pole phase asymptote | breaks 10^(−1/2Q)·f0 and 10^(1/2Q)·f0; slope −180·Q °/decade | Eq.(8.69) |
| real vs complex poles | real for Q ≤ 0.5 | §8.1.6 |
| low-Q approximation accuracy | within 10% for Q ≤ 0.3 | Key pt 6 p.336 |
| high-Q (inverse-sum) accuracy | within 10% for Q1·Q2 > 5 | Key pt 7 p.336 |
| dB anchors (Table 8.1) | 1/2 → −6 dB; 1 → 0 dB; 2 → 6 dB; 5 → 14 dB; 10 → 20 dB; 1000 → 60 dB | Table 8.1 p.280 |
### 2.17 Magnetic material properties quoted in Ch.10 (p.412, p.424–425)

| material | saturation flux density Bsat | core loss / notes | typical use (text) |
|---|---|---|---|
| iron laminations, silicon steel | 1–2 T (p.412); 1.5–2 T (p.424) | high core loss (low resistivity → eddy loss); laminated / thin ribbon | filter inductors, low-frequency transformers |
| other ferrous alloys (Mo, Co) | somewhat lower than Si steel | somewhat lower loss | — |
| powdered iron, molypermalloy (MPP) powder | 0.5–1 T (p.412); 0.6–0.8 T (p.425) | much lower loss than laminations; distributed gap → low permeability | transformers at several kHz; filter inductors at ≈100 kHz |
| amorphous alloys | 0.6–1.5 T | low hysteresis loss; eddy loss between ferrous alloys and ferrite | — |
| MnZn ferrite | 0.25–0.5 T | very high resistivity → low eddy loss; Steinmetz β ≈ 2.6–2.8 | inductors/transformers 10 kHz – 1 MHz |
| NiZn ferrite | — | — | above MnZn frequencies |
| relative permeability μr of core materials | 10^3 – 10^5 | — | — |

### 2.18 Units for magnetic quantities — Table 10.1 (p.413)

| quantity | MKS | unrationalized CGS | conversion |
|---|---|---|---|
| core material equation | B = μ0·μr·H | B = μr·H | — |
| B | Tesla | Gauss | 1 T = 10^4 G; 1 T = 1 Wb/m^2 |
| H | Ampere/meter | Oersted | 1 A/m = 4π·10^-3 Oe |
| Φ | Weber | Maxwell | 1 Wb = 10^8 Mx |
| μ0 | 4π·10^-7 H/m | — | — |

### 2.19 Copper conductor data (Ch.10)

| item | value | source |
|---|---|---|
| resistivity, soft-annealed copper, room temperature | 1.724·10^-6 Ω·cm | p.426 |
| resistivity at 100°C | 2.3·10^-6 Ω·cm | p.426 |
| skin depth, copper at 100°C | δ = 7.5/sqrt(f) cm (f in Hz) | Eq.(10.62) |
| d/δ = 1 anchors | AWG #40 at ≈500 kHz; AWG #22 at ≈10 kHz | Fig.10.23 p.428 |
| typical porosity η of round-wire layers spanning the bobbin | 0.8 | p.433 |
| rectangular PWM current THD | 48% (D = 0.5), 76% (D = 0.3), 191% (D = 0.1) | p.442 |

### 2.20 Proximity-loss functions (Dowell form, §10.4.4–10.4.5)

| function | expression | limits |
|---|---|---|
| G1(ϕ) | (sinh 2ϕ + sin 2ϕ)/(cosh 2ϕ − cos 2ϕ) | → 1 for large ϕ |
| G2(ϕ) | (sinh ϕ·cos ϕ + cosh ϕ·sin ϕ)/(cosh 2ϕ − cos 2ϕ) | → 0 for large ϕ |
| layer factor Q'(ϕ, m) | (2m^2 − 2m + 1)·G1 − 4m(m − 1)·G2 | → m^2 + (m − 1)^2 for large ϕ |
| layer loss | P = I^2·Rdc·ϕ·Q'(ϕ, m) | m = F(h)/(F(h) − F(0)) |
| M-layer winding FR | ϕ·[G1 + (2/3)(M^2 − 1)(G1 − 2·G2)] | large ϕ → (ϕ/3)(2M^2 + 1) |
| interleaved (m = 1) optimum | ϕ = π/2 (loss ≈ flat for ϕ ≥ 1) | p.438 |
### 2.21 Window fill factor Ku (§11.1.3, p.462)

| construction | typical Ku |
|---|---|
| simple low-voltage inductor (with bobbin) | 0.5 |
| off-line transformer | 0.25–0.3 |
| high-voltage transformer (several kV) | 0.05–0.2 |
| low-voltage foil transformer or inductor | 0.65 |
| round-wire packing factor alone | 0.7–0.55 (winding-technique dependent) |
| wire conductor/total area (insulation) | 0.95–0.65 (size/insulation dependent) |
| book design problems: transformer with inter-winding insulation | 0.35 (inductors 0.5) (Problem 12.1) |

### 2.22 Magnetics design procedures — formulas in the book's mixed units (Ac, WA in cm^2; MLT, lm in cm; ρ in Ω·cm; B in T; lg in m)

| step | Kg method (filter inductor, §11.2) | Kg method (coupled inductor / flyback, §11.3.3) | Kgfe method (transformer, §12.2) | Kgfe method (ac inductor, §12.4.2) |
|---|---|---|---|---|
| core size | Kg ≥ ρ·L^2·Imax^2·10^8/(Bmax^2·R·Ku) | Kg ≥ ρ·LM^2·Itot^2·IM,max^2·10^8/(Bmax^2·Pcu·Ku) | Kgfe ≥ ρ·λ1^2·Itot^2·Kfe^(2/β)·10^8/(4·Ku·Ptot^((β+2)/β)) | Kgfe ≥ ρ·λ^2·I^2·Kfe^(2/β)·10^8/(2·Ku·Ptot^((β+2)/β)) |
| flux density | Bmax specified | Bmax specified | ΔB = [10^8·(ρ·λ1^2·Itot^2/(2Ku))·(MLT/(WA·Ac^3·lm))/(β·Kfe)]^(1/(β+2)) | same with λ, I |
| turns | n = L·Imax·10^4/(Bmax·Ac) | n1 = LM·IM,max·10^4/(Bmax·Ac) | n1 = λ1·10^4/(2·ΔB·Ac) | n = λ·10^4/(2·ΔB·Ac) |
| gap | lg = μ0·Ac·n^2·10^-4/L | lg = μ0·LM·IM,max^2·10^4/(Bmax^2·Ac) | none | lg = μ0·Ac·n^2·10^-4/L |
| AL (mH/1000 turns) | 10·Bmax^2·Ac^2/(L·Imax^2) | — | — | 10^9·L/n^2 |
| wire | AW ≤ Ku·WA/n | Awj ≤ αj·Ku·WA/nj, αj = nj·Ij/(n1·Itot) | Awj ≤ αj·Ku·WA/nj | Aw ≤ Ku·WA/n |
| checks | R = ρ·n·MLT/AW | — | ΔB (+dc) < Bsat; LM = μ·n1^2·Ac/lm; iM,pk = λ1/(2LM) | Bmax = ΔB + L·Idc·10^4/(n·Ac) < Bsat; Pcu, Pfe |

Kg definition: Kg = Ac^2·WA/MLT (cm^5). Kgfe definition: WA·Ac^(2(β−1)/β)/(MLT·lm^(2/β))·[(β/2)^(−β/(β+2)) + (β/2)^(2/(β+2))]^(−(β+2)/β).

### 2.23 Core data quoted in Ch.11–12 worked examples (full tables are in Appendix B, outside this extraction range)

| core | Kg (cm^5) | Kgfe | Ac (cm^2) | WA (cm^2) | MLT (cm) | lm (cm) | source |
|---|---|---|---|---|---|---|---|
| PQ 20/16 | 22.4·10^-3 | — | 0.62 | 0.256 | 4.4 | — | p.475 |
| EE30 | 0.0857 | — | 1.09 | 0.476 | 6.6 | 5.77 | p.478 |
| 2213 pot | — | 0.0049 (β = 2.7); 0.0047 (β = 2.6) | 0.635 | 0.297 | 4.42 | 3.15 | p.494 (Eq.12.30 values) |
| EE40 | — | 0.0118 (β = 2.7); 0.0108 (β = 2.6) | 1.27 | 1.1 | 8.5 | 7.7 | p.497–498 (Eq.12.41 values) |
| EE50 | — | 0.0284 | — | 1.78 (window used in Eq.12.52) | — | — | p.498–499 |

Ferrite core-loss parameters quoted: Kfe = 24.7 W/(T^β·cm^3), β = 2.6 at 200 kHz (pot core example); Kfe = 7.6 W/(T^β·cm^3), β = 2.6 at 75 kHz (Magnetics Inc. P material); Kfe = 50 W/(T^β·cm^3), β = 2.6 (or 2.7) at 100 kHz (problems); ferrite Bsat ≈ 0.35 T (examples), ≈0.3 T at 120°C (Problem 12.1). Fig.11.16 anchor: ΔB = 0.041 T at 150 kHz → 0.04 W/cm^3.


## 3. Mechanizable checks

Input table convention (one row per converter/operating corner): `topology` ∈ {buck, boost, buckboost, flyback, forward, fullbridge, halfbridge, pushpull, sepic, cuk}, `Vin_min`, `Vin_max` (V), `Vout` (V, magnitude), `Iout_max`, `Iout_min` (A), `fsw` (Hz), `L` (H, output/magnetizing inductance referred as noted), `C` (F), `ESR` (Ω), `n` (secondary/primary turns ratio n2/n1 or book's n; forward: n1, n2 (reset), n3), `Ron`, `VD`, `RD`, `RL` (Ω / V), device ratings `V_Q,rated`, `V_D,rated`, `I_Q,rated`, magnetics `Ac`, `WA`, `MLT`, `lm` (cm), `Bsat` (T), `Ku`. Ts = 1/fsw, D' = 1 − D. Ripple quantities are PEAK (half of p-p), as in the book. Evaluate every check at all four (Vin_min/max × Iout_min/max) corners and report the worst case.

`CHECK-duty-range`: inputs (topology, Vin_min, Vin_max, Vout, n, VD) → D from the ideal CCM ratio: buck D = V/Vg; boost D = 1 − Vg/V; buck–boost/SEPIC/Ćuk D = V/(V + Vg); flyback D = V/(V + n·Vg); forward/bridge D = V/(n·Vg) (half-bridge 2V/(n·Vg)); optionally add VD to V → pass: 0 < D_min ≤ D_max < D_limit, where D_limit = 1/(1 + n2/n1) for the single-transistor forward (0.5 for n1 = n2), 0.5 for the two-transistor forward, controller max duty otherwise → margin = D_limit − D_max (and D_min − controller min duty) → rows ERICKSON-1007, 1016, 1020, 1089, 1095, 1098, 1099, 1101, 1102, 1103, 1105; tables 2.1, 2.12, 2.13.

`CHECK-inductor-ripple-ratio`: inputs (topology, Vin corners, Vout, L, fsw, Iout_max) → ΔiL (peak): buck (Vg − V)·D·Ts/(2L) (worst at Vin_max); boost Vg·D·Ts/(2L); buck–boost/flyback (primary) Vg·D·Ts/(2L); I_L,dc: buck Iout; boost Iout/D'; buck–boost Iout/D'; flyback magnetizing I_M = n·Vout/(D'·R) (= n·Iout/D') → r = ΔiL/I_L,dc(full load) → pass: 0.10 ≤ r ≤ 0.20 (book "typical" band — flag outside as review item, not hard fail) → margin = distance to band edges → rows ERICKSON-1012, 1013, 1014, 1017, 1103, 1184, 1185.

`CHECK-peak-current-stress`: inputs (I_L,dc, ΔiL, I_Q,rated, I_D,rated, Isat of inductor) → I_pk = I_L,dc + ΔiL (switch and diode see the inductor peak; flyback secondary peak = I_pk,primary/n) → pass: I_pk ≤ min(I_Q,rated, I_D,rated) × user derating AND I_pk < Isat (inductor/transformer) → margin = 1 − I_pk/limit → rows ERICKSON-1015, 1157, 1158, 1195.

`CHECK-output-ripple`: inputs (topology, ΔiL, Ts, C, ESR, V, D, R, Δv_spec) → capacitive peak ripple: two-pole output (buck, forward, bridge, Ćuk output) Δv_C = ΔiL·Ts/(8C); pulsating output (boost, buck–boost, flyback, SEPIC) Δv_C = V·D·Ts/(2·R·C); ESR contribution (derived, medium): buck Δv_ESR,pp = ESR·2·ΔiL, boost-type Δv_ESR,pp ≈ ESR·I_pk,diode → p-p ripple ≈ 2·Δv_C + Δv_ESR,pp (conservative sum) → pass: ripple_pp ≤ spec (book example: < 1% of V, "a few tens of mV" at 3.3 V) → margin = 1 − ripple/spec → rows ERICKSON-1008, 1018, 1022, 1138.

`CHECK-ccm-dcm-mode`: inputs (topology, L, fsw, Vout, Iout_min, Iout_max, D at each corner, intended_mode) → R = Vout/Iout (effective load), K = 2L/(R·Ts); Kcrit: buck 1 − D, boost D·(1 − D)^2, buck–boost/flyback (1 − D)^2 (flyback: use L referred to the winding whose current is examined; SEPIC/Ćuk not tabulated in this range) → pass: intended CCM → K > Kcrit at Iout_min (report the load current at which DCM begins: I_crit = Vout·Kcrit·Ts/(2L)); intended DCM → K ≤ 0.75·Kcrit at every corner → margin = K/Kcrit − 1 (CCM) or 0.75·Kcrit/K − 1 (DCM) → rows ERICKSON-1074…1078, 1084; table 2.11.

`CHECK-dcm-duty`: inputs (topology, Vg, V, K) when in DCM → required D from Table 5.2 inverted: buck D = M·sqrt(K/(1 − M)); boost D = sqrt(K·M·(M − 1)); buck–boost D = abs(M)·sqrt(K) → pass: D within controller range; also compute i_pk (buck (Vg − V)·D·Ts/L; boost/buck–boost Vg·D·Ts/L) against ratings → rows ERICKSON-1079…1081 (inversions derived, medium).

`CHECK-switch-voltage-stress`: inputs (topology, Vin_max, Vout, n (n1, n2, n3), ringing_margin, V_Q,rated) → ideal transistor off-state voltage: buck Vg; boost V; buck–boost/SEPIC/Ćuk Vg + V (= Vg/D'); flyback Vg + V/n; single-transistor forward Vg·(1 + n1/n2) (2Vg for n1 = n2); two-transistor forward, full-bridge, half-bridge Vg; full-bridge isolated boost V/n; push-pull boost 2V/n; forward with auxiliary reset at minimum Vr Vg/(1 − D); half-bridge inverter from ±Vg 2Vg → V_stress = V_ideal·(1 + ringing_margin) (book gives no number for leakage ringing; ringing_margin user-set or from simulation) → pass: V_stress ≤ V_Q,rated × derating → margin = 1 − V_stress/(V_Q,rated × derating) → rows ERICKSON-1042, 1093, 1095, 1098, 1100, 1101, 1103, 1104, 1105, 1106; table 2.13.

`CHECK-diode-reverse-voltage`: inputs (topology, Vin_max, Vout, turns) → buck freewheel diode Vg; boost diode V; buck–boost diode Vg + V; forward output rectifier D3 (n3/n1)·Vg,max (stated p.187), forward D2 during reset (n3/n2)·Vg (derived); flyback output diode V + n·Vg (derived from winding voltages, medium); centre-tapped bridge secondary diodes 2·n·Vg (derived) → pass ≤ V_D,rated × derating → rows ERICKSON-1039, 1099, 1103 (derived items medium).

`CHECK-conduction-loss`: inputs (I_L,dc, r = ΔiL/I_L,dc, D, Ron, VD, RD, RL; topology) → ripple factor k = 1 + r^2/3; buck: P_Q = D·I^2·k·Ron, P_D = D'·(VD·I + RD·I^2·k), P_L = I^2·k·RL; boost: same with I = I_L (input current), transistor duty D, diode duty D'; synchronous rectifier: P_SR = D'·I^2·k·Ron2 → P_cond = ΣP → report each term → rows ERICKSON-1033, 1036, 1037, 1038, 1043, 1165; table 2.2.

`CHECK-boost-gain-feasibility`: inputs (Vin_min, Vout, R = Vout/Iout_max, RL, Ron, VD, RD) → required M = Vout/Vin_min; model M(D) = (1/D')·(1 − D'·VD/Vg)/(1 + (RL + D·Ron + D'·RD)/(D'^2·R)); with RL only M_max = 0.5·sqrt(R/RL) at D' = sqrt(RL/R) (η = 50% there) → pass: required M ≤ max over D of M(D) with margin, and operating D well below the D of M_max (efficiency collapses near it) → margin = M_max/M_required − 1 → rows ERICKSON-1028…1031, 1034, 1035; table 2.3.

`CHECK-switching-loss`: inputs (Vg (or V for boost-type), I (switched current), t_on, t_off, Coss (or C0, V0 law), Cj, Qr, tr, L_stray, fsw, Qg, V_drive) → W_on + W_off = 0.5·Vg·I·(t_on + t_off); W_C = 0.5·(Cds + Cj)·Vg^2 (linear) or (2/3)·Cds(VDS)·VDS^2 (∝ 1/sqrt(v) law); W_D = Vg·(Qr + I·tr) (buck) / V·(Qr + I·tr) (boost); W_L = 0.5·L_stray·I^2; gate-drive loss Qg·V_drive per cycle (charge/discharge through driver resistance; capacitive-type loss per §4.6.1, quantified here as Qg·V_drive — derived, medium) → P_sw = (ΣW)·fsw → rows ERICKSON-1046, 1052, 1053, 1059, 1060, 1061, 1063; table 2.10.

`CHECK-efficiency-and-fcrit`: inputs (Pout, P_cond, P_fixed, W_tot, fsw, η_spec, P_loss,max from cooling) → η = Pout/(Pout + P_cond + P_fixed + W_tot·fsw); Q = η/(1 − η); f_crit = (P_cond + P_fixed)/W_tot → pass: η ≥ η_spec at every corner including light load, total loss ≤ cooling capability, and fsw ≤ f_crit (warn when fsw > f_crit: efficiency falls rapidly with fsw) → margin = η − η_spec; f_crit/fsw − 1 → rows ERICKSON-1001, 1002, 1052, 1063, 1085.

`CHECK-lc-corner-vs-fsw`: inputs (L, C, fsw, [Le = L/D'^2 for boost/buck–boost]) → f0 = 1/(2π·sqrt(Le·C)) → pass: f0 << fsw (book gives no factor; ratio threshold user-configurable) and report Q = R·sqrt(C/Le) at light load (high Q at light load) → rows ERICKSON-1005, 1119, 1125, 1134.

`CHECK-forward-reset`: inputs (n1, n2, n3, Vin range, Vout, D_max) → D_max ≤ 1/(1 + n2/n1); reset duty D2 = (n2/n1)·D; D3 = 1 − D·(1 + n2/n1) ≥ 0; V_Q = Vg·(1 + n1/n2) → pass: D3 > 0 with margin at Vin_min (max duty) and V_Q within rating at Vin_max → margin = min(D3, 1 − V_Q/V_rated) → rows ERICKSON-1099, 1100, 1106, 1107.

`CHECK-transformer-flux`: inputs (λ1 = volt-seconds of positive portion, e.g. Vg·D·Ts; n1; Ac (cm^2); dc flux B_dc; Bsat(T_hot)) → ΔB = λ1·10^4/(2·n1·Ac); B_max = B_dc + ΔB (forward/flyback have dc bias; bridge/push-pull bipolar B_dc = 0 ideally) → pass: B_max ≤ 0.75·Bsat(T_hot) → margin = 1 − B_max/(0.75·Bsat) → rows ERICKSON-1160, 1187, 1190, 1196.

`CHECK-inductor-saturation`: inputs (L, I_pk, n, Ac, Bsat, [or Isat from datasheet]) → B_max = L·I_pk·10^4/(n·Ac) (from n·Φ = L·i) → pass: B_max ≤ 0.75·Bsat(T_hot) and I_pk < Isat → margin as above → rows ERICKSON-1158, 1176, 1195, 1196.

`CHECK-Kg-core-size`: inputs (ρ, L, Imax, Bmax, R (or Pcu/Irms^2), Ku, core Ac, WA, MLT) → Kg_req = ρ·L^2·Imax^2·10^8/(Bmax^2·R·Ku); Kg_core = Ac^2·WA/MLT → pass: Kg_core ≥ Kg_req → margin = Kg_core/Kg_req − 1; then n, lg, AW per Eq.(11.17)–(11.20) and window fit n·AW ≤ Ku·WA → rows ERICKSON-1176…1180, 1183.

`CHECK-Kgfe-core-size`: inputs (ρ, λ1, Itot (Σ (nj/n1)·Ij rms), Ku, Ptot_allowed, Kfe, β, core Ac, WA, MLT, lm) → Kgfe_req = ρ·λ1^2·Itot^2·Kfe^(2/β)·10^8/(4·Ku·Ptot^((β+2)/β)) (ac inductor: 2·Ku and I instead of Itot); Kgfe_core per Eq.(12.16) → pass: Kgfe_core ≥ Kgfe_req; then compute ΔBopt, n1, and after rounding turns recompute Pfe = Kfe·ΔB^β·Ac·lm, Pcu (Eq.12.7) and require Pfe + Pcu ≤ Ptot_allowed → margin = 1 − (Pfe + Pcu)/Ptot → rows ERICKSON-1187…1194.

`CHECK-winding-ac-resistance`: inputs (f (fundamental), conductor d or foil h, porosity η (default 0.8 round wire), layers M per winding, interleaving (m per layer), D (for PWM harmonics), T (for ρ)) → δ = 7.5/sqrt(f) cm (100°C); ϕ = sqrt(η)·sqrt(π/4)·d/δ (foil: h/δ); FR = ϕ·[G1(ϕ) + (2/3)(M^2 − 1)(G1(ϕ) − 2·G2(ϕ))]; harmonics: ϕj = sqrt(j)·ϕ1, Ij = sqrt(2)·Ipk·sin(jπD)/(jπ), exclude dc → P_cu = I0^2·Rdc + Σ Ij^2·Rdc·ϕj·Q'(ϕj, m) → pass: P_cu within copper-loss budget; flag ϕ > 1 with M ≥ 2 non-interleaved, or flyback/SEPIC interleaving assumed effective → rows ERICKSON-1166…1173; table 2.20.

`CHECK-loop-stability`: inputs (loop gain T(jω) from averaged model/sim at every corner, fsw, topology RHP-zero fz, spec_overshoot) → fc (abs(T) = 1), φm = 180° + ∠T(fc), count crossovers; Q = sqrt(cos φm)/sin φm; overshoot = exp(−π/sqrt(4Q^2 − 1)) (Q > 0.5) → pass: single crossover and T has no RHP poles (else run Nyquist), φm > 0; φm ≥ 76° if no overshoot allowed (Q ≤ 0.5) or ≥ 52° for Q ≤ 1 (≈16% overshoot); fc < ≈0.1·fsw; fc well below fz (RHP) for boost/buck–boost/flyback; abs(T(2·f_line)) ≥ 20 dB for rectified-input converters → margin = φm − φm,req; 0.1·fsw/fc − 1 → rows ERICKSON-1116, 1131, 1142…1147.

`CHECK-closed-loop-disturbance`: inputs (Gvg(s), Zout(s), T(s), v̂g amplitude at f_ripple, load step I0, Vout tolerance) → |v̂| = |Gvg/(1 + T)|·v̂g at f_ripple; closed-loop Zout,cl = Zout/(1 + T); load-step peak ≈ I0·R0·Q (R0, Q of the closed-loop Zout resonance; ≤ I0·R0) → pass: ripple and step deviation within tolerance → rows ERICKSON-1139, 1140, 1142, 1146, 1151.

`CHECK-ringing-loss`: inputs (measured/simulated ring frequency f_r, first-cycle peak ac current I_pk and voltage V_pk, fsw) → L_par = V_pk/(2π·f_r·I_pk); C_par = I_pk/(2π·f_r·V_pk); E = 0.5·L_par·I_pk^2 (= 0.5·C_par·V_pk^2); P_ring = E·fsw → pass: P_ring included in loss budget; ring decays before end of Ts is itself an indicator of switching loss → rows ERICKSON-1061, 1062 (formula derived from Eq.4.41 and Problem 4.14; medium).

`CHECK-gate-drive`: inputs (V_drive, I_pk,driver, Cgd, dv/dt of switch node, Vth of the off FET, Cboot, Qg, UVLO) → Rthev = V_drive/I_pk,driver; induced vgs ≈ Cgd·(dv/dt)·Rthev (first-order) → pass: vgs < Vth with margin; bootstrap voltage stays above UVLO over the maximum high-side on-time (Cboot droop ≈ Qg/Cboot, derived); dead time > 0 at both edges → rows ERICKSON-1055, 1069…1072 (droop estimate derived, medium).


## 4. Verification procedures & plots

| # | property demonstrated | method | x-axis / y-axis | sweep / corners | what "good" looks like / pass criterion | notes & source |
|---|---|---|---|---|---|---|
| V1 | Steady-state operating point and ripple | switching (transient) ngspice simulation run to periodic steady state | time (several Ts at the end of the run) / iL(t), vC(t), switch-node v(t) | Vin_min, Vin_max × Iout_min, Iout_max | cycle-to-cycle equality iL(nTs) = iL((n+1)Ts); average vL ≈ 0 and average iC ≈ 0 (volt-second / charge balance); measured ΔiL and Δv match CHECK-inductor-ripple-ratio / CHECK-output-ripple | ERICKSON-1010–1012, 1022; §2.2 Fig.2.10–2.11 |
| V2 | Start-up transient (inductor/cap stress) | switching or averaged transient | time / iL, v | nominal and max load, Vin_max | peak iL during start-up below Isat and device rating; no output overshoot beyond spec (a 3.3 V rail must not overshoot toward 5–6 V) | Fig.2.11 p.22; §9.4.4 p.375 |
| V3 | Conversion ratio with losses | dc sweep of duty cycle in averaged or switching model with RL, Ron, VD, RD, Qr/tr | D (0–1) / V/Vg and η | RL/R and other loss ratios | curve follows Eq.(3.34)/(4.33); required M reached well below the D of the M(D) maximum; η high at the operating D | Figs.3.9, 3.15, 4.45, 4.46; ERICKSON-1028, 1034, 1054 |
| V4 | Efficiency vs load | averaged model with conduction + switching loss terms, or measured | Pout (or load current) / η | Vin_min, Vin_nom, Vin_max | meets η spec at every load; expect η → 0 at light load when switching loss is fixed (constant fs) — if light-load η matters use reduced-fs / burst schemes | ERICKSON-1052, 1085; Fig.4.39 p.94 |
| V5 | Efficiency vs switching frequency | loss model Ploss = Pcond + Pfixed + Wtot·fsw | fsw (log, e.g. 10 kHz–1 MHz) / η at full load | device options | operating fsw at or below f_crit = (Pcond + Pfixed)/Wtot; knee visible where switching loss equals other losses | Fig.4.77 p.127; ERICKSON-1063 |
| V6 | CCM/DCM mode map | computation of K = 2L/(R·Ts) vs Kcrit(D) | D / K and Kcrit(D) curves; overlay operating points for all corners | Iout_min…Iout_max, Vin range | all intended-CCM points above Kcrit; intended-DCM points at K ≤ 0.75·Kcrit | Figs.5.5, 5.6, 5.13, 5.14; ERICKSON-1075–1078, 1084 |
| V7 | DCM conversion family | averaged/switching sim or Table 5.2 | D / M(D, K) for several K | K = 0.01…1 (buck), 0.01…4/27 (boost) | simulated V matches Table 5.2; controller duty range covers the DCM operating points | Figs.5.11, 5.19, 5.20 |
| V8 | Hard-switching transition energy | switching sim with device models (Coss, Qrr, stray L) — zoomed transition | time (ns) / vDS, iD, p(t) = vDS·iD | turn-on and turn-off, max current, Vin_max | integrate p(t) to get W_on, W_off; compare with 0.5·Vg·I·t and capacitive / recovery terms; ringing that has not decayed by end of Ts indicates additional loss | Figs.4.25, 4.31, 4.34, 4.69, 4.76; ERICKSON-1046–1062 |
| V9 | Half-bridge gate-drive integrity | switching sim / measurement of vgs of the OFF device during the opposite device's turn-on | time / vgs(off FET), vs(t), cHS/cLS logic | max dv/dt (Vin_max), both current directions | vgs stays below Vth for the whole transition; dead time present at both edges; no shoot-through current spike from Vg; bootstrap capacitor voltage above UVLO at max duty | Figs.4.55–4.58; ERICKSON-1069–1072 |
| V10 | Small-signal plant | ac analysis of averaged (state-space or averaged-switch) model | frequency (log, up to ≈ fs/3) / magnitude (dB, normalized: dBV, dBΩ) and phase of Gvd, Gvg, Zout, Zin | all Vin/load corners (Le = L/D'^2 and Q move with operating point) | Gd0, f0, Q, fz match Table 8.2 within model tolerance; RHP zero present for boost-type; do not trust averaged results above ≈ fs/3 | Table 8.2; ERICKSON-1109, 1118, 1129; Figs.8.35, 8.36 |
| V11 | Loop gain & stability | ac analysis of T(s) = H·Gc·Gvd/VM (or loop broken at an ideal injection point in sim) | frequency / abs(T) (dB) and ∠T (deg); annotate fc and φm | all corners, component tolerances | single crossover; φm ≥ 76° (no overshoot) or ≥ 52° (Q ≈ 1) per spec; fc ≤ ≈0.1·fs; abs(T) ≥ 20 dB at 100/120 Hz where line ripple matters; if multiple crossovers, Nyquist plot shows no encirclement of −1 | ERICKSON-1143–1147; Figs.9.9, 9.25, 9.41 |
| V12 | Closed-loop disturbance rejection | ac analysis | frequency / abs(Gvg/(1 + T)), abs(Zout/(1 + T)), abs(1/(1 + T)) overlaid on open-loop curves | corners | closed-loop curves equal open-loop / abs(T) below fc and coincide above fc; ripple at 2·f_line within spec; closed-loop Zout below the output-impedance spec over the specified band | Figs.9.7, 9.8, 9.42, 9.45; ERICKSON-1140 |
| V13 | Transient response | transient sim of averaged or switching model | time / v̂ for reference step and for load-current step I0 | Q from φm | overshoot matches exp(−π/sqrt(4Q^2 − 1)); load-step peak ≈ I0·R0·Q (≤ I0·R0); settling within spec | Figs.9.26, 9.27; ERICKSON-1145, 1146 |
| V14 | Loop-gain measurement on hardware | network (frequency-response) analyzer, voltage injection through isolation transformer / series resistor at a point with abs(Z1) << abs(Z2) (or current injection where abs(Z2) << abs(Z1)) | frequency / Tv magnitude & phase | nominal and worst-case corners | data valid only where abs(T) >> abs(Z1/Z2); dc operating point set by the circuit itself; for an oscillating unit add Rext (bypassed by Lext) at the injection point | ERICKSON-1135, 1136, 1152–1154; Figs.9.48–9.53 |
| V15 | Transformer volt-second balance / flux walking | switching sim over many (≥ tens of) cycles; measure magnetizing current | time / iM(t) (and its cycle average) | device-drop / timing mismatch cases, load steps | iM returns to the same value each period (forward: resets to zero within the off time); no ratcheting drift in bridge/push-pull (add blocking cap or current-programmed control otherwise) | ERICKSON-1091, 1096, 1099; Figs.6.21, 6.28 |
| V16 | Magnetic flux excursion | computation from λ1 and turns (or sim of B = ∫v dt/(n·Ac)) | time / B(t); or H / B locus (minor loop) | Vin_max, D_max, max load (dc bias) | B_max ≤ 0.75·Bsat(T_hot); ΔB near the Kgfe optimum for core-loss-limited parts | Figs.10.42, 10.46, 11.14, 11.15; ERICKSON-1160, 1187, 1196 |
| V17 | Core loss | vendor loss curves / Steinmetz fit | ΔB (T, log) / loss density (W/cm^3, log), family of fs | operating fs | Pfe = density × Ac·lm within budget; dc bias ignored for loss only if far from saturation | Figs.10.20, 11.16; ERICKSON-1164 |
| V18 | Winding ac resistance / proximity loss | Dowell-model computation (or FEA) per layer from the MMF diagram | ϕ = h/δ (log) / FR or P/Pdc,ϕ=1 for M = 0.5…15 layers; per-layer MMF diagram F(x) | fundamental + PWM harmonics (ϕj = sqrt(j)·ϕ1) | chosen ϕ near the minimum for the layer count (ϕ ≈ 1 or below for multilayer; π/2 for interleaved m = 1); interleave where currents are in phase | Figs.10.28, 10.31–10.35, 10.39; ERICKSON-1167–1173 |
| V19 | Averaged model validity | compare averaged-model and switching-model responses | frequency or time | modulation frequency sweep | agreement below ≈ fs/3; discrepancy above indicates sampling/averaging limits (PWM samples at fs, Nyquist fs/2) | ERICKSON-1109, 1116 |
| V20 | Low-impedance measurement (output impedance, capacitor ESR) | network analyzer with injection isolation transformer and separate current probe | frequency / abs(Z) (dBΩ) | — | Z >> Zprobe‖Zrz or use isolated injection; otherwise readings floor at tens–hundreds of mΩ | ERICKSON-1136; Fig.8.63 |


## 5. Pitfalls, failure modes, review checklist

- [ ] Ripple symbols: Erickson's ΔiL and Δv are PEAK (half of peak-to-peak) values — do not mix with p-p conventions from datasheets/other rulebooks. (§2.2 p.21)
- [ ] Small-ripple approximation applied only to inductor currents and capacitor voltages, never to switch voltage/current or inductor voltage. (Key pt 3 p.37)
- [ ] Two-pole-filter outputs (buck, Ćuk) — output ripple computed from inductor ripple charge (ΔiL·Ts/8C), not from the small-ripple approximation (which predicts zero). (§2.5 p.35)
- [ ] Capacitor ESR ripple added to the capacitive ripple estimate. (§2.5 p.37)
- [ ] Device current ratings checked against I + ΔiL (peak), not average current. (§2.2 p.21)
- [ ] Boost / buck–boost not designed to run near D → 1: losses (RL, Ron) cap the achievable gain and efficiency collapses; limit max duty. (§3.2 p.48–49)
- [ ] Conduction-loss estimates use rms currents (ripple raises loss by factor 1 + (Δi/I)^2/3; 33% at Δi = I). (Table 3.1 p.60)
- [ ] Every switch realization checked for voltage-blocking and current polarity over ALL operating points (including bidirectional power flow). (§4.1)
- [ ] MOSFET body diode allowed to conduct only if rated for it (fast-recovery body diode); otherwise add series/antiparallel diodes; budget its reverse-recovery loss. (§4.1.2 p.72–73; §4.4.1 p.101)
- [ ] Standard-recovery (50/60 Hz) rectifiers not used at switching frequency; tr and Qr specified for converter diodes. (§4.3.2 p.88)
- [ ] Negative-tempco devices (diodes, BJTs, SCRs) not paralleled without matching/common heatsink/ballasting. (§4.3.2 p.89)
- [ ] Datasheet Ron (typically 25°C) corrected for operating temperature before loss calculations. (§4.4.1 p.103)
- [ ] Output capacitance (Coss, Cj) turn-on loss included above ≈100 V; nonlinear Cds uses (2/3)·Cds(V)·V^2 energy. (§4.6.1 p.123)
- [ ] Stray / leakage / package inductance energy and turn-off overshoot included for high-current or isolated designs. (§4.6.1 p.124)
- [ ] Ringing that has not decayed before the end of Ts treated as evidence of switching loss (and EMI). (§4.6.2 p.126)
- [ ] fsw not above the critical frequency where switching loss equals conduction + fixed loss. (§4.6.3 p.126)
- [ ] Half-bridge: dead time at both edges (no shoot-through even for a few ns); bootstrap refresh guaranteed (low-side must turn on periodically; watch max duty); Cboot voltage above UVLO. (§4.4.3 p.107–108)
- [ ] dv/dt-induced turn-on of the off FET checked (vgs < Vth during opposite device's turn-on); add turn-on gate resistor with bypass diode if needed. (§4.4.3 p.110–111)
- [ ] GaN gate: on-state gate current limited (gate is a diode); VGS within 3–5 V class; ≈4 V reverse-conduction drop in dead time budgeted. (§4.4.2 p.106–107)
- [ ] SiC MOSFET: body-diode drop 3–4 V — use synchronous conduction; junction temperature ≤ 175°C (oxide). (§4.4.2 p.105)
- [ ] IGBT fs kept in the ≈1–30 kHz class unless soft-switched (current tail). (§4.5.2 p.119)
- [ ] Light-load (minimum load / no load) operating point checked for DCM: gain becomes load-dependent, output impedance rises, regulation can be lost at no load, and dynamics change. (Ch.5 intro p.135)
- [ ] DCM-by-design converters keep K ≤ 0.75·Kcrit at every corner. (Problem 5.17 p.160)
- [ ] Forward converter maximum duty respects reset (D ≤ 1/(1 + n2/n1)) at minimum input voltage, and transistor rating covers Vg·(1 + n1/n2) plus leakage ringing at maximum input. (§6.3.2 p.190–191)
- [ ] Flyback transistor rating covers Vg + V/n plus leakage-inductance ringing; SEPIC/Ćuk isolated: Vg/D' plus ringing. (§6.3.4 p.198; §6.3.6 p.201–202)
- [ ] Bridge / push-pull transformers protected from flux walking (series blocking capacitor or current-programmed control); push-pull not run with plain duty-cycle control; half-bridge not used with current-programmed control. (§6.3.1 p.184–186; §6.3.3 p.193)
- [ ] Transformer saturation fixed by more turns or more Ac — NOT by adding an air gap. (§10.2.2 p.421)
- [ ] Auxiliary (unregulated) outputs of multi-output converters given wider tolerance; cross-regulation degraded by leakage. (§6.3 p.179, 181)
- [ ] Averaged models / averaged simulations not trusted above ≈ fs/3; loop crossover well below fs/2 (PWM sampling) and typically < 10% of fs. (§7.2.3 p.224; §7.3 p.244; §9.5.1 p.377)
- [ ] Boost-type (CCM boost, buck–boost, flyback) control loops account for the RHP zero D'^2·R/(D·L) (buck–boost) / D'^2·R/L (boost): wide-bandwidth single-loop voltage control is hard. (§8.2.3 p.316–317)
- [ ] Plant Q, f0 and RHP zero re-evaluated at every line/load corner (Le = L/D'^2, Q = D'·R·sqrt(C/L) grows at light load). (Table 8.2; §8.4 p.328)
- [ ] Phase margin evaluated at a single crossover; multiple crossovers (e.g. input-filter or LC resonance peaks above 0 dB) or RHP loop-gain poles require the Nyquist test. (§9.4.2 p.360–369)
- [ ] Phase margin sized for the overshoot spec (76° for no overshoot, 52° ≈ 16% overshoot), not just "positive". (§9.4.3–9.4.4 p.370–375)
- [ ] Compensator includes high-frequency poles below fs so switching ripple on vc does not corrupt the PWM. (§9.5.1 p.377; §7.3 p.245)
- [ ] Output-voltage accuracy set by precision divider H and reference; forward-path gains need not be tight. (§9.2.2 p.353)
- [ ] Loop-gain measurements taken by injection at a point with correct impedance ratio; data below abs(Z1/Z2) discarded. (§9.6.1 p.395)
- [ ] Small-impedance measurements use isolated injection; otherwise results floor at tens–hundreds of mΩ. (§8.5 p.335)
- [ ] Inductor Bmax (incl. dc bias + ripple) below Bsat at hot temperature with ≈25% margin; ferrite Bsat is only 0.25–0.5 T (≈0.3 T at 120°C). (§10.1.1 p.412; Problem 12.1 p.502)
- [ ] Copper loss evaluated at 100°C resistivity (2.3·10^-6 Ω·cm), not room temperature (1.724·10^-6 Ω·cm). (§10.3.2 p.426)
- [ ] Multi-layer windings: effective thickness ϕ checked (≈1 or less for non-interleaved multilayer); high-THD PWM currents push optimum ϕ well below 1; dc component excluded from proximity calculations. (§10.4.5–10.4.7 p.436–443)
- [ ] Interleaving not relied on to cut proximity loss in flyback/SEPIC transformers (out-of-phase winding currents). (§10.4.6 p.440; §10.5.5 p.449)
- [ ] Gapped-inductor turns/gap from Kg method treated as first pass: fringing raises L (gap slightly longer); turns round-off re-checked for ΔB and loss (EE40 example missed the 4 W budget after rounding). (§11.2 p.464; §12.3.2 p.498)
- [ ] Transformer loss optimum is where dPfe/dΔB = −dPcu/dΔB (Pcu ≈ (β/2)·Pfe), not Pfe = Pcu. (§12.1.5 p.488)
- [ ] Window fill factor realistic for insulation class (0.25–0.3 off-line, 0.05–0.2 kV-class). (§11.1.3 p.462)

## 6. Standards referenced

No standard document identifiers (IEC, UL, IEEE Std, CISPR, MIL-STD, etc.) are cited in the extracted range (Chs.1–12, §13.1–13.3; verified by search of lines 1–34310). Generic regulatory references only:

| standard id | edition / clause | what it governs (as stated) | page |
|---|---|---|---|
| (unnamed) regulatory-agency isolation requirements | — | isolation "usually required by regulatory agencies" for off-line converters connected to the ac utility | §6.3 p.178 |
| (unnamed) conducted-EMI regulations | — | input L–C filters "commonly used to meet regulations limiting conducted electromagnetic interference (EMI)" | Problem 2.10 p.41; Ch.17 (outside range) |
| American Wire Gauge (AWG) | table in Appendix B (outside this range) | wire bare areas used in Kg/Kgfe wire selection | §11.2 p.465 |

## 7. Process / lifecycle guidance

This is a design/analysis textbook, not a lifecycle text; the process content in range is limited to the design loop below.

| stage | activity | deliverable | exit criterion | source |
|---|---|---|---|---|
| 1 Specification | define specifications and design goals (Vin range, Vout tolerance, load range/steps, ripple, efficiency, line-ripple rejection, overshoot) | spec table | measurable limits for every item | Ch.8 intro p.277; §9.5 p.376–377 |
| 2 Topology | propose circuit; screen by M(D), duty range, device stresses, isolation, pulsating vs nonpulsating currents; spreadsheet trade study | topology choice with stress table | duty and stresses within device capabilities at all corners | Ch.6 intro p.163–164; §6.2–6.3 |
| 3 Modelling | steady-state dc model with losses (Ch.3), switching-loss terms (Ch.4), DCM check (Ch.5), small-signal averaged model (Ch.7) | dc/ac models | model predicts V, I, η and transfer functions at every corner | Chs.3–5, 7 |
| 4 Design-oriented analysis | choose L, C, magnetics (Kg / Kgfe first pass), compensator (PD/PI/PID) | element values, magnetics build sheets, compensator values | CHECK-* rows in §3 pass | Chs.8–9, 11–12 |
| 5 Model verification | build prototype; measure transfer functions and loop gain by injection; compare with model; refine model | measured Bode plots, efficiency data | model agrees with lab data at nominal operating point | Ch.8 intro p.277; §8.5, §9.6 |
| 6 Worst-case analysis | simulate over line/load/component tolerances and temperature (averaged and switching simulation) | worst-case report | all specs met under all conditions; adequate production yield | Ch.8 intro p.277; §9.5.4 p.392 |
| 7 Iteration | repeat 2–6 (e.g. re-optimize magnetics with ρeff = ρ·Pcu/Pdc once proximity loss is known) | final design | worst-case behaviour meets specs | Ch.8 intro p.277; §12.2.1 p.491–492 |


## 8. Coverage log

Source file: refs-text/Erickson_Maksimovic_Fundamentals_of_Power_Electronics_2020.txt (68,610 lines). Assigned range: lines 1–34300 (Chs.1–12 complete, Ch.13 §13.1–13.3 through printed p.525). Lines 34301–68610 (rest of Ch.13, Chs.14–23, appendices) are covered by the part-2 extraction.

Read in order with the Read tool (chunks of 66–700 lines; the front matter needed small chunks because the TOC lines are up to 3,300 characters long):

| lines | content | notes |
|---|---|---|
| 1–135 | title page, ISBN, preface, full TOC | TOC used to map chapters to line numbers |
| 135–684 | Ch.1 Introduction | |
| 685–2800 | Ch.2 Principles of steady-state analysis + problems | problems skimmed (spec values only) |
| 2800–4310 | Ch.3 Steady-state equivalent circuits, losses, efficiency + problems | |
| 4310–7847 | Ch.4 Switch realization (incl. Tables 4.1–4.6) + problems | |
| 7848–9671 | Ch.5 Discontinuous conduction mode + problems | Problems 5.17/5.18 contain design guidance → extracted |
| 9672–12788 | Ch.6 Converter circuits, transformer isolation + problems | Problems 6.8/6.9 reset guidance → extracted (medium) |
| 12789–17145 | Ch.7 AC equivalent circuit modeling + problems | state-space examples read, derivations not transcribed |
| 17146–22589 | Ch.8 Converter transfer functions §8.1–8.6 | rules ERICKSON-1121…1137 written |
| 22589–22960 | Ch.8 problems | skimmed; ESR note (Problem 8.22) extracted |
| 22961–26155 | Ch.9 Controller design §9.1–9.7 | rules ERICKSON-1138…1154 written |
| 26155–26521 | Ch.9 problems | skimmed (specs only) |
| 26522–29311 | Ch.10 Basic magnetics theory + problems | rules ERICKSON-1155…1175; Fig.10.20/10.31–10.35/10.39 are graphs (anchors only) |
| 29312–31120 | Ch.11 Inductor design (Kg method) + problems | rules ERICKSON-1176…1186 |
| 31121–32962 | Ch.12 Transformer design (Kgfe method) + problems | rules ERICKSON-1187…1197 |
| 32963–34310 | Ch.13 §13.1–13.3 (feedback theorem; op-amp PD example through p.525) | rules ERICKSON-1198…1199; example continues past the range boundary (line 34300) into the part-2 extraction |

Rule-id map (199 rules, ERICKSON-1001…1199, four-digit to avoid collision with the part-2 extraction): Ch.1–3 → 1001–1038; Ch.4 → 1039–1072; Ch.5 → 1073–1086; Ch.6 → 1087–1108; Ch.7 → 1109–1120; Ch.8 → 1121–1138; Ch.9 → 1139–1154; Ch.10 → 1155–1175; Ch.11 → 1176–1186; Ch.12 → 1187–1197; Ch.13 → 1198–1199.

Skipped / summarized (with reason):
- End-of-chapter problem sets: read, but not transcribed except where they state explicit design guidance or margins (Problems 2.10, 4.14, 5.17, 5.18, 6.8, 6.9, 8.22, 12.1, 12.4, 12.5 → cited rows); problem specification values are exercises, not rules.
- Long derivations summarized as results only: state-space matrices of §7.5 examples, Nyquist principle-of-argument development (§9.4.2), feedback-theorem derivation (§13.2.2), Lagrange-multiplier window allocation (§11.3.1), Dowell field solution (§10.4.4).
- Ch.1 application narratives (laptop, spacecraft, EV power systems) — no design numbers beyond those captured.

Extraction limitations:
- Figures are not in the text. Graph-based data (Figs. 3.9, 3.15, 4.39, 4.45, 4.46, 4.77, 5.11, 5.19, 8.24–8.25, 9.25–9.27, 10.20, 10.23, 10.31–10.35, 10.39, 11.16, 12.7) are represented only by captions, the numeric anchors stated in the prose, and the closed-form equations behind them.
- OCR flattening dropped primes (D'), minus signs and fraction bars in many equations (e.g., buck Kcrit printed as "D" for 1 − D; Watkins–Johnson family ratios). Every such formula was re-derived or numerically cross-checked against the book's worked numbers before transcription; reconstructed items are tagged conf = medium (e.g., ERICKSON-1054, 1127, 1168, 1186; Table 2.12 rows 6–8). The placement of the process constant k in Eq.(4.40) could not be recovered and is described qualitatively only.
- Book typos noted and not propagated: Fig.8.26 caption "within 10% for Q < 3" (Key pt 6 and F(0.3) = 0.9 confirm Q ≤ 0.3); "BVCBO" repeated for the zero-base-current breakdown (BVCEO intended) in §4.5.1; §4.4.2 sentence "At lower rated voltages, SiC MOSFETs exhibits lower specific resistance" (context implies higher) not used; Table 4.1 part number reproduced as printed ("SD453N2S20PC").
- The assignment asked for the switch-stress / switch-utilization comparison tables: this 3rd-edition text does not contain the 2nd edition's switch-stress table (Ch.6 intro mentions switch utilization only in words). Section 2.13 compiles the transistor stresses stated in the §6.3 prose; ERICKSON-1108 records the utilization definition (conf low).
- Appendix A (rms formulas) and Appendix B (core Kg/Kgfe tables, AWG table, EC-core Rth) fall outside this range (part 2); only the core data quoted inside Chs.11–12 examples are reproduced (table 2.23).
- Derived checks and derived rule consequences (e.g., Pcu = (β/2)·Pfe at the Kgfe optimum, DCM duty inversions, diode reverse-voltage expressions, ringing-loss L/C estimates, input-filter inductor ripple dual of Eq.2.60) are marked medium in the rows/checks that use them.
