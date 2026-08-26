# Harness Protocol

Wiring design — the copper between subsystems. Every ICD `power|signal` edge is realized here as
wire the assembler can cut, crimp, and route. Undersized battery leads are a fire, a missing
ground is a dead stack, and a guessed connector is an assembly-day stall — so the harness is a
**table the `pinout` gate checks**, not a diagram in someone's head.

## The harness table (`harness/harness.tsv`)

```
wire_id	icd_id	from	to	signal	awg	length_mm	current_a	color	notes
W-1	ICD-1	BAT-1.XT60+	PDB.VIN+	VBAT	12	60	60	red	pre-tinned, strain relief at PDB
W-2	ICD-1	BAT-1.XT60-	PDB.VIN-	GND	12	60	60	black	
W-3	ICD-2	FC.J3.1	ESC-1.J1.1	DSHOT_M1	28	85	0.1	white	inside loom L-1
W-4	ICD-3	FC.J4.5	VTX-1.J1.2	SMARTAUDIO	30	70	0.05	yellow	
```

- `from`/`to` are `<endpoint>.<connector>.<pin>` — endpoints are subsystem realizations
  (module_id from the COTS catalog, or `<board>.<ref>` for a custom PCB connector from its
  netlist). Free-text endpoints don't verify; they're a red row.
- `icd_id` links every wire to the interface it realizes. A wire with no ICD row, or a
  `power|signal` ICD row with no wire (and no board-to-board connector), is a `pinout` violation.
- `current_a` is the worst-case current **from the ICD row** — not re-estimated per wire.

## Ampacity floor (bundled/chassis, conservative)

`pinout` red-flags any wire whose `current_a` exceeds its gauge's floor:

| AWG | 30 | 28 | 26 | 24 | 22 | 20 | 18 | 16 | 14 | 12 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A max | 0.5 | 0.8 | 1.3 | 2.0 | 3.0 | 5.0 | 7.0 | 10 | 15 | 25 | 35 |

Short unbundled power leads (< 150 mm, free air, burst duty — e.g. quad battery pigtails) may use
the high-duty column ×2 **only** with a logged justification in `harness/README.md`; silence
means the floor applies. Voltage drop on power runs: `2 × length × I × ρ(awg)` shown against the
rail tolerance for any run > 300 mm.

## Connector mate table (`harness/mates.tsv`)

```
mate_id	side_a	side_b	series	pins	crimp_tool	notes
MT-1	BAT-1.XT60	W-1/W-2 pigtail	XT60	2	solder	polarity keyed
MT-2	FC.J3	loom L-1	JST-SH 1.0	8	SH crimp or pre-crimped	buy pre-crimped
```

Every connector named in the harness table appears in exactly one mate row; a mate whose two
sides are different series is a violation (adapters are their own wire rows, not a mate hack).

## Rules

1. **Polarity + keying:** every power mate is keyed (XT60/XT30/JST-RCY) or its pin-1 convention
   is stated in `notes`. Reversible power mates on field-swapped items are a must-be violation.
2. **Loom discipline:** wires sharing a route belong to a named loom (`L-n` in notes) with
   length matched to the routed path from the mechanical model — not "close enough".
3. **Strain relief** at every wire exit per the mechanical protocol; service loops ≥ 1 bend
   radius at board ends.
4. **RF separation:** video/RF coax never loomed parallel to motor phase or battery leads;
   crossings at 90°. Noted per wire in `notes`.
5. **Gauge is chosen from the table, not vibes** — and the gate re-checks it every iteration.

## The gate

`score-anvil.sh pinout harness/harness.tsv system/icd.tsv` → `PINOUT_VIOLATIONS: N` (stderr:
one line per violation). Checks: every wire's `icd_id` exists; every `power|signal` ICD row is
realized by ≥ 1 wire; `current_a ≤ ampacity(awg)`; endpoints are well-formed
`<endpoint>.<connector>.<pin>`; mates table covers every connector once. N must be 0 before the
integration phase gate lifts.
