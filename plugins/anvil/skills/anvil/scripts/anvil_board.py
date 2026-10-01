#!/usr/bin/env python3
"""Board creation, placement and autorouting through KiCad's own Python (anvil_pcb.py) and Freerouting.

- `board <schematic> <template.kicad_pcb> <out.kicad_pcb> [--placement placement.tsv]`: footprints and nets
  from a fresh netlist export onto a template board that carries the outline, stackup and design rules
  (KiCad has no command-line "update PCB from schematic"). Unplaced parts are shelf-packed inside the
  outline so the first iteration starts legal; placement.tsv (ref, x_mm, y_mm, rot_deg, side) is the
  knob the design loop turns.
- `place <pcb> <placement.tsv>`: apply a placement to an existing board.
- `route <pcb> <out.kicad_pcb>`: Specctra DSN export, Freerouting (headless), SES import, zone refill,
  then DRC on the result; the copy is routed, the input is never modified.
Stdlib only; Java plus the Freerouting jar from ANVIL_FREEROUTING_JAR or %LOCALAPPDATA%/anvil/tools.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from anvil import DETAILS, execute, executable, kicad, read, require


def kicad_python():
    if os.environ.get("KICAD_PYTHON"):
        return os.environ["KICAD_PYTHON"]
    cli = Path(executable("kicad-cli")).resolve()
    for candidate in (cli.parent / "python.exe", cli.parent / "python3",
                      cli.parents[1] / "Frameworks/Python.framework/Versions/Current/bin/python3"):
        if candidate.is_file():
            return str(candidate)
    for name in ("python3", "python"):
        found = shutil.which(name)
        if found and subprocess.run([found, "-c", "import pcbnew"], capture_output=True).returncode == 0:
            return found
    raise ValueError("KiCad's Python (with pcbnew) not found; set KICAD_PYTHON")


def pcbnew_run(*args, timeout=900):
    script = Path(__file__).resolve().with_name("anvil_pcb.py")
    run = subprocess.run([kicad_python(), "-u", str(script), *map(str, args)], capture_output=True, text=True,
                         encoding="utf-8", errors="replace", timeout=timeout)
    require(run.returncode == 0, f"pcbnew {args[0]} failed ({run.returncode}): {(run.stdout + run.stderr)[-600:]}")
    return run.stdout


def dump_board(pcb):
    pcb = Path(pcb).resolve()
    read(pcb)
    with tempfile.TemporaryDirectory(prefix="anvil-board-") as temp:
        out = Path(temp) / "board.json"
        pcbnew_run("dump", pcb, out)
        return json.loads(out.read_text(encoding="utf-8"))


def footprint_tables(project_dir):
    cli = Path(executable("kicad-cli")).resolve()
    share = cli.parents[1] / "share" / "kicad" / "footprints"
    config = Path(os.environ.get("APPDATA", Path.home() / ".config")) / "kicad"
    versions = sorted((p for p in config.glob("*") if (p / "fp-lib-table").is_file()), key=lambda p: [int(x) for x in p.name.split(".") if x.isdigit()])
    tables = [str(versions[-1] / "fp-lib-table")] if versions else []
    if (Path(project_dir) / "fp-lib-table").is_file():
        tables.append(str(Path(project_dir) / "fp-lib-table"))
    require(tables, "no fp-lib-table found (KiCad user config or project)")
    return str(share), tables


def build_board(schematic, template, output, placement=None):
    import anvil_netlist
    schematic, output = Path(schematic).resolve(), Path(output).resolve()
    require(output != Path(template).resolve(), "write the built board to a new file, not over the template")
    with tempfile.TemporaryDirectory(prefix="anvil-netlist-") as temp:
        xml = Path(temp) / "netlist.xml"
        xml.write_text(anvil_netlist.export_netlist(schematic)[-1], encoding="utf-8")
        share, tables = footprint_tables(schematic.parent)
        out = pcbnew_run("build", xml, Path(template).resolve(), output, placement or "-", share, *tables)
    DETAILS.append(out.strip())
    return out.strip().splitlines()[-1]


def place(pcb, placement, routes=None):
    """Apply placement.tsv, then lock the pre-routed critical copper from routes.tsv (RF lines, fences)."""
    args = [Path(pcb).resolve(), Path(placement).resolve()] + ([Path(routes).resolve()] if routes else [])
    return pcbnew_run("place", *args).strip().splitlines()[-1]


def freerouting():
    jar = os.environ.get("ANVIL_FREEROUTING_JAR")
    if not jar:
        found = sorted((Path(os.environ.get("LOCALAPPDATA", Path.home())) / "anvil" / "tools").glob("freerouting-*.jar"))
        jar = str(found[-1]) if found else None
    require(jar and Path(jar).is_file(), "Freerouting jar not found: set ANVIL_FREEROUTING_JAR")
    java = shutil.which("java") or (str(Path(os.environ["JAVA_HOME"]) / "bin" / "java") if os.environ.get("JAVA_HOME") else None)
    require(java, "java not found (Freerouting needs a Java runtime)")
    return java, jar


def route(pcb, output, passes=20):
    pcb, output = Path(pcb).resolve(), Path(output).resolve()
    require(pcb != output, "route writes a routed copy; give a different output path")
    shutil.copyfile(pcb, output)
    for sibling in (".kicad_pro", ".kicad_dru", ".kicad_sch"):  # rules and schematic travel with the copy (DRC parity)
        if pcb.with_suffix(sibling).is_file() and not output.with_suffix(sibling).exists():
            shutil.copyfile(pcb.with_suffix(sibling), output.with_suffix(sibling))
    java, jar = freerouting()
    with tempfile.TemporaryDirectory(prefix="anvil-route-") as temp:
        dsn, ses = Path(temp) / "board.dsn", Path(temp) / "board.ses"
        pcbnew_run("export-dsn", output, dsn)
        # one optimisation thread: the multithreaded optimiser gives a different board on every run
        run = execute([java, "-jar", jar, "-de", str(dsn), "-do", str(ses), "-mp", str(passes), "-mt", "1", "--gui.enabled=false"], cwd=temp)
        require(ses.is_file(), f"Freerouting produced no session file (exit {run.returncode})")
        pcbnew_run("import-ses", output, ses)
    summary, ok = kicad("drc", str(output))
    return f"ROUTED: {output.name}; {summary}", ok
