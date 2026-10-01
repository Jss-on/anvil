#!/usr/bin/env python3
"""Verification plots: ngspice raw waveforms per corner, assertion margins, rule margins.

matplotlib is an optional dependency; its absence is an error, never a silent skip.
Plot runs re-execute the corner circuit with a rawfile (ngspice forbids .measure with -r),
so a plot is always produced from a fresh run of the same materialized variant.
"""
from __future__ import annotations

import math
import json
import re
import struct
import tempfile
from pathlib import Path

from anvil import DETAILS, corner_cases, execute, executable, inside, read, require, table


def parse_raw(data: bytes):
    """Parse an ngspice rawfile (ASCII or binary). Returns (variables, columns)."""
    header_end = None
    for marker in (b"Values:", b"Binary:"):
        pos = data.find(marker)
        if pos >= 0 and (header_end is None or pos < header_end[0]):
            header_end = (pos, marker)
    require(header_end, "rawfile has no Values/Binary section")
    header = data[:header_end[0]].decode("ascii", errors="replace").replace("\r", "")
    fields = dict(re.findall(r"^([A-Za-z. ]+?):\s*(.*)$", header, re.M))
    count = int(fields["No. Variables"])
    points = int(fields["No. Points"].strip())
    names = [line.split("\t")[2] for line in re.findall(r"^\t\d+\t\S+\t\S+", header, re.M)]
    if not names:
        names = [line.split()[1] for line in re.findall(r"^\s*\d+\s+\S+\s+\S+", header.split("Variables:")[1], re.M)]
    require(len(names) == count, "rawfile variable list mismatch")
    complex_data = "complex" in fields.get("Flags", "")
    columns = [[] for _ in range(count)]
    body = data[header_end[0] + len(header_end[1]):]
    if header_end[1] == b"Values:":
        tokens = body.decode("ascii", errors="replace").split()
        index = 0
        for _ in range(points):
            index += 1  # point index
            for column in columns:
                token = tokens[index]
                index += 1
                if complex_data:
                    real, imag = token.split(",")
                    column.append(complex(float(real), float(imag)))
                else:
                    column.append(float(token))
    else:
        body = body.lstrip(b"\r\n")
        width = 16 if complex_data else 8
        for point in range(points):
            for column in columns:
                offset = (point * count + columns.index(column)) * width
                if complex_data:
                    real, imag = struct.unpack_from("<dd", body, offset)
                    column.append(complex(real, imag))
                else:
                    column.append(struct.unpack_from("<d", body, offset)[0])
    return names, columns


def materialize(circuit, corner):
    source = read(circuit)
    for key, value in corner.items():
        pattern = rf"(?im)^(\.param\s+{re.escape(key)}\s*=\s*)[^\s;]+\s*(?:;[^\n]*)?$"
        source, replaced = re.subn(pattern, lambda m: m[1] + value, source)
        require(replaced == 1, f"{circuit}: declare corner {key} on its own .param line exactly once")
    # Strip .measure lines: ngspice refuses .measure when a rawfile is requested.
    return re.sub(r"(?im)^\.meas(?:ure)?\b[^\n]*\n?", "", source)


def run_raw(circuit, corner):
    circuit = Path(circuit).resolve()
    with tempfile.TemporaryDirectory(prefix=".anvil-plot-", dir=circuit.parent) as temp:
        variant, raw, log = Path(temp) / "corner.cir", Path(temp) / "out.raw", Path(temp) / "run.txt"
        variant.write_text(materialize(circuit, corner), encoding="utf-8")
        run = execute([executable("ngspice"), "-n", "-b", "-r", str(raw), "-o", str(log), str(variant)], cwd=circuit.parent)
        require(run.returncode == 0 and raw.is_file(), f"ngspice raw run failed for {circuit.name} {corner}")
        return parse_raw(raw.read_bytes())


def pyplot():
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError as error:
        raise ValueError("matplotlib is required for plots: install it in the project's Python environment") from error
    return plt


def sim_plots(directory, outdir):
    """sim/plots.tsv: id, circuit, corners, vectors (comma list), x, title, traces."""
    directory, outdir = Path(directory).resolve(), Path(outdir)
    rows = table(directory / "plots.tsv", ("id", "circuit", "corners", "vectors", "x", "title", "traces"))
    require(len({r["id"] for r in rows}) == len(rows), "duplicate plot ids")
    plt = pyplot()
    outdir.mkdir(parents=True, exist_ok=True)
    written = []
    for row in rows:
        circuit = inside(directory, row["circuit"])
        wanted = [v.strip() for v in row["vectors"].split(",") if v.strip()]
        fig, axes = plt.subplots(len(wanted), 1, figsize=(8, 2.6 * len(wanted)), sharex=True, squeeze=False)
        for corner in corner_cases(row["corners"]):
            names, columns = run_raw(circuit, corner)
            lookup = {n.lower(): c for n, c in zip(names, columns)}
            x = lookup.get(row["x"].lower()) or columns[0]
            x = [v.real if isinstance(v, complex) else v for v in x]
            label = ", ".join(f"{k}={v}" for k, v in corner.items()) or "nominal"
            for axis, vector in zip(axes[:, 0], wanted):
                require(vector.lower() in lookup, f"vector {vector} not in rawfile; available: {names}")
                values = lookup[vector.lower()]
                if any(isinstance(v, complex) for v in values):  # AC sweep: magnitude in dB on a log frequency axis
                    axis.semilogx(x, [20 * math.log10(max(abs(v), 1e-30)) for v in values], label=label, linewidth=1)
                    axis.set_ylabel(f"|{vector}| (dB)")
                else:
                    axis.plot(x, values, label=label, linewidth=1)
                    axis.set_ylabel(vector)
                axis.grid(True, which="both", alpha=.3)
        axes[-1, 0].set_xlabel(row["x"])
        axes[0, 0].set_title(row["title"])
        axes[0, 0].legend(fontsize=7, loc="best")
        target = outdir / f"{row['id']}.png"
        fig.tight_layout()
        fig.savefig(target, dpi=120)
        plt.close(fig)
        written.append(target.name)
        DETAILS.append(f"{row['id']}: {target} corners={row['corners']} vectors={row['vectors']}")
    return f"PLOTS: {len(written)} -> {outdir}", True


def margin_plot(records, outdir, name="margins"):
    """records: list of dict(id, margin, units, status). Horizontal bar chart, red for failures."""
    plt = pyplot()
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    records = [r for r in records if r.get("margin") is not None]
    if not records:
        return None
    fig, axis = plt.subplots(figsize=(8, .35 * len(records) + 1.2))
    labels = [f"{r['id']} [{r.get('units', '')}]" for r in records]
    values = [float(r["margin"]) for r in records]
    colors = ["#2a9d8f" if r.get("status", "pass") == "pass" else "#e63946" for r in records]
    axis.barh(labels, values, color=colors)
    axis.axvline(0, color="black", linewidth=.8)
    axis.set_xlabel("margin (positive = inside limit)")
    axis.set_title("Assertion margins")
    fig.tight_layout()
    target = outdir / f"{name}.png"
    fig.savefig(target, dpi=120)
    plt.close(fig)
    return target


def margins_from_transcripts(project):
    """Collect 'ID {...}: value units margin=x PASS|FAIL' lines from evidence transcripts."""
    records = []
    for log in sorted(Path(project, "evidence").glob("*.log")):
        for line in log.read_text(encoding="utf-8", errors="replace").splitlines():
            match = re.match(r"^(\S+)(?: (\{.*\}))?: (\S+) (\S+) margin=(\S+) (PASS|FAIL)$", line)
            if match:
                corner = json.loads(match[2]) if match[2] else {}
                tag = match[1] + ("@" + ",".join(f"{k}={v}" for k, v in corner.items()) if corner else "")
                records.append(dict(id=tag, value=match[3], units=match[4], margin=float(match[5]), status=match[6].lower()))
            match = re.match(r"^(\S+): margin=(\S+) (\S+)$", line)
            if match:
                records.append(dict(id=match[1], margin=float(match[2]), units=match[3], status="pass" if float(match[2]) >= 0 else "fail"))
    return records
