# Service Scheduling and Parts Management

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Customer and Experience Operations`
- Operating systems: `Retail and Service Commerce`
- Industries using this workflow: `Motor vehicle and parts dealers`
- Industry count: 1
- Systems-of-record categories: `Loan Origination and Servicing | Maintenance Management | Dealership Management System | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Match a customer need to the right appointment, technician, or part-supported service slot.
- Trigger: A customer requests service or a follow-up intervention must be scheduled.
- End outcome: The appointment or work slot is booked with the right resources and dependencies prepared.
- Primary actors: scheduler; customer; field or service team; parts or operations support
- Major decisions: What slot, technician, or resource best fits the request?; Which dependency such as parts or authorization must be secured first?; What issue should be escalated because the standard schedule will fail?
- Major handoffs: customer request -> scheduler; scheduled job -> field or service team; completed service -> billing, support, or account owner
- Systems of record involved: Loan Origination and Servicing | Maintenance Management | Dealership Management System | CRM

## Current-State Friction

- Where money is lost: Leakage appears through low first-time fix, no-shows, deadhead travel, and rescheduling churn.
- Where time is lost: Schedulers spend time on calendar juggling, parts checks, and customer callbacks.
- Where human judgment dominates: Experienced schedulers still know which combinations of customer, asset, and worker will actually succeed.
- Where people leave the system of record: Real-world exceptions are coordinated through calls, texts, and side notes outside the scheduler.

## Software Landscape

- What software exists today: Typical stacks combine Loan Origination and Servicing, Maintenance Management, Dealership Management System, CRM; representative software in market today includes nCino Commercial Lending, nCino, Temenos, Dealertrack, IFS Enterprise Asset Management, Yardi.
- Representative vendors: nCino Commercial Lending; nCino; Temenos; Dealertrack; IFS Enterprise Asset Management; Yardi; ServiceTitan; Oracle Utilities
- Why this has not been solved cleanly: The slotting problem is only half the challenge; the other half is local exception management with incomplete visibility. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Technical`

## Current Vendor Research

- [nCino Commercial Lending](https://www.ncino.com/solutions/commercial-lending?nxtPslug=commercial-loan-origination-system)
- [IFS Enterprise Asset Management](https://www.ifs.com/en/products/alm/eam)
- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Retail and Service Commerce`: Monetizes traffic, assortment, transactions, service execution, labor, and repeat demand across commerce channels.
