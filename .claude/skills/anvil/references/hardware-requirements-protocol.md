# Hardware Requirements Protocol

The contract behind `/anvil:requirements` and `build` Phase 3. Shape: IEEE 29148 adapted to
electronics, agile-right-sized.

## The four measurability checks (every HR-n passes all four)

| Check | Fails | Passes |
|---|---|---|
| Value + unit | "low ripple", "fast", "small" | "≤ 30 mV p-p on 3V3" |
| Conditions | unstated (= nominal only) | "at Vin 4.5–5.5 V, Iload 0–1 A, Ta ≤ 60 °C" |
| Limit direction | "about 3.3 V" | "3.3 V ± 3 %" |
| Verification method | absent | `verify: simulation` (or test/analysis/inspection) |

## Verification ladder (strongest feasible, downgrade only with logged reason)

`test` (measured on the physical board — future `bringup`) > `simulation` (ngspice assertion at
corners) > `analysis` (calculation in the HRS with shown work — e.g. thermal budget from θJA) >
`inspection` (a property of the files — connector pinout matches, silkscreen present, footprint
correct). A spec marked `simulation` satisfied only by prose analysis is NOT satisfied.

## The nine elicitation domains

1. **Function & performance** — what it does, the numbers that define "works".
2. **Power** — source (USB, battery, mains adapter, PoE), input range incl. transients, per-rail
   budget, efficiency/quiescent targets, sequencing.
3. **Electrical environment** — line sags/surges, hot-plug, ESD exposure class, load dumps.
4. **Mechanical** — max L×W×H, mounting pattern, connector types/positions/orientation, enclosure,
   keep-outs. For products (not bare boards): enclosure/frame envelope + mass ceiling, **ingress
   protection (IP rating — IP54 splash / IP65 washdown / IP67 immersion, or explicit "none")**,
   materials + process (FDM/SLA/CNC), serviceability (tool-less vs fastened access, field-swap
   items) — feeds `mechanical-protocol.md`.
5. **Thermal/ambient/dynamic** — Ta range, airflow (none/convection/forced), max component temp
   policy. **Vibration** (source + profile: motor-band sine for airborne, random g RMS for
   vehicle-mount, or "benign desk") and **shock/drop** (drop height onto surface, expected crash
   loads for airborne — drives isolator + sacrificial-part requirements). "Rugged" is not a spec
   until it is an IP class, a vibration profile, and a drop height with numbers.
6. **EMC & regulatory** — target class (FCC/CE class A/B, none-for-lab), isolation requirements.
7. **Interfaces** — every external protocol with voltage levels + speed (USB FS/HS, UART baud,
   I²C addresses reserved, CAN termination policy…).
8. **Manufacturing** — fab preset, layer budget, qty, BOM cost target **@ that qty**, assembly
   (hand / PCBA), one-sided placement preference, panelization needs.
9. **Lifecycle & safety** — production years (drives lifecycle floor on parts), second-source
   policy, field service, voltage class (>30 V triggers the HV register; mains adds the human
   sign-off row).

## The must-be checklist (Kano: never stated, always expected)

Candidate HR rows generated BEFORE elicitation so the client reacts, not recalls:
- Reverse-polarity / miswire protection on field-accessible power inputs.
- ESD (IEC 61000-4-2 contact level appropriate to exposure) on every user-facing connector.
- Brown-out: defined behavior through input sag and recovery (no latch-up, no corrupted state).
- Inrush limited to the source's capability (USB ≤ 10 µF hard-start rule, adapter surge).
- Thermal: every part below its derated ceiling at max Ta, worst load.
- Bench-readiness: test points on every rail + key signals, pin-1/polarity silkscreen, mounting
  holes, current-limited first-power values documented.
- Boot/default state: outputs safe at power-up and during reset (motor drivers LOW, relays open).
- Product builds add: strain relief at every wire exit; vibration-sensitive modules (IMU/camera)
  isolated, never hard-mounted; enclosure ingress consistent with the declared IP class (seal or
  declared "none"); crash/impact consumables replaceable without full teardown; every external
  fastener captive or standard-driver accessible in the field.

## HRS template (`hrs/requirements.md`)

```markdown
# HRS — <board>
## Goals
G-1 <one sentence, client language>
## Requirements
### Functional / performance
HR-1 (G-1) — 3V3 rail: 3.3 V ± 3 %, Iload 0–1 A, Vin 4.5–5.5 V, Ta −10…60 °C. verify: simulation
HR-2 — Output ripple ≤ 30 mV p-p at full load, worst-case line. verify: simulation
### Electrical environment
HR-3 — Survives reverse input polarity indefinitely. verify: simulation
### Mechanical
HR-4 — Board ≤ 50 × 40 mm, M3 holes at 4 corners. verify: inspection
### Manufacturing
HR-5 — BOM ≤ $8.00 @ qty 10 (catalog snapshot 2026-08-26). verify: analysis
### … (all nine domains, omit domains with a stated "none")
## Out of scope
## Open questions (each with recommended default)
```

Rules: stable IDs, never renumber (retired = `HR-n (RETIRED: reason)`); every HR tagged with the
goal(s) it serves; conditions inline, not in a footnote.

## build-spec.yaml schema (the ready `anvil:build` input)

```yaml
name: buck-3v3
summary: one line
fab: jlcpcb          # rule-deck preset
layers: 2
targets:
  bom_cost: {limit: 8.00, currency: USD, qty: 10}
  board_area: {limit: 2000, units: mm2}
specs:               # one row per HR-n
  - {id: HR-1, text: "3V3 3.3V±3% 0–1A over line/temp", dimension: simulation, verify: simulation}
  - {id: HR-4, text: "≤50×40mm, 4×M3", dimension: layout, verify: inspection}
golden_connectivity: # electrical dimension must-pass rows
  - "net VBUS reaches U1.VIN through F1 and D1"
  - "every U1 power pin has 100nF within its block"
  - "U1.EN strapped, never floating"
sim_assertions:      # seeds sim/assertions.tsv
  - {id: A-HR-1, measure: vout_avg, op: within, limit: "3.3±3%", units: V,
     corners: "vin=4.5,5.5;iload=0,1", traces: HR-1}
```

### Product-mode extension (end-to-end builds)

A spec whose deliverable is an assembled product (not a bare board) adds a `product:` block; each
entry seeds the corresponding track's protocol and acceptance rows:

```yaml
product:
  subsystems:        # seeds system/decomposition.md (system-protocol.md)
    - {id: S-2, subsystem: propulsion, kind: cots, realization: "cots: MOT-*,ESC-1"}
  cots:              # seeds cots/modules.csv — datasheet-anchored numbers required
    - {module_id: BAT-1, role: power, key_specs: "6S 1300mAh 120C, 28.9Wh, 205g"}
  mech:              # seeds mech/assertions.tsv (fit/mass/dfm classes)
    - {id: HR-12, text: "FC stack fits cavity, ≥0.5mm z-clearance", verify: analysis}
  budgets:           # seeds system/budgets.tsv — must CLOSE (sys-budget gate)
    - {id: B-1, quantity: mass, demand: AUW, capability: "thrust@hover", derate: 0.5}
  environment:       # rugged numbers — IP class, vibration profile, drop height
    ip: IP54
    vibration: "motor band 100–400 Hz, isolators required on FC"
    drop: "1.5 m onto concrete, arms sacrificial"
```

## Anti-patterns (reject on sight)
- A requirement that names a part instead of a property ("use an LM2596") — parts are Phase 4
  decisions; the HRS states the property. Client-mandated parts go in constraints, with the
  mandate noted.
- Cost target without a quantity, or size without units.
- "Industrial temperature range" without the actual range.
- Verification method chosen for convenience over strength.
