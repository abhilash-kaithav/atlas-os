# Asset Maintenance and Uptime Management

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Production and Asset Operations`
- Operating systems: `Process Manufacturing and Throughput Control`
- Industries using this workflow: `Primary metals | Paper products`
- Industry count: 2
- Systems-of-record categories: `Maintenance Management | Supply Chain Planning | Industrial Automation and SCADA | Shop Floor Control and Quality | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Restore or preserve asset readiness with the right work orders, parts, sequencing, and outage discipline.
- Trigger: An asset reaches a maintenance threshold, fails, turns over, or must be prepared for the next use.
- End outcome: The asset returns to service or readiness with maintenance history and follow-up actions captured.
- Primary actors: maintenance planner; technician; operations owner; parts or contractor support
- Major decisions: What work is urgent now versus deferrable?; What outage, turnover, or turnaround scope is required to restore readiness?; What issue should be repaired, monitored, or replaced entirely?
- Major handoffs: operations signal -> maintenance planning; planned work -> technicians or contractors; returned asset -> operations and finance history
- Systems of record involved: Maintenance Management | Supply Chain Planning | Industrial Automation and SCADA | Shop Floor Control and Quality | ERP

## Current-State Friction

- Where money is lost: Leakage comes from downtime, repeat failures, poor work scope, and weak turnover discipline.
- Where time is lost: Teams chase parts, permits, technician availability, and asset-history context.
- Where human judgment dominates: Maintenance leaders still assess condition, risk, and repair tradeoffs beyond simple rules.
- Where people leave the system of record: Readiness and outage details are frequently tracked in calls, notes, and local sheets outside the CMMS.

## Software Landscape

- What software exists today: Typical stacks combine Maintenance Management, Supply Chain Planning, Industrial Automation and SCADA, Shop Floor Control and Quality, and adjacent specialist systems; representative software in market today includes IFS Enterprise Asset Management, Yardi, ServiceTitan, Oracle Utilities, IFS, Blue Yonder Integrated Business Planning.
- Representative vendors: IFS Enterprise Asset Management; Yardi; ServiceTitan; Oracle Utilities; IFS; Blue Yonder Integrated Business Planning; Kinaxis; o9 Solutions
- Why this has not been solved cleanly: Maintenance systems track work orders, but true readiness still depends on fragmented context and field judgment. It typically spans 1 operating-system context and 5 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [IFS Enterprise Asset Management](https://www.ifs.com/en/products/alm/eam)
- [Blue Yonder Integrated Business Planning](https://blueyonder.com/solutions/supply-chain-planning/integrated-business-planning)
- [Kinaxis](https://www.kinaxis.com/en)
- [o9 Solutions](https://o9solutions.com/)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Process Manufacturing and Throughput Control`: Converts feedstocks into standardized output through planning, process control, quality, maintenance, and logistics.
