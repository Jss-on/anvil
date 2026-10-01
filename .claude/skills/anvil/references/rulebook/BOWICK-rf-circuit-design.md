# RF Circuit Design (Bowick, Blyler, Ajluni, 2nd ed.) — Anvil rulebook

## 0. Citation

[1] C. Bowick, J. Blyler, and C. Ajluni, *RF Circuit Design*, 2nd ed. Burlington, MA, USA: Newnes/Elsevier, 2008. ISBN-13 978-0-7506-8518-4, ISBN-10 0-7506-8518-2. LCCN 2007036371.

Chapters covered by this extraction (whole file, lines 1–13423):
- Ch.1 Components and Systems (pp.1–21): wire, skin effect, resistors, capacitors, inductors, toroids, toroidal inductor design, winding hints
- Ch.2 Resonant Circuits (pp.23–36): definitions, loaded Q, insertion loss, impedance transformation, coupling
- Ch.3 Filter Design (pp.37–62): normalized low-pass prototypes, Butterworth/Chebyshev/Bessel tables, scaling, HP/BP/BR transforms, finite-Q effects
- Ch.4 Impedance Matching (pp.63–80 of pp.63–102): L, pi, T networks, low-Q wideband networks, Smith chart construction and basic moves
- Ch.5 The Transistor at Radio Frequencies (pp.103–123): materials, equivalent circuit, Y and S parameters, data sheets
- Ch.6 Small-Signal RF Amplifier Design (pp.125–146 of pp.125–167): biasing, Y-parameter design, stability, neutralization, selective mismatch, S-parameter stability/MAG/conjugate match/transducer gain
- Ch.7 RF (Large Signal) Power Amplifiers (pp.169–183): power transistors, biasing, classes, matching, broadband transformers
- Ch.8 RF Front-End Design (pp.185–201): receiver architectures, mixers, noise, intercept points, ADC effects, SDR, CDMA case study
- Ch.9 RF Design Tools (pp.203–225): EDA flow, modelling, PCB design, packaging, 802.11a CMOS case study
- Appendix A (pp.227–228), Bibliography (pp.233–235)

Not read / not available: pp.81–102 (Ch.4 "Impedance Matching on the Smith Chart", "Software Design Tools", Summary), pp.147–167 (rest of Ch.6: stability circles, design for specified gain, design for optimum noise figure) and pp.229–232 (Appendix B, vector algebra) are absent from the source text file. The index (pp.237 on) was skipped per the brief. Figure-only pages (toroid data sheets Figs. 1-25/1-26, Smith-chart graphics, the 2N5179 and MRF233 data sheets) are not in the extraction; prose readings of them are used where given.

Notation: all formulas in plain ASCII. `log` = log10, `ln` = natural log, `sqrt` = square root, `||` = parallel combination, `|x|` = magnitude, `w` = omega = 2*pi*f, `a/b deg` in S-parameter values = magnitude a at angle b degrees. Inside markdown tables literal pipes are escaped (`\|\|` = parallel, `\|S21\|` = magnitude). Printed page numbers are cited as p.N; figure/table/equation numbers are the book's. Section 1 columns use single tokens: verify-by is the primary method; `conf` is the lowest confidence that applies, with a "conf note" in the applicability column when parts of a rule differ.

## 1. Design rules

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| BOWICK-001 | components | AWG wire diameter approximately doubles every six gauge numbers (use to interpolate Table 1-1 without the chart) | d(AWG n-6) ~= 2 * d(AWG n); anchor: AWG 50 = 1.0 mil, AWG 14 = 64 mil | AWG number | copper round wire, AWG system | calc | p.1, Example 1-1, Table 1-1 | high |
| BOWICK-002 | components | Skin depth is the depth at which current density falls to 1/e (37%) of the surface value; it depends on frequency, permeability and conductivity, so different metals (Ag, Al, Cu) have different skin depths | delta defined by J(delta) = J_surface / e | f, mu, sigma | all conductors incl. resistor/capacitor/inductor leads | calc | p.1 | high |
| BOWICK-003 | components | Copper skin depth anchors: 0.85 cm at 60 Hz and 0.007 cm (70 um) at 1 MHz; 63% of RF current in a copper wire flows within 0.007 cm of the surface at 1 MHz | delta_Cu(60 Hz) = 0.85 cm; delta_Cu(1 MHz) = 0.007 cm; general scaling delta ~ 1/sqrt(f) (derived from the two anchors: 0.85*sqrt(60/1e6) = 0.0066 cm) | f (Hz) | copper; conf note: high (anchors), medium (1/sqrt(f) scaling) | calc | p.1 | medium |
| BOWICK-004 | components | Effective conducting area of a round wire at RF is the annulus of one skin depth: A_eff = pi*(r2^2 - r1^2) with r1 = r2 - delta; AC resistance rises accordingly | A_eff = pi*(r2^2 - (r2-delta)^2) | wire radius r2 (cm), delta (cm) | round conductor, delta < r2 | calc | p.2, Fig. 1-1 | high |
| BOWICK-005 | components | Inductance of a straight round wire (self-inductance) | L_uH = 0.002 * l * (2.3*log(4*l/d) - 0.75); l = wire length (cm), d = wire diameter (cm) | l (cm), d (cm) | any lead/hookup wire; worked values: 5 cm of AWG22 (d=0.0643 cm) -> 50 nH (recomputed 49.8 nH); Example 1-3 prints 8.7 nH for 1.27 cm of AWG14 (d=0.1628 cm), but Eq. 1-1 gives 6.8 nH for those inputs (recomputed in this extraction) | calc | p.2, Eq. 1-1, Examples 1-2, 1-3 | high |
| BOWICK-006 | components | Every conductor at RF (hookup wire, capacitor leads, resistor leads) must be modeled as an inductor; budget lead inductance with Eq. 1-1 | see BOWICK-005 | lead length, diameter | all RF nets | calc | p.2 | high |
| BOWICK-007 | components | Resistor RF equivalent circuit = series lead inductance L on each lead + R + shunt parasitic capacitance C across R | Z = (R \|\| 1/(jwC)) + 2*jwL (lead L on each side) | R, L_lead (from Eq. 1-1), C_par | all resistor types | calc | p.2, Fig. 1-2 | high |
| BOWICK-008 | components | Carbon-composition resistors are poor high-frequency performers: inter-granule parasitic capacitance dominates their equivalent circuit; do not use in RF signal paths | impedance falls with f (Fig. 1-4 curve labelled Carbon Composition) | resistor type | RF paths | review | p.2, Fig. 1-4 | high |
| BOWICK-009 | components | Wirewound resistors behave as inductors at RF: impedance rises with frequency until L resonates with shunt C (peak at Fr), then falls; worst for low resistance values in 10 MHz to 200 MHz | Fr = 1/(2*pi*sqrt(L*C)); L from single-layer air-core formula Eq. 1-8 | R value, winding geometry | 10–200 MHz, low-value wirewound | calc | p.2, Fig. 1-3 | high |
| BOWICK-010 | components | Metal-film resistors have the best RF behaviour of leaded types, but impedance falls with frequency above ~10 MHz due to shunt C; for values under 50 ohm lead inductance produces a resonance peak (5 ohm curve peaks ~120% of DC) and skin effect flattens the roll-off | Z/R_dc vs f per Fig. 1-4 (1–1000 MHz axis): 5 ohm peaks >100%; 100 ohm, 1 k ~flat then down; 10 k, 100 k, 1 M fall steeply | R value, f | leaded metal-film resistors, 1 MHz–1 GHz | calc | p.3, Fig. 1-4 (graph) | medium |
| BOWICK-011 | components | Impedance of a resistor with shunt parasitic capacitance: Z = R*Xc/sqrt(R^2 + Xc^2); worked: 10 kohm with C=0.3 pF at 200 MHz (Xc = 2653 ohm) -> 2564 ohm, i.e. a 10 k resistor looks like 2.56 k; lead L (printed 8.7 nH = 10.93 ohm per lead; Eq. 1-1 actually gives 6.8 nH = 8.6 ohm) negligible versus 10 k | Zmag = R*Xc/sqrt(R^2+Xc^2), Xc = 1/(2*pi*f*C) | R, C_par (pF), f | high-value resistors at VHF/UHF | calc | p.3–4, Example 1-3, Fig. 1-5 | high |
| BOWICK-012 | components | Thin-film chip resistors (alumina or beryllia substrate) have very little parasitic reactance from DC to 2 GHz; prefer them for RF bias/pad/combiner resistors | usable DC–2 GHz | resistor technology | RF | review | p.4, Fig. 1-6 | high |
| BOWICK-013 | components | Parallel-plate capacitance | C_pF = 0.2249 * (eps/eps0) * A / d, A in in^2, d in inches; eps0 = 8.854e-12 F/m; valid only when A is large relative to d | A (in^2), d (in), k = eps/eps0 | plate capacitors, PCB pad capacitance estimates | calc | p.4, Eq. 1-2 | high |
| BOWICK-014 | materials | Dielectric constants: air 1; polystyrene 2.5; paper 4; mica 5 (mica capacitors ~6, p.7); ceramic low-K 10; ceramic high-K 100–10,000 | k values as listed | material | capacitor dielectric | calc | p.4, Fig. 1-7; p.7 | high |
| BOWICK-015 | components | Capacitor RF equivalent circuit: C in series with ESR Rs and lead/plate inductance L, with insulation resistance Rp in parallel; Rp is typically 100,000 megohm or more | Z = Rs + jwL + 1/(jwC) (Rp \|\| C for DC leakage) | C, ESR, L_lead, Rp | all capacitors | calc | p.4–5, Fig. 1-8 | high |
| BOWICK-016 | components | Capacitor power factor, ESR, dissipation factor and Q definitions | PF = cos(phi); ESR = PF*(1e6)/(w*C) with w = 2*pi*f (factor 1e6 implies C in uF); DF = ESR/Xc * 100%; Q = 1/DF = Xc/ESR; larger Q = better capacitor | PF, C, f | capacitor selection | calc | p.5 | high |
| BOWICK-017 | components | A capacitor is series-resonant at Fr = 1/(2*pi*sqrt(L*C)) where L is lead+plate inductance; above Fr it is inductive. Larger-value capacitors generally have more internal inductance, so at high frequency a 0.1 uF part can present higher impedance than a 300–330 pF part; check self-resonance for any bypass above 100 MHz (example given at 250 MHz) | Fr = 1/(2*pi*sqrt(L_ESL*C)); usable as capacitor only for f < Fr | C, ESL (from lead length via Eq. 1-1 plus body) | bypass/decoupling above 100 MHz | calc | p.5, Fig. 1-9 | high |
| BOWICK-018 | components | Every component used in a VHF-or-higher design should be characterised on a network analyzer before use | measure Z(f) | part | VHF and above | measure | p.5, Fig. 1-10 | high |
| BOWICK-019 | components | Ceramic capacitor dielectric constant ranges k = 5 to 10,000; the higher the k the worse the temperature characteristic | rule of thumb | k | ceramic capacitors | review | p.6 | high |
| BOWICK-020 | components | NPO (temperature-compensating, low-k) ceramics: TC from +150 to -4700 ppm/degC with tolerances as tight as +/-15 ppm/degC, linear TC; use for oscillator, resonant-circuit and filter capacitors | TC in [-4700, +150] ppm/degC; tol >= +/-15 ppm/degC | dielectric class | frequency-determining capacitors | review | p.6, Fig. 1-11 | high |
| BOWICK-021 | components | Moderately stable ceramics vary typically +/-15% of rated C over their temperature range, nonlinearly; use in switching circuits, avoid in resonant circuits/filters where stability matters | dC/C <= +/-15% over T range | dielectric class | -55 to +125 degC (Fig. 1-11 axis) | review | p.6, Fig. 1-11 | high |
| BOWICK-022 | components | High-K (general-purpose) ceramics vary as much as 80% in capacitance over temperature; use only for RF bypass | dC/C up to -80% | dielectric class | -55 to +125 degC | review | p.6, Fig. 1-11 | high |
| BOWICK-023 | components | RF-grade ceramic capacitors are high-Q (low ESR) with flat ribbon leads (solid silver or silver plated) or no leads (chip); chip capacitors are required above 500 MHz where lead inductance cannot be tolerated | f > 500 MHz -> chip capacitors | f | RF capacitors | review | p.6, Fig. 1-12 | high |
| BOWICK-024 | components | Mica capacitors: k ~ 6, physically large, excellent temperature stability; silvered mica typically +20 ppm/degC over -60 degC to +89 degC; NPO ceramic is usually the cheaper equivalent | TC = +20 ppm/degC, -60..+89 degC | dielectric | resonant circuits/filters when board area is not a concern | review | p.7 | high |
| BOWICK-025 | components | Metalized-film (polycarbonate, polystyrene, teflon) capacitors: available with +/-2% capacitance tolerance over full temperature range; polystyrene must not be used above +85 degC; parts larger than ceramic equivalents | tol +/-2%; T_max(polystyrene) = +85 degC | dielectric | filtering, bypass, coupling where space allows | review | p.7 | high |
| BOWICK-026 | components | Inductor RF equivalent circuit: L in series with winding resistance Rs, with distributed capacitance Cd in parallel; parallel self-resonance at Fr, above which the inductor looks capacitive; series resistance keeps impedance finite at Fr and broadens the peak | Fr = 1/(2*pi*sqrt(L*Cd)); Z_ideal parallel LC -> infinite at w^2*L*C = 1 (Eq. 1-6/1-7) | L, Cd, Rs | all inductors | calc | p.7–8, Figs. 1-14 to 1-16, Example 1-4 | high |
| BOWICK-027 | components | Microminiature fixed chip inductors (ceramic substrate, wrap-around terminations): available 0.01 uH to 1.0 mH with typical Q of 40 to 60 at 200 MHz | Q(200 MHz) = 40..60 | part class | chip inductors | review | p.8, Fig. 1-17 | high |
| BOWICK-028 | components | Inductor Q = X/Rs (reactance over series resistance); Q rises ~linearly with f at low f, flattens as skin effect grows, then falls to zero at the self-resonant frequency; operate inductors well below the Q peak/SRF | Q = w*L/Rs (Eq. 1-11); Q(Fr) = 0 | L, Rs(f), Fr | all inductors | calc | p.9, Fig. 1-18 | high |
| BOWICK-029 | components | To raise inductor Q / extend usable frequency: (1) larger wire diameter (lower AC+DC resistance), (2) space the turns (air gap lowers interwinding capacitance), (3) magnetic core (fewer turns) | qualitative design levers | geometry | air-core coils | review | p.9 | high |
| BOWICK-030 | magnetics | Single-layer air-core solenoid inductance | L_uH = 0.394 * r^2 * N^2 / (9*r + 10*l); r = coil radius (cm), l = coil length (cm), N = turns; valid for l > 0.67*r; accurate to within 1% | r, l, N | air-core single-layer coils | calc | p.9, Eq. 1-8, Fig. 1-19 | high |
| BOWICK-031 | magnetics | Optimum Q of a single-layer air-core coil occurs when coil length equals its diameter (l = 2r); then N = sqrt(29*L_uH/(0.394*r)) with r in cm | N = sqrt(29*L/(0.394*r)) at l = 2r; worked: 100 nH on 0.635 cm form (r = 0.317 cm) -> 4.8 turns, AWG18 (42.4 mil coated) is the largest wire that fits 4.8 turns in 0.635 cm | L (uH), r (cm) | air-core coil design | calc | p.9–10, Example 1-5 | high |
| BOWICK-032 | magnetics | A close-wound coil (turns touching) raises distributed capacitance and lowers SRF; either use the next-smaller AWG at the same length (small air gap, slightly lower Q) or lengthen the coil with the same wire to leave a gap (lower Q somewhat, much lower Cd) | design compromise | wire size, l | air-core coils | review | p.10 | high |
| BOWICK-033 | magnetics | Magnetic cores: advantages smaller size, higher Q (fewer turns), tunability; problems: (1) core loss can lower Q, (2) permeability falls with frequency toward that of air at the top of the range, (3) higher permeability = more temperature sensitivity, (4) permeability changes with signal level (saturation). Choose cores from manufacturer data over the operating frequency and temperature | four checks per core | core material, f, T, drive | ferrite/powdered-iron cores | review | p.11 | high |
| BOWICK-034 | magnetics | Toroids are self-shielding (flux contained in the core), eliminating shield cans that consume space and reduce Q; air-core solenoids radiate because surrounding air is part of the flux path | — | inductor form | RF inductors | review | p.12, Fig. 1-22 | high |
| BOWICK-035 | magnetics | Permeability mu = B/H (webers/ampere-turn); specify initial permeability mu_i on the linear part of the B-H curve; keep RF excitation small enough to remain linear (below Hsat/Bsat) | mu = B/H (Eq. 1-9) | core data | all magnetic cores | review | p.12, Fig. 1-23 | high |
| BOWICK-036 | magnetics | Core operating flux density must be below the published saturation flux density: Bop < Bsat | Bop_gauss = E * 1e8 / (4.44 * f * N * Ae); E = maximum rms voltage across inductor (V), f (Hz), N turns, Ae = effective core area (cm^2) | E, f, N, Ae, Bsat | toroidal/magnetic-core inductors and transformers | calc | p.12–13, Eq. 1-10 | high |
| BOWICK-037 | magnetics | Adding a core adds hysteresis + eddy-current loss (Rp in Fig. 1-24B). New Q depends on the ratio by which inductance and total loss each increase (loss x4 with L x2 halves Q); core loss usually increases with frequency, so Q must be computed from the manufacturer's curves at the operating frequency | Q_core = (Rp/N^2)/(Xp/N^2) = Rp/Xp (Eq. 1-15) | Rp/N^2, Xp/N^2 curves | magnetic-core inductors | calc | p.13, p.19, Fig. 1-24 | high |
| BOWICK-038 | magnetics | Powdered iron vs ferrite: powdered iron handles more RF power without saturation/damage and returns to mu_i after overdrive, whereas ferrite driven hard can retain magnetism permanently (permanently changed permeability); powdered iron gives higher Q at higher frequencies (narrowband/tuned circuits); ferrite (higher permeability per size) for VLF–VHF broadband and where board area must be minimised | selection rule | application | core choice | review | p.13 | high |
| BOWICK-039 | magnetics | Toroidal inductor inductance (linear region) | L_nH = 0.4*pi*N^2*mu_i*Ac*1e-2/le; N turns, mu_i initial permeability, Ac core cross-section (cm^2), le effective path length (cm) | N, mu_i, Ac, le | toroids below saturation | calc | p.19, Eq. 1-12 | high |
| BOWICK-040 | magnetics | Toroid inductance from inductance index: L_nH = N^2 * AL, N = sqrt(L_nH/AL); AL in nH/turn^2. If a vendor gives AL in uH/100 turns, divide by 10 to get nH/turn^2 (22 uH/100 t = 2.2 nH/t^2) | L = N^2*AL (Eq. 1-13); N = sqrt(L/AL) (Eq. 1-14); AL[nH/t^2] = AL[uH/100t]/10 | AL, L | toroids | calc | p.19, p.21, Example 1-6/1-7 | high |
| BOWICK-041 | magnetics | Largest wire diameter for a single-layer toroid winding: d = 2*pi*r1/(N + pi) (inches; r1 = core inner radius in inches); apply a 90% factor for insulation variation and pick the next AWG size below the result | d_max = 0.9 * 2*pi*r1/(N+pi); worked: r1 = 0.060 in, N = 10 -> 28.69 mil -> 25.82 mil -> AWG 22 | r1, N | single-layer toroids | calc | p.20, Eq. 1-15 (second), Fig. 1-27 | high |
| BOWICK-042 | magnetics | Ferrite toroid (Indiana General BBR-7403 curves): Q ~54 at 100 kHz, Q = 1 near 3 MHz, below 1 up to ~100 MHz where Q returns to ~1 — high-permeability ferrite cores are for broadband/low-Q transformers, not tuned circuits at VHF | Q(100 kHz) ~ 54; Q(3 MHz) ~ 1; Q(100 MHz) ~ 1 | core data curves | ferrite toroids | review | p.19–20, Example 1-6, Fig. 1-25 (graph) | medium |
| BOWICK-043 | magnetics | Example high-Q toroid design at 100 MHz: material No.12 (IRN-8, 50–150 MHz), T-25-12 core (OD 0.255 in) AL = 12 uH/100t = 1.2 nH/t^2 -> 300 nH needs N = sqrt(300/1.2) = 15.8 -> 16 turns; largest wire for T-25 = AWG 28; vendor Q curves show Q > 80 at 100 MHz | N = sqrt(L/AL) | L, core, material | powdered iron at VHF | calc | p.21, Example 1-7, Fig. 1-26 (graph) | high |
| BOWICK-044 | magnetics | Wind toroids with the winding covering the core except a 30–40 degree gap between the start and finish leads (Fig. 1-28A); do not bring leads across each other or across the winding — that adds lead capacitance and interwinding capacitance and lowers SRF | gap = 30..40 deg | winding layout | toroids | inspect | p.21, Fig. 1-28 | high |
| BOWICK-045 | rf | Decibel references: 0 dBm = 1 mW, 1 dBm ~= 1.259 mW; dBW relative to 1 W (10 W = 10 dBW, 1,000,000 W = 60 dBW) | P_dBm = 10*log(P_mW); P_dBW = 10*log(P_W) | P | link budgets | calc | p.23 | high |
| BOWICK-046 | filter | Bandwidth of a resonant circuit = f2 - f1 between the points 3 dB below passband (half-power bandwidth) | BW = f2 - f1 at -3 dB | response | resonant circuits/filters | sim | p.23 | high |
| BOWICK-047 | filter | Circuit (loaded) Q = center frequency / 3-dB bandwidth; higher Q = narrower bandwidth = higher selectivity. Component Q affects circuit Q, not vice versa | Q = fc/(f2 - f1) (Eq. 2-1) | fc, BW | resonant circuits | sim | p.24 | high |
| BOWICK-048 | filter | Shape factor = 60-dB bandwidth / 3-dB bandwidth; ideal = 1, values < 1 are physically impossible; smaller = steeper skirts | SF = (f4 - f3)/(f2 - f1); example 3 MHz/1.5 MHz = 2 | response | filters | sim | p.24, Figs. 2-2, 2-3 | high |
| BOWICK-049 | filter | Ultimate attenuation = final minimum stopband attenuation; out-of-band response peaks (component parasitics) reduce it — check the stopband over the full range for re-entrant peaks | measure min attenuation outside passband | response | filters | sim | p.24, Fig. 2-2 | high |
| BOWICK-050 | filter | Insertion loss = signal lost in resistive component losses when a network is inserted between generator and load (no matching function assumed), in dB; ripple = max minus min passband attenuation, in dB | IL_dB, ripple_dB | response | resonant circuits/filters | sim | p.24 | high |
| BOWICK-051 | filter | Single-reactance networks (shunt C = low-pass, shunt L = high-pass) roll off at 6 dB/octave; each additional significant reactive element adds 6 dB/octave; a parallel LC across a source gives 12 dB/octave near resonance and 6 dB/octave far from it | Vout/Vin = 20*log(Xc/(Rs+Xc)) (Eq. 2-3); 20*log(XL/(Rs+XL)) (Eq. 2-4); LC: Vout/Vin = jwL/((Rs - w^2*Rs*L*C) + jwL) (magnitudes) | Rs, L, C, f | voltage-divider filters | sim | p.24–26, Eqs. 2-2 to 2-5, Figs. 2-5, 2-6, 2-8 | high |
| BOWICK-052 | filter | Loaded Q of a parallel resonant circuit (lossless components) = Rp/Xp where Rp = Rs \|\| RL (source parallel load) and Xp = reactance of L or C at resonance (equal) | Q_L = Rp/Xp (Eq. 2-6), Rp = Rs*RL/(Rs+RL) | Rs, RL, L or C, f0 | parallel LC between source and load | calc | p.27, Eq. 2-6, Fig. 2-11 | high |
| BOWICK-053 | filter | Loaded Q depends on (1) source resistance, (2) load resistance, (3) component Q. Raising the external resistance raises Q: 0.05 uH / 25 pF with 50 ohm source Q ~= 1.1, with 1000 ohm source Q ~= 22.4 (f0 = 142.35 MHz) | Q_L proportional to Rp | Rs, RL | parallel resonant circuits | calc | p.26–27, Figs. 2-8, 2-10 | high |
| BOWICK-054 | filter | For fixed source/load resistance, maximise loaded Q by using a small inductor and large capacitor (small Xp): 50 nH/25 pF/50 ohm gives Q 1.1 while 2.5 nH/500 pF/50 ohm gives Q 22.4 at 142.35 MHz | Q_L = Rp/(w0*L) = Rp*w0*C | L, C, Rp | parallel resonant circuits (component values may become impractical) | calc | p.27–28, Fig. 2-12, 2-13 | high |
| BOWICK-055 | filter | Resonant-circuit design from required Q: Xp = Rp/Q, then L = Xp/w0 and C = 1/(w0*Xp). Worked: Rs = 150, RL = 1000 -> Rp = 130 ohm; Q = 20 at 50 MHz -> Xp = 6.5 ohm -> L = 20.7 nH, C = 489.7 pF | Xp = Rp/Q; L = Xp/(2*pi*f0); C = 1/(2*pi*f0*Xp) | Rs, RL, Q, f0 | lossless parallel LC, no matching | calc | p.28, Example 2-1 | high |
| BOWICK-056 | filter | Series-to-parallel transformation of a lossy component (valid at one frequency only): Rp = (Q^2 + 1)*Rs, Xp = Rp/Qp with Qs = Qp = component Q; for Q > 10 use Rp ~= Q^2*Rs and Xp ~= Xs | Eqs. 2-7 to 2-10; worked: 50 nH with Rs = 10 ohm at 100 MHz: Q = 3.14, Rp = 108.7 ohm, Xp = 34.62 ohm -> Lp = 55.1 nH | Rs, Xs, f | lossy L or C in resonant circuits | calc | p.28, Eqs. 2-7..2-10, Example 2-2, Fig. 2-15 | high |
| BOWICK-057 | filter | Component loss appears as a shunt resistor Rp across the resonant circuit and lowers loaded Q / widens bandwidth; usually only the inductor Q must be included (capacitor Q is high enough that its shunt Rp can be neglected — verify) | Q_L = (Rs \|\| RL \|\| Rp_L \|\| Rp_C)/Xp | component Qs | high-selectivity designs | calc | p.28 | high |
| BOWICK-058 | filter | Insertion loss from finite inductor Q: worked case Rs = RL = 1000 ohm, 0.05 uH (Q = 10) with 25 pF (Q = inf) at resonance gives Rp_L = 4.5 k across the load, V1 = 0.45*Vin instead of 0.5*Vin -> 0.9 dB insertion loss | IL_dB = 20*log[(Rp\|\|RL)/(Rs + Rp\|\|RL)] - 20*log[RL/(Rs+RL)] | Rs, RL, Q_L component, Xp | resonant circuits | calc | p.29, Fig. 2-16 | high |
| BOWICK-059 | filter | Resonant-circuit design with lossy inductor (Example 2-3): required Q = fc/BW; inductor shunt Rp = Q_L*Xp; loaded Q = (Rp \|\| Rs \|\| RL)/Xp — solve the two equations for Xp and Rp, then L = Xp/w0, C = 1/(w0*Xp). Worked: BW 10 MHz at 100 MHz, Rs = RL = 1000 ohm, Q_L = 85 -> Q = 10, Xp = 44.1 ohm, Rp = 3.75 k, L = 70 nH, C = 36 pF; insertion loss 20*log(0.44/0.5) = 1.1 dB | Q = (Rp\|\|Rs\|\|RL)/Xp with Rp = Q_L*Xp | fc, BW, Rs, RL, Q_L(inductor) | parallel LC bandpass, lossless C | calc | p.30, Example 2-3, Fig. 2-17 | high |
| BOWICK-060 | filter | Insertion loss of a parallel resonant circuit at f0 = 20*log[(Rp\|\|RL)/(Rs + Rp\|\|RL)] - 20*log[RL/(Rs+RL)] (dB); small per-stage IL (0.9–1.1 dB) accumulates quickly when resonators are cascaded | IL_dB formula | Rs, RL, Rp | resonant circuits/filters | calc | p.29–30 | high |
| BOWICK-061 | matching | Tapped-C impedance transformer: the resonant circuit sees Rs' = Rs*(1 + C1/C2)^2; the total capacitance resonating with L is CT = C1*C2/(C1 + C2). Use when the required loaded Q > 10 with low source/load resistances (otherwise L becomes impractically small or negative) | Rs' = Rs*(1 + C1/C2)^2 (Eq. 2-13); CT = C1*C2/(C1+C2) (Eq. 2-14); C1/C2 = sqrt(Rs'/Rs) - 1 | Rs, Rs', CT | tapped-C resonators; also provides a DC block | calc | p.30–31, Fig. 2-18A, Example 2-4 | high |
| BOWICK-062 | matching | Tapped-L impedance transformer: Rs' = Rs*(n/n1)^2 where n = total turns and n1 = turns from the tap to ground (text superscript garbled in extraction; formula per Fig. 2-18B) | Rs' = Rs*(n/n1)^2 (Eq. 2-15) | Rs, n, n1 | tapped inductor resonators | calc | p.31, Eq. 2-15, Fig. 2-18B | medium |
| BOWICK-063 | filter | Worked tapped-C design (Example 2-4): Q = 20 at 100 MHz, Rs = 50 ohm, RL = 2000 ohm, Q_L = 100 -> transform Rs to 2000 ohm (C1 = 5.3*C2); Rp = 100*Xp; Q = 1000*Rp/((1000+Rp)*Xp) = 20 -> Xp = 40 ohm, Rp = 4000 ohm, L = 63.6 nH, CT = 39.78 pF -> C2 = 47.3 pF, C1 = 250.6 pF | as BOWICK-059/061 | Q, f0, Rs, RL, Q_L | tapped-C bandpass | calc | p.31, Example 2-4, Fig. 2-18D | high |
| BOWICK-064 | filter | Critical coupling of two identical resonators: coupling element too large -> double-humped, broadened passband (overcoupled); too small -> excessive insertion loss (undercoupled); critical coupling gives lowest IL and maximum power transfer | choose C12 or L12 per BOWICK-066 | coupling value | two-resonator coupled filters | sim | p.32, Fig. 2-20 | high |
| BOWICK-065 | filter | Loaded Q of a critically coupled two-resonator filter ~= 0.707 x the loaded Q of one resonator (3-dB bandwidth is wider than a single resonator's, but skirts are steeper and shape factor smaller); design each resonator for Q_R = Q_total/0.707 | Q_total = 0.707*Q_R; Q_R = Q_total/0.707 | Q_total | two-resonator capacitively or inductively coupled filters | calc | p.32, Fig. 2-21, Example 2-5 | high |
| BOWICK-066 | filter | Coupling element values for two identical resonators at critical coupling: top-C C12 = C/Q; top-L L12 = Q*L (C, L = resonator values, Q = loaded Q of a single resonator). X(C12) = X(L12) at the same Q and f0, so a top-C design converts to top-L by substituting an inductor of equal reactance without changing coupling, Q or f0 | C12 = C/Q (Eq. 2-19); L12 = Q*L (Eq. 2-20) | C, L, Q | coupled resonators | calc | p.32–34, Eqs. 2-19, 2-20 | high |
| BOWICK-067 | filter | Capacitively (top-C) coupled two-resonator response is skewed: 18 dB/octave below resonance, 6 dB/octave above; inductively (top-L/transformer) coupled is the mirror image: 6 dB/octave below, 18 dB/octave above. Use top-C to meet ultimate-attenuation specs below the passband, top-L for specs above; mix a top-L section with top-C to symmetrise the response | slope asymmetry 18/6 dB/octave | coupling type | two-resonator filters | sim | p.33–34, Figs. 2-20, 2-22, 2-24, 2-25 | high |
| BOWICK-068 | magnetics | Transformer coupling has no exact design procedure (geometry, spacing, core, shielding all matter): (1) decreasing primary–secondary spacing increases coupling, (2) increasing magnetic-path permeability increases coupling, (3) shielding decreases loaded Q and increases coupling. Procedure: set each resonator's loaded Q to ~2x the final requirement, then reduce spacing until the response broadens to the needed Q; document every iteration; check commercial transformers first | start Q_R ~= 2*Q_needed | winding geometry | transformer-coupled resonators | measure | p.34 | medium |
| BOWICK-069 | filter | Active (unilateral transistor) coupling of n identical tuned circuits each of loaded Q: Q_total = Q/sqrt(2^(1/n) - 1); e.g. n = 4, Q_total = 50 requires only Q ~= 22 per resonator | Q_total = Q/sqrt(2^(1/n) - 1) (Eq. 2-21); Q = Q_total*sqrt(2^(1/n) - 1) | n, Q_total | cascaded actively isolated resonators | calc | p.34, Eq. 2-21 | high |
| BOWICK-070 | filter | Worked top-L coupled two-resonator design (Example 2-5): f0 = 75 MHz, BW = 3.75 MHz, Rs = 100 ohm, RL = 1000 ohm, inductor Q_u = 85, tapped-C source transform to 1000 ohm: Q_total = 20 -> Q_R = 28.3; Rp = 85*Xp; Xp = 1000*Rp/((1000+Rp)*28.3) -> Xp = 23.57 ohm, Rp = 2003 ohm; L1 = L2 = 50 nH, C_res = 90 pF; C1/C2 = sqrt(1000/100) - 1 = 2.16 -> C2 = 132 pF, C1 = 285 pF; L12 = Q_R*L = 28.3*50 nH = 1.415 uH | chain of BOWICK-065, 059, 061, 066 | specs | two-resonator top-L filter | calc | p.35–36, Example 2-5, Fig. 2-27 | high |
| BOWICK-071 | filter | Filter order n = number of significant reactive elements; final stopband slope = 6*n dB/octave (2nd order 12 dB/octave, 3rd order 18 dB/octave) | slope = 6*n dB/octave | n | LC ladder filters | sim | p.38–39 | high |
| BOWICK-072 | filter | Two-element (series L, shunt C) low-pass: peak occurs at Fr = 1/(2*pi*sqrt(L*C)) if loaded Q is high enough; Q1 = XL/Rs, Q2 = RL/Xc, Q_total = Q1*Q2/(Q1+Q2). If Q_total > ~0.5, set Q1 = Q2 for optimum power transfer (response approaches 0 dB IL at the peak); if Q_total < ~0.5 there is no peak and set Rs = RL | Eqs. 3-1 to 3-4 | L, C, Rs, RL | 2-pole LC low-pass | calc | p.38, Fig. 3-2, 3-3 | high |
| BOWICK-073 | filter | Number of passband response peaks (ripple peaks) = N - 1 for an N-element ladder (only when loaded Q > 1). Odd-order networks: 0 dB at DC and at the upper passband edge with dips between; even-order networks: insertion loss at DC equals the passband ripple in dB | peaks = N - 1 | N | LC ladder filters | sim | p.38–39, Figs. 3-5, 3-6 | high |
| BOWICK-074 | filter | Optimum passband flatness of a three-element low-pass occurs at loaded Q = 1; Q < 1 rolls off within the passband (worse selectivity AND worse passband IL); Q > 1 adds ripple but steeper initial skirt. Trading ripple for bandwidth: less ripple -> wider bandwidth, less selectivity | Q_L = 1 for flattest 3-element response | Q_L | 3-element LC low-pass | sim | p.39, Fig. 3-6 | high |
| BOWICK-075 | filter | Terminating the filter with source/load resistances other than the design values changes its Q, passband ripple and shape factor in proportion to the termination error — verify with the actual Rs and RL | response sensitivity to Rs, RL | Rs, RL | all LC filters | sim | p.39 | high |
| BOWICK-076 | filter | Normalization convention for all low-pass prototypes: cutoff wc = 1 rad/s (0.159 Hz), load = 1 ohm (source = 1 ohm for equal-termination tables); capacitors in farads, inductors in henries; scale to final frequency/impedance afterwards | wc = 1 rad/s, RL = 1 ohm | prototype | filter catalog | calc | p.40, p.41 | high |
| BOWICK-077 | filter | Butterworth (maximally flat, no ripple, medium-Q) attenuation: A_dB = 10*log[1 + (w/wc)^(2n)], wc = 3-dB cutoff, n = number of elements. Anchors: n = 5 gives ~30 dB at 2*fc; at f/fc = 3, n = 6 gives ~57 dB and n = 5 ~47 dB (Example 3-1: 50 dB at 3*fc needs n = 6) | A_dB = 10*log(1 + (f/fc)^(2n)) (Eq. 3-5) | f/fc, n | Butterworth LP (HP by inverting ratio) | calc | p.40–41, Eq. 3-5, Fig. 3-9, Example 3-1 | high |
| BOWICK-078 | filter | Butterworth equal-termination (Rs = RL = 1) prototype element values: A_k = 2*sin((2k-1)*pi/(2n)), k = 1..n (radians); A_k is the k-th ladder reactance (C or L alternating) | A_k = 2*sin((2k-1)*pi/(2n)) (Eq. 3-6); see Table 3-1 in Section 2 | n | Butterworth, Rs = RL | calc | p.41, Eq. 3-6, Table 3-1 | high |
| BOWICK-079 | filter | Table-reading rule for all prototype tables: if the ratio Rs/RL is computed use the schematic ABOVE the table (first element C1 shunt) reading element designators top-down; if RL/Rs is computed use the schematic BELOW the table (first element L1 series) reading bottom-up; element values not listed are omitted; the 1-ohm load goes directly across the output | selection rule | Rs/RL or RL/Rs | all prototype tables (3-1 to 3-8) | calc | p.41, p.48 | high |
| BOWICK-080 | filter | Unequal terminations: normalise so RL = 1 ohm (divide both by RL), take whatever Rs results; if the exact ratio is not tabulated pick the closest listed ratio (the response is then approximate); for ratios of ~100:1 or more treat the ratio as infinite (current/voltage source drive) | Rs_norm = Rs/RL; ratio >= ~100 -> use the "inf" row | Rs, RL | unequal-termination prototypes | calc | p.41–42, Example 3-2 | high |
| BOWICK-081 | filter | Chebyshev (equal-ripple, high-Q) filters trade passband ripple for a steeper initial stopband slope: an n = 3, 3-dB-ripple Chebyshev gives ~10 dB more stopband attenuation than an n = 3 Butterworth (Fig. 3-14); more ripple = more selectivity and possibly fewer elements | see Eq. 3-7 | ripple, n | Chebyshev LP | calc | p.42–44, Fig. 3-14 | high |
| BOWICK-082 | filter | Chebyshev attenuation: A_dB = 10*log[1 + eps^2 * Cn^2(w'/wc)], eps = sqrt(10^(R_dB/10) - 1) with R_dB = passband ripple; B = (1/n)*acosh(1/eps); w'/wc = (w/wc)*cosh(B) where w/wc is the ratio of interest to the 3-dB cutoff; Cn = Chebyshev polynomial of order n (Table 3-3). Hyperbolics: cosh(x) = 0.5*(e^x + e^-x); acosh(x) = ln(x + sqrt(x^2 - 1)) | Eqs. 3-7 to 3-10; worked (Example 3-3): n = 4, 2.5 dB ripple, w/wc = 2.5: eps = 0.882, B = 0.1279, w'/wc = 2.5204, C4 = 273.05, A = 47.63 dB | R_dB, n, w/wc | Chebyshev LP; curves in Figs. 3-15..3-18 start at the 3-dB cutoff (ripple not shown) | calc | p.44–46, Eqs. 3-7..3-10, Example 3-3 | high |
| BOWICK-083 | filter | Even-order (n = 2, 4, 6, ...) Chebyshev filters cannot have equal terminations; source and load must differ (use only the Rs/RL ratios listed in Tables 3-4..3-7) | n even -> Rs != RL | n | Chebyshev | review | p.47 | high |
| BOWICK-084 | filter | Bessel (maximally flat group delay / linear phase) initial stopband attenuation ~ A_dB = 3*(w/wc)^2, accurate only to w/wc ~= 2; beyond that use 6 dB/octave per element. Use Bessel when wideband signals must pass with minimum delay distortion; Butterworth/Chebyshev have strongly nonlinear passband phase | A_dB ~= 3*(w/wc)^2 for w/wc <= 2 (Eq. 3-11) | w/wc, n | Bessel LP | calc | p.48–50, Eq. 3-11, Fig. 3-20 | high |
| BOWICK-085 | filter | Frequency and impedance scaling of a low-pass prototype: C = Cn/(2*pi*fc*R), L = R*Ln/(2*pi*fc) where R = final load resistance, fc = final cutoff; source resistor: Rs_final = Rs_norm * RL_final (ratio preserved) | Eqs. 3-12, 3-13; worked (Example 3-5): Cn 3.546 at 50 MHz/250 ohm -> 45 pF; Ln 0.295 -> 235 nH; Rs = 0.2*250 = 50 ohm | Cn, Ln, fc, R | all LP prototypes (apply after HP/BP/BR transformation of the normalised network) | calc | p.50–52, Eqs. 3-12, 3-13, Example 3-5, Fig. 3-21 | high |
| BOWICK-086 | filter | Low-pass design procedure: (1) specify attenuation at selected frequencies, (2) normalise frequencies to f/fc (3-dB point = 1), (3) choose maximum allowable passband ripple (more ripple = more selective, may save components), (4) match against the attenuation curves with a small fudge factor to get the minimum n, (5) read prototype values, (6) scale to final frequency and impedance | 6-step process | specs | LP filters | review | p.52–53 | high |
| BOWICK-087 | filter | Worked Butterworth LP (Example 3-6): fc = 35 MHz, > 60 dB at 105 MHz (f/fc = 3), Rs = 50, RL = 500 (Rs/RL = 0.1) -> n = 7 from Fig. 3-9; Table 3-2B n = 7, 0.100 row -> C1 = 21 pF, L2 = 152 nH, C3 = 97 pF, L4 = 323 nH, C5 = 153 pF, L6 = 414 nH, C7 = 143 pF | scaling per BOWICK-085 | specs | Butterworth LP | calc | p.54–55, Example 3-6, Fig. 3-23 | high |
| BOWICK-088 | filter | High-pass transformation: replace every prototype element with the opposite type of reciprocal value (L_hp = 1/C_lp, C_hp = 1/L_lp); terminations unchanged; the HP attenuation curve is the mirror image of the LP curve, so read the LP curves at fc/f (e.g. 5-element 0.1-dB Chebyshev: 60 dB at f/fc = 3 for LP equals 60 dB at fc/f = 3 for HP); ripple and skirt slope magnitudes unchanged | L_hp,n = 1/C_lp,n; C_hp,n = 1/L_lp,n; then scale with Eqs. 3-12/3-13 | prototype | HP filters | calc | p.53–56, Fig. 3-24 | high |
| BOWICK-089 | filter | Worked HP (Example 3-7): fc = 60 MHz, >= 40 dB at 30 MHz (fc/f = 2), Rs = RL = 300 ohm, 0.5 dB ripple -> n = 5 Chebyshev (Table 3-6B, 1.000 row: 1.807, 1.303, 2.691, 1.303, 1.807); HP: C1 = 1/(1.807*2*pi*60e6*300) = 4.9 pF, L2 = 300/(1.303*2*pi*60e6) = 611 nH, C3 = 3.3 pF, L4 = 611 nH, C5 = 4.9 pF | HP scaling: C = 1/(Ln_lp*2*pi*fc*R)... i.e. C = 1/(2*pi*fc*R*Cn_lp) and L = R/(2*pi*fc*Ln_lp) | specs | Chebyshev HP | calc | p.57–58, Example 3-7, Fig. 3-25 | high |
| BOWICK-090 | filter | Equal-termination filters are symmetric (identical values mirrored about the centre) -> fewer calculations and fewer distinct part values for high-volume production | symmetry check | prototype | Rs = RL designs | inspect | p.56 | high |
| BOWICK-091 | filter | Dual network rules (same attenuation, phase and group delay): (1) L <-> C with values unchanged (3 H -> 3 F), (2) R <-> G with value unchanged (3 ohm -> 3 mho = 1/3 ohm), (3) shunt <-> series branches, (4) series-connected elements <-> parallel-connected, (5) voltage source <-> current source. With unequal terminations the terminations change value (1/R) — only use the dual freely for equal terminations | 5 rules | ladder | LC ladder filters | calc | p.56, Fig. 3-26 | high |
| BOWICK-092 | filter | Minimise the number of inductors in any filter (inductors have lower Q than capacitors -> higher insertion loss and degraded response): choose the prototype form (above/below table) or the dual that yields the fewest inductors after HP/BP transformation (e.g. Example 3-7: the lower-schematic form gives 2 inductors instead of 3) | count(L) -> min | topology choice | all LC filters | inspect | p.56–57 | high |
| BOWICK-093 | filter | Bandpass from low-pass prototype: the attenuation-bandwidth ratios are preserved — BW/BWc = f/fc, where BWc = 3-dB bandwidth of the bandpass and BW = bandwidth at the required attenuation; read the LP curves with this ratio. Worked: BW3dB = 2 MHz, BW40dB = 6 MHz -> ratio 3 -> 5-element Butterworth | BW_A/BW_3dB = (f/fc) on LP curves (Eq. 3-14) | BW3dB, BW at attenuation A | LP-to-BP designs | calc | p.58–59, Eq. 3-14, Example 3-8 | high |
| BOWICK-094 | filter | Bandpass responses are geometrically symmetric: f0 = sqrt(fa*fb) for any pair of equal-attenuation frequencies; given specs at asymmetric frequencies compute f0, then the missing edge f3 = f0^2/f4. Worked: 45/75 MHz edges -> f0 = 58.1 MHz; 125 MHz 40-dB edge -> f3 = 27 MHz; BW40/BW3 = (125 - 27)/(75 - 45) = 3.27 -> 4th-order or better Butterworth | f0 = sqrt(fa*fb) (Eq. 3-15) | fa, fb, spec frequencies | BP filters | calc | p.59, Eq. 3-15, Fig. 3-28 | high |
| BOWICK-095 | filter | LP-to-BP transformation: resonate every prototype element with an element of the opposite type and the SAME normalised value — shunt elements become parallel-resonant branches, series elements become series-resonant branches | shunt Cn -> Cn \|\| Ln(=Cn); series Ln -> Ln in series with Cn(=Ln) | prototype | BP filters | calc | p.59, Fig. 3-29 | high |
| BOWICK-096 | filter | BP scaling: parallel (shunt) branches C = Cn/(2*pi*R*B), L = R*B/(2*pi*f0^2*Ln); series branches C = B/(2*pi*f0^2*Cn*R), L = R*Ln/(2*pi*B); R = final load, B = 3-dB bandwidth (Hz), f0 = geometric centre (Hz). Worked (Example 3-9: f0 = 75 MHz, 1-dB Chebyshev n = 3, Rs/RL = 0.5, B = 7 MHz, RL = 100): 4.431 -> C1 = 1007 pF, L1 = 4.47 nH; 0.817 -> C2 = 2.4 pF, L2 = 1.86 uH; 2.216 -> C3 = 504 pF, L3 = 8.93 nH | Eqs. 3-16..3-19 | Cn, Ln, R, B, f0 | BP filters | calc | p.60–61, Example 3-9, Fig. 3-32 | high |
| BOWICK-097 | filter | Bandpass design procedure: (1) convert BP spec to LP ratio with Eq. 3-14, (2) pick response/order from LP curves, (3) write down prototype, (4) transform LP -> BP, (5) scale with Eqs. 3-16..3-19. Worked spec: 1-dB ripple, BW3 = 7 MHz, BW45 = 35 MHz -> ratio 5 -> n = 3 (1-dB Chebyshev gives ~50 dB at f/fc = 5) | 5 steps | spec | BP filters | review | p.60, Example 3-9 | high |
| BOWICK-098 | filter | Band-reject from low-pass prototype: use the inverse ratio BWc/BW = (f4 - f1)/(f3 - f2) in place of fc/f on the LP curves (f1..f4 = 3-dB and stopband-attenuation edges); transform: each shunt prototype element -> shunt series-resonant circuit, each series element -> series parallel-resonant circuit, both elements of each resonator having the same normalised value | BWc/BW substituted for fc/f | f1..f4 | BR filters | calc | p.60, Figs. 3-30, 3-31 | high |
| BOWICK-099 | filter | BR scaling as printed: series-resonant circuits C = Cn/(2*pi*R*B), L = R*B/(2*pi*f0^2*Ln); parallel-resonant circuits C = B/(2*pi*f0^2*R*Cn), L = R*Ln/(2*pi*B) (B = 3-dB bandwidth, R = final load, f0 = geometric centre). WARNING (verified by simulation in this extraction): these are the BP forms and, fed with low-pass prototype values g, they resonate at f0 but give a stopband ~f0^2/B wide (Butterworth n = 3, f0 = 100 MHz, B = 10 MHz: -3 dB at 9.9 and 1011 MHz). Correct scaling for LP values g (= BP forms with g -> 1/g): shunt series-resonant L = R/(2*pi*g*B), C = g*B/(2*pi*f0^2*R); series parallel-resonant L = g*R*B/(2*pi*f0^2), C = 1/(2*pi*g*R*B) (same example: -3 dB at 95.15 and 105.15 MHz) | Eqs. 3-20..3-23 (printed) and corrected forms | g, R, B, f0 | BR filters; conf note: high (as printed) / medium (correction, derived and simulated) | calc | p.60–61 | medium |
| BOWICK-100 | filter | Finite element Q in a filter designed for lossless elements: (1) insertion loss rises while ultimate stopband attenuation is unchanged (relative attenuation falls), (2) response near fc rounds off — attenuation at fc exceeds the intended 3 dB, (3) designed passband ripple shrinks and disappears at low enough Q, (4) band-reject stopband attenuation becomes finite. Use the highest-Q inductors available | 4 effects | element Q | all LC filters | sim | p.61–62, Fig. 3-33 | high |
| BOWICK-101 | filter | Minimum inductor (element) Q for the response to closely resemble the ideal: Bessel 3; Butterworth 15; Chebyshev 0.01 dB 24; 0.1 dB 39; 0.5 dB 57; 1 dB 75 (Table 3-9). Flag any filter whose inductor Q at f0/fc is below the table value | Q_L >= Q_min(type) | inductor Q, filter type | LC filters | calc | p.62, Table 3-9 | high |
| BOWICK-102 | filter | Filter insertion loss from element Q: replace each reactive element by the resistance corresponding to its Q (series Rs = X/Q or parallel Rp = Q*X) and apply the voltage-division rule from source to load, as in Ch.2 | IL via voltage division with loss resistors | element Qs | LC filters | calc | p.62 | high |
| BOWICK-103 | matching | Maximum power transfer: DC — RL = Rs (P1 = RL/(1 + RL)^2 for Rs = 1, Vs = 1, peak at RL = 1); AC — ZL = conjugate of Zs (same real part, opposite reactance) so source and load reactances cancel and Rs = RL remains | ZL = Zs* | Zs, ZL | any source-load interface | calc | p.63–64, Figs. 4-1, 4-2 | high |
| BOWICK-104 | matching | A reactive conjugate match is exact at only one frequency (where +jX = -jX); away from it the match degrades progressively — broadband matches need the wideband techniques (multiple L sections) | single-frequency validity | f | all LC matching networks | sim | p.64 | high |
| BOWICK-105 | matching | Mismatch loss when a 100-ohm source drives a 1000-ohm load directly is ~4.8 dB (about one third of the available power lost); an L network removes it | ML_dB = -10*log(1 - \|Gamma\|^2), Gamma = (RL - Rs)/(RL + Rs) = 0.818 -> 4.8 dB (derived) | Rs, RL | resistive mismatch; conf note: high (value), medium (formula derived) | calc | p.65 | medium |
| BOWICK-106 | matching | L-network mechanism: the shunt element transforms the larger termination down to a series equivalent whose real part equals the other termination (e.g. -j333 \|\| 1000 = 100 - j300); the series element then cancels the residual reactance (+j300). Four arrangements exist: two low-pass (series L / shunt C) and two high-pass (series C / shunt L) | Z = Xc*RL/(Xc + RL) | RL, Xp | L networks | calc | p.64–65, Figs. 4-4..4-8 | high |
| BOWICK-107 | matching | L-network design equations: Qs = Qp = sqrt(Rp/Rs - 1); Xs = Qs*Rs; Xp = Rp/Qp; Rp = the termination in the shunt leg (larger), Rs = the termination in the series leg (smaller); Xp and Xs must be opposite reactance types. Worked: 100 -> 1000 ohm at 100 MHz with DC pass: Q = 3, Xs = 300 ohm (L = 477 nH), Xp = 333 ohm (C = 4.8 pF) | Eqs. 4-1, 4-2, 4-3 | Rs, Rp, f | L match between two resistances | calc | p.65–66, Fig. 4-9, Example 4-1 | high |
| BOWICK-108 | matching | The L network's Q is fixed by the impedance ratio (Q = sqrt(Rp/Rs - 1)); this is also the minimum Q achievable with pi or T networks between the same terminations | Q_L = sqrt(Rp/Rs - 1) | Rs, Rp | L, pi, T networks | calc | p.66 | high |
| BOWICK-109 | matching | Complex terminations — absorption: choose the L topology so that element capacitors are in parallel with stray capacitance and element inductors in series with stray inductance, then subtract the strays from the computed element values (C' = C_calc - C_stray, L' = L_calc - L_stray). Worked: source 100 + j126 ohm (200 nH at 100 MHz), load 1000 ohm \|\| 2 pF -> element L = 477 - 200 = 277 nH, element C = 4.8 - 2 = 2.8 pF | C' = C_calc - C_stray; L' = L_calc - L_stray; requires stray < calculated | Zs, ZL, f | complex source/load | calc | p.66–67, Example 4-2, Fig. 4-12 | high |
| BOWICK-110 | matching | Complex terminations — resonance: when absorption is impossible (stray larger than the computed element, e.g. 20 pF stray vs 4.8 pF needed), cancel the stray with an equal and opposite reactance at f0 (L = 1/(w^2*C_stray)), then match the real parts; combine the cancelling element with the adjacent matching element of the same type (parallel Ls: L1*L2/(L1+L2)). Worked (Example 4-3, 75 MHz, DC block): 40 pF stray -> 112.6 nH; 50 -> 600 ohm: Q = 3.32, Xs = 166 ohm -> series C = 12.78 pF, Xp = 181 ohm -> shunt L = 384 nH; 384 \|\| 112.6 = 87 nH | L_res = 1/((2*pi*f)^2*C_stray) | Zs, ZL, f | complex loads | calc | p.67–68, Example 4-3, Figs. 4-13..4-16 | high |
| BOWICK-111 | matching | Pi network = two back-to-back L networks matching each termination to a virtual resistance R that is SMALLER than both terminations; loaded Q (accepted approximation) Q = sqrt(RH/R - 1) with RH = larger termination, so R = RH/(Q^2 + 1); design each L section with Eqs. 4-1..4-3 (load side: Xp2 = RL/Q, Xs2 = Q*R; source side: Q1 = sqrt(Rs/R - 1), Xp1 = Rs/Q1, Xs1 = Q1*R); the two series reactances add if alike or subtract if opposite -> four pi variants | Eq. 4-4; worked (Example 4-4: 100 -> 1000 ohm, Q = 15): R = 4.42 ohm; Xp2 = 66.7, Xs2 = 66.3; Q1 = 4.6, Xp1 = 21.7, Xs1 = 20.5; series combinations 87.4 (like) or 46.4 (opposite) ohm (figure values) | Rs, RL, Q, f | narrowband/high-Q matching; Q must exceed the L-network Q | calc | p.66–70, Eq. 4-4, Example 4-4, Figs. 4-19..4-21 | high |
| BOWICK-112 | matching | T network = two L networks with shunt legs joined, matching to a virtual R LARGER than both terminations; Q = sqrt(R/Rsmall - 1) (the L section on the smaller termination sets the Q), R = Rsmall*(Q^2 + 1); the two shunt reactances combine in parallel (like: X1*X2/(X1+X2); opposite: X1*X2/\|X2 - X1\|) -> four T variants; used to match two low impedances with high Q | Eq. 4-5; worked (Example 4-5: 10 -> 50 ohm, Q = 10): R = 1010 ohm; Xs1 = 100, Xp1 = 101; Q2 = sqrt(1010/50 - 1) = 4.4, Xp2 = 230 (231), Xs2 = 220; shunt combos 70 (like) or 179 (opposite) ohm | Rs, RL, Q, f | low-impedance high-Q matching | calc | p.69–71, Eq. 4-5, Example 4-5, Figs. 4-22..4-24 | high |
| BOWICK-113 | matching | Choose among the equivalent L/pi/T variants by: (1) which strays can be absorbed, (2) harmonic filtering needed (low-pass forms), (3) DC pass (series L) or DC block (series C) | selection criteria | application | matching network topology | review | p.69 | high |
| BOWICK-114 | matching | Wideband (low-Q) matching: two series-connected L sections with the virtual R between the terminations (Rsmaller < R < Rlarger); Q = sqrt(R/Rsmaller - 1) = sqrt(Rlarger/R - 1); minimum Q (maximum bandwidth) when R = sqrt(Rs*RL); for still wider bandwidth cascade n L sections with equal successive resistance ratios R1/Rsmaller = R2/R1 = ... = Rlarger/Rn, i.e. each ratio = (Rlarger/Rsmaller)^(1/(n+1)) | Eqs. 4-6, 4-7, 4-8 | Rs, RL, n | broadband matching | calc | p.71–72, Figs. 4-25, 4-26 | high |
| BOWICK-115 | matching | Smith chart construction: reflection coefficient rho = (Zn - 1)/(Zn + 1) with Zn = R + jX normalised; constant-resistance circles centred at (R/(R+1), 0) with radius 1/(R+1); constant-reactance arcs centred at (1, 1/X) with radius 1/X; upper half = +jX (inductive), lower = -jX (capacitive); R = 0 circle is the outer boundary; R = inf and X = inf coincide at (1, 0); any point outside the chart is negative resistance (oscillation risk) | circle equations (Steps 1–8) | Zn | Smith chart | calc | p.72–75, Fig. 4-28 | high |
| BOWICK-116 | matching | Smith chart plotting: normalise all impedances by one convenient number that places them near the chart centre (e.g. 100 + j150 -> /100 -> 1 + j1.5); all impedances on that chart must use the same normalisation; values near the right edge (near infinity) cannot be read accurately | Zn = Z/Z_norm | Z | Smith chart | review | p.75 | high |
| BOWICK-117 | matching | Smith chart moves: adding a series capacitor moves the point counter-clockwise (downward) along the constant-R circle by Xc; a series inductor moves clockwise (upward) by XL (e.g. 0.5 + j0.7 with series -j1.0 -> 0.5 - j0.3); flipping the chart gives admittance (Y = G +/- jB); an overlaid Z/Y chart (immittance chart) handles shunt elements | series C: -jX along const-R; series L: +jX along const-R | Z, element | Smith-chart matching | calc | p.75 | high |
| BOWICK-118 | components | Transistor hybrid-pi (common-emitter) typical element values: rbb' (base spreading) tens of ohms, larger for smaller transistors; rb'e ~1000 ohm; rb'c ~5 megohm; rce ~100 kohm; Ce (emitter diffusion + junction) ~100 pF; Cc (collector-base feedback) ~3 pF; collector current Ic = beta*IB'. Add LB, LE, LC (bond wire + lead inductance) at RF | typical values | device | BJT RF modelling | review | p.104, Figs. 5-2, 5-3 | high |
| BOWICK-119 | rf | BJT input-impedance model: drop rb'c (5 Mohm ~ open); Miller-transpose Cc to the input as Cc*(1 - beta*RL) (magnitude of the gain term; as printed) and add to Ce -> CT; Zin = jw*(LB + LE) + rbb' + rb'e/(1 + jw*rb'e*CT). Input impedance is maximum (rbb' + rb'e) at DC and falls with frequency until rbb', LB, LE dominate. Worked: LT = 20 nH, rb'e = 1000, rbb' = 50, CT = 100 pF -> 1050 ohm at DC, 50 ohm at 112 MHz | Zin formula | model values, f | BJT common emitter | calc | p.105, Figs. 5-4..5-6 | high |
| BOWICK-120 | rf | Keep LB and LE limited to the bond-wire inductance by careful layout (short base/emitter connections); then they do not affect input impedance until well above VHF | minimise LB, LE | layout | BJT stages | inspect | p.105 | high |
| BOWICK-121 | rf | BJT output impedance falls with frequency (Cc, Ce reactances plus collector-to-base feedback through Cc amplified by beta); increasing the external source resistance Rs decreases Zout | qualitative | Rs, f | BJT stages | measure | p.106–107, Fig. 5-7 | medium |
| BOWICK-122 | rf | Internal feedback (Cc dominant, rb'c negligible) means input and output are not isolated: a load change alters Zin and a source change alters Zout, so sequential input-then-output matching does not converge; use the simultaneous conjugate match (Ch.6) or accept a tolerable mismatch when Cc is small. At high frequency Cc plus strays can give 180 deg feedback phase -> oscillation | coupled ports | Cc | BJT amplifiers | calc | p.107 | high |
| BOWICK-123 | rf | Transistor power gain vs frequency behaves like an RC low-pass: falls at 6 dB/octave and passes through 0 dB at fmax; fT (hfe = 1) is extrapolated, only indicates proximity to the frequency limit (power gain may remain above fT) | slope 6 dB/oct; G(fmax) = 0 dB | fmax, fT | RF transistors | review | p.107, p.115, Fig. 5-8 | high |
| BOWICK-124 | rf | Gain classes: unilateralized (both rb'c and Cc negated) > neutralized (only Cc negated) > unneutralized; the unilateralized–neutralized difference is usually negligible, so neutralization (external C-B feedback of correct amplitude/phase) is sufficient | ordering | design | BJT amplifiers | review | p.108 | high |
| BOWICK-125 | rf | Switch operation: cut-off (IB = 0, IC = 0, VCE = supply) and saturation (max IB, max IC, min VCE) dissipate minimum power; amplifiers bias on the linear (near-horizontal) part of the output curves | bias regions | Ic-Vce curves | BJT switch/amplifier | review | p.108, Figs. 5-9, 5-10 | high |
| BOWICK-126 | rf | Two-port short-circuit Y parameters: yi = I1/V1 (V2 = 0), yr = I1/V2 (V1 = 0), yf = I2/V1 (V2 = 0), yo = I2/V2 (V1 = 0); I1 = yi*V1 + yr*V2, I2 = yf*V1 + yo*V2. Y = G +/- jB (parallel form); +jB = shunt capacitor, -jB = shunt inductor. The RF short is a large capacitor, which fails at high frequency (capacitor SRF/reactance) — hence S parameters for VHF+ devices | Eqs. 5-1..5-6 | device data | transistor characterisation | review | p.109–110, p.122 | high |
| BOWICK-127 | rf | Reflection coefficient Gamma = V_reflected/V_incident = rho angle theta; Gamma = (ZL - Zo)/(ZL + Zo) = (Zn - 1)/(Zn + 1); \|Gamma\| = 0 for ZL = Zo, 1 for open/short; \|Gamma\| > 1 implies the load is a power source — unacceptable in amplifier input networks. Worked: ZL = 100 + j75 in 50 ohm -> Zn = 2 + j1.5 -> 0.54 angle 29.7 deg | Eqs. 5-7..5-9 | ZL, Zo | transmission lines, S-parameters | calc | p.111–112, Example 5-1 | high |
| BOWICK-128 | rf | S parameters: b1 = S11*a1 + S12*a2, b2 = S21*a1 + S22*a2; S11 = b1/a1 (a2 = 0) input reflection, S22 = b2/a2 (a1 = 0) output reflection, S21 = b2/a1 forward transmission, S12 = b1/a2 reverse transmission; measured with source and load = Zo (50 ohm) so no termination reflections; S21/S12 are the forward/reverse gain in the Zo system; dB = 20*log\|S\|; S11/S22 plot directly on the Smith chart to give Zin/Zout | Eqs. 5-10..5-15 | measured S | two-port characterisation | calc | p.113–114 | high |
| BOWICK-129 | rf | Y-to-S conversion (y's normalised: multiply each Y by Zo first): D = (1 + yi)(1 + yo) - yr*yf; S11 = [(1 - yi)(1 + yo) + yr*yf]/D; S12 = -2*yr/D; S21 = -2*yf/D; S22 = [(1 + yi)(1 - yo) + yr*yf]/D | formulas 1–4 | y-parameters, Zo | parameter conversion | calc | p.114 | high |
| BOWICK-130 | rf | S-to-Y conversion: D' = (1 + S11)(1 + S22) - S12*S21; yi = [(1 + S22)(1 - S11) + S12*S21]/D' * (1/Zo); yr = -2*S12/D' * (1/Zo); yf = -2*S21/D' * (1/Zo); yo = [(1 + S11)(1 - S22) + S12*S21]/D' * (1/Zo) | formulas 5–8 | S-parameters, Zo | parameter conversion | calc | p.114 | high |
| BOWICK-131 | rf | RF transistor data-sheet parameters to check: fT (gain-bandwidth, extrapolated); Ccb (collector-base C at 1 MHz, Vcb = 10 V, emitter open) — smaller is better, equals Cc of the model; hfe at 1 kHz (use DC hFE for bias design); rb'Cc time constant — smaller is better; NF only valid at the stated bias/Rs/frequency — use the NF contours (NF vs Ic and Rs) and note NF rises with frequency | items | data sheet | device selection | review | p.115 | high |
| BOWICK-132 | rf | Noise figure depends strongly on bias and source resistance: 2N5179 at VCE = 6 V, 105 MHz, NF = 3.5 dB is met by (Ic mA : Rs ohm) 0.5 : 105 or 600; 1.0 : 90 or 500; 1.5 : 85 or 430; 2.0 : 82 or 390; 3.0 : 81 or 320; 5.0 : 94 or 250 — two Rs values per Ic; data-sheet NF max 4.5 dB at VCE = 6 V, Ic = 1.5 mA, Rs = 50 ohm; do not extrapolate contours to other frequencies (none given at 300 MHz) | NF contour data | Ic, Rs, f | LNA bias/source design (2N5179 example) | review | p.115, p.122, Fig. 5-17 (graph) | high |
| BOWICK-133 | rf | Bias for maximum fT: 2N5179 fT peaks at ~12 mA collector current; choose Ic from the fT-vs-Ic curve when operating near the device limit, then measure Y/S parameters at that bias (manufacturer data exist only at a few bias points, e.g. VCE = 6 V, Ic = 1.5 mA and 5 mA) | Ic(fT max) ~ 12 mA (2N5179) | fT vs Ic curve | high-frequency gain | review | p.122 | high |
| BOWICK-134 | rf | Worked data-sheet readings (2N5179): at 200 MHz, VCE = 6 V, Ic = 1.5 mA: yi = 2.5 + j7.5 mmho (400 ohm \|\| 6 pF, Xc = 133 ohm), yo = 0.25 + j1.8 mmho (4 kohm \|\| 1.4 pF, Xc = 555.5 ohm); at 100 MHz, Ic = 5 mA: S11 = 0.65 angle 309, S22 = 0.84 angle 348, S12 = 0.03 angle 70 (-30.5 dB isolation), S21 = 8.2 angle 123 (18.3 dB gain in 50 ohm without matching); Zin = 48 - j79 ohm from a 50-ohm-normalised Smith chart | values | data sheet | example device | calc | p.122–123, Fig. 5-18 | high |
| BOWICK-135 | rf | Bias-point stability matters because every Y/S parameter changes with bias; a temperature-stable DC operating point is required whenever gain/NF specs must hold over temperature | — | bias network | RF amplifiers | review | p.127 | high |
| BOWICK-136 | rf | Silicon BJT VBE falls ~2.5 mV/degC from ~0.7 V at room temperature; the resulting collector-current drift is dIC/IC ~= -dVBE/VE, so emitter voltage VE (not RE) sets VBE stability: VE = 20*dVBE limits the change to 5%; for +/-50 degC (dVBE = 125 mV) VE = 2.5 V gives +/-5% IC; typical VE = 2–4 V (higher wastes power and lowers AC gain — bypass RE at the signal frequency) | dIC/IC = -dVBE/VE (Eq. 6-1); dVBE = 2.5 mV/degC * dT | dT, VE | BJT bias networks with emitter resistor | calc | p.127–128, Eq. 6-1, Fig. 6-4 | high |
| BOWICK-137 | rf | BJT beta rises ~0.5%/degC (silicon): +/-50 degC -> +/-25% in beta and hence IC; production beta spread is typically 10:1 (e.g. 50–500) — bias networks must tolerate both | dbeta/beta = 0.5%/degC * dT | dT | BJT bias design | calc | p.128 | high |
| BOWICK-138 | rf | Collector-current change with beta: dIC = IC1 * (dbeta/(beta1*beta2)) * (1 + RB/RE), RB = R1 \|\| R2 (base divider), RE = emitter resistor, IC1 = current at beta1 (lowest), dbeta = beta2 - beta1; the only lever is RB/RE — rule of thumb RB/RE < 10 (smaller ratio = more stable but less AC current gain; below ~1 little further improvement) | Eq. 6-2; RB/RE < 10 | IC1, beta1, beta2, R1, R2, RE | emitter-degenerated divider bias (Fig. 6-4) | calc | p.128 | high |
| BOWICK-139 | rf | Bias network 1 (divider + RE, most stable) design sequence: choose IC, VC, VCC, beta; choose VE (~2.5 V); IE ~= IC; RE = VE/IE; RC = (VCC - VC)/IC; IB = IC/beta; VBB = VE + VBE (0.7 V); choose divider current IBB (larger is better, e.g. 1.5 mA); R1 = VBB/IBB; R2 = (VCC - VBB)/(IBB + IB). Worked: IC = 10 mA, VC = 10 V, VCC = 20 V, beta = 50, VE = 2.5 V -> RE = 250, RC = 1000, IB = 0.2 mA, VBB = 3.2 V, R1 = 2133, R2 = 9882 ohm | 10 steps | operating point | BJT bias | calc | p.127, Fig. 6-4 | high |
| BOWICK-140 | rf | Bias network 2 (collector-feedback resistor RF plus base divider from VC): choose VBB, IBB; IB = IC/beta; RB = (VBB - VBE)/IB; R1 = VBB/IBB; RF = (VC - VBB)/(IBB + IB); RC = (VCC - VC)/(IC + IB + IBB). Worked (same point, VBB = 2 V, IBB = 1 mA): RB = 6500, R1 = 2000, RF = 6667, RC = 893 ohm | 7 steps | operating point | BJT bias, second-most stable | calc | p.128, Fig. 6-5 | high |
| BOWICK-141 | rf | Bias network 3 (single collector-to-base RF, least stable): IB = IC/beta; RF = (VC - VBE)/IB; RC = (VCC - VC)/(IB + IC). Worked: RF = (10 - 0.7)/0.2 mA = 46.5 k, RC = 980 ohm. Networks 2 and 3 give no control over RB/RE or VE ("potluck" stability) though RF feedback works reasonably well | 4 steps | operating point | BJT bias | calc | p.129, Fig. 6-6 | high |
| BOWICK-142 | rf | JFET/depletion-FET bias law ID = IDSS*(1 - VGS/Vp)^2 -> VGS = Vp*(1 - sqrt(ID/IDSS)); design 4 (divider + source resistor): RD = (VCC - VD)/ID; choose VS = 2–3 V; RS = VS/ID; VG = VGS + VS; choose R1 for input resistance (e.g. 220 k); R2 = R1*(VCC - VG)/VG. Worked: ID = 10 mA, VD = 10 V, VCC = 20 V, Vp = -6 V, IDSS = 5 mA -> RD = 1000, VGS = 2.48 V, VS = 2.5 V, RS = 250, VG = 4.98 V, R2 = 664 k. Design 5 (self-bias, IG = 0): VS = VGS, RS = VGS/ID = 248 ohm, RG ~ 1 Mohm | Eq. 6-3 | ID, IDSS, Vp | FET bias | calc | p.129–130, Figs. 6-7, 6-8 | high |
| BOWICK-143 | rf | Transistor selection for an amplifier: check stability and maximum available gain (MAG) first; MAG is never reached in practice, so leave margin — e.g. for an 18 dB requirement at 200 MHz do not pick a device with MAG = 19 dB (yr, matching-network loss and bias drift eat the margin) | MAG - G_required >= margin (>1 dB implied) | MAG, spec | device selection | review | p.130–131 | high |
| BOWICK-144 | rf | Linvill stability factor C = \|yr*yf\| / (2*gi*go - Re(yr*yf)); C < 1 -> unconditionally stable at that bias (any passive source/load, absent unaccounted external feedback); C > 1 -> potentially unstable (oscillates for some terminations); C near 1 is dangerous because bias/temperature drift shifts the Y parameters; smaller C is better | Eq. 6-4; worked (Example 6-1): \|yf*yr\| = 5.57, Re = -1.47, 2*gi*go = 6.4 -> C = 0.71 | yi, yo, yf, yr (mmho) | Y-parameter design | calc | p.130–131, Eq. 6-4 | high |
| BOWICK-145 | rf | Stern stability factor for a specific circuit: K = 2*(gi + GS)*(go + GL) / (\|yr*yf\| + Re(yr*yf)); K > 1 -> stable with those source/load conductances; K < 1 -> potentially unstable (will most likely oscillate). Use Linvill C to choose devices, Stern K to check the circuit | Eq. 6-5 | y-params, GS, GL | Y-parameter design | calc | p.131, Eq. 6-5 | high |
| BOWICK-146 | rf | Maximum available gain MAG = \|yf\|^2 / (4*gi*go) (occurs for yr = 0 with YS = yi*, YL = yo*). Worked: yf = 52 - j20 mmho, gi = 8, go = 0.4 -> 242.5 = 23.8 dB | Eq. 6-6; MAG_dB = 10*log(MAG) | yf, gi, go | device gain screening | calc | p.131, Eq. 6-6, Example 6-1 | high |
| BOWICK-147 | rf | Simultaneous conjugate match (unconditionally stable device, includes yr): GS = sqrt([2*gi*go - Re(yf*yr)]^2 - \|yf*yr\|^2) / (2*go); BS = -bi + Im(yf*yr)/(2*go); GL = sqrt([2*gi*go - Re(yf*yr)]^2 - \|yf*yr\|^2) / (2*gi) = GS*go/gi; BL = -bo + Im(yf*yr)/(2*gi). The transistor then presents Yin = YS* and Yout = YL* | Eqs. 6-7..6-11; worked (Example 6-1, 100 MHz, VCE = 10 V, IC = 5 mA, yi = 8 + j5.7, yo = 0.4 + j1.5, yf = 52 - j20, yr = 0.01 - j0.1 mmho): YS = 6.95 - j12.41 mmho, YL = 0.347 - j1.84 mmho | y-parameters | Y-parameter amplifier design | calc | p.131–132, Example 6-1 | high |
| BOWICK-148 | matching | Matching-network realisation from normalised Smith-chart arcs (Example 6-1): normalise the chart to a convenient resistance N (50 ohm = 20 mmho for the input; 200 ohm = 5 mmho for the tiny output admittance); series C: C = 1/(w*x_n*N); shunt L: L = N/(w*b_n) (x_n, b_n = normalised reactance/susceptance; by duality series L: L = x_n*N/w, shunt C: C = b_n/(w*N)). Worked at 100 MHz: input YS_n = 0.34 - j0.62 (ZS_n = 0.69 + j1.2): series C -j1.3 -> 24.5 pF, shunt L -j1.1 mho -> 72 nH; output YL_n = 0.069 - j0.368 (ZL_n = 0.495 + j2.62): series C -j1.9 -> 4.18 pF, shunt L -j0.89 -> 358 nH | denormalisation formulas; the book's Eqs. 4-11..4-14 (on pp.81–102, absent from the extraction) are identified by their use in Examples 6-1/6-4: Eq. 4-11 series C = 1/(w*X*N), Eq. 4-12 shunt C = B/(w*N), Eq. 4-13 series L = X*N/w, Eq. 4-14 shunt L = N/(w*B) | arcs, N, f | L-network synthesis on the Smith chart; conf note: high (values) / medium (equation numbering inferred) | calc | p.135, p.146, Examples 6-1, 6-4, Figs. 6-9..6-12 | medium |
| BOWICK-149 | rf | Complete 100-MHz amplifier example (Fig. 6-12): 20 V supply, 10 k / 2 k base divider, 2 k collector resistor, 500 ohm emitter resistor, 0.1 uF bypass capacitors as RF bypass at 100 MHz, input L-network 24.5 pF series / 72 nH shunt, output 4.2 pF series / 358 nH shunt | example values | — | reference circuit | review | p.135, Fig. 6-12 | high |
| BOWICK-150 | rf | S-parameter stability test (RF Toolbox demo, applies generally): delta = S11*S22 - S12*S21; K = (1 - \|S11\|^2 - \|S22\|^2 + \|delta\|^2) / (2*\|S12*S21\|); unconditionally stable iff K > 1 AND \|delta\| < 1 (any passive source or load is then stable). Worked: K = 1.0599, \|delta\| = 0.6776 at 1.9 GHz -> stable | K, delta formulas | S11, S12, S21, S22 | S-parameter amplifier design | calc | p.136 | high |
| BOWICK-151 | rf | S-parameter simultaneous conjugate match load reflection coefficient: B2 = 1 + \|S22\|^2 - \|S11\|^2 - \|delta\|^2; C2 = S22 - delta*conj(S11); GammaL = (B2 - sqrt(B2^2 - 4*\|C2\|^2)) / (2*C2) (input side by symmetry with S11/S22 swapped); expected matched gain Gt = 10*log(\|S21\|/\|S12\| * (K - sqrt(K^2 - 1))) (= MAG in S-parameter form) — worked 19.24 dB, measured matched S21 between 19 and 19.5 dB at 1.9 GHz | formulas | S-parameters, K | S-parameter amplifier design | calc | p.136–139 | high |
| BOWICK-152 | rf | Single-stub microstrip matching (demo): draw the SWR circle of radius \|GammaL\|, the constant-conductance circle through the 50-ohm load (g = 1), take the intersection (two solutions; lower-half chosen, yA = 1 + j0.62), stub susceptance jb = yA - yL, open stub length = rotation angle from y = 0 point /360/2 wavelengths, series line length from angle A to Zin /360/2; worked: output stub 0.0883 lambda + series 0.2147 lambda, input stub 0.0763 lambda + series 0.2266 lambda; microstrip default Z0 = 50.2561 ohm; verify by plotting S11, S22 (dB) and S21 (dB) with/without networks over 1.5–2.3 GHz | procedure | GammaL, Z0 | distributed matching | calc | p.136–139, Figs. 6-13..6-18 | high |
| BOWICK-153 | rf | Transducer gain (output power to load / maximum power available from source, incl. matching, excl. component loss): GT = 4*GS*GL*\|yf\|^2 / \|(yi + YS)*(yo + YL) - yf*yr\|^2; compute GT after choosing YS/YL — it is the best estimate of actual stage gain (yr may take an appreciable toll). Worked (Example 6-2): 231.2 = 23.64 dB vs MAG 23.8 dB | Eq. 6-12 | y-params, YS, YL | Y-parameter design | calc | p.139, Eq. 6-12, Example 6-2 | high |
| BOWICK-154 | rf | Potentially unstable transistor (C > 1): options in order of simplicity — (1) change the bias point (especially when C is just above 1; the new point must be temperature-stable), (2) unilateralize/neutralize with an external feedback admittance Yf = -yr so the composite yrc = 0 (then C = 0, unconditionally stable), (3) selectively mismatch input/output to reduce gain | options | C | amplifier stabilisation | review | p.139–140 | high |
| BOWICK-155 | rf | Neutralization (preferred over unilateralization): add external feedback cancelling only the reverse susceptance, Bf = -br, so the composite brc = 0; works because gr is negligible versus br in most transistors. For yr = +jb use a series L-C branch tuned to present net negative (inductive) susceptance (Fig. 6-19A); for yr = -jb provide an external positive susceptance (Fig. 6-19B) | Bf = -br | yr = gr + j*br | narrowband BJT/FET stages | calc | p.140, Fig. 6-19 | high |
| BOWICK-156 | rf | Neutralization/unilateralization adds cost and complexity and cancels feedback only at the operating frequency — it can create instability at other frequencies; sweep stability (K or C) over the full band, not just f0 | stability check across band | yr(f) | neutralized amplifiers | sim | p.140 | high |
| BOWICK-157 | rf | Stabilise a potentially unstable device without feedback by selective mismatch: (1) choose GS from the optimum-noise source data (or convenience / input-network Q), (2) choose a K > 1 (Stern), (3) solve Eq. 6-5 for GL, (4) set BL = -bo, (5) compute Yin = yi - yr*yf/(yo + YL), (6) set BS = -Im(Yin), (7) compute GT with Eq. 6-12. Gain is necessarily below the simultaneous-conjugate value | Yin = yi - yr*yf/(yo + YL) (Eq. 6-13) | y-params, GS, K | potentially unstable devices (C > 1) | calc | p.140–141, Eq. 6-13 | high |
| BOWICK-158 | rf | Worked selective-mismatch design (Example 6-3, 200 MHz): yi = 2.25 + j7.2, yo = 0.4 + j1.9, yf = 40 - j20, yr = 0.05 - j0.7 mmho -> Linvill C = 2.27 (potentially unstable); GS = 1/250 ohm = 4 mmho (2N5179 optimum-NF source resistance 250 ohm); K = 3 chosen "for an adequate safety margin"; \|yr*yf\| = 31.35, Re = -12 -> GL = 4.24 mmho; BL = -j1.9; Yin = 4.84 + j13.44 mmho; YS = 4.84 - j13.44 mmho; GT = 67.61 = 18.3 dB, stable | worked chain | example | reference design | calc | p.141, Example 6-3 | high |
| BOWICK-159 | rf | S-parameter stability (Rollett): Ds = S11*S22 - S12*S21; K = (1 + \|Ds\|^2 - \|S11\|^2 - \|S22\|^2)/(2*\|S21\|*\|S12\|); K > 1 -> unconditionally stable for any source/load (book text); the complete test also requires \|Ds\| < 1 (stated in the book's RF Toolbox demo, p.136). If K < 1: choose another bias point, another transistor, or design with stability-aware terminations | Eqs. 6-14, 6-15 | S-params at bias and f | S-parameter amplifier design | calc | p.142, Eqs. 6-14, 6-15; p.136 | high |
| BOWICK-160 | rf | S-parameter maximum available gain: B1 = 1 + \|S11\|^2 - \|S22\|^2 - \|Ds\|^2; MAG_dB = 10*log(\|S21\|/\|S12\|) + 10*log\|K -/+ sqrt(K^2 - 1)\| — use the minus sign when B1 > 0 and the plus sign when B1 < 0; MAG is undefined (imaginary) for K < 1 | Eqs. 6-16, 6-17 | S-params, K | unconditionally stable devices | calc | p.142 | high |
| BOWICK-161 | rf | S-parameter simultaneous conjugate match: C2 = S22 - Ds*conj(S11); B2 = 1 + \|S22\|^2 - \|S11\|^2 - \|Ds\|^2; \|GammaL\| = (B2 -/+ sqrt(B2^2 - 4*\|C2\|^2))/(2*\|C2\|) with the sign before the radical opposite to the sign of B2; angle(GammaL) = -angle(C2); GammaS = conj[S11 + S12*S21*GammaL/(1 - GammaL*S22)] | Eqs. 6-18..6-21 | S-params | K > 1 devices | calc | p.142–143 | high |
| BOWICK-162 | rf | Worked S-parameter design (Example 6-4, 200 MHz, VCE = 10 V, IC = 10 mA): S11 = 0.4/162, S22 = 0.35/-39, S12 = 0.04/60, S21 = 5.2/63 (mag/deg) -> Ds = 0.068/-57, K = 1.74, B1 = 1.03, MAG = 21.14 - 5 = 16.1 dB; C2 = 0.377/-39, B2 = 0.958, GammaL = 0.487/39 (ZL = 50*(1.6 + j1.28) = 80 + j64 ohm); GammaS = 0.522/-162 (ZS = 50*(0.32 - j0.14) = 16 - j7 ohm; the printed intermediate "0.522/162" is the bracket before conjugation). Networks (50 ohm): input shunt C b = 1.45 -> 23 pF, series L x = 0.33 -> 13 nH; output series C x = -1.3 -> 12 pF, shunt L b = -0.78 -> 51 nH | worked chain | example | reference design | calc | p.143–146, Example 6-4, Figs. 6-20..6-22 | high |
| BOWICK-163 | rf | S-parameter transducer gain (includes matching, excludes component loss): GT = \|S21\|^2*(1 - \|GammaS\|^2)*(1 - \|GammaL\|^2) / \|(1 - S11*GammaS)*(1 - S22*GammaL) - S12*S21*GammaL*GammaS\|^2; for a simultaneous conjugate match GT = MAG (Example 6-5: 41.15 = 16.1 dB) — compute GT before building | Eq. 6-22 | S-params, GammaS, GammaL | S-parameter design verification | calc | p.146, Eq. 6-22, Example 6-5 | high |
| BOWICK-164 | rf | Y and S parameters are small-signal parameters and must not be used to design RF power amplifiers; use the manufacturer's large-signal input/output impedances, measured with the device operating as a conjugately matched amplifier at the intended supply voltage and output power | — | data sheet | large-signal PA design | review | p.169, p.178 | high |
| BOWICK-165 | rf | Check whether large-signal impedance data are series (R +/- jX) or shunt (R \|\| C) before designing the match; convert with the series-parallel equations (Ch.2). MRF233 at 100 MHz: series Zin = 1.7 - j2.7 ohm, Zout = 5 - j5.6 ohm; parallel input 6 ohm \|\| 422 pF, output 11.3 ohm \|\| 158 pF | Rp = (Q^2 + 1)*Rs, Xp = Rp/Q | data-sheet impedances | PA matching | calc | p.169, Figs. 7-2, 7-3 | high |
| BOWICK-166 | rf | Required RF drive increases with frequency for a given output: MRF233 1 W in -> 20 W out at 50 MHz (13 dB) but only 14 W at 90 MHz (11.5 dB); size the driver at the highest operating frequency | Pout(f) at fixed Pin from data-sheet curve | frequency | PA drive budgeting | calc | p.169 | high |
| BOWICK-167 | rf | Amplifier classes: A — conduction 360 deg, most linear, efficiency < 50%, bias as small-signal; B — conduction ~180 deg, efficiency ~70%, much less linear (harmonics must be filtered), push-pull or single device with a resonant output circuit; C — conduction significantly < 180 deg, idles at cutoff, poorest linearity, efficiency approaching 85% | eta_A < 50%; eta_B ~ 70%; eta_C up to ~85% | class | PA architecture | review | p.174–176 | high |
| BOWICK-168 | rf | Nonlinear transfer Vout = A*Vin + B*Vin^2 + C*Vin^3 + ...; the 2nd-order term grows as the square of input so it eventually equals the fundamental — the (extrapolated) point where 2nd-order and 1st-order outputs are equal is the second-order intercept; the analogous point for the 3rd-order term is the third-order intercept; higher intercept = better large-signal handling (figure of merit) | Eq. 7-1; slopes 1:1 (fundamental), 2:1 (2nd order), 3:1 (3rd order) dB/dB | A, B, C coefficients | amplifiers, mixers | measure | p.174–175, Figs. 7-5, 7-6 | high |
| BOWICK-169 | rf | Two-tone intermodulation products of a nonlinear stage: fundamentals f1, f2; 2nd order 2f1, 2f2, f1 + f2, f1 - f2; 3rd order 3f1, 3f2, 2f1 +/- f2, 2f2 +/- f1. When f1 and f2 are close, 2f1 - f2 and 2f2 - f1 fall next to the fundamentals and cannot practically be filtered out — IMD must be controlled by linearity (intercept point) | product frequency list | f1, f2 | linear amplifiers, receivers | calc | p.175 | high |
| BOWICK-170 | rf | Class-B bias: set VBE ~0.7 V with a silicon diode (heavy-duty, run at fairly high current for stable bias), preferably mounted on the transistor to prevent thermal runaway; alternatives: diode-biased emitter follower (current amplifier), or an op-amp-driven adjustable bias to optimise IMD; the RFC + bypass capacitor keep RF out of the bias network and the RFC must be a low-Q choke | V_bias ~ 0.7 V; RFC low Q | bias topology | class-B PAs | inspect | p.175–176, Figs. 7-8..7-10 | high |
| BOWICK-171 | rf | Class-C self bias: return the base to ground through an RF choke; the base current through rbb' reverse-biases the base-emitter junction, so no external negative supply is needed | base RFC to ground | topology | class-C PAs | inspect | p.176, Figs. 7-11, 7-12 | high |
| BOWICK-172 | components | RF semiconductor selection: Si cheapest; GaAs better for high frequency/high power; Si LDMOS for 100 W-and-up base-station PAs; SiGe for low-power high-frequency front ends (better linearity and power efficiency than GaAs, lower cost); InP for exceptional low noise at mm-wave (> 40 GHz) and higher-frequency PAs (costlier than SiGe); GaN highest power density (many times GaAs/InP) for 100 W+ transmitters but high cost; SiGe HBTs reach several hundred GHz | technology map (Fig. 7-13 graph: power 0.1–1000 W vs 1e7–1e12 Hz) | power, frequency, cost | device technology choice | review | p.126, p.176–177, Fig. 7-13, Table 7-1 | medium |
| BOWICK-173 | components | MMICs (1–300 GHz; GaAs, InP, SiGe; chip ~1–10 mm^2) are cheap in volume but cannot be tuned after design; where low noise is critical a discrete-transistor LNA may outperform a multifunction MMIC | selection rule | NF requirement | microwave front ends | review | p.177 | high |
| BOWICK-174 | filter | On-chip L and C values are limited and element size scales with wavelength, so monolithic LC filters perform poorly; specify FBAR, SAW (or ceramic/crystal/dielectric/YIG) resonator filters for RF front ends; active RC (op-amp) filters are practical mainly at IF | technology rule | frequency | front-end filtering | review | p.177–178 | high |
| BOWICK-175 | rf | Optimum collector load resistance for a required RF output power: RL = (VCC - Vsat)^2/(2*P); the matching network must also absorb the device's shunt output capacitance. Worked: VCC = 12 V, Vsat = 2 V, P = 2 W -> 25 ohm | Eq. 7-2 | VCC, Vsat, P | PA output network when only Cout is given | calc | p.178, Eq. 7-2, Example 7-1 | high |
| BOWICK-176 | rf | Gain-distribution budget for a transmitter chain: pick a final device that handles Pout, then drivers: 15 W out with a 10 dB final needs 1.5 W drive; a 15 dB driver then needs 47 mW from the source/oscillator. Each interstage network transforms the next stage's (low) input impedance up to the load resistance the previous stage needs (e.g. 1.7 - j2.7 ohm up to 25 ohm) while absorbing the previous stage's output capacitance (e.g. 15 pF) | P_in,k = P_out,k / G_k (dB arithmetic) | Pout, stage gains | multistage PAs | calc | p.178–180, Figs. 7-19, 7-20 | high |
| BOWICK-177 | matching | Worked class-C PA match (Example 7-2: MRF233, 15 W, 100 MHz, 50 ohm): input — cancel -j2.7 with +j2.7, L-match 1.7 -> 50 ohm: Q = 5.33, Xs = 9.06 ohm, Xp = 9.38 ohm -> 170 pF shunt, 19 nH series (absorbing the +j2.7); output — cancel -j5.6, L-match 5 -> 50 ohm: Q = 3, Xs = 15 ohm, Xp = 16.7 ohm -> 32.7 nH series (20.6 ohm total), 95.3 pF shunt; supply +12.5 V via 1 uH RFC with 1 uF / 0.01 uF / 0.1 uF bypass and a 310 ohm 1 W resistor (Fig. 7-18) | Eqs. 4-1..4-3 | Zin, Zout, f | PA matching | calc | p.179, Example 7-2, Figs. 7-15..7-18 | high |
| BOWICK-178 | antenna | Antenna radiation resistance at resonance: quarter-wave vertical over a very good ground plane ~35 ohm; half-wave centre-fed dipole ~70 ohm; above resonance the antenna is inductive, below resonance capacitive | Ra(quarter-wave) ~ 35 ohm; Ra(dipole) ~ 70 ohm | antenna type | feedline matching | calc | p.180, Figs. 7-21, 7-22 | high |
| BOWICK-179 | cables | A transmission line presents its characteristic impedance at its input only when terminated in Zo; otherwise the input impedance varies with line length (repeating every half wavelength, where it equals the load resistance) — design antenna matching networks to be tunable (T with tapped inductors + tunable C, or pi with tunable Cs), in the low-pass form for harmonic suppression; if a harmonic spec (e.g. 50 dB below fundamental) applies, design the filter with the Ch.3 method | Zin(l = n*lambda/2) = ZL | line length, ZL, Zo | transmitter-to-antenna feeds | calc | p.180–181, Fig. 7-23 | high |
| BOWICK-180 | protection | Protect PA output transistors against load mismatch (reflected power can cause secondary breakdown): monitor output VSWR (directional/magnetic coupling -> peak detector -> comparator with threshold set) and reduce drive/stage gain when VSWR is excessive | VSWR > threshold -> reduce drive | VSWR | high-power transmitters | measure | p.181, Fig. 7-24 | high |
| BOWICK-181 | magnetics | Broadband (transmission-line) transformer ratios: 1:1 balun — balanced-to-unbalanced, no impedance transformation; 4:1 — input 2V at I/2 into R gives 4R; 9:1 built from two transformers (3V, I/3); 16:1 from three transformers (4V, I/4); dots mark winding polarity. 4:1 from a bifilar 1:1: join lines 2 and 3 as output, ground line 4, line 1 = input | Z_ratio = n^2 for n-conductor voltage stacking (1, 4, 9, 16) | topology | broadband PA matching | calc | p.181–183, Figs. 7-25, 7-26, 7-30 | high |
| BOWICK-182 | rf | Power combining/splitting: two amplifiers operated 180 deg out of phase into a combiner transformer deliver P1 + P2; a transformer splitter nominally divides drive equally, but amplifier input-impedance differences unbalance it — the centre-tap resistor is often omitted to equalise the split | P_out = P1 + P2 | topology | multi-device PAs | measure | p.182, Figs. 7-27, 7-28 | high |
| BOWICK-183 | magnetics | Transmission-line transformer winding: use bifilar/trifilar twisted windings (or coax, which has a defined Zo but cannot be trifilar); winding characteristic impedance should be Zo = sqrt(Rs*RL) (Eq. 7-3), usually found experimentally; tight twists (many turns per inch) for low impedance, untwisted side-by-side for high impedance; wind on low-Q, high-permeability ferrite toroids (permeability needed at the low-frequency end) | Zo_winding = sqrt(Rs*RL) | Rs, RL | broadband transformers | calc | p.182–183, Eq. 7-3, Figs. 7-29, 7-30 | high |
| BOWICK-184 | process | Power-amplifier design is less exact than small-signal design and needs experimentation; the source must supply the required RF drive or the calculated output power will never be achieved | drive margin check | P_drive | PA development | measure | p.183 | high |
| BOWICK-185 | filter | Bowick's Chebyshev prototype values (Tables 3-4..3-7) are normalised to the 3-DB cutoff (w = 1 rad/s at -3 dB), i.e. ripple-normalised g-values x cosh(B), B = (1/n)*acosh(1/eps); Bessel values (Table 3-8) are normalised to 3 dB at 1 rad/s, not unit delay. Scale them with Eqs. 3-12/3-13 using the 3-dB frequency; never mix with ripple- or delay-normalised tables without conversion | g_Bowick = g_ripple * cosh(B) (e.g. 0.1 dB, n = 5: cosh(B) = 1.1347) | ripple, n | prototype-table use | calc | derived from Tables 3-4..3-8 by response simulation (this extraction, Section 2.14a) | medium |
| BOWICK-186 | transmission-line | 50-ohm standardisation exists to match separately designed blocks and test equipment; matched 50-ohm interfaces are needed only where interconnects are long compared to the carrier wavelength — short on-chip/MCM links at GHz need not be 50 ohm, but the chip must present 50 ohm where it drives PCB traces (CMOS makes a 50-ohm input difficult) | require Zo match when l_interconnect is not << lambda | length, f | RF front ends, modules | review | p.186 | medium |
| BOWICK-187 | rf | Double-sideband AM (carrier 900 kHz, 1 kHz tone -> 899 and 901 kHz sidebands) needs twice the information bandwidth and wastes up to 50% of the transmitted power in the redundant sideband; the diode detector has poor power-transfer efficiency; a shunt inductor ahead of the diode acts as an RF choke holding the diode input at DC ground while keeping high RF impedance | BW = 2*f_mod | f_mod | AM detector receivers | calc | p.187–188, Figs. 8-4, 8-5 | high |
| BOWICK-188 | rf | Receiver sensitivity = the smallest input signal giving an acceptable SNR (analog) or BER (digital); selectivity = ability to separate the wanted channel from others and is governed by filter Q; both are primary receiver TPMs | definitions | — | receiver requirements | review | p.188, p.194 | high |
| BOWICK-189 | filter | Tuned-RF (TRF) receivers with a fixed-Q tuned chain have bandwidth BW = f0/Q that grows with tuning: Q = 50 gives 11 kHz at 550 kHz but 33 kHz at 1650 kHz, so selectivity and gain vary across the band and every stage must track (TRF has no image responses) | BW = f0/Q | f0, Q | tunable front ends | calc | p.189, Fig. 8-6 | high |
| BOWICK-190 | rf | Direct-conversion (homodyne, zero-IF) receiver: LO = RF, fixed (higher-Q) RF filter, low-pass after the mixer; digitally modulated signals need I and Q mixers (0/90 deg LO) to keep both sidebands/phase; LO leakage self-mixing and amplifier-mixer mismatches create DC offsets — maximise mixer LO-to-RF isolation; near-zero IF avoids DC but images and distortion beats can fall inside the IF band | architecture rules | — | DCR front ends | review | p.189–190, Fig. 8-7 | high |
| BOWICK-191 | rf | Superheterodyne: LO offset from RF by the IF; the image lies 2*IF from the wanted signal (Fig. 8-11: LO = F + IF, image = F + 2*IF) and must be removed by the preselector/image-reject filter before the mixer; channel filtering is done at IF with fixed filters (switch filters to change bandwidth) because tunable filters cannot hold a constant bandwidth | f_image = f_RF +/- 2*f_IF (sign = LO side) | f_RF, f_IF | superhet front ends | calc | p.190–194, Figs. 8-8, 8-11 | high |
| BOWICK-192 | rf | LO requirements: tuning step no larger than the channel spacing (25-kHz channels are not served by 1-MHz steps); specify SSB phase noise at an offset equal to the channel spacing — close-in phase noise is typically specified at offsets of 1 kHz or less, a 1-MHz-offset figure is insufficient; provide enough LO drive for acceptable mixer conversion loss (add an LO buffer) and include LO power in portable power budgets | step <= channel spacing; L(f_offset = channel spacing) specified | synthesiser data | LO/synthesiser design | review | p.190–191 | high |
| BOWICK-193 | rf | Single-diode mixer insertion loss = sideband conversion loss (nominally 3 dB) + balun losses (~0.75 dB each side) + diode series-resistance loss, i.e. at least ~4.5 dB (sum derived); the input balun/filter must be highly selective so the LO is not radiated back through the RF port and antenna | IL >= 3 + 2*0.75 dB = 4.5 dB | mixer type | passive diode mixers; conf note: high (components) / medium (sum) | calc | p.191 | medium |
| BOWICK-194 | rf | Mixer topology selection: antiparallel diode pair = LO 2nd-harmonic (subharmonic) mixing, simpler IF filtering but more LO power; single-balanced (2 diodes) cancels LO/RF noise at the IF port; double-balanced diode ring = excellent spurious suppression and all-port isolation, higher 1-dB compression, similar conversion loss, much greater dynamic range (higher intercept) but more LO power; active FET/BJT mixers give conversion gain at lower LO drive but distort with excessive LO; Gilbert cell = low power, high gain, wide bandwidth, needs differential signals | selection table | IP3, LO power, isolation | mixer choice | review | p.191–192, Fig. 8-10 | high |
| BOWICK-195 | rf | Mixer IF termination: fIF = fLO +/- fRF (Eq. 8-1); the unwanted sum product reflected from a reflective IF filter re-enters the mixer, mixes with 2*fLO and produces a secondary IF at the IF frequency with different phase (uneven conversion loss) and extra IMD; terminate the IF port in a constant-impedance (absorptive) IF filter — its return loss sets the reflected sum-frequency level | fIF* = 2*fLO - (fLO + fRF) = fIF (printed as +/-[2fLO - (fLO - fRF)], Eq. 8-2) | f_LO, f_RF, filter return loss | mixer IF ports; conf note: high (rule) / medium (Eq. 8-2 form) | inspect | p.192, Eqs. 8-1, 8-2 | medium |
| BOWICK-196 | rf | Two-tone third-order mixer responses occur where fLO = +/-(2*fRF1 - fRF2) and fLO = +/-(2*fRF2 - fRF1) (Eqs. 8-3, 8-4); careful IF-filter-to-mixer impedance matching minimises sum-frequency products and their IMD | Eqs. 8-3, 8-4 | f_LO, f_RF1, f_RF2 | mixer spur analysis | calc | p.192 | high |
| BOWICK-197 | rf | Intermodulation product order = sum of the harmonic multipliers; only odd-order products land near the fundamentals: f1 = 100 kHz, f2 = 101 kHz -> 3rd order 99 and 102 kHz, 5th order 98 and 103 kHz, while even orders fall at 1, 2, 201, 402 kHz (Table 8-1; the prose calls 2f1 + f2 "fourth order" and 3f1 - f2 "fifth order" — the table's classification is the consistent one) | order = \|m\| + \|k\| for m*f1 +/- k*f2 | f1, f2 | spur/IMD planning | calc | p.192–193, Table 8-1 | high |
| BOWICK-198 | rf | Pre-mixer selectivity check: two strong signals inside the preselector bandwidth can produce a third-order product on the tuned channel even when the IF filter rejects each of them — tuned 1000 kHz with 1020 and 1040 kHz present: 2*1020 - 1040 = 1000 kHz (IF filter 2.5 kHz wide). Check every pair of strong signals for 2fa - fb (and 2fb - fa) landing within the channel | \|2fa - fb - f_tuned\| <= BW_ch/2 -> IM3 hit | interferer list | receiver frequency plans | calc | p.193 | high |
| BOWICK-199 | rf | Intercept definitions (Table 8-2): P1dB = level where output deviates 1 dB from linear; IP2/IP3 = extrapolated points where the 2nd/3rd-order products equal the fundamental (products rise 2:1 and 3:1 dB/dB); IIP3 = OIP3 / small-signal gain (IIP3_dBm = OIP3_dBm - G_dB); measure IP3 with two equal-power tones close in frequency | IIP3 = OIP3 - G (dB) | two-tone data | amplifiers, mixers, receivers | measure | p.193, p.195, Table 8-2 | high |
| BOWICK-200 | rf | The output third-order intercept exceeds the actual output 1-dB compression point by as little as 6 dB and as much as 20 dB — treat OIP3 - OP1dB outside 6..20 dB as a data-entry or measurement error flag | 6 dB <= OIP3 - OP1dB <= 20 dB | OIP3, OP1dB | device data sanity | calc | p.195–196 | high |
| BOWICK-201 | rf | Antenna-to-preselector coupling/matching loss adds directly to NF and reduces sensitivity — minimise it; antenna impedance changes with antenna type, environment (buildings, foliage) and frequency, so broadband receivers may need mechanically/electrically tuned matching; include interconnect cable loss in the sensitivity budget | NF += L_match + L_cable (dB, passive) | losses | receive front ends | calc | p.193–194, p.228 | high |
| BOWICK-202 | rf | Split high-selectivity preselection into several filter sections with LNAs between them so filter loss does not dominate NF; the balance of filter loss vs LNA gain sets both selectivity and sensitivity | Friis with lossy filters (F_filter = 10^(IL/10)) | IL, G, NF per stage | superhet front ends | calc | p.194 | high |
| BOWICK-203 | rf | Thermal noise floor: kTB with k = 1.38e-23 J/K (1.38e-20 mW/K), T = 293 K gives 4.057e-21 W in 1 Hz = -174 dBm/Hz; noise power rises with bandwidth (N_dBm = -174 + 10*log(B_Hz) + NF_dB, derived); the final (narrowest) IF filter sets the receiver noise bandwidth — make it as narrow as the channel allows | kTB = -174 dBm/Hz @ 293 K | T, B | sensitivity budgets; conf note: high (constant) / medium (N formula) | calc | p.194–195 | medium |
| BOWICK-204 | rf | Noise factor F = SNR_in/SNR_out (>= 1) and NF = 10*log(F) dB (Eqs. 8-5/8-6 as printed invert the ratio; the case study states the correct input/output order); a noiseless device has NF = 0 dB; a passive lossy device has NF = its insertion loss (1-dB attenuator -> NF = 1 dB) | F = SNR_in/SNR_out; NF_passive = IL | SNRs, IL | all stages | calc | p.194, p.199 | high |
| BOWICK-205 | rf | Cascaded noise (Friis): F_total = F1 + (F2 - 1)/A1 + (F3 - 1)/(A1*A2) + ... + (Fn - 1)/(A1*A2*...*A(n-1)), F = 10^(NF/10), A = 10^(G/10) numeric power gain; two stages NF = 10*log[F1 + (F2 - 1)/A1] (Eq. 8-7 prints the bracket misplaced); the first stage dominates, later stages are suppressed by the preceding gain | Eqs. 8-7, 8-8 | NF_i, G_i | receiver chains | calc | p.194–195, Eqs. 8-7, 8-8 | high |
| BOWICK-206 | rf | Digital-receiver sensitivity is referenced to a BER (GSM: 0.1%) and measured by lowering the input until that BER is reached; MDS = input-referred noise level; SINAD includes harmonics and noise-like distortion | BER-referenced sensitivity | BER target | digital receivers | measure | p.195 | high |
| BOWICK-207 | rf | Any gain reduction raises the input-referred noise floor, so the system SNR needs margin for AGC gain reduction on large signals; attenuation ahead of the LNA improves large-signal handling but adds its loss to NF (1-dB pad -> +1 dB NF) — AGC trades small-signal sensitivity for large-signal handling | NF_new = NF + L_pad (dB, pad first) | AGC range | AGC placement | calc | p.195–196 | high |
| BOWICK-208 | rf | LNA specification set: bandwidth, noise figure, small-signal gain, supply voltage and power consumption, output P1dB, and linearity (IP3 and IP2); SiGe HBT LNAs match or beat GaAs NF/gain up to about 10 GHz | required spec fields | LNA data | LNA selection | review | p.195 | high |
| BOWICK-209 | rf | Dynamic range = MDS to maximum signal; single-channel DR ~= output P1dB - output noise floor; SFDR = input range over which the output exceeds the noise floor while distortion products stay below it; with the 3:1 IM3 slope this gives SFDR = (2/3)*(IIP3 - N_in) dB (derived; N_in = input-referred noise floor, dBm) | DR = OP1dB - N_out; SFDR = 2/3*(IIP3 - N_in) | P1dB, IIP3, N | receiver budgets; conf note: high (definitions) / medium (SFDR formula) | calc | p.195 | medium |
| BOWICK-210 | rf | Multicarrier/OFDM signals have peak power far above average (random carrier phases): peaks drive stages into nonlinearity -> spectral regrowth and adjacent-channel leakage (ACPR); set P1dB from peak, not average, power (Ch.9 example: 16 dBm average OFDM/64QAM needs 21 dBm output P1dB) | OP1dB >= P_avg + PAR | P_avg, PAR | transmit/receive linearity | calc | p.196, p.223 | high |
| BOWICK-211 | rf | Place front-end selectivity as close to the antenna as possible to remove large interferers before active stages; highly selective filters are hard to match and their mismatch degrades the following mixer | filter before first active device | lineup | receiver lineup | review | p.196 | high |
| BOWICK-212 | filter | Filter figures of merit: insertion loss, return loss (VSWR), rejection (measured including IL), ripple, selectivity, group delay, phase response, Q. Specify a bandpass centre arithmetically, f_c = (f_L + f_H)/2 (900/1000 MHz -> 950 MHz), design with the geometric centre; filter Q = f_c/BW_3dB (950–1000 MHz -> 19.5; 500–1000 MHz -> 1.5) | f_c,arith = (fL + fH)/2; Q = f_c/BW | edges | filter specification | calc | p.196 | high |
| BOWICK-213 | filter | Low-Q elements raise passband IL, reduce stopband attenuation and round the response; extra sections add rejection but also IL and complexity; use linear-phase responses for pulsed/OFDM waveforms and equiripple where passband amplitude deviation must be minimum | qualitative trade | element Q, n | filter selection | review | p.196–197 | high |
| BOWICK-214 | hw-fw | ADC resolution by architecture: IF sampling in a double-downconversion IEEE 802.16 (WiMAX) receiver can use a 12-bit ADC; a single-downconversion receiver with a higher IF should use 14 bits to cover its poorer selectivity and avoid saturation by strong interferers; ADC input bandwidth must cover the highest IF; specify SFDR; add an anti-aliasing filter at the ADC input | 12 b (double conv.) / 14 b (single conv.) | architecture | receiver ADC selection | review | p.197 | high |
| BOWICK-215 | hw-fw | Nyquist: sampling rate fs >= 2*f_max of the analog input; a 20-MHz ADC accepts at most 10 MHz, so an FM receiver (88–108 MHz) using it must translate the band to an IF no higher than 10 MHz | fs >= 2*f_max | fs, f_max | ADC/IF planning | calc | p.197 | high |
| BOWICK-216 | hw-fw | ADC driver (buffer) amplifier: rise/fall time and transient response must preserve the modulation, with the amplitude accuracy and flatness to present the optimum level to the ADC; inaccurate RSSI leveling either overdrives the ADC or wastes its dynamic range — hold a constant level into the ADC with VGA-based AGC | level into ADC = target +/- tolerance | RSSI accuracy | IF/baseband chain | measure | p.197, p.200 | high |
| BOWICK-217 | rf | W-CDMA/CDMA receiver numbers (case study): band 1930–1990 MHz (60-MHz allocation); W-CDMA channel bandwidth 3.84 MHz; double superheterodyne (duplexer, LNA, image-reject filter, mixer, IF filters/amp, I/Q demod) with a first IF of 183 MHz; reference sensitivity = minimum antenna input power with BER <= 1e-3; acceptable in-channel noise power -99 dBm -> receiver NF 9 dB (check: -174 + 10*log(3.84e6) + 9 = -99.2 dBm, derived) | Pn = -174 + 10*log(B) + NF | B, NF | cellular receivers; conf note: high (values) / medium (check) | calc | p.197–199, Figs. 8-12..8-14 | medium |
| BOWICK-218 | rf | Adjacent channel selectivity (ACS) = ratio of the receive-filter attenuation on the assigned channel to the attenuation on the adjacent channel (IS-95/IS-98 requirement family together with reference sensitivity and intermodulation/IP3) | ACS definition | filter response | receiver specs | measure | p.199 | high |
| BOWICK-219 | control-loop | Analog AGC/ALC loop: VGA output sampled via a directional coupler into a detector, detector into an op-amp integrator referenced to Vref, integrator output drives the VGA gain control; the loop settles when detector output = Vref, so VGA gain-law errors, nonlinearity and temperature drift drop out — only a monotonic gain-control law is required, but the detector must be temperature-stable at the setpoint; loop dynamic range = the smaller of VGA control range and detector linear range; small integrator RC -> fast settling but envelope ringing, large RC -> stable but slow; use analog loops where digital-AGC latency is unacceptable (the function is really ALC) | V_det = V_ref at equilibrium; tau = R*C | VGA, detector, R, C | IF/RF level control | sim | p.200–201, Fig. 8-15 | high |
| BOWICK-220 | process | RF design dominates system design effort: ~75% of system design time, of which ~25% is design work and ~75% interface, library and integration issues — plan schedules and reuse libraries accordingly | 75% / 25% / 75% | — | project planning | review | p.203 | high |
| BOWICK-221 | process | System-level executable specification: build a behavioural model starting from ideal RF blocks and degrade each block's specs until system performance degrades, to find the tolerable noise, nonlinearity and frequency-domain distortion; the behavioural model + testbench validate the spec and later host mixed-level (transistor-in-system) verification; start with simple models and add effects only when needed | spec derivation by degradation sweep | behavioural models | RF system design | sim | p.208, p.210 | high |
| BOWICK-222 | process | RFIC flow: system design -> circuit design (foundry PDK, time- and frequency-domain simulation) -> layout (critical analog blocks routed manually/full custom) -> parasitic extraction (full-wave 3D EM for VCOs and critical radio blocks; RC-only for insensitive nets, RLC for sensitive nets, RLC + inductor + substrate for the most sensitive) -> full-chip verification in the system testbench | stage gates | — | RFIC development | review | p.208–211, Figs. 9-5, 9-6, 9-9 | high |
| BOWICK-223 | process | Mixed-level block verification in three steps: idealised block model in the system simulation, then the block netlist, then the extracted model; compare netlist vs extracted results to validate the extracted model, then use it for other blocks' mixed-level runs; back-annotate calibrated behavioural models with key performance parameters | 3-step compare | models | RFIC verification | sim | p.211–212 | high |
| BOWICK-224 | emc | Check whether noisy circuits (digital logic, PLLs) couple into sensitive RF circuits; if they do, change the floorplan or add guard bands around the noisy circuitry; analyse mutual inductance between spiral inductors from early placement | isolation review | floorplan | RFIC / mixed-signal layout | inspect | p.210–211 | high |
| BOWICK-225 | test | Use EVM simulations (much faster than BER) at successive test points (mixer out, DC-offset-cancellation out, VGA out, baseband filter out) to find the block that degrades the chain and to verify correct wiring; minimising EVM minimises BER (example: 802.11b DCR, 2547 devices of which 1377 nonlinear, ~10 min minimum run) | EVM per test point | modulated source | receiver/transmitter verification | sim | p.212–213, Figs. 9-10, 9-11 | high |
| BOWICK-226 | rf | Simulator choice for mixers/DCRs: Harmonic Balance needs one large-signal tone per LO and RF tone (3 for LO + two RF tones; 2 if (Flo - Frf1) is an integer multiple of (Frf1 - Frf2)); Circuit Envelope needs only the LO as a large-signal tone, with envelope bandwidth = 1/(time step) around each tone and baseband tones up to 0.5/(time step) generated automatically; time-domain simulators are inefficient for an LO plus near-DC baseband (example: RF 2.44875 and 2.44900 GHz, LO 2.45 GHz, ~4.5 min) | BW_env = 1/dt | tones, dt | RF simulation setup | sim | p.213–214, Figs. 9-12, 9-13 | high |
| BOWICK-227 | components | Spiral-inductor models must predict Q and self-resonance: include frequency-dependent resistance (top metal a few microns thick/wide ~ one skin depth at GHz -> current crowding raises R, lowers Q), frequency-dependent (falling) internal inductance, substrate loss (a ground shield under the spiral reduces it), an explicit ground-return assumption (inductance is defined only for a loop), inter-turn capacitance, and the underpass; frequency-dependent R/L models exported to SPICE can become nonphysical (example model: 13 physical parameters, NS = 15, W = 10 um, S = 5 um) | model checklist | layout geometry | RFIC passives | sim | p.214–216, Figs. 9-14, 9-15 | high |
| BOWICK-228 | components | An RF model library should contain corner cases, statistical models, digital/analog mismatch models, pad models with RF ESD, flicker-noise models, substrate-resistance models, and well-proximity and shallow-trench-isolation stress effects; foundry kits with only corner-case models may be unsuitable for RF | library checklist | PDK contents | PDK qualification | review | p.215 | high |
| BOWICK-229 | dfm | PCB flow: specification -> schematic capture (library parts with correct package and silkscreen) -> netlist -> layout with DFM, signal-integrity and EMI/EMC restrictions written into the design rules (track width, spacing, pad sizes, via sizes, routing types) -> placement (thermal spacing, short critical signals) -> constraint-driven routing (80–90% or more of signals are critical) -> DRC against netlist and rules -> cleanup -> verification -> prototype/production (ODB++ data) | flow gates | — | PCB development | review | p.216–217, Fig. 9-16 | high |
| BOWICK-230 | rf | On RF transmitter/receiver PCBs, minimise layout parasitics or model them (SPICE); many practical circuits can be analysed with a simple lumped-element model | parasitic modelling | layout | RF PCBs | sim | p.217 | high |
| BOWICK-231 | mechanical | RF packaging: few I/Os at high frequency; at GHz, interconnect dispersion, radiation loss, resonance, skin effect and conductor surface roughness affect performance, so package interconnects need 3D EM models; choose the packaging strategy during design (reliability, manufacturability, RF performance, size, cost), never as an afterthought | EM-model package paths | package | RF modules/ICs | sim | p.218–219 | high |
| BOWICK-232 | materials | Package/substrate options: ceramics are hermetic and robust (space, military); thin film gives the smallest features, thick film can print resistors and inductors; LTCC multilayer for high integration/reliability; HTCC alumina standard; aluminium nitride for thermal performance; HiTCE ceramics for CTE matched to PCB; low-k ceramics permit larger features and lower delay; hybrid laminates (FR4 core with RF materials on selected layers) are low-cost GHz substrates; SiP/stacked-die (2–4 die) when X-Y area is the constraint | material selection | requirements | RF packaging | review | p.217–219 | high |
| BOWICK-233 | rf | 802.11a CMOS LNA reference (0.18-um CMOS, 5.15–5.825 GHz): differential cascode common-source; device width ~160 um (NR = 64), fT ~44 GHz, 14 mA bias; NF 1.2 dB over 4–6 GHz (1.1 dB at 5.2 GHz), gain 20 dB, S11 -20 to -30 dB into 100-ohm differential; inductive source degeneration provides the real input resistance and a series input inductor (high Q to minimise NF) resonates the gate capacitance; drain load inductor Q low enough to cover 5.15–5.85 GHz; output not matched (drives on-chip I/Q demodulator); K > 1 in and out of band; avoid capacitance at the differential-pair source (negative resistance); P1dB -10 dBm, IP3 > 10 dBm | reference values | — | CMOS LNA design | sim | p.220–221, Fig. 9-21 | high |
| BOWICK-234 | rf | 802.11a Gilbert-cell down-converter reference: conversion gain ~6 dB (set by bias and load resistor), simulated NF 5 dB (flagged as possibly missing noise sources), source-degeneration inductors improve linearity, input P1dB ~ -10 dBm; simulate LO-IF and LO-RF isolation by deliberately mismatching the RF and LO switching pairs | reference values | — | CMOS mixers | sim | p.221–222, Fig. 9-22 | high |
| BOWICK-235 | rf | Transmit chain back-off: up-converter P1dB set 10 dB above its operating level (input P1dB 8 dBm with <= -2 dBm drive); system simulation showed 8 dB back-off from P1dB needed for no BER degradation with the PA at 4–5 dB back-off; summing the I and Q paths selects the lower sideband, subtracting selects the upper; up-converter conversion loss ~5 dB at 10 dBm differential LO (NF ~1.5 dB flagged as not simulating correctly) | back-off >= 8 dB (mixer), 4–5 dB (PA) for OFDM/64QAM | P1dB, drive | OFDM transmitters | sim | p.222–223, Fig. 9-23 | high |
| BOWICK-236 | rf | 802.11a CMOS PA reference (5.18–5.26 GHz, two-stage common source): 40 mW (16 dBm) average but 21 dBm required output P1dB for OFDM/64QAM; designed for 22–23 dBm to allow for loss; 22-ohm load for 23 dBm from 3 V (consistent with Eq. 7-2 at Vsat ~ 0: 3^2/(2*0.2 W) = 22.5 ohm); larger 960 um/0.18 um output device (480 um first stage) for linearity and gain; class-A bias (Vgs - Vth > 0.1 V); stabilise before matching (small source inductance = bond wire, small gate resistor) to K > 2 in band; high-pass L-matches with DC blocks to 50 ohm, re-checked vs drive level (large-signal impedance); results: LSS21 21 dB, input P1dB 3 dBm (output 22.6 dBm), OIP3 ~40 dBm, IM3 ~33 dBc at 18 dBm, PAE ~27% at P1dB, S11/S22 < -25 dB; 22.6 dBm P1dB gives > 6 dB peak-to-average headroom vs a 5 dB target | reference values | — | CMOS PA design | sim | p.223–225, Fig. 9-24 | high |
| BOWICK-237 | rf | Frequency-band designations and wavelengths (Table A1): VLF 3–30 kHz (100–10 km), LF 30–300 kHz (10–1 km), MF 0.3–3 MHz (1–0.1 km), HF 3–30 MHz (100–10 m), VHF 30–300 MHz (10–1 m), UHF 300–3000 MHz (100–10 cm), SHF 3–30 GHz (10–1 cm, "microwave"), EHF 30–300 GHz (10–1 mm, "millimetre-wave"); notable allocations: 2450 MHz (WLAN, Bluetooth, microwave ovens), 12 and 18 GHz (DBS), 77 GHz (automotive radar) | lambda = c/f | f | band naming | calc | p.227, Table A1 | high |
| BOWICK-238 | antenna | Antenna coupling network: on receive, achieve the lowest possible loss (loss degrades NF and sensitivity; include cable loss); on transmit, maximise radiated power from the transmitter | receive: min loss; transmit: max radiated power | network loss | antenna interfaces | calc | p.227–228 | high |
| BOWICK-239 | components | MEMS RF switches achieve very high off-state isolation through physical separation of the switch ports; MEMS variable capacitors give a mechanically-trimmer-like tuning range under programmable control — candidates for switched/tunable preselectors, IF filters and tunable antenna/amplifier matching (early adoption stage in 2008) | qualitative | — | reconfigurable front ends | review | p.108–109 | medium |
| BOWICK-240 | components | Device class selection: BJTs switch fast and handle large currents/power; FETs are preferred for weak-signal amplification and high circuit impedance (MOSFET input impedance extremely high); SiGe HBTs reach several hundred GHz and integrate with CMOS | qualitative selection | application | active device choice | review | p.126 | medium |
| BOWICK-241 | magnetics | A high-permeability toroid needs far fewer turns than an air-core coil: 35 uH takes 8 turns on a mu_i = 2500 toroid versus 90 turns on a 1/4-inch air-core form wound for optimum Q (fewer turns = less AC resistance, higher Q) | N = sqrt(L/AL) | L, AL | inductor form selection | calc | p.11, Fig. 1-21 | high |

## 2. Formulas & tables (numbers)

### 2.1 Table 1-1 — AWG wire chart (p.10)

1 mil = 2.54e-3 cm. "Coated" = enamel-coated diameter. Resistance is copper, ohms per 1000 ft. Area in circular mils.

| AWG | dia bare (mil) | dia coated (mil) | ohm/1000 ft | area (circ. mil) |
|---|---|---|---|---|
| 1 | 289.3 | — | 0.124 | 83690 |
| 2 | 257.6 | — | 0.156 | 66360 |
| 3 | 229.4 | — | 0.197 | 52620 |
| 4 | 204.3 | — | 0.249 | 41740 |
| 5 | 181.9 | — | 0.313 | 33090 |
| 6 | 162.0 | — | 0.395 | 26240 |
| 7 | 144.3 | — | 0.498 | 20820 |
| 8 | 128.5 | 131.6 | 0.628 | 16510 |
| 9 | 114.4 | 116.3 | 0.793 | 13090 |
| 10 | 101.9 | 104.2 | 0.999 | 10380 |
| 11 | 90.7 | 93.5 | 1.26 | 8230 |
| 12 | 80.8 | 83.3 | 1.59 | 6530 |
| 13 | 72.0 | 74.1 | 2.00 | 5180 |
| 14 | 64.1 | 66.7 | 2.52 | 4110 |
| 15 | 57.1 | 59.5 | 3.18 | 3260 |
| 16 | 50.8 | 52.9 | 4.02 | 2580 |
| 17 | 45.3 | 47.2 | 5.05 | 2050 |
| 18 | 40.3 | 42.4 | 6.39 | 1620 |
| 19 | 35.9 | 37.9 | 8.05 | 1290 |
| 20 | 32.0 | 34.0 | 10.1 | 1020 |
| 21 | 28.5 | 30.2 | 12.8 | 812 |
| 22 | 25.3 | 27.0 | 16.2 | 640 |
| 23 | 22.6 | 24.2 | 20.3 | 511 |
| 24 | 20.1 | 21.6 | 25.7 | 404 |
| 25 | 17.9 | 19.3 | 32.4 | 320 |
| 26 | 15.9 | 17.2 | 41.0 | 253 |
| 27 | 14.2 | 15.4 | 51.4 | 202 |
| 28 | 12.6 | 13.8 | 65.3 | 159 |
| 29 | 11.3 | 12.3 | 81.2 | 123 |
| 30 | 10.0 | 11.0 | 104.0 | 100 |
| 31 | 8.9 | 9.9 | 131 | 79.2 |
| 32 | 8.0 | 8.8 | 162 | 64.0 |
| 33 | 7.1 | 7.9 | 206 | 50.4 |
| 34 | 6.3 | 7.0 | 261 | 39.7 |
| 35 | 5.6 | 6.3 | 331 | 31.4 |
| 36 | 5.0 | 5.7 | 415 | 25.0 |
| 37 | 4.5 | 5.1 | 512 | 20.2 |
| 38 | 4.0 | 4.5 | 648 | 16.0 |
| 39 | 3.5 | 4.0 | 847 | 12.2 |
| 40 | 3.1 | 3.5 | 1080 | 9.61 |
| 41 | 2.8 | 3.1 | 1320 | 7.84 |
| 42 | 2.5 | 2.8 | 1660 | 6.25 |
| 43 | 2.2 | 2.5 | 2140 | 4.84 |
| 44 | 2.0 | 2.3 | 2590 | 4.00 |
| 45 | 1.76 | 1.9 | 3350 | 3.10 |
| 46 | 1.57 | 1.7 | 4210 | 2.46 |
| 47 | 1.40 | 1.6 | 5290 | 1.96 |
| 48 | 1.24 | 1.4 | 6750 | 1.54 |
| 49 | 1.11 | 1.3 | 8420 | 1.23 |
| 50 | 0.99 | 1.1 | 10600 | 0.98 |

### 2.2 Component-level formulas (Ch.1)

| quantity | formula (ASCII) | units / notes | source |
|---|---|---|---|
| Copper skin depth anchors | delta = 0.85 cm @ 60 Hz; 0.007 cm @ 1 MHz | 1/e (37%) current-density depth | p.1 |
| Straight wire inductance | L_uH = 0.002*l*(2.3*log10(4*l/d) - 0.75) | l, d in cm | Eq. 1-1, p.2 |
| Parallel-plate capacitance | C_pF = 0.2249*k*A/d | A in^2, d in; k = eps/eps0; eps0 = 8.854e-12 F/m | Eq. 1-2, p.4 |
| Capacitor ESR | ESR = PF*1e6/(w*C) | w = 2*pi*f; PF = cos(phi); (1e6 factor => C in uF) | p.5 |
| Dissipation factor | DF = ESR/Xc * 100% | Xc = 1/(w*C) | p.5 |
| Capacitor Q | Q = 1/DF = Xc/ESR | — | p.5 |
| Series resonance of a real capacitor | Fr = 1/(2*pi*sqrt(L_lead*C)) | inductive above Fr | p.5, Fig. 1-9 |
| Inductor Q | Q = X_L/Rs = w*L/Rs | Rs = winding series resistance | Eq. 1-11, p.9 |
| Single-layer air-core solenoid | L_uH = 0.394*r^2*N^2/(9*r + 10*l) | r, l cm; l > 0.67*r; +/-1% | Eq. 1-8, p.9 |
| Turns for optimum-Q coil (l = 2r) | N = sqrt(29*L_uH/(0.394*r)) | r cm | Example 1-5, p.9 |
| Permeability | mu = B/H | Wb/(A-turn) | Eq. 1-9, p.12 |
| Operating flux density | Bop_G = E*1e8/(4.44*f*N*Ae) | E rms V, f Hz, N turns, Ae cm^2 | Eq. 1-10, p.12 |
| Toroid inductance | L_nH = 0.4*pi*N^2*mu_i*Ac*1e-2/le | Ac cm^2, le cm | Eq. 1-12, p.19 |
| Inductance index | L_nH = N^2*AL; N = sqrt(L_nH/AL) | AL nH/turn^2; AL[uH/100 t]/10 = AL[nH/t^2] | Eqs. 1-13, 1-14, p.19/21 |
| Core-data Q | Q = (Rp/N^2)/(Xp/N^2) | from vendor curves | Eq. 1-15, p.19 |
| Max single-layer toroid wire | d_in = 2*pi*r1/(N + pi), then x0.9 | r1 inner radius (in) | Eq. 1-15(b), p.20 |

Dielectric constants (Fig. 1-7, p.4): air 1; polystyrene 2.5; paper 4; mica 5; ceramic low-K 10; ceramic high-K 100–10,000.

Capacitor temperature classes (Fig. 1-11, p.6–7): NPO/temperature-compensating TC = +150 to -4700 ppm/degC, tolerance to +/-15 ppm/degC (axis -55 to +125 degC); moderately stable +/-15% (nonlinear); general-purpose high-K up to -80%; silvered mica +20 ppm/degC (-60 to +89 degC); film +/-2% over temperature; polystyrene max +85 degC.

Chip inductors (p.8): 0.01 uH – 1.0 mH, Q 40–60 at 200 MHz.

### 2.3 Table 1-3 — Powdered-iron core materials (p.19)

| material | Q / frequency range | use / cost |
|---|---|---|
| Carbonyl C | medium Q at 150 kHz | AM tuning, low-frequency IF transformers; high cost |
| Carbonyl E | high Q, medium permeability, 1–30 MHz | IF transformers, antenna coils, general purpose; medium cost; most widely used |
| Carbonyl J | high Q at 40–100 MHz, medium permeability | FM and TV; high cost |
| Carbonyl SF | like E but better Q up to 50 MHz | costs more than E |
| Carbonyl TH | Q higher than E up to 30 MHz, below SF | higher cost than E |
| Carbonyl W | high Q to 100 MHz, medium permeability | highest cost |
| Carbonyl HP | good Q and excellent stability to 50 kHz | low-frequency |
| Carbonyl GS6 | good stability, high Q | commercial broadcast frequencies |
| IRN-8 | good Q 50–150 MHz (synthetic oxide, hydrogen-reduced) | FM and TV; medium price (Amidon material No. 12) |

Toroid core symbols (Table 1-2, p.19): Ac available winding cross-section (cm^2); Ae effective core area (cm^2); AL inductive index (nH/turn^2); Bsat saturation flux density (gauss); Bop operating flux density (gauss); le effective flux-path length (cm); mu_i initial permeability (numeric).

### 2.4 Resonant-circuit formulas (Ch.2)

| quantity | formula | source |
|---|---|---|
| Loaded Q from response | Q = fc/(f2 - f1) (3-dB points) | Eq. 2-1, p.24 |
| Shape factor | SF = BW_60dB/BW_3dB (>= 1) | p.24 |
| RC low-pass loss | Vout/Vin(dB) = 20*log(Xc/(Rs + Xc)) (complex magnitudes) | Eq. 2-3, p.24 |
| RL high-pass loss | Vout/Vin(dB) = 20*log(XL/(Rs + XL)) | Eq. 2-4, p.25 |
| Parallel LC across source | Vout/Vin = jwL/((Rs - w^2*Rs*L*C) + jwL) | Eq. 2-5 derivation, p.26 |
| Loaded Q (lossless) | Q = Rp/Xp, Rp = Rs\|\|RL, Xp = w0*L = 1/(w0*C) | Eq. 2-6, p.27 |
| Series-to-parallel (exact) | Rp = (Q^2 + 1)*Rs; Xp = Rp/Qp; Qs = Qp = Q | Eqs. 2-7, 2-8, p.28 |
| Series-to-parallel (Q > 10) | Rp ~= Q^2*Rs; Xp ~= Xs | Eqs. 2-9, 2-10, p.28 |
| Tapped-C transformer | Rs' = Rs*(1 + C1/C2)^2; CT = C1*C2/(C1 + C2) | Eqs. 2-13, 2-14, p.31 |
| Tapped-L transformer | Rs' = Rs*(n/n1)^2 (superscript lost in extraction) | Eq. 2-15, p.31 |
| Critical coupling, top-C | C12 = C/Q | Eq. 2-19, p.32 |
| Critical coupling, top-L | L12 = Q*L | Eq. 2-20, p.34 |
| Two critically coupled resonators | Q_total = 0.707*Q_resonator | p.32 |
| Actively coupled n resonators | Q_total = Q/sqrt(2^(1/n) - 1) | Eq. 2-21, p.34 |

### 2.5 Filter formulas (Ch.3)

| quantity | formula | source |
|---|---|---|
| 2-element LP resonance | Fr = 1/(2*pi*sqrt(L*C)) | Eq. 3-1, p.38 |
| 2-element LP Qs | Q1 = XL/Rs; Q2 = RL/Xc; Q_total = Q1*Q2/(Q1 + Q2) | Eqs. 3-2..3-4, p.38 |
| Passband peaks | N - 1 (N = elements, loaded Q > 1) | p.38 |
| Butterworth attenuation | A_dB = 10*log(1 + (w/wc)^(2n)) | Eq. 3-5, p.40 |
| Butterworth equal-termination elements | A_k = 2*sin((2k - 1)*pi/(2n)), k = 1..n | Eq. 3-6, p.41 |
| Chebyshev attenuation | A_dB = 10*log(1 + eps^2*Cn^2(w'/wc)) | Eq. 3-7, p.44 |
| Chebyshev ripple factor | eps = sqrt(10^(R_dB/10) - 1) | Eq. 3-8, p.44 |
| Chebyshev B | B = (1/n)*acosh(1/eps) | Eq. 3-9, p.44 |
| Chebyshev frequency correction | w'/wc = (w/wc)*cosh(B) | Eq. 3-10, p.44 |
| Hyperbolics | cosh(x) = 0.5*(e^x + e^-x); acosh(x) = ln(x + sqrt(x^2 - 1)) | p.45 |
| Bessel initial attenuation | A_dB ~= 3*(w/wc)^2 (valid w/wc <= 2; beyond: 6 dB/oct/element) | Eq. 3-11, p.48 |
| LP scaling | C = Cn/(2*pi*fc*R); L = R*Ln/(2*pi*fc); Rs = Rs_norm*RL | Eqs. 3-12, 3-13, p.50 |
| HP transform | L_hp = 1/C_lp; C_hp = 1/L_lp; terminations unchanged; then scale | p.53–55 |
| BP bandwidth mapping | BW/BWc = f/fc (BWc = 3-dB bandwidth) | Eq. 3-14, p.59 |
| Geometric centre | f0 = sqrt(fa*fb) (fa, fb equal-attenuation frequencies) | Eq. 3-15, p.59 |
| BP scaling, parallel (shunt) branches | C = Cn/(2*pi*R*B); L = R*B/(2*pi*f0^2*Ln) | Eqs. 3-16, 3-17, p.60 |
| BP scaling, series branches | C = B/(2*pi*f0^2*Cn*R); L = R*Ln/(2*pi*B) | Eqs. 3-18, 3-19, p.60 |
| BR bandwidth mapping | BWc/BW = (f4 - f1)/(f3 - f2), substituted for fc/f | p.60 |
| BR scaling, series-resonant (shunt) circuits | C = Cn/(2*pi*R*B); L = R*B/(2*pi*f0^2*Ln) | Eqs. 3-20, 3-21, p.60 |
| BR scaling, parallel-resonant (series) circuits | C = B/(2*pi*f0^2*R*Cn); L = R*Ln/(2*pi*B) | Eqs. 3-22, 3-23, p.60 |

(In the BP/BR scaling formulas R = final load resistance, B = final 3-dB bandwidth (Hz), f0 = geometric centre (Hz), Ln/Cn = the normalised prototype value of that branch — both elements of each resonator carry the same normalised value.)

Correction (this extraction, verified by simulation — see BOWICK-099): the printed BR Eqs. 3-20..3-23 repeat the BP forms and give a stopband ~f0^2/B wide when fed low-pass values g. Use instead: shunt series-resonant branch (from LP shunt C = g): L = R/(2*pi*g*B), C = g*B/(2*pi*f0^2*R); series parallel-resonant branch (from LP series L = g): L = g*R*B/(2*pi*f0^2), C = 1/(2*pi*g*R*B). The BP Eqs. 3-16..3-19 are correct (Example 3-9 network simulates to -3 dB at 71.76/78.76 MHz = 7.00 MHz).

### 2.6 Table 3-3 — Chebyshev polynomials Cn(x), x = w/wc (p.44)

| n | Cn(x) |
|---|---|
| 1 | x |
| 2 | 2x^2 - 1 |
| 3 | 4x^3 - 3x |
| 4 | 8x^4 - 8x^2 + 1 |
| 5 | 16x^5 - 20x^3 + 5x |
| 6 | 32x^6 - 48x^4 + 18x^2 - 1 |
| 7 | 64x^7 - 112x^5 + 58x^3 - 7x (printed "58"; the recurrence C7 = 2x*C6 - C5 gives 56 — use 64x^7 - 112x^5 + 56x^3 - 7x) |

### 2.7 Butterworth attenuation vs f/fc (computed from Eq. 3-5; Fig. 3-9 graph equivalent)

A_dB = 10*log10(1 + (f/fc)^(2n)). Columns n = 2..7.

| f/fc | n=2 | n=3 | n=4 | n=5 | n=6 | n=7 |
|---|---|---|---|---|---|---|
| 1.5 | 7.8 | 10.9 | 14.3 | 17.7 | 21.2 | 24.7 |
| 2 | 12.3 | 18.1 | 24.1 | 30.1 | 36.1 | 42.1 |
| 2.5 | 16.0 | 23.9 | 31.8 | 39.8 | 47.8 | 55.7 |
| 3 | 19.1 | 28.6 | 38.2 | 47.7 | 57.3 | 66.8 |
| 3.5 | 21.8 | 32.6 | 43.5 | 54.4 | 65.3 | 76.2 |
| 4 | 24.1 | 36.1 | 48.2 | 60.2 | 72.2 | 84.3 |
| 5 | 28.0 | 41.9 | 55.9 | 69.9 | 83.9 | 97.9 |
| 6 | 31.1 | 46.7 | 62.3 | 77.8 | 93.4 | 108.9 |
| 7 | 33.8 | 50.7 | 67.6 | 84.5 | 101.4 | 118.3 |
| 8 | 36.1 | 54.2 | 72.2 | 90.3 | 108.4 | 126.4 |
| 9 | 38.2 | 57.3 | 76.3 | 95.4 | 114.5 | 133.6 |
| 10 | 40.0 | 60.0 | 80.0 | 100.0 | 120.0 | 140.0 |

(Book anchors: n = 5 at f/fc = 2 -> ~30 dB; n = 6 at 3 -> ~57 dB; n = 5 at 3 -> ~47 dB; n = 7 needed for 60 dB at 3. conf = high for the formula; table values are computed.)

### 2.7a Chebyshev attenuation vs f/fc (computed from Eqs. 3-7..3-10; replaces graphs Figs. 3-15..3-18)

A_dB = 10*log10(1 + eps^2*Cn^2((f/fc)*cosh(B))), eps = sqrt(10^(R_dB/10) - 1), B = (1/n)*acosh(1/eps); fc = 3-dB cutoff (the book's curves start at f/fc = 1 = 3 dB). Book anchors reproduced: 0.1 dB n = 5 at 3 -> 60.0 dB ("about 60 dB", p.53); 0.5 dB n = 5 at 2 -> 44.9 dB (>= 40 dB, Example 3-7); 1 dB n = 3 at 5 -> 50.3 dB ("about 50 dB", Example 3-9); 2.5 dB n = 4 at 2.5 -> 47.63 dB (Example 3-3). conf = medium (computed).

0.01-dB ripple:

| f/fc | n=2 | n=3 | n=4 | n=5 | n=6 | n=7 |
|---|---|---|---|---|---|---|
| 1.5 | 8.0 | 12.1 | 17.2 | 23.2 | 29.7 | 36.7 |
| 2 | 12.6 | 19.7 | 28.0 | 37.2 | 46.9 | 57.0 |
| 2.5 | 16.4 | 25.7 | 36.2 | 47.5 | 59.4 | 71.8 |
| 3 | 19.5 | 30.5 | 42.7 | 55.8 | 69.4 | 83.5 |
| 4 | 24.5 | 38.1 | 52.9 | 68.6 | 84.9 | 101.5 |
| 5 | 28.4 | 43.9 | 60.8 | 78.4 | 96.7 | 115.4 |
| 6 | 31.5 | 48.7 | 67.1 | 86.4 | 106.3 | 126.6 |
| 8 | 36.5 | 56.2 | 77.2 | 99.0 | 121.4 | 144.2 |
| 10 | 40.4 | 62.1 | 85.0 | 108.7 | 133.1 | 157.9 |

0.1-dB ripple:

| f/fc | n=2 | n=3 | n=4 | n=5 | n=6 | n=7 |
|---|---|---|---|---|---|---|
| 1.5 | 8.4 | 13.4 | 19.6 | 26.5 | 33.8 | 41.4 |
| 2 | 13.2 | 21.5 | 31.0 | 41.1 | 51.6 | 62.3 |
| 2.5 | 17.1 | 27.6 | 39.3 | 51.6 | 64.3 | 77.3 |
| 3 | 20.2 | 32.5 | 45.9 | 60.0 | 74.4 | 89.1 |
| 4 | 25.3 | 40.2 | 56.2 | 72.9 | 90.0 | 107.2 |
| 5 | 29.2 | 46.1 | 64.1 | 82.8 | 101.8 | 121.1 |
| 6 | 32.3 | 50.9 | 70.5 | 90.8 | 111.5 | 132.4 |
| 8 | 37.3 | 58.4 | 80.6 | 103.4 | 126.6 | 150.0 |
| 10 | 41.2 | 64.2 | 88.4 | 113.2 | 138.3 | 163.7 |

0.5-dB ripple:

| f/fc | n=2 | n=3 | n=4 | n=5 | n=6 | n=7 |
|---|---|---|---|---|---|---|
| 1.5 | 9.1 | 15.2 | 22.3 | 29.9 | 37.8 | 45.8 |
| 2 | 14.2 | 23.7 | 34.1 | 44.9 | 55.9 | 67.0 |
| 2.5 | 18.2 | 30.0 | 42.6 | 55.6 | 68.8 | 82.1 |
| 3 | 21.5 | 35.0 | 49.4 | 64.0 | 78.9 | 93.9 |
| 4 | 26.6 | 42.8 | 59.7 | 77.0 | 94.5 | 112.2 |
| 5 | 30.5 | 48.7 | 67.6 | 87.0 | 106.5 | 126.1 |
| 6 | 33.7 | 53.5 | 74.1 | 95.0 | 116.1 | 137.3 |
| 8 | 38.7 | 61.1 | 84.2 | 107.6 | 131.2 | 155.0 |
| 10 | 42.6 | 66.9 | 91.9 | 117.3 | 142.9 | 168.6 |

1.0-dB ripple:

| f/fc | n=2 | n=3 | n=4 | n=5 | n=6 | n=7 |
|---|---|---|---|---|---|---|
| 1.5 | 9.7 | 16.4 | 23.9 | 31.8 | 39.9 | 48.0 |
| 2 | 15.0 | 25.1 | 35.9 | 47.0 | 58.1 | 69.4 |
| 2.5 | 19.1 | 31.5 | 44.5 | 57.7 | 71.1 | 84.5 |
| 3 | 22.4 | 36.5 | 51.3 | 66.2 | 81.3 | 96.4 |
| 4 | 27.5 | 44.3 | 61.7 | 79.2 | 96.9 | 114.6 |
| 5 | 31.4 | 50.3 | 69.6 | 89.1 | 108.8 | 128.6 |
| 6 | 34.6 | 55.1 | 76.0 | 97.2 | 118.5 | 139.8 |
| 8 | 39.7 | 62.6 | 86.1 | 109.8 | 133.6 | 157.5 |
| 10 | 43.5 | 68.5 | 93.9 | 119.6 | 145.3 | 171.1 |

### 2.7b Bessel attenuation vs f/fc (computed by simulating the Table 3-8 Rs = RL rows; replaces graph Fig. 3-20)

Relative to DC. The book's approximation A_dB ~= 3*(f/fc)^2 (Eq. 3-11, valid to f/fc ~ 2, then 6 dB/octave per element) is consistent with these values. conf = medium (computed).

| f/fc | n=2 | n=3 | n=4 | n=5 | n=6 | n=7 |
|---|---|---|---|---|---|---|
| 1.0 | 3.0 | 3.0 | 3.0 | 3.0 | 3.0 | 3.0 |
| 1.5 | 6.4 | 7.1 | 7.4 | 7.4 | 7.3 | 7.2 |
| 2 | 9.8 | 12.0 | 13.4 | 14.1 | 14.2 | 14.0 |
| 2.5 | 13.0 | 16.7 | 19.5 | 21.4 | 22.5 | 23.0 |
| 3 | 15.7 | 20.9 | 25.1 | 28.3 | 30.7 | 32.3 |
| 4 | 20.4 | 27.8 | 34.4 | 40.0 | 44.7 | 48.6 |
| 5 | 24.1 | 33.4 | 41.9 | 49.4 | 55.9 | 61.7 |
| 6 | 27.2 | 38.1 | 48.1 | 57.1 | 65.3 | 72.6 |
| 8 | 32.1 | 45.5 | 58.0 | 69.5 | 80.1 | 89.9 |
| 10 | 35.9 | 51.2 | 65.7 | 79.1 | 91.6 | 103.4 |

### 2.8 Table 3-1 — Butterworth low-pass prototype, equal terminations Rs = RL = 1 (p.41)

Element order C1, L2, C3, ... (schematic above table: first element shunt C) or L1, C2, L3, ... (schematic below: first element series L). Values are symmetric.

| n | A1 | A2 | A3 | A4 | A5 | A6 | A7 |
|---|---|---|---|---|---|---|---|
| 2 | 1.414 | 1.414 | | | | | |
| 3 | 1.000 | 2.000 | 1.000 | | | | |
| 4 | 0.765 | 1.848 | 1.848 | 0.765 | | | |
| 5 | 0.618 | 1.618 | 2.000 | 1.618 | 0.618 | | |
| 6 | 0.518 | 1.414 | 1.932 | 1.932 | 1.414 | 0.518 | |
| 7 | 0.445 | 1.247 | 1.802 | 2.000 | 1.802 | 1.247 | 0.445 |

### 2.9 Tables 3-2A/B — Butterworth low-pass prototype, unequal terminations (pp.42–43)

Reading rule: with Rs/RL use schematic above (C1 shunt first) reading down; with RL/Rs use schematic below (L1 series first) reading up (i.e. the same numbers apply to L1, C2, L3, ... for ratio RL/Rs). "inf" = infinite ratio (ideal current-source drive / open-circuit termination).

Table 3-2A (n = 2, 3, 4):

| n | Rs/RL | C1 | L2 | C3 | L4 |
|---|---|---|---|---|---|
| 2 | 1.111 | 1.035 | 1.835 | | |
| 2 | 1.250 | 0.849 | 2.121 | | |
| 2 | 1.429 | 0.697 | 2.439 | | |
| 2 | 1.667 | 0.566 | 2.828 | | |
| 2 | 2.000 | 0.448 | 3.346 | | |
| 2 | 2.500 | 0.342 | 4.095 | | |
| 2 | 3.333 | 0.245 | 5.313 | | |
| 2 | 5.000 | 0.156 | 7.707 | | |
| 2 | 10.000 | 0.074 | 14.814 | | |
| 2 | inf | 1.414 | 0.707 | | |
| 3 | 0.900 | 0.808 | 1.633 | 1.599 | |
| 3 | 0.800 | 0.844 | 1.384 | 1.926 | |
| 3 | 0.700 | 0.915 | 1.165 | 2.277 | |
| 3 | 0.600 | 1.023 | 0.965 | 2.702 | |
| 3 | 0.500 | 1.181 | 0.779 | 3.261 | |
| 3 | 0.400 | 1.425 | 0.604 | 4.064 | |
| 3 | 0.300 | 1.838 | 0.440 | 5.363 | |
| 3 | 0.200 | 2.669 | 0.284 | 7.910 | |
| 3 | 0.100 | 5.167 | 0.138 | 15.455 | |
| 3 | inf | 1.500 | 1.333 | 0.500 | |
| 4 | 1.111 | 0.466 | 1.592 | 1.744 | 1.469 |
| 4 | 1.250 | 0.388 | 1.695 | 1.511 | 1.811 |
| 4 | 1.429 | 0.325 | 1.862 | 1.291 | 2.175 |
| 4 | 1.667 | 0.269 | 2.103 | 1.082 | 2.613 |
| 4 | 2.000 | 0.218 | 2.452 | 0.883 | 3.187 |
| 4 | 2.500 | 0.169 | 2.986 | 0.691 | 4.009 |
| 4 | 3.333 | 0.124 | 3.883 | 0.507 | 5.338 |
| 4 | 5.000 | 0.080 | 5.684 | 0.331 | 7.940 |
| 4 | 10.000 | 0.039 | 11.094 | 0.162 | 15.642 |
| 4 | inf | 1.531 | 1.577 | 1.082 | 0.383 |

Table 3-2B (n = 5, 6, 7):

| n | Rs/RL | C1 | L2 | C3 | L4 | C5 | L6 | C7 |
|---|---|---|---|---|---|---|---|---|
| 5 | 0.900 | 0.442 | 1.027 | 1.910 | 1.756 | 1.389 | | |
| 5 | 0.800 | 0.470 | 0.866 | 2.061 | 1.544 | 1.738 | | |
| 5 | 0.700 | 0.517 | 0.731 | 2.285 | 1.333 | 2.108 | | |
| 5 | 0.600 | 0.586 | 0.609 | 2.600 | 1.126 | 2.552 | | |
| 5 | 0.500 | 0.686 | 0.496 | 3.051 | 0.924 | 3.133 | | |
| 5 | 0.400 | 0.838 | 0.388 | 3.736 | 0.727 | 3.965 | | |
| 5 | 0.300 | 1.094 | 0.285 | 4.884 | 0.537 | 5.307 | | |
| 5 | 0.200 | 1.608 | 0.186 | 7.185 | 0.352 | 7.935 | | |
| 5 | 0.100 | 3.512 (as printed; response check gives ~3.140) | 0.091 | 14.095 | 0.173 | 15.710 | | |
| 5 | inf | 1.545 | 1.694 | 1.382 | 0.894 | 0.309 | | |
| 6 | 1.111 | 0.289 | 1.040 | 1.322 | 2.054 | 1.744 | 1.335 | |
| 6 | 1.250 | 0.245 | 1.116 | 1.126 | 2.239 | 1.550 | 1.688 | |
| 6 | 1.429 | 0.207 | 1.236 | 0.957 | 2.499 | 1.346 | 2.062 | |
| 6 | 1.667 | 0.173 | 1.407 | 0.801 | 2.858 | 1.143 | 2.509 | |
| 6 | 2.000 | 0.141 | 1.653 | 0.654 | 3.369 | 0.942 | 3.094 | |
| 6 | 2.500 | 0.111 | 2.028 | 0.514 | 4.141 | 0.745 | 3.931 | |
| 6 | 3.333 | 0.082 | 2.656 | 0.379 | 5.433 | 0.552 | 5.280 | |
| 6 | 5.000 | 0.054 | 3.917 | 0.248 | 8.020 | 0.363 | 7.922 | |
| 6 | 10.000 | 0.026 | 7.705 | 0.122 | 15.786 | 0.179 | 15.738 | |
| 6 | inf | 1.553 | 1.759 | 1.553 | 1.202 | 0.758 | 0.259 | |
| 7 | 0.900 | 0.299 | 0.711 | 1.404 | 1.489 | 2.125 | 1.727 | 1.296 |
| 7 | 0.800 | 0.322 | 0.606 | 1.517 | 1.278 | 2.334 | 1.546 | 1.652 |
| 7 | 0.700 | 0.357 | 0.515 | 1.688 | 1.091 | 2.618 | 1.350 | 2.028 |
| 7 | 0.600 | 0.408 | 0.432 | 1.928 | 0.917 | 3.005 | 1.150 | 2.477 |
| 7 | 0.500 | 0.480 | 0.354 | 2.273 | 0.751 | 3.553 | 0.951 | 3.064 |
| 7 | 0.400 | 0.590 | 0.278 | 2.795 | 0.592 | 4.380 | 0.754 | 3.904 |
| 7 | 0.300 | 0.775 | 0.206 | 3.671 | 0.437 | 5.761 | 0.560 | 5.258 |
| 7 | 0.200 | 1.145 | 0.135 | 5.427 | 0.287 | 8.526 | 0.369 | 7.908 |
| 7 | 0.100 | 2.257 | 0.067 | 10.700 | 0.142 | 16.822 | 0.182 | 15.748 |
| 7 | inf | 1.558 | 1.799 | 1.659 | 1.397 | 1.055 | 0.656 | 0.223 |

(Cross-check: Example 3-6 uses the n = 7, 0.100 row exactly.)

### 2.10 Tables 3-4A/B — Chebyshev low-pass prototype, 0.01-dB ripple (pp.46–47)

Same reading rule as the Butterworth tables. Even-order rows exist only for unequal terminations.

| n | Rs/RL | C1 | L2 | C3 | L4 | C5 | L6 | C7 |
|---|---|---|---|---|---|---|---|---|
| 2 | 1.101 | 1.347 | 1.483 | | | | | |
| 2 | 1.111 | 1.247 | 1.595 | | | | | |
| 2 | 1.250 | 0.943 | 1.997 | | | | | |
| 2 | 1.429 | 0.759 | 2.344 | | | | | |
| 2 | 1.667 | 0.609 | 2.750 | | | | | |
| 2 | 2.000 | 0.479 | 3.277 | | | | | |
| 2 | 2.500 | 0.363 | 4.033 | | | | | |
| 2 | 3.333 | 0.259 | 5.255 | | | | | |
| 2 | 5.000 | 0.164 | 7.650 | | | | | |
| 2 | 10.000 | 0.078 | 14.749 | | | | | |
| 2 | inf | 1.412 | 0.742 | | | | | |
| 3 | 1.000 | 1.181 | 1.821 | 1.181 | | | | |
| 3 | 0.900 | 1.092 | 1.660 | 1.480 | | | | |
| 3 | 0.800 | 1.097 | 1.443 | 1.806 | | | | |
| 3 | 0.700 | 1.160 | 1.228 | 2.165 | | | | |
| 3 | 0.600 | 1.274 | 1.024 | 2.598 | | | | |
| 3 | 0.500 | 1.452 | 0.829 | 3.164 | | | | |
| 3 | 0.400 | 1.734 | 0.645 | 3.974 | | | | |
| 3 | 0.300 | 2.216 | 0.470 | 5.280 | | | | |
| 3 | 0.200 | 3.193 | 0.305 | 7.834 | | | | |
| 3 | 0.100 | 6.141 | 0.148 | 15.390 | | | | |
| 3 | inf | 1.501 | 1.433 | 0.591 | | | | |
| 4 | 1.100 | 0.950 | 1.938 | 1.761 | 1.046 | | | |
| 4 | 1.111 | 0.854 | 1.946 | 1.744 | 1.165 | | | |
| 4 | 1.250 | 0.618 | 2.075 | 1.542 | 1.617 | | | |
| 4 | 1.429 | 0.495 | 2.279 | 1.334 | 2.008 | | | |
| 4 | 1.667 | 0.398 | 2.571 | 1.128 | 2.461 | | | |
| 4 | 2.000 | 0.316 | 2.994 | 0.926 | 3.045 | | | |
| 4 | 2.500 | 0.242 | 3.641 | 0.729 | 3.875 | | | |
| 4 | 3.333 | 0.174 | 4.727 | 0.538 | 5.209 | | | |
| 4 | 5.000 | 0.112 | 6.910 | 0.352 | 7.813 | | | |
| 4 | 10.000 | 0.054 | 13.469 | 0.173 | 15.510 | | | |
| 4 | inf | 1.529 | 1.694 | 1.312 | 0.523 | | | |
| 5 | 1.000 | 0.977 | 1.685 | 2.037 | 1.685 | 0.977 | | |
| 5 | 0.900 | 0.880 | 1.456 | 2.174 | 1.641 | 1.274 | | |
| 5 | 0.800 | 0.877 | 1.235 | 2.379 | 1.499 | 1.607 | | |
| 5 | 0.700 | 0.926 | 1.040 | 2.658 | 1.323 | 1.977 | | |
| 5 | 0.600 | 1.019 | 0.863 | 3.041 | 1.135 | 2.424 | | |
| 5 | 0.500 | 1.166 | 0.699 | 3.584 | 0.942 | 3.009 | | |
| 5 | 0.400 | 1.398 | 0.544 | 4.403 | 0.749 | 3.845 | | |
| 5 | 0.300 | 1.797 | 0.398 | 5.772 | 0.557 | 5.193 | | |
| 5 | 0.200 | 2.604 | 0.259 | 8.514 | 0.368 | 7.826 | | |
| 5 | 0.100 | 5.041 | 0.127 | 16.741 | 0.182 | 15.613 | | |
| 5 | inf | 1.547 | 1.795 | 1.645 | 1.237 | 0.488 | | |
| 6 | 1.101 | 0.851 | 1.796 | 1.841 | 2.027 | 1.631 | 0.937 | |
| 6 | 1.111 | 0.760 | 1.782 | 1.775 | 2.094 | 1.638 | 1.053 | |
| 6 | 1.250 | 0.545 | 1.864 | 1.489 | 2.403 | 1.507 | 1.504 | |
| 6 | 1.429 | 0.436 | 2.038 | 1.266 | 2.735 | 1.332 | 1.899 | |
| 6 | 1.667 | 0.351 | 2.298 | 1.061 | 3.167 | 1.145 | 2.357 | |
| 6 | 2.000 | 0.279 | 2.678 | 0.867 | 3.768 | 0.954 | 2.948 | |
| 6 | 2.500 | 0.214 | 3.261 | 0.682 | 4.667 | 0.761 | 3.790 | |
| 6 | 3.333 | 0.155 | 4.245 | 0.503 | 6.163 | 0.568 | 5.143 | |
| 6 | 5.000 | 0.100 | 6.223 | 0.330 | 9.151 | 0.376 | 7.785 | |
| 6 | 10.000 | 0.048 | 12.171 | 0.162 | 18.105 | 0.187 | 15.595 | |
| 6 | inf | 1.551 | 1.847 | 1.790 | 1.598 | 1.190 | 0.469 | |
| 7 | 1.000 | 0.913 | 1.595 | 2.002 | 1.870 | 2.002 | 1.595 | 0.913 |
| 7 | 0.900 | 0.816 | 1.362 | 2.089 | 1.722 | 2.202 | 1.581 | 1.206 |
| 7 | 0.800 | 0.811 | 1.150 | 2.262 | 1.525 | 2.465 | 1.464 | 1.538 |
| 7 | 0.700 | 0.857 | 0.967 | 2.516 | 1.323 | 2.802 | 1.307 | 1.910 |
| 7 | 0.600 | 0.943 | 0.803 | 2.872 | 1.124 | 3.250 | 1.131 | 2.359 |
| 7 | 0.500 | 1.080 | 0.650 | 3.382 | 0.928 | 3.875 | 0.947 | 2.948 |
| 7 | 0.400 | 1.297 | 0.507 | 4.156 | 0.735 | 4.812 | 0.758 | 3.790 |
| 7 | 0.300 | 1.669 | 0.372 | 5.454 | 0.546 | 6.370 | 0.568 | 5.148 |
| 7 | 0.200 | 2.242 (as printed; response check gives ~2.424) | 0.242 | 8.057 | 0.360 | 9.484 | 0.378 | 7.802 |
| 7 | 0.100 | 4.701 | 0.119 | 15.872 | 0.178 | 18.818 | 0.188 | 15.652 |
| 7 | inf | 1.559 | 1.867 | 1.866 | 1.765 | 1.563 | 1.161 | 0.456 |

(Table 3-4B was column-serialised in the text extraction and re-assembled by row count (11 rows per order); the symmetric n = 5 and n = 7 rows for Rs/RL = 1.000 confirm the alignment.)

### 2.11 Tables 3-5A/B — Chebyshev low-pass prototype, 0.1-dB ripple (pp.48–49)

| n | Rs/RL | C1 | L2 | C3 | L4 | C5 | L6 | C7 |
|---|---|---|---|---|---|---|---|---|
| 2 | 1.355 | 1.209 | 1.638 | | | | | |
| 2 | 1.429 | 0.977 | 1.982 | | | | | |
| 2 | 1.667 | 0.733 | 2.489 | | | | | |
| 2 | 2.000 | 0.560 | 3.054 | | | | | |
| 2 | 2.500 | 0.417 | 3.827 | | | | | |
| 2 | 3.333 | 0.293 | 5.050 | | | | | |
| 2 | 5.000 | 0.184 | 7.426 | | | | | |
| 2 | 10.000 | 0.087 | 14.433 | | | | | |
| 2 | inf | 1.391 | 0.819 | | | | | |
| 3 | 1.000 | 1.433 | 1.594 | 1.433 | | | | |
| 3 | 0.900 | 1.426 | 1.494 | 1.622 | | | | |
| 3 | 0.800 | 1.451 | 1.356 | 1.871 | | | | |
| 3 | 0.700 | 1.521 | 1.193 | 2.190 | | | | |
| 3 | 0.600 | 1.648 | 1.017 | 2.603 | | | | |
| 3 | 0.500 | 1.853 | 0.838 | 3.159 | | | | |
| 3 | 0.400 | 2.186 | 0.660 | 3.968 | | | | |
| 3 | 0.300 | 2.763 | 0.486 | 5.279 | | | | |
| 3 | 0.200 | 3.942 | 0.317 | 7.850 | | | | |
| 3 | 0.100 (printed "1.100") | 7.512 | 0.155 | 15.466 | | | | |
| 3 | inf | 1.513 | 1.510 | 0.716 | | | | |
| 4 | 1.355 | 0.992 | 2.148 | 1.585 | 1.341 | | | |
| 4 | 1.429 | 0.779 | 2.348 | 1.429 | 1.700 | | | |
| 4 | 1.667 | 0.576 | 2.730 | 1.185 | 2.243 | | | |
| 4 | 2.000 | 0.440 | 3.227 | 0.967 | 2.856 | | | |
| 4 | 2.500 | 0.329 | 3.961 | 0.760 | 3.698 | | | |
| 4 | 3.333 | 0.233 | 5.178 | 0.560 | 5.030 | | | |
| 4 | 5.000 | 0.148 | 7.607 | 0.367 | 7.614 | | | |
| 4 | 10.000 | 0.070 | 14.887 | 0.180 | 15.230 | | | |
| 4 | inf | 1.511 | 1.768 | 1.455 | 0.673 | | | |
| 5 | 1.000 | 1.301 | 1.556 | 2.241 | 1.556 | 1.301 | | |
| 5 | 0.900 | 1.285 | 1.433 | 2.380 | 1.488 | 1.488 | | |
| 5 | 0.800 | 1.300 | 1.282 | 2.582 | 1.382 | 1.738 | | |
| 5 | 0.700 | 1.358 | 1.117 | 2.868 | 1.244 | 2.062 | | |
| 5 | 0.600 | 1.470 | 0.947 | 3.269 | 1.085 | 2.484 | | |
| 5 | 0.500 | 1.654 | 0.778 | 3.845 | 0.913 | 3.055 | | |
| 5 | 0.400 | 1.954 | 0.612 | 4.720 | 0.733 | 3.886 | | |
| 5 | 0.300 | 2.477 | 0.451 | 6.196 | 0.550 | 5.237 | | |
| 5 | 0.200 | 3.546 | 0.295 | 9.127 | 0.366 | 7.889 | | |
| 5 | 0.100 | 6.787 | 0.115 (as printed; response check gives ~0.145) | 17.957 | 0.182 | 15.745 | | |
| 5 | inf | 1.561 | 1.807 | 1.766 | 1.417 | 0.651 | | |
| 6 | 1.355 | 0.942 | 2.080 | 1.659 | 2.247 | 1.534 | 1.277 | |
| 6 | 1.429 | 0.735 | 2.249 | 1.454 | 2.544 | 1.405 | 1.629 | |
| 6 | 1.667 | 0.542 | 2.600 | 1.183 | 3.064 | 1.185 | 2.174 | |
| 6 | 2.000 | 0.414 | 3.068 | 0.958 | 3.712 | 0.979 | 2.794 | |
| 6 | 2.500 | 0.310 | 3.765 | 0.749 | 4.651 | 0.778 | 3.645 | |
| 6 | 3.333 | 0.220 | 4.927 | 0.551 | 6.195 | 0.580 | 4.996 | |
| 6 | 5.000 | 0.139 | 7.250 | 0.361 | 9.261 | 0.384 | 7.618 | |
| 6 | 10.000 | 0.067 | 14.220 | 0.178 | 18.427 | 0.190 | 15.350 | |
| 6 | inf | 1.534 | 1.884 | 1.831 | 1.749 | 1.394 | 0.638 | |
| 7 | 1.000 | 1.262 | 1.520 | 2.239 | 1.680 | 2.239 | 1.520 | 1.262 |
| 7 | 0.900 | 1.242 | 1.395 | 2.361 | 1.578 | 2.397 | 1.459 | 1.447 |
| 7 | 0.800 | 1.255 | 1.245 | 2.548 | 1.443 | 2.624 | 1.362 | 1.697 |
| 7 | 0.700 | 1.310 | 1.083 | 2.819 | 1.283 | 2.942 | 1.233 | 2.021 |
| 7 | 0.600 | 1.417 | 0.917 | 3.205 | 1.209 (as printed; response check gives ~1.109) | 3.384 | 1.081 | 2.444 |
| 7 | 0.500 | 1.595 | 0.753 | 3.764 | 0.928 | 4.015 | 0.914 | 3.018 |
| 7 | 0.400 | 1.885 | 0.593 | 4.618 | 0.742 | 4.970 | 0.738 | 3.855 |
| 7 | 0.300 | 2.392 | 0.437 | 6.054 | 0.556 | 6.569 | 0.557 | 5.217 |
| 7 | 0.200 | 3.428 | 0.286 | 8.937 | 0.369 | 9.770 | 0.372 | 7.890 |
| 7 | 0.100 | 6.570 | 0.141 | 17.603 | 0.184 | 19.376 | 0.186 | 15.813 |
| 7 | inf | 1.575 | 1.858 | 1.921 | 1.827 | 1.734 | 1.379 | 0.631 |

(Cross-check: Example 3-4 uses n = 5, 0.200 row: 3.546, 0.295, 9.127, 0.366, 7.889.)

### 2.12 Tables 3-6A/B — Chebyshev low-pass prototype, 0.5-dB ripple (pp.50–51)

| n | Rs/RL | C1 | L2 | C3 | L4 | C5 | L6 | C7 |
|---|---|---|---|---|---|---|---|---|
| 2 | 1.984 | 0.983 | 1.950 | | | | | |
| 2 | 2.000 | 0.909 | 2.103 | | | | | |
| 2 | 2.500 | 0.564 | 3.165 | | | | | |
| 2 | 3.333 | 0.375 | 4.411 | | | | | |
| 2 | 5.000 | 0.228 | 6.700 | | | | | |
| 2 | 10.000 | 0.105 | 13.322 | | | | | |
| 2 | inf | 1.307 | 0.975 | | | | | |
| 3 | 1.000 | 1.864 | 1.280 | 1.834 | | | | |
| 3 | 0.900 | 1.918 | 1.209 | 2.026 | | | | |
| 3 | 0.800 | 1.997 | 1.120 | 2.237 | | | | |
| 3 | 0.700 | 2.114 | 1.015 | 2.517 | | | | |
| 3 | 0.500 | 2.557 | 0.759 | 3.436 | | | | |
| 3 | 0.400 | 2.985 | 0.615 | 4.242 | | | | |
| 3 | 0.300 | 3.729 | 0.463 | 5.576 | | | | |
| 3 | 0.200 | 5.254 | 0.309 | 8.225 | | | | |
| 3 | 0.100 | 9.890 | 0.153 | 16.118 | | | | |
| 3 | inf | 1.572 | 1.518 | 0.932 | | | | |
| 4 | 1.984 | 0.920 | 2.586 | 1.304 | 1.826 | | | |
| 4 | 2.000 | 0.845 | 2.720 | 1.238 | 1.985 | | | |
| 4 | 2.500 | 0.516 | 3.766 | 0.869 | 3.121 | | | |
| 4 | 3.333 | 0.344 | 5.120 | 0.621 | 4.480 | | | |
| 4 | 5.000 | 0.210 | 7.708 | 0.400 | 6.987 | | | |
| 4 | 10.000 | 0.098 | 15.352 | 0.194 | 14.262 | | | |
| 4 | inf | 1.436 | 1.889 | 1.521 | 0.913 | | | |
| 5 | 1.000 | 1.807 | 1.303 | 2.691 | 1.303 | 1.807 | | |
| 5 | 0.900 | 1.854 | 1.222 | 2.849 | 1.238 | 1.970 | | |
| 5 | 0.800 | 1.926 | 1.126 | 3.060 | 1.157 | 2.185 | | |
| 5 | 0.700 | 2.035 | 1.015 | 3.353 | 1.058 | 2.470 | | |
| 5 | 0.600 | 2.200 | 0.890 | 3.765 | 0.942 | 2.861 | | |
| 5 | 0.500 | 2.457 | 0.754 | 4.367 | 0.810 | 3.414 | | |
| 5 | 0.400 | 2.870 | 0.609 | 5.296 | 0.664 | 4.245 | | |
| 5 | 0.300 | 3.588 | 0.459 | 6.871 | 0.508 | 5.625 | | |
| 5 | 0.200 | 5.064 | 0.306 | 10.054 | 0.343 | 8.367 | | |
| 5 | 0.100 | 9.556 | 0.153 | 19.647 | 0.173 | 16.574 | | |
| 5 | inf | 1.630 | 1.740 | 1.922 | 1.514 | 0.903 | | |
| 6 | 1.984 | 0.905 | 2.577 | 1.368 | 2.713 | 1.299 | 1.796 | |
| 6 | 2.000 | 0.830 | 2.704 | 1.291 | 2.872 | 1.237 | 1.956 | |
| 6 | 2.500 | 0.506 | 3.722 | 0.890 | 4.109 | 0.881 | 3.103 | |
| 6 | 3.333 | 0.337 | 5.055 | 0.632 | 5.699 | 0.635 | 4.481 | |
| 6 | 5.000 | 0.206 | 7.615 | 0.406 | 8.732 | 0.412 | 7.031 | |
| 6 | 10.000 | 0.096 | 15.186 | 0.197 | 17.681 | 0.202 | 14.433 | |
| 7 | 1.000 | 1.790 | 1.296 | 2.718 | 1.385 | 2.718 | 1.296 | 1.790 |
| 7 | 0.900 | 1.835 | 1.215 | 2.869 | 1.308 | 2.883 | 1.234 | 1.953 |
| 7 | 0.800 | 1.905 | 1.118 | 3.076 | 1.215 | 3.107 | 1.155 | 2.168 |
| 7 | 0.700 | 2.011 | 1.007 | 3.364 | 1.105 | 3.416 | 1.058 | 2.455 |
| 7 | 0.600 | 2.174 | 0.882 | 3.772 | 0.979 | 3.852 | 0.944 | 2.848 |
| 7 | 0.500 | 2.428 | 0.747 | 4.370 | 0.838 | 2.289 (as printed; response check gives ~4.484) | 0.814 | 3.405 |
| 7 | 0.400 | 2.835 | 0.604 | 5.295 | 0.685 | 5.470 | 0.669 | 4.243 |
| 7 | 0.300 | 3.546 | 0.455 | 6.867 | 0.522 | 7.134 | 0.513 | 5.635 |
| 7 | 0.200 | 5.007 | 0.303 | 10.049 | 0.352 | 10.496 | 0.348 | 8.404 |
| 7 | 0.100 | 9.456 | 0.151 | 19.649 | 0.178 | 20.631 | 0.176 | 16.665 |
| 7 | inf | 1.646 | 1.777 | 2.031 | 1.789 | 1.924 | 1.503 | 0.895 |

(n = 3 has no 0.600 row and n = 6 has no "inf" row in the extracted table. Cross-check: Example 3-7 uses n = 5, 1.000 row: 1.807, 1.303, 2.691, 1.303, 1.807.)

### 2.13 Tables 3-7A/B — Chebyshev low-pass prototype, 1.0-dB ripple (pp.52–53)

| n | Rs/RL | C1 | L2 | C3 | L4 | C5 | L6 | C7 |
|---|---|---|---|---|---|---|---|---|
| 2 | 3.000 | 0.572 | 3.132 | | | | | |
| 2 | 4.000 | 0.365 | 4.600 | | | | | |
| 2 | 8.000 | 0.157 | 9.658 | | | | | |
| 2 | inf | 1.213 | 1.109 | | | | | |
| 3 | 1.000 | 2.216 | 1.088 | 2.216 | | | | |
| 3 | 0.500 | 4.431 | 0.817 | 2.216 | | | | |
| 3 | 0.333 | 6.647 | 0.726 | 2.216 | | | | |
| 3 | 0.250 | 8.862 | 0.680 | 2.216 | | | | |
| 3 | 0.125 | 17.725 | 0.612 | 2.216 | | | | |
| 3 | inf | 1.652 | 1.460 | 1.108 | | | | |
| 4 | 3.000 | 0.653 | 4.411 | 0.814 | 2.535 | | | |
| 4 | 4.000 | 0.452 | 7.083 | 0.612 | 2.848 | | | |
| 4 | 8.000 | 0.209 | 17.164 | 0.428 | 3.281 | | | |
| 4 | inf | 1.350 | 2.010 | 1.488 | 1.106 | | | |
| 5 | 1.000 | 2.207 | 1.128 | 3.103 | 1.128 | 2.207 | | |
| 5 | 0.500 | 4.414 | 0.565 | 4.653 | 1.128 | 2.207 | | |
| 5 | 0.333 | 6.622 | 0.376 | 6.205 | 1.128 | 2.207 | | |
| 5 | 0.250 | 8.829 | 0.282 | 7.756 | 1.128 | 2.207 | | |
| 5 | 0.125 | 17.657 | 0.141 | 13.961 | 1.128 | 2.207 | | |
| 5 | inf | 1.721 | 1.645 | 2.061 | 1.493 | 1.103 | | |
| 6 | 3.000 | 0.679 | 3.873 | 0.771 | 4.711 | 0.969 | 2.406 | |
| 6 | 4.000 | 0.481 | 5.644 | 0.476 | 7.351 | 0.849 | 2.582 | |
| 6 | 8.000 | 0.227 | 12.310 | 0.198 | 16.740 | 0.726 | 2.800 | |
| 6 | inf | 1.378 | 2.097 | 1.690 | 2.074 | 1.494 | 1.102 | |
| 7 | 1.000 | 2.204 | 1.131 | 3.147 | 1.194 | 3.147 | 1.131 | 2.204 |
| 7 | 0.500 | 4.408 | 0.566 | 6.293 | 0.895 | 3.147 | 1.131 | 2.204 |
| 7 | 0.333 | 6.612 | 0.377 | 9.441 | 0.796 | 3.147 | 1.131 | 2.204 |
| 7 | 0.250 | 8.815 | 0.283 | 12.588 | 0.747 | 3.147 | 1.131 | 2.204 |
| 7 | 0.125 | 17.631 | 0.141 | 25.175 | 0.671 | 3.147 | 1.131 | 2.204 |
| 7 | inf | 1.741 | 1.677 | 2.155 | 1.703 | 2.079 | 1.494 | 1.102 |

(Cross-check: Example 3-9 uses n = 3, 0.500 row: 4.431, 0.817, 2.216.)

### 2.14 Tables 3-8A/B — Bessel low-pass prototype (pp.54–56)

| n | Rs/RL | C1 | L2 | C3 | L4 | C5 | L6 | C7 |
|---|---|---|---|---|---|---|---|---|
| 2 | 1.000 | 0.576 | 2.148 | | | | | |
| 2 | 1.111 | 0.508 | 2.310 | | | | | |
| 2 | 1.250 | 0.443 | 2.510 | | | | | |
| 2 | 1.429 | 0.380 | 2.764 | | | | | |
| 2 | 1.667 | 0.319 | 3.099 | | | | | |
| 2 | 2.000 | 0.260 | 3.565 | | | | | |
| 2 | 2.500 | 0.203 | 4.258 | | | | | |
| 2 | 3.333 | 0.149 | 5.405 | | | | | |
| 2 | 5.000 | 0.097 | 7.688 | | | | | |
| 2 | 10.000 | 0.047 | 14.510 | | | | | |
| 2 | inf | 1.362 | 0.454 | | | | | |
| 3 | 1.000 | 0.337 | 0.971 | 2.203 | | | | |
| 3 | 0.900 | 0.371 | 0.865 | 2.375 | | | | |
| 3 | 0.800 | 0.412 | 0.761 | 2.587 | | | | |
| 3 | 0.700 | 0.466 | 0.658 | 2.858 | | | | |
| 3 | 0.600 | 0.537 | 0.558 | 3.216 | | | | |
| 3 | 0.500 | 0.635 | 0.459 | 3.714 | | | | |
| 3 | 0.400 | 0.783 | 0.362 | 4.457 | | | | |
| 3 | 0.300 | 1.028 | 0.267 | 5.689 | | | | |
| 3 | 0.200 | 1.518 | 0.175 | 8.140 | | | | |
| 3 | 0.100 | 2.983 | 0.086 | 15.470 | | | | |
| 3 | inf | 1.463 | 0.843 | 0.293 | | | | |
| 4 | 1.000 | 0.233 | 0.673 | 1.082 | 2.240 | | | |
| 4 | 1.111 | 0.209 | 0.742 | 0.967 | 2.414 | | | |
| 4 | 1.250 | 0.184 | 0.829 | 0.853 | 2.630 | | | |
| 4 | 1.429 | 0.160 | 0.941 | 0.741 | 2.907 | | | |
| 4 | 1.667 | 0.136 | 1.089 | 0.630 | 3.273 | | | |
| 4 | 2.000 | 0.112 | 1.295 | 0.520 | 3.782 | | | |
| 4 | 2.500 | 0.089 | 1.604 | 0.412 | 4.543 | | | |
| 4 | 3.333 | 0.066 | 2.117 | 0.306 | 5.805 | | | |
| 4 | 5.000 | 0.043 | 3.142 | 0.201 | 8.319 | | | |
| 4 | 10.000 | 0.021 | 6.209 | 0.099 | 15.837 | | | |
| 4 | inf | 1.501 | 0.978 | 0.613 | 0.211 | | | |
| 5 | 1.000 | 0.174 | 0.507 | 0.804 | 1.111 | 2.258 | | |
| 5 | 0.900 | 0.193 | 0.454 | 0.889 | 0.995 | 2.433 | | |
| 5 | 0.800 | 0.215 | 0.402 | 0.996 | 0.879 | 2.650 | | |
| 5 | 0.700 | 0.245 | 0.349 | 1.132 | 0.764 | 2.927 | | |
| 5 | 0.600 | 0.284 | 0.298 | 1.314 | 0.651 | 3.295 | | |
| 5 | 0.500 | 0.338 | 0.247 | 1.567 | 0.538 | 3.808 | | |
| 5 | 0.400 | 0.419 | 0.196 | 1.946 | 0.427 | 4.573 | | |
| 5 | 0.300 | 0.555 | 0.146 | 2.577 | 0.317 | 5.843 | | |
| 5 | 0.200 | 0.825 | 0.096 | 3.835 | 0.210 | 8.375 | | |
| 5 | 0.100 | 1.635 | 0.048 | 7.604 | 0.104 | 15.949 | | |
| 5 | inf | 1.513 | 1.023 | 0.753 | 0.473 | 0.162 | | |
| 6 | 1.000 | 0.137 | 0.400 | 0.639 | 0.854 | 1.113 | 2.265 | |
| 6 | 1.111 | 0.122 | 0.443 | 0.573 | 0.946 | 0.996 | 2.439 | |
| 6 | 1.250 | 0.108 | 0.496 | 0.508 | 1.060 | 0.881 | 2.655 | |
| 6 | 1.429 | 0.094 | 0.564 | 0.442 | 1.207 | 0.767 | 2.933 | |
| 6 | 1.667 | 0.080 | 0.655 | 0.378 | 1.402 | 0.653 | 3.300 | |
| 6 | 2.000 | 0.067 | 0.782 | 0.313 | 1.675 | 0.541 | 3.812 | |
| 6 | 2.500 | 0.053 | 0.973 | 0.249 | 2.084 | 0.429 | 4.577 | |
| 6 | 3.333 | 0.040 | 1.289 | 0.186 | 2.763 | 0.319 | 5.847 | |
| 6 | 5.000 | 0.026 | 1.289 (as printed, duplicates the row above; response check gives ~1.914) | 0.123 | 4.120 | 0.211 | 8.378 | |
| 6 | 10.000 | 0.013 | 3.815 | 0.061 | 8.186 | 0.105 | 15.951 | |
| 6 | inf | 1.512 | 1.033 | 0.813 | 0.607 | 0.379 | 0.129 | |
| 7 | 1.000 | 0.111 | 0.326 | 0.525 | 0.702 | 0.869 | 1.105 | 2.266 |
| 7 | 0.900 | 0.122 | 0.292 | 0.582 | 0.630 | 0.963 | 0.990 | 2.440 |
| 7 | 0.800 | 0.137 | 0.259 | 6.652 (as printed; response check confirms 0.652) | 0.559 | 1.080 | 0.875 | 2.656 |
| 7 | 0.700 | 0.156 | 0.226 | 0.743 | 0.487 | 1.231 | 0.762 | 2.932 |
| 7 | 0.600 | 0.182 | 0.193 | 0.863 | 0.416 | 1.431 | 0.649 | 3.298 |
| 7 | 0.500 | 0.217 | 0.160 | 1.032 | 0.346 | 1.711 | 0.537 | 3.809 |
| 7 | 0.400 | 0.270 | 0.127 | 1.285 | 0.276 | 2.130 | 0.427 | 4.572 |
| 7 | 0.300 | 0.358 | 0.095 | 1.705 | 0.206 | 2.828 | 0.318 | 5.838 |
| 7 | 0.200 | 0.534 | 0.063 | 2.545 | 0.137 | 4.221 | 0.210 | 8.362 |
| 7 | 0.100 | 1.061 | 0.031 | 5.062 | 0.068 | 8.397 | 0.104 | 15.917 |
| 7 | inf | 1.509 | 1.029 | 0.835 | 0.675 | 0.503 | 0.311 | 0.105 |

### 2.14a Verification of the transcribed prototype tables (this extraction, not in the book)

Every row of Tables 3-1, 3-2, 3-4..3-8 above (340 rows) was simulated as a doubly terminated ladder (Rs = the Rs/RL value, RL = 1, C1 shunt at the source, alternating L/C, "inf" as Rs = 1e6) and compared with the ideal response normalised to a 3-dB cutoff of 1 rad/s: Butterworth A = A(0) + 10*log(1 + w^(2n)); Chebyshev A = -10*log(K) + 10*log(1 + eps^2*Cn^2(w*cosh(B))) with K = GT(0)*(1 + eps^2*Cn(0)^2); Bessel = the reverse Bessel polynomial rescaled to 3 dB at 1 rad/s. All rows agree within 0.16 dB over 0 < w <= 3 rad/s (Bessel within 0.09 dB) except the seven cells annotated "response check" above; each of those rows returns to <= 0.034 dB when only that one cell is replaced by the value shown. Findings:
- Bowick's Chebyshev element values are normalised to the 3-dB frequency, i.e. they equal the ripple-normalised g-values (Matthaei/Zverev form) multiplied by cosh(B), B = (1/n)*acosh(1/eps). Check: 0.1-dB n = 5 equal-termination g = 1.1468, 1.3712, 1.9750 times cosh(B) = 1.1347 gives 1.301, 1.556, 2.241 (Table 3-5B). Do not mix these tables with ripple-normalised tables without that factor.
- Bowick's Bessel values are normalised to 3 dB at 1 rad/s (not unit group delay): n = 2, Rs = RL gives H = 1/(0.618*s^2 + 1.3617*s + 1), which is the Bessel polynomial with w3dB = 1.
- The ladder orientation is confirmed: C1 is the shunt element adjacent to the source even when Rs < RL (e.g. Butterworth n = 3, Rs/RL = 0.1: 5.167/0.138/15.455 gives 1 + 2s + 2s^2 + s^3 after normalisation).
- Table 3-5A n = 3 row printed "1.100" is the 0.100 row (it passes the check only as 0.100).

### 2.15 Table 3-9 — Minimum element Q required for the filter response to resemble the ideal (p.62)

| filter type | minimum element (inductor) Q |
|---|---|
| Bessel | 3 |
| Butterworth | 15 |
| Chebyshev 0.01 dB | 24 |
| Chebyshev 0.1 dB | 39 |
| Chebyshev 0.5 dB | 57 |
| Chebyshev 1 dB | 75 |
### 2.16 Impedance-matching formulas (Ch.4)

| quantity | formula | notes | source |
|---|---|---|---|
| Max power transfer (DC) | P1 = RL/(1 + RL)^2 for Rs = 1, Vs = 1; maximum at RL = Rs | | p.63, Fig. 4-1 |
| Max power transfer (AC) | ZL = Zs* (Zs = R + jX -> ZL = R - jX) | exact at one frequency only | p.63–64 |
| Shunt R-C to series equivalent | Z = Xc*RL/(Xc + RL) (complex): -j333 \|\| 1000 = 315/-71.58 deg = 100 - j300 ohm | L-network mechanism | p.65 |
| L-network Q | Qs = Qp = sqrt(Rp/Rs - 1) | Rp = shunt-leg (larger) R, Rs = series-leg R | Eq. 4-1, p.65 |
| L-network series reactance | Xs = Qs*Rs | opposite type to Xp | Eq. 4-2 |
| L-network shunt reactance | Xp = Rp/Qp | | Eq. 4-3 |
| Pi network (virtual R < both) | Q = sqrt(RH/R - 1) -> R = RH/(Q^2 + 1) | RH = larger termination | Eq. 4-4, p.69 |
| T network (virtual R > both) | Q = sqrt(R/Rsmall - 1) -> R = Rsmall*(Q^2 + 1) | Rsmall = smaller termination | Eq. 4-5, p.69 |
| Wideband two-L, max bandwidth | R = sqrt(Rs*RL) | minimum Q | Eq. 4-6, p.72 |
| Wideband two-L, loaded Q | Q = sqrt(R/Rsmaller - 1) = sqrt(Rlarger/R - 1) | Rsmaller < R < Rlarger | Eq. 4-7, p.72 |
| n-section wideband | R1/Rsmaller = R2/R1 = ... = Rlarger/Rn | equal ratios -> optimum bandwidth | Eq. 4-8, p.72 |
| Stray-C resonating inductor | L = 1/((2*pi*f)^2*C_stray) | 40 pF at 75 MHz -> 112.6 nH | Example 4-3 |
| Reflection coefficient | rho = (Zs - ZL)/(Zs + ZL); normalised rho = (Zn - 1)/(Zn + 1) | Smith-chart basis (Step 1–2) | p.72 |
| Smith chart p, q | p = (R^2 - 1 + X^2)/((R + 1)^2 + X^2); q = 2X/((R + 1)^2 + X^2) | rho = p + jq | Steps 4, 5, p.74 |
| Constant-R circle | (p - R/(R+1))^2 + q^2 = (1/(R+1))^2 | centre (R/(R+1), 0), radius 1/(R+1) | Step 7 |
| Constant-X circle | (p - 1)^2 + (q - 1/X)^2 = (1/X)^2 | centre (1, 1/X), radius 1/X | Step 8 |
| Denormalise series C (N = chart normalising R) | C = 1/(w*x*N) | Eq. 4-11 (identified from use) | p.135, p.146 |
| Denormalise shunt C | C = b/(w*N) | Eq. 4-12 | p.146 |
| Denormalise series L | L = x*N/w | Eq. 4-13 | p.146 |
| Denormalise shunt L | L = N/(w*b) | Eq. 4-14 | p.135, p.146 |

Worked matching values (Ch.4):

| example | terminations | f | result | source |
|---|---|---|---|---|
| 4-1 L (DC pass) | 100 -> 1000 ohm | 100 MHz | Q = 3, Xs = 300 ohm (477 nH), Xp = 333 ohm (4.8 pF) | p.66 |
| 4-2 absorption | 100 + j126 source, 1000 ohm \|\| 2 pF load | 100 MHz | 277 nH series (477 - 200 nH), 2.8 pF shunt (4.8 - 2 pF) | p.67 |
| 4-3 resonance (DC block) | 50 -> 600 ohm \|\| 40 pF | 75 MHz | 112.6 nH resonates 40 pF; Q = 3.32; Xs = 166 ohm (12.78 pF series); Xp = 181 ohm (384 nH); 384 \|\| 112.6 = 87 nH | p.68 |
| 4-4 pi, Q = 15 | 100 -> 1000 ohm | — | R = 4.42 ohm; Xp2 = 66.7, Xs2 = 66.3, Q1 = 4.6, Xp1 = 21.7, Xs1 = 20.5 ohm; series totals 87.4 or 46.4 ohm | p.70 |
| 4-5 T, Q = 10 | 10 -> 50 ohm | — | R = 1010 ohm; Xs1 = 100, Xp1 = 101, Q2 = 4.4, Xp2 = 230 (231), Xs2 = 220 ohm; shunt totals 70 or 179 ohm | p.71 |
| no match | 100-ohm source into 1000 ohm | — | ~4.8 dB of available power lost | p.65 |

### 2.17 Transistor and two-port formulas (Ch.5)

| quantity | formula / value | source |
|---|---|---|
| Hybrid-pi typicals | rbb' tens of ohms; rb'e ~1000 ohm; rb'c ~5 Mohm; rce ~100 k; Ce ~100 pF; Cc ~3 pF | p.104 |
| Miller capacitance (as printed) | C_Miller = Cc*(1 - beta*RL), added to Ce to form CT | p.105 |
| Input impedance | Zin = jw*(LB + LE) + rbb' + rb'e/(1 + jw*rb'e*CT) | p.105 |
| Worked Zin | LT = 20 nH, rb'e = 1000, rbb' = 50, CT = 100 pF: 1050 ohm at DC, 50 ohm at 112 MHz | p.105 |
| Y parameters | yi = I1/V1 (V2 = 0); yr = I1/V2 (V1 = 0); yf = I2/V1 (V2 = 0); yo = I2/V2 (V1 = 0) | Eqs. 5-1..5-4 |
| Y port equations | I1 = yi*V1 + yr*V2; I2 = yf*V1 + yo*V2 | Eqs. 5-5, 5-6 |
| Reflection coefficient | Gamma = Vrefl/Vinc = (ZL - Zo)/(ZL + Zo) = (Zn - 1)/(Zn + 1) | Eqs. 5-7..5-9 |
| S parameters | b1 = S11*a1 + S12*a2; b2 = S21*a1 + S22*a2; S11 = b1/a1, S21 = b2/a1 (a2 = 0); S22 = b2/a2, S12 = b1/a2 (a1 = 0) | Eqs. 5-10..5-15 |
| Y -> S (y normalised by Zo) | D = (1 + yi)(1 + yo) - yr*yf; S11 = [(1 - yi)(1 + yo) + yr*yf]/D; S12 = -2yr/D; S21 = -2yf/D; S22 = [(1 + yi)(1 - yo) + yr*yf]/D | p.114 |
| S -> Y | D' = (1 + S11)(1 + S22) - S12*S21; yi = [(1 + S22)(1 - S11) + S12*S21]/(D'*Zo); yr = -2S12/(D'*Zo); yf = -2S21/(D'*Zo); yo = [(1 + S11)(1 - S22) + S12*S21]/(D'*Zo) | p.114 |
| Gain in dB from S | G_dB = 20*log10\|S21\| | p.122 |

2N5179 data-sheet readings (Fig. 5-17; data sheet itself not in the extraction):

| quantity | condition | value | source |
|---|---|---|---|
| NF max | VCE = 6 V, IC = 1.5 mA, Rs = 50 ohm | 4.5 dB | p.115 |
| fT peak | vs IC | at ~12 mA | p.122 |
| yi | 200 MHz, VCE = 6 V, IC = 1.5 mA | 2.5 + j7.5 mmho (400 ohm \|\| 6 pF) | p.122 |
| yo | same | 0.25 + j1.8 mmho (4 k \|\| 1.4 pF) | p.122 |
| S11, S22, S12, S21 | 100 MHz, VCE = 6 V, IC = 5 mA | 0.65/309 deg, 0.84/348 deg, 0.03/70 deg (-30.5 dB), 8.2/123 deg (18.3 dB) | p.122 |
| Zin (50-ohm Smith chart) | 100 MHz, 5 mA, 6 V | 48 - j79 ohm | p.123 |
| optimum source R for NF | (Example 6-3) | 250 ohm | p.141 |

Noise-figure contour, 2N5179, VCE = 6 V, 105 MHz, NF = 3.5 dB (p.122):

| IC (mA) | 0.5 | 1.0 | 1.5 | 2.0 | 3.0 | 5.0 |
|---|---|---|---|---|---|---|
| Rs (ohm), either value | 105 or 600 | 90 or 500 | 85 or 430 | 82 or 390 | 81 or 320 | 94 or 250 |

### 2.18 Small-signal amplifier formulas (Ch.6)

| quantity | formula | source |
|---|---|---|
| VBE tempco (Si) | dVBE/dT ~= -2.5 mV/degC from ~0.7 V | p.127 |
| IC drift from VBE | dIC/IC ~= -dVBE/VE | Eq. 6-1 |
| beta tempco (Si) | +0.5%/degC (+/-25% over +/-50 degC); production spread up to 10:1 (e.g. 50–500) | p.128 |
| IC drift from beta | dIC = IC1*(dbeta/(beta1*beta2))*(1 + RB/RE), RB = R1 \|\| R2 | Eq. 6-2 |
| Bias ratio rule | RB/RE < 10 | p.128 |
| FET square law | ID = IDSS*(1 - VGS/Vp)^2 | Eq. 6-3 |
| Linvill C | C = \|yr*yf\|/(2*gi*go - Re(yr*yf)); C < 1 unconditionally stable | Eq. 6-4 |
| Stern K | K = 2*(gi + GS)*(go + GL)/(\|yr*yf\| + Re(yr*yf)); K > 1 stable | Eq. 6-5 |
| MAG (Y) | MAG = \|yf\|^2/(4*gi*go) | Eq. 6-6 |
| Conjugate-match GS | GS = sqrt([2gigo - Re(yf*yr)]^2 - \|yf*yr\|^2)/(2go) | Eq. 6-7 |
| Conjugate-match BS | BS = -bi + Im(yf*yr)/(2go) | Eq. 6-8 |
| Conjugate-match GL | GL = sqrt([2gigo - Re(yf*yr)]^2 - \|yf*yr\|^2)/(2gi) = GS*go/gi | Eqs. 6-9, 6-10 |
| Conjugate-match BL | BL = -bo + Im(yf*yr)/(2gi) | Eq. 6-11 |
| Transducer gain (Y) | GT = 4*GS*GL*\|yf\|^2/\|(yi + YS)(yo + YL) - yf*yr\|^2 | Eq. 6-12 |
| Input admittance with load | Yin = yi - yr*yf/(yo + YL) | Eq. 6-13 |
| Ds | Ds = S11*S22 - S12*S21 | Eq. 6-14 |
| Rollett K | K = (1 + \|Ds\|^2 - \|S11\|^2 - \|S22\|^2)/(2*\|S21\|*\|S12\|); unconditionally stable: K > 1 (and \|Ds\| < 1, p.136) | Eq. 6-15 |
| B1 | B1 = 1 + \|S11\|^2 - \|S22\|^2 - \|Ds\|^2 | Eq. 6-16 |
| MAG (S, dB) | 10*log(\|S21\|/\|S12\|) + 10*log\|K -/+ sqrt(K^2 - 1)\| (minus if B1 > 0, plus if B1 < 0) | Eq. 6-17 |
| C2 | C2 = S22 - Ds*conj(S11) | Eq. 6-18 |
| B2 | B2 = 1 + \|S22\|^2 - \|S11\|^2 - \|Ds\|^2 | Eq. 6-19 |
| GammaL | \|GammaL\| = (B2 -/+ sqrt(B2^2 - 4\|C2\|^2))/(2\|C2\|) (sign opposite to B2); angle = -angle(C2) | Eq. 6-20 |
| GammaS | GammaS = conj[S11 + S12*S21*GammaL/(1 - GammaL*S22)] | Eq. 6-21 |
| Transducer gain (S) | GT = \|S21\|^2(1 - \|GammaS\|^2)(1 - \|GammaL\|^2)/\|(1 - S11*GammaS)(1 - S22*GammaL) - S12*S21*GammaL*GammaS\|^2 | Eq. 6-22 |
| Matched gain from K (demo) | Gt_dB = 10*log(\|S21\|/\|S12\|*(K - sqrt(K^2 - 1))) | p.139 |

Bias network worked values (Figs. 6-4..6-8; IC or ID = 10 mA, VC or VD = 10 V, VCC = 20 V, beta = 50, VBE = 0.7 V):

| design | configuration | assumed | computed values |
|---|---|---|---|
| 1 (Fig. 6-4) | divider + RE (most stable) | VE = 2.5 V, IBB = 1.5 mA | RE = 250, RC = 1000, IB = 0.2 mA, VBB = 3.2 V, R1 = 2133, R2 = 9882 ohm |
| 2 (Fig. 6-5) | RF collector feedback + divider | VBB = 2 V, IBB = 1 mA | RB = 6500, R1 = 2000, RF = 6667, RC = 893 ohm |
| 3 (Fig. 6-6) | RF collector feedback only (least stable) | — | RF = 46.5 k, RC = 980 ohm |
| 4 (Fig. 6-7) | FET divider + RS | Vp = -6 V, IDSS = 5 mA, VS = 2.5 V, R1 = 220 k | RD = 1000, VGS = 2.48 V (as printed), RS = 250, VG = 4.98 V, R2 = 664 k |
| 5 (Fig. 6-8) | FET self bias | Vp = -6 V, IDSS = 5 mA | RD = 1000, RS = 248 ohm, RG ~ 1 Mohm |

Amplifier worked examples:

| example | data | results | source |
|---|---|---|---|
| 6-1 (Y, 100 MHz, VCE 10 V, IC 5 mA) | yi = 8 + j5.7, yo = 0.4 + j1.5, yf = 52 - j20, yr = 0.01 - j0.1 mmho | C = 0.71; MAG 23.8 dB; YS = 6.95 - j12.41, YL = 0.347 - j1.84 mmho; 24.5 pF / 72 nH input, 4.18 pF / 358 nH output; GT 23.64 dB (Ex. 6-2) | p.132–139 |
| 6-3 (Y, 200 MHz) | yi = 2.25 + j7.2, yo = 0.4 + j1.9, yf = 40 - j20, yr = 0.05 - j0.7 mmho | C = 2.27; GS = 4, K = 3 -> GL = 4.24; YL = 4.24 - j1.9; Yin = 4.84 + j13.44; YS = 4.84 - j13.44 mmho; GT = 18.3 dB | p.141 |
| 6-4 (S, 200 MHz, VCE 10 V, IC 10 mA) | S11 0.4/162, S22 0.35/-39, S12 0.04/60, S21 5.2/63 | Ds 0.068/-57, K 1.74, MAG 16.1 dB, GammaL 0.487/39 (80 + j64 ohm), GammaS 0.522/-162 (16 - j7 ohm); 23 pF, 13 nH, 12 pF, 51 nH; GT 16.1 dB (Ex. 6-5) | p.143–146 |
| RF Toolbox demo (1.9 GHz) | samplebjt2.s2p | K 1.0599, \|Ds\| 0.6776, Gt 19.24 dB; stubs 0.0883/0.0763 lambda, series 0.2147/0.2266 lambda; microstrip Z0 50.2561 ohm | p.136–139 |

### 2.19 Power-amplifier data (Ch.7)

| quantity | value / formula | source |
|---|---|---|
| Class A | conduction 360 deg; most linear; efficiency < 50% | p.174–175 |
| Class B | conduction ~180 deg; efficiency ~70% | p.175 |
| Class C | conduction << 180 deg; idles at cutoff; efficiency approaching 85% | p.176 |
| Nonlinear transfer | Vout = A*Vin + B*Vin^2 + C*Vin^3 + ... (example Vout = 5Vin + 2Vin^2) | Eq. 7-1, Fig. 7-5 |
| Two-tone products | 2nd: 2f1, 2f2, f1 + f2, f1 - f2; 3rd: 3f1, 3f2, 2f1 +/- f2, 2f2 +/- f1 | p.175 |
| Optimum collector load | RL = (VCC - Vsat)^2/(2P); 12 V, 2 V, 2 W -> 25 ohm | Eq. 7-2, Example 7-1 |
| Transmission-line transformer Zo | Zo = sqrt(Rs*RL) | Eq. 7-3 |
| Broadband transformer ratios | 1:1 balun; 4:1 (2V, I/2); 9:1 (two transformers); 16:1 (three transformers) | Figs. 7-25, 7-26 |
| Antenna radiation resistance | quarter-wave vertical ~35 ohm; half-wave dipole ~70 ohm | p.180 |
| MRF233 series impedances, 100 MHz | Zin = 1.7 - j2.7 ohm; Zout = 5 - j5.6 ohm | p.169, Fig. 7-2 |
| MRF233 parallel impedances, 100 MHz | input 6 ohm \|\| 422 pF; output 11.3 ohm \|\| 158 pF | p.169, Fig. 7-3 |
| MRF233 drive | 1 W in -> 20 W at 50 MHz (13 dB); 14 W at 90 MHz (11.5 dB) | p.169 |
| 15 W transmitter chain | 47 mW -> 15 dB driver -> 1.5 W -> 10 dB final -> 15 W | Fig. 7-19 |
| Example 7-2 networks (15 W, 100 MHz) | input Q 5.33, Xs 9.06, Xp 9.38 ohm -> 170 pF, 19 nH; output Q 3, Xs 15, Xp 16.7 ohm -> 32.7 nH, 95.3 pF; 12.5 V, 1 uH RFC, 310 ohm 1 W | pp.179, Fig. 7-18 |

### 2.20 Receiver front-end data (Ch.8)

| quantity | value / formula | source |
|---|---|---|
| Boltzmann constant | 1.38e-23 J/K = 1.38e-20 mW/K | p.194 |
| Thermal noise, 293 K, 1 Hz | 4.057e-21 W = -174 dBm (-174 dBm/Hz) | p.195 |
| Noise factor | F = SNR_in/SNR_out (book Eqs. 8-5/8-6 print the inverse) | p.194, p.199 |
| Noise figure | NF = 10*log10(F) | Eq. 8-6 |
| Passive device | NF = insertion loss | p.194 |
| Friis | F = F1 + (F2 - 1)/A1 + (F3 - 1)/(A1A2) + ... + (Fn - 1)/(A1...A(n-1)); F = 10^(NF/10), A = 10^(G/10) | Eqs. 8-7, 8-8 |
| Mixer products | fIF = fLO +/- fRF | Eq. 8-1 |
| Secondary IF (sum reflected) | fIF* = +/-[2fLO - (fLO - fRF)] as printed (intended 2fLO - (fLO + fRF) = fLO - fRF) | Eq. 8-2 |
| Two-tone mixer IM3 | fLO = +/-(2fRF1 - fRF2); fLO = +/-(2fRF2 - fRF1) | Eqs. 8-3, 8-4 |
| Single-diode mixer loss | ~3 dB conversion + ~0.75 dB per balun side + diode resistance | p.191 |
| OIP3 - OP1dB | 6 to 20 dB | p.195–196 |
| Nyquist | fs >= 2*f_max (20 MHz ADC -> 10 MHz max) | p.197 |
| ADC resolution | 12 b (double-conversion WiMAX IF sampling); 14 b (single conversion, higher IF) | p.197 |
| LO tuning / phase noise | step <= channel spacing (25 kHz example); phase noise specified at channel-spacing offset, close-in at <= 1 kHz | p.190–191 |
| TRF bandwidth drift | Q = 50: 11 kHz at 550 kHz, 33 kHz at 1650 kHz | p.189 |
| GSM sensitivity reference | BER 0.1% | p.195 |
| CDMA/W-CDMA | band 1930–1990 MHz (60 MHz); W-CDMA channel 3.84 MHz; first IF 183 MHz; sensitivity at BER <= 1e-3; in-channel noise -99 dBm -> NF 9 dB | p.198–199 |
| SiGe LNA capability | NF/gain comparable or better than GaAs to ~10 GHz | p.195 |

Table 8-1 — Intermodulation products, f1 = 100 kHz, f2 = 101 kHz (p.192):

| order | products | frequencies |
|---|---|---|
| 1st | f1, f2 | 100 kHz, 101 kHz |
| 2nd | f1 + f2, f2 - f1 | 201 kHz, 1 kHz |
| 3rd | 2f1 - f2, 2f2 - f1 | 99 kHz, 102 kHz |
| 3rd | 2f1 + f2, 2f2 + f1 | 301 kHz, 302 kHz |
| 4th | 2f2 + 2f1, 2f2 - 2f1 | 402 kHz, 2 kHz |
| 5th | 3f1 - 2f2, 3f2 - 2f1 | 98 kHz, 103 kHz |
| 5th | 3f1 + 2f2, 3f2 + 2f1 | 502 kHz, 503 kHz |

Table 8-2 — Intercept points (p.193):

| term | meaning |
|---|---|
| 1-dB compression point | level at which the output (IF for a mixer) deviates by 1 dB from linear following of the input |
| IP2 | theoretical input-vs-output point where the desired signal and second-order products are equal |
| IP3 | theoretical point where the desired signal and third-order products are equal; IIP3 = OIP3 divided by small-signal gain |

Fig. 8-14 — Typical CDMA block specifications (figure garbled in the extraction; conf = low). Recovered tokens in block order duplexer/RF filter -> LNA -> image filter -> mixer -> IF amplifier (order inferred from Fig. 8-13): Gain (dB) -3, 15, -2, 8, 10; NF (dB) < 4, < 2.5, < 3, < 3, < 15. Remaining tokens that could not be assigned to blocks: IIP2 > 37 and > 47 dBm; IIP3 values > -3, > -3, > 3, > 10, > 20 dBm; "< 25". (A Friis sum of the recovered gain/NF limits gives NF ~6.7 dB, inside the 9 dB receiver requirement — derived.)

### 2.21 Chapter 9 case-study reference numbers (IEEE 802.11a, 0.18-um RF CMOS)

| block | parameter | value | source |
|---|---|---|---|
| LNA | band / topology | 5.15–5.825 GHz, differential cascode common source | p.220–221 |
| LNA | gain, NF | 20 dB; 1.2 dB (4–6 GHz), 1.1 dB at 5.2 GHz (1.5–1.9 dB estimated within power budget) | p.220–221 |
| LNA | device, fT, bias | W ~160 um (NR = 64), fT ~44 GHz, 14 mA | p.220–221 |
| LNA | input match, S11 | 100 ohm differential, -20 to -30 dB | p.221 |
| LNA | P1dB, IP3 | -10 dBm; > 10 dBm | p.221 |
| Down-converter | conversion gain, NF, P1dB | ~6 dB; 5 dB (possibly understated); ~ -10 dBm input | p.221–222 |
| Up-converter | input P1dB vs operating level | 8 dBm vs <= -2 dBm (10 dB higher); 8 dB back-off needed for no BER loss (PA at 4–5 dB back-off) | p.222–223 |
| Up-converter | conversion loss | ~5 dB at 10 dBm differential LO | p.223 |
| PA | band, average power | 5.18–5.26 GHz, 40 mW (16 dBm) | p.223 |
| PA | required output P1dB, design target | 21 dBm; 22–23 dBm with loss allowance | p.223 |
| PA | load, supply | ~22 ohm for 23 dBm at 3 V | p.224 |
| PA | devices | 960 um/0.18 um output, 480 um/0.18 um first stage, class A (Vgs - Vth > 0.1 V) | p.224 |
| PA | stability, match | K > 2 in band; S11, S22 < -25 dB; high-pass L-match with DC block | p.224 |
| PA | results | LSS21 21 dB; input P1dB 3 dBm (output 22.6 dBm); OIP3 ~40 dBm; IM3 ~33 dB below 18 dBm; PAE ~27% at P1dB; > 6 dB PAR headroom (target 5 dB) | p.224–225 |

### 2.22 Table A1 — Frequency bands and wavelengths (p.227)

| band | range | wavelength |
|---|---|---|
| VLF | 3 to 30 kHz | 100 to 10 km |
| LF | 30 to 300 kHz | 10 to 1 km |
| MF | 0.3 to 3 MHz | 1 to 0.1 km |
| HF | 3 to 30 MHz | 100 to 10 m |
| VHF | 30 to 300 MHz | 10 to 1 m |
| UHF | 300 to 3000 MHz | 100 to 10 cm |
| SHF | 3 to 30 GHz | 10 to 1 cm |
| EHF | 30 to 300 GHz | 10 to 1 mm |

## 3. Mechanizable checks

Conventions: SI units unless stated; w = 2*pi*f; dB power = 10*log10, dB voltage = 20*log10. "Test vector" = a worked value from the book (or computed from the book's formula where marked) that an implementation must reproduce. Where Bowick gives no numeric margin, the margin is reported and the minimum is a project setting (stated as such).

### Components at RF

**CHECK-skin-depth** — inputs: f (Hz), conductor (Cu), conductor radius r or thickness t (cm). Formula: delta_Cu(f) = 0.85 cm * sqrt(60/f) (anchored at 0.85 cm @ 60 Hz; gives 0.0066 cm @ 1 MHz vs the book's rounded 0.007 cm); annulus area A_eff = pi*(r^2 - (r - delta)^2) for delta < r; R_ac/R_dc = r^2/(r^2 - (r - delta)^2). Pass: report delta and R_ac/R_dc; flag conductors with t or r < ~delta at the operating frequency (current crowding, Q loss — spiral inductors). Margin: t/delta (or r/delta). Sources: BOWICK-002..004, BOWICK-227. Test vector: delta(1 MHz) ~= 0.007 cm; delta(60 Hz) = 0.85 cm. (1/sqrt(f) scaling derived from the two book anchors — medium.)

**CHECK-lead-inductance** — inputs: lead/wire length l (cm), diameter d (cm) (from AWG Table 1-1), f. Formula: L_uH = 0.002*l*(2.3*log10(4*l/d) - 0.75); X_L = w*L. Pass: X_L <= project fraction of the circuit impedance at that node (Bowick: lead inductance negligible vs 10 k but not vs low-value resistors / bypass capacitors). Margin: Z_node/X_L. Sources: BOWICK-005, 006. Test vector: l = 5 cm, d = 0.0643 cm -> 49.8 nH (book: 50 nH).

**CHECK-resistor-parasitics** — inputs: R, shunt C_par, lead L (per lead), f. Formula: Z = 2*jwL + R || (1/(jwC_par)); for high R: |Z| = R*Xc/sqrt(R^2 + Xc^2). Pass: | |Z|/R - 1 | <= resistor-function tolerance (project). Margin: tolerance - deviation. Sources: BOWICK-007..012, Fig. 1-4. Test vector: R = 10 k, C_par = 0.3 pF, 200 MHz -> Xc = 2653 ohm, |Z| = 2564 ohm.

**CHECK-capacitor-self-resonance** — inputs: C (F), ESL (H; from datasheet or lead length via CHECK-lead-inductance), ESR, f_max of use. Formula: Fr = 1/(2*pi*sqrt(ESL*C)); Z(f) = ESR + j(w*ESL - 1/(w*C)); Q = Xc/ESR; DF = ESR/Xc. Pass: capacitive use (coupling, resonator, filter): f_max < Fr; bypass use: |Z(f_op)| <= target impedance (either side of Fr, noting that a larger C may have higher |Z| than a smaller one above its Fr). Margin: Fr/f_max (minimum ratio is a project setting; Bowick gives none). Sources: BOWICK-015..018, 023. Test vector: at 250 MHz a 0.1 uF part may present more impedance than a 300 pF part (qualitative, p.5).

**CHECK-inductor-self-resonance-and-q** — inputs: L, distributed capacitance Cd (or vendor SRF), Rs(f) (or vendor Q), f_op. Formula: Fr = 1/(2*pi*sqrt(L*Cd)); Q(f) = w*L/Rs(f); Q -> 0 at Fr. Pass: f_op < Fr (inductor still inductive) AND Q(f_op) >= required element Q (filter: Table 3-9; resonator: loaded-Q budget). Margin: Fr/f_op and Q(f_op) - Q_required. Sources: BOWICK-026..029, 101. Test vector: chip inductors typical Q 40–60 at 200 MHz.

**CHECK-air-core-coil** — inputs: L target (uH), form radius r (cm), length l (cm), wire AWG. Formula: L = 0.394*r^2*N^2/(9r + 10l); at l = 2r: N = sqrt(29*L/(0.394*r)); winding fit N*d_coated <= l. Pass: l > 0.67*r (formula validity) and turns fit; flag close-wound coils (raised Cd, lower SRF). Margin: l - N*d_coated (air gap). Sources: BOWICK-030..032, Table 1-1. Test vector: L = 0.1 uH, r = 0.317 cm, l = 0.635 cm -> N = 4.8 turns, AWG18 (42.4 mil coated) fits.

**CHECK-toroid-design** — inputs: L target (nH), AL (nH/turn^2; vendor uH/100 t divided by 10), inner radius r1 (in), wire AWG. Formula: N = sqrt(L/AL); d_max = 0.9 * 2*pi*r1/(N + pi) (in). Pass: chosen wire bare/coated diameter <= d_max (single layer); vendor Q curve at f_op >= required Q. Margin: d_max - d_wire; Q margin. Sources: BOWICK-039..044. Test vectors: 50 uH on AL = 495 -> N = 10; r1 = 0.060 in -> 28.69 mil, x0.9 = 25.82 mil -> AWG22. T-25-12 (AL = 1.2 nH/t^2), 300 nH -> 15.8 -> 16 turns.

**CHECK-core-saturation** — inputs: max rms voltage E across winding (V), f (Hz), N, Ae (cm^2), Bsat (gauss). Formula: Bop = E*1e8/(4.44*f*N*Ae) gauss. Pass: Bop < Bsat. Margin: Bsat/Bop (or Bsat - Bop). Sources: BOWICK-036. Test vector: none printed (formula only).

### Resonant circuits

**CHECK-series-parallel-conversion** — inputs: Rs, Xs, f. Formula: Q = Xs/Rs; Rp = (Q^2 + 1)*Rs; Xp = Rp/Q (Q > 10: Rp ~= Q^2*Rs, Xp ~= Xs). Pass: round-trip conversion error < 1e-6 (implementation self-test). Sources: BOWICK-056. Test vector: 50 nH, 10 ohm, 100 MHz -> Q = 3.14, Rp = 108.7 ohm, Xp = 34.62 ohm, Lp = 55.1 nH.

**CHECK-resonator-loaded-q** — inputs: Rs, RL, component Q_L (inductor), Q_C (optional), f0, required BW or Q. Formula: Rp_L = Q_L*Xp; R_total = Rs || RL || Rp_L (|| Rp_C); Q_loaded = R_total/Xp; BW = f0/Q_loaded; design Xp = R_total/Q (solve simultaneously when Rp_L depends on Xp); L = Xp/w0; C = 1/(w0*Xp); IL_dB = 20*log[(Rp||RL)/(Rs + Rp||RL)] - 20*log[RL/(Rs + RL)]. Pass: |BW - BW_spec|/BW_spec <= tolerance; IL <= IL_max; L and C realisable (not impractically small). Margin: IL_max - IL. Sources: BOWICK-052..060. Test vector (Example 2-3): BW 10 MHz at 100 MHz, 1000/1000 ohm, Q_L = 85 -> Xp = 44.1 ohm, Rp = 3.75 k, 70 nH, 36 pF, IL = 1.1 dB.

**CHECK-tapped-c-transformer** — inputs: Rs, target Rs', C_total. Formula: C1/C2 = sqrt(Rs'/Rs) - 1; C_total = C1*C2/(C1 + C2) -> C2 = C_total*(1 + C1/C2)/(C1/C2), C1 = (C1/C2)*C2. Pass: loaded Q of the tapped resonator >= 10 (validity of Eq. 2-13) and computed values realisable. Sources: BOWICK-061, 063. Test vector (Example 2-4): 50 -> 2000 ohm, CT = 39.78 pF -> C1/C2 = 5.3, C2 = 47.3 pF, C1 = 250.6 pF.

**CHECK-coupled-resonators** — inputs: Q_total required, resonator L, C, number of resonators n, coupling type. Formula: two passive critically coupled: Q_R = Q_total/0.707, C12 = C/Q_R or L12 = Q_R*L; n actively coupled: Q = Q_total*sqrt(2^(1/n) - 1). Pass: skirt-slope side matches the ultimate-attenuation requirement (top-C: 18 dB/oct below; top-L: 18 dB/oct above). Sources: BOWICK-064..070. Test vectors: Example 2-5: Q_total = 20 -> Q_R = 28.3, L = 50 nH -> L12 = 1.415 uH; n = 4, Q_total = 50 -> Q ~= 22.

### Filters

**CHECK-filter-order** — inputs: type (Butterworth, Chebyshev ripple R_dB, Bessel), required attenuation A_req at normalised frequency x (LP: f/fc; HP: fc/f; BP: BW_A/BW_3dB; BR: BW_3dB/BW_A), margin policy. Formula: Butterworth A(n,x) = 10*log(1 + x^(2n)) (closed form n >= log10(10^(A/10) - 1)/(2*log10(x))); Chebyshev A(n,x) = 10*log(1 + eps^2*Cn^2(x*cosh(B))), eps = sqrt(10^(R/10) - 1), B = acosh(1/eps)/n, Cn(y) = cosh(n*acosh(y)) for y >= 1; Bessel: Section 2.7b table / 6 dB/oct/element beyond x = 2. Choose the smallest n with A(n,x) >= A_req + margin. Pass: n_chosen >= n_min. Margin: A(n_chosen,x) - A_req (dB; the book says allow "a small fudge factor", no number). Sources: BOWICK-077, 081, 082, 084, 093, 094, 098, Sections 2.7–2.7b. Test vectors: Butterworth 50 dB at 3 -> n = 6 (47.7 dB at n = 5); 60 dB at 3 -> n = 7; 40 dB at BW ratio 3 -> n = 5; 0.5-dB Chebyshev 40 dB at 2 -> n = 5 (44.9 dB); 1-dB Chebyshev 45 dB at 5 -> n = 3 (50.3 dB); 2.5-dB Chebyshev n = 4 at 2.5 -> 47.63 dB.

**CHECK-filter-element-scaling** — inputs: prototype values (Section 2 tables; read with the correct above/below schematic), response type, fc or (f0, B), final load R, Rs/RL ratio. Formulas: LP: C = Cn/(2*pi*fc*R), L = R*Ln/(2*pi*fc); HP: replace Cn -> L = R/(2*pi*fc*Cn), Ln -> C = 1/(2*pi*fc*R*Ln); BP (f0 = sqrt(fa*fb)): shunt branch C = Cn/(2*pi*R*B), L = R*B/(2*pi*f0^2*Cn); series branch L = R*Ln/(2*pi*B), C = B/(2*pi*f0^2*Ln*R); BR (use the corrected forms, BOWICK-099; the printed Eqs. 3-20..3-23 fail this check): shunt series-resonant L = R/(2*pi*g*B), C = g*B/(2*pi*f0^2*R); series parallel-resonant L = g*R*B/(2*pi*f0^2), C = 1/(2*pi*g*R*B); Rs_final = Rs_norm*R. Pass: simulated (ngspice) response of the scaled network reproduces the prototype response at the scaled frequencies (3-dB point within tolerance, attenuation at spec points >= requirement) and each BP/BR resonator resonates at f0 (L*C = 1/(2*pi*f0)^2). Margin: attenuation margin at spec points. Sources: BOWICK-085..099, 185. Test vectors: Example 3-5 (50 MHz, 250 ohm): 3.546 -> 45 pF, 0.295 -> 235 nH; Example 3-7 HP (60 MHz, 300 ohm): 1.807 -> 4.9 pF, 1.303 -> 611 nH, 2.691 -> 3.3 pF; Example 3-9 BP (75 MHz, B = 7 MHz, 100 ohm): 4.431 -> 1007 pF / 4.47 nH, 0.817 -> 1.86 uH / 2.4 pF, 2.216 -> 504 pF / 8.93 nH (simulated: -3 dB at 71.76 and 78.76 MHz = 7.00 MHz); BR Butterworth n = 3 (1, 2, 1), 50 ohm, f0 = 100 MHz, B = 10 MHz, corrected forms -> -3 dB at 95.15 and 105.15 MHz.

**CHECK-filter-element-q** — inputs: filter type/ripple, inductor Q at the operating (cut-off or centre) frequency. Formula: Q_min from Table 3-9 (Bessel 3, Butterworth 15, Chebyshev 0.01 dB 24, 0.1 dB 39, 0.5 dB 57, 1 dB 75). Pass: every inductor Q >= Q_min; then compute insertion loss by replacing each element with its loss resistor (Rs = X/Q) and simulating. Margin: min(Q_i) - Q_min; IL_max - IL. Sources: BOWICK-100..102, Table 3-9.

**CHECK-prototype-table-sanity** — inputs: a prototype row (n, Rs/RL, g1..gn). Formula: simulate Rs - C1 (shunt) - L2 (series) - ... - RL = 1 and compare with the ideal 3-dB-normalised response (Section 2.14a). Pass: max deviation over 0 < w <= 3 rad/s <= 0.2 dB (all verified Bowick rows <= 0.16 dB). Margin: 0.2 dB - deviation. Sources: Section 2.14a (this extraction). Test vectors: the seven flagged cells fail as printed and pass with the corrected values shown.

### Impedance matching

**CHECK-l-match** — inputs: source Zs = Rs + jXs, load ZL = RL + jXL, f, topology preference (DC pass = series L; DC block = series C; harmonic filtering = low-pass). Formula: absorb or resonate strays (L_res = 1/(w^2*C_stray)); with R_large in the shunt leg: Q = sqrt(R_large/R_small - 1); X_series = Q*R_small; X_shunt = R_large/Q (opposite types); element values: series L = X/w, series C = 1/(w*X), shunt L = X/w, shunt C = 1/(w*X); absorbed values C' = C - C_stray >= 0, L' = L - L_stray >= 0. Pass: Zin(f0) looking into network+load equals Zs* (|Gamma_in| = |(Zin - Zs*)/(Zin + Zs)| <= project limit) and all absorbed element values >= 0. Margin: return loss -20*log|Gamma_in| vs requirement. Sources: BOWICK-103..110, 177. Test vectors: Example 4-1: 100 -> 1000 ohm at 100 MHz: Q = 3, 477 nH, 4.8 pF; Example 4-2: 277 nH, 2.8 pF; Example 4-3: 12.78 pF series, 87 nH shunt; Example 7-2: 1.7 -> 50 ohm Q = 5.33 (Xs 9.06, Xp 9.38 ohm), 5 -> 50 ohm Q = 3 (Xs 15, Xp 16.7 ohm).

**CHECK-pi-t-match** — inputs: Rs, RL, required loaded Q, f. Formula: pi: R_v = R_H/(Q^2 + 1) (R_v < min(Rs, RL)); T: R_v = R_small*(Q^2 + 1) (R_v > max(Rs, RL)); each side an L-match to R_v; combine series (pi) or shunt (T) reactances (add like / subtract opposite; parallel for shunt). Pass: Q_required >= Q_L-network = sqrt(R_large/R_small - 1) (otherwise use an L or wideband network) and resulting element values realisable. Margin: Q_required - Q_L. Sources: BOWICK-111..113. Test vectors: Example 4-4 (100 -> 1000, Q = 15): R_v = 4.42 ohm; Example 4-5 (10 -> 50, Q = 10): R_v = 1010 ohm.

**CHECK-wideband-match** — inputs: Rs, RL, number of L sections n. Formula: each ratio k = (R_large/R_small)^(1/(n+1)); R_i = R_small*k^i; per-section Q = sqrt(k - 1); n = 1: R = sqrt(Rs*RL). Pass: per-section Q <= Q_max allowed by the bandwidth requirement (BW ~ f0/Q; project). Sources: BOWICK-114.

**CHECK-reflection-and-mismatch** — inputs: ZL, Zo (or Zs). Formula: Gamma = (ZL - Zo)/(ZL + Zo); mismatch loss = -10*log(1 - |Gamma|^2) (derived); |Gamma| > 1 = negative resistance. Pass: |Gamma| <= limit; |Gamma| < 1 at every amplifier input network. Sources: BOWICK-105, 115, 127. Test vectors: 100 + j75 in 50 ohm -> 0.54/29.7 deg; 100 ohm source into 1000 ohm -> ~4.8 dB.

### Amplifiers

**CHECK-linvill-stability** — inputs: yi, yo, yf, yr at the bias point, over the full frequency range where |yf| is significant. Formula: C = |yr*yf|/(2*gi*go - Re(yr*yf)). Pass: C < 1 at every frequency (unconditionally stable device); C > 1 -> potentially unstable (must use CHECK-stern-stability or stabilise). Margin: 1 - C (Bowick: C near 1 is dangerous because bias/temperature drift moves the Y parameters; "the smaller C is, the better"). Sources: BOWICK-144. Test vectors: Example 6-1 C = 0.71; Example 6-3 C = 2.27.

**CHECK-stern-stability** — inputs: y-parameters, GS, GL. Formula: K = 2*(gi + GS)*(go + GL)/(|yr*yf| + Re(yr*yf)). Pass: K > 1 at every frequency for the actual terminations. Margin: K - 1 (Example 6-3 used K = 3 "for an adequate safety margin"). Sources: BOWICK-145, 157, 158. Test vector: Example 6-3: GS = 4 mmho, K = 3 -> GL = 4.24 mmho.

**CHECK-k-factor-stability (Rollett, S-parameters)** — inputs: S11, S12, S21, S22 (complex) at the bias point, swept over the whole band where the device has gain (not only f0; neutralized designs especially). Formula: Ds = S11*S22 - S12*S21; K = (1 + |Ds|^2 - |S11|^2 - |S22|^2)/(2*|S21|*|S12|). Pass: K > 1 AND |Ds| < 1 at every frequency (unconditionally stable); otherwise flag potentially unstable. Margin: min over f of (K - 1) and (1 - |Ds|). Sources: BOWICK-150, 156, 159, 233, 236. Test vectors: Example 6-4: Ds = 0.068/-57 deg, K = 1.74; demo: K = 1.0599, |Ds| = 0.6776.

**CHECK-mag-and-gain-margin** — inputs: S- or Y-parameters, required gain G_req. Formula: Y: MAG = |yf|^2/(4*gi*go); S (K > 1 only): MAG_dB = 10*log(|S21|/|S12|) + 10*log|K -/+ sqrt(K^2 - 1)| (minus if B1 = 1 + |S11|^2 - |S22|^2 - |Ds|^2 > 0). Pass: MAG_dB - G_req_dB > margin (Bowick: MAG 19 dB for an 18 dB need is too little — yr, network loss and bias drift consume the margin; exact minimum is a project setting). Margin: MAG_dB - G_req_dB. Sources: BOWICK-143, 146, 160. Test vectors: Example 6-1 MAG = 23.8 dB; Example 6-4 MAG = 16.1 dB.

**CHECK-conjugate-match-and-gt** — inputs: device parameters, designed source/load terminations. Formula: Y: GS, BS, GL, BL per Eqs. 6-7..6-11 and GT per Eq. 6-12; S: C2, B2, GammaL, GammaS per Eqs. 6-18..6-21 and GT per Eq. 6-22. Pass: GT >= G_req; for a simultaneous conjugate match GT ~= MAG (within rounding); matching networks reproduce GammaS/GammaL (CHECK-l-match). Margin: GT - G_req. Sources: BOWICK-147, 151, 153, 161..163. Test vectors: Example 6-1/6-2: YS = 6.95 - j12.41, YL = 0.347 - j1.84 mmho, GT = 23.64 dB; Example 6-4/6-5: GammaL = 0.487/39, GammaS = 0.522/-162, GT = 16.1 dB.

**CHECK-bias-thermal-stability** — inputs: VE (V), temperature range dT (degC), beta1..beta2 spread, R1, R2, RE, IC. Formula: dVBE = 2.5 mV/degC * dT; dIC/IC (VBE) = dVBE/VE; beta drift 0.5%/degC; dIC (beta) = IC1*(beta2 - beta1)/(beta1*beta2)*(1 + RB/RE), RB = R1 || R2. Pass: combined IC drift <= allowed drift (Bowick's example target 5% from VBE for +/-50 degC with VE = 2.5 V); RB/RE < 10. Margin: allowed - computed drift. Sources: BOWICK-136..139. Test vector: VE = 2.5 V, +/-50 degC -> +/-5%.

**CHECK-pa-load-line** — inputs: VCC, Vsat, required RF output P. Formula: RL = (VCC - Vsat)^2/(2P). Pass: matching network transforms the 50-ohm load to RL (absorbing Cout) — verify with CHECK-l-match; device ratings cover VCC and current. Sources: BOWICK-175, 236. Test vectors: 12 V, 2 V, 2 W -> 25 ohm; 3 V, ~0 V, 0.2 W -> 22.5 ohm (book: 22 ohm).

**CHECK-pa-drive-chain** — inputs: required Pout, stage gains G_i (dB) at the highest operating frequency, source power. Formula: P_in,k = P_out,k - G_k (dB), backwards from the final stage. Pass: available source power >= required input; each stage's rated output >= its required output (with P1dB >= P_avg + PAR for modulated signals). Margin: dB headroom per stage. Sources: BOWICK-166, 176, 184, 210, 235. Test vector: 15 W, 10 dB final, 15 dB driver -> 1.5 W drive, 47 mW source.

### Receiver lineup

**CHECK-cascaded-noise-figure** — inputs: per stage NF_i (dB; passive = insertion loss) and G_i (dB) in order. Formula: F_i = 10^(NF_i/10), A_i = 10^(G_i/10); F = F1 + sum_{i>=2} (F_i - 1)/prod_{k<i} A_k; NF = 10*log(F). Pass: NF <= NF_required (case study: 9 dB). Margin: NF_required - NF. Sources: BOWICK-202, 204, 205, 207, 217. Test vector (derived from the recovered Fig. 8-14 limits): (-3 dB, NF 4), (15, 2.5), (-2, 3), (8, 3), (10, 15) -> NF = 6.73 dB (<= 9 dB).

**CHECK-cascaded-ip3** — inputs: per stage IIP3_i (dBm) and G_i (dB). Formula (derived from the book's intercept definitions with coherent addition of IM3 — not printed in Bowick): 1/IIP3_tot = 1/IIP3_1 + A_1/IIP3_2 + A_1*A_2/IIP3_3 + ... (linear mW); OIP3_tot = IIP3_tot + G_total (dB); per-stage consistency IIP3_i = OIP3_i - G_i. Pass: IIP3_tot >= required IIP3 (e.g. from the IM3-hit check). Margin: IIP3_tot - IIP3_req (dB). Sources: BOWICK-168, 199, 200, 209. Test vector (computed): G1 = 10 dB, IIP3_1 = 0 dBm, IIP3_2 = +10 dBm -> 1/IIP3 = 1 + 10/10 = 2 /mW -> IIP3_tot = -3.0 dBm. conf = medium.

**CHECK-sensitivity** — inputs: noise bandwidth B (Hz; final IF / channel filter), NF_total (dB), required SNR (dB) or BER-derived Eb/No, T = 293 K. Formula: N_in = -174 + 10*log(B) + NF (dBm); sensitivity = N_in + SNR_req. Pass: sensitivity <= specified reference sensitivity. Margin: spec - sensitivity (dB). Sources: BOWICK-203, 206, 217. Test vector: B = 3.84 MHz, NF = 9 dB -> N_in = -99.2 dBm (book: -99 dBm).

**CHECK-dynamic-range-sfdr** — inputs: IIP3 (dBm), N_in (dBm), OP1dB, output noise floor. Formula: SFDR = (2/3)*(IIP3 - N_in) (derived); single-channel DR = OP1dB - N_out. Pass: SFDR >= required. Sources: BOWICK-209. Test vector (computed): IIP3 = +10 dBm, N_in = -99.2 dBm -> SFDR = 72.8 dB.

**CHECK-ip3-p1db-consistency** — inputs: OIP3, OP1dB of each active block (datasheet). Formula: delta = OIP3 - OP1dB. Pass: 6 dB <= delta <= 20 dB; otherwise flag data error or unusual device. Sources: BOWICK-200. Test vector: 802.11a PA: OIP3 ~40 dBm, OP1dB 22.6 dBm -> 17.4 dB (pass).

**CHECK-im3-channel-hit** — inputs: tuned frequency f0, channel bandwidth BW_ch, list of strong signals (f_i, P_i) inside the preselector passband, mixer/LNA IIP3. Formula: for every ordered pair (a, b): f_IM3 = 2*f_a - f_b; P_IM3,in = 2*P_a + P_b - 2*IIP3 (dBm, input-referred, equal-tone form generalised; derived from the 3:1 slope). Pass: no f_IM3 within f0 +/- BW_ch/2 with P_IM3,in above the sensitivity floor. Margin: sensitivity-floor - P_IM3,in. Sources: BOWICK-169, 196..198. Test vector: f0 = 1000 kHz, signals at 1020 and 1040 kHz -> 2*1020 - 1040 = 1000 kHz (hit).

**CHECK-image-frequency** — inputs: f_RF, f_IF, LO side (high/low), preselector/image-filter response. Formula: f_LO = f_RF +/- f_IF; f_image = f_RF +/- 2*f_IF (same sign as LO side). Pass: preselector + image-reject attenuation at f_image >= required image rejection (project). Margin: attenuation - requirement. Sources: BOWICK-191, 202.

**CHECK-adc-sampling** — inputs: highest IF or baseband frequency f_max, ADC rate fs, architecture (single/double conversion), anti-alias filter. Formula: fs >= 2*f_max; resolution >= 12 b (double conversion) or 14 b (single conversion, high IF) per the WiMAX example. Pass: both hold and an anti-aliasing filter precedes the ADC. Sources: BOWICK-214..216. Test vector: fs = 20 MHz -> f_max <= 10 MHz (FM 88–108 MHz must be converted to an IF <= 10 MHz).

**CHECK-lo-synthesiser** — inputs: channel spacing, synthesiser step, phase-noise specification offsets, LO drive vs mixer requirement. Pass: step <= channel spacing; phase noise specified at an offset equal to the channel spacing (close-in <= 1 kHz where relevant); LO power >= mixer's required drive (buffer if not). Sources: BOWICK-192, 194.

**CHECK-broadband-transformer** — inputs: Rs, RL, transformer ratio type (1:1, 4:1, 9:1, 16:1), winding Zo. Formula: Rin = n^2*R (n = 1..4 stacked voltages); optimum winding Zo = sqrt(Rs*RL). Pass: n^2 matches Rs/RL within tolerance and the measured/declared winding Zo ~= sqrt(Rs*RL). Sources: BOWICK-181, 183.

## 4. Verification procedures & plots

| # | property | plot / test (x-axis; y-axis) | sweep / corners | what "good" looks like / pass criterion | instrument & setup notes | source |
|---|---|---|---|---|---|---|
| V-01 | Real component impedance (R, L, C) | log f; \|Z\| (log) and phase | DC to >= 2x highest operating frequency; include self-resonance | capacitor: capacitive (-90 deg) up to Fr, series-resonant dip at Fr, inductive above; inductor: rises to parallel peak at Fr then capacitive; resistor: \|Z\|/R near 100% at f_op; pass: f_op < Fr with required \|Z\| | network analyzer (e.g. Agilent E5071C); characterise every VHF-and-up part before use; fixture/lead length as in the final layout | p.5, Figs. 1-3, 1-4, 1-9, 1-10, 1-16 |
| V-02 | Inductor Q | f; Q = X/Rs | low f to SRF | Q rises ~linearly, flattens (skin effect), falls to 0 at SRF; pass: Q(f_op) >= required (Table 3-9 for filters) | VNA or Q-meter; compare with vendor Q curves (toroids: Rp/N^2, Xp/N^2 curves) | p.9, p.19, Fig. 1-18 |
| V-03 | Core saturation / linearity | drive voltage E; L or Bop | up to max rms voltage, max temperature | Bop < Bsat, inductance flat vs drive (linear B-H region) | compute Bop (Eq. 1-10) and confirm by L vs drive measurement | p.12–13, Fig. 1-23 |
| V-04 | Resonant circuit | f (log, around f0); attenuation (dB) | f0/10 to 10*f0 | measure f0, BW3dB (f2 - f1), Q = f0/BW, insertion loss at f0, 60-dB/3-dB shape factor, ultimate attenuation, absence of out-of-band re-entrant peaks | source/load terminations as in the real circuit (Rs, RL change loaded Q) | p.23–30, Figs. 2-2, 2-8, 2-10, 2-13, 2-16 |
| V-05 | Coupled resonators | f; attenuation | across passband and both skirts | critical coupling: single-humped, minimum IL; over-coupled: double hump; under-coupled: high IL; skirt asymmetry 18/6 dB/oct on the expected side | vary coupling element (C12/L12) or spacing; document iterations for transformer coupling | p.32–34, Figs. 2-20, 2-21, 2-24 |
| V-06 | Filter amplitude response | f/fc (log); attenuation (dB) and return loss (dB) | 0.1*fc to 10*fc (HP mirror; BP/BR vs bandwidth ratio) | 3-dB point at fc (or BW at f0), passband ripple = design value, attenuation at each spec frequency >= requirement; response matches Section 2.7/2.7a/2.7b tables | simulate with ideal elements first, then with finite element Q; ngspice AC sweep of the scaled ladder with the true Rs, RL | p.37–62, Figs. 3-9, 3-15..3-18, 3-20 |
| V-07 | Finite-Q degradation | f; attenuation | same as V-06 with each inductor given its measured/vendor Q | increased passband IL, rounded knee (more than 3 dB at fc), reduced ripple, finite BR notch depth; pass: IL and edge attenuation within spec with Q >= Table 3-9 minimum | model inductor loss as series R = X/Q (or parallel R = Q*X) | p.61–62, Fig. 3-33, Table 3-9 |
| V-08 | Group delay (Bessel / pulsed / OFDM paths) | f; group delay | passband | flat (maximally flat for Bessel); Butterworth/Chebyshev strongly non-flat near cutoff | simulate phase derivative | p.50, p.197 |
| V-09 | Matching network | Smith chart of Zin(f); \|S11\| (dB) vs f | f0 +/- band edges | Zin = Zs* at f0 (chart centre when normalised to Zs real), S11 minimum at f0; bandwidth consistent with network Q (L: fixed Q; pi/T: higher Q; multi-L: lower Q) | plot on a chart normalised to a convenient R (50 or 200 ohm) | p.63–75, Figs. 4-27..4-33, 6-9, 6-10, 6-20, 6-21 |
| V-10 | Device S/Y parameters | f; S11/S22 on Smith chart, \|S21\|, \|S12\| (dB) polar | full band where \|S21\| > 1, at the actual bias | smooth data; S12 isolation (e.g. -30.5 dB), S21 gain (e.g. 18.3 dB) at the design point | measure at Zo = 50 ohm terminations (S) or RF-shorted ports (Y; hard at HF); re-measure when bias changes | p.109–123 |
| V-11 | Stability | f; Rollett K and \|Ds\| (or Linvill C / Stern K) | entire band where the device has gain, and at temperature/bias corners | K > 1 and \|Ds\| < 1 everywhere (or C < 1); neutralized amplifiers checked off f0 too | compute from swept S-parameters; include matching networks and bias parts for circuit K | p.130–142 (neutralization caveat p.140; K/\|Ds\| demo p.136) |
| V-12 | Amplifier gain and match | f; S21, S11, S22 (dB) | around f0 (e.g. 1.5–2.3 GHz for a 1.9 GHz design) | S21 close to predicted GT/MAG (e.g. 19–19.5 dB vs 19.24 dB), deep S11/S22 minima at f0 | compare "original" vs "matched" amplifier traces | p.138–139, Figs. 6-16..6-18 |
| V-13 | Bias stability | temperature; IC (or ID) | +/-50 degC around room, beta min/max parts | IC drift within budget (e.g. +/-5% from VBE with VE = 2.5 V) | thermal chamber; test min- and max-beta samples | p.127–128 |
| V-14 | Noise figure vs source and bias | Rs (or GammaS); NF; parameter IC | bias points and frequencies of use | chosen (Rs, IC) inside the required NF contour; note two Rs solutions per IC | noise-figure meter with tuner; do not extrapolate contours to other frequencies | p.115, p.122 |
| V-15 | PA transfer | Pin (dBm); Pout (dBm), gain (dB), PAE | up to beyond 1-dB compression, at band edges | required Pout reached with available drive; P1dB >= P_avg + PAR; PAE reported (e.g. 27% at P1dB class-A-biased CMOS PA) | large-signal (harmonic balance) simulation and power sweep measurement; drive requirement rises with frequency | p.169, p.223–225, Fig. 9-24 |
| V-16 | Large-signal impedance / load pull | Smith chart gain contours; Z_in vs drive | power sweep | matching tracks large-signal impedance at the operating level; optimum load within design contour | load-pull; monitor Z-comp vs input power | p.224, Fig. 9-24 |
| V-17 | Linearity (two-tone) | Pin per tone (dBm); fundamental and IM3 output (dBm) | from noise floor to compression | slopes 1:1 and 3:1; extrapolated OIP3/IIP3 and SFDR; OIP3 - OP1dB within 6..20 dB | two equal-power tones close in frequency; also 2nd-order (IP2) | p.174–175, p.193, p.195–196, Figs. 7-5, 7-6 |
| V-18 | Harmonics and spurious (transmitter) | f; output spectrum | fundamental to >= 3rd harmonic | harmonics below requirement (e.g. -50 dB) — add low-pass matching/filtering if not | spectrum analyser at full output into the real load | p.180–181 |
| V-19 | VSWR protection | load VSWR; Pout, drive, device current | open/short/rotating-phase mismatches | drive reduced above threshold; device survives | directional coupler + detector + comparator (Fig. 7-24) | p.181 |
| V-20 | Receiver cascade budget | stage index; cumulative gain, NF, IIP3 | nominal and gain-reduced (AGC) states | final NF and IIP3 meet specs (e.g. NF 9 dB for -99 dBm in 3.84 MHz) | RF budget tool (e.g. VSS RFA) or spreadsheet; include image noise | p.194–195, p.199, Fig. 9-7 |
| V-21 | Sensitivity | input level (dBm); BER (or SNR/SINAD) | around reference sensitivity | BER target (e.g. <= 1e-3 CDMA, 0.1% GSM) reached at or below the specified level | lower the input until the BER is reached | p.195, p.198 |
| V-22 | Selectivity: image, adjacent channel, IM3 hits | f; rejection (dB) | image frequency, adjacent channels, strong-pair IM3 products | image and adjacent-channel rejection >= spec; no 2fa - fb products on channel above sensitivity | two-tone test with interferers placed so that 2fa - fb = f0 (e.g. 1020/1040 kHz for 1000 kHz) | p.193, p.199 |
| V-23 | Mixer | LO power; conversion loss/gain; port isolations; IF-port return loss | LO drive range, RF level to P1dB | flat conversion loss at the chosen LO level, LO-RF and LO-IF isolation within spec, IF port terminated in constant impedance | large-signal S-parameter (LSS) measurements, conversion loss vs LO power (Figs. 9-22, 9-23) | p.191–192, p.221–223 |
| V-24 | AGC/ALC loop | time; VGA output envelope | input steps across the dynamic range | settles to the setpoint without excessive ringing; level independent of VGA gain-law and temperature | vary integrator RC to trade settling time vs ringing; verify detector temperature stability at the setpoint | p.200–201, Fig. 8-15 |
| V-25 | Chain EVM | test point along chain; EVM (and constellation, spectra) | mixer out, DC-offset-cancel out, VGA out, filter out | no block causes a step degradation in EVM; minimising EVM minimises BER | circuit-envelope / transient with modulated I/Q source | p.212–213, Figs. 9-10, 9-11 |
| V-26 | Spiral inductor model | f; L, Q, SRF (model vs measured/EM) | to beyond SRF | model predicts Q and SRF; includes frequency-dependent R and L, substrate, underpass | EM simulation (3D full-wave for critical blocks) | p.214–216, Figs. 9-14, 9-15 |
| V-27 | Post-layout RF performance | as V-06/V-12 on extracted netlists | after RC/RLC/EM extraction | specs still met with parasitics and inter-block interconnect; noisy blocks isolated | hierarchical extraction for inter-block nets; calibrated behavioural models | p.209–212 |

## 5. Pitfalls, failure modes, review checklist

### 5.1 Design review checklist (one line each)

- [ ] Every VHF-and-up component characterised (network analyzer) or modelled with its parasitics, not assumed ideal — p.5.
- [ ] No carbon-composition resistors in RF paths; wirewound resistors not used where they would resonate (10–200 MHz, low values) — p.2.
- [ ] High-value resistors at VHF checked for shunt-capacitance loss of impedance (10 k -> 2.56 k at 200 MHz with 0.3 pF) — p.3–4.
- [ ] Every capacitor's self-resonant frequency is above its highest operating frequency (or bypass |Z| verified above Fr); do not assume a larger bypass C is better above 100 MHz — p.5.
- [ ] Leaded capacitors not used above ~500 MHz (use chip capacitors) — p.6.
- [ ] Oscillator/resonator/filter capacitors are NPO/C0G (or silvered mica), never "moderately stable" (+/-15%) or high-K (up to -80%) types — p.6–7.
- [ ] Polystyrene capacitors not exposed above +85 degC — p.7.
- [ ] Every inductor operates well below its SRF with adequate Q at the operating frequency — p.8–9.
- [ ] Air-core coils not close-wound where SRF matters; formula validity l > 0.67*r respected — p.9–10.
- [ ] Magnetic cores checked for Bop < Bsat, permeability vs frequency and temperature, and core loss at f_op (a core can lower Q) — p.11–13.
- [ ] Ferrite cores not over-driven with RF (permanent permeability change); powdered iron chosen for high power and narrowband Q — p.13.
- [ ] Toroid leads do not cross the winding or each other; 30–40 deg gap between start and finish — p.21.
- [ ] Shield cans around inductors accounted for (they reduce Q and change coupling) — p.12, p.34.
- [ ] Loaded Q computed with source, load AND component losses (inductor Q usually dominates) — p.26–28.
- [ ] Insertion loss of each cascaded resonator/filter budgeted (0.9–1.1 dB per resonator adds up) — p.29–30.
- [ ] Coupled-resonator skew placed on the side where ultimate attenuation is required (top-C below, top-L above) — p.33–34.
- [ ] Filter terminated in the resistances it was designed for — p.39.
- [ ] Correct prototype schematic used (Rs/RL -> schematic above, read down; RL/Rs -> schematic below, read up) and the source resistor scaled too — p.41, p.50.
- [ ] Even-order Chebyshev never designed for equal terminations — p.47.
- [ ] Prototype tables not mixed across normalisations (Bowick Chebyshev/Bessel = 3-dB-normalised) — Section 2.14a.
- [ ] Prototype cells flagged in Section 2 (7 misprints) corrected before use — Section 2.14a.
- [ ] Band-reject designs scaled with the corrected formulas (printed Eqs. 3-20..3-23 give a stopband ~f0^2/B wide) — BOWICK-099.
- [ ] Inductor count minimised (choose prototype orientation/dual) — p.56–57.
- [ ] Inductor Q >= Table 3-9 minimum for the chosen response — p.62.
- [ ] Matching networks re-checked away from f0 (a conjugate match exists at one frequency only) — p.64.
- [ ] Strays absorbed only where stray < computed element; otherwise resonated out first — p.66–68.
- [ ] Pi/T Q chosen above the L-network Q for the same terminations — p.66.
- [ ] Smith-chart normalisation consistent for every impedance plotted on one chart — p.75.
- [ ] Input and output matches designed simultaneously (sequential matching does not converge because of yr/S12) — p.107, p.131.
- [ ] Stability (K > 1 and |Ds| < 1, or C < 1) verified over the whole band and at temperature/bias corners, not just at f0 — p.131, p.136, p.140.
- [ ] Neutralized amplifiers checked for instability away from the neutralization frequency — p.140.
- [ ] Transistor MAG exceeds required gain with margin (not 19 dB MAG for an 18 dB spec) — p.131.
- [ ] Bias network temperature-stable: VE sized for dVBE (2.5 mV/degC), RB/RE < 10, beta spread 10:1 and +0.5%/degC considered — p.127–128.
- [ ] Y/S parameters used only at the bias point they were measured at; re-characterise after a bias change — p.122, p.127.
- [ ] NF data used only at the stated frequency/bias/source resistance (no extrapolation of contours) — p.115, p.122.
- [ ] No small-signal Y/S design equations used for power amplifiers (large-signal impedances only) — p.169, p.178.
- [ ] Series vs shunt form of data-sheet large-signal impedances identified before matching — p.169.
- [ ] Driver sized at the highest operating frequency (PA gain falls with frequency) — p.169.
- [ ] Class-B bias diode thermally coupled to the transistor; RF chokes in bias paths are low-Q — p.175–176.
- [ ] PA output protected by VSWR sensing that reduces drive — p.181.
- [ ] Antenna feed matching tunable where the antenna/line impedance varies (coax is Zo only when terminated in Zo) — p.180.
- [ ] Transmitter harmonic suppression verified (low-pass matching or a designed filter) — p.180–181.
- [ ] DCR: LO-to-RF isolation and DC-offset handling designed in — p.190.
- [ ] Superhet: image at f_RF +/- 2*f_IF rejected before the mixer — p.193.
- [ ] Mixer IF port terminated in a constant-impedance (absorptive) filter — p.192.
- [ ] Strong-signal pairs checked for on-channel 2fa - fb products — p.193.
- [ ] LO step <= channel spacing and phase noise specified at the channel-spacing offset — p.190–191.
- [ ] Losses before the LNA (matching, cable, preselector, AGC pads) counted in NF — p.193–196, p.228.
- [ ] P1dB sized for peak (PAR) not average power on multicarrier/OFDM signals — p.196, p.223.
- [ ] ADC: fs >= 2*f_max, anti-alias filter present, resolution matched to architecture (12 b / 14 b) — p.197.
- [ ] AGC leveling accuracy (RSSI) adequate so the ADC is neither overdriven nor under-used — p.200.
- [ ] Noisy digital/PLL blocks isolated from sensitive RF (floorplan, guard bands) — p.211.
- [ ] Package interconnect modelled electromagnetically at GHz; packaging chosen during design — p.218–219.

### 5.2 Failure modes and pitfalls

- Capacitor used above its series resonance behaves as an inductor — bypass/coupling fails — p.5, Fig. 1-9.
- Inductor used above its parallel resonance behaves as a capacitor; Q is zero at resonance — p.7–9.
- Close-wound coil: high interwinding capacitance lowers SRF — p.10.
- Magnetic core added "for Q" can lower Q when core loss rises faster than inductance — p.13.
- Ferrite core over-driven by RF retains magnetism: permanent permeability shift — p.13.
- Low-Q inductor in a narrow filter: effective shunt resistor collapses loaded Q, widens bandwidth, raises insertion loss — p.28–29, p.61.
- Driving a filter from terminations it was not designed for changes ripple, bandwidth and shape factor — p.39.
- Loaded Q below 1 in a three-element low-pass: passband droop and extra loss even at low frequency — p.39.
- Using the Bowick band-reject scaling equations as printed: centre correct but stopband ~f0^2/B wide — BOWICK-099 (verified by simulation).
- Using transcribed prototype cells without the corrections: e.g. Table 3-6B n = 7 0.500 C5 printed 2.289 (should be ~4.484) gives a 24.5 dB response error — Section 2.14a.
- Single-frequency match used broadband: mismatch grows away from f0 — p.64.
- Absorption impossible when stray exceeds the required element (e.g. 20 pF stray vs 4.8 pF needed) — p.66.
- Sequential input-then-output matching of a transistor never converges because of internal feedback (Cc, yr, S12) — p.107.
- Cc feedback with strays can give 180 deg extra phase at HF and turn an amplifier into an oscillator — p.107.
- Linvill C just below 1: bias drift with temperature can make the device potentially unstable — p.131.
- Neutralization is exact only at one frequency; can cause instability elsewhere — p.140.
- Y-parameter measurement error at HF: the "short circuit" capacitor has reactance — p.110.
- Short-circuit terminations can make active devices oscillate during Y measurement (50-ohm S terminations generally keep them stable) — p.111.
- MAG undefined (imaginary) when K < 1 — p.142.
- Bias without emitter degeneration (collector-feedback only) gives "potluck" DC stability — p.129.
- PA designed with small-signal S-parameters — invalid; use large-signal impedances — p.169.
- Class-B bias thermal runaway when the bias diode is not thermally coupled — p.175.
- Mismatched PA load: reflected power causes secondary breakdown without VSWR protection — p.181.
- Transmission-line input impedance assumed equal to Zo on an unterminated/mismatched line — p.180.
- DCR LO leakage self-mixes to DC offset; amplifier-mixer mismatches add DC offsets — p.190.
- Near-zero-IF: image and distortion beats fall inside the IF band — p.190.
- Reflective IF filter: sum frequency re-enters the mixer (secondary IF, uneven conversion loss, IMD) — p.192.
- Weak preselection: two strong adjacent signals produce an on-channel IM3 product the IF filter cannot remove — p.193.
- LO phase noise specified only at 1 MHz offset hides close-in noise that degrades adjacent channels — p.190–191.
- AGC attenuation ahead of the LNA degrades NF dB-for-dB — p.196.
- Multicarrier peaks drive a linear-on-average stage into compression: spectral regrowth, ACPR failure — p.196.
- ADC aliasing when the IF exceeds fs/2 — p.197.
- Inaccurate RSSI: ADC overdrive or wasted dynamic range — p.200.
- AGC integrator RC too small: envelope ringing; too large: slow settling — p.201.
- Frequency-dependent R/L spiral-inductor models exported to SPICE can become nonphysical — p.216.
- Foundry kits with corner-only models may miss RF statistics, flicker noise and substrate effects — p.215.

### 5.3 Book errata found during extraction (use the corrected form)

- Example 1-3: printed lead inductance 8.7 nH for 1.27 cm of AWG14; Eq. 1-1 gives 6.8 nH (8.6 ohm at 200 MHz rather than 10.93 ohm; conclusion unchanged) — p.3.
- Example 1-6: core outside diameter printed "0.0230 inch"; the text says "just under a quarter of an inch", i.e. 0.230 inch — p.19.
- Eq. 2-15 (tapped-L) exponent lost in extraction; use Rs' = Rs*(n/n1)^2 — p.31.
- Example 2-5 cites "Equation 2-12" for the tapped-C transform; the transform is Eq. 2-13 — p.36.
- Table 3-3: C7 printed with 58x^3; correct coefficient 56 — p.44.
- Table 3-5A: n = 3 row labelled "1.100" is the 0.100 row — p.48.
- Seven prototype cells mis-printed/OCR-damaged (Tables 3-2B, 3-4B, 3-5B x2, 3-6B, 3-8B x2) — corrections in Section 2 (response-verified).
- Eqs. 3-20..3-23 band-reject scaling are the band-pass forms — correct forms in BOWICK-099.
- Chapter 7 refers to "Equations 2-6 and 2-7" for series-parallel conversion; the conversion equations are Eqs. 2-7 and 2-8 — p.169.
- Example 6-4: printed "[0.522/-162]* = 0.522/162"; the source reflection coefficient actually used (and correct) is 0.522/-162 (ZS = 16 - j7 ohm) — p.143–146.
- Figs. 6-7/6-8 FET bias examples use ID = 10 mA > IDSS = 5 mA, giving VGS = +2.48 V with Vp = -6 V — a forward-biased gate for a JFET; the numbers are consistent with Eq. 6-3 but the operating point is only valid for a depletion MOSFET — p.129–130.
- TRF example prints "500/50 or 11 kHz" for 550 kHz (550/50 = 11 kHz) — p.189.
- Eq. 8-2 printed 2fLO - (fLO - fRF); the reflected-sum mechanism described gives 2fLO - (fLO + fRF) = fIF — p.192.
- Eqs. 8-5/8-6 print the noise factor as output SNR / input SNR; correct F = SNR_in/SNR_out (as stated on p.199) — p.194.
- Eq. 8-7 prints NF = 10*log{[F1 + (F2 - 1)]/A1}; correct NF = 10*log[F1 + (F2 - 1)/A1] — p.194.
- Table 8-1 prose: calls 2f1 + f2 "fourth order" and 3f1 - f2 "fifth order"; the table itself classifies correctly (order = sum of multipliers) — p.192.

## 6. Standards referenced

| standard / system | edition / year | clause / table | what it governs (as used in the book) | page |
|---|---|---|---|---|
| American Wire Gauge (AWG) | — | Table 1-1 | wire diameters (bare/coated), ohms per 1000 ft, circular mils, AWG 1–50 | p.1, p.10 |
| FCC ISM bands (Industrial, Scientific, Medical) | 1985 opening | — | licence-free bands that enabled consumer wireless | Preface p.ix |
| IS-95 / IS-98 (CDMA) | — | reference sensitivity, ACS, intermodulation | CDMA receiver requirements: sensitivity at BER <= 1e-3, in-channel noise -99 dBm (NF 9 dB) | p.198–199 |
| W-CDMA (3G) | — | channel bandwidth | 3.84 MHz channels, 1930–1990 MHz band in the case study | p.198 |
| GSM (TDMA) | — | sensitivity | sensitivity referenced to 0.1% BER | p.195, p.198 |
| IEEE 802.16 (WiMAX, BWA) | — | — | example double-downconversion receiver with 12-bit IF-sampling ADC; OFDM | p.195, p.197 |
| IEEE 802.11a (WLAN) | — | — | 5.15–5.825 GHz CMOS transceiver case study (OFDM, 64-QAM) | p.219–225 |
| IEEE 802.11b (WLAN) | — | — | modulated test signal for direct-conversion receiver simulation | p.212 |
| Bluetooth, ZigBee, Wi-Fi, LTE, EGPRS | — | — | cited protocols driving RF front-end design (no requirements extracted) | Preface p.ix |
| IEEE 1800 (SystemVerilog) | — | — | unified hardware description and verification language | p.204 |
| IEEE 1364 (Verilog) | — | — | HDL base for SystemVerilog | p.204 |
| IEEE 1076.1 (VHDL-AMS) | — | — | analog/mixed-signal modelling language; extensions VHDL-AMS/FD (harmonic balance) and VHDL-RF/MW | p.204–205 |
| Verilog-AMS / Verilog-A | — | — | analog/mixed-signal behavioural and device modelling | p.204 |
| ODB++ | — | — | PCB manufacturing data format for prototype fabrication | p.217 |
| Nyquist sampling theorem | — | — | fs >= 2*f_max | p.197 |

No component-qualification, safety or EMC regulatory standards (IPC, IEC, CISPR, MIL) are cited in the text.

## 7. Process / lifecycle guidance

The book is a design text; Chapter 9 describes RFIC/PCB design flows and Chapters 3, 6 and 7 give step procedures. Mapped to stage -> activity -> deliverable -> exit criterion.

| stage | activity | deliverable | exit criterion | source |
|---|---|---|---|---|
| System design | build a behavioural model from ideal blocks; degrade block specs until system performance (PER/BER/EVM) degrades; build a behavioural testbench | executable specification (model + testbench) and per-block specs (NF, IP3, P1dB, phase noise) | specification validated by functional verification tools | p.208, p.220, Figs. 9-5..9-7 |
| Architecture / budget | select receiver architecture (superhet, DCR, near-zero IF) and ADC; run cascaded gain/NF/IP3 budget incl. image noise | RF budget (e.g. VSS RFA), frequency plan | budget meets sensitivity, selectivity, dynamic range | p.185–201, Fig. 9-7 |
| Process selection | choose technology (e.g. 0.18/0.25 um), install foundry PDK | PDK in the design environment | PDK contains the model classes needed for RF (corners, statistical, mismatch, pad/ESD, flicker, substrate, stress) | p.209, p.215, p.220 |
| Block circuit design | device characterisation (DC/AC, fT, Y/S), schematic, time/frequency simulation, spiral synthesis and early placement | block schematics and simulation results | block specs met in the top-level context | p.209–211, p.220–221 |
| Small-signal amplifier design | choose transistor (stability + MAG), bias network, check C/K, design matches, compute GT | amplifier schematic with component values | K > 1 (or stabilised), GT >= spec, bias stable over temperature | p.127–146 |
| Filter design | specify attenuation points, normalise, choose ripple, pick n from curves with margin, read prototype, transform, scale, check element Q | filter schematic | response and IL meet spec with real element Q | p.52–53, p.60 |
| PA design | choose final device from power data, compute RL, match large-signal impedances, plan driver chain, protect against VSWR | PA schematic, drive budget | Pout at required drive, P1dB for PAR, stability, harmonics | p.169–183, p.223–225 |
| Layout | automated routing for ordinary nets; manual full-custom routing for critical analog/RF; PCB: DFM, SI, EMI/EMC rules | layout database | DRC and LVS clean | p.209–211, p.216–217 |
| Parasitic extraction | EM extraction of critical blocks, net-based RC/RLC for the rest, hierarchical extraction of inter-block nets | extracted views and calibrated models | post-layout simulation still meets block specs | p.209–212 |
| Verification | full-chip (mixed-level) simulation in the system testbench; three-step idealised -> netlist -> extracted model validation; EVM checks at chain test points | verification report | system specs met with all parasitics; regression template maintained | p.210–213 |
| PCB release | final DRC against netlist and rules, cleanup, final verification, prototype (ODB++) or direct production | fabrication data | verification passed | p.216–217, Fig. 9-16 |
| Packaging | choose ceramic/laminate/SiP strategy during design; EM-model package interconnects | package design | reliability, manufacturability, RF performance, size, cost met | p.218–219 |

## 8. Coverage log

Source file: Bowick_Christopher_Blyler_John_Ajluni_Cheryl_RF_Circuit_Desi.txt, 13423 lines, 585,907 characters, maximum line length 2053 characters (437 lines longer than 400 characters). Read with awk line-numbered prints in ~26-KB chunks (outputs that exceeded the display limit were re-read in smaller ranges, so no line was skipped).

| lines | content | status |
|---|---|---|
| 1–161 | title, copyright (ISBN), preface, contents | read |
| 162–1345 | Ch.1 Components and Systems (pp.1–21) | read in full |
| 1346–2754 | Ch.2 Resonant Circuits (pp.23–36) | read in full |
| 2755–6321 | Ch.3 Filter Design (pp.37–62), incl. Tables 3-1..3-9 | read in full; column-serialised tables re-assembled by row count |
| 6322–7509 | Ch.4 Impedance Matching (pp.63–80) | read in full |
| 7510–8397 | Ch.5 The Transistor at Radio Frequencies (pp.103–123) | read in full (data-sheet figure pages are image-only) |
| 8398–9973 | Ch.6 Small-Signal RF Amplifier Design (pp.125–146) | read in full |
| 9974–10743 | Ch.7 RF (Large Signal) Power Amplifiers (pp.169–183) | read in full (data-sheet figure pages image-only) |
| 10744–11429 | Ch.8 RF Front-End Design (pp.185–201) | read in full |
| 11430–11931 | Ch.9 RF Design Tools (pp.203–225) | read in full |
| 11932–11991 | Appendix A RF and Antennas (pp.227–228) | read in full |
| 11992–12024 | Bibliography (pp.233–235) | read (no rules) |
| 12025–13423 | Index (pp.237–) | skipped per brief; grep-sampled to identify topics on missing pages; tail verified |

Gaps in the source extraction (pages absent from the text file, "Next Page" markers at lines 7506 and 9896):
- pp.81–102 (Ch.4): "Impedance Matching on the Smith Chart" (series/shunt element moves, multi-element matching), "Software Design Tools", Summary. Eqs. 4-11..4-14 are therefore not printed here; their forms were identified from their use in Examples 6-1 and 6-4 (BOWICK-148).
- pp.147–167 (Ch.6): the rest of S-parameter design — potentially unstable devices (stability circles), design for a specified gain (constant-gain circles), design for optimum noise figure (noise circles) — per the index terms. No rules could be extracted for these topics.
- pp.229–232: Appendix B (vector algebra: addition, subtraction, multiplication of complex quantities); only one stray figure (5 + j5 = 7.07/45 deg; 5 - j10 = 11.18/-63.4 deg) survives inside Appendix A.

Figures and data not recoverable (image-only in the source): toroid core data sheets Figs. 1-25/1-26 (only the prose readings survive), all Smith-chart constructions (Figs. 4-27..4-33, 5-6, 5-15, 6-9, 6-10, 6-13..6-15, 6-20, 6-21), 2N5179 data sheet (Fig. 5-17) and MRF233 data sheet (Fig. 7-1) — only values quoted in the prose are used; Fig. 8-14 (CDMA block specs) is garbled — partial token recovery at low confidence (Section 2.20). The attenuation graphs (Figs. 3-9, 3-15..3-18, 3-20) are replaced by tables computed from the book's own equations/prototypes (Sections 2.7, 2.7a, 2.7b), anchored to the values the prose quotes.

Extraction quality notes and verification performed:
- Equation typography flattened by the PDF extraction (fractions, radicals, exponents, subscripts, "Ϫ"/"ϩ" for minus/plus, "Ͻ"/"Ͼ" for </>); every formula was reconstructed and, where the book gives a worked example, re-computed against it.
- Prototype tables: all 340 rows of Tables 3-1, 3-2, 3-4..3-8 were simulated as ladders and compared with ideal responses; 7 misprinted/OCR-damaged cells found and annotated with response-verified corrections (Section 2.14a). Bandpass Example 3-9 simulated (-3 dB bandwidth 7.00 MHz); band-reject Eqs. 3-20..3-23 found incorrect as printed (BOWICK-099).
- Book errata identified are listed in Section 5.3; printed values are preserved and corrections are marked with how they were obtained.
- Confidence tags: high = stated in the book; medium = derived from stated relations or computed (Friis/IP3 cascade forms, SFDR, skin-depth scaling, computed attenuation tables, table corrections); low = the Fig. 8-14 token reconstruction.
- Rules extracted: 241 (BOWICK-001..BOWICK-241); mechanizable checks: 38; verification procedures: 27.
