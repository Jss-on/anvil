"""Synthetic 4-layer KiCad board for layout-truth tests (written as KiCad 8 text; KiCad 9/10 load it)."""
import uuid
from pathlib import Path

LAYERS = ('(0 "F.Cu" signal) (1 "In1.Cu" signal) (2 "In2.Cu" signal) (31 "B.Cu" signal) (36 "B.SilkS" user "B.Silkscreen") '
          '(37 "F.SilkS" user "F.Silkscreen") (38 "B.Mask" user) (39 "F.Mask" user) (44 "Edge.Cuts" user) '
          '(46 "B.CrtYd" user "B.Courtyard") (47 "F.CrtYd" user "F.Courtyard") (48 "B.Fab" user) (49 "F.Fab" user)')
STACKUP = ('(stackup (layer "F.SilkS" (type "Top Silk Screen")) (layer "F.Mask" (type "Top Solder Mask") (thickness 0.01) (epsilon_r 3.3)) '
           '(layer "F.Cu" (type "copper") (thickness 0.035)) '
           '(layer "dielectric 1" (type "prepreg") (thickness 0.2) (material "FR4") (epsilon_r 4.2) (loss_tangent 0.02)) '
           '(layer "In1.Cu" (type "copper") (thickness 0.035)) '
           '(layer "dielectric 2" (type "core") (thickness 1.065) (material "FR4") (epsilon_r 4.5) (loss_tangent 0.02)) '
           '(layer "In2.Cu" (type "copper") (thickness 0.035)) '
           '(layer "dielectric 3" (type "prepreg") (thickness 0.2) (material "FR4") (epsilon_r 4.2) (loss_tangent 0.02)) '
           '(layer "B.Cu" (type "copper") (thickness 0.035)) (layer "B.Mask" (type "Bottom Solder Mask") (thickness 0.01) (epsilon_r 3.3)) '
           '(layer "B.SilkS" (type "Bottom Silk Screen")) (copper_finish "None") (dielectric_constraints no))')
NETS = ["", "GND", "RF", "PWR", "HV", "LV", "DP", "DN"]


def uid():
    return str(uuid.uuid4())


def segment(x1, y1, x2, y2, width, layer, net):
    return f'(segment (start {x1} {y1}) (end {x2} {y2}) (width {width}) (layer "{layer}") (net {NETS.index(net)}) (uuid "{uid()}"))'


def via(x, y, net="GND"):
    return f'(via (at {x} {y}) (size 0.6) (drill 0.3) (layers "F.Cu" "B.Cu") (net {NETS.index(net)}) (uuid "{uid()}"))'


def footprint(ref, x, y, net, size=(0.36, 0.6), value="PAD", name="anvil:PAD", pads=None, nets=None):
    """SMD footprint on F.Cu; default one pad (an EM port landing). pads: [(number, dx, dy, w, h, net)]."""
    nets = nets or NETS
    effects = "(effects (font (size 0.5 0.5) (thickness 0.1)))"
    pads = pads or [("1", 0, 0, size[0], size[1], net)]
    body = " ".join(f'(pad "{n}" smd rect (at {dx} {dy}) (size {w} {h}) (layers "F.Cu" "F.Mask") (net {nets.index(pn)} "{pn}") (uuid "{uid()}"))'
                    for n, dx, dy, w, h, pn in pads)
    return (f'(footprint "{name}" (layer "F.Cu") (uuid "{uid()}") (at {x} {y}) '
            f'(property "Reference" "{ref}" (at 0 -1 0) (layer "F.SilkS") (uuid "{uid()}") {effects}) '
            f'(property "Value" "{value}" (at 0 1 0) (layer "F.Fab") (uuid "{uid()}") {effects}) (attr smd) {body})')


def zone(layer, pts, net="GND", clearance=0.2):
    pts_text = " ".join(f"(xy {x} {y})" for x, y in pts)
    return (f'(zone (net {NETS.index(net)}) (net_name "{net}") (layer "{layer}") (uuid "{uid()}") (hatch edge 0.5) '
            f'(connect_pads (clearance {clearance})) (min_thickness 0.2) (filled_areas_thickness no) '
            f'(fill yes (thermal_gap 0.3) (thermal_bridge_width 0.3) (island_removal_mode 1)) (polygon (pts {pts_text})))')


def write_board(path, slot_under_rf=False, hv_gap=1.0, pour=None, rf_len=30):
    """RF microstrip (y=10, F.Cu) fenced by GND vias every 1 mm at +/-1.2 mm; diff pair on B.Cu over In2 GND;
    PWR 0.5 mm on B.Cu; HV/LV 0.5 mm traces on F.Cu with `hv_gap` mm edge spacing; GND planes on In1/In2.
    pour: None | "stitched" (F.Cu GND pour hugging the fence, 0.3 mm gap: grounded CPW) | "wide" (the same pour
    spread 5 mm past the fence ends: unstitched tips)."""
    items = [segment(5, 10, 5 + rf_len, 10, 0.36, "F.Cu", "RF"), segment(5, 20, 35, 20, 0.5, "B.Cu", "PWR"),
             segment(5, 25, 35, 25, 0.5, "F.Cu", "HV"), segment(5, 25 + 0.5 + hv_gap, 35, 25 + 0.5 + hv_gap, 0.5, "F.Cu", "LV"),
             segment(5, 15, 35, 15, 0.15, "B.Cu", "DP"), segment(5, 15.3, 35, 15.3, 0.15, "B.Cu", "DN")]
    items += [via(x, y) for x in range(5, 6 + rf_len) for y in (8.8, 11.2)]
    items += [footprint("J1", 5, 10, "RF"), footprint("U1", 5 + rf_len, 10, "RF")]  # RF port landings at the trace ends
    full = [(0.5, 0.5), (39.5, 0.5), (39.5, 29.5), (0.5, 29.5)]
    if slot_under_rf:  # two pours leave a 5 mm gap under the RF trace
        items += [zone("In1.Cu", [(0.5, 0.5), (15, 0.5), (15, 29.5), (0.5, 29.5)]), zone("In1.Cu", [(20, 0.5), (39.5, 0.5), (39.5, 29.5), (20, 29.5)])]
    else:
        items.append(zone("In1.Cu", full))
    items.append(zone("In2.Cu", full))
    if pour:
        x0, x1 = (4.5, 35.5) if pour == "stitched" else (0.5, 39.5)
        items.append(zone("F.Cu", [(x0, 8.0), (x1, 8.0), (x1, 12.0), (x0, 12.0)], clearance=0.3))
    text = (f'(kicad_pcb (version 20240108) (generator "anvil-test") (generator_version "8.0") (general (thickness 1.6) (legacy_teardrops no)) '
            f'(paper "A4") (layers {LAYERS}) (setup {STACKUP} (pad_to_mask_clearance 0)) '
            + " ".join(f'(net {i} "{n}")' for i, n in enumerate(NETS))
            + f' (gr_rect (start 0 0) (end 40 30) (stroke (width 0.1) (type default)) (fill none) (layer "Edge.Cuts") (uuid "{uid()}")) '
            + " ".join(items) + ")\n")
    Path(path).write_text(text, encoding="utf-8")
    return Path(path)


PATCH_NETS = ["", "GND", "ANT"]
TWO_LAYERS = ('(0 "F.Cu" signal) (31 "B.Cu" signal) (36 "B.SilkS" user "B.Silkscreen") (37 "F.SilkS" user "F.Silkscreen") '
              '(38 "B.Mask" user) (39 "F.Mask" user) (44 "Edge.Cuts" user) (46 "B.CrtYd" user "B.Courtyard") '
              '(47 "F.CrtYd" user "F.Courtyard") (48 "B.Fab" user) (49 "F.Fab" user)')
TWO_STACKUP = ('(stackup (layer "F.SilkS" (type "Top Silk Screen")) (layer "F.Mask" (type "Top Solder Mask") (thickness 0.01) (epsilon_r 3.3)) '
               '(layer "F.Cu" (type "copper") (thickness 0.035)) '
               '(layer "dielectric 1" (type "core") (thickness 1.53) (material "FR4") (epsilon_r 4.3) (loss_tangent 0.02)) '
               '(layer "B.Cu" (type "copper") (thickness 0.035)) (layer "B.Mask" (type "Bottom Solder Mask") (thickness 0.01) (epsilon_r 3.3)) '
               '(layer "B.SilkS" (type "Bottom Silk Screen")) (copper_finish "None") (dielectric_constraints no))')


def patch_design(f_hz=2.45e9, er=4.3, h=1.53):
    """Balanis transmission-line-model rectangular patch (Antenna Theory §14.2.2): W, L, eps_eff, dL in mm."""
    c = 299_792_458.0
    w = c / (2 * f_hz) * (2 / (er + 1)) ** 0.5 * 1e3
    eeff = (er + 1) / 2 + (er - 1) / 2 * (1 + 12 * h / w) ** -0.5
    dl = 0.412 * h * (eeff + 0.3) * (w / h + 0.264) / ((eeff - 0.258) * (w / h + 0.8))
    return w, c / (2 * f_hz * eeff ** 0.5) * 1e3 - 2 * dl, eeff, dl


def write_patch_board(path, f_hz=2.45e9, feed_from_edge=10.3):
    """2-layer 70 x 70 mm board, B.Cu ground pour, Balanis-sized F.Cu patch (net ANT, a zone) centred at
    (35, 35) and resonant along y; FEED.1 is the probe-feed landing `feed_from_edge` mm inside the edge."""
    w, length, _, _ = patch_design(f_hz)
    x0, x1, y0, y1 = 35 - w / 2, 35 + w / 2, 35 - length / 2, 35 + length / 2

    def pzone(layer, net, pts):
        pts_text = " ".join(f"(xy {x:.4f} {y:.4f})" for x, y in pts)
        return (f'(zone (net {PATCH_NETS.index(net)}) (net_name "{net}") (layer "{layer}") (uuid "{uid()}") (hatch edge 0.5) '
                f'(connect_pads yes (clearance 0.2)) (min_thickness 0.2) (filled_areas_thickness no) '
                f'(fill yes (thermal_gap 0.3) (thermal_bridge_width 0.3) (island_removal_mode 1)) (polygon (pts {pts_text})))')

    items = [footprint("FEED", 35, round(y0 + feed_from_edge, 4), "ANT", size=(1.0, 1.0), nets=PATCH_NETS),
             pzone("F.Cu", "ANT", [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]),
             pzone("B.Cu", "GND", [(0.5, 0.5), (69.5, 0.5), (69.5, 69.5), (0.5, 69.5)])]
    text = (f'(kicad_pcb (version 20240108) (generator "anvil-test") (generator_version "8.0") (general (thickness 1.6) (legacy_teardrops no)) '
            f'(paper "A4") (layers {TWO_LAYERS}) (setup {TWO_STACKUP} (pad_to_mask_clearance 0)) '
            + " ".join(f'(net {i} "{n}")' for i, n in enumerate(PATCH_NETS))
            + f' (gr_rect (start 0 0) (end 70 70) (stroke (width 0.1) (type default)) (fill none) (layer "Edge.Cuts") (uuid "{uid()}")) '
            + " ".join(items) + ")\n")
    Path(path).write_text(text, encoding="utf-8")
    return Path(path)


def write_cpw_board(path, w=1.5, gap=0.3, length=20.0):
    """2-layer 1.53 mm FR-4 board: a coplanar line (F.Cu, `w` wide, `gap` to the F.Cu GND pour) over the B.Cu ground,
    pads J1/U1 as wide as the line at its ends, the pour stitched to B.Cu every 1 mm on both sides. The ground plane
    is 5x farther than the gaps, like an SMA launch pad over an inner-layer cut-out."""
    x0, x1, yc = 5.0, 5.0 + length, 10.0
    items = [segment(x0, yc, x1, yc, w, "F.Cu", "RF"),
             footprint("J1", x0, yc, "RF", size=(1.0, w)), footprint("U1", x1, yc, "RF", size=(1.0, w)),
             zone("F.Cu", [(0.5, 0.5), (x1 + 4.5, 0.5), (x1 + 4.5, 19.5), (0.5, 19.5)], clearance=gap),
             zone("B.Cu", [(0.5, 0.5), (x1 + 4.5, 0.5), (x1 + 4.5, 19.5), (0.5, 19.5)])]
    items += [via(x, yc + side * (w / 2 + gap + 0.8)) for x in range(3, int(x1) + 3) for side in (-1, 1)]
    text = (f'(kicad_pcb (version 20240108) (generator "anvil-test") (generator_version "8.0") (general (thickness 1.6) (legacy_teardrops no)) '
            f'(paper "A4") (layers {TWO_LAYERS}) (setup {TWO_STACKUP} (pad_to_mask_clearance 0)) '
            + " ".join(f'(net {i} "{n}")' for i, n in enumerate(NETS[:3]))
            + f' (gr_rect (start 0 0) (end {x1 + 5} 20) (stroke (width 0.1) (type default)) (fill none) (layer "Edge.Cuts") (uuid "{uid()}")) '
            + " ".join(items) + ")\n")
    Path(path).write_text(text, encoding="utf-8")
    return Path(path)


PDN_NETS = ["", "GND", "VCC"]


def write_pdn_board(path, far_c3=True):
    """4-layer PDN board: In1 GND plane, In2 VCC plane (0.2 mm prepreg to each surface, 1.065 mm core between
    them). U2 is the load (VCC/GND pads with via-in-pad); C1 100 nF and C2 1 uF 0603 sit 5 mm away, C3 10 uF
    0805 sits 10 mm (or 3 mm) away; every cap pad fans out 0.6 mm to a via."""
    def seg(x1, y1, x2, y2, net):
        return f'(segment (start {x1} {y1}) (end {x2} {y2}) (width 0.3) (layer "F.Cu") (net {PDN_NETS.index(net)}) (uuid "{uid()}"))'

    def pvia(x, y, net):
        return f'(via (at {x} {y}) (size 0.6) (drill 0.3) (layers "F.Cu" "B.Cu") (net {PDN_NETS.index(net)}) (uuid "{uid()}"))'

    def pzone(layer, net):
        return (f'(zone (net {PDN_NETS.index(net)}) (net_name "{net}") (layer "{layer}") (uuid "{uid()}") (hatch edge 0.5) '
                f'(connect_pads yes (clearance 0.2)) (min_thickness 0.2) (filled_areas_thickness no) '
                f'(fill yes (thermal_gap 0.3) (thermal_bridge_width 0.3) (island_removal_mode 1)) '
                f'(polygon (pts (xy 0.5 0.5) (xy 39.5 0.5) (xy 39.5 29.5) (xy 0.5 29.5))))')

    items = [footprint("U2", 20, 15, None, value="LOAD", name="anvil:LOAD", nets=PDN_NETS,
                       pads=[("1", -1, 0, 0.8, 0.8, "VCC"), ("2", 1, 0, 0.8, 0.8, "GND"), ("3", 0, -1, 0.8, 0.8, "VCC"), ("4", 0, 1, 0.8, 0.8, "GND")]),
             pvia(19, 15, "VCC"), pvia(21, 15, "GND"), pvia(20, 14, "VCC"), pvia(20, 16, "GND")]
    caps = [("C1", 25, 15, "100n", "Capacitor_SMD:C_0603_1608Metric", 0.8), ("C2", 25, 18, "1u", "Capacitor_SMD:C_0603_1608Metric", 0.8),
            ("C3", 10 if far_c3 else 17, 15, "10u", "Capacitor_SMD:C_0805_2012Metric", 0.95)]
    for ref, x, y, value, name, half in caps:
        items.append(footprint(ref, x, y, None, value=value, name=name, nets=PDN_NETS,
                               pads=[("1", -half, 0, 0.9, 1.0, "VCC"), ("2", half, 0, 0.9, 1.0, "GND")]))
        items += [seg(x - half, y, x - half, y + 1.1, "VCC"), pvia(x - half, y + 1.1, "VCC"),
                  seg(x + half, y, x + half, y + 1.1, "GND"), pvia(x + half, y + 1.1, "GND")]
    items += [pzone("In1.Cu", "GND"), pzone("In2.Cu", "VCC")]
    text = (f'(kicad_pcb (version 20240108) (generator "anvil-test") (generator_version "8.0") (general (thickness 1.6) (legacy_teardrops no)) '
            f'(paper "A4") (layers {LAYERS}) (setup {STACKUP} (pad_to_mask_clearance 0)) '
            + " ".join(f'(net {i} "{n}")' for i, n in enumerate(PDN_NETS))
            + f' (gr_rect (start 0 0) (end 40 30) (stroke (width 0.1) (type default)) (fill none) (layer "Edge.Cuts") (uuid "{uid()}")) '
            + " ".join(items) + ")\n")
    Path(path).write_text(text, encoding="utf-8")
    return Path(path)


def write_intent(directory, rf_ghz=6.0):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    cols = "net\tkind\tcurrent_a\tmax_rise_c\tvoltage_v\tz_target\tz_tol_pct\tpair\tzdiff_target\tmax_length_mm\tmatch_group\tmatch_tol_mm\tref_net\ttraces\n"
    rows = ["RF\trf\t-\t-\t-\t50\t10\t-\t-\t40\t-\t-\tGND\t",
            "PWR\tpower\t2\t30\t-\t-\t-\t-\t-\t-\t-\t-\t-\t",
            "HV\tsignal\t-\t-\t230\t-\t-\t-\t-\t-\t-\t-\t-\t",
            "DP\tdiff\t-\t-\t-\t-\t10\tDN\t100\t-\tpair\t0.1\tGND\t",
            "DN\tdiff\t-\t-\t-\t-\t10\tDP\t100\t-\tpair\t0.1\tGND\t"]
    (directory / "nets.tsv").write_text(cols + "\n".join(rows) + "\n", encoding="utf-8")
    (directory / "rf.tsv").write_text("net\tf_max_hz\tsource\tmax_vias\tfence_pitch_mm\tfence_band_mm\tmatch_max_mm\tkeepout_refs\ttraces\n"
                                      f"RF\t{rf_ghz * 1e9:g}\t-\t0\t-\t1.5\t-\t-\t\n", encoding="utf-8")
    return directory
