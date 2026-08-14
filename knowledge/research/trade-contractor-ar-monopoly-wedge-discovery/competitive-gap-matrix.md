# Competitive Gap Matrix

Last updated: 2026-08-14
Status: Active market layer

## How To Read This Matrix

- `Direct`: purpose-built for the workflow from the subcontractor side.
- `Partial`: covers part of the workflow or only the GC/payor side.
- `Adjacent`: supports the process but is not the workflow owner.

## High-Pain Workflow Comparison

| Workflow | Existing products | Adoption level | Customer sentiment | What current tools solve well | What they still do not solve cleanly | What customers still do outside software |
| --- | --- | --- | --- | --- | --- | --- |
| SOV line build and billing-template normalization | [Siteline](https://www.g2.com/sellers/siteline) `Direct`; [GCPay](https://www.g2.com/products/gcpay/reviews) `Partial`; [Procore Pay](https://www.procore.com/pay) `Partial`; [Autodesk Build + GCPay](https://www.autodesk.com/blogs/construction/autodesk-forma-build-gcpay-a-new-integration-connecting-field-and-finance-is-here/) `Partial`; ERP stack `Adjacent` | Moderate direct-tool adoption; high incumbent adoption | Positive on digitization, but mixed on setup friction | Centralized packet creation, basic pay-app digitization, GC-facing visibility | Neutral subcontractor-side normalization across many GC billing styles | Manual SOV entry, Excel-based line mapping, phone or email clarification of project-specific requirements |
| Approved change-order sync into billable lines | [Clearstory](https://www.g2.com/products/clearstory/reviews) `Direct`; Procore `Partial`; Autodesk Cost `Partial`; Siteline `Partial` | Rising direct-tool adoption | Strong for dedicated change-order tools | Change-order logs, visibility, time-and-material tags, status tracking | Guaranteed downstream translation of approved change orders into the current pay app for the subcontractor | Separate Excel logs, re-uploaded files, side-by-side review against billing sheets |
| Waiver and notary packet preparation | GCPay `Partial`; Procore Pay `Partial`; Textura-class workflows `Partial`; Sage and Vista `Adjacent` | High in GC-side workflows; lower in neutral sub-side tools | Mixed; useful but still frustrating | Conditional and unconditional waiver exchange, compliance gating, payment controls | Smooth subcontractor-side correction flow when waiver timing, form choice, or notary availability breaks the packet | Manual notary sequencing, printing or restamping, waiting to re-log into portals, separate waiver edits |
| Rejection diagnosis and resubmission | Siteline `Direct but broad`; GCPay `Partial`; Procore Pay `Partial`; Autodesk Build + GCPay `Partial`; Sage/Vista `Adjacent`; [Scaftra](https://scaftra.com/features/pay-applications/) `Direct but early-stage` | High incumbent presence, low clear category ownership | Repeated complaints around unclear statuses, inability to self-correct, and cross-tool friction | Audit trail, checklist visibility, portal submission, some workflow status | A neutral exception desk that tells the subcontractor exactly what failed, why it failed, and what corrected packet to send next | Calling the GC, rebuilding in Excel or PDF, tracking blockers in spreadsheets, resubmitting manually |
| Payment-status tracking and collections follow-up | [Siteline](https://www.g2.com/sellers/siteline) `Direct`; [Cotillo](https://cotillo.io/) `Direct`; ERP aging tools `Partial` | Direct adoption still emerging; ERP adoption high | Clear value, but public practitioner evidence is still thinner than for billing errors | Aging views, GC payment-pattern reporting, reminders, collections tasks | Hard linkage between packet exception history and the reason cash is still delayed | Separate aging notes, email chase logs, portal logins, controller-side cash forecasting outside the billing tool |
| Retainage release and closeout packet | Siteline `Direct`; Cotillo `Direct`; Vista/Sage/Spectrum `Partial`; Procore `Partial` | Moderate direct-tool adoption; entrenched ERP presence | Pain is obvious and economically severe | Mechanical retainage tracking, some release workflows, final billing support | A narrow, high-urgency release workflow that closes the loop on final waivers, milestone proof, and release timing from the sub side | Retainage spreadsheets, closeout punch lists, manual release calendars, repeated follow-up calls |

## Takeaway

The clean-path market is not empty.

The best opening appears where:

- a trade contractor already has software,
- the GC already has software,
- and the subcontractor still has to run a manual exception desk whenever the pay app is blocked.
