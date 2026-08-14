# Inventory and Perishables Management

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Production and Asset Operations`
- Operating systems: `Retail and Service Commerce`
- Industries using this workflow: `Food and beverage stores`
- Industry count: 1
- Systems-of-record categories: `POS and Payments | Supply Chain Planning | Warehouse Management System | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Run the physical process or line at the required throughput and quality with clear status and escalation control.
- Trigger: A production run, asset cycle, or operating shift is ready to execute.
- End outcome: Output is produced, status is recorded, and any exception is handed to the right follow-up owner.
- Primary actors: operations supervisor; machine or process operator; quality or maintenance staff; planner
- Major decisions: What run order or operating mode best fits current conditions?; What issue should stop the line versus be worked around?; When is output acceptable enough to release or continue?
- Major handoffs: plan -> line or field operators; execution -> quality or maintenance team; completed output -> logistics, inventory, or finance
- Systems of record involved: POS and Payments | Supply Chain Planning | Warehouse Management System | ERP

## Current-State Friction

- Where money is lost: Scrap, slow cycles, poor yields, and unplanned downtime are the main leakages.
- Where time is lost: Operators lose time to waiting, restarts, manual data capture, and coordination across shifts.
- Where human judgment dominates: Supervisors balance throughput, quality, and risk when conditions diverge from the ideal run.
- Where people leave the system of record: Operational nuance lives in shift notes, whiteboards, and tribal knowledge outside MES and ERP fields.

## Software Landscape

- What software exists today: Typical stacks combine POS and Payments, Supply Chain Planning, Warehouse Management System, ERP; representative software in market today includes Toast POS, Square, Oracle MICROS, NCR Voyix, Blue Yonder Integrated Business Planning, Kinaxis.
- Representative vendors: Toast POS; Square; Oracle MICROS; NCR Voyix; Blue Yonder Integrated Business Planning; Kinaxis; o9 Solutions; Blue Yonder
- Why this has not been solved cleanly: Even with modern MES, the last mile of execution still depends on local conditions and human adaptation. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [Toast POS](https://pos.toasttab.com/products/point-of-sale)
- [Blue Yonder Integrated Business Planning](https://blueyonder.com/solutions/supply-chain-planning/integrated-business-planning)
- [Kinaxis](https://www.kinaxis.com/en)
- [o9 Solutions](https://o9solutions.com/)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Retail and Service Commerce`: Monetizes traffic, assortment, transactions, service execution, labor, and repeat demand across commerce channels.
