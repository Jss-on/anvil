# Complete PCB Design Using OrCAD Capture and PCB Editor (2nd ed.) — Anvil rulebook

## 0. Citation

K. Mitzner, B. Doe, A. Akulin, A. Suponin, and D. Müller, *Complete PCB Design Using OrCAD® Capture and PCB Editor*, 2nd ed. London, UK: Academic Press (Elsevier), 2019. ISBN 978-0-12-817684-9. Chapter DOIs as printed: 10.1016/B978-0-12-817684-9.000NN-X (e.g., Ch.1 = .00001-1, Ch.6 = .00006-0, Ch.12 = .00012-6).

BOOKTAG: MITZ. Page numbers cited as `p.NNN` are the printed page numbers preserved in the text extraction.

Chapters covered by THIS extraction (whole file, lines 1–11391):
- Ch.1 Introduction to PCB design and CAD (fabrication process, stack-up, PTH, soldermask, files)
- Ch.2 Design flow by example (7-step flow; OrCAD click paths skipped)
- Ch.3 Project structures and the PCB Editor tool set (Gerber/aperture/D-code concepts kept; click paths skipped)
- Ch.4 Introduction to industry standards (IPC, EIA, JEDEC, IEC, MIL, ANSI, IEEE organizations; performance classes, producibility levels, fabrication types, density levels; panel/thickness/core/prepreg/plating/copper tables; etch, hole, aspect-ratio and soldermask allowances). UL is not discussed anywhere in the book.
- Ch.5 Introduction to design for manufacturing (placement spacing, courtyard, solder fillets, PTH/annular ring/fab allowances, thermal)
- Ch.6 PCB design for signal integrity (grounds, planes, impedance, termination, crosstalk, current capacity, spacing, stack-ups, PSpice TL simulation)
- Ch.7 Making and editing Capture parts (pin types; tool-agnostic library rules only)
- Ch.8 Making and editing footprints (padstack/footprint design rules; pad-size tables; hole types)
- Ch.9 PCB design examples (stack-ups, split planes, guard rings, via/physical constraints, max safe trace length table)
- Ch.10 Artwork development and board fabrication (fiducials, artwork element sets, drill/route files, pick-and-place, fab documentation)
- Ch.11 Component information system (BOM/variant rules only)
- Ch.12 Signal integrity simulation (tool-agnostic SI simulation checks only)
- Appendix A List of design standards; Appendix B Packages and footprints (JEDEC/EIA outline tables); Appendix C Rise and fall times of logic families; Appendix D Drill and screw dimensions; Appendix E References by subject (standard clause map)

Chapters NOT read: none. Skipped within chapters: OrCAD-specific menu/dialog click paths, screenshots, per-figure GUI descriptions; the index (lines 11236–11391) was scanned only.

## 1. Design rules

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| MITZ-001 | materials | Copper cladding thickness is specified in oz/ft²; 1.0 oz/ft² copper is approximately 1.2–1.4 mil (0.0012–0.0014 in; 0.03–0.035 mm) thick | t(1 oz) = 1.2–1.4 mil (30–35 um) | copper weight (oz) | Base cladding before plating | calc | p.3, §1 | high |
| MITZ-002 | stackup | Multilayer boards are built of cores (C-stage, fully cured, copper-clad) bonded by prepreg (B-stage, partially cured); outer-foil construction (foil + prepreg on outside, cores inside) is more widely used because foil is cheaper than cladding and outer layers are patterned after drilling | — | stack-up construction | Multilayer boards; Fig. 1.4 | review | p.3–4, Fig. 1.3–1.4 | high |
| MITZ-003 | fab | Inner layers are patterned before lamination; outer layers are patterned after lamination, drilling and PTH plating (plating would re-plate removed areas) | — | — | Process sequence: inner-etch → laminate → drill → desmear → plate → outer-etch → mask → silkscreen | review | p.4, p.9–11 | high |
| MITZ-004 | via | Plated through-hole (PTH) barrel plating thickness is typically about 1 mil (0.001 in) | t_plate ≈ 1 mil (25 um) typical | — | Standard PTH; see MITZ Ch.4 Table 4.5 for IPC minimums | inspect | p.9, §1 | high |
| MITZ-005 | via | Holes are drilled after all cores are laminated (not etched into pads) to guarantee hole-to-pad alignment across layers; drilling is followed by desmear/etchback before plating | — | — | PTH fabrication | review | p.8–9 | high |
| MITZ-006 | fab | Layer registration uses fiducials and tooling holes that slide onto guide pins; registration is critical so pads on each layer align when holes are drilled | — | fiducials, tooling holes | Multilayer | inspect | p.8 | high |
| MITZ-007 | pdn | Plane layers provide low-impedance (resistance and inductance) connections to power and ground and access to power/ground at any board location | — | — | Multilayer with plane layers | review | p.10 | high |
| MITZ-008 | solder | Every through-hole pin connected to a copper plane must use a thermal relief to limit heat conduction during soldering while keeping electrical continuity | — | plane-connected PTH pins | Plane layers; Fig. 1.14 | inspect | p.10, Fig. 1.14 | high |
| MITZ-009 | via | A via passing through a plane it must not connect to gets a clearance (antipad) larger than the normal pad size, etched into the plane, to keep the plane isolated from the plated hole | antipad > pad diameter | via pad dia, plane clearance | Plane layers; Fig. 1.15 | inspect | p.10, Fig. 1.15 | high |
| MITZ-010 | solder | Soldermask protects outer copper from oxidation and prevents solder bridges between closely spaced pads; openings are made only where components are soldered | — | mask openings | All boards with mask | inspect | p.10 | high |
| MITZ-011 | via | Small or densely placed vias should be tented (no mask opening) to keep flux from being trapped in the hole and to prevent solder migration into the hole, which causes poor joints on small components close to and connected to the via | — | via list, mask openings | Vias near/under small SMT pads | inspect | p.10–11 | high |
| MITZ-012 | fab | Fabrication deliverables: one artwork (Gerber) file per etch layer, per soldermask, per silkscreen, per solder paste, per assembly layer, plus route (outline) file and drill file; PCB Editor generates ~30 layer files | — | layer list | See Table 1.1 in §2 | inspect | p.14–15, Table 1.1 | high |
| MITZ-013 | assembly | Solder-paste layer (top and bottom) is used to make the stencil; assembly layer contains part type, position and orientation for assemblers — both are assembly, not fabrication, files | — | — | Reflow assembly | inspect | p.14–15 | high |
| MITZ-014 | process | Design flow: (1) set up project, (2) schematic, (3) netlist to layout, (4) board outline, (5) place parts within outline, (6) route, (7) generate manufacturing data | — | — | Any PCB | review | p.17, p.40 | high |
| MITZ-015 | dfm | Board outline generates a route keep-in (edge of any plane layer and boundary traces must stay within) and a package keep-in (all components must reside within); default edge clearance 400 mil, example uses 200 mil | edge clearance default = 400 mil (10.16 mm); example 200 mil | board outline, keep-ins | KiCad equivalent: copper-to-edge clearance + courtyard-to-edge | inspect | p.29–30 | high |
| MITZ-016 | process | After routing, run DRC and read the DRC report before generating artwork; DRC errors listed by type | DRC violations = 0 | DRC report | Any board | inspect | p.38 | high |
| MITZ-017 | process | Schematic wires must snap to grid; an unconnected-looking pin box that persists means the wire is not connected and netlisting will fail | — | schematic | Schematic entry (ERC/netlist) | inspect | p.24–25 | high |
| MITZ-018 | emc | Floating copper islands (pieces of planes/shapes detached from the main shape by spacing around pin groups) must be deleted — they become EMI issues | count(unconnected copper islands) = 0 | copper zones | All plane/pour layers; KiCad "remove islands" | inspect | p.51, §3 | high |
| MITZ-019 | pdn | Copper areas on plane layers should be dynamic (self-healing, DRC-aware) shapes so clearances to pins/vias are generated automatically; static filled rectangles on planes may not connect to pins properly | — | plane shapes | Plane layers | inspect | p.51, §3 | high |
| MITZ-020 | fab | Artwork output format: RS-274X is the most common Gerber format; the fabricator specifies which files/format it needs | — | — | Fab package | review | p.65, §3 | high |
| MITZ-021 | fab | A Gerber D-code is an aperture (size/shape) index; thermal reliefs connecting PTHs to planes are produced with flash symbols (e.g., D11); each layer has its own aperture list | — | — | Gerber generation | review | p.66, §3 | high |
| MITZ-022 | process | Keep the DRC status current before any export; a non-green DRC status means DRC is stale or errors exist — update and run the DRC report | DRC up to date AND errors = 0 | — | Before artwork | inspect | p.59, §3 | high |
| MITZ-023 | process | Yield requires three things: (1) manufacturable within standard fabrication allowances (SFAs) and assemblable, (2) performs (mechanical fit, environment: temperature/vibration/humidity; electrical: power, I/O, immunity, emissions), (3) reliable over expected life | yield = boards entering service / boards manufactured (%) | — | Any product | review | p.68, §4 | high |
| MITZ-024 | requirements | Select an IPC performance class: Class 1 general electronic (consumer, no extended life), Class 2 dedicated service (communications, instrumentation, sensors; repairable, stricter test), Class 3 high reliability (critical medical, weapons; wide environment, reworkable), Class 3/A military/space avionics. Class sets allowed copper-plating thickness variation, feature location tolerance, hole diameter tolerance | class ∈ {1, 2, 3, 3/A} | product end use | IPC-7351B §1.3; IPC-CM-770E §1.2.1; IPC-D-330 §1.1.42.6 | review | p.71, §4 | high |
| MITZ-025 | requirements | Select an IPC producibility level: Level A general design (preferred complexity), Level B moderate (standard complexity), Level C high (reduced producibility); smaller features (trace widths etc.) require stricter tolerances and raise level | level ∈ {A, B, C} | min feature sizes | IPC-7351B §1.3.1; IPC-CM-770E §1.2.2; IPC-D-330 §1.1.42.6 | review | p.71–72, §4 | high |
| MITZ-026 | requirements | Declare IPC fabrication type: Type 1 single-sided; Type 2 double-sided; Type 3 multilayer without blind/buried vias; Type 4 multilayer with blind and/or buried vias; Type 5 multilayer metal-core without blind/buried; Type 6 multilayer metal-core with blind/buried. Higher number = more sophistication | type ∈ {1..6} | layer count, via types | IPC-CM-770E §1.2.3 | review | p.72, §4 | high |
| MITZ-027 | requirements | Declare assembly subclass: A THD only; B SMD only; C mixed THD/SMD simple; X complex THD/SMD fine pitch + BGA; Y complex ultrafine pitch + CSP; Z complex fine pitch + flip-chip. Higher-performance-class boards are made more reliable by stricter producibility levels and lower (easier) fabrication types/assembly subclasses | subclass ∈ {A,B,C,X,Y,Z} | component technologies | IPC-CM-770E §1.2.2 | review | p.72, §4 | high |
| MITZ-028 | dfm | Choose IPC-7351B land-pattern density level: A = most land protrusion (largest courtyard, least density), B = nominal (median), C = least protrusion (smallest courtyard, highest density) | density ∈ {A,B,C} | board density, routing difficulty | IPC-7351B §1.4 | review | p.72, §4 | high |
| MITZ-029 | fab | Manufacturing tolerances (drill location/diameter, plating, etching, soldermask resolution) accumulate at each step; importance rises with layer count and as line width/spacing decrease — always confirm the specific fabricator's capabilities, not just the IPC minimum | — | layer count, min width/space | All boards | review | p.73, §4 | high |
| MITZ-030 | via | The PTH is the most misregistration-vulnerable feature (many layers, many steps): combined hole-diameter, hole-location and land tolerances can cause loss of annular ring and land breakout; PTHs may function with breakout but reliability is greatly reduced — design annular ring allowances per Table 5.14/5.15 | annular ring ≥ per class (see MITZ Table 5.14) | drill tol, location tol, land size | All PTH | calc | p.73, Fig. 4.1–4.2, §4 | high |
| MITZ-031 | dfm | Standard copper-clad panel sizes: 16 sizes A1..D4 (letter = x: A 2.4, B 4.7, C 7.1, D 9.5 in; number = y: 1 3.2, 2 6.7, 3 10.2, 4 13.8 in); choose board dimensions to maximize boards per standard panel when free to do so | see Table 4.1 | board L × W | ANSI/IPC-D-322; IPC-2221B Fig. 1 | calc | p.74–75, Table 4.1 | high |
| MITZ-032 | dfm | Tooling area from board outline edge to panel boundary is 0.375–1.5 in (typically 1.0 in); on panelized designs the distance between board outlines is typically 0.1–0.5 in | tooling margin 0.375–1.5 in (typ 1.0 in); board-to-board 0.1–0.5 in | panel, board outline | ANSI/IPC-D-322; IPC-D-330 §2 Table 2-6 p.9 | calc | p.75, §4 | high |
| MITZ-033 | dfm | Very small boards must be panelized (breakaway tabs / tab routes or V-scores) and very large boards need special fixtures (sag) for automated soldering; automated equipment has min and max board size limits | — | board size | Automated assembly | review | p.75, p.88 | high |
| MITZ-034 | stackup | Typical finished board thicknesses: 0.020, 0.030, 0.040, 0.062, 0.093, 0.125, 0.250, 0.500 in (0.51, 0.76, 1.02, 1.6, 2.4, 3.2, 6.4, 12.7 mm); pick one of these unless there is a reason not to | see Table 4.2 | finished thickness | Standard fab | review | p.75–76, Table 4.2 | high |
| MITZ-035 | stackup | Core (laminate without copper) thickness must be chosen from standard ranges (Table 4.3: 0.98–250 mil); prepreg from standard glass styles (Table 4.4: 106, 1080, 2313, 2116, 2165, 2157, 7628 = 1.5–7.8 mil uncured); cured prepreg between signal layers ends up thinner than between plane layers because signal copper sinks into the prepreg | see Tables 4.3, 4.4 | stack-up | Controlled-impedance boards | review | p.76, Tables 4.3–4.4 | high |
| MITZ-036 | via | Electroless copper plating thickness is typically 20–100 uin in holes and on surfaces; finished PTH wall thickness is usually 1 mil (25 um) or less; minimum plating per IPC-2221B Table 4-2: Class 1&2 avg 0.79 mil (0.020 mm)/thin 0.71 mil (0.018 mm); Class 3 avg 0.98 mil (0.025 mm)/thin 0.79 mil (0.020 mm) | see Table 4.5 | class | PTH design | review | p.76–78, Table 4.5 | high |
| MITZ-037 | current-carrying | Use finished (not nominal) copper thickness for current and impedance calculations: nominal vs internal/external minimum finished thickness by oz weight per Table 4.6 (±10%); e.g., 1 oz nominal 1.35 mil, internal min finished 0.98 mil, external min finished 1.89 mil | see Table 4.6 | copper weight, layer (int/ext) | Current capacity, impedance | calc | p.77–78, Table 4.6 | high |
| MITZ-038 | dfm | Thicker copper takes longer to etch and increases trace-width variation and etchback (undercut); the etched trace wall is sloped — use the wider (bottom, mask-defined) width W, not the top width w0, for design calculations | W_design = mask width (bottom) | copper weight | Etched boards | calc | p.78–79, Fig. 4.3 | high |
| MITZ-039 | dfm | Trace width tolerance ranges from ±4.0 to ±0.6 mil for 1.5 oz copper depending on producibility level and plating; account for it in controlled-impedance and current-carrying width calculations | width tol = ±0.6..±4.0 mil (1.5 oz) | level, plating | MIL-STD-275 | calc | p.79, §4 | high |
| MITZ-040 | dfm | Minimum trace width and spacing per IPC-2221B is 3.9 mil; typical fabricator minimum trace widths are 4–8 mil; make traces as wide as practical | w_min ≥ 3.9 mil (0.1 mm) (IPC-2221B); typical ≥ 4–8 mil | trace widths, spacings | General design | inspect | p.79, §4 | high |
| MITZ-041 | fab | Specify drill sizes from the standard twist-drill set (ANSI B94.11M); fabricators may round the requested hole up or down to an available bit — rounding changes annular ring width and can cause breakout; IPC-D-330 §2 Table 2-4 lists minimum PTH size by board thickness and class | drill ∈ standard set | hole sizes | PTH/NPTH | review | p.79, §4 | high |
| MITZ-042 | via | Plating can add as much as 1 mil on all surfaces, so finished hole diameter can be up to 2 mil smaller than the drill diameter; the padstack drill size is the FINISHED hole size (fab compensates the drill) — critical when lead diameter is close to hole diameter | d_finished = d_drill − 2·t_plate, t_plate ≤ 1 mil | drill dia, lead dia | PTH | calc | p.80, §4 | high |
| MITZ-043 | via | Excessive desmear/etchback can cause partial delamination, internal shorts (with misregistration) and enlarge the hole — one reason adequate clearance (antipad) is required between a PTH and a ground plane | — | antipad clearance | PTH through planes | review | p.80, §4 | high |
| MITZ-044 | via | Aspect ratio (board thickness : plated hole diameter) should be 3:1 to 5:1 for Level A boards (3:1 a good target); 6:1–8:1 for Level B; Level C may be 9:1 or higher; too-high AR causes incomplete plating (opens) and barrel cracking | AR = T_board / d_hole; Level A ≤ 5 (target 3), Level B ≤ 8, Level C ≥ 9 allowed | board thickness, min finished hole | IPC-2221B Table 5-1 p.40; IPC-CM-770E; IPC-D-330 Table 6-30; Coombs p.42.3 | calc | p.80, §4 | high |
| MITZ-045 | solder | Soldermask openings must be oversized relative to lands: liquid screen-printed masks 16–20 mil oversize; photoimageable masks 0–5 mil oversize (IPC-2221B); library footprints commonly carry 0–10 mil; confirm with the fabricator who applies the oversize | mask_expansion = 0–5 mil (LPI) or 16–20 mil (liquid screen) | mask type | All SMT/PTH lands; especially small parts (SOT23) | inspect | p.80–81, §4 | high |
| MITZ-046 | assembly | Orient all polarized components (capacitors, diodes) the same direction and all ICs with pin 1 in the same direction to reduce manual/automated assembly defects and ease inspection/test | — | placement | All boards | inspect | p.84, p.90 | high |
| MITZ-047 | assembly | Through-hole components are usually placed only on the top side so leads can be wave soldered without exposing the component body to molten solder; automated THD sequence: DIPs, then axial, then radial, then odd-form | — | placement | Wave-soldered boards | inspect | p.84–85 | high |
| MITZ-048 | assembly | Automated placement rates: THD 20,000–40,000 CPH; SMD 10,000–100,000 CPH (use for assembly-time/cost estimates) | THD 20k–40k CPH; SMD 10k–100k CPH | part counts | Cost/time estimate | calc | p.84–85 | high |
| MITZ-049 | assembly | Double-sided SMD with same paste on both sides: put all heavy components on the side that is assembled in the second reflow pass so they do not fall off during the second reflow | — | component mass, side | Two-pass reflow | inspect | p.85 | high |
| MITZ-050 | assembly | Mixed THD + double-sided SMD requires sequential reflow (top SMD) → THD insert → glue-dot bottom SMD → adhesive cure → wave (THD leads + bottom SMD); each extra assembly phase adds cost, failure points and rework difficulty — minimize phases | phases = f(sides, technologies) | placement | Mixed technology | review | p.85, p.90 | high |
| MITZ-051 | assembly | Wave-soldered (bottom-side) SMDs: very small parts (glue dot larger than part oozes onto pads) and large tantalum capacitors / plastic-leaded chip carriers (thermal-stress cracking) are problematic — do not place PLCCs or large tantalums on the wave side | — | bottom-side parts | Wave soldering | inspect | p.86, p.90 | high |
| MITZ-052 | assembly | Wave-soldered SMDs must be oriented relative to board travel so smaller parts are not shadowed by larger parts and so IC lead rows are parallel to travel; add solder thieves (extra or enlarged/extended pads) after the trailing last two pads of SMD ICs to prevent bridging | — | travel direction, orientation | Wave soldering SMD | inspect | p.87–88, Fig. 5.3 | high |
| MITZ-053 | via | When top-side SMDs are reflowed and the board is later wave soldered, fan-out vias must be ≥ 20 mil (0.5 mm) from via edge to pad edge to prevent solder re-reflow wicking down the via (heat conducts up the barrel) | s(via edge, pad edge) ≥ 20 mil | via/pad geometry | Reflow then wave; IPC-7351B | calc | p.88, §5 | high |
| MITZ-054 | assembly | Reflow: do not cluster all thermally massive parts in one board area — thermal gradients cause poor joints in cooler areas and tombstoning of small parts whose pads melt at different times | — | part thermal mass, placement | Reflow | inspect | p.89 | high |
| MITZ-055 | assembly | Placement rules: uniform spacing/alignment; component edges parallel to board edges (except wave-solder orientation); THD on a single side opposite the solder; connectors on the short board side for automated soldering when possible; leave edge space for handling and mounting hardware | — | placement | All boards | inspect | p.90, items 1–3, 10–11 | high |
| MITZ-056 | dfm | Placement grid: 100 mil (2.5 mm) preferred; 20 mil (0.5 mm) or 2 mil (0.05 mm) if leads are off standard grid (IPC-2221B §5.4.2, §8.1.2); metric grids 2.54, 1.27, 0.64, 0.50 mm (IPC-7351B); boards for bed-of-nails test use a 0.100 in (2.54 mm) grid | grid ∈ {100, 20, 2} mil or {2.54, 1.27, 0.64, 0.50} mm; ICT boards 100 mil | placement | All boards | inspect | p.90, items 6–7 | high |
| MITZ-057 | assembly | Add fiducials (global and local) when machine-vision-assisted assembly is used | — | fiducial list | Automated assembly | inspect | p.90, item 9 | high |
| MITZ-058 | mechanical | Components weighing more than 5.0 g per lead must be mechanically supported (not solder-only) if the board experiences vibration | m_part / n_leads > 5.0 g → support required | part mass, lead count | Vibration environments; IPC-2221B §5.2.7 p.43 | calc | p.90, item 12 | high |
| MITZ-059 | emc | Mixed-signal boards: segregate analog from digital components to minimize switching-noise coupling; segregate high-power from low-power/low-noise circuits; electrical considerations take priority over mechanical unless mechanical failure would result | — | placement partitions | Mixed-signal | inspect | p.90, items 14–15 | high |
| MITZ-060 | dfm | Axial THD minimum spacing (Table 5.1): side-to-PCB-edge a = 75 mil (1.9 mm); end-to-PCB-edge b = 90 mil (2.29 mm); end-to-end 100 mil (2.54 mm); side-to-side 100 mil (2.54 mm) when body diameters < 100 mil; when D2 > D1 > 100 mil: a = 70 + D1/2 mil, b = 10 + D1/2 + D2/2 mil (a, b ≥ 100 mil) [mm: a = 1.78 + D1/2, b = 0.25 + D1/2 + D2/2, ≥ 2.54 mm]; side-to-end when any body diameter > 100 mil: 95 + D1/2 mil (2.41 + D1/2 mm) | see Table 5.1 | body diameters D1, D2 | IPC-2221B Fig. 7-1 p.68 | calc | p.91, Table 5.1 | high |
| MITZ-061 | dfm | Radial THD minimum spacing (Table 5.2): to PCB edge r = max(D/2, H/2) and r ≥ 60 mil (1.52 mm); to other parts r = max(D/2, H/2) | r_edge = max(D/2, H/2, 60 mil); r_part = max(D/2, H/2) | body dia D, height H | Radial THD | calc | p.92, Table 5.2 | high |
| MITZ-062 | dfm | THD IC (DIP) minimum spacing (Table 5.3): side-to-PCB-edge a = 100 mil (2.54 mm); end-to-edge b = 75 mil (1.91 mm); end-to-end 200 mil (5.08 mm); side-to-side 100 mil (2.54 mm). A placement DRC that only checks place-outline overlap can pass while violating these IPC values | see Table 5.3 | DIP outlines | THD ICs | calc | p.92–93, Table 5.3 | high |
| MITZ-063 | dfm | THD discrete-to-IC minimum spacing (Table 5.4): discrete side to IC (D1 > 100 mil): a = 115 + D1/2 mil (2.91 + D1/2 mm); discrete end to IC end (D < 100 mil): b = 200 mil (5.08 mm); discrete side to IC side (D < 100 mil): c = 100 mil (2.54 mm); discrete end to IC (D1 > 100 mil): d = 40 + D1/2 mil (1.02 + D1/2 mm) | see Table 5.4 | body dia D/D1 | Mixed THD | calc | p.93, Table 5.4 | high |
| MITZ-064 | dfm | Hole-to-hole (plated or nonplated) spacing: must not violate pad spacing rules AND residual laminate between holes must be > 20 mil (0.5 mm); jumper wires (any direction) 100 mil (2.54 mm) | laminate web ≥ 20 mil; jumper pitch 100 mil | hole positions, diameters | All boards | calc | p.93, Table 5.5 | high |
| MITZ-065 | dfm | Discrete SMD minimum spacing (Table 5.6): side or end to PCB edge 60 mil (1.5 mm); end-to-end / side-to-side 20 mil (0.50 mm) for 0603 and larger, 12 mil (0.30 mm) smaller than 0603; pad to via 20 mil (0.50 mm) | see Table 5.6 | package size | IPC-2221B p.73; IPC-7351B Tables 3.5–3.8, Fig. 3.15 | calc | p.94, Table 5.6 | high |
| MITZ-066 | dfm | IC SMD minimum spacing (Table 5.7): component side/end to PCB edge 60 mil (1.5 mm); end-to-end (body) 20 mil (0.50 mm); side-to-side (pad to pad) 20 mil (0.50 mm) | see Table 5.7 | outlines/pads | IPC-2221B p.73; IPC-7351B Tables 3.2–3.22 | calc | p.94–95, Table 5.7 | high |
| MITZ-067 | dfm | Mixed SMD discrete/IC, or mixed THD/SMD: use the greater of the applicable spacing rules for the components involved (usually the THT spacing governs) | s = max(rule_i) | — | Mixed technology | calc | p.95 | high |
| MITZ-068 | dfm | Library footprints (vendor or tool) do not necessarily meet a specific IPC density level; to build a Level C (or Level A high-yield) board, modify or create footprints to that level; if the tool DRC only checks place-outline overlap, set the placement grid conservatively and check spacing manually against Tables 5.6/5.7 | — | footprint library | Any board with density target | review | p.95, p.102 | high |
| MITZ-069 | components | SMD land-pattern source priority: (1) copy/adapt an existing library footprint with the same lead geometry, (2) manufacturer datasheet recommended land pattern, (3) IPC-7351 land-pattern calculator, (4) derive from datasheet/JEDEC package dimensions with Eqs. 5.1–5.2 | — | datasheet, JEDEC MS/MO number | New footprints | review | p.96 | high |
| MITZ-070 | components | SMD pad must be larger than the lead by the solder-fillet allowances JT (toe), JH (heel), JS (side) per IPC-7351B pp.10–21; nominal (density B) values in Tables 5.8–5.10 | JT, JH, JS by package | package type | SMD footprints | calc | p.98–100, Tables 5.8–5.10 | high |
| MITZ-071 | components | Max SMD pad width (along lead) per Eq. 5.1 (derived from IPC-7351B, without IPC rounding): WP(MAX) = E_MIN − (E_MAX − 2·L_MIN) + 2·JT + 2·JH + 2·sqrt(E_TOL² + F² + P²) as printed (radical extent ambiguous in extraction; equivalent IPC-7351B form: pad length = (Z − G)/2 with Z = E_MIN + 2JT + sqrt(E_TOL² + F² + P²), G = (E_MAX − 2L_MIN) − 2JH − sqrt(E_TOL² + F² + P²)); E = lead-span (toe-to-toe) min/max, E_TOL = E_MAX − E_MIN, L = soldered lead length, F = fab tolerance (IPC-2221B, typically 0.1 mm / 4 mil), P = placement tolerance (typically 0.15 mm / 6 mil) | see formula | E_MIN, E_MAX, L_MIN, JT, JH, F, P | Gull-wing/SO packages | calc | p.100, Eq. 5.1 | medium |
| MITZ-072 | components | Max SMD pad height (across lead) per Eq. 5.2: HP(MAX) = b_MIN + 2·JS + sqrt(b_TOL² + F² + P²); b = lead width, b_TOL = b_MAX − b1_MIN (JEDEC), JS from Table 5.10, F = 0.1 mm (4 mil) typical, P = 0.15 mm (6 mil) typical | HP = b_min + 2JS + sqrt(b_tol² + F² + P²) | b_MIN, b_TOL, JS, F, P | SMD footprints | calc | p.100, Eq. 5.2 | high |
| MITZ-073 | dfm | Fabrication tolerance F = 0.1 mm (4 mil) typical (IPC-2221B); pick-and-place placement tolerance P = 0.15 mm (6 mil) typical (machine-dependent) — use these in land-pattern tolerance RSS | F = 4 mil; P = 6 mil | — | Land-pattern design | calc | p.100 | high |
| MITZ-074 | dfm | IPC-7351B courtyard = component outline + land pattern + courtyard excess; the excess sets minimum component separation; courtyard excess by density level per Table 5.11 (e.g., SOG/SOJ/SO/chip≥0603/tantalum/MELF/LCC: A 20 mil (0.50 mm), B 10 mil (0.25 mm), C 4 mil (0.10 mm); chip < 0603: A 8 mil (0.20), B 6 mil (0.15), C 4 mil (0.10); butt joints: A 59 mil (1.50), B 31 mil (0.80), C 8 mil (0.20)) — KiCad courtyard layer should include this excess | see Table 5.11 | package, density level | SMD footprints; IPC-7351B Tables 3-2..3-22 | inspect | p.101–102, Table 5.11 | high |
| MITZ-075 | components | Tool place-boundary (courtyard) outlines in stock libraries often have zero courtyard excess (do not include space at body ends or around leads); add IPC excess when density-level compliance matters | excess > 0 per Table 5.11 | footprint courtyards | Library audit | inspect | p.101–102, Fig. 5.11 | high |
| MITZ-076 | components | Axial THD pad spacing: LP = LB + 2·(R + LA), where LB = body length, R = bend radius allowance, LA = lead extension from body end to bend start (Table 5.12 by lead diameter DL: DL < 31 mil → R = 1.0·DL, LA = 31 mil; 31 ≤ DL ≤ 47 → R = 1.5·DL, LA = DL; DL > 47 → R = 2.0·DL, LA = DL); then snap LP to nearest standard grid (usually 100 mil) | LP = LB + 2(R + LA) | LB, DL | Axial THD; IPC-CM-770E §11.1.8 | calc | p.104, Eq. 5.3, Table 5.12 | high |
| MITZ-077 | mechanical | Total length of both leads of an axial component (LP − LB) must not exceed 1 in (25 mm) unless the component is mechanically supported | LP − LB ≤ 1.0 in (25 mm) | LP, LB | Axial THD | calc | p.104 | high |
| MITZ-078 | via | PTH failure points are breakout (annular ring loss from misalignment) and opens from thermal stress/cycling during soldering and rework; design PTH by: lead-to-hole ratio, aspect ratio, annular ring, plane clearance, fabricator capability | — | — | THD padstacks | review | p.104–105 | high |
| MITZ-079 | components | PTH drill size, method 1 (IPC-2221B + Coombs §42.2.1): DH = (DL + 2·TP) × k; DL = lead diameter, TP = hole plating thickness (use 1 mil if unknown), k = tolerance factor with 1.05 < k ≤ 3.0 (1.5 recommended); finished hole = DH − 2·TP. Example DL = 32 mil → DH = (32 + 2)·1.5 = 51 mil, finished 49 mil. Clearance grows with lead diameter and may become too large for capillary action at large DL | DH = (DL + 2TP)·k; d_fin = DH − 2TP | DL, TP, k | THD; hole must let lead slip in but not defeat capillary solder rise | calc | p.105, Eq. 5.4 | high |
| MITZ-080 | components | PTH hole size, method 2 (IPC-2222A Table 9-5 p.25, Table 5.13): finished hole minimum = max lead diameter + (Level A 10 mil/0.25 mm; B 8 mil/0.20 mm; C 6 mil/0.15 mm); finished hole maximum = min lead diameter + (A 28 mil/0.70 mm; B 28 mil/0.70 mm; C 24 mil/0.60 mm). Example: 32 mil ±10% lead → 35.2/28.8 mil → Level A hole 45.2–56.8 mil | d_min = DL_max + Δmin(level); d_max = DL_min + Δmax(level) | DL_max, DL_min, level | THD | calc | p.105–106, Table 5.13 | high |
| MITZ-081 | components | PTH pad (land) diameter per IPC-2221B p.96: DP = a + 2·b + c; a = finished hole (DH − 2TP); b = minimum annular ring (Table 5.14, IPC-2221B Table 9-2: internal 1 mil/0.025 mm, external 2 mil/0.05 mm); c = standard fabrication allowance (Table 5.15, IPC-2221B Table 9-1: Level A 16 mil/0.40 mm, B 10 mil/0.25 mm, C 8 mil/0.20 mm). Example: 50 mil drill, TP 1 mil, external, Level A: (50 − 2) + 2·2 + 16 = 68 mil | DP = a + 2b + c | a, level, layer (int/ext) | THD/via padstacks | calc | p.106–107, Eq. 5.5, Tables 5.14–5.15 | high |
| MITZ-082 | solder | Too large a PTH pad only increases heat needed for the joint; too small a pad gives a weak joint and lifts under heat or mechanical stress — use Eq. 5.5, not arbitrary oversize | — | DP | THD | review | p.106 | high |
| MITZ-083 | via | Nonfunctional lands (pads on layers with no connection): use on internal layers when possible (IPC-2222A §9.1.4 p.23); not required on every layer if the board is over 10 layers; not required on plane layers | — | padstack per-layer pads | Multilayer | review | p.107 | high |
| MITZ-084 | via | Plane-to-PTH clearance: trace-to-trace spacing requirements (Table 6.8) apply to plane edge vs. PTH/land (IPC-2221B §6.3.1 p.57); minimum plane-edge to internal nonfunctional land or plated-hole edge = 10 mil (0.25 mm), i.e., antipad diameter = drill diameter + 20 mil (0.51 mm) (IPC-2222 p.22 Fig. 9-1); purposes: fab allowance, avoid plating-solution wicking shorts, voltage withstand | antipad_dia ≥ drill + 20 mil AND (antipad − drill)/2 ≥ Table 6.8 spacing for the voltage | drill dia, voltage | Vias/PTH through planes | calc | p.107–108 | high |
| MITZ-085 | via | If the via/PTH land is larger than the plane clearance diameter, land and plane overlap (even if edge clearance d meets IPC) → capacitive coupling that alters trace characteristic impedance and can cause crosstalk at high frequency; require clearance diameter > land diameter | antipad_dia > land_dia | padstack | Plane layers | calc | p.108, Fig. 5.15 | high |
| MITZ-086 | return-path | Keep plane clearance diameters no larger than necessary: closely spaced pins (connectors, sockets) merge antipads into slots in the ground/return plane; signals crossing the slot force return current around it and increase loop inductance | no merged antipad slots under signal crossings | connector pin pitch, antipad | High-speed digital / high-frequency analog | inspect | p.108 | high |
| MITZ-087 | solder | Soldermask opening is typically larger than the land; a 5 mil oversize is a common fabricator requirement; if the fabricator does not adjust automatically, set it before artwork generation | mask_expansion ≈ 5 mil unless fab specifies | padstack mask layers | All | inspect | p.108 | high |
| MITZ-088 | assembly | Solder paste aperture is usually the same size as the external land; stock library footprints may lack paste definitions — verify every SMD footprint has paste layers defined for the assembly process | paste = land (1:1) unless specified | footprint paste layers | Reflow | inspect | p.109 | high |
| MITZ-089 | requirements | Three SI/EMC goals for every PCB: (1) immune to interference from other systems, (2) no emissions that disturb other systems (FCC rules apply, e.g., 47CFR15), (3) required signal quality; ringing/reflections are PCB problems, while clipping, slew-rate, GBW and intrinsic noise are circuit-design problems — do not attribute them to layout | — | — | All boards | review | p.113–115 | high |
| MITZ-090 | emc | Contact (1/f, excess) noise from poor connectors and solder joints is large at low frequency — specify good-quality connectors and reliable joints for low-level analog | — | connector grade | Low-level analog | review | p.113 | high |
| MITZ-091 | return-path | Magnetic field of a straight conductor B = μ0·I/(2·π·r) (Wb/m²; μ0 = 4π×10⁻⁷ Wb/(A·m)); flux Φ = B·A·cos(θ); induced emf E = −dΦ/dt; L = N·Φ/I (N = 1 for a trace and its return); L = μ0·n²·A·l (volume-proportional) — loop inductance scales with the loop volume/area, so minimize signal-to-return separation and loop area | L ∝ loop area; XL = 2·π·f·L | geometry | All signals; Serway refs | calc | p.116–120, Eqs. 6.1–6.6 | high |
| MITZ-092 | return-path | Return path must be as wide as possible (low self-inductance) and as close as possible to the signal path (max mutual coupling, small loop area) — a solid return (image) plane under every signal layer is the standard way; wider return + smaller spacing also raises trace-to-plane capacitance C = ε0·A/d and lowers XC = 1/(2πfC) | plane adjacent to every signal layer | stack-up | All boards | inspect | p.120–122, Eqs. 6.7–6.9 | high |
| MITZ-093 | crosstalk | Crosstalk between unrelated traces falls with separation (r large; XC between traces rises with d) — keep unrelated signals apart and keep each signal close to its own return | see MITZ 3W rule | trace spacing | All | inspect | p.120–122 | high |
| MITZ-094 | grounding | "Ground" is not an equipotential sink: series (daisy-chain / common) return connections create common-impedance coupling (Z_COMMON) so V_R1 ≠ V_R2 ≠ V_S and return-path points are not equipotential; never share a return path between high-power/noisy signals and low-level analog; the parallel (separate-return) scheme is ideal but unroutable at scale — a return plane approximates it | — | net topology | Mixed-signal, high-speed | review | p.122–125, Figs. 6.9–6.11 | high |
| MITZ-095 | grounding | Use IEEE Std 315-1975 (ANSI Y32.2-1975) ground symbols distinctly: Earth GND (direct earth / vehicle frame serving as earth), Noiseless GND (low-noise earth), Safety GND (shock protection), Chassis GND (chassis/frame, may differ from earth), Return (common return); annotate symbol purpose on the schematic | — | schematic symbols | ERC/schematic review | inspect | p.122–123, Table 6.1 | high |
| MITZ-096 | return-path | AC return current follows the path of least impedance (least inductance): directly under the signal trace in the plane, for any trace path, as long as no discontinuities exist in the return plane; returns of two signals are not common as long as their traces do not overlap (on different layers) or come too close | no plane discontinuity under any signal | plane voids, trace overlap | Multilayer with planes | inspect | p.125–126, Fig. 6.12 | high |
| MITZ-097 | pdn | Switching noise: a CMOS gate transition momentarily shorts VDD–VSS through the partially-on pair and CL, causing rail collapse (VDD dip) and ground bounce (VSS rise) that increases roughly linearly with distance from the connector without bypass capacitors; bypass capacitors at every IC hold the rails except very near the switching gate | — | bypass placement | Digital | review | p.126–128, Figs. 6.13–6.14 | high |
| MITZ-098 | decoupling | Every digital IC gets bypass capacitors (purpose: stable PDN, prevent rail collapse/ground bounce); every analog IC gets bypass capacitors acting as low-pass filters to short supply transients before the amplifier | bypass count ≥ 1 per IC supply pin group | BOM/placement | All ICs | inspect | p.128 | high |
| MITZ-099 | emc | Digital switching noise can be 100 mV or more; analog paths at mV/uV levels must not lie between the power connector and noisy digital circuitry on the shared planes (any drop along the path is analog noise) | V_switching_noise ≈ ≥ 100 mV | placement order: connector → analog? → digital | Mixed-signal | inspect | p.128 | high |
| MITZ-100 | return-path | When a signal changes layers through a via, its return current must have an easy path between the two reference planes near the via (stitching via or same-net plane); otherwise HF return currents spread across the plane seeking least inductance | return via within reach of every layer-change via | via list, plane nets | High-speed / HF analog | inspect | p.128 | high |
| MITZ-101 | grounding | Mixed-signal segregation: physically separate analog and digital components AND eliminate common return paths by split planes (isolated areas on one layer with a common reference point), moated planes (local reference for high-speed clocks or sections with own regulated supply), or fully isolated planes (no common reference) | — | plane partitions | Mixed-signal | review | p.129–130, Fig. 6.15 | high |
| MITZ-102 | grounding | Split/isolated analog and digital planes on different layers must NOT overlap (capacitive coupling of noise across the dielectric); either keep them non-overlapping or separate them with a shield plane | overlap area(AGND, DGND on adjacent layers) = 0 OR shield plane between | plane outlines per layer | Mixed-signal stack-ups | inspect | p.130, Fig. 6.16 | high |
| MITZ-103 | grounding | When analog and digital references on different layers must be electrically common (ADC/DAC), connect isolated planes at a single point with a plated through hole (shorting via) or a shorting bar; moated planes are bridged with a shorting bar | one connection point | plane nets | ADC/DAC boards | inspect | p.130–131, Fig. 6.17 | high |
| MITZ-104 | transmission-line | Characteristic impedance Z0 is the instantaneous impedance V_line/I of a uniform LC line before the wave reaches the load; until the wave arrives, the source cannot see the load; RG58 coax is ≈ 52 Ω not 50 Ω | Z0 = sqrt(L0/C0) (lumped model) | L0, C0 | All traces | calc | p.131–133 | high |
| MITZ-105 | transmission-line | EM wave velocity in the dielectric v = 1/sqrt(ε0·εr·μ0·μr) = c/sqrt(εr·μr) = c/sqrt(εr) for PCB polymers (μr = 1); ε0 = 8.89×10⁻¹² F/m [as printed; standard 8.854×10⁻¹²], μ0 = 4π×10⁻⁷ H/m; electrons drift ~1 cm/s — the wave, not the electrons, carries the signal | v = c/sqrt(εr) | εr | All | calc | p.134, Eqs. 6.10–6.13 | high |
| MITZ-106 | transmission-line | Trace capacitance is set by geometry and εr; loop inductance by geometry only (μr = 1); designer controls w fully, t partially (oz selection), h rarely — solve the Table 6.6/6.7 equations for w | — | w, t, h, εr | Controlled impedance | calc | p.135 | high |
| MITZ-107 | transmission-line | Surface microstrip: Z0 = (k/sqrt(εr + 1.41))·ln(5.98·h/(0.8·w + t)) Ω, k = 87 for 15 < w < 25 mil, k = 79 for 5 < w < 15 mil; valid 0.1 < w/h < 3.0, 1 < εr < 15 (FR4 typically 4.0–4.5); C0 = 0.67·(εr + 1.41)/ln(5.98·h/(0.8·w + t)) pF/in; L0 = Z0²·C0/1000 nH/in; tPD = 84.75·sqrt(0.475·εr + 0.67) ps/in; design width w = 7.475·h·exp(−Z0·sqrt(εr + 1.41)/k) − 1.25·t | see formulas (w, h, t in same units) | w, h, t, εr | IPC-2141A; IPC-2251 p.32; Montrose | calc | p.135, Tables 6.2, 6.6 | high |
| MITZ-108 | transmission-line | Surface edge-coupled differential microstrip: Zdiff = 2·Z0·[1 − 0.48·exp(−0.96·d/h)] Ω (Z0 = single-ended surface microstrip); spacing for a target Zdiff: d = −(h/0.96)·ln(2.08 − 1.04·Zdiff/Z0); restriction Z0 < Zdiff < 2·Z0 | see formulas | d, h, Z0, Zdiff | IPC-2251 p.36; Montrose | calc | p.135, Tables 6.2, 6.6 | high |
| MITZ-109 | transmission-line | Embedded microstrip: Z0 = (87/sqrt(εr' + 1.41))·ln(5.98·h2/(0.8·w + t)) Ω with εr' = εr·[1 − exp(−1.55·H/h2)], h2 = dielectric below trace, H = total dielectric height (plane to top of cover); C0 = 1.41·εr'/ln(5.98·h/(0.8·w + t)) pF/in; tPD = 84.75·sqrt(εr') ps/in (or 84.75·sqrt(0.475·εr + 0.67)); width w = 7.475·h2·exp(−x) − 1.25·t, x = Z0·sqrt(εr' + 1.41)/87; valid 0.1 < w/h2 < 3.0, 1 < εr < 15, w and dielectric 5–15 mil (0.127–0.381 mm), 40 < Z0 < 90 Ω. (Alternate IPC-2251 p.32 form with factor [1 − (h1/…)]^0.1 is garbled in extraction — do not use.) | see formulas | w, t, h2, H, εr | IPC-2141A; IPC-2251 p.32–33; Montrose 2000 p.103 | calc | p.135, Tables 6.3, 6.6 | high |
| MITZ-110 | transmission-line | Embedded edge-coupled differential: Zdiff = 2·Z0·[1 − 0.48·exp(−0.96·d/(h1 + h2 + t))] Ω; spacing d = −((h1 + h2 + t)/0.96)·ln(2.08 − 1.04·Zdiff/Z0); restrictions same as embedded microstrip | see formulas | d, h1, h2, t | IPC-2251 p.36 | calc | p.135, Tables 6.3, 6.6 | high |
| MITZ-111 | transmission-line | Symmetric (balanced) stripline: Z0 = (60/sqrt(εr))·ln(1.9·(2·h + t)/(0.8·w + t)) Ω [= (60/sqrt(εr))·ln(1.9·H/(0.8·w + t)) with H = h1 + h2 + t plane-to-plane]; C0 = 1.41·εr/ln(3.81·h/(0.8·w + t)) pF/in; tPD = 84.75·sqrt(εr) ps/in; width w = 1.25·[1.9·H·exp(−Z0·sqrt(εr)/60) − t]; restrictions w/(h − t) < 0.35, w/h < 2.0, t/h < 0.25, 0.005 < w < 0.015 in; line widths and dielectric 5–15 mil, 40 < Z0 < 90 Ω | see formulas | w, t, h, εr | IPC-2141A; IPC-2251 p.33; Brooks 2003 p.203; Montrose | calc | p.135, Tables 6.4, 6.7 | high |
| MITZ-112 | transmission-line | Edge-coupled differential stripline (symmetric): Zdiff = 2·Z0·[1 − 0.347·exp(−2.9·d/(2·h + t))] Ω (Z0 = symmetric stripline) | see formula | d, h, t | IPC-2141A; IPC-2251 p.35 | calc | p.135, Tables 6.4, 6.7 | high |
| MITZ-113 | transmission-line | Asymmetric (unbalanced) stripline: Z0 = (80/sqrt(εr))·ln(1.9·(2·h2 + t)/(0.8·w + t))·[1 − h2/(4·H)] Ω, h2 = distance to nearer plane, H = plane-to-plane spacing; C0 = 2.82·εr/ln(2·(h − t)/(0.268·w + 0.335·t)) pF/in; tPD = 84.75·sqrt(εr) ps/in; width w = 2.375·(2·h2 + t)·exp(−x) − 1.25·t with x = Z0·sqrt(εr)/(80·(1 − h2/(4·H))); restrictions w/(h2 − t) < 0.35, t/h2 < 0.25 | see formulas | w, t, h2, H, εr | IPC-2251 p.33; Montrose 2000 p.105 | calc | p.135, Tables 6.5, 6.7 | medium |
| MITZ-114 | transmission-line | Broadside-coupled differential stripline (symmetric): Zdiff = (82.2/sqrt(εr))·ln(5.98·D/(0.8·w + t))·(1 − exp(−0.6·h)) Ω as printed (D = trace-to-trace vertical spacing, h = trace-to-plane; exponential argument garbled in extraction — verify against IPC-2251 p.35 before use); width w = 7.475·D·exp(−x) − 1.25·t, x = Zdiff·sqrt(εr)/(82.2·(1 − exp(−0.6·h))); tPD = 84.75·sqrt(εr) ps/in | see formulas | w, t, D, h, εr | IPC-2251 p.35 | calc | p.135, Tables 6.5, 6.7 | low |
| MITZ-115 | transmission-line | Lumped L0 for any topology: L0 = Z0²·C0/1000 nH/in with C0 in pF/in (Table 6.2 prints "/12"; the table note gives /1000) | L0 = Z0²·C0/1000 | Z0, C0 | All | calc | p.135, Tables 6.2–6.5 note | high |
| MITZ-116 | transmission-line | Reflection from an open (high-impedance) termination returns with the same polarity and amplitude as the incident wave (rope analogy); the stored inductor energy overcharges the last capacitor and the raised voltage front propagates back to the source | Γ_open = +1 | Z_T | Unterminated lines | sim | p.135, Fig. 6.22 | high |
| MITZ-117 | transmission-line | Edge-coupled differential stripline, symmetric or asymmetric (Table 6.7): Zdiff = 2·Z0·[1 − 0.374·exp(−2.9·d/H)] Ω (Table 6.4 prints coefficient 0.347 with (2h + t) in place of H; IPC-2141A uses 0.347); spacing for target Zdiff: d = −0.347·H·ln[2.67·(1 − Zdiff/(2·Z0))]; asymmetric single-ended Z0 per MITZ-113, symmetric per MITZ-111 | see formulas | d, H, Z0, Zdiff | IPC-2251 p.35 | calc | p.142, Table 6.7 | medium |
| MITZ-118 | termination | Reflection coefficient at any impedance interface: ρ = (Z_T − Z_line)/(Z_T + Z_line), −1 ≤ ρ ≤ +1; open → +1 (same polarity, same amplitude), short → −1 (inverted), matched (Z_T = Z_0) → 0 (no reflection). Reflections occur at BOTH driver–line and line–load interfaces and bounce until absorbed | ρ = (ZT − Z0)/(ZT + Z0) | Z_T, Z_0, R_S | All | calc | p.143–145, Eqs. 6.14–6.16 | high |
| MITZ-119 | transmission-line | Ringing = repeated reflections between mismatched driver and load; overshoot can exceed device absolute-maximum input ratings, radiates more EMI, and over/undershoot crossing logic thresholds causes false triggering; in analog circuits reflections create standing/traveling waves that degrade the signal | overshoot ≤ V_abs_max(input); no threshold re-crossing | ρ_src, ρ_load, PT, RT | Unterminated lines | sim | p.145–146 | high |
| MITZ-120 | transmission-line | Definitions: RT = driver rise time (datasheet); v_P = propagation velocity (from εr and geometry); PT = L_trace/v_P = propagation time; L_SE = v_P × RT = spatial extent of the rising edge (transition distance). If L_trace > L_SE (equivalently RT < PT) the whole edge fits on the line and the reflection is a full-amplitude copy scaled by ρ | PT = L/v_P; L_SE = v_P·RT | L_trace, RT, v_P | All digital nets | calc | p.147 | high |
| MITZ-121 | transmission-line | A trace is electrically long (must be treated as a transmission line: controlled Z0 over its whole length and matched to source/load) unless PT < ½·RT, i.e., L_trace < ½·L_SE = ½·v_P·RT. The ½ rule is a LIMIT, not a goal — shorter traces / slower edges are always better | L_trace < 0.5·v_P·RT (critical length = equality) | L_trace, RT, v_P (or tPD per Tables 6.6/6.7) | All digital nets; also Table 9.10 for worked values | calc | p.148, p.151 | high |
| MITZ-122 | transmission-line | Worked reflection example (Fig. 6.25–6.26): R_S = 10 Ω, Z0 = 50 Ω, R_L = 1 kΩ, VCC = 5 V, PT = 4·RT: V_drive = VCC·Z0/(Z0 + R_S) = 5·50/60 = 4.17 V; ρ_load = (1000 − 50)/(1000 + 50) = 0.90; ρ_source = (10 − 50)/(10 + 50) = −0.67; load overshoot 4.17 + 0.90·4.17 = 7.92 V; then 5.42, 3.16, 4.67 V … decaying to steady state (settling time) | V_step = VCC·Z0/(Z0 + R_S) | R_S, Z0, R_L | Lattice/bounce diagram check | sim | p.147–150 | high |
| MITZ-123 | transmission-line | When L_trace << L_SE (PT << RT), reflections fold back onto the still-rising edge, are smeared, and only small final over/undershoots remain; ring frequency is higher for shorter traces; at exactly PT = ½RT ringing still occurs but peaks never level off and settle sooner | — | PT/RT | Electrically short traces | sim | p.150–152, Figs. 6.27–6.29 | high |
| MITZ-124 | termination | If rise time cannot be slowed or trace shortened, terminate. Full matching R_S = Z0 = R_L (series at source + parallel at load) gives zero reflections but V_load = ½·V_source, which may fail logic thresholds — check V_load ≥ V_IH | V_load = ½·V_source when R_S = Z0 = R_L | V_IH | Double termination | calc | p.152 | high |
| MITZ-125 | termination | Series (source) termination: R_series = Z0 − R_S (driver output resistance); e.g., Z0 = 50 Ω, R_S = 10 Ω → R_series = 40 Ω; only one reflection occurs (a flat step on V_drive lasting one round trip, e.g., 10–20 ns) and it is absorbed at the source; load voltage is near ideal. Caution for high-speed clocks whose on/off time ≈ rise time (the half-amplitude hold is a problem) | R_series = Z0 − R_S | Z0, R_S | Point-to-point digital lines | calc | p.152–153, Fig. 6.31 | high |
| MITZ-126 | termination | Parallel (load) termination: R_parallel = (R_L·Z0)/(R_L − Z0) in parallel with the load so the combination equals Z0 | R_par = R_L·Z0/(R_L − Z0) | R_L, Z0 | Load-end termination | calc | p.153 | high |
| MITZ-127 | emc | Four electrical routing areas: parts placement, layer stack-up, bypass capacitors, trace width/spacing; when electrical and mechanical placement conflict, electrical wins unless mechanical failure would result — but the board must still be manufacturable | — | — | All | review | p.153–154 | high |
| MITZ-128 | emc | Analog placement: follow the signal flow, parts as close together as possible, traces as short as possible, signal path straight (no zigzag, no crossing the board and back); digital: cluster functionally related parts and put the highest-speed clocks/fastest edges closest together to minimize their line lengths | — | placement | Analog / digital | inspect | p.154–155 | high |
| MITZ-129 | emc | Mixed-signal board zoning (Fig. 6.32): highest-power/noisiest circuits (switching regulators, digital) nearest the connector(s), medium next, quietest analog farthest; this limits the return-plane area shared between noisy and quiet circuits; back it with split/isolated planes per Fig. 6.15 | zones ordered connector → noisy → medium → quiet | placement, plane splits | Mixed-signal | inspect | p.155, Fig. 6.32 | high |
| MITZ-130 | stackup | Define the stack-up and board thickness early (before layout) with the fabricator: it fixes layer count and number of power/ground planes; drivers: fabricator capability, routing/part density, analog frequency and digital rise/fall times, cost; high-speed boards may need more layers even at low density for impedance control and shielding; per-layer cost increment drops after 4 layers | — | density, edge rates, cost | All multilayer | review | p.155–156 | high |
| MITZ-131 | stackup | Use an even number of layers (cores + prepreg are pairs; 5 layers costs the same as 6 — use the extra layer as another return plane); even count also minimizes warpage | n_layers mod 2 = 0 | layer count | Multilayer | inspect | p.156 | high |
| MITZ-132 | stackup | Every signal layer must be adjacent and close to a plane layer, preferably a return/GND plane (min loop inductance → min radiation and crosstalk); every power plane should be adjacent and close to a return plane (interplane capacitance reduces supply noise/radiation); if forced to choose, signal-adjacent-to-return wins and extra bypass/bulk capacitors replace lost interplane capacitance | ∀ signal layer: adjacent plane exists | stack-up | Multilayer | inspect | p.156 | high |
| MITZ-133 | stackup | Reference stack-up examples: finished 0.093 in, 1 oz (1.35 mil) copper; table thicknesses (Tables 4.3–4.5) are pre-lamination — signal-layer prepreg ends thinner than plane-layer prepreg because traces sink in; confirm finished dielectric thicknesses with the fabricator before impedance calculation | — | fab stack-up sheet | Controlled impedance | review | p.157 | high |
| MITZ-134 | return-path | Return current uses the plane closest to the signal (power or ground — to AC they are shorted by bulk/bypass capacitors); when a signal changes layers the return may have to detour via a bypass capacitor and the line impedance departs from design; install return-current bridges (free GND-to-GND vias, or capacitors with fan-out vias) adjacent to every signal layer-transition via | stitching via or cap next to each layer-change via | via list | High-speed | inspect | p.157 | high |
| MITZ-135 | stackup | Assign preferred routing directions per layer (H horizontal, V vertical, R nonspecific); alternating H/V on adjacent signal layers makes dense routing efficient and reduces via count; bury high-speed (HS) signals between plane layers for shielding | — | layer plan | Dense / high-speed | inspect | p.157 | high |
| MITZ-136 | transmission-line | Every routed trace is one of three transmission-line types — microstrip, stripline, coplanar — whether intended or not; choose the stack-up so the type and impedance of critical nets are known | — | stack-up | All | review | p.157 | high |
| MITZ-137 | stackup | Four-layer reference stack-ups (Fig. 6.33, 1 oz Cu, dielectrics in mil): (A) Sig-H / GND / PWR / Sig-V with 10 prepreg / 40 core / 10 prepreg → surface microstrip on both outer layers (most common; outer traces allow inspection/rework); (B) GND / Sig-H / Sig-V / PWR, 10/40/10 → unbalanced stripline, planes outside shield traces and contain emissions; (C) GND / Sig-H + PWR pours / Sig-V + PWR pours / GND for low-density dual-supply (±V) analog | see §2 stack-up table | layer count = 4 | Simple digital/analog | review | p.158, Fig. 6.33 | high |
| MITZ-138 | stackup | Six-layer reference stack-ups (Fig. 6.34): (A) Sig-H / GND / Sig-V / Sig-H / PWR / Sig-V, 10/14/10/14/10 → outer surface microstrip, inner asymmetric stripline (put higher-speed signals on the shielded inner layers); (B) Sig / GND / +PWR + Sig / −PWR + Sig / GND / Sig for dual-supply analog (ground adjacent to every signal and power layer); (C) GND / HS-H / GND / PWR / HS-V / GND, 11.5 mil each → two balanced-stripline high-speed layers, only two routing layers | see §2 | layer count = 6 | Digital / dual-supply analog / high-speed | review | p.158–159, Fig. 6.34 | high |
| MITZ-139 | stackup | Eight-layer reference stack-ups (Fig. 6.35): (A) Sig-H / PWR / GND / Sig-V / Sig-H / GND / PWR / Sig-V, 8.7/9.1/8.7/9.1/8.7/9.1/8.7; (B) GND / HS-H / GND / HS-V / PWR / Sig-H / Sig-V / GND, 8 mil each (balanced stripline HS pairs, asymmetric stripline for H/V). Ten-layer (Fig. 6.36): Sig-H / GND / HS / HS / PWR / GND / HS / HS / GND / Sig-V, 5.6/5.3/5.6/5.3/9.1/5.3/5.6/5.3/5.6 | see §2 | layer count = 8, 10 | High-speed digital | review | p.159–160, Figs. 6.35–6.36 | high |
| MITZ-140 | decoupling | Bypass capacitors (a) short HF noise to ground and (b) act as current reservoirs. Power-pin fan-out: (A) IC power pin → bypass capacitor → via to plane (recommended for analog); (B) IC power pin → via to plane → bypass capacitor (recommended for digital); autorouter style with separate fan-out vias for IC and capacitor pins is generally acceptable; assembly method (wave vs reflow) and real estate also drive capacitor orientation | topology per circuit type | bypass routing | All ICs | inspect | p.159–161, Fig. 6.37 | high |
| MITZ-141 | current-carrying | Minimum trace width for temperature rise (derived from IPC-2221B): w[mil] = (1/(1.4·h)) · (I/(k·ΔT^0.421))^1.379 with h = copper weight (oz/ft²; 1.4 mil/oz), I = current (A), ΔT = permissible rise above ambient (°C), k = 0.024 inner layers, k = 0.048 outer layers; sanity anchors (1 oz, ΔT = 10 °C): 6 mil trace ≈ 300 mA inner, ≈ 600 mA outer (Fig. 6.38 graph 0–1 A → 0–35 mil) | w = (I/(k·ΔT^0.421))^1.379/(1.4·h) | I, h, ΔT, layer | Power nets; make power traces as wide as practical | calc | p.161–162, Eq. 6.17, Fig. 6.38 | high |
| MITZ-142 | thermal | FR4 glass-transition temperature is 125–135 °C; as ambient rises the allowed conductor ΔT shrinks and minimum width grows; even at room ambient intentionally restrict ΔT (e.g., specify ΔT = 20 °C when more would be allowed) | Tg(FR4) = 125–135 °C; T_amb + ΔT << Tg | T_amb | Current-capacity design | calc | p.161–162 | high |
| MITZ-143 | transmission-line | Before paying for controlled impedance, decide whether it is needed: digital → PT < ½·RT (RT > 2·PT) using the SMALLER of datasheet rise/fall time; PT = L_trace × tPD (Eq. 6.18); max length L_trace < RT/(2·tPD) (Eq. 6.19); C0 = tPD/Z0 (pF/in with ps/in and Ω), L0 = Z0²·C0/1000 nH/in (IPC-2251 p.32) | L_max = RT/(2·tPD) | RT/FT, tPD (Tables 6.6/6.7) | Digital nets | calc | p.162–163, Eqs. 6.18–6.19 | high |
| MITZ-144 | transmission-line | Analog critical length uses wavelength λ = v_P/f = 1/(f·tPD) of the highest frequency component; literature limits range λ/6 to λ/20; IPC-2251 recommends L_trace < λ/15; example: 66 MHz on surface microstrip, εr = 4.2 → λ = 110.8 in | L_trace < λ/15 (IPC-2251) | f_max, tPD | Analog/RF traces | calc | p.163–164, p.172, Eqs. 6.20–6.21 | high |
| MITZ-145 | transmission-line | Units for h, w, t may be mils, cm, in — but must be consistent; t (oz), h (mil) and εr come from the fabricator; trace width w is the designer's variable | — | fab data | Controlled impedance | review | p.162, p.164 | high |
| MITZ-146 | transmission-line | Coplanar line: typically d < h, w relatively wide, side copper (top-side return) extends > 5·w on both sides; formulas (Wadell 1991) are unwieldy and the type is rarely used on FR4; guard traces/pours with h < d or h ≈ d produce an accidental surface microstrip, not a coplanar line | side pour ≥ 5·w; d < h | d, h, w | RF / guard-trace designs | review | p.164, Fig. 6.39 | high |
| MITZ-147 | compliance | Minimum conductor spacing for voltage withstand (Table 6.8, abridged IPC-2221B Table 6-1): 0–15 V and 16–30 V: internal 2 mil, external bare 4 mil, soldermask-only 2 mil, conformal-coated 5 mil; 31–50 V and 51–100 V: internal 4 mil, external bare 24 mil, soldermask-only 5 mil, conformal-coated 5 mil (voltage = VDC or Vpk-pk between conductors) | see Table 6.8 | net voltage, layer, coating | All nets; also plane-to-PTH clearance (MITZ-084) | calc | p.164–165, Table 6.8 | high |
| MITZ-148 | crosstalk | 3W rule: default edge-to-edge spacing = 1 trace width; crosstalk-susceptible traces must be ≥ 2·w edge-to-edge (3·w center-to-center) — outside ~70% of each other's magnetic field for controlled-impedance lines; 10·w center-to-center → outside ~98% (Montrose 1999 p.210) | s_edge ≥ 2·w (3W); s_center ≥ 10·w for ~98% isolation | w, spacing | Clocks, sensitive analog, high-speed | calc | p.165, Fig. 6.40 | high |
| MITZ-149 | transmission-line | 90° corners: sharp corner widens the trace ×1.414 (12 mil → 16.97 mil; ΔZ0 ≈ 11.5 Ω for εr = 4.2, h = 10 mil); CAD corners drawn with round apertures are rounded outside (12 → 14.49 mil; ΔZ0 ≈ 6.2 Ω); excess copper area 7.73 mil² for a 12-mil trace is insignificant vs. a via/land; measurable reflections only at upper GHz (traces > 50 mil) to THz (< 10 mil); 135° corners acceptable to ~1 GHz (Brooks p.385) — vias dominate discontinuities | avoid 90° only on controlled-impedance lines; 135° OK ≤ 1 GHz | corner geometry | High-speed | review | p.166–168, Figs. 6.42–6.44 | high |
| MITZ-150 | transmission-line | PSpice/SPICE transmission-line test bench (Fig. 6.45): VPULSE V1 = 0, V2 = 5 V, TD = 0, TR = TF = 2 ns, PW = 100 ns, PER = 200 ns; R_source = 10 Ω; ideal T line Z0 = 50 Ω, TD = PT; load R = 1 kΩ ∥ C = 15 pF; reflection coefficients: into line from source +0.667, into source from line −0.667, into load +0.90; specify TD (= tPD × L) for digital, or F and NL (= L/λ) for analog | ρ_src→line = (Z0 − R1)/(Z0 + R1) = 0.667; ρ_line→R1 = −0.667; ρ_line→R2 = 0.90 | R1, Z0, R2, C1 | Ringing simulation (ngspice T/LTRA element) | sim | p.168–170, Fig. 6.45 | high |
| MITZ-151 | transmission-line | Transient step ceiling for TL simulation: maximum step size ≤ 1/1000 of total run time, otherwise the simulation can go unstable | h_max ≤ T_run/1000 | T_run | SPICE transient of T lines | sim | p.170 | high |
| MITZ-152 | transmission-line | Critical length rule with safety factor: L_trace < RT/(k·tPD), k = RT/PT; k = 2 is the maximum recommended length (critical), larger k (shorter) is better; example ALS logic RT ≈ 2 ns, εr = 4.2 surface microstrip (the book's numbers imply tPD ≈ 137 ps/in, i.e., 85·sqrt(0.457·εr + 0.67) as printed in Eq. 9.2; the Table 6.6 coefficient 0.475 gives ≈ 139 ps/in) → critical length 7.3 in; Table 6.9: long 30 in (k ≈ ½, TD 4.1 ns), critical 7.3 in (k = 2, TD 1 ns), safe 3.5 in (k = 4, TD printed 0.24 ns; consistent value ≈ 0.48 ns) | L < RT/(k·tPD), k ≥ 2 | RT, tPD, k | Digital placement/routing | calc | p.170–171, Table 6.9 | high |
| MITZ-153 | components | Use logic-family rise/fall times from datasheets (Appendix C lists RT/FT by family); ALS ≈ 2 ns | RT_ALS ≈ 2 ns | logic family | Digital | review | p.162, p.171 | high |
| MITZ-154 | process | Schematic symbol pins carry one of eight electrical types — Power/GND, Three-state, Bidirectional, Open collector, Open emitter, Input, Output, Passive — and the type (not the graphics) governs ERC results, netlisting and routing; assign types deliberately when creating symbols | pin type ∈ 8 types | symbol library | ERC (KiCad electrical types equivalent) | inspect | p.175–176, Table 7.1 | high |
| MITZ-155 | process | Symbol pin numbers must match footprint pad names exactly (including alphabetic pad names such as "A"/"K" for diodes), otherwise the schematic-to-layout ECO/netlist fails | ∀ pin: pin_number ∈ footprint pad names | symbol, footprint | Library validation | inspect | p.184, p.217 | high |
| MITZ-156 | process | Multi-unit packages sharing power pins: declare shared pins as Power type (visible for analog parts, typically invisible for digital); a "duplicate pin number" netlist warning is ignorable only if the duplicates are Power type | — | multi-unit symbols | Library validation | inspect | p.191–193 | high |
| MITZ-157 | process | Keep user-made parts and models in separate user libraries/folders — never add to the vendor-supplied libraries | — | library paths | Library management | review | p.174 | high |
| MITZ-158 | process | SPICE simulation requires at least one node named 0 (reference ground); any ground symbol works for layout but simulation needs the "0" net | ∃ net "0" | schematic | Simulation setup | inspect | p.211 | high |
| MITZ-159 | process | For simulatable symbols, pin names and pin ORDER in the symbol/SPICE template must match the model's node order exactly, and the implementation/model name must match the .SUBCKT/.MODEL name, or simulation fails; custom model libraries must be added to the simulation profile (global library) | — | symbol template, .lib | Simulation setup | inspect | p.217–218 | high |
| MITZ-160 | process | Subcircuit-model creation flow for non-primitive parts (transformer, IC): (1) draw the equivalent circuit with primitives (e.g., L per winding, series R for winding DC resistance, K_Linear coupling coefficient linking all coils) and simulate with a source and dummy load; (2) verify behaviour (e.g., 1:2 step-up → output = 2× input in transient plot); (3) delete sources/loads/grounds, add hierarchical ports as the pins; (4) export a subcircuit-format netlist (.LIB); (5) generate the symbol from the model | — | datasheet L, R_DC, k | Custom models | sim | p.207–216 | high |
| MITZ-161 | process | Primitive models (.model) can be downloaded from vendor sites as text (.mod) and imported into a user .lib; the model import wizard matches models with the same pin count and requires explicit pin mapping | — | vendor models | Custom models | review | p.205–206, p.218 | high |
| MITZ-162 | components | Minimum footprint content: (1) at least one pin/pad, (2) at least one reference designator, (3) a component outline (silkscreen and/or assembly layer), (4) a place-bound (courtyard) rectangle; optional: device type, value, tolerance, height, part number, route keep-out, via keep-out, extra etch, vias | all 4 present | footprint library | Library lint (KiCad: F.SilkS/F.Fab outline, F.CrtYd) | inspect | p.229, Fig. 8.1, Table 8.2 | high |
| MITZ-163 | components | A padstack defines outer/inner copper pads, thermal relief and antipad (plane clearance), soldermask openings, paste openings and the drill; the plating is NOT part of it (fab-controlled); through-hole padstacks connect any layer to any other; SMD pads exist on one outer layer only and reach other layers through fan-out vias added during layout | — | padstack fields | Library | review | p.227, p.230, Fig. 8.2 | high |
| MITZ-164 | components | Padstack naming convention: through-hole padXcirYd (X = pad OD, cir/sq/rec = shape, Y = drill/finished hole, e.g., pad62cir42d); SMD smdXrecY or smdX_Y (X = width, Y = height) | name encodes geometry | library | Library hygiene | inspect | p.230–231 | high |
| MITZ-165 | fab | Specify the FINISHED hole diameter (what assembly needs), not the tool size; hole tolerance typically ±0.1 mm, ±0.05 mm for press-fit holes; leave drill tool size to the fabricator unless an assembly technique requires a specific hole; nonstandard drilling (laser, plasma, punch) must be declared; through-hole (component) padstacks are always plated per IPC-2581B | tol = ±0.1 mm (±0.05 mm press-fit) | hole list | Drill specification | inspect | p.232 | high |
| MITZ-166 | via | Backdrilling (secondary drill) to remove unused via stub for high-speed signals in thick boards: backdrill tool diameter is usually 0.3–0.4 mm larger than the finished plated hole diameter; counterbore likewise defined as a secondary drill | d_backdrill = d_finished + 0.3..0.4 mm | via list, signal speed | Thick high-speed boards | inspect | p.232–233 | high |
| MITZ-167 | fab | Drill-symbol (drill chart figure) size should be about the hole size or slightly smaller; drill symbols appear only once a drill table/legend is placed | — | drill legend | Fab drawing | inspect | p.233, p.237 | high |
| MITZ-168 | components | Inner-layer regular pads may equal outer pads but are often 0–20 mil smaller in diameter; the plane antipad must be at least as large as the LARGEST pad in the padstack (otherwise capacitive coupling between the larger pad and an adjacent plane), typically 10–20 mil larger than the pad diameter, and never smaller than the trace-spacing constraints in use | antipad_dia ≥ max(pad_dia) + 10..20 mil; (antipad − pad)/2 ≥ min spacing | padstack per layer | THT/via padstacks | calc | p.238 | high |
| MITZ-169 | solder | Soldermask opening larger than the pad: about 2 mil (0.05 mm) per side (p.235) — or 4–8 mil (0.1–0.2 mm) larger in diameter than the outer pad (p.239) — to keep registration error from covering the pad; confirm the value with the fabricator | mask_dia = pad + 4..8 mil (i.e., 2–4 mil/side) | padstack mask | All pads | inspect | p.235, p.239 | high |
| MITZ-170 | assembly | Paste (stencil) opening normally slightly smaller than the pad, about 1 mil (0.025 mm) per side; large pads (thermal pads) must have the paste split into several smaller openings covering not more than 50% of the pad area | paste = pad − 1 mil/side; large pad: paste coverage ≤ 50% split into windows | padstack paste | SMD, exposed-pad packages | inspect | p.235 | high |
| MITZ-171 | mechanical | Flex coverlay openings are smaller than the pad by 2 mil (0.05 mm) per side | coverlay = pad − 2 mil/side | flex padstacks | Rigid-flex | inspect | p.235 | high |
| MITZ-172 | via | "Suppress unconnected internal pads" (remove nonfunctional inner pads) improves manufacturability and signal integrity — use only after confirming the fabricator accepts it (see also MITZ-083) | — | via/PTH padstacks | Multilayer | review | p.235 | high |
| MITZ-173 | components | Worked THT padstack (1/4 W resistor, lead 25 mil, body 250 × 100 mil): IPC Level A gives hole 33–56 mil and pad 51–74 mil; chosen drill 42 mil, pad 62 mil (annular ring 10 mil), pad spacing 400 mil on 100-mil grid; through-hole footprint origin at pin 1, SMD footprint origin at body center | — | lead dia, body | Library convention | calc | p.236, p.239 | high |
| MITZ-174 | components | Silkscreen outline lines need explicit width (about 10 mil; 5 mil used for PGA); zero-width lines/rectangles are ignored in artwork unless a default undefined-line width is set; reference designator text about 31 mil high; assembly outline drawn at actual component size with 1-mil lines | silk width ≥ 5–10 mil; refdes text ≈ 31 mil | footprint graphics | Library lint | inspect | p.242–247, p.250, p.258 | high |
| MITZ-175 | components | Chip-capacitor footprint data (Table 8.3, mil): library smdcap ≈ 2010: pad 87 × 50, pad C/C 195, body 245 × 90, place outline 250 × 90 (smd50_87); IPC 1206: pad 71 × 45, C/C 118, body 126 × 63, place outline 185 × 91 (smd45_71) | see Table 8.3 | package | Chip components | calc | p.248, Table 8.3 | high |
| MITZ-176 | components | PGA/BGA footprint: 22-mil pins on 100-mil pitch → padstack hole 32 mil, pad 50 mil (pad50cir32d), square pad for pin 1, package 860 mil, JEDEC lettering (number right, letter down); wizard courtyards expanded 40 mil per side; bevel the pin-1 corner of the assembly outline | pin 22 mil → hole 32, pad 50 | pin dia, pitch | Array packages | calc | p.252–258 | high |
| MITZ-177 | solder | Thermal relief (flash) geometry: ID = pad diameter on that layer, OD = antipad diameter (± a couple of mils), spoke width W = 60%·P/n where P = pad diameter and n = number of spokes (IPC-2222A pp.21–22); example pad62cir42d inner: ID 60, OD 80, 4 spokes → W = 9 mil; on positive planes OD = ID + 2 × shape-to-pin spacing and spoke width = trace-width constraint | W = 0.6·P/n | P, n | Plane-connected PTH pins | calc | p.258–260, Table 8.4 | high |
| MITZ-178 | components | Reference padstack pad62cir42d (Table 8.4, mil): drill 42; outer pad 62, outer antipad 82, outer pad-to-antipad clearance 10, outer annular ring 10; inner pad 60, inner antipad 80, inner annular ring 9, inner clearance 10 | see Table 8.4 | — | THT padstacks | calc | p.260, Table 8.4 | high |
| MITZ-179 | mechanical | Mounting holes come in four types (plated/nonplated × with/without lands); a mounting hole connected to a net (e.g., chassis/GND) must appear on the schematic as a part with a connection-type padstack (thermal relief or full contact to the plane); unconnected holes are added in layout only | — | hole list, netlist | Mechanical design | inspect | p.263–264, Table 8.5 | high |
| MITZ-180 | mechanical | Nonplated unsupported mounting hole (e.g., mtg125): drill 125 mil, dummy pads 25 mil (drilled away), nonplated, antipad ≥ 20 mil larger than the drill diameter so planes stay clear within fab tolerance; general rule: NPTH antipad ≥ drill + 20 mil | antipad ≥ drill + 20 mil | NPTH list | All NPTH | calc | p.264–265, p.267 | high |
| MITZ-181 | fab | Nonplated holes are drilled after plating, PTHs before — supply separate drill files (name.drl for plated, name-np.drl for nonplated) or a combined file with plating clearly distinguished; Appendix D gives drill vs. screw size table | — | drill export | Fab package | inspect | p.267 | high |
| MITZ-182 | via | Blind vias connect one outer layer to inner layers; buried vias connect inner layers only; both require built-up (sequential lamination) boards where core PTHs become buried vias; microvia types: laser-drilled plated, laser-drilled paste-filled, plasma-etched plated; needed to fan out dense BGAs with components on both sides | — | stack-up, BGA pitch | HDI | review | p.268–270, Fig. 8.47 | high |
| MITZ-183 | mechanical | Attach 3D (STEP) models to footprints and mechanical symbols (including the enclosure) and run collision detection with a minimum spacing (e.g., 0.1 mm) between component surfaces, PCB (rigid or bent flex) and mechanical parts | clearance ≥ 0.1 mm (example) | STEP models | Mechanical fit check (KiCad 3D viewer / MCAD) | inspect | p.272–276 | high |
| MITZ-184 | process | Maintain a parts/footprint spreadsheet from the start (reference, value, mounting package/footprint, datasheet) and keep adding design details through the flow; it is the fault-isolation record when the fabricated board does not fit the parts | every part row: refdes, value, package, footprint, datasheet | BOM | Any design | review | p.282–283, Table 9.1 | high |
| MITZ-185 | process | Pre-netlist checklist: (1) all footprints assigned (generate a BOM listing the footprint field to find blanks), (2) related parts grouped into rooms, (3) annotation performed (check multi-unit parts), (4) design cache cleaned, (5) schematic DRC/ERC clean | footprint field non-empty ∀ parts; ERC errors = 0 | schematic | Before layout | inspect | p.292–299 | high |
| MITZ-186 | process | ERC pin-type matrix: output-to-output connection = error; passive-to-output = no error; tune the matrix per project but never silence output–output or power-to-output conflicts; custom scripted DRC checks are possible | ERC matrix | pin types | Schematic ERC | inspect | p.299–300 | high |
| MITZ-187 | process | Every pad in the footprint must have a corresponding pin in the schematic symbol (netlist fails otherwise, e.g., 7-pin symbol on 8-pin SOIC); add NC pins with UNIQUE names (NC1, NC2, …) or an NC property listing pin numbers, and place no-connect markers on all unused pins | count(footprint pads) = count(symbol pins) | symbol/footprint | Library validation; KiCad ERC "unconnected pin" | inspect | p.317–319, p.370 | high |
| MITZ-188 | process | Digital library gates have invisible power pins named VCC/GND that connect only by net NAME: the digital ground net must be named GND (or the pin renamed); a wire joining two differently named global symbols makes ONE net (name chosen alphabetically) — check the chosen name; multi-unit parts must have all units' power pins connected the same way (all global or all wired) | — | power nets | Schematic power connectivity | inspect | p.287–288, p.366–369 | high |
| MITZ-189 | process | Bus notation: busname[n..m] (also [n:m], [n-m]) with member aliases busname n … busname m; overbar pin names use C\S\ on symbol pins only — never on power symbols (invalid netlist names) | — | schematic | Schematic entry | inspect | p.369–370, p.398 | high |
| MITZ-190 | process | Placement grid 50 mil or 25 mil (IPC suggests 25 mil); plane-pour etch grid 100 mil; split-plane void vertices on a 5 mil grid; autorouting grid 25 mil | grids per task | — | Layout setup | inspect | p.311, p.336, p.373, p.442 | high |
| MITZ-191 | mechanical | Place mounting holes immediately after the board outline, before moving parts in; plated mounting holes need pads sized for the annular ring requirement; nonplated holes are drilled last with no subsequent plating | — | outline, holes | Layout setup | inspect | p.307–310 | high |
| MITZ-192 | stackup | Layer count from needs: e.g., dual-rail op amp → V+ plane, V− plane, ≥ 1 GND plane, 2 routing layers = 5 → round up to 6 and use the extra layer as a second GND plane (GND_T / VPOS / VNEG / GND_B) | n = ceil_even(planes + routing) | supply rails, routing needs | Stack-up planning | calc | p.333 | high |
| MITZ-193 | solder | Connector-pin thermal flash example: ID 90 mil (2.3 mm), OD 106 mil (2.7 mm), spoke width 20 mil (0.5 mm) (flash F2_3X2_7) with antipad 155 mil; smaller F1_8X2_2 for capacitor pins; every plane-connected pin must show a thermal relief, every non-connected pin a clearance — verify per layer | thermal present ∀ connected pins; antipad ∀ others | padstacks | Plane connectivity audit | inspect | p.340–345 | high |
| MITZ-194 | via | Fan-out and routing vias are normally full-contact (no thermal relief) to planes because nothing is soldered into them; thermals on vias are optional/debated | full contact on vias | via padstacks | Vias to planes | review | p.350 | high |
| MITZ-195 | current-carrying | Trace width is the max of three constraints: fabricator minimum, current capacity (Eq. 6.17), impedance; example: 741 op amp short-circuit output 64 mA → design margin 100 mA → 1 oz: 1.3 mil inner / 0.5 mil outer minimum by heating, so default 5–6 mil is electrically adequate but 5 mil is narrow for many fabricators — pick the fab's comfortable minimum | w = max(w_fab, w_current, w_Z0) | I_max, fab capability | All nets | calc | p.346 | high |
| MITZ-196 | compliance | Spacing from worst-case voltage between any two traces: ±15 V rails → 30 Vpk-pk → conservatively use the 31–50 V row of Table 6.8 → > 4 mil internal, > 5 mil external with soldermask; the chosen spacing must also be within fabricator capability | s ≥ Table 6.8(V_max) | rail voltages | All nets | calc | p.348 | high |
| MITZ-197 | process | Group nets into net classes (power, digital signal, analog signal, bus) and apply constraint sets (width, spacing, allowed layers, allowed vias) per class rather than per net; each net must have at least one allowed via; restrict nets to layers with per-class layer rules so a misrouted net raises DRC | classes ⊇ {power, analog, digital} | netlist | Constraint setup (KiCad net classes + custom rules) | inspect | p.348, p.412–416, Table 9.7 | high |
| MITZ-198 | process | Post-routing inspection checklist: acute angles, long parallel traces (crosstalk), bad via locations, traces over plane voids/splits, silkscreen legibility, new DRC errors, 100 % nets routed, unplaced components; then gloss/clean-up (protect fixed and NO_GLOSS nets), final DRC, back-annotate to schematic | routed = 100 %; DRC = 0 | board | Before artwork | inspect | p.281, p.356–359 | high |
| MITZ-199 | requirements | Mixed-signal board constraint table (Table 9.5 example): mixed SMD/THD, parts on 1 side, 2 plane layers, 2 routing layers, ≥ 4 layers, smallest lead SOIC, min pad spacing 50 mil, max pad width 25 mil, max current 0.1 A, min inner trace 1.3 mil, min outer 0.5 mil, max voltage 10 V, inner spacing 4 mil, outer spacing 5 mil — write such a constraint table before layout | see Table 9.5 | requirements | Any board | review | p.371, Table 9.5 | high |
| MITZ-200 | grounding | Split ground plane: one GND net, analog and digital areas separated by a void strip about 50 mil wide, left joined by a copper neck at the connector ground pin; if the ADC vendor requires common ground under the IC, add a small dynamic-copper bridge under the ADC merged with the plane — return currents follow least impedance so the bridge does not defeat the split | void ≈ 50 mil; one neck at connector (+ optional ADC bridge) | placement partitions | Mixed-signal | inspect | p.373–376 | high |
| MITZ-201 | pdn | Multiple power areas on one plane layer: draw distinct copper areas per net (VCC over the digital ground area, V+/V− over the analog area, each including its connector pin and fan-outs); the gap between digital and analog power areas must line up with the ground-plane void except near the connector; keep every power pour entirely on its own side of the ground split | overlap(power area, other-side ground) = 0 | plane shapes | Mixed-signal | inspect | p.376–377, Fig. 9.100 | high |
| MITZ-202 | return-path | No trace may cross a void/split in its reference plane (loop inductance ↑ → ringing, EMI); fix by moving the trace and add a route keep-out over the void extended 10–20 mil beyond it on all routing layers; run a "segments over voids" check after autorouting | count(trace segments over plane voids) = 0; keep-out = void + 10–20 mil | traces, plane voids | Every board with split/moated planes | inspect | p.380–381, p.442–443, p.451 | high |
| MITZ-203 | crosstalk | Long side-by-side runs (e.g., MCU–ADC control lines) are crosstalk risks: move traces apart (3W), add stitched guard traces, or move some to another layer; use a coupling-analysis report to find excessive coupling | flag parallel runs > threshold at < 3W | routing | Post-route review | inspect | p.381 | high |
| MITZ-204 | crosstalk | Guard traces between aggressor/victim and guard rings around sensitive pins must be tied to the ground plane with vias at intervals along their length (not floating); their benefit is debated and they can worsen things if misapplied | guard has ≥ 2 stitching vias; no floating guard | guard geometry | Sensitive analog | inspect | p.382–384 | high |
| MITZ-205 | emc | Ground pours on routing layers: use dynamic (self-clearing) copper; thermal reliefs orthogonal by default (diagonal optional); voids/merges must mirror the inner ground plane; islands and isolated strips between pins act as antennas — stitch them with vias, trim, or delete unconnected copper; multiple ground planes need many stitching vias across the board and under the ADC | islands = 0; stitching via coverage | pours | Every pour | inspect | p.384–390 | high |
| MITZ-206 | grounding | Separate ground nets (AGND, GND, SHLD) that must join at one controlled point: keep them separate nets in the schematic (a two-pin pseudo-part with no internal connection documents the tie) and join in layout via (a) a shorting-strip footprint (wire, ferrite bead, inductor or copper strip), (b) a net-short copper shape, or (c) a shorting via whose plane clearances are below the drill diameter so plating shorts the planes — the latter MUST be documented on the schematic and marked on silkscreen (drill it out to separate) | exactly 1 tie point per pair | ground nets | Multi-ground boards | review | p.392–394, p.419–424 | high |
| MITZ-207 | grounding | Overlapping analog and digital ground planes on adjacent layers couple noise; insert a buried shield plane (SHLD) connected to chassis ground (single-pin connector J2) between them — 10-layer stack-up in the example with routing restricted per side and blind vias per side (Table 9.7) | shield plane between overlapping A/D planes | stack-up | Isolated-plane designs | review | p.391–395, Fig. 9.117, 9.120 | high |
| MITZ-208 | via | Blind/buried via generation creates every layer-pair via; delete or never allow a via that joins two different plane nets (e.g., VCC–GND) — it would short the supply and scrap the board; blind vias (name contains an outer layer) vs buried (inner only) | no via padstack spans two plane nets | via list | HDI | inspect | p.412 | high |
| MITZ-209 | process | Simulation-in-schematic hygiene: PSpice-only parts flagged (PSpiceOnly = TRUE, blank footprint); a "0" ground joins AGND/GND only during simulation and must be deleted before netlisting; parts without models are ignored (marked); transient run-to-time ≈ 3 cycles (5 ms for 1 kHz), max step ≈ 1/1000 of run time; VSIN for time domain, VAC + AC sweep for frequency response; floating model pins use FLOAT = RtoGND | — | sim setup | Co-simulated schematics | inspect | p.400–404 | high |
| MITZ-210 | via | Example via set for a 4-layer high-speed board (Table 9.9, mil): default VIA drill 13 / pad 24 / clearance 30, full plane connection, mask opening; VIATENT same but tented (no mask opening) used for fan-outs; VIAHEAT drill 10 / pad 20 / clearance 26, full connection, for heat-pipe arrays | see Table 9.9 | via padstacks | High-speed 4-layer | calc | p.427, Table 9.9 | high |
| MITZ-211 | thermal | Exposed-pad heat spreader: copper plate on top layer under the package thermal pad, array of small full-contact vias (heat pipes, e.g., drill 10 / pad 20 mil placed close together) to a plane, soldermask opening 5 mil larger than the plate on all sides, paste layer if SMT-soldered; build it BEFORE fan-out/routing and fix the vias and plate so routing passes cannot disturb them; a plane can be bolted to a heat sink for more dissipation | mask = plate + 5 mil/side; vias full contact | package thermal pad | Exposed-pad ICs (ADN2530 example) | inspect | p.427–434 | high |
| MITZ-212 | transmission-line | High-speed example: signals with 200 ps–1.9 ns edges require controlled impedance; PT should be < ½·RT, better < ¼·RT; Eq. 9.1 L < RT/(k·tPD) with k ≥ 2; tPD = 85·sqrt(0.475·εr + 0.67) = 137 ps/in for εr = 4.2; Table 9.10 max lengths: 66 MHz oscillator (RT assumed = ¼ period = 3.8 ns): 13.9 / 9.26 / 6.95 in for k = 2/3/4; ALS logic (RT 1.9 ns): 6.95 / 4.63 / 3.47 in; ADN2530 (RT 26 ps): 0.095 / 0.063 / 0.048 in | L_max = RT/(k·tPD) | RT, εr | Digital placement | calc | p.436–437, Table 9.10 | high |
| MITZ-213 | transmission-line | Surface microstrip width for Z0 = 50 Ω, εr = 4.2, h = 10 mil, t = 1.35 mil (1 oz), k = 87: w = 7.47·h·exp(−Z0·sqrt(εr + 1.41)/k) − 1.25·t = 17.5 mil (17 mil → 50.9 Ω); use a short narrow (6 mil) neck at the pad (thermal relief for reflow, too short to affect impedance) then the 17.5 mil line; set per-net min 6 / max 17.5 mil and a max-neck-length rule (e.g., 40 mil) | w(50 Ω) = 17.5 mil | Z0, εr, h, t | Controlled impedance routing | calc | p.437–440 | high |
| MITZ-214 | timing | Differential/complementary pairs (MODP/MODN) should be length-matched per datasheet: measure both; a 58 mil mismatch was removed by rotating the driver 45° and relocating it (match within 0.01 mil), otherwise add trombone/accordion/sawtooth length | ΔL ≤ datasheet tolerance | pair lengths | Differential lines | calc | p.438 | high |
| MITZ-215 | emc | Moated ground for clock/oscillator circuits: after routing the clock traces, void a moat in the ground plane around the oscillator leaving a bridge wide enough to include the IC ground pin and the area under the clock traces (corrals ground currents back to the IC ground pin); replicate moats on top/bottom pours, stitch all ground planes, and put a route keep-out on all layers over the moat | bridge width ≥ span(GND pin … clock traces) | clock circuit | High-speed clocks | inspect | p.440–443, p.451 | high |
| MITZ-216 | process | Pin/gate swapping (same pin-group, same gate, same pin type; SWAP_INFO for heterogeneous parts) shortens rat's nest; always back-annotate to the schematic; note that a swapped microcontroller pin changes the firmware pin map, and re-placing the modified part from the library undoes the swap | — | swappable pins | Digital layout; hw-fw | review | p.443–451 | high |
| MITZ-217 | pdn | Plane layers must be typed PLANE (not routing/conductor) so autorouters never route traces on them — traces on a ground plane create slots that break return paths | no signal traces on plane layers | layer types | All plane layers | inspect | p.453 | high |
| MITZ-218 | solder | Positive-plane thermal reliefs are generated from constraints: relief clearance = shape-to-pin spacing (default gave 55 mil pad in a 65 mil clearance = 5 mil gap), spoke width = trace-width constraint (e.g., set both to 10 mil); check orientation (orthogonal/diagonal/full contact), number of spokes, fixed vs scaled spoke width; changing width/spacing rules changes thermal geometry — re-verify | gap = shape-to-pin spacing; spoke = line width | constraints | Positive planes / pours (KiCad zone settings) | inspect | p.453–454, p.386–389 | high |
| MITZ-219 | via | IPC-2221B: unconnected (nonfunctional) pads on routing layers should be retained; unconnected pads on plane layers may be removed — suppress unconnected pads only on plane layers (requires padstack option + artwork option + positive plot) | suppress on plane layers only | padstacks, artwork | Artwork generation | inspect | p.456–457 | high |
| MITZ-220 | fab | Positive vs negative plane artwork: for the example the positive GND Gerber was 54 lines / 1.15 kB vs 128 lines / 2.34 kB negative; positive planes are simpler unless thermal reliefs must be precisely engineered (negative flashes are fixed, positive reliefs follow constraints) | — | plane polarity | Artwork | review | p.458–459 | high |
| MITZ-221 | process | Reuse: keep board templates (design parameters, grids, stack-up, outline, artwork setup, colors, constraints) and exportable technology/constraint files; wizard inputs include route keep-in and package keep-in distance from board edge, minimum line width and spacing, default via | — | templates | New projects | review | p.459–466 | high |
| MITZ-222 | mechanical | Mounting-hole footprints (plated and nonplated) must carry place keep-out (courtyard) boundaries on BOTH top and bottom so no component sits near the hole or touches the mounting hardware (standoffs, washers, nuts) | courtyard on both sides ≥ hardware outline | mounting-hole footprints | All boards | inspect | p.473 | high |
| MITZ-223 | mechanical | Nonplated (mechanical) mounting holes must also carry an all-layer route keep-out so traces are not routed under mounting hardware or across the hole (they would be drilled away); DRC cannot catch this otherwise because there are no pads to space against | route keep-out (all layers) ≥ hardware diameter | NPTH footprints | All boards | inspect | p.473 | high |
| MITZ-224 | assembly | Fiducials (stencil alignment and pick-and-place vision) need three elements: copper mark on the outer etch layer, a soldermask opening (mask removed at the fiducial), and an identical pastemask copy (visible through the stencil); example 40 × 40 mil copper, 50 × 50 mil mask opening (5 mil larger per side), 40 × 40 mil paste; place two or more fiducials on the outer perimeter of the board | copper + mask (+5 mil/side) + paste; n ≥ 2 on perimeter | fiducial list | SMT assembly | inspect | p.474–475, Table 10.2 | high |
| MITZ-225 | assembly | The stencil is a thin stainless-steel sheet whose thickness sets the paste volume; the stencil maker works from the pastemask Gerber — every SMD footprint (and fiducial) must have paste openings; many stock library footprints lack them | paste openings present ∀ SMD pads | paste Gerber | SMT | inspect | p.474, p.434 | high |
| MITZ-226 | fab | Manufacturing data = artwork (Gerber RS-274X) for every copper layer, soldermask per side, paste per side (if stencil), silkscreen per side that carries legend, and a board outline film, plus NC drill (plated and nonplated) and NC route (if milling/slots). Example 4-layer board with top-only legend produced 8 Gerbers: 4 copper + 2 mask + 1 silk + 1 outline | N_gerber = N_cu + N_mask + N_silk + N_paste + 1 (outline) | layer list | Fab release | inspect | p.475–487 | high |
| MITZ-227 | fab | Provide a dedicated outline film (photoplot/board-edge outline); the design outline used during layout may carry no manufacturing data | outline Gerber present | outline | Fab release | inspect | p.477, p.485 | high |
| MITZ-228 | fab | Board-level markings: add board part number, revision/manufacturing date and logo as silkscreen (or etch) text owned by the board, not by a component | P/N + rev present on legend | legend layer | Fab release | inspect | p.477, Fig. 10.7 | medium |
| MITZ-229 | fab | Film composition: conductor films = etch + pins + vias for each copper layer (Table 10.3); silkscreen film = board-geometry text/lines + reference designators + package outlines (+ optional value, device type, tolerance, user part number); soldermask film = pin + via mask openings + package- and board-geometry mask shapes (Table 10.4) — omit a silkscreen film for a side with no legend | — | artwork setup | Gerber generation | inspect | p.479–482, Tables 10.3–10.4 | high |
| MITZ-230 | fab | Silkscreen clean-up before artwork: legend must not lie under component bodies, over pads or soldermask openings (clip it at mask openings), must not overprint other legend; reference designators close to their parts, outside place boundaries and clear of fan-out vias; drop outline segments that collide with vias near the body | silk ∩ mask openings = ∅; silk ∩ silk = ∅; refdes near owner | silk layer | Fab release (KiCad silk-to-mask / silk-overlap DRC) | inspect | p.483–485 | high |
| MITZ-231 | fab | Zero-width lines and text (e.g., library outlines drawn as rectangles, which always have width 0) are dropped from Gerbers unless a default/undefined line width of 5–10 mil is set — otherwise large blank areas appear on the silkscreen | default width 5–10 mil; count(zero-width legend objects) = 0 | legend objects | Gerber generation | inspect | p.485–486 | high |
| MITZ-232 | fab | Negative plane films must be plotted Negative; removing unused pads from negative planes (vector-based pad behavior) gives a larger, safer clearance gap; RS-274X (extended Gerber) carries its apertures, only legacy RS-274D needs a separate aperture list | plot polarity = plane polarity | artwork setup | Negative planes | inspect | p.485–486 | high |
| MITZ-233 | fab | After artwork generation read the photoplot report for errors and confirm every expected file exists; verify the Gerbers by re-importing them (origin at 0,0) into a blank board/Gerber viewer or a CAM tool (GerbTool, CAM350); negative planes appear as true negative images; drill and mill data can only be reviewed in a CAM tool | photoplot errors = 0; file list complete | Gerber set | Before release | inspect | p.487, p.494–496 | high |
| MITZ-234 | fab | Take a drill inventory before NC output: a drill legend/chart listing each drill figure, finished hole size, plated/nonplated and quantity, placed on the fab drawing next to or above the board outline (drill symbols then appear on every hole) | drill chart covers all hole sizes | drill table | Fab drawing | inspect | p.487–488, Fig. 10.17 | high |
| MITZ-235 | fab | NC drill settings per fabricator: coordinate format (e.g., 2.4), zero suppression, Excellon options, optional header, scale 1, tool sequence; enable automatic tool selection so the Excellon file carries its tool table (otherwise only coordinates and manual stops); separate plated/nonplated files unless the fab accepts a combined file; repeat codes and optimized head travel on if unspecified; layer-pair drilling normally, by-layer drill files for backdrill and blind/buried vias | tool table present in each drill file | drill export | Fab release | inspect | p.488–490 | high |
| MITZ-236 | fab | Drill-file naming: <board>-<startlayer>-<endlayer>.drl (plated), <board>-<start>-<end>-np.drl (nonplated), <board>-bl-<a>-<b>.drl per layer pair when drilling by layer; a manual tool list line = hole diameter, P/N (plated/nonplated), tool number Tnn, +/− tolerance | naming convention followed | drill files | Fab release | inspect | p.490, Fig. 10.20 | high |
| MITZ-237 | fab | NC route (mill) file is needed when the board is cut from a panel with specific requirements, for slots or irregular holes, or when you buy panels and depanel yourself; route tool list = bit diameter + tool number (example bit 0.100 in); cut marks: line width = bit diameter (100 mil), offset = ½ bit (50 mil) outside the board edge so the bit does not cut into the board, mark length ≈ 2 × width, inside and outside corners for non-rectangular boards; draw the cut path with line width = cut width (selects the tool) and mark start point (1) and cut direction (2) | path offset = d_bit/2 outside edge | route outline | Panelized / milled boards | calc | p.491–494 | high |
| MITZ-238 | mechanical | Export ECAD to MCAD (DXF, IDF, IDX or STEP) and check form, fit and function against the enclosure and mounting hardware; every footprint needs a maximum package height property (used by MCAD for body height) and a STEP model whose orientation and origin match the footprint | ∀ footprint: height_max defined; STEP aligned | 3D export | Mechanical integration | inspect | p.497–500 | high |
| MITZ-239 | fab | Board houses differ in capability (layer count, copper thickness, drill sizes), file-submission policy, minimum order and billing; obtain the actual fabricator's capability sheet and CAM review/quote before release | design rules ⊆ fab capability | fab capability sheet | Procurement | review | p.500 | high |
| MITZ-240 | test | Inspect bare boards (especially the first run) and do initial electrical tests — continuity and isolation, particularly power and ground — before loading any component; IPC-2515A (bare-board electrical test data description) and IPC-6011 (generic performance specification) define inspection and acceptance tests | supply-to-ground isolation verified before assembly | bare boards | First article / bring-up | measure | p.501 | high |
| MITZ-241 | assembly | Pick-and-place file per placed part: REFDES, PART_NUMBER (distinguishes same-value parts, e.g., 1206 1 kΩ 0.1 % vs 1 %), X and Y of the symbol center, rotation, and side (mirror) for double-sided SMT; every part must carry its part number before the file is generated | fields = {refdes, P/N, X, Y, rotation, side}; P/N non-empty | placement report | Assembly release | inspect | p.501–505, Fig. 10.38 | high |
| MITZ-242 | components | Part database minimum fields: unique internal Part Number (never change it — the link breaks), Part Type (category), Schematic Part (symbol), PCB Footprint (required for netlisting), Value (unit-aware: Ω, pF, uH); simulation adds Implementation (= model name), Implementation Type and simulation template (pin map), best kept on the symbol | required fields non-empty ∀ parts | parts DB | Library / BOM | inspect | p.509–510 | high |
| MITZ-243 | components | Optional part fields typically: description, tolerance, rating, speed, timing, manufacturer, cost — as many as needed but as simple as possible; never reuse a property name (Manufacturer1, Manufacturer2); avoid reserved names (Power = power dissipation, Voltage = net voltage, Color); convert ERP/PLM field types to text via DB views and rename to tool names (e.g., currency "gl-abc" → varchar Price); SQLite: ANSI SQL-92 types only | — | parts DB | Library / BOM | inspect | p.510–514 | high |
| MITZ-244 | process | Part-DB administration: keep the DB configuration file in a read-only shared directory; the ODBC data source must be configured identically on every client; the DB may be an ERP/PLM extract with periodic (e.g., overnight) update or live DB views | — | DB setup | Team libraries | review | p.509, p.514–516 | high |
| MITZ-245 | components | Include mechanical (virtual) parts — screws, nuts, standoffs — in the BOM (mapping table of mechanical parts to electrical parts) so the BOM export is complete | BOM ⊇ mechanical hardware | BOM | Assembly BOM | inspect | p.517 | high |
| MITZ-246 | components | Keep approved alternates per internal part number in a relational vendor table (example: 8 replacements for one 100 nF capacitor P/N) and link datasheets as browsable fields; allow duplicate part numbers only for associated mechanical parts; temporary parts get tracked TMP-prefixed numbers | ≥ 1 approved source per P/N; TMP parts = 0 at release | parts DB | Release | inspect | p.518–521 | high |
| MITZ-247 | components | Part-status audit before release: every placed part must match its DB record (green); red = missing part number or not found in DB, yellow = not yet checked — update/verify all parts against the DB and the symbol libraries | count(red ∪ yellow parts) = 0 at release | part manager | Release | inspect | p.535–536 | high |
| MITZ-248 | components | BOM generation: group (key) by part number or part reference; compressed reference ranges (C1–C3) or one line per part; exclude non-purchased reference prefixes (e.g., TP test points); list variant not-stuffed parts with quantity 0 and a short not-present text such as "DNI" (Do Not Install) | DNI parts listed with qty 0 | BOM | Variant BOMs | inspect | p.520, p.536–538 | high |
| MITZ-249 | process | Assembly variants: groups (functions, e.g., power, channel), subgroups (assembly options, e.g., 220 V / 110 V / DNI; 1 or 2 channels), core design, common parts, and BOM variants each built from common + one subgroup per group; view and report each variant | each BOM variant = common + exactly one subgroup per group | variant tree | Multi-variant products | review | p.538–541 | high |
| MITZ-250 | process | SPICE passive models: ideal R/L/C use Value, Tolerance (DEV %), TC1 (linear) and TC2 (quadratic) temperature coefficients, plus IC (initial condition), IL1/IL2 (inductor current coefficients), VC1/VC2 (capacitor voltage coefficients), e.g., `.model Rx RES R=1 DEV=tol% TC1=… TC2=…`; populate tolerance and TCs so Monte-Carlo/worst-case runs are meaningful | tolerance non-blank for simulated passives | passive models | Worst-case simulation (ngspice tc1/tc2) | sim | p.523–524 | high |
| MITZ-251 | process | Precise circuits: model real capacitors and inductors as subcircuits with parasitics — capacitor = base C + ESR + ESL + leakage resistance (parameters ESL, ESR, CAP, LEAK) — and store per-P/N parasitic values in the part DB | C model includes ESR, ESL, R_leak | part parasitics | Precision analog, PDN, filters | sim | p.524–528, Fig. 11.13 | high |
| MITZ-252 | process | Symbols with more pins than the model (e.g., 8-pin ua741, 5 modelled nodes in+, in−, V+, V−, OUT) mark the extra pins FLOAT = Unmodeled; heterogeneous multi-unit parts are not simulatable in PSpice; simulate a sub-block (e.g., switching regulator) of the production schematic through a test-bench copy rather than a separate project so the simulated and built circuits stay identical | — | sim setup | Co-simulation | sim | p.528–531 | high |
| MITZ-253 | transmission-line | High-speed criterion is edge rate, not clock frequency: rise time measured 10 %–90 % of amplitude; rule of thumb: rise time faster than 1 ns on a postcard-size (3 in × 4 in) PCB = high-speed design (interconnect must be treated as a transmission line/channel) | t_r(10–90 %) < 1 ns on ~3 × 4 in board → high speed | t_r, board size | SI triage | calc | p.544, Fig. 12.3 | high |
| MITZ-254 | transmission-line | Interconnect model: distributed RLGC (series R and L, shunt G and C) per segment, accuracy rising with segment count; model the whole channel — driver/receiver die and package with IBIS (behavioral IBIS for pre-emphasis), connectors and cables with measured S-parameter models, PCB traces and vias from the stack-up | — | IBIS, S-parameters, stack-up | SI simulation | sim | p.543–545, Figs. 12.2, 12.4 | high |
| MITZ-255 | transmission-line | Pre-layout SI simulation: set εr (FR4 ≈ 4.0–4.5) and the stack-up, drive a low→high→low pulse, observe driver and receiver waveforms while varying trace length/delay and impedance (or width/dielectric thickness) and inserting vias; judge edge quality, overshoot, setup/hold time and eye opening; without an IBIS model use a default buffer model tuned to datasheet parameters | — | topology | Pre-layout | sim | p.545–548 | high |
| MITZ-256 | timing | Derive routing constraints from SI simulation: maximum interconnect length from the setup-time margin, minimum length from the hold-time margin, maximum via count per signal, equal via count across all bits of a bus; load them into the constraint system so layout DRC enforces them | L_min ≤ L ≤ L_max; vias ≤ N_max; Δvias(bus) = 0 | simulation results | Buses, clocks | sim | p.546–547 | high |
| MITZ-257 | transmission-line | Post-layout verification: extract each routed critical net (exact trace geometry, vias, terminations) and re-simulate it to confirm it is still within SI specification | 100 % of critical nets re-simulated | routed topology | Post-layout | sim | p.547, Fig. 12.7 | high |
| MITZ-258 | termination | Tolerance sweep of terminations: sweep the termination resistor (e.g., 10–50 Ω in 2 Ω steps), find the passing window, then select a real part whose nominal ± tolerance fits inside it (e.g., 22 Ω ±10 %) | R_nom·(1 ± tol) ⊆ passing window | sweep results | Terminated nets | sim | p.547 | high |
| MITZ-259 | transmission-line | Multi-load net topology scheduling: minimum spanning tree, daisy chain, source-load daisy chain, star, far-end cluster; T-points control branch lengths; capture a proven topology (e.g., fly-by for a DDR address bus) as a constraint set and apply it to every net of the bus | same topology ∀ nets of a bus | net schedule | Multi-drop buses | review | p.550–551 | high |
| MITZ-260 | transmission-line | Model-free layout SI screen (electrical rule check): extract per-segment impedance and coupling from traces, vias, planes and stack-up and flag impedance discontinuities, coupling to neighbouring traces, unequal via counts within a bus, differential pairs out of phase, routing across split planes, and routing too close to other signals' traces or vias | violations = 0 or dispositioned | layout | Post-layout | inspect | p.551–553, Figs. 12.12–12.14 | high |
| MITZ-261 | pdn | SI is degraded by reflections, crosstalk, ground bounce and power-supply noise; higher-tier analyses add ground bounce, EMI, IR-drop and thermal self-heating — plan PI/IR-drop analysis for dense or high-current boards | — | — | Advanced SI/PI | review | p.547 | medium |
| MITZ-262 | components | Identify every footprint by its package standard and variation: the JEDEC outline drawing plus variation code fixes pitch and lead count (e.g., SOIC narrow MS-012: 0.150 in body, 0.236 in (6.0 mm) across leads, 1.27 mm pitch, 0.40 mm leads; SOIC wide MS-013: 0.300 in body, 0.403 in (10.3 mm) across leads; SSOP MO-137 / MO-118: 0.635 mm pitch; MSOP MO-187: 0.65 / 0.50 mm; SOT-23 TO-236: 0.95 mm; SOT-223 TO-261: 2.30 mm; DPAK TO-252: 0.090 in; D3PAK TO-268: 5.45 mm); record it in the footprint/part data | JEDEC doc + variation recorded ∀ footprints | package data | Library | inspect | p.559–572, Tables B.1–B.10 | high |
| MITZ-263 | components | Molded tantalum case letters map to EIA metric size codes LLWW-HH (EIAJ RC-2134B): A 3216-18, B 3528-21, C 6032-28, D 7343-31, E 7260-38, R 2012-12, T 3528-12, V 7343-20, X "7343", Y "7340" (as printed); the footprint must match the case code, and the height suffix distinguishes low-profile variants (T vs B, V vs D) | footprint ↔ EIA case code | tantalum parts | Library | inspect | p.563, Table B.2 | medium |
| MITZ-264 | timing | Where no datasheet edge rate is available, use tabulated logic-family transition times (Appendix C, from IPC-2251 Table 5-4 and Coombs Table 13.2) and take the smaller of RT and FT, e.g., HC 3.6/4.1 ns, HCT 4.6/3.9, AC 1.7/1.5, LCX 2.9/2.4, ALS 2.3/2.3, LS 15/10, 10KH 1.7/1.7, 100K 0.6/0.6, EP 0.11/0.11, GaAs 0.02/0.02 | t_edge = min(RT, FT) | logic family | Critical length, SI triage | calc | p.573–574, Appendix C | high |
| MITZ-265 | mechanical | Mounting-hole diameter per screw size and fit class (Appendix D): e.g., M3 close 3.2 mm, normal 3.4 mm, loose 3.6 mm; M2.5 2.7 / 2.9 / 3.1; M4 4.3 / 4.5 / 4.8; #4-40 close No.31 (0.120 in), normal No.30 (min 0.130 in), loose No.27 (min 0.156 in); choose the fit from the positional tolerance stack and specify it as the finished hole | hole ∈ {close, normal, loose}(screw) | screw size | Mounting holes | calc | p.575–576, Tables D.1–D.2 | high |
| MITZ-266 | mechanical | Keep copper, courtyards and components clear of mounting hardware: keep-out diameter around a mounting hole ≥ largest of washer, head and nut diameter (Appendix D; e.g., M3 washer 6.0 mm, head/nut 5.4 mm; #4 washer 0.375 in, head 0.219 in, nut 1/4 in) plus the conductor-to-hardware spacing (IPC-2221B Fig. 8-4). Consistent book example: #4 normal-fit plated hole 0.130 in with a 400 mil pad (≥ 0.375 in washer) and a nonplated 130 mil hole with 160 mil plane clearance | keep-out_dia ≥ max(washer, head, nut) + 2·s_hw | screw size | Mounting holes | calc | p.470, p.473, p.575–576, p.588 | medium |

## 2. Formulas & tables (numbers)

### Table 1.1 — PCB project, Gerber and drill files (p.15)

| File | Function |
|---|---|
| ProjectName.brd | Main board project file |
| Assembly_Top.art / Assembly_Bottom.art | Top/bottom side assembly |
| Solderpaste_Top.art / Solderpaste_Bottom.art | Top/bottom solder paste (stencil) |
| Silkscreen_Top.art / Silkscreen_Bottom.art | Top/bottom silk screen |
| Soldermask_Top.art / Soldermask_Bottom.art | Top/bottom soldermask |
| TOP.art / BOTTOM.art | Top/bottom copper (usually routing) |
| INNER1.art, INNER2.art, INNERx.art | Inner routing layers |
| PWR.art / GND.art | Power / ground plane layers |
| ProjectName.rou | Board outline cutting (route) path |
| ProjectName.drl | Drill hole data |

### Table 4.1 — Standard copper-clad panel sizes, inches (ANSI/IPC-D-322; IPC-2221B Fig. 1) (p.75)

| Letter (x) \ Number (y) | 1 (y=3.2) | 2 (y=6.7) | 3 (y=10.2) | 4 (y=13.8) |
|---|---|---|---|---|
| A (x=2.4) | 2.4 × 3.2 | 2.4 × 6.7 | 2.4 × 10.2 | 2.4 × 13.8 |
| B (x=4.7) | 4.7 × 3.2 | 4.7 × 6.7 | 4.7 × 10.2 | 4.7 × 13.8 |
| C (x=7.1) | 7.1 × 3.2 | 7.1 × 6.7 | 7.1 × 10.2 | 7.1 × 13.8 |
| D (x=9.5) | 9.5 × 3.2 | 9.5 × 6.7 | 9.5 × 10.2 | 9.5 × 13.8 |

Tooling area (board outline edge to panel boundary): 0.375–1.5 in, typically 1.0 in. Board-to-board spacing on panelized designs: 0.1–0.5 in (p.75).

### Table 4.2 — Typical finished board thicknesses (p.76)

| in | mil | mm |
|---|---|---|
| 0.020 | 20 | 0.51 |
| 0.030 | 30 | 0.76 |
| 0.040 | 40 | 1.02 |
| 0.062 | 62 | 1.6 |
| 0.093 | 93 | 2.4 |
| 0.125 | 125 | 3.2 |
| 0.250 | 250 | 6.4 |
| 0.500 | 500 | 12.7 |

### Table 4.3 — Typical laminate core thicknesses, without copper (Coombs Table 5-5; IPC-4101E Table 3-7) (p.77)

| Range (mil) | Avg (mil) | Range (mm) | Avg (mm) |
|---|---|---|---|
| 0.98–4.69 | 2.8 | 0.025–0.119 | 0.072 |
| 4.72–6.46 | 5.6 | 0.120–0.164 | 0.142 |
| 6.50–11.8 | 9.1 | 0.165–0.299 | 0.232 |
| 11.8–19.6 | 15.7 | 0.300–0.499 | 0.400 |
| 19.7–30.9 | 25.3 | 0.500–0.785 | 0.643 |
| 30.9–40.9 | 35.9 | 0.786–1.039 | 0.913 |
| 40.9–65.9 | 53.4 | 1.040–1.674 | 1.357 |
| 65.9–101 | 83.4 | 1.675–2.564 | 2.120 |
| 101–141 | 121 | 2.565–3.579 | 3.072 |
| 141–250 | 195 | 3.580–6.350 | 4.965 |

### Table 4.4 — Standard prepreg thicknesses, uncured (Coombs Tables 6-3, 10-2) (p.77)

| Prepreg glass style | Thickness (mil) | Thickness (mm) |
|---|---|---|
| 106 | 1.5–2.3 | 0.038–0.058 |
| 1080 | 2.3–3.0 | 0.058–0.076 |
| 2313 | 3.5–4.0 | 0.089–0.102 |
| 2116 | 4.5–5.3 | 0.114–0.135 |
| 2165 | 5.0–6.8 | 0.127–0.173 |
| 2157 | 5.8–6.5 | 0.147–0.165 |
| 7628 | 7.0–7.8 | 0.178–0.198 |

Note (p.76): cured thickness depends on neighbors — prepreg between signal layers ends thinner than between plane layers (signal copper sinks in). Dielectric constant varies by manufacturer.

### Table 4.5 — Minimum electroless plating thickness, surfaces and holes (IPC-2221B Table 4-2, partial) (p.78)

| | Classes 1 and 2 (mil / mm) | Class 3 (mil / mm) |
|---|---|---|
| Average | 0.79 / 0.020 | 0.98 / 0.025 |
| Thin (minimum) | 0.71 / 0.018 | 0.79 / 0.020 |

Also: electroless plating typically 20–100 uin in holes and surfaces (Coombs p.28.8; MIL-STD-275 Table 4-3); finished PTH wall usually ≤ 1 mil (25 um); most finished hole sizes ≥ 8 mil (p.76–77).

### Table 4.6 — Nominal and finished copper thickness by weight (±10%) (Coombs Tables 5-4, 5-11; IPC-4101E Table 1-2; IPC-D-330 §2 Table 2-16) (p.78)

| Area wt (oz/ft²) | Nominal (mil) | Nominal (mm) | Internal min finished (mil) | Internal min finished (mm) | External min finished (mil) | External min finished (mm) |
|---|---|---|---|---|---|---|
| 0.148 (1/8) | 0.20 | 0.005 | 0.12 | 0.0031 | 0.91 | 0.0231 |
| 0.25 (1/4) | 0.34 | 0.009 | 0.24 | 0.0062 | 1.03 | 0.0262 |
| 0.35 (3/8) | 0.47 | 0.012 | 0.37 | 0.0093 | 1.15 | 0.0293 |
| 0.50 (1/2) | 0.68 | 0.017 | 0.45 | 0.0114 | 1.32 | 0.0334 |
| 0.75 (3/4) | 1.01 | 0.026 | 0.76 | 0.0193 | 1.62 | 0.0410 |
| 1 | 1.35 | 0.034 | 0.98 | 0.0249 | 1.89 | 0.0479 |
| 2 | 2.70 | 0.069 | 2.19 | 0.0557 | 3.10 | 0.0787 |
| 3 | 4.05 | 0.103 | 3.41 | 0.0866 | 4.32 | 0.110 |
| 4 | 5.40 | 0.137 | 4.63 | 0.118 | 5.49 | 0.139 |
| 5 | 6.75 | 0.171 | 5.92 | 0.150 | 6.32 | 0.160 |
| 6 | 8.10 | 0.206 | 7.13 | 0.181 | 7.28 | 0.185 |
| 7 | 9.45 | 0.240 | 8.35 | 0.212 | 8.22 | 0.209 |
| 10 | 13.5 | 0.343 | 12.0 | 0.305 | 10.9 | 0.277 |
| 14 | 18.9 | 0.480 | 16.9 | 0.428 | 14.3 | 0.364 |

### Etch/width/hole/mask allowances (Ch.4, p.79–81)

| Parameter | Value | Source |
|---|---|---|
| Trace width tolerance, 1.5 oz Cu | ±4.0 to ±0.6 mil (by producibility level and plating) | MIL-STD-275 |
| IPC-2221B minimum trace width and spacing | 3.9 mil | IPC-2221B |
| Typical fabricator minimum trace width | 4–8 mil | p.79 |
| Plating added per surface | up to 1 mil → finished hole up to 2 mil under drill | p.80 |
| Aspect ratio (thickness:hole) Level A | 3:1 to 5:1 (target 3:1) | IPC-2221B Table 5-1 p.40 |
| Aspect ratio Level B | 6:1 to 8:1 | p.80 |
| Aspect ratio Level C | 9:1 or higher | p.80 |
| Soldermask oversize, liquid screen-printed | 16–20 mil | IPC-2221B |
| Soldermask oversize, photoimageable | 0–5 mil | IPC-2221B |
| Library footprint mask clearance (typical) | 0–10 mil | p.81 |

### Table 5.1 — Minimum recommended spacing, discrete axial through-hole devices (IPC-2221B Fig. 7-1 p.68) (p.91)

| Parameter | mil | mm |
|---|---|---|
| Side to PCB edge (a) | 75 | 1.9 |
| End to PCB edge (b) | 90 | 2.29 |
| End to end | 100 | 2.54 |
| Side to side, body diameters < 100 mil (2.54 mm) | 100 | 2.54 |
| Side to side, D2 > D1 > 100 mil: a | 70 + D1/2 (≥ 100) | 1.78 + D1/2 (≥ 2.54) |
| Side to side, D2 > D1 > 100 mil: b | 10 + D1/2 + D2/2 (≥ 100) | 0.25 + D1/2 + D2/2 (≥ 2.54) |
| Side to end, one or more body diameters > 100 mil | 95 + D1/2 | 2.41 + D1/2 |

### Table 5.2 — Minimum recommended spacing, discrete radial through-hole devices (p.92)

| Parameter | Value |
|---|---|
| To PCB edge, r | max(D/2, H/2), and r ≥ 60 mil (1.52 mm) |
| To other parts, r | max(D/2, H/2) |

### Table 5.3 — Minimum recommended spacing, through-hole ICs (p.92–93)

| Parameter | mil | mm |
|---|---|---|
| Side to PCB edge (a) | 100 | 2.54 |
| End to edge (b) | 75 | 1.91 |
| End to end | 200 | 5.08 |
| Side to side | 100 | 2.54 |

### Table 5.4 — Minimum spacing between through-hole discretes and ICs (p.93)

| Parameter | mil | mm |
|---|---|---|
| a (discrete side to IC, D1 > 100 mil) | 115 + D1/2 | 2.91 + D1/2 |
| b (discrete end to IC, D < 100 mil) | 200 | 5.08 |
| c (discrete side to IC, D < 100 mil) | 100 | 2.54 |
| d (discrete end to IC, D1 > 100 mil) | 40 + D1/2 | 1.02 + D1/2 |

### Table 5.5 — Holes and jumper wires (p.93)

| Parameter | Value |
|---|---|
| Hole to hole (plated or nonplated) | (1) do not violate pad spacing rules; (2) residual laminate > 20 mil (0.5 mm) between holes |
| Jumper wires (any direction) | 100 mil (2.54 mm) |

### Table 5.6 — Minimum spacing, discrete SMDs (IPC-2221B p.73; IPC-7351B Tables 3.5–3.8, Fig. 3.15) (p.94)

| Parameter | mil | mm |
|---|---|---|
| Side or end to PCB edge | 60 | 1.5 |
| End-to-end / side-to-side, 0603 or larger | 20 | 0.50 |
| End-to-end / side-to-side, smaller than 0603 | 12 | 0.30 |
| Pad to via | 20 | 0.50 |

### Table 5.7 — Minimum spacing, IC SMDs (IPC-2221B p.73; IPC-7351B Tables 3.2–3.22) (p.94–95)

| Parameter | mil | mm |
|---|---|---|
| Component side/end to PCB edge | 60 | 1.5 |
| End to end (body) | 20 | 0.50 |
| Side to side (pad to pad) | 20 | 0.50 |

### Tables 5.8–5.10 — Nominal (density level B) solder fillet allowances, IPC-7351B-derived (p.99–100)

| Package type | JT toe (mil / mm) | JH heel (mil / mm) | JS side (mil / mm) |
|---|---|---|---|
| Gull wing (SOG), pitch > 0.625 mm | 14 / 0.35 | 14 / 0.35 | 1 / 0.03 |
| Gull wing (SOG), pitch < 0.625 mm | 14 / 0.35 | 14 / 0.35 | −1 / −0.02 |
| J lead (SOJ) | 14 / 0.35 | −8 / −0.20 | 1 / 0.03 |
| Small outline (SO) | 12 / 0.30 | 0 / 0.00 | −2 / −0.04 |
| Chip components, 0603 and larger | 14 / 0.35 | −2 / −0.05 | 0 / 0.00 |
| Chip components, smaller than 0603 | 4 / 0.10 | −2 / −0.05 | 0 / 0.00 |
| Tantalum capacitors | 6 / 0.15 | 20 / 0.50 | −2 / −0.05 |
| MELF | 16 / 0.40 | 4 / 0.10 | 2 / 0.05 |
| Leadless chip carrier | 22 / 0.55 | 6 / 0.15 | −2 / −0.05 |
| Butt joints | 31 / 0.80 | 31 / 0.80 | 8 / 0.20 |

Note: negative values were rendered with a leading "2" in the extraction (e.g., "28" = −8, "22" = −2); decoded by matching the mm column. IPC-7351B also gives Level A (greater) and Level C (lesser) values not reproduced in the book.

### Eqs. 5.1–5.2 — SMD pad size (derived from IPC-7351B, no rounding factors) (p.100)

- WP(MAX) [pad width, along lead] = E_MIN − (E_MAX − 2·L_MIN) + 2·JT + 2·JH + 2·sqrt((E_TOL)² + F² + P²)  (as printed; see MITZ-071 for the IPC Z/G form)
- HP(MAX) [pad height, across lead] = b_MIN + 2·JS + sqrt((b_TOL)² + F² + P²)
- E = lead span (end-to-end of leads) MIN/MAX; E_TOL = E_MAX − E_MIN; L = soldered lead length; b = lead width; b_TOL = b_MAX − b1_MIN; F = fab tolerance = 0.1 mm (4 mil) typ.; P = placement tolerance = 0.15 mm (6 mil) typ.
- Example package (JEDEC MS-012 SOIC-8, Fig. 5.5–5.6): E = 5.80–6.20 mm, e = 1.27 BSC, b = 0.31–0.51 (b1 0.28–0.48), L = 0.40–1.27 mm, body 4.80–5.00 × 3.80–4.00 mm.

### Table 5.11 — Courtyard excess (protrusion) by density level (IPC-7351B Tables 3-2..3-22) (p.102)

| Package type | Level A (mil / mm) | Level B (mil / mm) | Level C (mil / mm) |
|---|---|---|---|
| Gull wing (SOG) | 20 / 0.50 | 10 / 0.25 | 4 / 0.10 |
| J lead (SOJ) | 20 / 0.50 | 10 / 0.25 | 4 / 0.10 |
| Small outline (SO) | 20 / 0.50 | 10 / 0.25 | 4 / 0.10 |
| Chip components (0603 and larger) | 20 / 0.50 | 10 / 0.25 | 4 / 0.10 |
| Tantalum capacitors | 20 / 0.50 | 10 / 0.25 | 4 / 0.10 |
| MELF | 20 / 0.50 | 10 / 0.25 | 4 / 0.10 |
| Leadless chip carrier | 20 / 0.50 | 10 / 0.25 | 4 / 0.10 |
| Chip components (smaller than 0603) | 8 / 0.20 | 6 / 0.15 | 4 / 0.10 |
| Butt joints | 59 / 1.50 | 31 / 0.80 | 8 / 0.20 |

### Table 5.12 — Axial lead bend radius and extension allowances (p.104)

| Lead diameter DL (mil) | Bend radius R (mil) | Lead extension LA (mil) |
|---|---|---|
| DL < 31 | 1.0 × DL | 31 |
| 31 ≤ DL ≤ 47 | 1.5 × DL | DL |
| DL > 47 | 2.0 × DL | DL |

Eq. 5.3: LP = LB + 2·(R + LA); LE = LA + R. Snap LP to standard grid (usually 100 mil). Total lead length ≤ 1 in (25 mm) unless supported.

### Eq. 5.4 — PTH drill size, method 1 (p.105)

DH = (DL + 2·TP) × k; TP = 1 mil if unknown; 1.05 < k ≤ 3.0, k = 1.5 recommended; finished hole = DH − 2·TP. Example: DL = 32 mil → DH = 51 mil, finished 49 mil.

### Table 5.13 — Hole-to-lead size by producibility level (IPC-2222A Table 9-5 p.25) (p.106)

| Finished hole | Level A (mil / mm) | Level B (mil / mm) | Level C (mil / mm) |
|---|---|---|---|
| Minimum = max lead diameter + | 10 / 0.25 | 8 / 0.20 | 6 / 0.15 |
| Maximum = min lead diameter + | 28 / 0.70 | 28 / 0.70 | 24 / 0.60 |

Example: 32 mil ±10% lead → max 35.2, min 28.8 mil → Level A hole 45.2–56.8 mil.

### Eq. 5.5 + Tables 5.14–5.15 — PTH land diameter (IPC-2221B p.96, Tables 9-1, 9-2) (p.106–107)

DP = a + 2·b + c; a = finished hole (DH − 2TP); b = minimum annular ring; c = standard fabrication allowance.

| Table 5.14 annular ring b | mil | mm |
|---|---|---|
| Internal | 1 | 0.025 |
| External | 2 | 0.05 |

| Table 5.15 fabrication allowance c | Level A | Level B | Level C |
|---|---|---|---|
| mil | 16 | 10 | 8 |
| mm | 0.40 | 0.25 | 0.20 |

Example: drill 50 mil, TP 1 mil, external, Level A → DP = 48 + 4 + 16 = 68 mil.

Plane clearance (p.107–108): antipad diameter = drill + 20 mil (0.51 mm) minimum (10 mil / 0.25 mm edge clearance, IPC-2222 Fig. 9-1); and edge clearance must also satisfy Table 6.8 voltage spacing (IPC-2221B §6.3.1). Soldermask oversize commonly 5 mil; paste = land.

### Tables 6.2–6.7 — Transmission-line design equations (IPC-2141A; IPC-2251 pp.32–36; Montrose 1999/2000; Brooks 2003) (p.135–142)

Symbols: w = trace width, t = trace thickness, h = dielectric height trace-to-plane (h1 above / h2 below for embedded or asymmetric), H = total dielectric (plane-to-plane for stripline; plane-to-top-of-cover for embedded microstrip), d = edge-to-edge spacing of a differential pair (D = vertical spacing for broadside), εr = relative permittivity. Units of w, t, h, d consistent (mil, in, cm). C0 in pF/in, L0 in nH/in, tPD in ps/in.

| Topology | Z0 (Ω) | Zdiff (Ω) | Design width / spacing | tPD (ps/in) | C0 (pF/in) | Restrictions | conf |
|---|---|---|---|---|---|---|---|
| Surface microstrip | (k/sqrt(εr + 1.41))·ln(5.98·h/(0.8·w + t)); k = 87 for 15 < w < 25 mil, k = 79 for 5 < w < 15 mil | — | w = 7.475·h·exp(−Z0·sqrt(εr + 1.41)/k) − 1.25·t | 84.75·sqrt(0.475·εr + 0.67) | 0.67·(εr + 1.41)/ln(5.98·h/(0.8·w + t)) | 0.1 < w/h < 3.0; 1 < εr < 15 (FR4 4.0–4.5) | high |
| Surface differential (edge-coupled) | as surface | 2·Z0·[1 − 0.48·exp(−0.96·d/h)] | d = −(h/0.96)·ln(2.08 − 1.04·Zdiff/Z0) | as surface | — | Z0 < Zdiff < 2·Z0 | high |
| Embedded microstrip | (87/sqrt(εr' + 1.41))·ln(5.98·h2/(0.8·w + t)); εr' = εr·[1 − exp(−1.55·H/h2)] | — | w = 7.475·h2·exp(−x) − 1.25·t, x = Z0·sqrt(εr' + 1.41)/87 | 84.75·sqrt(εr') or 84.75·sqrt(0.475·εr + 0.67) | 1.41·εr'/ln(5.98·h/(0.8·w + t)) | 0.1 < w/h2 < 3.0; 1 < εr < 15; w and dielectric 5–15 mil; 40 < Z0 < 90 Ω | high |
| Embedded differential | as embedded | 2·Z0·[1 − 0.48·exp(−0.96·d/(h1 + h2 + t))] | d = −((h1 + h2 + t)/0.96)·ln(2.08 − 1.04·Zdiff/Z0) | as embedded | — | as embedded | high |
| Symmetric (balanced) stripline | (60/sqrt(εr))·ln(1.9·(2·h + t)/(0.8·w + t)) = (60/sqrt(εr))·ln(1.9·H/(0.8·w + t)), H = h1 + h2 + t | — | w = 1.25·[1.9·H·exp(−Z0·sqrt(εr)/60) − t] | 84.75·sqrt(εr) | 1.41·εr/ln(3.81·h/(0.8·w + t)) | w/(h − t) < 0.35; w/h < 2.0; t/h < 0.25; 0.005 < w < 0.015 in; w, dielectric 5–15 mil; 40 < Z0 < 90 Ω | high |
| Asymmetric (unbalanced) stripline | (80/sqrt(εr))·ln(1.9·(2·h2 + t)/(0.8·w + t))·[1 − h2/(4·H)] | — | w = 2.375·(2·h2 + t)·exp(−x) − 1.25·t, x = Z0·sqrt(εr)/(80·(1 − h2/(4·H))) | 84.75·sqrt(εr) | 2.82·εr/ln(2·(h − t)/(0.268·w + 0.335·t)) | w/(h2 − t) < 0.35; t/h2 < 0.25 | medium |
| Edge-coupled differential stripline (sym. or asym.) | per row above | 2·Z0·[1 − 0.374·exp(−2.9·d/H)] (Table 6.4: 0.347 with (2h + t)) | d = −0.347·H·ln[2.67·(1 − Zdiff/(2·Z0))] | 84.75·sqrt(εr) | — | — | medium |
| Broadside-coupled differential stripline | — | (82.2/sqrt(εr))·ln(5.98·D/(0.8·w + t))·(1 − exp(−0.6·h)) as printed (exp argument garbled) | w = 7.475·D·exp(−x) − 1.25·t, x = Zdiff·sqrt(εr)/(82.2·(1 − exp(−0.6·h))) | 84.75·sqrt(εr) | — | none given | low |

General: C0 = tPD/Z0 (pF/in, ps/in, Ω); L0 = Z0²·C0/1000 (nH/in). Reflection ρ = (Z_T − Z0)/(Z_T + Z0). PT = L·tPD; L_SE = v_P·RT; L_max(digital) = RT/(2·tPD); L_max(analog) = λ/15 with λ = 1/(f·tPD).

### Table 6.8 — Minimum conductor spacing, mil (abridged IPC-2221B Table 6-1) (p.165)

| Voltage between conductors (VDC or Vp-p) | Internal traces | External, bare | External, soldermask only | External, conformal coating |
|---|---|---|---|---|
| 0–15 | 2 | 4 | 2 | 5 |
| 16–30 | 2 | 4 | 2 | 5 |
| 31–50 | 4 | 24 | 5 | 5 |
| 51–100 | 4 | 24 | 5 | 5 |

### Table 6.9 — TD (= PT) for various trace lengths, ALS logic RT ≈ 2 ns, surface microstrip εr = 4.2 (TD values imply tPD ≈ 137 ps/in) (p.170)

| Case | L_trace (in) | k ≈ RT/PT | TD (ns) |
|---|---|---|---|
| Long | 30 | 1/2 | 4.1 |
| Critical | 7.3 | 2 | 1 |
| Safe | 3.5 | 4 | 0.24 as printed (0.48 consistent with 137 ps/in) |

### Reference stack-ups (Figs. 6.33–6.36; 1 oz = 1.35 mil Cu; dielectric thickness in mil between successive copper layers) (p.158–160)

| Layers | Layer order (top → bottom) | Dielectrics (mil) | Line types |
|---|---|---|---|
| 4 (A) | Sig-H, GND, PWR, Sig-V | 10, 40, 10 | surface microstrip both sides (most common) |
| 4 (B) | GND, Sig-H, Sig-V, PWR | 10, 40, 10 | unbalanced stripline (planes outside shield) |
| 4 (C) | GND, Sig-H + PWR, Sig-V + PWR, GND | 10, 40, 10 | unbalanced stripline; ±V routed as wide traces/pours |
| 6 (A) | Sig-H, GND, Sig-V, Sig-H, PWR, Sig-V | 10, 14, 10, 14, 10 | surface microstrip outer, asymmetric stripline inner |
| 6 (B) | Sig-R, GND, +PWR + Sig-R, −PWR + Sig-R, GND, Sig-R | 10, 14, 10, 14, 10 | dual-supply analog; GND adjacent to all |
| 6 (C) | GND, HS-H, GND, PWR, HS-V, GND | 11.5, 11.5, 11.5, 11.5, 11.5 | balanced stripline high-speed pairs |
| 8 (A) | Sig-H, PWR, GND, Sig-V, Sig-H, GND, PWR, Sig-V | 8.7, 9.1, 8.7, 9.1, 8.7, 9.1, 8.7 | surface microstrip outer, asymmetric stripline inner |
| 8 (B) | GND, HS-H, GND, HS-V, PWR, Sig-H, Sig-V, GND | 8 × 7 | balanced stripline HS; asymmetric stripline H/V |
| 10 | Sig-H, GND, HS, HS, PWR, GND, HS, HS, GND, Sig-V | 5.6, 5.3, 5.6, 5.3, 9.1, 5.3, 5.6, 5.3, 5.6 | surface microstrip outer; asymmetric stripline HS |

Finished thickness for the examples: 0.093 in.

### Table 7.1 — Schematic pin types, shapes and visibility (p.176)

| Pin types (electrical) | Pin shapes | Visibility settings |
|---|---|---|
| Power/GND, Three state, Bidirectional, Open collector, Open emitter, Input, Output, Passive | Clock, Dot, Dot-clock, Line, Short, Zero length | pin number, pin name, the pin itself (power pins only; all other pins are always visible) |

### Table 8.3 — Chip-capacitor footprint data, mil (p.248)

| Parameter | smdcap (≈2010) X | smdcap Y | IPC 1206 X | IPC 1206 Y |
|---|---|---|---|---|
| Pad size | 87 | 50 | 71 | 45 |
| Pad center-to-center | 195 | — | 118 | — |
| Body L / W | 245 | 90 | 126 | 63 |
| Place outline L / W | 250 | 90 | 185 | 91 |
| Padstack | smd50_87 | | smd45_71 | |

Origin at body center, so outline coordinates are ± half the listed values.

### Table 8.4 — Reference through-hole padstack pad62cir42d, mil (p.260)

| Parameter | mil |
|---|---|
| Drill-hole diameter | 42 |
| Outer pad diameter | 62 |
| Outer antipad diameter | 82 |
| Outer pad-to-antipad clearance | 10 |
| Outer annular ring | 10 |
| Inner pad diameter | 60 |
| Inner antipad diameter | 80 |
| Inner annular ring | 9 |
| Inner pad-to-antipad clearance | 10 |

Thermal flash (IPC-2222A pp.21–22): ID = pad on that layer, OD = antipad (± a couple of mils), spoke W = 0.6·P/n → TR_80_60_9: ID 60, OD 80, 4 spokes, W = 9 mil. Other flashes used: F2_3X2_7 = ID 90 mil (2.3 mm), OD 106 mil (2.7 mm), spokes 20 mil (0.5 mm), with antipad 155 mil (p.343–344); TR_90_60 on pad 60/hole 36, TR_102_72 on pad 72/hole 42 (Table 10.1).

### Table 8.5 — Basic hole types (p.264)

| | With pads (lands) | Without pads |
|---|---|---|
| Plated | plated, supported | plated, no lands |
| Nonplated | nonplated with lands | nonplated unsupported hole (library mtgXXX; XXX = drill in mil; e.g., mtg125 = 125 mil drill, 25 mil dummy pads, antipad = drill + 20 mil) |

### Table 9.5 — Mixed-signal board constraint table (example) (p.371)

| Item | Value |
|---|---|
| Component mounting | mixed SMD and THD |
| Sides with parts | 1 |
| Plane layers / routing layers / total (min) | 2 / 2 / 4 |
| Smallest leads | SOIC |
| Pad spacing (min) | 50 mil |
| Pad width (max) | 25 mil |
| Maximum current | 0.1 A |
| Trace width min, inner / outer | 1.3 mil / 0.5 mil |
| Maximum voltage | 10 V |
| Trace spacing, inner / outer | 4 mil / 5 mil |

### Table 9.7 — Net, layer, via and constraint-set relationships (10-layer shielded example) (p.407)

| Net | Routing layers | Plane | Via | Physical CSet |
|---|---|---|---|---|
| Analog nets | TOP, ANLGBOT | — | BBANLG | PCSanalog |
| V+ | Top | VPOS | BBANLG | — |
| AGND | Top | AGND | BBANLG | — |
| V− | Top | VNEG | BBANLG | — |
| SHLD | — | SHIELD | VIA (modified) | — |
| VCC | BOTTOM | VCC | BBDIG-VCC-BOTTOM | — |
| GND | BOTTOM | GND | BBDIG-GND-BOTTOM | — |
| Digital bus nets | DIGTOP, BOTTOM | — | BBDIG-DIGTOP-BOTTOM | PCS1 |
| Digital ADC nets | TOP, DIGTOP, BOTTOM | — | VIA (through) | PCS2 |

### Table 9.9 — Via set for the 4-layer high-speed example, mil (p.427)

| Via | Function | Drill | Pad | Clearance | Plane connection | Soldermask opening |
|---|---|---|---|---|---|---|
| VIA | default | 13 | 24 | 30 | full | yes |
| VIATENT | fan-outs | 13 | 24 | 30 | full | no (tented) |
| VIAHEAT | heat pipes | 10 | 20 | 26 | full | yes |

### Table 9.10 — Maximum safe trace lengths, surface microstrip εr = 4.2, tPD = 137 ps/in (p.437)

| Driver | RT (ns) | L_max k = 2 (in) | L_max k = 3 (in) | L_max k = 4 (in) |
|---|---|---|---|---|
| 66 MHz oscillator (RT assumed ¼ period) | 3.8 | 13.9 | 9.26 | 6.95 |
| ALS logic | 1.9 | 6.95 | 4.63 | 3.47 |
| ADN2530 | 0.026 | 0.095 | 0.063 | 0.048 |

L_max = RT/(k·tPD) (Eq. 9.1). Surface-microstrip 50 Ω design (Eq. 9.3): h = 10 mil, t = 1.35 mil, εr = 4.2, k = 87 → w = 17.5 mil (17 mil → 50.9 Ω).

### Table 10.1 — Manufacturing example parts, footprints, padstacks, flashes (p.470)

| Item | Qty | Ref | Part | Footprint | Padstack | Flash / clearance |
|---|---|---|---|---|---|---|
| 1 | 1 | C1 | 0.1 µF | smdcap1206 | smd45rec71 | N/A |
| 2 | 1 | J1 | CON10 | CH10_Conn10f | CH10_pad60cir36f | TR_90_60 |
| 3 | 2 | M1, M2 (plated, grounded mounting holes) | MTG130 | CH10_mtg130p | CH10_pad400cir130f | AB00 |
| 4 | 2 | R1, R2 | 1 kΩ | CH10_res400f | CH10_pad72cir42f | TR_102_72 |
| 5 | 1 | U1 | 7400 | soic14 | smd50_25 | N/A |
| 6 | 2 | (nonplated mounting holes) | — | CH10_mtg130np | CH10_Hole130np | circle 160 |
| 7 | — | (vias) | — | — | VIA | AB00 |

### Table 10.2 — Elements of a fiducial (p.474)

| Function | Class | Subclass | Example size (p.475) |
|---|---|---|---|
| Copper object | Etch | Top | 40 × 40 mil |
| Soldermask opening | Board geometry | Soldermask_Top | 50 × 50 mil (5 mil larger per side) |
| Pastemask opening | Board geometry | Pastemask_Top | 40 × 40 mil (directly over the copper) |

### Tables 10.3–10.4 — Artwork film contents (p.481–482)

| Film | Classes collected |
|---|---|
| Each copper layer (conductor) | Etch, Pin, Via (that layer) |
| Silkscreen (per side) | Board geometry, Component value, Component device type, Component reference designator, Component tolerance, Component user part number, Package geometry |
| Soldermask (per side) | Board geometry, Package geometry, Pin, Via |
| Outline | Photoplot/board outline |
| Paste (per side, if stencil) | Package geometry / pin paste, board-geometry paste (fiducials) |

### Appendix B — Package outline data (JEDEC JEP95 and EIA/EIAJ; "as printed") (p.559–572)

Table B.2 — common discrete packages:

| Type | Case / size | Standard |
|---|---|---|
| Resistor, chip | 0402, 0805, 1206, … | IEC 60115-B, JIS C 5201-B (as printed) |
| Capacitor, tantalum (molded) | A 3216-18, B 3528-21, C 6032-28, D 7343-31, E 7260-38, R 2012-12, T 3528-12, V 7343-20, X 7343, Y 7340 | EIAJ RC-2134B / EIA size codes |
| MELF (DL-41, LL-34) | metal electrode face | EIC 10H01, LL-34 |
| SOD, SC-76 (molded) | small outline diode | JEDEC DO215-D, EIAJ SC-76 |
| SMA / SMB / SMC (molded) | SMT diode outline | JEDEC DO214-D variation AC / AA / AB |
| DO-213 (BMELF) | diode outline | JEDEC DO213-D |
| DO-214 (molded) | diode outline | JEDEC DO214-D |
| Inductor chip / molded / power wire-wound | 0805, 1206 / IMC-2220 / MSS5131 | chip sizes as resistor; vendor outlines (Vishay, Coilcraft) |

Table B.3 — discrete power packages:

| Package | JEDEC | Variation — pitch (leads) |
|---|---|---|
| DPAK (TO-252) | TO252-E | AA, AB, AC — 0.090 in (3); AD — 0.045 in (5) |
| D2PAK (TO-263) | TO263-D | AA — 0.100 in (4); AB — 0.100 in (3); BA — 0.067 in (6); BB — 0.067 in (5); CA — 0.050 in (8); CB — 0.050 in (7) |
| D3PAK (TO-268) | TO268-A | AA — 5.45 mm (4) |

Table B.4 — small-outline transistor packages:

| Package | JEDEC | Variation — pitch |
|---|---|---|
| SOT23-3, SC-59, SSOT-3 (3-lead) | TO-236 | AA, AB — 0.95 mm (dimension a); 1.90 mm (dimension b) |
| SOT23-5, SC-74A (5), SOT-26 (6), SOT23-8 (8) | MO178-C, MO193-C | AA — 0.95 mm (5); AB — 0.95 mm (6); BA — 0.65 mm (8) |
| SOT223-3 (4-lead), SOT223-4 (5-lead) | TO261-C | AA — 2.30 mm (4); AB — 1.50 mm (5) |
| SOT-89 (2- and 3-lead) | TO243-C | AB — 3.0 mm (2); AA — 1.5 mm (3) |
| SOT-143, SOT-343 (4-lead) | TO253-D (EIAJ SC-61B) | AA — 1.92 mm; 1.30 mm |
| SOT-353, SC-88 (5), SC70 (6), SC-74 (8), SSOT-n | MO059-B, MO203-B | AA — 0.65 mm (5); AB — 0.65 mm (6); BA — 0.50 mm (8) |

Table B.5 — small-outline IC packages:

| Package | Leads | JEDEC | Width across leads | Pitch | Lead width | Lead gap |
|---|---|---|---|---|---|---|
| MSOP, body 2.3 / 2.8 / 3.0 mm | 8, 10 | MO187-E | — | AA, AA-T, DA 0.65 mm (8); CA 0.50 mm (8); BA, BA-T 0.50 mm (10) | — | — |
| SOIC narrow, 0.150 in (3.8 mm) body | 8, 14, 16 | MS012-E | 0.236 in (6.0 mm) | 0.050 in (1.27 mm) | 0.016 in (0.40 mm) | 0.034 in (0.87 mm) |
| SOIC wide, 0.300 in (7.5 mm) body | 14, 16, 18, 20, 24, 28 | MS013-E | 0.403 in (10.3 mm) | 0.050 in (1.27 mm) | 0.016 in (0.4 mm) | 0.034 in (0.87 mm) |
| SSOP narrow, 0.150 in (3.8 mm) body | 14, 16, 18, 20, 24, 28 | MO137-C | 0.236 in (6.0 mm) | 0.025 in (0.635 mm) | 0.010 in (0.25 mm) | 0.015 in (0.385 mm) |
| SSOP wide, 0.300 in (7.5 mm) body | — | MO118-B | 0.410 in (10.4 mm) | 0.025 in (0.635 mm) | 0.010 in (0.25 mm) | 0.015 in (0.4 mm) |
| SOP | 28, 48, 56, 64 (44–90 …) | MO174-A, MO175-A, MO180-B | various | — | — | — |

Table B.6 — through-hole packages (row alignment reconstructed):

| Package | JEDEC |
|---|---|
| DIP, 0.100 in pitch | MS001-D |
| DO-35 | DO-204-AH |
| DO-15 (DO-41 glass/plastic) | DO204B-D, MO043-A (as printed) |
| IPAK (TO-251) / I2PAK (TO-262) | TO251-D / TO262-A |
| TO-205AF / TO-39 | TO205-E |
| TO-3P / TO-41 / TO-247AD | TO204-C |
| TO-92; TO-18 | TO226-G; TO206-B |
| TO-126 | similar to TO-220 |
| TO-218AC / TO-220 (and variations) / TO-226AE | TO218-E / TO220-K, TO262-A / TO226-G |
| TO-247 (2L, 3L) / TO-264 | TO247-E_01 / TO264-B |

Tables B.7–B.10 — array and chip-carrier families (JEDEC doc → title; pitch where given):

- BGA (B.7): MO-151 → elevated to MS-034A (revised to MS-034B 2/20/03); MO-156 square ceramic BGA 1.00/1.27/1.50 mm; MO-157 rectangular ceramic BGA; MO-158-D column grid array 47.5/50.0/52.5/55.0 mm bodies, 1.27 and 1.00 mm pitch; MO-163-B replaced by MS-028-A; MO-192 low-profile square BGA; MO-195 thin fine-pitch BGA 0.5 mm; MO-205 low-profile fine-pitch BGA 0.80 mm (rectangular); MO-207 square and rectangular die-size BGA; MO-210 thin fine-pitch rectangular BGA 0.80 mm; MO-211 die-size BGA, thin/very thin/extremely thin; MO-216 thin square/rectangular BGA 1.00 and 0.80 mm; MO-219 low-profile FBGA 0.80 mm; MO-221 extremely thin two-row cavity-down BGA 0.50 mm; MO-222 ceramic BGA rectangular; MO-225 VFBGA variations AB, BC; MO-228 square dual-pitch FBGA; MO-233 mixed pitch 0.80/1.00 mm DSBGA; MO-234B low-profile rectangular BGA; MO-237E DDR2 SDRAM DIMM 1.00 mm contact centers; MO-242B rectangular die-size stacked BGA 0.80 mm; MO-246C rectangular fine-pitch thin BGA 0.65 mm; MO-261A thick/very thick rectangular fine-pitch BGA 0.80 mm; MO-264A die-size stacked BGA dual pitch; MO-266A very thin stackable BGA 0.50 mm; MO-273A upper PoP square FBGA 0.65 and 0.50 mm; MO-275-A low-profile square FBGA; MO-280A ultrathin / very very thin FBGA; MO-028-C rectangular BGA variations; MS-034-D plastic BGA 1.0/1.27/1.5 mm pitch with increased dimensions for thicker packages.
- QFP (B.8): MO-134-A CQFP 0.50 mm lead pitch, ceramic nonconductive tie bar; MO-143-C replaced by MS-029-A; MO-148-A MCM ceramic QFP (S-CQFP); MO-188-B power PQFP with heat slug; MO-189-A plastic QFP/heat slug (H-LQP/G) 2.00 mm thick / 2.00 mm footprint; MO-198-A 3-tier PQFP-B; MO-204-B PQFP with exposed heat sink; MS026-D low/thin-profile plastic QFP, 2.00 mm footprint, optional heat slug; TO271-A 4-lead quad flatpack.
- QFN (B.8/B.9): MO-220K thermally enhanced very thin / very very thin fine-pitch QFN; MO-239-B very thin dual-row QFN; MO-241-B DIL-compatible thermally enhanced QFN; MO-243-A bumped QFN; MO-247C staggered multirow QFN; MO-248E ultrathin/extremely thin QFN; MO-250-A bumped very thin QFN; MO-251-A very thick QFN; MO-254-A low/thin-profile QFN; MO-255-B very very thin / ultrathin / extremely thin quad flat small-outline nonleaded; MO-257-B staggered two-row thermally enhanced; MO-262A 0.50 mm flange-molded thermally enhanced (topside) QFN; MO-263A 0.50 and 0.40 mm flange-molded QFN; MO-265A QFN with corner terminals; MO-267B punch-singulated staggered dual-row QFN.
- Chip carriers (B.10): 0.050 in center leadless types A–D MS002-A, MS003-A, MS004-B, MS005-A (variations AA–AH, BA–BH, CA–CH, DA–DH), types E/F MO041-C/MO042-A; leaded 0.050 in types A/B MS006-A, MS007-A, MS008-A; 0.040 in center MS009-A, MS014-A (ceramic single layer); 0.025 in MO056-A, MO062-A (148 pin), MO131-A (top brazed); 0.020 in MO057-A, MO129-A; 0.015 in MO130-A; plastic chip carriers 1.27 mm/0.050 in MS016-A (rectangular), MS018-A (square), MO047-B (square), MO052-A (replaced by MS-016-A); ceramic leaded 0.050 in 68/84 terminals MO044-A; J-lead/gull-wing ceramic MO107-A (J-bend, 20 mil min), MO110-A, MO111-A; leadless SO ceramic MO126-B (0.400 in body), MO144-A (0.350 in body, R-CDCC-N); SOJ ceramic MO147-A (0.415 in body); nonhermetic LCC MO075-A (square), MO076-A (SO rectangular); very very thin quad bottom-terminal MO217-B.

### Appendix C — Rise and fall times of logic families (IPC-2251 Table 5-4 partial; Coombs Table 13.2) (p.573–574)

| Group | Family | RT (ns) | FT (ns) | Rank as printed (1 = fastest) |
|---|---|---|---|---|
| BiCMOS | ABT | 1.6 | 1.4 | 14 |
| BiCMOS | BCT | 0.7 | 0.7 | 12 |
| BiCMOS | LVT | 2.7 | 2.8 | 29 |
| CMOS | AC | 1.7 | 1.5 | 15 |
| CMOS | ACT | 1.7 | 1.5 | 25 |
| CMOS | ACQ | 2.4 | 2.4 | 16 |
| CMOS | ACTQ | 2.5 | 2.4 | 27 |
| CMOS | AHCT | 2.4 | 2.4 | 26 |
| CMOS | C | 35 | 25 | 39 |
| CMOS | FCT | 1.5 | 1.2 | 13 |
| CMOS | HC | 3.6 | 4.1 | 33 |
| CMOS | HCT | 4.6 | 3.9 | 34 |
| CMOS | LCX | 2.9 | 2.4 | 28 |
| CMOS | LV | 3.0 | 3.0 | 30 |
| CMOS | LVQ | 3.5 | 3.2 | 31 |
| CMOS | LVX | 4.8 | 3.7 | 35 |
| CMOS | VCX | 2.0 | 2.0 | 20 |
| CMOS | VHC | 4.1 | 3.2 | 32 |
| ECL | 10K | 2.2 | 2.2 | 22 |
| ECL | 10KH | 1.7 | 1.7 | 17 |
| ECL | 100K | 0.6 | 0.6 | 11 |
| ECL | 300K | 0.5 | 0.5 | 10 |
| ECL | E | 0.38 | 0.38 | 8 |
| ECL | EP | 0.11 | 0.11 | 6 |
| ECL | LVEL | 0.22 | 0.22 | 3 |
| ECL | EL | 0.23 | 0.23 | 5 |
| GaAs | GaAs | 0.02 | 0.02 | 1 |
| LVDS | LVDS | 0.3 | 0.03 (as printed) | 2 |
| SiGe | SiGe-2.5V | 0.3 | 0.1 | 4 |
| SiGe | SiGe-3.3V | 0.3 | 0.3 | 7 |
| SSTL | SSTL | 0.3 | 0.5 | 9 |
| TTL | 74nn | 8.0 | 5.0 | 36 |
| TTL | ALS | 2.3 | 2.3 | 24 |
| TTL | AS | 2.1 | 1.5 | 18 |
| TTL | F | 2.3 | 1.7 | 21 |
| TTL | FR | 2.1 | 1.5 | 19 |
| TTL | H | 7.0 | 7.0 | 37 |
| TTL | L | 35 | 30 | 40 |
| TTL | LS | 15 | 10 | 38 |
| TTL | S | 2.5 | 2.0 | 23 |

Note: rows reconstructed from a flattened extraction (conf medium). The printed ranks disagree with the values for several rows (e.g., ACT vs ACQ, EP vs LVEL) and the LVDS FT of 0.03 ns is likely a typo for 0.3 ns; use the RT/FT columns, not the rank. The book elsewhere uses ALS RT ≈ 2 ns (p.171) and 1.9 ns (p.437).

### Appendix D — Drill and screw dimensions (p.575–576)

Table D.1 — English sizes (inches):

| Screw | Threads/in | Close fit drill (min in) | Normal fit drill (min in) | Loose fit drill (min in) | Head dia typ | Washer dia typ | Nut size |
|---|---|---|---|---|---|---|---|
| 0 | 80 | No.51 (0.067) | No.48 (0.079) | 3/32 (0.104) | 0.116 | 0.188 | 5/32 |
| 1 | 72 or 64 | No.46 (0.081) | No.43 (0.092) | No.37 (0.114) | 0.141 | 0.219 | 5/32 |
| 2 | 64 or 56 | 3/32 (0.094) | No.38 (0.105) | No.32 (0.126) | 0.167 | 0.250 | 3/16 |
| 3 | 56 or 48 | No.36 (0.106) | No.32 (0.119) | No.30 (0.140) | 0.193 | 0.312 | 3/16 |
| 4 | 48 or 40 | No.31 (0.120) | No.30 (0.130) | No.27 (0.156) | 0.219 | 0.375 | 1/4 |
| 5 | 44 or 40 | 9/64 (0.141) | 5/32 (0.160) | 11/64 (0.184) | 0.245 | 0.406 | 1/4 |
| 6 | 40 or 32 | No.23 (0.154) | No.18 (0.174) | No.13 (0.197) | 0.270 | 0.438 | 5/16 |
| 8 | 36 or 32 | No.15 (0.180) | No.9 (0.200) | No.3 (0.225) | 0.322 | 0.445 | 11/32 |
| 10 | 32 or 24 | No.5 (0.206) | No.2 (0.225) | B (0.250) | 0.373 | 0.500 | 3/8 |
| 1/4 | 28 or 20 | 17/64 (0.266) | 9/32 (0.286) | 19/64 (0.311) | 0.492 | 0.625 | 7/16 |
| 5/16 | 24 or 18 | 21/64 (0.328) | 11/32 (0.349) | 23/64 (0.373) | 0.615 | 0.688 | 9/16 |
| 3/8 | 24 or 16 | 25/64 (0.391) | 13/32 (0.411) | 27/64 (0.438) | 0.740 | 0.813 | 5/8 |

Note: for normal and loose fits the printed "Min (in.)" is slightly larger than the listed gauge drill (e.g., No.30 = 0.1285 in vs 0.130); treat "Min" as the minimum finished clearance hole.

Table D.2 — Metric sizes (mm):

| Screw | Pitch | Close fit | Normal fit | Loose fit | Head / nut size | Washer dia |
|---|---|---|---|---|---|---|
| M1.6 | 0.4 | 1.7 | 1.8 | 2.0 | 2.9 | 3.2 |
| M2.0 | 0.4 | 2.2 | 2.4 | 2.6 | 3.6 | 4.0 |
| M2.5 | 0.5 | 2.7 | 2.9 | 3.1 | 4.5 | 5.0 |
| M3.0 | 0.5 | 3.2 | 3.4 | 3.6 | 5.4 | 6.0 |
| M4.0 | 0.7 | 4.3 | 4.5 | 4.8 | 7.2 | 8.0 |
| M5.0 | 0.8 | 5.3 | 5.5 | 5.8 | 9.0 | 10.0 |
| M6.0 | 1.0 | 6.4 | 6.6 | 7.0 | 10.8 | 12.0 |
| M8.0 | 1.3 | 8.4 | 9.0 | 10.0 | 14.4 | 16.0 |
| M10 | 1.5 | 10.5 | 11.0 | 12.0 | 18.0 | 20.0 |

(Tabulated head/nut = 1.8·d and washer = 2·d throughout — derived observation.)

## 3. Mechanizable checks

Units: mil unless stated (1 mil = 0.0254 mm). "Level" = IPC producibility level A/B/C. Margins are positive when passing.

Hole, land and via geometry
- `CHECK-aspect-ratio`: inputs board_thickness_mil, finished_hole_mil (smallest plated hole), level → AR = board_thickness / finished_hole → pass AR ≤ AR_max with AR_max = 5 (Level A; target 3), 8 (Level B), ≥ 9 only with written fab confirmation (Level C) → margin = AR_max − AR → MITZ-044.
- `CHECK-hole-vs-lead`: inputs lead_dia_max, lead_dia_min, finished_hole, level → d_min = lead_dia_max + {A 10, B 8, C 6}; d_max = lead_dia_min + {A 28, B 28, C 24} → pass d_min ≤ finished_hole ≤ d_max → margin = min(finished_hole − d_min, d_max − finished_hole) → MITZ-080 (Table 5.13).
- `CHECK-drill-factor`: inputs lead_dia, drill_dia, plating_thk (default 1 mil) → k = drill_dia / (lead_dia + 2·plating_thk) → pass 1.05 < k ≤ 3.0 (1.5 recommended) → margin = min(k − 1.05, 3.0 − k) → MITZ-079.
- `CHECK-pth-land`: inputs finished_hole, pad_dia, layer ∈ {internal, external}, level → DP_min = finished_hole + 2·b + c, b = 1 (internal) / 2 (external), c = 16 / 10 / 8 (A / B / C) → pass pad_dia ≥ DP_min → margin = pad_dia − DP_min → MITZ-081 (Eq. 5.5).
- `CHECK-plane-antipad`: inputs drill_dia, antipad_dia, max_pad_dia over all layers, V_between (plane vs hole net) → pass antipad_dia ≥ drill_dia + 20 AND antipad_dia > max_pad_dia AND (antipad_dia − drill_dia)/2 ≥ S_internal(V_between) from Table 6.8 → margin = min of the three differences → MITZ-084, -085, -168, -147.
- `CHECK-npth-clearance`: inputs npth_drill, plane_clearance_dia → pass plane_clearance_dia ≥ npth_drill + 20 → margin = plane_clearance_dia − npth_drill − 20 → MITZ-180.
- `CHECK-thermal-spokes`: inputs pad_dia P, n_spokes, spoke_width W → W_target = 0.6·P/n → pass n·W ≥ 0.6·P (total spoke copper ≥ 60 % of pad diameter; interpretation, conf medium) → margin = n·W − 0.6·P → MITZ-177.
- `CHECK-backdrill`: inputs finished_dia_mm, backdrill_dia_mm → pass 0.3 ≤ backdrill − finished ≤ 0.4 mm → margin = distance to the nearer bound → MITZ-166.
- `CHECK-hole-web`: inputs hole pairs (center distance, d1, d2) → web = center_distance − (d1 + d2)/2 → pass web > 20 → margin = web − 20 → MITZ-064.
- `CHECK-blind-via-sanity`: inputs via padstack spans, plane nets per layer → pass no via spans connect two different plane nets (e.g., VCC–GND) → margin = count of violators (must be 0) → MITZ-208.

Conductors, current and spacing
- `CHECK-trace-ampacity`: inputs I_A, copper_oz, layer ∈ {internal, external}, dT_C, T_ambient_C, trace_width → w_min = (1/(1.4·copper_oz))·(I_A/(k·dT_C^0.421))^1.379 with k = 0.024 internal, 0.048 external → pass trace_width ≥ w_min AND T_ambient + dT < Tg (FR4 125–135 °C, use 125) → margin = trace_width − w_min → MITZ-141, -142, -195. Self-test anchors (1 oz, ΔT 10 °C): 0.3 A internal → ≈ 6.1 mil; 0.6 A external → ≈ 6.1 mil; 0.1 A internal → ≈ 1.3 mil; 0.1 A external → ≈ 0.5 mil.
- `CHECK-copper-thickness-basis`: inputs copper_oz, layer → t_calc = minimum finished thickness from Table 4.6 (internal or external column) → pass the impedance/current calculations use t_calc, not nominal (flag if nominal used) → MITZ-037.
- `CHECK-voltage-spacing`: inputs V_between (VDC or Vpk-pk), layer ∈ {internal, external}, coating ∈ {bare, soldermask, conformal}, spacing → S_min from Table 6.8 (0–30 V: 2 / 4 / 2 / 5; 31–100 V: 4 / 24 / 5 / 5 for internal / bare / mask / coated) → pass spacing ≥ S_min; V_between > 100 V → error "outside book table, use IPC-2221B Table 6-1" → margin = spacing − S_min → MITZ-147, -196.
- `CHECK-min-width-space`: inputs min_trace, min_space, fab_min → pass min_trace ≥ max(3.9, fab_min) AND min_space ≥ max(3.9, fab_min) → margin = min(min_trace, min_space) − max(3.9, fab_min) → MITZ-040, -239.
- `CHECK-3w`: inputs net pairs with parallel run, trace_width w, edge_spacing, sensitive flag → pass edge_spacing ≥ 2·w (center ≥ 3·w) for sensitive nets; warn if center spacing < 10·w on very sensitive nets → margin = edge_spacing − 2·w → MITZ-148, -203.

Transmission lines and timing
- `CHECK-tpd`: inputs topology, εr, (H, h2 for embedded) → tPD = 84.75·sqrt(0.475·εr + 0.67) (surface microstrip), 84.75·sqrt(εr') (embedded), 84.75·sqrt(εr) (stripline) ps/in → feeds the length checks → MITZ-107, -109, -111.
- `CHECK-critical-length-digital`: inputs net, L_trace_in, RT_ns, FT_ns (or logic family → Appendix C), tPD_ps_per_in → t_edge = min(RT, FT); k = t_edge·1000 / (L_trace·tPD) → pass k ≥ 2 (limit), preferred k ≥ 4; nets failing must be flagged controlled-impedance and pass `CHECK-termination` → margin_in = t_edge·1000/(2·tPD) − L_trace → MITZ-121, -143, -152, -212, -264.
- `CHECK-critical-length-analog`: inputs f_max_Hz, L_trace_in, tPD → λ_in = 1/(f_max·tPD·1e-12) → pass L_trace < λ/15 (IPC-2251); warn when between λ/20 and λ/6 limits quoted in literature → margin = λ/15 − L_trace → MITZ-144.
- `CHECK-highspeed-triage`: inputs min edge rate on board (10–90 %), board area → pass/flag: t_r < 1 ns on a ~3 × 4 in board → high-speed flow (controlled impedance, SI simulation) required → MITZ-253.
- `CHECK-z0-microstrip`: inputs w, h, t, εr, Z_target, tol → Z0 = (k/sqrt(εr + 1.41))·ln(5.98·h/(0.8·w + t)), k = 87 (15 < w < 25 mil) or 79 (5 < w < 15 mil) → pass |Z0 − Z_target| ≤ tol·Z_target AND 0.1 < w/h < 3.0 AND 1 < εr < 15 → margin = tol·Z_target − |Z0 − Z_target| → MITZ-107. Self-test: w 17.5, h 10, t 1.35, εr 4.2, k 87 → 49.95 Ω; w 17 → 50.9 Ω.
- `CHECK-z0-embedded-microstrip`: εr' = εr·(1 − exp(−1.55·H/h2)); Z0 = (87/sqrt(εr' + 1.41))·ln(5.98·h2/(0.8·w + t)) → pass as above plus 5 ≤ w ≤ 15 mil, 5 ≤ h2 ≤ 15 mil, 40 < Z0 < 90 Ω → MITZ-109.
- `CHECK-z0-stripline`: symmetric Z0 = (60/sqrt(εr))·ln(1.9·(2·h + t)/(0.8·w + t)); asymmetric Z0 = (80/sqrt(εr))·ln(1.9·(2·h2 + t)/(0.8·w + t))·(1 − h2/(4·H)) → pass tolerance plus w/(h − t) < 0.35, t/h < 0.25, 40 < Z0 < 90 Ω → MITZ-111, -113.
- `CHECK-zdiff`: surface Zdiff = 2·Z0·(1 − 0.48·exp(−0.96·d/h)); embedded replace h by (h1 + h2 + t); stripline Zdiff = 2·Z0·(1 − 0.374·exp(−2.9·d/H)) → pass |Zdiff − Z_target| ≤ tol·Z_target AND Z0 < Zdiff < 2·Z0 → MITZ-108, -110, -117.
- `CHECK-termination`: inputs Z0, R_driver, R_series, R_load_in, R_parallel, VCC, V_IH → series: pass |R_driver + R_series − Z0| ≤ tol·Z0; parallel: pass |R_load ∥ R_parallel − Z0| ≤ tol·Z0; double termination: pass VCC/2 ≥ V_IH → margin = tol·Z0 − |error| → MITZ-124, -125, -126, -258.
- `CHECK-lattice-overshoot`: inputs VCC, R_S, Z0, R_L, V_abs_max_in, V_IH, V_IL, n_bounces → V1 = VCC·Z0/(Z0 + R_S); ρL = (R_L − Z0)/(R_L + Z0); ρS = (R_S − Z0)/(R_S + Z0); load voltage after n round trips by bounce-diagram summation → pass max(V_load) ≤ V_abs_max AND no re-crossing of V_IH/V_IL after the first crossing → margin = V_abs_max − max(V_load) → MITZ-118, -119, -122. Self-test: 5 V, 10 Ω, 50 Ω, 1 kΩ → 4.17 V launch, 7.92 V first load peak, then 5.42, 3.16, 4.67 V.
- `CHECK-diff-length-match`: inputs L_P, L_N, tolerance (datasheet) → pass |L_P − L_N| ≤ tolerance → margin = tolerance − |L_P − L_N| → MITZ-214.
- `CHECK-bus-via-count`: inputs vias per net for all bits of a bus, N_max → pass all counts equal AND ≤ N_max → MITZ-256.
- `CHECK-neck-length`: inputs neck segments on controlled-impedance nets, max_neck (e.g., 40 mil) → pass every neck length ≤ max_neck → MITZ-213.

Stack-up, planes and return paths
- `CHECK-stackup-reference`: inputs ordered layer list with types → pass every signal layer has an adjacent plane layer; every power plane is adjacent to a return plane (warning only); number of copper layers even; plane layers typed "plane" → margin = count of violations → MITZ-131, -132, -217.
- `CHECK-standard-thickness`: inputs finished thickness → pass value ∈ {0.020, 0.030, 0.040, 0.062, 0.093, 0.125, 0.250, 0.500 in} (else fab confirmation required) → MITZ-034.
- `CHECK-split-plane-overlap`: inputs analog and digital plane polygons per layer, shield layers → pass overlap area between analog and digital planes on adjacent layers = 0 unless a shield plane lies between them → margin = −overlap area → MITZ-102, -207.
- `CHECK-power-area-vs-ground-split`: inputs power pours and ground-split void polygon → pass no power pour crosses the ground split (except the connector region) → MITZ-201.
- `CHECK-trace-over-void`: inputs trace segments with their reference plane, plane voids/splits/moats → pass count(segments whose projection crosses a void) = 0; route keep-out = void grown 10–20 mil → MITZ-202, -215.
- `CHECK-copper-islands`: inputs pour fragments → pass count(fragments not connected to their net or not stitched) = 0 → MITZ-018, -205.
- `CHECK-thermal-connections`: inputs THT pads on plane nets, vias on plane nets → pass every THT pin on a plane net has a thermal relief; routing/fan-out vias and heat-pipe vias are full contact → MITZ-008, -193, -194, -211.
- `CHECK-bypass-presence`: inputs IC power pins, capacitor list with nets → pass every IC supply pin group has ≥ 1 bypass capacitor on the same supply/return pair (the book gives no distance limit) → MITZ-098, -140.

Placement and DFM
- `CHECK-smd-spacing`: inputs component pairs with package class (discrete < 0603, discrete ≥ 0603, IC), edge-to-edge distance, distance to board edge, pad-to-via distance → pass board edge ≥ 60 (1.5 mm); discrete ≥ 0603 ≥ 20 (0.50 mm); discrete < 0603 ≥ 12 (0.30 mm); IC body end-to-end ≥ 20; IC pad-to-pad side-to-side ≥ 20; pad-to-via ≥ 20; mixed → max of the applicable rules → margin = distance − limit → MITZ-065, -066, -067.
- `CHECK-tht-spacing`: inputs axial/radial/DIP bodies with diameters D1, D2, heights → limits per Tables 5.1–5.4 (e.g., axial side-to-edge 75, end-to-edge 90, end-to-end 100; radial edge ≥ max(D/2, H/2, 60); DIP end-to-end 200) → pass distance ≥ limit → MITZ-060–063.
- `CHECK-courtyard-excess`: inputs footprint courtyard, extent of body ∪ lands, package type, density level → excess = minimum offset between courtyard and body ∪ lands → pass excess ≥ Table 5.11 value → margin = excess − required → MITZ-074, -075.
- `CHECK-smd-land`: inputs JEDEC E_min/E_max, L_min, b_min/b_max, JT/JH/JS (Tables 5.8–5.10), F = 4, P = 6 → RSS_E = sqrt(E_tol² + F² + P²), RSS_b = sqrt(b_tol² + F² + P²); Z_max = E_min + 2·JT + RSS_E; G_min = (E_max − 2·L_min) − 2·JH − RSS_E; X_max = b_min + 2·JS + RSS_b → pass footprint outer land span ≤ Z_max, inner span ≥ G_min, land width ≤ X_max → MITZ-071, -072, -073.
- `CHECK-axial-pitch`: inputs body length LB, lead diameter DL, pad pitch LP, supported flag → R, LA from Table 5.12; LP_min = LB + 2·(R + LA) → pass LP ≥ LP_min AND LP on a 100 mil grid AND (LP − LB ≤ 1.0 in OR supported) → MITZ-076, -077.
- `CHECK-heavy-part`: inputs part mass (g), lead count, vibration flag, support flag → pass mass/lead ≤ 5.0 g OR supported → margin = 5.0 − mass/lead → MITZ-058.
- `CHECK-wave-via-to-pad`: inputs process ∈ {reflow then wave}, via-edge to SMD-pad-edge distance → pass distance ≥ 20 → MITZ-053.
- `CHECK-wave-side-parts`: inputs bottom-side parts, process = wave → pass no PLCC and no large tantalum on the wave side; SMD ICs oriented per travel direction with solder thieves → MITZ-051, -052.
- `CHECK-mask-expansion`: inputs pad size, mask opening, mask type, fab rule → expansion = (mask − pad)/2 per side → pass mask ≥ pad AND expansion within fab rule (book: LPI 0–5 mil total, 2 mil/side typical, 4–8 mil larger in diameter for THT; liquid screen 16–20 mil) → MITZ-045, -087, -169.
- `CHECK-paste`: inputs SMD pads, paste openings, pad area → pass every SMD pad has paste; paste ≈ pad − 1 mil per side; pads with split paste (large/exposed pads) have total paste ≤ 50 % of pad area → MITZ-088, -170, -225.
- `CHECK-fiducials`: inputs fiducial list → pass ≥ 2 global fiducials on the board perimeter, each with copper, soldermask opening (≈ +5 mil per side) and paste copy → MITZ-057, -224.
- `CHECK-placement-grid`: inputs component origins, board test method → pass origins on 100 / 50 / 25 / 20 mil (or 2.54 / 1.27 / 0.64 / 0.50 mm) grid; boards for bed-of-nails test on 0.100 in grid → MITZ-056, -190.
- `CHECK-orientation-consistency`: inputs rotation of polarized parts and pin-1 of ICs → pass all polarized parts share one orientation and all IC pin-1 marks point the same way (per board side) → MITZ-046.
- `CHECK-mounting-hole`: inputs screw size, hole diameter, keep-out diameter, plated flag → pass close ≤ hole ≤ loose (Tables D.1/D.2); keep-out ≥ max(washer, head, nut) diameter; NPTH has all-layer route keep-out; courtyard on both sides → MITZ-222, -223, -265, -266.
- `CHECK-panel-fit` (derived, conf medium): inputs board L × W (in), tooling margin m (0.375–1.5, default 1.0 in), board spacing s (0.1–0.5 in) → for each standard panel X × Y (Table 4.1): n = floor((X − 2·m + s)/(L + s))·floor((Y − 2·m + s)/(W + s)), also with the board rotated → choose the smallest panel with maximum boards → MITZ-031, -032.

Library, schematic, BOM and release package
- `CHECK-footprint-lint`: inputs footprint → pass ≥ 1 pad, ≥ 1 reference designator, outline on silkscreen and/or assembly layer, courtyard present, silkscreen line width ≥ 5 mil, no zero-width graphics, height property present, STEP origin/orientation aligned → MITZ-162, -174, -231, -238.
- `CHECK-symbol-footprint-pins`: inputs symbol pin numbers, footprint pad names → pass sets equal (no missing, no extra; NC pins uniquely named) → MITZ-155, -187.
- `CHECK-erc`: inputs netlist with pin electrical types → pass no output-to-output nets, no undriven input-only nets, power pins resolved by name, no two differently named globals merged unintentionally → MITZ-154, -186, -188.
- `CHECK-bom`: inputs BOM and part DB → pass every placed part has part number (found in DB), footprint and value; no TMP part numbers; DNI parts listed with quantity 0; mechanical hardware lines present; ≥ 1 approved source per part number → margin = count of failures → MITZ-184, -242, -245, -246, -247, -248.
- `CHECK-pick-and-place`: inputs placement file, layout part list → pass one row per placed part with refdes, part number, X, Y, rotation, side; row count equals placed-part count → MITZ-241.
- `CHECK-fab-package`: inputs output file list, layer list, hole list → pass one Gerber per copper layer, soldermask per side, paste per side with SMD pads, silkscreen per side with legend, outline film; plated and nonplated drill files with tool tables; drill chart on the fab drawing; route file if slots or panel routing; photoplot report error-free → margin = −(missing items) → MITZ-012, -226, -227, -233, -234, -235, -236, -237.


## 4. Verification procedures & plots

- **VP-01 Transmission-line ringing vs line length (digital)** — MITZ-120…123, 150–152; Figs. 6.25–6.29, 6.45–6.49 (p.146–152, 168–171). Circuit: VPULSE V1 = 0, V2 = 5 V, TD = 0, TR = TF = 2 ns, PW = 100 ns, PER = 200 ns → source resistor 10 Ω (driver output impedance) → ideal line Z0 = 50 Ω, TD = tPD × L → load 1 kΩ ∥ 15 pF. Sweep L = 30 in (TD 4.1 ns, k ≈ ½), 7.3 in (TD 1 ns, k = 2), 3.5 in (k = 4). Transient 0–200 ns, maximum step ≤ 1/1000 of run time (SPICE lossless `T` or `TXL/LTRA` element in ngspice). Plot V(source), V(drive), V(load) on one axis: x = time 0–200 ns, y = 0–9 V. Good: k ≥ 2 shows only small over/undershoots that die out while the edge is still rising (ring frequency higher, peaks never level off). Bad (k = ½): drive steps to 4.17 V, load peaks ≈ 7.92 V, then about 5.42 V at the source, 3.16 V and 4.67 V later, decaying slowly (settling time). Pass: max V_load ≤ receiver absolute maximum, no re-crossing of V_IH/V_IL after the first crossing, settled before the next sampling edge.
- **VP-02 Termination comparison** — MITZ-124…126; Figs. 6.30–6.31 (p.152–154). Same bench with (a) no termination, (b) series R = Z0 − R_S = 40 Ω at the driver, (c) R_S = Z0 = R_L (source + load matched). Plot V(drive) and V(load) vs time. Expected: (b) one flat half-amplitude step on V(drive) for one round trip (≈ 10–20 ns in the example) then a clean edge, load close to ideal; (c) no reflections but V(load) = ½·V(source). Pass: V(load) reaches V_IH with margin and no ringing; for clocks, confirm the half-amplitude hold is shorter than the clock high/low time.
- **VP-03 Termination value sweep** — MITZ-258 (p.547). Parametric sweep of the termination resistor 10–50 Ω in 2 Ω steps; plot overshoot, undershoot and settling time vs R; mark the passing window; select a real resistor whose nominal ± tolerance fits the window (example 22 Ω ±10 %).
- **VP-04 Analog line length** — MITZ-144 (p.163–164, 170–172). Specify the SPICE line by frequency F and normalized length NL = L/λ with λ = 1/(f·tPD) (example 66 MHz, εr = 4.2 → λ = 110.8 in). AC sweep of |V(load)/V(source)| vs frequency (log x) and a transient at f_max. Good: flat response, no standing-wave peaks; pass L < λ/15 (IPC-2251).
- **VP-05 Pre-layout SI (channel) simulation** — MITZ-254…256 (p.545–548). Models: IBIS driver/receiver (behavioral IBIS for pre-emphasis), S-parameter connectors/cables, RLGC traces from the stack-up (FR4 εr 4.0–4.5), vias as discrete elements. Stimulus: pulse low→high→low (custom pattern for eye). Plots: driver and receiver waveforms vs time; eye diagram at the receiver. Sweeps: trace length/delay, impedance (width, dielectric), via count. Extract: maximum length from setup-time margin, minimum length from hold-time margin, maximum and equal via count per bus → write into layout constraints.
- **VP-06 Post-layout verification of critical nets** — MITZ-257 (p.547, Figs. 12.7, 12.10). Extract each routed critical net (segment lengths, impedances, vias, terminations) and re-simulate. Plot all receivers of a multi-drop net on one axis (x = 0–30 ns, y = −1…6 V; the book's figure marks 100 mV, 2.0 V, 2.5 V, 3.0 V and 4.5 V levels — graph, conf medium). Fail: any receiver with a glitch or non-monotonic edge in the switching-threshold band (the book's example shows one receiver with a critical glitch).
- **VP-07 Model-free layout impedance/coupling screen** — MITZ-260 (p.551–553). Per-segment impedance map (color-coded) and per-segment coupling report for all high-speed nets. Pass: every segment within Z_target ± tolerance; flagged items (impedance discontinuities, excessive coupling, unequal via counts in a bus, differential pairs out of phase, crossings of split planes, proximity to other nets' vias/traces) fixed or dispositioned.
- **VP-08 Trace current capacity chart** — MITZ-141 (Fig. 6.38, p.161). Plot minimum trace width (y, mil) vs current (x, 0–1 A) from Eq. 6.17 for inner and outer layers at the design's copper weight and ΔT (book chart: 1 oz, ΔT = 10 °C, y range 0–35 mil); overlay each power net as a point (I_max, actual width). Pass: every point on or above its layer's curve; ambient + ΔT below Tg (FR4 125–135 °C).
- **VP-09 Rail collapse / ground bounce profile** — MITZ-097, -099 (Fig. 6.14, p.127). Transient PDN simulation (plane R and L plus IC switching current sources) with and without bypass capacitors; plot supply and return voltages vs distance from the power connector at the switching instant. Expected: without bypass capacitors a roughly linear drop (rise on return) worsening toward the switching gate; with bypass capacitors the rails are held except close to the switching gate. The book gives no numeric pass limit (digital switching noise "can be as much as 100 mV or more"); use the IC supply tolerance and analog noise budget.
- **VP-10 Subcircuit model validation (e.g., transformer)** — MITZ-160 (p.207–216). Build the equivalent circuit (winding inductances, winding DC resistances, K coupling), drive with VSIN into a dummy load, transient plot V(in) and V(out). Pass: amplitude ratio equals the turns ratio (example 1:2); optionally AC sweep for frequency response before exporting the .SUBCKT.
- **VP-11 Mixed-signal schematic simulation hygiene** — MITZ-158, -209, -252 (p.400–404, 528–531). Transient over about three signal cycles (5 ms for a 1 kHz VSIN), maximum step ≈ run/1000; AC sweep with VAC for frequency response; probes on analog nets (nets of unmodelled parts return "no simulation data"). Simulate sub-blocks through a test bench of the production schematic; delete the temporary "0" ground ties before netlisting.
- **VP-12 Bare-board electrical test and inspection** — MITZ-240 (p.501). Visual inspection of first-run boards; continuity and isolation tests, particularly each supply net to ground, before any component is loaded (IPC-2515A test data description; IPC-6011 acceptance; IPC-9252B listed in Appendix A). Pass: no supply-to-ground shorts, continuity per netlist.
- **VP-13 Artwork verification** — MITZ-233 (p.494–496). Import every Gerber into a blank board or Gerber viewer with its origin at 0,0 (or review in a CAM tool); overlay copper, soldermask, silkscreen, paste; negative planes appear as true negative images; review drill and route data in CAM. Pass: photoplot report error-free, expected file count present (see `CHECK-fab-package`), no silkscreen on pads/mask openings, plane clearances visible around non-connected holes.
- **VP-14 Mechanical fit (ECAD–MCAD)** — MITZ-183, -238 (p.272–276, 497–500). Export STEP/IDF/IDX/DXF with component heights; collision detection against the enclosure and hardware with a minimum spacing (example 0.1 mm); bend rigid-flex sections and re-run. Pass: zero collisions.
- **VP-15 Release gates (ERC/DRC/status)** — MITZ-016, -022, -185, -198 (p.38, 59, 297–300, 356–359). Schematic ERC report = 0 errors; layout DRC up to date and 0 errors (or waived with documentation, e.g., intentional net shorts); routing statistics 100 %, no unplaced parts, shapes updated. Pass required before artwork generation.

## 5. Pitfalls, failure modes, review checklist

Fabrication and padstacks
- [ ] Etched trace walls slope (undercut); width calculations use the bottom (mask-defined) width W, and thicker copper widens the spread (p.78–79, Fig. 4.3).
- [ ] Trace width tolerance for 1.5 oz copper is ±0.6 to ±4.0 mil — include it in impedance and ampacity margins (p.79).
- [ ] Padstack drill value is the FINISHED hole; plating can reduce the hole by up to 2 mil — check lead fit when lead and hole diameters are close (p.80).
- [ ] Fabricators round requested drill sizes to available bits; rounding erodes annular ring and can cause breakout (p.79, Fig. 4.2).
- [ ] Aspect ratio beyond the fab's capability gives incomplete plating (opens) and barrel cracking (p.80).
- [ ] Excess desmear/etchback causes partial delamination and internal shorts with misregistration and enlarges holes (p.80).
- [ ] A land larger than the plane antipad overlaps the plane: capacitive coupling changes trace impedance and adds crosstalk (p.108, Fig. 5.15).
- [ ] Antipads merged across closely spaced connector pins form slots in the return plane under crossing signals (p.108).
- [ ] Inner pads smaller than outer pads still need antipads larger than the largest pad (p.238).
- [ ] A via or padstack deliberately shorting two planes (clearance smaller than drill) is invisible in normal reviews — document it on the schematic and mark it on silkscreen (p.424).
- [ ] Auto-generated blind/buried via sets can include a via that joins two plane nets (e.g., VCC–GND) and scraps the board (p.412).
- [ ] Plane layers typed as routing layers let the autorouter cut slots into ground planes (p.453).
- [ ] Nonfunctional pads on routing layers must be retained (IPC-2221B); suppress only on plane layers (p.456–457).

Soldermask, paste, silkscreen
- [ ] Mask misregistration and swell can cover lands, especially on very small parts such as SOT23 — oversize openings, confirm who applies the oversize (p.80–81).
- [ ] Soldermask guidance differs across chapters (0–5 mil LPI oversize; 5 mil common; 2 mil per side; 4–8 mil larger) — use the fabricator's number (p.81, 108, 235, 239).
- [ ] Stock library footprints often lack paste layers — no paste means no stencil aperture (p.109, 434, 474).
- [ ] Large (exposed) pads with a full paste opening over-print; split the paste into windows covering ≤ 50 % of the pad (p.235).
- [ ] Zero-width lines and text (library rectangles) are silently dropped from Gerbers unless a default width is set (p.242, 251, 485–486).
- [ ] Silkscreen over pads/mask openings, under bodies or overlapping other legend is lost or illegible — run silkscreen clean-up (p.483–485).

Assembly and soldering
- [ ] Tombstoning from uneven pad heating; do not cluster thermally massive parts in one area (p.89).
- [ ] Reflow-then-wave: fan-out vias < 20 mil from SMD pads wick solder away from the joint (p.88).
- [ ] Wave soldering: last two pins of fine-pitch SMD rows bridge — add solder thieves; small parts shadowed by large parts get poor joints (p.87–88).
- [ ] PLCCs and large tantalum capacitors crack in the wave — keep them off the wave side (p.86, 90).
- [ ] Glue dot larger than a very small part oozes onto pads in wave assembly (p.86).
- [ ] Two-sided reflow with the same paste: heavy parts on the first-reflowed side fall off in the second pass (p.85).
- [ ] Parts heavier than 5.0 g per lead without mechanical support fail under vibration (p.90).
- [ ] Axial lead length (LP − LB) above 1 in without support (p.104).
- [ ] Mounting hardware (standoffs, washers, nuts) collides with parts or cuts traces when mounting holes lack place and route keep-outs; DRC cannot detect it for pad-less holes (p.473).

Signal integrity and grounding
- [ ] "Ground" treated as equipotential: shared (series) return paths couple noisy high-power returns into low-level analog (p.122–124).
- [ ] Analog circuitry placed between the power connector and noisy digital circuitry sees the digital return drops as noise (p.128).
- [ ] Signal crossing a split, void or moat in its reference plane: loop inductance up, ringing and EMI (p.380–381, 442–443).
- [ ] Layer change without a nearby return path forces return current through bypass capacitors and changes the line impedance (p.157).
- [ ] Overlapping analog and digital planes on adjacent layers couple noise capacitively (p.130).
- [ ] Unstitched copper islands and ground strips act as antennas (p.51, 390).
- [ ] Guard traces or rings not stitched to ground (or misapplied) can worsen crosstalk; benefit is debated (p.382).
- [ ] An attempted coplanar line built from guard pours with h ≤ d is really a surface microstrip (p.164).
- [ ] Unterminated electrically long lines: overshoot can exceed input ratings, radiate EMI and re-cross logic thresholds (p.146).
- [ ] Double termination halves the load voltage — may miss V_IH (p.152).
- [ ] Series termination's half-amplitude hold is a problem for high-speed clocks whose on/off time ≈ rise time (p.153).
- [ ] Judging high-speed by clock frequency instead of edge rate (rise time < 1 ns on a small board is already high-speed) (p.544).
- [ ] 90° corners are a minor effect compared with vias; do not trade vias for corner fixes (p.166–168).
- [ ] Using nominal copper and pre-lamination prepreg thickness in impedance calculations; signal layers sink into prepreg (p.76, 157).
- [ ] Ampacity at high ambient: FR4 Tg 125–135 °C shrinks the allowed ΔT (p.161).
- [ ] Pin swapping on a microcontroller changes the firmware pin map and is silently undone if the part is later replaced from the library (p.447–448).

Schematic, library and data
- [ ] Wire ends that only look connected (off-grid) break the netlist (p.24–25, 285).
- [ ] Invisible digital power pins connect by NAME only: a digital ground net not named GND leaves gates unpowered (p.366).
- [ ] Two differently named global symbols wired together become one net whose name is chosen alphabetically (p.368).
- [ ] Overbars on power symbols produce invalid netlist names (p.398).
- [ ] Several NC pins with the same name cause DRC errors — name them NC1, NC2, … (p.318).
- [ ] Symbol pin count ≠ footprint pad count (e.g., 7-pin symbol on 8-pin SOIC) prevents placement (p.317).
- [ ] Editing one unit of a multi-unit part with "update current" renames it and breaks netlisting — update all units (p.444–445).
- [ ] Heterogeneous multi-unit parts cannot be simulated; model pins must match symbol pin names and order exactly (p.217, 528).
- [ ] Simulation-only "0" ground ties left in the schematic merge separate ground nets in the layout netlist (p.400).
- [ ] Changing an internal part number breaks the part-database link (p.510).
- [ ] Reserved property names (Power, Voltage, Color) and duplicated property names corrupt part data (p.510–511).
- [ ] Temporary (TMP) part numbers left in a released BOM (p.520).

Book-internal inconsistencies to be aware of
- [ ] ALS rise time quoted as ≈ 2 ns (p.171), 1.9 ns (p.437) and 2.3/2.3 ns (Appendix C) — use the datasheet.
- [ ] tPD coefficient printed as 0.475 (Table 6.6) and 0.457 (Eq. 9.2); the book's worked numbers (137 ps/in) follow 0.457.
- [ ] ε0 printed as 8.89 × 10⁻¹² F/m (p.134).
- [ ] L0 printed as Z0²·C0/12 in Table 6.2 and Z0²·C0/1000 in the table note.
- [ ] Table 6.9 "safe" TD printed 0.24 ns for 3.5 in (0.48 ns is consistent with the other rows).
- [ ] Edge-coupled stripline Zdiff coefficient printed 0.347 (Table 6.4) and 0.374 (Table 6.7).
- [ ] Current-capacity Eq. 6.17 prints the ΔT exponent as 0.421; cross-check against IPC-2221B §6.2 before relying on it.
- [ ] Appendix C "rank" column conflicts with its own RT/FT values for several families; LVDS FT printed 0.03 ns.

## 6. Standards referenced

| Standard | Edition / year (as cited) | Clause / table cited | Governs | Book page(s) |
|---|---|---|---|---|
| IPC-2221B | Nov 2003 (Ch.5 refs); 2012 (Ch.6/9 refs) | Table 4-2 (plating thickness; hole-to-land); Tables 4-3/4-4/4-5 p.27 and Table 5-1 p.40 (aspect ratio); §5.2.7 p.43 (support > 5 g/lead); §5.4.2 & §8.1.2 (grids); §5.4–5.7 p.45–49 (fiducials); Fig. 7-1 p.68 (axial spacing, heat-sink spacing); p.73 & §8.1.2 (SMD spacing); Fig. 8-1 p.75 (orientation); §8.1.3 p.74 (wave); §8.1.9 p.76 (mounting); Fig. 8-4 p.76 (trace to mounting hardware); §6.2 p.56 (current capacity); Table 6-1 p.57 (conductor spacing; column B1 = plane clearance); §6.3.1 p.57 (plane-to-PTH clearance); §6.4.1–6.4.4 p.59–61, Fig. 6-4 (impedance); Tables 9-1/9-2, §9.1.1–9.1.2 p.95–96 (land, annular ring, fab allowance); §9.2 p.98 (PTH types); Table 4-1 p.23 & Table 6-2 p.60 (dielectric); §4.4 p.26 (copper); Tables 10-1/10-2 p.103 (plating); §1.6.2/§1.6.3 (class, producibility); Figs. 6-1…6-3 p.54 (power distribution); Fig. 1, Fig. 3-5 p.18, Fig. 5-1 p.41 (panel sizes); §3.3 p.9 (diagrams); §3.6 p.10 (testing); §7 p.65 (thermal); 3.9 mil min width/space; LPI mask oversize 0–5 mil; keep nonfunctional pads on routing layers | Generic printed-board design (successor of MIL-STD-275) | 70, 74, 79–81, 90–96, 100, 106–107, 161–165, 457, 557, 577–589 |
| IPC-2222A (once cited "IPC-2222B") | Dec 2010 | Table 9-5 p.25 (hole-to-lead); pp.21–22 (thermal-relief spoke width W = 0.6·P/n); Fig. 9-1 p.22 & §9.1.3 (plane clearance 10 mil); §9.1.4 p.23 (nonfunctional lands); §9.2.1 p.25 (unsupported holes); §9.2.2.3 p.25 (filled/plugged holes); Table 9-6 p.26 (aspect ratio); §5.2.1 (borders); §1.6 (assembly types) | Sectional design standard, rigid organic boards | 105–107, 259–260, 557, 580–582 |
| IPC-7351B | June 2010 | §1.3 (classes); §1.3.1 (producibility); §1.4 (density levels A/B/C); §1.5 p.3 (PTH types); pp.10–21 (JT/JH/JS fillets); §3.1 pp.7–12 (SMD land design); Tables 3-2…3-22 (courtyard excess, spacing); Tables 3.5–3.8, Fig. 3.15 (discrete SMD spacing); Table 3-23 p.24 (naming convention); Tables 3-25/3-26, Fig. 3-20 p.38 (fab allowances); §3.4 p.31 (placement); §3.4.6 p.35 (vias); §3.4.7 p.37 (annular ring); §7.4 Fig. 7-1 p.50 (assembly); §8.0–16.0 pp.54–86 (package types); 20 mil via-to-pad; metric grids | SMT land patterns (superseded IPC-SM-780/2 as printed) | 71–72, 88, 90, 94–102, 249, 271, 558, 577–582 |
| IPC-CM-770E | Jan 2004 | §1.2.1 (classes); §1.2.2 (producibility, assembly subclasses); §1.2.3 (fabrication types); §1.2.4; p.34 (soldering methods); §6.2.2.1/§6.2.2.3/§6.2.2.4 p.35 (wave, reflow); §6.3, §7.1 p.37 (assembly); §7.2 p.35 (DRC); §8.1 p.44 (placement); §8.1.2 (wave); §8.4 p.46 (fiducials); §8.6 p.47 (vias); Tables 8-1/8-2 p.50 (fab allowances); §11.1.8 p.67 (axial lead forming) | Component mounting guidelines | 71–72, 80, 86, 103, 558, 577–587 |
| IPC-D-330 | Design Guide Manual 1992 (superseded by IPC-2221/2222/7351) | §1.1.42.6 (classes/producibility); §2 Table 2-4 (min PTH vs thickness and class); §2 Table 2-6 p.9 (panel usage); §2 Table 2-16 (copper); Table 6-30 (aspect ratio) | Legacy design guide | 71, 75, 78–80, 172 |
| ANSI/IPC-D-322 | — | panel table; tooling area 0.375–1.5 in | Standard panel sizes | 74–75, 81, 558, 580 |
| IPC-4101E | — | Table 3-7 (core thickness); Table 1-2 p.3 (copper) | Base materials, rigid and multilayer | 76–78, 557, 579 |
| IPC-2141A | 2004 | §4.1–4.7 pp.15–27 (impedance); §3.4.7 p.9 (propagation delay) | Controlled-impedance boards and high-speed logic | 135–142, 172, 557, 589–590 |
| IPC-2251 | 2003 | pp.32–36 (TL equations, restrictions); L < λ/15; Table 5-4 p.29 (logic rise/fall times); §5.4 p.30; §5.5–5.5.5.4 pp.31–36; §5.6.2 p.36 (reflections) | Packaging of high-speed circuits (design guide) | 135–164, 172, 573–574, 589–590 |
| IPC-2581B | — | through-hole padstacks always plated; combined output format "IPC2581" (named only) | Product-data exchange format | 15, 232 |
| IPC-2515A | 2000 | — | Bare-board electrical test data description (BDTST) | 501, 505, 557 |
| IPC-6011 | 1996 | — | Generic performance specification for printed boards (inspection/acceptance) | 501, 505 |
| IPC-9252B, IPC-D-356B, IPC-D-350D, IPC-A-600J, IPC-A-610G, IPC-HDBK-610 | — | listed only | Unpopulated-board electrical test; bare-substrate test data format; digital board description; board and assembly acceptability | 558 |
| IPC J-STD-001G | — | — | Soldering requirements | 587 |
| IPC-SM-780 | July 1998 | §6.7.1.1 p.64 (fan-outs); §6.7.2 p.66 (land patterns); §8.1 p.84 (soldering); §8.4.2 p.94 (lead bend); §8.6.1.5 p.103 (lead-to-hole) | Component packaging and interconnection, SMT | 98, 109, 558, 578–587 |
| IPC-AJ-820A | — | §1.3.2 Fig. 1-1 (assembly types); §2.0 pp.2-2…2-8 (general design); §2.5.1.4, §2.5.3.1 (lead bend); §2.5.2 p.2-11 (lead-to-hole); Fig. 2-12 (trace to mounting hardware) | Assembly and joining handbook | 577–588 |
| IPC-2223D, IPC-2224, IPC-2225, IPC-2226A, IPC/JPCA-2315, IPC/JPCA-6801, IPC-1902/IEC 60097, IPC-2615, IPC/WHMA-A-620C | — | listed (IPC-1902 grid resolution; IPC-2615 dimensions and tolerances) | Flex/rigid-flex; PC cards; MCM-L; HDI; HDI/microvias; HDI terms; grid systems; board dimensions/tolerances; cable and harness | 557–558, 577, 580, 587 |
| MIL-STD-275(E) | — | Table 4-3 (plating); width tolerance ±4.0…±0.6 mil (1.5 oz) | Printed wiring for electronic equipment (superseded by IPC-2221B) | 70, 76, 79, 81, 558 |
| MIL-HDBK-1861A, MIL-HDBK-198(A), MIL-HDBK-199(A), MIL-HDBK-5961A, MIL-STD-1276G | — | — | Assemblies/boards; capacitor and resistor selection; standard semiconductors; component leads | 81, 558 |
| IEEE Std 315-1975 / ANSI Y32.2-1975 | 1975 | ground symbols (Table 6.1) | Graphic symbols for electrical and electronics diagrams | 70, 122–123, 557, 583 |
| IEEE-1445-1998 | 1998 | — | Digital test interchange format | 70, 81 |
| ANSI/ASME B94.11M | 1993 | — | Twist-drill (standard drill bit) sizes | 79, 81, 557, 580 |
| ASME B18.2.8-1999; B18.6.3-2003; B18.6.7M-2000; B18.2.4.1M-2002; B18.2.4.2M-2005; B18.12-2001; B18.13-1996; B18.13.1M-1999; B18.21.1-1999; B18.21.2M-1999; B18.22.1-1981; B18.22M-1981; B1-10M; ASA B18.11-1961 (printed "ASA 618.11-1961"); Y14.5M | as listed | Appendix D tables | Clearance holes, machine screws, nuts, washers, miniature threads, dimensioning and tolerancing | 81, 557, 575–576, 580 |
| 47 CFR 15 | — | — | FCC rules on radio-frequency devices incl. unintentional radiators | 81, 115 |
| JEDEC JEP95 (Publication No. 95) | — | MS-012 (SOIC, Fig. 5.6); outline tables B.2–B.10 | Package outlines for footprint design | 69, 96–97, 558–572 |
| JEDEC Standard 51 | — | — | Package thermal characterization (reference list) | 588 |
| EIAJ RC-2134B; EIAJ SC-59/SC-61B/SC-74A/SC-76; IEC 60115-B & JIS C 5201-B (as printed); EIC 10H01 | — | Appendix B | Tantalum case codes; small-outline packages; chip resistors; MELF | 563–566 |

Not covered by this book (checked by full-text search): UL 94, UL 796, IPC-2152, IPC-6012 (classes/acceptance), IPC-D-325 (fabrication documentation), ODB++ (the "ODB" hits are ODBC), CTE; IPC-2581 and IPC-D-356 are named only.

## 7. Process / lifecycle guidance

Tool-agnostic flow distilled from the 7-step flow (p.17, 40) and the expanded outline (p.279–281), with Ch.4–6 and Ch.10–12 activities placed where they belong.

| # | Stage | Activities | Deliverable | Exit criterion | Source |
|---|---|---|---|---|---|
| 1 | Concept and preparation | Initial drawings; simulate critical sections; collect datasheets; inventory packages and footprints; find or build symbols and SPICE models | Concept schematic; parts/footprint spreadsheet (ref, value, package, footprint, datasheet) | Every part has a symbol, footprint source and datasheet | p.279, 281–283, Table 9.1 |
| 2 | Classification | Elect IPC performance class (1/2/3/3A), producibility level (A/B/C), fabrication type (1–6), assembly subclass (A/B/C/X/Y/Z), land-pattern density level (A/B/C) | Class/level record (goes on the fab drawing) | Elections recorded; they drive annular ring, aspect ratio, hole and spacing limits | p.71–72; MITZ-024…028 |
| 3 | Schematic capture | Place and wire; global power/ground naming; multi-unit parts; annotation; rooms (placement groups); cache clean-up; buses and off-page connectors | Schematic | ERC = 0 errors; no off-grid wires; NC markers on unused pins | p.279, 284–300, 366–370; MITZ-154…159, 185…189 |
| 4 | Simulation (pre-layout) | SPICE of analog blocks (test bench copies of the production schematic); transmission-line and channel SI for fast nets; derive length/via/termination constraints | Simulation reports; constraint list | Assertions pass at the stated conditions; constraints captured | Ch.6, 7, 9, 11, 12; VP-01…VP-11 |
| 5 | BOM and footprints | BOM listing footprint field; assign or create IPC-7351B footprints and padstacks (Eqs. 5.1–5.5, Tables 5.8–5.15); part numbers from the part database | BOM with footprints; library | No blank footprint; symbol pins = footprint pads; part status green | p.95–109, 223–276, 292–294, 507–541 |
| 6 | Netlist to layout | Generate netlist; review netlist error report | Board database | No unexplained netlist warnings/errors | p.46, 300–301 |
| 7 | Board requirements | Board dimensions and mounting holes; height restrictions and assembly method; noise and shielding; SMT/THT mix; trace width/spacing by current, voltage, impedance; vias and fan-outs (size, tenting); number of plane and routing layers | Board constraint table (e.g., Table 9.5) | Reviewed before placement; within the fabricator's capability | p.280, 346–348, 370–371; MITZ-195…199 |
| 8 | Physical setup and placement | Board outline and edge keep-ins; mounting holes (keep-outs on both sides); dimensions; placement by function and noise zoning (noisy near connector); DRC for footprint/placement problems | Placed board | DFM spacing checks pass (Tables 5.1–5.7, courtyards); polarity/pin-1 orientation consistent | p.89–95, 153–155, 280, 303–333 |
| 9 | Stack-up and planes | Define stack-up with the fabricator (even layer count, every signal layer next to a plane); assign plane nets; split/moated planes; thermal-relief parameters; via types per net | Stack-up; plane artwork; via assignment | Stack-up approved by fab; plane connectivity verified (thermals on connected pins, clearances elsewhere) | p.155–160, 280, 333–346, 370–377 |
| 10 | Pre-route | Power/ground fan-outs; heat spreaders; critical nets (transmission lines, clocks with moats, differential pairs) routed manually and fixed | Pre-routed board | DRC = 0; critical nets meet Z0 and length rules | p.280, 349–353, 424–443 |
| 11 | Route | Autoroute or manual routing of the remaining nets; pin/gate swaps back-annotated | Routed board | 100 % routed; DRC = 0 | p.280, 353–356, 443–451 |
| 12 | Finalize | Post-route inspection (acute angles, long parallel runs, via locations, traces over voids, silkscreen); guard traces and stitching; island removal; gloss/clean-up; final DRC; back-annotation; post-layout SI | Final board; back-annotated schematic | DRC = 0; segments over voids = 0; islands = 0; schematic in sync | p.281, 356–362, 380–390; VP-06, VP-07 |
| 13 | Manufacturing data | Fiducials; board legend (P/N, revision); photoplot outline; silkscreen clean-up; Gerber RS-274X films; drill chart; NC drill (plated/nonplated, tool tables); NC route if needed; artwork verification; ECAD–MCAD export; pick-and-place file with part numbers; variant BOMs | Fabrication and assembly package | `CHECK-fab-package` passes; photoplot report clean; MCAD fit clean | p.469–505; VP-13, VP-14 |
| 14 | Fabrication | Fabricator capability check and CAM review/quote | Quote and DFM feedback | No open fab exceptions | p.500 |
| 15 | Bare-board acceptance | First-article inspection; continuity and isolation (supplies to ground) before assembly | Bare-board test record | Pass (IPC-2515A / IPC-6011 criteria) | p.501; VP-12 |
| 16 | Assembly | Stencil from paste data; placement program from the P&P file; reflow/wave sequence per mix of technologies | Assembled boards | Joints to the chosen class | p.84–89, 474, 501–505 |
| 17 | Reliability loop | If field or test failures occur within operational limits: failure analysis, then redesign | FA report; design change | Root cause addressed | p.68 |

Yield framing for all stages (p.68): manufacturable (within standard fabrication allowances and assemblable) + performs (mechanical fit, environment, electrical, EMI/EMC) + reliable over life.

## 8. Coverage log

Source file: `refs-text/Kraig_Mitzner_Bob_Doe_Alexander_Akulin_Anton_Suponin_Dirk_Mu.txt`, 11391 lines, read in order with the Read tool:

| Lines | Content | Notes |
|---|---|---|
| 1–800 | Front matter, introduction (chapter summaries), Ch.1, Ch.2, start of Ch.3 | — |
| 801–1500 | Ch.3, Ch.4 to Table 4.3 | first attempt at 950 lines exceeded the token cap; re-read at 700 |
| 1500–2099 | Ch.4 end, Ch.5 to Table 5.3 | — |
| 2100–3029 | Ch.5 (Tables 5.4–5.15, Eqs. 5.1–5.5) | read as 2100–2659 and 2660–3029 |
| 3023–5961 | Ch.6 | five chunks of ≤ 700 lines |
| 5962–6481 | Ch.7 | — |
| 6482–7521 | Ch.8, start of Ch.9 | two chunks |
| 7522–8521 | Ch.9 examples 1–3 | 500-line reads exceeded the token cap; re-read as four 250-line chunks |
| 8522–9011 | Ch.9 example 4, positive planes, templates | — |
| 9006–10205 | Ch.10, Ch.11, Ch.12, Appendix A, start of Appendix B | four 300-line chunks |
| 10205–11235 | Appendix B, C, D, E | three chunks |
| 11236–11391 | Index | scanned only (skipped per brief) |

Work was interrupted once (API rate limit after Ch.9, last saved rule MITZ-221) and again by a session restart; each time the output file was re-checked and work continued from the next unwritten part. Nothing was lost.

Output totals: 266 design rules (MITZ-001 … MITZ-266), 57 mechanizable checks, 15 verification procedures, ~45 reproduced tables/equation sets.

Skipped deliberately: OrCAD/Allegro click paths, dialog-box descriptions, screenshots, toolbar tours, license notes and file-extension trivia (Ch.2, 3, 7–12), except where they encode a tool-agnostic check (kept, e.g., zero-width silkscreen, suppression of unconnected pads, negative-plane polarity, ECO/back-annotation hygiene). Worked examples with numbers were extracted.

Extraction limitations:
- Equations arrive with broken glyphs (radicals as ligature runs, "5" for "=", "1" for "+", "2" or "À" for "−", "3" for "×", "ð6:17Þ" equation tags). All formulas were reconstructed and checked against the book's own worked numbers where possible (Z0 50 Ω at 17.5 mil, 137 ps/in, 6 mil ≈ 300/600 mA, 100 mA → 1.3/0.5 mil, 4.17/7.92 V bounce, Table 9.10). Rows whose reconstruction stays ambiguous are marked medium/low: MITZ-071 (radical extent of Eq. 5.1), MITZ-113 (asymmetric stripline), MITZ-114 (broadside-coupled Zdiff exponent), MITZ-117 (0.347 vs 0.374).
- Negative fillet values in Tables 5.8–5.10 were printed with a leading "2"; decoded against the mm column.
- Figures are absent from the text; graph-dependent content (Fig. 6.38 current chart, Figs. 6.26–6.31 ringing plots, Fig. 12.10 glitch plot) is described from captions and the numbers in the prose.
- Appendix B/C/D tables were flattened in extraction and re-assembled by column order; Appendix C ranks and Appendix B.6 row alignment are flagged "as printed".
- Book-internal inconsistencies are listed at the end of section 5 rather than silently corrected.
- Topics in the coordinator's focus list that the book does not contain: UL 94/796, IPC-2152, IPC-6012 classes and acceptance, IPC-D-325 fabrication-drawing notes, ODB++, IPC-2581 content (named only), IPC-D-356 netlist test (listed only), stack-up drawing content, CTE/Tg beyond one Tg sentence, copper balance, panel breakaway/V-score dimensions, tooling-hole sizes.
