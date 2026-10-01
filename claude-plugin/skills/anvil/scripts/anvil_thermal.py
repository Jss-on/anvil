#!/usr/bin/env python3
"""Board thermal: a layered (2.5-D) steady-state model built from the board's own copper (numpy required).

`thermal <pcb> <design-dir>` reads design/thermal.tsv (one row per dissipating part). Every copper layer is a
grid of cells whose in-plane conductance is the copper actually there (coverage from tracks, pads, zones,
vias, supersampled 3x3 per cell, k_Cu = 386 W/m.K) plus its share of the neighbouring dielectric
(k_xy, BROOKS-017); adjacent layers couple through the dielectric (k_z) and through every plated via
barrel in the cell; the outer faces lose heat to still air with a combined convection + radiation
coefficient (BROOKS-052/053: ~10-11 W/m^2.K per face). Each part's power enters the board under its pads;
Tj = T_board(pads, max) + P x theta_jb from the datasheet. Conservative defaults: k_xy 0.5, k_z 0.3,
h 10 W/m^2.K; override per row (all rows must agree). The heat map goes to analysis/thermal/.
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np

import anvil_em as E
import anvil_layout as L
from anvil import DETAILS, OUTPUTS, number, require, table, traces

THERMAL = ("ref", "power_w", "theta_jb_c_per_w", "max_tj_c", "ambient_c", "traces")
K_CU = 386.0  # W/m.K (BROOKS-017)


def coverage(board, layer, xc, yc, cell, tracks, sub=3):
    """Copper fraction of each cell on one layer (sub x sub samples per cell)."""
    offsets = (np.arange(sub) + 0.5) / sub - 0.5
    fx = (xc[:, None] + offsets[None, :] * cell).ravel()
    fy = (yc[:, None] + offsets[None, :] * cell).ravel()
    hit = E.raster(board, layer, fx, fy, tracks).astype(float)
    return hit.reshape(len(xc), sub, len(yc), sub).mean(axis=(1, 3))


def solve(sheet, vertical, inside, power, h_faces, cell_mm, tol=1e-10):
    """Steady temperature rise [K] on a (layers, nx, ny) grid.
    sheet: in-plane k*t per layer and cell [W/K]; vertical: conductance between layer l and l+1 [W/K]
    (layers-1, nx, ny); h_faces: (h_top, h_bottom) W/m^2.K on the outer layers; power: W per cell."""
    area = (cell_mm * 1e-3) ** 2
    n = sheet.shape[0]
    conv = np.zeros_like(sheet)
    conv[0] = h_faces[0] * area
    conv[-1] += h_faces[1] * area
    conv *= inside
    kx = np.where(inside[None, :-1, :] & inside[None, 1:, :], 2 * sheet[:, :-1, :] * sheet[:, 1:, :] / np.maximum(sheet[:, :-1, :] + sheet[:, 1:, :], 1e-30), 0.0)
    ky = np.where(inside[None, :, :-1] & inside[None, :, 1:], 2 * sheet[:, :, :-1] * sheet[:, :, 1:] / np.maximum(sheet[:, :, :-1] + sheet[:, :, 1:], 1e-30), 0.0)
    kz = vertical * inside[None]

    def apply(t):
        out = conv * t
        fx = kx * (t[:, 1:, :] - t[:, :-1, :])
        out[:, :-1, :] -= fx
        out[:, 1:, :] += fx
        fy = ky * (t[:, :, 1:] - t[:, :, :-1])
        out[:, :, :-1] -= fy
        out[:, :, 1:] += fy
        if n > 1:
            fz = kz * (t[1:] - t[:-1])
            out[:-1] -= fz
            out[1:] += fz
        return out * inside[None]

    diag = conv.copy()
    diag[:, :-1, :] += kx
    diag[:, 1:, :] += kx
    diag[:, :, :-1] += ky
    diag[:, :, 1:] += ky
    if n > 1:
        diag[:-1] += kz
        diag[1:] += kz
    mask = np.broadcast_to(inside[None], sheet.shape)
    inv = np.where(mask, 1.0 / np.where(diag > 0, diag, 1.0), 0.0)
    rhs = np.where(mask, power, 0.0)
    theta = np.zeros_like(rhs)
    r = rhs.copy()
    z = inv * r
    p = z.copy()
    rz = float(np.sum(r * z))
    norm = math.sqrt(float(np.sum(rhs * rhs))) or 1.0
    for _ in range(200000):
        ap = apply(p)
        alpha = rz / float(np.sum(p * ap))
        theta += alpha * p
        r -= alpha * ap
        if math.sqrt(float(np.sum(r * r))) < tol * norm:
            return np.where(mask, theta, np.nan)
        z = inv * r
        rz_new = float(np.sum(r * z))
        p = z + (rz_new / rz) * p
        rz = rz_new
    raise ValueError("thermal solver did not converge")


def model(board, cell, k_xy, k_z):
    """Grid, outline mask, per-layer sheet conductance and inter-layer conductance from the board copper."""
    require(board.stack, "board has no physical stackup: define the fabricator's stackup in Board Setup")
    pts = np.array([p for poly in board.data["outline"] for p in poly["outline"]])
    require(len(pts), "board has no outline")
    xc = np.arange(pts[:, 0].min(), pts[:, 0].max(), cell) + cell / 2
    yc = np.arange(pts[:, 1].min(), pts[:, 1].max(), cell) + cell / 2
    gx, gy = np.meshgrid(xc, yc, indexing="ij")
    inside = L.polys_contain(board.data["outline"], gx.ravel(), gy.ravel()).reshape(gx.shape)
    tracks = E.all_tracks(board)
    names = board.copper
    cover = np.array([coverage(board, layer, xc, yc, cell, tracks) for layer in names])
    t_cu = np.array([board.copper_t(layer) for layer in names]) * 1e-3
    gaps = [sum(t for t, _, _ in gap) * 1e-3 for gap in board.stack["gaps"]]
    sheet = K_CU * t_cu[:, None, None] * cover
    for i, g in enumerate(gaps):  # each dielectric slab's in-plane conduction split between its two faces
        sheet[i] += k_xy * g / 2
        sheet[i + 1] += k_xy * g / 2
    area = (cell * 1e-3) ** 2
    vertical = np.array([np.full(gx.shape, k_z * area / g) for g in gaps]) if gaps else np.zeros((0,) + gx.shape)
    index = {name: i for i, name in enumerate(names)}
    for v in board.data["vias"]:  # plated barrels: 20 um wall, the plating anvil_rules assumes for via current
        i, j = int((v["x"] - xc[0] + cell / 2) // cell), int((v["y"] - yc[0] + cell / 2) // cell)
        if 0 <= i < len(xc) and 0 <= j < len(yc):
            r_out = v["drill"] / 2 * 1e-3
            a_wall = math.pi * (r_out ** 2 - max(r_out - 20e-6, 0) ** 2)
            for k in range(index[v["top"]], index[v["bottom"]]):
                vertical[k, i, j] += K_CU * a_wall / gaps[k]
    return xc, yc, inside, sheet, vertical


def heat_map(path, xc, yc, temp, parts):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        DETAILS.append("NOTE: matplotlib missing; heat map skipped")
        return None
    fig, ax = plt.subplots(figsize=(7, 5), tight_layout=True)
    img = ax.imshow(temp.T, origin="upper", extent=(xc[0], xc[-1], yc[-1], yc[0]), cmap="inferno")
    fig.colorbar(img, ax=ax, label="board temperature (C), hottest layer")
    for ref, (x, y, tj) in parts.items():
        ax.annotate(f"{ref} Tj {tj:.0f}C", (x, y), color="cyan", fontsize=7, ha="center")
    ax.set_xlabel("x (mm)")
    ax.set_ylabel("y (mm)")
    fig.savefig(path, dpi=130)
    plt.close(fig)
    return Path(path)


def evaluate(pcb, design_dir):
    design = Path(design_dir).resolve()
    rows = table(design / "thermal.tsv", THERMAL)
    board = L.Board(L.dump_board(pcb))
    settings = {}
    for key, default in (("k_xy", 0.5), ("k_z", 0.3), ("h_w_m2k", 10.0), ("cell_mm", 0.5)):
        values = {L.optional(r, key) for r in rows} - {None}
        require(len(values) <= 1, f"thermal.tsv rows disagree on {key}")
        settings[key] = float(number(values.pop() if values else default, positive=True))
    ambients = {float(number(r["ambient_c"])) for r in rows}
    require(len(ambients) == 1, "thermal.tsv rows must share one ambient_c")
    ambient = ambients.pop()
    cell = settings["cell_mm"]
    xc, yc, inside, sheet, vertical = model(board, cell, settings["k_xy"], settings["k_z"])
    power = np.zeros_like(sheet)
    index = {name: i for i, name in enumerate(board.copper)}
    spots = {}
    for row in rows:
        traces(row["traces"])
        pads = [p for p in board.data["pads"] if p["ref"] == row["ref"]]
        require(pads, f"thermal.tsv part {row['ref']} not on the board")
        layer = index[pads[0]["layers"][0]]
        gx, gy = np.meshgrid(xc, yc, indexing="ij")
        under = np.zeros(gx.shape, dtype=bool)
        for pad in pads:
            shapes = pad["shapes"].get(board.copper[layer]) or next(iter(pad["shapes"].values()))
            under |= L.polys_contain(shapes, gx.ravel(), gy.ravel()).reshape(gx.shape)
        if not under.any():  # pads smaller than a cell: the cells holding the pad centres
            for pad in pads:
                under[int(np.argmin(np.abs(xc - pad["x"]))), int(np.argmin(np.abs(yc - pad["y"])))] = True
        watts = float(number(row["power_w"], minimum=0))
        power[layer][under] += watts / under.sum()
        spots[row["ref"]] = (layer, under, watts)
    rise = solve(sheet, vertical, inside, power, (settings["h_w_m2k"], settings["h_w_m2k"]), cell)
    total = float(np.nansum(power))
    convected = float(np.nansum(rise[0] * settings["h_w_m2k"] * (cell * 1e-3) ** 2) + np.nansum(rise[-1] * settings["h_w_m2k"] * (cell * 1e-3) ** 2))
    DETAILS.append(f"thermal: {len(board.copper)} layers, {int(inside.sum())} cells of {cell} mm, k_xy {settings['k_xy']}, k_z {settings['k_z']}, "
                   f"h {settings['h_w_m2k']} W/m^2K per face; energy balance {convected:.4g} W out / {total:.4g} W in")
    results, marks = [], {}
    for row in rows:
        layer, under, watts = spots[row["ref"]]
        board_c = ambient + float(np.nanmax(rise[layer][under]))
        tj = board_c + watts * float(number(row["theta_jb_c_per_w"], minimum=0))
        pad = next(p for p in board.data["pads"] if p["ref"] == row["ref"])
        marks[row["ref"]] = (pad["x"], pad["y"], tj)
        L.emit(results, f"{row['ref']}:tj", tj, "C", "le", row["max_tj_c"],
               f"board under pads {board_c:.1f} C + {watts:g} W x theta_jb {row['theta_jb_c_per_w']} C/W (layered board model)")
    hottest = ambient + np.nanmax(rise, axis=0)
    out = design.parent / "analysis" / "thermal"
    out.mkdir(parents=True, exist_ok=True)
    picture = heat_map(out / "thermal.png", xc, yc, hottest, marks)
    if picture:
        OUTPUTS.add(picture.resolve())
    DETAILS.append(f"thermal: hottest board point {np.nanmax(hottest):.1f} C at ambient {ambient:g} C")
    return f"THERMAL: {sum(results)}/{len(results)}", all(results)
