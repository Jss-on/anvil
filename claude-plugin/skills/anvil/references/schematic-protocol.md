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

## Sheet & naming conventions (clarity over compactness)

- **Hierarchy by function**, not location: power on one sheet/block, MCU on another, comms per
  interface. Flat is acceptable ≤ 2 sheets; beyond that, hierarchical sheets are the reuse and
  review unit. Signal flow left→right, top→bottom; inputs enter left, outputs exit right.
- **Reference designators** per IEEE 315 / ASME Y14.44 class letters (R, C, L, U, D, Q, K, J,
  TP…) — one letter class per component type, no local inventions.
- **Net labels are scoped deliberately**: local for same-sheet, hierarchical/global for
  cross-sheet. Never short generics (`EN`, `OUT`, `CLK`) that invite silent collisions — prefix
  by block (`BUCK_EN`, `MCU_SWCLK`).
- **Power ports** (+3V3/+5V/GND symbols), never power wires dragged across the sheet. Mixed-signal:
  distinct AGND/DGND symbols with the single join point drawn explicitly (per the converter
  datasheet — a DGND *pin name* does not mandate a separate system digital plane).
- Decoupling caps drawn **adjacent to their IC** in the same block — visible, never "assumed";
  intent must survive the trip to layout.

## Footprints & land patterns (IPC-7351)

- Land patterns to **IPC-7351 density Level B (Nominal)** by default; Level A for hand-soldered /
  high-rel boards, Level C only with the assembler's written confirmation (see `standards.md`).
- Every footprint verified against the **datasheet's recommended pattern** before first use;
  project-local pinned libraries over global mutable ones. A wrong pattern is the
  tombstone/bridge/open defect class — caught here or at bring-up, nowhere between.
- Thermal-pad footprints carry their paste/via strategy (segmented stencil intent noted for
  uncapped via farms — the fab protocol's stencil rule consumes it).

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
- **Obsolescence is quiet**: > 50 % of recent discontinuations shipped with NO PCN
  (`standards.md`) — lifecycle is re-checked at every explicit catalog refresh, never assumed
  from silence. A PCN/LTB on a catalog part (~6-month buy window) is a drop-everything GitHub
  issue; the substitution enters through the normal loop (derating + affected sims re-verified).
- Multi-sourced, widely-used parts over exotic singles; note the drop-in FFF alternate for each
  keystone part in `arch/architecture.md` — designing the alternate in NOW is what makes the
  future substitution a catalog edit instead of a respin.
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
- [ ] Debug/DFT access: SWD/JTAG header or TC pads on every MCU/FPGA; boundary-scan
      (IEEE 1149.1) parts preferred where BGAs hide joints, scan-chain order documented.
- [ ] Unused gates/pins terminated per datasheet.
- [ ] Net names: rails as `+3V3`/`+5V`/`GND`, signals functional (`UART_TX`), never `Net-(R5-Pad1)`
      on anything a human will probe.

## Evidence

Export `kicad-cli sch export pdf` and **VIEW every page** (Read the PDF). Store at
`docs/renders/sch-<rev>.pdf`. The gate row cites it. Unviewed exports are not evidence — viewing
catches the crossed-wire and missing-junction class ERC cannot.
