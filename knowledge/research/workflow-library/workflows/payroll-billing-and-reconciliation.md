# Payroll, Billing, and Reconciliation

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Finance and Revenue Operations`
- Operating systems: `Workforce Coordination and Service Operations`
- Industries using this workflow: `Administrative and support services`
- Industry count: 1
- Systems-of-record categories: `CRM | ERP | HCM / Workforce Management | Service Management`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Close the loop between source activity, cash movement, and the official financial record with defensible reconciliation.
- Trigger: Transactions from multiple sources must be balanced, settled, or closed for a period or event.
- End outcome: Balances are reconciled, exceptions are documented, and the official close or settlement state is updated.
- Primary actors: accounting or settlement analyst; operations source owner; treasury or payments partner; manager or reviewer
- Major decisions: What is the authoritative source when records disagree?; Which exception can be auto-cleared versus requiring investigation?; What threshold is material enough to escalate before close?
- Major handoffs: source system -> reconciliation or settlement team; unmatched item -> operations, treasury, or counterparty; resolved balance -> reporting and management review
- Systems of record involved: CRM | ERP | HCM / Workforce Management | Service Management

## Current-State Friction

- Where money is lost: Unmatched items, late close, duplicate settlements, and poor exception control create hidden leakage and working-capital drag.
- Where time is lost: Analysts spend time matching records manually, collecting support, and rebuilding audit trails.
- Where human judgment dominates: Materiality, root cause, and acceptable resolution still depend on experienced finance staff.
- Where people leave the system of record: Exception triage almost always moves into spreadsheets, email, and bank or partner portals.

## Software Landscape

- What software exists today: Typical stacks combine CRM, ERP, HCM / Workforce Management, Service Management; representative software in market today includes Salesforce CRM, Microsoft Dynamics 365 Sales, HubSpot CRM, VTS, Cox Automotive, SAP Cloud ERP.
- Representative vendors: Salesforce CRM; Microsoft Dynamics 365 Sales; HubSpot CRM; VTS; Cox Automotive; SAP Cloud ERP; Acumatica Cloud ERP; Oracle
- Why this has not been solved cleanly: Reconciliation spans asynchronous systems and low-standardization edge cases that resist full automation. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)
- [SAP Cloud ERP](https://www.sap.com/products/erp.html?dfa=1&gad=1)
- [Acumatica Cloud ERP](https://www.acumatica.com/cloud-erp-software/)
- [Workday Workforce Management](https://forms.workday.com/en-us/quick-demos/managing-your-workforce-with-workday-demo/form.html?step=step1_default)
- [Deputy](https://www.deputy.com/)
- [Legion](https://legion.co/en-gb/products/)

## Atlas Context

- `Workforce Coordination and Service Operations`: Matches labor to demand, schedules execution, monitors service levels, and converts work into payroll and billing.
