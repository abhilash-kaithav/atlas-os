# Asset and Investor Reporting

Last updated: 2026-08-14
Status: Active Phase 2 workflow record

## Metadata

- Workflow family: `Governance and Portfolio Operations`
- Operating systems: `Asset Utilization and Lease Management`
- Industries using this workflow: `Other real estate`
- Industry count: 1
- Systems-of-record categories: `Fund Administration and Accounting | Property Management System | Real Estate Asset Management | CRM`
- Validation status: `Complete`

## Current-State Mapping

- Objective: Maintain an accurate investment, fund, or investor record across accounting, performance, portfolio, and client-facing views.
- Trigger: A trade, valuation change, investor event, or reporting cycle requires the portfolio record to be refreshed.
- End outcome: Positions, valuations, reporting views, and investor outputs align closely enough to support action and oversight.
- Primary actors: portfolio or fund operations team; investment professional; accounting partner; investor relations or client service
- Major decisions: What portfolio, fund, or investor state is authoritative for the current action?; Which break, exception, or exposure deserves escalation?; What action should be taken before downstream reporting or client communication proceeds?
- Major handoffs: front-office activity -> middle or back office; accounting and valuation outputs -> investor reporting; exception review -> portfolio manager or leadership
- Systems of record involved: Fund Administration and Accounting | Property Management System | Real Estate Asset Management | CRM

## Current-State Friction

- Where money is lost: Leakage comes from stale positions, NAV breaks, manual reporting overhead, and slow exception closure.
- Where time is lost: Teams reconcile books and records repeatedly across portfolio, accounting, and investor-reporting systems.
- Where human judgment dominates: Materiality, valuation challenge, and client communication still depend on experienced professionals.
- Where people leave the system of record: Exception narratives and investor context move through emails, memos, and spreadsheet bridges.

## Software Landscape

- What software exists today: Typical stacks combine Fund Administration and Accounting, Property Management System, Real Estate Asset Management, CRM; representative software in market today includes Allvue Fund Accounting, Aladdin Accounting, SS&C, SimCorp, State Street Alpha, Clearwater.
- Representative vendors: Allvue Fund Accounting; Aladdin Accounting; SS&C; SimCorp; State Street Alpha; Clearwater; Yardi; RealPage
- Why this has not been solved cleanly: Even sophisticated platforms still depend on cross-book reconciliation and human review to maintain trust. It typically spans 1 operating-system context and 4 systems-of-record categories.
- Primary reason: `Technical`

## Current Vendor Research

- [Allvue Fund Accounting](https://www.allvuesystems.com/solutions/fund-accounting/)
- [Aladdin Accounting](https://www.blackrock.com/aladdin/platforms/products/aladdin-accounting)
- [Yardi](https://www.yardi.com/solution/property-management-software/)
- [Salesforce CRM](https://www.salesforce.com/crm/)
- [Microsoft Dynamics 365 Sales](https://www.microsoft.com/en-us/dynamics-365/products/sales)
- [HubSpot CRM](https://www.hubspot.com/products/crm?gh_jid=5988617)

## Atlas Context

- `Asset Utilization and Lease Management`: Monetizes owned or controlled assets through occupancy or utilization, contract terms, maintenance, turnover, and billing discipline.
