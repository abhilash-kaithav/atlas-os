# Store Labor Execution

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Workforce and Labor Operations`
- Operating systems: `Retail and Service Commerce`
- Industries using this workflow: `General merchandise stores`
- Industry count: 1
- Systems-of-record categories: `Order Management System | Supply Chain Planning | Commerce Platform | Warehouse Management System | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Publish and maintain a near-term labor schedule that covers demand, skills, and compliance constraints.
- Trigger: A shift pattern, service forecast, or operational change requires schedule creation or adjustment.
- End outcome: Workers know where to be, managers know coverage, and actual changes can flow into payroll and performance systems.
- Primary actors: scheduler; frontline manager; worker; HR or payroll partner
- Major decisions: Who should work which shift or route?; How should shortages, absences, or overtime risk be handled?; When is a local override justified despite the planning rule?
- Major handoffs: forecast -> scheduler; published schedule -> workers and managers; actual changes -> payroll, billing, or service review
- Systems of record involved: Order Management System | Supply Chain Planning | Commerce Platform | Warehouse Management System | ERP

## Current-State Friction

- Where money is lost: Overtime, uncovered demand, idle time, and payroll corrections are the core leaks.
- Where time is lost: Schedulers constantly rework the plan around callouts, fairness concerns, and compliance rules.
- Where human judgment dominates: Managers know who can actually handle the work and what informal tradeoffs will hold the operation together.
- Where people leave the system of record: The live schedule lives in texts, calls, and local shift notes once the day starts moving.

## Software Landscape

- What software exists today: Typical stacks combine Order Management System, Supply Chain Planning, Commerce Platform, Warehouse Management System, and adjacent specialist systems; representative software in market today includes Manhattan ActiveOrder, Manhattan Associates, Salesforce Commerce Cloud, Oracle Retail, Blue Yonder Integrated Business Planning, Kinaxis.
- Representative vendors: Manhattan ActiveOrder; Manhattan Associates; Salesforce Commerce Cloud; Oracle Retail; Blue Yonder Integrated Business Planning; Kinaxis; o9 Solutions; Blue Yonder
- Why this has not been solved cleanly: Workforce systems solve the baseline but not the velocity of same-day human exceptions. It typically spans 1 operating-system context and 5 systems-of-record categories.
- Primary reason: `Behavioral`

## Current Vendor Research

- [Manhattan ActiveOrder](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system)
- [Blue Yonder Integrated Business Planning](https://blueyonder.com/solutions/supply-chain-planning/integrated-business-planning)
- [Kinaxis](https://www.kinaxis.com/en)
- [o9 Solutions](https://o9solutions.com/)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Retail and Service Commerce`: Monetizes traffic, assortment, transactions, service execution, labor, and repeat demand across commerce channels.
