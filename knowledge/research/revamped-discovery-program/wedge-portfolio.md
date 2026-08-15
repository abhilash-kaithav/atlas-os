# Wedge Portfolio

Last updated: 2026-08-15
Status: Canonical preserved wedge list for revamped Batch 1

## Summary

| Wedge ID | Industry | Atomic job summary | Evidence strength | Status | Source objective |
| --- | --- | --- | --- | --- | --- |
| W-001 | Construction | Diagnose why a submitted pay app was blocked and coordinate the corrected resubmission before payment slips a cycle. | High | GREEN | `TASK-017`, `TASK-020` |
| W-002 | Housing | Diagnose why a vacant unit will miss its make-ready date and coordinate blockers before vacancy days extend. | High | GREEN | `TASK-018`, `TASK-020` |
| W-003 | Administrative and support services | Diagnose why approved staffing hours cannot flow cleanly into payroll and invoicing and correct the mismatch before close. | Medium | YELLOW | `TASK-018`, `TASK-020` |

## W-001

- Industry: `Construction`
- Operating system: `Project Delivery and Contracting`
- Workflow: `Collections, waiver, and payment dispute recovery`
- Structural failure: `SF-01 Exception-Path Breakdown`; related `SF-03 Decision Context Escapes the Record`
- End user: project accountant; billing specialist; AR lead
- Economic buyer: controller or CFO at a commercial trade contractor
- Atomic job:
  - "AR manager at a commercial subcontractor needs to diagnose why a submitted pay application was rejected and coordinate the evidence required for resubmission so payment is not delayed."
- Existing systems/products: GCPay; Oracle Textura; Procore; Autodesk Construction Cloud; Vista / Sage
- Existing workaround: spreadsheets for SOV and draw tracking; calls and email with GC AP or PM teams; manual waiver sequencing and re-entry
- Customer pain evidence: repeated review and practitioner evidence show manual SOV entry, unclear blocker visibility, and long cash delays
- Economic impact: delayed receivables; higher aging; extra billing labor; financing pressure
- Frequency: `Monthly billing cycle across active projects`
- Why current solution fails: dominant tools optimize the GC or owner control layer and still leave subcontractor-side correction work fragmented across portals, PDFs, and email
- Why now: digital pay-app tooling is widespread enough that the exception desk is visible and recurring; working-capital pressure makes the pain acute
- Startup entry logic: enter as a neutral correction and resubmission layer across GC portals rather than a new construction ERP
- Competitive threat: GCPay; Textura; Procore; Autodesk; Siteline
- Key assumptions: rejection volume is high enough to justify budget; neutral multi-portal workflow is valuable
- Invalidation evidence: trade contractors report current portals already make correction fast and obvious
- Source links:
  - [Customer Evidence Repository](./customer-evidence-repository.md)
  - [Construction Workflow Inventory](./workflow-inventories/construction.md)
  - [GCPay Reviews | G2](https://www.g2.com/products/gcpay/reviews)
  - [Tara Cristel podcast transcript](https://podscan.fm/podcasts/bred-to-build-construction-podcast/episodes/ep-53-a-200-day-pay-app-nightmare-amp-financing-gcs-w-tara-cristel)
- Status: `GREEN`
- Related wedges: `W-003`

## W-002

- Industry: `Housing`
- Operating system: `Asset Utilization and Lease Management`
- Workflow: `Turnover and make-ready recovery`
- Structural failure: `SF-06 Plan vs. Reality Divergence`; related `SF-03 Decision Context Escapes the Record`
- End user: turns coordinator; maintenance coordinator; community manager
- Economic buyer: regional operations leader; property manager; asset manager
- Atomic job:
  - "Maintenance coordinator at a multifamily operator needs to diagnose why a vacant unit will miss its make-ready date and coordinate vendors, approvals, parts, and inspections so vacancy days do not extend."
- Existing systems/products: AppFolio Maintenance; Entrata; Yardi Facility Manager / Maintenance IQ; ResMan; Property Meld
- Existing workaround: turn boards and spreadsheets; calls and texts with vendors; owner-approval chasing; side tracking of stale work orders
- Customer pain evidence: practitioner and job-role evidence show vendor chasing, approval delays, and missed ready dates still living outside the PMS
- Economic impact: added vacancy days; delayed rent start; coordinator labor; repeat vendor trips
- Frequency: `Every turn plus recurring stalled repair situations`
- Why current solution fails: PMS and maintenance tools track tasks, but blocker recovery crosses vendor responsiveness, approvals, unit access, parts, and inspection sequencing
- Why now: labor scarcity and vacancy sensitivity make each missed ready date more expensive while mobile tooling makes the gap more legible
- Startup entry logic: enter as a readiness-recovery layer that protects turn dates rather than as a general PMS replacement
- Competitive threat: Yardi; Entrata; AppFolio; ResMan; Property Meld
- Key assumptions: the pain is diagnosable coordination failure rather than uncontrollable capex backlog
- Invalidation evidence: operators report that modern PMS plus maintenance add-ons already resolve most missed-ready-date cases
- Source links:
  - [Customer Evidence Repository](./customer-evidence-repository.md)
  - [Housing Workflow Inventory](./workflow-inventories/housing.md)
  - [How do you handle maintenance coordination for a small PM portfolio?](https://www.biggerpockets.com/forums/899/topics/1283438-how-do-you-handle-maintenance-coordination-for-a-small-pm-portfolio?page=1)
  - [Maintenance Coordinator | Edgewood Properties](https://careers.edgewoodproperties.com/jobs/2026-5245)
- Status: `GREEN`
- Related wedges: `W-001`

## W-003

- Industry: `Administrative and support services`
- Operating system: `Workforce Coordination and Service Operations`
- Workflow: `Pay/bill discrepancy resolution`
- Structural failure: `SF-02 Cross-System Reconciliation`; related `SF-01 Exception-Path Breakdown`
- End user: staffing payroll specialist; billing operations coordinator; reconciliation analyst
- Economic buyer: controller; VP finance; back-office operations leader at a staffing firm
- Atomic job:
  - "Back-office payroll and billing specialist at a staffing agency needs to diagnose why approved hours cannot cleanly flow into payroll and client invoicing because of client approval, VMS, rate, shift, or pay/bill rule mismatches so workers are paid and clients billed on time."
- Existing systems/products: Bullhorn Time & Expense / Middle Office; Avionte Payroll & Billing; Ascen; ATS plus payroll stacks
- Existing workaround: spreadsheet reconciliation; email and portal chasing; downloading and re-uploading records; manual approval follow-up
- Customer pain evidence: recurring job-role and product evidence show this is still a dedicated middle-office task, but the independent practitioner base is thinner than for `W-001` and `W-002`
- Economic impact: payroll delay; invoice delay; gross-margin leakage; extra reconciliation labor; slower cash conversion
- Frequency: `Weekly payroll and invoice cycle`
- Why current solution fails: client rules, VMS approvals, and pay/bill logic vary by account; integrated suites reduce volume but still leave mismatch diagnosis to humans
- Why now: tighter staffing margins and better time/pay APIs make a cross-system overlay more plausible
- Startup entry logic: enter as a pay/bill exception desk that sits on top of existing middle-office stacks and client portals
- Competitive threat: Bullhorn; Avionte; Ascen; category-adjacent middle-office tooling
- Key assumptions: staffing firms will buy standalone exception software rather than continue staffing the workflow manually
- Invalidation evidence: middle-office suites prove good enough and buyers keep treating the problem as clerical labor instead of a software budget
- Source links:
  - [Customer Evidence Repository](./customer-evidence-repository.md)
  - [Administrative and Support Services Workflow Inventory](./workflow-inventories/administrative-and-support-services.md)
  - [Bullhorn Reconciliation Dashboard](https://kb.bullhorn.com/bhone/Content/BH1/Topics/reconciliationDashboard.htm)
  - [Payroll/Billing Specialist | WorldWide Medical Staffing](https://www.simplyhired.com/job/JcFijGynFMbh9z433tIFxyVEUgZojUlMYQQIt9_rk5dMkZSaXLELqg)
- Status: `YELLOW`
- Related wedges: `W-001`
