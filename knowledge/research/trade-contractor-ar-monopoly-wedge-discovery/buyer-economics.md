# Buyer Economics

Last updated: 2026-08-14
Status: Active economics layer

## Assumptions

The estimates below are scenario-based, not market-wide averages.

They are intended to answer whether a buyer can justify spend on the workflow, not to estimate TAM.

## Top Candidate Workflows

| Candidate workflow | Economic buyer | Current budget owner | Direct economic harm | Why a buyer might add another product |
| --- | --- | --- | --- | --- |
| Pay-app rejection diagnosis and resubmission | Controller / AR manager | AR + project accounting | A rejected pay app can delay a six-figure receivable by a full billing cycle, disrupt cash forecasting, and force repeat admin work under cutoff pressure. | Current stack records the project; it does not own the recovery loop once the billing packet is blocked. |
| Retainage release tracking and collections | Controller / CFO | AR + finance leadership | Retainage can trap 5-10% of project billings for months after work is effectively done. | ERP mechanics exist, but visibility and follow-up still sprawl across closeout, waivers, and milestone proof. |
| SOV normalization and billing-packet setup | Billing manager | Project accounting | A bad setup creates repeat rejection risk across the whole project lifecycle. | Buyers may pay to avoid repeated first-pass errors if the implementation is fast and portal-aware. |
| Change-order-to-billing sync | PM + billing manager | PM + finance | Approved work can sit unbilled if it never makes it into the current billable line structure. | Buyers will pay if the tool reliably converts approved change into collectible billing without extra admin work. |
| Lien-waiver and notary exception handling | Controller / AR lead | AR + compliance | Missing or mistimed waivers can hold otherwise payable invoices and final closeout funds. | Buyers may add workflow help if it materially reduces payment holds without changing the ERP. |

## Concrete Economics For The Winning Wedge

### Wedge

Pay-app rejection diagnosis and resubmission.

### Buyer

- Controller
- AR manager
- Billing manager at a commercial trade contractor

### Current budget footprint

- Construction ERP or accounting system
- Billing staff time
- PM support for backup and change-order reconciliation
- Mandatory use of GC-chosen payment portals

### Why the pain is measurable

- One rejected pay app can move a receivable from this cycle to the next one.
- The same error often creates extra labor across billing, PM, and sometimes field teams.
- The cost is not only admin time. It is also working-capital stress when payroll and vendors are paid before the receivable lands.

### Example scenario

- Monthly pay app value: `$150K-$300K`
- Delay if rejected near cutoff: `2-4+ weeks` or the next billing cycle
- Labor consumed per rejection: billing manager + PM + follow-up with GC AP or PM
- Side effects:
  - cash forecast misses,
  - higher aging,
  - more collections follow-up,
  - more risk of short-term borrowing or owner-funded float.

### Why a net-new purchase is believable

- The buyer already spends money here.
- The pain is experienced by one team every month.
- Implementation can sit on top of current portals and ERP rather than replacing them.
- The value proposition is tied directly to fewer rejections and faster cash, not abstract analytics.

## Why The Winner Beats The Other Candidates

- It is more frequent than retainage release.
- It is less occupied than change-order tooling.
- It is more acute than generic billing visibility.
- It is narrow enough to implement without asking the buyer to replatform accounting.
