"""Size the 50-ohm RF line on the rffe stackup with Anvil's 2-D field solver (0.2 mm prepreg er 4.2 to the In1
ground plane, 35 um copper, 10 um solder mask er 3.3; coplanar F.Cu ground pour at `gap`)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "scripts"))
import anvil_fields as F  # noqa: E402

for gap in (None, 0.3, 0.4, 0.5):
    row = []
    for w in (0.30, 0.32, 0.34, 0.36, 0.38):
        z = F.stack_line([(0.2, 4.2)], [], w, 0.035, mask=(0.01, 3.3), gap=gap)["z0"]
        row.append(f"w{w:.2f}:{z:5.1f}")
    print(f"gap {gap}: " + "  ".join(row))
