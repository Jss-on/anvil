#!/usr/bin/env python3
"""Audit documentation: every research citation, execution instance, iteration, BOM, result and plot
of a project, assembled from the project's own evidence into audit/AUDIT.md, audit/audit.json and an
IEEE-style paper skeleton (audit/paper/paper.tex + refs.bib). Standard library only; plots optional.

The report never computes readiness: it quotes the receipts and the last `gate` result verbatim.
"""
from __future__ import annotations

import csv
import io
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from anvil import GATES, gate, package_root, project, read_json, results, table

ITERATION_FIELDS = ["n", "timestamp", "phase", "change", "metric", "value", "checks", "result", "files", "rules", "note"]
DECISION_FIELDS = ["id", "timestamp", "topic", "decision", "alternatives", "rules", "sources", "requirement", "note"]
RESEARCH_FIELDS = ["id", "timestamp", "kind", "source", "locator", "claim", "used_for", "rules"]
LEDGERS = {"iteration": ("iterations.tsv", ITERATION_FIELDS, None), "decision": ("decisions.tsv", DECISION_FIELDS, "D"),
           "research": ("research.tsv", RESEARCH_FIELDS, "SRC")}  # `anvil.py log` ledger -> (audit file, columns, id prefix)


def reference_root():
    for candidate in (package_root() / ".claude/skills/anvil/references", package_root() / "references"):
        if (candidate / "bibliography.json").is_file():
            return candidate
    raise ValueError("bibliography.json not found beside the installed Anvil references")


def optional_table(path, fields):
    path = Path(path)
    if not path.is_file():
        return []
    return table(path, fields, allow_empty=True)


def append_row(path, fields, row, prefix=None):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    new = not path.exists()
    existing = optional_table(path, fields) if not new else []
    row = dict(row)
    if "n" in fields and not row.get("n"):
        row["n"] = str(len(existing) + 1)
    if prefix and not row.get("id"):
        row["id"] = f"{prefix}-{len(existing) + 1}"
    row.setdefault("timestamp", datetime.now(timezone.utc).isoformat(timespec="seconds"))
    for key in fields:
        row.setdefault(key, "")
    with path.open("a", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        if new:
            writer.writeheader()
        writer.writerow(row)
    return path


def md_table(rows, columns, headers=None):
    if not rows:
        return "_none_\n"
    headers = headers or columns
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(columns)]
    for row in rows:
        out.append("| " + " | ".join(str(row.get(c, "")).replace("|", "\\|").replace("\n", " ") for c in columns) + " |")
    return "\n".join(out) + "\n"


def receipts(root):
    found = []
    for path in sorted((root / "evidence").glob("*.json")) if (root / "evidence").is_dir() else []:
        if path.name.endswith(".draft.json"):
            continue
        try:
            data = read_json(path)
        except ValueError:
            continue
        if not isinstance(data, dict) or not data.get("check_id"):  # the project template's blank receipt names no check
            continue
        transcript = data.get("transcript")
        text = (root / transcript).read_text(encoding="utf-8", errors="replace") if transcript and (root / transcript).is_file() else ""
        found.append(dict(path=path.relative_to(root).as_posix(), data=data, transcript=text))
    return found


def margins(transcript):
    out = []
    for line in transcript.splitlines():
        match = re.match(r"^(\S+)(?: (\{.*\}))?: (\S+) (\S+) margin=(\S+) (PASS|FAIL)$", line)
        if match:
            out.append(dict(id=match[1], corner=match[2] or "", value=match[3], units=match[4], margin=match[5], status=match[6]))
            continue
        match = re.match(r"^(\S+): margin=(\S+) (\S+)$", line)
        if match:
            out.append(dict(id=match[1], corner="", value="", units=match[3], margin=match[2], status="PASS" if float(match[2]) >= 0 else "FAIL"))
    return out


def analyze_iterations(rows):
    """Mechanical trajectory analysis of audit/iterations.tsv (autoresearch loop ledger)."""
    if not rows:
        return dict(verdict="NO_ITERATIONS", kept=0, tried=0)
    kept = [r for r in rows if r["result"] == "keep"]
    values = []
    for r in kept:
        try:
            values.append(float(r["value"]))
        except ValueError:
            pass
    streak, longest = 0, 0
    for r in rows:
        streak = 0 if r["result"] == "keep" else streak + 1
        longest = max(longest, streak)
    verdict = "CONTINUE"
    if streak >= 5:
        verdict = "PLATEAU"
    regressions = [r for r in rows if r["result"] == "discard" and "regress" in r["note"].lower()]
    return dict(verdict=verdict, kept=len(kept), tried=len(rows), consecutive_no_improvement=streak,
                longest_dry_streak=longest, first_value=values[0] if values else None,
                last_value=values[-1] if values else None, regressions=len(regressions),
                metrics=sorted({r["metric"] for r in rows if r["metric"]}))


def load_bibliography():
    data = read_json(reference_root() / "bibliography.json")
    return {entry["key"]: entry for entry in data["entries"]}


def cited_keys(decisions, research, rule_ids, bib):
    keys = set()
    for row in decisions + research:
        for token in re.split(r"[;,\s]+", row.get("sources", "") + " " + row.get("source", "")):
            if token in bib:
                keys.add(token)
    for rule in rule_ids:
        prefix = rule.split("-")[0]
        for key, entry in bib.items():
            if prefix in entry.get("rule_prefixes", []):
                keys.add(key)
    return sorted(keys)


def rule_ids_in(rows):
    ids = set()
    for row in rows:
        ids |= {t for t in re.split(r"[;,\s]+", row.get("rules", "")) if t}
    return ids


def build(root_path, target=None):
    root, cfg = project(root_path)
    audit = root / "audit"
    audit.mkdir(exist_ok=True)
    reqs = table(root / cfg["requirements"], ("id", "statement", "units", "conditions", "method", "gate", "owner"), allow_empty=True)
    ledger = results(root / "anvil-results.tsv") if (root / "anvil-results.tsv").is_file() else []
    plan = read_json(root / "lifecycle-plan.json") if (root / "lifecycle-plan.json").is_file() else {"checks": []}
    manifest = read_json(root / "release-manifest.json") if (root / "release-manifest.json").is_file() else None
    verdict, blockers = gate(root, target or cfg["target_gate"])
    iterations, decisions, research = (optional_table(audit / name, fields) for name, fields, _ in LEDGERS.values())
    evidence = receipts(root)
    bib = load_bibliography()
    rules_used = rule_ids_in(iterations) | rule_ids_in(decisions) | rule_ids_in(research)
    for item in evidence:
        rules_used |= set(re.findall(r"\b([A-Z][A-Z0-9]{2,}-\d{3,4})\b", item["transcript"]))
    keys = cited_keys(decisions, research, rules_used, bib)
    boms = []
    for role in ("bom", "product_bom"):
        for name in cfg["artifacts"].get(role, []):
            if name.endswith(".csv") and (root / name).is_file():
                boms.append((name, table(root / name, allow_empty=True)))
    plots = sorted(p.name for p in (audit / "plots").glob("*.png")) if (audit / "plots").is_dir() else []
    renders = sorted(p.name for p in (audit / "renders").glob("*") if p.suffix.lower() in {".png", ".svg", ".pdf"}) if (audit / "renders").is_dir() else []
    board = root / "analysis"  # layout/si/pdn/thermal/em/emc outputs written by the board analyses
    board_figures = sorted(p.relative_to(root).as_posix() for p in board.rglob("*.png")) if board.is_dir() else []
    board_data = sorted(p.relative_to(root).as_posix() for p in board.rglob("*")
                        if re.fullmatch(r"\.(s\d+p|cir|xml)", p.suffix.lower())) if board.is_dir() else []
    analysis = analyze_iterations(iterations)
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")

    doc = [f"# Audit record: {cfg['name']} (hardware revision {cfg['hardware_revision']})", "",
           f"Generated {now} by Anvil from the project's own evidence. Release kind `{cfg['release_kind']}`, "
           f"target gate `{target or cfg['target_gate']}`, sectors {cfg['sectors']}, markets {cfg['markets']}, features {cfg['features']}.", "",
           f"**Gate result: `{verdict}`** with {len(blockers)} blocker(s)." + ("" if not blockers else "\n\n" + "\n".join(f"- {b}" for b in blockers)), "",
           "This document quotes receipts and transcripts; it does not itself authorize release.", "",
           "## 1. Requirements", "", md_table(reqs, ["id", "statement", "units", "conditions", "method", "gate", "owner"]),
           "## 2. Research and sources consulted", "",
           md_table(research, ["id", "timestamp", "kind", "source", "locator", "claim", "used_for", "rules"]),
           "## 3. Design decisions", "",
           md_table(decisions, ["id", "timestamp", "topic", "decision", "alternatives", "rules", "sources", "requirement"]),
           "## 4. Iteration ledger (modify → verify → keep/discard)", "",
           f"Analysis: **{analysis['verdict']}** — {analysis['kept']} kept of {analysis['tried']} tried; "
           f"consecutive non-improving: {analysis.get('consecutive_no_improvement', 0)}; metrics: {', '.join(analysis.get('metrics', [])) or '-'}.", "",
           md_table(iterations, ["n", "timestamp", "phase", "change", "metric", "value", "checks", "result", "rules", "note"]),
           "## 5. Execution instances (receipts)", ""]
    exec_rows = []
    for item in evidence:
        d = item["data"]
        exec_rows.append(dict(check=d.get("check_id"), status=d.get("status"), producer=d.get("producer"), method=d.get("method"),
                              command=" ".join(d.get("command", [])) if isinstance(d.get("command"), list) else "",
                              tool=next((line.strip("* ") for line in d.get("tool_version", "").splitlines() if re.search(r"[A-Za-z0-9]", line)),
                                        d.get("approval", {}).get("role", "")),  # ngspice's banner starts with a row of stars
                              created=d.get("created_at", ""), files=len(d.get("files", {})), receipt=item["path"]))
    doc.append(md_table(exec_rows, ["check", "status", "producer", "method", "command", "tool", "created", "files", "receipt"]))
    doc += ["### 5.1 Measured margins", ""]
    margin_rows = []
    for item in evidence:
        for m in margins(item["transcript"]):
            margin_rows.append(dict(check=item["data"].get("check_id"), **m))
    doc.append(md_table(margin_rows, ["check", "id", "corner", "value", "units", "margin", "status"]))
    doc += ["### 5.2 Transcripts", ""]
    for item in evidence:
        if item["transcript"]:
            doc += [f"<details><summary>{item['data'].get('check_id')} — {item['data'].get('transcript')}</summary>", "", "```text",
                    item["transcript"].strip()[:20000], "```", "</details>", ""]
    doc += ["## 6. Lifecycle ledger", "", md_table(ledger, ["n", "dimension", "assertion", "status", "evidence", "traces"]),
            "## 7. Bills of materials", ""]
    for name, rows in boms:
        doc += [f"### {name}", "", md_table(rows, list(rows[0].keys()) if rows else [])]
    doc += ["## 8. Verification plots and renders", ""]
    doc += [f"![{p}](plots/{p})" for p in plots] + [""] + [f"- [renders/{r}](renders/{r})" for r in renders] + [""]
    doc += ["### 8.1 Board analyses (S-parameters, PDN impedance, SI waveforms, heat map, emission estimate)", ""]
    doc += [f"![{p}](../{p})" for p in board_figures] + [""]
    doc += [f"- [{p}](../{p}) (Touchstone / SPICE deck / openEMS model as simulated)" for p in board_data] + [""]
    doc += ["## 9. Release manifest", ""]
    if manifest:
        doc.append(f"Configuration digest `{manifest.get('sha256')}`; {len(manifest.get('files', {}))} controlled files.\n")
        doc.append(md_table([dict(file=k, sha256=v) for k, v in sorted(manifest.get("files", {}).items())], ["file", "sha256"]))
    else:
        doc.append("_no release manifest yet_\n")
    doc += ["## 10. References", ""]
    for n, key in enumerate(keys, 1):
        doc.append(f"[{n}] {bib[key]['ieee']}")
    doc += ["", "Rule identifiers cited: " + (", ".join(sorted(rules_used)) or "-"), ""]
    (audit / "AUDIT.md").write_text("\n".join(doc), encoding="utf-8")
    summary = dict(schema_version=1, generated_at=now, project=cfg["name"], hardware_revision=cfg["hardware_revision"],
                   gate=target or cfg["target_gate"], verdict=verdict, blockers=blockers, requirements=len(reqs),
                   receipts=len(evidence), iterations=analysis, decisions=len(decisions), research=len(research),
                   rules_cited=sorted(rules_used), references=[bib[k]["ieee"] for k in keys], plots=plots, renders=renders,
                   board_figures=board_figures, board_data=board_data,
                   release_sha256=manifest.get("sha256") if manifest else None)
    (audit / "audit.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    write_paper(audit, cfg, reqs, decisions, iterations, margin_rows, exec_rows, keys, bib, verdict, analysis,
                [f"audit/plots/{p}" for p in plots] + board_figures)
    return f"AUDIT: {audit / 'AUDIT.md'} ({len(evidence)} receipts, {len(iterations)} iterations, {len(keys)} references)"


TEX_SYMBOLS = {"\\": "\\textbackslash{}", "<=": "$\\le$", ">=": "$\\ge$", "<": "\\textless{}", ">": "\\textgreater{}",
               "|": "\\textbar{}", "~": "\\textasciitilde{}", "^": "\\textasciicircum{}", "λ": "$\\lambda$", "Ω": "$\\Omega$",
               "µ": "$\\mu$", "μ": "$\\mu$", "ε": "$\\varepsilon$", "θ": "$\\theta$", "±": "$\\pm$", "×": "$\\times$",
               "≤": "$\\le$", "≥": "$\\ge$", "≈": "$\\approx$", "→": "$\\rightarrow$", "√": "$\\surd$", "°": "\\textdegree{}"}
TEX_PATTERN = re.compile("[&%$#_{}]|" + "|".join(re.escape(k) for k in sorted(TEX_SYMBOLS, key=len, reverse=True)))


def tex(text):
    """Plain text -> LaTeX text mode in one pass: specials escaped; OT1 would print < > | as ¡ ¿ —, and pdflatex
    stops on Greek letters, so those are set as symbols."""
    return TEX_PATTERN.sub(lambda m: TEX_SYMBOLS.get(m[0], "\\" + m[0]), str(text))


def tex_table(rows, columns, caption, label, wrap=()):
    """IEEE table; the columns named in `wrap` wrap inside a full-width table* (tabularx), the rest stay on one line."""
    if not rows:
        return ""
    body = " \\\\\n".join(" & ".join(tex(r.get(c, "")) for c in columns) for r in rows)
    spec = "|".join(">{\\raggedright\\arraybackslash}X" if c in wrap else "l" for c in columns)
    env = "table*" if wrap else "table"
    begin, end = (f"\\begin{{tabularx}}{{\\textwidth}}{{{spec}}}", "\\end{tabularx}") if wrap else (f"\\begin{{tabular}}{{{spec}}}", "\\end{tabular}")
    head = " & ".join(f"\\textbf{{{tex(c)}}}" for c in columns)
    return (f"\\begin{{{env}}}[!t]\n\\caption{{{tex(caption)}}}\n\\label{{{label}}}\n\\centering\n\\scriptsize\n"
            f"{begin}\n\\hline\n{head} \\\\\n\\hline\n{body} \\\\\n\\hline\n{end}\n\\end{{{env}}}\n")


FIGURE_KINDS = {"plots": "Circuit simulation at declared corners", "em": "openEMS S-parameters of the board copper",
                "pdn": "PDN impedance against Z_target", "si": "Signal-integrity waveform", "thermal": "Board temperature",
                "emc": "Radiated-emission estimate against the limit line", "layout": "Copper"}


def write_paper(audit, cfg, reqs, decisions, iterations, margin_rows, exec_rows, keys, bib, verdict, analysis, figure_paths=()):
    paper = audit / "paper"
    paper.mkdir(exist_ok=True)
    cites = " ".join(f"\\cite{{{k}}}" for k in keys)
    figures = "\n".join(  # project-relative PNGs, included from audit/paper/
        f"\\begin{{figure}}[!t]\n\\centering\n\\includegraphics[width=\\columnwidth,height=0.45\\textheight,keepaspectratio]{{../../{p}}}\n"
        f"\\caption{{{tex('Assertion margins of every check' if Path(p).stem == 'margins' else FIGURE_KINDS.get(Path(p).parent.name, Path(p).parent.name))}: {tex(Path(p).stem)}}}\n"
        f"\\label{{fig:{re.sub(r'[^A-Za-z0-9]+', '-', Path(p).parent.name + '-' + Path(p).stem)}}}\n\\end{{figure}}" for p in figure_paths)
    def closeness(row):  # margin relative to the limit (|limit| = |value| + |margin| for le/ge rows); counts go last
        try:
            value, margin = float(row["value"] or 0), float(row["margin"])
        except ValueError:
            return (2, 0.0)
        return (int(row["units"] in {"count", "present"}), margin / (abs(value) + abs(margin) or 1.0))

    tightest = {}
    for row in margin_rows:  # the paper keeps each check's closest call; AUDIT.md lists every row
        if row["check"] not in tightest or closeness(row) < closeness(tightest[row["check"]]):
            tightest[row["check"]] = row
    body = rf"""\documentclass[conference]{{IEEEtran}}
\usepackage{{cite,graphicx,booktabs,url,tabularx}}
\begin{{document}}
\title{{{tex(cfg['name'])}: Design, Verification and Release Evidence for Hardware Revision {tex(cfg['hardware_revision'])}}}
\author{{\IEEEauthorblockN{{Author Name}}\IEEEauthorblockA{{Affiliation\\email@example.com}}}}
\maketitle
\begin{{abstract}}
% Auto-generated skeleton. Replace with the actual contribution statement.
This paper documents the requirements, design method, verification and release evidence of a {tex(cfg['release_kind'])}-scope electronic product.
The design was developed with an iterative modify--verify--retain loop ({analysis['kept']} retained of {analysis['tried']} candidate changes) and gated by
electrical-rule, design-rule, corner simulation and rule-based checks. The current gate result is \texttt{{{tex(verdict)}}}.
\end{{abstract}}
\begin{{IEEEkeywords}}
hardware design, verification, PCB, design rules, evidence
\end{{IEEEkeywords}}

\section{{Introduction}}
State the problem, intended use and the contribution. Sources consulted during design: {cites}.

\section{{Requirements}}
{tex_table(reqs, ["id", "statement", "units", "conditions", "method", "gate"], "Requirements baseline", "tab:reqs", wrap=("statement", "conditions"))}

\section{{Design Method}}
Describe the architecture and the design rules applied (see Table~\ref{{tab:decisions}}).
{tex_table(decisions, ["id", "topic", "decision", "rules", "sources"], "Design decisions and the rules that justify them", "tab:decisions", wrap=("decision", "rules", "sources"))}

\section{{Verification}}
Every check executed is recorded as a hashed receipt (Table~\ref{{tab:exec}}); the closest call of each, relative to its limit, is in Table~\ref{{tab:margins}}.
{tex_table(exec_rows, ["check", "status", "method", "tool", "created"], "Execution instances", "tab:exec", wrap=("tool",))}
{tex_table(list(tightest.values()), ["check", "id", "corner", "value", "units", "margin", "status"], "Closest call of each check, relative to its limit (every row: AUDIT.md)", "tab:margins", wrap=("id", "corner"))}
{figures}

\section{{Iteration Results}}
{tex_table(iterations, ["n", "change", "metric", "value", "result"], "Iteration ledger", "tab:iter", wrap=("change", "value"))}

\section{{Conclusion}}
Summarize what was demonstrated, the remaining blockers and the intended next gate.

\bibliographystyle{{IEEEtran}}
\bibliography{{refs}}
\end{{document}}
"""
    (paper / "paper.tex").write_text(body, encoding="utf-8")
    entries = []
    for key in keys:
        e = bib[key]
        authors = " and ".join(n for n in re.split(r",\s*(?:and\s+)?|\s+and\s+", e["author"]) if n.strip())  # BibTeX: "A and B"
        fields = [f"  title={{{e['title']}}}", f"  author={{{authors}}}", f"  year={{{e['year']}}}"]
        for name in ("publisher", "edition", "isbn", "note"):
            if e.get(name):
                fields.append(f"  {name}={{{e[name]}}}")
        entries.append(f"@{e.get('type', 'book')}{{{key},\n" + ",\n".join(fields) + "\n}")
    (paper / "refs.bib").write_text("\n\n".join(entries) + "\n", encoding="utf-8")
    (paper / "README.md").write_text("Build with `pdflatex paper && bibtex paper && pdflatex paper && pdflatex paper` "
                                     "(IEEEtran class required). The skeleton is generated from audit data; prose sections are placeholders.\n", encoding="utf-8")
