"""Regression checks for the wiring, plotting, rule-calculation and audit-report tools (stdlib only)."""
from pathlib import Path
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import anvil  # noqa: E402
import anvil_netlist as net  # noqa: E402
import anvil_plots as plots  # noqa: E402
import anvil_report as report  # noqa: E402
import anvil_rules as rules  # noqa: E402
import anvil_schematic as sch  # noqa: E402

XML = """<?xml version="1.0" encoding="UTF-8"?>
<export version="E"><components>
 <comp ref="U1"><value>REG</value><footprint>SOT-23-5</footprint><units><unit name="A"><pins><pin num="1"/><pin num="2"/><pin num="3"/></pins></unit></units></comp>
 <comp ref="C1"><value>100n</value><footprint>C_0402</footprint><units><unit name="A"><pins><pin num="1"/><pin num="2"/></pins></unit></units></comp>
 <comp ref="R1"><value>10k</value><footprint>R_0402</footprint><units><unit name="A"><pins><pin num="1"/><pin num="2"/></pins></unit></units></comp>
 <comp ref="#PWR01"><value>GND</value></comp>
</components><nets>
 <net code="1" name="/VIN"><node ref="U1" pin="1" pintype="power_in"/><node ref="C1" pin="1" pintype="passive"/><node ref="#PWR01" pin="1"/></net>
 <net code="2" name="GND"><node ref="U1" pin="2" pintype="power_in"/><node ref="C1" pin="2" pintype="passive"/><node ref="R1" pin="2" pintype="passive"/></net>
 <net code="3" name="/EN"><node ref="U1" pin="3" pintype="input"/><node ref="R1" pin="1" pintype="passive"/></net>
</nets></export>"""

RAW = """Title: * rc test
Date: now
Plotname: Transient Analysis
Flags: real
No. Variables: 2
No. Points: 3
Variables:
\t0\ttime\ttime
\t1\tv(out)\tvoltage
Values:
0\t0.0
\t0.0
1\t1e-3
\t2.5
2\t2e-3
\t5.0
"""


class Tools(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="anvil-tools-")
        self.root = Path(self.temp.name).resolve()  # Windows runners hand out 8.3 short temp paths
        anvil.READS.clear()
        anvil.DETAILS.clear()

    def tearDown(self):
        self.temp.cleanup()

    def test_netlist_assertions_cover_every_kind(self):
        nets, parts, types = net.parse_netlist(XML)
        self.assertEqual(nets["/VIN"], {("U1", "1"), ("C1", "1")})  # power symbols are not physical pins
        good = [("equals", "VIN", "U1.1 C1.1"), ("contains", "GND", "U1.2"), ("excludes", "GND", "U1.1"),
                ("connected", "", "U1.1 C1.1"), ("isolated", "", "U1.1 U1.2"), ("count", "GND", "eq 3"),
                ("decoupled", "U1", "GND 1"), ("no_floating", "U1", ""), ("series", "R1", "EN GND"), ("pin_type", "U1.3", "input")]
        for kind, target, args in good:
            ok, observation = net.check(kind, target, args, nets, parts, types)
            self.assertTrue(ok, f"{kind}: {observation}")
        bad = [("equals", "VIN", "U1.1"), ("contains", "GND", "R1.1"), ("excludes", "GND", "R1.2"), ("connected", "", "U1.1 R1.1"),
               ("isolated", "", "U1.2 R1.2"), ("count", "GND", "le 2"), ("decoupled", "U1", "GND 3"), ("pin_type", "U1.3", "power_in")]
        for kind, target, args in bad:
            self.assertFalse(net.check(kind, target, args, nets, parts, types)[0], kind)
        with self.assertRaisesRegex(ValueError, "net not in schematic"):
            net.check("equals", "NOPE", "U1.1", nets, parts, types)
        with self.assertRaisesRegex(ValueError, "unknown assertion kind"):
            net.check("magic", "", "", nets, parts, types)
        with self.assertRaisesRegex(ValueError, "not a KiCad XML netlist"):
            net.parse_netlist("<html/>")

    def test_connectivity_uses_a_fresh_export_and_records_transcript(self):
        sch = self.root / "board.kicad_sch"
        sch.write_text("(kicad_sch)", encoding="utf-8")
        (self.root / "connectivity.tsv").write_text("id\tkind\ttarget\targs\ttraces\nW-1\tequals\tVIN\tU1.1 C1.1\tHR-1\nW-2\tcount\tEN\tge 3\t\n", encoding="utf-8")

        def fake(command, cwd=None):
            Path(command[command.index("-o") + 1]).write_text(XML, encoding="utf-8")
            return subprocess.CompletedProcess(command, 0, "")
        with patch.object(anvil, "executable", return_value="fixture-kicad"), patch.object(net, "executable", return_value="fixture-kicad"), patch.object(net, "execute", side_effect=fake):
            label, ok = net.connectivity(sch, self.root / "connectivity.tsv")
            self.assertEqual((label, ok), ("CONNECTIVITY: 1/2", False))
            self.assertTrue(any("W-2 count EN" in d and "FAIL" in d for d in anvil.DETAILS))
            self.assertIn("WIRING: 3 nets, 3 parts", net.wiring_tables(sch, self.root / "wiring"))
        self.assertIn("| `/VIN` | 2 | C1.1, U1.1 |", (self.root / "wiring/wiring.md").read_text(encoding="utf-8"))
        self.assertIn('"C1" -- "/VIN"', (self.root / "wiring/wiring.dot").read_text(encoding="utf-8"))
        with patch.object(net, "executable", return_value="fixture-kicad"), patch.object(net, "execute", return_value=subprocess.CompletedProcess([], 1, "boom")):
            with self.assertRaisesRegex(ValueError, "netlist export failed"):
                net.connectivity(sch, self.root / "connectivity.tsv")

    def test_raw_parser_and_measure_stripping(self):
        names, columns = plots.parse_raw(RAW.encode())
        self.assertEqual(names, ["time", "v(out)"])
        self.assertEqual(columns[1], [0.0, 2.5, 5.0])
        circuit = self.root / "c.cir"
        circuit.write_text("t\n.param vin=1\nV1 a 0 {vin}\n.meas tran x MAX v(a)\n.end\n", encoding="utf-8")
        text = plots.materialize(circuit, {"vin": "3"})
        self.assertIn(".param vin=3", text)
        self.assertNotIn(".meas", text)
        with self.assertRaisesRegex(ValueError, "no Values/Binary"):
            plots.parse_raw(b"Title: x\n")
        records = [dict(id="A", margin=1.0, units="V", status="pass")]
        try:
            import matplotlib  # noqa: F401
        except ImportError:
            with self.assertRaisesRegex(ValueError, "matplotlib"):
                plots.margin_plot(records, self.root / "p")
        else:
            self.assertTrue(plots.margin_plot(records, self.root / "p").is_file())

    def test_rule_calculations_match_textbook_anchors(self):
        self.assertAlmostEqual(rules.skin_depth(1e6)["value"], 66.1, delta=1.0)          # copper ~66 um at 1 MHz
        self.assertAlmostEqual(rules.bandwidth_from_risetime(1)["value"], 0.35)
        self.assertAlmostEqual(rules.adc_snr_ideal(12)["value"], 74.0, places=2)
        self.assertAlmostEqual(rules.capacitor_reactance(100, 2400)["value"], 0.663, places=3)
        self.assertAlmostEqual(rules.capacitor_reactance(100, 2400, esl_nh=0.6)["value"], 9.048 - 0.663, places=2)  # above SRF: inductive
        self.assertEqual(rules.clearance_ipc2221(48, "B1")["value"], 0.10)
        self.assertEqual(rules.clearance_ipc2221(48, "B2")["value"], 0.60)
        self.assertAlmostEqual(rules.clearance_ipc2221(600, "B2")["value"], 3.0, places=6)
        self.assertEqual(rules.clearance_ipc2221(48, "A5")["value"], 0.13)   # Mitzner Table 6.8: conformal 5 mil
        self.assertAlmostEqual(rules.fusing_time_onderdonk(6, 9.75 * 6.4516e-4)["value"], 0.09, delta=0.005)  # Brooks §12.8.1
        z = rules.microstrip_z0(0.3, 0.2, 4.4)["value"]
        self.assertTrue(40 < z < 60, z)
        self.assertAlmostEqual(rules.pdn_target_impedance(3.3, 3, 2)["value"], 49.5)
        buck = rules.buck_ripple(12, 5, 2, 500, 10, 22, 10)
        self.assertAlmostEqual(buck["duty"], 5 / 12)
        self.assertAlmostEqual(buck["ripple_current_a"], 0.5833, places=3)
        self.assertTrue(buck["ccm"])
        self.assertAlmostEqual(rules.return_loss(50)["value"], 99.0)
        self.assertAlmostEqual(rules.return_loss(75)["value"], 13.98, places=2)
        self.assertAlmostEqual(rules.cascade_noise_figure("2,6", "20")["value"], 2.13, places=1)
        self.assertAlmostEqual(rules.trace_resistance(1, 1, 100)["value"], 0.0497, places=3)
        i = rules.trace_current_ipc2221(1.0, 1, 10)["value"]
        self.assertTrue(1.5 < i < 3.5, i)   # 1 mm / 1 oz / 10 C external is a ~2-3 A trace on the IPC-2221 chart
        self.assertGreater(rules.trace_current_ipc2221(1.0, 1, 10)["value"], rules.trace_current_ipc2221(1.0, 1, 10, "internal")["value"])
        with self.assertRaisesRegex(ValueError, "missing inputs"):
            rules.run_check("skin_depth", {})
        with self.assertRaisesRegex(ValueError, "unknown check"):
            rules.run_check("teleport", {})
        self.assertIn("um", rules.calc("skin_depth", {"frequency_hz": "1e9"}))

    def test_rules_table_evaluation(self):
        design = self.root / "design"
        design.mkdir()
        (design / "rules.tsv").write_text("id\tcheck\tinputs\top\tlimit\tunits\ttraces\tsource\n"
                                          "DR-1\tclearance_margin\tactual_mm=0.8;voltage_v=48;condition=B2\tge\t0\tmm\tHR-1\tIPC2221-001\n"
                                          "DR-2\ttrace_temp_rise_ipc2221\tcurrent_a=3;width_mm=0.5;thickness_oz=1\tle\t10\tC\t\tBROOKS-001\n", encoding="utf-8")
        label, ok = rules.evaluate(design)
        self.assertEqual(label, "RULES: 1/2")
        self.assertFalse(ok)
        self.assertTrue(any(d.startswith("DR-2:") and "FAIL" in d for d in anvil.DETAILS))
        (design / "rules.tsv").write_text("id\tcheck\tinputs\top\tlimit\tunits\ttraces\tsource\nDR-1\tskin_depth\tfrequency_hz=1e6\tle\t100\tmm\t\tX\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "units"):
            rules.evaluate(design)

    def test_audit_ledgers_and_report(self):
        shutil.copytree(anvil.template_root(), self.root, dirs_exist_ok=True)
        cfg = anvil.read_json(self.root / "anvil-project.json")
        cfg.update(name="SYNTHETIC", features=["electronics"])
        (self.root / "hrs/requirements.tsv").write_text("id\tstatement\tunits\tconditions\tmethod\tgate\towner\nHR-1\tSynthetic\tboolean\tfixture\tinspection\tG3\tTest\n", encoding="utf-8")
        cfg["artifacts"] = {}
        anvil.write_json(self.root / "anvil-project.json", cfg)
        anvil.plan(self.root)
        fields = report.ITERATION_FIELDS
        for n, (result, value) in enumerate([("keep", "10"), ("discard", "12"), ("keep", "9"), ("discard", "9"), ("discard", "9")], 1):
            report.append_row(self.root / "audit/iterations.tsv", fields, dict(phase="improve", change=f"c{n}", metric="bom_cost", value=value, checks="erc,drc", result=result, rules="BROOKS-001"))
        report.append_row(self.root / "audit/decisions.tsv", report.DECISION_FIELDS, dict(id="D-1", topic="inductor", decision="10 uH", rules="ERICKSON-012", sources="erickson2020"))
        report.append_row(self.root / "audit/research.tsv", report.RESEARCH_FIELDS, dict(id="R-1", kind="book", source="brooks2021", locator="p.45", claim="1 oz trace", used_for="width", rules="BROOKS-014"))
        rows = report.optional_table(self.root / "audit/iterations.tsv", fields)
        analysis = report.analyze_iterations(rows)
        self.assertEqual((analysis["kept"], analysis["tried"], analysis["consecutive_no_improvement"], analysis["verdict"]), (2, 5, 2, "CONTINUE"))
        rows += [dict(r, result="discard", note="") for r in rows[:3]]
        self.assertEqual(report.analyze_iterations(rows)["verdict"], "PLATEAU")
        (self.root / "analysis/em").mkdir(parents=True)
        (self.root / "analysis/em/rf_in.png").write_bytes(b"\x89PNG")
        label = report.build(self.root)
        self.assertIn("AUDIT:", label)
        doc = (self.root / "audit/AUDIT.md").read_text(encoding="utf-8")
        self.assertIn("G3_BLOCKED", doc)
        self.assertIn("D. Brooks and J. Adam", doc)
        self.assertIn("R. W. Erickson", doc)
        self.assertIn("BROOKS-014", doc)
        summary = json.loads((self.root / "audit/audit.json").read_text(encoding="utf-8"))
        self.assertEqual(summary["verdict"], "G3_BLOCKED")
        self.assertIn("erickson2020", (self.root / "audit/paper/refs.bib").read_text(encoding="utf-8"))
        paper = (self.root / "audit/paper/paper.tex").read_text(encoding="utf-8")
        self.assertIn("\\documentclass[conference]{IEEEtran}", paper)
        self.assertIn("keepaspectratio]{../../analysis/em/rf_in.png}", paper)
        self.assertEqual(report.tex("S11<=-15 dB | 50 Ω_x"), "S11$\\le$-15 dB \\textbar{} 50 $\\Omega$\\_x")
        run = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/anvil.py"), "log", str(self.root), "iteration", "change=x", "result=keep", "bogus=1"], capture_output=True, text=True)
        self.assertEqual(run.returncode, 2, run.stdout + run.stderr)
        run = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/anvil.py"), "log", str(self.root), "research", "source=wilson2011", "claim=derating"], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertIn("SRC-2\t", (self.root / "audit/research.tsv").read_text(encoding="utf-8"))  # the ledger the report reads, auto-numbered
        run = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/anvil.py"), "calc", "pdn_target_impedance", "rail_v=3.3", "ripple_pct=3", "transient_a=2"], capture_output=True, text=True)
        self.assertIn("49.5 mohm", run.stdout)

    def test_schematic_geometry_matches_kicad_conventions(self):
        # Device:R pin 1 sits at library (0, 3.81): top at 0 deg, left at 90, bottom at 180, right at 270.
        for rot, expected in ((0, (0, -3.81)), (90, (-3.81, 0)), (180, (0, 3.81)), (270, (3.81, 0))):
            self.assertEqual(tuple(round(v, 6) + 0.0 for v in sch.transform(rot)(0, 3.81)), expected, rot)
        self.assertEqual(sch.transform(0, "y")(2.54, 0), (-2.54, 0))
        lib = {n: sch.parse(t) for n, t in {
            "BASE": '(symbol "BASE" (property "Value" "BASE") (symbol "BASE_1_1" (pin passive line (at 0 2.54 270) (length 1.27) (name "~") (number "1"))))',
            "CHILD": '(symbol "CHILD" (extends "BASE") (property "Value" "CHILD"))'}.items()}
        flat = sch.flatten(lib, "CHILD")
        self.assertIn('"CHILD_1_1"', sch.dump(flat))
        self.assertIn('"Value" "CHILD"', sch.dump(flat))
        geo = sch.placed(sch.local_geometry(flat, 1), (10.16, 10.16), 0)
        self.assertEqual(geo["pins"]["1"]["point"], (10.16, 7.62))
        self.assertEqual(geo["pins"]["1"]["outward"], (0, -1))
        self.assertEqual(sch.parse(sch.dump(flat)), flat)

    def test_generated_schematic_is_wired_and_proven(self):
        try:
            anvil.executable("kicad-cli")
        except ValueError:
            self.skipTest("kicad-cli not installed")
        spec = dict(schema_version=1, project="t", parts=[
            dict(ref="J1", symbol="Connector_Generic:Conn_01x02", value="IN"), dict(ref="R1", symbol="Device:R", value="10k"),
            dict(ref="C1", symbol="Device:C", value="100n"), dict(ref="D1", symbol="Device:LED", value="LED")],
            nets={"VIN": ["J1.1", "R1.1"], "N1": ["R1.2", "C1.1", "D1.2"], "GND": ["J1.2", "C1.2", "D1.1"]}, pwr_flag=["VIN", "GND"])
        anvil.write_json(self.root / "circuit.json", spec)
        label, ok = sch.generate(self.root / "circuit.json", self.root / "out/t.kicad_sch")
        report = json.loads((self.root / "out/t.wiring.json").read_text(encoding="utf-8"))
        self.assertTrue(ok, report)
        self.assertEqual((report["netlist_match"], report["wired_fraction"], report["erc_errors"]), (True, 1.0, 0))
        self.assertGreater(report["wires"], 5)
        (self.root / "out/golden.tsv").write_text("id\tkind\ttarget\targs\ttraces\nW-1\tgolden\t../circuit.json\t\t\n", encoding="utf-8")
        self.assertTrue(net.connectivity(self.root / "out/t.kicad_sch", self.root / "out/golden.tsv")[1])
        spec["nets"]["N1"] = ["R1.2", "C1.1"]
        spec["nets"]["N2"] = ["D1.2"]
        anvil.write_json(self.root / "circuit.json", spec)  # golden now disagrees with the drawing
        self.assertFalse(net.connectivity(self.root / "out/t.kicad_sch", self.root / "out/golden.tsv")[1])

    def test_schematic_generation_is_deterministic(self):
        spec = ROOT / "examples/rf-frontend/sch/circuit.json"
        try:
            anvil.executable("kicad-cli")
        except ValueError:
            self.skipTest("kicad-cli not installed")
        outputs = []
        for seed in ("1", "2"):  # set iteration order follows the hash seed: output must not
            out = self.root / f"seed{seed}" / "rffe.kicad_sch"
            out.parent.mkdir(parents=True)
            env = dict(os.environ, PYTHONHASHSEED=seed)
            run = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/anvil.py"), "schematic", str(spec), str(out)],
                                 capture_output=True, text=True, env=env)
            self.assertEqual(run.returncode, 0, run.stdout[-500:] + run.stderr[-500:])
            outputs.append(out.read_bytes())
        self.assertEqual(outputs[0], outputs[1])

    def test_bibliography_is_complete_and_well_formed(self):
        data = json.loads((ROOT / ".claude/skills/anvil/references/bibliography.json").read_text(encoding="utf-8"))
        keys = [e["key"] for e in data["entries"]]
        self.assertEqual(len(keys), len(set(keys)))
        prefixes = [p for e in data["entries"] for p in e["rule_prefixes"]]
        self.assertEqual(len(prefixes), len(set(prefixes)))
        for entry in data["entries"]:
            self.assertTrue(entry["ieee"].endswith("."), entry["key"])
            for field in ("author", "title", "year"):
                self.assertTrue(entry.get(field), f"{entry['key']} missing {field}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
