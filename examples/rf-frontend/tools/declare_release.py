"""Declare the rffe release in anvil-project.json: every controlled artifact and every automatic check."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
cfg = json.loads((ROOT / "anvil-project.json").read_text(encoding="utf-8"))
gerbers = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / "fab" / "gerbers").glob("*.gbr"))
board = "pcb/rffe.kicad_pcb"
cfg["hardware_revision"] = "A"
cfg["artifacts"] = {
    "schematic": ["pcb/rffe.kicad_sch"], "pcb": [board], "project": ["pcb/rffe.kicad_pro"], "rules": ["pcb/rffe.kicad_dru"],
    "libraries": ["pcb/rffe_symbols.kicad_sym", "pcb/sym-lib-table", "pcb/fp-lib-table"],
    "gerbers": gerbers, "drill": ["fab/gerbers/rffe-PTH.drl", "fab/gerbers/rffe-NPTH.drl"],
    "circuit_spec": ["sch/circuit.json"], "connectivity": ["sch/connectivity.tsv"],
    "simulation": ["sim/bias_filter.cir", "sim/assertions.tsv"], "design_rules": ["design/rules.tsv"],
    "layout_intent": ["design/nets.tsv"], "rf_intent": ["design/rf.tsv"], "pdn_intent": ["design/pdn.tsv"],
    "si_intent": ["design/si.tsv"], "thermal_intent": ["design/thermal.tsv"], "em_intent": ["design/em.tsv"],
    "emc_intent": ["design/emc.tsv"],
}
cfg["checks"] = {
    "AUTO-ERC": ["erc", "pcb/rffe.kicad_sch"], "AUTO-DRC": ["drc", board], "AUTO-SIM": ["sim", "sim"],
    "AUTO-CONNECTIVITY": ["connectivity", "pcb/rffe.kicad_sch", "sch/connectivity.tsv"], "AUTO-RULES": ["rules", "design"],
    **{f"AUTO-{c.upper()}": [c, board, "design"] for c in ("layout", "pdn", "si", "thermal", "em", "emc")},
}
(ROOT / "anvil-project.json").write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8")
print(f"RELEASE: {sum(len(v) for v in cfg['artifacts'].values())} artifacts, {len(cfg['checks'])} automatic checks")
