# Eligibility and Authorization

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Access, Intake, and Contracting`
- Operating systems: `Care Delivery and Reimbursement`
- Industries using this workflow: `Ambulatory health care services`
- Industry count: 1
- Systems-of-record categories: `EHR and Care Management | Revenue Cycle Management | Practice Management`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Move a person into service with the right eligibility, timing, and required intake information captured up front.
- Trigger: A person requests entry into care, education, or a case-based program.
- End outcome: The person is cleared for service, scheduled or enrolled, and visible to downstream service teams.
- Primary actors: intake coordinator; participant or patient; authorization or eligibility staff; service scheduler
- Major decisions: Is the person eligible and appropriately prioritized?; What slot, program, or service path should they enter?; What information gap blocks progression into service?
- Major handoffs: front-door intake -> authorization or scheduling; eligibility review -> service owner; admitted participant -> ongoing service team
- Systems of record involved: EHR and Care Management | Revenue Cycle Management | Practice Management

## Current-State Friction

- Where money is lost: Leakage starts with avoidable denials, no-shows, unused capacity, and mis-routed participants.
- Where time is lost: Teams repeatedly collect the same history and chase coverage, paperwork, and schedule coordination.
- Where human judgment dominates: Staff balance urgency, fit, and operational constraints under incomplete documentation.
- Where people leave the system of record: Phone calls, scanned documents, and message threads still carry the real intake context.

## Software Landscape

- What software exists today: Typical stacks combine EHR and Care Management, Revenue Cycle Management, Practice Management; representative software in market today includes Epic, Oracle Health EHR, Meditech, PointClickCare, athenahealth RCM, R1 RCM.
- Representative vendors: Epic; Oracle Health EHR; Meditech; PointClickCare; athenahealth RCM; R1 RCM; Optum; eClinicalWorks
- Why this has not been solved cleanly: Eligibility and access rules can be encoded, but edge cases and capacity realities still require manual orchestration. It typically spans 1 operating-system context and 3 systems-of-record categories.
- Primary reason: `Organizational`

## Current Vendor Research

- [Epic](https://www.epic.com/)
- [Oracle Health EHR](https://www.oracle.com/health/clinical-suite/electronic-health-record/)
- [athenahealth RCM](https://www.athenahealth.com/solutions/revenue-cycle-management)
- [R1 RCM](https://www.r1rcm.com/enterprise-partnerships)

## Atlas Context

- `Care Delivery and Reimbursement`: Delivers regulated care where access, documentation, staffing, reimbursement, and collections drive economics.
