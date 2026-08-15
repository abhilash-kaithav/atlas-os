# Housing Workflow Inventory

Last updated: 2026-08-15
Status: Batch 1 inventory complete

## Industry Context

- Industry: `Housing`
- Operating system: `Asset Utilization and Lease Management`
- Lifecycle: marketing -> lead intake -> screening -> lease execution -> move-in onboarding -> occupancy and billing -> maintenance -> delinquency and collections -> turnover and make-ready -> inspections and compliance -> renewal or move-out closeout

## Workflow Inventory

| Lifecycle stage | Workflow | Description | Primary roles | External parties |
| --- | --- | --- | --- | --- |
| Commercial | Unit marketing and lead management | Generate demand, manage tours, and keep unit availability current. | leasing agent; community manager | prospects; listing channels |
| Commercial | Applicant screening and lease execution | Qualify residents, process applications, and execute leases or denials. | leasing agent; assistant manager | screening vendors; prospects |
| Commercial / Onboarding | Move-in onboarding and account setup | Create resident records, utility or portal setup, keys, inspections, and initial communications. | leasing admin; property manager | residents; utility providers |
| Financial | Rent billing and cash application | Post rent, concessions, fees, and receipts into the PMS and general ledger. | property accountant; manager | residents; payment processors |
| Financial / Recovery | Delinquency, collections, and move-out notices | Track overdue balances, payment plans, notices, and escalations before vacancy or write-off. | property manager; collections specialist | residents; legal counsel |
| Operational | Maintenance intake and triage | Receive service requests, assess urgency, and determine internal versus vendor dispatch. | maintenance coordinator; resident services | residents; call centers |
| Supplier / Partner | Vendor onboarding and compliance | Set up vendors, COIs, scopes, pricing, and local compliance records. | maintenance coordinator; AP admin | contractors; insurers |
| Operational | Repair dispatch and work order execution | Schedule technicians or vendors, track progress, and confirm completion. | maintenance supervisor; vendor coordinator | technicians; vendors; residents |
| Recovery | Turnover and make-ready recovery | Diagnose why a unit will miss ready date, coordinate blockers, and recover the plan before lost rent grows. | turns coordinator; community manager | vendors; inspectors; owners |
| Customer / Retention | Resident communication, renewal, and retention | Coordinate status updates, renewal offers, inspections, and move-out planning. | leasing manager; community manager | residents |
| Governance / Risk | Inspections, owner reporting, and compliance | Produce maintenance, Fair Housing, safety, capex, and owner or lender reporting. | regional manager; property accountant | owners; lenders; local regulators |

## Completeness Test

| Domain | Coverage result | Notes |
| --- | --- | --- |
| Commercial | Pass | Demand, pricing, contracting, onboarding, renewal, and retention are covered. |
| Operational | Pass | Planning, scheduling, execution, monitoring, maintenance, and recovery are covered. |
| Financial | Pass | Billing, payment, collections, reconciliation, and close are covered. |
| Workforce | Pass | Staffing, assignment, time capture, training, and performance are embedded in maintenance and property operations. |
| Supplier / Partner | Pass | Sourcing, onboarding, compliance, delivery, and dispute handling are covered. |
| Customer / Participant | Pass | Intake, service, communication, complaints, escalation, and move-out handling are covered. Returns are `N/A`. |
| Regulatory / Risk | Pass | Approvals, controls, evidence, reporting, audits, and remediation are covered. |
| Exception / Recovery | Pass | Rejections, correction work, schedule deviation, failed inspections, and recovery loops are covered. |

## Batch 1 Interpretation

The complete inventory shows that make-ready recovery is not an isolated maintenance annoyance. It is the workflow where leasing, maintenance, vendors, approvals, and revenue timing collide.
