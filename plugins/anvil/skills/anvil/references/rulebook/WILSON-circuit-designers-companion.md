# The Circuit Designer's Companion (3rd ed.) — Anvil rulebook

## 0. Citation

P. Wilson, *The Circuit Designer's Companion*, 3rd ed. (revision of the 1st and 2nd editions by T. Williams). Oxford, U.K.: Newnes (an imprint of Elsevier), 2012 (copyright 2012, 2005, 1991; LCCN 2011940053). ISBN 978-0-08-097138-4. DOI prefix 10.1016/B978-0-08-097138-4.

BOOKTAG: WILSON. Source text: `refs-text/Wilson_Circuit_Designers_Companion_2011.txt` (6876 lines).

**Chapters covered by this extraction (all read in order):**
- Front matter and introductions (pp. xiii–xv)
- Ch.1 Grounding and wiring (pp.1–43): grounding, wiring and cables, transmission lines
- Ch.2 Printed circuits (pp.45–84): board types, design rules, SM/through-hole assembly, thermal behaviour, surface protection, sourcing
- Ch.3 Passive components (pp.85–144): resistors, potentiometers, capacitors, inductors/magnetics, crystals and resonators
- Ch.4 Active components (pp.145–187): diodes, zeners, thyristors/triacs, bipolar, JFET, MOSFET, IGBT
- Ch.5 Analog integrated circuits (pp.189–234): op-amps, comparators, voltage references, circuit modelling
- Ch.6 Digital circuits (pp.235–291): logic ICs, interfacing, data interface standards, microcontrollers, watchdogs/supervisors, defensive software, platforms, ADCs
- Ch.7 Power supplies (pp.293–332): input/output parameters, fusing, inrush, PFC, linear design, abnormal conditions, mechanics, safety, batteries, SSPC
- Ch.8 Electromagnetic compatibility (pp.333–365): immunity/emission environment, legislation and standards, coupling, circuit design, shielding, filtering, cables and connectors, **EMC design checklist (§8.8, transcribed in full in §5 below)**
- Ch.9 General product design (pp.367–401): safety, design for production, ESD, testability, reliability, thermal management
- Appendix: Standards (pp.403–407) — transcribed in §6
- Bibliography (pp.409–412) — read; not extracted (reading list only)

**Not read:** Index (pp.413–439, file lines 6175–6876) — index pages are skippable per the brief (start and end spot-checked; no technical content).

**Notation.** The OCR renders micro as "m" and ohm as "U" (e.g. "0.1 mF" = 0.1 uF, "10 mU" = 10 mohm). Values below are converted to SI using context; where the prefix is genuinely ambiguous the cell says "printed ...". "uF", "uA", "uV" = micro-units. C = degrees Celsius.

## 1. Design rules

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| WILSON-001 | grounding | Make only ONE connection to the metal chassis/enclosure: a dedicated metal stud carrying mains safety earth, 0 V power rail and any PSU screen/filter connections. Multiple chassis points cause circulating chassis currents (proportion set by impedance ratio, frequency dependent) | single chassis ground point | chassis connections list | LF/general grounding; multi-point required only for RF shielding / low-inductance ground (Ch.8) | inspect | §1.1.2 p.4-5, Fig 1.2/1.3 | high |
| WILSON-002 | grounding | Aluminium chassis joints: surface Al2O3 is an insulator, so contact resistance of two Al sheets is unpredictably high. Bond plates by welding or fixings with shakeproof serrated washers; ground stud must be force-fit or welded, else serrated washer under the nut | none | chassis material, joint type | any aluminium chassis used as ground | inspect | §1.1.3 p.5, Fig 1.4 | high |
| WILSON-003 | grounding | Mild steel has ~3x the bulk resistance of aluminium; die-cast zinc conductivity 28% of copper; silver oxide is conductive and solderable (RF use). Use Table 1.1 conductivities for chassis/ground-path resistance calc | see Table 1.1 | chassis metal | chassis ground path calc | calc | §1.1.3 p.6, Table 1.1 | high |
| WILSON-004 | grounding | Ground-loop induced EMF (Lenz): V = -1e-8 * A * n * dB/dt, A = loop area (cm^2), B = flux density normal to loop (uT), n = turns. Example: 10 uT 50 Hz field through 10 cm^2 loop (conductor 1 cm above chassis for 10 cm, grounded both ends) -> 314 uV peak | V[V] = -1e-8 * A[cm^2] * n * dB/dt[uT/s]; example 314 uV pk | loop area, field, frequency | LF magnetic coupling near transformers, contactors, solenoids, fans, SMPS magnetics | calc | §1.1.4 p.6-7, Fig 1.5 | high |
| WILSON-005 | grounding | Ground-loop cures: open loop (ground at one point only); reduce loop area (route wire next to ground plane/chassis, shorten); reorient loop or source; reduce source (toroidal transformer) | reduce A in WILSON-004 | layout | LF magnetic pickup, audio/precision instrumentation | review | §1.1.4 p.7-8 | high |
| WILSON-006 | grounding | Always separate power-supply returns so each supply's load current flows in its own conductor back to the PSU; same for the feed rail. Shared 2 m of 7/0.2 wire (0.2 ohm) carrying 1.2 A + 50 mA drops 0.25 V and pulls a 3.3 V logic rail to 3.05 V (below limit); separate returns give 10 mV on the logic rail | Vs = Rs * sum(I_shared) | return currents, conductor R | any multi-supply / multi-board unit; also single-PCB tracks | inspect, calc | §1.1.5 p.8-10, Fig 1.6-1.8 | high |
| WILSON-007 | grounding | Varying loads (relays switching) on a shared return inject noise on 0 V: unreliable processor operation, shifted thresholds, chattering relays, LF "motor-boating"; treat dynamic drop, not just static | dV = Rs * dI_load | load current swing | shared returns | review | §1.1.5 p.9 | high |
| WILSON-008 | current-carrying | Wire impedance is inductive above a few kHz: 1 m of 16/0.2 equipment wire has R = 38 mohm and L = 1.5 uH; 4 A DC drops 152 mV but 4 A/us drops 6 V | V = L * di/dt + R * I | wire length, di/dt | supply/return wiring carrying switched currents | calc | §1.1.5 p.11 | high |
| WILSON-009 | grounding | Single-ended input: take the input ground return directly to the input amplifier's reference point (the node from which input voltage must be developed for the gain to act on it alone); never to 0 V elsewhere on the PCB, to chassis via connector shell, or to an external ground | none | input net topology | all low-level / sensitive inputs; auto-routers treat 0 V as one node - define input return as a separate net | inspect | §1.1.6 p.11-12, Fig 1.9(a)-(d) | high |
| WILSON-010 | grounding | Local earth potential differences: up to 50 V at mains frequency at bad locations (power stations); several volts common; sub-mV RMS in quiet sites. If the source is tied to a remote ground, use a differential amplifier (Fig 1.9(e)) | Vn up to 50 V (bad), several V (common) | site class | inputs referenced to external grounds; inter-unit links | review | §1.1.6 p.12, §1.1.10 p.17 | high |
| WILSON-011 | grounding | Output-to-input common impedance Rs creates feedback: Vin' = Vin - Iout*Rs; Vout/Vin = A/(1 + A*Rs/(RL+Rs)); circuit oscillates if A*Rs/(RL+Rs) more negative than -1 -> for an inverting amplifier the ratio load impedance : common impedance must be less than the gain to avoid instability | stable if abs(A) * Rs/(RL+Rs) < 1 (inverting) | A, Rs, RL (all frequency dependent) | any system with input-output gain incl. digital with analog input | calc | §1.1.7 p.13, Fig 1.10 | high |
| WILSON-012 | grounding | Output ground return goes directly to the point sourcing the output current (normally the PSU); high-current output gets its own ground track or is returned to the PSU bypassing the board | none | output current path | high-current outputs (relays, lamps, drivers) | inspect | §1.1.7 p.13-14, Fig 1.11 | high |
| WILSON-013 | grounding | Inter-board signals with no dedicated return see ground noise Vn along supply lines; acceptable if noise << noise margin (e.g. 100 mV noise vs 1 V CMOS margin) or signal is DC & filtered at receiver | Vn < NM | Vn, receiver noise margin | inter-board digital/processed-analog links | calc | §1.1.8 p.14, Fig 1.12 | high |
| WILSON-014 | grounding | A local inter-board ground link becomes an alternate path for supply return current. Fix: (a) separate the input-side ground on the receiving PCB and bridge the gap X-X with a "stopper" resistor of a few ohms (blocks DC ground current, ties buffer at HF, prevents floating if link removed); or (b) differential interface | R_stopper = a few ohm | ground topology | high-speed digital (ringing from inductive return) or precision analog inter-board links | inspect | §1.1.8 p.15-16, Fig 1.13/1.14 | high |
| WILSON-015 | grounding | Star-point grounding: chassis, mains earth, PSU ground and 0 V returns to one point; usable as PSU voltage-sense reference; do not substitute for return-current analysis when many connections | none | ground topology | few connections | inspect | §1.1.9 p.16 | high |
| WILSON-016 | grounding | Inter-unit signal ground return: its impedance Rs must be much less than the noise source impedance Rn or ground-injected noise is not reduced; it also forms a large, variable ground loop | Rs << Rn | Rs, Rn | mains-powered units linked by signal cable | review | §1.1.10 p.18, Fig 1.16 | high |
| WILSON-017 | grounding | Breaking the inter-unit ground link: floating (removing mains earth) is NOT permitted on safety Class I equipment; use differential link (add a ground return anyway to bound the CM voltage; CM rejection holds up to several volts) or galvanic isolation (transformer / opto / fibre - several hundred volts or more per isolation rating) | CM limit: several V (diff); hundreds of V (isolation) | interface type, safety class | inter-unit links | review | §1.1.10 p.18 | high |
| WILSON-018 | cables | RF shielding of a cable between two screened enclosures: shield is an extension of the enclosures, bond at BOTH ends via low-inductance connection, preferably the connector screen itself. LF shielding: ground shield at ONE end only. Both HF and LF: use double-shielded cable | none | frequency range of threat | inter-unit shielded cables | inspect | §1.1.11 p.19, Fig 1.17 | high |
| WILSON-019 | cables | Do not use the shield as signal return unless at RF with coaxial cable; a shield does not protect against magnetic pickup (use twisted pair for that) | none | cable type | shielded pair for high-impedance low-level inputs (capacitive pickup) | inspect | §1.1.11 p.19 | high |
| WILSON-020 | cables | LF shield end selection: floating source -> ground shield at amplifier input; grounded single-ended source -> ground shield at source, float at amplifier end or connect via choke / low-value resistor to amp ground; never ground shield at the end opposite the signal ground. Float the end with the lower capacitive coupling Cc (usually the sensor end) | none | source grounding, Cc | LF shielded inputs | inspect | §1.1.11 p.19-20, Fig 1.18 | high |
| WILSON-021 | cables | Electrostatic screening of output / inter-unit lines: ground shield at both ends; provide low-impedance ground return for shield currents driven by conductor-to-shield capacitance | none | cable capacitance | non-susceptible output lines | inspect | §1.1.11 p.20, Fig 1.19 | high |
| WILSON-022 | cables | Surface transfer impedance (shielding figure of merit): typical single braid ~10 mohm/m below 1 MHz rising at 20 dB/decade; aluminium/Mylar foil ~20 dB worse | Zt ~ 10 mohm/m (<1 MHz), +20 dB/decade | shield type, f | shielded cable selection | calc | §1.1.11 p.21 | high |
| WILSON-023 | compliance | Safety earth: mandatory for equipment relying on earthing (Class I); conductor cross-section must carry prospective fault current; all accessible conductive parts bonded; path intact until protection operates; impedance must not restrict fault current. EN 60065 example limit: < 0.5 ohm at 10 A for 1 minute | R_earth < 0.5 ohm @ 10 A, 1 min (EN 60065) | earth path resistance | Class I mains equipment | measure | §1.1.12 p.21-22, Fig 1.20 | high |
| WILSON-024 | cables | Straight round wire HF inductance: L[uH] = K * l * (2.3*log10(4*l/d) - 1), K = 0.0051 (l,d in inches) or 0.002 (l,d in cm), valid l >> d. Inductance only marginally affected by diameter; reactance dominates above a few kHz | see formula | l, d | any wire / lead / link | calc | §1.2.1 p.22, Table 1.2 | high |
| WILSON-025 | cables | Rule of thumb: inductance of 1 inch of equipment wire ~20 nH; 1 cm ~7 nH | 20 nH/in; 7 nH/cm | length | high-speed digital, RF, high di/dt loops | calc | §1.2.1 p.23 | high |
| WILSON-026 | cables | Enamelled winding wire (BS EN 60182 / IEC 60182-1): Grade 1 thinner insulation; Grade 2 roughly 2x breakdown voltage; tinned copper to BS EN 13602 | Grade 2 ~ 2x Vbd of Grade 1 | grade | wound components | review | §1.2.1 p.22 | high |
| WILSON-027 | cables | PVC equipment wire (BS 4808) max 85 C; 70 C current ratings allow 15 C rise to max; 105 C PVC to UL/CSA; PTFE to 200 C; silicone rubber 150 C. Published current ratings are temperature-rise based | Tmax(PVC) = 85 C; PTFE 200 C; silicone 150 C | insulation, ambient | wire selection | review | §1.2.1 p.23 | high |
| WILSON-028 | cables | Copper tempco of resistivity +0.00393 /C: room-temperature resistance is optimistic by several % at high ambient or with self-heating - correct R for operating temperature | R(T) = R20 * (1 + 0.00393*(T-20)) | T | voltage-drop / fusing calcs | calc | §1.2.1 p.23, Table 1.1 | high |
| WILSON-029 | current-carrying | Use Table 1.2 (bare copper wire: current & fusing current vs diameter) and Table 1.3 (BS 4808 PVC wire: current at 25 C / 70 C, mV/m drop) to size wires; fusing current is 3-15x the rated current | see tables | diameter/strands, I | wire sizing | calc | §1.2.1 p.23-24, Tables 1.2/1.3 | high |
| WILSON-030 | cables | Mains cables: BS 6500 / IEC 60227 (PVC) / IEC 60245 (rubber) harmonised; rubber ~2x PVC price; HOFR grade for heat/oil. Use CEE-22 6 A inlet and supply market-specific cable sets (UL/CSA cables do not meet EU harmonised standards and vice versa) | see Table 1.5 | market | mains-powered equipment | review | §1.2.3 p.24-25 | high |
| WILSON-031 | current-carrying | Mains cable ampacity derating by ambient (IEE Wiring Regs 17th ed.): 60 C rubber/PVC: CF 0.92 @35 C, 0.82 @40, 0.71 @45, 0.58 @50, 0.41 @55; 85 C HOFR: 1.0 @35-50 C, 0.96 @55, 0.83 @60, 0.67 @65, 0.47 @70 | I_allowed = I_table * CF(T) | ambient, cable type | mains cables | calc | Table 1.5 p.25 | high |
| WILSON-032 | cables | Never use multicore for mains power; never run high-power and signal conductors in the same cable. Multicore ratings are below those of single wires (bunching). Nominal conductor-to-screen capacitance 150-200 pF/m | C ~ 150-200 pF/m | cable | multicore selection | review | §1.2.4 p.25 | high |
| WILSON-033 | cables | Shield types: copper braid 80-95% coverage (good general shield, adds size/weight); aluminised Mylar foil + drain wire (mediocre shielding, negligible size); composite foil+braid (excellent electrostatic, ~2x foil price) | coverage 80-95% braid | environment | cable selection | review | §1.2.4 p.27 | high |
| WILSON-034 | cables | Low-noise (anti-microphonic) cable has a semiconducting layer between braid and insulation; strip it back to the braid at terminations or risk a near-short inner-to-outer | none | termination | low-level audio / vibration | inspect | §1.2.4 p.27 | high |
| WILSON-035 | cables | Coax: 50 ohm universal; 75 ohm and 93 ohm video/data; other Z0 = special. Solid/cellular polyethylene rated 85 C; PTFE 200 C. Stranded inner for flexing; braid coverage sets HF attenuation and shielding. Interpolate attenuation (dB/10 m at spot frequencies); allow several extra dB at the top of a wide band on long runs | Z0 = 50/75/93 ohm | application | RF interconnect | review | §1.2.5 p.28-29, Table 1.8 | high |
| WILSON-036 | cables | Never substitute screened audio cable for RF coax (undefined Z0, high HF attenuation); RF coax can carry audio | none | cable | RF | inspect | §1.2.5 p.29 | high |
| WILSON-037 | cables | Twisted pair reduces LF magnetic pickup to the end areas; twist rate not critical: 8-16 turns/ft (26-50 turns/m) usual; does not help against common-mode capacitive coupling (needs shielding) | 26-50 turns/m | pair | balanced / low-level links | inspect | §1.2.6 p.29-30, Fig 1.23 | high |
| WILSON-038 | crosstalk | Lumped capacitive crosstalk (cable as lumped element): worst case (coupling Xc << circuit impedances) crosstalk = ratio of circuit impedances. Example: 2 m at 150 pF/m = 300 pF (53 kohm at 10 kHz); 10k//10k = 5 kohm each side -> 5/(5+5+53) = -22 dB; with 50 ohm source: 49/(49+49+53k) = -60 dB | XT = Zv/(Zv + Zs + Xc) where Zv,Zs = victim/source parallel impedances | C/m, length, Z, f | multicore / cable bundles, LF-MF | calc | §1.2.7 p.31-32, Fig 1.24/1.25(a) | high |
| WILSON-039 | crosstalk | Edge-driven crosstalk: I = C * dV/dt * (1 - exp(-t/RC)). EIA-232 example: 16 m x 108 pF/m = 1728 pF, 30 V/us for 0.66 us, R = 567 ohm -> 25 mA into 300//5k//5k = 267 ohm -> 6.8 V spike on the victim | I = C*dV/dt*(1-exp(-t/RC)); Vpk = I * R_load_par | C, dV/dt, R | digital cables, RS-232 | calc | §1.2.7 p.32, Fig 1.25(b) | high |
| WILSON-040 | crosstalk | Crosstalk reduction: low source & load impedances (offender high-Z source, victim low-Z); shorter cable / lower pF/m; grounded conductor between each signal in ribbon (or ribbon with ground plane); individual screens (must be grounded); limit bandwidth / slow edges (RC across victim input also divides against Ccc); differential transmission (EIA-422) with twisted pair to balance coupling | none | cable, drivers | data cables | review | §1.2.7 p.33 | high |
| WILSON-041 | transmission-line | Treat a cable/track as a transmission line when wavelength of the highest frequency < 10 x length (lambda = 3e8/f; lambda_d = lambda/sqrt(er)); precision high-speed work may see effects at lambda/40; certainly by lambda/4 | L_crit = lambda_d/10 (general); lambda_d/40 (precision) | f_max, length, er | all interconnect | calc | §1.3 p.34 | high |
| WILSON-042 | transmission-line | Pulse criterion: transmission line if shortest rise time < 3 x one-way propagation time. 10 ns rise, coax VF 0.66 -> critical length 2/3 m | L_crit = tr * v / 3, v = VF * 3e8 | tr, VF | digital | calc | §1.3 p.34 | high |
| WILSON-043 | transmission-line | Z0 = sqrt((R + j*w*L)/(G + j*w*C)); lossless Z0 = sqrt(L/C); v = 1/sqrt(L*C) = 3e8/sqrt(er). Z0 is real only if G/C = R/L. Z0 = sqrt(L/C) * [1 + j(G/(wC) - R/(wL))] shows loss effect | see formulas | R,L,G,C per m | any line | calc | §1.3.1, §1.3.3 p.34-40 | high |
| WILSON-044 | transmission-line | Matched condition: both source and load = Z0 for undistorted transmission (exception to low-source / high-load rule) | Zs = ZL = Z0 | Z0 | lines longer than WILSON-041/042 limits | sim | §1.3.1 p.35 | high |
| WILSON-045 | transmission-line | Reflection: Vr/Vi = (Z - Z0)/(Z + Z0). Driver Zo/2 with open load (HCMOS buffer into unterminated HCMOS input) rings; ringing period set by transit time (line length). Typical ringing frequency for 0.6 mm track over ground plane on 1.6 mm epoxy-glass: 35 MHz / length(m) | Gamma = (Z-Z0)/(Z+Z0); f_ring ~ 35 MHz / L[m] | Z, Z0, L | digital tracks and cables | sim | §1.3.2 p.35-36, Fig 1.27 | high |
| WILSON-046 | transmission-line | Ringing tolerable only if amplitude within logic noise-immunity band or transit time faster than device response; otherwise terminate each end in Z0. Use Bergeron diagram with driver/receiver I-V characteristics extending outside supply rails | none | driver I-V, Z0 | fast logic | sim | §1.3.2 p.37 | high |
| WILSON-047 | transmission-line | Shorted-stub pulse generator: 1 m coax with VF 0.66 gives a 10 ns pulse (2 x transit) | t_pulse = 2*L/(VF*3e8) | L, VF | test/pulse gen | calc | §1.3.2 p.38, Fig 1.28 | high |
| WILSON-048 | rf | SWR = (1+abs(Gamma))/(1-abs(Gamma)) = RL/Z0 for resistive load; SWR 1:1 matched; infinite for short/open; independent of source impedance. Standing-wave pattern repeats every lambda/2 | see formula | Gamma | RF lines | measure | §1.3.3 p.39 | high |
| WILSON-049 | matching | Quarter-wave transformer: Zin = Z0^2/ZL at lambda/4 (and odd multiples); at any multiple of lambda/2 the load impedance is regained regardless of Z0; shorted line is ~0 ohm lambda/2 away (distributed tuned circuit) | Zin = Z0^2/ZL | Z0, ZL, f | RF matching | calc | §1.3.3 p.40 | high |
| WILSON-050 | rf | Lossy lines: loss under standing waves exceeds matched loss (Table 1.8 values are matched); attenuation improves apparent SWR at the generator; long cable acts as attenuator | none | loss, SWR | RF feeders | calc | §1.3.3 p.40 | high |
| WILSON-051 | transmission-line | Coax design: D = d * exp(Z0 * sqrt(er) / 60). Example 24 SWG (d = 0.56 mm), PTFE er = 2.1, Z0 = 50 ohm -> D = 1.873 mm | D = d*exp(Z0*sqrt(er)/60) | d, er, Z0 | coax / cylindrical geometry | calc | §1.3.3 p.41-42, Table 1.9/1.10 | high |
| WILSON-052 | rf | Reflection coefficient from VSWR: rho_v = abs(Vrefl)/abs(Vinc) = (VSWR-1)/(VSWR+1); phase[deg] = 720*(x/lambda - 1/4), x = distance of the voltage minimum from the load (m), lambda in m; plot on reflection-coefficient (Smith) chart to classify load | see formulas | VSWR, x, lambda | RF measurement | measure | §1.3.3 p.42-43, Fig 1.30 | high |
| WILSON-053 | materials | Copper foil weight: 1 oz = 0.035 mm +/- 0.002 mm thick; other weights (0.25, 0.5, 2, 3, 4 oz) pro rata. Outer-layer thickness = foil + total plating | t(1 oz) = 0.035 +/- 0.002 mm | copper weight | all PCBs | calc | §2.1.1 p.47, §2.1.5 p.54 | high |
| WILSON-054 | materials | Laminate selection per Table 2.1 (FR4: er max 5.4 typ 4.6-4.9, tan d max 0.035, 1.0 kV/mil min, 13-16 ppm/C, Tmax 110-150 C). Phenolic paper only for very cost-sensitive low-performance boards (no PTH, brittle, moisture absorbing, poor Cu adhesion for rework). Polyester flex cannot be soldered (low softening temp) - tails only; polyimide flex accepts components | see Table 2.1 | performance needs | laminate choice | review | §2.1.1 p.47-48, Table 2.1 | high |
| WILSON-055 | stackup | Multilayer boards always have an even number of copper layers (4, 6, 8 ...); up to 24 layers fabricable; all boards on one panel must share layer count and thickness | N_layers even | stackup | multilayer | inspect | §2.1.4-2.1.5 p.51-52 | high |
| WILSON-056 | dfm | Packing density guide: double-sided PTH 4-7 cm^2 per 16-pin DIL package; multilayer approaches 2 cm^2 per package. Proper power/ground plane distribution needs minimum 4-layer construction; at lower density a ground plane on one side of a double-sided board | 4-7 cm^2/DIL (2-layer PTH); ~2 cm^2 (multilayer) | package count, area | board type selection | calc | §2.1.3 p.50 | high |
| WILSON-057 | mechanical | Standard sizes: Eurocard 100 x 160 mm, double-Eurocard 233.4 x 160 mm. Optimum size for large boards ~30-50 cm on the longer edge (stiffness, tolerancing, handling). Allow a safety factor in area per subsystem - modifications nearly always add components | 30-50 cm max longer edge | board size | board sizing | review | §2.1.4 p.51 | high |
| WILSON-058 | fab | Typical best PCB manufacturer capabilities (Table 2.2): thickness 0.35-3.5 mm; 14-24 layers; min track & gap (1 oz) 0.1 mm possible / 0.15 mm preferred; min PTH hole 0.2 mm possible / 0.3 mm preferred; max hole aspect ratio 12:1 possible / 6:1 preferred; drill-to-pad registration 0.03 mm; layer-to-layer (incl. solder mask) 0.075 mm. Thicker copper needs wider minimum tracks (etch undercut). Confirm with supplier | see values | design min features | DRC limits | review | §2.2 p.55, Table 2.2 | high |
| WILSON-059 | current-carrying | Track resistance R = rho*l/A (Fig 2.10 gives ohm/cm vs width for each copper weight - graph). Manufactured tolerance (base Cu + plating + tin-lead) gives up to 2:1 variation in final value; add several % for copper tempco over ambient and self-heating. PTH > 0.8 mm dia presents < 1 mohm | R = rho*l/A; tolerance 2:1; R_PTH(>0.8 mm) < 1 mohm | w, t, l, I | DC drop calcs | calc | §2.2.1 p.56, Fig 2.10 | high |
| WILSON-060 | current-carrying | Max track current is set by self-heating: use Fig 2.11 "Safe currents in PCB tracks" (safe current vs track width for a given temperature rise, abstracted from BS 6221 Part 3:1984 - graph, no numeric anchors in text) | graph | w, dT | track ampacity | calc | §2.2.1 p.57, Fig 2.11 | medium |
| WILSON-061 | fab | Voltage breakdown spacing (benign environment - dry, no conductive particles): 1 mm per 200 V, allowing for manufacturing tolerances. Mains voltages: spacing set by safety approval requirements (see Ch.9). Spacings < 0.5 mm risk solder bridging in wave soldering if no solder resist | s >= V/200 mm (V in volts); s >= 0.5 mm if wave-soldered without resist | V between tracks | benign environment PCB | calc | §2.2.1 p.57 | high |
| WILSON-062 | crosstalk | Track-to-track crosstalk rule of thumb: spacing > 1 mm gives crosstalk < 10% of signal voltage for most board configurations; electrically short connections may be closer; route ground conductors between susceptible signal pairs; use field solvers for exact C | s > 1 mm -> XT < 10% (-20 dB) | s | low-voltage digital / high-speed analog boards | calc | §2.2.1 p.57 | high |
| WILSON-063 | transmission-line | Constant-impedance layers: microstrip (track over ground plane) or stripline (track between two planes). Wider track -> lower Z0 and tighter tolerance (etch-controlled); thinner separation -> lower Z0 (pre-preg thickness & bonding pressure). Inner-layer Z0 scales with 1/sqrt(er); surface layer mixed air/epoxy. General FR4 has loose er spec - use premium material for controlled impedance | Z0 per Table 1.9 strip-over-plane | w, h, er | high-frequency / fast digital tracks | calc | §2.2.1 p.57-58 | high |
| WILSON-064 | fab | Component hole diameter = lead diameter + 0.15 to 0.3 mm (auto-insertion may need more). Standardise: 0.8 mm for DIL & most small parts, 1.0 mm for larger; specify hole size AFTER plating on PTH boards; verify lead diameters (capacitors, power rectifiers are larger than expected); multilayer holes cannot be drilled out | d_hole = d_lead + 0.15..0.3 mm | lead dia | through-hole parts | inspect | §2.2.2 p.58 | high |
| WILSON-065 | via | Via aspect ratio (board thickness : hole dia) up to 6:1 plates without trouble; keep via drill = smallest component hole, or one size smaller (e.g. 0.6 mm) to prevent false lead insertion; minimise the count of distinct drill sizes | AR <= 6:1 | t_board, d_via | vias | calc | §2.2.2 p.58 | high |
| WILSON-066 | fab | Pads: non-PTH round pad for a 0.8 mm hole ~2 mm dia (no room for a track between DIL pins; oval allows one track). PTH pad for 0.8 mm hole: 1.3-1.5 mm dia. Non-PTH pads for larger holes: exceed hole dia by >= 1 mm; pad/hole ratio ~2 (epoxy-glass), 2.5-3 (phenolic paper) | PTH pad = 1.3-1.5 mm @0.8 mm hole; non-PTH pad/hole ~2 (FR4), 2.5-3 (SRBP) | hole dia, board type | pad sizing | calc | §2.2.2 p.59, Fig 2.12 | high |
| WILSON-067 | assembly | SM pad sizes are fixed by component terminal and soldering method (wave vs reflow); use supplier datasheet pad recommendations; verify CAD library footprints on introduction | none | footprint | SMT | inspect | §2.2.2 p.60 | high |
| WILSON-068 | dfm | Routing: minimise track length; swap gate/op-amp pins to shorten tracks; X-Y auto-routing can be disastrous on analog boards; 45-degree bends preferred, avoid right/acute angles (etchant traps -> corrosion), fillet acute joins; no track closer than 0.5 mm to board edge; balance copper coverage on both sides / all layers to avoid warp | edge clearance >= 0.5 mm | layout | all boards | inspect | §2.2.3 p.60 | high |
| WILSON-069 | pdn | Track inductance depends on length, only logarithmically on width; minimise total loop inductance by running signal/power and return paths very close (mutual inductance subtracts). Run power and ground rails with identical geometry on opposite sides of the board, or give board space to the ground and control power-rail noise by decoupling | none | routing | HF currents | inspect | §2.2.4 p.61, Fig 2.13 | high |
| WILSON-070 | grounding | Ground bus acceptable at low frequency, low gain, low current, high signal level (rail drops << operating voltages). Gridded ground on 2-layer boards approaches a plane if ICs are regular and rails well decoupled; not for sensitive analog needing controlled return paths. Ground plane best for random ground connection patterns (analog, mixed package sizes) | none | circuit class | ground strategy | review | §2.2.4 p.60-61 | high |
| WILSON-071 | return-path | Ground plane: minimum interruptions; individual holes are harmless, large slots are not; never let a slot cut across high-di/dt return paths (under fast logic or switching-current tracks); even a narrow track bridging two plane segments is better than none; HF return current concentrates under its signal track. Cross-hatched plane acceptable if warping/resist crazing is a concern | no slot under high di/dt tracks | plane cutouts vs tracks | all planes | inspect | §2.2.4 p.62, Fig 2.14/2.15 | high |
| WILSON-072 | solder | Pads on surface planes/large copper areas must be broken out via one or more short narrow tracks (thermal relief) for reliable soldering; not needed for internal planes (PTH barrel adds thermal resistance) | thermal relief on outer-layer plane pads | pad-plane connections | soldered pads on outer copper pours | inspect | §2.2.4 p.63, Fig 2.16 | high |
| WILSON-073 | stackup | 4-layer plane placement: planes INSIDE for densely packed boards needing HF decoupling (~90% of designs) - close power/ground planes give distributed low-inductance capacitance; planes OUTSIDE only for few-component, many-track boards (backplanes) where E-field screening matters | planes inner, adjacent, close | stackup | 4-layer | inspect | §2.2.4 p.63-64, Fig 2.17 | high |
| WILSON-074 | stackup | Multiple identical ground planes (8+ layers) so each signal layer is adjacent to a plane; stitch planes together with vias at frequent, short intervals; never split ground with x-y "moats" if any signal crossing them is high-frequency or low-level | stitch vias frequent; no moats for critical signals | stackup | multilayer | inspect | §2.2.4 p.64 | high |
| WILSON-075 | fab | Surface finish: HASL usual for SM (flat for paste); gold/nickel for connector contacts; silver for RF loss; carbon ink for keypads/low-spec resistors. Plating thickness from fractions of a um to > 10 um per mating-cycle need; peelable mask protects gold fingers during wave solder | none | finish | outer layers | review | §2.2.5 p.64-65 | high |
| WILSON-076 | fab | Solder resist: screen-printed epoxy needs 0.3-0.4 mm misregistration/bleed allowance pad-edge to resist-edge (fine tracks between pads may be left exposed; may crack over tin-lead areas when wave soldered); photo-imaged film registration better than 0.1 mm - use for dense boards; liquid photo-imageable now usual. Resist is essential for dense wave-soldered SM boards | resist clearance 0.3-0.4 mm (screen), < 0.1 mm (photo) | resist type | mask design | inspect | §2.2.6 p.65-66, Fig 2.18 | high |
| WILSON-077 | connectors | Wire-to-board: direct solder OK only on PTH boards; on non-PTH use second hole strain relief, staked pins or fish-beads. Multi-way connectors: parallel several ways for each power and ground rail; check insertion/withdrawal force; use nut-and-bolt fixed moldings; tighten fixings BEFORE soldering pins (state on drawing) | >= 2 parallel contacts per power/ground rail | connector | board connectors | inspect | §2.2.7 p.66-67, Fig 2.19 | high |
| WILSON-078 | connectors | Edge connectors: keying slot in finger pattern; gold plate fingers including SIDES; tolerance board thickness (contact pressure) and machining; route spare contacts to dummy inboard pads; avoid multi-row < 0.1 inch high-density connectors unless essential | none | connector | edge-connector boards | inspect | §2.2.7 p.67-68 | high |
| WILSON-079 | assembly | Wave soldering SM: orient IC packages along the direction of board travel; rows of adjacent pins across the direction of flow (parallel to the wave) to avoid bridges; observe minimum spacing; larger pads to absorb placement tolerance (adhesive fixes position); max SM component height limited by wave detachment. Reflow: smaller pads, orientation not critical; watch shadowing and differing heat absorption. Never use wave pad dimensions for reflow | none | solder process | SMT layout | inspect | §2.3.1 p.69-72 | high |
| WILSON-080 | assembly | SM board quality: surface flatness; solder resist essential; photo-imageable resist preferred (thickness & window tolerance); no resist bleed onto pads; HASL to avoid reflowed-tin bumps | none | fab spec | SMT | inspect | §2.3.1 p.72 | high |
| WILSON-081 | reliability | CTE mismatch: do not mount larger ceramic chip components or leadless chip carriers (LCC) directly on epoxy-fibreglass (cracks component or track under thermal cycling); leaded SM (SO, flat-pack, J-lead PLCC) and small chip ceramics are acceptable | none | package type, substrate | SMT reliability | inspect | §2.3.1 p.72 | high |
| WILSON-082 | test | Never place test probes on component leadouts (damage; probe pressure masks bad joints). Bring every test node to a dedicated test pad with no component connection, on the side opposite the components; pads need be no more than 1 mm dia. Dense double-sided SM -> use JTAG/boundary scan | test pad dia ~1 mm, component-free, opposite side | net list | ICT | inspect | §2.3.1 p.72 | high |
| WILSON-083 | assembly | Placement producibility: components/packages facing the same way on a defined grid; single lead pitch for tubular parts (0.4 or 0.5 inch popular); all IC pin-1 to the same corner; polarised parts same orientation; spacing for test probes / insertion guides; clear "stacking edge" on one or two board edges for handling/wave machinery; precision parts away from power dissipators | none | placement | all boards | inspect | §2.3.2 p.73 | high |
| WILSON-084 | dfm | Legend: print on flat surfaces, never over/near holes (allow tolerances); tent or fill vias in legend areas; one consistent polarity-indication convention across all boards; consider grid-reference IDs on dense boards | none | silkscreen | all boards | inspect | §2.3.3 p.73-74 | high |
| WILSON-085 | thermal | Conduction: Q = k*A*(TH - TL)/L; thermal resistance R_theta = L/(k*A) (k = thermal conductivity, A = area, L = path length) | R_th = L/(k*A) | k, A, L | any conductive path | calc | §2.3.4 p.74-75, Fig 2.25 | high |
| WILSON-086 | thermal | Forced-air flow at sea level to remove Wloss with rise dT: Airflow[cfm] = 1.76 * Wloss / dT; Airflow[lpm] = 28.32 * 1.76 * Wloss / dT. Altitude reduces convection effectiveness | cfm = 1.76*W/dT; lpm = 28.32*1.76*W/dT | W, dT (C) | forced convection | calc | §2.3.4 p.75 | high |
| WILSON-087 | thermal | Radiation: P_rad = 5.67e-8 * E * (T^4 - Tambient^4) [W/m^2, T in K]; emissivity E per Table 2.3 (polished Al 0.04, painted Al 0.9, rough Al 0.056, matt anodised Al 0.8, rolled bright Cu 0.03, plain steel 0.5, painted steel 0.8) | Stefan-Boltzmann | E, T | radiated heat to neighbours | calc | §2.3.4 p.75, Table 2.3 | high |
| WILSON-088 | reliability | CTE (Table 2.4): Al 24e-6, brass 19e-6, steel 13e-6, Cu 17e-6, Au 14e-6, Ag 18e-6 /C; bonded dissimilar materials crack under thermal shock; estimate stress from expansion + Hooke's law (F = -kx). Thermal cycling stresses solder joints (internal cracks in solder; external cracks at bond interface) | see values | materials, dT | thermal shock / cycling | calc | §2.3.4 p.76-77, Table 2.4 | high |
| WILSON-089 | reliability | MTBF model: lambda_m = sum_i (A_ti * S_i * lambda_i) over n modules; thermal accelerator A_ti = exp( (ea/k) * (1/Tref - 1/Top) ), k = 8.6e-5 eV/K, ea = activation energy (eV), T in K; Fig 2.28 plots failure-rate ratio vs temperature relative to 25 C | Arrhenius | ea, Tref, Top, S_i, lambda_i | reliability prediction | calc | §2.3.4 p.77-78, Fig 2.28 | high |
| WILSON-090 | materials | Surface insulation resistance between parallel conductors on a clean board: Ri = 160 * Rm * (w/l), Rm = material surface resistance (Table 2.1), w = spacing, l = parallel length. Real boards: 10-1000x lower under normal conditions (plating, solder, dust, moisture, temperature); worse in severe environments | Ri = 160*Rm*w/l; derate /10 .. /1000 | Rm, w, l | high-impedance / precision nodes | calc | §2.4 p.78-79 | high |
| WILSON-091 | materials | High-impedance nodes: keep operating impedances low; replace long-time-constant analog integrators / S&H with digital; take critical node off-board to a PTFE stand-off; shorten and space high-Z tracks; never run a power rail past a high-Z node biased near 0 V (unwanted divider) | none | net list | high-Z circuits | inspect | §2.4 p.79 | high |
| WILSON-092 | materials | Guarding: surround high-Z node with a guard trace driven from a low-impedance point at the same potential (Fig 2.29 for follower/inverting/non-inverting op-amps); guard on BOTH sides of a double-sided board; width irrelevant for surface leakage, wider helps bulk leakage | none | op-amp config | high-Z inputs | inspect | §2.4.1 p.79-80, Fig 2.29 | high |
| WILSON-093 | process | Conformal coating only after all else fails (RH ~100%, conductive/organic contamination, corrosive atmosphere). Pre-coat: vapour degrease, rinse in DI water or IPA, oven bake 2 h at 65-70 C (higher if parts allow), handle with gloves, bag with desiccant. Apply >= 2 (preferably 3) coats, dry between; mask connectors/trimmers; ALL production test before coating; acrylics/polyurethanes are reworkable, others not; can double production cost. Coating does not permit closer spacing | bake 2 h @ 65-70 C; >= 2-3 coats | environment class | severe environments | review | §2.4.2 p.80-82 | high |
| WILSON-094 | process | Prototype PCB service: fastest normal double-sided PTH turn-round 4-5 days at 2-5x the production-quantity price; pooling/panelisation shares tooling cost; stay with a proven supplier | 4-5 days; 2-5x cost | quantity | procurement | review | §2.5.2 p.83 | high |
| WILSON-095 | components | Thick-film chip resistor power rating is governed by the PCB pad thermal design: if running near rated power, verify pad layout against the manufacturer's recommended pad geometry | P_actual near P_rated -> pad check | pad geometry, P | SM chip resistors | inspect | §3.1.1 p.89 | high |
| WILSON-096 | components | Resistors printed directly on FR4 are very poor quality; never use where a stable, predictable value is required | none | resistor type | printed resistors | review | §3.1.1 p.90 | high |
| WILSON-097 | components | Wirewound resistors for medium/high power (> 2 W); noticeably inductive - avoid in HF / pulse circuits; aluminium-housed types > 100 W on a heatsink | P > 2 W -> wirewound | P, frequency | power resistors | review | §3.1.1 p.90 | high |
| WILSON-098 | components | Precision resistors: "precision" metal film ~10x better than standard at >= 10x price; drift < 10 ppm/C brings thermal EMF, mechanical/thermal stress, termination resistance into play (unit cost in pounds, delivery months) | tempco < 10 ppm/C = special | tempco requirement | precision circuits | review | §3.1.1 p.90 | high |
| WILSON-099 | components | Worst-case potential divider: with R1 at +K and R2 at -K tolerance, V'/V = 1 - 2K*R1/[R2*(1-K) + R1*(1+K)]; for equal resistors the output variation equals the resistor tolerance. Example 10 V into two 68 k 5% -> 4.75 V / 5.25 V (+/-5%). Check all critical combinations (both corners); use a simulator for complex networks | V'/V = 1 - 2K*R1/(R2*(1-K) + R1*(1+K)) | R1, R2, K | any divider / ratio | calc | §3.1.2 p.91, Fig 3.2 | high |
| WILSON-100 | components | Normal-distribution tolerance model: 68.2% of parts within +/-1 sigma, 95.45% within +/-2 sigma, 99.73% within +/-3 sigma; designers work to 3 sigma ("six-sigma design" = +/-3 sigma). Model a toleranced parameter as r = normal(mean, mean-3sigma, mean+3sigma), e.g. normal(100, 90, 110) for 100 ohm with 3 sigma = 10 ohm (measured example mean 99.949 ohm, sigma 3.3854 ohm, 1 of 1000 outside +/-3 sigma) | tolerance = 3*sigma | mean, sigma | Monte Carlo / tolerance analysis | sim | §3.1.2 p.92-95, Eq 3.1-3.5, Fig 3.3-3.6 | high |
| WILSON-101 | components | NEVER assume tolerance averaging across several resistors: a batch of 5% parts may all lie within 1% of each other but 4% off nominal (manufacturer screened out the tight-tolerance parts, leaving "holes"). Do worst-case, not statistical, for critical paths | worst-case corners | tolerances | production design | calc | §3.1.2 p.95 | high |
| WILSON-102 | components | Standardise on 1% or 2% metal film (negligible cost premium); extreme low/high values may not exist in tight tolerances; below 1% use precision types (custom values). Standard values per IEC 60063 E6/E12/E24/E48/E96 (Table 3.3) | E-series | value | BOM policy | review | §3.1.2 p.95-96, Table 3.3 | high |
| WILSON-103 | derating | Standard metal-film / chip tempco +/-50 to +/-200 ppm/C: a 200 ppm/C part can shift up to 1% over 50 C. Carbon film -150 to -1000 ppm/C depending on value; precision wirewound/metal film/bulk metal reach 1 ppm/C | dR/R = tempco * dT (e.g. 200e-6 * 50 = 1%) | tempco, dT | value stability | calc | §3.1.3 p.95-96 | high |
| WILSON-104 | components | Reference divider: divider resistors must match the reference's stability (no 30 ppm/C reference with 200 ppm/C resistors). Worked case: Vout = 1.00 V +/-1.5%, 30 ppm/C from LM385B-1.2 (1.235 V +/-1%, 20 ppm/C), R3 = 10 k, R2 = 2.35 k (E96: 2.37 k) -> resistor tolerance must be better than 1.4% and tempco better than 26 ppm/C -> 1%, 25 ppm metal film | tol_R < 1.4%, tc_R < 26 ppm/C for that spec | Vref tol/tc, target tol/tc | reference dividers | calc | §3.1.3 p.96, Fig 3.7 | high |
| WILSON-105 | derating | Stability applications: minimise or at least keep constant the power dissipated in the resistor; check manufacturer temperature-rise vs power graph | none | P | precision resistors | review | §3.1.3 p.97 | high |
| WILSON-106 | derating | Rule of thumb for reliability: never dissipate more than HALF the rated power in any component. Hot-spot temperature adds to max ambient. Compute power at worst-case conditions (e.g. nominal 12 V rail that can reach 17 V -> nearly 2x dissipation) | P_actual <= 0.5 * P_rated, at worst-case V | P_rated, V_max | all components | calc | §3.1.4 p.97 | high |
| WILSON-107 | components | Helical-cut film resistors are low-Q inductors; at RF use carbon composition / ceramic-carbon, non-inductive metal film/foil, or chip resistors (inherently low L) | none | f | RF | review | §3.1.5 p.97-98, Fig 3.8 | high |
| WILSON-108 | components | Pulse/snubber resistors: helical film types arc between turns; wirewound self-inductance forms a low-Q tuned circuit that can INCREASE the transient seen by the switch; use carbon composition or pulse-characterised chip/metal glaze types; same for telecom surge series resistors | none | pulse V, resistor type | snubbers, surge protection | review | §3.1.6 p.98, Fig 3.9 | high |
| WILSON-109 | derating | Limiting element voltage (LEV): max continuous voltage across the resistor regardless of power. Example: 470 k, 0.33 W, 1206 needs 394 V for rated power but LEV = 200 V, so continuous dissipation limited to 85 mW. Check V_applied <= LEV, incl. peak pulse voltage on low-value parts | P_allowed = min(P_rated, LEV^2/R) | R, LEV, V | high-value / pulsed resistors | calc | §3.1.6 p.98-99 | high |
| WILSON-110 | derating | Repetitive pulse power: rectangular pulse P_avg = (V^2/R)*(tau/T) <= P_rated; exponential pulse P_avg = (V^2/R)*(tau'/(2T)) <= P_rated, V = peak pulse voltage, T = period, tau = pulse width, tau' = time constant to 0.37*V. Derate further for pulse duration > 1 ms or duty cycle > 10-20% (film/wirewound must dissipate in the element itself); use manufacturer pulse curves | see formulas | V, R, tau, T | pulsed resistors | calc | §3.1.6 p.99 | high |
| WILSON-111 | components | Current-sense resistors: e.g. 10 mohm gives 50 mV at 5 A; bulk metal chips/solder-in wire down to 3 mohm at 1-10 W. Use four-terminal (Kelvin) connection with force and sense tracks arriving separately at the pads (or a true 4-terminal part); minimise sense loop area (magnetic pickup); design for thermal symmetry at both terminations (thermocouple EMFs cancel only if both ends at the same temperature) | Kelvin connection mandatory | R, I | low-value sense resistors | inspect | §3.1.7 p.99-100, Fig 3.10 | high |
| WILSON-112 | components | Sense-resistor self-inductance: 100 nH at 400 Hz is 0.25 mohm -> 5% error on a 5 mohm sense resistor; avoid wirewound for AC sensing, prefer bulk metal or chip | Z_L = 2*pi*f*L vs R_sense | L, f, R | AC current sensing | calc | §3.1.7 p.100 | high |
| WILSON-113 | components | Multi-megohm resistors (to 1e14 ohm, glass encapsulated): handle by leads only; add a guard electrode; self-capacitance matters - 100 Gohm with 1 pF gives 0.1 s time constant | tau = R*C_self | R, C | high-value resistors | calc | §3.1.7 p.100 | high |
| WILSON-114 | protection | Inrush-limiting / sacrificial series resistor at a PSU input must be specified for a predictable fusing characteristic (time to open vs energy) and be flameproof; use metal oxide / metal film parts characterised for this | none | fault energy | mains input | review | §3.1.8 p.100 | high |
| WILSON-115 | cost | Leaded resistor bought for < 1 p costs 5-10 p once inserted; networks trade package cost vs insertions; SM placement cost per part is negligible. Do not "gather up" widely separated resistors into a network at the expense of long tracks | none | production cost model | BOM/layout | review | §3.1.9 p.101 | high |
| WILSON-116 | components | Thick-film network: absolute tempco typ 250 ppm/C but tracking 50 ppm/C between elements; thin film ~10x better. Use tracking networks for ratio-critical circuits (differential op-amp: R1/R2 = R3/R4 for CMRR; unity gain all equal); derive fractional references from equal-valued elements in one package (series/parallel) | tracking 50 ppm/C (thick), ~5 ppm/C (thin) | ratio spec | diff amps, dividers | review | §3.1.9 p.101-102, Fig 3.11/3.12 | high |
| WILSON-117 | components | Potentiometers: use only where signal frequency x circuit resistance < 1e6 Hz*ohm; prefer digital trimming / auto-zero (op-amps < 0.5 mV offset, choppers a few uV) | f * R < 1e6 Hz*ohm | f, R | pot applications | calc | §3.2 p.102 | high |
| WILSON-118 | components | Trimmers: carbon +/-20% tolerance, not for professional use; cermet 10 ohm-2 Mohm, +/-10% (cheap +/-20%), best for HF; wirewound: low tempco, higher power, low noise, tight tolerance, max ~50 kohm, poor resolution, not for HF; single-turn < 270 deg travel; multi-turn (4, 10, 12, 15, 20, 25 turns) ~2x cost/size | see values | requirement | trimmer selection | review | §3.2.1 p.103 | high |
| WILSON-119 | components | Panel pots: carbon ~0.4 W; cermet/wirewound 1-5 W; conductive plastic for long life / position transducers | P ratings | P | panel controls | review | §3.2.2 p.104 | high |
| WILSON-120 | components | Pot wiper rules: draw as little DC through the wiper as possible (use wirewound if current is significant); divider mode into high impedance; DC-blocking capacitor in signal paths; some types need a minimum wetting current (printed "25 mA" - m/u prefix OCR-ambiguous) kept low | I_wiper -> minimum | circuit | all pots | inspect | §3.2.3 p.104, Fig 3.13 | high |
| WILSON-121 | components | Rheostat connection: tie the wiper to one end of the track so a lifted wiper leaves max = end-to-end R instead of open circuit. Wiper current <= spec; if unspecified assume the current giving rated power through the wiper alone, absolute max 100 mA for small trimmers. End resistance prevents ratio 0 or 1 | I_wiper <= 100 mA (small trimmers) | I | rheostat use | inspect | §3.2.3 p.104-105, Fig 3.14 | high |
| WILSON-122 | components | Adjustability: use a series fixed resistor so the trimmer spans only the needed range; multi-turn for fine settability (Fig 3.15); wirewound ~"100-way switch"; place side-adjust pots at board edge, top-adjust in the middle; minimise the number of trims | none | trim range | production trims | inspect | §3.2.3 p.105-106 | high |
| WILSON-123 | components | Pot law accuracy: low-cost linearity unspecified / ~10%; good quality ~5%; < 1% possible at a price; log pots worse. Tolerance spec refers only to end-to-end R | linearity 10% / 5% / <1% | use | position sensing | review | §3.2.3 p.106 | high |
| WILSON-124 | assembly | Electro-mechanical parts (pots, relays, switches) dislike soldering thermal shock and washing (sealed: fluid ingress via damaged seal; open: fluid contaminates); many manufacturers hand-fit them after solder & clean | none | part type | assembly flow | review | §3.2.3 p.106-107 | high |
| WILSON-125 | components | Film capacitors: metallised film self-heals (thinner dielectric, ~1.5 um min, higher C/volume); film-foil needs thicker dielectric (lower C, larger case) | none | type | film cap selection | review | §3.3.1 p.107 | high |
| WILSON-126 | components | Polyester: highest C/volume of films, non-linear high tempco, tan d ~8e-3 at 1 kHz/20 C (varies with T and f) - coupling/decoupling only. Polycarbonate: near-flat C(T) (~-1% at extremes), tan d < 2e-3 - filters/timing. Polypropylene: -200 ppm/C, tan d ~3e-4 nearly constant with T - high power/high frequency (SMPS, deflection). Polystyrene: -125 ppm/C, tan d ~5e-4; PP/PS dielectric absorption 0.02-0.03% (best for S&H); PP/PS limited to 85 C (some PS 70 C, some PP 100 C) | see values | application | film capacitor choice | review | §3.3.1 p.110-111, Fig 3.17 | high |
| WILSON-127 | protection | Across-the-line mains suppression capacitors: use metallised paper (minimal carbon deposit on breakdown -> no ignition); plastic film can self-heat and ignite without blowing the fuse | none | mains suppression | X capacitors | review | §3.3.1 p.111-112 | high |
| WILSON-128 | components | Class 1 ceramic COG/NP0: near-zero tempco (0 +/- 30 ppm/C), negligible C and tan d change with V or f, tan d ~0.001, 1 pF-27 nF - stability/timing. X7R: up to ~1 uF, non-linear +/-15% over -55..125 C, tan d 0.025 at 20 C/1 kHz, C and tan d shift up to 10% with V and f - general coupling/decoupling only; X5R lower upper temp. Y5V/Z5U: > 50% change with T and V, Z5U rated +10..+85 C, Y5V -30 C, tolerance -20/+80%, WV <= 100 V, up to 2.2 uF - IC decoupling only | see values | dielectric | MLCC choice | review | §3.3.2 p.113, Table 3.4 | high |
| WILSON-129 | components | Single-layer ceramic: barrier-layer (low Vbd, high tan d, C*V constant per disc) only advantage cost; Type 1 (low-K) tempco +100 to -1500 ppm/C linear, stable vs V and f, tan d ~1.5e-3 at 1 MHz (printed "1.5 x 10"), <1 pF..~500 pF - RF; Type 2 (hi-K, barium titanate) 100 pF-47 nF, variable with V, f, T, age, kV ratings by dielectric thickness | see values | dielectric | disc ceramics | review | §3.3.3 p.114 | high |
| WILSON-130 | components | Aluminium electrolytic: polarised (reverse bias -> hydrogen, overpressure); operate below rated V (surge rating = forming voltage without safety factor); general range 1-4700 uF (0.1 uF to tens of thousands uF available) | V_applied < V_rated | V | electrolytics | review | §3.3.4 p.114-115 | high |
| WILSON-131 | components | Electrolytic leakage: general purpose 0.01*C*V to 0.03*C*V uA (C in uF, V = rated V; printed "mA", uA is the standard convention); low-leakage types 0.002*C*V uA; leakage falls to ~1/10 of rated at ~40% of rated voltage; can be 10x rated value at max operating temperature; higher when first energised | I_leak = (0.01..0.03)*C*V uA | C, V, T | timing / coupling with electrolytics | calc | §3.3.4 p.115 | high |
| WILSON-132 | derating | Electrolytic ripple current: observe published RMS I_R rating (increases with frequency, decreases with temperature); derive a correction factor for non-sinusoidal ripple; select higher V or C rating than circuit needs if ripple heating dictates | I_ripple_rms <= I_R(f, T) | ripple waveform | reservoir / SMPS caps | calc | §3.3.4 p.115-116 | high |
| WILSON-133 | components | ESR sets SMPS output ripple (not C); non-solid electrolytic ESR rises dramatically below 0 C - "impedance ratio" (ESR at sub-zero / ESR at 20 C) usually 3-4, may be much worse; solid types better | V_ripple ~ I_ripple * ESR; ESR(cold) = 3..4 x ESR(20 C) | ESR, T | SMPS output filters | calc | §3.3.4 p.116, Fig 3.20 | high |
| WILSON-134 | reliability | Electrolytic temperature/lifetime: C varies ~+/-20% over temp (falls when cold; solid types 2x better); tan d 0.1-0.3 at 100 Hz/20 C (worse cold and at HF; higher-V ratings lower tan d); typical -40..+85 C (extended -55..+105/125 C); non-solid life DOUBLES for each 10 C reduction in operating temperature; solid types don't dry out | L = L0 * 2^((T0 - T)/10) | T | electrolytic life | calc | §3.3.4 p.116 | high |
| WILSON-135 | reliability | Electrolytic shelf life (years at 25 C): Al2O3 degrades without polarising voltage -> high leakage; re-form via current-limited forming voltage; don't use in circuits without normal polarising voltage; products stored > 1-2 years must tolerate high leakage for the first minutes of operation | none | storage time | electrolytics | review | §3.3.4 p.117 | high |
| WILSON-136 | mechanical | Electrolytics are the largest/heaviest parts: choose for terminal mechanical strength under vibration or provide additional mounting | none | mass, vibration | vibrating assemblies | inspect | §3.3.4 p.117 | high |
| WILSON-137 | components | Solid tantalum: -55..85 C or to +125 C, far higher reliability than Al; leakage ~0.01*C*V uA; tan d 0.04-0.1 (~2x better than Al); dC over temp +/-15% to +/-3%; some reverse voltage tolerated; chips 0.1-470 uF; supply risk - multi-source or consider niobium oxide | see values | application | tantalum use | review | §3.3.5 p.117 | high |
| WILSON-138 | components | Worst-case capacitance: C_actual = C * [1 +/- tol] * [1 +/- dT*tempco] * [1 +/- dV*Vcoeff] * [1 +/- df*fcoeff] * [t*aging]. Example 0.1 uF Z5U 50 V (-20/+80%, +22/-56% over +10..85 C, -35% at 60% rated V, -3% at 10 kHz / -6% at 100 kHz, -6% per 1000 h) over 5-30 V and 10-100 kHz: 0.219 uF max, 0.0202 uF min = 11:1. Same 0.1 uF 10% polycarbonate 63 V: 0.089-0.11 uF; 20% tantalum bead 35 V: 0.038-0.125 uF (frequency loss 0.5 at HF) | product of factors | datasheet coefficients | any capacitor in a value-critical role | calc | §3.3.6 p.118-119 | high |
| WILSON-139 | components | Integrator / timing capacitors: Vout = -Vin*t/(C*R); voltage coefficient of Z5U (and even X7R) produces gross non-linearity; choose NP0/COG, polycarbonate, polystyrene, polypropylene (in that order of preference) and/or under-run (e.g. 100 V part with <= 1 V ramp); for long stable periods divide a high frequency digitally instead of using large C | dielectric class + V derating | C, dielectric | timing, tuning, oscillators, ADC ramps | review | §3.3.6 p.119 | high |
| WILSON-140 | components | Series capacitors for voltage: DC divides by the ratio of leakage resistances Rdc (tens to thousands of Mohm, undefined, plus PCB leakage), not by C -> unpredictable overvoltage; add bleed resistors across each capacitor sized comfortably BELOW the minimum specified leakage resistance; bleeders also define discharge time to a safe voltage on HV reservoirs | R_bleed << Rdc_min | Rdc_min, V | series caps, HV reservoirs | calc | §3.3.7 p.119-121, Fig 3.21/3.22 | high |
| WILSON-141 | components | Dielectric absorption (voltage memory): DA = dV/(VA - VB) for t >> ts; modelled by Rd-Cd in parallel; reduce error by short hold of old voltage and measuring soon after sampling; polystyrene and polypropylene best at 0.01-0.02% | DA(PS, PP) = 0.01-0.02% | dielectric | sample-and-hold | review | §3.3.8 p.121, Fig 3.23 | high |
| WILSON-142 | decoupling | Capacitor self-resonance: C-ESR-ESL series circuit; above SRF the part is a low-Q inductor. Typical: 47 uF tantalum SRF ~500 kHz (broad); 100 pF COG chip ~100 MHz (sharp); a 1 MHz-SRF tantalum is useless for 10-20 MHz clock decoupling - parallel with e.g. 10 nF ceramic/film (SRF 10-100 MHz); ESL set by lead + track length and body size (chips lowest); beware inter-component (anti-)resonances between the large part's ESL and the small C | f_SRF = 1/(2*pi*sqrt(ESL*C)) | C, ESL | decoupling, RF | sim | §3.3.9 p.121-123, Fig 3.24/3.25 | high |
| WILSON-143 | magnetics | Air-cored inductors: low loss but > 100 uH impractical (size/wire); at LF winding R approaches reactance. Q = w*L/Req; tan d = 1/Q | Q = wL/Req | L, f, R | inductor choice | calc | §3.4.1 p.123, Fig 3.26 | high |
| WILSON-144 | magnetics | Permeable cores: extra loss (lower Q), saturation (L drops at high current), hysteresis (remanence), wide L tolerance (control with an air gap), permeability and loss vary with temperature and vanish above the Curie point. Use published B-H curve to set power handling | none | core material | all cored inductors | review | §3.4.1 p.124, Fig 3.27 | high |
| WILSON-145 | magnetics | Ferrite selection: MnZn high permeability, losses rise fast with f (LF use); NiZn lower permeability, usable to ~200 MHz, resistivity several orders higher, higher Curie point. Soft magnetic: coercivity < 1 kA/m; hard: > 10 kA/m. Standard core shapes: RM (IEC 60431), E, EP, EC. Iron powder: permeability <= ~30, very hard to saturate - HF tuned cores and suppression chokes | NiZn f_max ~200 MHz; iron powder mu <= 30 | f, current | core material choice | review | §3.4.1 p.124-125 | high |
| WILSON-146 | magnetics | Hysteresis metrics (Table 3.7): BR remanence, HC coercive force, BMAX, HMAX, mu_MAX, mu_i; B-H loop area = energy lost per cycle -> core loss = area x frequency; minor loops must be non-congruent for wideband transformer models | P_core = loop_area * f | B-H data | magnetics modelling | calc | §3.4.2 p.127-129, Table 3.7, Fig 3.32 | high |
| WILSON-147 | magnetics | Leakage inductance: measure with secondary shorted, inductance across primary (bridge / impedance analyser) over the frequency range of interest at LOW signal level (IEEE Std 389-1996); or FEA with equal-and-opposite winding currents. Reduce by interleaving (sectionalised) or bifilar windings; split bobbins increase it | none | winding topology | SMPS transformers, line transformers | measure | §3.4.2 p.129-130, Fig 3.33/3.34 | high |
| WILSON-148 | magnetics | Winding self-capacitance: never wind directly on the ferrite (high er raises Cp several times) - use a bobbin; single layer lowest Cp; scramble/wave winding cuts Cp ~20% vs layer winding; two-section former cuts Cp ~3x. Measure per IEEE Std 389-1979 resonant method | Cp reduction: scramble -20%, 2-section /3 | construction | HF magnetics | inspect | §3.4.3 p.131, Fig 3.35 | high |
| WILSON-149 | magnetics | Winding DC resistance: Rdc = 4*rho_c*N*lw/(pi*d^2) (N turns, lw mean turn length, d wire diameter); rho_Cu = 1.709e-8 ohm*m at 20 C, tempco 0.00393/C (a 40 C rise is common in power parts) | Rdc = 4*rho*N*lw/(pi*d^2) | N, lw, d, T | all windings | calc | §3.4.4 p.132 | high |
| WILSON-150 | magnetics | Skin depth D = sqrt(rho_c/(pi*mu0*mu_c*f)); skin effect negligible if d/D < 2; for d/D > 5 the AC-resistance factor is approximately 1 + F ~ (1/4)*(d/D + 1) (printed "1 + F ~ 1/4 (d/D + 1)", i.e. Rac/Rdc); proximity-effect loss for round conductors P_pe = pi*w^2*Bmax^2*l*d^4/(128*rho_c), with an additional frequency factor Gr -> 1 at LF and growing for d/D > 4 (printed fragment not reliably recoverable). Measure Rac with an impedance analyser at low signal level | D = sqrt(rho/(pi*mu0*mur*f)); d/D < 2 ok; Rac/Rdc ~ (d/D + 1)/4 for d/D > 5 | d, f, rho | HF windings, litz decisions | calc | §3.4.4 p.132-133, Fig 3.36/3.37 | medium |
| WILSON-151 | magnetics | Tuned-circuit inductors: predictable L, high Q; pot cores at LF, other ferrites or iron dust > ~1 MHz; lower permeability material for best stability/tolerance; consider disaccommodation (permeability step after shock then slow relaxation); varnish-impregnate winding/bobbin/core; never hard-encapsulate (shrinkage cracks brittle core) | none | environment | stable inductors | review | §3.4.5 p.134 | high |
| WILSON-152 | magnetics | Power chokes/transformers: energy = L*I^2 (as printed; conventionally 0.5*L*I^2); choose high saturation flux density; hysteresis dominates loss at high f; gapped MnZn ferrite or iron dust (distributed gap) for higher saturation current at reduced effective permeability | E ~ L*I^2 (printed) | I_pk, Bsat | SMPS magnetics | calc | §3.4.5 p.134-135 | high |
| WILSON-153 | emc | Suppression chokes want HIGH loss ferrite (energy absorbed, not reflected); ferrite bead on a wire gives several tens of ohms complex impedance at HF; monolithic ferrite chips for SM | Z_bead ~ tens of ohm | f | EMI filtering | review | §3.4.5 p.135, Fig 3.38 | high |
| WILSON-154 | protection | Inductive switch-off transient V = -L*di/dt: amplitude limited only by Q and self-capacitance or by switch breakdown; relay coils commonly produce several x supply, hundreds of volts from 12 V; transistor avalanche may survive on the bench and fail in the field; contact spark erosion when small contacts drive coils. Coil C is never specified -> measure the transient in circuit | V_pk >> V_supply (measure) | L, Q, C_self | every switched inductor / relay / solenoid | measure | §3.4.6 p.135-137, Fig 3.39/3.40 | high |
| WILSON-155 | protection | Transient clamps: (a) freewheel diode across coil - clamps positive spike to supply; rate diode for coil-R-limited flyback current, V rating = supply; lengthens drop-out time. (b) Zener across coil (or series diode with switch) also clamps negative excursions and supply transients; clamp voltage must exceed worst-case supply + zener tolerance; sized to trade turn-off time. (c) AC coils: RC snubber across switch or coil (low supply impedance); C no larger than needed (slows switch, leaks current to load when open); R as high as consistent with snubbing (Section 4.2.6 values) | diode: V_R >= V_supply; I_F >= I_coil | coil V, I, L | DC coils / AC coils | inspect | §3.4.6 p.137-138, Fig 3.41 | high |
| WILSON-156 | components | Quartz crystal: AT-cut (35 deg 21') for general use - no subsidiary resonances, cubic-plus-linear f(T); X/Y cuts have large tempco and low f limit. Equivalent circuit: series L (henries), C (femtofarads), R (tens-hundreds ohm), parallel C0 (several hundred x C); Q 30,000-100,000; fs = 1/(2*pi*sqrt(L*C)); fp = 1/(2*pi*sqrt(L*Cx)), Cx = series(C, Cp), Cp = C0 + external C. Crystal runs at marked frequency only at its quoted load capacitance; series C pulls fs up, parallel C pulls fp down | fs, fp formulas | L, C, C0, C_load | crystal oscillators | calc | §3.5-3.5.1 p.138-140, Fig 3.42/3.43 | high |
| WILSON-157 | components | Pierce (parallel) oscillator: CMOS/high-Z only; runs at very low power (printed "down to 1 mA"; m/u prefix ambiguous) but slow to start (up to ~1 s); Rf 10-15 Mohm; C1, C2 in series plus strays (<= 10 pF with good layout) = load capacitance; C2:C1 ~ 3:1 (C2 variable for trim). Series-mode oscillator starts fast, higher supply current, works with low or high Z devices | C_load = C1*C2/(C1+C2) + C_stray(<=10 pF); C2/C1 ~ 3 | C_load spec | clock oscillators | calc | §3.5.2 p.140-141, Fig 3.44 | high |
| WILSON-158 | components | Crystal drive level: include series drive-limiting resistor Ra; AT-cut max drive 0.5-1 mW; too high -> instability/damage, too low -> slow/no start, interference susceptible; 32.768 kHz watch crystals need Ra of tens-hundreds kohm; motional R spreads 2-3:1 unit to unit -> design start-up with 3x the quoted R | P_drive <= 0.5-1 mW; design R_m = 3 x quoted | Ra, crystal R | crystal oscillators | calc | §3.5.2 p.141 | high |
| WILSON-159 | components | Crystal layout: minimise extra capacitance across the crystal (parallel mode); no logic signals near/through the oscillator; ground traces around the crystal to buffer other tracks (jitter/instability otherwise) | none | layout | oscillator layout | inspect | §3.5.2 p.142 | high |
| WILSON-160 | components | Crystal tempco: AT-cut cubic, flat near room temp, worsens toward limits; tuning-fork 32.768 kHz is parabolic ~-0.04 ppm/C^2 with turnover ~25 C: at +85 C or -35 C it is 144 ppm low = 12 s/day loss - unusable for industrial RTCs, use AT-cut | df/f = -0.04e-6 * (T - 25)^2 | T range | RTC / timing | calc | §3.5.3 p.142 | high |
| WILSON-161 | components | Ceramic resonator: tempco ~1e-5/C (quartz < 1 ppm/C, LC 1e-3..1e-4/C); initial tolerance ~+/-0.5% (quartz +/-0.003%); orders of magnitude lower Q -> fast start (good for sleep-mode products); needs load capacitors per manufacturer to avoid spurious modes. Modes: 30 kHz-1 MHz longitudinal, 100 kHz-2 MHz area, 1-10 MHz shear thickness, 2-100 MHz expansion thickness, 10 MHz-1 GHz SAW | tol 0.5%, tc 1e-5/C | accuracy spec | low/mid-performance clocks | review | §3.5.4 p.142-144 | high |
| WILSON-162 | components | Diode equation IF = IS*[exp(VF*q/(k*T)) - 1]; kT/q = 0.025 V at 20 C; rule of thumb VF = 0.6 V, but VF -> 0 at uA/nA (behaves as non-linear resistor) with slope resistance r_d = 0.025/IF ohm at room temperature; VF approaches 1 V near IFmax (hundreds of mA for signal diodes) | r_d = 0.025/IF | IF, T | all Si p-n junctions | calc | §4.1.1 p.147-148, Eq 4.1 | high |
| WILSON-163 | derating | IFmax set by dissipation IF*VF and Tj max (usually 125-200 C); pulsed operation: P_avg = D*P_pk; rectifier surge rating 30-70x average current, quoted for a duration (US: 8.33 ms = one 60 Hz half cycle); extrapolate to other durations with constant I^2*t; VF keeps rising above IFmax. Check reservoir-charging switch-on surge against surge rating | I_surge_allowed(t) = I_surge_spec * sqrt(t_spec/t) | surge duration | rectifiers | calc | §4.1.1 p.148 | high |
| WILSON-164 | components | VF tempco ~ -2 mV/C at constant current (IS exponential in T). Over 0-70 C VF shifts ~150 mV. Example: 10 k/10 k divider from +5 V with series diode (VF 0.45-0.6 V) gives Vo = 2.275 V to 2.2 V, not 2.5 V. VF/IF curves are "instantaneous" (pulse-measured) - do not apply to steady state without self-heating correction | dVF = -2 mV/C * dT | dT | diodes in linear circuits | calc | §4.1.1 p.148-149, Fig 4.3 | high |
| WILSON-165 | components | Diode-pair bias compensation: with R1 = R2, IE = (R2/(R1+R2))*VS/RE if VBE ~ VF; imperfect (different temperatures/currents); one diode acceptable if R1 >> R2; dual transistors for accurate compensation | IE = VS*R2/((R1+R2)*RE) | R1, R2, RE | discrete bias stages | calc | §4.1.1 p.149-150, Fig 4.4 | high |
| WILSON-166 | protection | Reverse breakdown VBR: avalanche current limited only by source impedance; inductive turn-off transients can push blocking diodes into breakdown unnoticed during evaluation - use avalanche-energy-rated diodes where predictable transients exceed VBR | V_R < VBR or use avalanche-rated part | transient V | flyback/blocking diodes | review | §4.1.2 p.150-151 | high |
| WILSON-167 | derating | Reverse leakage IR ~doubles every 10 C: 100 nA at 25 C -> 2.2 uA at 70 C; batch-to-batch variation up to 10x; datasheet max is artificially high vs typical - design to worst-case even if bench samples are far better (prototype diodes are likely low-leakage). Measured 1N4148/1N4004 all < 10 nA at 25 C; 1N4004 below rated V leaks less than signal diodes | IR(T) = IR(25)*2^((T-25)/10) | IR spec, T | high-impedance / low-current circuits | calc | §4.1.3 p.151, Fig 4.5 | high |
| WILSON-168 | components | Junction capacitance few pF to hundreds of pF, falls with reverse voltage (Fig 4.6); small-signal switching: assume constant C, reduce by raising bias; large-signal/rectifying: expect distortion from non-linear C(V) | C_j(V) from datasheet/graph | V_R | HF diode circuits | calc | §4.1.4 p.152 | medium |
| WILSON-169 | components | Reverse recovery: conventional rectifiers 1-20 us; fast recovery 150-200 ns; ultra-fast down to 20 ns; recovery dissipates VR*I - limits diode rating at high f/V. Fast "snap" recovery has the highest di/dt in the circuit -> main EMI source; use soft-recovery diodes. All p-n diodes (even mains rectifiers) generate switching-harmonic interference | trr classes | f_sw | rectifiers in SMPS | review | §4.1.5 p.153-154, Fig 4.7 | high |
| WILSON-170 | components | Schottky vs p-n (Table 4.1): VF ~0.4 V vs 0.6 V at medium current; no charge storage (fast) vs minority-carrier limited; VBR 30-100 V vs > 1 kV achievable; leakage up to 10x higher (same exponential T law); VF tempco ~ -1 mV/C at mA level; cost ~5 p vs 1 p. In a 5 V switcher a 1 V p-n rectifier drop wastes 20% of output power, a 0.5 V Schottky 10% | loss fraction = VF/Vout | Vout, VF | low-voltage SMPS outputs, mixers, fast switching | calc | §4.1.6 p.154-155, Table 4.1 | high |
| WILSON-171 | components | Zener: 2.4 V to ~270 V practical max; working voltage = quoted Vz (at IZ) + (I - IZ)*Rs; keep off the knee (knee current rarely < a few hundred uA - unsuitable for micropower; use band-gap references); Rs minimum around 6.8 V, poor regulation below 5 V and above 100 V - series lower-voltage zeners beat one HV zener | Vz(I) = Vz + (I - IZ)*Rs | IZ, Rs, I | shunt regulators/clamps | calc | §4.1.7 p.155-156, Fig 4.8/4.9 | high |
| WILSON-172 | components | Zener leakage is specified 20-30% below Vz (same T doubling law as diodes) - critical for clamp use. Tempco: tunnelling (< ~5 V, negative tc) vs avalanche (> ~5 V, positive tc); minimum tempco at 4.7-5.6 V; 5.6-5.9 V zener (+2 mV/C) in series with a forward junction (-2 mV/C) gives a ~zero-tc 6.2-6.4 V reference (1N821 series); 7.5 V zener (+4 mV/C) + two junctions ~ 8.4 V. Band-gap references usually win (lower Rs, lower current). Zener breakdown is noisy - decouple with parallel C for precision references | choose 4.7-5.6 V for min tc | Vz | zener references | review | §4.1.7 p.157-158, Fig 4.10 | high |
| WILSON-173 | protection | Zener input clamp worked example: +/-15 V op-amp, 100 V continuous fault input, +/-10 V normal, 10 k source, 0.1% accuracy 0-50 C. Clamp must stay below 15 V - VF(0.8 V) - 5% tolerance -> Vz_max 13.5 V -> BZX79C12 (12 V) reaches 13.5 V at ~25 mA (within 400 mW at 50 C); RIN = (100 - 13.5 - 0.8)/25 mA = 3.4 k -> 3k3. Leakage budget: 0.1% of 10 V = 10 mV across 13.3 k = 0.75 uA; zener 0.1 uA at 25 C/8 V doubles per 10 C -> 0.56 uA at 50 C (just OK). ~30 pF at 10 V with 13.3 k -> 400 kHz -3 dB. Zener clamps are limited to low-Z, LF inputs and waste usable input range; use transient absorbers or rail diodes (§6.2.3) otherwise | RIN = (V_fault - Vz_max - VF)/I_z_max; I_leak(T) <= V_err/R_source | V_fault, Vz, tolerance, IR | analog input protection | calc | §4.1.8 p.158-159, Fig 4.11 | high |
| WILSON-174 | components | Triacs: only for low-power (< 40 A) mains-frequency circuits; with inductive loads the reapplied voltage at current zero can re-fire it (commutating dV/dt) - snubbing required. Thyristor/triac VF 0.8-2 V (p-n-p-n). Gate is a p-n junction: drive from low-impedance current source; trigger is energy-dependent (more energy needed at low temperature); triac quadrant IV least sensitive - prefer negative-going gate pulses | I_load < 40 A for triacs | load, f | thyristor/triac control | review | §4.2.1-4.2.2 p.160-161, Fig 4.13/4.14 | high |
| WILSON-175 | protection | False triggering via anode-gate capacitance: I_gate = C*dV/dt; observe datasheet max dV/dt (snubber), add a low-value gate-cathode resistor or capacitor (sensitive-gate devices are more susceptible), never drive the gate from a pulse transformer alone (leakage inductance is high-Z to dV/dt pulses); overdrive the gate as far as dissipation allows | I = C*dV/dt | C, dV/dt | thyristor gate design | calc | §4.2.3 p.162, Fig 4.15 | high |
| WILSON-176 | components | Holding current IH: several mA to tens of mA even for small thyristors (sets minimum load); short trigger pulses early in the half cycle may fail if load current hasn't reached IH - lengthen pulse or avoid the first tens of degrees; reverse gate bias raises IH, forward bias lowers it (datasheet values with gate open) - a driving transistor's VCEsat of hundreds of mV alters latching | I_load(t_trigger_end) > IH | IH, load | AC phase control | calc | §4.2.4 p.162-163, Fig 4.16 | high |
| WILSON-177 | components | Thyristor turn-on di/dt limit: conduction spreads slowly - add series L = V/(di/dt) if load is not inductive enough; higher gate drive raises permissible di/dt and cuts turn-on delay (typ 1-2 us). Turn-off (thyristor only, by reverse V) = reverse recovery + forward-blocking recovery, tens of us, longer with Tj and current; negative gate bias shortens it | L_series >= V/(di/dt_max) | di/dt spec, V | thyristor switching | calc | §4.2.5 p.163-164 | high |
| WILSON-178 | protection | Snubber (R-C-D across device): C = 0.63*Vpeak/((dv/dt)*RL) with RL = minimum (cold) load resistance, dv/dt = device max spec, Vpeak = max applied voltage (340 V for 240 V mains; allow more for spiky supplies). R = larger of Vpeak/(0.5*(ITSM - IL)) or sqrt(Vpeak/(C*di/dt)); omit D if R <= ~RL; D rated at device voltage with surge 2-3x IL; check resistor pulse rating; a bigger device (higher ITSM) allows lower R; pulse-rated C. Example: 1 kW heater, 240 V, cold RL = 6 ohm, 56 A peak, TIC226M (500 V/us, ITSM 80 A) -> C = 0.63*340/(500*6) = 0.07 uF -> 0.1 uF; R = 340/((80-56)*0.5) = 28.3 -> 27 ohm (di/dt 4.7 A/us); R >> RL so use diode/bridge | C = 0.63*Vpk/(dv/dt*RL); R = max(Vpk/(0.5*(ITSM-IL)), sqrt(Vpk/(C*di/dt))) | Vpk, dv/dt, RL, ITSM, IL, di/dt | thyristor/triac and general dV/dt snubbers | calc | §4.2.6 p.164-165, Fig 4.17 | high |
| WILSON-179 | components | BJT leakage ICBO (collector-base, emitter open) is amplified by following stages in DC-coupled chains: TR1 off-state leakage of several uA (mA for power parts) x gain of TR2 (~200) gives >= 1 mA in the load; a few tens of mV of base offset makes it worse (printed: 1 mA at 600 mV -> "2.5 mA" at 100 mV, x100 x200 -> "50 mA" in RL; prefixes OCR-ambiguous). Add a base-emitter resistor to every leakage-threatened transistor, sized to divert ~1/10 of the on-state base current (example: IB = 1 mA, VBE 0.6 V -> 6 k; then 10 uA leakage (printed "10 mA") develops only 60 mV -> only 45 nA into the base) | R_BE = VBE/(0.1*IB_on) | IB_on, leakage | DC-coupled switching/level-shift stages | calc | §4.3.1 p.165-166, Fig 4.19 | high |
| WILSON-180 | components | VCEsat: ohmic at high IC plus residual 50-200 mV; base drive above IC/10 gives negligible further reduction; tempco < 0.5 mV/C with complex IC/Tj dependence. A saturated driver's VCEsat (hundreds of mV at high power) can hold the next stage partially on - use a base-emitter divider. Darlington VCEsat ~1 V (VCEsat(A) + VBE(B)); VBE doubled; power-switching Darlingtons include low-value internal B-E resistors | IB_on ~ IC/10 max | IC | saturated switches | calc | §4.3.2-4.3.3 p.167-168, Fig 4.20/4.21 | high |
| WILSON-181 | derating | Bipolar SOA limits: IC max, VCE max, P max (IC*VC + IB*VB, specified at 25 C ambient/case - derate with thermal resistance; a power transistor never reaches rated dissipation without a heatsink), second breakdown (thermal current-crowding at high VCE, independent of average Tj; power devices only). Check the operating locus against the datasheet SOA plot | operating point inside SOA at Tj | IC, VCE, t_pulse, Tj | power transistors | calc | §4.3.4 p.168-169, Fig 4.22 | high |
| WILSON-182 | components | hFE (DC gain) is specified min-max, e.g. BC848 110-800 with A/B/C grades 110-220 / 200-450 / 420-800 (no cost penalty for grades); gain falls off either side of the optimised current range (more at high IC), falls at low VCE (large-signal distortion from drive starvation), rises with temperature and falls when cold by up to 2-3x. Never let circuit operation depend on gain; assume gain below datasheet minimum somewhere in the envelope | hFE_design <= hFE_min / (2..3) at cold | hFE spec, IC, VCE, T | all BJT circuits | calc | §4.3.5 p.169-170, Fig 4.23/4.24 | high |
| WILSON-183 | components | BJT switching: turn-on = delay + rise, turn-off = storage + fall; small-signal switching types ton < 50 ns, toff 100-200 ns; general-purpose amplifier types (BC84x) several times slower and unspecified; test circuits overdrive and reverse-bias the base (reverse VBE breakdown only 7-10 V - keep within); times fall with IC. Darlingtons switch slowly (no anti-saturation, no reverse base current). Avoid saturation for speed: emitter-coupled pair (ECL) or base-collector Schottky clamp (Baker clamp) | V_BE_reverse < 7 V | drive, IC | fast switches | review | §4.3.6 p.170-171, Fig 4.25/4.26 | high |
| WILSON-184 | cost | Transistor grading: same die sold under many part numbers by tested gain, breakdown voltage, noise; specify the most relaxed grade acceptable (cheapest, most available) | none | spec | BOM | review | §4.3.7 p.171-172 | high |
| WILSON-185 | components | JFET: majority-carrier, high-Z voltage-controlled; symmetrical channel (except RF-optimised parts - don't reverse); depletion mode; abs(Vp) = abs(VGS(off)); VGS(off) spreads up to 6:1 unit-to-unit - bias design must absorb this (hard at low supply voltage); cost ~10 p vs ~2 p bipolar - reserve for analog switches, RF, current regulators, high-Z amplifiers | VGS(off) spread 6:1 | datasheet range | JFET bias | calc | §4.4-4.4.2 p.172-174, Fig 4.27/4.28 | high |
| WILSON-186 | components | JFET analog switch: off-state gate must be beyond the source by at least VGS(off) -> driver supply must exceed the signal range by several volts and the gate must follow the signal when on; prefer integrated analog switches (characterised feedthrough and Ron) unless outside their voltage range | V_drive > V_signal_range + VGS(off) | signal range | analog switching | review | §4.4.2 p.175, Fig 4.29 | high |
| WILSON-187 | components | JFET current regulator (gate tied to source, optional source resistor): I = IDSS above pinch-off; low output impedance, temperature dependent (zero-tc crossover exists), wide device spread - only where absolute current is unimportant; "current regulator diodes" available in selected bands 0.2-5 mA (~50 p) | I ~ IDSS | IDSS spread | bias current sources | review | §4.4.2 p.175-176, Fig 4.30 | high |
| WILSON-188 | derating | JFET gate leakage: a few pA at room temperature but exponential with T: > 20x at 70 C and ~1000x at 125 C (a good bipolar input beats it at 125 C); PCB/connector leakage usually limits anyway | IG(T) ~ IG(25)*2^((T-25)/10) (diode law) | T | high-Z JFET inputs | calc | §4.4.3 p.176 | high |
| WILSON-189 | components | n-channel JFET gate-current breakpoint: IG rises rapidly above a drain-gate voltage of 1/3 to 1/2 of the drain-gate breakdown (depends on ID); input impedance can fall by orders of magnitude vs IGSS -> limits CM range. Hold VDG below the breakpoint: lower drain bias, or cascode the input FET with a second FET (p-channel devices barely show the effect) | VDG < (1/3..1/2)*V_DG_breakdown | VDG, ID | JFET high-Z amplifiers | calc | §4.4.3 p.176-178, Fig 4.31/4.32 | high |
| WILSON-190 | esd | Low-power MOSFET gate breakdown +/-15 to +/-40 V with only a few pF gate capacitance: ~100 pC destroys it - electrostatic handling damage before assembly. Options: rigorous anti-static handling (short all leads until assembled; incompatible with SM) or gate-zener-protected versions (limit negative gate swing to one diode drop, add diode leakage with its temperature law). In-circuit gates biased through high-megohm (or no) resistors remain vulnerable at board/equipment level | Q_crit ~ 100 pC; Vgs_max 15-40 V | gate bias network | low-power MOSFET use | review | §4.5.1 p.178-179, Fig 4.33 | high |
| WILSON-191 | components | Power MOSFET vs bipolar vs IGBT (Table 4.2): MOSFET to 1 kV/100 A, < 100 ns switching independent of T, VGS(th) 3-10 V, gain tempco -0.2%/C, resistive output shares current when paralleled, RDSon tempco +0.7%/C, body diode, thermally limited SOA, ESD precautions, ~1.5 p/W; bipolar to 1 kV/500 A, 0.3-5 us, hFE 20-100 (tempco +0.8%/C), current hogging in parallel, VCEsat tempco -0.25%/C, second breakdown, thermal runaway, 0.75-1 p/W; IGBT to 1200 V/500 A, 0.2-1 us with switching loss rising with T, VGE(th) 5-8 V (tempco -11 mV/C), VCEsat tempco positive at high I / negative at low I, no body diode, thermally limited SOA, ~2 p/W | see values | V, I, f | power switch selection | review | §4.5.2 p.180, Table 4.2 | high |
| WILSON-192 | components | MOSFET gate drive: switching time set by driver output impedance into CGS + Miller CGD. 74HC gate (4 mA at 5 V) into 200 pF to a 3 V threshold takes C*V/I = 150 ns. Devices characterised for RDSon at VGS = 10 V must not be driven from 5 V logic (knee operation, unpredictable high RDSon) - use logic-level (VGS = 5 V) parts. Gate charge method: t = Qg/Ig (20 nC: 20 us at 1 mA, 20 ns at 1 A); keep RG low, IG high | t_sw = Qg/Ig; t_th = C*Vth/I | Qg, Ig, Vth, C | MOSFET switching | calc | §4.5.3 p.181, Fig 4.34/4.35 | high |
| WILSON-193 | protection | Gate-source overvoltage from drain transients through CGD: with high dynamic drive impedance (e.g. pulse transformer) the gate sees V_drain * CGD/(CGD+CGS); typical CGD:CGS = 1:6, so a 300 V drain spike gives ~50 V on the gate (destructive). Specify integral gate zener or place one at the gate-source terminals, or ensure low driver source impedance | V_gate ~ V_drain * CGD/(CGD+CGS) (~1/7) | CGD, CGS, V_transient | MOSFETs with drains exposed to transients | calc | §4.5.3 p.181-182 | high |
| WILSON-194 | pdn | Source lead inductance: high di/dt through the source lead develops a voltage that subtracts from VGS and slows switching; route the gate-drive return separately from the high-current source return right up to the device terminals (no common impedance / Kelvin source) | separate gate return | layout | power MOSFET layout | inspect | §4.5.3 p.183, Fig 4.36 | high |
| WILSON-195 | protection | Drain-source turn-off spikes from stray inductance: V = L*di/dt, e.g. 20 A switched across 0.5 uH in 50 ns = 200 V; clamp diode forward recovery may miss the leading edge. Minimise all high-di/dt loop lengths and add a local drain-source zener or snubber; faster switching also raises EMI | V_spike = L_stray*I/t_sw | L_stray, I, t_sw | fast power switching | calc | §4.5.4 p.183-184, Fig 4.37 | high |
| WILSON-196 | derating | RDSon positive tempco: at max Tj (usually 150 C) RDSon is ~1.8-2x the 25 C value; with heatsink sized for max Tj at max dissipation, allowable current is ~0.7x the 25 C figure; lower VGS than the characterisation value raises RDSon further. Positive tempco enables paralleling (no current hogging); bipolars need emitter resistors per device to prevent thermal runaway | RDSon(Tj_max) = (1.8..2)*RDSon(25); I_allowed ~ 0.7*I(25) | RDSon, Tj, VGS | MOSFET conduction loss / heatsink sizing | calc | §4.5.5 p.184 | high |
| WILSON-197 | components | P-channel MOSFET of the same RDSon/V rating needs a larger die (p-type resistivity) - dearer but with higher current ratings, larger SOA and lower thermal resistance than its "complement"; threshold, gm and capacitances can be nearly matched | none | complementary pairs | complementary output stages | review | §4.5.5 p.184 | high |
| WILSON-198 | components | IGBT: on-state drop never below a diode threshold (PNP output driven by MOSFET); ~70% of a 500 V MOSFET's conduction loss is in the N-region, which IGBT conductivity modulation removes (up to 20x MOSFET / 5x bipolar current density); no inherent reverse diode (choose external); IGBT preferred > 1000 V, MOSFET < 250 V; 400-600 V: MOSFET for high frequency, IGBT for low frequency; turn-off tail current (open-base PNP charge) limits switching frequency and grows with temperature | V_on >= V_diode; class by V and f | V, f | high-voltage/high-current switches | review | §4.6 p.184-187, Fig 4.38/4.39 | high |
| WILSON-199 | components | Op-amp category parameter ranges (Table 5.1): general purpose GBW 1-30 MHz, SR 0.5-40 V/us, VOS 0.5-20 mV; low power GBW 0.05-5 MHz, SR 0.03-3 V/us, VOS 0.5-20 mV, ICC 0.015-1 mA; precision SR 0.3-10 V/us, VOS 0.06-0.5 mV, VOS drift 0.5-4 uV/C, noise 3-30 nV/rtHz; high speed/video GBW 30-1000 MHz, SR 100-5000 V/us, VOS 1-25 mV, ICC 3-15 mA, gain/phase error 0.01-0.3%. Any parameter missing from a datasheet: assume a pessimistic value (manufacturer won't test it) | see table | application | op-amp selection | review | §5.1 p.191-192, Table 5.1 | high |
| WILSON-200 | components | "Precision" op-amp = VOS < 200 uV and VOS tempco < 2 uV/C (printed "mV" = uV by context). Bipolar inputs best for low VOS unless bandwidth limited to tens of Hz, where CMOS chopper-stabilised parts (auto-null several hundred times/s) win | VOS < 200 uV, tc < 2 uV/C | spec | precision amplifiers | review | §5.2.1 p.192 | high |
| WILSON-201 | components | Output offset = VOS x closed-loop gain: non-inverting AC amp, gain 1000, TL072 (VOS max 10 mV) on +/-12 V -> 10 V DC at the output (device saturates at 9-10 V) -> asymmetric clipping; a 1 mV bench sample hides it; polarised output coupling capacitor may see reversed polarity. Fixes: AC-couple the feedback (DC gain 1; Rf*C gives seconds of power-on delay), cascade lower-gain stages (2 x 33), or lower-VOS part (OP-227G 180 uV) | V_out_offset = VOS_max * A_CL must leave headroom | VOS_max, A_CL, rails | high-gain amplifiers | calc | §5.2.1 p.192-194, Fig 5.1/5.2 | high |
| WILSON-202 | components | VOS drift: standard devices 5-40 uV/C, typ 10 uV/C; bipolar rule of thumb 3.3 uV/C per mV of initial room-temperature offset; add drift x dT to worst-case VOS; LinCMOS-type CMOS parts achieve 1-2 uV/C. Microcontroller nulling (store zero-input reading in NV memory) removes offset, leaving only drift; repetitive real-time nulling removes drift too | drift ~ 3.3 uV/C per mV VOS (bipolar) | VOS, dT | wide-temperature precision | calc | §5.2.1 p.194-195, Fig 5.3 | high |
| WILSON-203 | components | Input bias current: bipolar few uA down to few nA (industry standard < 0.5 uA; precision < 20 nA; current-nulled pA); JFET/CMOS pA-tens of pA at 25 C JUNCTION temperature, doubling per 10 C so no better than bipolar at high T (precision JFET/CMOS still nA at 125 C); JFET op-amps self-heat several to tens of degrees above ambient. Speed trades against bias current | IB(T) doubles per 10 C (FET) | IB spec, Tj | high-impedance sources | calc | §5.2.2 p.195-196 | high |
| WILSON-204 | components | Offset from currents: equal source resistances RS at both inputs (balance resistor R3 = R1//R2) cancel IB, leaving IOS*RS; unequal RS gives IB*dRS (IB may be 10x IOS). Break-even where IOS*RS = VOS: 741 (VOS 1 mV, IOS 30 nA) at RS = 33 kohm; TL081 (5 mV, 5 pA) at 1000 Mohm. R3 adds current-noise x R noise - omit in low-noise circuits if not needed | dVOS = IOS*RS (balanced) or IB*dRS (unbalanced) | IB, IOS, RS | op-amp DC accuracy | calc | §5.2.2 p.196-197, Fig 5.4 | high |
| WILSON-205 | components | CMRR: 80 dB -> 100 uV input-referred error per 1 V common-mode change; varies with CM level and temperature, always worsens with frequency, specified at DC; inverting configuration is immune. PSRR: 80 dB -> 100 uV per 1 V rail change; may be only 20-30 dB at tens-hundreds of kHz; +ve and -ve rail PSRR can differ by tens of dB - do not rely on anti-phase ripple cancelling | V_err = V_cm * 10^(-CMRR/20) | CMRR(f), PSRR(f) | non-inverting / differential stages | calc | §5.2.3 p.196-198, Fig 5.5 | high |
| WILSON-206 | components | CM input range: LM324-type (pnp pair) and CMOS inputs work down to (slightly below) the negative rail; some stop a few volts short of the positive rail; rail-to-rail types include both; 741-class bipolar and BiFET cannot come within 2 V of either rail. Absolute max input usually = supply: exceeding it without current limit destroys the device; even limited overvoltage can latch up or reverse input polarity (709 effect) - put a resistor directly in series with EACH input pin (capacitor discharge, staggered rail sequencing) | series R at each input | rails, source | all op-amp inputs | inspect | §5.2.4 p.198-199 | high |
| WILSON-207 | components | Output swing: compute at worst-case (minimum, unregulated) supply; classic bipolar/BiFET outputs stop >= 2 V from each rail (VDR(min)+VBE), may be asymmetric (beware "peak-to-peak" specs); single-supply sink outputs reach within tens of mV of ground; CMOS rail-to-rail only into open circuit - any load incl. the feedback resistor reduces swing by Rout/Rload ratio. Output current typically limited to ~+/-10 mA (spec'd into 2-10 kohm loads). External buffer: take feedback from the final output, protect against shorts, recheck stability. Some single-supply parts show crossover distortion on split supplies. Output forced outside the rails by a fault flows through internal diodes limited only by the source (§6.2.3) | V_swing <= V_rail_min - 2 V (bipolar); I_out <= 10 mA | rails, load | op-amp outputs | calc | §5.2.5 p.199-200, Fig 5.6/5.7 | high |
| WILSON-208 | components | Slew rate = i_out1/CC (741: 20 uA into 30 pF = 0.67 V/us); full-power bandwidth 2*pi*f_max = SR/Vp; above it output becomes triangular, asymmetric slew rates produce DC-offset-like errors. BiFET inputs give >= 10x slew rate for the same stability | f_max = SR/(2*pi*Vp) | SR, Vp | large-signal AC | calc | §5.2.7 p.201-203, Fig 5.9/5.10 | high |
| WILSON-209 | components | Gain-bandwidth: open-loop corner at low Hz-tens of Hz, then -20 dB/decade to unity-gain f. LM324 GBW 1 MHz -> gain 10 to 100 kHz, gain 100 to 10 kHz (small signal only); recent devices 5-30 MHz; > 30 MHz = "high speed". Settling time is specified only for some parts (unity gain, low Z, low C load) and cannot be derived from SR and GBW | f_-3dB(closed) ~ GBW/A_CL | GBW, A_CL | AC design | calc | §5.2.8-5.2.9 p.203-204, Fig 5.11 | high |
| WILSON-210 | components | Diagnosing op-amp oscillation: frequency near unity-gain BW -> feedback instability (confirm by raising closed-loop gain: oscillation stops or drops in frequency). Other causes: common-impedance ground coupling (inductive, wide frequency range); power-supply coupling - PSRR falls with f and 0.01-0.1 uF decouplers resonate with long lead inductance in the 1-10 MHz range -> add 1-10 uF tantalum bypass; output-stage instability with capacitive loads (high-MHz) - decouple at the supply pins with the ground point near the load return, or series R inside the loop; parasitic output-to-non-inverting-input coupling - keep feedback/input parts close, separate in/out, short tracks, ground plane/shield tracks | none | f_osc | any feedback amplifier | measure | §5.2.10 p.204-207, Fig 5.12 | high |
| WILSON-211 | components | Capacitive load phase lag (with open-loop Rout) erodes phase margin; 10 m of RG58C/U coax ~1000 pF (looks capacitive until ~lambda/4). Isolate with a low-value series resistor and add a small direct feedback capacitor CF. Stray capacitance at the inverting input is 3-5 pF with normal layout - significant with high-value feedback resistors (FET-input amps); choose CF to roughly equate feedback and input time constants (CF*RF ~ CS*R_in); recommended for all LF circuits to limit bandwidth | CS ~ 3-5 pF; C_coax ~ 100 pF/m (RG58) | RF, CS, CL | op-amp stability | calc | §5.2.10 p.206-207, Fig 5.13/5.14 | high |
| WILSON-212 | components | Open-loop gain: ACL = AOL/(1 + AOL*beta); AOL >= 80 dB (usually 100-120 dB) at DC but sags -20 dB/decade: beta = 0.01, AOL = 1e5 gives 99.9; a decade below the closed-loop bandwidth AOL ~ 1000 gives 90.9 (10% low). AOL commonly halves from the cold to the hot temperature extreme. For precise gain evaluate actual AOL(f, T); reduce A_CL or pick higher AOL | A_CL = AOL/(1 + AOL*beta); need AOL*beta >> 1 at f_max | AOL(f,T), beta | precision gain stages | calc | §5.2.11 p.207-208 | high |
| WILSON-213 | components | Noise summation: uncorrelated sources add as mean squares (10 uV + 20 uV -> sqrt(500) = 22.36 uV RMS); any source < 1/3 of another may be neglected (< 5% error). Standard deviation = RMS; variance = mean square. Noise spectral density in V/rtHz; total = density x sqrt(bandwidth) if flat | V_tot = sqrt(sum Vi^2) | sources | noise budgets | calc | §5.2.12 p.208-210 | high |
| WILSON-214 | components | Thermal noise en = sqrt(4*k*T*B*R), k = 1.38e-23 J/K. Rules: 1 kohm at 298 K in 1 Hz = 4 nV RMS; 100 kohm in 1 Hz or 1 kohm in 100 Hz = 40 nV; scales with sqrt(R) and sqrt(B). Peak-to-peak = 6.6 x RMS (< 0.1% exceedance) or 5 x RMS (< 1%). Example: 100 kohm at 27 C: S = 4kTR = 1.66e-15 V^2/Hz -> 40.7 nV/rtHz; vs 16-bit/3.3 V ADC step ~50 uV that is 0.16% of one LSB per rtHz. Divider R1 = R2 = 100 k (gain 0.5) + 100 ohm filter R: S_total = 2*(0.5^2*1.66e-15) + 1.66e-18 = 8.30e-16 -> 28.8 nV/rtHz (simulation 28.818 nV/rtHz) | en = sqrt(4kTBR); 4 nV/rtHz per 1 kohm | R, T, B | any input network | calc | §5.2.12 p.211-213 | high |
| WILSON-215 | components | Op-amp noise model: en in series with one input, in at each input, resistors thermal. Output contributions (per rtHz, x sqrt(B)): N(RIN) = sqrt(4kT*RIN)*AV; N(R1) = sqrt(4kT*R1)*(AV+1); N(RF) = sqrt(4kT*RF); N(in-) = in-*RF; N(in+) = in+*R1*(AV+1); N(en) = en*(AV+1); total = sqrt(sum of squares). Unspecified amplifier noise may be 2-4x worse than a low-noise equivalent. Example parts at 1 kHz: OP27 3 nV/rtHz, 0.4 pA/rtHz; TL071 18 nV, 0.01 pA; LMV324 39 nV, 0.21 pA. Low-Z case (RIN 200, R1 180, RF 2 k, gain 10): totals 41.9 / 200 / 430 nV/rtHz (en dominates). High-Z case (200 k, 180 k, 2 M): 1402 / 836 / 1127 nV/rtHz (resistor or current noise dominates). Rules: high-Z circuits are noisy; low-Z -> voltage noise dominates; high-Z -> use biFET/CMOS and delete R1; a low-en op-amp gives no benefit at high Z | see model | en, in, R network, AV | low-noise design | calc | §5.2.12 p.213-215, Fig 5.17/5.18 | high |
| WILSON-216 | components | Noise bandwidth: single-pole (6 dB/octave) filter with cut-off fc has noise bandwidth 1.57*fc; cascaded poles reduce the ratio; ignore a LF cut-off more than a decade below the HF one (except below a few tens of Hz where 1/f noise rises; 1/f corner ranges from a few hundred Hz down to < 10 Hz by design). Use simulator AC noise analysis (frequency-domain) rather than time-domain random sources | B_noise = 1.57*fc (1 pole) | fc | noise integration | sim | §5.2.12 p.215-216, Fig 5.19 | high |
| WILSON-217 | power | Op-amp supply current: sum datasheet maxima at no load; IS varies with supply voltage (graph) and increases when cold; load current can dominate - a 10 kohm load with +/-10 V swing doubles a ~1 mA quiescent budget; include capacitive-load drive current. Speed trade: 10 uA parts slew only 0.03 V/us; fast parts up to 10 mA: +/-15 V x 10 mA = 300 mW, with theta_JA 100-150 C/W gives Tj 30-45 C above ambient before any load | P = (V+ - V-)*IS; dT = P*theta_JA | IS, rails, theta_JA | power budget / thermal | calc | §5.2.13 p.217-218 | high |
| WILSON-218 | reliability | IC temperature grades: commercial 0..+70 C; industrial -40..+85 C (occasionally -25..+85); military -55..+125 C; automotive -40..+125 C; some Japanese digital -20..+75 C. Using commercial parts outside range: unspecified, parameters may drift beyond spec (often more than inside), different vendors differ; semiconductor life halves per +10 C; Tj max 100-150 C must always be observed; below 0 C included moisture in plastic packages freezes -> parameter jumps; condensation on cold boards | grade vs ambient; life x0.5 per +10 C | ambient range | part selection | review | §5.2.14 p.218-219 | high |
| WILSON-219 | cost | Prefer multi-sourced industry-standard op-amps (80/20 rule, 741 > 30 years) but beware unspecified parameters differing between manufacturers (TI LM324 slew 0.5 V/us typ at 5 V; National unspecified) - design and test to the loosest source; reuse a small set of parts across products | none | sourcing | BOM | review | §5.2.15 p.219-220 | high |
| WILSON-220 | cost | Prefer dual/quad op-amp packages when several stages are used (LM324 ~5 p per op-amp - cheapest); quiescent current only slightly above a single, better offset/drift tracking; drawbacks: common supply, layout inflexibility, thermal/rail/RF interaction between sections; > several-hundred-MHz parts are singles only (crosstalk); multi-channel pinouts less standard | none | stage count | BOM | review | §5.2.15 p.220 | high |
| WILSON-221 | components | Current-feedback op-amps: bandwidth set by RF (doubling RF halves bandwidth), then gain by the resistor ratio; nearly constant transition time regardless of amplitude; needs ZS >> RF; NEVER add capacitance across RF (destabilises); best at video/wideband; voltage feedback gives free RF choice, two high-Z inputs and better DC specs | BW ~ 1/RF; no C across RF | RF | CFB amplifiers | review | §5.2.16 p.221-222, Fig 5.20 | high |
| WILSON-222 | components | Comparator outputs: open-collector (LM339/393) needs a pull-up, allows any output rail; totem-pole fixed at 3.3/5 V levels. Response time depends on overdrive (small overdrive -> surprisingly long) and load: sink transistor gives 10-50 mA (fast falling edge) but the pull-up supplies an order of magnitude less (slow rising edge) - dV/dt = I/C | dV/dt = I_pullup/C_load | RL, CL, overdrive | comparator interfaces | calc | §5.3.1-5.3.2 p.222-224, Fig 5.22/5.23 | high |
| WILSON-223 | timing | Comparator pulse-timing error: slow rising edge vs fast falling edge shifts the following gate's crossing point (CMOS threshold anywhere between 0.3 and 0.7 x supply) - error can exceed a microsecond in low-power circuits; use active-low outputs for low-duty-cycle pulses (leading edge from the transistor, low power), lower the pull-up if the trailing edge matters | none | RL, CL, gate threshold | analog-to-pulse-width timing | calc | §5.3.2 p.224-225, Fig 5.24/5.25 | high |
| WILSON-224 | components | Op-amp as comparator only if: slew rate adequate (0.5 V/us takes ~3 us to cross the 0.8-2 V logic grey area); saturation recovery (unspecified) is acceptable; output levels suit the logic (an output swinging to within 2 V of +/-15 V cannot drive 5 V logic - use feedback zener clamp to avoid saturation and speed response). Comparator as op-amp: avoid (unstable, uncharacterised; some totem-pole outputs draw destructive current in linear mode) | SR >= logic swing / allowed transit time | SR, rails | spare-op-amp comparators | calc | §5.3.3 p.225-226 | high |
| WILSON-225 | components | Comparator edge oscillation: any transit of the linear region longer than a few hundred ns is "slow" and stray positive feedback makes it oscillate at ~several MHz (seen by logic as multiple edges, clock double-counting; also RF interference). Golden rules: keep input drive impedance low (2 pF stray with 10 kohm gives an 8 MHz pole -> keep source < 10 kohm, preferably 10x lower); minimise output-to-input stray C by layout (never route output back past the inputs; guard inputs); no ground-loop/common-mode feedback paths | R_source < 10 kohm (prefer < 1 kohm) | R_source, C_stray | all comparators with slow inputs | inspect | §5.3.4 p.226-227, Fig 5.26 | high |
| WILSON-226 | components | Hysteresis (Fig 5.27, open-collector output, pull-up R3): Vout(H) = Vcc - (Vcc - Vref)*R3/(R1+R2+R3); Vth_h = a*Vcc + (1 - a)*Vref [printed "(1 + a)"; (1 - a) is the self-consistent divider form], a = R1/(R1+R2+R3); dVth_h = a*(Vcc + Vref) [as printed]; Vth_l = b*Vsat + (1 - b)*Vref, b = R1/(R1+R2); dVth_l = b*(Vsat - Vref). With R3 << R1+R2 (a = b), Vref = Vcc/2, Vsat = 0: total hysteresis band = b*Vcc. Totem-pole outputs: omit R3 but include output levels/impedance. AC-only hysteresis (capacitor for R2) leaves DC threshold intact but fails with slow inputs | hysteresis band ~ Vcc*R1/(R1+R2) | R1, R2, R3, Vref, Vcc, Vsat | Schmitt / comparator thresholds | calc | §5.3.4 p.227-228, Fig 5.27 | medium |
| WILSON-227 | protection | Comparator differential input limit must be checked (LM339 family = supply range; NE529 only +/-5 V differential with +/-6 V CM - both inputs at +4 V OK, but the other cannot go below -1 V). Abnormal conditions (separate rails cycling) -> series input resistance R = V_over/I_in_absmax or from dissipation. Response time and bias currents degrade toward CM limits; some parts show bias-current steps vs differential voltage | R_series >= V_over/I_in_max | limits, V_over | comparator inputs | calc | §5.3.5 p.229, Fig 5.28 | high |
| WILSON-228 | components | Unused comparators in a package: never leave inputs open (self-oscillation couples into siblings); do not ground both (offset makes output/current unpredictable) - ground one input and tie the other to a fixed voltage inside the differential/CM limits so the device is saturated | none | package usage | multi-comparator packages | inspect | §5.3.5 p.230 | high |
| WILSON-229 | components | Zener reference: low-tc zener 5.5-7 V + series silicon diode, constant current, buffered; buried (sub-surface) zener with laser trim gives 50 ppm/year, 0.1% absolute, +/-10 ppm/C; heated (LM399) gives sub-ppm/C at high supply drain and seconds of warm-up; output ~6.9 V needs a high supply | 50 ppm/yr; 0.1%; 10 ppm/C | accuracy need | precision references | review | §5.4.1 p.230 | high |
| WILSON-230 | components | Band-gap reference: Vref = VBE3 + (VBE1 - VBE2)*R2/R1, zero tc near 1.2 V (actual 1.205-1.26 V by design/process); trimmed 2.5/5/10 V versions; lower minimum current and sharper knee than any zener. Two-terminal 1.2 V parts (Table 5.2): tolerances 0.2-4%, tempcos 20-100 ppm/C, minimum current 10-50 uA (printed "mA"; context = uA), 0.30-1.68 GBP. Not directly interchangeable: nominal voltages differ (1.2-1.25 V), some REQUIRE 0.1-1 uF across them and others FORBID it; TO-92/SOT23 pinouts differ | design for the loosest tolerance of all candidates | tolerance, tc, I_min | 1.2 V references | review | §5.4.2 p.230-232, Table 5.2, Fig 5.29 | high |
| WILSON-231 | components | Reference specs: line regulation (uV/V), load regulation (% per dI or dynamic ohm; should include self-heating), tolerance (work to upper/lower limits, not nominal - bounds may be asymmetric), tempco (average ppm/C, spot values, or error band in mV - normalise before comparing; curves are not straight), long-term stability (ppm/1000 h, typical only; burn-in zeners), settling tens-hundreds us, minimum supply current (band-gap typ 50-100 uA, 10 uA available) | none | datasheet | reference selection | review | §5.4.3 p.232-233, Fig 5.30 | high |
| WILSON-232 | process | SPICE op-amp models: use for initial assessment to ~+/-20% accuracy; models use typical not worst-case specs, miss supply/temperature/load sensitivities, slew/overshoot and CM-limit behaviour; add board strays (a few pF), ground topology; run Monte Carlo over tolerances; use evaluation-board layouts; breadboard critical performance | model accuracy ~ +/-20% | model | analog simulation | sim | §5.5 p.233-234 | high |
| WILSON-233 | hw-fw | Logic thresholds: use worst-case VIL/VIH guaranteed over temperature AND supply voltage; state undefined between them - no decisions during transition or settling time; prefer synchronous design. Noise immunity is an interface property: NM_H = VOH(min) - VIH(min), NM_L = VIL(max) - VOL(max); e.g. HCMOS driven by LS-TTL: 2.4 V high / 0.47 V low (worst case). Negative margin = unreliable by design: LS-TTL VOH 2.7 V < HCMOS VIH 3.15 V -> add pull-up to VCC (min R from driver capability, max from timing) or use HCT inputs | NM_H = VOH - VIH >= 0; NM_L = VIL - VOL >= 0 | family thresholds | every logic interface across families/rails | calc | §6.1.1 p.237-239, Fig 6.1-6.3 | high |
| WILSON-234 | hw-fw | Current immunity = noise-margin voltage / driver output impedance; 4000B CMOS at 5 V has high Rout (poor), ~10x better at 15 V; microcontroller ports are high-Z (poor); prefer 74HC at 5 V. Dynamic noise margin rises for pulses shorter than device speed (Fig 6.4, graph). Level translators (74LVT: VIH 2.0 / VIL 0.8 from 5 V or 3.3 V rails) for 3.3 V/5 V mixes | I_immunity = NM/R_out | R_out, NM | noisy environments | calc | §6.1.1 p.239-240, Fig 6.4 | high |
| WILSON-235 | timing | Fan-out/loading: DC fan-out from VOH/VOL vs input currents (may differ high/low; CMOS unlimited at DC); dynamic: input C 5-10 pF each + ~5 pF interconnect; 74HC dynamic drive ~+/-40 mA (std) / +/-60 mA (buffers) at 4.5 V; slew time = C*dV/I, e.g. 100 pF from 0 to 3 V at 40 mA = 7.5 ns to add (plus safety factor) to propagation delays; heavy C loads also reduce driver reliability (transient currents); use 74xx244-type buffers on loaded buses | t_slew = C_node*V_th/I_drive | C_node, I_drive | timing budgets | calc | §6.1.2 p.240-241, Fig 6.5-6.7 | high |
| WILSON-236 | pdn | Ground bounce: I = Cn*dV/dt; 74AC gate at 1.6 V/ns into 30 pF draws 50 mA; 50 mA/ns through 20 nH (1 inch of track) = 1 V pulse ~ fast-logic noise margin; synchronous octal switching (FF->00 into a loaded bus) exceeds 1 A and can corrupt the eighth bit -> low-inductance ground plane mandatory; observe with scope probe tip shorted to its ground (magnetic pickup) | V_gnd = L_track*dI/dt | Cn, dV/dt, L | fast logic boards | calc | §6.1.3 p.242-243, Fig 6.8/6.9 | high |
| WILSON-237 | decoupling | Decoupling capacitor distance: < 0.5 inch from the IC for 74AC/ECL and bus drivers; up to several inches for 4000B. Too long a path forms a high-Q LC with track inductance and rings - worse than no capacitor. Lead/package inductance matters more than value: small chips (0805, 0603, 0402). Value: C = I*t/V, e.g. 74HC octal buffer 8 x 50 mA for 6 ns = 0.4 A, droop 0.4 V -> 6 nF; use 10-100 nF (22 nF good compromise), Z5U/Y5V acceptable. Very high-speed ICs: capacitors under the package on the far side, via-connected; close power/ground planes decouple HF better than discretes | C_min = I_pk*t/dV_allowed; d < 12.7 mm (fast logic) | I_pk, t, dV | all logic ICs | calc | §6.1.4 p.243-245, Fig 6.10 | high |
| WILSON-238 | decoupling | Low-frequency decoupling: 1-2 uF tantalum around the board near groups that switch together (DRAM refresh); 10-47 uF at board power entry (kHz components). Minimum guideline: one 22 uF bulk per board; one 1 uF tantalum per 10 SSI/MSI packages; one 1 uF tantalum per 2-3 LSI packages; one 10-100 nF ceramic per supply pin of multi-supply-pin LSI; one 10-100 nF per octal or MSI package; one 10-100 nF per 4 SSI packages; calculate individually for power/speed-hungry parts. Ripple on rails can false-switch slow edges - use Schmitt inputs for slow edges | see counts | package inventory | board decoupling BOM | inspect | §6.1.4 p.245-246, Fig 6.11 | high |
| WILSON-239 | hw-fw | All unused logic inputs tied high or low, never floating (poor immunity; preset/clear pins spike-sensitive); every unused CMOS input to VCC or ground directly (floating -> threshold-region shoot-through current, buffered gates may oscillate); no series protection resistor needed unless rail spikes could exceed max input voltage | none | net list | all logic | inspect | §6.1.5 p.246, Fig 6.12 | high |
| WILSON-240 | grounding | ADC resolution per LSB at 10 V full scale (Table 6.1): 8-bit 39 mV, 10-bit 10 mV, 12-bit 2.4 mV, 14-bit 0.6 mV, 16-bit 0.15 mV. Digital ground switching noise is tens to hundreds of mV peak: if it reaches the converter input, precision above 8-10 bits is unusable. Filter analog bandwidth below the noise band where signals are slow; otherwise prevent injection at source | LSB = VFS/2^N; require V_noise_at_input << LSB | N, VFS, ground noise | mixed-signal boards | calc | §6.2.1 p.247, Table 6.1 | high |
| WILSON-241 | grounding | Mixed-signal segregation: separate analog and digital grounds joined at ONE point; physically separate sections with no digital tracks crossing analog areas or vice versa; single-board with one ADC: join at the ADC, separate PSU returns (two supply circuits), digital ground gridded/plane, analog star or own plane, never extend the digital plane under the analog section (capacitive coupling); multi-board: join at the power supply, run separate analog/digital grounds to each board, put digital-only boards closest to the PSU. Signals crossing ground regions must be low-risk (bandwidth, sensitivity) | one AGND-DGND tie | topology | any ADC/DAC design | inspect | §6.2.1 p.247-249, Fig 6.13 | high |
| WILSON-242 | hw-fw | Analog-to-logic-level conversion: always a comparator or Schmitt-trigger gate; never an ordinary gate (ill-defined threshold; needs > 5 V/us slew for a clean output). 74HC14-type Schmitt thresholds are loosely toleranced - use a comparator with a defined reference for precision. If the analog rail exceeds the logic rail (or during power sequencing) add a series resistor to limit clamp-diode current; better, run the analog front end from the logic supply | slew > 5 V/us for plain gates; else Schmitt/comparator | signal slew | analog-driven logic inputs | inspect | §6.2.2 p.249-250, Fig 6.14 | high |
| WILSON-243 | hw-fw | Switch de-bounce: contacts bounce for typically ~1 ms; RC filter with time constant >> bounce period into a Schmitt input (also attenuates RF/impulse noise); alternatives: R-S latch with changeover switch, clocked shift-register window, or software (act only after 2-3 consecutive agreeing polls; poll 2-3x faster than the response-time minimum) | tau_RC >> 1 ms | switch type | edge-sensitive inputs | inspect | §6.2.2 p.250, Fig 6.15/6.16; §6.5.1 p.278 | high |
| WILSON-244 | protection | Off-board logic I/O WILL see overvoltage (misconnection, ESD): consequences are immediate damage, progressive degradation, or latch-up. Protect with external clamp diodes to VCC/0 V plus series resistors (needed if the IC's internal diodes would still share too much current given forward-voltage ratios); the rail must absorb the dumped current without rising (review regulator / add local rail clamps); series resistors alone can suffice on inputs (limit to internal-diode capability) | I_fault = (V_over - V_rail)/R_series <= I_diode_max | V_over, R_series | all off-board logic lines | calc | §6.2.3 p.251-252, Fig 6.17 | high |
| WILSON-245 | protection | Do not take logic signals or power/ground rails outside the enclosure directly (antennas for ground noise out / interference in); isolate external lines. Opto-couplers 25 p-5 GBP per channel: standard transistor types switch in 2-5 us (~100 kbit/s max); 10 Mbit/s parts > 5 GBP; CTR 10-80% (1 mA out at 20% CTR needs 5 mA LED), add 20-50% end-of-life CTR margin; Darlington CTR 200-500% but ~100 us turn-off; residual coupling C 0.5-2 pF (x channel count) - never route output tracks alongside inputs; common-mode transient immunity ranges < 100 V/us to > 5 kV/us (screened types); alternatives: relays, pulse transformers with DC-free coding | I_LED = I_out/(CTR*(1 - margin)) | CTR, speed, channels | isolated interfaces | calc | §6.2.4 p.252-254, Fig 6.18 | high |
| WILSON-246 | connectors | EIA-232F (Table 6.2): unbalanced point-to-point; ~15 m typical / 2500 pF max load incl. receiver; 20 kb/s; driver +/-5 to +/-15 V into 3-7 kohm (+V = logic 0), 500 mA short-circuit max, rise 4% of unit interval (1 ms max), slew <= 30 V/us, > 300 ohm off-power; receiver +/-3 V max thresholds, 3-7 kohm, < 2500 pF. Practical: <= 3 m above 20 kb/s; no tri-state/multi-driver; paralleled receivers must keep 3-7 kohm; cannot legitimately run from +/-5 V rails; prefer on-chip slew-limited drivers; use 1488/1489 or charge-pump parts; add supply isolating diodes | C_load <= 2500 pF; SR <= 30 V/us | length, rate | RS-232 links | calc | §6.2.5 p.255-257, Table 6.2, Fig 6.20/6.21 | high |
| WILSON-247 | connectors | EIA-422: balanced differential, one driver + up to 10 receivers, 100 ohm line, L ~ 1e5/B metres (B in kb/s), 10 Mb/s max, 4000 ft at 100 kbaud; driver +/-10 V unloaded, >= +/-2 V into 100 ohm, 150 mA short circuit, rise 10% of unit interval (min 20 ns), +/-100 uA leakage off; receiver +/-200 mV sensitivity, >= 4 kohm, +/-7 V CM. Terminate ONCE, 100 ohm at the far-end receiver (matches twisted pair); unterminated lines ring and false-switch; 26LS31/26LS32 | L_max[m] ~ 1e5/B[kb/s]; one 100 ohm termination at far end | rate | RS-422 links | calc | §6.2.5 p.257, Table 6.2 | high |
| WILSON-248 | connectors | EIA-485: multi-driver half duplex, 120 ohm line terminated at BOTH ends, up to 1200 m (attenuation limited), 10 Mb/s, up to 32 unit loads (UL = 1 mA at +12 V CM or 0.8 mA at -7 V; excludes terminations); driver +/-6 V unloaded, >= +/-1.5 V into 54 ohm, 150 mA to ground / 250 mA to -7/+12 V, rise 30% of unit interval, > 12 kohm off; receiver +/-200 mV, 12 kohm, +12 to -7 V CM. Provide a passive "failsafe" network holding > 200 mV differential when idle, within termination and UL limits; 485 parts work in 422 systems, not necessarily vice versa | 120 ohm x 2; <= 32 UL; failsafe > 200 mV | node count | RS-485 buses | calc | §6.2.6 p.258-259, Table 6.2 | high |
| WILSON-249 | connectors | CAN (ISO 11898): up to 1 Mb/s, single twisted pair terminated 120 ohm at each end; max 40 m with up to 30 nodes and stubs <= 0.3 m at full rate (longer at lower rates); recessive both lines ~2.5 V; dominant CANH +1 V, CANL -1 V (2 V differential); CM range -2 to +7 V (+/-4.5 V about quiescent); unpowered nodes must be high-Z; CAN 2.0A 11-bit / 2.0B 29-bit identifiers; ISO 11519 125 kb/s | L <= 40 m, stub <= 0.3 m at 1 Mb/s | rate, topology | CAN buses | calc | §6.2.6 p.259 | high |
| WILSON-250 | connectors | USB: differential receiver sensitivity >= 200 mV over CM 0.8-2.5 V; driver low < 0.3 V into 1.5 kohm to 3.6 V, high > 2.8 V with 15 kohm to ground; full-speed cable Z0 = 90 ohm +/-15%, one-way delay <= 26 ns; driver impedance 28-44 ohm; USB 1.1: 12 Mb/s full / 1.5 Mb/s low speed with biased terminations for detection; USB 2.0: 480 Mb/s with 45 ohm source and load terminations; USB 3.0: 5 Gbit/s (3.2 achievable); +5 V power pair; NRZI + bit stuffing, SYNC field | Z0 = 90 ohm +/-15%; t_pd <= 26 ns | speed class | USB ports | calc | §6.2.6 p.259-260 | high |
| WILSON-251 | connectors | Ethernet (IEEE 802.3): 10BaseT 2.5 V peak differential, 100BaseT 1 V peak differential into 100 ohm twisted pair (IEC 11801 cabling, Table 1.7); rise/fall and amplitude symmetry specified for balance; isolate with transformer + common-mode choke; twisted-pair segments are point-to-point (hubs/switches); lengths set by timing. PCIe 2.0 5 GT/s, 3.0 8 GT/s | V_diff 1 V (100BaseT) / 2.5 V (10BaseT) into 100 ohm | variant | Ethernet PHY | review | §6.2.6 p.260-262, Fig 6.22 | high |
| WILSON-252 | firmware | Real-time budget: identify critical routines and compute worst-case execution vs deadline early, e.g. 44 kHz audio sample period 23 us at 30 ns/instruction = 766 instructions absolute max; keep a healthy contingency. Interrupts: assign priorities; mask others only for critical periods; latency = stack save + jump + routine; interrupt-driven code may not be provably deterministic - safety-critical software may forbid real-time interrupts; hand-written assembler only for time-critical ISRs, well documented | N_instr_max = T_deadline/t_instr | t_instr, deadlines | microcontroller design | calc | §6.3.2-6.3.3 p.265-266, 269, Fig 6.24 | high |
| WILSON-253 | hw-fw | Sampling: fs >= 2 x highest signal frequency AND band-limit the input (anti-alias filter incl. noise) - components above fs/2 alias to abs(f_sig - n*f_sample): 40 kHz or 48 kHz sampled at 44 ks/s appears at 4 kHz; a signal at fs produces a phase-dependent DC offset. Resolution q = VFS/2^n; DC input varies >= 1 step (+/- 1/2 LSB quantisation + input noise); many ADC types need a sample-and-hold (adds noise, drift, slew, offset errors) - prefer integrated ADCs | f_alias = abs(f_sig - n*fs) | fs, f_max | all ADC front ends | calc | §6.3.2 p.266-267, Fig 6.25/6.26 | high |
| WILSON-254 | hw-fw | PWM analog output: n-bit timer clocked at 2^n x output frequency; 10 MHz clock with 16-bit counter gives only 152 Hz, so ripple filtering to LSB level makes it very slow; logic levels must be accurate - drive the output buffer B1 from a separate calibrated supply; follow the filter with a high-Z unity-gain buffer B2 with low/zeroed offset; passes through one opto-coupler (account for asymmetric delays) | f_pwm = f_clk/2^n | f_clk, n | cheap DACs | calc | §6.3.2 p.267-268, Fig 6.27 | high |
| WILSON-255 | hw-fw | Wake-up settling: a switched analog supply from a 100 ohm port output into 100 nF has tau = 10 us (printed "10 ms") and reaches 99.6% (8-bit accuracy) only after 5.5 tau = 55 us - no accurate conversion before the supply/reference has settled to the required number of bits | t_settle = -ln(2^-N) * tau (5.5 tau for 8 bit) | R_out, C_decouple, N | sleep/wake designs | calc | §6.3.2 p.268-269 | high |
| WILSON-256 | hw-fw | Microprocessor rails are only characterised within e.g. 3.0-3.6 V or 4.75-5.25 V; behaviour outside is undefined - supervise power-up/down reset, power-fail detection and NV-memory write protection; accept that transients (sub-us ESD/mains/cable) WILL corrupt program flow and provide automatic recovery (watchdog) | none | rail spec | all micro designs | review | §6.4.1 p.269-270, Fig 6.28 | high |
| WILSON-257 | hw-fw | Watchdog: use the on-chip one if present; else a simple hardware timer (555 has wide RC tolerance; CMOS 4060B divider from a reliable clock, e.g. 50/60 Hz, needs no extra parts and barks repeatedly - astable preferred over one-shot); NEVER a programmable timer (transient can program it off); timeout typically 10 ms-1 s (long enough for service/restart, short enough for safety); output to RESET only (not an interrupt, even NMI); trigger the timer from POR for defined reset width; AC-couple (R-C-D) the re-trigger so a stuck port cannot hold it off; use a programmable port bit (two instructions) rather than an address-decode pulse; generate the two edges in two software modules (e.g. one in the tick ISR, one in the background loop), one edge in exactly one place; cover initialisation and EEPROM writes (tens of ms); test with repeated transient bursts (LED on output, statistically many events, bursts during recovery); provide a disable link for software test | 10 ms <= t_wd <= 1 s | firmware structure | all micro designs | review | §6.4.2 p.271-274, Fig 6.29-6.31 | high |
| WILSON-258 | hw-fw | Supervisor: RC power-on reset misses dips of a few ms, needs minimum VCC rise rate, gives no warning - consumer only; undervoltage comparator on the regulator INPUT holds reset until regulator output is stable and resets on any dip; add a second comparator at a higher Vin for power-fail NMI so housekeeping completes before reset; brownouts produce trains of power-fail pulses without reset - software must recover from repeated power-fail interrupts of unpredictable width at line frequency (or monostable-buffer the power-fail); LM339-type comparators work down to 2 V; prefer dedicated supervisor ICs | V_pf_threshold > V_reset_threshold > V_in_min(regulator) | Vin thresholds | micro supervision | review | §6.4.3 p.274-275, Fig 6.32/6.33 | high |
| WILSON-259 | hw-fw | Non-volatile memory (EEPROM, battery RAM, RTC): gate write-enable or chip-enable in hardware with the "low line" signal (software cannot protect); the gate package must be powered from the backup rail and its inputs from the main circuit must be pulled DOWN (not up) so they don't sit in the CMOS threshold region draining the battery (months instead of years) - pull-ups create sneak paths through bus-driver protection diodes; RAM VCC sits one diode below main VCC (Schottky reduces the drop but leaks more at high temperature): CMOS RAMs may latch up when inputs exceed VCC by 0.3 V - limit current via driver impedance or use an active MOS switch-over; quote backup time only at room temperature; if no RTC is needed, use EEPROM and drop the battery | V_in(RAM) <= VCC(RAM) + 0.3 V | backup topology | battery-backed designs | inspect | §6.4.3 p.275-276, Fig 6.34/6.35 | high |
| WILSON-260 | firmware | Defensive firmware: reject/flag inputs outside known range or rate-of-change limits (but don't mask genuine sensor failures); average streams; accept digital inputs only after 2-3 consecutive agreeing polls; prefer level-sensitive over edge-sensitive interrupts (treat edge inputs like clock pins: layout, low drive impedance); protect RAM tables with checksums recomputed on every modification and verified in background; error detection on all long-distance data links; fill unused ROM with one-byte NOPs ending in JMP RESET (consider filling the entire map); periodically re-initialise all critical control registers (ports, UARTs) in the idle loop | none | firmware | all micro firmware | review | §6.5 p.277-280, Fig 6.36 | high |
| WILSON-261 | requirements | Hardware platform selection: FPGA for clock speeds up to ~100 MHz, dedicated/parallel hardware, or mixed complex controller + hardware; overkill at 3-4 MHz; DSP for multiply/add-heavy algorithms in C; PIC-class microcontroller for compact, cheap, non-stringent speed; PLD/CPLD for small simple blocks; leave FPGA headroom (~60% utilisation) for protocol updates; benchmark candidates with synthesis tools before committing | f_clk > tens of MHz -> FPGA | requirements | platform choice | review | §6.6 p.280-281 | high |
| WILSON-262 | hw-fw | ADC specification checklist: bits (typ 8-20), sampling rate (50 Hz-100 MHz), relative accuracy, integral non-linearity, differential linearity (step variation; converters should be linear to better than 1/2 bit or the LSB is meaningless), monotonicity / no missing codes, SNR (dynamic range). Definitions: levels 2^N; resolution q = VFS/(2^N - 1); MSB weight 2^-1 VFS, LSB 2^-N VFS; max quantisation error +/- q/2 | linearity < 1/2 LSB | spec | ADC selection | review | §6.9 p.281-286 | high |
| WILSON-263 | hw-fw | 8-bit example, 0-10 V: q = 10/255 = 39.21 mV; 6.0 V -> 10011001 (5.976563 V); 6.2 V -> 6.210938 V, error +10.938 mV = 0.176% of input = 0.109% of FS; max quantisation error one LSB (39.063 mV) | worked example | VFS, N, Vin | ADC error budgets | calc | §6.9.1 p.286-287 | high |
| WILSON-264 | hw-fw | Quantisation noise: e_rms = q/sqrt(12) (uniform, white over Nyquist band for N > 5); full-scale sine peak 2^N*q/2, RMS 2^N*q/(2*sqrt(2)); SQNR = (3/2)*2^(2N) = (6.02*N + 1.76) dB (~6 dB per bit; 16-bit = 98 dB). Oversampling: OSR = fs/(2*fm); in-band noise power = e_rms^2/OSR (PSD 2*e_rms^2/fs) | SQNR_dB = 6.02N + 1.76; noise = e^2/OSR | N, fs, fm | ADC/sigma-delta budgets | calc | §6.9.1 p.287-288 | high |
| WILSON-265 | hw-fw | Oversampled SQNR = 6.02*N + 1.76 + 10*log10(OSR) dB (= (3/2)*2^(2N)*OSR); doubling OSR adds ~3 dB (half a bit) for a plain (unshaped) quantiser | SQNR_dB = 6.02N + 1.76 + 10log(OSR) | N, OSR | oversampled ADC budgets | calc | §6.9.1 p.288 | high |
| WILSON-266 | hw-fw | ADC architecture choice: flash needs 2^N - 1 comparators and 2^N resistors, converts in one clock, accuracy set by resistor matching/comparators, practical to ~8 bits (video, scopes); counting/tracking ADC speed depends on the change since the last sample (slow for fast signals); successive approximation always N cycles, uniform conversion time, good efficiency/accuracy compromise; dual-slope up to ~14 bits, independent of exact R and C, slow (integrator time constant), variable execution time (instrumentation); sigma-delta: 1-bit stream, very high resolution/low distortion, audio, easy OSR/order configuration | flash comparators = 2^N - 1 | speed, bits | ADC selection | review | §6.3.1 p.263-264; §6.10 p.288-291, Fig 6.44-6.47 | high |
| WILSON-267 | hw-fw | Second-order sigma-delta in-band RMS noise n0 = e_rms * (pi^2/sqrt(5)) * OSR^(-5/2) (printed); SNR improves with both modulator order and OSR (Fig 6.49, graph); higher orders shape noise better but risk instability and are hard to analyse (sensor interfaces) | n0 = e_rms*pi^2/sqrt(5)*OSR^-2.5 | e_rms, OSR, order | sigma-delta converters | calc | §6.10.5 p.290-291, Fig 6.48/6.49 | medium |
| WILSON-268 | power | Direct-off-line SMPS: transformer runs at 30-300 kHz (vs 50 Hz) -> far smaller/lighter; input filtering must be more stringent; primary rectifier/reservoir work at full line voltage; small secondary reservoir; duty-cycle regulation needs an ISOLATED feedback path that preserves mains separation | f_sw = 30-300 kHz typ | topology | power supply architecture | review | §7.1.1-7.1.2 p.295-296, Fig 7.1 | high |
| WILSON-269 | requirements | Power supply specification checklist: input (min/max V, max input current surge & continuous, frequency range, allowable waveform distortion/interference generation); efficiency over all load/line; outputs (min/max V, min/max load I, ripple & noise, load & line regulation, transient response); abnormal conditions (overload, spikes, surges, dips, interruptions, turn-on/off, soft start, power-down interrupts); mechanical (size, weight, thermal, environment, connectors, screening); safety approvals; cost/availability | all items specified | PSU spec | PSU requirements | review | §7.1.3 p.296 | high |
| WILSON-270 | cost | Buy, don't build, when an off-the-shelf PSU fits: saves design/test and brings existing safety & EMC compliance; budget ~GBP 1 per watt in the 50-200 W range (Fig 7.2 graph); little cost difference linear vs switch-mode; in-house wins only at high volume or custom needs; bend the circuit to standard rails 3.3 V/5 V and +/-12 V/15 V | cost ~ 1 GBP/W (50-200 W) | power, volume | PSU sourcing | review | §7.1.4 p.296-297, Fig 7.2 | high |
| WILSON-271 | power | Mains input range: nominal 230 V (UK/Europe) or 115 V (US); variability +/-10% or +10/-15% -> design for 207-253 V or 195-253 V transparently; UK supply held to +/-6% at the point of connection plus local loading; US can dip below 100 V; prefer universal-input switch-mode over a voltage-selector switch (230 V into a 115 V setting blows fuses or damages the unit) | 195-253 V (230 V +10/-15%) | market | mains-powered design | calc | §7.2.1 p.297-298, Fig 7.3 | high |
| WILSON-272 | protection | If the input fuse must clear output overloads, characterise input current over the whole input-voltage range: need at least 2:1 between prospective fault current and maximum operating current; otherwise the input fuse protects only the input circuit and separate secondary protection (current limit) is required | I_fault/I_op_max >= 2 | I_op_max, I_fault | PSU fusing strategy | calc | §7.2.2 p.298 | high |
| WILSON-273 | protection | Fuse rated current: IEC 60127 = max continuous without opening or overheating, typically 60% of minimum fusing current; UL 198G rated current is 85-90% of minimum fusing current (runs hotter at rating) - do not interchange ratings between standards without re-derating | I_N(IEC) ~ 0.6*I_min_fuse; I_N(UL) ~ 0.85-0.9*I_min_fuse | fuse standard | fuse selection | calc | §7.2.3 p.299 | high |
| WILSON-274 | protection | Fuse time-current classes (Fig 7.4 graph, current normalised to rating): FF very fast, F fast, M medium time lag, T time lag (anti-surge), TT long time lag; specify F or T wherever possible (easy replacement); FF mainly for semiconductor protection; include arcing time in total operating time when interrupting > ~10x rated current | prefer F or T | load type | fuse class | review | §7.2.3 p.299-300, Fig 7.4 | high |
| WILSON-275 | protection | Surge/pulse survival: a current pulse that must not open the fuse should have I^2*t below 50-80% of the fuse's published I^2*t | I2t_pulse <= (0.5..0.8)*I2t_fuse | pulse waveform | inrush / pulse loads | calc | §7.2.3 p.300 | high |
| WILSON-276 | protection | Fuse rated voltage must exceed the maximum system voltage; breaking capacity must exceed the maximum prospective fault current (in mains products usually set by the next fuse upstream); HBC cartridges are sand-filled with breaking capacities of thousands of amps, LBC unquenched with a few tens of amps or less | V_fuse > V_sys_max; I_break > I_prospective | V_sys, I_prospective | mains fuses | calc | §7.2.3 p.300 | high |
| WILSON-277 | power | Switch-on surge: a (toroidal) mains transformer switched at the voltage peak can draw > 10x its operating current (limited only by source, primary resistance, leakage inductance); magnitude depends on the random switching phase - test many switch-ons or the problem passes unnoticed; uncharged reservoir capacitor adds a secondary surge; off-line SMPS charge the reservoir directly through the bridge and may need soft-start | I_surge > 10*I_op (toroid) | transformer type | mains input design | measure | §7.2.4 p.300-301, Fig 7.5 | high |
| WILSON-278 | protection | Anti-surge (T/TT) fuses carry 10-20x rated current for a few ms but rupture at ~2x rating if sustained for tens to hundreds of seconds - may still be hard to size for high surge:operating ratios; resettable thermal circuit breakers are inherently insensitive to switch-on surges | T fuse: 10-20x for ms; ~2x for 10-100 s | I_surge, I_op | inrush protection | calc | §7.2.4 p.301 | high |
| WILSON-279 | protection | NTC inrush limiter in series with primary and fuse: heats and drops resistance over 1-2 s; drawbacks: performance varies with ambient range, runs hot in normal operation (ventilate, keep away from heat-sensitive parts), cool-down of several tens of seconds gives poor protection against short supply interruptions | reset time ~ tens of s | ambient, interruption profile | inrush limiting | review | §7.2.4 p.301 | high |
| WILSON-280 | protection | PTC thermistor in place of a fuse: low R until fault current self-heats it; surge-insensitive; does NOT provide electric-shock protection (cannot replace a safety fuse) - use for local winding protection. Alternatives: triac switching at zero crossing; power MOSFET controlled turn-on resistance for DC inputs (with reverse-polarity protection, standby switching) | PTC not a safety fuse | fault type | winding / DC-input protection | review | §7.2.4 p.301-302 | high |
| WILSON-281 | compliance | Mains harmonics: EN 61000-3-2:2000 limits each input-current harmonic up to the 40th (2 kHz at 50 Hz) for apparatus up to 16 A per phase; non-lighting products < 75 W rated power exempt; rectifier/reservoir inputs draw peaky current (RMS/average 1.11 for a sinusoid is far exceeded), PF 0.5-0.75; crest factor Ipk/Irms rises as reservoir impedance falls; coincident peaks of many supplies flatten the network waveform | harmonics <= EN 61000-3-2 limits (P >= 75 W or lighting) | P_rated, I_in | mains-powered products | measure | §7.2.5 p.302-303, Fig 7.6 | high |
| WILSON-282 | power | Power factor correction: boost pre-regulator after the bridge; CIN too small to affect the 50 Hz current but a reservoir at the 50-100 kHz switching frequency; controller forces average inductor current in phase with rectified input; output DC slightly above the highest supply peak; controllers L4981A/B, L6561, UC3853-5, MC33626/33368; side benefits: universal input range and uniform response to dips/interruptions; costs: extra converter and filtering | V_bus > V_peak_max(mains) | P_rated | PFC front ends | review | §7.2.5 p.303-304, Fig 7.7 | high |
| WILSON-283 | power | Mains frequency: Europe 50 Hz +/-1% (long-term much tighter, usable for clocks), US 60 Hz; a design verified at 50 Hz works at 60 Hz (ripple amplitude 83% of the 50 Hz value, higher trough voltage); using mains for timing needs a 50/60 Hz selection | ripple(60 Hz) = 0.83 * ripple(50 Hz) | f_mains | mains timing / ripple | calc | §7.2.6 p.304, Fig 7.8 | high |
| WILSON-284 | power | Efficiency eta = Pout/Pin = Pout/(Pout + Ploss); falls at light load (don't heavily over-rate the PSU); linear efficiency worst at high input voltage and rarely > 50% unless the input range is narrow; switch-mode easily > 70%, up to 90% with care; critical for battery equipment | eta = Pout/(Pout + Ploss) | Pout, losses | PSU selection | calc | §7.2.7 p.304-305 | high |
| WILSON-285 | power | Loss budget: transformer core loss (level, material) + copper I^2*R; rectifier VF x I (dominant at low output voltages); linear pass element (Vin - Vout) x I (worst at high line); switching element saturation loss + switching/snubber losses proportional to f_sw; sum them to forecast efficiency and investigate if measurement disagrees widely | P_loss = sum of components | component data | PSU design review | calc | §7.2.7 p.305 | high |
| WILSON-286 | power | Linear supply input derivation (worst case = min output V, max load, min line): Vin_dc(min) = Vout(min) + Vtol_reg + Vseries_reg(dropout) + Vseries_CS; transformer Vtx(rms) = (Vin_dc + Vripple + VD)/0.92 * (Vac_nom/Vac_min) * 1/sqrt(2) (0.92 = full-wave single-C rectifier efficiency, Schade). Example: 5 V +/-5% at 1 A with 7805 (+/-4% = 0.2 V, dropout 2.5 V max at 1 A and Tj 25 C): Vin_dc = 4.75 + 0.2 + 2.5 = 7.45 V; ripple 2 V, two 1 V diode drops, 240 V nominal / 195 V minimum: Vtx = 10.83 V rms. Account for crest-current IR drop in the transformer (specify transformer for the circuit) | see formulas | Vout, tolerances, dropout, ripple, VD, line range | linear PSU design | calc | §7.2.8 p.305-306, Fig 7.9/7.10 | high |
| WILSON-287 | thermal | Linear regulator dissipation at high line: in the 7805 example at 264 V mains the average Vin_dc rises to 12.5 V, so 7.45 V is dropped at full load = 1.5x the load power; regulator dropout alone is >= 50% of output power at 5 V; use low-dropout PNP-pass regulators (LM2930 range) where input headroom is small (automotive) | P_reg = (Vin_dc_avg(max) - Vout) * I_load | Vin range, I | linear regulator thermal design | calc | §7.2.8 p.307 | high |
| WILSON-288 | derating | Off-load/high-line voltage stress: transformer regulation = (Vsec_unloaded - Vsec_loaded)/Vsec_loaded, can exceed 20% for small/poor transformers; in the 7805 example off-load peak Vtx at max line is 20.2 V and with 0.6 V diode drops the reservoir sees ~19 V - a 16 V electrolytic is inadequate; higher-voltage designs may exceed the regulator's maximum input (add a pre-regulator). Size reservoir/regulator voltage ratings at no load + max line | V_cap_rating > V_res(no load, max line) | transformer regulation, line max | reservoir & regulator voltage ratings | calc | §7.2.9 p.307 | high |
| WILSON-289 | thermal | Series-pass dissipation peaks below full load when the drop across the DC source's equivalent series resistance at full load exceeds half of (no-load input voltage - output voltage) (Fig 7.11 graph). Derived: P(I) = I*(V_nl - I*Rs - Vout), maximum at I = (V_nl - Vout)/(2*Rs) | I_Pmax = (V_nl - Vout)/(2*Rs) if < I_full | V_nl, Rs, Vout | regulator heatsink sizing | calc | §7.2.9 p.308, Fig 7.11 | medium |
| WILSON-290 | power | Minimum load: regulator (especially switch-mode) stability may not hold to zero load - some rails need a bleed resistor minimum load (wasted power) unless the circuit always draws current | I_load >= I_min(spec) | load profile | SMPS rails | review | §7.2.9 p.308 | high |
| WILSON-291 | components | Reservoir capacitor: C = IL * t / Vripple, t ~ AC period minus ~2 ms (printed: 8 ms for 50 Hz, 6 ms for 60 Hz full-wave); Schade's curves for accuracy, but reservoir tolerance is typically +/-20% so accuracy is rarely needed | C = IL*t/Vripple | IL, Vripple, f | rectifier/reservoir design | calc | §7.2.10 p.308 | high |
| WILSON-292 | derating | Reservoir ripple current: RMS ripple current is 2-3x the DC load current and above ~1 A dominates capacitor selection; derate further for high ambient/high reliability. Example 2 A, 3 V ripple at 100 Hz -> 5300 uF; 6800 uF parts are rated 2-4 A at 85 C but 4-6 A is needed -> use ~22 000 uF, parallel capacitors, or a lower operating temperature (electrolytics are the prime cause of PSU failure) | I_ripple_rms ~ (2..3)*I_DC <= I_R(T) | I_DC, T | reservoir capacitors | calc | §7.2.10 p.308-309 | high |
| WILSON-293 | derating | Rectifier current: rate at least the full DC load current, preferably 2x (RMS is 2-3x DC); off-line SMPS need up to 5x average DC. Switch-on surge: peak = Vmax/Rs, tau = C*Rs; safe if tau < a half-cycle and Vmax/Rs < rated IFSM (e.g. 1N5400: 3 A average, IFSM 200 A); otherwise add series resistance, a larger diode, or inrush limiting | I_F(rated) >= 2*I_DC; Vmax/Rs < IFSM; C*Rs < T/2 | Vmax, Rs, C | bridge rectifiers | calc | §7.2.10 p.309 | high |
| WILSON-294 | derating | Rectifier PIV: >= peak AC for a full-wave bridge, >= 2x peak for full-wave centre-tap, then +50-100% for line transients; on 240 V mains specify >= 600 V, preferably 800 V PIV even with an input transient suppressor | PIV >= 1.5..2 x V_pk (bridge); >= 800 V preferred at 240 V | V_pk, topology | rectifier voltage rating | calc | §7.2.10 p.309, Fig 7.9 | high |
| WILSON-295 | power | Regulation: load and line regulation are regulator properties provided input never leaves its operating range; monolithic regulators also show thermal regulation (output shift from on-chip dissipation change over time; rarely specified - may rule them out for precision). Remote sensing: route sense pair to the load (carries only signal current), add coupling resistors from output to sense terminals so an open sense lead is safe, allow extra input headroom for the load-lead drop; only one remote regulation point possible | V_in >= V_out + dropout + V_leads | lead R, I | distributed loads | inspect | §7.2.11 p.309-310, Fig 7.12 | high |
| WILSON-296 | power | Ripple/noise: linear ripple = reservoir ripple reduced by regulator rejection (typ 70-80 dB) -> < 1 mV rms easy; switch-mode ripple+noise typ 1% of rail (printed "100-200 mV"), specify/measure over >= 10 MHz bandwidth; noise often common-mode on both rails; reduce differential spikes with a series ferrite bead plus a small ceramic across the output capacitor; for wideband sensitive analog (video, pulse, DC amps) prefer a linear supply when the choice exists | linear: < 1 mV rms; SMPS ~1% of rail over >= 10 MHz BW | topology | PSU noise spec | measure | §7.2.12 p.310-311 | high |
| WILSON-297 | grounding | Reservoir layout: peak charging current ~5x DC (1 A DC -> ~5 A peaks), so 10 mohm of shared ground gives 50 mV hum between "equivalent" grounds; larger reservoirs make it worse. Take ALL load grounds (and V+) from the supply side of the reservoir capacitor so the only common impedance is the capacitor ESR. Diagnose on a scope: pulse-shaped ripple = wiring; sawtooth = insufficient smoothing | V_hum = I_R_pk * R_g | I_pk, R_g | rectifier/reservoir layout | inspect | §7.2.12 p.311-312, Fig 7.13/7.14 | high |
| WILSON-298 | power | Transient response set by regulator loop bandwidth vs stability; don't rely on a big output capacitor (load-dependent, inefficient). 78XX regulators: ~0.1 uF at the output for transient response/HF decoupling plus 0.33-1 uF at the input for stability. Switch-mode recovery is milliseconds vs tens of microseconds for linear - matters with instantaneously switched loads (relay coils, LED banks) next to sensitive loads; line-transient response is of the same order | C_in 0.33-1 uF, C_out 0.1 uF (78XX) | load steps | regulator application | measure | §7.2.13 p.312-313, Fig 7.15 | high |
| WILSON-299 | protection | Every PSU must survive a continuous short on each output without damage (pass/switch element otherwise far outside SOA). Constant-current limit: ISC set by sense transistor VBE (temperature dependent) - allow margin or use a better circuit; switch-mode needs cycle-by-cycle current limiting (output-line sensing is insufficient) | survives continuous short | ISC(T) | all PSU outputs | measure | §7.3.1 p.313-314, Fig 7.16 | high |
| WILSON-300 | protection | Foldback limiting uses the pass element's SOA better, but the maximum foldback ratio is [IK/ISC]max = 1 + VOUT/VBE(on) (RSC infinite) and higher ratios need more input voltage -> ratios > 2-3 are impractical for low-voltage regulators | IK/ISC <= 1 + Vout/VBE(on) | Vout, VBE | foldback design | calc | §7.3.1 p.314, Fig 7.17 | high |
| WILSON-301 | power | Hold-up: mains dips/outages up to 500 ms are fairly common (UK average consumer loses 90 min/year); hold-up time depends almost entirely on reservoir C; linear regulator = constant-current sink: t_h = (Vres_trough - Vin_min)*C/I; SMPS draws more current as input falls (integrate); stored energy 0.5*C*V^2 favours high-voltage (off-line) reservoirs. Example (7805 design): C = 1 A x 10 ms/2 V = 5000 uF; at 240 V trough 14.05 - 2 - 2 = 10.05 V -> t_h = (10.05 - 7.45)*5000e-6/1 = 13 ms; at 204 V trough 7.94 V -> 2.5 ms; at the minimum design input hold-up is zero -> specify hold-up at a stated (minimum) input voltage and worst-case phase (ripple trough) | t_h = (V_trough - V_min)*C/I | C, I, V_trough, V_min | hold-up specification | calc | §7.3.2 p.314-316, Fig 7.18 | high |
| WILSON-302 | protection | Transient suppressor placement in a linear PSU: Z1 across the mains input protects everything from differential surges but sees the lowest source impedance (needs high energy rating; lets through ~2x peak operating voltage); Z2 on the transformer secondary protects the rectifiers, is shielded by transformer impedance (smaller part, better clamp ratio) but misses spikes converted to common mode by inter-winding capacitance; Z3 after the reservoir protects the regulator (clamp just below regulator abs max input), catches CM spikes but not the rectifiers. Fast low-energy transients need layout, low ground inductance and filtering | Z3 clamp < V_in_absmax(reg) | surge levels | PSU surge protection | review | §7.3.2-7.3.3 p.316-317, Fig 7.19 | high |
| WILSON-303 | protection | Overvoltage protection for expensive loads: a 6.2 or 6.8 V zener across a 5 V rail may fail (possibly open) under a sustained low-impedance fault (failed pass element); use a crowbar thyristor (across output or reservoir) triggered by a supervisor, rated for high single-pulse I^2*t and di/dt (dump continuous short-circuit current plus reservoir energy), fast gate edge well above minimum gate current, deliberate trigger delay to avoid nuisance trips on short transients; PSU must be current-limited and/or fused against the sustained short | V_trip > V_nom + tol; delay > transient width | Vnom, load abs max | protected rails | review | §7.3.4 p.317-318, Fig 7.20 | high |
| WILSON-304 | hw-fw | PSU turn-on/off: rails ramp, may overshoot (poorly compensated SMPS) and be noisy; provide a power-good flag to the micro's RESET; on loss of input give a power-fail interrupt first, then an undervoltage warning, separated by ~the hold-up time which must exceed the micro's housekeeping time. Supervisor inputs: DC output (OVP), reservoir (undervoltage), low-voltage AC (power fail); outputs to crowbar and load; must work down to very low supply voltage; ICs MC3423, ICL7665/7673, TL7705, MAX690 (few second sources) or discrete LM339 | t_holdup > t_housekeeping | hold-up, firmware timing | supervised supplies | review | §7.3.5 p.318-319, Fig 7.21/7.22 | high |
| WILSON-305 | mechanical | PSU construction classes: open frame (cheapest, no screening/protection, fully enclosed by host; 10-100 W, up to 250 W); enclosed (> 100 W, screening for SMPS, fan cooling, screw terminals); encapsulated (up to 40 W, PCB or chassis mount, can include EMI screen; higher power needs external heatsink - seek reliability data); rack cassettes (25-500 W, mostly SMPS; connector must carry load current and be mains rated - DIN 41612 H15 with leading earth pin) | P ranges per class | P, environment | PSU mechanical selection | review | §7.4.1 p.319-320 | high |
| WILSON-306 | thermal | PSU is usually the most concentrated heat source: as soon as efficiency is known compute heat output, place heatsinked components accordingly and give the unit a conductive path to the environment - not a fan added as an afterthought | P_heat = Pout*(1/eta - 1) | Pout, eta | PSU thermal layout | calc | §7.4.2 p.320-321 | high |
| WILSON-307 | compliance | PSU safety: segregate user-accessible low-voltage circuits from mains parts by minimum distances (including primary-secondary transformer spacing) or by insulation of at least a minimum thickness; EN 60950-1 (IEC 60950-1) is the default quoted standard; UL (US), CSA (Canada), CENELEC/Low Voltage Directive (EU); for worldwide markets apply the most stringent set; "certified to" skips part of your own approval, "designed to meet" does not; no safety standard quoted -> beware | creepage/clearance per standard | market | mains PSUs | review | §7.4.3 p.321 | high |
| WILSON-308 | components | Batteries: choose the cell type early; design the circuit to work over the widest part of the discharge curve (cheaper chemistries give useful energy down to 60-70% of nominal voltage); check load-current capability over the working temperature (chemistry dependent); recharge temperature range is often narrower than discharge; use standard types when users replace batteries | V_min(circuit) <= 0.6-0.7*V_nom | chemistry, T | battery-powered design | calc | §7.5.1 p.322 | high |
| WILSON-309 | components | Battery ratings: open-circuit voltage can exceed on-load voltage by up to 15%, operating voltage may sit well below nominal; capacity (Ah, "C") falls at high discharge rate - a 15 Ah lead-acid at 15 A (1C) lasts ~20 min (Fig 7.23 graph); constant-power discharge uses sloping-characteristic cells (alkaline) most efficiently but needs a regulating converter | V_oc <= 1.15*V_load; runtime(1C) << 1 h | discharge profile | battery sizing | calc | §7.5.1 p.322-323, Fig 7.23 | high |
| WILSON-310 | reliability | Series cells: raise voltage but lower reliability and risk reversing the weakest cell at end of life (leak/rupture) - replace all cells together, minimise series count, boost from fewer cells with a switching converter; parallel cells need a series diode per path for reliability; avoid recharging parallel cells (unknown charge sharing) - use purpose-assembled packs; protect against reverse battery insertion (keyed compartment, fuse, series diode or dedicated circuit) | minimise N_series | pack topology | battery packs | review | §7.5.1 p.322-323 | high |
| WILSON-311 | mechanical | Battery mechanics: contacts of nickel-plated steel, austenitic stainless steel or inconel - never copper or its alloys (corrosion); springy to take up tolerances; multiple contacts for high current; PCB-mount batteries are hand-soldered after other assembly; vent gas safely (charging/overload out-gassing, flammable) and keep away from sparking or hot parts; keep cool (life/efficiency); anchor against shock/vibration; keep organic solvents/adhesives away from cases | contact material spec | environment | battery holders | inspect | §7.5.1 p.323 | high |
| WILSON-312 | process | Battery storage & disposal: store within a restricted temperature/humidity range (self-discharge rises with temperature), avoid temperature cycling, rotate stock, top-up-charge rechargeables in stock; mercury cells banned (Batteries and Accumulators Directive 91/157/EEC); EU targets: collect/recycle 75% consumer and 95% industrial batteries, >= 55% of recovered material recycled; recycling targets 25% by 2012, 45% by 2016 | stock rotation | storage conditions | battery logistics | review | §7.5.1 p.325 | high |
| WILSON-313 | components | Primary cells: alkaline MnO2 nominal 1.5 V, operating 1.3-0.8 V/cell, end voltage 0.8 V/cell up to 6 in series (0.9 V for more), -30 to +80 C, high-current capable, avoid high RH (external corrosion), ~85% energy retained after 3 years at 20 C; silver oxide ~1.5-1.55 V, stable then gradual decay, pulse capable, good cold performance, 2-year shelf life; zinc-air highest volumetric density, OCV 1.45 V, output 1.3-1.1 V, use within 2 months of unsealing, narrow T/RH range, no sustained high current; lithium MnO2 2.5-3.5 V, pulses up to 30 A, cylindrical to 1.5 Ah, very low self-discharge, wide temperature, possible transport restrictions (Li-SOCl2, Li-SO2 for specialised use) | see values | load, environment | primary battery choice | review | §7.5.2 p.325-326 | high |
| WILSON-314 | components | Sealed lead-acid (VRLA): nominal 2 V, OCV 2.15 V, end 1.75 V per cell; 6/12 V blocks 1-100 Ah; C quoted at the 20-hour rate (5-hour for NiCd/NiMH); -30 to +50 C with ~60% capacity at the cold extreme; self-discharge ~3%/month at 20 C rising with T; irreversibly damaged if left discharged (sulfation) - recharge stock regularly and fit batteries at despatch/installation; float life 4-5 years (extended types to 15 years); cycle life at 100% depth of discharge only ~15% of that at 30% DoD - oversize for cyclic duty | V_end = 1.75 V/cell; DoD <= 30% for long cycle life | duty, T | standby batteries | calc | §7.5.3 p.326-328, Fig 7.24 | high |
| WILSON-315 | components | NiCd: 0.15-7 Ah, nominal 1.2 V, OCV 1.35-1.4 V, end 1.0 V/cell, -40 to +50 C, low internal resistance (high discharge rate), not damaged by full discharge, high self-discharge (months), memory effect (recharge from full discharge), heavy-metal disposal issue. NiMH: same voltages and flat profile, -20 to +50 C, ~20% heavier with ~40% more capacity, less memory effect, less tolerant of trickle charging | V_end = 1.0 V/cell | application | NiCd/NiMH selection | review | §7.5.3 p.328, Fig 7.25 | high |
| WILSON-316 | components | Li-ion: much higher gravimetric energy density (Fig 7.26), cell voltage 3.6-3.7 V (3x nickel), flat discharge to a 3 V endpoint, no memory effect; must be protected against over-charge, over-discharge and over-current at all times -> use purpose-designed packs with integral charge control and protection | V_end = 3.0 V/cell; protection mandatory | application | Li-ion packs | review | §7.5.3 p.328-330, Fig 7.26/7.27 | high |
| WILSON-317 | power | Lead-acid charging: current-limited constant voltage; initial current limited to 0.1-0.25 C; 2.25-2.5 V per cell (lower for float/trickle, higher for cyclic recovery - never leave the cyclic level applied continuously); temperature compensate -4 mV/C per cell for wide ambient; two-step charger drops to float when current falls to ~0.05 C; avoid resistor "taper" charging from rectified AC (overcharge, ripple) or add a timer; constant current 0.05-0.2 C with voltage monitoring works for series strings | V_float = 2.25-2.5 V/cell, -4 mV/C; I_max = 0.1-0.25 C | T, duty | lead-acid chargers | calc | §7.5.4 p.330-331, Fig 7.28 | high |
| WILSON-318 | power | NiCd/NiMH charging: constant current only (terminal voltage drops on overcharge); continuous 0.1 C permissible for NiCd (full recharge takes ~16 h, not 10); up to 0.3 C for long periods (cell warms at end); rapid charge only with monitoring/termination before overheating (temperature sensor, charger ICs TEA1100, MC33340, LT1510, MAX713); simple series resistor from a source well above the up-to-1.55 V/cell terminal voltage is adequate for slow charge; repeatedly recharging a full battery shortens life; NiMH trickle <= C/250 (not 0.1 C or 0.05 C continuous) | I = 0.1 C (16 h); <= 0.3 C long-term; NiMH trickle <= C/250 | C, chemistry | nickel chargers | calc | §7.5.4 p.331 | high |
| WILSON-319 | power | Li-ion charging: tightly controlled constant-current/constant-voltage regime integrated with over-charge, over-discharge and over-current protection inside the pack | CC/CV + protection | pack | Li-ion chargers | review | §7.5.4 p.331 | high |
| WILSON-320 | protection | Solid-state protection circuit (SSPC): power MOSFET switch + current sense + microcontroller computing an equivalent fuse blow time; rating and I^2*t characteristic are programmable and field-modifiable | programmable I2t | load profile | electronic fusing | review | §7.6 p.331-332, Fig 7.29 | high |
| WILSON-321 | emc | Far-field field strength from a transmitter: E = sqrt(30*P)/d (V/m), P = radiated power (feed power x antenna gain, W), d = distance (m); valid in the far field d > lambda/(2*pi); near-field strengths can be much higher and depend on antenna type/drive | E = sqrt(30*P)/d | P, gain, d, f | RF immunity assessment | calc | §8.1.1 p.335 | high |
| WILSON-322 | emc | RF threat levels: AM broadcast 100-500 kW (1-10 V/m occasionally, inefficient coupling at MF); TV/FM ~10 kW near buildings -> > 10 V/m possible on upper floors in line of sight (cables/tracks near resonance); 1 W UHF hand-held gives 5-7 V/m at 0.5 m; 1-10 GHz radars: pulsed 50 V/m up to 3 km (airports); civil aircraft worst case 17 kV/m (2-4 GHz ground radars, EUROCAE WG33). Design criterion: minimum 3 V/m from 10 MHz to 1 GHz, 10 V/m preferred; pulsed > 1 GHz immunity hard to quantify | E_immunity >= 3 V/m (10 V/m pref.), 10 MHz-1 GHz | environment | RF immunity requirement | review | §8.1.1 p.335-336 | high |
| WILSON-323 | emc | Mains transient statistics (ZVEI survey, 28 000 live-to-earth transients > 100 V, 40 locations, ~3400 h): average rate per hour industrial 17.5, business 2.8, domestic 0.6, laboratory 2.3 (Table 8.2); number of transients ~ inversely proportional to the cube of peak voltage (Fig 8.1); rate of rise ~ proportional to sqrt(peak): typ 3 V/ns at 200 V, 10 V/ns at 2 kV; mechanical switching produces bursts with rise times of a few ns and several hundred volts peak | N(>V) ~ V^-3; dV/dt ~ sqrt(Vpk) | environment class | transient immunity requirement | calc | §8.1.1 p.336-337, Table 8.2, Fig 8.1 | high |
| WILSON-324 | emc | Microprocessor equipment transient immunity: test to withstand pulses of at least 2 kV peak; thresholds < 1 kV give unacceptably frequent corruption in nearly all environments, 1-2 kV occasional corruption; 4-6 kV for high-reliability equipment | V_test >= 2 kV (4-6 kV hi-rel) | reliability class | micro-based products | measure | §8.1.1 p.337 | high |
| WILSON-325 | emc | Automotive 12 V transients (Fig 8.2 waveforms, graph): load dump (alternator load suddenly disconnected during heavy charging), switching of inductive loads (motors, solenoids), alternator field decay (negative spike when ignition is switched off) - the transient environment is severe relative to the nominal supply range | design for load dump + negative field-decay spike | vehicle supply | automotive electronics | review | §8.1.1 p.337-338, Fig 8.2 | medium |
| WILSON-326 | esd | ESD model: human body ~150 pF in series with 150 ohm; charging voltage depends on relative humidity and synthetic materials (Fig 8.3, IEC 61000-4-2); discharge currents of tens of amps with sub-nanosecond rise couple into internal circuitry even when the discharge goes to ground via the case | HBM 150 pF / 150 ohm | RH, materials | ESD immunity design | calc | §8.1.1 p.338, Fig 8.3 | high |
| WILSON-327 | requirements | Before immunity testing define exactly what constitutes acceptable performance and what is a failure (accuracy degradation, audio deterioration, program corruption possibly masked by recovery or mistaken for a software glitch); standards' performance criteria distinguish temporary, operator-recoverable and permanent failure | pass/fail criteria defined per test | function list | EMC test plan | review | §8.1.1 p.338-339; §8.2.2 p.344 | high |
| WILSON-328 | emc | Emissions: conducted limits apply below 30 MHz (mains leads), radiated above 30 MHz (empirical coupling breakpoint); digital clocks and harmonics are the main source (energy concentrated), data/address lines add wideband noise that varies with operating mode/software; regulations protect victim receivers only - two compliant products can still interfere in the same rack (intra-system EMC is the designer's problem) | f < 30 MHz conducted; f > 30 MHz radiated | spectrum | emission design/test | review | §8.1.2 p.339-340 | high |
| WILSON-329 | compliance | Market EMC regimes: US FCC Rules Part 15 subpart J - "digital device" uses timing signals > 9 kHz; class A (business/commercial/industrial) and class B (residential, stricter); personal computers need FCC certification, others verification; Australia/NZ "C-tick" declaration; Japan VCCI (quasi-voluntary, ITE); China, Taiwan, South Korea generally mandate in-country tests | class B for residential | market | compliance planning | review | §8.2 p.340 | high |
| WILSON-330 | compliance | EU EMC Directive essential requirements: (a) emissions must not prevent radio/telecom and other apparatus operating as intended; (b) adequate intrinsic immunity. Routes: self-declaration against harmonized EN standards (DoC referencing them; testing not mandatory but normally needed) or technical construction file with independent competent body statement where no standard exists. Only EN standards listed in the OJEU give presumption of conformity - IEC documents cannot be self-certified against; product standards take precedence over generic | DoC to OJEU-listed EN | product sector | EU market | review | §8.2.1 p.340-342 | high |
| WILSON-331 | compliance | Emission & immunity standard map (Table 8.3): ISM EN 55011/CISPR 11/FCC Part 18; household EN 55014-1/CISPR 14-1 (immunity EN 55014-2/CISPR 14-2); lighting EN 55015/CISPR 15 (immunity EN 61547/IEC 61547); radio & TV receivers EN 55013/CISPR 13 (immunity EN 55020/CISPR 20 incl. antenna terminals); ITE EN 55022/CISPR 22/FCC Part 15 (immunity EN 55024/CISPR 24). Immunity standards cover RFI, ESD and transients. Consult current specifications to confirm limit values (Figs 8.4/8.5, graphs) | see Table 8.3 | product sector | standard selection | review | §8.2.2 p.342-344, Table 8.3, Fig 8.4/8.5 | high |
| WILSON-332 | compliance | CISPR 16-1 quasi-peak receiver (Table 8.4): 9-150 kHz: 200 Hz bandwidth, 45 ms charge, 500 ms discharge, 24 dB overload factor; 0.15-30 MHz: 9 kHz, 1 ms, 160 ms, 30 dB; 30-1000 MHz: 120 kHz, 1 ms, 550 ms, 43.5 dB; continuous (narrowband) interference reads ~peak; pulse interference is progressively desensitised as PRF falls | see Table 8.4 | band | pre-compliance measurement setup | measure | §8.2.2 p.343-344, Table 8.4 | high |
| WILSON-333 | compliance | Emission test set-up: conducted (< 30 MHz) at the mains terminals through a LISN / artificial mains network (CISPR 16: 50 ohm in parallel with 50 uH to earth); radiated (> 30 MHz) on an open area test site or absorber-lined screened room at 3, 10 or 30 m; scaling limits by 1/d from 10 m to 3 m is not strictly accurate (near-field) but widely applied | E_3m ~ E_10m * 10/3 (approx.) | distance | EMC test planning | measure | §8.2.2 p.343-345, Fig 8.7 | high |
| WILSON-334 | grounding | Common-impedance conducted coupling (usually the ground return, e.g. motor/switching impulses into a micro's 0 V); earthing and bonding conductors become high impedance at frequencies where their length is an odd multiple of a quarter wavelength (resonance) | avoid L_bond ~ (2k+1)*lambda/4 at threat frequencies | bond length, f | bonding design | calc | §8.3.1 p.345 | high |
| WILSON-335 | emc | Mains supply RF impedance is well characterised: 50 ohm in parallel with 50 uH to earth; power cables act as low-loss transmission lines up to ~10 MHz so interference propagates around the distribution network; interference is differential (symmetric) or common mode (asymmetric) and each needs its own filter treatment | Z_mains = 50 ohm // 50 uH | f | mains filter design | calc | §8.3.1 p.345-346, Fig 8.7/8.8 | high |
| WILSON-336 | emc | Magnetic (inductive) coupling: V = 2*pi*f*Is*M (M = mutual inductance, H) - a current / low-impedance phenomenon, proportional to loop areas, spacing, orientation and screening; short cable lengths in the same loom have M of 0.1-3 uH | V = 2*pi*f*Is*M; M = 0.1-3 uH (loom) | Is, f, M | near-field coupling | calc | §8.3.2 p.346 | high |
| WILSON-337 | emc | Capacitive (electric) coupling: V = 2*pi*f*Vs*C*Z (C = mutual capacitance, Z = victim impedance to ground) - a voltage / high-impedance phenomenon; typical mutual capacitance 1-100 pF | V = 2*pi*f*Vs*C*Z; C = 1-100 pF | Vs, f, C, Z | near-field coupling | calc | §8.3.2 p.347 | high |
| WILSON-338 | emc | Radiation from electrically small conductors (far field, distance d m, current I A, frequency f Hz): loop E = 131.6e-16*(f^2*A*I)/d V/m (A in m^2); monopole over ground plane E = 4*pi*1e-7*(f*L*I)/d V/m (L in m). Far field E/H = 377 ohm (120*pi), E ~ 1/d. Near field: loop gives high H falling as 1/d^3 with E as 1/d^2; short rod gives high E falling as 1/d^3 with H as 1/d^2. Conductors approaching lambda/4 (1 m at 75 MHz) are no longer electrically small and couple much more efficiently | E_loop = 1.316e-14*f^2*A*I/d; E_mono = 1.2566e-6*f*L*I/d | f, A or L, I, d | emission estimates (loops, cables) | calc | §8.3.2 p.347 | high |
| WILSON-339 | emc | Design EMC in at circuit level first (shielding and filtering cost money, circuit design doesn't); the majority of post-design interference problems trace to poor grounding; short, direct tracks run close to their ground returns are inefficient antennas and help both emissions and immunity | none | layout | all designs | review | §8.4 p.347-348 | high |
| WILSON-340 | emc | Rise-time control: harmonic envelope of a trapezoidal clock rolls off faster with slower edges (Fig 8.9, graph) - a 5 MHz clock with 8 ns instead of 1 ns rise time is nearly 20 dB lower around 200 MHz. Use the slowest logic family that does the job; fast logic only where needed with clocks kept local; add a series resistor of a few tens of ohms at clock driver outputs (RC with line/input capacitance) | ~20 dB @200 MHz (8 ns vs 1 ns, 5 MHz clock) | t_r, f_clk | digital emissions | calc | §8.4.1 p.348, Fig 8.9 | high |
| WILSON-341 | emc | Immunity/emission logic practice: prefer the family with the highest noise margin (faster drivers have lower output impedance - trade-off); use the lowest clock frequency (multi-phase low-frequency clocks), possibly shift the clock so harmonics avoid a susceptible frequency; stop rail/ground switching noise spreading with a solid unbroken ground plane plus local power-plane segments and thorough decoupling - apply even on low-speed circuits for immunity | none | logic family, f_clk | digital boards | review | §8.4.1 p.348-349 | high |
| WILSON-342 | emc | Analog circuits: check gain stages at prototype stage with a high-frequency scope or spectrum analyser for RF oscillation even if function looks fine; terminate all long lines, especially those ending at CMOS inputs (no inherent termination) - ringing generates frequencies set by line length | none | prototypes | analog/pulse circuits | measure | §8.4.2 p.349 | high |
| WILSON-343 | emc | Interface immunity strategies: minimise signal bandwidth with passive RC or ferrite filtering (every analog amplifier should have intentional bandwidth limitation); run the interface at the highest power/voltage level consistent with dynamic range; use balanced signalling (interference becomes common mode, rejected by CMR); galvanically isolate (opto/transformer) in severe cases; keep good dynamic range and overload margin so interference stays linear and can be filtered later | BW_signal minimised | interface spec | I/O design | review | §8.4.2 p.349-350 | high |
| WILSON-344 | firmware | EMC firmware measures: watchdog on every microprocessor; type- and range-check all input data; sample several times and average (analog) or require 2-3 identical successive states (digital); parity and checksums on all data transmission; error detecting/correcting codes on volatile memory blocks (as overheads allow); level- rather than edge-triggered interrupts; periodically re-initialise programmable interface chips (PIAs, ACIAs) | none | firmware | embedded products | review | §8.4.3 p.350 | high |
| WILSON-345 | emc | Shielding materials: all-metal enclosure needed for low-frequency protection; a thin conductive coating on plastic is adequate if only > 30 MHz shielding is needed. Shielding effectiveness grades: < 20 dB minimal, 20-80 dB average, 80-120 dB above average, > 120 dB not achievable cost-effectively | SE classes | f range | enclosure design | review | §8.5 p.350 | high |
| WILSON-346 | emc | Solid-barrier shielding SE(dB) = R + A + B. Reflection: E field R = 322 - 10*log10((mu_r/sigma_r)*r^2*f^3); H field R = 15 - 10*log10((mu_r/sigma_r)/(r^2*f)); plane wave R = 168 - 10*log10((mu_r/sigma_r)*f) (r = source distance, f in Hz; near field r < lambda/(2*pi)); absorption A = 0.1314*t_mm*sqrt(mu_r*sigma_r*f); re-reflection B negligible when A > 10 dB. Skin depth delta = 6.61*(mu_r*sigma_r*F)^-0.5 cm (8.7 dB per skin depth; Cu 0.012 mm at 30 MHz). Material examples: 0.05 mm Al foil (sigma_r 0.61, mu_r 1), 0.5 mm steel (sigma_r 0.1, mu_r 60 at 10 kHz falling to 1 above 1 MHz) (Fig 8.11) | see formulas | t, mu_r, sigma_r, f, r | shield material SE | calc | §8.5 p.351-352, Fig 8.10/8.11 | high |
| WILSON-347 | emc | Apertures dominate real shielding (material SE > 200 dB is irrelevant): no shielding for lambda <= 2*d (d = longest aperture dimension, cut-off frequency); below cut-off SE rises at 20 dB/decade (Fig 8.12) i.e. SE ~ 20*log10(lambda/(2*d)) [derived]; for 20 dB minimum up to 1 GHz the maximum hole is 1.6 cm. Arrays of holes spaced < lambda/2 degrade SE by ~sqrt(N) vs one hole (100 x 4 mm holes = 20 dB worse than one 4 mm hole); apertures > lambda/2 apart don't compound. Cover windows with conductive mesh bonded to the screen; keep sensitive or noisy circuits away from apertures; use EM modelling for accurate figures | SE_ap ~ 20log(lambda/2d) - 20log(sqrt(N)); d_max = 1.6 cm for 20 dB @1 GHz | d, N, f_max | ventilation, windows, slots | calc | §8.5.1 p.352-353, Fig 8.12 | medium |
| WILSON-348 | emc | Seams act as apertures of their non-conductive length (distortion, paint, anodising, corrosion): keep mating surfaces conductive (no paint/anodise; alochrome for aluminium); maximise overlap (lapped/flanged joints; overlap adds HF capacitance); space screws/rivets no farther apart than lambda/20 at the highest frequency of interest; use conductive gaskets (knitted wire mesh, silver-loaded or oriented-wire elastomer, fabric-over-foam, form-in-place) for hinged panels/environmental seals; beryllium-copper finger stock for frequently mated surfaces | fastener pitch <= lambda_min/20 | f_max, joint design | enclosure seams | calc | §8.5.2 p.354-355, Fig 8.13 | high |
| WILSON-349 | emc | Filter insertion loss (voltage across load with vs without filter) depends on source and load impedances as well as components (Fig 8.14): a series inductor/ferrite bead gives > 40 dB in low-impedance circuits but is useless at high impedance; a shunt capacitor works at high impedance, useless at low; in multi-element filters the capacitor must face the high impedance and the inductor the low impedance; compute with a circuit simulator or build and measure | C faces high Z; L faces low Z | Zs, ZL | EMI filter topology | sim | §8.6.1 p.355-356, Fig 8.14 | high |
| WILSON-350 | emc | Filter impedances: mains impedance is predictable (LISN model); signal-circuit HF impedances can be derived; power-supply input HF impedance must be measured or estimated; assume 50 ohm for a cable acting as an antenna (standard filter test impedance) but expect in-circuit insertion loss to differ from 50 ohm catalogue data - characterise filter + circuit together | Z_source(cable) = 50 ohm assumed | circuit | filter evaluation | measure | §8.6.1 p.356-357 | high |
| WILSON-351 | emc | Discrete-component filters lose performance above ~10 MHz (component self-resonance; larger parts break earlier): above capacitor SRF its impedance rises and insertion loss falls. Layout faults that destroy HF performance: high-inductance filter ground (common impedance couples straight through) and input/output wiring run together (mutual C and L). Mount the filter ground directly to the lowest-inductance ground (chassis), keep I/O leads separate/screened, ideally straddle the equipment shield | f_useful(discrete) <~ 10 MHz | layout | filter installation | inspect | §8.6.1 p.357, Fig 8.15 | high |
| WILSON-352 | emc | Mains filter topology (Fig 8.16): common-mode choke 1-10 mH (two identical windings on one high-permeability, usually toroidal core, differential mains current cancels so no saturation; only leakage inductance attenuates differential mode); CX (line-line) 0.1-0.47 uF for differential mode (omit if source/load impedance too low); CY (line/neutral-earth) for common mode, value capped by allowable earth leakage current 0.25-5 mA per safety class and application; BS 613 maximum for class I plug-connected appliances 0.005 uF per Y capacitor; X and Y parts must be mains-rated (fire/shock hazard on failure); block filter ~GBP 5 | L_cm 1-10 mH; CX 0.1-0.47 uF; CY <= 5 nF (class I, plug) | leakage limit | mains filters | calc | §8.6.2 p.358-359, Fig 8.16/8.17 | high |
| WILSON-353 | derating | Mains filter current rating: choke saturation destroys attenuation; rectifier-capacitor inputs have crest factors giving peaks >= 3x RMS, so a filter adequately rated on RMS can be overloaded on peaks - rate for peak current; catalogue insertion loss is between 50 ohm terminations | I_pk(input) <= filter saturation current | I_rms, crest factor | mains filter selection | calc | §8.6.2 p.359 | high |
| WILSON-354 | emc | I/O filters are application-specific: RF-bandwidth signals (10 Mbit/s data, video) cannot take shunt capacitors - use common-mode chokes (invisible to the signal); slow signals (transducers, switches) can use a simple capacitor; low-pass filtering may alter waveshape even with cut-off above the signal bandwidth; transient clamping by low-pass + zener/varistor; for fast-rising transients lead inductance defeats discrete clamps - use a combined capacitor/varistor component | C_shunt only if f_signal << f_filter | signal bandwidth | I/O line filtering | review | §8.6.3 p.359-360 | high |
| WILSON-355 | emc | Three-terminal capacitors turn lead inductance into a T-filter and extend a small ceramic's effective range from below 50 MHz to above 200 MHz (add ferrite beads on the through leads); the centre ground terminal must go by the shortest path to a good ground plane (SM versions available) | f_eff: < 50 MHz (2-term) -> > 200 MHz (3-term) | ground path | VHF filtering | inspect | §8.6.4 p.360, Fig 8.18 | high |
| WILSON-356 | emc | Feedthrough capacitors (body screwed/soldered into the bulkhead, 360-degree ground, ~no ground inductance) work into the GHz region; pi-section versions include an internal ferrite; solder-in 100-1000 pF cost tens of pence, screw-mount GBP 1-2, low-MHz performance costs more - parallel a small feedthrough with a larger cheap conventional capacitor for the lower frequencies | f_eff to GHz | penetration type | shield penetrations (UHF+, military) | review | §8.6.4 p.361, Fig 8.19 | high |
| WILSON-357 | emc | Capacitive filtering on isolated circuits: RF capacitance to ground and its imbalance between signal and return lines degrade AC isolation and can INCREASE low-frequency common-mode susceptibility - restrict filter capacitance to a few tens of pF there. Multi-line filters with a common earth (filtered-D connectors): any earth series impedance couples lines together (designed-in crosstalk) - ground filtered connectors well to the case and make the case the signal ground | C_filter(isolated) <= a few tens of pF | isolation spec | isolated interfaces, filtered connectors | calc | §8.6.4 p.361-362, Fig 8.20/8.21 | high |
| WILSON-358 | cables | Cable shield termination: cables act as antennas (length and uncontrolled orientation); bond the shield 360 degrees to the equipment screen (conductive gland, or connector backshell); a pigtail/drain-wire termination is almost as bad as none at HF - negligible difference below ~3 MHz but approaching 40 dB worse than 360-degree above, with > 20 dB swings over small frequency changes (pigtail resonance); EIA-232 pin-1 shield practice is inadequate | 360-degree bond; no pigtails above ~3 MHz | frequency | shielded cable entries | inspect | §8.7 p.362-363, Fig 8.22 | high |
| WILSON-359 | connectors | Screened multi-way connector chain: screened conductive backshell with the cable shield clamped to it -> backshell contacting the connector shell -> 360-degree shell contact with the mating connector -> mating connector bolted firmly and conductively to the case; any break in the chain compromises HF shielding. Insulation-displacement two-part connectors cannot give shielded connections - use only on well-filtered interfaces or internal inter-board links | complete conductive chain | connector type | external connectors | inspect | §8.7 p.363-364 | high |
| WILSON-360 | grounding | Earth straps short and wide: aim for length/width ratio below 3:1; bonding methods must not deteriorate in adverse environments; mask paint from intended conductive areas | L/W < 3 | strap geometry | bonding | calc | §8.8 p.364 | high |
| WILSON-361 | emc | Use conductive gaskets wherever gaps or seams longer than lambda/20 are unavoidable; determine type and extent of shielding from the frequency range of interest; add internal shields around particularly sensitive or noisy areas; avoid large or resonant apertures or mitigate them; run internal cables away from apertures | seam/gap <= lambda/20 or gasket | f_max | shielded enclosures | inspect | §8.8 p.365 | high |
| WILSON-362 | compliance | EU Low Voltage Directive 73/23/EEC applies to electrical equipment rated 50-1000 V AC or 75-1500 V DC (few exceptions); conformity presumed via harmonized standards, e.g. EN 60065:1994 (mains-operated household electronic apparatus, ~IEC 60065) or EN 60950-1:2002 (ITE, ~IEC 60950-1); proof by mark/certificate from a recognised laboratory or manufacturer's declaration (no compulsory approval); product-liability duty: safe in proper use, adequate safety information, risks researched and minimised | 50-1000 V AC / 75-1500 V DC -> LVD | rated voltage | EU market | review | §9.1 p.368-369 | high |
| WILSON-363 | compliance | Hazard inventory (Table 9.1) to review for every product: electric shock (accessible live parts), heat/flammable gases (hot parts, heatsinks, overloaded parts and wiring), toxic fumes, moving parts/mechanical instability (motors, weak/heavy/sharp parts), implosion/explosion (CRTs, tubes, overloaded capacitors and batteries), ionizing radiation (HV CRTs, sources), non-ionizing RF (power RF, transmitters, antennas), laser, acoustic (loudspeakers, ultrasonic transducers) | all hazards addressed | product features | safety risk assessment | review | §9.1 p.369, Table 9.1 | high |
| WILSON-364 | compliance | Electric shock: AC body current < 0.5 mA harmless, > 50-500 mA (duration dependent) can be fatal (IEC 60479) - limiting current protects regardless of voltage; SELV = < 50 V AC rms isolated from the mains (or independent supply) and allows relaxed contact requirements; a "live part" is any conductor that may be energised in normal use (not just mains live); other measures: earthing with automatic disconnection, inaccessibility of live parts | I_touch < 0.5 mA AC; SELV < 50 V rms | circuit voltages | shock protection | calc | §9.1 p.369-370 | high |
| WILSON-365 | compliance | Safety classes (IEC 60536): Class 0 - basic insulation only, no earth provision (unacceptable in the UK); Class I - basic insulation plus bonding of all accessible conductive parts to protective earth, relies on the earth path for the equipment's life; Class II - no protective earth, double or reinforced insulation (double-square symbol); Class III - supplied from SELV and generates no voltage above SELV, no second-line defence needed | class elected per product | supply, construction | safety architecture | review | §9.1.1 p.370 | high |
| WILSON-366 | compliance | Insulation: at least two levels of protection between user and hazard - basic insulation + protective earth (Class I); double insulation = basic + supplementary layer (fail-safe); reinforced insulation = single layer of equivalent strength. Required strength per the applicable standard | 2 independent protection levels | construction | insulation design | review | §9.1.2 p.370-371 | high |
| WILSON-367 | compliance | Inaccessibility: the standard test finger must not reach live parts through any opening; small suspended bodies (e.g. a necklace) dropped through ventilation holes must not become live (internal baffles); hand-removable covers must not expose live parts (else tool-only removal or internal covers); segregate high-voltage/mains sections under separate covers; signal circuits count as SELV only if the mains isolating transformer insulation is adequate | test-finger and suspended-body tests pass | enclosure openings | enclosure design | inspect | §9.1.3 p.371, Fig 9.1 | high |
| WILSON-368 | compliance | Safety insulation must also be mechanically adequate (drop, impact, scratch, vibration tests) and work under humid conditions - no hygroscopic materials (wood, paper) | non-hygroscopic, mechanically tested | materials | insulation materials | inspect | §9.1.3 p.371 | high |
| WILSON-369 | compliance | Creepage (shortest path along an insulating surface) and clearance (shortest path through air) per the standard, e.g. EN 60065: 0.5 mm below 34 V rising to 3 mm at 354 V, extrapolated beyond; between PCB conductors slightly relaxed: 0.5 mm up to 124 V rising to 3 mm at 1240 V (intermediate values from the standard; interpolation law not printed) | d >= 0.5 mm (< 34 V) ... 3 mm (354 V); PCB 0.5 mm (<= 124 V) ... 3 mm (1240 V) | working voltage | mains-connected parts, PCB spacing | inspect | §9.1.3 p.371-372, Fig 9.2 | high |
| WILSON-370 | compliance | Safety marking: discernible, legible, indelible identification of apparatus and its mains supply, protective earth and live terminals; mains cables/terminations labelled earth, neutral, live; Class I apparatus labelled "WARNING: THIS APPARATUS MUST BE EARTHED"; fuse holders marked with ratings; mains switch "off" position clearly shown; safety instructions preferably marked permanently on the equipment | all markings present | product | labels/artwork | inspect | §9.1.3 p.372 | high |
| WILSON-371 | connectors | Connectors carrying live conductors: exposed pins must be on the dead side when separated; the protective earth contact mates first and breaks last (e.g. CEE-22 6 A inlet) | earth first-make/last-break; live side shrouded | connector choice | power connectors | inspect | §9.1.3 p.372 | high |
| WILSON-372 | protection | Fire hazard under fault conditions: no overheating or flammable-gas release when any component, terminal pair or insulation that could conceivably short (judged by creepage/clearance) is shorted, motors stall, or forced cooling fails; protect with current limiting, fuses, thermal cut-outs or circuit breakers wherever over-current could be hazardous; use flame-retardant materials (e.g. PCB laminates) where overheating can occur | single-fault analysis passes | fault list | safety design | review | §9.1.4 p.372 | high |
| WILSON-373 | protection | Fuses: select carefully when prospective fault current is not much above operating current; must be easily replaceable but are abused (nails, foil) - label fuseholders with rating and give replacement instructions; thermal cut-outs/circuit breakers cost more but reset, and must be in close thermal contact with the protected part (motor, transformer) | fuse rating marked | protection devices | fusing | inspect | §9.1.4 p.372 | high |
| WILSON-374 | process | DFM sourcing checklist: purchasing involved throughout; multiple vendors/industry-standard parts; alternate sources verified compatible with the design; reuse parts from other products; close tolerances only where essential; sole-sourced parts with vendor price/lead-time assurances; no "not recommended for new designs" parts; new vendors vetted for quality | all items answered yes | BOM | design release | review | §9.2.1 p.373 | high |
| WILSON-375 | process | DFM production checklist: production involved; design works at all mechanical and electrical tolerances; parts fit together easily; polarised parts oriented the same way; identical pitches/footprints for discretes; minimal wiring looms, mass-termination (IDC) connectors; modular/identical units; soldering/assembly process matches factory capability (placement machines cope with all SM parts); special procedures (potting, conformal coat, MOSFET/LED/battery/relay handling) minimised and understood by production and stores; adequate solder mask, track/hole sizes, clearances, legend understood by assemblers; clear assembly drawings | all items answered yes | design package | design release | review | §9.2.1 p.373-374 | high |
| WILSON-376 | test | Test & calibration checklist: test staff involved; adjustment and test points clearly marked and accessible; DIL switches or link connectors rather than solder-in wire links; circuit allows test-signal selection, test subdivision and stimulus/response (incl. boundary scan); bed-of-nails access and tooling holes for ATE, with the ATE program and fixture validated; validated test software suite for microprocessor products | all items answered yes | test plan | design release | review | §9.2.1 p.374 | high |
| WILSON-377 | process | Installation checklist: product is safe; EMC adequate; installation/user instructions clear and correct; installation requirements match real site conditions (environmental range, power supply, housing) | all items answered yes | site conditions | release | review | §9.2.1 p.374 | high |
| WILSON-378 | esd | ESD: triboelectric charging (Fig 9.3 series) can exceed 10 kV (Fig 8.3); components can be damaged well below 1 kV; relative humidity > 65% makes damage unlikely, < 20% is much more hazardous; MOS/CMOS gate-oxide breakdown is the commonest failure; damage may be total, intermittent or latent degradation, from one high discharge or cumulative lower ones; ESD also causes transient malfunction in operating systems | RH > 65% low risk; < 20% high risk | RH, device sensitivity | handling and assembly | review | §9.2.2 p.374-375 | high |
| WILSON-379 | esd | Static-safe practice (BS CECC 00015 Part 1:1991; BS 5783:1987 layout Fig 9.4): sensitive parts kept in marked conductive containers until use; conductive floor and bench mats bonded to ground via 1 Mohm; remove non-conductive items (polystyrene cups, synthetic garments, film); operator wrist strap via 1 Mohm series resistor (shock protection); grounded soldering tips; ionised air or high RH; defined static-safe work areas including the design lab; operator training; mark ESD-hazard areas on circuits; design to minimise exposed high-impedance/unprotected nodes | R_ground = 1 Mohm (mats, straps) | work area | production and lab | inspect | §9.2.2 p.375-376, Fig 9.4 | high |
| WILSON-380 | test | Decide the test strategy (in-circuit, manual functional, ATE functional, boundary scan, or a mix) at the very start and design in test access as the design progresses, not bolted on at the end | strategy defined at concept | volume, complexity | test planning | review | §9.3 p.377 | high |
| WILSON-381 | test | In-circuit test (bed-of-nails, fixture and program generated from layout and schematic data): verifies each component's presence, type/value, orientation and soldering by driving nodes with guarding/back-driving; effective for discrete-heavy, high-volume boards; weak for ICs; does not prove a working board - a functional test is still needed | every node probed | layout, netlist | high-volume boards | measure | §9.3.1 p.377-378, Fig 9.5 | high |
| WILSON-382 | test | Functional test: manual procedures with bench instruments suit low volume (cheap equipment, costly test time; technicians' tacit fixes must be fed back to design); ATE (bed-of-nails or connector jig, IEEE-488 instruments) de-skills and cuts per-unit time to minutes but needs up-front programming, fixture build and rigorous program validation - justified at high volume | choose by volume | volume | test method | review | §9.3.2 p.378 | high |
| WILSON-383 | test | Boundary scan (JTAG, IEEE 1149.1-1990, amended 1149.1a-1993, 1149.1b-1994, current 1149.1-2001): a boundary-scan cell at every digital I/O pin forming a shift register between TDI and TDO; Test Access Port pins TCK, TDI, TDO, TMS; 1-bit bypass register; drive a known value from one device's output cell and read the connected input cell to find broken traces, dry joints, bridges and ESD-damaged buffers; chain devices (partition for speed); supports BIST, reuse of IC pattern sets, and flash programming via PC controller or stand-alone programmer | TAP (TCK, TDI, TDO, TMS) on all compliant devices | device list | dense/double-sided SM boards | measure | §9.3.3 p.379-381, Fig 9.6 | high |
| WILSON-384 | test | Boundary-scan/structured-test decision (TI JTAG primer, ASIC gate counts): < 10 K gates - structured test not justified, good unstructured practice suffices; 10-20 K gates - consider it, especially with sequential logic, feedback and memory (combinatorial-only may not need it); > 20 K gates - structured approaches (boundary scan) needed for high fault grades; weigh IC logic overhead, board TAP overhead and test-department investment | gates > 20 K -> boundary scan | gate count | test architecture | review | §9.3.3 p.381 | high |
| WILSON-385 | test | Bed-of-nails layout: large clear margin around the board; no unfilled holes (vacuum hold-down) or space for clamps; test target pads on the underside on a 0.1 inch (2.5 mm) grid (down to 0.05 inch / 1 mm if tight); never use component lead pads as targets; accurately aligned tooling holes. The fixture's long coupled wires alter circuit strays - unsuitable for functional test of HF or high-speed digital circuits | pad grid 2.54 mm (>= 1.27 mm) | layout | ICT/ATE boards | inspect | §9.3.4 p.381-382 | high |
| WILSON-386 | test | Without bed-of-nails, bring test points to cheap local pin-strip test connectors (or spare pins of existing connectors); avoid routing long test tracks across the board (crosstalk, noise susceptibility, stability) | local test connectors | test point list | test access | inspect | §9.3.4 p.382 | high |
| WILSON-387 | test | Design-for-test circuit techniques: series resistor where back-driving an output or measuring a current (check it doesn't affect normal operation); tie unused gate inputs through a pull-up resistor so the node can inhibit/enable logic under test; route clocks through a 2-input data multiplexer (e.g. 74HC157) with clock-select and test-clock inputs left unconnected in normal use; resident self-test firmware entered at start-up via a test link/probe input that exercises all inputs, outputs and control signals predictably | DFT features present | schematic | testability | review | §9.3.4 p.382-383, Fig 9.7/9.8 | high |
| WILSON-388 | reliability | Reliability = probability a system operates without failure for a specified period under specified environmental conditions; must agree what counts as a failure, the operating lifetime, and the environment (temperature, moisture, corrosive atmosphere, dust, vibration, shock, supply and EM disturbances); a figure cannot be extrapolated to other conditions without knowing the parameter dependencies | R(t) specified with failure definition, period, environment | spec | reliability requirements | review | §9.4.1 p.383-384 | high |
| WILSON-389 | reliability | MTBF = 1/lambda during the constant failure-rate period (after infant mortality, before wear-out): e.g. MTBF 10 000 h = 0.0001 faults/h = 100 faults per 1e6 h; MTTF for non-repairable parts = mean of observed lifetimes in life testing | MTBF = 1/lambda | lambda | reliability figures | calc | §9.4.1 p.384 | high |
| WILSON-390 | reliability | Availability A = U/(U + D) = MTBF/(MTBF + MTTR) (up-time, down-time, mean time to repair) - also the probability the system is working at a given instant; validate predicted MTBF/MTTR by logging operating data | A = MTBF/(MTBF + MTTR) | MTBF, MTTR | availability requirements | calc | §9.4.1 p.384 | high |
| WILSON-391 | cost | Reliability vs cost: unit cost rises and life-cycle (operating/repair) cost falls with designed-in reliability, giving a cost-optimum reliability (Fig 9.9); safety-critical systems (nuclear/chemical plant control, railway signalling, flight-critical avionics) must instead meet a defined reliability with cost secondary | minimise life-cycle cost (non-safety) | cost model | reliability targets | review | §9.4.2 p.385, Fig 9.9 | high |
| WILSON-392 | reliability | Temperature: Arrhenius failure rate lambda = K*exp(-E/(k*T)) (k = 1.38e-23 J/K, T absolute, E = activation energy); many mechanisms have E ~ 0.5 eV, giving roughly a doubling of failure rate per 10 C rise (rule of thumb for multi-component equipment); higher-E reactions accelerate faster | lambda(T+10) ~ 2*lambda(T) | T | reliability vs temperature | calc | §9.4.3 p.385-386 | high |
| WILSON-393 | derating | Capacitor voltage derating: near maximum working voltage the failure rate rises as the FIFTH power of voltage - running at half rated voltage gives a 32x lower failure rate; film parts rated 50/100 V in 5 V circuits are naturally derated; heavily derate electrolytics (already the highest failure-rate parts, drying out at high temperature) | lambda ~ (V/V_rated)^5; V <= 0.5*V_rated -> /32 | V_op, V_rated | capacitor selection | calc | §9.4.3 p.386 | high |
| WILSON-394 | derating | Resistor power derating lowers internal temperature and failure rate; in low-voltage circuits only low values need checking: 0.4 W metal film on a 10 V maximum supply - every resistor above 500 ohm is derated by at least 2x (V^2/R = 0.2 W), normally enough | P = V_max^2/R <= 0.5*P_rated | V_max, R | resistor derating | calc | §9.4.3 p.386 | high |
| WILSON-395 | derating | Semiconductor derating on power, current and voltage all improve failure rate; most important are power dissipation (junction temperature rise, cooling) and operating voltage, especially where transient overvoltages are possible | derate P, I, V | ratings, transients | semiconductor selection | calc | §9.4.3 p.386 | high |
| WILSON-396 | reliability | Cost of finding and replacing a faulty part rises by an order of magnitude at each stage (goods-in -> board assembly -> test -> final assembly -> field repair) - consider guaranteed-reliability (assessed quality) parts; Europe: CECC harmonized quality assessment scheme (superseded BS 9000) with generic specifications (physical, mechanical, electrical, test) | cost x10 per stage | production flow | procurement strategy | review | §9.4.3 p.386-387 | high |
| WILSON-397 | reliability | Stress screening / burn-in: operate under stress (elevated temperature, vibration, humidity, max rated voltage) to precipitate early failures - typical 160 h at 125 C, or repeated temperature cycling between range extremes for bonding/mechanical faults; applicable to parts and assemblies; use on the first batches of a new design to find recurrent production faults; expensive, not a crutch for poor production; standard only if the customer pays | 160 h @ 125 C typical | new-product batches | early production | measure | §9.4.3 p.387 | high |
| WILSON-398 | reliability | Series reliability model: assembly failure rate ~ sum of component failure rates (any failure fails the assembly) - highest reliability comes from the simplest circuit; minimise component count (Occam's razor) | lambda_assy = sum(lambda_i) | BOM failure rates | architecture | calc | §9.4.3 p.387 | high |
| WILSON-399 | reliability | Redundancy: paralleled subsystems each able to carry the full load (e.g. diode-OR'ed power supplies) fail together with probability = product of individual failure probabilities, provided common-mode failures (e.g. loss of mains) are excluded and interconnections are reliable; component-level redundancy is mandatory in intrinsic safety (triple parallel zener barrier survives two open-circuit zener failures, Fig 9.10); provide detection/indication of a failed redundant element or reliability collapses | P_sys_fail = product(P_i) (independent) | P_i | redundant designs, IS barriers | calc | §9.4.3 p.388, Fig 9.10 | high |
| WILSON-400 | reliability | MTBF prediction by summing component failure rates from MIL-HDBK-217F Notice 2 (US DoD; models by operating/environmental conditions, derating, construction/package, IC complexity and pinout) or British Telecom HRD4; data lag technology (pessimistic, especially ICs), results are order-of-magnitude; use software tools; value lies in finding the dominant contributors (often electrolytics -> derate or add redundancy) and guiding service diagnosis, not in predicting actual life | lambda_total = sum(lambda_i(conditions)) | BOM stresses | reliability prediction | calc | §9.4.4 p.388-389 | high |
| WILSON-401 | process | Design reviews: frequent peer critiques by reviewers unconnected with the project, questioning unstated assumptions: concept sound and cost-effective, all component tolerances accounted for, no part operated outside ratings; tolerate harmless personal idiosyncrasies; hold before mistakes become costly | review held per design stage | design package | design process | review | §9.4.5 p.389-390 | high |
| WILSON-402 | thermal | Thermal-electrical analogy (Table 9.2): temperature difference (C) = voltage, thermal resistance (C/W) = resistance, heat flow (W) = current, heat capacity (J/C) = capacitance; 0 V = 0 C; ambient assumed infinite heat capacity. Simple model: T = PD*R_theta + TA, with TA the extreme of the specified ambient range | T = PD*R_th + TA_max | PD, R_th, TA | all thermal calcs | calc | §9.5.1 p.390-391, Table 9.2, Fig 9.11 | high |
| WILSON-403 | thermal | Power device on heatsink: Tj = PD*(Rth_j-c + Rth_c-h + Rth_h-a) + TA (Rth_c-a in parallel, negligible with a large heatsink) and Tj must not exceed the data-sheet maximum. Example IRF640, 35 W, heatsink 0.5 C/W, insulating pad 0.8 C/W, Rth_j-c 1.0 C/W, TA 70 C: Tj = 35*(1.3 + 1.0) + 70 = 150.5 C (> 150 C max -> bigger heatsink); including Rth_j-a 80 C/W in parallel gives 148.25 C (not enough to rely on). The 125 W rating assumes 25 C case - even a 0.5 C/W heatsink (~80 sq in) allows only 35 W at 70 C ambient: use derating curves; paralleling two devices halves each device's dissipation and junction rise | Tj = PD*sum(Rth) + TA <= Tj_max | PD, Rth chain, TA | heatsink sizing | calc | §9.5.1 p.391-392, Fig 9.12 | high |
| WILSON-404 | thermal | Thermal capacity: heatsink capacitance Ch = volume x volumetric heat capacity (Table 9.3, Al 2.47 J/cm^3/C); a 1 C/W aluminium heatsink of ~120 cm^3 has 296 J/C -> time constant ~296 s; capacity does not change steady-state temperature, only the time to reach it, but reduces peak Th/Tj for low-duty transient heat pulses (analyse with the RC analog, Fig 9.13) | tau = Rth*Ch | volume, material | transient heating | calc | §9.5.1 p.392-393, Fig 9.13, Table 9.3 | high |
| WILSON-405 | thermal | Pulsed dissipation faster than the heatsink time constant: Tj = PDmax*[K*Rth_j-c + d*(Rth_c-h + Rth_h-a)] + TA, d = duty cycle, K from transient thermal impedance curves (Fig 9.14, IRF640), PDmax = on-period power; above a few kHz with duty > 20% K -> d (average power governs); current crowding (RF amplifiers, highly inductive loads) invalidates thermal-resistance methods - observe SOA and di/dt limits | Tj = PDmax*(K*Rjc + d*(Rch + Rha)) + TA | PDmax, d, K | pulsed power devices | calc | §9.5.1 p.394, Fig 9.14 | high |
| WILSON-406 | thermal | Heatsinks: prefer proprietary parts characterised for Rth (free air, fins vertical) over custom designs; fins vertical - horizontal orientation loses up to 30% efficiency; black-anodised aluminium (radiative efficiency 10-15x polished) is the norm, copper for maximum conductivity (heavier, dearer) | vertical fins; derate 30% if horizontal | orientation, finish | heatsink selection | calc | §9.5.2 p.394-395 | high |
| WILSON-407 | thermal | Altitude derating of free-air cooling (Table 9.4): sea level 100%, 2000 ft 97%, 5000 ft 90%, 10 000 ft 80%, 20 000 ft 63% (pressure falls ~1 mb per 30 ft from 1013 mb; heat transfer ~ air density) | Rth_h-a(alt) = Rth_h-a / eff(alt) | altitude | high-altitude products | calc | §9.5.2 p.395, Table 9.4 | high |
| WILSON-408 | thermal | Heatsink geometry and operating point: efficiency does not scale linearly with size (air heats along the fins; spreading resistance) - performance ~ proportional to width across the airflow and ~ sqrt(fin length) along it, so shorter-wider beats longer; Rth_h-a falls with temperature difference: at 20 C rise it is ~80% of the 10 C value (i.e. at 10 C rise it can be 25% higher than quoted at 20 C) | perf ~ W * sqrt(L); Rth(10 C) ~ 1.25 * Rth(20 C) | geometry, dT | heatsink sizing | calc | §9.5.2 p.395-396 | high |
| WILSON-409 | thermal | Forced-air heatsinks: design empirically or by thermal simulation (analytics are ballpark); Fig 9.15 gives Rth vs air velocity for flat plates (graph); staggered fins improve transfer; radiation becomes negligible so surface finish is irrelevant (bare aluminium as good as black anodised); verify prototypes with a thermocouple and a power resistor on a DC supply as the heat source | measure dT at known P | prototype | forced-air cooling | measure | §9.5.2 p.396, Fig 9.15 | high |
| WILSON-410 | thermal | Enclosure ventilation fan: flow (m^3/h) = 3600*PD/(rho*c*theta) for internal rise theta (C) with PD watts; air at 30 C: rho = 1.3 kg/m^3, c ~ 1000 J/kg/C; 1 CFM = 1.7 m^3/h; read the operating point from the fan's flow vs pressure-drop curve against the system resistance (filters, louvres, PCBs), usually derived empirically | Q = 3600*PD/(1300*theta) m^3/h | PD, theta | fan selection | calc | §9.5.2 p.396-397 | high |
| WILSON-411 | thermal | Radiation: Q = 5.7e-12 * dT^4 * emissivity W/cm^2 (as printed; physically use T^4 - Tamb^4 in kelvin, cf. §2.3.4); radiant heat travels line of sight and heats neighbouring parts, contributes little for finned sinks (fins face each other) but helps hot parts with a clear view to ambient; matt beats glossy, colour hardly matters, keep coatings thin (convection); shiny foil shields heat-sensitive parts; keep external heatsinks out of sunlight | Q_rad = 5.7e-12 * eps * dT^4 W/cm^2 (printed) | eps, T | radiative cooling | calc | §9.5.2 p.397, Table 9.3 | medium |
| WILSON-412 | mechanical | Heatsink mounting surface: finish comparable to the device (50-60 microinch adequate for most); flatness < 4 mil per inch (0.004 in/in) across the mounting area; mounting hole just clears fastener (+ bush) - oversize holes with over-torque deform the tab into the hole, lift the package over the die and can crack it; no chamfers, but de-burr (insulation puncture, contact); clean dust, grease and swarf just before assembly | flatness <= 0.004 in/in; finish 50-60 uin | mechanical drawing | power device mounting | inspect | §9.5.3 p.397-398, Fig 9.16 | high |
| WILSON-413 | assembly | Lead bending: mount upright where possible; plastic packages (TO220, TO126) may be bent only >= 4 mm from the body, radius >= 2 mm, angle <= 90 degrees, never repeatedly at the same point, no axial strain (round-nosed pliers or forming jig); never bend leads of metal-cased devices (glass seal). Solder leads only after the mechanical fastening is tightened; do not let production insert screws after mass soldering to keep cadmium-plated screws out of the bath - hand solder or change the screws | bend >= 4 mm from body, R >= 2 mm, <= 90 deg | package, assembly flow | power device assembly | inspect | §9.5.3 p.398 | high |
| WILSON-414 | thermal | Insulating interface: best thermally is to isolate the whole heatsink, or use fully isolated packages; otherwise polyimide, mica or hard-anodised aluminium washers need a THIN film of thermal grease (fills voids only - more is not better; excess collects dust/swarf and breaks down), silicone rubber can be used dry; keep contact force >= 20 N (more is better short of damage); washer holes no larger than the device holes (flashover); interface resistances per Table 9.5 (e.g. TO220 0.6-1.2 C/W metal-to-metal, 1.6-3.4 mica, 2.2-4.5 polyimide, 1.8 silicone rubber) | F_clamp >= 20 N; Rth_c-h per Table 9.5 | package, washer | power device insulation | calc | §9.5.3 p.399, Table 9.5 | high |
| WILSON-415 | mechanical | Mounting hardware: check package hole tolerances (vary between manufacturers); flat washer (rectangular for plastic packages) under the screw head to spread pressure; conical compression washer gives correct force without a torque driver; correct torque is critical (too little: high Rth; too much: package failure); for isolated screw mounting put the insulating bush in the heatsink with large flat washers; bush of glass-filled nylon or polycarbonate (not unfilled nylon - creeps), long enough to overlap and prevent flashover; spring clips press directly over the die (lower Rth for plastic packages, no washer hole); a rigid clamping bar with enough fixings for several TO220s | correct torque; no unfilled nylon bushes | hardware | power device mounting | inspect | §9.5.3 p.400, Fig 9.17 | high |
| WILSON-416 | thermal | Thermal placement: mount PCBs vertically for convection and don't block airflow with solid screens (use punched/louvred/mesh); put hot parts near board edges and at the top of vertical boards; keep them away from (or above) precision op-amps and electrolytic capacitors; allow for internal enclosure temperature rise; put heatsinks near the air outlet, not the inlet, and never obstruct their airflow; for high heat density use a thermally conductive ladder bonded to an external heatsink (laminate conducts heat poorly); in sealed cases heat passes through three convection stages - mount hot parts to the case but check the external case temperature for safety | layout rules met | placement | board/enclosure thermal layout | inspect | §9.5.4 p.401 | high |
| WILSON-417 | process | PCB fabrication data package: artwork for all copper layers; solder-mask artwork; ident, peelable and carbon layers as applicable; drilling data; board or panel drawings; material specification (usually the fabricator's standard materials); metallic finish; solder-mask and ident type/colour; layer build; testing requirements - keep a company "boilerplate" specification so only differences need review; involve purchasing (prototype vs production suppliers differ) | all items in package | fab package | PCB release | inspect | §2.5 p.83-84 | high |
| WILSON-418 | process | In-house PCB design rules (base on BS 6221 Part 3) should cover track width/spacing, hole/pad sizes, routing, ground distribution, solder mask/legend/finish and terminations; know the chosen fabricator's capabilities (Table 2.2); review the rules regularly against process advances (a 0.3 mm minimum track rule forfeits density) and never enforce them so rigidly that they prevent an optimum design | rules reviewed periodically | fab capability | design-rule governance | review | §2.2 p.55 | high |

## 2. Formulas & tables (numbers)

### Table 1.1 Conductivity of metals (relative to Cu = 1 at 20 C) and tempco of resistance (/C at 20 C) — p.7
| Metal | Relative conductivity | Tempco (/C) |
|---|---|---|
| Aluminium (pure) | 0.59 | 0.0039 |
| Al alloy soft-annealed | 0.45–0.50 | 0.0039 |
| Al alloy heat-treated | 0.30–0.45 | 0.0039 |
| Brass | 0.28 | 0.002–0.007 |
| Cadmium | 0.19 | 0.0038 |
| Copper hard-drawn | 0.895 | 0.00382 |
| Copper annealed | 1.0 | 0.00393 |
| Gold | 0.65 | 0.0034 |
| Iron pure | 0.177 | 0.005 |
| Iron cast | 0.02–0.12 | 0.005 |
| Lead | 0.7 (as printed; physical value ~0.07 — print/OCR ambiguity) | 0.0039 |
| Nichrome | 0.0145 | 0.0004 |
| Nickel | 0.12–0.16 | 0.006 |
| Silver | 1.06 | 0.0038 |
| Steel | 0.03–0.15 | 0.004–0.005 |
| Tin | 0.13 | 0.0042 |
| Tungsten | 0.289 | 0.0045 |
| Zinc | 0.282 | 0.0037 |
Mild steel ~3x the bulk resistance of aluminium; die-cast zinc 28% of copper (p.6).

### Table 1.2 Characteristics of bare copper wire — p.23
| Wire dia (mm) | SWG (approx) | AWG (approx) | Current rating (A) | Fusing current (A) | Resistance/m at 20 C (ohm) | Inductance of 1 m length (uH) |
|---|---|---|---|---|---|---|
| 1.6 | 16 | 14 | 22 | 70 | 0.0085 | 1.36 |
| 1.25 | 18 | 16 | 12.2 | 45 | 0.014 | 1.41 |
| 0.71 | 22 | 21 | 3.5 | 25 | 0.043 | 1.53 |
| 0.56 | 24 | 23 | 2.5 | 17 | 0.069 | 1.57 |
| 0.315 | 30 | 28 | 0.9 | 9 | 0.22 | 1.69 |
| 0.2 | 35 | 32 | 0.33 | 5 | 0.54 | 1.78 |
Wire inductance: L[uH] = K * l * (2.3*log10(4l/d) - 1), K = 0.0051 (inch) / 0.002 (cm), l >> d. Rule of thumb 20 nH/inch, 7 nH/cm.

### Table 1.3 BS 4808 PVC equipment wire — p.24
| Size (strands/mm) | R (ohm/1000 m @20 C) | I rating @70 C (A) | I rating @25 C (A) | V drop per m at 25 C current (mV) | Voltage rating (kV) | OD (mm) | Near AWG |
|---|---|---|---|---|---|---|---|
| 1/0.6 | 64 | 1.8 | 3.0 | 192 | 1 | 1.2 | 23 |
| 7/0.2 | 88 | 1.4 | 2.0 | 176 | 1 | 1.2 | 24 |
| 16/0.2 | 38 | 3.0 | 4.0 | 152 | 1 | 1.55 | 20 |
| 24/0.2 | 25.5 | 4.5 | 6.0 | 153 | 1.5 | 2.4 | 18 |
| 32/0.2 | 19.1 | 6.0 | 10.0 | 191 | 1.5 | 2.6 | 17 |
| 63/0.2 | 9.7 | 11.0 | 18.0 | 175 | 1.5 | 3.0 | 15 |
PVC to BS 4808: 85 C max; 70 C ratings allow a 15 C rise; PTFE to 200 C; silicone rubber 150 C.

### Table 1.4 Wire-wrap wire — p.24
| Type | Conductor dia (mm) | Max service temp (C) | R/m @20 C (ohm) | Voltage rating (V) | Current rating @50 C (A) |
|---|---|---|---|---|---|
| Kynar 30 AWG | 0.25 | 105 | 0.345 | – | – |
| Kynar 26 AWG | 0.4 | 105 | 0.136 | – | – |
| Tefzel 30 AWG | 0.25 | 155 | 0.345 | 375 | 2.6 |
| Tefzel 26 AWG | 0.4 | 155 | 0.136 | 375 | 4.5 |

### Table 1.5 BS 6500 mains cables (source: IEE Wiring Regulations 17th ed.) — p.25
| CSA (mm^2) | Current capacity (A) | V drop per A per m (mV) | Max supportable mass (kg) |
|---|---|---|---|
| 0.5 | 3 | 93 | 2 |
| 0.75 | 6 | 62 | 3 |
| 1.0 | 10 | 46 | 5 |
| 1.25 | 13 | 37 | 5 |
| 1.5 | 16 | 32 | 5 |
| 2.5 | 25 | 19 | 5 |
Ambient correction factor CF — 60 C rubber & PVC: 35 C 0.92; 40 C 0.82; 45 C 0.71; 50 C 0.58; 55 C 0.41. 85 C HOFR rubber: 35–50 C 1.0; 55 C 0.96; 60 C 0.83; 65 C 0.67; 70 C 0.47.

### Table 1.6 Data transmission cables — p.26
| Cable type | Inter-conductor C (pF/m) | Conductor-screen C (pF/m) | Z0 (ohm) | Voltage rating (V) |
|---|---|---|---|---|
| Ribbon, straight | 50 | – | 105 | 300 |
| Ribbon, twisted pair | 72 | – | 105 | 300 |
| Round Type A (multi-pair/multicore, overall foil screen) | 40–115 | 66–213 | – | 300 |
| Round Type B (multi-pair, individually foil screened) | 41–98 | 72–180 | 50 | 30 |
Standard multicore conductor-to-screen capacitance 150–200 pF/m (p.25); braid coverage 80–95%.

### Table 1.7 TIA/EIA-568 (ISO/IEC 11801) 100 ohm quad-pair cable — p.27
| Parameter | Cat 3 | Cat 5 | Cat 5e | Cat 6 |
|---|---|---|---|---|
| Bandwidth (MHz) | 16 | 100 | 100 | 250 |
| Z0 at 0.1 MHz | 75–150 ohm | 75–150 ohm | N/A | N/A |
| Z0 at >= 1 MHz | 100 +/- 15 ohm | 100 +/- 15 | 100 +/- 15 | 100 +/- 15 |
| Attenuation dB/100 m @0.256 MHz | 1.3 | 1.1 | 1.1 | N/A |
| @1.0 MHz | 2.6 | 2.1 | 2.1 | 2.0 |
| @4.0 MHz | 5.6 | 4.3 | 4.3 | 3.8 |
| @10 MHz | 9.8 | 6.6 | 6.6 | 6.0 |
| @16 MHz | 13.1 | 8.2 | 8.2 | 7.6 |
| @31.25 MHz | N/A | 11.8 | 11.8 | 10.7 |
| @62.5 MHz | N/A | 17.1 | 17.1 | 15.4 |
| @100 MHz | N/A | 22.0 | 22.0 | 19.8 |
| @200 MHz | N/A | N/A | N/A | 29.0 |
| @250 MHz | N/A | N/A | N/A | 32.8 |
| Capacitance unbalance @1 kHz | 3400 pF/km | 3400 pF/km | 330 pF/100 m | 330 pF/100 m (printed: three values for four columns) |
| DC loop resistance | 19.2 ohm/100 m, max unbalance 3% (all categories) | | | |
| Return loss (dB, 100 m) 1–10 MHz | 12 | 23 | 20+5log(f) | 20+5log(f) |
| 10–20 MHz | 12–10log(f/10) | 23 | 25 | 25 |
| 20–100 MHz | N/A | 23–10log(f/20) | 25–7log(f/20) | 25–7log(f/20) |
| 200 MHz | N/A | N/A | N/A | 18.0 |
| 250 MHz | N/A | N/A | N/A | 17.3 |
(Return-loss cell-to-column mapping reconstructed from the flattened table; conf medium.)

### Table 1.8 50 ohm coaxial cables — p.29
| Type | OD (mm) | Conductor | Dielectric | Voltage rating* | Atten dB/10 m @100 MHz | @1 GHz | Temp range (C) | Cost/100 m (GBP, 1990) |
|---|---|---|---|---|---|---|---|---|
| URM43 | 5 | Solid 1/0.9 | solid polythene | 2.6 kV pk | 1.3 | 4.5 | -40 to +85 | 18.9 |
| URM67 | 10.3 | Str 7/0.77 | solid polythene | 6.5 kV pk | 0.68 | 2.5 | -40 to +85 | 70.0 |
| RG58C/U | 5 | Str 19/0.18 | solid polythene | 3.5 kV pk | 1.6 | 6.6 | -40 to +85 | 22.5 |
| RG174A/U | 2.6 | Str 7/0.16 | solid polythene | 1.5 kV RMS | 2.9 | 10 | -40 to +85 | 26.3 |
| RG178B/U | 1.8 | Str 7/0.1 | PTFE | 1 kV RMS | 4.4 | 14 | -55 to +200 | 81.9 |
*Voltage ratings may be specified differently between manufacturers. Standards: MIL-C-17 (RG/U), BS 2316 (UR-M), IEC 60096.

### Table 1.9 Characteristic impedance vs geometry — p.41 (h = separation, w = width, d = wire dia, t = thickness, D = outer dia; all same units)
| Geometry | Z0 (ohm) |
|---|---|
| Side-by-side parallel strip | Z0 = 120/sqrt(er) * ln( h/w + sqrt((h/w)^2 - 1) ) |
| Face-to-face parallel strip | Z0 = 377/sqrt(er) * h/w (if h > 3t, w >> h); Z0 = 120/sqrt(er) * ln(4h/w) (if h >> w) |
| Parallel wire | Z0 = 120/sqrt(er) * ln( h/d + sqrt((h/d)^2 - 1) ); = 120/sqrt(er) * ln(2h/d) if d << h. Typical PVC pairs / twisted pairs ~100 ohm |
| Wire parallel to infinite plate | Z0 = 60/sqrt(er) * ln( 2h/d + sqrt((2h/d)^2 - 1) ); = 60/sqrt(er) * ln(4h/d) if d << h |
| Strip parallel to infinite plate | Z0 = 377/sqrt(er) * h/w (if w > 3h); Z0 = 60/sqrt(er) * ln(8h/w) (if h > 3w) |
| Coaxial | Z0 = 60/sqrt(er) * ln(D/d) |
Free-space impedance 377 ohm (120*pi).

### Table 1.10 Dielectric constants — p.42
| Material | er | Velocity factor 1/sqrt(er) |
|---|---|---|
| Air | 1.0 | 1.0 |
| Polythene/polyethylene | 2.3 | 0.66 |
| PTFE | 2.1 | 0.69 |
| Silicone rubber | 3.1 | 0.57 |
| FR4 fibreglass PCB | 4.5 (typ) | 0.47 |
| PVC | 5.0 | 0.45 |

### Grounding, crosstalk and transmission-line formulas — §1.1–1.3
- Ground-loop EMF: V = -1e-8 * A[cm^2] * n * dB/dt[uT/s]; example 10 uT, 50 Hz, 10 cm^2 -> 314 uV pk
- Shared return drop: Vs = Rs * sum(I); example 0.2 ohm x 1.25 A = 0.25 V
- Wire drop with inductance: V = L*di/dt + R*I (1 m 16/0.2: 38 mohm, 1.5 uH; 4 A/us -> 6 V)
- Output-input coupling: Vout/Vin = A/(1 + A*Rs/(RL+Rs)); unstable if A*Rs/(RL+Rs) < -1
- Surface transfer impedance: braid ~10 mohm/m below 1 MHz, +20 dB/decade; foil ~20 dB worse
- Earth continuity (EN 60065): < 0.5 ohm at 10 A for 1 min
- Lumped crosstalk: XT = Zv/(Zv + Zs + 1/(2*pi*f*Cc)); edge crosstalk I = C*dV/dt*(1 - exp(-t/RC))
- lambda = 3e8/f (m); lambda_d = lambda/sqrt(er); line if length > lambda_d/10 (lambda_d/40 precision) or tr < 3 x transit
- Z0 = sqrt((R + jwL)/(G + jwC)); lossless sqrt(L/C); v = 1/sqrt(LC) = 3e8/sqrt(er)
- Gamma = (Z - Z0)/(Z + Z0); SWR = (1 + abs(Gamma))/(1 - abs(Gamma)) = RL/Z0 (resistive)
- Quarter-wave: Zin = Z0^2/ZL; ringing ~35 MHz / L[m] (0.6 mm track on 1.6 mm FR4 over plane)
- rho_v = (VSWR - 1)/(VSWR + 1); phase(deg) = 720*(x/lambda - 1/4)
- Coax design: D = d*exp(Z0*sqrt(er)/60) (24 SWG, PTFE, 50 ohm -> D = 1.873 mm)
- Shorted-stub pulse: t = 2L/(VF*3e8) (1 m, VF 0.66 -> 10 ns)

### Table 2.1 PCB laminate material properties — p.47
| Material | Surface resistance min (Mohm) | Dielectric er | tan d max | Dielectric strength min (kV/mil) | Tempco x-y (ppm/C) | Max temp (C) |
|---|---|---|---|---|---|---|
| Standard FR4 | 1e4 | max 5.4, typ 4.6–4.9 | 0.035 | 1.0 | 13–16 | 110–150 |
| FR408 (high quality) | 1e6 | 3.8 | 0.01 | 1.4 | 13 | 180 |
| Epoxy-aramid (close tolerance) | 5e6 | 3.8 | 0.022 | 1.6 | 10 | 180 |
| Polyimide (Kapton) | – | 3.4 | 0.01 | 3.8 | 20 | 300 |
| Polyester (Mylar) | – | 3.0 | 0.018 | 3.4 | 27 | 105 |
Copper: 1 oz = 0.035 +/- 0.002 mm; available 0.25, 0.5, 1, 2, 3, 4 oz.

### Table 2.2 Typical best capabilities of PCB manufacturers — p.55
| Parameter | Value |
|---|---|
| Board thickness range | 0.35–3.5 mm |
| Maximum number of layers | 14–24 |
| Minimum track and gap width (1 oz Cu) | 0.1 mm possible, 0.15 mm preferred |
| Minimum PTH hole diameter | 0.2 mm possible, 0.3 mm preferred |
| Maximum PTH aspect ratio | 12:1 possible, 6:1 preferred |
| Registration drill to pad | 0.03 mm |
| Registration layer to layer incl. solder mask | 0.075 mm |

### PCB numeric rules (Ch.2)
| Item | Value | Source |
|---|---|---|
| Track resistance | R = rho*l/A; manufactured tolerance up to 2:1; PTH > 0.8 mm < 1 mohm | p.56 |
| Safe track current | Fig 2.11 (graph, BS 6221 Pt 3:1984) — no numbers in text | p.57 |
| Breakdown spacing (benign env.) | 1 mm per 200 V | p.57 |
| Wave-solder bridging risk (no resist) | spacing < 0.5 mm | p.57 |
| Crosstalk rule of thumb | spacing > 1 mm -> < 10% coupling | p.57 |
| Component hole | lead dia + 0.15–0.3 mm; std 0.8 mm (DIL/small), 1.0 mm (large) | p.58 |
| Via aspect ratio | <= 6:1 comfortable; via = smallest component hole or one size smaller (0.6 mm) | p.58 |
| PTH pad for 0.8 mm hole | 1.3–1.5 mm | p.59 |
| Non-PTH pad | ~2 mm for 0.8 mm hole; >= hole + 1 mm; pad/hole ~2 (FR4), 2.5–3 (SRBP) | p.59 |
| Track to board edge | >= 0.5 mm | p.60 |
| Screen-printed resist clearance | 0.3–0.4 mm | p.65 |
| Photo-imaged resist registration | better than 0.1 mm | p.66 |
| Test pad | <= 1 mm dia, component-free, opposite side | p.72 |
| Conformal coat pre-bake | 2 h at 65–70 C; 2–3 coats | p.81 |
| Packing density | 4–7 cm^2 per 16-pin DIL (2-layer PTH), ~2 cm^2 (multilayer) | p.50 |
| Board size | Eurocard 100 x 160; double 233.4 x 160; large boards 30–50 cm max edge | p.51 |
| Prototype PCB service | 4–5 days, 2–5x production price | p.83 |
| Tubular component lead pitch | single pitch, 0.4 or 0.5 inch popular | p.73 |

### Thermal formulas (§2.3.4)
- Conduction: Q = k*A*(TH - TL)/L; R_theta = L/(k*A)
- Forced air: Airflow[cfm] = 1.76*Wloss/dT; Airflow[lpm] = 28.32*1.76*Wloss/dT (sea level)
- Radiation: P = 5.67e-8 * E * (T^4 - Tamb^4) (W/m^2, K)
- MTBF: lambda_m = sum_i A_ti*S_i*lambda_i; A_ti = exp((ea/k)*(1/Tref - 1/Top)), k = 8.6e-5 eV/K

### Table 2.3 Surface emissivity — p.75
| Surface | Emissivity |
|---|---|
| Aluminium polished | 0.04 |
| Aluminium painted (any colour) | 0.9 |
| Aluminium rough | 0.056 |
| Aluminium matt anodised | 0.8 |
| Copper rolled bright | 0.03 |
| Steel plain | 0.5 |
| Steel painted (any colour) | 0.8 |

### Table 2.4 Coefficients of thermal expansion — p.77
| Material | alpha (/C) |
|---|---|
| Aluminium | 24e-6 |
| Brass | 19e-6 |
| Steel | 13e-6 |
| Copper | 17e-6 |
| Gold | 14e-6 |
| Silver | 18e-6 |

### Surface insulation resistance — p.79
Ri = 160 * Rm * (w/l); real boards 10–1000x lower.

### Table 3.1 Survey of resistor types — p.87-88 (ranges for guidance; costs UK medium quantity at time of writing)
| Type | Ohmic range | Power range | Tolerance | Tempco range | Application |
|---|---|---|---|---|---|
| Carbon film | 2.2 – 10 M | 0.25–2 W | 5% | -150 to -1000 ppm/C | general purpose / commercial (< 1 p) |
| Carbon composition | 2.2 – 10 M | 0.25–1.0 W | 10% | +400 to -900 ppm/C | pulse, low inductance (1–3 p) |
| Metal film (standard) | 1 – 10 M | 0.125–2.5 W | 1%, 2%, 5% | +/-50 to 200 ppm/C | general purpose / industrial & military |
| Metal film (high ohm) | 1 – 100 M | 0.5–1 W | 5% | +/-200 to 300 ppm/C | high voltage and special |
| Metal glaze | 1 – 100 M | 0.25 W | 2%, 5% | +/-100 to 300 ppm/C | small size |
| Wirewound | 0.1 – 33 k (0.01 ... aluminium-housed) | 2–20 W (10–100 W aluminium) | 5%, 10% | +/-75 to 400 ppm/C | high power (15–50 p; 50 p–GBP 1 Al) |
| Metal film (precision) | 0.5 – 1 M | 0.125–0.4 W | 0.05 to 1% | +/-15 to 50 ppm/C | precision (10–50 p) |
| Wirewound (precision) | to 1 M | 0.1–0.5 W | 0.01 to 0.1% | +/-3 to 10 ppm/C | extra precision (GBP 2–20) |
| Bulk metal (precision) | 1 – 200 k | 0.33–1 W | 0.005 to 1% | +/-1 to 5 ppm/C | extra precision |
| Resistor networks/arrays | 1 – 10 M | 0.125–0.3 W per element | 2% | +/-100 to 300 ppm/C; +/-50 ppm/C tracking | multi-resistor (10–35 p) |
| SM chip film | 0 – 10 M | 0.1–0.5 W | 1%, 2%, 5% | +/-100 to 200 ppm/C | surface mount, hybrids (0.2–2 p) |
(Cost column mapping to rows partly ambiguous in the flattened print.)

### Table 3.2 Chip resistor sizes (L x W x H, mm) — p.89
| Size | Dimensions |
|---|---|
| 0201 | 0.6 x 0.3 x 0.25 |
| 0402 | 1.0 x 0.5 x 0.25 |
| 0603 | 1.6 x 0.8 x 0.45 |
| 0805 | 2.0 x 1.25 x 0.5 |
| 1206 | 3.2 x 1.6 x 0.6 |
| 1210 | 3.2 x 2.6 x 0.6 |
| 2010 | 5.1 x 2.5 x 0.6 |
| 2512 | 6.5 x 3.2 x 0.6 |

### Table 3.3 IEC 60063 standard values — p.96
- E6 (+/-20%): 1.0, 1.5, 2.2, 3.3, 4.7, 6.8
- E12 (+/-10%): 1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2
- E24 (+/-5%): 1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1
- E48 (+/-2%): 1.00, 1.05, 1.1, 1.15, 1.21, 1.27, 1.33, 1.40, 1.47, 1.54, 1.62, 1.69, 1.78, 1.87, 1.96, 2.05, 2.15, 2.26, 2.37, 2.49, 2.61, 2.74, 2.87, 3.01, 3.16, 3.32, 3.48, 3.65, 3.83, 4.02, 4.22, 4.42, 4.64, 4.87, 5.11, 5.36, 5.62, 5.90, 6.19, 6.49, 6.81, 7.15, 7.50, 7.87, 8.25, 8.66, 9.09, 9.53
- Additional E96 (+/-1%): 1.02, 1.07, 1.13, 1.18, 1.24, 1.30, 1.37, 1.43, 1.50, 1.58, 1.65, 1.74, 1.82, 1.91, 2.00, 2.10, 2.21, 2.32, 2.43, 2.55, 2.67, 2.80, 2.94, 3.09, 3.24, 3.40, 3.57, 3.74, 3.92, 4.12, 4.32, 4.53, 4.75, 4.99, 5.23, 5.49, 5.76, 6.04, 6.34, 6.65, 6.98, 7.32, 7.68, 8.06, 8.45, 8.87, 9.31, 9.76

### Resistor formulas (§3.1)
- Divider worst case: V'/V = 1 - 2K*R1/[R2*(1-K) + R1*(1+K)]
- Normal PDF: 68.2% within 1 sigma, 95.45% within 2 sigma, 99.73% within 3 sigma; tolerance = 3 sigma
- Pulse: rectangular P_avg = (V^2/R)*(tau/T); exponential P_avg = (V^2/R)*(tau'/(2T))
- Derating rule of thumb: P <= 0.5*P_rated
- LEV example: 470 k, 0.33 W, 1206: 394 V needed for rated power; LEV 200 V -> 85 mW
- Tempco: 200 ppm/C x 50 C = 1%; reference divider example -> 1%, 25 ppm/C parts
- Pot usable where f x R < 1e6 Hz*ohm; small trimmer wiper max 100 mA

### Table 3.4 Survey of capacitor types — p.107-108
| Type | C range | WV range | Tolerance | Tempco / temp characteristic | Application | Unit cost |
|---|---|---|---|---|---|---|
| Metallised polyester | 1 nF–15 uF | 50–1500 V | 5, 10, 20% | non-linear +/-5% over -55..100 C | general coupling & decoupling | 5–50 p |
| Polycarbonate | 100 pF–15 uF | 63–1000 V | 5, 10, 20% | < -1% over -55..100 C | low tc, timing & filtering | 10 p–GBP 3 |
| Polypropylene | 100 pF–10 uF | 63–2000 V | 1, 5, 10% | +/-2% over -55..100 C | high power, high frequency | 10 p–GBP 1.50 |
| Polystyrene | 10 pF–47 nF | 30–630 V | 1–10% | -125 ppm/C | close tolerance, low loss | 7–50 p |
| Metallised paper | 1 nF–0.47 uF | 250 VAC | +/-20% | – | mains RFI suppression | 20 p–GBP 1.00 |
| Ceramic single layer (barrier layer) | 10–220 nF | 12–50 V | -20/+80% | (barrier layer type) | general purpose | 3 p–GBP 1.50 |
| Ceramic single layer (low-K/high-K) | 1 pF–47 nF | 50 V–6 kV | 2% to +80/-20% | dependent on dielectric | general purpose & HV | |
| Multilayer COG/NP0 | 1 pF–27 nF | 50–200 V | 2, 5, 10% | 0 +/- 30 ppm/C | low tc, frequency sensitive & timing | 30 p–GBP 2 moulded; 10 p–GBP 1.50 dipped; 3–60 p chip |
| Multilayer X7R | 1–680 nF | 50–200 V | 5, 10, 20% | non-linear +/-15% over -55..125 C | general coupling & decoupling | |
| Multilayer Y5V, Z5U | 1 nF–10 uF | 10 V, 16 V, 50 V, 100 V | 20%; -20/+80% | non-linear +22/-56% over +10..85 C | general coupling & decoupling | |
| Aluminium electrolytic | 0.1–68 000 uF (general 1–4700 uF) | 6.3–100 V, up to 450 V | -10/+30%, +/-20% | – | general reservoir & decoupling | 4 p–GBP 3 |
| Solid aluminium | 0.1–68 uF | 6.3–40 V | +/-20% | – | high performance | 10 p–GBP 10 |
| Tantalum bead and chip | 0.1–150 uF | 6.3–35 V | +/-20% | – | general purpose, small size | 20 p–GBP 2; 6 p–GBP 1 |
(WV/tolerance row alignment partly reconstructed from flattened print; conf medium for those cells.)

### Table 3.5 EIA 198 Class 2 ceramic temperature characteristic codes — p.113
| Low temp | High temp | Max dC (ref 25 C) |
|---|---|---|
| X = -55 C | 4 = +65 C | P = +/-10% |
| Y = -30 C | 5 = +85 C | R = +/-15% |
| Z = +10 C | 6 = +105 C | S = +/-22% |
| | 7 = +125 C | T = +22/-33% |
| | 8 = +150 C | U = +22/-56% |
| | | V = +22/-82% |

### Capacitor loss / stability numbers (§3.3)
| Dielectric | tan d (20 C, 1 kHz unless stated) | Tempco / dC | Dielectric absorption | Notes |
|---|---|---|---|---|
| Polyester | ~8e-3 | non-linear, high | – | varies with T and f |
| Polycarbonate | < 2e-3 | ~-1% at extremes | – | filters/timing |
| Polypropylene | ~3e-4 (constant with T) | -200 ppm/C | 0.02–0.03% | to 85 C (some 100 C) |
| Polystyrene | ~5e-4 | -125 ppm/C | 0.02–0.03% (0.01–0.02% quoted §3.3.8) | 85 C (some 70 C) |
| COG/NP0 | ~0.001 | 0 +/- 30 ppm/C | – | negligible V/f dependence |
| X7R | 0.025 | +/-15% (-55..125 C); +/-10% with V and f | – | |
| Y5V/Z5U | ~X7R | > 50% with T and V | – | WV <= 100 V |
| Type 1 single layer | ~1.5e-3 at 1 MHz | +100 to -1500 ppm/C | – | RF |
| Al electrolytic | 0.1–0.3 at 100 Hz | ~+/-20% | – | ESR ratio cold/20 C ~3–4 |
| Solid tantalum | 0.04–0.1 | +/-15% to +/-3% | – | |
Leakage: Al electrolytic 0.01–0.03 CV uA (low-leakage 0.002 CV uA); tantalum ~0.01 CV uA. Life: x2 per 10 C cooler (non-solid Al).
SRF examples: 47 uF tantalum ~500 kHz; 100 pF COG ~100 MHz.
Worst-case 0.1 uF example (5–30 V, 10–100 kHz, +10..85 C, 1000 h): Z5U 0.0202–0.219 uF (11:1); polycarbonate 0.089–0.11 uF; tantalum bead 0.038–0.125 uF.

### Magnetics formulas (§3.4)
- Q = w*L/Req; tan d = 1/Q
- Rdc = 4*rho*N*lw/(pi*d^2); rho_Cu = 1.709e-8 ohm*m; tempco 0.00393/C
- Skin depth D = sqrt(rho/(pi*mu0*mu_r*f)); negligible if d/D < 2; Rac/Rdc = 1 + F ~ (1/4)(d/D + 1) for d/D > 5
- Proximity loss (round conductors) P_pe = pi*w^2*Bmax^2*l*d^4/(128*rho)
- Soft magnetic Hc < 1 kA/m; hard Hc > 10 kA/m; ferrite sintering 1150–1300 C; iron powder mu <= ~30; NiZn usable to ~200 MHz
- Table 3.6 transition metals in ferrites XFe2O4: Mn, Zn, Ni, Co, Cu, Fe, Mg
- Table 3.7 metrics: BR remanence, HC coercive force, BMAX, HMAX, mu_MAX, mu_i
- Winding capacitance: scramble winding -20% vs layer; two-section former /3
- Inductive kick: V = -L*di/dt

### Crystal / resonator numbers (§3.5)
- fs = 1/(2*pi*sqrt(L*C)); fp = 1/(2*pi*sqrt(L*Cx)), Cx = C*Cp/(C+Cp), Cp = C0 + Cext
- Q 30,000–100,000; C ~ fF, L ~ H, R tens–hundreds ohm; AT cut at 35 deg 21'
- Rf 10–15 Mohm; strays <= 10 pF; C2:C1 ~ 3:1; drive 0.5–1 mW max; design start-up for 3x quoted R
- 32.768 kHz tuning fork: -0.04 ppm/C^2, turnover 25 C, -144 ppm at +85/-35 C (12 s/day)
- Ceramic resonator: tc ~1e-5/C, tol +/-0.5%; quartz tol +/-0.003%, < 1 ppm/C; LC 1e-3–1e-4/C

### Table 4.1 Schottky vs conventional diodes — p.154
| Conventional p-n | Schottky |
|---|---|
| VF typically 0.6 V at medium currents | VF typically 0.4 V |
| Minority-carrier charge storage limits speed | No minority carriers, no charge storage, high speed |
| High VBR achievable, > 1 kV | Low VBR, generally 30–100 V |
| Low reverse leakage | Higher reverse leakage |
Recovery times: conventional 1–20 us; fast 150–200 ns; ultra-fast down to 20 ns. Leakage doubles per 10 C (100 nA @25 C -> 2.2 uA @70 C). VF tempco -2 mV/C (Si p-n), ~-1 mV/C (Schottky at mA). kT/q = 0.025 V at 20 C; slope resistance 0.025/IF ohm. Rectifier surge 30–70x average (8.33 ms half-cycle, constant I^2t). Zener 2.4–270 V; minimum tempco 4.7–5.6 V; min slope resistance ~6.8 V; 1N821-type reference 6.2–6.4 V.

### Table 4.2 Power MOSFET / bipolar / IGBT — p.180
| Parameter | Power MOSFET | Power bipolar | IGBT |
|---|---|---|---|
| Max voltage | up to 1 kV | up to 1 kV | up to 1200 V |
| Max current | up to 100 A | up to 500 A | up to 500 A |
| Switching speed | typ. < 100 ns, independent of T | 0.3–5 us typical | 0.2–1 us typical; switching losses rise with T |
| Input | Voltage, VGSth 3–10 V, gain tempco -0.2%/C | Current, hFE 20–100, hFE tempco +0.8%/C | Voltage, VGEth 5–8 V, tempco -11 mV/C |
| Output | Resistive, current sharing when paralleled, RDSon tempco +0.7%/C, inherent body-drain diode | Non-resistive, current hogging when paralleled, VCEsat tempco -0.25%/C, no output diode | Hybrid, VCEsat tempco positive at high I / negative at low I, no output diode |
| Breakdown | SOA thermally limited; static precautions advisable | Second breakdown at high VCE; thermal runaway | SOA thermally limited; static precautions advisable |
| Unit cost* | 1.5 p/W | 0.75–1 p/W | 2 p/W |
*Average cost per watt of max 25 C dissipation, plastic package, n-channel/npn, 100 V or 600 V, 30–150 W.

### Snubber design (§4.2.6)
- C = 0.63 * Vpeak / ((dv/dt) * RL)
- R = max( Vpeak / (0.5*(ITSM - IL)), sqrt(Vpeak / (C * di/dt)) )
- Example: 1 kW heater, 240 V (Vpeak 340 V), RL cold 6 ohm, IL 56 A, TIC226M (500 V/us, ITSM 80 A) -> C 0.07 -> 0.1 uF; R 28.3 -> 27 ohm (di/dt 4.7 A/us)

### Zener clamp example (§4.1.8)
- RIN = (100 - 13.5 - 0.8)/25 mA = 3.4 k -> 3k3; leakage budget 0.75 uA vs 0.56 uA at 50 C; ~30 pF -> 400 kHz

### BJT / JFET / MOSFET numbers (§4.3–4.5)
- BC848 hFE 110–800; grades A 110–220, B 200–450, C 420–800; gain falls 2–3x cold
- VCEsat residual 50–200 mV; base drive > IC/10 pointless; Darlington VCEsat ~1 V; reverse VBE breakdown 7–10 V
- Switching transistor ton < 50 ns, toff 100–200 ns
- JFET VGS(off) spread up to 6:1; gate leakage x20 at 70 C, x1000 at 125 C; IG breakpoint at 1/3–1/2 of VDG breakdown; current-regulator diodes 0.2–5 mA
- 74HC (4 mA) into 200 pF to 3 V: 150 ns; t = Qg/Ig (20 nC: 20 us @1 mA, 20 ns @1 A)
- CGD:CGS ~ 1:6 -> 300 V drain spike -> ~50 V gate
- 20 A across 0.5 uH in 50 ns -> 200 V
- RDSon at Tj_max = 1.8–2 x RDSon(25 C); I_allowed ~ 0.7 x
- Low-power MOSFET gate breakdown +/-15 to +/-40 V; ~100 pC destroys
- IGBT preferred > 1000 V; MOSFET < 250 V; IGBT current density up to 20x MOSFET, 5x bipolar

### Table 5.1 Op-amp application categories — p.192
| Category | GBW (MHz) | Slew rate (V/us) | VOS (mV) | ICC (mA) | VOS drift (uV/C) | Noise (nV/rtHz) | Gain/phase error (%) |
|---|---|---|---|---|---|---|---|
| General purpose | 1–30 | 0.5–40 | 0.5–20 | – | – | – | – |
| Low power | 0.05–5 | 0.03–3 | 0.5–20 | 0.015–1 | – | – | – |
| Precision | – | 0.3–10 | 0.06–0.5 | – | 0.5–4 | 3–30 | – |
| High speed and video | 30–1000 | 100–5000 | 1–25 | 3–15 | – | – | 0.01–0.3 |

### Op-amp numeric anchors (§5.2)
| Item | Value | Source |
|---|---|---|
| Precision op-amp definition | VOS < 200 uV, tc < 2 uV/C | p.192 |
| VOS drift, standard | 5–40 uV/C (typ 10); bipolar 3.3 uV/C per mV VOS; LinCMOS 1–2 uV/C | p.194-195 |
| Bias current | bipolar < 0.5 uA (std), < 20 nA (precision); FET pA–tens pA at 25 C junction, x2 per 10 C | p.195-196 |
| IOS*RS = VOS break-even | 741: 33 kohm (1 mV, 30 nA); TL081: 1000 Mohm (5 mV, 5 pA) | p.196 |
| CMRR/PSRR 80 dB | 100 uV per 1 V | p.197-198 |
| PSRR at 10s–100s kHz | 20–30 dB | p.198 |
| Output swing (bipolar/BiFET) | >= 2 V from rails; I_out ~ +/-10 mA | p.199-200 |
| Slew rate 741 | 20 uA / 30 pF = 0.67 V/us; f_max = SR/(2*pi*Vp) | p.202 |
| GBW | LM324 1 MHz; recent 5–30 MHz; > 30 MHz = high speed | p.203 |
| PSU decoupling resonance | 0.01–0.1 uF + lead L -> 1–10 MHz; use 1–10 uF tantalum | p.205 |
| Coax load | 10 m RG58C/U ~ 1000 pF | p.206 |
| Input stray C | 3–5 pF | p.206 |
| AOL | >= 80 dB, usually 100–120 dB; halves cold->hot; ACL = AOL/(1+AOL*beta) | p.207-208 |
| Thermal noise | 4 nV/rtHz per 1 kohm at 298 K; pk-pk = 6.6x (0.1%) or 5x (1%) RMS | p.211 |
| Noise bandwidth single pole | 1.57 fc | p.215 |
| Op-amp noise at 1 kHz | OP27 3 nV/rtHz, 0.4 pA/rtHz; TL071 18 nV, 0.01 pA; LMV324 39 nV, 0.21 pA | p.213 |
| Supply dissipation | +/-15 V x 10 mA = 300 mW; theta 100–150 C/W -> 30–45 C rise | p.217 |
| Temperature grades | commercial 0..70; industrial -40..85 (-25..85); military -55..125; automotive -40..125 | p.218 |
| SPICE model accuracy | ~+/-20% (typical-value models) | p.234 |

### Op-amp noise model output contributions (Fig 5.17, per rtHz, multiply by sqrt(B))
| Cause | Contribution |
|---|---|
| RIN thermal | sqrt(4kT*RIN) * AV |
| R1 thermal | sqrt(4kT*R1) * (AV+1) |
| RF thermal | sqrt(4kT*RF) |
| in- | in- * RF |
| in+ | in+ * R1 * (AV+1) |
| en | en * (AV+1) |
| Total | sqrt(sum of squares) |

Low-Z example (RIN 200, R1 180, RF 2 k): OP27 / TL071 / LMV324 -> N(RIN) 17.9 each; N(R1) 18.7 each; N(RF) (5.6); N(in-) (0.8)/(0.02)/(0.42); N(in+) (0.79)/(0.02)/(0.46); N(en) 33/198/429; total 41.9 / 200 / 430 nV/rtHz.
High-Z example (200 k, 180 k, 2 M): N(RIN) 565; N(R1) 590; N(RF) 178; N(in-) 800/(20)/420; N(in+) 792/(19.8)/460; N(en) (33)/198/429; total 1402 / 836 / 1127 nV/rtHz.

### Table 5.2 Some 1.2 V voltage references — p.232
| Type | Vout | Tolerance | Tempco | Min current | Cost GBP (25 off) |
|---|---|---|---|---|---|
| MAX6520EUR-T | 1.2 V | +/-1% | 20 ppm/C typ | 50 uA | 1.29 |
| LM4041B-1.2 | 1.225 V | +/-0.2% | 100 ppm/C | 45 uA | 0.97 |
| ICL8069DCZR | 1.23 V | +/-1.6% | 100 ppm/C | 50 uA | 0.78 |
| ICL8069CCZR | 1.23 V | +/-1.6% | 50 ppm/C | 50 uA | 1.27 |
| LM385Z-1.2 | 1.235 V | +/-2% | 20 ppm/C avg | 10 uA | 0.30 |
| LM385Z-1.2 | 1.235 V | +/-1% | 20 ppm/C avg | 10 uA | 0.55 |
| LT1004CZ-1.2 | 1.235 V | +/-4 mV | 20 ppm/C | 10 uA | 1.68 |
| ZRA124A01 | 1.24 V | +/-1% | 30 ppm/C | 50 uA | 0.67 |
| ZRA125F02 | 1.25 V | +/-2% | 30 ppm/C | 50 uA | 0.55 |
(Current column printed "mA"; context (band-gap minimum currents 10–100 uA) indicates uA.) Buried-zener references: 50 ppm/year, 0.1%, +/-10 ppm/C.

### Hysteresis formulas (Fig 5.27, open-collector comparator with pull-up R3)
- Vout(H) = Vcc - (Vcc - Vref)*R3/(R1+R2+R3); Vout(L) = Vsat
- Vth_h = a*Vcc + (1 - a)*Vref [printed "(1 + a)"], a = R1/(R1+R2+R3); dVth_h = a*(Vcc + Vref) [as printed]
- Vth_l = b*Vsat + (1 - b)*Vref, b = R1/(R1+R2); dVth_l = b*(Vsat - Vref)
- Simplified (R3 << R1+R2, Vref = Vcc/2, Vsat = 0): total hysteresis band = b*Vcc
- Comparator source impedance: 2 pF stray x 10 kohm -> 8 MHz pole; keep < 10 kohm

### Logic / interface numbers (Ch.6)
| Item | Value | Source |
|---|---|---|
| HCMOS driven by LS-TTL noise immunity | 2.4 V high, 0.47 V low (worst case) | p.239 |
| LS-TTL VOH vs HCMOS VIH | 2.7 V < 3.15 V (negative margin) | p.239 |
| 74LVT thresholds | VIH 2.0 V, VIL 0.8 V | p.240 |
| Logic input capacitance | 5–10 pF + ~5 pF interconnect | p.241 |
| 74HC dynamic drive | +/-40 mA std, +/-60 mA buffers at 4.5 V | p.241 |
| Slew example | 100 pF, 0 -> 3 V, 40 mA: 7.5 ns | p.241 |
| 74AC edge | ~1.6 V/ns; 30 pF -> 50 mA | p.242 |
| Ground bounce | 50 mA/ns x 20 nH (1 inch) = 1 V | p.243 |
| Decoupling distance | < 0.5 inch (74AC/ECL); several inches (4000B) | p.244 |
| Decoupling value | C = I*t/V: 0.4 A x 6 ns / 0.4 V = 6 nF; use 10–100 nF, 22 nF | p.244 |
| LF decoupling | 1–2 uF tantalum distributed; 10–47 uF at entry | p.245 |
| Guideline counts | 22 uF/board; 1 uF per 10 SSI/MSI; 1 uF per 2–3 LSI; 10–100 nF per LSI supply pin; per octal/MSI; per 4 SSI | p.245-246 |
| Ground switching noise | tens to hundreds of mV peak | p.247 |
| Plain gate needs slew | > 5 V/us | p.249 |
| Contact bounce | ~1 ms | p.250 |
| Opto speeds | standard 2–5 us (~100 kbit/s); 10 Mbit/s > GBP 5 | p.253 |
| Opto CTR | 10–80% (Darlington 200–500%, 100 us off); EOL margin 20–50% | p.253 |
| Opto coupling C | 0.5–2 pF; CMTI < 100 V/us to > 5 kV/us | p.254 |
| Audio real-time example | 23 us / 30 ns = 766 instructions | p.265 |
| Aliasing example | 40 or 48 kHz at 44 ks/s -> 4 kHz | p.267 |
| PWM example | 10 MHz / 2^16 = 152 Hz | p.268 |
| Wake-up example | 100 ohm x 100 nF = 10 us; 5.5 tau = 55 us for 8-bit | p.269 |
| Micro rail spec | 3.0–3.6 V or 4.75–5.25 V | p.270 |
| Watchdog timeout | 10 ms – 1 s | p.271 |
| RC POR weakness | misses dips of a few ms | p.275 |
| CMOS RAM input limit | VCC + 0.3 V | p.277 |
| FPGA threshold | ~100 MHz clocks; ~60% utilisation headroom | p.280 |

### Table 6.1 ADC resolution voltage, 10 V full scale — p.247
| Word length | Resolution voltage |
|---|---|
| 8 bit | 39 mV |
| 10 bit | 10 mV |
| 12 bit | 2.4 mV |
| 14 bit | 0.6 mV |
| 16 bit | 0.15 mV |

### Table 6.2 EIA-232F / EIA-422 / EIA-485 — p.255
| Parameter | EIA-232F | EIA-422 | EIA-485 |
|---|---|---|---|
| Line type | Unbalanced, point to point | Balanced differential, multidrop (one driver per bus) | Balanced differential, multiple drivers (half duplex) |
| Line impedance | N/A | 100 ohm | 120 ohm |
| Max line length | load dependent, typ 15 m (capacitance) | L ~ 1e5/B m, B = bit rate kb/s | max recommended 1200 m (attenuation) |
| Max data rate | 20 kb/s | 10 Mb/s | 10 Mb/s |
| Driver output voltage | +/-5 to +/-15 V loaded 3–7 kohm; +V = logic 0, -V = logic 1 | +/-10 V max diff unloaded; +/-2 V min into 100 ohm | +/-6 V max diff unloaded; +/-1.5 V min into 54 ohm |
| Driver short-circuit current | 500 mA max | 150 mA max | 150 mA to gnd, 250 mA to -7 or +12 V |
| Driver rise time | 4% of unit interval (1 ms max); 30 V/us max slew | 10% of unit interval (min 20 ns) | 30% of unit interval |
| Driver output, power off | > 300 ohm | +/-100 uA max leakage | > 12 kohm |
| Receiver sensitivity | +/-3 V max thresholds | +/-200 mV | +/-200 mV |
| Receiver input impedance | 3–7 kohm, < 2500 pF | 4 kohm min | 12 kohm |
| Receiver common-mode range | N/A | +/-7 V | +12 to -7 V |
EIA-422: one driver, up to 10 receivers, one 100 ohm termination at the far end; 4000 ft at 100 kbaud. EIA-485: 32 unit loads (UL = 1 mA at +12 V / 0.8 mA at -7 V), 120 ohm at both ends, failsafe > 200 mV.

### CAN / USB / Ethernet numbers (§6.2.6)
- CAN: 1 Mb/s; 120 ohm each end; 40 m, 30 nodes, stub 0.3 m; recessive 2.5 V; dominant CANH +1 V / CANL -1 V; CM -2..+7 V; 2.0A 11-bit, 2.0B 29-bit ID; ISO 11519 125 kb/s
- USB: Rx >= 200 mV over CM 0.8–2.5 V; Tx low < 0.3 V (1.5 k to 3.6 V), high > 2.8 V (15 k to gnd); Z0 90 ohm +/-15%; delay <= 26 ns; driver 28–44 ohm; 12 / 1.5 Mb/s; USB 2.0 480 Mb/s with 45 ohm terminations; USB 3.0 5 Gbit/s
- Ethernet: 10BaseT 2.5 V pk diff; 100BaseT 1 V pk diff into 100 ohm; PCIe 2.0 5 GT/s, 3.0 8 GT/s

### ADC formulas (§6.9)
- q = VFS/(2^N - 1); e_rms = q/sqrt(12); SQNR = (3/2)*2^(2N) = 6.02N + 1.76 dB (16-bit: 98 dB)
- OSR = fs/(2*fm); in-band noise power = e_rms^2/OSR; PSD = 2*e_rms^2/fs
- 8-bit/10 V example: q = 39.21 mV; 6.2 V -> 6.210938 V (+10.938 mV, 0.176% of input, 0.109% FS)

### ADC architecture / sigma-delta (§6.10)
- Oversampled SQNR = 6.02N + 1.76 + 10*log10(OSR) dB; x2 OSR = +3 dB
- Flash: 2^N - 1 comparators, 2^N resistors, 1 clock, practical <= 8 bits
- SAR: N cycles; dual slope: up to 14 bits, R/C independent, slow
- 2nd-order sigma-delta noise: n0 = e_rms * pi^2/sqrt(5) * OSR^(-5/2) (printed form)

### Power-supply design numbers (Ch.7)
| Item | Value | Source |
|---|---|---|
| SMPS switching frequency | 30–300 kHz typical | p.296 |
| Off-the-shelf PSU cost | ~GBP 1/W (50–200 W) | p.297 |
| Mains voltage | 230 V (EU/UK), 115 V (US); +/-10% or +10/-15% -> 207–253 V or 195–253 V; UK +/-6% at connection | p.297-298 |
| Fuse coordination | fault : max operating current >= 2:1 | p.298 |
| IEC 60127 rated current | ~60% of minimum fusing current | p.299 |
| UL 198G rated current | 85–90% of minimum fusing current | p.299 |
| Fuse classes | FF, F, M, T, TT; prefer F or T | p.299-300 |
| Non-opening pulse | I^2t <= 50–80% of fuse I^2t | p.300 |
| Arc time significant | > ~10x rated current | p.300 |
| HBC / LBC breaking capacity | thousands of A / a few tens of A | p.300 |
| Toroid switch-on surge | > 10x operating current | p.300 |
| T/TT fuse | 10–20x for ms; ruptures ~2x sustained 10–100 s | p.301 |
| NTC limiter | 1–2 s to heat; tens of s to cool | p.301 |
| Sine RMS/average | 1.11 | p.302 |
| EN 61000-3-2:2000 | to 40th harmonic (2 kHz); <= 16 A; non-lighting < 75 W exempt | p.303 |
| Peaky-input PF | 0.5–0.75 | p.303 |
| PFC switching frequency | 50–100 kHz typ | p.303 |
| Mains frequency | 50 Hz +/-1%; 60 Hz ripple = 83% of 50 Hz | p.304 |
| Efficiency | linear rarely > 50%; SMPS > 70%, up to 90% | p.305 |
| Rectifier efficiency factor | 0.92 (full wave, single C) | p.306 |
| 7805 example | Vin_dc 7.45 V; Vtx 10.83 V rms; 264 V line -> 12.5 V avg, 1.5x load power lost | p.306-307 |
| Transformer regulation | can exceed 20% | p.307 |
| Reservoir t | ~8 ms (50 Hz FW), 6 ms (60 Hz FW) as printed; tolerance +/-20% | p.308 |
| Ripple current | RMS 2–3x DC load; example 2 A, 3 V, 100 Hz -> 5300 uF; need 4–6 A | p.308-309 |
| Rectifier current rating | >= I_DC, preferably 2x; off-line SMPS up to 5x | p.309 |
| 1N5400 | 3 A average, IFSM 200 A | p.309 |
| PIV | bridge >= V_pk, CT >= 2 V_pk, +50–100%; 240 V: >= 600 V, pref. 800 V | p.309 |
| Linear ripple rejection | 70–80 dB; < 1 mV rms | p.311 |
| SMPS ripple & noise | ~1% of rail ("100–200 mV"); measure >= 10 MHz BW | p.311 |
| Reservoir peak current | ~5x DC; 10 mohm -> 50 mV | p.311 |
| 78XX capacitors | 0.1 uF out; 0.33–1 uF in | p.312 |
| Transient recovery | SMPS ms; linear tens of us | p.313 |
| Foldback limit | [IK/ISC]max = 1 + Vout/VBE(on); practical <= 2–3 | p.314 |
| Mains dips/outages | up to 500 ms common; UK avg 90 min/year lost | p.314-315 |
| Hold-up example | 5000 uF, 1 A: 13 ms at 240 V; 2.5 ms at 204 V | p.315-316 |
| OVP zener for 5 V | 6.2 or 6.8 V | p.317 |
| PSU packaging | open frame 10–100 W (to 250 W); enclosed > 100 W; encapsulated <= 40 W; rack 25–500 W | p.320 |

### Linear PSU formulas (§7.2.8–7.3.2)
- Vin_dc(min) = Vout(min) + Vtol_reg + Vdropout + Vsense
- Vtx(rms) = (Vin_dc + Vripple + VD)/0.92 * (Vac_nom/Vac_min) / sqrt(2)
- Transformer regulation = (Vsec_unloaded - Vsec_loaded)/Vsec_loaded
- C_res = IL * t / Vripple
- Hold-up t_h = (V_trough - V_in_min) * C / I (linear); stored energy 0.5*C*V^2
- Rectifier surge: I_pk = Vmax/Rs, tau = C*Rs < T/2 and I_pk < IFSM
- Foldback: [IK/ISC]max = 1 + Vout/VBE(on)
- Efficiency eta = Pout/(Pout + Ploss); heat = Pout*(1/eta - 1)
- Series-pass peak dissipation current (derived): I = (V_nl - Vout)/(2*Rs)

### Battery chemistries (§7.5)
| Chemistry | Nominal V/cell | OCV | End V | Temp range | Other |
|---|---|---|---|---|---|
| Alkaline MnO2 | 1.5 | – | 0.8 (<= 6 cells), 0.9 (more) | -30 to +80 C | operating 1.3–0.8 V; 85% after 3 yr at 20 C |
| Silver oxide | 1.5 (table 1.55) | – | gradual decay | good low temp | 2 yr shelf life |
| Zinc–air | – | 1.45 | output 1.3–1.1 V | narrow | use within 2 months of unsealing |
| Lithium MnO2 | 3 | – | op. 2.5–3.5 V | wide | pulses to 30 A; cylindrical to 1.5 Ah |
| Sealed lead–acid | 2 | 2.15 | 1.75 | -30 to +50 C (60% cap. cold) | 1–100 Ah; C @ 20 h; 3%/month self-discharge; float life 4–5 yr (to 15) |
| NiCd | 1.2 | 1.35–1.4 | 1.0 | -40 to +50 C | 0.15–7 Ah; C @ 5 h; memory effect |
| NiMH | 1.2 | 1.35–1.4 | 1.0 | -20 to +50 C | +20% weight, +40% capacity vs NiCd |
| Li-ion | 3.6–3.7 | – | 3.0 | – | pack protection mandatory |
Battery OCV can exceed on-load voltage by up to 15%; 15 Ah lead-acid at 1C lasts ~20 min; lead-acid cycle life at 100% DoD ~15% of that at 30% DoD.

### Charging (§7.5.4)
| Chemistry | Method | Values |
|---|---|---|
| Lead–acid | current-limited constant voltage | I0 0.1–0.25 C; 2.25–2.5 V/cell; -4 mV/C/cell; switch to float at ~0.05 C; CC alternative 0.05–0.2 C with voltage monitor |
| NiCd | constant current | 0.1 C continuous (16 h full charge); <= 0.3 C long periods; rapid only with termination; up to 1.55 V/cell |
| NiMH | constant current | trickle <= C/250 |
| Li-ion | CC/CV + protection in pack | – |

### Table 7.1 Sizes of popular primary batteries — p.324
| Chemistry | IEC | ANSI | Size | Voltage (V) | Dia or L x W (mm) | Height (mm) |
|---|---|---|---|---|---|---|
| Alkaline MnO2 | LR03 | 24A | AAA | 1.5 | 10.5 | 44.5 |
| Alkaline MnO2 | LR6 | 15A | AA | 1.5 | 14.5 | 50.5 |
| Alkaline MnO2 | LR14 | 14A | C | 1.5 | 26.2 | 50 |
| Alkaline MnO2 | LR20 | 13A | D | 1.5 | 34.2 | 61.5 |
| Alkaline MnO2 | 6LR61 | 1604A | PP3 | 9 | 26.5 x 17.5 | 48.5 |
| Alkaline MnO2 | 4LR25X | 908A | Lamp | 6 | 67 x 67 | 115 |
| Alkaline MnO2 | 4LR25-2 | 918A | Lamp | 6 | 136.5 x 73 | 127 |
| Li MnO2 cylindrical | CR17345 | 5018LC | 2/3A | 3 | 17 | 34.5 |
| Li MnO2 cylindrical | CR11108 | 5008LC | 1/3N | 3 | 11.6 | 10.8 |
| Li MnO2 cylindrical | 2CR11108 | 1406LC | 2 x 1/3N | 6 | printed "25.2" | printed "13" (column order likely swapped: 13 dia x 25.2 high) |
| Li MnO2 cylindrical | 2CR5 | 5032LC | 2 x 2/3A | 6 | 17 x 34 | 45 |
| Li MnO2 cylindrical | CR-P2 | 5024LC | 2 x 2/3A | 6 | 19.5 x 35 | 36 |
| Li MnO2 coin | CR2016 | 5000LC | – | 3 | 20 | 1.6 |
| Li MnO2 coin | CR2025 | 5003LC | – | 3 | 20 | 2.5 |
| Li MnO2 coin | CR2032 | 5004LC | – | 3 | 20 | 3.2 |
| Li MnO2 coin | CR2430 | 5011LC | – | 3 | 24.5 | 3 |
| Li MnO2 coin | CR2450 | 5029LC | – | 3 | 24.5 | 5 |
| Silver oxide (42 mAh) | SR41 | 1135SO | – | 1.55 | 7.87 | 3.6 |
| Silver oxide (120 mAh) | SR43 | 1133SO | – | 1.55 | 11.56 | 4.19 |
| Silver oxide (165 mAh) | SR44 | 1131SO | – | 1.55 | 11.56 | 5.58 |
| Silver oxide (70 mAh) | SR48 | 1137SO | – | 1.55 | 7.87 | 5.38 |
| Silver oxide (70 mAh) | SR54 | 1138SO | – | 1.55 | 11.56 | 3.05 |
| Silver oxide (40 mAh) | SR55 | 1160SO | – | 1.55 | 11.56 | 2.21 |
| Silver oxide (55 mAh) | SR57 | 1165SO | – | 1.55 | 9.5 | 2.69 |
| Silver oxide (30 mAh) | SR59 | 1163SO | – | 1.55 | 7.9 | 2.64 |
| Silver oxide (18 mAh) | SR60 | 1175SO | – | 1.55 | 6.8 | 2.15 |
| Silver oxide (25 mAh) | SR66 | 1176SO | – | 1.55 | 6.78 | 2.64 |

### EMC field and coupling formulas (§8.1, §8.3)
- Far field of a transmitter: E = sqrt(30*P)/d V/m (P radiated W incl. antenna gain; d in m; valid d > lambda/(2*pi))
- Magnetic coupling: V = 2*pi*f*Is*M (M = 0.1–3 uH for short lengths in one loom)
- Capacitive coupling: V = 2*pi*f*Vs*C*Z (C = 1–100 pF typical)
- Small loop far field: E = 131.6e-16 * f^2 * A * I / d V/m (A in m^2)
- Short monopole over ground plane: E = 4*pi*1e-7 * f * L * I / d V/m (L in m)
- Far field E/H = 377 ohm; near field loop: H ~ 1/d^3, E ~ 1/d^2; rod: E ~ 1/d^3, H ~ 1/d^2; lambda/4 = 1 m at 75 MHz
- Mains RF impedance (CISPR 16 LISN): 50 ohm in parallel with 50 uH to earth; power cables low-loss lines to ~10 MHz
- Clock rise-time: 5 MHz clock, 8 ns vs 1 ns edges -> ~20 dB less at ~200 MHz; clock series R of a few tens of ohms

### RF threat levels (§8.1.1)
| Source | Level |
|---|---|
| AM broadcast (100–500 kW) | 1–10 V/m occasionally |
| TV/FM (~10 kW) near buildings | > 10 V/m possible (upper floors) |
| 1 W UHF hand-held at 0.5 m | 5–7 V/m |
| 1–10 GHz radar (airports) | pulsed 50 V/m up to 3 km |
| Civil aircraft worst case (2–4 GHz radars, EUROCAE WG33) | 17 kV/m |
| Design criterion | >= 3 V/m (10 V/m preferred), 10 MHz–1 GHz |

### Table 8.2 Average rate of occurrence of mains transients (> 100 V, ZVEI survey) — p.336
| Area class | Transients per hour |
|---|---|
| Industrial | 17.5 |
| Business | 2.8 |
| Domestic | 0.6 |
| Laboratory | 2.3 |
Number ~ 1/V_peak^3; rise rate ~ sqrt(V_peak): ~3 V/ns at 200 V, ~10 V/ns at 2 kV. Immunity targets: >= 2 kV (1–2 kV occasional upsets; < 1 kV unacceptable); 4–6 kV high reliability. ESD human body: 150 pF + 150 ohm.

### Table 8.3 Most common EMC standards — p.342
| Product sector | Emission EN | CISPR | FCC | Immunity EN | IEC/CISPR | Immunity scope |
|---|---|---|---|---|---|---|
| Industrial, scientific & medical | EN 55011 | 11 | Part 18 | – | – | – |
| Household appliances | EN 55014-1 | 14-1 | – | EN 55014-2 | CISPR 14-2 | RFI, ESD & transient |
| Lighting equipment | EN 55015 | 15 | – | EN 61547 | IEC 61547 | RFI, ESD & transient |
| Radio & TV receivers | EN 55013 | 13 | – | EN 55020 | CISPR 20 | RFI, ESD & transient, antenna terminals |
| Information technology equipment | EN 55022 | 22 | Part 15 | EN 55024 | CISPR 24 | RFI, ESD & transient |
Limits: Figs 8.4 (conducted) and 8.5 (radiated, normalised to 10 m) are graphs — "consult current specifications to confirm limit values".

### Table 8.4 CISPR 16-1 quasi-peak measuring receiver — p.344
| Parameter | 9–150 kHz | 0.15–30 MHz | 30–1000 MHz |
|---|---|---|---|
| Bandwidth | 200 Hz | 9 kHz | 120 kHz |
| Charge time | 45 ms | 1 ms | 1 ms |
| Discharge time | 500 ms | 160 ms | 550 ms |
| Overload factor | 24 dB | 30 dB | 43.5 dB |

### Shielding (§8.5, Fig 8.11/8.12)
| Quantity | Formula / value |
|---|---|
| Total | SE = R + A + B (B negligible if A > 10 dB) |
| Reflection, E field | R = 322 - 10*log10((mu_r/sigma_r) * r^2 * f^3) dB |
| Reflection, H field | R = 15 - 10*log10((mu_r/sigma_r) / (r^2 * f)) dB |
| Reflection, plane wave | R = 168 - 10*log10((mu_r/sigma_r) * f) dB |
| Absorption | A = 0.1314 * t_mm * sqrt(mu_r * sigma_r * f) dB |
| Skin depth | delta = 6.61 * (mu_r * sigma_r * F)^-0.5 cm; 8.7 dB per delta; Cu at 30 MHz 0.012 mm |
| Aluminium foil | 0.05 mm, sigma_r 0.61, mu_r 1 |
| Sheet steel | 0.5 mm, sigma_r 0.1, mu_r 60 at 10 kHz -> 1 above 1 MHz |
| Aperture cut-off | no shielding for lambda <= 2d; below, +20 dB/decade (SE ~ 20log(lambda/2d), derived) |
| Max hole for 20 dB to 1 GHz | 1.6 cm |
| Hole arrays (< lambda/2 spacing) | SE worse by ~sqrt(N): 100 x 4 mm holes = 20 dB worse than one |
| Seam fastener spacing | <= lambda/20 at highest frequency |
| SE grades | < 20 dB minimal; 20–80 average; 80–120 above average; > 120 not cost-effective |
| Pigtail vs 360-degree shield bond | ~same < 3 MHz; up to ~40 dB worse above; > 20 dB swings |
| Earth strap | length/width < 3:1 |

### Filters (§8.6)
| Item | Value |
|---|---|
| Series L / ferrite bead | > 40 dB in low-Z circuits; useless at high Z |
| Discrete filter useful range | up to ~10 MHz |
| Mains CM choke | 1–10 mH |
| CX (line-line) | 0.1–0.47 uF |
| CY limit | earth leakage 0.25–5 mA per class/application; BS 613: <= 0.005 uF (class I, plug-connected) |
| Mains filter block cost | ~GBP 5 |
| Input peak current | >= 3x RMS (crest factor) — check saturation |
| 3-terminal capacitor | effective range < 50 MHz (2-terminal) -> > 200 MHz |
| Feedthrough capacitors | to GHz; solder-in 100–1000 pF tens of pence; screw-mount GBP 1–2 |
| Isolated-circuit filter C | a few tens of pF max |

### Table 9.1 Safety hazards — p.369
| Hazard | Main risk | Source |
|---|---|---|
| Electric shock | Electrocution, injury from muscular contraction, burns | Accessible live parts |
| Heat or flammable gases | Fire, burns | Hot components, heatsinks, damaged/overloaded components and wiring |
| Toxic gases or fumes | Poisoning | Damaged or overloaded components and wiring |
| Moving parts, mechanical instability | Physical injury | Motors, parts with inadequate mechanical strength, heavy or sharp parts |
| Implosion/explosion | Injury from flying glass/fragments | CRTs, vacuum tubes, overloaded capacitors and batteries |
| Ionizing radiation | Radiation exposure | High-voltage CRTs, radioactive sources |
| Non-ionizing radiation | RF burns, possible chronic effects | Power RF circuits, transmitters, antennas |
| Laser radiation | Eyesight damage, burns | Lasers |
| Acoustic radiation | Hearing damage | Loudspeakers, ultrasonic transducers |

### Safety numbers (§9.1)
| Item | Value | Source |
|---|---|---|
| LVD scope | 50–1000 V AC, 75–1500 V DC | p.368 |
| Harmless / possibly fatal AC body current | < 0.5 mA / > 50–500 mA (duration dependent) | p.369 |
| SELV | < 50 V AC rms, isolated from mains | p.370 |
| Creepage/clearance EN 60065 | 0.5 mm below 34 V -> 3 mm at 354 V (extrapolate) | p.371 |
| PCB conductors EN 60065 | 0.5 mm up to 124 V -> 3 mm at 1240 V | p.371 |
| Earth continuity EN 60065 | < 0.5 ohm at 10 A for 1 minute | p.22 |
| Benign-environment PCB spacing | 1 mm per 200 V | p.57 |
| ESD mats / wrist strap | 1 Mohm to ground | p.375-376 |
| ESD risk vs RH | > 65% low; < 20% high | p.375 |
(The book prints no IEC 60950/62368/61010 creepage/clearance tables — only the EN 60065 anchor values above.)

### Safety classes (IEC 60536) — p.370
| Class | Protection |
|---|---|
| 0 | Basic insulation only, no earth provision (unacceptable in UK) |
| I | Basic insulation + all accessible conductive parts bonded to protective earth |
| II | Double or reinforced insulation, no protective earth |
| III | Supplied at SELV, no higher voltage generated |

### Testability numbers (§9.3)
| Item | Value |
|---|---|
| Test pad (SM, Ch.2) | <= 1 mm dia, no component connection, opposite side |
| Bed-of-nails target grid | 0.1 inch (2.5 mm); down to 0.05 inch / 1 mm |
| JTAG TAP pins | TCK, TDI, TDO, TMS |
| Structured test threshold | < 10 K gates no; 10–20 K consider; > 20 K yes |

### Reliability formulas (§9.4, §2.3.4)
- Reliability R = P(no failure over specified period, specified conditions)
- MTBF = 1/lambda (e.g. 10 000 h = 1e-4 /h = 100 per 1e6 h)
- Availability A = U/(U + D) = MTBF/(MTBF + MTTR)
- Arrhenius lambda = K*exp(-E/(kT)); E ~ 0.5 eV -> x2 per 10 C; accelerator A_t = exp((ea/k)(1/Tref - 1/Top)), k = 8.6e-5 eV/K
- Capacitor voltage: lambda ~ V^5 (half voltage -> /32)
- Series model lambda_assy = sum(lambda_i); redundancy P_fail = product(P_i)
- Burn-in example 160 h at 125 C; fault-cost x10 per production stage

### Table 9.2 Thermal and electrical equivalences — p.390
| Thermal parameter | Units | Electrical analog | Units |
|---|---|---|---|
| Temperature difference | C | Potential difference | V |
| Thermal resistance | C/W | Resistance | ohm |
| Heat flow | J/s (W) | Current | A |
| Heat capacity | J/C | Capacitance | F |

### Table 9.3 Thermal properties of common metals — p.393
| Metal | Finish | Heat capacity (J/cm^3/C) | Bulk thermal conductivity (W/C/m) | Surface emissivity |
|---|---|---|---|---|
| Aluminium | Polished | 2.47 | 210 | 0.04 |
| Aluminium | Unfinished | 2.47 | 210 | 0.06 |
| Aluminium | Painted | 2.47 | 210 | 0.9 |
| Aluminium | Matt anodized | 2.47 | 210 | 0.8 |
| Copper | Polished | 3.5 | 380 | 0.03 |
| Copper | Machined | 3.5 | 380 | 0.07 |
| Copper | Black oxidized | 3.5 | 380 | 0.78 |
| Steel | Plain | 3.8 | 40–60 | 0.5 |
| Steel | Painted | 3.8 | 40–60 | 0.8 |
| Zinc | Gray oxidized | 2.78 | 113 | 0.23–0.28 |

### Table 9.4 Free-air cooling efficiency vs altitude — p.395
| Altitude | Sea level | 2000 ft | 5000 ft | 10 000 ft | 20 000 ft |
|---|---|---|---|---|---|
| Efficiency | 100% | 97% | 90% | 80% | 63% |

### Table 9.5 Interface thermal resistances Rth_c-h (C/W) — p.399 (column mapping reconstructed from flattened print; conf medium)
| Package | Metal-metal dry | Metal-metal greased | 2-mil mica dry | 2-mil mica greased | 2-mil polyimide dry | 2-mil polyimide greased | 6-mil silicone rubber |
|---|---|---|---|---|---|---|---|
| TO204AA (TO3), metal flanged | 0.5 | 0.1 | 1.2 | 0.5 | 1.5 | 0.55 | 0.4–0.6 |
| TO213AA (TO66), metal flanged | 1.5 | 0.5 | 2.3 | 0.9 | – | – | – |
| TO126, plastic | 2.0 | 1.3 | 4.3 | 3.3 | – | – | 4.8 |
| TO220AB, plastic | 1.2 | 0.6 | 3.4 | 1.6 | 4.5 | 2.2 | 1.8 |
Minimum clamping force 20 N.

### Thermal formulas (§9.5)
- T = PD*Rth + TA; Tj = PD*(Rth_j-c + Rth_c-h + Rth_h-a) + TA (Rth_c-a in parallel)
- IRF640 example: 35 W, 0.5 + 0.8 + 1.0 C/W, 70 C -> 150.5 C (148.25 C with Rth_j-a 80 C/W in parallel); rated 125 W only at 25 C case
- tau = Rth*Ch; 1 C/W Al heatsink ~120 cm^3 -> 296 J/C -> ~296 s
- Pulsed: Tj = PDmax*[K*Rth_j-c + d*(Rth_c-h + Rth_h-a)] + TA; K -> d above a few kHz with d > 20%
- Heatsink performance ~ width (across flow) x sqrt(fin length); horizontal fins -30%; Rth(10 C rise) ~ 1.25 x Rth(20 C rise); black anodise 10–15x polished radiative efficiency
- Enclosure fan: flow = 3600*PD/(rho*c*theta) m^3/h; air at 30 C rho 1.3 kg/m^3, c ~1000 J/kg/C; 1 CFM = 1.7 m^3/h
- Radiation (printed): Q = 5.7e-12 * dT^4 * eps W/cm^2
- Mounting: surface finish 50–60 microinch; flatness < 0.004 in/in; lead bend >= 4 mm from body, radius >= 2 mm, <= 90 deg

## 3. Mechanizable checks

Convention: margin = (limit - value)/limit for upper limits, (value - limit)/limit for lower limits; negative margin = fail. Thresholds marked (conf low) are screening choices where the book gives a qualitative condition only.

### Grounding, wiring, cables
- `CHECK-shared-return-drop`: inputs rail V_nom (V), rail minimum V_min (V), each shared feed/return conductor R (ohm, corrected R(T) = R20*(1 + 0.00393*(T - 20))), currents sharing it I_k (A) → Vs = R*sum(I_k) for feed + return → pass V_nom - Vs_feed - Vs_return >= V_min → margin (V_nom - Vs_total - V_min)/V_nom; also flag any conductor shared by a switched (relay/lamp) load and a logic/analog supply → WILSON-006, 007, 028.
- `CHECK-wire-dynamic-drop`: inputs length l (cm), diameter d (cm), R per m (ohm/m), I (A), di/dt (A/s), budget V_b (V) → L[uH] = 0.002*l*(2.3*log10(4*l/d) - 1); V = L*1e-6*di/dt + R*(l/100)*I → pass V <= V_b → margin 1 - V/V_b → WILSON-008, 024, 025.
- `CHECK-ground-loop-pickup`: inputs loop area A (cm^2), turns n, field B_pk (uT), f (Hz), allowed pickup V_allow (V) → V_pk = 1e-8*A*n*2*pi*f*B_pk → pass V_pk <= V_allow → margin 1 - V_pk/V_allow → WILSON-004, 005.
- `CHECK-common-impedance-stability`: inputs forward gain A (signed, per frequency point), common impedance Rs (ohm), load RL (ohm) → loop = A*Rs/(RL + Rs) → pass loop > -1 at every frequency (inverting: abs(A)*Rs/(RL+Rs) < 1); warn if abs(loop) > 0.1 (response error > ~10%, conf low) → margin 1 - abs(loop) → WILSON-011.
- `CHECK-inter-unit-ground-noise`: inputs site class (bad: up to 50 V; common: several V; quiet: < 1 mV rms), interface type, CM range (V), isolation rating (V) → pass single-ended only if Vn << signal noise margin; differential if Vn <= CM range; else isolated with rating >= Vn; Class I equipment must never be floated → WILSON-010, 013, 016, 017.
- `CHECK-wire-ampacity`: inputs wire row (Table 1.2 / 1.3 / 1.5), I_rms (A), ambient T (C), insulation → I_allowed = I_table (25 C or 70 C column for BS 4808; Table 1.5 value x CF(T) for mains cable) → pass I <= I_allowed → margin 1 - I/I_allowed; fusing current (Table 1.2) must exceed fault-clearing current of upstream protection → WILSON-027, 029, 031.
- `CHECK-wire-voltage-drop`: inputs cable row, length L (m), I (A), T (C) → V = I*R_per_m*L*(1 + 0.00393*(T - 20)) (or mV/A/m from Table 1.5 x I x L) → pass V <= budget → WILSON-028, Tables 1.3/1.5.
- `CHECK-cable-crosstalk-lumped`: inputs C per m (pF/m), length (m), f (Hz), offender circuit impedance Z1 = Rsource//Rload (ohm), victim impedance Z2 (ohm), spec (dB) → Xc = 1/(2*pi*f*C*L); XT = Z2/(Z1 + Z2 + Xc); XT_dB = 20*log10(XT) → pass XT_dB <= spec → margin spec - XT_dB (dB) → WILSON-038, 040.
- `CHECK-edge-crosstalk`: inputs coupling C (F), offender dV/dt (V/s), edge duration t (s), loop resistance R (ohm), victim load R_par (ohm), victim noise margin NM (V) → I = C*dV/dt*(1 - exp(-t/(R*C))); V_pk = I*R_par → pass V_pk < NM → margin 1 - V_pk/NM → WILSON-039.
- `CHECK-tline-needed`: inputs length L (m), f_max (Hz) and/or rise time tr (s), er (or velocity factor) → lambda_d = 3e8/(f_max*sqrt(er)); t_transit = L*sqrt(er)/3e8 → flag transmission line if L > lambda_d/10 (lambda_d/40 for precision) or tr < 3*t_transit → then require source/load terminations = Z0 or proof that ringing stays inside noise immunity (sim) → WILSON-041, 042, 044, 045, 046.
- `CHECK-coax-Z0`: inputs D, d (same units), er, Z0 target, tolerance → Z0 = 60/sqrt(er)*ln(D/d) (other geometries Table 1.9) → pass abs(Z0 - target) <= tol → WILSON-051.
- `CHECK-reflection-swr`: inputs Z_load (ohm, resistive), Z0 → Gamma = (Z - Z0)/(Z + Z0); SWR = (1 + abs(Gamma))/(1 - abs(Gamma)) → pass SWR <= spec → WILSON-045, 048.
- `CHECK-shield-termination`: inputs per shielded cable: threat band (LF/HF), shield bonding (one end / both / 360-degree / pigtail), connector type → pass: HF shields bonded 360 degrees at both enclosures (no pigtail above ~3 MHz), LF input shields single-ended per source grounding rule, no shield used as signal return except coax at RF, no IDC connector on unfiltered external lines → WILSON-018, 019, 020, 358, 359.

### PCB fabrication and layout
- `CHECK-pcb-hv-spacing`: inputs per net pair: V_peak (V), spacing s (mm), environment (benign?), wave-soldered without resist (bool), mains-connected (bool) → s_min = V/200 mm (benign); s_min = max(s_min, 0.5 mm) if wave-soldered without resist; mains-connected -> CHECK-creepage-clearance → pass s >= s_min → margin s/s_min - 1 → WILSON-061, 369.
- `CHECK-pcb-crosstalk-spacing`: inputs spacing s (mm) between electrically long, susceptible nets → pass s > 1 mm (crosstalk < 10%) or ground track between them or field-solver result within budget → WILSON-062.
- `CHECK-fab-capability`: inputs min track, min gap (mm), min finished PTH (mm), board thickness t (mm), layer count → pass track/gap >= 0.15 mm (warn 0.10–0.15, fail < 0.10); PTH >= 0.3 mm (warn 0.2–0.3, fail < 0.2); aspect ratio t/d <= 6 (warn to 12, fail > 12); 0.35 <= t <= 3.5 mm; layers even and <= 14–24; thicker copper -> wider minimum track → WILSON-055, 058, 065.
- `CHECK-hole-lead-fit`: inputs lead diameter, finished hole diameter (mm) → clearance = hole - lead → pass 0.15 <= clearance <= 0.30 mm (auto-insertion may need more) → WILSON-064.
- `CHECK-pad-size`: inputs hole (mm), pad (mm), plated (bool), laminate → PTH: pad >= 1.3 mm for a 0.8 mm hole (i.e. pad - hole >= 0.5 mm, derived); non-PTH: pad - hole >= 1.0 mm and pad/hole >= 2 (FR4) or >= 2.5 (SRBP) → WILSON-066.
- `CHECK-edge-clearance`: inputs copper-to-board-edge distance (mm) → pass >= 0.5 mm → WILSON-068.
- `CHECK-resist-registration`: inputs mask process (screen / photo), pad-to-adjacent-track gap g (mm) → clearance c = 0.3–0.4 mm (screen) or < 0.1 mm (photo) → pass g > c (track stays covered); dense wave-soldered SM requires photo-imaged mask → WILSON-076, 080.
- `CHECK-track-resistance`: inputs width w, copper thickness t (0.035 mm per oz), length l, I, T → R = rho*l/(w*t) x 2 (manufacturing tolerance up to 2:1) x (1 + 0.00393*(T - 20)); V = I*R → pass V <= budget → WILSON-053, 059.
- `CHECK-plane-slots`: inputs plane cut-outs, tracks with high di/dt (clock, switching) → pass no slot crosses under a high-di/dt track's return path; no x-y moat crossed by HF or low-level signals; multiple planes stitched → WILSON-071, 074.
- `CHECK-test-access`: inputs net list with test requirement, test pads → pass every required node has a dedicated component-free pad (<= 1 mm dia) on the non-component side, on a 2.54 mm grid (>= 1.27 mm), never a component lead pad; tooling holes present → WILSON-082, 385.
- `CHECK-sir`: inputs surface resistance Rm (Mohm, Table 2.1), spacing w, parallel length l, derating factor D (10–1000 by environment), required leakage resistance R_req → Ri = 160*Rm*w/l/D → pass Ri >= R_req, else guard ring or PTFE stand-off → WILSON-090, 091, 092.

### Passive components
- `CHECK-divider-tolerance`: inputs R1, R2 (nominal), tolerance K, output spec → V'/V at (R1 +K, R2 -K) = 1 - 2K*R1/(R2*(1-K) + R1*(1+K)) and the mirror corner → pass both corners within spec (never rely on statistical averaging for critical ratios) → WILSON-099, 101.
- `CHECK-resistor-stress`: inputs R, worst-case voltage V_max across it (at maximum rail, e.g. 17 V on a nominal 12 V rail), P_rated, LEV → P = V_max^2/R → pass P <= 0.5*P_rated and V_max <= LEV → margin 1 - P/(0.5*P_rated) → WILSON-106, 109, 394.
- `CHECK-resistor-pulse`: inputs V_pk, R, pulse width tau (or exponential tau'), period T → P_avg = (V^2/R)*(tau/T) (rectangular) or (V^2/R)*(tau'/(2T)) (exponential) → pass P_avg <= P_rated; flag tau > 1 ms or duty > 0.1 for manufacturer pulse-derating curves; flag helical film/wirewound in snubbers → WILSON-108, 110.
- `CHECK-tempco-drift`: inputs tempco (ppm/C) or tracking tempco for ratio pairs, dT (C), drift budget → dR/R = tc*dT → pass <= budget → WILSON-103, 104, 116.
- `CHECK-cap-effective-value`: inputs C_nom, tolerance (+/-), tempco limits over the operating range, voltage coefficient at V_op, frequency coefficient at f_op, aging per 1000 h → C_max = C*(1 + tol+)*(1 + tc+)*(1 + vc+)*(1 + fc+); C_min = C*(1 - tol-)*(1 - tc-)*(1 - vc-)*(1 - fc-)*(1 - aging) → pass [C_min, C_max] inside the circuit's allowed window → WILSON-138, 139.
- `CHECK-cap-voltage-derating`: inputs V_op_max incl. transients and off-load/high-line (V), V_rated, type → ratio = V_op/V_rated; relative failure rate = ratio^5 → pass ratio <= 1 (hard), ratio <= 0.5 recommended (electrolytics: derate heavily) → margin 0.5 - ratio → WILSON-130, 288, 393.
- `CHECK-electrolytic-leakage`: inputs C (uF), V_rated, k (0.01–0.03 general, 0.002 low-leakage), T_max → I_leak = k*C*V_rated uA, x10 at maximum temperature, higher at first power-up → pass circuit error (I_leak x source impedance / timing error) within budget → WILSON-131, 135.
- `CHECK-electrolytic-life`: inputs rated life L0 (h) at T0 (C), operating core temperature T (C) incl. ripple heating, required life (h) → L = L0*2^((T0 - T)/10) → pass L >= required → margin L/required - 1 → WILSON-134.
- `CHECK-ripple-current`: inputs RMS ripple current (computed; ~2–3 x DC load for rectifier reservoirs), rating I_R at f and T (correct for non-sinusoidal waveform) → pass I_ripple <= I_R → WILSON-132, 292.
- `CHECK-series-cap-bleed`: inputs N capacitors in series, V_total, minimum leakage resistance Rdc_min, V_rated, C, safe voltage V_safe, required discharge time → R_bleed <= Rdc_min/10 ("comfortably below", factor 10 conf low); V_each = V_total/N <= V_rated; t_discharge = R_bleed_total*C_total*ln(V0/V_safe) <= requirement → WILSON-140.
- `CHECK-decap-srf`: inputs C, ESL (from package/leads), highest frequency to decouple f_max → f_SRF = 1/(2*pi*sqrt(ESL*C)) → pass f_SRF >= f_max or a smaller parallel capacitor covers the band; flag anti-resonance between parallel parts (sim) → WILSON-142.
- `CHECK-sense-resistor`: inputs R_sense, stray/self inductance L, f, error budget; Kelvin connection flag → Z_L = 2*pi*f*L; pass Z_L/R_sense <= budget and 4-terminal connection present → WILSON-111, 112.
- `CHECK-winding-ac-resistance`: inputs wire diameter d, f, resistivity, mu_r → D = sqrt(rho/(pi*mu0*mu_r*f)); pass d/D < 2 (skin effect negligible); else Rac/Rdc ~ (d/D + 1)/4 for d/D > 5 (use litz/thinner strands) → WILSON-149, 150.
- `CHECK-inductive-clamp`: inputs every relay/solenoid/inductive load and its switch → pass clamp present: DC coil freewheel diode (I_F >= coil current, V_R >= supply) or zener (V_z > V_supply_max + tolerance and < switch V_BR); AC coil RC snubber → WILSON-154, 155.
- `CHECK-crystal-circuit`: inputs C1, C2, C_stray (<= 10 pF), specified C_L, drive power P_d, quoted motional R → C_load = C1*C2/(C1 + C2) + C_stray → pass abs(C_load - C_L) within trim range; C2/C1 ~ 3; P_d <= 0.5–1 mW; oscillator starts with 3x quoted R → WILSON-156, 157, 158.
- `CHECK-rtc-drift`: inputs crystal type, T_min, T_max, spec (s/day) → tuning fork: df/f = -0.04e-6*(T - 25)^2; s/day = abs(df/f)*86400 → pass <= spec at both extremes, else AT-cut → WILSON-160.
- `CHECK-pot-use`: inputs signal frequency f, circuit resistance R → pass f*R < 1e6 Hz*ohm; wiper DC current minimal; rheostats have wiper tied to one end; small-trimmer wiper current <= 100 mA → WILSON-117, 120, 121.

### Active devices
- `CHECK-leakage-at-temperature`: inputs leakage I25 (A, datasheet max), T_max (C), source/bias resistance R (ohm), error budget (V) → I(T) = I25*2^((T - 25)/10); V_err = I(T)*R → pass V_err <= budget → WILSON-167, 172, 188, 203.
- `CHECK-zener-clamp`: inputs V_fault, Vz_nom, tolerance, slope resistance, VF, zener power rating P_z (at T), R_in, leakage at V_op and T, source R → Vz_max(I) = Vz*(1 + tol) + (I - IZ)*Rs; I_z = (V_fault - Vz_max - VF)/R_in; pass Vz_max + VF <= protected-pin limit, Vz_max*I_z <= P_z, I_leak(T)*R_source <= error budget, clamp capacitance x R bandwidth >= required → WILSON-171, 173.
- `CHECK-snubber`: inputs V_peak, device dv/dt, minimum load RL, ITSM, IL, di/dt → C_min = 0.63*V_peak/((dv/dt)*RL); R_min = max(V_peak/(0.5*(ITSM - IL)), sqrt(V_peak/(C*di/dt))) → pass chosen C >= C_min (pulse-rated), R >= R_min, add diode if R >> RL, resistor pulse rating OK → WILSON-178.
- `CHECK-base-emitter-bleed`: inputs IB_on, VBE (0.6 V), worst-case leakage/offset current I_off(T) → R_BE ~ VBE/(0.1*IB_on); V_off = I_off(T)*R_BE → pass V_off well below conduction (book example 60 mV) → WILSON-179, 180.
- `CHECK-bjt-drive`: inputs IC required, IB available, hFE_min (at IC, VCE), cold derating k = 2–3 → pass IB*hFE_min/k >= IC; IB <= IC/10 is enough for saturation (more is wasted) → WILSON-180, 182.
- `CHECK-soa`: inputs operating locus (VCE, IC, duration), Tj → pass every point inside the derated SOA (IC max, VCE max, P max derated from 25 C by thermal resistance, second breakdown) → WILSON-181.
- `CHECK-gate-drive`: inputs Qg (C), drive current Ig (A), required switching time t_req (s), drive voltage V_drive, VGS at which RDSon is specified → t = Qg/Ig → pass t <= t_req and V_drive(min) >= VGS_spec (no 10 V-rated MOSFET on 5 V logic) → WILSON-192.
- `CHECK-gate-coupling`: inputs drain transient V_spike, CGD, CGS, VGS_max, gate zener present, driver dynamic impedance → V_g = V_spike*CGD/(CGD + CGS) → pass V_g < VGS_max or gate zener fitted at the pins → WILSON-193.
- `CHECK-stray-inductance-spike`: inputs loop inductance L (H), switched current I (A), turn-off time t (s), bus voltage, VDS_max → V_ds_pk = V_bus + L*I/t → pass V_ds_pk <= VDS_max (with local clamp/snubber otherwise) → WILSON-195.
- `CHECK-rdson-hot`: inputs RDSon(25 C), factor 1.8–2 at Tj_max, I_rms, VGS actual vs spec → P = I^2*RDSon(25)*2 → feed CHECK-junction-temperature; flag VGS below characterisation value → WILSON-196.

### Analog ICs
- `CHECK-opamp-dc-error`: inputs VOS_max, drift (uV/C) x dT, IOS, IB, source resistances at + and - inputs, noise gain G, output headroom (V) → V_in_err = VOS + drift*dT + IOS*RS (balanced) or IB*dRS (unbalanced); V_out_err = G*V_in_err → pass V_out_err <= allowed error and, for AC-coupled high-gain stages, V_out_err + V_signal_pk <= swing limit → WILSON-201, 202, 203, 204.
- `CHECK-opamp-cmrr-psrr`: inputs CMRR(f), PSRR(f) (dB), common-mode swing, rail ripple at frequency → V_err = V_cm*10^(-CMRR/20) + V_ripple*10^(-PSRR/20) → pass <= budget (use 20–30 dB PSRR at tens-hundreds of kHz) → WILSON-205.
- `CHECK-opamp-swing`: inputs required V_out_pk, minimum rail (unregulated low line), output headroom (2 V for bipolar/BiFET, datasheet for rail-to-rail incl. load ratio), load current → pass V_out_pk <= V_rail_min - headroom and I_load <= ~10 mA → WILSON-207.
- `CHECK-slew-fpbw`: inputs slew rate SR (V/s), f_max (Hz), V_pk (V) → pass SR >= 2*pi*f_max*V_pk → margin SR/(2*pi*f*Vp) - 1 → WILSON-208.
- `CHECK-gain-accuracy`: inputs GBW (Hz), frequency f, feedback factor beta, AOL at DC, hot/cold AOL factor (0.5), gain-error spec → AOL(f) = min(AOL_dc, GBW/f)*0.5; A_CL = AOL/(1 + AOL*beta); error = 1 - A_CL*beta → pass error <= spec → WILSON-209, 212.
- `CHECK-noise-budget`: inputs en, in (per rtHz), RIN, R1, RF, AV, T, fc and filter order → per-source output densities per the Fig 5.17 model; noise bandwidth B = 1.57*fc (single pole); V_out_rms = sqrt(sum N_i^2)*sqrt(B); pk-pk = 6.6*rms → pass <= spec (e.g. below 1/2 LSB at the ADC) → WILSON-213, 214, 215, 216.
- `CHECK-opamp-power`: inputs rails, IS_max (cold), load swing and resistance, theta_JA → P = (V+ - V-)*IS + load share; Tj = TA + P*theta_JA → pass Tj within grade; sum IS for supply budget → WILSON-217, 218.
- `CHECK-comparator-drive`: inputs source resistance at inputs, input transit time through the linear region, hysteresis band, input noise pk-pk → pass R_source <= 10 kohm (prefer <= 1 kohm); if transit > a few hundred ns require hysteresis with band >= noise pk-pk (band ~ Vcc*R1/(R1 + R2)) → WILSON-225, 226.
- `CHECK-comparator-inputs`: inputs worst-case differential and CM voltages (incl. rail sequencing), datasheet limits, series R → pass within limits or R >= V_over/I_in_max; unused comparators saturated (one input grounded, other fixed) → WILSON-227, 228.
- `CHECK-reference-substitution`: inputs candidate references (Vmin, Vmax, tempco, min current, capacitor requirement, pinout) → design limits = envelope over all approved candidates; pass bias current >= max(I_min) and capacitor rule compatible with every candidate → WILSON-230, 231.

### Digital, interfaces, firmware
- `CHECK-logic-noise-margin`: inputs driver VOH_min/VOL_max at actual load current and temperature, receiver VIH_min/VIL_max at its own supply → NM_H = VOH_min - VIH_min; NM_L = VIL_max - VOL_max → pass both >= 0 (plus expected coupled noise); fail examples: LS-TTL into HCMOS (2.7 V < 3.15 V) → WILSON-233, 234.
- `CHECK-node-slew-timing`: inputs per net: sum of input capacitances (5–10 pF each) + ~5 pF interconnect, driver dynamic current (74HC 40 mA, buffers 60 mA), threshold V, propagation delays, timing slack → t = C*V/I + t_pd → pass t <= slack with safety factor → WILSON-235.
- `CHECK-ground-bounce`: inputs number of simultaneously switching outputs N, load C each, edge rate dV/dt, edge time t_r, ground inductance L (20 nH per inch of track) → I = N*C*dV/dt; V = L*I/t_r → pass V < receiver noise margin (book: ~1 V approaches fast-logic margin) → WILSON-236.
- `CHECK-decoupling`: inputs per IC: peak transient current I_pk, edge duration t, allowed droop dV (<= system noise margin), capacitor distance d, package inventory → C_min = I_pk*t/dV; pass C >= C_min, d <= 12.7 mm for 74AC/ECL/bus drivers, board counts: >= 1 x 22 uF bulk, >= ceil(N_SSI_MSI/10) + ceil(N_LSI/3) x 1 uF tantalum, 10–100 nF per LSI supply pin, per octal/MSI, per 4 SSI → WILSON-237, 238.
- `CHECK-floating-inputs`: inputs netlist → pass no unconnected logic input (esp. CMOS, preset/clear); no floating comparator inputs → WILSON-228, 239.
- `CHECK-mixed-signal-grounds`: inputs ground nets and tie points, plane outlines, routing → pass exactly one AGND-DGND tie (at the ADC for single-board, at the PSU for multi-board), digital plane not under analog area, no digital track through the analog region → WILSON-241.
- `CHECK-adc-noise-vs-lsb`: inputs VFS, N, input-referred noise (rms or pk-pk incl. ground noise) → LSB = VFS/2^N → pass noise pk-pk < 1 LSB (conf low; book: noise equal to one LSB gives one-bit uncertainty) → WILSON-240, 253, 262.
- `CHECK-sqnr`: inputs N, OSR, required SNR → SQNR = 6.02*N + 1.76 + 10*log10(OSR) (dB) → pass SQNR >= required → WILSON-264, 265.
- `CHECK-anti-alias`: inputs fs, f_max of wanted signal, input noise/interference spectrum, filter response → pass fs >= 2*f_max and filter attenuation at every alias source (abs(f - n*fs) in band) >= required rejection → WILSON-253.
- `CHECK-wakeup-settle`: inputs switching source resistance R, decoupling C, resolution N, time before first conversion → t_settle = R*C*ln(2^N) → pass t_before_conversion >= t_settle → WILSON-255.
- `CHECK-opto-ctr`: inputs required output current, CTR_min, end-of-life margin m (0.2–0.5), LED drive current, data rate → pass I_LED >= I_out/(CTR_min*(1 - m)); rate <= 100 kbit/s for standard transistor couplers; CMTI >= expected dV/dt → WILSON-245.
- `CHECK-rs232`: inputs cable C/m, length, receiver C, data rate, rails → pass total C <= 2500 pF; rate <= 20 kb/s (<= 3 m above 20 kb/s); driver swing >= +/-5 V into 3–7 kohm (no +/-5 V-rail drivers) → WILSON-246.
- `CHECK-rs422`: inputs length L (m), bit rate B (kb/s), receivers, terminations → pass L <= 1e5/B, receivers <= 10, exactly one 100 ohm termination at the far end → WILSON-247.
- `CHECK-rs485`: inputs sum of unit loads, terminations, idle bias network, length → pass UL <= 32, 2 x 120 ohm at the ends, idle differential > 200 mV with terminations, L <= 1200 m → WILSON-248.
- `CHECK-can`: inputs bit rate, trunk length, node count, max stub, terminations → pass at 1 Mb/s: L <= 40 m, nodes <= 30, stubs <= 0.3 m, 2 x 120 ohm; unpowered nodes high-Z → WILSON-249.
- `CHECK-usb-channel`: inputs cable Z0, one-way delay, driver impedance → pass Z0 = 90 ohm +/-15%, delay <= 26 ns, driver 28–44 ohm → WILSON-250.
- `CHECK-watchdog`: inputs watchdog type, timeout t_wd, maximum interval between re-triggers across all code paths (incl. initialisation and EEPROM writes), output connection → pass hardware (non-programmable) timer or on-chip watchdog, 10 ms <= t_wd <= 1 s, max interval < t_wd, output drives RESET, re-trigger AC-coupled from a port bit set/cleared in two modules → WILSON-257.
- `CHECK-supervisor`: inputs regulator minimum input, reset threshold, power-fail threshold, hold-up between them, firmware housekeeping time → pass V_pf > V_reset >= V_in_min(regulator), t(V_pf -> V_reset) >= t_housekeeping at maximum load, firmware tolerant of repeated power-fail interrupts (brownout) → WILSON-258, 304.
- `CHECK-nv-memory-protection`: inputs NV write/chip-enable gating, backup-domain input pull resistors, RAM input vs VCC difference → pass hardware "low line" gating present, pull-DOWNs (not pull-ups) on backup-domain inputs, V_in <= VCC_RAM + 0.3 V or current-limited → WILSON-259.

### Power supplies and batteries
- `CHECK-fuse`: inputs max operating input current I_op (over whole input range), prospective fault current I_f, fuse standard and rating I_N, pulse I^2t, fuse I^2t, system voltage, prospective short-circuit current → pass I_f/I_op >= 2 (else secondary protection); pulse I^2t <= 0.5–0.8 x fuse I^2t; V_fuse > V_sys; breaking capacity > prospective current; class F or T preferred → WILSON-272, 273, 274, 275, 276.
- `CHECK-linear-psu-headroom`: inputs Vout_min, regulator tolerance, dropout at I_max and Tj, sense drop, ripple, diode drops, Vac_nom, Vac_min → Vin_dc_min = Vout_min + Vtol + Vdrop + Vsense; Vtx = (Vin_dc_min + Vripple + VD)/0.92*(Vac_nom/Vac_min)/sqrt(2) → pass selected transformer secondary >= Vtx (at the crest-current IR drop) → WILSON-286.
- `CHECK-regulator-thermal`: inputs Vin_dc at maximum line (average), Vout, I range, source ESR Rs, V_nl → P(I) = I*(V_nl - I*Rs - Vout); worst P at I = (V_nl - Vout)/(2*Rs) if below full load, else at full load → feed CHECK-junction-temperature → WILSON-287, 289.
- `CHECK-reservoir-voltage`: inputs transformer off-load voltage at maximum line (incl. regulation up to 20%+), diode drops at low current (0.6 V) → V_res_max = sqrt(2)*Vtx_offload_maxline - 2*VD → pass V_res_max <= capacitor rating (derated) and <= regulator absolute maximum input (else pre-regulator) → WILSON-288.
- `CHECK-reservoir-capacitance`: inputs IL, allowed ripple Vr, mains frequency → C_min = IL*t/Vr, t = 8 ms (50 Hz FW) / 6 ms (60 Hz FW), apply -20% tolerance → pass C_nom*0.8 >= C_min; ripple current per CHECK-ripple-current → WILSON-291, 292.
- `CHECK-rectifier`: inputs I_DC, topology, V_pk, Rs, C, IFSM, PIV → pass I_F(rated) >= 2*I_DC (5x for off-line SMPS), Vmax/Rs <= IFSM, C*Rs < half-cycle, PIV >= 1.5–2 x V_pk (bridge) or 2 x that (centre tap), >= 600 V (pref. 800 V) on 240 V mains → WILSON-293, 294.
- `CHECK-hold-up`: inputs C, load current I (or SMPS power), ripple-trough voltage at the minimum specified line, regulator minimum input → t_h = (V_trough - V_min)*C/I (linear) → pass t_h >= spec at minimum line (hold-up is zero at the design minimum input) → WILSON-301.
- `CHECK-foldback`: inputs Vout, VBE(on), requested IK/ISC → pass IK/ISC <= 1 + Vout/VBE(on) and practical <= 2–3 for low-voltage rails → WILSON-300.
- `CHECK-reservoir-hum`: inputs peak charging current (~5 x I_DC), resistance of any conductor shared between reservoir charging path and load ground → V_hum = I_pk*R_shared → pass V_hum <= budget (ideally R_shared = 0: loads grounded at the capacitor) → WILSON-297.
- `CHECK-harmonics-applicability`: inputs rated power, product type, input current per phase → EN 61000-3-2 applies if <= 16 A and (P >= 75 W or lighting) → then PFC or measured compliance required → WILSON-281, 282.
- `CHECK-psu-noise-choice`: inputs sensitive analog bandwidth, SMPS switching frequency, ripple+noise spec measured over >= 10 MHz → flag if analog bandwidth > f_sw on an SMPS rail (prefer linear or add filtering) → WILSON-296.
- `CHECK-battery-window`: inputs chemistry, cells in series N, circuit operating range → pass circuit V_min <= N*V_end (alkaline 0.8–0.9, lead-acid 1.75, NiCd/NiMH 1.0, Li-ion 3.0 V/cell) and V_max >= N*V_OC (+15% over on-load); runtime at actual discharge rate (capacity falls at high C rate) → WILSON-308, 309, 313, 314, 315, 316.
- `CHECK-charger`: inputs chemistry, charge voltage per cell, temperature compensation, current limit, trickle current → pass lead-acid 2.25–2.5 V/cell with -4 mV/C/cell and I <= 0.25 C (float at ~0.05 C); NiCd constant current <= 0.1 C continuous (<= 0.3 C with care); NiMH trickle <= C/250; Li-ion pack with integrated protection → WILSON-317, 318, 319.

### EMC, safety, reliability, thermal
- `CHECK-rf-field-exposure`: inputs nearby transmitters (P, antenna gain, distance d) → E = sqrt(30*P*gain)/d (far field) → pass E <= specified immunity level (>= 3 V/m, 10 V/m preferred, 10 MHz–1 GHz) → WILSON-321, 322.
- `CHECK-transient-immunity-target`: inputs environment class, reliability class → pass test level >= 2 kV (4–6 kV high reliability); expected upset rate from Table 8.2 x fraction above threshold (N ~ V^-3) acceptable → WILSON-323, 324.
- `CHECK-radiated-emission-estimate`: inputs loop areas A (m^2) or unterminated conductor lengths L (m), harmonic currents I (A) at f (Hz), distance d (m), limit (from the current standard) → E = 1.316e-14*f^2*A*I/d (loop) or 1.2566e-6*f*L*I/d (monopole); dBuV/m = 20*log10(E/1e-6) → pass below limit with margin; flag conductors >= lambda/4 → WILSON-338, 340.
- `CHECK-aperture-se`: inputs longest aperture dimension d (m), number of similar apertures within lambda/2, f_max (Hz), required SE (dB) → lambda = 3e8/f_max; SE = 20*log10(lambda/(2*d)) - 10*log10(N) (0 if lambda <= 2d) → pass SE >= required (d <= 1.6 cm for 20 dB at 1 GHz) → WILSON-347.
- `CHECK-seam-pitch`: inputs fastener/contact pitch p (m), f_max → pass p <= (3e8/f_max)/20, else conductive gasket/finger stock; mating surfaces unpainted → WILSON-348, 361.
- `CHECK-shield-material-se`: inputs thickness t (mm), mu_r, sigma_r, f, source distance r, field type → R (E, H or plane-wave formula) + A = 0.1314*t*sqrt(mu_r*sigma_r*f) (+ B if A < 10 dB) → pass >= required (usually far above aperture-limited SE) → WILSON-346.
- `CHECK-filter-topology`: inputs source and load impedances at the interference frequency, filter element order → pass capacitor faces the high impedance, inductor faces the low impedance; filter ground bonded directly to chassis; input/output wiring separated → WILSON-349, 351.
- `CHECK-y-cap-leakage`: inputs total line-to-earth capacitance C_Y (F), mains V (rms), f (Hz), leakage limit for class/application (0.25–5 mA) → I_leak = 2*pi*f*V*C_Y (derived) → pass <= limit; class I plug-connected: each C_Y <= 5 nF (BS 613); X/Y parts mains-rated → WILSON-352.
- `CHECK-mains-filter-current`: inputs input I_rms, crest factor (>= 3 for rectifier-capacitor inputs), filter saturation/peak rating → pass I_rms*crest <= peak rating → WILSON-353.
- `CHECK-earth-strap`: inputs strap length and width → pass L/W < 3 → WILSON-360.
- `CHECK-creepage-clearance`: inputs working voltage V (V), measured creepage and clearance (mm), location (general / between PCB conductors) → required (EN 60065 anchors): general 0.5 mm at <= 34 V ... 3 mm at 354 V; PCB conductors 0.5 mm at <= 124 V ... 3 mm at 1240 V; intermediate values from the standard's table (linear interpolation only as a screening assumption, conf low) → pass measured >= required → WILSON-369.
- `CHECK-earth-continuity`: inputs measured earth-path resistance at 10 A for 60 s → pass < 0.5 ohm (EN 60065 example) → WILSON-023.
- `CHECK-touch-safety`: inputs accessible circuit voltages and possible touch current → pass accessible parts are SELV (< 50 V rms, isolated) or touch current < 0.5 mA AC; Class I: all accessible conductive parts bonded → WILSON-364, 365, 366.
- `CHECK-junction-temperature`: inputs PD (W), Rth_j-c, Rth_c-h (Table 9.5 by package/washer/grease), Rth_h-a (catalogue, divided by altitude efficiency Table 9.4, x1/0.7 if fins horizontal, x1.25 if heatsink rise is ~10 C instead of 20 C), TA_max, Tj_max → Tj = PD*(Rjc + Rch + Rha_eff) + TA_max → pass Tj <= Tj_max (IRF640 example 150.5 C fails 150 C) → margin (Tj_max - Tj)/(Tj_max - TA) → WILSON-402, 403, 406, 407, 408, 414.
- `CHECK-pulsed-junction`: inputs PDmax (on-period), duty d, K from transient thermal impedance curves, Rjc, Rch, Rha, TA → Tj = PDmax*(K*Rjc + d*(Rch + Rha)) + TA → pass <= Tj_max; K = d above a few kHz with d > 20% → WILSON-405.
- `CHECK-thermal-time-constant`: inputs Rth_h-a, heatsink volume and material (Table 9.3) → tau = Rth*V*c_vol → report time to steady state (~5 tau) for test duration planning → WILSON-404.
- `CHECK-fan-flow`: inputs dissipated power PD (W), allowed internal rise theta (C), fan curve and system pressure drop → Q_req = 3600*PD/(1.3*1000*theta) m^3/h (/1.7 for CFM; cross-check 1.76*W/dT CFM) → pass fan operating-point flow >= Q_req → WILSON-086, 410.
- `CHECK-reliability-prediction`: inputs per-part base failure rate lambda_i, stress factor S_i, activation energy ea, Tref, Top, MTTR, capacitor V/V_rated → A_t = exp((ea/8.6e-5)*(1/Tref - 1/Top)); lambda = sum(A_t*S_i*lambda_i) (x (V/Vr)^5 relative factor for capacitors); MTBF = 1/lambda; A = MTBF/(MTBF + MTTR) → pass MTBF and A >= requirements; report top contributors → WILSON-089, 389, 390, 392, 393, 398, 400.
- `CHECK-redundancy`: inputs per-channel failure probabilities P_i, common-mode failure list, failure annunciation present → P_sys = product(P_i) only if no common-mode path → pass P_sys <= target and failed-element detection exists → WILSON-399.
- `CHECK-power-device-mounting`: inputs lead-bend distance/radius/angle, heatsink flatness and finish, clamp force, washer/bush material → pass bend >= 4 mm from body, R >= 2 mm, <= 90 deg (none for metal cans); flatness <= 0.004 in/in, finish 50–60 uin; force >= 20 N; bush not unfilled nylon; soldering after fastening → WILSON-412, 413, 414, 415.
- `CHECK-boundary-scan-need`: inputs gate count (ASIC/FPGA), sequential/memory content, probe access → < 10 K no structured test; 10–20 K consider; > 20 K require boundary scan (TAP routed, chain documented) → WILSON-383, 384.
- `CHECK-psu-sizing`: inputs output power, efficiency → heat = Pout*(1/eta - 1); linear eta <= ~0.5, SMPS 0.7–0.9 → feed thermal checks; PSU not heavily over-rated (light-load efficiency) → WILSON-284, 285, 306.

## 4. Verification procedures & plots

| property | method | x / y axes | sweep / corners | good / pass criterion | setup notes | source |
|---|---|---|---|---|---|---|
| Ground/return drops | measure DC and dynamic voltage along each 0 V and supply conductor relative to the PSU star point | x: load state (all combinations of switched relays/lamps), y: V at each board's 0 V and supply pins | min/max load, max ambient (copper tempco) | far-end rails >= V_min; 0 V noise << receiving circuits' noise margin (e.g. 100 mV vs 1 V CMOS) | DVM for static; scope for switched-load transients (chattering, motor-boating) | §1.1.5, WILSON-006/007 |
| Ground-loop pickup | spectrum of a low-level input with the unit beside transformers/contactors/fans | x: frequency (mains harmonics), y: input-referred pickup (V) | orientation and position of field sources | pickup below input noise spec; compare with V = 1e-8*A*n*dB/dt | toroidal sources reduce field; reroute wires against chassis | §1.1.4, WILSON-004 |
| Output-to-input common impedance | simulate/measure loop A*Rs/(RL+Rs) including track/wire impedance | x: frequency, y: loop magnitude and phase | full bandwidth of the amplifier | loop never reaches -1; response error small | model Rs as R + jwL (20 nH/inch) | §1.1.7, WILSON-011 |
| Transmission-line behaviour | step/TDR bench test: fast pulse generator, line, wideband scope at both ends; or Bergeron / SPICE line model | x: time (ns), y: V at source and far end | open, matched and shorted loads; worst driver impedance | ringing within logic noise-immunity band; ringing period ~2x transit (~35 MHz/L[m] for 0.6 mm track on 1.6 mm FR4) | driver/receiver I-V characteristics must extend beyond the rails for Bergeron analysis | §1.3.2, Fig 1.26/1.27, WILSON-045/046 |
| Standing waves / VSWR | move a sniffer probe along a (leaky) line with an RF voltmeter; locate voltage minimum | x: position (fraction of lambda), y: abs(V) | at each operating frequency (pattern is frequency dependent) | SWR <= spec; phase = 720*(x/lambda - 1/4) deg | plot Gamma on reflection-coefficient (Smith) chart to classify the load | §1.3.3, Fig 1.29/1.30, WILSON-048/052 |
| Twisted-pair/cable pickup | inject a known magnetic field; compare twisted vs parallel pairs | x: frequency, y: attenuation (dB) | 22 AWG pairs, parallel spacing 0.032 in reference (Fig 1.23) | twisted pair much better than parallel at LF; check end-loop areas | twist rate 26–50 turns/m | §1.2.6, Fig 1.23 |
| Cable/track crosstalk | victim response to offender sine sweep (lumped) or offender edge (digital) | x: frequency or time; y: victim V (dB or V) | max cable length, max edge rate, min victim impedance | XT <= spec (e.g. -60 dB audio); digital spikes < victim noise margin | model Cc = pF/m x length | §1.2.7, Fig 1.24/1.25, WILSON-038/039 |
| Surface/leakage stability | log high-impedance node bias vs time with RH and temperature cycling, with/without guard | x: time / RH, y: node voltage or leakage current | humid, dusty, handled boards | drift within spec; guard reduces surface leakage | expect 10–1000x worse than clean-board Ri = 160*Rm*w/l | §2.4, WILSON-090/092 |
| Resistor/parameter tolerance | Monte Carlo with r = normal(mean, mean-3sigma, mean+3sigma) plus explicit worst-case corners | x: parameter value / circuit output, y: count (histogram with mean and +/-3 sigma) | >= 1000 runs; corners for every critical ratio | all outputs within spec at the corners; never rely on averaging | batch "holes" possible (screened-out tight parts) | §3.1.2, Fig 3.3–3.6, WILSON-099–101 |
| Capacitor/decoupling impedance | impedance analyser on each part and on the combined decoupling network (or SPICE with ESR/ESL) | x: frequency (log), y: abs(Z) (log) | 100 kHz – several hundred MHz | abs(Z) below target across the band; note SRF (47 uF tantalum ~500 kHz, 100 pF COG ~100 MHz) and anti-resonances | include mounting/track inductance | §3.3.9, Fig 3.24/3.25, WILSON-142 |
| Capacitance vs bias/temperature | measure C at DC bias and temperature; ramp linearity for integrators | x: V_bias or T, y: dC/C (%) | full voltage and temperature range, 1000 h aging | inside circuit window (Z5U can span 11:1) | Table 3.5 codes give temperature limits only | §3.3.6, WILSON-138/139 |
| Dielectric absorption | charge to VA, short, open-circuit, record recovery | x: time, y: recovered V/(VA - VB) | hold times of the application | <= 0.01–0.02% for PS/PP sample-and-hold caps | measure soon after sampling in the application | §3.3.8, Fig 3.23, WILSON-141 |
| Electrolytic ESR/ripple | ESR vs temperature; case temperature at rated ripple | x: T (C) / ripple current, y: ESR (ohm) / case rise | down to minimum ambient | impedance ratio (cold/20 C) <= 3–4; ripple within rating | non-sinusoidal ripple needs a correction factor | §3.3.4, WILSON-132/133 |
| Magnetics characterisation | B-H loop; leakage inductance with secondary shorted; Rac sweep; winding capacitance by resonance (IEEE 389) | x: H / f, y: B / L / R / Z | low signal level (avoid saturation), frequency range of use | loop area x f = core loss; Lleak and Rac within design | FEA alternative for leakage inductance | §3.4.2–3.4.4, WILSON-146–150 |
| Inductive turn-off transient | scope the switch node (collector/drain/contact) at coil turn-off, with and without clamp | x: time, y: V_switch | supply max, coil at temperature | peak below switch breakdown with margin (hundreds of volts possible from 12 V without clamp) | coil self-capacitance is never specified - must measure | §3.4.6, Fig 3.40, WILSON-154/155 |
| Crystal oscillator margin | start-up with extra series resistance = 2x quoted motional R (3x total); drive level; frequency vs temperature | x: time / T, y: amplitude / df/f (ppm) | coldest temperature, lowest supply | reliable start with 3x R; drive <= 0.5–1 mW; df/f within spec (tuning fork -144 ppm at +85/-35 C) | keep probe capacitance off the high-Z node | §3.5, Fig 3.45, WILSON-157–160 |
| Diode/zener leakage and tempco | temperature sweep 0–100 C of production-representative samples from several batches/vendors | x: T (C), y: leakage (log) / Vz | min/max temperature; different manufacturers | worst case within design budget (doubling per 10 C) | prototype parts are usually low-leakage - do not trust them | §4.1.3, Fig 4.5/4.10, WILSON-167/172 |
| Transistor SOA | overlay the measured VCE-IC trajectory (incl. switching transients) on the datasheet SOA derated to Tj | x: VCE (log), y: IC (log) | worst load, supply and temperature | whole trajectory inside SOA | second breakdown limits high-VCE operation | §4.3.4, Fig 4.22, WILSON-181 |
| BJT gain/drive | IC vs IB at temperature extremes; large-signal waveform at low VCE/high IC | x: IC / time, y: hFE / waveform | coldest temperature, min-grade parts | saturation maintained / no drive-starved distortion (Fig 4.24) | assume gain below datasheet minimum somewhere | §4.3.5, Fig 4.23/4.24, WILSON-182 |
| MOSFET switching | gate voltage (Miller plateau), VDS and ID at turn-on/off; drain spike | x: time (ns), y: VGS, VDS, ID | max current, max bus voltage, hot | switching time ~ Qg/Ig; VDS spike < rating; VGS transient < rating | short scope ground lead; Kelvin source layout | §4.5.3–4.5.4, WILSON-192–195 |
| Thyristor/triac triggering | gate trigger at lowest temperature with actual pulse width; dv/dt immunity with fast supply transients; light-load latching | x: gate pulse width / conduction angle, y: trigger success | cold, light load, early firing angle | reliable triggering; no false firing | Fig 4.13 energy dependence | §4.2, WILSON-174–178 |
| Op-amp stability | closed-loop step and frequency response with the real load (coax, capacitance); HF scope/spectrum analyser scan of every gain stage on prototypes | x: time / f, y: Vout / gain & phase | all gains, max capacitive load, supply extremes | no oscillation; acceptable overshoot; if oscillating near unity-gain BW, raising gain should stop it (loop instability diagnosis) | check decoupling resonance 1–10 MHz; series R + CF fixes | §5.2.10, §8.4.2, WILSON-210/211/342 |
| Op-amp DC error / headroom | output offset vs temperature with worst-case (not typical) parts; headroom of high-gain AC stages | x: T, y: V_out offset | max VOS part, temperature extremes, min rails | offset + signal within swing (e.g. TL072 x1000 = 10 V fails on +/-12 V) | a 1 mV bench sample hides the problem | §5.2.1, WILSON-201/202 |
| Noise | simulator AC noise analysis (not time-domain random sources) and hand calc per Fig 5.17 model | x: frequency (log), y: output noise density (nV/rtHz) | over the full bandwidth incl. 1/f region | integrated noise (x sqrt(1.57 fc)) within spec; hand calc matches sim (e.g. 28.8 nV/rtHz) | pk-pk = 6.6 x rms | §5.2.12, Fig 5.19, WILSON-213–216 |
| Comparator behaviour | output edges vs load capacitance; slow-input crossing viewed on a fast timebase; hysteresis thresholds up and down | x: time, y: Vout / thresholds | max load C, slowest input, max source impedance | single clean edge per crossing; thresholds as calculated | edge bursts are invisible at slow timebases | §5.3.2–5.3.4, Fig 5.23/5.26, WILSON-222–226 |
| Voltage reference | Vout vs temperature, line and load; power-up settling | x: T / Vin / Iload / time, y: Vout | full temperature range; all approved vendors | within the design's worst-case envelope | tempco curves are bowed; normalise specs | §5.4.3, Fig 5.30, WILSON-230/231 |
| Logic noise, ground bounce | dynamic noise-margin curve; scope probe tip shorted to its own ground clip next to the IC to see ground noise | x: pulse width / time, y: switching threshold amplitude / ground noise | all outputs switching (FF->00) | ground/supply noise << noise margin (1 V bounce = failure for fast logic) | pulses occur at the clock period; magnitude varies with data | §6.1.1/6.1.3, Fig 6.4/6.9, WILSON-234/236 |
| Switch and input debounce | storage-scope the raw switch input; count edges seen by logic | x: time (ms), y: V | many operations | exactly one logical event per actuation | bounce ~1 ms | §6.2.2, Fig 6.15/6.16, WILSON-243 |
| ADC signal chain | DC-input code histogram; full-scale sine FFT; alias injection at n*fs +/- f | x: code / frequency, y: count / dBFS | fs, full input range, digital activity running | noise within 1 LSB target; SQNR near 6.02N + 1.76 dB; aliases below requirement | measure with the digital circuit active (ground noise tens-hundreds of mV) | §6.2.1, §6.3.2, §6.9, WILSON-240/253/264 |
| Watchdog recovery | repeated transient bursts strong enough to derail the CPU; LED on watchdog output | x: event number, y: recovered (yes/no) | many events; bursts arriving during recovery | 100% correct reset and recovery | use deliberately weakened hardware if needed; keep a disable link for firmware debug | §6.4.2, WILSON-257 |
| Supervisor / brownout / NV memory | slow ramps, few-ms dips, brownout with line-frequency ripple; backup-battery drain with main power off | x: time, y: VCC, RESET, NMI, write-enable | repeated cycles; low temperature | no NV corruption; recovers from repeated power-fail interrupts; backup drain as designed (months vs years hides at prototype stage) | RC power-on reset misses dips of a few ms | §6.4.3, WILSON-258/259 |
| PSU inrush | switch-on current captured at many random phase angles incl. the voltage peak | x: time (ms), y: input current | cold NTC, hot NTC after short interruption | peak within fuse I^2t (<= 50–80%), rectifier IFSM | toroids can exceed 10x operating current | §7.2.4, Fig 7.5, WILSON-277–279/293 |
| PSU ripple & noise | scope output with >= 10 MHz bandwidth; inspect ripple shape | x: time, y: Vout ripple | full load, min/max line | linear < 1 mV rms; SMPS ~1% of rail; pulse-shaped ripple = layout fault, sawtooth = smoothing | measure common-mode noise too | §7.2.12, Fig 7.13/7.14, WILSON-296/297 |
| PSU load transient | load step response | x: time, y: Vout deviation | max step (relays, LED banks), min/max line | recovery within spec (linear tens of us, SMPS ms) | 78XX needs 0.1 uF out / 0.33–1 uF in | §7.2.13, Fig 7.15, WILSON-298 |
| PSU hold-up | interrupt mains at the ripple trough; time until regulation lost | x: time, y: Vres, Vout | minimum specified line, full load | hold-up >= spec at minimum line (13 ms at 240 V vs 2.5 ms at 204 V in the example) | spec hold-up at a stated line voltage | §7.3.2, Fig 7.18, WILSON-301 |
| PSU abnormal conditions | continuous short on each output; foldback V-I curve; overvoltage crowbar trip with transient injection | x: load current / time, y: Vout | hot ambient; max line | survives indefinitely; crowbar trips on sustained OV only | cycle-by-cycle limit for SMPS | §7.3.1/7.3.4, Fig 7.16/7.17/7.20, WILSON-299/300/303 |
| PSU efficiency and stress | efficiency vs load and line; reservoir voltage at no load/max line; regulator dissipation at worst point | x: load (%), y: efficiency / V / P | min/max line, no load to full load | reservoir < capacitor rating; regulator Tj within limit | linear worst at high line; SMPS worst at light load | §7.2.7–7.2.9, WILSON-284–289 |
| Mains harmonics | measure input-current harmonics to the 40th | x: harmonic order, y: current (A) with EN 61000-3-2 limit line | nominal line, full load | below limits (products >= 75 W or lighting, <= 16 A) | PFC boost pre-regulator if needed | §7.2.5, WILSON-281/282 |
| Battery runtime | discharge at the real load profile to the circuit's cut-off | x: time (h), y: cell voltage | low and high temperature | runtime >= spec; circuit works to N x end voltage | capacity falls at high C rate (15 Ah at 1C ~20 min) | §7.5, Fig 7.23–7.27, WILSON-308/309 |
| Conducted emissions | LISN (50 ohm // 50 uH) + CISPR 16-1 quasi-peak receiver (9 kHz BW, 0.15–30 MHz; 200 Hz BW below 150 kHz) | x: frequency (log), y: dBuV with limit line (Fig 8.4) | all operating modes/software states | below the current standard's limit with margin | pre-compliance continuously during the design | §8.2.2, Table 8.4, WILSON-331–333 |
| Radiated emissions | OATS or absorber-lined room, 3/10/30 m, 120 kHz BW QP, 30–1000 MHz | x: frequency, y: dBuV/m with limit line (Fig 8.5, normalised to 10 m) | antenna height/polarisation, cable layouts | below limit with margin | 1/d scaling 10 m -> 3 m only approximate | §8.2.2, WILSON-328/333/338 |
| RF immunity | radiated field 10 MHz – 1 GHz with defined performance criteria | x: frequency, y: pass/fail or degradation | >= 3 V/m (10 V/m preferred); pulsed near radars | no loss of function beyond the agreed criterion | define acceptable vs failure before testing | §8.1.1, WILSON-321/322/327 |
| Transient and ESD immunity | burst/surge on mains and I/O; ESD (150 pF/150 ohm) contact and air | x: test level (kV), y: upset/failure | >= 2 kV bursts (4–6 kV hi-rel); automotive load dump, field decay | no corruption at target level; watchdog recovery otherwise | Table 8.2 gives field rates by environment | §8.1.1, Fig 8.1–8.3, WILSON-323–326 |
| Shielding effectiveness | field or current-injection measurement across the enclosure; compare aperture/seam predictions | x: frequency, y: SE (dB) | all panels closed/opened, gaskets fitted | SE >= requirement; no resonant slots | apertures, not material, dominate (Fig 8.11/8.12) | §8.5, WILSON-345–348 |
| Filter insertion loss | measure the filter in the real circuit (not only 50 ohm catalogue data), incl. at peak line current | x: frequency (log), y: insertion loss (dB) | 150 kHz – 30 MHz+ ; load current incl. crest peaks | loss maintained; no collapse above ~10 MHz or from choke saturation | bond filter ground directly to chassis, separate I/O wiring | §8.6, WILSON-349–353 |
| Electrical safety | earth-bond test; creepage/clearance inspection; test finger and suspended-body probe; Y-capacitor leakage current; single-fault tests | pass/fail per item; temperatures during faults | short any component/terminal pair, stall motors, stop fans | earth < 0.5 ohm at 10 A for 1 min (EN 60065 example); no fire/shock hazard under single faults | markings and labels inspected | §9.1, WILSON-023/364–373 |
| Testability | ICT fault coverage; functional/ATE program validation on known-bad boards; boundary-scan interconnect test | fault list vs detected | seeded faults (wrong value, reversed polarity, bridges, opens) | all seeded faults detected; no false fails | bed-of-nails unsuitable for HF functional tests | §9.3, WILSON-380–387 |
| Early-life reliability | stress screening / burn-in of first batches; temperature cycling | x: time / cycles, y: cumulative failures | 160 h at 125 C typical; range-extreme cycling | failures traced to root cause; recurrent production faults fixed | not a substitute for good production | §9.4.3, WILSON-397 |
| Thermal | thermocouple on prototype heat source (or power resistor on a DC supply) with enclosure closed | x: time, y: temperature rise; steady-state dT vs power | max ambient, altitude, fan failure | Tj (from case/heatsink temperature + Rth_j-c) <= Tj_max; time constant ~ Rth*Ch | forced-air Rth vs velocity (Fig 9.15); transient curves for pulsed loads (Fig 9.14) | §9.5, WILSON-402–416 |

## 5. Pitfalls, failure modes, review checklist

### 5.1 EMC design checklist — transcribed in full from §8.8 (pp.364–365)
- Design for EMC from the beginning; know what performance you require.
- Select components and circuits with EMC in mind:
  - use slow and/or high-immunity logic
  - use good RF decoupling of power supplies
  - minimize signal bandwidths with RC filtering, maximize levels
  - use resistor buffering on long clock or data lines
  - incorporate a watchdog circuit on every microprocessor.
- PCB layout:
  - keep interference paths segregated from sensitive circuits
  - minimize ground inductance with an unbroken ground plane or ground grid
  - minimize loop areas in high-current or sensitive circuits
  - minimize track and component leadout lengths.
- Cables:
  - avoid parallel runs of signal and power cables
  - make sure that screens are 360-degree bonded through properly designed connectors
  - use twisted pair for high-speed data or high-current switching
  - run internal cables away from apertures in shielded enclosures
  - use multiple ground wires or planes in ribbon or flexi cables.
- Grounding:
  - ensure adequate bonding of screens, connectors, filters, cabinets, etc.
  - ensure that bonding methods will not deteriorate in adverse environments
  - mask paint from any intended conductive areas
  - keep earth straps short and wide: aim for a length/width ratio less than 3:1
  - route conductors to avoid common ground impedances.
- Filters:
  - apply a mains filter for both emissions and immunity: check its required current rating
  - use correct components and filter configuration for I/O lines
  - ensure a good interface ground return for each filter group
  - ensure that filter input and output terminal wiring is kept separate
  - apply filtering to interference sources, such as switches or motors.
- Shielding:
  - determine the type and extent of shielding required from the frequency range of interest
  - enclose particularly sensitive or noisy areas with extra internal shielding
  - avoid large or resonant apertures in the shield, or take measures to mitigate them
  - use conductive gaskets where long (> lambda/20) gaps or seams are unavoidable
  - test and evaluate for EMC continuously as the design progresses.

### 5.2 Design-for-production checklist — transcribed from §9.2.1 (pp.373–374)
**Sourcing**
- Have you involved purchasing staff as the design progressed?
- Are the parts available from several vendors or manufacturers wherever possible? Have you made extensive use of industry-standard devices?
- Where you have specified alternate sources, have you made sure that they are all compatible with the design?
- Have you made use of components which are already in use on other products?
- Have you specified close-tolerance components only where absolutely necessary?
- Where sole-sourced parts have to be used, do you have assurances from the vendor on price and lead time? How reliable are they? Have you checked that there is no "not recommended for new designs" warning on each part?
- Does your company vet vendors for quality control? If new vendors are added with this product, will they need to be vetted?

**Production**
- Have you involved production staff as the design progressed?
- Will the mechanical and electrical design work with all mechanical and electrical tolerances?
- Does the mechanical design allow the parts to be fitted together easily?
- Are components, especially polarized ones, all oriented in the same direction on the PCB for inspection and insertion?
- Are discrete components (resistors, capacitors, transistors) specified with identical pitch spacings and footprints as far as possible?
- Have you minimized wiring looms to front/rear panels and between PCBs, and used mass-termination (e.g. IDC) connections wherever possible?
- Have you modularized the design as far as possible to make maximum use of multiple identical units?
- Is the specified soldering and assembly process (wave, infra-red, auto-insert, pick-and-place) compatible with the manufacturing capability? Will the placement machines cope with all the SM components?
- If production calls for special procedures (potting, conformal coating) or special handling (MOSFETs, LEDs, batteries, relays), are production and stores staff conversant and able to implement them? Have you minimized the need for them?
- Do all PCBs have adequate solder mask, track and hole dimensions, clearances and legend for the process? Are test and assembly personnel conversant with the legend symbols?
- Are the assembly drawings clear and easy to follow?

**Testing and calibration**
- Have you involved test staff as the design progressed?
- Are all adjustment and test points clearly marked and easily accessible?
- Have you used easily set parts (DIL switches, linking connectors) in preference to solder-in wire links?
- Does the circuit allow selection of test signals, test subdivision and stimulus/response testing (including boundary scan) where necessary?
- If specifying ATE, does the layout allow access and tooling holes for bed-of-nails probing? Have you confirmed the validity of the ATE program and the functional test fixture?
- Have you written and validated a test software suite for microprocessor-based products?

**Installation**
- Is the product safe?
- Does the design have adequate EMC?
- Are the installation instructions or user handbook clear, correct and easy to follow?
- Do the installation requirements match the conditions on installation (environmental range, power supply, housing)?

### 5.3 PSU specification checklist (§7.1.3, p.296)
- Input: min/max voltage, max input current (surge and continuous), frequency range, permissible waveform distortion and interference generation.
- Efficiency over the entire range of load and line.
- Output: min/max voltage(s), min/max load current(s), ripple and noise, load and line regulation, transient response.
- Abnormal conditions: output overload; input spikes, surges, dips, interruptions; turn-on/turn-off behaviour (soft start, power-down interrupts).
- Mechanical: size, weight, thermal and environmental requirements, input/output connectors, screening.
- Safety approval requirements; cost and availability.

### 5.4 Pitfalls and failure modes (one line each)
**Grounding, wiring, transmission lines (Ch.1)**
- Treating any conductor that carries return current as "0 V" — voltage develops along it (Fig 1.1) (§1.1).
- Multiple chassis ground points: unpredictable circulating currents; faults that vanish when a screw is tightened; corrosion drift (§1.1.2).
- Aluminium panels joined without serrated washers/welding: oxide gives high, variable contact resistance (§1.1.3).
- High-current and logic returns sharing a wire: a 3.3 V rail drops to 3.05 V in the book's example; relays switching inject 0 V noise (§1.1.5).
- CAD auto-routing the input return to the nearest 0 V (§1.1.6).
- Uninsulated BNC shell plus coax outer to PCB 0 V forms a LF ground loop (§1.1.6).
- Input returned to an external ground: up to 50 V mains-frequency noise in series with the signal (§1.1.6).
- Local inter-board ground link that diverts supply return currents (§1.1.8).
- "Lifting the earth" of a Class I unit to break a ground loop — a safety violation (§1.1.10).
- Shield used as a signal return (except coax at RF); shield expected to stop magnetic pickup (§1.1.11).
- LF shield grounded at the end opposite the signal ground (§1.1.11).
- Low-noise cable's semiconducting layer not stripped back — near short circuit (§1.2.4).
- Mains in multicore, or power and signal in the same cable (§1.2.4).
- Screened audio cable used for RF (§1.2.5).
- Twisting pairs to fix common-mode capacitive coupling (needs a shield) (§1.2.6).
- EIA-232 over 16 m of multicore: 6.8 V crosstalk spikes (§1.2.7).
- Unterminated fast lines ringing beyond the noise-immunity band (§1.3.2).
- Using matched-line attenuation figures on a line with standing waves (§1.3.3).

**PCBs (Ch.2)**
- Out-of-date (0.3 mm minimum track) or over-enforced design rules (§2.2).
- Ignoring the 2:1 manufacturing spread of track resistance (§2.2.1).
- < 0.5 mm spacing on wave-soldered boards without resist — bridges (§2.2.1).
- Hole sizes not specified after plating; oversize capacitor/rectifier leads; multilayer holes cannot be drilled out (§2.2.2).
- X-Y auto-routing of analog boards (§2.2.3).
- Acute-angle track joins (etchant traps), tracks < 0.5 mm from the edge, unbalanced copper (warp) (§2.2.3).
- Plane slots under high-di/dt tracks; moats crossed by HF or low-level signals (§2.2.4).
- Surface-plane pads without thermal relief — unreliable joints (§2.2.4).
- Planes on the outside of dense 4-layer boards — loses interplane decoupling (§2.2.4).
- Screen-printed resist with fine tracks between pads — tracks left exposed (§2.2.6).
- Soldering connector pins before tightening the fixings (§2.2.7).
- Edge-connector fingers plated only on top — edge corrosion (§2.2.7).
- Wave-solder pad sizes used for reflow (§2.3.1).
- Large ceramic chips / LCCs directly on FR4 — thermal-cycle cracking (§2.3.1).
- Test probes on component leads — masks bad joints (§2.3.1).
- Legend printed over holes; inconsistent polarity markings (§2.3.3).
- Conformal coating over contaminated or damp boards (seals contamination in); testing after coating (§2.4.2).
- Potting that cracks poorly anchored tracks, making the unit unrepairable (§2.4.2).

**Passive components (Ch.3)**
- Assuming tolerances average out across a batch (§3.1.2).
- Dividing a 30 ppm/C reference with 200 ppm/C resistors (§3.1.3).
- Resistor power calculated at the nominal, not maximum, rail (12 V vs 17 V) (§3.1.4).
- Helical film or wirewound resistors in snubbers or pulse duty (§3.1.6).
- Exceeding LEV on high-value resistors (470 k 1206 limited to 85 mW) (§3.1.6).
- Two-terminal current sensing; unequal heating of sense-resistor terminations (thermocouple EMF) (§3.1.7).
- Rheostat without a wiper-to-end link — open circuit when the wiper lifts (§3.2.3).
- DC through a pot wiper; expecting infinite resolution; trimmer supplying the whole resistance (§3.2.3).
- Washing/soldering sealed electromechanical parts (§3.2.3).
- Plastic-film X capacitors across the mains — fire without blowing the fuse (§3.3.1).
- Z5U/Y5V anywhere but decoupling (11:1 value spread) (§3.3.2, §3.3.6).
- Electrolytics with no polarising voltage; long-stored product with high initial leakage (§3.3.4).
- Ignoring non-sinusoidal ripple correction and ESR rise below 0 C (§3.3.4).
- Heavy electrolytics hung on their leads under vibration (§3.3.4).
- Series capacitors without bleed resistors (§3.3.7).
- Tantalum decoupling at 10–20 MHz, far above its ~1 MHz SRF (§3.3.9).
- Winding directly on ferrite (self-capacitance up several times) (§3.4.3).
- Hard-encapsulated ferrite cores (shrinkage cracks) (§3.4.5).
- Unclamped relay/solenoid coils; transistor avalanche passing bench tests then failing in the field (§3.4.6).
- Crystal without drive-limiting resistor, or with logic routed near it (§3.5.2).
- 32.768 kHz tuning fork in a wide-temperature RTC (12 s/day at +85/-35 C) (§3.5.3).

**Discrete semiconductors (Ch.4)**
- VF assumed constant 0.6 V in linear circuits (-2 mV/C) (§4.1.1).
- 25 C leakage figures applied at high temperature; prototype parts unrepresentative of production batches (§4.1.3).
- Snap-off fast-recovery diodes as the dominant EMI source (§4.1.5).
- Zener operated on the knee; one high-voltage zener instead of series lower-voltage ones (§4.1.7).
- Triac with an inductive load and no snubber; triacs above ~40 A (§4.2.1).
- Pulse-transformer gate drive without a gate-cathode resistor — dV/dt false triggering (§4.2.3).
- Short trigger pulses early in the half cycle with light loads — no latching (§4.2.4).
- DC-coupled BJT chains without base-emitter resistors (§4.3.1).
- Circuit behaviour relying on hFE; trusting datasheet switching times from overdriven test circuits (§4.3.5–4.3.6).
- Reverse VBE beyond 7–10 V when speeding turn-off (§4.3.6).
- JFET bias not tolerating the 6:1 VGS(off) spread (§4.4.1).
- JFET high-Z input above the gate-current breakpoint (§4.4.3).
- Unprotected MOSFET gates floating in high-megohm circuits or unshorted during handling (§4.5.1).
- 10 V-characterised MOSFET driven from 5 V logic (§4.5.3).
- Drain transients reaching the gate through CGD (300 V -> 50 V) with a high-impedance driver (§4.5.3).
- Gate drive returned through the power source lead (§4.5.3).
- Heatsink sized using RDSon at 25 C (§4.5.5).
- IGBT at high switching frequency when hot (tail current) (§4.6.3).

**Analog ICs (Ch.5)**
- Assuming a parameter missing from a datasheet is good (§5.1).
- High-gain stage saturated by VOS x gain (TL072 x1000) (§5.2.1).
- Unequal source resistances on bipolar inputs (§5.2.2).
- Expecting anti-phase rail ripple to cancel via PSRR (§5.2.3).
- Input overvoltage with no series resistor — latch-up or phase reversal (§5.2.4).
- Output swing checked at nominal instead of minimum unregulated rail; "rail-to-rail" parts driving real loads (§5.2.5).
- Relying on high AOL close to the bandwidth limit (10% gain error a decade below) (§5.2.11).
- Choosing a low-en op-amp for a high-impedance circuit (§5.2.12).
- Commercial-grade parts outside their range without design margin; frozen moisture below 0 C (§5.2.14).
- Designing to one vendor's unspecified parameter (LM324 slew rate) (§5.2.15).
- Capacitance across RF of a current-feedback op-amp (§5.2.16).
- Comparator with a slow, high-impedance input — burst oscillation, multiple clock edges (§5.3.4).
- Comparator output track routed back past its inputs (§5.3.4).
- Unused comparators floating or with both inputs grounded (§5.3.5).
- Substituting a voltage reference without checking voltage, capacitor requirement and pinout (§5.4.2).
- Treating typical-value SPICE models as worst case (§5.5).

**Digital, interfaces, firmware (Ch.6)**
- Negative noise margin between families (LS-TTL -> HCMOS) (§6.1.1).
- High-Rout microcontroller pins driving noisy lines (§6.1.1).
- Ignoring input + trace capacitance in timing budgets (§6.1.2).
- Octal bus switching FF->00 corrupting the eighth bit via ground bounce (§6.1.3).
- Decoupling capacitor too far away — LC rings, worse than none (§6.1.4).
- Floating CMOS inputs (§6.1.5).
- Digital plane under the analog section; more than one AGND-DGND tie (§6.2.1).
- Analog signal driving an ordinary gate (§6.2.2).
- Edge-triggered counters fed from undebounced switches (§6.2.2).
- Off-board I/O without clamps/series resistors; rail unable to absorb clamp current (§6.2.3).
- Opto-coupler output tracks alongside inputs; no end-of-life CTR margin (§6.2.4).
- EIA-232 driven from +/-5 V rails; tri-stated or paralleled 232 drivers/receivers (§6.2.5).
- EIA-422 unterminated, or terminated at both ends (only the far end) (§6.2.5).
- EIA-485 bus with no failsafe bias (§6.2.6).
- Programmable timer as watchdog; watchdog to an interrupt; kick generated by address decode or inside tight loops (§6.4.2).
- RC power-on reset in professional equipment; firmware not tolerating brownout pulse trains (§6.4.3).
- Pull-ups on battery-backup-domain inputs — sneak battery drain (§6.4.3).
- Assuming peripheral control registers keep their initialised state (§6.5.3).
- Unused ROM left at FF (§6.5.2).

**Power supplies and batteries (Ch.7)**
- Inrush not tested at the voltage-peak switch-on phase (§7.2.4).
- NTC limiter still hot after a short interruption (§7.2.4).
- PTC thermistor used as the safety fuse (§7.2.4).
- Heavily over-rated PSU with poor light-load efficiency (§7.2.7).
- Dropout taken at Tj 25 C for hot operation (§7.2.8).
- 16 V reservoir capacitor in a 5 V linear supply (19 V off-load at high line) (§7.2.9).
- Reservoir chosen on ripple voltage only — ripple current 2–3x DC overheats it (§7.2.10).
- Loads grounded on the wrong side of the reservoir — hum (§7.2.12).
- Remote-sense leads without output-to-sense resistors (§7.2.11).
- Hold-up quoted at nominal line (§7.3.2).
- Crowbar without trigger delay (nuisance trips) or without upstream current limit (§7.3.4).
- Supervisor that stops working at low supply voltage (§7.3.5).
- "Designed to meet" safety claims taken as certification (§7.4.3).
- Series-cell reversal, copper battery contacts, recharging parallel cells, reverse insertion, lead-acid fitted long before despatch, NiMH trickle at 0.1 C, taper charging without a timer (§7.5).

**EMC (Ch.8)**
- EMC deferred to the end and fixed by brute-force shielding/filtering (§8.4).
- Two individually compliant products interfering in one rack (§8.1.2).
- Immunity testing without agreed pass/fail criteria (§8.1.1).
- Fast logic where slow would do; long clock lines without series resistors (§8.4.1).
- Long unterminated lines into CMOS inputs (§8.4.2).
- Painted/anodised seams and widely spaced fasteners (§8.5.2).
- Ventilation holes larger than 1.6 cm when 20 dB is needed at 1 GHz (§8.5.1).
- Filter with a long ground lead, or input and output wiring loomed together (§8.6.1).
- Mains filter rated on RMS current while crest-factor peaks saturate the choke (§8.6.2).
- Y capacitors exceeding the earth-leakage limit (§8.6.2).
- RF filter capacitors destroying the CM rejection of isolated inputs (§8.6.4).
- Filtered connectors with a poor case ground — designed-in crosstalk (§8.6.4).
- Pigtail shield terminations (~40 dB worse above 3 MHz) (§8.7).
- IDC connectors on unfiltered external lines (§8.7).

**Product design (Ch.9)**
- Ventilation openings admitting the test finger or suspended bodies (§9.1.3).
- Hygroscopic insulating materials (§9.1.3).
- Earth contact not first-make/last-break (§9.1.3).
- Unlabelled fuse ratings (§9.1.4).
- ESD-unsafe prototyping lab — time lost to static-damaged parts (§9.2.2).
- Bed-of-nails used for HF or high-speed functional testing (§9.3.4).
- Long test tracks run across the board (§9.3.4).
- Reliability figure quoted without failure definition, period and environment (§9.4.1).
- MTBF prediction from obsolete data treated as a life prediction (§9.4.4).
- Redundancy without failed-element annunciation (§9.4.3).
- Burn-in used as a crutch for poor production (§9.4.3).
- Designing to a power device's 25 C-case power rating (IRF640: 125 W rated, 35 W usable at 70 C) (§9.5.1).
- Horizontal fins (-30%) and no altitude derating (§9.5.2).
- Oversize or chamfered mounting holes, excess grease, unfilled nylon bushes, soldering before fastening, bent metal-can leads (§9.5.3).
- Heatsink at the air inlet; solid screens blocking airflow over vertical boards (§9.5.4).

## 6. Standards referenced

| Standard | Edition / year (as given) | Clause / table / value cited | Governs | Page |
|---|---|---|---|---|
| EN 60065 (IEC 60065; BS EN 60065) | EN 60065:1994 | earth continuity < 0.5 ohm at 10 A for 1 min; creepage/clearance 0.5 mm < 34 V -> 3 mm at 354 V; PCB 0.5 mm <= 124 V -> 3 mm at 1240 V | Safety of mains-operated audio/video/household electronic apparatus; LVD harmonized | p.22, 369, 371, App. p.404 |
| EN 60950-1 (IEC 60950-1; BS EN 60950) | EN 60950-1:2002 | default safety standard quoted for off-the-shelf PSUs | Safety of information technology equipment; LVD harmonized | p.321, 369, App. p.404 |
| Low Voltage Directive | 73/23/EEC | 50–1000 V AC, 75–1500 V DC | EU electrical safety; presumption via harmonized standards | p.321, 368 |
| EMC Directive (EU) | – | essential requirements (emission, immunity); DoC or technical construction file; OJEU-listed EN standards only | EU EMC compliance | p.302, 340–342 |
| Batteries and Accumulators Directive | 91/157/EEC (update pending) | mercury cells banned; collection/recycling targets | EU batteries | p.325 |
| EN 61000-3-2 | 2000 | harmonics to 40th (2 kHz), <= 16 A, < 75 W non-lighting exempt | Mains harmonic current emissions | p.303 |
| CISPR 16-1 | – | Table 8.4 QP receiver; artificial mains network 50 ohm // 50 uH; coupling clamp | EMC measuring apparatus | p.342–345 |
| EN 55011 / CISPR 11 / FCC Part 18 | – | Table 8.3 | Emissions: industrial, scientific & medical equipment | p.342 |
| EN 55014-1 / CISPR 14-1 (BS EN 55014) | – | Table 8.3 | Emissions: household appliances, electric tools | p.342, App. p.404 |
| EN 55014-2 / CISPR 14-2 | – | Table 8.3 | Immunity: household appliances (RFI, ESD, transient) | p.342, 344 |
| EN 55015 / CISPR 15 | – | Table 8.3 | Emissions: lighting equipment | p.342 |
| EN 61547 / IEC 61547 | – | Table 8.3 | Immunity: lighting equipment | p.342 |
| EN 55013 / CISPR 13 | – | Table 8.3 | Emissions: radio & TV receivers | p.342 |
| EN 55020 / CISPR 20 | – | Table 8.3 (incl. antenna terminals) | Immunity: radio & TV receivers | p.342, 344 |
| EN 55022 / CISPR 22 (BS EN 55022) / FCC Part 15 | – | Table 8.3 | Emissions: information technology equipment | p.342, App. p.404 |
| EN 55024 / CISPR 24 | – | Table 8.3 | Immunity: information technology equipment | p.342, 344 |
| FCC Rules Part 15 subpart J | – | digital device > 9 kHz timing; class A / class B; certification (PCs) vs verification | US emissions | p.340 |
| C-tick | – | declaration of compliance | Australia/New Zealand EMC | p.340 |
| VCCI | – | quasi-voluntary ITE emission limits | Japan EMC | p.340 |
| IEC 61000-4-2 | – | Fig 8.3 electrostatic charging voltages | ESD immunity | p.339 |
| EUROCAE WG33 user's guide | – | aircraft RF environment, 17 kV/m worst case (2–4 GHz) | Civil aircraft HIRF protection | p.336 |
| BS 613 | – | max Y capacitor 0.005 uF (class I, plug and socket) | Components and filter units for EMI suppression | p.359, App. p.403 |
| IEC 60479 | – | < 0.5 mA harmless; 50–500 mA potentially fatal | Effects of current through the human body | p.369, App. p.405 |
| IEC 60536 (BS 2754) | – | classes 0, I, II, III | Classification of equipment for electric-shock protection | p.370, App. p.404 |
| IEC 60127 (BS EN 60127) | – | rated current ~60% of minimum fusing current | Miniature fuses | p.299, App. p.404 |
| UL 198G | – | rated current 85–90% of minimum fusing current | Fuses (US) | p.299 |
| IEC 60269 (BS EN 60269; see BS 88) | – | – | Low-voltage fuses | App. p.404 |
| BS 6500 | – | Table 1.5 (current, mV/A/m, supportable mass) | Flexible cords up to 300/500 V for appliances | p.24, App. p.404 |
| IEC 60227 / IEC 60245 | – | harmonized cable codes (CENELEC) | PVC / rubber insulated mains cables | p.24 |
| IEE Wiring Regulations | 17th edition | source of Table 1.5 ratings and correction factors | Cable current ratings (UK) | p.25 |
| CEE-22 | 6 A | universal mains inlet; earth first-make/last-break example | Appliance inlet connectors | p.25, 372 |
| UL / CSA approvals | – | 105 C PVC wire; mains cable sets differ from EU | North American cable/equipment approvals | p.23, 25, 321 |
| BS 4808 (related IEC 60189) | – | Table 1.3; PVC 85 C | PVC equipment wires and cables | p.23–24, App. p.404 |
| BS EN 13602 | – | – | Drawn round copper wire for electrical conductors (tinned wire) | p.22, App. p.404 |
| BS EN 60182 / IEC 60182-1 (IEC 60851) | – | Grade 1 / Grade 2 enamel | Enamelled winding-wire dimensions | p.22, App. p.404 |
| ISO/IEC 11801, TIA/EIA-568, EN 50173 | – | Table 1.7 Cat 3/5/5e/6 | Structured (generic) cabling | p.26–27, 261 |
| MIL-C-17 / BS 2316 / IEC 60096 | – | Table 1.8 (RG/U and UR-M series) | RF coaxial cables | p.29, App. p.403 |
| EIA-232F (RS-232C 1969; CCITT V.24/V.28; ISO IS2110) | – | Table 6.2; 2500 pF; 30 V/us; 20 kb/s | Unbalanced serial interface | p.32, 254–257 |
| EIA-423 | – | not directly compatible with 232 | Unbalanced interface | p.257 |
| EIA-422 (RS-422); EIA-449, EIA-530 | – | Table 6.2; 100 ohm far-end termination; 10 receivers | Balanced multidrop interface (449/530 add mechanics/functions) | p.33, 257 |
| EIA-485 (HVD-SCSI basis) | – | Table 6.2; 32 UL; 120 ohm both ends; failsafe | Balanced multipoint half-duplex interface | p.258–259 |
| ISO 11898 (CAN 2.0A 1993; 2.0B 1995 amendment); ISO 11519 | 1993 / 1995 | 1 Mb/s, 40 m, 30 nodes, 0.3 m stubs; 125 kb/s (11519) | Controller Area Network physical/data-link | p.259 |
| USB 1.1 / 2.0 / 3.0 | – | 12/1.5 Mb/s; 480 Mb/s; 5 Gbit/s; 90 ohm cable | Universal Serial Bus | p.259–260 |
| IEEE 802.3 (DIX 1980; Fast Ethernet 1995; Gigabit 1999); IEEE 802.3.1-2011 | – | 10BaseT 2.5 V, 100BaseT 1 V differential | Ethernet (802.3.1: MIB definitions) | p.260–261, App. p.406 |
| PCI Express 1/2/3 | – | 2.0: 5 GT/s; 3.0: 8 GT/s | Serial expansion interconnect | p.261–262 |
| BS 6221 Part 3 (related IEC 60326) | 1984 | Fig 2.11 safe track currents; design practice | Printed wiring boards: design and use | p.55, 57, App. p.404 |
| NEMA FR4 | – | flame-retardant epoxy woven glass | PCB laminate grade | p.48 |
| DIN 41612 | – | Eurocard connectors; H15 for PSU cassettes with leading earth | Two-part PCB connectors | p.67, 320 |
| MIL-C-24308 | – | subminiature D | External data connectors | p.67 |
| IEC 60063 (BS 2488) | – | Table 3.3 E6–E96 | Preferred number series for resistors and capacitors | p.95–96, App. p.403 |
| IEC 60062 (BS EN 60062) | – | – | Marking codes for resistors and capacitors | App. p.404 |
| EIA 198-1 / -2 / -3 | – | Table 3.5 Class 2 temperature codes | Ceramic dielectric capacitors | p.113 |
| IEC 60384 (BS QC 300XXX) | – | – | Fixed capacitors: harmonized quality assessment | App. p.405 |
| IEC 60115 (BS 9940, QC 400XXX) | – | – | Fixed resistors: harmonized quality assessment | App. p.405 |
| IEC 60431 (BS EN 60431) | – | RM cores | Dimensions of square (RM) ferrite cores | p.124, App. p.404 |
| IEC 60647 | – | EC cores | Ferrite cores for power supplies | App. p.405 |
| IEEE Std 389 | 1996 (leakage inductance); 1979 (winding capacitance) | shorted-secondary and resonance methods | Testing electronic transformers and inductors | p.130–131 |
| IEEE 295 | 1969 | – | Electronics power transformers | App. p.406 |
| IEEE 388 | 1992 | – | Transformers and inductors in electronic power conversion | App. p.406 |
| IEEE 393 | 1991 | – | Test procedures for magnetic cores | App. p.406 |
| IEEE 484 | 2002 | – | Installation of vented lead-acid batteries (stationary) | App. p.406 |
| IEEE 937 | 2007 | – | Lead-acid batteries for PV systems | App. p.406 |
| IEEE 1159 | 2009 | – | Monitoring electric power quality | App. p.406 |
| IEEE 1515 | 2000 | – | Electronic power subsystems: parameter definitions, test conditions/methods | App. p.406 |
| IEEE 1573 | 2003 | – | Electronic power subsystems: parameters, interfaces, elements, performance | App. p.406 |
| IEEE 139 | 1988 | – | RF emission measurement of ISM equipment on user premises | App. p.406 |
| IEEE 644 | 1994 | – | Measurement of power-frequency E and H fields from AC lines | App. p.406 |
| IEEE 1528 | 2003 | – | Peak spatial-average SAR in the human head from wireless devices | App. p.406 |
| IEEE 1775 | 2010 | – | Power-line communication equipment EMC requirements/tests | App. p.407 |
| ANSI C63.4 | 1991 | 9 kHz – 40 GHz | Radio-noise emission measurement methods | App. p.407 |
| IEC 60285 (BS EN 60285) | – | – | Sealed NiCd cylindrical rechargeable cells | App. p.404 |
| IEC 61951 (BS EN 61951; formerly IEC 60509) | – | – | Secondary cells with alkaline/non-acid electrolyte | App. p.405 |
| IEC 60529 (BS EN 60529) | – | IP code | Degrees of protection by enclosures | App. p.404 |
| IEC 60068 (BS EN 60068) | – | – | Environmental testing | App. p.404 |
| IEC 60617 (BS EN 60617) | – | – | Graphical symbols for diagrams | App. p.404 |
| BS 5783 | 1987 | Fig 9.4 static-safe workshop layout | Handling of electrostatic sensitive devices | p.376, App. p.404 |
| BS CECC 00015 Part 1 | 1991 | – | Code of practice for handling electrostatic-sensitive devices | p.376 |
| IEEE 1149.1 (JTAG) | 1990; 1149.1a-1993; 1149.1b-1994; 1149.1-2001 | TAP: TCK, TDI, TDO, TMS; boundary-scan cells; bypass register | Boundary-scan test | p.379–381 |
| IEEE-488 | – | – | Instrument bus for ATE | p.378 |
| CECC harmonized quality assessment (supersedes BS 9000) | – | generic specifications | Assessed-quality electronic components (Europe) | p.387 |
| MIL-HDBK-217F Notice 2 | 217F-2 | failure-rate models and tables | Reliability prediction (US DoD) | p.388 |
| British Telecom HRD4 | – | – | Failure-rate data (telecoms) | p.388 |

## 7. Process / lifecycle guidance

| Stage | Activity | Deliverable | Exit criterion | Source |
|---|---|---|---|---|
| Specification | Define the full PSU specification (input, efficiency, outputs, abnormal conditions, mechanical, safety, cost); EMC performance required and immunity pass/fail criteria; safety class and target standards; reliability definition (failure, period, environment); test strategy (ICT / functional / ATE / boundary scan); hardware platform choice | Requirements incl. PSU checklist (§5.3), EMC criteria, safety class, reliability spec, test strategy | All items quantified and agreed before design starts | §7.1.3, §8.1.1, §8.8, §9.1.1, §9.3, §9.4.1, §6.6 |
| Make/buy | Off-the-shelf PSU unless volume or custom needs justify in-house (~GBP 1/W, 50–200 W); prefer "certified to" safety approvals; bend circuit to standard rails | PSU sourcing decision | Bought unit's safety/EMC status confirmed | §7.1.4, §7.4.3 |
| Component selection | Industry-standard, multi-sourced parts; relaxed grades; temperature grade vs ambient; no NRND parts; tantalum supply risk; assessed-quality (CECC) parts where early-failure cost is high | Approved parts list | Sourcing checklist (§5.2) all "yes" | §5.2.14–5.2.15, §4.3.7, §3.3.5, §9.2.1, §9.4.3 |
| Circuit design | Worst-case tolerance analysis (never statistical averaging for critical paths), Monte Carlo, derating (P <= 0.5 rated, capacitor V <= 0.5 rated), leakage at temperature, SPICE to ~+/-20% then breadboard critical functions, watchdog/supervisor/defensive firmware | Calculations, simulation results, derating sheet | Every part within derated rating at worst case; design review passed | §3.1, §5.5, §6.4–6.5, §9.4.3 |
| Layout | Company design rules based on BS 6221 Pt 3 and fabricator capability; grounding scheme (return paths, single AGND-DGND tie); decoupling; DFT (test pads, tooling holes, JTAG); thermal placement; EMC layout checklist | Layout database, DRC report, fab package (copper, mask, legend/peelable/carbon, drill, drawings, materials, finish, layer build, test requirements) | DRC clean against fabricator limits; boilerplate spec applied | §2.2, §2.5, §6.1.4, §6.2.1, §9.3.4, §9.5.4, §8.8 |
| Design review | Peer critique by reviewers unconnected with the project (concept, cost, tolerances, ratings, assumptions) | Review record | No open actions | §9.4.5 |
| Prototype PCBs | Prototype service (4–5 days, 2–5x production price); panel pooling | Prototype boards | Boards received matching fab package | §2.1.4, §2.5.2 |
| Prototype evaluation | Continuous EMC pre-compliance; HF scope/spectrum-analyser scan of every gain stage; worst-case parts (max VOS, leakage from several batches); inrush at many switch-on phases; watchdog burst testing; thermal thermocouple measurements; ESD-safe lab | Evaluation reports and plots (§4) | All §4 pass criteria met | §8.8, §8.4.2, §5.2.1, §4.1.3, §7.2.4, §6.4.2, §9.5.2, §9.2.2 |
| Compliance | EMC: self-declare against OJEU-listed EN standards (or technical construction file); FCC class A/B, C-tick, VCCI as markets require; harmonics EN 61000-3-2; safety: LVD via EN 60065 / EN 60950-1, markings, single-fault tests | Declarations of conformity, test reports, certificates | Mandatory markets covered | §8.2, §7.2.5, §9.1 |
| Production introduction | DFM production and test checklists; ICT/functional/ATE fixtures and programs validated; static-safe work areas; conformal coating only if unavoidable (clean, bake 2 h at 65–70 C, 2–3 coats, test first); stress screening/burn-in of first batches (e.g. 160 h at 125 C) | Validated test programs, work instructions | First batches free of recurrent faults | §9.2, §9.3, §2.4.2, §9.4.3 |
| Installation and field | Installation checklist; clear instructions; logging of up-time/down-time to validate MTBF/MTTR and availability; battery stock rotation and top-up charging; fit lead-acid batteries at despatch | Field data, availability records | Availability meets requirement | §9.2.1, §9.4.1, §7.5.1, §7.5.3 |

## 8. Coverage log

**Line ranges read (in order, Read tool):** 1–299, 300–749, 750–1199, 1200–1579 (an initial 450-line request over this span was refused for size and re-read with a smaller limit), 1580–1919, 1920–2249, 2250–2579, 2580–2909, 2910–3239, 3240–3569, 3570–3829, 3830–4089, 4090–4349, 4350–4609, 4610–4869, 4870–5128, 5129–5378, 5379–5628, 5629–5878, 5879–6128, 6129–6248 (end of bibliography, start of index), 6840–6876 (end-of-file spot check). Every line from 1 to 6248 was read.

**Skipped:** lines 6249–6839, the body of the index (pp.413–439) — index pages are skippable per the brief. The start and end were spot-checked and contain no technical content. The bibliography (pp.409–412) was read but not extracted, as it is a reading list only.

**Output:** 418 design rules (WILSON-001 … WILSON-418; ids unique and contiguous, verified), 65 transcribed table/formula blocks, 115 mechanizable checks, 48 verification procedures, the full EMC (§8.8) and DFM (§9.2.1) checklists, 153 pitfalls, and 81 standards entries.

**Extraction limitations:**
- Figures are absent from the text. Graph-only data is referenced by caption and marked "graph"/medium, not digitised. This covers Fig 2.10/2.11 (track resistance and safe current), 3.15, 3.24/3.25 (capacitor impedance), 3.45 (AT-cut curves), 4.5, 4.10, 4.13, 4.22, 4.23, 5.8–5.19, 6.4, 7.2, 7.4 (fuse curves), 7.23–7.27 (battery discharge), 8.1, 8.3, 8.4/8.5 (conducted/radiated emission limit curves), 8.9, 8.11/8.12 (shielding), 9.9, 9.14 (transient thermal impedance) and 9.15.
- OCR renders micro as "m", ohm as "U", minus as "À" and times as "Â". Units were converted using context, and genuinely ambiguous prefixes are flagged as "printed" (WILSON-120, 131, 157, 179, 200, 230, 255; Table 5.2 currents).
- Several flattened tables were reconstructed and flagged conf medium in place: Table 1.7 (return-loss and capacitance-unbalance columns), Table 3.1 (cost column), Table 3.4 (WV/tolerance alignment), Table 7.1 (2CR11108 row), Table 9.5 (column mapping).
- Some formulas were partly garbled in the print and are flagged: the skin-effect factor (reconstructed as Rac/Rdc ~ (d/D + 1)/4); the proximity-effect Gr factor (not recoverable); the sign of the hysteresis threshold "(1 + a)"; the second-order sigma-delta noise expression; and the radiation formula printed with dT^4 in W/cm^2.
- The book prints no IEC 60950/62368/61010 creepage/clearance tables, no IPC-2221-style track-current table and no component derating table. Only the EN 60065 anchor values, the 1 mm per 200 V rule, the BS 6221 graph reference and qualitative derating rules exist, and nothing was invented for the missing tables. Interpolation between the EN 60065 anchors is labelled a screening assumption (conf low) in CHECK-creepage-clearance.
- The EMC emission limit values appear only as graphs, with the book's own warning to consult current specifications, so they were not transcribed.
- The book is the 3rd edition, copyright 2012 (the source filename says 2011). Prices are UK pence/GBP at the time of writing (coax costs are 1990 averages).
- Section 3 margin conventions and a few pass thresholds are screening choices where the book is qualitative; each is marked conf low in place.

