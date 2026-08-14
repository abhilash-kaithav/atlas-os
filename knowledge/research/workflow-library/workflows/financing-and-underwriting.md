# Financing and Underwriting

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Finance and Revenue Operations`
- Operating systems: `Retail and Service Commerce`
- Industries using this workflow: `Motor vehicle and parts dealers`
- Industry count: 1
- Systems-of-record categories: `Loan Origination and Servicing | Maintenance Management | Dealership Management System | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Advance credit, account, or financing decisions while balancing growth, risk, documentation, and servicing control.
- Trigger: A borrower or account relationship requires onboarding, underwriting, servicing, collections, or payment handling.
- End outcome: The credit or servicing action is completed with the record, controls, and next follow-up updated.
- Primary actors: relationship manager or lender; underwriter or analyst; borrower or account holder; servicing or collections team
- Major decisions: Is the customer or credit request acceptable under current policy and risk appetite?; What servicing, payment, or workout action is most appropriate now?; What exception deserves manual review despite automation rules?
- Major handoffs: relationship owner -> credit or onboarding review; approved account or loan -> servicing operations; risk signal -> collections, workout, or compliance team
- Systems of record involved: Loan Origination and Servicing | Maintenance Management | Dealership Management System | CRM

## Current-State Friction

- Where money is lost: Leakage appears through slow decisioning, avoidable losses, poor collections, and high manual servicing cost.
- Where time is lost: Banking teams chase documents, reconcile exposures, and move work across front, middle, and back office queues.
- Where human judgment dominates: Risk appetite, borrower quality, and workout strategy still rely heavily on expert human judgment.
- Where people leave the system of record: Core context moves into credit memos, committee notes, shared spreadsheets, and email threads outside the core record.

## Software Landscape

- What software exists today: Typical stacks combine Loan Origination and Servicing, Maintenance Management, Dealership Management System, CRM; representative software in market today includes nCino Commercial Lending, nCino, Temenos, Dealertrack, IFS Enterprise Asset Management, Yardi.
- Representative vendors: nCino Commercial Lending; nCino; Temenos; Dealertrack; IFS Enterprise Asset Management; Yardi; ServiceTitan; Oracle Utilities
- Why this has not been solved cleanly: Core systems are mature, but cross-functional credit work remains document-heavy and policy-sensitive. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Regulatory`

## Current Vendor Research

- [nCino Commercial Lending](https://www.ncino.com/solutions/commercial-lending?nxtPslug=commercial-loan-origination-system)
- [IFS Enterprise Asset Management](https://www.ifs.com/en/products/alm/eam)
- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Retail and Service Commerce`: Monetizes traffic, assortment, transactions, service execution, labor, and repeat demand across commerce channels.
