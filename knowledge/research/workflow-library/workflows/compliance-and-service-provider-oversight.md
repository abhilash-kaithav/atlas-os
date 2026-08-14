# Compliance and Service-Provider Oversight

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Risk, Compliance, and Reporting`
- Operating systems: `Capital Markets and Investment Management`
- Industries using this workflow: `Funds, trusts, and other financial vehicles`
- Industry count: 1
- Systems-of-record categories: `Fund Administration and Accounting | Investor Reporting and Performance | Portfolio and Order Management | Reconciliation and Reporting`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Produce a compliant, decision-useful record of activity while ensuring the supporting evidence can stand up to review.
- Trigger: A formal period close, audit, regulatory filing, or quality checkpoint requires documented output.
- End outcome: The report or compliance record is submitted with evidence, exceptions, and ownership clearly documented.
- Primary actors: reporting or compliance analyst; source operations owner; manager or approver; external reviewer
- Major decisions: What source should be treated as authoritative for this report?; Which exception is material enough to disclose or remediate?; What evidence is sufficient to sign off the output?
- Major handoffs: source teams -> reporting or compliance owner; prepared output -> reviewer, auditor, or regulator; findings -> remediation owner
- Systems of record involved: Fund Administration and Accounting | Investor Reporting and Performance | Portfolio and Order Management | Reconciliation and Reporting

## Current-State Friction

- Where money is lost: Late or weak reporting creates fines, reserve exposure, rework, and management blind spots.
- Where time is lost: Teams manually stitch files, request attestations, and chase evidence for every cycle.
- Where human judgment dominates: Control owners still decide what is material, what is remediated, and what can be tolerated temporarily.
- Where people leave the system of record: Supporting evidence sits in attachments, spreadsheets, emails, and external filing systems.

## Software Landscape

- What software exists today: Typical stacks combine Fund Administration and Accounting, Investor Reporting and Performance, Portfolio and Order Management, Reconciliation and Reporting; representative software in market today includes Allvue Fund Accounting, Aladdin Accounting, SS&C, SimCorp, State Street Alpha, Clearwater.
- Representative vendors: Allvue Fund Accounting; Aladdin Accounting; SS&C; SimCorp; State Street Alpha; Clearwater; Aladdin; SS&C Advent
- Why this has not been solved cleanly: The form of the report may be standardized, but the data lineage and exception handling still are not. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Regulatory`

## Current Vendor Research

- [Allvue Fund Accounting](https://www.allvuesystems.com/solutions/fund-accounting/)
- [Aladdin Accounting](https://www.blackrock.com/aladdin/platforms/products/aladdin-accounting)
- [Aladdin](https://www.blackrock.com/institutions/en-us/investment-capabilities/technolgy/aladdin-portfolio-management-software)

## Atlas Context

- `Capital Markets and Investment Management`: Manages portfolios, trades, valuation, reporting, and compliance for entrusted capital.
