# Printed Circuits Handbook (7th ed.) — Anvil rulebook, part 4 (Ch. 55§55.8 – end)

## 0. Citation

C. F. Coombs, Jr. and H. T. Holden (eds.), *Printed Circuits Handbook*, 7th ed. New York: McGraw-Hill Education, 2016. ISBN 978-0-07-183395-0 (print), 978-0-071-83396-7 (eBook).

Chapters covered by THIS extraction (text lines 12150–16154): Ch. 55 (from §55.8, 3-D solder paste inspection, onward), 56 (Design for Testing), 57 (Loaded Board Testing), 58 (FMEA), 59 (CAF), 60 (Reliability of PCBs), 61 (Reliability of Microvia PCBs), 62 (Component-to-PWB reliability: design variables & lead-free), 63 (Lead-free solder joint reliability rules), 64 (Estimating solder joint reliability), 65–71 (Flexible circuits: applications/materials, design, manufacturing, terminations, multilayer/rigid-flex, special constructions, QA), plus the Appendix (Summary of Key Component, Material, Process, and Design Standards, M. Carter) and the Glossary; the Index was scanned and skipped.
Chapters NOT read: 1–54 and the first part of 55 (§55.1–55.7) — assigned to other agents (parts 1–3).

Page numbers: the eBook extraction carries no printed page numbers; citations are by §chapter.section, figure and table numbers. Tables and figures are images in the source and are absent from the text; where a value came only from prose around a table, it is marked.

## 1. Design rules

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| COOMBS-4001 | test | 3-D solder-paste inspection (SPI) images one "view" at a time; plan inspection time from view count. | view 10–25 mm diameter; >100 views per typical assembly | board area | SPI systems | calc | §55.8.1.1 | high |
| COOMBS-4002 | test | SPI throughput budget for line balancing. | 2–22 cm²/s | board area, line takt | 3-D SPI | calc | §55.8.1.2 | high |
| COOMBS-4003 | test | Pre-reflow 2-D AOI throughput budget (2–3× faster than 3-D SPI). | 10–40 cm²/s | board area | pre-reflow AOI (placement/2-D paste) | calc | §55.9.1 | high |
| COOMBS-4004 | test | Post-reflow AOI throughput budget. | 10–40 cm²/s | board area | post-reflow optical AOI | calc | §55.10.1.1 | high |
| COOMBS-4005 | test | Post-reflow AOI cannot inspect hidden joints; if the BOM has BGA/PGA/(some) J-lead parts, or fine-pitch ≤0.5 mm / SOT parts, AOI alone is insufficient — plan x-ray or electrical coverage. | pitch ≤ 0.5 mm → high false accept/reject on AOI | package types, pitch | post-reflow AOI | review | §55.10.1.2 | high |
| COOMBS-4006 | test | Transmission x-ray fillet acceptance example: heel-fillet grayscale ≥ 2× joint center; toe-fillet ≥ 1.5× center. | heel/center ≥ 2.0; toe/center ≥ 1.5 (grayscale ratio) | x-ray grayscale readings | example decision rule for gull-wing joints | inspect | §55.10.2.1 | high |
| COOMBS-4007 | test | Transmission (2-D) x-ray is valid only for single-sided SMT assemblies; it cannot resolve double-sided overlapping joints, PTH barrels, or BGA ball bottoms. | — | assembly sides, package types | AXI selection | review | §55.10.2.2 | high |
| COOMBS-4008 | test | Cross-sectional (laminographic) x-ray resolves a focal slice ≈0.2–0.4 mm thick; use it for double-sided, PTH and BGA joints and for insufficient-solder detection on BGA/PTH. | slice thickness 0.2–0.4 mm | — | AXI selection | review | §55.10.3 | high |
| COOMBS-4009 | test | AXI throughput and cost budget. | 50–150 joints/s; price ≈ 1.5–2.0× fastest optical system | joint count | x-ray solder joint inspection | calc | §55.10.4 | high |
| COOMBS-4010 | process | Plan dedicated technical support for the first 6 months after installing an automated inspection system; start with SPC measurements, not defect thresholds. | 6 months | — | AOI/AXI/SPI deployment | review | §55.11 | high |
| COOMBS-4011 | dfm | Keep parallel board/panel edges clear for conveyor clamps/belts. | edge clearance ≥ 3 mm (typical) | board outline, component keep-out | automated board handling (inspection) | inspect | §55.12.1 | high |
| COOMBS-4012 | dfm | Place alignment fiducials (or usable solder joints post-reflow) at three corners of the assembly or panel. | 3 corner fiducials | — | automated inspection | inspect | §55.12.1 | high |
| COOMBS-4013 | dfm | Provide a bar-code (assembly number + serial) at a predefined location on every PCA. | — | — | automated inspection / traceability | inspect | §55.12.1 | high |
| COOMBS-4014 | dfm | Boards thinner than 30 mil or panels with pre-routed breakaways need fixturing review — they may vibrate excessively on conveyors. | thickness < 30 mil (0.76 mm) flags | board thickness, panelization | automated inspection | review | §55.12.1 | high |
| COOMBS-4015 | dfm | Component/heat-sink/daughter-board height above and below the board must not exceed the inspection system's height clearance. | h_max ≤ clearance of targeted system | max component heights top/bottom | automated inspection | calc | §55.12.1 | high |
| COOMBS-4016 | dfm | Minimize approved suppliers per component type (ideally one) — package/lead dimension variation lengthens AOI program development. | 1 supplier per component type (ideal) | AVL | inspection programming | review | §55.12.2 | high |
| COOMBS-4017 | dfm | Pad shapes and sizes must be uniform within each component package type. | — | footprint library | inspection programming | inspect | §55.12.2 | high |
| COOMBS-4018 | dfm | For transmission x-ray: do not place components opposite or under dense structures (transformers, large capacitors, thick steel heat sinks). | — | placement, opposite-side parts | 2-D AXI | inspect | §55.12.2 | high |
| COOMBS-4019 | dfm | No silkscreen outlines around components — they confuse AOI. | — | silkscreen layer | AOI | inspect | §55.12.2 | high |
| COOMBS-4020 | test | Tie unused preset/clear (and similar control) pins to the rail through a resistor, never directly, so a tester can overdrive them. | 100 Ω series resistor | unused control pins | ad-hoc DFT | inspect | §56.3 | high |
| COOMBS-4021 | test | Decide bed-of-nails access early; use test pads and vias as probe targets; when full nodal access is impossible, prioritize access by circuit needs. | — | net list, via list | ICT DFT | review | §56.3.1 | high |
| COOMBS-4022 | test | IEEE 1149.1 TAP: four mandatory pins (TCK, TMS, TDI, TDO); TRST* optional and active-low; if TRST* exists give it a board-level pull-down; TAP can also be reset by 5 TCK pulses with TMS high. | 4 mandatory pins; reset = 5 TCK @ TMS=1 | JTAG parts | boundary-scan designs | inspect | §56.5.1, fn. f | high |
| COOMBS-4023 | test | Chain boundary-scan devices TDO→TDI; every device has a 1-bit BYPASS register; IDCODE register optional. | — | JTAG parts | boundary-scan chain | inspect | §56.5.1 | high |
| COOMBS-4024 | test | A spare DFT control input must be held at logic 0 in normal operation (pull-down to ground); tester asserts 1 during test. | pull-down resistor | spare control inputs | ad-hoc DFT | inspect | §56.3.2, fn. c | high |
| COOMBS-4025 | test | IEEE 1149.4 mixed-signal test bus adds two analog test pins (AT1, AT2) to the 1149.1 set; analog pins get an analog boundary module (ABM). | +2 pins | mixed-signal ICs | 1149.4 designs | inspect | §56.5.2 | high |
| COOMBS-4026 | test | 1149.4 impedance measurement: force known current via AT1/AB1 through Z, measure voltage at each terminal via AT2/AB2; Z = (V1 − V2)/I — valid despite non-linear silicon switches because voltmeter path draws ~0 current. | Z = (V_pin1 − V_pin2) / I_forced | I, V | in-situ analog component test | measure | §56.5.2, Fig. 56.10 | high |
| COOMBS-4027 | test | System-level first-pass probability is the product of board post-test yields; set the board yield target from system board count. | P_sys = Y_board^N; e.g. 0.97^20 = 0.54 | N boards, Y_board | multi-board systems; target Y ≥ 0.99 | calc | §57.2, fn. c, d | high |
| COOMBS-4028 | test | Test yield ≠ defect coverage: example pre-test yield 50% → post-test yield 97% with a test covering 90% of important defects. | — | pre-test yield, coverage | yield accounting | calc | §57.2, fn. b | high |
| COOMBS-4029 | test | IC-level yield benchmark: 250 ppm defective = 99.975% yield; 1 ppm = 99.9999%. | 250 ppm | — | — | calc | §57.2, fn. d | high |
| COOMBS-4030 | test | ICT probe target size: common probe target ≈ 35 mil; standard probe centers 100, 75, 50 mil. | target ≥ 35 mil (0.89 mm) typical; probe pitches 100/75/50 mil | test pad size/pitch | bed-of-nails ICT | inspect | Fig. 57.1 caption | medium (from figure caption) |
| COOMBS-4031 | components | Chip passive body sizes: 0402 = 40 × 20 mil; 0201 = 20 × 10 mil. | 0402: 1.0 × 0.5 mm; 0201: 0.5 × 0.25 mm | — | — | — | Fig. 57.1 caption | high |
| COOMBS-4032 | test | Manufacturing-defect testers (ICT/MDA) need < 10% of the programming time of functional testers; prefer them for defect detection. | < 10% of functional-test dev time | — | test strategy | review | §57.4.2 | high |
| COOMBS-4033 | test | Unpowered analog ICT shorts/component tests use a stimulus small enough not to forward-bias any junction. | stimulus < 0.2 V (typical) | — | analog ICT | measure | §57.5.1, fn. j | high |
| COOMBS-4034 | test | Shorts test: run first, exit to repair before power-up; locate shorted partner by half-splitting (O(log2 N)) not linear search. | — | node count N | ICT flow | review | §57.5.1, §57.5.4, fn. k | high |
| COOMBS-4035 | test | Use guarding (3-wire) to isolate parallel paths in analog ICT; add sense wires where component value ratios are extreme. | 3-wire (+sense for extreme ratios) | net topology | analog ICT | review | §57.5.1 | high |
| COOMBS-4036 | test | Digital ICT backdriving can damage upstream drivers within milliseconds — limit backdrive duration and insert cooling intervals; condition (disable) upstream drivers when possible. | damage onset: ms scale | test vector duration | digital ICT | review | §57.5.2, fn. m | high |
| COOMBS-4037 | test | Capacitive lead-frame opens test: nominal lead-to-plate capacitance ~100 fF; an open joint drops the measured value by 2–10×. | C1 ≈ 100 fF; open → C/2 … C/10 | — | ICs with lead frames, connectors, switches | measure | §57.6 | high |
| COOMBS-4038 | test | A missing/tombstoned bypass capacitor among many paralleled ones is NOT detectable by ICT (falls inside summed tolerance) — cover with AOI/AXI. | — | decoupling cap count | ICT coverage analysis | review | §57.6 | high |
| COOMBS-4039 | test | Fault-dictionary storage scales as faults × vectors × outputs — impractical for VLSI (example 100k gates → 2.5e13 bits ≈ 3.1 TB). | bits = N_faults × N_vectors × N_outputs | — | functional test planning | calc | §57.4.1, fn. g | high |
| COOMBS-4040 | process | FMEA: Risk Priority Number = frequency × criticality × detection rankings; rank modes by RPN and eliminate at least the top 50% of modes by RPN. | RPN = F × C × D; act on top 50% | rankings per Tables 58.1–58.3 (not in text) | design FMEA and process FMEA | review | §58.2.1.2 steps 8–12, §58.3.2 | high |
| COOMBS-4041 | process | FMEA must be complete before design freeze; start at investigation/launch and update as design changes. | — | — | product development | review | §58.3.3 | high |
| COOMBS-4042 | reliability | Electrochemical migration needs DC bias + surface moisture; driving field E = V/d rises as spacing shrinks — check conductor spacing against bias. | E = V / d (V/mm) | V, spacing d | biased conductors in humid service | calc | §59.2, Eq. 59.1 | high |
| COOMBS-4043 | reliability | Bono copper-corrosion test setup (original). | Cu trace 9–10 µm thick; anode–cathode 2 mm; V2 = 12 V via R2 = 50 kΩ; V1 = 250 V via R1 = 5 kΩ | — | flux-residue corrosivity test | measure | §59.3, Fig. 59.2 | high |
| COOMBS-4044 | reliability | Corrosion factor from trace resistance rise (R = ρL/A; corrosion reduces A). | CF(t) = 1 − R(0)/R(t) = fraction of trace cross-section lost (derived from the stated R = ρL/A; reported as %CF; equation body missing in text) | R(0), R(t) | Bono/Turbini/Zhou tests (anodic trace ≈ 5 Ω) | measure | §59.3 | medium |
| COOMBS-4045 | reliability | Turbini-modified corrosion coupon: anode–cathode 0.5 mm (matches IPC-B-24), 8.6 µm Cu, V1 lowered 250 → 50 V to avoid CAF confounding; resistors moved outside chamber. | 0.5 mm; 8.6 µm; 50 V | — | corrosion test | measure | §59.3 | high |
| COOMBS-4046 | reliability | Weak-organic-acid flux corrosion test: recommended stress 60°C/93% RH; 10 days sufficient (20 used); 85°C/85% RH is NOT discriminating (WOA evaporates, %CF < 0.2%); 40°C too cold. Equilibrate 24 h (85/85) or 40 h (60/93, 40/93) before first reading. | 60°C / 93% RH / 10 d | — | flux residue corrosion qualification | measure | §59.3, Table 59.2 (values in prose) | high |
| COOMBS-4047 | reliability | WOA corrosivity ranking (increasing): abietic < succinic < adipic ≈ glutaric < malic; doubling WOA concentration strongly increases %CF. | — | flux chemistry | flux selection | review | §59.3 | high |
| COOMBS-4048 | reliability | Bell Labs flex CAF vehicle: 0.005–0.007 in epoxy-glass, 0.008 in lines / 0.009 in spaces; tested 35–95°C, 25–95% RH, ≤400 VDC; at 85°C/80% RH/78 V failures in 2–5 days; through-substrate shorts only above 75°C and 85% RH. | see limits | — | historical CAF acceleration data | — | §59.4 | high |
| COOMBS-4049 | reliability | Multilayer "punch-thru" (CAF) appears only under DC bias (not AC, not unbiased); incidence falls with bias voltage; urethane conformal coat accelerated it. Test used 100 V, 65°C/95% RH, 10 days. | 100 VDC, 65°C/95% RH, 10 d | — | CAF screening | measure | §59.4 | high |
| COOMBS-4050 | reliability | CAF mean time to failure scales with spacing^4 / voltage^2 (hole-to-hole pattern, tested at 0.50 & 0.75 mm, 150 & 200 V). | MTTF ∝ L^4 / V^2 | spacing L, bias V | hole-to-hole CAF; use for relative scaling only | calc | §59.4, Eq. 59.14 | high |
| COOMBS-4051 | reliability | CAF filament chemistry/size: Cu2(OH)3Cl (atacamite), insoluble below pH 4, semiconducting; filaments ≤ 50 µm diameter, ≈ 0.2 mm long. | ≤ 50 µm dia; 0.2 mm length | — | failure analysis | inspect | §59.4.1 | high |
| COOMBS-4052 | materials | Laminate CAF susceptibility ranking (most → least): MC-2 > epoxy/Kevlar > FR-4 ≈ PI > G-10 > CEM-3 > CE > BT; BT most CAF-immune (low moisture uptake). | — | laminate type | CAF-critical designs | review | §59.5.1 | high |
| COOMBS-4053 | reliability | Conductor-configuration CAF susceptibility: hole-to-hole > hole-to-line > line-to-line; failure initiates in the most deeply buried layers; smaller spacing and glass fibers closer to Cu → faster growth. | — | geometry | CAF-critical designs | review | §59.5.1.1 | high |
| COOMBS-4054 | reliability | Lead-free (higher) soldering temperatures significantly increase CAF incidence; water-soluble flux polyglycols diffuse into epoxy above Tg — a hotter profile gave SIR one order of magnitude lower. | ΔSIR ≈ −1 decade for hotter profile | reflow profile, flux type | WS-flux + lead-free assembly | review | §59.5.2 | high |
| COOMBS-4055 | reliability | Field CAF example: inner-layer power plane (+20 V) to ground pin (−20 V) separated 0.005 in shorted via Cu-bromide CAF enhanced by flux residue. | 40 V across 0.127 mm | — | cautionary datum | — | §59.5.3, Fig. 59.15 | high |
| COOMBS-4056 | reliability | A relative-humidity threshold (voltage- and temperature-dependent) exists below which CAF does not form; but moisture absorbed in storage/transport counts, not just operating RH. | — | storage/transport RH | CAF risk assessment | review | §59.5.4 | high |
| COOMBS-4057 | reliability | Bromide CAF (Cu2(OH)3Br, insoluble below pH 7) forms with high-bromide flux (15 wt% Br); 2 wt% Cl or Br flux gave chloride CAF. Test: reflow 240–245°C ×1–2, 85°C/85% RH, +200 V bias, +100 V test, 28 days. | 15 wt% Br flux; 85/85, 200 V, 28 d | flux halide content | HASL/flux selection | measure | §59.5.6 | high |
| COOMBS-4058 | reliability | IPC-TM-650 2.6.25 CAF vehicle: hole-to-hole spacings 0.27, 0.38, 0.50, 0.65 mm, in-line vs staggered with glass; 65°C/85% RH, 500 h; staggered (diagonal) holes are more CAF-resistant than in-line. | 65°C / 85% RH / 500 h | — | CAF-resistant laminate qualification | measure | §59.6 | high |
| COOMBS-4059 | reliability | Minimum hole-wall to hole-wall spacing for CAF: 0.65 mm for telecom cycled 365×/yr; with high-Tg dicy FR-4 and a qualified supplier this gave ≥ 20 yr expected service life. | ≥ 0.65 mm wall-to-wall | drill dia, pitch | telecom-class reliability | calc | §59.7 | high |
| COOMBS-4060 | materials | Resin content vs construction: double-sided 1.5 mm board = 8 × 7628 (0.175 mm) → 30–40% resin; multilayer glass 0.035–0.10 mm/ply → 55–65% resin (0.035 mm) or 45–50% (0.10 mm); higher resin content → less drill damage at the glass/epoxy interface (lower CAF risk). | see values | stackup | CAF risk | review | §59.7 | high |
| COOMBS-4061 | reliability | Avoid a small anode facing a large cathode (high anodic current density accelerates corrosion/CAF); in CAF test boards make the plane the anode. | — | plane/pin polarity | biased plane-to-pin geometries | review | §59.7 | high |
| COOMBS-4062 | via | Laser microvias can be placed at tighter pitch than mechanical holes for CAF purposes (no drill damage, no drill wander). | — | via type | HDI | review | §59.7 | high |
| COOMBS-4063 | components | Package/via feature-size regimes: BGA 0.8–1.27 mm pitch for high-reliability; CSP 0.4 → 0.3 mm; conventional PTH ≥ 150 µm (6 mil) diameter; microvia ≤ 150 µm; direct die attach at ≤ 0.254 mm (10 mil) pitch requires microvia/SBU. | see values | pitch, via dia | technology selection | review | §60.2.1, §60.3.1 | high |
| COOMBS-4064 | reliability | Reliability bookkeeping: R(t) = 1 − F(t); in the constant-failure-rate region R(t) = exp(−r·t), r = 1/MTBF. | R = e^(−t/MTBF) | t, MTBF | steady-state region | calc | §60.2.3 | high |
| COOMBS-4065 | reliability | Use Weibull for solder-joint and PTH fatigue (β typically 2–4 for solder joints), log-normal for electrochemical failures; extrapolate to x% failures via the fitted distribution. | Weibull: t_x = η·(−ln(1 − x))^(1/β) (standard form; equation body missing in text) | η, β, x | wear-out extrapolation | calc | §60.2.3 | medium |
| COOMBS-4066 | reliability | Thermal-cycling PTH/solder failure rate scales roughly with (ΔT)^2; Arrhenius applies only when a thermally activated step (e.g. diffusion) is rate-controlling. | rate ∝ (ΔT)^2 | ΔT | thermal-cycle acceleration | calc | §60.2.5 step 4 | high |
| COOMBS-4067 | reliability | Do not accelerate thermal tests above laminate Tg unless service does so — z-CTE rises sharply and modulus falls, changing failure mode (may relieve solder strain but promote PTH failure). | T_test,max < Tg (or justify) | Tg | accelerated test design | review | §60.2.5 | high |
| COOMBS-4068 | reliability | Accelerated test design: 7 steps — service env → actual PCA env → failure modes → acceleration model per mode → test design & sampling → failure analysis confirms mode → transform life distribution. | — | — | any accelerated reliability test | review | §60.2.5 | high |
| COOMBS-4069 | reliability | Solder-float thermal stress (MIL-P-55110 / IPC-TM-650): bake 120–150°C, RMA flux, float on solder at 288°C for 10 s (SnPb) or ≥ 260°C (lead-free), then microsection PTHs for cracks. | 288°C/10 s; ≥ 260°C lead-free | — | bare-board qualification | measure | §60.2.6.1 | high |
| COOMBS-4070 | reliability | Cu/solder-mask adhesion: IPC-TM-650 2.4.28 peel test; quick tape test on scribed squares. | — | — | bare-board qualification | measure | §60.2.6.2 | high |
| COOMBS-4071 | reliability | SIR: surface resistivity (Ω/sq) = measured R × square count; square count = total parallel trace length / separation; readings > 1e12 Ω require careful shielding. | ρ_s = R × (L_total / d) | R, comb geometry | IPC-B-25 / Y coupon | measure | §60.2.6.3 | high |
| COOMBS-4072 | reliability | Moisture & insulation resistance (IPC-SM-840A, Class 2): 50°C, 90% RH, 100 VDC, 7 days; minimum IR 1e8 Ω. | IR_min = 1e8 Ω | — | commercial bare boards | measure | §60.2.6.3 | high |
| COOMBS-4073 | reliability | Military M&IR: MIL-P-55110 → MIL-STD-202 Method 106 with 100 VDC polarization, Method 402 condition A. | 100 VDC | — | military boards | measure | §60.2.6.3 | high |
| COOMBS-4074 | reliability | Electromigration resistance (IPC-SM-840A): 85°C/90% RH, 10 VDC, 1 mA current limit, 7 days; significant current change = fail; inspect for dendrites. | 85/90, 10 V, 1 mA, 7 d | — | solder-mask/laminate qualification | measure | §60.2.6.3 | high |
| COOMBS-4075 | reliability | Dendritic growth (flux residue) test: 85°C/85% RH, 1000 h, −20 VDC bias. | 85/85/1000 h/−20 V | — | flux/cleanliness qualification | measure | §60.2.6.3 | high |
| COOMBS-4076 | reliability | Thermal-shock oven (air-air) for PTH: −40 to +145°C, 25–35°C/min transitions, 20 s dwell at each extreme; measure cycles-to-failure. | −40/+145°C; 25–35°C/min; 20 s dwell | — | PCB PTH qualification | measure | §60.2.7.1 | high |
| COOMBS-4077 | reliability | IST (IPC-TM-650 2.6.26): DC-current-heated coupons; failure = 10% increase in PTH resistance. | ΔR ≥ +10% = fail | R0, R(n) | PTH/microvia qualification | measure | §60.2.7.2 | high |
| COOMBS-4078 | reliability | HATS: 4 daisy-chain nets per coupon, ≤ 36 coupons/chamber, air-to-air −55 to +160°C, ramps ≥ 25 up to 50°C/min. | −55/+160°C; 25–50°C/min | — | PTH qualification | measure | §60.2.7.3 | high |
| COOMBS-4079 | reliability | Microvia IST: cycle to 190°C (above Tg): a compromised microvia fails < 500 cycles without artifacts; 150°C gives MTTF ≫ 1000 cycles (not discriminating); > 190°C changes the failure mechanism. | T_max = 190°C; fail < 500 cycles | — | microvia qualification | measure | §60.2.7.4 | high |
| COOMBS-4080 | reliability | IST is more sensitive than microsection thermal shock (IPC-TM-650 2.6.8) for fine inner-layer separation; smaller-diameter vias are less prone to ILS than larger ones on the same panel. | — | via dia | ILS detection | review | §60.2.7.4 | high |
| COOMBS-4081 | reliability | PCQR2: HATS correlates reasonably with thermal-shock oven over the same 185°C span (−40/+145°C), 10% resistance-rise criterion. | ΔT = 185°C; +10% R | — | test-method equivalence | review | §60.2.7.4 | high |
| COOMBS-4082 | materials | FR-4 Tg range 125–170°C; polyimide Tg > 200°C with lower CTE and long PTV life for high-layer-count boards. | Tg 125–170°C (FR-4); > 200°C (PI) | — | laminate selection | review | §60.3 | high |
| COOMBS-4083 | via | Via diameter regimes: PTV to microvia 300–50 µm (12–2 mil); microvia ≤ 150 µm in one dielectric layer, aspect ratio ≈ 1:1 vs drilled through-vias > 10:1 — microvias are more reliable per via. | AR_microvia ≈ 1:1 | via dia, depth | HDI | calc | §60.3.1 | high |
| COOMBS-4084 | reliability | CAF is promoted by glass/resin delamination from thermal excursions above ≈ 260°C (FR-4) and thermal cycling; shorts fastest when a single fiber bundle links two pads. | > 260°C delamination threshold (FR-4) | assembly peak temp | FR-4 lead-free assembly | review | §60.3.2 | high |
| COOMBS-4085 | reliability | Pure-Sn whiskers: typically 50 µm long, 1–2 µm diameter; need neither field nor moisture. Check clearances of pure-Sn finishes against 50 µm. | L ≈ 50 µm; d = 1–2 µm | finish, spacing | pure-Sn plated parts | review | §60.3.2 | high |
| COOMBS-4086 | fab | Laminate voids larger than 76 µm (3 mil) are rejectable in most acceptability specs; smaller voids not considered detrimental. | void ≤ 76 µm | microsection | bare-board acceptance | inspect | §60.3.4.1 | high |
| COOMBS-4087 | materials | Inner-layer Cu foil ductility: ≥ 8% elongation required for 1-oz foil to avoid inner-layer foil cracks; verify with 180° bend test. | elongation ≥ 8% (1 oz) | foil spec | multilayer PCB | measure | §60.3.4.2 | high |
| COOMBS-4088 | fab | Etchback: positive (3-side contact) or negative etchback both give good results; zero/flush etchback puts the foil/plating bond line at the point of maximum stress (one source calls it most dangerous, another most reliable — conflicting). | — | etchback spec | PTH reliability | review | §60.3.4.3 | medium |
| COOMBS-4089 | via | Plating uniformity: tight process control needed for aspect ratio > 3:1; adequate coverage hard to obtain for AR > 5:1 by electroplating. | AR ≤ 3:1 routine; > 5:1 difficult | board thickness, hole dia | PTH design | calc | §60.3.4.4 | high |
| COOMBS-4090 | via | PTH barrel Cu thickness: specs range 12–25 µm; IPC average minimum 12 µm (0.5 mil) for Class 1, 25 µm (1.0 mil) for Class 2 and 3. | t_Cu ≥ 12 µm (Cl.1); ≥ 25 µm (Cl.2/3) | class | PTH spec | inspect | §60.3.4.4 | high |
| COOMBS-4091 | assembly | PTH rework with solder pot/fountain: preheat (≈ 100°C for FR-4); keep total removal + replacement contact time < 25 s to keep Cu dissolution negligible; limit and log rework count per site; NiAu finish essentially eliminates barrel Cu dissolution. | preheat ≈ 100°C; contact < 25 s | — | PGA/connector rework | review | §60.3.4.6 | high |
| COOMBS-4092 | materials | PTH strain is set by total z-axis expansion over the cycle; raising Tg (so more of the cycle is below Tg) helps far more than lowering the below-Tg CTE. | — | Tg, α1, α2, ΔT | laminate selection | calc | §60.3.5.1, Fig. 60.15 | high |
| COOMBS-4093 | materials | Overall CTE of a laminated composite (metal-core/CIC etc.). | CTE_overall = Σ(E_i·α_i·t_i) / Σ(E_i·t_i) | E, α, t per layer | constrained-core boards | calc | §60.3.5.1 | high |
| COOMBS-4094 | materials | Reinforcement CTE progression (decreasing): E-glass > S-glass > D-glass > quartz (≈ 1/10 of E-glass); aramid is negative-CTE in-plane but has higher z-CTE and moisture uptake. | quartz ≈ 0.1 × E-glass CTE | fiber type | low-CTE boards | review | §60.3.5.1 | high |
| COOMBS-4095 | materials | Measling onset ≈ 260°C for FR-4 (lower for more hygroscopic resins). | 260°C | — | lead-free assembly of FR-4 | review | §60.3.5.1 | high |
| COOMBS-4096 | solder | Tent vias with dry-film solder mask (LPI generally cannot tent); avoid excessively thick dry film over closely spaced traces (crevices trap flux); avoid solder mask over solder. | — | mask type, via tenting need | solder-mask selection (IPC-SM-840) | review | §60.3.5.2 | high |
| COOMBS-4097 | solder | Keep dissolved Au in SnPb joints below the embrittlement threshold (AuSn4/AuSn2). | Au ≤ 3–5 wt% of joint | Au thickness, pad area, joint volume | Au-finished pads/terminations, reflow | calc | §60.3.5.3 | high |
| COOMBS-4098 | reliability | HASL consumes one solder-shock life cycle of the PTHs before the board leaves the fabricator; count it in the thermal-excursion budget. | −1 cycle | — | HASL boards | calc | §60.3.5.3 | high |
| COOMBS-4099 | reliability | Ni barrier plating in PTH lowers Cu strain (higher modulus "rivet"), resists etch thinning, and dissolves far slower than Cu in molten solder → longer PTH life; electroless Ni gives more uniform barrel thickness for high-AR holes. | — | finish | high-AR / rework-heavy boards | review | §60.3.5.3 | high |
| COOMBS-4100 | reliability | Low-cycle PTH fatigue via Coffin-Manson; if no data, use εf ≈ 0.3 for electroplated Cu; increase life by lowering Δε. Model underestimates high-cycle life. | εf(Cu, ED) ≈ 0.3; N_f rises with (εf/Δε) (equation body missing in text) | Δε, εf | thermal-cycle PTH life | calc | §60.4.1 | medium |
| COOMBS-4101 | reliability | Linearized ED-Cu properties used by the IPC semi-empirical PTH model. | Su = 40,000 psi; Sy = 25,000 psi; E_Cu = 12e6 psi; Df = 30% | — | PTH strain/life calc | calc | Fig. 60.22 caption | high |
| COOMBS-4102 | reliability | Effective strain correction in the IPC PTH model: strain-distribution factor Kd (typically 1.6) and plating-quality factor KQ. | Δε_eff = Kd·Δε·(10/KQ); Kd ≈ 1.6; KQ: extraordinary 10, superior 8.7, good 6.7, marginal 4.8, poor 3.5 | Δε, KQ | PTH life prediction | calc | §60.4.2 | high |
| COOMBS-4103 | reliability | Designer/fabricator controls on PTH life: out-of-plane CTE, plating thickness, aspect ratio, plating strength/ductility/quality. | — | — | PTH design | review | §60.4.2 | high |
| COOMBS-4104 | reliability | FEA findings (Barker & Dasgupta): closer PTH spacing improves PTH mechanical reliability; lower AR (thinner board more effective than bigger hole) helps; inner planes/non-functional pads relieve local stress in FR-4 (raise it in Kevlar-PI); solder fill/voids don't change barrel stress; wave soldering transient consumed 33% of life but cooling compression gave back 25%. | — | — | PTH design | review | §60.4.2 | high |
| COOMBS-4105 | reliability | IST RT→150°C material effect: low-Tg/high-CTE material ≈ 370 cycles; lowest-CTE material ≈ 2900 cycles; ENIG finish gave highest CTF (higher modulus, lower CTE than HASL). | 370 vs 2900 cycles | laminate CTE/Tg, finish | material selection | measure | §60.4.2, Table 60.5 (values in prose) | high |
| COOMBS-4106 | reliability | High-density PTH cycling (Goyal): 1000 cycles −55/125°C (cond. B) or −65/150°C (cond. C); solder-filled PTHs: 0 failures; unfilled: cumulative failures cond. B 1/3/24/59% at 100/200/500/1000 cycles; cond. C 10/82/100% at 200/500/1000. Failure = barrel necking/cup-cone crack near board mid-thickness. | see values | — | unfilled vs filled PTH | measure | §60.4.2 | high |
| COOMBS-4107 | reliability | FEA sensitivities: +20% board thickness → +8–30% Cu barrel stress; Cu plating 12 → 38 µm cuts stress 25–70%; Ni 2.5 → 15 µm cuts Cu stress 30–70% (Ni more effective per µm); solder-filled vias cut barrel stress 20–70%; best fill has CTE close to Cu; prefer high-ductility, low-yield Cu. | see values | t_board, t_Cu, t_Ni | PTH design trades | calc | §60.4.2 | high |
| COOMBS-4108 | reliability | FEA −30/150°C: max von Mises at PTH mid-barrel 229.0 MPa (150°C) / 232.7 MPa (−30°C); residual strain 9613 µε; correlation to IPC model best with 20% daisy-chain resistance-change failure criterion. | — | — | reference values | sim | §60.4.2, Fig. 60.25 | high |
| COOMBS-4109 | reliability | Rigid-flex PTH: max barrel strain location depends on bond material, plating thickness, hole size, board thickness; acrylic adhesive (lower Tg) gives larger strain than epoxy/polyimide adhesive — prefer epoxy/PI adhesive for thermal-cycled rigid-flex. | — | adhesive type | rigid-flex | review | §60.4.2 | high |
| COOMBS-4110 | reliability | Inverse-power-law (IPL) acceleration is appropriate for Cu PTH thermal cycling (not Arrhenius/Eyring); log(N_f) is linear in log(stress or ΔT) with a discontinuity at Tg. | log N = a − n·log(S) (standard IPL; equation body missing in text) | N_f, S | PTH acceleration | calc | §60.4.3 | medium |
| COOMBS-4111 | reliability | Laminate property jump at Tg (measured, one FR-4): z-CTE 28.9 → 128.7 ppm/°C (4.45×); DMA storage modulus 18,000 → 2,500 MPa (7.2× drop). | α1 = 28.9, α2 = 128.7 ppm/°C; E 18 → 2.5 GPa | — | stress/strain estimates across Tg | calc | §60.4.3 | high |
| COOMBS-4112 | reliability | IST above Tg: 215°C is about the lowest peak still above Tg; 275°C produced non-PTH (post) interconnect failures (2 of 12 coupons; 0.85 mm holes, 3.3:1 AR) — don't test above the lead-free peak zone. Worst-case with 18× preconditioning at 245°C: 3,500 cycles, "> 9 years in the field at one thermal cycle/day" (text notes 18× as "> 2.5× is allowed on actual product with eutectic solder" — wording ambiguous). | 3500 cycles ≈ 9.6 yr @ 1/day | — | IST test design | review | §60.4.3 | high |
| COOMBS-4113 | reliability | Pb-free assembly damage: 0.8 mm via pitch is considerably more susceptible than 1.0 mm; 6× solder shock at 288°C is usually more severe than 6× reflow at 260°C, but hole-wall separation occurs more after 6× 260°C reflow (longer time at temperature). Example product: 20 layers, 2.92 mm, 11.5:1 AR. | — | via pitch, AR | thick high-AR Pb-free boards | review | §60.4.3 | high |
| COOMBS-4114 | materials | For PTH life, z-CTE below Tg (α1) is the key contributor; lower-resin-content constructions (lower z-CTE) last considerably longer; supplier-advertised α1 does not match measured multilayer values — measure on the actual construction. | — | α1 measured | material qualification | measure | §60.4.3 | high |
| COOMBS-4115 | reliability | PTH IPL data (Park): B10 = 606 cycles at ΔT 180°C (−55/125) and 1,065 cycles at ΔT 160°C (−35/125); acceleration factors 49 and 28 relative to field ΔT 80°C (−40/+40). | AF(180→80) = 49; AF(160→80) = 28 | ΔT | PTH acceleration | calc | §60.4.3 | high |
| COOMBS-4116 | reliability | Corner (pad/barrel knee) cracking under solder-pot-like shock (hot oil 240°C → forced-air RT): FR-4 ≈ 10 cycles avg, cyanate ester ≈ 50 cycles; FEA shows peaks at pad corner and mid-barrel. | 10 (FR-4) / 50 (CE) cycles | — | high-pin-count TH rework budgets | review | §60.4.4 | high |
| COOMBS-4117 | reliability | Pad-tilt strain at the pad-to-barrel joint (cantilever model): strain grows with laminate free expansion and pad thickness, falls with the square of remaining annular ring; use minimum remaining annular ring after drill misregistration. | ε = 3·d·r·b / (2·L²) as printed; text derivation: pad treated as cantilever, c = b/2 (b = pad thickness), end deflection δ = t·d (t = half board thickness, d = α_z·ΔT laminate free expansion) → printed "r" ≡ t; L = minimum remaining annular ring | b, d, L | annular ring sizing | calc | §60.4.4, Fig. 60.30 | medium |
| COOMBS-4118 | reliability | Solder-filled PTH: cracks initiate in the solder fill and then drive PTH corner cracks (~500 cycles); a solder dome over the PTH ring prevented both. | — | fill condition | TH joints | inspect | §60.4.4 | high |
| COOMBS-4119 | reliability | Small-PTH cycling (Wu, IPC-9701 0–100°C, 10°C/min, 6,000 cycles, 96-mil board): no failures for hole dia > 18 mil or AR < 5.3; first failures 10/12/16-mil holes at 2518/1830/3985 cycles; Weibull (shape, characteristic life) 10 mil: 4.92, 3932; 12 mil: 5.70, 4439; 16 mil: 11.89, 5037. | AR < 5.3 → no failure @ 6000 cycles 0–100°C | hole dia, thickness | small-hole PTH life | calc | §60.4.5 | high |
| COOMBS-4120 | via | Very small PTHs (≈114 µm / 4.5 mil) on 0.5 mm grid are mechanically robust but prone to crazing (fine crack networks) that become CAF paths — restrict such hole/grid sizes to controlled, non-humid environments. | dia ≈ 114 µm @ 0.5 mm grid → humidity-free use only | hole dia, grid, environment | small-hole HDI | review | §60.4.5 | high |
| COOMBS-4121 | via | PTH fatigue life is nearly insensitive to hole diameter in the 203–355 µm (8–14 mil) range (FEA on thick board; HATS −55/145°C data) — plating thickness, z-CTE and Tg are the levers, not hole size. | 203–355 µm: no clear trend | hole dia | thick boards (coupons 3.0 mm, 0.25 mm vias) | review | §60.4.5, Figs. 60.34–60.36 | high |
| COOMBS-4122 | via | Hole-fill material: lower fill CTE and lower fill modulus reduce PTH stress, but no fill brought sidewall stress below Cu yield — fill alone cannot prevent barrel necking; change Cu thickness/via size or laminate z-CTE. | prefer low-CTE, low-modulus fill | fill CTE, modulus | filled PTHs | review | §60.4.5, Fig. 60.37 | high |
| COOMBS-4123 | reliability | Via-in-pad (unfilled conformal microvia) reduced SAC BGA thermal-cycle life (BGA192: corner/adjacent-ball void % ≈ 4× that of non-ViP); void location in the crack path matters more than void size; expect Pb-free to suffer more than SnPb. | void ≈ 4× with ViP | ViP use, package type | Pb-free BGA on ViP | review | §60.4.5, §61.1.5, Fig. 60.38 | high |
| COOMBS-4124 | reliability | Board peak temperatures in soldering: 230–245°C with SnPb, 265–280°C with Pb-free — the PCB gets hotter than most components; standard FR-4 may be inadequate for Pb-free. | 265–280°C board peak (Pb-free) | — | Pb-free assembly | review | §60.4.6 | high |
| COOMBS-4125 | reliability | Each additional Pb-free reflow (250°C preconditioning 2× → 3×) cut subsequent HATS (−55/145°C) 63% life from 422 to ≈292–294 cycles (≈30% loss) — budget rework/reflow count. | −30% life per extra reflow (example) | reflow count | FR-4 PTH under Pb-free | calc | §60.4.6, Fig. 60.39 | high |
| COOMBS-4126 | materials | Soldering Temperature Impact Index (Engelmaier) for Pb-free laminate suitability; higher STII → more cycles to failure (range studied 181–247). | STII = (Tg + Td)/2 − [% thermal expansion 50→260°C] × 10 (temperatures in °C) | Tg, Td, z-expansion 50–260°C (%) | Pb-free laminate selection | calc | §60.4.6, Fig. 60.40 | high |
| COOMBS-4127 | via | Pb-free soldering (high Sn, higher T) dissolves up to 12 µm (0.5 mil) of barrel Cu — raise the minimum plating thickness accordingly, and bake out moisture more rigorously before Pb-free soldering. | allow ≥ 12 µm dissolution loss | plating spec | Pb-free assembly | calc | §60.4.6 | high |
| COOMBS-4128 | materials | Laminate thermal-stability metrics: time at 200°C for flexural strength to fall to 50%; time-to-blister in 290°C solder float; Cu peel after elevated-T exposure. | 200°C → 50% flexural; 290°C float blister time | — | material qualification | measure | §60.4.6 | high |
| COOMBS-4129 | reliability | Pb-free PTH qualification protocol (industry consortium): precondition 6× reflow at 260°C, then air-to-air −40/+135°C (10 min ramps and dwells) and IST 23→150°C (3 min heat, 2 min cool, no dwell), 3000 cycles (6000 for robust materials); also 6× solder float at 288°C — usually more severe than 6× 260°C reflow; use both. | 6×260°C; AtA −40/135; IST 23/150; 3000–6000 cycles; 6×288°C float | — | Pb-free material/product qualification | measure | §60.4.6 | high |
| COOMBS-4130 | reliability | Mechanical qualification standards: IPC/JEDEC-9702 (4-point bend), 9704 (strain-gage placement), 9707 (spherical bend for area arrays), IPC-9703 (drop/shock guidelines), IPC-9708 (pad cratering, Pb-free/phenolic boards), JESD22-B111 (portable drop: 1500 G, 0.5 ms half-sine per JESD22-B110 cond. B / B104-B), MIL-STD-810F; also MIL-HDBK-310, SAE J1211, Telcordia GR-3108, IEC 60721-3, IPC-SM-785, IPC-9701. | drop pulse 1500 G / 0.5 ms half-sine | — | mechanical test planning | review | §60.4.7 | high |
| COOMBS-4131 | reliability | IPC-9701(A) thermal cycling: reference TC1 = 0/100°C; TC4 = −55/125°C (military); number of cycles from 200 (min) to 6000 (reference); 3 of 5 conditions match JESD22-A104-A; SAC alloys need longer dwell (slower creep); Appendix A (2006) covers Pb-free. | TC1 0/100; TC4 −55/125; NTC 200–6000 | — | solder-attach qualification | measure | §60.4.7 | high |
| COOMBS-4132 | reliability | Miner cumulative-damage rule for combining assembly, test and field thermal cycles. | Σ n_i/N_i = C, 0.7 ≤ C ≤ 2.2 (C = 1 for simple life-fraction accounting) | n_i cycles applied, N_i life at each level | PTH field-life projection | calc | §60.4.8 | high |
| COOMBS-4133 | reliability | Worked PTH field-life budget (hole 0.0135 in, plating 0.0010–0.0015 in, difunctional FR-4, 7 assembly cycles): barrel uses 7/27 = 41%, knee 7/17 = 26% of life in assembly; remaining 59% of 19,400 barrel field cycles / 74% of 8,780 knee field cycles → knee wears out first at ≈6,500 field cycles; each extra assembly cycle ≡ 1,175 field cycles (barrel) or 318 (knee). | 1 assembly cycle ≈ 318–1175 field cycles | — | PTH life accounting | calc | §60.4.8, Table 60.7 (values in prose) | high |
| COOMBS-4134 | reliability | PTH life ∝ ½·(εf/Δε)^m — raise Cu ductility (εf) and yield strength (lowers Δε); balance the two since they trade off. | N_f ∝ 0.5·(εf/Δε)^m | εf, Δε | PTH design | calc | §60.4.9 | high |
| COOMBS-4135 | reliability | Single most effective PTH life measure: reduce the thermal-cycle range, especially any excursion above Tg; also preheat before HASL/wave/solder-pot rework to eliminate shocks. | minimize ΔT; keep T_max < Tg | ΔT, Tg | PTH life | review | §60.4.9, Fig. 60.42 | high |
| COOMBS-4136 | reliability | Reference PTH model parameters (acid-sulfate Cu on FR-4): strain energy to fracture 50 J/cm³; hole radius 0.45 mm; plating 0.02 mm; board thickness 2 mm; hole-center-to-pad-edge and to free end 0.8 mm. | see values | — | PTH model benchmarking | calc | Fig. 60.42 caption | high |
| COOMBS-4137 | via | Aspect ratio (board thickness / finished hole): > 3:1 requires good-quality plating; > 5:1 not recommended (center-barrel plating thickness); boards with ≥ 8 layers tend to high AR. | AR ≤ 5:1 (hard limit); ≤ 3:1 preferred | thickness, hole dia | PTH design | calc | §60.4.9 | high |
| COOMBS-4138 | via | Thicker barrel plating raises cycles-to-failure and lengthens the crack path to electrical open. | ↑ t_Cu → ↑ N_f | t_Cu | PTH design | review | §60.4.9, Fig. 60.45 | high |
| COOMBS-4139 | reliability | Ni over Cu in the barrel extends PTH life ≈ 3× or more (Ni layer stops the crack, survives 1000 cycles); but nicks/bubbles/breaks in the Ni cause "nickel acceleration" — failure in ≈ 1/3 the time of Ni-free coupons. Inspect Ni continuity. | ≈ 3× life (good Ni); ≈ 1/3 life (defective Ni) | Ni quality | Ni-plated PTH | inspect | §60.4.9 | high |
| COOMBS-4140 | reliability | Modeled (1.6 mm board, 0.25 mm PTH, 32 µm Cu): PTH fatigue life falls as Cu layer count rises (2→8 layers); higher PTH density raises cycles-to-failure. | — | layer count, PTH density | multilayer PTH | review | §60.4.9, Fig. 60.46 | high |
| COOMBS-4141 | fab | Inner-layer interconnect reliability ranking (Reid): flush ≈ best, negative etchback ≈ as robust, three-point-contact (positive etchback) least reliable (foil cracks). Conflicts with the "flush most dangerous" view in §60.3.4.3 — treat etchback type as a supplier-qualification item, not a fixed rule. | — | etchback type | PTH inner-layer connection | review | §60.4.9, Fig. 60.47 | medium |
| COOMBS-4142 | via | Microvia failure modes in priority order: base-to-target-pad separation (most common), barrel crack, corner crack, pull-out (circumferential crack); stacked (esp. Cu-filled) microvias add corner-crack modes. | — | via structure | HDI | inspect | §61.1.2 | high |
| COOMBS-4143 | via | Via-in-pad voiding (SnPb data): voids fall with pitch (except 1.27 mm BGA); smaller microvia → smaller void; Cu-filled or inverted microvias ≈ no voids; ENIG ≈ 25% more voids than IAg (OSP similar to IAg); 100 µm (4 mil) ViP = 6% of voids vs 150 µm 40% and 200 µm 46%; 1-layer-deep microvias 12% vs 3-layer-deep 56%; thinner PCB → more voids. | prefer ≤ 100 µm, 1-layer-deep, filled ViP | ViP dia, depth, fill, finish | ViP designs | review | §61.1.4 | high |
| COOMBS-4144 | solder | Reflow profile levers against ViP voids: extended soak above 150°C, lower peak, shorter time above liquidus; paste type/particle size/double print have minimal effect; Ag addition to SnPb reduces void size. | — | profile | ViP assembly | review | §61.1.4 | high |
| COOMBS-4145 | solder | SAC alloy ViP voiding (simulation): lowest for Sn95.5Ag3.8Cu0.7 and Sn95.5Ag3.5Cu1.5; voiding rises as Ag drops below 3.5% (higher surface tension). | prefer Ag ≥ 3.5 wt% for ViP | alloy | Pb-free ViP | review | §61.1.4 | high |
| COOMBS-4146 | reliability | "Thermal shock" is a ramp faster than 20°C/min (IPC-9701A); solder-mask cure and HASL can impose such rates on the bare board. | > 20°C/min = shock | ramp rate | test classification | calc | §61.1.5 | high |
| COOMBS-4147 | reliability | 0.4 mm FPBGA with microvias: ViP substrate gave +20% thermal-cycle life vs non-ViP; drop: ViP(substrate)/NViP(board) first failure at 148 drops vs ViP/ViP at 7 drops; bend cycling: ViP/ViP best. Choose the ViP combination per dominant load. | 148 vs 7 drops | ViP on package/board | 0.4 mm CSP | review | §61.1.5 | high |
| COOMBS-4148 | via | Microvia distance to PTH (LLTS −55/125°C, 10 s transition): most failures at 1 mm edge spacing (1.5 mm c-c from a 0.5 mm PTH); few at 125 µm spacing; first failure 1,100 cycles. Proximity is not simply "closer is worse". | — | via-to-PTH spacing | HDI layout | review | §61.1.5, Table 61.3 (not in text) | high |
| COOMBS-4149 | reliability | Microvia IST peak-temperature selection (after 5× 230°C precondition): 150/170/190/210/220°C → mean CTF 1000/789/464/76/44 cycles; 190°C chosen (< 500 cycles for marginal vias); ≥ 210°C produces knee cracks/delamination artifacts — unacceptable for qualification. | T_peak = 190°C | — | microvia qualification | measure | §61.1.5 | high |
| COOMBS-4150 | reliability | Pb-free preconditioning is severe for marginal microvias: coupons giving 788 IST cycles (150°C) fell to 443 after 6× 230°C and to 4 cycles after 6× 260°C; phenolic FR-4 microvias passed 1000 cycles at 190°C after 5× 230°C. | 788 → 443 → 4 cycles | precondition T, count | HDI Pb-free | measure | §61.1.5 | high |
| COOMBS-4151 | via | ALIVH handset board benchmark: 100/100 µm line/space, 200/400 µm via/land, 8 layers, 0.8 mm thick, low-moisture epoxy-glass; passed 500 shocks −25/125°C, 1000 h 85°C/85% RH, 1.5 m drop on hard vinyl. | 100/100 µm; 200/400 µm | — | any-layer via boards | measure | §61.1.5 | high |
| COOMBS-4152 | via | Voids in filled microvias: shape dominates — large rounded voids crack less than small sharp-cornered ones; degradation onset 2/65 non-voided vs 22/29 voided samples (some stress relief from voids). | — | void shape/size | filled microvias | inspect | §61.1.5, Fig. 61.4 | high |
| COOMBS-4153 | materials | Measured HDI PCB CTEs (TMA): z 43.21 ppm/°C, y 14.62, x 12.83 below Tg; z 297.7 ppm/°C above Tg; Tg ≈ 145°C (146.71°C); delamination after 260°C exposure; 3 TMA cycles −100/245°C gave no delamination. | see values | — | reference laminate data | calc | §61.1.5, §61.1.7, Fig. 61.9 | high |
| COOMBS-4154 | via | Microvia robustness ranking: unfilled surface microvia (best) > buried microvia filled at b-stage > third-material-filled > Cu-filled (worst, corner cracks); capped vs uncapped stand-alone microvias make no difference if the process is robust. | — | fill type | HDI | review | §61.1.6 | high |
| COOMBS-4155 | via | Microvia FEA (70 µm dielectric): total strain range rises as microvia diameter shrinks → lower fatigue life; thicker wall lowers TSR; at 20 µm wall the via has almost no plastic strain (fails in high-cycle regime). | ↓ dia → ↑ TSR; wall ≥ 20 µm | dia, wall thickness | microvia design | sim | §61.1.6, Fig. 61.11 | high |
| COOMBS-4156 | reliability | Microvias (0.1–0.15 mm) under WLCSP joints reduce global deflection but raise joint shear stress/creep strain and reduce solder-joint fatigue life (slightly worse for 96.5Sn3.5Ag than 62Sn2Ag36Pb); via stress stays below ED-Cu ultimate strength. | — | ViP under WLCSP | WLCSP assembly | sim | §61.1.6 | high |
| COOMBS-4157 | via | Microvia DOE (−55/125°C): smaller microvias have more manufacturing defects; any microvia electrically continuous before test survived 1000 cycles; pitch had no effect; 100 µm microvia predicted 2,607 cycles by IPC-TR-579 model. | 2607 cycles predicted; ≥ 1000 observed | — | microvia qualification | measure | §61.1.6 | high |
| COOMBS-4158 | via | Stacked microvias: corner stress on the bottom via rises with stack count; offsetting the stack from the resin-filled PTH lowered max stress from 37 to 30 kgf/mm² (≈53 → 43 ksi). Staggered microvias are ≈ 2 orders of magnitude more robust than stacked; pad rotation reverses for stacks ≥ 3. | prefer staggered; offset stacks | stack count, offset | HDI build-up | sim | §61.1.6, Table 61.4 (not in text) | high |
| COOMBS-4159 | via | 50 µm (2 mil) ViP microvias failed after 100 cycles −65/150°C; larger (3–4 mil) filled vias did not; optical microscopy beats x-ray for microvia condition (x-ray only shows fill). | dia ≥ 75 µm (3 mil) | via dia | fine microvias | inspect | §61.1.7 | high |
| COOMBS-4160 | reliability | Ceramic BGA body size is limited to ≈ 32 mm per side (32 × 32 mm) by CTE mismatch/DNP; larger ceramics need solder columns or sockets/connectors. | ≤ 32 mm | package type, size | ceramic packages | review | §62.2, Fig. 62.4, §62.3.13.8 | high |
| COOMBS-4161 | requirements | Automotive environment reference: −55°C to > 95°C, up to 100% RH, minutes-scale transitions, severe shock/vibration; on-engine 150–175°C. Measure the actual environment with thermocouples/accelerometers before qualification. | −55…>95°C; 100% RH; on-engine 150–175°C | — | env. definition | review | §62.3.1, §63.1, Table 62.1 (not in text) | high |
| COOMBS-4162 | reliability | Mirrored (back-to-back) BGAs: assume 50% reduction in solder-joint fatigue life (first pass); avoid; if unavoidable use quasi-mirror with NO common through-vias; stacked-package baseline is ≈10% below single package. | life × 0.5 | placement mirroring | double-sided BGA | calc | §62.3.2 | high |
| COOMBS-4163 | reliability | Solder-joint life falls with board thickness/stiffness (worse for ceramic than organic packages); qualify each package on two board thicknesses spanning use (IPC-9701). | 2 thicknesses | board thickness, layer count | BGA qualification | measure | §62.3.3 | high |
| COOMBS-4164 | dfm | Distribute packages uniformly on both sides and balance copper to limit post-reflow warpage (low-CTE packages on one side bow the board convex). | — | placement, Cu balance | dense BGA boards | review | §62.3.4 | high |
| COOMBS-4165 | assembly | Pb-free reflow peaks 235–260°C vs 220°C SnPb → higher residual stress; control the cooling ramp (multi-zone cooling, forced convection preferred over IR). | 235–260°C | profile | Pb-free assembly | review | §62.3.4.1 | high |
| COOMBS-4166 | materials | Dicy-cured FR-4 limited to ≤ 240°C peak reflow; use phenolic-cured FR-4 above 240°C (delamination resistance over multiple reflows); profile large boards to verify the actual board temperature rise. | dicy ≤ 240°C; phenolic > 240°C | laminate cure system, peak T | Pb-free | review | §62.3.5.1 | high |
| COOMBS-4167 | reliability | Second-level qualification test vehicles must include first-level (die-to-package) daisy chains so board-attach stress on the die/package is caught. | — | — | package qualification | review | §62.3.6 | high |
| COOMBS-4168 | reliability | Thermal-cycle qualify back-side components separately — they see over-contraction and residual stress from the second reflow. | — | — | double-sided assemblies | measure | §62.3.7 | high |
| COOMBS-4169 | assembly | Warpage vs bridging (1 mm pitch, SnPb surface tension): joint max diameter > 40 mil (1.016 mm) → bridge; effective package+board warpage > ≈ 9 mil (0.23 mm) over 7 mm → bridge (e.g. board concave 5 mil + package convex 4 mil). JEDEC ±8 mil coplanarity alone is insufficient for large packages on thick boards; measure warpage through the reflow range (JESD22-B112). | Δwarp ≤ 9 mil / 7 mm; d_max ≤ 40 mil @ 1 mm pitch | package/board warpage at liquidus | large BGAs (≥ 50 mm) on thick (≥ 125 mil, 20+ layer) boards | measure | §62.3.8, Figs. 62.13–62.14 | high |
| COOMBS-4170 | dfm | Typical high-end PWB planarity tolerance ±4 mil over a package site; tighter is cost-prohibitive. | ±4 mil (0.1 mm) | — | large-package sites | inspect | §62.3.8 | high |
| COOMBS-4171 | components | Depopulating the 6 corner-most balls at each corner absorbs ≈ 2 mil of effective warpage and improves fatigue life; many suppliers drop the 4 corner balls. | −6 balls/corner ≈ 2 mil | ball map | large organic BGAs | review | §62.3.8, Fig. 62.15 | high |
| COOMBS-4172 | dfm | BGA pad sizing: PWB pad = 80–100% of the package-side wetted pad area (equal is optimal; mismatch costs up to 25% fatigue life, smaller side fails first); NSMD pads for 1.27–0.8 mm pitch; SMD improves shock but degrades thermal fatigue; below 0.8 mm a NSMD/SMD mix is often forced by routing. | 0.8 ≤ A_pwb/A_pkg ≤ 1.0 | package pad size (JEDEC Pub 95 nomenclature) | BGA land patterns | calc | §62.3.9, Fig. 62.16 | high |
| COOMBS-4173 | dfm | Fabricated NSMD pad size varies: a 12-mil spec measured 9–15 mil — run WC/RSS tolerance analysis (IPC-7351) so the PWB pad never significantly exceeds the package pad; critical below 0.8 mm pitch. | 12 mil spec → 9–15 mil actual | pad spec, fab tolerance | fine-pitch BGA | calc | §62.3.9 | high |
| COOMBS-4174 | mechanical | Large heatsinks (≈10 in², > 1 lb; cards to 1000 W) must not transfer bolt-down compressive load to the package (die crack, ball collapse/bridging); attachment must absorb height/warpage tolerance; verify load with pressure-indicating film; in thermal-cycle tests shield/calibrate so joints see the same ΔT, and add a static high-temperature dwell for the creep-collapse mode. | — | heatsink mass, mount | heatsinked BGAs | measure | §62.3.10, Table 62.2 (not in text) | high |
| COOMBS-4175 | reliability | ENIG risks: brittle interfacial fracture at high strain rate (above ≈ 5000 µε/s bulk solder acts elastically and dumps strain into the Kirkendall-voided Ni-P/IMC interface); Ni-Cu-Sn ternary IMC grows with reflows; black pad from bath impurities (lot-dependent, visible discoloration). Use a Ni barrier on the board side to limit Cu migration; characterize strain/strain-rate per finish. | strain-rate threshold ≈ 5000 µε/s | finish, strain rate | ENIG packages/boards | measure | §62.3.11.1 | high |
| COOMBS-4176 | reliability | Solder-on-pad (no Ni barrier): pre-applied solder height must not exceed solder-mask thickness; Cu6Sn5/Cu3Sn thicken with aging → Kirkendall voiding; fit extrapolation at 50°C: 6000 days (16.5 yr) to 50% interface void area; un-aged SoP joints up to 2× ENIG strength. | h_solder ≤ t_mask; 50%-void at 50°C ≈ 16.5 yr | operating T, aging | SoP/OSP joints | review | §62.3.11.2, Fig. 62.23 | high |
| COOMBS-4177 | test | ICT strain control: distribute test points uniformly under BGAs; avoid push-fingers (never near package corners) — prefer a milled "zero-flex" top plate; boards < 93 mil are most at risk; verify with strain gages per IPC/JEDEC-9704; expect higher probe force with high-T OSP on Pb-free. | thickness < 93 mil = high risk | test-point map, fixture | ICT fixtures | measure | §62.3.12 | high |
| COOMBS-4178 | reliability | Distance-from-neutral-point: larger DNP → lower joint life; a package with 10–20% smaller DNP (all else equal) may be accepted on similarity to a qualified one; larger DNP needs full requalification. | ΔDNP ≤ −10…−20% by similarity | DNP | BGA qualification by similarity | calc | §62.3.13.1 | high |
| COOMBS-4179 | reliability | Ball size/stand-off: 0.889 mm (35 mil) balls ≈ 1.3× the fatigue life of 0.762 mm (30 mil) balls (FEA); pitch reduction lowers life via smaller balls/stand-off. | life(35 mil)/life(30 mil) ≈ 1.3 | ball dia | BGA selection | calc | §62.3.13.2, Fig. 62.26 | high |
| COOMBS-4180 | components | Prefer ball maps depopulated under the die perimeter and at package corners; place only redundant power/ground or thermal balls under the die core. | — | ball map vs die outline | PBGA | review | §62.3.13.3 | high |
| COOMBS-4181 | thermal | Lid/heat-spreader materials: AlSiC ≈ 180–200 W/(m·K) (≈ Al), lower CTE and slightly higher modulus than Cu; PBGA > 40 mm: use an integrated heat spreader to limit reflow warpage; mold compound Tg must be adequate for the peak reflow. | AlSiC k = 180–200 W/(m·K); PBGA > 40 mm → spreader | — | large packages | review | §62.3.13.4–5 | high |
| COOMBS-4182 | reliability | Larger die-to-package size ratio → higher CTE-mismatch strain in second-level joints (PBGA); plastic substrates match PWB CTE, ceramic substrates do not (limit ≈ 32 × 32 mm). | — | die size / body size | package selection | review | §62.3.13.7–8 | high |
| COOMBS-4183 | reliability | Low-k die packages: underfill/mold stiffness must be balanced (too stiff → low-k/ILD delamination, too soft → first-level failure); verify with component- and board-level cycling followed by SAM. | — | underfill E, CTE, Tg | FCBGA with low-k | measure | §62.3.13.6, §62.3.13.9 | high |
| COOMBS-4184 | reliability | Failure-rate units: 1 FIT = 1 failure per 1e9 device-hours; solder joints must be designed to fail after the components (joint failure rate below the component FIT budget). | 1 FIT = 1e-9 /h | — | reliability budgeting | calc | §63.1 | high |
| COOMBS-4185 | requirements | Design-life / failure-level benchmarks: laptop/desktop 3–5 yr; automobile 10 yr or 100,000 miles; aerospace/medical/solar no failures at 40 yr; telecom < 0.01% cumulative failures at 15–20 yr. | see values | product class | reliability goal setting | review | §63.2 | high |
| COOMBS-4186 | mechanical | Soft solder joints are not load-carrying members: never subject them to constant static mechanical load (creep rupture) — by design use mechanical fastening for loads. | static load = 0 on solder joints | — | all soldered assemblies | review | §63.3 | high |
| COOMBS-4187 | components | Alloy-42 lead frames (CTE ≈ 4 ppm/°C) vs solder (≈ 24 ppm/°C) add local mismatch stress (failures even at IPC Class III); for harsh environments require zero lead offset/rotation or avoid Alloy 42; Cu lead frames (≈ 17 ppm/°C) are benign. | Alloy 42: 4 ppm/°C; solder ≈ 24; Cu ≈ 17 | lead-frame material | SOT/SOD/TSOP in harsh env. | review | §63.3 | high |
| COOMBS-4188 | components | Low-profile leaded parts with short leads (e.g. thin SOIC) may lack lead compliance — estimate or measure lead stiffness together with board/component in-plane CTEs before relying on lead compliance. | — | lead stiffness, CTEs | short-lead packages | calc | §63.3 | high |
| COOMBS-4189 | reliability | Count every thermo-mechanical cycle from end of assembly to end of life — transport/storage diurnal and seasonal cycles caused LCCC failures in otherwise mild (37°C) medical-implant service. | — | shipping/storage profile | all products | review | §63.3 | high |
| COOMBS-4190 | reliability | Max cyclic shear strain of the critical (corner) joint under thermal cycling (rigid board/component, full stress relaxation). Example: CBGA 6 ppm/°C, board 18 ppm/°C, 20×20 @ 1 mm, hS = 0.508 mm, L = 10·1·√2 = 14.142 mm, ΔT = 30°C → γ = 1.0% (0.57°) — flag for deeper study (not an absolute limit). | γ = L·abs(α_B − α_C)·ΔT / h_S (dimensionless; L, h_S in mm, α in 1/°C) | DNP L, stand-off h_S, CTEs, ΔT | area-array / leadless joints | calc | §63.4.1, Eq. 63.1a (verified against worked example) | high |
| COOMBS-4191 | reliability | Thermal-cycle joint life follows Coffin-Manson in shear strain with exponent m ≈ 1–2; measured slope vs CTE mismatch is exactly −2 (LCCC 5.4 ppm/°C on 9–21 ppm/°C boards; CSP 8.6 ppm/°C on 13.4–17.3 ppm/°C boards: +4 ppm/°C mismatch cut life 2000 → 500 cycles). | N_f ∝ (1/γ)^m, m = 1–2; N_f ∝ (Δα)^−2 | γ or Δα | thermal cycling | calc | §63.4.1, Eq. 63.2, Fig. 63.2 | high |
| COOMBS-4192 | reliability | Four design levers for thermal-cycle joint life (any alloy): smaller component/die, smaller abs(α_B − α_C), larger stand-off h_S, smaller ΔT (and keep ΔT from growing via reliable cooling). | — | — | all SMT | review | §63.4.1 | high |
| COOMBS-4193 | reliability | Single-sided assemblies relieve joint strain by bimetallic bending (thin, compliant boards live longer); mirrored back-to-back mounting suppresses it: life ÷ 2…3 (Juso 1998, Primavera 2003, Shih 2004). Mirrored stiffness (derived from text: K3 → ∞, K2 halved): 1/K_mirr = 1/K1 + 2/K2; since life ∝ 1/K, N_mirrored/N_single ≈ K/K_mirr (< 1) (text: "ratio ... goes as K/K_MIRRORED"). | life_mirrored ≈ life/2 … life/3 | mirroring, K1, K2 | double-sided BGA | calc | §63.4.1, §63.6.4 | high |
| COOMBS-4194 | mechanical | Board clamped on two opposite edges: curvature peaks at the center AND at the clamped edges; mount large critical components at X = B/4 and 3B/4 (zero curvature); add stiffening ribs spanning clamp-to-clamp (along the bending axis) — ribs in the other direction add mass, lower fn and worsen deflection. | critical parts at B/4, 3B/4 | span B, clamp layout | vibration/shock/drop | review | §63.4.2, Fig. 63.5 | high |
| COOMBS-4195 | mechanical | Board natural frequency rises with flexural rigidity D_B and falls with mass per area ρ_B; center displacement ∝ G_out/fn², G_out = Q·G_in with Q ≈ √fn — raise fn (thicker/stiffer board, less mass) to cut joint strain in vibration. | D_B = E_B·h_B³ / (12·(1 − ν_B²)); fn ∝ sqrt(D_B/ρ_B) (equation bodies missing in text; standard forms) | E_B, ν_B, h_B, ρ_B | vibration design | calc | §63.4.2, Eqs. 63.4–63.5 | medium |
| COOMBS-4196 | reliability | Initial intermetallic thickness (set by reflow profile/time above liquidus) is a life driver: 1206 resistor joints lost > 2× characteristic thermal-cycle life when initial IMC grew 1 → 2.5 µm; vibration life shows an optimum IMC thickness. Monitor reflow profile deviations as reliability variables. | IMC 1 → 2.5 µm ⇒ life ÷ > 2 | IMC thickness | SnPb data (device-specific) | measure | §63.4.3, Fig. 63.6 | high |
| COOMBS-4197 | reliability | Joint-life models need 15 inputs: 9 board/component material properties (in-plane CTEs, tensile and flexural moduli, Poisson ratios), 5 geometric (DNP, joint thickness, board and component thickness, joint crack area A) plus pitch P; assembly stiffness for single-sided leadless parts = three springs in series (component stretch K1, board stretch K2, assembly bending K3). | 1/K = 1/K1 + 1/K2 + 1/K3 | listed parameters | strain-energy life models | calc | §63.5, Fig. 63.7, Eq. 63.7 (spring formulas missing in text) | medium |
| COOMBS-4198 | reliability | Cycles to failure scaled by crack area vary inversely with strain-energy density per cycle (hysteresis-loop area) for SnPb and SAC387/396; shear strain per °C = L·Δα/h_S sets the maximum energy density — minimize it by design regardless of alloy. | N_f/A = C/ΔW (C = solder-dependent constant; equation body missing in text) | ΔW, A | thermal cycling | calc | §63.5, Eqs. 63.8–63.9 | medium |
| COOMBS-4199 | materials | Commercial FR-4 board Tg ≈ 110–150°C; never operate or accelerate-test assembled boards above Tg (moduli drop by orders of magnitude; test data uninterpretable). | T_max < Tg (110–150°C typical) | Tg | all FR-4 assemblies | review | §63.6.1 | high |
| COOMBS-4200 | materials | Measured FR-4 board properties span in-plane CTE 12–21 ppm/°C and Young's modulus 10–30 GPa; there are no "typical" values — never use prepreg/laminate datasheet numbers; measure product-board coupons (strain gauge, TMA or moiré for CTE; DMA or 3/4-point bend for modulus; IPC-TM-650 2.4.24 Tg, 2.4.41 x/y CTE; ASTM D3039, D790, D6272). Component-area coupons read 1–2 ppm/°C higher CTE. | CTE 12–21 ppm/°C; E 10–30 GPa (measured range) | board construction | joint-life prediction | measure | §63.6.1, Fig. 63.9 | high |
| COOMBS-4201 | dfm | Board x- and y-CTEs can differ by up to ≈ 5 ppm/°C (example 16 vs 21, Δ = 4.7 ppm/°C): orient rectangular components (chip R/C, resistor networks) with the long axis along the lower-CTE board direction. | Δ(α_x, α_y) up to ≈ 5 ppm/°C | measured α_x, α_y | rectangular parts | review | §63.6.1 | high |
| COOMBS-4202 | reliability | Board thickness effect example: identical CSPs lived 2× longer on 0.4 mm boards than on 1.575 mm boards; thickness acts jointly with the concurrent change in board CTE and modulus (hiCTE CBGA on 62/93/130 mil boards with CTE 15.9/15.85/18.75 ppm/°C and E 26/23/30 GPa: the 93→130 mil drop is driven mostly by the CTE rise). | life(0.4 mm) ≈ 2 × life(1.575 mm) (CSP) | h_B, α_B, E_B | design curves via Eq. 63.10b (body missing in text) | calc | §63.6.2, Fig. 63.10 | high |
| COOMBS-4203 | materials | Rule-of-mixtures estimate of board in-plane CTE and modulus from the stack-up (valid for rigid, symmetrical multilayer epoxy-glass without compliant shear layers). | α_B = Σ(E_i·α_i·h_i)/Σ(E_i·h_i); E_B = Σ(E_i·h_i)/Σ(h_i) (standard forms; equation body missing in text) | h_i, α_i, E_i per layer | stack-up estimation | calc | §63.6.3 | medium |
| COOMBS-4204 | dfm | SMD vs NSMD board pads: industry favors NSMD for quality (mask registration offsets shrink wetted area unpredictably); SMD gave +15% SnPb BGA life in one study (stand-off 22.2 vs 20.8 mil, Δh_S = 1.4 mil) and mitigates pad cratering / drop with stiff Pb-free alloys — choose per dominant load. | — | load type, mask registration | BGA land patterns | review | §63.6.5, Fig. 63.11 | high |
| COOMBS-4205 | dfm | Board pad diameter ≤ component wettable pad diameter; equal is acceptable; ≈10% smaller on the board side improves thermal-cycle life (higher stand-off, shifts stress off the component side); much smaller board pads move failure to the board side and shorten life. | 0.9·c ≤ b ≤ c (b = board pad dia, c = component pad dia) | b, c | BGA/CSP land patterns | calc | §63.6.6, Fig. 63.12 | high |
| COOMBS-4206 | solder | Estimate BGA stand-off h_S by back-solving the truncated-sphere (barrel) joint volume for light packages (PBGA/CSP). | V = π·h_S·(3·(b/2)² + 3·(c/2)² + h_S²)/6 with V = ball volume + paste solder volume (standard spherical-segment form; equation body missing in text) | V, b, c | light area-array parts | calc | §63.6.6, Eq. 63.13 | medium |
| COOMBS-4207 | reliability | Board finish (immersion Ag, OSP, NiAu) shows no distinguishable effect on SAC387–396 thermal-cycle fatigue life (all within the fatigue scatter around one N_f·(1/A) vs shear-strain line, r = 0.96); finish still matters for wetting/IMC/initial quality. | — | finish | Pb-free thermal cycling | review | §63.6.7, Fig. 63.13 | high |
| COOMBS-4208 | solder | SAC Ag content trade: low-Ag (SAC105) gives 1.2–1.7× the drops-to-failure of SAC305, but thermal-cycle life rises roughly linearly with %Ag over 1–4% (slopes smaller for larger CTE mismatch and harsher cycles) — pick Ag by dominant load. | drop: SAC105/SAC305 = 1.2–1.7; TC: N_f ↑ with %Ag | alloy, load type | Pb-free alloy selection | review | §63.7.2, Figs. 63.14–63.15 | high |
| COOMBS-4209 | reliability | Dwell time in accelerated cycling: IPC-9701 offers 30+ min dwell for Pb-free vs ≈15 min SnPb, but a 10-min hot dwell already gives ≈50% stress relaxation at 100°C (SAC396, 0/100°C) and long dwells were judged unnecessary; going 10 → 30/60 min lengthens test duration 1.5–2.5×; characteristic life vs dwell follows power laws with exponents −0.18 (SAC105) and −0.22 (SAC305); typical TC test runs 3–6 months. | N_f ∝ t_dwell^−0.18…−0.22 | dwell time | Pb-free ATC planning | calc | §63.7.3, Fig. 63.16 | high |
| COOMBS-4210 | reliability | Thermal shock (rapid liquid/air transfer) runs in days but induces non-field failure modes and cannot be mapped to field ramps — use only for relative screening between parts with verified identical failure modes; thermal cycling (single-chamber, controlled ramp/dwell) is the qualification method (IPC-9701). Example profile: Tmax 100°C, Tmin −40°C, 60-min cycle. | — | — | second-level qualification | review | §64.2.1, Fig. 64.3, Table 64.1 (not in text) | high |
| COOMBS-4211 | test | Monitor daisy-chain resistance in situ with event (glitch) detectors during cycling; opens appear at temperature extremes and can close up at room temperature — periodic manual measurement underestimates failures. | continuous monitoring | — | ATC test setup | measure | §64.2.1, Fig. 64.4 | high |
| COOMBS-4212 | reliability | IPC-9701A App. B: 10-min dwell standard, 30-min (or longer) where possible for Pb-free; most damage accumulates in the hot dwell; use FEA to calibrate dwell-time effects. | dwell 10 min (30 min optional) | — | Pb-free ATC | measure | §64.2.1.1 | high |
| COOMBS-4213 | reliability | Weibull fitting: 2-parameter is more conservative than 3-parameter — choose by regression; compare data sets using double-sided confidence bounds (e.g. 90%) on the 1%-failure life, not only characteristic life η. | 90% CB on N(1%) | failure data | ATC data analysis | calc | §64.2.2, Fig. 64.5 | high |
| COOMBS-4214 | reliability | Solder constitutive modeling: Anand viscoplastic model (constants tabulated for Sn3.9Ag0.6Cu, iNEMI alloy — Table 64.2 not in text) captures steady-state but not primary creep, so it over-predicts field life where primary creep dominates; run several fatigue models and calibrate to test data. | — | — | FEA life prediction | sim | §64.2.3, Tables 64.2–64.3, 64.7 (not in text) | high |
| COOMBS-4215 | reliability | Norris-Landzberg acceleration factor (SnPb): reduces strain to ΔT for the same package; text example CBGA 20/80°C vs 0/100°C predicted AF = 3.2 (measured 2.9–3.6); conservative when mapping large lab ΔT to small field mini-cycles. | AF = N_field/N_lab = (ΔT_lab/ΔT_field)^1.9 · (f_field/f_lab)^(1/3) · exp(1414·(1/T_max,field − 1/T_max,lab)), T in K (constants 1.9, 1/3, 1414 K are the classic N-L SnPb values, not printed in text; with equal cycle frequencies they give AF = 3.27 for 0/100 → 20/80°C vs the text's 3.2) | ΔT, cycle frequency f, T_max | SnPb; same package geometry/materials | calc | §64.2.4, Eqs. 64.9–64.14, Fig. 64.7 | medium |
| COOMBS-4216 | reliability | Pb-free (SAC) modified N-L (Pan et al.): frequency term replaced by hot-dwell time and constants revised; valid within 0–100°C only; no industry-accepted Pb-free transform yet — package type, board thickness, dwell/ramp, mean temperature, DNP and Sn-grain orientation all shift AF; Pb-free ductility decreases with aging (SnPb increases). | AF = (ΔT_lab/ΔT_field)^n · (dwell-time ratio)^m · exp[(Ea/k)·(1/T_max,field − 1/T_max,lab)]; Pan constants not reproduced in the text (Eq. 64.15 body missing) — take from Pan et al., SMTA Int. 2005 | ΔT, t_dwell, T_max | SAC, 0–100°C | calc | §64.2.4.4 | medium |
| COOMBS-4217 | assembly | Mixed metallurgy (SAC balls with SnPb paste, ≈220°C peak) is not recommended: balls may not fully melt, no validated acceleration transform, unknown bend/shock behavior; if unavoidable, ensure full SAC ball melting/dissolution and benchmark process consistency and reliability. | avoid; else verify full ball melt | alloy mix | backward-compatible assembly | review | §64.2.4.5 | high |
| COOMBS-4218 | reliability | Field-life with power cycles + mini-cycles: map lab life to each condition with N-L, then Miner: N_power/N_power,only + N_mini/N_mini,only = 1 with N_mini = k·N_power (k = mini-cycles per power cycle); frequency in N-L means cycle duration, not occurrence rate. Worked example: lab AF between two profiles 0.641 (2291 → 3574 cycles); power AF 10.6 → 37,895; mini AF 45.6 → 163,020; 1 power cycle/30 d, 4 mini/day (k = 120) → 1,311 power cycles = 107.8 yr; apply safety factor 2 → 53.9 yr. | safety factor 2 on predicted life | AFs, k | server/network products | calc | §64.2.5–64.2.6, Eqs. 64.16–64.23 (Tables 64.4–64.5 not in text) | high |
| COOMBS-4219 | mechanical | Mechanical regimes: bend tests ≈ 10,000 µε/s (high strain, low rate), shock ≈ 100,000 µε/s (low strain, high rate) — characterize both; handheld shock ≈ 1500 G, server/network ≈ 500 G; run vibration for shipping; add shock indicators to shipped product. | bend 1e4 µε/s; shock 1e5 µε/s; 1500 G vs 500 G | product class | mechanical qualification | measure | §64.3, Table 64.6 (not in text) | high |
| COOMBS-4220 | test | Monotonic 4-point bend per IPC/JEDEC-9702 with three gauges (1 under corner joint, 2 under package center, 3 beside package toward anvil); production strain per IPC/JEDEC-9704 with acceptable strain vs strain-rate vs board-thickness limits (limit falls with higher rate and thinner board — graph only); ICT engage/disengage are the strain-rate spikes. | acceptance: strain(rate, thickness) curve (graph) | strain, strain rate, h_B | ICT/assembly strain control | measure | §64.3.1, Figs. 64.11–64.12, 64.21 | medium (graph) |
| COOMBS-4221 | reliability | Bend strength data (FCBGA, tested ≤ 1 day after reflow): SAC on ENIG ≈ 3× the force-to-failure of SnPb on ENIG; SnPb with small Cu addition > 2× SnPb; SOP/SOC finish > ENIG (large gain for SnPb, marginal for SAC); over 3 weeks SnPb/ENIG strength +50%, SnPb/SOP +10%, SAC unchanged — test time-after-reflow must be controlled. | see ratios | alloy, finish, age | bend qualification | measure | §64.3.1.2, Figs. 64.13–64.14 | high |
| COOMBS-4222 | mechanical | Chassis/carrier design: avoid PCBA resonance coinciding with chassis resonance with mode shapes that strain critical joints above failure strain; characterize with accelerometers + strain gauges; add stiffeners/frames/struts at high-strain locations; JESD22-B113 for cyclic bend (keypad-type repeated flexure, repeated ICT). | — | mode shapes, strains | product mechanical design | measure | §64.3.2–64.3.3 | high |
| COOMBS-4223 | test | Ball shear/pull: failure modes differ between low speed (0.0001–0.0006 m/s) and high speed (0.01–1.0 m/s); shear strength rises with speed; use JESD22-B117A high-speed procedure, characterize modes vs speed, test as soon after reflow as possible; SAC shows more interfacial fracture but moderately higher strength than SnPb. | low 1e-4…6e-4 m/s; high 0.01–1.0 m/s | speed | substrate lot monitoring | measure | §64.3.4 | high |
| COOMBS-4224 | reliability | FEA life workflow: 1/8-symmetry linear-elastic global model with unit ΔT to find the worst joint and its displacements (verify warpage by shadow moiré) → local joint model with temperature-dependent creep run 2–4 cycles to stabilize the hysteresis loop → damage metric (plastic work or plastic strain) → statistical roll-up over joints weighted by displacement/DNP; underfills with Tg 70–100°C need the temperature-stepped (5–10°C) cut-boundary method with flip-chip bumps included. | 2–4 cycles to loop stability | — | solder-joint FEA | sim | §64.4.1 | high |
| COOMBS-4225 | reliability | Bend FEA (quarter symmetry, linear-elastic solder at high rate): gauge locations 1 and 3 track critical-joint strain, location 2 (package center) is least sensitive; shrinking the package pad from 0.53 mm SMD to 0.40 mm SMD (board pad 0.5 mm NSMD fixed) raised critical joint strain ≈ 18% for the same board strain — do not transfer bend acceptance data across pad sizes. | +18% joint strain for 0.53 → 0.40 mm pad | pad sizes | bend qualification by similarity | sim | §64.4.2, Figs. 64.22–64.23 | high |
| COOMBS-4226 | cost | Flexible circuits cost more than rigid boards or flat cable of equal size — justify only where 3-D wiring, bend, weight or dynamic flexing is required; compare against rigid board + connectors + wires + assembly cost (e.g. a camera split into 1 rigid multilayer + > 10 flex circuits). | — | — | flex vs rigid decision | review | §65.1.2 | high |
| COOMBS-4227 | materials | Flex conductor/substrate basics: rolled-annealed (RA) Cu for flexibility; polyimide film for any soldering/wire-bond/flip-chip process; polyester (PET) is not solderable — low-cost for large circuits (instrument panels, printer cables); polyimide readily achieves UL 94 V-0 / VTM-0. | — | process temperature | flex material selection | review | §65.4–65.5, Tables 65.5–65.9 (not in text) | high |
| COOMBS-4228 | materials | Traditional PI films (Kapton H/HN, Apical AV) have CTE > 30 ppm/°C and high moisture uptake — unacceptable for HDI flex; use dimensionally stable low-moisture PI (Kapton E/EN/VN, Apical NP/FP, Upilex-S) for fine-pitch flex. | CTE > 30 ppm/°C → reject for HDI flex | film grade | HDI flex | review | §65.5.2.1 | high |
| COOMBS-4229 | materials | PI base-film thickness convention: 50 µm industrial/avionics; 25 µm consumer (most common, lowest cost); 12.5 µm for thinnest/most flexible; thicker film → higher reliability. | 12.5 / 25 / 50 µm | reliability class | flex substrate | review | §65.5.2.1, §66.2.2 | high |
| COOMBS-4230 | materials | Liquid (photoimageable) polyimide dielectrics reach 5 µm pitch with 10 µm vias (HDD suspensions); a 10 µm liquid-PI coverlay is sufficient for HDI flex; final cure > 300°C; cost 5–10× epoxy PIC; some inks stored < 0°C. | 5 µm pitch / 10 µm via; cure > 300°C | — | ultra-HDI flex | review | §65.5.2.3, §65.8.4.2 | high |
| COOMBS-4231 | materials | Kapton polyimide film: useful range −430 to 780°F (chars 1500°F); most data −195 to 200°C; tensile strength/modulus fall with T, elongation peaks 200–250°C; degrades hydrolytically (boiling water) and oxidatively (life = f(T, O2)); cut-through resistance to 12,000 psi (0.001 in film, ASTM D-876); shrinks on first heat exposure from residual stress — thermally pre-condition before precision processing; dimensional change also tracks RH. | see values | film gauge, T, RH | flex design | review | §65.5.2.4, Figs. 65.4–65.16, Tables 65.10–65.16 (not in text) | high |
| COOMBS-4232 | fab | Dry PI film/laminates before lamination and any high-temperature step (absorbed moisture → blisters, delamination; severe lamination can embrittle Kapton); flex circuits should ship moisture-sealed with desiccant and be baked before soldering. | — | RH exposure history | flex fabrication/assembly | review | §65.5.2.4, §67.8, Table 65.17 (not in text) | high |
| COOMBS-4233 | materials | PET (Mylar) film: dielectric strength ≈ 700 V/mil (0.001 in), tensile 23,000 psi, service −60 to 150°C but performance drops above 70°C; not solderable (special processes only), flammable (UL94 hard to meet), low moisture, low cost; Type A general-purpose to 0.014 in; Type HS shrinks 30% at 100°C. | 700 V/mil; 23 ksi; ≤ 70°C for full performance | — | non-soldered large flex (panels, printer cables) | review | §65.5.3, Table 65.18 (not in text) | high |
| COOMBS-4234 | materials | Thin glass-epoxy (< 200 µm) can serve as low-cost flex with rigid-board processes and soldering, but is not usable for repeated flexing. | thickness < 200 µm | bend cycles | flex-to-install only | review | §65.5.4 | high |
| COOMBS-4235 | materials | Flex copper: RA foil for dynamic flexing (12 µm RA standard; < 10 µm available); HD-ED foil as cheaper mid-class alternative; low-profile 12 µm ED for fine lines; ultrathin 3–5 µm by etch-down of 12 µm RA or 1–5 µm ED on carrier; < 5 µm needed for semi-additive 10 µm traces; sputter/plate gives < 5 µm conductors and < 10 µm pitch. | — | trace pitch, flex duty | conductor selection | review | §65.6, Table 65.20 (not in text) | high |
| COOMBS-4236 | materials | Adhesive-based (acrylic/epoxy) laminates and film coverlays limit heat resistance (Pb-free soldering, wire bonding) and often carry brominated flame retardants; adhesiveless laminates solve both (RoHS/halogen) — specify adhesiveless for Pb-free/wire-bond flex. | — | assembly process | flex laminate selection | review | §65.7.1, §65.11 | high |
| COOMBS-4237 | materials | Adhesiveless laminate types: cast (best cost/performance, high bond, substrate down to 12 µm, Cu up to 70/105 µm, double-sided needs > 300°C process); sputter/plate (seed < 100 nm, conductors 0.1–1 µm to < 10 µm, pinholes, lowest bond strength); thermoplastic-PI lamination (> 330°C lamination, > 350°C press; wide conductor choice incl. stainless/Cu alloy). | see values | thickness needs | HDI flex laminate | review | §65.7.2, Table 65.22, Fig. 65.26 (not in text) | high |
| COOMBS-4238 | materials | Coverlay selection: film coverlay (adhesive, refrigerate, weeks of pot life, manual registration) = best dynamic-flex endurance; screen-printed flexible mask = low cost, poor resolution, not for dynamic flexing (rigid-board solder mask cracks on bending); photoimageable coverlay (dry film or liquid; epoxy-liquid best cost/performance for volume, survives several bends but not long-term flexing; PI-based for dynamic flexing, > 250–300°C bake). | — | opening size, flex duty | coverlay | review | §65.8, §66.2.3, Tables 65.23–65.28 (not in text) | high |
| COOMBS-4239 | mechanical | Stiffeners: paper-phenolic/FR-4 for thick, PI/PET film for thin, Al/stainless plates (formable) for metal; paper-phenolic and PET cannot take thermosetting adhesives; PSA is low-cost but creeps under sustained stress (stiffener position drifts) — use thermoset adhesive where position/reliability matters. | — | load, temperature | flex stiffeners | review | §65.9–65.10, Tables 65.29–65.30 (not in text) | high |
| COOMBS-4240 | cost | Do not force all 3-D wiring into one complex flex; splitting into two or more simple circuits (with connections) is often cheaper; small design changes materially change flex cost — iterate with the fabricator. | — | — | flex architecture | review | §66.1 | high |
| COOMBS-4241 | materials | Flex copper thickness: 18 and 35 µm standard; 12 and 9 µm the new standard for fine-line etching; thinner foils only via sputtered/plated adhesiveless laminates; fine-line capability depends on the fabricator (exposure/etch). | 9/12/18/35 µm | trace pitch | flex design | review | §66.2.2, Fig. 66.4 (graph) | high |
| COOMBS-4242 | fab | Coverlay opening capability: film coverlay pre-punched (coarse); laser-drilled film openings < 100 µm (costly); screen print slightly better than punching; photoimageable coverlay finer than 200 µm pitch; practical hybrid = film coverlay in flexing areas + solder mask in SMT areas (extra process, lower yield). | PIC < 200 µm pitch; laser < 100 µm | opening size | flex SMT areas | review | §66.2.3, Table 66.3 (not in text) | high |
| COOMBS-4243 | mechanical | Stiffener systems by purpose: connector insertion → PET + PSA sized to the connector thickness (no heat resistance needed); through-hole components → thick FR-4 on component side with thermoset adhesive (must survive soldering); SMT → thin PI film on the opposite side. | — | termination type | flex stiffeners | review | §66.2.4, Fig. 66.6 | high |
| COOMBS-4244 | via | Double-sided flex PTH: electroplated Cu is brittle — keep plating thin (≈15 µm gives sufficient through-hole reliability; ≈20 µm nominal panel plating; > 25 µm only for high-reliability) and exclude plating from dynamic-flex areas by masking (button plating); excimer laser microvias < 40 µm in 25 µm adhesiveless PI. | t_plate ≈ 15–20 µm; > 25 µm hi-rel | flex duty | flex PTH/microvia | review | §66.2.5, §67.2.4, Fig. 66.8 (graph) | high |
| COOMBS-4245 | stackup | Rigid-flex: flexible regions carry only 1–2 conductor layers; rigid regions cap the flex core with glass-epoxy/PI; > 30 layers feasible (aerospace) but cost ≫ rigid; raising density to cut layer count lowers cost. | 1–2 layers in flex region | layer count | rigid-flex | review | §66.3 | high |
| COOMBS-4246 | components | Flying leads (double-access bare conductors): thicker Cu for mechanical strength (thin foil = fragile, yield loss); soft Au over Ni for wire bonding/direct bonding; Pb-free replaces SnPb plating. | — | Cu thickness | flex terminations | review | §66.3.1, Fig. 66.11 (graph) | high |
| COOMBS-4247 | connectors | Flex microbump/dimple arrays: pitches down to 50 µm; pressed dimple arrays with hard Au (> 60 dimples) give > 1,000 reliable non-permanent matings (inkjet cartridge example). | pitch ≥ 50 µm; > 1000 matings | — | separable flex terminations | review | §66.3.2 | high |
| COOMBS-4248 | mechanical | Dynamic-flex construction rules: conductor at the neutral axis with symmetrical layers; RA Cu (HD-ED survives ≈ 1e6 cycles with proper radius/stack; RA reaches 1e9); thinner is better — 18 µm Cu > 35 µm, 12.5 µm PI > 25 µm; adhesive as thin as bond strength allows; PI > PET; best = thin adhesiveless PI laminate + liquid PI coverlay; larger bend radius → longer life (IPC-TM-650 flex test, Fig. 66.18 graph). | symmetric stack; RA Cu; min thickness; max radius | stack-up, radius | dynamic flexing | review | §66.4, Figs. 66.15–66.18 | high |
| COOMBS-4249 | mechanical | Double-sided flex with through-holes is not for dynamic flexing: the dynamic area must have only one conductor layer, coverlay removed on the other side (symmetry), plating masked out; keep thin traces off the outside of the bend; prefer staggered/meshed/separated shield patterns per Fig. 66.20. | 1 conductor layer in dynamic zone | layout | dynamic flexing | inspect | §66.4, Fig. 66.20 | high |
| COOMBS-4250 | reliability | Flex insulation-resistance test: 100 V applied between conductors/layers after humidity–temperature conditioning, measured immediately; cover-coated flex retains high IR under severe humidity; bare flex only if clean (no flux/fingerprints). | 100 V test bias | — | flex IR qualification | measure | §66.5.1, Table 66.5 (not in text) | high |
| COOMBS-4251 | emc | Flex dielectric withstanding: flashover in air above conductors falls with altitude (air ionization) — increase conductor spacing for high-altitude use; use Figs. 66.21–66.22 (graphs) as design guide. | spacing ↑ with altitude | altitude, spacing | flex conductor spacing | review | §66.5.2 | medium (graph) |
| COOMBS-4252 | current-carrying | Flex conductor sizing inputs: current capacity, resistance, allowable temperature rise, derating for multiple conductors, mounting effects, fusing current, capacitance. | — | listed | flex conductor width | calc | §66.5.3 | high |
| COOMBS-4253 | crosstalk | Flex adjacent-conductor capacitance is fringing-dominated (about half the fringe field in air); grounded guard conductors on both sides cut C by ≈ 20%, an interspersed grounded guard plus peripheral guards by ≈ 85%; floating guards slightly increase C; scale reference values by dielectric-constant ratio. | guard: −20%; interspersed guard: −85% | guard layout | flex cables | calc | §66.5.4, Figs. 66.24–66.25, Table 66.6 (not in text) | high |
| COOMBS-4254 | transmission-line | Covercoated/embedded flex microstrip: Z0 ≈ 22% lower than air-exposed microstrip; epoxy-glass εr drifts ≈ 6 at 1 kHz → 5 at 25 MHz; treat > 50 MHz as transmission line; strip-line effective wire diameter d0 = 0.567·w + 0.67·t (2 oz: t = 0.0028 in); Z0 = sqrt(L/C) lossless. | Z0_embedded ≈ 0.78·Z0_microstrip | w, h/b, t, εr | flex controlled impedance | calc | §66.6.1–66.6.2 (microstrip/stripline formula bodies missing in text) | high |
| COOMBS-4255 | transmission-line | Strip-line design example (Fig. 66.34 curves): Z0 = 75 Ω, Teflon εr = 2.1, overall 0.062 in → normalized curve "110" (consistent with sqrt(εr)·Z0 ≈ 109), b = 0.050 in, w = 0.017 in. | — | — | flex strip-line sizing | calc | §66.6.2 | medium (graph) |
| COOMBS-4256 | transmission-line | Flex differential options for bend regions: edge-coupled microstrip over mesh ground (keep mesh symmetric under the pair — asymmetric spacing unbalances the E-field), coplanar differential without opposing ground (widened coplanar reference), broadside-coupled with offset ground and layer-swapped P/N (twisted-pair-like; impedance set by offset distance d). | — | mesh symmetry, offset d | high-speed flex | sim | §66.6.3, Figs. 66.36–66.38 | high |
| COOMBS-4257 | crosstalk | Reference capacitances: parallel lines spaced 0.062 in on 0.062 in epoxy-glass (εr = 5) ≈ 0.5 pF/in; Teflon ≈ 0.3 pF/in. | 0.5 pF/in (εr 5); 0.3 pF/in (PTFE) | — | flex/rigid cabling | calc | §66.6.4 | high |
| COOMBS-4258 | timing | Embedding a microstrip (multilayer) slows propagation: to keep the same delay, reduce critical embedded lengths by 22% (L_embedded = 0.78·L_unembedded); Td ∝ sqrt(εr_eff) (valid when line C > load C). | L_emb = 0.78·L_unemb | εr_eff, L | timing budgets | calc | §66.6.4.1, Fig. 66.40 (εr 4.5 graph) | high |
| COOMBS-4259 | crosstalk | Flex microstrip crosstalk: backward constant KB > 0, forward KF < 0 (zero in homogeneous dielectric); determine constants with lines where 2·Td > rise time; empirical curves valid for 0.0075 < W < 0.025 in, 2 oz Cu, Td = 1.8 ns/ft, lines terminated in Z0; VF(t) = KF·l·dV0/dt. | Td = 1.8 ns/ft reference | spacing, W, l | flex cables | calc | §66.6.4.2, Figs. 66.41–66.42 (graphs) | medium |
| COOMBS-4260 | transmission-line | Shielded flex cable (0.025 × 0.0027 in conductors, 0.020 in spacing, 0.003 in polyester each side, Al shield) has higher attenuation than RG-55 coax over 1–3000 MHz because of its low impedance (conductor loss dominates at low Z0, dielectric loss at high Z0). | — | Z0, frequency | flex RF cabling | measure | §66.6.4.3, Fig. 66.43 (graph) | medium |
| COOMBS-4261 | dfm | Flex reliability pattern rules: smooth tapered width transitions, pads as large as possible, conductors as wide as spacing allows, tear-stop features, coverlay opening extends past pad with minimal adhesive squeeze-out, and stress relief/pattern rules at stiffener edges (stress concentration). | — | pattern geometry | flex layout | inspect | §66.7, Figs. 66.44–66.48 | high |
| COOMBS-4262 | fab | Flex hole formation: NC drilling stacks more flex sheets than rigid; drilled and punched holes < 100 µm possible; punching is RTR-compatible but cannot make blind vias; adhesiveless laminates give clean PTH walls without desmear. | < 100 µm holes | volume, via type | flex fabrication | review | §67.2.3–67.2.4 | high |
| COOMBS-4263 | fab | Flex fine-line imaging: 15–20 µm dry film → 30–40 µm lines/spaces on 12 µm Cu; liquid resist for < 40 µm pitch; glass phototool and ±10 µm top/bottom alignment for < 50 µm pitch; LDI corrects random film distortion but is weaker below 25 µm L/S; per-lot mask compensation or smaller panels may be needed. | ±10 µm alignment @ < 50 µm pitch | pitch | HDI flex | review | §67.3.2–67.3.3 | high |
| COOMBS-4264 | fab | Etch chemistry for flex: cupric chloride preferred; ferric chloride stains; ammoniacal alkaline is fast but can attack polyimide and undercut fine lines; characterize etch factor (edge vs middle conductors differ), add non-functional copper beside fine features, taper traces to maximize copper area for dimensional stability. | — | Cu thickness, pitch | fine-line flex | review | §67.3.4 | high |
| COOMBS-4265 | fab | Coverlay process limits: film coverlay manual registration ≈ 50–75 µm; openings < 200 µm diameter needing ±100 µm placement require photoimageable coverlay; film-coverlay press cure ≈ 1.5 h (quick-press < 2 min + oven cure alternative); PIC: 15–30 min hold after lamination, develop in 1% Na2CO3, bake ≈ 150°C for ≈ 30 min. | < 200 µm opening → PIC | opening size | flex coverlay | review | §67.4.1–67.4.3 | high |
| COOMBS-4266 | fab | Laser coverlay openings: excimer gives ≤ 50 µm clean openings (slow); CO2/YAG an order of magnitude faster but leave char needing cleaning; examples 100 µm (excimer) and 200 µm (CO2). | excimer ≤ 50 µm | opening size, volume | flex prototypes/small volume | review | §67.4.4 | high |
| COOMBS-4267 | components | Flex termination finishes: soft Au (over Ni) for wire bonding, hard Au for separable contacts, ENIG through coverlay openings (high-pH chemistries can attack film/adhesive — use vendor-proven baths, remove residues first), OSP for solderability with shelf-life limits, HASL hard to level uniformly on flex. | — | termination type | flex finishes | review | §67.5, Table 67.3 (not in text) | high |
| COOMBS-4268 | fab | Depanelization: steel-rule dies (fast tooling, lower accuracy/life) vs Class A dies; CCD-located tooling holes punched to ±50 µm (can be punched after coverlay for outline alignment); provide strain relief at every rigid-to-flex transition in high-reliability designs. | tooling holes ±50 µm | — | flex outline & stiffeners | inspect | §67.6–67.7, Table 67.4 (not in text) | high |
| COOMBS-4269 | fab | High-density flex = features < 100 µm (leading edge ≈ 20 µm); thinner base copper is the first requirement (isotropic etch → trapezoidal traces); semi-additive plating for fine lines with high current (example 10 µm wide × 25 µm thick); button (holes-only) plating keeps base Cu thin except at PTHs. | < 100 µm = HDI flex | feature size, current | HDI flex | review | §67.9.1, Figs. 67.17–67.21 | high |
| COOMBS-4270 | via | Flex microvia (< 100 µm) methods: mechanical drill down to 50 µm in 50 µm laminate (low stack height); micro-punch 70 and 25 µm films at high rate; excimer laser finest (≤ 50 µm), CO2 fastest above 60 µm (needs Cu oxide treatment to drill Cu), UV-YAG drills Cu + polymer; chemical (hot caustic, polyimide only) and plasma (CF4/O2/N2) etch ≈ 100 µm holes in 50 µm film through a conformal Cu mask, unlimited holes per batch but undercut the top foil. | see values | via dia, volume | HDI flex | review | §67.9.2–67.9.5, Tables 67.7–67.9 (not in text) | high |
| COOMBS-4271 | connectors | First termination decision for every flex interface: permanent (solder, wire bond, conductive adhesive, weld, interference/IDC), separable (connector, or flex as one half of a mated pair) or intermittent (membrane switch). | — | interface list | flex terminations | review | §68.1.1, Table 68.1 (not in text) | high |
| COOMBS-4272 | assembly | Lap / hot-bar soldering of flex to a rigid board: strain-relieve the flex at the joint. | — | — | flex-to-board solder joints | inspect | §68.1.2, Fig. 68.1 | high |
| COOMBS-4273 | assembly | Wire bonding to flex terminations needs Ni/Au; ultrasonic Al wedge bonding (room temperature) needs only a very thin Au flash (thicker Au → Kirkendall voiding); thermosonic Au bonding needs thicker Au for a reliable Au–Au bond. | wedge: thin Au flash; thermosonic: thick Au | bond type, Au thickness | COB / chip-on-flex | review | §68.2 | high |
| COOMBS-4274 | assembly | Conductive adhesives: isotropic (Ag powder in epoxy; conductivity below solder; cure shrinkage densifies particles; stencil or dispense; coarser pitch) vs anisotropic (Z-axis only, dispersed particles; liquid or film; redundant contacts; fine pitch; display-driver attach). | ICA → coarse pitch; ACA/ACF → fine pitch | pitch | adhesive interconnect | review | §68.2.1–68.2.3, Fig. 68.3, Table 68.2 (not in text) | high |
| COOMBS-4275 | connectors | Metal-to-metal permanent joints on flex: insulation-piercing contacts crimped around conductors (flex analog of gas-tight press-fit); resistance welding (mostly repair, coarse pitch); ultrasonic TAB-style lead bonding — keep leads attached across the window until bonding and add an etched or embossed notch at the intended break point. | — | — | flex permanent joints | review | §68.2.4, Fig. 68.4 | high |
| COOMBS-4276 | connectors | Flex as half of a mated pair: the thin film creeps under contact pressure, so the mating spring must keep enough resilience to hold force as the film creeps; finish contacts with Ni/Au or raised bumps (embossed from the back with a mating die, or plated); embossed-bump lands must be large enough to avoid Cu fracture. | — | contact force, land size | separable flex contacts | review | §68.3, Fig. 68.5 | high |
| COOMBS-4277 | connectors | Edge-card insertion of flex: bond to a stiffener sized to the connector thickness and bevel the lead-in (single-sided: wrap the flex around the stiffener edge; two flexes: bond them to each other to form a nib); use ZIF latch connectors for bare thin flex (force insertion is impractical). | stiffened thickness = connector spec | connector thickness | flex-to-connector | inspect | §68.3.1–68.3.2, Figs. 68.6–68.7 | high |
| COOMBS-4278 | connectors | Flex connector pitch options: SMT mated-pair board-to-flex ≥ 0.5 mm (0.2 mm in advanced designs); zebra-strip elastomeric 200 µm linear pitch but relatively high contact resistance — not for high current; circular military/bulkhead connectors for sealed boxes. | SMT mated pair ≥ 0.2–0.5 mm; zebra 200 µm | pitch, current | flex connectors | review | §68.3.4–68.3.6 | high |
| COOMBS-4279 | connectors | Membrane-switch (intermittent-contact) flex runs relatively high voltage, low current and can use polymer thick-film (silver ink) conductors. | — | V, I | keyboards/switches | review | §68.3.7 | high |
| COOMBS-4280 | stackup | Before choosing rigid-flex, check whether a single/double/multilayer flex with a post-attached stiffener meets the need — typically much more cost-effective; rigid-flex rarely carries direct chip attach (wire bond/flip chip). | — | — | flex architecture | review | §69.2.1 | high |
| COOMBS-4281 | reliability | Rigid-flex rigid sections: replace unreinforced flexible bond ply (high z-CTE, cracked PTH barrels/corners in thermal excursions) with glass-reinforced prepreg; minimize high-CTE adhesive in the PTH region; prefer adhesiveless flex cores (adhesives expand far more than base films). | — | stack-up | rigid-flex PTH | review | §69.2.1–69.2.2, Fig. 69.3 | high |
| COOMBS-4282 | mechanical | Stiffness scales with thickness³ — leave air gaps (unbonded) between flex layers in bend zones. | stiffness ∝ t³ | layer bonding in bend zone | rigid-flex | review | §69.2.1, Fig. 69.4 | high |
| COOMBS-4283 | mechanical | Bookbinder construction for bends with several flex layers: lengthen each successive layer through the bend by nominally 250 µm; hold the bowed shape with tooling and relieve the lamination plates. | L_i = L_1 + 0.25 mm·(i − 1) | layer order i | multi-flex-layer bends | calc | §69.2.1, Figs. 69.6–69.7 | high |
| COOMBS-4284 | materials | Rigid-flex materials: inner flex polyimide ≥ 50 µm (thicker preferred for dimensional stability); acrylic common for coverlay/bond ply but smears when drilled; polyimide adhesives have higher heat resistance; hot-melt PI adhesive systems cut smear but laminate > 300°C; epoxy-glass or PI-glass prepreg controls z-expansion; all must survive Pb-free soldering. | PI ≥ 50 µm | stack-up | rigid-flex | review | §69.2.2, Table 69.1 (not in text) | high |
| COOMBS-4285 | fab | Rigid-flex process controls: plate layer-1/2 vias before coverlay; machine windows in the bond material so flex does not bond to rigid caps; cavity spacers for planarity (removed at routing); one tooling system for all layers; vacuum autoclave lamination preferred; vent holes against entrapped air, sealed (e.g. epoxy dot) before wet steps and considered again for plasma; drill study for unusual material sets or high layer count; plasma desmear preferred (acrylic smear); permanganate only with controlled dwell (resin swelling); hole-wall wetting step is critical for mixed PI/epoxy-glass/acrylic walls; agree the rigid-to-flex transition routing with the fabricator. | — | — | rigid-flex fabrication | review | §69.2.3, Fig. 69.8 | high |
| COOMBS-4286 | materials | Prospective aluminum-core rigid-flex ("SAFE"/Occam: tested parts embedded in cavities, no solder): Al CTE 22 vs Cu 18 ppm/°C (text values) vs reinforced laminate x ≈ 20, y ≈ 23, z ≈ 80 ppm/°C; Al 2.8 vs FR-4 1.8 g/cm³; cavity depth = component height; anodize/coating shrinks cavities (characterize); seal untreated Al edges before wet processing; etch Al with NaOH + sodium gluconate or ferric chloride; claimed 25–35% lower cost excluding components. | see values | — | prospective construction | review | §69.3 | low (author claims, prospective) |
| COOMBS-4287 | assembly | Author states assembly yields drop appreciably below 0.5 mm lead pitch — flag sub-0.5 mm pitch parts in yield planning. | pitch < 0.5 mm → yield risk | pitch | SMT | review | §69.3.3 | medium |
| COOMBS-4288 | fab | Flying-lead windows by pre-punching: openings < 1.0 mm are hard to hold with accuracy/yield (unstable punched film, adhesive squeeze-out) — use laser, plasma or chemical window formation for smaller features. | punched window ≥ 1.0 mm | window size | flying leads/TAB | review | §70.2.2 | high |
| COOMBS-4289 | fab | Laser window formation on flex (text prints "mm" where µm is meant): excimer slits < 50 µm, clean edges, carbon residue needs wet clean, slow → costly for large areas; UV:YAG cuts Cu and organics, best for very small openings, impractical above ≈ 10,000 µm² per opening; CO2 (TEA/diamond) most productive above 70 µm, poorer edges, needs plasma clean, Cu mask helps; CO2 heat — control power density for 18 µm Cu flying leads < 100 µm wide. | excimer < 50 µm; CO2 > 70 µm | opening size | flying leads | review | §70.2.3 | medium (unit rendering) |
| COOMBS-4290 | fab | Plasma window etch: sidewall slope 30–60°, hard below 100 µm holes in 50 µm PI; vacuum batch, unlimited openings, uniformity limited by chamber. Chemical (NaOH/KOH on Kapton-type PI): < 100 µm openings in 25 µm film with small slope; Upilex-type PI needs aggressive chemistry; RTR-friendly, no special capital. | plasma ≥ 100 µm @ 50 µm PI; chemical < 100 µm @ 25 µm | film type, thickness | flying leads | review | §70.2.4 | high |
| COOMBS-4291 | cost | Flying-lead window cost model (25 µm PI, 300 mm² working size as printed, 0.1 × 3 mm openings, 150 µm lead pitch, 18 µm Cu): plasma/chemical cost ≈ independent of number/size of openings (batch); laser cost ∝ ablated area; CO2 cheaper than excimer for larger openings despite residue cleaning. | — | opening area, count | process selection | calc | §70.2.5, Fig. 70.7 (graph) | medium |
| COOMBS-4292 | fab | TAB: 35 mm web standard, 70 and 155 mm available, sprocket-hole RTR in clean rooms; ≈ 40 µm lead pitch is the practical limit for flying leads — use COF (no device hole or flying leads) below 40 µm pitch. | flying-lead pitch ≥ 40 µm | pitch | TAB/COF | review | §70.3 | high |
| COOMBS-4293 | components | Flex microbump arrays: best 100–150 µm pitch on 50 µm dielectric; shape set by dielectric thickness and opening size (high opening aspect ratio → spherical, low → flat disc; plating mask for tall straight bumps); solder print/dispense + reflow for large balls, electroplating (Cu/Ni/Au/solder) for small or non-spherical bumps; laser for small exact holes through the dielectric, plasma/chemical for many low-cost holes. | pitch 100–150 µm on 50 µm dielectric | opening AR | bumped flex | review | §70.4 | high |
| COOMBS-4294 | materials | Polymer-thick-film flex (Ag paste in acrylic on PET): lowest cost for large circuits (membrane switches, keyboards, touch panels) but conductivity far below Cu foil — not for power or high-speed signal layers; not solderable (acrylic binder); Cu or carbon pastes are low-conductivity/unstable; pre-bake PET to remove shrinkage before printing; fine print 10–15 (unit printed "mm", likely µm). | — | current, speed | PTF flex | review | §70.5 | medium |
| COOMBS-4295 | emc | Flex cable shielding: screen-printed Ag paste (high shielding, flexible), carbon paste (low cost, limited shielding), thin Al foil laminated with thin flexible adhesive (reliable shielding and flexibility). | — | shielding need, flex duty | high-speed flex cables | review | §70.6, Fig. 70.14 | high |
| COOMBS-4296 | components | Functional flex: sputtered NiCr can form embedded resistors and strain gauges directly on flex. | — | — | functional flex | review | §70.7, Fig. 70.15, Table 70.2 (not in text) | high |
| COOMBS-4297 | reliability | Pb-free raises assembly temperature from ≈230°C (SnPb) to as high as 260°C and adds failure modes (e.g. microvia pull-out) — requalify flex designs made for SnPb. | 230 → 260°C | assembly alloy | flex QA | review | §71.1 | high |
| COOMBS-4298 | materials | Flex raw-material tests: initiation and propagation tear strength (low propagation tear → add tear-stop features), low-temperature flexibility, dimensional stability (shrink after Cu etch), peel strength (as received; after 289°C solder float 10 s; after 5 cycles −50/+150°C with 30 min dwells and 15 min at room temperature between extremes), volatile content. | see conditions | — | flex laminate incoming QA | measure | §71.3.1 | high |
| COOMBS-4299 | materials | Flex dielectric electrical tests: Dk (ratio to air capacitance), Df (rises with moisture), dielectric strength (critical for high-voltage and high-altitude arcing), surface and volume resistivity under damp heat. | — | — | flex laminate QA | measure | §71.4 | high |
| COOMBS-4300 | materials | Moisture: vapor pressure roughly doubles between SnPb and Pb-free soldering temperatures — control absorbed moisture (bake/dry-pack) to avoid explosive outgassing and coverlayer delamination; also run M&IR and fungus-resistance tests. | vapor pressure ≈ 2× (Pb-free vs SnPb) | moisture content | flex assembly | review | §71.4.1 | high |
| COOMBS-4301 | compliance | Flex flammability: UL 94 V-0 commonly required (now achievable with flex laminates); UL 796F covers flexible interconnect constructions. | UL 94 V-0 | material listing | flex compliance | review | §71.5, §71.12 | high |
| COOMBS-4302 | fab | Flex visual acceptance: delamination nearly always rejectable; edge nicks/tears rejectable (tear initiation, esp. dynamic flex); verify stiffener bond and fillet; solder wicking under coverlayer only within agreed limits; PTH ring voids rejectable (they cause blow holes). | — | — | flex lot acceptance | inspect | §71.6 | high |
| COOMBS-4303 | fab | Single-sided flex coverlayer must capture the land to prevent pad lift: "minimum of 270 percent of land capture" as printed (likely 270° of land perimeter). | capture ≥ 270 (unit as printed) | coverlay opening vs land | single-sided flex | inspect | §71.7 | medium |
| COOMBS-4304 | fab | Flex conductor/coverlay defects: localized width reduction from nicks/mouse bites ≤ 20% (many occurrences = process problem); soda-strawing and foreign inclusions accepted per agreed limits if not bridging/reducing spacing and not in critical bend areas; adhesive squeeze-out onto pads per standard allowances (photoimageable coverlayer avoids it). | Δw ≤ 20% | measured width | flex lot acceptance | inspect | §71.7 | high |
| COOMBS-4305 | reliability | Flex physical tests: plating adhesion tape test; unsupported (NPTH) land must survive 5 solder/desolder cycles; folding flexibility per drawing (location, radius, angle, direction, cycles); flex endurance by Engelmaier fatigue-ductility tester, rolling-flex, MIT flex or collapsing-radius tests (weeks–months for disk-drive duty). | NPTH land: 5 cycles | — | flex qualification | measure | §71.8–71.8.1, Fig. 71.1 | high |
| COOMBS-4306 | reliability | Flex construction integrity: microsection before and after thermal stress (289°C / 550°F solder float, oven reflow simulation, or IST); rework simulation = solder/desolder a component lead 5× in a PTH by a skilled operator; excess lifted lands after stress → redesign with lower-CTE materials. | float 289°C; rework 5× | — | flex/rigid-flex qualification | measure | §71.8.2–71.8.4 | high |
| COOMBS-4307 | test | Flex electrical acceptance: 100% continuity/isolation to the drawing (test voltage, minimum isolation resistance), fixture or flying probe; IR after processing; CAF on rigid-flex glass hybrids at 65°C / 85% RH isothermal (no cycling); TDR on controlled-impedance flex. | CAF 65°C/85% RH | — | flex acceptance | measure | §71.9 | high |
| COOMBS-4308 | reliability | Flex environmental tests: M&IR cycling 80% RH/25°C ↔ 98% RH/65°C; thermal cycling −65 to +150°C with 10 min–1 h dwells (shock uses short dwells); common bare-board cycling −55 to +125°C. | see conditions | — | flex qualification | measure | §71.10 | high |
| COOMBS-4309 | process | Flex cleanliness: ionic by solvent-extract resistivity (alcohol/water wash); organic residue by acetonitrile flush dried on a clean glass slide. | — | — | flex acceptance | measure | §71.10 | high |
| COOMBS-4310 | process | Split flex testing into qualification (full set) and lot acceptance (limited set); SPC on the process reduces formal inspection (ISO 9000 basis). | — | — | flex QA plan | review | §71.13 | high |
| COOMBS-4311 | materials | Kirkendall voiding (Cu–Au, Cu–Au–Sn): Cu diffuses into Au by grain-boundary diffusion below 150°C and bulk diffusion above; vacancies coalesce into voids that weaken the joint — keep Au thin at solder and wedge-bond sites. | regime change at 150°C | Au thickness, T | Au finishes | review | Glossary; §68.2 | medium (glossary garbled) |
| COOMBS-4312 | fab | Etch factor = etch depth / lateral etch; characterize per chemistry and Cu thickness and feed back to artwork compensation. | EF = depth / lateral | Cu thickness | fine-line etching | calc | Glossary; §67.3.4 | high |
| COOMBS-4313 | materials | Laminate mechanical metrics: flexural modulus from 3-point bend E_B = L³·m/(4·b·d³) (L span, m initial load–deflection slope, b width, d depth); heat-distortion point = temperature at which an ASTM D648 bar deflects 0.010 in under 66 or 264 psi. | E_B = L³m/(4bd³) | L, m, b, d | board modulus input to joint models | calc | Glossary | high |
| COOMBS-4314 | test | Tester selection: in-circuit / combinational testers where fault coverage and diagnostic resolution matter (most manufacturers); MDA (unpowered, low cost) where coverage/resolution can be traded for fast programming in low-cost high-volume product; functional/specification testers only when a contract or regulation requires them. | — | product class | test strategy | review | §57.7, Table 57.2 (not in text) | high |
| COOMBS-4315 | test | Boundary scan (1149.1) can replace many bed-of-nails points (board test prepared in ≈ 1 day vs weeks) and pinpoints opens that ICT would blame on the IC, but not all access points can go — keep nails where required. | test development ≈ 1 day | scan coverage | DFT | review | §56.5.1 | high |
| COOMBS-4316 | test | Place pre-reflow AOI after passive placement and before area-array/leaded placement so it can still see BGA/CSP/fine-pitch QFP paste deposits. | — | line layout | SMT line design | review | §55.9.2 | high |
| COOMBS-4317 | reliability | Galvanic corrosion needs moisture (bias only accelerates with correct polarity); a small anode against a large cathode corrodes rapidly; a large anode with a small electronegativity difference is unlikely to be serious — check dissimilar-metal pairs by area ratio. | A_anode ≪ A_cathode → high risk | metal pair, areas | mixed-metal finishes | review | §60.3.2 | high |
| COOMBS-4318 | solder | Bake hygroscopic laminates (polyimide, aramid) before reflow to prevent solder-mask and resin/reinforcement delamination; never apply solder mask over solder. | bake before reflow | laminate type | PI/aramid boards | review | §60.3.4.5 | high |
| COOMBS-4319 | process | Use FTA (top-down) only for serious system-level modes (safety, permanent damage) and FMEA (bottom-up) at component/module level; use both where possible; FTA needs a well-defined system, one tree per system failure mode. | — | — | reliability analysis | review | §58.1.2.2 | high |

## 2. Formulas & tables (numbers)

Source tables in these chapters are images and are absent from the text; the tables below are compiled from values stated in the prose. Units as printed; "(µm)" marks places where the extraction rendered µ as "m".

### 2.1 Automated assembly inspection benchmarks (§55.8–55.10)

| System | Measures | Throughput | View / slice | Limits | Source |
|---|---|---|---|---|---|
| 3-D SPI | paste height, area, volume (quantitative) | 2–22 cm²/s | view 10–25 mm dia; > 100 views per board | no placement/reflow defects | §55.8 |
| Pre-reflow 2-D AOI | placement offset, missing parts, 2-D paste | 10–40 cm²/s (2–3× SPI) | larger views; 0402/0201/01005 need SPI-like magnification | no reflow defects, no 3-D paste | §55.9 |
| Post-reflow AOI | attribute: bridges, no solder, toe fillet, misalignment | 10–40 cm²/s | small views | no hidden joints; false calls ≤ 0.5 mm pitch and SOT; shadowing by tall parts | §55.10.1 |
| Transmission x-ray | grayscale fillet features, voids | 50–150 joints/s | — | single-sided only; no PTH/BGA bottom | §55.10.2, §55.10.4 |
| Cross-sectional x-ray | calibrated thickness, fillet heights, void volume | 50–150 joints/s | focal slice 0.2–0.4 mm | price ≈ 1.5–2× fastest optical | §55.10.3–55.10.4 |

### 2.2 Thermal stress / cycling profiles (PCB, PTH, microvia, flex)

| Test | Range | Ramp / dwell / count | Failure criterion or result | Source |
|---|---|---|---|---|
| Solder float (MIL-P-55110 / IPC-TM-650) | 288°C (SnPb), ≥ 260°C (Pb-free), 10 s | bake 120–150°C first; RMA flux | microsection cracks | §60.2.6.1 |
| Flex thermal stress | 289°C (550°F) solder float | — | microsection | §71.8.4 |
| Thermal-shock oven, air-air | −40/+145°C | 25–35°C/min, 20 s dwells | cycles to failure | §60.2.7.1 |
| IST (IPC-TM-650 2.6.26) | RT → 150°C typical | DC self-heating | +10% resistance | §60.2.7.2 |
| IST, microvia | RT → 190°C after 5× 230°C | — | compromised via < 500 cycles | §60.2.7.4, §61.1.5 |
| HATS | −55/+160°C (data at −55/+145°C) | 25–50°C/min; 4 nets/coupon, ≤ 36 coupons | +10% resistance | §60.2.7.3 |
| PCQR2 correlation | −40/+145°C (185°C span) | — | +10% resistance | §60.2.7.4 |
| Pb-free consortium, AtA | −40/+135°C after 6× 260°C | 10 min ramps and dwells; 3000 (→ 6000) cycles | — | §60.4.6 |
| Pb-free consortium, IST | 23 → 150°C | 3 min heat, 2 min cool, no dwell | — | §60.4.6 |
| Goyal cond. B / C | −55/125°C; −65/150°C | 1000 cycles | unfilled PTH: B 1/3/24/59% at 100/200/500/1000; C 10/82/100% at 200/500/1000 | §60.4.2 |
| Park | −55/125°C; −35/125°C | — | B10 606 / 1065 cycles | §60.4.3 |
| Wu (IPC-9701) | 0/100°C | 10°C/min, 6000 cycles | no failure for dia > 18 mil or AR < 5.3 | §60.4.5 |
| Microvia–PTH proximity (LLTS) | −55/125°C | 10 s transfer | first failure 1100 cycles | §61.1.5 |
| ALIVH handset board | −25/125°C shock | 500 shocks | pass | §61.1.5 |
| Corner crack (Fehrer) | 240°C hot oil → RT forced air | — | FR-4 ≈ 10 cycles; cyanate ester ≈ 50 | §60.4.4 |
| IPC-9701 TC1 / TC4 | 0/100°C; −55/125°C | 10 min dwell (30 min optional Pb-free); NTC 200–6000 | — | §60.4.7, §64.2.1.1 |
| Example ATC profile | −40/+100°C | 60 min cycle | — | §64.2.1, Fig. 64.3 |
| Thermal shock definition | — | ramp > 20°C/min | — | §61.1.5 |
| Flex thermal cycling | −65/+150°C | dwells 10 min – 1 h | — | §71.10 |
| Bare-board cycling (common) | −55/+125°C | short dwells for shock | — | §71.10 |
| Flex peel after cycling | 5 cycles −50/+150°C | 30 min dwells, 15 min RT between | peel retained | §71.3.1 |

### 2.3 Temperature–humidity–bias tests

| Test | Conditions | Pass / result | Source |
|---|---|---|---|
| IPC-SM-840A M&IR, Class 2 | 50°C, 90% RH, 100 VDC, 7 d | IR ≥ 1e8 Ω | §60.2.6.3 |
| MIL-P-55110 M&IR | MIL-STD-202 Method 106 with 100 VDC; Method 402 cond. A | — | §60.2.6.3 |
| IPC-SM-840A electromigration | 85°C, 90% RH, 10 VDC, 1 mA limit, 7 d | no significant current change; no dendrites | §60.2.6.3 |
| Flux dendrite test | 85°C, 85% RH, 1000 h, −20 VDC | — | §60.2.6.3 |
| CAF, IPC-TM-650 2.6.25 (Sauter) | 65°C, 85% RH, 500 h; hole-to-hole 0.27/0.38/0.50/0.65 mm, in-line vs staggered | staggered more resistant | §59.6 |
| CAF, flex / rigid-flex | 65°C, 85% RH isothermal | — | §71.9 |
| Bromide CAF (Caputo) | reflow 240–245°C ×1–2; 85°C/85% RH, +200 V bias, +100 V test, 28 d | Cu2(OH)3Br found | §59.5.6 |
| Bell Labs flex vehicle | 85°C/80% RH/78 V | failures in 2–5 d | §59.4 |
| Raytheon punch-thru | 65°C/95% RH/100 V, 10 d | DC-only failure | §59.4 |
| WOA corrosion (modified Bono) | 85/85 (24 h equilibrate), 60°C/93% RH, 40°C/93% RH (40 h equilibrate); 20 d | 60/93 recommended; 10 d sufficient | §59.3 |
| Flex M&IR | cyclic 80% RH @ 25°C ↔ 98% RH @ 65°C | IR within limits | §71.10 |
| Flex IR | 100 V after humidity–temperature cycle | — | §66.5.1 |
| ALIVH humidity | 85°C/85% RH, 1000 h | pass | §61.1.5 |
| SIR measurement limit | > 1e12 Ω needs careful shielding | — | §60.2.6.3 |

### 2.4 CAF and electrochemical-migration data (Ch. 59)

| Item | Value | Source |
|---|---|---|
| CAF life scaling (hole-to-hole) | MTTF ∝ L⁴/V² (tested 0.50 & 0.75 mm, 150 & 200 V) | §59.4, Eq. 59.14 |
| Filament size | ≤ 50 µm diameter, ≈ 0.2 mm long | §59.4.1 |
| Chloride CAF | Cu2(OH)3Cl, insoluble below pH 4 | §59.4.1 |
| Bromide CAF | Cu2(OH)3Br, insoluble below pH 7; from 15 wt% Br flux (2 wt% Cl or Br → chloride CAF) | §59.5.6 |
| Laminate susceptibility | MC-2 > epoxy/Kevlar > FR-4 ≈ PI > G-10 > CEM-3 > CE > BT | §59.5.1 |
| Geometry susceptibility | hole-hole > hole-line > line-line | §59.5.1.1 |
| Min hole-wall spacing (telecom, 365 cycles/yr) | 0.65 mm → ≥ 20 yr with high-Tg dicy FR-4 | §59.7 |
| Resin content | DS 1.5 mm = 8 × 7628 (0.175 mm) → 30–40%; ML 0.035 mm glass → 55–65%; 0.10 mm glass → 45–50% | §59.7 |
| Bono coupon | Cu 9–10 µm, gap 2 mm, V2 = 12 V / R2 = 50 kΩ, V1 = 250 V / R1 = 5 kΩ | §59.3 |
| Turbini coupon | gap 0.5 mm (= IPC-B-24), Cu 8.6 µm, V1 = 50 V | §59.3 |
| Zhou system | resistors 200 Ω and 2 kΩ; anodic trace ≈ 5 Ω | §59.3 |
| WOA corrosivity | abietic < succinic < adipic ≈ glutaric < malic | §59.3 |
| Field failure | +20 V plane to −20 V pin, 0.005 in apart | §59.5.3 |

### 2.5 PTH / microvia fatigue model constants and life data (Ch. 60–61)

| Item | Value | Source |
|---|---|---|
| ED Cu (linearized) | Su = 40,000 psi; Sy = 25,000 psi; E_Cu = 12e6 psi; Df = 30%; εf ≈ 0.3 | Fig. 60.22, §60.4.1 |
| Strain-distribution factor | Kd ≈ 1.6 | §60.4.2 |
| Quality factor KQ | extraordinary 10, superior 8.7, good 6.7, marginal 4.8, poor 3.5 | §60.4.2 |
| Reference PTH model (Fig. 60.42) | 50 J/cm³ fracture energy; hole radius 0.45 mm; plating 0.02 mm; board 2 mm; hole-center to pad edge / free end 0.8 mm | Fig. 60.42 |
| Iannuzzelli example (0.0135 in hole, 1.0–1.5 mil plating, difunctional FR-4) | 7 assembly cycles use 41% barrel / 26% knee life; field 19,400 (barrel) / 8,780 (knee) cycles; knee fails ≈ 6,500 field cycles; 1 assembly cycle ≡ 1,175 (barrel) / 318 (knee) field cycles | §60.4.8 |
| IST RT/150°C material effect | low-Tg high-CTE ≈ 370 cycles; lowest-CTE ≈ 2,900 | §60.4.2 |
| Laminate across Tg (one FR-4) | α_z 28.9 → 128.7 ppm/°C (4.45×); DMA E 18,000 → 2,500 MPa (7.2×) | §60.4.3 |
| Park AF (field ΔT 80°C) | 49 (ΔT 180°C), 28 (ΔT 160°C) | §60.4.3 |
| Wu Weibull (shape, char. life) | 10 mil: 4.92, 3932; 12 mil: 5.70, 4439; 16 mil: 11.89, 5037; first failures 2518/1830/3985 | §60.4.5 |
| Extra Pb-free reflow (250°C, 2× → 3×) | HATS −55/145°C η 422 → 292–294 cycles | §60.4.6 |
| STII range studied | 181–247 | §60.4.6 |
| Microvia IST peak vs mean CTF (after 5× 230°C) | 150°C: 1000; 170: 789; 190: 464; 210: 76; 220: 44 | §61.1.5 |
| Pb-free preconditioning, marginal microvias | 788 (150°C IST) → 443 after 6× 230°C → 4 after 6× 260°C | §61.1.5 |
| FEA sensitivities | +20% board thickness → +8–30% barrel stress; Cu 12 → 38 µm → −25–70%; Ni 2.5 → 15 µm → −30–70%; solder fill → −20–70% | §60.4.2 |
| FEA −30/150°C | von Mises 229.0 MPa (150°C), 232.7 MPa (−30°C); residual 9613 µε | §60.4.2 |
| Stacked microvia offset | 37 → 30 kgf/mm² (≈ 53 → 43 ksi) | §61.1.6 |
| Microvia fatigue prediction (IPC-TR-579) | 2,607 cycles (−55/125°C), ≥ 1000 observed | §61.1.6 |
| Pb-free Cu dissolution | up to 12 µm (0.5 mil) | §60.4.6 |
| IPC barrel plating | ≥ 12 µm avg (Class 1); ≥ 25 µm (Class 2, 3) | §60.3.4.4 |
| Aspect ratio | > 3:1 good plating needed; > 5:1 not recommended | §60.3.4.4, §60.4.9 |

### 2.6 Board, laminate and package material data

| Item | Value | Source |
|---|---|---|
| FR-4 Tg | 125–170°C (§60.3); commercial 110–150°C (§63.6.1) | §60.3, §63.6.1 |
| Polyimide Tg | > 200°C | §60.3 |
| Measling / delamination onset, FR-4 | ≈ 260°C | §60.3.5.1, §61.1.5 |
| HDI test board (TMA) | x 12.83, y 14.62, z 43.21 ppm/°C; z 297.7 above Tg; Tg 146.71°C | §61.1.5 |
| FR-4 product boards (survey) | in-plane CTE 12–21 ppm/°C; E 10–30 GPa; x–y difference up to ≈ 5 (example 16 vs 21) | §63.6.1 |
| Board thickness series (Shih) | 62 mil: 15.9 ppm/°C, 26 GPa; 93 mil: 15.85, 23; 130 mil: 18.75, 30 | §63.6.2 |
| Components | CBGA 6; LCCC 5.4; CSP 8.6 ppm/°C; Alloy 42 ≈ 4; solder ≈ 24; Cu ≈ 17 (Ch. 63) / 18 (Ch. 69) | §63.3–63.4, §69.3.2.4 |
| Aluminum core | CTE 22 ppm/°C; 2.8 g/cm³ (FR-4 1.8) | §69.3 |
| Reinforced laminate (Ch. 69 example) | x ≈ 20, y ≈ 23, z ≈ 80 ppm/°C | §69.3.2.4 |
| AlSiC lid | k 180–200 W/(m·K) | §62.3.13.4 |
| Reinforcement CTE | E-glass > S-glass > D-glass > quartz (≈ 0.1 × E-glass); aramid negative in-plane | §60.3.5.1 |
| Traditional PI film CTE | > 30 ppm/°C (Kapton H, Apical AV) | §65.5.2.1 |
| Kapton range | −430 to 780°F usable; chars 1500°F; data mostly −195 to 200°C; cut-through 12,000 psi (0.001 in) | §65.5.2.4 |
| PET (Mylar) | 700 V/mil (0.001 in); 23,000 psi; −60 to 150°C; performance drops > 70°C | §65.5.3 |
| Thin glass-epoxy flex | < 200 µm | §65.5.4 |

### 2.7 Solder-joint reliability multipliers

| Variable | Effect on thermal-cycle life (unless noted) | Source |
|---|---|---|
| Mirrored (back-to-back) BGAs | × 0.5 (first pass); ÷ 2–3 | §62.3.2, §63.4.1 |
| Stacked vs single package | baseline ≈ 10% lower | §62.3.2.1 |
| CSP on 0.4 mm vs 1.575 mm board | ≈ 2× on thin board | §63.6.2 |
| Board CTE 13.4 → 17.3 ppm/°C (CSP 8.6) | 2000 → 500 cycles (slope −2 vs Δα) | §63.4.1 |
| Pad mismatch package vs board | up to −25% | §62.3.9 |
| SMD vs NSMD board pads (SnPb BGA) | SMD +15% (stand-off 22.2 vs 20.8 mil) | §63.6.5 |
| Ball 0.889 vs 0.762 mm | ≈ 1.3× | §62.3.13.2 |
| Corner depopulation (6 balls/corner) | absorbs ≈ 2 mil warpage | §62.3.8 |
| ViP (unfilled) under BGA192 | void % ≈ 4×; life reduced | §60.4.5 |
| SAC105 vs SAC305 | drop 1.2–1.7× better; thermal-cycle life lower (∝ %Ag) | §63.7.2 |
| Initial IMC 1 → 2.5 µm (1206) | life ÷ > 2 | §63.4.3 |
| Dwell 10 → 30/60 min | test duration × 1.5–2.5; η ∝ t^−0.18 (SAC105), t^−0.22 (SAC305) | §63.7.3 |
| Ni-plated PTH barrel | ≈ 3× (defective Ni ≈ 1/3) | §60.4.9 |
| ENIG vs SAC bend strength | SAC/ENIG ≈ 3× SnPb/ENIG force to failure | §64.3.1.2 |
| Un-aged SoP vs ENIG joints | up to 2× strain/strain-rate strength | §62.3.11.2 |
| 0.4 mm FPBGA ViP package substrate | +20% thermal-cycle life; drop 148 (ViP/NViP) vs 7 (ViP/ViP) | §61.1.5 |

### 2.8 Environments, design life, load levels

| Item | Value | Source |
|---|---|---|
| Laptop/desktop design life | 3–5 yr | §63.2 |
| Automobile | 10 yr or 100,000 miles | §63.2 |
| Aerospace/medical/solar | no failures at 40 yr | §63.2 |
| Telecom network | < 0.01% cumulative failures at 15–20 yr | §63.2 |
| Automotive environment | −55 to > 95°C, up to 100% RH, minutes-scale transitions; on-engine 150–175°C | §62.3.1, §63.1 |
| Handheld shock / drop | ≈ 1500 G; JESD22-B111 1500 G, 0.5 ms half-sine | §60.4.7, §64.3.3 |
| Server/network shock | ≈ 500 G | §62.3.11.2, §64.3.3 |
| Strain rates | bend ≈ 1e4 µε/s; shock ≈ 1e5 µε/s; ENIG brittle above ≈ 5000 µε/s | §64.3.3, §62.3.11.1 |
| Card power / heatsinks | up to 1000 W per card; heatsinks ≈ 10 in², > 1 lb | §62.3.10 |
| Field-life example | 1 power cycle/30 d + 4 mini-cycles/d → 107.8 yr; × ½ safety → 53.9 yr | §64.2.6.3 |
| Consistency check (derived) | package B lab life ≈ 3,575 cycles (37,895/10.6 = 163,020/45.6) | §64.2.6 |

### 2.9 Flex-circuit materials and process capability

| Item | Value | Source |
|---|---|---|
| PI base film | 12.5 / 25 (consumer) / 50 µm (industrial, avionics) | §65.5.2.1 |
| Cu foil | 35, 18 standard; 12, 9 new standard; RA < 10 µm available; 3–5 µm by etch-down; 1–5 µm ED on carrier | §65.6, §66.2.2 |
| Liquid PI dielectric | 5 µm pitch, 10 µm vias; 10 µm coverlay sufficient; cure > 300°C; cost 5–10× epoxy PIC | §65.5.2.3, §65.8.4.2 |
| Cast adhesiveless | substrate ≥ 12 µm; Cu 70/105 µm possible; double-sided > 300°C | §65.7.2.1 |
| Sputter/plate adhesiveless | seed < 100 nm; conductors 0.1–1 µm to < 10 µm | §65.7.2.2 |
| Lamination adhesiveless | > 330°C lamination; > 350°C press | §65.7.2.3 |
| Flex PTH plating | ≈ 15 µm sufficient; ≈ 20 µm nominal; > 25 µm hi-rel | §66.2.5, §67.2.4 |
| Excimer microvia | < 40 µm in 25 µm adhesiveless PI | §66.2.5 |
| Dry-film imaging | 15–20 µm film → 30–40 µm L/S on 12 µm Cu | §67.3.2 |
| Phototool alignment | ±10 µm for < 50 µm pitch | §67.3.3 |
| Coverlay | PIC openings finer than 200 µm pitch; laser < 100 µm; film registration ≈ 50–75 µm | §66.2.3, §67.4.1 |
| PIC process | hold 15–30 min; develop 1% Na2CO3; bake ≈ 150°C ≈ 30 min | §67.4.3 |
| Tooling holes (CCD punch) | ±50 µm | §67.6 |
| Semi-additive example | 10 µm wide × 25 µm thick trace | §67.9.1 |
| Microvia methods | drill 50 µm in 50 µm; punch 70 & 25 µm; excimer ≤ 50 µm; CO2 > 60 µm; chemical/plasma ≈ 100 µm in 50 µm | §67.9.3–67.9.5 |
| Flying leads | punched ≥ 1.0 mm; excimer < 50 µm; CO2 > 70 µm; plasma slope 30–60° | §70.2 |
| TAB | web 35/70/155 mm; lead pitch limit ≈ 40 µm | §70.3 |
| Microbumps | 100–150 µm pitch on 50 µm; dimples > 60 per array, > 1000 matings; pitch ≥ 50 µm | §70.4, §66.3.2 |
| Connectors | SMT mated pair ≥ 0.5 mm (0.2 mm advanced); zebra 200 µm | §68.3.4–68.3.5 |
| Bookbinder | +250 µm per successive layer | §69.2.1 |
| Rigid-flex inner PI | ≥ 50 µm | §69.2.2 |
| HD-ED vs RA copper | HD-ED ≈ 1e6 flex cycles; RA up to 1e9 | §66.4 |

### 2.10 Flex electrical design numbers (Ch. 66)

| Item | Value | Source |
|---|---|---|
| Guarding, adjacent-pair capacitance | grounded guards both sides −20%; interspersed + peripheral grounded guards −85%; floating guards slightly increase C | §66.5.4 |
| Embedded/covercoated microstrip Z0 | ≈ 22% lower than air-exposed | §66.6.1 |
| Epoxy-glass εr drift | ≈ 6 at 1 kHz → 5 at 25 MHz | §66.6.1 |
| Transmission-line regime | usually > 50 MHz | §66.6 |
| Parallel lines, 0.062 in apart on 0.062 in | 0.5 pF/in (εr = 5); 0.3 pF/in (PTFE) | §66.6.4 |
| Embedded line length for equal delay | 0.78 × unembedded | §66.6.4.1 |
| Crosstalk curves | 0.0075 < W < 0.025 in, 2 oz (0.0028 in) Cu, Td = 1.8 ns/ft, lines terminated in Z0 | §66.6.4.2 |
| Strip-line example | Z0 75 Ω, PTFE εr 2.1, 0.062 in overall → curve 110, b = 0.050 in, w = 0.017 in | §66.6.2 |

### 2.11 Formulas (ASCII)

- F1 System first-pass yield: `P_sys = Y_board^N` (e.g. 0.97^20 = 0.54). §57.2
- F2 FMEA: `RPN = F × C × D` (rankings Tables 58.1–58.3, not in text). §58.2
- F3 Field between conductors: `E = V / d` (V/mm). §59.2
- F4 Trace resistance `R = ρ·L/A`; corrosion factor `CF = 1 − R(0)/R(t)` (derived). §59.3
- F5 CAF: `MTTF ∝ L^4 / V^2`. §59.4
- F6 `R(t) = 1 − F(t)`; constant rate `R(t) = exp(−r·t)`, `MTBF = 1/r`. §60.2.3
- F7 Weibull x-fraction life: `t_x = η·(−ln(1 − x))^(1/β)`; solder joints β ≈ 2–4 (standard form; body missing). §60.2.3
- F8 Arrhenius equivalence for diffusion-controlled steps: `t1/t2 = exp[(Ea/k)·(1/T1 − 1/T2)]` (standard; body missing). §60.2.5
- F9 Thermal-cycling failure rate `∝ ΔT^2`. §60.2.5
- F10 SIR: `ρ_s (Ω/sq) = R × (L_parallel / d)`. §60.2.6.3
- F11 Composite CTE: `α = Σ(E_i·α_i·t_i) / Σ(E_i·t_i)`. §60.3.5.1
- F12 Low-cycle PTH fatigue: `N_f ∝ 0.5·(εf/Δε)^m`; εf(ED Cu) ≈ 0.3. §60.4.1, §60.4.9
- F13 IPC PTH effective strain: `Δε_eff = Kd·Δε·(10/KQ)`, Kd ≈ 1.6. §60.4.2
- F14 Inverse power law: `log N_f = log A − n·log S` (standard; body missing; slope break at Tg). §60.4.3
- F15 Pad-tilt strain: `ε = 3·d·t·b / (2·L^2)`, d = α_z·ΔT, t = half board thickness (printed "r"), b = pad thickness, L = remaining annular ring. §60.4.4
- F16 Miner: `Σ n_i/N_i = C`, 0.7 ≤ C ≤ 2.2; power + mini-cycles: `N_p = 1 / (1/N_p,only + k/N_m,only)`, k = mini-cycles per power cycle. §60.4.8, §64.2.6.3
- F17 `STII = (Tg + Td)/2 − 10 × (% z-expansion 50→260°C)`. §60.4.6
- F18 Corner-joint shear strain: `γ = L·|α_B − α_C|·ΔT / h_S`. §63.4.1
- F19 Joint life: `N_f ∝ γ^(−m)`, m ≈ 1–2; observed `N_f ∝ Δα^(−2)`. §63.4.1
- F20 Assembly stiffness: `1/K = 1/K1 + 1/K2 + 1/K3`; mirrored `1/K_M = 1/K1 + 2/K2`; `N_mirrored/N_single ≈ K/K_M`. §63.5, §63.6.4
- F21 Strain-energy life: `N_f / A = C / ΔW` (standard form; body missing). §63.5
- F22 Plate rigidity `D = E·h^3 / (12·(1 − ν^2))`; `fn ∝ sqrt(D/ρ_area)`; center deflection `∝ G_out/fn^2`, `G_out = Q·G_in`, `Q ≈ sqrt(fn)` (D, fn bodies missing; standard). §63.4.2
- F23 Clamped–clamped first mode (derived to match the text's zero-curvature points): `Z(X) ≈ Z0·(1 − cos(2πX/B))/2`, curvature `∝ cos(2πX/B)` → 0 at X = B/4, 3B/4. §63.4.2 (medium)
- F24 Barrel joint volume: `V = π·h_S·(3(b/2)^2 + 3(c/2)^2 + h_S^2) / 6`, solve for h_S. §63.6.6
- F25 Norris–Landzberg: `AF = (ΔT_lab/ΔT_field)^1.9 · (f_field/f_lab)^(1/3) · exp(1414·(1/T_max,field − 1/T_max,lab))`, T in K (constants not printed; reproduce the text's 3.2 example). §64.2.4
- F26 `Z0 = sqrt(L/C)` (lossless). §66.6
- F27 Strip-line: `Z0 = (60/sqrt(εr))·ln(4b/(π·d0))`, `d0 = 0.567·w + 0.67·t` (d0 from text; Z0 form standard; gives ≈ 71 Ω for the §66.6.2 example vs 75 Ω read from the graph). §66.6.2
- F28 Microstrip (fringing-corrected, standard IPC form; body missing): `Z0 = 87/sqrt(εr + 1.41) · ln(5.98·h/(0.8·w + t))`; embedded ≈ 0.78 × Z0. §66.6.1
- F29 Forward crosstalk: `V_F(t) = K_F·l·dV0/dt` (K_F < 0 microstrip, 0 homogeneous; K_B > 0). §66.6.4.2
- F30 Flexural modulus: `E_B = L^3·m / (4·b·d^3)`. Glossary
- F31 Etch factor = depth / lateral etch. Glossary
- F32 Fault dictionary bits = `N_faults × N_vectors × N_outputs`. §57.4.1
- F33 1149.4 in-situ impedance: `Z = (V_pin1 − V_pin2) / I_forced`. §56.5.2
- F34 `1 FIT = 1 failure / 1e9 device-hours`. §63.1
- F35 Bookbinder layer length: `L_i = L_1 + 0.25 mm·(i − 1)`. §69.2.1

## 3. Mechanizable checks

Solder-joint and package reliability
- `CHECK-joint-shear-strain`: inputs dnp_mm, standoff_mm, cte_board_ppm, cte_comp_ppm, dT_C → γ = dnp·|α_B − α_C|·1e-6·ΔT / standoff → pass γ < 0.01 (≥ 1% = flag for deeper analysis, not an absolute limit) → margin = 1 − γ/0.01 → COOMBS-4190, 4191, 4192.
- `CHECK-cte-mismatch-life-scaling`: inputs N_ref, dalpha_ref, dalpha_new, N_required → N_new = N_ref·(dalpha_ref/dalpha_new)² → pass N_new ≥ N_required → margin N_new/N_required − 1 → 4191.
- `CHECK-mirrored-bga`: inputs per BGA top/bottom outline polygons, via list → overlap area of opposite-side BGA outlines; shared through-vias inside overlap → pass no overlap; overlap without shared vias = warn (life × 0.5); overlap with shared vias = fail → margin = −overlap_area → 4162, 4193.
- `CHECK-dnp-similarity`: inputs dnp_qualified_mm, dnp_new_mm, same_materials (bool) → ratio = dnp_new/dnp_qualified → pass same_materials ∧ ratio ≤ 0.9 (10–20% smaller accepted by similarity); ratio > 1 = requalify → margin 1 − ratio → 4178.
- `CHECK-bga-pad-ratio`: inputs pkg_pad_dia_mm (wettable), pwb_pad_dia_mm nominal, pwb_pad_tol_mm → A_ratio = (d_pwb/d_pkg)²; d_pwb,max = d_pwb + tol → pass 0.80 ≤ A_ratio ≤ 1.00 ∧ d_pwb,max ≤ d_pkg (≈ 10% smaller diameter preferred) → margin min(A_ratio − 0.80, 1.00 − A_ratio) → 4172, 4173, 4205.
- `CHECK-warpage-bridging`: inputs pkg_warp_mil and board_warp_mil at/above liquidus over 7 mm (signed: convex +, concave −), pitch_mm → eff = |pkg − board| (opposite curvatures add) → pass pitch = 1.0 mm ∧ eff ≤ 9 mil; other pitches = review → margin 9 − eff → 4169.
- `CHECK-au-embrittlement`: inputs au_um, au_area_mm² (all Au surfaces wetted by the joint), solder_vol_mm³, rho_au, rho_solder (user densities) → wt% = m_Au/(m_Au + m_solder)·100 → pass ≤ 3 wt% (low end of 3–5%) → margin 3 − wt% → 4097.
- `CHECK-norris-landzberg-life`: inputs N_lab, dT_lab, dT_field, f_lab, f_field (cycles/day), Tmax_lab_C, Tmax_field_C, required_field_cycles → AF (F25) → N_field = AF·N_lab → pass N_field ≥ 2·required (safety factor 2) → margin N_field/(2·required) − 1 → 4215, 4218. SnPb only; Pb-free needs a validated transform (4216).
- `CHECK-miner-power-mini`: inputs N_power_only, N_mini_only, k_mini_per_power, power_cycles_per_year, design_life_yr → N_p = 1/(1/N_power_only + k/N_mini_only); life_yr = N_p/power_cycles_per_year → pass life_yr/2 ≥ design_life_yr → margin → 4218, 4132.
- `CHECK-weibull-early-life`: inputs η, β, x_fraction (e.g. 0.01), required_cycles → t_x = η·(−ln(1 − x))^(1/β) → pass t_x (90% lower bound where available) ≥ required → margin t_x/required − 1 → 4065, 4213.
- `CHECK-reliability-goal`: inputs product_class, design_life_yr, allowed_fraction_failed → compare to benchmarks (3–5 yr PC; 10 yr/100k mi auto; 0 at 40 yr aerospace/medical/solar; < 0.01% at 15–20 yr telecom) → pass goal stated and ≥ benchmark for class → 4185.
- `CHECK-vibration-placement`: inputs span_B_mm (clamp to clamp), component_x_mm, component_is_critical → k = |cos(2π·x/B)| (normalized curvature, F23) → pass critical parts at k ≤ user threshold (near B/4, 3B/4), none near center or clamped edges → margin threshold − k → 4194 (two-edge-clamped boards).
- `CHECK-component-cte-orientation`: inputs board_alpha_x, board_alpha_y, part long-axis orientation → pass long axis along min(α_x, α_y) when |α_x − α_y| is material (up to ≈ 5 ppm/°C) → 4201.

PTH, via and laminate
- `CHECK-pth-aspect-ratio`: inputs board_thk_mm, finished_hole_mm → AR = thk/hole → pass AR ≤ 5 (fail above); warn AR > 3 → margin 5 − AR → 4089, 4137.
- `CHECK-pth-plating`: inputs ipc_class, barrel_cu_min_um, pbfree (bool), dissolution_allowance_um (≤ 12 reported) → t_req = 12 (Class 1) or 25 (Class 2/3) + (pbfree ? allowance : 0) → pass barrel_cu_min ≥ t_req → margin barrel_cu_min − t_req → 4090, 4127.
- `CHECK-pth-effective-strain`: inputs d_eps (FEA/analytic), quality (extraordinary…poor), ref_d_eps_eff → Δε_eff = 1.6·Δε·(10/KQ) → pass Δε_eff ≤ ref (qualified design) → margin ref/Δε_eff − 1; relative life ≈ (ref/Δε_eff)^m with m user-set → 4100, 4102, 4134.
- `CHECK-pth-assembly-life-fraction`: inputs n_assembly_excursions (reflows + wave + rework + HASL), N_barrel_asm, N_knee_asm, N_barrel_field, N_knee_field, field_cycles_required → remaining_i = 1 − n/N_i,asm; capacity_i = remaining_i·N_i,field → pass min(capacity) ≥ required → margin → 4133, 4098, 4125.
- `CHECK-pad-tilt-strain`: inputs alpha_z_ppm, dT_C, board_thk_mm, pad_thk_mm, min_remaining_ring_mm, ref_eps → ε = 3·(α_z·ΔT)·(thk/2)·pad_thk / (2·ring²) → pass ε ≤ ref (qualified design) → 4117.
- `CHECK-caf-spacing`: inputs wall_to_wall_mm, environment (telecom/hi-rel/other), bias_V, ref_L_mm, ref_V → pass telecom/hi-rel: wall_to_wall ≥ 0.65 mm; relative MTTF = (L/ref_L)⁴·(ref_V/V)² ≥ 1 → margin wall_to_wall − 0.65 → 4059, 4050.
- `CHECK-caf-layout`: inputs laminate family, hole pairs in line with glass weave (bool), plane polarity → flag in-line holes (staggered preferred), non-CAF-resistant laminate at < 0.65 mm, small anode facing large cathode → 4052, 4053, 4058, 4061.
- `CHECK-stii`: inputs Tg_C, Td_C, z_expansion_50_260_pct → STII = (Tg + Td)/2 − 10·pct → pass STII ≥ that of the qualified reference laminate (studied 181–247) → margin STII − ref → 4126.
- `CHECK-laminate-thermal-window`: inputs cure_system (dicy/phenolic), Tg_C, peak_reflow_C, max_service_or_test_C → pass (dicy → peak ≤ 240°C) ∧ max_service_or_test < Tg ∧ peak < 260°C for standard FR-4 (measling/delamination) → margins 240 − peak, Tg − max → 4166, 4199, 4067, 4095, 4084.
- `CHECK-composite-cte`: inputs per layer E_i, α_i, t_i → α_eff = Σ(E·α·t)/Σ(E·t), E_eff = Σ(E·t)/Σt → feeds CHECK-joint-shear-strain → 4093, 4203.
- `CHECK-microvia-structure`: inputs via_dia_um, stack_count, fill_type, staggered (bool), under_BGA_pad (bool), depth_layers → flags: stack_count ≥ 3 (pad-rotation reversal; staggered ≈ 100× more robust), Cu-filled stack (corner cracks), dia < 75 µm for −65/150°C duty, unfilled ViP under SAC BGA, depth ≥ 3 layers or dia ≥ 150 µm (void share 40–56%) → pass no flags → 4123, 4143, 4154, 4158, 4159.
- `CHECK-thermal-test-plan`: inputs test_Tmax_C, laminate_Tg_C, via_type, ist_peak_C → pass (PTH/solder tests) Tmax < Tg unless service exceeds Tg; microvia IST peak = 190°C (fail if ≥ 210°C) → 4067, 4079, 4149.

Test, inspection and DFT
- `CHECK-inspection-throughput`: inputs area_cm2_per_side, sides, speed_cm2_s (SPI 2–22, AOI 10–40), joints, axi_joints_s (50–150), takt_s → t = Σ area/speed + joints/rate → pass t ≤ takt, else plan sampling → margin takt − t → 4002–4004, 4009.
- `CHECK-inspection-dfm`: inputs edge_clearance_mm (parallel edges), corner_fiducials, silk_outlines (bool), max_height_top/bottom_mm, system_clearance_mm, board_thk_mil → pass clearance ≥ 3 mm ∧ fiducials ≥ 3 corners ∧ ¬silk_outlines ∧ heights ≤ clearance; thk < 30 mil = fixture review → 4011–4015, 4019.
- `CHECK-inspection-coverage`: inputs BOM package type, pitch_mm, double_sided (bool), PTH parts → parts with hidden joints (BGA, PGA, some J-lead), pitch ≤ 0.5 mm or SOT → need AXI or electrical coverage; double-sided/PTH/BGA → cross-sectional (not transmission) x-ray → pass all parts covered → 4005, 4007, 4008.
- `CHECK-system-yield`: inputs Y_board, N_boards, target → P = Y^N → pass P ≥ target → 4027.
- `CHECK-ict-access`: inputs nets, pad_dia_mil, pad_pitch_mil, probe class (100/75/50 mil) → pass pad ≥ 35 mil (medium) ∧ pitch ≥ probe class; nets without access must be boundary-scan observable → 4030, 4021, 4315.
- `CHECK-jtag-hygiene`: inputs JTAG netlist → pass TDO→TDI chain continuous ∧ TCK/TMS to all devices ∧ TRST* (if present) pulled down ∧ unused preset/clear tied through ≈ 100 Ω (not direct) ∧ spare DFT inputs pulled to 0 → 4020, 4022–4024.
- `CHECK-ict-strain`: inputs board_thk_mil, peak_strain_ue, strain_rate_ue_s, limit_curve(thk, rate) (user, per IPC/JEDEC-9704), push_finger_positions → pass strain < limit ∧ no push finger within package corner zones; thk < 93 mil = high-risk flag → margin limit − strain → 4177, 4220.
- `CHECK-fmea-rpn`: inputs per mode F, C, D, action_assigned, fmea_date, design_freeze_date → RPN = F·C·D; rank → pass every mode in top 50% by RPN has an action ∧ fmea_date < freeze → 4040, 4041.

Flex and rigid-flex
- `CHECK-flex-dynamic-zone`: inputs per flex region: dynamic (bool), conductor_layers, cu_type (RA/HD-ED/ED), symmetric_about_conductor (bool), coverlay_type, plating_in_zone (bool), required_cycles → pass dynamic ⇒ layers = 1 ∧ symmetric ∧ ¬plating ∧ cu_type = RA (HD-ED only if required ≤ 1e6) ∧ coverlay ∈ {film, PI liquid} → 4248, 4249, 4238, 4244.
- `CHECK-flex-bookbinder`: inputs n_flex_layers_in_bend, per_layer_increment_mm → pass n = 1 or increment ≈ 0.25 mm per successive layer (outer longer) → 4283.
- `CHECK-flex-film-cte`: inputs film_cte_ppm, finest_pitch_um → pass HDI (fine pitch) ⇒ film_cte ≤ 30 ppm/°C → 4228.
- `CHECK-flex-opening-process`: inputs coverlay_opening_um, position_tol_um, coverlay_process, flying_lead_window_mm, window_process → pass (opening < 200 µm ∨ tol ≤ ±100 µm ⇒ PIC or laser) ∧ (window < 1.0 mm ⇒ not pre-punched) → 4265, 4242, 4288.
- `CHECK-tab-pitch`: inputs lead_pitch_um, construction (TAB flying lead / COF) → pass pitch ≥ 40 µm for flying leads, else COF → 4292.
- `CHECK-flex-conductor-nicks`: inputs nominal_width, min_measured_width → reduction = 1 − min/nominal → pass ≤ 0.20 → margin 0.20 − reduction → 4304.
- `CHECK-flex-rigidflex-materials`: inputs inner_PI_um, bond_ply_type in rigid area, adhesive type → pass inner_PI ≥ 50 µm ∧ rigid area uses glass-reinforced prepreg (not unreinforced flexible bond ply) → 4281, 4284.

Signal integrity on flex
- `CHECK-stripline-z0`: inputs w_in, t_in, b_in, er, Z_target, tol_pct → d0 = 0.567w + 0.67t; Z0 = 60/sqrt(er)·ln(4b/(π·d0)) → pass |Z0 − Z_target| ≤ tol → 4254, 4255 (validate against field solver/TDR; graph method preferred by the text).
- `CHECK-microstrip-embedded`: inputs Z0_surface, embedded (bool) → Z0 = 0.78·Z0_surface when covercoated → pass vs target → 4254.
- `CHECK-embedded-delay-length`: inputs max_len_surface (timing budget) → max_len_embedded = 0.78·max_len_surface → pass routed_len ≤ limit → 4258.
- `CHECK-sir-square-count`: inputs R_meas_ohm, parallel_len_mm, gap_mm → ρ_s = R·len/gap → report Ω/sq; pass (IPC-SM-840A Class 2) R_meas ≥ 1e8 Ω → 4071, 4072.
- `CHECK-guard-capacitance`: inputs C_pair, guard_config (none / grounded both sides / interspersed + peripheral) → C × {1, 0.80, 0.15} → pass ≤ allowed coupling C → 4253.

## 4. Verification procedures & plots

- V1 Accelerated thermal cycling (IPC-9701/9701A): x = cycles (log), y = cumulative % failed (Weibull scale); fit 2- and 3-parameter Weibull, keep the better regression, draw 90% two-sided confidence bounds; good = steep β and 1%-life lower bound ≥ requirement after AF mapping. Setup: in-situ event detection on daisy chains (opens appear at temperature extremes), first-level chains included, two board thicknesses, back-side parts included, TC1 0/100°C or TC4 −55/125°C, ≥ 10 min dwell (30 min option for SAC). Sources §64.2.1–64.2.2, §62.3.3, §62.3.6–62.3.7.
- V2 Acceleration model plot: log N_f vs log ΔT (or stress), separate fits below and above Tg (inverse power law); annotate the field ΔT and projected AF; confirm by failure analysis that test and field modes match. §60.2.5, §60.4.3.
- V3 PTH/microvia interconnect resistance vs cycles (IST/HATS/AtA): y = %ΔR, x = cycles; fail at +10% (IST/HATS) or +20% (FEA correlation); plots per preconditioning (as-built, 6× 260°C) and per hole size; microvias at 190°C IST peak. §60.2.7, §60.4.6, §61.1.5.
- V4 PTH design-trade curves: cycles-to-failure vs peak temperature (mark Tg), vs plating thickness, vs aspect ratio; good = operating range left of Tg knee with AR ≤ 5. §60.4.9, Figs. 60.42–60.45.
- V5 SIR / M&IR: y = log10 R (Ω), x = hours, per condition in §2.3; pass Class 2 ≥ 1e8 Ω and no dendrites under microscope; guard/shield leads for readings > 1e12 Ω. §60.2.6.3.
- V6 CAF: resistance vs time for 0.27/0.38/0.50/0.65 mm hole-to-hole, in-line vs staggered, 65°C/85% RH, 500 h; secondary plot MTTF vs L⁴/V² should be linear; cross-section failures to confirm anode-origin filaments. §59.4–59.6.
- V7 Flux-residue corrosion: %CF vs time at 60°C/93% RH for 10 days (modified Bono coupon, 0.5 mm gap, 50 V); rank fluxes; inspect for dendrites/green residues. §59.3.
- V8 Warpage vs temperature (shadow moiré per JESD22-B112) of package and board site through the reflow profile; plot effective (combined) warpage vs T; pass ≤ 9 mil over 7 mm at/above liquidus for 1 mm pitch; representative production boards. §62.3.8.
- V9 Production strain survey (IPC/JEDEC-9704): strain vs time for ICT engage/disengage, connector press, heatsink attach, card-cage insertion; scatter peak strain vs strain rate over the board-thickness limit curve. §62.3.12, §64.3.1.1.
- V10 Monotonic 4-point bend (IPC/JEDEC-9702): force or board strain to failure with gauges 1 (under corner joint), 2 (center), 3 (beside package); failure-mode histogram per finish/alloy; FEA joint-to-board strain ratio to transfer limits (not across pad sizes). §64.3.1, §64.4.2.
- V11 Drop/shock (JESD22-B111, 1500 G, 0.5 ms half-sine; server ≈ 500 G): drops-to-failure Weibull; accelerometers + strain gauges on the carrier; compare SAC alloys and ViP combinations. §64.3.3, §63.7.2, §61.1.5.
- V12 Vibration modal survey: first-mode shape and curvature map of the clamped board; overlay critical-part locations (target zero-curvature lines B/4, 3B/4); verify stiffeners raise fn. §63.4.2.
- V13 Solder-joint FEA: global 1/8-symmetry model (unit ΔT) → worst joint → local model 2–4 cycles to a stable shear stress–strain hysteresis loop; loop area ΔW → N_f/A = C/ΔW; calibrate models against test data before prediction. §63.5, §64.4.1.
- V14 Board property characterization on product (and component-area) coupons: TMA α_x, α_y, α_z vs T (Tg knee), DMA storage modulus vs T; feed measured values, never datasheet values, into V13 and CHECK-joint-shear-strain. §63.6.1, §60.4.3.
- V15 ViP void characterization: x-ray void % per ball for corner and adjacent balls, and location relative to the board-side crack path; microsection microvias optically (x-ray shows fill only). §60.4.5, §61.1.4, §61.1.7.
- V16 Bare-board thermal stress: solder float 288/289°C for 10 s (≥ 260°C Pb-free), plus 6× 260°C reflow and 6× 288°C float for Pb-free qualification; microsection for barrel/corner cracks, ILS, hole-wall separation, lifted lands. §60.2.6.1, §60.4.6, §71.8.4.
- V17 Flex endurance: cycles to failure vs bend radius (IPC-TM-650 flex test; Engelmaier fatigue-ductility, rolling, MIT or collapsing-radius testers), resistance monitored; compare RA vs ED; folding test at drawing location/radius/angle/direction. §66.4, §71.8.1.
- V18 Flex/transmission-line electrical: TDR impedance along the flex; backward/forward crosstalk vs spacing with lines terminated in Z0; attenuation vs frequency (1–3000 MHz) for shielded flex cable. §66.6.4, §71.9.
- V19 Capacitive lead-frame opens test: measured pin capacitance (~100 fF nominal) per pin; open = 2–10× drop; plot per-pin distribution for each IC/connector. §57.6.
- V20 Dwell-time study for Pb-free ATC: characteristic life vs dwell (log–log; expect exponents ≈ −0.18/−0.22) and test duration vs dwell; choose the shortest dwell that preserves failure mode. §63.7.3.

## 5. Pitfalls, failure modes, review checklist

Inspection and test
- [ ] AOI alone on BGA/PGA/J-lead, ≤ 0.5 mm pitch or SOT parts → escapes and false calls. §55.10.1.2
- [ ] Transmission (2-D) x-ray on double-sided boards, PTH or BGA joints → overlapping, unresolvable images. §55.10.2.2
- [ ] Tuning AOI/AXI accept thresholds before reducing process variation → endless false-accept/false-reject tweaking. §55.11
- [ ] Silkscreen outlines around parts, non-uniform pads per package type, several suppliers per part type → slow, unreliable inspection programs. §55.12.2
- [ ] Parts under/opposite transformers, large capacitors or thick steel heat sinks → blocked transmission x-ray. §55.12.2
- [ ] Unused preset/clear pins tied directly to a rail → tester cannot control them. §56.3
- [ ] Expecting ICT to find one missing/tombstoned bypass cap among many in parallel. §57.6
- [ ] Replacing an IC for a solder-open input → "fixes" the board but pollutes process data. §57.2.3, §57.6
- [ ] Long digital backdrive bursts → upstream driver damage within milliseconds. §57.5.2
- [ ] Powering a board before shorts test. §57.5.4
- [ ] Using performance/specification testing as design validation. §57.3.2, §57.3.4
- [ ] ICT push fingers near BGA corners; boards < 93 mil; high-force OSP probing on Pb-free. §62.3.12
- [ ] Periodic room-temperature resistance checks during cycling — cracked joints close up at RT. §64.2.1

FMEA and test planning
- [ ] FMEA started late or not finished before design freeze; no action on the top 50% by RPN. §58.2.1.2, §58.3.3
- [ ] Qualification pass/fail treated as a life distribution. §60.2.4
- [ ] Acceleration above Tg or beyond service severity → new, irrelevant failure modes. §60.2.5
- [ ] Thermal-shock results mapped to field life. §64.2.1.2
- [ ] SnPb Norris–Landzberg constants applied to Pb-free without validation. §64.2.4.3
- [ ] Anand (steady-state) creep model used for field projection where primary creep dominates. §64.2.3
- [ ] Bend acceptance data transferred across pad sizes (≈ 18% joint-strain change). §64.4.2
- [ ] Bend/shear tests at uncontrolled time after reflow (SnPb/ENIG strength +50% in 3 weeks). §64.3.1.2, §64.3.4
- [ ] Workmanship class compliance (even Class III) taken as proof of reliability. §63.1, §63.3
- [ ] Shipping/storage thermal cycles left out of the damage budget. §63.3

PCB fabrication and PTH
- [ ] "Handbook" or prepreg-datasheet CTE/modulus in joint models (real boards 12–21 ppm/°C, 10–30 GPa). §63.6.1
- [ ] Supplier-advertised α1 assumed valid for the actual multilayer construction. §60.4.3
- [ ] Inner-layer Cu foil elongation < 8% (1 oz) → foil cracks. §60.3.4.2
- [ ] Thin plating at the PTH knee (excess leveler) or AR > 5:1. §60.3.4.4, §60.4.9
- [ ] Defective Ni in barrel ("nickel acceleration") — failure in ≈ 1/3 the time. §60.4.9
- [ ] Solder-pot/fountain rework > 25 s contact, no preheat, unlogged rework count. §60.3.4.6
- [ ] Pulling parts before solder is fully molten → lifted pads. §60.3.4.6
- [ ] HASL not counted as a PTH thermal cycle; each extra Pb-free reflow ≈ −30% PTH life. §60.3.5.3, §60.4.6
- [ ] Au in SnPb joints above 3–5 wt% → AuSn4/AuSn2 embrittlement. §60.3.5.3
- [ ] Thick dry-film mask over tight traces (crevices) or mask over solder. §60.3.5.2, §60.3.4.5
- [ ] Hygroscopic laminates (PI, aramid) reflowed without bake. §60.3.4.5
- [ ] 4.5 mil holes on 0.5 mm grid in humid service → crazing → CAF. §60.4.5
- [ ] 0.8 mm via pitch through Pb-free reflow → internal delamination (1 mm safer). §60.4.5
- [ ] In-line hole pairs along glass, < 0.65 mm wall-to-wall, water-soluble polyglycol flux, hot profiles → CAF. §59.5, §59.7
- [ ] Dicy-cured FR-4 above 240°C peak; operating or testing above Tg. §62.3.5.1, §63.6.1

HDI / microvia
- [ ] Microvia IST above 190°C (artifacts) or at 150°C (non-discriminating). §61.1.5
- [ ] Stacked (esp. Cu-filled) microvias where staggered would fit (≈ 100× less robust). §61.1.6
- [ ] 50 µm microvias in −65/150°C service. §61.1.7
- [ ] Unfilled ViP under SAC BGAs; 150–200 µm or 3-layer-deep ViPs (void share 40–56%). §60.4.5, §61.1.4
- [ ] X-ray alone to judge microvia quality. §61.1.7

Assembly and solder-joint reliability
- [ ] Mirrored BGAs, especially sharing through-vias. §62.3.2
- [ ] Qualifying on a thinner board than the product. §62.3.3, §63.6.2
- [ ] Relying on JEDEC ±8 mil coplanarity for large BGAs on thick boards; warpage measured only at room temperature. §62.3.8
- [ ] Board pad larger than package pad; drawing pad size assumed equal to fabricated size (12 → 9–15 mil). §62.3.9, §63.6.6
- [ ] Die edge over solder balls; corner balls populated on large organic packages. §62.3.8, §62.3.13.3
- [ ] Bolt-down heatsink tolerance stack loading the package; thermal cycling heatsinked parts without joint-ΔT calibration. §62.3.10
- [ ] ENIG under high strain-rate loads (brittle interfacial fracture) and black-pad lots. §62.3.11.1
- [ ] Aged solder-on-pad / OSP joints under shock (Kirkendall voids). §62.3.11.2
- [ ] Alloy-42 leads in harsh environments; short stiff leads assumed compliant. §63.3
- [ ] Static mechanical load carried by solder joints. §63.3
- [ ] Rectangular parts oriented along the higher board CTE axis. §63.6.1
- [ ] Critical parts at board center or clamped edges under vibration; ribs across the wrong axis. §63.4.2
- [ ] Reflow profile drift changing initial IMC thickness (1 → 2.5 µm halves life). §63.4.3
- [ ] SAC Ag content chosen without regard to drop vs thermal-cycle dominance. §63.7.2
- [ ] SAC balls with SnPb paste (mixed metallurgy). §64.2.4.5
- [ ] Carrier/chassis resonance matching the PCBA with high-strain mode shapes. §64.3.3

Flex and rigid-flex
- [ ] Kapton H / Apical AV (CTE > 30 ppm/°C) for HDI flex. §65.5.2.1
- [ ] PET film where soldering or > 70°C service is required. §65.5.3
- [ ] Adhesive-based laminates/coverlays for Pb-free or wire bonding; brominated adhesives where halogen concerns apply. §65.7.1, §65.11
- [ ] Rigid-board solder mask on flex (cracks on bending); screen-printed or epoxy PIC in dynamic zones. §65.8
- [ ] PSA-bonded stiffeners where position must hold (creep). §65.10
- [ ] PTH, plating or two conductor layers in a dynamic zone; asymmetric stack; thin traces on the outside of a bend; ED copper for high-cycle flexing. §66.4
- [ ] Film coverlay for openings < 200 µm; adhesive squeeze-out onto pads. §67.4, §71.7
- [ ] Ammoniacal etchant on PI fine lines (attack/undercut); high-pH ENIG baths attacking coverlay adhesive. §67.3.4, §67.5
- [ ] Moist flex into reflow (vapor pressure ≈ 2× at Pb-free temperatures). §67.8, §71.4.1
- [ ] Unreinforced flexible bond ply in rigid sections; no air gap in bend zones; no bookbinder on multi-layer bends. §69.2.1
- [ ] Rigid-flex vent holes left unsealed before wet processing; permanganate desmear dwell uncontrolled. §69.2.3
- [ ] Pre-punched flying-lead windows < 1.0 mm; TAB flying leads below 40 µm pitch. §70.2.2, §70.3
- [ ] Polymer-thick-film silver conductors for power or high-speed signals. §70.5
- [ ] Edge nicks/tears on flex outlines (tear initiation); coverlayer not capturing single-sided lands. §71.6, §71.7

## 6. Standards referenced

| Standard | Edition / year (as given) | Clause / table | Governs | Source |
|---|---|---|---|---|
| IEEE 1149.1 (incl. 1149.1a) | 1990 / 1993 | EXTEST, TAP (TCK, TMS, TDI, TDO, optional TRST*), BYPASS, IDCODE | boundary-scan test access | §56.5.1 |
| IEEE 1149.4 | 1999 | ATAP (AT1, AT2), ABM | mixed-signal test bus | §56.5.2 |
| MIL-STD-1629 | — | — | FMECA procedures | §58.4 |
| Ford "Potential Failure Modes and Effects Analysis" | Sep 1988 | — | FMEA method | §58.5 |
| IPC-B-24 | — | 0.5 mm comb spacing | SIR test board (flux) | §59.3 |
| IPC-TM-650 2.6.25 (A) | 2007 | 65°C/85% RH/500 h; 0.27–0.65 mm hole spacing | CAF resistance, X-Y axis | §59.6 |
| IPC-TR-609 | Sep 1988 | — | round-robin reliability of small-diameter PTHs | §60.2.1, §60.4.9 |
| IPC-6012 / IPC-6016 / IPC-6016-HDI | — | — | rigid PCB / HDI qualification and performance | §60.2.1, §60.7 |
| IPC/JPCA-2315 | June 2000 | Table 61.2 HDI design rules | HDI & microvia design guide | §60.2.1, §61.1.1 |
| IPC/JPCA-4104 | — | — | HDI/microvia materials | §60.2.1 |
| IPC-TM-650 2.6.26 | — | +10% ΔR failure | interconnect stress test (IST) | §60.2.1, §60.2.7.2 |
| IPC-TM-650 2.6.8 | — | microsection | thermal stress/shock of PTH | §60.2.1, §60.2.7.4 |
| IPC-TM-650 2.4.28 | — | tape/peel | Cu and solder-mask adhesion | §60.2.6.2 |
| IPC-TM-650 2.4.24 / 2.4.41 | — | — | Tg / x-y CTE | §63.9 |
| MIL-P-55110 | — | 288°C/10 s float; M&IR | rigid PWB (thermal stress, moisture resistance) | §60.2.6.1, §60.2.6.3 |
| MIL-STD-202 | — | Method 106 (100 VDC), Method 402 cond. A | moisture resistance | §60.2.6.3 |
| IPC-SM-840 (A; C in Appendix) | — | Class 2: 50°C/90% RH/100 VDC/7 d ≥ 1e8 Ω; electromigration 85°C/90% RH/10 VDC/1 mA/7 d | permanent solder mask qualification | §60.2.6.3, §60.3.5.2 |
| IPC-B-25 / Y coupon | — | — | SIR/M&IR process qualification / SPC coupon | §60.2.6.3 |
| ASTM D 260-78 (as printed) | 1978 | — | DC resistance/conductance of insulating materials | §60 ref. 19 |
| IPC-D-279 (printed "Dd-279") | July 1996 | Table 60.2 laminate properties | reliable SMT PBA design | §60.3.5.1 |
| IPC-TR-484 | — | — | Cu foil ductility round robin | §60.4.9 |
| IPC-TR-579 | — | — | PTH semi-empirical fatigue model | §61.1.6 |
| IPC-TR-476 | Sep 1977 | — | metallic growth problems | §60 ref. 27 |
| IPC-9151 (PCQR2) | — | — | process capability, quality, relative reliability benchmark | §60.2.6.1, Appendix |
| IPC/JEDEC-9702 | June 2004 | 4-point bend | monotonic bend characterization | §60.4.7, §64.3.1 |
| IPC/JEDEC-9704 | June 2005 | strain vs rate vs thickness limits | PWB strain-gage testing | §60.4.7, §62.3.12, §64.3.1.1 |
| IPC/JEDEC-9707 | — | spherical bend | area-array interconnect bend | §60.4.7, §63.4.2 |
| IPC-9703 | — | — | mechanical shock/drop guidelines | §60.4.7 |
| IPC-9708 | — | — | pad cratering | §60.4.7 |
| JESD22-B111 | July 2003 | 1500 G, 0.5 ms half-sine | board-level drop (handheld) | §60.4.7, §64.3.3 |
| JESD22-B110 (A) | Nov 2004 | condition B | subassembly mechanical shock | §60.4.7, §64.3.3 |
| JESD22-B104-B; "JESD-B210A" (as printed) | — | Table 1 | mechanical shock | §60.4.7 |
| JESD22-B113 | Mar 2006 | — | board-level cyclic bend | §63.4.2, §64.3.2 |
| JESD22-B117A | Oct 2006 | high-speed shear | solder ball shear | §64.3.4 |
| JESD22-B112 | May 2005 | — | high-temperature package warpage | §62.3.8 |
| JESD22-A104-A | — | 3 of 5 conditions = IPC-9701 | temperature cycling | §60.4.7 |
| MIL-STD-810F (updated 2008) / 810G | — | vibration, shock | environmental testing | §60.4.7, §63.4.2 |
| MIL-HDBK-310; SAE J1211; Telcordia GR-3108; IEC 60721-3 | — | — | use-environment definitions | §60.4.7 |
| IPC-SM-785 | 1992 | Table 62.1 environments | accelerated reliability testing of SMT attachments | §60.4.7, §62.3.1 |
| IPC-9701 | Jan 2002 | TC1 0/100°C … TC4 −55/125°C; NTC 200–6000 | SMT solder attachment qualification | §60.4.7, §64.2.1 |
| IPC-9701A | Feb 2006 | App. A (Pb-free data/models), App. B (dwell 10 min, 30 min option) | as above + Pb-free | §60.4.7, §64.2.1.1 |
| JEDEC Publication 95, Design Guide 4.14 | Issue D, Dec 2002 (rev. 2004 pad nomenclature) | ±8 mil coplanarity | BGA outlines | §62.3.8–62.3.9 |
| IPC-7351 | Feb 2005 | WC/RSS pad tolerance; ICT test-point guidance | SMT land patterns | §62.3.9, §62.3.12 |
| EU Directive 2002/95/EC (RoHS); Commission Decision 2005/747/EC | 21 Oct 2005 | Annex exemption | RoHS; first-level interconnect exemption | §62.3.13.6, Glossary |
| IPC J-STD-001 | — | — | soldered assembly requirements | §63.1, §71.11 |
| ASTM D3039; D790; D6272 | — | — | tensile / 3-point / 4-point flexural properties (board modulus) | §63.6.1 |
| UL 94 | — | V-0, VTM-0 | flammability | §65.5.2.1, §71.5 |
| UL 796F | — | — | flexible materials interconnect constructions | §71.12 |
| ASTM D-876-61 | 1961 | adapted to film | cut-through resistance | §65.5.2.4 |
| IPC-TM-650 (flex endurance method) | — | Figs. 66.17–66.18 | dynamic flex life vs radius | §66.4 |
| ASTM D 648; "ASTM D 256 51T" (as printed) | — | 66/264 psi, 0.010 in | heat-distortion point; volume resistivity | Glossary |
| ANSI Y14.5 (printed "ANSI-Y-145") | — | — | dimensioning and tolerancing | §71.12 |
| IEC 249-2-15; IEC 326-7/-8/-9/-10/-11 | — | — | flex Cu-clad PI (flammability grade); flex SS/DS without and with PTH, multilayer flex, flex-rigid DS and ML | §71.12 |
| IPC-2221B; IPC-2223C (ex IPC-D-249); IPC-2611; IPC-2614 | — | — | board design; flex design; documentation | §71.12 |
| IPC-4202A (ex FC-231); 4203A (ex FC-232); 4204A (ex FC-241); 4412B; 4562A (ex MF-150) | — | — | flex base dielectrics; cover/bond films; metal-clad flex; E-glass fabric; metal foil | §71.12 |
| IPC-6011; IPC-6013C; IPC-9252A; IPC-A-600H; IPC-DR-572A; IPC-FC-234A | — | — | generic board performance; flex qualification; bare-board electrical test; board acceptability; drilling; PSA assembly | §71.12 |
| IPC J-STD-002 / -003 / -004 / -005 / -006 | — | — | solderability of components / boards; fluxes; paste; solder alloys | §71.12 |
| JIS C 5016, C 5017, C 6471, C 6472 | — | — | flex test methods; flex SS/DS; flex laminate test methods; flex laminates (PET, PI) | §71.12 |
| JPCA-BM01, FC01, FC02, FC03 | — | — | flex laminates; SS and DS flex; visual defect criteria | §71.12 |
| MIL-STD-2118; MIL-C-28809; MIL-P-50884C; MIL-STD-105/129/130/202/2000/45662; DOD-D-1000; DOD-STD-100; MIL-S-13949; MIL-C-14550; MIL-I-43553; MIL-G-45204; MIL-I-45208; MIL-Q-9858; MIL-P-81728; QQ-N-290 | — | — | military flex/rigid-flex design and wiring, sampling, marking, test, soldering, calibration, drawings, laminate, Cu/Au/SnPb/Ni plating, inspection and quality systems | §71.12 |
| IPC-7711A/7721A | — | (no limits given in text) | rework, repair and modification of assemblies | Appendix |
| IPC J-STD-020 / J-STD-033 / J-STD-035 | — | — | MSL classification / MSD handling / acoustic microscopy | Appendix |
| IPC-4552 / IPC-4553 | — | — | ENIG / immersion-silver finishes | Appendix |
| IPC-3406 / 3407 / 3408 | — | — | electrically conductive SMT adhesive / isotropic / anisotropic films | Appendix |
| IPC-CC-830A; IPC-CF-148; IPC-CF-152A; IPC-4101; IPC-4103; IPC-4110; IPC-4121; IPC-4130; IPC-4411 | — | — | conformal coating; resin-coated metal; Cu/Invar/Cu foil; rigid base materials; HF substrates; paper; core constructions; E-glass mat; para-aramid | Appendix |
| IPC-1902 (= IEC 60097); IPC-2141; 2222; 2224; 2225; 2226; 2251; 2252; 2615; 7525; 7530; IPC-C-406; J-STD-026/-027 | — | — | grid; controlled impedance; rigid, PC-card, MCM-L, HDI array design; high-speed; RF; dimensions; stencil; profiling; SMT connectors; flip-chip design/outline | Appendix |
| IPC-7093 / 7094 / 7095; IPC-CM-770D; IPC-MC-790; IPC-SM-780 / 784; J-STD-032; EIA-CB-11 | — | — | BTC, flip chip, BGA implementation; component mounting; MCM; SMT packaging; direct chip attach; BGA bumps; MLCC mounting | Appendix |
| IPC-7912; IPC-9191 / 9194 / 9199; IPC-9201; IPC-9251; IPC-9261; IPC-A-20/21, -24, -36, -38, -48; IPC-A-610; JEP-150; JESD51-3/-5/-7/-8/-9/-10/-11; J-STD-028; MIL-STD-883 | — | — | DPMO; SPC; SIR handbook; fine-line test vehicles; in-process DPMO; test patterns; assembly acceptability; stress-test qualification; thermal test boards; flip-chip bumps; microelectronics test | Appendix |
| IPC-5701; IPC-AC-62; IPC-CH-65; IPC-SA-61; IPC-SC-60 | — | — | cleanliness and cleaning | Appendix |
| JESD22-A113; JESD22-A111 / A112 / B102C / B105-B / B106 / B108 / B117; IPC-9501–9504; IPC-9850; IPC/JPCA-6801 | — | — | preconditioning; immersion, moisture-induced stress, solderability, lead integrity, TH soldering resistance, coplanarity, ball shear; process simulation and MSL for non-IC parts; placement equipment; build-up test methods | Appendix |
| IPC-2511–2518; IPC-2581; EIA-274-D and related NC standards | — | — | manufacturing data transfer | Appendix |
| IPC-T-50F; JEP99; JESD12-1; JESD77; JESD99; JESD100 | — | — | terms and definitions | Appendix |
| EIA-186-E; EIA-481-2-A; EIA-364-C; EIA-944/945; EIA/IS-47; JEP-95; JESD-30B; JESD-625A; component detail/qualification specs (capacitors, resistors, switches, sockets) | — | — | component test methods, tape & reel, connector tests, contact finishes, outlines, ESD handling | Appendix |

## 7. Process / lifecycle guidance

| Stage | Activity | Deliverable | Exit criterion | Source |
|---|---|---|---|---|
| Requirements | Measure the real use environment (thermocouples, humidity, accelerometers) incl. transport and storage; set design life and acceptable failure fraction | environment profile (T extremes, cycle rate, dwell, RH, shock/vibration) and reliability goal | goal stated per product class (CHECK-reliability-goal); all life phases counted | §60.2.5 (steps 1–2), §62.3.1, §63.2–63.3 |
| Architecture (flex) | Flex vs rigid + connectors + wires value analysis; split complex flex; rigid-flex only if flex + stiffener cannot do it | wiring architecture | value analysis done with fabricator | §65.1.2, §66.1, §69.2.1 |
| Design FMEA / FTA | Team FMEA from functional and reliability block diagrams; F × C × D = RPN; FTA for safety/permanent-damage modes | ranked FMEA worksheet | top 50% of modes by RPN actioned before design freeze | §58.1–58.3 |
| DFT | Access plan (bed-of-nails vs boundary scan), controllability/observability rules, JTAG chain, test-point layout for low strain | test strategy and access map | CHECK-ict-access, CHECK-jtag-hygiene, CHECK-ict-strain pass | §56, §57, §62.3.12 |
| Design for reliability | Four thermal-cycle levers; no mirrored BGAs; pad sizing; ViP/microvia rules; measured board properties; PTH AR/plating; CAF spacing; flex dynamic-zone rules | DfR review record | all §3 checks pass or have documented waivers | §60–§63, §66 |
| Accelerated test design | Failure modes → acceleration model per mode → conditions and sample size → failure analysis → transform life distribution | test plan (profiles §2.2–2.3), AF model | predicted field life ≥ goal with safety factor 2 | §60.2.5, §64.2.6 |
| Qualification | Board-level ATC (IPC-9701, two board thicknesses, first-level chains, back-side parts); bend/drop/shock; bare-board IST/HATS/AtA after 6× 260°C; solder float; CAF; SIR; STII screening | qualification report (Weibull, AF, failure analysis) | test failure mode = field mode; 1%-life lower bound ≥ requirement | §60.4.6, §62.3, §64.2–64.3 |
| Process development | P-FMEA; reflow profile control (IMC, cooling ramp); inspection system benchmark and 6-month implementation support (SPC first); production strain survey | P-FMEA, profile spec, SPC plan, strain map | strains below limit curve; SPC in control | §55.11, §58.3, §62.3.4.1, §63.4.3, §64.3.1.1 |
| Production | Test as a process monitor (resolve defects, not faults); SPI/AOI control charts; AXI on hidden joints; rework count per site logged | defect Pareto, yields, rework log | board post-test yield toward ≥ 99%; rework counts within PTH life budget | §55.8–55.10, §57.2, §60.3.4.6, §60.4.8 |
| Flex QA | Incoming raw-material tests; lot acceptance (visual, dimensional, electrical, cleanliness); periodic qualification; SPC | lot test data | §71 acceptance criteria met | §71 |
| Field / sustaining | Miner-based life accounting (power + mini-cycles); prognostics and health management; feed field returns into FMEA | reliability update | projected remaining life ≥ goal | §58.1, §60.4.8, §64.2.5–64.2.6 |

## 8. Coverage log

- Lines read: 1–200 (front matter, TOC through Ch. 64) in full; 201–400 (TOC remainder) viewed as preview only — chapter list for the range cross-checked against the chapter headings in the text; 12150–16033 read sequentially in 36 chunks of ≤ 27 KB (lines < 2.4 KB, nothing truncated); 16034–16154 is the book index — scanned for non-index content (none) and skipped.
- Chapters extracted: 55 (§55.8–55.13), 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, Appendix (standards summary, M. Carter) and Glossary. 319 rule rows (COOMBS-4001 … 4319).
- Skipped by design: reference lists, acknowledgments, the §61.3 acronym list, polyimide chemistry narrative, historical anecdotes (§56.1, §56.4), index.
- Extraction limitations: every table and figure in these chapters is an image and absent from the text (e.g. Tables 57.1–57.2, 58.1–58.3 FMEA rankings, 59.1–59.3, 60.1–60.7, 61.1–61.4, 62.1–62.3, 64.1–64.7, 65.x–70.x); values were taken only from prose and captions and graph-dependent rules are marked medium. Many equation bodies are missing (Ch. 59 Eqs. 59.1–59.16; Ch. 60 Coffin–Manson, Arrhenius, Weibull, IPL; Ch. 63 Eqs. 63.1–63.13 except worked numbers; Ch. 64 Eqs. 64.1–64.23; Ch. 66 microstrip, strip-line, capacitance, delay and crosstalk formulas); where a standard form is supplied it is labelled "standard form / body missing" with conf medium. The extraction renders µ as "m" in Ch. 70 and as "θ" in Ch. 69 — units interpreted and flagged. Figure numbering errors in the source (e.g. "FIGURE 54.4" inside Ch. 56; duplicated captions for Figs. 65.21–65.23) are ignored.
- Special-focus items not present in this range: Engelmaier solder fatigue-ductility constants (c, εf′); IPC-7711/7721 rework limits and procedures (title only, in the Appendix — rework guidance limited to §60.3.4.6 and §71.8.4); HALT/HASS conditions; numeric ICT/functional/boundary-scan coverage percentages (only the illustrative "test covers 90% of important defects" example, §57.2); flex bend-radius-vs-thickness rules (IPC-2223 not reproduced; only graph Fig. 66.18); RoHS/REACH/halogen-free ppm limits (only qualitative RoHS and bromine statements, §65.11, §69.3.2.7, Glossary). Ch. 50 (repair/rework) and Chs. 53–54 (acceptability) are in other agents' ranges.
- Review corrections applied after first pass: COOMBS-4044 (corrosion-factor form), 4112 (ambiguous preconditioning wording), 4117 (pad-tilt symbol), 4193 (mirrored life-ratio direction), 4215 (N-L constants provenance, verified 3.27 vs 3.2), 4216 (removed Pan constants not given in the text).
