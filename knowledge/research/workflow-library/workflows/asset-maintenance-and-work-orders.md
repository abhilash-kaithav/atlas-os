# Asset Maintenance and Work Orders

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Production and Asset Operations`
- Operating systems: `Asset Utilization and Lease Management`
- Industries using this workflow: `Housing | Other real estate`
- Industry count: 2
- Systems-of-record categories: `Property Management System | Fund Administration and Accounting | Maintenance Management | Real Estate Asset Management | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Restore or preserve asset readiness with the right work orders, parts, sequencing, and outage discipline.
- Trigger: An asset reaches a maintenance threshold, fails, turns over, or must be prepared for the next use.
- End outcome: The asset returns to service or readiness with maintenance history and follow-up actions captured.
- Primary actors: maintenance planner; technician; operations owner; parts or contractor support
- Major decisions: What work is urgent now versus deferrable?; What outage, turnover, or turnaround scope is required to restore readiness?; What issue should be repaired, monitored, or replaced entirely?
- Major handoffs: operations signal -> maintenance planning; planned work -> technicians or contractors; returned asset -> operations and finance history
- Systems of record involved: Property Management System | Fund Administration and Accounting | Maintenance Management | Real Estate Asset Management | CRM

## Current-State Friction

- Where money is lost: Leakage comes from downtime, repeat failures, poor work scope, and weak turnover discipline.
- Where time is lost: Teams chase parts, permits, technician availability, and asset-history context.
- Where human judgment dominates: Maintenance leaders still assess condition, risk, and repair tradeoffs beyond simple rules.
- Where people leave the system of record: Readiness and outage details are frequently tracked in calls, notes, and local sheets outside the CMMS.

## Software Landscape

- What software exists today: Typical stacks combine Property Management System, Fund Administration and Accounting, Maintenance Management, Real Estate Asset Management, and adjacent specialist systems; representative software in market today includes Yardi, RealPage, AppFolio, Entrata, Allvue Fund Accounting, Aladdin Accounting.
- Representative vendors: Yardi; RealPage; AppFolio; Entrata; Allvue Fund Accounting; Aladdin Accounting; SS&C; SimCorp
- Why this has not been solved cleanly: Maintenance systems track work orders, but true readiness still depends on fragmented context and field judgment. It typically spans 1 operating-system context and 5 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [Yardi](https://www.yardi.com/solution/property-management-software/)
- [Allvue Fund Accounting](https://www.allvuesystems.com/solutions/fund-accounting/)
- [Aladdin Accounting](https://www.blackrock.com/aladdin/platforms/products/aladdin-accounting)
- [IFS Enterprise Asset Management](https://www.ifs.com/en/products/alm/eam)
- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Asset Utilization and Lease Management`: Monetizes owned or controlled assets through occupancy or utilization, contract terms, maintenance, turnover, and billing discipline.
