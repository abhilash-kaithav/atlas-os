# Quality Inspection and Certification

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Risk, Compliance, and Reporting`
- Operating systems: `Process Manufacturing and Throughput Control | Product Manufacturing and Lifecycle Operations`
- Industries using this workflow: `Fabricated metal products | Primary metals`
- Industry count: 2
- Systems-of-record categories: `Maintenance Management | Manufacturing Execution System | Shop Floor Control and Quality | Industrial Automation and SCADA | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Prove that output, operations, or service meet required standards before release or continued execution.
- Trigger: A production step, service checkpoint, or formal control requirement calls for inspection or compliance review.
- End outcome: The item is passed, failed, quarantined, or escalated with evidence attached to the record.
- Primary actors: quality or compliance owner; operator or frontline staff; manager; external customer or regulator
- Major decisions: Does the item meet the release threshold?; What deviation is acceptable versus requiring stop-work or escalation?; What corrective action and evidence are necessary?
- Major handoffs: operations -> quality or compliance team; quality finding -> rework or management action; released item -> downstream fulfillment or reporting
- Systems of record involved: Maintenance Management | Manufacturing Execution System | Shop Floor Control and Quality | Industrial Automation and SCADA | ERP

## Current-State Friction

- Where money is lost: Failures, recalls, rework, and excess inspection labor are the major leakage points.
- Where time is lost: Teams repeat data entry, collect evidence manually, and wait on disposition decisions.
- Where human judgment dominates: Inspectors still interpret severity, traceability gaps, and acceptable release decisions.
- Where people leave the system of record: Evidence often sits in attachments, lab systems, spreadsheets, and manual checklists outside the main record.

## Software Landscape

- What software exists today: Typical stacks combine Maintenance Management, Manufacturing Execution System, Shop Floor Control and Quality, Industrial Automation and SCADA, and adjacent specialist systems; representative software in market today includes IFS Enterprise Asset Management, Yardi, ServiceTitan, Oracle Utilities, IFS, Siemens Opcenter.
- Representative vendors: IFS Enterprise Asset Management; Yardi; ServiceTitan; Oracle Utilities; IFS; Siemens Opcenter; Rockwell FactoryTalk MES; Plex
- Why this has not been solved cleanly: Standards are formal, but real-world deviations and root-cause interpretation remain human-heavy. It typically spans 2 operating-system contexts and 5 systems-of-record categories.
- Primary reason: `Regulatory`

## Current Vendor Research

- [IFS Enterprise Asset Management](https://www.ifs.com/en/products/alm/eam)
- [Siemens Opcenter](https://www.siemens.com/en-us/products/opcenter/)
- [Rockwell FactoryTalk MES](https://www.rockwellautomation.com/en-us/products/software/factorytalk/operationsuite/mes.html)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Process Manufacturing and Throughput Control`: Converts feedstocks into standardized output through planning, process control, quality, maintenance, and logistics.
- `Product Manufacturing and Lifecycle Operations`: Designs, plans, manufactures, certifies, fulfills, and supports discrete products across supplier and channel networks.
