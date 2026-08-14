# Deposit and Payment Operations

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Finance and Revenue Operations`
- Operating systems: `Deposit, Credit, and Payment Intermediation`
- Industries using this workflow: `Federal Reserve banks, credit intermediation, and related activities`
- Industry count: 1
- Systems-of-record categories: `Core Banking | Loan Origination and Servicing | Payments | Risk and Compliance | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Advance credit, account, or financing decisions while balancing growth, risk, documentation, and servicing control.
- Trigger: A borrower or account relationship requires onboarding, underwriting, servicing, collections, or payment handling.
- End outcome: The credit or servicing action is completed with the record, controls, and next follow-up updated.
- Primary actors: relationship manager or lender; underwriter or analyst; borrower or account holder; servicing or collections team
- Major decisions: Is the customer or credit request acceptable under current policy and risk appetite?; What servicing, payment, or workout action is most appropriate now?; What exception deserves manual review despite automation rules?
- Major handoffs: relationship owner -> credit or onboarding review; approved account or loan -> servicing operations; risk signal -> collections, workout, or compliance team
- Systems of record involved: Core Banking | Loan Origination and Servicing | Payments | Risk and Compliance | CRM

## Current-State Friction

- Where money is lost: Leakage appears through slow decisioning, avoidable losses, poor collections, and high manual servicing cost.
- Where time is lost: Banking teams chase documents, reconcile exposures, and move work across front, middle, and back office queues.
- Where human judgment dominates: Risk appetite, borrower quality, and workout strategy still rely heavily on expert human judgment.
- Where people leave the system of record: Core context moves into credit memos, committee notes, shared spreadsheets, and email threads outside the core record.

## Software Landscape

- What software exists today: Typical stacks combine Core Banking, Loan Origination and Servicing, Payments, Risk and Compliance, and adjacent specialist systems; representative software in market today includes Temenos, Finastra Phoenix, Fiserv, FIS, Jack Henry, nCino Commercial Lending.
- Representative vendors: Temenos; Finastra Phoenix; Fiserv; FIS; Jack Henry; nCino Commercial Lending; nCino; Dealertrack
- Why this has not been solved cleanly: Core systems are mature, but cross-functional credit work remains document-heavy and policy-sensitive. It typically spans 1 operating-system context and 5 systems-of-record categories.
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
