# Workforce Scheduling and Dispatch

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Workforce and Labor Operations`
- Operating systems: `Workforce Coordination and Service Operations`
- Industries using this workflow: `Other services, except government`
- Industry count: 1
- Systems-of-record categories: `POS and Payments | CRM | HCM / Workforce Management | Service Management`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Publish and maintain a near-term labor schedule that covers demand, skills, and compliance constraints.
- Trigger: A shift pattern, service forecast, or operational change requires schedule creation or adjustment.
- End outcome: Workers know where to be, managers know coverage, and actual changes can flow into payroll and performance systems.
- Primary actors: scheduler; frontline manager; worker; HR or payroll partner
- Major decisions: Who should work which shift or route?; How should shortages, absences, or overtime risk be handled?; When is a local override justified despite the planning rule?
- Major handoffs: forecast -> scheduler; published schedule -> workers and managers; actual changes -> payroll, billing, or service review
- Systems of record involved: POS and Payments | CRM | HCM / Workforce Management | Service Management

## Current-State Friction

- Where money is lost: Overtime, uncovered demand, idle time, and payroll corrections are the core leaks.
- Where time is lost: Schedulers constantly rework the plan around callouts, fairness concerns, and compliance rules.
- Where human judgment dominates: Managers know who can actually handle the work and what informal tradeoffs will hold the operation together.
- Where people leave the system of record: The live schedule lives in texts, calls, and local shift notes once the day starts moving.

## Software Landscape

- What software exists today: Typical stacks combine POS and Payments, CRM, HCM / Workforce Management, Service Management; representative software in market today includes Toast POS, Square, Oracle MICROS, NCR Voyix, Salesforce CRM, Microsoft Dynamics 365 Sales.
- Representative vendors: Toast POS; Square; Oracle MICROS; NCR Voyix; Salesforce CRM; Microsoft Dynamics 365 Sales; HubSpot CRM; VTS
- Why this has not been solved cleanly: Workforce systems solve the baseline but not the velocity of same-day human exceptions. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Behavioral`

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
