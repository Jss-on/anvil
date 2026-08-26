# <board|product> — anvil project layout

Board build: the tree below at repo root. **Product build** (end-to-end unit): each custom PCB
lives in `boards/<name>/` with this same tree, plus the product tracks beside them:

```
boards/<name>/             one full board tree (below) per custom PCB
system/decomposition.md    P-P1 — subsystem registry (every part owned exactly once)
system/icd.tsv             P-P1 — interface control: icd_id from to kind connector pins v_nom i_max_a protocol traces
system/budgets.tsv         P-P1 — budget_id quantity worst_demand capability derate units traces (+ budgets.md formulas)
cots/modules.csv           P-P1 — pinned module catalog (datasheet-anchored key_specs, mass_g, price, stock)
mech/cad/*.py              P-P2 — CAD-as-code sources; mech/build/ STL+STEP; mech/measures.json
mech/assertions.tsv        P-P2 — id class(fit|mass|dfm) measure op limit units traces
mech/renders/              P-P2 — section + exploded renders (VIEWED evidence)
harness/harness.tsv        P-P3 — wire_id icd_id from to signal awg length_mm current_a color notes
harness/mates.tsv          P-P3 — connector mate table
product-bom.csv            P-P4 — item_id category qty unit_price currency mass_g mpn source (full unit + spares)
assembly/                  P-P4 — ASSEMBLY.md, INTEGRATION.md, config/, QC.md, exploded.png
```

Board tree:

```
charter.md                 P1 — objectives, in/out scope, iteration budget, risk register (+ GO/NO-GO)
hrs/requirements.md        P3 — HRS: HR-n, value + unit + tolerance + conditions + verify method
arch/architecture.md       P4 — block diagram (mermaid), power budget, interface map, trade study
catalog/parts-catalog.csv  P4 — pinned snapshot: mpn,description,qty,unit_price,currency,stock,lifecycle,distributor,accessed
sch/                       P5 — netlist source (SKiDL .py / .ato / .kicad_sch), erc.json, derating.md
sim/                       P6 — *.cir harnesses, models/ (with provenance headers), assertions.tsv
pcb/<board>.kicad_pcb      P7 — board; pcb/rules/<fab>.kicad_dru rule deck; drc.json
fab/                       P8 — gerbers/, bom.csv, cpl.csv, DFM-REPORT.md
docs/                      P8 — SIM-REPORT.md, TEST-PLAN.md, BRINGUP.md, renders/ (VIEWED evidence)
anvil-results.tsv          acceptance ledger: n dimension assertion status weight evidence traces
iterations.tsv             loop ledger: n timestamp phase change dimension result pass_rate notes
handoff.json               chain contract
```

Gates (run from the board dir; scripts resolve per SKILL.md):

```bash
bash scripts/score-anvil.sh erc  sch/<board>.kicad_sch     # ERC_VIOLATIONS: 0
bash scripts/score-anvil.sh sim  sim/                      # SIM_PASS: y/y
bash scripts/score-anvil.sh drc  pcb/<board>.kicad_pcb     # DRC_VIOLATIONS: 0
bash scripts/score-anvil.sh area pcb/<board>.kicad_pcb     # AREA_MM2 vs target
bash scripts/score-anvil.sh bom-cost fab/bom.csv catalog/parts-catalog.csv
bash scripts/score-anvil.sh pass-rate anvil-results.tsv
bash scripts/score-anvil.sh verdict anvil-results.tsv hrs/requirements.md
```

Product gates (from the product root):

```bash
bash scripts/score-anvil.sh mesh mech/build/<part>.stl          # MESH_DEFECTS: 0
bash scripts/score-anvil.sh fit  mech/                          # FIT_PASS: y/y
bash scripts/score-anvil.sh mass mech/                          # MASS_PASS: y/y
bash scripts/score-anvil.sh mech-dfm mech/                      # DFM_PASS: y/y (PRUSA_SLICER arms slicer seam)
bash scripts/score-anvil.sh pinout harness/harness.tsv system/icd.tsv harness/mates.tsv
bash scripts/score-anvil.sh product-bom product-bom.csv         # PRODUCT_COST vs target
bash scripts/score-anvil.sh sys-budget system/budgets.tsv       # SYS_BUDGET: y/y — budgets CLOSE
```
