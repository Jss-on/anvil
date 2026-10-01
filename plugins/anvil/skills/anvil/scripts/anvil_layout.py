#!/usr/bin/env python3
"""Layout truth: design intent measured on the geometry KiCad itself reports.

`layout <pcb> <design-dir>` dumps the board through KiCad's own Python (anvil_pcb.py; zones refilled in
memory) and checks every row of design/nets.tsv (and design/rf.tsv) against the real copper:
- current: IPC-2152 trace heating per segment (Brooks & Adam fits) and via-group adequacy;
- voltage: IPC-2221 Table 6-1 spacing measured copper-to-copper on each layer;
- impedance: 2-D field solution of the actual cross-section (stackup from Board Setup, reference planes
  and coplanar grounds found in the refilled zones), single-ended and differential;
- routed length, match groups, and reference-plane continuity under fast/RF traces;
- RF (design/rf.tsv): via-fence pitch, stitching near RF copper, via count, sharp bends, matching-part
  proximity to the RF source, antenna keep-out rule areas.
numpy required. Every result is a margin row in the transcript; nothing is inferred from typed numbers.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

import anvil_fields as F
import anvil_rules as R
from anvil import DETAILS, OUTPUTS, compare, number, require, table, traces
from anvil_board import dump_board  # noqa: F401  (re-exported: every board analysis reads the dump from here)

C0 = 299_792_458.0
NETS = ("net", "kind", "current_a", "max_rise_c", "voltage_v", "z_target", "z_tol_pct", "pair", "zdiff_target",
        "max_length_mm", "match_group", "match_tol_mm", "ref_net", "traces")
RF = ("net", "f_max_hz", "source", "max_vias", "fence_pitch_mm", "fence_band_mm", "match_max_mm", "keepout_refs", "traces")
FAST = {"rf", "diff", "clock", "highspeed"}


# --- geometry ----------------------------------------------------------------------------------------------------
def ring_contains(ring, px, py):
    """Even-odd test of many points against one polygon ring."""
    ring = np.asarray(ring, dtype=float)
    x1, y1 = ring[:, 0], ring[:, 1]
    x2, y2 = np.roll(x1, -1), np.roll(y1, -1)
    inside = np.zeros(px.shape, dtype=bool)
    for a, b, c, d in zip(x1, y1, x2, y2):
        if b == d:
            continue
        crossing = ((b > py) != (d > py)) & (px < (c - a) * (py - b) / (d - b) + a)
        inside ^= crossing
    return inside


def polys_contain(polys, px, py):
    px, py = np.asarray(px, dtype=float), np.asarray(py, dtype=float)
    inside = np.zeros(px.shape, dtype=bool)
    for poly in polys:
        if not poly["outline"]:
            continue
        hit = ring_contains(poly["outline"], px, py)
        for hole in poly["holes"]:
            hit &= ~ring_contains(hole, px, py)
        inside |= hit
    return inside


def seg_distance(a, b):
    """Pairwise distance between segment arrays a (N,4) and b (M,4) -> (N,M)."""
    def point_seg(px, py, s):
        x1, y1, x2, y2 = s[:, 0][None, :], s[:, 1][None, :], s[:, 2][None, :], s[:, 3][None, :]
        dx, dy = x2 - x1, y2 - y1
        length2 = dx * dx + dy * dy
        t = np.clip(((px[:, None] - x1) * dx + (py[:, None] - y1) * dy) / np.where(length2 > 0, length2, 1.0), 0, 1)
        return np.hypot(px[:, None] - (x1 + t * dx), py[:, None] - (y1 + t * dy))
    d = np.minimum(np.minimum(point_seg(a[:, 0], a[:, 1], b), point_seg(a[:, 2], a[:, 3], b)),
                   np.minimum(point_seg(b[:, 0], b[:, 1], a).T, point_seg(b[:, 2], b[:, 3], a).T))
    def orient(ax, ay, bx, by, cx, cy):
        return np.sign((bx - ax) * (cy - ay) - (by - ay) * (cx - ax))
    A = [a[:, i][:, None] for i in range(4)]
    B = [b[:, i][None, :] for i in range(4)]
    o1, o2 = orient(*A[:2], *A[2:], *B[:2]), orient(*A[:2], *A[2:], *B[2:])
    o3, o4 = orient(*B[:2], *B[2:], *A[:2]), orient(*B[:2], *B[2:], *A[2:])
    return np.where((o1 * o2 < 0) & (o3 * o4 < 0), 0.0, d)


def ring_segments(ring):
    ring = np.asarray(ring, dtype=float)
    return np.hstack([ring, np.roll(ring, -1, axis=0)])


class Board:
    def __init__(self, data):
        self.data = data
        self.copper = data["copper_layers"]
        self.stack = stack_model(data)
        self.fills = {}
        for zone in data["zones"]:
            if not zone["rule_area"]:
                for layer, polys in zone["filled"].items():
                    self.fills.setdefault((zone["net"], layer), []).extend(polys)

    def outer(self, layer):
        return layer in (self.copper[0], self.copper[-1])

    def copper_t(self, layer):
        if self.stack:
            for c in self.stack["copper"]:
                if c["name"] == layer:
                    return c["t"]
        return 0.035

    def tracks(self, net):
        rows = [t for t in self.data["tracks"] if t["net"] == net]
        for arc in self.data["arcs"]:
            if arc["net"] == net:
                (x1, y1), (xm, ym), (x2, y2) = arc["start"], arc["mid"], arc["end"]
                rows += [dict(net=net, layer=arc["layer"], width=arc["width"], start=(x1, y1), end=(xm, ym)),
                         dict(net=net, layer=arc["layer"], width=arc["width"], start=(xm, ym), end=(x2, y2))]
        return rows

    def covered(self, net, layer, px, py):
        return polys_contain(self.fills.get((net, layer), []), px, py)

    def copper_segments(self, layer):
        """Every copper boundary on a layer as (segments (K,4), radius (K,), net list)."""
        segs, radius, nets = [], [], []
        for t in self.data["tracks"]:
            if t["layer"] == layer:
                segs.append((*t["start"], *t["end"]))
                radius.append(t["width"] / 2)
                nets.append(t["net"])
        index = {name: i for i, name in enumerate(self.copper)}
        for v in self.data["vias"]:
            if index.get(v["top"], 0) <= index.get(layer, -1) <= index.get(v["bottom"], len(self.copper)):
                segs.append((v["x"], v["y"], v["x"], v["y"]))
                radius.append(v["diameter"] / 2)
                nets.append(v["net"])
        for pad in self.data["pads"]:
            if layer in pad["layers"]:
                shapes = pad["shapes"].get(layer) or next(iter(pad["shapes"].values()), [])
                for poly in shapes:
                    for ring in [poly["outline"]] + poly["holes"]:
                        for s in ring_segments(ring):
                            segs.append(tuple(s))
                            radius.append(0.0)
                            nets.append(pad["net"])
        for (net, zlayer), polys in self.fills.items():
            if zlayer == layer:
                for poly in polys:
                    for ring in [poly["outline"]] + poly["holes"]:
                        for s in ring_segments(ring):
                            segs.append(tuple(s))
                            radius.append(0.0)
                            nets.append(net)
        return np.array(segs, dtype=float).reshape(-1, 4), np.array(radius), np.array(nets, dtype=object)


def stack_model(data):
    st = data.get("stackup")
    if not st:
        return None
    copper, gaps, masks, pending = [], [], {}, []
    for item in st["layers"]:
        kind = (item.get("type") or "").lower()
        if kind == "copper":
            if copper:
                gaps.append(pending)
            copper.append(dict(name=item["name"], t=item.get("thickness", 0.035)))
            pending = []
        elif kind in {"core", "prepreg"} or "dielectric" in item["name"].lower():
            require(item.get("thickness"), f"stackup dielectric {item['name']} has no thickness")
            pending.append((item["thickness"], item.get("epsilon_r", 4.5), item.get("loss_tangent", 0.02)))
        elif "mask" in kind or "mask" in item["name"].lower():
            masks["top" if not copper else "bottom"] = (item.get("thickness", 0.01), item.get("epsilon_r", 3.3))
    return dict(copper=copper, gaps=gaps, masks=masks)


# --- cross-section of a real trace ------------------------------------------------------------------------------
def side_gaps(board, layer, x, y, u, ref_nets, edge, reach):
    """Same-layer reference copper seen across the trace at (x, y): gap from each conductor edge (at +-edge
    along the normal of direction u) to the pour, 5 um steps out to `reach`; None where there is none."""
    n = np.array([-u[1], u[0]]) / (math.hypot(*u) or 1.0)
    d = np.arange(edge, edge + reach, 0.005)
    gaps = []
    for sign in (-1, 1):
        px, py = x + sign * n[0] * d, y + sign * n[1] * d
        hit = np.zeros(d.shape, dtype=bool)
        for net in ref_nets:
            hit |= board.covered(net, layer, px, py)
        gaps.append(round(float(d[hit.argmax()] - edge), 3) if hit.any() and d[hit.argmax()] > edge else None)
    return tuple(gaps) if any(gaps) else None


def cross_section_of(board, layer, x, y, ref_nets, w, u=(1.0, 0.0), edge=None):
    """Dielectric slabs toward the nearest reference plane(s) at (x, y), coplanar ground gaps per side, mask.
    edge: offset of the outer conductor edge from (x, y) (w/2 for one trace, s/2 + w from a pair's centre)."""
    require(board.stack, "board has no physical stackup: define the fabricator's stackup in Board Setup")
    names = [c["name"] for c in board.stack["copper"]]
    i = names.index(layer)

    def side(step):
        slabs, j = [], i
        while 0 <= j + step < len(names):
            gap = board.stack["gaps"][min(j, j + step)]
            slabs += [(t, er) for t, er, _ in (gap if step > 0 else reversed(gap))]
            j += step
            if any(board.covered(net, names[j], np.array([x]), np.array([y]))[0] for net in ref_nets):
                return slabs, True
            slabs.append((board.stack["copper"][j]["t"], slabs[-1][1]))  # an unplaned copper layer is dielectric here
        return slabs, False

    up, up_plane = side(-1)
    down, down_plane = side(+1)
    t = board.copper_t(layer)
    if up_plane and down_plane:
        below, above, top_plane, mask = down, up, True, None
    elif down_plane or up_plane:
        below = down if down_plane else up
        surface = up if down_plane else down
        above, top_plane = [s for s in surface if s], False
        mask = board.stack["masks"].get("top" if down_plane else "bottom")
    else:
        return None
    # pours farther than 5 h change Z0 by well under the solver error; beyond that the line is a microstrip
    gap = side_gaps(board, layer, x, y, u, ref_nets, w / 2 if edge is None else edge, 5 * sum(tk for tk, _ in below))
    return dict(below=below, above=above, top_plane=top_plane, mask=mask, t=t, gap=gap)


def depth_between(board, a, b):
    """Distance (mm) between two copper layers by stack index: dielectric plus the copper strictly between."""
    i, j = sorted((a, b))
    return sum(t for gap in board.stack["gaps"][i:j] for t, _, _ in gap) + sum(board.stack["copper"][k]["t"] for k in range(i + 1, j))


_SOLVED = {}


def solve_line(xs, w, s=None):
    key = (json.dumps(xs, sort_keys=True), round(w, 4), None if s is None else round(s, 4))
    if key not in _SOLVED:
        _SOLVED[key] = F.stack_line(xs["below"], xs["above"], w, xs["t"], top_plane=xs["top_plane"], mask=xs["mask"],
                                    s=s, gap=xs["gap"])
    return _SOLVED[key]


# --- the checks ---------------------------------------------------------------------------------------------------
def optional(row, key):
    value = row.get(key, "").strip()
    return None if value in {"", "-"} else value


def emit(results, check_id, value, units, op, limit, note=""):
    ok, margin = compare(f"{value:.9g}", op, str(limit))
    results.append(ok)
    DETAILS.append(f"{check_id}: {value:.6g} {units} margin={margin} {'PASS' if ok else 'FAIL'}")
    if note:
        DETAILS.append(f"  {note}")


def check_current(board, row, results):
    amps, limit = float(number(row["current_a"], minimum=0)), float(number(optional(row, "max_rise_c") or 20, positive=True))
    worst = None
    for t in board.tracks(row["net"]):
        rise = R.trace_rise_ipc2152(amps, t["width"], board.copper_t(t["layer"]), "external" if board.outer(t["layer"]) else "internal")["value"]
        if worst is None or rise > worst[0]:
            worst = (rise, t)
    require(worst, f"{row['net']}: no copper tracks found for a current-carrying net")
    emit(results, f"{row['net']}:trace_rise", worst[0], "C", "le", limit,
         f"narrowest heating: {worst[1]['width']} mm on {worst[1]['layer']} (IPC-2152 fit, lone trace in still air: BROOKS-046/048)")
    vias = [v for v in board.data["vias"] if v["net"] == row["net"]]
    groups, used = [], set()
    for i, v in enumerate(vias):
        if i in used:
            continue
        group = [j for j, u in enumerate(vias) if j not in used and math.hypot(u["x"] - v["x"], u["y"] - v["y"]) <= 2.0]
        used |= set(group)
        groups.append([vias[j] for j in group])
    narrow = worst[1]
    for n, group in enumerate(groups):
        ratio = R.via_group_adequacy(narrow["width"], board.copper_t(narrow["layer"]), len(group), min(v["drill"] for v in group))["value"]
        emit(results, f"{row['net']}:via_group{n + 1}", ratio, "ratio", "ge", 1.0,
             f"{len(group)} via(s) near ({group[0]['x']:.2f},{group[0]['y']:.2f}); 2*A_via/A_trace (BROOKS-079/081)")


def check_voltage(board, row, voltages, results):
    volts = float(number(row["voltage_v"]))
    net = row["net"]
    for layer in board.copper:
        segs, radius, owners = board.copper_segments(layer)
        mine = owners == net
        if not mine.any() or mine.all():
            continue
        others = np.where(~mine)[0]
        a, ra = segs[mine], radius[mine]
        nearest = {}
        for start in range(0, len(others), 4000):
            chunk = others[start:start + 4000]
            d = (seg_distance(a, segs[chunk]) - ra[:, None] - radius[chunk][None, :]).min(axis=0)
            for owner, dist in zip(owners[chunk], d):
                nearest[owner] = min(nearest.get(owner, math.inf), float(dist))
        condition = "B1" if not board.outer(layer) else (optional(row, "condition") or "B2")
        worst = None
        for owner, dist in nearest.items():  # the binding neighbour is the worst margin, not the nearest copper
            dv = abs(volts - voltages.get(owner, 0.0))
            required = R.clearance_ipc2221(dv, condition)["value"]
            if worst is None or dist - required < worst[0] - worst[1]:
                worst = (dist, required, owner, dv)
        emit(results, f"{net}:clearance@{layer}", worst[0], "mm", "ge", worst[1],
             f"binding neighbour {worst[2]} at {worst[3]:g} V difference; IPC-2221 Table 6-1 {condition} needs {worst[1]} mm")


def check_impedance(board, row, results):
    ref_nets = [n for n in (optional(row, "ref_net") or "GND").split(",") if n]
    target, tol = float(number(row["z_target"], positive=True)), float(number(optional(row, "z_tol_pct") or 10, positive=True))
    seen = {}
    own_pads = [p for p in board.data["pads"] if p["net"] == row["net"]]
    for t in board.tracks(row["net"]):
        u = np.subtract(t["end"], t["start"])
        length = math.hypot(*u)
        if length < 1e-6:
            continue
        # sample along the segment (a pour gap can change near pads), skipping points inside the net's own pads
        for frac in ((0.5,) if length < 1.0 else (0.1, 0.3, 0.5, 0.7, 0.9)):
            x, y = t["start"][0] + frac * u[0], t["start"][1] + frac * u[1]
            if any(polys_contain(p["shapes"].get(t["layer"]) or [], np.array([x]), np.array([y]))[0] for p in own_pads if t["layer"] in p["layers"]):
                continue
            xs = cross_section_of(board, t["layer"], x, y, ref_nets, t["width"], u)
            if xs is None:
                emit(results, f"{row['net']}:reference@({x:.2f},{y:.2f})", 0.0, "planes", "ge", 1, f"no {ref_nets} plane on either side of {t['layer']}")
                continue
            key = (t["layer"], round(t["width"], 4), xs["gap"])
            if key not in seen:
                seen[key] = solve_line(xs, t["width"])["z0"]
    for (layer, width, gap), z in seen.items():
        shown = "" if not gap else "/gap" + "|".join("-" if g is None else f"{g:g}" for g in gap)
        emit(results, f"{row['net']}:z0@{layer}/{width}mm{shown}", z, "ohm", "within", f"{target}±{tol}%",
             "2-D field solution of the board stackup and refilled reference copper (validated <1 % vs exact solutions)")


def check_pair(board, row, results):
    other, target = row["pair"], float(number(row["zdiff_target"], positive=True))
    tol = float(number(optional(row, "z_tol_pct") or 10, positive=True))
    ref_nets = [n for n in (optional(row, "ref_net") or "GND").split(",") if n]
    mine, theirs = board.tracks(row["net"]), board.tracks(other)
    seen = {}
    for a in mine:
        ax, ay = (a["start"][0] + a["end"][0]) / 2, (a["start"][1] + a["end"][1]) / 2
        va = np.subtract(a["end"], a["start"])
        best = None
        for b in theirs:
            if b["layer"] != a["layer"]:
                continue
            vb = np.subtract(b["end"], b["start"])
            if np.linalg.norm(va) < 1e-6 or np.linalg.norm(vb) < 1e-6:
                continue
            if abs(abs(np.dot(va, vb)) / np.linalg.norm(va) / np.linalg.norm(vb) - 1) > 0.004:
                continue  # not parallel (> ~5 deg)
            d = float(seg_distance(np.array([[ax, ay, ax, ay]]), np.array([[*b["start"], *b["end"]]]))[0, 0])
            if best is None or d < best[0]:
                best = (d, b)
        if best is None:
            continue
        spacing = best[0] - (a["width"] + best[1]["width"]) / 2
        if spacing <= 0 or spacing > 5 * a["width"]:
            continue
        b0, b1 = np.array(best[1]["start"]), np.array(best[1]["end"])
        foot = b0 + np.clip(np.dot([ax, ay] - b0, b1 - b0) / max(np.dot(b1 - b0, b1 - b0), 1e-12), 0, 1) * (b1 - b0)
        cx, cy = (ax + foot[0]) / 2, (ay + foot[1]) / 2  # centre of the pair, where the symmetric model sits
        xs = cross_section_of(board, a["layer"], cx, cy, ref_nets, a["width"], va, edge=spacing / 2 + a["width"])
        if xs is None:
            continue
        key = (a["layer"], round(a["width"], 4), round(spacing, 4), xs["gap"])
        if key not in seen:
            seen[key] = solve_line(xs, a["width"], s=spacing)["zdiff"]
    require(seen, f"{row['net']}/{other}: no coupled parallel segments found")
    for (layer, width, spacing, gap), z in seen.items():
        shown = "" if not gap else "/gap" + "|".join("-" if g is None else f"{g:g}" for g in gap)
        emit(results, f"{row['net']}+{other}:zdiff@{layer}/{width}/{spacing}mm{shown}", z, "ohm", "within", f"{target}±{tol}%",
             "odd-mode field solution of the coupled pair on the board stackup (equal widths assumed)")


def net_length(board, net):
    return sum(math.dist(t["start"], t["end"]) for t in board.tracks(net))


def check_reference(board, row, results):
    ref_nets = [n for n in (optional(row, "ref_net") or "GND").split(",") if n]
    own_pads = [p for p in board.data["pads"] if p["net"] == row["net"]]
    uncovered = 0.0
    step = 0.2
    for t in board.tracks(row["net"]):
        length = math.dist(t["start"], t["end"])
        n = max(2, int(length / step) + 1)
        px = np.linspace(t["start"][0], t["end"][0], n)
        py = np.linspace(t["start"][1], t["end"][1], n)
        i = board.copper.index(t["layer"])
        neighbours = [board.copper[j] for j in (i - 1, i + 1) if 0 <= j < len(board.copper)]
        ok = np.zeros(n, dtype=bool)
        for layer in neighbours:
            for net in ref_nets:
                ok |= board.covered(net, layer, px, py)
        for p in own_pads:  # trace inside its own pad is the land pattern (a launch cut-out under it is deliberate)
            if t["layer"] in p["layers"]:
                ok |= polys_contain(p["shapes"].get(t["layer"]) or [], px, py)
        uncovered += float((~ok).sum()) * length / n
    emit(results, f"{row['net']}:return_path", uncovered, "mm", "le", 0.2,
         f"trace length (outside its own pads) without an adjacent {ref_nets} plane (return current detours: ARCH, BOGATIN return-path rules)")


def lambda_eff_mm(board, net, f_hz, ref_nets):
    """Guided wavelength on the RF net itself: the shortest over its segments' field solutions."""
    er = []
    for t in board.tracks(net):
        u = np.subtract(t["end"], t["start"])
        if math.hypot(*u) > 1e-6:
            xs = cross_section_of(board, t["layer"], (t["start"][0] + t["end"][0]) / 2, (t["start"][1] + t["end"][1]) / 2,
                                  ref_nets, t["width"], u)
            require(xs, f"{net}: no reference plane under the RF trace; cannot size fences or stitching")
            er.append(solve_line(xs, t["width"])["er_eff"])
    require(er, f"{net}: RF net has no routed copper")
    return C0 / (f_hz * math.sqrt(max(er))) * 1e3


def check_rf(board, row, results):
    net, f_hz = row["net"], float(number(row["f_max_hz"], positive=True))
    ref_nets = [n for n in (optional(row, "ref_net") or "GND").split(",") if n]
    lam = lambda_eff_mm(board, net, f_hz, ref_nets)
    # a gap between fence vias is a slot resonating at lambda/2: lambda/10 keeps it >= 5 f_max (ARCH-065)
    pitch = float(number(optional(row, "fence_pitch_mm") or lam / 10, positive=True))
    band = float(number(optional(row, "fence_band_mm") or 1.5, positive=True))
    gnd = [v for v in board.data["vias"] if v["net"] in ref_nets]
    gnd += [dict(x=p["x"], y=p["y"]) for p in board.data["pads"] if p["net"] in ref_nets and len(p["layers"]) > 1]
    worst = 0.0
    own_pads = [p for p in board.data["pads"] if p["net"] == net]
    for t in board.tracks(net):
        p0, p1 = np.array(t["start"]), np.array(t["end"])
        length = float(np.linalg.norm(p1 - p0))
        if length < 1e-6:
            continue
        u = (p1 - p0) / length
        n = np.array([-u[1], u[0]])
        # only the exposed line counts: the stretch inside the net's own pads is the component, not the line
        s = np.linspace(0, length, max(2, int(length / 0.05) + 1))
        inside = np.zeros(s.shape, dtype=bool)
        for p in own_pads:
            if t["layer"] in p["layers"]:
                inside |= polys_contain(p["shapes"].get(t["layer"]) or [], p0[0] + s * u[0], p0[1] + s * u[1])
        if inside.all():
            continue
        a0, a1 = float(s[~inside][0]), float(s[~inside][-1])
        for sign in (1, -1):
            along = [float(np.dot(np.array([v["x"], v["y"]]) - p0, u)) for v in gnd
                     if t["width"] / 2 < sign * float(np.dot(np.array([v["x"], v["y"]]) - p0, n)) <= t["width"] / 2 + band]
            points = [a0] + sorted(min(max(a, a0), a1) for a in along if a0 - pitch / 2 <= a <= a1 + pitch / 2) + [a1]
            worst = max(worst, max(b - a for a, b in zip(points, points[1:])))
    emit(results, f"{net}:via_fence_gap", worst, "mm", "le", pitch,
         f"largest unfenced run along the RF trace, band {band} mm each side; lambda_eff = {lam:.3g} mm at {f_hz:g} Hz (ARCH-065: <= lambda/10)")
    vias = sum(1 for v in board.data["vias"] if v["net"] == net)
    if optional(row, "max_vias") is not None:
        emit(results, f"{net}:vias", vias, "count", "le", row["max_vias"], "layer changes on the RF path (each via adds a discontinuity)")
    segs = board.tracks(net)
    sharp = 0
    for a in segs:
        for b in segs:
            if a is b or a["layer"] != b["layer"]:
                continue
            if math.dist(a["end"], b["start"]) < 1e-3:
                va, vb = np.subtract(a["end"], a["start"]), np.subtract(b["end"], b["start"])
                la, lb = np.linalg.norm(va), np.linalg.norm(vb)
                if la > 1e-6 and lb > 1e-6 and math.degrees(math.acos(np.clip(np.dot(va, vb) / la / lb, -1, 1))) > 45.5:
                    sharp += 1
    emit(results, f"{net}:sharp_bends", sharp, "count", "le", 0, "direction changes above 45 degrees on the RF trace (miter or arc them)")
    source = optional(row, "source")
    if source:
        ref, _, pin = source.partition(".")
        anchor = next((p for p in board.data["pads"] if p["ref"] == ref and p["number"] == pin), None)
        require(anchor, f"{net}: RF source pad {source} not on the board")
        limit = float(number(optional(row, "match_max_mm") or lam / 20, positive=True))
        far = 0.0
        for p in board.data["pads"]:
            if p["net"] == net and p["ref"] != ref and p["ref"][:1] in {"C", "L", "R"}:
                far = max(far, math.hypot(p["x"] - anchor["x"], p["y"] - anchor["y"]))
        emit(results, f"{net}:matching_distance", far, "mm", "le", limit, f"farthest matching part from {source}")
    refs = [r for r in (optional(row, "keepout_refs") or "").split(",") if r]
    areas = [z for z in board.data["zones"] if z["rule_area"] and z["keepout"]["copper_pour"] and z["keepout"]["tracks"]]
    for ref in refs:
        fp = next((f for f in board.data["footprints"] if f["ref"] == ref), None)
        require(fp, f"{net}: keep-out footprint {ref} not on the board")
        x0, y0, x1, y1 = fp["bbox"]
        px, py = np.meshgrid(np.linspace(x0, x1, 9), np.linspace(y0, y1, 9))
        cover = any(polys_contain(z["outline"], px.ravel(), py.ravel()).any() for z in areas)
        emit(results, f"{net}:keepout@{ref}", 1.0 if cover else 0.0, "present", "ge", 1, "antenna/module needs a no-copper rule area (DRC then enforces it)")
    check_stitching(board, net, segs, ref_nets, gnd, lam, results)


def check_stitching(board, net, segs, ref_nets, gnd, lam, results):
    """Ground pour on the RF trace's own layer(s) within 5 mm of it: every point must lie within lambda/20 of a
    stitching via, so no unstitched copper tip reaches its lambda/4 resonance below 5 f_max (WILLIAMS-2038)."""
    step = min(0.25, lam / 40)
    pts = np.vstack([np.linspace(t["start"], t["end"], max(2, int(math.dist(t["start"], t["end"]) / step) + 1)) for t in segs])
    x0, y0 = pts.min(axis=0) - 5.0
    x1, y1 = pts.max(axis=0) + 5.0
    gx, gy = np.meshgrid(np.arange(x0, x1, step), np.arange(y0, y1, step))
    gx, gy = gx.ravel(), gy.ravel()
    near = np.zeros(gx.shape, dtype=bool)
    for start in range(0, len(pts), 256):
        chunk = pts[start:start + 256]
        near |= np.min(np.hypot(gx[:, None] - chunk[None, :, 0], gy[:, None] - chunk[None, :, 1]), axis=1) <= 5.0
    pour = np.zeros(gx.shape, dtype=bool)
    for layer in {t["layer"] for t in segs}:
        for ref in ref_nets:
            pour |= near & board.covered(ref, layer, gx, gy)
    if not pour.any():
        return
    g = np.column_stack([gx[pour], gy[pour]])
    if not gnd:
        span = float(np.hypot(*(g.max(axis=0) - g.min(axis=0))))  # finite stand-in: the whole pour is unstitched
        emit(results, f"{net}:stitching", span, "mm", "le", lam / 20, "same-layer ground pour near the RF trace has no stitching via at all")
        return
    vx = np.array([[v["x"], v["y"]] for v in gnd])
    nearest = np.concatenate([np.min(np.hypot(g[i:i + 4096, None, 0] - vx[None, :, 0], g[i:i + 4096, None, 1] - vx[None, :, 1]), axis=1)
                              for i in range(0, len(g), 4096)])
    k = int(np.argmax(nearest))
    emit(results, f"{net}:stitching", float(nearest[k]), "mm", "le", lam / 20,
         f"worst distance from same-layer ground pour (within 5 mm of the trace) to a stitching via, at ({g[k, 0]:.2f},{g[k, 1]:.2f}); "
         "lambda_eff/20 (WILLIAMS-2038)")


def plot_copper(board, out_dir):
    """One PNG per copper layer from KiCad's own geometry: refilled zones, tracks, pads, vias (audit figures)."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from matplotlib.patches import Circle, Polygon
    except ImportError:
        DETAILS.append("NOTE: matplotlib missing; copper plots skipped")
        return []
    out_dir.mkdir(parents=True, exist_ok=True)
    outline = [p for poly in board.data["outline"] for p in poly["outline"]]
    xs, ys = [p[0] for p in outline], [p[1] for p in outline]
    palette = [plt.cm.tab20(i) for i in range(20)]
    colours = {}

    def colour(net):
        return colours.setdefault(net, palette[len(colours) % len(palette)])
    written = []
    for layer in board.copper:
        fig, ax = plt.subplots(figsize=(8, 8 * (max(ys) - min(ys)) / max(max(xs) - min(xs), 1e-6) + 0.5), tight_layout=True)
        for (net, zlayer), polys in board.fills.items():
            if zlayer == layer:
                for poly in polys:
                    ax.add_patch(Polygon(poly["outline"], closed=True, facecolor=colour(net), alpha=0.25, linewidth=0))
                    for hole in poly["holes"]:
                        ax.add_patch(Polygon(hole, closed=True, facecolor="white", linewidth=0))
        for t in board.data["tracks"]:
            if t["layer"] == layer:
                ax.plot([t["start"][0], t["end"][0]], [t["start"][1], t["end"][1]], color=colour(t["net"]),
                        linewidth=t["width"] * 8 * 72 / (max(xs) - min(xs) + 2), solid_capstyle="round")  # true width in points
        for pad in board.data["pads"]:
            for poly in pad["shapes"].get(layer, []) if layer in pad["layers"] else []:
                ax.add_patch(Polygon(poly["outline"], closed=True, facecolor=colour(pad["net"]), edgecolor="k", linewidth=0.3))
        for v in board.data["vias"]:
            ax.add_patch(Circle((v["x"], v["y"]), v["diameter"] / 2, facecolor="0.3", edgecolor="k", linewidth=0.3))
        ax.plot(xs + xs[:1], ys + ys[:1], "k-", linewidth=0.8)
        ax.set_xlim(min(xs) - 1, max(xs) + 1)
        ax.set_ylim(max(ys) + 1, min(ys) - 1)
        ax.set_aspect("equal")
        ax.set_title(f"{layer} (KiCad geometry, zones refilled)")
        ax.set_xlabel("x (mm)")
        ax.set_ylabel("y (mm)")
        handles = [plt.Line2D([], [], color=c, linewidth=4, label=n or "(no net)") for n, c in sorted(colours.items())]
        ax.legend(handles=handles, fontsize=6, loc="upper right", ncol=2)
        path = out_dir / f"copper-{layer.replace('.', '_')}.png"
        fig.savefig(path, dpi=150)
        plt.close(fig)
        written.append(path)
    return written


def evaluate(pcb, design_dir):
    design = Path(design_dir).resolve()
    rows = table(design / "nets.tsv", ("net", "kind", "traces"))
    for row in rows:
        traces(row["traces"])
    board = Board(dump_board(pcb))
    names = set(board.data["nets"])

    def resolve(name):  # KiCad prefixes sheet-local nets with "/"
        return name if name in names else "/" + name if "/" + name in names else None
    missing = sorted(r["net"] for r in rows if resolve(r["net"]) is None)
    require(not missing, f"nets.tsv names nets that are not on the board: {missing}")
    for row in rows:
        row["net"] = resolve(row["net"])
        if optional(row, "pair"):
            require(resolve(row["pair"]), f"pair net not on the board: {row['pair']}")
            row["pair"] = resolve(row["pair"])
    voltages = {r["net"]: float(number(r["voltage_v"])) for r in rows if optional(r, "voltage_v") is not None}
    results = []
    if board.stack is None:
        DETAILS.append("NOTE: board has no physical stackup; copper assumed 35 um; impedance checks will fail until it is defined")
    pairs = set()
    for row in rows:
        if optional(row, "current_a") is not None:
            check_current(board, row, results)
        if optional(row, "voltage_v") is not None:
            check_voltage(board, row, voltages, results)
        if optional(row, "z_target") is not None:
            check_impedance(board, row, results)
        if optional(row, "pair") is not None and optional(row, "zdiff_target") is not None and frozenset((row["net"], row["pair"])) not in pairs:
            pairs.add(frozenset((row["net"], row["pair"])))
            check_pair(board, row, results)
        if optional(row, "max_length_mm") is not None:
            emit(results, f"{row['net']}:length", net_length(board, row["net"]), "mm", "le", row["max_length_mm"], "routed copper length")
        if row["kind"] in FAST:
            check_reference(board, row, results)
    groups = {}
    for row in rows:
        if optional(row, "match_group"):
            groups.setdefault(row["match_group"], []).append(row)
    for name, members in groups.items():
        lengths = [net_length(board, r["net"]) for r in members]
        tol = float(number(optional(members[0], "match_tol_mm") or 0.5, positive=True))
        emit(results, f"match:{name}", max(lengths) - min(lengths), "mm", "le", tol, f"lengths {dict(zip([r['net'] for r in members], [round(x, 3) for x in lengths]))}")
    if (design / "rf.tsv").is_file():
        for row in table(design / "rf.tsv", ("net", "f_max_hz", "traces")):
            traces(row["traces"])
            require(resolve(row["net"]), f"rf.tsv net not on the board: {row['net']}")
            row["net"] = resolve(row["net"])
            check_rf(board, row, results)
    require(results, "nets.tsv declared nothing measurable")
    for picture in plot_copper(board, design.parent / "analysis" / "layout"):
        OUTPUTS.add(picture.resolve())
    return f"LAYOUT: {sum(results)}/{len(results)}", all(results)
