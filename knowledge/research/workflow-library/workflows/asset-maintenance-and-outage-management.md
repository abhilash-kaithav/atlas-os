# Asset Maintenance and Outage Management

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Production and Asset Operations`
- Operating systems: `Network Infrastructure Operations`
- Industries using this workflow: `Utilities`
- Industry count: 1
- Systems-of-record categories: `Maintenance Management | Utility Operations and Billing | Industrial Automation and SCADA | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Restore or preserve asset readiness with the right work orders, parts, sequencing, and outage discipline.
- Trigger: An asset reaches a maintenance threshold, fails, turns over, or must be prepared for the next use.
- End outcome: The asset returns to service or readiness with maintenance history and follow-up actions captured.
- Primary actors: maintenance planner; technician; operations owner; parts or contractor support
- Major decisions: What work is urgent now versus deferrable?; What outage, turnover, or turnaround scope is required to restore readiness?; What issue should be repaired, monitored, or replaced entirely?
- Major handoffs: operations signal -> maintenance planning; planned work -> technicians or contractors; returned asset -> operations and finance history
- Systems of record involved: Maintenance Management | Utility Operations and Billing | Industrial Automation and SCADA | ERP

## Current-State Friction

- Where money is lost: Leakage comes from downtime, repeat failures, poor work scope, and weak turnover discipline.
- Where time is lost: Teams chase parts, permits, technician availability, and asset-history context.
- Where human judgment dominates: Maintenance leaders still assess condition, risk, and repair tradeoffs beyond simple rules.
- Where people leave the system of record: Readiness and outage details are frequently tracked in calls, notes, and local sheets outside the CMMS.

## Software Landscape

- What software exists today: Typical stacks combine Maintenance Management, Utility Operations and Billing, Industrial Automation and SCADA, ERP; representative software in market today includes IFS Enterprise Asset Management, Yardi, ServiceTitan, Oracle Utilities, IFS, Oracle Utilities Customer to Meter.
- Representative vendors: IFS Enterprise Asset Management; Yardi; ServiceTitan; Oracle Utilities; IFS; Oracle Utilities Customer to Meter; SAP; GE Vernova
- Why this has not been solved cleanly: Maintenance systems track work orders, but true readiness still depends on fragmented context and field judgment. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [IFS Enterprise Asset Management](https://www.ifs.com/en/products/alm/eam)
- [Oracle Utilities Customer to Meter](https://docs.oracle.com/en/industries/energy-water/advanced-meter/index.html)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Network Infrastructure Operations`: Operates capital-intensive service networks through planning, provisioning, reliability, billing, and regulatory control.
