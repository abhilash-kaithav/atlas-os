# Coding and Charge Capture

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Finance and Revenue Operations`
- Operating systems: `Care Delivery and Reimbursement`
- Industries using this workflow: `Ambulatory health care services`
- Industry count: 1
- Systems-of-record categories: `EHR and Care Management | Revenue Cycle Management | Practice Management`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Turn completed work or contractual obligation into clean bills, timely collections, and accurate receivable records.
- Trigger: A billable event, service completion, or recurring obligation reaches the point of invoicing or follow-up.
- End outcome: The bill is issued, the receivable is updated, and collection or exception status is clear.
- Primary actors: billing specialist; collections or revenue-cycle staff; source operations team; customer or payer
- Major decisions: Is the billable record complete enough to issue or submit?; What denial, dispute, or delinquency path should be pursued next?; When should the item be escalated, adjusted, or written down?
- Major handoffs: source operations -> billing or coding team; billing -> customer, payer, or clearing partner; open item -> collections, finance, or account owner
- Systems of record involved: EHR and Care Management | Revenue Cycle Management | Practice Management

## Current-State Friction

- Where money is lost: Missed charges, denial cycles, underbilling, and slow cash application are the primary leakage points.
- Where time is lost: Teams repeatedly reconcile source evidence, payer rules, and customer-specific exceptions.
- Where human judgment dominates: Operators interpret contract nuance, collection strategy, and what evidence is enough to close the item.
- Where people leave the system of record: Collections context and exception history often live in email, payer portals, and spreadsheets outside the core system.

## Software Landscape

- What software exists today: Typical stacks combine EHR and Care Management, Revenue Cycle Management, Practice Management; representative software in market today includes Epic, Oracle Health EHR, Meditech, PointClickCare, athenahealth RCM, R1 RCM.
- Representative vendors: Epic; Oracle Health EHR; Meditech; PointClickCare; athenahealth RCM; R1 RCM; Optum; eClinicalWorks
- Why this has not been solved cleanly: Automation handles the clean path, but exceptions are driven by messy upstream data and contract interpretation. It typically spans 1 operating-system context and 3 systems-of-record categories.
- Primary reason: `Regulatory`

## Current Vendor Research

- [Epic](https://www.epic.com/)
- [Oracle Health EHR](https://www.oracle.com/health/clinical-suite/electronic-health-record/)
- [athenahealth RCM](https://www.athenahealth.com/solutions/revenue-cycle-management)
- [R1 RCM](https://www.r1rcm.com/enterprise-partnerships)

## Atlas Context

- `Care Delivery and Reimbursement`: Delivers regulated care where access, documentation, staffing, reimbursement, and collections drive economics.
