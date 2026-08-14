# Freight Audit and Settlement

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Finance and Revenue Operations`
- Operating systems: `Transportation Network Operations`
- Industries using this workflow: `Other transportation and support activities`
- Industry count: 1
- Systems-of-record categories: `Transportation Management System | Fleet Telematics and Visibility | ERP`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Close the loop between source activity, cash movement, and the official financial record with defensible reconciliation.
- Trigger: Transactions from multiple sources must be balanced, settled, or closed for a period or event.
- End outcome: Balances are reconciled, exceptions are documented, and the official close or settlement state is updated.
- Primary actors: accounting or settlement analyst; operations source owner; treasury or payments partner; manager or reviewer
- Major decisions: What is the authoritative source when records disagree?; Which exception can be auto-cleared versus requiring investigation?; What threshold is material enough to escalate before close?
- Major handoffs: source system -> reconciliation or settlement team; unmatched item -> operations, treasury, or counterparty; resolved balance -> reporting and management review
- Systems of record involved: Transportation Management System | Fleet Telematics and Visibility | ERP

## Current-State Friction

- Where money is lost: Unmatched items, late close, duplicate settlements, and poor exception control create hidden leakage and working-capital drag.
- Where time is lost: Analysts spend time matching records manually, collecting support, and rebuilding audit trails.
- Where human judgment dominates: Materiality, root cause, and acceptable resolution still depend on experienced finance staff.
- Where people leave the system of record: Exception triage almost always moves into spreadsheets, email, and bank or partner portals.

## Software Landscape

- What software exists today: Typical stacks combine Transportation Management System, Fleet Telematics and Visibility, ERP; representative software in market today includes project44, McLeod, Oracle Transportation Management, Descartes, CargoWise, Samsara.
- Representative vendors: project44; McLeod; Oracle Transportation Management; Descartes; CargoWise; Samsara; Trimble Transportation; SAP Cloud ERP
- Why this has not been solved cleanly: Reconciliation spans asynchronous systems and low-standardization edge cases that resist full automation. It typically spans 1 operating-system context and 3 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [project44](https://www.project44.com/platform/tms/)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)

## Atlas Context

- `Transportation Network Operations`: Plans capacity, routes assets, manages exceptions, and settles transport across operating networks.
