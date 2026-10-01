# PCB Design Guide to Via and Trace Currents and Temperatures — Anvil rulebook

## 0. Citation

D. Brooks with J. Adam, *PCB Design Guide to Via and Trace Currents and Temperatures*, 1st ed. Norwood, MA: Artech House, 2021. ISBN 13: 978-1-63081-860-9.

Chapters covered by THIS extraction: Preface, Technical Note (TRM), Ch.1 (Introduction/History), Ch.2 (Materials), Ch.3 (Resistivity & Resistance), Ch.4 (Trace Heating & Cooling), Ch.5 (IPC Curves), Ch.6 (Thermal Simulations — modeling), Ch.7 (Thermal Simulations — sensitivities), Ch.8 (Via Temperatures), Ch.9 (Current Densities in Vias), Ch.10 (Thinking Outside the Box), Ch.11 (Fusing Currents: Background), Ch.12 (Fusing Currents: Analyses), Ch.13 (Do Traces Heat Uniformly?), Ch.14 (Stop Thinking about Current Density), Ch.15 (AC Currents), Ch.16 (Industrial CT Scanning), Appendices A–I.

Chapters NOT read: none intentionally; see §8 Coverage log for skipped material (index, long derivation steps in Appendix G).

Unit conventions used below (author's): trace width W and thickness Th in mils unless stated; current I (the book writes C in Ch.5 fits) in amperes; ΔT in °C above ambient; resistivity ρ in μΩ·cm (book writes "mohm-cm" for micro-ohm-cm due to OCR of μ) or μΩ·in; 1 oz copper ≈ 1.3 mil (book also uses 1.2–1.38 mil, see BROOKS-011).

## 1. Design rules

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| BROOKS-001 | current-carrying | Quick estimate of trace DC resistance at 20°C | R = 0.68 * L / (W * Th); R [ohm], L [inch], W [mil], Th [mil] | L, W, Th | Copper trace, 20°C; use as first-pass before voltage-drop calc | calc | Preface p.xvi | high |
| BROOKS-002 | current-carrying | Trace resistance temperature correction (rule of thumb) | R increases ≈ 4.0% per 10°C rise (i.e. ≈0.004/°C) | ΔT | Copper traces, moderate temperatures | calc | Preface p.xvi | high |
| BROOKS-003 | process | Trace-sizing workflow: (1) circuit designer supplies max current (and duty cycle); (2) system engineer sets max allowable trace ΔT as a policy value; (3) pick size from charts (worst case); (4) compute R; (5) compute V-drop = I*R; (6) keep, enlarge, or shrink (shrink only with simulation evidence) | — | I_max, duty, ΔT_limit | Every power trace; ΔT limit is application/market dependent (medical, space vs consumer) | review | Preface p.xv–xvi | high |
| BROOKS-004 | via | Via temperature is determined primarily by the parent trace temperature, not by via current or via dimensions | T_via ≈ T_trace (parent) | T_trace | Via connecting traces of the same width/thickness; see BROOKS-1xx (Ch.8) for limits | sim | Preface p.xiv; Ch.8 | high |
| BROOKS-005 | current-carrying | For AC / pulsed / non-DC current, size the trace on the RMS current | I_design = I_rms | waveform | Frequencies where thermal time constant >> period; skin-effect resistance correction separate (out of scope) | calc | Preface p.xv; Ch.15 | high |
| BROOKS-006 | current-carrying | Do not size traces or vias by current density; current density is a derived variable (I/A) with no unique relation to temperature | — | I, W, Th | All traces; form factor (W vs Th) matters independently | review | Preface p.xv; §4.6; Ch.14 | high |
| BROOKS-007 | reliability | Any board on which a trace has been subjected to a very high (fusing-range) temperature is to be treated as damaged and replaced | — | event log | After overload/fusing events | inspect | Preface p.xv | high |
| BROOKS-008 | process | Charts/equations give worst-case (conservative) trace sizes; when precision or complex surroundings (planes, adjacent traces, enclosure) matter, a 3-D thermal field solver is required | — | — | Analogy: impedance formulas vs field solvers | review | Preface p.xv; §1.2 p.5 | high |
| BROOKS-009 | current-carrying | IPC-2152 (2009) external-trace data give allowable currents ≈25% lower than the older IPC-2221 / MIL-STD-275 curves for the same ΔT | I_2152_ext ≈ 0.75 * I_2221_ext | I_2221 | Legacy designs sized with IPC-2221 external curves | calc | §1.2 p.2 | high |
| BROOKS-010 | current-carrying | Pre-2009 "internal trace" charts were simply the external chart derated by a factor of 2; this was wrong — internal traces run cooler than external traces because the dielectric conducts heat better than air | I_internal_allowed ≥ I_external_allowed (for equal ΔT) | layer | FR4-class dielectrics; still air; no vacuum | sim | §1.2 p.2; §4.4 p.30; §5.4.3 p.47 | high |
| BROOKS-011 | materials | Nominal copper thickness conventions and tolerance: 0.5 oz = 0.60–0.65 mil (0.015–0.017 mm); 1 oz = 1.2–1.3 mil (0.03–0.034 mm), often quoted 0.035 mm = 1.38 mil or 1.35 mil (0.034 mm); IPC allows 10% tolerance on trace thickness | Th_1oz ≈ 1.3 mil (book default); tolerance ±10% | copper weight | All thermal calcs; use consistent value | calc | §1.3 p.5; §5.4 footnote p.50 | high |
| BROOKS-012 | materials | Foil resistivity differs by type: electrodeposited (ED) foil (after bonding to laminate) 1.62–1.66 μΩ·cm; rolled foil 1.74–1.78 μΩ·cm | ρ_ED = 1.62–1.66 μΩ·cm; ρ_rolled = 1.74–1.78 μΩ·cm | foil type | Rolled preferred for high-frequency (roughness); ED for bonded assemblies | calc | §2.3.1 p.10 | high |
| BROOKS-013 | materials | Copper foil thickness is held within 10% or better by the foil process | tol_foil ≤ ±10% | — | Base foil only (not plating) | inspect | §2.3.1 p.10 | high |
| BROOKS-014 | fab | Plated copper thickness varies across a panel by up to 50% (anecdotally up to 100%); even with fabricator countermeasures variations of 20% still occur — use worst-case (thin) thickness for outer-layer trace resistance/heating | Th_plated_min ≈ 0.5–0.8 × nominal | Th_nom | Outer layers (pattern- or panel-plated); inner layers use foil tolerance | inspect | §2.3.2 p.11; §3.5 p.24 | high |
| BROOKS-015 | materials | Copper resistivity values: pure copper 1.68 μΩ·cm; annealed copper 1.72 μΩ·cm; UNS "coppers" C10100–C15999 ≥99.3% purity; high-copper alloys C16000–C19999 >96%; random UNS C10100–C14500 alloys range 1.69–1.86 μΩ·cm | ρ_Cu = 1.68–1.72 μΩ·cm (nominal); alloy range 1.69–1.86 | alloy | 20°C | calc | §2.3.3 p.12 | high |
| BROOKS-016 | materials | Impurities can change copper resistivity by ~25% even at small concentrations | ρ uncertainty up to +25% | — | Contaminated/plated copper | calc | §2.3.3 p.12 | high |
| BROOKS-017 | thermal | Dielectric thermal conductivity is anisotropic: in-plane Tcon-x typically 0.5 or 0.6 W/m·K, through-plane Tcon-z 0.3 to 0.5 W/m·K; copper 386 W/m·K. Datasheets often omit Tcon or don't say which direction | k_xy ≈ 0.5–0.6; k_z ≈ 0.3–0.5 W/m·K; k_Cu = 386 W/m·K | material | FR4-class laminates | calc | §2.4.1 p.13 | high |
| BROOKS-018 | materials | Only Tcon matters at normal trace temperatures; Tg, Td and T260/T288 become relevant when trace temperature exceeds ~100°C | T_trace > 100°C → check Tg, Td, T260/T288 | T_trace | — | review | §2.4 p.13 | high |
| BROOKS-019 | materials | Decomposition temperature Td (5% mass loss) is irreversible; typical Td ≈ 350°C | T_trace < Td (≈350°C typical) | material | Also an assembly (wave solder) consideration | review | §2.4.3 p.14 | high |
| BROOKS-020 | materials | Time-to-delamination T260/T288 (IPC-TM-650 2.4.24.1): ramp 10°C/min to 260°C (or 288°C), hold; time to event ranges from a few minutes to over an hour. Delamination disrupts conductive cooling → thermal runaway → conductor melt | if T_trace ≥ 260°C: t_survive ≤ T260 rating | material T260 | Traces with supplemental cooling that could be lost | review | §2.4.4 p.14 | high |
| BROOKS-021 | materials | Above Tg, CTE increases and z-axis expansion stresses vias (via conductivity can be lost in extreme cases); effect reversible, boards usable above Tg but Tcon changes | — | Tg | High-temperature traces near vias | review | §2.4.2 p.13–14 | medium |
| BROOKS-022 | materials | Element resistivities at 20°C: silver 1.6e-8 Ω·m (0.63 μΩ·in); copper 1.7e-8 Ω·m (0.67 μΩ·in); gold 2.2e-8 Ω·m (0.87 μΩ·in); silicon 6.4e2 Ω·m; glass 1e9–1e15 Ω·m | ρ_Cu(20°C) = 0.67 μΩ·in = 1.7 μΩ·cm | — | 20°C, pure elements | calc | §3.2 p.19–20 | high |
| BROOKS-023 | current-carrying | Trace resistance from resistivity: R = ρ * L / A, A = W * Th. Worked example: ρ = 0.67 μΩ·in, Th = 0.00065 in (0.5 oz), W = 0.1 in, L = 6 in → R = 0.0618 Ω | R = (ρ/A)*L | ρ, L, W, Th | Uniform cross-section, single temperature | calc | §3.3 eq.(3.1),(3.1a) p.20 | high |
| BROOKS-024 | current-carrying | Resistance/resistivity vs temperature: R(T) = R(To) * (1 + αo*(T − To)); ρ(T) = ρ(To) * (1 + αo*(T − To)); αo is the coefficient at reference To (commonly 20°C) | eq.(3.5),(3.6) | R(To), αo, T, To | αo itself varies with T (see Table 3.1) | calc | §3.4 p.22 | high |
| BROOKS-025 | materials | Copper thermal coefficient of resistivity: α ≈ 0.0040 /°C (referenced to 20°C) for 27–127°C, rising slowly to 0.0048 /°C at 1084°C (Matula data, ≥99.99% Cu) | α20 = 0.0040 /°C (use 0.0041–0.0048 for T > 200°C) | T | See Table 3.1 in §2 | calc | §3.4 Table 3.1 p.23 | high |
| BROOKS-026 | materials | Copper melts at 1084°C; resistivity 10.17 μΩ·cm solid at melting point and 21.01 μΩ·cm liquid (≈6× the 20°C value / ≈2× jump on melting) | ρ(1084°C, solid) = 10.17; ρ(1084°C, liquid) = 21.01 μΩ·cm | — | Fusing analyses | calc | §3.4 Table 3.1 p.23 | high |
| BROOKS-027 | test | Trace dimensions for resistivity/resistance verification must be measured, not taken from nominal: plating over foil varies thickness up to 50%+; photo-etch width tolerance at least 1–2 mils; microsection measurement tolerance ≈0.1 mil (10–15% of a 0.5-oz thickness) | width tol ≥ ±1–2 mil; Th tol up to 50%; microsection ±0.1 mil | — | Any resistivity back-calculation | measure | §3.5 p.24–25 | high |
| BROOKS-028 | materials | Resistivity of plated copper ≈ that of pure copper (test-board result) | ρ_plating ≈ 1.68–1.72 μΩ·cm | — | Prototron test boards; details in Appendix B | measure | §3.5.1 p.25; App. B | high |
| BROOKS-029 | thermal | Trace heating model: P = I²R (W); steady-state ΔT reached when heating = cooling; ΔT ∝ I²R / (W + Th) (cooling scales with surface ~ W + Th) | ΔT ∝ I²R/(W+Th) | I, R, W, Th | Basis for the IPC curve fits in Ch.5 | calc | §4.3 eq.(4.2); §4.5 eq.(4.3) p.28,32 | high |
| BROOKS-030 | thermal | Typical dielectric thermal conductivity 0.3–0.8 W/m·K; ceramic-filled materials much higher. Higher k → cooler trace | k_diel = 0.3–0.8 W/m·K | material | — | calc | §4.4 p.29–30 | high |
| BROOKS-031 | thermal | Convection and radiation contribute approximately equally to surface cooling under lab conditions; in vacuum surface traces cool ≈50% less effectively (radiation only) → vacuum traces run hotter | HTC_vacuum ≈ 0.5 * HTC_air | environment | Space / vacuum applications; confirmed by IPC vacuum data and simulation | sim | §4.4 p.30 | high |
| BROOKS-032 | thermal | Heat-transfer coefficient (HTC) to air depends on trace-air ΔT and air velocity; experimental data must be taken in still air after temperature stabilizes | — | — | IPC-style measurements | measure | §4.4 p.30 | high |
| BROOKS-033 | thermal | Narrow traces cool relatively better than wide ones (shorter conduction path out from under the trace); simulated thermal plume at ~70°C extends ≈10 mm each side of a 200-mil (5-mm) trace (≈4× W) and ≈7.5 mm each side of a 20-mil (0.5-mm) trace (≈30× W) | plume ≈ 7.5–10 mm each side | W | Steady state; sets minimum spacing for "thermally independent" traces | sim | §4.4.1 p.30–32, Fig.4.4 | medium (graph) |
| BROOKS-034 | test | IPC standard test trace (IPC-TM-650 2.5.4.1a): 12 in end-to-end, 200-mil diameter end pads, sense pads 20 mil × 400 mil located 3 in from each end, 6-in active length, #26 AWG magnet-wire sense leads; board horizontal in still air | L_active = 6 in | — | Current/temperature characterization | measure | §4.7.1 p.33, Fig.4.5; §5.3 p.42 | high |
| BROOKS-035 | test | Change-of-resistance temperature measurement: ΔT = (1/α0) * (Rt/Rt0 − 1); reference R measured at ≤100 mA | ΔT = (Rt/Rt0 − 1)/α0 | Rt, Rt0, α0 | Gives AVERAGE temperature over sensed length, not hot spot | measure | §4.7.1 eq.(4.4) p.34; §5.3 eq.(5.2) p.43 | high |
| BROOKS-036 | test | Cross-sectional area of a test trace can be back-calculated: A = ρ * L / Rt0 | A = ρ*L/Rt0 | ρ, L, Rt0 | Assumes published ρ (which may be off — see BROOKS-015/016) | calc | §5.3 eq.(5.1) p.42 | high |
| BROOKS-037 | test | Infrared (thermal camera) measurement: non-contact point measurement; requires known emissivity; uncertainty typically several °C; only viable method for very high (fusing-range) temperatures | uncertainty ≈ several °C | emissivity | — | measure | §4.7.2 p.34–35 | high |
| BROOKS-038 | test | Thermocouple measurement: point measurement; probe tips as small as 3 mils, response 1–2 s; many probes limited to ≈300–350°C by coatings; ensure solid contact; loading of trace is minimal | T_max_probe ≈ 300–350°C | — | — | measure | §4.7.3 p.35–36 | high |
| BROOKS-039 | test | Traces are coolest at end pads and hottest near the center; point measurements may miss the hottest spot; choose method per need (average vs peak) | — | — | — | measure | §4.7.4 p.36; Ch.13 | high |
| BROOKS-040 | thermal | Trace temperature stabilization time after current step is typically ≈6 to 15 minutes (normal load) | t_stab = 6–15 min | — | Test dwell time before reading | measure | §4.8.1 p.37 | high |
| BROOKS-041 | thermal | Heavy overload: temperature rises roughly linearly to melt within a few seconds (< 5–10 s) | t_melt < 5–10 s | I >> rating | Fusing regime (Ch.12) | sim | §4.8.2 p.37 | high |
| BROOKS-042 | thermal | Marginal overload / loss of supplemental cooling: temperature stabilizes (6–15 min), plateaus for minutes to hours, then rises to failure; onset of the final rise typically ≈220–270°C; final rise to melt ≈15 min (situation-specific) | T_runaway_onset ≈ 220–270°C; t_C ≈ 15 min | — | Traces needing heat sink/forced air; delamination-driven | review | §4.8.3 p.39 | high |
| BROOKS-043 | current-carrying | IPC-2152 data span 0.5-oz to 3.0-oz copper with separate external, internal and vacuum sets; no separate 1-oz external chart and no 1-oz vacuum chart exist in IPC-2152 | — | — | Use fitted equations (BROOKS-046/048) for 1 oz | review | §5.2 p.41; §5.4.2 p.47; §5.4.4 p.49 | high |
| BROOKS-044 | test | Reference-resistance measurement at ≤100 mA gives very small voltages for large traces: 2.0 oz × 100 mil × 6 in ≈ 0.016 Ω → 1.6 mV; use a precision meter / 4-wire method | V_ref = I_ref * R ≥ instrument resolution | R | Large traces | measure | §5.3 p.43 | high |
| BROOKS-045 | current-carrying | IPC-2152 charts plot I vs cross-sectional area on constant-ΔT lines; the data are aggregated/interpolated across samples, so treat chart values as smoothed, not exact | — | — | — | review | §5.3 p.43 | medium |
| BROOKS-046 | current-carrying | EXTERNAL trace temperature rise (fit to IPC-2152 external data, verified against 2-oz and 3-oz sets): ΔT = 215.3 * I^2 * W^-1.15 * Th^-1.0 (ΔT °C, I A, W mil, Th mil) | ΔT = 215.3 * I^2 * W^(-1.15) * Th^(-1.0) | I, W, Th | External layer, still air, no adjacent copper/planes, IPC test board (worst case); all copper weights | calc | §5.4.2 eq.(5.5) p.46; Table 5.1 p.50 | high |
| BROOKS-047 | current-carrying | Because W and Th exponents differ (−1.15 vs −1.0), ΔT is NOT a function of cross-sectional area (current density) alone; wider/thinner traces run cooler than narrower/thicker traces of equal area | ΔT(W,Th) ≠ f(W*Th) | W, Th | — | calc | §5.4.2 p.47 | high |
| BROOKS-048 | current-carrying | INTERNAL trace temperature rise fits (IPC-2152 internal data), ΔT = K * I^a * W^b * Th^c with W, Th in mils: 0.5 oz: K=110–130, a=2, b=−1.10, c=−1.52; 1 oz: K=200, a=1.9, b=−1.10, c=−1.52; 2 oz: K=300, a=2, b=−1.15, c=−1.52; 3 oz: K=429–368, a=1.9, b=−1.10, c=−1.52 | see Table 5.1 (§2) | I, W, Th, oz | Internal layer, IPC test board; constant K varies with width (range given) — likely test-control scatter | calc | §5.4.3 Table 5.1 p.48,50; App. C, D | high |
| BROOKS-049 | current-carrying | VACUUM trace temperature rise fits (IPC-2152 vacuum data; no internal/external distinction): 0.5 oz: K=210–235, a=1.9, b=−1.10, c=−1.52; 2 oz: K=480, a=1.9, b=−1.10, c=−1.52; 3 oz: K=460, a=1.95, b=−1.15, c=−1.52 (W, Th mil) | see Table 5.1 (§2) | I, W, Th, oz | Vacuum; no 1-oz data | calc | §5.4.4 Table 5.1 p.49–50; App. C, D | high |
| BROOKS-050 | current-carrying | Ordering for identical trace: T_vacuum > T_external(air) > T_internal, for every thickness in IPC-2152 | ΔT_int < ΔT_ext < ΔT_vac | layer/env | — | calc | §5.4.4 p.49, Fig.5.7 | high |
| BROOKS-051 | thermal | Thermal simulation must iterate resistivity with temperature: 2–3 loops suffice for low temperatures (40–50°C) and internal traces; 4+ loops needed at higher temperatures (up to ≈100°C) | loops ≥ 3 (T ≤ 50°C), ≥ 4 (T ≤ 100°C) | T_final | Any Joule-heating FEM/FDM solver with temperature-dependent ρ | sim | §6.3 p.53; §6.4 p.58 | high |
| BROOKS-052 | thermal | Heat-transfer coefficient (convection + radiation) for a trace on a bare board in still air: base ≈10 W/m²·K at low current; calibrated range ≈11–14 W/m²·K for external and internal IPC traces; in vacuum 5–9 W/m²·K (≈half). Low-temperature results insensitive to HTC (≤1°C); at high temperature HTC 11→14 changes result by ≈10°C (up to 20°C) | HTC_air = 10–14; HTC_vac = 5–9 W/m²·K | environment | Still air, 20°C ambient; single trace on board | sim | §6.3 p.53–54, Fig.6.2; §6.4 p.60 | high |
| BROOKS-053 | thermal | Reference simulation reproducing IPC-2152 2-oz external data: trace 300 mm × 5 mm (200 mil), 68 μm (2 oz), board 350 × 45 mm, 1.6 mm (63 mil) polyimide modeled as 4 × 400 μm layers, k = 0.53 W/m·K in-plane and through-plane, ambient 20°C, HTC 11, thermal pixel 0.2 mm, 16 A → midpoint 65.5°C (ΔT = 45.5°C). Equation (5.5) gives 47.9°C for the same inputs (Th = 2.6 mil) | ΔT_sim(16 A, 200 mil, 2 oz, ext) = 45.5°C | — | Validation anchor for any solver | sim | §6.4 p.55–58 | high |
| BROOKS-054 | thermal | Simulation mesh: thermal pixel (cell side) must be smaller than the smallest x-y feature; for via models this is the plating wall thickness (≈0.02 mm pixel vs 0.2 mm for trace models) | pixel < min(W, via wall) | geometry | FDM/FEM thermal sims | sim | §6.4 p.55; §8.3 p.91 | high |
| BROOKS-055 | current-carrying | Narrow traces have very steep I–ΔT curves: 1-oz 5-mil trace ≈25°C rise at 1.0 A, ≈100°C at 2.0 A, and 0.5→1.0 A adds ≈20°C (eq. 5.5 gives 26°C @1 A, 104°C @2 A); 10-mil only slightly better | ΔT(5 mil,1 oz,1 A) ≈ 25°C; (2 A) ≈ 100°C | I, W | External, worst case | calc | §7.2.1 p.64, Fig.7.1 | high |
| BROOKS-056 | dfm | For narrow traces, fabrication width tolerance (e.g. 5 mil etched to 4 mil, 10 to 9 mil) produces unexpectedly large temperature variation; specify narrow high-current widths conservatively | evaluate ΔT at W_nom − etch tolerance (≥1 mil) | W, tol | W ≤ 10 mil | calc | §7.2.1 p.65, Fig.7.2; §3.5 p.24 | medium (graph) |
| BROOKS-057 | thermal | Thermal transient: 1-oz, 6-in, 200-mil external trace at 15 A stabilizes at 94.6°C; reaches 90% of final rise in ≈3.5 min and 95% in ≈5 min; internal traces rise slightly more slowly | t_90% ≈ 3.5 min; t_95% ≈ 5 min | — | Lab dwell time; pulse-rating basis | sim | §7.2.2 p.66, Fig.7.3 | high |
| BROOKS-058 | thermal | Standard sensitivity model (matches Prototron test board): board 192 × 25 mm, 63 mil thick, measured k = 0.68 W/m·K in-plane / 0.51 through-plane, pads 13 × 7.8 mm, trace 6 in (152 mm), Th nominal 1.9 mil (≈1.5 oz: 1-oz foil + 0.5-oz plating), copper strips along board edges; 100-mil trace at 9.35 A → max 69.2°C (center); measured 67.0°C | anchor: 100 mil, 1.9 mil, 9.35 A → 69.2°C sim / 67.0°C meas | — | 20°C ambient | sim | §7.2.3 p.66–67, Fig.7.4–7.5; Table 7.1 | high |
| BROOKS-059 | thermal | Trace length effect (100 mil, 9.35 A): 6 in 69.2°C; 4 in 68.0; 2 in 60.9; 2 in with plane under pads 59.3; 1 in 49.0; 1 in with plane under pads 46.3°C — length matters only for very short traces (< ≈2 in); pad size influences the drop | see Table 7.1 | L | Ends terminated in large pads | sim | §7.2.4 Table 7.1 p.65,68 | high |
| BROOKS-060 | fab | Measured trace thickness deviated ≈40% from nominal (27-mil trace nominal 1.9 mil, actual 2.7 mil); at 4.75 A simulated 77.8°C (1.9 mil) vs 56.2°C (2.7 mil). Never analyze with nominal dimensions on production boards | ΔT sensitivity to Th ≈ 21.6°C for +0.8 mil at this operating point | Th_actual | Plated outer layers | measure | §7.2.5 Table 7.2 p.68–69 | high |
| BROOKS-061 | thermal | Underlying plane cools a trace strongly (100 mil, 1.9 mil, 9.35 A): no plane 69.2°C; full plane on opposite (bottom) side of 63-mil board 54.1°C; plane 10 mils under trace layer 45.9°C — but the thermal halo spreads much wider, heating neighbors | ΔT reduction ≈31% (bottom plane), ≈53% (10-mil plane) of the 49.2°C rise | plane distance | Full-area plane | sim | §7.2.6 Table 7.3 p.69–70, Fig.7.7 | high |
| BROOKS-062 | thermal | Adjacent unpowered 100-mil trace 8 mil away: driven trace drops 69.2→≈65°C while the passive neighbor rises to ≈55°C; adding a plane 8 mils under both: driven 45.7°C, neighbor 43.0°C — check neighbors' temperature ratings, not just the driven trace | T_neighbor ≈ 55°C for T_driven 65°C (no plane) | spacing, plane | 8-mil gap | sim | §7.2.7–7.2.8 Table 7.4 p.70–72 | high |
| BROOKS-063 | thermal | Splitting a 100-mil power trace into two 50-mil traces 50 mil apart gives no benefit: max 64.7°C each (vs 69.2°C single) with dielectric between them at 59.1°C and a wider thermal envelope; stacking two half-width traces on adjacent layers gives identical 69.2°C | do not split traces for thermal reasons | — | Same total copper | sim | §7.2.9–7.2.10 p.71–73 | high |
| BROOKS-064 | thermal | Forced-air / supplemental cooling as HTC (27-mil, 2.7-mil trace, 4.75 A): HTC 14 → 56.2°C; 20 → 51.1°C; 28 → 46.9°C; mapping of airflow to HTC for a single trace is not established — treat as rough | see Table 7.5 | HTC | Very approximate | sim | §7.2.11 Table 7.5 p.73 | medium |
| BROOKS-065 | thermal | Sensitivity to every layout/material parameter grows with temperature rise: at low ΔT parameters barely matter; at high ΔT they matter a lot — run sensitivity checks at the maximum operating current | — | ΔT | — | sim | §7.2.12 p.73–74 | high |
| BROOKS-066 | thermal | IPC-2152 curves / eq.(5.5) are worst case for a bare single trace; any real-board feature (planes, adjacent copper, pads, shorter length, airflow) lowers the trace temperature — but may raise the dielectric/neighbor temperature | ΔT_real ≤ ΔT_IPC | — | Excludes vacuum, enclosures, hot ambient | review | §7.1 p.63; §7.2.12 p.74 | high |
| BROOKS-067 | thermal | Material-sensitivity base model: 100 mil × 1 oz × 6 in trace, FR4 6.5 × 2 in, 63 mil thick, 7 A, ρ = 1.68 μΩ·cm, HTC 11, k = 0.6 in-plane / 0.4 through-plane, ambient 20°C → ≈56.7–60°C (≈40°C rise) | anchor: 100 mil, 1 oz, 7 A → ≈57°C | — | — | sim | §7.3 p.75; §7.3.1 p.77 | high |
| BROOKS-068 | thermal | Trace temperature decreases with board thickness, steeply for thin boards, saturating for thick boards (63-mil vs 240-mil compared); thin boards have too little material for heat spreading | dT/d(board thickness) < 0, diminishing above ≈63 mil | board thickness | Bare board, no planes | sim | §7.3.1 p.75–76, Fig.7.12–7.14 | medium (graph) |
| BROOKS-069 | thermal | Two full internal planes at 20 mil and 40 mil below the trace in a 63-mil board drop the base-model trace from 56.7°C to 34.5°C (rise 36.7→14.5°C, −60%) and spread heat widely | ΔT with 2 planes ≈ 0.4 × ΔT bare | planes | Full-area planes | sim | §7.3.1 p.77, Fig.7.15–7.16 | high |
| BROOKS-070 | materials | Trace temperature is linear in resistivity; a 10.7% increase in ρ gives an 8.1% increase in trace temperature (base model). ED/plated copper ≈1.68 μΩ·cm; rolled copper 1.72–1.78 μΩ·cm (rolled more common as PCB foil) | dT/T ≈ 0.76 × dρ/ρ | ρ | Base model ≈57°C | calc | §7.3.2 p.77; §7.5 p.87 | high |
| BROOKS-071 | thermal | HTC values to use: 11 W/m²·K representative for still air in this temperature range; 6 for vacuum (space); >11 implies supplemental cooling (range studied 6–18, but no established mapping from airflow to HTC) | HTC = 11 (air), 6 (vacuum) | environment | — | sim | §7.3.3 p.78–79, Fig.7.18 | high |
| BROOKS-072 | materials | In-plane (x-y) thermal conductivity has more effect on trace temperature than through-plane; a difference of 0.3 W/m·K between material choices can lower the trace temperature by ≈10°C at ≈50°C rise (more at higher rise) | ΔT reduction ≈10°C per +0.3 W/m·K (at ΔT≈50°C) | k_xy | Datasheets rarely give k or direction | calc | §7.3.4 p.79, Fig.7.19; §7.5 p.87 | high |
| BROOKS-073 | thermal | Trace thickness sensitivity ≈1.0°C per 0.03 mil change (base model 1 oz, 100 mil, 7 A) — normal plating variation explains non-uniform heating | dT/dTh ≈ 33°C/mil at this operating point | Th | Base model | calc | §7.3.5 p.80, Fig.7.20 | high |
| BROOKS-074 | thermal | Material-parameter partial sensitivities (base model, ≈40°C rise): +1.0°C per 2% resistivity; +3.0°C per 0.1 mil thickness decrease; 5.0°C between HTC 11 and 14; 5.6°C between k = 0.5 and 0.7 W/m·K | see Table 7.7 | ρ, Th, HTC, k | Scale with ΔT | calc | §7.3.6 Table 7.7 p.80,82 | high |
| BROOKS-075 | current-carrying | Internal (mid-board) vs external temperature rise for the same trace and current (regression on IPC-2152 1/2/3-oz data): ΔTi = 0.82 * Th^0.053 * W^0.021 * ΔTe^0.976; ratio ΔTi/ΔTe = 0.82 * Th^0.053 * W^0.021 * ΔTe^-0.024 (Th, W in mils; ΔT in °C). Ratio falls with rising ΔTe; thinner and wider internal traces cool relatively better | ΔTi = 0.82 * Th^0.053 * W^0.021 * ΔTe^0.976 | ΔTe, W, Th | Mid-board internal trace; IPC-2152 materials; example 20 mil/1 oz/ΔTe 40°C → ratio 0.81 | calc | §7.4 eq.(7.2),(7.3) p.82–83, Fig.7.21 | high |
| BROOKS-076 | current-carrying | Depth correction for internal traces not at board center: Fraction = (ΔTe − ΔTi)/(ΔTe − ΔTi(min)) = 1.41 * Depth^0.5 for 0 < Depth ≤ 0.5 (Depth = trace depth / total board thickness); ΔTi(depth) = ΔTe − (ΔTe − ΔTi(min)) * Fraction. Example: 60-mil board, 20-mil 1-oz, 2.8 A, ΔTe = 40°C → ΔTi(min) = 32.4°C; at 12 mil depth (0.2) Fraction = 1.41*0.2^0.5 = 0.63 → ΔTi = 35.2°C; at depth 0.1 book reads ≈42.5% | Fraction = 1.41 * sqrt(Depth) | Depth, ΔTe, ΔTi(min) | Cooling benefit begins at very shallow depth; guide only — derived from IPC-2152 materials | calc | §7.4 eq.(7.4)–(7.9) p.84–86, Fig.7.22 | high (exponent 0.5 recovered from worked example 7.8) |
| BROOKS-077 | via | Legacy rule (IPC-2152 p.26): via conducting cross-section ≥ incoming conductor cross-section, else use multiple vias to match — works but is extremely conservative | A_via_total ≥ A_trace (legacy) | A_trace, A_via | Retain only as a fallback when no thermal sim is available | calc | §8.2 p.90 | high |
| BROOKS-078 | via | Via wall thickness is assumed equal to plating thickness, typically 0.5–1.0 oz (0.65–1.3 mil), but plating is often non-uniform down the barrel — use minimum plating in via-area calcs | th_wall = 0.65–1.3 mil nominal | plating spec | — | inspect | §8.2 p.90–91 | high |
| BROOKS-079 | via | Via conducting area: A_via = π * (r² − (r − th)²), r = drill radius, th = wall plating. Standard via: 10-mil (0.26 mm) drill, 0.030 mm wall → 0.0217 mm² ≈ area of a 1-oz, 26-mil (0.66 mm) trace | A_via = π(r² − (r−th)²) | drill d, th | Uniform plating assumed | calc | §8.3.1 p.91 | high |
| BROOKS-080 | via | Single 0.0217-mm² via in 1-oz traces on 63-mil FR4 (sim, absolute °C, 20°C ambient) — trace TC / via top / via mid: 0.40 mm: 2.0 A 91.4/83.2/82.4, 2.3 A 123.2/111.1/109.9; 0.66 mm: 3.0 A 86.9/81.4/80.9, 4.0 A 166.7/154.1/152.9; 1.2 mm: 3 A 47.9/48.6/48.7, 4 A 74.1/75.7/75.8, 5 A 115.5/118.8/118.8; 1.8 mm: 5 A 70.8/76.8/76.8, 6 A 100.2/110.2/110.2; 2.5 mm: 6 A 68.1/77.6/77.6, 7 A 90.3/104.9/104.9 | Table 8.2 | W, I | Via area = 0.66-mm trace area | sim | §8.3.4 Table 8.2 p.94 | high |
| BROOKS-081 | via | Via-vs-trace temperature rule: if A_trace < A_via the trace is hotter than the via (via acts like an internal trace and cools the trace); if A_trace > A_via the via is slightly hotter than the trace (trace heat-sinks the via); equality at A_trace ≈ 1.5–2.0 × A_via | T_via ≈ T_trace when A_trace ≈ (1.5–2.0) A_via; T_via − T_trace grows slowly beyond | A_trace/A_via, ΔT_trace | 1-oz traces; via 0.0217 mm²; 63-mil board | sim | §8.3.4 p.94–95 | high |
| BROOKS-082 | via | A via's temperature is nearly independent of current when the trace is sized for it: same 0.0217-mm² via at 6 A in a 2.5-mm 1-oz trace is cooler (77.6°C) than at 2 A in a 0.40-mm trace (82.4°C) | see Table 8.3 | — | — | sim | §8.3.4 Table 8.3 p.95 | high |
| BROOKS-083 | via | Small via in a heavy trace: 2-oz, 2.5-mm trace with a single 0.0217-mm² via: 7 A → TC 51.3, via mid 60.8°C; 10 A → TC 93.5, via mid 117.9°C (≈25°C above trace). A 0.66-mm 1-oz trace alone at 10 A would melt in ≈7.5 s — the via survives only by heat-sinking into the trace | T_via − T_trace ≈ 10°C @7 A, ≈25°C @10 A | I, A_trace/A_via | A_trace/A_via ≈ 4 | sim | §8.3.4 Table 8.4 p.96 | high |
| BROOKS-084 | via | At design-typical rises (20–40°C) the via penalty is small: 2-oz 2.5-mm trace, single small via, 5 A → trace +17.1°C, via +21.1°C above 20°C ambient (vs the same via at 4 A in a 0.66-mm trace: +145°C) | ΔT_via ≈ ΔT_trace + 4°C @ ΔT_trace ≈ 17°C | — | — | sim | §8.3.4 Table 8.5 p.96 | high |
| BROOKS-085 | via | Two vias in a 2.5-mm trace (TC / via top / via mid °C): 1 oz 6 A 67.1/69.5/69.5, 7 A 88.6/92.3/92.4; 2 oz 6 A 41.3/43.3/43.5, 7 A 49.9/52.7/53.0, 10 A 89.6/96.5/97.3 — current splits equally; even at 10 A in 2 oz the vias are <10°C warmer than the trace | see Table 8.6 | n_via, I | Straight-through traces | sim | §8.3.5 Table 8.6 p.97 | high |
| BROOKS-086 | via | Typical design target is 20–40°C maximum trace temperature rise | ΔT_target = 20–40°C | policy | Designer policy, not a limit from physics | review | §8.3.4 p.96 | high |
| BROOKS-087 | via | Experimental confirmation (Prototron board: ≈60-mil FR4, 0.5-oz foil + 1.0-oz plating, k = 0.679 in-plane / 0.512 through-plane measured, Th actual top 2.1 mil / bottom 2.9 mil, single 10-mil via): 27-mil trace 4.75 A trace 66 / via 64.5°C, 6.65 A 114 / 109°C; 200-mil trace 4.75 A 30.5 / 31.5°C, 8.55 A 40.5 / 44.5°C. Simulation: 72.8/70.1, 114.2/108.2, 30.8/31.8, 44.8/48.1 (via/trace = 96.3%, 94.7%, 103.2%, 107.4%) | measured ≈ simulated within a few °C; via ≤ 1.12 × trace temperature | — | Via area ≈ 27-mil trace area | measure | §8.4–8.5 Tables 8.7–8.8 p.98–101 | high |
| BROOKS-088 | test | Via/trace temperature test: constant current confirmed by second DMM; thermocouple tip 30 Ga (≈10 mil), response ≈1 s, calibrated at ice water and boiling water; dwell ≈6 min to stabilize; verify probe does not load the trace; microsection afterwards for actual dimensions | dwell ≥ 6 min | — | — | measure | §8.5 p.100 | high |
| BROOKS-089 | via | Voltage drop across a via is negligible: 0.66-mm (26-mil) 1-oz trace, 115 mm, 3 A, T = 86°C, ρ = 1.7 μΩ·cm, α = 0.004 → R(20°C) = 0.0897 Ω, R(86°C) = 0.11339 Ω, V = 0.34 V; via (1.6 mm long) ≈ 0.34 × 1.6/115 = 0.0047 V (sim: 0.32 V trace-with-via, ≈0.00 V across via). 2.5-mm trace, 7 A, 90°C: R20 = 0.0237 Ω, R90 = 0.0303 Ω, V = 0.212 V; via ≈ 0.011 V | V_via ≈ V_trace × L_via / L_trace | L, W, Th, I, T | Through via in 63-mil board | calc | §8.6 eq.(8.1)–(8.3) p.102–103 | high |
| BROOKS-090 | via | Trace with a via runs slightly cooler than the same trace without one (via conducts heat into the board); ignore via resistance in PDN DC-drop budgets unless via length is comparable to trace length | — | — | — | calc | §8.6.1 p.103 | high |
| BROOKS-091 | thermal | Thermal-via model (60 × 120 mm, 1.5-mm FR4, 20 × 20 mm 1-oz pad, 40 A → 82.1°C = +62.1°C; 0.5-mm solid-Cu thermal vias): pad ΔT — no plane 62.1; small plane (pad-size, opposite side) 59.6, +1 via 58.7, +5 vias 47.5; large plane 23.0, +1 via 22.1, +5 vias 16.4; 20°C isothermal heat sink 9.5, +1 via 8.1, +5 vias 4.2; single "special" 20°C-clamped via 22.6 | Table 8.9 | plane size, n_via | Thermal vias help materially only when the receiving copper is small | sim | §8.7 Table 8.9 p.104–105, Fig.8.10 | high |
| BROOKS-092 | thermal | Conduction through the dielectric to an overlapping plane beats thermal vias: Q/t = k*A*ΔT/d; ratio (kA)_pad/(kA)_via = (0.5 × 400 mm²)/(385 × 0.196 mm²) = 2.65 for a 20 × 20 mm pad vs one 0.5-mm via across 1.5 mm; with a large plane or heat sink present, added thermal vias give only marginal improvement | (Q/t)_plane/(Q/t)_via = (k_FR4 * A_pad)/(k_Cu * A_via) | A_pad, n_via, d | k_FR4 ≈ 0.5, k_Cu ≈ 385 W/m·K | calc | §8.7 eq.(8.4)–(8.6) p.105–107 | high |
| BROOKS-093 | via | Thermal vias from a trace to a plane give trivial (if any) improvement — traces cool vias, vias do not cool traces; dielectric coupling to a parallel plane is the effective mechanism | — | — | — | sim | §10.4.1 p.120; §8.7.2 p.107 | high |
| BROOKS-094 | via | Current divides equally among parallel vias when the traces continue straight (4 vias, 4 A → ≈0.98 A each); with the exit trace turned 90°, the shortest-path via carries 1.14 A, the farthest 0.72 A, the other two 0.96 A (±≈20% imbalance) | I_via,max ≈ 1.14 × I/n for a 4-via 90° turn | n_via, geometry | 0.9-mm (35-mil) 1-oz trace, 0.26-mm vias, 63-mil FR4 | sim | §9.4–9.5 p.113–115 | high |
| BROOKS-095 | via | Current density in a via wall is non-uniform at the entry (leading edge 223.7 vs trailing 140.4 A/mm², avg 181 A/mm² for 4 A in 0.0217 mm²) and uniform at mid-depth (181.3 A/mm²); these gradients have no effect on via/trace temperature (copper spreads the heat) | — | — | Square-pixel model of round wall gives ≈2% current error | sim | §9.3 p.110–112; §9.6 p.116 | high |
| BROOKS-096 | thermal | Ch.10 test board: 220 × 20 mm, 1.55 mm thick incl. 38-μm (1-oz) top/bottom copper, polyimide; reference trace 150 mm × 1.0 mm (40 mil), 4 A → 53.2°C (ΔT 33.2°C) | anchor: 40 mil, 1 oz, 4 A, 6 in → +33.2°C | — | Compare eq.(5.5): 215.3×16×40^-1.15×1.5^-1 ≈ 33.5°C (Th=1.5 mil) | sim | §10.3 p.118 | high |
| BROOKS-097 | thermal | Copper under a 40-mil 4-A trace (ΔT and % improvement): none 33.2°C; same-width trace beneath 32.95 (0.8%); 3×-wider (120 mil) trace beneath 29.2 (12.0%); full plane on bottom layer 24.8 (25.3%); full plane on the layer directly under the trace 19.5 (41.3%) | Table 10.1 | copper under trace | Cooling copper carries no current; tie to ground with one via; consult SI for AC/pulsed | sim | §10.4 Table 10.1 p.119 | high |
| BROOKS-098 | thermal | Distributed copper stubs along a high-current trace (nine 5.0-mm-wide stubs on a 1.0-mm trace, 15 mm apart) cut peak temperature from 53.2°C to 44.4°C (ΔT 33.2→24.4°C, −26.5%); high-current traces need not be constant width | ΔT reduction ≈26.5% for stub area ratio 5:1 every 15 mm | stub geometry | Little current fringes into stubs | sim | §10.5 p.120–121 | high |
| BROOKS-099 | thermal | Short narrow links are heat-sunk by the parent trace: 11-mil-wide, ≈3-mm-long link in a 40-mil 4-A trace → ΔT 54.6°C (vs 33.2°C; an isolated 11-mil trace at 4 A would exceed 150°C); adding a 40 × 6 mm copper area under the link → 40.0°C; adding a second parallel link → 39.3°C | link ΔT ≈ 1.6 × trace ΔT (bare), ≈1.2 × with plane or second link | link W, L | Link looks like a fuse — verify with sim | sim | §10.6 Table 10.2 p.121–123 | high |
| BROOKS-100 | protection | Preece fusing (melting-point) current for a copper wire in air, slow heating, no time variable: I = a * d^(3/2), d = wire diameter [inch], a = 10244 for copper, I [A]; equivalently I = 12277 * A^(3/4), A = cross-section [in²] | I_fuse = 10244 * d^1.5 = 12277 * A^0.75 | d or A | Round wire in air; "fusing" = wire glows, i.e. reaches melting point (t1), not separation | calc | §11.3 eq.(11.1),(11.2) p.126 | high |
| BROOKS-101 | protection | Onderdonk short-time fusing relation (no cooling): 33 * (I/A)² * S = log10(ΔT/(234 + Ta) + 1); I [A], A [circular mils], S [s], ΔT = temperature rise [°C], Ta = reference/initial temperature [°C]; for Ta = 40°C the denominator is 274. Time form used by the book: t = (1/33.5) * log10(ΔT/(234 + Tref) + 1) * (A/I)² | see formula | I, A, S, Ta | Valid only while cooling is negligible: typically < 10 s for wires in air; on a PCB deviates within ≈1 s | calc | §11.4 eq.(11.3),(11.4) p.127–128; §12.2 eq.(12.1),(12.2) p.134 | high (constant printed as 33 in (11.3)/(12.1) and 33.5 in (12.2); (12.3) below is consistent with 33.5) |
| BROOKS-102 | protection | Unit conversions for Onderdonk: A_cmil = d² (d in mils); 1 mil² = 1.273 circular mil; 1 circular mil = 0.7854 mil²; 1 m² = 19.736e8 circular mil; 1 circular mil = 5.067e-10 m² = 5.067e-4 mm² | — | — | — | calc | §11 end note 8 p.131; §12 end note 1 p.151 | high |
| BROOKS-103 | protection | Both Preece and Onderdonk give the time/current to REACH the melting temperature (t1); the additional heat of fusion / liquid separation (t2) is excluded; liquid copper has higher ρ (≈2×) so runaway follows; circuit opens only when the liquid path separates | t_open > t1 | — | — | review | §11.4.1 p.129–130 | high |
| BROOKS-104 | protection | Onderdonk in book's PCB units (Tref = 20°C, melt 1083°C, A in mil²): t = 0.0346 * (A/I)²  ⇔  t * (I/A)² = 0.0346  ⇔  I² t = const for fixed A (fuse-industry I²t); t [s], A [mil²], I [A] | t_Onderdonk = 0.0346 * (A/I)² | A, I | No cooling; matches TRM "fuse" model exactly | calc | §12.5.1 eq.(12.3),(12.4) p.136,138 | high |
| BROOKS-105 | protection | Fusing temperature for PCB traces = copper melting point 1083°C; fusing time = time to reach 1083°C | T_fuse = 1083°C | — | — | calc | §12.3 p.134 | high |
| BROOKS-106 | protection | Fusing simulation practice: temperature-dependent resistivity must be updated every time step; 0.1-s step is an adequate compromise; HTC value is irrelevant in the < 5-s regime (conduction into the board dominates) | Δt_step ≤ 0.1 s | — | — | sim | §12.5 p.135–137 | high |
| BROOKS-107 | protection | On a 63-mil FR4 board a real trace survives longer than Onderdonk predicts because heat conducts into the dielectric; board size has no effect; a plane on the opposite side of the board has no effect; a plane 12 mils under the trace lengthens fusing time by 30–100% (larger at lower current/longer times); polyimide slightly longer than FR4 | t_trace ≥ t_Onderdonk; ×1.3–2.0 with plane 12 mil below | plane spacing | Short-time (≤ 5 s) overloads | sim | §12.5.2 p.137–138 | high |
| BROOKS-108 | protection | Ratio of simulated trace fusing current to Onderdonk fusing current at fixed time (63-mil FR4, 6-in trace) — columns t = 0.5/1/2/3/4/5 s: 2 oz × 20 mil (52 mil²): 3.46/3.87/4.65/5.30/5.84/6.30; 1 oz × 20 mil (26 mil²): 2.24/2.45/3.03/3.53/3.83/4.20; 1 oz × 100 mil (130 mil²): 2.02/2.14/2.45/2.69/3.02/3.15; 1 oz × 200 mil (260 mil²): 1.88/2.04/2.37/2.62/2.77/2.97; 2 oz × 200 mil (520 mil²): 1.57/1.67/1.90/2.05/2.20/2.37; 2 oz × 100 mil (260 mil²): 1.51/1.63/1.82/1.98/2.10/2.20 | I_trace(t) = ratio(W,Th,t) * I_Onderdonk(t) | W, Th, t | 1 oz = 1.35 mil, 2 oz = 2.7 mil in these sims; ratios grow with time; narrower traces gain more | calc | §12.5.3 Table 12.1 p.141 | high |
| BROOKS-109 | protection | Short-time survival design rule (first ≈3 s): for all simulated traces except 1 oz × 20 mil, t * (I/A)² ≤ 0.25 at fusing; conservative design: require t * (I/A)² < 0.15 (t [s], I [A], A [mil²]). Example: 40 A for 1.0 s → A > (1600/0.15)^0.5 = 103 mil² → 1-oz (1.35 mil), 76-mil-wide trace; cross-check: Onderdonk I = sqrt(0.0346 * 103²/1) = 19 A, ×2.14 (Table 12.1) = 40.6 A | A_min = I * sqrt(t / 0.15) | I, t | Traces ≥ 100 mil wide assumed in the example; 1-oz 20-mil traces exceed 0.25 | calc | §12.5.3 p.140–142, Fig.12.8 | high |
| BROOKS-110 | protection | Real fusing times are 1.5–6.0× Onderdonk (more with adjacent copper); relatively, narrower traces take longer to fuse because their thermal plume is wider relative to width (dielectric under a 20-mil 1-oz trace at fusing ≈720°C vs ≈952°C under a 200-mil 2-oz trace) | t_actual = (1.5–6) × t_Onderdonk | — | Use simulation for anything but a rough estimate | sim | §12.5.3–12.5.4 p.140–142 | high |
| BROOKS-111 | reliability | A fused trace is a destructive failure: never repair and return the board to service; a trace used as a fuse is a one-time event; use a fuse component when a replaceable fuse is needed | — | — | — | review | §12.5.4 p.142 | high |
| BROOKS-112 | materials | Thermal decomposition Td typically 300–350°C; the laminate used in fusing tests is rated time-to-delamination > 60 min at 260°C and > 20 min at 288°C | Td = 300–350°C; T260 > 60 min; T288 > 20 min (test material) | material | — | review | §12.6.2 p.144 | high |
| BROOKS-113 | protection | Fast-fusing experiment: 15-mil, 0.5-oz trace, 6 A step → fused in 2.75 s (simulation 4 s); voltage/temperature ramps ≈linearly; fuses within one 1/30-s video frame at its weakest point; no smoke, negligible board damage | t_fuse(15 mil, 0.5 oz, 6 A) = 2.75 s meas / 4 s sim | — | Onderdonk: A = 15×0.65 = 9.75 mil² → t = 0.0346 × (9.75/6)² = 0.09 s (≈30× shorter) | measure | §12.8.1 p.146–147 | high |
| BROOKS-114 | protection | Slow-fusing experiment: 20-mil, 1.5-oz (nominal 1.9–2.6 mil) trace at 8.5 A → plateau ≈250°C then runaway, fused after ≈30 min; visible glow 35 s before, smoke 90 s before, burning smell ≈15 min before; delamination bubbles along the trace. Same trace: 8.3 A no runaway in 2 h; 8.4 A fused at 1 h 16 min; a nominally identical trace on another board: 8.5 A no runaway > 1 h | runaway threshold band ≈ 8.3–8.5 A (±1%) for this trace — not predictable per trace | — | Marginal overload; board-specific discontinuities | measure | §12.8.2–12.8.3 p.147–149 | high |
| BROOKS-115 | test | Fusing-test instrumentation: constant-current supply (10 A max) and scope accurate within 2–3%; test traces 6 in, 15–27 mil wide, 0.5-oz foil + 1.0-oz plating with total thickness 1.9–2.6 mil worst case (widths well controlled); temperature estimated from V/I with R20 from nominal geometry, ρ = 0.67 μΩ·in, α = 0.0039 /°C (average trace temperature) | — | — | — | measure | §12.8 p.145; end note 5 p.151 | high |
| BROOKS-116 | thermal | Traces do not heat uniformly: hot spots exist along the trace even at ≈50°C (IR close-up), the centerline is hotter than the edges (shorter cooling path at edges), the hottest point is often off-center, and fusing occurs at the (unpredictable) weakest point; a thermocouple moved slightly changes reading up to 1.5°C | T_peak > T_avg (IPC method) | — | Design margin must cover hot spots, not just average ΔT | measure | §13.3 p.153–158 | high |
| BROOKS-117 | fab | Trace thickness varies along a trace: 2.60 → 2.29 mil (0.31 mil) within a 40-mil length in one microsection; with ≈1°C per 0.03 mil sensitivity this alone gives ≈10°C local variation | ΔTh_local ≈ 0.3 mil | — | Plated outer layers | inspect | §13.3.3 p.156–157, Fig.13.6 | high |
| BROOKS-118 | thermal | Hot-spot test set (max temperature reached, IR): 100 mil / 0.5 oz foil (0.65 mil) / 5.6 A → 53.0°C; 100 mil / 0.5+1.0 oz (1.9 mil) / 8.0 A → 54.0°C; 100 mil / 1.5 oz (2.0 mil) / 7.5 A → 54.5°C; 100 mil / 1.5+1.75 oz (4.4 mil) / 10 A → 47.0°C; 200 mil / 2.0 oz (2.6 mil) / 10 A → 39.0°C; 200 mil / 2.0+1.0 oz (3.9 mil) / 10 A → 35.0°C; 200 mil / 2.0+2.0 oz (5.2 mil) / 10 A → 33.6°C | Table 13.1 | — | Room ambient; all show non-uniform heating, no pattern vs thickness | measure | §13.3.2 Table 13.1 p.156 | high |
| BROOKS-119 | thermal | Right-angle corners are not a thermal problem: 200-mil, 1-oz trace on 1.5-mm FR4 at 8 A (≈44°C, +24°C): inside of corner only 0.5–1.5°C warmer than outside; the corner is at or below the straight-trace temperature because it is wider (lower R); the imbalance is caused by cooling geometry (inside sees a 90° arc of board, outside 270°), not by current density; larger corner width and sharper inside corner increase the difference; narrower traces / lower current reduce it | ΔT_corner ≤ 0 vs body; inside − outside ≈ 0.5–1.5°C | corner style | Confirmed by FLIR SC640 IR (7.5–13 μm) on 60-mil FR4 | sim | §13.4 p.158–164 | high |
| BROOKS-120 | current-carrying | Current-density form of the external fit: ΔT = 215.3 * J² * W^0.85 * Th with J = I/(W*Th) [A/mil²] — ΔT at fixed J still depends on W and Th, so J cannot be the design variable | ΔT = 215.3 * J^2 * W^0.85 * Th | J, W, Th | — | calc | §14.3 eq.(14.2) p.166 | high |
| BROOKS-121 | materials | Rolled copper (ρ ≈ 1.76 μΩ·cm) runs ≈7.3% hotter than deposited copper (ρ ≈ 1.64 μΩ·cm) at the same current and geometry | ΔT_rolled/ΔT_ED ≈ 1.073 | foil type | — | calc | §14.5 p.166–167 | high |
| BROOKS-122 | current-carrying | Form-factor table (eq. 5.5, external, A = 390 mil², I = 15 A, J = 0.0385 A/mil² for all rows): 0.5 oz (0.65 mil) × 600 mil → ΔT 47.5°C; 1 oz (1.3) × 300 → 52.8; 1.5 oz (1.95) × 200 → 56.1; 2 oz (2.6) × 150 → 58.6; 3 oz (3.9) × 100 → 62.3; 4 oz (5.2) × 75 → 65.0; 5 oz (6.5) × 60 → 67.2°C — prefer wide/thin over narrow/thick for equal area | Table 14.1 | W, Th | — | calc | §14.8 Table 14.1 p.168 | high |
| BROOKS-123 | via | Constant-via-temperature simulation (board 80 × 12 × 1.6 mm, Cu 0.04 mm, traces 32 mm top + 32 mm bottom, via 0.26 mm drill, 0.04 mm wall, A_via = 0.02675 mm² as printed [π(0.13² − 0.09²) = 0.0276]): W 0.6 mm / 2.74 A → T_trace 61.2, T_via 60.4°C, J_trace 114.2, J_via 99.1 A/mm²; 0.7 / 2.95 A → 59.5 / 59.4 / 105.4 / 106.7; 1.0 / 3.57 A → 58.6 / 60.5 / 89.3 / 129.1; 2.0 / 5.25 A → 56.5 / 60.5 / 65.6 / 189.9; 3.0 / 6.5 A → 54.8 / 59.8 / 54.2 / 235.1; 4.0 / 7.5 A → 53.7 / 60.0 / 46.9 / 271.2; 5.0 / 8.4 A → 52.7 / 59.6 / 42.0 / 303.8. Via temperature stays ≈60°C from 2.7 to 8.4 A while via current density triples; the via alone would melt at 8.4 A in ≈1 s | Table 14.2 | W, I | Via J up to ≈300 A/mm² acceptable when the trace is sized for ≈+35–40°C | sim | §14.9 Table 14.2 p.168–170 | high |
| BROOKS-124 | current-carrying | Pulsed (square) current: equivalent heating current I_rms = I_peak * sqrt(D), D = duty cycle (fraction); steady trace temperature is linear in D. Model (26-mil × 2.9-mil trace, k = 0.7 W/m·K, ρ_mass = 2000 kg/m³, cp = 900 J/kg·K, ambient 26°C, 5 A peak): D 100% 5.000 A → 65.7°C; 99% 4.975 → 65.3; 90% 4.743 → 61.2; 80% 4.472 → 56.8; 70% 4.183 → 52.6; 60% 3.873 → 49.5; 50% 3.536 → 45.4; 40% 3.162 → 41.2; 30% 2.739 → 37.3; 20% 2.236 → 33.8; 10% 1.581 → 29.8; 1% 0.50 → 26.0 | I_eq = I_pk * sqrt(D) | I_pk, D | Includes α correction; 5 A in this trace dissipates 1.464 W | sim | §15.2 eq.(15.1), Table 15.1 p.171–174 | high |
| BROOKS-125 | current-carrying | Trace temperature is independent of frequency for f above ≈10 Hz (thermal inertia; 4–6 min time constant) — verified 0.05 Hz to 10 kHz at 50% duty (≈45°C measured vs 45.4°C model) and 0.5–1000 Hz for analog waveforms; skin effect not covered (expected to still follow RMS) | T(f) = const for f ≳ 10 Hz | f | Below ≈1 Hz the temperature ripples within the cycle (0.04-Hz, 80% example) | measure | §15.2–15.4 p.176–185 | high |
| BROOKS-126 | current-carrying | RMS values for sizing: 50% square = peak amplitude (A1 − Am); pulse train = (A1 − A0) * sqrt(D); sine = 0.707 * peak; triangle/sawtooth = 0.577 * peak; with DC offset: I_rms,total = sqrt(I_rms_ac² + I_dc²) (dc = Am for square/sine, A0 for sawtooth/pulse) | see formulas | waveform | Measure true-RMS of current (not collector voltage) when the circuit is nonlinear | calc | §15.4.2 eq.(15.3) p.182–183 | high |
| BROOKS-127 | current-carrying | Analog-waveform verification (100-mil, 0.5-oz, 6-in trace, 100 Hz): sine 5.39 A rms → 65.5°C; sawtooth 5.68 A → 68.5°C; square 50% 5.11 A → 62.0°C; square 75% 6.12 A → 75.0°C; square 99% 7.27 A → 97.0°C — all fall on the DC I–T curve | T = T_DC(I_rms) | I_rms | — | measure | §15.4.4 Table 15.3 p.184–185 | high |
| BROOKS-128 | test | AC-thermal test setup: constant-current source must never see an open — alternate the current between two identical traces with complementary-driven Darlington switches; thermocouple logger 1-s sampling, 0.5°C resolution; ambient ≈26°C; analog test: 10.0-V source through 1.05-Ω low-tempco resistor, I = (10.0 − V_collector)/1.05, true-RMS from scope data (≈900 samples/cycle) | — | — | — | measure | §15.3 p.177–178; §15.4.1 p.181–184 | high |
| BROOKS-129 | test | Dimension verification: microsection measures better than 0.1 mil (2.5 μm) but is destructive, single-point, and needs ≈1 × 0.5 in coupon; industrial CT scan (≈2200 projections per 360°) is non-destructive, works on assembled boards, images via walls and whole traces, but resolution is only qualitative (find opens/shorts, gross plating non-uniformity); board size limit ≈5–6 in square; turnaround days vs hours | microsection: < 0.1 mil; CT: qualitative only | — | — | inspect | Ch.16 p.187–196, Table 16.1 | high |
| BROOKS-130 | materials | Thermal conductivity of a laminate must be measured in both directions (anisotropic); Modified Transient Plane Source (MTPS, C-Therm) method: ≈1.5-in-square sample flat on sensor → through-plane k; multiple samples stacked edge-wise and compressed → in-plane k; short (1–2 s) heat burst | need k_xy and k_z | material | Datasheets usually give one unlabeled value or none | measure | App. A p.199–201 | high |
| BROOKS-131 | materials | Resistivity sanity bound: pure copper 1.676 μΩ·cm at 20°C, copper alloys ≈1.72; silver 1.6 is the lowest of any element — any measured copper trace resistivity < 1.6 μΩ·cm at 20°C is a measurement error; plated copper is pure copper (≈1.7 μΩ·cm), reports well above 1.7 for plating are suspect | 1.6 ≤ ρ_Cu(20°C) ≤ ≈1.8 μΩ·cm | ρ_meas | — | measure | App. B.1 p.204 | high |
| BROOKS-132 | test | Trace resistance measurement: inject current at the trace ends and sense voltage at separate points ON the trace inside the injection points (Kelvin/IPC style, Fig. B.2); never include lead or probe contact resistance; use the largest practical current, area, length and voltage; ordinary ohmmeters drive only 50–200 mA (too small); special 4-terminal meters supply 2–4 A | 4-wire, I_test as large as possible without heating | — | Resistivity extraction requires measured (not nominal) W, L, Th | measure | App. B.2–B.3 p.204–207 | high |
| BROOKS-133 | test | Dimension error budget for resistivity extraction: width tolerance ≈0.1 mil (≈1% on a 200-mil trace, design value usable); length ambiguous when end pads are not much wider than the trace (pad resistance matters); thickness is the dominant error — plated traces vary up to 50% over a board, foil ±10%, and up to 10% edge-to-edge across one plated trace | width ±0.1 mil; Th ±10% (foil) / ±50% (plated) | — | — | measure | App. B.4 p.207–208 | high |
| BROOKS-134 | materials | Copper–laminate interface roughness has no significant effect on DC trace resistance | ΔR_DC(roughness) ≈ 0 | — | DC/thermal only; matters for high-speed loss | calc | App. B.4.4 p.208 | high |
| BROOKS-135 | fab | Measured thickness spread on 200-mil test traces (six points across width, ±0.2–0.3 mil tolerance): 2-oz foil (nominal 2.3 mil): max 2.8 / min 1.9 / avg 2.4 mil; 2-oz foil + 1-oz plating (nominal 3.9): 4.3 / 3.0 / 3.6; 2-oz foil + 2×1-oz plating (nominal 5.2): 5.7 / 4.3 / 4.7 mil — plated thickness ≈ 0.9 × nominal on average, min ≈ 0.77–0.83 × nominal | Th_min ≈ 0.8 × Th_nom (plated); Th_avg ≈ 0.9 × Th_nom | — | One fabricator/panel | measure | App. B.5 Table B.1 p.209–211 | high |
| BROOKS-136 | materials | Measured resistivities (2.1 A, 24.5°C, corrected to 20°C): 2-oz foil 1.806 → 1.788 μΩ·cm; foil + 1-oz plating 1.786 → 1.758 (expected 1.752 from parallel layers of 1.788 foil and 1.7 plating); foil + 2-oz plating 1.766 → 1.739 (expected 1.739). Model multi-layer traces as parallel resistors of foil (ρ ≈ 1.79) and plating (ρ = 1.70) | ρ_eff = Th_total / (Th_foil/ρ_foil + Th_plate/ρ_plate) | Th_foil, Th_plate | — | calc | App. B.5–B.6 Table B.2 p.211 | high |
| BROOKS-137 | current-carrying | Full IPC-2152 fit set (Appendix D), ΔT = const * W^a1 * Th^a2 * I^a3 (W, Th mil, I A): External all: 215.3, −1.15, −1.00, 2.0. Internal 0.5 oz: 110 (W ≥ 100 mil), 125 (W = 50 mil), 130 (W ≤ 20 mil), a1 = −1.10, a2 = −1.52, a3 = 2.0; 1 oz: 200, −1.10, −1.52, 1.9 (all W); 2 oz: 300, −1.15, −1.52, 2.0 (all W); 3 oz: 429 (W ≥ 50 mil) / 368 (W < 50 mil), −1.10, −1.52, 1.9. Vacuum 0.5 oz: 210 (W ≤ 100 mil), 215 (150 mil), 225 (200 mil), 235 (500 mil), −1.10, −1.52, 1.9; 2 oz: 480, −1.10, −1.52, 1.9; 3 oz: 460, −1.10, −1.52, 1.95 (all W) | see §2.5b | I, W, Th, layer, env | Width-dependence of const attributed to graphical/material scatter; interpolate const between listed widths | calc | App. D p.219–220 | high |
| BROOKS-138 | current-carrying | Appendix E current/temperature charts (0.25, 0.5, 1, 2, 3, 4, 5 oz) were generated with: board 200 × 110 × 1.6 mm polyimide, k_xy = k_z = 0.58 W/m·K, ρ_Cu = 1.75e-8 Ω·m, α = 0.00394 /°C, trace length 150 mm, HTC 10–14 depending on external trace temperature; results approximate, use at own risk | chart model constants | — | Charts are graphs (not transcribed) — regenerate from eq.(5.5)/Table 5.1 or a solver with these constants | sim | App. E p.221–229 | medium (graph) |
| BROOKS-139 | protection | Adiabatic (Onderdonk) derivation constants for copper: cp = 385 J/kg·K; density 8900 kg/m³; ρ20 = 1.72e-8 Ω·m (0.0172 Ω·mm²/m); α20 = 0.00393 /K; energy balance cp*M*ΔT = R*I²*Δt with R = ρ20*(1 + α20*(T − 20))*L/A; solution ln(1 + α20*Θ) = (α20*ρ20/(cp*ρd))*(I/A)²*t; α20*ρ20/(cp*ρd) = 1.973e-17 (SI) → 76.9 per (A/cmil)²·s → /ln(10) = 33.5 | 33.5 * (I/A_cmil)² * t = log10(Θ/(234 + Tref) + 1) | I, A, t, Tref | Θ = rise above initial temperature; no heat loss | calc | App. G eq.(G.1)–(G.22) p.244–248 | high |
| BROOKS-140 | materials | Temperature-coefficient identity: α_T2 * ρ_T2 = α_T1 * ρ_T1 for any two reference temperatures, hence 1/α_Tref = 1/α_20 + (Tref − 20) = 234 + Tref (using 1/0.00393 = 254) | α_ref = 1/(234 + Tref) | Tref | Copper | calc | App. G eq.(G.19)–(G.21), G.3 p.248–251 | high |
| BROOKS-141 | protection | Onderdonk log denominator (234 + Tref) and fusing-time constant c in t = c * (A/I)² for melt at 1083°C from Tref: Tref 20°C: denom 254, c = 0.0213 (A in circular mil) / 0.0346 (A in mil²) / 8.30e4 (A in mm²); 40°C: 274, 0.0203 / 0.0330 / 7.92e4; 85°C: 319, 0.0184 / 0.0298 / 7.15e4; 105°C: 339, 0.0176 / 0.0285 / 6.85e4 (85/105°C are automotive references; hotter start → shorter time) | t = c(Tref) * (A/I)² | A, I, Tref | Adiabatic lower bound on real PCB fusing time | calc | App. G Tables G.2, G.3 p.249–250 | high |
| BROOKS-142 | protection | Independent derivation check: Babrauskas & Wichman (2011) time-to-melting-temperature (their eq. 6) is ≈4% below Onderdonk; their eq. 8 (including heat of fusion) is 17% above and should not be compared to Onderdonk | t_B&W,eq6 ≈ 0.96 × t_Onderdonk | — | — | calc | App. G.2 p.243–244 | high |
| BROOKS-143 | test | Trace-thermal test coupons in this book: 6-in traces, widths 15–200 mil, end pads ≈0.5 × 0.3 in (13 × 7.8 mm); 63-mil FR4; copper 0.5-oz foil + 1-oz plating (nominal 1.9 mil, actual 1.9–2.9 mil); board k measured 0.68/0.51 W/m·K; supply ≤10 A; ambient 20–26°C still air; dwell ≥ 6 min | — | — | Reuse this geometry when correlating a solver to IPC-2152 | measure | §7.2.3; §8.4; §12.8; App. B | high |
<!-- RULES-APPEND -->

## 2. Formulas & tables (numbers)

### 2.1 Copper resistivity vs temperature (Matula, ≥99.99% Cu) — Table 3.1, p.23

| Temp (°C) | Resistivity (μΩ·cm) | Implied α from 20°C (1/°C) |
|---|---|---|
| 0 | 1.541 | — |
| 20 | 1.676 | — |
| 27 | 1.723 | 0.0040 |
| 77 | 2.061 | 0.0040 |
| 127 | 2.400 | 0.0040 |
| 227 | 3.088 | 0.0041 |
| 327 | 3.790 | 0.0041 |
| 427 | 4.512 | 0.0042 |
| 527 | 5.260 | 0.0042 |
| 627 | 6.039 | 0.0043 |
| 727 | 6.856 | 0.0044 |
| 827 | 7.715 | 0.0045 |
| 927 | 8.624 | 0.0046 |
| 1027 | 9.950 | 0.0047 |
| 1084 (solid, m.p.) | 10.17 | 0.0048 |
| 1084 (liquid) | 21.01 | — |
| 1127 (liquid) | 21.43 | — |
| 1227 (liquid) | 22.42 | — |
| 1327 (liquid) | 23.42 | — |
| 1427 (liquid) | 24.41 | — |

Source: Matula, R. A., J. Phys. Chem. Ref. Data, Vol. 8, No. 4, 1979, Table 2 p.1161 (cited §3.4 end note 6).

### 2.2 Resistivity reference values

| Material / condition | ρ | Units | Source |
|---|---|---|---|
| Silver (20°C) | 1.6e-8 Ω·m = 0.63 μΩ·in | — | §3.2 p.19 |
| Copper (20°C) | 1.7e-8 Ω·m = 0.67 μΩ·in | — | §3.2 p.19 |
| Gold (20°C) | 2.2e-8 Ω·m = 0.87 μΩ·in | — | §3.2 p.19 |
| Pure copper | 1.68 | μΩ·cm | §2.3.3 p.12 |
| Annealed copper | 1.72 | μΩ·cm | §2.3.3 p.12 |
| ED foil (after bonding) | 1.62–1.66 | μΩ·cm | §2.3.1 p.10 |
| Rolled foil | 1.74–1.78 | μΩ·cm | §2.3.1 p.10 |
| UNS C10100–C14500 alloys (sample) | 1.69–1.86 | μΩ·cm | §2.3.3 p.12 |
| Silicon | 6.4e2 | Ω·m | §3.2 p.20 |
| Glass | 1e9 – 1e15 | Ω·m | §3.2 p.20 |
| Reported internet PCB-trace measurements (unreliable) | 1.6–2.7 | μΩ·cm | §3.5 p.25 |

Conversion: 1 μΩ·cm = 0.3937 μΩ·in; 0.67 μΩ·in = 1.70 μΩ·cm.

### 2.3 Thermal conductivity references

| Item | k (W/m·K) | Source |
|---|---|---|
| Dielectric in-plane (Tcon-x), typical | 0.5 or 0.6 | §2.4.1 p.13 |
| Dielectric through-plane (Tcon-z), typical | 0.3 to 0.5 | §2.4.1 p.13 |
| Dielectrics, general range | 0.3 to 0.8 | §4.4 p.29 |
| Copper | 386 | §2.4.1 p.13 |

### 2.4 Copper thickness conventions (§1.3 p.5; §5.4 p.50)

| Copper weight | mil | mm |
|---|---|---|
| 0.5 oz | 0.60–0.65 (book: 0.65 in ex. 3.1a) | 0.015–0.017 |
| 1 oz | 1.2–1.3 (≈1.3 default); also quoted 1.35 / 1.38 | 0.030–0.034; often 0.035 |
| IPC tolerance on trace thickness | ±10% | |
| Definition | 1 oz = one ounce of copper spread over 1 ft² | |

### 2.5 IPC-2152 curve-fit coefficients — Table 5.1, p.50 (ΔT = K * I^a * W^b * Th^c; ΔT °C, I A, W mil, Th mil)

| Data set | Cu weight | K (constant) | a (I exponent) | b (W exponent) | c (Th exponent) |
|---|---|---|---|---|---|
| External | all | 215.3 | 2 | −1.15 | −1.0 |
| Internal | 0.5 oz | 110–130 | 2 | −1.10 | −1.52 |
| Internal | 1 oz | 200 | 1.9 | −1.10 | −1.52 |
| Internal | 2 oz | 300 | 2 | −1.15 | −1.52 |
| Internal | 3 oz | 429–368 | 1.9 | −1.10 | −1.52 |
| Vacuum | 0.5 oz | 210–235 | 1.9 | −1.10 | −1.52 |
| Vacuum | 2 oz | 480 | 1.9 | −1.10 | −1.52 |
| Vacuum | 3 oz | 460 | 1.95 | −1.15 | −1.52 |

Notes: external equation (5.5) verified graphically against IPC-2152 2-oz and 3-oz external data (Figs. 5.4, 5.5, "extremely good" fits); 1-oz external curves (Fig. 5.6) are generated from (5.5), not from IPC data. Ranges in K reflect width-dependent scatter in the IPC internal/vacuum data (attributed to test control). Full per-width equation set is in Appendix D (§2.5b below).

### 2.6 IPC test coupon (IPC-TM-650 2.5.4.1a) — Fig. 4.5 / 5.1

| Feature | Value |
|---|---|
| Overall trace length | 12 in |
| End pad diameter | 200 mil |
| Sense pad | 20 mil wide × 400 mil long, 3 in from each end |
| Active (sensed) length | 6 in |
| Sense lead | #26 AWG magnet wire |
| Reference-resistance measurement current | ≤ 100 mA |
| Orientation | horizontal, still air |
| Temperature calc | ΔT = (1/α0)(Rt/Rt0 − 1) |

### 2.7 Time constants and thresholds (Ch.4)

| Quantity | Value | Source |
|---|---|---|
| Time to stable temperature after current step | ≈6–15 min | §4.8.1 p.37 |
| Heavy-overload melt time | < 5–10 s (≈linear rise) | §4.8.2 p.37 |
| Marginal-overload plateau | minutes to hours | §4.8.3 p.39 |
| Runaway onset temperature | ≈220–270°C | §4.8.3 p.39 |
| Runaway-to-melt duration ("C") | ≈15 min (varies) | §4.8.3 p.39 |
| Typical Td | ≈350°C | §2.4.3 p.14 |
| T260/T288 ramp | 10°C/min | §2.4.4 p.14 |
| Thermocouple probe limit | ≈300–350°C | §4.7.3 p.36 |
| Thermal plume half-width, 200-mil trace @≈70°C | ≈10 mm (≈4×W) | §4.4.1 p.32 |
| Thermal plume half-width, 20-mil trace @≈70°C | ≈7.5 mm (≈30×W) | §4.4.1 p.32 |
| 1 A | 6.25e18 electrons/s | §3.2 p.18 |
### 2.5b Appendix D — detailed IPC-2152 fit coefficients, ΔT = const * W^a1 * Th^a2 * I^a3 (W, Th mil; I A; ΔT °C), p.220

| Trace set | Cu weight | const | a1 (W) | a2 (Th) | a3 (I) | Width condition |
|---|---|---|---|---|---|---|
| External | all | 215.3 | −1.15 | −1.00 | 2.0 | all widths |
| Internal | 0.5 oz | 110 | −1.10 | −1.52 | 2.0 | W ≥ 100 mil |
| Internal | 0.5 oz | 125 | −1.10 | −1.52 | 2.0 | W = 50 mil |
| Internal | 0.5 oz | 130 | −1.10 | −1.52 | 2.0 | W ≤ 20 mil |
| Internal | 1 oz | 200 | −1.10 | −1.52 | 1.9 | all |
| Internal | 2 oz | 300 | −1.15 | −1.52 | 2.0 | all |
| Internal | 3 oz | 429 | −1.10 | −1.52 | 1.9 | W ≥ 50 mil |
| Internal | 3 oz | 368 | −1.10 | −1.52 | 1.9 | W < 50 mil |
| Vacuum | 0.5 oz | 210 | −1.10 | −1.52 | 1.9 | W ≤ 100 mil |
| Vacuum | 0.5 oz | 215 | −1.10 | −1.52 | 1.9 | W = 150 mil |
| Vacuum | 0.5 oz | 225 | −1.10 | −1.52 | 1.9 | W = 200 mil |
| Vacuum | 0.5 oz | 235 | −1.10 | −1.52 | 1.9 | W = 500 mil |
| Vacuum | 2 oz | 480 | −1.10 | −1.52 | 1.9 | all |
| Vacuum | 3 oz | 460 | −1.10 | −1.52 | 1.95 | all |

Author's note (p.219): width-dependent differences are small and probably reflect graphical/manipulation errors and material variation. No 1-oz vacuum data exist. Internal fits: "not exactly equal" across widths; suspected test-control issue in IPC study (p.48).

### 2.5c Internal/external relation and depth correction (§7.4, p.82–86)

| Relation | Formula | Units / range |
|---|---|---|
| Mid-board internal rise from external rise | ΔTi = 0.82 * Th^0.053 * W^0.021 * ΔTe^0.976 | Th, W mil; ΔT °C; regression on IPC-2152 1/2/3-oz data |
| Ratio form | ΔTi/ΔTe = 0.82 * Th^0.053 * W^0.021 * ΔTe^-0.024 | e.g. 1 oz, 20 mil, ΔTe = 40 → 0.81 |
| Depth fraction | Fraction = (ΔTe − ΔTi)/(ΔTe − ΔTi_min) = 1.41 * Depth^0.5 | Depth = trace depth / board thickness, 0 < Depth ≤ 0.5 (→ 1.0 at 0.5) |
| Internal rise at depth | ΔTi(depth) = ΔTe − (ΔTe − ΔTi_min) * Fraction | example: depth 0.2 → 0.63; book reads 42.5% at 0.1 (formula: 44.6%) |

### 2.6b Heat-transfer coefficient (HTC, convection + radiation) values used/calibrated (W/m²·K)

| Condition | HTC | Source |
|---|---|---|
| Base value, low current, still air | 10 | §6.3 p.53 |
| Calibrated range, external & internal IPC traces (rises with temperature) | 11–14 (11 at ≈40–60°C rise) | §6.3 Fig.6.2; §7.2.11 p.73; §7.3.3 p.78 |
| Vacuum (radiation only) | 5–9 (6 representative) | §6.4 p.60; §7.3.3 p.78 |
| Supplemental cooling (undefined airflow) | 18–28 used for illustration | §7.2.11 Table 7.5; §7.3.3 |
| Appendix E chart model | 10–14 | App. E p.221 |
| Effect of HTC 11→14 at high temperature | ≈10°C (up to 20°C) | §6.3 p.53–54 |

### 2.8 Layout sensitivity tables (Ch.7; standard model: 100-mil trace, 1.9 mil, 6 in, 63-mil board k 0.68/0.51, 9.35 A unless noted; absolute °C, 20°C ambient)

Table 7.1 — trace length (p.65)

| Test condition | Center temperature (°C) |
|---|---|
| 6-in trace, measured | 67.0 |
| 6-in trace, simulated | 69.2 |
| 4-in, simulated | 68.0 |
| 2-in, simulated | 60.9 |
| 2-in, simulated, plane under pads | 59.3 |
| 1-in, simulated | 49.0 |
| 1-in, simulated, plane under pads | 46.3 |

Table 7.2 — dimensional uncertainty, 27-mil trace, 4.75 A (p.69)

| Thickness | Temperature (°C) |
|---|---|
| 1.9 mil (nominal) | 77.8 |
| 2.7 mil (actual, microsectioned) | 56.2 |

Table 7.3 — underlying plane (p.70)

| Plane position | Trace temperature (°C) |
|---|---|
| No plane | 69.2 |
| Bottom of board (opposite side, 63 mil) | 54.1 |
| 10 mil under trace | 45.9 |

Table 7.4 — parallel trace (100 mil, 8-mil gap) and plane (8 mil under) (p.72)

| Condition | Driven trace (°C) | Adjacent trace (°C) |
|---|---|---|
| Single trace | 69.2 | — |
| Single trace over plane | 45.9 | — |
| Parallel trace | 65.0 | 55.0 |
| Parallel trace over plane | 45.7 | 43.0 |

Table 7.5 — HTC (27-mil, 2.7-mil trace, 4.75 A) (p.73)

| HTC (W/m²·K) | Temperature (°C) |
|---|---|
| 14 | 56.2 |
| 20 | 51.1 |
| 28 | 46.9 |

Table 7.6 — summary of sensitivity simulations (p.74)

| Simulation model | Basic trace (°C) | Parallel/adjacent (°C) |
|---|---|---|
| 6 inch | 69.2 | |
| 4 inch | 68.0 | |
| 2 inch | 60.9 | |
| 2 inch with sink (plane under pads) | 59.3 | |
| 1 inch | 49.0 | |
| 1 inch with sink | 46.3 | |
| 6 inch, gradient measured adjacent to pad | 44.8 | |
| With opposite plane | 54.1 | 43.3 (plane max) |
| With underlying plane | 45.9 | 44.7 (plane max) |
| Parallel trace | 62.0 (text: ≈65) | 55.0 (adjacent trace max) |
| Parallel + plane | 45.7 | 43.0 |
| Split power trace (2 × 50 mil) | 64.7 | 59.1 (dielectric between) |
| With air flow (very approximate) | 46.9 | |

Table 7.7 — material parameter partial sensitivities (base model: 100 mil × 1 oz × 6 in, FR4 63 mil, 7 A, ρ 1.68 μΩ·cm, HTC 11, k 0.6/0.4, ≈40°C rise) (p.82)

| Change in temperature (°C) | For each |
|---|---|
| 1.0 | 2% Δ resistivity |
| 3.0 | 0.1-mil Δ thickness |
| 5.0 | HTC between 11 and 14 |
| 5.6 | thermal conductivity coefficient 0.5 → 0.7 W/m·K |

Other Ch.7 anchors: 10.7% ρ increase → 8.1% temperature increase (p.87); Δk = 0.3 W/m·K → ≈10°C at ≈50°C rise (p.87); 1°C per 0.03 mil thickness (p.80); two planes at 20 & 40 mil: 56.7 → 34.5°C (p.77); transient 1 oz/200 mil/15 A: 94.6°C final, 90% at ≈3.5 min, 95% at ≈5 min (p.66).

### 2.9 Via temperature tables (Ch.8; 63-mil FR4; single via 0.26-mm drill, 0.030-mm wall, A = 0.0217 mm²; absolute °C at 20°C ambient)

Table 8.2 — single via, 1-oz traces (p.94)

| Width (mm) | Current (A) | Thermocouple/trace (°C) | Via top (°C) | Via midpoint (°C) |
|---|---|---|---|---|
| 0.40 | 2.0 | 91.4 | 83.2 | 82.4 |
| 0.40 | 2.3 | 123.2 | 111.1 | 109.9 |
| 0.66 | 3.0 | 86.9 | 81.4 | 80.9 |
| 0.66 | 4.0 | 166.7 | 154.1 | 152.9 |
| 1.2 | 3.0 | 47.9 | 48.6 | 48.7 |
| 1.2 | 4.0 | 74.1 | 75.7 | 75.8 |
| 1.2 | 5.0 | 115.5 | 118.8 | 118.8 |
| 1.8 | 5.0 | 70.8 | 76.8 | 76.8 |
| 1.8 | 6.0 | 100.2 | 110.2 | 110.2 |
| 2.5 | 6.0 | 68.1 | 77.6 | 77.6 |
| 2.5 | 7.0 | 90.3 | 104.9 | 104.9 |

Table 8.4 / 8.5 — 2-oz, 2.5-mm trace, single small via (p.96)

| Current (A) | Trace (°C) | Via top (°C) | Via midpoint (°C) |
|---|---|---|---|
| 5.0 | 37.1 | 40.3 | 41.1 |
| 7 | 51.3 | 59.0 | 60.8 |
| 10 | 93.5 | 113.2 | 117.9 |

Table 8.6 — 2.5-mm trace, two vias (p.97)

| Cu (oz) | Current (A) | Trace (°C) | Via top (°C) | Via midpoint (°C) |
|---|---|---|---|---|
| 1.0 | 6.0 | 67.1 | 69.5 | 69.5 |
| 1.0 | 7.0 | 88.6 | 92.3 | 92.4 |
| 2.0 | 6.0 | 41.3 | 43.3 | 43.5 |
| 2.0 | 7.0 | 49.9 | 52.7 | 53.0 |
| 2.0 | 10 | 89.6 | 96.5 | 97.3 |

Table 8.7 / 8.8 — test board (≈60-mil FR4, 0.5-oz foil + 1-oz plating, Th 2.1 mil top / 2.9 mil bottom, k 0.679/0.512, single 10-mil via) (p.99–101)

| Width (mil) | Current (A) | Sim trace (°C) | Sim via (°C) | Sim via/trace (%) | Measured trace (°C) | Measured via (°C) |
|---|---|---|---|---|---|---|
| 27 | 4.75 | 72.8 | 70.1 | 96.3 | 66 | 64.5 |
| 27 | 6.65 | 114.2 | 108.2 | 94.7 | 114 | 109 |
| 200 | 4.75 | 30.8 | 31.8 | 103.2 | 30.5 | 31.5 |
| 200 | 8.55 | 44.8 | 48.1 | 107.4 | 40.5 | 44.5 |

Table 8.9 — thermal vias (60 × 120 mm, 1.5-mm FR4, 20 × 20 mm 1-oz pad, 40 A; 0.5-mm solid-copper vias; 20°C ambient) (p.105)

| Simulation | Pad T (°C) | Pad ΔT (°C) | Plane/sink T (°C) | Plane/sink ΔT (°C) |
|---|---|---|---|---|
| No plane or via | 82.1 | 62.1 | n/a | n/a |
| Small plane only | 79.6 | 59.6 | 73.5 | 53.5 |
| Small plane + 1 via | 78.7 | 58.7 | 76.0 | 56.0 |
| Small plane + 5 vias | 67.5 | 47.5 | 66.0 | 46.0 |
| Large plane only | 43.0 | 23.0 | 35.8 | 15.8 |
| Large plane + 1 via | 42.1 | 22.1 | 38.7 | 18.7 |
| Large plane + 5 vias | 36.4 | 16.4 | 34.7 | 14.7 |
| Heat sink (20°C) only | 29.5 | 9.5 | 20.0 | 0.0 |
| Heat sink + 1 via | 28.1 | 8.1 | 20.0 | 0.0 |
| Heat sink + 5 vias | 24.2 | 4.2 | 20.0 | 0.0 |
| Special (20°C-clamped) via | 42.6 | 22.6 | n/a | n/a |

Conduction comparison (eq. 8.4–8.6): Q/t = k*A*ΔT/d; (kA)_pad/(kA)_via = (0.5 × 400 mm²)/(385 × 0.196 mm²) = 2.65; A/d = 267 mm (pad) vs 0.131 mm (via) across d = 1.5 mm.

Via voltage drop anchors (§8.6): 0.66 mm × 1 oz × 115 mm at 3 A, 86°C: R20 = 0.0897 Ω, R86 = 0.11339 Ω, V = 0.34 V (sim 0.34 no via / 0.32 with via / 0.00 across via); via ≈ 0.0047 V. 2.5 mm at 7 A, 90°C: R20 = 0.0237 Ω, R90 = 0.0303 Ω, V = 0.212 V; via ≈ 0.011 V.

Table 14.2 — constant-via-temperature simulation (80 × 12 × 1.6 mm board, 0.04-mm copper, 0.26-mm via with 0.04-mm wall, printed A_via = 0.02675 mm²) (p.169)

| Trace W (mm) | Current (A) | T trace (°C) | T via (°C) | J trace (A/mm²) | J via (A/mm²) |
|---|---|---|---|---|---|
| 0.6 | 2.74 | 61.2 | 60.4 | 114.2 | 99.1 |
| 0.7 | 2.95 | 59.5 | 59.4 | 105.4 | 106.7 |
| 1.0 | 3.57 | 58.6 | 60.5 | 89.3 | 129.1 |
| 2.0 | 5.25 | 56.5 | 60.5 | 65.6 | 189.9 |
| 3.0 | 6.5 | 54.8 | 59.8 | 54.2 | 235.1 |
| 4.0 | 7.5 | 53.7 | 60.0 | 46.9 | 271.2 |
| 5.0 | 8.4 | 52.7 | 59.6 | 42.0 | 303.8 |

Via current split (Ch.9, 4 A total, 4 vias, 0.9-mm trace): straight-through ≈0.98 A each; 90° turn: 1.14 / 0.96 / 0.96 / 0.72 A. Single-via wall current density at entry layer: 223.7 (leading) … 140.4 (trailing) A/mm², avg 181.0; mid-depth uniform 181.3 A/mm².

### 2.10 Ch.10 layout options (220 × 20 × 1.55 mm polyimide board, 1-oz top/bottom, 1.0-mm (40-mil) × 150-mm trace, 4 A, 20°C ambient)

Table 10.1 — copper under the trace (p.119)

| Case | Temperature (°C) | ΔT (°C) | % ΔT improvement |
|---|---|---|---|
| A simple trace | 53.2 | 33.2 | 0.0 |
| B same-width trace on the layer under | 52.95 | 32.95 | 0.8 |
| C 3×-wider (120 mil) trace under | 49.2 | 29.2 | 12.0 |
| D full plane, bottom layer | 44.8 | 24.8 | 25.3 |
| E full plane, layer directly under | 39.5 | 19.5 | 41.3 |

Stubs (§10.5): nine 5.0-mm-wide stubs on the 1.0-mm trace, 15-mm pitch: 53.2 → 44.4°C (ΔT 33.2 → 24.4, −26.5%).

Table 10.2 — connecting links (11-mil-wide short link) (p.123)

| Case | Temperature (°C) | ΔT (°C) |
|---|---|---|
| Basic trace | 53.2 | 33.2 |
| Single link (A) | 74.6 | 54.6 |
| Single link + 40 × 6 mm copper under (C) | 60.0 | 40.0 |
| Second parallel link (B) | 59.3 | 39.3 |

### 2.11 Fusing constants and tables

| Item | Value | Source |
|---|---|---|
| Preece constant a (copper), I = a * d^1.5, d in inch | 10244 | §11.3 eq.(11.1) |
| Preece area form, I = 12277 * A^0.75, A in in² | 12277 | §11.3 eq.(11.2) |
| Onderdonk, general: 33 * (I/A_cmil)² * S = log10(ΔT/(234 + Ta) + 1); Ta = 40°C → /274 | 33 (printed), 33.5 (derived, App. G) | §11.4 eq.(11.3),(11.4); App. G eq.(G.22) |
| Fusing temperature (Cu melt) | 1083°C (Table 3.1: 1084) | §12.3 |
| Onderdonk in mil², Tref 20°C | t = 0.0346 * (A/I)² | §12.5.1 eq.(12.3) |
| cp (Cu) | 385 J/kg·K | Table G.1 |
| density (Cu) | 8900 kg/m³ | Table G.1 |
| ρ20 (Cu) used in derivation | 1.72e-8 Ω·m (also written 1.75e-8) | Table G.1, p.247 |
| α20 (Cu) used in derivation | 0.00393 /K | Table G.1 |
| α20*ρ20/(cp*ρd) | 1.973e-17 (SI) | p.247 |
| 1 m² in circular mils | 1.98e9 (elsewhere 19.736e8) | p.247, p.131 |
| Circular mil | A_cmil = d_mil²; 1 mil² = 1.273 cmil; 1 cmil = 0.7854 mil² = 5.067e-10 m² = 5.067e-4 mm² | §11 note 8 |

Table G.2 — log10 denominator (234 + Tref)

| Reference temperature (°C) | Denominator |
|---|---|
| 20 | 254 |
| 40 | 274 |
| 85 | 319 |
| 105 | 339 |

Table G.3 — c in t = c * (A/I)² (t s, I A; melt at 1083°C)

| Tref (°C) | c, A in circular mil | c, A in mil² | c, A in mm² |
|---|---|---|---|
| 20 | 0.0213 | 0.0346 | 8.30e4 |
| 40 | 0.0203 | 0.0330 | 7.92e4 |
| 85 | 0.0184 | 0.0298 | 7.15e4 |
| 105 | 0.0176 | 0.0285 | 6.85e4 |

Table 12.1 — ratio of simulated PCB-trace fusing current to Onderdonk current (63-mil FR4, 6-in trace, no planes) (p.141)

| Cu (oz) | Width (mil) | Area (mil²) | 0.5 s | 1.0 s | 2.0 s | 3.0 s | 4.0 s | 5.0 s |
|---|---|---|---|---|---|---|---|---|
| 2 | 20 | 52 | 3.46 | 3.87 | 4.65 | 5.30 | 5.84 | 6.30 |
| 1 | 20 | 26 | 2.24 | 2.45 | 3.03 | 3.53 | 3.83 | 4.20 |
| 1 | 100 | 130 | 2.02 | 2.14 | 2.45 | 2.69 | 3.02 | 3.15 |
| 1 | 200 | 260 | 1.88 | 2.04 | 2.37 | 2.62 | 2.77 | 2.97 |
| 2 | 200 | 520 | 1.57 | 1.67 | 1.90 | 2.05 | 2.20 | 2.37 |
| 2 | 100 | 260 | 1.51 | 1.63 | 1.82 | 1.98 | 2.10 | 2.20 |

(1 oz = 1.35 mil, 2 oz = 2.7 mil in these simulations.) Trace model t*(I/A)² ≤ 0.25 during first 3 s except 1 oz × 20 mil (p.140). Plane 12 mil under trace: +30–100% fusing time; opposite-side plane: no effect (p.138).

Experimental fusing anchors (§12.8): 15 mil × 0.5 oz, 6 A → 2.75 s (sim 4 s); 20 mil × 1.5 oz (1.9–2.6 mil), 8.5 A → ≈30 min, 8.4 A → 1 h 16 min, 8.3 A → no runaway in 2 h; plateau ≈250°C before runaway.

### 2.12 Hot-spot test set — Table 13.1 (p.156)

| Width (mil) | Foil (oz) | Plating (oz) | Total nominal Th (mil) | Current (A) | Max temperature (°C) |
|---|---|---|---|---|---|
| 100 | 0.5 | — | 0.65 | 5.6 | 53.0 |
| 100 | 0.5 | 1.0 | 1.9 | 8.0 | 54.0 |
| 100 | 1.5 | — | 2.0 | 7.5 | 54.5 |
| 100 | 1.5 | 1.75 | 4.4 | 10.0 | 47.0 |
| 200 | 2.0 | — | 2.6 | 10.0 | 39.0 |
| 200 | 2.0 | 1.0 | 3.9 | 10.0 | 35.0 |
| 200 | 2.0 | 2.0 | 5.2 | 10.0 | 33.6 |

Corner model (§13.4): 200-mil, 1-oz trace, 1.5-mm FR4, 8 A → ≈44°C; inside–outside corner difference 0.5–1.5°C.

### 2.13 Form factor — Table 14.1 (eq. 5.5; A = 390 mil², I = 15 A, J = 0.0385 A/mil²) (p.168)

| Cu (oz) | Th (mil) | Width (mil) | ΔT (°C) |
|---|---|---|---|
| 0.5 | 0.65 | 600 | 47.5 |
| 1.0 | 1.3 | 300 | 52.8 |
| 1.5 | 1.95 | 200 | 56.1 |
| 2.0 | 2.6 | 150 | 58.6 |
| 3.0 | 3.9 | 100 | 62.3 |
| 4.0 | 5.2 | 75 | 65.0 |
| 5.0 | 6.5 | 60 | 67.2 |

### 2.14 AC / pulsed current (Ch.15)

Table 15.1 — duty cycle (26-mil × 2.9-mil trace; k 0.7 W/m·K; 2000 kg/m³; 900 J/kg·K; 26°C ambient; 5 A peak; 1.464 W at 5 A) (p.172)

| Duty cycle (%) | RMS current (A) | Max temperature (°C) |
|---|---|---|
| 100 | 5.000 | 65.7 |
| 99 | 4.975 | 65.3 |
| 90 | 4.743 | 61.2 |
| 80 | 4.472 | 56.8 |
| 70 | 4.183 | 52.6 |
| 60 | 3.873 | 49.5 |
| 50 | 3.536 | 45.4 |
| 40 | 3.162 | 41.2 |
| 30 | 2.739 | 37.3 |
| 20 | 2.236 | 33.8 |
| 10 | 1.581 | 29.8 |
| 1.0 | 0.50 | 26.0 |

RMS factors (§15.4.2): pulse train (A1 − A0)*sqrt(D); 50% square = peak; sine 0.707 × peak; triangle/sawtooth 0.577 × peak; with offset sqrt(rms² + dc²).

Table 15.3 — analog waveforms, 100-mil × 0.5-oz × 6-in trace, 100 Hz (p.185)

| Waveform | Max V | Min V | RMS current (A) | Trace temperature (°C) |
|---|---|---|---|---|
| Sine | 7.5 | 2.1 | 5.39 | 65.5 |
| Sawtooth | 7.15 | 2.0 | 5.68 | 68.5 |
| Square 50% | 7.0 | 2.25 | 5.11 | 62.0 |
| Square 75% | 7.68 | 2.25 | 6.12 | 75.0 |
| Square 99% | 7.9 | 2.25 | 7.27 | 97.0 |

Frequency independence verified 0.05 Hz–10 kHz (50% duty, ≈45°C) and 0.5–1000 Hz (analog); thermal inertia makes cycles > ≈10 Hz invisible.

### 2.15 Appendix B thickness and resistivity (200-mil × 5-in traces, 2.1 A, 24.5°C → 20°C)

Table B.1 — thickness variation (mil; six points across width; ±0.2–0.3 mil)

| | 2.0 oz foil (nom 2.3) | 3.0 oz = foil + 1 oz plating (nom 3.9) | 4.0 oz = foil + 2 oz plating (nom 5.2) |
|---|---|---|---|
| Maximum | 2.8 | 4.3 | 5.7 |
| Minimum | 1.9 | 3.0 | 4.3 |
| Overall average | 2.4 | 3.6 | 4.7 |

Table B.2 — calculated resistivities (μΩ·cm)

| | 2.0 oz | 3.0 oz | 4.0 oz |
|---|---|---|---|
| Average resistivity (24.5°C) | 1.806 | 1.786 | 1.766 |
| Adjusted to 20°C | 1.788 | 1.758 | 1.739 |
| Expected (foil 1.788 ∥ plating 1.7) | 1.788* | 1.752 | 1.739 |

*taken as the foil value.

### 2.16 Simulation model parameter sets used in the book (for solver correlation)

| Model | Board | Dielectric, k (W/m·K) | Copper | Trace | HTC | Ambient | Result | Source |
|---|---|---|---|---|---|---|---|---|
| IPC 2-oz external replica | 350 × 45 × 1.6 mm (4 × 400 μm) | polyimide 0.53/0.53 | 68 μm | 300 × 5 mm, sense 250 mm apart | 11 | 20°C | 16 A → 65.5°C | §6.4 |
| Ch.7 standard (test board) | 192 × 25 mm × 63 mil | 0.68 xy / 0.51 z (measured) | 1.9 mil nominal | 6 in × 27/100/200 mil, pads 13 × 7.8 mm | 12–14 | 20°C | 100 mil, 9.35 A → 69.2°C | §7.2.3 |
| Ch.7 material base | 6.5 × 2 in × 63 mil FR4 | 0.6 xy / 0.4 z | 1 oz, ρ 1.68 μΩ·cm | 100 mil × 6 in | 11 | 20°C | 7 A → ≈57–60°C | §7.3 |
| Ch.8 via model | few mm wide × 1.6 mm FR4 | FR4 | 1 oz; via 0.26 mm/0.030 mm | 2 × 60 mm, W 0.40–2.5 mm | — | 20°C | Table 8.2 | §8.3.2 |
| Ch.8 thermal-via | 60 × 120 × 1.5 mm FR4 | ≈0.5 | 1-oz pad 20 × 20 mm | 40 A | — | 20°C | 82.1°C bare | §8.7 |
| Ch.9 current-density | 1.61 mm (7 × 230 μm) FR4 | FR4 | 34 μm; via 0.26/0.03 mm (0.021677 mm²) | 0.33 mm (13 mil) / 0.9 mm (35 mil) | — | — | 4 A | §9.3–9.4 |
| Ch.10 layout | 220 × 20 × 1.55 mm | polyimide | 38 μm top/bottom | 150 × 1.0 mm | — | 20°C | 4 A → 53.2°C | §10.3 |
| Ch.12 fuse (adiabatic) | none (two Cu layers, no dielectric) | — | 1 oz (1.35 mil), 2 oz (2.7 mil) | 200 mil long × 20/100/200 mil | 0 | 20°C | = Onderdonk | §12.5 |
| Ch.12 trace | 63-mil FR4, 3 mm margins | FR4 | 1 / 2 oz | 155 mm × 20/100/200 mil | 10 | 20°C | Table 12.1 | §12.5.2 |
| Ch.13 corner | 1.5-mm FR4 | FR4 | 35 μm | 5 mm wide, 8 A | — | 20°C | ≈44°C | §13.4.1 |
| Ch.14 via constant-T | 80 × 12 × 1.6 mm | FR4 | 0.04 mm; via 0.26/0.04 mm | 32 + 32 mm, 0.6–5 mm | — | — | Table 14.2 | §14.9 |
| Ch.15 AC | — | k 0.7, 2000 kg/m³, 900 J/kg·K | 2.9 mil | 26 mil | — | 26°C | 5 A → 65.7°C | §15.2 |
| App. E charts | 200 × 110 × 1.6 mm | polyimide 0.58/0.58 | ρ 1.75e-8 Ω·m, α 0.00394 | 150 mm | 10–14 | — | charts 0.25–5 oz | App. E |
<!-- TABLES-APPEND -->

## 3. Mechanizable checks
Conventions for all checks: W, Th in mil; I in A (RMS); ΔT in °C; T_amb in °C; A in mil² unless stated; t in s. `oz_to_mil(oz) = 1.3 * oz` (book default; use fabricator's actual/minimum thickness when known). Margin is always (allowed − actual)/allowed unless stated.

**CHECK-TRACE-DT-EXTERNAL** — steady-state rise of an outer-layer trace (worst case, bare board, still air)
- inputs: I_rms [A], W [mil], Th [mil]
- formula: `dT = 215.3 * I**2 * W**-1.15 * Th**-1.0`
- pass: `dT <= dT_limit` (policy; typical 20–40°C) and `T_amb + dT <= T_max_material`
- margin: `1 - dT/dT_limit`; current margin `I_allow = sqrt(dT_limit * W**1.15 * Th / 215.3)`, `I_allow/I - 1`
- validity: IPC-2152 range 0.5–3 oz, widths ≈ 5–500 mil, ΔT ≤ ≈100°C; equation fitted to 2-oz and 3-oz data, extrapolated to 1 oz and to 0.25–5 oz in App. E. Real boards with planes/adjacent copper run cooler (see CHECK-PLANE-COOLING-CREDIT).
- source rows: BROOKS-046, -047, -053, -055, -066, -122

**CHECK-TRACE-DT-INTERNAL** — steady-state rise of an inner-layer trace at mid-board
- inputs: I, W, Th, oz (0.5, 1, 2, 3)
- coefficients (K, a, b, c) per Appendix D table §2.5b; `dT = K * I**a * W**b * Th**c`
  - 0.5 oz: K = 130 (W ≤ 20), 125 (W = 50), 110 (W ≥ 100) — interpolate linearly in W between; a=2, b=−1.10, c=−1.52
  - 1 oz: K=200, a=1.9, b=−1.10, c=−1.52
  - 2 oz: K=300, a=2, b=−1.15, c=−1.52
  - 3 oz: K=429 (W ≥ 50), 368 (W < 50); a=1.9, b=−1.10, c=−1.52
  - other thicknesses: interpolate K linearly in Th between the bracketing weights and use the thicker weight's exponents (`conf=medium`); or use CHECK-TRACE-DT-INTERNAL-FROM-EXTERNAL
- pass / margin: as CHECK-TRACE-DT-EXTERNAL
- alternative (any Th, W): `dTi_min = 0.82 * Th**0.053 * W**0.021 * dTe**0.976` with dTe from CHECK-TRACE-DT-EXTERNAL
- source rows: BROOKS-048, -075, -137

**CHECK-TRACE-DT-INTERNAL-DEPTH** — inner trace not at board center
- inputs: dTe (external rise for same I, W, Th), dTi_min (from CHECK-TRACE-DT-INTERNAL or eq. 7.2), depth_mil, board_mil
- formula: `Depth = min(depth_mil, board_mil - depth_mil) / board_mil` (0 < Depth ≤ 0.5); `Fraction = min(1.0, 1.41 * Depth**0.5)`; `dTi = dTe - (dTe - dTi_min) * Fraction`
- pass: `dTi <= dT_limit`
- caveat: derived from IPC-2152 materials; guide only (`conf=high` formula, `medium` applicability to other laminates)
- source rows: BROOKS-076

**CHECK-TRACE-DT-VACUUM** — trace in vacuum/space (any layer)
- inputs: I, W, Th, oz
- coefficients: 0.5 oz K = 210 (W ≤ 100), 215 (150), 225 (200), 235 (500) — interpolate; a=1.9, b=−1.10, c=−1.52. 2 oz: K=480, a=1.9, b=−1.10, c=−1.52. 3 oz: K=460, a=1.95, b=−1.10, c=−1.52. 1 oz: no data — use K=480 with 2-oz exponents as conservative (`conf=low`, derived).
- pass / margin: as external. Sanity: dT_vac > dT_ext > dT_int for the same trace.
- source rows: BROOKS-049, -050, -031, -137

**CHECK-TRACE-WIDTH-FOR-DT** — minimum width for a ΔT limit
- inputs: I, Th, dT_limit, layer (ext/int/vac), oz
- formula (external): `W_min = (215.3 * I**2 / (dT_limit * Th)) ** (1/1.15)`; internal/vacuum: `W_min = (K * I**a / (dT_limit * Th**1.52)) ** (1/|b|)` with K chosen for the resulting width band (iterate once)
- then apply CHECK-TRACE-WORSTCASE-DIMENSIONS to the chosen W
- pass: `W_design >= W_min`; margin `W_design/W_min - 1`
- source rows: BROOKS-046, -048, -049

**CHECK-TRACE-WORSTCASE-DIMENSIONS** — tolerance-adjusted rise
- inputs: W_nom, Th_nom, layer_type (foil-only inner vs plated outer), etch_tol_mil (default 1.0; use 2.0 if unknown), plating_tol (default 0.2; up to 0.5 if fabricator uncontrolled), foil_tol 0.10, rho_tol (default +6% = rolled 1.78 vs 1.68)
- formula: `W_wc = W_nom - etch_tol`; `Th_wc = Th_nom * (1 - foil_tol)` for foil-only, `Th_wc = Th_foil*(1-0.10) + Th_plate*(1-plating_tol)` for plated; `dT_wc = dT(I, W_wc, Th_wc) * (1 + 0.76 * rho_tol)`
- pass: `dT_wc <= dT_limit`; warn if `W_nom <= 10 mil` and `dT_wc/dT_nom > 1.3`
- source rows: BROOKS-011, -013, -014, -027, -056, -060, -070, -073, -117, -135

**CHECK-TRACE-RESISTANCE-AT-T** — DC resistance at operating temperature
- inputs: L [in], W [mil], Th [mil], T [°C], rho_uohm_in (default 0.67 = 1.70 μΩ·cm; ED 0.64–0.65, rolled 0.685–0.70), alpha (default 0.0040 /°C at 20°C; 0.00393 for derivations)
- formula: `R20 = rho_uohm_in * 1e-6 * L / (W * 1e-3 * Th * 1e-3)` (≡ `0.68 * L/(W*Th)` at ρ = 1.72 μΩ·cm); `R_T = R20 * (1 + alpha * (T - 20))`
- for T > 200°C use α from Table 3.1 (0.0041–0.0048) or ρ(T) directly from Table 3.1
- multi-layer (foil + plating): `R = 1 / (1/R_foil + 1/R_plate)` with ρ_foil ≈ 1.79, ρ_plate = 1.70 μΩ·cm
- pass: user PDN budget; report `V_drop = I * R_T`, `P = I**2 * R_T`
- source rows: BROOKS-001, -002, -023, -024, -025, -136

**CHECK-TRACE-VDROP** — voltage drop including temperature
- inputs: I, L, W, Th, T_amb, dT (from CHECK-TRACE-DT-*), V_budget
- formula: `V = I * R_T(T_amb + dT)`; for the via in series: `V_via ≈ V * L_via/L` (negligible; e.g. 0.0047 V for 63-mil via vs 0.34 V trace)
- pass: `V <= V_budget`; margin `1 - V/V_budget`
- source rows: BROOKS-089, -090

**CHECK-PULSED-RMS** — equivalent current for non-DC waveforms
- inputs: waveform type, I_peak (or A1, A0), duty D, dc offset, frequency f
- formula: square/pulse `I_eq = I_pk * sqrt(D)`; sine `0.707 * I_pk`; triangle/sawtooth `0.577 * I_pk`; with offset `sqrt(I_ac_rms**2 + I_dc**2)`; arbitrary sampled waveform `sqrt(mean(i**2))`
- applicability: `f >= 10 Hz` → steady-state with I_eq. `f < 1 Hz` or single pulses → transient: thermal time constant such that 90% of final rise at ≈3.5 min, 95% at ≈5 min (1 oz/200 mil/15 A); single pulses ≤ 5 s → CHECK-PULSE-ADIABATIC-RISE / CHECK-FUSING-*
- pass: feed I_eq to CHECK-TRACE-DT-*
- source rows: BROOKS-005, -057, -124, -125, -126, -127

**CHECK-PULSE-ADIABATIC-RISE** — upper bound on temperature rise for a short pulse (no cooling, Onderdonk form)
- inputs: I [A], A [mil²], t [s], Tref [°C] (initial trace temperature)
- formula: `Theta = (234 + Tref) * (10 ** (20.67 * (I/A)**2 * t) - 1)` (20.67 = 33.5/1.273²; for A in circular mils use 33.5; for A in m² use `ln(1 + 0.00393*Theta) = 1.973e-17 * (I/A)**2 * t`)
- pass: `Tref + Theta <= T_limit` (e.g. stay below Tg or the 220°C runaway band); reaching Θ = 1083 − Tref means fusing
- note: conservative for t ≤ ≈1 s on a PCB; for 1–5 s real rises are lower (cooling into the board, Table 12.1); beyond 5 s use steady-state checks
- source rows: BROOKS-101, -104, -139, -141

**CHECK-FUSING-ONDERDONK** — adiabatic time to reach melting
- inputs: I, A [mil²] (or cmil / mm²), Tref
- formula: `t_melt = c(Tref) * (A/I)**2` with c = 0.0346 (20°C), 0.0330 (40°C), 0.0298 (85°C), 0.0285 (105°C) for A in mil²; ×0.6154 for cmil; ×2.4e6 for mm² (Table G.3). General: `t = log10((1083 - Tref)/(234 + Tref) + 1) / (33.5 * (I/A_cmil)**2)`
- inverse: `I_fuse(t) = A * sqrt(c/t)`
- pass (overload survival I_ov for t_ov): `t_melt(I_ov) >= t_ov` — lower bound on real behavior (real traces last 1.5–6× longer)
- margin: `t_melt/t_ov - 1` or `I_fuse(t_ov)/I_ov - 1`
- source rows: BROOKS-101, -104, -105, -141

**CHECK-FUSING-PCB-TRACE** — realistic fusing current for a trace on 63-mil FR4 (no nearby plane)
- inputs: I_ov, t_ov (0.5–5 s), A [mil²], oz
- formula: `I_fuse_trace(t) = ratio(A, oz, t) * A * sqrt(0.0346/t)` where ratio is Table 12.1 (interpolate in ln(A) and t; rows: 26, 52, 130, 260(1 oz), 260(2 oz), 520 mil²). Outside 0.5–5 s or A outside 26–520 mil²: use ratio = 1.0 (Onderdonk) → conservative. Plane ≤ 12 mil below: multiply fusing TIME by 1.3 (conservative end of 30–100%).
- pass: `I_ov <= I_fuse_trace(t_ov)`; margin `I_fuse_trace/I_ov - 1`
- note: simulation-derived; experiments show fast fusing 1.5× shorter than sim (2.75 s vs 4 s). Suggested policy factor ≥ 1.5 on current.
- source rows: BROOKS-107, -108, -110, -113

**CHECK-SHORT-TIME-SURVIVAL** — simple rule for "must carry I for t seconds" (t ≤ 3 s)
- inputs: I, t, A (or W, Th)
- formula: `x = t * (I/A)**2`; pass if `x < 0.15`; marginal 0.15–0.25 (all simulated traces except 1 oz × 20 mil fused above 0.25); fail ≥ 0.25. Sizing: `A_min = I * sqrt(t/0.15)`
- example: 40 A, 1 s → A ≥ 103 mil² → 1-oz (1.35 mil) × 76 mil
- exclude: 1-oz traces ≤ 20 mil wide (use CHECK-FUSING-PCB-TRACE)
- source rows: BROOKS-109

**CHECK-PREECE** — legacy wire fusing current (reference only)
- inputs: d [inch] or A [in²]
- formula: `I = 10244 * d**1.5` = `12277 * A**0.75`
- use: comparison point only (round wire in air, slow heating); not a PCB design rule
- source rows: BROOKS-100

**CHECK-TRACE-MAX-TEMP-MATERIAL** — absolute temperature vs laminate limits
- inputs: T_amb, dT (worst case), Tg, Td, T260/T288 rating, policy_limit
- pass: `T = T_amb + dT <= policy_limit`; AND if `T > 100°C` require Tg, Td, T260 review (BROOKS-018); AND `T < 220°C` hard (onset band of thermal runaway 220–270°C; slow-fusing plateau ≈250°C); AND `T < Td` (300–350°C typical); if `T >= 260°C` possible: `t_exposure <= T260 rating`
- margin: `min(policy_limit, 220) - T`
- source rows: BROOKS-018, -019, -020, -042, -112, -114

**CHECK-VIA-AREA** — conducting cross-section of a plated via
- inputs: drill_d [mm or mil], wall_th (use MINIMUM plating; nominal 0.5–1 oz = 0.65–1.3 mil = 0.0165–0.033 mm)
- formula: `A_via = pi * (r**2 - (r - th)**2)`, r = drill_d/2. Reference: 10-mil drill, 0.030-mm wall → 0.0217 mm² ≈ 1-oz × 26-mil trace
- pass: informational; feeds CHECK-VIA-TEMP-VS-TRACE and CHECK-VIA-COUNT
- source rows: BROOKS-078, -079

**CHECK-VIA-TEMP-VS-TRACE** — via temperature from the parent trace (book's central result)
- inputs: dT_trace (from CHECK-TRACE-DT-* with real-board credits), A_trace = W*Th, A_via (per via, or n_via * A_via for parallel vias), T_limit
- formula: `ratio = A_trace / A_via_total`; `f = 1.00 if ratio <= 1.1 else 1.04 if ratio <= 2.0 else 1.13 if ratio <= 3.0 else 1.21 if ratio <= 4.0 else 1.35` (envelope over Tables 8.2/8.4/8.5/8.6/8.8 rise ratios: 0.87–0.91 @0.65–1.06; 1.03 @1.9; 1.12 @2.9; 1.20 @4.0; 1.23–1.33 @7.8 single via; 1.10 @3.9 two vias; measured 1.20 @≈12) — `conf=medium`, derived
- `dT_via = f * dT_trace`; pass: `T_amb + dT_via <= T_limit`
- hard rule: a via must always be thermally attached to a trace/plane sized for the current — a via carrying its "own" current alone (0.66-mm-equivalent at 10 A) melts in ≈7.5 s
- via current density up to ≈300 A/mm² is acceptable when the trace is sized for ≈+35–40°C (Table 14.2) — do NOT size vias by current density
- source rows: BROOKS-004, -080 … -087, -123

**CHECK-VIA-COUNT** — number of vias for a layer transition
- inputs: I, A_trace, A_via, geometry (straight-through vs 90° turn), sim_available
- thermal rule (book): `n_via = 1` suffices when the trace passes CHECK-TRACE-DT-* and CHECK-VIA-TEMP-VS-TRACE
- legacy fallback when no thermal check is run (IPC-2152 p.26, extremely conservative): `n_via >= ceil(A_trace / A_via)`
- current sharing: straight-through → `I_via = I/n`; 90° turn → `I_via_max = 1.14 * I/n` (4-via case; farthest via 0.72 I/n)
- pass: `n_design >= n_via` and per-via `I_via_max` fed to CHECK-VIA-TEMP-VS-TRACE
- source rows: BROOKS-077, -085, -094

**CHECK-VIA-VDROP** — via resistance/drop in PDN budgets
- formula: `R_via = rho * L_via / A_via * (1 + alpha*(T-20))`; `V_via = I * R_via` (≈0.0047 V at 3 A for a 63-mil, 0.0217-mm² via; 0.011 V at 7 A)
- pass: negligible unless `L_via / L_trace > 0.05`
- source rows: BROOKS-089, -090

**CHECK-NEIGHBOR-TRACE-HEATING** — passive neighbors of a hot trace
- inputs: dT_driven, gap [mil], plane_under (bool), neighbor T_limit
- formula: `dT_neighbor ≈ 0.80 * dT_driven` for gap ≤ 8 mil without plane (55−20 vs 65−20 → 0.78); `≈ 0.90 * dT_driven` with plane 8 mil below (23/25.7); decay with distance: thermal plume half-width ≈ 7.5–10 mm at ≈70°C, so traces/components within ≈10 mm are coupled (`conf=medium`, derived from Table 7.4 / Fig.4.4)
- pass: `T_amb + dT_neighbor <= neighbor T_limit`
- source rows: BROOKS-033, -061, -062

**CHECK-PLANE-COOLING-CREDIT** — factor on ΔT for copper near the trace (derived from Tables 7.3, 7.4, 10.1, §7.3.1; 40–100-mil traces at 33–49°C rise; `conf=medium`)
- inputs: copper configuration below/above the trace
- factors (multiply IPC ΔT): full plane on opposite side of a 60–63-mil board 0.75 (sims: 0.69, 0.75); full plane ≤ 10 mil below 0.60 (0.53, 0.59); two full planes at 20 & 40 mil 0.40; same-width trace directly below 0.99; 3×-width trace below 0.88; distributed stubs 5:1 width every 15 mm 0.74; short trace 2 in 0.83 (60.9−20)/(69.2−20), 1 in 0.59
- do NOT credit: splitting into parallel/stacked half-width traces (1.0); thermal vias to a plane (≈1.0); airflow without a measured HTC
- pass: `dT_IPC * factor <= dT_limit` (use only when the plane is full-area under the trace's whole length; otherwise factor = 1)
- source rows: BROOKS-059, -061, -063, -069, -093, -097, -098

**CHECK-THERMAL-VIA-BENEFIT** — is adding thermal vias worthwhile?
- inputs: k_diel (≈0.5 FR4), A_pad [mm²], n_via, d_via [mm] (solid or effective copper area), d [mm] board thickness, receiving copper size
- formula: `Q_ratio = (k_diel * A_pad) / (385 * n_via * pi * (d_via/2)**2)`; e.g. 20 × 20 mm pad vs one 0.5-mm via → 2.65
- pass/decision: if the receiving copper is a large plane or heat sink, expect only marginal improvement from vias (Table 8.9: +5 vias, large plane: ΔT 23.0 → 16.4°C; heat sink 9.5 → 4.2°C); if receiving copper is small (pad-size), vias matter (59.6 → 47.5°C with 5 vias). Vias never cool a trace via a parallel plane (dielectric coupling dominates).
- source rows: BROOKS-091, -092, -093

**CHECK-SENSITIVITY-BUDGET** — uncertainty band on a computed rise (base ≈40°C rise; scale linearly with ΔT/40; `conf=medium`)
- inputs: dT_nom, rho_tol_pct, Th_tol_mil, k_known (bool), HTC_known (bool)
- formula: `dT_unc = (dT_nom/40) * (1.0 * rho_tol_pct/2 + 3.0 * Th_tol_mil/0.1 + (5.0 if not HTC_known else 0) + (5.6 if not k_known else 0))`
- pass: `dT_nom + dT_unc <= dT_limit`
- source rows: BROOKS-074, -065

**CHECK-RESISTIVITY-SANITY** — validate a measured/derived copper resistivity
- inputs: rho_meas (μΩ·cm at 20°C)
- pass: `1.6 <= rho_meas <= 1.9` (expected 1.62–1.66 ED foil, 1.68–1.72 pure/annealed/plated, 1.74–1.79 rolled foil; alloys to 1.86); `< 1.6` impossible; `> 1.9` suspect measurement (thickness/length/contact error)
- source rows: BROOKS-012, -015, -022, -131, -136

**CHECK-SIM-SETTINGS** — minimum settings for Anvil's own Joule-heating solver run
- resistivity iteration loops ≥ 3 (T ≤ 50°C) / ≥ 4 (T ≤ 100°C) or per-step update (Δt ≤ 0.1 s) for transients
- cell size < smallest x-y feature (via wall ≈ 0.02 mm for via models; 0.2 mm for traces)
- HTC = 11 W/m²·K still air (10–14 band; use 6 for vacuum); ambient 20°C reference
- dielectric k entered as in-plane AND through-plane (FR4 default 0.6 / 0.4; measured 0.68 / 0.51; polyimide 0.53–0.58); copper k = 385–386
- ρ_Cu = 1.68–1.75e-8 Ω·m; α = 0.0039–0.0040 /°C; cp = 385 J/kg·K; density 8900 kg/m³
- correlation anchors: IPC replica 16 A/200 mil/2 oz → 65.5°C (ext, HTC 11, k 0.53); Ch.7 100 mil/1.9 mil/9.35 A → 69.2°C (k 0.68/0.51); Ch.10 40 mil/1 oz/4 A → 53.2°C (polyimide)
- source rows: BROOKS-051 … -054, -067, -071, -139
<!-- CHECKS-APPEND -->

## 4. Verification procedures & plots
| # | Property | Plot / procedure | Axes, sweep, corners | What "good" looks like / pass | Setup notes | Source |
|---|---|---|---|---|---|---|
| V1 | Trace ΔT vs current | Plot ΔT (y) vs I (x), one curve per width, fixed Th; overlay external (eq. 5.5), internal (Table 5.1), vacuum | I 0–max; widths 5–500 mil; Th 0.5–3 oz; corners: W−1 mil, Th_min, ρ_max | Design point below ΔT_limit line with margin; curves get very steep below 10 mil; vacuum > external > internal | Same axes as Fig. 5.3 / 7.1; mark tolerance-shifted curve (Fig. 7.2) | §5.4, §7.2.1 |
| V2 | IPC-style chart | I (y) vs cross-section (x) on constant-ΔT lines (10, 20, 30, 45, 60, 75, 100°C) | area 10–1000 mil² | Straight constant-J lines must cross several ΔT curves (proves J is not the variable) | Fig. 5.2 / 14.1 | §5.4.1, §14.4 |
| V3 | Thermal transient | T (y) vs time (x) after current step | 0–15 min; include internal & external | Reaches 90% at ≈3.5 min, 95% at ≈5 min; fully stable by 6–15 min; internal slightly slower | Lab: dwell ≥ 6 min (book) before reading; log with 1-s thermocouple | §7.2.2, §4.8.1, §8.5 |
| V4 | Along-trace gradient | T (y) vs position (x) along trace | full length incl. pads; widths 27/100/200 mil | Hottest near center (may be off-center), sharp drop within ≈1 in of pads; measured ≈ simulated | Multiple thermocouple points or IR line profile | §7.2.3, Fig. 7.5–7.6 |
| V5 | Via vs trace temperature | T_trace and T_via_mid (y) vs I (x), one pair per trace width | I to ΔT ≈ 100°C; A_trace/A_via 0.6–8 | T_via ≤ T_trace when A_trace ≤ ≈1.5–2 A_via; T_via − T_trace ≤ +10°C at +30°C rise, ≤ +25°C at +75°C for ratio ≈ 8 | Fig. 8.3 / 8.4; measured Table 8.8 | §8.3–8.5 |
| V6 | Via current sharing | Current per via (bar) for n parallel vias, straight vs turned traces | n = 2–4; 0°/90° exit | Equal split (±2% numerical) straight; ≤ +14%/−28% for 90° turn | Fig. 9.5–9.8 | §9.4–9.5 |
| V7 | Fusing time vs current | log t (y) vs I (x): Onderdonk line, trace model, measured points | t 0.1–10 s; A 26–520 mil² | Trace curve to the right of Onderdonk; ratio grows with t (Table 12.1) | Fig. 12.5; also t·(I/A)² vs t (Fig. 12.7) flat ≈0.0346 for fuse, rising for trace | §12.5 |
| V8 | Marginal overload / runaway | T (y) vs t (x) at 0.97–1.0× runaway current | minutes–hours; log every 1 s | Plateau then accelerating rise from ≈220–270°C (≈250°C); nominally identical traces differ ±1% in threshold | IR camera (thermocouples limited to 300–350°C); destructive — scrap board after | §4.8.3, §12.8.2–12.8.3 |
| V9 | Duty-cycle / RMS linearity | T (y) vs duty cycle (x) at fixed peak; T vs log f | D 0–100%; f 0.05 Hz–10 kHz; sine/triangle/square | T linear in D; T flat vs f above ≈10 Hz; all waveforms fall on the DC I_rms–T curve | Two identical traces alternately switched to keep the constant-current source loaded; true-RMS current from sampled data | §15.2–15.4 |
| V10 | Plane / copper credit | ΔT (y) vs configuration (bar): bare, opposite plane, plane 10 mil, two planes, adjacent trace, split, stubs | per Tables 7.3/7.4/10.1 | Factors ≈0.75 / 0.60 / 0.40; split = 1.0; neighbor ≈0.8× driven | Thermal image halo widens with planes (Fig. 7.7, 7.15) | §7.2.6–7.2.10, §10.4–10.5 |
| V11 | Material sensitivity tornado | ΔT change (x) for ρ +2%, Th −0.1 mil, HTC 11→14, k 0.5→0.7 | at ≈40°C rise; scale with ΔT | 1.0 / 3.0 / 5.0 / 5.6°C; thickness dominates | Table 7.7, Fig. 7.17–7.20 | §7.3 |
| V12 | Board-thickness / depth | ΔT (y) vs board thickness (x); ΔTi/ΔTe (y) vs depth fraction (x) | 20–240 mil; depth 0–0.5 | ΔT falls steeply then saturates (>63 mil); Fraction = 1.41√Depth reaching 1.0 at 0.5 | Fig. 7.12, 7.22 | §7.3.1, §7.4 |
| V13 | Thermal-via benefit | Pad ΔT (y) vs number of thermal vias (x), one curve per receiving copper (small plane / large plane / heat sink) | 0, 1, 5 vias | Large drop from plane/heat sink alone; vias add little unless receiving copper is small | Fig. 8.10, Table 8.9 | §8.7 |
| V14 | Hot-spot map | IR image with narrow scale (e.g. 150–166°C or 40–50°C span) | full trace | Non-uniform patches; centerline hotter than edges; corner inside ≤ +1.5°C vs outside | Fluke Ti32 / FLIR SC640 class; emissivity known | §13.3–13.4 |
| V15 | Resistance-method temperature (IPC-TM-650 2.5.4.1a) | ΔT = (Rt/Rt0 − 1)/α0 vs I | I steps to ΔT 100°C; Rt0 at ≤100 mA | Gives average ΔT; compare with IR peak (peak > average) | 12-in coupon, 6-in sensed length, still air, horizontal; 4-wire sense on the trace | §4.7.1, §5.3 |
| V16 | Dimension verification | Microsection thickness at ≥ 6 points across width and several points along length | — | Plated Th within 0.8–1.2× nominal; edge-to-edge ≤ 10% | ±0.1–0.3 mil; destructive; CT scan only qualitative | §13.3.3, App. B.5, Ch.16 |
| V17 | Resistivity extraction | 4-wire R at large I (≈2 A, no heating), correct to 20°C via α, compute ρ = R·A/L with measured A | — | 1.6 ≤ ρ ≤ 1.9 μΩ·cm; plating ≈ 1.70 | Kelvin contacts on the trace (Fig. B.2); big traces (200 mil × 5 in) | App. B |
| V18 | Laminate thermal conductivity | MTPS (C-Therm) through-plane and in-plane | 1.5-in sample; edge-stacked for in-plane | 0.3–0.8 W/m·K; in-plane > through-plane (e.g. 0.68 / 0.51) | Needed before any solver correlation | App. A |
<!-- VERIFY-APPEND -->

## 5. Pitfalls, failure modes, review checklist
- Sizing traces or vias by current density (A/mm², A/mil²) — no unique relation to temperature; use current + W + Th (§4.6, Ch.14).
- Derating internal traces by 50% (old IPC-2221 practice) — internal traces run cooler; the derating is backwards (§1.2, §5.4.3).
- Using IPC-2221 external curves — IPC-2152 allows ≈25% less current for the same ΔT (§1.2).
- Using nominal copper thickness for outer (plated) layers — actual varies 20–50% (one test trace was 2.7 mil vs 1.9 nominal, 40%); use minimum plating (§2.3.2, §7.2.5, App. B).
- Ignoring etch tolerance on narrow (≤10 mil) high-current traces — 5→4 mil or 10→9 mil changes ΔT noticeably (§7.2.1).
- Assuming a half-oz trace is 0.65 mil and a 1-oz is 1.3 mil everywhere — conventions range 0.60–0.65 and 1.2–1.38 mil; state which is used (§1.3).
- Treating "1-oz external" IPC-2152 charts as measured — they don't exist; the 1-oz external curve is eq.(5.5) extrapolated (§5.4.2).
- Assuming a via with the same cross-section as the trace runs at the trace temperature — it runs cooler (≈6–13°C at 87–167°C) (§8.3.3).
- Adding vias in parallel "to match cross-section" when the trace is already sized — unnecessary; one standard via is thermally adequate (§8.3.6, §8.5.2).
- Routing a via carrying high current without a properly sized trace/plane attached — the trace is the via's heat sink; alone it melts in seconds (§8.3.4, §14.9).
- Expecting thermal vias to cool a trace — vias don't cool traces; parallel copper through the dielectric does (§10.4.1, §8.7).
- Adding thermal vias under a pad that already has a large plane/heat sink — marginal benefit; only small receiving copper benefits (§8.7).
- Splitting a power trace into two parallel or stacked half-width traces for thermal reasons — same peak temperature, wider hot zone (§7.2.9–7.2.10).
- Forgetting the neighbor: a passive trace 8 mil from a 65°C trace reaches ≈55°C; planes spread the halo wider (§7.2.7, §7.2.6).
- Using datasheet thermal conductivity without direction — in-plane matters most; a single unlabeled value is often through-plane (§7.3.4, App. A).
- Applying Onderdonk beyond ≈1 s on a PCB (or ≈10 s for wires) — cooling makes real times 1.5–6× longer; conversely, never use it to claim a trace will NOT fuse in slow overload (§11.4.1, §12.5.4).
- Using a mis-printed Onderdonk formula (Codreanu et al. copy contains a misprint) — use eq.(12.2)/(G.22) with 33.5 and (234 + Tref) (§11 end note 7).
- Confusing "time to melting temperature" with "time to open" — heat of fusion and liquid-path separation add unpredictable time (§11.4.1).
- Repairing a fused trace and returning the board to service — destructive event; scrap (§12.5.4, Preface).
- Relying on supplemental cooling (fan/heat sink) for a trace without a failure analysis — loss of cooling leads to slow runaway from ≈220–270°C (§4.8.3, §12.9).
- Using thermocouples above ≈300–350°C — probe coatings fail; use IR (§4.7.3).
- Measuring ΔT with the IPC resistance method and calling it the peak — it is the average; hot spots and centerline are hotter (§4.7.4, §13.3).
- Measuring trace resistance with an ohmmeter or with voltage sensed on the current leads — contact/lead resistance and tiny currents (50–200 mA) corrupt it; use Kelvin sensing on the trace at large current (App. B.2–B.3).
- Trusting any copper resistivity below 1.6 μΩ·cm or plated-copper values well above 1.7 — measurement error (App. B.1).
- Taking readings before stabilization — needs 6–15 min (3.5 min to 90%) (§4.8.1, §7.2.2).
- Using a single-value HTC across the temperature range — HTC rises with temperature (10 → 14); results insensitive at low ΔT, ±10–20°C at high ΔT (§6.3).
- Running a thermal solver without iterating resistivity with temperature — under-predicts (§6.3).
- Modeling a via with cells larger than the plating wall — geometry lost (§8.3, §6.4).
- Assuming pulse currents heat by peak value — use RMS (I_pk·√D); above ≈10 Hz frequency is irrelevant (Ch.15).
- Believing right-angle corners create thermal hot spots — inside/outside difference ≤ 1.5°C and corner is not hotter than the body (§13.4).
- Forgetting that ΔT sensitivity to every parameter grows with ΔT — check worst case at maximum current, not at nominal (§7.2.12).
- Assuming an opposite-side plane helps fusing time — it doesn't; only a plane ≤ 12 mil below the trace does (+30–100%) (§12.5.2).
- Relying on CT/X-ray to measure trace thickness — resolution is qualitative today; microsection for numbers (Ch.16).
- Assuming plated-through vias have uniform wall thickness — often non-uniform; use minimum (§8.2).
- Ignoring Tg/Td/T260 when a trace can exceed ≈100°C — laminate property changes alter cooling; delamination → runaway (§2.4, §12.6.2).
<!-- PITFALLS-APPEND -->

## 6. Standards referenced
| Standard / source | Edition, year | Clause / table / figure | Governs | Book page |
|---|---|---|---|---|
| IPC-2152, Standard for Determining Current Carrying Capacity in Printed Board Design | August 2009 | Section 5 (consolidated charts); Appendix A.7 p.85; Fig. A-89 p.86 (NBS chart); Fig. A-26 p.42 (2-oz external); p.26 via cross-section guidance | Trace current/temperature data (external, internal, vacuum; 0.5–3 oz), via sizing guidance | p.2, 6, 41, 90, 166 |
| IPC-2221 / IPC-2221A, Generic Standard on Printed Board Design | 1998 / May 2003 | Fig. 6-4, p.41 | Legacy current-carrying charts (external; internal = ½) | p.2, 6 |
| ANSI/IPC-D-275, Design Standard for Rigid Printed Boards | September 1991 | Fig. 3-4, p.10 | Legacy current charts | p.2, 6 |
| MIL-STD-275E, Printed Wiring for Electronic Equipment | 1984 | — | Legacy current charts | p.2, 6 |
| MIL-STD-1495, Multilayer Printed Wiring Boards | 1973 | — | First publication of NBS charts | p.2, 6 |
| NBS Report 4283, Characterization of Metal-Insulator Laminates | 1956 | p.26 chart ("Tentative") | Origin of trace current/temperature charts | p.1–3, 6 |
| IPC-TM-650 Test Method 2.5.4.1a, Conductor Temperature Rise Due to Current Changes in Conductors | — | 12-in coupon, 6-in sensed, ≤100 mA reference | Change-of-resistance ΔT measurement | p.33, 39, 41–43, 50 |
| IPC-TM-650 Test Method 2.4.24, Glass Transition Temperature and Z-Axis Thermal Expansion by TMA | — | — | Tg | p.13, 15 |
| IPC-TM-650 Test Method 2.4.24.1, Time to Delamination (TMA Method) | — | 10°C/min to 260/288°C | T260 / T288 | p.14, 15 |
| UNS (Unified Numbering System for Metals and Alloys) | — | C10100–C15999 coppers (≥99.3%); C16000–C19999 high-copper alloys (>96%) | Copper alloy resistivity range 1.69–1.86 μΩ·cm | p.12 |
| Matula, R. A., "Electrical Resistivity of Copper, Gold, Palladium, and Silver," J. Phys. Chem. Ref. Data 8(4) | 1979 | Table 2, p.1161 | ρ(T) for copper to liquid state | p.22–23, 26 |
| Chapman, D., High Conductivity Copper for Electrical Engineering, CDA Pub. 122 / ECI Cu0232 | 1998 | Fig. 1, p.6 | Impurity effect on resistivity (≈25%) | p.12, 15 |
| Rogers Corp., "Copper Foils for High Frequency Materials" | 2015 | — | ED vs rolled foil resistivity | p.10, 15 |
| Preece, W. H., Proc. Royal Society 36 (1883) 464–471; 43 (1887) 280–295; 44 (1888) 109–111 | 1883–1888 | 1888 paper: a = 10244 for copper | Preece fusing equation | p.126, 130 |
| Stauffacher, E. R., "Short-Time Current Carrying Capacity of Copper Wire," GE Review 31(6) | June 1928 | Fig. 1 chart; footnote attributing formula to Onderdonk | Earliest Onderdonk reference | p.129, 131 |
| Anon., "Short-Time Current Required to Melt Copper Conductors," Electrical World 121(26) p.98 | June 24, 1944 | nomograph | Onderdonk nomograph | p.128, 130 |
| Fink & Beaty, Standard Handbook for Electrical Engineers, 14th ed., McGraw-Hill | 1999 | p.4-74 | Onderdonk equation | p.130 |
| Babrauskas, V., and I. Wichman, "Fusing of Wires by Electrical Current," Fire and Materials Conf. | 2011 | eq. 6, 7, 8 | Independent fusing derivation (eq. 6 ≈ 4% below Onderdonk) | p.131, 243–244, 251 |
| Codreanu, N., R. Bunea, P. Svasta, "New Methods of Testing PCB Traces Capacity and Fusing," UPB-CETTI | Winter 2010 | Fig. 6 | Long-term trace failure curve; NOTE: contains a misprinted Onderdonk formula | p.39, 131 |
| Adam, J., TRM White Paper No. 10, "Adiabatic Wire" (adam-research.de) | — | — | Onderdonk derivation | p.251 |
| Brooks, D. G., "90 Degree Corners: The Final Turn," Printed Circuit Design Magazine | Jan 1998 | — | Corner impedance/EMI non-issue | p.158, 164 |
| Brooks, D., PCB Currents; How They Flow, How They React, Prentice Hall | 2013 | Ch.1, 4; p.216 (critical length) | Current fundamentals | p.26, 164 |
| Brooks, D., "Temperature Rise in PCB Traces," PCB Design Conference West | March 1998 | — | 40% discrepancy IPC vs 1968 Design News data | p.2, 6 |
<!-- STANDARDS-APPEND -->

## 7. Process / lifecycle guidance
(The book is a design/analysis text, not a product-development text; only the trace-sizing workflow and the measurement/validation sequence are process guidance.)

| Stage | Activity | Deliverable | Exit criterion | Source |
|---|---|---|---|---|
| Requirements | Circuit designer states maximum current and duty cycle per power trace | Current table (I_max, I_rms, overload I/t) | Every high-current net has I_max and duty; overload survival cases (e.g. 40 A for 1 s) listed | Preface p.xv |
| Requirements | System engineer sets allowable trace temperature rise as a policy (market/reliability/regulatory driven) | ΔT_limit (typ. 20–40°C) and absolute T limit | ΔT_limit documented before layout starts | Preface p.xiii–xv; §8.3.4 |
| Design (first pass) | Size traces from IPC-2152 / eq.(5.5) / Table 5.1 (worst case) | W per net, layer assignment | CHECK-TRACE-DT-* pass with worst-case dimensions | Preface p.xvi; Ch.5 |
| Design | Compute R and V-drop at operating temperature; keep, enlarge, or shrink | R, V-drop, P per net | V-drop within PDN budget | Preface p.xvi; §8.6 |
| Design (optimization) | Shrink traces only with thermal simulation credit for planes, adjacent copper, stubs, short length; verify neighbors | Solver report with correlation anchors | ΔT_sim ≤ ΔT_limit at max current with ±tolerance inputs; neighbor temperatures acceptable | Ch.7, Ch.10, §7.5 |
| Design | Vias: one standard via per transition when trace is sized; check via ΔT envelope; legacy area-matching only as fallback | Via table | CHECK-VIA-TEMP-VS-TRACE pass | Ch.8, §14.9 |
| Design | Overload / fusing cases: Onderdonk lower bound, Table 12.1 ratio, t(I/A)² < 0.15; plane ≤ 12 mil below if needed | Overload analysis | Survival time ≥ required with factor ≥ 1.5 | Ch.11–12 |
| Fab data | Obtain laminate k (in-plane and through-plane), Tg, Td, T260/T288; copper type (ED/rolled) and minimum plating spec | Material sheet | k both directions known or measured (MTPS); plating minimum specified | §2.4, §7.3.4, App. A |
| Validation | Build IPC-TM-650 2.5.4.1a coupons or test traces on the production stackup; measure ΔT (resistance method + IR/thermocouple), dwell ≥ 6 min | Test report | Measured ≤ simulated + uncertainty; hot spots inspected by IR | §4.7, §5.3, §8.5 |
| Validation | Microsection coupons: thickness at several points; back out ρ if needed | Dimension report | Th_min ≥ assumed; ρ within 1.6–1.9 μΩ·cm | §3.5, App. B, Ch.16 |
| Sustaining | Any board with a fused or ≥ fusing-range trace event is scrapped; supplemental-cooling failure modes reviewed | Disposition | No repaired fused traces in service | Preface p.xv; §12.5.4 |

## 8. Coverage log

- File: Douglas_Brooks_Johannes_Adam_PCB_Design_Guide_to_Via_and_Tra.txt, 6154 lines / 376,685 bytes. Read sequentially in 15 chunks: 1–917, 918–1116, 1117–1391, 1392–1754, 1755–2036, 2037–2401, 2402–3009, 3010–3395, 3396–3730, 3731–4038, 4039–4424, 4425–4862, 4863–5306, 5307–6125, 6126–6154. All lines read.
- Chapters read: Preface, Technical Note, Ch.1–16, Appendices A–I, About the Authors. Index (≈lines 5900–6154) scanned only (no engineering content).
- Skipped/not transcribed: Appendix C (figures only, fitted curves — coefficients taken from Table 5.1/App. D); Appendix E (charts only — model parameters transcribed); Appendix F figures (numeric current-density anchors taken from Ch.9 text/Table 9.1); Appendix G intermediate calculus steps (results and constants transcribed); Appendix H/I (figures only); figure-based content in Ch.4 (Fig. 4.4 plume widths quoted from prose), Ch.7 (Fig. 7.1–7.3, 7.12, 7.17–7.22 — numeric anchors quoted from prose), Ch.8 (Fig. 8.3, 8.10 — tables transcribed instead), Ch.12 (Fig. 12.3–12.9 — Table 12.1 and prose anchors used), Ch.13 (thermal images), Ch.15 (Fig. 15.1–15.10 — tables used), Ch.16 (photographs).
- Extraction limitations: OCR renders μ as "m" in "mohm-cm" (interpreted as μΩ·cm throughout) and lost the exponent in eq.(7.5) — recovered as Depth^0.5 from the worked example (7.8) and verified numerically. Onderdonk constant printed as 33 in eq.(11.3)/(12.1) and 33.5 in eq.(12.2)/(G.18)–(G.24); all numeric results (0.0346, Table G.3) correspond to 33.5. Table 14.2 prints A_via = 0.02675 mm² where geometry gives 0.0276 (flagged). Two thicknesses used for "1 oz" in different chapters (1.3 mil / 33–35 μm / 1.35 mil / 38 μm) — each rule states the value used. The IPC-2152 width/current range of validity for the fits is not stated explicitly in the book (only 0.5–3 oz and App. D width conditions 20–500 mil); marked medium where inferred.
- Numeric verification: eq.(5.5) reproduces Table 14.1 to < 0.3°C; eq.(7.2)/(7.5) reproduce the §7.4 worked example; App. G constants reproduce Table G.3 for all four reference temperatures; §12.5.3 example (103 mil², 19 A, ×2.14) reproduced; Preece forms consistent; via area 0.0217 mm² reproduced; §8.6 R20 = 0.0897 Ω reproduced with 1 oz = 33 μm.
- Rule count: BROOKS-001 … BROOKS-143 (143 rows); 24 mechanizable checks; 18 verification procedures.
