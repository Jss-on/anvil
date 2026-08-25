# Simulation Protocol

Contract for `build` Phase 6 and the `simulation` dimension. One rule above all: **a spec passes at
its declared corners with a recorded margin, or it does not pass.**

## Harness shape

One ngspice batch harness per simulable HRS spec: `sim/<spec-id>.cir`.

```spice
* A-HR-2 — output ripple, worst-case line/load
.include models/TPS562200.lib      ; vendor model, provenance header in the file
.param VIN=4.5 ILOAD=1
VIN in 0 DC {VIN}
* ... circuit under test, parameterized by the corner params ...
.tran 100n 5m 4m uic
.measure tran vripple PP v(out) from=4.2m to=5m
.control
run
.endc
.end
```

Rules:
- **Vendor SPICE models first**, `models/` with a provenance header (source URL, accessed date,
  encrypted/unencrypted). No vendor model → datasheet-derived behavioral model with derivation
  shown in a comment block. Model provenance is a `documentation` row.
- `.measure` names match assertion IDs — the parser keys on them.
- Corner parameters enter via `.param`; the runner sweeps them. Never hand-edit values per run.
- Deterministic: fixed seeds where MC is used; timesteps chosen for the measured quantity
  (ripple needs ≥100 pts/switching period).

## assertions.tsv (the contract — 7 tab-separated cols)

```
id	measure	op	limit	units	corners	traces
A-HR-1	vout_avg	within	3.3±3%	V	vin=4.5,5.5;iload=0,1	HR-1
A-HR-2	vripple	le	0.030	V	vin=4.5,5.5;iload=1	HR-2
A-HR-6	eff	ge	0.85	-	vin=5.0;iload=0.5	HR-6
```
`op ∈ le|ge|within` (`within` takes `center±pct%` or `lo..hi`). `corners`: `;`-joined param lists —
the runner executes the **cross product** and the row passes only if EVERY corner passes. Margin =
worst-corner distance to the limit, in the row's units (and as % of limit in the report).

`scripts/score-anvil.sh sim sim/` runs every harness (`ngspice -b -o <id>.log <id>.cir`), parses
`measure = value` lines, evaluates ops, prints per-row `PASS|FAIL` + margin, and
`SIM_PASS: x/y` last.

## Corner policy

- **Nominal first** (fast inner-loop signal), **corners before any keep** that touches the block,
  full corner suite before the phase gate.
- Standard corner set: line min/max × load min/max × Ta-driven parameter shifts where the model
  supports temp. Component tolerance: `.step`/Monte Carlo on the parts that dominate the spec
  (feedback dividers, sense elements) — worst-case method recorded in the report.
- **Maximin discipline:** the margin that matters is the WORST corner's. Averages hide cliffs.

## Convergence playbook (a sim that can't run is a red row, never a skip)

In order: check topology floats (every node DC path to ground) → `.options gmin=1e-10` then step
gmin → `uic` with sensible `.ic` on reactive states → relax `reltol` to 1e-2 ONLY for exploratory
runs, never for the gated result → replace the vendor model with the behavioral fallback and note
the downgrade. Every workaround is a comment in the harness, not tribal memory.

## Downgrades

A spec that genuinely cannot be simulated (no model, mechanical property, EMC field behavior) is
downgraded `simulation → analysis` **in the HRS itself** with a one-line reason, and the analysis
must show work (equations, datasheet figures). Silent downgrades are audit failures — the
requirement-satisfaction audit re-checks every `verify:` tag against the evidence class.

## Report (`docs/SIM-REPORT.md`)

Per assertion: limit · worst corner · value at worst corner · margin (units and %) · harness path ·
log path. The margin table is the input to `improve`'s `worst_case_margin` metric and to evals'
silent-erosion detection. Plots optional; numbers mandatory.
