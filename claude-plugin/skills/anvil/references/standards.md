# Standards & Compliance Reference

The numbers annex. Protocols cite this file instead of re-transcribing standards; the loop reads
anchor values here, the human verifies against the purchased standard for anything safety-critical.

## Provenance caveat (read first)

IPC standards are copyrighted and paywalled. Values below are corroborated across multiple
secondary sources (EDA-vendor and fab documentation, mutually consistent) but are transcriptions,
not quotations. For Class 3 / safety-critical work, verify against the purchased standard. Always
state the exact revision on RFQs ("IPC-A-610**J** Class 2") — acceptance criteria change between
revisions. Revisions listed are current as of 2026; re-check before citing on a new RFQ.

## The IPC registry (what owns what)

| Standard | Owns | Current rev |
|---|---|---|
| IPC-2221 | generic design: spacing/creepage, conductor sizing, materials, thermal | C (Dec 2023) |
| IPC-2222 | rigid-board sectional (supplements 2221) | |
| IPC-2152 | conductor current capacity — replaced 2221's 1950s-era charts | 2009 |
| IPC-2141A | controlled-impedance formulas (use the fab's REAL dielectric values) | |
| IPC-7351 | SMT land patterns — density levels A/B/C, computed not fixed | |
| IPC-A-600 | bare-board acceptability | |
| IPC-A-610 | assembly acceptability (Acceptable / Process Indicator / Defect) | J (Apr 2024) |
| IPC-6012 | rigid-board qualification & performance | F (2023) |
| J-STD-001 | soldering requirements | |
| J-STD-020 / 033 | moisture sensitivity classification / handling | 020F (Nov 2022) |
| IPC-2581 / ODB++ | intelligent fab data exchange (single-file: copper + stackup + netlist + BOM) | |
| Gerber RS-274X | de-facto fab image format (~90 % of boards); X2/X3 add metadata | |
| IEEE 1149.1 | JTAG boundary scan (BSDL, scan chains) | |
| IEEE 315 / ASME Y14.44 | reference-designator class letters / application practice | |

## Class election (1/2/3) — the most consequential early decision

Declared in the HRS manufacturing domain, recorded in the charter and `build-spec.yaml`
(`ipc_class`), stated on the DFM report and every RFQ. Default: **Class 2**. Changing the
operating environment, data rate, or reliability target re-opens the election.

| | Class 1 | Class 2 (default) | Class 3 |
|---|---|---|---|
| Domain | general/consumer | dedicated service — commercial/industrial | high-rel: aerospace, medical, military |
| Annular ring | breakout tolerated | reduced ring acceptable | **zero tolerance for breaks** |
| Hole-wall Cu plating (6012F) | 20 µm (0.8 mil) | 20 µm | **25 µm (1 mil)** |
| Vertical barrel fill (6012F) | — | ≥ 50 % | ≥ 75 % |
| Inspection posture | functionality primary | process-indicator tolerant | strictest accept criteria |

Class drives annular-ring minimums, spacing, hole fill, and inspection criteria through every
downstream gate — electing it late re-prices the whole board.

## IPC-2152 ampacity anchors (1 oz copper, 10 °C rise)

| Width | External copper |
|---|---|
| 10 mil (0.25 mm) | ~1.0 A |
| 20 mil (0.51 mm) | ~1.7 A |
| 50 mil (1.27 mm) | ~3.5 A |

Internal traces carry only **50–70 % of external** (poorer heat escape). Rule of thumb:
~1 mm width per amp, external 1 oz — anchors and thumb are for sanity checks; real nets are
sized from the standard/calculator and recorded per net in the layout report. Heavier copper
(2 oz) halves required width for the same rise.

## IPC-2221 spacing (creepage & clearance) — Table 6-1 anchors

Columns: B1 internal · B2 external uncoated (sea level) · B3 external uncoated > 3050 m ·
B4 polymer coated. Spacing keys on **PEAK** working voltage:

| Peak working V | B2 external uncoated | Known cross-checks |
|---|---|---|
| ≤ 30 | ~0.1 mm | |
| 50–150 | ~0.6 mm | |
| 170–300 | ~1.25 mm | internal (B1) ~0.2 mm @ 300 V |
| 301–500 | ~2.5 mm | coated (B4) ~0.8 mm @ 340 V |
| > 500 | ≈ 2.5 + 0.005 × (V − 500) mm | per-volt formula, third-party derivation |

Creepage additionally depends on **RMS** voltage, pollution degree (1 = none, 2 = normally
non-conductive/condensation, 3 = conductive) and material group. IPC values are voluntary:
where a product falls under a safety standard, the creepage/clearance rules of **IEC 60664-1**
(insulation coordination) or **IEC 62368-1** (AV/IT/telecom — replaced 60950-1) are mandatory
and override. Every HV-register row states which regime applied.

## IPC-7351 land-pattern density levels

| Level | Name | Use |
|---|---|---|
| A | Most | maximum pads — hand-soldering, high-reliability |
| B | Nominal | **default** for standard reflow production |
| C | Least | high-density — only with the CM's confirmation |

Patterns are computed from lead geometry + solder-joint goals + fab tolerances, never fixed pads.
Undersized pads → fatigue failures; oversized → bridging on fine pitch, tombstoning on chips.

## Moisture sensitivity (J-STD-020F / J-STD-033)

Floor life at ≤ 30 °C / 60 % RH after bag open; exceeded = bake before reflow (popcorning risk):

| MSL | 1 | 2 | 2a | 3 | 4 | 5 | 5a | 6 |
|---|---|---|---|---|---|---|---|---|
| Floor life | unlimited* | 1 year | 4 weeks | **168 h** | 72 h | 48 h | 24 h | bake always |

*MSL 1 rated at ≤ 30 °C/85 % RH. MSL 3 is the most common rating for fine-pitch BGAs/QFNs —
one calendar week of floor life. SAC305 reflow peaks ~230–250 °C.

## Substance & material compliance

- **RoHS 3 (EU 2015/863):** 10 restricted substances measured at the *homogeneous-material*
  level — Pb, Hg, Cr(VI), PBB, PBDE + 4 phthalates (DEHP, BBP, DBP, DIBP) each < 1000 ppm;
  **Cd < 100 ppm**. Drove the industry to lead-free SAC solder.
- **REACH (EU):** SVHC Candidate List grows ~2×/year (253 entries, early 2026). Article
  suppliers must notify when an SVHC exceeds 0.1 % w/w per article; SCIP database entry
  required since Jan 2021.
- **UL:** UL 796 = bare-board recognition ("UR" mark + E-file number + flammability rating on
  the board); **UL 94V-0** the typical FR-4 flammability target (no burning > 10 s, no flaming
  drips). Assembled end products list separately (e.g. UL 62368-1).

## Obsolescence numbers (why the pinned-catalog discipline exists)

- **> 50 % of 2025 component discontinuations shipped with NO PCN** (Z2Data: 323 286 of
  621 909); 25–30 % was typical in prior years. Lifecycle silence ≠ safety — check status at
  every explicit catalog refresh, not only when a notice arrives.
- When a PCN does land: JEDEC requires 90 days' notice, and the **last-time-buy window is
  typically ~6 months**. An LTB on a catalog part is a drop-everything GitHub issue, not a
  backlog item.
