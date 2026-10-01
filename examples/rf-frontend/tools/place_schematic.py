"""Functional schematic placement for sch/circuit.json (A4, mm): RF chain across the middle, bias tee below it,
power bottom-left, clock top-right. The wired-schematic generator routes the wires and proves the netlist."""
import json
from pathlib import Path

SPEC = Path(__file__).resolve().parents[1] / "sch" / "circuit.json"
AT = {
    "J1": (45, 95, 180), "C1": (70, 95, 90), "U2": (100, 95, 0), "C2": (135, 95, 90), "J2": (165, 95, 0),
    "L1": (120, 112, 0), "C3": (105, 130, 0), "C4": (120, 130, 0), "R1": (150, 118, 90), "R3": (150, 131, 90), "R5": (150, 144, 90),
    "J4": (40, 165, 180), "C6": (60, 172, 0), "U1": (85, 165, 0), "C7": (112, 172, 0), "C8": (125, 172, 0),
    "R4": (145, 165, 0), "D1": (160, 172, 90),
    "X1": (195, 60, 0), "C5": (215, 72, 0), "R2": (225, 57, 90), "J3": (250, 57, 0),
}
spec = json.loads(SPEC.read_text(encoding="utf-8"))
for part in spec["parts"]:
    x, y, rot = AT[part["ref"]]
    part["at"], part["rot"] = [round(x / 2.54) * 2.54, round(y / 2.54) * 2.54], rot  # 1.27 mm connection grid
SPEC.write_text(json.dumps(spec, indent=2) + "\n", encoding="utf-8")
print(f"PLACED: {len(AT)} schematic symbols")
