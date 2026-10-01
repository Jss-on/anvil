#!/usr/bin/env python3
"""Power-distribution impedance from the board itself (numpy required).

`pdn <pcb> <design-dir>` reads design/pdn.tsv (one row per rail) and builds the impedance the load sees:
- every capacitor footprint with one pad on the rail and one on the reference net becomes a series
  R-L-C branch: C from the footprint value; body ESL/ESR by dielectric and package (ARCH-067,
  Archambeault Table 8-1) unless design/caps.tsv overrides them; mounting inductance computed from
  the copper: the connected pad-to-via track path costed with its field-solved inductance per mm
  (anvil_fields; 32 pH/mil per square bound where no plane lies under it), the via pair down to the
  power cavity (BOGATIN-2132) and cavity spreading to the load (BOGATIN-2135);
- plane-pair capacitance from the rail/reference fill overlap on adjacent layers (BOGATIN-2147),
  with dielectric loss from the stackup loss tangent;
- the regulator as R + L (from its datasheet), and optionally package L and on-die C.
The branches are combined exactly (non-interacting-capacitor model, BOGATIN-2130) and the worst
|Z| from f_min to f_max is checked against Z_target = V x ripple / I_step (BOGATIN-2110).
"""
from __future__ import annotations

import heapq
import math
import re
from pathlib import Path

import numpy as np

import anvil_layout as L
from anvil import DETAILS, OUTPUTS, number, require, table, traces

EPS0 = 8.8541878128e-12
MIL = 0.0254
PDN = ("rail", "ref_net", "load", "v_nom", "ripple_pct", "i_step_a", "f_max_hz", "vrm_r_mohm", "vrm_l_nh", "traces")
# ARCH-067 (Archambeault, PCB Design for Real-World EMI Control, Table 8-1 p.123): ESL nH, ESR ohm @100 MHz
BODY = {("NPO", "0603"): (0.6, 0.060), ("NPO", "0805"): (1.0, 0.070), ("NPO", "1206"): (1.0, 0.090),
        ("X7R", "0603"): (0.6, 0.090), ("X7R", "0805"): (0.9, 0.110), ("X7R", "1206"): (1.2, 0.120),
        ("Y5V", "0603"): (2.5, 0.080), ("Y5V", "0805"): (3.1, 0.090), ("Y5V", "1206"): (3.2, 0.100),
        ("X5R", "0603"): (0.4, 0.060), ("X5R", "0805"): (1.0, 0.080), ("X5R", "1206"): (1.1, 0.110)}
PREFIX = {"p": 1e-12, "n": 1e-9, "u": 1e-6, "µ": 1e-6, "m": 1e-3, "": 1.0}


def farads(text):
    m = re.search(r"(\d+(?:\.\d+)?)\s*([pnuµm]?)F?", text.replace(",", "."))
    require(m and float(m[1]) > 0, f"capacitor value not readable: {text!r}")
    rkm = re.fullmatch(r"(\d+)([pnuµ])(\d+).*", text.strip())
    return float(f"{rkm[1]}.{rkm[3]}") * PREFIX[rkm[2]] if rkm else float(m[1]) * PREFIX[m[2]]


def body_parasitics(fp, overrides):
    """(ESL H, ESR ohm, source) for one capacitor footprint."""
    for row in overrides:
        if re.fullmatch(row["match"], fp["ref"]) or re.search(row["match"], f"{fp['footprint']} {fp['value']}"):
            return float(number(row["esl_nh"], positive=True)) * 1e-9, float(number(row["esr_mohm"], positive=True)) * 1e-3, f"caps.tsv {row['match']}"
    text = f"{fp['footprint']} {fp['value']}".upper()
    if re.search(r"CP_|ELEC|POLARIZED", text):
        return 15e-9, 0.1, "electrolytic ESL 15 nH (BOGATIN-2145); ESR 0.1 ohm default: set design/caps.tsv from the datasheet"
    if "TANT" in text:
        return 5e-9, 0.1, "tantalum ESL 5 nH (BOGATIN-2146); ESR 0.1 ohm default: set design/caps.tsv from the datasheet"
    dielectric = next((d for d in ("X5R", "X7R", "Y5V") if d in text), "NPO" if re.search(r"NP0|NPO|C0G", text) else "X7R")
    size = re.search(r"(0201|0402|0603|0805|1206|1210|1812|2220)", fp["footprint"])
    package = size[1] if size else "0805"
    listed = {"0201": "0603", "0402": "0603", "1210": "1206", "1812": "1206", "2220": "1206"}.get(package, package)
    esl, esr = BODY[(dielectric, listed)]
    note = f"ARCH-067 {dielectric} {listed}" + ("" if listed == package else f" (nearest listed size for {package})")
    return esl * 1e-9, esr, note


def cavity(board, rail, refs, cell=0.25):
    """Adjacent-layer rail/reference fill overlap with the largest area: (upper, lower, h mm, er, tand, area mm^2)."""
    if not board.stack:
        return None
    pts = np.array([p for poly in board.data["outline"] for p in poly["outline"]])
    gx, gy = np.meshgrid(np.arange(pts[:, 0].min(), pts[:, 0].max(), cell) + cell / 2, np.arange(pts[:, 1].min(), pts[:, 1].max(), cell) + cell / 2)
    px, py = gx.ravel(), gy.ravel()
    best = None
    for i in range(len(board.copper) - 1):
        a, b = board.copper[i], board.copper[i + 1]
        for top, bottom in ((a, b), (b, a)):
            rail_hit = board.covered(rail, top, px, py)
            ref_hit = np.zeros(px.shape, dtype=bool)
            for ref in refs:
                ref_hit |= board.covered(ref, bottom, px, py)
            area = float((rail_hit & ref_hit).sum()) * cell * cell
            if area > 0 and (best is None or area > best[-1]):
                gap = board.stack["gaps"][i]
                h = sum(t for t, _, _ in gap)
                best = (a, b, h, sum(t * er for t, er, _ in gap) / h, sum(t * tan for t, _, tan in gap) / h, area)
    return best


def depth(board, layer, target):
    return L.depth_between(board, board.copper.index(layer), board.copper.index(target))


def fanout(board, pad, layer, reach=10.0):
    """Shortest connected track path from a pad to a via of its net: (tracks, via) or ([], None)."""
    net = pad["net"]
    shapes = pad["shapes"].get(layer) or next(iter(pad["shapes"].values()))
    vias = [v for v in board.data["vias"] if v["net"] == net and math.hypot(v["x"] - pad["x"], v["y"] - pad["y"]) <= reach]
    for v in vias:  # via in pad
        if L.polys_contain(shapes, np.array([v["x"]]), np.array([v["y"]]))[0]:
            return [], v
    tracks = [t for t in board.tracks(net) if t["layer"] == layer
              and max(math.dist(t["start"], (pad["x"], pad["y"])), math.dist(t["end"], (pad["x"], pad["y"]))) <= reach]
    node = lambda p: (round(p[0], 4), round(p[1], 4))  # noqa: E731
    edges = {}
    for t in tracks:
        edges.setdefault(node(t["start"]), []).append((node(t["end"]), t))
        edges.setdefault(node(t["end"]), []).append((node(t["start"]), t))
    queue = [(0.0, n, []) for n in edges if L.polys_contain(shapes, np.array([n[0]]), np.array([n[1]]))[0]]
    heapq.heapify(queue)
    seen = set()
    while queue:
        cost, n, path = heapq.heappop(queue)
        if n in seen:
            continue
        seen.add(n)
        hit = next((v for v in vias if math.hypot(v["x"] - n[0], v["y"] - n[1]) <= v["diameter"] / 2), None)
        if hit:
            return path, hit
        for m, t in edges.get(n, []):
            if m not in seen:
                heapq.heappush(queue, (cost + math.dist(t["start"], t["end"]), m, path + [t]))
    return [], None


def trace_inductance(board, tracks, planes):
    """Loop inductance (H) of surface tracks over their nearest plane, from the 2-D field solution."""
    total = 0.0
    for t in tracks:
        x, y = (t["start"][0] + t["end"][0]) / 2, (t["start"][1] + t["end"][1]) / 2
        xs = L.cross_section_of(board, t["layer"], x, y, planes, t["width"], (t["end"][0] - t["start"][0], t["end"][1] - t["start"][1]))
        if xs is None:  # no plane under it: the sheet-inductance bound (32 pH/mil per square) over the first dielectric
            gap = sum(tk for tk, _, _ in board.stack["gaps"][0 if t["layer"] == board.copper[0] else -1])
            total += 32e-12 * (gap / MIL) * math.dist(t["start"], t["end"]) / t["width"]
        else:
            total += L.solve_line(xs, t["width"])["l_nh_per_mm"] * 1e-9 * math.dist(t["start"], t["end"])
    return total


def mounting(board, fp, pads, rail, refs, cav, load_xy):
    """Mounted loop inductance (H) above the body ESL, and its parts, from the copper around one capacitor."""
    layer = pads[0]["layers"][0]
    first_gap = sum(t for t, _, _ in board.stack["gaps"][0 if layer == board.copper[0] else -1])
    paths = [fanout(board, pad, layer) for pad in pads]
    vias = [via for _, via in paths if via]
    l_trace = trace_inductance(board, [t for path, _ in paths for t in path], refs + [rail])
    if len(vias) == 2 and cav:
        s = math.hypot(vias[0]["x"] - vias[1]["x"], vias[0]["y"] - vias[1]["y"])
        d = min(v["diameter"] for v in vias)
        h_via = min(depth(board, layer, cav[0]), depth(board, layer, cav[1]))
        l_via = 10e-12 * (h_via / MIL) * math.log(max(2 * s / d, 1.0))
    else:
        l_via = 0.0
    rail_via = next((v for v in vias if v["net"] == rail), None)
    if cav and rail_via:
        b = math.dist((rail_via["x"], rail_via["y"]), load_xy)
        l_spread = 21e-12 * (cav[2] / MIL) * math.log(max(b / rail_via["diameter"], 1.0))
    else:  # no cavity: the rail copper itself, as squares over its reference (straight-line estimate)
        width = np.median([t["width"] for t in board.tracks(rail)] or [0.5])
        l_spread = 32e-12 * (first_gap / MIL) * math.dist((fp["x"], fp["y"]), load_xy) / width
    return l_trace + l_via + l_spread, dict(trace=l_trace, via=l_via, spread=l_spread, vias=len(vias))


def impedance(f, branches):
    w = 2j * math.pi * f
    y = np.zeros(f.shape, dtype=complex)
    for b in branches:
        z = b.get("r", 0.0) + w * b.get("l", 0.0)
        if b.get("c"):
            z = z + 1 / (w * b["c"] * (1 - 1j * b.get("tand", 0.0)))
        y += 1 / z
    return 1 / y


def plot(path, f, z, target, rail):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        DETAILS.append("NOTE: matplotlib missing; PDN plot skipped")
        return None
    fig, ax = plt.subplots(figsize=(7, 4), tight_layout=True)
    ax.loglog(f, np.abs(z), label="|Z| at the load")
    ax.axhline(target, color="r", linestyle="--", label=f"Z_target {target:.3g} ohm")
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("|Z| (ohm)")
    ax.set_title(f"PDN {rail}")
    ax.grid(True, which="both", alpha=0.4)
    ax.legend()
    fig.savefig(path, dpi=130)
    plt.close(fig)
    return Path(path)


def evaluate(pcb, design_dir):
    design = Path(design_dir).resolve()
    rows = table(design / "pdn.tsv", PDN)
    overrides = table(design / "caps.tsv", ("match", "esl_nh", "esr_mohm"), allow_empty=True) if (design / "caps.tsv").is_file() else []
    board = L.Board(L.dump_board(pcb))
    out = design.parent / "analysis" / "pdn"
    out.mkdir(parents=True, exist_ok=True)
    results = []
    for row in rows:
        traces(row["traces"])
        rail, refs = row["rail"], [n for n in row["ref_net"].split(",") if n]
        require(rail in board.data["nets"], f"rail {rail} not on the board")
        load_pads = [p for p in board.data["pads"] if p["ref"] == row["load"] and p["net"] == rail]
        require(load_pads, f"{rail}: load {row['load']} has no pad on the rail")
        load_xy = (float(np.mean([p["x"] for p in load_pads])), float(np.mean([p["y"] for p in load_pads])))
        v, ripple, step = (float(number(row[k], positive=True)) for k in ("v_nom", "ripple_pct", "i_step_a"))
        target = v * ripple / 100 / step
        f_max = float(number(row["f_max_hz"], positive=True))
        f_min = float(number(L.optional(row, "f_min_hz") or 1e3, positive=True))
        cav = cavity(board, rail, refs)
        branches = [dict(name="VRM", r=float(number(row["vrm_r_mohm"], positive=True)) * 1e-3, l=float(number(row["vrm_l_nh"], minimum=0)) * 1e-9)]
        if cav:
            c_plane = EPS0 * cav[3] * cav[5] * 1e-6 / (cav[2] * 1e-3)
            branches.append(dict(name="planes", c=c_plane, tand=cav[4], r=1e-6))
            DETAILS.append(f"{rail}: cavity {cav[0]}/{cav[1]} h={cav[2]:.3g} mm er={cav[3]:.3g} area={cav[5]:.0f} mm^2 -> {c_plane * 1e9:.3g} nF (BOGATIN-2147)")
        else:
            DETAILS.append(f"{rail}: no rail/reference plane pair found; rail copper treated as traces (spreading estimated from straight-line squares)")
        count = 0
        for fp in board.data["footprints"]:
            pads = [p for p in board.data["pads"] if p["ref"] == fp["ref"]]
            nets = {p["net"] for p in pads}
            if len(pads) != 2 or not fp["ref"].upper().startswith("C") or rail not in nets or not nets & set(refs):
                continue
            c = farads(fp["value"])
            esl, esr, source = body_parasitics(fp, overrides)
            l_mount, parts = mounting(board, fp, pads, rail, refs, cav, load_xy)
            branches.append(dict(name=fp["ref"], c=c, l=esl + l_mount, r=esr))
            count += 1
            DETAILS.append(f"  {fp['ref']} {c * 1e9:.4g} nF: ESL {esl * 1e9:.2g} nH + trace {parts['trace'] * 1e9:.2g} + via pair {parts['via'] * 1e9:.2g}"
                           f" + spreading {parts['spread'] * 1e9:.2g} nH ({parts['vias']} fanout vias), ESR {esr * 1e3:.3g} mohm [{source}]")
        if L.optional(row, "pkg_l_nh") is not None or L.optional(row, "die_c_nf") is not None:
            DETAILS.append(f"{rail}: package {row.get('pkg_l_nh', '-')} nH / on-die {row.get('die_c_nf', '-')} nF applied at the load")
        f = np.logspace(math.log10(f_min), math.log10(f_max), 600)
        z = impedance(f, branches)
        if L.optional(row, "pkg_l_nh") is not None:
            z = z + 2j * math.pi * f * float(number(row["pkg_l_nh"], minimum=0)) * 1e-9
        if L.optional(row, "die_c_nf") is not None:
            z = 1 / (1 / z + 2j * math.pi * f * float(number(row["die_c_nf"], positive=True)) * 1e-9)
        worst = int(np.argmax(np.abs(z)))
        picture = plot(out / f"pdn-{re.sub(r'[^A-Za-z0-9_.-]', '_', rail)}.png", f, z, target, rail)
        if picture:
            OUTPUTS.add(picture.resolve())
        L.emit(results, f"{rail}:z_pdn_max", float(abs(z[worst])), "ohm", "le", f"{target:.6g}",
               f"{count} capacitors; worst at {f[worst]:.4g} Hz over {f_min:g}-{f_max:g} Hz; Z_target = {v:g} V x {ripple:g}% / {step:g} A (BOGATIN-2110)")
    return f"PDN: {sum(results)}/{len(results)}", all(results)
