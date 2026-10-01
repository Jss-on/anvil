# Switching Power Supply Design (3rd ed.), Part 1 — Anvil rulebook

## 0. Citation

[1] A. I. Pressman, K. Billings, and T. Morey, *Switching Power Supply Design*, 3rd ed. New York, NY, USA: McGraw-Hill, 2009. ISBN 978-0-07-148272-1 (print, MHID 0-07-148272-5); eBook ISBN 978-0-07-159432-5 (MHID 0-07-159432-9).

Page citations `p.NNN` are the printed page numbers. "After Pressman", "Tip" and "Note" passages by K. Billings (K.B.) or T. Morey (T.M.) are cited to the same page.

**Chapters covered by this extraction (text lines 1-9000):**
- Front matter, contents, preface (orientation only).
- Part I, Topologies: Ch. 1 Basic Topologies (linear, buck, boost, inverting; pp. 3-43); Ch. 2 Push-Pull and Forward Converter Topologies (push-pull, single-ended, two-switch and interleaved forward; pp. 45-101); Ch. 3 Half- and Full-Bridge Converter Topologies (pp. 103-115); Ch. 4 Flyback Converter Topologies (DCM/CCM, MPP/gapped cores, interleaved, two-switch; pp. 117-160); Ch. 5 Current-Mode and Current-Fed Topologies (slope compensation, buck-fed bridges, turn-on snubbers, Weinberg; pp. 161-228); Ch. 6 Miscellaneous Topologies (SCR/ASCR resonant, Cuk, housekeeping supplies, Royer; pp. 229-281).
- Part II: Ch. 7 Transformers and Magnetic Design, §7.1-§7.5 (core materials, geometries, flux selection, core-power equations and charts, temperature rise, skin and proximity effects) and the §7.6 introduction with the area-product definition (pp. 285-339).

**Not read in this part (assigned to the part-2 extraction, text lines 9001-17886):** Ch. 7 from §7.6.1 on (area-product inductor/choke design, common-mode and rod-core filters, ferrite and powder-core choke design examples, swinging chokes); Ch. 8 Bipolar base drive; Ch. 9 MOSFET/IGBT gate drive (most gate-drive rules); Ch. 10 Magnetic-amplifier postregulators; Ch. 11 Snubbers and load-line shaping (RCD snubber design formulas); Ch. 12 Feedback-loop stabilization; Ch. 13 Resonant converters; Ch. 14 Typical waveforms; Ch. 15 Power-factor correction; Ch. 16 Electronic ballasts; Ch. 17 Low-input-voltage regulators; appendix, bibliography, index.

## 1. Design rules

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| PRESSMAN-1001 | power | NPN series-pass linear regulator needs a minimum input-output headroom, guaranteed at the bottom of the input ripple at minimum AC line | Vdc(min at ripple trough) - Vo >= 2.5 V | Vo, Vdc ripple trough, Vac(min) | NPN pass transistor with base drive via Rb from raw DC (1.5 V across Rb + Vbe) | calc | p.5 Fig 1.1b; p.6; p.10 Fig 1.3a | high |
| PRESSMAN-1002 | power | PNP series-pass (or NPN in negative return) linear regulator headroom is set only by the Ic-Vce knee | Vdc - Vo < 0.5 V achievable | Vo, Io | PNP pass element; drive from common negative line | review | p.9-10 §1.2.5, Fig 1.3b | high |
| PRESSMAN-1003 | thermal | Linear-regulator pass-element dissipation | Pd = (Vdc - Vo) * Io (W) | Vdc(max), Vo, Io | series-pass linear regulator; evaluate at Vdc(max) | calc | p.6 §1.2.3 | high |
| PRESSMAN-1004 | power | Linear regulator maximum DC input at high line when secondary is set for 2.5 V headroom at ripple trough at low line | Vdc(max) = [(1+0.01T)/(1-0.01T)] * (Vo + 2.5 + Vr/2); T = line tolerance +/-%; Vr = p-p ripple (V) | Vo, T(%), Vr | 60-Hz transformer + rectifier + capacitor input | calc | p.7-8 Eq 1.1 | high |
| PRESSMAN-1005 | power | Worst-case (high-line) linear-regulator efficiency | eff_max = Vo/Vdc(max) = [(1-0.01T)/(1+0.01T)] * Vo/(Vo + 2.5 + Vr/2) | Vo, T(%), Vr | NPN pass, 2.5 V headroom; plotted in Fig 1.2 for Vr = 8 V p-p | calc | p.8 Eq 1.2, Fig 1.2 | high |
| PRESSMAN-1006 | power | 60-Hz full-wave rectifier reservoir capacitor industry-standard sizing gives about 8 V p-p ripple | C_f ~ 1000 uF per ampere of DC load current -> Vr ~ 8 V p-p | Idc | 60-Hz full-wave capacitor-input rectifier | calc | p.8 | high |
| PRESSMAN-1007 | power | Linear regulators are unacceptable at low Vo with realistic line tolerance | 5 V out, +/-15% line with realistic ripple: eff only 32-35%; 10 V out, +/-10% line: eff < 50% | Vo, line tolerance | 60-Hz fed NPN linear regulator | calc | p.7-8, Fig 1.2 | high |
| PRESSMAN-1008 | components | Monolithic linear regulator current ceiling (at time of writing) | <= 3 A in single plastic package; <= 5 A in metal-case package | Io | integrated linear regulators | review | p.9 | high |
| PRESSMAN-1009 | power | Power-density benchmarks for topology/technology choice | linear 0.2-0.3 W/in^3; modern switching up to 20 W/in^3 (up to 50 W/in^3 claimed for switching elements); switching efficiency 70-95% | Po, volume | sanity check of volume budget | review | p.11 | high |
| PRESSMAN-1010 | power | Buck CCM output voltage relation | Vo = Vdc * Ton/T = Vdc * D | Vdc, D | CCM, ideal switch/diode | calc | p.13 §1.3.1.2; p.24 | high |
| PRESSMAN-1011 | control-loop | Voltage-mode PWM sawtooth amplitude typical value (sets modulator gain) | Vramp(p-p) ~ 3 V | - | comparator-type PWM | review | p.13 | high |
| PRESSMAN-1012 | power | Buck inductor current slopes with ~1 V diode drop | on: di/dt = (Vdc - Vo)/Lo; off: di/dt = (Vo + 1)/Lo (A/s) | Vdc, Vo, Lo | CCM; freewheel diode ~1 V (clamps V1 at ~ -0.8 V) | calc | p.13-14 | high |
| PRESSMAN-1013 | power | Buck ripple current is independent of load; mean of ramp = Io | dI = I2 - I1 constant vs load; ramp center = Io | Vdc, Vo, L, T | CCM | calc | p.15 | high |
| PRESSMAN-1014 | power | Buck conduction loss with ~1 V switch and diode drops | Pdc = 1 V * Io (Ton/T) + 1 V * Io (Toff/T) = 1 * Io (W) ; conduction efficiency = Vo/(Vo + 1) | Vo, Io | neglects AC losses; ~1 V forward drop for both Q1 and D1 | calc | p.16 Eq 1.3 | high |
| PRESSMAN-1015 | power | Switching (V-I overlap) loss, best case: linear simultaneous V and I transitions | per transition energy avg: Io*Vdc/6 over Ts; Pac = Vdc*Io*Ts/(3T) (both edges, Ts each) ; eff = Vo/(Vo + 1 + Vdc*Ts/(3T)) | Vdc, Io, Ts, T | idealized Fig 1.5a; Ton-transition = Toff-transition = Ts | calc | p.17-18 Eq 1.4 | high |
| PRESSMAN-1016 | power | Switching loss, worst case (inductive: V stays at Vdc until I reaches Io, I hangs at Io until V reaches Vdc) | P(Ton) = (Vdc*Io/2)(Tcr/T) + (Io*Vdc/2)(Tvf/T); P(Toff) = (Io*Vdc/2)(Tvr/T) + (Vdc*Io/2)(Tcf/T); all = Ts -> Pac = 2*Vdc*Io*Ts/T | Vdc, Io, Tcr, Tvf, Tvr, Tcf, T | Fig 1.5b; closer to reality for clamped inductive load | calc | p.19 Eq 1.5 | high |
| PRESSMAN-1017 | power | Buck total loss and efficiency, worst-case switching | Pt = 1*Io + 2*Vdc*Io*Ts/T ; eff = Vo/(Vo + 1 + 2*Vdc*Ts/T) | Vo, Vdc, Io, Ts, T | ~1 V drops; excludes diode recovery and core loss | calc | p.19-20 Eq 1.6, 1.7 | high |
| PRESSMAN-1018 | power | Worked example buck efficiencies (anchor for simulation cross-check) | 48 V -> 5 V, 50 kHz (T = 20 us), Ts = 0.3 us: conduction-only 83.3%; best-case switching 80.1%; worst-case 67.2%; equivalent linear 5/48 = 10.4% | - | example | calc | p.19-20 | high |
| PRESSMAN-1019 | power | Switching loss scales inversely with period; higher fsw shrinks L,C but increases loss and heat sink | Pac proportional to Ts/T = Ts*fsw | fsw, Ts | frequency selection trade-off | calc | p.20 §1.3.5 | high |
| PRESSMAN-1020 | components | Buck freewheeling diode must be ultrafast soft-recovery with minimum recovered charge | trr <= ~35 ns typical | trr, Qrr | hard-switched buck freewheel diode | inspect | p.20 | high |
| PRESSMAN-1021 | power | Designer's switching-frequency preference (after Pressman, K.B.) for lower cost and easier layout/magnetics | fsw < 100 kHz preferred (MHz designs exist but need more experience) | fsw | general guidance, technology-dependent | review | p.21 Note | low |
| PRESSMAN-1022 | power | Buck CCM/DCM boundary (critical load current): inductor runs dry when mean current equals half the p-p ripple | Io_crit = (I2 - I1)/2 = dI/2 | dI | fixed-frequency buck | calc | p.21 | high |
| PRESSMAN-1023 | power | Buck DCM output voltage (duty becomes load dependent) | Vo = V1 * 2D / (D + sqrt(D^2 + 8L/(R*T))) | V1(=Vdc), D, L, R (load ohms), T | DCM only; Vo = V1*D no longer valid | calc | p.24 Tip | high |
| PRESSMAN-1024 | control-loop | Buck in DCM has finite output impedance, duty changes with load, transient response degrades; loop must accommodate transfer-function change at critical current | - | Io range vs Io_crit | buck crossing CCM/DCM | sim | p.22-24 | medium |
| PRESSMAN-1025 | emc | Buck DCM ring at switch node (Lo with node capacitance) should be damped with a small RC snubber across the freewheel diode for RFI | RC snubber across D1 | - | DCM operation | inspect | p.24 Tip, Fig 1.7b | high |
| PRESSMAN-1026 | magnetics | Buck output choke sized for CCM down to 10% of nominal load (dI = 0.2*Ion) | L = (Vdc - Vo)*Ton/dI = 5*(Vdcn - Vo)*Vo*T/(Vdcn*Ion) (H) | Vdcn (nominal), Vo, T, Ion | min load 0.1*Ion (industry-standard 90% dynamic load range) | calc | p.26 Eq 1.8 | high |
| PRESSMAN-1027 | magnetics | Buck choke must not significantly saturate at nominal current plus half ripple | Isat >= 1.1 * Ion (for dI = 0.2 Ion) | Ion, dI | choke per Eq 1.8 | measure | p.26-27 | high |
| PRESSMAN-1028 | magnetics | Halving the Eq 1.8 inductance moves DCM onset from 1/10 to 1/5 of nominal current, trading slight load-regulation loss for faster transient response | L = 0.5*L(Eq1.8) -> Io_crit = 0.2*Ion | L, Ion | buck | calc | p.27 | high |
| PRESSMAN-1029 | magnetics | DC-biased power inductor must be designed as a choke: gapped ferrite or distributed-gap powder (iron, MPP) core | - | - | any inductor carrying DC | inspect | p.26-27 §1.3.6.3 | high |
| PRESSMAN-1030 | decoupling | Output-capacitor ESL can be neglected for ripple estimation below the capacitor's transition frequency | ESL negligible below ~500 kHz (typical; design dependent) | fsw | electrolytic output capacitors | review | p.27 Note | high |
| PRESSMAN-1031 | power | ESR-dominated ripple rule: at mid frequencies output ripple ~ inductor p-p ripple current times ESR | Vripple(p-p) ~ dI * Ro (ESR) | dI, ESR | electrolytic output cap at fsw; worst case assumes ESR and C components in phase | calc | p.28 | high |
| PRESSMAN-1032 | components | Aluminium electrolytic ESR*C product is roughly constant across voltage ratings and values | Ro*Co = 50 to 80 x 10^-6 ohm*F (s); use ~65 x 10^-6 typical (50 x 10^-6 used in example) | Co | older (non low-ESR) aluminium electrolytics; use datasheet ESR for low-ESR types | calc | p.28; p.30 Eq 1.10 | high |
| PRESSMAN-1033 | power | Required output-capacitor ESR for a p-p ripple target | Ro = Vor/(I2 - I1) = Vor/(0.2*Ion) (ohm) | Vor (p-p ripple spec), dI | buck with Eq 1.8 choke | calc | p.29-30 Eq 1.9 | high |
| PRESSMAN-1034 | power | Output capacitance from ESR*C constant | Co = 65e-6/Ro = 65e-6 * 0.2*Ion/Vor (F) | Ion, Vor | aluminium electrolytic, ESR-dominated | calc | p.30 Eq 1.10 | high |
| PRESSMAN-1035 | power | ESR (not C) dominates ripple when the ESR time constant exceeds half the on-time and half the off-time (Kantak) | Ro*Co > Ton/2 and Ro*Co > Toff/2 | ESR, C, Ton, Toff | general PWM converters | calc | p.30 ref 1 (Kantak 1987) | high |
| PRESSMAN-1036 | power | Capacitive ripple component (author's method): triangle current averages dI/4 over T/2 for each polarity | Vcr(per half) = (dI/4)*(T/2)/Co; total p-p ~ 2x that = dI*T/(4*Co) | dI, T, Co | conservative (exact triangle integral gives dI*T/(8Co)) | calc | p.29 | medium |
| PRESSMAN-1037 | power | Buck output-filter design example anchor | 25 kHz (T = 40 us), 20 V -> 5 V, Ion = 5 A, 50 mV p-p, CCM to 0.5 A: L = 150 uH, dI = 1 A, ESR = 0.05 ohm, Co = 1000 uF (RoCo = 50e-6), capacitive ripple 10 mV vs ESR ripple 50 mV | - | example | calc | p.28-29 | high |
| PRESSMAN-1038 | power | Isolated semi-regulated auxiliary output from a winding on the buck choke (peak rectified during freewheel) | Vo2 = (N2/N1)*(Vo + 0.4) - 0.4 (V) with Schottky D1, D2 ; regulation ~2-3% | N2/N1, Vo | D1 must remain conducting: main output power >> ancillary power; requires minimum load on main output | calc | p.30-31 §1.3.8, Fig 1.9 | high |
| PRESSMAN-1039 | power | Auxiliary-winding hold capacitor C2 must hold up over the maximum Q1 on time (D2 is reverse biased while Q1 is on) | C2 >= Iaux*Ton(max)/dV_allowed | Iaux, Ton(max), dV | Fig 1.9 aux output | calc | p.31 | medium |
| PRESSMAN-1040 | power | Boost inductor peak current and stored energy | Ip = Vdc*Ton/L1 (A); E = 0.5*L1*Ip^2 (J) | Vdc, Ton, L1 | boost; DCM or from zero current | calc | p.31, p.33 Eq 1.11 | high |
| PRESSMAN-1041 | power | Boost DCM power: energy from L plus direct supply contribution during reset | Pt = 0.5*L1*Ip^2/T + Vdc*(Ip/2)*(Tr/T) = Vdc^2*Ton*(Ton + Tr)/(2*T*L1) (W) | Vdc, Ton, Tr, L1, T | DCM boost, 100% efficiency | calc | p.34 Eq 1.12-1.15 | high |
| PRESSMAN-1042 | power | Boost DCM output voltage | Vo = Vdc*sqrt(k*Ro*Ton/(2*L1)), k = (Ton + Tr)/T < 1 | Vdc, Ro (load ohms), Ton, L1, k | DCM boost | calc | p.34 Eq 1.16 | high |
| PRESSMAN-1043 | control-loop | CCM boost (and any boost-type action incl. CCM flyback) has a right-half-plane zero; loop must be rolled off well below the RHP-zero frequency | f_crossover << f_RHPZ | L, D, Rload | continuous-mode boost-derived converters | sim | p.35-37 | high |
| PRESSMAN-1044 | power | Boost DCM guarantee: provide 20% dead-time margin at Vdc(min), Ro(min) | Ton + Tr + Tdt = T with Tdt = 0.2T -> Ton + Tr = 0.8T (k = 0.8) | T | DCM boost design | calc | p.38 Eq 1.17, Fig 1.13 | high |
| PRESSMAN-1045 | magnetics | Inductor volt-second balance (core reset) per cycle | Vdc*Ton = (Vo - Vdc)*Tr (boost) | Vdc, Vo, Ton, Tr | any choke: core must return to B1 each cycle or it walks up the loop and saturates | calc | p.37-38 Eq 1.18, Fig 1.12 | high |
| PRESSMAN-1046 | power | Boost DCM maximum on-time with 20% dead time | Ton(max) = 0.8*T*(Vo - Vdc(min))/Vo | Vo, Vdc(min), T | then L1 from Eq 1.16 with k = 0.8 at Ro(min) | calc | p.38-39 Eq 1.19 | high |
| PRESSMAN-1047 | protection | Boost must limit maximum on time or peak current, else overload/low line eats the dead time and forces CCM; alternatively inhibit turn-on until inductor current reaches zero | Ton <= Ton(max) or Ipk <= Ip(design) | Ton, Ipk | DCM boost | inspect | p.39 + Tip | high |
| PRESSMAN-1048 | power | Boost typical applications/power range | 5 V logic -> 12/15 V op-amp rails; 12/28 V battery sagging to ~9/22 V restored; 50-200 W | - | non-isolated boost | review | p.40 | high |
| PRESSMAN-1049 | power | Polarity-inverting (buck-boost) DCM power: no direct source contribution during reset | Pt = 0.5*Lo*Ip^2/T; Ip = Vdc*Ton/Lo | Lo, Vdc, Ton, T | DCM inverting regulator | calc | p.42 Eq 1.20-1.21 | high |
| PRESSMAN-1050 | power | Inverting regulator DCM output voltage | Vo = Vdc*Ton*sqrt(Ro/(2*T*Lo)) | Vdc, Ton, Ro, T, Lo | DCM | calc | p.42 Eq 1.22 | high |
| PRESSMAN-1051 | power | Inverting regulator DCM design with 20% dead time | Ton + Tr = 0.8T; Vdc*Ton = Vo*Tr; Ton(max) = 0.8*Vo*T/(Vdc(min) + Vo) | Vo, Vdc(min), T | then Lo from Eq 1.22 at Ro(min) | calc | p.42-43 Eq 1.23-1.25 | high |
| PRESSMAN-1052 | power | Push-pull secondary pulse amplitude and duty (two pulses per period) | Vsec_pk = (Vdc - 1)*(Ns/Np) - Vd ; rectified duty = 2*Ton/T ; Vce(sat) ~ 1 V; Vd = 1 V fast-recovery, 0.5 V Schottky | Vdc, Ns/Np, Vd, Ton, T | push-pull, CCM output chokes | calc | p.46-47 | high |
| PRESSMAN-1053 | power | Push-pull master output voltage (Schottky rectifiers) | Vm = [(Vdc - 1)*(Nm/Np) - 0.5] * (2*Ton/T) | Vdc, Nm/Np, Ton, T | master output with feedback, CCM | calc | p.47 Eq 2.1 | high |
| PRESSMAN-1054 | power | Push-pull slave output voltage (fast-recovery rectifiers) | Vs = [(Vdc - 1)*(Ns/Np) - 1] * (2*Ton/T) | Vdc, Ns/Np, Ton, T | slaves share master Ton; line-regulated, only partly load-regulated | calc | p.48 Eq 2.2-2.3 | high |
| PRESSMAN-1055 | power | Slave (cross) regulation band for master/slave multi-output converters | slave Vout within +/-5 to +/-8% for load changes if no output choke (esp. master) goes discontinuous; ~5% above master critical current | load ranges | push-pull and forward master/slave; coupled output inductors give much better cross regulation | measure | p.48-50, p.80 | high |
| PRESSMAN-1056 | power | Slave output setting granularity: one secondary turn changes Vout by the volts-per-turn times duty | dV_per_turn = [(Vdc - 1)/Np]*(2*Ton/T) (push-pull) | Vdc, Np, Ton | integral turns only; if exact value needed, design higher and post-regulate (linear/buck) | calc | p.49 §2.2.3 | medium |
| PRESSMAN-1057 | power | Slaves typically only need to be within about 2 V of target (op-amps, motors); otherwise post-regulate | abs(Vs - Vs_target) <= ~2 V else add linear/buck post-regulator | Vs | semi-regulated slave outputs | review | p.49 | high |
| PRESSMAN-1058 | power | Master and slave output chokes must stay continuous down to each output's specified minimum current | size each output L from Eq 1.8 (or 2.20/2.47) at its own Imin | Imin per output | master/slave converters: below master critical current Ton collapses and slaves drop | calc | p.49-50 §2.2.4 | high |
| PRESSMAN-1059 | magnetics | Ferrite power-transformer flux limits vs frequency (Ferroxcube 3C8-type) | stay on linear part: Bpk <= +/-2000 G up to ~25-30 kHz; 100-300 kHz: +/-1200 or +/-800 G (core loss) | fsw, material | ferrite, bipolar-flux (push-pull/bridge) transformers | calc | p.50-51, Fig 2.3 | high |
| PRESSMAN-1060 | magnetics | Push-pull flux-walking risk: volt-second mismatch walks the core into saturation; 0.01% imbalance walks B1->B2 in ~10,000 cycles | sum(V*t) half-cycle A == half-cycle B each period | Vce(sat), storage-time spread | bipolar storage times 0.3-6 us with large spread, rising with temperature | review | p.51-53 | high |
| PRESSMAN-1061 | magnetics | Push-pull magnetizing current slope and peak | dI/dt = (Vdc - 1)/Lpm ; Ipm = (Vdc - 1)*Ton/Lpm | Vdc, Ton, Lpm | Lpm = primary inductance with all secondaries open | calc | p.53 Eq 2.4-2.5 | high |
| PRESSMAN-1062 | magnetics | Peak magnetizing current limit | Ipm <= 0.10 * primary reflected load current | Ipm, Ipft | push-pull; forward: >10% adds significant copper loss | calc | p.55; p.88 | high |
| PRESSMAN-1063 | test | Flux-imbalance acceptance from transformer center-tap current probe | reject if any upward concavity in current ramps; reject if alternate peak currents differ by > 20% even with linear ramps | center-tap current waveform | push-pull at all line/load/temperature corners | measure | p.55 Fig 2.4 | high |
| PRESSMAN-1064 | test | Flux-imbalance margin test: insert ~1 V silicon diode in series with one half-primary | if one diode makes a ramp go concave -> too close to failure; use two diodes to gauge margin; swap sides | - | push-pull prototype | measure | p.55-56 Fig 2.4d | high |
| PRESSMAN-1065 | magnetics | Magnetizing force from winding current (CGS) | H = 0.4*pi*Np*Im/lm (Oe) ; lm in cm, Im in A | Np, Im, lm | any core | calc | p.56 Eq 2.6 | high |
| PRESSMAN-1066 | magnetics | Push-pull core gap to tolerate DC imbalance | gap 2-4 mils (0.002-0.004 in) total; shims in centre + outer legs give total gap = 2x shim; in production grind centre leg to 2x shim thickness | - | trade: lower Lm -> larger critical current | inspect | p.56-57 §2.2.8.1 | high |
| PRESSMAN-1067 | magnetics | Added series primary resistance to damp flux imbalance | R_added < 0.25 ohm per side (set empirically from centre-tap waveform) | - | push-pull; costs efficiency | measure | p.57 §2.2.8.2 | high |
| PRESSMAN-1068 | power | MOSFET push-pull is dependable at low power/low input voltage; current-mode control is the only complete fix for flux imbalance | voltage-mode MOSFET push-pull OK for Po < 100 W at low Vin (DC/DC); otherwise current-mode | Po, Vin | push-pull topology election | review | p.58 §2.2.8.4-5 | high |
| PRESSMAN-1069 | magnetics | Transformer design should start from a maximum permitted temperature rise | dT_rise(max) typically 30 C | - | nomogram/area-product design methods | review | p.59 After Pressman | high |
| PRESSMAN-1070 | power | Maximum on-time clamp for push-pull/forward (core reset + no cross-conduction with storage time) | Ton(max) <= 0.8*(T/2) at Vdc(min); total duty <= 0.8 (push-pull), <= 0.4 (single-ended forward) | T | enforced by clamp/dead time in PWM | inspect | p.60 §2.2.9.2; p.78 | high |
| PRESSMAN-1071 | magnetics | Primary turns from Faraday's law (CGS form) | Np = (Vdc(min) - 1)*(0.8*T/2)*1e8/(Ae*dB) ; Ae cm^2, dB gauss (peak-to-peak), T s | Vdc(min), T, Ae, dB | push-pull half primary; forward uses same form (Eq 2.40) | calc | p.61 Eq 2.7 | high |
| PRESSMAN-1072 | magnetics | Faraday's law in modified SI units (K.B.) | N = V*Ton/(Ae*dB) ; V volts, Ton microseconds, dB tesla, Ae mm^2 | V, Ton, Ae, dB | any transformer/inductor winding | calc | p.61 Tip | high |
| PRESSMAN-1073 | magnetics | Ferrite core loss scaling | Pcore proportional to Bpk^2.7 * f^1.6 (approx.) | Bpk, f | ferrite power materials | calc | p.61 | high |
| PRESSMAN-1074 | magnetics | Design flux swing must survive a 50% line step during error-amplifier delay: set dB = 3200 G (+/-1600 G) not 4000 G, even when core loss permits more | dB(steady) <= 3200 G so 1.5*dB from -1600 G peaks at +3200 G (tolerable at 100 C) | dB, transient factor | ferrite, bipolar-flux transformer, f <= ~50 kHz | calc | p.62-63 §2.2.9.4 | high |
| PRESSMAN-1075 | magnetics | Flux swing from applied volt-seconds | dB = (Vdc - 1)*Ton*1e8/(Np*Ae) (G) | Vdc, Ton, Np, Ae | check at Vdc(max) with Ton(max) for transient | calc | p.62 Eq 2.8 | high |
| PRESSMAN-1076 | magnetics | High-frequency flux derating for ferrite transformers | above 50 kHz losses force lower Bpk: 100-200 kHz -> 1200 or even 800 G peak | fsw | ferrite; check core temperature rise | calc | p.63 | high |
| PRESSMAN-1077 | power | Push-pull equivalent flat-topped primary current pulse | Ipft = 1.56*Po/Vdc(min) (A) | Po, Vdc(min) | 80% efficiency (achievable up to ~200 kHz), total duty 0.8 at Vdc(min) | calc | p.64 Eq 2.9 | high |
| PRESSMAN-1078 | current-carrying | RMS of flat-topped pulse | Irms = Ipk*sqrt(D) | Ipk, D | rectangular pulses | calc | p.64 Eq 2.10 | high |
| PRESSMAN-1079 | current-carrying | Push-pull half-primary RMS current | Irms = 0.632*Ipft = 0.986*Po/Vdc(min) | Po, Vdc(min) | D = 0.4 per half primary | calc | p.64 Eq 2.10-2.11 | high |
| PRESSMAN-1080 | current-carrying | Winding current density (wire sizing) | conservative 500 circular mils per rms A; 300 CM/A acceptable for few-turn windings; do not go below 300 CM/A (excess copper loss and temperature rise) | Irms | transformer/choke windings (low-frequency copper sizing, skin/proximity separate) | calc | p.64 | high |
| PRESSMAN-1081 | current-carrying | Push-pull half-primary copper area | CM = 493*Po/Vdc(min) (circular mils) | Po, Vdc(min) | 500 CM/A | calc | p.65 Eq 2.12 | high |
| PRESSMAN-1082 | current-carrying | Circular-mil conversion | area(in^2) = (pi/4)*1e-6 * area(CM) | CM | wire tables | calc | p.63 footnote | high |
| PRESSMAN-1083 | current-carrying | Push-pull half-secondary RMS and copper area (full-wave CT rectifier) | Is(rms) = 0.632*Idc ; CM = 500*0.632*Idc = 316*Idc | Idc | D = 0.4; ignores freewheel 'ledge' (each half ~Idc/2 for 20% dead time) — include ledge for copper-loss estimate | calc | p.65-67 Eq 2.13-2.14 (text prints 3.16Idc; 500x0.632 = 316) | high |
| PRESSMAN-1084 | derating | Push-pull transistor off-voltage stress including leakage spike | Vp = 1.3*(2*Vdc(max)) = 2.6*Vdc(max) | Vdc(max) | conservative: leakage spike adds up to 30%; add >=15% transient margin on top | calc | p.67 Eq 2.15 | high |
| PRESSMAN-1085 | magnetics | Leakage inductance limit for a good power transformer | Lleak <= 0.04 * Lmag | Lleak, Lmag | minimize with long centre-leg core and sandwiching secondaries between primary halves | measure | p.67 | high |
| PRESSMAN-1086 | test | Leakage inductance measurement | short-circuit all other windings; measure residual inductance of the winding | - | any transformer | measure | p.67 Tip | high |
| PRESSMAN-1087 | magnetics | Low-frequency transformer equivalent (Lm + primary/secondary leakage) validity | valid up to ~300-500 kHz; above that include inter/intra-winding capacitance | f | circuit modelling of transformers | sim | p.69 Fig 2.7c | high |
| PRESSMAN-1088 | power | Push-pull per-transistor turn-off overlap loss (turn-on loss negligible because leakage L slows current rise) | Pt(ac) = 2*Ipft*Vdc*Ts/T = 3.12*(Po/Vdc(min))*Vdc(max)*(Ts/T) | Po, Vdc(min), Vdc(max), Ts, T | voltage rises to 2Vdc while current held at Ipft; Tvr = Tcf = Ts | calc | p.69-70 Eq 2.16 | high |
| PRESSMAN-1089 | power | Push-pull per-transistor conduction loss (Baker-clamped bipolar, Von ~1 V) | Pdc = 0.4*Ipft*Von = 0.624*Po/Vdc(min) (Von = 1 V) ; Ptotal = Pt(ac) + Pdc | Po, Vdc(min), Von | duty 0.4 per transistor | calc | p.70 Eq 2.17-2.18 | high |
| PRESSMAN-1090 | power | Worked loss example: 150 W, 50 kHz push-pull, 48 V telecom (38-60 V), bipolar Ts = 0.3 us | Pdc = 2.46 W; Pac = 11.8 W (4.5x conduction); MOSFET Ts ~0.05 us -> switching loss negligible | - | example | calc | p.71 §2.2.12.3 | high |
| PRESSMAN-1091 | requirements | Telephone-industry DC bus range | nominal 48 V, minimum 38 V, maximum 60 V | - | telecom converters | review | p.71 | high |
| PRESSMAN-1092 | power | Push-pull practical output-power ceiling (bipolar era) | Po <~ 500 W | Po | limited by Ipft and 2.6Vdc stress; MOSFETs extend | review | p.71 §2.2.13 | medium |
| PRESSMAN-1093 | derating | Device voltage rating selection with margin above computed stress | 400 W telecom push-pull: Ipft = 16.4 A, Vp = 2.6*60 = 156 V -> choose >= 200 V device | Vp | example of margin practice | calc | p.72 | high |
| PRESSMAN-1094 | derating | Off-line input transient allowance when unspecified | assume stress >= 15% above maximum steady-state value (e.g. 484 V -> 557 V) | Vstress(max steady) | commercial off-line supplies | calc | p.72 | high |
| PRESSMAN-1095 | power | Push-pull (and single-ended forward) unsuited to off-line input because of 2.6*Vdc stress | 120 VAC +10%: Vdc = 1.41*1.1*120 = 186 V -> 2.6*186 = 484 V (557 V with 15% transient); MIL-STD-704 180 VAC 10-ms transient -> 660 V | Vac, tolerance | topology election for off-line | calc | p.72 §2.2.13 | high |
| PRESSMAN-1096 | magnetics | Push-pull (full-wave) output choke for CCM | Lo = 0.05*Vo*T/Idc(min) ; with Idc(min) = 0.1*Ion: Lo = 0.5*Vo*T/Ion (H) | Vo, T, Idc(min) or Ion | Ns chosen so V1 = 1.25*Vo at Vdc(min) (duty 0.8) | calc | p.73-74 Eq 2.19-2.20 | high |
| PRESSMAN-1097 | power | Output ripple (ESR-dominated) and capacitor sizing, push-pull/interleaved | Vr = Ro*dI ; Co = 80e-6*dI/Vr (F) | dI, Vr | aluminium electrolytic RoCo 50-80e-6 (upper value used) | calc | p.74-75 Eq 2.21-2.22 | high |
| PRESSMAN-1098 | power | Single-ended forward converter application window | Po < ~200 W; Vdc 60-200 V (below 60 V primary current too high; above ~250 V transistor stress too high); telecom (<60 V) limit 150-200 W | Po, Vdc | topology election | review | p.75; p.83 | high |
| PRESSMAN-1099 | power | Forward converter output voltage | Vom = [(Vdc - 1)*(Nm/Np) - Vd] * Ton/T ; design at Vdc(min) with Ton(max) = 0.8*T/2 | Vdc(min), Nm/Np, Vd, T | CCM, freewheel drop = rectifier drop = Vd | calc | p.78 Eq 2.24-2.25 | high |
| PRESSMAN-1100 | power | Forward slave outputs | Vs = [(Vdc - 1)*(Ns/Np) - Vd] * Ton/T | Vdc(min), Ns/Np, Vd | slaves regulated vs line, 5-8% vs load | calc | p.80 Eq 2.26-2.27 | high |
| PRESSMAN-1101 | magnetics | Forward converter core reset requires reset volt-seconds A2 = set volt-seconds A1 before next cycle | Vdc*Ton = (Np/Nr)*Vdc*Tr ; with Nr = Np and Ton(max) = 0.4T, Ton + Tr = 0.8T | Ton, Tr, Np/Nr | single-ended forward with reset winding and catch diode D1 | calc | p.77-78, Fig 2.10 | high |
| PRESSMAN-1102 | power | Forward converter equivalent flat-topped primary current | Ipft = 3.13*Po/Vdc(min) (twice push-pull) | Po, Vdc(min) | 80% eff, duty 0.4 at Vdc(min), Nr = Np | calc | p.82 Eq 2.28 | high |
| PRESSMAN-1103 | derating | Forward (Nr = Np) transistor off-voltage stress | Vms = 1.3*(2*Vdc(max)) = 2.6*Vdc(max) | Vdc(max) | includes 30% leakage spike allowance | calc | p.83 Eq 2.29 | high |
| PRESSMAN-1104 | power | Off-line single-ended forward, 120 VAC +/-10%, 200 W worked stresses | high line 1.1*120*1.41 - 2 = 184 V -> Vms = 478 V (550 V with 15% transient); low line 0.9*120*1.41 - 2 = 150 V -> Ipft = 3.13*200/150 = 4.17 A | - | example (text prints 3.13x22/150; 200 W intended) | calc | p.83-84 | high |
| PRESSMAN-1105 | power | Forward with unequal reset/power turns: maximum on-time | Ton(max) = 0.8*T/(1 + Nr/Np) | Nr/Np, T | Ton + Tr = 0.8T | calc | p.86 Eq 2.32 (text garbled; derived from Eq 2.30-2.31) | high |
| PRESSMAN-1106 | power | Forward peak primary current vs Nr/Np | Ipft = 1.56*(Po/Vdc(min))*(1 + Nr/Np) | Po, Vdc(min), Nr/Np | 80% efficiency | calc | p.86 Eq 2.33 | high |
| PRESSMAN-1107 | derating | Forward transistor off stress vs Nr/Np (excluding leakage spike) | Vms = Vdc(max)*(1 + Np/Nr) + leakage spike | Vdc(max), Np/Nr | trade peak current vs voltage (table T4) | calc | p.86 Eq 2.34 | high |
| PRESSMAN-1108 | magnetics | Forward converter core operates in first quadrant only; same core handles half the push-pull power, with half the push-pull core loss | P_forward(core) ~ 0.5 * P_pushpull(core) | - | core selection | review | p.86-88 §2.3.9.1 | high |
| PRESSMAN-1109 | magnetics | Ungapped ferrite remanence limits unipolar flux swing | Br ~ +/-1000 G -> ungapped forward dB(max) ~ 1000 G; ferrite coercive force ~0.2 Oe | material | 3C8-type ferrite | calc | p.88 Fig 2.3 | high |
| PRESSMAN-1110 | magnetics | Small gap in forward transformer core raises usable unipolar swing | gap 2-4 mils -> Br ~200 G -> usable dB ~1800 G | gap | cores for 200-500 W; costs lower Lm, higher Im | calc | p.88 §2.3.9.2 | high |
| PRESSMAN-1111 | magnetics | Magnetizing inductance from Faraday (CGS) | Lm = Np*Ae*dB*1e-8/dIm (H); Ae cm^2, dB G | Np, Ae, dB, dIm | any transformer | calc | p.89 Eq 2.35 | high |
| PRESSMAN-1112 | magnetics | Ampere's law across a gapped core, flux density | Hi*li + Ha*la = 0.4*pi*N*Im ; Bi = 0.4*pi*N*Im/(la + li/u) (G; lengths cm) | N, Im, la, li, u | fringing ignored | calc | p.89 Eq 2.36-2.37 | high |
| PRESSMAN-1113 | magnetics | Gapped-core inductance | L = 0.4*pi*N^2*Ae*1e-9/(la + li/u) (H); Ae cm^2, la, li cm | N, Ae, la, li, u | fringing ignored; if li/u << la, L set by gap | calc | p.89 Eq 2.38 | high |
| PRESSMAN-1114 | magnetics | Inductance reduction by adding a gap | L(gap)/L(no gap) = (li/u)/(la + li/u) ; example 783E608-3C8 (li = 9.7 cm, u = 2300) with 4-mil (0.0102 cm) gap -> 0.29 | li, u, la | - | calc | p.90 Eq 2.39 | high |
| PRESSMAN-1115 | magnetics | Forward transformer design flux density (unipolar, gapped, ~200 G remanence) | dB ~1600 G (0 -> 1600 G) at low frequency; primary turns Np = (Vdc(min) - 1)*(0.8T/2)*1e8/(Ae*dB) | Vdc(min), T, Ae | ferrite, core loss not limiting (<= 50 kHz); leaves transient margin | calc | p.90-91 Eq 2.40 | high |
| PRESSMAN-1116 | components | Rectifier selection by output voltage | 5 V high-current main: Schottky, Vf ~0.5 V; higher-voltage slaves: fast-recovery, Vf ~1.0 V | Vout, Vrrm | forward/push-pull secondaries | review | p.91 | high |
| PRESSMAN-1117 | current-carrying | Forward primary RMS current and copper area | Irms = 3.12*(Po/Vdc(min))*sqrt(0.4) = 1.97*Po/Vdc(min) ; CM = 985*Po/Vdc(min) | Po, Vdc(min) | 500 CM/A | calc | p.91-92 Eq 2.41-2.42 | high |
| PRESSMAN-1118 | current-carrying | Forward secondary RMS current and copper area | Irms = 0.632*Idc ; CM = 316*Idc | Idc | duty 0.4 | calc | p.92 Eq 2.43-2.44 | high |
| PRESSMAN-1119 | current-carrying | Forward reset-winding RMS current and copper area | Ip(mag) = Vdc*Ton/Lmg ; Irms = Ip*sqrt(0.4/3) = 0.365*Vdc*Ton/Lmg ; CM = 500*0.365*Vdc*Ton/Lmg (usually AWG 30 or finer) | Vdc, Ton, Lmg | Lmg gapped Lm (Eq 2.39) | calc | p.92-93 Eq 2.45 | high |
| PRESSMAN-1120 | magnetics | Inductance from catalogue AL (per 1000 turns) | Ln = AL*(n/1000)^2 | AL, n | ferrite catalogue AL (ungapped) | calc | p.92 | high |
| PRESSMAN-1121 | current-carrying | RMS of a repeating triangle | Irms = Ip/sqrt(3) (continuous); times sqrt(D) if gated at duty D | Ip, D | - | calc | p.92 | high |
| PRESSMAN-1122 | magnetics | Forward (single-transformer, half-wave) output choke for CCM | L1 = 0.3*Vo*T/Idc(min) ; with Idc(min) = 0.1*Ion: L1 = 3*Vo*T/Ion (H) | Vo, T, Idc(min) or Ion | Ton(max) = 0.4T at Vdc(min) | calc | p.93-94 Eq 2.46-2.47 | high |
| PRESSMAN-1123 | power | Forward output capacitor (ESR-dominated) | Co = 65e-6*dI/Vor (F) | dI, Vor | aluminium electrolytic RoCo ~65e-6 | calc | p.94 Eq 2.48 | high |
| PRESSMAN-1124 | derating | Double-ended (two-switch) forward converter clamps each switch to the bus with no leakage spike; leakage energy returned to Vdc | Vstress = Vdc(max) | Vdc(max) | diodes D1, D2 to rails | calc | p.94-96 Fig 2.13 | high |
| PRESSMAN-1125 | power | 220 VAC mains (~308 Vdc nominal) excludes the single-ended forward (and push-pull); use two-switch forward, half bridge or full bridge | Vdc(nom) ~308 V -> 2.6*Vdc too high | Vac | European 220 VAC input | review | p.96 | high |
| PRESSMAN-1126 | power | Two-switch forward core resets in a time equal to on-time; Ton(max) <= 0.8*T/2 gives 20% reset margin | Ton(max) = 0.4T at Vdc(min) | T | double-ended forward | calc | p.96 | high |
| PRESSMAN-1127 | power | Two-switch forward practical output power | Po = 400-500 W | Po | reduced voltage stress | review | p.97 §2.4.1.1 | high |
| PRESSMAN-1128 | requirements | Rectified DC range for 120 VAC +/-10% line with +/-15% transient allowance | Vdc(max) = 1.41*120*1.1*1.15 = 214 V ; Vdc(min) = 1.41*120/1.1/1.15 = 134 V | Vac, tol, transient | off-line bridge rectifier | calc | p.97 | high |
| PRESSMAN-1129 | power | Two-switch forward 400 W, 120 VAC example | Ipft = 3.13*400/134 = 9.6 A; with voltage doubler: stress 428 V, Ipft 4.8 A (400 V Vceo bipolar with -1 to -5 V turn-off bias OK) | - | example | calc | p.97 | high |
| PRESSMAN-1130 | magnetics | Two-switch forward primary turns and flux | Np via Eq 2.40 with (Vdc - 2); dB = 1600 G up to 50 kHz; 100-300 kHz: 1400 to 800 G; smaller cores tolerate higher B (more surface per volume) | fsw, core size | ferrite | calc | p.97-98 | high |
| PRESSMAN-1131 | power | Interleaved forward: per-transistor peak current halves; EMI scales with peak current, not pulse count | Ipft = 3.13*Pot/(2*Vdc(min)) | Pot, Vdc(min) | two forward converters on alternate half cycles | calc | p.98 §2.5.1 | high |
| PRESSMAN-1132 | components | Freewheel diode reverse voltage at high Vout: single forward sees Vo/0.4, interleaved Vo/0.8 | Vr(FWD) = Vo/Dmax: 200 V out -> 500 V (single, D = 0.4) vs 250 V (interleaved, D = 0.8) | Vo, Dmax | Vout > ~200 V favours interleaved (faster, lower-voltage diode) | calc | p.100 | high |
| PRESSMAN-1133 | magnetics | Interleaved forward design: each transformer for half power; secondary turns at duty 0.8; choke per push-pull Eq 2.20, capacitor per Eq 2.22 | Np per Eq 2.40; CM per Eq 2.42 at Pot/2; CM secondary per Eq 2.44 | Pot | - | calc | p.100-101 | high |
| PRESSMAN-1134 | power | Bridge topologies stress each off switch to Vdc (not 2Vdc) and clamp leakage spikes to the bus, returning leakage energy; use them for >= 220 VAC input and often for 120 VAC | Vstress = Vdc(max) | Vdc(max) | half and full bridge with clamp diodes across switches | calc | p.103; p.109 §3.2.5 | high |
| PRESSMAN-1135 | power | Universal-input doubler/full-wave front end (link S1) | 220 VAC full-wave: 1.41*220 - 2 = 308 V; 120 VAC doubler: 2*(1.41*120 - 1) = 336 V; range ~308-336 Vdc | Vac | half/full bridge off-line front end | calc | p.103-105 Fig 3.1 | high |
| PRESSMAN-1136 | derating | Half-bridge switch rating on universal doubler input | Vstress = 336 V nominal + 15% = 386 V | Vdc | 120/220 VAC link-selected | calc | p.105 | high |
| PRESSMAN-1137 | power | Series bulk capacitors in half bridge / doubler need equal bleeder resistors to equalize midpoint voltage | equal R across C1 and C2 | - | half bridge, voltage doubler | inspect | p.105 | high |
| PRESSMAN-1138 | protection | Automatic 120/220 V line sensing (relay in place of link S1) prevents damage from running on 220 V while linked for 120 V | - | - | universal-input doubler | review | p.105 After Pressman (T.M.) | high |
| PRESSMAN-1139 | protection | Bridge legs: maximum on-time clamped at 80% of half period to prevent shoot-through, under all fault/transient conditions | Ton(max) = 0.8*T/2 | T | half and full bridge | inspect | p.105-106; p.113 | high |
| PRESSMAN-1140 | magnetics | Half-bridge primary turns: Faraday with minimum primary voltage (Vdc/2 - 1); flux excursion is twice the peak (1st and 3rd quadrant) | Np = ((Vdc(min)/2) - 1)*(0.8T/2)*1e8/(Ae*dB), dB = 2*Bpk = 3200 G (<50 kHz), less at higher f | Vdc(min), T, Ae | ferrite | calc | p.106 §3.2.2.1 | high |
| PRESSMAN-1141 | power | Half-bridge equivalent flat-topped primary current | Ipft = 3.13*Po/Vdc(min) | Po, Vdc(min) | 80% efficiency, duty 0.8 at Vdc(min), primary voltage Vdc/2 | calc | p.106 Eq 3.1 | high |
| PRESSMAN-1142 | current-carrying | Half-bridge primary RMS current and copper area | Irms = Ipft*sqrt(0.8) = 2.79*Po/Vdc(min) ; CM = 1395*Po/Vdc(min) | Po, Vdc(min) | 500 CM/A | calc | p.106-107 Eq 3.2-3.3 | high |
| PRESSMAN-1143 | power | Half-bridge secondaries and filters designed exactly as push-pull, with (Vdc/2 - 1) in place of (Vdc - 1) | Vout per Eq 2.1-2.3; Is(rms) = 0.632 Idc; L per Eq 2.20; C per Eq 2.22 | - | full-wave secondaries | calc | p.107 §3.2.2.4-3.2.3 | high |
| PRESSMAN-1144 | magnetics | Half/full-bridge series DC-blocking capacitor sized for primary voltage droop | Cb = Ipft*(0.8*T/2)/dV (F); droop dV <= 10% of primary pulse amplitude; non-polarized | Ipft, T, dV | half bridge (mandatory), full bridge (recommended; imbalance less likely) | calc | p.107-108 Eq 3.4, Fig 3.2; p.115 | high |
| PRESSMAN-1145 | magnetics | Blocking-capacitor worked example | 150 W, 100 kHz, 320 V nom, 15% low line 272 V (+/-136 V primary), dV = 14 V: Ipft = 1.73 A -> Cb = 1.73*0.8*5e-6/14 = 0.49 uF | - | example | calc | p.108 | high |
| PRESSMAN-1146 | power | Half bridge vs two-switch forward: half bridge has full-wave secondary (2x ripple frequency -> smaller L, C) and half the primary turns (fewer parasitics, slightly lower proximity loss); the forward's higher peak secondary voltage (half the duty) matters only above ~200 V out | CM: forward primary 985*Po/Vdc vs half bridge 1395*Po/Vdc | - | topology election at 220 VAC | review | p.109-110 §3.2.6 | high |
| PRESSMAN-1147 | magnetics | Above ~50 kHz the peak-to-peak flux swing is core-loss limited to typically < 200 mT, obtainable by both single- and double-ended topologies | dB(p-p) < 0.2 T for f > ~50 kHz | fsw | ferrite (K.B.) | calc | p.110 After Pressman | high |
| PRESSMAN-1148 | power | Half-bridge practical output-power limit (120 VAC doubler) | ~400-500 W; worked: Vdc(max) = 1.41*120*2*1.1*1.15 = 428 V, Vdc(min) = 1.41*120*2/1.1/1.15 = 268 V, 500 W -> Ipft = 5.84 A; pushable to 1000 W (12 A) with difficulty; above 500 W use full bridge | Po | bipolar needs -1 to -5 V turn-off bias for Vcev rating | calc | p.111 §3.2.7 | high |
| PRESSMAN-1149 | power | Full bridge gives twice half-bridge power with same switch ratings (primary sees +/-Vdc); usable off-line up to 440 VAC line | P_full ~ 2*P_half for equal Ipk, Vstress | - | primary turns 2x, current 1/2 of half bridge at equal power | review | p.111-112 §3.3.1 | high |
| PRESSMAN-1150 | power | Full-bridge output voltages (1 V per switch, 0.5 V Schottky master, 1 V slave diodes) | Vom = [(Vdc - 2)*(Nsm/Np) - 0.5]*(2*ton/T) ; Vo1 = [(Vdc - 2)*(Ns1/Np) - 1]*(2*ton/T) | Vdc(min), Ns/Np, ton = 0.8T/2 | full-wave secondaries | calc | p.113 Eq 3.5-3.6 | high |
| PRESSMAN-1151 | magnetics | Full-bridge primary turns | Np = (Vdc(min) - 2)*(0.8T/2)*1e8/(Ae*dB), dB = 3200 G (<= 50 kHz), reduced at higher f | Vdc(min), T, Ae | ferrite | calc | p.113-114 §3.3.2.1 | high |
| PRESSMAN-1152 | power | Full-bridge equivalent flat-topped primary current | Ipft = 1.56*Po/Vdc(min) | Po, Vdc(min) | 80% efficiency, duty 0.8 | calc | p.114 Eq 3.7 | high |
| PRESSMAN-1153 | current-carrying | Full-bridge primary RMS current and copper area | Irms = 1.40*Po/Vdc(min) ; CM = 700*Po/Vdc(min) | Po, Vdc(min) | 500 CM/A | calc | p.114 Eq 3.8-3.9 | high |
| PRESSMAN-1154 | magnetics | Flyback 'transformer' is a multi-winding choke: ampere-turns (not volts) are conserved between primary and secondary at the switching instant | Np*Ip = sum(Ns*Is) at turn-off; Vsec set by load (never open-circuit a flyback secondary) | Np, Ns, Ip | all flyback-derived converters | review | p.117-119 Foreword (K.B.) | high |
| PRESSMAN-1155 | magnetics | Flyback minimum primary turns (K.B. SI form) | Np = V*T/(dB*Ae) ; V = max primary DC voltage (V), T = max on period (us), dB = AC p-p flux swing (T), typically 0.2 T for ferrite, Ae = centre-pole area (mm^2) | V, T, dB, Ae | gapped ferrite flyback | calc | p.119-120 (K.B. key point 2) | high |
| PRESSMAN-1156 | magnetics | Flyback energy per cycle and gap requirement | E = 0.5*L*I^2 (J) is the max transferable energy per cycle (all of it only in DCM); gap chosen so core does not saturate for DC + AC magnetization, usually larger than minimum to meet power transfer | L, Ipk | gapped ferrite flyback; lower L -> higher I -> more stored energy | calc | p.120 key point 4 + Note | high |
| PRESSMAN-1157 | magnetics | Do not design a flyback for a fixed inductance; let L be the dependent variable of turns, gap and permeability | - | - | flyback/choke design practice (K.B.) | review | p.120 key point 5 | low |
| PRESSMAN-1158 | power | Flyback application ranges | ~5 W to ~150 W typical; high voltage <= 5000 V at < 15 W; up to 150 W if Vdc >= 160 V; many outputs (up to 10 isolated) at 50-150 W; Vdc from 5 V; typical 160 Vdc (115 VAC) | Po, Vout, Vdc | topology election | review | p.121; p.127 | high |
| PRESSMAN-1159 | power | Flyback slaves track the master better than forward-converter slaves (no output inductors) | - | - | multi-output supplies | review | p.123; p.127 | high |
| PRESSMAN-1160 | power | DCM flyback primary peak current and stored energy | Ip = (Vdc - 1)*Ton/Lp ; E = Lp*Ip^2/2 | Vdc, Ton, Lp | DCM | calc | p.123 Eq 4.1 | high |
| PRESSMAN-1161 | power | DCM flyback input power | P = 0.5*Lp*Ip^2/T = [(Vdc - 1)*Ton]^2/(2*T*Lp) ~ (Vdc*Ton)^2/(2*T*Lp) (W) | Vdc, Ton, T, Lp | DCM; loop holds Vdc*Ton constant | calc | p.124 Eq 4.2 | high |
| PRESSMAN-1162 | power | DCM flyback output voltage (80% efficiency) | Vo = Vdc*Ton*sqrt(Ro/(2.5*T*Lp)) | Vdc, Ton, Ro, T, Lp | DCM | calc | p.124 Eq 4.3 | high |
| PRESSMAN-1163 | power | Flyback secondary inductance and downslope | Ls = (Ns/Np)^2*Lp ; dIs/dt = (Vo + 1)/Ls | Lp, Ns/Np, Vo | 1 V rectifier drop | calc | p.124-125 | high |
| PRESSMAN-1164 | control-loop | Flyback entering CCM changes the transfer function (RHP zero); if the error amplifier bandwidth was not drastically reduced the loop oscillates | f_c << f_RHPZ for any operating point that can be CCM | Lp, load range, Vdc range | flyback crossing DCM/CCM | sim | p.122 Fig 4.2 caption; p.126-127; p.130-131 | high |
| PRESSMAN-1165 | power | DCM vs CCM flyback trade: DCM secondary peak current 2-3x CCM; larger turn-off output spike, RFI, RMS currents, capacitor ripple rating and primary peak; but no RHP zero, faster transient response, and no rectifier reverse-recovery (diodes off before next turn-on) | Is_pk(DCM) ~ 2-3 x Is_pk(CCM) | - | mode election | review | p.128-129 | high |
| PRESSMAN-1166 | derating | Flyback switch off-stress (single-ended) excluding leakage spike; choose turns ratio so a 0.3*Vdc leakage spike still leaves ~30% margin below the relevant rating (Vceo, Vcer or Vcev) | Vms = Vdc(max) + (Np/Nsm)*(Vo + 1) ; Vms + 0.3*Vdc(max) <= 0.7*Vrating | Vdc(max), Np/Nsm, Vo, Vrating | single-ended flyback | calc | p.130 Eq 4.4 | high |
| PRESSMAN-1167 | magnetics | Flyback volt-second balance (reset) | (Vdc - 1)*Ton = (Vo + 1)*(Np/Nsm)*Tr | Vdc, Ton, Vo, Np/Nsm, Tr | 1 V switch and diode drops | calc | p.130 Eq 4.5 | high |
| PRESSMAN-1168 | power | DCM flyback 20% dead-time guarantee | Ton + Tr = 0.8*T at Vdc(min), Ro(min) | T | DCM flyback | calc | p.130-131 Eq 4.6 | high |
| PRESSMAN-1169 | power | DCM flyback maximum on-time | Ton(max) = (Vo + 1)*(Np/Nsm)*0.8*T / [(Vdc(min) - 1) + (Vo + 1)*(Np/Nsm)] | Vo, Np/Nsm, T, Vdc(min) | DCM flyback | calc | p.131 Eq 4.7 | high |
| PRESSMAN-1170 | magnetics | DCM flyback primary inductance for max power at min line | Lp = (Ro/(2.5*T))*(Vdc(min)*Ton/Vo)^2 = (Vdc(min)*Ton)^2/(2.5*T*Po) (H) | Vdc(min), Ton(max), T, Po(max) | 80% efficiency | calc | p.131 Eq 4.8 | high |
| PRESSMAN-1171 | power | Flyback primary peak current | Ip = Vdc(min)*Ton/Lp | Vdc(min), Ton, Lp | DCM | calc | p.131 Eq 4.9 | high |
| PRESSMAN-1172 | derating | MOSFET flyback switch current rating selection | Id(rating) ~ 5-10 x Ip (to get acceptably low Rds(on) drop and loss) | Ip | MOSFET switch | review | p.131 | high |
| PRESSMAN-1173 | current-carrying | DCM flyback primary RMS current and copper area | Irms(pri) = (Ip/sqrt(3))*sqrt(Ton/T) ; CM = 500*Irms | Ip, Ton, T | triangle pulse | calc | p.132 Eq 4.10-4.11 | high |
| PRESSMAN-1174 | current-carrying | DCM flyback secondary RMS current and copper area | Irms(sec) = (Ip*(Np/Ns)/sqrt(3))*sqrt(Tr/T) ; CM = 500*Irms ; Tr = 0.8T - Ton | Ip, Np/Ns, Tr, T | triangle pulse | calc | p.132 Eq 4.12-4.13 | high |
| PRESSMAN-1175 | power | DCM flyback worked example (anchor) | 5 V/50 W (10 A, min 1 A), 38-60 Vdc, 50 kHz, 200 V switch, Vms = 120 V (50 V margin with 25%/30 V spike): Np/Nsm = 10; Ton = 9.9 us; Lp = 56.6 uH; Ip = 6.6 A; Irms(pri) = 2.7 A (1350 CM -> AWG 19, 1290 CM); Tr = 6.1 us; Irms(sec) = 21 A (10,500 CM -> AWG 10: use foil or paralleled strands) | - | example | calc | p.132-134 §4.6 | high |
| PRESSMAN-1176 | magnetics | Flyback leakage inductance and strand size matter: use multiple parallel strands (limit skin/proximity), minimize leakage for energy transfer, lower switch spike, less snubbing, lower RFI | - | - | flyback transformer construction | inspect | p.134 After Pressman | high |
| PRESSMAN-1177 | power | Flyback output capacitor from droop during switch on-time | Co = Io*(T - toff)/dV ; worked: 10 A * 13.9 us / 0.05 V = 2800 uF | Io, T, toff (reset), dV | capacitor alone supplies load during on-time | calc | p.134 | high |
| PRESSMAN-1178 | power | Flyback turn-off output spike from secondary peak current through ESR | Vspike = Ip*(Np/Ns)*Resr ; width < ~0.5 us (time constant Resr*Co); worked: 66 A * 0.023 ohm = 1.5 V | Ip, Np/Ns, ESR | large Np/Ns (low Vout) flybacks | calc | p.135; p.145 §4.6.4.1 | high |
| PRESSMAN-1179 | filter | Flyback output needs a small LC post-filter after the main storage capacitor to remove the thin turn-off spike; sense Vout for the error amplifier BEFORE the LC filter; paralleled ceramic/film capacitors also reduce the spike | L, C small (spike < 0.5 us wide) | - | typical: 50 mV p-p fundamental with 1 V spike if unfiltered | measure | p.135 After Pressman; p.145-146 | high |
| PRESSMAN-1180 | power | Flyback output capacitor RMS ripple current (author's approximation, Ton + Tr = 0.8T) | Icap(rms) ~ Idc*sqrt(0.8) = 0.89*Idc ; capacitor ripple-current rating often governs selection over ripple voltage | Idc | DCM flyback | calc | p.146 Eq 4.15 | high |
| PRESSMAN-1181 | magnetics | Flyback core must carry the full primary ampere-turns as DC-like bias (no secondary cancellation): use gapped ferrite or distributed-gap MPP; an ungapped ferrite saturates almost immediately | - | - | flyback transformers | inspect | p.135-136 §4.6.1 | high |
| PRESSMAN-1182 | magnetics | Gapped-ferrite saturation 'cliff' in ampere-turns | NI_sat = Bsat*(la + li/u)/(0.4*pi) with Bsat ~2500 G (3C8 ferrite; bend not sharp) | la, li, u | gapped ferrite; usually la >> li/u | calc | p.138 §4.6.2 (Eq 2.37) | high |
| PRESSMAN-1183 | magnetics | Turns for a target inductance from gapped AL (per 1000 turns) | N = 1000*sqrt(L/Alg) | L, Alg | ferrite with gap (Alg from Eq 2.39 or manufacturer curves, Fig 4.3) | calc | p.138 Eq 4.14 | high |
| PRESSMAN-1184 | magnetics | MPP (molypermalloy powder) core facts | 79% Ni, 17% Fe, 4% Mo (Square Permalloy 80) powder in resin binder = distributed gap; permeability held within +/-5% over large temperature range; available mu = 14 to 550 | - | MPP toroids (Magnetics Inc. MPP303S, Arnold PC104G) | review | p.136; p.138 | high |
| PRESSMAN-1185 | magnetics | MPP permeability selection for DC-biased power magnetics: rarely use mu > 125; accept 10% inductance swing zero-to-max current | max H for 10% L falloff: mu14 170 Oe; mu26 95 Oe; mu60 39 Oe; mu125 19 Oe | Ipk, N, lm | DC bias usually >= 1 A; graph Fig 4.5 | calc | p.139 Fig 4.5 | medium |
| PRESSMAN-1186 | magnetics | MPP maximum turns and inductance for a 10% swing at peak current | Nmax = NI(10%)/Ipk with NI = H(10%)*lm/(0.4*pi) ; Lmax = 0.9*AL*(Nmax/1000)^2 | H(10%), lm, AL, Ipk | MPP toroid; core ID must fit turns at 500 CM/A | calc | p.139-141, p.145 | high |
| PRESSMAN-1187 | magnetics | MPP turns for desired inductance within 5% | Nd = 1000*sqrt(Ld/(0.95*AL)) (Ld mH, AL mH/1000 T) | Ld, AL | after selecting core from Tables 4.1-4.3 | calc | p.141 | high |
| PRESSMAN-1188 | magnetics | Powder-core turns correction for bias falloff | if L at Imax is P% low, increase turns by P% (L rises 2P% at zero bias, H rises P%, net L correct at Imax); if swing too large use a bigger core | P | MPP/powder chokes | calc | p.145 | high |
| PRESSMAN-1189 | magnetics | Tables 4.1-4.3 (MPP OD 0.80/1.06/1.84 in) cover about 90% of flyback transformers < 500 W and output inductors up to 50 A | - | - | core pre-selection | review | p.145 | high |
| PRESSMAN-1190 | power | Universal (115-220 VAC, no doubler) flyback on-time range with bipolar switches is limited by storage time | Ton(min) = Ton(max)*Vdc(min)/Vdc(max); worked 50 kHz: 128 V (92 VAC) -> 7.96 us, 372 V (264 VAC) -> 2.74 us; bipolar storage 0.5-1.0 us => fsw <= ~100 kHz | Vdc range, fsw, tstorage | universal-input flyback | calc | p.147-148 §4.7 | high |
| PRESSMAN-1191 | power | Universal-input flyback worked example | Vms = 500 V, Vdc(max) with transient 375 V, 5 V out -> Np/Ns = 21; 150 W: Ro = 0.167 ohm, Lp = 139 uH, Ip = 7.33 A; MPP 55933 (NI 859): Nmax = 117, Lmax(10% swing) = 222 uH, 90 turns for 139 uH | - | example; leakage spike ~500 V is a reliability concern vs two-switch forward/half bridge | calc | p.148-149 | high |
| PRESSMAN-1192 | power | CCM flyback output voltage (volt-second balance, no dead time) | Vom = (Vdc - 1)*(Ns/Np)*(ton/toff) - 1 = (Vdc - 1)*(Ns/Np)/((T/ton) - 1) - 1 | Vdc, Ns/Np, ton, T | CCM flyback | calc | p.150 Eq 4.16-4.17 | high |
| PRESSMAN-1193 | power | CCM flyback ramp-centre currents | Icsr = Po/(Vo*(1 - ton/T)) ; Icpr = 1.25*Po/(Vdc*(ton/T)) | Po, Vo, Vdc, ton/T | 80% efficiency | calc | p.150-151 Eq 4.18-4.20 | high |
| PRESSMAN-1194 | power | Flyback CCM/DCM boundary: primary ramp p-p equals twice the ramp-centre current at minimum power | dIp = 2*Icpr = 2.5*Po(min)/(Vdc(min)*(ton/T)) | Po(min), Vdc(min), ton/T | CCM down to Po(min) | calc | p.152 Eq 4.21 | high |
| PRESSMAN-1195 | magnetics | CCM flyback primary inductance to stay continuous down to Po(min) | Lp = (Vdc(min) - 1)*Vdc(min)*ton^2/(2.5*Po(min)*T) | Vdc(min), ton (Eq 4.17 at Vdc(min)), Po(min), T | CCM flyback | calc | p.152 Eq 4.22 | high |
| PRESSMAN-1196 | power | DCM vs CCM flyback comparison at 5 V/50 W, 38 V min, 50 kHz, Np/Ns = 9 (Vms 114 V on 150 V Vceo), CCM to 5 W | DCM: Lp 52 uH, Ipri pk 6.9 A, Isec pk 62 A, ton 9.49 us, toff 6.5 us ; CCM: Lp 791 uH, Icpr 2.77 A, Icsr 24.6 A, ton 11.86 us, toff 8.13 us | - | example (table T7) | calc | p.153-154 §4.8.4 | high |
| PRESSMAN-1197 | power | Interleaved DCM flybacks (secondaries ORed) extend DCM flyback to ~300 W with lower, higher-frequency ripple; design each at half power; at 150 W a single forward is usually better; interleaved flyback useful for > 5 outputs | Po <= ~300 W | Po, outputs | ORing works because flyback secondary is a high-impedance current source | review | p.155-156 §4.9 | high |
| PRESSMAN-1198 | derating | Single-ended flyback off-stress includes reflected output and a leakage spike up to one-third of Vdc; two-switch flyback clamps both switches at Vdc | single: Vdc(max) + (Np/Ns)(Vo + 1) + up to Vdc/3 ; two-switch: Vdc(max) | Vdc, Np/Ns, Vo | - | calc | p.157 §4.10.1 | high |
| PRESSMAN-1199 | magnetics | Two-switch flyback reflected voltage choice: leakage current resets at Vl/Ll; keep reflected voltage about two-thirds of Vdc(min), leaving one-third across leakage | Vr = (Np/Ns)*(Vo + VD3) ~ (2/3)*Vdc(min) ; Vl = Vdc - Vr ~ Vdc/3 | Vdc(min), Vo, VD3 | too low Vr lengthens magnetizing reset and cuts output power | calc | p.158-160 Fig 4.8-4.9 | high |
| PRESSMAN-1200 | power | Two-switch flyback primary current slope includes leakage | dI/dt = Vdc/(Lm + Ll) | Vdc, Lm, Ll | double-ended flyback | calc | p.157 | high |
| PRESSMAN-1201 | control-loop | Peak-current-mode control: inner pulse-by-pulse peak-current loop removes the output choke from the small-signal outer loop, gives intrinsic current limit/short-circuit protection, line feed-forward, and cures push-pull flux imbalance | - | - | forward-derived converters with current sense in switch return | review | p.161-164 §5.1-5.2 | high |
| PRESSMAN-1202 | control-loop | Voltage-mode output LC filter vs current-mode small-signal plant | LC: fo = 1/(2*pi*sqrt(L*C)), up to 180 deg, -40 dB/dec above fo ; current mode: current source into C parallel with Rload, max 90 deg, -20 dB/dec | L, C, Rload | small-signal only; L still limits large-signal slew | calc | p.164; p.172-174 | high |
| PRESSMAN-1203 | power | Current-mode supplies parallel with equal load share when each uses an equal current-sense resistor and a common error-amplifier output | Rsense1 = Rsense2 = ... ; common Veao | - | paralleled current-mode modules | inspect | p.164 §5.2.1.4 | high |
| PRESSMAN-1204 | control-loop | SG1524-class voltage-mode PWM: 3 V sawtooth (0.5 V valley, 3.5 V peak), period T ~ Rt*Ct; current-limit comparator threshold 200 mV | Rs = 0.2/Im (ohm) | Im | SG1524/UC1524A | calc | p.165-167 | high |
| PRESSMAN-1205 | control-loop | UC1846 current-mode controller: oscillator period ~0.9*Rt*Ct; totem-pole outputs sink/source 100 mA continuous, 400 mA during transitions; both outputs held low during dead time and clock pulse (guaranteed dead time) | T ~ 0.9*Rt*Ct | Rt, Ct | UC1846 (UC1842 for single-ended) | calc | p.170-171 | high |
| PRESSMAN-1206 | control-loop | Uncompensated peak-current mode regulates peak, not average, inductor current (peak-to-average error) | Iav = Ip - m2*T/2 + m2*ton/2 ; m2 = Vo/Lo (inductor down-slope) | Ip, m2, T, ton | causes line-step seesaw oscillation | calc | p.176-178 Eq 5.1 | high |
| PRESSMAN-1207 | control-loop | Current-mode perturbation propagation; duty > 50% is unstable (subharmonic) without slope compensation | dI2 = dI1*(m2/m1) ; unstable when m2 > m1 (D > 0.5) | m1 (up-slope), m2 (down-slope) | fixed-frequency peak-current mode | calc | p.179 Eq 5.2, Fig 5.5 | high |
| PRESSMAN-1208 | control-loop | Slope compensation magnitude (makes average inductor current independent of on-time) | negative ramp on EA output m = dVea/dt = (Ns/Np)*Ri*(m2/2), or positive ramp added to sense voltage dV/dt = (Ns/Np)*Ri*(m2/2) (V/s) | Ns/Np, Ri, m2 = Vo/Lo | peak-current-mode, forward-derived | calc | p.179-181 Eq 5.3-5.5 | high |
| PRESSMAN-1209 | control-loop | UC1846 slope-compensation divider from timing capacitor ramp | Vosc = (dV/dt)*ton with dV = 1.8 V, dt = 0.45*Rt*Ct ; R1/(R1 + R2) = (Ns/Np)*Ri*(m2/2)/(1.8/(0.45*Rt*Ct)) | Rt, Ct, Ri, m2 | R1 + R2 loads the timing capacitor: make it large or buffer | calc | p.182-183 Eq 5.6-5.8, Fig 5.7 | high |
| PRESSMAN-1210 | control-loop | Current-mode noise jitter: with large Lo or high fsw the sensed ramp slope near turn-off approaches zero, so small noise shifts the switching instant | use non-inductive sense resistor or DCCT, careful layout; may need smaller L (more ripple) | Lo, fsw | peak-current mode | inspect | p.183 After Pressman | high |
| PRESSMAN-1211 | power | Current-fed topologies (input inductor, no bus capacitor at bridge) are favoured for > 1000 W, outputs > 200 V, and multi-output supplies needing close slave tracking | - | Po, Vout, outputs | topology election | review | p.184 §5.6.1 | high |
| PRESSMAN-1212 | magnetics | High-voltage output chokes are prohibitive: 2 kW, 200 V, 10 A (1 A min), 50 kHz needs Lo = 200 uH (powdered-iron toroid ~2.5 in dia x 1.0 in); above ~1000 V outputs chokes risk corona/arcing during dead time | Lo = 0.5*Vo*T/Ion | Vo, Ion, T | voltage-fed PWM bridge | calc | p.185 §5.6.2.1 | high |
| PRESSMAN-1213 | derating | Voltage-fed bridge turn-on current overshoot caused by output rectifier (freewheeling) reverse recovery through leakage inductance | I_overshoot = Vcc*trr/Ll ; trr 35 ns (ultrafast) to 200 ns (fast) | Vcc, trr, Ll | PWM full bridge with centre-tapped rectifier doubling as freewheel | calc | p.186 §5.6.2.2 | high |
| PRESSMAN-1214 | protection | Output rectifier recovery ring can more than double diode reverse voltage stress; fit series RC snubbers across rectifiers | Vr(peak) up to > 2x steady reverse voltage | - | hard-switched secondaries | measure | p.186-187 | high |
| PRESSMAN-1215 | power | Clamped turn-off overlap loss per transistor (voltage held at Vcc by clamp diodes, current falls linearly) | PD = Vcc*(Ip/2)*(tf/T) | Vcc, Ip, tf, T | bridge with clamp diodes; example 2 kW, 50 kHz, Vcc(max) 370 V, Ip 10.3 A, tf 0.3 us -> 28.5 W each, 114 W for 4; conduction only 1*10.3*0.4 = 4.1 W | calc | p.187-188 Eq 5.9 | high |
| PRESSMAN-1216 | power | Buck voltage-fed full bridge: buck preregulator + unmodulated bridge at fixed ~90% of half period; V2 about 25% below the lowest rectified V1; Vo = V2*(Ns/Np); practical 2-5 kW | V2 = 0.75*V1(min) ; Vo = V2*Ns/Np | V1(min), Ns/Np | peak-rectified outputs without chokes | calc | p.188-189 §5.6.3, Fig 5.9 | high |
| PRESSMAN-1217 | power | Choke-less (peak-rectified) multi-output topologies give slave tracking within about +/-2% vs +/-6 to +/-8% with CCM output chokes (coupled output inductor is the alternative) | slave error ~ +/-2% | - | buck-fed bridge, current-fed, Weinberg | measure | p.190; p.216 | high |
| PRESSMAN-1218 | power | Buck voltage-fed bridge reduces bridge turn-off loss because switches see V2 not V1(max) | example: V2 = 0.75*302 = 227 V, Ip = 10.8 A -> (10.8/2)*227*(0.3/20) = 18.4 W per transistor, 74 W bridge (vs 114 W) | - | example | calc | p.192 §5.6.4.3 | high |
| PRESSMAN-1219 | protection | Voltage-fed bridge fed from a capacitor can still shoot through when storage time is long (high temperature, low load, low line without on-time clamp/UVLO) -> immediate failure | - | - | bipolar bridges | review | p.193; p.198 | high |
| PRESSMAN-1220 | power | Buck current-fed full bridge: no buck filter capacitor (virtual capacitor = reflected output caps), bridge pairs deliberately overlap ~1 us so V2 collapses and leakage energy goes to the load; upper Zener clamp on V2 required; only two turn-off snubbers needed | overlap ~1 us; clamp Z1 | - | 1-10 (to 20) kW; outputs > 200 V, > 5 A | review | p.193-198 §5.6.6, Fig 5.10-5.13 | high |
| PRESSMAN-1221 | power | Buck transistor turn-on loss (hard turn-on into conducting freewheel diode) | PD(turn-on) = V1*IL*tr/(2*T) ; example 330 V, 12.5 A, 0.3 us, 50 kHz -> 31 W | V1, IL, tr, T | buck preregulator; diode recovery neglected (worse for >= 400 V diodes) | calc | p.199-200 Eq 5.10 | high |
| PRESSMAN-1222 | power | Buck turn-off peak instantaneous power with constant inductor current | Pp = (V1/2)*IL at half voltage | V1, IL | reducible only by an alternate current path (turn-off snubber) | calc | p.199 After Pressman | high |
| PRESSMAN-1223 | components | Buck freewheel diode voltage rating and recovery | Vrrm >= 400 V for V1(max) = 330 V; high-voltage diodes recover slower -> Q5 current overshoot and ringing | V1(max) | high-voltage buck | review | p.200 | high |
| PRESSMAN-1224 | protection | Buck turn-on snubber inductor in series with freewheel diode | L2 = V1*tr/IL (H); example 330 V*0.3 us/12.5 A = 7.9 uH | V1(max), tr, IL | Fig 5.15 | calc | p.201-202 Eq 5.11 | high |
| PRESSMAN-1225 | protection | Turn-on snubber reset resistor limits switch stress at turn-off | VQ5(max) = V1 + Rc*IL ; example 450 = 330 + Rc*12.5 -> Rc = 9.6 ohm | V1, IL, V rating | Fig 5.15 (Rc, Dc across L2) | calc | p.202-203 Eq 5.12 | high |
| PRESSMAN-1226 | thermal | Turn-on snubber resistor dissipation equals the inductor energy per cycle (loss is diverted, not removed) | P(Rc) = 0.5*L2*IL^2/T ; example 0.5*7.9 uH*12.5^2/20 us = 31 W | L2, IL, T | resistively reset snubber | calc | p.203 §5.6.6.6 | high |
| PRESSMAN-1227 | protection | Snubber inductor must fully recharge during the switch off time | t_charge(95%) = 3*L2/Rc <= Toff ; example 3.7 us < 8 us off time | L2, Rc, Toff | Fig 5.15 | calc | p.203 §5.6.6.7 | high |
| PRESSMAN-1228 | protection | Lossless turn-on snubber: small transformer T2 replaces L2/Rc; its primary gap sets L = L2 at IL; turns ratio clamps reset voltage | Ns/Np = V1/Vn ; Q5 stress = V1 + Vn | V1, Vn | energy returned via L1 to the load | calc | p.204 Fig 5.16 | high |
| PRESSMAN-1229 | power | Buck current-fed bridge design choices: V2 25% below lowest V1 ripple trough; L1 for CCM at minimum total output power; output capacitors chosen so reflected ESR gives desired ripple at V2 | Vbr = dI*Resr(reflected) ; Vsr = Vbr*(Ns/Np) ; dI = 2*IL(min) | V1(min), Po(min), Resr | - | calc | p.205 §5.6.6.9 | high |
| PRESSMAN-1230 | power | Current-fed vs voltage-fed bridge at same V2: voltage-fed on-time 80% of half period -> 20% higher peak current; current-fed needs 20% more primary turns (longer on-time for same flux) | Ipk(VF) = 1.2*Ipk(CF) ; Np(CF) = 1.2*Np(VF) | - | - | calc | p.206 | high |
| PRESSMAN-1231 | power | Buck preregulator switch frequency and sharing | single buck switch at 2x bridge frequency, synchronized; or two buck switches at bridge frequency on alternate half cycles | - | buck-fed bridges/push-pull | review | p.206 §5.6.6.10 | high |
| PRESSMAN-1232 | power | Buck current-fed push-pull: saves two switches; off-stress 2*V2 (+ leakage spike) with V2 ~0.75*V1(min); best at 2-5 kW, multi or high-voltage outputs | Vstress = 2*V2 + spike | V2 | Fig 5.18 | calc | p.206-207 §5.6.6.11 | high |
| PRESSMAN-1233 | power | Weinberg (flyback current-fed push-pull) circuit: flyback choke in series with push-pull centre tap; no output inductors, no flux-imbalance failure, no dead time needed; usual 1-2 kW | Po ~ 1-2 kW | - | D3 returned to Vo minimizes output ripple; to Vin minimizes input ripple (continuous input current, smaller RFI filter) | review | p.208-210, p.214 Fig 5.19 | high |
| PRESSMAN-1234 | power | Weinberg non-overlap mode: centre-tap clamp and output relation | Vct(on) = (Np/Ns)*(Vo + Vd) set to 0.75*Vdc(min) ; Vo = 2*Vdc*(Ns/Np)*(ton/T) - Vd ; ton = (Vo + Vd)*(Np/Ns)*T/(2*Vdc) | Vdc, Np/Ns, ton, T | NLP/NLS = Np/Ns for negligible output ripple | calc | p.212-216 Eq 5.13 | high |
| PRESSMAN-1235 | filter | Weinberg commutation spikes (< 1 us) at transitions when one diode anode falls faster than the next rises; remove with a small LC integrator | - | - | Fig 5.21 | measure | p.214-215 | high |
| PRESSMAN-1236 | power | Weinberg non-overlap 2 kW/48 V design example (115 VAC +/-15%: 136/160/184 Vdc, 50 kHz) | Vct = 102 V, N = 2; centre-tap current 2500/102 = 24.5 A; half-primary Irms 14.7 A (7350 CM); EC70 core (Ae 2.79 cm^2, 2536 W at 48 kHz), 3F3 ~60 mW/cm^3 at 1600 G, 50 kHz -> 2.4 W in 40.1 cm^3; Np = 8 turns/half, Ns = 4; secondary Irms 25 A (12,500 CM, foil); flyback L = 49 uH; flyback sec Irms 28.5 A (14,260 CM), flyback pri Irms 21.2 A (10,600 CM) | - | example; table T8 | calc | p.215-219 §5.6.7.6-7 | high |
| PRESSMAN-1237 | power | Weinberg overlap mode (D > 0.5, boost-like) output relation | Vo = Vdc/(2*N1*(1 - D)) - Vd ; D = [2*N1*(Vo + Vd) - Vdc]/(2*N1*(Vo + Vd)) | Vdc, N1 = Np/Ns, D | overlap mode | calc | p.221-222 Eq 5.14 | high |
| PRESSMAN-1238 | power | Weinberg overlap-mode turns ratios | N1 = Vdcn/(Vo + Vd) (D = 0.5 at nominal) ; N2 = NLP/NLS > [N1*(Vo + Vd) - Vdc(min)]/(Vo + Vd), use 2x this minimum | Vdcn, Vdc(min), Vo, Vd | margin against push-pull leakage spikes | calc | p.222 Eq 5.15-5.16 | high |
| PRESSMAN-1239 | power | Weinberg above nominal input (forced non-overlap) | Vo ~ Vdc*D/(N2*(0.5 - D) + N1*D) ; D = 0.5*Vo*N2/(Vdc - Vo*(N1 - N2)) | Vdc, N1, N2 | D < 0.5; smooth transition at Vdcn | calc | p.223-224 Eq 5.17-5.18 | high |
| PRESSMAN-1240 | derating | Weinberg transistor voltage rating | Vce(max) = Vdc(max) + (N1 + N2)*(Vo + Vd) + leakage spike allowance | Vdc(max), N1, N2 | overlap-mode design | calc | p.226 | high |
| PRESSMAN-1241 | current-carrying | Weinberg overlap-mode currents | Ip(centre tap) = Pin*T/(2*Vct*Toff) (example 156/Toff(us)); flyback secondary sized for full DC output at 100% duty; flyback primary RMS = 2x half-primary RMS | Pin, Vct, Toff | currents become very high at low Vdc (short Toff) | calc | p.226-227 Eq 5.21 | high |
| PRESSMAN-1242 | components | SCR commutation constraints: anode current must be held at zero for at least tq, and reapplied dV/dt must stay below rating; early inverter SCRs: tq(recombination) 10-20 us, dV/dt 200 V/us, dI/dt 100-400 A/us, practical fsw 8-10 kHz | Toff_current >= tq ; dV/dt(reapplied) <= rating ; dI/dt(turn-on) <= rating | tq, dV/dt, dI/dt | SCR inverters | review | p.229-230, p.235 | high |
| PRESSMAN-1243 | requirements | Switching frequency must exceed the audible band for office/factory acceptability | fsw > ~20 kHz (also minimum trigger frequency of variable-frequency resonant supplies) | fsw(min) | variable-frequency resonant designs especially | review | p.230; p.252 | high |
| PRESSMAN-1244 | components | Asymmetrical SCR (ASCR) capabilities (RCA S7310; Marconi ACR25U) | tq ~4 us; reverse blocking only ~7 V (7-10 V); dV/dt 3000 V/us, dI/dt 2000 A/us with 1 V negative gate bias (vs 20 V/us and 400 A/us conventional); VDRM 400-1200 V; 40 A RMS; 40-50 kHz operation | - | reverse voltage must be clamped (anti-parallel diode ~1 V) | review | p.230-231, p.236 | high |
| PRESSMAN-1245 | components | ASCR (ACR25U) conduction and gate data | Va = 2.2 V typ at 100 A (1.2-2.2 V over 20-100 A); gate pulse > 400 ns and 90-200 mA for 100 A anode; Vgk 0.9-3 V | Ia | ACR25U | review | p.231-234 Fig 6.2-6.4 | high |
| PRESSMAN-1246 | power | SCR turn-on loss control: anode voltage falls slowly; use half-sine anode current with base width > 2.5 us (Va < 5 V over pulse); >= ~8 us half-period keeps turn-on loss low | t_halfsine >= 2.5 us (min), ~8-10 us preferred | pi*sqrt(LC) | resonant SCR converters | calc | p.232; p.239; p.245 Fig 6.5 | medium |
| PRESSMAN-1247 | power | Series-resonant SCR commutation: SCR self-extinguishes if anti-parallel diode conduction time exceeds tq; heavier load shortens diode time | tr = 2*pi*sqrt(L*C) ; Td(min, max load) > tq(max) | L, C, load | single-ended and bridge SCR resonant converters | sim | p.236-237; p.243-244 | high |
| PRESSMAN-1248 | power | SCR resonant inverter trigger period for low distortion sine output | tt = 1.5-2 x tr at minimum line, maximum load | tr | DC/AC use | calc | p.237 | high |
| PRESSMAN-1249 | power | Resonant converters regulate by varying trigger frequency (constant-width pulses), losing the fixed-frequency advantage of syncing to display horizontal rate or system clock; but lower di/dt gives less RFI | - | - | resonant vs PWM election | review | p.237-239 | high |
| PRESSMAN-1250 | power | SCR resonant power capability | single 800 V/45 A RMS SCR single-ended: ~1 kW; half bridge with two 800 V ASCRs: up to 4 kW from rectified 220 VAC; 1200 V full bridge: up to 8 kW | Po | ASCR ACR25U-class | review | p.239-240 | high |
| PRESSMAN-1251 | protection | Series-loaded resonant half bridge tolerates output short but not open circuit (Q collapses, SCR fails to commutate); shunt-loaded tolerates open but not short | - | load extremes | SCR resonant bridges | review | p.240-241 | high |
| PRESSMAN-1252 | power | Series-loaded SCR half-bridge resonant period choice | minimum resonant period = 2*tq(worst) (tq 5 us typ +20% = 6 us -> 12 us, 83 kHz); chosen 20 us (50 kHz) so half period >= 4 x 2.5 us | tq, Fig 6.5 | Chambers method | calc | p.245 Eq 6.1 | high |
| PRESSMAN-1253 | power | Series-loaded SCR half-bridge transformer ratio (primary peak = 60% of bridge-capacitor voltage) | Vp(min) = 0.6*Vdc(min)/2 ; Np/Ns = 0.6*Vdc(min)/(2*(Vo + 2)) | Vdc(min), Vo | bridge rectifier (2 V) | calc | p.245 Eq 6.2-6.3 | high |
| PRESSMAN-1254 | power | Series-loaded SCR half-bridge peak current and LC ratio (diode peak = 1/4 SCR peak) | Io(dc) = 1.25*Ips/pi ; Ipp = 0.8*pi*Io(dc)*(Ns/Np) ; Vap = 0.8*Vdc(min) ; Ipp = Vap/sqrt(L/C) ; sqrt((L1 + L3)/C3) = Vdc(min)*(Np/Ns)/(pi*Io(dc)) | Vdc(min), Io(dc), Np/Ns | minimum line, maximum load, edge of continuous | calc | p.246 Eq 6.4-6.8 | high |
| PRESSMAN-1255 | power | Series-loaded SCR half-bridge 2 kW example | 48 V, 41.7 A, 270-370 Vdc: Np/Ns = 1.62; C3 = 0.95 uF; L3 + L1 = 10.6 uH; Ipp = 64.7 A; SCR RMS 22.9 A (duty 0.25); diode peak 16.2 A; rectifier peaks 104.8/26.2 A -> use full-wave CT (one diode drop) not bridge | - | example | calc | p.247-248 | high |
| PRESSMAN-1256 | magnetics | Do not rely on transformer leakage alone for the resonant inductance (wide variation); add discrete inductance; smaller L3/L1 lowers SCR off-stress and dV/dt | - | - | resonant SCR bridges | inspect | p.247; p.250 | high |
| PRESSMAN-1257 | magnetics | Single-ended SCR resonant converter charging inductor and open-circuit behaviour | L3 >= 20*(L1 + L2); gap T1 so magnetizing L does not kill Q at light/open load | L1, L2, L3 | Fig 6.15 | calc | p.250 | high |
| PRESSMAN-1258 | derating | Single-ended SCR resonant capacitor peak voltage vs trigger ratio | Vmax = 2*Vdc/(1 - tr/tt) ; tr/tt = 0.6 -> 5.0*Vdc (690 V at 138 V) fits an 800 V SCR | Vdc(min), tr/tt | Table 6.1 | calc | p.251-252 Eq 6.10 | high |
| PRESSMAN-1259 | power | Single-ended SCR resonant design relations | Is(av) = 1.25*Ipp*N*tr/(pi*tt) ; N = 0.6*Vmax/(Vo + 1) ; Ipp = 1.6*Vmax/sqrt((L1 + L2)/C1) ; tr = 2*pi*sqrt((L1 + L2)*C1) | Vmax, Vo, Io, tr, tt | example 1 kW/48 V/20.8 A: N = 8.44, Ipp = 10.3 A, C1 = 0.024 uF, L1 + L2 = 275 uH, tt(min) 26.6 us (38 kHz), min trigger ~13 kHz | calc | p.252-254 Eq 6.11-6.15 | high |
| PRESSMAN-1260 | power | Cuk converter conversion ratio and coupling-capacitor voltage | Vo = Vdc*ton/toff (inverted) ; Vp = Vdc*T/toff | Vdc, ton, toff | CCM | calc | p.256-257 Eq 6.16-6.18 | high |
| PRESSMAN-1261 | power | Cuk inductor slopes; with L1 = L2 slopes match, and winding L1, L2 on one core (proper polarity) drives input and output ripple current to ~zero | L1: +Vdc/L1, -(Vp - Vdc)/L1 ; L2: +(Vp - Vo)/L2, -Vo/L2 ; L1 = L2 -> equal | L1, L2 | ultra-low-noise input/output; isolation needs extra 1:1 transformer | calc | p.255-259 Eq 6.19 | high |
| PRESSMAN-1262 | power | Housekeeping (auxiliary) supply requirements | 1-3 W at ~10-45 V (typ 10-15 V) on output common; loads tolerate +/-15%; regulate to ~+/-2% for predictable operation; PWM chips accept 8-40 V | P, V | all isolated converters with controller on output side | review | p.260-264 | high |
| PRESSMAN-1263 | hw-fw | Prefer an always-present housekeeping supply over bootstrapping the controller from a main-transformer auxiliary winding (on shutdown the decaying VCC can race to excessive pulse width; remote indicators lost) | - | - | controller supply architecture | review | p.261 | high |
| PRESSMAN-1264 | power | 60-Hz transformer + linear-regulator housekeeping supply | 2-6 VA transformer (6 VA: 1.88 x 1.56 x 0.85 in; 2 VA: 1.88 x 1.56 x 0.65 in); rectified DC ~3 V above regulated output; ~55% efficiency at 3 W, 10% high line | - | off-line (AC prime power) | calc | p.262-264 Fig 6.19 | high |
| PRESSMAN-1265 | power | Housekeeping oscillator converter efficiencies from DC prime power | self-oscillating converter 75-80% at 3 W; with linear preregulator (60 V -> 35 V) ~44%; with buck preregulator 70-75% | - | telecom 38-60 V input | calc | p.264-265 | high |
| PRESSMAN-1266 | power | Flyback housekeeping start-up circuit values | start-up emitter follower from 10 V Zener (~9 V to PWM IC); bootstrap winding ~12 V turns Q3 off; base bias ~1 mA supplies 10-20 mA IC start current; slaves track master within 1-2% | - | Fig 6.21/6.28 | inspect | p.265-266; p.278-279 | high |
| PRESSMAN-1267 | power | Royer (saturating-core) oscillator frequency | F = Vdc*1e8/(4*Bs*Np*Ae) (Hz; Bs G, Ae cm^2) ; half period T/2 = 2*Bs*Np*Ae*1e-8/Vdc | Vdc, Bs, Np, Ae | square-loop core; frequency proportional to Vdc (RFI spread) | calc | p.266-268 Eq 6.20-6.22 | high |
| PRESSMAN-1268 | reliability | Voltage-fed Royer end-of-on-time current spike (1-2 us, 3-5x prior current, at ~Vdc) can exceed SOA (secondary breakdown); fix with series centre-tap inductor (current-fed) and 100-500 pF cross-coupled collector-to-opposite-base capacitors | spike 3-5 x Ic for 1-2 us | - | example 2.4 W at 38 V: 50.6% efficient voltage-fed vs ~71% current-fed | measure | p.268-271 | high |
| PRESSMAN-1269 | power | Current-fed Royer worked data | series 630 uH (50 T on 1408-3C8 ferrite, 2-mil total gap); 38/50/60 V in -> 11.24/15.05/18.08 V out into 49.8 ohm; efficiency 69.6/71.4/72.7% | - | Table 6.2 | measure | p.271-273 Table 6.2 | high |
| PRESSMAN-1270 | power | Buck-preregulated current-fed Royer housekeeping supply | composite efficiency 57.9-69.5% over 38-60 V and 2.3-5.7 W; line regulation < 0.5% (feedback from buck output), load regulation ~+/-5%; output 9.79-10.74 V; sense bootstrapped slave for better load regulation | - | Fig 6.26-6.27 | measure | p.271-274 | high |
| PRESSMAN-1271 | magnetics | Royer core must have a square hysteresis loop (most ferrites unsuitable) else flip-over is sluggish and the 'on' transistor fails in tens of microseconds; very square amorphous cores with Br ~ Bsat can latch and not oscillate | - | - | Royer transformers | review | p.274-276 | high |
| PRESSMAN-1272 | magnetics | Square-loop tape core frequency limits | Square Permalloy 80: Bsat 6600-8200 G, 1-mil or 1/2-mil tape; use 1/2 mil above 50 kHz; losses prohibitive above 100 kHz; amorphous (Metglas, Toshiba MB): Bsat 5700-6200 G, usable to ~200 kHz; Fair-rite 83 ferrite: Bsat 4000 G, max ~50 kHz | fsw, material | Table 6.3 | review | p.276-277 | high |
| PRESSMAN-1273 | thermal | Tape-wound cores have high thermal resistance; limit total loss unless heat-sunk | Rth = 40-100 C/W ; Ploss(total) < 1 W | Ploss | toroidal tape cores | calc | p.277 | high |
| PRESSMAN-1274 | power | Current-fed Royer application window | 12/24 V automotive, 28 V aircraft, 48 V telecom inputs; up to 200-300 W with modern cores; no output inductor -> easy high voltage | - | - | review | p.277 | high |
| PRESSMAN-1275 | power | Minimum-parts DCM flyback housekeeping supply: 6 W at 50 kHz from 38-60 V (just at DCM threshold at 38 V), ~70% efficient; beyond 6 W at < 38 V enters CCM and oscillates unless loop changed; secondary peak 3 A vs 0.36 A for buck-fed Royer | - | - | Fig 6.28-6.29 | measure | p.278-280 | high |
| PRESSMAN-1276 | materials | Switching-power ferrites (all vendors) share a similar DC loop at 100 C | within 10% of full saturation at 3000-3200 G; coercive force 0.10-0.15 Oe; remanence 900-1200 G | material | MnZn power ferrites (3C8, 3C85, 3F3, R, P, H7C1, H7C4, N27, N47) | review | p.287 §7.2.1 | high |
| PRESSMAN-1277 | magnetics | Datasheet/Table 7.1 core-loss data are for bipolar (1st + 3rd quadrant) excitation; for unipolar (forward, flyback) the book conservatively takes half the tabulated loss at the same peak flux (alternatives: 1/4 argument; TDK Kfc = 0.39 at 20 kHz, 0.35 at 60 kHz, 0.34 at 100 kHz; Table 7.1 note: read the table at Bpk/2) | P_unipolar(Bmax) = 0.5*P_bipolar(Bmax) (book default) | Bmax, f, material | forward/flyback core-loss estimates | calc | p.287-289; Table 7.1 note p.291 | high |
| PRESSMAN-1278 | magnetics | Core loss from loss density | Pcore(W) = Pv(mW/cm^3)*Ve(cm^3)/1000 | Pv at (Bpk, f, 100 C), Ve | ferrite; Table 7.1 at 100 C | calc | p.294 | high |
| PRESSMAN-1279 | magnetics | Ferrite loss scaling used for frequency/flux derating | Pv proportional to Bpk^2.7 and f^1.6 to f^1.7 | Bpk, f | ferrite power materials | calc | p.294; p.314 | high |
| PRESSMAN-1280 | magnetics | Pot cores: lowest radiated field (coil enclosed) but narrow lead slot; use up to ~125 W, mostly DC/DC; avoid for high currents, many outputs, and high voltage (arcing in exit notch) | Po <= ~125 W | Po, Vout, #leads | core-shape election | review | p.289-292 §7.2.2 | high |
| PRESSMAN-1281 | magnetics | Gapped cores: use manufacturer centre-leg-gapped cores (published AL and saturation 'cliff' ampere-turns) rather than shimmed halves; shims are not reproducible over time, temperature and production, and an outer-leg gap increases EMI | - | - | chokes, flyback and gapped forward transformers | inspect | p.292-293 | high |
| PRESSMAN-1282 | magnetics | Round-centre-leg cores (EC, ETD) have ~11% shorter mean turn length than square-leg EE of equal area -> ~11% lower winding resistance and copper loss | MLT(round) ~ 0.89*MLT(square) | - | core-shape election | calc | p.293 | high |
| PRESSMAN-1283 | magnetics | EE core power range and paralleling: EE cores span < 5 W to 5-10 kW; two identical square-leg EE cores side by side double Ae (half the turns) and roughly double power | Ae(pair) = 2*Ae | - | core-shape election | calc | p.293 | high |
| PRESSMAN-1284 | magnetics | RM core centre-hole tuning rod adjusts AL by up to 30% but only for frequency-sensitive filters, not power transformers (extra loss) | dAL <= 30% | - | RM cores | review | p.293 | high |
| PRESSMAN-1285 | magnetics | Other shapes: PQ optimizes volume vs radiating surface and winding area (lowest rise per watt); LP cores (long centre legs) minimize leakage for low profile; UU/UI for high voltage or ultra-high power, rarely < 1 kW, with larger leakage | - | Po, profile, Vout | core-shape election | review | p.293-294 | high |
| PRESSMAN-1286 | magnetics | Book-wide design peak flux density for ferrite transformers | Bmax = 1600 G below ~50 kHz (core loss negligible <= 25 kHz; 2000 G ends linear region; hard saturation > 3200 G at 100 C); reduce above 50 kHz for temperature rise | fsw | all topologies; transient/EA-delay margin | calc | p.294-295 §7.2.3 | high |
| PRESSMAN-1287 | magnetics | Bobbin winding space factor for power transformers | SF = 0.4 (typ 0.4-0.6) of bobbin window is copper; primary and total secondary each get half (0.2*Ab) | Ab | derivation basis of Eq 7.7/7.13/7.18 | calc | p.295-296 | high |
| PRESSMAN-1288 | compliance | VDE safety construction allowances that eat window area | 4 mm creepage margin between each end of a layer and the bobbin ends; three layers of 1-mil insulation between windings (sandwich construction costs ~6 mils of height) | - | off-line transformers to European safety specs (at time of writing) | inspect | p.296 | high |
| PRESSMAN-1289 | power | Forward converter output power vs primary current (80% eff., duty 0.4 at Vdc(min)) | Po = 0.32*Vdc(min)*Ipft = 0.506*Vdc(min)*Irms ; Ipft = 1.58*Irms | Vdc(min), Ipft/Irms | forward | calc | p.296-297 Eq 7.1-7.2 | high |
| PRESSMAN-1290 | magnetics | Forward converter core power capability (core selection equation) | Po = 0.00050*Bmax*f*Ae*Ab/Dcma (W; Bmax G, f Hz, Ae and Ab cm^2, Dcma circular mils per rms A) ; in-inch form 0.00322*Bmax*f*Ae*Ab(in^2)/Dcma | Bmax, f, Ae, Ab, Dcma | SF 0.4, eff 80%, Ton = 0.8T/2 | calc | p.297-299 Eq 7.3-7.7 | high |
| PRESSMAN-1291 | power | Push-pull output power vs half-primary current | Po = 0.64*Vdc(min)*Ipft = 1.01*Vdc(min)*Irms | Vdc(min), Ipft/Irms | push-pull | calc | p.299 Eq 7.8-7.9 | high |
| PRESSMAN-1292 | magnetics | Push-pull core power capability (twice the forward) | Po = 0.0010*Bmax*f*Ae*Ab/Dcma (W, G, Hz, cm^2, CM/A) | Bmax, f, Ae, Ab, Dcma | SF 0.4; flux swing 2*Bmax | calc | p.299-300 Eq 7.10-7.13 | high |
| PRESSMAN-1293 | magnetics | Push-pull at twice the forward power on the same core doubles core loss but leaves copper loss unchanged; with low-loss ferrite, core loss is not the limit below ~30 kHz | Pcore(PP) = 2*Pcore(FWD) ; Pcu(PP) = Pcu(FWD) | - | same core, same Bmax | calc | p.301-302 §7.3.2.1 | high |
| PRESSMAN-1294 | magnetics | Doubling a forward converter's frequency and peak current doubles core power with unchanged copper loss but ~3x core loss (f^1.7) per Pressman (K.B.: loss need not rise if Bpk unchanged); practical only if original fsw < 50-80 kHz (switching/snubber losses) | P(2f) = 2*P(f); Pcu same; Pcore ~ 3x | fsw | forward converter | calc | p.302-304 §7.3.2.2 | high |
| PRESSMAN-1295 | power | Forward reset ratio Nr/Np = 0.5 trade | Ton(max) = 0.53*T vs 0.4*T; peak current 1.51 Ip vs 2 Ip; switch stress 3*Vdc vs 2*Vdc; Nr/Np < 0.5 gives unacceptable off-voltage stress | Nr/Np | forward converter | calc | p.303-304 | high |
| PRESSMAN-1296 | power | Half-bridge output power vs primary current (duty 0.8, Vdc/2 on primary) | Po = 0.32*Vdc(min)*Ipft = 0.358*Vdc(min)*Irms ; Irms = 0.894*Ipft | Vdc(min), Ipft/Irms | half bridge | calc | p.304-305 Eq 7.14-7.17 | high |
| PRESSMAN-1297 | magnetics | Half/full-bridge core power capability | Po = 0.0014*Bmax*f*Ae*Ab/Dcma (W, G, Hz, cm^2, CM/A) = 2.8 x forward capability | Bmax, f, Ae, Ab, Dcma | SF 0.4, eff 80% | calc | p.305-306 Eq 7.18 | high |
| PRESSMAN-1298 | magnetics | A full bridge gets no more power than a half bridge from the same core; its 2x power needs a larger core (2x primary turns at the same current density) | P_FB(core) = P_HB(core) | - | core selection | review | p.306 §7.3.4 | high |
| PRESSMAN-1299 | magnetics | Core-power chart scaling (Tables 7.2a/7.2b) | P = P_table*(Bmax/1600)*(500/Dcma) ; push-pull = 2 x forward table ; bridge table = 2.8 x forward table | Bmax, Dcma | tables computed at 1600 G, 500 CM/A, SF 0.4 | calc | p.309; p.312 notes | high |
| PRESSMAN-1300 | current-carrying | Winding current density rule of thumb and its limitation | 500 CM/A is the usual compromise; down to 300 CM/A acceptable; below 300 CM/A definitely avoid; CM/A only fixes DC resistance (skin/proximity add AC loss) | Irms | transformer windings | calc | p.313 | high |
| PRESSMAN-1301 | process | Core/frequency selection procedure from Tables 7.2a/b | pick topology (switch V/I stress, cost); in chosen frequency column take first core (ascending AeAb) with Po >= spec; or fix core and move to first frequency meeting Po; if short, consider push-pull (2x) | Po, fsw, space | then verify temperature rise at chosen Bmax | review | p.313 | high |
| PRESSMAN-1302 | magnetics | Above ~50 kHz large cores may not reach tabulated power at 1600 G without excess rise; reduce Bmax to 1400-800 G and derate power by Bmax/1600 | Bmax = 800-1400 G for f > 50 kHz (large cores) | f, core size | check with Table 7.1 + Eq 7.19 rise | calc | p.314 §7.3.5.1 | high |
| PRESSMAN-1303 | thermal | Small cores tolerate higher flux at high frequency (loss ~ volume, cooling ~ surface) | E55 (43.5 cm^3, 16.5 in^2) at 1600 G/200 kHz in 3C85 (700 mW/cm^3): 30.5 W core loss -> ~185 C rise; 813E343 (1.64 cm^3, 1.90 in^2): 1.15 W -> ~57 C | - | worked example | calc | p.314; p.319-320 | high |
| PRESSMAN-1304 | thermal | Transformer surface temperature rise from total loss and radiating area (heat-sink analogy) | dT(C) = 80*A^-0.70*P^0.85 ; Rt(1 W) = 80*A^-0.70 (C/W) ; power factor K1 = P^-0.15 ; A = total outer area 2(w*h + w*t + h*t) in in^2 ; P = core + copper loss (W) | A, P | natural convection; accuracy ~ +/-10 C; forced air lowers rise | calc | p.315-318 Fig 7.4 | high |
| PRESSMAN-1305 | thermal | Internal hot spot (centre leg) above outer surface | add 10-15 C to surface rise | dT_surface | educated guess used by core makers | calc | p.315 | medium |
| PRESSMAN-1306 | thermal | EC core thermal resistance, measured vs Rt = 80*A^-0.70 | EC35 18.5 vs 23.7 C/W; EC41 16.5 vs 19.0; EC52 11.0 vs 12.6; EC70 7.5 vs 9.2 (formula conservative by ~15-28%) | core | Table 7.4 | calc | p.320 Table 7.4 | high |
| PRESSMAN-1307 | magnetics | Skin depth in copper at 70 C | S(mils) = 2837/sqrt(f[Hz]) (e.g. 17.9 mils at 25 kHz, 8.97 at 100 kHz, 4.01 at 500 kHz) | f | round/foil copper | calc | p.323 Eq 7.19, Table 7.5 | high |
| PRESSMAN-1308 | magnetics | Skin-effect AC/DC resistance of round wire (annulus model) | Rac/Rdc = (d/2S)^2/[(d/2S)^2 - (d/2S - 1)^2] for d > 2S, else ~1 | d (bare dia), S | sinusoidal current | calc | p.324 Eq 7.20-7.21, Fig 7.6 | high |
| PRESSMAN-1309 | current-carrying | Larger wire still has lower Rac, but large single wires are too lossy at high frequency; n parallel strands of equal total CM increase skin area by sqrt(n) (two strands: +41%) | A_skin(n strands) = sqrt(n)*A_skin(1) | n | skin effect only | calc | p.326 | high |
| PRESSMAN-1310 | components | Litz wire practice | strands 28-50 AWG; ~5% cost premium; every strand soldered at both ends (broken/open strands raise loss, may cause audible noise/vibration); avoid Litz at fsw <= 50 kHz; occasionally at 100 kHz — weigh vs up to four parallel wires | fsw | transformer windings | inspect | p.327 | high |
| PRESSMAN-1311 | current-carrying | Copper foil windings for high-current secondaries | use foil above ~15-20 A; thickness ~1.37 x skin depth at the fundamental; width = bobbin width (less VDE margins); 1-mil Mylar interlayer | Irms, fsw | secondaries | calc | p.327 | high |
| PRESSMAN-1312 | magnetics | Square-wave (rectangular) winding currents: evaluate skin depth as average over first three harmonics | Sav = 13.2, 9.66, 6.83, 4.83 mils at 25, 50, 100, 200 kHz; AWG 18 Rac/Rdc 1.13/1.35/1.75/2.36 (square) vs 1.05/1.15/1.40/1.85 (sine) | fsw, AWG | Tables 7.7-7.8 (approximation; higher harmonics make it optimistic) | calc | p.327-330 Tables 7.7-7.8 | high |
| PRESSMAN-1313 | magnetics | Proximity effect dominates skin effect in multilayer coils: surface eddy currents grow with layer number (layer m faces carry about (m-1) and m times the net layer current) | I_surface(layer m) ~ m*I_layer | layers | transformer windings | review | p.328-333 Fig 7.7-7.8 | high |
| PRESSMAN-1314 | magnetics | Dowell AC/DC resistance ratio for multilayer windings | X = h*sqrt(Fl)/delta with h = 0.866*d (round wire equivalent height), Fl = Nl*d/w (Fl = 1 for foil), delta = skin depth ; for X > 5: FR = Rac/Rdc ~ ((2*p^2 + 1)/3)*X ; p = layers per portion ; X = 4: p = 2 -> ~13, p = 1 -> 4, p = 1/2 -> 2 | d, Nl, w, delta, p | graph Fig 7.9 for X < 5 | calc | p.333-336 Fig 7.9-7.11 | high |
| PRESSMAN-1315 | magnetics | At high frequency, size wire/foil for Dowell X ~ 1.5 instead of blindly using 500 CM/A (higher Rdc but lower Rac and copper loss) | X = h*sqrt(Fl)/delta ~ 1.5 | d, delta | multilayer windings | calc | p.336 | high |
| PRESSMAN-1316 | magnetics | Interleave primary and secondary layers to cut layers per portion (2 -> 1 cuts FR from ~13 to ~4 at X = 4); a single-layer secondary between two half-primaries works at 1/2 layer per portion | p(after interleave) < p(stacked) | winding order | forward/push-pull/bridge transformers (not flyback) | inspect | p.334-336 Fig 7.10-7.11 | high |
| PRESSMAN-1317 | magnetics | Push-pull interleave order: the simultaneously conducting half-primary and half-secondary must be adjacent; a non-conducting half-secondary next to a conducting primary carries eddy currents | Fig 7.12a order | winding order | push-pull | inspect | p.336 Fig 7.12 | high |
| PRESSMAN-1318 | magnetics | Flyback windings: interleaving gives no proximity benefit (primary and secondary not simultaneous); minimize layer count and use finer wire than 500 CM/A | - | - | flyback transformers | inspect | p.336 | high |
| PRESSMAN-1319 | magnetics | Area product (McLyman) figure of merit for core size | AP = Ae*Aw (cm^4) ; power capability of Eq 7.7/7.13/7.18 is proportional to Ae*Ab | Ae, Aw | detailed AP design methods in §7.6+ (part 2 extraction) | calc | p.338-339 §7.6.1 | high |
| PRESSMAN-1320 | emc | Terminal-current continuity by topology: buck input current is pulsating (needs input capacitor/RFI filter) while its output current is continuous; boost input current is continuous but output (diode) current is discontinuous (output-capacitor ripple current); Cuk has both continuous | - | topology | input-filter and output-capacitor ripple-current sizing | review | p.15 Note; p.33 Tip; p.254 §6.5 | high |
| PRESSMAN-1321 | emc | Switching devices whose noisy drain is isolated from the heat-sink tab (integrated off-line switches) substantially reduce RFI in DCM flybacks; a tab tied to the switching node radiates via the heat sink | - | package | off-line flyback layout/mechanical | inspect | p.129 After Pressman | medium |
| PRESSMAN-1322 | reliability | Optocoupler feedback has wide gain tolerance and was regarded as not very reliable; alternatives are primary-side sensing (e.g. regulate the preregulated bus or a bootstrapped slave winding) or a pulse transformer carrying the PWM signal | - | isolation feedback method | isolated converters | review | p.190; p.261 | medium |

## 2. Formulas & tables (numbers)

### T1. Linear regulator efficiency example, AC line +/-15%, 2.5 V headroom, negligible ripple (p.7)

| Vo (V) | Io (A) | Vdc(min) (V) | Vdc(max) (V) | Headroom max (V) | Pin(max) (W) | Pout (W) | Q1 dissipation max (W) | Efficiency Po/Pin(max) (%) |
|---|---|---|---|---|---|---|---|---|
| 5.0 | 10 | 7.5 | 10.1 | 5.1 | 101 | 50 | 51 | 50 |
| 15.0 | 10 | 17.5 | 23.7 | 8.7 | 237 | 150 | 87 | 63 |
| 30.0 | 10 | 32.5 | 44.0 | 14 | 440 | 300 | 140 | 68 |

Note: with realistic ripple the 5 V case falls to 32-35% (p.7). Fig 1.2 (graph): efficiency vs Vo for line +/-5..15%, 8 V p-p ripple, 2.5 V headroom.

### T2. Buck efficiency worked example, 48 V -> 5 V, 50 kHz, Ts = 0.3 us (p.19-20)

| Loss model | Formula | Efficiency |
|---|---|---|
| Conduction only (1 V drops) | Vo/(Vo+1) | 83.3% |
| + best-case linear overlap (Fig 1.5a) | Vo/(Vo+1+Vdc*Ts/3T) | 80.1% |
| + worst-case clamped-inductive (Fig 1.5b) | Vo/(Vo+1+2*Vdc*Ts/T) | 67.2% |
| Linear regulator, same job | Vo/Vdc | 10.4% |

### T3. Push-pull / forward / interleaved design constants (Ch. 2, 80% efficiency, Ton(max) = 0.8*T/2 at Vdc(min), 500 CM/A)

| Quantity | Push-pull | Single-ended forward (Nr = Np) | Two-switch forward | Interleaved forward | Source |
|---|---|---|---|---|---|
| Equivalent flat-top primary current Ipft | 1.56 Po/Vdc(min) | 3.13 Po/Vdc(min) | 3.13 Po/Vdc(min) | 3.13 Pot/(2 Vdc(min)) | Eq 2.9, 2.28; p.98 |
| Primary RMS | 0.986 Po/Vdc(min) (each half) | 1.97 Po/Vdc(min) | 1.97 Po/Vdc(min) | per converter at Pot/2 | Eq 2.11, 2.41 |
| Primary copper (CM) | 493 Po/Vdc(min) (each half) | 985 Po/Vdc(min) | 985 Po/Vdc(min) | Eq 2.42 at Pot/2 | Eq 2.12, 2.42 |
| Secondary RMS / CM | 0.632 Idc / 316 Idc (each half) | 0.632 Idc / 316 Idc | same | same | Eq 2.13-2.14, 2.43-2.44 |
| Switch off-stress | 2.6 Vdc(max) | 2.6 Vdc(max) | Vdc(max) | 2.6 Vdc(max) | Eq 2.15, 2.29; p.96 |
| Output choke (CCM to 0.1 Ion) | 0.5 Vo T/Ion | 3 Vo T/Ion | 3 Vo T/Ion | 0.5 Vo T/Ion | Eq 2.20, 2.47 |
| Output cap (ESR-dominated) | 80e-6 dI/Vr | 65e-6 dI/Vor | 65e-6 dI/Vor | 80e-6 dI/Vr | Eq 2.22, 2.48 |
| Design flux | dB = 3200 G (+/-1600 G) <= 50 kHz | 0 -> 1600 G (gapped, Br ~200 G) | 1600 G <= 50 kHz; 1400-800 G at 100-300 kHz | as forward | p.63, p.90, p.97 |
| Practical power | <~500 W (bipolar) | 150-200 W (Vdc < 60 V) / <200 W | 400-500 W | 2x single forward at same Ipk | p.71, p.83, p.97, p.98 |

### T4. Forward converter peak current and switch stress vs reset/power turns ratio (Eq 2.33, 2.34; p.86)

| Nr/Np | 0.6 | 0.8 | 1.0 | 1.2 | 1.4 | 1.6 |
|---|---|---|---|---|---|---|
| Ipft (x Po/Vdc(min)) | 2.50 | 2.81 | 3.12 | 3.43 | 3.74 | 4.06 |
| Vms (x Vdc(max)) + leakage spike | 2.67 | 2.25 | 2.00 | 1.83 | 1.71 | 1.62 |

### T5. Ferrite flux-density guidance (Ch. 2 text; 3C8-class ferrite)

| Condition | Peak flux density | Source |
|---|---|---|
| Linear region of loop (ungapped) | <= +/-2000 G | p.50, Fig 2.3 |
| Push-pull design value, <= 50 kHz (transient-safe) | +/-1600 G (dB = 3200 G) | p.62-63 |
| 100-200 kHz (core-loss limited) | 1200 or even 800 G | p.63 |
| 100-300 kHz | ~+/-1200 to +/-800 G (Fig 2.3); 1400-800 G (two-switch forward, p.97) | p.51, p.97 |
| Ungapped unipolar (forward) usable swing | ~1000 G (Br ~1000 G) | p.88 |
| Gapped 2-4 mil unipolar usable swing | ~1800 G (Br ~200 G) | p.88 |
| Forward design value, low frequency | 0 -> 1600 G | p.90 |

### T6. MPP toroids: maximum turns Nmax and inductance Lmax (uH) for <= 10% inductance falloff at peak current Ip (Tables 4.1-4.3, p.142-144; Magnetics Inc.)

Lmax = 0.9*AL*(Nmax/1000)^2; Nmax = NI(10%)/Ip; NI from H(10%) via H = 0.4*pi*NI/lm. OCR of Tables 4.2/4.3 was scrambled; values below were re-assembled and cross-checked against Lmax = 0.9*AL*(N/1000)^2 (agree to rounding). Table 4.1 mu125 row is printed as shown (does not fully match the formula).

Table 4.1 — OD 1.060 in, ID 0.58 in, height 0.44 in, lm = 6.35 cm

| Core | mu | AL (mH/1000 T) | H 10% (Oe) | NI max | Ip = 1 A | 2 A | 3 A | 5 A | 10 A | 20 A | 50 A |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 55930 | 125 | 157 | 19 | 96 | 96 / 1,382 | 48 / 339 | 32 / 145 | 19 / 56 | 10 / 15 | 5 / 3.5 | 2 / 0.6 |
| 55894 | 60 | 75 | 39 | 197 | 197 / 2,620 | 99 / 662 | 66 / 294 | 39 / 103 | 20 / 27 | 10 / 7 | 4 / 1 |
| 55932 | 26 | 32 | 95 | 480 | 480 / 6,635 | 240 / 1,659 | 160 / 737 | 96 / 265 | 48 / 66 | 24 / 17 | 10 / 3 |
| 55933 | 14 | 18 | 170 | 859 | 859 / 11,954 | 430 / 2,995 | 286 / 1,325 | 172 / 479 | 86 / 120 | 43 / 30 | 17 / 5 |

Table 4.2 — OD 0.80 in, ID 0.50 in, height 0.25 in, lm = 5.09 cm

| Core | mu | AL | H 10% | NI max | 1 A | 2 A | 3 A | 5 A | 10 A | 20 A | 50 A |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 55206 | 125 | 68 | 19 | 77 | 77 / 363 | 39 / 93 | 26 / 41 | 15 / 14 | 8 / 4 | 4 / 1 | 2 / 0.24 |
| 55848 | 60 | 32 | 39 | 158 | 158 / 719 | 79 / 180 | 53 / 81 | 32 / 29 | 16 / 7 | 8 / 2 | 3 / 0.26 |
| 55208 | 26 | 14 | 95 | 385 | 385 / 1,868 | 193 / 469 | 128 / 206 | 77 / 75 | 39 / 19 | 19 / 4.5 | 8 / 0.8 |
| 55209 | 14 | 7.8 | 170 | 689 | 689 / 3,333 | 345 / 836 | 230 / 371 | 138 / 134 | 69 / 33 | 34 / 8 | 14 / 1.4 |

Table 4.3 — OD 1.84 in, ID 0.95 in, height 0.71 in, lm = 10.74 (printed "in"; cm by consistency with the other tables)

| Core | mu | AL | H 10% | NI max | 1 A | 2 A | 3 A | 5 A | 10 A | 20 A | 50 A |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 55438 | 125 | 281 | 19 | 162 | 162 / 6,637 | 81 / 1,659 | 54 / 737 | 32 / 259 | 16 / 65 | 8 / 16 | 3 / 2 |
| 55439 | 60 | 135 | 39 | 333 | 333 / 13,473 | 167 / 3,389 | 111 / 1,497 | 67 / 545 | 33 / 132 | 17 / 35 | 7 / 6 |
| 55440 | 26 | 59 | 95 | 812 | 812 / 35,011 | 406 / 8,753 | 271 / 3,900 | 162 / 1,394 | 81 / 348 | 41 / 89 | 16 / 14 |
| 55441 | 14 | 32 | 170 | 1,454 | 1,454 / 60,744 | 727 / 15,222 | 485 / 6,774 | 291 / 2,439 | 145 / 605 | 73 / 153 | 29 / 24 |

(cell = Nmax / Lmax uH)

### T7. DCM vs CCM flyback at identical spec: 5 V, 50 W, 50 kHz, Vdc(min) 38 V, Np/Ns = 9, CCM down to 5 W (p.154)

| Mode | Primary inductance (uH) | Primary peak current (A) | Secondary peak current (A) | On time (us) | Off time (us) |
|---|---|---|---|---|---|
| Discontinuous | 52 | 6.9 | 62.0 | 9.49 | 6.5 |
| Continuous | 791 | 2.77 (ramp centre) | 24.6 (ramp centre) | 11.86 | 8.13 |

### T8. Weinberg (flyback current-fed push-pull) on-times — non-overlap design, 2 kW, 48 V, 50 kHz, N = 2, Vct = 102 V (Table 5.1, p.216)

| Vdc (V) | 200 | 184 | 160 | 136 |
|---|---|---|---|---|
| ton/T | 0.245 | 0.266 | 0.306 | 0.360 |
| ton (us) | 4.9 | 5.3 | 6.12 | 7.2 |

### T9. Weinberg overlap/non-overlap design, 2 kW, 48 V, 50 kHz, N1 = 3.27, N2 = 2.46, Vdcn = 160 V, Vdc(min) = 100 V (Table 5.2, p.225)

| Vdc (V) | 50 | 100 | 136 | 160 | 175 | 185 | 200 |
|---|---|---|---|---|---|---|---|
| D | 0.840 | 0.688 | 0.576 | 0.500 | 0.433 | 0.404 | 0.366 |
| Ton (us) | 16.9 | 13.8 | 11.5 | 10.0 | 8.67 | 8.08 | 7.32 |
| Toff (us) | 3.1 | 6.2 | 8.5 | 10.0 | 11.3 | 11.9 | 12.7 |
| Ip (A), Eq 5.21 | 50.2 | 25.2 | 18.3 | 15.6 | 13.8 | 13.1 | 12.3 |
| Irms per half secondary (A), Eq 5.22 | 24.6 | 15.1 | 12.2 | 11.0 | - | - | - |

Note: the printed Irms values equal sqrt(Ip^2*Toff/T + (Ip/2)^2*(T - 2*Toff)/(2T)); the prose says the Ip/2 segment occurs twice per period, which would give larger values — treat as the book's worked numbers.

### T10. Single-ended SCR resonant converter: capacitor peak voltage vs tr/tt at Vdc(min) = 138 V (Table 6.1, p.252; Vmax = 2*Vdc/(1 - tr/tt))

| tr/tt | 0.7 | 0.6 | 0.5 | 0.4 | 0.3 |
|---|---|---|---|---|---|
| Vmax / Vdc | 6.6 | 5.0 | 4.0 | 3.3 | 2.9 |
| Vmax (V) at 138 V | 911 | 690 | 552 | 455 | 393 |

### T11. Current-fed Royer oscillator measured data, 630 uH series inductor, Ro = 49.8 ohm (Table 6.2, p.273)

| Vdc in (V) | Idc in (mA) | Pin (W) | Vout (V) | Pout (W) | Efficiency (%) |
|---|---|---|---|---|---|
| 38.0 | 96 | 3.65 | 11.24 | 2.54 | 69.6 |
| 50.0 | 127 | 6.37 | 15.05 | 4.55 | 71.4 |
| 60.0 | 151 | 9.03 | 18.08 | 6.56 | 72.7 |

(Same Royer voltage-fed, no series inductor: 50.6% at 38 V, p.269.)

### T12. Square-hysteresis-loop core materials for Royer oscillators (Table 6.3, p.277; losses for excursions between +/- saturation)

| Material | Bsat (G) | Core loss 50 kHz (W/cm^3) | Core loss 100 kHz (W/cm^3) |
|---|---|---|---|
| Toshiba MB (amorphous) | 6000 | 0.49 | 1.54 |
| Metglas 2714A (amorphous) | 6000 | 0.62 | 1.72 |
| Square Permalloy 80, 1/2-mil tape | 7800 | 0.98 | 2.26 |
| Square Permalloy 80, 1-mil tape | 7800 | 4.2 | 9.6 |
| Fair-rite Type 83 ferrite | 4000 | 4.0 (1 W/cm^3 at 25 kHz) | 30.0 |

Text ranges: Square Permalloy 80 Bsat 6600-8200 G; amorphous 5700-6200 G (p.276).

### T13. Ferrite core loss at 100 C, bipolar excitation, mW/cm^3 (Table 7.1, p.290-291) — recoverable rows only

For unipolar (forward, flyback) excitation: book text uses half the tabulated loss at the same Bpk; the table note says read the table at Bpk/2 (p.289, p.291).

| f (kHz) | Material | 1600 G | 1400 G | 1200 G | 1000 G | 800 G | 600 G |
|---|---|---|---|---|---|---|---|
| 100 | Ferroxcube 3C8 | 850 | 600 | 400 | 250 | 140 | 65 |
| 100 | Ferroxcube 3C85 | 260 | 160 | 100 | 80 | 48 | 30 |
| 100 | Ferroxcube 3F3 | 180 | 120 | 70 | 55 | 30 | 14 |
| 100 | Magnetics R | 250 | 150 | 85 | 70 | 35 | 16 |
| 100 | Magnetics P | 340 | 181 | 136 | 96 | 57 | 23 |
| 100 | TDK H7C1 | 500 | 300 | 200 | 140 | 75 | 35 |
| 100 | TDK H7C4 (5 values printed; alignment inferred) | 300 | 180 | 100 | 70 | 50 | - |
| 200 | Ferroxcube 3C8 (3 values printed; alignment inferred) | - | - | - | 700 | 400 | 190 |
| 200 | Ferroxcube 3C85 | 700 | 500 | 350 | 300 | 180 | 75 |
| 200 | Ferroxcube 3F3 | 600 | 360 | 250 | 180 | 85 | 40 |
| 200 | Magnetics R | 650 | 450 | 280 | 200 | 100 | 45 |
| 200 | Magnetics P | 850 | 567 | 340 | 227 | 136 | 68 |
| 200 | TDK H7C1 | 1400 | 900 | 500 | 400 | 200 | 100 |
| 200 | TDK H7C4 | 800 | 500 | 300 | 200 | 100 | 45 |
| 50 | Ferroxcube 3C8 (probable; block scrambled) | 270 | 190 | 130 | 80 | 65 | 40 |

Printed value sequences whose flux-column alignment was lost in the OCR (highest-flux value first): 500 kHz — 3C85: 1800, 950, 500; 3F3: 1800, 1200, 900, 500, 280; Magnetics R: 2200, 1300, 1100, 700, 400; Magnetics P: 4500, 3200, 1800, 1100, 570; TDK H7C4: 2800, 1800, 1200, 980, 320; TDK H7F: 100. 1000 kHz — 3C85: 2000; 3F3: 3500, 2500, 1200; Magnetics R: 5000, 3000, 1500; Magnetics P: 6200. Siemens N27: 480 (100 kHz), 960/480 (200 kHz); N47: 190 (100 kHz), 480 (200 kHz) — columns unknown. The 20 kHz and 50 kHz blocks (3C8, 3C85, 3F3, R, P, H7C1, H7C4, N27) are too scrambled to reproduce; see printed Table 7.1.
Text anchors: 3C85 at 200 kHz, 1600 G = 700 mW/cm^3 (p.314); 3F3 at 50 kHz, 1600 G ~ 60 mW/cm^3 (p.217).

### T14. Maximum available transformer output power (W) — Tables 7.2a (forward) / 7.2b (half or full bridge), p.307-312

Basis: Bmax = 1600 G, Dcma = 500 CM/rms A, SF = 0.4, efficiency 80%. Forward: Po = 0.00050*Bmax*f*Ae*Ab/Dcma = 0.0016*f*AeAb. Half/full bridge = 2.8 x forward value (Table 7.2b; e.g. E55 at 20 kHz 885.6 W). Push-pull = 2 x forward value. Scale by Bmax/1600 and 500/Dcma. Values below are the FORWARD column values (Table 7.2a).

| Core | Ae (cm^2) | Ab (cm^2) | AeAb (cm^4) | Vol (cm^3) | 20 kHz | 24 kHz | 48 kHz | 72 kHz | 96 kHz | 150 kHz | 200 kHz | 250 kHz | 300 kHz |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EE 814E250 | 0.202 | 0.171 | 0.035 | 0.57 | 1.1 | 1.3 | 2.7 | 4.0 | 5.3 | 8.3 | 11.1 | 13.8 | 16.6 |
| EE 813E187 | 0.225 | 0.329 | 0.074 | 0.89 | 2.4 | 2.8 | 5.7 | 8.5 | 11.4 | 17.8 | 23.7 | 29.6 | 35.5 |
| EE 813E343 | 0.412 | 0.359 | 0.148 | 1.64 | 4.7 | 5.7 | 11.4 | 17.0 | 22.7 | 35.5 | 47.3 | 59.2 | 71.0 |
| EE 812E250 | 0.395 | 0.581 | 0.229 | 1.93 | 7.3 | 8.8 | 17.6 | 26.4 | 35.3 | 55.1 | 73.4 | 91.8 | 110.2 |
| EE 782E272 | 0.577 | 0.968 | 0.559 | 3.79 | 17.9 | 21.4 | 42.9 | 64.3 | 85.8 | 134.0 | 178.7 | 223.4 | 268.1 |
| EE E375 | 0.810 | 1.149 | 0.931 | 5.64 | 29.8 | 35.7 | 71.5 | 107.2 | 143.0 | 223.4 | 297.8 | 372.3 | 446.7 |
| EE E21 | 1.490 | 1.213 | 1.807 | 11.50 | 57.8 | 69.4 | 138.8 | 208.2 | 277.6 | 433.8 | 578.4 | 722.9 | 867.5 |
| EE 783E608 | 1.810 | 1.781 | 3.224 | 17.80 | 103.2 | 123.8 | 247.6 | 371.4 | 495.1 | 773.7 | 1031.6 | 1289.4 | 1547.3 |
| EE 783E776 | 2.330 | 1.810 | 4.217 | 22.90 | 135.0 | 161.9 | 323.9 | 485.8 | 647.8 | 1012.2 | 1349.5 | 1686.9 | 2024.3 |
| EE E625 | 2.340 | 1.370 | 3.206 | 20.80 | 102.6 | 123.1 | 246.2 | 369.3 | 492.4 | 769.4 | 1025.9 | 1282.3 | 1538.8 |
| EE E55 | 3.530 | 2.800 | 9.884 | 43.50 | 316.3 | 379.5 | 759.1 | 1138.6 | 1518.2 | 2372.2 | 3162.9 | 3953.6 | 4744.3 |
| EE E75 | 3.380 | 2.160 | 7.301 | 36.00 | 233.6 | 280.4 | 560.7 | 841.1 | 1121.4 | 1752.2 | 2336.3 | 2920.3 | 3504.4 |
| EC35 | 0.843 | 0.968 | 0.816 | 6.53 | 26.1 | 31.3 | 62.7 | 94.0 | 125.3 | 195.8 | 261.1 | 326.4 | 391.7 |
| EC41 | 1.210 | 1.350 | 1.634 | 10.80 | 52.3 | 62.7 | 125.5 | 188.2 | 250.9 | 392.0 | 522.7 | 653.4 | 784.1 |
| EC52 | 1.800 | 2.130 | 3.834 | 18.80 | 122.7 | 147.2 | 294.5 | 441.7 | 588.9 | 920.2 | 1226.9 | 1533.6 | 1840.3 |
| EC70 | 2.790 | 4.770 | 13.308 | 40.10 | 425.9 | 511.0 | 1022.1 | 1533.1 | 2044.2 | 3194.0 | 4258.7 | 5323.3 | 6388.0 |
| ETD29 | 0.760 | 0.903 | 0.686 | 5.50 | 22.0 | 26.4 | 52.7 | 79.1 | 105.4 | 164.7 | 219.6 | 274.5 | 329.4 |
| ETD34 | 0.971 | 1.220 | 1.185 | 7.64 | 37.9 | 45.5 | 91.0 | 136.5 | 182.0 | 284.3 | 379.1 | 473.8 | 568.6 |
| ETD39 | 1.250 | 1.740 | 2.175 | 11.50 | 69.6 | 83.5 | 167.0 | 250.6 | 334.1 | 522.0 | 696.0 | 870.0 | 1044.0 |
| ETD44 | 1.740 | 2.130 | 3.706 | 18.00 | 118.6 | 142.3 | 284.6 | 427.0 | 569.3 | 889.5 | 1186.0 | 1482.5 | 1779.0 |
| ETD49 | 2.110 | 2.710 | 5.718 | 24.20 | 183.0 | 219.6 | 439.2 | 658.7 | 878.3 | 1372.3 | 1829.8 | 2287.2 | 2744.7 |
| Pot 704 | 0.070 | 0.022 | 0.002 | 0.07 | 0.0 | 0.1 | 0.1 | 0.2 | 0.2 | 0.4 | 0.5 | 0.6 | 0.7 |
| Pot 905 | 0.101 | 0.034 | 0.003 | 0.13 | 0.1 | 0.1 | 0.3 | 0.4 | 0.5 | 0.8 | 1.1 | 1.4 | 1.6 |
| Pot 1107 | 0.167 | 0.054 | 0.009 | 0.25 | 0.3 | 0.3 | 0.7 | 1.0 | 1.4 | 2.2 | 2.9 | 3.6 | 4.3 |
| Pot 1408 | 0.251 | 0.097 | 0.024 | 0.50 | 0.8 | 0.9 | 1.9 | 2.8 | 3.7 | 5.8 | 7.8 | 9.7 | 11.7 |
| Pot 1811 | 0.433 | 0.187 | 0.081 | 1.12 | 2.6 | 3.1 | 6.2 | 9.3 | 12.4 | 19.4 | 25.9 | 32.4 | 38.9 |
| Pot 2213 | 0.635 | 0.297 | 0.189 | 2.00 | 6.0 | 7.2 | 14.5 | 21.7 | 29.0 | 45.3 | 60.4 | 75.4 | 90.5 |
| Pot 2616 | 0.948 | 0.407 | 0.386 | 3.53 | 12.3 | 14.8 | 29.6 | 44.4 | 59.3 | 92.6 | 123.5 | 154.3 | 185.2 |
| Pot 3019 | 1.380 | 0.587 | 0.810 | 6.19 | 25.9 | 31.1 | 62.2 | 93.3 | 124.4 | 194.4 | 259.2 | 324.0 | 388.8 |
| Pot 3622 | 2.020 (7.2a prints 2.20) | 0.774 | 1.563 | 10.70 | 50.0 | 60.0 | 120.1 | 180.1 | 240.2 | 375.2 | 500.3 | 625.4 | 750.5 |
| Pot 4229 | 2.660 | 1.400 | 3.724 | 18.20 | 119.2 | 143.0 | 286.0 | 429.0 | 572.0 | 893.8 | 1191.6 | 1489.6 | 1787.5 |
| RM5 | 0.250 | 0.095 | 0.024 | 0.45 | 0.8 | 0.9 | 1.8 | 2.7 | 3.6 | 5.7 | 7.6 | 9.5 | 11.4 |
| RM6 | 0.370 | 0.155 | 0.057 | 0.80 | 1.8 | 2.2 | 4.4 | 6.6 | 8.8 | 13.8 | 18.4 | 22.9 | 27.5 |
| RM8 | 0.630 | 0.310 | 0.195 | 1.85 | 6.2 | 7.5 | 15.0 | 22.5 | 30.0 | 46.9 | 62.5 | 78.1 | 93.7 |
| RM10 | 0.970 | 0.426 | 0.413 | 3.47 | 13.2 | 15.9 | 31.7 | 47.6 | 63.5 | 99.2 | 132.2 | 165.3 | 198.3 |
| RM12 | 1.460 | 0.774 | 1.130 | 8.34 | 36.2 | 43.4 | 86.8 | 130.2 | 173.6 | 271.2 | 361.6 | 452.0 | 542.4 |
| RM14 | 1.980 | 1.100 | 2.178 | 13.19 | 69.7 | 83.6 | 167.3 | 250.9 | 334.5 | 522.7 | 697.0 | 871.2 | 1045.4 |
| PQ 42016 (Magnetics) | 0.620 | 0.256 | 0.159 | 2.31 | 5.1 | 6.1 | 12.2 | 18.3 | 24.4 | 38.1 | 50.8 | 63.5 | 76.2 |
| PQ 42020 | 0.620 | 0.384 | 0.238 | 2.79 | 7.6 | 9.1 | 18.3 | 27.4 | 36.6 | 57.1 | 76.2 | 95.2 | 114.3 |
| PQ 42620 | 1.190 | 0.322 | 0.383 | 5.49 | 12.3 | 14.7 | 29.4 | 44.1 | 58.9 | 92.0 | 122.6 | 153.3 | 183.9 |
| PQ 42625 | 1.180 | 0.502 | 0.592 | 6.53 | 19.0 | 22.7 | 45.5 | 68.2 | 91.0 | 142.2 | 189.6 | 236.9 | 284.3 |
| PQ 43220 | 1.700 | 0.470 | 0.799 | 9.42 | 25.6 | 30.7 | 61.4 | 92.0 | 122.7 | 191.8 | 255.7 | 319.6 | 383.5 |
| PQ 43230 | 1.610 | 0.994 | 1.600 | 11.97 | 51.2 | 61.5 | 122.9 | 184.4 | 245.8 | 384.1 | 512.1 | 640.1 | 768.2 |
| PQ 43535 | 1.960 | 1.590 | 3.116 | 17.26 | 99.7 | 119.7 | 239.3 | 359.0 | 478.7 | 747.9 | 997.2 | 1246.6 | 1495.9 |
| PQ 44040 | 2.010 | 2.490 | 5.005 | 20.45 | 160.2 | 192.2 | 384.4 | 576.6 | 768.8 | 1201.2 | 1601.6 | 2002.0 | 2402.4 |

Table 7.2b print errors noted: 812E250 row repeats 154.2 (sequence is 20.6, 24.8, 49.3, 74.1, 98.7, 154.2, 205.6, 257.0, 308.4); E375 150 kHz printed "6254" (= 625.4); 783E776 72 kHz printed "136.2" (formula gives ~1360).

### T15. Geometrically interchangeable core type numbers (Table 7.3, p.316-317) — rows whose alignment is unambiguous

| Family | Ferroxcube-Philips | Magnetics Inc. | TDK |
|---|---|---|---|
| EC | EC35, EC41, EC52, EC70 | 43517, 44119, 45224, 47035 | EC35, EC41, EC52, EC70 |
| ETD | ETD34, ETD39, ETD44, ETD49 (also ETD29) | 43434, 43939, 44444, 44949 | ETD34, ETD39, ETD44, ETD49 |
| Pot | 704, 905, 1107, 1408, 1811, 2213, 2616, 3019, 3622, 4229 | 40704, 40905, 41107, 41408, 41811, 42213, 42616, 43019, 43622, 44229 | P7/4, P9/5, P11/7, P14/8, P18/11, P22/13, P26/16, P30/19, P36/22, P42/29 (as printed partly garbled) |
| PQ | - | 42016, 42020, 42620, 42625, 43220, 43230, 43535, 44040 | PQ20/16, PQ20/20, PQ26/20, PQ26/25, PQ32/20, PQ32/30, PQ35/35, PQ40/40 (PQ50/50 also listed) |
EE and RM cross-references (Magnetics 41205, 41808, 43515, 44317, 44721, 45724; 41110, 41510, 41812, 42316, 42819, 43723; TDK EE19, EE42/42/15, EE55/55/21; RM4-RM14) lost row alignment in the OCR.

### T16. Core thermal resistance, EC cores (Table 7.4, p.320)

| Core | Radiating area (in^2) | Rt measured by manufacturer (C/W) | Rt from 80*A^-0.70 (C/W) |
|---|---|---|---|
| EC35 | 5.68 | 18.5 | 23.7 |
| EC41 | 7.80 | 16.5 | 19.0 |
| EC52 | 10.8 | 11.0 | 12.6 |
| EC70 | 22.0 | 7.5 | 9.2 |

### T17. Skin depth in copper at 70 C, S = 2837/sqrt(f) mils (Table 7.5, p.323)

| f (kHz) | 25 | 50 | 75 | 100 | 125 | 150 | 175 | 200 | 225 | 250 | 300 | 400 | 500 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S (mils) | 17.9 | 12.7 | 10.4 | 8.97 | 8.02 | 7.32 | 6.78 | 6.34 | 5.98 | 5.67 | 5.18 | 4.49 | 4.01 |

### T18. Skin-effect Rac/Rdc, sinusoidal current (Table 7.6, p.325); d = max bare diameter

| AWG | d (mils) | 25 kHz d/S | Rac/Rdc | 50 kHz d/S | Rac/Rdc | 100 kHz d/S | Rac/Rdc | 200 kHz d/S | Rac/Rdc |
|---|---|---|---|---|---|---|---|---|---|
| 12 | 81.6 | 4.56 | 1.45 | 6.43 | 1.85 | 9.10 | 2.55 | 12.87 | 3.50 |
| 14 | 64.7 | 3.61 | 1.30 | 5.09 | 1.54 | 7.21 | 2.00 | 10.21 | 2.90 |
| 16 | 51.3 | 2.87 | 1.10 | 4.04 | 1.25 | 5.72 | 1.70 | 8.09 | 2.30 |
| 18 | 40.7 | 2.27 | 1.05 | 3.20 | 1.15 | 4.54 | 1.40 | 6.42 | 1.85 |
| 20 | 32.3 | 1.80 | 1.00 | 2.54 | 1.05 | 3.60 | 1.25 | 5.09 | 1.54 |
| 22 | 25.6 | 1.43 | 1.00 | 2.02 | 1.00 | 2.85 | 1.10 | 4.04 | 1.30 |
| 24 | 20.3 | 1.13 | 1.00 | 1.60 | 1.00 | 2.26 | 1.04 | 3.20 | 1.15 |
| 26 | 16.1 | 0.90 | 1.00 | 1.27 | 1.00 | 1.79 | 1.00 | 2.54 | 1.05 |
| 28 | 12.7 | 0.71 | 1.00 | 1.00 | 1.00 | 1.42 | 1.00 | 2.00 | 1.00 |
| 30 | 10.1 | 0.56 | 1.00 | 0.80 | 1.00 | 1.13 | 1.00 | 1.59 | 1.00 |
| 32 | 8.1 | 0.45 | 1.00 | 0.64 | 1.00 | 0.90 | 1.00 | 1.28 | 1.00 |
| 34 | 6.4 | 0.36 | 1.00 | 0.50 | 1.00 | 0.71 | 1.00 | 1.01 | 1.00 |

(Text p.324-326 quotes AWG 14 at 25 kHz as 1.25 and at 200 kHz as 3.3 from the Fig 7.6 graph; table values above are as printed.)

### T19. Skin-effect Rac/Rdc for square-wave currents, average skin depth of first three harmonics (Table 7.7, p.329)

Sav = 13.2 mils (25 kHz), 9.66 (50 kHz), 6.83 (100 kHz), 4.83 (200 kHz).

| AWG | d (mils) | 25 kHz d/S | Rac/Rdc | 50 kHz d/S | Rac/Rdc | 100 kHz d/S | Rac/Rdc | 200 kHz d/S | Rac/Rdc |
|---|---|---|---|---|---|---|---|---|---|
| 12 | 81.6 | 6.18 | 1.85 | 8.45 | 2.40 | 11.95 | 3.30 | 16.89 | 4.50 |
| 14 | 64.7 | 4.90 | 1.50 | 6.70 | 1.90 | 9.47 | 2.65 | 13.40 | 3.70 |
| 16 | 51.3 | 3.89 | 1.25 | 5.31 | 1.59 | 7.51 | 2.12 | 10.62 | 2.90 |
| 18 | 40.7 | 3.08 | 1.13 | 4.21 | 1.35 | 5.96 | 1.75 | 8.43 | 2.36 |
| 20 | 32.3 | 2.45 | 1.05 | 3.34 | 1.17 | 4.73 | 1.45 | 6.69 | 1.90 |
| 22 | 25.6 | 1.94 | 1.00 | 2.65 | 1.07 | 3.75 | 1.25 | 5.30 | 1.56 |
| 24 | 20.3 | 1.54 | 1.00 | 2.10 | 1.01 | 2.97 | 1.12 | 4.20 | 1.35 |
| 26 | 16.1 | 1.22 | 1.00 | 1.67 | 1.00 | 2.36 | 1.04 | 3.33 | 1.17 |
| 28 | 12.7 | 0.96 | 1.00 | 1.31 | 1.00 | 1.86 | 1.00 | 2.63 | 1.07 |
| 30 | 10.1 | 0.77 | 1.00 | 1.05 | 1.00 | 1.48 | 1.00 | 2.09 | 1.01 |
| 32 | 8.1 | 0.61 | 1.00 | 0.84 | 1.00 | 1.19 | 1.00 | 1.68 | 1.00 |
| 34 | 6.4 | 0.48 | 1.00 | 0.66 | 1.00 | 0.94 | 1.00 | 1.33 | 1.00 |

### T20. AWG 18 Rac/Rdc, sine vs square wave (Table 7.8, p.330)

| f (kHz) | 25 | 50 | 100 | 200 |
|---|---|---|---|---|
| Sine (Table 7.6) | 1.05 | 1.15 | 1.40 | 1.85 |
| Square (Table 7.7) | 1.13 | 1.35 | 1.75 | 2.36 |

### T21. Dowell proximity factor anchors (Fig 7.9, p.334-336; graph)

FR = Rac/Rdc vs X = h*sqrt(Fl)/delta, h = 0.866 d, Fl = Nl*d/w (1 for foil). Asymptote for X > 5: FR ~ ((2p^2 + 1)/3)*X. Curves plotted for p = 1/2, 1, 1.5, 2, 2.5, 3, 3.5, 4, 6, 10 layers per portion.

| X | p = 1/2 | p = 1 | p = 2 |
|---|---|---|---|
| 4 | ~2 | ~4 | ~13 |


## 3. Mechanizable checks

Conventions: T = 1/fsw (s); D = Ton/T; Vd = diode drop (book default 1 V fast-recovery, 0.5 V Schottky); Vsw = switch on-drop (book default 1 V); all "min/max" are over the specified input range. Where the book assumes 80% efficiency the constant is kept. Checks marked (derived) combine stated relations.

`CHECK-buck-duty-and-ripple`: inputs Vin_min, Vin_max (V), Vout (V), Iout_nom, Iout_min (A), fsw (Hz), L (H) → D(Vin) = Vout/Vin; dI(Vin) = (Vin - Vout)*D*T/L = (Vin - Vout)*Vout/(Vin*fsw*L), evaluated at Vin_max (worst); ripple% = 100*dI/Iout_nom → pass: dI <= 0.2*Iout_nom for the book's CCM-to-10%-load design (Eq 1.8; halving L -> dI = 0.4*Ion is an accepted trade with DCM at 0.2 Ion) → margin = 0.2*Iout_nom - dI → rows PRESSMAN-1010, 1012, 1026, 1028.

`CHECK-ccm-dcm-boundary`: inputs dI (A, from topology check at Vin_max), Iout_min (A), loop_designed_for_dcm (bool) → Io_crit = dI/2 → pass: Iout_min > Io_crit (CCM over whole range) OR loop explicitly compensated for both modes; for master/slave multi-output supplies every output must pass at its own Imin → margin = Iout_min - Io_crit → rows 1022, 1024, 1058, 1164.

`CHECK-choke-saturation`: inputs Iout_max (A), dI (A), Isat (A, at max temperature) → Ipk = Iout_max + dI/2 → pass: Isat >= Ipk (book: >= 1.1*Ion when dI = 0.2*Ion) → margin = Isat/Ipk - 1 → rows 1027, 1029.

`CHECK-output-ripple-esr`: inputs dI (A p-p), C (F), ESR (ohm; if unknown and aluminium electrolytic: ESR = 65e-6/C, range 50e-6/C..80e-6/C), Ton, Toff (s), Vripple_spec (V p-p) → V_esr = dI*ESR; V_cap = dI*T/(4*C) (book's conservative method; exact triangle = dI*T/(8*C)); V_total = V_esr + V_cap (in-phase worst case); esr_dominant = ESR*C > max(Ton, Toff)/2 → pass: V_total <= Vripple_spec → margin = Vripple_spec - V_total → rows 1031-1036, 1097, 1123.

`CHECK-cap-from-ripple-spec` (inverse sizing): inputs dI, Vripple_spec, capacitor family → ESR_req = Vripple_spec/dI; C_req = 65e-6/ESR_req (buck, forward) or 80e-6/ESR_req (push-pull/bridge, conservative) → pass: chosen C >= C_req AND datasheet ESR(fsw) <= ESR_req → rows 1033, 1034, 1097, 1123.

`CHECK-buck-efficiency-estimate`: inputs Vin_max, Vout, Iout, fsw, Ts (s, switching transition time; book uses 0.3 us bipolar, 0.05 us MOSFET), Vdrop (V, conduction drop, default 1) → eta_best = Vout/(Vout + Vdrop + Vin*Ts*fsw/3); eta_worst = Vout/(Vout + Vdrop + 2*Vin*Ts*fsw) → pass: eta_worst >= eta_spec (else confirm by thermal measurement) → margin = eta_worst - eta_spec → rows 1014-1018.

`CHECK-linear-regulator`: inputs Vac tolerance T (%), Vripple (V p-p), Vout, Iout, pass-element type → Vdc_max = [(1 + 0.01T)/(1 - 0.01T)]*(Vout + Vhead + Vripple/2) with Vhead = 2.5 V (NPN) or 0.5 V (PNP); Pd = (Vdc_max - Vout)*Iout; eta_min = Vout/Vdc_max → pass: headroom at ripple trough at low line >= Vhead AND Pd <= thermal budget → rows 1001-1006.

`CHECK-boost-dcm-deadtime` (derived): inputs Vin_min, Vout, Iout_max, L, fsw → Ton = sqrt(2*T*L*Iout_max*(Vout - Vin_min))/Vin_min; Tr = Vin_min*Ton/(Vout - Vin_min); duty_used = (Ton + Tr)/T → pass: duty_used <= 0.8 (20% dead time) → margin = 0.8 - duty_used; also Ip = Vin_min*Ton/L for switch/choke rating → rows 1040-1047.

`CHECK-inverting-dcm-deadtime` (derived): inputs Vin_min, Vout (magnitude), Pout_max, L, fsw → Ton = sqrt(2*L*Pout_max*T)/Vin_min (from Pt = 0.5*L*Ip^2/T, Ip = Vin*Ton/L); Tr = Vin_min*Ton/Vout → pass: (Ton + Tr)/T <= 0.8 → rows 1049-1051.

`CHECK-flyback-dcm-design`: inputs Vin_min, Vin_max, Vout, Pout_max (W), fsw, Np/Ns, Lp (H), Vrating (V), Vd = 1 V → Ton = sqrt(2.5*T*Pout_max*Lp)/Vin_min (inverse of Eq 4.8); Tr = (Vin_min - 1)*Ton/((Vout + 1)*Np/Ns); Ip = Vin_min*Ton/Lp; Is_pk = Ip*Np/Ns; Irms_pri = Ip*sqrt(Ton/(3T)); Irms_sec = Is_pk*sqrt(Tr/(3T)); Vms = Vin_max + (Np/Ns)*(Vout + 1); Vsw_peak = Vms + 0.3*Vin_max → pass: (Ton + Tr)/T <= 0.8 AND 1 - Vsw_peak/Vrating >= 0.25 (book example; target ~0.30) → margins = 0.8 - (Ton + Tr)/T; 1 - Vsw_peak/Vrating → rows 1160-1174.

`CHECK-flyback-output-cap`: inputs Iout, T, Tr (s), dV_droop spec (V), ESR (ohm), Is_pk (A), cap ripple-current rating (A rms) → C_req = Iout*(T - Tr)/dV_droop; V_spike = Is_pk*ESR; I_cap_rms = 0.89*Iout → pass: C >= C_req AND I_rating >= I_cap_rms AND (V_spike <= spike spec OR LC post-filter present) → rows 1177-1180.

`CHECK-flyback-ccm-boundary`: inputs Vin_min, Vout, Np/Ns, Pout_min, fsw, Lp → ton/T from Vout = (Vin_min - 1)*(Ns/Np)/((T/ton) - 1) - 1, i.e. ton/T = (Vout + 1)*(Np/Ns)/((Vin_min - 1) + (Vout + 1)*(Np/Ns)); Lp_min_ccm = (Vin_min - 1)*Vin_min*ton^2/(2.5*Pout_min*T) → pass (for an intended CCM design): Lp >= Lp_min_ccm; for an intended DCM design the complementary CHECK-flyback-dcm-design applies → rows 1192-1195.

`CHECK-switch-voltage-stress`: inputs topology, Vin_max (steady), Np/Nr (forward), Np/Ns and Vout (flyback), Vrating → Vstress = 2.6*Vin_max (push-pull; forward with Nr = Np); Vin_max*(1 + Np/Nr) + spike (forward, general); Vin_max (two-switch forward, half bridge, full bridge, two-switch flyback); Vin_max + (Np/Ns)*(Vout + 1) + up to Vin_max/3 (single-ended flyback); 2*V2 + spike (buck-fed push-pull) ; apply transient factor 1.15 when transients unspecified → pass: Vrating >= 1.15*Vstress (plus design margin; book selects 200 V parts for 156 V stress) → margin = Vrating/(1.15*Vstress) - 1 → rows 1084, 1094, 1103, 1107, 1124, 1134, 1166, 1198, 1232.

`CHECK-switch-peak-current`: inputs topology, Pout, Vin_min → Ipft = 1.56*Pout/Vin_min (push-pull, full bridge); 3.13*Pout/Vin_min (forward, two-switch forward, half bridge); 3.13*Pout/(2*Vin_min) (interleaved forward); 1.56*(Pout/Vin_min)*(1 + Nr/Np) (forward, general reset ratio); flyback Ip per CHECK-flyback-dcm-design → pass: device pulse-current rating >= Ipft (MOSFET flyback: rating ~5-10x Ip for low Rds(on)) → rows 1077, 1102, 1106, 1131, 1141, 1152, 1172.

`CHECK-winding-rms-and-copper`: inputs topology, Pout, Vin_min, Idc per secondary, wire circular-mil area per winding (CM) → Irms: push-pull half-primary 0.986*Pout/Vin_min; forward primary 1.97*Pout/Vin_min; half-bridge primary 2.79*Pout/Vin_min; full-bridge primary 1.40*Pout/Vin_min; full-wave half-secondary or forward secondary 0.632*Idc; flyback triangles per CHECK-flyback-dcm-design; forward reset winding 0.365*Vin*Ton/Lmg; Dcma = CM/Irms → pass: Dcma >= 300 (fail below), warn if Dcma < 500 → margin = Dcma/300 - 1 → rows 1079-1083, 1117-1119, 1142, 1153, 1173-1174, 1300.

`CHECK-transformer-flux`: inputs topology, Vin_min, Vin_max, fsw, Np, Ae (cm^2), material → Ton_max = 0.4*T (forward/push-pull/bridges at Vin_min); Vpri = Vin_min - 1 (push-pull, forward), Vin_min/2 - 1 (half bridge), Vin_min - 2 (full bridge, two-switch forward); dB = Vpri*Ton_max*1e8/(Np*Ae) (G); Bpk = dB/2 (bipolar) or dB (unipolar); transient: dB_tr = 1.5*dB → pass: Bpk <= 1600 G for fsw <= 50 kHz (<= 1400-800 G above, per core-loss/temperature check) AND bipolar: -Bpk + dB_tr <= ~3200 G (hard saturation at 100 C); unipolar gapped: Br(~200 G) + dB_tr below saturation → margin = 1600/Bpk - 1 → rows 1059, 1071, 1074-1076, 1115, 1140, 1151, 1286.

`CHECK-core-power-capability`: inputs topology, Ae, Ab (cm^2), fsw, Bmax (G), Dcma, Pout → Pcore = K*Bmax*fsw*Ae*Ab/Dcma with K = 0.00050 (forward), 0.0010 (push-pull), 0.0014 (half/full bridge) → pass: Pcore >= Pout → margin = Pcore/Pout - 1 → rows 1290, 1292, 1297, 1299, table T14.

`CHECK-magnetizing-current`: inputs Vin, Ton, Lm (H), Ipft → Ipm = (Vin - 1)*Ton/Lm → pass: Ipm <= 0.10*Ipft → margin = 0.10 - Ipm/Ipft → rows 1061, 1062.

`CHECK-leakage-ratio`: inputs Llk (H, measured with all other windings shorted), Lm (H) → ratio = Llk/Lm → pass: ratio <= 0.04 → rows 1085, 1086.

`CHECK-gapped-inductance-and-saturation`: inputs N, Ae (cm^2), la, li (cm), mu, Ipk (A), Bsat_design (G, default 2500 for 3C8-class cliff) → L = 0.4*pi*N^2*Ae*1e-9/(la + li/mu); Bpk = 0.4*pi*N*Ipk/(la + li/mu) → pass: Bpk <= Bsat_design → margin = Bsat_design/Bpk - 1 → rows 1112-1114, 1182.

`CHECK-mpp-swing`: inputs N, Ipk, lm (cm), mu → H = 0.4*pi*N*Ipk/lm (Oe) → pass: H <= H10 where H10 = 170 (mu14), 95 (mu26), 39 (mu60), 19 (mu125) Oe (10% inductance falloff) → margin = H10/H - 1 → rows 1185-1188, table T6.

`CHECK-halfbridge-blocking-cap`: inputs Ipft, fsw, Vpri_pk (V, = Vin_min/2), Cb (F) → dV = Ipft*0.4*T/Cb → pass: dV <= 0.10*Vpri_pk, Cb non-polarized → rows 1144, 1145.

`CHECK-output-choke-ccm` (isolated bucks): inputs Vout, fsw, Idc_min, topology → L_min = 0.3*Vout*T/Idc_min (single-ended forward) or 0.05*Vout*T/Idc_min (push-pull, half/full bridge, interleaved forward) → pass: L >= L_min → rows 1096, 1122, 1133.

`CHECK-rectifier-reverse-voltage` (derived): inputs Vout, Dmax at Vin_min (0.4 half-wave forward, 0.8 full-wave), Vin_max/Vin_min ratio, Vrrm → Vsec_pk(max) = (Vout + Vd)/Dmax*(Vin_max/Vin_min) ; ringing allowance up to 2x without snubber → pass: Vrrm >= Vsec_pk(max) with margin, or RC snubber fitted → rows 1132, 1214.

`CHECK-skin-and-proximity`: inputs fsw, bare wire diameter d (mils) or foil thickness, turns per layer Nl, layer width w, layers per portion p, waveform (sine/square) → S = 2837/sqrt(f) mils; for square waves S_av = mean(2837/sqrt(n*fsw)), n = 1..3 (reproduces Table 7.7 at 50-200 kHz; Table prints 13.2 mils at 25 kHz); Rac/Rdc_skin = (d/2S)^2/((d/2S)^2 - (d/2S - 1)^2) (d > 2S); X = 0.866*d*sqrt(Nl*d/w)/S; FR ~ ((2p^2 + 1)/3)*X for X > 5 (else graph) → advisory pass: X <= ~1.5 (book recommendation) and foil thickness ~1.37*S at fundamental; FR feeds copper loss → rows 1307-1316.

`CHECK-transformer-temp-rise`: inputs Pv (mW/cm^3 at Bpk, f, 100 C; x0.5 unipolar), Ve (cm^3), winding Irms and Rdc and FR per winding, outer dimensions w, h, t (in) → Pcore = Pv*Ve/1000; Pcu = sum(Irms^2*Rdc*FR); A = 2*(w*h + w*t + h*t); dT_surface = 80*A^-0.70*(Pcore + Pcu)^0.85; dT_hot = dT_surface + 10..15 → pass: dT_hot <= dT_allowed (K.B.: designs typically start from 30 C rise) → margin = dT_allowed - dT_hot → rows 1069, 1277-1279, 1304-1306.

`CHECK-current-mode-slope-comp`: inputs Dmax, Ns/Np, Ri (ohm), Vout, Lo (H), Se_added (V/s at sense node) → Se_req = (Ns/Np)*Ri*(Vout/Lo)/2 → pass: Dmax < 0.5 OR Se_added >= Se_req (also avoid peak/average error on line steps) → margin = Se_added/Se_req - 1 → rows 1206-1209.

`CHECK-buck-turn-on-snubber`: inputs V1_max, IL, tr (s), Vrating_target, Toff_min, fsw → L2 = V1_max*tr/IL; Rc_max = (Vrating_target - V1_max)/IL; t95 = 3*L2/Rc; P_Rc = 0.5*L2*IL^2*fsw → pass: t95 <= Toff_min AND P_Rc within resistor rating → rows 1224-1227.

`CHECK-min-on-time`: inputs Ton_max (at Vin_min), Vin_min, Vin_max, t_min_device (bipolar storage 0.5-1 us, or controller minimum on-time) → Ton_min = Ton_max*Vin_min/Vin_max → pass: Ton_min > t_min_device → rows 1190, 1236-1239.

`CHECK-audible-and-resonant-commutation`: inputs fsw_min (or minimum trigger frequency), td_min (anti-parallel diode conduction at max load, min line), tq_max (SCR) → pass: fsw_min >= 20 kHz AND td_min > tq_max (worst tq = typical +20%) → rows 1243, 1247, 1252.

`CHECK-push-pull-flux-balance` (from captured waveform): inputs centre-tap current waveform samples over >= 2 periods → r = max(peak_A, peak_B)/min(peak_A, peak_B); concavity = sign of second derivative of each ramp near its end → pass: r <= 1.2 AND no upward concavity (repeat with 1 V diode in series with each half) → rows 1063, 1064.

## 4. Verification procedures & plots

| Property | Plot / test (x vs y) | Sweep / corners | What good looks like / pass | Setup notes | Source |
|---|---|---|---|---|---|
| CCM/DCM transition (buck, boost, flyback) | switch (or choke) current vs time, one trace per load step | Iout from nominal down below Io_crit; Vin min/nom/max | ramp-on-step becomes triangle at Io_crit = dI/2; on-time constant above Io_crit, collapses below; loop stable across both | current probe in switch/choke; Fig 1.6 shows 25 kHz, 20 V -> 5 V, 5 A -> 0.2 A, critical at 0.95 A | p.22-23 Fig 1.6 |
| Switch-node ringing in DCM | V(switch node) vs time | lightest loads (deep DCM) | ring after inductor runs dry is damped quickly by RC snubber across freewheel diode | Fig 1.7b | p.24 Fig 1.7 |
| Switching-loss measurement (preferred method) | device case temperature vs time -> steady state; then equivalent DC power for the same temperature rise | max load, max line, final snubbers/drive fitted | measured loss (DC-equivalent) within thermal budget; tune drive/snubber for minimum rise | replace AC operation by DC current through the device to reproduce the temperature; direct loss from DC V*I | p.17 After Pressman (K.B.) |
| Efficiency vs load and line | efficiency (%) vs Iout, family of curves for Vin min/nom/max | 10-110% load | at or above spec; lies between Eq 1.4 (best-case) and Eq 1.7 (worst-case) estimates | - | p.16-20 |
| Output ripple and spikes | Vout AC-coupled vs time over several periods, full bandwidth; also fundamental p-p | max load, Vin max (largest dI) | ESR component ~ dI*ESR dominates; flyback thin turn-off spike (< 0.5 us) measured and removed by LC post-filter; spec includes spike, not only RMS/fundamental | probe tip-and-barrel at capacitor; typical bad flyback: 50 mV p-p with 1 V spike | p.28-30; p.135; p.145-146 |
| Push-pull flux balance | transformer centre-tap current vs time (>= 2 periods) | all line/load corners, hot; repeat with a ~1 V silicon diode in series with one half-primary, then the other; then two diodes | alternate peaks within 20%, ramps linear with no upward concavity; one inserted diode must not produce concavity | current probe in centre tap (Fig 2.4d) | p.53-56 Fig 2.4 |
| Leakage inductance | inductance of each winding with all other windings shorted | at operating frequency | Llk <= 4% of magnetizing inductance | LCR meter | p.67 Tip |
| Magnetizing current | primary current with secondaries open (or ramp slope difference) | Vin min, Ton max | peak magnetizing current <= 10% of reflected load current; linear ramp (no saturation curvature) | - | p.55; p.88 |
| Switch voltage stress | Vds/Vce vs time around turn-off | Vin max, max load, transient line step (+15%, or spec transient e.g. MIL-STD-704) | peak including leakage spike below derated rating (flyback: ~30% margin; push-pull/forward: <= 2.6 Vdc(max) assumed) | - | p.67; p.72; p.130 |
| Rectifier reverse-voltage ring | diode cathode voltage vs time at commutation | max line, max load | first ring peak below Vrrm with margin; if ring ~2x steady reverse voltage add series-RC snubber | - | p.186-187 |
| Flyback DCM margin | primary and secondary current vs time | Vin min, Pout max (and over-load limit) | secondary current reaches zero with dead time >= 0.2T before next turn-on; no front-end step on primary current | waveform set of Fig 6.29 (threshold at 38 V, dead time at 50/60 V) | p.130-131; p.278-280 |
| Loop stability (Bode) | loop gain magnitude (dB) and phase (deg) vs log frequency | line/load corners, both sides of CCM/DCM boundary | voltage mode: LC double pole (-40 dB/dec, up to 180 deg) compensated; current mode: -20 dB/dec, <= 90 deg from power stage; CCM boost/flyback: crossover far below RHP zero | injection at error-amplifier input | p.36-37; p.164; p.172-175 |
| Current-mode subharmonic stability | switch current vs time (look for alternate-cycle amplitude) | D > 0.5, line steps | no period-doubling; average current independent of on-time after slope compensation | step Vin and observe settling | p.176-181 Fig 5.5-5.6 |
| Load-step transient | Vout vs time for load step | min->max load, both modes | returns without sustained oscillation; DCM flyback responds faster (no RHPZ) than CCM | - | p.126-129; p.154 |
| Cross regulation | slave Vout vs master and slave load | min..max loads on each output | +/-5..8% with CCM output chokes; ~+/-2% for choke-less (peak-rectified, flyback, current-fed) designs; all chokes CCM above their Imin | - | p.48-50; p.190; p.216 |
| Transformer temperature rise | surface and hot-spot temperature vs time to steady state | max load, max line (core loss) and min line (copper loss), max ambient | rise <= design value (typ 30 C); prediction dT = 80 A^-0.7 P^0.85 within ~10 C; hot spot 10-15 C above surface | thermocouple on centre leg / winding surface | p.59; p.315-320 |
| Winding AC resistance | Rac vs frequency per winding | fsw to ~5*fsw | Rac/Rdc consistent with skin (Eq 7.21) and Dowell prediction for the layer arrangement; interleaving reduces it | impedance analyzer, other windings shorted as in operation | p.323-336 |
| SCR commutation margin | SCR and anti-parallel diode currents vs time | max load, min line | diode conduction time td > worst-case tq (typ +20%); resonant half period ~8-10 us for low turn-on loss | - | p.243-245 |
| Royer end-of-on-time spike | collector current vs time | 38-60 V input | no 3-5x current spike when current-fed (series inductor) and cross-coupled 100-500 pF caps fitted | - | p.268-273 Fig 6.22-6.24 |

## 5. Pitfalls, failure modes, review checklist

- [ ] Linear regulator headroom verified at the ripple trough at minimum AC line, not at average DC (>= 2.5 V NPN, < 0.5 V PNP knee) — p.5, p.8
- [ ] Linear regulator dissipation computed at MAXIMUM line, where efficiency is worst — p.6-7
- [ ] Buck/boost: CCM/DCM boundary current located in the load range and the loop compensated for BOTH transfer functions — p.22-24, p.35-37
- [ ] Buck in DCM: switch-node ringing (Lo with node capacitance) damped by RC snubber across freewheel diode — p.24
- [ ] Choke saturation current >= nominal load + half ripple (>= 1.1 Ion for 20% ripple) at max temperature — p.26-27
- [ ] Output-cap ESR from datasheet at fsw; if unknown, aluminium electrolytic RoCo = 50-80 us — p.28
- [ ] Auxiliary winding on buck choke: main output must carry a minimum load (D1 must stay conducting); do not power the controller from it (may not start) — p.31 Tip
- [ ] Boost: core volt-seconds reset each cycle (Vdc*Ton = (Vo - Vdc)*Tr), else core walks up the B-H loop, saturates, and the transistor is destroyed — p.37-38, Fig 1.12
- [ ] Boost/flyback in CCM: RHP zero; no compensation network removes it — slow the loop — p.36-37
- [ ] DCM boost/inverter: Ton(max) or peak current limited so overload / low line cannot push into CCM — p.39
- [ ] Push-pull: Ton(max) clamp <= 80% of half period at Vdc(min) (core reset + no simultaneous conduction with bipolar storage time) — p.60
- [ ] Push-pull flux imbalance: centre-tap current ramps show no upward concavity and alternate peaks within 20% at all corners, incl. hot — p.55
- [ ] Push-pull: sudden load transients can saturate an already-offset core — p.55 Note
- [ ] Transformer turns sized for transient: 50% line step during error-amp delay must not saturate (use dB = 3200 G, not 4000 G) — p.62-63
- [ ] Leakage inductance measured (others shorted) and <= 4% of magnetizing inductance — p.67
- [ ] Single-ended forward/push-pull switch rating >= 2.6*Vdc(max) plus >= 15% transient margin — p.67, p.72, p.83
- [ ] Forward: catch diode + reset winding present; without it the switch avalanches at turn-off — p.77
- [ ] Forward: magnetizing current <= 10% of primary load current (gap trade-off) — p.88
- [ ] Multi-output master/slave: every output choke continuous at its own minimum load, else slaves collapse or rise — p.49-50
- [ ] Gapping: prefer centre-leg ground gap (stable, less radiated field/RFI) over shims in production — p.57
- [ ] Off-line 220 VAC: never single-ended forward or push-pull; use two-switch forward/half/full bridge — p.96
- [ ] High-voltage outputs (> ~200 V) with single forward: freewheel diode sees Vo/0.4; slow-recovery diode runs hot — p.100
- [ ] Half bridge: series non-polarized DC-blocking capacitor present; primary droop <= 10% — p.107-108
- [ ] Half bridge / doubler: equal bleeder resistors across the series bulk capacitors — p.105
- [ ] Universal doubler link/switch: guard against 220 VAC on the 120 V (doubler) setting (auto-sensing relay) — destroys switch, rectifiers, capacitors — p.105, p.147
- [ ] Bridge legs: hard on-time clamp <= 0.8*T/2 or adaptive dead time; shoot-through destroys the leg instantly — p.105-106, p.113
- [ ] Full bridge: blocking capacitor still fitted (unequal storage times / Rds(on) between diagonal pairs) — p.115
- [ ] Flyback secondary never left open-circuit (ampere-turns conserved -> destructive voltage) — p.119
- [ ] Flyback: turns ratio chosen so Vdc(max) + reflected voltage + 0.3*Vdc spike stays ~30% below switch rating — p.130
- [ ] Flyback designed DCM: 20% dead time at Vdc(min)/Ro(min) AND on-time/peak-current limit so overload cannot push into CCM (loop not compensated for RHP zero) — p.130-131
- [ ] Flyback output: thin turn-off spike (Ip*Np/Ns*ESR, < 0.5 us) measured with full-bandwidth probe, not just RMS/p-p fundamental; LC post-filter fitted; sense before the post-filter — p.145-146
- [ ] Flyback output capacitor ripple-current rating >= ~0.89*Idc — p.146
- [ ] Flyback secondary copper: paralleled strands/foil (e.g. 21 A RMS needs 10,500 CM) — p.134
- [ ] Flyback core gapped (or MPP) — ungapped ferrite saturates immediately — p.136
- [ ] MPP choke: inductance swing at Ipk <= 10% (mu <= 125 typical for >= 1 A bias) and turns fit core ID at 500 CM/A — p.139, p.145
- [ ] Universal-input flyback with bipolars: minimum on-time at high line exceeds storage time (fsw <= ~100 kHz) — p.148
- [ ] Two-switch flyback: reflected voltage ~2/3 Vdc(min) so leakage energy resets quickly — p.160
- [ ] Peak-current mode above D = 0.5 (or wide duty range): slope compensation >= (Ns/Np)*Ri*(Vo/Lo)/2 present, else subharmonic oscillation — p.176-181
- [ ] Current-sense path: non-inductive sense resistor, short layout; with large Lo the ramp is nearly flat at turn-off and noise causes jitter — p.183
- [ ] Current-mode small-signal simplification does not apply to large transients: output choke still limits slew when the EA saturates — p.174 After Pressman
- [ ] Hard-switched secondaries: output rectifier recovery ring measured; RC snubbers across rectifiers if peak exceeds rating (ring can double reverse stress) — p.186-187
- [ ] Bridge turn-on current overshoot Vcc*trr/Ll checked against switch pulse rating; ultrafast rectifiers (35 ns) preferred over fast (200 ns) — p.186
- [ ] Voltage-fed bridges: storage-time growth at high temperature/low line cannot erode dead time into shoot-through (on-time clamp + UVLO) — p.193, p.198
- [ ] Buck preregulator: turn-on snubber inductor recharges within the off time (3*L2/Rc < Toff) and Rc keeps V1 + Rc*IL below the switch rating — p.202-203
- [ ] Current-fed bridge: upper Zener clamp on the bridge input node fitted (slower transistor turn-off overshoot) — p.197
- [ ] Weinberg: N2 >= 2x the minimum that keeps D3 reverse biased in overlap mode; transistor rating >= Vdc(max) + (N1 + N2)(Vo + Vd) + spike — p.222, p.226
- [ ] SCR resonant: anti-parallel-diode conduction time at max load and min line exceeds worst-case tq (typ +20%) — p.243-245
- [ ] Series-loaded resonant converters: define behaviour at open-circuit load (Q collapse, commutation failure); gap transformer — p.240, p.250
- [ ] Variable-frequency converters: minimum switching/trigger frequency stays above ~20 kHz at light load — p.230, p.252
- [ ] Housekeeping supply: controller powered from an always-present source; bootstrap-only designs checked for shutdown race to maximum pulse width — p.261
- [ ] Royer: square-loop core (not standard ferrite), current-fed series inductor, 100-500 pF cross-coupling caps; tape cores < 1 W loss unless heat-sunk — p.269-277
- [ ] Core-loss data taken from bipolar (datasheet) curves de-rated correctly for unipolar forward/flyback use (book: x0.5 at same Bpk) — p.287-289
- [ ] Core loss evaluated at 100 C data and at the actual Bpk AND f (Pv ~ B^2.7 f^1.6-1.7) — p.294, p.314
- [ ] Transformer flux design point <= 1600 G below 50 kHz even when core loss would permit more (transient/EA-delay saturation margin; hard saturation > 3200 G at 100 C) — p.294-295
- [ ] Tabulated core power (Table 7.2) only valid if temperature rise at 1600 G is acceptable; large cores above 50 kHz need 800-1400 G — p.314
- [ ] Temperature rise estimated from total loss and total radiating area (dT = 80 A^-0.7 P^0.85) plus 10-15 C hot-spot allowance — p.315-319
- [ ] Gapped cores bought centre-leg gapped (no shims, no outer-leg gap) for reproducible AL and lower EMI — p.293
- [ ] Pot cores not used for high-voltage windings (lead-exit notch arcing) or many heavy leads — p.292
- [ ] Wire gauge checked against skin depth at the harmonic-weighted average (square-wave currents), not just the fundamental — p.327-330
- [ ] Multilayer windings checked with Dowell FR (layers per portion); interleave or use thinner conductors (X ~ 1.5) where FR is large — p.333-336
- [ ] Push-pull interleaving order: conducting half-primary adjacent to its conducting half-secondary — p.336
- [ ] Flyback: do not rely on interleaving to cut proximity loss; minimize layers — p.336
- [ ] Litz wire: every strand terminated at both ends; not used at <= 50 kHz where parallel strands suffice — p.327
- [ ] Foil secondary (> 15-20 A) thickness ~1.37 x skin depth at the fundamental — p.327
- [ ] Safety (VDE) creepage margins and interlayer insulation included in window fill (SF 0.4) — p.296

## 6. Standards referenced

| Standard | Edition/clause | What it governs (as used in the book) | Page |
|---|---|---|---|
| MIL-STD-704 (Military Standard 704) | not given | Military aircraft electric power: nominal 113 VAC with a 10-ms transient to 180 VAC; used to size switch off-stress (180*1.41*2.6 = 660 V for push-pull) | p.72 |
| VDE (European safety specifications) | "at this time"; no number/clause given | Transformer construction: 4-mm gap between each end of a winding layer and the bobbin ends; three layers of 1-mil insulation between layers (sandwich construction costs ~6 mils); foil width reduced for VDE margins | p.296; p.327 |
| MMPA (Magnetic Material Producers Association) publications | refs 5, 6 of Ch. 7 (not in range) | International-standard ferrite core shapes and dimensions | p.289 |
| IEC publications (via American National Standards Institute) | ref 7 of Ch. 7 (not in range) | International-standard ferrite core geometries | p.289 |
| Telephone-industry DC power (industry practice, no standard number) | - | 48 V nominal, 38 V minimum, 60 V maximum input range used throughout examples | p.71; p.83 |

## 7. Process / lifecycle guidance

The book is a design text, not a product-lifecycle text. The converter design sequence it prescribes (chapters 1-7) is recorded here because Anvil can gate on it.

| Stage | Activity | Deliverable | Exit criterion | Source |
|---|---|---|---|---|
| 1 Topology election | compare switch off-stress (1x vs 2.6x Vdc), peak current (1.56 vs 3.13 Po/Vdc), power range, isolation/outputs, RFI | chosen topology with stress numbers | Vstress and Ipft within affordable devices; 220 VAC input -> bridge or two-switch forward | p.3-4; p.71-72; p.83-84; p.96; p.111; §7.1 |
| 2 Frequency and core | select fsw and core from Tables 7.2a/b (Bmax 1600 G, 500 CM/A), or K.B. nomogram / area product | core part number, fsw | Pcore >= Pout and predicted rise acceptable at chosen Bmax | p.285-286; p.306-314 |
| 3 Turns | Ton(max) = 0.8T/2 at Vdc(min); Np from Faraday; secondaries from output equations | turns table | Bpk <= design limit incl. 1.5x transient step | p.60-63; p.90-91 |
| 4 Currents and wire | Ipft, RMS per winding; 500 CM/A (>= 300); skin/proximity check; layer order/interleave | winding spec | Dcma >= 300; Dowell X ~ 1.5 at high fsw | p.63-67; p.91-93; p.320-336 |
| 5 Losses and temperature | core loss (Table 7.1), copper loss (Rdc x FR), switch conduction and overlap loss | loss budget | transformer rise <= target (typ 30 C); efficiency >= spec | p.16-20; p.69-71; p.315-320 |
| 6 Output filter | L for CCM at Imin (Eq 1.8/2.20/2.47), C from ESR for ripple | L, C part numbers | ripple and CCM checks pass | p.26-30; p.73-75; p.93-94 |
| 7 Protection and snubbers | on-time clamp/dead time, current limit, leakage-spike snubbers, turn-on snubbers | schematic | measured stresses within derated ratings | p.60; p.67-68; p.198-204 |
| 8 Loop | compensate for LC double pole or current-mode single pole; RHPZ roll-off for CCM boost/flyback; slope compensation | compensation network | Bode margins at all corners incl. CCM/DCM transition | p.36-37; p.164; p.176-183 |
| 9 Bench verification | Section 4 tests (flux balance, stresses, ripple, thermal) | test report | all pass criteria met | Section 4 |

## 8. Coverage log

- **Line ranges read (in order, Read tool, chunks sized to the long OCR lines):** 1-130, 131-250, 251-400 (front matter, contents, preface; Ch. 1 starts at line 296), 400-700, 700-1100, 1100-1440 (Ch. 1), 1440-1640, 1640-1800, 1800-2100, 2100-2430, 2430-2800 (Ch. 2), 2799-3068 (Ch. 3), 3069-3269, 3269-3689, 3689-4089, 4089-4334 (Ch. 4), 4334-4593, 4593-5013, 5013-5143, 5143-5303, 5303-5602, 5602-5802 (Ch. 5), 5802-6001, 6001-6521, 6521-6720, 6720-6874 (Ch. 6), 6874-7113, 7113-7443, 7443-7773, 7773-8102, 8102-8422, 8422-8701, 8701-9010 (Ch. 7 to §7.6.1). Lines 9001-9010 were read only for boundary context; only the area-product definition was taken from them.
- **Skipped (no rules):** copyright/terms, author biographies, acknowledgments, preface narrative, chapter reference lists (cited where used), historical remarks (Royer 1955, SCR history). No exercises exist in this range.
- **Rule count:** 322 design rules, ids PRESSMAN-1001 to PRESSMAN-1322 (a 4-digit 1xxx block for part 1 so the part-2 extraction cannot collide). 21 tables (T1-T21), 31 mechanizable checks.
- **Special-focus coverage within this range:** duty-cycle/transfer relations for buck, boost, inverting, push-pull, forward (incl. unequal reset turns), two-switch forward, interleaved forward, half/full bridge, flyback DCM/CCM, current-fed/Weinberg, Cuk, SCR resonant; inductor/transformer design equations with the author's constants (1.56/3.13/0.986/1.97/2.79/1.40 x Po/Vdc, 493/985/1395/700 CM, L = 5(Vdc-Vo)VoT/(VdcIon), 0.5VoT/Ion, 3VoT/Ion); RoCo = 50-80e-6 (65e-6 typical); DCM boundaries; switch stresses (2.6 Vdc, 1.3 x 2Vdc, flyback 30% margin); snubbers (buck turn-on L2 = V1 tr/IL, Rc, lossless transformer snubber — RCD turn-off snubber design is Ch. 11, part 2); core selection (Eq 7.7/7.13/7.18, Tables 7.2a/b, AP definition); flux limits (1600 G design, 2000 G linear, 3200 G saturation, 1400-800 G above 50 kHz, 200 mT p-p K.B.); skin depth and wire sizing (2837/sqrt(f) mils, 500/300 CM per A, Litz, foil); leakage (<= 4% of Lm); gate-drive items only where they appear in Ch. 2-5 (dead time, storage time, UC1846 output drive, MOSFET current rating) — the gate-drive chapters (8, 9) are part 2.
- **Extraction limitations:**
  - OCR flattened fractions and dropped radical signs; every equation was re-derived and checked against the book's worked numbers. Restored: boost Eq 1.16 and inverting Eq 1.22 (sqrt lost), flyback Eq 4.3, forward Eq 2.32 (printed garbled; Ton = 0.8T/(1 + Nr/Np)), Eq 4.7, Eq 5.5, Eq 6.8, Eq 7.7, Eq 7.21.
  - Printed errata preserved and flagged: forward off-line example prints "3.13 x 22/150" (200 W intended, p.83); push-pull secondary copper prints "3.16Idc" (500 x 0.632 = 316 Idc, p.67); buck turn-on snubber example prints T = 2 us (20 us) and a 7.9/6.4 time constant alongside Rc = 9.6 ohm (p.203); Table 7.2a pot 3622 Ae printed 2.20 (2.02 in Table 7.2b and by AeAb); Table 7.2b "6254" (625.4) and "136.2" (~1360); Table 4.1 mu125 row does not fully follow its own Lmax formula; Table 5.2 Irms values follow a one-T1-per-period weighting that disagrees with the prose; Table 7.6 vs prose (AWG 14 at 25 kHz 1.30 vs 1.25; at 200 kHz 2.90 vs 3.3).
  - Table 7.1 (core loss vs f and B) is badly scrambled in the text: 100 kHz and 200 kHz rows reproduced; 500 kHz/1 MHz values given without flux-column alignment; 20 and 50 kHz blocks not reproducible (one probable 3C8 row). Tables 4.2, 4.3 and 7.3 were re-assembled from scrambled OCR and cross-checked (Tables 4.2/4.3 via Lmax = 0.9*AL*(N/1000)^2).
  - Figures are absent: graph-only data (Fig 1.2, 2.3, 4.3, 4.5, 6.5-6.7, 7.1, 7.4, 7.6, 7.9) are captured only through the numeric anchors the prose gives, marked as graph-derived where used.
  - Units follow the book: CGS magnetics (gauss, oersted, cm, cm^2) with 1e8/1e-8 factors; K.B.'s SI form (us, tesla, mm^2) given where he states it. Several device-specific data (SG1524, UC1846, ASCR S7310/ACR25U, MJ13330, MTH30N20) are from the 2009 text and may be obsolete.
