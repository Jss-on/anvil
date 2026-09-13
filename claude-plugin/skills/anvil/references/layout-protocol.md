# Layout and active design rules

Start with the actual manufacturer stackup, material/process capability, mechanical datums,
connector positions, mounting and envelope constraints. Fix mechanical contracts before routing.
Choose layer count and reference planes from signal/power integrity and EMC requirements.
Control return paths and power-loop area; justify any split reference plane against actual
device and interface requirements. Use the fabricator's dielectric/geometry for impedance.

## Rules that KiCad actually loads

For `pcb/controller.kicad_pcb`, place the active rules at `pcb/controller.kicad_dru`, with
`pcb/controller.kicad_pro` and `pcb/controller.kicad_sch`. A deck stored only in
`pcb/rules/vendor.kicad_dru` is inactive. Copy the reviewed starter deck to the matching path,
configure board settings consistently, and add all four files to the release manifest.
The supplied JLCPCB two-layer example needs current supplier review before use; other
manufacturers require their own explicit rule setup.

Route critical power/switching loops, feedback/sensing, clocks and interfaces with datasheet
constraints. Control references, impedance/skew, noise coupling, decoupling loop inductance,
thermal spreading and connector protection. Size conductors and vias for current, temperature,
copper, stackup and duty cycle. Derive insulation/creepage/clearance from applicable product
safety standards and installation conditions, not a generic voltage lookup table.

Review manufacturability: pad/trace geometry, soldermask web, paste, thermal vias, annular rings,
silkscreen/polarity, placement orientation, fiducials, tooling and panel constraints. Confirm
assembly access, enclosure/connector fit and component height. An autorouter does not change
the acceptance requirements; rerun verification after any imported routing or zone change.

`drc <pcb>` runs fresh KiCad DRC with schematic parity and all reported severities. Its source
siblings must exist, the run must succeed, and the report must contain the expected groups.
Record the execution using `AUTO-DRC`; multi-board recording covers the manifested board list.
Review and refill copper zones with the selected KiCad workflow before export; do not silently
save/refill a released board while measuring an unchanged baseline.

`area <pcb>` computes the enclosing Edge.Cuts rectangle, including cardinal extrema of arcs
and circles. It is not the polygon area or proof of a closed/manufacturable outline. Unsupported
outline primitives and footprint-local cuts fail explicitly rather than underestimate size.
Export and view top/bottom and assembly renders; inspect every intended fabrication layer.
