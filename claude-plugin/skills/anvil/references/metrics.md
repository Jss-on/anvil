# Scoring CLI

`python scripts/anvil.py` is the implementation; `score-anvil.sh` is its compatibility launcher.
Python 3.10+ standard library only. Metric commands exit 0 for a well-formed observation even
when the measured criterion fails, and 2 for invalid input or tool error. `record` and `gate`
exit 1 for a failing/blocked result, 2 for execution/schema errors. Check both output and exit
status. Never interpret metric exit 0 as a passing release.

| Command | Output | Interpretation |
|---|---|---|
| `pass-rate <ledger>` | `PASS_RATE: n.nn` | Weighted diagnostic; unexecuted rows do not pass |
| `coverage <ledger> <requirements.tsv\|md>` | `REQ_COVERAGE: n.nn` | Exact trace linkage; orphans fail; no release authorization |
| `erc <schematic> [report.json]` | `ERC_VIOLATIONS: n` | Fresh KiCad report; all reported findings count |
| `drc <pcb> [report.json]` | `DRC_VIOLATIONS: n` | Fresh report including parity; matching active project/rules/schematic required |
| `sim <directory>` | `SIM_PASS: passed/assertions` | Every row must pass every declared corner in its own execution |
| `bom-cost <bom.csv> <catalog.csv>` | `BOM_COST: amount CUR` | Exact MPN join, positive integer quantities, one currency |
| `area <pcb>` | `AREA_MM2: amount` | Edge.Cuts bounding box, including curved arc extrema |
| `mesh <stl>` | `MESH_DEFECTS: n` | Facet degeneracy, edge manifoldness and winding; not solid self-intersection proof |
| `fit\|mass\|mech-dfm <directory>` | `FIT_PASS\|MASS_PASS\|DFM_PASS: x/y` | Strict numeric assertion comparison against CAD measures |
| `pinout <wires.tsv> <icd.tsv> [mates.tsv]` | `PINOUT_VIOLATIONS: n` | Exact endpoint, voltage/protocol and approved current/wire agreement |
| `product-bom <csv>` | `PRODUCT_COST: amount CUR` | Source-row price/mass join; mass rollup on stderr |
| `sys-budget <tsv>` | `SYS_BUDGET: x/y` | Nonnegative demand <= positive capability x derate, 0 < derate <= 1 |
| `firmware <release.json>` | `FIRMWARE_RECORD: VALID` | Binary/lock/build/compatibility record consistency |
| `factory <directory>` | `FACTORY_YIELD: x/y first-pass; a/b final` | Unit attempts, configurations, calibration, rework and acceptance policy |
| `commercial <cost-model.csv>` | `PRODUCT_ECONOMICS: amount CUR` | Complete cost categories and pinned assumptions, one currency |
| `init <empty-directory> [selectors]` | `INITIALIZED: ...` | Copies incomplete project templates |
| `plan <project>` | `PLAN: ...` | Reconciles checklist plus project requirements; preserves existing rows |
| `manifest <project>` | `RELEASE_SHA256: ...` | Hashes complete declared release inputs |
| `prepare <project> <id> <files...>` | `REVIEW_DRAFT: ...` | Hashes evidence and prepares an unverified review record |
| `record <project> <id> [--evidence receipt]` | `RECORDED: id status` | Executes built-in check or validates imported review/test evidence |
| `gate <project> [G0..G7\|Sustaining]` | Scoped readiness or `Gx_BLOCKED` | Cumulative unrounded requirement/check/evidence validation |
| `handoff <project> --write <command> [--gate Gx]` | `HANDOFF: VALID` | Writes and validates current verdict and blockers |
| `handoff <handoff.json>` | `HANDOFF: VALID\|INVALID` | Recomputes claimed gate and verifies hashes |
| `verdict [project]` | G3 result; `FAB_BLOCKED` for legacy input | Migration alias; old TSV-only green verdicts removed |

Diagnostics retain `ANVIL_W_<DIMENSION>`, `ELECTRICAL_GATE_CAP`, and `ANVIL_RESULTS` settings.
These do not influence the release checker. Missing required dimensions/checks cannot be
compensated by documentation weight. Standard comparison operators: `le`, `lt`, `ge`, `gt`,
`eq`, `within`; the latter accepts `center±absolute` or `center±percent%` (also `+/-`).
All numeric inputs must be finite; quantities, currents, capacities and mass have semantic bounds.

Simulation and budget margins are emitted per row/corner on stderr. For optimization compare
the minimum normalized margin against its own baseline and physical units. Do not add margins
in different units or average away a failing corner. Catalog refreshes, spec changes and rule
changes are controlled baseline changes, not optimization wins.

See `evidence-protocol.md` for schema and trust boundaries. Every output label describes only
the checker named; file existence or a metric alone is insufficient for product release.
