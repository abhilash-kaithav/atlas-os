# Account and Loan Onboarding

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Access, Intake, and Contracting`
- Operating systems: `Deposit, Credit, and Payment Intermediation`
- Industries using this workflow: `Federal Reserve banks, credit intermediation, and related activities`
- Industry count: 1
- Systems-of-record categories: `Core Banking | Loan Origination and Servicing | Payments | Risk and Compliance | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Stand up a new account, relationship, or fund record while satisfying verification, risk, and setup requirements.
- Trigger: A new customer, borrower, investor, or fund relationship is approved for activation.
- End outcome: The relationship is activated in the necessary systems with required checks, documents, and controls completed.
- Primary actors: onboarding specialist; customer or counterparty; risk or compliance reviewer; operations setup team
- Major decisions: Is the relationship verified enough to activate?; What documentation or control gap still blocks go-live?; Which setup path fits the relationship complexity and risk level?
- Major handoffs: sales or relationship owner -> onboarding team; onboarding -> risk, compliance, or legal review; approved setup -> servicing or operations team
- Systems of record involved: Core Banking | Loan Origination and Servicing | Payments | Risk and Compliance | CRM

## Current-State Friction

- Where money is lost: Slow onboarding delays revenue start dates and increases abandonment, while weak controls raise risk and rework.
- Where time is lost: Teams chase documents, approvals, signatures, and duplicate data entry across systems.
- Where human judgment dominates: Analysts still judge risk, beneficial ownership complexity, and what counts as a satisfactory exception path.
- Where people leave the system of record: Onboarding packets, emails, shared checklists, and external verification portals carry the real process state.

## Software Landscape

- What software exists today: Typical stacks combine Core Banking, Loan Origination and Servicing, Payments, Risk and Compliance, and adjacent specialist systems; representative software in market today includes Temenos, Finastra Phoenix, Fiserv, FIS, Jack Henry, nCino Commercial Lending.
- Representative vendors: Temenos; Finastra Phoenix; Fiserv; FIS; Jack Henry; nCino Commercial Lending; nCino; Dealertrack
- Why this has not been solved cleanly: Verification is partly automatable, but high-value or high-risk relationships still require context-heavy review and layered approvals. It typically spans 1 operating-system context and 5 systems-of-record categories.
- Primary reason: `Regulatory`

## Current Vendor Research

- [Temenos](https://www.temenos.com/)
- [Finastra Phoenix](https://www.finastra.com/us-mid-market/solutions/phoenix-banking-core)
- [nCino Commercial Lending](https://www.ncino.com/solutions/commercial-lending?nxtPslug=commercial-loan-origination-system)
- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Deposit, Credit, and Payment Intermediation`: Grows and services deposits and credit while managing payments, losses, exceptions, and regulation.
