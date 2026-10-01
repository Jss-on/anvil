"""Analysis-engine regression: every solver is held to an analytic anchor, and every board check to a
synthetic KiCad board whose right answer is known. numpy required; KiCad/ngspice/openEMS tests skip
when the tool is absent (the openEMS run is opt-in: set ANVIL_EM_TESTS=1, it takes minutes)."""
from pathlib import Path
import importlib.util
import json
import math
import os
import sys
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "tests"))
import anvil  # noqa: E402

HAVE_NUMPY = importlib.util.find_spec("numpy") is not None
if HAVE_NUMPY:
    import numpy as np
    import anvil_em as E
    import anvil_fields as F
    import anvil_layout as L
    import anvil_pdn as P
    import anvil_si as SI
    import anvil_thermal as T
    import fixture_board as FB


def tool(name):
    try:
        return anvil.executable(name)
    except ValueError:
        return None


KICAD = tool("kicad-cli") is not None
NGSPICE = tool("ngspice") is not None


def k0(x):
    """Modified Bessel K0 from its integral form (no scipy)."""
    t = np.linspace(0, 12, 200001)
    y = np.exp(-x * np.cosh(t))
    return float(np.sum((y[1:] + y[:-1]) / 2 * np.diff(t)))


@unittest.skipUnless(HAVE_NUMPY, "numpy not installed")
class Solvers(unittest.TestCase):
    def test_field_solver_anchors(self):
        z = F.line("stripline", 0.2, 0.25, 4.0, t=0.0, h2=0.25)["z0"]
        self.assertAlmostEqual(z, F.stripline_exact(0.2, 0.5, 4.0), delta=0.01 * z)
        r = F.line("microstrip", 0.3, 0.2, 4.4, t=0.0)
        z_hj, e_hj = F.microstrip_hj(0.3, 0.2, 4.4)
        self.assertAlmostEqual(r["z0"], z_hj, delta=0.01 * z_hj)
        self.assertAlmostEqual(r["er_eff"], e_hj, delta=0.01 * e_hj)
        cpwg = F.line("cpwg", 0.3, 0.2, 4.4, t=0.0, gap=0.15)["z0"]
        self.assertAlmostEqual(cpwg, F.cpwg_closed(0.3, 0.15, 0.2, 4.4)[0], delta=0.012 * cpwg)
        # physics limit: side grounds far away leave a plain microstrip (the closed form overshoots here)
        far = F.line("cpwg", 0.36, 0.2, 4.2, t=0.0, gap=1.2)["z0"]
        plain = F.line("microstrip", 0.36, 0.2, 4.2, t=0.0)["z0"]
        self.assertLess(abs(far - plain) / plain, 0.005)
        self.assertGreater(F.cpwg_closed(0.36, 1.2, 0.2, 4.2)[0], plain * 1.05)
        one_side = F.line("cpwg", 0.36, 0.2, 4.2, t=0.0, gap=(0.3, None))["z0"]
        both = F.line("cpwg", 0.36, 0.2, 4.2, t=0.0, gap=0.3)["z0"]
        self.assertTrue(both < one_side < plain)

    def test_thermal_point_source_matches_k0(self):
        cell, n, kt, h = 0.25, 301, 0.027, 100.0
        power = np.zeros((1, n, n))
        power[0, n // 2, n // 2] = 1.0
        rise = T.solve(np.full((1, n, n), kt), np.zeros((0, n, n)), np.ones((n, n), dtype=bool), power, (h, h), cell)
        lam = math.sqrt(kt / (2 * h)) * 1e3
        for r_mm in (2.0, 5.0, 10.0):
            numeric = rise[0, n // 2 + int(round(r_mm / cell)), n // 2]
            exact = k0(r_mm / lam) / (2 * math.pi * kt)
            self.assertLess(abs(numeric - exact) / exact, 0.01, r_mm)
        self.assertAlmostEqual(float(np.nansum(rise)) * 2 * h * (cell * 1e-3) ** 2, 1.0, places=6)

    def test_pdn_branch_math(self):
        f = np.array([1 / (2 * math.pi * math.sqrt(1e-9 * 100e-9))])
        z = P.impedance(f, [dict(c=100e-9, l=1e-9, r=0.02)])
        self.assertAlmostEqual(abs(z[0]), 0.02, places=6)  # series RLC at its SRF is its ESR
        f = np.logspace(3, 9, 50)
        one = P.impedance(f, [dict(c=100e-9, l=2e-9, r=0.05)])
        ten = P.impedance(f, [dict(c=100e-9, l=2e-9, r=0.05)] * 10)
        self.assertTrue(np.allclose(ten, one / 10))  # BOGATIN-2139: n identical caps scale Z by 1/n
        for text, value in (("4n7", 4.7e-9), ("100nF/50V", 100e-9), ("10uF X5R", 10e-6)):
            self.assertAlmostEqual(P.farads(text) / value, 1.0, places=12)

    def test_emc_spectrum_matches_paul_example(self):
        import anvil_emc as EMC
        for tr, expected in ((20e-9, 73.8), (5e-9, 90.4)):  # PAUL-1047: 1 V, 10 MHz, 50 %, 11th harmonic
            f, vn = EMC.harmonics(1.0, 10e6, 0.5, tr, 110e6)
            self.assertAlmostEqual(f[-1], 110e6)
            self.assertAlmostEqual(20 * math.log10(vn[-1] / 1e-6), expected, delta=0.05)
        self.assertEqual(EMC.limit_at("fcc_b", 100e6), 43.5)
        self.assertEqual(EMC.limit_at("cispr32_b", 300e6), 37.0)
        self.assertIsNone(EMC.limit_at("cispr32_b", 2e9))

    def test_touchstone_roundtrip_and_orientation(self):
        with tempfile.TemporaryDirectory() as temp:
            f = np.linspace(1e9, 2e9, 5)
            s = np.zeros((5, 2, 2), dtype=complex)
            s[:, 0, 0], s[:, 1, 0], s[:, 0, 1], s[:, 1, 1] = 0.1, 0.9j, 0.8, -0.2
            path = E.write_touchstone(Path(temp) / "x.s2p", f, s)
            f2, s2, z0 = E.read_touchstone(path)
            self.assertTrue(np.allclose(f, f2) and np.allclose(s, s2) and z0 == 50)
            # v1 two-port rows list S11 S21 S12 S22; dB/angle format
            (Path(temp) / "m.s2p").write_text("! vna\n# MHz S DB R 50\n100 -20 0 -1 90 -40 0 -15 180\n200 -21 0 -1.5 80 -40 0 -16 170\n300 -22 0 -2 70 -40 0 -17 160\n", encoding="utf-8")
            f3, s3, _ = E.read_touchstone(Path(temp) / "m.s2p")
            self.assertAlmostEqual(20 * math.log10(abs(s3[0, 1, 0])), -1.0, places=9)  # S21 is the 2nd pair
            self.assertAlmostEqual(20 * math.log10(abs(s3[0, 0, 1])), -40.0, places=9)
            anvil.DETAILS.clear()
            results = []
            E.judge("m", f3, s3, E.checks_of("S11<=-19@100e6:300e6;S21>=-1.8@100e6:300e6"), results, "test")
            self.assertEqual(results, [True, False])  # S21 falls to -2 dB at 300 MHz
            self.assertIn("m:S21@1e+08-3e+08Hz: -2 dB margin=-0.2 FAIL", anvil.DETAILS)
            self.assertAlmostEqual(E.value_of("2n2") / 2.2e-9, 1.0, places=12)
            self.assertAlmostEqual(E.value_of("4R7"), 4.7, places=12)


@unittest.skipUnless(HAVE_NUMPY and KICAD, "numpy and KiCad required")
class Boards(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.dir = Path(self.temp.name).resolve()  # Windows runners hand out 8.3 short temp paths
        anvil.DETAILS.clear()

    def tearDown(self):
        self.temp.cleanup()

    def detail(self, prefix):
        return next(d for d in anvil.DETAILS if d.startswith(prefix))

    def test_em_port_stands_where_the_pin_enters(self):
        board = L.Board(L.dump_board(FB.write_board(self.dir / "p.kicad_pcb")))
        pad = E.pad_named(board, "J1.1")
        site = E.port_site(board, pad, board.tracks("RF"), ["GND"], E.stack_z(board)[0], "J1.1")
        x0, y0, x1, y1 = E.pad_box(pad, site["layer"])
        self.assertEqual((site["layer"], site["plane"], site["along_x"], site["gaps"]), ("F.Cu", "In1.Cu", True, None))
        self.assertAlmostEqual(site["x"], x0)  # the trace leaves toward +x, so the pin enters on the -x edge
        self.assertAlmostEqual(site["width"], y1 - y0)  # across the whole pad, not just the trace width
        cpw = L.Board(L.dump_board(FB.write_cpw_board(self.dir / "c.kicad_pcb")))  # ground 1.53 mm down, gaps 0.3 mm
        site = E.port_site(cpw, E.pad_named(cpw, "J1.1"), cpw.tracks("RF"), ["GND"], E.stack_z(cpw)[0], "J1.1")
        self.assertIsNone(site["plane"])
        self.assertAlmostEqual(site["gaps"][0], 0.3, delta=0.01)

    def test_em_part_models(self):
        board = L.Board(L.dump_board(FB.write_pdn_board(self.dir / "pdn.kicad_pcb")))
        row = dict(name="bypass", nets="VCC", ports="C2.1", parts="C1=100n", f_start_hz="1.5e9", f_stop_hz="3.5e9",
                   checks="S11<=-1@1.5e9:3.5e9", traces="")
        part = next(attrs for _, attrs, _, _ in E.build(board, row)["model"].props if attrs.get("Name") == "part_C1")
        self.assertEqual((part["LEtype"], "C" in part), ("1", False))  # 100 nF is 10x above self-resonance: ESL + ESR in band
        part = next(attrs for _, attrs, _, _ in E.build(board, dict(row, parts="C1=1p"))["model"].props if attrs.get("Name") == "part_C1")
        self.assertEqual((part["LEtype"], part["C"], float(part["R"]) > 0), ("1", "1e-12", True))  # near resonance: series ESR-ESL-C

    def test_layout_truth(self):
        design = FB.write_intent(self.dir / "design")
        board = FB.write_board(self.dir / "a.kicad_pcb", hv_gap=1.3)
        label, ok = L.evaluate(board, design)
        self.assertTrue(ok, "\n".join(anvil.DETAILS))
        z = float(self.detail("RF:z0@F.Cu/0.36mm:").split()[1])
        self.assertAlmostEqual(z, 48.36, delta=0.5)  # 0.36 mm on 0.2 mm er 4.2, 35 um copper, 10 um mask
        rise = float(self.detail("PWR:trace_rise:").split()[1])
        self.assertAlmostEqual(rise, 20.3, delta=0.5)  # IPC-2152 fit, 2 A in 0.5 mm 1 oz external
        anvil.DETAILS.clear()
        label, ok = L.evaluate(FB.write_board(self.dir / "b.kicad_pcb", slot_under_rf=True), design)
        self.assertFalse(ok)
        self.assertIn("FAIL", self.detail("RF:return_path:"))
        self.assertIn("B2 needs 1.25 mm", "\n".join(anvil.DETAILS))  # 230 V at 1.0 mm edge gap
        self.assertIn("FAIL", self.detail("HV:clearance@F.Cu:"))
        anvil.DETAILS.clear()
        L.evaluate(FB.write_board(self.dir / "c.kicad_pcb", hv_gap=1.3, pour="stitched"), design)
        self.assertIn("/gap0.305|0.305", self.detail("RF:z0@F.Cu/0.36mm/gap"))
        self.assertIn("PASS", self.detail("RF:stitching:"))
        anvil.DETAILS.clear()
        L.evaluate(FB.write_board(self.dir / "d.kicad_pcb", hv_gap=1.3, pour="wide"), FB.write_intent(self.dir / "d20", rf_ghz=20.0))
        self.assertIn("FAIL", self.detail("RF:stitching:"))
        self.assertIn("FAIL", self.detail("RF:via_fence_gap:"))  # 1 mm fence pitch > lambda/10 at 20 GHz

    @unittest.skipUnless(NGSPICE, "ngspice required")
    def test_si_matches_lattice_theory(self):
        board = FB.write_board(self.dir / "si.kicad_pcb")
        design = self.dir / "design"
        design.mkdir()
        (design / "si.tsv").write_text("net\tdriver\treceivers\trise_ps\tr_drv_ohm\tv_swing\tc_rx_pf\tmax_overshoot_pct\ttraces\n"
                                       "RF\tJ1.1\tU1.1\t50\t10\t1\t0\t80\t\n", encoding="utf-8")
        label, ok = SI.evaluate(board, design)
        self.assertTrue(ok)
        z0 = float(self.detail("RF: 1 segments").split("w0.36: ")[1].split()[0])
        overshoot = float(self.detail("RF@U1.1:overshoot:").split()[1])
        self.assertAlmostEqual(overshoot, (2 * z0 / (z0 + 10) - 1) * 100, delta=0.3)  # open end doubles the launched step

    def test_pdn_and_thermal_from_copper(self):
        board = FB.write_pdn_board(self.dir / "pdn.kicad_pcb")
        design = self.dir / "design"
        design.mkdir()
        (design / "pdn.tsv").write_text("rail\tref_net\tload\tv_nom\tripple_pct\ti_step_a\tf_max_hz\tvrm_r_mohm\tvrm_l_nh\ttraces\n"
                                        "VCC\tGND\tU2\t1.0\t5\t0.5\t1e8\t5\t20\t\n", encoding="utf-8")
        label, ok = P.evaluate(board, design)
        self.assertFalse(ok)  # a 1.065 mm cavity cannot hold 0.1 ohm to 100 MHz with three caps
        cavity = self.detail("VCC: cavity In1.Cu/In2.Cu")
        area = float(cavity.split("area=")[1].split()[0])
        self.assertAlmostEqual(float(cavity.split("-> ")[1].split()[0]), F.EPS0 * 4.5 * area * 1e-6 / 1.065e-3 * 1e9, delta=0.001)
        c1 = self.detail("  C1 100 nF")
        self.assertIn("ARCH-067 X7R 0603", c1)
        spread = float(c1.split("spreading ")[1].split()[0])
        b = math.dist((24.2, 16.1), (19.5, 14.5))
        self.assertAlmostEqual(spread, 21e-3 * (1.065 / 0.0254) * math.log(b / 0.6), delta=0.06)  # BOGATIN-2135
        (design / "thermal.tsv").write_text("ref\tpower_w\ttheta_jb_c_per_w\tmax_tj_c\tambient_c\ttraces\nU2\t1.0\t10\t125\t25\t\n", encoding="utf-8")
        anvil.DETAILS.clear()
        label, ok = T.evaluate(board, design)
        balance = self.detail("thermal: 4 layers").split("energy balance ")[1].split()
        self.assertAlmostEqual(float(balance[0]), float(balance[4]), places=3)  # "<out> W out / <in> W in"
        tj1 = float(self.detail("U2:tj:").split()[1])
        (design / "thermal.tsv").write_text("ref\tpower_w\ttheta_jb_c_per_w\tmax_tj_c\tambient_c\ttraces\nU2\t2.0\t10\t125\t25\t\n", encoding="utf-8")
        anvil.DETAILS.clear()
        T.evaluate(board, design)
        tj2 = float(self.detail("U2:tj:").split()[1])
        self.assertAlmostEqual(tj2 - 25, 2 * (tj1 - 25), delta=0.01)  # linear conduction model

    def test_record_layout_through_the_gate(self):
        root = self.dir / "proj"
        self.assertEqual(anvil.main(["init", str(root), "--scope", "pcb", "--features", "electronics"]), 0)
        pcb = root / "pcb"
        pcb.mkdir(exist_ok=True)
        FB.write_board(pcb / "board.kicad_pcb", hv_gap=1.3)
        for name, text in (("board.kicad_pro", "{}\n"), ("board.kicad_dru", "(version 1)\n"), ("board.kicad_sch", "(kicad_sch (version 20250114))\n"),
                           ("board-F_Cu.gbr", "G04 placeholder*\n"), ("board.drl", "M48\n")):
            (pcb / name).write_text(text, encoding="utf-8")
        FB.write_intent(root / "design")
        (root / "hrs" / "requirements.tsv").write_text("id\tstatement\tunits\tconditions\tmethod\tgate\towner\n"
                                                       "HR-001\tRF line 50 ohm +/-10 %\tohm\tall\tanalysis\tG3\tEngineering\n", encoding="utf-8")
        cfg = json.loads((root / "anvil-project.json").read_text(encoding="utf-8"))
        cfg["artifacts"] = {"schematic": ["pcb/board.kicad_sch"], "pcb": ["pcb/board.kicad_pcb"], "project": ["pcb/board.kicad_pro"],
                            "rules": ["pcb/board.kicad_dru"], "gerbers": ["pcb/board-F_Cu.gbr"], "drill": ["pcb/board.drl"],
                            "layout_intent": ["design/nets.tsv"], "rf_intent": ["design/rf.tsv"]}
        cfg["checks"] = {"AUTO-LAYOUT": ["layout", "pcb/board.kicad_pcb", "design"]}
        (root / "anvil-project.json").write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8")
        anvil.plan(root)
        self.assertEqual(anvil.main(["manifest", str(root)]), 0)
        self.assertEqual(anvil.record(root, "AUTO-LAYOUT"), ("RECORDED: AUTO-LAYOUT pass", True))
        receipt = json.loads((root / "evidence" / "AUTO-LAYOUT.json").read_text(encoding="utf-8"))
        self.assertTrue({"pcb/board.kicad_pcb", "design/nets.tsv", "design/rf.tsv"} <= receipt["files"].keys())
        self.assertIn("kicad", receipt["tool_version"].lower())
        verdict, blockers = anvil.gate(root, "G3")
        self.assertFalse([b for b in blockers if b.startswith("AUTO-LAYOUT")], blockers)
        with mock.patch.object(anvil, "engine_digest", return_value="0" * 64):  # a changed analysis module voids the receipt
            self.assertTrue([b for b in anvil.gate(root, "G3")[1] if "checker version" in b])
        with (root / "design" / "nets.tsv").open("a", encoding="utf-8") as stream:  # an edited intent table invalidates the receipt
            stream.write("LV\tsignal\t-\t-\t5\t-\t-\t-\t-\t-\t-\t-\t-\t\n")
        verdict, blockers = anvil.gate(root, "G3")
        self.assertTrue([b for b in blockers if b.startswith("AUTO-LAYOUT")], blockers)

    def test_emc_loop_from_copper(self):
        import anvil_emc as EMC
        board = FB.write_board(self.dir / "emc.kicad_pcb")
        design = self.dir / "design"
        design.mkdir()
        (design / "emc.tsv").write_text("net\tv_swing\tf_clock_hz\tduty\trise_ps\tlimit\ttraces\nRF\t3.3\t50e6\t0.5\t1000\tfcc_b\t\n", encoding="utf-8")
        label, ok = EMC.evaluate(board, design)
        self.assertTrue(ok, "\n".join(anvil.DETAILS))
        note = next(d for d in anvil.DETAILS if "loop " in d)
        self.assertIn("loop 6 mm^2 (30.0 mm routed)", note)  # 30 mm trace, 0.2 mm to its plane
        import anvil_report
        rows = anvil_report.margins("\n".join(anvil.DETAILS))
        self.assertEqual([(r["id"], r["units"], r["status"]) for r in rows], [("RF:excess_over_fcc_b", "dB", "PASS")])

    @unittest.skipUnless(os.environ.get("ANVIL_EM_TESTS") == "1", "openEMS runs take ~10 minutes: set ANVIL_EM_TESTS=1")
    def test_em_microstrip_agrees_with_field_solver(self):
        runs = {}
        for length in (30, 20):  # two lengths: the phase difference cancels the port landings
            root = self.dir / f"len{length}"
            design = root / "design"
            design.mkdir(parents=True)
            (design / "em.tsv").write_text("name\tnets\tports\tf_start_hz\tf_stop_hz\tchecks\ttraces\n"
                                           "rfline\tRF\tJ1.1,U1.1\t0.5e9\t6e9\tS11<=-15@0.5e9:6e9;S21>=-1.5@0.5e9:6e9\t\n", encoding="utf-8")
            label, ok = E.evaluate(FB.write_board(root / "line.kicad_pcb", rf_len=length), design)
            self.assertTrue(ok, "\n".join(anvil.DETAILS))
            runs[length] = E.read_touchstone(root / "analysis" / "em" / "rfline.s2p")
        f, s30, _ = runs[30]
        s20 = runs[20][1]
        # reciprocity from two runs: ~1e-6 mid-band, 2.6e-5 at the band edges where the pulse is 20 dB down
        self.assertLess(float(np.max(np.abs(s30[:, 0, 1] - s30[:, 1, 0]))), 1e-4)
        zin = 50 * (1 + s30[:, 0, 0]) / (1 - s30[:, 0, 0])
        ref = F.stack_line([(0.2, 4.2)], [], 0.36, 0.035)  # FDTD omits the mask
        self.assertLess(abs(float(np.interp(1e9, f, zin.real)) - ref["z0"]) / ref["z0"], 0.02)
        dphi = np.unwrap(np.angle(s30[:, 1, 0])) - np.unwrap(np.angle(s20[:, 1, 0]))
        eeff = (-dphi * F.C0 / (2 * np.pi * f * 0.010)) ** 2
        band = (f >= 1e9) & (f <= 6e9)
        err = np.abs(eeff[band] - ref["er_eff"]) / ref["er_eff"]
        self.assertLess(float(err.mean()), 0.015)
        self.assertLess(float(err.max()), 0.025)
        # loss of the extra 10 mm (mismatch removed) vs the analytic dielectric loss at f_stop, where the model's
        # conductivity is exact (Pozar 3.198): recorded 0.171 vs 0.169 dB
        entered30 = np.abs(s30[:, 1, 0]) ** 2 / (1 - np.abs(s30[:, 0, 0]) ** 2)
        entered20 = np.abs(s20[:, 1, 0]) ** 2 / (1 - np.abs(s20[:, 0, 0]) ** 2)
        loss = float(np.mean(10 * np.log10(entered20[band] / entered30[band])))
        k0, er = 2 * np.pi * 6e9 / F.C0, 4.2
        analytic = 8.686 * k0 * er * (ref["er_eff"] - 1) * 0.02 / (2 * np.sqrt(ref["er_eff"]) * (er - 1)) * 0.010
        self.assertLess(abs(loss - analytic) / analytic, 0.05)


    @unittest.skipUnless(os.environ.get("ANVIL_EM_TESTS") == "1", "openEMS runs take ~10 minutes: set ANVIL_EM_TESTS=1")
    def test_em_coplanar_launch_agrees_with_field_solver(self):
        # 1.5 mm line with 0.3 mm gaps over a ground 1.53 mm down (an SMA pad over a cut-out): the ports drive the gaps
        design = self.dir / "design"
        design.mkdir()
        (design / "em.tsv").write_text("name\tnets\tports\tf_start_hz\tf_stop_hz\tchecks\ttraces\n"
                                       "cpw\tRF\tJ1.1,U1.1\t0.5e9\t4e9\tS11<=-15@0.5e9:4e9\t\n", encoding="utf-8")
        label, ok = E.evaluate(FB.write_cpw_board(self.dir / "cpw.kicad_pcb"), design)
        self.assertTrue(ok, "\n".join(anvil.DETAILS))
        self.assertTrue(any("across the coplanar gaps" in d for d in anvil.DETAILS), "\n".join(anvil.DETAILS))
        f, s, _ = E.read_touchstone(self.dir / "analysis" / "em" / "cpw.s2p")
        s11, s21 = s[:, 0, 0], s[:, 1, 0]
        z0 = 50 * np.sqrt(((1 + s11) ** 2 - s21 ** 2) / ((1 - s11) ** 2 - s21 ** 2))  # uniform-line Z0 from the S-matrix
        ref = F.stack_line([(1.53, 4.3)], [], 1.5, 0.035, gap=0.3)["z0"]
        band = (f >= 1e9) & (f <= 3e9)
        self.assertLess(float(np.max(np.abs(z0.real[band] - ref))) / ref, 0.03)

    @unittest.skipUnless(os.environ.get("ANVIL_EM_TESTS") == "1", "openEMS antenna run takes ~20 minutes: set ANVIL_EM_TESTS=1")
    def test_em_patch_antenna_resonance_and_feed(self):
        # Balanis TL-model patch for 2.45 GHz on 1.53 mm FR-4, probe 7 mm inside the radiating edge.
        # Recorded validation: resonance -3.2 % vs the TL model (converged: 2x z-cells moves it 0.15 %),
        # Re(Zin) 17.8 -> 48.2 ohm from 10.3 -> 7 mm feed, cos^2(pi y0/L) predicts the same ratio within 1 %.
        board = FB.write_patch_board(self.dir / "patch.kicad_pcb", feed_from_edge=7.0)
        design = self.dir / "design"
        design.mkdir()
        (design / "em.tsv").write_text("name\tnets\tports\tf_start_hz\tf_stop_hz\tchecks\tkind\tcopper\tref_net\ttraces\n"
                                       "patch\tANT\tFEED.1\t1.8e9\t3.2e9\tS11<=-10@2.36e9:2.41e9\tantenna\tsheet\tGND\t\n", encoding="utf-8")
        label, ok = E.evaluate(board, design)
        self.assertTrue(ok, "\n".join(anvil.DETAILS))
        f, s, _ = E.read_touchstone(self.dir / "analysis" / "em" / "patch.s1p")
        zin = 50 * (1 + s[:, 0, 0]) / (1 - s[:, 0, 0])
        k = int(np.argmax(zin.real))
        self.assertLess(abs(f[k] - 2.45e9) / 2.45e9, 0.04)  # Balanis TL model accuracy
        self.assertTrue(40 < zin.real[k] < 60, zin[k])


class Gate(unittest.TestCase):
    def test_released_intents_make_analyses_mandatory(self):
        cfg = dict(release_kind="pcb", features=["electronics"], sectors=["embedded"], markets=["US"],
                   artifacts={"layout_intent": ["design/nets.tsv"], "em_intent": ["design/em.tsv"], "sparams_intent": ["design/sparams.tsv"]})
        checks = {c["id"]: c for c in anvil.expected_checks(cfg)}
        self.assertEqual((checks["AUTO-LAYOUT"]["gate"], checks["AUTO-LAYOUT"]["criterion"]), ("G3", "layout"))
        self.assertEqual((checks["AUTO-EM"]["gate"], checks["AUTO-EM"]["dimension"]), ("G3", "simulation"))
        self.assertEqual(checks["AUTO-SPARAMS"]["gate"], "G4")
        self.assertNotIn("AUTO-PDN", checks)


if __name__ == "__main__":
    unittest.main()
