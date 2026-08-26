#!/usr/bin/env bash
# score-anvil.sh — scoring backend for anvil (hardware: requirements → PCB).
#
#   pass-rate [results.tsv]              → weighted acceptance pass-rate      "PASS_RATE: 0.NN"
#   coverage  [results.tsv] [hrs.md]     → HRS traceability (RTM gate)        "REQ_COVERAGE: 0.NN"
#   erc       <sch> [out.json]           → KiCad ERC violation count          "ERC_VIOLATIONS: N"
#   drc       <pcb> [out.json]           → KiCad DRC (+parity+deck) count     "DRC_VIOLATIONS: N"
#   sim       [sim-dir]                  → run ngspice harnesses, assert      "SIM_PASS: x/y"
#   bom-cost  <bom.csv> <catalog.csv>    → pinned-catalog BOM roll-up         "BOM_COST: X.XX CUR"
#   area      <pcb>                      → Edge.Cuts bounding-box area        "AREA_MM2: N.N"
#   mesh      <file.stl>                 → STL watertight/manifold defects    "MESH_DEFECTS: N"
#   fit       <mech-dir>                 → fit-class assertions (clearances)  "FIT_PASS: x/y"
#   mass      <mech-dir>                 → mass-class assertions (budget)     "MASS_PASS: x/y"
#   mech-dfm  <mech-dir>                 → dfm-class assertions (+slicer)     "DFM_PASS: x/y"
#   pinout    <harness.tsv> <icd.tsv> [mates.tsv] → wiring consistency        "PINOUT_VIOLATIONS: N"
#   product-bom <product-bom.csv>        → full-unit rollup (cost+mass)       "PRODUCT_COST: X.XX CUR"
#   verdict   [results.tsv] [hrs.md]     → FAB_READY | FAB_BLOCKED
#
# fit/mass/mech-dfm evaluate <mech-dir>/assertions.tsv rows (cols: id class measure op limit
#   units traces; class selects the gate; op grammar identical to sim) against kernel-emitted
#   <mech-dir>/measures.json — see references/mechanical-protocol.md.
#
# pass-rate (higher_is_better):
#   - six dimensions, weights renormalized over the dims that actually ran:
#       electrical 0.30 · simulation 0.25 · layout 0.20 · manufacturing 0.15
#       · testability 0.10 · documentation 0.10
#   - ELECTRICAL GATE: while ANY `electrical` row is red, the headline rate is capped at
#     ELECTRICAL_GATE_CAP (default 0.50) — wrong electricity can't be polished over.
#   - per-dimension score = sum(weight of pass) / sum(weight of pass|fail); skip excluded.
#   - no measurable rows → PASS_RATE: 0.00 (honest baseline).
#   - STDOUT is exactly one line; breakdown goes to STDERR.
#   - exit 0 on well-formed input (a red baseline is valid data); exit 2 on hard error only.
#
# sim: executes every sim-dir/*.cir via `ngspice -b` (skipped when ngspice is absent or
#   SKIP_NGSPICE=1 — then existing .log files are parsed), then evaluates sim-dir/assertions.tsv
#   (cols: id measure op limit units corners traces; op ∈ le|ge|within; within takes
#   "center±pct%", "center±abs", or "lo..hi"). A `.step` corner sweep emits multiple measure
#   lines — a row passes only if EVERY emitted value passes; margin = worst distance to a bound.
#
# Overridable env: ANVIL_RESULTS, HRS_MD, ELECTRICAL_GATE_CAP, TARGET_RATE, KICAD_CLI,
#   ANVIL_W_ELECTRICAL, ANVIL_W_SIMULATION, ANVIL_W_LAYOUT, ANVIL_W_MANUFACTURING,
#   ANVIL_W_TESTABILITY, ANVIL_W_DOCUMENTATION
set -uo pipefail
export LC_ALL=C

ANVIL_W_ELECTRICAL="${ANVIL_W_ELECTRICAL:-0.30}"
ANVIL_W_SIMULATION="${ANVIL_W_SIMULATION:-0.25}"
ANVIL_W_LAYOUT="${ANVIL_W_LAYOUT:-0.20}"
ANVIL_W_MANUFACTURING="${ANVIL_W_MANUFACTURING:-0.15}"
ANVIL_W_TESTABILITY="${ANVIL_W_TESTABILITY:-0.10}"
ANVIL_W_DOCUMENTATION="${ANVIL_W_DOCUMENTATION:-0.10}"
ELECTRICAL_GATE_CAP="${ELECTRICAL_GATE_CAP:-0.50}"

die() { echo "score-anvil: $*" >&2; exit 2; }

find_kicad() {
  if [[ -n "${KICAD_CLI:-}" && -x "${KICAD_CLI:-}" ]]; then echo "$KICAD_CLI"; return 0; fi
  if command -v kicad-cli >/dev/null 2>&1; then echo "kicad-cli"; return 0; fi
  local g
  for g in "/c/Program Files/KiCad/"*/bin/kicad-cli.exe; do
    [[ -x "$g" ]] && { echo "$g"; return 0; }
  done
  return 1
}

# ---------------------------------------------------------------------------
# embedded node helpers (JSON / CSV / s-expr parsing seam)
# ---------------------------------------------------------------------------
NODE_VCOUNT=$(cat <<'EOF'
const fs = require('fs');
const j = JSON.parse(fs.readFileSync(process.argv[1], 'utf8'));
let n = 0;
(function walk(o) {
  if (Array.isArray(o)) { o.forEach(walk); return; }
  if (o && typeof o === 'object') {
    if (typeof o.severity === 'string' && (o.type !== undefined || o.description !== undefined)) n++;
    for (const k of Object.keys(o)) walk(o[k]);
  }
})(j);
console.log(n);
EOF
)

NODE_SIM=$(cat <<'EOF'
const fs = require('fs'), path = require('path');
const dir = process.argv[1];
const af = path.join(dir, 'assertions.tsv');
if (!fs.existsSync(af)) { console.error('missing ' + af); process.exit(2); }
const rows = fs.readFileSync(af, 'utf8').split(/\r?\n/).filter(l => l.trim() && !l.startsWith('#'));
const logs = fs.readdirSync(dir).filter(f => f.endsWith('.log'))
  .map(f => fs.readFileSync(path.join(dir, f), 'utf8')).join('\n');
let pass = 0, total = 0;
for (const line of rows) {
  const c = line.split('\t');
  if (c[0] === 'id') continue;
  const [id, meas, op, limit, units] = c;
  if (!id || !meas) continue;
  total++;
  const re = new RegExp('^\\s*' + meas.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\s*=\\s*([-+0-9.eE]+)', 'gmi');
  const vals = []; let m;
  while ((m = re.exec(logs))) vals.push(parseFloat(m[1]));
  if (!vals.length) { console.error(id + ' FAIL no measure "' + meas + '" emitted'); continue; }
  let lo = -Infinity, hi = Infinity, mm;
  const lim = (limit || '').replace(/\s/g, '');
  if (op === 'le') hi = parseFloat(lim);
  else if (op === 'ge') lo = parseFloat(lim);
  else if (op === 'within') {
    if ((mm = lim.match(/^([-+0-9.eE]+)(?:±|\+-|\+\/-)([-+0-9.eE]+)%$/))) { const ctr = +mm[1], p = +mm[2] / 100; lo = ctr * (1 - p); hi = ctr * (1 + p); }
    else if ((mm = lim.match(/^([-+0-9.eE]+)(?:±|\+-|\+\/-)([-+0-9.eE]+)$/))) { lo = +mm[1] - +mm[2]; hi = +mm[1] + +mm[2]; }
    else if ((mm = lim.match(/^([-+0-9.eE]+)\.\.([-+0-9.eE]+)$/))) { lo = +mm[1]; hi = +mm[2]; }
    else { console.error(id + ' FAIL unparseable within-limit "' + limit + '"'); continue; }
  } else { console.error(id + ' FAIL unknown op "' + op + '"'); continue; }
  if (isNaN(lo) || isNaN(hi)) { console.error(id + ' FAIL unparseable limit "' + limit + '"'); continue; }
  const bad = vals.filter(v => v < lo || v > hi);
  let margin = Infinity;
  for (const v of vals) { const d = Math.min(v - lo, hi - v); if (d < margin) margin = d; }
  if (bad.length) console.error(`${id} FAIL worst=${bad[0]} bounds=[${lo},${hi}] ${units || ''} over ${vals.length} corner value(s)`);
  else { pass++; console.error(`${id} PASS margin=${margin.toPrecision(4)} ${units || ''} over ${vals.length} corner value(s)`); }
}
console.log(`SIM_PASS: ${pass}/${total}`);
EOF
)

NODE_BOM=$(cat <<'EOF'
const fs = require('fs');
function csv(text) {
  const rows = []; let row = [], cur = '', q = false;
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (q) { if (ch === '"') { if (text[i + 1] === '"') { cur += '"'; i++; } else q = false; } else cur += ch; }
    else if (ch === '"') q = true;
    else if (ch === ',') { row.push(cur); cur = ''; }
    else if (ch === '\n') { row.push(cur.replace(/\r$/, '')); rows.push(row); row = []; cur = ''; }
    else cur += ch;
  }
  if (cur !== '' || row.length) { row.push(cur.replace(/\r$/, '')); rows.push(row); }
  return rows.filter(r => r.length > 1 || (r[0] && r[0].trim()));
}
const bom = csv(fs.readFileSync(process.argv[1], 'utf8'));
const cat = csv(fs.readFileSync(process.argv[2], 'utf8'));
const bh = bom[0].map(h => h.toLowerCase());
const chh = cat[0].map(h => h.toLowerCase());
const bMpn = bh.findIndex(h => h.includes('mpn') || h.includes('part number'));
const bQty = bh.findIndex(h => h === 'qty' || h.includes('quantity'));
const cMpn = chh.findIndex(h => h === 'mpn');
const cPrice = chh.findIndex(h => h.includes('unit_price') || h.includes('price'));
const cCur = chh.findIndex(h => h.includes('currency'));
if (bMpn < 0 || bQty < 0 || cMpn < 0 || cPrice < 0) { console.error('missing columns (bom: MPN,Qty; catalog: mpn,unit_price)'); process.exit(2); }
const price = {}; let currency = 'USD';
for (const r of cat.slice(1)) { if (!r[cMpn]) continue; price[r[cMpn]] = parseFloat(r[cPrice]); if (cCur >= 0 && r[cCur]) currency = r[cCur]; }
let total = 0; const missing = [];
for (const r of bom.slice(1)) {
  const mpn = r[bMpn];
  if (!mpn || /^dnp$/i.test(mpn.trim())) continue;
  const qty = parseFloat(r[bQty]) || 0;
  if (!(mpn in price)) { missing.push(mpn); continue; }
  total += qty * price[mpn];
  console.error(`${mpn} x${qty} @ ${price[mpn]} = ${(qty * price[mpn]).toFixed(2)}`);
}
if (missing.length) { console.error('NOT IN PINNED CATALOG: ' + missing.join(', ')); process.exit(2); }
console.log(`BOM_COST: ${total.toFixed(2)} ${currency}`);
EOF
)

NODE_AREA=$(cat <<'EOF'
const fs = require('fs');
const src = fs.readFileSync(process.argv[1], 'utf8');
const toks = []; let i = 0;
while (i < src.length) {
  const c = src[i];
  if (c === '(' || c === ')') { toks.push(c); i++; }
  else if (/\s/.test(c)) i++;
  else if (c === '"') { let j = i + 1, s = ''; while (j < src.length && src[j] !== '"') { if (src[j] === '\\') j++; s += src[j]; j++; } toks.push({ str: s }); i = j + 1; }
  else { let j = i; while (j < src.length && !/[\s()"]/.test(src[j])) j++; toks.push(src.slice(i, j)); i = j; }
}
let p = 0;
function parse() { const out = []; p++; while (p < toks.length && toks[p] !== ')') { if (toks[p] === '(') out.push(parse()); else { out.push(toks[p]); p++; } } p++; return out; }
while (p < toks.length && toks[p] !== '(') p++;
if (p >= toks.length) { console.error('not an s-expression file'); process.exit(2); }
const tree = parse();
let minx = Infinity, miny = Infinity, maxx = -Infinity, maxy = -Infinity, found = false;
const sval = t => (t && typeof t === 'object' && 'str' in t) ? t.str : t;
function isEdge(node) { return node.some(ch => Array.isArray(ch) && ch[0] === 'layer' && sval(ch[1]) === 'Edge.Cuts'); }
function coords(node, acc) {
  for (const ch of node) if (Array.isArray(ch)) {
    if (['start', 'end', 'mid', 'center', 'xy'].includes(ch[0])) { const x = parseFloat(ch[1]), y = parseFloat(ch[2]); if (isFinite(x) && isFinite(y)) acc.push([x, y]); }
    coords(ch, acc);
  }
}
function walk(node) {
  if (!Array.isArray(node)) return;
  if (typeof node[0] === 'string' && isEdge(node)) {
    const acc = []; coords(node, acc);
    if (node[0] === 'gr_circle' || node[0] === 'circle') {
      let c = null, e = null;
      for (const ch of node) if (Array.isArray(ch)) { if (ch[0] === 'center') c = [+ch[1], +ch[2]]; if (ch[0] === 'end') e = [+ch[1], +ch[2]]; }
      if (c && e) { const r = Math.hypot(e[0] - c[0], e[1] - c[1]); acc.push([c[0] - r, c[1] - r], [c[0] + r, c[1] + r]); }
    }
    for (const [x, y] of acc) { found = true; if (x < minx) minx = x; if (y < miny) miny = y; if (x > maxx) maxx = x; if (y > maxy) maxy = y; }
  }
  for (const ch of node) walk(ch);
}
walk(tree);
if (!found) { console.error('no Edge.Cuts geometry found'); process.exit(2); }
console.log('AREA_MM2: ' + ((maxx - minx) * (maxy - miny)).toFixed(1));
EOF
)

NODE_MESH=$(cat <<'EOF'
const fs = require('fs');
const buf = fs.readFileSync(process.argv[1]);
let tris = [];
const head = buf.slice(0, Math.min(512, buf.length)).toString('latin1');
if (/^\s*solid/.test(head) && head.includes('facet')) {
  const txt = buf.toString('latin1');
  const re = /outer\s+loop([\s\S]*?)endloop/gi; let m;
  while ((m = re.exec(txt))) {
    const vs = [...m[1].matchAll(/vertex\s+([-+0-9.eE]+)\s+([-+0-9.eE]+)\s+([-+0-9.eE]+)/g)]
      .map(v => [+v[1], +v[2], +v[3]]);
    if (vs.length === 3) tris.push(vs);
  }
} else {
  if (buf.length < 84) { console.error('not an STL (too small)'); process.exit(2); }
  const n = buf.readUInt32LE(80);
  if (84 + n * 50 > buf.length) { console.error('binary STL truncated'); process.exit(2); }
  for (let i = 0; i < n; i++) {
    const o = 84 + i * 50 + 12, t = [];
    for (let v = 0; v < 3; v++)
      t.push([buf.readFloatLE(o + v * 12), buf.readFloatLE(o + v * 12 + 4), buf.readFloatLE(o + v * 12 + 8)]);
    tris.push(t);
  }
}
if (!tris.length) { console.error('no triangles parsed'); process.exit(2); }
const K = p => p.join(',');
let degenerate = 0;
const edges = new Map(); // undirected key -> {fwd,rev} counts relative to canonical vertex order
for (const t of tris) {
  const k = t.map(K);
  if (k[0] === k[1] || k[1] === k[2] || k[0] === k[2]) { degenerate++; continue; }
  for (let i = 0; i < 3; i++) {
    const a = k[i], b = k[(i + 1) % 3];
    const und = a < b ? a + '|' + b : b + '|' + a;
    const e = edges.get(und) || { fwd: 0, rev: 0 };
    e[a < b ? 'fwd' : 'rev']++; edges.set(und, e);
  }
}
let open = 0, nonman = 0, winding = 0;
for (const e of edges.values()) {
  const c = e.fwd + e.rev;
  if (c === 1) open++;
  else if (c > 2) nonman++;
  else if (e.fwd !== 1 || e.rev !== 1) winding++; // two uses, same direction = flipped facet
}
console.error(`tris=${tris.length} open=${open} nonmanifold=${nonman} winding=${winding} degenerate=${degenerate}`);
console.log('MESH_DEFECTS: ' + (open + nonman + winding + degenerate));
EOF
)

NODE_MECHEVAL=$(cat <<'EOF'
const fs = require('fs'), path = require('path');
const dir = process.argv[1], cls = process.argv[2], label = process.argv[3];
const af = path.join(dir, 'assertions.tsv'), mf = path.join(dir, 'measures.json');
if (!fs.existsSync(af)) { console.error('missing ' + af); process.exit(2); }
if (!fs.existsSync(mf)) { console.error('missing ' + mf + ' (kernel-emitted — run the CAD build)'); process.exit(2); }
const meas = JSON.parse(fs.readFileSync(mf, 'utf8'));
const rows = fs.readFileSync(af, 'utf8').split(/\r?\n/).filter(l => l.trim() && !l.startsWith('#'));
let pass = 0, total = 0;
for (const line of rows) {
  const c = line.split('\t');
  if (c[0] === 'id') continue;
  const [id, klass, m, op, limit, units] = c;
  if (!id || klass !== cls) continue;
  total++;
  if (!(m in meas)) { console.error(id + ' FAIL no measure "' + m + '" in measures.json'); continue; }
  const v = +meas[m];
  if (!isFinite(v)) { console.error(id + ' FAIL non-numeric measure "' + m + '"'); continue; }
  let lo = -Infinity, hi = Infinity, mm;
  const lim = (limit || '').replace(/\s/g, '');
  if (op === 'le') hi = parseFloat(lim);
  else if (op === 'ge') lo = parseFloat(lim);
  else if (op === 'within') {
    if ((mm = lim.match(/^([-+0-9.eE]+)(?:±|\+-|\+\/-)([-+0-9.eE]+)%$/))) { const ctr = +mm[1], p = +mm[2] / 100; lo = ctr * (1 - p); hi = ctr * (1 + p); }
    else if ((mm = lim.match(/^([-+0-9.eE]+)(?:±|\+-|\+\/-)([-+0-9.eE]+)$/))) { lo = +mm[1] - +mm[2]; hi = +mm[1] + +mm[2]; }
    else if ((mm = lim.match(/^([-+0-9.eE]+)\.\.([-+0-9.eE]+)$/))) { lo = +mm[1]; hi = +mm[2]; }
    else { console.error(id + ' FAIL unparseable within-limit "' + limit + '"'); continue; }
  } else { console.error(id + ' FAIL unknown op "' + op + '"'); continue; }
  if (isNaN(lo) || isNaN(hi)) { console.error(id + ' FAIL unparseable limit "' + limit + '"'); continue; }
  if (v < lo || v > hi) console.error(`${id} FAIL ${m}=${v} bounds=[${lo},${hi}] ${units || ''}`);
  else { pass++; const margin = Math.min(v - lo, hi - v); console.error(`${id} PASS margin=${isFinite(margin) ? margin.toPrecision(4) : 'inf'} ${units || ''}`); }
}
console.log(`${label}: ${pass}/${total}`);
EOF
)

NODE_PINOUT=$(cat <<'EOF'
const fs = require('fs');
const tsv = f => fs.readFileSync(f, 'utf8').split(/\r?\n/)
  .filter(l => l.trim() && !l.startsWith('#')).map(l => l.split('\t'));
const H = tsv(process.argv[1]), I = tsv(process.argv[2]);
const matesf = process.argv[3];
const idx = (hdr, name) => hdr.indexOf(name);
const hh = H[0], ih = I[0];
const hW = idx(hh, 'wire_id'), hIcd = idx(hh, 'icd_id'), hFrom = idx(hh, 'from'),
      hTo = idx(hh, 'to'), hAwg = idx(hh, 'awg'), hCur = idx(hh, 'current_a');
const iId = idx(ih, 'icd_id'), iKind = idx(ih, 'kind');
if ([hW, hIcd, hFrom, hTo, hAwg, hCur].some(c => c < 0)) { console.error('harness.tsv missing columns (wire_id icd_id from to awg current_a)'); process.exit(2); }
if (iId < 0 || iKind < 0) { console.error('icd.tsv missing columns (icd_id kind)'); process.exit(2); }
// bundled/chassis ampacity floor — mirrors references/harness-protocol.md
const AMP = { 30: 0.5, 28: 0.8, 26: 1.3, 24: 2.0, 22: 3.0, 20: 5.0, 18: 7.0, 16: 10, 14: 15, 12: 25, 10: 35 };
let v = 0;
const bad = m => { console.error('VIOLATION: ' + m); v++; };
const icd = new Map();
for (const r of I.slice(1)) if (r[iId]) icd.set(r[iId], r[iKind]);
const realized = new Set();
const EP = /^[^.\s]+\.[^\s]+$/; // <endpoint>.<connector>[.<pin>]
const prefixes = new Set();
for (const r of H.slice(1)) {
  const w = r[hW]; if (!w) continue;
  if (!icd.has(r[hIcd])) bad(`${w}: unknown icd_id "${r[hIcd]}"`);
  else realized.add(r[hIcd]);
  const awg = parseInt(r[hAwg], 10), cur = parseFloat(r[hCur]);
  if (!(awg in AMP)) bad(`${w}: awg ${r[hAwg]} not in ampacity table`);
  else if (isFinite(cur) && cur > AMP[awg]) bad(`${w}: ${cur} A exceeds AWG${awg} floor ${AMP[awg]} A`);
  for (const ep of [r[hFrom], r[hTo]]) {
    if (!EP.test(ep || '')) { bad(`${w}: malformed endpoint "${ep}"`); continue; }
    const seg = ep.split('.');
    prefixes.add(seg.length >= 3 ? seg.slice(0, -1).join('.') : ep);
  }
}
for (const [id, kind] of icd)
  if ((kind === 'power' || kind === 'signal') && !realized.has(id))
    bad(`${id} (${kind}) unrealized by any harness wire`);
if (matesf && fs.existsSync(matesf)) {
  const M = tsv(matesf), mh = M[0];
  const mA = idx(mh, 'side_a'), mB = idx(mh, 'side_b');
  if (mA < 0 || mB < 0) { console.error('mates.tsv missing columns (side_a side_b)'); process.exit(2); }
  const sides = new Set();
  for (const r of M.slice(1)) { if (r[mA]) sides.add(r[mA]); if (r[mB]) sides.add(r[mB]); }
  for (const p of prefixes) if (!sides.has(p)) bad(`connector ${p} not covered by any mate row`);
}
console.log('PINOUT_VIOLATIONS: ' + v);
EOF
)

NODE_PRODBOM=$(cat <<'EOF'
const fs = require('fs');
function csv(text) {
  const rows = []; let row = [], cur = '', q = false;
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (q) { if (ch === '"') { if (text[i + 1] === '"') { cur += '"'; i++; } else q = false; } else cur += ch; }
    else if (ch === '"') q = true;
    else if (ch === ',') { row.push(cur); cur = ''; }
    else if (ch === '\n') { row.push(cur.replace(/\r$/, '')); rows.push(row); row = []; cur = ''; }
    else cur += ch;
  }
  if (cur !== '' || row.length) { row.push(cur.replace(/\r$/, '')); rows.push(row); }
  return rows.filter(r => r.length > 1 || (r[0] && r[0].trim()));
}
const bom = csv(fs.readFileSync(process.argv[1], 'utf8'));
const h = bom[0].map(x => x.toLowerCase());
const col = n => h.findIndex(x => x === n || x.includes(n));
const cId = col('item_id'), cCat = col('category'), cQty = col('qty'),
      cPrice = col('unit_price'), cCur = col('currency'), cMass = col('mass_g'), cSrc = col('source');
if ([cId, cCat, cQty, cPrice, cMass, cSrc].some(c => c < 0)) {
  console.error('product BOM missing columns (item_id,category,qty,unit_price,mass_g,source)'); process.exit(2);
}
const CATS = new Set(['pcb', 'cots', 'mech', 'fastener', 'wire', 'consumable', 'spare']);
let cost = 0, mass = 0, currency = 'USD';
const bad = [];
for (const r of bom.slice(1)) {
  const id = r[cId]; if (!id) continue;
  const qty = parseFloat(r[cQty]), price = parseFloat(r[cPrice]), m = parseFloat(r[cMass]);
  if (!CATS.has((r[cCat] || '').trim())) bad.push(`${id}: bad category "${r[cCat]}"`);
  if (!(qty > 0)) bad.push(`${id}: qty missing/zero`);
  if (!isFinite(price)) bad.push(`${id}: unit_price missing`);
  if (!isFinite(m)) bad.push(`${id}: mass_g missing (a blank mass is not a zero)`);
  if (!(r[cSrc] || '').trim()) bad.push(`${id}: source missing`);
  if (bad.length) continue;
  if (cCur >= 0 && r[cCur]) currency = r[cCur];
  cost += qty * price; mass += qty * m;
  console.error(`${id} [${r[cCat]}] x${qty} @ ${price} = ${(qty * price).toFixed(2)}  (${(qty * m).toFixed(1)} g)`);
}
if (bad.length) { console.error('INCOMPLETE PRODUCT BOM:\n  ' + bad.join('\n  ')); process.exit(2); }
console.error(`PRODUCT_MASS_G: ${mass.toFixed(1)}`);
console.log(`PRODUCT_COST: ${cost.toFixed(2)} ${currency}`);
EOF
)

# ---------------------------------------------------------------------------
pass_rate() {
  local tsv="${1:-${ANVIL_RESULTS:-anvil-results.tsv}}"
  [[ -f "$tsv" ]] || die "no results TSV: $tsv"
  awk -F'\t' \
    -v cap="$ELECTRICAL_GATE_CAP" \
    -v wE="$ANVIL_W_ELECTRICAL" -v wS="$ANVIL_W_SIMULATION" -v wL="$ANVIL_W_LAYOUT" \
    -v wM="$ANVIL_W_MANUFACTURING" -v wT="$ANVIL_W_TESTABILITY" -v wD="$ANVIL_W_DOCUMENTATION" '
    /^#/ { next } $1 == "n" { next } NF < 5 { next }
    {
      dim = $2; st = $4; w = $5 + 0
      if (st == "skip") next
      den[dim] += w
      if (st == "pass") num[dim] += w
      if (dim == "electrical" && st == "fail") efail++
      rows++
    }
    END {
      if (rows == 0) { print "PASS_RATE: 0.00"; exit 0 }
      W["electrical"] = wE; W["simulation"] = wS; W["layout"] = wL
      W["manufacturing"] = wM; W["testability"] = wT; W["documentation"] = wD
      D = 0; N = 0
      for (d in den) {
        dw = (d in W) ? W[d] : 0.10
        frac = (den[d] > 0) ? num[d] / den[d] : 0
        D += dw; N += dw * frac
        printf "dim %-14s %.2f (w=%.2f)\n", d, frac, dw > "/dev/stderr"
      }
      rate = (D > 0) ? N / D : 0
      if (efail > 0) {
        printf "ELECTRICAL_GATE: %d red row(s), cap %.2f\n", efail, cap > "/dev/stderr"
        if (rate > cap) rate = cap
      }
      printf "PASS_RATE: %.2f\n", rate
    }' "$tsv"
}

coverage() {
  local rows="${1:-${ANVIL_RESULTS:-anvil-results.tsv}}" hrs="${2:-${HRS_MD:-hrs/requirements.md}}"
  if [[ "$rows" == "--spec" ]]; then rows="${2:?spec file}"; hrs="${3:?hrs file}"; fi
  [[ -f "$rows" ]] || die "coverage: missing $rows"
  [[ -f "$hrs" ]] || die "coverage: missing $hrs"
  local id covered=0 total=0
  local ids; ids=$(grep -oE 'HR-[0-9]+' "$hrs" | sort -u)
  if [[ -z "$ids" ]]; then echo "no HR-n ids found in $hrs" >&2; echo "REQ_COVERAGE: 0.00"; return 0; fi
  while IFS= read -r id; do
    total=$((total + 1))
    if grep -qE "\b${id}\b" "$rows"; then covered=$((covered + 1)); else echo "uncovered: $id" >&2; fi
  done <<<"$ids"
  local oid
  for oid in $(grep -oE 'HR-[0-9]+' "$rows" | sort -u); do
    grep -qE "\b${oid}\b" "$hrs" || echo "orphan trace (not in HRS): $oid" >&2
  done
  awk -v c="$covered" -v t="$total" 'BEGIN { printf "REQ_COVERAGE: %.2f\n", (t > 0) ? c / t : 0 }'
}

erc() {
  local sch="${1:?usage: score-anvil.sh erc <schematic> [out.json]}"
  local out="${2:-$(dirname "$sch")/erc.json}"
  local kc; kc="$(find_kicad)" || die "kicad-cli not found (references/toolchain.md)"
  "$kc" sch erc --format json --severity-error --exit-code-violations -o "$out" "$sch" >/dev/null 2>&1 || true
  [[ -s "$out" ]] || die "ERC produced no report ($out)"
  echo "ERC_VIOLATIONS: $(node -e "$NODE_VCOUNT" "$out")"
}

drc() {
  local pcb="${1:?usage: score-anvil.sh drc <board> [out.json]}"
  local out="${2:-$(dirname "$pcb")/drc.json}"
  local kc; kc="$(find_kicad)" || die "kicad-cli not found (references/toolchain.md)"
  "$kc" pcb drc --format json --schematic-parity --severity-error --exit-code-violations -o "$out" "$pcb" >/dev/null 2>&1 || true
  [[ -s "$out" ]] || die "DRC produced no report ($out)"
  echo "DRC_VIOLATIONS: $(node -e "$NODE_VCOUNT" "$out")"
}

sim() {
  local dir="${1:-sim}"
  [[ -d "$dir" ]] || die "sim: no such dir $dir"
  if [[ "${SKIP_NGSPICE:-0}" != "1" ]] && command -v ngspice >/dev/null 2>&1; then
    (
      cd "$dir" || exit 2
      local cir
      for cir in *.cir; do
        [[ -f "$cir" ]] || continue
        ngspice -b -o "${cir%.cir}.log" "$cir" >/dev/null 2>&1 || echo "ngspice non-zero exit: $cir" >&2
      done
    )
  else
    echo "ngspice unavailable or SKIP_NGSPICE=1 — parsing existing logs only" >&2
  fi
  node -e "$NODE_SIM" "$dir"
}

bom_cost() {
  local bom="${1:?usage: score-anvil.sh bom-cost <bom.csv> <catalog.csv>}"
  local catalog="${2:?pinned catalog csv required}"
  [[ -f "$bom" ]] || die "no BOM: $bom"
  [[ -f "$catalog" ]] || die "no catalog: $catalog"
  node -e "$NODE_BOM" "$bom" "$catalog"
}

area() {
  local pcb="${1:?usage: score-anvil.sh area <board.kicad_pcb>}"
  [[ -f "$pcb" ]] || die "no board: $pcb"
  node -e "$NODE_AREA" "$pcb"
}

mesh() {
  local stl="${1:?usage: score-anvil.sh mesh <file.stl>}"
  [[ -f "$stl" ]] || die "no STL: $stl"
  node -e "$NODE_MESH" "$stl"
}

fit() {
  local dir="${1:?usage: score-anvil.sh fit <mech-dir>}"
  [[ -d "$dir" ]] || die "fit: no such dir $dir"
  node -e "$NODE_MECHEVAL" "$dir" fit FIT_PASS
}

mass() {
  local dir="${1:?usage: score-anvil.sh mass <mech-dir>}"
  [[ -d "$dir" ]] || die "mass: no such dir $dir"
  node -e "$NODE_MECHEVAL" "$dir" mass MASS_PASS
}

mech_dfm() {
  local dir="${1:?usage: score-anvil.sh mech-dfm <mech-dir>}"
  [[ -d "$dir" ]] || die "mech-dfm: no such dir $dir"
  local out x y
  out=$(node -e "$NODE_MECHEVAL" "$dir" dfm DFM_PASS) || exit $?
  x=${out#DFM_PASS: }; y=${x#*/}; x=${x%%/*}
  if [[ -n "${PRUSA_SLICER:-}" ]]; then
    # slicer seam: every build STL must slice clean when a slicer is configured
    local stl ok=0 tot=0 g
    for stl in "$dir"/build/*.stl; do
      [[ -f "$stl" ]] || continue
      tot=$((tot + 1))
      g="$(mktemp -u).gcode"
      if "$PRUSA_SLICER" --export-gcode --output "$g" "$stl" >/dev/null 2>&1; then
        ok=$((ok + 1)); echo "slice PASS: $stl" >&2
      else
        echo "slice FAIL: $stl" >&2
      fi
      rm -f "$g"
    done
    x=$((x + ok)); y=$((y + tot))
  else
    echo "slicer seam disabled (PRUSA_SLICER unset) — dfm assertions only" >&2
  fi
  echo "DFM_PASS: $x/$y"
}

pinout() {
  local h="${1:?usage: score-anvil.sh pinout <harness.tsv> <icd.tsv> [mates.tsv]}"
  local i="${2:?icd.tsv required}"
  [[ -f "$h" ]] || die "no harness table: $h"
  [[ -f "$i" ]] || die "no ICD: $i"
  node -e "$NODE_PINOUT" "$h" "$i" "${3:-}"
}

product_bom() {
  local pb="${1:?usage: score-anvil.sh product-bom <product-bom.csv>}"
  [[ -f "$pb" ]] || die "no product BOM: $pb"
  node -e "$NODE_PRODBOM" "$pb"
}

verdict() {
  local tsv="${1:-${ANVIL_RESULTS:-anvil-results.tsv}}" hrs="${2:-}"
  [[ -f "$tsv" ]] || die "no results TSV: $tsv"
  local rate efail mustfail cov="1.00" target="${TARGET_RATE:-1.00}"
  rate=$(pass_rate "$tsv" 2>/dev/null | awk '{print $2}')
  efail=$(awk -F'\t' '$1 != "n" && !/^#/ && $2 == "electrical" && $4 == "fail" { c++ } END { print c + 0 }' "$tsv")
  mustfail=$(awk -F'\t' '$1 != "n" && !/^#/ && ($2 == "simulation" || $2 == "layout") && $4 == "fail" { c++ } END { print c + 0 }' "$tsv")
  [[ -n "$hrs" ]] && cov=$(coverage "$tsv" "$hrs" 2>/dev/null | awk '{print $2}')
  if awk -v r="$rate" -v t="$target" 'BEGIN { exit !(r + 0 >= t + 0) }' \
    && [[ "$efail" == 0 && "$mustfail" == 0 && "$cov" == "1.00" ]]; then
    echo "FAB_READY"
  else
    echo "blocking: rate=$rate target=$target electrical_fails=$efail sim/layout_fails=$mustfail coverage=$cov" >&2
    echo "FAB_BLOCKED"
  fi
}

# ---------------------------------------------------------------------------
cmd="${1:-}"
shift || true
case "$cmd" in
  pass-rate) pass_rate "$@" ;;
  coverage)  coverage "$@" ;;
  erc)       erc "$@" ;;
  drc)       drc "$@" ;;
  sim)       sim "$@" ;;
  bom-cost)  bom_cost "$@" ;;
  area)      area "$@" ;;
  mesh)      mesh "$@" ;;
  fit)       fit "$@" ;;
  mass)      mass "$@" ;;
  mech-dfm)  mech_dfm "$@" ;;
  pinout)    pinout "$@" ;;
  product-bom) product_bom "$@" ;;
  verdict)   verdict "$@" ;;
  *) echo "usage: score-anvil.sh {pass-rate|coverage|erc|drc|sim|bom-cost|area|mesh|fit|mass|mech-dfm|pinout|product-bom|verdict} [args]" >&2; exit 2 ;;
esac
