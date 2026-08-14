# Atomic Workflow Map

Last updated: 2026-08-14
Status: Active decomposition layer

## Scope

This map decomposes commercial trade-contractor AR into the smallest workflows that still have a clear owner and output.

## Atomic Steps

| ID | Phase | Atomic workflow | Primary owner | Main systems touched | Why this is atomic |
| --- | --- | --- | --- | --- | --- |
| 1 | Setup | Contract billing-requirement intake | Project accountant | Contract PDF, email, ERP notes | Someone must interpret billing rules before any packet can be built. |
| 2 | Setup | GC portal onboarding and permissions setup | Billing coordinator | GC portal, email, identity tools | Portal access is a distinct gate before billing work can start. |
| 3 | Setup | Billing calendar and cutoff tracking | AR lead | Spreadsheet, calendar, GC notices | Billing deadlines are tracked separately from invoice math. |
| 4 | Setup | Schedule-of-values line build | Project accountant | Excel, portal, ERP | The SOV structure must exist before any monthly billing can roll forward. |
| 5 | Setup | Internal cost-code to SOV mapping | Project accountant | ERP, job cost, Excel | Internal job-cost structure rarely matches the GC-facing SOV automatically. |
| 6 | Pre-bill | Approved change-order sync into billable lines | PM + billing | Change-order log, portal, ERP | Approved COs must be turned into billable SOV changes before invoicing. |
| 7 | Pre-bill | Pending change-order hold tracking | PM + AR | Change-order log, notes, email | Pending CO value must be tracked separately from approved billable value. |
| 8 | Pre-bill | Percent-complete capture from field or PM | PM | PM system, field notes, Excel | Someone must decide what work is actually billable this period. |
| 9 | Pre-bill | Stored-material and backup collection | Project engineer | Folder system, email, portal | Backup packet assembly is a distinct document-gathering step. |
| 10 | Pre-bill | Pay-app rollforward math | Billing manager | Excel, ERP, portal | Prior billed, current billed, retainage, and to-date amounts must reconcile. |
| 11 | Pre-bill | Conditional waiver drafting | AR / legal ops | Waiver templates, PDF, portal | Waiver generation has its own legal form and amount logic. |
| 12 | Pre-bill | Notary and signature collection | AR / signer | Notary tool, PDF, portal | Signature and notarization timing is separate from packet creation. |
| 13 | Pre-bill | Compliance requirement check | AR / admin | COI tracker, portal, ERP | Expired compliance can block payment even when the bill is otherwise correct. |
| 14 | Pre-bill | GC-specific packet assembly | Billing manager | Excel, PDF, portal, e-sign | Each GC's packet can require a different final package shape. |
| 15 | Submission | Submission into portal, email, or owner form | Billing manager | Portal or email | Submission is its own workflow boundary with its own failure modes. |
| 16 | Exception loop | Rejection reason intake | AR / billing | Portal status, email, phone | Someone must determine why the packet was held or rejected. |
| 17 | Exception loop | Correction and resubmission | Billing manager | Excel, portal, PDF, phone | The rejected packet must be rebuilt and resubmitted before cutoff. |
| 18 | Post-submit | Payment-status tracking and collections follow-up | AR lead | Aging report, email, portal, phone | Once submitted, someone still has to chase status and next action. |
| 19 | Cash receipt | Cash application and unconditional waiver release | AR / controller | ERP, bank, waiver tools | Payment receipt and post-payment waiver release are separate from invoicing. |
| 20 | Closeout | Retainage release and final closeout packet | Controller / AR | ERP, closeout docs, portal | Final retainage requires its own packet, logic, and collection effort. |

## Observations

- The workflow is not one monolith. It is a chain of separate choke points.
- The highest-friction steps cluster around translation and correction, not basic invoice posting.
- The clean-path systems are already present. The gaps appear where trade contractors must adapt to each GC's rules and recover from billing exceptions.
