"""Runnable regression checks; external approvals below are explicitly synthetic test data."""
from pathlib import Path
import csv
from datetime import datetime, timezone, timedelta
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "tests/fixtures"
spec = importlib.util.spec_from_file_location("anvil", ROOT / "scripts/anvil.py")
anvil = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = anvil
spec.loader.exec_module(anvil)
jev_spec = importlib.util.spec_from_file_location("jev_triage", ROOT / "scripts/jev_triage.py")
jev = importlib.util.module_from_spec(jev_spec)
jev_spec.loader.exec_module(jev)


class Regression(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="anvil-test-")
        self.root = Path(self.temp.name).resolve()  # Windows runners hand out 8.3 short temp paths
        anvil.READS.clear()
        anvil.DETAILS.clear()

    def tearDown(self):
        self.temp.cleanup()

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def csv(self, name, rows, delimiter="\t"):
        path = self.write(name, "")
        with path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter=delimiter, lineterminator="\n")
            writer.writeheader(); writer.writerows(rows)
        return path

    def test_metric_and_coverage_contract(self):
        self.assertEqual(anvil.pass_rate(FIX / "gate-results.tsv")[0], "PASS_RATE: 0.50")
        with patch.dict(os.environ, {"ELECTRICAL_GATE_CAP": ".25"}):
            self.assertEqual(anvil.pass_rate(FIX / "gate-results.tsv")[0], "PASS_RATE: 0.25")
        self.assertEqual(anvil.pass_rate(FIX / "product-results.tsv")[0], "PASS_RATE: 0.81")
        self.assertEqual(anvil.coverage(FIX / "cov-results.tsv", FIX / "cov-hrs.md")[0], "REQ_COVERAGE: 0.67")
        rows = anvil.table(FIX / "cov-results.tsv")
        rows[0]["traces"] = "HR-999"
        with self.assertRaisesRegex(ValueError, "orphan"):
            anvil.coverage(self.csv("orphan.tsv", rows), FIX / "cov-hrs.md")
        rows[0]["traces"] = "HR-1"
        for value in ("0", "-1", "NaN", "inf", "abc"):
            rows[0]["weight"] = value
            with self.assertRaises(ValueError):
                anvil.pass_rate(self.csv("invalid.tsv", rows))
        self.assertEqual(anvil.requirements(self.write("hrs.md", "<!-- HR-9 -->\nHR-1 a requirement\nMention HR-8 here\n")), {"HR-1": {}})
        hrs = self.write("large.md", "\n".join(f"HR-{i} definition" for i in range(1, 1001)))
        rows[0].update(weight="1", traces=";".join(f"HR-{i}" for i in range(1,1000)))
        rows[1]["traces"] = ""
        label, complete = anvil.coverage(self.csv("partial.tsv", rows), hrs)
        self.assertFalse(complete); self.assertNotEqual(label, "REQ_COVERAGE: 1.00")

    def test_money_and_budget_validation(self):
        self.assertEqual(anvil.bom_cost(FIX / "bom.csv", FIX / "parts-catalog.csv")[0], "BOM_COST: 0.87 USD")
        bom = anvil.table(FIX / "bom.csv")
        for qty in ("broken", "-1", "0", ".5", "NaN"):
            bom[0]["Qty"] = qty
            with self.assertRaises(ValueError):
                anvil.bom_cost(self.csv("bom.csv", bom, ","), FIX / "parts-catalog.csv")
        catalog = anvil.table(FIX / "parts-catalog.csv")
        catalog[1]["currency"] = "EUR"
        with self.assertRaisesRegex(ValueError, "currency"):
            anvil.bom_cost(FIX / "bom.csv", self.csv("catalog.csv", catalog, ","))
        catalog.append(catalog[0])
        with self.assertRaisesRegex(ValueError, "duplicate"):
            anvil.bom_cost(FIX / "bom.csv", self.csv("catalog.csv", catalog, ","))
        self.assertEqual(anvil.budget(FIX / "system/budgets.tsv")[0], "SYS_BUDGET: 3/4")
        budgets = anvil.table(FIX / "system/budgets.tsv")
        for field, value in (("derate", "100"), ("derate", "0"), ("worst_demand", "-1"), ("capability", "NaN")):
            altered = [dict(r) for r in budgets]; altered[0][field] = value
            with self.assertRaises(ValueError):
                anvil.budget(self.csv("budgets.tsv", altered))
        sourced = [dict(budgets[0], demand_source="values.json#mass", capability_source="values.json#capacity")]
        anvil.write_json(self.root / "values.json", dict(mass=dict(value=610, units="g"), capacity=dict(value=6600, units="g")))
        self.assertTrue(anvil.budget(self.csv("sourced.tsv", sourced))[1])
        sourced[0]["worst_demand"] = "1"
        with self.assertRaisesRegex(ValueError, "disagree"):
            anvil.budget(self.csv("sourced.tsv", sourced))
        products = anvil.table(FIX / "system/product-bom-good.csv")
        pinned = [dict(item_id=r["item_id"], unit_price=r["unit_price"], currency=r["currency"], mass_g=r["mass_g"]) for r in products]
        self.csv("sources.csv", pinned, ",")
        for row in products:
            row["source"] = "sources.csv#" + row["item_id"]
        path = self.csv("product.csv", products, ",")
        self.assertEqual(anvil.product_bom(path)[0], "PRODUCT_COST: 94.26 USD")
        products[0]["mass_g"] = "0"
        with self.assertRaisesRegex(ValueError, "mismatch"):
            anvil.product_bom(self.csv("product.csv", products, ","))

    def test_geometry(self):
        self.assertEqual(anvil.area(FIX / "edge.kicad_pcb")[0], "AREA_MM2: 2000.0")
        self.assertEqual(anvil.mesh(FIX / "mech/cube-good.stl")[0], "MESH_DEFECTS: 0")
        self.assertFalse(anvil.mesh(FIX / "mech/cube-open.stl")[1])
        text = 'solid line\n' + '\n'.join('facet normal 0 0 0\nouter loop\n' + '\n'.join(f'vertex {x} 0 0' for x in tri) + '\nendloop\nendfacet' for tri in ((0,1,2),(0,3,1),(0,2,3),(1,3,2))) + '\nendsolid line\n'
        self.assertFalse(anvil.mesh(self.write("line.stl", text))[1])
        arc = '(kicad_pcb (gr_arc (start 0 0) (mid 20 0) (end 20 20) (layer "Edge.Cuts")))'
        self.assertEqual(anvil.area(self.write("arc.kicad_pcb", arc))[0], "AREA_MM2: 582.8")
        self.assertEqual(anvil.mechanical("fit", FIX / "mech/encl")[0], "FIT_PASS: 3/3")
        self.assertEqual(anvil.mechanical("mass", FIX / "mech/encl")[0], "MASS_PASS: 2/2")
        self.assertEqual(anvil.mechanical("dfm", FIX / "mech/encl")[0], "DFM_PASS: 1/2")
        shutil.copytree(FIX / "mech/encl", self.root / "mech")
        data = anvil.read_json(self.root / "mech/measures.json"); data["interference_mm3"] = None
        anvil.write_json(self.root / "mech/measures.json", data)
        with self.assertRaises(ValueError):
            anvil.mechanical("fit", self.root / "mech")

    def test_pinout_checks_both_endpoints_and_ratings(self):
        self.write("rating.md", "Synthetic fixture: AWG24 pair qualified to 2 A at 5 V. Not engineering advice.")
        icd = [dict(icd_id="ICD-1", **{"from":"A.J1.1", "to":"B.J1.1"}, kind="power", i_max_a="1", ampacity_a="2", awg="24", voltage_v="5", protocol="DC", rating_source="rating.md")]
        wires = [dict(wire_id="W-1", icd_id="ICD-1", **{"from":"A.J1.1", "to":"B.J1.1"}, awg="24", current_a=".9", length_mm="30", voltage_v="5", protocol="DC")]
        spec = self.csv("icd.tsv", icd)
        self.assertEqual(anvil.pinout(self.csv("wires.tsv", wires), spec)[0], "PINOUT_VIOLATIONS: 0")
        mates = self.csv("mates.tsv", [dict(mate_id="M1", side_a="A.J1", side_b="B.J1", pins="1", pin_ids_a="1", pin_ids_b="1")])
        self.assertTrue(anvil.pinout(self.root / "wires.tsv", spec, mates)[1])
        self.csv("mates.tsv", [dict(mate_id="M1", side_a="A.J1", side_b="B.J1", pins="1", pin_ids_a="2", pin_ids_b="1")])
        self.assertFalse(anvil.pinout(self.root / "wires.tsv", spec, mates)[1])
        for field, value in (("to", "C.J1.1"), ("current_a", "1.1"), ("awg", "30"), ("voltage_v", "3.3"), ("protocol", "UART")):
            changed = [dict(wires[0])]; changed[0][field] = value
            self.assertFalse(anvil.pinout(self.csv("wires.tsv", changed), spec)[1])
        with self.assertRaisesRegex(ValueError, "missing"):
            anvil.pinout(self.csv("wires.tsv", wires), spec, self.root / "missing.tsv")

    def test_kicad_fresh_report_and_active_rules(self):
        source = self.write("board.kicad_pcb", "(kicad_pcb)")
        for suffix in (".kicad_sch", ".kicad_pro", ".kicad_dru"):
            self.write("board" + suffix, "test fixture")
        output = self.write("drc.json", '{"violations": []}')
        def run(command, cwd=None):
            report = Path(command[command.index("-o") + 1])
            report.write_text(json.dumps(dict(kicad_version="10.0.5", violations=[], unconnected_items=[], schematic_parity=[])), encoding="utf-8")
            return subprocess.CompletedProcess(command, 0, "")
        with patch.object(anvil, "executable", return_value="fixture-kicad"), patch.object(anvil, "execute", side_effect=run):
            self.assertEqual(anvil.kicad("drc", source, output)[0], "DRC_VIOLATIONS: 0")
        with patch.object(anvil, "executable", return_value="fixture-kicad"), patch.object(anvil, "execute", return_value=subprocess.CompletedProcess([], 3, "missing source")):
            with self.assertRaisesRegex(ValueError, "execution failed"):
                anvil.kicad("drc", source, output)
        def malformed(command, cwd=None):
            Path(command[command.index("-o")+1]).write_text("{}", encoding="utf-8")
            return subprocess.CompletedProcess(command, 0, "")
        with patch.object(anvil, "executable", return_value="fixture-kicad"), patch.object(anvil, "execute", side_effect=malformed):
            with self.assertRaisesRegex(ValueError, "schema"):
                anvil.kicad("drc", source, output)
        (self.root / "board.kicad_dru").unlink()
        self.write("rules/board.kicad_dru", "inactive")
        with self.assertRaisesRegex(ValueError, "missing"):
            anvil.kicad("drc", source, output)

    def test_sim_executes_every_corner_without_log_pooling(self):
        self.write("power.cir", "Title\n.param vin=1\n.param load=1\n.end\n")
        row = dict(id="A-1", measure="vout", op="le", limit="2", units="V", corners="vin=1,3;load=1,2", traces="HR-1", circuit="power.cir")
        self.csv("assertions.tsv", [row])
        self.write("old.log", "vout = 1\n")
        executed = []
        def run(command, cwd=None):
            source = Path(command[-1]).read_text()
            value = "3" if ".param vin=3" in source else "1"
            executed.append(source)
            Path(command[command.index("-o")+1]).write_text("vout = " + value + "\n")
            return subprocess.CompletedProcess(command, 0, "")
        with patch.object(anvil, "executable", return_value="fixture-ngspice"), patch.object(anvil, "execute", side_effect=run), patch.dict(os.environ, {}, clear=True):
            self.assertEqual(anvil.sim(self.root)[0], "SIM_PASS: 0/1")
        self.assertEqual(len(executed), 4)
        with patch.dict(os.environ, {"SKIP_NGSPICE":"1"}):
            with self.assertRaisesRegex(ValueError, "cached"):
                anvil.sim(self.root)
        self.assertTrue(anvil.compare("-3.2", "within", "-3.3±5%")[0])
        with patch.object(anvil, "executable", return_value="fixture-ngspice"), patch.object(anvil, "execute", return_value=subprocess.CompletedProcess([], 1, "failure")), patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(ValueError, "ngspice failed"):
                anvil.sim(self.root)

    def project(self):
        shutil.copytree(anvil.template_root(), self.root, dirs_exist_ok=True)
        cfg = anvil.read_json(self.root / "anvil-project.json")
        cfg.update(name="SYNTHETIC TEST PRODUCT", features=["electronics"])
        self.csv("hrs/requirements.tsv", [dict(id="HR-1", statement="Synthetic inspection criterion", units="boolean", conditions="fixture only", method="inspection", gate="G3", owner="Test fixture")])
        cfg["artifacts"] = {role:[name] for role, name in {"schematic":"board.kicad_sch", "pcb":"board.kicad_pcb", "project":"board.kicad_pro", "rules":"board.kicad_dru", "gerbers":"board.gbr", "drill":"board.drl"}.items()}
        for names in cfg["artifacts"].values():
            self.write(names[0], "Synthetic test input, not a hardware design.")
        cfg["checks"] = {"AUTO-ERC":["erc", "board.kicad_sch"], "AUTO-DRC":["drc", "board.kicad_pcb"]}
        anvil.write_json(self.root / "anvil-project.json", cfg)
        anvil.plan(self.root)
        snap, sha = anvil.snapshot(self.root, cfg)
        anvil.write_json(self.root / "release-manifest.json", dict(snap, sha256=sha))
        return cfg, sha

    def receipts(self, cfg, sha, target="G3"):
        checks, _ = anvil.all_checks(self.root, cfg)
        ledger = anvil.results(self.root / "anvil-results.tsv")
        self.write("approved.txt", "SYNTHETIC APPROVAL FIXTURE. No real person approved any product.")
        for check in checks:
            if anvil.GATES.index(check["gate"]) > anvil.GATES.index(target):
                continue
            key = check["id"]
            data = dict(schema_version=1, check_id=key, check_sha256=anvil.json_digest(check), status="pass", method=check["method"], producer="external" if check["authority"] == "external" else "review", created_at=datetime.now(timezone.utc).isoformat(), profile_sha256=anvil.json_digest(anvil.profile(cfg)), release_sha256=sha, files={"approved.txt":anvil.digest(self.root / "approved.txt"), cfg["requirements"]:anvil.digest(self.root / cfg["requirements"])}, approval=dict(reviewer="SYNTHETIC FIXTURE", role="Test", decision="approved", record="approved.txt"))
            if check["authority"] == "tool":
                data.update(producer="anvil", command=cfg["checks"].get(key), exit_code=0, passed=True, tool_version="SYNTHETIC", transcript="approved.txt", engine_sha256=anvil.engine_digest())
                for names in cfg["artifacts"].values():
                    data["files"].update({name:anvil.digest(self.root / name) for name in names})
            relative = "evidence/" + key + ".json"
            anvil.write_json(self.root / relative, data)
            for row in ledger:
                if row["assertion"] == key:
                    row.update(status="pass", evidence=relative)
        anvil.write_ledger(self.root / "anvil-results.tsv", ledger)

    def test_lifecycle_is_cumulative_scoped_and_revision_bound(self):
        cfg, sha = self.project()
        self.assertEqual(anvil.gate(self.root, "G3")[0], "G3_BLOCKED")
        self.receipts(cfg, sha)
        self.assertEqual(anvil.gate(self.root, "G3"), ("PCB_FAB_READY", []))
        self.assertEqual(anvil.gate(self.root, "G4")[0], "G4_BLOCKED")
        self.assertEqual(anvil.main(["handoff", str(self.root), "--write", "build"]), 0)
        self.assertEqual(anvil.handoff(self.root / "handoff.json"), "HANDOFF: VALID")
        self.write("board.kicad_pcb", "changed")
        self.assertEqual(anvil.gate(self.root, "G3")[0], "G3_BLOCKED")
        with self.assertRaises(ValueError):
            anvil.handoff(self.root / "handoff.json")
        cfg["markets"] = ["TW"]
        ids = {r["id"] for r in anvil.expected_checks(cfg)}
        self.assertIn("HW-069", ids); self.assertNotIn("HW-064", ids)
        cfg.update(markets=["US","EU","GB","NI","TW"], sectors=["embedded","connected","robotics","industrial","medical","automotive"], features=["electronics","firmware","mechanics","radio","battery","cloud","taiwan_export"])
        ids = {r["id"] for r in anvil.expected_checks(cfg)}
        self.assertTrue({f"HW-{i:03}" for i in range(1,76)} <= ids)

    def test_jev_advice_fallback_and_gate_isolation(self):
        from copy import deepcopy
        from urllib.error import HTTPError, URLError
        self.project()
        before_gate = anvil.gate(self.root, "G3")
        before_files = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        packet = dict(id="synthetic-finding", sources=["fixture only"], state={"observation":"synthetic failure"})
        response = dict(model=jev.MODEL, usage=dict(input_tokens=10, output_tokens=5), answers={
            "review_track": dict(type="choice", choice="circuit", confidence=.95,
                                 probabilities={track:float(track == "circuit") for track in jev.TRACKS}),
            "repeated_attempt": dict(type="noul", noul=.1),
            "insufficient_context": dict(type="noul", noul=.1),
        })
        with patch.object(jev, "fetch", return_value=response) as fetch:
            advice = jev.triage(packet, key="synthetic-test-key")
            self.assertEqual(advice["suggested_track"], "circuit")
            self.assertEqual(advice["mode"], "shadow")
            self.assertNotIn("synthetic-test-key", json.dumps(advice))
            fetch.assert_called_once_with(packet["state"], "synthetic-test-key", 10)
        self.assertEqual(anvil.gate(self.root, "G3"), before_gate)
        self.assertEqual(before_gate[0], "G3_BLOCKED")
        self.assertEqual({p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}, before_files)
        with patch.object(jev, "fetch") as fetch:
            self.assertEqual(jev.triage(packet, key="")["fallback_reason"], "missing_api_key")
            fetch.assert_not_called()
        for error, reason in [(TimeoutError("synthetic-secret"), "network_error"),
                              (URLError("synthetic-secret"), "network_error"),
                              (HTTPError(jev.ENDPOINT, 429, "synthetic-secret", {}, None), "http_429")]:
            with self.subTest(reason=reason), patch.object(jev, "fetch", side_effect=error):
                result = jev.triage(packet, key="synthetic-test-key")
                self.assertIsNone(result["suggested_track"])
                self.assertEqual(result["fallback_reason"], reason)
                self.assertNotIn("synthetic-secret", json.dumps(result))
        for bad in (None, {}, dict(response, model="jev-latest"), dict(response, answers={})):
            with self.subTest(response=bad), patch.object(jev, "fetch", return_value=bad):
                self.assertEqual(jev.triage(packet, key="synthetic-test-key")["fallback_reason"], "invalid_response")
        for field, value, reason in [("confidence", .2, "low_confidence"), ("confidence", True, "invalid_response"),
                                     ("confidence", float("nan"), "invalid_response"), ("choice", "approve_release", "invalid_response"),
                                     ("probabilities", {"circuit":1}, "invalid_response")]:
            bad = deepcopy(response)
            bad["answers"]["review_track"][field] = value
            with self.subTest(field=field, value=value), patch.object(jev, "fetch", return_value=bad):
                self.assertEqual(jev.triage(packet, key="synthetic-test-key")["fallback_reason"], reason)
        bad = deepcopy(response)
        bad["answers"]["insufficient_context"]["noul"] = .9
        with patch.object(jev, "fetch", return_value=bad):
            self.assertEqual(jev.triage(packet, key="synthetic-test-key")["fallback_reason"], "insufficient_context")
        for bad in (dict(packet, expected="circuit"), dict(packet, state={"key":"synthetic-test-key"})):
            with self.assertRaises(ValueError), patch.object(jev, "fetch"):
                jev.triage(bad, key="synthetic-test-key")
        self.assertIsNone(jev.NoRedirect().redirect_request(None, None, 302, "", {}, "https://example.invalid"))
        for plugin in ("claude-plugin", "plugins/anvil"):
            self.assertEqual((ROOT / "scripts/jev_triage.py").read_bytes(),
                             (ROOT / plugin / "skills/anvil/scripts/jev_triage.py").read_bytes())

    def test_evidence_cannot_be_missing_skipped_wrong_method_or_expired(self):
        cfg, sha = self.project()
        self.receipts(cfg, sha)
        path = self.root / "evidence/HW-014.json"
        data = anvil.read_json(path)
        for change in ({"method":"simulation"}, {"files":{}}, {"status":"na", "rationale":"Synthetic reason for exclusion", "expires_at":"2020-01-01T00:00:00+00:00"}):
            anvil.write_json(path, dict(data, **change))
            self.assertEqual(anvil.gate(self.root, "G3")[0], "G3_BLOCKED")
        anvil.write_json(path, data)
        self.assertIn("REVIEW_DRAFT", anvil.prepare(self.root, "HW-014", ["approved.txt"]))
        with self.assertRaisesRegex(ValueError, "passing disposition"):
            anvil.record(self.root, "HW-014", self.root / "evidence/HW-014.draft.json")
        anvil.record(self.root, "HW-014", path)
        with patch.object(anvil, "metric", side_effect=ValueError("execution failed")):
            with self.assertRaises(ValueError):
                anvil.record(self.root, "AUTO-ERC")
        self.assertEqual(anvil.gate(self.root, "G3")[0], "G3_BLOCKED")
        with self.assertRaises(ValueError):
            anvil.inside(self.root, "../outside.txt")
        with self.assertRaises(ValueError):
            anvil.read_json(self.write("duplicate.json", '{"x":1,"x":2}'))
        for filename in ("handoff-good.json", "handoff-bad.json"):
            with self.assertRaises(ValueError):
                anvil.handoff(FIX / filename)

    def test_market_release_requires_all_external_gates_and_exact_inputs(self):
        cfg, sha = self.project()
        cfg["checks"].update({"AUTO-FACTORY":["factory", "manufacturing"], "AUTO-COST":["commercial", "commercial/cost-model.csv"]})
        cfg["artifacts"]["factory_policy"] = ["manufacturing/acceptance.json"]
        now = datetime.now(timezone.utc)
        anvil.write_json(self.root / "manufacturing/acceptance.json", dict(first_pass_yield=1, minimum_units=1, hardware_revision=cfg["hardware_revision"], firmware_sha256="none", fixtures={"F1":"1"}))
        self.write("manufacturing/unit.txt", "SYNTHETIC unit record for software contract testing")
        self.csv("manufacturing/unit-records.csv", [dict(serial="1", lot="L1", hardware_revision=cfg["hardware_revision"], firmware_sha256="none", fixture_id="F1", fixture_revision="1", calibration_due=(now+timedelta(days=1)).isoformat(), operator="SYNTHETIC", timestamp=now.isoformat(), attempt="1", rework_reference="", result="pass", measurement_record="unit.txt", provisioning_record="unit.txt")], ",")
        self.write("commercial/basis.md", "SYNTHETIC cost assumptions")
        self.csv("commercial/cost-model.csv", [dict(category=c, description=c, quantity="1", unit_cost="1", currency="USD", source="basis.md", assumption="Synthetic per-unit basis") for c in "components assembly test yield_loss packaging freight duties certification development warranty returns support channel overhead".split()], ",")
        anvil.write_json(self.root / "anvil-project.json", cfg)
        snap, sha = anvil.snapshot(self.root, cfg)
        anvil.write_json(self.root / "release-manifest.json", dict(snap, sha256=sha))
        self.receipts(cfg, sha, "G7")
        self.assertTrue(anvil.record(self.root, "AUTO-FACTORY")[1])
        self.assertTrue(anvil.record(self.root, "AUTO-COST")[1])
        self.assertEqual(anvil.gate(self.root, "G7"), ("MARKET_READY", []))
        self.assertEqual(anvil.gate(self.root, "Sustaining")[0], "Sustaining_BLOCKED")
        ledger = anvil.results(self.root / "anvil-results.tsv")
        for status in ("skip", "error", "not_run", "blocked", "fail"):
            altered = [dict(row, status=status) if row["assertion"] == "HW-050" else row for row in ledger]
            anvil.write_ledger(self.root / "anvil-results.tsv", altered)
            self.assertEqual(anvil.gate(self.root, "G7")[0], "G7_BLOCKED")
        anvil.write_ledger(self.root / "anvil-results.tsv", ledger)
        data = anvil.read_json(self.root / "evidence/AUTO-DRC.json")
        data["files"].pop("board.kicad_pcb")
        anvil.write_json(self.root / "evidence/AUTO-DRC.json", data)
        self.assertEqual(anvil.gate(self.root, "G7")[0], "G7_BLOCKED")

    def test_factory_yield_does_not_hide_rework(self):
        now = datetime.now(timezone.utc)
        policy = dict(first_pass_yield=1, minimum_units=2, hardware_revision="A", firmware_sha256="a"*64, fixtures={"F1":"1"})
        anvil.write_json(self.root / "acceptance.json", policy)
        self.write("record.txt", "Synthetic measurement and disposition fixture")
        base = dict(serial="1", lot="L1", hardware_revision="A", firmware_sha256="a"*64, fixture_id="F1", fixture_revision="1", calibration_due=(now+timedelta(days=1)).isoformat(), operator="SYNTHETIC", timestamp=(now-timedelta(minutes=1)).isoformat(), attempt="1", rework_reference="", result="pass", measurement_record="record.txt", provisioning_record="record.txt")
        rows = [base, dict(base, serial="2", result="fail"), dict(base, serial="2", attempt="2", result="pass", rework_reference="record.txt", timestamp=now.isoformat())]
        self.csv("unit-records.csv", rows, ",")
        label, ok = anvil.factory(self.root)
        self.assertEqual(label, "FACTORY_YIELD: 1/2 first-pass; 2/2 final"); self.assertFalse(ok)
        policy["first_pass_yield"] = .5
        anvil.write_json(self.root / "acceptance.json", policy)
        self.assertTrue(anvil.factory(self.root)[1])
        rows[0]["calibration_due"] = (now-timedelta(days=1)).isoformat()
        with self.assertRaisesRegex(ValueError, "expired"):
            anvil.factory(self.csv("unit-records.csv", rows, ",").parent)

    def test_firmware_and_full_cost_records(self):
        now = datetime.now(timezone.utc).isoformat()
        for name in ("app.bin", "lock.txt", "sbom.json", "issues.md", "recovery.md", "build.log"):
            self.write(name, "Synthetic record")
        build = dict(source_revision="a"*40, command=["fixture-build"], toolchain="fixture-1", dependency_sha256=anvil.digest(self.root / "lock.txt"), binary_sha256=anvil.digest(self.root / "app.bin"), created_at=now, exit_code=0, transcript="build.log")
        anvil.write_json(self.root / "build.json", build)
        release = dict(schema_version=1, source_revision="a"*40, toolchain="fixture-1", build_command=["fixture-build"], dependency_lock="lock.txt", binary="app.bin", binary_sha256=build["binary_sha256"], supported_hardware=["A"], bootloader_versions=["1"], sbom="sbom.json", known_issues="issues.md", support_until="2028-01-01", recovery_test="recovery.md", production_debug_policy="Locked with approved service recovery", calibration_schema="1", build_record="build.json")
        anvil.write_json(self.root / "release.json", release)
        self.assertTrue(anvil.firmware(self.root / "release.json")[1])
        self.write("lock.txt", "changed dependency")
        with self.assertRaisesRegex(ValueError, "dependency"):
            anvil.firmware(self.root / "release.json")
        categories = "components assembly test yield_loss packaging freight duties certification development warranty returns support channel overhead".split()
        rows = [dict(category=c, description=c, quantity="1", unit_cost="2.50", currency="USD", source="issues.md", assumption="Synthetic per-unit allocation") for c in categories]
        self.assertEqual(anvil.commercial(self.csv("cost.csv", rows, ","))[0], "PRODUCT_ECONOMICS: 35.00 USD")
        with self.assertRaisesRegex(ValueError, "missing cost"):
            anvil.commercial(self.csv("cost.csv", rows[:-1], ","))

    def test_installed_payload_and_versions(self):
        plugin = ROOT / "claude-plugin"
        shutil.copytree(plugin / "skills/anvil", self.root / "installed")
        entry = self.root / "installed/scripts/anvil.py"
        environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        run = subprocess.run([sys.executable, str(entry), "init", str(self.root / "consumer"), "--features", "electronics"], cwd=self.root, env=environment, capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertTrue((self.root / "consumer/lifecycle-checks.csv").is_file())
        self.assertTrue((self.root / "installed/scripts/doctor.cmd").is_file())
        if os.name == "nt":
            shim_env = dict(environment, ANVIL_PYTHON=sys.executable.replace("\\", "/"))
            probe = subprocess.run(["cmd.exe", "/d", "/c", str(self.root / "installed/scripts/doctor.cmd")], cwd=self.root, env=shim_env, capture_output=True, text=True)
            self.assertEqual(probe.returncode, 0, probe.stdout + probe.stderr)
            self.assertEqual(probe.stderr, "")
            self.assertIn("DOCTOR: READY", probe.stdout)
        run = subprocess.run([sys.executable, str(entry), "plan", str(self.root / "consumer")], cwd=self.root, env=environment, capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        run = subprocess.run([sys.executable, str(entry), "gate", str(self.root / "consumer"), "G7"], cwd=self.root, env=environment, capture_output=True, text=True)
        self.assertNotEqual(run.returncode, 0)
        self.assertNotIn("MARKET_READY", run.stdout)
        version = (ROOT / "VERSION").read_text().strip()
        self.assertEqual(json.loads((plugin / ".claude-plugin/plugin.json").read_text())["version"], version)
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        self.assertEqual(market["version"], version)
        self.assertTrue(all(p["version"] == version for p in market["plugins"]))
        self.assertIn(f'version: "{version}"', (ROOT / ".claude/skills/anvil/SKILL.md").read_text(encoding="utf-8"))
        for original_dir, installed_dir in [(ROOT / ".claude/commands", plugin / "commands"), (ROOT / ".claude/skills/anvil", plugin / "skills/anvil"), (ROOT / "templates", plugin / "skills/anvil/templates")]:
            for original in original_dir.rglob("*"):
                if original.is_file():
                    self.assertEqual(original.read_bytes(), (installed_dir / original.relative_to(original_dir)).read_bytes(), str(original))
        for original, copy in [(ROOT / "scripts/anvil.py", entry)]:
            self.assertEqual(original.read_bytes(), copy.read_bytes())

    def test_codex_marketplace_and_isolated_payload(self):
        market = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
        listing, = market["plugins"]
        self.assertEqual(market["name"], "anvil")
        self.assertEqual(listing["source"]["source"], "local")
        plugin = (ROOT / listing["source"]["path"]).resolve()
        self.assertTrue(plugin.is_relative_to(ROOT))
        manifest = json.loads((plugin / ".codex-plugin/plugin.json").read_text())
        self.assertEqual(manifest["name"], listing["name"])
        self.assertEqual(manifest["name"], plugin.name)
        self.assertEqual(manifest["version"].split("+")[0], (ROOT / "VERSION").read_text().strip())
        self.assertEqual(listing["policy"], dict(installation="AVAILABLE", authentication="ON_INSTALL"))
        self.assertEqual(listing["category"], manifest["interface"]["category"])

        installed = self.root / "codex install"
        shutil.copytree(plugin, installed)
        skill = installed / manifest["skills"] / "anvil"
        self.assertTrue((skill / "agents/openai.yaml").is_file())
        for source in (ROOT / "claude-plugin").rglob("*"):
            relative = source.relative_to(ROOT / "claude-plugin")
            if source.is_file() and ".claude-plugin" not in relative.parts:
                self.assertEqual(source.read_bytes(), (installed / relative).read_bytes(), str(relative))
        for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", (skill / "SKILL.md").read_text(encoding="utf-8")):
            target = (skill / link).resolve()
            self.assertTrue(target.is_relative_to(installed), link)
            self.assertTrue(target.is_file(), link)

        consumer = self.root / "hardware project"
        for args, should_pass in [(["init", str(consumer), "--features", "electronics"], True),
                                 (["plan", str(consumer)], True), (["gate", str(consumer), "G7"], False)]:
            run = subprocess.run([sys.executable, "-B", str(skill / "scripts/anvil.py"), *args],
                                 cwd=self.root, capture_output=True, text=True)
            self.assertEqual(run.returncode == 0, should_pass, run.stdout + run.stderr)
        self.assertTrue((consumer / "lifecycle-checks.csv").is_file())
        self.assertNotIn("MARKET_READY", run.stdout)

    @unittest.skipUnless(os.getenv("ANVIL_NATIVE_TESTS") == "1", "set ANVIL_NATIVE_TESTS=1 for installed KiCad/ngspice integration")
    def test_native_kicad_ngspice_and_execution_receipts(self):
        cfg, _ = self.project()
        self.write("board.kicad_sch", '(kicad_sch (version 20250114) (generator "eeschema") (uuid "3d3b9440-8f03-4e66-8d71-4d8f57d238ba") (paper "A4") (lib_symbols) (sheet_instances (path "/" (page "1"))))\n')
        self.write("board.kicad_pcb", '(kicad_pcb (version 20221018) (generator pcbnew) (general (thickness 1.6)) (paper "A4") (layers (0 "F.Cu" signal) (31 "B.Cu" signal) (44 "Edge.Cuts" user)) (setup (pad_to_mask_clearance 0)) (net 0 "") (gr_rect (start 0 0) (end 20 20) (layer "Edge.Cuts") (width 0.05) (fill none)))\n')
        self.write("board.kicad_pro", '{"board":{"design_settings":{"rules":{"min_track_width":0.01}}}}')
        self.write("board.kicad_dru", '(version 1)\n(rule "test minimum" (constraint track_width (min 0.2mm)))\n')
        self.assertEqual(anvil.kicad("erc", self.root / "board.kicad_sch")[0], "ERC_VIOLATIONS: 0")
        self.assertEqual(anvil.kicad("drc", self.root / "board.kicad_pcb")[0], "DRC_VIOLATIONS: 0")
        snap, sha = anvil.snapshot(self.root, cfg)
        anvil.write_json(self.root / "release-manifest.json", dict(snap, sha256=sha))
        self.assertTrue(anvil.record(self.root, "AUTO-ERC")[1])
        self.assertTrue(anvil.record(self.root, "AUTO-DRC")[1])
        check = next(c for c in anvil.expected_checks(cfg) if c["id"] == "AUTO-DRC")
        anvil.receipt_valid(self.root, cfg, check, "evidence/AUTO-DRC.json", sha)
        board = (self.root / "board.kicad_pcb").read_text()
        board = board.rstrip()[:-1] + '(segment (start 5 5) (end 10 5) (width 0.1) (layer "F.Cu") (net 0)))\n'
        self.write("board.kicad_pcb", board)
        self.assertFalse(anvil.kicad("drc", self.root / "board.kicad_pcb")[1])
        report = anvil.read_json(self.root / "board.drc.json")
        self.assertTrue(any(v["type"] == "track_width" for v in report["violations"]), "adjacent custom rule must actually fire")
        self.write("models/load.inc", 'R1 out 0 1k\n')
        self.write("sim/supply.cir", '* native corner test\n.param vin=3.3\nV1 out 0 DC {vin}\n.include ../models/load.inc\n.tran 1u 10u\n.measure tran vout AVG v(out) FROM=1u TO=10u\n.end\n')
        row = dict(id="A-1", measure="vout", op="le", limit="3.4", units="V", corners="vin=3.3,5", traces="HR-1", circuit="supply.cir")
        self.csv("sim/assertions.tsv", [row])
        self.assertEqual(anvil.sim(self.root / "sim")[0], "SIM_PASS: 0/1")
        row["limit"] = "5.1"
        self.csv("sim/assertions.tsv", [row])
        self.assertEqual(anvil.sim(self.root / "sim")[0], "SIM_PASS: 1/1")
        self.assertIn(self.root / "models/load.inc", anvil.READS)
        cfg["verification_methods"] = ["simulation"]
        cfg["checks"]["AUTO-SIM"] = ["sim", "sim"]
        cfg["artifacts"]["simulation_inputs"] = ["sim/assertions.tsv", "sim/supply.cir", "models/load.inc"]
        anvil.write_json(self.root / "anvil-project.json", cfg)
        anvil.plan(self.root)
        snap, sha = anvil.snapshot(self.root, cfg)
        anvil.write_json(self.root / "release-manifest.json", dict(snap, sha256=sha))
        self.assertTrue(anvil.record(self.root, "AUTO-SIM")[1])
        check = next(c for c in anvil.expected_checks(cfg) if c["id"] == "AUTO-SIM")
        anvil.receipt_valid(self.root, cfg, check, "evidence/AUTO-SIM.json", sha)
        (self.root / "board.kicad_pcb").unlink()
        with self.assertRaisesRegex(ValueError, "missing"):
            anvil.kicad("drc", self.root / "board.kicad_pcb")


if __name__ == "__main__":
    unittest.main(verbosity=2)
