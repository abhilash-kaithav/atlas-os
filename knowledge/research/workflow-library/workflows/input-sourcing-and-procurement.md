# Input Sourcing and Procurement

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Sourcing and Supply`
- Operating systems: `Field Production and Resource Extraction`
- Industries using this workflow: `Farms`
- Industry count: 1
- Systems-of-record categories: `Farm Management Platform | Precision Agriculture and Telematics`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Secure the right materials or supplies at the right time and cost without destabilizing downstream operations.
- Trigger: Planned or reactive demand requires a purchase, replenishment, or sourcing action.
- End outcome: A committed supply action is placed and visible to receiving, planning, and operating teams.
- Primary actors: buyer; planner; supplier; operations or inventory owner
- Major decisions: What quantity and timing should be ordered now?; Which source best fits the current cost, quality, and service tradeoff?; What shortage or exception requires escalation?
- Major handoffs: demand plan -> procurement; purchase action -> supplier; confirmed supply -> receiving or execution teams
- Systems of record involved: Farm Management Platform | Precision Agriculture and Telematics

## Current-State Friction

- Where money is lost: Leakage appears through rush buys, stockouts, overbuying, and weak term control.
- Where time is lost: Buyers spend time chasing confirmations, comparing suppliers, and repairing plan mismatches.
- Where human judgment dominates: Source selection and expedites still rely on local knowledge and changing supplier behavior.
- Where people leave the system of record: Exception discussions and commitments often move into email and supplier portals beyond the ERP trail.

## Software Landscape

- What software exists today: Typical stacks combine Farm Management Platform, Precision Agriculture and Telematics; representative software in market today includes John Deere Operations Center, Climate FieldView, Granular, AgLeader, Trimble Agriculture.
- Representative vendors: John Deere Operations Center; Climate FieldView; Granular; AgLeader; Trimble Agriculture
- Why this has not been solved cleanly: Procurement tools are strong on structured buying, but supply volatility and exception-driven replenishment remain stubborn. It typically spans 1 operating-system context and 2 systems-of-record categories.
- Primary reason: `Economic`

## Atlas Context

- `Field Production and Resource Extraction`: Converts land or reserves into output through field planning, operations, logistics, and revenue or regulatory management.
