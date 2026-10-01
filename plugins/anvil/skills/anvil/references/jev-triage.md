# Optional Jev triage

Use only when the user enables Jev for the session (for example `Jev: shadow`) and
authorizes sending selected findings to TypeSafe. Existing authorization persists.
It is optional: no API key, an outage, or an abstention leaves the normal workflow available.

First handle exact conditions with Anvil: missing files/tools, failed measurements, stale
receipts, missing physical tests and the plateau counter do not require inference.
For an ambiguous failure, prepare one small JSON packet in the project run directory:

```json
{
  "id": "HR-14-brownout",
  "sources": ["sim/A-HR-14.log", "hrs/requirements.md#HR-14"],
  "state": {
    "criterion": "3V3 must remain at or above 3.10 V during the declared input sag",
    "observation": "Measured minimum 3.054 V; more output capacitance gave 2.815 V",
    "prior_attempts": ["Increasing output capacitance worsened the minimum voltage"],
    "proposed_action": "Increase output capacitance again"
  }
}
```

Supply only observations available at the decision time. Keep outcome labels, later
diagnoses, credentials and unrelated project content out of the packet. Source strings
are provenance references; the helper does not open them or scan the project.

Resolve `scripts/jev_triage.py` from the loaded skill as for `scripts/anvil.py`:

```sh
python -B /resolved/anvil/scripts/jev_triage.py /project/run/finding.json
```

Authentication reads `TYPESAFE_API_KEY`. For a manual run, `--prompt-key` reads it without
echo and does not persist it. Never put a key in the packet, command arguments, tracked
files or a report. The fixed HTTPS endpoint is https://api.typesafe.ai/v1/systemone;
redirects are rejected. The model is pinned to `jev-1.13.0`.

Stdout is a single advisory JSON record with the finding/source IDs, input/question
hashes, model, distributions, usage, elapsed time and fallback reason. Capture it in a
new run report if needed; never redirect it to a ledger, manifest, receipt or handoff.
Exit 0 means an advisory suggestion, 1 means fallback, and 2 means invalid input/options.
These exit codes say nothing about hardware acceptance. The helper itself writes no files.

The default confidence threshold is an uncalibrated 0.8; `--min-confidence` retains a tuning
knob. Confidence describes a distribution, not demonstrated correctness. An unknown track,
insufficient context, low confidence, missing credential, network failure or invalid response
falls back to the host agent. The default network I/O timeout is 10 seconds, with no retries.

This pilot only records suggestions. The host independently decides the next authorized
engineering action and runs actual checks. A Jev opinion cannot close requirements, choose
verification methods, waive corners, approve a release or become an Anvil evidence receipt.
Do not route actions automatically until a separate held-out evaluation establishes benefit.

Source API contract: [TypeSafe API](https://docs.typesafe.ai/api).
In the Anvil source checkout, `evals/jev/pilot.py` replays a supplied diagnostic corpus;
model opinions and agent-authored expected labels are not external engineering approvals.
