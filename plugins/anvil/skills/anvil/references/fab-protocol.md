# Fabrication, assembly and prototype release

G3 distinguishes `PCB_FAB_READY`, `ASSEMBLY_READY`, and `PRODUCT_BUILD_READY`. Neither a bare
board export nor a passing DRC implies assembled-product or market readiness.

| Package | Required work |
|---|---|
| PCB fabrication | Released board/project/schematic/rules, correct Gerber copper/mask/silk/outline set, drills, fabrication drawing, stackup/material/finish and acceptance specification |
| Assembly | PCB package plus BOM, exact parts and DNP/variant rules, approved substitutions, placement/orientation files, assembly drawings, stencil/paste/reflow and inspection requirements |
| Product prototype | Assembly package plus mechanical sources/exports/drawings, harness/mates/ICD, product BOM and budgets, firmware/programming, assembly/test/bring-up procedures |

Use the selected KiCad CLI's documented export commands (`pcb export gerbers`, `pcb export
drill`, schematic BOM and placement export) and verify their exit codes and actual outputs.
Record units, origins, side, rotation convention, PTH/NPTH, layer set and variant. View the
manufacturing exports with an appropriate viewer and review them against source. Export settings
and dependencies are part of the controlled build. Supply IPC-2581 when agreed with the supplier;
format choice does not replace package review.

`fab/DFM-REPORT.md` records the supplier's reviewed capability/source/date, active rule file,
stackup, dimensions/tolerances, material/finish, acceptance class/edition, assembly sides,
paste/stencil strategy, moisture handling, polarity/rotation review, tooling/panelization and
all closed DFM/DFA questions. Select process parameters with the actual fabricator/assembler;
do not infer universal quality class or stencil coverage from the product label.

Reconcile BOM/placement/footprints by reference and MPN, declared population variants, board
revision and orientation. `bom-cost` verifies the exact catalog join and numeric pricing; it
does not prove availability, procurement authorization or assembly compatibility. Preserve quote,
stock/lifecycle snapshots, alternates and approved deviations.

Before releasing prototypes, prepare staged first-power instructions with current limits,
instruments, safe states, stop conditions, firmware/debug versions and test/rework records.
Verify actual test access in the design. Archive the immutable manifest, package and reviewed
receipts. Ordering, supplier submission or purchases occur only within the session's action
authorization; complete the reviewable package first.

Only `templates/anvil-project/pcb/rules/jlcpcb-2layer.kicad_dru` is supplied as a starter example.
It is not automatically active and not a promise of current supplier capability. PCBWay and
generic presets from older documentation were never bundled and are no longer advertised.
