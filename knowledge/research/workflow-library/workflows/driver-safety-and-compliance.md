# Driver Safety and Compliance

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Risk, Compliance, and Reporting`
- Operating systems: `Transportation Network Operations`
- Industries using this workflow: `Truck transportation`
- Industry count: 1
- Systems-of-record categories: `Transportation Management System | Fleet Telematics and Visibility | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Prove that output, operations, or service meet required standards before release or continued execution.
- Trigger: A production step, service checkpoint, or formal control requirement calls for inspection or compliance review.
- End outcome: The item is passed, failed, quarantined, or escalated with evidence attached to the record.
- Primary actors: quality or compliance owner; operator or frontline staff; manager; external customer or regulator
- Major decisions: Does the item meet the release threshold?; What deviation is acceptable versus requiring stop-work or escalation?; What corrective action and evidence are necessary?
- Major handoffs: operations -> quality or compliance team; quality finding -> rework or management action; released item -> downstream fulfillment or reporting
- Systems of record involved: Transportation Management System | Fleet Telematics and Visibility | ERP

## Current-State Friction

- Where money is lost: Failures, recalls, rework, and excess inspection labor are the major leakage points.
- Where time is lost: Teams repeat data entry, collect evidence manually, and wait on disposition decisions.
- Where human judgment dominates: Inspectors still interpret severity, traceability gaps, and acceptable release decisions.
- Where people leave the system of record: Evidence often sits in attachments, lab systems, spreadsheets, and manual checklists outside the main record.

## Software Landscape

- What software exists today: Typical stacks combine Transportation Management System, Fleet Telematics and Visibility, ERP; representative software in market today includes project44, McLeod, Oracle Transportation Management, Descartes, CargoWise, Samsara.
- Representative vendors: project44; McLeod; Oracle Transportation Management; Descartes; CargoWise; Samsara; Trimble Transportation; SAP Cloud ERP
- Why this has not been solved cleanly: Standards are formal, but real-world deviations and root-cause interpretation remain human-heavy. It typically spans 1 operating-system context and 3 systems-of-record categories.
- Primary reason: `Regulatory`

## Current Vendor Research

- [project44](https://www.project44.com/platform/tms/)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Transportation Network Operations`: Plans capacity, routes assets, manages exceptions, and settles transport across operating networks.
