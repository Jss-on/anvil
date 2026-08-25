# Metrics Contract

The scoring spine. Everything here is mechanical; nothing here is impressions.

## anvil-results.tsv (7 tab-separated columns)

```
n	dimension	assertion	status	weight	evidence	traces
1	electrical	ERC violations == 0	pass	1.0	evidence:sch/erc.json	HR-1
2	electrical	VBUS reaches U1.VIN via F1,D1	pass	1.0	evidence:sch/netlist.net	HR-3
3	simulation	A-HR-2 ripple ≤30mV @ corners	fail	1.0	evidence:sim/A-HR-2.log	HR-2
```
`status ∈ pass|fail|skip` (skip = not applicable, excluded from scoring — never a parking lot for
hard rows). `weight` scales within the dimension. `evidence:` is a repo-relative path — a row
without evidence is `fail` by definition. `traces` = comma-joined HR-n (the RTM).

## Dimensions & weights (renormalized over dims that ran)

| Dimension | Weight | Owns |
|---|---|---|
| `electrical` | 0.30 | ERC=0 · connectivity goldens · derating table · power budget closes |
| `simulation` | 0.25 | every simulable HRS spec at corners, margins recorded |
| `layout` | 0.20 | DRC=0 incl. parity + fab deck · critical-net constraints · area target |
| `manufacturing` | 0.15 | package complete · DFM report · catalog lifecycle/stock · BOM cost ≤ target |
| `testability` | 0.10 | test points as footprints · bring-up plan · safe power-up defaults |
| `documentation` | 0.10 | schematic PDF viewed · renders viewed · model provenance · README · RTM |

**ELECTRICAL GATE:** while ANY `electrical` row is red, headline pass-rate is capped at
`ELECTRICAL_GATE_CAP` (default 0.50). Wrong electricity cannot be polished over.

## score-anvil.sh surface

| Subcommand | Emits (stdout, one line) | Notes |
|---|---|---|
| `pass-rate [tsv]` | `PASS_RATE: 0.NN` | per-dim breakdown → stderr |
| `coverage [tsv] [hrs]` | `REQ_COVERAGE: 0.NN` | every HR-n traced ≥1 row; orphans listed → stderr |
| `erc <sch>` | `ERC_VIOLATIONS: N` | kicad-cli JSON, severity error |
| `drc <pcb>` | `DRC_VIOLATIONS: N` | incl. `--schematic-parity` + rule deck |
| `sim <dir>` | `SIM_PASS: x/y` | per-row PASS/FAIL + margin → stderr |
| `bom-cost <bom> <catalog>` | `BOM_COST: X.XX CUR` | pinned-catalog join; missing MPN = hard error |
| `area <pcb>` | `AREA_MM2: N` | Edge.Cuts bbox |
| `verdict [tsv]` | `FAB_READY` \| `FAB_BLOCKED` | all must-pass green ∧ rate ≥ target ∧ coverage 1.00 |

All: exit 0 on well-formed input (a red baseline is valid data); exit 2 on hard error only.

## Optimization metrics (the `improve` loop)

| Metric | Direction | Source | Guard |
|---|---|---|---|
| `bom_cost` | minimize | `bom-cost` (pinned catalog) | catalog refresh = explicit logged event |
| `board_area` | minimize | `area` | HRS-pinned mechanics immutable |
| `part_count` | minimize | distinct BOM lines | redundancy proven by sim, not intuition |
| `worst_case_margin` | maximize | min margin across `sim` rows | **maximin** — never the average |

Hard ratchet under every metric: ERC=0 ∧ DRC=0 ∧ all sim assertions pass ∧ no margin below
`Floor × baseline` ∧ derating green. Gates are never tradeable for metric.

## Goodhart guards (why these metrics are "correct")

1. **Tool JSON only** — violation counts parsed from kicad-cli output, never self-reported.
2. **Worst corner, not typical** — a spec's margin is its worst corner's distance to the limit.
3. **Pinned snapshots** — parts catalog + fab deck carry accessed dates; refresh is explicit.
4. **Maximin margins** — averaging margins lets one spec ride the cliff.
5. **Evidence or fail** — a row without a readable evidence path is red.
6. **Viewed renders** — image evidence must actually be Read; export ≠ evidence.
7. **Verification-ladder audit** — `verify:` method downgrades only with a logged reason, and the
   convergence audit re-checks every HR against its evidence class.
