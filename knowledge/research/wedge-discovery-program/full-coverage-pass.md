# Full Coverage Pass

Last updated: 2026-08-15
Status: Top-50 coverage complete under Atlas Research Program v1.0

## Scope

This file records the post-Batch-1 full pass across the remaining industries after Atlas adopted the frozen v1.0 operating specification.

All industries were evaluated using:

- `industry-workflow-maps.md` for Phase 0 and Phase 0B
- the existing normalized census, workflow library, and structural-failure atlas for Pain Surface Scan and Candidate Workflow Selection
- current product and practitioner evidence for any workflow that appeared strong enough to advance

## Outcome Summary

- Preserved new wedges: `W-004`, `W-005`
- New merges: `M-001`, `M-002`, `M-003`
- Most industries were killed before a canonical candidate was formed because they failed Gate 1, Gate 3, or both

## Batch 002 — Commerce and CPG

| Industry | Workflow taken deepest | Outcome | Why |
| --- | --- | --- | --- |
| Wholesale trade | Billing and collections | KILL | Recurring order, rebate, and deduction pain exists, but distributor-side evidence for a distinct underserved exception desk was too thin relative to existing ERP and AR tooling. |
| Other retail | Fulfillment and returns management | KILL | Returns and omnichannel friction are real, but the boundary is crowded and the remaining pain looked process-specific rather than wedge-specific. |
| Food and beverage and tobacco products | Distribution and trade promotion | KILL | Deduction-management software now clearly validates the market; remaining dissatisfaction looked feature- and services-oriented rather than an open first wedge. |
| Food and beverage stores | Margin and shrink management | KILL | Pain was visible but not narrow enough to produce a buyer-recognized atomic recovery job. |
| General merchandise stores | Returns and markdown management | KILL | Existing OMS, WMS, and retail platforms already own too much of the boundary for a clean startup entry. |

## Batch 003 — Capital, Banking, and Insurance

| Industry | Workflow taken deepest | Outcome | Why |
| --- | --- | --- | --- |
| Insurance carriers and related activities | Claims administration | KILL | Strong pain, but the workflow remains deeply occupied by policy and claims leaders plus AI-enabled incumbents. |
| Federal Reserve banks, credit intermediation, and related activities | Account and loan onboarding; collections | KILL | Exception volume is real, but core-banking, fraud, and compliance incumbents already sit too close to the workflow. |
| Securities, commodity contracts, and investments | Trade execution, settlement, and books-and-records exceptions | MERGE -> `W-004` | The surviving job is materially the same pre-reporting reconciliation and break-triage loop preserved in fund operations. |
| Funds, trusts, and other financial vehicles | Valuation, NAV, and reconciliation | YELLOW -> `W-004` | Buyer, recurrence, and economics are strong, but the practitioner-evidence base remains weaker than the best current GREEN wedges. |
| Management of companies and enterprises | Shared-service operations | KILL | Pain existed only as a broad shared-services thesis, not as a clear atomic monopoly wedge. |

## Batch 004 — Transportation

| Industry | Workflow taken deepest | Outcome | Why |
| --- | --- | --- | --- |
| Truck transportation | Freight audit and billing | YELLOW -> `W-005` | Repeated manual proof, rate, and accessorial resolution work remains visible and budgeted, but startup defensibility versus TMS vendors still needs more proof. |
| Other transportation and support activities | Freight audit and settlement | MERGE -> `W-005` | The surviving brokerage-side job was functionally the same document-and-rate exception loop as truck billing recovery. |
| Air transportation | Operational recovery and disruption management | KILL | Pain is intense, but incumbent depth, integration burden, and control-center economics make startup entry unattractive. |

## Batch 005 — Real Estate, Hospitality, and Venue Operations

| Industry | Workflow taken deepest | Outcome | Why |
| --- | --- | --- | --- |
| Other real estate | Billing and reconciliation | KILL | CAM and tenant true-up pain is real, but the strongest available evidence remained too vendor-shaped and too annual to preserve. |
| Rental and leasing services and lessors of intangible assets | Asset maintenance and turnover | KILL | Turn and recovery work exists, but no sharper buyer-validated job emerged beyond broad asset-turnover operations. |
| Accommodation | Front desk, housekeeping, and maintenance recovery | MERGE -> `W-002` | The job reduced to turn-blocker diagnosis and readiness orchestration for a revenue-generating unit, which is fundamentally the same atomic job preserved in housing. |
| Performing arts, spectator sports, museums, and related activities | Event settlement and reporting | KILL | Operations are fragmented, but no recurring, buyer-specific workflow survived the stress test. |
| Amusements, gambling, and recreation industries | Loyalty and settlement management | KILL | The candidate remained too broad and too incumbent-bound to preserve. |

## Batch 006 — Healthcare and Social Services

| Industry | Workflow taken deepest | Outcome | Why |
| --- | --- | --- | --- |
| Ambulatory health care services | Billing, claims, and collections | KILL | Reconfirmed prior Atlas learning: denial and reimbursement pain is real but already occupied by scaled RCM and EHR ecosystems. |
| Hospitals | Billing, claims, and collections | KILL | Throughput and reimbursement pain did not produce a startup-credible atomic wedge separate from giant incumbent control points. |
| Nursing and residential care facilities | Billing, claims, and collections | KILL | The strongest candidates collapsed back into occupied reimbursement and compliance surfaces. |
| Social assistance | Billing, grant reporting, and reimbursement | KILL | Administrative pain exists, but budget ownership and software economics looked too weak for a venture wedge. |

## Batch 007 — Professional and Workforce Services

| Industry | Workflow taken deepest | Outcome | Why |
| --- | --- | --- | --- |
| Miscellaneous professional, scientific, and technical services | Time and expense capture to billing | KILL | Manual time-to-bill leakage persists, but PSA, ERP, and services-heavy workflows already own too much of the boundary. |
| Computer systems design and related services | Time, billing, and renewal handoffs | KILL | Similar pain to broader professional services, but not enough distinct customer evidence to preserve separately. |
| Legal services | Time and expense capture | KILL | Pain is real, but the strongest surfaces are already deeply served by legal practice-management incumbents. |
| Educational services | Billing, aid, and regulatory reporting | KILL | Compliance and reimbursement work remained too institution-specific and politically constrained. |
| Other services, except government | Billing and payment processing | KILL | Recurring service-ops friction exists, but no clear atomic wedge was stronger than the staffing pay/bill correction candidate. |

## Batch 008 — Digital, Media, and Network

| Industry | Workflow taken deepest | Outcome | Why |
| --- | --- | --- | --- |
| Data processing, internet publishing, and other information services | Usage billing and monetization | KILL | Reconfirmed prior Atlas learning that SaaS and usage-billing exception management is already too occupied. |
| Publishing industries, except internet (includes software) | Billing and renewals | KILL | Renewal and rights friction did not survive the stress test as a startup entry point. |
| Motion picture and sound recording industries | Royalty and participation accounting | KILL | Manual royalty work is visible, but customer-evidence depth and buyer concentration were too weak to preserve. |
| Broadcasting and telecommunications | Outage and regulatory management | KILL | High pain but deeply embedded incumbent boundary and heavy integration burden. |
| Utilities | Meter-to-cash | KILL | The candidate collapsed back into incumbent CIS, outage, and regulatory systems with slow adoption cycles. |

## Batch 009 — Discrete Manufacturing

| Industry | Workflow taken deepest | Outcome | Why |
| --- | --- | --- | --- |
| Motor vehicles, bodies and trailers, and parts | Shop floor execution and quality management | KILL | Quality and supplier pain is clear, but startup entry looked unattractive against OEM and plant-system constraints. |
| Fabricated metal products | Shipping and invoice reconciliation | KILL | Billing friction exists, but not enough independent evidence supported a preserved wedge. |
| Machinery | Aftermarket service and field support | KILL | Attractive in theory, but field-service and aftermarket categories already sit too close to the pain. |
| Other transportation equipment | Delivery and contract milestone management | KILL | Episodic program economics and incumbent control points dominated the candidate. |
| Computer and electronic products | Engineering change management | KILL | Rework and traceability matter, but no specific buyer/job/outcome triad cleared the gates. |
| Plastics and rubber products | Quality and compliance management | KILL | The workflow pain remained plant-specific rather than wedge-specific. |
| Electrical equipment, appliances, and components | Compliance and certification management | KILL | Certification burden was real but too occupied and too services-dependent to preserve. |

## Batch 010 — Process Manufacturing and Field Industries

| Industry | Workflow taken deepest | Outcome | Why |
| --- | --- | --- | --- |
| Chemical products | Contract and margin management | KILL | Margin and compliance pain exists, but no atomic workflow proved meaningfully underserved. |
| Petroleum and coal products | Maintenance and turnaround management | KILL | Strong pain but poor startup entry due incumbent depth and plant-specific services economics. |
| Primary metals | Quality inspection and certification | KILL | Certification and paperwork pain did not produce a better wedge than broader manufacturing incumbents already target. |
| Paper products | Quality and converting management | KILL | Workflow remained too plant-specific and evidence too thin. |
| Farms | Harvest and logistics management | KILL | Seasonal variability and fragmented economics weakened startup entry. |
| Oil and gas extraction | Revenue and regulatory reporting | KILL | High-value workflow, but heavily occupied by specialist systems and service firms. |
| Motor vehicle and parts dealers | Financing and underwriting; service scheduling | KILL | Buyer pain exists, but dealer-management incumbents own too much of the operating boundary. |

## Program-Level Interpretation

- Mandatory workflow mapping did not create more surviving wedges; it mostly improved kill confidence.
- The most promising preserved jobs still lived in recovery, reconciliation, and correction loops rather than in primary systems of record.
- `YELLOW` was necessary to avoid overstating conviction where recurrence and economics were visible but customer evidence or incumbent-boundary proof remained incomplete.
