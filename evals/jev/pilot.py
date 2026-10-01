#!/usr/bin/env python3
"""Replay a small diagnostic corpus; expected labels are never sent to Jev."""
import argparse
from datetime import datetime, timezone
import getpass
import json
import math
import os
from pathlib import Path
import statistics
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import jev_triage as jev


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cases", type=Path)
    parser.add_argument("output", type=Path, help="new run directory")
    parser.add_argument("--prompt-key", action="store_true")
    args = parser.parse_args()
    corpus = jev.read_json(args.cases)
    cases = corpus["cases"]
    jev.require(0 < len(cases) <= 30, "pilot requires 1 to 30 cases")
    jev.require(len({case["packet"]["id"] for case in cases}) == len(cases), "duplicate case IDs")
    for case in cases:
        jev.require(case["expected_tracks"] and set(case["expected_tracks"]) <= jev.TRACKS.keys(), "invalid expected labels")
    key = getpass.getpass("TypeSafe API key (not saved): ") if args.prompt_key else os.getenv("TYPESAFE_API_KEY", "")
    jev.require(bool(key), "set TYPESAFE_API_KEY or use --prompt-key")
    args.output.mkdir(parents=True, exist_ok=False)
    records = []
    with (args.output / "results.jsonl").open("x", encoding="utf-8") as stream:
        for case in cases:
            result = jev.triage(case["packet"], key=key)
            actual = result.get("answers", {}).get("review_track", {}).get("choice")
            record = dict(id=case["packet"]["id"], origin=case["origin"], expected=case["expected_tracks"],
                          actual=actual, match=actual in case["expected_tracks"], result=result)
            records.append(record)
            stream.write(json.dumps(record, allow_nan=False) + "\n")
            stream.flush()
            print(f"{record['id']}: {actual or result['fallback_reason']}; {result['elapsed_ms']} ms", flush=True)
            if result["fallback_reason"] in {"http_401", "http_403", "http_429", "http_529"}:
                break  # Stop a batch when credentials, account access or capacity prevent evaluation.
    key = None
    valid = [r for r in records if "answers" in r["result"]]
    accepted = [r for r in valid if r["result"]["suggested_track"]]
    timings = sorted(r["result"]["elapsed_ms"] for r in records)
    input_tokens = sum(r["result"]["usage"]["input_tokens"] for r in valid)
    summary = dict(created_at=datetime.now(timezone.utc).isoformat(), model=jev.MODEL,
                   corpus_sha256=jev.json_digest(corpus), planned=len(cases), attempted=len(records),
                   valid_responses=len(valid), matching_labels=sum(r["match"] for r in valid),
                   suggestions=len(accepted), matching_suggestions=sum(r["match"] for r in accepted),
                   fallbacks=len(records)-len(accepted), input_tokens=input_tokens,
                   estimated_usd=round(input_tokens / 1_000_000 * .042, 8),
                   p50_ms=statistics.median(timings), p95_ms=timings[math.ceil(.95 * len(timings))-1],
                   limitation="Diagnostic cases and assistant-authored labels; not held-out accuracy or an engineering approval.")
    (args.output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    lines = ["Jev diagnostic pilot", "", summary["limitation"], "",
             f"Pinned model: {jev.MODEL}. {len(records)}/{len(cases)} cases attempted; {len(valid)} valid responses.",
             f"Labels matched: {summary['matching_labels']}/{len(valid)}. Advisory suggestions: {len(accepted)}; matching suggestions: {summary['matching_suggestions']}.",
             f"p50/p95 elapsed: {summary['p50_ms']:.2f}/{summary['p95_ms']:.2f} ms, including failed calls.",
             f"Reported input tokens: {input_tokens}; estimated successful-call cost: ${summary['estimated_usd']:.8f} at $0.042/M input tokens.",
             "Price source: [TypeSafe models](https://docs.typesafe.ai/models). Failed-call billing was not observable.", "",
             "| Case | Expected review track(s) | Jev | Fallback |", "|---|---|---|---|"]
    for record in records:
        lines.append(f"| {record['id']} | {', '.join(record['expected'])} | {record['actual'] or '-'} | {record['result']['fallback_reason'] or '-'} |")
    lines += ["", "The corpus preserves provenance locally and supplies only each packet's state to Jev. Expected labels and source documents are not uploaded.",
              "No ledger, manifest, receipt, handoff, design or release criterion was modified by this evaluator.",
              "The 0.8 confidence threshold is exploratory. These results do not establish calibration, cost savings versus the host agent, or prospective debugging accuracy.",
              "Next evaluation: fresh decision-time cases, independently reviewed labels, and a rules/host-agent baseline before any automatic routing."]
    (args.output / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0 if len(valid) == len(cases) else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, TypeError):
        print("JEV_PILOT_ERROR: check corpus, credential availability and new output directory", file=sys.stderr)
        sys.exit(2)
