# Customer Voice Repository

Last updated: 2026-08-14
Status: Active practitioner evidence layer

## Rules Used

- Practitioner evidence outranks vendor claims.
- Only recurring signals were kept.
- Marketing pages were excluded from this file.

## Practitioner Evidence

| Source | Practitioner role | Date or review window | Workflow(s) implicated | Recurrent complaint | Manual workaround or outside-system behavior |
| --- | --- | --- | --- | --- | --- |
| [GCPay Reviews | G2](https://www.g2.com/products/gcpay/reviews) | Accounting specialist, accounting manager, AR user, operations manager, subcontractor admin | Reviews dated 2026-02-19 to 2026-05-05; page reviewed 2026-08-14 | SOV setup, waivers, rejection handling, status tracking | Users report manual SOV entry, unclear statuses or error messages, awkward waiver flow, premature waiver triggers, and no easy subcontractor-side way to reject and fix an invoice without calling the GC. | Calls to the GC, extra email, manual SOV entry, waiting for notary or waiver events before logging back in and resubmitting. |
| [Procore Reviews | G2](https://www.g2.com/products/procore/reviews) | Project coordinator | Review dated 2026-04-16; page reviewed 2026-08-14 | Change-order reconciliation, advanced billing tracking | Advanced tracking across commitments, change orders, and bill-of-material updates still requires re-uploading the same Excel file in multiple tools. | Duplicate Excel uploads and external tracking. |
| [Autodesk Forma Reviews | G2](https://www.g2.com/products/autodesk-forma-formerly-autodesk-construction-cloud/reviews) | Vice president of construction | Review dated 2026-04-08; page reviewed 2026-08-14 | Subcontractor billing workflow adoption | Subcontractors must still learn each GC's process inside the system, which makes onboarding and billing consistency difficult. | Human training and process memorization by GC. |
| [Smartsheet construction workflow thread](https://community.smartsheet.com/discussion/92913/construction-contract-work-flow-best-practices) | Construction operations practitioners | Community page reviewed 2026-08-14 | Change orders, draw status, invoicing, lien waivers | Practitioners still use VLOOKUP-heavy grids to track change orders, draw status, invoicing, and waivers. | Spreadsheet master tracker outside the core stack. |
| [Sage ACH payments and lien waivers thread](https://communityhub.sage.com/us/sage_construction_and_real_estate/f/sage-300-construction-and-real-estate/161870/ach-payments-and-lien-waivers) | Construction accounting users | Thread active over multiple years; page reviewed 2026-08-14 | Conditional vs unconditional waivers, ACH flow | Users describe too much volume to create conditional waivers manually and note that GCPay still required workarounds and exposed design faults. | Manual waiver creation or add-on tools such as MyAssistant or GCPay. |
| [Sage AP lien waivers include credit memos thread](https://communityhub.sage.com/us/sage_construction_and_real_estate/f/sage-300-construction-and-real-estate/124514/ap-lien-waivers-to-include-credit-memos) | AP clerk / Sage users | Thread reviewed 2026-08-14 | Lien waiver correction | Standard waiver output misses credit memo logic, forcing manual recreation after each check run. | Manual editing after every run. |
| [Sage automated waiver transmission thread](https://communityhub.sage.com/us/sage_construction_and_real_estate/f/sage-300-construction-and-real-estate/231871/automated-waiver-transmission) | Sage CRE accounting users | Thread reviewed 2026-08-14 | Waiver delivery | Users ask for an automated waiver-send process because the standard flow does not cover it well enough. | Third-party automation or MyAssistant. |
| [Sage 300 CRE Reviews | G2](https://www.g2.com/products/sage-300-construction-and-real-estate/reviews) | Controller, project admin, finance users | Reviews dated 2023-05-19 to 2025-07-17; page reviewed 2026-08-14 | Reporting, billing visibility, integration | Users say reports are difficult to export cleanly, require significant manipulation in Excel, and often require consultants or outside help. | ODBC, Excel manipulation, custom reports, external reporting. |
| [Vista Reviews | G2](https://www.g2.com/products/trimble-vista/reviews) | Project controller, controller, AP users | Reviews dated 2020-10-29 to 2025-02-07; page reviewed 2026-08-14 | Change-order flow, reports, subcontractor accounting | Users say some processes remain complicated, reporting gets messy across departments, and custom report changes cost more. Another user explicitly says Vista works well with GCPay, implying the ERP alone is not enough for the payment workflow. | Custom reports, add-on tools, GCPay alongside Vista. |
| [Spectrum Reviews | G2](https://www.g2.com/products/trimble-spectrum/reviews) | Project logistics manager | Review dated 2026-05-06; page reviewed 2026-08-14 | Retainage tracking | Users praise easier retainage visibility than prior systems, which confirms retainage is a distinct and painful workflow surface. | Prior manual or weaker-system retention tracking. |
| [Clearstory Reviews | G2](https://www.g2.com/products/clearstory/reviews) | Project engineer, PMs, executive PMs | Reviews dated 2023-08-09 to 2026-02-13; page reviewed 2026-08-14 | Change-order communication | Users say the platform replaced email-based change-order tracking and lost paper tags, showing that this wedge is already directly recognized and digitized. | Historically email, paper tags, and manual logs; now increasingly direct software. |
| [Tara Cristel podcast transcript](https://podscan.fm/podcasts/bred-to-build-construction-podcast/episodes/ep-53-a-200-day-pay-app-nightmare-amp-financing-gcs-w-tara-cristel) | Commercial glazing subcontractor owner | Episode published 2026-05-05; page reviewed 2026-08-14 | Payment delay, retainage, waiver conditions | A small sub describes a 200-day pay-app delay, being forced to front nearly $500,000 of materials, and still not receiving payment or retainage. | Contract digging, lien filing, manual collections pressure. |
| [Tara Cristel LinkedIn post](https://www.linkedin.com/posts/tara-cristel-5364ba244_thesubcontractorproject-activity-7445067897263185920-xlOe) | Commercial subcontractor operator | Post reviewed 2026-08-14 | Payment release conditions, vendor waivers | Practitioner describes having already paid $313,000, with $77,000 still outstanding, while being told to pay vendors and produce signed waivers before payment release. | Manual vendor proof gathering and cash bridge financing. |
| [Jadon Farris LinkedIn post](https://www.linkedin.com/posts/jadon-farris-8ba452185_a-subcontractor-can-do-everything-right-and-activity-7440518560386461697-Bn4M) | Construction practitioner | Post reviewed 2026-08-14 | Wrong form, missed deadline, new portal rule | Practitioner says subs can do the work correctly and still wait because a lien waiver is missing, a portal requirement changed, or the pay app went in on the wrong form. | Chasing, follow-up, and deadline recovery outside the system. |

## Pattern

The strongest recurring signal is not "we need another ERP."

It is:

- every GC has different billing rules,
- current software helps the clean path,
- when the packet is blocked, the sub still has to diagnose the blocker and recover manually.
