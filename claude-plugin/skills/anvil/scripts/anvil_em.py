#!/usr/bin/env python3
"""Full-wave RF verification with openEMS (FDTD) on the board's real copper; Touchstone in and out.

`em <pcb> <design-dir>` builds one FDTD model per design/em.tsv row from the KiCad board itself: the
physical stackup; the tracks, pads, via barrels and refilled zones of the named nets and their reference
nets (ref_net, default GND) inside the region around the signal path (the nets that carry a port) and the
listed parts, where a support net such as a bias feed is cut (other nets have no
terminations in the model and are left out: floating copper rings as a lossless resonator); lumped ports at the named pads, where the pin or
lead enters the pad (vertical to the first reference plane below, or across both coplanar gaps when the same-layer
ground is under half as far, e.g. an SMA pad over a cut-out) and the named parts as lumped R/L/C (capacitors
as series ESR-ESL-C: ARCH-067 or design/caps.tsv). openEMS runs once per port with a pulse confined to the analysed
band until the field energy is 50 dB down (end_db); a `settled` row fails when dropping the last 10 % of the run still
moves a checked S-parameter by more than 0.01. The S-matrix is written to
<name>.sNp (Touchstone) and <name>.png, the exact model to <name>.xml, and every limit in the row's `checks` becomes a margin row (outputs under analysis/em/).
`sparams <design-dir>` applies the same limits to the Touchstone files named in design/sparams.tsv:
the VNA measurement of the built board, which is what finally proves an RF path.

Model fidelity (stated in every transcript): copper is perfect conductor with its real thickness
(conductor loss is not modelled; dielectric loss is, from the stackup loss tangent, exact at f_stop
and over-estimated below it); solder mask and component bodies are omitted; copper away from the
named nets is staircased at the local mesh size; axis-aligned RF traces and their pour gaps get
thirds-rule mesh lines (last metal line 1/3 cell inside the edge), diagonal ones are staircased.
Validated on a 50-ohm microstrip: Zin at 1 GHz within 1.1 % of the 2-D field solution, eps_eff from
a two-length S21 phase difference within 1.6 % of it (mean 1.1 %) over 1-6 GHz, line loss within 1.5 % of
the analytic dielectric loss, |S12 - S21| < 3e-5 (largest at the band edges, where the band-limited pulse
is 20 dB down). Antenna mode, probe-fed FR-4 patch:
resonance within 3.2 % of the Balanis transmission-line design and mesh-converged (2x z-cells moves
it 0.15 %); input resistance follows the cos^2(pi y0/L) feed law within 1 % (tests/test_anvil_analysis.py). numpy required; openEMS from OPENEMS, PATH or
%LOCALAPPDATA%/anvil/tools/openEMS/openEMS.
"""
from __future__ import annotations

import math
import os
import re
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

import numpy as np

import anvil_fields as F
import anvil_layout as L
import anvil_pdn as P
from anvil import DETAILS, OUTPUTS, number, read, require, table, traces

C0, EPS0 = F.C0, F.EPS0
EM = ("name", "nets", "ports", "f_start_hz", "f_stop_hz", "checks", "traces")
FREQ = r"\d+(?:\.\d+)?(?:[eE]\+?\d+)?"
CHECK = re.compile(rf"S(\d)(\d)(<=|>=)(-?\d+(?:\.\d+)?)(?:dB)?@({FREQ}):({FREQ})")
PREFIX = {"p": 1e-12, "n": 1e-9, "u": 1e-6, "µ": 1e-6, "m": 1e-3, "": 1.0, "k": 1e3, "M": 1e6, "G": 1e9}


def openems():
    local = Path(os.environ.get("LOCALAPPDATA", str(Path.home()))) / "anvil/tools/openEMS/openEMS/openEMS.exe"
    for candidate in (os.environ.get("OPENEMS"), shutil.which("openEMS"), str(local)):
        if candidate and Path(candidate).is_file():
            return candidate
    raise ValueError("openEMS not found: set OPENEMS to the openEMS executable")


def value_of(text):
    """Component value: 2.2n, 4n7, 4R7, 10k, 1pF, 0 -> float (farad/henry/ohm)."""
    t = text.strip().replace("Ω", "").replace("ohm", "")
    t = re.sub(r"[FH]$", "", t)
    m = re.fullmatch(r"(\d+)([pnuµmkMGR])(\d+)", t)  # RKM code: 4n7, 4R7
    if m:
        t = f"{m[1]}.{m[3]}{'' if m[2] == 'R' else m[2]}"
    m = re.fullmatch(r"(\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)([pnuµmkMG]?)", t)
    require(m, f"cannot read component value: {text!r}")
    return float(m[1]) * PREFIX[m[2]]


# --- Touchstone ------------------------------------------------------------------------------------------------
def read_touchstone(path):
    """Touchstone v1/v2 S-parameters -> (f Hz, S[f, i, j] complex, z_ref ohm)."""
    path = Path(path)
    ports = re.search(r"\.s(\d+)p$", path.name.lower())
    require(ports, f"{path}: Touchstone files are named *.sNp")
    n = int(ports[1])
    scale, fmt, z0, order, numbers = 1e9, "MA", 50.0, "21_12", []
    for raw in read(path).splitlines():
        line = raw.split("!", 1)[0].strip()
        if not line:
            continue
        if line.startswith("#"):
            tokens = line[1:].upper().split()
            for i, tok in enumerate(tokens):
                if tok in {"HZ", "KHZ", "MHZ", "GHZ"}:
                    scale = {"HZ": 1.0, "KHZ": 1e3, "MHZ": 1e6, "GHZ": 1e9}[tok]
                elif tok in {"MA", "DB", "RI"}:
                    fmt = tok
                elif tok in {"Y", "Z", "H", "G"}:
                    raise ValueError(f"{path}: only S-parameter Touchstone files are supported")
                elif tok == "R":
                    z0 = float(tokens[i + 1])
            continue
        if line.startswith("["):
            if line.lower().startswith("[two-port data order]"):
                order = line.split("]", 1)[1].strip()
            continue
        numbers += [float(x) for x in line.split()]
    per = 1 + 2 * n * n
    require(numbers and len(numbers) % per == 0, f"{path}: data does not fit {n}-port records")
    rows = np.array(numbers).reshape(-1, per)
    a, b = rows[:, 1::2], rows[:, 2::2]
    s = {"RI": a + 1j * b, "MA": a * np.exp(1j * np.radians(b)), "DB": 10 ** (a / 20) * np.exp(1j * np.radians(b))}[fmt]
    s = s.reshape(-1, n, n)
    if n == 2 and order == "21_12":  # v1 (and v2 default) two-port order is S11 S21 S12 S22
        s = s.transpose(0, 2, 1)
    f = rows[:, 0] * scale
    require(np.all(np.diff(f) > 0), f"{path}: frequencies must increase")
    return f, s, z0


def write_touchstone(path, f, s, z0=50.0, comment=""):
    n = s.shape[1]
    lines = [f"! {line}" for line in comment.splitlines()] + [f"# Hz S RI R {z0:g}"]
    for k, fk in enumerate(f):
        m = s[k].T if n == 2 else s[k]  # two-port files list S11 S21 S12 S22
        rows = [m.reshape(-1)] if n <= 2 else list(m)
        for r, row in enumerate(rows):
            pairs = " ".join(f"{v.real:.9e} {v.imag:.9e}" for v in row)
            lines.append((f"{fk:.9e} " if r == 0 else "  ") + pairs)
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")
    return Path(path)


def checks_of(text):
    parsed = []
    for item in [c.strip() for c in text.split(";") if c.strip()]:
        m = CHECK.fullmatch(item.replace(" ", ""))
        require(m, f"bad S-parameter check {item!r}; write e.g. S11<=-10@2.4e9:2.5e9 (dB, band in Hz)")
        parsed.append((int(m[1]), int(m[2]), "le" if m[3] == "<=" else "ge", float(m[4]), float(m[5]), float(m[6])))
    require(parsed, "no S-parameter checks given")
    return parsed


def judge(label, f, s, checks, results, source):
    for i, j, op, limit, f1, f2 in checks:
        require(i <= s.shape[1] and j <= s.shape[1], f"{label}: S{i}{j} not in a {s.shape[1]}-port result")
        band = (f >= f1) & (f <= f2)
        require(f1 < f2 and band.sum() >= 3 and f[0] <= f1 and f2 <= f[-1], f"{label}: band {f1:g}-{f2:g} Hz not covered by the data")
        db = 20 * np.log10(np.maximum(np.abs(s[band, i - 1, j - 1]), 1e-12))
        worst = float(db.max() if op == "le" else db.min())
        at = float(f[band][int(db.argmax() if op == "le" else db.argmin())])
        L.emit(results, f"{label}:S{i}{j}@{f1:g}-{f2:g}Hz", worst, "dB", op, limit, f"worst at {at:.6g} Hz ({source})")


def plot(path, f, s, checks, title):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        DETAILS.append("NOTE: matplotlib missing; S-parameter plot skipped")
        return None
    fig, ax = plt.subplots(figsize=(7, 4), tight_layout=True)
    for i in range(s.shape[1]):
        for j in range(s.shape[1]):
            if i == j or j == 0:
                ax.plot(f / 1e9, 20 * np.log10(np.maximum(np.abs(s[:, i, j]), 1e-12)), label=f"S{i + 1}{j + 1}")
    for _, _, _, limit, f1, f2 in checks:
        ax.plot([f1 / 1e9, f2 / 1e9], [limit, limit], "k--", linewidth=1)
    ax.set_xlabel("Frequency (GHz)")
    ax.set_ylabel("|S| (dB)")
    ax.set_title(title)
    ax.grid(True)
    ax.legend()
    fig.savefig(path, dpi=130)
    plt.close(fig)
    return Path(path)


# --- geometry -> model ----------------------------------------------------------------------------------------
def stack_z(board, collapse=False):
    """Copper layer -> (z_bottom, thickness) and dielectric slabs (z0, z1, er, tand); board bottom at z = 0.
    collapse: copper as zero-thickness planes between the dielectrics (conducting-sheet models)."""
    require(board.stack, "board has no physical stackup: define the fabricator's stackup in Board Setup")
    copper, gaps = board.stack["copper"], board.stack["gaps"]
    thick = [0.0 if collapse else c["t"] for c in copper]
    z = top = sum(thick) + sum(t for gap in gaps for t, _, _ in gap)
    layers, slabs = {}, []
    for i, c in enumerate(copper):
        layers[c["name"]] = (z - thick[i], thick[i])
        if 0 < i < len(copper) - 1 and thick[i]:  # an inner copper layer sits in the resin of the slab above it
            slabs.append((z - thick[i], z, gaps[i - 1][-1][1], gaps[i - 1][-1][2]))
        z -= thick[i]
        for t, er, tand in gaps[i] if i < len(gaps) else []:
            slabs.append((z - t, z, er, tand))
            z -= t
    return layers, slabs, top


def pad_named(board, name):
    ref, _, pin = name.partition(".")
    pad = next((p for p in board.data["pads"] if p["ref"] == ref and p["number"] == pin), None)
    require(pad, f"pad {name} not on the board")
    return pad


def pad_box(pad, layer=None):
    shapes = pad["shapes"].get(layer) or next(iter(pad["shapes"].values()))
    pts = np.array([pt for poly in shapes for pt in poly["outline"]])
    return (*pts.min(axis=0), *pts.max(axis=0))


def all_tracks(board):
    return [t for net in sorted({t["net"] for t in board.data["tracks"] + board.data["arcs"]}) for t in board.tracks(net)]


def raster(board, layer, xc, yc, tracks, nets=None, refs=(), drop=None):
    """Copper of one layer sampled at mesh cell centres -> bool grid [ix, iy]; with `nets`, only those nets'
    copper and the pads of the parts in `refs`; `drop(item)` excludes pads and vias."""
    def kept(item):
        return (nets is None or item["net"] in nets or item.get("ref") in refs) and not (drop and drop(item))

    gx, gy = np.meshgrid(xc, yc, indexing="ij")
    px, py = gx.ravel(), gy.ravel()
    hit = np.zeros(px.shape, dtype=bool)
    lo, hi = (xc[0], yc[0]), (xc[-1], yc[-1])
    for t in tracks:
        if t["layer"] != layer or not kept(t):
            continue
        (x1, y1), (x2, y2), r = t["start"], t["end"], t["width"] / 2
        if max(x1, x2) + r < lo[0] or min(x1, x2) - r > hi[0] or max(y1, y2) + r < lo[1] or min(y1, y2) - r > hi[1]:
            continue
        dx, dy = x2 - x1, y2 - y1
        u = np.clip(((px - x1) * dx + (py - y1) * dy) / max(dx * dx + dy * dy, 1e-12), 0, 1)
        hit |= np.hypot(px - (x1 + u * dx), py - (y1 + u * dy)) <= r
    index = {name: i for i, name in enumerate(board.copper)}
    for v in board.data["vias"]:
        if kept(v) and index.get(v["top"], 0) <= index[layer] <= index.get(v["bottom"], len(board.copper)):
            hit |= np.hypot(px - v["x"], py - v["y"]) <= v["diameter"] / 2
    for pad in board.data["pads"]:
        if layer in pad["layers"] and kept(pad):
            hit |= L.polys_contain(pad["shapes"].get(layer) or next(iter(pad["shapes"].values()), []), px, py)
    for (net, zlayer), polys in board.fills.items():
        if zlayer == layer and kept(dict(net=net)):
            hit |= L.polys_contain(polys, px, py)
    return hit.reshape(gx.shape)


def clip_segment(t, box):
    """A track segment cut to the box (x0, y0, x1, y1) (Liang-Barsky), or None when it lies outside."""
    (x1, y1), (x2, y2) = t["start"], t["end"]
    dx, dy, lo, hi = x2 - x1, y2 - y1, 0.0, 1.0
    for p, q in ((-dx, x1 - box[0]), (dx, box[2] - x1), (-dy, y1 - box[1]), (dy, box[3] - y1)):
        if p == 0:
            if q < 0:
                return None
        elif p < 0:
            lo = max(lo, q / p)
        else:
            hi = min(hi, q / p)
    return dict(t, start=(x1 + lo * dx, y1 + lo * dy), end=(x1 + hi * dx, y1 + hi * dy)) if lo < hi else None


def rectangles(mask):
    """Merge a bool grid [ix, iy] into rectangles (i0, i1, j0, j1), inclusive cell ranges."""
    rects, open_runs = [], {}
    for j in range(mask.shape[1]):
        col, runs, i = mask[:, j], [], 0
        while i < len(col):
            if col[i]:
                k = i
                while k + 1 < len(col) and col[k + 1]:
                    k += 1
                runs.append((i, k))
                i = k + 1
            else:
                i += 1
        still = {run: open_runs.pop(run, j) for run in runs}
        rects += [(i0, i1, j0, j - 1) for (i0, i1), j0 in open_runs.items()]
        open_runs = still
    return rects + [(i0, i1, j0, mask.shape[1] - 1) for (i0, i1), j0 in open_runs.items()]


def fill(a, b, fine, coarse, ratio):
    """Cells between two keys: fine at both ends, growing by `ratio` to `coarse`, the whole graded sequence
    scaled to fit exactly (no sliver cell anywhere: the smallest cell sets the FDTD time step)."""
    length = b - a
    if length <= 1.5 * fine:
        return [a, b]
    sizes, h, total = [], fine, 0.0
    left, right = [], []
    while total < length:
        left.append(h)
        total += h
        if total >= length:
            break
        right.append(h)
        total += h
        h = min(h * ratio, coarse)
    options = [left + right[::-1]]
    if len(options[0]) > 2:
        options.append(options[0][:-1] if len(left) > len(right) else left + right[:-1][::-1])
    sizes = min(options, key=lambda s: abs(math.log(length / sum(s))))
    edges = a + np.cumsum([0.0] + sizes) * (length / sum(sizes))
    edges[-1] = b
    return list(edges)


def lines(keys, lo, hi, fine, coarse, ratio=1.3):
    """Graded FDTD mesh: fine at every key (keys closer than fine/2 merged: the smallest cell sets the
    time step), growing by `ratio` to `coarse`, then growing outward to the domain bounds."""
    kept = []
    for k in sorted(k for k in keys if lo < k < hi):
        if not kept or k - kept[-1] > fine / 2:
            kept.append(k)
    core = [kept[0]]
    for a, b in zip(kept, kept[1:]):
        core += fill(a, b, fine, coarse, ratio)[1:]

    def grow(start, end, step):
        out, h, pos, sign = [], step, start, 1.0 if end > start else -1.0
        while (end - pos) * sign > 1e-9:
            h = min(h * ratio, coarse)
            pos = end if (end - pos) * sign < 1.5 * h else pos + sign * h  # no sliver before the bound
            out.append(pos)
        return out

    left = grow(core[0], lo, core[1] - core[0] if len(core) > 1 else fine)
    right = grow(core[-1], hi, core[-1] - core[-2] if len(core) > 1 else fine)
    grid = left[::-1] + core + right
    for _ in range(10000):  # split any cell over 1.5x a neighbour: abrupt steps reflect numerically
        d = np.diff(grid)
        cuts = set()
        for i in range(len(d)):
            if i > 0 and d[i] > 1.5 * d[i - 1] and d[i] - 1.3 * d[i - 1] > 0.5 * d[i - 1]:
                cuts.add(grid[i] + 1.3 * d[i - 1])
            elif i + 1 < len(d) and d[i] > 1.5 * d[i + 1] and d[i] - 1.3 * d[i + 1] > 0.5 * d[i + 1]:
                cuts.add(grid[i + 1] - 1.3 * d[i + 1])
        if not cuts:
            break
        grid = sorted(set(grid) | cuts)
    return np.array(grid)


def snap(grid, value):
    return float(grid[int(np.argmin(np.abs(grid - value)))])


class Model:
    """CSXCAD/openEMS XML for one simulation (units: mm)."""

    def __init__(self):
        self.props = []

    def add(self, kind, attrs, boxes, prop=None):
        self.props.append((kind, attrs, prop, boxes))

    def write(self, path, grid, f0, fc, boundary, excite_port, end_criteria, pulses=40):
        cells = [np.diff(g).min() * 1e-3 for g in grid]
        dt = 1 / (C0 * math.sqrt(sum(1 / c ** 2 for c in cells)))
        steps = int(pulses * 9 / (math.pi * fc) / dt)  # budget in excitation lengths (openEMS pulse = 9/(pi fc))
        root = ET.Element("openEMS")
        fdtd = ET.SubElement(root, "FDTD", NumberOfTimesteps=str(steps), endCriteria=f"{end_criteria:g}", f_max=f"{f0 + fc:.9g}")
        ET.SubElement(fdtd, "Excitation", Type="0", f0=f"{f0:.9g}", fc=f"{fc:.9g}")
        ET.SubElement(fdtd, "BoundaryCond", **dict(zip(("xmin", "xmax", "ymin", "ymax", "zmin", "zmax"), boundary)))
        cs = ET.SubElement(root, "ContinuousStructure", CoordSystem="0")
        props = ET.SubElement(cs, "Properties")
        for kind, attrs, prop, boxes in self.props:
            if kind == "Excitation" and not re.fullmatch(rf"port_excite_{excite_port}[ab]?", attrs["Name"]):
                continue
            node = ET.SubElement(props, kind, **{k: str(v) for k, v in attrs.items()})
            if prop:
                ET.SubElement(node, "Property", **{k: str(v) for k, v in prop.items()})
            prims = ET.SubElement(node, "Primitives")
            for prio, a, b in boxes:
                box = ET.SubElement(prims, "Box", Priority=str(prio))
                ET.SubElement(box, "P1", X=f"{a[0]:.9g}", Y=f"{a[1]:.9g}", Z=f"{a[2]:.9g}")
                ET.SubElement(box, "P2", X=f"{b[0]:.9g}", Y=f"{b[1]:.9g}", Z=f"{b[2]:.9g}")
        rect = ET.SubElement(cs, "RectilinearGrid", DeltaUnit="0.001", CoordSystem="0")
        for tag, values in zip(("XLines", "YLines", "ZLines"), grid):
            ET.SubElement(rect, tag).text = ",".join(f"{v:.9g}" for v in values)
        ET.ElementTree(root).write(path, encoding="UTF-8", xml_declaration=True)


def port_site(board, pad, rf, ref_nets, layers, label):
    """Where and how a lumped port drives its pad. It stands where the connector pin or device lead enters (the side
    away from the trace that leaves the pad; a port at the pad centre would leave half the pad as an open stub),
    across the pad's full width. It drives the pad against the first reference plane below, or across both coplanar
    gaps when the same-layer ground is under half as far as that plane (a launch over a cut-out: a 1.5 mm tall
    vertical port would add its own landing inductance). -> dict(layer, plane, x, y, along_x, width, inward, gaps)"""
    layer = pad["layers"][0]
    order = board.copper.index(layer)
    step = 1 if order < len(board.copper) // 2 or order == 0 else -1
    x0, y0, x1, y1 = pad_box(pad, layer)
    centre = (pad["x"], pad["y"])
    touching = [t for t in rf if t["layer"] == layer and min(math.dist(t["start"], centre), math.dist(t["end"], centre)) < 1.0]
    if touching:
        far = max((touching[0]["start"], touching[0]["end"]), key=lambda q: math.dist(q, centre))
        along_x = abs(far[0] - centre[0]) >= abs(far[1] - centre[1])
        axis = 0 if along_x else 1
        inward = 1 if far[axis] > centre[axis] else -1  # from the port into the line
        entry = ((x0, y0) if inward > 0 else (x1, y1))[axis]
        spots = [(c, centre[1]) if along_x else (centre[0], c) for c in np.linspace(entry, centre[axis], 26)]
        width = (y1 - y0) if along_x else (x1 - x0)
    else:  # a probe feed (no trace): vertical, at the pad centre
        along_x, inward, spots, width = True, 0, [centre], min(x1 - x0, y1 - y0)
    for sx, sy in spots:
        plane = next((board.copper[k] for k in range(order + step, len(board.copper) if step > 0 else -1, step)
                      if any(board.covered(net, board.copper[k], np.array([sx]), np.array([sy]))[0] for net in ref_nets)), None)
        height = abs(layers[plane][0] - layers[layer][0]) if plane else math.inf
        # gaps on the -/+ side of the transverse axis (y for a line along x, x for a line along y)
        gaps = L.side_gaps(board, layer, sx, sy, (1.0, 0.0) if along_x else (0.0, -1.0), ref_nets, width / 2, 2.0) if inward else None
        if gaps and None not in gaps and max(gaps) <= height / 2 and layers[layer][1] > 0:
            return dict(layer=layer, plane=None, x=sx, y=sy, along_x=along_x, width=width, inward=inward, gaps=gaps)
        if plane:
            return dict(layer=layer, plane=plane, x=sx, y=sy, along_x=along_x, width=width, inward=inward, gaps=None)
    require(False, f"{label}: no {ref_nets} plane or coplanar ground at the port pad")


def coplanar_port(model, n, site, copper, grid, zref):
    """Lumped port across both coplanar gaps where the pin enters the pad: a 2 x zref resistor and a source in each
    gap (in parallel: zref); the voltage across one gap, the pad current one mesh line into the line."""
    z0, t = copper
    along_x, w, (g_lo, g_hi), inward = site["along_x"], site["width"], site["gaps"], site["inward"]
    ga, gt = grid if along_x else grid[::-1]  # mesh lines along the line / across it
    pa, ct = snap(ga, site["x"] if along_x else site["y"]), snap(gt, site["y"] if along_x else site["x"])
    across = 1 if along_x else 0  # the axis the gap fields point along

    def point(a, c, z):  # (along the line, across it, z) -> (x, y, z)
        return (a, c, z) if along_x else (c, a, z)

    for tag, sign, g in (("a", -1, g_lo), ("b", 1, g_hi)):
        lo, hi = sorted((ct + sign * w / 2, ct + sign * (w / 2 + g)))
        box = [(50, point(pa, lo, z0), point(pa, hi, z0 + t))]
        model.add("LumpedElement", dict(Name=f"port_resist_{n}{tag}", Direction=str(across), Caps="1", R=f"{2 * zref:g}"), box)
        excite = ["0", "0", "0"]
        excite[across] = str(sign)  # the field points from the pad out to the ground: the pad is driven positive
        model.add("Excitation", dict(Name=f"port_excite_{n}{tag}", Type="0", Excite=",".join(excite)), box)
    zm = z0 + t / 2
    model.add("ProbeBox", dict(Name=f"port_ut{n}", Type="0", Weight="-1"), [(50, point(pa, ct + w / 2 + g_hi, zm), point(pa, ct + w / 2, zm))])
    a_in = float(ga[int(np.argmin(np.abs(ga - pa))) + inward])
    model.add("ProbeBox", dict(Name=f"port_it{n}", Type="1", Weight=str(inward), NormDir=str(1 - across)),
              [(50, point(a_in, ct - w / 2 - g_lo / 2, z0 - 0.1), point(a_in, ct + w / 2 + g_hi / 2, z0 + t + 0.1))])


def build(board, row, caps=()):
    """Model, mesh and port bookkeeping for one em.tsv row (caps: design/caps.tsv capacitor ESL/ESR overrides)."""
    known = set(board.data["nets"])

    def resolved(text):  # sheet-local nets carry KiCad's "/" prefix on the board
        return [n if n in known or "/" + n not in known else "/" + n for n in text.split(",") if n]

    nets, ref_nets = resolved(row["nets"]), resolved(L.optional(row, "ref_net") or "GND")
    f1, f2 = float(number(row["f_start_hz"], positive=True)), float(number(row["f_stop_hz"], positive=True))
    require(f2 > f1, f"{row['name']}: f_stop_hz must exceed f_start_hz")
    antenna = (L.optional(row, "kind") or "line") == "antenna"
    sheet = (L.optional(row, "copper") or "thick") == "sheet"
    layers, slabs, top = stack_z(board, collapse=sheet)
    er_max = max(er for _, _, er, _ in slabs)
    port_names = [p for p in row["ports"].split(",") if p]
    require(port_names, f"{row['name']}: name at least one port pad (REF.PIN)")
    ports = [pad_named(board, p) for p in port_names]
    parts = []
    for item in [x for x in (L.optional(row, "parts") or "").split(";") if x]:
        ref, _, value = item.partition("=")
        pads = [p for p in board.data["pads"] if p["ref"] == ref.strip()]
        require(len(pads) == 2, f"{row['name']}: part {ref} must have exactly two pads")
        parts.append((ref.strip(), value_of(value), pads))
    rf = [t for net in nets for t in board.tracks(net)]
    pours = [poly for (net, _), polys in board.fills.items() if net in nets for poly in polys]  # patches, pour antennas
    require(rf or pours, f"{row['name']}: nets {nets} have no routed or poured copper")
    # the region spans the signal path (nets that carry a port) and the listed parts; a support net such as a bias
    # feed is modelled until it leaves the region, where the absorbing boundary terminates it
    port_nets = {pad["net"] for pad in ports}
    pts = [p for t in rf if t["net"] in port_nets for p in (t["start"], t["end"])] + [p for poly in pours for p in poly["outline"]]
    for pad in ports + [p for _, _, pads in parts for p in pads]:
        x0, y0, x1, y1 = pad_box(pad)
        pts += [(x0, y0), (x1, y1)]
    pts = np.array(pts)
    margin = float(number(L.optional(row, "margin_mm") or 3.0, positive=True))
    region = (*(pts.min(axis=0) - margin), *(pts.max(axis=0) + margin))
    sites = [port_site(board, pad, rf, ref_nets, layers, f"{row['name']} port {name}") for pad, name in zip(ports, port_names)]

    # mesh: thirds-rule lines on axis-aligned RF trace edges and their pour gaps; lines on pads and ports. The fine
    # cell comes from the nets that carry a port (the signal path), not from a narrow feed behind a choke
    kx, ky, feature, thirds = [], [], [], []
    for t in rf:
        (x1, y1), (x2, y2), w = t["start"], t["end"], t["width"]
        signal = t["net"] in port_nets
        if signal:
            feature.append(w / 4)
        along_x = abs(y2 - y1) < 1e-6 and abs(x2 - x1) > 1e-6
        along_y = abs(x2 - x1) < 1e-6 and abs(y2 - y1) > 1e-6
        if not (along_x or along_y):
            continue
        c = y1 if along_x else x1
        edges = [(c - w / 2, 1), (c + w / 2, -1)]  # (edge, side the metal lies on)
        mid = np.array([(x1 + x2) / 2, (y1 + y2) / 2])
        u = np.array([x2 - x1, y2 - y1]) / math.dist((x1, y1), (x2, y2))
        normal = np.array([-u[1], u[0]])  # side_gaps reports the -normal side first
        gaps = L.side_gaps(board, t["layer"], *mid, u, ref_nets, w / 2, 2.0)
        for side, g in zip((-1, 1), gaps or (None, None)):
            if g:
                edge = mid + side * normal * (w / 2 + g)
                outward = float(np.sign((side * normal)[1] if along_x else (side * normal)[0]))
                edges.append((edge[1] if along_x else edge[0], outward))
                if signal:
                    feature.append(g / 3)
        thirds.append((along_x, edges))
        (kx if along_x else ky).extend([x1, x2] if along_x else [y1, y2])
    for poly in pours:  # rectangular copper of the named nets (patches): thirds-rule on its bounding edges
        ring = np.array(poly["outline"])
        thirds.append((False, [(ring[:, 0].min(), 1), (ring[:, 0].max(), -1)]))
        thirds.append((True, [(ring[:, 1].min(), 1), (ring[:, 1].max(), -1)]))
    for pad in ports + [p for _, _, pads in parts for p in pads]:
        x0, y0, x1, y1 = pad_box(pad)
        kx += [x0, x1, pad["x"]]
        ky += [y0, y1, pad["y"]]
    for s in sites:
        (kx if s["along_x"] else ky).append(s["x"] if s["along_x"] else s["y"])
        if s["gaps"]:  # the ground edges across both coplanar gaps
            c = s["y"] if s["along_x"] else s["x"]
            (ky if s["along_x"] else kx).extend([c - s["width"] / 2 - s["gaps"][0], c + s["width"] / 2 + s["gaps"][1]])
    lam_min = C0 / (f2 * math.sqrt(er_max)) * 1e3
    fine = max(min(feature + [0.15]), 0.03)
    coarse = min(lam_min / 20, 2.0)  # openEMS guidance: no cell above lambda/20 in the densest material
    for along_x, edges in thirds:  # FDTD edge singularity: last metal line 1/3 cell inside the true edge
        for edge, metal in edges:
            (ky if along_x else kx).extend([edge + metal * fine / 3, edge - metal * 2 * fine / 3])
    # the 8 PML cells live inside the mesh: give them their own room beyond the modelled region
    pml = 8 * coarse
    air = max(C0 / f1 * 1e3 / 4, 10.0) if antenna else 0.0
    lo_x, lo_y, hi_x, hi_y = region[0] - air - pml, region[1] - air - pml, region[2] + air + pml, region[3] + air + pml
    x = lines(kx + [region[0], region[2]], lo_x, hi_x, fine, coarse)
    y = lines(ky + [region[1], region[3]], lo_y, hi_y, fine, coarse)
    z_air = air + pml if antenna else max(2.0, 3 * top)  # guided lines: first-order Mur above/below, no PML cells
    kz = [z for z0, t in layers.values() for z in (z0, z0 + t)] + [z for s in slabs for z in s[:2]]
    copper_t = [t for _, t in layers.values() if t > 0]
    z_cells = int(number(L.optional(row, "z_cells") or 4, positive=True, integer=True))  # cells per dielectric layer
    fine_z = max(min(copper_t + [(s[1] - s[0]) / z_cells for s in slabs if (s[1] - s[0]) > max(copper_t + [0.0])]), 0.01)
    z = lines(kz, -z_air, top + z_air, fine_z, coarse)
    xc, yc = (x[:-1] + x[1:]) / 2, (y[:-1] + y[1:]) / 2

    model = Model()
    gx, gy = np.meshgrid(xc, yc, indexing="ij")  # board material only inside the real outline
    inside = L.polys_contain(board.data["outline"], gx.ravel(), gy.ravel()).reshape(gx.shape)
    rects = rectangles(inside)
    for n, (z0, z1, er, tand) in enumerate(slabs):
        kappa = 2 * math.pi * f2 * EPS0 * er * tand  # exact loss at f_stop, over-estimated below it (conservative S21)
        model.add("Material", dict(Name=f"dielectric_{n}"), [(0, (x[i0], y[j0], z0), (x[i1 + 1], y[j1 + 1], z1)) for i0, i1, j0, j1 in rects],
                  prop=dict(Epsilon=f"{er:g}", Kappa=f"{kappa:.6g}"))
    # only the analysed and reference nets (and the listed parts' pads): other nets' copper has no terminations
    # in the model, so it rings as lossless resonators, and a via of one net would short another net's plane
    # wherever the mesh is coarser than its anti-pad
    modelled, listed = set(nets) | set(ref_nets), {ref for ref, _, _ in parts}
    # a support net (no port: a bias feed) is cut at the region edge rather than run into the absorbing boundary;
    # what remains beyond its bypass is a short stub
    support = set(nets) - port_nets

    def beyond(item):  # a support-net pad or via outside the region
        return item["net"] in support and not (region[0] <= item["x"] <= region[2] and region[1] <= item["y"] <= region[3])

    tracks = [c for c in (clip_segment(t, region) if t["net"] in support else t for t in all_tracks(board) if t["net"] in modelled) if c]
    metal = []
    for name, (z0, t) in layers.items():
        mask = raster(board, name, xc, yc, tracks, modelled, listed, lambda item: "x" in item and beyond(item)) & inside
        za, zb = z0, z0 + t  # t = 0 for conducting sheets (stack collapsed)
        metal += [(10, (x[i0], y[j0], za), (x[i1 + 1], y[j1 + 1], zb)) for i0, i1, j0, j1 in rectangles(mask)]
    for v in board.data["vias"]:  # barrels as PEC wires on mesh lines
        if v["net"] in modelled and not beyond(v) and x[0] < v["x"] < x[-1] and y[0] < v["y"] < y[-1]:
            vx, vy = snap(x, v["x"]), snap(y, v["y"])
            za, zb = layers[v["bottom"]][0], layers[v["top"]][0] + layers[v["top"]][1]
            metal.append((10, (vx, vy, za), (vx, vy, zb)))
    for pad in board.data["pads"]:
        if (pad["net"] in modelled or pad["ref"] in listed) and not beyond(pad) and pad["attribute"] == "pth" and len(pad["layers"]) > 1 \
                and x[0] < pad["x"] < x[-1] and y[0] < pad["y"] < y[-1]:
            px, py = snap(x, pad["x"]), snap(y, pad["y"])
            metal.append((10, (px, py, layers[pad["layers"][-1]][0]), (px, py, layers[pad["layers"][0]][0] + layers[pad["layers"][0]][1])))
    if sheet:
        model.add("ConductingSheet", dict(Name="copper", Conductivity="5.8e7", Thickness=f"{board.copper_t(board.copper[0]) * 1e-3:g}"), metal)
    else:
        model.add("Metal", dict(Name="copper"), metal)

    zref = float(number(L.optional(row, "z_ref") or 50, positive=True))
    for n, s in enumerate(sites, 1):
        if s["gaps"]:
            coplanar_port(model, n, s, layers[s["layer"]], (x, y), zref)
            DETAILS.append(f"{row['name']}: port {n} {port_names[n - 1]} at ({s['x']:.3f}, {s['y']:.3f}) mm, across the coplanar "
                           f"gaps {s['gaps'][0]:.3f}/{s['gaps'][1]:.3f} mm to {ref_nets} on {s['layer']}, {s['width']:.2f} mm wide")
            continue
        layer, plane, width = s["layer"], s["plane"], s["width"]
        below = board.copper.index(plane) > board.copper.index(layer)
        z_pad = layers[layer][0] if below else layers[layer][0] + layers[layer][1]
        z_ref = layers[plane][0] + layers[plane][1] if below else layers[plane][0]
        px, py = snap(x, s["x"]), snap(y, s["y"])
        if s["along_x"]:  # sheet across the pad where the pin/lead enters
            a, b = (px, py - width / 2, z_ref), (px, py + width / 2, z_pad)
        else:
            a, b = (px - width / 2, py, z_ref), (px + width / 2, py, z_pad)
        DETAILS.append(f"{row['name']}: port {n} {port_names[n - 1]} at ({px:.3f}, {py:.3f}) mm, {layer} to {plane} "
                       f"({abs(z_pad - z_ref):.3f} mm), {width:.2f} mm wide")
        direction = 1 if z_pad > z_ref else -1
        mid = (z_ref + z_pad) / 2
        model.add("LumpedElement", dict(Name=f"port_resist_{n}", Direction="2", Caps="1", R=f"{zref:g}"), [(50, a, b)])
        model.add("Excitation", dict(Name=f"port_excite_{n}", Type="0", Excite=f"0,0,{-direction}"), [(50, a, b)])
        centre = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        model.add("ProbeBox", dict(Name=f"port_ut{n}", Type="0", Weight="-1"), [(50, (*centre, z_ref), (*centre, z_pad))])
        model.add("ProbeBox", dict(Name=f"port_it{n}", Type="1", Weight=str(direction), NormDir="2"), [(50, (a[0], a[1], mid), (b[0], b[1], mid))])
    for ref, value, (p1, p2) in parts:
        layer = p1["layers"][0]
        z0, t = layers[layer]
        b1, b2 = pad_box(p1, layer), pad_box(p2, layer)
        axis = 0 if abs(p2["x"] - p1["x"]) >= abs(p2["y"] - p1["y"]) else 1
        first, second = (b1, b2) if (p1["x"], p1["y"])[axis] < (p2["x"], p2["y"])[axis] else (b2, b1)
        lo_t, hi_t = max(b1[1 - axis], b2[1 - axis]), min(b1[3 - axis], b2[3 - axis])
        span = (first[2 + axis], second[axis])
        a = [0.0, 0.0, z0]
        b = [0.0, 0.0, z0 + t]
        a[axis], b[axis], a[1 - axis], b[1 - axis] = span[0], span[1], lo_t, hi_t
        kind = ref[:1].upper()
        if kind == "R" and value == 0:
            model.add("Metal", dict(Name=f"link_{ref}"), [(20, tuple(a), tuple(b))])
            continue
        require(kind in {"R", "L", "C"}, f"{row['name']}: part {ref} must be an R, L or C")
        attrs = dict(Name=f"part_{ref}", Direction=str(axis), Caps="1", **{kind: f"{value:g}"})
        if kind == "L":  # a real chip inductor: series L with the ESR of its Q (openEMS's lossless series L grows without bound)
            q = float(number(L.optional(row, "l_q") or 50, positive=True))  # typical 0402/0603 chip-inductor Q near 2 GHz
            esr = math.pi * (f1 + f2) * value / q
            attrs.update(LEtype="1", R=f"{esr:g}")
            DETAILS.append(f"{row['name']}: {ref} {value:.3g} H + ESR {esr:.3g} ohm (Q {q:g} at the band centre)")
        if kind == "C":  # a real capacitor is series ESR-ESL-C; an ideal lumped C spread over the mesh never lets the energy decay
            esl, esr, source = P.body_parasitics(next(f for f in board.data["footprints"] if f["ref"] == ref), caps)
            attrs.update(LEtype="1", L=f"{esl:g}", R=f"{esr:g}")
            above = (2 * math.pi * f1) ** 2 * esl * value > 100  # 10x above self-resonance at the band bottom: X_C < 1 % of X_L
            if above:  # an ESL-ESR short in band; its huge C would only hold charge that never decays in the model
                del attrs["C"]
            DETAILS.append(f"{row['name']}: {ref} {value:.3g} F + ESL {esl * 1e9:.2g} nH + ESR {esr * 1e3:.3g} mohm [{source}]"
                           + ("; above self-resonance across the band: modelled as its ESL and ESR" if above else ""))
        model.add("LumpedElement", attrs, [(20, tuple(a), tuple(b))])
    boundary = ["PML_8"] * 6 if antenna else ["PML_8"] * 4 + ["MUR"] * 2
    return dict(model=model, grid=(x, y, z), f=(f1, f2), ports=len(ports), zref=zref, boundary=boundary,
                cells=(len(x) - 1) * (len(y) - 1) * (len(z) - 1), fine=(fine, fine_z), coarse=coarse)


# --- run + post-process ----------------------------------------------------------------------------------------
def probe(path):
    data = np.loadtxt(path, comments="%")
    return data[:, 0], data[:, 1]


def dft(t, v, f):
    """Single-sided DFT of a probe signal at the given frequencies (openEMS/CSXCAD DFT_time2freq)."""
    return np.concatenate([2 * (t[1] - t[0]) * (np.exp(-2j * np.pi * np.outer(f[k:k + 64], t)) @ v) for k in range(0, len(f), 64)])


def simulate(spec, workdir, f, excite, end_criteria=1e-5, pulses=4):
    """One openEMS run exciting port `excite`: until the field energy falls by `end_criteria` or `pulses` excitation
    lengths have passed (a weakly coupled high-Q part, such as a bypass pair, can hold energy long after the ports have
    settled: the `settled` row, not the energy, decides whether the S-parameters converged)."""
    work = Path(workdir) / f"port{excite}"
    work.mkdir(parents=True, exist_ok=True)
    xml = work / "model.xml"
    # excite only the analysed band: a pulse with DC content charges conductors that have no DC path in the model
    # (split planes, DC blocks) and that stored energy never decays to the end criterion
    f1, f2 = spec["f"]
    spec["model"].write(xml, spec["grid"], (f1 + f2) / 2, (f2 - f1) / 2, spec["boundary"], excite, end_criteria, pulses)
    command = [openems(), "model.xml", "--engine=multithreaded", "--exact-endcriteria", "--disable-dumps"]
    console = work / "console.txt"  # watch progress here (timestep, MC/s, energy in dB)
    with console.open("w", encoding="utf-8") as stream:
        run = subprocess.run(command, cwd=work, stdout=stream, stderr=subprocess.STDOUT, timeout=int(os.environ.get("ANVIL_EM_TIMEOUT", "7200")))
    text = console.read_text(encoding="utf-8", errors="replace")
    require(run.returncode == 0, f"openEMS failed ({run.returncode}): {text[-1500:]}")
    budget = re.search(r"Max\. number of timesteps:\s*(\d+)", text)
    reached = re.findall(r"Time for (\d+) iterations", text) or re.findall(r"Timestep:\s*(\d+)", text)
    if budget and reached and int(reached[-1]) >= int(budget[1]) - 1:
        level = re.findall(r"Energy: ~\S+ \((-?\s*[\d.]+)dB\)", text)
        DETAILS.append(f"  port {excite} run stopped at its {pulses:g}-pulse cap with the field energy at "
                       f"{level[-1].replace(' ', '') if level else '?'} dB, not {10 * math.log10(end_criteria):.0f} dB; the settled row judges it")
    # a diverging run ends "at the end criterion" with a NaN energy: never turn it into S-parameters
    require(not re.search(r"Energy: ~-?nan|-?nandB", text, re.IGNORECASE), "openEMS diverged (field energy NaN): an unstable lumped element or mesh")
    signals = [(probe(work / f"port_ut{n}"), probe(work / f"port_it{n}")) for n in range(1, spec["ports"] + 1)]
    require(all(np.all(np.isfinite(v)) for pair in signals for _, v in pair), "openEMS diverged: port signals are not finite")

    def waves(share):  # (incident, reflected) per port from the first `share` of the record
        out = []
        for (tu, u), (ti, i) in signals:
            k = int(len(tu) * share)
            uf, jf = dft(tu[:k], u[:k], f), dft(ti[:k], i[:k], f)
            out.append((0.5 * (uf + jf * spec["zref"]), 0.5 * (uf - jf * spec["zref"])))
        return out

    # the record without its last 10 %: how far the end of the run still moves the result
    return waves(1.0), waves(0.9), xml, text


def solve_sparams(spec, workdir, points=401, end_db=50.0, pulses=4):
    """S-matrix from one run per port, and the same without the last 10 % of each record (settling check)."""
    f1, f2 = spec["f"]
    f = np.linspace(f1, f2, points)
    n = spec["ports"]
    s, early = np.zeros((points, n, n), dtype=complex), np.zeros((points, n, n), dtype=complex)
    log = ""
    for j in range(1, n + 1):
        full, short, xml, log = simulate(spec, workdir, f, j, 10 ** (-end_db / 10), pulses)
        for i in range(n):
            s[:, i, j - 1] = full[i][1] / full[j - 1][0]
            early[:, i, j - 1] = short[i][1] / short[j - 1][0]
    return f, s, early, xml, log


def evaluate(pcb, design_dir):
    design = Path(design_dir).resolve()
    rows = table(design / "em.tsv", EM)
    board = L.Board(L.dump_board(pcb))
    out = design.parent / "analysis" / "em"
    out.mkdir(parents=True, exist_ok=True)
    results = []
    caps = table(design / "caps.tsv", ("match", "esl_nh", "esr_mohm"), allow_empty=True) if (design / "caps.tsv").is_file() else []
    DETAILS.append("EM model: copper of the named nets, their reference nets and the listed parts only (other nets omitted); "
                   "PEC copper with real thickness (no conductor loss), dielectric loss exact at f_stop and over-estimated "
                   "below it, thirds-rule mesh on RF edges, no solder mask, component bodies or connector; capacitors as series "
                   "ESR-ESL-C; lumped ports where the pin/lead enters each port pad, to the first reference plane below or "
                   "across both coplanar gaps when the same-layer ground is under half as far")
    for row in rows:
        traces(row["traces"])
        require(re.fullmatch(r"[A-Za-z0-9_-]+", row["name"]), f"em.tsv name must be a plain identifier: {row['name']!r}")
        checks = checks_of(row["checks"])
        spec = build(board, row, caps)
        DETAILS.append(f"{row['name']}: {spec['cells']} cells, fine {spec['fine'][0]:.3g}/{spec['fine'][1]:.3g} mm, coarse {spec['coarse']:.3g} mm, "
                       f"{spec['ports']} port(s), boundary {spec['boundary'][0]}")
        with tempfile.TemporaryDirectory(prefix="anvil-em-") as work:
            # -50 dB field-energy decay unless the row asks for more; the settling row below proves it was enough
            f, s, early, xml, log = solve_sparams(spec, work, end_db=float(number(L.optional(row, "end_db") or 50, positive=True)),
                                                  pulses=float(number(L.optional(row, "max_pulses") or 4, positive=True)))
            model_copy = out / f"{row['name']}.xml"
            shutil.copyfile(xml, model_copy)
        touch = write_touchstone(out / f"{row['name']}.s{spec['ports']}p", f, s, spec["zref"],
                                 f"Anvil openEMS model {row['name']} from {Path(pcb).name}\nports {row['ports']}")
        picture = plot(out / f"{row['name']}.png", f, s, checks, f"{row['name']} (openEMS)")
        OUTPUTS.update(p.resolve() for p in (touch, model_copy) + ((picture,) if picture else ()))
        DETAILS.append(f"{row['name']}: wrote {touch.name}" + (f", {picture.name}" if picture else "") + f"; openEMS: {log.strip().splitlines()[-1] if log.strip() else ''}")
        for i in range(spec["ports"]):  # where each port is best matched, and what it sees there (for tuning the match)
            k = int(np.argmin(np.abs(s[:, i, i])))
            zin = spec["zref"] * (1 + s[k, i, i]) / (1 - s[k, i, i])
            DETAILS.append(f"{row['name']}: port {i + 1} best |S{i + 1}{i + 1}| {20 * math.log10(max(abs(s[k, i, i]), 1e-12)):.1f} dB "
                           f"at {f[k]:.6g} Hz, Zin {zin.real:.1f}{zin.imag:+.1f}j ohm")
        judge(row["name"], f, s, checks, results, "openEMS FDTD of the board copper")
        band = np.zeros(len(f), dtype=bool)
        for _, _, _, _, b1, b2 in checks:
            band |= (f >= b1) & (f <= b2)
        moved = max(float(np.abs(s[band, i - 1, j - 1] - early[band, i - 1, j - 1]).max()) for i, j, *_ in checks)
        L.emit(results, f"{row['name']}:settled", moved, "|dS|", "le", 0.01,
               "largest change of a checked S-parameter in its band when the last 10 % of the run is dropped; raise end_db if it fails")
    return f"EM: {sum(results)}/{len(results)}", all(results)


def measured(design_dir):
    """Limits applied to Touchstone files (VNA measurements or vendor models) named in design/sparams.tsv."""
    design = Path(design_dir).resolve()
    results = []
    for row in table(design / "sparams.tsv", ("file", "checks", "traces")):
        traces(row["traces"])
        path = (design.parent / row["file"]).resolve()
        require(path.is_relative_to(design.parent), f"sparams file outside the project: {row['file']}")
        f, s, z0 = read_touchstone(path)
        judge(Path(row["file"]).stem, f, s, checks_of(row["checks"]), results, f"{row['file']}, reference {z0:g} ohm")
    return f"SPARAMS: {sum(results)}/{len(results)}", all(results)
