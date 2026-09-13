#!/usr/bin/env python3
"""Anvil's scoring and release seam. Python standard library only.

Metrics describe an observation; only `gate` authorizes a scoped readiness claim.
Malformed, absent, stale, or unexecuted evidence never becomes a passing observation.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
import hashlib
import io
import importlib.util
import itertools
import json
import math
import os
from pathlib import Path
import re
import shlex
import shutil
import struct
import subprocess
import sys
import tempfile

DIMENSIONS = dict(electrical=.30, simulation=.25, layout=.20, manufacturing=.15,
                  testability=.10, documentation=.10, mechanical=.20, integration=.15,
                  system=.15, firmware=.15, security=.15, compliance=.15, commercial=.10)
METHODS = {"test", "simulation", "analysis", "inspection"}
STATUSES = {"pass", "fail", "not_run", "blocked", "error", "na", "skip"}
GATES = [f"G{i}" for i in range(8)] + ["Sustaining"]
READS: set[Path] = set()
OUTPUTS: set[Path] = set()
DETAILS: list[str] = []


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read(path):
    path = Path(path).resolve()
    require(path.is_file(), f"missing file: {path}")
    READS.add(path)
    return path.read_text(encoding="utf-8-sig")


def read_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, f"duplicate JSON key {key}: {path}")
            result[key] = value
        return result
    return json.loads(read(path), object_pairs_hook=unique,
                      parse_constant=lambda s: require(False, f"non-finite JSON: {s}"))


def table(path, required=(), delimiter=None, allow_empty=False):
    content = read(path)
    lines = [line for line in content.splitlines() if line.strip() and not line.lstrip().startswith("#")]
    parser = csv.DictReader(io.StringIO("\n".join(lines)), delimiter=delimiter or ("," if Path(path).suffix == ".csv" else "\t"), strict=True)
    fields = parser.fieldnames or []
    require(fields and len(set(fields)) == len(fields), f"missing/duplicate headers: {path}")
    require(set(required) <= set(fields), f"{path}: required columns {', '.join(required)}")
    rows = list(parser)
    require(rows or allow_empty, f"empty table: {path}")
    for row in rows:
        require(None not in row and None not in row.values(), f"wrong column count: {path}")
        for key in row:
            row[key] = row[key].strip()
    return rows


def number(value, *, minimum=None, positive=False, integer=False):
    require(not isinstance(value, bool) and value is not None, f"invalid number: {value!r}")
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise ValueError(f"invalid number: {value!r}") from None
    require(result.is_finite(), f"non-finite number: {value!r}")
    require(minimum is None or result >= minimum, f"number below {minimum}: {value}")
    require(not positive or result > 0, f"number must be positive: {value}")
    require(not integer or result == result.to_integral_value(), f"integer required: {value}")
    return result


def index(rows, key):
    result = {}
    for row in rows:
        require(row[key] and row[key] not in result, f"empty/duplicate {key}: {row[key]}")
        result[row[key]] = row
    return result


def traces(value):
    ids = re.split(r"[;,\s]+", value.strip()) if value.strip() not in {"", "-"} else []
    require(all(re.fullmatch(r"HR-\d+", key) for key in ids), f"invalid traces: {value}")
    require(len(set(ids)) == len(ids), f"duplicate trace: {value}")
    return set(ids)


def results(path):
    rows = table(path, ("n", "dimension", "assertion", "status", "weight", "evidence", "traces"))
    index(rows, "assertion")
    index(rows, "n")
    for row in rows:
        number(row["n"], minimum=0, integer=True)
        require(row["dimension"] in DIMENSIONS, f"unknown dimension: {row['dimension']}")
        require(row["status"] in STATUSES, f"unknown status: {row['status']}")
        number(row["weight"], positive=True)
        traces(row["traces"])
    return rows


def requirements(path, allow_empty=False):
    if Path(path).suffix == ".tsv":
        rows = table(path, ("id", "statement", "units", "conditions", "method", "gate", "owner"), allow_empty=allow_empty)
        index(rows, "id")
        for row in rows:
            require(re.fullmatch(r"HR-\d+", row["id"]), f"invalid requirement ID: {row['id']}")
            require(row["method"] in METHODS and row["gate"] in GATES, f"invalid method/gate: {row['id']}")
            require(all(row[k] for k in ("statement", "units", "conditions", "owner")), f"incomplete requirement: {row['id']}")
        return {r["id"]: r for r in rows}
    # Legacy Markdown: count definitions only, never comments or incidental mentions.
    content = re.sub(r"<!--.*?-->", "", read(path), flags=re.S)
    ids = re.findall(r"^\s*(?:#{1,6}\s+|\|\s*)?(HR-\d+)(?=\s|\|)[^\n]*", content, re.M)
    require(ids and len(ids) == len(set(ids)), "missing/duplicate requirement definitions")
    return {key: {} for key in ids}


def pass_rate(path):
    rows = results(path)
    totals, passes = {}, {}
    for row in rows:
        if row["status"] == "na":
            continue  # Diagnostic only; gate checks reviewed NA evidence separately.
        dim, weight = row["dimension"], number(row["weight"])
        totals[dim] = totals.get(dim, 0) + weight
        passes[dim] = passes.get(dim, 0) + (weight if row["status"] == "pass" else 0)
    require(totals, "no scored assertions")
    weights = {d: number(os.getenv("ANVIL_W_" + d.upper(), DIMENSIONS[d]), positive=True) for d in totals}
    rate = sum(passes[d] / totals[d] * weights[d] for d in totals) / sum(weights.values())
    if any(r["dimension"] == "electrical" and r["status"] not in {"pass", "na"} for r in rows):
        cap = number(os.getenv("ELECTRICAL_GATE_CAP", ".5"), minimum=0)
        require(cap <= 1, "gate cap must be <= 1")
        rate = min(rate, cap)
    return f"PASS_RATE: {rate:.2f}", all(r["status"] in {"pass", "na"} for r in rows)


def coverage(path, hrs):
    rows, reqs = results(path), requirements(hrs)
    linked = set().union(*(traces(r["traces"]) for r in rows))
    require(linked <= reqs.keys(), f"orphan traces: {sorted(linked - reqs.keys())}")
    # Display must not round incomplete coverage to 1.00. Release uses exact sets.
    ratio = math.floor(len(linked) / len(reqs) * 100) / 100
    if len(reqs) <= 100:
        ratio = round(len(linked) / len(reqs), 2)
    return f"REQ_COVERAGE: {ratio:.2f}", linked == reqs.keys()


def executable(name):
    override = os.getenv(name.upper().replace("-", "_"))
    found = override or shutil.which(name)
    if not found and name == "kicad-cli":
        candidates = []
        for base in [Path(os.getenv("ProgramFiles", "C:/Program Files")) / "KiCad",
                     Path(os.getenv("LOCALAPPDATA", "C:/missing")) / "Programs/KiCad"]:
            if base.is_dir():
                candidates += list(base.glob("*/bin/kicad-cli.exe"))
        found = str(sorted(candidates, key=lambda p: tuple(int(x) for x in re.findall(r"\d+", p.parent.parent.name)))[-1]) if candidates else None
    require(found and (Path(found).is_file() or shutil.which(found)), f"tool unavailable: {name}")
    return found


def execute(command, cwd=None):
    result = subprocess.run(command, cwd=cwd, text=True, encoding="utf-8", errors="replace",
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=300)
    DETAILS.append(f"COMMAND: {json.dumps([str(x) for x in command])}\nEXIT: {result.returncode}\n{result.stdout}")
    return result


def kicad(kind, source, output=None):
    source = Path(source).resolve()
    read(source)
    if kind == "drc":
        for suffix in (".kicad_pro", ".kicad_dru", ".kicad_sch"):
            read(source.with_suffix(suffix))
    output = Path(output or source.with_suffix(f".{kind}.json")).resolve()
    require(output != source, "report cannot overwrite input")
    require(output.suffix == ".json", "KiCad report output must be a JSON file")
    output.parent.mkdir(parents=True, exist_ok=True)
    command = [executable("kicad-cli"), "sch" if kind == "erc" else "pcb", kind,
               "--format", "json", "--severity-all", "--exit-code-violations"]
    if kind == "drc":
        command += ["--schematic-parity"]
    # Fresh isolated report: a failed run cannot consume an earlier report.
    with tempfile.TemporaryDirectory(prefix="anvil-", dir=output.parent) as temp:
        candidate = Path(temp) / "report.json"
        run = execute(command + ["-o", str(candidate), str(source)], cwd=source.parent)
        require(run.returncode in {0, 5}, f"KiCad {kind} execution failed ({run.returncode})")
        data = read_json(candidate)
        require(isinstance(data, dict) and isinstance(data.get("kicad_version"), str), "invalid KiCad report schema/version")
        if kind == "erc":
            sheets = data.get("sheets")
            require(isinstance(sheets, list) and sheets, "ERC report missing sheets")
            groups = []
            for sheet in sheets:
                require(isinstance(sheet, dict) and isinstance(sheet.get("violations"), list), "invalid ERC sheet")
                groups.append(sheet["violations"])
        else:
            keys = ("violations", "unconnected_items", "schematic_parity")
            require(all(isinstance(data.get(k), list) for k in keys), "DRC report missing violation groups")
            groups = [data[k] for k in keys]
        count = 0
        for violation in itertools.chain.from_iterable(groups):
            require(isinstance(violation, dict) and violation.get("severity") in {"error", "warning", "exclusion"}
                    and violation.get("type") and violation.get("description"), "invalid violation record")
            # Exclusions also need a disposition; no silent blanket suppression.
            count += 1
        require(not (run.returncode == 5 and count == 0), "KiCad exit/report contradiction")
        os.replace(candidate, output)
        READS.discard(candidate.resolve())
        READS.add(output)
        OUTPUTS.add(output)
    return f"{kind.upper()}_VIOLATIONS: {count}", count == 0


def compare(value, op, limit):
    value = number(value)
    if op == "within":
        match = re.fullmatch(r"(.+?)(?:±|\+/-)([^%]+)(%)?", limit)
        require(match, f"invalid within limit: {limit}")
        center = number(match[1])
        delta = number(match[2], minimum=0)
        if match[3]:
            delta = abs(center) * delta / 100
        margin = min(value - (center - delta), center + delta - value)
        return margin >= 0, margin
    bound = number(limit)
    require(op in {"le", "lt", "ge", "gt", "eq"}, f"unknown comparison: {op}")
    margin = bound - value if op in {"le", "lt"} else value - bound
    if op == "eq":
        return value == bound, -abs(value - bound)
    return (margin > 0 if op in {"lt", "gt"} else margin >= 0), margin


def corner_cases(spec):
    if spec in {"nominal", "-", ""}:
        return [{}]
    params = {}
    for item in spec.split(";"):
        require(item.count("=") == 1, f"invalid corner: {item}")
        key, values = item.split("=")
        require(re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key) and key.lower() not in params, f"invalid/duplicate parameter: {key}")
        params[key.lower()] = [str(number(v)) for v in values.split(",")]
        require(len(set(params[key.lower()])) == len(params[key.lower()]), f"duplicate corner value: {key}")
    require(math.prod(map(len, params.values())) <= 256, "corner matrix exceeds 256 runs; split the harness")
    return [dict(zip(params, values)) for values in itertools.product(*params.values())]


def sim(directory):
    require(not os.getenv("SKIP_NGSPICE"), "SKIP_NGSPICE was removed: cached logs cannot verify a simulation")
    directory = Path(directory).resolve()
    rows = table(directory / "assertions.tsv", ("id", "measure", "op", "limit", "units", "corners", "traces", "circuit"))
    index(rows, "id")
    tool, passed = executable("ngspice"), 0
    for row in rows:
        require(re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", row["measure"]), "invalid measurement name")
        require(row["units"], "measurement units required (use '-' for dimensionless)")
        traces(row["traces"])
        circuit = inside(directory, row["circuit"])
        source = read(circuit)
        # Read the actual dependency graph, including models outside the sim subdirectory.
        def dependencies(path, active=()):
            require(path not in active, f"cyclic SPICE include: {path}")
            require(len(active) < 32, "SPICE include nesting exceeds 32 levels")
            content = read(path)
            for line in content.splitlines()[1 if path == circuit else 0:]:
                text_line = line.strip()
                require(not re.match(r"(?i)^\.control\b", text_line), "batch assertions require .measure without .control; use a separately reviewed runner for interactive scripts")
                if re.match(r"(?i)^\.(?:include|inc|lib)\b", text_line):
                    parts = shlex.split(text_line, comments=True)
                    if parts[0].lower() == ".lib" and len(parts) == 2 and not any(c in parts[1] for c in (".", "/", "\\")):
                        continue  # Named section declaration inside a library.
                    require(len(parts) >= 2, "SPICE include has no filename")
                    candidates = {(path.parent / parts[1]).resolve(), (circuit.parent / parts[1]).resolve()}
                    existing = [p for p in candidates if p.is_file()]
                    require(existing, f"missing SPICE dependency: {parts[1]}")
                    for dependency in existing:
                        dependencies(dependency, active + (path,))
        dependencies(circuit)
        ok = True
        for corner in corner_cases(row["corners"]):
            text_source = source
            for key, value in corner.items():
                pattern = rf"(?im)^(\.param\s+{re.escape(key)}\s*=\s*)[^\s;]+\s*(?:;[^\n]*)?$"
                text_source, replaced = re.subn(pattern, lambda m: m[1] + value, text_source)
                require(replaced == 1, f"{circuit}: declare corner {key} on its own .param line exactly once")
            # In the source directory to preserve SPICE .include semantics.
            with tempfile.TemporaryDirectory(prefix=".anvil-sim-", dir=circuit.parent) as temp:
                variant = Path(temp) / "corner.cir"
                log = Path(temp) / "run.log"
                variant.write_text(text_source, encoding="utf-8")
                run = execute([tool, "-n", "-b", "-o", str(log), str(variant)], cwd=circuit.parent)
                require(run.returncode == 0, f"ngspice failed: {row['id']} {corner}")
                content = log.read_text(encoding="utf-8", errors="replace") if log.is_file() else ""
                DETAILS.append(content)
                require(not re.search(r"(?im)^\s*(?:fatal error|error)(?:\s*:|\s+on line)", content), f"ngspice logged an error: {row['id']} {corner}")
                matches = re.findall(rf"(?im)^\s*{re.escape(row['measure'])}\s*=\s*(\S+)", content)
                require(len(matches) == 1, f"missing/ambiguous measure {row['measure']} in its own run")
                success, margin = compare(matches[0], row["op"], row["limit"])
                DETAILS.append(f"{row['id']} {json.dumps(corner, sort_keys=True)}: {matches[0]} {row['units']} margin={margin} {'PASS' if success else 'FAIL'}")
                ok &= success
        passed += ok
    return f"SIM_PASS: {passed}/{len(rows)}", passed == len(rows)


def currency(value):
    require(re.fullmatch(r"[A-Z]{3}", value), f"invalid currency: {value}")
    return value


def bom_cost(bom, catalog):
    rows = table(bom, ("MPN", "Qty"))
    parts = index(table(catalog, ("mpn", "unit_price", "currency")), "mpn")
    total, currencies, included = Decimal(0), set(), 0
    for row in rows:
        qty = number(row["Qty"], positive=True, integer=True)
        if row["MPN"].upper() == "DNP" or row.get("DNP", "").lower() in {"yes", "true", "1"}:
            continue
        require(row["MPN"] in parts, f"MPN missing from catalog: {row['MPN']}")
        part = parts[row["MPN"]]
        price = number(part["unit_price"], minimum=0)
        currencies.add(currency(part["currency"]))
        total += qty * price
        included += 1
    require(included and len(currencies) == 1, "BOM must contain priced parts in one currency; explicit FX conversion required")
    return f"BOM_COST: {total:.2f} {next(iter(currencies))}", True


def product_bom(path):
    path = Path(path).resolve()
    rows = table(path, ("item_id", "category", "qty", "unit_price", "currency", "mass_g", "source"))
    index(rows, "item_id")
    cost, mass, currencies = Decimal(0), Decimal(0), set()
    for row in rows:
        require(row["category"] in {"pcb", "cots", "mech", "fastener", "wire", "consumable", "spare"}, "unknown product category")
        qty = number(row["qty"], positive=True)
        price, grams = number(row["unit_price"], minimum=0), number(row["mass_g"], minimum=0)
        currencies.add(currency(row["currency"]))
        require(row["source"].count("#") == 1, "source must be a pinned CSV path#item_id")
        filename, key = row["source"].split("#")
        pinned = index(table(path.parent / filename, ("item_id", "unit_price", "currency", "mass_g")), "item_id")
        require(key in pinned, f"missing pinned source row: {row['source']}")
        item = pinned[key]
        require(price == number(item["unit_price"], minimum=0) and grams == number(item["mass_g"], minimum=0)
                and row["currency"] == item["currency"], f"source/rollup mismatch: {row['item_id']}")
        cost += price * qty
        mass += grams * qty
    require(len(currencies) == 1, "mixed product BOM currencies; explicit FX conversion required")
    DETAILS.append(f"PRODUCT_MASS_G: {mass:.1f}")
    return f"PRODUCT_COST: {cost:.2f} {next(iter(currencies))}", True


def budget(path):
    rows = table(path, ("quantity", "worst_demand", "capability", "derate", "units", "traces"))
    for row in rows:
        row["id"] = row.get("id", row.get("budget_id", ""))
    index(rows, "id")
    passed = 0
    for row in rows:
        demand = number(row["worst_demand"], minimum=0)
        capacity = number(row["capability"], positive=True)
        derate = number(row["derate"], positive=True)
        require(derate <= 1, f"derate must be a fraction <= 1: {row['id']}")
        require(row["quantity"] and row["units"], "budget quantity/units required")
        traces(row["traces"])
        for key, value in (("demand_source", demand), ("capability_source", capacity)):
            if key in row:
                require(row[key].count("#") == 1, f"{key} must be a JSON file#key reference")
                filename, pointer = row[key].split("#")
                source = read_json(Path(path).parent / filename)
                for part in pointer.split("."):
                    require(isinstance(source, dict) and part in source, f"missing budget source key: {pointer}")
                    source = source[part]
                require(isinstance(source, dict) and source.get("units") == row["units"] and number(source.get("value")) == value,
                        f"budget value/units disagree with {key}: {row['id']}")
        passed += demand <= capacity * derate
        DETAILS.append(f"{row['id']}: margin={capacity * derate - demand} {row['units']}")
    return f"SYS_BUDGET: {passed}/{len(rows)}", passed == len(rows)


def pinout(harness, icd, mates=None):
    wires = table(harness, ("wire_id", "icd_id", "from", "to", "awg", "current_a", "length_mm", "voltage_v", "protocol"))
    interfaces = index(table(icd, ("icd_id", "from", "to", "kind", "i_max_a", "ampacity_a", "awg", "voltage_v", "protocol", "rating_source")), "icd_id")
    index(wires, "wire_id")
    errors, used, endpoints = 0, set(), set()
    for wire in wires:
        require(wire["icd_id"] in interfaces, f"unknown ICD: {wire['icd_id']}")
        spec = interfaces[wire["icd_id"]]
        require(spec["kind"] in {"power", "signal"}, "harness references non-electrical ICD")
        require(all(re.fullmatch(r"[^.\s]+\.[^.\s]+\.[^.\s]+", wire[k]) for k in ("from", "to")), "endpoint must be module.connector.pin")
        current = number(wire["current_a"], minimum=0)
        number(wire["length_mm"], positive=True)
        awg = number(wire["awg"], minimum=0, integer=True)
        require(awg <= 40, "unsupported AWG")
        rated = number(spec["ampacity_a"], positive=True)
        require(spec["rating_source"], "source for connector/wire rating required")
        read(Path(icd).parent / spec["rating_source"])
        errors += (wire["from"], wire["to"]) != (spec["from"], spec["to"])
        errors += current > number(spec["i_max_a"], minimum=0) or current > rated
        errors += awg != number(spec["awg"], minimum=0, integer=True)
        errors += number(wire["voltage_v"]) != number(spec["voltage_v"])
        errors += not wire["protocol"] or wire["protocol"] != spec["protocol"]
        for end in (wire["from"], wire["to"]):
            errors += end in endpoints
            endpoints.add(end)
        used.add(wire["icd_id"])
    errors += len({k for k, r in interfaces.items() if r["kind"] in {"power", "signal"}} - used)
    if mates is not None:
        rows = table(mates, ("mate_id", "side_a", "side_b", "pins", "pin_ids_a", "pin_ids_b"))
        index(rows, "mate_id")
        seen = {}
        for row in rows:
            count = int(number(row["pins"], positive=True, integer=True))
            pair = (row["side_a"], row["side_b"])
            require(pair not in seen, "duplicate mate")
            sides = [row[key].split(",") for key in ("pin_ids_a", "pin_ids_b")]
            require(all(len(pins) == count and len(set(pins)) == count and all(pins) for pins in sides), "mate pin identifiers must match the declared count")
            seen[pair] = sides
        for wire in wires:
            pair = tuple(wire[k].rsplit(".", 1)[0] for k in ("from", "to"))
            errors += pair not in seen
            if pair in seen:
                errors += any(wire[key].rsplit(".", 1)[1] not in pins for key, pins in zip(("from", "to"), seen[pair]))
    return f"PINOUT_VIOLATIONS: {errors}", errors == 0


def firmware(path):
    path = Path(path).resolve()
    data = read_json(path)
    require(isinstance(data, dict) and data.get("schema_version") == 1, "firmware manifest schema_version must be 1")
    for key in ("source_revision", "toolchain", "support_until", "production_debug_policy", "calibration_schema"):
        require(isinstance(data.get(key), str) and data[key].strip(), f"firmware {key} required")
    require(re.fullmatch(r"[a-fA-F0-9]{40}|[a-fA-F0-9]{64}", data["source_revision"]), "firmware source_revision must be a full commit ID")
    require(isinstance(data.get("build_command"), list) and data["build_command"] and all(isinstance(s, str) and s for s in data["build_command"]), "firmware build_command array required")
    for key in ("supported_hardware", "bootloader_versions"):
        require(isinstance(data.get(key), list) and data[key] and all(isinstance(s, str) and s for s in data[key]), f"firmware {key} required")
    for key in ("dependency_lock", "binary", "sbom", "known_issues", "recovery_test", "build_record"):
        dep = inside(path.parent, data.get(key))
        READS.add(dep)
    require(re.fullmatch(r"[a-f0-9]{64}", str(data.get("binary_sha256"))) and digest(inside(path.parent, data["binary"])) == data["binary_sha256"], "firmware binary hash mismatch")
    build = read_json(inside(path.parent, data["build_record"]))
    require(build.get("exit_code") == 0 and build.get("source_revision") == data["source_revision"]
            and build.get("binary_sha256") == data["binary_sha256"] and build.get("command") == data["build_command"]
            and build.get("toolchain") == data["toolchain"], "firmware build record does not match release")
    require(build.get("dependency_sha256") == digest(inside(path.parent, data["dependency_lock"])), "firmware dependency lock changed since build")
    timestamp(build.get("created_at"))
    READS.add(inside(path.parent, build.get("transcript")))
    return "FIRMWARE_RECORD: VALID", True


def factory(directory):
    directory = Path(directory).resolve()
    policy = read_json(directory / "acceptance.json")
    target = number(policy.get("first_pass_yield"), minimum=0)
    require(target <= 1, "first_pass_yield must be a fraction <= 1")
    minimum = number(policy.get("minimum_units"), positive=True, integer=True)
    require(policy.get("hardware_revision") and (policy.get("firmware_sha256") == "none" or re.fullmatch(r"[a-f0-9]{64}", str(policy.get("firmware_sha256")))), "factory acceptance must identify hardware/firmware")
    fixtures = policy.get("fixtures")
    require(isinstance(fixtures, dict) and fixtures, "approved fixture revisions required")
    rows = table(directory / "unit-records.csv", ("serial", "lot", "hardware_revision", "firmware_sha256", "fixture_id", "fixture_revision", "calibration_due", "operator", "timestamp", "attempt", "rework_reference", "result", "measurement_record", "provisioning_record"))
    units = {}
    for row in rows:
        require(all(row[k] for k in ("serial", "lot", "operator", "measurement_record", "provisioning_record")), "incomplete unit traceability")
        require(row["hardware_revision"] == policy["hardware_revision"] and row["firmware_sha256"] == policy["firmware_sha256"], "unit configuration does not match pilot acceptance")
        require(fixtures.get(row["fixture_id"]) == row["fixture_revision"], "unapproved fixture revision")
        instant = timestamp(row["timestamp"])
        due = datetime.fromisoformat(row["calibration_due"].replace("Z", "+00:00"))
        require(due.tzinfo and due >= instant, "fixture calibration was expired at test time")
        attempt = int(number(row["attempt"], positive=True, integer=True))
        require(row["result"] in {"pass", "fail"}, "unit result must be pass or fail")
        attempts = units.setdefault(row["serial"], {})
        require(attempt not in attempts, "duplicate unit test attempt")
        attempts[attempt] = row
        if attempt > 1:
            require(row["rework_reference"], "retest/rework needs a disposition record")
            read(inside(directory, row["rework_reference"]))
        for key in ("measurement_record", "provisioning_record"):
            read(inside(directory, row[key]))
    for attempts in units.values():
        require(set(attempts) == set(range(1, max(attempts)+1)), "missing first test or intermediate attempt")
        require([timestamp(attempts[i]["timestamp"]) for i in sorted(attempts)] == sorted(timestamp(r["timestamp"]) for r in attempts.values()), "unit attempts out of time order")
    first = sum(attempts[1]["result"] == "pass" for attempts in units.values())
    final = sum(attempts[max(attempts)]["result"] == "pass" for attempts in units.values())
    ok = len(units) >= minimum and Decimal(first)/len(units) >= target and final == len(units)
    return f"FACTORY_YIELD: {first}/{len(units)} first-pass; {final}/{len(units)} final", ok


def commercial(path):
    rows = table(path, ("category", "description", "quantity", "unit_cost", "currency", "source", "assumption"))
    categories = {"components", "assembly", "test", "yield_loss", "packaging", "freight", "duties", "certification", "development", "warranty", "returns", "support", "channel", "overhead"}
    require(categories <= {r["category"] for r in rows}, f"missing cost categories: {sorted(categories - {r['category'] for r in rows})}")
    total, currencies = Decimal(0), set()
    for row in rows:
        require(row["description"] and row["assumption"] and row["source"], "cost lines need description, source and basis/zero-cost rationale")
        read(Path(path).parent / row["source"])
        total += number(row["quantity"], minimum=0) * number(row["unit_cost"], minimum=0)
        currencies.add(currency(row["currency"]))
    require(len(currencies) == 1, "cost model currencies differ; supply an explicit pinned conversion")
    return f"PRODUCT_ECONOMICS: {total:.2f} {next(iter(currencies))}", True


def mechanical(kind, directory):
    directory = Path(directory)
    data = read_json(directory / "measures.json")
    require(isinstance(data, dict) and data, "mechanical measures must be a nonempty object")
    def flatten(obj, prefix=""):
        values = {}
        for key, value in obj.items():
            name = prefix + key
            if isinstance(value, dict):
                values.update(flatten(value, name + "."))
            else:
                values[name] = number(value)
        return values
    values = flatten(data)
    rows = table(directory / "assertions.tsv", ("id", "class", "measure", "op", "limit", "units", "traces"))
    index(rows, "id")
    require(all(r["class"] in {"fit", "mass", "dfm"} for r in rows), "unknown mechanical assertion class")
    selected = [r for r in rows if r["class"] == kind]
    require(selected, f"no {kind} assertions")
    passed = 0
    for row in selected:
        require(row["measure"] in values, f"missing measure: {row['measure']}")
        traces(row["traces"])
        require(row["units"], "units required")
        if kind == "mass":
            require(values[row["measure"]] >= 0, "negative measured mass")
        good, margin = compare(values[row["measure"]], row["op"], row["limit"])
        passed += good
        DETAILS.append(f"{row['id']}: margin={margin} {row['units']}")
    return f"{kind.upper()}_PASS: {passed}/{len(selected)}", passed == len(selected)


def mesh(path):
    path = Path(path).resolve()
    READS.add(path)
    data = path.read_bytes()
    triangles = []
    if len(data) >= 84 and len(data) == 84 + struct.unpack_from("<I", data, 80)[0] * 50:
        for offset in range(84, len(data), 50):
            values = struct.unpack_from("<12fH", data, offset)
            triangles.append([tuple(values[i:i+3]) for i in (3, 6, 9)])
    else:
        content = data.decode("ascii")
        require(re.match(r"\s*solid\b", content) and "endsolid" in content, "invalid STL")
        for facet in re.findall(r"facet\b(.*?)endfacet", content, re.S):
            vertices = re.findall(r"vertex\s+(\S+)\s+(\S+)\s+(\S+)", facet)
            require(len(vertices) == 3, "STL facet must have three vertices")
            triangles.append([tuple(float(number(v)) for v in vertex) for vertex in vertices])
    require(triangles, "empty STL")
    edges, defects = {}, 0
    for a, b, c in triangles:
        require(all(math.isfinite(v) for point in (a, b, c) for v in point), "non-finite STL vertex")
        u, v = [b[i]-a[i] for i in range(3)], [c[i]-a[i] for i in range(3)]
        cross = [u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0]]
        require(all(math.isfinite(x) for x in cross), "STL coordinates overflow geometry calculation")
        defects += math.hypot(*cross) <= 1e-12
        for p, q in ((a, b), (b, c), (c, a)):
            key = tuple(sorted((p, q)))
            edges.setdefault(key, []).append((p, q))
    for uses in edges.values():
        defects += len(uses) != 2 or uses[0] == uses[-1]
    # ponytail: topology/degeneracy only; use a CAD kernel for self-intersection and solid validity.
    return f"MESH_DEFECTS: {defects}", defects == 0


def sexpr(content):
    tokens = re.findall(r'\(|\)|"(?:\\.|[^"\\])*"|[^\s()]+', content)
    stack, roots = [], []
    for token in tokens:
        if token == "(":
            node = []
            (stack[-1] if stack else roots).append(node)
            stack.append(node)
        elif token == ")":
            require(stack, "unbalanced KiCad document")
            stack.pop()
        else:
            require(stack, "text outside KiCad expression")
            stack[-1].append(token.strip('"'))
    require(not stack and len(roots) == 1, "unbalanced KiCad document")
    return roots[0]


def area(path):
    root = sexpr(read(path))
    require(root[0] == "kicad_pcb", "not a KiCad PCB")
    points = []
    def point(node):
        require(len(node) == 3, "invalid outline coordinate")
        coords = tuple(float(number(x)) for x in node[1:])
        require(all(math.isfinite(x) for x in coords), "outline coordinates exceed supported range")
        return coords
    for node in root[1:]:
        if not isinstance(node, list) or not node:
            continue
        if node[0] == "footprint":
            require(not any(isinstance(x, list) and ["layer", "Edge.Cuts"] in x for x in node), "footprint Edge.Cuts must be moved to board coordinates before area scoring")
        if ["layer", "Edge.Cuts"] not in node:
            continue
        children = {x[0]: x for x in node[1:] if isinstance(x, list) and x}
        kind = node[0]
        require(kind in {"gr_line", "gr_rect", "gr_circle", "gr_arc", "gr_poly"}, f"unsupported outline primitive: {kind}")
        if kind == "gr_poly":
            points.extend(point(x) for x in children["pts"][1:])
            continue
        start, end = point(children.get("start", children.get("center", []))), point(children["end"])
        points.extend((start, end))
        if kind == "gr_circle":
            radius = math.dist(start, end)
            require(radius > 0, "zero-radius outline circle")
            points.extend((start[0]+dx*radius, start[1]+dy*radius) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        elif kind == "gr_arc":
            mid = point(children["mid"])
            ax, ay = start; bx, by = mid; cx, cy = end
            d = 2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
            require(math.isfinite(d) and abs(d) > 1e-12, "collinear or out-of-range outline arc")
            center = ((sum((x*x+y*y)*z for x,y,z in ((ax,ay,by-cy),(bx,by,cy-ay),(cx,cy,ay-by))))/d,
                      (sum((x*x+y*y)*z for x,y,z in ((ax,ay,cx-bx),(bx,by,ax-cx),(cx,cy,bx-ax))))/d)
            require(all(math.isfinite(x) for x in center), "arc calculation exceeds supported range")
            angles = [math.atan2(p[1]-center[1], p[0]-center[0]) % math.tau for p in (start, mid, end)]
            span = (angles[2]-angles[0]) % math.tau
            ccw = (angles[1]-angles[0]) % math.tau <= span
            radius = math.dist(start, center)
            for angle in (0, math.pi/2, math.pi, 3*math.pi/2):
                on_arc = (angle-angles[0]) % math.tau <= span + 1e-12
                if on_arc == ccw:
                    points.append((center[0]+radius*math.cos(angle), center[1]+radius*math.sin(angle)))
    require(points, "no supported Edge.Cuts geometry")
    width = max(p[0] for p in points) - min(p[0] for p in points)
    height = max(p[1] for p in points) - min(p[1] for p in points)
    require(width > 0 and height > 0 and math.isfinite(width*height), "zero-area or out-of-range outline")
    return f"AREA_MM2: {width*height:.1f}", True


def inside(root, relative):
    require(isinstance(relative, str) and relative and not Path(relative).is_absolute(), f"relative artifact path required: {relative}")
    require("\\" not in relative and not re.match(r"^[A-Za-z]:", relative), "use portable project-relative paths with forward slashes")
    path = (Path(root) / relative).resolve()
    require(path.is_relative_to(Path(root).resolve()), f"artifact escapes project: {relative}")
    require(path.is_file(), f"missing artifact: {relative}")
    return path


def metric(command, arguments):
    functions = {"pass-rate": pass_rate, "coverage": coverage, "sim": sim, "bom-cost": bom_cost,
                 "product-bom": product_bom, "sys-budget": budget, "pinout": pinout, "area": area, "mesh": mesh,
                 "firmware": firmware, "factory": factory, "commercial": commercial}
    if command in {"erc", "drc"}:
        return kicad(command, *arguments)
    if command in {"fit", "mass", "mech-dfm"}:
        return mechanical("dfm" if command == "mech-dfm" else command, *arguments)
    require(command in functions, f"unknown metric: {command}")
    return functions[command](*arguments)


def package_root():
    return Path(__file__).resolve().parent.parent


def template_root():
    return package_root() / "templates" / "anvil-project"


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def json_digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()).hexdigest()


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Atomic replacement keeps interrupted recording from leaving valid-looking partial JSON.
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as stream:
        temp = Path(stream.name)
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write("\n")
    try:
        os.replace(temp, path)
    finally:
        temp.unlink(missing_ok=True)


def write_ledger(path, rows):
    with Path(path).open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["n", "dimension", "assertion", "status", "weight", "evidence", "traces"], delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def project(root):
    root = Path(root).resolve()
    cfg = read_json(root / "anvil-project.json")
    require(isinstance(cfg, dict) and cfg.get("schema_version") == 1, "anvil-project.json schema_version must be 1")
    require(isinstance(cfg.get("name"), str) and cfg["name"].strip(), "project name required")
    require(isinstance(cfg.get("hardware_revision"), str) and cfg["hardware_revision"].strip(), "hardware_revision required")
    require(cfg.get("release_kind") in {"pcb", "assembly", "product"}, "release_kind must be pcb, assembly, or product")
    for field, allowed in {
        "sectors": {"embedded", "connected", "robotics", "industrial", "medical", "automotive"},
        "markets": {"US", "EU", "GB", "NI", "TW"},
        "features": {"electronics", "firmware", "mechanics", "radio", "battery", "cloud", "taiwan_export"},
    }.items():
        values = cfg.get(field)
        require(isinstance(values, list) and len(values) == len(set(values)) and set(values) <= allowed,
                f"invalid/duplicate {field}; allowed: {sorted(allowed)}")
        require(values or field == "features", f"{field} cannot be empty")
    require("electronics" in cfg["features"], "Anvil's release profiles require electronics")
    require(not ({"radio", "cloud"} & set(cfg["features"])) or "connected" in cfg["sectors"], "radio/cloud products must include connected sector")
    require(cfg.get("target_gate") in GATES, "invalid target_gate")
    require(isinstance(cfg.get("artifacts"), dict), "artifacts must map role to relative file paths")
    require(isinstance(cfg.get("checks", {}), dict), "checks must map automatic check IDs to command arrays")
    require(isinstance(cfg.get("requirements"), str) and cfg["requirements"].endswith(".tsv"), "release requirements must be a structured TSV")
    return root, cfg


def profile(cfg):
    # Artifact additions do not invalidate opportunity/requirements reviews; profile changes do.
    return {k: cfg[k] for k in ("name", "hardware_revision", "release_kind", "sectors", "markets", "features", "requirements")}


def applies(selector, cfg):
    # Comma = OR, '&' = AND. Fixed bundled catalog; no executable expressions.
    def term(value):
        if value == "all":
            return True
        field, name = value.split(":", 1)
        if field == "scope":
            return cfg["release_kind"] == name
        return name in cfg[{"feature": "features", "sector": "sectors", "market": "markets"}[field]]
    return any(all(term(t) for t in branch.split("&")) for branch in selector.split(","))


def expected_checks(cfg):
    rows = table(template_root() / "lifecycle-checks.csv", ("id", "gate", "dimension", "applies", "method", "authority", "criterion", "owner"))
    index(rows, "id")
    rows = [r for r in rows if applies(r["applies"], cfg)]
    autos = [("AUTO-ERC", "electrical", "inspection", "erc"), ("AUTO-DRC", "layout", "inspection", "drc")]
    if "simulation" in cfg.get("verification_methods", []):
        autos.append(("AUTO-SIM", "simulation", "simulation", "sim"))
    if cfg["release_kind"] in {"assembly", "product"}:
        autos.append(("AUTO-BOM", "manufacturing", "analysis", "bom-cost"))
    if cfg["release_kind"] == "product":
        autos += [("AUTO-PINOUT", "integration", "inspection", "pinout"),
                  ("AUTO-PRODUCT-BOM", "system", "analysis", "product-bom"),
                  ("AUTO-BUDGET", "system", "analysis", "sys-budget")]
    if "mechanics" in cfg["features"]:
        autos += [("AUTO-FIT", "mechanical", "analysis", "fit"), ("AUTO-MASS", "mechanical", "analysis", "mass"),
                  ("AUTO-DFM", "mechanical", "analysis", "mech-dfm")]
    if "firmware" in cfg["features"]:
        autos.append(("AUTO-FIRMWARE", "firmware", "inspection", "firmware"))
    for key, dim, method, command in autos:
        rows.append(dict(id=key, gate="G3", dimension=dim, method=method, authority="tool", criterion=command, owner="Engineering"))
    rows += [dict(id="AUTO-FACTORY", gate="G6", dimension="manufacturing", method="analysis", authority="tool", criterion="factory", owner="Manufacturing quality"),
             dict(id="AUTO-COST", gate="G7", dimension="commercial", method="analysis", authority="tool", criterion="commercial", owner="Product owner")]
    return rows


def all_checks(root, cfg, allow_empty=False):
    reqs = requirements(inside(root, cfg["requirements"]), allow_empty=allow_empty)
    methods = {r["method"] for r in reqs.values()}
    require(set(cfg.get("verification_methods", [])) <= METHODS, "invalid verification_methods")
    actual = dict(cfg, verification_methods=sorted(methods | set(cfg.get("verification_methods", []))))
    checks = expected_checks(actual)
    for key, req in reqs.items():
        checks.append(dict(id="REQ-" + key, gate=req["gate"], dimension="documentation", method=req["method"],
                           authority="external" if req["method"] == "test" else "review", criterion=req["statement"], owner=req["owner"]))
    return checks, reqs


def snapshot(root, cfg, enforce=True):
    mandatory = {"schematic", "pcb", "project", "rules", "gerbers", "drill"}
    if cfg["release_kind"] in {"assembly", "product"}:
        mandatory |= {"bom", "placement", "catalog", "assembly"}
    if cfg["release_kind"] == "product":
        mandatory |= {"icd", "harness", "product_bom", "budgets"}
    if "mechanics" in cfg["features"]:
        mandatory |= {"cad", "mechanical_export", "mechanical_measures"}
    if "firmware" in cfg["features"]:
        mandatory |= {"firmware_source", "firmware_lock", "firmware_binary", "firmware_manifest"}
    if enforce:
        require(mandatory <= cfg["artifacts"].keys(), f"missing release artifact roles: {sorted(mandatory - cfg['artifacts'].keys())}")
    files = {cfg["requirements"]: digest(inside(root, cfg["requirements"]))}
    for role, paths in cfg["artifacts"].items():
        require(isinstance(role, str) and isinstance(paths, list) and paths and len(paths) == len(set(paths)), f"empty/invalid artifact role: {role}")
        for name in paths:
            path = inside(root, name)
            require(path.stat().st_size > 0, f"empty release artifact: {name}")
            require(path.relative_to(root).as_posix() == name, f"artifact path must be canonical: {name}")
            files[name] = digest(path)
    if enforce:
        boards = [inside(root, name) for name in cfg["artifacts"]["pcb"]]
        for board in boards:
            for role, suffix in (("rules", ".kicad_dru"), ("project", ".kicad_pro"), ("schematic", ".kicad_sch")):
                sibling = board.with_suffix(suffix)
                require(sibling in {inside(root, p) for p in cfg["artifacts"][role]}, f"{role} must be beside and share stem with {board.name}")
        extensions = {"schematic": {".kicad_sch"}, "pcb": {".kicad_pcb"}, "project": {".kicad_pro"},
                      "rules": {".kicad_dru"}, "gerbers": {".gbr", ".gtl", ".gbl", ".gm1"}, "drill": {".drl", ".xln"}}
        for role, allowed in extensions.items():
            require(all(Path(p).suffix.lower() in allowed for p in cfg["artifacts"][role]), f"wrong file type for {role}")
    data = {"schema_version": 1, "profile": profile(cfg), "artifacts": cfg["artifacts"], "files": files}
    return data, json_digest(data)


def timestamp(value):
    require(isinstance(value, str), "ISO timestamp required")
    instant = datetime.fromisoformat(value.replace("Z", "+00:00"))
    require(instant.tzinfo is not None and instant <= datetime.now(timezone.utc), "timestamp needs timezone and cannot be in the future")
    return instant


def receipt_valid(root, cfg, check, path, release_hash):
    data = read_json(inside(root, path))
    require(isinstance(data, dict) and data.get("schema_version") == 1, "receipt schema_version must be 1")
    require(data.get("check_id") == check["id"], "receipt check ID mismatch")
    require(data.get("check_sha256") == json_digest(check), "receipt is stale for the planned criterion/method/gate")
    require(data.get("status") in {"pass", "na"}, "receipt has no passing disposition")
    require(data.get("method") == check["method"], "receipt method does not match the planned verification method")
    require(data.get("profile_sha256") == json_digest(profile(cfg)), "receipt belongs to a different project/profile")
    timestamp(data.get("created_at"))
    if GATES.index(check["gate"]) >= 3:
        require(release_hash and data.get("release_sha256") == release_hash, "receipt is stale for the release configuration")
    files = data.get("files")
    require(isinstance(files, dict) and files, "receipt must bind evidence files")
    for filename, expected in files.items():
        require(re.fullmatch(r"[a-f0-9]{64}", str(expected)), "invalid file digest")
        require(digest(inside(root, filename)) == expected, f"changed receipt input/evidence: {filename}")
    if check["gate"] in {"G1", "G2"}:
        require(cfg["requirements"] in files, "requirements/architecture review must bind the requirements baseline")
    if check["authority"] == "tool":
        require(data.get("producer") == "anvil" and data.get("status") == "pass", "automatic checks require a successful Anvil execution receipt")
        command = cfg.get("checks", {}).get(check["id"])
        require(isinstance(command, list) and len(command) >= 2 and all(isinstance(s, str) and s for s in command)
                and command[0] == check["criterion"], "required automatic command missing or wrong checker")
        require(data.get("command") == command, "receipt command differs from project check")
        require(data.get("exit_code") == 0 and data.get("passed") is True, "automatic check did not succeed")
        require(data.get("tool_version") and data.get("transcript") in files, "automatic receipt needs tool version and hashed transcript")
        require(data.get("engine_sha256") == digest(__file__), "automatic receipt is from a different Anvil checker version")
        for operand in command[1:]:
            path = (root / operand).resolve()
            require(path.is_relative_to(root), "check operand outside project")
            if path.is_dir():
                filenames = {"sim": ["assertions.tsv"], "fit": ["assertions.tsv", "measures.json"], "mass": ["assertions.tsv", "measures.json"], "mech-dfm": ["assertions.tsv", "measures.json"], "factory": ["acceptance.json", "unit-records.csv"]}.get(command[0], [])
                require(filenames, "unexpected automatic check directory")
                require(all((path / name).relative_to(root).as_posix() in files for name in filenames), "receipt omitted required check inputs")
            else:
                require(path.is_file() and path.relative_to(root).as_posix() in files, "receipt omitted required check input")
        if command[0] in {"erc", "drc"}:
            role = "schematic" if command[0] == "erc" else "pcb"
            require(set(cfg["artifacts"][role]) <= files.keys(), "receipt omitted a released board/schematic")
        if command[0] == "factory":
            policy_path = (root / command[1] / "acceptance.json").resolve()
            require(policy_path in {inside(root, p) for p in cfg["artifacts"].get("factory_policy", [])}, "factory acceptance policy must be controlled in the release manifest")
    else:
        require(data.get("producer") in {"review", "external"}, "review/import receipt required")
        if check["authority"] == "external":
            require(data.get("producer") == "external", "physical/market approval requires imported external evidence")
        approval = data.get("approval", {})
        require(isinstance(approval, dict) and all(isinstance(approval.get(k), str) and approval[k].strip()
                    for k in ("reviewer", "role", "decision", "record")), "reviewer, role, decision, and approval record required")
        require(approval["record"] in files, "approval record must be included in hashed evidence")
        require(approval["decision"] == ("not_applicable" if data["status"] == "na" else "approved"), "approval decision mismatch")
    if data["status"] == "na":
        require(not check["id"].startswith(("AUTO-", "REQ-")), "required automatic/requirement check cannot be waived as NA")
        require(isinstance(data.get("rationale"), str) and len(data["rationale"].strip()) >= 20, "NA needs a specific applicability rationale")
        expiry = datetime.fromisoformat(data.get("expires_at", "").replace("Z", "+00:00"))
        require(expiry.tzinfo and expiry > datetime.now(timezone.utc), "NA disposition expired or has no expiry")
    return data


def gate(root, target=None):
    root, cfg = project(root)
    target = target or cfg["target_gate"]
    require(target in GATES, f"unknown gate: {target}")
    level = GATES.index(target)
    checks, reqs = all_checks(root, cfg, allow_empty=level == 0)
    blockers = []
    release_hash = None
    if level >= 3:
        try:
            snap, release_hash = snapshot(root, cfg)
            manifest = read_json(root / "release-manifest.json")
            require(manifest == dict(snap, sha256=release_hash), "release manifest is stale; regenerate then rerun/review affected checks")
        except (ValueError, OSError) as error:
            blockers.append(str(error))
    ledger = index(results(root / "anvil-results.tsv"), "assertion")
    linked = set().union(*(traces(r["traces"]) for r in ledger.values()))
    require(linked <= reqs.keys(), f"orphan requirement traces: {sorted(linked - reqs.keys())}")
    expected = {c["id"]: c for c in checks}
    require(set(ledger) <= expected.keys(), f"unknown ledger checks: {sorted(set(ledger) - expected.keys())}; add project requirements instead")
    for check in checks:
        if GATES.index(check["gate"]) > level:
            continue
        key, row = check["id"], ledger.get(check["id"])
        try:
            require(row and row["status"] in {"pass", "na"}, f"{key}: missing or {row['status'] if row else 'not_run'}")
            require(row["dimension"] == check["dimension"], f"{key}: wrong dimension")
            if key.startswith("REQ-"):
                require(traces(row["traces"]) == {key[4:]}, f"{key}: missing exact requirement trace")
            receipt = receipt_valid(root, cfg, check, row["evidence"], release_hash)
            require(row["status"] == receipt["status"], "ledger/receipt status mismatch")
        except (ValueError, OSError) as error:
            blockers.append(f"{key}: {error}")
    labels = {"G0": "OPPORTUNITY_REVIEWED", "G1": "HRS_READY", "G2": "ARCHITECTURE_READY",
              "G3": {"pcb": "PCB_FAB_READY", "assembly": "ASSEMBLY_READY", "product": "PRODUCT_BUILD_READY"}[cfg["release_kind"]],
              "G4": "EVT_COMPLETE", "G5": "DESIGN_QUALIFIED", "G6": "PRODUCTION_READY", "G7": "MARKET_READY", "Sustaining": "SUSTAINING_REVIEWED"}
    return (f"{target}_BLOCKED" if blockers else labels[target]), blockers


def plan(root):
    root, cfg = project(root)
    checks, _ = all_checks(root, cfg, allow_empty=True)
    path = root / "anvil-results.tsv"
    previous = index(results(path), "assertion") if path.exists() else {}
    expected = {c["id"] for c in checks}
    require(set(previous) <= expected, "profile removed existing checks: retain the old ledger as a reviewed archive before planning")
    rows = []
    for n, check in enumerate(checks, 1):
        key = check["id"]
        row = previous.get(key, dict(assertion=key, dimension=check["dimension"], status="not_run", weight="1", evidence="", traces=key[4:] if key.startswith("REQ-") else ""))
        rows.append(dict(row, n=str(n)))
    write_ledger(path, rows)
    write_json(root / "lifecycle-plan.json", {"schema_version": 1, "profile": profile(cfg), "checks": checks})
    return f"PLAN: {len(rows)} checks; evidence not yet verified"


def prepare(root, check_id, files):
    root, cfg = project(root)
    checks, _ = all_checks(root, cfg, allow_empty=True)
    by_id = index(checks, "id")
    require(check_id in by_id and by_id[check_id]["authority"] != "tool", "prepare is for applicable review/external checks; execute automatic checks with record")
    check = by_id[check_id]
    hashes = {name: digest(inside(root, name)) for name in files}
    if check["gate"] in {"G1", "G2"}:
        hashes[cfg["requirements"]] = digest(inside(root, cfg["requirements"]))
    release_hash = snapshot(root, cfg)[1] if GATES.index(check["gate"]) >= 3 else None
    path = root / "evidence" / f"{check_id}.draft.json"
    require(not path.exists(), "review draft already exists; preserve it or choose a new evidence file explicitly")
    write_json(path, dict(schema_version=1, check_id=check_id, check_sha256=json_digest(check), status="not_run",
                         method=check["method"], producer="external" if check["authority"] == "external" else "review",
                         created_at=datetime.now(timezone.utc).isoformat(), profile_sha256=json_digest(profile(cfg)),
                         release_sha256=release_hash, files=hashes, approval=dict(reviewer="", role=check["owner"], decision="", record="")))
    return f"REVIEW_DRAFT: {path}; requires actual evidence review and approval"


def record(root, check_id, evidence=None):
    root, cfg = project(root)
    checks, _ = all_checks(root, cfg, allow_empty=True)
    by_id = index(checks, "id")
    require(check_id in by_id, f"check is not applicable/planned: {check_id}")
    check = by_id[check_id]
    ledger_path = root / "anvil-results.tsv"
    ledger = results(ledger_path)
    require(check_id in {r["assertion"] for r in ledger}, "run plan before recording evidence")
    for row in ledger:
        if row["assertion"] == check_id:
            row.update(status="not_run", evidence="")
    write_ledger(ledger_path, ledger)
    release_hash = snapshot(root, cfg)[1] if GATES.index(check["gate"]) >= 3 else None
    destination = root / "evidence" / (check_id + ".json")
    if evidence:
        require(check["authority"] != "tool", "automatic checks must execute through record; --evidence is for reviews and external tests")
        # Import a completed attestation, never invent an approval identity or test result.
        relative = Path(evidence).resolve().relative_to(root).as_posix()
        receipt_valid(root, cfg, check, relative, release_hash)
        data = read_json(root / relative)
    else:
        require(check["authority"] == "tool", "review/test checks require --evidence with an externally completed receipt")
        command = cfg.get("checks", {}).get(check_id)
        require(isinstance(command, list) and len(command) >= 2 and all(isinstance(a, str) and a for a in command), "configure this check's command array in anvil-project.json")
        require(command[0] == check["criterion"], f"{check_id} must execute {check['criterion']}")
        # Every operand is an existing input, with optional report output managed by the wrapper.
        require(not (command[0] in {"erc", "drc"} and len(command) != 2), "record ERC/DRC with the input only; output is managed by Anvil")
        inputs = []
        for operand in command[1:]:
            path = (root / operand).resolve()
            require(not Path(operand).is_absolute() and path.is_relative_to(root) and path.exists(), "check inputs must exist inside the project")
            inputs.append(str(path))
        manifest_files = snapshot(root, cfg)[0]["files"]
        role = {"erc": "schematic", "drc": "pcb", "bom-cost": "bom", "pinout": "harness", "product-bom": "product_bom", "sys-budget": "budgets", "fit": "mechanical_measures", "mass": "mechanical_measures", "mech-dfm": "mechanical_measures", "firmware": "firmware_manifest"}.get(command[0])
        if role:
            operand = Path(inputs[0]) / "measures.json" if command[0] in {"fit", "mass", "mech-dfm"} else Path(inputs[0])
            require(operand in {inside(root, p) for p in cfg["artifacts"].get(role, [])}, f"check does not use released {role}")
        if command[0] == "pinout":
            require(len(inputs) == 3, "product harness recording requires the actual mates file")
            require(Path(inputs[1]) in {inside(root, p) for p in cfg["artifacts"].get("icd", [])}, "pinout must use the released ICD")
        if command[0] == "sys-budget":
            table(inputs[0], ("demand_source", "capability_source"))
        if command[0] == "bom-cost":
            require(len(inputs) == 2 and Path(inputs[1]) in {inside(root, p) for p in cfg["artifacts"].get("catalog", [])}, "BOM must use the released catalog")
        if command[0] == "factory":
            require(Path(inputs[0]) / "acceptance.json" in {inside(root, p) for p in cfg["artifacts"].get("factory_policy", [])}, "declare the approved factory_policy in release artifacts before recording PVT")
            policy = read_json(Path(inputs[0]) / "acceptance.json")
            require(policy.get("hardware_revision") == cfg["hardware_revision"], "pilot hardware differs from release")
            binaries = {digest(inside(root, p)) for p in cfg["artifacts"].get("firmware_binary", [])}
            require(policy.get("firmware_sha256") in (binaries if "firmware" in cfg["features"] else {"none"}), "pilot firmware differs from release")
        if command[0] == "firmware":
            release = read_json(inputs[0])
            require(cfg["hardware_revision"] in release.get("supported_hardware", []), "firmware does not support the released hardware revision")
            for key, expected_role in (("binary", "firmware_binary"), ("dependency_lock", "firmware_lock")):
                require(inside(Path(inputs[0]).parent, release.get(key)) in {inside(root, p) for p in cfg["artifacts"].get(expected_role, [])}, f"firmware {key} differs from release role")
        # Multi-board releases require project requirements for every additional board; enforce
        # one automatic invocation per released board through this list, without a shell runner.
        commands = [inputs]
        if command[0] in {"erc", "drc"}:
            commands = [[str(inside(root, p))] for p in cfg["artifacts"][role]]
        READS.clear()
        OUTPUTS.clear()
        DETAILS.clear()
        summaries, passed = [], True
        for operands in commands:
            text_result, success = metric(command[0], operands)
            summaries.append(text_result)
            passed &= success
        DETAILS.extend(summaries)
        require(snapshot(root, cfg)[1] == release_hash, "release inputs changed during check")
        input_hashes = {}
        for path in READS:
            require(path.is_relative_to(root), f"check input outside project: {path}; vendor/pin it inside the project")
            rel = path.relative_to(root).as_posix()
            if path not in OUTPUTS and command[0] not in {"factory", "commercial"}:
                require(rel in manifest_files, f"check dependency omitted from release manifest: {rel}")
            input_hashes[rel] = digest(path)
        transcript = f"evidence/{check_id}.log"
        destination.parent.mkdir(parents=True, exist_ok=True)
        (root / transcript).write_text("\n".join(DETAILS) + "\n", encoding="utf-8")
        input_hashes[transcript] = digest(root / transcript)
        version = sys.version.split()[0]
        if command[0] in {"erc", "drc", "sim"}:
            tool = executable("ngspice" if command[0] == "sim" else "kicad-cli")
            version_run = execute([tool, "--version" if command[0] == "sim" else "version"])
            require(version_run.returncode == 0 and version_run.stdout.strip(), "tool version could not be recorded")
            version = version_run.stdout.strip()
        data = dict(schema_version=1, check_id=check_id, check_sha256=json_digest(check), status="pass" if passed else "fail", method=check["method"],
                    producer="anvil", created_at=datetime.now(timezone.utc).isoformat(), profile_sha256=json_digest(profile(cfg)),
                    release_sha256=release_hash, files=input_hashes, command=command, exit_code=0, passed=passed,
                    tool_version=version, transcript=transcript, engine_sha256=digest(__file__))
    write_json(destination, data)
    for row in ledger:
        if row["assertion"] == check_id:
            row.update(status=data["status"], evidence=destination.relative_to(root).as_posix())
    write_ledger(ledger_path, ledger)
    return f"RECORDED: {check_id} {data['status']}", data["status"] in {"pass", "na"}


def handoff(path):
    data = read_json(path)
    require(isinstance(data, dict) and data.get("schema_version") == 1, "handoff schema_version must be 1")
    commands = {"anvil", "build", "requirements", "improve", "evals", "lifecycle"}
    require(data.get("command") in commands, "unknown handoff command")
    require(data.get("gate") in GATES and isinstance(data.get("project"), str), "handoff needs project and gate")
    root = (Path(path).resolve().parent / data["project"]).resolve()
    verdict, blockers = gate(root, data["gate"])
    require(data.get("verdict") == verdict, f"handoff verdict not supported by current evidence: {verdict}")
    require(data.get("results_sha256") == digest(root / "anvil-results.tsv"), "handoff ledger is stale")
    require(data.get("project_sha256") == digest(root / "anvil-project.json"), "handoff project is stale")
    require(data.get("blockers") == blockers, "handoff must carry the actual blockers")
    for key in ("baseline", "final", "metric_value", "pass_rate", "coverage"):
        if key in data:
            require(isinstance(data[key], (int, float)) and not isinstance(data[key], bool), f"{key} must be a JSON number")
            value = number(data[key])
            if key in {"pass_rate", "coverage"}:
                require(0 <= value <= 1, f"{key} must be within [0,1]")
    return "HANDOFF: VALID"


def doctor(build=False, product_tools=False):
    missing = 0
    require(sys.version_info >= (3, 10), "Python 3.10+ required")
    print(f"FOUND python {sys.version.split()[0]} ({sys.executable})")
    if shutil.which("git"):
        print("FOUND git")
    else:
        print("MISSING git: install Git for source history")
        missing += 1
    for name in ("kicad-cli", "ngspice"):
        try:
            tool = executable(name)
            run = execute([tool, "version" if name == "kicad-cli" else "--version"])
            require(run.returncode == 0 and run.stdout.strip(), f"{name} version probe failed")
            print(f"FOUND {name} {tool}")
        except (ValueError, OSError) as error:
            print(f"{'MISSING' if build or product_tools else 'OPTIONAL'} {name}: {error}")
            missing += bool(build or product_tools)
    cad = [name for name in ("build123d", "cadquery") if importlib.util.find_spec(name)]
    if shutil.which("openscad"):
        cad.append("openscad")
    if cad:
        print(f"FOUND CAD {', '.join(cad)}; validate the selected project generator")
    else:
        print(f"{'MISSING' if product_tools else 'OPTIONAL'} CAD: selected build123d, CadQuery or OpenSCAD authoring tool")
        missing += bool(product_tools)
    print("OPTIONAL authoring: SKiDL/kiutils, firmware SDK/HIL, slicer/CAM and fixture tools as selected by the project")
    print("DOCTOR: READY" if not missing else f"DOCTOR: BLOCKED {missing} missing")
    DETAILS.clear()
    return int(bool(missing))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("doctor")
    p.add_argument("--require-build", action="store_true")
    p.add_argument("--require-product", action="store_true")
    for command in ("pass-rate", "coverage", "erc", "drc", "sim", "bom-cost", "area", "mesh", "fit", "mass", "mech-dfm", "pinout", "product-bom", "sys-budget", "firmware", "factory", "commercial", "verdict"):
        p = sub.add_parser(command)
        p.add_argument("inputs", nargs="*")
    for command in ("init", "plan", "manifest", "gate", "record", "prepare", "handoff"):
        p = sub.add_parser(command)
        p.add_argument("project")
        if command == "init":
            p.add_argument("--scope", choices=("pcb", "assembly", "product"), default="pcb")
            p.add_argument("--sectors", default="embedded")
            p.add_argument("--markets", default="US,EU")
            p.add_argument("--features", default="electronics,firmware")
        if command == "gate":
            p.add_argument("target", choices=GATES, nargs="?")
        if command == "record":
            p.add_argument("check_id")
            p.add_argument("--evidence")
        if command == "prepare":
            p.add_argument("check_id")
            p.add_argument("files", nargs="+")
        if command == "handoff":
            p.add_argument("--write", choices=("anvil", "build", "requirements", "improve", "evals", "lifecycle"))
            p.add_argument("--gate", choices=GATES)
    args = parser.parse_args(argv)
    try:
        command = args.command
        if command == "doctor":
            return doctor(args.require_build, args.require_product)
        elif command == "init":
            root = Path(args.project).resolve()
            require(not root.exists() or (root.is_dir() and not any(root.iterdir())), "init requires an empty destination; migrate existing projects explicitly")
            shutil.copytree(template_root(), root, dirs_exist_ok=True)
            cfg = read_json(root / "anvil-project.json")
            cfg.update(name=root.name, release_kind=args.scope, sectors=args.sectors.split(","), markets=args.markets.split(","), features=args.features.split(","))
            write_json(root / "anvil-project.json", cfg)
            project(root)
            print(f"INITIALIZED: {root}; define requirements and artifacts, then run plan")
        elif command == "plan":
            print(plan(args.project))
        elif command == "prepare":
            print(prepare(args.project, args.check_id, args.files))
        elif command == "manifest":
            root, cfg = project(args.project)
            snap, sha = snapshot(root, cfg)
            write_json(root / "release-manifest.json", dict(snap, sha256=sha))
            print(f"RELEASE_SHA256: {sha}")
        elif command == "gate":
            verdict, blockers = gate(args.project, args.target)
            print(verdict)
            for block in blockers:
                print(block, file=sys.stderr)
            return 1 if blockers else 0
        elif command == "record":
            result, ok = record(args.project, args.check_id, args.evidence)
            print(result)
            return 0 if ok else 1
        elif command == "handoff":
            if args.write:
                root, cfg = project(args.project)
                target = args.gate or cfg["target_gate"]
                verdict, blockers = gate(root, target)
                path = root / "handoff.json"
                write_json(path, dict(schema_version=1, command=args.write, project=".", gate=target, verdict=verdict,
                                     blockers=blockers, results_sha256=digest(root / "anvil-results.tsv"), project_sha256=digest(root / "anvil-project.json")))
            else:
                path = args.project
            print(handoff(path))
        elif command == "verdict":
            require(len(args.inputs) <= 1, "verdict now accepts a project directory; use gate <project> G3")
            root = Path(args.inputs[0] if args.inputs else ".")
            if not root.is_dir() or not (root / "anvil-project.json").is_file():
                print("FAB_BLOCKED")
                print("Legacy ledgers cannot authorize release; migrate to anvil-project.json and gate.", file=sys.stderr)
                return 1
            verdict, blockers = gate(root, "G3")
            print(verdict)
            for block in blockers:
                print(block, file=sys.stderr)
            return int(bool(blockers))
        else:
            inputs = args.inputs
            if command == "pass-rate" and not inputs:
                inputs = [os.getenv("ANVIL_RESULTS", "anvil-results.tsv")]
            output, _ = metric(command, inputs)
            print(output)
        for detail in DETAILS:
            print(detail, file=sys.stderr)
        return 0
    except (ValueError, OSError, KeyError, TypeError, ArithmeticError, csv.Error, subprocess.SubprocessError) as error:
        if args.command == "handoff":
            print("HANDOFF: INVALID")
        print(f"ANVIL_ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
