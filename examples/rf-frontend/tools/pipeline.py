"""Reproduce the rffe board from its sources with Anvil's own commands:
schematic (wired, proven) -> template -> board (footprints + nets) -> place -> RF pre-routes -> Freerouting + DRC.
Every step is the same CLI an engineer or agent runs; nothing here edits KiCad files directly."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANVIL = [sys.executable, "-B", str(ROOT.parents[1] / "scripts" / "anvil.py")]


def run(*args, tool=False):
    command = [sys.executable, "-B", str(ROOT / "tools" / args[0])] + list(args[1:]) if tool else ANVIL + list(args)
    done = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
    last = [line for line in done.stdout.splitlines() if line.strip()][-1:] or [done.stderr.strip()[-300:]]
    print(f"{' '.join(args)} -> {last[0]}", flush=True)
    return done.returncode


steps = [
    ("place_schematic.py",),
    ("schematic", "sch/circuit.json", "pcb/rffe.kicad_sch"),
    ("make_template.py",),
    ("board", "pcb/rffe.kicad_sch", "pcb/template.kicad_pcb", "pcb/rffe-placed.kicad_pcb", "--placement", "design/placement.tsv"),
    ("make_routes.py",),
    ("place", "pcb/rffe-placed.kicad_pcb", "design/placement.tsv", "--routes", "design/routes.tsv"),
    ("route", "pcb/rffe-placed.kicad_pcb", "pcb/rffe.kicad_pcb", "--passes", "30"),
]
for step in steps:
    code = run(*step, tool=step[0].endswith(".py"))
    if code and step[0] != "route":
        sys.exit(f"step failed: {step}")
