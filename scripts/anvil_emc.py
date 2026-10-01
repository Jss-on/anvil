#!/usr/bin/env python3
"""Radiated-emission pre-compliance estimate from the routed board (numpy required).

`emc <pcb> <design-dir>` reads design/emc.tsv. For each clock/data net the loop is measured on the board:
every segment's length times its height to the reference plane (field-solver cross-section), and the
line's Z0 sets the harmonic current I_n = V_n / Z0 of the trapezoidal waveform (PAUL-1044). Each
harmonic radiates as a small loop, E = 1.316e-14 f^2 I A / d (PAUL-2011), +6 dB for the ground-plane
reflection of an OATS/SAC measurement; optional cable rows add the common-mode dipole
E = 1.257e-6 f I_C L / d (PAUL-2018) from a measured or budgeted CM current. The worst harmonic is
compared with the limit line (FCC Part 15 Class A/B, CISPR 32 Class A/B: PAUL-1022..1025) less a
design margin (default 6 dB). This is an estimate for steering the design (+/-10 dB); only a
chamber measurement demonstrates compliance.
"""
from __future__ import annotations

import math
import re
from pathlib import Path

import numpy as np

import anvil_layout as L
from anvil import DETAILS, OUTPUTS, number, require, table, traces

EMC = ("net", "v_swing", "f_clock_hz", "duty", "rise_ps", "limit", "traces")
# (f_low_Hz, f_high_Hz, dBuV/m) at the stated distance (m); quasi-peak below 1 GHz, average above
LIMITS = {
    "fcc_b": (3.0, [(30e6, 88e6, 40.0), (88e6, 216e6, 43.5), (216e6, 960e6, 46.0), (960e6, 40e9, 54.0)]),       # PAUL-1022
    "fcc_a": (10.0, [(30e6, 88e6, 39.0), (88e6, 216e6, 43.5), (216e6, 960e6, 46.4), (960e6, 40e9, 49.5)]),      # PAUL-1023
    "cispr32_b": (10.0, [(30e6, 230e6, 30.0), (230e6, 1e9, 37.0)]),                                              # PAUL-1024
    "cispr32_a": (10.0, [(30e6, 230e6, 40.0), (230e6, 1e9, 47.0)]),                                              # PAUL-1025
}


def limit_at(name, f):
    for lo, hi, level in LIMITS[name][1]:
        if lo <= f < hi:
            return level
    return None


def harmonics(v, f0, duty, tr, f_max):
    """One-sided trapezoid harmonic amplitudes |c_n| (V) for n f0 <= f_max (PAUL-1044, tr = tf)."""
    n = np.arange(1, int(f_max // f0) + 1)
    sinc = lambda x: np.where(x == 0, 1.0, np.sin(x) / np.where(x == 0, 1.0, x))  # noqa: E731
    return n * f0, 2 * v * duty * np.abs(sinc(n * math.pi * duty)) * np.abs(sinc(n * math.pi * tr * f0))


def loop(board, net, ref_nets):
    """(loop area m^2, median Z0 ohm, routed length mm) of a net over its reference plane."""
    area, z, length = 0.0, [], 0.0
    for t in board.tracks(net):
        seg = math.dist(t["start"], t["end"])
        if seg < 1e-6:
            continue
        x, y = (t["start"][0] + t["end"][0]) / 2, (t["start"][1] + t["end"][1]) / 2
        xs = L.cross_section_of(board, t["layer"], x, y, ref_nets, t["width"], (t["end"][0] - t["start"][0], t["end"][1] - t["start"][1]))
        require(xs, f"{net}: segment on {t['layer']} at ({x:.2f},{y:.2f}) has no reference plane; its return loop is undefined")
        area += seg * 1e-3 * sum(tk for tk, _ in xs["below"]) * 1e-3
        z.append(L.solve_line(xs, t["width"])["z0"])
        length += seg
    require(z, f"{net}: no routed copper")
    return area, float(np.median(z)), length


def plot(path, curves, limit_name):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        DETAILS.append("NOTE: matplotlib missing; emission plot skipped")
        return None
    fig, ax = plt.subplots(figsize=(7, 4), tight_layout=True)
    for label, f, e in curves:
        ax.semilogx(f, e, "o", markersize=3, label=label)
    for lo, hi, level in LIMITS[limit_name][1]:
        ax.plot([lo, min(hi, 6e9)], [level, level], "r-", linewidth=1.5)
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel(f"E (dBuV/m) at {LIMITS[limit_name][0]:g} m")
    ax.set_title(f"Radiated-emission estimate vs {limit_name} (estimate, +/-10 dB)")
    ax.grid(True, which="both", alpha=0.4)
    ax.legend(fontsize=8)
    fig.savefig(path, dpi=130)
    plt.close(fig)
    return Path(path)


def evaluate(pcb, design_dir):
    design = Path(design_dir).resolve()
    rows = table(design / "emc.tsv", EMC)
    board = L.Board(L.dump_board(pcb))
    results, curves, limits = [], [], set()
    for row in rows:
        traces(row["traces"])
        name = row["limit"].lower()
        require(name in LIMITS, f"limit must be one of {sorted(LIMITS)}")
        limits.add(name)
        d = LIMITS[name][0]
        margin_db = float(number(L.optional(row, "margin_db") or 6, minimum=0))
        f0, duty = float(number(row["f_clock_hz"], positive=True)), float(number(row["duty"], positive=True))
        require(duty < 1, "duty is a fraction (0.5 for a clock)")
        tr = float(number(row["rise_ps"], positive=True)) * 1e-12
        f_top = LIMITS[name][1][-1][1] if name.startswith("cispr") else 6e9
        f, vn = harmonics(float(number(row["v_swing"], positive=True)), f0, duty, tr, f_top)
        if L.optional(row, "cable_len_m"):  # common-mode dipole from a measured/budgeted CM current (PAUL-2018)
            i_cm = float(number(row["i_cm_ua"], positive=True)) * 1e-6
            e = 1.257e-6 * f * i_cm * float(number(row["cable_len_m"], positive=True)) / d * np.ones_like(vn)
            label = f"{row['net']} (CM cable)"
            source = f"CM {i_cm * 1e6:g} uA on {row['cable_len_m']} m"
        else:
            net = row["net"] if row["net"] in board.data["nets"] else "/" + row["net"]
            require(net in board.data["nets"], f"net {row['net']} not on the board")
            area, z0, length = loop(board, net, [n for n in (L.optional(row, "ref_net") or "GND").split(",") if n])
            e = 2 * 1.316e-14 * f ** 2 * (vn / z0) * area / d  # x2: ground-plane reflection of the test site
            label = row["net"]
            source = f"loop {area * 1e6:.3g} mm^2 ({length:.1f} mm routed), Z0 {z0:.1f} ohm"
        level = 20 * np.log10(np.maximum(e, 1e-30) / 1e-6)
        lim = np.array([limit_at(name, x) if limit_at(name, x) is not None else np.nan for x in f])
        valid = ~np.isnan(lim)
        require(valid.any(), f"{row['net']}: no harmonic falls inside the {name} limit band")
        excess = level[valid] - lim[valid]
        k = int(np.argmax(excess))
        worst_f = f[valid][k]
        L.emit(results, f"{row['net']}:excess_over_{name}", float(excess[k]), "dB", "le", f"{-margin_db:g}",
               f"worst harmonic {worst_f / 1e6:.4g} MHz: {level[valid][k]:.1f} dBuV/m vs {lim[valid][k]:g} at {d:g} m; {source}; "
               "PAUL-2011/2018 estimate (+/-10 dB), not a compliance result")
        curves.append((name, label, f[valid], level[valid]))
    out = design.parent / "analysis" / "emc"
    out.mkdir(parents=True, exist_ok=True)
    for name in sorted(limits):
        mine = [(label, f, e) for limit_name, label, f, e in curves if limit_name == name]
        picture = plot(out / f"emc-{re.sub(r'[^a-z0-9_]', '_', name)}.png", mine, name)
        if picture:
            OUTPUTS.add(picture.resolve())
    return f"EMC_ESTIMATE: {sum(results)}/{len(results)}", all(results)
