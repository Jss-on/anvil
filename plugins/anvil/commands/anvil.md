---
name: anvil
description: "Run a bounded hardware iteration loop or route requirements, builds, optimization, and lifecycle reviews"
argument-hint: "[Goal: ...] [Metric: ...] [Scope: ...] [Verify: ...] [Iterations: N]"
---

Read the Anvil skill and resolve its installed tools. Route a new design to `anvil:build`,
raw needs to `anvil:requirements`, lifecycle or release work to `anvil:lifecycle`, and an
existing hardware cost/area/margin optimization to `anvil:improve`.

For a custom metric loop, infer the authorized scope and goal; default to 10 iterations.
Inspect repository instructions and user changes. Establish the baseline with the declared
verification command. Inspect a supplied command before running it; quoting, network writes,
destructive operations, and executable content remain subject to the session's authorization.
Missing tools or failing execution produce an error, never a numeric pass.

Choose one useful change, verify it, then retain it only if it improves the metric and preserves
all required checks. Restore only the agent's change on regression. Commit when authorized or
expected by the repository workflow; do not create a remote or push by default. Stop on the
iteration bound or five consecutive attempts without improvement, preserving the best state.

Record exact metric values, command exit status, changed files, evidence paths, and why the
change was retained or discarded. A plateau does not complete an unmet user objective; report
the remaining constraint and pursue useful independent work.

For hardware release claims, run `gate <project> <G0..G7|Sustaining>` from the resolved Anvil
tool path. Do not convert a weighted score or an optimization verdict into release readiness.
Write `handoff <project> --write anvil` and validate the handoff before chaining. A generic
non-product loop can report its metric without a lifecycle release claim.
