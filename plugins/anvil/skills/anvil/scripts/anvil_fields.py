#!/usr/bin/env python3
"""Numerical field solvers for board checks (numpy required).

1. `cross_section`: 2-D electrostatic finite-volume solver for transmission-line cross-sections
   (microstrip, embedded/coated microstrip, stripline, grounded coplanar waveguide, differential
   pairs) on a graded rectilinear mesh, Jacobi-preconditioned conjugate gradients, grounded box.
   Z0 = 1/(c0 sqrt(C C_air)), eps_eff = C/C_air; odd/even modes from +/- excitation.
   Validated against Cohn's exact stripline and the Hammerstad-Jensen microstrip (tests).
2. `board_thermal`: steady 2-D heat balance of a board (in-plane copper/dielectric conduction,
   two-sided convection, component heat sources) on a cell grid.
Units: mm for geometry, SI for results.
"""
from __future__ import annotations

import math

try:
    import numpy as np
except ImportError as error:  # the gate must fail loudly, never skip
    raise ValueError("numpy is required for field solvers: install it in the Python that runs Anvil") from error

EPS0 = 8.8541878128e-12
C0 = 299_792_458.0
ETA0 = 376.730313668


# --- graded mesh ------------------------------------------------------------------------------------------
def fill_interval(a, b, fine, ratio, coarse):
    length = b - a
    if length <= 1.5 * fine:
        return [a, b]
    left, right, h = [a], [b], fine
    while left[-1] + h < right[-1] - h:
        left.append(left[-1] + h)
        right.append(right[-1] - h)
        h = min(h * ratio, coarse)
    gap = right[-1] - left[-1]
    k = max(1, math.ceil(gap / h))
    return left + [left[-1] + gap * i / k for i in range(1, k)] + right[::-1]


def mesh(keys, lo, hi, fine, ratio=1.3, coarse=None):
    """Mesh lines through every key coordinate, fine next to each key and growing geometrically."""
    coarse = coarse or (hi - lo) / 20
    points = sorted({round(k, 9) for k in keys if lo <= k <= hi} | {lo, hi})
    lines = [points[0]]
    for a, b in zip(points, points[1:]):
        lines += fill_interval(a, b, fine, ratio, coarse)[1:]
    return np.array(sorted(set(round(v, 9) for v in lines)))


# --- electrostatic solver ------------------------------------------------------------------------------------
def solve(x, y, eps, fixed, potential, tol=1e-10, maxiter=20000):
    """Finite-volume Laplace solve. x, y: mesh lines (m); eps: cell permittivity (nx-1, ny-1);
    fixed: bool node mask; potential: node potentials for fixed nodes. Returns node potential array."""
    dx, dy = np.diff(x), np.diff(y)
    nx, ny = len(x), len(y)
    epad = np.zeros((nx - 1, ny + 1))
    epad[:, 1:-1] = eps
    dypad = np.concatenate([[0.0], dy, [0.0]])
    ax = (epad[:, :-1] * dypad[None, :-1] / 2 + epad[:, 1:] * dypad[None, 1:] / 2) / dx[:, None]   # (nx-1, ny)
    epad = np.zeros((nx + 1, ny - 1))
    epad[1:-1, :] = eps
    dxpad = np.concatenate([[0.0], dx, [0.0]])
    ay = (epad[:-1, :] * dxpad[:-1, None] / 2 + epad[1:, :] * dxpad[1:, None] / 2) / dy[None, :]   # (nx, ny-1)

    def apply(phi):
        out = np.zeros_like(phi)
        fx = ax * (phi[1:, :] - phi[:-1, :])
        out[:-1, :] -= fx
        out[1:, :] += fx
        fy = ay * (phi[:, 1:] - phi[:, :-1])
        out[:, :-1] -= fy
        out[:, 1:] += fy
        return out

    free = ~fixed
    base = np.where(fixed, potential, 0.0)
    rhs = -apply(base) * free
    diag = np.zeros((nx, ny))
    diag[:-1, :] += ax
    diag[1:, :] += ax
    diag[:, :-1] += ay
    diag[:, 1:] += ay
    inv = np.where(free, 1.0 / np.where(diag > 0, diag, 1.0), 0.0)
    xk = np.zeros((nx, ny))
    r = rhs.copy()
    z = inv * r
    p = z.copy()
    rz = float(np.sum(r * z))
    norm = math.sqrt(float(np.sum(rhs * rhs))) or 1.0
    for _ in range(maxiter):
        ap = apply(p) * free
        alpha = rz / float(np.sum(p * ap))
        xk += alpha * p
        r -= alpha * ap
        if math.sqrt(float(np.sum(r * r))) < tol * norm:
            break
        z = inv * r
        rz_new = float(np.sum(r * z))
        p = z + (rz_new / rz) * p
        rz = rz_new
    else:
        raise ValueError("field solver did not converge; refine or enlarge the model")
    phi = base + xk
    return phi, apply(phi)


def cross_section(slabs, conductors, box, fine=None):
    """slabs: [(y0, y1, er)] dielectric layers (mm, air elsewhere); conductors: [dict(x0, x1, y0, y1, v)]
    rectangles (v = volts; 0 for ground); box: (xmin, xmax, ymin, ymax) grounded enclosure (mm).
    Returns (charge per conductor [C/m] with dielectrics, same in air), Richardson-extrapolated from
    two mesh densities: node conductors reach half a cell past their true edge, a first-order error."""
    thick = [c["y1"] - c["y0"] for c in conductors if c["y1"] > c["y0"]]
    widths = [c["x1"] - c["x0"] for c in conductors]
    fine = fine or max(min([t / 3 for t in thick] + [w / 40 for w in widths] + [(s[1] - s[0]) / 10 for s in slabs]), 1e-4)
    # Validated (tests): <= 0.5 % vs Cohn's exact stripline and Hammerstad-Jensen microstrip, <= 0.9 % vs
    # conformal-mapping CPWG. Far-field cells are left coarse on purpose: refining them costs 20x run
    # time for < 0.05 % change.
    coarse_q = _cross_section(slabs, conductors, box, fine, 1.3, None)
    fine_q = _cross_section(slabs, conductors, box, fine / 2, 1.3, None)
    return tuple([2 * f - c for f, c in zip(fq, cq)] for fq, cq in zip(fine_q, coarse_q))


def _cross_section(slabs, conductors, box, fine, ratio, coarse):
    xs = [c[k] for c in conductors for k in ("x0", "x1")]
    ys = [c[k] for c in conductors for k in ("y0", "y1")] + [s[k] for s in slabs for k in (0, 1)]
    x = mesh(xs, box[0], box[1], fine, ratio, coarse) * 1e-3
    y = mesh(ys, box[2], box[3], fine, ratio, coarse) * 1e-3
    xc, yc = (x[:-1] + x[1:]) / 2e-3, (y[:-1] + y[1:]) / 2e-3
    results = []
    for use_dielectric in (True, False):
        eps = np.ones((len(x) - 1, len(y) - 1))
        if use_dielectric:
            for y0, y1, er in slabs:
                eps[:, (yc > y0) & (yc < y1)] = er
        fixed = np.zeros((len(x), len(y)), dtype=bool)
        fixed[0, :] = fixed[-1, :] = fixed[:, 0] = fixed[:, -1] = True
        potential = np.zeros((len(x), len(y)))
        masks = []
        tol = 1e-9
        for c in conductors:
            m = ((x[:, None] >= c["x0"] * 1e-3 - tol) & (x[:, None] <= c["x1"] * 1e-3 + tol)
                 & (y[None, :] >= c["y0"] * 1e-3 - tol) & (y[None, :] <= c["y1"] * 1e-3 + tol))
            fixed |= m
            potential[m] = c["v"]
            masks.append(m)
        phi, flux = solve(x, y, eps, fixed, potential)
        results.append([EPS0 * float(np.sum(flux[m])) for m in masks])
    return results[0], results[1]


def line(kind, w, h, er, t=0.035, s=None, gap=None, h2=None, er2=None, mask_t=0.0, mask_er=3.5, gnd_w=None, fine=None, box_scale=1.0):
    """Textbook geometries: microstrip | stripline | cpwg | diff_microstrip | diff_stripline (h: dielectric
    below the trace to its plane; h2/er2: dielectric above to the upper plane for stripline; s: edge spacing
    for pairs; gap: coplanar ground gap; mask_t/mask_er: solder mask over outer layers)."""
    top_plane = kind.endswith("stripline")
    return stack_line([(h, er)], [(h2 or h, er2 or er)] if top_plane else [], w, t, top_plane=top_plane,
                      mask=(mask_t, mask_er) if mask_t > 0 and not top_plane else None,
                      s=s if kind.startswith("diff") else None, gap=gap, gnd_w=gnd_w, fine=fine, box_scale=box_scale)


def stack_line(below, above, w, t=0.035, top_plane=False, mask=None, s=None, gap=None, gnd_w=None, fine=None, box_scale=1.0):
    """Characteristic impedance of a trace in a real stackup from a field solution.
    below: [(thickness_mm, er)] from the trace down to its reference plane, nearest first.
    above: [(thickness_mm, er)] from the trace upward, nearest first: to the upper reference plane when
    top_plane (stripline), else to the board surface (embedded microstrip; empty for outer layers).
    mask: (thickness_mm, er) solder mask on the surface. s: edge spacing of a differential pair (odd/even
    modes solved). gap: same-layer ground gap (grounded coplanar), a number or (left, right) with None for
    no ground on that side; gnd_w: coplanar ground width."""
    diff = s is not None
    h = sum(tk for tk, _ in below)
    slabs, y = [], h
    for tk, er_ in below:
        slabs.append((y - tk, y, er_))
        y -= tk
    band_er = above[0][1] if above else (mask[1] if mask else 1.0)
    slabs.append((h, h + t, band_er))  # the dielectric (or mask) that surrounds the copper layer
    y = h + t
    for tk, er_ in above:
        slabs.append((y, y + tk, er_))
        y += tk
    if mask and not top_plane:
        slabs.append((y, y + mask[0], mask[1]))
    gaps = tuple(gap) if isinstance(gap, (tuple, list)) else (gap, gap)  # (left, right); None = no side ground
    span = ((2 * w + s) if diff else w) + 2 * max([g for g in gaps if g] or [0.0])  # the region the field lives in
    margin = box_scale * (12 * max(h, y if top_plane else h) + 4 * span)
    ymax = y if top_plane else y + (mask[0] if mask else 0.0) + box_scale * max(20 * h, 10 * span)
    box = (-span / 2 - margin, span / 2 + margin, -0.2 * h, ymax)
    conductors = [dict(x0=box[0], x1=box[1], y0=box[2], y1=0.0, v=0.0)]
    if top_plane:
        conductors.append(dict(x0=box[0], x1=box[1], y0=y, y1=ymax, v=0.0))
    if diff:
        conductors += [dict(x0=-s / 2 - w, x1=-s / 2, y0=h, y1=h + t, v=1.0), dict(x0=s / 2, x1=s / 2 + w, y0=h, y1=h + t, v=-1.0)]
    else:
        conductors.append(dict(x0=-w / 2, x1=w / 2, y0=h, y1=h + t, v=1.0))
    edge = s / 2 + w if diff else w / 2
    for sign, g in zip((-1, 1), gaps):  # side grounds run to the box edge (a wide pour) unless a finite width is given
        if g:
            inner = edge + g
            outer = min(edge + g + gnd_w, box[1]) if gnd_w else box[1]
            conductors.append(dict(x0=min(sign * inner, sign * outer), x1=max(sign * inner, sign * outer), y0=h, y1=h + t, v=0.0))
    q, q_air = cross_section(slabs, conductors, box, fine)
    index = 1 + int(top_plane)  # conductors: bottom plane, [top plane], trace(s)
    c, c_air = q[index], q_air[index]
    z = 1.0 / (C0 * math.sqrt(c * c_air))
    result = dict(z0=z, er_eff=c / c_air, delay_ps_per_mm=math.sqrt(c / c_air) / C0 * 1e9,
                  c_pf_per_mm=c * 1e9, l_nh_per_mm=1.0 / (C0 * C0 * c_air) * 1e6)
    if diff:
        result.update(zodd=z, zdiff=2 * z)
        for cond in conductors:
            if cond["v"] == -1.0:
                cond["v"] = 1.0
        qe, qe_air = cross_section(slabs, conductors, box, fine)
        ze = 1.0 / (C0 * math.sqrt(qe[index] * qe_air[index]))
        result.update(zeven=ze, zcommon=ze / 2)
    return result


# --- closed forms used as references and quick estimates ------------------------------------------------------
def ellipk(k):
    """Complete elliptic integral of the first kind K(k) by the arithmetic-geometric mean."""
    a, b = 1.0, math.sqrt(1.0 - k * k)
    for _ in range(60):
        a, b = (a + b) / 2, math.sqrt(a * b)
    return math.pi / (2 * a)


def stripline_exact(w, b, er):
    """Cohn's exact zero-thickness centred stripline: Z0 = (eta0/4/sqrt(er)) K(k)/K(k'), k = sech(pi w / 2b)."""
    k = 1.0 / math.cosh(math.pi * w / (2 * b))
    kp = math.tanh(math.pi * w / (2 * b))
    return ETA0 / (4 * math.sqrt(er)) * ellipk(k) / ellipk(kp)


def microstrip_hj(w, h, er):
    """Hammerstad & Jensen (1980) zero-thickness microstrip: Z0 and eps_eff (quoted accuracy < 0.2 %)."""
    u = w / h
    a = 1 + math.log((u ** 4 + (u / 52) ** 2) / (u ** 4 + 0.432)) / 49 + math.log(1 + (u / 18.1) ** 3) / 18.7
    bb = 0.564 * ((er - 0.9) / (er + 3)) ** 0.053
    eeff = (er + 1) / 2 + (er - 1) / 2 * (1 + 10 / u) ** (-a * bb)
    f = 6 + (2 * math.pi - 6) * math.exp(-((30.666 / u) ** 0.7528))
    z_air = ETA0 / (2 * math.pi) * math.log(f / u + math.sqrt(1 + (2 / u) ** 2))
    return z_air / math.sqrt(eeff), eeff


def cpwg_closed(w, gap, h, er):
    """Grounded coplanar waveguide, zero thickness, infinite side grounds (conformal mapping, Ghione/Wadell).
    Valid for gap <~ h only: at wider gaps it overshoots the microstrip limit (g=6h: +8 %), which the field
    solver reaches correctly; never use it to judge a real layout."""
    k = w / (w + 2 * gap)
    k1 = math.tanh(math.pi * w / (4 * h)) / math.tanh(math.pi * (w + 2 * gap) / (4 * h))
    r, r1 = ellipk(k) / ellipk(math.sqrt(1 - k * k)), ellipk(k1) / ellipk(math.sqrt(1 - k1 * k1))
    eeff = (1 + er * r1 / r) / (1 + r1 / r)
    return 60 * math.pi / math.sqrt(eeff) / (r + r1), eeff


# --- board thermal ------------------------------------------------------------------------------------------
def board_thermal(sheet, inside, power, h_total, ambient, cell_mm, tol=1e-10):
    """Steady 2-D board temperature. sheet: in-plane conductance k*t per cell [W/K] (sum over copper and
    dielectric layers); inside: bool mask of board cells; power: W per cell; h_total: convection +
    radiation coefficient summed over both faces [W/m^2K]; returns temperature [C] (NaN outside)."""
    area = (cell_mm * 1e-3) ** 2
    g_conv = np.where(inside, h_total * area, 0.0)
    kx = np.where(inside[:-1, :] & inside[1:, :], 2 * sheet[:-1, :] * sheet[1:, :] / np.maximum(sheet[:-1, :] + sheet[1:, :], 1e-30), 0.0)
    ky = np.where(inside[:, :-1] & inside[:, 1:], 2 * sheet[:, :-1] * sheet[:, 1:] / np.maximum(sheet[:, :-1] + sheet[:, 1:], 1e-30), 0.0)

    def apply(theta):
        out = g_conv * theta
        fx = kx * (theta[1:, :] - theta[:-1, :])
        out[:-1, :] -= fx
        out[1:, :] += fx
        fy = ky * (theta[:, 1:] - theta[:, :-1])
        out[:, :-1] -= fy
        out[:, 1:] += fy
        return out * inside

    diag = g_conv.copy()
    diag[:-1, :] += kx
    diag[1:, :] += kx
    diag[:, :-1] += ky
    diag[:, 1:] += ky
    inv = np.where(inside, 1.0 / np.where(diag > 0, diag, 1.0), 0.0)
    rhs = np.where(inside, power, 0.0)
    theta = np.zeros_like(rhs)
    r = rhs.copy()
    z = inv * r
    p = z.copy()
    rz = float(np.sum(r * z))
    norm = math.sqrt(float(np.sum(rhs * rhs))) or 1.0
    for _ in range(50000):
        ap = apply(p)
        alpha = rz / float(np.sum(p * ap))
        theta += alpha * p
        r -= alpha * ap
        if math.sqrt(float(np.sum(r * r))) < tol * norm:
            break
        z = inv * r
        rz_new = float(np.sum(r * z))
        p = z + (rz_new / rz) * p
        rz = rz_new
    else:
        raise ValueError("thermal solver did not converge")
    return np.where(inside, ambient + theta, np.nan)
