#!/usr/bin/env python3
"""Signal integrity of routed nets: the board's own topology as field-solved transmission lines in ngspice.

`si <pcb> <design-dir>` reads design/si.tsv (one row per net). For each net the routed copper is turned
into a circuit: every track segment (split at T-junctions) is a lossless line whose Z0 and delay come
from the 2-D field solution of its real cross-section (anvil_fields), vias join layers and add their
unused-barrel stub capacitance (5 fF/mil, BOGATIN-286), pads join the copper they touch. The driver is
an ideal ramp (rise_ps, 0-100 %) behind r_drv_ohm (+ optional series termination); every receiver pad
gets c_rx_pf and optional parallel termination r_term_ohm to v_term. ngspice then gives, per receiver:
overshoot, ringback after the first crossing of 90 %, 50 %-to-50 % delay and 5 % settling time.
The model is linear, so the falling edge mirrors the rising one (undershoot below ground = overshoot).
Lossless lines are conservative for ringing and optimistic for edge degradation on long, fast channels.
"""
from __future__ import annotations

import math
import re
import tempfile
from pathlib import Path

import numpy as np

import anvil_layout as L
from anvil import DETAILS, OUTPUTS, execute, executable, number, require, table, traces

SI = ("net", "driver", "rise_ps", "r_drv_ohm", "v_swing", "c_rx_pf", "traces")
MIL = 0.0254


class Nodes:
    """Union-find over copper points."""

    def __init__(self):
        self.parent = {}

    def find(self, key):
        self.parent.setdefault(key, key)
        while self.parent[key] != key:
            self.parent[key] = self.parent[self.parent[key]]
            key = self.parent[key]
        return key

    def join(self, a, b):
        self.parent[self.find(a)] = self.find(b)


def key(layer, x, y):
    return (layer, round(x, 4), round(y, 4))


def topology(board, net):
    """Segments split at T-junctions, as (layer, start, end, width), plus the node union-find."""
    tracks = board.tracks(net)
    require(tracks, f"{net}: no routed copper")
    ends = {}
    for t in tracks:
        ends.setdefault(t["layer"], []).extend([t["start"], t["end"]])
    segments = []
    for t in tracks:
        a, b = np.array(t["start"], dtype=float), np.array(t["end"], dtype=float)
        d = b - a
        length2 = float(d @ d)
        if length2 < 1e-12:
            continue
        cuts = {0.0, 1.0}
        for p in ends[t["layer"]]:
            u = float((np.array(p) - a) @ d) / length2
            if 1e-6 < u < 1 - 1e-6 and np.linalg.norm(a + u * d - p) < 1e-3:
                cuts.add(u)
        us = sorted(cuts)
        segments += [(t["layer"], tuple(a + u0 * d), tuple(a + u1 * d), t["width"]) for u0, u1 in zip(us, us[1:])]
    nodes = Nodes()
    for layer, s, e, _ in segments:
        nodes.find(key(layer, *s))
        nodes.find(key(layer, *e))
    index = {name: i for i, name in enumerate(board.copper)}
    points = list(nodes.parent)
    for v in board.data["vias"]:
        if v["net"] != net:
            continue
        span = [name for name in board.copper if index[v["top"]] <= index[name] <= index[v["bottom"]]]
        anchor = ("via", round(v["x"], 4), round(v["y"], 4))
        for p in points:
            if p[0] in span and math.hypot(p[1] - v["x"], p[2] - v["y"]) <= v["diameter"] / 2:
                nodes.join(p, anchor)
    for pad in board.data["pads"]:
        if pad["net"] != net:
            continue
        anchor = ("pad", pad["ref"], pad["number"])
        nodes.find(anchor)
        for p in points:
            if p[0] in pad["layers"]:
                shapes = pad["shapes"].get(p[0]) or next(iter(pad["shapes"].values()), [])
                if L.polys_contain(shapes, np.array([p[1]]), np.array([p[2]]))[0]:
                    nodes.join(p, anchor)
    return segments, nodes


def stubs(board, net, nodes, segments):
    """Via node -> unused barrel length (mm): the part of the via beyond the deepest/shallowest used layer."""
    index = {name: i for i, name in enumerate(board.copper)}
    used = {}
    for layer, s, e, _ in segments:
        for p in (s, e):
            used.setdefault(nodes.find(key(layer, *p)), set()).add(layer)
    out = {}
    for v in board.data["vias"]:
        if v["net"] != net:
            continue
        root = nodes.find(("via", round(v["x"], 4), round(v["y"], 4)))
        layers = sorted(index[name] for name in used.get(root, set()))
        if not layers:
            continue
        top, bottom = index[v["top"]], index[v["bottom"]]
        out[root] = out.get(root, 0.0) + L.depth_between(board, top, layers[0]) + L.depth_between(board, layers[-1], bottom)
    return out


def netlist(board, row, segments, nodes, ref_nets):
    net = row["net"]
    names = {}

    def node(k):
        root = nodes.find(k)
        return names.setdefault(root, f"n{len(names) + 1}")

    driver = row["driver"].split(".", 1)
    require(len(driver) == 2, f"{net}: driver must be REF.PIN")
    v, tr = float(number(row["v_swing"], positive=True)), float(number(row["rise_ps"], positive=True)) * 1e-12
    r_src = float(number(row["r_drv_ohm"], minimum=0)) + float(number(L.optional(row, "r_series_ohm") or 0, minimum=0))
    solved, cache, total = [], {}, 0.0
    for layer, s, e, w in segments:
        ka, kb = key(layer, *s), key(layer, *e)
        if nodes.find(ka) == nodes.find(kb):
            continue
        x, y = (s[0] + e[0]) / 2, (s[1] + e[1]) / 2
        xs = L.cross_section_of(board, layer, x, y, ref_nets, w, (e[0] - s[0], e[1] - s[1]))
        require(xs, f"{net}: segment at ({x:.2f},{y:.2f}) on {layer} has no {ref_nets} reference plane; Z0 undefined")
        tag = (layer, round(w, 4), xs["gap"])
        if tag not in cache:
            cache[tag] = L.solve_line(xs, w)
        delay = cache[tag]["delay_ps_per_mm"] * math.dist(s, e) * 1e-12
        total += delay
        solved.append((ka, kb, cache[tag]["z0"], delay))
    # a line far shorter than the edge is a lumped capacitance: merge its ends and keep C = TD/Z0 as a shunt
    # (sub-picosecond T-lines stall the simulator's time step and change nothing the receiver can see)
    # a line far shorter than the edge is a lumped capacitance C = TD/Z0 at a junction; its time constant with the
    # lines meeting there (~TD/2) is below the simulation step, so it is both invisible to the receiver and a stiff
    # node that stalls ngspice's step control: merge the ends and record the capacitance left out
    short = min(5e-12, tr / 100)
    step = min(tr / 50, max(total, tr) / 200)
    z_node = min([z0 for _, _, z0, _ in solved] or [50.0]) / 2
    dropped = 0.0
    for ka, kb, z0, delay in solved:
        if delay < short:
            nodes.join(ka, kb)
            dropped += delay / z0
    if dropped:
        DETAILS.append(f"{net}: {dropped * 1e15:.3g} fF of line fragments shorter than {short * 1e12:.2g} ps merged (time constant below the {step * 1e12:.3g} ps step)")
    drv = node(("pad", *driver))
    receivers = [r.split(".", 1) for r in (L.optional(row, "receivers") or "").split(",") if r]
    if not receivers:
        receivers = [(p["ref"], p["number"]) for p in board.data["pads"] if p["net"] == net and (p["ref"], p["number"]) != tuple(driver)]
    require(receivers, f"{net}: no receiver pads")
    rx = {f"{r}.{n}": node(("pad", r, n)) for r, n in receivers}
    lines = [f"T{k} {node(ka)} 0 {node(kb)} 0 Z0={z0:.6g} TD={delay:.6g}"
             for k, (ka, kb, z0, delay) in enumerate(solved) if delay >= short and node(ka) != node(kb)]
    cards = [f"* anvil SI {net}", f"Vsrc src 0 PULSE(0 {v:g} 0 {tr:.6g} {tr:.6g} 1 2)", f"Rsrc src {drv} {max(r_src, 1e-3):g}"] + lines
    c_rx = float(number(row["c_rx_pf"], minimum=0)) * 1e-12
    r_term = L.optional(row, "r_term_ohm")
    v_term = float(number(L.optional(row, "v_term") or 0))
    if r_term:
        cards.append(f"Vterm vterm 0 DC {v_term:g}")
    for i, (name, n) in enumerate(rx.items()):
        if c_rx > 0:
            cards.append(f"Crx{i} {n} 0 {c_rx:.6g}")
        if r_term:
            cards.append(f"Rterm{i} {n} vterm {float(number(r_term, positive=True)):g}")
    for i, (root, stub) in enumerate(stubs(board, net, nodes, segments).items()):
        c_stub = 5e-15 * stub / MIL
        if c_stub * z_node >= step:  # resolvable at this edge rate (same rule as the merged fragments)
            cards.append(f"Cstub{i} {node(root)} 0 {c_stub:.6g}")
        elif stub > 1e-3:
            DETAILS.append(f"{net}: via stub {c_stub * 1e15:.3g} fF left out (time constant below the {step * 1e12:.3g} ps step)")
    stop = max(30 * total, 15 * tr) + tr
    cards += [f".tran {step:.6g} {stop:.6g} 0 {step:.6g}", ".end"]
    g_src = 1 / max(r_src, 1e-3)
    g_term = len(rx) / float(number(r_term, positive=True)) if r_term else 0.0
    final = (v * g_src + v_term * g_term) / (g_src + g_term)  # DC through lossless lines
    return "\n".join(cards) + "\n", drv, rx, dict(v=v, tr=tr, final=final, total=total, cache=cache)


def measure(t, v, tr, final):
    require(final > 0, "final receiver level must be positive (check v_swing / v_term)")
    above = np.nonzero(v >= 0.5 * final)[0]
    require(len(above), "receiver never reached 50 % of its final value; lengthen the run or check the net")
    t50 = float(t[above[0]])
    cross90 = np.nonzero(v >= 0.9 * final)[0]
    peak = float(v.max())
    after = v[cross90[0]:] if len(cross90) else v
    ringback = (final - float(after.min())) / final * 100 if len(cross90) else 100.0
    outside = np.nonzero(np.abs(v - final) > 0.05 * abs(final))[0]
    settle = float(t[outside[-1]]) - tr / 2 if len(outside) else 0.0
    return dict(overshoot=(peak - final) / final * 100, ringback=max(ringback, 0.0), delay=t50 - tr / 2, settle=max(settle, 0.0))


def plot(path, t, waves, final, net):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        DETAILS.append("NOTE: matplotlib missing; SI plot skipped")
        return None
    fig, ax = plt.subplots(figsize=(7, 4), tight_layout=True)
    for name, v in waves.items():
        ax.plot(t * 1e9, v, label=name)
    ax.axhline(final, color="k", linestyle=":", linewidth=1)
    ax.set_xlabel("Time (ns)")
    ax.set_ylabel("V")
    ax.set_title(f"SI {net} (rising edge; falling edge mirrors it)")
    ax.grid(True, alpha=0.4)
    ax.legend(fontsize=8)
    fig.savefig(path, dpi=130)
    plt.close(fig)
    return Path(path)


def evaluate(pcb, design_dir):
    from anvil_plots import parse_raw
    design = Path(design_dir).resolve()
    rows = table(design / "si.tsv", SI)
    board = L.Board(L.dump_board(pcb))
    out = design.parent / "analysis" / "si"
    out.mkdir(parents=True, exist_ok=True)
    results = []
    for row in rows:
        traces(row["traces"])
        net = row["net"] if row["net"] in board.data["nets"] else "/" + row["net"]
        require(net in board.data["nets"], f"net {row['net']} not on the board")
        row = dict(row, net=net)
        ref_nets = [n for n in (L.optional(row, "ref_net") or "GND").split(",") if n]
        segments, nodes = topology(board, net)
        cir, drv, rx, info = netlist(board, row, segments, nodes, ref_nets)
        safe = re.sub(r"[^A-Za-z0-9_.-]", "_", net.strip("/"))
        (out / f"si-{safe}.cir").write_text(cir, encoding="utf-8")
        with tempfile.TemporaryDirectory(prefix="anvil-si-") as temp:
            raw = Path(temp) / "out.raw"
            run = execute([executable("ngspice"), "-n", "-b", "-r", str(raw), str(out / f"si-{safe}.cir")], cwd=temp)
            require(run.returncode == 0 and raw.is_file(), f"{net}: ngspice failed")
            names, columns = parse_raw(raw.read_bytes())
        data = {n.lower(): np.asarray(c, dtype=float) for n, c in zip(names, columns)}
        t = data["time"]
        lines = ", ".join(f"{tag[0]} w{tag[1]}: {v['z0']:.1f} ohm {v['delay_ps_per_mm']:.2f} ps/mm" for tag, v in info["cache"].items())
        DETAILS.append(f"{net}: {len(segments)} segments, total flight {info['total'] * 1e12:.0f} ps; lines {lines}")
        waves = {f"driver {row['driver']}": data[f"v({drv})"]}
        for name, n in rx.items():
            waves[name] = data[f"v({n})"]
            m = measure(t, data[f"v({n})"], info["tr"], info["final"])
            label = f"{row['net']}@{name}"
            for column, metric, units in (("max_overshoot_pct", "overshoot", "%"), ("max_ringback_pct", "ringback", "%"),
                                          ("max_delay_ns", "delay", "ns"), ("max_settle_ns", "settle", "ns")):
                value = m[metric] * (1e9 if units == "ns" else 1)
                if L.optional(row, column) is not None:
                    L.emit(results, f"{label}:{metric}", value, units, "le", row[column], "ngspice transient on the field-solved routed topology")
                else:
                    DETAILS.append(f"{label}:{metric}: {value:.4g} {units} (no limit set)")
        picture = plot(out / f"si-{safe}.png", t, waves, info["final"], net)
        if picture:
            OUTPUTS.add(picture.resolve())
    require(results, "si.tsv set no limits (max_overshoot_pct / max_ringback_pct / max_delay_ns / max_settle_ns)")
    return f"SI: {sum(results)}/{len(results)}", all(results)
