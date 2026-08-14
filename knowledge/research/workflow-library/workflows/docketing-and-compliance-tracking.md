# Docketing and Compliance Tracking

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Risk, Compliance, and Reporting`
- Operating systems: `Professional Services and Matter Management`
- Industries using this workflow: `Legal services`
- Industry count: 1
- Systems-of-record categories: `Document Management | Practice Management and Billing | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Prove that output, operations, or service meet required standards before release or continued execution.
- Trigger: A production step, service checkpoint, or formal control requirement calls for inspection or compliance review.
- End outcome: The item is passed, failed, quarantined, or escalated with evidence attached to the record.
- Primary actors: quality or compliance owner; operator or frontline staff; manager; external customer or regulator
- Major decisions: Does the item meet the release threshold?; What deviation is acceptable versus requiring stop-work or escalation?; What corrective action and evidence are necessary?
- Major handoffs: operations -> quality or compliance team; quality finding -> rework or management action; released item -> downstream fulfillment or reporting
- Systems of record involved: Document Management | Practice Management and Billing | CRM

## Current-State Friction

- Where money is lost: Failures, recalls, rework, and excess inspection labor are the major leakage points.
- Where time is lost: Teams repeat data entry, collect evidence manually, and wait on disposition decisions.
- Where human judgment dominates: Inspectors still interpret severity, traceability gaps, and acceptable release decisions.
- Where people leave the system of record: Evidence often sits in attachments, lab systems, spreadsheets, and manual checklists outside the main record.

## Software Landscape

- What software exists today: Typical stacks combine Document Management, Practice Management and Billing, CRM; representative software in market today includes iManage, NetDocuments, Litera, Thomson Reuters Elite, Clio, Salesforce CRM.
- Representative vendors: iManage; NetDocuments; Litera; Thomson Reuters Elite; Clio; Salesforce CRM; Microsoft Dynamics 365 Sales; HubSpot CRM
- Why this has not been solved cleanly: Standards are formal, but real-world deviations and root-cause interpretation remain human-heavy. It typically spans 1 operating-system context and 3 systems-of-record categories.
- Primary reason: `Regulatory`

## Current Vendor Research

- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Professional Services and Matter Management`: Monetizes expert labor through pipeline management, staffing, delivery, work product, time capture, and client billing.
