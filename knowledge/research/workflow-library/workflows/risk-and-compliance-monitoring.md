# Risk and Compliance Monitoring

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Risk, Compliance, and Reporting`
- Operating systems: `Deposit, Credit, and Payment Intermediation`
- Industries using this workflow: `Federal Reserve banks, credit intermediation, and related activities`
- Industry count: 1
- Systems-of-record categories: `Core Banking | Loan Origination and Servicing | Payments | Risk and Compliance | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Produce a compliant, decision-useful record of activity while ensuring the supporting evidence can stand up to review.
- Trigger: A formal period close, audit, regulatory filing, or quality checkpoint requires documented output.
- End outcome: The report or compliance record is submitted with evidence, exceptions, and ownership clearly documented.
- Primary actors: reporting or compliance analyst; source operations owner; manager or approver; external reviewer
- Major decisions: What source should be treated as authoritative for this report?; Which exception is material enough to disclose or remediate?; What evidence is sufficient to sign off the output?
- Major handoffs: source teams -> reporting or compliance owner; prepared output -> reviewer, auditor, or regulator; findings -> remediation owner
- Systems of record involved: Core Banking | Loan Origination and Servicing | Payments | Risk and Compliance | CRM

## Current-State Friction

- Where money is lost: Late or weak reporting creates fines, reserve exposure, rework, and management blind spots.
- Where time is lost: Teams manually stitch files, request attestations, and chase evidence for every cycle.
- Where human judgment dominates: Control owners still decide what is material, what is remediated, and what can be tolerated temporarily.
- Where people leave the system of record: Supporting evidence sits in attachments, spreadsheets, emails, and external filing systems.

## Software Landscape

- What software exists today: Typical stacks combine Core Banking, Loan Origination and Servicing, Payments, Risk and Compliance, and adjacent specialist systems; representative software in market today includes Temenos, Finastra Phoenix, Fiserv, FIS, Jack Henry, nCino Commercial Lending.
- Representative vendors: Temenos; Finastra Phoenix; Fiserv; FIS; Jack Henry; nCino Commercial Lending; nCino; Dealertrack
- Why this has not been solved cleanly: The form of the report may be standardized, but the data lineage and exception handling still are not. It typically spans 1 operating-system context and 5 systems-of-record categories.
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
