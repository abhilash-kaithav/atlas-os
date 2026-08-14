# Material Sourcing

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Sourcing and Supply`
- Operating systems: `Process Manufacturing and Throughput Control | Product Manufacturing and Lifecycle Operations`
- Industries using this workflow: `Food and beverage and tobacco products | Chemical products | Petroleum and coal products | Primary metals | Plastics and rubber products | Paper products`
- Industry count: 6
- Systems-of-record categories: `Maintenance Management | Manufacturing Execution System | Supply Chain Planning | Industrial Automation and SCADA | Shop Floor Control and Quality | PLM and Engineering Design | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Secure the right materials or supplies at the right time and cost without destabilizing downstream operations.
- Trigger: Planned or reactive demand requires a purchase, replenishment, or sourcing action.
- End outcome: A committed supply action is placed and visible to receiving, planning, and operating teams.
- Primary actors: buyer; planner; supplier; operations or inventory owner
- Major decisions: What quantity and timing should be ordered now?; Which source best fits the current cost, quality, and service tradeoff?; What shortage or exception requires escalation?
- Major handoffs: demand plan -> procurement; purchase action -> supplier; confirmed supply -> receiving or execution teams
- Systems of record involved: Maintenance Management | Manufacturing Execution System | Supply Chain Planning | Industrial Automation and SCADA | Shop Floor Control and Quality | PLM and Engineering Design | ERP

## Current-State Friction

- Where money is lost: Leakage appears through rush buys, stockouts, overbuying, and weak term control.
- Where time is lost: Buyers spend time chasing confirmations, comparing suppliers, and repairing plan mismatches.
- Where human judgment dominates: Source selection and expedites still rely on local knowledge and changing supplier behavior.
- Where people leave the system of record: Exception discussions and commitments often move into email and supplier portals beyond the ERP trail.

## Software Landscape

- What software exists today: Typical stacks combine Maintenance Management, Manufacturing Execution System, Supply Chain Planning, Industrial Automation and SCADA, and adjacent specialist systems; representative software in market today includes IFS Enterprise Asset Management, Yardi, ServiceTitan, Oracle Utilities, IFS, Siemens Opcenter.
- Representative vendors: IFS Enterprise Asset Management; Yardi; ServiceTitan; Oracle Utilities; IFS; Siemens Opcenter; Rockwell FactoryTalk MES; Plex
- Why this has not been solved cleanly: Procurement tools are strong on structured buying, but supply volatility and exception-driven replenishment remain stubborn. It typically spans 2 operating-system contexts and 7 systems-of-record categories.
- Primary reason: `Economic`

## Current Vendor Research

- [IFS Enterprise Asset Management](https://www.ifs.com/en/products/alm/eam)
- [Siemens Opcenter](https://www.siemens.com/en-us/products/opcenter/)
- [Rockwell FactoryTalk MES](https://www.rockwellautomation.com/en-us/products/software/factorytalk/operationsuite/mes.html)
- [Blue Yonder Integrated Business Planning](https://blueyonder.com/solutions/supply-chain-planning/integrated-business-planning)
- [Kinaxis](https://www.kinaxis.com/en)
- [o9 Solutions](https://o9solutions.com/)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Process Manufacturing and Throughput Control`: Converts feedstocks into standardized output through planning, process control, quality, maintenance, and logistics.
- `Product Manufacturing and Lifecycle Operations`: Designs, plans, manufactures, certifies, fulfills, and supports discrete products across supplier and channel networks.
