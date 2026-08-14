# Client Onboarding and KYC

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Access, Intake, and Contracting`
- Operating systems: `Capital Markets and Investment Management`
- Industries using this workflow: `Securities, commodity contracts, and investments`
- Industry count: 1
- Systems-of-record categories: `Investor Reporting and Performance | Portfolio and Order Management | Trading and Market Data | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Stand up a new account, relationship, or fund record while satisfying verification, risk, and setup requirements.
- Trigger: A new customer, borrower, investor, or fund relationship is approved for activation.
- End outcome: The relationship is activated in the necessary systems with required checks, documents, and controls completed.
- Primary actors: onboarding specialist; customer or counterparty; risk or compliance reviewer; operations setup team
- Major decisions: Is the relationship verified enough to activate?; What documentation or control gap still blocks go-live?; Which setup path fits the relationship complexity and risk level?
- Major handoffs: sales or relationship owner -> onboarding team; onboarding -> risk, compliance, or legal review; approved setup -> servicing or operations team
- Systems of record involved: Investor Reporting and Performance | Portfolio and Order Management | Trading and Market Data | CRM

## Current-State Friction

- Where money is lost: Slow onboarding delays revenue start dates and increases abandonment, while weak controls raise risk and rework.
- Where time is lost: Teams chase documents, approvals, signatures, and duplicate data entry across systems.
- Where human judgment dominates: Analysts still judge risk, beneficial ownership complexity, and what counts as a satisfactory exception path.
- Where people leave the system of record: Onboarding packets, emails, shared checklists, and external verification portals carry the real process state.

## Software Landscape

- What software exists today: Typical stacks combine Investor Reporting and Performance, Portfolio and Order Management, Trading and Market Data, CRM; representative software in market today includes Aladdin, SS&C Advent, Clearwater, State Street Alpha, Charles River, SimCorp.
- Representative vendors: Aladdin; SS&C Advent; Clearwater; State Street Alpha; Charles River; SimCorp; Bloomberg; Salesforce CRM
- Why this has not been solved cleanly: Verification is partly automatable, but high-value or high-risk relationships still require context-heavy review and layered approvals. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Regulatory`

## Current Vendor Research

- [Aladdin](https://www.blackrock.com/institutions/en-us/investment-capabilities/technolgy/aladdin-portfolio-management-software)
- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Capital Markets and Investment Management`: Manages portfolios, trades, valuation, reporting, and compliance for entrusted capital.
