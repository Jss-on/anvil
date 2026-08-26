# System Protocol

The contract that turns anvil from a board factory into a product factory. A product — a rugged
FPV drone, a handheld instrument, a sensor node — is custom PCBs **plus** COTS modules, mechanical
parts, and the wiring between them. This protocol owns the decomposition and every interface;
`cots-protocol.md`, `mechanical-protocol.md`, `harness-protocol.md`, and `assembly-protocol.md`
own the tracks it fans out to.

## Product decomposition (`system/decomposition.md`)

Break the product into a **subsystem registry** — every physical thing that ends up in the
assembled unit belongs to exactly one subsystem:

```
id	subsystem	kind	realization	owns
S-1	flight-controller	electronics	custom-pcb boards/fc/	IMU, MCU, sensor fusion
S-2	propulsion	cots	cots/modules.csv: MOT-*, ESC-1	thrust
S-3	power	cots+harness	BAT-1, PDB path	energy storage + distribution
S-4	airframe	mechanical	mech/cad/frame.py	structure, crash loads
S-5	video	cots	CAM-1, VTX-1	FPV link
```

`kind ∈ electronics|cots|mechanical|harness|firmware`. `realization` points at the artifact that
builds it (a `boards/<n>/` tree, a COTS catalog id, a `mech/cad/` source). A part with no
subsystem, or a subsystem with no realization, is a red `system` row.

## Interface Control Document — the ICD (`system/icd.tsv`)

Every connection **between subsystems** is an ICD row — the system-level analog of a net:

```
icd_id	from	to	kind	connector	pins	v_nom	i_max_a	protocol	traces
ICD-1	S-3	S-2	power	XT60 → ESC pads	2	14.8	60	DC	HR-3
ICD-2	S-1	S-2	signal	JST-SH 8p	8	3.3	0.1	DShot600	HR-5
ICD-3	S-1	S-5	signal	JST-GH 6p	6	5.0	0.8	analog+SmartAudio	HR-7
ICD-4	S-4	S-1	mechanical	M3 × 4 on 30.5mm grid	-	-	-	TPU isolated	HR-12
```

`kind ∈ power|signal|rf|mechanical|thermal`. Rules:

- Every subsystem pair that touches (electrically, mechanically, thermally) has **exactly one**
  ICD row per distinct interface — no implicit connections.
- Every `power|signal` ICD row is realized by ≥ 1 wiring-harness row or a board-to-board
  connector (checked by the `pinout` gate).
- Every `mechanical` ICD row is realized by a fit-class assertion in `mech/assertions.tsv`
  (checked by the `fit` gate).
- Voltage/current columns are worst-case, and feed the harness ampacity check and the system
  budgets.
- Each ICD row traces → HR-n; the RTM runs through the ICD, not around it.

## System golden cases

Seed as red `system` acceptance rows at architecture time (the product analog of connectivity
goldens): every subsystem reachable from the power source through ICD rows; every ICD row
realized (harness row, board connector, or fit assertion); no orphan module in the COTS catalog;
every firmware-kind subsystem has a config artifact in `assembly/`.

## System budgets (`system/budgets.tsv`)

Product-level budgets that must CLOSE, evaluated by `score-anvil.sh sys-budget`:

```
budget_id	quantity	worst_demand	capability	derate	units	traces
B-1	mass	AUW: sum(product-bom mass_g)	thrust × 4	0.5	g	HR-2
B-2	power	hover current draw	battery C × Ah	0.8	A	HR-3
B-3	endurance	target flight time	Wh / hover W	1.0	min	HR-4
B-4	cost	product-bom rollup	budget @ qty	1.0	USD	HR-8
```

`demand ≤ capability × derate` or the row is red. Demands and capabilities are **numbers pulled
from the pinned COTS catalog, the product BOM, and measures.json** — a budget hand-waved from
memory is self-certification. Thrust-to-weight, hover draw, and endurance are arithmetic over
datasheet-anchored module specs (motor thrust table @ prop + cell count, battery Wh), shown in
`system/budgets.md` with the formula visible.

## Multi-board orchestration

Each custom PCB is its own `boards/<name>/` tree running the full electronics pipeline
(HRS slice → schematic → sim → layout → fab) with its own `anvil-results.tsv`; the product's
ledger aggregates them. Board-to-board interfaces are ICD rows, so parity is checked at both
ends: the board's netlist must expose exactly the connector the ICD declares (`pinout` gate).

## Verification summary

| Claim | Gate |
|---|---|
| decomposition complete, every part owned | `system` golden rows in the ledger |
| every electrical interface realized + within ampacity | `score-anvil.sh pinout` |
| every mechanical interface realized + clearances hold | `score-anvil.sh fit` |
| budgets close (mass/power/endurance/cost) | `score-anvil.sh sys-budget` |
| everything in the unit is priced + sourced | `score-anvil.sh product-bom` |
