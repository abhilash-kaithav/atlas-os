# Wedge Portfolio

Last updated: 2026-08-16
Status: Canonical preserved wedge list for the completed Top-50 program

## Summary

| Wedge ID | Industry | Atomic job summary | Evidence strength | Status | Source objective |
| --- | --- | --- | --- | --- | --- |
| W-001 | Construction | Diagnose why a submitted pay app was blocked and coordinate the corrected resubmission before payment slips a cycle. | High | GREEN | `TASK-017`, `TASK-021`, `TASK-022` |
| W-002 | Housing | Diagnose why a vacant unit will miss its make-ready date and coordinate blockers before vacancy days extend. | High | GREEN | `TASK-018`, `TASK-021`, `TASK-022` |
| W-003 | Administrative and support services | Diagnose why approved staffing hours cannot flow cleanly into payroll and invoicing and correct the mismatch before close. | Medium | YELLOW | `TASK-018`, `TASK-021`, `TASK-022` |
| W-004 | Funds, trusts, and other financial vehicles | Diagnose why cash, position, pricing, or accounting records do not reconcile across administrator, custodian, and portfolio systems before NAV and reporting. | Medium | YELLOW | `TASK-021`, `TASK-022` |
| W-005 | Truck transportation | Assemble missing proof, validate rates and accessorials, and resolve billing disputes so completed loads invoice cleanly and cash is not delayed. | Medium | YELLOW | `TASK-021`, `TASK-022` |

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
- Validation gates: Workflow Coverage `Pass`; Customer Evidence `Pass`; Frequency `Pass`; Buyer `Pass`; Bottom-up Economics `Pass`; Incumbent Boundary `Pass`; Timing `Pass`; Competitive Stress Test `Pass`; Kill Test `Pass`
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
- Validation gates: Workflow Coverage `Pass`; Customer Evidence `Pass`; Frequency `Pass`; Buyer `Pass`; Bottom-up Economics `Pass`; Incumbent Boundary `Pass`; Timing `Pass`; Competitive Stress Test `Pass`; Kill Test `Pass`
- Key assumptions: the pain is diagnosable coordination failure rather than uncontrollable capex backlog
- Invalidation evidence: operators report that modern PMS plus maintenance add-ons already resolve most missed-ready-date cases
- Source links:
  - [Customer Evidence Repository](./customer-evidence-repository.md)
  - [Housing Workflow Inventory](./workflow-inventories/housing.md)
  - [How do you handle maintenance coordination for a small PM portfolio?](https://www.biggerpockets.com/forums/899/topics/1283438-how-do-you-handle-maintenance-coordination-for-a-small-pm-portfolio?page=1)
  - [Maintenance Coordinator | Edgewood Properties](https://careers.edgewoodproperties.com/jobs/2026-5245)
- Status: `GREEN`
- Related wedges: `W-001`

## W-004

- Industry: `Funds, trusts, and other financial vehicles`
- Operating system: `Capital Markets and Investment Management`
- Workflow: `Valuation, NAV, and reconciliation`
- Structural failure: `SF-02 Cross-System Reconciliation`; related `SF-03 Decision Context Escapes the Record`
- End user: NAV oversight analyst; fund accountant; reconciliation lead
- Economic buyer: COO; CFO; or head of fund operations at a manager, allocator platform, or administrator
- Atomic job:
  - "Fund operations staff need to diagnose why cash, position, pricing, or accounting records do not reconcile across the administrator, custodian, and portfolio systems before NAV publication or investor reporting."
- Existing systems/products: SS&C Geneva and fund-accounting services; Clearwater; SimCorp; State Street Alpha; Allvue
- Existing workaround: spreadsheets for break logs; email with administrators and custodians; shadow-accounting workpapers; manual exception comments before close
- Customer pain evidence: practitioner roles still revolve around daily reconciliations, break research, and escalation; current users still frame reconciliation labor reduction as a core purchase reason rather than a solved commodity
- Economic impact: delayed NAV; slower investor reporting; audit risk; staff cost; client-confidence and oversight burden
- Frequency: `Daily or period-close recurring habit`
- Why current solution fails: books and records remain split across managers, administrators, custodians, and reporting layers; exception narratives still live outside the authoritative record and are often absorbed by services teams
- Why now: transparency demands are higher; multi-provider operating models remain common; ingestion and workflow tooling are better than when many incumbent stacks were designed
- Startup entry logic: enter as an oversight and break-triage layer that sits across manager, administrator, custodian, and reporting boundaries
- Competitive threat: SS&C; Clearwater; SimCorp; State Street; BlackRock Aladdin
- Validation gates: Workflow Coverage `Pass`; Customer Evidence `Borderline`; Frequency `Pass`; Buyer `Pass`; Bottom-up Economics `Pass`; Incumbent Boundary `Borderline`; Timing `Pass`; Competitive Stress Test `Borderline`; Kill Test `Borderline`
- Key assumptions: operators will buy a standalone oversight layer instead of continuing to absorb break research through administrators or shadow accounting
- Invalidation evidence: buyers say administrators already clear breaks fast enough or prefer outsourced operations over a new software category
- Source links:
  - [Customer Evidence Repository](./customer-evidence-repository.md)
  - [Funds, Trusts, and Other Financial Vehicles Workflow Inventory](./workflow-inventories/funds-trusts-and-other-financial-vehicles.md)
  - [Clearwater Analytics Reviews | G2](https://www.g2.com/it/products/clearwater-analytics/reviews)
  - [Analyst, Fund Accounting @ Principal Financial Services](https://www.tealhq.com/job/analyst-fund-accounting_c40ca656-f356-4f90-a7c7-b7a4e864e1cc)
- Status: `YELLOW`
- Related wedges: `W-005`

## W-005

- Industry: `Truck transportation`
- Operating system: `Transportation Network Operations`
- Workflow: `Freight audit and billing`
- Structural failure: `SF-02 Cross-System Reconciliation`; related `SF-01 Exception-Path Breakdown`
- End user: billing specialist; freight auditor; brokerage billing coordinator
- Economic buyer: controller; head of settlement or billing; operations finance leader at a carrier or broker
- Atomic job:
  - "Transportation billing staff need to assemble missing proof, validate rates and accessorials, and resolve detention or billing disputes so completed loads invoice cleanly and cash is not delayed."
- Existing systems/products: McLeod LoadMaster; Descartes transportation management and local haulage tools; Oracle Transportation Management; Trimble; project44 adjacent visibility
- Existing workaround: spreadsheets; email with drivers, carriers, brokers, and customers; manual POD chasing; local dispute logs
- Customer pain evidence: freight-billing roles explicitly exist to validate rates, proof, and discrepancy queues; software reviews still point to missing trucking-specific billing logic and manual rate handling
- Economic impact: missed accessorials; delayed billing; over- or undercharges; higher DSO; extra back-office labor; lower load margin
- Frequency: `Daily and weekly invoice cycle across completed loads`
- Why current solution fails: clean-path TMS automation still depends on late or missing proof, customer-specific requirements, and multi-party document collection; exception memory still leaves the core system
- Why now: mobile document capture, connected TMS workflows, and API/EDI maturity improve the chance of a thin exception layer; margin pressure makes missed charges more painful
- Startup entry logic: enter as a billing-recovery and exception-resolution layer on top of existing TMS and document flows rather than as a full TMS replacement
- Competitive threat: McLeod; Descartes; Oracle Transportation Management; Trimble; TMS vendors that can extend billing modules
- Validation gates: Workflow Coverage `Pass`; Customer Evidence `Borderline`; Frequency `Pass`; Buyer `Pass`; Bottom-up Economics `Pass`; Incumbent Boundary `Borderline`; Timing `Pass`; Competitive Stress Test `Borderline`; Kill Test `Borderline`
- Key assumptions: carriers and brokers will pay for a focused recovery layer instead of adding more clerical headcount or waiting for TMS vendors
- Invalidation evidence: current TMS plus document-capture stacks already solve the issue well enough or TMS vendors can close the gap quickly
- Source links:
  - [Customer Evidence Repository](./customer-evidence-repository.md)
  - [Truck Transportation Workflow Inventory](./workflow-inventories/truck-transportation.md)
  - [IntelliTrans Transportation Freight Audit & Payment Reviews | G2](https://www.g2.com/products/intellitrans-transportation-freight-audit-payment/reviews)
  - [Invoice Audit Analyst | Worldpac](https://careers.worldpac.com/careers-home/jobs/4510?lang=en-us)
- Status: `YELLOW`
- Related wedges: `W-001`, `W-004`

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
- Validation gates: Workflow Coverage `Pass`; Customer Evidence `Borderline`; Frequency `Pass`; Buyer `Pass`; Bottom-up Economics `Pass`; Incumbent Boundary `Borderline`; Timing `Pass`; Competitive Stress Test `Borderline`; Kill Test `Borderline`
- Key assumptions: staffing firms will buy standalone exception software rather than continue staffing the workflow manually
- Invalidation evidence: middle-office suites prove good enough and buyers keep treating the problem as clerical labor instead of a software budget
- Source links:
  - [Customer Evidence Repository](./customer-evidence-repository.md)
  - [Administrative and Support Services Workflow Inventory](./workflow-inventories/administrative-and-support-services.md)
  - [Bullhorn Reconciliation Dashboard](https://kb.bullhorn.com/bhone/Content/BH1/Topics/reconciliationDashboard.htm)
  - [Payroll/Billing Specialist | WorldWide Medical Staffing](https://www.simplyhired.com/job/JcFijGynFMbh9z433tIFxyVEUgZojUlMYQQIt9_rk5dMkZSaXLELqg)
- Status: `YELLOW`
- Related wedges: `W-001`
