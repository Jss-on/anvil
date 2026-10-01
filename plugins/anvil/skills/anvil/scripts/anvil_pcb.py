#!/usr/bin/env python3
"""KiCad board access through KiCad's own Python (pcbnew): exact geometry dump, zone fill,
Specctra export/import for autorouting. Run by `anvil.py` with the interpreter bundled with KiCad.

Only layer-qualified pcbnew calls are used: KiCad 10 raises blocking assert dialogs for
padstack/via queries made without a layer, so every such call names its copper layer.
Coordinates in the dump are millimetres in KiCad board space (x right, y down).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from anvil_schematic import child, children, parse, unq  # noqa: E402  (stdlib-only s-expression reader)


def stackup(board_path):
    """Physical stackup from the board file (the pcbnew stackup binding is not usable in KiCad 10)."""
    root = parse(Path(board_path).read_text(encoding="utf-8"))
    setup = child(root, "setup")
    node = child(setup, "stackup") if setup else None
    if node is None:
        return None
    layers = []
    for item in children(node, "layer"):
        entry = dict(name=unq(item[1]))
        for key in ("type", "material", "color"):
            if child(item, key):
                entry[key] = unq(child(item, key)[1])
        for key in ("thickness", "epsilon_r", "loss_tangent"):
            if child(item, key):
                entry[key] = float(unq(child(item, key)[1]))
        layers.append(entry)
    finish = child(node, "copper_finish")
    return dict(layers=layers, copper_finish=unq(finish[1]) if finish else None)


def dump(board_path, out_path):
    import pcbnew as p

    board = p.LoadBoard(str(board_path))
    mm = p.ToMM
    name = board.GetLayerName
    copper = [layer for layer in board.GetEnabledLayers().CuStack()]
    zones = list(board.Zones())
    if zones:
        p.ZONE_FILLER(board).Fill(board.Zones())  # measure the copper fabrication will get (not saved)

    def poly(shape_set):
        outlines = []
        for i in range(shape_set.OutlineCount()):
            ring = shape_set.Outline(i)
            holes = [[(mm(shape_set.Hole(i, h).CPoint(k).x), mm(shape_set.Hole(i, h).CPoint(k).y))
                      for k in range(shape_set.Hole(i, h).PointCount())] for h in range(shape_set.HoleCount(i))]
            outlines.append(dict(outline=[(mm(ring.CPoint(k).x), mm(ring.CPoint(k).y)) for k in range(ring.PointCount())], holes=holes))
        return outlines

    tracks, vias, arcs = [], [], []
    for item in board.GetTracks():
        kind = type(item).__name__
        if kind == "PCB_VIA":
            vias.append(dict(net=item.GetNetname(), x=mm(item.GetPosition().x), y=mm(item.GetPosition().y),
                             diameter=mm(item.GetWidth(item.TopLayer())), drill=mm(item.GetDrillValue()),
                             top=name(item.TopLayer()), bottom=name(item.BottomLayer())))
        elif kind == "PCB_ARC":
            arcs.append(dict(net=item.GetNetname(), layer=name(item.GetLayer()), width=mm(item.GetWidth()),
                             start=(mm(item.GetStart().x), mm(item.GetStart().y)), mid=(mm(item.GetMid().x), mm(item.GetMid().y)),
                             end=(mm(item.GetEnd().x), mm(item.GetEnd().y))))
        else:
            tracks.append(dict(net=item.GetNetname(), layer=name(item.GetLayer()), width=mm(item.GetWidth()),
                               start=(mm(item.GetStart().x), mm(item.GetStart().y)), end=(mm(item.GetEnd().x), mm(item.GetEnd().y))))
    footprints, pads = [], []
    for fp in board.Footprints():
        ref = fp.GetReference()
        side = name(fp.GetLayer())
        court = fp.GetCourtyard(p.F_CrtYd if side == "F.Cu" else p.B_CrtYd)
        bbox = fp.GetBoundingBox(False)
        footprints.append(dict(ref=ref, value=fp.GetValue(), footprint=str(fp.GetFPID().GetLibItemName()),
                               x=mm(fp.GetPosition().x), y=mm(fp.GetPosition().y), rotation=fp.GetOrientationDegrees(),
                               side=side, courtyard=poly(court) if court.OutlineCount() else [],
                               bbox=(mm(bbox.GetLeft()), mm(bbox.GetTop()), mm(bbox.GetRight()), mm(bbox.GetBottom()))))
        for pad in fp.Pads():
            layers = [name(l) for l in pad.GetLayerSet().CuStack() if l in copper]
            attribute = {0: "pth", 1: "smd", 2: "conn", 3: "npth"}.get(pad.GetAttribute(), str(pad.GetAttribute()))
            shapes = {}
            for layer_id in [l for l in pad.GetLayerSet().CuStack() if l in copper]:
                shapes[name(layer_id)] = poly(pad.GetEffectivePolygon(layer_id, p.ERROR_INSIDE))
                if attribute in {"pth", "npth"}:
                    break  # plated/unplated through pads share one copper shape here
            drill = pad.GetDrillSize()
            pads.append(dict(ref=ref, number=pad.GetNumber(), net=pad.GetNetname(), attribute=attribute,
                             x=mm(pad.GetPosition().x), y=mm(pad.GetPosition().y), layers=layers,
                             drill=(mm(drill.x), mm(drill.y)), shapes=shapes))
    zone_list = []
    for zone in zones:
        layers = [name(l) for l in zone.GetLayerSet().Seq()]
        entry = dict(net=zone.GetNetname(), layers=layers, rule_area=bool(zone.GetIsRuleArea()),
                     outline=poly(zone.Outline()), clearance=mm(zone.GetLocalClearance() or 0) if hasattr(zone, "GetLocalClearance") else None)
        if zone.GetIsRuleArea():
            entry["keepout"] = dict(tracks=zone.GetDoNotAllowTracks(), vias=zone.GetDoNotAllowVias(), pads=zone.GetDoNotAllowPads(),
                                    copper_pour=zone.GetDoNotAllowZoneFills(), footprints=zone.GetDoNotAllowFootprints())
        else:
            entry["filled"] = {name(l): poly(zone.GetFilledPolysList(l)) for l in zone.GetLayerSet().Seq()}
        zone_list.append(entry)
    edges = p.SHAPE_POLY_SET()
    board.GetBoardPolygonOutlines(edges, True)
    data = dict(schema_version=1, board=Path(board_path).name, kicad=p.Version(), copper_layers=[name(l) for l in copper],
                thickness=mm(board.GetDesignSettings().GetBoardThickness()), stackup=stackup(board_path),
                nets=sorted({board.GetNetInfo().GetNetItem(i).GetNetname() for i in range(board.GetNetCount())} - {""}),
                tracks=tracks, arcs=arcs, vias=vias, footprints=footprints, pads=pads, zones=zone_list, outline=poly(edges))
    Path(out_path).write_text(json.dumps(data, indent=1), encoding="utf-8")
    print(f"DUMP: {len(tracks)} tracks, {len(arcs)} arcs, {len(vias)} vias, {len(pads)} pads, {len(zone_list)} zones -> {out_path}")


def library_paths(tables, footprint_dir):
    """Footprint library nickname -> .pretty path from fp-lib-table files (later tables override)."""
    libs = {}
    for table_path in tables:
        if not Path(table_path).is_file():
            continue
        for lib in children(parse(Path(table_path).read_text(encoding="utf-8")), "lib"):
            uri = unq(child(lib, "uri")[1])
            for var in ("KICAD10_FOOTPRINT_DIR", "KICAD9_FOOTPRINT_DIR", "KICAD8_FOOTPRINT_DIR", "KICAD_FOOTPRINT_DIR"):
                uri = uri.replace("${" + var + "}", footprint_dir)
            uri = uri.replace("${KIPRJMOD}", str(Path(table_path).parent))
            libs[unq(child(lib, "name")[1])] = uri
    return libs


def read_placement(path):
    return {row["ref"]: row for row in read_table(path)} if path and path != "-" else {}


def apply_placement(p, board, rows):
    for ref, row in rows.items():
        fp = board.FindFootprintByReference(ref)
        if fp is None:
            raise SystemExit(f"placement names {ref}, which is not on the board")
        want_back = row.get("side", "F").upper().startswith("B")
        if want_back != (fp.GetLayer() == p.B_Cu):
            fp.Flip(fp.GetPosition(), p.FLIP_DIRECTION_TOP_BOTTOM)
        fp.SetPosition(p.VECTOR2I(p.FromMM(float(row["x_mm"])), p.FromMM(float(row["y_mm"]))))
        fp.SetOrientationDegrees(float(row.get("rot_deg") or 0))


def shelf(p, board, footprints, gap=1.0):
    """Deterministic first placement: largest parts first, in rows inside the board outline."""
    edges = p.SHAPE_POLY_SET()
    board.GetBoardPolygonOutlines(edges, True)
    box = edges.BBox()
    x0, y0, x1 = p.ToMM(box.GetLeft()) + gap, p.ToMM(box.GetTop()) + gap, p.ToMM(box.GetRight()) - gap
    x, y, row_h = x0, y0, 0.0
    for fp in sorted(footprints, key=lambda f: -(p.ToMM(f.GetBoundingBox(False).GetWidth()) * p.ToMM(f.GetBoundingBox(False).GetHeight()))):
        bb = fp.GetBoundingBox(False)
        w, h = p.ToMM(bb.GetWidth()), p.ToMM(bb.GetHeight())
        if x + w > x1 and x > x0:
            x, y, row_h = x0, y + row_h + gap, 0.0
        dx, dy = p.ToMM(fp.GetPosition().x) - p.ToMM(bb.GetLeft()), p.ToMM(fp.GetPosition().y) - p.ToMM(bb.GetTop())
        fp.SetPosition(p.VECTOR2I(p.FromMM(x + dx), p.FromMM(y + dy)))
        x, row_h = x + w + gap, max(row_h, h)


def build(netlist_path, template_path, out_path, placement_path, footprint_dir, *tables):
    """Footprints and nets from a KiCad XML netlist onto a template board (outline, stackup, rules)."""
    import xml.etree.ElementTree as ET
    import pcbnew as p

    board = p.LoadBoard(str(template_path))
    libs = library_paths(tables, footprint_dir)
    root = ET.parse(netlist_path).getroot()
    added = []
    for comp in root.iter("comp"):
        ref = comp.get("ref")
        excluded = any(prop.get("name") == "exclude_from_board" for prop in comp.iter("property"))
        if ref.startswith("#") or excluded or board.FindFootprintByReference(ref) is not None:
            continue
        fpid = (comp.findtext("footprint") or "").strip()
        if ":" not in fpid:
            raise SystemExit(f"{ref} has no footprint (Library:Name) in the schematic")
        lib, name = fpid.split(":", 1)
        if lib not in libs and Path(footprint_dir, f"{lib}.pretty").is_dir():
            libs[lib] = str(Path(footprint_dir, f"{lib}.pretty"))  # stock KiCad library (what KiCad's default table maps)
        if lib not in libs:
            raise SystemExit(f"{ref}: footprint library {lib} is not in any fp-lib-table")
        fp = p.FootprintLoad(libs[lib], name)
        if fp is None:
            raise SystemExit(f"{ref}: footprint {fpid} not found in {libs[lib]}")
        fp.SetFPID(p.LIB_ID(lib, name))  # keep the library nickname: DRC schematic parity compares it
        fp.SetReference(ref)
        fp.SetValue(comp.findtext("value") or "")
        sheet = comp.find("sheetpath")
        stamp = (comp.findtext("tstamps") or "").split()
        if sheet is not None and stamp:  # link footprint to its symbol like "Update PCB from Schematic"
            fp.SetPath(p.KIID_PATH(sheet.get("tstamps", "/").rstrip("/") + "/" + stamp[0]))
        for prop in comp.iter("property"):
            if prop.get("name") == "Sheetname" and hasattr(fp, "SetSheetname"):
                fp.SetSheetname(prop.get("value") or "")
            if prop.get("name") == "Sheetfile" and hasattr(fp, "SetSheetfile"):
                fp.SetSheetfile(prop.get("value") or "")
        board.Add(fp)
        added.append(fp)
    for net in root.iter("net"):
        name = net.get("name")
        info = board.FindNet(name)
        if info is None:
            info = p.NETINFO_ITEM(board, name)
            board.Add(info)
        for node in net.iter("node"):
            fp = board.FindFootprintByReference(node.get("ref"))
            if fp is None:
                continue
            for pad in fp.Pads():  # every pad with the pin number (exposed pads share numbers)
                if pad.GetNumber() == node.get("pin"):
                    pad.SetNet(info)
    placement = read_placement(placement_path)
    shelf(p, board, [f for f in added if f.GetReference() not in placement])
    apply_placement(p, board, placement)
    p.ZONE_FILLER(board).Fill(board.Zones())
    p.SaveBoard(str(out_path), board)
    print(f"BOARD: {len(added)} footprints, {len(list(root.iter('net')))} nets -> {out_path}")


def add_routes(p, board, path):
    """Pre-routed critical copper from routes.tsv (kind, net, layer, width_mm, x1, y1, x2, y2, drill_mm), locked so
    the autorouter keeps it: `track` rows are segments, `via` rows are through vias at (x1, y1). Earlier
    locked copper of the same nets is replaced, so re-running with an edited table is idempotent."""
    rows = [r for r in read_table(path)]
    found = {}
    for name in {r["net"] for r in rows}:  # sheet-local nets carry KiCad's "/" prefix on the board
        found[name] = board.FindNet(name) or board.FindNet("/" + name)
        if found[name] is None:
            raise SystemExit(f"routes.tsv names net {name}, which is not on the board")
    names = {n.GetNetname() for n in found.values()}
    for item in [t for t in board.GetTracks() if t.IsLocked() and t.GetNetname() in names]:
        board.Remove(item)
    mm = p.FromMM
    for r in rows:
        net = found[r["net"]]
        if r["kind"] == "track":
            t = p.PCB_TRACK(board)
            t.SetStart(p.VECTOR2I(mm(float(r["x1"])), mm(float(r["y1"]))))
            t.SetEnd(p.VECTOR2I(mm(float(r["x2"])), mm(float(r["y2"]))))
            t.SetWidth(mm(float(r["width_mm"])))
            t.SetLayer(board.GetLayerID(r["layer"]))
        elif r["kind"] == "via":
            t = p.PCB_VIA(board)
            t.SetPosition(p.VECTOR2I(mm(float(r["x1"])), mm(float(r["y1"]))))
            t.SetLayerPair(p.F_Cu, p.B_Cu)
            t.SetWidth(p.F_Cu, mm(float(r["width_mm"])))
            t.SetDrill(mm(float(r["drill_mm"])))
        else:
            raise SystemExit(f"routes.tsv kind must be track or via, not {r['kind']}")
        t.SetNet(net)
        t.SetLocked(True)
        board.Add(t)
    return len(rows)


def read_table(path):
    lines = [l for l in Path(path).read_text(encoding="utf-8").splitlines() if l.strip() and not l.lstrip().startswith("#")]
    head = lines[0].split("\t")
    return [dict(zip(head, [c.strip() for c in line.split("\t")])) for line in lines[1:]]


def place(board_path, placement_path, routes_path="-"):
    import pcbnew as p

    board = p.LoadBoard(str(board_path))
    rows = read_placement(placement_path)
    apply_placement(p, board, rows)
    routed = add_routes(p, board, routes_path) if routes_path and routes_path != "-" else 0
    p.ZONE_FILLER(board).Fill(board.Zones())
    p.SaveBoard(str(board_path), board)
    print(f"PLACED: {len(rows)} footprints, {routed} pre-routed items in {board_path}")


def fill(board_path):
    import pcbnew as p

    board = p.LoadBoard(str(board_path))
    p.ZONE_FILLER(board).Fill(board.Zones())
    p.SaveBoard(str(board_path), board)
    print(f"FILLED: {len(list(board.Zones()))} zones in {board_path}")


def export_dsn(board_path, dsn_path):
    import pcbnew as p

    board = p.LoadBoard(str(board_path))
    if not p.ExportSpecctraDSN(board, str(dsn_path)):
        raise SystemExit("Specctra DSN export failed")
    print(f"DSN: {dsn_path}")


def import_ses(board_path, ses_path):
    import pcbnew as p

    board = p.LoadBoard(str(board_path))
    if not p.ImportSpecctraSES(board, str(ses_path)):
        raise SystemExit("Specctra SES import failed")
    p.ZONE_FILLER(board).Fill(board.Zones())
    p.SaveBoard(str(board_path), board)
    print(f"SES: imported {ses_path} into {board_path}")


if __name__ == "__main__":
    command, *args = sys.argv[1:]
    {"dump": dump, "fill": fill, "export-dsn": export_dsn, "import-ses": import_ses, "build": build, "place": place}[command](*args)
