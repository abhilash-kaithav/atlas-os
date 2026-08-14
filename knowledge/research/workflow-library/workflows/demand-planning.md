# Demand Planning

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Planning and Allocation`
- Operating systems: `Distribution and Trade Operations | Process Manufacturing and Throughput Control`
- Industries using this workflow: `Wholesale trade | Food and beverage and tobacco products`
- Industry count: 2
- Systems-of-record categories: `Supply Chain Planning | Manufacturing Execution System | Order Management System | Industrial Automation and SCADA | Warehouse Management System | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Set the next operating baseline for capacity, demand, production, or resource use under uncertain conditions.
- Trigger: A planning horizon opens or enough signal changes that the current plan no longer fits reality.
- End outcome: A practical baseline plan is published with assumptions and accountable owners documented.
- Primary actors: planner; operations leader; commercial or finance partner; downstream execution owner
- Major decisions: What demand and capacity assumptions should the organization trust right now?; Which tradeoff between service, cost, and utilization is acceptable?; When should the baseline be changed rather than managed through exceptions?
- Major handoffs: market or operating signals -> planning team; published plan -> procurement, labor, or execution teams; plan variance -> management review
- Systems of record involved: Supply Chain Planning | Manufacturing Execution System | Order Management System | Industrial Automation and SCADA | Warehouse Management System | ERP

## Current-State Friction

- Where money is lost: Forecast error and poor allocation create excess cost, missed revenue, and avoidable firefighting.
- Where time is lost: Planning teams spend time rebuilding assumptions and chasing sign-off across functions.
- Where human judgment dominates: Planners still decide which signals to trust and when the model output does not fit local reality.
- Where people leave the system of record: Scenario analysis and negotiation happen in spreadsheets, slides, and side conversations.

## Software Landscape

- What software exists today: Typical stacks combine Supply Chain Planning, Manufacturing Execution System, Order Management System, Industrial Automation and SCADA, and adjacent specialist systems; representative software in market today includes Blue Yonder Integrated Business Planning, Kinaxis, o9 Solutions, Blue Yonder, Manhattan Associates, Infor.
- Representative vendors: Blue Yonder Integrated Business Planning; Kinaxis; o9 Solutions; Blue Yonder; Manhattan Associates; Infor; Siemens Opcenter; Rockwell FactoryTalk MES
- Why this has not been solved cleanly: The hard problem is not math alone; it is aligning noisy signals, local constraints, and organizational trust. It typically spans 2 operating-system contexts and 6 systems-of-record categories.
- Primary reason: `Technical`

## Current Vendor Research

- [Blue Yonder Integrated Business Planning](https://blueyonder.com/solutions/supply-chain-planning/integrated-business-planning)
- [Kinaxis](https://www.kinaxis.com/en)
- [o9 Solutions](https://o9solutions.com/)
- [Siemens Opcenter](https://www.siemens.com/en-us/products/opcenter/)
- [Rockwell FactoryTalk MES](https://www.rockwellautomation.com/en-us/products/software/factorytalk/operationsuite/mes.html)
- [Manhattan ActiveOrder](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Distribution and Trade Operations`: Coordinates suppliers, inventory, pricing, order flow, and receivables across trade networks.
- `Process Manufacturing and Throughput Control`: Converts feedstocks into standardized output through planning, process control, quality, maintenance, and logistics.
