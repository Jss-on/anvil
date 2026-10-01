# IPC standards excerpts (IPC-2221C, IPC-6012F, J-STD-001E, IPC-A-610J) + End-to-End Hardware Design Library guides — Anvil rulebook

BOOKTAG: IPC (rule-id prefixes IPC2221-, IPC6012-, JSTD001-, A610-, LIB-)

> Scope note. The four IPC files are TOC/front-matter excerpts, not full standards. Every numeric limit below is one that is actually printed in the excerpt. Where only a clause title is present the row says **value not in excerpt** — Anvil must cite the clause/table id and fetch the value from the licensed standard, never infer it.

## 0. Citation

| ref | IEEE-style reference | covered by this extraction | NOT read (reason) |
|---|---|---|---|
| [1] | IPC, *IPC-2221C: Generic Standard on Printed Board Design*, IPC-2221/2222 Task Group (D-31b), Rigid Printed Board Committee (D-30), IPC International, Inc., Bannockburn, IL, Dec. 2023. Supersedes IPC-2221B (Nov. 2012). | Front matter; complete Table of Contents (pp. v–xiii) incl. Figures and Tables lists; §1 Scope, §1.1 Purpose, §1.2 Documentation Hierarchy, §1.3 Presentation, §1.3.1 Units (p. 1). | §1.4–§12 body text and Appendices A–C — not present in excerpt (file ends at p. 1). |
| [2] | IPC, *IPC-6012F: Qualification and Performance Specification for Rigid Printed Boards*, Rigid Printed Board Performance Specifications Task Group (D-33a), IPC International, Bannockburn, IL, Sept. 2023. Supersedes IPC-6012E (Mar. 2020). | Front matter; complete TOC (pp. v–vii); Figures list (p. viii); Tables list (p. ix); §1 Scope through §1.7 (pp. 1–5) incl. Table 1-1 Technology Adders and Table 1-2 Default Requirements, Figs 1-1..1-3. | §2–§5 body (pp. 6–52), Tables 3-1..3-21, 4-1..4-4 — not in excerpt. |
| [3] | IPC, *IPC J-STD-001E-2010: Requirements for Soldered Electrical and Electronic Assemblies*, J-STD-001 Task Group (5-22a), 5-22aCN, 5-22aND, Assembly and Joining Processes Committees (5-20, 5-20CN), IPC, Bannockburn, IL, Apr. 2010. Supersedes J-STD-001D (Feb. 2005), C (Mar. 2000), B (Oct. 1996), A (Apr. 1992). **Superseded**: ref [6] states the J revision is current. | Complete TOC (pp. vii–x) incl. Figures and Tables lists; §1.1 Scope, §1.2 Purpose, §1.3 Classification, §1.4 Units, §1.4.1 Verification of Dimensions (p. 1). | §1.5 onward — not in excerpt. |
| [4] | IPC, *IPC-A-610J: Acceptability of Electronic Assemblies*, Rev. J, IPC-A-610 Task Group (7-31b), 7-31b-EU, 7-31b-CN, Product Assurance Committee (7-30), IPC International, Bannockburn, IL, Mar. 2024. Supersedes IPC-A-610H (Sept. 2020). ISBN 978-1-63816-163-9. | Front matter and committee lists; complete TOC (pp. xiii–xxv) incl. Tables list and Appendix A TOC; body pages 8-46 (§8.3.4.4–8.3.4.5), 9-5..9-7 (§9.3), 10-55 (§10.8.2); Index (Index-1..3). | All other body pages (chapters 1–13 text, tables) — not in excerpt. |
| [5] | *End-to-End Electronics Hardware Design Library* (curated reading guide, 26 pp., no author printed; cites 2024 editions and targets "an actual 2026 product"). | Entire document (executive summary; selection criteria; prioritized top-20 table; detailed core library tables; category coverage matrix; learning sequence flowchart; product-gate table; footnoted URLs). | — |
| [6] | *End-to-End Electronics Hardware Design Library for Product Development* (curated reading guide, 21 pp., no author printed; cites IEC 61000-4-2:2025 and 2026 editions). | Entire document (ranking method; scope/level codes; must-have/recommended/optional tables with ISBNs; standards and living references tables; topic-by-topic ranking; gaps; 13-step reading path; minimum purchase order). | — |

Page citation convention: IPC-2221C/6012F/J-STD-001E use flat page numbers (p.NN); IPC-A-610J uses chapter-page numbers (p.8-46). Guide [5]/[6] cite printed page numbers (p.NN) as they appear as stray lines in the text.

## 1. Design rules

Domain vocabulary per brief. `verify by` ∈ {calc, sim, measure, inspect, review}. conf: high = explicit in text; medium = derived/only clause title present; low = qualitative guidance quantified.

### 1.1 IPC-2221C (design)

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| IPC2221-001 | process | Use IPC-2221C only together with the sectional standard for the board technology: IPC-2222 rigid organic, IPC-2223 flex/rigid-flex, IPC-2225 organic MCM-L, IPC-2226 HDI, IPC-2228 RF/microwave. IPC-2220 is the family ordering number. | n/a | board technology class | every design; more than one sectional standard may apply | review | [1] §1.1–1.2 p.1 | high |
| IPC2221-002 | process | Do not cite IPC-2221C as a performance specification for finished boards or as an acceptance document for assemblies; use IPC-6012 (rigid board performance) and J-STD-001 / IPC-A-610 (assembly). | n/a | drawing notes | fabrication and assembly drawings | review | [1] §1.1 p.1; [6] p.14 | high |
| IPC2221-003 | dfm | Dimensions ≥ 0.1 mm are expressed in mm [in]; dimensions < 0.1 mm in µm [µin]; metric is the controlling unit. | threshold 0.1 mm [0.0039 in] | all dimensions | design documentation | inspect | [1] §1.3, §1.3.1 p.1 | high |
| IPC2221-004 | requirements | Classify the product before selecting rules: printed board type (§1.6.1), performance classification (§1.6.2), producibility level (§1.6.3). | value not in excerpt (titles only) | product intent | all designs | review | [1] §1.6–1.6.3 pp.2–3 | medium |
| IPC2221-005 | requirements | Complete the Printed Board Design/Performance Tradeoff Checklist (Table 3-1) and resolve order of precedence (§3.1.1) and end-product performance requirements (§3.1.2) before layout. | value not in excerpt | requirements | all designs | review | [1] Table 3-1 p.6; §3.1.1–3.1.2 p.8 | medium |
| IPC2221-006 | dfm | Perform density evaluation (§3.4) and feasibility density evaluation (§3.7.2) using component grid areas (Table 3-2), package size vs I/O count (Fig 3-1) and usable-area calculation (Fig 3-5). | value not in excerpt | package count, I/O, board area | before placement | calc | [1] §3.4 p.9, §3.7.2 p.18, Table 3-2 p.19, Fig 3-5 p.19, Fig 3-6 p.21 | medium |
| IPC2221-007 | test | Design bare-board test in: HiPot (§3.6.1.2.1), impedance considerations (§3.6.1.2.2), test data/source data (§3.6.1.3). | value not in excerpt | netlist, impedance nets | bare board test | review | [1] §3.6.1 pp.10–13 | medium |
| IPC2221-008 | test | Provide assembly testability: test-land free areas for parts and other intrusions (Fig 3-2) and for tall parts (Fig 3-3); probing test lands (Fig 3-4); boundary scan (§3.6.3); in-circuit test fixtures and electrical considerations (§3.6.5.1–3.6.5.2); Appendix C testability checklist. | value not in excerpt (figure-driven) | test points, part heights | ICT / functional test | review | [1] §3.6.2–3.6.5 pp.13–17, Figs 3-2..3-4 p.17, App. C p.156 | medium |
| IPC2221-009 | test | Functional-test design items: test connectors (§3.6.4.1), initialization/synchronization (§3.6.4.2), long counter chains (§3.6.4.3), self diagnostics (§3.6.4.4), physical test concerns (§3.6.4.5). | n/a | | functional test | review | [1] §3.6.4 pp.14–15 | medium |
| IPC2221-010 | connectors | Keep connector uniformity and uniform power-distribution arrangement / signal levels on connectors (§3.6.6.1–3.6.6.2). | n/a | connector pinouts | multi-board systems | review | [1] §3.6.6 p.18 | medium |
| IPC2221-011 | materials | Select materials for structural strength, electrical, environmental and physical properties (§4.1.1–4.1.4); prepreg (§4.2.1); adhesives (epoxies, silicone elastomers, acrylics, polyurethanes, specialized acrylate, other §4.2.2.x); electrically conductive (§4.2.4) and thermally conductive/electrically insulating adhesives (§4.2.5). | n/a | environment, loads | material selection | review | [1] §4.1–4.2 pp.21–24 | medium |
| IPC2221-012 | materials | Laminate choices: high-Tg laminates (§4.3.1), color pigmentation (§4.3.2), dielectric thickness/spacing (§4.3.3), thermally conductive laminates (§4.3.4), minimum base material (§4.3.5). | value not in excerpt | Tg, thickness | stackup | review | [1] §4.3 pp.24–25 | medium |
| IPC2221-013 | fab | Final finish, plating and coating requirements per Table 4-1; surface and hole copper plating minimums per Table 4-2 (buried vias > 2 layers, through-holes, blind vias), Table 4-3 (microvias blind and buried), Table 4-4 (buried via cores, 2 layers). | value not in excerpt | hole type, class | plated holes | inspect | [1] §4.4 p.25, Tables 4-1..4-4 pp.26–27 | medium |
| IPC2221-014 | materials | Surface finish selection per Table 4-5 with advantage/limitation tables: ENIG (Table 4-7), ENIG/EG (4-8), ENEPIG (4-9), immersion silver (4-10), immersion tin (4-11), OSP (4-12); gold plating uses Table 4-6; tin/lead and tin plating §4.4.9; HASL tin-lead and Pb-free §4.4.10.1.x. | value not in excerpt | assembly process | finish selection | review | [1] §4.4.4–4.4.10 pp.28–33, Tables 4-5..4-12 | medium |
| IPC2221-015 | materials | Copper foil/film minimum recommendations per Table 4-13; resin-coated copper foil with single or two resin layers (§4.4.12.2.1.1–2); metal core substrates Table 4-14. | value not in excerpt | layer function | foil selection | review | [1] §4.4.12 pp.34–35 | medium |
| IPC2221-016 | components | Embedded (buried) resistors, capacitors, inductors are design options (§4.5.1–4.5.3). | n/a | | embedded passives | review | [1] §4.5 p.35 | medium |
| IPC2221-017 | dfm | Solder mask: adhesion and coverage (§4.6.1.1); mask clearances and dams per Table 4-15 typical minimum. | value not in excerpt | pad geometry | solder mask design | inspect | [1] §4.6.1 pp.35–36, Table 4-15 p.36 | medium |
| IPC2221-018 | materials | Conformal coating type and thickness range per Table 4-16; functionality Table 4-17; tarnish protective coating §4.6.3. | value not in excerpt | environment | coated assemblies | inspect | [1] §4.6.2 pp.36–37 | medium |
| IPC2221-019 | dfm | Marking and legends per §4.7; ESD considerations §4.7.1. | n/a | | all | review | [1] §4.7–4.7.1 pp.37–38 | medium |
| IPC2221-020 | mechanical | Fabrication assumptions and considerations per Table 5-1; board size standardization (Fig 5-1); PC-card form-factor substrate dimensions Table 5-2. | value not in excerpt | form factor | board outline | review | [1] §5.1–5.2.3 pp.38–40 | medium |
| IPC2221-021 | mechanical | Bow and twist (§5.2.4; PC-card §5.2.4.1); structural strength (§5.2.5); constraining-core composite boards (§5.2.6, Figs 5-2, 5-3A/B); vibration design (§5.2.7). | value not in excerpt | thickness, layup | mechanical | review | [1] §5.2.4–5.2.7 pp.41–42 | medium |
| IPC2221-022 | dfm | Typical assembly equipment limits per Table 5-3; tooling rails for PC-card boards (§5.3.4); component clearance for automatic insertion (Fig 7-1). | value not in excerpt | board size | assembly | review | [1] §5.3 p.43, Table 5-3 p.43, Fig 7-1 p.69 | medium |
| IPC2221-023 | dfm | Dimension with positional (true-position) tolerancing and a datum reference frame (Fig 5-4 advantage of positional over bilateral; Fig 5-5 datum reference frame; Figs 5-6..5-10 examples); datum features for palletization (§5.4.3.1). | n/a | drawing | fab drawing | review | [1] §5.4 pp.44–48 | medium |
| IPC2221-024 | dfm | Fiducial clearance requirements per Fig 5-11; panelization/assembly array (Fig 5-12); breakaway tabs (§5.7.1); X-out fiducials (Fig 5-14). | value not in excerpt (figure) | | panelized boards | inspect | [1] §5.6–5.7 pp.49–51 | medium |
| IPC2221-025 | dfm | Board thickness tolerance (§5.5); connector key slot location/tolerance (Fig 5-13); board edge tolerancing (Fig 8-13); lead-in chamfer (Fig 8-14). | value not in excerpt | | edge connectors | inspect | [1] §5.5 p.50, Figs 5-13, 8-13, 8-14 | medium |
| IPC2221-026 | fab | Plated edges: perimeter edge plating (§5.8.1), edge plating for round parts (§5.8.2), anchor points (§5.8.3); edge plating clearance (Fig 5-15); common nets anchored to board edge preferred (Fig 5-16). | value not in excerpt | | edge-plated boards | inspect | [1] §5.8 pp.51–52 | medium |
| IPC2221-027 | pdn | Power distribution considerations (§6.1.2), voltage/ground distribution concepts (Fig 6-1), circuit distribution (Fig 6-3), single reference edge routing (Fig 6-2); digital vs analog circuit-type considerations (§6.1.3.1–6.1.3.2). | n/a | | all | review | [1] §6.1 pp.52–55 | medium |
| IPC2221-028 | current-carrying | Conductor material requirement for surge current per §6.2.1 with example algorithm calculation §6.2.1.1. | value not in excerpt | surge I, t | surge-carrying conductors | calc | [1] §6.2 pp.55–56 | medium |
| IPC2221-029 | clearance | Electrical clearance is evaluated three ways: line-of-sight through air/vacuum without insulation (§6.3.1), dielectric spacing layer-to-layer through the dielectric (§6.3.2, DWV §6.3.2.1, measured per Fig 6-4), creepage along surface contours (§6.3.3). | value not in excerpt | V, category | all | inspect | [1] §6.3–6.3.3 pp.56–57 | medium |
| IPC2221-030 | clearance | Minimum spacing per Table 6-1 "Electrical Conductor Spacing" is selected by category: B1 internal conductors; B2 external uncoated, sea level to 3050 m [10,007 ft]; B3 external uncoated, over 3050 m or in vacuum; B4 external with solder mask (any elevation); B5 external coated (any elevation or vacuum); A6 external component lead coated (any elevation or vacuum); A7 external component lead uncoated, sea level to 3050 m; A8 external component leads without conformal coating, over 3050 m or vacuum. | altitude break = 3050 m [10,007 ft]; spacing values not in excerpt | net voltage, layer, coating, altitude | every conductor pair | inspect (DRC) | [1] §6.3.3.1–6.3.3.1.8 pp.58–59, Table 6-1 p.58 | high (categories) / n.a. (values) |
| IPC2221-031 | reliability | Consider conductive anodic filament (CAF) growth (§6.3.4) and comparative tracking index material groups (Table 6-2, §6.3.5) when setting spacing. | value not in excerpt | laminate CTI | high-voltage / humid | review | [1] §6.3.4–6.3.5 pp.59–60 | medium |
| IPC2221-032 | transmission-line | Impedance control structures: microstrip (§6.4.1), embedded microstrip (§6.4.2), stripline (§6.4.3), asymmetric stripline (§6.4.4); document impedance per §6.4.5 with tolerance examples Table 6-4; example plane sequences for six-layer board Table 6-3; transmission-line construction Fig 6-5. | value not in excerpt | er, h, w, t | controlled-impedance nets | review | [1] §6.4 pp.60–63 | medium |
| IPC2221-033 | transmission-line | Capacitance vs conductor width and dielectric thickness for microstrip (Fig 6-6) and vs width and spacing for striplines (Fig 6-7); inductance considerations §6.4.7; single conductor crossover Fig 6-8. | graph, values not in excerpt | w, h | | calc | [1] §6.4.6–6.4.7 pp.63–65 | medium |
| IPC2221-034 | thermal | Thermal design: cooling mechanisms conduction/radiation/convection/altitude (§7.1.x); material type effects Table 7-1; emissivity ratings Table 7-2; enclosed vs ventilated housing (§7.2.1.x); heatsink assembly preferences Table 7-3; CTE comparison Fig 7-2; thermal design reliability §7.4. | value not in excerpt | P, ambient, altitude | all | calc | [1] §7 pp.65–72 | medium |
| IPC2221-035 | reliability | Comparative reliability matrix for component lead/termination attachment per Table 7-4. | value not in excerpt | package type | attachment choice | review | [1] Table 7-4 p.70 | medium |
| IPC2221-036 | assembly | Placement rules: automatic assembly board size / mixed assemblies / surface mounting (§8.1.1.x); component orientation for boundaries and wave solder (Fig 8-1); accessibility, design envelope, body centering (Fig 8-2), flush mounting over conductive areas (§8.1.7, Figs 8-3, 8-4), clearances (§8.1.8). | value not in excerpt | | placement | inspect | [1] §8.1 pp.73–76 | medium |
| IPC2221-037 | mechanical | Physical support for shock/vibration: clamp-mounted (Fig 8-5), adhesive-bonded (Fig 8-6), filleting vs bonding (§8.1.9.1.1, Fig 8-7), feet/standoffs (Fig 8-8); Class 3 high-reliability applications §8.1.9.2. | n/a | mass, environment | heavy parts, Class 3 | review | [1] §8.1.9 pp.76–78 | medium |
| IPC2221-038 | thermal | Component heat dissipation (§8.1.10, Fig 8-9) and stress relief (§8.1.11); lead bends Fig 8-10; typical lead configurations Fig 8-11. | n/a | | leaded parts | review | [1] §8.1.10–8.1.11 pp.78–79 | medium |
| IPC2221-039 | assembly | Attachment requirements: through-hole (§8.2.1), surface mount (§8.2.2), mixed (§8.2.3), soldering considerations and thermal stress methodologies (§8.2.4–8.2.4.1). | n/a | | | review | [1] §8.2 pp.79–80 | medium |
| IPC2221-040 | connectors | Connector types and rules: one-part, dual in-line, edge board, two-part multiple, two-part discrete-contact, edge board adapter (§8.2.5.1–8.2.5.6); keying (Fig 8-12); fastening hardware §8.2.6; stiffeners §8.2.7. | n/a | | connectors | review | [1] §8.2.5–8.2.7 pp.81–83 | medium |
| IPC2221-041 | assembly | Lands for flattened round leads (§8.2.8, §9.1.5, Fig 8-17); solder terminals mechanical/electrical mounting (§8.2.9.1–8.2.9.2, Figs 8-18, 8-19); eyelets §8.2.10; jumper wires §8.2.11.1; bus bar §8.2.13; flexible cable §8.2.14. | value not in excerpt | | | review | [1] §8.2.8–8.2.14 pp.84–86 | medium |
| IPC2221-042 | assembly | Through-hole lead rules: straight, unclinched, clinched, partially clinched (Fig 8-20); DIP/SIP (Fig 8-21 lead bends); solder in lead bend radius (Fig 8-22); axial (§8.3.1.6); radial two-lead mounting (Figs 8-23, 8-24); meniscus clearance (Fig 8-25); TO-can (Fig 8-26); perpendicular mounting (Fig 8-27); flat-packs (Figs 8-28, 8-29); metal power packages with compliant / noncompliant leads and resilient spacers (Figs 8-30..8-32). | value not in excerpt (figures with mm [in]) | | THT parts | inspect | [1] §8.3 pp.87–90 | medium |
| IPC2221-043 | assembly | SMT rules: leaded SMT (§8.4.1), flat-pack (§8.4.2, Fig 8-33), ribbon lead (§8.4.3, Fig 8-35), round lead (§8.4.4, Fig 8-34), heel mounting (Fig 8-36), sockets (§8.4.5); fine-pitch peripherals §8.5; bare die wire bond / flip chip / chip scale §8.6; TAB §8.7; grid array (§8.8, Figs 8-39..8-41 BGA/CGA/LGA); no-lead QFN/SON/PQFN (§8.9, Figs 8-42..8-44); compliant pin §8.10. | n/a | package | SMT | review | [1] §8.4–8.10 pp.90–94 | medium |
| IPC2221-044 | via | Lands with holes: land requirements (§9.1.1, modified land shapes Fig 9-1); minimum annular ring per Table 9-1, external (§9.1.2.1, Fig 9-2) and internal (§9.1.2.2, Fig 9-3). | value not in excerpt | hole dia, land dia, class | all PTH | inspect (DRC) | [1] §9.1–9.1.2 pp.94–96, Table 9-1 p.96 | medium |
| IPC2221-045 | via | Thermal relief in conductor planes (§9.1.3, Fig 9-4); clearance area in planes (§9.1.4, Fig 9-5) with pad-to-plane clearance per Table 9-2; small-pitch clearance §9.1.4.1. | value not in excerpt | | plane layers | inspect (DRC) | [1] §9.1.3–9.1.4 pp.96–98, Table 9-2 p.97 | medium |
| IPC2221-046 | dfm | Conductive pattern feature location tolerance (diameter true position) per Table 9-3; minimum hole location tolerance DTP per Table 9-4; NPTH/PTH tolerances §9.2.5.x. | value not in excerpt | producibility level | | inspect | [1] §9.1.7 p.98, Table 9-3 p.98, §9.2.5 pp.101–102, Table 9-4 p.102 | medium |
| IPC2221-047 | via | Holes: unsupported tooling/mounting (§9.2.1.x); supported plated / component / via holes (§9.2.2.1–9.2.2.3); specifying hole sizes for vias (§9.2.2.4); blind (§9.2.2.5), buried (§9.2.2.6), thermal vias (§9.2.2.7); compliant-pin press-fit systems (§9.2.2.8). | n/a | | | review | [1] §9.2 pp.99–101 | medium |
| IPC2221-048 | via | Through-hole diameter minimum/maximum and aspect ratio per Table 9-5; aspect ratio §9.2.8; spacing of adjacent holes §9.2.7; hole pattern variation §9.2.4; etchback §9.2.9. | value not in excerpt | board thickness, drill | all PTH | calc | [1] §9.2.7–9.2.9 p.102, Table 9-5 p.103 | medium |
| IPC2221-049 | via | Via protection requirements (§9.3.1) and via fill (§9.3.2); back-drilling guidance (§9.4). | n/a | | via-in-pad, HDI, high-speed | review | [1] §9.3–9.4 pp.102–104 | medium |
| IPC2221-050 | current-carrying | Conductor width and thickness per §10.1.1 (etched conductor characteristics Fig 10-1); internal layer foil thickness after processing Table 10-1; external conductor thickness after plating Table 10-2. | value not in excerpt | I, ΔT, Cu weight | all conductors | calc | [1] §10.1.1 pp.104–105, Tables 10-1, 10-2 p.105 | medium |
| IPC2221-051 | dfm | Conductor routing (§10.1.3): beef-up / neck-down (Fig 10-2), conductor optimization between lands (Fig 10-3); conductor spacing §10.1.4; electrical clearance §10.1.2 (refers back to §6.3). | n/a | | routing | inspect | [1] §10.1.2–10.1.4 pp.107–108 | medium |
| IPC2221-052 | fab | Balanced metallization (§10.1.5) and plating thieves (§10.1.6); large conductive areas §10.3 with cross-hatched large layers and isothermal conductors (Fig 10-4). | n/a | copper balance | outer layers, planes | review | [1] §10.1.5–10.3 pp.108–109 | medium |
| IPC2221-053 | dfm | Land characteristics: manufacturing allowances (§10.2.1), SMT lands (§10.2.2), test points (§10.2.3), orientation symbols (§10.2.4), offset lands (§10.2.5). | n/a | | | review | [1] §10.2 p.108 | medium |
| IPC2221-054 | process | Documentation: special tooling §11.1; layout viewing/accuracy/notes/automated techniques §11.2.x; deviation requirements §11.3; phototool / artwork master files / film base / solder mask phototools §11.4.x; design/fabrication sequence flow chart Fig 11-1; gang vs pocket solder mask windows Figs 11-3, 11-4. | n/a | | release package | review | [1] §11 pp.109–112 | medium |
| IPC2221-055 | test | Conformance test coupons: Appendix A coupons (AB/R plated-hole thermal stress/rework/registration; propagated B; E moisture and insulation resistance; S hole solderability; W SMT solderability; D interconnect resistance and continuity; G solder mask adhesion; H surface insulation resistance; P peel strength/plating adhesion; K; Z controlled impedance) with requirements Table 12-1, quantity/location §12.3.1, identification §12.3.2; Appendix B legacy coupons (A, B, A/B, E, S, M, D, G, H, C, F, R, N, X) Table 12-2; coupon X bending flexibility (flex); process control coupon §12.4.13. | value not in excerpt | class, technology | every fab panel | inspect | [1] §12 pp.112–119, App. A p.121, App. B p.139 | medium |
| IPC2221-056 | via | Definitions: microvia (§1.5.1, Fig 1-1), back-drilling (§1.5.2, Fig 1-2), stub (§1.5.3). Numeric limits printed in IPC-6012F §1.4.4 (see IPC6012-022). | see IPC6012-022 | | | review | [1] §1.5.1–1.5.3 p.2 | medium |

### 1.2 IPC-6012F (rigid board qualification and performance)

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| IPC6012-001 | fab | Performance Class (1, 2 or 3 per IPC-6011) shall be specified in the procurement documentation; if not selected, **default = Class 2**. | Class 2 default | class | all rigid boards | review | [2] §1.3.1, §1.3.3, Table 1-2 pp.1–2 | high |
| IPC6012-002 | fab | Requirements deviating from the heritage classes are AABUS; sector deviations via addenda IPC-6012XS (space), IPC-6012XM (medical), IPC-6012XA (automotive), applicable only when specified in procurement documentation; base-standard amendments published after an addendum do not extend to the addendum. | n/a | sector | space/medical/automotive | review | [2] §1.3.1.1–1.3.1.4 p.1 | high |
| IPC6012-003 | fab | Declare printed board Type: 1 single-sided; 2 double-sided; 3 multilayer without blind/buried vias; 4 multilayer with blind and/or buried vias (may include microvias); 5 multilayer metal core without blind/buried vias; 6 multilayer metal core with blind/buried vias (may include microvias). Type 1 has no PTH; Types 2–6 have PTH. | n/a | stackup | all | review | [2] §1.3.2 p.1 | high |
| IPC6012-004 | fab | Add technology adder codes as applicable: HDI (build-up, stacked/staggered microvias), VP (via protection), WBP (wire-bondable pads), MB (metal base), AMC (active metal core), NAMC (non-active metal core), HF (external heat frame), EP (embedded passives per IPC-6017), VIP-C (via-in-pad conductive fill), VIP-N (via-in-pad nonconductive fill). | n/a | features | | review | [2] Table 1-1 p.2 | high |
| IPC6012-005 | fab | Optional selection identifier: Quality spec / Spec / Type / Plating Process / Surface Finish / Selective Finish ("-" if none) / Class / Technology Adders. Example: `IPC-6011/6012/3/1/S/-/3/HDI/EP`. | string format | | drawing note | review | [2] §1.3.3.2 p.3, p.2 example | high |
| IPC6012-006 | fab | Procurement documentation shall contain enough information to fabricate the board per IPC-2611 and IPC-2614; all AABUS selections must be documented. | n/a | | | review | [2] §1.3.3, §1.3.3.1 p.2 | high |
| IPC6012-007 | test | Procurement documentation shall specify the thermal stress test method: §3.6.1.1 IPC-TM-650 Method 2.6.8 (for wave, selective, hand solder); §3.6.1.2 Method 2.6.27 at 230 °C (conventional eutectic SnPb reflow); §3.6.1.3 Method 2.6.27 at 260 °C (Pb-free reflow). **Default = Method 2.6.8, Condition A.** | 230 °C / 260 °C; default 2.6.8 Cond. A | assembly process | all | measure | [2] §1.3.3 p.2, Table 1-2 p.3, TOC §3.6.1.x p.24 | high |
| IPC6012-008 | materials | Default laminate = epoxy-glass laminate per §3.2.1. | n/a | | when not specified | review | [2] Table 1-2 p.2 | high |
| IPC6012-009 | materials | Default surface finish: **X1 per Table 3-3** for designs (drawings) initially released on or before 01 Oct 2023 (Note 1); **ENIG2 per Table 3-3** for designs initially released on or after 01 Oct 2023 (Note 2). | date break 2023-10-01 | drawing release date | when not specified | review | [2] Table 1-2 p.2 and Notes p.3 | high |
| IPC6012-010 | fab | Default minimum starting foil weight: 1/2 oz for all internal and external layers, except Type 1 which starts with 1 oz; plated HDI layers: 1/4 oz for all layers (internal or external). | 1/2 oz (≈17 µm); Type 1: 1 oz; HDI plated layers: 1/4 oz | layer type | when not specified | review | [2] Table 1-2 p.2 | high (oz values) |
| IPC6012-011 | materials | Default copper foil type = electrodeposited per §3.2.4. | n/a | | | review | [2] Table 1-2 p.2 | high |
| IPC6012-012 | fab | Default hole diameter tolerance, plated component holes: ± 100 µm [3,937 µin]. | ±100 µm | drill list | when not specified | measure | [2] Table 1-2 p.2 | high |
| IPC6012-013 | fab | Default hole diameter tolerance, plated via-only holes: + 80 µm [3,150 µin], minus: no requirement (via may be totally or partially plugged). | +80 µm / −(no req.) | drill list | when not specified | measure | [2] Table 1-2 p.2 | high |
| IPC6012-014 | fab | Default hole diameter tolerance, non-plated holes: ± 80 µm [3,150 µin]. | ±80 µm | drill list | when not specified | measure | [2] Table 1-2 p.2 | high |
| IPC6012-015 | fab | Default conductor width tolerance = Class 2 requirements per §3.5.1; default conductor spacing tolerance = Class 2 per §3.5.2 (numeric values not in excerpt). | value not in excerpt | | when not specified | measure | [2] Table 1-2 p.3 | high (default) / n.a. (values) |
| IPC6012-016 | stackup | Default minimum dielectric separation = 65 µm [2,560 µin] per §3.6.2.18 (§3.6.2.18.1 Minimum Dielectric Spacing, Fig 3-47). | ≥ 65 µm | layer-to-layer dielectric | when not specified | measure (microsection) | [2] Table 1-2 p.3 | high |
| IPC6012-017 | fab | Default marking ink: contrasting color, nonconductive per §3.3.5. | n/a | | | inspect | [2] Table 1-2 p.3 | high |
| IPC6012-018 | fab | Solder mask: not applied unless specified (§1.3.4.3); when specified without class, **Class T of IPC-SM-840** per §3.7. | IPC-SM-840 Class T | | | review | [2] Table 1-2 p.3 | high |
| IPC6012-019 | solder | Default SnPb solder coating = Sn63/Pb37 per §3.2.7.3.1; Pb-free solder coating per §3.2.7.3.2. | Sn63/Pb37 | | HASL/solder coat | review | [2] Table 1-2 p.3 | high |
| IPC6012-020 | test | Default solderability test per §3.3.6: J-STD-003 Category 2 for SnPb, Category A for Pb-free. | J-STD-003 Cat. 2 / Cat. A | finish | | measure | [2] Table 1-2 p.3 | high |
| IPC6012-021 | test | Test voltage, isolation resistance and continuity resistance per IPC-9252 by default. | per IPC-9252 | | electrical test | measure | [2] Table 1-2 p.3 | high |
| IPC6012-022 | via | Microvia definition: blind structure (as plated) with maximum aspect ratio 1:1 (X/Y per Fig 1-3), terminating on or penetrating a target land, with total depth X ≤ 0.25 mm [0.00984 in] measured from capture-land foil to target land. Note 3: X < 0.25 mm and aspect ratio < 1:1. | X ≤ 0.25 mm; X/Y ≤ 1:1 (X = depth, Y = hole diameter at capture land) | depth, diameter | HDI | calc | [2] §1.4.4 p.5, Fig 1-3 | high |
| IPC6012-023 | via | Shallow back-drill: external layer is pierced and approximately 0.05–0.127 mm [0.002–0.005 in] of barrel drilled out to prevent shorting of the plated via to any component/chassis directly above or below. | 0.05–0.127 mm | | back-drilled vias | inspect | [2] §1.4.1 p.4, Fig 1-2 | high |
| IPC6012-024 | via | Back-drill geometry vocabulary (Fig 1-1): 1 primary drilled hole dia; 2 back-drill hole dia; 3 distance between nearest conductive feature and back-drill hole; 4 target layer (must-not-cut layer); 5 stub length (excluding target layer copper thickness); 6 back-drill depth. Stub = maximum remaining hole-wall plating from target layer to back-drill termination; back-drill depth = distance from dielectric surface on penetration side to nearest remaining copper stub. | n/a | | signal-integrity back-drill | inspect (microsection §3.6.2.20) | [2] §1.4.1–1.4.3 pp.4–5 | high |
| IPC6012-025 | fab | Plating process code (single digit): 1 acid copper electroplating only; 2 pyrophosphate copper only; 3 acid and/or pyrophosphate copper; 4 additive/electroless copper; 5 electrodeposited nickel underplate with acid and/or pyrophosphate copper. | code 1–5 | | drawing | review | [2] §1.3.4.2 pp.3–4 | high |
| IPC6012-026 | materials | Surface finish designators (thickness per Table 3-3 unless specified): S solder coating; T electrodeposited SnPb fused; X either S or T; TLU SnPb unfused; b1 Pb-free solder coating; G gold electroplate edge connectors; GS gold for soldered areas; GWB-1 gold for ultrasonic wire bond; GWB-2 gold for thermosonic wire bond; N nickel edge connectors; NB nickel barrier to Cu-Sn diffusion; OSP; HT OSP; ENIG; ENEPIG; DIG direct immersion gold; NBEG nickel barrier/electroless gold; IAg; ISn; C bare copper (AABUS); SMOBC solder mask over bare copper; SM solder mask over non-melting metal; SM-LPI; SM-DF; SM-TM (§3.2.8); Y other (§3.2.7.11). Coating thickness may be exempted in Table 3-3 for SnPb plate or solder coating. | value not in excerpt (Table 3-3) | | finish spec | review | [2] §1.3.4.3 p.4 | high (codes) |
| IPC6012-027 | dfm | Units: dimensions ≥ 1.0 mm [0.0394 in] in mm/in; < 1.0 mm in µm/µin. Note the break differs from IPC-2221C (0.1 mm). | threshold 1.0 mm | | documentation | inspect | [2] §1.6 p.5 | high |
| IPC6012-028 | process | "Shall" is mandatory; deviation may be considered only with sufficient justifying data. When photographs/illustrations conflict with text, the written text takes precedence. | n/a | | | review | [2] §1.5 p.5 | high |
| IPC6012-029 | process | Design data shall be protected as specified in procurement documentation; fabricator must have internal protection policies regardless; optional protocol §3.10.14. | n/a | | | review | [2] §1.7 p.5 | high |
| IPC6012-030 | fab | Use IPC-A-600 figures/photographs as visualization companion for acceptable/nonconforming conditions. | n/a | | | inspect | [2] §1.2.1 p.1 | high |
| IPC6012-031 | fab | Scope covers: single/double-sided with or without PTH; multilayer with PTH with or without buried/blind vias/microvias; embedded active/passive circuitry with distributive capacitive planes; metal core with/without external heat frame. Requirements apply to the finished product. | n/a | | | review | [2] §1.2 p.1 | high |
| IPC6012-032 | fab | Visual examination acceptance items (values not in excerpt): edges §3.3.1; laminate imperfections — measling, crazing, delamination/blistering, foreign inclusions, weave exposure, mechanically induced disrupted fibers, scratches/dents/tool marks, surface voids, color variations in bond enhancement, pink ring (§3.3.2.1–3.3.2.10); plating/coating voids in hole per Table 3-4; lifted lands §3.3.4; marking §3.3.5.x; solderability §3.3.6; plating adhesion §3.3.7; edge contact gold-to-solder junction gap Table 3-5; back-drilled holes §3.3.9; cavities §3.3.10 with voids Table 3-6; workmanship §3.3.11. | value not in excerpt | | incoming inspection | inspect | [2] §3.3 pp.13–18, Tables 3-4..3-6 | medium |
| IPC6012-033 | fab | Dimensional requirements: hole size, hole pattern accuracy and pattern feature accuracy §3.4.1; annular ring and breakout (external) §3.4.2 with **minimum annular ring per Table 3-7** (p.19), measurement Fig 3-2, breakout of 90° and 180° Fig 3-3; bow and twist §3.4.3. | value not in excerpt | | | measure | [2] §3.4 pp.18–21, Table 3-7 p.19 | medium |
| IPC6012-034 | fab | Conductor definition: width and thickness §3.5.1; spacing §3.5.2; imperfections — width reduction (Fig 3-4), thickness reduction (§3.5.3.1–3.5.3.2); nicks/pinholes in ground or voltage planes §3.5.4.1; solderable SMT lands — rectangular (Fig 3-6) and round/BGA (Fig 3-7); wire bond pad §3.5.4.3; board edge connector lands (Fig 3-8, edge pull back Fig 3-10); dewetting (Fig 3-9) / nonwetting; surface finish coverage; SnPb under solder mask §3.5.4.7.2; cap plating of filled holes §3.5.4.8; copper-filled microvias §3.5.4.9; nonfunctional lands §3.5.4.10. | value not in excerpt | | | measure | [2] §3.5 pp.21–23 | medium |
| IPC6012-035 | reliability | Structural integrity via thermal stress (§3.6.1) then microsection (§3.6.2): plating integrity §3.6.2.1 with **plated hole integrity after stress per Table 3-8** (p.26); copper plating voids §3.6.2.2; laminate voids / cracks / delamination §3.6.2.3–3.6.2.5 (thermal zones Fig 3-16); etchback (evidence when specified, copper penetration) §3.6.2.6.x (Figs 3-17, 3-18); smear removal §3.6.2.7; negative etchback per **Table 3-9** (Fig 3-19); annular ring/breakout in microsection external/internal §3.6.2.9.x (Figs 3-20..3-24, microvia target-land breakout can reduce dielectric spacing); lifted lands §3.6.2.10; nail heading §3.6.2.21. | value not in excerpt | class | qualification & lot acceptance | measure (microsection) | [2] §3.6 pp.23–31, Tables 3-8, 3-9 | medium |
| IPC6012-036 | fab | Hole copper plating minimums (§3.6.2.11, measurement locations Fig 3-25): **Table 3-10** surface and hole copper for buried vias > 2 layers, through-holes and blind vias; **Table 3-11** microvias (blind and buried); **Table 3-12** buried cores (2 layers) — all p.32. Copper wrap plating §3.6.2.11.1 (Figs 3-26..3-30; wrap removed by sanding/planarization/etching = not acceptable). | value not in excerpt (class columns in tables) | class, hole type | all PTH | measure (microsection) | [2] §3.6.2.11 pp.31–34 | medium |
| IPC6012-037 | via | Filled holes: cap plating requirements per **Table 3-13** (p.33; cap thickness Fig 3-31, bump Fig 3-32, dimple Fig 3-33, cap plating voids Fig 3-34, via fill between cap layers Figs 3-35, 3-36); plated copper-filled vias (through, blind, buried, microvia) §3.6.2.11.3 with acceptable/nonconforming voiding Figs 3-37..3-40; depression and protrusion in copper-filled microvias per **Table 3-14** (p.35); material fill of via structures §3.6.2.19 (Figs 3-48, 3-49 void at hole-wall interface); hole fill insulation material §3.2.11; via protection §3.2.13. | value not in excerpt | VIP-C/VIP-N, VP adder | via-in-pad / filled vias | measure (microsection) | [2] §3.6.2.11.2–3.6.2.11.3, §3.6.2.19 pp.33–40 | medium |
| IPC6012-038 | via | Microvia target-land contact dimension per **Table 3-15** (laser drilled) and **Table 3-16** (mechanically drilled), p.37 (Figs 3-41, 3-42); target land piercing §3.6.2.13 (Fig 3-43); performance-based testing for microvia structures §3.10.15. | value not in excerpt | drill method | HDI | measure | [2] §3.6.2.12–3.6.2.13 pp.36–37 | medium |
| IPC6012-039 | fab | Minimum internal layer copper foil thickness after processing per **Table 3-17** (plated internal layers §3.6.2.14.1); minimum surface conductor thickness per **Table 3-18** (external, after plating), both p.38; overhang §3.6.2.16 (Fig 3-45). | value not in excerpt | starting foil weight | all layers | measure | [2] §3.6.2.14–3.6.2.16 pp.37–39 | medium |
| IPC6012-040 | stackup | Metal cores §3.6.2.17 (metal core to plated hole spacing Fig 3-46; Table 3-1 metal planes/cores p.10; horizontal microsection §3.10.9); dielectric spacing §3.6.2.18 with minimum §3.6.2.18.1 (Fig 3-47); back-drilled holes microsection evaluation §3.6.2.20. | see IPC6012-016 for 65 µm default | | metal core, all | measure | [2] §3.6.2.17–3.6.2.20 pp.39–40 | medium |
| IPC6012-041 | fab | Solder mask: coverage §3.7.1; cure and adhesion §3.7.2 with **Table 3-19 Solder Mask Adhesion** (p.41); thickness §3.7.3. | value not in excerpt | | masked boards | inspect | [2] §3.7 pp.40–42 | medium |
| IPC6012-042 | test | Electrical requirements: dielectric withstanding voltage §3.8.1 per **Table 3-20** (p.42); electrical continuity and isolation resistance §3.8.2 with **Table 3-21 Insulation Resistance**; circuit/plated-hole shorts to metal substrate §3.8.3; moisture and insulation resistance (MIR) §3.8.4 and DWV after MIR §3.8.4.1. | value not in excerpt | class | qualification / acceptance | measure | [2] §3.8 p.42 | medium |
| IPC6012-043 | fab | Cleanliness: prior to solder mask §3.9.1; after solder mask/solder/alternative coating §3.9.2; inner layers after oxide treatment prior to lamination §3.9.3. | value not in excerpt | | | measure | [2] §3.9 p.43 | medium |
| IPC6012-044 | reliability | Special requirements when specified: outgassing, fungus resistance, vibration, mechanical shock, impedance testing (§3.10.5), CTE, thermal shock, surface insulation resistance as received, rework simulation (TH §3.10.10.1, SMT §3.10.10.2), bond strength of unsupported hole land, destructive physical analysis, peel strength (foil laminated construction only), CAF migration §3.10.16, wire bond pad surface roughness §3.10.17. | value not in excerpt | | when specified | measure | [2] §3.10 pp.43–44 | medium |
| IPC6012-045 | fab | Repair (circuit repairs §3.11.1) and rework §3.12 are separately governed. | n/a | | | review | [2] §3.11–3.12 p.45 | medium |
| IPC6012-046 | test | Quality assurance: qualification §4.1.1 with **Table 4-1 Qualification Test Coupons** (p.45); sample test coupons §4.1.2; acceptance tests §4.2 with **C=0 zero-acceptance-number sampling plan per lot size Table 4-2** (p.47) and **Table 4-3 Acceptance Testing and Frequency** (p.47); referee tests §4.2.2; periodic quality conformance testing §4.3 with **Table 4-4** (p.52) and coupon selection §4.3.1. | value not in excerpt | lot size | every lot | inspect | [2] §4 pp.45–52 | medium |
| IPC6012-047 | materials | Materials clauses: laminates and bonding §3.2.1; external bonding §3.2.2; other dielectrics §3.2.3; metal foils §3.2.4 (resistive metal §3.2.4.1); metal planes/cores §3.2.5 Table 3-1; electroless / electrodeposited / fully additive copper §3.2.6.x; finishes §3.2.7.1–3.2.7.11 with solder bath contaminant limits **Table 3-2** (p.11) and **Table 3-3 Final Finish, Plating and Coating Requirements** (p.12); polymer coating §3.2.8; fusing fluids/fluxes §3.2.9; marking inks §3.2.10; external heatsink planes §3.2.12; embedded passive materials §3.2.14. | value not in excerpt | | | review | [2] §3.2 pp.9–13 | medium |
| IPC6012-048 | process | Ordering data §5.1 lists what the purchaser must state; superseded specifications §5.2. | n/a | | | review | [2] §5 p.52 | medium |

### 1.3 J-STD-001E (soldering process requirements; superseded by rev. J)

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| JSTD001-001 | requirements | The **user** defines the product Class and states it in the procurement documentation package. Class 1 General Electronic Products (major requirement is function); Class 2 Dedicated Service (continued performance and extended life required, uninterrupted service desired but not critical, end-use environment typically would not cause failures); Class 3 High Performance (continued high performance or performance-on-demand critical, downtime cannot be tolerated, environment may be uncommonly harsh, must function when required, e.g., life support). | Class ∈ {1,2,3} | intended use | all assemblies | review | [3] §1.3 p.1 | high |
| JSTD001-002 | test | All specified limits are absolute limits as defined in ASTM E29; actual measurement of part mounting and fillet dimensions and percentage determination are not required except for referee purposes. | absolute limits (ASTM E29) | | conformance decisions | inspect | [3] §1.4.1 p.1 | high |
| JSTD001-003 | process | Units: SI with imperial in brackets; mm is the main dimensional unit, µm when mm is too cumbersome; temperature in °C; weight in grams. | n/a | | documentation | inspect | [3] §1.4 p.1 | high |
| JSTD001-004 | process | The standard relies on process-control methodology for consistent quality (§1.2); process control requirements §11.3, opportunities determination §11.3.1, statistical process control §11.4; process verification inspection §11.2.1, visual §11.2.2, sampling §11.2.3. | n/a | | manufacturing | review | [3] §1.2 p.1; TOC §11 p.48–49 | high |
| JSTD001-005 | process | Use J-STD-001 with IPC-HDBK-001, IPC-A-610 and IPC-HDBK-610 for tutorial context; J-STD-001 does not exclude any placement, flux or solder application procedure. | n/a | | | review | [3] §1.1–1.2 p.1 | high |
| JSTD001-006 | assembly | Butt/I connections are **not permitted for Class 3 products** (clause title). | Class 3 prohibition | lead style | SMT butt/I terminations | inspect | [3] TOC §7.5.10 p.33, Table 7-10 | high (title) |
| JSTD001-007 | solder | Solder bath contaminant maximum limits per Table 3-1 (values not in excerpt); solder purity maintenance §3.2.2; lead-free solder §3.2.1. | value not in excerpt | bath assay | wave/dip soldering | measure | [3] TOC §3.2, Table 3-1 p.7 | medium |
| JSTD001-008 | assembly | Facility controls: ESD §4.1; environmental controls §4.2.1; temperature and humidity §4.2.2; lighting §4.2.3; field assembly operations §4.2.4. | value not in excerpt | | | inspect | [3] TOC §4.1–4.2 pp.8–9 | medium |
| JSTD001-009 | assembly | Solderability §4.3 and maintenance §4.4; gold removal §4.5.1 and other finish removal §4.5.2; thermal protection §4.6; rework of nonsolderable parts §4.7; presoldering cleanliness §4.8. | value not in excerpt | | | inspect | [3] TOC §4.3–4.8 p.9–10 | medium |
| JSTD001-010 | assembly | Part mounting: stress relief §4.9.1; hole obstruction §4.10 (Fig 4-1); metal-cased component isolation §4.11; adhesive coverage limits §4.12; stacking of components §4.13; connectors and contact areas §4.14; preheating, controlled cooling, drying/degassing, holding devices §4.15.x. | value not in excerpt | | | inspect | [3] TOC §4.9–4.15 pp.10–11 | medium |
| JSTD001-011 | solder | Solder connection requirements: acceptable wetting angles (Fig 4-2); machine soldering controls and solder bath §4.16.x; reflow §4.17 and intrusive soldering (paste-in-hole) §4.17.1; exposed surfaces, connection defects, partially visible/hidden connections §4.18.x; heat-shrinkable soldering devices §4.19. | value not in excerpt (figure) | | | inspect | [3] TOC §4.16–4.19 pp.11–12 | medium |
| JSTD001-012 | cables | Wire and terminals: insulation damage §5.1.1; strand damage per Table 5-1; tinning of stranded wire §5.1.3; bifurcated/turret/slotted terminal installation §5.3 (flange damage Fig 5-1, flare angles Fig 5-2, mounting mechanical/electrical Figs 5-3, 5-4); terminal soldering requirements Table 5-2; wire placement Tables 5-3 (turret/straight pin), 5-4 (AWG 30 and smaller wrap), 5-5 (bifurcated side route), 5-6 (staking side route straight-through), 5-7 (bifurcated bottom route), 5-8 (hook), 5-9 (pierced/perforated), 5-10 (solder wire to post); insulation clearance Fig 5-5; service loop Fig 5-6; stress relief Fig 5-7. | value not in excerpt | AWG, terminal type | wired assemblies | inspect | [3] TOC §5 pp.12–19 | medium |
| JSTD001-013 | assembly | Through-hole: lead forming §6.1.1 with lead bend radius per Table 6-1 (Fig 6-1); lead deformation limits §6.1.2; lead trimming §6.1.4 (Fig 6-2); interfacial connections §6.1.5; coating meniscus in solder §6.1.6; protrusion of leads in supported holes Table 6-2 and unsupported holes Table 6-3; minimum acceptable conditions for supported holes Table 6-4 (vertical fill example Fig 6-3) and unsupported holes Table 6-5. | value not in excerpt | lead dia, hole type | THT | inspect | [3] TOC §6 pp.20–22 | medium |
| JSTD001-014 | assembly | SMT lead forming minimum lead length Table 7-1 (Figs 7-1, 7-2); lead deformation limits, flat-pack parallelism, lead bends, flattened leads, DIPs, parts not configured for SMT §7.1.x; leaded component body clearance §7.2, axial §7.2.1; butt-lead configured parts §7.3; hold-down of SMT leads §7.4. | value not in excerpt | | SMT | inspect | [3] TOC §7.1–7.4 pp.23–24 | medium |
| JSTD001-015 | assembly | SMT solder joint dimensional criteria by termination style: Table 7-2 surface mount components (general); 7-3 bottom-only terminations; 7-4 rectangular/square end chip 1, 3 or 5 side; 7-5 cylindrical end cap; 7-6 castellated; 7-7 flat gull wing; 7-8 round/coined gull wing; 7-9 J leads; 7-10 butt/I; 7-11 flat lug; 7-12 tall profile bottom-only; 7-13 inward-formed L-shaped ribbon; 7-14 BGA collapsing balls; 7-15 BGA noncollapsing balls; 7-16 column grid array; 7-17 BTC; 7-18 bottom thermal plane (D-Pak); 7-19 flattened post. Misaligned components §7.5.1; BGA solder ball spacing Fig 7-14. | value not in excerpt | package | SMT | inspect | [3] TOC §7.5 pp.24–41 | medium |
| JSTD001-016 | assembly | Cleaning: cleanliness exemptions §8.1; ultrasonic cleaning §8.2; post-solder cleanliness — particulate §8.3.1, flux residues and ionic/organic contaminants §8.3.2, cleanliness designator §8.3.3 (surfaces Table 8-1, testing designators Table 8-2), cleaning option §8.3.4, test for cleanliness §8.3.5–8.3.6. | value not in excerpt | | | measure | [3] TOC §8 pp.42–43 | medium |
| JSTD001-017 | fab | PCB damage acceptance after assembly: blistering/delamination, weave exposure/cut fibers, haloing, land separation, land/conductor reduction in size, flex delamination/damage, burns, solder on gold contacts, measles (§9.1.1–9.1.10); marking §9.2; bow and twist (warpage) §9.3. | value not in excerpt | | assembled boards | inspect | [3] TOC §9 pp.43–44 | medium |
| JSTD001-018 | assembly | Conformal coating application/performance/inspection/rework §10.1.x with coating thickness per Table 10-1 (p.45); encapsulation §10.2.x; staking (adhesive) §10.3.x. | value not in excerpt | coating type | coated assemblies | measure | [3] TOC §10 pp.45–47 | medium |
| JSTD001-019 | test | Magnification aid applications for solder connections per Table 11-1 and other inspections Table 11-2; hardware defects requiring disposition §11.1. | value not in excerpt | land width | inspection | inspect | [3] TOC §11 p.48 | medium |
| JSTD001-020 | clearance | Minimum electrical clearance / electrical conductor spacing per Appendix B (p.53); definitions: electrical clearance §1.8.3, high voltage §1.8.4. | value not in excerpt | V | assemblies | inspect | [3] TOC App. B p.53, §1.8.3–1.8.4 p.3 | medium |
| JSTD001-021 | process | Requirements flowdown §1.9; personnel proficiency §1.10; acceptance requirements §1.11; general assembly requirements §1.12; health and safety §1.13.1; procedures for specialized technologies §1.13.2; order of precedence and conflict §1.7.x; design and fabrication specifications referenced in Table 1-1. | n/a | | | review | [3] TOC §1.7–1.13 pp.3–5 | medium |
| JSTD001-022 | process | Materials, components and equipment: flux §3.3 and application §3.3.1; solder paste §3.4; preforms §3.5; adhesives §3.6; chemical strippers §3.7; component and seal damage §3.8.1; coating meniscus §3.8.2; soldering tools and equipment §3.9 with Appendix A guidelines (p.51). | n/a | | | review | [3] TOC §3 pp.6–8, App. A p.51 | medium |
| JSTD001-023 | process | Rework §12.1, repair §12.2, post-rework/repair cleaning §12.3. | n/a | | | review | [3] TOC §12 p.49 | medium |
| JSTD001-024 | process | Cite the current revision on drawings: ref [6] identifies **J-STD-001J** (with IPC-A-610J) as the issued current revision; this excerpt is rev. E (2010). | rev J current | | contract manufacturing quality plan | review | [6] p.11, p.14; [3] cover | high |

### 1.4 IPC-A-610J (assembly acceptability)

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| A610-001 | requirements | Acceptance is judged per Class 1, 2, 3 (§1.3) with criteria categories: Acceptable (§1.5.1.1), Defect (§1.5.1.2) with Disposition (§1.5.1.2.1), Process Indicator (§1.5.1.3), Conditions Not Specified (§1.5.1.4), Specialized Designs (§1.5.1.5), Should (§1.5.1.6); process control methodologies §1.6. | Class ∈ {1,2,3} | class | all assemblies | inspect | [4] TOC §1.3–1.6 pp.1-2..1-3 | high (structure) |
| A610-002 | assembly | Castellated termination minimum side joint length (D): **Acceptable Class 1,2,3** — solder extends from the back of the castellation onto the land at or beyond the edge of the component; **Acceptable Class 1** — wetted fillet evident; **Defect Class 1,2,3** — wetted fillet not evident, or solder does not extend from the back of the castellation onto the land at or beyond the component edge. | D ≥ (castellation back → component edge) | fillet extent | castellated terminations (LCC, modules) | inspect | [4] §8.3.4.4 p.8-46, Fig 8-71 | high |
| A610-003 | assembly | Castellated termination maximum fillet height (E): Acceptable Class 1,2,3 — fillet may extend past the top of the castellation provided it does not extend onto the component body. | E ≤ top of castellation, or higher if not on body | | castellated | inspect | [4] §8.3.4.5 p.8-46, Figs 8-72, 8-73 | high |
| A610-004 | components | Leaded/leadless device body damage — **Acceptable Class 1 / Process Indicator Class 2,3**: indentations or chip-outs on plastic body do not enter lead seal or lid seals and do not expose an internal functional element (Figs 9-12, 9-13, 9-14). | n/a | | plastic packages | inspect | [4] §9.3 p.9-5 | high |
| A610-005 | components | Acceptable Class 1 / PI Class 2,3: component damage has not removed required identification. | n/a | | all | inspect | [4] §9.3 p.9-5 | high |
| A610-006 | components | Acceptable Class 1 / PI Class 2,3: insulation/sleeving damage only if the damaged area shows no evidence of increasing (rounded edges, no cracks, sharp corners or brittle heat-damaged material; Figs 9-13, 9-14) and the exposed conductive surface provides no danger of shorting to adjacent components or circuitry (Fig 9-15). | n/a | | insulated parts | inspect | [4] §9.3 p.9-5 | high |
| A610-007 | components | Defect Class 1,2,3: chip-out or crack that enters into the seal (Fig 9-16: 1 chip enters seal, 2 exposed lead, 3 seal). | n/a | | | inspect | [4] §9.3 p.9-6 | high |
| A610-008 | components | Defect Class 1,2,3: cracks leading from the chip-out on a ceramic body component (Fig 9-16). | n/a | | ceramic packages | inspect | [4] §9.3 p.9-6 | high |
| A610-009 | components | Defect Class 1,2,3: chip or crack exposing the component substrate or active element, or affecting hermeticity, integrity, form, fit, function (Fig 9-17). | n/a | | | inspect | [4] §9.3 p.9-6 | high |
| A610-010 | components | Defect Class 1,2,3: chips or cracks in glass body beyond the part specification (Fig 9-18); cracked or damaged glass bead beyond part specification. | per part spec | part spec | glass-body diodes etc. | inspect | [4] §9.3 p.9-6 | high |
| A610-011 | components | Defect Class 1,2,3: required identification missing due to component damage. | n/a | | | inspect | [4] §9.3 p.9-6 | high |
| A610-012 | components | Defect Class 1,2,3: insulating coating damaged to the extent that the internal functional element is exposed or the component shape is deformed. | n/a | | | inspect | [4] §9.3 p.9-6 | high |
| A610-013 | components | Defect Class 1,2,3: damaged area shows evidence of increasing (cracks, sharp corners, brittle material from heat; Fig 9-19). | n/a | | | inspect | [4] §9.3 p.9-6 | high |
| A610-014 | components | Defect Class 1,2,3: damage permits potential shorting to adjacent components or circuitry. | n/a | | | inspect | [4] §9.3 p.9-6 | high |
| A610-015 | components | Defect Class 1,2,3: flaking, peeling, or blistering of plating. | n/a | | | inspect | [4] §9.3 p.9-6 | high |
| A610-016 | components | Defect Class 1,2,3: burned, charred components (charred surface has black / dark-brown appearance due to excessive heat; Fig 9-20). | n/a | | | inspect | [4] §9.3 p.9-6 | high |
| A610-017 | components | Defect Class 1,2,3: dents, scratches in the component body that affect form, fit, function or exceed component manufacturer's specifications (Fig 9-21). | per mfr spec | | | inspect | [4] §9.3 p.9-6 | high |
| A610-018 | components | Defect Class 1,2,3: cracks in shield material (Fig 9-22). | n/a | | shielded parts | inspect | [4] §9.3 p.9-6 | high |
| A610-019 | components | Defect Class 1,2,3: component body delaminates from substrate (Fig 9-23). | n/a | | | inspect | [4] §9.3 p.9-6 | high |
| A610-020 | assembly | Conformal coating coverage inspection method: unaided eye (see §1.13.2 Magnification Aids); coatings with fluorescent pigment may be examined with blacklight; white light may aid; outer-layer conductors covered by solder mask are **not** considered exposed conductors. | n/a | coating type | coated assemblies | inspect | [4] §10.8.2 p.10-55 | high |
| A610-021 | assembly | Conformal coating coverage Acceptable Class 1,2,3: coating is cured; coating only in areas where required; orange peel accepted (Fig 10-157); entrapped material does not violate minimum electrical clearance between components, lands or conductive surfaces; no discoloration or loss of transparency. | MEC not violated | | coated assemblies | inspect | [4] §10.8.2 p.10-55 | high |
| A610-022 | assembly | Conformal coating Process Indicator Class 1,2,3: bubbles, voids or loss of adhesion that do not bridge or expose conductive surfaces; bubbles bridging noncommon leads or conductors not covered with solder mask which have been qualified and documented as benign. | n/a | | coated assemblies | inspect | [4] §10.8.2 p.10-55 | high |
| A610-023 | test | Inspection magnification is selected by land width per Table 1-2 (p.1-9); magnification aid applications for wires and soldered conductors Table 1-3 and other Table 1-4 (p.1-10); lighting §1.13.1. | value not in excerpt | land width | inspection setup | inspect | [4] TOC §1.13, Tables 1-2..1-4 | medium |
| A610-024 | clearance | Minimum Electrical Clearance (MEC) §1.12 (p.1-7); electrical clearance definition §1.8.8 (TOC; the printed Index cites §1.8.5 and §4.1.1 — use TOC numbering); hardware installation electrical clearance §4.1.1; high voltage §12; insulation clearance §6.2.2. | value not in excerpt | V | all | inspect | [4] TOC §1.12, §1.8.8, §4.1.1, §12; Index-1 | medium |
| A610-025 | assembly | SMT joint acceptance uses lettered features per termination family: A side overhang, B end/toe overhang, C end joint width, D side joint length, E maximum (heel) fillet height, F minimum (heel) fillet height, G solder thickness, J end overlap, Q minimum side joint height (round/coined gull wing). Dimensional criteria tables: 8-1 chip bottom-only; 8-2 rectangular/square-end chip 1,2,3 or 5 side; 8-2A center/lateral termination; 8-3 cylindrical end cap; 8-3A its center/lateral; 8-4 castellated; 8-5 flat gull wing; 8-6 round/coined gull wing; 8-7 J leads; 8-8 butt/I modified THT leads; 8-9 butt/I solder-charged; 8-10 flat lug; 8-11 tall-profile bottom-only; 8-12 inward-formed L ribbon; 8-13 BGA collapsing balls; 8-14 BGA noncollapsing; 8-15 column grid array; 8-16 BTC; 8-17 D-Pak bottom thermal pad; 8-18 flattened post; 8-19 P-style; 8-20 vertical cylindrical cans with outward L leads; 8-21 flex/rigid-flex flat unformed leads; 8-22 wrapped terminals; 8-23 flat-leaded SMT connectors; 8-24 SMTS / SMT fasteners minimum solder. | value not in excerpt | package family | SMT | inspect | [4] TOC §8.3 pp.8-6..8-113, Tables 8-1..8-24 | medium |
| A610-026 | assembly | Chip termination variations: billboarding §8.3.2.9.1, upside-down §8.3.2.9.2, stacking §8.3.2.9.3, tombstoning §8.3.2.9.4; center and lateral terminations solder width §8.3.2.10.1 and minimum fillet height §8.3.2.10.2. | value not in excerpt | | chip parts | inspect | [4] TOC §8.3.2.9–8.3.2.10 pp.8-25..8-32 | medium |
| A610-027 | assembly | Area array: alignment §8.3.12.1; solder ball spacing §8.3.12.2; solder connections §8.3.12.3; voids §8.3.12.4; underfill/staking §8.3.12.5; package-on-package §8.3.12.6. | value not in excerpt | | BGA/CSP/CGA | inspect (X-ray) | [4] TOC §8.3.12 pp.8-87..8-92 | medium |
| A610-028 | assembly | Bottom termination components §8.3.13 (Table 8-16); bottom thermal pad D-Pak §8.3.14 (Table 8-17); flattened post connections §8.3.15 with max overhang on square/round land and max fillet height; P-style §8.3.16; vertical cylindrical cans §8.3.17; flex circuitry with flat unformed leads §8.3.18; wrapped terminals §8.3.19; flat-leaded SMT connectors §8.3.20; specialized SMT §8.4; SMT connectors §8.5 and SMT threaded standoffs/fasteners §8.5.1. | value not in excerpt | | | inspect | [4] TOC §8.3.13–8.5.1 pp.8-94..8-113 | medium |
| A610-029 | assembly | Staking adhesive: component bonding §8.1.1; mechanical strength §8.1.2; SMT leads plastic components, damage, flattening §8.2.x; coplanarity for flat gull wing §8.3.5.8, coined gull wing §8.3.6.9, J leads §8.3.7.8. | value not in excerpt | | | inspect | [4] TOC §8.1–8.2, §8.3.5.8, 8.3.6.9, 8.3.7.8 | medium |
| A610-030 | assembly | Through-hole supported holes: axial horizontal/vertical §7.3.1–7.3.2; protrusion of leads per Table 7-3 (§7.3.3); clinches §7.3.4; solder §7.3.5 with minimum solder requirements Table 7-4 and features: vertical fill (A) §7.3.5.1, destination-side lead-to-barrel (B) §7.3.5.2, destination-side land area coverage (C) §7.3.5.3, source-side lead-to-barrel (D) §7.3.5.4, source-side land area coverage (E) §7.3.5.5; solder in lead bend §7.3.5.6; solder touching THT body §7.3.5.7; meniscus in solder §7.3.5.8; lead cutting after soldering §7.3.5.9; coated wire insulation in solder §7.3.5.10; vias without lead §7.3.5.11; board-in-board §7.3.5.12 (Table 7-5). | value not in excerpt | | THT PTH | inspect | [4] TOC §7.3 pp.7-28..7-50 | medium |
| A610-031 | assembly | Unsupported holes: axial horizontal/vertical §7.4.1–7.4.2; protrusion Table 7-6 (§7.4.3); clinches §7.4.4; solder §7.4.5 with minimum acceptable conditions Table 7-7; lead cutting after soldering §7.4.6. | value not in excerpt | | NPTH | inspect | [4] TOC §7.4 pp.7-53..7-60 | medium |
| A610-032 | components | THT component mounting: orientation horizontal/vertical §7.1.1.x; lead forming bend radius per Table 7-1 (§7.1.2.1), space between seal/weld and bend §7.1.2.2, stress relief §7.1.2.3, damage §7.1.2.4; leads crossing conductors §7.1.3; hole obstruction §7.1.4; DIP/SIP and sockets §7.1.5; radial vertical/spacers/horizontal §7.1.6–7.1.7; connectors right-angle and vertical shrouded headers §7.1.8.x; component-to-land clearance Table 7-2 (p.7-29). | value not in excerpt | lead dia | THT | inspect | [4] TOC §7.1 pp.7-1..7-18 | medium |
| A610-033 | mechanical | Component securing: mounting clips §7.2.1; adhesive bonding nonelevated §7.2.2.1 / elevated §7.2.2.2; other devices §7.2.3. | n/a | | | inspect | [4] TOC §7.2 pp.7-19..7-27 | medium |
| A610-034 | mechanical | Hardware installation: electrical clearance §4.1.1; interference §4.1.2; high-power component mounting §4.1.3; heatsinks with insulators/thermal compounds §4.1.4.1 and contact §4.1.4.2; threaded fasteners §4.1.5 with torque §4.1.5.1, solid wires §4.1.5.2, stranded wires §4.1.5.3; jackpost mounting §4.2. | value not in excerpt | torque spec | mechanical assembly | inspect | [4] TOC §4.1–4.2 pp.4-2..4-15 | medium |
| A610-035 | connectors | Connector pins: edge connector pins §4.3.1; press-fit pins §4.3.2 with land/annular ring §4.3.2.1 and soldering §4.3.2.2; wire bundle securing §4.4; routing wires and bundles §4.5; damage to connectors §9.5, edge connector pins §9.9, press-fit pins §9.10, backplane pins §9.11. | value not in excerpt | | connectors | inspect | [4] TOC §4.3–4.5, §9.5–9.11 | medium |
| A610-036 | solder | Soldering anomalies catalog (§5.2): exposed basis metal §5.2.1; pin holes/blow holes/voids §5.2.2; reflow of solder paste §5.2.3; nonwetting §5.2.4; cold connection §5.2.5; dewetting §5.2.6; excess solder §5.2.7 — solder balls §5.2.7.1, bridging §5.2.7.2, webbing/splashes §5.2.7.3; disturbed solder §5.2.8; cooling lines and secondary reflow §5.2.9; fractured solder §5.2.10; solder projections §5.2.11; Pb-free fillet lift §5.2.12; Pb-free hot tear/shrink hole §5.2.13; probe marks §5.2.14; inclusions §5.2.15; partially visible/hidden connections §5.3; heat-shrinkable soldering devices §5.4. | value not in excerpt | | all solder joints | inspect | [4] TOC §5 pp.5-1..5-21 | medium |
| A610-037 | cables | Terminal connections (§6): swaged hardware terminals — base-to-land separation §6.1.1.1, turret §6.1.1.2, bifurcated §6.1.1.3, rolled/flared flange §6.1.2–6.1.3, controlled split §6.1.4, solder §6.1.5 with Table 6-1 minimum soldering; insulation damage pre/post solder §6.2.1.x, clearance §6.2.2, sleeving placement/damage §6.2.3.x; conductor deformation/damage (strand damage Table 6-2; solid wire), birdcaging pre/post solder §6.3.3–6.3.4, tinning §6.3.5; service loops §6.4; bend radius Table 6-3 (§6.5); stress relief §6.6; placement Tables 6-4 (turret/straight pin), 6-5 (bifurcated side route), 6-6 (staking side route), 6-7 (bifurcated bottom route), 6-8 (pierced/perforated), 6-9 (hook), 6-10 (AWG 30 and smaller wrap); solder cups §6.14; series connected §6.16; edge clip position §6.17. | value not in excerpt | AWG, terminal | wired assemblies | inspect | [4] TOC §6 pp.6-1..6-55 | medium |
| A610-038 | components | Component damage chapters: loss of metallization §9.1; chip resistor element §9.2; ceramic chip capacitors §9.4 with nick or chip-out criteria Table 9-1 (p.9-8); relays §9.6; ferrite core components §9.7; connectors/handles/extractors/latches §9.8; heatsink hardware §9.12; threaded items §9.13. | value not in excerpt | | | inspect | [4] TOC §9 pp.9-1..9-19 | medium |
| A610-039 | fab | Printed board conditions after assembly (§10): non-soldered contact area contamination/damage §10.1.x; laminate — measling and crazing §10.2.1, blistering/delamination §10.2.2, weave texture/exposure §10.2.3, haloing §10.2.4, nicks and cracks §10.2.5, burns §10.2.6, bow and twist §10.2.7, depanelization §10.2.8, mechanical damage §10.2.9; conductors/lands reduction §10.3.1, lifted §10.3.2, mechanical damage §10.3.3; flex/rigid-flex damage, delamination (flex, flex-to-stiffener), solder wicking, attachment §10.4.x. | value not in excerpt | | assembled boards | inspect | [4] TOC §10.1–10.4 pp.10-1..10-31 | medium |
| A610-040 | assembly | Marking: etched incl. hand printing §10.5.1; screened §10.5.2; stamped §10.5.3; laser §10.5.4; labels — bar code/data matrix §10.5.5.1, readability §10.5.5.2, adhesion and damage §10.5.5.3, position §10.5.5.4; RFID tags §10.5.6. | n/a | | | inspect | [4] TOC §10.5 pp.10-32..10-40 | medium |
| A610-041 | assembly | Cleanliness: flux residues — cleaning required §10.6.1.1, no-clean process §10.6.1.2; FOD §10.6.2; chlorides, carbonates and white residues §10.6.3; surface appearance §10.6.4. | value not in excerpt | | | inspect | [4] TOC §10.6 pp.10-41..10-47 | medium |
| A610-042 | assembly | Solder mask coating: wrinkling/cracking §10.7.1; voids/blisters/scratches §10.7.2; breakdown §10.7.3; discoloration §10.7.4. Conformal coating general §10.8.1, coverage §10.8.2 (see A610-020..022), thickness §10.8.3 with **Table 10-1 Coating Thickness Requirements** (p.10-57); electrical insulation coating coverage/thickness §10.9.x; encapsulation §10.10. | value not in excerpt | coating type | | measure | [4] TOC §10.7–10.10 pp.10-48..10-59 | medium |
| A610-043 | assembly | Discrete wiring solderless wrap §11.1; high voltage §12; jumper wires §13 — routing §13.1, staking adhesive or tape §13.2, terminations lap (component lead / land), wire-in-hole, wrapped, SMT (chip/cylindrical, gull wing, castellations) §13.3.x. | value not in excerpt | | rework / jumpers | inspect | [4] TOC §11–13 | medium |
| A610-044 | esd | Appendix A handling: ESD control program A.1.1; EPA requirements A.1.2; minimizing static charge A.1.3 with Table A-1 typical static charge sources and Table A-2 typical static voltage generation (p.A-3); protective packaging A.1.4; training; tools; compliance verification A.1.7; warning labels A.1.8; general handling A.2 with Table A-3 recommended practices (p.A-6); contamination prevention, gloves/finger cots A.2.2–A.2.3; moisture sensitive devices A.3. | value not in excerpt | | handling | review | [4] TOC App. A pp.A-1..A-8 | medium |
| A610-045 | process | Terms (§1.8): board orientation primary/secondary/solder source/solder destination side §1.8.1.x; bubble and bridging bubble §1.8.2.x; cold solder connection §1.8.3; common/noncommon conductors §1.8.4/§1.8.18; conductor overlap/overwrap §1.8.5–1.8.6; diameter §1.8.7; engineering documentation §1.8.9; FOD §1.8.10; form/fit/function §1.8.11; high voltage §1.8.12; intrusive solder §1.8.13; kink §1.8.14; locking mechanism §1.8.15; manufacturer §1.8.16; meniscus §1.8.17; nonfunctional land §1.8.19; pin-in-paste §1.8.20; solder balls §1.8.21; standard industry practice §1.8.22; stress relief §1.8.23; supplier §1.8.24; tempered leads §1.8.25; user §1.8.26. Requirements flowdown §1.9; personnel proficiency §1.10; acceptance requirements §1.11 with missing parts §1.11.1 and jumper/Z-wire §1.11.2. | n/a | | | review | [4] TOC §1.8–1.11 pp.1-4..1-6 | high (structure) |
| A610-046 | process | Applicable documents: IPC §2.1, joint industry §2.2, Electrostatic Association §2.3, IEC §2.4, ASTM §2.5, military standards §2.6, SAE §2.7; Table 1-1 summary of related documents (p.1-1). | n/a | | | review | [4] TOC §2 pp.2-1..2-3 | high |

### 1.5 Library guides (process rules)

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| LIB-001 | process | Books teach engineering; they do not freeze compliance. The applicable **current** standards, component datasheets, reference designs and the PCB fabricator/assembler's current capabilities are the controlling documents for a real product. | n/a | | every release | review | [5] p.1, p.23; [6] p.11 | high |
| LIB-002 | process | Bring each specialist reference into the project **before** the corresponding design becomes expensive to change; use one real product as the spine of the curriculum rather than reading all books first. | n/a | | | review | [5] p.21 | high |
| LIB-003 | process | Learning/design sequence (guide 1 flowchart): Electronics foundation (Scherz & Monk → Horowitz & Hill) → Product architecture (Wilson + Cohen) → Embedded co-design (White + Stringham) → Power architecture (Erickson → Pressman) → Schematic/ECAD (Mitzner et al.) → PCB technology + DfM (Coombs & Holden) → High-speed/SI/PI (Johnson & Graham → Bogatin) → [Custom RF/wireless? yes: Bowick → Pozar → Balanis] → EMC engineering (Ott → Williams → Archambeault) → Prototype bring-up, debug + validation (Pease) → Production transfer (Bralla + Coombs/Holden + Cohen + current standards). | ordered list | product type | first product | review | [5] p.21–22 | high |
| LIB-004 | process | Guide 2 13-step end-to-end path: (1) Practical Electronics for Inventors + build circuits; (2) AoE 3e in parallel with Learning the Art of Electronics 2e; (3) Circuit Designer's Companion before first serious product; (4) architecture + schematic: partition power domains, analog/digital/RF blocks, clocks, reset, programming/debug, interfaces, connectors, ESD/protection, test points; (5) Printed Circuits Handbook + PCEA PCB Basics, then fabrication requirements from IPC-2221C and IPC-6012F rather than tool defaults; (6) Bogatin before committing the stackup, then Johnson & Graham — fix layer count, reference planes, impedance classes, via strategy, connector launches, PDN structure before dense routing; (7) Brooks & Adam for high-current traces/vias plus a board- and enclosure-level thermal budget; (8) Erickson then Pressman for custom switching power — validate startup, stability, transient response, losses, component stresses by calculation, simulation and bench; (9) RF: Steer → Pozar → Razavi, move quickly into S-parameters, VNA, EM simulation, current RF standards; (10) EMC before layout freeze: Paul/Scully/Steffka → Ott → Williams; (11) structured EVT/DVT; (12) before production release: Printed Circuits Handbook, O'Connor/Kleyner, IPC-6012F, J-STD-001J, IPC-A-610J — put fabrication, assembly, inspection, programming and functional-test requirements into controlled production documentation; (13) freeze regulatory requirements only after checking current rules for the exact product and target countries. | ordered list | | | review | [6] pp.18–19 | high |
| LIB-005 | requirements | Determine regulatory applicability (FCC/EU directives/safety standard family) **during architecture, not after DVT**; IEC 62368-1 is AV/ICT-scoped only — industrial, medical, appliance, automotive, aerospace need different regimes. | n/a | market, product family | | review | [6] pp.12–13, p.17 | high |
| LIB-006 | test | EVT/DVT must exercise: supply limits, temperature, load transients, clocks/interfaces, ESD/immunity, emissions, fault cases, sensor accuracy, long-duration operation; use applicable IEC 61000-4 and environmental/product standards to make robustness tests reproducible. | n/a | | prototype validation | measure | [6] p.19 step 11 | high |
| LIB-007 | current-carrying | Size high-current traces and vias by electrothermal analysis (Brooks & Adam) connecting copper width, via count and temperature rise, instead of legacy "amps per trace width" charts; do not treat copper width, via count and temperature rise as separate subjects. | n/a | I, Cu geometry | power paths | calc/sim | [6] p.6, p.15, p.18 step 7 | medium (qualitative) |
| LIB-008 | stackup | Determine layer count, reference planes, impedance classes, via strategy, connector launches and PDN structure **before** dense routing begins. | n/a | | PCB planning | review | [6] p.18 step 6; [5] p.22 gate "PCB planning" | high |
| LIB-009 | hw-fw | Hardware/software partitioning, boot/reset, register maps, debug interfaces and testability are architecture decisions, not firmware clean-up; commit Stringham's HW/FW interface practices before register maps, FPGA/MCU interfaces and reset/boot behavior are frozen. | n/a | | embedded products | review | [5] p.15, p.22 | high |
| LIB-010 | process | Product gates → engineering outputs (guide 1): Concept/architecture → requirements, subsystem block diagram, interfaces, preliminary risks, power budget, MCU/FPGA/RF decisions; Electrical architecture → power tree, clocks, reset/boot strategy, ADC/DAC/sensor interfaces, HW/FW contract; Detailed schematic → hierarchical schematic, component choices, protection, test/debug connectors, BOM, initial simulation; PCB planning → layer stack-up, impedance targets, placement zoning, return paths, PDN concept, fabrication capabilities; PCB implementation → placement, routing, via strategy, decoupling, RF/clock/high-speed constraints, DRC/DFM; Prototype bring-up → rail/clock/reset checks, current limits, firmware boot, interface validation, fault isolation; Pre-compliance/design validation → SI measurements, power integrity, thermal behavior, emissions/immunity, RF performance, antenna tuning; Production release → fabrication/assembly package, process tolerances, inspection/test strategy, supplier qualification, yield feedback. | deliverable list per gate | | all products | review | [5] p.22 | high |
| LIB-011 | process | Put IPC-2221 (design), IPC-6012 (rigid board qualification/performance), J-STD-001 (assembly process) and IPC-A-610 (assembly acceptability) into the fabrication and assembly drawings; a team with only layout books has not completed the PCB-manufacturing side of design. | n/a | | fab & assembly drawings | review | [6] p.14 | high |
| LIB-012 | process | Study-time budget (guide 1 estimates, active study): all 20 books deeply ≈ 700–1,000 h; competent non-RF end-to-end path ≈ 350–550 h (Coombs/Holden and Bralla as references; selective Erickson, Ott, AoE); custom wireless/antenna adds ≈ 150–250 h (Bowick/Pozar/Balanis). | hours | team plan | curriculum planning | review | [5] p.18 | high |
| LIB-013 | process | Irreducible five-book core (guide 1): Horowitz & Hill AoE; Wilson Circuit Designer's Companion; Mitzner et al. Complete PCB Design Using OrCAD; Bogatin Signal and Power Integrity—Simplified; Ott Electromagnetic Compatibility Engineering. | 5 titles | | | review | [5] p.1 | high |
| LIB-014 | process | Minimal purchase set, non-RF embedded product (guide 1): AoE, Wilson, Cohen, Mitzner, Coombs/Holden, Johnson, Bogatin, Ott, Williams, Erickson, Pressman, White, Stringham, Pease, Bralla (15). Wireless: add Bowick, Pozar, Balanis. Scherz/Monk is a prerequisite/refresher; Archambeault when EMI performance is a serious constraint. | 15 (+3 RF) | | | review | [5] p.23 | high |
| LIB-015 | process | Minimum purchase order (guide 2): Practical Electronics for Inventors; AoE; Learning the Art of Electronics; Circuit Designer's Companion; Printed Circuits Handbook; Signal and Power Integrity—Simplified; High-Speed Digital Design; PCB Design Guide to Via and Trace Currents and Temperatures; Introduction to Electromagnetic Compatibility; Electromagnetic Compatibility Engineering; EMC for Product Designers; Fundamentals of Power Electronics; then Steer (RF), Fraden (sensor-heavy), O'Connor/Kleyner (volume/reliability). Pair from the beginning with IPC-2221C, IPC-6012F, J-STD-001J, IPC-A-610J and applicable safety/EMC/regulatory standards. | 12 (+3 conditional) | | | review | [6] p.19 | high |
| LIB-016 | process | Indispensable stack for a normal MCU commercial board (USB/Ethernet, switching regulators, sensors, pre-certified wireless module): AoE/Practical Electronics → Wilson → Printed Circuits Handbook/IPC → Bogatin → Brooks/Adam → Paul/Ott/Williams → applicable safety/regulatory documents. RF/microwave stack is must-have only if the antenna, RF front end or microwave interconnect is your design responsibility. | ordered list | product type | | review | [6] p.16 | high |
| LIB-017 | process | Tier definitions (guide 2): Must-have = materially reduces risk on a general commercial hardware product; Recommended = important once the product contains the corresponding technology; Optional = excellent depth, not needed cover-to-cover before shipping a first product. | tier ∈ {must-have, recommended, optional} | | | review | [6] p.1 | high |
| LIB-018 | transmission-line | For multi-gigabit links (PCIe, USB, Ethernet), the current interface electrical/channel specification (PCI-SIG, USB-IF, IEEE 802.3) defines channel budgets, compliance measurements and TX/RX requirements; use books (Johnson, Bogatin, Hall, Ritchey) for physics and the live spec plus FPGA/ASIC/connector vendor channel models for design; validate with field/circuit solvers. | n/a | interface | high-speed serial | sim/measure | [6] p.13, p.16 | high |
| LIB-019 | rf | For cellular products, band plan, RF performance requirements, conformance cases, modem/module constraints, antenna tuning and certification inputs come from current 3GPP TS 38-series and chipset/module documentation; Steer/Razavi supply architecture only. | n/a | | 5G/NR | review | [6] p.13, p.17 | high |
| LIB-020 | firmware | Real embedded products additionally require current MCU/SoC reference manuals, errata, boot/security documentation, RTOS documentation, low-power-state behavior and BSP information — none replaceable by static books. | n/a | | embedded | review | [6] p.17 | high |
| LIB-021 | process | Schematic-capture durable knowledge = component behavior, power-domain partitioning, interface protection, grounding, decoupling, design-for-test, unambiguous communication; the implementation layer (hierarchical sheets, net classes, differential-pair definitions, variants, BOM fields, library management, ERC) is learned in the current EDA system's documentation. | n/a | | | review | [6] p.13, p.17 | high |
| LIB-022 | thermal | Thermal/mechanical is the weakest part of an electronics-only library: enclosure CFD, shock/vibration, connector retention, ingress protection, plastics, tolerance stacks and structural mechanics need mechanical references and simulation; determine environmental qualification from the intended operating environment and IEC/product standards, not from PCB temperature calculations alone. | n/a | | | review | [6] p.17 | high |
| LIB-023 | emc | Study EMC before prototype layout is frozen; the cheapest EMC failure is the one removed from the stackup, connector, return-current path or enclosure architecture before fabrication. Start Ott before layout, not after an EMC failure; revisit during enclosure/cabling design and pre-compliance debugging. | n/a | | | review | [6] p.18 step 10; [5] p.12 | high |
| LIB-024 | power | For simple integrated point-of-load regulators study Erickson selectively; for custom switch-mode power stages or control loops study the relevant Erickson converter chapters before choosing a topology, then Pressman for magnetics, gate drive, snubbers and compensation. | n/a | topology | power design | review | [5] p.13, p.22 | high |
| LIB-025 | bringup | Read Pease before the first prototype arrives; keep at the bench through bring-up (measurement strategy, failure isolation, component problems, oscillation/noise, avoiding misleading measurements). | n/a | | bring-up | review | [5] p.16, p.22 | high |
| LIB-026 | dfm | Before locking stack-up, via structures, materials, panel assumptions or fabrication drawings, read the relevant Coombs/Holden sections; DfM material connects production yield to design complexity; use Bralla + Coombs/Holden manufacturing sections before tooling, supplier selection, production release and large-volume procurement. | n/a | | | review | [5] p.22 | high |
| LIB-027 | sim | SPICE (LTspice + vendor models/reference designs) accompanies, never replaces, hand analysis; use for op-amp stability, filters, startup/transients, switching regulators and tolerance exploration before PCB fabrication. | n/a | | pre-layout | sim | [6] p.12 | high |
| LIB-028 | rf | Use current solver documentation (Keysight ADS, Ansys HFSS, equivalents) when geometry must be electromagnetically modeled rather than estimated with closed-form equations (antennas, RF matching, packages, connectors, high-speed channels). | n/a | | RF/SI | sim | [6] p.13 | high |
| LIB-029 | reliability | Bring reliability engineering (O'Connor & Kleyner: failure rates, reliability prediction, testing, maintainability) into requirements and DVT rather than waiting for field failures. | n/a | | volume products | review | [6] p.9, p.15 | high |
| LIB-030 | process | Newest book is not automatically first choice: Bogatin (2018) is the SI/PI entry but does not replace Johnson; Paul/Scully/Steffka (2022) pairs with Ott (2009); Steer (2019) is the RF entry while Pozar remains the deeper theory reference. | n/a | | | review | [6] p.10 | high |
| LIB-031 | process | Wilson's Circuit Designer's Companion should shape the engineering checklist (PCB design rules, component selection, EMC design checklist, production/testability/reliability, standards appendix) **before** schematic capture starts. | n/a | | | review | [5] p.7 | high |

## 2. Formulas & tables (numbers)

### 2.1 Printed numeric limits (the only numbers actually present in the four IPC excerpts)

| # | quantity | value | class cols | condition | source |
|---|---|---|---|---|---|
| N1 | IPC-2221C unit break | ≥ 0.1 mm [0.0039 in] → mm/in; < 0.1 mm → µm/µin | all | documentation | [1] §1.3 p.1 |
| N2 | IPC-6012F unit break | ≥ 1.0 mm [0.0394 in] → mm/in; < 1.0 mm → µm/µin | all | documentation | [2] §1.6 p.5 |
| N3 | Altitude boundary for spacing categories B2/B3, A7/A8 | 3050 m [10,007 ft] | all | uncoated external conductors / leads | [1] §6.3.3.1.2–6.3.3.1.8 pp.58–59 |
| N4 | Default performance class | Class 2 | — | when not specified | [2] Table 1-2 p.2 |
| N5 | Default starting foil weight | 1/2 oz all internal + external layers; Type 1: 1 oz; plated HDI layers: 1/4 oz | — | when not specified | [2] Table 1-2 p.2 |
| N6 | Default hole dia tolerance, plated component holes | ± 100 µm [3,937 µin] | Class 2 default | when not specified | [2] Table 1-2 p.2 |
| N7 | Default hole dia tolerance, plated via-only | + 80 µm [3,150 µin] / − no requirement (may be totally or partially plugged) | Class 2 default | when not specified | [2] Table 1-2 p.2 |
| N8 | Default hole dia tolerance, non-plated | ± 80 µm [3,150 µin] | Class 2 default | when not specified | [2] Table 1-2 p.2 |
| N9 | Default minimum dielectric separation | 65 µm [2,560 µin] | Class 2 default | when not specified, per §3.6.2.18 | [2] Table 1-2 p.3 |
| N10 | Microvia maximum depth X (capture-land foil → target land) | ≤ 0.25 mm [0.00984 in] | all | definition | [2] §1.4.4 p.5, Fig 1-3 Note 3 |
| N11 | Microvia maximum plating aspect ratio X/Y | ≤ 1:1 | all | definition | [2] §1.4.4 p.5 |
| N12 | Shallow back-drill barrel removal | ≈ 0.05–0.127 mm [0.002–0.005 in] | all | prevent short to component/chassis | [2] §1.4.1 p.4, Fig 1-2 |
| N13 | Thermal stress temperatures (Method 2.6.27) | 230 °C (eutectic SnPb reflow, §3.6.1.2); 260 °C (Pb-free reflow, §3.6.1.3) | all | selected in procurement doc | [2] TOC §3.6.1.2–3.6.1.3 p.24; §1.3.3 p.2 |
| N14 | Default thermal stress method | IPC-TM-650 2.6.8 Condition A | all | when not specified | [2] Table 1-2 p.3 |
| N15 | Default SnPb solder coating | Sn63/Pb37 | all | HASL/solder coat | [2] Table 1-2 p.3 |
| N16 | Default solderability test category | J-STD-003 Category 2 (SnPb); Category A (Pb-free) | all | | [2] Table 1-2 p.3 |
| N17 | Default surface finish switch date | on/before 2023-10-01: X1 (Table 3-3); on/after 2023-10-01: ENIG2 (Table 3-3) | all | initial drawing release date | [2] Table 1-2 Notes 1–2 p.3 |
| N18 | Default solder mask class | IPC-SM-840 Class T | all | when mask specified without class | [2] Table 1-2 p.3 |
| N19 | Conformance limits interpretation | absolute limits per ASTM E29 | all | J-STD-001 | [3] §1.4.1 p.1 |

No other numeric limits (annular ring, spacing, plating thickness, fillet dimensions, coating thickness, torque, bend radius, magnification) are printed in these excerpts. Table ids are mapped below so Anvil can cite them.

### 2.2 IPC-6012F Table 1-1 Technology Adders (p.2)

| code | technology |
|---|---|
| HDI | HDI build-up features (stacked and/or staggered microvias) |
| VP | Via Protection |
| WBP | Wire Bondable Pads |
| MB | Metal Base |
| AMC | Active Metal Core |
| NAMC | Non-active Metal Core |
| HF | External Heat Frame |
| EP | Embedded Passives per IPC-6017 |
| VIP-C | Via-in-Pad, Conductive Fill |
| VIP-N | Via-in-Pad, Nonconductive Fill |

Selection-string example: `IPC-6011/6012/3/1/S/-/3/HDI/EP` = quality spec IPC-6011 / spec IPC-6012 / Type 3 / plating process 1 / finish S / no selective finish / Class 3 / adders HDI, EP ([2] §1.3.3.2 p.3).

### 2.3 IPC-6012F Table 1-2 Default Requirements (pp.2–3), verbatim

| category | default selection |
|---|---|
| Performance Class | Class 2 |
| Material | Epoxy-Glass Laminate per 3.2.1 |
| Surface Finish (Note 1: designs initially released on or prior to 01 Oct 2023) | X1 per Table 3-3 |
| Surface Finish (Note 2: designs initially released on or after 01 Oct 2023) | ENIG2 per Table 3-3 |
| Minimum Starting Foil Weight | 1/2 oz for all internal and external layers except Type 1 which shall start with 1 oz. For plated HDI layers – 1/4 oz for all layers (internal or external) |
| Copper Foil Type | Electrodeposited per 3.2.4 |
| Hole Diameter Tolerance — Plated, components | (±) 100 µm [3,937 µin] |
| Hole Diameter Tolerance — Plated, via only | (+) 80 µm [3,150 µin], (−) no requirement (may be totally or partially plugged) |
| Hole Diameter Tolerance — Non-plated | (±) 80 µm [3,150 µin] |
| Conductor Width tolerance | Class 2 requirements per 3.5.1 |
| Conductor Spacing tolerance | Class 2 requirements per 3.5.2 |
| Dielectric Separation | 65 µm [2,560 µin] minimum per 3.6.2.18 |
| Marking Ink | Contrasting color, nonconductive per 3.3.5 |
| Solder Mask | Not applied, if not specified per 1.3.4.3 |
| Solder Mask, specified | Class T of IPC-SM-840 if class not specified per 3.7 |
| SnPb Solder Coating | Sn63/Pb37 per 3.2.7.3.1 |
| Pb-free Solder Coating | 3.2.7.3.2 |
| Solderability Test | Per 3.3.6, Category 2 for SnPb and Category A for Pb-free of J-STD-003 |
| Thermal Stress Test | IPC-TM-650, Method 2.6.8, Condition A per 3.6.1.1 |
| Test Voltage, Isolation Resistance, Continuity Resistance | Per IPC-9252 |
| Qualification not specified | See IPC-6011 |

### 2.4 IPC-6012F codes (§1.3.2, §1.3.4.2, §1.3.4.3 pp.1–4)

Board Types: 1 single-sided (no PTH) · 2 double-sided · 3 multilayer, no blind/buried vias · 4 multilayer with blind and/or buried vias (may include microvias) · 5 multilayer metal core, no blind/buried · 6 multilayer metal core with blind/buried (may include microvias).

Plating process (one digit): 1 acid Cu electroplating only · 2 pyrophosphate Cu only · 3 acid and/or pyrophosphate Cu · 4 additive/electroless Cu · 5 electrodeposited Ni underplate + acid and/or pyrophosphate Cu.

| designator | surface finish / coating | thickness ref |
|---|---|---|
| S | Solder coating | Table 3-3 |
| T | Electrodeposited tin-lead, fused | Table 3-3 |
| X | Either Type S or T | Table 3-3 |
| TLU | Electrodeposited tin-lead, unfused | Table 3-3 |
| b1 | Pb-free solder coating | Table 3-3 |
| G | Gold electroplate for edge printed board connectors | Table 3-3 |
| GS | Gold electroplate for areas to be soldered | Table 3-3 |
| GWB-1 | Gold electroplate, ultrasonic wire bond areas | Table 3-3 |
| GWB-2 | Gold electroplate, thermosonic wire bond areas | Table 3-3 |
| N | Nickel for edge printed board connectors | Table 3-3 |
| NB | Nickel barrier to copper-tin diffusion | Table 3-3 |
| OSP | Organic solderability preservative | Table 3-3 |
| HT OSP | High-temperature OSP | Table 3-3 |
| ENIG | Electroless nickel immersion gold | Table 3-3 |
| ENEPIG | Electroless Ni / electroless Pd / immersion Au | Table 3-3 |
| DIG | Direct immersion gold | Table 3-3 |
| NBEG | Nickel barrier / electroless gold | Table 3-3 |
| IAg | Immersion silver | Table 3-3 |
| ISn | Immersion tin | Table 3-3 |
| C | Bare copper | AABUS |
| SMOBC | Solder mask over bare copper | Table 3-3 / §3.2.8 |
| SM | Solder mask over non-melting metal | §3.2.8 |
| SM-LPI | Liquid photoimageable SM over non-melting metal | §3.2.8 |
| SM-DF | Dry film SM over non-melting metal | §3.2.8 |
| SM-TM | Thermal mask SM over non-melting metal | §3.2.8 |
| Y | Other | §3.2.7.11 |

(Column alignment of the thickness-reference column is reconstructed from the extraction's parallel lists; the standard's own table governs.)

### 2.5 IPC-2221C electrical-clearance categories (§6.3.3.1, pp.58–59) — key into Table 6-1 (values not in excerpt)

| category | conductor situation | altitude / coating |
|---|---|---|
| B1 | Internal conductors | any |
| B2 | External conductors, uncoated | sea level to 3050 m [10,007 ft] |
| B3 | External conductors, uncoated | over 3050 m [10,007 ft] or in a vacuum |
| B4 | External conductors, solder mask | any elevation |
| B5 | External conductors, coated (conformal) | any elevation or in a vacuum |
| A6 | External component lead, coated | any elevation or in a vacuum |
| A7 | External component lead, uncoated | sea level to 3050 m [10,007 ft] |
| A8 | External component leads without conformal coating | over 3050 m [10,007 ft] or in a vacuum |

### 2.6 IPC-2221C clause map (complete TOC, page numbers as printed)

| clause | title | p. |
|---|---|---|
| 1 | SCOPE | 1 |
| 1.1 | Purpose | 1 |
| 1.2 | Documentation Hierarchy | 1 |
| 1.3 | Presentation | 1 |
| 1.3.1 | Dimensional Units – Units of Measure | 1 |
| 1.4 | Interpretation "Shall" | 2 |
| 1.5 | Definition of Terms | 2 |
| 1.5.1 / 1.5.2 / 1.5.3 | Microvia / Back-Drilling / Stub | 2 |
| 1.6 | Classification of Products | 2 |
| 1.6.1 / 1.6.2 / 1.6.3 | Printed Board Type / Performance Classification / Producibility Level | 3 |
| 2 | APPLICABLE DOCUMENTS | 3 |
| 3 | GENERAL REQUIREMENTS | 6 |
| 3.1.1 / 3.1.2 / 3.1.3 | Order of Precedence / End-Product Performance Requirements / Design Data Protection | 8 |
| 3.2 | Design Considerations | 8 |
| 3.3 | Schematic/Logic Diagram | 9 |
| 3.4 | Density Evaluation | 9 |
| 3.5 | Parts List | 10 |
| 3.6 | Test Requirement Considerations | 10 |
| 3.6.1 / 3.6.1.1 | Electrical / Bare Printed Board Testing | 10 |
| 3.6.1.2 | Test Methods | 11 |
| 3.6.1.2.1 | HiPot Testing | 11 |
| 3.6.1.2.2 | Impedance Considerations | 12 |
| 3.6.1.3 | Test Data (Source Data) | 13 |
| 3.6.2 | Printed Board Assembly Testability | 13 |
| 3.6.3 | Boundary Scan Testing | 14 |
| 3.6.4 | Functional Test Concern for Printed Board Assemblies | 14 |
| 3.6.4.1 | Test Connectors | 14 |
| 3.6.4.2 / 3.6.4.3 / 3.6.4.4 / 3.6.4.5 | Initialization and Synchronization / Long Counter Chains / Self Diagnostics / Physical Test Concerns | 15 |
| 3.6.5 | In-Circuit Test Concerns for Printed Board Assemblies | 16 |
| 3.6.5.1 | In-Circuit Test Fixtures | 16 |
| 3.6.5.2 | In-Circuit Test Electrical Considerations | 17 |
| 3.6.6 | Mechanical | 18 |
| 3.6.6.1 / 3.6.6.2 | Uniformity of Connectors / Uniformity of Power Distribution Arrangement and Signal Levels on Connectors | 18 |
| 3.7 / 3.7.1 / 3.7.1.1 / 3.7.2 | Layout Evaluation / Printed Board Layout Design / Layout Concepts / Feasibility Density Evaluation | 18 |
| 4 | MATERIALS | 21 |
| 4.1 | Material Selection | 21 |
| 4.1.1 / 4.1.2 / 4.1.3 / 4.1.4 | Material Selection for Structural Strength / Electrical Properties / Environmental Properties / Physical Properties | 22 |
| 4.2 | Dielectric Base Materials (Including Prepregs and Adhesives) | 22 |
| 4.2.1 / 4.2.2 | Preimpregnated Bonding Layer (Prepreg) / Adhesives | 22 |
| 4.2.2.1–4.2.2.6 | Epoxies / Silicone Elastomers / Acrylics / Polyurethanes / Specialized Acrylate-Based Adhesives / Other Adhesives | 23 |
| 4.2.3 | Adhesive Films or Sheets | 23 |
| 4.2.4 | Electrically Conductive Adhesives | 24 |
| 4.2.5 | Thermally Conductive/Electrically Insulating Adhesives | 24 |
| 4.2.5.1–4.2.5.4 | Epoxies / Silicone Elastomers / Urethanes / Use of Structural Adhesives as Thermal Adhesives | 24 |
| 4.3 | Laminate Materials | 24 |
| 4.3.1–4.3.5 | High Tg Laminates / Color Pigmentation / Dielectric Thickness/Spacing / Thermally Conductive Laminates / Minimum Base Material | 25 |
| 4.4 | Conductive Materials | 25 |
| 4.4.1 / 4.4.2 / 4.4.3 / 4.4.3.1 / 4.4.4 | Electroless Copper Plating / Semiconductive Coatings / Electrolytic Copper Plating / Plating Methods / Gold Plating | 28 |
| 4.4.4.1 / 4.4.4.2 | ENIG / ENIG/EG | 29 |
| 4.4.4.3 / 4.4.5 | ENEPIG / Immersion Silver | 30 |
| 4.4.6 / 4.4.7 | Immersion [Tin] / OSP | 31 |
| 4.4.8 / 4.4.9 | Nickel Plating / Tin/Lead Plating | 32 |
| 4.4.9.1 / 4.4.10 / 4.4.10.1 / 4.4.10.1.1 / 4.4.10.1.2 | Tin Plating / Solder Coating / HASL / Tin Lead HASL / Pb-free HASL | 33 |
| 4.4.11 / 4.4.12 / 4.4.12.1 / 4.4.12.2 / 4.4.12.2.1 / 4.4.12.2.1.1 / 4.4.12.2.1.2 | Other Metallic Coatings for Edge Contacts / Metallic Foil/Film / Copper Foil / Copper Film / Resin Coated Copper Foil / Single Layer Resin / Two Layers Resin | 34 |
| 4.4.12.3 / 4.4.12.4 / 4.5 / 4.5.1 / 4.5.2 / 4.5.3 | Other Foils/Film / Metal Core Substrates / Electronic Component Materials / Embedded Resistors / Embedded Capacitors / Embedded Inductors | 35 |
| 4.6 / 4.6.1 | Organic Protective Coatings / Solder Mask Coatings | 35 |
| 4.6.1.1 / 4.6.1.2 / 4.6.2 / 4.6.2.1 | Mask Adhesion and Coverage / Mask Clearances and Dams / Conformal Coatings / Conformal Coating | 36 |
| 4.6.3 / 4.7 | Tarnish Protective Coating / Marking and Legends | 37 |
| 4.7.1 | ESD Considerations | 38 |
| 5 | MECHANICAL/PHYSICAL PROPERTIES | 38 |
| 5.1 / 5.1.1 / 5.2 | Fabrication Considerations / Bare Printed Board Fabrication / Product/Printed Board Configuration | 38 |
| 5.2.1 / 5.2.2 / 5.2.3 / 5.2.3.1 | Printed Board Type / Size / Size and Shape / Material Size | 39 |
| 5.2.4 / 5.2.4.1 / 5.2.5 / 5.2.6 | Bow and Twist / Bow and Twist for PC Card / Structural Strength / Composite (Constraining-Core) Printed Boards | 41 |
| 5.2.7 | Vibration Design | 42 |
| 5.3 / 5.3.1–5.3.4 | Assembly Requirements / Mechanical Hardware Attachment / Part Support / Assembly and Test / Tooling Rails for PC Card | 43 |
| 5.4 / 5.4.1 / 5.4.2 / 5.4.2.1 | Dimensioning Systems / Dimensions and Tolerances / Component and Feature Location / Grid Systems | 44 |
| 5.4.2.2 / 5.4.3 | Gridless Systems / Datum Features | 45 |
| 5.4.3.1 | Datum Features for Palletization | 47 |
| 5.5 / 5.6 / 5.7 | Printed Board Thickness Tolerance / Panelization / Palletization | 50 |
| 5.7.1 / 5.8 / 5.8.1 / 5.8.2 | Breakaway Tabs / Plated Edges / Perimeter Edge Plating / Edge Plating for Round Parts | 51 |
| 5.8.3 / 6.1 / 6.1.1 / 6.1.2 | Anchor Points / Electrical Considerations / Electrical Performance / Power Distribution Considerations | 52 |
| 6.1.3 | Circuit Type Considerations | 53 |
| 6.1.3.1 | Digital Circuits | 54 |
| 6.1.3.2 / 6.2 / 6.2.1 | Analog Circuits / Conductive Material Requirements / Surge Current | 55 |
| 6.2.1.1 / 6.3 | Example Algorithm Calculation Within an Application / Electrical Clearance | 56 |
| 6.3.1 / 6.3.2 / 6.3.2.1 / 6.3.3 | Line-of-Sight / Dielectric Spacing (Layer-to-layer) / DWV / Creepage | 57 |
| 6.3.3.1 / 6.3.3.1.1–6.3.3.1.4 | Minimum Spacing Categories / B1 / B2 / B3 / B4 | 58 |
| 6.3.3.1.5–6.3.3.1.8 / 6.3.4 / 6.3.5 | B5 / A6 / A7 / A8 / CAF Growth / CTI | 59 |
| 6.4 / 6.4.1 | Impedance Controls / Microstrip | 60 |
| 6.4.2 / 6.4.3 | Embedded Microstrip / Stripline Properties | 61 |
| 6.4.4 | Asymmetric Stripline Properties | 62 |
| 6.4.5 / 6.4.6 | Impedance Documentation / Capacitance Considerations | 63 |
| 6.4.7 / 7 | Inductance Considerations / THERMAL MANAGEMENT | 65 |
| 7.1 / 7.1.1 / 7.1.2 / 7.1.3 | Cooling Mechanisms / Conduction / Radiation / Convection | 66 |
| 7.1.4 / 7.2 / 7.2.1 / 7.2.1.1 | Altitude Effects / Heat Dissipation Considerations / Printed Board Housings / Enclosed Housing | 67 |
| 7.2.1.2 / 7.2.2 / 7.2.3 | Ventilated Housing / Individual Component Heat Dissipation / Thermal Management for Printed Board Heatsinks | 68 |
| 7.2.4 | Assembly of Heatsinks to Printed Boards | 69 |
| 7.2.5 / 7.3 / 7.3.1 | Special Design Considerations for SMT Heatsinks / Heat Transfer Techniques / CTE Characteristics | 70 |
| 7.3.2 / 7.3.3 / 7.4 | Thermal Transfer / Thermal Matching / Thermal Design Reliability | 71 |
| 8 | COMPONENT AND ASSEMBLY ISSUES | 72 |
| 8.1 / 8.1.1 / 8.1.1.1–8.1.1.3 / 8.1.2 | General Placement Requirements / Automatic Assembly / Board Size, Mixed Assemblies, Surface Mounting / Component Placement | 73 |
| 8.1.3 | Orientation | 74 |
| 8.1.4–8.1.7 | Accessibility / Design Envelope / Component Body Centering / Flush Mounting Over Conductive Areas | 75 |
| 8.1.8 / 8.1.9 / 8.1.9.1 / 8.1.9.1.1 | Clearances / Physical Support / Mounting Techniques for Shock and Vibration / Filleting | 76 |
| 8.1.9.2 | Class 3 High Reliability Applications | 77 |
| 8.1.10 / 8.1.11 | Heat Dissipation / Stress Relief | 78 |
| 8.2 / 8.2.1 | General Attachment Requirements / Through-Hole | 79 |
| 8.2.2 / 8.2.3 / 8.2.4 / 8.2.4.1 | Surface Mounting / Mixed Assemblies / Soldering Considerations / Thermal Stress Methodologies | 80 |
| 8.2.5 | Connectors and Interconnects | 81 |
| 8.2.5.1–8.2.5.5 | One-Part / Dual In-line / Edge Printed Board / Two-Part Multiple / Two-Part Discrete-Contact Connectors | 82 |
| 8.2.5.6 / 8.2.6 / 8.2.7 | Edge Printed Board Adapter Connectors / Fastening Hardware / Stiffeners | 83 |
| 8.2.8 / 8.2.9 / 8.2.9.1 | Lands for Flattened Round Leads / Solder Terminals / Terminal Mounting-Mechanical | 84 |
| 8.2.9.2 / 8.2.9.3 / 8.2.10 | Terminal Mounting-Electrical / Attachment of Wires/Leads to Terminals / Eyelets | 85 |
| 8.2.11 / 8.2.11.1–8.2.11.3 / 8.2.12 / 8.2.13 / 8.2.14 | Special Wiring / Jumper Wires, Types, Application / Heat Shrinkable Devices / Bus Bar / Flexible Cable | 86 |
| 8.3 / 8.3.1 / 8.3.1.1–8.3.1.6 | Through-Hole Requirements / Leads Mounted in Through-Holes / Straight, Unclinched, Clinched, Partially Clinched, DIP and SIP, Axial Leaded | 87 |
| 8.3.1.7 | Radial-Lead Components | 88 |
| 8.3.1.8 / 8.3.1.9 / 8.3.1.10 | Perpendicular (Vertical) Mounting / Flat-Packs / Metal Power Packages | 89 |
| 8.4 / 8.4.1 | Standard Surface Mount Requirements / Surface-Mounted Leaded Components | 90 |
| 8.4.2 | Flat-Pack Components | 91 |
| 8.4.3 / 8.4.4 / 8.4.5 / 8.5 | Ribbon Lead Termination / Round Lead Termination / Component Lead Sockets / Fine Pitch SMT (Peripherals) | 92 |
| 8.6 / 8.6.1–8.6.3 / 8.7 / 8.8 / 8.9 | Bare Die / Wire Bond, Flip Chip, Chip Scale / TAB / Grid Array SMT / No-Lead Devices | 93 |
| 8.9.1 / 8.10 / 9 / 9.1 | PQFN, PSON / Compliant Pin Design Guidelines / HOLES/INTERCONNECTIONS / General Requirements for Lands with Holes | 94 |
| 9.1.1 / 9.1.2 | Land Requirements / Annular Ring Requirements | 95 |
| 9.1.2.1 / 9.1.2.2 / 9.1.3 | External Annular Ring / Internal Annular Ring / Thermal Relief in Conductor Planes | 96 |
| 9.1.4 | Clearance Area in Planes | 97 |
| 9.1.4.1 / 9.1.5 / 9.1.6 / 9.1.7 | Small Pitch Clearance Area in Planes / Lands for Flattened Round Leads / Lands for Eyelets or Standoff Terminals / Conductive Pattern Feature Location Tolerance | 98 |
| 9.2 / 9.2.1 / 9.2.1.1 / 9.2.1.2 / 9.2.2 / 9.2.2.1–9.2.2.4 | Holes / Unsupported Holes / Tooling / Mounting / Supported Holes / Plated, Component Plated, Plated Via, Specifying Hole Sizes for Vias | 99 |
| 9.2.2.5–9.2.2.8 / 9.2.2.8.1 | Blind Vias / Buried Vias / Thermal Vias / Compliant Pin (Press-fit) Systems / Considerations | 100 |
| 9.2.3 / 9.2.4 / 9.2.5 | Location / Hole Pattern Variation / Location Tolerances | 101 |
| 9.2.5.1 / 9.2.5.1.1 / 9.2.5.1.2 / 9.2.5.2 / 9.2.5.2.1 / 9.2.5.2.2 / 9.2.6–9.2.9 / 9.3 | NPTH Tolerances / Tooling / Mounting / PTH Tolerances / PTH Tolerances / Board Mounting Holes / Quantity, Spacing of Adjacent Holes, Aspect Ratio, Etchback / Via Protection | 102 |
| 9.3.1 | Via Protection Requirements | 103 |
| 9.3.2 / 9.4 / 10 / 10.1 / 10.1.1 | Via Fill / Back-drilling Guidance / GENERAL CIRCUIT FEATURE REQUIREMENTS / Conductor Characteristics / Conductor Width and Thickness | 104 |
| 10.1.2 / 10.1.3 | Electrical Clearance / Conductor Routing | 107 |
| 10.1.4 / 10.1.5 / 10.1.6 / 10.2 / 10.2.1–10.2.5 / 10.3 | Conductor Spacing / Balanced Metallization / Plating Thieves / Land Characteristics / Manufacturing Allowances, Lands for Surface Mounting, Test Points, Orientation Symbols, Offset Lands / Large Conductive Areas | 108 |
| 11 / 11.1 | DOCUMENTATION / Special Tooling | 109 |
| 11.2 / 11.2.1–11.2.4 / 11.3 / 11.4 | Layout / Viewing, Accuracy and Scale, Layout Notes, Automated-Layout Techniques / Deviation Requirements / Phototool Considerations | 111 |
| 11.4.1 / 11.4.2 / 11.4.3 / 12 / 12.1 | Artwork Master Files / Film Base Material / Solder Mask Coating Phototools / QUALITY ASSURANCE / Conformance Test Coupons | 112 |
| 12.2 / 12.2.1 / 12.2.2 / 12.3 / 12.3.1 | Material Quality Assurance / Laminates / Compliant Pin / Conformance Evaluations / Coupon Quantity and Location | 113 |
| 12.3.2 | Coupon Identification | 115 |
| 12.3.3 / 12.3.3.1–12.3.3.4 / 12.4 / 12.4.1 / 12.4.1.1 / 12.4.1.2 / 12.4.2 / 12.4.2.1 | General Coupon Requirements / Tolerances, Etched Letters, Interlayer Connection Holes, Metal Cores / Individual Coupon Design / Plated Hole Evaluation Coupons / AB/R Coupon / Legacy A, B or A/B / MIR Coupons / E Coupon | 117 |
| 12.4.2.2 / 12.4.3 / 12.4.3.1 / 12.4.3.2 / 12.4.4 / 12.4.4.1 / 12.4.4.2 / 12.4.5 / 12.4.5.1 / 12.4.5.2 / 12.4.6 / 12.4.6.1 / 12.4.6.2 / 12.4.7 / 12.4.7.1 / 12.4.7.2 / 12.4.8 / 12.4.8.1 / 12.4.8.2 | Legacy E / Hole Solderability / S / Legacy S / SMT Solderability / W / Legacy M / Interconnect Resistance and Continuity / D / Legacy D / Solder Mask Adhesion / G / Legacy G / SIR / H / Legacy H / Peel Strength and Plating Adhesion / P / Legacy C | 118 |
| 12.4.9 / 12.4.9.1 / 12.4.10 / 12.4.11 / 12.4.12 / 12.4.13 | Controlled Impedance Coupons / Z Coupon / Optional Legacy Registration Coupons / Legacy N Coupon / Coupon X (Bending, Flex) / Process Control Test Coupon | 119 |
| App. A / App. B / App. C | Coupon Requirements / (Legacy) Coupon Requirements / Example of a Testability Design Checklist | 121 / 139 / 156 |

IPC-2221C tables (id → title → page): 3-1 Design/Performance Tradeoff Checklist 6 · 3-2 Component Grid Areas 19 · 4-1 Final Finish, Plating and Coating Requirements 26 · 4-2 Surface and Hole Cu Plating Min for Buried Vias > 2 Layers, Through-Holes, Blind Vias 27 · 4-3 Hole Cu Plating Min for Microvias 27 · 4-4 Hole Cu Plating Min for Buried Via Cores (2 layers) 27 · 4-5 Surface Finishes 28 · 4-6 Gold Plating Uses 29 · 4-7 ENIG adv/disadv 29 · 4-8 ENIG/EG 30 · 4-9 ENEPIG 30 · 4-10 Immersion Silver 31 · 4-11 Immersion Tin 31 · 4-12 OSP 32 · 4-13 Minimum Copper Foil/Film Recommendations 34 · 4-14 Metal Core Substrates 35 · 4-15 Typical Minimum Solder Mask Clearances and Dams 36 · 4-16 Conformal Coating Types and Thickness Range 37 · 4-17 Conformal Coating Functionality 37 · 5-1 Fabrication Assumptions 38 · 5-2 PC Card Substrate Dimensions 39 · 5-3 Typical Assembly Equipment Limits 43 · 6-1 Electrical Conductor Spacing 58 · 6-2 CTI Material Groups 60 · 6-3 Example Plane Sequences, Six Layer 62 · 6-4 Example Impedance Tolerances 63 · 7-1 Effects of Material Type on Construction 66 · 7-2 Emissivity Ratings 66 · 7-3 PB Heatsink Assembly Preferences 70 · 7-4 Comparative Reliability Matrix, Lead/Termination Attachment 70 · 9-1 Annular Rings (Minimum) 96 · 9-2 Pad to Plane Clearance 97 · 9-3 Feature Location Tolerances (DTP) 98 · 9-4 Minimum Hole Location Tolerance, DTP 102 · 9-5 Through-Hole Diameters Min/Max and Aspect Ratio 103 · 10-1 Internal Layer Foil Thickness After Processing 105 · 10-2 External Conductor Thickness After Plating 105 · 12-1 Appendix A Coupon Requirements 113 · 12-2 Appendix B Legacy Coupon Requirements 114 · A.1-1 IPC Coupons 121 · A.2-1 AB/R Parameters 122 · A.3-1 Propagated B 125 · A.4-1 E 126 · A.5-1 S 127 · A.6-1 W 128 · A.7-1 D 130 · A.8-1 G 134 · A.9-1 H 135 · A.10-1 P 136 · B.1-1 Legacy Coupons 139.

IPC-2221C figures worth citing: 1-1 Microvia Definition 2 · 1-2 Back-drilled Hole 2 · 3-1 Package Size and I/O Count 10 · 3-2/3-3 Test Land Free Area 17 · 3-4 Probing Test Lands 17 · 3-5 Usable Area Calculation 19 · 3-6 Density Evaluation 21 · 4-1 HASL Surface Topology 33 · 5-1 Board Size Standardization 40 · 5-2, 5-3A, 5-3B Constraining-Core 41 · 5-4 Positional vs Bilateral Tolerance 44 · 5-5 Datum Reference Frame 45 · 5-6 PTH Pattern Location 46 · 5-7 Tooling/Mounting Holes 46 · 5-8 Fiducials 47 · 5-9 Profile Location/Tolerance 48 · 5-10 GD&T Drawing 48 · 5-11 Fiducial Clearance 49 · 5-12 Panelization/Assembly Array 49 · 5-13 Connector Key Slot 50 · 5-14 X-Out Fiducials 51 · 5-15 Edge Plating Clearance 51 · 5-16 Common Nets Anchored to Edge 52 · 6-1 Voltage/Ground Distribution 53 · 6-2 Single Reference Edge Routing 54 · 6-3 Circuit Distribution 54 · 6-4 Minimum Dielectric Spacing Measurement 57 · 6-5 Transmission Line Construction 61 · 6-6 Microstrip Capacitance vs w, h 64 · 6-7 Stripline Capacitance vs w, s 64 · 6-8 Single Conductor Crossover 65 · 7-1 Component Clearance for Automatic Insertion 69 · 7-2 Relative CTE Comparison 71 · 8-1 Orientation for Wave Solder 75 · 8-2 Body Centering 75 · 8-3 Axial over Conductors 75 · 8-4 Uncoated Board Clearance 76 · 8-5 Clamp-Mounted Axial 76 · 8-6 Adhesive-Bonded Axial 76 · 8-7 Filleting vs Bonding 77 · 8-8 Feet/Standoffs 78 · 8-9 Heat Dissipation Examples 78 · 8-10 Lead Bends 79 · 8-11 Lead Configurations 79 · 8-12 Keying 82 · 8-13 Board Edge Tolerancing 82 · 8-14 Lead-In Chamfer 83 · 8-15 Two-Part Connector 83 · 8-16 Edge Adapter Connector 83 · 8-17 Round/Coined Lead Joint 84 · 8-18 Standoff Terminal Mounting 85 · 8-19 Dual Hole Terminal Mounting 85 · 8-20 Partially Clinched Leads 87 · 8-21 DIP Lead Bends 88 · 8-22 Solder in Lead Bend Radius 88 · 8-23/8-24 Radial Two-Lead 88 · 8-25 Meniscus Clearance 89 · 8-26 TO Can 89 · 8-27 Perpendicular Mounting 89 · 8-28..8-32 Flat-Packs / Metal Power Packages 89–90 · 8-33..8-38 SMT flat-pack, coined lead, heel mounting, TSSOP, ribbon leads, SQFP 91–93 · 8-39 BGA 94 · 8-40 CGA 94 · 8-41 LGA 94 · 8-42 QFN 94 · 8-43 SON 95 · 8-44 PQFN 95 · 9-1 Modified Land Shapes 95 · 9-2 External Annular Ring 96 · 9-3 Internal Annular Ring 96 · 9-4 Thermal Relief 97 · 9-5 Clearance Area in Planes 98 · 10-1 Etched Conductor Characteristics 106 · 10-2 Beef-Up / Neck-Down 107 · 10-3 Conductor Optimization Between Lands 107 · 10-4 Cross-hatched Large Layers 109 · 11-1 Design/Fabrication Sequence Flow Chart 110 · 11-2 Multilayer Viewing 111 · 11-3 Gang Solder Mask Window 111 · 11-4 Pocket Solder Mask Window 111 · 12-1/12-2 Panel Utilization Coupons 115–116 · 12-3 Ten-Layer Stack-up Example 116 · 12-4 SPC Implementation Path 119 · A.2-1..A.11-2 coupon layouts 123–137 · B.2-1..B.12-2 legacy coupon layouts and Bending Test 140–155 (B.10-3 Worst-Case Hole/Land Relationship 153).

### 2.7 IPC-6012F clause map (complete TOC)

| clause | title | p. |
|---|---|---|
| 1 / 1.1 / 1.2 / 1.2.1 | SCOPE / Statement of Scope / Purpose / Supporting Documentation | 1 |
| 1.3 / 1.3.1 / 1.3.1.1–1.3.1.4 / 1.3.2 | Performance Classification and Type / Classification / Requirement, Space, Medical, Automotive Deviations / Printed Board Type | 1 |
| 1.3.3 / 1.3.3.1 | Selection for Procurement / Selection (Default) | 2 |
| 1.3.3.2 / 1.3.4 / 1.3.4.1 / 1.3.4.2 | Selection System (Optional) / Material, Plating Process and Surface Finish / Laminate Material / Plating Process | 3 |
| 1.3.4.3 / 1.4 / 1.4.1 | Surface Finish and Coatings / Terms and Definitions / Back-Drilling | 4 |
| 1.4.2 / 1.4.3 / 1.4.4 / 1.4.5 / 1.5 / 1.6 / 1.7 | Stub (Plated Hole) / Back-drill Depth / Microvia / Design Data / Interpretation / Presentation / Design Data Protection | 5 |
| 2 / 2.1 | APPLICABLE DOCUMENTS / IPC | 6 |
| 2.2 / 2.3 / 2.4 / 2.4.2 / 2.4.3 / 2.4.4 / 2.4.5 / 2.4.6 / 2.4.7 / 3 / 3.1 | Joint Industry Standards / Federal / Other Publications / Underwriters Lab / NEMA / ASQ / AMS / ASME / SAE / REQUIREMENTS / General | 8 |
| 3.2 / 3.2.1 / 3.2.2 / 3.2.3 / 3.2.4 / 3.2.4.1 / 3.2.5 | Materials / Laminates and Bonding Material / External Bonding Materials / Other Dielectric Materials / Metal Foils / Resistive Metal / Metal Planes/Cores | 9 |
| 3.2.6 / 3.2.6.1 / 3.2.6.2 / 3.2.6.3 / 3.2.7 / 3.2.7.1 / 3.2.7.2 / 3.2.7.3 | Base Metallic Plating Depositions and Conductive Coatings / Electroless Cu / Electrodeposited Cu / Fully Additive Electroless Cu / Surface Finish Depositions and Coatings / ED Tin / ED Tin-Lead / HASL/Solder | 10 |
| 3.2.7.3.1 / 3.2.7.3.2 / 3.2.7.4 / 3.2.7.5 / 3.2.7.6 / 3.2.7.7 / 3.2.7.8 / 3.2.7.9 | Eutectic Tin-Lead Solder Coating / Pb-Free Solder Coating / ED Nickel / ED Gold / ENIG / ENEPIG / Immersion Silver (IAg) / Immersion Tin (ISn) | 11 |
| 3.2.7.10 / 3.2.7.11 | OSP / Other Metals and Coatings | 12 |
| 3.2.8 / 3.2.9 / 3.2.10 / 3.2.11 / 3.2.12 / 3.2.13 / 3.2.14 / 3.3 | Polymer Coating (Solder Mask) / Fusing Fluids and Fluxes / Marking Inks / Hole Fill Insulation Material / Heatsink Planes, External / Via Protection / Embedded Passive Materials / Visual Examination | 13 |
| 3.3.1 / 3.3.2 / 3.3.2.1–3.3.2.4 | Edges / Laminate Imperfections / Measling, Crazing, Delamination/Blistering, Foreign Inclusions | 14 |
| 3.3.2.5–3.3.2.10 / 3.3.3 / 3.3.4 / 3.3.5 / 3.3.5.1 | Weave Exposure, Mechanically Induced Disrupted Fibers, Scratches/Dents/Tool Marks, Surface Voids, Color Variations in Bond Enhancement, Pink Ring / Plating and Coating Voids in the Hole / Lifted Lands / Marking / Etched Marking | 15 |
| 3.3.5.2 / 3.3.5.3 / 3.3.6 / 3.3.7 / 3.3.8 | Ink Marking / Ink Marking Adhesion / Solderability / Plating Adhesion / Edge Board Contact, Junction of Gold Plate to Solder Finish | 16 |
| 3.3.9 / 3.3.10 | Back-Drilled Holes / Printed Board Cavities | 17 |
| 3.3.11 / 3.4 / 3.4.1 / 3.4.2 | Workmanship / Printed Board Dimensional Requirements / Hole Size, Hole Pattern Accuracy and Pattern Feature Accuracy / Annular Ring and Breakout (External) | 18 |
| 3.4.3 / 3.5 / 3.5.1 / 3.5.2 / 3.5.3 / 3.5.3.1 / 3.5.3.2 / 3.5.4 / 3.5.4.1 / 3.5.4.2 | Bow and Twist / Conductor Definition / Conductor Width and Thickness / Conductor Spacing / Conductor Imperfections / Width Reduction / Thickness Reduction / Conductive Surfaces / Nicks and Pinholes in Ground or Voltage Planes / Solderable Surface Mount Lands | 21 |
| 3.5.4.2.1 / 3.5.4.2.2 / 3.5.4.3 / 3.5.4.4 | Rectangular SMT Lands / Round SMT Lands (BGA Pads) / Wire Bond Pad (WBP) / Board Edge Connector Lands | 22 |
| 3.5.4.5 / 3.5.4.6 / 3.5.4.7 / 3.5.4.7.2 / 3.5.4.8 / 3.5.4.9 / 3.5.4.10 / 3.6 | Dewetting / Nonwetting / Surface Finish Coverage / Tin-Lead under Solder Mask / Cap Plating of Filled Holes / Copper Filled Microvias / Nonfunctional Lands / Structural Integrity | 23 |
| 3.6.1 / 3.6.1.1 / 3.6.1.1.1 / 3.6.1.2 / 3.6.1.3 / 3.6.1.4 / 3.6.2 | Thermal Stress Testing / Method 2.6.8 / Method 2.6.8 (Microvias) / Method 2.6.27 (230 °C) / Method 2.6.27 (260 °C) / Deviations to Thermal Stress Testing / Requirements for Microsectioned Coupons or Printed Boards | 24 |
| 3.6.2.1 | Plating Integrity | 25 |
| 3.6.2.2 | Copper Plating Voids | 26 |
| 3.6.2.3 / 3.6.2.4 / 3.6.2.5 | Laminate Voids / Laminate Cracks / Delamination or Blistering | 27 |
| 3.6.2.6 / 3.6.2.6.1 / 3.6.2.6.2 | Etchback / Evidence of Etchback (When Specified) / Copper Penetration | 28 |
| 3.6.2.7 / 3.6.2.8 / 3.6.2.9 / 3.6.2.9.1 | Smear Removal / Negative Etchback / Annular Ring and Breakout in a Microsection Evaluation / External | 29 |
| 3.6.2.9.2 | Annular Ring and Breakout (Internal) | 30 |
| 3.6.2.9.2.1 / 3.6.2.9.2.2 / 3.6.2.10 / 3.6.2.11 | Breakout (Internal) Conditions / Microvia to Target Land / Lifted Lands / Hole Copper Plating | 31 |
| 3.6.2.11.1 / 3.6.2.11.2 | Copper Wrap Plating / Copper Cap Plating of Filled Holes | 33 |
| 3.6.2.11.3 | Plated Copper Filled Vias (Through, Blind, Buried and Microvia) | 35 |
| 3.6.2.12 | Microvia Target Land Contact Dimension | 36 |
| 3.6.2.13 / 3.6.2.14 | Microvia Target Land Piercing / Minimum Internal Layer Copper Foil Thickness | 37 |
| 3.6.2.14.1 / 3.6.2.15 | Plated Internal Layers / Minimum Surface Conductor Thickness | 38 |
| 3.6.2.16 / 3.6.2.17 / 3.6.2.18 / 3.6.2.18.1 / 3.6.2.19 | Overhang / Metal Cores / Dielectric Spacing / Minimum Dielectric Spacing / Material Fill of Through, Blind, Buried and Microvia Structures | 39 |
| 3.6.2.20 / 3.6.2.21 / 3.7 / 3.7.1 | Back-Drilled Holes (Microsection Evaluation) / Nail Heading / Solder Mask Requirements / Solder Mask Coverage | 40 |
| 3.7.2 | Solder Mask Cure and Adhesion | 41 |
| 3.7.3 / 3.8 / 3.8.1 / 3.8.2 / 3.8.3 / 3.8.4 / 3.8.4.1 | Solder Mask Thickness / Electrical Requirements / DWV / Electrical Continuity and Isolation Resistance / Circuit/Plated Hole Shorts to Metal Substrate / MIR / DWV After MIR | 42 |
| 3.9 / 3.9.1 / 3.9.2 / 3.9.3 / 3.10 / 3.10.1 / 3.10.2 / 3.10.3 / 3.10.4 / 3.10.5 / 3.10.6 / 3.10.7 | Cleanliness / Prior to Solder Mask / After Solder Mask, Solder, or Alternative Surface Coating / Inner Layers After Oxide Treatment / Special Requirements / Outgassing / Fungus Resistance / Vibration / Mechanical Shock / Impedance Testing / CTE / Thermal Shock | 43 |
| 3.10.8–3.10.17 | SIR (As Received) / Metal Core (Horizontal Microsection) / Rework Simulation (TH 3.10.10.1, SMT 3.10.10.2) / Bond Strength, Unsupported Component Hole Land / Destructive Physical Analysis / Peel Strength (Foil Laminated Construction Only) / Design Data Protection / Performance Based Testing for Microvia Structures / CAF Migration / Wire Bond Pad Surface Roughness | 44 |
| 3.11 / 3.11.1 / 3.12 / 4 / 4.1 / 4.1.1 / 4.1.2 | Repair / Circuit Repairs / Rework / QUALITY ASSURANCE PROVISIONS / General / Qualification / Sample Test Coupons | 45 |
| 4.2 / 4.2.1 / 4.2.2 / 4.3 / 4.3.1 | Acceptance Tests / C=0 Zero Acceptance Number Sampling Plan / Referee Tests / Periodic Quality Conformance Testing / Coupon Selection | 46 |
| 5 / 5.1 / 5.2 | NOTES / Ordering Data / Superseded Specifications | 52 |

IPC-6012F tables: 1-1 Technology Adders 2 · 1-2 Default Requirements 2 · 3-1 Metal Planes/Cores 10 · 3-2 Maximum Limits of Solder Bath Contaminant 11 · 3-3 Final Finish, Plating and Coating Requirements 12 · 3-4 Plating and Coating Voids in the Hole 15 · 3-5 Edge Printed Board Contact Gap 16 · 3-6 Plating and Coating Voids in the Cavity Wall(s) 17 · 3-7 Minimum Annular Ring 19 · 3-8 Plated Hole Integrity After Stress 26 · 3-9 Negative Etchback Allowance 29 · 3-10 Surface and Hole Cu Plating Min — Buried Vias > 2 Layers, Through-Holes, Blind Vias 32 · 3-11 Hole Cu Plating Min — Microvias (Blind and Buried) 32 · 3-12 Hole Cu Plating Min — Buried Cores (2 layers) 32 · 3-13 Cap Plating Requirements for Filled Holes 33 · 3-14 Depression and Protrusions in Copper Filled Microvias 35 · 3-15 Microvia Contact Dimension (Laser Drilled) 37 · 3-16 Microvia Contact Dimension (Mechanically Drilled) 37 · 3-17 Internal Layer Copper Thickness after Processing 38 · 3-18 Thickness of External Conductor after Plating 38 · 3-19 Solder Mask Adhesion 41 · 3-20 Dielectric Withstanding Voltages 42 · 3-21 Insulation Resistance 42 · 4-1 Qualification Test Coupons 45 · 4-2 C=0 Sampling Plan per Lot Size 47 · 4-3 Acceptance Testing and Frequency 47 · 4-4 Periodic Quality Conformance Testing 52.

IPC-6012F figures: 1-1 Back-drilled Hole 5 · 1-2 Shallow Back-drill 5 · 1-3 Microvia Definition 5 · 3-1 Printed Board Cavities (Type 2 left, Type 3 right) 18 · 3-2 Annular Ring Measurement (External) 20 · 3-3 Breakout of 90° and 180° 20 · 3-4 External Conductor Width Reduction 20 · 3-5 Intermediate Target Land in a Microvia 20 · 3-6 Rectangular SMT Lands 21 · 3-7 Round SMT Lands 22 · 3-8 Edge Connector Lands 22 · 3-9 Dewetting 23 · 3-10 Edge Pull Back 23 · 3-11 Plated Hole Microsection (Grinding/Polishing) Tolerance 25 · 3-12 Plating to Target Land Separation 25 · 3-13 Copper Crack Definition 27 · 3-14 Separations at External Foil 27 · 3-15 Plating Folds/Inclusions – Minimum Measurement Points 28 · 3-16 Thermal Zones for Microsection Evaluation of Laminate Attributes 28 · 3-17 Etchback Measurement 29 · 3-18 Copper Penetration Measurement 29 · 3-19 Negative Etchback Measurement 30 · 3-20 Annular Ring (External, Filled, Microsection) 30 · 3-21 Annular Ring (Internal) 30 · 3-22 Microsection Rotations for Breakout Detection 31 · 3-23 Comparison of Microsection Rotations 31 · 3-24 Non-Conforming Dielectric Spacing Reduction Due to Breakout at Microvia Target Land 31 · 3-25 Measurement Locations for Hole Copper Plating 32 · 3-26 Surface Copper Wrap, Filled Holes (Over Foil) 33 · 3-27 Surface Copper Wrap, Filled (Over Laminate) 33 · 3-28 Surface Copper Wrap, Non-Filled 33 · 3-29 Wrap Copper (Acceptable) 34 · 3-30 Wrap Copper Removed by Excessive Processing (Not Acceptable) 34 · 3-31 Copper Cap Thickness 34 · 3-32 Cap Filled Via Height (Bump) 34 · 3-33 Cap Depression (Dimple) 35 · 3-34 Cap Plating Voids 35 · 3-35 Nonconforming Via Fill Between Cap Layers 35 · 3-36 Acceptable Via Fill Between Cap Layers 35 · 3-37 Acceptable Voiding, Cap Plated Cu Filled Via 36 · 3-38 Acceptable Voiding, Cu Filled Microvia without Cap 36 · 3-39 Nonconforming Void, Cap Plated Cu Filled Microvia 36 · 3-40 Nonconforming Void, Cu Filled Microvia 36 · 3-41 Microvia Contact Dimension 36 · 3-42 Exclusion of Separations in Contact Dimension 36 · 3-43 Unintended Piercing of Target Land (Laser) 37 · 3-45 Overhang 39 · 3-46 Metal Core to Plated Hole Spacing 39 · 3-47 Measurement of Minimum Dielectric Spacing 39 · 3-48 Fill Material in Blind/Through Vias When Cap Plating Not Specified 40 · 3-49 Void in Fill Material at Hole Wall Interface 40.

### 2.8 J-STD-001E clause map (complete TOC)

| clause | title | p. |
|---|---|---|
| 1 / 1.1 / 1.2 / 1.3 / 1.4 / 1.4.1 | GENERAL / Scope / Purpose / Classification / Measurement Units and Applications / Verification of Dimensions | 1 |
| 1.5 / 1.5.1 / 1.5.2 / 1.6 | Definition of Requirements / Hardware Defects and Process Indicators / Material and Process Nonconformance / General Requirements | 2 |
| 1.7 / 1.7.1 / 1.7.2 / 1.7.3 / 1.8 / 1.8.1–1.8.6 | Order of Precedence / Conflict / Clause References / Appendices / Terms and Definitions / Defect, Disposition, Electrical Clearance, High Voltage, Manufacturer (Assembler), Objective Evidence | 3 |
| 1.8.7–1.8.15 / 1.9 / 1.10 / 1.11 | Process Control, Process Indicator, Proficiency, Solder Destination Side, Solder Source Side, Supplier, User, Wire Overwrap, Wire Overlap / Requirements Flowdown / Personnel Proficiency / Acceptance Requirements | 4 |
| 1.12 / 1.13 / 1.13.1 / 1.13.2 / 2 / 2.1 / 2.2 | General Assembly Requirements / Miscellaneous Requirements / Health and Safety / Procedures for Specialized Technologies / APPLICABLE DOCUMENTS / EIA / IPC | 5 |
| 2.3 / 2.4 / 2.5 / 3 / 3.1 | Joint Industry Standards / ASTM / ESD Association / MATERIALS, COMPONENTS AND EQUIPMENT REQUIREMENTS / Materials | 6 |
| 3.2 / 3.2.1 / 3.2.2 / 3.3 | Solder / Solder – Lead Free / Solder Purity Maintenance / Flux | 7 |
| 3.3.1 / 3.4 / 3.5 / 3.6 / 3.7 / 3.8 / 3.8.1 / 3.8.2 / 3.9 / 4 / 4.1 / 4.2 / 4.2.1 / 4.2.2 | Flux Application / Solder Paste / Solder Preforms / Adhesives / Chemical Strippers / Components / Component and Seal Damage / Coating Meniscus / Soldering Tools and Equipment / GENERAL SOLDERING AND ASSEMBLY REQUIREMENTS / ESD / Facilities / Environmental Controls / Temperature and Humidity | 8 |
| 4.2.3 / 4.2.4 / 4.3 / 4.4 / 4.5 / 4.5.1 / 4.5.2 / 4.6 / 4.7 | Lighting / Field Assembly Operations / Solderability / Solderability Maintenance / Removal of Component Surface Finishes / Gold Removal / Other Metallic Surface Finishes Removal / Thermal Protection / Rework of Nonsolderable Parts | 9 |
| 4.8 / 4.9 / 4.9.1 / 4.10 / 4.11 / 4.12 / 4.13 / 4.14 / 4.15 / 4.15.1 / 4.15.2 / 4.15.3 | Presoldering Cleanliness / General Part Mounting / Stress Relief / Hole Obstruction / Metal-Cased Component Isolation / Adhesive Coverage Limits / Mounting of Parts on Parts (Stacking) / Connectors and Contact Areas / Handling of Parts / Preheating / Controlled Cooling / Drying/Degassing | 10 |
| 4.15.4 / 4.16 / 4.16.1 / 4.16.2 / 4.17 / 4.17.1 / 4.18 | Holding Devices and Materials / Machine (Nonreflow) Soldering / Machine Controls / Solder Bath / Reflow Soldering / Intrusive Soldering (Paste-in-Hole) / Solder Connection | 11 |
| 4.18.1 / 4.18.2 / 4.18.3 / 4.19 / 5 / 5.1 / 5.1.1 | Exposed Surfaces / Solder Connection Defects / Partially Visible or Hidden Solder Connections / Heat Shrinkable Soldering Devices / WIRES AND TERMINAL CONNECTIONS / Wire and Cable Preparation / Insulation Damage | 12 |
| 5.1.2 / 5.1.3 / 5.2 / 5.3 / 5.3.1 / 5.3.2 | Strand Damage / Tinning of Stranded Wire / Solder Terminals / Bifurcated, Turret and Slotted Terminal Installation / Shank Damage / Flange Damage | 13 |
| 5.3.3 / 5.3.4 / 5.3.5 | Flared Flange Angles / Terminal Mounting – Mechanical / Terminal Mounting – Electrical | 14 |
| 5.3.6 / 5.4 / 5.4.1 | Terminal Soldering / Mounting to Terminals / General Requirements | 15 |
| 5.4.2 | Bifurcated and Turret Terminals | 16 |
| 5.4.3 / 5.4.4 | Slotted Terminals / Hook Terminals | 18 |
| 5.4.5 / 5.4.6 / 5.5 / 5.5.1 | Pierced or Perforated Terminals / Cup and Hollow Cylindrical Terminals / Soldering to Terminals / Cup and Hollow Cylindrical Terminals | 19 |
| 6 / 6.1 / 6.1.1 / 6.1.2 / 6.1.3 | THROUGH-HOLE MOUNTING AND TERMINATIONS / General / Lead Forming / Lead Deformation Limits / Termination Requirements | 20 |
| 6.1.4 / 6.1.5 / 6.1.6 / 6.2 / 6.2.1 / 6.2.2 | Lead Trimming / Interfacial Connections / Coating Meniscus In Solder / Supported Holes / Solder Application / Through-Hole Component Lead Soldering | 21 |
| 6.3 / 6.3.1 | Unsupported Holes / Lead Termination Requirements for Unsupported Holes | 22 |
| 7 / 7.1 / 7.1.1 / 7.1.2 | SURFACE MOUNTING OF COMPONENTS / SMD Lead Forming / Lead Deformation Limits / Flat Pack Parallelism | 23 |
| 7.1.3 / 7.1.4 / 7.1.5 / 7.1.6 / 7.2 / 7.2.1 / 7.3 / 7.4 / 7.5 / 7.5.1 / 7.5.2 | SMD Lead Bends / Flattened Leads / DIPs / Parts Not Configured for SMT / Leaded Component Body Clearance / Axial-Leaded / Butt Lead Mounting / Hold Down of SMT Leads / Soldering Requirements / Misaligned Components / Unspecified and Special Requirements | 24 |
| 7.5.3 | Bottom Only Terminations | 26 |
| 7.5.4 | Rectangular or Square End Chip Components – 1, 3 or 5 Side Termination | 27 |
| 7.5.5 | Cylindrical End Cap Terminations | 28 |
| 7.5.6 | Castellated Terminations | 29 |
| 7.5.7 | Flat Gull Wing Leads | 30 |
| 7.5.8 | Round or Flattened (Coined) Gull Wing Leads | 31 |
| 7.5.9 | "J" Leads | 32 |
| 7.5.10 | Butt/I Connections (Not Permitted for Class 3 Products) | 33 |
| 7.5.11 | Flat Lug Leads | 34 |
| 7.5.12 | Tall Profile Components Having Bottom Only Terminations | 35 |
| 7.5.13 | Inward Formed L-Shaped Ribbon Leads | 36 |
| 7.5.14 | Surface Mount Area Array Packages | 37 |
| 7.5.15 | Bottom Termination Components (BTC) | 39 |
| 7.5.16 | Components with Bottom Thermal Plane Terminations (D-Pak) | 40 |
| 7.5.17 / 7.6 | Flattened Post Connections / Specialized SMT Terminations | 41 |
| 8 / 8.1 / 8.2 / 8.3 / 8.3.1 / 8.3.2 / 8.3.3 / 8.3.4 / 8.3.5 | CLEANING PROCESS REQUIREMENTS / Cleanliness Exemptions / Ultrasonic Cleaning / Post-Solder Cleanliness / Particulate Matter / Flux Residues and Other Ionic or Organic Contaminants / Post-Soldering Cleanliness Designator / Cleaning Option / Test for Cleanliness | 42 |
| 8.3.6 / 9 / 9.1 / 9.1.1 | Testing / PCB REQUIREMENTS / Printed Circuit Board Damage / Blistering/Delamination | 43 |
| 9.1.2–9.1.10 / 9.2 / 9.3 | Weave Exposure/Cut Fibers, Haloing, Land Separation, Land/Conductor Reduction in Size, Flexible Circuitry Delamination, Flexible Circuitry Damage, Burns, Solder on Gold Contacts, Measles / Marking / Bow and Twist (Warpage) | 44 |
| 10 / 10.1 / 10.1.1 / 10.1.2 | COATING, ENCAPSULATION AND STAKING / Conformal Coating / Application / Performance Requirements | 45 |
| 10.1.3 / 10.1.4 / 10.2 / 10.2.1–10.2.4 / 10.3 | Conformal Coating Inspection / Rework of Conformal Coating / Encapsulation / Application, Performance, Rework, Inspection / Staking (Adhesive) | 46 |
| 10.3.1 / 10.3.2 | Staking / Staking (Inspection) | 47 |
| 11 / 11.1 / 11.2 / 11.2.1 / 11.2.2 / 11.2.3 / 11.3 | PRODUCT ASSURANCE / Hardware Defects Requiring Disposition / Inspection Methodology / Process Verification Inspection / Visual Inspection / Sampling Inspection / Process Control Requirements | 48 |
| 11.3.1 / 11.4 / 12 / 12.1 / 12.2 / 12.3 | Opportunities Determination / Statistical Process Control / REWORK AND REPAIR / Rework / Repair / Post Rework/Repair Cleaning | 49 |
| App. A / App. B | Guidelines for Soldering Tools and Equipment / Minimum Electrical Clearance – Electrical Conductor Spacing | 51 / 53 |

J-STD-001E tables: 1-1 Design and Fabrication Specification 3 · 3-1 Maximum Limits of Solder Bath Contaminant 7 · 5-1 Allowable Strand Damage 13 · 5-2 Terminal Soldering Requirements 15 · 5-3 Turret and Straight Pin Wire Placement 16 · 5-4 AWG 30 and Smaller Wire Wrap Requirements 17 · 5-5 Bifurcated Terminal Wire Placement – Side Route 17 · 5-6 Staking Requirements of Side Route Straight Through Connections 17 · 5-7 Bifurcated – Bottom Route 18 · 5-8 Hook Terminal Wire Placement 18 · 5-9 Pierced/Perforated Wire Placement 19 · 5-10 Solder Requirements Wire to Post 19 · 6-1 Lead Bend Radius 20 · 6-2 Protrusion of Leads in Supported Holes 21 · 6-3 Protrusion in Unsupported Holes 21 · 6-4 Supported Holes with Component Leads, Minimum Acceptable Conditions 22 · 6-5 Unsupported Holes, Minimum Acceptable Conditions 22 · 7-1 SMT Lead Forming Minimum Lead Length 23 · 7-2 Surface Mount Components 25 · 7-3 Dimensional Criteria – Bottom Only Terminations 26 · 7-4 Rectangular/Square End Chip 1, 3 or 5 Side 27 · 7-5 Cylindrical End Cap 28 · 7-6 Castellated 29 · 7-7 Flat Gull Wing 30 · 7-8 Round/Coined Gull Wing 31 · 7-9 J Leads 32 · 7-10 Butt/I 33 · 7-11 Flat Lug 34 · 7-12 Tall Profile Bottom Only 35 · 7-13 Inward Formed L-Shaped Ribbon 36 · 7-14 BGA with Collapsing Balls 37 · 7-15 BGA with Noncollapsing Balls 38 · 7-16 Column Grid Array 38 · 7-17 BTC 39 · 7-18 Bottom Thermal Plane 40 · 7-19 Flattened Post 41 · 8-1 Designation of Surfaces to be Cleaned 42 · 8-2 Cleanliness Testing Designators 42 · 10-1 Coating Thickness 45 · 11-1 Magnification Aid Applications for Solder Connections 48 · 11-2 Magnification Aid Applications – Other 48. Figures: 1-1 Overwrap 4 · 1-2 Overlap 4 · 4-1 Hole Obstruction 10 · 4-2 Acceptable Wetting Angles 11 · 5-1 Flange Damage 14 · 5-2 Flare Angles 14 · 5-3/5-4 Terminal Mounting Mechanical/Electrical 14 · 5-5 Insulation Clearance Measurement 15 · 5-6 Service Loop 15 · 5-7 Stress Relief Examples 15 · 5-8 Continuous Runs 16 · 5-9 Wire and Lead Wrap Around 16 · 5-10 Side Route Connections, Bifurcated 17 · 5-11 Top and Bottom Route 18 · 5-12 Hook 18 · 5-13 Pierced/Perforated Wire Wrap 19 · 5-14 Solder Height 19 · 6-1 Lead Bends 20 · 6-2 Lead Trimming 21 · 6-3 Vertical Fill Example 22 · 7-1/7-2 SMD Lead Forming 23 · 7-3..7-17 termination-family figures 26–41 (7-14 BGA Solder Ball Spacing 37).

### 2.9 IPC-A-610J clause map (complete TOC; pages are chapter-page)

| clause | title | p. |
|---|---|---|
| 1.0 / 1.1 | General / Scope | 1-1 |
| 1.2 / 1.3 / 1.4 / 1.4.1 / 1.5 | Purpose / Classification / Measurement Units and Applications / Verification of Dimensions / Requirements | 1-2 |
| 1.5.1 / 1.5.1.1 / 1.5.1.2 / 1.5.1.2.1 / 1.5.1.3 / 1.5.1.4 / 1.5.1.5 / 1.5.1.6 / 1.6 | Acceptance Criteria / Acceptable / Defect / Disposition / Process Indicator / Conditions Not Specified / Specialized Designs / Should / Process Control Methodologies | 1-3 |
| 1.7 / 1.7.1 / 1.7.2 / 1.8 / 1.8.1 / 1.8.1.1–1.8.1.4 / 1.8.2 / 1.8.2.1 / 1.8.3 / 1.8.4 / 1.8.5 / 1.8.6 | Order of Precedence / Clause References / Appendices / Terms and Definitions / Board Orientation / Primary Side, Secondary Side, Solder Source Side, Solder Destination Side / Bubble / Bridging Bubble / Cold Solder Connection / Common Conductors / Conductor Overlap / Conductor Overwrap | 1-4 |
| 1.8.7–1.8.22 | Diameter / Electrical Clearance (1.8.8) / Engineering Documentation / FOD / Form, Fit, Function / High Voltage / Intrusive Solder / Kink / Locking Mechanism / Manufacturer / Meniscus (Component) / Noncommon Conductors / Nonfunctional Land / Pin-in-Paste / Solder Balls / Standard Industry Practice (SIP) | 1-5 |
| 1.8.23–1.8.26 / 1.9 / 1.10 / 1.11 / 1.11.1 / 1.11.2 | Stress Relief / Supplier / Tempered Leads / User / Requirements Flowdown / Personnel Proficiency / Acceptance Requirements / Missing Parts and Components / Jumper Wire or Z-Wire | 1-6 |
| 1.12 | Minimum Electrical Clearance (MEC) | 1-7 |
| 1.13 / 1.13.1 / 1.13.2 | Inspection Methodology / Lighting / Magnification Aids | 1-9 |
| 2.0 / 2.1 | Applicable Documents / IPC Documents | 2-1 |
| 2.2 / 2.3 / 2.4 / 2.5 | Joint Industry Documents / Electrostatic Association Documents / IEC Documents / ASTM | 2-2 |
| 2.6 / 2.7 | Military Standards / SAE International | 2-3 |
| 3.0 | Handling Electronic Assemblies | 3-1 |
| 4.0 | Hardware | 4-1 |
| 4.1 / 4.1.1 | Hardware Installation / Electrical Clearance | 4-2 |
| 4.1.2 | Interference | 4-3 |
| 4.1.3 | Component Mounting – High Power | 4-4 |
| 4.1.4 / 4.1.4.1 | Heatsinks / Insulators and Thermal Compounds | 4-6 |
| 4.1.4.2 | Heatsinks – Contact | 4-7 |
| 4.1.5 | Threaded Fasteners and Other Threaded Hardware | 4-8 |
| 4.1.5.1 | Threaded Fasteners – Torque | 4-10 |
| 4.1.5.2 | Threaded Fasteners – Solid Wires | 4-12 |
| 4.1.5.3 | Threaded Fasteners – Stranded Wires | 4-14 |
| 4.2 | Jackpost Mounting | 4-15 |
| 4.3 / 4.3.1 / 4.3.2 | Connector Pins / Edge Connector Pins / Press Fit Pins | 4-16 |
| 4.3.2.1 | Press Fit Pins – Land/Annular Ring | 4-18 |
| 4.3.2.2 | Press Fit Pins – Soldering | 4-19 |
| 4.4 / 4.5 | Wire Bundle Securing / Routing – Wires and Wire Bundles | 4-20 |
| 5.0 | Soldering | 5-1 |
| 5.1 | Soldering Acceptability Requirements | 5-2 |
| 5.2 / 5.2.1 | Soldering Anomalies / Exposed Basis Metal | 5-3 |
| 5.2.2 | Pin Holes/Blow Holes/Voids | 5-5 |
| 5.2.3 | Reflow of Solder Paste | 5-6 |
| 5.2.4 | Nonwetting | 5-7 |
| 5.2.5 / 5.2.6 | Cold Connection / Dewetting | 5-8 |
| 5.2.7 | Excess Solder | 5-9 |
| 5.2.7.1 | Excess Solder – Solder Balls | 5-10 |
| 5.2.7.2 | Excess Solder – Bridging | 5-11 |
| 5.2.7.3 | Excess Solder – Solder Webbing/Splashes | 5-12 |
| 5.2.8 | Disturbed Solder | 5-13 |
| 5.2.9 | Cooling Lines and Secondary Reflow | 5-14 |
| 5.2.10 | Fractured Solder | 5-15 |
| 5.2.11 | Solder Projections | 5-16 |
| 5.2.12 | Pb-Free Fillet Lift | 5-17 |
| 5.2.13 | Pb-Free Hot Tear/Shrink Hole | 5-18 |
| 5.2.14 | Probe Marks and Other Similar Surface Conditions in Solder Joints | 5-19 |
| 5.2.15 / 5.3 | Inclusions / Partially Visible or Hidden Solder Connections | 5-20 |
| 5.4 | Heat Shrinkable Soldering Devices | 5-21 |
| 6.0 | Terminal Connections | 6-1 |
| 6.1 / 6.1.1 / 6.1.1.1 | Swaged Hardware / Terminals / Terminal Base to Land Separation | 6-2 |
| 6.1.1.2 | Terminals – Turret | 6-4 |
| 6.1.1.3 | Terminals – Bifurcated | 6-5 |
| 6.1.2 | Rolled Flange | 6-6 |
| 6.1.3 | Flared Flange | 6-7 |
| 6.1.4 | Controlled Split | 6-8 |
| 6.1.5 | Swaged Hardware – Solder | 6-9 |
| 6.2 / 6.2.1 / 6.2.1.1 | Insulation / Damage / Damage – Presolder | 6-11 |
| 6.2.1.2 | Damage – Post-Solder | 6-13 |
| 6.2.2 | Insulation – Clearance | 6-14 |
| 6.2.3 / 6.2.3.1 | Insulation Sleeving / Placement | 6-16 |
| 6.2.3.2 | Insulation Sleeving – Damage | 6-18 |
| 6.3 / 6.3.1 | Conductor / Deformation | 6-19 |
| 6.3.2 / 6.3.2.1 | Damage / Damage – Stranded Wire | 6-20 |
| 6.3.2.2 / 6.3.3 | Damage – Solid Wire / Strand Separation (Birdcaging) – Presolder | 6-21 |
| 6.3.4 | Strand Separation (Birdcaging) – Post-Solder | 6-22 |
| 6.3.5 | Conductor – Tinning | 6-23 |
| 6.4 | Service Loops | 6-25 |
| 6.5 | Routing – Wires and Wire Bundles – Bend Radius | 6-26 |
| 6.6 / 6.6.1 | Stress Relief / Stress Relief – Wire | 6-27 |
| 6.7 | Lead/Conductor Placement – General Requirements | 6-29 |
| 6.8 | Solder – General Requirements | 6-30 |
| 6.9 / 6.9.1 | Turrets and Straight Pins / Conductor Placement | 6-32 |
| 6.9.2 | Turrets and Straight Pins – Solder | 6-34 |
| 6.10 / 6.10.1 | Bifurcated / Conductor Placement – Side Route Attachments | 6-35 |
| 6.10.2 | Bifurcated – Staked Wires | 6-37 |
| 6.10.3 | Bifurcated – Bottom and Top Route Attachments | 6-38 |
| 6.10.4 | Bifurcated – Solder | 6-39 |
| 6.11 / 6.11.1 | Slotted / Conductor Placement | 6-41 |
| 6.11.2 | Slotted – Solder | 6-42 |
| 6.12 / 6.12.1 | Pierced/Perforated / Conductor Placement | 6-43 |
| 6.12.2 | Pierced/Perforated – Solder | 6-45 |
| 6.13 / 6.13.1 | Hook / Conductor Placement | 6-46 |
| 6.13.2 | Hook – Solder | 6-48 |
| 6.14 / 6.14.1 | Solder Cups / Conductor Placement | 6-49 |
| 6.14.2 | Solder Cups – Solder | 6-50 |
| 6.15 | AWG 30 and Smaller Diameter Wires – Conductor Placement | 6-52 |
| 6.16 | Series Connected | 6-54 |
| 6.17 | Edge Clip – Position | 6-55 |
| 7.0 / 7.1 / 7.1.1 | Through-Hole Technology / Component Mounting / Orientation | 7-1 |
| 7.1.1.1 | Orientation – Horizontal | 7-2 |
| 7.1.1.2 | Orientation – Vertical | 7-3 |
| 7.1.2 / 7.1.2.1 | Lead Forming / Bend Radius | 7-4 |
| 7.1.2.2 | Lead Forming – Space between Seal/Weld and Bend | 7-5 |
| 7.1.2.3 | Lead Forming – Stress Relief | 7-6 |
| 7.1.2.4 | Lead Forming – Damage | 7-8 |
| 7.1.3 | Leads Crossing Conductors | 7-9 |
| 7.1.4 | Hole Obstruction | 7-10 |
| 7.1.5 | DIP/SIP Devices and Sockets | 7-11 |
| 7.1.6 | Radial Leads – Vertical | 7-13 |
| 7.1.6.1 | Radial Leads – Vertical – Spacers | 7-14 |
| 7.1.7 | Radial Leads – Horizontal | 7-15 |
| 7.1.8 | Connectors | 7-16 |
| 7.1.8.1 | Connectors – Right Angle | 7-17 |
| 7.1.8.2 | Connectors – Vertical Shrouded Pin Headers and Vertical Receptacle Connectors | 7-18 |
| 7.2 / 7.2.1 | Component Securing / Mounting Clips | 7-19 |
| 7.2.2 | Adhesive Bonding | 7-20 |
| 7.2.2.1 | Adhesive Bonding – Nonelevated Components | 7-21 |
| 7.2.2.2 | Adhesive Bonding – Elevated Components | 7-24 |
| 7.2.3 | Component Securing – Other Devices | 7-27 |
| 7.3 / 7.3.1 | Supported Holes / Axial Leaded – Horizontal | 7-28 |
| 7.3.2 | Axial Leaded – Vertical | 7-29 |
| 7.3.3 | Leads/Conductors Protrusion | 7-31 |
| 7.3.4 | Lead/Conductor Clinches | 7-32 |
| 7.3.5 | Supported Holes – Solder | 7-33 |
| 7.3.5.1 | Solder – Vertical Fill (A) | 7-36 |
| 7.3.5.2 | Solder Destination Side – Lead to Barrel (B) | 7-38 |
| 7.3.5.3 | Solder Destination Side – Land Area Coverage (C) | 7-40 |
| 7.3.5.4 | Solder Source Side – Lead to Barrel (D) | 7-41 |
| 7.3.5.5 | Solder Source Side – Land Area Coverage (E) | 7-42 |
| 7.3.5.6 | Solder Conditions – Solder in Lead Bend | 7-43 |
| 7.3.5.7 | Solder Conditions – Touching Through-Hole Component Body | 7-44 |
| 7.3.5.8 | Solder Conditions – Meniscus in Solder | 7-45 |
| 7.3.5.9 | Lead Cutting After Soldering | 7-47 |
| 7.3.5.10 | Coated Wire Insulation in Solder | 7-48 |
| 7.3.5.11 | Interfacial Connection without Lead – Vias | 7-49 |
| 7.3.5.12 | Board in Board | 7-50 |
| 7.4 / 7.4.1 | Unsupported Holes / Axial Leads – Horizontal | 7-53 |
| 7.4.2 | Axial Leads – Vertical | 7-54 |
| 7.4.3 | Wire/Lead Protrusion | 7-55 |
| 7.4.4 | Wire/Lead Clinches | 7-56 |
| 7.4.5 | Unsupported Holes – Solder | 7-58 |
| 7.4.6 | Lead Cutting After Soldering | 7-60 |
| 8.0 | Surface Mount Assemblies | 8-1 |
| 8.1 / 8.1.1 | Staking Adhesive / Component Bonding | 8-2 |
| 8.1.2 | Staking Adhesive – Mechanical Strength | 8-3 |
| 8.2 / 8.2.1 / 8.2.2 | SMT Leads / Plastic Components / Damage | 8-5 |
| 8.2.3 / 8.3 | SMT Leads – Flattening / SMT Connections | 8-6 |
| 8.3.1 | Chip Components – Bottom Only Terminations | 8-7 |
| 8.3.1.1 | Bottom Only – Side Overhang (A) | 8-8 |
| 8.3.1.2 | Bottom Only – End Overhang (B) | 8-9 |
| 8.3.1.3 | Bottom Only – End Joint Width (C) | 8-10 |
| 8.3.1.4 | Bottom Only – Side Joint Length (D) | 8-11 |
| 8.3.1.5 / 8.3.1.6 | Bottom Only – Maximum Fillet Height (E) / Minimum Fillet Height (F) | 8-12 |
| 8.3.1.7 / 8.3.1.8 | Bottom Only – Solder Thickness (G) / End Overlap (J) | 8-13 |
| 8.3.2 | Rectangular or Square End Chip Components – 1, 2, 3 or 5 Side Termination(s) | 8-14 |
| 8.3.2.1 | Rect/Sq Chip – Side Overhang (A) | 8-15 |
| 8.3.2.2 | Rect/Sq Chip – End Overhang (B) | 8-17 |
| 8.3.2.3 | Rect/Sq Chip – End Joint Width (C) | 8-18 |
| 8.3.2.4 | Rect/Sq Chip – Side Joint Length (D) | 8-20 |
| 8.3.2.5 | Rect/Sq Chip – Maximum Fillet Height (E) | 8-21 |
| 8.3.2.6 | Rect/Sq Chip – Minimum Fillet Height (F) | 8-22 |
| 8.3.2.7 | Rect/Sq Chip – Solder Thickness (G) | 8-23 |
| 8.3.2.8 | Rect/Sq Chip – End Overlap (J) | 8-24 |
| 8.3.2.9 / 8.3.2.9.1 | Termination Variations / Mounting on Side (Billboarding) | 8-25 |
| 8.3.2.9.2 | Termination Variations – Mounting Upside Down | 8-27 |
| 8.3.2.9.3 | Termination Variations – Stacking | 8-28 |
| 8.3.2.9.4 | Termination Variations – Tombstoning | 8-29 |
| 8.3.2.10 | Center and Lateral Terminations | 8-30 |
| 8.3.2.10.1 | Center/Lateral – Solder Width of Side Termination | 8-31 |
| 8.3.2.10.2 | Center/Lateral – Minimum Fillet Height of Side Termination | 8-32 |
| 8.3.3 | Cylindrical End Cap Terminations | 8-33 |
| 8.3.3.1 … 8.3.3.8 | Cylindrical End Cap – Side Overhang (A) 8-34 / End Overhang (B) 8-35 / End Joint Width (C) 8-36 / Side Joint Length (D) 8-37 / Maximum Fillet Height (E) 8-38 / Minimum Fillet Height (F) 8-39 / Solder Thickness (G) 8-40 / End Overlap (J) 8-41 | 8-34..8-41 |
| 8.3.3.9 | Cylindrical End Cap – Center and Lateral Terminations | 8-42 |
| 8.3.4 | Castellated Terminations | 8-43 |
| 8.3.4.1 | Castellated – Side Overhang (A) | 8-44 |
| 8.3.4.2 / 8.3.4.3 | Castellated – End Overhang (B) / Minimum End Joint Width (C) | 8-45 |
| 8.3.4.4 / 8.3.4.5 | Castellated – Minimum Side Joint Length (D) / Maximum Fillet Height (E) | 8-46 |
| 8.3.4.6 / 8.3.4.7 | Castellated – Minimum Fillet Height (F) / Solder Thickness (G) | 8-47 |
| 8.3.5 | Flat Gull Wing Leads | 8-48 |
| 8.3.5.1 … 8.3.5.8 | Flat Gull Wing – Side Overhang (A) 8-49 / Toe Overhang (B) 8-52 / Minimum End Joint Width (C) 8-53 / Minimum Side Joint Length (D) 8-54 / Maximum Heel Fillet Height (E) 8-55 / Minimum Heel Fillet Height (F) 8-56 / Solder Thickness (G) 8-57 / Coplanarity 8-58 | 8-49..8-58 |
| 8.3.6 | Round or Flattened (Coined) Gull Wing Leads | 8-59 |
| 8.3.6.1 … 8.3.6.9 | Coined Gull Wing – Side Overhang (A) 8-60 / Toe Overhang (B) 8-61 / Minimum End Joint Width (C) 8-61 / Minimum Side Joint Length (D) 8-62 / Maximum Heel Fillet Height (E) 8-63 / Minimum Heel Fillet Height (F) 8-64 / Solder Thickness (G) 8-65 / Minimum Side Joint Height (Q) 8-65 / Coplanarity 8-66 | 8-60..8-66 |
| 8.3.7 / 8.3.7.1 | J Leads / Side Overhang (A) | 8-67 |
| 8.3.7.2 … 8.3.7.8 | J Leads – Toe Overhang (B) 8-69 / End Joint Width (C) 8-70 / Side Joint Length (D) 8-71 / Maximum Heel Fillet Height (E) 8-72 / Minimum Heel Fillet Height (F) 8-73 / Solder Thickness (G) 8-75 / Coplanarity 8-75 | 8-69..8-75 |
| 8.3.8 / 8.3.8.1 | Butt/I Connections / Modified Through-Hole Terminations | 8-76 |
| 8.3.8.1.1 … 8.3.8.1.7 | Butt/I Modified THT – Maximum Side Overhang (A) 8-77 / Toe Overhang (B) 8-77 / Minimum End Joint Width (C) 8-78 / Minimum Side Joint Length (D) 8-78 / Maximum Fillet Height (E) 8-78 / Minimum Fillet Height (F) 8-79 / Solder Thickness (G) 8-79 | 8-77..8-79 |
| 8.3.8.2 | Butt/I – Solder Charged Terminations | 8-80 |
| 8.3.8.2.1 … 8.3.8.2.4 | Solder Charged – Maximum Side Overhang (A) 8-81 / Maximum Toe Overhang (B) 8-81 / Minimum End Joint Width (C) 8-82 / Minimum Fillet Height (F) 8-82 | 8-81..8-82 |
| 8.3.9 | Flat Lug Leads | 8-83 |
| 8.3.10 | Tall Profile Components Having Bottom Only Terminations | 8-84 |
| 8.3.11 | Inward Formed L-Shaped Ribbon Leads | 8-85 |
| 8.3.12 | Surface Mount Area Array | 8-87 |
| 8.3.12.1 / 8.3.12.2 | Area Array – Alignment / Solder Ball Spacing | 8-88 |
| 8.3.12.3 | Area Array – Solder Connections | 8-89 |
| 8.3.12.4 / 8.3.12.5 | Area Array – Voids / Underfill/Staking | 8-91 |
| 8.3.12.6 | Area Array – Package on Package | 8-92 |
| 8.3.13 | Bottom Termination Components (BTC) | 8-94 |
| 8.3.14 | Components with Bottom Thermal Pad Terminations (D-Pak) | 8-96 |
| 8.3.15 / 8.3.15.1 | Flattened Post Connections / Maximum Termination Overhang – Square Solder Land | 8-98 |
| 8.3.15.2 / 8.3.15.3 | Flattened Post – Maximum Termination Overhang – Round Solder Land / Maximum Fillet Height | 8-99 |
| 8.3.16 | P-Style Terminations | 8-100 |
| 8.3.16.1 / 8.3.16.2 | P-Style – Maximum Side Overhang (A) / Maximum Toe Overhang (B) | 8-101 |
| 8.3.16.3 / 8.3.16.4 | P-Style – Minimum End Joint Width (C) / Minimum Side Joint Length (D) | 8-102 |
| 8.3.16.5 | P-Style – Minimum Fillet Height (F) | 8-103 |
| 8.3.17 | Vertical Cylindrical Cans with Outward L-Shaped Lead Terminations | 8-104 |
| 8.3.18 | Flexible and Rigid Flex Printed Circuitry with Flat Uniformed Leads | 8-106 |
| 8.3.19 | Wrapped Terminals | 8-107 |
| 8.3.19.1 … 8.3.19.3 | Wrapped – Side Overhang (A) / End Joint Width (C) / Side Joint Length (D) | 8-108 |
| 8.3.19.4 / 8.3.19.5 | Wrapped – Minimum Heel Fillet Height (F) / Solder Thickness (G) | 8-109 |
| 8.3.20 | Flat Leaded Surface Mount Connectors | 8-110 |
| 8.4 | Specialized SMT Terminations | 8-111 |
| 8.5 | Surface Mount Connectors | 8-112 |
| 8.5.1 | Surface Mount Threaded Standoffs (SMTS) or Surface Mount Fasteners | 8-113 |
| 9.0 | Component Damage | 9-1 |
| 9.1 | Loss of Metallization | 9-2 |
| 9.2 | Chip Resistor Element | 9-3 |
| 9.3 | Leaded/Leadless Devices | 9-4 |
| 9.4 | Ceramic Chip Capacitors | 9-8 |
| 9.5 | Connectors | 9-10 |
| 9.6 / 9.7 | Relays / Ferrite Core Components | 9-13 |
| 9.8 | Connectors, Handles, Extractors, Latches | 9-14 |
| 9.9 | Edge Connector Pins | 9-15 |
| 9.10 | Press Fit Pins | 9-16 |
| 9.11 | Backplane Connector Pins | 9-17 |
| 9.12 | Heatsink Hardware | 9-18 |
| 9.13 | Threaded Items and Hardware | 9-19 |
| 10.0 / 10.1 / 10.1.1 | Printed Boards and Assemblies / Non-Soldered Contact Areas / Contamination | 10-1 |
| 10.1.2 / 10.2 | Non-Soldered Contact Area – Damage / Laminate Conditions | 10-3 |
| 10.2.1 | Measling and Crazing | 10-5 |
| 10.2.2 | Blistering and Delamination | 10-7 |
| 10.2.3 | Weave Texture/Weave Exposure | 10-10 |
| 10.2.4 | Haloing | 10-11 |
| 10.2.5 | Nicks and Cracks | 10-13 |
| 10.2.6 | Burns | 10-15 |
| 10.2.7 | Bow and Twist | 10-16 |
| 10.2.8 | Depanelization | 10-17 |
| 10.2.9 | Mechanical Damage | 10-19 |
| 10.3 / 10.3.1 | Conductors/Lands / Reduction | 10-20 |
| 10.3.2 | Conductors/Lands – Lifted | 10-21 |
| 10.3.3 | Conductors/Lands – Mechanical Damage | 10-23 |
| 10.4 / 10.4.1 | Flexible and Rigid-Flex Printed Boards / Damage | 10-24 |
| 10.4.2 / 10.4.2.1 | Delamination/Blister / Flex | 10-27 |
| 10.4.2.2 | Delamination/Blister – Flex to Stiffener | 10-29 |
| 10.4.3 | Solder Wicking | 10-30 |
| 10.4.4 | Attachment | 10-31 |
| 10.5 | Marking | 10-32 |
| 10.5.1 | Marking – Etched (Including Hand Printing) | 10-34 |
| 10.5.2 | Marking – Screened | 10-35 |
| 10.5.3 | Marking – Stamped | 10-36 |
| 10.5.4 / 10.5.5 / 10.5.5.1 | Marking – Laser / Labels / Bar Coding/Data Matrix | 10-37 |
| 10.5.5.2 | Labels – Readability | 10-38 |
| 10.5.5.3 / 10.5.5.4 | Labels – Adhesion and Damage / Position | 10-39 |
| 10.5.6 | Marking – RFID Tags | 10-40 |
| 10.6 | Cleanliness | 10-41 |
| 10.6.1 / 10.6.1.1 | Flux Residues / Cleaning Required | 10-42 |
| 10.6.1.2 | Flux Residues – No Clean Process | 10-43 |
| 10.6.2 | Foreign Object Debris (FOD) | 10-44 |
| 10.6.3 | Chlorides, Carbonates and White Residues | 10-45 |
| 10.6.4 | Surface Appearance | 10-47 |
| 10.7 | Solder Mask Coating | 10-48 |
| 10.7.1 | Wrinkling/Cracking | 10-49 |
| 10.7.2 | Voids, Blisters, Scratches | 10-51 |
| 10.7.3 | Breakdown | 10-53 |
| 10.7.4 / 10.8 / 10.8.1 | Discoloration / Conformal Coating / General | 10-54 |
| 10.8.2 | Conformal Coating – Coverage | 10-55 |
| 10.8.3 | Conformal Coating – Thickness | 10-57 |
| 10.9 / 10.9.1 / 10.9.2 | Electrical Insulation Coating / Coverage / Thickness | 10-58 |
| 10.10 | Encapsulation | 10-59 |
| 11.0 / 11.1 | Discrete Wiring / Solderless Wrap | 11-1 |
| 12.0 | High Voltage | 12-1 |
| 13.0 | Jumper Wires | 13-1 |
| 13.1 | Wire Routing | 13-2 |
| 13.2 | Wire Staking – Adhesive or Tape | 13-3 |
| 13.3 | Terminations | 13-4 |
| 13.3.1 / 13.3.1.1 | Terminations – Lap / Component Lead | 13-5 |
| 13.3.1.2 | Lap – Land | 13-7 |
| 13.3.2 | Wire in Hole | 13-8 |
| 13.3.3 | Wrapped | 13-9 |
| 13.3.4 / 13.3.4.1 | SMT / Chip and Cylindrical End Cap Components | 13-10 |
| 13.3.4.2 | SMT – Gull Wing | 13-11 |
| 13.3.4.3 | SMT – Castellations | 13-13 |
| App. A / A.1 / A.1.1 | Protecting the Assembly – ESD and Other Handling / ESD Prevention / ESD Control Program | A-1 |
| A.1.2 | ESD Protective Area (EPA) Requirements | A-2 |
| A.1.3 | Minimizing Static Charge | A-3 |
| A.1.4 / A.1.5 / A.1.6 | ESD Protective Packaging / Training / Tools and Equipment | A-4 |
| A.1.7 / A.1.8 | Compliance Verification / Warning Labels | A-5 |
| A.2 / A.2.1 | General Handling / Handling Considerations | A-6 |
| A.2.2 / A.2.3 | Preventing Contamination / Gloves and Finger Cots | A-7 |
| A.3 | Moisture Sensitive Devices | A-8 |

IPC-A-610J tables: 1-1 Summary of Related Documents 1-1 · 1-2 Inspection Magnification (Land Width) 1-9 · 1-3 Magnification Aid Applications for Wires and Soldered Conductors 1-10 · 1-4 Magnification Aid Applications – Other 1-10 · 6-1 Swaged Hardware Minimum Soldering Requirements 6-9 · 6-2 Strand Damage 6-20 · 6-3 Minimum Bend Radius Requirements 6-26 · 6-4 Turret or Straight Pin Terminal Conductor Placement 6-32 · 6-5 Bifurcated – Side Route 6-35 · 6-6 Staking Requirements, Side Route Straight Through 6-37 · 6-7 Bifurcated – Bottom Route 6-38 · 6-8 Pierced or Perforated 6-43 · 6-9 Hook 6-46 · 6-10 AWG 30 and Smaller Wire Wrap 6-52 · 7-1 Lead Bend Radius 7-4 · 7-2 Component to Land Clearance 7-29 · 7-3 Protrusion of Leads/Conductors in Supported Holes 7-31 · 7-4 Supported Hole – Minimum Solder Requirements 7-35 · 7-5 Board in Board – Minimum Acceptable Solder Conditions 7-50 · 7-6 Protrusion of Leads in Unsupported Holes 7-55 · 7-7 Unsupported Holes with Component Leads, Minimum Acceptable Conditions 7-58 · 8-1 Chip Bottom Only Termination Features 8-7 · 8-2 Rect/Sq Chip 1, 2, 3 or 5 Side 8-14 · 8-2A Center/Lateral Termination 8-30 · 8-3 Cylindrical End Cap 8-33 · 8-3A Cylindrical Center/Lateral 8-42 · 8-4 Castellated 8-43 · 8-5 Flat Gull Wing 8-48 · 8-6 Round/Coined Gull Wing 8-59 · 8-7 J Leads 8-67 · 8-8 Butt/I Modified THT Leads 8-76 · 8-9 Butt/I Solder Charged 8-80 · 8-10 Flat Lug 8-83 · 8-11 Tall Profile Bottom Only 8-84 · 8-12 Inward Formed L Ribbon 8-85 · 8-13 BGA Collapsing Balls 8-87 · 8-14 BGA Noncollapsing Balls 8-87 · 8-15 Column Grid Array 8-87 · 8-16 BTC 8-94 · 8-17 Bottom Thermal Pad (D-Pak) 8-96 · 8-18 Flattened Post 8-98 · 8-19 P-Style 8-100 · 8-20 Vertical Cylindrical Cans, Outward L Leads 8-105 · 8-21 Flex/Rigid-Flex Flat Unformed Leads 8-106 · 8-22 Wrapped Terminals 8-107 · 8-23 Flat Leaded SMT Connectors 8-110 · 8-24 SMTS/SM Fasteners Minimum Solder 8-113 · 9-1 Nick or Chip-Out Criteria 9-8 · 10-1 Coating Thickness Requirements 10-57 · A-1 Typical Static Charge Sources A-3 · A-2 Typical Static Voltage Generation A-3 · A-3 Recommended Practices for Handling A-6.

Index cross-references printed in the excerpt (topic → clause): billboarding 8.3.2.9.1 · tombstoning 8.3.2.9.4 · upside down 8.3.2.9.2 · stacking 8.3.2.9.3 · solder balls 5.2.7.1 · bridging 5.2.7.2 · webbing 5.2.7.3 · cold solder 1.8.3, 5.2.5 · blowholes/pinholes 5.2.2 · exposed basis metal 5.2.1 · bow and twist 10.2.7 · haloing 10.2.4 · measles 10.2.1 · weave exposure 10.2.3 · vertical fill 7.3.5.1 · circumferential wetting 7.3.5, 7.4.5 · clinch 7.3.4, 7.4.4 · lead protrusion 7.3.3, 7.4.3 · meniscus 1.8.14 [TOC: 1.8.17], 7.3.5.8 · hole obstruction 4.1.2, 7.1.4 · heatsink 4.1.3, 7.1.5, 9.12 · torque 4.1.5.1 · thread extension 4.1.5 · press-fit pins 9.10 · board lock 7.1.8, 8.5 · conformal coating 10.8 · adhesive bonding 7.2.2, 8.1, 13.2 · cleanliness/contamination 3.0, 10.1, 10.6 · white residue 10.6.3 · chlorides/carbonates 10.6.3 · no-clean 10.6.1.2 · insulation clearance 6.2.2, 12 · electrical clearance 1.8.5 [TOC: 1.8.8], 4.1.1 · classification 1.3 · magnification 1.13.2 · jumper 13.0 · pin-in-paste 1.8.17 [TOC: 1.8.20] · wire diameter 1.8.4 [TOC: 1.8.7]. (Bracketed = TOC numbering, which differs from the index in the extraction; prefer TOC.)

### 2.10 Library guide [5] — prioritized top twenty (ranked by value to an end-to-end product developer, not reading order)

| # | book | level | active study estimate | role / sequence point |
|---|---|---|---|---|
| 1 | Horowitz & Hill, *The Art of Electronics*, 3rd ed., Cambridge Univ. Press, 2015 | Intermediate | ~80–120 h selective | Foundation; permanent circuit reference |
| 2 | Wilson, *The Circuit Designer's Companion*, 4th ed., Newnes/Elsevier, 2017 | Intermediate | ~25–40 h | Immediately after fundamentals; shapes checklist before schematic capture |
| 3 | Cohen, *Prototype to Product*, O'Reilly, 2015 (438 pp.; 11 h 17 min straight reading) | Beginner–intermediate | ~14–22 h | Architecture stage; revisit before production transfer |
| 4 | Mitzner, Doe, Akulin, Suponin, Müller, *Complete PCB Design Using OrCAD Capture and PCB Editor*, 2nd ed., Newnes/Elsevier, 2019 (OrCAD 17.2; downloadable design files) | Beginner–intermediate | ~35–55 h reproducing projects | First ECAD implementation book, while creating first schematic + board |
| 5 | Coombs & Holden (eds.), *Printed Circuits Handbook*, 7th ed., McGraw Hill, 2016 | Intermediate–advanced | ~20–35 h essential DFM; 80–120 h broad | Before stack-up/layout frozen; during manufacturer interaction; treat as encyclopedia |
| 6 | Bogatin, *Signal and Power Integrity—Simplified*, 3rd ed., Pearson, 2018 (digital ©2022) | Intermediate–advanced | ~35–55 h | After Johnson or after PCB fundamentals; during stack-up, routing, PDN |
| 7 | Ott, *Electromagnetic Compatibility Engineering*, Wiley, 2009 (880 pp.) | Intermediate–advanced | ~45–70 h | Before layout; revisit for enclosure/cabling and pre-compliance |
| 8 | Johnson & Graham, *High-Speed Digital Design: A Handbook of Black Magic*, Prentice Hall/Pearson, 1993 | Intermediate | ~25–40 h | Before routing any board with fast edges, DDR, high-speed serial, fast clocks, long cables, sensitive mixed-signal |
| 9 | Williams, *EMC for Product Designers*, 5th ed., Newnes/Elsevier, 2016 | Intermediate | ~25–40 h | After first pass through Ott; before design reviews and pre-compliance |
| 10 | Erickson & Maksimović, *Fundamentals of Power Electronics*, 3rd ed., Springer, 2020 | Advanced | ~70–110 h; ~35–50 h selective DC/DC | Before custom switch-mode stages/control loops |
| 11 | White, *Making Embedded Systems*, 2nd ed., O'Reilly, 2024 (428 pp.; 12 h 6 m straight reading) | Intermediate | ~20–30 h | System architecture before MCU/SoC and peripheral interfaces frozen; through bring-up |
| 12 | Stringham, *Hardware/Firmware Interface Design*, Newnes/Elsevier, 2010 (>300 practices, 7 principles) | Intermediate–advanced | ~20–35 h | After embedded architecture, before register maps / reset / boot committed |
| 13 | Archambeault & Drewniak, *PCB Design for Real-World EMI Control*, Kluwer/Springer, 2002 | Advanced | ~20–35 h | After Ott/Bogatin, before layout review; when EMC margins are tight |
| 14 | Pease, *Troubleshooting Analog Circuits*, 1st ed., Newnes, 1991 (>60 legacy Electronics Workbench circuits) | Intermediate | ~15–25 h | Before first prototype bring-up; keep at bench |
| 15 | Pressman, Billings & Morey, *Switching Power Supply Design*, 3rd ed., McGraw Hill, 2009 | Intermediate–advanced | ~40–65 h | After core Erickson chapters, when implementing an actual topology |
| 16 | Bowick (with Blyler, Ajluni), *RF Circuit Design*, 2nd ed., Newnes/Elsevier (2011 e-record) | Intermediate | ~15–25 h | First RF book; before first wireless schematic and impedance-controlled layout |
| 17 | Pozar, *Microwave Engineering*, 4th ed., Wiley, 2011 | Advanced | ~60–100 h | After Bowick when designing (not integrating) RF; custom matching, filters, microwave structures |
| 18 | Balanis, *Antenna Theory: Analysis and Design*, 4th ed., Wiley, 2016 (1,104 pp.; MATLAB companion) | Advanced | ~70–120 h broad; ~30–50 h one antenna family | After RF/transmission-line competence; when product has integrated/custom antenna |
| 19 | Bralla (ed.), *Design for Manufacturability Handbook*, 2nd ed., McGraw-Hill, 1999 (>70 contributors; DFM for electronics, DFX, concurrent engineering chapters) | Intermediate | ~12–20 h selective; 40–80 h general | Enclosure/mechanical/production planning; before tooling or high-volume commitments |
| 20 | Scherz & Monk, *Practical Electronics for Inventors*, 4th ed., McGraw-Hill Education, 2016 | Beginner–intermediate | ~45–70 h | First only when fundamentals are weak; otherwise desk reference |

Books 1–15 and 19–20 = broadly applicable product-development shelf; 16–18 mandatory only for intentional RF/wireless/antenna design ([5] p.4). Total: ~700–1,000 h deep; ~350–550 h compressed non-RF; +150–250 h RF ([5] p.18).

Category coverage matrix ([5] pp.19–20; first book in each cell is the first to reach for):

| category | core books |
|---|---|
| System architecture | Prototype to Product; Circuit Designer's Companion; Making Embedded Systems; The Art of Electronics |
| Schematic capture | Complete PCB Design Using OrCAD; Circuit Designer's Companion; The Art of Electronics |
| PCB layout | Complete PCB Design Using OrCAD; Printed Circuits Handbook; High-Speed Digital Design; PCB Design for Real-World EMI Control |
| RF / antenna | RF Circuit Design → Microwave Engineering → Antenna Theory |
| Signal integrity / EMC | Signal and Power Integrity—Simplified; High-Speed Digital Design; Electromagnetic Compatibility Engineering; EMC for Product Designers; PCB Design for Real-World EMI Control |
| Power electronics | Fundamentals of Power Electronics; Switching Power Supply Design; power sections of Circuit Designer's Companion |
| Embedded firmware / hardware integration | Making Embedded Systems; Hardware/Firmware Interface Design; digital sections of Circuit Designer's Companion |
| Manufacturing / DfM | Printed Circuits Handbook; Design for Manufacturability Handbook; Complete PCB Design Using OrCAD; Prototype to Product |
| Testing / validation | Troubleshooting Analog Circuits; Electromagnetic Compatibility Engineering; EMC for Product Designers; Making Embedded Systems; Printed Circuits Handbook |

### 2.11 Library guide [6] — tiered books with ISBNs

Scope codes: SYS system architecture; ANA analog; DIG digital; SCH schematic/circuit design; PCB board design/layout; SI/PI; RF; PWR power electronics; EMC; TH thermal/mechanical; TEST bring-up/validation; DFM; REL reliability; REG regulatory. Levels: B beginner, I intermediate, A advanced, Ind professional/industry.

| priority | scope | book | level |
|---|---|---|---|
| Must-have | ANA, DIG, SCH, PWR, TEST | Scherz & Monk, *Practical Electronics for Inventors*, 4th ed., 2016, McGraw-Hill Education, ISBN 978-1-259-58754-2 | B→I |
| Must-have | ANA, DIG, SCH, PWR, TEST | Horowitz & Hill, *The Art of Electronics*, 3rd ed., 2015, Cambridge UP, ISBN 978-0-521-80926-9 | I→A/Ind |
| Must-have | ANA, DIG, SCH, TEST, FW/HW | Hayes, Abrams et al., *Learning the Art of Electronics: A Hands-On Lab Course*, 2nd ed. (current), Cambridge UP (labs through programmable logic/Verilog, ARM MCU, RTOS) | B→I |
| Recommended | ANA, sensors, advanced SCH | Horowitz & Hill, *The Art of Electronics: The x-Chapters*, 2nd ed., 2026, Cambridge UP (+~150 pp. incl. sensors chapter; buy 2026 2e, not 2020 1e) | A/Ind |
| Must-have | SYS, ANA, DIG, SCH, REL, TEST | Wilson, *The Circuit Designer's Companion*, 4th ed., 2017, Newnes/Elsevier, ISBN 978-0-08-101764-7 (incl. wide-bandgap power devices) | I→Ind |
| Must-have | PCB, DFM, TEST, REL, manufacturing | Coombs & Holden, *Printed Circuits Handbook*, 7th ed., 2016, McGraw-Hill, ISBN 978-0-07-183395-0 | I→A/Ind |
| Must-have | PCB, DFM | PCEA, *Printed Circuit Board Basics: An Introduction to the PCB Industry*, 6th ed., 2026, ISBN-10 0-9743561-0-7 (read before diving into IPC documents) | B→I/Ind |
| Must-have | PCB, SI/PI, DIG, EMC | Bogatin, *Signal and Power Integrity—Simplified*, 3rd ed., 2018, Pearson/Prentice Hall, ISBN 978-0-13-451341-6 | I→A/Ind |
| Must-have classic | PCB, SI, EMC | Johnson & Graham, *High-Speed Digital Design: A Handbook of Black Magic*, 1993, Prentice Hall, ISBN 978-0-13-395724-2 | I→A/Ind |
| Recommended classic | PCB, SI | Johnson & Graham, *High-Speed Signal Propagation: Advanced Black Magic*, 2003, Prentice Hall, ISBN 978-0-13-084408-8 | A/Ind |
| Recommended | SI, PCB, channels | Hall & Heck, *Advanced Signal Integrity for High-Speed Digital Designs*, 2009, Wiley, ISBN 978-0-470-19235-1 | A/Ind |
| Recommended classic | SYS, PCB, SI | Hall, Hall & McCall, *High-Speed Digital System Design*, 2000, Wiley, ISBN 978-0-471-36090-9 | A/Ind |
| Recommended | PCB, SI, stackup | Ritchey, *Right the First Time*, Vol. 1, 2003, Speeding Edge, ISBN-10 0-9741936-0-7 | I→A/Ind |
| Recommended | PCB, SI, stackup | Ritchey, *Right the First Time*, Vol. 2, 2007, Speeding Edge, ISBN-10 0-9741936-1-5 (dense BGAs, high-speed interfaces) | A/Ind |
| Must-have | PCB, PWR, TH | Brooks & Adam, *PCB Design Guide to Via and Trace Currents and Temperatures*, 2021, Artech House, ISBN-10 1-63081-860-7 | I→A/Ind |
| Recommended classic | PCB, EMC | Archambeault, *PCB Design for Real-World EMI Control*, 2002, Kluwer Academic, ISBN 978-1-4757-3642-7 | A/Ind |
| Must-have | EMC, TEST, REG | Paul, Scully & Steffka, *Introduction to Electromagnetic Compatibility*, 3rd ed., 2022, Wiley, ISBN 978-1-119-40434-7 | I→A/Ind |
| Must-have classic | EMC, PCB, grounding, shielding | Ott, *Electromagnetic Compatibility Engineering*, 2009, Wiley, ISBN 978-0-470-18930-6 | I→A/Ind |
| Must-have | EMC, TEST, REG, product process | Williams, *EMC for Product Designers*, 5th ed., 2016, Newnes/Elsevier, ISBN 978-0-08-101016-7 | I→Ind |
| Must-have for custom power | PWR, control, magnetics | Erickson & Maksimović, *Fundamentals of Power Electronics*, 3rd ed., 2020, Springer, ISBN 978-3-030-43879-1 | I→A/Ind |
| Recommended for power | PWR, magnetics, practical | Pressman, Billings & Morey, *Switching Power Supply Design*, 3rd ed., 2009, McGraw-Hill, ISBN 978-0-07-148272-1 | I→A/Ind |
| Must-have for RF products | RF, SYS | Steer, *Fundamentals of Microwave and RF Design*, 3rd ed., 2019, NC State Univ./UNC Press, ISBN 978-1-4696-5688-5 | I→A |
| Recommended for serious RF | RF, SYS, matching, amplifiers | Steer, *Microwave and RF Design*, five-volume 3rd-ed. series, 2019, NC State/UNC Press (Vol. 1 ISBN 978-1-4696-5690-8; Vol. 3 978-1-4696-5694-6; Vol. 5 978-1-4696-5698-4) | A/Ind |
| Recommended for RFIC/front-end | RF, ANA, RFIC | Razavi, *RF Microelectronics*, 2nd ed., 2011, Prentice Hall/Pearson, ISBN 978-0-13-713473-1 | A |
| Recommended classic for microwave | RF, microwave | Pozar, *Microwave Engineering*, 4th ed., 2011, Wiley, ISBN 978-0-470-63155-3 | A |
| Recommended for sensor products | sensors, ANA, interfaces | Fraden, *Handbook of Modern Sensors*, 5th ed., 2016, Springer, ISBN 978-3-319-19302-1 | I→A/Ind |
| Recommended | REL, TEST, production | O'Connor & Kleyner, *Practical Reliability Engineering*, 5th ed., 2012, Wiley, ISBN 978-0-470-97982-2 | I→A/Ind |
| Optional classic | TH, mechanical | Steinberg, *Cooling Techniques for Electronic Equipment*, 2nd ed., 1991, Wiley, ISBN 978-0-471-52451-9 (read Brooks/Adam first for PCB copper heating) | I→A/Ind |

Topic-by-topic first/second/deep choice ([6] pp.15–16):

| discipline | first | second | deep / specialized |
|---|---|---|---|
| General circuit design | AoE 3e | Circuit Designer's Companion 4e | x-Chapters 2e |
| Beginner-to-working designer | Practical Electronics for Inventors 4e | Learning the Art of Electronics 2e | AoE 3e |
| PCB fabrication / DFM | Printed Circuits Handbook 7e | PCB Basics 6e | IPC-2221C + IPC-6012F |
| High-speed PCB / SI/PI | Bogatin 3e | Johnson & Graham, High-Speed Digital Design | Hall/Heck + Ritchey + Advanced Black Magic |
| PCB current / temperature | Brooks & Adam 2021 | Bogatin (PDN context) | thermal simulation / vendor models |
| EMC/EMI | Paul/Scully/Steffka 3e | Ott | Williams + Archambeault |
| Power electronics | Erickson & Maksimović 3e | Pressman 3e | semiconductor-vendor design guides/models |
| RF system/PCB design | Steer 3e | Pozar 4e | current EM-solver documentation |
| RFIC / transceiver circuits | Razavi 2e | Steer Vols. 1/5 | current RFIC/module reference designs |
| Sensors / instrumentation | Fraden 5e | AoE 3e | sensor-vendor datasheets/app notes |
| Reliability | O'Connor & Kleyner | Wilson | applicable IEC/environmental qualification standards |
| Manufacturing / assembly | Printed Circuits Handbook | IPC-6012F | J-STD-001J + IPC-A-610J |

## 3. Mechanizable checks

Each check is computable from tabular design inputs. "Source rows" cite §1 rule ids.

`CHECK-microvia-geometry`: inputs — per blind-via row: depth_X_mm (capture-land foil to target land), dia_Y_mm (hole diameter at capture land). Formula: AR = X / Y. Pass: X ≤ 0.25 mm AND AR ≤ 1.0. Margin: min(0.25 − X, 1.0 − AR) (mm and ratio reported separately). Consequence of fail: structure is not an IPC-6012F "microvia" — cite Table 3-10 (blind via plating) instead of Table 3-11 and remove HDI adder assumption. Source: IPC6012-022, IPC6012-036.

`CHECK-ipc6012-plating-table-select`: inputs — hole_type ∈ {through, blind, buried_gt2_layers, buried_2layer_core, microvia}, filled (bool), cap_plated (bool). Output: citation string — through/blind/buried>2 → "IPC-6012F Table 3-10"; microvia → "Table 3-11"; buried 2-layer core → "Table 3-12"; filled AND cap_plated → add "Table 3-13"; copper-filled microvia → add "Table 3-14"; laser microvia → "Table 3-15"; mechanically drilled microvia → "Table 3-16". Pass: every plated hole row resolves to exactly one plating table. Source: IPC6012-036..038.

`CHECK-hole-tolerance-declared`: inputs — drill table rows (hole_class ∈ {plated_component, plated_via_only, non_plated}, nominal_um, tol_plus_um, tol_minus_um, declared_on_drawing bool). Default when not declared: plated_component ±100 µm; plated_via_only +80 µm / no minus limit (may be plugged); non_plated ±80 µm. Pass: declared tolerance ≥ default (looser or equal) OR declared explicitly on drawing when tighter. Margin: declared − default (µm); negative ⇒ tighter than default ⇒ must be AABUS/on drawing. Flag: any via that must stay open (vent, test, press-fit) but relies on the "via only" default (no minus limit ⇒ may be totally plugged). Source: IPC6012-012..014.

`CHECK-dielectric-min-spacing`: inputs — stackup rows (layer_i, layer_j, dielectric_thickness_um, is_adjacent_conductive_pair). Pass: thickness ≥ 65 µm for every adjacent conductive pair unless drawing states another minimum per §3.6.2.18. Margin: thickness − 65 (µm). Note: measured after lamination (microsection, Fig 3-47), so design nominal should carry fabricator's tolerance. Source: IPC6012-016.

`CHECK-starting-foil-default`: inputs — layer rows (layer, board_type 1–6, is_HDI_plated_layer, foil_oz_declared or null). Rule: if null → assume 1/2 oz (Type 1: 1 oz; HDI plated layer: 1/4 oz). Pass: every layer has a resolved starting foil; flag rows where the current-carrying calculation assumed a heavier foil than the resolved default. Source: IPC6012-010.

`CHECK-class-declared`: inputs — fab_notes text, assy_notes text. Pass: fab notes contain "IPC-6012" with a Class ∈ {1,2,3}; assembly notes contain "J-STD-001" and "IPC-A-610" each with the same Class; all three classes equal. If fab class missing → report "Class 2 default applies (IPC-6012F Table 1-2)"; if assembly class missing → fail (J-STD-001 §1.3: user must define). Source: IPC6012-001, JSTD001-001, A610-001, LIB-011.

`CHECK-thermal-stress-method-declared`: inputs — fab_notes, assembly_process ∈ {wave/selective/hand, SnPb_reflow, PbFree_reflow}. Expected: wave/selective/hand → IPC-TM-650 2.6.8; SnPb_reflow → 2.6.27 @ 230 °C; PbFree_reflow → 2.6.27 @ 260 °C. Pass: declared method == expected. If undeclared → default 2.6.8 Condition A; flag WARN when assembly is Pb-free reflow (default does not represent 260 °C exposure). Source: IPC6012-007.

`CHECK-surface-finish-resolved`: inputs — finish_declared (designator from §2.4 list or null), drawing_release_date. If null: date ≤ 2023-10-01 → "X1 per Table 3-3"; date ≥ 2023-10-01 → "ENIG2 per Table 3-3". Pass: finish declared explicitly (designator in §2.4 table, thickness per Table 3-3 or specified). Output: resolved finish + citation. Source: IPC6012-009, IPC6012-026.

`CHECK-solder-mask-resolved`: inputs — fab_notes. States: (a) mask not mentioned → "NOT APPLIED" (flag: almost always unintended for SMT boards); (b) mask mentioned without IPC-SM-840 class → "Class T"; (c) class given → pass. Source: IPC6012-018.

`CHECK-spacing-category`: inputs — per conductor-pair row: layer ∈ {internal, external}, coating ∈ {none, solder_mask, conformal}, feature ∈ {conductor, component_lead}, altitude_m, in_vacuum bool, V_peak. Category: internal → B1; external conductor uncoated & altitude ≤ 3050 & !vacuum → B2; external conductor uncoated & (altitude > 3050 | vacuum) → B3; external conductor solder mask → B4; external conductor conformal → B5; lead coated → A6; lead uncoated & ≤ 3050 → A7; lead uncoated & (> 3050 | vacuum) → A8. Then: required = Table6_1[category][V_peak] (table values NOT in this rulebook — external lookup). Pass: spacing ≥ required. Margin: spacing − required. Source: IPC2221-030.

`CHECK-shallow-backdrill-depth`: inputs — backdrill rows flagged shallow: depth_mm. Pass: 0.05 ≤ depth ≤ 0.127 (approximate band as printed). Margin: min(depth − 0.05, 0.127 − depth). Source: IPC6012-023.

`CHECK-backdrill-definition-complete`: inputs — backdrill rows: primary_dia, backdrill_dia, target_layer, must_not_cut_layer, max_stub_mm, depth_mm, nearest_feature_clearance_mm. Pass: all seven fields populated (Fig 1-1 notes 1–6 + §1.4.2–1.4.3 terms). Source: IPC6012-024.

`CHECK-unit-format`: inputs — dimension strings, target_doc ∈ {IPC-2221C, IPC-6012F, J-STD-001}. Rule: 2221C — values < 0.1 mm must be in µm; 6012F — values < 1.0 mm must be in µm; J-STD-001 — mm main, µm when needed, °C, grams. Pass: no violation. Source: IPC2221-003, IPC6012-027, JSTD001-003.

`CHECK-castellation-D`: inputs — per castellated joint: solder_reaches_land_at_or_beyond_component_edge (bool), wetted_fillet_evident (bool), class. Pass: Class 2/3 → reaches_edge == true; Class 1 → reaches_edge OR wetted_fillet_evident. Defect otherwise (all classes if wetted fillet not evident). Source: A610-002.

`CHECK-castellation-E`: inputs — fillet_on_component_body (bool). Pass: false (fillet may exceed castellation top). Source: A610-003.

`CHECK-component-damage-disposition`: inputs — observation code ∈ {chipout_not_into_seal, id_not_removed, insulation_damage_stable_no_short, chip_into_seal, ceramic_crack_from_chipout, exposes_substrate_or_FFF, glass_beyond_spec, id_missing, coating_exposes_element_or_deforms, damage_increasing, damage_permits_short, plating_flake_peel_blister, burned_charred, dents_scratches_FFF_or_spec, shield_crack, body_delaminates}, class. Output: first three → Acceptable (Class 1) / Process Indicator (Class 2,3); all others → Defect (Class 1,2,3). Source: A610-004..019.

`CHECK-conformal-coating-coverage`: inputs — cured (bool), coating_in_keepout (bool), orange_peel (bool), entrapped_material_violates_MEC (bool), discoloration_or_opacity (bool), bubbles_expose_or_bridge_conductors (bool), bubbles_bridge_noncommon_unmasked_qualified_benign (bool). Acceptable: cured ∧ ¬keepout ∧ ¬MEC_violation ∧ ¬discoloration (orange peel allowed). Process indicator: bubbles/voids/adhesion loss that neither bridge nor expose conductors; bridging bubbles only if qualified & documented benign. Source: A610-020..022.

`CHECK-drawing-standard-revisions`: inputs — fab_notes, assy_notes. Pass: fab notes cite IPC-6012 rev F (2023) and IPC-2221 rev C (2023); assembly notes cite J-STD-001 rev J and IPC-A-610 rev J; any citation of J-STD-001E (2010) or IPC-A-610H or IPC-6012E → WARN superseded. Source: JSTD001-024, LIB-011, [6] p.11.

`CHECK-gate-deliverables`: inputs — gate id, artifact list. Required per gate (LIB-010): concept → {requirements, block_diagram, interfaces, risks, power_budget, MCU/FPGA/RF decision}; electrical_architecture → {power_tree, clock_plan, reset_boot_strategy, ADC/DAC/sensor_interfaces, HW_FW_contract}; schematic → {hierarchical_schematic, component_choices, protection, test_debug_connectors, BOM, initial_simulation}; pcb_planning → {stackup, impedance_targets, placement_zoning, return_paths, PDN_concept, fab_capabilities}; pcb_implementation → {placement, routing, via_strategy, decoupling, HS/RF/clock constraints, DRC, DFM}; bringup → {rail_clock_reset_checks, current_limits, firmware_boot, interface_validation, fault_isolation}; precompliance → {SI_measurements, PI, thermal, emissions, immunity, RF_performance, antenna_tuning}; production_release → {fab_assy_package, process_tolerances, inspection_test_strategy, supplier_qualification, yield_feedback}. Pass: all present. Source: LIB-010.

`CHECK-regulatory-plan-at-architecture`: inputs — markets ⊆ {US, EU, …}, has_radio, mains_powered, product_family ∈ {AV/ICT, industrial, medical, appliance, automotive, aerospace, other}, plan_exists_at_gate ∈ {concept, later}. Pass: plan_exists_at_gate == concept AND plan lists: US → FCC 47 CFR Part 15 + equipment authorization; EU → EMC 2014/30/EU, RED 2014/53/EU if has_radio, LVD 2014/35/EU if in scope, RoHS 2011/65/EU; safety → IEC 62368-1:2023 only if AV/ICT else family-specific; EMC → CISPR 32/35 or product-family; immunity → IEC 61000-4-x incl. 61000-4-2:2025; environmental → IEC 60068 family. Source: LIB-005, [6] pp.11–13.

`CHECK-evt-dvt-coverage`: inputs — test plan rows (category, pass_criterion). Required categories: supply_limits, temperature, load_transients, clocks_interfaces, ESD_immunity, emissions, fault_cases, sensor_accuracy, long_duration. Pass: each category has ≥ 1 test with a numeric pass criterion. Source: LIB-006.

`CHECK-power-stage-validation`: inputs — per regulator: startup_verified, stability_verified (loop gain/phase), transient_verified, losses_verified, component_stress_verified, each with method ∈ {calc, sim, bench}. Pass: all five true with at least calc + sim before fabrication and bench at bring-up. Source: LIB-004 step 8.

`CHECK-stackup-decided-before-routing`: inputs — routing_started (bool), stackup fields {layer_count, reference_plane_map, impedance_classes, via_strategy, connector_launches, PDN_structure}. Pass: routing_started ⇒ all fields non-null. Source: LIB-008.

## 4. Verification procedures & plots

| property | procedure / instrument | axes / corners / what good looks like | pass criterion | source |
|---|---|---|---|---|
| Plated-hole structural integrity | Thermal stress per IPC-TM-650 2.6.8 (default, Condition A) or 2.6.27 at 230 °C (SnPb reflow) / 260 °C (Pb-free reflow); then microsection per IPC-6012F §3.6.2 | No plating separation/cracks (Table 3-8), copper voids within Table 3-4/§3.6.2.2 limits, hole Cu ≥ Tables 3-10/3-11/3-12, wrap copper present (Figs 3-29 vs 3-30), dielectric ≥ 65 µm (Fig 3-47), etchback per Table 3-9 | table values (not in excerpt) | IPC6012-007, 035, 036 |
| Microvia integrity | 2.6.8 (microvias) §3.6.1.1.1; contact dimension Tables 3-15/3-16; performance-based testing §3.10.15 | target-land contact ≥ table, no piercing (Fig 3-43), voids per Figs 3-37..3-40 | table values | IPC6012-038 |
| Solderability | J-STD-003 Category 2 (SnPb) / Category A (Pb-free), coupons S (holes) and W (SMT) | wetting per J-STD-003 | category pass | IPC6012-020, IPC2221-055 |
| Electrical continuity / isolation / DWV / IR | IPC-9252 test; DWV Table 3-20; IR Table 3-21; MIR §3.8.4 then DWV after MIR; coupons D (interconnect resistance/continuity), E (MIR), H (SIR) | no opens/shorts; IR ≥ table; no breakdown at test voltage | table values | IPC6012-021, 042 |
| Controlled impedance | Z coupon (IPC-2221C §12.4.9.1) with impedance documentation §6.4.5 and tolerance per Table 6-4 example; IPC-6012F §3.10.5 | TDR plot: Z0 vs position; within tolerance across coupon length | ±tolerance as documented | IPC2221-032, 055 |
| Bare-board HiPot | IPC-2221C §3.6.1.2.1 | no breakdown between nets | per design | IPC2221-007 |
| Solder mask adhesion | G coupon; IPC-6012F Table 3-19 | no lifting after test | table | IPC6012-041 |
| Peel strength / plating adhesion | P coupon (legacy C); IPC-6012F §3.10.13 / §3.3.7 | ≥ table | table | IPC2221-055 |
| Flex endurance | Coupon X bending test (Fig B.12-2) | cycles without open | per spec | IPC2221-055 |
| Lot acceptance | IPC-6012F C=0 sampling per lot size Table 4-2; Table 4-3 test set/frequency; PQC Table 4-4 | zero rejects in sample | c = 0 | IPC6012-046 |
| Assembly visual acceptance | IPC-A-610J with magnification by land width (Table 1-2), lighting §1.13.1 | per chapter criteria (Acceptable / PI / Defect) | class-based | A610-001, 023 |
| Conformal coating coverage | Unaided eye; blacklight for fluorescent-pigment coatings; white light aid; thickness per Table 10-1 (A-610J) / Table 10-1 (J-STD-001) | full coverage where required, none in keep-outs, no bridging bubbles | A610-020..022 | A610-020 |
| Component damage | Visual per §9.3 with Figs 9-12..9-23 as references | no chip into seal, no cracks from chip-outs on ceramic, no charring | A610-004..019 | A610-004 |
| EMC emissions/immunity | CISPR 32 (emissions) / CISPR 35 (immunity) or product-family standard; IEC 61000-4-2:2025 ESD and other 61000-4-x at severity levels set by the product-family standard | plot: emission amplitude (dBµV or dBµV/m) vs frequency with the current standard's limit line; immunity: performance criterion per test | margin below limit line; use live standard limits, not book values | LIB-005, LIB-006, [6] p.12 |
| ESD handling | IPC-A-610J Appendix A: static sources Table A-1, voltage generation Table A-2, handling practices Table A-3; EPA per A.1.2 | — | program in place | A610-044 |
| Power-stage behavior | Calculation + SPICE (LTspice with vendor models) + bench: startup, loop stability (gain/phase vs frequency), load transient (Vout vs time), losses, component stresses; op-amp stability, filters, tolerance exploration pre-layout | Bode plot with phase margin; transient plot; loss budget | per design targets | LIB-004 step 8, LIB-027 |
| SI/PI | Bogatin methodology: reflections, crosstalk, losses, eye diagrams, S-parameters, PDN impedance vs frequency; solvers (ADS/HFSS) when closed-form insufficient; interface compliance per PCI-SIG/USB-IF/IEEE 802.3 | eye diagram open per spec mask; PDN |Z| below target vs frequency; S-parameters within spec | interface spec limits | LIB-018, LIB-028 |
| PCB conductor heating | Electrothermal trace/via analysis (Brooks & Adam) + board/enclosure thermal budget; enclosure CFD / mechanical simulation where needed | ΔT vs current for given copper geometry | ΔT ≤ budget | LIB-007, LIB-022 |
| RF | S-parameters / VNA measurements; EM simulation; antenna tuning during pre-compliance | |S11| vs frequency; matching at band | per RF spec / 3GPP where cellular | LIB-004 step 9, LIB-019 |
| Bring-up | Rail/clock/reset checks, current limits, firmware boot, interface validation, fault isolation (Pease methodology) | rail sequencing vs time | all rails/clocks within spec before firmware | LIB-010, LIB-025 |
| Reliability | O'Connor & Kleyner reliability prediction/testing; IEC 60068 environmental (temperature, thermal cycle, shock, vibration) with product-specific severities | — | per requirements | LIB-029, [6] p.12 |

## 5. Pitfalls, failure modes, review checklist

- [ ] IPC-2221C cited as a performance/acceptance spec — it is design-only; fab acceptance = IPC-6012, assembly = J-STD-001 + IPC-A-610 ([1] §1.1; [6] p.14).
- [ ] Sectional standard missing: 2221C must be paired with IPC-2222/2223/2225/2226/2228 as applicable ([1] §1.2).
- [ ] Performance Class not on fab drawing → Class 2 applies silently ([2] Table 1-2).
- [ ] Solder mask not mentioned on fab drawing → **not applied** by default ([2] Table 1-2).
- [ ] Surface finish not specified → default flipped from X1 to ENIG2 for drawings first released on/after 2023-10-01 ([2] Table 1-2 Notes 1–2).
- [ ] "Via only" plated holes carry no minus tolerance and may be fully plugged — specify if vias must remain open ([2] Table 1-2).
- [ ] Thermal stress method not specified → 2.6.8 Condition A default, which is not the 260 °C Pb-free reflow method; Pb-free reflow boards should call 2.6.27 at 260 °C ([2] §1.3.3, §3.6.1.3).
- [ ] "Microvia" used for a blind via deeper than 0.25 mm or AR > 1:1 — wrong plating table (3-11 vs 3-10) and wrong HDI adder ([2] §1.4.4).
- [ ] Microvia breakout at the target land can reduce dielectric spacing below minimum (Fig 3-24) ([2] §3.6.2.9.2.2).
- [ ] Wrap copper removed by sanding/planarization/etching is not acceptable (Fig 3-30) ([2] §3.6.2.11.1).
- [ ] Back-drill drawings must define primary/back-drill diameters, must-not-cut layer, max stub and depth (Fig 1-1) ([2] §1.4.1–1.4.3).
- [ ] Unit-break mismatch: 2221C switches to µm below 0.1 mm; 6012F below 1.0 mm ([1] §1.3; [2] §1.6).
- [ ] Clause mis-citation: in IPC-2221C annular ring is §9.1.2 / Table 9-1 (p.96), holes §9.2, aspect ratio Table 9-5 (p.103); §10.1 is conductor width/thickness (Tables 10-1, 10-2); spacing is §6.3.3.1 / Table 6-1 (p.58) with categories B1–B5, A6–A8 ([1] TOC).
- [ ] IPC-A-610J index numbering differs from TOC in this extraction (electrical clearance 1.8.5 vs 1.8.8; meniscus 1.8.14 vs 1.8.17; pin-in-paste 1.8.17 vs 1.8.20) — cite TOC numbers ([4] Index vs TOC).
- [ ] J-STD-001E (2010) is superseded; drawings should cite rev J ([6] p.11).
- [ ] Butt/I connections not permitted for Class 3 ([3] §7.5.10).
- [ ] Castellated joints: for Class 2/3 solder must extend from the castellation back onto the land at or beyond the component edge; "wetted fillet evident" alone is Class 1 only ([4] §8.3.4.4).
- [ ] Chip-out entering the seal, cracks from chip-outs on ceramic bodies, charred bodies, shield cracks, plating flaking, body delamination = Defect all classes ([4] §9.3).
- [ ] Conformal coating present where not required is not acceptable; bubbles bridging noncommon unmasked conductors need documented qualification ([4] §10.8.2).
- [ ] Solder-mask-covered outer conductors are not "exposed" for coating coverage decisions ([4] §10.8.2).
- [ ] Sector addenda (6012XS/XM/XA) freeze at their publication — later base-standard amendments do not flow into them ([2] §1.3.1.2–1.3.1.4).
- [ ] Newest revision is not automatically contractual — use of the latest revision must be required by contract ([2]/[4] IPC Position Statement).
- [ ] Photographs/illustrations never override text ([2] §1.5).
- [ ] All J-STD-001 limits are absolute (ASTM E29) — no rounding toward acceptance ([3] §1.4.1).
- [ ] Regulatory applicability decided after DVT — decide at architecture ([6] p.12).
- [ ] IEC 62368-1 assumed universal — it is AV/ICT only ([6] p.12, p.17).
- [ ] EMC/thermal/manufacturing learned only after the schematic is complete — stackup, return paths, PI, thermal limits, manufacturability, test access and regulatory constraints belong in architecture and layout planning ([6] p.17).
- [ ] Legacy amps-per-width charts used for high-current traces instead of electrothermal analysis ([6] p.15).
- [ ] SerDes channel designed from a 20-year-old book instead of the live interface spec and vendor channel models ([6] p.13, p.16).
- [ ] Static books used as the MCU/SoC authority — reference manuals, errata, boot/security docs, RTOS docs, BSP change too fast ([6] p.17).
- [ ] Coombs/Holden and Bralla read cover-to-cover — treat as selective references ([5] p.1).
- [ ] Standards only in the library, not in fab/assembly drawings → manufacturing side incomplete ([6] p.14).
- [ ] Working prototype equated with product — Cohen's architecture/process view missing ([5] p.3).

## 6. Standards referenced

| standard | edition / year (as given) | clause / table cited | governs | where cited |
|---|---|---|---|---|
| IPC-2220 (family) | — | ordering number for the design family | generic + sectional design standards | [1] §1.2 p.1 |
| IPC-2221C | Dec. 2023 (supersedes B, Nov. 2012) | all (see §2.6) | generic printed board design | [1]; [6] p.11 |
| IPC-2222 / IPC-2223 / IPC-2225 / IPC-2226 / IPC-2228 | — | — | rigid / flex & rigid-flex / MCM-L / HDI / RF-microwave sectional design | [1] §1.2 p.1 |
| IPC-6011 | — | performance classes; qualification when not specified | generic performance spec | [2] §1.3.1, Table 1-2 |
| IPC-6012F | Sept. 2023 (supersedes E, Mar. 2020) | all (see §2.7) | rigid board qualification/performance | [2]; [6] p.11 |
| IPC-6012XS / XM / XA addenda | "X" = applicable revision | §1.3.1.2–1.3.1.4 | space / medical / automotive deviations | [2] p.1 |
| IPC-6017 | — | Table 1-1 EP adder | embedded passives | [2] p.2 |
| IPC-A-600 | — | §1.2.1 | visual aid for acceptable/nonconforming board conditions | [2] p.1 |
| IPC-2611 / IPC-2614 | — | §1.3.3 | procurement documentation content | [2] p.2 |
| IPC-T-50 | — | §1.4 | terms and definitions | [2] p.5 |
| IPC-TM-650 Method 2.6.8 | — | §3.6.1.1, Table 1-2 (Condition A default) | thermal stress (wave/selective/hand) | [2] p.2–3 |
| IPC-TM-650 Method 2.6.27 | — | §3.6.1.2 (230 °C), §3.6.1.3 (260 °C) | thermal stress (reflow simulation) | [2] p.2, TOC p.24 |
| J-STD-003 | — | Category 2 (SnPb), Category A (Pb-free) | solderability test | [2] Table 1-2 p.3 |
| IPC-9252 | — | Table 1-2 | electrical test (voltage, IR, continuity) | [2] p.3 |
| IPC-SM-840 | — | Class T default | solder mask qualification | [2] Table 1-2 p.3 |
| UL, NEMA, ASQ, AMS, ASME, SAE publications | — | §2.4.2–2.4.7 | referenced "other publications" (titles not in excerpt) | [2] TOC p.8 |
| Federal / Joint Industry standards | — | §2.2–2.3 | referenced (titles not in excerpt) | [2] TOC p.8 |
| J-STD-001E | Apr. 2010 | all (see §2.8) | soldered assembly requirements (superseded) | [3] |
| J-STD-001J | J revision (current per guide) | — | soldering/process requirements for CM quality plan | [6] p.11 |
| IPC-HDBK-001 / IPC-HDBK-610 | — | §1.1 | tutorial companions to J-STD-001 / A-610 | [3] p.1 |
| ASTM E29 | — | §1.4.1 | absolute-limit interpretation of specified limits | [3] p.1 |
| EIA / IPC / Joint / ASTM / ESD Association documents | — | §2.1–2.5 | referenced (titles not in excerpt) | [3] TOC pp.5–6 |
| IPC-A-610J | Mar. 2024 (supersedes H, Sept. 2020); ISBN 978-1-63816-163-9 | all (see §2.9) | acceptability of electronic assemblies | [4]; [6] p.11 |
| IPC / Joint / ESD Association / IEC / ASTM / Military / SAE documents | — | §2.1–2.7, Table 1-1 | referenced (titles not in excerpt) | [4] TOC pp.2-1..2-3 |
| IEC 62368-1 | 2023 | — | AV/ICT equipment safety (not universal) | [6] p.12 |
| IEC 61000-4-2 | 2025 (substantially revised) | — | ESD immunity test methodology | [6] p.11–12, p.19 |
| IEC 61000-4-x family | current | — | immunity tests; severities set by product-family standard | [6] p.12 |
| CISPR 32 / CISPR 35 | current consolidated editions | — | multimedia equipment emissions / immunity | [6] p.12 |
| IEC 60068 family | current | — | environmental tests (temperature, thermal cycle, shock, vibration) | [6] p.12 |
| FCC 47 CFR Part 15 + equipment-authorization guidance | current eCFR | — | US intentional/unintentional radiators | [6] p.13 |
| EU EMC Directive 2014/30/EU | — | — | EU EMC | [6] p.13 |
| EU Radio Equipment Directive 2014/53/EU | — | — | EU radio products | [6] p.13 |
| EU Low Voltage Directive 2014/35/EU | — | — | EU electrical safety in scope | [6] p.13 |
| EU RoHS 2011/65/EU + amendments/harmonized standards | — | — | hazardous substances | [6] p.13 |
| PCI-SIG specifications / USB-IF documents / IEEE 802.3 | current | — | SerDes channel budgets, compliance, TX/RX requirements | [6] p.13 |
| 3GPP specification series, esp. TS 38-series | current | — | 5G/NR bands, RF requirements, conformance | [6] p.13 |
| IPC / JEDEC / IEEE standards (as taught by Mitzner) | — | — | standards-aware PCB workflow | [5] p.1, p.23 |
| EMC standards / legislation (Wilson appendix; Williams) | — | — | product EMC compliance process | [5] p.1, [6] p.7 |
| EDA vendor documentation (Altium Designer, KiCad, Cadence, Siemens) | current | — | libraries, constraints, differential pairs, impedance rules, stackups, variants, BOMs, fab outputs, DRC | [6] p.13 |
| LTspice + vendor models/reference designs | current | — | circuit simulation | [6] p.13 |
| Keysight ADS, Ansys HFSS and equivalents | current | — | EM/SI/PI solvers | [6] p.13 |
| Metric Conversion Act of 1975 (US); EU Council Directive 80/181/EEC (Metric Directive, effective 1 Jan 2010); NIST metric guidance | — | §1.3.1 | metric units basis | [1] p.1 |

## 7. Process / lifecycle guidance

### 7.1 Product gates → outputs → references (guide [5] p.22, guide [6] pp.11–13, IPC procurement flow)

| stage | activity | deliverable | exit criterion | references to have open | source |
|---|---|---|---|---|---|
| Concept / architecture | Product decomposition, tradeoffs, HW/SW partitioning; regulatory applicability decided | Requirements, subsystem block diagram, interfaces, preliminary risks, power budget, MCU/FPGA/RF decisions; regulatory plan (FCC/EU/safety family/EMC/immunity/environmental) | All deliverables exist; regulatory plan complete before DVT planning | Prototype to Product; Circuit Designer's Companion; AoE; Making Embedded Systems; IEC 62368-1 (if AV/ICT), FCC Part 15, EU directives | [5] p.22; [6] pp.12–13 |
| Electrical architecture | Power tree, clocks, reset/boot, sensor interfaces, HW/FW contract | Power tree, clock plan, reset/boot strategy, ADC/DAC/sensor interfaces, HW/FW contract (registers, interrupts, error behavior) | HW/FW contract committed before register maps/boot frozen | AoE; Wilson; White; Stringham; Erickson | [5] p.22, LIB-009 |
| Detailed schematic | Hierarchical schematic, protection, test/debug access, simulation | Hierarchical schematic, component choices, protection, test/debug connectors, BOM, initial simulation (SPICE) | ERC clean; simulation of stability/startup/transients done | Mitzner; Wilson; AoE; Pressman; LTspice + vendor models | [5] p.22; [6] p.13 |
| PCB planning | Stack-up, impedance, zoning, return paths, PDN, fab capability; IPC design rules | Layer stack-up, impedance targets, placement zoning, return paths, PDN concept, fabrication capabilities; IPC-2221C design rules + IPC-6012F fab requirements captured (class, type, adders, finish, mask, tolerances, thermal stress method) | Stack-up frozen only after Bogatin/Johnson review; fab capability confirmed | Coombs/Holden; PCEA PCB Basics; Johnson; Bogatin; Ott; IPC-2221C; IPC-6012F | [5] p.22; [6] p.11, p.18 |
| PCB implementation | Placement, routing, vias, decoupling, HS/RF/clock constraints, DRC/DFM; conductor heating | Placement, routing, via strategy, decoupling, RF/clock/high-speed constraints, DRC/DFM pass; electrothermal trace/via check; board + enclosure thermal budget | DRC = 0, DFM clean, thermal budget met | Mitzner; Bogatin; Archambeault; Ott; Bowick/Pozar (RF); Brooks & Adam; EDA docs | [5] p.22; [6] p.18 |
| Fabrication handoff | Fab drawing with standards, coupons, ordering data | Fab package citing IPC-2221 (design) and IPC-6012F (class N, Type, plating code, finish, adders, Table 1-2 selections, thermal stress method), conformance coupons per IPC-2221C App. A, ordering data per IPC-6012F §5.1, procurement documentation per IPC-2611/2614 | Every AABUS item written; selection string complete | IPC-2221C §11–12; IPC-6012F §1.3.3, §5.1 | IPC6012-005..007, IPC2221-054..055 |
| Board qualification / lot acceptance | Fabricator qualification, acceptance testing, PQC | Qualification per IPC-6011/6012F §4.1 (Table 4-1 coupons); acceptance per C=0 plan (Table 4-2) and Table 4-3; PQC per Table 4-4; microsections after thermal stress | Zero rejects in C=0 sample; microsection attributes within Tables 3-7..3-21 | IPC-6012F §3–4; IPC-A-600 | IPC6012-046 |
| Prototype bring-up | Structured power-up and validation | Rail/clock/reset checks, current limits, firmware boot, interface validation, fault isolation | All rails/clocks/reset verified before firmware integration | Pease; White; Stringham; AoE | [5] p.22 |
| Pre-compliance / design validation (EVT/DVT) | SI/PI/thermal/EMC/RF measurements; robustness | SI measurements, power integrity, thermal behavior, emissions/immunity, RF performance, antenna tuning; EVT/DVT covering supply limits, temperature, load transients, clocks/interfaces, ESD/immunity, emissions, fault cases, sensor accuracy, long duration | Margins to current CISPR/IEC 61000-4 limits; IEC 60068 environmental per use environment | Bogatin; Ott; Williams; Pozar/Balanis; IEC 61000-4-x; CISPR 32/35; IEC 60068 | [5] p.22; [6] p.19 |
| Assembly process definition | CM quality plan | Assembly drawing citing J-STD-001J (process) and IPC-A-610J (acceptability) with the same Class; cleanliness designator; coating/staking requirements; inspection magnification plan | Class defined by user in procurement package | J-STD-001; IPC-A-610; IPC-HDBK-001/610 | JSTD001-001, LIB-011 |
| Production release | Fab/assembly package, process tolerances, inspection/test, supplier qualification, yield feedback; reliability | Controlled production documentation for fabrication, assembly, inspection, programming, functional test; reliability plan | Documentation controlled (not assumptions between team and CM) | Coombs/Holden; Bralla; Mitzner; Cohen; O'Connor & Kleyner; IPC-6012F; J-STD-001J; IPC-A-610J | [5] p.22; [6] p.19 |
| Certification / market release | Freeze regulatory requirements against current rules for exact product and countries | Technical file / declaration of conformity (EU); FCC authorization; radio/interface certifications | Current standards verified at certification time | Williams (process); live FCC/EU/IEC/CISPR/3GPP/interface specs | [6] p.19 step 13 |
| Sustaining / supplier quality | Production inspection, failure review | IPC-A-610J-based inspection records; IPC-6012F incoming quality | — | IPC-A-610J; IPC-6012F | [6] p.11 |

### 7.2 Where each standard enters the lifecycle (guide [6] pp.11–13, verbatim placement)

| standard / reference | lifecycle entry |
|---|---|
| IPC-2221C | PCB architecture, documentation, design rules, fabrication handoff |
| IPC-6012F | Supplier drawing, board class/performance, incoming quality |
| J-STD-001J | Assembly process, manufacturing acceptance, workmanship |
| IPC-A-610J | Production inspection, supplier quality, failure review |
| IEC 62368-1:2023 | Architecture, insulation, power input, enclosure, certification |
| IEC 61000-4-2:2025 and 61000-4-x | EVT/DVT EMC testing, ESD protection, robustness |
| CISPR 32 / CISPR 35 + product-family EMC | EMC test plan and certification |
| IEC 60068 family | DVT, reliability qualification, mechanical/thermal validation |
| FCC 47 CFR Part 15 | Regulatory plan, RF/EMC design, market release |
| EU stack (2014/30/EU, 2014/53/EU, 2014/35/EU, RoHS 2011/65/EU) | Requirements capture, technical file, declaration/conformity |
| EDA vendor documentation | SCH → PCB → release package |
| LTspice + vendor models | Circuit design, pre-layout verification |
| Keysight ADS / Ansys HFSS | Antennas, RF matching, packages, connectors, high-speed channels |
| PCI-SIG / USB-IF / IEEE 802.3 | Architecture, stackup, connectors, SI simulation, compliance |
| 3GPP TS 38-series | RF architecture, filters/PAs/LNAs/antennas, certification |

### 7.3 Reading-sequence dependency rationale ([5] p.22)

Wilson puts grounding, PCB construction, components, power, EMC, production, testability and reliability into one product framework → Mitzner walks CAD/schematic through PCB, DfM, SI and fabrication → Bogatin and Johnson explain interconnect physics before final layout → Ott and Williams convert those structures into EMC-conscious system design. RF branch (Bowick early so impedance, matching, RF power, filter, connector and PCB requirements influence architecture; Pozar for distributed design; Balanis when designing/integrating the antenna). Bring-up: Pease before the prototype arrives. Manufacturing: Bralla and Coombs/Holden before tooling, supplier selection, production release, large-volume procurement.

### 7.4 IPC-6012F procurement decision flow (from §1.3)

1. Specify Performance Class (else Class 2). 2. Select board Type 1–6 and technology adders (Table 1-1). 3. Select plating process code 1–5. 4. Select surface finish designator(s) and selective finish; thickness per Table 3-3 unless specified. 5. Select thermal stress method matching assembly process (2.6.8 / 2.6.27-230 / 2.6.27-260). 6. Resolve every AABUS item and every Table 1-2 category in procurement documentation, Ordering Data (§5.1), customer drawing and/or supplier control plan. 7. Invoke sector addendum (XS/XM/XA) if required. 8. Optionally encode as `IPC-6011/6012/Type/Plating/Finish/Selective/Class/Adders`.

## 8. Coverage log

| file | lines read | content | skipped / limitations |
|---|---|---|---|
| 1071920276_IPC_2221C_En_TOC2023_Generic_Standard_on_Printed_.txt | 1–1514 (all) | Cover, complete TOC incl. Figures and Tables lists, §1–§1.3.1 body (p.1) | File ends at p.1 of the body ("This document has ended"). No numeric design limits (Table 6-1, 9-1, 9-5, 10-1/10-2, 4-2..4-4) are present; recorded as clause/table ids only. Some TOC rows were concatenated by the extractor (e.g., 4.2.2.2–4.2.2.6, 4.5.3–4.7.1, 10.1.4–10.3); reconstructed by matching titles to numbers. §6 chapter heading line missing in extraction (subclauses present). |
| 1071920278_IPC_6012F_2023_en_Qualification_and_Performance_S.txt | 1–1354 (all) | Cover, mission/position statements, acknowledgments, complete TOC, Figures and Tables lists, §1–§1.7 body (pp.1–5) incl. Tables 1-1, 1-2 and Figs 1-1..1-3 notes | File ends at p.5. §2–§5 body and all Tables 3-x/4-x absent. Table 1-2 surface-finish rows and the finish-designator thickness-reference column were split across lines by the extractor; reconstructed conservatively (noted in §2.4). Acknowledgment pages contain OCR-garbled mission text (ignored). |
| 490019949_J_STD_001E.txt | 1–173 (all) | Cover, complete TOC incl. Figures and Tables lists, §1.1–§1.4.1 (p.1) | File ends at p.1. No dimensional criteria present. Standard is superseded (rev J current per [6]). |
| 895309757_IPC_A_610J_2024.txt | 1–1700 (all; read in 5 chunks) | Cover, IPC statements, full committee rosters (skipped as non-technical), complete TOC (pp.xiii–xxv) incl. Tables list and Appendix A, body pages 8-46 (§8.3.4.4–8.3.4.5), 9-5..9-7 (§9.3), 10-55 (§10.8.2), Index-1..3 | Only four body pages present; OCR inserted spaces inside words on those pages (transcribed after de-spacing). Index clause numbers disagree with TOC in three places (noted). Figures 8-71..8-73, 9-12..9-23, 10-155..10-157 referenced but not viewable. |
| End_to_End_Electronics_Hardware_Design_Library.txt | 1–899 (all) | Executive summary, selection criteria, top-20 table, detailed core library tables, coverage matrix, sequence flowchart, gate table, closing, 60 footnote URLs | Multi-column tables were linearized by the extractor; hours/levels re-associated with titles by row order. Footnote URLs not reproduced. |
| End_to_End_Electronics_Hardware_Design_Library_for_Product_D.txt | 1–736 (all) | Executive summary, ranking method, scope/level codes, tiered book tables with ISBNs, standards/living-references tables, topic-by-topic ranking, gaps, 13-step path, minimum purchase order, 61 footnote URLs | Same linearization caveat; ISBNs copied exactly as printed (some ISBN-10). Footnote URLs not reproduced. |

Extraction limits: this rulebook contains 19 printed numeric limits (§2.1) and ~150 rules; every other IPC limit is referenced by clause/table id with "value not in excerpt" so Anvil can cite precisely and fetch the value from the licensed text. Nothing was inferred or fabricated.

