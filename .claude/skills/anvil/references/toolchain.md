# Toolchain

What anvil needs on a machine, how to install it, how `doctor.sh` verifies it.

## Required (CORE)

| Tool | Why | Install (Windows) | Check |
|---|---|---|---|
| git | loop memory | present on dev machines | `git --version` |
| node | JSON parsing seam for score scripts | present | `node --version` |
| bash | scripts run under Git Bash | ships with git | — |

## Required for `build` / `improve` (BUILD)

| Tool | Why | Install (Windows) | Check |
|---|---|---|---|
| KiCad 9 (`kicad-cli`) | ERC · DRC · netlist · gerber/drill/BOM/CPL · PDF/PNG renders | `winget install KiCad.KiCad` | `kicad-cli version` |
| ngspice (standalone CLI) | batch simulation with `.measure` | ngspice.sourceforge.io Windows zip → extract → add `bin/` to PATH (KiCad bundles ngspice as a DLL for its GUI simulator — the batch CLI is a separate install) | `ngspice --version` |
| Python 3 | SKiDL netlists, kiutils board surgery | `py -3` or `uv` — NEVER the Microsoft Store stub | `py -3 --version` |
| SKiDL | netlist-as-code (default flow) | `uv pip install skidl` (or `py -3 -m pip`) | `py -3 -c "import skidl"` |
| kiutils | programmatic `.kicad_pcb`/`.kicad_sch` edits | `uv pip install kiutils` | `py -3 -c "import kiutils"` |

`kicad-cli` path note: winget installs under
`C:\Program Files\KiCad\<ver>\bin\kicad-cli.exe`; doctor probes PATH first, then that glob, and
prints the export line to add when found off-PATH.

## Optional

| Tool | Why |
|---|---|
| freerouting (Java jar) | autoroute seam (DSN → SES); gates re-verify after import |
| atopile | `.ato` schematic-as-code alternative flow |
| KiCad footprint/symbol libs | installed with KiCad; project-local libs preferred for pinned parts |

## doctor.sh contract

`bash scripts/doctor.sh [--require-build]` — from Git Bash or a Claude Code session.
From Windows PowerShell/cmd use `scripts\doctor.cmd` instead: bare `bash` there resolves to the
WSL relay stub in System32 and fails with `execvpe(/bin/bash) failed` when no distro is
installed; the shim locates Git for Windows' bash and never falls back to the stub.
- Prints one `FOUND <tool> <version|path>` / `MISSING <tool> <install hint>` line per tool.
- Last line: `DOCTOR: READY` (exit 0) or `DOCTOR: BLOCKED <n> missing` (exit 1).
- `--require-build` adds the BUILD set to the required list; without it only CORE blocks.
- Never installs anything itself — it prescribes, the human (or an approved setup step) installs.

## Windows environment notes (this machine class)

- Bare `python` may hit the Store stub — always `py -3` or `uv run`.
- `curl` may be blocked — HTTP checks via `node -e "fetch(...)"`.
- Paths in probe scripts: forward slashes; write probes as `.cjs`/`.py` FILES, not inline
  `bash -c` chains (quoting eats backslashes).
- ngspice + kicad-cli both write logs where invoked — run them inside the board dir, artifacts
  land in the run/evidence tree.
