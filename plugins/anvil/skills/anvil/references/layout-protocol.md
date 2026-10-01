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

## Board truth loop

1. `board <sch> <template.kicad_pcb> <pcb>`: the template carries the fabricator stackup (Board Setup, with
   thickness/εr/loss tangent per dielectric), outline, zones and rules; footprints and nets come from a fresh
   netlist. `design/placement.tsv` places parts (unlisted parts are shelf-packed inside the outline).
2. `route <pcb> <routed.kicad_pcb>`: Freerouting on a copy, SES import, zone refill, DRC. Freerouting sees
   only what Specctra DSN carries (net-class widths/clearances, keepouts), not custom `.kicad_dru` rules:
   separate mains/isolation groups by placement and net classes, then let DRC enforce the custom rules.
   Hand-route or fix critical nets (RF, switching loops, pairs) in KiCad; the checks below judge the
   result either way.
3. Verify on the copper, each a margin row in the transcript:
   - `layout`: IPC-2152 heating (Brooks/Adam fits) and via groups; IPC-2221 Table 6-1 spacing to every
     neighbour (B1 inner, B2 outer unless `condition`); Z0/Zdiff from the 2-D field solver of the real
     stackup, mask and measured coplanar gaps per side; return-plane continuity; length match; RF fence
     pitch ≤ λ_eff/10 (ARCH-065), same-layer pour stitched ≤ λ_eff/20 (WILLIAMS-2038), matching-part
     distance, antenna keep-out rule areas.
   - `si`: lossless field-solved lines (conservative for ringing, optimistic for long lossy channels);
     linear driver/receiver; via stubs 5 fF/mil (BOGATIN-286).
   - `pdn`: non-interacting capacitor branches (BOGATIN-2130): body ESL/ESR (ARCH-067), pad-to-via path
     inductance (field solver), via pair (BOGATIN-2132), cavity spreading (BOGATIN-2135), plane C
     (BOGATIN-2147), VRM R+L; clustered capacitors that share spreading paths make it optimistic.
   - `thermal`: layered conduction with real copper coverage and via barrels, still-air convection; datasheet
     θjb to the junction. Validate hot parts with a thermocouple/IR at EVT.
   - `em`: openEMS FDTD, PEC copper with thickness, dielectric loss exact at f_stop, thirds-rule mesh on
     RF edges, lumped ports where the pin enters each port pad (to the plane below, or across the coplanar gaps
     over a launch cut-out); capacitors as series ESR-ESL-C, inductors with the ESR of their Q (`l_q`, default
     50); conductor loss, mask, component bodies and
     connectors are not modelled. A `settled` row proves the run was long enough. Only the row's nets, its `ref_net` and its listed parts are modelled:
     another net's copper (a power plane between grounds) has no decoupling in the model and rings as a
     lossless resonator, so list every part that terminates a net you include (bias resistors, bypass
     capacitors). Minutes per port: run at sign-off. Measure with a VNA (`sparams`).
   - `emc`: loop area × trapezoid harmonics (Paul) vs FCC/CISPR limit lines with a 6 dB design margin;
     ±10 dB estimate; cable common mode needs a measured or budgeted CM current.
4. Change placement/routing/stackup, re-run, keep or discard (log each iteration), then `drc`, `fabpack`.

`area <pcb>` computes the enclosing Edge.Cuts rectangle, including cardinal extrema of arcs
and circles. It is not the polygon area or proof of a closed/manufacturable outline. Unsupported
outline primitives and footprint-local cuts fail explicitly rather than underestimate size.
Export and view top/bottom and assembly renders; inspect every intended fabrication layer.
