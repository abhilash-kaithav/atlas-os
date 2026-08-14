# Field Execution and Change Management

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Delivery and Service Execution`
- Operating systems: `Project Delivery and Contracting`
- Industries using this workflow: `Construction`
- Industry count: 1
- Systems-of-record categories: `Project and Construction Management | Scheduling and Planning | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Execute work in the field while adapting safely to site conditions, change requests, and incomplete information.
- Trigger: A field team is dispatched or mobilized to perform work at a site, customer, or operating location.
- End outcome: The field task is completed, deferred, or escalated with actual conditions captured for downstream use.
- Primary actors: field supervisor; technician or crew; customer or site contact; back-office coordinator
- Major decisions: What can actually be completed given current site conditions?; What change requires new approval, scope, or documentation?; What issue should be solved locally versus escalated?
- Major handoffs: dispatch or planning -> field crew; field crew -> back office, customer, or inspector; completed work -> billing, maintenance history, or reporting
- Systems of record involved: Project and Construction Management | Scheduling and Planning | ERP

## Current-State Friction

- Where money is lost: Travel waste, revisit rates, change-order misses, and field rework are the main economic leaks.
- Where time is lost: Crews lose time to waiting, missing parts, unclear scope, and back-and-forth approvals.
- Where human judgment dominates: Field leads interpret site reality, safety, and customer context in ways that no template fully captures.
- Where people leave the system of record: Actual field decisions are coordinated over calls, text, and paper notes before systems are updated later.

## Software Landscape

- What software exists today: Typical stacks combine Project and Construction Management, Scheduling and Planning, ERP; representative software in market today includes Procore, Procore Financial Management, Autodesk Construction Cloud, Oracle Primavera, Anaplan, Blue Yonder.
- Representative vendors: Procore; Procore Financial Management; Autodesk Construction Cloud; Oracle Primavera; Anaplan; Blue Yonder; SAP Cloud ERP; Acumatica Cloud ERP
- Why this has not been solved cleanly: Field conditions mutate faster than central systems, making local judgment indispensable. It typically spans 1 operating-system context and 3 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [Procore](https://www.procore.com/what-is-procore)
- [Procore Financial Management](https://www.procore.com/financial-management)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Project Delivery and Contracting`: Delivers scoped projects through estimation, scheduling, subcontractor coordination, field execution, and progress billing.
