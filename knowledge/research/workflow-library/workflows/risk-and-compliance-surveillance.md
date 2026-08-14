# Risk and Compliance Surveillance

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Risk, Compliance, and Reporting`
- Operating systems: `Capital Markets and Investment Management`
- Industries using this workflow: `Securities, commodity contracts, and investments`
- Industry count: 1
- Systems-of-record categories: `Investor Reporting and Performance | Portfolio and Order Management | Trading and Market Data | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Produce a compliant, decision-useful record of activity while ensuring the supporting evidence can stand up to review.
- Trigger: A formal period close, audit, regulatory filing, or quality checkpoint requires documented output.
- End outcome: The report or compliance record is submitted with evidence, exceptions, and ownership clearly documented.
- Primary actors: reporting or compliance analyst; source operations owner; manager or approver; external reviewer
- Major decisions: What source should be treated as authoritative for this report?; Which exception is material enough to disclose or remediate?; What evidence is sufficient to sign off the output?
- Major handoffs: source teams -> reporting or compliance owner; prepared output -> reviewer, auditor, or regulator; findings -> remediation owner
- Systems of record involved: Investor Reporting and Performance | Portfolio and Order Management | Trading and Market Data | CRM

## Current-State Friction

- Where money is lost: Late or weak reporting creates fines, reserve exposure, rework, and management blind spots.
- Where time is lost: Teams manually stitch files, request attestations, and chase evidence for every cycle.
- Where human judgment dominates: Control owners still decide what is material, what is remediated, and what can be tolerated temporarily.
- Where people leave the system of record: Supporting evidence sits in attachments, spreadsheets, emails, and external filing systems.

## Software Landscape

- What software exists today: Typical stacks combine Investor Reporting and Performance, Portfolio and Order Management, Trading and Market Data, CRM; representative software in market today includes Aladdin, SS&C Advent, Clearwater, State Street Alpha, Charles River, SimCorp.
- Representative vendors: Aladdin; SS&C Advent; Clearwater; State Street Alpha; Charles River; SimCorp; Bloomberg; Salesforce CRM
- Why this has not been solved cleanly: The form of the report may be standardized, but the data lineage and exception handling still are not. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Regulatory`

## Current Vendor Research

- [Aladdin](https://www.blackrock.com/institutions/en-us/investment-capabilities/technolgy/aladdin-portfolio-management-software)
- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Capital Markets and Investment Management`: Manages portfolios, trades, valuation, reporting, and compliance for entrusted capital.
