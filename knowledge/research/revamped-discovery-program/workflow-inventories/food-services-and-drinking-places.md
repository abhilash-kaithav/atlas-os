# Food Services and Drinking Places Workflow Inventory

Last updated: 2026-08-15
Status: Batch 1 inventory complete

## Industry Context

- Industry: `Food services and drinking places`
- Operating system: `Retail and Service Commerce`
- Lifecycle: menu and promotion planning -> labor planning -> procurement and receiving -> prep -> order capture -> kitchen and service execution -> payment and close -> inventory and margin review -> complaint or refund recovery -> compliance and reporting

## Workflow Inventory

| Lifecycle stage | Workflow | Description | Primary roles | External parties |
| --- | --- | --- | --- | --- |
| Commercial | Menu, pricing, and promotion planning | Set menus, prices, channels, promos, and expected margin guardrails. | owner; GM; finance lead | distributors; marketing tools |
| Workforce | Labor scheduling and time capture | Build staffing plans, approve time, and reconcile labor to demand. | GM; shift manager | employees; workforce software |
| Supplier / Partner | Procurement, receiving, and inventory setup | Order products, receive deliveries, and maintain vendor and SKU records. | kitchen manager; purchasing lead | suppliers; distributors |
| Operational | Prep and production planning | Translate forecasted demand into prep, station setup, and par levels. | chef; kitchen manager | internal teams |
| Customer / Commercial | POS, delivery-channel, and order capture | Accept dine-in, takeout, web, and marketplace orders with correct pricing and tax treatment. | cashier; manager | guests; marketplaces; POS vendor |
| Operational | Kitchen and service fulfillment | Produce and hand off orders while managing substitutions, holds, and service speed. | line cooks; expeditor; FOH manager | guests; drivers |
| Financial | Daily sales summary and cash close | Review sales, deposits, labor, payment types, and close package before posting. | GM; bookkeeper; accountant | payment processors; POS |
| Financial / Recovery | Inventory, waste, and recipe variance reconciliation | Compare expected to actual inventory and diagnose spoilage, comps, theft, or process drift. | kitchen manager; finance analyst | suppliers |
| Recovery | Complaint, refund, chargeback, and third-party dispute recovery | Investigate failed orders, refund requests, payout issues, and partner disputes. | GM; bookkeeper; owner | guests; DoorDash; Uber Eats; Grubhub |
| Governance / Risk | Health, safety, labor, tax, and compliance reporting | Produce labor, food safety, tax, and audit evidence across locations or shifts. | GM; accountant; HR admin | health inspectors; tax authorities |

## Completeness Test

| Domain | Coverage result | Notes |
| --- | --- | --- |
| Commercial | Pass | Demand, pricing, onboarding, repeat demand, and retention are covered. Formal contracting is limited and mostly `N/A` outside supplier or delivery relationships. |
| Operational | Pass | Planning, scheduling, execution, monitoring, quality, and recovery are covered. Maintenance is operationally present but subordinate to facility management rather than the core commerce loop. |
| Financial | Pass | Billing, payment, settlement, reconciliation, and close are covered. Collections are limited and mostly `N/A` at store level. |
| Workforce | Pass | Scheduling, time capture, payroll inputs, training, and performance are covered. Recruiting is usually local and repetitive but not the deepest pain surface in this batch. |
| Supplier / Partner | Pass | Sourcing, onboarding, compliance, delivery, and dispute handling are covered. |
| Customer / Participant | Pass | Intake, service, communication, complaints, returns, and escalation are covered. |
| Regulatory / Risk | Pass | Approvals, evidence, reporting, audit, and remediation are covered. |
| Exception / Recovery | Pass | Failed orders, payment issues, refunds, disputes, and data corrections are covered. |

## Batch 1 Interpretation

The complete inventory makes the industry clearer, but it still does not produce a strong preserved wedge. The deepest recurring recovery work remains real, yet too occupied and too incremental relative to current platform boundaries.
