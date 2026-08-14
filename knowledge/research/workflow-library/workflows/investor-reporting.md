# Investor Reporting

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Governance and Portfolio Operations`
- Operating systems: `Capital Markets and Investment Management`
- Industries using this workflow: `Funds, trusts, and other financial vehicles`
- Industry count: 1
- Systems-of-record categories: `Fund Administration and Accounting | Investor Reporting and Performance | Portfolio and Order Management | Reconciliation and Reporting`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Maintain an accurate investment, fund, or investor record across accounting, performance, portfolio, and client-facing views.
- Trigger: A trade, valuation change, investor event, or reporting cycle requires the portfolio record to be refreshed.
- End outcome: Positions, valuations, reporting views, and investor outputs align closely enough to support action and oversight.
- Primary actors: portfolio or fund operations team; investment professional; accounting partner; investor relations or client service
- Major decisions: What portfolio, fund, or investor state is authoritative for the current action?; Which break, exception, or exposure deserves escalation?; What action should be taken before downstream reporting or client communication proceeds?
- Major handoffs: front-office activity -> middle or back office; accounting and valuation outputs -> investor reporting; exception review -> portfolio manager or leadership
- Systems of record involved: Fund Administration and Accounting | Investor Reporting and Performance | Portfolio and Order Management | Reconciliation and Reporting

## Current-State Friction

- Where money is lost: Leakage comes from stale positions, NAV breaks, manual reporting overhead, and slow exception closure.
- Where time is lost: Teams reconcile books and records repeatedly across portfolio, accounting, and investor-reporting systems.
- Where human judgment dominates: Materiality, valuation challenge, and client communication still depend on experienced professionals.
- Where people leave the system of record: Exception narratives and investor context move through emails, memos, and spreadsheet bridges.

## Software Landscape

- What software exists today: Typical stacks combine Fund Administration and Accounting, Investor Reporting and Performance, Portfolio and Order Management, Reconciliation and Reporting; representative software in market today includes Allvue Fund Accounting, Aladdin Accounting, SS&C, SimCorp, State Street Alpha, Clearwater.
- Representative vendors: Allvue Fund Accounting; Aladdin Accounting; SS&C; SimCorp; State Street Alpha; Clearwater; Aladdin; SS&C Advent
- Why this has not been solved cleanly: Even sophisticated platforms still depend on cross-book reconciliation and human review to maintain trust. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Technical`

## Current Vendor Research

- [Allvue Fund Accounting](https://www.allvuesystems.com/solutions/fund-accounting/)
- [Aladdin Accounting](https://www.blackrock.com/aladdin/platforms/products/aladdin-accounting)
- [Aladdin](https://www.blackrock.com/institutions/en-us/investment-capabilities/technolgy/aladdin-portfolio-management-software)

## Atlas Context

- `Capital Markets and Investment Management`: Manages portfolios, trades, valuation, reporting, and compliance for entrusted capital.
