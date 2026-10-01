# Reference-mining brief (read fully before starting)

You are extracting engineering knowledge from ONE reference text for **Anvil**, a hardware-design
plugin that designs, simulates, lays out, and releases electronic hardware products through an
autoresearch-style loop (modify → verify → keep/discard) with mechanical gates (ERC/DRC/ngspice
simulation/DFM/system budgets). Anvil's weakness today is that its design guidance is qualitative.
Your extraction turns this book into **cited, quantitative, mechanizable design rules and checks**.

## Method (mandatory)

1. Read the assigned line range of the text file with the Read tool in sequential chunks
   (offset/limit ≤ 2000 lines each). Start with the book's front matter/TOC (first ~800 lines of the
   file, even if outside your range) to orient yourself. Then read your range **in order**. Do not
   skip chunks; do not rely on Grep alone. Skip only: exercises/problem sets, long pure-math
   derivations, index pages, historical anecdotes. Engineering examples with numbers are NOT skippable.
   Some files have very long lines: if a Read result reports it was truncated/capped, re-read that
   span with a smaller `limit` (e.g. 400–800 lines) so that no lines are skipped.
2. As you read, accumulate rules into the output file (write incrementally with Write, then
   Edit/append, so nothing is lost if you run out of budget). Copy numbers, units, and conditions
   **exactly**. Never invent a number. If the text gives a formula, transcribe it in plain ASCII
   (e.g. `Z0 = 87/sqrt(er+1.41) * ln(5.98*h/(0.8*w+t))`) with every symbol defined and units.
3. Page references: the extraction preserves printed page numbers as stray lines; also form-feed
   characters mark PDF page breaks. Cite `p.NNN` (printed) when visible, else `§chapter.section`.
   Cite the exact figure/table number when a value comes from one.
4. Confidence tags: `high` = explicit numeric/formula stated in the text; `medium` = you derived
   it from a stated relation; `low` = qualitative guidance you quantified — mark clearly.

Tooling note: create and extend files with the Write/Edit tools. A hook blocks Bash heredocs and
any shell command that mentions a `*.log` filename. Keep scratch parts in a subfolder named after
your BOOKTAG and assemble them into the single output file before you finish.

## Output file format (markdown)

```
# <Book title> — Anvil rulebook
## 0. Citation
IEEE-style reference (authors, title, edition, publisher, year, ISBN if printed). Chapters covered
by THIS extraction (list), chapters NOT read (list, with reason).
## 1. Design rules
| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
- id: <BOOKTAG>-NNN (BOOKTAG given in your task). domain ∈ {power, pdn, decoupling, grounding,
  return-path, transmission-line, crosstalk, termination, timing, emc, esd, thermal, current-carrying,
  via, stackup, materials, dfm, fab, assembly, solder, test, bringup, hw-fw, firmware, rf, antenna,
  matching, filter, magnetics, control-loop, protection, components, derating, reliability,
  mechanical, connectors, cables, requirements, process, cost, compliance}.
- verify by ∈ {calc, sim, measure, inspect, review}. One row per rule. Hundreds of rows are welcome.
## 2. Formulas & tables (numbers)
Reproduce every useful table (material properties, ampacity, clearance, resistivity, dielectric
constants, loss tangents, thermal resistances, derating factors, standard values, tolerances...) as
markdown tables with units and source. Precision matters.
## 3. Mechanizable checks
For each check a Python function could compute from tabular design inputs:
`CHECK-name`: inputs (columns, units) → formula → pass criterion → margin definition → source rows.
## 4. Verification procedures & plots
What simulation/test/plot demonstrates each important property: x/y axes, sweep/corners, what
'good' looks like, pass criteria, instrument/setup notes. (Anvil will auto-generate these plots.)
## 5. Pitfalls, failure modes, review checklist
Concrete, checkable items (one line each) with source.
## 6. Standards referenced
Standard id, edition/year if given, clause/table if given, what it governs, page.
## 7. Process / lifecycle guidance (only if the book is about product development, DFM, test, mfg)
Stage → activity → deliverable → exit criterion, with source.
## 8. Coverage log
Line ranges read; anything skipped and why; extraction limitations (OCR noise, missing figures).
```

## Quality bar

- Precision over volume, but volume matters: a 400-page engineering book typically yields
  150–400 rules. Target 25–80 KB of output for a full book; more if rule-dense.
- Prefer rules with numbers/formulas. Qualitative rules are included only when they are checkable
  by inspection (e.g. "every IC VCC pin has a decoupling capacitor within X mm").
- Figures are not in the text. When a rule depends on a figure/graph, transcribe the figure's
  caption and any numeric anchors the prose gives; mark `conf=medium` and say "graph".
- Keep the author's conditions (frequency range, temperature, copper weight, class, voltage...).
- Do not summarize prose; extract rules. Do not editorialize.
- Finish with the Coverage log even if you had to stop early. Save the file before your final message.
- Your final message: 3 lines — output path, number of rules extracted, chapters not read.
