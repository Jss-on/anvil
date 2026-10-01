# rffe — Anvil showcase: 2.4 GHz gain block + 25 MHz reference clock

A complete Anvil project, taken from requirements to recorded G3 evidence. Every number below was produced by
Anvil's own commands on the KiCad files in this folder. Each one is quoted from a hashed receipt in `evidence/`;
none are typed in.

**Board:** 4 layers, 50 × 36 mm.
- **RF chain:** J1 → C1 → U2 (Mini-Circuits GALI-84+) → C2 → J2, on 50 Ω grounded-coplanar lines over the In1
  ground plane. The edge-launch SMA pads reference B.Cu through cut-outs in In1 and In2.
- **Bias tee:** 22 nH choke, 3 × 220 Ω 2512 from 12 V, 10 pF + 100 nF bypass.
- **Clock:** a 25 MHz oscillator drives a 33 Ω series-terminated SMA output.
- **Supply:** an AMS1117 makes +3V3 on an In2 plane.

> Showcase design. The GALI-84 and AMS1117 bias, θjb and output-impedance values are datasheet typicals
> marked "to confirm". This is not a product release.

## Reproduce

```sh
python tools/pipeline.py                         # schematic -> template -> board -> place + RF pre-routes -> Freerouting + DRC
python ../../scripts/anvil.py rules design       # cited sizing calculations
python ../../scripts/anvil.py layout  pcb/rffe.kicad_pcb design
python ../../scripts/anvil.py pdn     pcb/rffe.kicad_pcb design
python ../../scripts/anvil.py si      pcb/rffe.kicad_pcb design
python ../../scripts/anvil.py thermal pcb/rffe.kicad_pcb design
python ../../scripts/anvil.py emc     pcb/rffe.kicad_pcb design
python ../../scripts/anvil.py em      pcb/rffe.kicad_pcb design   # openEMS, ~50 min (4 port runs)
python ../../scripts/anvil.py fabpack pcb/rffe.kicad_pcb fab && python ../../scripts/anvil.py renders .
python tools/write_ledgers.py && python tools/declare_release.py
python ../../scripts/anvil.py plan . && python ../../scripts/anvil.py manifest . && python ../../scripts/anvil.py record . AUTO-...
python ../../scripts/anvil.py gate . G3 && python ../../scripts/anvil.py report .
```

`tools/` holds the project-specific steps an engineer or agent would script:
- `size_rf_line.py`: field-solver width/gap table.
- `make_template.py`: stackup, outline, planes and the SMA launch cut-outs.
- `make_routes.py`: RF lines, clock line, fence, launch/thermal/stitching vias and plane fanouts, all computed from
  the placed pads.
- `place_schematic.py`: functional sheet layout.
- `declare_release.py`, `write_ledgers.py`.

## What the loop found and fixed (`audit/iterations.tsv`)

| # | Found by | Problem | Fix |
|---|---|---|---|
| 1 | `schematic` | Netlist mismatch on the first run only | Generator nondeterminism (set order); fixed in Anvil, regression test added |
| 2 | `drc` | 137 → 20 violations: edge-launch pads, zone islands, silkscreen | SMA pull-back, scoped edge rule, island removal, placement |
| 3 | `drc` | Floating +3V3 plane, fragmented ground pour | Plane fanouts and stitching pre-routed |
| 4 | `layout` | RF fence gaps and pour tips beyond λ/10 and λ/20 at 5 GHz | Greedy fence, launch vias, gap-fill stitching: 58/58 |
| 5 | `rules` | Bias resistors at 51.6 % of rating at 13.2 V (2× derating, WILSON-394) | 2 × 150 Ω → 3 × 220 Ω: 35 % |
| 6 | `thermal` | GALI-84 at 130.3 °C against a 130 °C limit after the extra resistor | R1 moved, 2 × 3 thermal vias: 129.0 °C |
| 7 | `si` | ngspice stalled on sub-ps line fragments | Fixed in Anvil: fragments below the time step are merged |
| 8 | `em` | openEMS field energy never decayed (a −11 dB plateau), so no S-parameters | Fixed in Anvil (below) |
| 9 | `em` | SMA centre pad (1.5 mm) over In1 at 0.2 mm is an 18 Ω section: `rf_in` S11 −6.8 dB, S21 −1.26 dB | In1/In2 cut-out under the J1/J2 centre pads (JOHNSON03-1307): the pad references B.Cu, 47.8 Ω; S11 −15.9 dB |
| 10 | `rules` + `em` | 100 pF DC blocks are 8.8 Ω *inductive* at 2.5 GHz: far above their self-resonance | 10 pF C0G, series-resonant near the band: 3.1 Ω (BOGATIN-2128, ARCH-067) |
| 11 | `em` | S11 then read −14.95 dB with Zin 42 + j14 Ω: the inductive 100 pF had been masking the launch *port's* own inductance, a 1.5 mm tall sheet down to B.Cu | Fixed in Anvil: over a cut-out the port drives the coplanar gaps (validated against the 2-D solver); S11 −17.1 dB |

Iteration 8 was diagnosed with 16 point field probes and truncated-record comparisons, not the energy log. The
port signals had decayed 50 dB while the "energy" stayed flat. Removing the ideal 100 pF lumped capacitor let the
model converge: spread over the mesh, an ideal C rings losslessly. The EM engine now:
- models capacitors as series ESR-ESL-C;
- models only the analysed and ground nets;
- places each port where the pin or lead enters its pad;
- runs to −50 dB;
- reports a `settled` row, so an unconverged result cannot pass.

The first converged run then exposed iteration 9, a real layout flaw that every earlier check had passed.
Iteration 11 is the loop checking its own instrument: a model artifact, found because the numbers moved the
wrong way after a change that should have helped, then fixed and validated before the result was trusted.

## Results

Receipts bind release `da83c6a3…` (`release-manifest.json`, 33 controlled files) and the checker code.

| Check | Result | Tightest margin |
|---|---|---|
| AUTO-ERC / AUTO-DRC | 0 / 0 violations | KiCad 10.0.5 on the release files |
| AUTO-CONNECTIVITY | 5/5 | netlist equals `sch/circuit.json` |
| AUTO-SIM | 2/2 | bias-node ripple −15.1 dB at 100 kHz (worst corner) against −3 dB |
| AUTO-RULES | 11/11 | DC block 3.06 Ω against 5 Ω; bias current 103.6 mA in 100 ± 10 mA |
| AUTO-LAYOUT | 58/58 | RF Z0 50.0 Ω; fence ≤ λ/10 and stitching ≤ λ/20 at 5 GHz |
| AUTO-PDN | 1/1 | +3V3 Zmax 0.80 Ω against 1.65 Ω |
| AUTO-SI | 4/4 | CLK_OUT ringback 9.8 % against 20 %; settled in 0.55 ns against 5 ns |
| AUTO-THERMAL | 5/5 | U2 junction 129.0 °C against 130 °C (thin: confirm at EVT) |
| AUTO-EMC | 2/2 | CLK_OUT 32 dB under CISPR 32 Class B, 26 dB after the 6 dB design margin |
| AUTO-EM | not yet recorded | `rf_in` probe passes: S11 −17.1 dB (limit −15), S21 −0.21 dB (limit −0.6). `rf_out` diverges in openEMS 0.37 (below) |

**Open issue: `rf_out`.** With the bias tee in the model, every run diverges after the pulse: the energy decays to
about −20 dB, then grows without bound from roughly 30k timesteps. Bisection so far:
- Any single series-type lumped part triggers it, the choke alone or the capacitors alone, even though each is
  stable in a small test model.
- Collapsing the parts to single-edge lines does not help, and neither does cutting the bias feed at the region
  edge.

The all-resistor control run had not finished when this snapshot was taken. Anvil rejects a diverged run
(NaN energy or non-finite port signals) instead of reporting it, so AUTO-EM stays open until `rf_out` converges.

Figures: `analysis/em/*.png` (S-parameters against the limits), `analysis/layout/copper-*.png`,
`analysis/thermal/thermal.png`, `analysis/pdn/pdn-_3V3.png`, `analysis/si/si-CLK_OUT.png`,
`analysis/emc/emc-cispr32_b.png`, `audit/plots/P-1.png` (bias ripple at the tolerance corners).

![In1 with the SMA launch cut-outs](analysis/layout/copper-In1_Cu.png)

## Gate

`anvil.py gate . G3` returns `G3_BLOCKED`: AUTO-EM (above) and the 41 human sign-offs:
- 2 G0 opportunity reviews;
- 15 G1 requirement and compliance-plan reviews;
- 6 G2 architecture reviews;
- 8 G3 release reviews;
- 10 requirement closures (REQ-HR-001 … 010).

Anvil will not record an approval it would have to invent. A reviewer closes each one in three steps:
1. `anvil.py prepare . <check> <evidence files>`
2. Fill in reviewer, role, decision and record.
3. `anvil.py record . <check> --evidence evidence/<check>.draft.json`

## Audit documentation

- `audit/AUDIT.md` and `audit/audit.json`: requirements, 11 research sources, 9 decisions, 12 iterations, every
  receipt with its transcript and margins, the BOM, figures, the release manifest and IEEE references.
- `audit/paper/paper.tex` + `refs.bib`: IEEE conference skeleton with the requirement, decision, execution, margin
  and iteration tables and every verification figure. The prose sections are for the author.
- `fab/`: gerbers, drill, placement, IPC-2581, IPC-D-356 test netlist, STEP; `audit/renders/`: schematic PDF/SVG,
  board SVG/PNG.

## What stays physical

- VNA S-parameters of the built board (HR-011 at G4). The EM model has no SMA body, solder mask or conductor loss,
  and its lumped launch port stands 1.5 mm tall.
- The gain block's own S-parameters, from the vendor file, not from copper.
- Chamber EMC: the emission figure is an estimate (±10 dB).
- A thermocouple or IR check of U2: the thermal margin is under 1 °C in the model.
