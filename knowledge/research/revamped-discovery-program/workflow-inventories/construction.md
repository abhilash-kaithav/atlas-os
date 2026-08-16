# Construction Workflow Inventory

Last updated: 2026-08-16
Status: Batch 1 inventory complete

## Industry Context

- Industry: `Construction`
- Operating system: `Project Delivery and Contracting`
- Lifecycle: market development -> bid intake -> estimating -> contracting -> project setup -> planning -> sourcing and subcontractor onboarding -> field execution -> quality and safety control -> change management -> billing and cash collection -> closeout -> warranty or retainage recovery

## Workflow Inventory

| Lifecycle stage | Workflow | Description | Primary roles | External parties |
| --- | --- | --- | --- | --- |
| Commercial | Market development and bid intake | Track opportunities, invitations to bid, prequalification, and go/no-go decisions. | business development lead; estimating lead | owner; GC; architect |
| Commercial | Estimating and proposal management | Price scope, assemble proposal, and align inclusions, exclusions, and assumptions. | estimator; preconstruction lead | GC; suppliers; subcontractors |
| Commercial | Contract review and project setup | Translate award terms into billing rules, schedules of values, compliance requirements, and internal controls. | project accountant; PM; controller | owner; GC; legal; surety |
| Planning | Project scheduling and resource planning | Build the execution plan, crew sequencing, production targets, and billing-calendar dependencies. | PM; superintendent; scheduler | GC; vendors; subcontractors |
| Supplier / Partner | Subcontractor and vendor onboarding and compliance | Set up counterparties, collect insurance and compliance items, and align contract terms. | project engineer; AP/AR admin; PM | subcontractors; suppliers; insurers |
| Workforce | Labor time capture and cost coding | Record labor, equipment, and cost-code detail needed for WIP, billing support, and claims. | foreman; superintendent; payroll admin | labor brokers; field crews |
| Operational | Field execution and daily production | Perform scoped work, record progress, and coordinate daily site constraints. | superintendent; foreman; field engineer | GC; inspectors; trades |
| Operational | Safety, quality, and inspection management | Manage inspections, deficiency lists, compliance evidence, and quality signoff. | safety manager; QA lead; superintendent | inspectors; owner rep; AHJ |
| Recovery | Change-order and cost-to-complete reconciliation | Diagnose scope drift, align field change evidence to cost exposure, and correct financial expectations. | PM; project accountant; estimator | GC; owner; architect |
| Financial | Progress billing, SOV, and pay application preparation | Build and submit AIA or portal billing packages with SOV alignment, waivers, and backup. | project accountant; billing specialist | GC AP; owner; lender |
| Financial / Recovery | Collections, waiver, and payment dispute recovery | Chase statuses, correct rejected pay apps, resolve waiver or compliance blockers, and protect cash timing. | AR specialist; controller; project accountant | GC AP; owner; lender; surety |
| Closeout | Punchlist, closeout, and retainage release | Assemble final documents, complete punch items, and release retainage or final billings. | project engineer; PM; project accountant | owner; GC; inspectors |

## Completeness Test

| Domain | Coverage result | Notes |
| --- | --- | --- |
| Commercial | Pass | Demand, pricing, contracting, and onboarding are covered. Renewal and retention are `N/A` for project-based work. |
| Operational | Pass | Planning, scheduling, execution, monitoring, quality, and recovery are covered. Maintenance is `N/A` at the contractor workflow level. |
| Financial | Pass | Billing, payment, collections, reconciliation, and closeout are covered. |
| Workforce | Pass | Staffing and assignment are embedded in planning; time capture is explicit; training and performance live inside field supervision and safety management. |
| Supplier / Partner | Pass | Sourcing, onboarding, compliance, delivery, and dispute handling are covered. |
| Customer / Participant | Pass | Intake, communication, escalation, and dispute handling occur through bid intake, field coordination, billing, and closeout. Returns are `N/A`. |
| Regulatory / Risk | Pass | Approvals, controls, evidence, inspections, reporting, audit support, and remediation are covered. |
| Exception / Recovery | Pass | Rejections, corrections, disputes, failed approvals, resubmissions, and retainage recovery are covered. |

## Batch 1 Interpretation

The complete inventory reinforces that the surviving pain does not sit in generic construction billing automation. It sits in the correction loop after a pay application, waiver package, or compliance-backed billing record fails to move forward.
