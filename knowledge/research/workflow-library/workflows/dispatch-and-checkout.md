# Dispatch and Checkout

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Delivery and Service Execution`
- Operating systems: `Asset Utilization and Lease Management`
- Industries using this workflow: `Rental and leasing services and lessors of intangible assets`
- Industry count: 1
- Systems-of-record categories: `Maintenance Management | Rental Operations Management | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Execute work in the field while adapting safely to site conditions, change requests, and incomplete information.
- Trigger: A field team is dispatched or mobilized to perform work at a site, customer, or operating location.
- End outcome: The field task is completed, deferred, or escalated with actual conditions captured for downstream use.
- Primary actors: field supervisor; technician or crew; customer or site contact; back-office coordinator
- Major decisions: What can actually be completed given current site conditions?; What change requires new approval, scope, or documentation?; What issue should be solved locally versus escalated?
- Major handoffs: dispatch or planning -> field crew; field crew -> back office, customer, or inspector; completed work -> billing, maintenance history, or reporting
- Systems of record involved: Maintenance Management | Rental Operations Management | ERP

## Current-State Friction

- Where money is lost: Travel waste, revisit rates, change-order misses, and field rework are the main economic leaks.
- Where time is lost: Crews lose time to waiting, missing parts, unclear scope, and back-and-forth approvals.
- Where human judgment dominates: Field leads interpret site reality, safety, and customer context in ways that no template fully captures.
- Where people leave the system of record: Actual field decisions are coordinated over calls, text, and paper notes before systems are updated later.

## Software Landscape

- What software exists today: Typical stacks combine Maintenance Management, Rental Operations Management, ERP; representative software in market today includes IFS Enterprise Asset Management, Yardi, ServiceTitan, Oracle Utilities, IFS, AssetWorks.
- Representative vendors: IFS Enterprise Asset Management; Yardi; ServiceTitan; Oracle Utilities; IFS; AssetWorks; LeaseQuery; Oracle
- Why this has not been solved cleanly: Field conditions mutate faster than central systems, making local judgment indispensable. It typically spans 1 operating-system context and 3 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [IFS Enterprise Asset Management](https://www.ifs.com/en/products/alm/eam)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Asset Utilization and Lease Management`: Monetizes owned or controlled assets through occupancy or utilization, contract terms, maintenance, turnover, and billing discipline.
