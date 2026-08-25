# Layout Protocol

Contract for `build` Phase 7 and the `layout` dimension. Gate of record:
`kicad-cli pcb drc` at zero, **including schematic parity and the fab rule deck**.

## Board setup before the first footprint

- Stackup from the fab preset (2-layer default: sig/gnd-pour top, gnd/sig bottom with an
  unbroken ground under everything that switches; 4-layer: sig, GND, PWR, sig).
- Board setup constraints = the fab deck's minima (never KiCad defaults).
- Install `pcb/rules/<fab>.kicad_dru` (custom rules: the deck ships in `templates/`, versioned —
  the DFM report cites the deck version).
- Edge.Cuts drawn first, from the HRS mechanical spec; mounting holes + connectors placed as
  **fixed** items with locked positions.

## Placement protocol (order matters)

1. **Connectors + mounting** — HRS-pinned, immovable contracts.
2. **Power-stage current loops** — minimize the switching loop AREA first (buck: Cin–FET–diode
   loop is the EMI antenna); place before anything else can steal the space.
3. **Decoupling at pin** — 100 nF caps at their pins, same side, via-to-plane ≤ 2 vias.
4. **Sensitive analog** — feedback dividers/sense away from switch nodes; kelvin where sensing.
5. **Everything else** — grouped by schematic block; silkscreen refs readable, pin-1 marks.

## Routing constraints (critical nets first, as `.kicad_dru` rules where expressible)

- Feedback nets: short, thin ok, never under the inductor or switch node.
- Switch node: minimum copper that carries the current — it's the noise source, not a pour.
- Diff pairs / USB: matched, coupled, 90 Ω diff (impedance by stackup calculator; on 2-layer
  short runs, spacing rule + length cap recorded as analysis).
- High-current paths: width from IPC-2152 (external 1 oz ≈ 3 A/mm at 10 °C rise — compute per
  net, record in the report); vias paralleled for >1 A transitions.
- Thermal: exposed pads with via farms to the ground pour; thermal relief only on hand-solder
  pads.
- Creepage/clearance: nets > 30 V get IPC-2221-derived clearance rules in the deck (HV register)
  — human-reviewed before FAB_READY.

## DRC discipline

```
kicad-cli pcb drc --format json --schematic-parity --severity-error --exit-code-violations -o drc.json <pcb>
```
`scripts/score-anvil.sh drc <pcb>` → `DRC_VIOLATIONS: N`. Gate: **0** — unconnected items and
parity mismatches count. Warnings triaged like ERC (fix or excluded-with-reason). The rule deck
runs in the same pass; a deck violation IS a DRC violation.

## Mechanical + area

`scripts/score-anvil.sh area <pcb>` → Edge.Cuts bounding-box mm² (honest note: bbox — irregular
outlines report the enclosing rectangle; the HRS target is stated as bbox for that reason).
Mounting holes, connector positions, and max height parts are `inspection` rows against the HRS.

## Autorouting seam

Manual/agent routing first-class (edit `.kicad_pcb` via kiutils/pcbnew python). freerouting
(Java) is an OPTIONAL seam for non-critical fills: export DSN → route → import SES → then the
critical-net constraints are re-verified — an autorouted board still passes the same gates. The
gate never knows or cares who routed.

## Evidence

`kicad-cli pcb render --side top|bottom` PNGs (plus `kicad-cli pcb export pdf` assembly view) →
`docs/renders/`, **VIEWED** before the gate. Viewing catches the render-class defects DRC cannot:
silkscreen over pads, refs unreadable, connector facing the wrong edge, tombstone-bait passives
under a shield. A layout gate without viewed renders is invalid.
