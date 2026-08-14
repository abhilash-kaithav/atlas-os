# Product and Engineering Configuration

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Product, Content, and Engineering`
- Operating systems: `Product Manufacturing and Lifecycle Operations`
- Industries using this workflow: `Machinery`
- Industry count: 1
- Systems-of-record categories: `Maintenance Management | Manufacturing Execution System | PLM and Engineering Design | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Maintain the authoritative product, engineering, or release record so downstream execution runs against the correct definition.
- Trigger: A new product, change request, or release milestone requires controlled updates to the master record.
- End outcome: The approved version is published with dependencies and downstream impact clearly communicated.
- Primary actors: product or engineering owner; change or release manager; operations partner; commercial or legal reviewer
- Major decisions: Which change set is safe and worth promoting now?; What dependency or downstream effect blocks release?; What version should be treated as authoritative for execution?
- Major handoffs: product or design work -> engineering or release control; approved record -> manufacturing, platform, or commercial teams; released version -> support, billing, or customer-facing teams
- Systems of record involved: Maintenance Management | Manufacturing Execution System | PLM and Engineering Design | ERP

## Current-State Friction

- Where money is lost: Master-data mistakes and release delays create rework, scrap, missed launch windows, and downstream confusion.
- Where time is lost: Teams manually synchronize definitions across PLM, ERP, support, and commercial systems.
- Where human judgment dominates: Tradeoffs among quality, timing, and downstream disruption remain human-led.
- Where people leave the system of record: Critical rationale and version decisions live in reviews, comments, and docs outside the system of record.

## Software Landscape

- What software exists today: Typical stacks combine Maintenance Management, Manufacturing Execution System, PLM and Engineering Design, ERP; representative software in market today includes IFS Enterprise Asset Management, Yardi, ServiceTitan, Oracle Utilities, IFS, Siemens Opcenter.
- Representative vendors: IFS Enterprise Asset Management; Yardi; ServiceTitan; Oracle Utilities; IFS; Siemens Opcenter; Rockwell FactoryTalk MES; Plex
- Why this has not been solved cleanly: Structured data and collaborative work still sit in separate tools, so version truth remains hard to unify. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [IFS Enterprise Asset Management](https://www.ifs.com/en/products/alm/eam)
- [Siemens Opcenter](https://www.siemens.com/en-us/products/opcenter/)
- [Rockwell FactoryTalk MES](https://www.rockwellautomation.com/en-us/products/software/factorytalk/operationsuite/mes.html)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Product Manufacturing and Lifecycle Operations`: Designs, plans, manufactures, certifies, fulfills, and supports discrete products across supplier and channel networks.
