# Load Forecasting and Dispatch

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Network and Transportation Operations`
- Operating systems: `Network Infrastructure Operations`
- Industries using this workflow: `Utilities`
- Industry count: 1
- Systems-of-record categories: `Maintenance Management | Utility Operations and Billing | Industrial Automation and SCADA | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Assign the right asset, route, crew, or carrier to the job while balancing service, utilization, and cost.
- Trigger: Demand is ready to be moved or serviced across a network and requires a dispatch decision.
- End outcome: The movement or service plan is issued with owners, route, and timing visible to the network.
- Primary actors: dispatcher or planner; carrier, crew, or field operator; operations control; customer or receiving party
- Major decisions: Which asset, route, or partner should carry the work?; What tradeoff between service, cost, and utilization is acceptable?; What exception requires re-plan or escalation now?
- Major handoffs: demand intake -> dispatch control; dispatch plan -> driver, crew, or carrier; movement status -> customer service, billing, or recovery desk
- Systems of record involved: Maintenance Management | Utility Operations and Billing | Industrial Automation and SCADA | ERP

## Current-State Friction

- Where money is lost: The biggest leaks are empty capacity, bad routing, detention, and poor network utilization.
- Where time is lost: Dispatchers lose time chasing status, making call-based updates, and rerouting around late disruptions.
- Where human judgment dominates: Controllers interpret service priorities and real-world constraints faster than static optimization models.
- Where people leave the system of record: Carrier calls, texts, and manual route notes remain central to live execution.

## Software Landscape

- What software exists today: Typical stacks combine Maintenance Management, Utility Operations and Billing, Industrial Automation and SCADA, ERP; representative software in market today includes IFS Enterprise Asset Management, Yardi, ServiceTitan, Oracle Utilities, IFS, Oracle Utilities Customer to Meter.
- Representative vendors: IFS Enterprise Asset Management; Yardi; ServiceTitan; Oracle Utilities; IFS; Oracle Utilities Customer to Meter; SAP; GE Vernova
- Why this has not been solved cleanly: Network state changes in real time and often depends on partner data that is late, partial, or nonstandard. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Technical`

## Current Vendor Research

- [IFS Enterprise Asset Management](https://www.ifs.com/en/products/alm/eam)
- [Oracle Utilities Customer to Meter](https://docs.oracle.com/en/industries/energy-water/advanced-meter/index.html)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Network Infrastructure Operations`: Operates capital-intensive service networks through planning, provisioning, reliability, billing, and regulatory control.
