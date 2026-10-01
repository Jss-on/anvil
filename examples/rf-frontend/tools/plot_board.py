"""Copper plots of any rffe board file (same renderer the `layout` check writes to analysis/layout/)."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parents[1] / "scripts"))
import anvil_layout as L  # noqa: E402

board = L.Board(L.dump_board(ROOT / "pcb" / (sys.argv[1] if len(sys.argv) > 1 else "rffe.kicad_pcb")))
for path in L.plot_copper(board, ROOT / "audit" / "renders" / (sys.argv[2] if len(sys.argv) > 2 else "copper")):
    print(path)
