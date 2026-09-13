# Toolchain

Core checks use Python 3.10+ standard library. Git is used for controlled source history; Git
Bash provides compatibility launchers on Windows. Node is no longer required. Use an existing
Python interpreter (`python3`, `py -3`, or an offline installed `uv` Python); `ANVIL_PYTHON`
can name an explicit executable. Avoid the Windows Store Python stub.

KiCad CLI is needed for ERC/DRC and manufacturing exports. Anvil's report schema targets KiCad
9/10; the upgrade is exercised against the installed KiCad 10 CLI. Discover PATH, `KICAD_CLI`,
Program Files and per-user LocalAppData installation paths. Keep matching board/project/
schematic/rule files together. Record the actual tool version with each run.

ngspice standalone CLI is needed for circuit simulation; KiCad's simulator DLL alone does not
provide the batch command. Use PATH or `NGSPICE`. Missing tools are errors, not parse-only
fallbacks. Model syntax and numerical convergence still need actual circuit validation.

Only require authoring dependencies selected by the project: SKiDL for SKiDL sources, kiutils
when used for KiCad edits, build123d/CadQuery/OpenSCAD for those CAD sources, Java for freerouting,
and the actual firmware SDK/compiler, HIL runner, slicer/CAM or fixture tooling when used.
Imported native designs do not need every possible authoring library installed.

`doctor.sh` checks core tools by default. `--require-build` also requires KiCad and ngspice;
`--require-product` adds an available CAD authoring tool. Missing optional tools are reported
without blocking unrelated work. `DOCTOR: READY` means the requested tooling is available,
not that a product passed verification. The script never installs dependencies.

From PowerShell/cmd, use `scripts/doctor.cmd`; it locates Git for Windows Bash and does not
use the WSL relay stub. Direct `uv run --no-project --offline python scripts/anvil.py ...`
works without Bash. Installed plugin copies include the Python seam, launchers, Windows shim,
references and all project templates; `sync-plugin.sh --check` enforces byte parity.
