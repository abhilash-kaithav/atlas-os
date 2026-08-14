# Production Planning

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Planning and Allocation`
- Operating systems: `Product Manufacturing and Lifecycle Operations | Field Production and Resource Extraction`
- Industries using this workflow: `Farms | Fabricated metal products | Plastics and rubber products`
- Industry count: 3
- Systems-of-record categories: `Manufacturing Execution System | Shop Floor Control and Quality | Farm Management Platform | PLM and Engineering Design | Precision Agriculture and Telematics | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Set the next operating baseline for capacity, demand, production, or resource use under uncertain conditions.
- Trigger: A planning horizon opens or enough signal changes that the current plan no longer fits reality.
- End outcome: A practical baseline plan is published with assumptions and accountable owners documented.
- Primary actors: planner; operations leader; commercial or finance partner; downstream execution owner
- Major decisions: What demand and capacity assumptions should the organization trust right now?; Which tradeoff between service, cost, and utilization is acceptable?; When should the baseline be changed rather than managed through exceptions?
- Major handoffs: market or operating signals -> planning team; published plan -> procurement, labor, or execution teams; plan variance -> management review
- Systems of record involved: Manufacturing Execution System | Shop Floor Control and Quality | Farm Management Platform | PLM and Engineering Design | Precision Agriculture and Telematics | ERP

## Current-State Friction

- Where money is lost: Forecast error and poor allocation create excess cost, missed revenue, and avoidable firefighting.
- Where time is lost: Planning teams spend time rebuilding assumptions and chasing sign-off across functions.
- Where human judgment dominates: Planners still decide which signals to trust and when the model output does not fit local reality.
- Where people leave the system of record: Scenario analysis and negotiation happen in spreadsheets, slides, and side conversations.

## Software Landscape

- What software exists today: Typical stacks combine Manufacturing Execution System, Shop Floor Control and Quality, Farm Management Platform, PLM and Engineering Design, and adjacent specialist systems; representative software in market today includes Siemens Opcenter, Rockwell FactoryTalk MES, Plex, Epicor, Rockwell FactoryTalk, JobBOSS.
- Representative vendors: Siemens Opcenter; Rockwell FactoryTalk MES; Plex; Epicor; Rockwell FactoryTalk; JobBOSS; Infor; John Deere Operations Center
- Why this has not been solved cleanly: The hard problem is not math alone; it is aligning noisy signals, local constraints, and organizational trust. It typically spans 2 operating-system contexts and 6 systems-of-record categories.
- Primary reason: `Technical`

## Current Vendor Research

- [Siemens Opcenter](https://www.siemens.com/en-us/products/opcenter/)
- [Rockwell FactoryTalk MES](https://www.rockwellautomation.com/en-us/products/software/factorytalk/operationsuite/mes.html)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Product Manufacturing and Lifecycle Operations`: Designs, plans, manufactures, certifies, fulfills, and supports discrete products across supplier and channel networks.
- `Field Production and Resource Extraction`: Converts land or reserves into output through field planning, operations, logistics, and revenue or regulatory management.
