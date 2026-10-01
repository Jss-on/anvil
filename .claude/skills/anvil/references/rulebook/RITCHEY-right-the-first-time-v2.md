# Right the First Time, Vol. 2 (Ritchey/Zasio) — Anvil rulebook

## 0. Citation

L. W. Ritchey and J. Zasio (BGA/package chapter), K. J. Knack (ed.), *Right the First Time: A Practical Handbook on High Speed PCB and System Design, Volume 2*, Speeding Edge, Fall 2006 (revised Jan. 29, 2007 version), copyright 2007. ISBN 0-9741936-1-5. LCCN 2003109272.

Chapters covered by THIS extraction (read in full and mined): Ch.1 Introduction; Ch.2 PCB design process; Ch.3 Power delivery details; Ch.4 PCB fabrication; Ch.5 PCB materials; Ch.6 Signal integrity and PCB structures; Ch.7 EMI/EMC; Ch.8 Gb/s and higher signalling; Ch.9 Simulation and simulators; Ch.10 IC package design (Zasio); Glossary; Appendices 1 (PCB materials), 2 (power system tests), 3 (generic PCB fabrication specification), 6 (standard drill chart), 7 (metric pad-stack tables), 8 (attaching scope probe grounds), 9 (conversions), 10 (drill size vs aspect ratio). See §8 for exact line ranges.

Chapters NOT mined: Appendix 4 (index to Vol.1) and Appendix 11 (index to Vol.2) are index pages (read, no rules). Appendix 5 (107 references) was read and used only to resolve reference numbers cited in rules. Volume 1, which this book cites throughout, was not available.

Key references the rules lean on (App.5 numbering): [10] D. Brooks, "90 Degree Corners, The Final Turn," Printed Circuit Design, Jan 1998; [13] T. Hubing et al., "Power Bus Decoupling on Multilayer Printed Circuit Boards," IEEE Trans. EMC 37(2), May 1995; [14] L. Ritchey, "Test Lab, Cuts in Power Planes and Soldermask Effects on Impedance," Printed Circuit Design, Jan 2000; [21] L. Smith et al., "Power Distribution System Design Methodology and Capacitor Selection for Modern CMOS Technology," 1999; [66] H. Chen et al., "Effects of 20H Rule and Shielding Vias on EMI in PCBs," UC Santa Cruz, May 2001; [84] G. Brist et al., "Non-classical Conductor Losses Due to Copper Foil Treatment," Circuitree, May 2005; [89] Speeding Edge Current Source newsletter Vol.1 Issue 4, Fall 2005 (ferrite-bead and 20H tests).

Page citations `p.NNN` are the printed page numbers ("Page NNN" stray lines in the text).

## 1. Design rules

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| RITCHEY-001 | transmission-line | A net is "high speed" (needs transmission-line management) when its length exceeds 1/4 of the electrical length of the driver rise/fall time; conservative limit 1/6. Clock frequency is irrelevant. | L_crit = tr * v / 4 (conservative tr * v / 6); v ~ 6 in/ns in PCB (er ~ 4) | tr (ns), trace length (in), er | All logic families. Simulation basis: 3.3 V CMOS, 50 ohm, Rs = 0, tr = 1 ns showed over-voltage starting at L = tr/12; experience sets 1/4..1/6 | calc | p.15-16, Figs 1.1-1.7 | high |
| RITCHEY-002 | transmission-line | 2006-era CMOS (tr = 0.2 ns; transitional electrical length TEL = 1.2 in / 3.6 cm) has a high-speed boundary of 0.3 in (0.9 cm) — shorter than package lead length — so ALL nets of such parts are high speed regardless of clock. | boundary = TEL/4 = 0.3 in | tr | 0.2 ns edges | calc | p.16 | high |
| RITCHEY-003 | termination | Receiver input must never exceed Vdd + 0.3 V (Schottky input-protection diodes begin conducting at 0.3 V; turning them on can cause logic failure). For 3.3 V logic max input = 3.6 V. | Vin_max = Vdd + 0.3 V | Vdd, simulated overshoot | CMOS inputs | sim | p.15 | high |
| RITCHEY-004 | termination | Unterminated 3.3 V CMOS driver (Rs = 0) on 50 ohm line, tr = 1 ns: receiver overshoot = 4.3 V for 12 in, 6 in and 3 in; 4.1 V at 1.5 in; 3.99 V at 0.75 in; 3.7 V at 0.5 in. Shortening only shortens the over-voltage duration until L < ~tr/12. | see values | line length, tr | HyperLynx LineSim, Virtex AGP driver model, 50.3 ohm line, 1.760 ns for 12 in | sim | p.15-16, Figs 1.2-1.7 | high |
| RITCHEY-005 | termination | Remedies for overshoot: terminate (series/parallel), shorten the line below the 1/4-tr boundary, or slow the edge (only possible with custom ASIC drivers or FPGA slew-rate-controlled outputs). Off-the-shelf parts must be terminated. | — | driver type | — | review | p.16-17 | high |
| RITCHEY-006 | crosstalk | Backward crosstalk grows linearly with parallel coupled length up to the "critical length", then saturates; more parallel run beyond it adds no backward crosstalk. Backward crosstalk is the first crosstalk to cause failures. | Xb proportional to L for L < L_crit; constant for L >= L_crit | coupled length, tr, er | — | sim | p.17, Fig 1.8 | high |
| RITCHEY-007 | crosstalk | Critical length for a 0.2 ns (200 ps) edge in er = 4 is roughly 0.75 in; runs this short already produce worst-case backward crosstalk, so crosstalk must be managed even in slow-clock products using fast parts. Fig 1.9 (graph): L_crit vs tr for er = 2, 3, 4; er = 4 curve ~8 in at tr = 2 ns; "LVDS edge rates" marked at the low-tr end. | L_crit(0.2 ns, er = 4) ~ 0.75 in | tr, er | — | calc | p.17-18, Fig 1.9 (graph) | medium |
| RITCHEY-008 | process | Every rule of thumb admitted to a rule set must pass five questions: (1) is there a problem? (2) what is it? (3) does the fix solve it? (4) does it create another problem? (5) is it the best solution? Most fail at question 1. | — | — | Applies to app-note advice (ferrite beads, split planes, guard traces...) | review | p.12 | high |
| RITCHEY-009 | process | Two rules of thumb named as harmful: ferrite beads in IC power leads; splitting ground planes to isolate imagined noise sources. | — | — | — | review | p.12 | high |
| RITCHEY-010 | process | Library models (footprints, IBIS, timing, thermal) must be built by technically qualified staff and checked by a second qualified person; IBIS models may need validation against hardware. Mirror-image footprint is the typical error. | — | — | Everything downstream depends on these | review | p.22 | high |
| RITCHEY-011 | process | Simulate one member of each net class (GbE, SPI-4, DDR...) with IBIS/SPICE driver+receiver models, proposed Z0 (almost always 50 ohm), clock/data rate and estimated lengths BEFORE schematic capture, to fix termination rules, worst-case voltage margins and loading/timing effects; reject drivers that cannot drive transmission lines. | — | IBIS models, Z0, lengths, rates | Step 3 of the virtual-prototyping flow | sim | p.22 | high |
| RITCHEY-012 | process | Signal-layer count is usually set by the highest-pin-count IC; estimate from similar prior designs or an experienced layout designer. | — | max IC pin count | — | review | p.22 | low |
| RITCHEY-013 | timing | Timing analysis must add interconnect delay from Manhattan (X+Y) length after placement; silicon-only timing is inadequate (example: worst-case silicon delay 3 ns vs wire delay 6 ns in a recent large system). | t_path = t_silicon + t_wire | placement, net list, propagation delay | Modern logic | calc | p.23-24 | high |
| RITCHEY-014 | process | Pre-route checks: net list error-free (no unwanted inter-net connections, no single-pin nets, matches schematic); no mechanical interferences; every transmission line has the correct termination at the correct location; every net has a driver and a load. | — | net list | Before routing | inspect | p.24 | high |
| RITCHEY-015 | process | Post-route checks: all nets routed; no contact with other nets or power/ground; length matching correct; spacing correct; clearances around component and mounting holes correct. Full-board post-route SI is "too late"; do SI up front; post-route SI only on a few critical nets. | — | routed database | — | inspect | p.26-27 | high |
| RITCHEY-016 | process | Technology-table rule set, one row per net class: class name; technology (GB DIFF, 3.3CMOS, LVTTL, PWR); SE/DIFF; frequency; quantity; impedance (50 ohm for every class); allowed layers; termination type (INT / SER / N/A); stub length (0 for all); trace width (from stackup); spacing in class; spacing to other classes; length-tune tolerance; route order. | — | — | Example Fig 2.3: 22-layer board; routing layers 2,5,6,9,10,13,14,17,18,21; layers 1 and 22 not routing layers | review | p.25, Fig 2.3 | high |
| RITCHEY-017 | crosstalk | Example spacings from Fig 2.3 (mils): Gb differential classes (10GE 9.6 Gb/s, 10GE CLK 4.8 GHz, XAUI 3.125 Gb/s, XAUI CLK 1.55 GHz, 1GE 1 Gb/s) 10 in-class / 20 to other classes; 3.3 V CMOS single-ended classes 6 in-class / 15 to other classes; the IFCLK (150 MHz clock) class 10/15. Differential-pair spacing is a minimum (members may be spaced wider). | — | class | Lengths in mils | inspect | p.25, Fig 2.3 | high |
| RITCHEY-018 | timing | Example length-tune tolerances (mils, ±) from Fig 2.3: 10GE and 10GE CLK 100; XAUI, XAUI CLK, 1GE 300; single-ended classes untuned (a trailing "200" in the extracted table cannot be assigned to a class). All Gb differential classes on layer 2 only, stub length 0, termination INT (on-chip). | — | class | — | inspect | p.25, Fig 2.3 | high |
| RITCHEY-019 | grounding | All ground planes tied together at every device ground pin. | — | — | Technology-table note | inspect | p.25, Fig 2.3 | high |
| RITCHEY-020 | process | Fabrication/assembly data package: film (Gerber) for every layer; bare-board test net list (IPC-356); fabrication drawing; NC drill files and drill reports for plated and non-plated holes; soldermask and silkscreen artwork; aperture list; final BOM; pick-and-place; engineering contact. Archive two copies, one off-site. | — | — | Steps 19-20 | inspect | p.27; p.46 Table 4.1 | high |
| RITCHEY-021 | pdn | PDS ripple = load current x PDS impedance; both frequency dependent. Design Zps(f) so ripple stays within the circuit limit across the load spectrum. | Vripple(f) = Iload(f) * Zps(f) | Iload spectrum, ripple spec | All rails | calc | p.28, Fig 3.1 | high |
| RITCHEY-022 | pdn | The largest PDS transient is a wide single-ended bus switching 0->1 simultaneously; it is also the most frequent cause of EMI and intermittent failures. Size the PDS for it. | — | bus width, Z0, V | Single-ended parallel buses | calc | p.28 | high |
| RITCHEY-023 | pdn | Current drawn to charge a series-terminated line: I = V/(2*Z0) for one round-trip delay (2 x line delay). | I = V/(2*Z0); duration = 2*t_pd*L | V, Z0, t_pd, L | Example: Zout 25 ohm, Rs 25 ohm, 5 V, 50 ohm 2.0 ns/ft, 12 in | calc | p.28-29, Figs 3.2-3.3 | high |
| RITCHEY-024 | pdn | Spectrum of the line-charging current is not at clock harmonics: lowest frequency set by the pulse length (line length), highest by rise/fall time. Example 30 MHz clock, 12 in line: spectrum from a little below 100 MHz to ~900 MHz. Product EMI spectra look like this because inadequate PDS decoupling puts this current shape on Vdd and every wire held at logic 1 radiates it. | — | line length, tr | — | sim | p.29-30, Fig 3.4 (FFT of line current in SI tool) | high |
| RITCHEY-025 | pdn | Parasitic inductance degrades the PDS far more than resistance. Via inductance ~36 pH per mil of length (Vol.1 Eq 35.1); in thick boards via inductance dominates the capacitor path, so premium low-inductance capacitors are usually not worth it. | L_via ~ 36 pH/mil x length(mil) | via length | Thick boards, plane pairs distributed through stackup | calc | p.30 | high |
| RITCHEY-026 | stackup | Assign the plane pair that feeds the parallel data buses to the first two planes below the surface (minimizes via inductance for capacitors and IC pins); keep each power/ground pair close together to minimize plane inductance. | — | stackup | — | inspect | p.30 | high |
| RITCHEY-027 | pdn | PDS capacitance lives in five places: IC die, IC package, PCB plane pairs, discrete capacitors, power-supply output. Start from the target impedance implied by the ripple limit, then compute values/quantities (spreadsheet, SPICE, or 2D plane field solver). | — | — | — | calc | p.30-31 | high |
| RITCHEY-028 | decoupling | Spreadsheet (parallel-impedance) method ignores parallel resonances between capacitor ESL and plane capacitance; SPICE shows them; measurement matches SPICE up to ~200 MHz, above which plane resonances (2D plane modelling needed) dominate. | — | cap C/ESR/ESL/qty, Cplane | — | sim | p.31-33, Figs 3.5-3.9 (confirm by measurement) | high |
| RITCHEY-029 | decoupling | PDS capacitors are ±15% or worse; the target impedance must be adjusted for this; with lossy X5R/X7R parts the resonance effects are small enough that the spreadsheet method works for most problems. | — | tolerance | X5R/X7R | calc | p.33 | high |
| RITCHEY-030 | decoupling | SPICE PDS model per capacitor value: C = n x C_each; ESL = ESL_each/n; ESR = ESR_each/n; mounting L = L_mount_each/n; drive with a 1 A variable-frequency sine so 1 mV = 1 mohm; Lplane and Rplane negligible for real PCBs. | Z(f) = V(f)/1 A | per-cap C, ESR, ESL, L_mount, n | — | sim | p.32, Fig 3.7 | high |
| RITCHEY-031 | decoupling | Estimate plane capacitance needed to support simultaneous switching (when the IC has no appreciable on-die I/O capacitance): dV ~ (Sum_Cswl/Cplane) x V -> Cplane >= V x Sum_Cswl / dV. Crude but conservative in the author's dozens of uses. | Cplane = V * Sum_Cswl / dV; dV = allowable ripple (V); V = supply (V); Sum_Cswl = sum of parasitic capacitance of simultaneously driven lines (F) | ripple spec, supply, line capacitances | Prefer a PDS field-solver tool when available | calc | p.33-34, Figs 3.10-3.11 | high |
| RITCHEY-032 | pdn | Ferrite beads in IC power leads (incl. PLL, serdes, "analog" rails): VERDICT = do not use. They raise PDS impedance over 30 MHz-1 GHz (the EMI test band and the band the part needs); a 3.125 Gb/s serdes output measured worse with the vendor-recommended bead than with the lead tied directly to Vdd. Author: never used one in 30+ years; all products passed EMI/ESD. | — | — | Any bead recommendation must pass RITCHEY-008; demand the vendor's test circuit; be suspicious if none exists | measure | p.34-38, Figs 3.13-3.18 | high |
| RITCHEY-033 | pdn | Bead + capacitor + Vdd-plane island under an ASIC/transceiver (Fig 3.16): VERDICT = do not use. Deprives the part of plane capacitance; high probability of EMI and logic failure from excess ripple. | — | — | 130 nm-class and faster logic | review | p.36, Fig 3.16 | high |
| RITCHEY-034 | decoupling | Do not use very-low-ESR capacitors in the PDS: 1 uF 0603 with 20 mohm ESR against 10 nF plane capacitance gives a 20 mohm minimum at 3.5 MHz but a 10 ohm parallel-resonance peak at 35 MHz; ESR 100 or 400 mohm suppresses the peak (can be made zero). Hit the target with more lossy caps in parallel (20 x 400 mohm caps for 20 mohm). | n = ESR_each / Z_target | ESR, n, Cplane | — | sim | p.38, Fig 3.19 | high |
| RITCHEY-035 | components | Ceramic dielectrics: C0G/NP0 (mil BP) ultra-stable, lowest loss — not for PDS; X7R (mil BX/BR) ±15%; X5R ±15%; Z5U +22/-56%; Y5V +22/-82%. Y5V: at 16% of rated voltage capacitance is halved; at 50% of rated voltage only 10% remains; worse with temperature — avoid. | — | dielectric code, V/V_rated | — | inspect | p.38-39, Fig 3.20 | high |
| RITCHEY-036 | derating | X5R: ±15% over -55..+85 C; X7R: ±15% over -55..+125 C. Product operating much above 25 C -> X7R is the only logical choice. | — | operating temperature | — | inspect | p.39 | high |
| RITCHEY-037 | power | DC-DC converter output impedance is flat at its regulated value only to ~100 Hz (quarter-brick at full load: 1 mohm -> 1 mV per 1 A step); above that it is a voltage source in series with an inductance. Extract L from the curve: L = Z/(2*pi*f) (example 10 mohm at ~3000 Hz -> 1.6 uH); mounting adds more. | X_L = 2*pi*f*L | measured Z(f) | Output cap 42 uF vs 2147 uF gave identical curves to ~4 kHz | measure | p.39-40, Figs 3.21-3.22 | high |
| RITCHEY-038 | power | Vendor impedance curves can overstate regulation bandwidth (claimed sub-mohm to 5 kHz; measured roll-off at 100 Hz; inferred L 5x too small). Load-test every new DC-DC converter, else an impedance gap 100 Hz-3 kHz remains (needs very large capacitors); risky with cores going standby->active under software. | — | — | — | measure | p.40 | high |
| RITCHEY-039 | power | Synqor 100 A converter: 1 mohm at ~2 kHz -> 80 nH; impedance dips to 40 uohm below that (typical of very high-power converters). | L = 1e-3/(2*pi*2e3) | — | — | measure | p.41, Fig 3.23 | high |
| RITCHEY-040 | test | PSU Z(f) test: square-wave generator drives Q1 through R2; sense resistor R1 sized to develop ~1/10 of the output voltage at maximum rated load; set amplitude for rated load current; sweep frequency; read ripple at the output terminals; Z = Vripple/Iload. Keep the R1-Q1-converter loop L and R low. | Z(f) = Vripple(f)/Iload(f) | — | Dual-trace scope | measure | p.41-42, Fig 3.24 | high |
| RITCHEY-041 | components | Extract C, ESR, ESL from a capacitor impedance curve: C from the left slope, ESL from the right slope, ESR at the minimum. 10 nF X7R 0603 (AVX SpiCap): 8 ohm at 2 MHz -> ~10 nF; 10 ohm at 3 GHz -> 0.5 nH; ESR ~100 mohm at resonance. ESR varies with frequency but may be held constant for PDS calcs. | X_C = 1/(2*pi*f*C); X_L = 2*pi*f*L | Z(f) | — | calc | p.42, Figs 3.25-3.26 | high |
| RITCHEY-042 | decoupling | Mounting-pad + via inductance is commonly larger than the capacitor ESL and shifts the useful frequency down; include both in the model (Vol.1 pp.142-143 tabulate pad inductances). | L_total = ESL + L_pads + L_vias | — | — | calc | p.42 | high |
| RITCHEY-043 | pdn | Plane capacitance has the lowest inductance of any PDS capacitance and is the only element supporting switching currents above ~200 MHz, where discrete capacitors have ceased to work. | — | separation, area | — | calc | p.43-44 | high |
| RITCHEY-044 | pdn | Plane capacitance vs dielectric thickness (Fig 3.27, er 4.1 nominal for high-layer-count laminates, graph labelled er = 4.0): C[pF/in^2] = 224.9 x er / t[mil] (parallel-plate, derived; ~922/t for er = 4.1). Curves: solid, 85%, 70% copper remaining (holes); 70% = very high component density. | C = 224.9*er/t (pF/in^2; t in mil) | er, t, fill fraction | 0-20 mil plotted; ~400 pF/in^2 at the thinnest plotted | calc | p.43, Fig 3.27 (graph; formula derived) | medium |
| RITCHEY-045 | pdn | Prefer plane capacitance from pairing existing planes across thin laminate/prepreg (no cost premium) over specialty capacitive laminate (e.g., Sanmina ZBC). | — | — | — | review | p.43 | high |
| RITCHEY-046 | pdn | When extra planes are impossible, flood unused signal-layer area with copper tied to the rail OPPOSITE the adjacent plane (fill beside Vdd plane -> ground; beside ground plane -> Vdd). PCMCIA 6-layer example: inter-plane C 500 pF -> 4000 pF fixed EMI (all failing frequencies > 200 MHz) and logic flakiness. | — | layer adjacency | L1 sig/L2 Vdd/L3 sig/L4 sig/L5 GND/L6 sig; L1,L3 fill -> GND; L4,L6 fill -> Vdd | inspect | p.43-44, Figs 3.28, 7.12 | high |
| RITCHEY-047 | stackup | Four-layer 50-60 mil boards (sig/Vdd/GND/sig, 5-6 mil signal-to-plane) put the planes >= 40 mil apart -> negligible plane capacitance; high-frequency switching then relies on on-die/on-package capacitance, and signals must stay on one layer point-to-point (no low-inductance plane-to-plane return path). | — | — | 4-layer boards | review | p.44 | high |
| RITCHEY-048 | fab | Net-list compare (net list synthesized from Gerber vs CAD net list) is the mandatory first tooling step; no work proceeds until differences are resolved. | — | Gerber, CAD net list | — | inspect | p.46 | high |
| RITCHEY-049 | fab | Specify trace widths and laminate styles/thicknesses for every controlled-impedance layer yourself (fabs otherwise build different boards from the same film). Specify DRILL size, not finished hole size, in the drill chart. | — | — | Controlled impedance, fine pitch | inspect | p.48 | high |
| RITCHEY-050 | materials | Copper foil: 1 oz/ft^2 = 1.4 mil = 36 um; 1/2 oz = 0.7 mil = 18 um. | t(mil) = 1.4 x oz | oz | — | calc | p.49 | high |
| RITCHEY-051 | fab | Do not pumice-scrub copper thinner than 1 oz (micro-scratches open 1/2 oz traces); use chemical micro-etch (removes < 0.1 mil). | — | copper weight | — | review | p.49 | high |
| RITCHEY-052 | fab | Never put two copper weights on opposite sides of one laminate detail: the thick side sets etch time and the thin side over-etches; width control becomes inadequate for controlled impedance. Same weight both sides. | — | stackup | Controlled impedance | inspect | p.50 | high |
| RITCHEY-053 | fab | Inner-layer etched trace-width accuracy on a well-managed line: ±0.5 mil in 1/2 oz; ±1.0 mil in 1 oz. Thicker copper needs wider spaces for etchant access; fine lines/spaces are built on thin copper. | ±0.5 mil (1/2 oz); ±1.0 mil (1 oz) | copper weight | — | inspect | p.50 | high |
| RITCHEY-054 | fab | Cross-hatched planes are unnecessary (black-oxide / alternative-oxide treatments solve adhesion); use solid planes. | — | — | — | review | p.51 | high |
| RITCHEY-055 | fab | Foil lamination is cheaper than cap lamination (one fewer detail); use cap lamination only for L1-L2 blind vias without laser/controlled-depth drilling, or for a specialty laminate (e.g., Rogers 4350) between L1 and L2. | — | — | — | review | p.51-52 | high |
| RITCHEY-056 | fab | Boards laminated several per press opening need a rigid (stainless-steel) separator; flexible separators cause thickness variation across large BGAs -> soldering difficulty and short BGA life. | — | — | High layer count | review | p.52 | high |
| RITCHEY-057 | fab | Drill true position of ±5 mil (±127 um) on an 18 x 24 in panel needs post-lamination x-ray drill optimization (or Truedrill) plus post-etch punch; fabs without these cannot hold tight tolerances. | drill TP <= ±5 mil | — | High density | review | p.54 | high |
| RITCHEY-058 | fab | Electroless copper is brittle and serves only as the plating seed; hole-wall thickness must be electrolytic copper. Pattern plating (not panel plating) is required for fine-pitch SMT pad-width control. | — | — | — | review | p.55 | high |
| RITCHEY-059 | fab | Plating thieving (dummy pads) evens plating current/hole copper across the panel; thieving must NOT be placed over controlled-impedance traces on layer 2 / n-1, or the fab notes must state where thieving is and is not allowed. | — | — | Outer layers over controlled-impedance buried microstrip | inspect | p.56 | high |
| RITCHEY-060 | fab | High-aspect-ratio holes plate "dog-bone" (thin at mid-barrel) with DC plating; specify/verify reverse-pulse plating (RPP) for uniform barrel copper. | — | aspect ratio | High aspect ratio holes | review | p.56 | high |
| RITCHEY-061 | dfm | Silkscreen letter sizes and line widths must stay within the screening-process limits (or use photo-imageable legend). | — | — | — | inspect | p.57 | low |
| RITCHEY-062 | via | Definitions: blind via = starts on a surface, does not pass through; buried via = between inner layers, touches neither surface; microvia (IPC) = via of diameter <= 8 mil (203 um) whether or not it passes through. Do not call every blind via a microvia. | d_microvia <= 8 mil | — | — | review | p.58 | high |
| RITCHEY-063 | via | Blind-via formation cost ranking: controlled-depth mechanical drill (cheapest, no extra steps; hole must be large enough for a mechanical drill and area under the hole kept clear of circuits) < laser (excimer/UV drills copper+dielectric in one step; CO2 needs a copper pre-etch and has a mask-alignment problem) < photo-defined (same cost for one or thousands; not available in the US as of 2006) < sequential lamination (most costly, thin-laminate yield loss; last resort). | — | — | — | review | p.59-60 | high |
| RITCHEY-064 | via | Blind-via plating limit: hole diameter must be >= hole depth (aspect ratio <= 1:1); many fabricators require diameter >= 1.5 x depth. This usually precludes blind vias below layer 2, so all fine-pitch pins must be reachable on layer 1 or layer 2 (others fanned out to through-holes). | d_blind >= depth (fab-typical: d >= 1.5 x depth) | via diameter, depth | Laser / controlled-depth / photo-defined vias | calc | p.60 | high |
| RITCHEY-065 | assembly | Blind via centred in a BGA pad traps air under the paste; the bubble rises to the top of the ball and causes thermal-cycle opens. Either fill the via with plated copper (button plating, sanded flush) or offset the via to the side of the pad; a bubble not directly under the ball is harmless. Stacked unfilled vias must be offset from each other. | — | — | Via-in-pad BGA | inspect | p.60-61, Figs 4.29-4.30 | high |
| RITCHEY-066 | via | Via parasitic capacitance scales with barrel outer area (drill diameter x board thickness); blind vias cut both length and diameter and are recommended for signal paths above 4.8 Gb/s. | C_via proportional to d_drill x t_pcb | drill, thickness | > 4.8 Gb/s | calc | p.61 | high |
| RITCHEY-067 | fab | Build-up construction: core of up to 8 layers (planes + some signals) built conventionally, through-holes plugged with resin or conductive epoxy, then one prepreg ply + foil per side laminated and laser/blind-via processed per added layer pair. Needed when lead pitch is ~25 mil (0.6 mm) with parts on both sides (cell phones) and for high-pin-count BGA substrates. | — | — | — | review | p.61-63, Fig 4.31 | high |
| RITCHEY-068 | assembly | Surface finish verdicts: electroplated gold over electroplated nickel = lowest-risk, author's only choice for expensive boards; HASL = OK but non-uniform on fine pitch (QFP/BGA shorts), thermal shock can fail small PTHs in thick boards, not RoHS; ENIG = good only with tightly controlled chemistry (black-pad risk, undetectable until after assembly); OSP (Entec 106) = single-sided assemblies only; immersion silver = consumer-only (tarnishes on press-fit holes/test points within months, second-side corrosion); electroplated tin and immersion tin = NEVER (tin whiskers -> shorts/leakage in the field); electroplated solder = lead content, mask-over-solder failures. | — | finish | — | review | p.63-66 | high |
| RITCHEY-069 | assembly | Gold thickness over nickel: specify no more than 10 uin (0.25 um) gold (>= ~5% gold dissolved in the joint embrittles it) and a minimum of 5 uin (printed "12 microns"; 0.12 um intended). Nickel is the mandatory barrier (gold on bare copper alloys and corrodes). | 5 uin <= Au <= 10 uin | — | Electroplated Au/Ni | inspect | p.64 | high |
| RITCHEY-070 | fab | With electroplated Au/Ni as etch resist on small high-aspect holes, poorly controlled nickel may leave mid-barrel copper unprotected and partially etched (passes bare-board test, fails after soldering). Require the fab to plate extra copper in the holes or plug vias with photo-imageable material before outer-layer etch. | — | — | Au/Ni finish, high AR holes | review | p.64 | high |
| RITCHEY-071 | assembly | OSP (Entec 106) limits: destroyed by finger contact, short shelf life, insulating (blocks test probing), second-side coating degrades while the first side is soldered -> use only on single-sided assemblies. | — | — | — | review | p.65 | high |
| RITCHEY-072 | process | Select a fabricator that demonstrates control of the chosen finish process and monitor it continually; PCB failures from wrong finish are only fixed by scrapping assemblies. | — | — | — | review | p.63 | high |
| RITCHEY-073 | materials | Glass-cloth nominal thicknesses: 106 ~1.5 mil (38 um); 1080 ~2.5 mil (63 um); 2113 ~2.9 mil (75 um); 3313 ~3.2 mil (printed 102 um); 2116 ~3.8 mil (97 um); 1652 ~4.5 mil (115 um); 7628 ~6.5 mil (165 um). Ultrathin styles for high performance, coarse for low cost. | — | glass style | — | inspect | p.67 | high |
| RITCHEY-074 | materials | Glass-weave effect: a trace over glass bundles sees er ~6, between bundles er ~3; impedance varies by as much as 5 ohm along the trace -> jitter and skew on high-rate signals. Occurs with thin 1080 as well as coarse 7628. (Solution in Ch.5: spread-glass / 3313 style, angled routing.) | dZ0 up to 5 ohm | glass style | 5 mil trace example | measure | p.68, Fig 4.40 (TDR) | high |
| RITCHEY-075 | stackup | Finished copper for stackup/impedance design: use 0.6 mil for 1/2 oz (actual 0.5-0.6 mil after cleaning) and 1.2 mil for 1 oz. Industry uses 1/2, 1 and 2 oz foils; 1 oz most common. | t(1/2 oz) = 0.6 mil; t(1 oz) = 1.2 mil | — | — | calc | p.68 | high |
| RITCHEY-076 | stackup | Outer layers (1 and n) are not used for controlled impedance: crowded with mounting structures, and plating thickness varies up to 3:1 across the panel -> impedance variation up to 20%. Reserve them for component mounting and non-critical traces; the noise budget must allow the wider variation. | dZ0 up to 20% on outer layers | — | — | review | p.69, p.73 | high |
| RITCHEY-077 | stackup | Buried microstrip (layer 2 / n-1, plane on one side only) is electrically as good as stripline and is not an EMI source; the myth that outer/near-surface signal layers cannot carry high-speed signals is false. | — | — | — | review | p.70 | high |
| RITCHEY-078 | stackup | Preferred 10-layer arrangement (foil lamination; layer numbers reconstructed from the text and the 22-layer example): L1 mount / L2 sig / L3 GND / L4 PWR / L5 sig / L6 sig / L7 PWR-or-GND / L8 GND / L9 sig / L10 mount; laminate pairs (2,3) (4,5) (6,7) (8,9); every signal layer mated to a plane across a LAMINATE (core); plane pairs (3,4) and (7,8) mated across thin PREPREG (as little as 2.5 mil) for plane capacitance; signal pair (5,6) and the outer openings adjusted with prepreg. Preferred over the all-stripline alternative because it has two plane-capacitor pairs. | — | — | — | inspect | p.69-70, Fig 4.42 | high |
| RITCHEY-079 | stackup | Signal-to-plane spacing must be a laminate (core) thickness, never prepreg: prepreg compresses unpredictably during lamination (resin flows into copper voids) so height above plane — the dominant impedance dimension after trace width — cannot be held. Fab can pre-measure laminate and reject out-of-tolerance sheets. | — | — | Controlled impedance | inspect | p.70, Fig 4.43 | high |
| RITCHEY-080 | crosstalk | Adjacent signal layers between two planes (dual stripline / signal pair) must be routed orthogonally: one layer X, the other Y. Done this way there is no detectable inter-layer crosstalk, and only same-layer edge-to-edge spacing governs crosstalk. Requires roughly equal X and Y wire load (true of most daughter cards). | — | routing direction per layer | Dual-stripline pairs | inspect | p.70 | high |
| RITCHEY-081 | stackup | Backplanes (wire load predominantly one direction) must use single-stripline stackups (each signal layer between two planes) to avoid broadside coupling; plane capacitance is lost but backplanes usually have no circuits needing it (add extra planes if they do). | — | — | Backplanes | review | p.70-71, Fig 4.44 | high |
| RITCHEY-082 | stackup | Signal-layer copper: 1/2 oz is sufficient for impedance and skin-effect loss (verified by simulation/measurement) and gives ±0.5 mil (12 um) width control; make plane copper the same weight (1/2 oz) — adequate for all but the largest power devices (three terabit routers, 7 kW at 2.2 V and 1.8 V, used 1/2 oz planes). Guideline: make all copper layers 1/2 oz. | — | — | Check plane DC drop per Vol.1 Ch.33 for very high current | calc | p.71, p.79 | high |
| RITCHEY-083 | stackup | Set signal-to-plane height as thin as reasonably manufacturable: 5 mil for most fabricators, 4 mil for top-tier fabricators. This dimension (with edge-to-edge spacing) also sets maximum crosstalk. | h = 5 mil (typical fab); 4 mil (best fab) | fab capability | — | inspect | p.71 | high |
| RITCHEY-084 | materials | er depends on resin content (glass:resin ratio) and on frequency (drops with frequency); the exact laminate construction chosen for each opening must be named on the fabrication drawing, otherwise a second fabricator will build a different impedance. | — | construction, resin %, f | See Table 4.2 (§2) | inspect | p.72 | high |
| RITCHEY-085 | stackup | Frequency at which to take er for impedance calculation: for 300 ps edges the equivalent frequency is about 1.8 GHz (confirmed by measured boards). | f_equiv(300 ps) ~ 1.8 GHz | tr | — | calc | p.72 | high |
| RITCHEY-086 | stackup | Prepreg is available in the laminate thicknesses up to about 6 mil; thicker prepreg openings are built from combinations of thinner plies. | — | — | — | review | p.72 | high |
| RITCHEY-087 | process | Have one or two capable fabricators' engineering teams review the proposed stackup for manufacturability, then FREEZE it (lets the fab order materials early). | — | — | — | review | p.72 | high |
| RITCHEY-088 | stackup | To reach the final board thickness, add dielectric only in the openings that barely affect impedance: between L1-L2, Ln-1 - Ln, and between the two signal layers of a signal pair (L5-L6 in the 10-layer); then recheck every layer's impedance and fine-tune widths. | — | — | — | calc | p.73 | high |
| RITCHEY-089 | stackup | To add routing layers, duplicate the middle four-layer block (plane / sig / sig / plane): 10 -> 14 -> 18 -> 22 -> 26 layers, each step adding two planes and two signal layers. | N = 10 + 4k | — | — | inspect | p.73 | high |
| RITCHEY-090 | stackup | Plane assignment: every plane pair = one ground + one voltage; all grounds tied together at every ground pin; the first plane below the surface on EACH side is ground (keeps Vdd noise off component pads); with many pairs, never put two power planes back-to-back; choose assignments so signal-layer copper fills maximize plane capacitance. | — | — | 14+ layers | inspect | p.73 | high |
| RITCHEY-091 | stackup | Below 10 layers either impedance control or plane capacitance is compromised; use signal-plane fill; a 4-layer board has no plane capacitance -> accept high Vcc ripple/EMI or move plane capacitance into IC packages / plug-in cards. | — | — | 4-8 layer boards | review | p.73 | high |
| RITCHEY-092 | stackup | Minimum plane-to-plane dielectric: never a single ply of 106 (plane-to-plane shorts under lamination pressure); a single 1080 ply often shorts too; a single 2113 ply is proven -> final separation 3.4 mil (85 um); 2 x 106 also gives ~3.4 mil at higher cost. Specify minimum plane separation 3.4 mil. Bellcore GR-78-CORE requires >= 4 mil (100 um) between planes of different voltages. | t_plane_min = 3.4 mil (GR-78-CORE: 4 mil) | prepreg style | — | inspect | p.74 | high |
| RITCHEY-093 | stackup | Stackup drawing must name, for every opening: material type (e.g., FR-408), construction (e.g., 1 x 3313 Rc = 53.8%; 2 x 106 ULRC Rc = 63.3%), er at ~2 GHz unpressed and pressed, unpressed and pressed thickness, copper thickness/weight per layer, SE trace width and impedance and differential width per signal layer. Nothing is left to the fabricator. | — | — | See Fig 4.45 transcription (§2) | inspect | p.74-76, Fig 4.45 | high |
| RITCHEY-094 | crosstalk | Note from the 22-layer stackup: single-ended traces kept at least 25 mil from each other and from differential traces. | s >= 25 mil | — | 22-layer processor card, 3313 glass, 5 mil h | inspect | p.75, Fig 4.45 | high |
| RITCHEY-095 | transmission-line | Impedance-predicting equations are curve fits with limited sweet spots; the field-solver comparison (t = 1.4 mil, h = 5 mil, er = 4, w = 4-10 mil) agreed well only for the stripline equation and poorly for surface and buried microstrip. Always use a 2D field solver for stackup impedance. | — | w, h, t, er | — | calc | p.77-78, Figs 4.46-4.48 | high |
| RITCHEY-096 | transmission-line | Solder mask lowers surface-microstrip impedance and must be included in outer-layer impedance calculations; it has little effect on buried microstrip and none on stripline. | — | — | — | calc | p.78 | high |
| RITCHEY-097 | stackup | Stackup design steps: (1) number of signal layers to route; (2) planes as partners for every signal layer; (3) arrange signal/plane pairs; (4) mate planes for the plane-capacitance goal; (5) set height above plane for the crosstalk goal; (6) set width for impedance; (7) set the signal-pair and near-surface openings for total thickness; (8) verify manufacturability with a good fabricator. Guidelines: signal mated to plane across laminate; planes mated across thinnest possible prepreg; same copper both sides of each laminate; all 1/2 oz. | — | — | — | review | p.78-79 | high |
| RITCHEY-098 | test | Bare-board connectivity test against the CAD net list (IPC-D-356 with XY locations), not the CAM/Gerber net list; flying probe for small lots or pitches too fine for bed-of-nails; bed-of-nails for volume. | — | — | — | inspect | p.79 | high |
| RITCHEY-099 | test | TDR edge rate changes the measured impedance (er falls with frequency -> Z rises with faster edges): 40 ps (Agilent) vs 125 ps (Tek 1502C) vs 175 ps (Polar CITS800) gave L1 55.1/53.9/53.0 ohm; L8 57.4/56.5/52.6; L11 54.7/53.2/52.8 (~4% Agilent-vs-Polar). All parties must use the fab's production tester (Polar CITS800) or match its rise time. | see Table 4.3 | TDR tr | — | measure | p.81-82, Table 4.3 | high |
| RITCHEY-100 | test | Read impedance at the START of the test trace (cursor just after the probe-contact transient), not the average along the trace: series DC resistance makes the TDR trace slope upward (3 in lines read ~50 ohm at the left end and ~55 ohm at the right against ±10% limits), enough to reject in-spec lots. Polar testers report the average (impedance + DC resistance) and mislead. | — | — | — | measure | p.82-83, Fig 4.53 | high |
| RITCHEY-101 | test | OEM receiving inspection of bare boards: (a) impedance on the built-in test traces; (b) layer order via stacking stripes under a microscope; (c) plane capacitance of each rail with a capacitance meter across labelled Vdd/GND test contacts. | — | — | — | measure | p.83 | high |
| RITCHEY-102 | test | In-circuit-test access via: a via with drilled diameter <= 12 mil (300 um) adds ~0.3 pF and has no adverse effect up to 5.2 Gb/s if placed anywhere ALONG the net; any short escape trace to reach a via must be at one END of the trace (otherwise it is a stub). A 35-40 mil (0.8-1 mm) round test pad adds far less than 0.3 pF and is harmless unless it creates a stub. | C_via(<= 12 mil drill) ~ 0.3 pF | drill, position | <= 5.2 Gb/s | inspect | p.83-84 | high |
| RITCHEY-103 | test | Dense double-sided assemblies without through-vias for probing must include boundary scan (JTAG) on every IC; design the JTAG tests so field/depot repair uses the same suite. | — | — | — | review | p.84 | high |
| RITCHEY-104 | test | Three test structures belong INSIDE every high-speed PCB body (not on a separable coupon): one impedance test trace per controlled-impedance layer, plane-pair access points per rail, stacking stripes. Coupons can have different trace widths than the board and are usually separated/lost. | — | — | — | inspect | p.84-85 | high |
| RITCHEY-105 | test | Impedance test trace design: same width as the layer's signal traces; length >= 3 in (may be bent); signal via to its ground via spacing = 100 mil (2.54 mm); drill diameter 30 mil (0.76 mm) for standard probes; ground vias connected to all ground planes; access at both ends is optional; label each trace's layer number in silkscreen; provide differential versions for differential layers. Four traces may share one central ground via. | L >= 3 in; via pitch 100 mil; drill 30 mil | — | — | inspect | p.85-86, Figs 4.56-4.57 | high |
| RITCHEY-106 | test | The TDR ground contact may be tied to ANY continuous plane in the board (all planes are shorted at TDR frequencies by inter-plane capacitance and component ground vias); measured impedance is identical regardless of which plane is used. | — | — | — | measure | p.86 | high |
| RITCHEY-107 | test | Plane-access test structure: two per supply voltage, >= 1 in (2.54 cm) apart, labelled with the voltage; capture pad 44 mil square (voltage) or round (ground); plane clearance 50 mil; drill 30 mil; hole-to-hole 75 mil (1.9 mm); no thermal reliefs; one point injects the signal, the other measures the voltage (PDS impedance measurement). | — | — | — | inspect | p.86-87, Fig 4.58 | high |
| RITCHEY-108 | test | Stacking stripes: copper strip 50 mil wide x 50 mil long on L1, each lower layer 50 mil longer (staircase), plotted 25 mil inside and 25 mil outside the routed board edge so the copper edge is exposed; plus a 5 mil wide x 50 mil long trace segment seen end-on to measure etched width; stripes must not touch any internal copper — indent planes >= 0.020 in from the stripe. Gives layer order, copper and dielectric thicknesses and etch factor without destructive sectioning. Satisfies "no exposed copper" rules because the stripes are isolated from all circuits. | — | — | — | inspect | p.86-88, Fig 4.59 | high |
| RITCHEY-109 | dfm | Overlapping plane clearances (anti-pads) of closely spaced holes form slots in every plane -> severe SI damage, and no room to route between pins. Pad stacks must be co-designed by SI and manufacturing. | — | hole pitch, clearance | Fine-pitch BGA fields | inspect | p.89, Fig 4.63 | high |
| RITCHEY-110 | dfm | Minimum insulation between hole plating (hole shadow) and any plane/trace copper: 5 mil for most products; 4 mil (printed "10.2 mm"; 0.1 mm) for Telco equipment under Bellcore GR-78-CORE. | ins >= 5 mil (GR-78-CORE: 4 mil) | — | — | calc | p.91 | high |
| RITCHEY-111 | dfm | Drill wander (TIR): best fabricators ±5 mil; US middle tier ±6 mil; average high-volume Asian consumer fabs ±7 mil. TID (total included diameter) = 2 x TIR. Pad stacks must be designed for the fab that will build the volume boards. | TID = 2 x TIR; TIR = 5/6/7 mil | fab tier | — | calc | p.92 | high |
| RITCHEY-112 | dfm | Thermal ties (thermal reliefs) are needed only on through-hole leads soldered into plane-connected holes; two spokes are sufficient when hole spacing is correct; do NOT use thermal reliefs on SMT pads. | — | — | — | inspect | p.92 | high |
| RITCHEY-113 | dfm | Dimension pad stacks from the DRILL size, and list drill size (not finished hole) in the drill chart. For finished-hole requirements (press-fit) add the plating allowance: typically 2 mil per side -> drill = finished hole + 4 mil (100 um). | d_drill = d_finished + 4 mil | finished hole | — | calc | p.93-94 | high |
| RITCHEY-114 | dfm | Reference pad stack, 100+ mil thick board, 50 mil (1.27 mm) BGA, top-tier fab (TID 10 mil): drill 12 mil (smaller drills plate unreliably at this thickness); hole shadow = 12 + 10 = 22 mil; plane clearance = 22 + 2 x 5 = 32 mil; plane web = 50 - 32 = 18 mil -> two 5 mil traces with 5 mil space fit. With a 2 mil annular ring: capture pad 26 mil; signal-layer gap = 50 - 26 - 10 = 14 mil -> two traces still fit. | shadow = drill + TID; clearance = shadow + 2 x ins; web = pitch - clearance; pad = shadow + 2 x AR | pitch, drill, TID, ins, AR | — | calc | p.94 | high |
| RITCHEY-115 | dfm | 1 mm pitch (39.37 mil) BGA, same pad stack: web = 39.37 - 32 = 7.37 mil -> ONE trace between pins; with 2 mil annular ring the signal-layer gap is 3.37 mil -> one trace, barely. Routing TWO traces between 1 mm pins (needs 4/4 mil lines/spaces -> 12 mil web -> clearance <= 25.37 mil) forces unreliable drills or sub-minimum insulation: high shorts/opens fallout, CAF failures, hi-pot failures. VERDICT: never route two traces between 1 mm pins. | — | — | 1 mm BGA | calc | p.94 | high |
| RITCHEY-116 | dfm | 0.8 mm pitch (31.5 mil) BGA on a thick board leaves NO plane web with through-hole vias: connect most pins on layer 2 with blind vias and fan out the rest to through-holes spaced for full through-hole rules (e.g., 0.5 mm part fanned out to 1 mm through-hole pitch). Never route traces between 0.8 mm pins on through-hole boards. | — | — | 0.8 mm and finer BGA | review | p.94-95, Fig 4.68 | high |
| RITCHEY-117 | components | When the BGA pitch can be influenced, choose 50 mil (1.27 mm) over 1 mm: the 1 mm part needs more routing layers (single trace between pins). | — | — | — | review | p.94 | high |
| RITCHEY-118 | dfm | Volume-shop minimum trace/space: 4 mil / 4 mil (3/3 exists at a few fabs but is not for volume). | w, s >= 4 mil | — | Volume production | inspect | p.94 | high |
| RITCHEY-119 | via | Minimum drill = board thickness / aspect ratio. Aspect ratios 6:1, 8:1, 10:1 are standard; 12:1 is possible only with near-hand plating. Use 8:1 for high reliability, 10:1 for best fabs. | d_min = t_pcb / AR | thickness, AR | — | calc | p.95, Fig 4.69 | high |
| RITCHEY-120 | via | Pad-stack tables (Figs 4.70-4.72) follow: drill = t/AR; hole shadow = drill + TID; capture pad = shadow + 2 x annular ring; plane clearance = shadow + 10 mil (2 x 5 mil insulation). Use TID 10 mil / 2 mil ring only with the very best fabs; TID 12 mil / 2 mil ring for most fabs; TID 10 mil / 0 ring only with the best fabs and only when the butt-joint reliability exposure is accepted. | see §2 T9 | t_pcb, AR, TID, AR ring | — | calc | p.95-97 | high |
| RITCHEY-121 | via | Zero annular ring (trace butt-connected to the barrel) is a reliability exposure: resin expansion during soldering/operation opens the butt joint and it re-closes on cooling ("rubber-band boards"). Provide an annular ring where reliability matters. | — | — | — | review | p.94, p.98 | high |
| RITCHEY-122 | fab | Non-functional inner-layer pads are unnecessary since mid/late-1980s ductile plating; remove them from all inner-layer artwork (or have the fab CAM delete them) to cut short risks between pads and passing traces. | — | — | — | inspect | p.98 | high |
| RITCHEY-123 | via | Back drilling removes unused via barrel to cut parasitic capacitance (less reflection jitter, better rise time); the back-drill is several mils larger than the original drill, so plane/trace clearances must be enlarged. Author's view: backplanes with hundreds/thousands of equally critical 2.4-4.8 Gb/s links cannot single out "critical" layers, so back drilling is not a general fix; SMT press-fit-free connectors (smaller via drill) are the direction. | — | — | Thick backplanes | review | p.98-99 | high |
| RITCHEY-124 | via | Two-diameter press-fit via: drill 26 mil (6.6 mm printed; 0.66 mm) for the top ~80 mil to accept the press-fit pin, then 12 mil (3.05 mm printed; 0.305 mm) for the remainder, plated conventionally — used successfully on a terabit backplane. | — | — | Press-fit backplanes | review | p.99 | high |
| RITCHEY-125 | via | For simulation up to ~6 GHz a via is adequately modelled as a lumped parasitic capacitor at its location. Reference 5.2 Gb/s path values (Fig 4.74): Ca = 0.5 pF, Cb = 0.8 pF, Cc = 1.1 pF, Cd = 0.6 pF; backplane 125 mil thick with 13.5 mil vias; daughter cards 116 mil with 12.0 mil vias; connector holes 26 mil. | — | drill, thickness | <= 6 GHz | sim | p.99, Fig 4.74 | high |
| RITCHEY-126 | via | Measured S21 of that path (DC-6 GHz): via capacitance has little effect up to ~1.6 GHz (= 3.2 Gb/s); above it, via capacitance and via spacing create resonances that move when a single extra routing via is added. Back-drilling half the barrel of every via improved the loss curve. Simulation reproduces these resonances, so simulate before routing. | — | — | > 3.2 Gb/s | measure | p.99-100, Fig 4.75 (VNA S21; also sim) | high |
| RITCHEY-127 | via | RULE: at serial rates <= 3.125 Gb/s no back drilling and no via-count restrictions are needed; above 3.125 Gb/s simulate each data path (with via capacitances) to derive its routing rules. | — | data rate | — | sim | p.100 | high |
| RITCHEY-128 | via | Vias are NOT stubs: for 2.4-3.125 Gb/s (fundamental 1.2-1.56 GHz, tr ~150 ps) the edge's first harmonic is ~2 GHz (period 500 ps, wavelength ~3 in in PCB, quarter wave ~3/4 in / 22 mm); even a 0.250 in (6.3 mm) backplane via is only 1/3 of a quarter wave (1/12 wavelength). Vias act as small capacitors that cause a negative (undershoot) reflection. | lambda/4 @ 2 GHz ~ 0.75 in | via length, tr | — | calc | p.101 | high |
| RITCHEY-129 | via | Press-fit backplane via (26 mil / 0.66 mm drill): capacitance ~0.6 pF per 100 mil (2.54 mm) of length -> ~1.5 pF for a 250 mil backplane. Effect at 2.4-3.125 Gb/s: increased jitter; at 4.8 Gb/s: visible jitter AND rise-time degradation. C scales with plated-cylinder area: reduce by smaller drill (GBX / SMT connectors) or thinner board before resorting to back drilling. | C_via ~ 0.6 pF per 100 mil (26 mil hole) | length, drill | — | sim | p.101-102 | high |
| RITCHEY-130 | emc | MYTH: vias radiate EMI / back-drill to cut EMI. VERDICT: false — vias are trapped in the board and cannot radiate; no laboratory evidence; boards with thousands of vias pass EMI daily. Back drilling for EMI is "worse than elephant repellant" (cost without benefit). | — | — | — | review | p.102 | high |
| RITCHEY-131 | fab | Drill chart lists DRILL size for every hole type; for holes where finished size is critical (press-fit connectors) list both drill and finished size. Blind, buried and back-drilled holes need their own chart entries and per-step drill files. | — | — | — | inspect | p.102 | high |
| RITCHEY-132 | fab | Reference fabrication notes for a high-speed multilayer (Fig 4.78): Hi-Tg FR-4 class, Tg >= 170 C; all prepreg and laminate >= 2 plies with resin content >= 50% unless authorized (plane separations < 3 mil may be single ply, no filler); glass styles allowed only 106, 1080, 2113, 2116, 2313, 3313; overall thickness tolerance ± the lesser of 0.010 in (0.254 mm) or 10%. | — | — | — | inspect | p.103, Fig 4.78 notes 3 | high |
| RITCHEY-133 | fab | Fab notes (cont.): minimum annular ring 2 mil (51 um); hole-wall copper >= 0.001 in (25 um) minimum (finished = drill - 0.002 in); finish electroplated 6-15 uin gold over >= 200 uin nickel (palladium allowed between); LPI solder mask over bare copper or Au/Ni, green; nonconductive yellow/white legend; inside corners and slots radius 0.062 in (1.57 mm) ± 0.005 in or less. | ring >= 2 mil; Cu wall >= 1 mil; Au 6-15 uin; Ni >= 200 uin | — | — | inspect | p.103, notes 6-12 | high |
| RITCHEY-134 | fab | Fab notes (cont.): no film modification without authorization; do not remove/modify stacking stripes; compare CAD net list to Gerber-derived net list before fabrication; remove non-functional pads from all inner layers; GERBER TRACE WIDTHS ARE FINISHED WIDTHS — inner-layer finished-width accuracy ± 0.0005 in (12.5 um), outer ± 0.001 in (25 um); fab may add etch compensation only in working film; controlled cross-section board — etch to Gerber widths and build dielectrics to the stackup drawing. | inner width tol ± 0.5 mil; outer ± 1.0 mil | — | — | inspect | p.103, notes 13-18 | high |
| RITCHEY-135 | fab | Fab notes (cont.): first delivery includes a diazo film set and the stackup sheet actually used; teardrops only on through-hole pads <= 23 mil (0.584 mm) at the trace exit — implemented by flashing a second 23 mil pad offset 3 mil (76 um); thieving allowed on outer layers only >= 0.100 in (2.54 mm) from any other outer copper and never within 0.100 in of traces on the first buried signal layer, never solid copper; measure dielectric and copper thicknesses on one board per lot via the stacking stripes and report with first delivery; drilled-hole true position vs CAD <= 0.005 in (127 um); via capping of 12 mil (305 um) vias from the BGA side with epoxy then LPI mask, opposite-side mask encroachment 0.008 in (203 um) beyond drill diameter. | — | — | — | inspect | p.103, notes 19-24 | high |
| RITCHEY-136 | fab | MYTH: right-angle / acute-angle trace bends create "acid traps". VERDICT: false (every fabricator asked says no; residue would cause leakage and rinses remove it). The rule descends from cosmetic ink bleed in silk-screened imaging. Right-angle bends also do not cause reflections at PCB scales. | — | — | — | review | p.103-104 | high |
| RITCHEY-137 | dfm | Design to the STANDARD-process column of the 2005 fab-capability table (§2 T18) for high-volume/Asian production; the ADVANCED column only for fabs with post-etch punch, x-ray drill optimization etc. Key standard vs advanced: aspect ratio 6:1 vs 10:1; min via drill 12 vs 8 mil; min line 5 vs 3 mil; min space 5 vs 4 mil; registration ±8 vs ±5 mil; min dielectric 5 vs 2.2 mil; impedance tolerance ±10% vs ±5%; max thickness 187 vs 500 mil. | — | fab tier | — | inspect | p.104, Fig 4.79 | high |
| RITCHEY-138 | dfm | Thermal tie electrical adequacy: a 5 mil wide x 7 mil long tie in 1/2 oz copper is ~1 mohm and ~0.14 nH — far below the lead-frame of the soldered pin; two ties are more than enough electrically and give the best thermal balance. One tie is thermally best but risks a lost connection. | R_tie ~ 1 mohm; L_tie ~ 0.14 nH (5 x 7 mil, 1/2 oz) | tie geometry | Through-hole pins into planes | calc | p.105-106 | high |
| RITCHEY-139 | dfm | Thermal-tie geometry: capture pad normally 10-12 mil larger than the drill, clearance pad 10 mil larger than the capture pad (5 mil/side) — leaving ties only ~5 mil long. To lengthen ties, make the plane-layer capture pad only 5 mil larger than the drill and accept breakout (one tie still connects when the drill is off-centre). Applies to plane layers only; signal layers keep full annular ring. | — | — | — | inspect | p.105-106, Fig 4.81 | high |
| RITCHEY-140 | dfm | Holes must never be placed so close that a neighbouring clearance pad breaks a thermal tie or overlaps another clearance; with correct spacing two ties always suffice (four-spoke ties exist only to survive bad spacing). | — | hole pitch | — | inspect | p.105 | high |
| RITCHEY-141 | cost | Choose board outline dimensions that nest efficiently in standard panels (usable area after ~1 in tooling border on all sides): 24 x 36 in -> 22 x 34 usable; 18 x 24 -> 16 x 22; 16 x 18 -> 14 x 16; 12 x 18 -> 10 x 16. Avoid odd panel sizes (limits fab portability). | — | board L x W | — | calc | p.106 | high |
| RITCHEY-142 | fab | Mass lamination (panels up to 48 x 72 in) is the lowest-cost multilayer process but works ONLY for 4-layer boards (tolerance build-up across the panel); pin lamination on standard panels for everything else. | — | layer count | — | review | p.107 | high |
| RITCHEY-143 | dfm | Why hole-to-copper insulation is 5 mil although laminate withstands > 1000 V/mil and the usual requirement is 1200 V: drilling chatters glass fibers and plating chemistry wicks along them up to 3 mil from the barrel (example: 1.2 mil / 30.5 um plating with wicking ~2x that), leaving only ~2 mil; poor resin-to-fiber bonding wicks too. Keep 5 mil (127 um) in most designs. Fabricators ask >= 3 mil (76 um) between planes; 2 mil ZBC sheets have shorted in handling. | ins >= 5 mil; plane-plane >= 3 mil | — | — | inspect | p.107-108, Fig 4.82 | high |
| RITCHEY-144 | materials | Copper foil is roughened for adhesion (black oxide peaks can short planes across 106-thin laminates; alternative oxide / double-treat / reverse-double-treat keep it smooth enough for thin laminates). Roughness-driven skin-effect loss is not significant below 3 GHz on FR-4-class laminates; it matters for very rough copper on PTFE microwave boards. | — | — | < 3 GHz | review | p.109-110 | high |
| RITCHEY-145 | materials | Foil thickness: 1/2 oz = 0.7 mil (18 um); 1 oz = 1.4 mil (36 um); 2 oz = 2.8 mil (72 um); finished foils average 0.2 mil (5 um) thinner after cleaning. | t_final ~ t_nominal - 0.2 mil | oz | — | calc | p.110 | high |
| RITCHEY-146 | materials | Glass cloth shrinks under lamination heat; uneven shrinkage is the primary cause of warped boards. Require preshrunk glass (low-cost laminates skip it) and laminate + prepreg from ONE supplier per board — every warped board the author investigated mixed suppliers. | — | — | — | inspect | p.110, p.119 | high |
| RITCHEY-147 | materials | E-glass has a relatively high loss tangent; S-glass lowers laminate loss (Nelco 4000-13SI vs 4000-13, same resin) at higher cost and single-source (Japan). Isola IS620 (filled resin, E-glass) is a drop-in second source for 4000-13SI without stackup redesign. Fig 5.1 (graph): loss vs frequency for a 33 in (84 cm) line — Hi-Tg FR-4 > Nelco 4000-13 > 4000-13SI. | — | material | 33 in path | review | p.110-111, Fig 5.1 (graph) | medium |
| RITCHEY-148 | materials | Glass-bundle pitch is ~16 mil (0.41 mm) and large bundles ~12 mil (305 um) wide; PCB traces (3-5 mil) are small relative to the weave, so a trace alternates between er ~6 (over glass) and er ~3 (resin). Measured 50 ohm trace over 1080 swings almost the full ±10% along one layer (Fig 5.10); harmless when slow, but at 2.5 Gb/s and above it causes reflections and propagation-time variation that can make a path unusable. | dZ0 ~ ±10% over 1080 | glass style, rate | >= 2.5 Gb/s | measure | p.111-113, Figs 5.10-5.11 (TDR) | high |
| RITCHEY-149 | materials | Weave-effect fixes: 45-degree routing (impractical); stacking 106 + 1080 plies to nest (usually but not always works); BEST: specify 3313 glass, whose flattened, spread bundles distribute glass uniformly — TDR over 3313 is uniform at any routing angle (Fig 5.13). 7628 looks uniform but has voids between threads; 3070 and 2113 may be acceptable but are unverified. | — | glass style | Very high speed serial links | inspect | p.113-115 | high |
| RITCHEY-150 | materials | Resin verdicts: epoxy "Hi-Tg FR-4" = workhorse for high layer count; PPO (GETEK/Megtron) = not worth the extra cost (its lower-er claim came from comparing 75% vs 42% resin content; same resin content -> same er; only slightly lower tan d); BT = higher Tg but hard to drill, rarely used; PPE = unavailable (sole plant burned); cyanate ester = absorbs water, fails leakage in humidity (used only blended with epoxy); polyimide = highest Tg, costly, hard to process, needs bake + conformal coat (military). Rogers RO4350 usable in multilayer at extra cost; PTFE is not a multilayer material. | — | — | — | review | p.115-116 | high |
| RITCHEY-151 | materials | Laminate properties Table 5.2 (§2 T16): Tg, er (TDR velocity method, 55% resin), tan d, DBV (V/mil), water absorption for RO4350, FR-4 grades, N4000-6, Hi-Tg FR-4, GETEK, BT, 4000-13SI, CE, polyimide, PTFE. | — | — | — | inspect | p.116, Table 5.2 | high |
| RITCHEY-152 | reliability | Z-axis expansion: below Tg all three materials expand alike (resin alpha1 = 50 ppm/C; copper 16.5; glass 11); above Tg resin alpha2 = 275 ppm/C, all in Z because glass/copper pin X-Y -> barrel copper fractures in thick boards. Eutectic solder melts at 185 C (365 F). Fig 5.14 (graph) Z-expansion to ~275 C: FR-4 5.1%, multifunctional 4.7% / 4.5% / 4%, BT-epoxy & GETEK 3.8%, polyimide 3% / 2%, cyanate ester 2.3%. | — | Tg, thickness | — | calc | p.117, Fig 5.14 (graph) | medium |
| RITCHEY-153 | materials | Tg selection, eutectic (leaded) solder: Tg 135 C laminate is acceptable for boards <= 63 mil (1.6 mm); boards thicker than 63 mil need Tg >= 170 C (low-Tg fails at 93 mil and above). | t <= 63 mil: Tg >= 135 C; t > 63 mil: Tg >= 170 C | thickness | Leaded solder | inspect | p.117-118 | high |
| RITCHEY-154 | materials | Tg selection, lead-free (solder melting >= 225 C / 436 F): boards <= 63 mil need Tg >= 170 C; boards thicker than 63 mil need Tg >= 220 C (decomposition and via failure risks otherwise). | t <= 63 mil: Tg >= 170 C; t > 63 mil: Tg >= 220 C | thickness | RoHS | inspect | p.118 | high |
| RITCHEY-155 | materials | There is no fixed loss-tangent threshold for "needing" a low-loss laminate: loss depends on frequency x length; the only valid method is to simulate the proposed path with skin-effect and dielectric loss in the chosen material and judge the eye (Ch.8). | — | tan d, length, rate | — | sim | p.118 | high |
| RITCHEY-156 | materials | Dielectric breakdown >= 1000 V/mil for all common laminates -> 2 mil would meet the 1700 VDC Ethernet isolation spec, but fiber wicking can cut effective insulation below 1 mil; safe minimum laminate between opposing planes = 3 mil (76 um). | t_min = 3 mil for 1700 VDC | — | — | calc | p.118-119 | high |
| RITCHEY-157 | materials | Water absorption < 0.2% -> no leakage problems; above it leakage failures can and do occur. Cyanate ester and polyimide absorb enough to need a bake plus a waterproof conformal coating (Table 5.2 prints 0.70% and 0.43% for the last rows; row mapping is ambiguous, see T16); avoid them if possible. | WA < 0.2% | material | — | inspect | p.119 | high |
| RITCHEY-158 | components | Buried (Ohmegaply nickel) resistors: 25 ohm/square; a 50 ohm terminator = 2 squares (10 x 20 mil at 50 mil BGA pitch; 20 x 40 mil at 100 mil PGA pitch); accuracy no better than ±10%, ±18% for the 50 mil-pitch case — outside SI needs; cost exceeds discretes; area saving only for parallel terminations to a Vtt plane (series terminators need two vias -> no saving). | R = 25 ohm/sq x squares | — | — | review | p.120-121 | high |
| RITCHEY-159 | pdn | Buried-capacitance laminate (ZBC etc., 2 mil, ~450 pF/in^2): not needed — pairing ordinary planes across thin prepreg gives the same function without license fees and without breaking the signal-over-laminate stackup rule. Author has never seen a design that needed it. | ~450 pF/in^2 at 2 mil | — | — | review | p.121-122 | high |
| RITCHEY-160 | return-path | Split (multi-voltage) power planes: the ONLY valid reason to cut a plane is to carry more than one supply in one layer. Never split a ground plane (author never saw a benefit in any digital or mixed-signal design). All voltages share one ground structure; each rail's PDS must be low impedance (<= ~10 mohm DC to >= 1 GHz) so each half is AC-shorted to the ground plane and hence to the other half. | Z_pds <= 10 mohm, DC-1 GHz | — | — | review | p.123 | high |
| RITCHEY-161 | return-path | MYTH: routing over a plane split degrades SI / causes EMI. VERDICT (measured on 18-layer test board, 10 mil gaps, L2 traces over L3 cuts): TDR shows no detectable disturbance; near-field probe with RF drive shows no change across the split. Exception: boards whose planes cannot be bypassed to each other (2-layer 32 mil spacing test, 4-layer motherboards) — there, add capacitors across the gap or avoid crossing. | — | plane spacing / PDS | Requires proper PDS; not for 4-layer | measure | p.123-125, Figs 6.1-6.3 (TDR, near-field probe) | high |
| RITCHEY-162 | return-path | Plane split width: 1700 VDC isolation needs only 2 mil (laminate > 1000 V/mil = 39,370 V/mm); etch limits: >= 3 mil gap for 1/2 oz plane, twice that (6 mil) for 1 oz; use 10 mil (0.25 mm) — easy to etch, small feature; no need for wider gaps. | gap = 10 mil (min 3 mil for 1/2 oz, 6 mil for 1 oz) | copper weight | — | inspect | p.125 | high |
| RITCHEY-163 | return-path | MYTH: a signal changing reference planes needs an adjacent "ground via" / causes SI or EMI problems. VERDICT (18-layer test board, Tek 1502C 125 ps TDR; L9->L10 and L2->L17 changes, with and without adjacent ground vias): all four cases identical, no detectable discontinuity, even with NO discrete capacitors (interplane capacitance alone). No ground via required beside a layer-change via; hundreds of boards routed layer-to-layer freely passed stringent EMI. | — | — | Requires each rail's PDS to be low impedance | measure | p.125-129, Figs 6.4-6.7 (TDR) | high |
| RITCHEY-164 | decoupling | Capacitive reactance reference (Fig 6.2/6.4, ignoring mounting inductance): 100 pF = 53 / 16 / 1.6 ohm at 30 MHz / 100 MHz / 1 GHz; 1000 pF = 5.3 / 1.6 / 0.16 ohm; 0.01 uF = 0.53 / 0.16 / 0.016 ohm. Even one 1 nF capacitor "shorts" two planes at 100 MHz (0.16 ohm); for fast edges the interplane capacitor dominates. | X_C = 1/(2*pi*f*C) | C, f | — | calc | p.124, p.128 | high |
| RITCHEY-165 | decoupling | Place the computed decoupling capacitors for each rail UNIFORMLY across that rail's plane area (this also ties all ground planes together in many places). Each rail's PDS impedance should be "less than a dozen or so milliohms" so that all planes are shorted together at signal frequencies and any high-speed signal may be routed over any plane. | Z_pds < ~12 mohm | — | — | inspect | p.128 | high |
| RITCHEY-166 | stackup | 4-layer motherboards (planes far apart) cannot be adequately bypassed at signal frequencies: route each single-ended signal to begin and end on the same layer and avoid crossing plane cuts. | — | — | 4-layer | inspect | p.125, p.129 | high |
| RITCHEY-167 | termination | Noise margins shrink with voltage: 3.3 V HSTL CMOS 1.15 V vs 1.8 V CMOS 430 mV — undershoot (negative reflection, erodes margin) now matters more than overshoot (positive reflection, does not erode margin). Board impedance tolerance is ±10% (45-55 ohm for 50 ohm nominal). | — | Vdd family | — | calc | p.129 | high |
| RITCHEY-168 | termination | Parallel termination value = nominal Z0 + 10% (55 ohm for 50 ohm lines; 110 ohm for 100 ohm differential; ECL used 55 ohm): zero reflection at the high impedance limit and only acceptable overshoot elsewhere in tolerance. | R_par = 1.1 x Z0 | Z0 | Parallel-terminated lines | calc | p.129 | high |
| RITCHEY-169 | termination | Series termination: choose Zst so that Zout + Zst <= Z0 - 10% (45 ohm in a 50 ohm system) so the bench voltage Vbench = V x Z0/(Z0 + Zst + Zout) is >= V/2 for every in-tolerance board (avoids undershoot at the receiver). | Zout + Zst <= 0.9 x Z0 | Zout, Z0 | Series-terminated SE lines | calc | p.130, Fig 6.10 | high |
| RITCHEY-170 | return-path | Set the router's minimum via-to-via spacing so plane clearance pads can never overlap — a continuous copper web must remain between every pair of holes; overlapping clearances slot ALL planes at the same place (unlike a single-plane split) and cause real SI and EMI problems. | pitch_min > clearance_pad diameter | clearance pad | — | inspect | p.130-131 | high |
| RITCHEY-171 | emc | EMI test bands: conducted 150 kHz-30 MHz; radiated 30 MHz-1 GHz or 5 x the highest clock frequency, whichever is greater. | — | f_clk | — | measure | p.132 | high |
| RITCHEY-172 | emc | EMI needs a source (Vdd ripple / fast edges) and an antenna. Since modern parts cannot be slowed (edges are above 30 MHz content), containment = eliminate accidental antennas. Ferrite beads in power leads (source removal) are obsolete and degrade signals (3.125 Gb/s serdes example). | — | — | — | review | p.132-133 | high |
| RITCHEY-173 | emc | MYTH: traces on outer layers radiate. VERDICT: conductors close to planes neither radiate detectable EMI nor pick it up (antennas are reciprocal; a hand-held FM radio fades near a metal sheet). Good antennas are things that stick up or leave the board: PLCC lead frames, unshielded cables (mouse, monitor), two boards joined by a DIMM connector (dipole), PGAs/BGAs in sockets. | — | — | — | review | p.133 | high |
| RITCHEY-174 | emc | Three treatments for a potential antenna: (1) shield it where it leaves (shield to logic ground if no cage, else to the cage at the exit point — shields are extensions of the cage); (2) low-pass filter at the exit with substantial attenuation 30 MHz-1 GHz built from plane/fill capacitance (only when the useful signal is well below 30 MHz — never ferrite-choke USB-class signals); (3) Faraday cage. | — | — | — | review | p.133-134 | high |
| RITCHEY-175 | emc | Faraday cage rules: any common metal; paint must not cover metal-to-metal bonding areas; connect logic ground to the cage at ONE and only one place (on the side where unshielded-line drivers sit); NEVER tie plug-in faceplates or board edges (card-guide strips) to logic ground; "EMI leaking at the cracks/seams" = multiple ground-to-cage connections turning the cage into an antenna. | n_connections(logic GND -> cage) = 1 | — | — | inspect | p.134, p.140, p.142 | high |
| RITCHEY-176 | grounding | "Ground" verdicts: green-wire/earth ground = safety only, no EMI role; a "chassis ground" plane in a backplane has no EMI value (cost only); logic ground need not connect to chassis to pass EMI (cell phones have no green wire); analog ground must be the SAME net as the converter's logic ground — splitting analog/digital grounds does not improve performance and often raises EMI. | — | — | — | review | p.134-135 | high |
| RITCHEY-177 | emc | Ventilation openings in a Faraday cage: holes/mesh no larger than 1/4 in (6.35 mm) contain EMI to at least 10 GHz (measured); screens and honeycombs must be bonded to the cage all the way around. | d_hole <= 0.25 in -> OK to 10 GHz | — | — | inspect | p.135 | high |
| RITCHEY-178 | emc | Shielded-cable exits: shield -> connector shell -> Faraday cage with a very low inductance bond; do NOT tie the shell to logic ground when it is part of the cage. Before shielding both ends of a cable between boxes on different AC sources, verify there is no potential difference. Fiber-optic I/O removes the problem entirely. | — | — | — | inspect | p.136 | high |
| RITCHEY-179 | emc | When a shield may not be DC-connected to the cage (10Base2: 1700 VDC isolation), discrete capacitors fail (no part has both the voltage rating and low impedance 30 MHz-1 GHz). Build a plane capacitor: isolate the last ~1 in of all layers by cuts, flood outer layers and tie them to the faceplate/cage, use inner-layer plates per coax shield -> ~370 pF per line with 8 mil minimum insulation (> 8000 V); 80 mil (2 mm) outer-layer isolation gap; 4-layer cross-section 8 / 40 / 8 mil. Emissions dropped from failing CISPR B to passing. The same AC connection works for logic ground when a DC bond is not permitted. | C ~ 370 pF; ins >= 8 mil; gap 80 mil | — | — | measure | p.137-139, p.143, Figs 7.5-7.7 | high |
| RITCHEY-180 | emc | Unshielded slow control lines leaving the cage (fan control, keyboard, mouse): attach a large copper patch in a signal layer (parallel plate to the ground planes) to the trace at the exit to form a broadband low-pass filter. | — | — | Useful signal << 30 MHz | inspect | p.139, Fig 7.8 | high |
| RITCHEY-181 | emc | UTP Ethernet at the far end of a plug-in card: use an output transformer with center-tapped secondary and connect the center tap to the Faraday cage through a plane-built capacitor; never cut the ground plane under the magnetics (almost always causes an EMI problem). | — | — | — | inspect | p.139-140, p.142, Fig 7.9 | high |
| RITCHEY-182 | emc | Power entry: conducted band 150 kHz-30 MHz is low enough for discrete L-C filters or filter modules. AC products: filter in the inlet module. -48 VDC backplane systems: put the filter on EACH plug-in module where raw DC enters from the backplane. Wall-adapter products: filter on the main PCB at DC entry. | — | — | — | inspect | p.140 | high |
| RITCHEY-183 | emc | Card-cage Faraday cage: two solid cage sides; the backplane's ground planes form the back, bonded to the cage flanges through plated copper strips on the backplane (no "chassis" plane, no edge plating needed); honeycomb bonded top and bottom; faceplates sealed to each other with EMI gaskets (foam+mesh or spring fingers); power supply and fans outside the cage with filtered feeds. Terabit router (7 kW, half rack) passed first try, as did two successors. | — | — | — | inspect | p.140-142, Figs 7.10-7.11 | high |
| RITCHEY-184 | emc | A backplane ground plane may be bonded to the cage at many points only if it carries NO power current (no voltage gradient); in that design -48 V was distributed in unused signal-layer areas and the planes served only as transmission-line partners. RJ-45 housings along a pizza-box front may all bond to the cage provided the board's ground plane is uncut. | — | — | — | review | p.142 | high |
| RITCHEY-185 | emc | MYTH: the system clock is the primary EMI source. VERDICT: no — emissions (30 MHz to > 1 GHz) are not clock harmonics; the source is Vdd ripple from a PDS that cannot supply switching current, conducted out on any wire at logic 1. Discrete capacitors cannot supply switching current above ~100 MHz (Hubing); plane capacitance must. PCMCIA fix: plane capacitance 500 pF -> 4100 pF via signal-layer fill turned a CISPR B failure into a pass. | — | — | — | measure | p.143, Fig 7.12 (emissions scan) | high |
| RITCHEY-186 | emc | Emission spectra of identical designs differ unit to unit because the current trapezoid (set by part rise time and line length) sets the spectrum: 12 in line, fastest edge -> 85-900 MHz; slowest edge -> different amplitude and frequencies; 3 in line -> V-shaped current spike, dramatically different spectrum. Design the PDS for the fastest-edge, longest-line case. | — | tr, line length | — | sim | p.143-144, Figs 7.13-7.14 (FFT) | high |
| RITCHEY-187 | emc | Cheapest EMI strategy: design each rail's bypassing (including enough plane capacitance) to minimize Vdd ripple — the author has fixed failing products this way alone; containment vessels are far more expensive. | — | — | — | review | p.144 | high |
| RITCHEY-188 | compliance | Design emissions to at least 6 dB below the regulatory limit: unit-to-unit edge-rate variation changes the emission spectrum (amplitude and frequency), and the tested specimen may be the best-behaving unit. | margin >= 6 dB | emissions scan | — | measure | p.144-145 | high |
| RITCHEY-189 | emc | Conducted EMI (150 kHz-30 MHz, leaves via the power cord): use filter modules from DC-DC converter makers or a discrete L-C filter on the PCB; ferrite toroids clamped on power cords are afterthought fixes that cost more than an on-board filter. | — | — | — | review | p.145 | high |
| RITCHEY-190 | emc | Spread-spectrum clocking (clock period modulated cycle to cycle) is the EMI tool for products that cannot be enclosed in a Faraday cage (ink-jet printers, low-cost video games); requires a clock slow enough that edges can be moved within the cycle. | — | f_clk | — | review | p.145 | high |
| RITCHEY-191 | emc | Treat any EMI rule of thumb whose proponent cannot demonstrate it by measurement as suspect; valid EMI rules are easy to demonstrate. | — | — | — | review | p.145 | high |
| RITCHEY-192 | emc | Invalid EMI rules (tested): right-angle bends cause EMI (false, ref 10); outer-layer traces cause EMI (false, ref 10); traces crossing power-plane splits cause EMI (false, ref 14); ferrite beads in IC power leads reduce EMI (only by degrading the device; never do it, ref 89). | — | — | — | review | p.146 | high |
| RITCHEY-193 | emc | 20H rule (recess the Vdd plane from the ground-plane edge by 20 x plane separation): VERDICT = invalid. Testing (ref 89) found little or no detectable EMI at board edges and recessing made it WORSE; no supporting evidence was ever produced. Do not recess power planes for EMI. | — | — | — | review | p.146-147 | high |
| RITCHEY-194 | emc | lambda/20 rule (bond logic ground to "chassis" every lambda/20) and mounting every plug-in PCB on a "chassis ground" backing plate that includes the faceplate: VERDICT = invalid. Both assume one dominant frequency and an EMI-neutral chassis; they create multiple ground-to-cage current paths (EMI) and add cost without benefit. | logic GND to cage: 1 point | — | — | review | p.146-147, Fig 7.17 | high |
| RITCHEY-195 | emc | Splitting ground planes to "eliminate EMI": VERDICT = invalid; it can turn the PCB into a dipole antenna and raise EMI. | — | — | — | review | p.146 | high |
| RITCHEY-196 | emc | "Connect bypass capacitors directly to IC power pins to reduce EMI": VERDICT = invalid (Fig 7.16 contrasts the right and wrong connection; details are in the Vol.1 power-delivery chapters). Author's method elsewhere: capacitors connect to the planes, which feed the IC. | — | — | Figure not in text | review | p.146, Fig 7.16 | medium |
| RITCHEY-197 | emc | Plating PCB edges, rows of ground vias around the board edge, and grounded edge "guard rings" do not contain EMI (fields stay close to their traces). A guard ring is legitimate only as ESD handling protection (routes a handler's charge into ground instead of component leads). | — | — | — | review | p.146 | high |
| RITCHEY-198 | emc | Whole-product EMI prediction by modelling tools is not achievable (needs a 3D model of the operating product from 30 MHz to >= 1 GHz). Instead: a good PDS and a good transmission-line environment (minimize sources and antennas); any product with two PCBs joined by connector or cable needs a Faraday cage; manage every antenna leaving the cage. | — | — | — | review | p.147-148 | high |
| RITCHEY-199 | compliance | Emission rules: US FCC Rule (Part) 15 Class A (commercial) / Class B (residential); EU EN 55022, shorthand CISPR A / CISPR B (similar, not identical); other countries (e.g., Canada) adopt one. Compliance is self-declared (test, keep the file, label units); violations are fined per unit shipped (author's employer paid $10,000 per non-compliant unit). Put a compliance specialist (EMI, safety, RoHS, telecom homologation) on every product sold worldwide. | — | — | — | review | p.148 | high |
| RITCHEY-200 | emc | UTP carries in-band signals without EMI because closely spaced equal-and-opposite currents cancel a few spacings away; impedance between the wires is irrelevant, small spacing and exact balance matter. Common-mode noise on both wires (e.g., through the magnetics) defeats it. | — | — | — | review | p.148-150, Figs 7.18-7.20 | high |
| RITCHEY-201 | emc | Differential pair feeding UTP or a multi-pair connector: length-match the two traces from driver/serdes/transformer to the cable within 2.5% of the smallest bit period -> no detectable EMI (empirical). Example 2.4 Gb/s: bit 416 ps = 2.4 in (6.1 cm) of PCB -> match within 60 mil (1.5 mm). | dL <= 0.025 x t_bit x v | bit rate, v | — | calc | p.150 | high |
| RITCHEY-202 | emc | Reciprocity: a balanced pair that does not radiate cannot pick up a differential signal; external fields induce only common-mode noise, rejected by a receiver that ignores common mode. | — | — | — | review | p.150 | high |
| RITCHEY-203 | crosstalk | Multi-row high-speed connectors without row shields (e.g., FCI AirMax VS) get low crosstalk from in-pair field cancellation, which fails while a pair's edges are misaligned: length-match each pair tightly from source to connector (less critical after the connector). | — | — | — | inspect | p.150, p.168 | high |
| RITCHEY-204 | emc | Cable shields between separately earthed boxes (several volts AC between earth grounds): bond the shield DC (low inductance) to the cage at one end and through a plane capacitor at the other, sized low impedance at 30 MHz and high impedance at power-line frequency (the 370 pF plane capacitors of Fig 7.6 work); or plane capacitors at both ends; all connections very low inductance. | — | — | — | inspect | p.150-151 | high |
| RITCHEY-205 | transmission-line | Single-ended logic compares against a fixed Vref midway between levels; at high rates and low Vdd, ground offsets, injected ground noise and attenuation make it unreliable. Use differential signalling at high data rates or where the return path is poor (e.g., laptop display across the hinge). | — | — | — | review | p.152 | high |
| RITCHEY-206 | transmission-line | LVDS mechanics: H-switch between two 4 mA current sources (driver floats with the receiver's ground within source compliance); each line 50 ohm terminated 50 ohm to Vref -> ±200 mV per line, 400 mV differential; the receiver current switch needs as little as ~50 mV difference (most CMOS). Swing = I x Z0, so line impedance sets the voltage. | V_line = I x Z0 = 4 mA x 50 ohm = 200 mV | I, Z0 | LVDS | calc | p.153-154, Figs 8.1-8.3 | high |
| RITCHEY-207 | termination | A differential pair needs two 50 ohm lines each terminated in 50 ohm to Vref; "100 ohm differential" is the differential-TDR measurement convention. At 2.4 Gb/s and above install both 50 ohm terminators (not one 100 ohm resistor) with ~10 pF from their junction to logic ground to supply the momentary current when the edges are not perfectly aligned; at LVDS speeds a single 100 ohm resistor is fine. | C_ct ~ 10 pF | data rate | >= 2.4 Gb/s | inspect | p.153-154 | high |
| RITCHEY-208 | transmission-line | A differential receiver is a crossing detector: rules must preserve the crossing (edges crossing in the straight part of the transitions). The two lines have no beneficial electrical relationship beyond carrying equal, opposite, tightly timed waveforms. | — | — | — | review | p.154-155, Fig 8.4 | high |
| RITCHEY-209 | crosstalk | MYTH #1: side-by-side routing gives common-mode rejection of neighbouring noise. VERDICT = false in a PCB (the reference plane makes the aggressor field unequal at the two members). Fig 8.5 (aggressor 5 mil away, 5 mil geometry): broadside pair near member 12%, far member 1% (11% differential); coplanar pair near 12%, far 2% (10% differential). Keep aggressors away per the noise budget. | — | — | — | sim | p.156-157, Fig 8.5 | high |
| RITCHEY-210 | crosstalk | Broadside (over-under) differential pairs: do not use; no performance benefit, very hard to route, and fabricators cannot register two layers well enough to keep the traces aligned. | — | — | — | inspect | p.156 | high |
| RITCHEY-211 | transmission-line | Pair members need NOT be side-by-side or even on the same layer; they must have the same impedance, the same length, and differentially coupled noise within budget (max crosstalk from a noise-margin analysis, then spacing to neighbours from a 2D field solver). Members may split around BGA pins (e.g., out different rows of a 1 mm BGA). | — | — | — | review | p.156-157 | high |
| RITCHEY-212 | transmission-line | MYTH #2: tight in-pair coupling is beneficial. VERDICT = false: tight coupling forces narrower traces to hold 100 ohm differential -> more skin loss (Fig 8.7: 5/5 mil vs 10/15 mil pairs at 2.4 Gb/s over 30 in; the loose pair delivers more amplitude). Stand-alone impedance of one member: tight (5 mil) ~70.7 ohm; loose (10 mil) ~54 ohm. Spread to 39 mil (to pass a 1 mm BGA field): Zdiff 100 -> 140 ohm tight vs 100 -> 109 ohm loose. | — | — | Fig 8.6 geometry | sim | p.157-159, Figs 8.6-8.8 | high |
| RITCHEY-213 | transmission-line | Choose the minimum in-pair spacing at which each member's impedance is barely reduced by its partner (loose coupling), then never route the members closer; impedance then stays constant when the pair spreads around obstacles. | — | — | — | sim | p.158 | high |
| RITCHEY-214 | transmission-line | The skin-loss penalty of tightly coupled (narrow) pairs is unimportant below ~2.4 Gb/s and paths below ~20 in, but the impedance-jump problem when the pair spreads remains. | — | rate, length | — | review | p.158 | high |
| RITCHEY-215 | return-path | Route both members of a pair over the same plane: one over ground and one over a rippling Vdd plane converts ripple into differential noise. Otherwise design the PDS so ripple is well within the pair's noise tolerance. | — | — | — | inspect | p.159 | high |
| RITCHEY-216 | return-path | MYTH #3: one member's return current flows in the other member. VERDICT = false: switching current follows the parasitic capacitance, i.e., the plane under each trace; only ~2% flows in the partner. | ~2% on partner | — | — | review | p.159 | high |
| RITCHEY-217 | timing | MYTH #4: very tight in-pair length matching is needed. VERDICT = over-constraint: allowable in-pair mismatch = the fastest edge (rise time) arriving at the receiver expressed as length (keeps the crossing in the straight part of the edges). LVDS in laptops: 400 ps -> ~2.4 in (works with 2 in mismatch, yet CAD is often told <= 100 mil); 2.4 Gb/s path: 300 mil. | dL_max = tr_fastest x v (v ~ 6 in/ns) | tr at receiver | UTP/connector entry has tighter rules (RITCHEY-201, -227) | calc | p.159-160 | high |
| RITCHEY-218 | test | Validate every simulation model against hardware before trusting it: the 5.2 Gb/s rack-to-rack model (8 in stripline + 4 m Infiniband + 8 in stripline) matched 4-port network-analyzer S21 of test boards to 6 GHz; residual differences came from SMA launch parasitics larger than calculated. | — | — | — | measure | p.160-162, Figs 8.9-8.11 (VNA) | high |
| RITCHEY-219 | transmission-line | Diagnostic method: simulate the path at increasing data rates and selectively turn off skin loss, dielectric loss and via capacitances to find which mechanism closes the eye; spend design effort only on the dominant one. | — | — | — | sim | p.161-165 | high |
| RITCHEY-220 | transmission-line | 5.2 Gb/s path findings (0.65 pF routing vias, 12 mil x 100 mil): 100 Mb/s edges rolled off but bit centre correct; 1 Gb/s eye "just open enough"; 2.4 Gb/s fails the amplitude mask with growing jitter — loss (dielectric + skin) erodes amplitude, via reflections drive jitter and become THE limit beyond 2.4 Gb/s; 4.8 Gb/s eye far too small without pre-emphasis. Routing vias are not a problem at <= 2.4 Gb/s. | — | — | — | sim | p.162-165, Figs 8.12-8.18 | high |
| RITCHEY-221 | via | Press-fit backplane hole (26 mil x 250 mil) ~2 pF: at 2.4 Gb/s it worsens amplitude and jitter versus 0.65 pF routing vias, but pre-emphasis still compensates at that rate. | C ~ 2 pF | — | — | sim | p.164-165, Fig 8.17 | high |
| RITCHEY-222 | transmission-line | Pre-emphasis and de-emphasis are the same process (boost the first bit after a transition vs attenuate later bits). 15% pre-emphasis opened the 5.2 Gb/s eye (more amplitude, less crossing jitter). Do not simply raise drive amplitude instead: short/low-loss paths then overdrive the receiver (more jitter, lost bits). | 15% (example) | — | 5.2 Gb/s | sim | p.166, Figs 8.19-8.20 | high |
| RITCHEY-223 | transmission-line | Post-emphasis (receiver high-pass equalizer + gain) is used on some > 6 Gb/s links only as a last resort: the gain amplifies coupled noise (SNR loss, bit errors) and the on-die filter costs silicon. | — | — | > 6 Gb/s | review | p.166-167 | high |
| RITCHEY-224 | materials | Low-loss laminate decision: no safe rule of thumb; model the path with the actual connectors, packages, drivers, receivers, vias and traces and simulate with each candidate dielectric. | — | — | — | sim | p.167 | high |
| RITCHEY-225 | materials | Skin vs dielectric loss trade (33 in path, 0.6 mil / 1/2 oz traces, Fig 8.21): at 2.5 GHz, doubling width 5 -> 10 mil saves only ~1 dB; Hi-Tg FR-4 -> Nelco 4000-13 saves ~2 dB; -> Nelco 4000-13SI or Isola IS620 saves ~4 dB. Traces wider than 5 mil are almost never needed, even at 6.125 Gb/s; use a lower-loss laminate instead (wider traces force thicker dielectrics -> thicker board, more crosstalk, longer higher-C press-fit vias). | — | width, material | 33 in path | sim | p.167-168, Fig 8.21 (graph) | medium |
| RITCHEY-226 | stackup | In backplanes, lower-loss dielectric permits narrow 50 ohm traces -> thinner dielectrics -> thinner backplane -> lower press-fit via capacitance. | — | — | Backplanes | review | p.167 | high |
| RITCHEY-227 | timing | Driver-to-connector in-pair length matching: 60 mil is satisfactory at 2.4 Gb/s for connectors with baffles between rows (from 3D connector-model crosstalk simulation); for other connectors obtain the value from the manufacturer. | dL <= 60 mil | — | 2.4 Gb/s, baffled connectors | sim | p.168 | high |
| RITCHEY-228 | termination | Differential parallel termination: 55 ohm per line or one 110 ohm resistor across the pair (100 ohm nominal, ±10% board tolerance) so only overshoot-type, margin-preserving reflections occur; LVDS leaves the driver at only ~400 mV, so undershoot must be avoided. | R = 1.1 x Z0 | — | — | calc | p.168-169, Fig 8.22 | high |
| RITCHEY-229 | components | AC-coupling capacitors in differential pairs (for DC offset beyond receiver rating; cheaper than transformers): 0.01 uF 0402 on inner-layer pairs with 12 mil via transitions to the pads showed no detectable S21 difference below 3 GHz and only minor above; not a significant degradation up to at least 9.6 Gb/s. | 0.01 uF 0402 | — | <= 9.6 Gb/s | measure | p.169-170, Fig 8.23 (VNA) | high |
| RITCHEY-230 | process | DVT / hardware prototyping can be worse than no testing: passing DVT does not prove stability across component and environmental variation; use virtual prototyping (simulation of all aspects). | — | — | — | review | p.171 | high |
| RITCHEY-231 | process | Every simulation tool has its own component library with no linkage between tools; each new part needs an entry per tool, created and maintained by technically qualified librarians. | — | — | — | review | p.172 | high |
| RITCHEY-232 | process | Schematic capture must carry a per-net class field (technology table) and per-net timing information. | — | — | — | inspect | p.172 | high |
| RITCHEY-233 | process | Floor planner passes placement-derived lengths to timing analysis, locations to thermal analysis and connectivity to logic simulation/emulation; any thermal-driven move requires re-verifying timing and routability. | — | — | — | review | p.172-173 | high |
| RITCHEY-234 | hw-fw | Develop software/firmware against a logic simulator (software model) or logic emulator (programmable array; use where parts such as microprocessors lack logic models, or with Ethernet/memory/printer mechanisms in the loop) before committing hardware; then correct the hardware net list from the verified model. | — | — | — | review | p.173-174 | high |
| RITCHEY-235 | timing | The timing analyzer must import wire delays from the proposed placement/routing (interconnect delay is a major share of the budget). | — | — | — | calc | p.174 | high |
| RITCHEY-236 | process | SI analysis pays most (a) before the first schematic (proposed rules and components across all conditions) and (b) after placement, before routing (proposed net topologies); SI during routing is difficult and whole-board post-route SI is too late. | — | — | — | review | p.174 | high |
| RITCHEY-237 | process | I/O models: prefer transistor-level SPICE (captures package parasitics and adjacent-driver interaction); IBIS cannot accurately include package parasitics, adjacent-driver interaction or pre-emphasis, but is adequate for robust design rules in almost all simulations. | — | — | — | sim | p.174-175 | high |
| RITCHEY-238 | process | Model fidelity ladder: "simple" line (Z0 + delay) suffices for sizing terminations when crosstalk and loss do not matter; 2D field-solved cross-sections when crosstalk or loss matters; connectors and IC packages need 3D models or S-parameters (measured on a network analyzer or from a 3D solver). | — | — | — | sim | p.175 | high |
| RITCHEY-239 | pdn | Use a PDS tool that models capacitors and planes together; capacitor-only tools miss plane interaction. | — | — | — | sim | p.175 | high |
| RITCHEY-240 | process | Router requirements: obey per-class trace width, layer restrictions, trace-to-trace spacing, length constraints and routing direction (X or Y); a DRC utility must flag violations before artwork. | — | — | — | inspect | p.176 | high |
| RITCHEY-241 | fab | CAM/Gerber checking (usually at the fabricator's front end; can be added in-house) checks feature spacing, layer-to-layer alignment and net-list accuracy before fabrication. | — | — | — | inspect | p.176 | high |
| RITCHEY-242 | components | CMOS at 130 nm and larger dissipates almost only on state changes: a chip can draw a few mA idle and many amperes active. High-end chips have thousands of pins and > 1000 signal pins; simultaneous switching can drive tens of amperes of I/O current with sub-ns rise times lasting many ns (DC-terminated lines). | — | — | — | calc | p.177 | high |
| RITCHEY-243 | components | Die attach: wire bonds have a few nH each (limit fast I/O and power; perimeter bonds push core current through resistive chip metal — prohibitive IR drop for high-power chips); flip-chip (97/3 Pb/Sn balls that do not melt at board reflow) ~50 pH per ball, distributed over the die. Use flip-chip for high-pin-count, high-power, fast devices. | L_wirebond ~ few nH; L_ball ~ 50 pH | — | — | review | p.180, p.186 | high |
| RITCHEY-244 | components | Package substrate: ceramic — er ~10 (high capacitance, low velocity), screened conductors more resistive than copper (attenuation on long lines), ~17% firing shrinkage, 90/10 Pb/Sn balls attached with eutectic roll to absorb the ceramic-to-PCB TCE mismatch; used on very-high-volume parts. Organic — er ~4, 1/2 oz copper, eutectic balls, TCE matched to the PCB; better signal quality and lower power-distribution drops; used for lower-volume or higher-speed parts. | er ~10 (ceramic), ~4 (organic) | — | — | review | p.179-180 | high |
| RITCHEY-245 | test | Measure series-terminated signals at the RECEIVER (e.g., on the vias under the receiving BGA); near the driver incident and reflected waves superimpose and cannot be judged. Instruments used: Tektronix TDS7404 4 GHz sampling scope, P7240 4 GHz active probe. | — | — | Series-terminated buses | measure | p.181 | high |
| RITCHEY-246 | components | Package design dominates I/O quality: the same SPI-4.1 bus (64 bit, source-synchronous, series-terminated HSTL, 200 MHz) from a Virtex-2 Pro FF1517 showed 1600 ps clock jitter and ~800 mV Vddq/ground bounce, vs 97 ps on Virtex-4 (Sparse-Chevron package) and a clean IBM ASIC in HyperBGA. Causes: poor core power distribution in the package (core droop each clock edge modulates clock-tree delay -> jitter) and poor signal return paths/Vddq distribution (bounce). Screen packages before committing (Section 10.12). | — | — | — | measure | p.180-183, Figs 10.7-10.12 | high |
| RITCHEY-247 | assembly | Reflow temperatures: eutectic 63Sn/37Pb melts at 183 C, reflow brings the package to ~220 C; lead-free SAC (95.5% Sn, 3.8% Ag, 0.5% Cu as printed) melts at 218 C with 260 C peak reflow. Package and board materials must survive these. | — | — | — | inspect | p.183 | high |
| RITCHEY-248 | reliability | Thermal cycling: activity-driven power changes cause millions of ~10 C cycles on high-power chips; the environment adds larger ones (telecom ambient 0-55 C plus internal heating; Tj max typically 100 C -> total 0-100 C). The customer must verify by thermal-cycle testing of the final assembled product. | — | — | — | measure | p.183 | high |
| RITCHEY-249 | pdn | Core PDS sizing inputs (90 nm example): Vdd ~1.2 V; a 50 W ASIC draws ~42 A average; clocking > 0.5 M DFFs produces core spikes of several hundred amperes lasting a few hundred ps, which chip + package + PCB must support from DC to several GHz. | I_avg = P/Vdd | P, Vdd | — | calc | p.183, p.187 | high |
| RITCHEY-250 | pdn | Single-ended I/O return current: series-terminated CMOS launches Vddq/2 into 50 ohm (1.8 V -> 0.9 V -> 18 mA per driver); a 100-bit bus switching together draws 1.8 A with a few hundred ps rise, and the same current must return through the package Vddq/ground pins. No on-die or on-package decoupling removes it, so Vddq needs an extremely low-inductance path (else ground bounce). Differential I/O has zero net return current. | I = (Vddq/2)/Z0 per driver; I_bus = N x I | Vddq, Z0, N | Series-terminated SE buses | calc | p.184 | high |
| RITCHEY-251 | thermal | Keep Tj below ~100 C: failure rates of mechanisms such as aluminium electromigration scale with absolute temperature (K) to the 4th power; CMOS speed degrades ~0.2% per C. Cooling guide: ~2 W easy; 5-10 W through PCB copper planes if the chip-to-PCB path is reasonable; 25-50 W needs a large heat sink and a few hundred lfm airflow; > 100 W needs heat pipes or liquid. | Tj <= 100 C; speed -0.2%/C | P, airflow | — | calc | p.184 | high |
| RITCHEY-252 | pdn | Core current estimation for CMOS: SPICE each cell (load capacitance, input rise time), apply activity factors per section in a spreadsheet; the clock tree and its DFFs switch every cycle and dominate the fast transient. Work in CHARGE per edge: I_peak ~ Q/t_pulse, P = Q x Vdd x f_clk. Example (0.13 um, 1.5 V, 500 MHz, 550k DFFs, 100 fF per DFF, 300 ps skew -> 150 ps pulse): idle 18.50 nC -> 123 A, 13.9 W; heavy 32.54 nC -> 217 A, 24.4 W; idle ~30% of max; whole chip ~45 W. | I_pk = Q/t_w; P = Q x V x f | cell charges, activity | — | calc | p.184-186, Table 10.1 | high |
| RITCHEY-253 | pdn | On-chip decoupling: idle CMOS cells supply some Vdd-Vss capacitance but not enough; thin-gate-oxide capacitor cells add the rest; high-power chips typically have > 50 nF on die. Equivalent core PDS (Fig 10.14): 200 A / 150 ps load, 50 nF on chip, 0.4 uF on package, then package balls, PCB planes and PCB capacitors. | C_die > 50 nF | — | High-power ASIC | review | p.186-187, Fig 10.14 | high |
| RITCHEY-254 | pdn | Each PDS element works only over a band (Table 10.2): power supply DC-5 kHz; PCB bulk capacitors 5 kHz-2 MHz; PCB ceramic capacitors 2-100 MHz; package power balls DC-100 MHz; package decoupling capacitors 50-500 MHz; chip power balls DC-500 MHz; on-chip decoupling above 500 MHz. The board-level PDS owns up to ~100 MHz; above that the package and die must carry the load. | — | — | — | review | p.187, Table 10.2 | high |
| RITCHEY-255 | decoupling | Capacitor ESL scales with body size and inversely with terminal count: conventional 0603/0402 (< 1 cent) > reverse-geometry 0612/0306 (several cents; need multiple vias per pad to realize low ESL) > 8-terminal inter-digitated (IDC 0612, 0508) > 16-terminal LICA (4 x 4 array, 400 um pitch, checkerboard V/G, four capacitors, most expensive). On-package ESL: 360 / 270 / 228 / 165 / 150 / 120 / 25 pH (Table 10.3). | — | — | Mounted on organic package | inspect | p.187-189, Table 10.3 | high |
| RITCHEY-256 | decoupling | The same capacitor has higher ESL on a PCB than on a package (0402: 450 pH on PCB vs 270 pH on package) because packages use thinner dielectrics and micro-vias; use footprints with multiple vias directly under or at the inner ends of the terminals. Low-ESL capacitors are pointless unless the IC-to-capacitor connection is also low inductance. | L_0402 = 450 pH (PCB), 270 pH (package) | — | — | inspect | p.189-190, Fig 10.17 | high |
| RITCHEY-257 | pdn | Plane-pair inductance: treat the pair as a wide transmission line. C = e0 x er x A / T (e0 = 8.854e-14 F/cm); Z0 = 100 x sqrt(er) / (3 x C[pF per cm of a 1 cm wide strip]) ohm; L = Z0^2 x C. Example er = 4.0, T = 75 um: C = 47.2 pF/cm^2, Z0 = 1.41 ohm, L = 94 pH per square; scale like sheet resistance (squares = length/width). Equivalent: L_sq = mu0 x T (derived). | L_sq = 94 pH at T = 75 um | er, T | Plane pairs in package or PCB | calc | p.190-191, Eqs 10.1-10.4 | high |
| RITCHEY-258 | pdn | Spreading inductance of a plane pair between a central die (radius R1) and a ring of capacitors or pins (radius R2): L = (Lsq / (2*pi)) x ln(R2/R1). Example: Lsq 94 pH, R1 = 8 mm, R2 = 16 mm -> 10.4 pH. Plane-pair inductance is independent of er and directly proportional to the dielectric thickness: planes on adjacent layers at 25 um -> Lsq 31 pH, ring 3.5 pH. Put plane pairs on adjacent layers with the thinnest dielectric. | L = Lsq/(2 pi) x ln(R2/R1) | Lsq, R1, R2 | — | calc | p.192, Eq 10.5 | high |
| RITCHEY-259 | pdn | Loop inductance of one wire turn (estimate for adjacent power/ground ball or pin pairs): L = 10 x R x (7.353 x log10(16 R / D) - 6.386) nH, R = loop radius (in), D = wire/ball diameter (in), valid for R > 2.5 D; for a ball pair R = half the ball pitch. 1.0 mm BGA (R = 0.020 in, D = 0.008 in): 1.06 nH. Table 10.4 adjacent-ball loops: 1.27 mm package 1.35 nH; 1.0 mm package 1.06 nH; LICA 0.4 mm 0.42 nH; chip C4 0.225 mm 0.24 nH. | L[nH] = 10 R (7.353 log10(16R/D) - 6.386) | R, D | R > 2.5 D | calc | p.192-193, Eq 10.6, Table 10.4 | high |
| RITCHEY-260 | pdn | Ball-array inductance: every adjacent V-G ball pair is one loop and loops add in parallel; fields concentrate between opposite-polarity neighbours, so adjacent same-polarity balls add little. Assign power/ground in a CHECKERBOARD. LICA 16-ball footprint: column assignment = 12 parallel loops x ~420 pH -> ~35 pH; checkerboard doubles the adjacent V-G loops -> ~18 pH (best measured LICA ESL 25 pH on a build-up package with short vias and 25 um plane dielectric, including vias and planes). Same principle for package core-power balls. | L_total ~ L_loop / N_loops | ball map | — | calc | p.193-194, Figs 10.22-10.23 | high |
| RITCHEY-261 | termination | Series termination (one driver, one load) suits lines whose round-trip delay is less than the data period and dissipates less than DC (parallel) termination; parallel termination suits data rates faster than the round trip at the cost of continuous current. Series-terminated driver current pulse = (V/2)/Z0 for one round trip; parallel-terminated current flows as long as the driver is on. | series OK if 2 x t_line < t_bit | line delay, bit time | — | calc | p.194-195 | high |
| RITCHEY-262 | pdn | Budget I/O current per bus (Table 10.5, SPI-4.1): 85 signals + clock, HSTL, 50 ohm, series-terminated, 10 in (1.67 ns), 200 MHz / 200 Mb/s, Vddq 1.8 V -> 18 mA per driver, 0.4 ns rise, 3.33 ns current pulse, max total 1.53 A, typical 460 mW. Six 2.5 V DDR1 ports at 333 MHz can pulse 13.8 A. For package/PDS design what matters is the rise time and amplitude of the aggregate current pulse, not the termination style. | I_bus = N x (Vddq/2)/Z0; t_pulse = 2 x t_line | N, Vddq, Z0, length | — | calc | p.194-195, Table 10.5 | high |
| RITCHEY-263 | pdn | Differential (LVDS) buses draw nearly constant supply current (current only changes direction; signal and return equal and opposite -> constant package current). SPI-4.2 (Table 10.6): 17 pairs + clock, LVDS, 100 ohm differential, 100 ohm parallel termination, 400 MHz / 800 Mb/s, Vddq 2.5 V, 6 mA drive, 0.2 ns rise, DC current, total 108 mA, 270 mW — 4x the data rate of SPI-4.1 on under half the pins. | — | — | — | calc | p.195-196, Table 10.6 | high |
| RITCHEY-264 | components | Differential signalling: advantages — constant supply current, equal/opposite signal and return currents, plane-coupled noise common to both lines, immunity to ground/supply shifts between parts, much higher speed; disadvantage — twice the wires. Coupling from ADJACENT TRACES is not equal on the two lines. Two driver classes: constant-current (short/slower links) and pre-emphasis (long lossy links); currents stay equal and opposite in both. | — | — | — | review | p.195 | high |
| RITCHEY-265 | return-path | Package signal wires are transmission lines needing adjacent power/ground planes, and every package signal ball (chip side and PCB side) needs adjacent Vddq/GND balls. Otherwise return current detours to the next nearest path (e.g., power balls under the die centre), several signals share one high-impedance return, and the resulting rail pulse passes through the low-impedance drivers of quiet lines onto their outputs (ground bounce) or couples into neighbours. I/O equivalent circuit (Fig 10.24): on-chip Vddq capacitance 100 pF, on-package Vddq cap 0.1 uF, ~3 pF per signal ball, 50 ohm package and PCB lines. | — | — | — | inspect | p.196-197, Fig 10.24 | high |
| RITCHEY-266 | decoupling | I/O-rail decoupling (Vddq-Vss on chip or package) cannot remove the return current or change its frequency content; it only adds a parallel return path (about half the current returns through the Vddq balls), cutting ground-bounce spikes by up to 50%. All return current still enters the PCB with the drive current's rise time. | bounce reduction <= 50% | — | — | review | p.197-198, Figs 10.25-10.27 | high |
| RITCHEY-267 | components | Organic BGA construction: drilled/plated thick epoxy-glass core, build-up layers with micro-vias, solder mask both faces, C4 balls on top, eutectic or SAC balls below; 6 or 8 copper layers most common (up to 10); much lower NRE than ceramic. Six-layer stackup in Table 10.7 (§2 T35), total 1.130 mm. | — | — | — | review | p.198-199, Fig 10.28, Table 10.7 | high |
| RITCHEY-268 | components | Package design responsibility: package fabs supply JEDEC body sizes/ball counts and mechanical reliability but usually lack ASIC electrical knowledge; the ASIC designer chooses body size, ball count, layer count, capacitor type/quantity, eutectic vs SAC balls, and specifies C4 ball assignment, layer assignment (power/ground/signal), per-layer layout rules, capacitor placement and package ball assignment. Chip and package must be co-designed. | — | — | — | review | p.198, p.210 | high |
| RITCHEY-269 | components | Poor BGA package signatures (Fig 10.29, 6-layer): no core Vdd plane (Vdd reaches the PCB only through centre balls; Vdd/GND copper under the die chopped into segments) -> activity-dependent core ripple, large clock jitter, intermittent high-speed failures; no decoupling capacitors, or capacitors reached through high-inductance traces; few power/ground balls at the edge where the signals are -> ground bounce and edge jitter; edge ground balls tied only to the bottom Vss layer; perimeter-only I/O drivers whose Vddq/GND C4 balls sit inboard on lower planes -> slotted Vddq/GND planes under the signals. | — | — | — | review | p.199-200, Fig 10.29 | high |
| RITCHEY-270 | components | Good BGA package signatures (Fig 10.30, 8-layer): continuous Vdd and Vss planes over the whole package (Vddq layer may be split into pie sections for multiple I/O voltages); core Vdd balls around the die perimeter as well as the centre; package-top decoupling capacitors fed through continuous low-inductance plane pairs; signal C4 balls spread over the whole die so planes have round antipads, not slits; every chip and package signal ball adjacent to a power and a ground ball. | — | — | — | review | p.200, Fig 10.30 | high |
| RITCHEY-271 | components | Good package ball map (PKG-B vs PKG-A, 1088 balls, 34.5 mm body, 12 mm die, 760 signals each): checkerboard Vdd/GND under the die (144 pairs vs 46); Vddq balls interspersed with the signal balls; every signal ball adjacent to two PWR/GND balls; core Vdd balls also around the perimeter; no clusters of same-type power balls or of adjacent signal balls. PKG-A: 224 GND / 50 Vdd / 54 Vddq; PKG-B: 164 GND / 96 Vdd / 68 Vddq. | — | ball map | — | inspect | p.201-203, Figs 10.31-10.32, Table 10.8 | high |
| RITCHEY-272 | pdn | Package vias and antipads (~2 mil) are far smaller than PCB ones, so package planes have lower R and L than the Swiss-cheesed PCB planes under the package; perimeter Vdd balls let core current reach solid PCB plane outside the footprint, in parallel with the centre path. | — | — | — | review | p.202 | high |
| RITCHEY-273 | pdn | Package-to-PCB ESL budget (Table 10.10): PKG-A — 46 core pairs x 1.0 nH -> 21.7 pH, plus PCB plane spreading 23.8 pH (Eq 10.5, R1 = 6 mm, R2 = 17 mm) = 45.5 pH. PKG-B — 144 pairs -> 6.9 pH + 23.8 pH = 30.7 pH centre path, in parallel with an edge path (package planes 12.0 pH + 168 edge pairs x 2.0 nH -> 11.9 pH = 23.9 pH) -> 13.4 pH total. | L_pairs = L_loop / N; L_par = 1/sum(1/L_i) | — | — | calc | p.203-204, Table 10.10, Fig 10.33 | high |
| RITCHEY-274 | decoupling | On-package capacitors are useless if their ESL is large relative to the package-to-PCB inductance: PKG-A's four 0402s (100 nF, 500 pH each) did nothing against its 45.5 pH path; PKG-B's four LICAs (72 nF, 25 pH) bridged the resonance. On-chip capacitance PKG-A 20 nF vs PKG-B 50 nF (Table 10.9). | ESL_caps / n << L_pkg-to-PCB | — | — | calc | p.203-205, Table 10.9 | high |
| RITCHEY-275 | pdn | Check the parallel resonance of package inductance with on-chip capacitance: f_res = 1/(2 pi sqrt(L_pkg x C_die)). PKG-A (45.5 pH, 20 nF) resonated at ~170 MHz above 50 mohm — fit only for very low power chips; PKG-B stayed below 7 mohm over the whole range. | f_res = 1/(2 pi sqrt(L C)) | L_pkg, C_die | — | calc | p.204-205, Figs 10.34-10.35 (confirm by sim) | high |
| RITCHEY-276 | pdn | Core ripple check: ripple_pp = Z_max x dI. 20 W 130 nm chip at 1.5 V draws 13.3 A; a 50% step (6.66 A) x 7 mohm (PKG-B) = ~47 mV = 3% of supply; x 50 mohm (PKG-A) -> ~21% ripple (serious performance problem). | V_ripple = Z x dI | P, V, step fraction, Z | — | calc | p.205 | high |
| RITCHEY-277 | components | Reference good package (EIT HyperBGA, 1657 balls, 42.5 mm; 17 mm die; eight LICAs on a 16 mm-radius ring, each split between core Vdd and one of eight Vddq rails): 53 um Copper/Invar/Copper core used as ground; PTFE build-up (low loss, fast propagation); nine conductor layers; every signal wire a controlled-impedance line with adjacent PWR/GND balls at both ends; I/O drivers over the entire die; ~100 nF on chip; checkerboard Vdd/GND centre with Vdd and Vddq balls near the edge; uniform PWR/GND array in the signal area. Lowest jitter and cleanest eye of the three packages measured. | — | — | — | review | p.191, p.206-207, Figs 10.36-10.37 | high |
| RITCHEY-278 | components | Xilinx Virtex-2 FF1517 problems (typical of many ASIC/FPGA packages): core ball assignment cannot give low PDS impedance at high frequency (large clock jitter); large clusters of adjacent signal balls at the edges (coupling). Virtex-4 FF1148 "Sparse Chevron": every signal ball adjacent to at least one PWR/GND ball, partial checkerboard core -> very good (97 ps jitter), slightly behind HyperBGA but more than adequate for an FPGA's many I/O banks. | — | — | — | review | p.208-209, Figs 10.38-10.39 | high |
| RITCHEY-279 | components | IC package screening at part selection: ask the IC maker how the package is designed and characterized; if it is not, test before committing. A vendor demo board may exercise only the showcased function (one FPGA's serial links looked fine alone but degraded severely with the parallel I/O active); if no suitable demo board exists, build a test PCB that exercises the IC under the intended conditions (Vol.1 Ch.38 method). | — | — | — | measure | p.210 | high |
| RITCHEY-280 | pdn | A package PDS must work from DC to several GHz even for chips clocked at only a few hundred MHz. | — | — | — | review | p.210 | high |
| RITCHEY-281 | grounding | Analog ground (reference for analog measurements) must connect to digital ground directly under any component that contains both analog and digital functions. | — | — | Mixed-signal ICs | inspect | p.211 (Glossary: Analog ground) | high |
| RITCHEY-282 | via | Aspect ratios above 6:1 are not considered candidates for volume production (consistent with the 6:1 standard-process column of Fig 4.79; 8:1 and 10:1 only at capable fabs). | AR <= 6:1 for volume | t_pcb, drill | — | calc | p.212 (Glossary: Aspect ratio) | high |
| RITCHEY-283 | timing | Detour routing (longer than Manhattan distance) of some bus members while others route minimum distance causes timing problems; constrain bus members together. | — | — | Parallel buses | inspect | p.216 (Glossary: Detour routing) | high |
| RITCHEY-284 | fab | Desmear (removing resin smeared over inner-layer copper by drilling) is mandatory; skipping it causes open plated through holes. | — | — | — | review | p.216 (Glossary: Desmear) | high |
| RITCHEY-285 | test | Rise/fall time is measured 10%-90% (90%-10% for fall), except 20%-80% for GaAs and ECL; do not confuse edge rate (V/ns) with rise time. | — | — | — | measure | p.217-218 (Glossary) | high |
| RITCHEY-286 | dfm | Gridded routing works best with regular pin pitch and more than four signal layers; gridless routing is valuable on 2- and 4-layer boards and less so beyond four signal layers. | — | layer count | — | review | p.220 (Glossary) | medium |
| RITCHEY-287 | process | IPC-2141 (replaced IPC-D-317), the IPC high-speed design specification, was written by a volunteer committee without rigorous technical review and contains many unvalidated, imprecise rules of thumb; do not adopt its rules without the RITCHEY-008 test. | — | — | — | review | p.222 (Glossary: IPC-2141) | high |
| RITCHEY-288 | process | No rule of thumb (neither a shortcut derived from detailed calculation nor an empirical "it changed something" observation) belongs in a final design rule set. | — | — | — | review | p.229 (Glossary: Rule of thumb) | high |
| RITCHEY-289 | termination | Incident-wave switching: full-amplitude launch absorbed by an end parallel termination, so data are valid all along the line as the wave passes each load. Reflected-wave switching: half-amplitude launch through a series termination that doubles at the open end, full amplitude along the line only after the reflection returns. Multi-load nets therefore favour incident-wave (parallel) termination. | — | load count | — | review | p.222, p.228 (Glossary) | medium |
| RITCHEY-290 | transmission-line | Overshoot occurs where the downstream impedance is higher than upstream; undershoot (ring-back) where it is lower; undershoot is not tied to edge polarity. | — | Z upstream, Z downstream | — | review | p.226, p.233 (Glossary) | high |
| RITCHEY-291 | protection | Excessive overshoot can trigger parasitic SCR structures between IC inputs/outputs (latch-up-type failures) — another reason to hold inputs within Vdd + 0.3 V. | — | — | — | sim | p.230 (Glossary: SCR) | high |
| RITCHEY-292 | via | Minimum annular ring is measured at the narrowest point between the pad edge and the edge of the DRILLED hole (not the plating edge). | — | — | — | inspect | p.225 (Glossary) | high |
| RITCHEY-293 | fab | Negative etch-back (inner copper recessed from the hole wall) is undesirable (poor plating-to-inner-layer contact); nail-heading (flared inner copper) indicates drill wobble. | — | — | Microsection | inspect | p.225 (Glossary) | high |
| RITCHEY-294 | compliance | RoHS (EU, effective July 1, 2006) restricts Pb, Cd, Hg, hexavalent Cr, PBB and PBDE in electrical/electronic equipment rated <= 1000 VAC / 1500 VDC. | — | — | — | review | p.229 (Glossary: RoHS) | high |
| RITCHEY-295 | termination | SSTL memory buses put a small series resistor, usually 22 ohm, between each module stub and the main bus; this limits performance at fast edges and high clock rates. | R ~ 22 ohm | — | — | inspect | p.231 (Glossary: SSTL) | high |
| RITCHEY-296 | fab | Reasons to plug vias: seal them for vacuum test fixtures; protect via copper from later etching; restore a flat pad (plate over the plug). | — | — | — | review | p.233-234 (Glossary) | high |
| RITCHEY-297 | emc | An unshielded wire leaving a Faraday cage is a monopole antenna; two PCBs joined by a connector form a dipole; each needs shielding, filtering or a cage. | — | — | — | review | p.217, p.225 (Glossary) | high |
| RITCHEY-298 | timing | Unit interval UI = 1 / bit rate (2.4 Gb/s -> 416 ps); EM propagation ~1 ft/ns (30.3 cm) in vacuum, ~6 in/ns in PCB; ISI becomes noticeable as data rates approach 1 Gb/s. | UI = 1/R_bit | bit rate | — | calc | p.222, p.225, p.233 (Glossary) | high |
| RITCHEY-299 | materials | Appendix-1 laminate summary: Isola FR406 (high-performance epoxy) Tg 170 C, Td 295 C, Df 0.017-0.022; FR408 (lead-free compatible, mid Dk/Df) Tg 180 C, Td 360 C, Df 0.010-0.013; IS410 (phenolic-epoxy, lead-free) Tg 170 C, Td 350 C, Df 0.02-0.028; IS620 (low Dk/Df, high speed) Tg 225 C, Td 363 C, Df 0.0084-0.0095; Nelco N4000-13 Tg 210 C Df 0.014; N4000-13SI (S-glass) Tg 210 C Df 0.009; N4000-29 (lead-free Hi-Tg commercial) Tg 180 C Df 0.016; Rogers R/Flex 3000 (flex) Df 0.0025; Rogers 4000 series Df 0.003. | — | material | Data current as of 2006; recheck supplier sites | inspect | p.236 | high |
| RITCHEY-300 | materials | Dk and Df depend on construction and resin content: higher resin content gives lower Dk and higher Df (FR408 at 2 GHz: 1-106, 63% resin -> Dk 3.49, Df 0.0128; 9-7628, 37% -> Dk 4.15, Df 0.0102). Take each opening's Dk from the supplier's construction table and name that construction on the drawing; the Appendix-1 data is accurate enough to design stackups that hit impedance. | — | construction, resin % | — | calc | p.236-240, §2 T38-T41 | high |
| RITCHEY-301 | materials | Dk falls slightly and Df rises with frequency (FR406 1-1080: Dk 3.75 -> 3.65 and Df 0.0205 -> 0.0213 from 2 to 10 GHz; FR408 1-106: Dk 3.49 / 3.48 / 3.47 at 2 / 5 / 10 GHz). | — | f | — | calc | p.237-240 | high |
| RITCHEY-302 | test | Three PDS verification tests: (1) bare-board plane capacitance per supply (capacitance meter, low frequency, any location); (2) PDS impedance vs frequency, 10 kHz-1 GHz, on a board assembled with only the bypass capacitors; (3) worst-case ripple on the fully operating board under worst-case loading. | — | — | — | measure | p.253 (App. 2) | high |
| RITCHEY-303 | pdn | Size plane capacitance with margin: the DC (meter) value exceeds the value at 100 MHz-1 GHz (er falls with frequency) — design the DC value larger by the er change from DC to 1 GHz; the biggest variable is plane spacing (especially across prepreg); the nominal plane capacitor may need to be at least 50% larger than what the switching events require. | C_nominal >= 1.5 x C_required (plus er(DC)/er(1 GHz)) | C_required, er(f), spacing tol | — | calc | p.253 (App. 2) | high |
| RITCHEY-304 | test | Shunt impedance measurement with spectrum analyzer + tracking generator: generator and analyzer each connect through 50 ohm coax to the same plane pair; connecting the generator directly to the analyzer sets the 25 ohm reference at the top of the screen; each -20 dB is one decade lower impedance (-20 dB = 2.5 ohm, -40 dB = 0.25 ohm, -60 dB = 25 mohm, -80 dB = 2.5 mohm). Settings (Agilent E4401B): 10 kHz-1 GHz, RBW 3 kHz, VBW 3 kHz, attenuation 10 dB, reference 0 dBm, log frequency axis, sweep 2.765 s, auto-sweep coupling SR, source 0 dBm. A network analyzer is the alternative. | Z = 25 ohm x 10^(dB/20) | analyzer reading (dB rel. calibration) | Z << 25 ohm | measure | p.253-258 (App. 2) | high |
| RITCHEY-305 | test | Low-inductance probing: probes from SR-141 semi-rigid coax, male SMA one end, stiff needle tip (sewing needle) mating the plane-access test structure (44 mil pads, 50 mil clearance, 30 mil drill, 75 mil pitch, two per rail >= 1 in apart); without test structures remove two 0603 capacitors and solder coax onto their pads; the two connections need only be far enough apart not to share inductance. | — | — | — | inspect | p.259-261 (App. 2) | high |
| RITCHEY-306 | pdn | Reject PDS impedance peaks such as ~0.5 ohm at 70 MHz (bypass-capacitor ESL resonating with the plane capacitor); they are likely to cause intermittent failures. | — | Z(f) sweep | — | measure | p.261 (App. 2), Fig 18 | high |
| RITCHEY-307 | bringup | Worst-case ripple test: bring-up software must repetitively exercise (a) the widest single-ended buses switching all 0 -> 1 simultaneously and (b) processors transitioning standby -> full operation, while each supply's ripple is measured with a scope whose bandwidth covers the highest signal frequencies. | — | — | — | measure | p.262 (App. 2) | high |
| RITCHEY-308 | pdn | Keep every rail's PDS impedance low from DC to ~1 GHz (last useful signal frequency) even if its own loads do not need it, so signals may route over any plane without ripple coupling and routing need not be restricted to ground planes. | — | — | — | measure | p.262-263 (App. 2) | high |
| RITCHEY-309 | process | Fab specification precedence: purchase order > fabrication drawing / CAD data > general fab spec > reference documents. Default IPC-6011 / IPC-6012 Class 2 where no reference is named. Fabricators from the approved manufacturer list, ISO 9002 or better, subject to audits. | — | — | — | review | p.269-270 (App. 3 §1-3) | high |
| RITCHEY-310 | fab | First article per part number: sample at General Inspection Level I (ANSI/ASQC Z1.4-1993); inspect per IPC-TM-650 — all drawing dimensions, bow/twist, hi-pot (multilayer), solderability, cosmetics per IPC-6012 3.3.1-3.3.9, microsections (IPC-TM-650 2.1.1 / 2.1.1.2) cut from reject or non-functional boards (never coupons, never from shipped arrays), ionic contamination, TDR impedance report, 100% e-test certificate, UL listing of materials; retain samples, sections and report 1 year; no further shipments until approval. Production lots: sampling S-1 and a production test report with each lot. | — | — | — | inspect | p.269-270 (App. 3 §2.5-2.6) | high |
| RITCHEY-311 | assembly | Board marking: manufacturer ID/logo and date code (year + calendar week); UL 94V-0 mark (the fabricator obtains and maintains UL recognition); markings on the part-number side, never touching the conductive pattern; no country of origin on the board; legend inks per IPC-SM-840 Class T. | — | — | — | inspect | p.271-272 (App.3 §4) | high |
| RITCHEY-312 | fab | Fabricator CAD-data handling: Gerber-to-net-list compare against IPC-D-356 before fabrication (resolve every difference); per-layer DRC against the README parameters; confirm part number / revision / dash; written discrepancy report before production. Only permitted data changes: etch compensation, breakaway markings, text clipping to keep 0.006 in from solderable surfaces, solid copper in breakaway areas kept 0.015-0.050 in from the profile. No thieving inside the outline without written approval; never remove stacking stripes; no added teardrops unless specified (report conditions that need them). | text-to-pad >= 0.006 in; breakaway copper 0.015-0.050 in from profile | — | — | inspect | p.272-273 (App.3 §5) | high |
| RITCHEY-313 | materials | Default laminate (App 3 §6.1): FR-4 prepreg and laminate per IPC-4101; minimum dielectric 0.002 in with IPC-4101 Class B thickness tolerance; permittivity as on the fabrication drawing; resin Tg >= 170 C by TMA; 0.5 oz copper on external and internal layers (IPC-MF-150; coated foil IPC-CF-148); no mid-order process or material change without written approval. | t_diel >= 2 mil; Tg >= 170 C | — | — | inspect | p.273 | high |
| RITCHEY-314 | materials | Multilayer construction (App 3 §6.2): glass warp direction aligned in every core and prepreg of a board; no blistering, delamination, measling, weave exposure or pink ring anywhere inside the profile (beyond IPC-A-600 Class 2); layer-to-layer registration ±0.005 in any layer to any other; every laminate/prepreg opening >= 2 plies with resin content >= 55% in signal/plane openings; only 106, 1080, 2116 and 3313 glass next to signal layers; single plies allowed between adjacent power planes with resin content down to 42%. (The Fig 4.78 fab notes instead allow 106/1080/2113/2116/2313/3313 and >= 50% resin.) | registration ±5 mil; RC >= 55%; >= 2 plies | — | — | inspect | p.273-274 | high |
| RITCHEY-315 | dfm | Mechanical tolerances (App 3 §7.1-7.4): non-plated tooling holes located ±0.003 in from datum, size +0.002/-0.001 in, drilled in the primary drill operation, clean; all other features incl. the profile ±0.005 in from datum; conductive features >= 0.020 in from the finished edge; non-plated holes and slots ±0.005 in. | edge clearance >= 20 mil | — | — | inspect | p.274 | high |
| RITCHEY-316 | fab | Board thickness is measured over solder-mask-coated conductors on both sides (no edge fingers), over the finished fingers (edge-finger boards), or over fiducial metal (PCMCIA). Fiducials: circular, flat within 0.0006 in, all fiducials on a board within 0.001 in of each other in size. | — | — | — | measure | p.274 | high |
| RITCHEY-317 | fab | Conductor tolerances (App 3 §7.7): finished trace width and space within the lesser of ±20% of the Gerber value or ±0.001 in (1/2 oz) / ±0.002 in (1 oz); edge roughness <= 0.0005 in peak-to-valley over any 0.50 in; SMT pads at 0.025 in pitch ±0.0014 in, below 0.025 in pitch ±0.0010 in (measured at pad top); plated holes ±0.003 in; plated slots ±0.005 in. (Fig 4.78 fab notes are tighter: inner ±0.5 mil, outer ±1.0 mil.) | — | — | — | inspect | p.275 | high |
| RITCHEY-318 | fab | Annular ring per IPC-6012 Class 3 (internal: drilled-hole edge to pad edge; external: plated-hole inside edge to pad outer edge); tangency acceptable only where no trace enters the pad; breakout on any functional plated hole rejects that board, and breakout on more than one board may reject the lot. | — | — | — | inspect | p.275 | high |
| RITCHEY-319 | fab | Bow and twist <= 0.007 in/in (IPC-6012); mandatory smear removal before metallization with no smear visible at 100X in microsection; nail-heading <= 2 x copper foil thickness; negative etch-back from nail-heading <= 0.005 in (as printed). | bow/twist <= 0.7% | — | — | measure | p.275-276 | high |
| RITCHEY-320 | fab | Board edges: routed-edge finish Ra <= 24 um; V-scored profiles still within ±0.005 in with conductors >= 0.020 in from the edge; finger edges chamfered/bevelled per drawing; breakaway residue within ±0.005 in of the outline. | — | — | — | inspect | p.276, p.283 | high |
| RITCHEY-321 | fab | Repairs (IPC-7711/7721, Class 2, highest conformance level): no inner-layer repairs on a completed multilayer; outer-layer trace repair by welding only, only on traces > 0.006 in wide, <= 2 weld repairs per side and 3 per board; exposed copper touched up with liquid mask; <= 3 mask touch-ups per side, each <= the lesser of 1 in long or 0.125 in^2; outer-layer etch rework only if adjacent circuitry is not exposed or damaged. | — | — | — | inspect | p.276 | high |
| RITCHEY-322 | fab | Cleanliness: ionic contamination <= 6.45 ug NaCl-equivalent per in^2; no flux residues; laminate free of processing discoloration (a brownish tint from overheating rejects). | <= 6.45 ug/in^2 | — | — | measure | p.276-278 | high |
| RITCHEY-323 | solder | Solderability: ANSI/J-STD-003 with exposure extended to 20 s and >= 95% of tested surfaces fully wetted; finishes must stay solderable with VOC-free no-clean flux for >= 6 months after receipt in the unopened package. | >= 95% wetting | — | — | measure | p.276-277 | high |
| RITCHEY-324 | fab | Copper plating: total copper on all conductors >= 0.001 in; no nodules, pits or poor adhesion; undercut <= 1:1 etch factor per side; electrodeposited copper elongation >= 10%; PTH wall average >= 0.001 in; drawing hole sizes are DRILLED sizes; <= 1 void per PTH covering <= 5% of the wall; inclusions may reduce minimum copper by <= 20% and never in the same plane on both walls; no inner-layer-to-barrel separation; no separation between plating layers or from the electroless/direct metallization. | Cu >= 1 mil; elongation >= 10% | — | — | measure | p.277 (microsection) | high |
| RITCHEY-325 | fab | HASL (if used): SN60 or SN63 solder per J-STD-003; <= 2 HASL passes; solder in PTH 0.0001-0.0035 in; 0.025 in pitch SMT pads 0.0001-0.0015 in; < 0.025 in pitch pads 0.0001-0.0010 in with <= 0.0006 in variation across one array; verify with six measurements in both axes at pad centre. | — | — | — | measure | p.277-278 | high |
| RITCHEY-326 | fab | Edge-finger plating: nickel per QQ-N-290, 200 uin +300/-100 uin; gold 99.7% purity, density 19.3 g/cm^3, Knoop 140-200, >= 30 uin average (no reading < 20 uin); roughness <= 20 uin CLA in the mating direction; no exposed Ni/Cu except at bevelled tips; exposed copper at the demarcation line <= 0.005 in and no solder below it; tape adhesion per IPC-TM-650 2.4.1; plating projections may not reduce finger spacing by more than 20%; keying slots must not cut conductors. | — | — | — | measure | p.278 | high |
| RITCHEY-327 | fab | ENIG thickness: electroless nickel >= 100 uin average (no reading < 80 uin); immersion gold >= 4 uin average (no reading < 3 uin), maximum 10 uin. | Ni >= 100 uin; Au 4-10 uin | — | — | measure | p.279 | high |
| RITCHEY-328 | fab | OSP: only ENTEK Plus CU-106A (0.35 ± 0.05 um, measured by UV photospectrometer) or Ronacoat imidazole (<= 0.001 mil passivation); never bake OSP boards; ship within 3 months of OSP application. | — | — | — | measure | p.279 | high |
| RITCHEY-329 | fab | Electroplated Ni/Au body finish (App 3 §8.7): nickel 150-600 uin nominal; gold (soft or hard) 5-15 uin nominal so gold is < 5% by volume of the finished joint; optional palladium 5-15 uin between; selective extra gold >= 20 uin only where socket contacts need it (second plating operation). | Au 5-15 uin; Ni 150-600 uin | — | — | measure | p.279-280 | high |
| RITCHEY-330 | fab | Solder mask: IPC-SM-840 Class T; hot-oil test IPC-TM-650 2.4.6; zero loss in the tape test on Ni and Au; green; approved liquid matte LPI masks Electra EMP110LGXM1399USR (hardener #1348 on Ni/Au, #1123 for HASL/TAB), Enthone DSR 3241M, Taiyo PSR 4000 MP, Enthone DSR 3241 CRI; one layer only; cured thickness 0.0004-0.0012 in over copper plane; no mask in PTHs; minimum mask web 0.004 in between exposed features; test pads, fiducials, SMT pads and tooling holes mask-free. | mask 0.4-1.2 mil; web >= 4 mil | — | — | inspect | p.280 | high |
| RITCHEY-331 | fab | Via plugging (vias <= 0.020 in, when specified): plug with solder mask after final plating; solder-side cap overlaps the primary mask by > 0.004 in and is <= 0.001 in thick above it; no broken plugs. Via masking: <= 5% of masked vias broken; mask in the barrel acceptable. BGA via damming (alternative to plugging): second mask pass of annular rings around the BGA pads, ring width = length of the pad-to-via trace. | — | — | — | inspect | p.281 | high |
| RITCHEY-332 | fab | Legend: <= 0.001 in thick over the mask; applied before any OSP; never on PTH pads, SMD pads, fiducials or edge fingers; white or yellow epoxy, non-flammable, non-conductive, non-hygroscopic, survives 288 C for 30 s and the tape test; laser-defined legend Hysol 50-202 BC cured 0.7-1.1 mil (cross-section every date code); registration within 0.010 in of the primary tooling hole vs Gerber. | — | — | — | inspect | p.281-282 | high |
| RITCHEY-333 | test | Bare-board e-test: 100% continuity and isolation of every net end point and branch against the verified net list at >= 40 VDC, continuity cutoff <= 10 ohm; golden-board testing not allowed; hard fixture probing both sides at once (probing an adjacent via instead of an SMT pad is not acceptable); flying probe acceptable for prototypes or orders < 50 boards; hi-pot (when specified) per IPC-TM-650 2.5.7 Condition B on every plane; pass mark not on pads, test points, fiducials or fingers. | V_test >= 40 VDC; R_cont <= 10 ohm | — | — | measure | p.282 | high |
| RITCHEY-334 | test | Multilayer insulation resistance >= 500 Mohm between any two conductors at 500 VDC, as received (IPC-6012 3.9.4). | IR >= 500 Mohm @ 500 VDC | — | — | measure | p.282 | high |
| RITCHEY-335 | test | Impedance acceptance: ±10% on designated layers, measured on the test traces defined on the fabrication drawing (coupons only if none are defined), AQL sampling, reference step amplitude measured and used in every reading, assumed permittivity 4.1, TDR rise time < 200 ps unless specified; automatic data acquisition (removes cursor-placement variation) and SPC against control limits; feedback to front-end engineering including cross-sections of passing and failing boards. | tol ±10%; tr_TDR < 200 ps | — | — | measure | p.282-283 | high |
| RITCHEY-336 | fab | Packaging: clean, dry, cooled boards; no panels containing coupons or not-per-print deviations; manual-lift containers <= 50 lb; no out-of-plane deformation; boards individually packaged, same orientation, no paper separators, no contact preservatives, tightly held; one facility/part/revision/PO per package; each shipment carries the first-article or production test report; storage life >= 6 months without corrosion, fingerprints, mold or solderability loss; vacuum pack in sulfur-free wrap, or heat-sealed bag with sulfur-free desiccant and humidity indicator; sulfur-free cardboard outers, no polystyrene; no single boards cut from ordered arrays. Max per innermost package: > 60 in^2 -> 25; > 20 to 60 in^2 -> 250; <= 20 in^2 -> 360; PCMCIA -> 1200. | — | — | — | inspect | p.283-285 | high |
| RITCHEY-337 | test | All-SMT boards: provide surface-mount scope ground loops (e.g., Keystone 5016/5018, Components Corp TP-107) instead of through-hole 25 mil wire-wrap posts, which force an extra wave-solder step. | — | — | — | inspect | p.299-300 (App.8) | high |
| RITCHEY-338 | via | Aspect-ratio manufacturability (App 10): AR = board thickness / drilled diameter (§2 T46). The five colour-coded classes are lost in extraction: any good fab; many but not all US fabs; top-tier US, a few European, few if any Pacific Rim fabs; fabs with reverse-pulse plating; hand-built only (experiments). Numeric bands inferred from Figs 4.69 and 4.79: <= 6:1 any fab; ~8:1 many US fabs; ~10:1 top tier; ~12:1 RPP or hand plating. | AR = t/d | t, d | — | calc | p.302 (App.10), p.95, p.104 | medium |

## 2. Formulas & tables (numbers)

### T1. Evolution of logic families (Table 1.1, p.14) — as printed

| Technology | tr/tf | Gate delay | Bit period | Max clock | Electrical length of clock period | Electrical length of rise time |
|---|---|---|---|---|---|---|
| Early relays | 0.1 s | 0.1 s | 0.3 s | 3.3 Hz | 150 million ft (45,700,000 m) | 50 million ft (15,240,000 m) |
| Reed relays | 1 ms | 1 ms | 3 ms | 330 Hz | 1,500,000 ft (457,000 m) | 500,000 ft (152,400 m) |
| Vacuum tubes | 1 us | 2 us | 4 us | 250 kHz | 2000 ft (610 m) | 500 ft (152 m) |
| Silicon transistors | 0.2 us | 0.4 us | 0.8 us | 1.25 MHz | 800 ft (244 m) | 100 ft (30 m) |
| Early CMOS | 70 ns | 140 ns | 280 ns | 3.6 MHz | 35 ft (11 m) | 140 ft (43 m) |
| TTL | 30 ns | 60 ns | 120 ns | 8.3 MHz | 15 ft (4.6 m) | 60 ft (18.3 m) |
| ASTTL | 2 ns | 6 ns | 10 ns | 100 MHz | 5 ft (1.5 m) | 1 ft (30 cm) |
| 10K ECL | 3 ns | 2 ns | 7 ns | 140 MHz | 3.5 ft (1.1 m) | 1.5 ft (46 cm) |
| 100K ECL | 1 ns | 1 ns | 3 ns | 333 MHz | 1.5 ft (46 cm) | 6 in (18 cm) |
| GaAs | 0.3 ns | 0.6 ns | 1.2 ns | 833 MHz | 7.2 in (printed "220 cm") | 1.8 in (printed "54 cm") |
| 2006 CMOS | 0.2 ns | 0.3 ns | 0.7 ns | 1.43 GHz | 4.2 in (printed "128 cm") | 1.2 in (printed "36 cm") |
| 4.8 Gb/s serial links | 75 ps | 50 ps | 0.2 ns | 2.4 GHz | 2.5 in (76 cm printed) | 0.45 in (14 cm printed) |

Notes: the book uses v = 6 in/ns (500 million ft/s) for PCB propagation. The Early-CMOS and TTL rows have the two length columns apparently swapped in print (30 ns x 6 in/ns = 15 ft is the rise-time length), and the metric values for the last three rows are inconsistent with the inch values; the inch values are consistent with 6 in/ns and should be used.

### T2. Capacitor population for a 10 mohm target PDS (Fig 3.6, p.31) — 8 in x 10 in board

| Device | Qty | C each (F) | ESR each (ohm) | ESL each (H) | C total (F) | ESR total (ohm) | ESL total (H) |
|---|---|---|---|---|---|---|---|
| DC/DC converter | 1 | — | 1.00E-04 | 7.00E-08 | — | 1.00E-04 | 7.00E-08 |
| Tantalum 330 uF | 2 | 3.30E-04 | 2.30E-02 | 3.00E-09 | 6.60E-04 | 1.15E-02 | 1.50E-09 |
| 0603 ceramic 1.0 uF | 2 | 1.00E-06 | 2.00E-02 | 7.00E-10 | 2.00E-06 | 1.00E-02 | 3.50E-10 |
| 0603 ceramic 0.1 uF | 4 | 1.00E-07 | 4.00E-02 | 6.00E-10 | 4.00E-07 | 1.00E-02 | 1.50E-10 |
| 0603 ceramic 0.01 uF | 8 | 1.00E-08 | 6.00E-02 | 5.00E-10 | 8.00E-08 | 7.50E-03 | 6.25E-11 |
| PC board 8 x 10 in (plane cap) | 1 | 3.20E-08 | — | — | 3.20E-08 | — | — |

(Totals follow C_tot = n x C, ESR_tot = ESR/n, ESL_tot = ESL/n. The ESL values above include mounting inductance. Resulting Z(f) plotted 1 kHz-1 GHz, Fig 3.5; measured Z matched SPICE to ~200 MHz, Fig 3.9.)

### T3. Example technology table (Fig 2.3, p.25) — selected rows

| Class | Technology | SE/DIFF | Rate | Qty | Z0 (ohm) | Layers | Term | Stub (mil) | Spacing in class (mil) | Spacing to other classes (mil) | Length tune (mil) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 10GE | GB DIFF | DIFF | 9.6 Gb/s | 8 pr | 50 | 2 | INT | 0 | 10 | 20 | 100 |
| 10GE CLK | GB DIFF | DIFF | 4.8 GHz | 2 pr | 50 | 2 | INT | 0 | 10 | 20 | 100 |
| XAUI | GB DIFF | DIFF | 3.125 Gb/s | 32 pr | 50 | 2 | INT | 0 | 10 | 20 | 300 |
| XAUI CLK | GB DIFF | DIFF | 1.55 GHz | 2 pr | 50 | 2 | INT | 0 | 10 | 20 | 300 |
| 1GE | GB DIFF | DIFF | 1 Gb/s | 4 pr | 50 | 2 | INT | 0 | 10 | 20 | 300 |
| GMII / BUS0A / BUS0B / BUS1A / BUS1B | 3.3CMOS | SE | 125-150 MHz | 48-66 | 50 | ANY | N/A or SER | 0 | 6 | 15 | — |
| IFCLK | 3.3CMOS | SE | 150 MHz | 1 | 50 | ANY | SER | 0 | 10 | 15 | — |
| SRAM ADDR/DATA/CLK, flash, JTAG, I2C, GPIO, RS-232, MDC/MDIO, clocks | 3.3CMOS / LVTTL | SE | 1-100 MHz or slow | — | 50 | ANY | SER or N/A | 0 | 6 | 15 | — (a trailing "200" in the extraction is unassignable) |

Notes printed with the table: "Length tuning tolerance is ±"; "Differential pair spacing is minimum spacing. Members of a pair can be spaced more than this"; "All ground planes tied together at every device ground pin"; "Lengths are in mils"; trace width per layer taken from the stackup.

### T4. Ceramic capacitor dielectric classes (p.38-39)

| Code | Class | Tolerance over temperature | Notes |
|---|---|---|---|
| C0G / NP0 (mil BP) | ultra-stable | — | lowest loss; do not use as PDS decoupling (parallel resonance with planes) |
| X7R (mil BX/BR) | stable | ±15% over -55..+125 C | preferred when product runs much above 25 C |
| X5R | stable | ±15% over -55..+85 C | — |
| Z5U | general purpose | +22% / -56% | — |
| Y5V | general purpose | +22% / -82% | capacitance halves at 16% of rated V; 10% left at 50% of rated V; worse with temperature |

### T5. PDS element numbers quoted in Ch.3

| Item | Value | Source |
|---|---|---|
| Via inductance | ~36 pH per mil of length | p.30 (Vol.1 Eq 35.1) |
| Frequency above which discrete capacitors are ineffective | ~200 MHz | p.33, p.44 |
| EMI radiated test band referenced | 30 MHz - 1 GHz | p.35 |
| Quarter-brick DC-DC output Z | 1 mohm DC-100 Hz; 10 mohm at ~3 kHz -> 1.6 uH | p.40 |
| Synqor 100 A DC-DC | 1 mohm at ~2 kHz -> 80 nH; 40 uohm minimum | p.41 |
| 10 nF X7R 0603 | ESR ~100 mohm; ESL 0.5 nH | p.42 |
| 1 uF 0603 vs 10 nF plane, ESR 20 mohm | 20 mohm min at 3.5 MHz; 10 ohm peak at 35 MHz | p.38, Fig 3.19 |
| PCMCIA card plane capacitance | 500 pF before fill; 4000 pF after fill | p.44 |
| 4-layer PC motherboard | 50-60 mil thick; 5-6 mil signal-to-plane; planes >= 40 mil apart | p.44 |
| Copper etch accuracy | ±0.5 mil (1/2 oz), ±1.0 mil (1 oz) | p.50 |
| Copper thickness | 1 oz = 1.4 mil = 36 um; 1/2 oz = 0.7 mil = 18 um | p.49 |
| Drill true position needing x-ray optimization | ±5 mil (±127 um) on 18 x 24 in panel | p.54 |

### T6. Typical "FR-4" laminate table (Table 4.2, p.72; data courtesy Nelco; 1 mil = 25 um)

| Thickness (in) | Construction (glass style) | Resin content | er @ 1 MHz | er @ 1 GHz |
|---|---|---|---|---|
| 0.002 | 1 x 106 | 69.0% | 3.84 | 3.63 |
| 0.003 | 1 x 1080 | 62.0% | 4.00 | 3.80 |
| 0.004 | 1 x 2113 | 54.4% | 4.19 | 4.00 |
| 0.004 | 1 x 106 + 1 x 1080 | 57.7% | 4.11 | 3.91 |
| 0.004 | 1 x 2116 | 43.0% | 4.54 | 4.37 |
| 0.005 | 1 x 106 + 1 x 2113 | 52.8% | 4.24 | 4.05 |
| 0.005 | 1 x 2116 | 51.8% | 4.26 | 4.08 |
| 0.006 | 1 x 1080 + 1 x 2113 | 52.2% | 4.25 | 4.06 |
| 0.006 | 1 x 106 + 1 x 2116 | 50.8% | 4.29 | 4.11 |
| 0.006 | 2 x 2113 | 43.5% | 4.52 | 4.35 |
| 0.007 | 2 x 2113 | 49.6% | 4.33 | 4.14 |
| 0.008 | 1 x 7628 | 44.4% | 4.49 | 4.32 |
| 0.010 | 2 x 2116 | 51.8% | 4.26 | 4.08 |
| 0.014 | 2 x 7628 | 38.8% | 4.69 | 4.53 |

Available with 1/2 oz or 1 oz copper both sides (2 oz or mixed by special order). Prepreg available in the same thicknesses up to ~6 mil.

### T7. Glass cloth styles — nominal thickness (p.67)

| Style | Thickness |
|---|---|
| 106 | ~1.5 mil (38 um) |
| 1080 | ~2.5 mil (63 um) |
| 2113 | ~2.9 mil (75 um) |
| 3313 | ~3.2 mil (printed 102 um) |
| 2116 | ~3.8 mil (97 um) |
| 1652 | ~4.5 mil (115 um) |
| 7628 | ~6.5 mil (165 um) |

### T8. Complete stackup specification — 22-layer processor card with 3313 glass, FR-408 (Fig 4.45, p.75; format courtesy Chuck Corley)

Column meanings: material; construction; er at ~2 GHz unpressed / pressed; thickness unpressed / pressed (mil); copper (mil / oz); SE trace width (mil) -> SE impedance (ohm); differential trace width 4.5 mil on all routing layers.

| Item | Material / construction | er unpressed / pressed | Thickness unpressed / pressed (mil) | Copper (mil / oz) | SE width -> Z0 |
|---|---|---|---|---|---|
| Solder mask (top) | — | — | 0.7 | — | — |
| L1 | foil | — | — | 2.2 / 1.5 oz | mount layer |
| Prepreg 1-2 | FR-408 1 x 3313, Rc = 53.8% | 3.7 / 4 | 4 / 3.4 | — | — |
| L2 | signal (buried microstrip) | — | — | 0.6 / 0.5 oz | 6.5 mil -> 52.7 ohm |
| Core 2-3 | FR-408 1 x 3313, Rc = 53.8% | 3.7 / 4 | 4 / 4 | — | — |
| L3 | plane | — | — | 0.6 / 0.5 | — |
| Prepreg 3-4 | FR-408 2 x 106 ULRC, Rc = 63.3% | 3.4 / 4 | 4 / 3 | — | plane pair |
| L4 | plane | — | — | 0.6 / 0.5 | — |
| Core 4-5 | 1 x 3313 | 3.7 / 4 | 4 / 4 | — | — |
| L5 | signal | — | — | 0.6 / 0.5 | 5 mil -> 52.0 ohm |
| Prepreg 5-6 | 1 x 3313 | 3.7 / 4 | 4 / 3.7 | — | signal pair opening |
| L6 | signal | — | — | 0.6 / 0.5 | 5 mil -> 52.0 ohm |
| Core 6-7 | 1 x 3313 | 3.7 / 4 | 4 / 4 | — | — |
| L7 | plane | — | — | 0.6 / 0.5 | — |
| Prepreg 7-8 | 2 x 106 ULRC | 3.4 / 4 | 4 / 3 | — | plane pair |
| L8 | plane | — | — | 0.6 / 0.5 | — |
| Core 8-9 | 1 x 3313 | 3.7 / 4 | 4 / 4 | — | — |
| L9 | signal | — | — | 0.6 / 0.5 | 5 mil -> 52.0 ohm |
| Prepreg 9-10 | 1 x 3313 | 3.7 / 4 | 4 / 3.5 | — | — |
| L10 | signal | — | — | 0.6 / 0.5 | 5 mil -> 50.6 ohm |
| Core 10-11 | 1 x 3313 | 3.7 / 4 | 4 / 4 | — | — |
| L11 | plane | — | — | 0.6 / 0.5 | — |
| Prepreg 11-12 | 2 x 106 ULRC | 3.4 / 4 | 4 / 3 | — | plane pair |
| L12 | plane | — | — | 0.6 / 0.5 | — |
| Core 12-13 | 1 x 3313 | 3.7 / 4 | 4 / 4 | — | — |
| L13 | signal | — | — | 0.6 / 0.5 | 5 mil -> 52.0 ohm |
| Prepreg 13-14 | 1 x 3313 | 3.7 / 4 | 4 / 3.5 | — | — |
| L14 | signal | — | — | 0.6 / 0.5 | 5 mil -> 52.0 ohm |
| Core 14-15 | 1 x 3313 | 3.7 / 4 | 4 / 4 | — | — |
| L15 | plane | — | — | 0.6 / 0.5 | — |
| Prepreg 15-16 | 2 x 106 ULRC | 3.4 / 4 | 4 / 3 | — | plane pair |
| L16 | plane | — | — | 0.6 / 0.5 | — |
| Core 16-17 | 1 x 3313 | 3.7 / 4 | 4 / 4 | — | — |
| L17 | signal | — | — | 0.6 / 0.5 | 5 mil -> 52.0 ohm |
| Prepreg 17-18 | 1 x 3313 | 3.7 / 4 | 4 / 3.5 | — | — |
| L18 | signal | — | — | 0.6 / 0.5 | 5 mil -> 52.0 ohm |
| Core 18-19 | 1 x 3313 | 3.7 / 4 | 4 / 4 | — | — |
| L19 | plane | — | — | 0.6 / 0.5 | — |
| Prepreg 19-20 | 2 x 106 ULRC | 3.4 / 4 | 4 / 3 | — | plane pair |
| L20 | plane | — | — | 0.6 / 0.5 | — |
| Core 20-21 | 1 x 3313 | 3.7 / 4 | 4 / 4 | — | — |
| L21 | signal (buried microstrip) | — | — | 0.6 / 0.5 | 6.5 mil -> 52.7 ohm |
| Prepreg 21-22 | 1 x 3313 | 3.7 / 4 | 4 / 3.4 | — | — |
| L22 | foil | — | — | 2.2 / 1.5 oz | mount layer |
| Solder mask (bottom) | — | — | 0.7 | — | — |
| Totals | — | — | dielectric 77.4; total 93.8 | copper 16.4 | — |

Notes on the drawing: "Single ended traces to be kept at least 25 mils from each other and differential traces." "When placing stackup information on fabrication drawing, do not put any of the information to the right of the solid heavy vertical line" (i.e., trace width/impedance columns stay off the fab drawing). Routing layers: 2, 5, 6, 9, 10, 13, 14, 17, 18, 21.

### T9. Impedance-predicting equations (Fig 4.46, p.77; dimensions per Fig 4.47; any consistent units)

- Surface microstrip (as printed): `Z0 = 79 / sqrt(er + 1.41) * ln(5.98*H / (0.8*W + T))` — H = dielectric height above plane, W = trace width, T = trace thickness. (Common literature form uses 87 in place of 79; the book prints 79.)
- Asymmetric stripline: `Z0 = 80 / sqrt(er) * ln(1.9*(2*B + T) / (0.8*W + T)) * (1 - B / (4*(B + C + T)))` — B = height from trace to nearer plane, C = height to farther plane.
- Buried microstrip: printed equation is unrecoverable from the text extraction (OCR-garbled); use a field solver.
- Book verdict: all three are curve fits with limited validity; field solvers agree with measurement within instrument accuracy and must be used. In the Fig 4.48 comparison (T = 1.4 mil, H = 5 mil, er = 4, W = 4-10 mil) only the stripline equation tracked the field solver.

### T10. Impedance measured with three TDR edge rates (Table 4.3, p.81)

| Layer | 40 ps (Agilent) | 125 ps (Tektronix 1502C) | 175 ps (Polar CITS800) |
|---|---|---|---|
| L1 | 55.1 ohm | 53.9 ohm | 53.0 ohm |
| L8 | 57.4 ohm | 56.5 ohm | 52.6 ohm |
| L11 | 54.7 ohm | 53.2 ohm | 52.8 ohm |

### T11. Pad-stack dimensions vs board thickness (Figs 4.70-4.72, p.96-97; all mils)

Generating formulas (verified against every printed row): `drill = t_pcb / AR`; `shadow = drill + TID`; `capture_pad = shadow + 2 * ring`; `clearance_pad = shadow + 10` (2 x 5 mil insulation). Printed rows cover t_pcb = 30..250 mil in 10 mil steps.

| t_pcb (mil) | 8:1 drill | 10:1 drill | 8:1 shadow (TID 10) | 8:1 capture (TID 10, ring 2) | 8:1 clearance (TID 10) | 10:1 shadow (TID 10) | 10:1 capture (TID 10, ring 2) | 10:1 clearance (TID 10) |
|---|---|---|---|---|---|---|---|---|
| 30 | 3.75 | 3 | 13.75 | 17.75 | 23.75 | 13 | 17 | 23 |
| 40 | 5 | 4 | 15 | 19 | 25 | 14 | 18 | 24 |
| 50 | 6.25 | 5 | 16.25 | 20.25 | 26.25 | 15 | 19 | 25 |
| 60 | 7.5 | 6 | 17.5 | 21.5 | 27.5 | 16 | 20 | 26 |
| 70 | 8.75 | 7 | 18.75 | 22.75 | 28.75 | 17 | 21 | 27 |
| 80 | 10 | 8 | 20 | 24 | 30 | 18 | 22 | 28 |
| 90 | 11.25 | 9 | 21.25 | 25.25 | 31.25 | 19 | 23 | 29 |
| 100 | 12.5 | 10 | 22.5 | 26.5 | 32.5 | 20 | 24 | 30 |
| 110 | 13.75 | 11 | 23.75 | 27.75 | 33.75 | 21 | 25 | 31 |
| 120 | 15 | 12 | 25 | 29 | 35 | 22 | 26 | 32 |
| 130 | 16.25 | 13 | 26.25 | 30.25 | 36.25 | 23 | 27 | 33 |
| 140 | 17.5 | 14 | 27.5 | 31.5 | 37.5 | 24 | 28 | 34 |
| 150 | 18.75 | 15 | 28.75 | 32.75 | 38.75 | 25 | 29 | 35 |
| 160 | 20 | 16 | 30 | 34 | 40 | 26 | 30 | 36 |
| 170 | 21.25 | 17 | 31.25 | 35.25 | 41.25 | 27 | 31 | 37 |
| 180 | 22.5 | 18 | 32.5 | 36.5 | 42.5 | 28 | 32 | 38 |
| 190 | 23.75 | 19 | 33.75 | 37.75 | 43.75 | 29 | 33 | 39 |
| 200 | 25 | 20 | 35 | 39 | 45 | 30 | 34 | 40 |
| 210 | 26.25 | 21 | 36.25 | 40.25 | 46.25 | 31 | 35 | 41 |
| 220 | 27.5 | 22 | 37.5 | 41.5 | 47.5 | 32 | 36 | 42 |
| 230 | 28.75 | 23 | 38.75 | 42.75 | 48.75 | 33 | 37 | 43 |
| 240 | 30 | 24 | 40 | 44 | 50 | 34 | 38 | 44 |
| 250 | 31.25 | 25 | 41.25 | 45.25 | 51.25 | 35 | 39 | 45 |

Fig 4.71 (TID 12 mil, ring 2 mil): shadow = drill + 12; capture = shadow + 4; clearance = shadow + 10 (e.g., 100 mil board, 8:1: drill 12.5, shadow 24.5, capture 28.5, clearance 34.5; 10:1: 10, 22, 26, 32). Fig 4.72 (TID 10 mil, ring 0): capture = shadow (e.g., 100 mil, 8:1: 12.5 / 22.5 / 22.5 / 32.5; 10:1: 10 / 20 / 20 / 30). Applicability: Fig 4.70 and 4.72 only for the very best high-layer-count fabricators; Fig 4.71 satisfactory for most multilayer fabricators. Metric versions are in Appendix 7 of the book.

### T12. Pad-stack worked examples (p.94)

| Case | Pitch (mil) | Drill | TID | Shadow | Insulation/side | Clearance | Ring | Capture pad | Plane web | Signal-layer gap | Traces between pins |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 50 mil BGA, no ring | 50 | 12 | 10 | 22 | 5 | 32 | 0 | 22 | 18 | — | 2 x (5 mil trace, 5 mil space) |
| 50 mil BGA, 2 mil ring | 50 | 12 | 10 | 22 | 5 | 32 | 2 | 26 | 18 | 14 | 2 |
| 1 mm BGA, no ring | 39.37 | 12 | 10 | 22 | 5 | 32 | 0 | 22 | 7.37 | — | 1 |
| 1 mm BGA, 2 mil ring | 39.37 | 12 | 10 | 22 | 5 | 32 | 2 | 26 | 7.37 | 3.37 | 1 (barely) |
| 1 mm BGA, 2 traces (4/4 mil) | 39.37 | — | — | — | — | <= 25.37 needed | — | — | 12 needed | — | not reliable |
| 0.8 mm BGA | 31.5 | 12 | 10 | 22 | 5 | 32 | — | — | none | — | 0 -> use blind vias |

### T13. Surface-finish numbers (p.63-66)

| Item | Value |
|---|---|
| Gold over nickel, max | 10 uin (0.25 um) |
| Gold over nickel, min | 5 uin (printed "12 microns") |
| Gold in solder joint that embrittles | ~5% (most common figure quoted) |
| OSP cost saving example that scrapped a program | ~$30 per bare PCB |

### T14. Drill / test / via numbers quoted in Ch.4

| Item | Value | Source |
|---|---|---|
| ICT access via capacitance (drill <= 12 mil) | ~0.3 pF; harmless to 5.2 Gb/s | p.83 |
| Test pad diameter | 35-40 mil (0.8-1 mm) | p.84 |
| Impedance test trace | >= 3 in; via pitch 100 mil; drill 30 mil | p.85 |
| Plane access structure | 44 mil pad, 50 mil clearance, 30 mil drill, 75 mil pitch, 2 per rail >= 1 in apart | p.87 |
| Stacking stripe | 50 x 50 mil L1, +50 mil per layer, 25 mil in / 25 mil out, 5 mil etch segment, >= 20 mil from planes | p.87 |
| Blind via aspect ratio | d >= depth (1:1); many fabs d >= 1.5 x depth | p.60 |
| Microvia (IPC) | diameter <= 8 mil (203 um) | p.58 |
| Cell-phone lead pitch driving build-up | ~25 mil (0.6 mm) | p.61 |
| Press-fit two-diameter via | 26 mil top ~80 mil deep, 12 mil below | p.99 |
| Drill wander TIR | ±5 (best) / ±6 (US mid) / ±7 mil (Asia volume) | p.92 |
| Min insulation hole-to-copper | 5 mil (GR-78-CORE: 4 mil) | p.91 |
| Plating allowance | 2 mil per side (drill = FHS + 4 mil) | p.94 |
| Volume min line/space | 4 / 4 mil | p.94 |
| Minimum reliable drill on 100+ mil board | 12 mil | p.94 |

### T15. Measured 5.2 Gb/s reference path (Fig 4.74, p.99)

| Element | Parameters |
|---|---|
| Daughter card A / B striplines | L = 3 in each; TW = 5 mil; T = 0.6 mil; S = 15 mil; er = 3.8; loss tangent 0.015; FR408; Z0 = 50 ohm |
| Backplane stripline | L = 4 in; same geometry |
| Connectors | HmZd, two |
| Via parasitic capacitances | Ca = 0.5 pF, Cb = 0.8 pF, Cc = 1.1 pF, Cd = 0.6 pF |
| Backplane | 125 mil thick, 13.5 mil drill vias, 26 mil connector holes |
| Daughter boards | 116 mil thick, 12.0 mil drill vias, 26 mil connector holes |
| Result (Fig 4.75, S21 DC-6 GHz) | vias negligible to ~1.6 GHz (3.2 Gb/s); resonances above; back-drilling half the barrel improves; one added via shifts resonances |

### T16. Properties of commonly used laminates (Table 5.2, p.116; er by TDR velocity method at 55% resin content; woven glass except PTFE)

The extraction prints 12 material names but only 11 Tg values and 11 property rows, so one row is missing. Rows are given in printed order; the first four and the last are unambiguous, the middle assignments are uncertain.

| # | Material (printed order) | Tg (C), printed order | er | tan d | DBV (V/mil) | Water absorption (%) | Assignment |
|---|---|---|---|---|---|---|---|
| 1 | Rogers RO4350 | 280 | 3.48 | 0.0037 | 780 | 0.04 | certain |
| 2 | Standard FR-4 epoxy glass | 125 | 4.1 | 0.02 | 1100 | 0.14 | certain |
| 3 | Multifunctional FR-4 | 145 | 4.1 | 0.022 | 1050 | 0.13 | certain |
| 4 | Tetra-functional FR-4 | 150 | 4.1 | 0.022 | 1050 | 0.13 | certain |
| 5 | Nelco N4000-6 | 170 | 4 | 0.012 | 1300 | 0.10 | probable |
| 6 | Hi-Tg FR-4 | 180 | 4.1 | 0.011 | 1100 | 0.12 | uncertain |
| 7 | GETEK | 185 | 4.1 | 0.023 | 1350 | 0.20 | uncertain |
| 8 | BT epoxy glass | 210 | 3.25 | 0.009 | 1400 | 0.09 | uncertain (er 3.25 / tan 0.009 fits N4000-13SI S-glass better) |
| 9 | Nelco 4000-13SI | 245 | 4 | 0.01 | 800 | 0.70 | uncertain |
| 10 | Cyanate ester | 285 | 4.1 | 0.015 | 1200 | 0.43 | uncertain |
| 11 | Polyimide glass | (285 per text) | — | — | — | — | row missing in extraction |
| 12 | Teflon (PTFE) | N/A | 2.2 | 0.0002 | 450 | 0.01 | certain |

The text says cyanate ester and polyimide absorb enough water to fail leakage tests and that polyimide's Tg is about 285 C; Appendix 1 gives N4000-13SI Tg = 210 C. So the 0.70% and 0.43% water-absorption rows most likely belong to cyanate ester and polyimide. Use the certain rows for checks and treat rows 5-11 as indicative only.

### T17. Glass cloth used in PCB laminates (Table 5.1, p.111; sources Isola, Matsushita, Nelco)

| Style | Warp (threads/in) | Fill (threads/in) | Cloth thickness (in) | Laminate thickness (in) | Resin content |
|---|---|---|---|---|---|
| 106 | 56 | 56 | 0.0015 | 0.002 | 69.00% |
| 1080 | 60 | 47 | 0.0025 | 0.003 | 62.00% |
| 2113 | 60 | 56 | 0.0029 | 0.004 | 54.50% |
| 3313 | 61 | 62 | 0.0031 | 0.004 | 54.00% |
| 3070 | 70 | 70 | 0.0034 | 0.004 | 49.50% |
| 2116 | 60 | 58 | 0.0038 | 0.005 | 51.80% |
| 1652 | 52 | 52 | 0.0045 | 0.005 | 42.00% |
| 7628 | 44 | 32 | 0.0065 | 0.007 | 44.40% |

Nominal glass-bundle pitch ~16 mil (0.41 mm); large bundles ~12 mil (305 um) wide; er ~6 over glass, ~3 in resin.

### T18. PCB manufacturing capabilities, 2005 (Fig 4.79, p.104; mils / mm)

| # | Parameter | Std process | Advanced | Std (mm) | Advanced (mm) |
|---|---|---|---|---|---|
| 1 | Drilling aspect ratio | 6:1 | 10:1 | 6:1 | 10:1 |
| 2 | Min drilled hole, vias | 12 | 8 | 0.30 | 0.20 |
| 3 | Min finished hole, vias | 8 | 6 | 0.20 | 0.15 |
| 4 | Min outer-layer via land | 31 | 22 | 0.78 | 0.55 |
| 5 | Min inner-layer via land | 31 | 20 | 0.78 | 0.50 |
| 6 | Min via relief (clearance) in planes | 36 | 24 | 0.91 | 0.60 |
| 7 | Min blind/buried via land | 31 | 20 | 0.78 | 0.50 |
| 8 | Min blind/buried via drill | 12 | 10 | 0.30 | 0.25 |
| 9 | Min outer-layer line width | 5 | 3 | 0.13 | 0.08 |
| 10 | Min inner-layer line width | 5 | 3 | 0.13 | 0.08 |
| 11 | Min outer-layer space | 5 | 4 | 0.13 | 0.10 |
| 12 | Min inner-layer space | 5 | 4 | 0.13 | 0.10 |
| 13 | Line to via land spacing | 5 | 4 | 0.13 | 0.10 |
| 14 | Layer-to-layer registration | ±8 | ±5 | 0.20 | 0.13 |
| 15 | Min component pitch | 25 | 10 | 0.63 | 0.25 |
| 16 | Max overall thickness | 187 | 500 | 4.71 | 12.59 |
| 17 | Min dielectric thickness | 5 | 2.2 | 0.13 | 0.06 |
| 18 | PCB edge to conductor | 20 | 10 | 0.50 | 0.25 |
| 19 | Soldermask clearance per side | 10 | 3 | 0.25 | 0.08 |
| 20 | Line to SMT pad min space | 10 | 4 | 0.25 | 0.10 |
| 21 | Min base copper weight | 0.7 mil (1/2 oz) | 0.35 mil (1/4 oz) | 0.02 | 0.01 |
| 22 | Average layer count | 10 | 16 | 10 | 16 |
| 23 | Fab panel OD | 18 x 24 in | 22 x 34 in | 46 x 61 cm | 56 x 86 cm |
| 24 | Fabrication (routing) radius | 62 | 16 | 1.56 | 0.40 |
| 25 | Warpage (design dependent) | 1% | 0.5% | 1% | 0.5% |
| 26 | Plated through-hole tolerance (design dep.) | ±3 | ±2 | ±0.08 | ±0.05 |
| 27 | Impedance tolerance | ±10% | ±5% | ±10% | ±5% |

### T19. Standard fabrication panels (p.106; laminate sheet 36 x 48 in)

| Panel | Usable area (~1 in tooling border) |
|---|---|
| 24 x 36 in (60.96 x 91.44 cm) | 22 x 34 in |
| 18 x 24 in (45.72 x 60.96 cm) | 16 x 22 in |
| 16 x 18 in | 14 x 16 in |
| 12 x 18 in | 10 x 16 in |

Mass lamination panels: up to 48 x 72 in (4-layer only).

### T20. Thermal expansion / Tg data (Fig 5.14, p.117; graph)

| Item | Value |
|---|---|
| Resin alpha1 (below Tg) | 50 x 10^-6 in/in/C |
| Resin alpha2 (above Tg) | 275 x 10^-6 in/in/C |
| TCE copper | 16.5 x 10^-6 in/in/C |
| TCE glass | 11 x 10^-6 in/in/C |
| Eutectic solder melting point | 185 C (365 F) |
| Lead-free solder melting point | >= 225 C (436 F) |
| Z-axis expansion to ~275 C (graph labels) | FR-4 5.1%; multifunctional 4.7%, 4.5%, 4%; BT epoxy / GETEK 3.8%; polyimide 3% and 2%; cyanate ester 2.3% |
| Tg selection, leaded solder | <= 63 mil: Tg 135 C OK; > 63 mil: Tg >= 170 C |
| Tg selection, lead-free | <= 63 mil: Tg >= 170 C; > 63 mil: Tg >= 220 C |

### T21. Capacitive reactance table (Figs 6.2, 6.4, p.124/126; mounting inductance ignored)

| Frequency | 100 pF | 1000 pF | 0.01 uF |
|---|---|---|---|
| 30 MHz | 53 ohm | 5.3 ohm | 0.53 ohm |
| 100 MHz | 16 ohm | 1.6 ohm | 0.16 ohm |
| 1 GHz | 1.6 ohm | 0.16 ohm | 0.016 ohm |

### T22. 18-layer test PCB cross-section (Fig 6.5, p.127; all dielectrics er = 3.5)

| Layer | Copper | Function | Z0 / width | Dielectric below (mil) |
|---|---|---|---|---|
| 1 | 1.50 oz | Signal1 | 74.8 ohm / 10.0 mil | 5.0 |
| 2 | 0.50 oz | Signal (buried microstrip) | 50.5 ohm / 8.5 mil | 5.0 |
| 3 | 0.50 oz | VCC | — | 3.0 |
| 4 | 0.50 oz | GND | — | 5.0 |
| 5 | 0.50 oz | Signal3 | 50.9 ohm / 8.0 mil | 15.0 |
| 6 | 0.50 oz | Signal4 | 50.9 ohm / 8.0 mil | 5.0 |
| 7 | 0.50 oz | VCC | — | 3.0 |
| 8 | 0.50 oz | GND | — | 7.0 |
| 9 | 0.50 oz | Signal5 | 49.9 ohm / 10.0 mil | 118.85 (thick core) |
| 10 | 0.50 oz | Signal6 | 49.9 ohm / 10.0 mil | 8.0 (printed order: 8.0, 7.0) |
| 11 | 0.50 oz | VCC | — | 7.0 / 3.0 |
| 12 | 0.50 oz | GND | — | 5.0 |
| 13 | 0.50 oz | Signal7 | 50.9 ohm / 8.0 mil | 15.0 |
| 14 | 0.50 oz | Signal8 | 50.9 ohm / 8.0 mil | 5.0 |
| 15 | 0.50 oz | VCC | — | 3.0 |
| 16 | 0.50 oz | GND | — | 5.0 |
| 17 | 0.50 oz | Signal9 | 50.5 ohm / 8.5 mil | 5.0 |
| 18 | 1.50 oz | Signal10 | 81.8 ohm / 8.0 mil | — |

(Dielectric sequence as printed top to bottom: 5.0, 5.0, 3.0, 5.0, 15.0, 5.0, 3.0, 7.0, 118.85, 8.0, 7.0, 3.0, 5.0, 15.0, 5.0, 3.0, 5.0, 5.0 mil; the mapping of the 8.0/7.0 pair around layers 10-11 is by printed order.) Plane pairs VCC/GND spaced 3.0 mil; signal-to-plane 5.0 mil; signal-pair openings 15.0 mil. TDR: Tek 1502C, 125 ps.

### T23. EMI numbers quoted in Ch.7 (through §7.12)

| Item | Value | Source |
|---|---|---|
| Conducted EMI band | 150 kHz - 30 MHz | p.132 |
| Radiated EMI band | 30 MHz - 1 GHz, or 5 x highest clock if greater | p.132 |
| Cage vent hole max | 1/4 in (6.35 mm) -> contained to >= 10 GHz | p.135 |
| 10Base2 shield isolation | 1700 VDC | p.137 |
| Plane capacitor to cage | ~370 pF per line; 8 mil min insulation (> 8000 V); 80 mil outer isolation gap; 4-layer 8/40/8 mil | p.138 |
| PCMCIA plane capacitance fix | 500 pF -> 4100 pF (Ch.7) / 4000 pF (Ch.3) | p.143 |
| Discrete-capacitor useful ceiling for switching current | ~100 MHz (Hubing ref.) | p.143 |
| Emission test example | 6-layer 100BT PCMCIA card, 33 MHz clock, CISPR B limit | p.143 |
| AB1000 example unit | clocks 1.89, 33.3, 40 MHz; i960; 8 unshielded RS232, shielded RS232, unshielded 10BT | p.137 |
| Current-spectrum of 12 in line, 5 V CMOS, 30 MHz clock | 85 MHz - ~900 MHz, no clock harmonics | p.143-144 |
| Logic-ground-to-cage connections | exactly 1 | p.142 |
| Terabit router example | 7 kW, half rack, passed EMI first try | p.142 |

### T24. Crosstalk into a differential pair from an aggressor 5 mil away (Fig 8.5, p.157)

| Pair geometry | Near member | Far member | Differential (unrejected) |
|---|---|---|---|
| Broadside (over-under) pair, 5 mil traces | 12% | 1% | 11% |
| Coplanar (side-by-side) pair, 5 mil trace / 5 mil space | 12% | 2% | 10% |

Dimensions printed on the figure: 0.015 in and 0.005 in dielectric heights, 5 mil traces and spaces.

### T25. Tight vs loose differential pair (Figs 8.6-8.8, p.158-159)

| Pair | Trace / space (mil) | Zdiff routed together | Zdiff spread to 39 mil space | Single member alone |
|---|---|---|---|---|
| Tightly coupled | 5 / 5 | 100 ohm | 140 ohm | ~70.7 ohm |
| Loosely coupled | 10 / 15 | 100 ohm | 109 ohm | ~54 ohm |

Figure dimensions as printed: 0.025 in and 0.010 in (plane spacing / dielectric). Fig 8.7: at 2.4 Gb/s over a 30 in path the loose pair keeps more amplitude (graph).

### T26. 5.2 Gb/s rack-to-rack model (Fig 8.9, p.160)

| Segment | Parameters |
|---|---|
| PCB A and PCB B | 8 in stripline each; TW 5 mil; T 0.6 mil; S 15 mil; er 3.8; loss tangent 0.015; FR408; Z0 50 ohm |
| Cable | 4 m (157.5 in) Infiniband; loss tangent 0.0005; er 1.8 |
| Vias | 0.65 pF each (routing vias 12 mil x 100 mil) |
| Driver/receiver | IBM SPICE models including pad transfers; driver edges < 100 ps; bit at 5.2 Gb/s = 192 ps |
| Validation | S21 simulated vs measured (4-port VNA) to 6 GHz, Fig 8.11 |

### T27. Data-rate sweep outcome on that path (Figs 8.12-8.20)

| Rate | Result |
|---|---|
| 100 Mb/s | edges rolled off, bit centre correct, reflections small — no problem |
| 1 Gb/s | eye just open enough to make margins |
| 2.4 Gb/s | fails amplitude mask; jitter grows; loss is main amplitude eroder, vias drive jitter; 2 pF press-fit vias worse; pre-emphasis compensates |
| 4.8 Gb/s | far too small without pre-emphasis |
| 5.2 Gb/s | works with 15% pre-emphasis |

### T28. Loss trade on a 33 in path at 2.5 GHz (Fig 8.21, p.168; graph)

| Change | Approximate improvement |
|---|---|
| Trace width 5 -> 10 mil (0.6 mil copper) | ~1 dB |
| Hi-Tg FR-4 -> Nelco 4000-13 | ~2 dB |
| Hi-Tg FR-4 -> Nelco 4000-13SI or Isola IS620 | ~4 dB |

(The printed text labels 2.5 GHz as "5 MB/S"; 2.5 GHz is the Nyquist frequency of 5 Gb/s.)

### T29. ASIC clock-tree current and power estimate (Table 10.1, p.185; 0.13 um, 1.5 V core, 500 MHz, 100 fF load per DFF; charge in coulombs)

| Cells | Idd-pk each (mA) | Charge each (fC) | Idle: % active | Idle qty | Idle charge (nC) | Heavy: % active | Heavy qty | Heavy charge (nC) |
|---|---|---|---|---|---|---|---|---|
| Total DFFs | — | — | — | 550000 | — | — | 550000 | — |
| Clock splitters | 2.00 | 305 | 100% | 36667 | 11.18 | 100% | 36667 | 11.18 |
| DFF non-active | 0.15 | 13.3 | 100% | 550000 | 7.32 | 50% | 275000 | 3.66 |
| DFF active: not switching | 0.15 | 13.3 | 50% of active | 0 | 0.00 | 50% | 137500 | 1.83 |
| DFF active: output falling | 0.40 | 38.7 | 25% of active | 0 | 0.00 | 25% | 68750 | 2.66 |
| DFF active: output rising | 1.00 | 192.2 | 25% of active | 0 | 0.00 | 25% | 68750 | 13.21 |
| Total charge per rising clock edge | — | — | — | — | 18.50 | — | — | 32.54 |
| Pulse width (ns) | — | — | — | — | 0.15 | — | — | 0.15 |
| Peak current (A) | — | — | — | — | 123 | — | — | 217 |
| Power (W) | — | — | — | — | 13.9 | — | — | 24.4 |

(Active fraction of DFFs: 0% idle, 50% heavy use. Clock skew 300 ps, normally distributed -> 150 ps midpoint width. Checks: P = Q x 1.5 V x 500 MHz; I_pk = Q / 0.15 ns.)

### T30. Effective frequency range of power-distribution elements (Table 10.2, p.187)

| Element | Effective frequency |
|---|---|
| Power supply | DC to 5 kHz |
| PCB bulk decoupling capacitors | 5 kHz to 2 MHz |
| PCB ceramic decoupling capacitors | 2 MHz to 100 MHz |
| IC package power balls | DC to 100 MHz |
| IC package decoupling capacitors | 50 MHz to 500 MHz |
| Chip power balls | DC to 500 MHz |
| On-chip decoupling capacitance | above 500 MHz |

### T31. Decoupling capacitors mounted on IC packages (Table 10.3, p.188)

| Type | Vendor part number | Rated C | Rated V | C @ 1 kHz | C @ 1 MHz | ESR (mohm) | ESL (pH) | Fres (MHz) |
|---|---|---|---|---|---|---|---|---|
| 0603 | AVX 0603YC104ZAT2A | 100 nF | 16 | 95 nF | 81 nF | 30 | 360 | 29 |
| 0402 | AVX 0402YC104ZAT2A | 100 nF | 16 | 105 nF | 80 nF | 30 | 270 | 33 |
| 0612 (reverse geometry) | AVX 0612YC104MAT | 100 nF | 16 | 95 nF | 92 nF | 14 | 228 | 35 |
| 0306 (reverse geometry) | AVX 0306ZC104KAT2S | 100 nF | 10 | 98 nF | 96 nF | 20 | 165 | 40 |
| 0612 IDC | AVX W3L1YC104MAT | 100 nF | 16 | 97 nF | 82 nF | 27 | 150 | 45 |
| 0508 IDC | AVX W2L1YC104MAT | 100 nF | 16 | 97 nF | 82 nF | 25 | 120 | 51 |
| LICA | AVX LICA3T183M3FC4AA | 72 nF | 25 | 65 nF | 60 nF | 20 | 25 | 125 |

Same 0402 on a PCB footprint: 450 pH (Fig 10.17). Fig 10.18 plots |Z| vs f (1 MHz-1 GHz) for all seven.

### T32. Package / attach numbers (Ch.10, p.177-186)

| Item | Value |
|---|---|
| Wire-bond inductance | a few nH per lead |
| Flip-chip ball (97/3 Pb/Sn) inductance | ~50 pH |
| Ceramic package er | ~10; firing shrinkage ~17%; balls 90/10 Pb/Sn |
| Organic package er | ~4; 1/2 oz copper; eutectic balls |
| Eutectic 63/37 | melts 183 C; reflow ~220 C |
| SAC lead-free (95.5 Sn / 3.8 Ag / 0.5 Cu) | melts 218 C; peak reflow 260 C |
| Activity thermal cycles | ~10 C, millions |
| Telecom ambient | 0-55 C; Tj max typically 100 C |
| 90 nm core | Vdd ~1.2 V; 50 W -> 42 A |
| Vddq | 1.8 V single-ended, 2.5 V differential drivers (typical) |
| SE driver current | 0.9 V into 50 ohm = 18 mA; 100-bit bus = 1.8 A |
| CMOS speed temperature coefficient | ~0.2% per C |
| On-die decoupling (high-power chip) | > 50 nF |
| Plane-pair example (er 4.0, 75 um) | 47.2 pF/cm^2; Z0 = 1.41 ohm per cm width; 94 pH per square |
| SPI-4.1 | 64-bit source-synchronous series-terminated HSTL, 200 MHz |
| SPI-4.2 | 16-bit LVDS, 800 MHz |
| Line card | 26 layers: 12 signal, 12 power/ground, 2 surface pad layers |
| Virtex-2 Pro FF1517 | clock jitter 1600 ps; ~800 mV Vddq/ground bounce |
| Virtex-4 FF1148 | clock jitter 97 ps |

### T33. Loop inductance of adjacent solder-ball pairs (Table 10.4, p.193; Eq 10.6 with R = pitch/2)

| Type | Ball pitch (mm) | Loop L (nH) |
|---|---|---|
| Package | 1.270 | 1.35 |
| Package | 1.000 | 1.06 |
| LICA capacitor | 0.400 | 0.42 |
| Chip C4 | 0.225 | 0.24 |

Eq 10.6: `L = 10 * R * (7.353 * log10(16*R/D) - 6.386)` nH; R = turn radius (in), D = wire diameter (in); valid R > 2.5 D. Eq 10.5: `L = (Lsq / (2*pi)) * ln(R2/R1)`.

### T34. I/O bus current characteristics (Tables 10.5 and 10.6, p.195-196)

| Parameter | SPI-4.1 | SPI-4.2 |
|---|---|---|
| Signal quantity | 85 + clock | 17 + clock |
| Signal type | HSTL | LVDS differential |
| Signal wire Z0 | 50 ohm | 100 ohm |
| Termination | series | parallel 100 ohm |
| Wire length / delay | 10 in / 1.67 ns | — |
| Clock frequency | 200 MHz | 400 MHz |
| Data rate per signal | 200 Mb/s | 800 Mb/s |
| Vddq | 1.8 V | 2.5 V |
| Drive current amplitude | 18 mA | 6 mA |
| Output rise time | 0.4 ns | 0.2 ns |
| Current pulse width | 3.33 ns | DC |
| Total bus current | 1.53 A (max) | 108 mA |
| Power dissipation | 460 mW (typical) | 270 mW |

Six 2.5 V DDR1 SDRAM ports at 333 MHz on the same ASIC: current pulse up to 13.8 A.

### T35. Six-conductor-layer organic package stackup (Table 10.7, p.199; mm)

| Layer | Material | Thickness (mm) |
|---|---|---|
| C4 ball side | solder mask | 0.025 |
| L1 | copper | 0.015 |
| — | build-up dielectric | 0.035 |
| L2 | copper | 0.015 |
| — | build-up dielectric | 0.035 |
| L3 | copper | 0.040 |
| Core | epoxy glass | 0.800 |
| L4 | copper | 0.040 |
| — | build-up dielectric | 0.035 |
| L5 | copper | 0.015 |
| — | build-up dielectric | 0.035 |
| L6 | copper | 0.015 |
| Package ball side | solder mask | 0.025 |
| Total | — | 1.130 |

(Bottom half printed in a scrambled order; the symmetric reading above sums to the printed 1.130 mm total.)

### T36. Example package comparison (Tables 10.8-10.10, p.203)

| Parameter | PKG-A (poor) | PKG-B (good) |
|---|---|---|
| Chip size / package size | 12 mm / 34.5 mm | 12 mm / 34.5 mm |
| GND / Vdd / Vddq / signal balls | 224 / 50 / 54 / 760 | 164 / 96 / 68 / 760 |
| Total balls | 1088 | 1088 |
| Package capacitors | 4 x 0402, 100 nF (80 nF @ 10 MHz), 30 mohm, 500 pH | 4 x LICA, 72 nF (60 nF @ 10 MHz), 20 mohm, 25 pH |
| On-chip capacitance | 20 nF | 50 nF |
| Core PWR/GND pairs; pair loop L | 46; 1.0 nH | 144; 1.0 nH |
| Core pins ESL | 21.7 pH | 6.9 pH |
| PCB Vdd/GND plane ESL (R1 6 mm, R2 17 mm) | 23.8 pH | 23.8 pH |
| Core ESL pins + PCB planes | 45.5 pH | 30.7 pH |
| Package Vdd/GND plane ESL | none | 12.0 pH |
| Edge PWR/GND pairs; pair loop L | none | 168; 2.0 nH |
| Edge pins ESL | — | 11.9 pH |
| Edge ESL pins + package planes | — | 23.9 pH |
| Total ESL chip to PCB | 45.5 pH | 13.4 pH |
| Core PDS impedance result | resonance ~170 MHz, > 50 mohm | < 7 mohm over whole range |

### T37. Glossary numbers (p.211-221)

| Term | Value / statement |
|---|---|
| 1U rack unit | 1.75 in |
| Ampere | 6.24 x 10^18 electrons per second |
| Aspect ratio | > 6:1 not a volume-production candidate |
| Foil | 1 oz = 1.4 mil = 35 um (glossary; text elsewhere says 36 um) |
| Current-mode driver | 4 mA into 50 ohm = 200 mV; LVDS pair 400 mV differential; real output impedance a few hundred ohms |
| Fall time | 90% -> 10% (20%/80% for GaAs and ECL) |
| FPBGA | ball pitch < 1 mm |
| BTL | drives buses down to 22 ohm at clock rates to 225 MHz; swing < 1 V p-p; open-collector NPN |
| IBIS | governed by ANSI/EIA-656 |
| EMI radiated band | 30 MHz - 1 GHz; conducted 150 kHz - 30 MHz |

### T38. Isola FR406 (high-performance epoxy; Tg 170 C, Td 295 C) — Dk and Df by construction (App. 1, p.237)

| Core thickness (in) | Construction | Resin % | Dk @ 2 GHz | Dk @ 10 GHz | Df @ 2 GHz | Df @ 10 GHz |
|---|---|---|---|---|---|---|
| 0.0025 | 1-1080 | 58 | 3.75 | 3.65 | 0.0205 | 0.0213 |
| 0.0030 | 1-2113 | 44 | 4.16 | 4.06 | 0.0180 | 0.0186 |
| 0.0035 | 2-106 | 65 | 3.56 | 3.48 | 0.0216 | 0.0224 |
| 0.0040 | 1-2116 | 45 | 4.13 | 4.02 | 0.0182 | 0.0188 |
| 0.0040 | 1-3070 | 48 | 3.97 | 3.95 | 0.0180 | 0.0189 |
| 0.0043 | 106/1080 | 60 | 3.69 | 3.60 | 0.0208 | 0.0216 |
| 0.0050 | 1-1652 | 42 | 4.23 | 4.12 | 0.0176 | 0.0182 |
| 0.0053 | 106/2113 | 56 | 3.80 | 3.71 | 0.0201 | 0.0209 |
| 0.0060 | 1080/2113 | 53 | 3.89 | 3.79 | 0.0196 | 0.0204 |
| 0.0070 | 1-7628 | 41 | 4.26 | 4.15 | 0.0174 | 0.0180 |
| 0.0080 | 2-2116 | 45 | 4.13 | 4.02 | 0.0182 | 0.0188 |
| 0.0095 | 2-2116 | 52 | 3.92 | 3.82 | 0.0195 | 0.0202 |
| 0.0100 | 2-1652 | 42 | 4.23 | 4.12 | 0.0176 | 0.0182 |
| 0.0120 | 2-1080/7628 | 47 | 4.07 | 3.96 | 0.0185 | 0.0192 |
| 0.0140 | 2-7628 | 41 | 4.26 | 4.15 | 0.0174 | 0.0180 |
| 0.0180 | 2-7628/2116 | 42 | 4.23 | 4.12 | 0.0176 | 0.0182 |
| 0.0210 | 3-7628 | 39 | 4.33 | 4.22 | 0.0170 | 0.0176 |
| 0.0240 | 3-7628/2113 | 41 | 4.26 | 4.15 | 0.0174 | 0.0180 |
| 0.0280 | 4-7628 | 40 | 4.30 | 4.18 | 0.0172 | 0.0178 |
| 0.0310 | 4-7628/2116 | 40 | 4.30 | 4.18 | 0.0172 | 0.0178 |
| 0.0340 | 5-7628 | 40 | 4.30 | 4.18 | 0.0172 | 0.0178 |
| 0.0350 | 5-7628 | 41 | 4.26 | 4.15 | 0.0174 | 0.0180 |
| 0.0390 | 6-7628 | 37 | 4.40 | 4.28 | 0.0165 | 0.0172 |

### T39. Isola FR408 (mid Dk/Df, high Tg, lead-free compatible; Tg 180 C, Td 360 C; rev April 2006) (App. 1, p.238)

| Core thickness (in) | Construction | Resin % | Dk @ 2 GHz | Dk @ 5 GHz | Dk @ 10 GHz | Df @ 2 GHz | Df @ 5 GHz | Df @ 10 GHz |
|---|---|---|---|---|---|---|---|---|
| 0.0020 | 1-106 | 63 | 3.49 | 3.48 | 3.47 | 0.0128 | 0.0136 | 0.0134 |
| 0.0025 | 1-1080 | 55 | 3.67 | 3.66 | 3.65 | 0.0120 | 0.0127 | 0.0125 |
| 0.0030 | 1-2113 | 44 | 3.95 | 3.94 | 3.93 | 0.0109 | 0.0114 | 0.0113 |
| 0.0035 | 1-2113 | 52 | 3.74 | 3.73 | 3.72 | 0.0112 | 0.0123 | 0.0122 |
| 0.0035 | 2-106 | 65 | 3.45 | 3.43 | 3.43 | 0.0131 | 0.0138 | 0.0136 |
| 0.0040 | 1-3070 | 48 | 3.84 | 3.83 | 3.82 | 0.0113 | 0.0119 | 0.0117 |
| 0.0043 | 106/1080 | 58 | 3.60 | 3.59 | 3.58 | 0.0123 | 0.0130 | 0.0128 |
| 0.0050 | 1-1652 | 42 | 4.00 | 3.99 | 3.99 | 0.0107 | 0.0112 | 0.0110 |
| 0.0053 | 106/2113 | 56 | 3.65 | 3.63 | 3.63 | 0.0121 | 0.0128 | 0.0126 |
| 0.0060 | 1080/2113 | 53 | 3.72 | 3.71 | 3.70 | 0.0118 | 0.0124 | 0.0123 |
| 0.0070 | 2113/2116 | 45 | 3.92 | 3.91 | 3.90 | 0.0110 | 0.0115 | 0.0114 |
| 0.0080 | 2-2116 | 45 | 3.92 | 3.91 | 3.90 | 0.0110 | 0.0115 | 0.0114 |
| 0.0100 | 2-1652 | 42 | 4.00 | 3.99 | 3.99 | 0.0107 | 0.0112 | 0.0110 |
| 0.0120 | 2-1080/7628 | 46 | 3.90 | 3.88 | 3.88 | 0.0111 | 0.0116 | 0.0115 |
| 0.0140 | 2-7628 | 41 | 4.03 | 4.02 | 4.01 | 0.0106 | 0.0111 | 0.0109 |
| 0.0180 | 2-7628/2116 | 42 | 4.00 | 3.99 | 3.99 | 0.0107 | 0.0112 | 0.0110 |
| 0.0210 | 3-7628 | 39 | 4.09 | 4.08 | 4.07 | 0.0104 | 0.0108 | 0.0107 |
| 0.0240 | 3-7628/2113 | 41 | 4.03 | 4.02 | 4.01 | 0.0106 | 0.0111 | 0.0109 |
| 0.0280 | 4-7628 | 40 | 4.06 | 4.05 | 4.04 | 0.0105 | 0.0110 | 0.0108 |
| 0.0310 | 4-7628/2113 | 40 | 4.06 | 4.05 | 4.04 | 0.0105 | 0.0110 | 0.0108 |
| 0.0350 | 5-7628 | 41 | 4.03 | 4.02 | 4.01 | 0.0106 | 0.0111 | 0.0109 |
| 0.0400 | 6-7628 | 37 | 4.15 | 4.13 | 4.13 | 0.0102 | 0.0106 | 0.0105 |
| 0.0590 | 9-7628 | 37 | 4.15 | 4.13 | 4.13 | 0.0102 | 0.0106 | 0.0105 |

### T40. Isola IS410 (phenolic-epoxy, lead-free compatible; Tg 170 C by DSC, Td 350 C by TGA at onset; Bereskin stripline method, ambient) (App. 1, p.239)

| Core thickness (in) | Construction | Resin % | Dk @ 2 GHz | Dk @ 5 GHz | Dk @ 10 GHz | Df @ 2 GHz | Df @ 5 GHz | Df @ 10 GHz |
|---|---|---|---|---|---|---|---|---|
| 0.0025 | 1-1080 | 58 | 3.72 | 3.65 | 3.65 | 0.026 | 0.027 | 0.027 |
| 0.0030 | 1-2113 | 44 | 4.04 | 3.98 | 3.98 | 0.021 | 0.022 | 0.022 |
| 0.0035 | 2-106 | 65 | 3.58 | 3.50 | 3.50 | 0.028 | 0.029 | 0.029 |
| 0.0040 | 1-2116 | 45 | 4.02 | 3.96 | 3.96 | 0.021 | 0.027 | 0.027 |
| 0.0043 | 106/1080 | 60 | 3.68 | 3.60 | 3.60 | 0.026 | 0.028 | 0.028 |
| 0.0050 | 1-1652 | 42 | 4.10 | 4.04 | 4.04 | 0.020 | 0.021 | 0.021 |
| 0.0053 | 106/2113 | 56 | 3.76 | 3.69 | 3.69 | 0.025 | 0.026 | 0.026 |
| 0.0060 | 1080/2113 | 53 | 3.83 | 3.76 | 3.76 | 0.024 | 0.025 | 0.025 |
| 0.0070 | 1-7628 | 41 | 4.12 | 4.07 | 4.07 | 0.020 | 0.021 | 0.021 |
| 0.0070 | 2-2113 | 51 | 3.87 | 3.81 | 3.81 | 0.023 | 0.024 | 0.024 |
| 0.0080 | 2-2116 | 45 | 4.02 | 3.96 | 3.96 | 0.021 | 0.027 | 0.027 |
| 0.0095 | 2-2116 | 52 | 3.85 | 3.78 | 3.78 | 0.024 | 0.025 | 0.025 |
| 0.0100 | 2-1652 | 42 | 4.10 | 4.04 | 4.04 | 0.020 | 0.021 | 0.021 |
| 0.0120 | 2-1080/7628 | 47 | 3.97 | 3.91 | 3.91 | 0.022 | 0.023 | 0.023 |
| 0.0140 | 2-7628 | 41 | 4.12 | 4.07 | 4.07 | 0.020 | 0.021 | 0.021 |
| 0.0180 | 2-7628/2116 | 42 | 4.10 | 4.04 | 4.04 | 0.020 | 0.021 | 0.021 |
| 0.0210 | 3-7628 | 39 | 4.18 | 4.12 | 4.12 | 0.019 | 0.020 | 0.020 |
| 0.0240 | 3-7628/2113 | 41 | 4.12 | 4.07 | 4.07 | 0.020 | 0.021 | 0.021 |
| 0.0280 | 4-7628 | 40 | 4.15 | 4.09 | 4.09 | 0.020 | 0.021 | 0.021 |
| 0.0310 | 4-7628/2116 | 40 | 4.15 | 4.09 | 4.09 | 0.020 | 0.021 | 0.021 |
| 0.0340 | 5-7628 | 40 | 4.15 | 4.09 | 4.09 | 0.020 | 0.021 | 0.021 |
| 0.0350 | 5-7628 | 41 | 4.12 | 4.07 | 4.07 | 0.020 | 0.021 | 0.021 |
| 0.0390 | 6-7628 | 37 | 4.23 | 4.18 | 4.18 | 0.019 | 0.020 | 0.020 |

### T41. Isola IS620 (low Dk, low Df, lead-free compatible; Tg 225 C, Td 363 C; rev April 2006) (App. 1, p.240)

| Core thickness (in) | Construction | Resin % | Dk @ 2 GHz | Dk @ 5 GHz | Dk @ 10 GHz | Df @ 2 GHz | Df @ 5 GHz | Df @ 10 GHz |
|---|---|---|---|---|---|---|---|---|
| 0.0020 | 1-106 | 70 | 3.33 | 3.31 | 3.30 | 0.0095 | 0.0098 | 0.0099 |
| 0.0021 (ZBC) | 1-106 | 71 | 3.33 | 3.31 | 3.30 | 0.0095 | 0.0098 | 0.0099 |
| 0.0027 | 1-1080 | 60 | 3.54 | 3.53 | 3.52 | 0.0090 | 0.0093 | 0.0094 |
| 0.0030 | 1-1080 | 63 | 3.47 | 3.46 | 3.45 | 0.0091 | 0.0094 | 0.0095 |
| 0.0035 | 2-106 | 66 | 3.41 | 3.39 | 3.48 (as printed) | 0.0093 | 0.0096 | 0.0097 |
| 0.0035 | 1-2113 | 51 | 3.76 | 3.74 | 3.74 | 0.0086 | 0.0089 | 0.0089 |
| 0.0040 | 2-106 | 70 | 3.33 | 3.31 | 3.30 | 0.0095 | 0.0098 | 0.0099 |
| 0.0040 | 1-3070 | 49 | 3.81 | 3.79 | 3.79 | 0.0086 | 0.0088 | 0.0089 |
| 0.0045 | 106/1080 | 63 | 3.47 | 3.41 | 3.41 | 0.0091 | 0.0094 | 0.0095 |
| 0.0050 | 1-2116 | 54 | 3.68 | 3.67 | 3.66 | 0.0088 | 0.0090 | 0.0091 |
| 0.0050 | 2-1080 | 57 | 3.61 | 3.59 | 3.59 | 0.0089 | 0.0092 | 0.0092 |
| 0.0050 | 106/2113 | 55 | 3.66 | 3.64 | 3.64 | 0.0088 | 0.0091 | 0.0091 |
| 0.0060 | 1080/2113 | 54 | 3.68 | 3.67 | 3.66 | 0.0088 | 0.0090 | 0.0091 |
| 0.0060 | 1080/106 | 70 | 3.33 | 3.31 | 3.30 | 0.0095 | 0.0098 | 0.0099 |
| 0.0070 | 2-2113 | 52 | 3.73 | 3.72 | 3.71 | 0.0087 | 0.0089 | 0.0090 |
| 0.0080 | 2-3070 | 49 | 3.81 | 3.79 | 3.79 | 0.0086 | 0.0088 | 0.0089 |
| 0.0100 | 3-1080 | 66 | 3.41 | 3.39 | 3.48 (as printed) | 0.0093 | 0.0096 | 0.0097 |
| 0.0100 | 2-2116 | 54 | 3.68 | 3.67 | 3.66 | 0.0088 | 0.0090 | 0.0091 |
| 0.0120 | 2-2113/1652 | 48 | 3.83 | 3.82 | 3.81 | 0.0085 | 0.0087 | 0.0088 |
| 0.0140 | 2-2116/1652 | 47 | 3.86 | 3.85 | 3.84 | 0.0087 | 0.0087 | 0.0087 |
| 0.0160 | 3-1652 | 46 | 3.89 | 3.87 | 3.87 | 0.0084 | 0.0086 | 0.0087 |
| 0.0180 | 2-3070/2-1652 | 46 | 3.89 | 3.87 | 3.87 | 0.0084 | 0.0086 | 0.0087 |
| 0.0210 | 2-2116/2-1652 | 50 | 3.78 | 3.77 | 3.76 | 0.0086 | 0.0088 | 0.0089 |
| 0.0240 | 2-2116/3-1652 | 46 | 3.89 | 3.87 | 3.87 | 0.0084 | 0.0086 | 0.0087 |
| 0.0280 | 2-3070/4-1652 | 45 | 3.91 | 3.90 | 3.89 | 0.0084 | 0.0086 | 0.0086 |

Nelco (p.241-248) and Rogers (p.249-252) data pages are images with no extractable text; only the p.236 summary values survive (see RITCHEY-299). The Appendix-1 N4000-13SI Tg (210 C) disagrees with the Table 5.2 printed order (245 C); treat as uncertain.

### T42. PDS impedance test set-up (App. 2, p.253-263)

| Setting / item | Value |
|---|---|
| Analyzer | Agilent E4401B with tracking generator; Agilent 82357A GPIB/USB + Benchlink export (.csv to spreadsheet) |
| Start / stop frequency | 10 kHz / 1 GHz |
| Resolution / video bandwidth | 3 kHz / 3 kHz |
| Attenuation / reference level | 10 dB / 0 dBm |
| Horizontal scale | log |
| Sweep time | 2.765 s |
| Auto sweep coupling | SR (stimulus response) |
| Source amplitude | 0 dBm |
| Calibration | generator cable straight to analyzer = 25 ohm level |
| Scale | 0 dB = 25 ohm; -20 dB = 2.5 ohm; -40 dB = 0.25 ohm; -60 dB = 25 mohm; -80 dB = 2.5 mohm |
| Probes | SR 141 semi-rigid coax, male SMA, needle tip |
| Cable parts (Pasternack) | PE9075 SMA-F to BNC-F $19.95; PE9073 SMA-F to BNC-M $19.95; PE4036 SMA-M cable connector $6.46; RG188A/U 50 ohm coax $0.54/ft; PE5006 crimp tool $69.95 |
| Bad-result example | ~0.5 ohm at 70 MHz (capacitor ESL vs plane-capacitor resonance) |

### T43. Generic fab-specification acceptance numbers (App. 3, p.264-287)

| Item | Requirement |
|---|---|
| Default quality class | IPC-6011 / IPC-6012 Class 2 (annular ring Class 3) |
| Min dielectric | 0.002 in, IPC-4101 Class B tolerance |
| Resin Tg | >= 170 C (TMA) |
| Default copper | 0.5 oz external and internal |
| Plies / resin content | >= 2 plies, >= 55% resin (signal/plane openings); plane-to-plane single ply, >= 42% |
| Glass next to signal layers | 106, 1080, 2116, 3313 |
| Layer registration | ±0.005 in |
| Tooling holes | location ±0.003 in; size +0.002/-0.001 in |
| Feature location / profile | ±0.005 in |
| Conductor to edge | >= 0.020 in |
| NPTH / non-plated slot | ±0.005 in |
| Fiducials | flat within 0.0006 in; sizes within 0.001 in of each other |
| Trace/space tolerance | lesser of ±20% or ±0.001 in (1/2 oz) / ±0.002 in (1 oz) |
| Edge roughness | <= 0.0005 in p-p over 0.50 in |
| SMT pad width tolerance | ±0.0014 in (0.025 in pitch); ±0.0010 in (< 0.025 in pitch) |
| Plated hole / plated slot | ±0.003 in / ±0.005 in |
| Bow and twist | <= 0.007 in/in |
| Nail-heading | <= 2 x foil thickness; negative etch-back <= 0.005 in |
| Edge finish | Ra <= 24 um |
| Weld repairs | outer only, traces > 0.006 in, <= 2 per side, <= 3 per board |
| Mask touch-ups | <= 3 per side, each <= 1 in long or 0.125 in^2 |
| Ionic contamination | <= 6.45 ug NaCl eq / in^2 |
| Solderability | J-STD-003, 20 s, >= 95% wetting; 6 months shelf |
| Copper | conductors >= 0.001 in; PTH average >= 0.001 in; elongation >= 10%; <= 1 void per PTH (<= 5% wall) |
| HASL | SN60/SN63; <= 2 passes; PTH 0.1-3.5 mil; 25 mil pitch pads 0.1-1.5 mil; finer pads 0.1-1.0 mil, <= 0.6 mil variation |
| Edge-finger Ni / Au | Ni 200 uin +300/-100; Au >= 30 uin avg (min 20), 99.7%, Knoop 140-200, <= 20 uin CLA |
| ENIG | Ni >= 100 uin avg (min 80); Au 4-10 uin (min 3) |
| OSP | Entek CU-106A 0.35 ± 0.05 um; Ronacoat <= 0.001 mil; ship within 3 months; no bake |
| Body Ni/Au | Ni 150-600 uin; Au 5-15 uin; optional Pd 5-15 uin; selective Au >= 20 uin |
| Solder mask | 0.4-1.2 mil cured; web >= 4 mil; one layer; green |
| Via plug cap | overlap > 0.004 in, <= 0.001 in above mask; vias <= 0.020 in |
| Legend | <= 0.001 in; 288 C / 30 s; registration <= 0.010 in; laser legend 0.7-1.1 mil |
| E-test | >= 40 VDC; continuity <= 10 ohm; flying probe if < 50 boards |
| Insulation resistance | >= 500 Mohm at 500 VDC |
| Impedance | ±10%; TDR tr < 200 ps; assumed permittivity 4.1 |
| Sampling | first article General Inspection Level I; production S-1 (ANSI/ASQC Z1.4-1993) |
| Package limits | > 60 in^2: 25; > 20-60 in^2: 250; <= 20 in^2: 360; PCMCIA: 1200; carton <= 50 lb |

### T44. Standard drill chart (App. 6, p.296; courtesy Sanmina) — decimal inch = size (fraction, wire gauge #, letter or mm)

0.0039 = 0.10 mm; 0.0051 = 0.13 mm; 0.0059 = #97; 0.0059 = 0.15 mm; 0.0063 = #96; 0.0067 = #95; 0.0071 = #94; 0.0075 = #93; 0.0079 = #92; 0.0079 = 0.20 mm; 0.0083 = #91; 0.0087 = #90; 0.0091 = #89; 0.0095 = #88; 0.0098 = 0.25 mm; 0.0100 = #87; 0.0105 = #86; 0.0110 = #85; 0.0115 = #84; 0.0118 = 0.30 mm; 0.0120 = #83; 0.0125 = #82; 0.0130 = #81; 0.0135 = #80; 0.0138 = 0.35 mm; 0.0145 = #79; 0.0156 = 1/64; 0.0157 = 0.40 mm; 0.0160 = #78; 0.0177 = 0.45 mm; 0.0180 = #77; 0.0197 = 0.50 mm; 0.0200 = #76; 0.0210 = #75; 0.0217 = 0.55 mm; 0.0225 = #74; 0.0236 = 0.60 mm; 0.0240 = #73; 0.0250 = #72; 0.0256 = 0.65 mm; 0.0260 = #71; 0.0276 = 0.70 mm; 0.0280 = #70; 0.0292 = #69; 0.0295 = 0.75 mm; 0.0310 = #68; 0.0312 = 1/32; 0.0315 = 0.80 mm; 0.0320 = #67; 0.0330 = #66; 0.0335 = 0.85 mm; 0.0350 = #65.

0.0354 = 0.90 mm; 0.0360 = #64; 0.0370 = #63; 0.0374 = 0.95 mm; 0.0380 = #62; 0.0390 = #61; 0.0394 = 1.00 mm; 0.0400 = #60; 0.0410 = #59; 0.0413 = 1.05 mm; 0.0420 = #58; 0.0430 = #57; 0.0433 = 1.10 mm; 0.0441 = 1.12 mm; 0.0453 = 1.15 mm; 0.0465 = #56; 0.0469 = 3/64; 0.0472 = 1.20 mm; 0.0492 = 1.25 mm; 0.0512 = 1.30 mm; 0.0520 = #55; 0.0531 = 1.35 mm; 0.0550 = #54; 0.0551 = 1.40 mm; 0.0571 = 1.45 mm; 0.0591 = 1.50 mm; 0.0595 = #53; 0.0610 = 1.55 mm; 0.0625 = 1/16; 0.0630 = 1.60 mm; 0.0635 = #52; 0.0650 = 1.65 mm; 0.0669 = 1.70 mm; 0.0670 = #51; 0.0689 = 1.75 mm; 0.0700 = #50; 0.0709 = 1.80 mm; 0.0728 = 1.85 mm; 0.0730 = #49; 0.0748 = 1.90 mm; 0.0760 = #48; 0.0768 = 1.95 mm; 0.0781 = 5/64; 0.0785 = #47; 0.0787 = 2.00 mm; 0.0807 = 2.05 mm; 0.0810 = #46; 0.0820 = #45; 0.0827 = 2.10 mm; 0.0846 = 2.15 mm; 0.0860 = #44; 0.0866 = 2.20 mm.

0.0886 = 2.25 mm; 0.0890 = #43; 0.0906 = 2.30 mm; 0.0925 = 2.35 mm; 0.0935 = #42; 0.0938 = 3/32; 0.0945 = 2.40 mm; 0.0960 = #41; 0.0965 = 2.45 mm; 0.0980 = #40; 0.0984 = 2.50 mm; 0.0995 = #39; 0.1004 = 2.55 mm; 0.1015 = #38; 0.1024 = 2.60 mm; 0.1040 = #37; 0.1043 = 2.65 mm; 0.1063 = 2.70 mm; 0.1065 = #36; 0.1083 = 2.75 mm; 0.1094 = 7/64; 0.1100 = #35; 0.1102 = 2.80 mm; 0.1110 = #34; 0.1122 = 2.85 mm; 0.1130 = #33; 0.1142 = 2.90 mm; 0.1160 = #32; 0.1161 = 2.95 mm; 0.1181 = 3.00 mm; 0.1200 = #31; 0.1201 = 3.05 mm; 0.1220 = 3.10 mm; 0.1240 = 3.15 mm; 0.1250 = 1/8; 0.1260 = 3.20 mm; 0.1280 = 3.25 mm; 0.1285 = #30; 0.1299 = 3.30 mm; 0.1319 = 3.35 mm; 0.1339 = 3.40 mm; 0.1358 = 3.45 mm; 0.1360 = #29; 0.1378 = 3.50 mm; 0.1398 = 3.55 mm; 0.1405 = #28; 0.1406 = 9/64; 0.1417 = 3.60 mm; 0.1437 = 3.65 mm; 0.1440 = #27; 0.1457 = 3.70 mm; 0.1470 = #26.

0.1476 = 3.75 mm; 0.1495 = #25; 0.1496 = 3.80 mm; 0.1516 = 3.85 mm; 0.1520 = #24; 0.1535 = 3.90 mm; 0.1540 = #23; 0.1555 = 3.95 mm; 0.1562 = 5/32; 0.1570 = #22; 0.1575 = 4.00 mm; 0.1590 = #21; 0.1594 = 4.05 mm; 0.1610 = #20; 0.1614 = 4.10 mm; 0.1634 = 4.15 mm; 0.1654 = 4.20 mm; 0.1660 = #19; 0.1673 = 4.25 mm; 0.1693 = 4.30 mm; 0.1695 = #18; 0.1713 = 4.35 mm; 0.1719 = 11/64; 0.1730 = #17; 0.1732 = 4.40 mm; 0.1752 = 4.45 mm; 0.1770 = #16; 0.1772 = 4.50 mm; 0.1791 = 4.55 mm; 0.1800 = #15; 0.1811 = 4.60 mm; 0.1820 = #14; 0.1831 = 4.65 mm; 0.1850 = #13; 0.1850 = 4.70 mm; 0.1870 = 4.75 mm; 0.1875 = 3/16; 0.1890 = #12; 0.1890 = 4.80 mm; 0.1909 = 4.85 mm; 0.1910 = #11; 0.1929 = 4.90 mm; 0.1935 = #10; 0.1949 = 4.95 mm; 0.1960 = #9; 0.1969 = 5.00 mm; 0.1988 = 5.05 mm; 0.1990 = #8; 0.2008 = 5.10 mm; 0.2010 = #7; 0.2028 = 5.15 mm; 0.2031 = 13/64.

0.2040 = #6; 0.2047 = 5.20 mm; 0.2055 = #5; 0.2067 = 5.25 mm; 0.2087 = 5.30 mm; 0.2090 = #4; 0.2106 = 5.35 mm; 0.2126 = 5.40 mm; 0.2130 = #3; 0.2146 = 5.45 mm; 0.2165 = 5.50 mm; 0.2185 = 5.55 mm; 0.2188 = 7/32; 0.2205 = 5.60 mm; 0.2210 = #2; 0.2224 = 5.65 mm; 0.2244 = 5.70 mm; 0.2264 = 5.75 mm; 0.2280 = #1; 0.2283 = 5.80 mm; 0.2303 = 5.85 mm; 0.2323 = 5.90 mm; 0.2340 = A; 0.2343 = 5.95 mm; 0.2344 = 15/64; 0.2362 = 6.00 mm; 0.2380 = B; 0.2382 = 6.05 mm; 0.2402 = 6.10 mm; 0.2420 = C; 0.2421 = 6.15 mm; 0.2441 = 6.20 mm; 0.2460 = D; 0.2461 = 6.25 mm; 0.2480 = 6.30 mm; 0.2500 = 1/4; 0.2500 = 6.35 mm; 0.2500 = E; 0.2520 = 6.40 mm; 0.2559 = 6.50 mm; 0.2570 = F; 0.2598 = 6.60 mm; 0.2610 = G; 0.2638 = 6.70 mm; 0.2656 = 17/64; 0.2657 = 6.75 mm; 0.2660 = H; 0.2677 = 6.80 mm; 0.2717 = 6.90 mm; 0.2720 = I; 0.2756 = 7.00 mm; 0.2770 = J.

### T45. Metric pad-stack tables (App. 7, p.297-298; mm)

Fig 4.70 metric — TID 0.254 mm, annular ring 0.051 mm:

| PCB thickness | 8:1 drill | 8:1 shadow | 8:1 capture | 8:1 clearance | 10:1 drill | 10:1 shadow | 10:1 capture | 10:1 clearance |
|---|---|---|---|---|---|---|---|---|
| 0.76 | 0.10 | 0.35 | 0.40 | 0.60 | 0.08 | 0.33 | 0.38 | 0.58 |
| 1.02 | 0.13 | 0.38 | 0.43 | 0.64 | 0.10 | 0.36 | 0.41 | 0.61 |
| 1.27 | 0.16 | 0.41 | 0.46 | 0.67 | 0.13 | 0.38 | 0.43 | 0.64 |
| 1.52 | 0.19 | 0.44 | 0.50 | 0.70 | 0.15 | 0.41 | 0.46 | 0.66 |
| 1.78 | 0.22 | 0.48 | 0.53 | 0.73 | 0.18 | 0.43 | 0.48 | 0.69 |
| 2.03 | 0.25 | 0.51 | 0.56 | 0.76 | 0.20 | 0.46 | 0.51 | 0.71 |
| 2.29 | 0.29 | 0.54 | 0.59 | 0.79 | 0.23 | 0.48 | 0.53 | 0.74 |
| 2.54 | 0.32 | 0.57 | 0.62 | 0.83 | 0.25 | 0.51 | 0.56 | 0.76 |
| 2.79 | 0.35 | 0.60 | 0.65 | 0.86 | 0.28 | 0.53 | 0.58 | 0.79 |
| 3.05 | 0.38 | 0.64 | 0.69 | 0.89 | 0.31 | 0.56 | 0.61 | 0.81 |
| 3.30 | 0.41 | 0.67 | 0.72 | 0.92 | 0.33 | 0.58 | 0.64 | 0.84 |
| 3.56 | 0.45 | 0.70 | 0.75 | 0.95 | 0.36 | 0.61 | 0.66 | 0.86 |
| 3.81 | 0.48 | 0.73 | 0.78 | 0.98 | 0.38 | 0.64 | 0.69 | 0.89 |
| 4.06 | 0.51 | 0.76 | 0.81 | 1.02 | 0.41 | 0.66 | 0.71 | 0.91 |
| 4.32 | 0.54 | 0.79 | 0.85 | 1.05 | 0.43 | 0.69 | 0.74 | 0.94 |
| 4.57 | 0.57 | 0.83 | 0.88 | 1.08 | 0.46 | 0.71 | 0.76 | 0.97 |
| 4.83 | 0.60 | 0.86 | 0.91 | 1.11 | 0.48 | 0.74 | 0.79 | 0.99 |
| 5.08 | 0.64 | 0.89 | 0.94 | 1.14 | 0.51 | 0.76 | 0.81 | 1.02 |
| 5.33 | 0.67 | 0.92 | 0.97 | 1.17 | 0.53 | 0.79 | 0.84 | 1.04 |
| 5.59 | 0.70 | 0.95 | 1.00 | 1.21 | 0.56 | 0.81 | 0.86 | 1.07 |
| 5.84 | 0.73 | 0.98 | 1.04 | 1.24 | 0.58 | 0.84 | 0.89 | 1.09 |
| 6.10 | 0.76 | 1.02 | 1.07 | 1.27 | 0.61 | 0.86 | 0.92 | 1.12 |
| 6.35 | 0.79 | 1.05 | 1.10 | 1.30 | 0.64 | 0.89 | 0.94 | 1.14 |

Fig 4.71 metric — TID 0.305 mm, annular ring 0.051 mm:

| PCB thickness | 8:1 drill | 8:1 shadow | 8:1 capture | 8:1 clearance | 10:1 drill | 10:1 shadow | 10:1 capture | 10:1 clearance |
|---|---|---|---|---|---|---|---|---|
| 0.76 | 0.10 | 0.40 | 0.45 | 0.71 | 0.08 | 0.38 | 0.43 | 0.69 |
| 1.02 | 0.13 | 0.43 | 0.48 | 0.74 | 0.10 | 0.41 | 0.46 | 0.71 |
| 1.27 | 0.16 | 0.46 | 0.51 | 0.77 | 0.13 | 0.43 | 0.48 | 0.74 |
| 1.52 | 0.19 | 0.50 | 0.55 | 0.80 | 0.15 | 0.46 | 0.51 | 0.76 |
| 1.78 | 0.22 | 0.53 | 0.58 | 0.83 | 0.18 | 0.48 | 0.53 | 0.79 |
| 2.03 | 0.25 | 0.56 | 0.61 | 0.86 | 0.20 | 0.51 | 0.56 | 0.81 |
| 2.29 | 0.29 | 0.59 | 0.64 | 0.90 | 0.23 | 0.53 | 0.59 | 0.84 |
| 2.54 | 0.32 | 0.62 | 0.67 | 0.93 | 0.25 | 0.56 | 0.61 | 0.86 |
| 2.79 | 0.35 | 0.65 | 0.70 | 0.96 | 0.28 | 0.58 | 0.64 | 0.89 |
| 3.05 | 0.38 | 0.69 | 0.74 | 0.99 | 0.31 | 0.61 | 0.66 | 0.92 |
| 3.30 | 0.41 | 0.72 | 0.77 | 1.02 | 0.33 | 0.64 | 0.69 | 0.94 |
| 3.56 | 0.45 | 0.75 | 0.80 | 1.06 | 0.36 | 0.66 | 0.71 | 0.97 |
| 3.81 | 0.48 | 0.78 | 0.83 | 1.09 | 0.38 | 0.69 | 0.74 | 0.99 |
| 4.06 | 0.51 | 0.81 | 0.86 | 1.12 | 0.41 | 0.71 | 0.76 | 1.02 |
| 4.32 | 0.54 | 0.85 | 0.90 | 1.15 | 0.43 | 0.74 | 0.79 | 1.04 |
| 4.57 | 0.57 | 0.88 | 0.93 | 1.18 | 0.46 | 0.76 | 0.81 | 1.07 |
| 4.83 | 0.60 | 0.91 | 0.96 | 1.21 | 0.48 | 0.79 | 0.84 | 1.09 |
| 5.08 | 0.64 | 0.94 | 0.99 | 1.25 | 0.51 | 0.81 | 0.86 | 1.12 |
| 5.33 | 0.67 | 0.97 | 1.02 | 1.28 | 0.53 | 0.84 | 0.89 | 1.14 |
| 5.59 | 0.70 | 1.00 | 1.05 | 1.31 | 0.56 | 0.86 | 0.92 | 1.17 |
| 5.84 | 0.73 | 1.04 | 1.09 | 1.34 | 0.58 | 0.89 | 0.94 | 1.19 |
| 6.10 | 0.76 | 1.07 | 1.12 | 1.37 | 0.61 | 0.92 | 0.97 | 1.22 |
| 6.35 | 0.79 | 1.10 | 1.15 | 1.40 | 0.64 | 0.94 | 0.99 | 1.25 |

Fig 4.72 metric — TID 0.254 mm, no annular ring: identical to the Fig 4.70 metric drill, shadow and clearance columns, with capture pad = hole shadow (e.g., 2.54 mm board, 8:1: 0.32 / 0.57 / 0.57 / 0.83; 10:1: 0.25 / 0.51 / 0.51 / 0.76).

### T46. Aspect ratio (thickness / drilled diameter) grid (App. 10, p.302)

Columns are the drilled diameter in mils (mm): 8 (0.2), 9 (0.23), 10 (0.254), 11 (0.279), 12 (0.305), 13 (0.33), 14 (0.356), 15 (0.381), 16 (0.406), 17 (0.432), 18 (0.457), 19 (0.483), 20 (0.508), 22 (0.559), 24 (0.61).

| t (mm) | t (mil) | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 22 | 24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.254 | 10 | 1.3 | 1.1 | 1 | 0.9 | 0.8 | 0.8 | 0.7 | 0.7 | 0.6 | 0.6 | 0.6 | 0.5 | 0.5 | 0.5 | 0.4 |
| 0.381 | 15 | 1.9 | 1.7 | 1.5 | 1.4 | 1.3 | 1.2 | 1.1 | 1.0 | 0.9 | 0.9 | 0.8 | 0.8 | 0.8 | 0.7 | 0.6 |
| 0.508 | 20 | 2.5 | 2.2 | 2 | 1.8 | 1.7 | 1.5 | 1.4 | 1.3 | 1.3 | 1.2 | 1.1 | 1.1 | 1.0 | 0.9 | 0.8 |
| 0.635 | 25 | 3.1 | 2.8 | 2.5 | 2.3 | 2.1 | 1.9 | 1.8 | 1.7 | 1.6 | 1.5 | 1.4 | 1.3 | 1.3 | 1.1 | 1.0 |
| 0.762 | 30 | 3.8 | 3.3 | 3 | 2.7 | 2.5 | 2.3 | 2.1 | 2.0 | 1.9 | 1.8 | 1.7 | 1.6 | 1.5 | 1.4 | 1.3 |
| 0.889 | 35 | 4.4 | 3.9 | 3.5 | 3.2 | 2.9 | 2.7 | 2.5 | 2.3 | 2.2 | 2.1 | 1.9 | 1.8 | 1.8 | 1.6 | 1.5 |
| 1.016 | 40 | 5.0 | 4.4 | 4 | 3.6 | 3.3 | 3.1 | 2.9 | 2.7 | 2.5 | 2.4 | 2.2 | 2.1 | 2.0 | 1.8 | 1.7 |
| 1.143 | 45 | 5.6 | 5.0 | 4.5 | 4.1 | 3.8 | 3.5 | 3.2 | 3.0 | 2.8 | 2.6 | 2.5 | 2.4 | 2.3 | 2.0 | 1.9 |
| 1.270 | 50 | 6.3 | 5.6 | 5 | 4.5 | 4.2 | 3.8 | 3.6 | 3.3 | 3.1 | 2.9 | 2.8 | 2.6 | 2.5 | 2.3 | 2.1 |
| 1.397 | 55 | 6.9 | 6.1 | 5.5 | 5.0 | 4.6 | 4.2 | 3.9 | 3.7 | 3.4 | 3.2 | 3.1 | 2.9 | 2.8 | 2.5 | 2.3 |
| 1.524 | 60 | 7.5 | 6.7 | 6 | 5.5 | 5.0 | 4.6 | 4.3 | 4.0 | 3.8 | 3.5 | 3.3 | 3.2 | 3.0 | 2.7 | 2.5 |
| 1.651 | 65 | 8.1 | 7.2 | 6.5 | 5.9 | 5.4 | 5.0 | 4.6 | 4.3 | 4.1 | 3.8 | 3.6 | 3.4 | 3.3 | 3.0 | 2.7 |
| 1.778 | 70 | 8.8 | 7.8 | 7 | 6.4 | 5.8 | 5.4 | 5.0 | 4.7 | 4.4 | 4.1 | 3.9 | 3.7 | 3.5 | 3.2 | 2.9 |
| 1.905 | 75 | 9.4 | 8.3 | 7.5 | 6.8 | 6.3 | 5.8 | 5.4 | 5.0 | 4.7 | 4.4 | 4.2 | 3.9 | 3.8 | 3.4 | 3.1 |
| 2.032 | 80 | 10.0 | 8.9 | 8 | 7.3 | 6.7 | 6.2 | 5.7 | 5.3 | 5.0 | 4.7 | 4.4 | 4.2 | 4.0 | 3.6 | 3.3 |
| 2.159 | 85 | 10.6 | 9.4 | 8.5 | 7.7 | 7.1 | 6.5 | 6.1 | 5.7 | 5.3 | 5.0 | 4.7 | 4.5 | 4.3 | 3.9 | 3.5 |
| 2.286 | 90 | 11.3 | 10.0 | 9 | 8.2 | 7.5 | 6.9 | 6.4 | 6.0 | 5.6 | 5.3 | 5.0 | 4.7 | 4.5 | 4.1 | 3.8 |
| 2.413 | 95 | 11.9 | 10.6 | 9.5 | 8.6 | 7.9 | 7.3 | 6.8 | 6.3 | 5.9 | 5.6 | 5.3 | 5.0 | 4.8 | 4.3 | 4.0 |
| 2.540 | 100 | 12.5 | 11.1 | 10 | 9.1 | 8.3 | 7.7 | 7.1 | 6.7 | 6.3 | 5.9 | 5.6 | 5.3 | 5.0 | 4.5 | 4.2 |
| 2.667 | 105 | 13.1 | 11.7 | 10.5 | 9.5 | 8.8 | 8.1 | 7.5 | 7.0 | 6.6 | 6.2 | 5.8 | 5.5 | 5.3 | 4.8 | 4.4 |
| 2.794 | 110 | 13.8 | 12.2 | 11 | 10.0 | 9.2 | 8.5 | 7.9 | 7.3 | 6.9 | 6.5 | 6.1 | 5.8 | 5.5 | 5.0 | 4.6 |
| 2.921 | 115 | 14.4 | 12.8 | 11.5 | 10.5 | 9.6 | 8.8 | 8.2 | 7.7 | 7.2 | 6.8 | 6.4 | 6.1 | 5.8 | 5.2 | 4.8 |
| 3.048 | 120 | 15.0 | 13.3 | 12 | 10.9 | 10.0 | 9.2 | 8.6 | 8.0 | 7.5 | 7.1 | 6.7 | 6.3 | 6.0 | 5.5 | 5.0 |
| 3.175 | 125 | 15.6 | 13.9 | 12.5 | 11.4 | 10.4 | 9.6 | 8.9 | 8.3 | 7.8 | 7.4 | 6.9 | 6.6 | 6.3 | 5.7 | 5.2 |
| 3.810 | 150 | 18.8 | 16.7 | 15 | 13.6 | 12.5 | 11.5 | 10.7 | 10.0 | 9.4 | 8.8 | 8.3 | 7.9 | 7.5 | 6.8 | 6.3 |
| 4.445 | 175 | 21.9 | 19.4 | 17.5 | 15.9 | 14.6 | 13.5 | 12.5 | 11.7 | 10.9 | 10.3 | 9.7 | 9.2 | 8.8 | 8.0 | 7.3 |
| 5.080 | 200 | 25.0 | 22.2 | 20 | 18.2 | 16.7 | 15.4 | 14.3 | 13.3 | 12.5 | 11.8 | 11.1 | 10.5 | 10.0 | 9.1 | 8.3 |
| 5.715 | 225 | 28.1 | 25.0 | 22.5 | 20.5 | 18.8 | 17.3 | 16.1 | 15.0 | 14.1 | 13.2 | 12.5 | 11.8 | 11.3 | 10.2 | 9.4 |
| 6.350 | 250 | 31.3 | 27.8 | 25 | 22.7 | 20.8 | 19.2 | 17.9 | 16.7 | 15.6 | 14.7 | 13.9 | 13.2 | 12.5 | 11.4 | 10.4 |

Legend classes (cell colours not preserved): manufacturable at any good fabricator; at many but not all US fabricators; at top-tier US, a few European and few if any Pacific Rim fabricators; at fabricators with reverse-pulse plating; hand-built only ("not a wise choice for any PCBs, except experiments"). See RITCHEY-338 for the inferred numeric bands.

### T47. Unit conversions (App. 9, p.301)

- mm -> mil (x 39.370): 0.1 = 3.937; 0.2 = 7.874; 0.3 = 11.811; 0.4 = 15.748; 0.5 = 19.685; 0.6 = 23.622; 0.7 = 27.559; 0.8 = 31.496; 0.9 = 35.433; 1.0 = 39.370; 1.1 = 43.307; 1.2 = 47.244; 1.3 = 51.181; 1.4 = 55.118; 1.5 = 59.055; 1.6 = 62.992; 1.7 = 66.929; 1.8 = 70.866; 1.9 = 74.803; 2.0 = 78.740.
- mil -> mm (x 0.0254): 0.7 = 0.018; 1 = 0.025; 1.4 = 0.036; 2 = 0.051; 2.8 = 0.071; 3 = 0.076; 4 = 0.102; 5 = 0.127; 6 = 0.152; 7 = 0.178; 8 = 0.203; 9 = 0.229; 10 = 0.254; 11 = 0.279; 12 = 0.305; 13 = 0.330; 14 = 0.356; 15 = 0.381; 16 = 0.406; 17 = 0.432; 18 = 0.457; 19 = 0.483; 20 = 0.508; 21 = 0.533; 22 = 0.559; 23 = 0.584; 24 = 0.610; 25 = 0.635; 26 = 0.660; 27 = 0.686; 28 = 0.711; 29 = 0.737; 30 = 0.762; 31 = 0.787; 32 = 0.813; 33 = 0.838; 34 = 0.864; 35 = 0.889; 36 = 0.914; 37 = 0.940; 38 = 0.965; 39 = 0.991; 40 = 1.016; 41 = 1.041; 42 = 1.067; 43 = 1.092; 44 = 1.118; 45 = 1.143; 46 = 1.168; 47 = 1.194; 48 = 1.219; 49 = 1.245; 50 = 1.270.
- mil -> micron (x 25.4): 0.7 = 17.78; 1 = 25.40; 1.4 = 35.56; 2 = 50.80; 2.8 = 71.12; 3 = 76.20; 4 = 101.60; 5 = 127.00; 6 = 152.40; 7 = 177.80; 8 = 203.20; 9 = 228.60; 10 = 254.00; 11 = 279.40; 12 = 304.80; 13 = 330.20; 14 = 355.60; 15 = 381.00; 16 = 406.40; 17 = 431.80; 18 = 457.20; 19 = 482.60; 20 = 508.00; 21 = 533.40; 22 = 558.80; 23 = 584.20; 24 = 609.60; 25 = 635.00.
- Copper weight: 0.7 mil = 1/2 oz, 1.4 mil = 1 oz, 2.8 mil = 2 oz (the conversion table's first mil rows).

## 3. Mechanizable checks

Notation: lengths in mil or in as stated; v = propagation velocity in the PCB. The book uses ~6 in/ns for er ~4; generally v = 11.8/sqrt(er_eff) in/ns (standard physics, not stated in the book). Items marked "(derived)" combine book relations into a computable form.

**Signal integrity / termination**

- `CHECK-hs-net-boundary`: inputs net, L_route (in), tr_min (ns, fastest IBIS edge), er_eff, term_type -> TEL = tr_min x v; L_limit = TEL/4 (conservative TEL/6) -> pass if L_route <= L_limit OR the net's class has a simulated termination rule (term_type != none) -> margin = (L_limit - L_route)/L_limit for unterminated nets -> RITCHEY-001, -002, -005.
- `CHECK-input-overshoot`: inputs per receiver simulated Vmax, Vmin (V), Vdd -> pass if Vmax <= Vdd + 0.3 V and Vmin >= Vss - 0.3 V (the Vss side is inferred from the protection diodes to both rails) -> margin = Vdd + 0.3 - Vmax -> RITCHEY-003, -004, -291.
- `CHECK-series-termination`: inputs Zout, Rs, Z0_nom (ohm), tol (default 0.10), loads, t_line, t_bit -> Vbench/V = Z0/(Z0 + Rs + Zout) -> pass if Zout + Rs <= Z0_nom x (1 - tol) (Vbench >= V/2 over the whole tolerance band) AND loads = 1 AND 2 x t_line < t_bit -> margin = Z0_nom(1 - tol) - (Zout + Rs) -> RITCHEY-169, -261, -289.
- `CHECK-parallel-termination`: inputs R_term, Z0_nom, tol (single-ended) or R_across and Z0 per line (differential) -> Gamma = (R - Z0)/(R + Z0) -> pass if R_term >= Z0_nom(1 + tol) (book value 1.1 x Z0: 55 ohm per 50 ohm line, 110 ohm across a 100 ohm pair), so Gamma >= 0 at every in-tolerance Z0 -> margin = R_term - Z0_max -> RITCHEY-168, -228.
- `CHECK-diff-termination-topology`: inputs data rate, termination netlist -> pass if rate < 2.4 Gb/s (single 100 ohm acceptable) or rate >= 2.4 Gb/s with two 50 ohm resistors plus ~10 pF from their centre to logic ground -> RITCHEY-207.
- `CHECK-backward-xtalk-critical-length`: inputs coupled length Lc (in), tr (ns), er -> L_crit = 0.75 in x (tr / 0.2 ns) x sqrt(4/er) (Fig 1.9 anchor scaled linearly; derived) -> classify: Lc >= L_crit means saturated backward crosstalk, so the class spacing rule must hold -> RITCHEY-006, -007.
- `CHECK-class-spacing`: inputs per adjacent-trace pair edge spacing s (mil), classes A and B, technology table -> pass if s >= in-class spacing (A = B) else >= to-other-class spacing (examples: SE 6/15, Gb diff 10/20, 22-layer SE >= 25 mil) -> margin = s - s_rule -> RITCHEY-016, -017, -094.
- `CHECK-dual-stripline-orthogonality`: inputs per layer preferred direction, segment vectors -> pass if adjacent signal layers between the same planes are X/Y orthogonal and broadside-parallel overlap is below L_crit (backplanes: single-stripline stackup required) -> RITCHEY-080, -081, -210.
- `CHECK-diff-inpair-skew`: inputs L_p, L_n (in), tr_fastest at receiver (ns), UI (ns), context -> limits: general = tr_fastest x v (400 ps -> 2.4 in; 2.4 Gb/s -> 300 mil); into UTP or a multi-pair connector = 0.025 x UI x v (2.4 Gb/s -> 60 mil); baffled connector at 2.4 Gb/s = 60 mil -> pass if abs(L_p - L_n) <= limit -> margin = limit - abs(dL) -> RITCHEY-201, -217, -227.
- `CHECK-diff-pair-geometry`: inputs 2D-solver Zdiff at nominal spacing and at the widest spacing the pair will spread to (e.g., 39 mil through a 1 mm BGA), reference plane under each member -> pass if Zdiff_spread / Zdiff_nom <= ~1.10 (loose example 109/100 acceptable; tight 140/100 fails — derived threshold), both members over the same plane, no broadside pairs -> RITCHEY-210 to -215.
- `CHECK-diff-aggressor-noise`: inputs coupling coefficients from each aggressor to the near and far pair members (2D solver), differential noise budget -> differential noise = k_near - k_far (Fig 8.5: 12% - 1% or 2%) -> pass if sum over aggressors <= budget -> RITCHEY-209, -211.
- `CHECK-channel-loss-choice`: inputs path length, rate, candidate laminate Df (T38-T41), trace width -> rule: before widening beyond 5 mil, try a lower-Df laminate (33 in @ 2.5 GHz: width 5 -> 10 mil ~1 dB vs FR-4 -> 4000-13 ~2 dB, -> 4000-13SI/IS620 ~4 dB) -> pass if the simulated eye meets the mask with margin -> RITCHEY-224, -225.
- `CHECK-ac-coupling-cap`: inputs coupling capacitor value/package, rate -> pass if 0.01 uF 0402 (or better) and rate <= 9.6 Gb/s (measured no degradation below 3 GHz) -> RITCHEY-229.
- `CHECK-via-capacitance-budget`: inputs per net rate, via count, drill d (mil), via length Lv (mil) -> C_via ~ 0.6 pF x (d/26 mil) x (Lv/100 mil) (scaling with barrel area, derived; anchors 12 x 100 mil ~0.65 pF, 26 x 250 mil ~1.5-2 pF) -> pass if rate <= 3.125 Gb/s (no restriction), else the channel must be simulated with these capacitances and show no resonance-closed eye; above 4.8 Gb/s prefer blind vias, smaller drills or back-drill -> RITCHEY-066, -125 to -129, -220, -221.
- `CHECK-stub`: inputs escape/test-point trace position -> pass if any short escape trace to a test via sits at a net END, not mid-net -> RITCHEY-102.
- `CHECK-glass-weave`: inputs glass style per signal opening, rate -> pass if rate < 2.5 Gb/s or the opening uses 3313 (or an accepted ±10% weave-induced impedance swing) -> RITCHEY-074, -148, -149.

**Power delivery**

- `CHECK-pdn-target-impedance`: inputs rail V, ripple spec dV, worst-case dI (widest SE bus 0 -> 1 plus core standby -> active), capacitor tolerance tol_C (0.15), measured or simulated Z(f) -> Z_target = dV/dI; Z_design = Z_target/(1 + tol_C) (derived) -> pass if Z(f) <= Z_design for DC <= f <= 1 GHz (board) -> margin = min_f(Z_design - Z(f)) -> RITCHEY-021, -022, -029, -160, -165, -308.
- `CHECK-cap-bank-model`: inputs per capacitor type C, ESR, ESL, L_mount (pads + vias; L_via = 36 pH/mil x length), n; plane C; converter L -> C_tot = nC, ESR_tot = ESR/n, L_tot = (ESL + L_mount)/n, Z_i(f) = ESR_tot + j(2 pi f L_tot - 1/(2 pi f C_tot)), total = parallel of all branches -> pass if total <= Z_design and no antiresonance peak exceeds it (use SPICE or a 2D plane model; the spreadsheet method is blind to antiresonances) -> RITCHEY-025, -028, -030, -034, -041, -042.
- `CHECK-cap-count-for-esr`: inputs ESR_each, Z_target -> n_min = ceil(ESR_each / Z_target) (e.g., 400 mohm parts for 20 mohm -> 20) -> RITCHEY-034.
- `CHECK-cap-dielectric`: inputs dielectric code, V_applied/V_rated, T_max -> fail C0G/NP0 used as bulk decoupling; fail Y5V (C x 0.5 at 16% of rating, x 0.1 at 50%); warn Z5U; require X7R when T_max > 85 C (X5R rated only to 85 C) and prefer X7R whenever T is well above 25 C -> RITCHEY-035, -036.
- `CHECK-plane-capacitance-required`: inputs V, dV, N simultaneously switched lines, per-line capacitance C_line (= length x t_pd / Z0, derived) -> C_req = V x N x C_line / dV; C_design = 1.5 x C_req x er(DC)/er(1 GHz) -> pass if C_available >= C_design -> RITCHEY-031, -303.
- `CHECK-plane-capacitance-available`: inputs overlap area A (in^2), separation t (mil), er, copper fill k (1.0 solid, 0.85 nominal density, 0.70 very high density) -> C = 224.9 x er x A x k / t pF (derived parallel-plate form; ~450 pF/in^2 at 2 mil er ~4) -> RITCHEY-044, -159, -257.
- `CHECK-plane-pair-inductance`: inputs dielectric t, die radius R1, capacitor/ball ring radius R2 -> L_sq = mu0 x t (94 pH at 75 um, 31 pH at 25 um); L_ring = L_sq/(2 pi) x ln(R2/R1) -> RITCHEY-257, -258.
- `CHECK-converter-gap`: inputs measured converter Z(f), bulk capacitor bank -> L_conv = Z/(2 pi f) above the regulation corner (~100 Hz) -> pass if the bulk bank keeps Z <= Z_target from the corner up to the ceramic crossover -> RITCHEY-037, -038, -039.
- `CHECK-io-return-current`: inputs N simultaneously switching SE outputs, Vddq, Z0, t_line, tr, return-path inductance L_ret -> I_bus = N x (Vddq/2)/Z0 (series-terminated); t_pulse = 2 x t_line; V_bounce ~ L_ret x I_bus / tr (derived) -> pass if V_bounce <= its noise-margin allocation -> RITCHEY-023, -250, -262.
- `CHECK-core-transient`: inputs charge per clock edge Q, pulse width t_w, Vdd, f_clk -> I_pk = Q/t_w; P = Q x Vdd x f_clk (Table 10.1 check: 18.50 nC / 0.15 ns = 123 A; 18.50 nC x 1.5 V x 500 MHz = 13.9 W) -> RITCHEY-252.
- `CHECK-package-pdn`: inputs ball map, pair loop inductance (Eq 10.6 at pitch), PCB plane spreading L, package plane L, on-chip C, package capacitor ESL/n -> L_pairs = L_loop/N_pairs; parallel centre and edge paths; f_res = 1/(2 pi sqrt(L_pkg x C_die)); ripple = Z_max x dI -> pass if Z(f) <= target over 1 MHz-several GHz and ripple <= spec (PKG-B: 13.4 pH, < 7 mohm, 3% ripple passes; PKG-A: 45.5 pH, 170 MHz peak > 50 mohm, 21% fails) -> RITCHEY-259 to -276.
- `CHECK-ball-map`: inputs BGA ball grid with types (S, Vdd, GND, Vddq) -> pass if every signal ball has >= 1 PWR/GND 4-neighbour (Virtex-4 minimum; PKG-B target >= 2), core Vdd/GND form a checkerboard (count adjacent V-G pairs), Vdd balls exist at the perimeter as well as the centre, no clusters of same-type power balls or of signal balls -> RITCHEY-260, -270, -271, -278.
- `CHECK-ripple-measured`: inputs measured worst-case ripple per rail (bus-switch and standby -> active tests) -> pass if <= spec -> RITCHEY-307.

**Stackup / materials**

- `CHECK-stackup-structure`: inputs ordered layers (type sig/plane/mount, net, oz) and dielectrics (core/prepreg, construction, thickness) -> pass if all hold: (a) each controlled-impedance signal layer's nearest plane is across a core, not prepreg; (b) each PWR/GND pair is adjacent across prepreg >= 3.4 mil (never a single 106 or 1080 ply; >= 4 mil between different voltages under GR-78-CORE); (c) same copper weight on both faces of every core; (d) first plane below each outer layer is GND; (e) no two power planes back-to-back; (f) every plane pair = one GND + one PWR; (g) outer layers carry no impedance-critical classes; (h) signal-to-plane h = 5 mil (typical fab) or 4 mil (best fab); (i) thickness padding only in L1-L2, Ln-1-Ln and signal-pair openings -> RITCHEY-026, -052, -076, -078, -079, -083, -088, -090, -092.
- `CHECK-layer-count-risk`: inputs layer count -> warn if < 10 (impedance or plane capacitance compromised; use signal-layer fill); fail-soft if 4 layers (no plane capacitance: route SE signals start-to-end on one layer, no split crossings) -> RITCHEY-047, -091, -166.
- `CHECK-impedance-design`: inputs field-solver Z0 per layer (er taken at ~2 GHz, or ~1.8 GHz for 300 ps edges; solder mask included on outer layers), target, fab tier -> pass if centred and the specified tolerance is achievable (±10% standard, ±5% advanced); outer layers budget up to 20% variation -> RITCHEY-076, -085, -095, -096, -137.
- `CHECK-copper-thickness`: inputs oz per layer -> t_design = 0.6 mil (1/2 oz), 1.2 mil (1 oz) (nominal minus ~0.2 mil) -> RITCHEY-075, -145.
- `CHECK-tg-selection`: inputs t_pcb (mil), solder type, laminate Tg -> pass: leaded — t <= 63: Tg >= 135 C; t > 63: Tg >= 170 C. Lead-free — t <= 63: Tg >= 170 C; t > 63: Tg >= 220 C -> RITCHEY-153, -154.
- `CHECK-water-absorption`: inputs laminate WA (%) -> pass if < 0.2%, else require bake + conformal coat -> RITCHEY-157.
- `CHECK-single-laminate-supplier`: inputs supplier per opening -> pass if a single supplier for all laminate and prepreg -> RITCHEY-146.
- `CHECK-dielectric-isolation`: inputs isolation voltage V_iso, dielectric t (mil) -> pass if t >= 3 mil for <= 1700 VDC (wicking allowance; DBV >= 1000 V/mil nominal) -> RITCHEY-143, -156.

**Via / pad stack / DFM**

- `CHECK-pad-stack`: inputs t_pcb, AR_max (6 volume, 8 high-rel, 10 best fab), TID (= 2 x TIR: 10 / 12 / 14 mil), insulation ins (5 mil; 4 mil GR-78-CORE), annular ring r (2 or 0 mil), pitch p, trace w and space s (>= 4/4 volume), traces needed n -> d = max(t_pcb/AR_max, fab minimum drill; 12 mil on 100+ mil boards); shadow = d + TID; clearance = shadow + 2 x ins; capture = shadow + 2 x r; plane web = p - clearance; signal gap = p - capture - 2 x ins; n_fit = floor((web + s)/(w + s)) -> pass if web > 0 (antipads never overlap) and n_fit >= n; auto-fail n = 2 at 1 mm pitch and any trace at 0.8 mm pitch with through-vias (use blind vias) -> margin = web - (n x w + (n - 1) x s) -> RITCHEY-109 to -121, -170. Worked anchors: 50 mil pitch web 18 mil; 1 mm web 7.37 mil.
- `CHECK-drill-chart`: inputs holes with finished-size requirements -> drill = FHS + 4 mil -> pass if the chart lists drill sizes (both for press-fit) -> RITCHEY-049, -113, -131.
- `CHECK-thru-via-aspect-ratio`: inputs t_pcb, d -> AR = t/d -> pass if <= 6 (any fab, volume), <= 8 (many US fabs), <= 10 (top tier); 12 needs RPP or hand plating -> RITCHEY-119, -137, -282, -338.
- `CHECK-blind-via-aspect-ratio`: inputs blind diameter d, depth h -> pass if d >= h (fab-safe d >= 1.5 h) -> RITCHEY-064.
- `CHECK-via-in-pad`: inputs BGA pads with vias -> pass if each via is copper-filled (button plated) or offset from the ball centre -> RITCHEY-065.
- `CHECK-fab-capability`: inputs design minima (via drill, finished hole, lands, antipad, line, space, line-to-land, registration, pitch, thickness, dielectric, edge clearance, mask clearance, line-to-SMT, impedance tolerance) -> pass if every value meets the Fig 4.79 column of the target fab tier -> RITCHEY-137, T18.
- `CHECK-thermal-relief`: inputs pad type -> pass if THT pins into planes use 2-spoke ties and SMT pads have no thermal reliefs -> RITCHEY-112, -138 to -140.
- `CHECK-nonfunctional-pads`: pass if no inner-layer pad lacks a trace connection -> RITCHEY-122.
- `CHECK-plane-split`: inputs gap width, copper oz, crossing signals, rail PDS impedance -> pass if gap >= 3 mil (1/2 oz) / 6 mil (1 oz) (10 mil recommended) and crossings only where both rails meet their PDS target (never on 4-layer boards) -> RITCHEY-160 to -162, -166.
- `CHECK-test-structures`: pass if every controlled-impedance layer has an in-board test trace (>= 3 in, signal width, 30 mil probe drill, 100 mil to ground via, silkscreen layer label), each rail has 2 plane-access structures >= 1 in apart (44/50/30 mil, 75 mil pitch, no thermals), and stacking stripes exist (50 mil + 50 mil per layer, 25 mil in / 25 mil out, 5 mil etch segment, >= 20 mil from planes) -> RITCHEY-104 to -108.
- `CHECK-panelization`: inputs board outline -> boards per usable panel area (22 x 34, 16 x 22, 14 x 16, 10 x 16 in) -> choose the outline that maximizes yield per standard panel -> RITCHEY-141.
- `CHECK-finish-thickness`: inputs finish spec -> pass if electroplated Au 5-10 uin (<= 15 uin nominal) over Ni >= 150-200 uin; ENIG Ni >= 100 uin, Au 4-10 uin; never tin or immersion tin -> RITCHEY-068, -069, -327, -329.
- `CHECK-fab-lot-acceptance`: inputs lot data -> pass if bow/twist <= 0.007 in/in; ionic <= 6.45 ug/in^2; IR >= 500 Mohm @ 500 V; e-test >= 40 V and <= 10 ohm; PTH copper >= 1 mil; impedance ±10% with TDR tr < 200 ps read at trace start; mask 0.4-1.2 mil -> RITCHEY-100, -319, -322, -324, -330, -333 to -335.

**EMI / enclosure / thermal**

- `CHECK-emi-margin`: inputs emission scan -> pass if emissions <= limit - 6 dB over 30 MHz to max(1 GHz, 5 x f_clk) radiated and 150 kHz-30 MHz conducted -> RITCHEY-171, -188.
- `CHECK-ground-cage-bonds`: inputs bond list -> pass if exactly one DC logic-ground-to-cage bond (non-current-carrying backplane ground planes excepted), no faceplate or card-edge bonds to logic ground -> RITCHEY-175, -183, -184, -194.
- `CHECK-emi-apertures`: inputs vent apertures -> pass if max dimension <= 0.25 in and screens/honeycombs are bonded all round -> RITCHEY-177.
- `CHECK-shield-plane-capacitor`: inputs area A, separation t, er, isolation V -> C = e0 er A/t (370 pF example with 8 mil insulation, > 8000 V) -> pass if t meets the isolation voltage and the capacitor is plane-built (no discrete part meets both requirements) -> RITCHEY-179, -204.
- `CHECK-cooling-class`: inputs chip power P -> class: <= ~2 W easy; 5-10 W via PCB planes; 25-50 W heat sink and a few hundred lfm; > 100 W heat pipe or liquid -> RITCHEY-251.
- `CHECK-junction-temperature`: inputs Tj -> pass if Tj <= 100 C; speed derate ~0.2%/C -> RITCHEY-251.

## 4. Verification procedures & plots

| # | Property | Plot / test | x axis | y axis | Sweep / corners | Good looks like / pass | Setup notes | Source |
|---|---|---|---|---|---|---|---|---|
| V1 | High-speed boundary / overshoot | Receiver voltage vs time for one driver/line | time (ns) | V (mV) | line length 12, 6, 3, 1.5, 0.75, 0.5 in; Rs = 0 then designed Rs; fastest and slowest IBIS corners | peak <= Vdd + 0.3 V (3.6 V for 3.3 V logic) | HyperLynx LineSim-type tool; 50 ohm line | p.15-16, Figs 1.2-1.7 |
| V2 | Backward crosstalk saturation | Backward and forward crosstalk vs parallel coupled length | coupled length | crosstalk amplitude | lengths past L_crit; tr of fastest part | backward term flattens at L_crit; noise within budget | 2D field solver + SI tool | p.17-18, Figs 1.8-1.9 |
| V3 | Load-current spectrum | FFT of the line-charging current pulse | frequency (0-1 GHz) | current spectral amplitude | 12 in vs 3 in line; fastest vs slowest edge | shows the band the PDS must cover (e.g., ~85-900 MHz), not clock harmonics | SI tool spectrum analyzer | p.29-30, p.143-144, Figs 3.4, 7.13-7.14 |
| V4 | PDS impedance, design | Z(f) per capacitor bank and total (spreadsheet), then SPICE and 2D plane model | log f, 1 kHz-1 GHz | log Z (ohm) | capacitor tolerance ±15%; ESR corners | total <= target line everywhere; no antiresonance above target; plane model above ~200 MHz | SPICE: 1 A AC source so 1 mV = 1 mohm; banks as nC, ESR/n, (ESL + L_mount)/n | p.31-33, Figs 3.5-3.9 |
| V5 | ESR vs antiresonance | Z(f) of 1 uF 0603 in parallel with 10 nF plane | f 1-1000 MHz | Z (mohm) | ESR 20, 100, 400 mohm | peak at ~35 MHz disappears as ESR rises; count parts for the target | — | p.38, Fig 3.19 |
| V6 | DC-DC converter output impedance | Load-step ripple vs frequency | log f, 10 Hz-100 kHz | Z (mohm) | full load; output C 42 uF vs 2147 uF | flat at regulated Z to ~100 Hz; extract L = Z/(2 pi f) above | square-wave generator drives Q1 load; R1 sized to ~1/10 Vout at max load; low-L loop; dual-trace scope | p.39-42, Figs 3.21-3.24 |
| V7 | Capacitor characterization | Capacitor Z(f) | log f | log Z | — | C from the left slope, ESL from the right slope, ESR at the minimum | vendor tool (e.g., AVX SpiCap) or VNA | p.42, Fig 3.25 |
| V8 | Plane capacitance vs spacing | C per in^2 vs dielectric thickness | t (mil), 0-20 | pF/in^2 | copper fill 100 / 85 / 70% | meets the required plane capacitance | er 4.1 | p.43, Fig 3.27 |
| V9 | Controlled impedance acceptance | TDR trace along each 3 in test trace | time / distance | ohm | every controlled layer; fab TDR rise time | read Z just after the probe transient; within ±10% band | same edge rate as the fab's tester (Polar CITS800 175 ps); any continuous plane as ground | p.81-86, Table 4.3, Fig 4.53 |
| V10 | Glass-weave impedance ripple | TDR of long traces at several angles | distance | ohm | 1080/106 vs 3313 cloth | 3313 flat; 1080 ripples almost ±10% | — | p.113-115, Figs 5.10, 5.13 |
| V11 | Plane split / layer change transparency | TDR across a plane split and through layer-change vias with and without adjacent ground vias; near-field probe scan across the split | time; position | ohm; dBuV | 125 ps TDR | no detectable discontinuity; no near-field change | Tek 1502C; RF generator + near-field probe + spectrum analyzer | p.123-128, Figs 6.3, 6.7 |
| V12 | Radiated emissions | Emission scan vs CISPR/FCC limit | f, 30 MHz-1 GHz (or 5 x f_clk) | dBuV/m | before/after fixes; several units (edge-rate spread) | >= 6 dB below the limit | compliant test site | p.132, p.137-145, Figs 7.5, 7.7, 7.12 |
| V13 | Channel loss and via resonances | Measured and simulated S21 | f, 0-6 GHz | dB | with/without back drilling; extra routing via; with/without AC-coupling capacitors | via effects negligible below ~1.6 GHz; resonances identified before routing; AC caps no effect below 3 GHz | 4-port network analyzer on test PCBs; SMA launches characterized | p.99-100, p.161-162, p.169-170, Figs 4.75, 8.11, 8.23 |
| V14 | Serial-link eye | Eye diagram at receiver | time over one UI | differential V | 0.1, 1, 2.4, 4.8, 5.2 Gb/s; losses on/off; via C on/off; pre-emphasis 0/15% | eye clears the hexagon mask and max-amplitude boxes | validated channel model with SPICE/IBIS drivers | p.162-166, Figs 8.12-8.20 |
| V15 | Differential crosstalk | Crosstalk into near and far pair members | aggressor spacing | % of aggressor | broadside vs coplanar pairs | differential (near - far) within noise budget | 2D field solver | p.156-157, Fig 8.5 |
| V16 | Differential impedance vs spreading | Zdiff vs in-pair spacing | spacing (mil) | ohm | tight 5/5 vs loose 10/15 | Zdiff stays near 100 ohm when spread (109 ok, 140 not) | 2D field solver | p.158-159, Fig 8.8 |
| V17 | Loss trade | Insertion loss vs frequency for trace widths and laminates | f | dB | width 5-10 mil; FR-4 / 4000-13 / 4000-13SI | pick the laminate before widening traces | 33 in path | p.167-168, Fig 8.21 |
| V18 | Package core PDS | Z(f) of package-ball path, package capacitors, on-chip capacitance | f, 1 MHz-10 GHz | ohm | candidate packages | no parallel resonance above target (PKG-B < 7 mohm) | Eq 10.5/10.6 estimates or 3D extraction | p.204-205, Figs 10.34-10.35 |
| V19 | Package I/O quality | Clock jitter and data eye measured at the receiving BGA vias | time | V | all I/O banks active | low jitter (e.g., 97 ps) and small Vddq/ground bounce | TDS7404 4 GHz scope, P7240 4 GHz active probe | p.181-182, Figs 10.7-10.12 |
| V20 | Bare-board plane capacitance | Capacitance meter across each rail's plane pair | — | pF/nF | every rail | matches design (allow er(f) and spacing tolerance) | labelled access structures | p.83, p.253 (App. 2) |
| V21 | Assembled PDS impedance | Shunt Z(f) with spectrum analyzer + tracking generator | log f, 10 kHz-1 GHz | dB -> ohm (0 dB = 25 ohm, -20 dB/decade) | board with only bypass capacitors fitted; each rail | below target; no peaks (e.g., 0.5 ohm at 70 MHz fails) | E4401B settings in T42; SR-141 needle probes | p.253-262 (App. 2) |
| V22 | Worst-case ripple | Scope capture of each rail during stress firmware | time | mV | widest SE bus toggling 0 -> 1 repeatedly; processor standby <-> full | ripple <= spec | scope bandwidth >= highest signal frequency | p.262 (App. 2) |
| V23 | Stackup audit | Stacking-stripe microscope inspection | — | — | every lot | layer order correct; dielectric and copper thickness and 5 mil etch segment as drawn | non-destructive, edge of board | p.86-88 |
| V24 | Bare-board electrical | Net-list e-test, hi-pot, insulation resistance | — | — | 100% of boards | no opens/shorts at >= 40 V; IR >= 500 Mohm at 500 V | IPC-D-356 CAD net list | p.79, p.282 |
| V25 | Thermal/mechanical reliability | Thermal cycling of the final assembly | cycles | failures | 0-100 C envelope plus ~10 C activity cycles | no opens | customer-run | p.183 |
| V26 | IC package screening | Test PCB exercising the IC as it will be used (all I/O active) | — | — | worst-case activity | serial links and parallel I/O meet margins together | Vol.1 Ch.38 method | p.210 |

## 5. Pitfalls, failure modes, review checklist

### 5a. The author's verdict on each rule of thumb / myth

| Myth / rule of thumb | Author's verdict | Source |
|---|---|---|
| "High speed" is defined by clock frequency | FALSE — rise time vs line length decides (1/4 of the edge's electrical length) | p.16-17 |
| Ferrite beads in IC power leads (PLL, serdes, "analog") | HARMFUL — raises PDS impedance; measured serdes eye worse with the bead; never used one in 30+ years | p.34-38, p.132-133, p.146 |
| Bead + capacitor + Vdd island under an ASIC | HARMFUL — removes plane capacitance; EMI and logic failures | p.36, p.146, Figs 3.16, 7.15 |
| Split ground planes to isolate noise / cut EMI | HARMFUL — can make a dipole antenna; never beneficial | p.12, p.123, p.146 |
| Separate analog and digital grounds | NO BENEFIT — often more EMI; tie the converter's grounds together under the part | p.135, p.211 |
| Don't route over power-plane splits | FALSE if each rail's PDS is low-Z (TDR and near-field show nothing); true only on 4-layer boards | p.123-125, p.129 |
| Layer change needs a ground via next to it / causes EMI | FALSE — TDR identical with and without ground vias | p.125-129 |
| Outer-layer or buried-microstrip traces radiate / are poor | FALSE — traces near planes neither radiate nor pick up | p.70, p.133, p.146 |
| Right-angle bends cause reflections, EMI or acid traps | FALSE (acid-trap myth comes from silkscreen-era cosmetic rejects) | p.103-104, p.146, p.211 |
| Cross-hatched planes needed for adhesion | OBSOLETE — oxide treatments solved it | p.51, p.215 |
| Non-functional pads needed | NO — remove them (short risk) | p.98, p.225 |
| Vias act as stubs | NO — they are small capacitors | p.101 |
| Vias radiate EMI / back-drill to reduce EMI | FALSE; "worse than elephant repellant" | p.102 |
| Back drilling as the general backplane fix | IMPRACTICAL when every link is equally critical; use smaller drills / SMT connectors | p.99 |
| 20H rule (recess Vdd plane) | FALSE — recessing made edge EMI worse | p.146-147, p.211 |
| lambda/20 ground-to-chassis stitching | FALSE — creates EMI | p.146-147, p.234 |
| Many logic-ground-to-chassis bonds eliminate EMI | FALSE — bond at one point only | p.142, p.146 |
| "Chassis ground" plane in backplanes | NO VALUE — cost only | p.134 |
| Green-wire (safety) ground contains EMI | FALSE — safety only | p.134, p.230 |
| Ground strips on plug-in card edges to card guides | NEVER — can worsen EMI | p.140 |
| Mount plug-in PCBs on "chassis ground" backing plates | NO BASIS — adds cost, can make EMI harder | p.147 |
| Plated board edges, edge via rows, guard rings for EMI | NO EFFECT on EMI (guard ring = ESD handling aid only) | p.146 |
| Bypass capacitors wired directly to IC power pins reduce EMI | INVALID | p.146, Fig 7.16 |
| The system clock is the main EMI source | FALSE — Vdd ripple from a weak PDS is | p.143 |
| EMI modelling tools predict product EMI | NOT FEASIBLE | p.147 |
| Guard traces | Not treated in Vol.2 (Vol.1 index p.108 only) | p.289 (index) |
| Side-by-side differential routing rejects crosstalk as common mode | FALSE — 10-11% differential coupling | p.156-157 |
| Tight in-pair coupling is beneficial | FALSE — narrower traces, more loss, impedance jumps when spread | p.157-159 |
| One member's return current flows in the other | FALSE — ~2%; the rest in the plane | p.159 |
| Very tight in-pair length matching (e.g., 100 mil for LVDS) | OVER-CONSTRAINT — tolerance = fastest edge length | p.159-160 |
| 100 ohm differential impedance is required | NO — two 50 ohm lines each terminated to Vref | p.154, p.216 |
| PPO (GETEK/Megtron) has much lower er | MISLEADING — compared at 75% vs 42% resin | p.115 |
| Buried-capacitance laminates are needed | NO — pair ordinary planes on thin prepreg | p.121-122 |
| Low-ESR (C0G) capacitors make better bypass capacitors | NO — antiresonance with plane capacitance | p.38 |
| Premium low-inductance capacitors pay off in thick boards | USUALLY NOT — via inductance dominates | p.30 |
| Auto-routers cannot route high-speed nets | FALSE — they fail only without rules; the skill is in the engineer | p.26 |
| Post-route SI analysis is the way to ensure SI | TOO LATE — do SI before schematic and before routing | p.26-27, p.174 |
| Passing DVT proves a design | FALSE — DVT can be worse than no testing | p.19, p.171 |
| Wider traces are the cure for loss | RARELY — > 5 mil almost never needed; change laminate | p.168 |
| Impedance equations are good enough | NO — use a 2D field solver | p.78 |
| Fab test coupons prove board impedance | NO — build test traces into the board | p.81, p.85 |
| Two traces between 1 mm BGA pins | UNRELIABLE — yield, CAF, hi-pot failures | p.94 |
| App-note rules must be followed ("we've always done it this way") | Demand proof and a test circuit; apply the five-question test | p.36-37, p.12 |
| IPC-2141 guidance | Unvalidated rules of thumb; use with caution | p.222 |

### 5b. Review checklist (one item per line)

- [ ] Every net whose length exceeds 1/4 of its driver edge's electrical length is in a terminated net class (p.16-17).
- [ ] No receiver sees more than Vdd + 0.3 V in worst-case simulation (p.15).
- [ ] Every net class has a technology-table row: impedance, layers, termination, stub length, width, spacing in class and to others, length tolerance (p.25).
- [ ] Parallel terminators are 1.1 x Z0 (55 ohm / 110 ohm), never below Z0 (p.129, p.169).
- [ ] Series terminator + driver impedance <= 0.9 x Z0 (p.130).
- [ ] At >= 2.4 Gb/s, differential terminations are split 50 + 50 ohm with ~10 pF to ground (p.154).
- [ ] No ferrite beads or plane islands in IC power leads (p.34-38).
- [ ] PDS target impedance is derived from ripple spec and worst-case dI, derated for ±15% capacitor tolerance (p.28, p.33).
- [ ] PDS model includes plane capacitance and mounting/via inductance (36 pH/mil) and was checked in SPICE/2D, not only a spreadsheet (p.30-33).
- [ ] No C0G/NP0 bulk decoupling; no Y5V; X7R where hot (p.38-39).
- [ ] DC-DC converter output impedance was measured under load, not taken from the data sheet (p.40-41).
- [ ] Plane capacitance meets V x Sum(C_lines)/dV with >= 50% margin and er(f) allowance (p.34, p.253).
- [ ] Each plane pair is adjacent across the thinnest safe prepreg (>= 3.4 mil; never single 106/1080) (p.74).
- [ ] Every signal layer is mated to its plane across a core, not prepreg (p.70).
- [ ] Same copper weight on both sides of every core; 1/2 oz everywhere unless DC drop demands more (p.50, p.71).
- [ ] First plane under each surface is ground; no back-to-back power planes (p.73).
- [ ] Outer layers carry no impedance-critical nets (p.73).
- [ ] Adjacent signal layers are routed orthogonally; backplanes use single-stripline layers (p.70-71).
- [ ] Stackup drawing names laminate type, construction, resin %, er, pressed thickness and copper for every opening (p.72-75).
- [ ] Impedance computed with a 2D field solver, er at ~2 GHz, solder mask included on outer layers (p.72, p.78).
- [ ] Stackup reviewed by 1-2 capable fabricators and frozen (p.72).
- [ ] Glass: 3313 (spread) for >= 2.5 Gb/s layers or accept weave-induced impedance ripple (p.111-115).
- [ ] Laminate Tg matches thickness and solder type (>= 170 C thick leaded; >= 220 C thick lead-free) (p.118).
- [ ] One laminate supplier per board (p.119).
- [ ] Drill chart specifies drill (not finished) size; press-fit drill = FHS + 4 mil (p.48, p.94).
- [ ] Pad stack uses the target fab's TIR; insulation >= 5 mil (4 mil GR-78); antipads never overlap (p.91-94, p.130).
- [ ] No two traces between 1 mm BGA pins; 0.8 mm BGAs use blind vias on layer 2 (p.94-95).
- [ ] Blind via diameter >= depth; via-in-pad vias filled or offset (p.60-61).
- [ ] Non-functional inner pads removed; thermal ties only on THT plane pins, 2 spokes (p.92, p.98, p.105).
- [ ] Thieving kept off controlled-impedance traces on layer 2 / n-1 (>= 0.100 in) (p.56, p.103).
- [ ] Surface finish is electroplated Ni/Au (Au 5-10 uin) or controlled ENIG; no tin finishes; OSP only single-sided (p.63-66).
- [ ] In-board impedance test traces on every controlled layer, plane-access pairs for every rail, stacking stripes (p.84-88).
- [ ] Impedance is read at the start of the TDR trace with the fab's tester edge rate (p.82).
- [ ] ICT access vias are placed along the net or at net ends, never as mid-net stubs (p.83-84).
- [ ] Dense double-sided boards have JTAG on every IC (p.84).
- [ ] Differential pairs: same impedance and length, both members over the same plane, spacing to aggressors from the noise budget (p.156-159).
- [ ] In-pair skew <= fastest edge length; <= 2.5% UI into UTP/connectors (60 mil at 2.4 Gb/s) (p.150, p.160, p.168).
- [ ] Channels above 3.125 Gb/s simulated with via capacitances, loss and packages; resonances resolved before routing (p.100).
- [ ] Laminate chosen by simulating the channel, not by rule of thumb (p.118, p.167).
- [ ] Signals crossing plane splits only where both rails meet their PDS target (not on 4-layer boards) (p.125, p.129).
- [ ] Plane splits 10 mil wide (>= 3 mil 1/2 oz, 6 mil 1 oz) (p.125).
- [ ] Logic ground bonded to the Faraday cage at exactly one point; faceplates not tied to logic ground (p.134, p.142).
- [ ] Every cable leaving the cage is shielded (shield bonded to the cage) or low-pass filtered with plane-built capacitors (p.133-139).
- [ ] Vent apertures <= 1/4 in; honeycombs/screens bonded all round (p.135).
- [ ] Power inputs have conducted-EMI filters at entry (on each module for -48 V backplanes) (p.140).
- [ ] Emission test margin >= 6 dB (p.145).
- [ ] IC packages screened: characterized PDS/ball map, or tested on a representative board with all I/O active (p.210).
- [ ] Package ball map: every signal ball next to a power/ground ball; checkerboard core power (p.200-202).
- [ ] Package capacitors' ESL small relative to the package-to-PCB inductance (p.204).
- [ ] Series-terminated signals probed at the receiver, not the driver (p.181).
- [ ] Bring-up firmware includes worst-case ripple stress patterns (bus 0 -> 1, standby -> full) (p.262).
- [ ] Library parts (footprints, IBIS, timing) checked by a second qualified person (p.22, p.172).
- [ ] Net-list compare (Gerber vs CAD) done before fabrication (p.46, p.103).
- [ ] Design archived in two copies, one off-site (p.27).

## 6. Standards referenced

| Standard | Edition / year | Clause / table cited | What it governs (per book) | Page |
|---|---|---|---|---|
| Bellcore (Telcordia) GR-78-CORE | — | — | Telco equipment: >= 4 mil between planes of different voltages; 4 mil minimum insulation | p.74, p.91 |
| FCC Rule (Part) 15 | — | Class A (commercial), Class B (residential) | US radiated/conducted emission limits | p.148, p.219 |
| EN 55022 (CISPR A / CISPR B) | — | Class A / B | EU emission limits | p.137-139, p.148, p.214 |
| EU RoHS directive | effective July 1, 2006 | — | Pb, Cd, Hg, Cr6+, PBB, PBDE limits; equipment <= 1000 VAC / 1500 VDC | p.118, p.183, p.229 |
| IPC-D-356 | — | — | Bare-board test net list in digital form (CAD net list with XY) | p.46, p.79, p.270, p.272 |
| IPC-2141 (replaces IPC-D-317) | — | — | High-speed PCB design guide (author: contains unvalidated rules of thumb) | p.222 |
| IPC-782 | — | — | SMT land patterns | p.222 |
| IPC-T-50 | — | — | Terms and definitions (E-glass formulation) | p.217, p.270 |
| IPC-CF-148 | — | — | Resin-coated metal (coated copper foil) | p.270, p.273 |
| IPC-MF-150 | — | — | Copper foil | p.270, p.273 |
| IPC-D-300 | — | — | Dimensions and tolerances, single/two-sided boards | p.270 |
| IPC-A-600 | — | Class 2 | Acceptability of printed boards | p.270, p.273 |
| IPC-A-610 | — | — | Acceptability of electronic assemblies | p.271 |
| IPC-TM-650 | — | 2.1.1 / 2.1.1.2 (microsection), 2.4.1 (tape adhesion), 2.4.6 (hot oil), 2.5.7 Cond. B (hi-pot) | Test methods | p.269-282 |
| IPC-SM-840 | — | Class T | Permanent solder mask; legend inks | p.271-272, p.280 |
| IPC-4101 | — | Class B thickness tolerance | Base materials for rigid/multilayer boards | p.271, p.273 |
| IPC-6011 | — | — | Generic performance spec for printed boards (default Class 2) | p.270-271 |
| IPC-6012 | — | Class 2 default; Class 3 annular ring; 3.3.1-3.3.9 cosmetics; 3.9.4 insulation resistance; bow/twist | Rigid board qualification and performance | p.270-282 |
| IPC-7711 / IPC-7721 | — | highest conformance level | Rework and repair | p.271, p.276 |
| ANSI/J-STD-003 | — | extended to 20 s exposure | Solderability test | p.271, p.276-277 |
| ASTM B-488-86 | 1986 | — | Gold plating testing | p.271 |
| QQ-N-290 | — | — | Nickel plating (edge fingers) | p.271, p.278 |
| QQ-S-571 | — | — | Tin/lead solder alloys | p.271 |
| UL 94 | — | V-0 | Flammability of plastics (board marking) | p.271, p.287 |
| UL 796 | — | — | Printed wiring board safety | p.271 |
| ANSI/ASQC Z1.4-1993 | 1993 | General Inspection Level I; S-1 | Sampling by attributes | p.269-271 |
| ISO 9002 | — | — | Fabricator quality system (minimum) | p.269 |
| ANSI/EIA-656 (IBIS), 656-A v4.0 | July 2002 (ref 34) | — | I/O buffer behavioural models | p.221, p.293 |
| IEEE 1149.1 (JTAG) | — | — | Boundary scan test | p.84, p.223 |
| IEEE 1149.6 | 2003, 2005 (refs 99-100) | — | AC-coupled boundary scan | p.295 |
| ANSI/TIA/EIA RS-644 (LVDS) | — | — | LVDS signalling (4 mA, 400 mV differential) | p.223, p.230 |
| TIA/EIA RS-232 / RS-422 | — | — | Serial interfaces (RS-232 < 20 kb/s, >= ±5 V swing) | p.230 |
| IEEE 1301.1 | — | — | 2 mm DIN connectors | p.217 |
| JEDEC package outlines | — | — | Standard BGA body sizes and ball counts | p.198, p.222 |
| MIL-STD-275 | — | — | Printed wiring for electronic equipment (US Navy) | p.224 |
| MIL-STD-55110 (MIL-PRF-55110) | — | — | Military printed wiring boards | p.225 |
| SPI-4.1 / SPI-4.2 (OIF) | — | — | 10 Gb/s framer interfaces (Tables 10.5/10.6) | p.180, p.195-196 |
| Ethernet 10Base2 / 100BaseT / XAUI / 10GE, Infiniband, PCI Express, SATA, USB, IEEE 1394 | — | — | Differential/shielded interfaces discussed (10Base2 shield isolation 1700 VDC) | p.136-140, p.152 |
| Motorola ECL System Design Handbook | 1974 | — | Historical transmission-line practice for ECL | p.13 |

## 7. Process / lifecycle guidance

### 7a. "Virtual prototyping" PCB design flow (Fig 2.2, p.20-27)

| Step | Activity | Deliverable | Exit criterion | Source |
|---|---|---|---|---|
| 1 Select parts | Choose ICs, connectors, capacitors, heat sinks, R-packs, laminate; obtain IBIS, worst-case timing, mechanical, logic, power (incl. current variation) and thermal data | Qualified parts list + model set | Every part has the models later steps need | p.20 |
| 2 Build part models | Library entries per tool (no linkage between tools) | Libraries | Checked by a second qualified person; IBIS validated against hardware where needed | p.20-22, p.172 |
| 3 Simulate net topologies | One member per net class with IBIS/SPICE, 50 ohm, rates, estimated lengths | Termination rules, voltage margins, rejected drivers | Every class passes worst case | p.22 |
| 4 Preliminary net list | Schematic (or backplane net list) | Net list | — | p.22 |
| 5 Power delivery needs | Load currents and spectra, target impedance, planes, capacitors | PDS design | Z(f) <= target (spreadsheet -> SPICE -> 2D) | p.22, Ch.3 |
| 6 Routing space | Signal-layer estimate (set by highest-pin-count IC) | Layer count | — | p.22 |
| 7 Stackup | Build stackup, assign planes (Ch.4.6 procedure, 7c) | Full stackup drawing | Reviewed by 1-2 capable fabs, then frozen | p.23, p.72 |
| 8 Preliminary routing rules | Technology table per net class | Route-control rules | — | p.23, Fig 2.3 |
| 9 Net list with classes | Class names attached to nets | Classed net list | — | p.23 |
| 10 Logic simulation/emulation | Debug hardware logic and software together on a model | Verified logic + firmware | Both error-free; hardware net list corrected from the model | p.23, p.173 |
| 11 Placement | Outline, keep-outs, parts placed | Placement | — | p.23 |
| 12 Length extraction | Manhattan lengths | Length file | — | p.23 |
| 13 Timing analysis | Silicon + wire delays | Timing report | Margins met | p.23-24 |
| 14 Thermal analysis | 3D model with airflow | Thermal map | No hot spots | p.24 |
| 15 Placement adjustment | Iterate 13-14 | Final placement | Timing and thermal met | p.24 |
| 16 Final routing rules | Rats-nest routability; simulate difficult multipoint nets | Updated technology table | Routable in the stackup | p.24 |
| 17 Route | Pre-route checks (clean net list, no mechanical interference, terminations present, drivers and loads); rule-driven auto-routing | Routed database | — | p.24-26 |
| 18 Post-route DRC | All nets routed, no shorts, length match, spacing, hole clearances; SI only on a few critical nets | DRC report | Zero violations | p.26-27 |
| 19 Release to fab | Gerbers, IPC-356 net list, fab drawing (stackup, notes, drill chart), drill files, mask/legend, BOM, pick-and-place | Fab + assembly package | Fab net-list compare passes | p.27, p.46 |
| 20 Archive | Two copies, one off-site | Archive | — | p.27 |
| Adoption | Add tools one at a time, transmission-line management and power delivery first | — | — | p.27 |

### 7b. Fabrication process (Fig 4.2, p.46-58) and its exit gates

| Stage | Activities | Exit criterion | Source |
|---|---|---|---|
| Front-end engineering | Data check, net-list compare, DRC, artwork compensation, drill files, test tooling, traveler, materials | Net lists agree; DRC clean; no unapproved changes | p.46-48, p.272 |
| Inner layers | Clean (chemical, not pumice, for thin Cu), image, DES, AOI, post-etch punch, oxide treatment | AOI clean; ±0.5 mil (1/2 oz) width control | p.49-51 |
| Lamination | Layup on pins, press, controlled cool-down; rigid steel separators | Flat, correct thickness | p.51-53 |
| Drill and plate | X-ray drill optimization, drill, desmear, electroless seed, pattern plate (RPP for high aspect ratio), thieving | TP <= ±5 mil; barrel >= 1 mil | p.53-56, p.277 |
| Outer layers | Strip-etch-strip, LPI mask, legend, finish, depanel | Finish per spec | p.57-58 |
| Test | Shorts/opens vs CAD net list, impedance, cross-sections | 100% e-test; impedance ±10% | p.47, p.79-82, p.282 |

### 7c. Stackup design procedure (p.78-79)

1. Determine signal layers needed. 2. Add planes as partners for every signal layer. 3. Arrange signal/plane pairs. 4. Mate planes for the plane-capacitance goal. 5. Set signal height above plane for the crosstalk goal. 6. Set trace widths for impedance. 7. Set the signal-pair and near-surface openings for total thickness. 8. Check manufacturability with a good fabricator, then freeze.

### 7d. Test and verification stages

| Stage | Activity | Exit criterion | Source |
|---|---|---|---|
| Part selection | Screen IC packages (characterization data or a representative test board) | Package PDS and I/O adequate | p.210 |
| Part selection | Challenge app-note ferrite beads/rules with the five questions; ask for the vendor test circuit | Every retained rule proven | p.12, p.37 |
| Bare board at fab | Net-list e-test (CAD net list), impedance on built-in test traces, cross-section | Lot passes App 3 criteria | p.79-82, p.282 |
| OEM receiving inspection | Impedance on test traces; stacking-stripe audit; plane capacitance per rail | Matches design | p.83, p.87-88 |
| Assembly test | ICT via bottom-side vias; JTAG where no probe access | No shorts/opens; functional | p.83-84 |
| Power bring-up | (1) bare-board plane C, (2) Z(f) with capacitors only, (3) worst-case ripple under stress firmware | Z(f) and ripple within target | p.253-262 |
| EMI | Design containment from the start; pre-scan; formal FCC/CISPR test with >= 6 dB margin; compliance specialist on the team | Pass with margin | p.132, p.145, p.148 |
| Reliability | Thermal-cycle the final assembly | No failures | p.183 |
| Field/repair | Reuse the JTAG tests at the depot | Single test suite | p.84 |
| Fab qualification | AML; first article (Level I sampling, full report); production lots (S-1) with reports | Written approval before further shipments | p.269-270 |

## 8. Coverage log

**Source file:** `_RIGHT_THE_FIRST_TIME_A_PRACTICAL_HANDBOOK_ON_HIGH_SPEED_PCB.txt`, 19,722 lines, 935,943 bytes (max line length 5,466 chars). Read in full, in order, in 38 sequential chunks of <= 24 KB each. Chunk boundaries: 1-162, 163-218 (re-read as 163-190 and 191-218 after an output overflow), 219-704, 705-1000, 1001-1545, 1546-1886, 1887-2174, 2175-2387, 2388-2589, 2590-2831, 2832-3091, 3092-3919, 3920-4176, 4177-5638, 5639-6230, 6231-6471, 6472-6748, 6749-6976, 6977-7176, 7177-7461, 7462-7653, 7654-7969, 7970-8146, 8147-8353, 8354-8572, 8573-9131, 9132-9785, 9786-11384, 11385-11503, 11504-11649, 11650-11810, 11811-11930, 11931-12289, 12290-12823, 12824-13107, 13108-13825, 13826-16095, 16096-19722.

**Line map (body headings):** front matter, TOC and figure list 1-198; Ch.1 199-822; Ch.2 823-1333; Ch.3 1334-2040; Ch.4 2041-6273; Ch.5 6274-6766; Ch.6 6767-7050; Ch.7 7051-7649; Ch.8 7650-8241; Ch.9 8242-8385; Ch.10 8386-11376; Glossary 11377-12016; App.1 12017-12278; App.2 12279-12467; App.3 12468-13413; App.4 13414-15057; App.5 15058-15137; App.6 and App.7 15138-16975; App.8 16976-17006; App.9 17007-17120; App.10 17121-18192; App.11 18193-19722.

**Mined for rules:** Chapters 1-10, the Glossary and Appendices 1, 2, 3, 6, 7, 8, 9, 10. 338 rules (RITCHEY-001 to RITCHEY-338, no duplicate ids), 47 tables (T1-T47), 56 mechanizable checks, 26 verification procedures.

**Read but not mined (by design):** App.4 (index to Vol.1) and App.11 (index to Vol.2) are index pages. App.5 (references) was used only to resolve reference numbers cited in rules (refs 10, 13, 14, 21, 35, 66, 67, 84, 89, 94). Historical narrative in Ch.1 (relays to CMOS) and Ch.10.2 was reduced to Table T1 and packaging facts. No chapters were skipped.

**Extraction limitations:**
- Figures are not in the text. Graph-based values (Figs 1.8, 1.9, 3.5, 3.19, 3.21, 3.27, 5.1, 5.14, 8.7, 8.21, 10.18, 10.34, 10.35) come from captions and prose anchors and are tagged "graph" / conf medium.
- Nelco (p.241-248) and Rogers (p.249-252) material pages in Appendix 1 are image-only; only the p.236 summary survives. Isola FR406/FR408/IS410/IS620 tables were fully transcribed (T38-T41).
- Table 5.2 prints 12 material names but only 11 Tg and 11 property rows, so the middle rows are ambiguous (flagged in T16 and RITCHEY-157).
- Table 10.7's bottom half is scrambled; it was reconstructed symmetrically and checked against the printed 1.130 mm total.
- The Fig 2.3 technology table columns are interleaved; one trailing "200" could not be assigned to a class.
- Table 1.1 metric and length columns are internally inconsistent; the inch values (6 in/ns) are used.
- The buried-microstrip impedance equation (Fig 4.46) is OCR-garbled; only the surface-microstrip and stripline forms were transcribed.
- Several book metric conversions are off by 10x (e.g., "1.27 mm" for a 5 mil TIR, "3.05 mm" for a 12 mil drill, "6.6 mm" for 26 mil); the mil values were used throughout.
- The text calls "layer 2 and 7" the buried-microstrip layers of the 10-layer stackup, apparently a typo for 2 and 9; RITCHEY-078 is reconstructed from the P/L sequence and the thickness-adjustment text.
- The Appendix 10 colour legend is lost; RITCHEY-338's numeric bands are inferred (conf medium).
- The Appendix 6 drill chart columns were interleaved in extraction; they were re-paired and every pair verified by decimal-to-size consistency.

**Internal inconsistencies recorded (not resolved by the book):**
- Fab-note glass styles and resin content (106/1080/2113/2116/2313/3313, >= 50%) vs App.3 (106/1080/2116/3313, >= 55%).
- Trace-width tolerance: Fig 4.78 (±0.5 / ±1.0 mil) vs App.3 (lesser of ±20% or ±1 / ±2 mil).
- Gold over nickel: 5-10 uin (Ch.4) vs 6-15 uin (Fig 4.78) vs 5-15 uin (App.3).
- N4000-13SI Tg: 245 C (Table 5.2 printed order) vs 210 C (App.1).
- PCMCIA plane capacitance after fill: 4000 pF (Ch.3) vs 4100 pF (Ch.7).
- 26 mil x 250 mil press-fit via: ~1.5 pF (Ch.4) vs ~2 pF (Ch.8).
- Microvia: <= 8 mil (Ch.4) vs < 8 mil (Glossary).
- 1 oz foil: 36 um (Ch.4) vs 35 um (Glossary).

**Not available:** Volume 1, which Vol.2 cites for via inductance (36 pH/mil, Eq 35.1), pad inductances, plane DC drop and stubs. Those values are recorded only as quoted in Vol.2.

**Page citations:** printed "Page NNN" markers; text preceding a marker belongs to that page.
