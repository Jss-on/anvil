# Mechanical Protocol

The contract behind the mechanical track of `build` — enclosure, frame, mounts, the parts you
hold. Same discipline as the electrical gates: geometry truth comes from tools (mesh analysis,
geometry-kernel measures, slicers), never from prose.

## CAD-as-code (the netlist-as-code analog)

- Parametric python: **build123d** (default) or **CadQuery** — a text artifact the loop can diff
  and revert. OpenSCAD `.scad` acceptable for simple prismatic parts.
- ONE params block at the top of each source (dimensions, clearances, wall, density) — the loop
  tunes parameters, never raw vertices.
- Headless build: `py -3 mech/cad/<part>.py` exports `mech/build/<part>.stl` + `.step` AND writes
  `mech/measures.json` — no GUI in the loop, ever.
- Source is truth; build artifacts are committed evidence, like sim logs.

## mech/ tree

```
mech/
  cad/<part>.py        parametric source (params block at top)
  build/<part>.stl     watertight export — mesh gate input
  build/<part>.step    exchange format (CNC quotes, fit checks in other CAD)
  measures.json        geometry-kernel measures — the mechanical "ngspice log"
  assertions.tsv       id  class  measure  op  limit  units  traces
  renders/*.png        exploded / section / cavity renders — VIEWED evidence
```

## measures.json (kernel-emitted, never hand-typed)

Written by the CAD script from the geometry kernel at build time — flat map `measure → number`.
Hand-editing measures.json is self-certification, the mechanical analog of prose-passing ERC: a
defect, not a shortcut. Required families for an enclosure/frame:

| Measure | How the kernel computes it |
|---|---|
| `interference_mm3` | boolean intersect(board + component envelopes, enclosure solid) volume |
| `clearance_x_mm` / `_y_mm` / `_z_mm` | cavity face ↔ board/component envelope distances |
| `wall_min_mm` | minimum shell thickness (offset test or ray sampling) |
| `boss_misalign_mm` | worst distance between boss axis and matching PCB hole axis |
| `aperture_slop_mm` | connector aperture minus connector body, per side |
| `mass_g`, `volume_mm3` | solid volume × material density (density lives in params) |
| `overhang_max_deg` | steepest down-facing surface angle (FDM printability) |

## assertions.tsv

Same grammar as `sim/assertions.tsv`: `op ∈ le|ge|within`; every row `traces` → HR-n.
`class ∈ fit|mass|dfm` selects which gate evaluates the row.

```
id	class	measure	op	limit	units	traces
F-1	fit	interference_mm3	le	0	mm3	HR-12
F-2	fit	clearance_z_mm	ge	0.5	mm	HR-12
F-3	fit	boss_misalign_mm	le	0.1	mm	HR-13
M-1	mass	mass_g	le	38	g	HR-9
D-1	dfm	wall_min_mm	ge	1.6	mm	HR-14
D-2	dfm	overhang_max_deg	le	55	deg	HR-14
```

## Gates (score-anvil.sh)

| Gate | Emits (stdout, one line) | Red when |
|---|---|---|
| `mesh <stl>` | `MESH_DEFECTS: N` | open edges, non-manifold edges, inconsistent winding — must be 0 |
| `fit <mech-dir>` | `FIT_PASS: x/y` | any `fit` assertion fails (interference, clearance, boss/aperture alignment) |
| `mass <mech-dir>` | `MASS_PASS: x/y` | any `mass` assertion fails (over budget) |
| `mech-dfm <mech-dir>` | `DFM_PASS: x/y` | wall under process floor, overhang over limit; when `PRUSA_SLICER` is set the STL must also slice clean |

Non-buildable CAD (script throws, kernel boolean fails) is a red row, never a skip — the
mechanical analog of a non-convergent sim.

## Process floors (defaults; the HRS may override, never silently relax)

| Process | Structural wall | Shell wall | Overhang | Clearance press / loose |
|---|---|---|---|---|
| FDM PETG/ABS/ASA | 1.6 mm | 0.8 mm | ≤ 55° | 0.15 / 0.30 mm |
| SLA tough resin | 1.0 mm | 0.6 mm | supported | 0.10 / 0.20 mm |
| CNC 6061 | 0.8 mm | 0.8 mm | n/a | 0.05 / 0.10 mm |

## Rugged rules (field / airborne products)

- External corners filleted ≥ 1.5 mm; stiffness comes from ribs, not wall thickness.
- Heat-set threaded inserts over printed threads for any serviceable joint; boss wall ≥ 1.6 mm
  around the insert.
- Vibration-sensitive modules (IMU, flight controller, camera) mount on TPU isolators or
  grommets — never hard-bolted to the airframe.
- IP-rated builds: continuous seal groove sized to the gland spec of the chosen o-ring/TPU seal;
  deliberate drain path below electronics.
- Strain relief on every wire exit; no bend under 3× jacket diameter at the exit.
- Impact zones (arms, bumpers, camera surrounds) are sacrificial, replaceable parts — listed in
  the product BOM with spare quantities.

## Viewed evidence

A section view through the cavity and an exploded assembly render are exported
(`mech/renders/`) and **Read** before the mechanical phase gate — unviewed geometry hides
interference the same way unviewed schematics hide ratsnest disasters.
