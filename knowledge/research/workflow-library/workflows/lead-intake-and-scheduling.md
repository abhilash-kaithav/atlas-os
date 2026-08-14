# Lead Intake and Scheduling

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Access, Intake, and Contracting`
- Operating systems: `Workforce Coordination and Service Operations`
- Industries using this workflow: `Other services, except government`
- Industry count: 1
- Systems-of-record categories: `POS and Payments | CRM | HCM / Workforce Management | Service Management`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Move a person into service with the right eligibility, timing, and required intake information captured up front.
- Trigger: A person requests entry into care, education, or a case-based program.
- End outcome: The person is cleared for service, scheduled or enrolled, and visible to downstream service teams.
- Primary actors: intake coordinator; participant or patient; authorization or eligibility staff; service scheduler
- Major decisions: Is the person eligible and appropriately prioritized?; What slot, program, or service path should they enter?; What information gap blocks progression into service?
- Major handoffs: front-door intake -> authorization or scheduling; eligibility review -> service owner; admitted participant -> ongoing service team
- Systems of record involved: POS and Payments | CRM | HCM / Workforce Management | Service Management

## Current-State Friction

- Where money is lost: Leakage starts with avoidable denials, no-shows, unused capacity, and mis-routed participants.
- Where time is lost: Teams repeatedly collect the same history and chase coverage, paperwork, and schedule coordination.
- Where human judgment dominates: Staff balance urgency, fit, and operational constraints under incomplete documentation.
- Where people leave the system of record: Phone calls, scanned documents, and message threads still carry the real intake context.

## Software Landscape

- What software exists today: Typical stacks combine POS and Payments, CRM, HCM / Workforce Management, Service Management; representative software in market today includes Toast POS, Square, Oracle MICROS, NCR Voyix, Salesforce CRM, Microsoft Dynamics 365 Sales.
- Representative vendors: Toast POS; Square; Oracle MICROS; NCR Voyix; Salesforce CRM; Microsoft Dynamics 365 Sales; HubSpot CRM; VTS
- Why this has not been solved cleanly: Eligibility and access rules can be encoded, but edge cases and capacity realities still require manual orchestration. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Organizational`

## Current Vendor Research

- [Toast POS](https://pos.toasttab.com/products/point-of-sale)
- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)
- [Workday Workforce Management](https://forms.workday.com/en-us/quick-demos/managing-your-workforce-with-workday-demo/form.html?step=step1_default)
- [Deputy](https://www.deputy.com/)
- [Legion](https://legion.co/en-gb/products/)

## Atlas Context

- `Workforce Coordination and Service Operations`: Matches labor to demand, schedules execution, monitors service levels, and converts work into payroll and billing.
