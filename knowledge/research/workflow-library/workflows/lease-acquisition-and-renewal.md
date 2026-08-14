# Lease Acquisition and Renewal

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Access, Intake, and Contracting`
- Operating systems: `Asset Utilization and Lease Management`
- Industries using this workflow: `Housing`
- Industry count: 1
- Systems-of-record categories: `Maintenance Management | Property Management System | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Keep monetizable capacity occupied by winning the right tenants or reservations and preserving renewal continuity.
- Trigger: A unit, asset, or capacity block must be leased, renewed, or moved through the reservation pipeline.
- End outcome: Capacity is committed on acceptable terms and downstream readiness or billing actions are triggered.
- Primary actors: leasing or reservations staff; prospect or tenant; property or asset manager; operations support
- Major decisions: What terms, concessions, or pricing are acceptable for this capacity?; Should the existing relationship be renewed, repriced, or replaced?; What readiness or turnover work must occur before commitment?
- Major handoffs: prospect management -> approval or contracting; signed commitment -> property or operations team; live lease or reservation -> billing and service teams
- Systems of record involved: Maintenance Management | Property Management System | CRM

## Current-State Friction

- Where money is lost: Vacancy, poor renewal timing, weak concessions discipline, and slow readiness cycles directly reduce yield.
- Where time is lost: Leasing teams spend time coordinating tours, approvals, readiness updates, and status checks across systems.
- Where human judgment dominates: Staff balance occupancy goals, asset condition, pricing power, and relationship context when deciding terms.
- Where people leave the system of record: Negotiation details, readiness notes, and exceptions live in email, call logs, and side trackers.

## Software Landscape

- What software exists today: Typical stacks combine Maintenance Management, Property Management System, CRM; representative software in market today includes IFS Enterprise Asset Management, Yardi, ServiceTitan, Oracle Utilities, IFS, RealPage.
- Representative vendors: IFS Enterprise Asset Management; Yardi; ServiceTitan; Oracle Utilities; IFS; RealPage; AppFolio; Entrata
- Why this has not been solved cleanly: The workflow spans commercial negotiation, physical readiness, and revenue optimization rather than a single clean transaction. It typically spans 1 operating-system context and 3 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [IFS Enterprise Asset Management](https://www.ifs.com/en/products/alm/eam)
- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Asset Utilization and Lease Management`: Monetizes owned or controlled assets through occupancy or utilization, contract terms, maintenance, turnover, and billing discipline.
