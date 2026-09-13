# Anvil project

These templates start unverified. Fill the actual product profile, `hardware_revision`,
requirements, artifact paths and check arrays before running `plan`. Never treat empty rows
or placeholder values as completed evidence. Resolve the Anvil executable from the installed
plugin; this project does not contain its scripts.

| Path | Purpose |
|---|---|
| `anvil-project.json` | Scope, sectors, destinations, features, requirements, controlled artifacts and check commands |
| `hrs/requirements.tsv` | Stable requirements, objective criteria, conditions, methods, due gates and owners |
| `lifecycle-checks.csv` | Reference copy of the 75 research items plus early planning checkpoints; the installed catalog controls gates |
| `pcb/rules/` | Starter deck; copy to `<board>.kicad_dru` beside the actual PCB/project/schematic to activate |
| `sim/assertions.tsv` | Exact harness, measure, comparison, units, corners and requirement traces |
| `system/`, `harness/` | Physical interface endpoints, sourced budgets, wires and explicit mating pin definitions |
| `bom/`, `catalog/` | Exact source joins for product cost/mass, including mechanical and COTS parts |
| `mech/` | CAD-derived measurements and fit/mass/process assertions |
| `firmware/` | Controlled source/build/dependencies/binary and compatibility/security records |
| `manufacturing/` | Control plan, pilot acceptance and per-unit test/provisioning/rework records |
| `compliance/` | SKU/destination applicability, dates, route, evidence and responsible owners |
| `commercial/` | Complete cost model and sourced assumptions for commercial review |
| `sustaining/` | Configuration changes, field/production incidents, support and retirement evidence |
| `evidence/` | Actual tool receipts and imported reviewed/external records |

Add the actual schematics/PCBs, libraries/models, firmware/CAD sources, controlled drawings,
fabrication/assembly exports, reports and procedures under these or other explicit paths.
Every release dependency enters `artifacts`; manifest files use portable relative paths.
Prepare G0 opportunity, G1 requirements and G2 architecture reviews before G3 prototype release.
Continue through G4 EVT, G5 DVT, G6 PVT, G7 market release and sustaining as the target requires.

```sh
python /installed/anvil/scripts/anvil.py plan .
python /installed/anvil/scripts/anvil.py manifest .
python /installed/anvil/scripts/anvil.py record . AUTO-ERC
python /installed/anvil/scripts/anvil.py gate . G3
python /installed/anvil/scripts/anvil.py handoff . --write build --gate G3
```

Use the installed lifecycle/evidence protocols to populate review receipts. Physical tests and
approvals must be real; templates contain no fabricated measurements or approvals. Changing a
release file invalidates G3+ evidence. A blocked gate identifies unfinished work, not permission
to drop its requirements.
