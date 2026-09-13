# Product classification, standards and market access

Research baseline: **14 September 2026**. Recheck binding rules, adopted editions, harmonized
lists, transitions and authority guidance for the SKU's intended use and actual launch date.
Profiles are planning prompts, not a legal classification or certification. The responsible
regulatory/quality owner approves applicability and evidence; Anvil cannot issue certificates.

`compliance/market-matrix.csv` records SKU, market, intended use/classification, legislation,
edition, effective date, route, authority, owner, required evidence, status, source URL and
checked date. Link hazard/risk controls, test reports, declarations, labels/instructions,
economic operators, registration, shipment and post-market obligations. Resolve scope early
at G1 and retain final external approval at G7. An approved NA needs rationale and expiry.

## Electronics and engineering standards

Select design/manufacturing/acceptance documents for their actual scope: IPC design guidance,
rigid-board performance, bare-board acceptance, assembly acceptability, soldering, land patterns,
current carrying, moisture handling and data exchange are different subjects. State the
contracted edition and class on drawings/RFQs and reconcile with supplier capability. Medical
or aerospace use alone does not mandate an IPC class. Use the actual standard and datasheet
for limits; this plugin intentionally supplies no universal clearance, ampacity, plating,
hole-fill, MSL or derating lookup table. [IPC scope and standards](https://www.ipc.org/ipc-design-standards).

For electrical/mechanical/thermal/battery hazards, select the applicable product safety standard
and installation conditions. Insulation coordination depends on working/transient voltage,
pollution, material, altitude and protective measures. IEC 62368-1, IEC 60601 families, machinery
standards and other product regimes have different applicability. A generic board guideline
does not replace those requirements.

## Sector routes

| Sector | Resolve and retain |
|---|---|
| Connected products | Device/service security, data/account/offline operation, dependencies, support duration, updates/recovery, vulnerability handling and destination duties |
| Robotics/industrial | Robot versus cell/machinery/installation scope, safety functions and performance claims, stopping/restart/maintenance, payload/tools, FAT/SAT and integrator responsibility |
| Medical | Intended medical purpose, class, QMS/design controls, ISO 14971 risk lifecycle, applicable software/usability/electrical/clinical evidence, transfer and destination authorization |
| Automotive | OEM/supplier interface and assumptions, ISO 26262 functional safety, ISO 21448 SOTIF and ISO/SAE 21434 cybersecurity applicability, customer APQP/control plan/PPAP and vehicle integration |

[ISO 10218-1:2025](https://www.iso.org/standard/73933.html) addresses industrial robots;
[Part 2](https://www.iso.org/standard/73934.html) addresses their applications/cells. Do not
extend these scopes automatically to medical or public-access service robots.
[IEC 62443-4-1](https://webstore.iec.ch/en/publication/33615) addresses industrial secure
product lifecycle processes. [ISO 14971](https://www.iso.org/standard/72704.html) and
[IEC 62304](https://webstore.iec.ch/en/publication/6792) cover different medical risk/software
responsibilities. [AIAG](https://go.aiag.org/apqp-cp) provides the automotive core-tool baseline;
UN R155/R156 responsibilities are vehicle/destination dependent, not a PCB certificate.

## Destination checklist

| Destination | Scope and release evidence |
|---|---|
| US | FCC intentional/unintentional radiator route, module/host integration, labels/responsible party; applicable CPSC product rules/certificates/import filings; workplace electrical approval where required; FDA route for medical devices |
| EU | Applicable CE legislation and conformity route, technical documentation/declaration, marking/instructions/operators; radio/EMC/safety, RoHS and REACH, GPSR/WEEE/producer obligations and sector-specific rules; cybersecurity and machinery transitions |
| Great Britain | Product-specific UKCA/recognized CE route and exceptions, declarations/labels/operators, connected-product security, separate medical rules |
| Northern Ireland | Applicable EU product regime and NI-specific operator/marking details; do not apply GB rules indiscriminately |
| Taiwan domestic | Current BSMI commodity scope and scheme/CNS/labels/material information; NCC controlled RF obligations; TFDA product and manufacturer quality-system routes for medical devices |
| Taiwan manufacture/export | Manufacturing-location duties plus each destination's own approvals, importer/operator, regional configuration, labels/languages/customs and shipping evidence |

Use the actual rule/authority as the project source:
[FCC digital devices](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/part-15/subpart-B/section-15.101),
[FCC intentional radiators](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/part-15/subpart-C/section-15.201),
[EU manufacturer obligations](https://single-market-economy.ec.europa.eu/single-market/goods/ce-marking/manufacturers_en),
[UK sector marking guidance](https://www.gov.uk/government/publications/product-regulations-by-sector-and-current-approaches-to-product-marking-ukca-and-ce-regimes/product-regulations-by-sector-and-current-approaches-to-product-marking-ukca-and-ce-regimes),
[BSMI regulated products](https://www.bsmi.gov.tw/wSite/lp?BaseDSD=7&CtUnit=4131&ctNode=9845),
[NCC law](https://ncclaw.ncc.gov.tw/Eng/PrintFLAWDAT0201.aspx?beginpos=18&id=FL091365&keyword=),
and [TFDA licensing](https://www.fda.gov.tw/ENG/lawContent.aspx?cid=5063&id=3354).
An approved radio module does not remove the final host's integration/conformity duties.

## Date-sensitive checks

- EU CRA Article 14 reporting applies from **11 September 2026**; main application is
  **11 December 2027**. Establish scope, support and reporting ownership now; do not treat
  already-applicable reporting as a future launch task. [Commission CRA summary and binding text](https://digital-strategy.ec.europa.eu/en/policies/cra-summary).
- FDA QMSR became effective **2 February 2026**, incorporating ISO 13485:2016 by reference.
  [FDA QMSR](https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr).
  Use the [February 2026 medical cybersecurity guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/cybersecurity-medical-devices-quality-management-system-considerations-and-content-premarket), which supersedes June 2025 guidance.
- EU Machinery Regulation applies from **20 January 2027**; use the correct launch-date
  legislation and transition. [Commission machinery guidance](https://single-market-economy.ec.europa.eu/sectors/mechanical-engineering/machinery_en).
- UK PSTI has applied since **29 April 2024** to in-scope consumer connectable products:
  password, vulnerability-reporting, support-period and statement obligations need evidence.
  [UK enforcement guidance](https://www.gov.uk/guidance/regulations-consumer-connectable-product-security).
- CPSC import eFiling requirements began for most covered imported regulated products on
  **8 July 2026**; determine actual product and importer applicability.
  [CPSC certification guidance](https://www.cpsc.gov/Business--Manufacturing/Testing-Certification/General-Use-Products-Certification-and-Testing).

Medical destinations have distinct approval, registration, representative, labeling and
post-market obligations. See [EU medical economic operators](https://health.ec.europa.eu/medical-devices-topics-interest/economic-operators_en),
[MHRA GB/NI guidance](https://www.gov.uk/guidance/regulating-medical-devices-in-the-uk), and
TFDA domestic QMS versus foreign-manufacturer QSD requirements. Device authorization and
manufacturer quality-system assessment are separate workstreams.

Lithium battery transport has its own classification, UN 38.3 evidence/test-summary,
packaging, carrier and shipment-document requirements. It is separate from product safety or
radio approval. [PHMSA test-summary guidance](https://www.phmsa.dot.gov/training/hazmat/new-un-requirement-test-summaries).

G7 requires actual applicable records and responsible release approvals, not this reference
table. Sustaining retains complaint, vulnerability, supplier-change and field-action processes
with jurisdiction-specific deadlines and accountable owners.
