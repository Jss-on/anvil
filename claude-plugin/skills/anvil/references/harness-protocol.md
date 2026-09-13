# Harness and connector control

Derive `harness/harness.tsv` from the released electrical ICD and actual pin definitions.
Required columns: `wire_id`, `icd_id`, `from`, `to`, `awg`, `current_a`, `length_mm`,
`voltage_v`, `protocol`. Endpoints are `module.connector.pin`, with explicit orientation.
Add signal/color, shield/return, routing/strain relief, labels, splice and assembly details.
Use one ICD row per wire mapping. A deliberate splice needs its own explicit terminal/node;
silently duplicating a physical pin is a defect.

`pinout` verifies both endpoints against the ICD, wire gauge, voltage/protocol agreement,
worst-case current against the ICD and qualified path rating, duplicate endpoints, and omitted
electrical mappings. Non-finite/negative quantities are errors. A source document must support
the rating; there is no universal AWG-to-current or two-times-burst rule. Consider connector
contacts, bundling, insulation, temperature, duty cycle, length/drop and protection coordination.

`harness/mates.tsv` identifies actual mating connectors: `mate_id`, `side_a`, `side_b`, `pins`, `pin_ids_a`, `pin_ids_b`,
where pin ID lists are comma-separated and match the declared count. Add vendor series, contact genders/keying, crimp/terminal part numbers and tools. Match the
actual connector pair in the wiring direction. Passing an absent mates file is an error;
product release recording requires the mate definition as an input.

Before G3, review datasheet pin numbering and contact side views, actual netlist membership,
signal direction, current return/shield path, wire/terminal compatibility, polarity, keying,
retention, strain relief, routing and service access. Record continuity/polarity and production
harness-test procedures; validate assembled samples with the intended tooling and fixtures.
Never assume a connector is safe because its pitch, count or family name matches another.
