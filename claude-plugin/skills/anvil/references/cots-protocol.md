# COTS Protocol

Module-level part selection — the product analog of the component parts catalog. A drone's
motors, ESCs, battery, camera, and VTX are **selected, not designed**; selecting them badly kills
the product as surely as a bad schematic. Same reuse principle as the schematic protocol's
"vendor reference design over novel topology": design ONLY what the HRS actually owns, buy the
rest — with the selection anchored to datasheet numbers, never to marketing copy.

## The pinned module catalog (`cots/modules.csv`)

The ONLY source system budgets and the product BOM join against (Goodhart guard — refreshing it
is an explicit, logged event, exactly like `catalog/parts-catalog.csv`):

```
module_id,role,mpn,mfr,mass_g,v_min,v_max,i_max_a,protocol,connector,unit_price,currency,stock,lifecycle,distributor,datasheet,accessed,key_specs
MOT-1,propulsion,2207-1750KV,T-Motor,32.1,14.8,25.2,38,DShot,solder-3ph,18.99,USD,214,active,GetFPV,https://…,2026-08-26,"thrust@6S/5in: 1650g @ 34A"
ESC-1,propulsion,F55A-4in1,Diatone,14.2,14.8,25.2,55,DShot600,JST-SH8,54.90,USD,89,active,GetFPV,https://…,2026-08-26,"55A cont / 65A burst"
BAT-1,power,6S-1300-120C,CNHL,205,19.8,25.2,156,DC,XT60,32.50,USD,340,active,RDQ,https://…,2026-08-26,"28.9Wh, 120C"
```

- `key_specs` carries the numbers the budgets consume (thrust @ cell count + prop, capacity Wh,
  C-rating, video power mW) — **transcribed from the datasheet/bench table, with the source URL
  in `datasheet`**. A module with no datasheet-anchored numbers cannot enter a budget row.
- `mass_g` is mandatory — the mass budget sums it; a blank mass is a hard error in
  `product-bom`, not a zero.
- Lifecycle + stock rules match the component catalog: `active`, in stock at ≥ 1 named
  distributor (≥ 2 or an approved alternate for production builds).

## Selection rules

1. **Requirements first:** each module selection traces to the HR-n rows it satisfies; the
   selection rationale (2–3 candidates, pick + why) lives in `arch/architecture.md`, same as a
   topology trade study.
2. **Compatibility is checked, not assumed** — mechanical fit is a fit-class assertion; the
   electrical rows below are seeded as red `system` acceptance rows at selection time:
   - voltage windows overlap across every ICD edge the module sits on
     (`v_min ≤ rail ≤ v_max` at worst case, e.g. 6S fully charged = 25.2 V);
   - source capability ≥ worst-case draw × derate (battery C×Ah vs sum of motor burst);
   - protocol match on every signal edge (DShot600 ESC ↔ FC that emits it; SmartAudio VTX ↔
     free UART);
   - connector mates exist for every `connector` value (or the harness protocol declares the
     adapter wire).
3. **Ecosystem constraints are requirements:** mounting patterns (30.5×30.5 FC grid, 25.5 whoop),
   prop shaft standards, RF band legality (VTX power/band table is region-gated — a human
   sign-off row, the loop can never pass it).
4. **Spares policy:** crash-consumable modules (props, arms-adjacent hardware) get a spare
   quantity column in the product BOM.

## What feeds what

| Consumer | Reads |
|---|---|
| `sys-budget` (mass/power/endurance) | `mass_g`, `key_specs` numbers |
| `product-bom` | `unit_price`, `mass_g`, `distributor`, `stock` |
| `pinout` gate | `connector`, `i_max_a`, `protocol` via the ICD |
| assembly package | module orientation/mounting notes |

A COTS module that appears in the decomposition but not in `cots/modules.csv` — or in the
catalog but in no subsystem — is a red `system` row (orphan check, both directions).
