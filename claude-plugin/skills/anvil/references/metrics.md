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
| `connectivity <sch> <assertions.tsv>` | `CONNECTIVITY: x/y` | Fresh netlist; kinds equals/contains/excludes/connected/isolated/count/decoupled/no_floating/series/pin_type/golden |
| `rules <design-dir>` | `RULES: x/y` | `rules.tsv`: id, check, inputs (k=v;...), op, limit, units, traces, source; margins in transcript |
| `calc <check> k=v...` | value + citation | Exploratory calculation from `anvil_rules.py`; no evidence |
| `schematic <circuit.json> <out.kicad_sch>` | `SCHEMATIC: ... netlist MATCH` | Wired drawing; KiCad reload, netlist == spec, ERC; exit 1 on mismatch/ERC errors; `<out>.wiring.json` |
| `schematic-spec <sch> <circuit.json>` | `CIRCUIT_SPEC: ...` | Golden spec from an existing drawing (symbols from its embedded library) |
| `wiring <sch> <dir>` | `WIRING: ...` | `netlist.xml`, `wiring.md` net/part tables, `wiring.dot` |
| `plots <project> [--sim dir]` | `PLOTS: n` + margin chart | `sim/plots.tsv`: id, circuit, corners, vectors, x, title, traces; needs matplotlib |
| `renders <project>` | `RENDERS: n` | Schematic SVG/PDF, PCB front/back SVG, 3D PNG, stats; `audit/renders/commands.json` |
| `fabpack <pcb> <dir>` | `FABPACK: n files` | Gerber X2, drill+map, placement CSV, IPC-2581, IPC-D-356, STEP; hashes in `fabpack.json` |
| `log <project> iteration\|decision\|research k=v...` | `LOGGED: ...` | Appends `audit/<ledger>s.tsv`; unknown columns rejected |
| `report <project> [--gate Gx]` | `AUDIT: ...` | `audit/AUDIT.md`, `audit.json`, `audit/paper/paper.tex` + `refs.bib`; quotes the gate, never decides it |
| `board <sch> <template.kicad_pcb> <out> [--placement tsv]` | `BOARD: n footprints, m nets` | Fresh netlist onto the template (stackup/outline/rules); unplaced parts shelf-packed |
| `place <pcb> <placement.tsv>` | `PLACED: n` | ref, x_mm, y_mm, rot_deg, side (F/B); zones refilled |
| `route <pcb> <out> [--passes n]` | `ROUTED: ...; DRC_VIOLATIONS: n` | Freerouting on a copy (DSN/SES via pcbnew), refill, fresh DRC; exit 1 on violations |
| `layout <pcb> <design-dir>` | `LAYOUT: x/y` | `nets.tsv` (+`rf.tsv`): IPC-2152, IPC-2221, Z0/Zdiff, return path, length/match, RF fence/stitching/keep-out |
| `si <pcb> <design-dir>` | `SI: x/y` | `si.tsv`: overshoot/ringback/delay/settle per receiver; `analysis/si/*.cir`, `*.png` |
| `pdn <pcb> <design-dir>` | `PDN: x/y` | `pdn.tsv` (+`caps.tsv`): worst |Z| f_min..f_max vs Z_target; per-cap L breakdown; `analysis/pdn/*.png` |
| `thermal <pcb> <design-dir>` | `THERMAL: x/y` | `thermal.tsv`: Tj per part, energy balance; `analysis/thermal/thermal.png` |
| `em <pcb> <design-dir>` | `EM: x/y` | `em.tsv`: openEMS S-parameters, `analysis/em/<name>.s<n>p/.png/.xml`; one `<name>:settled` row per network (dropping the last 10 % of the run moves no checked S by more than 0.01); minutes per port |
| `sparams <design-dir>` | `SPARAMS: x/y` | `sparams.tsv`: same `S11<=-10@f1:f2` limits on measured Touchstone files |
| `emc <pcb> <design-dir>` | `EMC_ESTIMATE: x/y` | `emc.tsv`: dB over the FCC/CISPR line per net (estimate, ±10 dB); `analysis/emc/*.png` |

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
