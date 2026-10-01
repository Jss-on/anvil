# Schematic and electrical verification

Keep the source diffable and reproducible: native `.kicad_sch`, SKiDL, or another selected
authoring flow with pinned tools/libraries. Native KiCad does not require SKiDL or kiutils.
Use hierarchy by function, unambiguous net names, deliberate power and ground topology, visible
decoupling/protection, and source-linked part choices. Follow the actual component datasheet
for unused pins, power flags, grounding, bias, reset/boot states and recommended circuitry.

Before creating connectivity, derive golden assertions from requirements and the ICD: exact
net/pin membership, power/return paths, enable/reset straps, interface direction/voltage, required
protection, sensing and test points. Parse exported netlists where possible; retain substantive
review evidence for properties requiring inspection. A grep hit for a net name is insufficient.

Check footprints against manufacturer drawings, tolerances, pad/pin numbering, exposed-pad
paste/thermal strategy and assembly process. Pin project-local symbol/footprint/model libraries.
For each part stress, record worst-case applied value, actual rating under conditions, ratio,
selected derating criterion and source. Include DC-bias capacitance, temperature/power, ripple,
transients and duty cycle where relevant. No universal 80-percent derating satisfies all parts.

## Wired drawings from a golden netlist

`sch/circuit.json` is the design intent: `{"schema_version": 1, "project", "title", "rev", "parts": [{"ref",
"symbol": "Lib:Name", "value", "footprint", "fields", "unit", "at": [x_mm, y_mm] (optional), "rot", "dnp"}],
"nets": {"NAME": ["R1.1", "U1.4"]}, "power_nets": [...], "pwr_flag": [...], "libraries": {"Nick": "path.kicad_sym"},
"notes": [{"text", "at"}]}`. Omitted coordinates are auto-placed next to the pin each part connects to.
`anvil.py schematic sch/circuit.json pcb/<board>.kicad_sch` vendors the symbols into a project library,
routes every signal net with orthogonal wires (never through pins, nodes or collinear with another net;
crossings only straight through), draws rails with power symbols, names each net with one label, marks
unused pins NC, reloads through KiCad, and fails unless the fresh netlist equals the spec and ERC has no
errors. A link the router cannot draw falls back to a same-name label and is listed in `<board>.wiring.json`
(`wired_fraction`, `unrouted`, `crossings`): improve placement and regenerate until it is 1.0. Render and
view the sheet; readability is part of review. Add a `golden` row to `sch/connectivity.tsv` so hand edits
are re-proven at every gate.

Execute `erc <schematic>` and capture a receipt through `record AUTO-ERC`. KiCad's real JSON
schema, successful execution and all reported findings are checked. Review project rule severity
and exclusions; resolve issues without globally suppressing the class. SKiDL ERC is useful
when SKiDL is used but does not replace checking the actual released KiCad schematic.

Review power budgets/sequencing, pull-ups and bus capacitance, oscillators, decoupling/return
paths, protection, safe defaults, programming/debug, calibration and production-test access.
Export and view every schematic page; retain the render and actual review. ERC does not prove
component values, circuit function, assembly orientation or safety compliance.
