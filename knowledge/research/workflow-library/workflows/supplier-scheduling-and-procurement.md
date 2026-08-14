# Supplier Scheduling and Procurement

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Sourcing and Supply`
- Operating systems: `Product Manufacturing and Lifecycle Operations`
- Industries using this workflow: `Motor vehicles, bodies and trailers, and parts | Machinery | Electrical equipment, appliances, and components`
- Industry count: 3
- Systems-of-record categories: `Manufacturing Execution System | Maintenance Management | Supply Chain Planning | PLM and Engineering Design | Shop Floor Control and Quality | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Maintain supplier or subcontractor performance, readiness, and compliance so upstream plans can translate into reliable execution.
- Trigger: A supplier relationship must be scheduled, coordinated, or reviewed against active operating requirements.
- End outcome: The external partner is committed, compliant, and visible in the delivery plan.
- Primary actors: supplier manager or buyer; supplier or subcontractor; operations or project owner; quality or compliance staff
- Major decisions: Which external partner should be trusted with this scope now?; What compliance or readiness gap must be closed before work starts?; When is a partner issue severe enough to replace or escalate?
- Major handoffs: project or production demand -> supplier manager; supplier commitment -> field, plant, or project team; performance issue -> quality, finance, or leadership review
- Systems of record involved: Manufacturing Execution System | Maintenance Management | Supply Chain Planning | PLM and Engineering Design | Shop Floor Control and Quality | ERP

## Current-State Friction

- Where money is lost: Leakage comes from supplier misses, poor coordination, and weak compliance discipline that forces recovery work.
- Where time is lost: Teams spend time on follow-up, document checks, and schedule alignment across organizational boundaries.
- Where human judgment dominates: Partner selection and intervention strategy remain experience-heavy and relationship-driven.
- Where people leave the system of record: Actual supplier coordination lives in calls, emails, and shared trackers beyond the formal procurement record.

## Software Landscape

- What software exists today: Typical stacks combine Manufacturing Execution System, Maintenance Management, Supply Chain Planning, PLM and Engineering Design, and adjacent specialist systems; representative software in market today includes Siemens Opcenter, Rockwell FactoryTalk MES, Plex, Epicor, Rockwell FactoryTalk, IFS Enterprise Asset Management.
- Representative vendors: Siemens Opcenter; Rockwell FactoryTalk MES; Plex; Epicor; Rockwell FactoryTalk; IFS Enterprise Asset Management; Yardi; ServiceTitan
- Why this has not been solved cleanly: Structured supplier master data is not the same as reliable day-to-day execution behavior. It typically spans 1 operating-system context and 6 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [Siemens Opcenter](https://www.siemens.com/en-us/products/opcenter/)
- [Rockwell FactoryTalk MES](https://www.rockwellautomation.com/en-us/products/software/factorytalk/operationsuite/mes.html)
- [IFS Enterprise Asset Management](https://www.ifs.com/en/products/alm/eam)
- [Blue Yonder Integrated Business Planning](https://blueyonder.com/solutions/supply-chain-planning/integrated-business-planning)
- [Kinaxis](https://www.kinaxis.com/en)
- [o9 Solutions](https://o9solutions.com/)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Product Manufacturing and Lifecycle Operations`: Designs, plans, manufactures, certifies, fulfills, and supports discrete products across supplier and channel networks.
