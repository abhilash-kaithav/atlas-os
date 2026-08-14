# Wedge Portfolio

Last updated: 2026-08-14
Status: Canonical GREEN wedge list

## Summary

| Wedge ID | Industry | Atomic job summary | Evidence strength | Status | Source objective |
| --- | --- | --- | --- | --- | --- |
| W-001 | Construction | Diagnose why a submitted pay app was blocked and coordinate the corrected resubmission before payment slips a cycle | High | GREEN | `TASK-016`, `TASK-017` |
| W-002 | Housing | Diagnose why a vacant unit will miss its make-ready date and coordinate the blockers before vacancy days extend | High | GREEN | `TASK-018` |
| W-003 | Administrative and support services | Diagnose why approved staffing hours cannot flow cleanly into payroll and invoicing and correct the mismatch before close | Medium | GREEN | `TASK-018` |

## W-001

- Industry: `Construction`
- Operating system: `Project Delivery and Contracting`
- Workflow: `Progress Billing and Compliance Administration`
- Structural failure: `SF-01 Exception-Path Breakdown`; related `SF-03 Decision Context Escapes the Record`
- End user: billing manager, AR lead, project accountant
- Economic buyer: controller or CFO at a commercial trade contractor
- Atomic job:
  - "AR manager at a commercial subcontractor needs to diagnose why a submitted pay application was rejected and coordinate the evidence required for resubmission so payment is not delayed."
- Existing systems/products:
  - GCPay
  - Oracle Textura
  - Procore
  - Autodesk Construction Cloud
  - Vista / Sage CRE
- Existing workaround:
  - spreadsheets for SOV and draw tracking
  - calls and email with GC AP or PM teams
  - manual waiver sequencing and re-entry
- Customer pain evidence:
  - repeated G2 complaints about manual SOV entry, awkward waiver handling, unclear statuses, and inability to self-correct
  - practitioner posts about missed deadlines, wrong forms, and prolonged payment delay
- Economic impact:
  - delayed receivables
  - extra billing labor
  - higher aging
  - working-capital stress
- Frequency: `Monthly billing cycle across active projects`
- Why current solution fails:
  - dominant products optimize the GC or owner control layer, not the neutral subcontractor correction desk
  - the real process still escapes into manual recovery across portals, PDFs, and calls
- Why now:
  - electronic pay apps, waiver workflows, and portal rules are now widespread enough that the correction loop is legible and recurring
  - working-capital pressure is higher and buyers feel cash delay directly
- Startup entry logic:
  - enter as a neutral exception desk across GC portals rather than a new construction ERP
- Competitive threat:
  - GCPay, Textura, Siteline, Procore, Autodesk
- Key assumptions:
  - subcontractor controllers will buy a standalone correction layer
  - rejection volume is frequent enough to justify net-new spend
- Invalidation evidence:
  - buyers say current portals already make correction easy
  - rejection frequency is too low to drive a budget line
- Source links:
  - `knowledge/research/trade-contractor-ar-monopoly-wedge-discovery/`
  - [GCPay Reviews | G2](https://www.g2.com/products/gcpay/reviews)
  - [Procore Reviews | G2](https://www.g2.com/products/procore/reviews)
  - [Tara Cristel podcast transcript](https://podscan.fm/podcasts/bred-to-build-construction-podcast/episodes/ep-53-a-200-day-pay-app-nightmare-amp-financing-gcs-w-tara-cristel)
- Status: `GREEN`
- Related wedges:
  - `W-003`
- Research objective that discovered it:
  - `TASK-016`
  - `TASK-017`

## W-002

- Industry: `Housing`
- Operating system: `Asset Utilization and Lease Management`
- Workflow: `Turnover and Readiness Management`
- Structural failure: `SF-06 Plan vs. Reality Divergence`; related `SF-03 Decision Context Escapes the Record`
- End user: maintenance coordinator, turns manager, community manager
- Economic buyer: regional operations leader, property manager, asset manager
- Atomic job:
  - "Maintenance coordinator at a multifamily operator needs to diagnose why a vacant unit will miss its make-ready date and coordinate vendors, approvals, parts, and inspections so vacancy days do not extend."
- Existing systems/products:
  - AppFolio Maintenance
  - Entrata
  - Yardi Facility Manager / Maintenance IQ
  - ResMan
  - Property Meld
- Existing workaround:
  - turn boards and spreadsheets
  - calls and texts with vendors
  - owner-approval chasing
  - side tracking of aging work orders and compliance
- Customer pain evidence:
  - practitioners describe maintenance coordination, stale work orders, vendor follow-up, and owner approvals as the operational bottleneck
  - users still struggle with make-ready boards and per-unit work-order handling even inside modern PMS tools
- Economic impact:
  - additional vacancy days
  - delayed rent start
  - repeat vendor trips
  - coordinator labor and resident dissatisfaction
- Frequency: `Every turn, plus recurring stalled repair situations`
- Why current solution fails:
  - PMS and maintenance tools track tasks, but the real blocker-resolution loop lives outside them
  - the workflow spans vendor responsiveness, unit access, approvals, parts, and inspection sequencing, which general maintenance modules do not fully own
- Why now:
  - labor scarcity and rising vacancy cost increase the cost of every missed ready date
  - mobile maintenance tooling exists, but visibility and accountability gaps remain after assignment
- Startup entry logic:
  - enter as a readiness-recovery layer that protects turn dates rather than a general PMS replacement
- Competitive threat:
  - Yardi, AppFolio, Entrata, ResMan, Property Meld
- Key assumptions:
  - buyers will pay specifically to protect make-ready dates
  - the failure mode is coordination, not merely labor scarcity
- Invalidation evidence:
  - operators say today’s PMS plus maintenance add-ons already handle blocker recovery well enough
  - most missed ready dates stem from uncontrollable capex or labor shortages rather than diagnosable coordination issues
- Source links:
  - `knowledge/research/wedge-discovery-program/batch-001-diverse-initial-pass.md`
  - [Property Meld | G2](https://www.g2.com/products/property-meld/reviews)
  - [Yardi Maintenance IQ](https://www.yardi.com/product/maintenance-iq/)
  - [AppFolio Maintenance](https://www.appfolio.com/property-manager/maintenance)
  - [How do you handle maintenance coordination for a small PM portfolio?](https://www.biggerpockets.com/forums/899/topics/1283438-how-do-you-handle-maintenance-coordination-for-a-small-pm-portfolio?page=1)
- Status: `GREEN`
- Related wedges:
  - `W-001`
- Research objective that discovered it:
  - `TASK-018`

## W-003

- Industry: `Administrative and support services`
- Operating system: `Workforce Coordination and Service Operations`
- Workflow: `Payroll, Billing, and Reconciliation`
- Structural failure: `SF-02 Cross-System Reconciliation`; related `SF-01 Exception-Path Breakdown`
- End user: staffing payroll specialist, billing operations coordinator, back-office analyst
- Economic buyer: controller, VP finance, back-office operations leader at a staffing firm
- Atomic job:
  - "Back-office payroll and billing specialist at a staffing agency needs to diagnose why approved hours cannot cleanly flow into payroll and client invoicing because of client approval, VMS, rate, shift, or pay/bill rule mismatches so workers are paid and clients billed on time."
- Existing systems/products:
  - Bullhorn Time & Expense / Middle Office
  - Avionte Payroll & Billing
  - Ascen
  - other ATS plus payroll stacks
- Existing workaround:
  - spreadsheet reconciliation
  - email and portal chasing
  - downloading and re-uploading candidate or vendor records
  - manual time approval and discrepancy review
- Customer pain evidence:
  - practitioners still describe vendor-specific onboarding and document flow over email and manual re-upload
  - job postings emphasize timesheet discrepancy resolution, approval chasing, and billing support as a core operational role
- Economic impact:
  - payroll delay
  - invoice delay
  - gross-margin leakage
  - extra reconciliation labor
  - slower cash conversion
- Frequency: `Weekly payroll and invoice cycle`
- Why current solution fails:
  - client rules, VMS approvals, and pay/bill logic vary by account
  - broad front-to-back suites still leave mismatch diagnosis to human specialists
  - operational truth is split across ATS, VMS, payroll, invoicing, and client approval layers
- Why now:
  - staffing firms face tighter margins and higher labor-cost sensitivity
  - time capture and pay/bill APIs are better, making an overlay workflow more plausible than in the past
- Startup entry logic:
  - enter as a pay/bill exception desk that sits on top of existing middle-office stacks and client portals
- Competitive threat:
  - Bullhorn
  - Avionte
  - Ascen
  - emerging middle-office specialists
- Key assumptions:
  - staffing firms will buy a standalone mismatch-resolution layer
  - exception volume is high enough even inside incumbent platforms
- Invalidation evidence:
  - customers report that integrated middle-office suites already eliminate most pay/bill exceptions
  - buyers see this as a services problem, not software worth buying
- Source links:
  - `knowledge/research/wedge-discovery-program/batch-001-diverse-initial-pass.md`
  - [Bullhorn Reviews | G2](https://www.g2.com/products/bullhorn/reviews)
  - [Avionté Reviews | G2](https://www.g2.com/products/avionte-avionte/reviews)
  - [Bullhorn Middle Office](https://www.bullhorn.com/products/middle-office/)
  - [Avionté Payroll & Billing](https://www.avionte.com/payroll-billing/)
- Status: `GREEN`
- Related wedges:
  - `W-001`
- Research objective that discovered it:
  - `TASK-018`
