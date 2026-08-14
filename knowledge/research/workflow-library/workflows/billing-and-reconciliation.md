# Billing and Reconciliation

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Finance and Revenue Operations`
- Operating systems: `Asset Utilization and Lease Management`
- Industries using this workflow: `Other real estate`
- Industry count: 1
- Systems-of-record categories: `Fund Administration and Accounting | Property Management System | Real Estate Asset Management | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Close the loop between source activity, cash movement, and the official financial record with defensible reconciliation.
- Trigger: Transactions from multiple sources must be balanced, settled, or closed for a period or event.
- End outcome: Balances are reconciled, exceptions are documented, and the official close or settlement state is updated.
- Primary actors: accounting or settlement analyst; operations source owner; treasury or payments partner; manager or reviewer
- Major decisions: What is the authoritative source when records disagree?; Which exception can be auto-cleared versus requiring investigation?; What threshold is material enough to escalate before close?
- Major handoffs: source system -> reconciliation or settlement team; unmatched item -> operations, treasury, or counterparty; resolved balance -> reporting and management review
- Systems of record involved: Fund Administration and Accounting | Property Management System | Real Estate Asset Management | CRM

## Current-State Friction

- Where money is lost: Unmatched items, late close, duplicate settlements, and poor exception control create hidden leakage and working-capital drag.
- Where time is lost: Analysts spend time matching records manually, collecting support, and rebuilding audit trails.
- Where human judgment dominates: Materiality, root cause, and acceptable resolution still depend on experienced finance staff.
- Where people leave the system of record: Exception triage almost always moves into spreadsheets, email, and bank or partner portals.

## Software Landscape

- What software exists today: Typical stacks combine Fund Administration and Accounting, Property Management System, Real Estate Asset Management, CRM; representative software in market today includes Allvue Fund Accounting, Aladdin Accounting, SS&C, SimCorp, State Street Alpha, Clearwater.
- Representative vendors: Allvue Fund Accounting; Aladdin Accounting; SS&C; SimCorp; State Street Alpha; Clearwater; Yardi; RealPage
- Why this has not been solved cleanly: Reconciliation spans asynchronous systems and low-standardization edge cases that resist full automation. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [Allvue Fund Accounting](https://www.allvuesystems.com/solutions/fund-accounting/)
- [Aladdin Accounting](https://www.blackrock.com/aladdin/platforms/products/aladdin-accounting)
- [Yardi](https://www.yardi.com/solution/property-management-software/)
- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Asset Utilization and Lease Management`: Monetizes owned or controlled assets through occupancy or utilization, contract terms, maintenance, turnover, and billing discipline.
