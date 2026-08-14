# Inventory Sourcing and Aging Management

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Planning and Allocation`
- Operating systems: `Retail and Service Commerce`
- Industries using this workflow: `Motor vehicle and parts dealers`
- Industry count: 1
- Systems-of-record categories: `Loan Origination and Servicing | Maintenance Management | Dealership Management System | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Place inventory and assortment into the right location, age bucket, or channel before demand crystallizes.
- Trigger: Inventory, assortment, or aging conditions require an allocation or reallocation decision.
- End outcome: Inventory is assigned to the right destination with downstream replenishment and commercial actions aligned.
- Primary actors: inventory planner; merchant or commercial lead; warehouse or store operations; finance partner
- Major decisions: Where should inventory sit given expected demand and margin?; What stock should be accelerated, protected, or marked down?; When is reallocation worth the operational disruption?
- Major handoffs: demand and stock signals -> inventory planning; allocation decision -> store, warehouse, or channel team; execution outcome -> pricing and finance review
- Systems of record involved: Loan Origination and Servicing | Maintenance Management | Dealership Management System | CRM

## Current-State Friction

- Where money is lost: Misallocation drives stockouts, markdowns, carrying cost, and lost working capital productivity.
- Where time is lost: Teams spend time reconciling stock truth and coordinating transfers or aged inventory action.
- Where human judgment dominates: Operators still judge local demand and whether aged stock can truly move through the planned channel.
- Where people leave the system of record: Inventory decisions are often managed in spreadsheets and store communications outside the planning system.

## Software Landscape

- What software exists today: Typical stacks combine Loan Origination and Servicing, Maintenance Management, Dealership Management System, CRM; representative software in market today includes nCino Commercial Lending, nCino, Temenos, Dealertrack, IFS Enterprise Asset Management, Yardi.
- Representative vendors: nCino Commercial Lending; nCino; Temenos; Dealertrack; IFS Enterprise Asset Management; Yardi; ServiceTitan; Oracle Utilities
- Why this has not been solved cleanly: System optimization struggles when demand is local, seasonal, and only partly observable in real time. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Technical`

## Current Vendor Research

- [nCino Commercial Lending](https://www.ncino.com/solutions/commercial-lending?nxtPslug=commercial-loan-origination-system)
- [IFS Enterprise Asset Management](https://www.ifs.com/en/products/alm/eam)
- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Retail and Service Commerce`: Monetizes traffic, assortment, transactions, service execution, labor, and repeat demand across commerce channels.
