#!/usr/bin/env python3
"""Schematic wiring truth: KiCad netlist export, connectivity assertions, wiring tables.

Standard library only. The netlist is exported fresh by kicad-cli for every run; an old
netlist file can never satisfy an assertion. ERC proves rule hygiene; this proves that the
intended wiring exists (golden connectivity), which ERC cannot know.
"""
from __future__ import annotations

import re
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

from anvil import DETAILS, READS, execute, executable, inside, read, require, table, traces

KINDS = {"equals", "contains", "excludes", "connected", "isolated", "count", "decoupled",
         "no_floating", "series", "pin_type", "golden"}


def export_netlist(schematic):
    """Run kicad-cli and return (nets, parts, pin_types, xml_text)."""
    schematic = Path(schematic).resolve()
    read(schematic)
    with tempfile.TemporaryDirectory(prefix="anvil-net-", dir=schematic.parent) as temp:
        target = Path(temp) / "netlist.xml"
        run = execute([executable("kicad-cli"), "sch", "export", "netlist", "--format", "kicadxml",
                       "-o", str(target), str(schematic)], cwd=schematic.parent)
        require(run.returncode == 0 and target.is_file(), f"kicad-cli netlist export failed ({run.returncode})")
        text = target.read_text(encoding="utf-8")
    return parse_netlist(text) + (text,)


def parse_netlist(text):
    root = ET.fromstring(text)
    require(root.tag == "export", "not a KiCad XML netlist")
    parts = {}
    for comp in root.findall("./components/comp"):
        ref = comp.get("ref")
        if ref.startswith("#"):
            continue  # power symbols and flags are not physical parts
        fields = {f.get("name"): (f.text or "").strip() for f in comp.findall("./fields/field")}
        parts[ref] = dict(value=(comp.findtext("value") or "").strip(),
                          footprint=(comp.findtext("footprint") or "").strip(), fields=fields,
                          pins={p.get("num") for p in comp.findall(".//pins/pin")})
    nets, pin_types = {}, {}
    for net in root.findall("./nets/net"):
        members = set()
        for node in net.findall("node"):
            ref, pin = node.get("ref"), node.get("pin")
            if ref.startswith("#"):
                continue  # power symbols and flags are not physical pins
            members.add((ref, pin))
            pin_types[(ref, pin)] = node.get("pintype", "")
        nets[net.get("name")] = members
    require(nets, "netlist has no nets")
    return nets, parts, pin_types


def endpoint(text):
    match = re.fullmatch(r"([^.\s]+)\.([^.\s]+)", text.strip())
    require(match, f"member must be REF.PIN: {text}")
    return match[1], match[2]


def members(text):
    return {endpoint(m) for m in re.split(r"[;,\s]+", text.strip()) if m}


def net_of(nets, ref, pin):
    for name, nodes in nets.items():
        if (ref, pin) in nodes:
            return name
    return None


def resolve_net(nets, name):
    """Accept net names with or without the hierarchical '/' prefix."""
    for candidate in (name, "/" + name, name.lstrip("/")):
        if candidate in nets:
            return candidate
    raise ValueError(f"net not in schematic: {name}")


def check(kind, target, args, nets, parts, pin_types):
    """Return (ok, observation)."""
    if kind == "equals":
        net = resolve_net(nets, target)
        want = members(args)
        return nets[net] == want, f"{net}={sorted(nets[net])}"
    if kind == "contains":
        net = resolve_net(nets, target)
        missing = members(args) - nets[net]
        return not missing, f"missing on {net}: {sorted(missing)}" if missing else f"{net} ok"
    if kind == "excludes":
        net = resolve_net(nets, target)
        present = members(args) & nets[net]
        return not present, f"forbidden on {net}: {sorted(present)}" if present else f"{net} ok"
    if kind in {"connected", "isolated"}:
        pins = members(args) | ({endpoint(target)} if target else set())
        require(len(pins) >= 2, "connected/isolated need two or more REF.PIN")
        found = {net_of(nets, *p) for p in pins}
        require(None not in found, f"pin not in netlist: {sorted(p for p in pins if net_of(nets, *p) is None)}")
        same = len(found) == 1
        return (same if kind == "connected" else not same), f"nets={sorted(found)}"
    if kind == "count":
        net = resolve_net(nets, target)
        op, limit = args.split()
        value, bound = len(nets[net]), int(limit)
        ok = {"eq": value == bound, "ge": value >= bound, "le": value <= bound}[op]
        return ok, f"{net} has {value} pins"
    if kind == "decoupled":
        # Every power_in pin of REF (or the listed pins) has a capacitor whose other pin is on GND.
        ref, gnd = target, resolve_net(nets, args.split()[0])
        listed = args.split()[1:]
        pins = set(listed) if listed else {p for (r, p), t in pin_types.items()
                                           if r == ref and t == "power_in" and net_of(nets, r, p) != gnd}  # a ground pin is not a rail
        require(pins, f"{ref}: no power_in pins found; list the pins explicitly")
        bad = []
        for pin in sorted(pins):
            net = net_of(nets, ref, pin)
            caps = [r for (r, p) in nets.get(net, set()) if r.startswith("C") and r != ref
                    and any(net_of(nets, r, q) == gnd for q in parts[r]["pins"] - {p})]
            if not caps:
                bad.append(f"{ref}.{pin} on {net}")
        return not bad, "undecoupled: " + "; ".join(bad) if bad else f"{ref} decoupled on {sorted(pins)}"
    if kind == "no_floating":
        ref = target
        allowed = {p for (_, p) in members(" ".join(f"{ref}.{a}" for a in args.split()))} if args.strip() else set()
        floating = sorted(p for p in parts[ref]["pins"] if net_of(nets, ref, p) is None and p not in allowed)
        return not floating, f"{ref} floating pins: {floating}" if floating else f"{ref} all pins wired"
    if kind == "series":
        # REF is in series between two nets: one pin on each.
        ref, (a, b) = target, [resolve_net(nets, n) for n in args.split()]
        hits = {net_of(nets, ref, p) for p in parts[ref]["pins"]}
        return {a, b} <= hits, f"{ref} pins on {sorted(hits)}"
    if kind == "pin_type":
        ref, pin = endpoint(target)
        return pin_types.get((ref, pin)) == args.strip(), f"{ref}.{pin} type={pin_types.get((ref, pin))}"
    raise ValueError(f"unknown assertion kind: {kind}")


def connectivity(schematic, assertions):
    schematic = Path(schematic).resolve()
    rows = table(assertions, ("id", "kind", "target", "args", "traces"))
    require(len({r["id"] for r in rows}) == len(rows), "duplicate assertion ids")
    nets, parts, pin_types, text = export_netlist(schematic)
    DETAILS.append(f"NETLIST: {len(nets)} nets, {len(parts)} parts (fresh kicad-cli export)")
    passed = 0
    for row in rows:
        require(row["kind"] in KINDS, f"unknown kind {row['kind']}: {row['id']}")
        traces(row["traces"])
        if row["kind"] == "golden":  # whole netlist == circuit spec (target: spec path relative to this table)
            import anvil_schematic
            golden = anvil_schematic.load_spec(Path(assertions).resolve().parent / row["target"])[2]
            READS.add((Path(assertions).resolve().parent / row["target"]).resolve())
            problems = anvil_schematic.compare(nets, golden)
            ok, observation = not problems, "; ".join(problems) or f"{len(golden)} nets identical"
        else:
            ok, observation = check(row["kind"], row["target"], row["args"], nets, parts, pin_types)
        passed += ok
        DETAILS.append(f"{row['id']} {row['kind']} {row['target']}: {observation} {'PASS' if ok else 'FAIL'}")
    return f"CONNECTIVITY: {passed}/{len(rows)}", passed == len(rows)


def wiring_tables(schematic, outdir):
    """Write wiring.md (net table + part table) and wiring.dot for the audit package."""
    nets, parts, pin_types, text = export_netlist(schematic)
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "netlist.xml").write_text(text, encoding="utf-8")
    lines = ["# Wiring (fresh KiCad netlist export)", "", "| Net | Pins | Members |", "|---|---|---|"]
    for name in sorted(nets):
        lines.append(f"| `{name}` | {len(nets[name])} | " + ", ".join(f"{r}.{p}" for r, p in sorted(nets[name])) + " |")
    lines += ["", "| Ref | Value | Footprint | Pins | Nets |", "|---|---|---|---|---|"]
    for ref in sorted(parts, key=lambda r: (re.sub(r"\d+$", "", r), int(re.search(r"(\d+)$", r)[1]) if re.search(r"\d+$", r) else 0)):
        touched = sorted({net_of(nets, ref, p) for p in parts[ref]["pins"]} - {None})
        lines.append(f"| {ref} | {parts[ref]['value']} | {parts[ref]['footprint']} | {len(parts[ref]['pins'])} | " + ", ".join(f"`{n}`" for n in touched) + " |")
    (outdir / "wiring.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    dot = ["graph wiring {", "  graph [overlap=false, splines=true]; node [fontsize=9];"]
    for ref, part in sorted(parts.items()):
        label = f"{ref}\\n{part['value']}".replace('"', "'")
        dot.append(f'  "{ref}" [shape=box, label="{label}"];')
    for name, nodes in sorted(nets.items()):
        dot.append(f'  "{name}" [shape=ellipse, style=filled, fillcolor="#eeeeee", fontsize=8];')
        for ref, pin in sorted(nodes):
            dot.append(f'  "{ref}" -- "{name}" [taillabel="{pin}", fontsize=7];')
    dot.append("}")
    (outdir / "wiring.dot").write_text("\n".join(dot) + "\n", encoding="utf-8")
    return f"WIRING: {len(nets)} nets, {len(parts)} parts -> {outdir}"
