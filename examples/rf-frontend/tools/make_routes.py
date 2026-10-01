"""Pre-routes for rffe, computed from the placed board's real pad centres (Anvil's board dump):
- RF lines: 0.32 mm (49.7 ohm grounded coplanar on this stackup, tools/size_rf_line.py) J1-C1-U2-C2-J2 along the
  RF axis, plus the stub from the line to the RF choke L1;
- GND via fence 1.0 mm off each side of the RF line, <= 1.5 mm pitch (lambda/10 at 6 GHz is 2.8 mm: ARCH-065);
- plane fanouts: every SMD pad on GND or +3V3 gets a short track to a via into its plane (In1 GND / In2 +3V3),
  so the autorouter never has to carry plane nets and the PDN loop stays short;
- thermal vias: a 2 x 3 array in the GALI-84 ground tab (0.44 W into the In1 plane);
- stitching: GND vias on a 4 mm grid wherever the pour is free, tying F.Cu/B.Cu pour fragments to In1.
Every via keeps 0.3 mm from all other copper and 0.8 mm from the board edge. Writes design/routes.tsv."""
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parents[1] / "scripts"))
import anvil_board  # noqa: E402

WIDTH, VIA, DRILL, OFFSET, PITCH, KEEP, EDGE = 0.32, 0.6, 0.3, 1.0, 1.5, 0.3, 0.8
board = anvil_board.dump_board(ROOT / "pcb" / "rffe-placed.kicad_pcb")
pads = board["pads"]
pad = {f"{p['ref']}.{p['number']}": p for p in pads if not (p["ref"] in {"J1", "J2", "J3"} and p["number"] == "2")}
outline = [q for poly in board["outline"] for q in poly["outline"]]
X0, Y0 = min(q[0] for q in outline), min(q[1] for q in outline)
X1, Y1 = max(q[0] for q in outline), max(q[1] for q in outline)


def at(name):
    return pad[name]["x"], pad[name]["y"]


def box(p):
    pts = [q for shapes in p["shapes"].values() for poly in shapes for q in poly["outline"]]
    return min(q[0] for q in pts), min(q[1] for q in pts), max(q[0] for q in pts), max(q[1] for q in pts)


rows, blocked = [], [(box(p), p["net"]) for p in pads]  # (bbox, net) of every copper feature placed so far


def seg_box(x1, y1, x2, y2, w):
    return (min(x1, x2) - w / 2, min(y1, y2) - w / 2, max(x1, x2) + w / 2, max(y1, y2) + w / 2)


def free(x, y, r, net, keep=KEEP):
    if not (X0 + EDGE <= x <= X1 - EDGE and Y0 + EDGE <= y <= Y1 - EDGE):
        return False
    return all(n == net and keep == 0 or x < bx0 - r - keep or x > bx1 + r + keep or y < by0 - r - keep or y > by1 + r + keep
               for (bx0, by0, bx1, by1), n in blocked)


def track(net, x1, y1, x2, y2, w=WIDTH):
    rows.append(("track", net, "F.Cu", w, round(x1, 4), round(y1, 4), round(x2, 4), round(y2, 4), ""))
    blocked.append((seg_box(x1, y1, x2, y2, w), net))


def via(net, x, y):
    rows.append(("via", net, "F.Cu", VIA, round(x, 4), round(y, 4), "", "", DRILL))
    blocked.append(((x - VIA / 2, y - VIA / 2, x + VIA / 2, y + VIA / 2), net))


# 1. RF lines
for net, a, b in [("RF_IN", "J1.1", "C1.1"), ("RF_A", "C1.2", "U2.1"), ("RF_B", "U2.3", "C2.1"), ("RF_OUT", "C2.2", "J2.1")]:
    track(net, *at(a), *at(b))
lx, ly = at("L1.1")
track("RF_B", lx, at("U2.3")[1], lx, ly)

# 1b. clock output: a pre-routed line on F.Cu over the In1 ground plane (R2 -> right -> down to the J3 launch)
cx, cy = at("R2.2")
jx, jy = at("J3.1")
track("CLK_OUT", cx, cy, jx, cy)
track("CLK_OUT", jx, cy, jx, jy)

# 1c. edge-launch ground: vias in each SMA ground pad and a row between ground and centre pads
for ref in ("J1", "J2", "J3"):
    centre = pad[f"{ref}.1"]
    cx0, cy0, cx1, cy1 = box(centre)
    along_x = (cx1 - cx0) > (cy1 - cy0)
    for g in [p for p in pads if p["ref"] == ref and p["number"] == "2" and "F.Cu" in p["shapes"]]:
        gx0, gy0, gx1, gy1 = box(g)
        for f in (0.2, 0.5, 0.8):
            x = gx0 + (gx1 - gx0) * f if along_x else (gx0 + gx1) / 2
            y = (gy0 + gy1) / 2 if along_x else gy0 + (gy1 - gy0) * f
            rows.append(("via", "GND", "F.Cu", VIA, round(x, 4), round(y, 4), "", "", DRILL))
            mx, my = (x, (y + centre["y"]) / 2) if along_x else ((x + centre["x"]) / 2, y)
            if free(mx, my, VIA / 2, "GND"):
                via("GND", mx, my)

# 2. thermal vias (2 x 3, iteration 3) in the GALI-84 tab (pad 2's polygon extends away from the pin row)
tab = box(pad["U2.2"])
row_y = at("U2.1")[1]
far = tab[1] if abs(tab[1] - row_y) > abs(tab[3] - row_y) else tab[3]
for fx in (0.25, 0.75):
    for fy in (0.2, 0.45, 0.7):
        x = tab[0] + (tab[2] - tab[0]) * fx
        y = far + (row_y - far) * fy
        rows.append(("via", "GND", "F.Cu", VIA, round(x, 4), round(y, 4), "", "", DRILL))

# 3. fence along the RF line: greedy walk at 0.05 mm resolution, a via as late as possible but never more than
#    PITCH after the previous one (or as soon as clearance allows where parts interrupt the fence)
y_line = at("J1.1")[1]
x_start, x_end = X0 + EDGE, X1 - EDGE
for side in (-1, 1):
    y = y_line + side * OFFSET
    candidates = [x_start + 0.05 * i for i in range(int((x_end - x_start) / 0.05) + 1)]
    last = None
    for i, x in enumerate(candidates):
        if not free(x, y, VIA / 2, "GND"):
            continue
        nxt = candidates[i + 1] if i + 1 < len(candidates) else None
        due = last is None or x - last >= PITCH - 0.05 or (nxt is not None and nxt - last > PITCH and not free(nxt, y, VIA / 2, "GND"))
        if due and (last is None or x - last >= VIA + KEEP):
            via("GND", x, y)
            last = x

# 4. plane fanouts for every SMD pad on GND / +3V3 (not the SMA launches: their ground pads sit in the pour)
for p in pads:
    if p["net"] not in {"GND", "+3V3"} or p["attribute"] != "smd" or p["ref"] in {"J1", "J2", "J3"} or (p["ref"], p["number"]) == ("U2", "2"):
        continue
    x0, y0, x1, y1 = box(p)
    for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)):
        reach_x = (x1 - x0) / 2 + VIA / 2 + 0.35 if dx else 0
        reach_y = (y1 - y0) / 2 + VIA / 2 + 0.35 if dy else 0
        vx, vy = p["x"] + dx * reach_x, p["y"] + dy * reach_y
        if free(vx, vy, VIA / 2, p["net"]):
            track(p["net"], p["x"], p["y"], vx, vy, 0.3)
            via(p["net"], vx, vy)
            break
    else:
        print(f"WARNING: no room for a plane via at {p['ref']}.{p['number']} ({p['net']})")

# 5. GND stitching: 2 mm grid within 6 mm of the RF line (pour tips <= lambda_eff/20 at 5 GHz, WILLIAMS-2038),
#    4 mm grid elsewhere
for pitch, near in ((2.0, True), (4.0, False)):
    for gx in [X0 + 1.0 + pitch * i for i in range(int((X1 - X0 - 2) // pitch) + 1)]:
        for gy in [Y0 + 1.0 + pitch * j for j in range(int((Y1 - Y0 - 2) // pitch) + 1)]:
            if (abs(gy - y_line) <= 6.0) == near and free(gx, gy, VIA / 2, "GND", keep=0.45):
                via("GND", gx, gy)

# 6. gap fill: the pour within 5 mm of the RF line must lie within LIMIT of a GND via (the `layout` stitching rule,
#    lambda_eff/20 at 5 GHz = 1.66 mm); put a via at the nearest legal spot to the worst point until it holds
import numpy as np  # noqa: E402
import anvil_layout as L  # noqa: E402

LIMIT = 1.5
geo = L.Board(board)
gx, gy = np.meshgrid(np.arange(X0, X1, 0.25), np.arange(Y0, Y1, 0.25))
gx, gy = gx.ravel(), gy.ravel()
rf_x0, rf_x1 = at("J1.1")[0], at("J2.1")[0]
band = (np.abs(gy - y_line) <= 5.0) & (gx >= rf_x0 - 5) & (gx <= rf_x1 + 5)
pour = band & geo.covered("GND", "F.Cu", gx, gy)
for (bx0, by0, bx1, by1), _ in blocked:  # copper added since the dump (RF lines, fanouts) is not pour
    pour &= ~((gx >= bx0 - 0.3) & (gx <= bx1 + 0.3) & (gy >= by0 - 0.3) & (gy <= by1 + 0.3))
pts = np.column_stack([gx[pour], gy[pour]])
for _ in range(60):
    vias = np.array([[r[4], r[5]] for r in rows if r[0] == "via" and r[1] == "GND"])
    d = np.min(np.hypot(pts[:, None, 0] - vias[None, :, 0], pts[:, None, 1] - vias[None, :, 1]), axis=1)
    order = np.argsort(-d)
    if d[order[0]] <= LIMIT:
        break
    placed = False
    for k in order[:40]:
        if d[k] <= LIMIT:
            break
        px, py = pts[k]
        for r in (0.0, 0.25, 0.5, 0.75, 1.0):
            for a in range(0, 360, 30 if r else 360):
                x, y = px + r * math.cos(math.radians(a)), py + r * math.sin(math.radians(a))
                if free(x, y, VIA / 2, "GND"):
                    via("GND", x, y)
                    placed = True
                    break
            if placed:
                break
        if placed:
            break
    if not placed:
        print(f"WARNING: pour at ({pts[order[0]][0]:.2f},{pts[order[0]][1]:.2f}) is {d[order[0]]:.2f} mm from a GND via; no legal spot nearby")
        break

out = ROOT / "design" / "routes.tsv"
head = "# Pre-routed copper for `place --routes` (generated by tools/make_routes.py from the placed pad centres)\n"
cols = "kind\tnet\tlayer\twidth_mm\tx1\ty1\tx2\ty2\tdrill_mm\n"
out.write_text(head + cols + "".join("\t".join(str(c) for c in r) + "\n" for r in rows), encoding="utf-8")
kinds = {}
for r in rows:
    kinds[(r[0], r[1])] = kinds.get((r[0], r[1]), 0) + 1
print(f"ROUTES: {len(rows)} items {dict(sorted(kinds.items()))} -> {out}")
