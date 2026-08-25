# Fab Protocol (DFM + output package)

Contract for `build` Phase 8 and the `manufacturing` dimension. Terminal deliverable: a package a
fab accepts on first upload. **Ordering is always the human's move.**

## The package (`fab/`)

| Artifact | Command | Gate |
|---|---|---|
| Gerbers | `kicad-cli pcb export gerbers -o fab/gerbers/ <pcb>` | layer set complete for the stackup (copper, mask, silk, paste, Edge.Cuts) |
| Drill | `kicad-cli pcb export drill -o fab/gerbers/ --format excellon <pcb>` | present; PTH/NPTH separated per fab preset |
| BOM | `kicad-cli sch export bom -o fab/bom.csv --fields "Reference,Value,Footprint,MPN,Qty" --group-by MPN <sch>` | every line has an MPN that exists in the pinned catalog; no DNP ambiguity (DNP column explicit) |
| CPL | `kicad-cli pcb export pos -o fab/cpl.csv --format csv --units mm --side both <pcb>` | present when assembly is in scope; rotation sanity-checked on polarized parts |
| DFM report | authored | see below |

Zip nothing until the user asks; fabs differ on packaging.

## DFM report (`fab/DFM-REPORT.md`)

- Rule-deck name + version + the fab preset it encodes; `DRC_VIOLATIONS: 0` evidence path.
- Stackup + finish + soldermask/silk colors (defaults stated, not implied).
- Min feature summary actually used vs deck minima (headroom, not just compliance).
- Panelization note: single board (default) or the fab's panel service; explicit.
- Assembly side(s), fiducials present if PCBA, polarized-part rotation table checked against
  footprint zero-orientation (the classic CPL failure — diodes/tantalums 180° out).

## BOM cost (mechanical, Goodhart-guarded)

`scripts/score-anvil.sh bom-cost fab/bom.csv catalog/parts-catalog.csv` joins BOM lines to the
**pinned catalog snapshot** by MPN → `BOM_COST: <total> <currency> @ qty<N>` + per-line detail to
stderr. Missing MPN in the catalog = hard error (a part chosen outside the pinned set), not a
zero. PCB + assembly cost, when targeted, enter as separate stated line items with their source.
The HRS cost target compares against this number and nothing else — live distributor prices
mid-loop would make the metric non-reproducible.

## Availability & lifecycle rows

`manufacturing` rows assert, per catalog line: `lifecycle == active`, `stock > 0` at snapshot
date. A part that went NRND between snapshots is caught at the explicit refresh event, becomes a
GitHub issue, and a substitution enters through the normal loop (derating + sims re-verified).

## Fab presets

`jlcpcb` (default), `pcbway`, `generic` — each pins: layer options, min track/space, min via
drill/diameter, min annular, board-edge clearance, mask sliver, finish options. Encoded twice:
board-setup constraints + the `.kicad_dru` deck (templates ship both). Presets carry an
`accessed` date and the note: **verify against the fab's current published specs at build time**
— fab capabilities drift; the deck is a snapshot, refreshing it is a logged event (same
discipline as the parts catalog).
