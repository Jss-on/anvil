#!/usr/bin/env python3
"""Wired schematics: place KiCad library symbols from a circuit spec, join pins with real
orthogonal wires, draw supply rails with power symbols, then prove the drawing against the
intended netlist with a fresh kicad-cli export and ERC.

Standard library only. `sch/circuit.json` is the golden netlist; the generated `.kicad_sch`
is a derived artifact that is re-verified every time it is written. KiCad connectivity rules
honoured by the router: wires connect only at their endpoints and at junctions, crossing wires
do not connect, collinear overlapping wires merge, and a wire end on another net's wire, pin,
label or junction would short the nets, so all of those are forbidden.
"""
from __future__ import annotations

import copy
import heapq
import math
import os
import re
import uuid
from pathlib import Path

from anvil import DETAILS, execute, executable, kicad, read, read_json, require, write_json

GRID = 1.27                                   # KiCad connection grid, 50 mil
PAPER = {"A4": (297.0, 210.0), "A3": (420.0, 297.0), "A2": (594.0, 420.0), "A1": (841.0, 594.0)}
FRAME = 12.7                                  # keep-out from the sheet edge (border strip)
TITLE = (116.84, 40.64)                       # bottom-right title block keep-out (width, height)
DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))     # right, down, left, up (schematic y grows down)
BEND, CROSS, CROWD = 3.0, 8.0, 0.35           # router costs per bend / crossing / crowded step
FORMAT = {10: "20260101", 9: "20250114", 8: "20231120"}
POWER_NET = re.compile(r"^(GND\w*|[ADP]GND\w*|VSS\w*|[+-]\d+(\.\d+)?V\d*\w*|[+-]?V(CC|DD)\w*)$")
TOKEN = re.compile(r'\(|\)|"(?:\\.|[^"\\])*"|[^\s()"]+')


# --- s-expressions that round-trip KiCad files --------------------------------------------------
def parse(text):
    stack = [[]]
    for token in TOKEN.findall(text):
        if token == "(":
            node = []
            stack[-1].append(node)
            stack.append(node)
        elif token == ")":
            require(len(stack) > 1, "unbalanced s-expression")
            stack.pop()
        else:
            stack[-1].append(token)
    require(len(stack) == 1 and len(stack[0]) == 1, "unbalanced s-expression")
    return stack[0][0]


def q(text):
    return '"' + str(text).replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'


def unq(token):
    if isinstance(token, str) and token.startswith('"'):
        return re.sub(r"\\(.)", lambda m: "\n" if m[1] == "n" else m[1], token[1:-1])
    return token


def child(node, key):
    return next((c for c in node[1:] if isinstance(c, list) and c and c[0] == key), None)


def children(node, key):
    return [c for c in node[1:] if isinstance(c, list) and c and c[0] == key]


def flag(node, key):
    found = child(node, key)
    if found is not None:
        return len(found) < 2 or found[1] == "yes"
    return key in node[1:]


def dump(node, depth=0):
    if not isinstance(node, list):
        return node
    lead = []
    for item in node:
        if isinstance(item, list):
            break
        lead.append(item)
    rest = node[len(lead):]
    if not rest:
        return "(" + " ".join(lead) + ")"
    flat = "(" + " ".join(lead + [dump(c) for c in rest]) + ")"
    if len(flat) <= 96 and all(not isinstance(c, list) or not any(isinstance(x, list) for x in c) for c in rest):
        return flat
    pad = "\t" * (depth + 1)
    return "(" + " ".join(lead) + "\n" + "\n".join(pad + dump(c, depth + 1) for c in rest) + "\n" + "\t" * depth + ")"


def fmt(value):
    text = f"{value:.4f}".rstrip("0").rstrip(".")
    return "0" if text in {"-0", ""} else text


def uid(*parts):
    return str(uuid.uuid5(uuid.NAMESPACE_URL, "anvil-schematic/" + "/".join(map(str, parts))))


# --- KiCad installation -----------------------------------------------------------------------------
def kicad_major():
    run = execute([executable("kicad-cli"), "version"])
    require(run.returncode == 0 and re.match(r"\s*\d+", run.stdout), "kicad-cli version failed")
    return int(re.match(r"\s*(\d+)", run.stdout)[1])


def kicad_footprint_dir():
    for name in ("KICAD10_FOOTPRINT_DIR", "KICAD9_FOOTPRINT_DIR", "KICAD_FOOTPRINT_DIR"):
        value = os.environ.get(name)
        if value and Path(value).is_dir():
            return Path(value)
    cli = Path(executable("kicad-cli")).resolve()
    for base in (cli.parents[1] / "share/kicad/footprints", cli.parents[1] / "SharedSupport/footprints",
                 Path("/usr/share/kicad/footprints"), Path("/usr/local/share/kicad/footprints")):
        if base.is_dir():
            return base
    return None


def link_footprint_libraries(project_dir, nicknames, major):
    """Project fp-lib-table rows for the stock KiCad footprint libraries the parts use, so ERC and
    `board` resolve every footprint even when the user's global table is empty. Existing rows are kept;
    nicknames that are not stock libraries must be added by the project."""
    stock = kicad_footprint_dir()
    if not stock:
        return
    table_path = Path(project_dir) / "fp-lib-table"
    text = table_path.read_text(encoding="utf-8") if table_path.is_file() else "(fp_lib_table\n  (version 7)\n)\n"
    rows = [f'  (lib (name "{nick}")(type "KiCad")(uri "${{KICAD{major}_FOOTPRINT_DIR}}/{nick}.pretty")(options "")(descr "KiCad stock library"))'
            for nick in sorted(nicknames) if f'(name "{nick}")' not in text and (stock / f"{nick}.pretty").is_dir()]
    if rows:
        table_path.write_text(text.rstrip().rstrip(")").rstrip() + "\n" + "\n".join(rows) + "\n)\n", encoding="utf-8")


def kicad_symbol_dir():
    for name in ("KICAD10_SYMBOL_DIR", "KICAD9_SYMBOL_DIR", "KICAD_SYMBOL_DIR"):
        value = os.environ.get(name)
        if value and Path(value).is_dir():
            return Path(value)
    cli = Path(executable("kicad-cli")).resolve()
    for base in (cli.parents[1] / "share/kicad/symbols", cli.parents[1] / "SharedSupport/symbols",
                 Path("/usr/share/kicad/symbols"), Path("/usr/local/share/kicad/symbols")):
        if base.is_dir():
            return base
    raise ValueError("KiCad symbol libraries not found; set KICAD_SYMBOL_DIR")


class Library:
    """Resolve Library:Name symbols from KiCad's libraries, project .kicad_sym files, or the
    embedded lib_symbols of an existing schematic. Derived symbols (extends) are flattened."""

    def __init__(self, base, extra):
        self.base, self.extra, self.files, self.version = Path(base), dict(extra or {}), {}, None
        self.system = None

    def table(self, nick):
        if nick not in self.files:
            if nick in self.extra:
                path = (self.base / self.extra[nick]).resolve()
            else:
                self.system = self.system or kicad_symbol_dir()
                path = self.system / f"{nick}.kicad_sym"
            require(path.is_file(), f"symbol library not found for {nick}: {path}")
            root = parse(read(path))
            if root[0] == "kicad_sch":
                lib = child(root, "lib_symbols") or ["lib_symbols"]
                self.files[nick] = ("embedded", {unq(s[1]): s for s in children(lib, "symbol")})
            else:
                require(root[0] == "kicad_symbol_lib", f"not a KiCad symbol library: {path}")
                version = child(root, "version")
                self.version = self.version or (version[1] if version else None)
                self.files[nick] = ("library", {unq(s[1]): s for s in children(root, "symbol")})
        return self.files[nick]

    def resolve(self, lib_id):
        nick, sep, name = lib_id.partition(":")
        require(sep and nick and name, f"symbol must be Library:Name: {lib_id}")
        kind, table = self.table(nick)
        if kind == "embedded":
            key = lib_id if lib_id in table else next((k for k in table if k.rpartition(":")[2] == name), None)
            require(key, f"symbol {lib_id} not embedded in {self.extra.get(nick)}")
            node = copy.deepcopy(table[key])
            node[1] = q(name)
            return node
        return flatten(table, name)


def flatten(table, name, seen=()):
    require(name in table, f"symbol not in library: {name}")
    node = copy.deepcopy(table[name])
    extends = child(node, "extends")
    if extends is None:
        return node
    require(name not in seen, f"cyclic extends: {name}")
    parent = flatten(table, unq(extends[1]), seen + (name,))
    parent_name = unq(parent[1])
    own = {c[0]: c for c in node[2:] if isinstance(c, list) and c[0] not in {"property", "extends", "symbol"}}
    props = {unq(c[1]): c for c in children(node, "property")}
    merged = ["symbol", q(name)]
    for item in parent[2:]:
        if isinstance(item, list) and item[0] == "property":
            merged.append(props.pop(unq(item[1]), item))
        elif isinstance(item, list) and item[0] == "symbol":
            merged.append(["symbol", q(name + unq(item[1])[len(parent_name):])] + item[2:])
        elif isinstance(item, list) and item[0] in own:
            merged.append(own.pop(item[0]))
        else:
            merged.append(item)
    return merged + list(own.values()) + list(props.values())


def rename(node, new_name):
    """Rename a flattened symbol and its unit sub-symbols (Name_U_B)."""
    old = unq(node[1]).rpartition(":")[2]
    out = copy.deepcopy(node)
    out[1] = q(new_name)
    base = new_name.rpartition(":")[2]
    for sub in children(out, "symbol"):
        sub[1] = q(base + unq(sub[1])[len(old):])
    return out


# --- symbol geometry --------------------------------------------------------------------------------
def local_geometry(node, unit, body_style=1):
    base = unq(node[1]).rpartition(":")[2]
    pins, points = {}, []
    for sub in children(node, "symbol"):
        match = re.fullmatch(re.escape(base) + r"_(\d+)_(\d+)", unq(sub[1]))
        if not match or int(match[1]) not in (0, unit) or int(match[2]) not in (0, body_style):
            continue
        for item in sub[2:]:
            if not isinstance(item, list):
                continue
            if item[0] == "pin":
                at, length = child(item, "at"), child(item, "length")
                number = unq(child(item, "number")[1])
                angle = float(at[3]) if len(at) > 3 else 0.0
                require(angle % 90 == 0, f"{base} pin {number}: only orthogonal pins are supported")
                pins[number] = dict(number=number, name=unq(child(item, "name")[1]), type=item[1],
                                    x=float(at[1]), y=float(at[2]), angle=angle % 360,
                                    length=float(length[1]) if length else 2.54, hidden=flag(item, "hide"))
            elif item[0] == "rectangle":
                points += [(float(child(item, k)[1]), float(child(item, k)[2])) for k in ("start", "end")]
            elif item[0] in {"polyline", "bezier"}:
                points += [(float(xy[1]), float(xy[2])) for xy in children(child(item, "pts"), "xy")]
            elif item[0] == "circle":
                center, radius = child(item, "center"), float(child(item, "radius")[1])
                cx, cy = float(center[1]), float(center[2])
                points += [(cx - radius, cy - radius), (cx + radius, cy + radius)]
            elif item[0] == "arc":
                points += [(float(child(item, k)[1]), float(child(item, k)[2])) for k in ("start", "mid", "end") if child(item, k)]
    require(pins, f"{base} unit {unit} has no pins")
    if not points:
        points = [(p["x"], p["y"]) for p in pins.values()]
    return dict(pins=pins, body=(min(p[0] for p in points), min(p[1] for p in points),
                                 max(p[0] for p in points), max(p[1] for p in points)))


MATRIX = {0: (1, 0, 0, -1), 90: (0, -1, -1, 0), 180: (-1, 0, 0, 1), 270: (0, 1, 1, 0)}


def transform(rot, mirror=None):
    """KiCad SCH_SYMBOL transform: library y-up coordinates to schematic y-down offsets."""
    x1, y1, x2, y2 = MATRIX[rot]
    if mirror == "y":
        x1, y1 = -x1, -y1
    if mirror == "x":
        x2, y2 = -x2, -y2
    return lambda px, py: (x1 * px + y1 * py, x2 * px + y2 * py)


def placed(local, at, rot, mirror=None):
    T = transform(rot, mirror)
    X, Y = at
    pins = {}
    for number, pin in local["pins"].items():
        dx, dy = T(pin["x"], pin["y"])
        vx, vy = T(math.cos(math.radians(pin["angle"])), math.sin(math.radians(pin["angle"])))
        inward = (round(vx), round(vy))
        point = (X + dx, Y + dy)
        pins[number] = dict(pin, point=point, inward=inward, outward=(-inward[0], -inward[1]),
                            root=(point[0] + inward[0] * pin["length"], point[1] + inward[1] * pin["length"]))
    b = local["body"]
    corners = [T(x, y) for x in (b[0], b[2]) for y in (b[1], b[3])]
    body = (X + min(c[0] for c in corners), Y + min(c[1] for c in corners),
            X + max(c[0] for c in corners), Y + max(c[1] for c in corners))
    xs = [body[0], body[2]] + [p["point"][0] for p in pins.values()]
    ys = [body[1], body[3]] + [p["point"][1] for p in pins.values()]
    return dict(pins=pins, body=body, full=(min(xs), min(ys), max(xs), max(ys)))


def gridpt(point):
    gx, gy = point[0] / GRID, point[1] / GRID
    require(abs(gx - round(gx)) < 1e-6 and abs(gy - round(gy)) < 1e-6,
            f"point {point} is off the {GRID} mm connection grid; place symbols on the 1.27 mm grid")
    return (round(gx), round(gy))


def direction_index(vector):
    return DIRS.index((int(vector[0]), int(vector[1])))


# --- the circuit spec -----------------------------------------------------------------------------------
def load_spec(path):
    path = Path(path).resolve()
    spec = read_json(path)
    require(isinstance(spec, dict) and spec.get("schema_version") == 1, "circuit spec schema_version must be 1")
    parts = spec.get("parts")
    require(isinstance(parts, list) and parts, "circuit spec needs a nonempty parts list")
    seen = set()
    for part in parts:
        require(isinstance(part, dict) and isinstance(part.get("ref"), str) and re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", part["ref"]),
                f"invalid part reference: {part!r}"[:120])
        require(isinstance(part.get("symbol"), str) and ":" in part["symbol"], f"{part['ref']}: symbol must be Library:Name")
        part.setdefault("unit", 1)
        part.setdefault("rot", 0)
        require(isinstance(part["unit"], int) and part["unit"] >= 1, f"{part['ref']}: unit must be a positive integer")
        require(part["rot"] in MATRIX, f"{part['ref']}: rot must be 0, 90, 180 or 270")
        require(part.get("mirror") in (None, "x", "y"), f"{part['ref']}: mirror must be x or y")
        if "at" in part:
            require(isinstance(part["at"], list) and len(part["at"]) == 2 and all(isinstance(v, (int, float)) and math.isfinite(v) for v in part["at"]),
                    f"{part['ref']}: at must be [x_mm, y_mm]")
        key = (part["ref"], part["unit"])
        require(key not in seen, f"duplicate part/unit: {key}")
        seen.add(key)
    nets = {name: list(members) for name, members in (spec.get("nets") or {}).items()}
    for part in parts:
        for pin, net in (part.get("pins") or {}).items():
            nets.setdefault(net, []).append(f"{part['ref']}.{pin}")
    owner, clean = {}, {}
    for name, members in nets.items():
        require(isinstance(name, str) and name and not re.search(r"[\[\]{}\s]", name), f"invalid net name: {name!r}")
        clean[name] = []
        for member in members:
            ref, sep, pin = str(member).partition(".")
            require(sep and ref and pin, f"{name}: member must be REF.PIN: {member}")
            require(owner.get((ref, pin), name) == name, f"{ref}.{pin} is on two nets: {owner.get((ref, pin))} and {name}")
            owner[(ref, pin)] = name
            if (ref, pin) not in clean[name]:
                clean[name].append((ref, pin))
    require(clean, "circuit spec needs nets")
    power = spec.get("power_nets")
    power = set(power) if power is not None else {n for n in clean if POWER_NET.match(n)}
    require(power <= set(clean), f"power_nets not in nets: {sorted(power - set(clean))}")
    flags = spec.get("pwr_flag") or []
    require(set(flags) <= set(clean), f"pwr_flag nets not in nets: {sorted(set(flags) - set(clean))}")
    return spec, parts, clean, owner, power, list(flags)


# --- placement --------------------------------------------------------------------------------------------
def overlaps(a, b):
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def grow(box, margin):
    return (box[0] - margin, box[1] - margin, box[2] + margin, box[3] + margin)


def auto_place(parts, local, owner, power, area, reserved, margin=3.81):
    """Grow a placement outward from the most connected part: each next part is put where the
    pin it shares a net with faces the already-placed pin on a straight line, when space allows."""
    placed_parts, occupied = {}, list(reserved)
    for part in parts:
        if "at" in part:
            geo = placed(local[(part["ref"], part["unit"])], part["at"], part["rot"], part.get("mirror"))
            placed_parts[(part["ref"], part["unit"])] = (tuple(part["at"]), part["rot"], geo)
            occupied.append(grow(geo["full"], margin))
    todo = [p for p in parts if "at" not in p]
    pins_of = {}
    for part in parts:
        for number in local[(part["ref"], part["unit"])]["pins"]:
            pins_of.setdefault((part["ref"], part["unit"]), []).append(number)

    def nets_of(part):
        return {owner[(part["ref"], n)] for n in pins_of[(part["ref"], part["unit"])] if (part["ref"], n) in owner}

    def free(box):
        return (box[0] >= area[0] and box[1] >= area[1] and box[2] <= area[2] and box[3] <= area[3]
                and not any(overlaps(box, o) for o in occupied))

    def commit(part, at, rot, geo):
        placed_parts[(part["ref"], part["unit"])] = (at, rot, geo)
        occupied.append(grow(geo["full"], margin))

    def scan(part):
        loc = local[(part["ref"], part["unit"])]
        for rot in dict.fromkeys([part["rot"], 0, 90]):
            geo0 = placed(loc, (0.0, 0.0), rot, part.get("mirror"))
            w, h = geo0["full"][2] - geo0["full"][0], geo0["full"][3] - geo0["full"][1]
            y = area[1] + margin
            while y + h <= area[3]:
                x = area[0] + margin
                while x + w <= area[2]:
                    at = (round((x - geo0["full"][0]) / GRID) * GRID, round((y - geo0["full"][1]) / GRID) * GRID)
                    geo = placed(loc, at, rot, part.get("mirror"))
                    if free(grow(geo["full"], margin)):
                        return at, rot, geo
                    x += 4 * GRID
                y += 4 * GRID
        raise ValueError(f"no room on the sheet for {part['ref']}; choose a larger paper size")

    while todo:
        placed_nets = {}
        for (ref, unit), (_, _, geo) in placed_parts.items():
            for number, pin in geo["pins"].items():
                if (ref, number) in owner:
                    placed_nets.setdefault(owner[(ref, number)], []).append(pin)
        score = lambda p: (len(nets_of(p) & placed_nets.keys() - power), len(nets_of(p) & placed_nets.keys()), len(pins_of[(p["ref"], p["unit"])]))
        part = max(todo, key=score) if placed_parts else max(todo, key=lambda p: len(pins_of[(p["ref"], p["unit"])]))
        todo.remove(part)
        loc = local[(part["ref"], part["unit"])]
        choice = None
        two_pin = len(loc["pins"]) <= 3
        rotations = [part["rot"], 0, 90, 180, 270] if two_pin else [part["rot"]]
        shared = sorted(nets_of(part) & placed_nets.keys(), key=lambda n: (n in power, n))  # total order: set order varies per process
        for net in shared:
            for anchor in placed_nets[net]:
                ax, ay = anchor["point"]
                out = anchor["outward"]
                side = (-out[1], out[0])
                offsets = [0, 2, -2, 4, -4, 6, -6] if net not in power else [3, -3, 5, -5, 7, -7]
                for rot in dict.fromkeys(rotations):
                    geo0 = placed(loc, (0.0, 0.0), rot, part.get("mirror"))
                    for number, pin in geo0["pins"].items():
                        if owner.get((part["ref"], number)) != net:
                            continue
                        if net not in power and pin["outward"] != (-out[0], -out[1]):
                            continue
                        for k in (6, 8, 10, 14, 18, 24):
                            for j in offsets:
                                tx = ax + out[0] * k * GRID + side[0] * j * GRID
                                ty = ay + out[1] * k * GRID + side[1] * j * GRID
                                at = (round((tx - pin["point"][0]) / GRID) * GRID, round((ty - pin["point"][1]) / GRID) * GRID)
                                geo = placed(loc, at, rot, part.get("mirror"))
                                if free(grow(geo["full"], margin)):
                                    choice = (at, rot, geo)
                                    break
                            if choice:
                                break
                        if choice:
                            break
                    if choice:
                        break
                if choice:
                    break
            if choice:
                break
        commit(part, *(choice or scan(part)))
    # Centre auto-placed parts on the drawing area (explicit coordinates are never moved).
    moved = [k for k, p in zip([(p["ref"], p["unit"]) for p in parts], parts) if "at" not in p]
    if moved:
        box = [min(placed_parts[k][2]["full"][0] for k in moved), min(placed_parts[k][2]["full"][1] for k in moved),
               max(placed_parts[k][2]["full"][2] for k in moved), max(placed_parts[k][2]["full"][3] for k in moved)]
        dx = round(((area[0] + area[2]) / 2 - (box[0] + box[2]) / 2) / 2.54) * 2.54
        dy = round(((area[1] + area[3]) / 2 - 12.7 - (box[1] + box[3]) / 2) / 2.54) * 2.54
        shifted = (box[0] + dx, box[1] + dy, box[2] + dx, box[3] + dy)
        fixed = [grow(placed_parts[k][2]["full"], margin) for k in placed_parts if k not in moved]
        if all(not overlaps(shifted, o) for o in fixed + list(reserved)) and shifted[0] >= area[0] and shifted[2] <= area[2] \
                and shifted[1] >= area[1] and shifted[3] <= area[3]:
            by_key = {(p["ref"], p["unit"]): p for p in parts}
            for k in moved:
                at, rot, _ = placed_parts[k]
                at = (at[0] + dx, at[1] + dy)
                placed_parts[k] = (at, rot, placed(local[k], at, rot, by_key[k].get("mirror")))
    return placed_parts


# --- the routing grid ---------------------------------------------------------------------------------------
def edge(a, b):
    return (a, b) if a <= b else (b, a)


class Grid:
    def __init__(self, width_mm, height_mm):
        self.nx, self.ny = int(width_mm / GRID) + 1, int(height_mm / GRID) + 1
        self.blocked, self.pins, self.edges, self.through, self.nodes = set(), {}, {}, {}, {}
        self.tree, self.segments, self.escapes = {}, [], {}

    def inside(self, p):
        return 0 <= p[0] < self.nx and 0 <= p[1] < self.ny

    def block_box(self, box_mm):
        x0, y0 = math.floor(box_mm[0] / GRID - 1e-9), math.floor(box_mm[1] / GRID - 1e-9)
        x1, y1 = math.ceil(box_mm[2] / GRID + 1e-9), math.ceil(box_mm[3] / GRID + 1e-9)
        for x in range(max(x0, 0), min(x1, self.nx - 1) + 1):
            for y in range(max(y0, 0), min(y1, self.ny - 1) + 1):
                self.blocked.add((x, y))

    def free_point(self, p, own_escape=None):
        return (self.inside(p) and p not in self.blocked and p not in self.pins and p not in self.nodes
                and not self.through.get(p) and (p not in self.escapes or p == own_escape))

    def commit(self, net, path, kind="route"):
        for a, b in zip(path, path[1:]):
            self.edges[edge(a, b)] = net
        for p in path:
            self.through.setdefault(p, set()).add(net)
            self.tree.setdefault(net, set()).add(p)
        start, previous = path[0], None
        for i in range(1, len(path)):
            step = (path[i][0] - path[i - 1][0], path[i][1] - path[i - 1][1])
            if previous is not None and step != previous:
                self.segments.append((net, start, path[i - 1], kind))
                self.nodes[path[i - 1]] = net
                start = path[i - 1]
            previous = step
        if len(path) > 1:
            self.segments.append((net, start, path[-1], kind))
        self.nodes[path[0]] = net
        self.nodes[path[-1]] = net

    def crowd(self, p, net):
        cost = 0.0
        for dx, dy in DIRS:
            n = (p[0] + dx, p[1] + dy)
            if n in self.blocked or (self.through.get(n, set()) - {net}):
                cost += CROWD
        return cost

    def route(self, net, start, out_dir, goals, limit=300_000):
        """A* from a pin (leaving along its outward direction) to any legal point of the net's tree."""
        if not goals:
            return None
        gx0, gx1 = min(p[0] for p in goals), max(p[0] for p in goals)
        gy0, gy1 = min(p[1] for p in goals), max(p[1] for p in goals)
        heuristic = lambda p: max(gx0 - p[0], 0, p[0] - gx1) + max(gy0 - p[1], 0, p[1] - gy1)
        frontier = [(heuristic(start), 0.0, start, -1)]
        best, came = {(start, -1): 0.0}, {}
        expanded = 0
        while frontier and expanded < limit:
            _, cost, p, d = heapq.heappop(frontier)
            if best.get((p, d), math.inf) < cost:
                continue
            expanded += 1
            crossing = p != start and bool(self.through.get(p, set()) - {net})
            for nd, (dx, dy) in enumerate(DIRS):
                if d == -1 and nd != out_dir:
                    continue
                if d != -1 and nd == (d + 2) % 4:
                    continue
                if crossing and nd != d:
                    continue  # a bend on another net's wire would connect the nets
                nxt = (p[0] + dx, p[1] + dy)
                if not self.inside(nxt) or nxt in self.blocked or edge(p, nxt) in self.edges:
                    continue
                if nxt in goals:
                    allowed = goals[nxt]
                    if allowed is None or nd in allowed:
                        came[(nxt, nd)] = (p, d)
                        path, state = [nxt], (p, d)
                        while state[0] != start or state[1] != -1:
                            path.append(state[0])
                            state = came[state]
                        path.append(start)
                        return list(reversed(path))
                    continue
                if nxt in self.pins or nxt in self.nodes:
                    continue
                others = self.through.get(nxt, set())
                if net in others:
                    continue
                step = cost + 1.0 + (BEND if d not in (-1, nd) else 0.0) + (CROSS if others else 0.0) + self.crowd(nxt, net)
                if self.escapes.get(nxt, net) != net:
                    step += 5.0  # keep other pins' exit squares open for their own nets
                if step < best.get((nxt, nd), math.inf):
                    best[(nxt, nd)] = step
                    came[(nxt, nd)] = (p, d)
                    heapq.heappush(frontier, (step + heuristic(nxt), step, nxt, nd))
        return None

    def goals(self, net):
        result = {}
        for p in self.tree.get(net, ()):
            if self.through.get(p, set()) - {net}:
                continue  # a crossing point on the tree: ending there would join the crossing net
            if p in self.pins:
                if self.pins[p][0] == net:
                    result[p] = {(self.pins[p][1] + 2) % 4}
            else:
                result[p] = None
        return result


# --- generation ---------------------------------------------------------------------------------------------
def power_symbol_name(net, available):
    if net in available:
        return net
    if re.match(r"^([ADP]?GND|VSS)", net):
        return "GND"
    if net.startswith("-"):
        return "-VDC" if "-VDC" in available else "GND"
    return "VCC" if "VCC" in available else "+VDC"


def text_box(x, y, text, justify="left", size=1.27):
    width = max(1, len(text)) * size * 0.9
    if justify == "left":
        return (x, y - size, x + width, y + size * 0.4)
    if justify == "right":
        return (x - width, y - size, x, y + size * 0.4)
    return (x - width / 2, y - size, x + width / 2, y + size * 0.4)


def field_layout(geo, ref, value):
    sides = {pin["outward"] for pin in geo["pins"].values()}
    b, f = geo["body"], geo["full"]
    if sides <= {(0, 1), (0, -1)}:
        cy = (b[1] + b[3]) / 2
        ref_pos, val_pos, just = (b[2] + 1.27, cy - 1.27), (b[2] + 1.27, cy + 1.27), "left"
    elif sides <= {(1, 0), (-1, 0)}:
        cx = (b[0] + b[2]) / 2
        ref_pos, val_pos, just = (cx, b[1] - 1.905), (cx, b[3] + 2.54), "center"
    else:
        ref_pos, val_pos, just = (f[0], f[1] - 1.905), (f[0], f[3] + 2.54), "left"
    return (ref_pos, val_pos, just, [text_box(*ref_pos, ref, just), text_box(*val_pos, value, just)])


def generate(spec_path, out_path, verify=True):
    spec_path, out_path = Path(spec_path).resolve(), Path(out_path).resolve()
    spec, parts, nets, owner, power, flags = load_spec(spec_path)
    major = kicad_major()
    version = FORMAT.get(major, FORMAT[max(FORMAT)] if major > max(FORMAT) else FORMAT[min(FORMAT)])
    library = Library(spec_path.parent, spec.get("libraries"))
    project = spec.get("project") or out_path.stem
    libname = spec.get("library_name") or f"{out_path.stem}_symbols"
    sheet = uid(project, out_path.name, "sheet")

    # 1. Resolve and vendor every symbol into one project library (unique names).
    vendored, lib_ids, local = {}, {}, {}
    for part in parts:
        if part["symbol"] not in lib_ids:
            node = library.resolve(part["symbol"])
            name = part["symbol"].rpartition(":")[2]
            if name in vendored:
                name = part["symbol"].replace(":", "_")
            vendored[name] = rename(node, name)
            lib_ids[part["symbol"]] = f"{libname}:{name}"
        node = vendored[lib_ids[part["symbol"]].partition(":")[2]]
        local[(part["ref"], part["unit"])] = local_geometry(node, part["unit"])
    known = {(p["ref"], n) for p in parts for n in local[(p["ref"], p["unit"])]["pins"]}
    unknown = sorted(f"{r}.{n}" for (r, n) in owner if (r, n) not in known)
    require(not unknown, f"nets reference pins that do not exist on the placed symbols/units: {unknown}")
    _, power_table = library.table("power")
    power_available = set(power_table)
    power_symbols = {}
    for net in sorted(power) + ["PWR_FLAG"]:
        name = power_symbol_name(net, power_available) if net != "PWR_FLAG" else "PWR_FLAG"
        if name not in vendored:
            vendored[name] = rename(flatten(power_table, name), name)
        power_symbols[net] = f"{libname}:{name}"

    # 2. Paper and keep-outs, then placement.
    total = sum((g["body"][2] - g["body"][0] + 25) * (g["body"][3] - g["body"][1] + 25)
                for g in (placed(local[(p["ref"], p["unit"])], (0.0, 0.0), p["rot"]) for p in parts))
    paper = spec.get("paper") or next((k for k in ("A4", "A3", "A2", "A1") if total < 0.45 * PAPER[k][0] * PAPER[k][1]), "A1")
    require(paper in PAPER, f"paper must be one of {sorted(PAPER)}")
    width, height = PAPER[paper]
    area = (FRAME, FRAME, width - FRAME, height - FRAME)
    title_box = (width - FRAME - TITLE[0], height - FRAME - TITLE[1], width, height)
    flag_row = (FRAME, height - FRAME - 17.78, FRAME + 12.7 * max(1, len(flags)) + 5.08, height - FRAME) if flags else None
    reserved = [title_box] + ([flag_row] if flag_row else [])
    notes = spec.get("notes") or []
    for note in notes:
        require(isinstance(note, dict) and isinstance(note.get("text"), str) and isinstance(note.get("at"), list), "notes need text and at")
        lines = note["text"].split("\n")
        reserved.append((note["at"][0], note["at"][1] - 1.27, note["at"][0] + max(map(len, lines)) * 1.2, note["at"][1] + 2.2 * len(lines)))
    placement = auto_place(parts, local, owner, power, area, reserved)

    grid = Grid(width, height)
    for box in [title_box] + reserved[1:]:
        grid.block_box(box)
    for x in range(grid.nx):
        for y in range(grid.ny):
            if not (area[0] <= x * GRID <= area[2] and area[1] <= y * GRID <= area[3]):
                grid.blocked.add((x, y))
    geos, fields = {}, {}
    for part in parts:
        key = (part["ref"], part["unit"])
        at, rot, geo = placement[key]
        geos[key] = geo
        grid.block_box(geo["body"])
        ref_pos, val_pos, just, boxes = field_layout(geo, part["ref"], str(part.get("value", "")))
        fields[key] = (ref_pos, val_pos, just)
        for box in boxes:
            grid.block_box(box)
    pin_points = {}
    for part in parts:
        key = (part["ref"], part["unit"])
        for number, pin in geos[key]["pins"].items():
            p = gridpt(pin["point"])
            net = owner.get((part["ref"], number))
            previous = pin_points.get(p)
            if previous is not None and (previous[2] != net or net is None):
                raise ValueError(f"pins overlap at {pin['point']}: {part['ref']}.{number} and {previous[0]}.{previous[1]}")
            pin_points[p] = (part["ref"], number, net)
            for k in range(1, round(pin["length"] / GRID) + 1):  # the pin line itself is not routable
                grid.blocked.add((p[0] + pin["inward"][0] * k, p[1] + pin["inward"][1] * k))
    for p, (ref, number, net) in pin_points.items():
        grid.blocked.discard(p)
        pin = next(g["pins"][number] for (r, _), g in geos.items() if r == ref and number in g["pins"])
        grid.pins[p] = (net, direction_index(pin["outward"]))
    for p, (ref, number, net) in pin_points.items():
        out = DIRS[grid.pins[p][1]]
        escape = (p[0] + out[0], p[1] + out[1])
        grid.blocked.discard(escape)  # keep every pin's escape square open
        grid.escapes[escape] = net

    wires, junctions, labels, no_connects, power_parts, report = [], [], [], [], [], dict(labelled=[], unrouted=[])

    # 3. Power rails: a short stub from each pin to a power symbol pointing away from the part.
    def place_power(net, p, out_index, want):
        """Stub from the pin, dog-legging so GND points down and supplies point up when possible."""
        out = DIRS[out_index]
        shapes = ([(2, 2), (3, 2), (2, 3)] if out[0] != 0 else []) + [(n, 0) for n in (2, 3, 1, 4, 5)]
        for length, turn in shapes:
            path = [(p[0] + out[0] * k, p[1] + out[1] * k) for k in range(length + 1)]
            path += [(path[-1][0] + want[0] * k, path[-1][1] + want[1] * k) for k in range(1, turn + 1)]
            if not all(grid.free_point(c, own_escape=path[1]) for c in path[1:]):
                continue
            end, final = path[-1], (want if turn else out)
            side = (-final[1], final[0])
            graphic = [(end[0] + final[0] * k + side[0] * j, end[1] + final[1] * k + side[1] * j) for k in (1, 2) for j in (-1, 0, 1)]
            if not all(grid.free_point(c) for c in graphic):
                continue
            grid.commit(net, path, kind="power")
            grid.blocked.update(graphic)
            return end, final
        return p, out

    power_rot = {"GND": {(0, 1): 0, (1, 0): 90, (0, -1): 180, (-1, 0): 270},
                 "SUPPLY": {(0, -1): 0, (-1, 0): 90, (0, 1): 180, (1, 0): 270}}
    counter = [0]

    def add_power(net, point, direction):
        counter[0] += 1
        lib_id = power_symbols[net]
        kind = "GND" if re.search(r":GND|:VSS|:-", lib_id) else "SUPPLY"
        power_parts.append(dict(ref=f"#PWR{counter[0]:03d}", lib_id=lib_id, value=net, at=(point[0] * GRID, point[1] * GRID),
                                rot=power_rot[kind].get(direction, 0), direction=direction))

    for net in sorted(power):
        want = (0, 1) if re.search(r":GND|:VSS|:-", power_symbols[net]) else (0, -1)
        for ref, number in nets[net]:
            p = next(pp for pp, v in pin_points.items() if v[0] == ref and v[1] == number)
            add_power(net, *place_power(net, p, grid.pins[p][1], want))

    # 4. PWR_FLAG row (bottom-left keep-out): flag + wire + rail symbol or label.
    for i, net in enumerate(flags):
        x, y = FRAME + 7.62 + i * 12.7, height - FRAME - 12.7
        top, bottom = gridpt((round(x / GRID) * GRID, round(y / GRID) * GRID)), None
        bottom = (top[0], top[1] + 3)
        grid.commit(net, [top, (top[0], top[1] + 1), (top[0], top[1] + 2), bottom], kind="flag")
        power_parts.append(dict(ref=f"#FLG{i + 1:02d}", lib_id=power_symbols["PWR_FLAG"], value="PWR_FLAG",
                                at=(top[0] * GRID, top[1] * GRID), rot=0, direction=(0, -1)))
        if net in power:
            add_power(net, bottom, (0, 1))
        else:
            labels.append(dict(text=net, at=(bottom[0] * GRID, bottom[1] * GRID), angle=0))

    # 5. Signal nets: shortest first; each pin joins the growing tree or falls back to a label.
    def span(net):
        pts = [pp for pp, v in pin_points.items() if (v[0], v[1]) in set(nets[net])]
        return (max(p[0] for p in pts) - min(p[0] for p in pts) + max(p[1] for p in pts) - min(p[1] for p in pts)) if pts else 0

    def stub_label(net, p):
        out = DIRS[grid.pins[p][1]]
        for length in (2, 3, 1):
            path = [(p[0] + out[0] * k, p[1] + out[1] * k) for k in range(length + 1)]
            if all(grid.free_point(c, own_escape=path[1]) for c in path[1:]):
                grid.commit(net, path, kind="stub")
                end = path[-1]
                labels.append(dict(text=net, at=(end[0] * GRID, end[1] * GRID), angle={(1, 0): 0, (0, -1): 90, (-1, 0): 180, (0, 1): 270}[out]))
                return
        labels.append(dict(text=net, at=(p[0] * GRID, p[1] * GRID), angle={(1, 0): 0, (0, -1): 90, (-1, 0): 180, (0, 1): 270}[out]))

    signal = sorted((n for n in nets if n not in power), key=span)
    for net in signal:
        points = [pp for m in nets[net] for pp, v in pin_points.items() if (v[0], v[1]) == m]
        if not points:
            continue
        grid.tree.setdefault(net, set()).add(points[0])
        todo = points[1:]
        while todo:
            tree = grid.tree[net]
            todo.sort(key=lambda p: min(abs(p[0] - t[0]) + abs(p[1] - t[1]) for t in tree))
            p = todo.pop(0)
            path = grid.route(net, p, grid.pins[p][1], grid.goals(net))
            if path is None:
                report["unrouted"].append(f"{pin_points[p][0]}.{pin_points[p][1]}")
                stub_label(net, p)
                report["labelled"].append(net)
                continue
            grid.commit(net, path)
            grid.tree[net].add(p)
        if len(points) == 1:
            stub_label(net, points[0])
    # One name label per wired tree, anchored on a route endpoint: it keeps the spec name in the
    # netlist and joins any label-fallback pins or PWR_FLAG labels of the same net.
    for net in signal:
        segments = [s for s in grid.segments if s[0] == net and s[3] == "route"]
        if not segments:
            continue
        best = None
        for _, a, b, _ in segments:
            length = abs(a[0] - b[0]) + abs(a[1] - b[1])
            horizontal = a[1] == b[1]
            anchor = min(a, b) if horizontal else max(a, b, key=lambda p: p[1])
            angle = 0 if horizontal else 90
            score = (horizontal, length)
            if best is None or score > best[0]:
                best = (score, anchor, angle)
        labels.append(dict(text=net, at=(best[1][0] * GRID, best[1][1] * GRID), angle=best[2]))

    for p, (ref, number, net) in pin_points.items():
        if net is None:
            no_connects.append((p[0] * GRID, p[1] * GRID))

    # 6. Junctions where a wire ends mid-way on another wire or three or more items meet.
    ends, mids = {}, {}
    for net, a, b, _ in grid.segments:
        ends[a] = ends.get(a, 0) + 1
        ends[b] = ends.get(b, 0) + 1
        if a[0] == b[0]:
            for y in range(min(a[1], b[1]) + 1, max(a[1], b[1])):
                mids[(a[0], y)] = mids.get((a[0], y), 0) + 1
        else:
            for x in range(min(a[0], b[0]) + 1, max(a[0], b[0])):
                mids[(x, a[1])] = mids.get((x, a[1]), 0) + 1
    for p, count in ends.items():
        if (mids.get(p, 0) and count) or count + (1 if p in grid.pins else 0) >= 3:
            junctions.append((p[0] * GRID, p[1] * GRID))
    wires = [(a[0] * GRID, a[1] * GRID, b[0] * GRID, b[1] * GRID) for _, a, b, _ in grid.segments]

    # 7. Emit the schematic, the vendored symbol library and the library table.
    hide_in_effects = major < 10
    def prop(key, value, at, hidden=False, justify=None, angle=0):
        node = ["property", q(key), q(value), ["at", fmt(at[0]), fmt(at[1]), fmt(angle)]]
        effects = ["effects", ["font", ["size", "1.27", "1.27"]]]
        if justify and justify != "center":
            effects.append(["justify", justify])
        if hidden and not hide_in_effects:
            node.append(["hide", "yes"])
        if hidden and hide_in_effects:
            effects.append(["hide", "yes"])
        return node + [effects]

    def instance(lib_id, ref, value, at, rot, unit, key, mirror=None, footprint="", extra=None, ref_pos=None, val_pos=None,
                 just="left", hide_ref=False, pins=(), in_bom=True, dnp=False):
        node = ["symbol", ["lib_id", q(lib_id)], ["at", fmt(at[0]), fmt(at[1]), fmt(rot)]]
        if mirror:
            node.append(["mirror", mirror])
        node += [["unit", str(unit)]] + ([["body_style", "1"]] if major >= 10 else []) + [
            ["exclude_from_sim", "no"], ["in_bom", "yes" if in_bom else "no"], ["on_board", "yes"]]
        if major >= 10:
            node.append(["in_pos_files", "yes"])
        node += [["dnp", "yes" if dnp else "no"], ["uuid", q(uid(project, "sym", key))]]
        node.append(prop("Reference", ref, ref_pos or at, hidden=hide_ref, justify=just))
        node.append(prop("Value", value, val_pos or at, justify=just))
        node.append(prop("Footprint", footprint, at, hidden=True))
        node.append(prop("Datasheet", (extra or {}).get("Datasheet", ""), at, hidden=True))
        for name, text in (extra or {}).items():
            if name not in {"Datasheet", "Reference", "Value", "Footprint"}:
                node.append(prop(name, str(text), at, hidden=True))
        for number in pins:
            node.append(["pin", q(number), ["uuid", q(uid(project, "pin", key, number))]])
        node.append(["instances", ["project", q(project), ["path", q("/" + sheet), ["reference", q(ref)], ["unit", str(unit)]]]])
        return node

    lib_symbols = ["lib_symbols"] + [rename(node, f"{libname}:{name}") for name, node in sorted(vendored.items())]
    title = ["title_block", ["title", q(spec.get("title", project))], ["date", q(spec.get("date", ""))], ["rev", q(spec.get("rev", ""))]]
    if spec.get("company"):
        title.append(["company", q(spec["company"])])
    for i, comment in enumerate(spec.get("comments", [])[:9], 1):
        title.append(["comment", str(i), q(comment)])
    root = ["kicad_sch", ["version", version], ["generator", q("anvil")], ["generator_version", q(f"{major}.0")],
            ["uuid", q(sheet)], ["paper", q(paper)], title, lib_symbols]
    for x, y in junctions:
        root.append(["junction", ["at", fmt(x), fmt(y)], ["diameter", "0"], ["color", "0", "0", "0", "0"], ["uuid", q(uid(project, "junction", fmt(x), fmt(y)))]])
    for x, y in no_connects:
        root.append(["no_connect", ["at", fmt(x), fmt(y)], ["uuid", q(uid(project, "nc", fmt(x), fmt(y)))]])
    for x1, y1, x2, y2 in wires:
        root.append(["wire", ["pts", ["xy", fmt(x1), fmt(y1)], ["xy", fmt(x2), fmt(y2)]], ["stroke", ["width", "0"], ["type", "default"]],
                     ["uuid", q(uid(project, "wire", fmt(x1), fmt(y1), fmt(x2), fmt(y2)))]])
    for label in labels:
        justify = {0: "left bottom", 90: "left bottom", 180: "right bottom", 270: "right bottom"}[label["angle"]]
        root.append(["label", q(label["text"]), ["at", fmt(label["at"][0]), fmt(label["at"][1]), str(label["angle"])],
                     ["effects", ["font", ["size", "1.27", "1.27"]], ["justify"] + justify.split()],
                     ["uuid", q(uid(project, "label", label["text"], fmt(label["at"][0]), fmt(label["at"][1])))]])
    for i, note in enumerate(notes):
        root.append(["text", q(note["text"]), ["exclude_from_sim", "no"], ["at", fmt(note["at"][0]), fmt(note["at"][1]), "0"],
                     ["effects", ["font", ["size", "1.27", "1.27"]], ["justify", "left", "bottom"]], ["uuid", q(uid(project, "note", i))]])
    for part in parts:
        key = (part["ref"], part["unit"])
        at, rot, geo = placement[key]
        ref_pos, val_pos, just = fields[key]
        root.append(instance(lib_ids[part["symbol"]], part["ref"], str(part.get("value", "")), at, rot, part["unit"], f"{part['ref']}/{part['unit']}",
                             mirror=part.get("mirror"), footprint=part.get("footprint", ""), extra=part.get("fields"),
                             ref_pos=ref_pos, val_pos=val_pos, just=just, pins=list(geo["pins"]), in_bom=not part.get("dnp", False),
                             dnp=bool(part.get("dnp", False))))
    for pw in power_parts:
        dx, dy = pw["direction"]
        val_pos = (pw["at"][0] + dx * 3.81, pw["at"][1] + dy * 3.81 + (0.635 if dy >= 0 else 0))
        root.append(instance(pw["lib_id"], pw["ref"], pw["value"], pw["at"], pw["rot"], 1, pw["ref"], ref_pos=pw["at"], val_pos=val_pos,
                             just="center", hide_ref=True, pins=["1"]))
    root.append(["sheet_instances", ["path", q("/"), ["page", q("1")]]])
    if major >= 9:
        root.append(["embedded_fonts", "no"])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(dump(root) + "\n", encoding="utf-8")
    lib_file = out_path.parent / f"{libname}.kicad_sym"
    lib_root = ["kicad_symbol_lib", ["version", library.version or "20241209"], ["generator", q("anvil")],
                ["generator_version", q(f"{major}.0")]] + [node for _, node in sorted(vendored.items())]
    lib_file.write_text(dump(lib_root) + "\n", encoding="utf-8")
    table_path = out_path.parent / "sym-lib-table"
    entry = f'  (lib (name "{libname}")(type "KiCad")(uri "${{KIPRJMOD}}/{lib_file.name}")(options "")(descr "Anvil vendored symbols"))'
    if table_path.is_file():
        text = table_path.read_text(encoding="utf-8")
        if f'(name "{libname}")' not in text:
            table_path.write_text(text.rstrip().rstrip(")") + "\n" + entry + "\n)\n", encoding="utf-8")
    else:
        table_path.write_text("(sym_lib_table\n  (version 7)\n" + entry + "\n)\n", encoding="utf-8")
    link_footprint_libraries(out_path.parent, {p["footprint"].partition(":")[0] for p in parts if ":" in (p.get("footprint") or "")}, major)
    pro = out_path.with_suffix(".kicad_pro")
    if not pro.exists():
        write_json(pro, {"meta": {"filename": pro.name, "version": 3}, "schematic": {"legacy_lib_dir": "", "legacy_lib_list": []}})

    total_links = sum(max(0, len(m) - 1) for n, m in nets.items() if n not in power)
    summary = dict(schema_version=1, schematic=out_path.name, paper=paper, kicad_major=major, parts=len(parts),
                   nets=len(nets), power_nets=sorted(power), wires=len(wires), junctions=len(junctions),
                   power_symbols=sum(1 for p in power_parts if p["ref"].startswith("#PWR")), labels=len(labels),
                   no_connects=len(no_connects), signal_links=total_links, unrouted_links=len(report["unrouted"]),
                   unrouted=report["unrouted"], wired_fraction=round(1 - len(report["unrouted"]) / total_links, 4) if total_links else 1.0,
                   crossings=sum(1 for p, n in grid.through.items() if len(n) > 1))
    if verify:
        summary.update(prove(out_path, nets, owner))
    write_json(out_path.with_suffix(".wiring.json"), summary)
    DETAILS.append(f"SCHEMATIC: {out_path} parts={len(parts)} wires={len(wires)} unrouted={len(report['unrouted'])} "
                   f"netlist_match={summary.get('netlist_match')} erc_errors={summary.get('erc_errors')}")
    ok = summary.get("netlist_match", True) and summary.get("erc_errors", 0) == 0
    return f"SCHEMATIC: {summary['wires']} wires, {summary['unrouted_links']}/{total_links} links labelled, " \
           f"netlist {'MATCH' if summary.get('netlist_match') else 'MISMATCH' if verify else 'unverified'}", ok


# --- proof: KiCad reload, fresh netlist export, ERC ---------------------------------------------------------
def prove(schematic, nets, owner):
    import anvil_netlist  # local import: sibling module
    tool = executable("kicad-cli")
    upgrade = execute([tool, "sch", "upgrade", "--force", str(schematic)], cwd=schematic.parent)
    require(upgrade.returncode == 0, f"KiCad could not load/re-save the generated schematic: {upgrade.stdout[-500:]}")
    exported, parts, _, _ = anvil_netlist.export_netlist(schematic)
    problems = compare(exported, nets)
    report = schematic.with_suffix(".erc.json")
    kicad("erc", schematic, report)
    data = read_json(report)
    counts = {}
    for sheet in data.get("sheets", []):
        for violation in sheet.get("violations", []):
            key = f"{violation.get('severity')}:{violation.get('type')}"
            counts[key] = counts.get(key, 0) + 1
    return dict(netlist_match=not problems, netlist_problems=problems, erc=counts,
                erc_errors=sum(v for k, v in counts.items() if k.startswith("error:")),
                erc_warnings=sum(v for k, v in counts.items() if k.startswith("warning:")))


def compare(exported, nets):
    """Exact membership comparison of an exported netlist against the golden spec nets."""
    member_net = {m: name for name, members in exported.items() for m in members}
    problems = []
    for name, members in nets.items():
        found = {member_net.get(m) for m in members}
        if None in found:
            problems.append(f"{name}: pins missing from the netlist {[f'{r}.{p}' for r, p in members if member_net.get((r, p)) is None]}")
            continue
        if len(found) > 1:
            problems.append(f"{name}: split across nets {sorted(found)}")
            continue
        actual = exported[found.pop()]
        extra = sorted(f"{r}.{p}" for r, p in actual - set(members))
        if extra:
            problems.append(f"{name}: unexpected pins joined {extra}")
    for name, members in exported.items():
        if len(members) > 1 and not any(set(m) <= members for m in nets.values() if m):
            problems.append(f"unexpected net {name}: {sorted(f'{r}.{p}' for r, p in members)}")
    return problems


# --- convert an existing (label-connected) schematic into a circuit spec ----------------------------------
def spec_from_schematic(schematic, out_spec):
    import anvil_netlist
    schematic, out_spec = Path(schematic).resolve(), Path(out_spec).resolve()
    root = parse(read(schematic))
    require(root[0] == "kicad_sch", "not a KiCad schematic")
    parts, flags = [], set()
    for sym in children(root, "symbol"):
        lib_id = unq(child(sym, "lib_id")[1])
        props = {unq(p[1]): unq(p[2]) for p in children(sym, "property")}
        at = child(sym, "at")
        ref = props.get("Reference", "")
        if ref.startswith("#"):
            continue
        unit = int(child(sym, "unit")[1]) if child(sym, "unit") else 1
        rot = int(float(at[3])) % 360 if len(at) > 3 else 0
        mirror = child(sym, "mirror")
        part = dict(ref=ref, symbol=lib_id, value=props.get("Value", ""), footprint=props.get("Footprint", ""), unit=unit,
                    at=[round(float(at[1]) / GRID) * GRID, round(float(at[2]) / GRID) * GRID], rot=rot)
        if mirror:
            part["mirror"] = mirror[1]
        extra = {k: v for k, v in props.items() if k not in {"Reference", "Value", "Footprint", "Description"} and v}
        if extra:
            part["fields"] = extra
        parts.append(part)
    _, _, _, text = anvil_netlist.export_netlist(schematic)
    import xml.etree.ElementTree as ET
    nets = {}
    for net in ET.fromstring(text).findall("./nets/net"):
        members = [(n.get("ref"), n.get("pin")) for n in net.findall("node")]
        types = {n.get("pintype", "") for n in net.findall("node")}
        # KiCad's netlist omits PWR_FLAG symbols; re-flag exactly the nets ERC would call undriven.
        if "power_in" in types and "power_out" not in types:
            flags.add(net.get("name").lstrip("/"))
        physical = [f"{r}.{p}" for r, p in members if not r.startswith("#")]
        if len(physical) >= 1 and not net.get("name").startswith("unconnected-"):
            nets[net.get("name").lstrip("/")] = physical
    title = child(root, "title_block")
    spec = dict(schema_version=1, project=schematic.stem, title=unq(child(title, "title")[1]) if title and child(title, "title") else schematic.stem,
                rev=unq(child(title, "rev")[1]) if title and child(title, "rev") else "",
                date=unq(child(title, "date")[1]) if title and child(title, "date") else "",
                comments=[unq(c[2]) for c in children(title, "comment") if unq(c[2])] if title else [],
                libraries={nick: os.path.relpath(schematic, out_spec.parent).replace("\\", "/") for nick in {p["symbol"].partition(":")[0] for p in parts}},
                parts=parts, nets=nets, pwr_flag=sorted(flags & set(nets)))
    write_json(out_spec, spec)
    return f"CIRCUIT_SPEC: {out_spec} ({len(parts)} parts, {len(nets)} nets) from {schematic.name}"
