# Commercial release, sustaining and retirement

## Economics and launch

Track recurring cost at the planned volume and explicit amortization assumptions. Use
`commercial/cost-model.csv`: category, description, quantity, unit_cost, currency, source,
assumption. `commercial` requires components, assembly, test, yield_loss, packaging, freight,
duties, certification, development, warranty, returns, support, channel, and overhead. Source
paths are relative to the CSV. A zero line needs a specific rationale; one pinned currency is
required. This completeness check cannot approve pricing or predict demand.

Keep inventory, MOQs, lead times, NRE/tooling cash, working capital, payment terms, forecast,
channel pricing/margin, exchange assumptions and stop criteria in the commercial review.
Separate accounting definitions of COGS, operating costs and capitalized/amortized development;
the checker totals the declared model and does not prescribe accounting treatment.

G7 needs approved SKU configurations, current destination evidence, languages/labels/packaging,
responsible operators/importers, availability/capacity, logistics and battery transport where
applicable. Validate installation, onboarding, normal user tasks and service. Assign warranty,
returns, repairs, spare parts, training, vulnerability contact, update delivery and escalation.
Identify who can authorize or stop shipment and initiate a field action. HW-035–041 and
AUTO-COST make this separate from production readiness.

## Field operation and change

Use `sustaining/incident-register.csv` for complaints, faults and vulnerabilities with affected
configuration/serial range, severity, owner, deadlines, containment, corrective action and
closure evidence. Do not publish reports or contact customers without session authorization.
Track production/field metrics by configuration and time period, including returns, escapes,
rework, update health and recurring failures. Escalate safety and reporting obligations through
the actual responsible owner and destination process.

Use `sustaining/change-register.csv` for supplier PCN/EOL, alternate parts, firmware, tools,
processes, calibration or materials changes. Record reason, affected configurations and serials,
risk/standards impact, gates reopened, verification, effectivity, approvals and service action.
Check interchangeability, electrical/thermal margins, mechanical fit, software compatibility,
test limits, regulatory evidence, supply records and installed-base implications. Refresh source
availability proactively; an absent supplier notice is not evidence of continued availability.

Anvil conservatively invalidates G3+ receipts whenever a manifested design file changes.
Archive old release packages and approvals; create a new manifest and evidence for the new
configuration. Do not rewrite a historical shipped-unit record to make it match the new design.

## Retirement

Plan support duration, owners and funding before launch. At retirement decide last production,
last service, spares/repair obligations, customer notices, software/bootloader compatibility,
offline behavior, cloud shutdown, data export/deletion, credential and signing-key custody,
ownership transfer and recycling/disposal. Resolve products that remain installed after cloud
or vendor dependency support ends. Document which security and legal obligations continue.
HW-042–047 requires periodic or event-triggered reviewed sustaining/retirement evidence; it
does not automatically schedule monitoring or shut down services.
