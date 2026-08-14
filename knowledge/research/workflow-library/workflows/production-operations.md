# Production Operations

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Production and Asset Operations`
- Operating systems: `Field Production and Resource Extraction`
- Industries using this workflow: `Oil and gas extraction`
- Industry count: 1
- Systems-of-record categories: `Geoscience and Reservoir Management | Production Accounting and Regulatory | Upstream Energy Management | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Run the physical process or line at the required throughput and quality with clear status and escalation control.
- Trigger: A production run, asset cycle, or operating shift is ready to execute.
- End outcome: Output is produced, status is recorded, and any exception is handed to the right follow-up owner.
- Primary actors: operations supervisor; machine or process operator; quality or maintenance staff; planner
- Major decisions: What run order or operating mode best fits current conditions?; What issue should stop the line versus be worked around?; When is output acceptable enough to release or continue?
- Major handoffs: plan -> line or field operators; execution -> quality or maintenance team; completed output -> logistics, inventory, or finance
- Systems of record involved: Geoscience and Reservoir Management | Production Accounting and Regulatory | Upstream Energy Management | ERP

## Current-State Friction

- Where money is lost: Scrap, slow cycles, poor yields, and unplanned downtime are the main leakages.
- Where time is lost: Operators lose time to waiting, restarts, manual data capture, and coordination across shifts.
- Where human judgment dominates: Supervisors balance throughput, quality, and risk when conditions diverge from the ideal run.
- Where people leave the system of record: Operational nuance lives in shift notes, whiteboards, and tribal knowledge outside MES and ERP fields.

## Software Landscape

- What software exists today: Typical stacks combine Geoscience and Reservoir Management, Production Accounting and Regulatory, Upstream Energy Management, ERP; representative software in market today includes SLB Delfi, Halliburton Landmark, Quorum, Enverus, SAP, Acumatica Cloud ERP.
- Representative vendors: SLB Delfi; Halliburton Landmark; Quorum; Enverus; SAP; Acumatica Cloud ERP; Oracle; NetSuite
- Why this has not been solved cleanly: Even with modern MES, the last mile of execution still depends on local conditions and human adaptation. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Field Production and Resource Extraction`: Converts land or reserves into output through field planning, operations, logistics, and revenue or regulatory management.
