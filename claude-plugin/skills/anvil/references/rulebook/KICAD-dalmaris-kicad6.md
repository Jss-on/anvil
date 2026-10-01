# KiCad 6 Like A Pro: Fundamentals and Projects — Anvil rulebook

## 0. Citation

P. Dalmaris, *KiCad 6 Like A Pro: Fundamentals and Projects — Getting started with the world's best open-source PCB tool*, 3rd ed. (Parts 1–10), Susteren, NL: Elektor International Media B.V., 2022. ISBN 978-3-89576-496-7 (print), 978-3-89576-497-4 (ebook). 548 pp. All procedures tested on KiCad 5.99 nightlies / KiCad 6.0 RC1 (p.15).

Companion volume (NOT part of this file): *KiCad 6 Like A Pro: Projects, Tips, and Recipes* (Parts 11–13), ISBN 978-3-89576-498-1. This book repeatedly defers details to that "Recipes" volume: Track Width calculator, differential pairs, length tuning, BOM export, autorouter, project templates, coordinate origins, image converter/logo footprints, bus wiring, Git. Those topics are therefore only touched here.

Chapters covered by THIS extraction: Front matter; Part 1 (PCB anatomy, design process, fabrication); Part 2 (project manager, apps, paths/libraries, KiCad 5→6 changes); Part 3 (LED-torch schematic project); Part 4 (LED-torch layout, Gerbers, ordering); Part 5 (design principles & PCB terms); Part 6 (schematic & layout workflows); Part 7 (symbols & Eeschema how-to); Part 8 (footprints & Pcbnew how-to, board setup, DRC, Gerbers, 3D); Part 9 (breadboard power-supply project incl. defect fix); Part 10 (4×8×8 LED-matrix project incl. 3D and bug fix). Not read: Index (lines 3575–4831 of the text file) and back-cover blurb — no engineering content.

KiCad 6 → 9/10 mapping notes for Anvil: "Eeschema" = Schematic Editor, "Pcbnew" = PCB Editor, "Cvpcb" = Assign Footprints, "Gerbview" = Gerber Viewer. Env-vars carry the major version (`KICAD6_*` → `KICAD9_*`). Layer names quoted are KiCad 6 (`F.Silkscreen`, `F.Courtyard` a.k.a. `F.CrtYd`, `F.Fab`, `Edge.Cuts`, `User.1`, `User.2`, `User.Drawings`). Legacy `.lib`/`.dcm` symbol files import in 6; native is `.kicad_sym`; footprints are `.kicad_mod` inside `.pretty` folders. Custom DRC rules use the `(version 1)` rule language (still valid in 9). The Python API, Action Plugins and Python shell are described as work-in-progress/undocumented in KiCad 6 (p.210, p.307, p.324); the book gives NO scripting, plugin, or CLI content (`kicad-cli` did not exist in 6). "Board classes"/"Via size"/"Track width"/"Electrical spacing" calculators exist in the Calculator Tools app (p.57) but are not detailed here.

## 1. Design rules

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| KICAD-001 | materials | Standard rigid PCB is fiberglass (FR4) with a nominal thickness of 1.6 mm. | t_board = 1.6 mm (typical) | board thickness | Default for hobby/online-fab boards unless otherwise ordered | inspect | p.26, Fig.1.1.7; p.159; p.455 | high |
| KICAD-002 | cost | Board area is the dominant cost driver at online fabs; minimize board area (and bounding box — cut-outs do not reduce cost). | typical small 2-layer order: ~$10 for a 2 sq-in board, 3 copies ⇒ ~$5 per sq in; "~$15 for several copies" | board W, H | Online fabs (PCBWay, NextPCB, OSH Park cited); pricing "consistent in the industry"; cost follows all-inclusive W×H even with substrate removed | calc | p.33, p.466 | high |
| KICAD-003 | process | Plan lead time: online manufacture + shipping takes weeks; expedite options cost a premium. | lead time ≈ 2 weeks+ ("a couple of weeks") | — | Online fab ordering | review | p.33, p.155–156, p.193, p.539 | high |
| KICAD-004 | fab | Deliverable to fab = Gerber set: one Gerber (text) file per manufacturable layer plus drill file(s), zipped. Gerber standard owned by Ucamco. | 1 file/layer + drill | layer list | Standard fab intake; some fabs (OSH Park) also accept native `.kicad_pcb` | inspect | p.33–34, p.148–151, p.193 | high |
| KICAD-005 | process | KiCad project = flat directory with `.kicad_pro` (project), `.kicad_sch` (one per schematic sheet), `.kicad_pcb` (layout); generated files `fp-lib-table`, `fp-info-cache`, `_autosave-*.kicad_sch`, `backups/`, Gerber output dir. All files are S-expression text (diffable/version-controllable). | — | — | KiCad 6 file format | inspect | p.37, p.62, p.71, p.77 | high |
| KICAD-006 | process | Library path environment variables: `KICAD6_3DMODEL_DIR`, `KICAD6_3RD_PARTY`, `KICAD6_FOOTPRINT_DIR`, `KICAD6_SYMBOL_DIR`, `KICAD6_TEMPLATE_DIR`, `KICAD_USER_TEMPLATE_DIR`. Do not change paths mid-project. | — | — | KiCad 6 (prefix changes with major version) | inspect | p.59, p.80 | high |
| KICAD-007 | process | Libraries are registered in Global or Project-Specific symbol/footprint library tables; keep project-specific libraries inside the project folder; a folder of `.kicad_mod` files is imported as one library. | — | — | Symbol/footprint library managers | inspect | p.60–61, p.234–236, p.338–339, p.343–347 | high |
| KICAD-008 | process | A symbol and its associated footprint share the same reference designator and the same number of pins/pads. | pins(symbol) == pads(footprint) | symbol pins, footprint pads | KiCad does NOT enforce this; ERC will not flag a mismatched association | inspect | p.41, p.252 | high |
| KICAD-009 | process | Schematic grid: snap-to-grid always on; 2.54 mm for placement and 1.27 mm for finer alignment (author's Alt-1/Alt-2 fast-switch pair); smaller grids for busy schematics; default minimum grid spacing 10 px. | grid ∈ {2.54, 1.27} mm | — | Eeschema | inspect | p.84–86, p.92, p.174, p.195 | high |
| KICAD-010 | process | Schematic wires/buses horizontal or vertical only ("Constrain buses and wires to H and V" on); never free-angle wires. | wire angle ∈ {0°, 90°} | — | Eeschema Editing Options | inspect | p.85, p.197, p.401 | high |
| KICAD-011 | process | Fill the Page Settings (title block) in both editors before drawing: date (issue date), revision, title, comments describing the PCB, sheet size. | fields non-empty | date, rev, title, comment | Schematic step 1 and Layout step 1 | inspect | p.87, p.112, p.175, p.297, p.401 | high |
| KICAD-012 | process | Every symbol carries a unique reference designator from the automatic annotator (default settings); `?` = not annotated. Power symbols and PWR_FLAGs added later must be re-annotated (ERC reports "not fully annotated"). | no `?` designators; designators unique | — | Schematic step 3; re-run after adding power symbols | inspect | p.93–94, p.177, p.206, p.413, p.484 | high |
| KICAD-013 | process | Every symbol must have a footprint assigned before "Update PCB from Schematic" (it errors on unassigned symbols); reference format `Library:Footprint`. | footprint field non-empty ∀ symbols (power symbols excepted) | — | Power symbols have no footprint by design | inspect | p.95–97, p.253, p.409 | high |
| KICAD-014 | process | Check symbol↔footprint compatibility manually: pin count, pin roles, pin layout/pitch, package shape versus the datasheet — KiCad accepts any association (e.g. resistor symbol ↔ switch footprint) without error. Use Assign Footprints filters (text, pin count `#`, library `L`) and "View selected footprint". | — | datasheet | Schematic step 3 | review | p.252, p.256–257 | high |
| KICAD-015 | process | Name important nets with labels: ground, supply rails (GND, 5V, 3.3V, 12V, Vcc), signal nets, antenna nets, data/address/clock/chip-select buses; auto-generated names are acceptable for the rest. | — | — | Enables net-class width control in layout | inspect | p.100–101, p.178, p.217, p.262, p.415, p.482–483 | high |
| KICAD-016 | process | A net label is attached only when the small box at its lower-left corner disappears; prefer labels directly on pins to long wires; a no-connect flag must sit exactly on the pin end. | — | — | Eeschema | inspect | p.259–262, p.485 | high |
| KICAD-017 | process | Run ERC before leaving the schematic; target 0 errors and 0 warnings; fix "Pin not connected" by wiring or by a no-connect flag on deliberately open pins; "symbol modified in library" warnings may be excluded. | ERC errors = 0 | ERC report | Schematic step 6 | inspect | p.102–103, p.179, p.215, p.276–278, p.414, p.485–487 | high |
| KICAD-018 | process | Every power-input pin (e.g. MCU VCC) must connect to a compatible power symbol/net; add a PWR_FLAG to GND and to every supply net that is not driven by a power-output pin; the GND power symbol auto-names the net "GND". | — | pin electrical types | ERC uses pin electrical type | inspect | p.207, p.214, p.247–248, p.411, p.480 | high |
| KICAD-019 | process | ERC Violation Severity: each violation is Error / Warning / Ignore; default "Pin not connected" = Error. Keep defaults unless project-specific. | — | — | Schematic Setup > Electrical Rules > Violation Severity | inspect | p.277–278 | high |
| KICAD-020 | process | ERC Pin Conflicts Map defaults: output↔output = error; tri-state↔output = warning (check); passive↔passive = allowed; passive↔input = allowed. Making passive↔input an error produced 115 false errors. | — | pin types | Schematic Setup > Pin Conflicts Map | inspect | p.279–281 | high |
| KICAD-021 | process | Annotate the schematic like source code: line boxes around functional groups, text naming each group, notes for non-obvious choices (e.g. flipped/mirrored symbols); optional custom field "Purpose" (Field Name Templates, visible) per symbol. | — | — | Schematic step 7 | inspect | p.104–105, p.180, p.418–420, p.489 | low |
| KICAD-022 | process | Use a consistent symbol style (IEC/European vs IEEE/US `*_US`); never mix in one schematic. | — | — | US variants suffixed `US` | inspect | p.159 | high |
| KICAD-023 | process | Custom symbol layout: VCC pin on top edge, GND on bottom, inputs left, outputs right; group pins by kind; pin number over the pin line, name inside the body; body filled rectangle. | — | — | Symbol Editor | inspect | p.242, p.247–249 | high |
| KICAD-024 | process | Pin electrical type (power input, input, output, bidirectional, passive, tri-state) is essential for ERC; graphic style is cosmetic. Pin numbers from the datasheet. | — | datasheet | Symbol Editor | inspect | p.248 | high |
| KICAD-025 | process | Custom symbol properties: default footprint, datasheet URL, description, keywords; tag self-made symbols with a suffix (author: `_PD`) in a separate `.kicad_sym` library. | — | — | Symbol Editor | inspect | p.245–246, p.250 | high |
| KICAD-026 | process | Symbol/footprint/3D sourcing order: (1) official KiCad library repos, (2) SnapEDA, (3) Octopart, (4) Ultralibrarian; also install Digi-Key (`dk_` prefix), SparkFun, Freetronics libraries. Rename downloaded `.lib` to the part name. | — | — | Ultralibrarian: symbol+footprint, no 3D for KiCad; SnapEDA ZIP: `.lib` + `.step` + `.kicad_mod` | review | p.230–241, p.341–343 | high |
| KICAD-027 | process | Downloaded symbols may have overlapping (stacked) pins; separate them in the Symbol Editor, otherwise ERC reports "pin not connected" on the hidden pin; each separated pin needs its own no-connect flag. | — | — | SnapEDA button/barrel-jack symbols cited | inspect | p.478–479, p.481, p.486 | high |
| KICAD-028 | process | Hierarchical sheets: each sheet is its own `.kicad_sch`; every sheet has exactly one parent except root; connect sheets with hierarchical labels + imported sheet pins (preferred) — use global labels sparingly. A global label creates a net named after the label. | — | — | Multi-sheet schematics | inspect | p.268–275 | high |
| KICAD-029 | process | Repeated-item auto-placement requires labels ending in a number and element pitch equal to the configured vertical pitch; multi-pin symbols use the 2.54 pitch convention (text prints "2.54-inch" — evidently 2.54 mm / 0.1 in). | pitch = 2.54 mm (0.1 in) | — | Eeschema Editing Options > Repeated Items | inspect | p.223 | medium |
| KICAD-030 | process | Bulk edits: Change Symbols by reference prefix / value / library id (e.g. `Device:R`); Edit Text & Graphics Properties; Find/Replace across all sheets. | — | — | Eeschema | inspect | p.281–287 | high |
| KICAD-031 | process | Layout grid strategy: 1.27 mm for outline, 0.635 mm for footprint placement, 0.508 or 0.254 mm for routing; custom grid (e.g. 0.5 mm) for exact metric dimensions; 0.0508 mm or 0.01 mm for precision placement/measurement. | grids ∈ {1.27, 0.635, 0.508, 0.254, 0.127, 0.0508, 0.01, custom} mm | board size, pad density | 50 mm side = 39×1.27 = 49.53 mm or 40×1.27 = 50.8 mm on a 1.27 grid | calc | p.181–182, p.427, p.496 | high |
| KICAD-032 | process | Rough outline first on a User layer (`User.1`/`User.2`, excluded from Gerbers) sized from constraints, verify the largest footprints fit, then trace the real outline on `Edge.Cuts`; refine after placement. | — | constraints | Layout step 2 | inspect | p.113–116, p.429, p.496–499 | high |
| KICAD-033 | mechanical | Define outline, mounting holes and cutouts BEFORE placing components so they match enclosure/mating hardware; relocating later is costly. | — | enclosure dims | Layout step 2 | review | p.184–185 | high |
| KICAD-034 | mechanical | Outline sizing questions: overall size (cost), user-control locations, largest component, enclosure attachment (screw holes/bosses/rails). Example LED torch ≈ 65 mm × 25 mm, 1–2 screw holes; rough rectangle drawn 66.29 mm × 26.41 mm. | — | — | Layout step 2 | review | p.113–114 | high |
| KICAD-035 | mechanical | Board outline must be one closed contour: remove redundant/overlapping `Edge.Cuts` segments (they break the 3D viewer and confuse the fab); join segments exactly (snap indicator circle); edge line must not touch any footprint courtyard. | contour closed; no stray segments; Edge.Cuts ∩ courtyard = ∅ | Edge.Cuts geometry | Magnetic snap "always" | inspect | p.129–133, p.322–323, p.439 | high |
| KICAD-036 | mechanical | Rounded corners: LED torch used arc centre at dx = dy = 1.27 mm from the corner (grid 0.254 mm); PSU board used radius 1.016 mm; then trim edge lines to the arc ends. | corner radius ∈ {1.27, 1.016} mm (author's choices) | — | Author's boards | inspect | p.134–136, p.439–440 | high |
| KICAD-037 | process | Mounting holes / cutouts: draw circles/polygons on `Edge.Cuts`, or place `MountingHole:MountingHole_2.5mm` footprints tied to `MountingHole` symbols (Mechanical library) so DRC has no "extra footprint" warnings; place holes symmetric about the board axis and aligned to ease enclosure design. | — | screw size | Layout step 2/3 | inspect | p.114, p.185–186, p.466, p.490–491, p.506 | high |
| KICAD-038 | stackup | Default hobby board = 2 copper layers; fabs price a 1-layer design the same as 2-layer. 4 layers for high-speed/RF: dedicated GND and power planes + 2 signal layers. Pcbnew supports 2–32 copper layers. | N_cu ∈ [2,32]; default 2 | complexity, RF | Board Setup > Physical Stackup | review | p.183, p.324–325 | high |
| KICAD-039 | stackup | Non-default stackup entries (dielectric material/thickness, silkscreen material, finish, castellated pads, plated board edge) must be confirmed with the fab before ordering — KiCad settings do not bind the manufacturer. | — | — | Board Setup > Physical Stackup / Board Finish | review | p.326–328 | high |
| KICAD-040 | stackup | Copper layer roles per layer: signal, power plane, mixed, jumper (author sets F.Cu and B.Cu = mixed on a 2-layer board carrying signal and power). | — | — | Board Setup > Board Editor Layers | inspect | p.327, p.493 | high |
| KICAD-041 | dfm | Solder mask / solder paste clearance (expansion) defaults of 0 are safe; only change with values from the fab. | mask expansion = 0; paste clearance = 0 (default) | fab spec | Board Setup > Solder Mask/Paste | inspect | p.328 | high |
| KICAD-042 | fab | Before layout, set Design Rules ≥ the fab's published minimums; for several fabs use the largest of their minimums; check units (in / mm / mil). | rule_i ≥ max_fabs(min_i) | fab capability tables | Board Setup > Constraints and Net Classes | calc | p.184 | high |
| KICAD-043 | fab | OSH Park (KiCad design-rules page, accessed 2018-11-19): minimum trace width 0.006 in; minimum via diameter 0.027 in. | w_min = 6 mil (0.1524 mm); via_dia_min = 27 mil (0.6858 mm) | — | OSH Park 2-layer | calc | p.184 | high |
| KICAD-044 | fab | PCBWay capabilities page (accessed 2018-11-19): minimum trace width 0.1 mm; minimum drill size 0.2 mm. | w_min = 0.1 mm; drill_min = 0.2 mm | — | PCBWay | calc | p.184 | high |
| KICAD-045 | fab | NextPCB standard 2-layer order defaults (2022): min trace/space outer 6/6 mil; min drilled hole 0.3 mm; 1 oz finished copper; 1.6 mm; tented vias; HASL. | trace/space ≥ 6/6 mil; hole ≥ 0.3 mm; Cu = 1 oz | — | NextPCB default options | calc | p.455 | high |
| KICAD-046 | fab | KiCad 6 default Constraints/Net Class values exceed OSH Park and PCBWay minimums and were accepted without issue by PCBWay, OSH Park and NextPCB; author keeps defaults and only ADDS power net classes. | — | — | Board Setup > Design Rules | inspect | p.184, p.334, p.424 | high |
| KICAD-047 | current-carrying | Signal traces carrying < 20 mA can be ~0.3 mm wide or less (down to fab minimum) to allow denser routing. | w_signal ≈ 0.3 mm for I < 20 mA | I | Low-power signal nets | calc | p.160 | high |
| KICAD-048 | current-carrying | Power traces (GND, 5V, 3.3V, 12V) 0.30–0.40 mm wide on low-voltage, low-power boards; wider/thicker for higher current (Track Width calculator for exact values). | w_power ∈ [0.30, 0.40] mm | I, ΔT | Low-voltage low-power boards | calc | p.188 | high |
| KICAD-049 | process | Power net classes must have track width, via size, via hole and clearance larger than Default, and net-class minimums ≥ global Constraints minimums. Author's values: PSU project `power_input`/`power_output` track 0.25 → 0.35 mm, via 0.9 mm, hole 0.5 mm; LED-matrix `Vcc`/`GND` track 0.3 mm, via 0.85 mm, hole 0.45 mm; `Signal` class = default. | class.min_i ≥ constraints.min_i; w_power ∈ {0.35, 0.3} mm; via ∈ {0.9/0.5, 0.85/0.45} mm | — | Board Setup > Net Classes (inherited from Schematic Setup > Net Classes) | inspect | p.264–265, p.333–334, p.424, p.491, p.493 | high |
| KICAD-050 | process | Custom DRC rule syntax (KiCad 6): `(version 1)`; `(rule ExampleMinPowerNetClearance (constraint clearance (min 1.0mm)) (condition "A.NetClass == 'Power'"))` → 1 mm min clearance for Power-class copper; run the Checker before OK; rule name appears in DRC messages; comment out to disable. | clearance_min(Power) = 1.0 mm (example) | net class | Board Setup > Custom Rules | inspect | p.334–337 | high |
| KICAD-051 | process | Board Setup > Constraints holds global minimums (copper clearance, through-hole diameter, ...); e.g. min clearance 0.50 mm draws clearance outlines; DRC uses these; consult the fab before changing. | — | fab minimums | — | inspect | p.332 | high |
| KICAD-052 | process | Pre-defined track/via/diff-pair sizes fill the toolbar dropdowns; default = "use net class"; enable "Existing track width" so continued segments keep their width (0.1 mm segment continued after selecting 0.2 mm stays 0.1 mm). | — | — | Board Setup > Pre-defined Sizes | inspect | p.308–309, p.333 | high |
| KICAD-053 | process | Placement order: (1) mechanically constrained / user-interface parts (connectors, headers, LEDs, buttons, switches, mounting holes) along edges → LOCK (`L`); (2) parts electrically adjacent to them; (3) largest internal part (MCU/regulators); (4) small parts (R, C). Lock everything after final refinement. | — | — | Layout step 3 | inspect | p.118, p.186–187, p.303, p.429–433, p.506 | high |
| KICAD-054 | process | Placement principles: functionally related parts close together; shorter traces; consider assembly; obey component datasheets (heat-sink space, thermal vias under exposed pads); iterate placement to remove wasted area (cost) and shorten traces. | — | — | Layout step 3 | review | p.187–188, p.433–434 | high |
| KICAD-055 | process | Orient/place footprints to minimize crossing ratsnest lines before routing (rotate 90° to uncross). | crossings → min | ratsnest | Layout step 3 | inspect | p.119–120 | high |
| KICAD-056 | connectors | Connector orientation must leave room for the mating cable/plug (rigid barrel-jack cables: extra clearance) and keep cables away from the work area (barrel jack on the side opposite the breadboard; on/off switch next to the jack; selector switches accessible from board sides; screw-terminal openings facing outward; indicator LED visible). | — | — | Layout step 3 | review | p.186–187, p.397, p.422, p.431–433, p.506 | low |
| KICAD-057 | process | Routing order: (1) critical traces (antennas, matched lengths), (2) power traces, (3) all remaining traces; DRC before moving on. | — | — | Layout step 4a | inspect | p.188–189 | high |
| KICAD-058 | antenna | PCB-trace antenna areas require a keep-out on ALL copper layers (no components, no traces, no copper under/behind the antenna). | keepout ∀ Cu layers | antenna region | ESP32 module, micro:bit BLE antenna | inspect | p.168, p.188 | high |
| KICAD-059 | mechanical | Keep-out for moving parts (slide-switch actuator travel) may exclude footprints while still allowing tracks/vias; keep-out zone options: per copper layer; tracks / vias / pads / copper fills / footprints. | — | — | Keep-out zone properties | inspect | p.168, p.354–355 | high |
| KICAD-060 | process | 2-layer routing plan: GND via a bottom copper fill (no manual GND tracks), all other nets on top; vias only where needed (`V` inserts a via and swaps layer); optionally a top-layer Vcc fill. Multilayer: GND bottom, rails on an inner layer, signals on top. Fill zones AFTER routing; DRC after filling (0 unconnected). | — | — | Layout step 4a/4b | inspect | p.189–190, p.441–445, p.514–519 | high |
| KICAD-061 | process | Routing craft: pack parallel tracks to the DRC minimum spacing (`D` drag) — gaps waste space; prefer shorter tracks; prefer a shorter track with vias over a long detour; minimize bottom-layer segment length; try moving existing routes before adding a via; optimize after each pin group; lock finished routes; route arm/edge headers close to the board edge to leave room. | — | — | Layout step 4a | review | p.514–516 | low |
| KICAD-062 | process | Interactive router modes: Shove (moves tracks/vias, never violates rules) and Walk-around (changes nothing, finds compliant path) for normal work; Highlight-collisions is the only mode that permits "Allow DRC violations" — use only for schematic-less scratch tracks, never for production routing. | — | — | Route > Interactive Router Settings | inspect | p.340, p.357–359, p.442 | high |
| KICAD-063 | solder | Pads connect to copper fills via thermal reliefs (up to 4 spokes) so soldering heat is not sunk into the plane; solid fills are the modern default (no warping observed); hatched fill also used by author. | spokes ≤ 4 | — | Zone properties | inspect | p.27, p.189–190, p.353 | high |
| KICAD-064 | process | Ground planes: some EMI protection, heat spreading, and enforce "signals on top, every GND pad via'd to the bottom plane". | — | — | 2-layer boards | review | p.190 | low |
| KICAD-065 | dfm | Silkscreen content checklist — front: pad/pin function labels, switch position labels (On/Off, voltage), polarity marks (`+`/`-`, `K`), component values; back: board name, version (from a text variable), power-input voltage + connector polarity, logos, URL. Bottom side has more free area. | — | — | Layout step 5 | inspect | p.137–143, p.190–192, p.446–449, p.520–525 | high |
| KICAD-066 | dfm | Silkscreen has no automated correctness check — manually verify every text/graphic (incl. those inherited from footprints), check typos in the Gerber viewer, verify in 3D. | — | — | Layout step 5/7 | review | p.139, p.192, p.394, p.530 | high |
| KICAD-067 | dfm | Text on the back must be on `B.Silkscreen` with "Mirrored" checked; footprints on the back via Side = Back (then re-position; graphics appear mirrored). | mirrored = true for B.Silkscreen text | — | Text/Footprint properties | inspect | p.142, p.449, p.511–513, p.523 | high |
| KICAD-068 | dfm | Silkscreen must not overlap other silkscreen or intrude into a pad's solder-mask opening — DRC errors "silkscreen overlapping" and "silkscreen clipped by solder mask"; fix inside the footprint (Footprint Editor) when the source is a custom footprint. | overlap = 0; silk ∩ mask opening = ∅ | — | DRC | inspect | p.126, p.138, p.526–529 | high |
| KICAD-069 | dfm | Reference designators must be placed outside the footprint's outer boundary and not overlap other silk so they stay readable on the assembled board; hide unhelpful texts (mounting-hole refs/values, long footprint names) rather than crowd the silk. | — | — | Layout step 5 | inspect | p.448, p.522–523 | high |
| KICAD-070 | dfm | Silkscreen text sizes used by the author (bulk-set via Edit Text & Graphics Properties): pin-header labels moved F.Fab→F.Silkscreen with line thickness 0.1 mm, text height 0.8 mm; reference designators line thickness 0.1 mm, width 0.7 mm, height 0.7 mm. | silk line = 0.1 mm; text h = 0.7–0.8 mm | — | KiCad 6 defaults are larger; fab silk minimums not stated | inspect | p.520–522 | high |
| KICAD-071 | dfm | Logo footprints must fit the board (KiCad ships `KiCad-Logo2_40mm_Silkscreen`, `KiCad-Logo2_8mm_Silkscreen`, `KiCad-Logo2_5mm_Silkscreen`, CE/ESD/OSHW logos in the `Symbol` library); place on the back via Side = Back. | logo size < available area | — | Layout step 5 | inspect | p.140–141, p.524 | high |
| KICAD-072 | process | Footprints only in the layout (logos) get `REF**` → DRC "undefined reference" warning; give a unique reference (e.g. `REF1`) and either add a schematic symbol (any single-pin symbol satisfies DRC), tick "Not in schematic", or accept the "Extra footprint" warning (default Warning). | — | — | DRC | inspect | p.145–148, p.337–338, p.451, p.529 | high |
| KICAD-073 | process | DRC cadence: during routing, after every major routing session, after every copper fill, and a final run before Gerber export with "refill zones before DRC", "report all errors for tracks", courtyard overlap and missing-courtyard checks enabled. Goal: 0 errors; each remaining warning individually justified. | DRC errors = 0 | — | Layout step 6 | inspect | p.126, p.144, p.192–193, p.389, p.450, p.463 | high |
| KICAD-074 | process | DRC Violation Severity per type = Error / Warning / Ignore; defaults "reasonable and appropriate"; `Extra footprint` default = Warning. | — | — | Board Setup > Violation Severity | inspect | p.337–338 | high |
| KICAD-075 | dfm | Footprint courtyard (`F.CrtYd`/`B.CrtYd`) = smallest area giving minimum electrical and mechanical clearance; DRC checks courtyard overlap and missing courtyards; every custom footprint needs a courtyard rectangle. | courtyards non-overlapping; ∀ footprint ∃ courtyard | — | DRC options; Footprint Editor step 4 | inspect | p.193, p.377 | high |
| KICAD-076 | fab | Gerber export (File > Fabrication Outputs > Gerbers, or Plot): Plot format = Gerber; output directory inside the project; layers = F.Cu, B.Cu, F.Paste, B.Paste, F.Silkscreen, B.Silkscreen, F.Mask, B.Mask, Edge.Cuts; General: Plot footprint values ON, Plot reference designators ON, Use drill/place file origin ON, Check zone fills before plotting ON; Gerber options: Use Protel filename extensions ON, Generate Gerber job file (optional), Use extended X2 format ON (recommended), Include netlist attributes (optional). Tested with NextPCB, JLCPCB, OSH Park, PCBWay. | 9 layers | — | KiCad 6 Plot dialog | inspect | p.148–150, p.389–391 | high |
| KICAD-077 | fab | Drill files: same output folder as Gerbers; Map File Format = PostScript; defaults otherwise; produces two files (PTH and NPTH). The "Generate Drill Files" button in the Plot window only opens the drill dialog — press its own "Generate Drill File" button. | 2 drill files (PTH + NPTH) | — | KiCad 6 | inspect | p.150, p.392 | high |
| KICAD-078 | fab | ZIP the Gerber directory; inspect every layer in the KiCad Gerber Viewer (open all files except `.gbrjob`) AND at least one online viewer (gerber-viewer.com, gerblook.org) AND the fab's own viewer; look for silkscreen typos/missing graphics, copper tracks/fills, vias/holes, edge cuts. Designer, not fab, owns file correctness. | — | — | Layout step 7 | inspect | p.151–153, p.393–395, p.452–454 | high |
| KICAD-079 | fab | Fab order forms need board width and height — measure from Edge.Cuts extents (dimension tool on a User layer); NextPCB extracts them from Gerbers. Example boards: 52.324 mm × 28.702 mm (PSU). | W, H (mm) | Edge.Cuts | Online fab order | calc | p.153, p.454, p.530 | high |
| KICAD-080 | fab | Common Gerber-export mistakes: wrong layer set, wrong filename extensions, wrong units, forgotten drill files; uploading native `.kicad_pcb` (OSH Park) removes this risk. | — | — | — | review | p.193 | high |
| KICAD-081 | fab | Non-standard fab options raise price sharply: NextPCB red mask +US$33 vs green; lead-free HASL +US$15; removing the fab's silkscreen tracking code costs extra. OSH Park = minimal options; PCBWay = full options. | Δcost(red mask) = US$33; Δcost(Pb-free HASL) = US$15 | — | 2022 prices, 5 pcs 28.7×52.3 mm | review | p.154–157, p.455–456 | high |
| KICAD-082 | via | Via = plated hole smaller than a component hole, mask-covered (tented), no soldering pad; types: through, blind, buried, micro-via (laser). Free-standing via types selectable: through / micro / blind. | — | — | — | inspect | p.163–164, p.313, p.455 | high |
| KICAD-083 | fab | Annular ring width = minimum distance from pad edge to hole edge; drill misregistration → tangency or breakout; keep ring ≥ fab minimum. | ring = (pad_dia − hole_dia)/2 ≥ fab minimum | pad_dia, hole_dia | Through-hole pads and vias | calc | p.164 | medium |
| KICAD-084 | fab | Drill bits (tungsten carbide) come in discrete sizes such as 0.3, 0.6, 1.2 mm; drill file gives coordinates and size per hole; laser drilling for micro-vias. | hole sizes ∈ discrete set | — | — | inspect | p.166 | high |
| KICAD-085 | fab | PTH = default hole type (connects both sides); NPTH for unplated mounting holes. | — | — | Pad properties | inspect | p.24, p.162–163 | high |
| KICAD-086 | dfm | Solder mask: green most common/cheapest; prevents oxidation and solder bridges. Silkscreen: white most common; black, yellow available. | — | — | — | review | p.165–166, p.455 | high |
| KICAD-087 | connectors | Gold-finger edge connectors withstand at least 1,000 insertion cycles. | cycles ≥ 1000 | — | Card-edge boards | review | p.167 | high |
| KICAD-088 | assembly | For volume/automated assembly and minimum size design with SMD; THT only where needed (pin headers); modules with 90° headers may need straight headers to mate PCB sockets; socket the MCU module if it must be removed for programming. | — | — | — | review | p.166–167, p.539–541 | low |
| KICAD-089 | assembly | Solder-paste stencils are stainless steel with apertures matching pads; paste + pick-and-place + reflow profile must suit board/components. | — | — | — | review | p.170–171 | low |
| KICAD-090 | dfm | Panelization: fabs place many boards on a panel; boards separate at breakaway routes/points (mouse bites). | — | — | — | review | p.169–170 | low |
| KICAD-091 | process | Layer alignment target not required by modern online fabs; add only if the fab asks. | — | — | — | review | p.315 | high |
| KICAD-092 | process | Set the drill/place origin and grid origin deliberately (Set Origins tool) and plot with "Use drill/place file origin". | — | — | Pcbnew right toolbar; Plot dialog | inspect | p.316, p.391 | medium |
| KICAD-093 | process | Pcbnew editing defaults the author recommends: grid lines 1 px; snap-to-grid always; full-window crosshair; rotate step 45° (`R`/Shift-`R`); magnetic snap to pads, tracks, graphics = "always". | rotate step = 45° | — | Preferences > PCB Editor | inspect | p.301, p.321–323 | high |
| KICAD-094 | process | Autosave every 5 minutes (author's setting); never use nightly builds for work you cannot lose. | autosave = 5 min | — | Preferences > Common > Session | inspect | p.36, p.296–297 | high |
| KICAD-095 | process | Hotkeys used throughout: `A` add symbol, `W` wire, `L` net label (schematic) / lock toggle (layout), `X` route, `V` via + layer swap, `D` drag 45°, `G` free drag, `M` move, `R` rotate, `O` footprint chooser, Ctrl-D duplicate, space resets dx/dy. | — | — | KiCad 6 defaults | inspect | p.88, p.98, p.101, p.121, p.124–126, p.303, p.307, p.344, p.373 | high |
| KICAD-096 | process | "Update PCB from Schematic" options: re-link footprints, delete footprints removed from schematic, replace footprints with changed assignments — enable re-link + replace when an assignment changed (e.g. THT→SMD); layout keeps stale tracks after net changes, so delete and re-route them, then DRC. | — | — | Pcbnew import | inspect | p.110, p.304–305, p.348–349, p.459–463 | high |
| KICAD-097 | process | Text variables `${NAME}` (Schematic Setup / Board Setup > Text Variables, shared between editors) drive the Revision field and silkscreen text; author uses `design_version` = "1.0". | — | — | KiCad 6 feature | inspect | p.329–331, p.469–470, p.524 | high |
| KICAD-098 | process | Text & Graphics defaults (Board Setup) set edge-cut line thickness and silkscreen/copper text size & thickness; units, format, precision. | — | — | Board Setup > Text & Graphics > Defaults | inspect | p.328–329 | high |
| KICAD-099 | process | Use the Selection Filter (Tracks / Footprints / Graphics / Text) and net-visibility toggles (hide GND/Vcc classes to reveal remaining ratsnest) in dense layouts. | — | — | Pcbnew Appearance | inspect | p.111, p.119, p.320, p.517 | low |
| KICAD-100 | process | Group related footprints so they move together; lock connectors/mounting holes fixed by external hardware; use Align/Distribute for symmetric rows (buttons, holes, module outlines). | — | — | Pcbnew Group / Lock / Align | inspect | p.301–303, p.431–432, p.497–498, p.506 | high |
| KICAD-101 | process | Thermal vias (unconnected to traces, under a die-attach paddle) are added during placement when the datasheet requires them. | — | datasheet | Exposed-pad ICs | inspect | p.187–188 | high |
| KICAD-102 | process | Footprint creation sequence: (1) new footprint in a library, (2) body outline on `F.Fab` from the datasheet mechanical drawing, (3) pads, (4) courtyard rectangle on `F.Courtyard`, (5) silkscreen graphics + pin-1 mark on `F.Silkscreen`, (6) save & use; use the footprint wizard for BGA/QFP/DIP/QFN/SOIC. | — | datasheet | Footprint Editor | inspect | p.366–369, p.372–380 | high |
| KICAD-103 | process | Footprint naming: package type + pin count + key dimension + component model (+ author initials), e.g. "DIP 8 W7.62mm NE555 PD". | — | — | Footprint Editor | inspect | p.371 | high |
| KICAD-104 | dfm | `F.Fab` outline = package body from the datasheet (DIP-8 body 10.16 mm × 7.11 mm); draw with grid 0.127 mm using dx/dy readouts (space bar resets). | body = 10.16 × 7.11 mm (NE555 PDIP) | datasheet | Footprint Editor step 2 | inspect | p.372–373 | high |
| KICAD-105 | dfm | THT pads: pitch 2.54 mm; row spacing per datasheet 7.37–7.87 mm → nominal 7.62 mm; grid 1.27 mm for pad placement; verify every pad number/position against the datasheet; pads span all layers; centre the body on the pads (grid 0.635 mm). | pitch = 2.54 mm; row = 7.62 mm (7.37–7.87) | datasheet | DIP-8 example | inspect | p.374–376 | high |
| KICAD-106 | dfm | Pad 1 rectangular (others round/oval) so pin 1 is identifiable without silkscreen; pad properties: size, hole shape, pad-to-hole offset, net name. | — | — | Footprint Editor step 3 | inspect | p.376 | high |
| KICAD-107 | dfm | Footprint silkscreen: grid 0.254 mm; short corner lines along the fab outline; small circle beside pad 1; verify with the footprint editor's 3D viewer. | — | — | Footprint Editor step 5 | inspect | p.378 | high |
| KICAD-108 | dfm | Footprints must NOT contain `Edge.Cuts` geometry (a custom Arduino footprint with an Edge.Cuts rectangle rendered as a hole in 3D and would be routed out by the fab). | Edge.Cuts items in footprint = 0 | — | Custom footprints | inspect | p.508–509 | high |
| KICAD-109 | process | 3D models: `.step` or `.wrl` via footprint properties > 3D Models; adjust scale/rotation/offset and verify orientation in the 3D viewer; models have no electrical effect (wrong model is harmless); add models when sharing designs. | — | — | Pcbnew / Footprint Editor | inspect | p.381–388, p.531–537 | high |
| KICAD-110 | process | Dimension tools (aligned linear, orthogonal, center, leader) on `User.N` layers (excluded from Gerbers) document board size and critical pitches; interactive ruler for transient checks and final sanity measurements. | — | — | Pcbnew | inspect | p.360–362, p.505, p.530 | high |
| KICAD-111 | process | Bulk layout edits: Edit Track & Via Properties; Edit Text & Graphics Properties (scope by refs/values/layer/footprint library id); Change Footprints; Swap Layers (e.g. F.Cu→In1.Cu); Global Deletions (all tracks/vias) — all undoable. | — | — | Pcbnew Edit menu | inspect | p.362–366, p.520–523 | high |
| KICAD-112 | process | Filled zone recipe: pick layer + net (B.Cu / GND), fill type solid or hatch, draw the polygon as close as possible to the board perimeter, Zones > Fill (Fill All); a net-connected zone auto-connects all same-net pads; duplicate a zone and change layer/net for a second fill (F.Cu / Vcc). | — | — | Layout step 4b | inspect | p.349–353, p.444–445, p.517–519 | high |
| KICAD-113 | requirements | Breadboard PSU requirements: plugs directly onto the breadboard (no wires); on/off switch; 5 V and 3.3 V outputs; input from 6–12 V wall supplies. | V_in ∈ [6, 12] V; V_out ∈ {5, 3.3} V | — | Part 9 project | review | p.396 | high |
| KICAD-114 | mechanical | Breadboard rail geometry: hole pitch 2.54 mm; outer power rails 19 × 2.54 = 48.26 mm (measured 48.52 mm); inner rails 17 × 2.54 = 43.18 mm (measured 43.25 mm); board height ≤ breadboard height (no overhang); notch width ≈ one column spacing. Author trusts caliper measurements over nominal after prototyping. | outer = 48.26 mm nominal / 48.52 mm measured; inner = 43.18 mm nominal / 43.25 mm measured | — | Mini breadboard | measure | p.421–422, p.426 | high |
| KICAD-115 | process | Precise pin-to-pin placement: superimpose the moving footprint's reference pad on the fixed one, reset dx/dy, move with dx = 0 until dy = target; grid 0.0508 mm achieved 43.2816 mm vs 43.25 mm target (within 1%) — accepted because breadboard tolerance is larger; lock immediately. | |Δ| ≤ 1% of target | target spacing | Layout step 2/3 | measure | p.427–428, p.461–462 | high |
| KICAD-116 | mechanical | LED-matrix module (MAX7219 8×8) measured: header-to-header 45.79 mm; module 31.88 mm × 50.59 mm; left edge → leftmost pin 11.20 mm; right edge → rightmost pin 10.55 mm (headers NOT symmetric). Placement error of even 1 mm makes assembly impossible (too close) or leaves visible gaps (too far). Drawn outline 31.850 × 50.670 mm on 0.01 mm grid; pin placed at 11.1760 mm vs 11.20 mm accepted. | spacing = 45.79 mm; |Δ| < 1 mm; achieved Δ ≈ 0.024 mm | caliper | Part 10 project | measure | p.495–496, p.501–504 | high |
| KICAD-117 | mechanical | Centring headers in a module outline: offset = (module_height − header_spacing)/2 = (50.59 − 45.79)/2 = 2.4 mm; place first header 2–3 mm from the edge. | offset = (H_module − S_header)/2 | H_module, S_header | Part 10 | calc | p.504 | high |
| KICAD-118 | protection | Never join the outputs of two different regulators (3.3 V and 5 V) on one net label: with selector switches set differently the regulators short (U2 pin 3 to U1 pin 2) and are destroyed; unfused 12 V wall supplies give no protection. Fix = separate nets per output (PWR_OUT_TOP / PWR_OUT_BOT) in the same net class. | — | net list | Design review of PSU project (defect found by a reader; not caught by ERC/DRC) | review | p.456–458 | high |
| KICAD-119 | process | Design-review lesson: a schematic bug can be invisible to ERC and DRC (shared net label) and a layout bug (header pair swapped J6↔J2/J4↔J5) invisible to DRC; keep a copy of the project directory before repairs; re-verify DRC = 0 errors/0 warnings after the fix; test the manufactured prototype. | — | — | — | review | p.456–463, p.531 | high |
| KICAD-120 | process | Net-label-only corrections that do not change connectivity (wrong label names) need no Gerber re-export; verify by comparing pad/net names between schematic and layout. | — | — | — | inspect | p.537–539 | high |
| KICAD-121 | power | Arduino Pro Mini `VCC` pin bypasses the on-board regulator → feed only regulated 5 V (5 V model; author uses a 5 V 500 mA mains adapter or USB-to-barrel cable); alternatively feed `RAW` (pin 26): 5–12 V for the 5 V model, 3.35–12 V for the 3.3 V model. | VCC = 5 V regulated; RAW ∈ [5, 12] V (5 V model) or [3.35, 12] V (3.3 V model) | supply | Part 10 project | review | p.468–469 | high |
| KICAD-122 | process | Header-based modelling of modules: represent an unavailable module by its `Conn_01x05` headers, but mirror the output-header symbol vertically so pin numbers align physically; orient header footprints from the physical part (Vcc pin left); add a schematic text reminder. | — | — | Part 10 | inspect | p.466, p.474–475, p.489, p.502–503 | high |
| KICAD-123 | dfm | Bottom-side placement of non-UI parts (MCU module, barrel jack, switch, resistors) keeps the top for the user interface; switch labels for a bottom-side switch go on `B.Silkscreen` mirrored ("On" near pin 3, "Off" near pin 1). | — | — | Part 10 | inspect | p.510–513, p.523 | high |

## 2. Formulas & tables (numbers)

### 2.1 Fab capability minimums quoted in the text

| Fab | Parameter | Value (as printed) | Metric | Source |
|---|---|---|---|---|
| OSH Park | min trace width | 0.006 in | 0.1524 mm (6 mil) | p.184 (accessed 2018-11-19) |
| OSH Park | min via diameter | 0.027 in | 0.6858 mm (27 mil) | p.184 |
| PCBWay | min trace width | 0.1 mm | 0.1 mm (3.94 mil) | p.184 |
| PCBWay | min drill size | 0.2 mm | 0.2 mm | p.184 |
| NextPCB (order defaults) | min trace/space outer | 6/6 mil | 0.1524/0.1524 mm | p.455 |
| NextPCB | min drilled hole | 0.3 mm | 0.3 mm | p.455 |
| NextPCB | finished copper | 1 oz | ≈35 µm | p.455 |
| NextPCB | thickness | 1.6 mm | — | p.455 |
| NextPCB | via process | tenting | — | p.455 |
| NextPCB | surface finish | HASL (lead-free +US$15) | — | p.455–456 |
| NextPCB | solder mask | green (red +US$33) | — | p.455–456 |
| NextPCB | silkscreen | white | — | p.455 |
| Generic 2-layer | price | ~$10 / 2 sq in / 3 pcs ⇒ ~$5 per sq in | — | p.33 |

Note: the book states KiCad 6 default Constraints exceed all these minimums (p.184, p.424) but does not print the default values themselves.

### 2.2 Net-class values used by the author (KiCad 6 Board Setup > Net Classes)

| Project | Net class | Nets | Track width (mm) | Via size (mm) | Via hole (mm) | Source |
|---|---|---|---|---|---|---|
| Breadboard PSU | Default | all others | 0.25 (KiCad default) | (default) | (default) | p.424 |
| Breadboard PSU | power_input | 12V, PWR_input | 0.35 | 0.9 | 0.5 | p.416, p.424 |
| Breadboard PSU | power_output | 3.3V, 5V, PWR_output → later PWR_OUT_TOP, PWR_OUT_BOT | 0.35 | 0.9 | 0.5 | p.416, p.424, p.458 |
| LED matrix | Vcc | Vcc | 0.3 | 0.85 | 0.45 | p.491, p.493 |
| LED matrix | GND | GND | 0.3 | 0.85 | 0.45 | p.491, p.493 |
| LED matrix | Signal | CLK0–3, DIN0–3, CS0–3, MODE_SELECT, TIMER_RESET, … | default | default | default | p.491 |
| Custom-rule example | Power | — | — | — | — (clearance min 1.0 mm) | p.335 |

### 2.3 Trace-width guidance

| Net type | Width | Condition | Source |
|---|---|---|---|
| Signal | ~0.3 mm or less (≥ fab minimum) | I < 20 mA | p.160 |
| Power (GND, 5 V, 3.3 V…) | 0.30–0.40 mm | low-voltage, low-power boards | p.188 |
| Power net class (author) | 0.35 mm / 0.30 mm | PSU / LED-matrix projects | p.424, p.493 |

### 2.4 Grid sizes by task (mm)

| Task | Grid | Source |
|---|---|---|
| Schematic placement | 2.54 (fine: 1.27) | p.92 |
| Board outline / large features | 1.27 | p.182 |
| Footprint placement | 0.635 | p.182 |
| Routing | 0.508 → 0.254 | p.182 |
| Exact metric outline | custom 0.5 | p.182 |
| Corner arcs / silkscreen / outline refinement | 0.254 | p.134, p.378, p.435, p.507(0.6450 used once) |
| Footprint body from datasheet | 0.127 | p.372 |
| Pad placement (2.54 pitch) | 1.27 | p.374 |
| Precision pin-to-pin placement | 0.0508 | p.427, p.504 |
| Drawing module outline to caliper values | 0.01 | p.496 |

### 2.5 Author's silkscreen text parameters (Part 10)

| Item | Line thickness (mm) | Text width (mm) | Text height (mm) | Layer | Source |
|---|---|---|---|---|---|
| Pin-header value labels | 0.1 | (default) | 0.8 | F.Fab → F.Silkscreen | p.520 |
| Reference designators | 0.1 | 0.7 | 0.7 | F/B.Silkscreen | p.521–522 |

### 2.6 Gerber/drill export settings (verified with NextPCB, JLCPCB, OSH Park, PCBWay)

| Setting | Value | Source |
|---|---|---|
| Plot format | Gerber | p.390 |
| Output directory | inside project dir | p.390 |
| Layers | F.Cu, B.Cu, F.Paste, B.Paste, F.Silkscreen, B.Silkscreen, F.Mask, B.Mask, Edge.Cuts | p.390 |
| Plot footprint values | ON | p.391 |
| Plot reference designators | ON | p.391 |
| Use drill/place file origin | ON | p.391 |
| Check zone fills before plotting | ON | p.391 |
| Use Protel filename extensions | ON | p.149, p.391 |
| Generate Gerber job file | optional | p.391 |
| Use extended X2 format | ON (recommended) | p.149, p.391 |
| Include netlist attributes | optional | p.391 |
| Drill: output folder | same as Gerbers | p.392 |
| Drill: map file format | PostScript | p.392 |
| Drill: other options | defaults | p.150, p.392 |
| Drill output | 2 files: PTH + NPTH | p.392 |
| Gerbview import | all files except `.gbrjob` | p.152, p.393 |

### 2.7 Project bills of materials (author's exact footprints)

Breadboard PSU (Table 9.1.1, p.398–399):

| Ref | Value | Footprint |
|---|---|---|
| C1 | 10u | Capacitor_THT:C_Disc_D3.0mm_W1.6mm_P2.50mm |
| C2 | 1u | Capacitor_THT:C_Disc_D3.0mm_W1.6mm_P2.50mm |
| C3 | 0.1u | Capacitor_THT:C_Disc_D3.0mm_W1.6mm_P2.50mm |
| D1 | LED | LED_THT:LED_D5.0mm |
| J1 | Barrel_Jack_Switch | Connector_BarrelJack:BarrelJack_Horizontal |
| J2, J5 | Screw_Terminal_01x02 | TerminalBlock:TerminalBlock_bornier-2_P5.08mm |
| J4, J6 | Conn_01x02_Male | Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical |
| J3, J7 | Conn_01x03_Male | Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical (as printed; evidently 1x03) |
| R2 | 330 | Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal |
| R1, R3 | 560 | Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal |
| S1 | EG1218 | digikey-footprints:Switch_Slide_11.6x4mm_EG1218 |
| U1 | LM317_TO-220 | Package_TO_SOT_THT:TO-220-3_Vertical |
| U2 | LM7805_TO220 | Package_TO_SOT_THT:TO-220-3_Vertical |

LED matrix (Table 10.1.1, p.467):

| Ref | Value | Footprint |
|---|---|---|
| H1–H4 | MountingHole | MountingHole:MountingHole_2.5mm |
| J1 | LED1_IN | Connector_PinHeader_2.54mm:PinHeader_1x05_P2.54mm_Vertical |
| J2 | Barrel_Jack | Connector_BarrelJack:BarrelJack_Horizontal |
| J3–J9 | LED1_OUT … LED4_OUT | Connector_PinSocket_2.54mm:PinSocket_1x05_P2.54mm_Vertical |
| R1, R2 | 10K | Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal |
| S1, S2 | 1825967-1 | 1825967-1:SW_1825967-1 (SnapEDA) |
| S3 | SS12D07VG4 | SS12D07VG4:SW_SS12D07VG4 (SnapEDA) |
| U1 | ArduinoProMiniSimple | DesktopLibrary:ArduinoProMiniCustom |

### 2.8 Mechanical constraint data (measured with caliper)

| Item | Nominal | Measured / used | Source |
|---|---|---|---|
| Breadboard hole pitch | 2.54 mm | — | p.422 |
| Outer power-rail spacing | 19 × 2.54 = 48.26 mm | 48.52 mm | p.422 |
| Inner power-rail spacing | 17 × 2.54 = 43.18 mm | 43.25 mm (placed 43.2816 / 43.282 mm) | p.422, p.428, p.462 |
| PSU rough outline | — | 52.578 mm × 35.560 mm | p.429 |
| PSU final board | — | 52.324 mm × 28.702 mm (order: 28.7 × 52.3) | p.454–455 |
| PSU corner radius | — | 1.016 mm | p.439 |
| LED-torch rough outline | ~65 × 25 mm | 66.29 mm × 26.41 mm | p.113–114 |
| LED-torch corner arc | — | dx = dy = 1.27 mm | p.135 |
| LED-matrix header spacing | — | 45.79 mm | p.495 |
| LED-matrix module W × H | — | 31.88 × 50.59 mm (drawn 31.850 × 50.670) | p.496 |
| LED-matrix header edge offsets | — | 11.20 mm (left), 10.55 mm (right); placed 11.1760 | p.501, p.504 |
| DIP-8 body (NE555) | 10.16 × 7.11 mm | — | p.372 |
| DIP-8 pitch / row | 2.54 mm / 7.37–7.87 mm | 7.62 mm | p.374–375 |
| Drill bit sizes (examples) | 0.3, 0.6, 1.2 mm | — | p.166 |
| Gold-finger insertion life | ≥ 1000 cycles | — | p.167 |
| Arduino Pro Mini RAW input | 5–12 V (5 V) / 3.35–12 V (3.3 V) | — | p.469 |

### 2.9 Formulas

- Board cost estimate (online fab, small 2-layer): `cost_USD ≈ 5 * area_sq_in` for a 3-piece order (p.33). Bounding-box area, not net area (p.466).
- Grid fit: `L = n * g` (n integer). For g = 1.27 mm: 39 → 49.53 mm, 40 → 50.8 mm; exact 50 mm requires g = 0.5 mm (p.182).
- Rail spacing: `S = k * 2.54 mm` (k = 19 outer, 17 inner) (p.422).
- Header centring: `offset = (H_module − S_header) / 2` = (50.59 − 45.79)/2 = 2.4 mm (p.504).
- Annular ring: `ring = (D_pad − D_hole) / 2` (definition p.164; formula derived).
- Placement acceptance: `|d_placed − d_target| / d_target ≤ 1%` (43.2816 vs 43.25 mm) (p.428).

## 3. Mechanizable checks

`CHECK-fab-minimums`: inputs = board constraints (min_track_mm, min_clearance_mm, min_via_dia_mm, min_drill_mm) and per-fab table (§2.1) → for each target fab i: pass iff constraint ≥ fab_i.min; margin = constraint − max_i(fab_i.min). Sources: KICAD-042/043/044/045.

`CHECK-netclass-ge-constraints`: inputs = net-class rows (track, clearance, via_dia, via_hole) and Constraints minimums → pass iff every class value ≥ global minimum; margin per field. Source: KICAD-049.

`CHECK-power-netclass-exists`: inputs = net names, net-class membership → pass iff every net matching /GND|VCC|VDD|\d+V\d*|PWR/ is in a class whose track width ≥ 0.30 mm and > Default width. Margin = width − 0.30. Sources: KICAD-048/049.

`CHECK-signal-width`: inputs = per-net max current (mA), track width (mm) → for I < 20 mA pass iff width ≥ fab_min; flag widths > 0.3 mm on signal nets as area-inefficient (warning). Source: KICAD-047.

`CHECK-annular-ring`: inputs = pad diameter, hole diameter, fab min ring → ring = (D_pad − D_hole)/2; pass iff ring ≥ fab min. Source: KICAD-083.

`CHECK-erc-clean`: inputs = ERC report (errors, warnings, "not fully annotated" flag) → pass iff errors = 0 and annotation complete; warnings must each carry an exclusion note. Sources: KICAD-012/017.

`CHECK-power-flags`: inputs = netlist, pin types → pass iff every net containing a power-input pin also contains a power-output pin or PWR_FLAG; GND has PWR_FLAG. Source: KICAD-018.

`CHECK-no-connect`: inputs = pins with no net → pass iff each has a no-connect flag positioned at the pin end. Sources: KICAD-016/017/027.

`CHECK-designators`: inputs = symbol references → pass iff none contains `?` and all unique; footprint references contain no `**`. Sources: KICAD-012/072.

`CHECK-footprint-assigned`: inputs = symbols (excluding power symbols) → pass iff footprint field non-empty and pad count == pin count. Sources: KICAD-008/013/014.

`CHECK-shared-source-nets`: inputs = netlist, regulator/supply output pins → fail iff two different power-output pins (or two regulator outputs via selector switches) can be joined on one net by any switch state. Source: KICAD-118.

`CHECK-drc-clean`: inputs = DRC report → pass iff errors = 0 and unconnected = 0; warnings limited to "Extra footprint"/schematic parity for logo footprints. Sources: KICAD-072/073.

`CHECK-courtyards`: inputs = footprints → pass iff every footprint has F/B.CrtYd geometry and no courtyard pair overlaps. Source: KICAD-075.

`CHECK-silkscreen`: inputs = silk items, pad mask openings → pass iff no silk∩silk overlap and no silk inside any mask opening; every reference designator centroid outside its footprint outline; back-silk text mirrored = true. Sources: KICAD-067/068/069.

`CHECK-outline`: inputs = Edge.Cuts segments → pass iff exactly one closed contour (endpoint tolerance = snap), no dangling segments, no intersection with any courtyard; footprints contain zero Edge.Cuts items. Sources: KICAD-035/108.

`CHECK-keepout-antenna`: inputs = antenna region polygon, copper on all layers → pass iff no copper/footprint inside the region on any layer. Source: KICAD-058.

`CHECK-zones`: inputs = zones → pass iff GND zone exists on B.Cu (2-layer), all GND pads connected after fill, DRC unconnected = 0. Sources: KICAD-060/112.

`CHECK-gerber-set`: inputs = plot output file list → pass iff files exist for F.Cu, B.Cu, F.Paste, B.Paste, F.Silkscreen, B.Silkscreen, F.Mask, B.Mask, Edge.Cuts with Protel extensions, X2 attributes present, plus PTH and NPTH drill files, in one ZIP. Sources: KICAD-076/077/078.

`CHECK-board-dims`: inputs = Edge.Cuts bounding box → report W, H (mm) for the fab form; cost ≈ 5 USD/sq-in × W×H/645.16. Sources: KICAD-002/079.

`CHECK-mating-geometry`: inputs = list of (pad_a, pad_b, target_mm, tol_pct) → pass iff |dist − target| ≤ tol_pct × target (author accepted 1%; module headers require < 1 mm absolute). Sources: KICAD-114/115/116.

`CHECK-mounting-holes`: inputs = hole footprints → pass iff each has a schematic symbol, count ≥ 1 (torch) / 4 symmetric about the board axis (matrix), and NPTH type. Source: KICAD-037.

`CHECK-title-block`: inputs = page settings (both editors) → pass iff title, date, revision non-empty; revision references a text variable when one exists. Sources: KICAD-011/097.

`CHECK-power-input-range`: inputs = module VCC/RAW pin used, supply voltage → pass iff (VCC and V = 5.0 regulated) or (RAW and 5 ≤ V ≤ 12 [5 V model] / 3.35 ≤ V ≤ 12 [3.3 V model]). Source: KICAD-121.

## 4. Verification procedures & plots

The book contains no simulation or electrical measurement procedures; its verification is tool-based:

1. ERC (schematic): run after wiring, after naming nets, and before layout. Good = "0 errors, 0 warnings" (p.102, p.417). Each violation pans to its location; use "Exclude this violation" only for documented library-modification warnings (p.487).
2. DRC (layout): run after routing, after zone fills (must report no unconnected items, p.445, p.519), and finally before plot with zone refill, all-track errors, courtyard overlap, missing courtyard enabled (p.193). Good = 0 errors; only "Extra footprint"/schematic-parity warnings for logo footprints remain (p.451, p.529).
3. 3D viewer: after outline refinement (holes/cutouts render correctly, p.508), after placement, and after silkscreen (verify text placement and mirroring, p.449, p.523).
4. Gerber review: KiCad Gerber Viewer layer-by-layer (edge cuts + one silkscreen at a time reduces clutter, p.394) + online viewer (gerber-viewer.com or gerblook.org) + fab viewer (NextPCB) before ordering (p.395, p.453). Pass = every layer matches intent, no typos, drill files present.
5. Mechanical fit: caliper measurement of mating hardware; interactive-ruler sanity check of every critical spacing after placement (p.505); acceptance ≤ 1% deviation (p.428).
6. Prototype test: order a small quantity (5 pcs) and assemble/test — defects invisible to ERC/DRC (regulator short, header pairing, label errors) surfaced only then (p.456, p.531, p.539).

## 5. Pitfalls, failure modes, review checklist

- [ ] Wire not actually attached to a pin → ERC "pin not connected" (p.412–414).
- [ ] Net label with the small attachment box still visible → not attached (p.259).
- [ ] No-connect flag drawn beside, not on, the pin end → still flagged (p.485).
- [ ] Overlapping/stacked pins in downloaded symbols hide unconnected pins (p.478, p.486).
- [ ] Power symbols/PWR_FLAG added after annotation → "schematic not fully annotated" (p.413, p.484).
- [ ] Symbol↔footprint mismatch is never reported by ERC (p.252).
- [ ] Missing footprint assignment → Update PCB error (p.253).
- [ ] One net label shared by two regulator outputs → short circuit when selectors differ (p.456–457).
- [ ] Header pairs mis-paired in layout (J6/J2 vs J5) — DRC cannot see it (p.457).
- [ ] Redundant Edge.Cuts segments → 3D viewer and fab problems (p.132).
- [ ] Edge.Cuts geometry inside a footprint → hole cut in the board (p.508).
- [ ] Edge cut touching a courtyard → DRC (p.439).
- [ ] Screw terminal openings facing inward (J5 rotated 180° wrong) (p.433).
- [ ] Logo footprint larger than the board (40 mm logo on a 25 mm board) (p.140).
- [ ] Back-side text not mirrored (p.142, p.449).
- [ ] Silkscreen overlapping silkscreen; silkscreen inside pad mask opening (p.526–527).
- [ ] `REF**` designators on layout-only footprints (p.146).
- [ ] Stale tracks left after schematic net changes (p.462).
- [ ] Wrong Gerber layer set / extensions / units / missing drill files (p.193); forgetting the second "Generate Drill File" button (p.150).
- [ ] Opening `.gbrjob` in the Gerber viewer (p.152, p.393).
- [ ] Changing library paths mid-project (p.80).
- [ ] Nightly builds crash — autosave 5 min (p.297).
- [ ] Custom stackup/finish selections not communicated to the fab (p.326).
- [ ] Non-standard fab options (colour, Pb-free) add large cost (p.456).
- [ ] Manufacturer tracking code appears on silkscreen unless paid to remove (p.157).
- [ ] Placement errors ≥ 1 mm on module headers → assembly impossible or visible gaps (p.495).
- [ ] Unregulated supply on Arduino Pro Mini VCC pin (p.468).
- [ ] Global labels used where hierarchical labels belong (p.273).
- [ ] "Allow DRC violations" left enabled in the interactive router (p.357).

## 6. Standards referenced

| Standard / spec | Governs | Page |
|---|---|---|
| Gerber format (Ucamco; X2 extended format) | fab data exchange; one file per layer; X2 attributes | p.34, p.149, p.391 |
| Excellon-style drill files (KiCad "Generate Drill Files", PTH/NPTH, PostScript map) | hole data | p.150, p.392 |
| IEEE (US) vs IEC (European) schematic symbol styles | symbol graphics consistency | p.159 |
| 2.54 mm (0.1 in) header/breadboard pitch convention | connector geometry | p.223, p.422 |
| Protel filename extensions (.GTL/.GBL/... via "Use Protel filename extensions") | Gerber file naming | p.149, p.391 |
| STEP (.step) / VRML (.wrl) | 3D model formats accepted by KiCad | p.385 |
| S-expression KiCad 6 file format | project/schematic/board files | p.71 |
| Reference-designator conventions (author's guide link) | designator prefixes | p.242 |

No IPC (e.g. IPC-7351, IPC-2221) or safety standards are cited anywhere in this volume.

## 7. Process / lifecycle guidance

The author's model workflow (Fig. 1.2.2, 3.2.1–3.2.3, 6.1.1, 6.2.1); linear as presented, iterative in practice (p.74–75, p.173, p.181).

### 7.1 Schematic design workflow (Eeschema)

| Step | Activity | Deliverable | Exit criterion | Source |
|---|---|---|---|---|
| 0 | Create project (new or from template); set library paths/tables; enable autosave | `.kicad_pro/.kicad_sch/.kicad_pcb` | project opens; libraries resolve | p.61–66, p.77–80 |
| 1 Setup | Grid (2.54/1.27 mm), snap on, H&V wires, Page Settings (title, date, rev via `${design_version}`), Schematic Setup: net classes pre-created, text variables, Field Name Templates (`Purpose`) | configured sheet | title block filled | p.81–87, p.173–175, p.401, p.469–470 |
| 2 Symbols | Find symbols (chooser / SnapEDA / Digi-Key libs / custom); add all; set Values (duplicate Ctrl-D) | all symbols on sheet with values | BOM symbol list complete | p.88–91, p.175–176, p.402–405, p.471–473 |
| 3 AAA | Arrange by functional group (inputs top-left → outputs); auto-Annotate; Associate footprints in bulk; cross-check designators vs BOM | annotated, associated schematic | no `?`; every symbol has `Library:Footprint` | p.92–97, p.176–177, p.406–409, p.474–477 |
| 4 Wire | Wires within groups, labels across groups, 90° only, no crossings, complete one group at a time; GND/power symbols; PWR_FLAG on GND and supply nets; no-connect on unused pins; fix overlapping pins | fully wired schematic | ratsnest complete after import | p.98–99, p.178, p.410–412, p.478–481 |
| 5 Nets | Name important nets; create net classes (power_input/power_output or Vcc/GND/Signal); assign nets | named nets + classes | all power/signal nets classified | p.100–101, p.178, p.415–416, p.482–483, p.491 |
| 6 ERC | Re-annotate if needed; run ERC; fix errors; exclude documented warnings | ERC report | 0 errors, 0 unexcluded warnings | p.102–103, p.179, p.276–281, p.413–417, p.484–487 |
| 7 Comments | Boxes + text per group; reminders for mirrored symbols; `Purpose` fields; rename header values (LED1_IN) | annotated schematic | reviewer can read intent | p.104–105, p.180, p.417–420, p.488–489 |
| 7b Last-minute | Add mounting-hole symbols with footprints; final net-class assignments | — | Update PCB imports without errors | p.490–491 |

### 7.2 Layout design workflow (Pcbnew)

| Step | Activity | Deliverable | Exit criterion | Source |
|---|---|---|---|---|
| 1 Setup | Board Setup: copper layers (2), layer roles, stackup defaults, solder mask/paste = 0, Text & Graphics defaults, Constraints ≥ fab minimums, Pre-defined sizes, Net Classes (power widths/vias), Custom Rules, Violation Severity; Page Settings; grid; Update PCB from Schematic | populated layout | import with no missing footprints | p.108–112, p.181–184, p.424–425, p.493–494 |
| 2 Outline & constraints | Caliper-measure mating hardware; draw module/guide rectangles on User.1/User.2; place & lock constrained footprints (pin headers at measured spacing); rough Edge.Cuts rectangle; mounting holes/cutouts | rough outline + locked anchors | anchors within 1% of target | p.113–117, p.184–186, p.426–429, p.494–499 |
| 3 Place | UI/perimeter parts → large → small; align/distribute; minimize ratsnest crossings; iterate to cut area; lock; set Side=Back for non-UI parts | placed footprints | all footprints inside outline; no courtyard overlaps | p.118–121, p.186–188, p.430–434, p.500–506, p.510–513 |
| 2' Refine outline | Delete rough rectangle; draw closed polygon on 0.254 mm grid; round corners (r ≈ 1.0–1.27 mm); check 3D | final Edge.Cuts | single closed contour; 3D correct | p.126–136, p.435–440, p.507–509 |
| 4a Route | Critical → power → rest; router Walk-around/Shove; net-class widths; `V` vias; leave GND (and Vcc) pads for fills; pack tracks; lock routes; DRC | routed board | only GND/Vcc ratsnest remain | p.122–126, p.188–189, p.441–444, p.514–517 |
| 4b Copper fills | B.Cu GND zone (and F.Cu Vcc zone) drawn to the perimeter; Fill All; DRC | filled board | DRC unconnected = 0 | p.189–190, p.444–445, p.517–519 |
| 5 Silkscreen | Move values F.Fab→F.Silkscreen; resize text in bulk (0.1 mm line, 0.7–0.8 mm height); polarity/switch labels; hide clutter; back side: name, version `${design_version}`, power info, logos (Side=Back, mirrored text); 3D check | silkscreen complete | no overlaps; all texts intentional | p.137–143, p.190–192, p.446–449, p.520–525 |
| 6 DRC | Final DRC with all options; fix silkscreen/courtyard errors (in footprint editor when inside a footprint); justify remaining warnings | DRC report | 0 errors | p.144–148, p.192–193, p.450–451, p.526–529 |
| 7 Export & manufacture | Plot Gerbers (§2.6) + drills; ZIP; review in Gerber Viewer + online + fab viewer; measure W×H; order (defaults; 5 pcs); wait ~2 weeks; assemble; test; document defects and iterate (copy project first) | fab package + ordered PCB | fab viewer renders correctly; prototype passes test | p.148–157, p.193, p.389–395, p.451–456, p.530 |

### 7.3 Footprint creation sub-process (p.366–380)

New library (Global/Project) → new footprint named "package pins dimension model initials" → F.Fab body from datasheet (grid 0.127 mm) → pads at datasheet pitch/row (grid 1.27 mm), pad 1 rectangular, verify numbers → F.Courtyard rectangle → F.Silkscreen corner lines + pin-1 circle (grid 0.254 mm) → 3D check → save → (optional) attach `.step`/`.wrl` with scale/rotation/offset.

### 7.4 Design-change control (p.456–463, p.537–539)

Copy project dir → fix schematic (nets/labels) → re-assign net classes → Update PCB → delete stale tracks → re-route → DRC 0/0 → re-export Gerbers only if connectivity/geometry changed.

## 8. Coverage log

- Text file: 4831 lines. Read sequentially in 200-line chunks: 1–3600 (all body text; the body ends at line 3572 with §10.6 "Assembled PCB"), then verified 3575–4831 = Index and back-cover blurb (skipped per brief; contains no engineering content).
- Skipped: Index (lines 3575–4831). No exercises exist. Nothing else skipped.
- Figures are not in the text; several values (Board Setup defaults, ERC/DRC dialog contents, net-class Default via values, silkscreen line widths in Text & Graphics defaults, the "Fig. 6.2.1.4 default constraint values") are only shown in screenshots and could not be transcribed — noted where relevant.
- The book is a tooling/workflow text: it contains no electrical formulas, no simulation, no thermal/current-carrying calculations (it defers to the Track Width calculator in the companion "Recipes" volume). Rule count is correspondingly weighted to process/DFM/fab.
- OCR/extraction noise: ligatures (ﬁ/ﬂ) preserved in source; some table rows in BOMs are split across lines (reassembled above); the printed "2.54-inch pitch" (p.223) and "PinHeader_1x02" for a 1x03 connector (Table 9.1.1) are transcribed as printed with notes.
- Version caveat: all UI names, layer names, env-vars and dialog options are KiCad 6; no CLI/Python/plugin content exists in this volume.
- Rules extracted: 123 (KICAD-001 … KICAD-123); mechanizable checks: 22; tables: 9.
