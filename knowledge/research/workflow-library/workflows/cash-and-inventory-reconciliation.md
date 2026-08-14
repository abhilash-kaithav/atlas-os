# Cash and Inventory Reconciliation

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Finance and Revenue Operations`
- Operating systems: `Retail and Service Commerce`
- Industries using this workflow: `Food services and drinking places`
- Industry count: 1
- Systems-of-record categories: `POS and Payments | Restaurant Back Office and Inventory | HCM / Workforce Management`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Close the loop between source activity, cash movement, and the official financial record with defensible reconciliation.
- Trigger: Transactions from multiple sources must be balanced, settled, or closed for a period or event.
- End outcome: Balances are reconciled, exceptions are documented, and the official close or settlement state is updated.
- Primary actors: accounting or settlement analyst; operations source owner; treasury or payments partner; manager or reviewer
- Major decisions: What is the authoritative source when records disagree?; Which exception can be auto-cleared versus requiring investigation?; What threshold is material enough to escalate before close?
- Major handoffs: source system -> reconciliation or settlement team; unmatched item -> operations, treasury, or counterparty; resolved balance -> reporting and management review
- Systems of record involved: POS and Payments | Restaurant Back Office and Inventory | HCM / Workforce Management

## Current-State Friction

- Where money is lost: Unmatched items, late close, duplicate settlements, and poor exception control create hidden leakage and working-capital drag.
- Where time is lost: Analysts spend time matching records manually, collecting support, and rebuilding audit trails.
- Where human judgment dominates: Materiality, root cause, and acceptable resolution still depend on experienced finance staff.
- Where people leave the system of record: Exception triage almost always moves into spreadsheets, email, and bank or partner portals.

## Software Landscape

- What software exists today: Typical stacks combine POS and Payments, Restaurant Back Office and Inventory, HCM / Workforce Management; representative software in market today includes Toast POS, Square, Oracle MICROS, NCR Voyix, PAR Technology, Workday Workforce Management.
- Representative vendors: Toast POS; Square; Oracle MICROS; NCR Voyix; PAR Technology; Workday Workforce Management; Deputy; Legion
- Why this has not been solved cleanly: Reconciliation spans asynchronous systems and low-standardization edge cases that resist full automation. It typically spans 1 operating-system context and 3 systems-of-record categories.
- Primary reason: `Legacy Architecture`

## Current Vendor Research

- [Toast POS](https://pos.toasttab.com/products/point-of-sale)
- [Workday Workforce Management](https://forms.workday.com/en-us/quick-demos/managing-your-workforce-with-workday-demo/form.html?step=step1_default)
- [Deputy](https://www.deputy.com/)
- [Legion](https://legion.co/en-gb/products/)

## Atlas Context

- `Retail and Service Commerce`: Monetizes traffic, assortment, transactions, service execution, labor, and repeat demand across commerce channels.
