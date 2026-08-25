# <board> — anvil project layout

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
