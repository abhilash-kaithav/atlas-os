# Regulatory Labeling and Compliance

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Risk, Compliance, and Reporting`
- Operating systems: `Process Manufacturing and Throughput Control`
- Industries using this workflow: `Food and beverage and tobacco products`
- Industry count: 1
- Systems-of-record categories: `Manufacturing Execution System | Supply Chain Planning | Industrial Automation and SCADA | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Prove that output, operations, or service meet required standards before release or continued execution.
- Trigger: A production step, service checkpoint, or formal control requirement calls for inspection or compliance review.
- End outcome: The item is passed, failed, quarantined, or escalated with evidence attached to the record.
- Primary actors: quality or compliance owner; operator or frontline staff; manager; external customer or regulator
- Major decisions: Does the item meet the release threshold?; What deviation is acceptable versus requiring stop-work or escalation?; What corrective action and evidence are necessary?
- Major handoffs: operations -> quality or compliance team; quality finding -> rework or management action; released item -> downstream fulfillment or reporting
- Systems of record involved: Manufacturing Execution System | Supply Chain Planning | Industrial Automation and SCADA | ERP

## Current-State Friction

- Where money is lost: Failures, recalls, rework, and excess inspection labor are the major leakage points.
- Where time is lost: Teams repeat data entry, collect evidence manually, and wait on disposition decisions.
- Where human judgment dominates: Inspectors still interpret severity, traceability gaps, and acceptable release decisions.
- Where people leave the system of record: Evidence often sits in attachments, lab systems, spreadsheets, and manual checklists outside the main record.

## Software Landscape

- What software exists today: Typical stacks combine Manufacturing Execution System, Supply Chain Planning, Industrial Automation and SCADA, ERP; representative software in market today includes Siemens Opcenter, Rockwell FactoryTalk MES, Plex, Epicor, Rockwell FactoryTalk, Blue Yonder Integrated Business Planning.
- Representative vendors: Siemens Opcenter; Rockwell FactoryTalk MES; Plex; Epicor; Rockwell FactoryTalk; Blue Yonder Integrated Business Planning; Kinaxis; o9 Solutions
- Why this has not been solved cleanly: Standards are formal, but real-world deviations and root-cause interpretation remain human-heavy. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Regulatory`

## Current Vendor Research

- [Siemens Opcenter](https://www.siemens.com/en-us/products/opcenter/)
- [Rockwell FactoryTalk MES](https://www.rockwellautomation.com/en-us/products/software/factorytalk/operationsuite/mes.html)
- [Blue Yonder Integrated Business Planning](https://blueyonder.com/solutions/supply-chain-planning/integrated-business-planning)
- [Kinaxis](https://www.kinaxis.com/en)
- [o9 Solutions](https://o9solutions.com/)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Process Manufacturing and Throughput Control`: Converts feedstocks into standardized output through planning, process control, quality, maintenance, and logistics.
