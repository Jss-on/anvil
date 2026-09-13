# Mechanical design and verification

Use the project's selected CAD tool and pinned source/parameters. build123d, CadQuery,
OpenSCAD or native controlled CAD can be used; do not require an unrelated kernel for a
native/imported workflow. Keep source, datums, coordinate transforms, materials and process
specification, tolerance drawings and export settings alongside STEP/STL/manufacturing outputs.

Design enclosure/frame and assembly interfaces with electronics and harnesses: connector
access/retention, mounting, component heights, board tolerances, thermal paths, strain relief,
sealing, EMC/shield bonds, sensor alignment, moving-part clearance, tools and service access.
Risk and actual application determine shock/vibration/ingress and wear requirements. Neither
isolation mounts nor a particular wall thickness is universally appropriate.

Generate `mech/measures.json` with finite numeric measurements, optionally nested objects
referenced by dotted keys. `mech/assertions.tsv` columns are `id,class,measure,op,limit,units,
traces` separated by tabs; class is fit, mass or dfm. Every selected class must have assertions.
Examples: maximum interference volume, minimum clearance under tolerance stack, mass ceiling,
minimum process feature and tooling access. A null measurement is an error, not zero clearance.

`fit`, `mass` and `mech-dfm` compare those measurements. Include CAD source, generator/tool
version, command/transcript, material/density, units and actual model/measure outputs in the
review and manifest. A JSON number is not proof that a CAD kernel ran or that the physical part
fits. HW-013/HW-015/HW-017 reviews bind the measures to the model and selected process.

`mesh` checks STL structure, finite vertices, degenerate triangles, edge manifoldness and
orientation. Its passing result does not establish absence of self-intersections, minimum wall
thickness, collision-free assembly, tolerance feasibility or process suitability. Use the CAD
kernel/process tooling for those checks and retain actual results. Slicer/CAM runs must be
executed explicitly with pinned profiles; Anvil does not silently run a slicer on imported STL.

G4/G5 validate physical fit, fastener torque/retention, material behavior, thermal path,
ingress/dynamics and service operation on identified samples. G6 validates tooling, fixtures,
critical dimensions, inspection/measurement capability and assembly process. Preserve rework,
nonconformances and sample/configuration differences from production intent.
