# Procurement and Replenishment

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Sourcing and Supply`
- Operating systems: `Distribution and Trade Operations`
- Industries using this workflow: `Wholesale trade`
- Industry count: 1
- Systems-of-record categories: `Order Management System | Supply Chain Planning | Warehouse Management System | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Secure the right materials or supplies at the right time and cost without destabilizing downstream operations.
- Trigger: Planned or reactive demand requires a purchase, replenishment, or sourcing action.
- End outcome: A committed supply action is placed and visible to receiving, planning, and operating teams.
- Primary actors: buyer; planner; supplier; operations or inventory owner
- Major decisions: What quantity and timing should be ordered now?; Which source best fits the current cost, quality, and service tradeoff?; What shortage or exception requires escalation?
- Major handoffs: demand plan -> procurement; purchase action -> supplier; confirmed supply -> receiving or execution teams
- Systems of record involved: Order Management System | Supply Chain Planning | Warehouse Management System | ERP

## Current-State Friction

- Where money is lost: Leakage appears through rush buys, stockouts, overbuying, and weak term control.
- Where time is lost: Buyers spend time chasing confirmations, comparing suppliers, and repairing plan mismatches.
- Where human judgment dominates: Source selection and expedites still rely on local knowledge and changing supplier behavior.
- Where people leave the system of record: Exception discussions and commitments often move into email and supplier portals beyond the ERP trail.

## Software Landscape

- What software exists today: Typical stacks combine Order Management System, Supply Chain Planning, Warehouse Management System, ERP; representative software in market today includes Manhattan ActiveOrder, Manhattan Associates, Salesforce Commerce Cloud, Oracle Retail, Blue Yonder Integrated Business Planning, Kinaxis.
- Representative vendors: Manhattan ActiveOrder; Manhattan Associates; Salesforce Commerce Cloud; Oracle Retail; Blue Yonder Integrated Business Planning; Kinaxis; o9 Solutions; Blue Yonder
- Why this has not been solved cleanly: Procurement tools are strong on structured buying, but supply volatility and exception-driven replenishment remain stubborn. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Economic`

## Current Vendor Research

- [Manhattan ActiveOrder](https://www.manh.com/solutions/omnichannel-software-solutions/order-management-system)
- [Blue Yonder Integrated Business Planning](https://blueyonder.com/solutions/supply-chain-planning/integrated-business-planning)
- [Kinaxis](https://www.kinaxis.com/en)
- [o9 Solutions](https://o9solutions.com/)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Distribution and Trade Operations`: Coordinates suppliers, inventory, pricing, order flow, and receivables across trade networks.
