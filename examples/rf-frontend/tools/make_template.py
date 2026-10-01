"""Board template for rffe: fabricator stackup (4 layers, 0.2 mm prepreg to the In1 ground plane), 50 x 36 mm
outline, In1 GND plane, In2 +3V3 plane, F.Cu/B.Cu ground pours with 0.3 mm clearance (the grounded-coplanar gap the
50-ohm width was solved for), and the SMA launch cut-outs. Anvil's `board` command adds the footprints and nets."""
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W, H = 50.0, 36.0
# SMA_Amphenol_132289_EdgeMount centre pad: 5.08 x 1.5 mm at the footprint origin, long side on the footprint x axis.
# Over In1 at 0.2 mm it is an 18 ohm section (openEMS: S11 -6 dB at 2.4 GHz); with In1 and In2 cut out beneath it
# references B.Cu 1.535 mm down and field-solves to 47.8 ohm with the 0.3 mm coplanar gap (iteration 10).
LAUNCH_PAD, LAUNCH_SIDE = (5.08, 1.5), 1.0  # cut-out reaches 1.0 mm beyond each pad side (5x the prepreg)
LAYERS = ('(0 "F.Cu" signal) (1 "In1.Cu" power) (2 "In2.Cu" power) (31 "B.Cu" signal) (32 "B.Adhes" user "B.Adhesive") '
          '(33 "F.Adhes" user "F.Adhesive") (34 "B.Paste" user) (35 "F.Paste" user) (36 "B.SilkS" user "B.Silkscreen") '
          '(37 "F.SilkS" user "F.Silkscreen") (38 "B.Mask" user) (39 "F.Mask" user) (40 "Dwgs.User" user "User.Drawings") '
          '(44 "Edge.Cuts" user) (45 "Margin" user) (46 "B.CrtYd" user "B.Courtyard") (47 "F.CrtYd" user "F.Courtyard") '
          '(48 "B.Fab" user) (49 "F.Fab" user)')
STACKUP = ('(stackup (layer "F.SilkS" (type "Top Silk Screen")) (layer "F.Paste" (type "Top Solder Paste")) '
           '(layer "F.Mask" (type "Top Solder Mask") (thickness 0.01) (epsilon_r 3.3)) (layer "F.Cu" (type "copper") (thickness 0.035)) '
           '(layer "dielectric 1" (type "prepreg") (thickness 0.2) (material "FR4") (epsilon_r 4.2) (loss_tangent 0.02)) '
           '(layer "In1.Cu" (type "copper") (thickness 0.035)) '
           '(layer "dielectric 2" (type "core") (thickness 1.065) (material "FR4") (epsilon_r 4.5) (loss_tangent 0.02)) '
           '(layer "In2.Cu" (type "copper") (thickness 0.035)) '
           '(layer "dielectric 3" (type "prepreg") (thickness 0.2) (material "FR4") (epsilon_r 4.2) (loss_tangent 0.02)) '
           '(layer "B.Cu" (type "copper") (thickness 0.035)) (layer "B.Mask" (type "Bottom Solder Mask") (thickness 0.01) (epsilon_r 3.3)) '
           '(layer "B.Paste" (type "Bottom Solder Paste")) (layer "B.SilkS" (type "Bottom Silk Screen")) '
           '(copper_finish "ENIG") (dielectric_constraints no))')
NETS = ["", "GND", "+3V3"]


def uid():
    return str(uuid.uuid4())


def zone(layer, net, inset, clearance, priority):
    pts = [(inset, inset), (W - inset, inset), (W - inset, H - inset), (inset, H - inset)]
    text = " ".join(f"(xy {x} {y})" for x, y in pts)
    return (f'(zone (net {NETS.index(net)}) (net_name "{net}") (layer "{layer}") (uuid "{uid()}") (hatch edge 0.5) (priority {priority}) '
            f'(connect_pads yes (clearance {clearance})) (min_thickness 0.2) (filled_areas_thickness no) '
            f'(fill yes (thermal_gap 0.3) (thermal_bridge_width 0.3) (island_removal_mode 0)) (polygon (pts {text})))')


def launch_cutouts():
    """No-pour rule areas on In1/In2 under the J1/J2 centre pads (placed from design/placement.tsv)."""
    rows = [line.split("\t") for line in (ROOT / "design" / "placement.tsv").read_text(encoding="utf-8").splitlines()
            if line and not line.startswith(("#", "ref\t"))]
    out = []
    for ref, x, y, rot, *_ in [r for r in rows if r[0] in {"J1", "J2"}]:
        x, y, rot = float(x), float(y), float(rot) % 180
        half = (LAUNCH_PAD[0] / 2, LAUNCH_PAD[1] / 2 + LAUNCH_SIDE) if rot == 0 else (LAUNCH_PAD[1] / 2 + LAUNCH_SIDE, LAUNCH_PAD[0] / 2)
        pts = " ".join(f"(xy {px:.3f} {py:.3f})" for px, py in ((x - half[0], y - half[1]), (x + half[0], y - half[1]),
                                                              (x + half[0], y + half[1]), (x - half[0], y + half[1])))
        out.append(f'(zone (net 0) (net_name "") (layers "In1.Cu" "In2.Cu") (uuid "{uid()}") (name "launch {ref}") (hatch edge 0.5) '
                   f'(connect_pads (clearance 0)) (min_thickness 0.25) (filled_areas_thickness no) '
                   f'(keepout (tracks allowed) (vias allowed) (pads allowed) (copperpour not_allowed) (footprints allowed)) '
                   f'(fill (thermal_gap 0.5) (thermal_bridge_width 0.5)) (polygon (pts {pts})))')
    return out


def main():
    items = [f'(gr_rect (start 0 0) (end {W} {H}) (stroke (width 0.05) (type default)) (fill none) (layer "Edge.Cuts") (uuid "{uid()}"))',
             zone("In1.Cu", "GND", 0.3, 0.3, 0), zone("In2.Cu", "+3V3", 1.0, 0.3, 0),  # power plane pulled back 1 mm (edge fringing)
             zone("F.Cu", "GND", 0.3, 0.3, 0), zone("B.Cu", "GND", 0.3, 0.3, 0)] + launch_cutouts()
    text = (f'(kicad_pcb (version 20240108) (generator "anvil-showcase") (generator_version "8.0") '
            f'(general (thickness 1.6) (legacy_teardrops no)) (paper "A4") '
            f'(title_block (title "rffe: 2.4 GHz gain block + 25 MHz reference") (rev "A") (company "Anvil showcase")) '
            f'(layers {LAYERS}) (setup {STACKUP} (pad_to_mask_clearance 0)) '
            + " ".join(f'(net {i} "{n}")' for i, n in enumerate(NETS)) + " " + " ".join(items) + ")\n")
    out = ROOT / "pcb" / "template.kicad_pcb"
    out.write_text(text, encoding="utf-8")
    print(f"TEMPLATE: {out}")


if __name__ == "__main__":
    main()
