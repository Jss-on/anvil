# System architecture and integration

At G2 allocate user functions and risk controls to electronics, firmware, mechanics, COTS,
cloud and manufacturing/service responsibilities. Define subsystem boundaries, each board or
module's realization, datums, power tree, data paths, safety states and operating modes.
List unknowns with experiment, owner and closure criterion. Architecture is not closed while
a high-risk feasibility assumption has no disposition.

## Interface control

`system/icd.tsv` uses one row per physical electrical connection, with exact
`module.connector.pin` endpoints. Required fields for the checker: `icd_id`, `from`, `to`,
`kind`, `i_max_a`, `ampacity_a`, `awg`, `voltage_v`, `protocol`, `rating_source`.
`kind` is power or signal for harness rows; mechanical interfaces are controlled separately.
Add connector/pin type, direction, shield/return, timing, allowable ranges, firmware ownership,
protection and trace IDs as needed. `i_max_a` is the approved worst-case current limit,
`ampacity_a` the qualified continuous path limit under declared conditions. `rating_source`
is a file relative to the ICD, containing the actual wire/connector rating and assumptions.

Both endpoints must agree with schematics/exported netlists, connector vendor drawings,
firmware assignments and assembly orientation. The pinout checker checks structured agreement;
HW-008/HW-015 review the source derivation, pin membership, direction and engineering meaning.
Subsystem-level labels such as `S-1 -> S-2` cannot substitute for actual pin mappings.

## Budgets

`system/budgets.tsv`: `id` (legacy `budget_id` accepted for diagnostics), `quantity`,
`worst_demand`, `capability`, `derate`, `units`, `traces`, `demand_source`, `capability_source`.
Budget source references use `relative.json#dotted.key`, selecting an object such as
`{"value": 610, "units": "g"}`. The checker compares both value and units; show work
for aggregation, tolerances, covariance, duty cycle, conversion efficiency and environmental
conditions. No live web value, freeform "AUW", or negative quantity may enter numeric fields.

Close mass, power/current, thermal, timing/bandwidth, memory/CPU, energy/endurance, cost and
resource budgets appropriate to the product. Use compatible units for demand and capability.
`sys-budget` evaluates demand <= capability x derate with 0 < derate <= 1. A value of 80
is not 80 percent. Where a different inequality or coupled equation is needed, express it as
an explicit project requirement and reviewed calculation rather than forcing an invalid budget.

## Integration review

For every variant, check board/harness/mechanical/firmware revision compatibility, interface
voltage and direction, sequencing, protection, test access and calibrated units. Reconcile the
system mass/cost rollup with actual assemblies and source catalogs. Identify who owns each
interface and who integrates the final installation. Record physical integration evidence in
EVT and validate intended operation and failure states in DVT; a passing board DRC proves
neither system compatibility nor installation safety.
