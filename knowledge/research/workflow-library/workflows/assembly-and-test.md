# Assembly and Test

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Production and Asset Operations`
- Operating systems: `Product Manufacturing and Lifecycle Operations`
- Industries using this workflow: `Machinery | Electrical equipment, appliances, and components`
- Industry count: 2
- Systems-of-record categories: `Manufacturing Execution System | Maintenance Management | PLM and Engineering Design | Shop Floor Control and Quality | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Run the physical process or line at the required throughput and quality with clear status and escalation control.
- Trigger: A production run, asset cycle, or operating shift is ready to execute.
- End outcome: Output is produced, status is recorded, and any exception is handed to the right follow-up owner.
- Primary actors: operations supervisor; machine or process operator; quality or maintenance staff; planner
- Major decisions: What run order or operating mode best fits current conditions?; What issue should stop the line versus be worked around?; When is output acceptable enough to release or continue?
- Major handoffs: plan -> line or field operators; execution -> quality or maintenance team; completed output -> logistics, inventory, or finance
- Systems of record involved: Manufacturing Execution System | Maintenance Management | PLM and Engineering Design | Shop Floor Control and Quality | ERP

## Current-State Friction

- Where money is lost: Scrap, slow cycles, poor yields, and unplanned downtime are the main leakages.
- Where time is lost: Operators lose time to waiting, restarts, manual data capture, and coordination across shifts.
- Where human judgment dominates: Supervisors balance throughput, quality, and risk when conditions diverge from the ideal run.
- Where people leave the system of record: Operational nuance lives in shift notes, whiteboards, and tribal knowledge outside MES and ERP fields.

## Software Landscape

- What software exists today: Typical stacks combine Manufacturing Execution System, Maintenance Management, PLM and Engineering Design, Shop Floor Control and Quality, and adjacent specialist systems; representative software in market today includes Siemens Opcenter, Rockwell FactoryTalk MES, Plex, Epicor, Rockwell FactoryTalk, IFS Enterprise Asset Management.
- Representative vendors: Siemens Opcenter; Rockwell FactoryTalk MES; Plex; Epicor; Rockwell FactoryTalk; IFS Enterprise Asset Management; Yardi; ServiceTitan
- Why this has not been solved cleanly: Even with modern MES, the last mile of execution still depends on local conditions and human adaptation. It typically spans 1 operating-system context and 5 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [Siemens Opcenter](https://www.siemens.com/en-us/products/opcenter/)
- [Rockwell FactoryTalk MES](https://www.rockwellautomation.com/en-us/products/software/factorytalk/operationsuite/mes.html)
- [IFS Enterprise Asset Management](https://www.ifs.com/en/products/alm/eam)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Product Manufacturing and Lifecycle Operations`: Designs, plans, manufactures, certifies, fulfills, and supports discrete products across supplier and channel networks.
