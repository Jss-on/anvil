# Assembly Protocol

The last mile: everything needed to turn the kit — fabbed boards, printed/machined parts, COTS
modules, cut wire — into a working unit, written for a **technician who has never seen the
project**. If a step needs tribal knowledge, the step is incomplete. The assembly package is a
deliverable with acceptance rows, not an afterthought README.

## assembly/ tree

```
assembly/
  ASSEMBLY.md        ordered build instructions (the script)
  exploded.png       exploded view render — VIEWED evidence
  step-*.png         per-stage renders where a step is ambiguous in prose
  INTEGRATION.md     system bring-up + functional test ladder
  config/            firmware/config artifacts (FC dump, VTX table, radio model)
  QC.md              final inspection checklist
```

## ASSEMBLY.md — ordered steps

Each step:

```
### Step 7 — Mount flight controller
Parts:  PB-14 (FC), PB-31 ×4 (M3×8 socket), PB-32 ×4 (TPU grommet)   ← product-BOM ids
Tools:  2.5 mm hex driver
Do:     Seat grommets in frame bosses; orient FC arrow FORWARD; torque M3×8 to 0.5 N·m.
Check:  FC sits level; USB port faces service cutout; no grommet extruded.
```

Rules:

- **Every part reference is a product-BOM id** — a step that names a part not in the BOM, or a
  BOM line no step consumes, is a red `documentation` row (both-direction orphan check).
- Torque values on every threaded fastener into insert/metal; adhesive type + cure time where
  bonded; thread-locker grade where vibration-exposed.
- Soldered joints list gauge, joint type, and heat-shrink spec (from the harness table).
- Order respects reachability: no step may require access a previous step closed. The exploded
  render is generated from the CAD assembly and **VIEWED** to sanity-check sequence and
  orientation before the gate.
- Consumables (zip ties, heat-shrink, TPU tape) are BOM lines with quantities, not assumptions.

## INTEGRATION.md — power-up and functional ladder

The system-level sibling of the board `BRINGUP.md`, ordered so each rung is safe given the last:

1. **Smoke check** — bench supply at current limit (value stated), props OFF, expected idle
   current ± tolerance per rail.
2. **Config load** — flash/restore artifacts from `assembly/config/` (FC dump, VTX band/power
   within the region table, radio model + failsafe). Every artifact is committed — a config that
   lives on someone's laptop is not a deliverable.
3. **Link checks** — RC bind + failsafe verified (throttle-cut on signal loss), telemetry, video
   link on the configured channel.
4. **Actuation** — motor order + direction per the layout diagram (props still OFF), then
   sensors (arm angle sanity, GPS lock if fitted).
5. **First armed test** — props on, restrained/tethered per the safety note; vibration check
   (blackbox/IMU trace where available).
6. Expected value + tolerance on every rung; a rung without a number is inspection-only and says
   so explicitly.

Safety notes are explicit and first: props off until step 5, LiPo handling, RF power legality
(region sign-off row from the COTS protocol).

## QC.md — final inspection

Checklist a second person can run in < 10 minutes: fastener torque spot-checks, connector
fully-seated pass, strain relief present at every exit, no wire chafe points against carbon
edges, CG within the spec'd range (measured, value logged), AUW weighed and logged against the
mass budget row, function ladder rungs 1–4 re-run green.

## Acceptance wiring

| Row (dimension) | Evidence |
|---|---|
| assembly instructions complete, BOM-consistent (documentation) | `assembly/ASSEMBLY.md` + orphan check |
| exploded render viewed (documentation) | `assembly/exploded.png` Read |
| integration ladder with numbers (testability) | `assembly/INTEGRATION.md` |
| config artifacts committed (system) | `assembly/config/*` |
| QC checklist exists + AUW/CG rows measured (testability) | `assembly/QC.md` |
