# Terminal and Yard Operations

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Network and Transportation Operations`
- Operating systems: `Transportation Network Operations`
- Industries using this workflow: `Other transportation and support activities`
- Industry count: 1
- Systems-of-record categories: `Transportation Management System | Fleet Telematics and Visibility | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Assign the right asset, route, crew, or carrier to the job while balancing service, utilization, and cost.
- Trigger: Demand is ready to be moved or serviced across a network and requires a dispatch decision.
- End outcome: The movement or service plan is issued with owners, route, and timing visible to the network.
- Primary actors: dispatcher or planner; carrier, crew, or field operator; operations control; customer or receiving party
- Major decisions: Which asset, route, or partner should carry the work?; What tradeoff between service, cost, and utilization is acceptable?; What exception requires re-plan or escalation now?
- Major handoffs: demand intake -> dispatch control; dispatch plan -> driver, crew, or carrier; movement status -> customer service, billing, or recovery desk
- Systems of record involved: Transportation Management System | Fleet Telematics and Visibility | ERP

## Current-State Friction

- Where money is lost: The biggest leaks are empty capacity, bad routing, detention, and poor network utilization.
- Where time is lost: Dispatchers lose time chasing status, making call-based updates, and rerouting around late disruptions.
- Where human judgment dominates: Controllers interpret service priorities and real-world constraints faster than static optimization models.
- Where people leave the system of record: Carrier calls, texts, and manual route notes remain central to live execution.

## Software Landscape

- What software exists today: Typical stacks combine Transportation Management System, Fleet Telematics and Visibility, ERP; representative software in market today includes project44, McLeod, Oracle Transportation Management, Descartes, CargoWise, Samsara.
- Representative vendors: project44; McLeod; Oracle Transportation Management; Descartes; CargoWise; Samsara; Trimble Transportation; SAP Cloud ERP
- Why this has not been solved cleanly: Network state changes in real time and often depends on partner data that is late, partial, or nonstandard. It typically spans 1 operating-system context and 3 systems-of-record categories.
- Primary reason: `Technical`

## Current Vendor Research

- [project44](https://www.project44.com/platform/tms/)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Transportation Network Operations`: Plans capacity, routes assets, manages exceptions, and settles transport across operating networks.
