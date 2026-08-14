# Field Service Execution

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Delivery and Service Execution`
- Operating systems: `Workforce Coordination and Service Operations`
- Industries using this workflow: `Other services, except government`
- Industry count: 1
- Systems-of-record categories: `POS and Payments | CRM | HCM / Workforce Management | Service Management`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Execute work in the field while adapting safely to site conditions, change requests, and incomplete information.
- Trigger: A field team is dispatched or mobilized to perform work at a site, customer, or operating location.
- End outcome: The field task is completed, deferred, or escalated with actual conditions captured for downstream use.
- Primary actors: field supervisor; technician or crew; customer or site contact; back-office coordinator
- Major decisions: What can actually be completed given current site conditions?; What change requires new approval, scope, or documentation?; What issue should be solved locally versus escalated?
- Major handoffs: dispatch or planning -> field crew; field crew -> back office, customer, or inspector; completed work -> billing, maintenance history, or reporting
- Systems of record involved: POS and Payments | CRM | HCM / Workforce Management | Service Management

## Current-State Friction

- Where money is lost: Travel waste, revisit rates, change-order misses, and field rework are the main economic leaks.
- Where time is lost: Crews lose time to waiting, missing parts, unclear scope, and back-and-forth approvals.
- Where human judgment dominates: Field leads interpret site reality, safety, and customer context in ways that no template fully captures.
- Where people leave the system of record: Actual field decisions are coordinated over calls, text, and paper notes before systems are updated later.

## Software Landscape

- What software exists today: Typical stacks combine POS and Payments, CRM, HCM / Workforce Management, Service Management; representative software in market today includes Toast POS, Square, Oracle MICROS, NCR Voyix, Salesforce CRM, Microsoft Dynamics 365 Sales.
- Representative vendors: Toast POS; Square; Oracle MICROS; NCR Voyix; Salesforce CRM; Microsoft Dynamics 365 Sales; HubSpot CRM; VTS
- Why this has not been solved cleanly: Field conditions mutate faster than central systems, making local judgment indispensable. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Legacy Architecture`

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
