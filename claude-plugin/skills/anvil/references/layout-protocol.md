# Layout Protocol

Contract for `build` Phase 7 and the `layout` dimension. Gate of record:
`kicad-cli pcb drc` at zero, **including schematic parity and the fab rule deck**.

## Board setup before the first footprint

- Stackup from the fab preset (2-layer default: sig/gnd-pour top, gnd/sig bottom with an
  unbroken ground under everything that switches; 4-layer: sig, GND, PWR, sig).
- Stackup physics, not folklore: a standard 4-layer GND–PWR core is **thick (~0.2 mm+) — its
  interplane capacitance is useless at HF; MLCCs at the pins carry HF decoupling**, the planes
  carry return paths (worth ~10–20 dB radiated-emissions reduction over 2-layer). 6-layer earns
  its cost by pairing PWR–GND across the thin central prepreg and giving every signal layer an
  adjacent reference. Impedance math (IPC-2141A / the fab's calculator) uses the **fabricator's
  actual dielectric values**, never catalog εr — resin content and glass weave vary.
- Board setup constraints = the fab deck's minima (never KiCad defaults), at the elected IPC
  class (`standards.md` — Class 3 tightens annular ring and plating acceptance).
- Install `pcb/rules/<fab>.kicad_dru` (custom rules: the deck ships in `templates/`, versioned —
  the DFM report cites the deck version).
- Edge.Cuts drawn first, from the HRS mechanical spec; mounting holes + connectors placed as
  **fixed** items with locked positions.

## Grounding doctrine (most reliability problems are return-path problems)

- **One continuous ground plane.** Never split analog/digital planes reflexively — the modern
  consensus (mixed-signal vendors included) is a single unbroken plane with disciplined
  *placement* partitioning. A split is permitted only with a specific, simulated/cited
  justification logged in the layout report.
- **Return current tracks directly under its trace** at HF (least inductance, not least
  resistance). Routing any switching or high-speed net across a plane gap creates an undefined
  high-inductance return loop that radiates (~5 dB harmonic penalty measured near gaps) — a
  routed net crossing a reference-plane void is a review defect even when DRC is silent.
- **Loop area is the enemy**: every signal + its return form a loop antenna; minimize the area,
  and keep off-board cable entries referenced to the plane at the connector (shield bonds 360°
  where the HRS declares shielded I/O).
- Data converters: tie AGND/DGND per the datasheet (usually under the device) — the pin *name*
  does not mandate a separate system plane.

## Placement protocol (order matters)

1. **Connectors + mounting** — HRS-pinned, immovable contracts.
2. **Power-stage current loops** — minimize the switching loop AREA first (buck: Cin–FET–diode
   loop is the EMI antenna); place before anything else can steal the space.
3. **Decoupling at pin** — 100 nF caps within ~2 mm of their pins, same side, via-to-plane ≤ 2
   vias. The budget is **loop inductance, not capacitance**: every extra via to an inner plane
   adds ~0.5–1.0 nH, enough to gut HF performance. Hierarchy per rail: bulk (10–100 µF) at rail
   entry → MLCCs at pins → plane pair; for fast low-voltage ICs record the PDN target
   (Z_target ≈ V_core × ripple% ÷ I_transient — single-digit mΩ territory) in the layout report.
4. **Sensitive analog** — feedback dividers/sense away from switch nodes; kelvin where sensing.
5. **Everything else** — grouped by schematic block; silkscreen refs readable and off pads,
   pin-1 marks. **Assembly orientation**: consistent rotation per package family, passives'
   long axis parallel to the reflow direction where known (tombstone bait: asymmetric thermal
   masses on 0402/0603), hot parts away from temperature-sensitive ones.
6. **Fiducials when PCBA**: 3 global (asymmetric pattern) + local pair at every fine-pitch
   (≤ 0.5 mm) part.

## Routing constraints (critical nets first, as `.kicad_dru` rules where expressible)

- Feedback nets: short, thin ok, never under the inductor or switch node.
- Switch node: minimum copper that carries the current — it's the noise source, not a pour.
- Diff pairs / USB: matched, coupled, 90 Ω diff — 100 Ω for most other differential standards
  (impedance by stackup calculator on the fab's real dielectrics; on 2-layer short runs, spacing
  rule + length cap recorded as analysis). Skew-tuning serpentines go **at the source of the
  mismatch**, not wherever space is left; pairs stay over unbroken reference the whole run.
- High-current paths: width from IPC-2152 anchors in `standards.md` (1 oz external 10 °C rise:
  10 mil ≈ 1.0 A, 50 mil ≈ 3.5 A; **internal layers only 50–70 % of that**) — compute per net,
  record in the report; vias paralleled for >1 A transitions.
- Thermal: exposed pads with via farms to the ground pour — Ø 0.2–0.33 mm at ~1.0–1.2 mm pitch,
  and **connected to real spreading copper on another layer** (a via farm into nothing is
  theater); thermal relief only on hand-solder pads; 2 oz pours where the current or the
  Arrhenius math demands it. Never plan on cooling through a plastic package top.
- Creepage/clearance: nets > 30 V get IPC-2221-derived clearance rules in the deck (HV register,
  anchor values + the >500 V formula in `standards.md`; IEC 60664-1/62368-1 override where a
  safety standard applies) — human-reviewed before FAB_READY.
- Teardrops at pad-trace junctions on fine annular rings; no soldermask slivers below the fab's
  minimum web.

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
