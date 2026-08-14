# Intake and Eligibility Determination

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Access, Intake, and Contracting`
- Operating systems: `Case Management and Program Administration`
- Industries using this workflow: `Social assistance`
- Industry count: 1
- Systems-of-record categories: `Case Management System | Grant and Program Reporting | Referral Management | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Move a person into service with the right eligibility, timing, and required intake information captured up front.
- Trigger: A person requests entry into care, education, or a case-based program.
- End outcome: The person is cleared for service, scheduled or enrolled, and visible to downstream service teams.
- Primary actors: intake coordinator; participant or patient; authorization or eligibility staff; service scheduler
- Major decisions: Is the person eligible and appropriately prioritized?; What slot, program, or service path should they enter?; What information gap blocks progression into service?
- Major handoffs: front-door intake -> authorization or scheduling; eligibility review -> service owner; admitted participant -> ongoing service team
- Systems of record involved: Case Management System | Grant and Program Reporting | Referral Management | CRM

## Current-State Friction

- Where money is lost: Leakage starts with avoidable denials, no-shows, unused capacity, and mis-routed participants.
- Where time is lost: Teams repeatedly collect the same history and chase coverage, paperwork, and schedule coordination.
- Where human judgment dominates: Staff balance urgency, fit, and operational constraints under incomplete documentation.
- Where people leave the system of record: Phone calls, scanned documents, and message threads still carry the real intake context.

## Software Landscape

- What software exists today: Typical stacks combine Case Management System, Grant and Program Reporting, Referral Management, CRM; representative software in market today includes Netsmart, WellSky, Eccovia, Apricot, Salesforce, Microsoft Dynamics 365 Sales.
- Representative vendors: Netsmart; WellSky; Eccovia; Apricot; Salesforce; Microsoft Dynamics 365 Sales; HubSpot CRM; VTS
- Why this has not been solved cleanly: Eligibility and access rules can be encoded, but edge cases and capacity realities still require manual orchestration. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Organizational`

## Current Vendor Research

- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Case Management and Program Administration`: Coordinates intake, service plans, documentation, referrals, and funding reporting across case-based programs.
