# Schematic Protocol

Contract for `build` Phase 5. Governs how netlists are authored, gated, and reviewed.

## Netlist as code (non-negotiable)

The schematic's source of truth is a **text artifact** the loop can diff, revert, and regenerate:
1. **SKiDL** (default) — `sch/netlist.py`, python; `generate_netlist()` emits a KiCad netlist.
   SKiDL's own `ERC()` runs as a free pre-gate before KiCad's.
2. **atopile** — `.ato` source compiled to a KiCad board, when the project opts in.
3. **Native `.kicad_sch`** — accepted (it IS s-expression text); edit via kiutils or careful
   surgery; never via untracked GUI-only state.
Binary-only or un-diffable schematic state fails the phase gate.

## Connectivity-TDD (goldens first)

Golden connectivity cases derive from the block diagram (build Phase 4) and are `electrical`
must-pass rows seeded RED before the netlist exists:
- Every block-diagram edge exists as a net between the named pins.
- Every IC power pin has its decoupling cap on the same net, declared in the same block.
- Every enable/reset/boot strap pin is deliberately driven or strapped — floating = red.
- Every off-board signal passes through its declared protection (ESD array, series R) before the
  connector.
Verification: mechanical where possible (grep/parse the exported netlist for the net + pin
membership), inspection with evidence path otherwise. Then build one block per iteration to green.

## ERC discipline

```
kicad-cli sch erc --format json --severity-error --exit-code-violations -o erc.json <sch>
```
`scripts/score-anvil.sh erc <sch>` wraps this → `ERC_VIOLATIONS: N`. Gate: **0**.
- Warnings are triaged: each either fixed or suppressed with an in-schematic exclusion + one-line
  reason. Blanket suppression is a defect.
- SKiDL flows: run SKiDL `ERC()` first (catches unconnected pins pre-export), KiCad ERC remains
  the gate of record.
- Power flags: every power net driven by exactly one PWR_FLAG/source; ERC's
  "input never driven" class is never globally silenced.

## Derating table (`sch/derating.md`)

Every part with a stress rating gets a row: `ref | mpn | stress kind | worst-case applied |
rating | ratio`. Policy: ratio ≤ 0.80 (voltage, current, power), ≤ 0.70 for aluminum electrolytic
ripple current and anything in the hot zone. Ceramic caps: applied voltage vs DC-bias-derated
capacitance — the CAPACITANCE at bias must satisfy the circuit, not the label value. Any ratio
over policy = `electrical` red row. Worst-case applied values come from the power budget and sim
corners, not typicals.

## Part selection rules (with Phase 4)

- Lifecycle: active — never NRND/EOL without explicit user waiver.
- Availability: in stock at ≥2 major distributors OR an approved drop-in second source captured
  in the catalog.
- The **pinned catalog** (`catalog/parts-catalog.csv`) is written when a part is chosen:
  `mpn,description,qty,unit_price,currency,stock,lifecycle,distributor,accessed`. `bom-cost`
  joins ONLY against it. Refreshing prices/stock is an explicit logged event, never a mid-loop
  side effect.
- Prefer the datasheet reference circuit; cite `datasheet §x.y` in a schematic note per block.

## Design-review checklist (gate, evidence path per row)

- [ ] I²C pull-ups present, one set per bus, value justified for bus capacitance/speed.
- [ ] MCU boot/strap pins at documented levels through reset.
- [ ] Crystal load caps computed from CL spec (show work), not copied.
- [ ] Bypass: bulk per rail entry + 100 nF per power pin, noted for at-pin placement.
- [ ] Series termination/level shift on every cross-domain signal.
- [ ] Connector ESD + labeled pinout table on the sheet.
- [ ] Test points: every rail, GND ≥2, key signals (feedback, clocks, comms) — as real TP
      footprints.
- [ ] Unused gates/pins terminated per datasheet.
- [ ] Net names: rails as `+3V3`/`+5V`/`GND`, signals functional (`UART_TX`), never `Net-(R5-Pad1)`
      on anything a human will probe.

## Evidence

Export `kicad-cli sch export pdf` and **VIEW every page** (Read the PDF). Store at
`docs/renders/sch-<rev>.pdf`. The gate row cites it. Unviewed exports are not evidence — viewing
catches the crossed-wire and missing-junction class ERC cannot.
