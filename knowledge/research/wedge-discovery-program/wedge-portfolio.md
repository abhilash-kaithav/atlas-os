# Wedge Portfolio

Last updated: 2026-08-15
Status: Canonical preserved wedge list (`GREEN` + `YELLOW`)

## Summary

| Wedge ID | Industry | Atomic job summary | Evidence strength | Status | Source objective |
| --- | --- | --- | --- | --- | --- |
| W-001 | Construction | Diagnose why a submitted pay app was blocked and coordinate the corrected resubmission before payment slips a cycle | High | GREEN | `TASK-016`, `TASK-017` |
| W-002 | Housing | Diagnose why a vacant unit will miss its make-ready date and coordinate the blockers before vacancy days extend | High | GREEN | `TASK-018`, `TASK-019` |
| W-003 | Administrative and support services | Diagnose why approved staffing hours cannot flow cleanly into payroll and invoicing and correct the mismatch before close | Medium | YELLOW | `TASK-018`, `TASK-019` |
| W-004 | Funds, trusts, and other financial vehicles | Diagnose why cash, position, or pricing records do not reconcile across admin, custodian, and portfolio systems before NAV and reporting | Medium | YELLOW | `TASK-019` |
| W-005 | Truck transportation | Assemble missing proof, validate rates and accessorials, and resolve billing disputes so completed loads invoice cleanly and cash is not delayed | Medium | YELLOW | `TASK-019` |

## W-001

- Industry: `Construction`
- Operating system: `Project Delivery and Contracting`
- Workflow: `Progress Billing and Compliance Administration`
- Structural failure: `SF-01 Exception-Path Breakdown`; related `SF-03 Decision Context Escapes the Record`
- End user: billing manager, AR lead, project accountant
- Economic buyer: controller or CFO at a commercial trade contractor
- Atomic job:
  - "AR manager at a commercial subcontractor needs to diagnose why a submitted pay application was rejected and coordinate the evidence required for resubmission so payment is not delayed."
- Existing systems/products: GCPay; Oracle Textura; Procore; Autodesk Construction Cloud; Vista / Sage CRE
- Existing workaround: spreadsheets for SOV and draw tracking; calls and email with GC AP or PM teams; manual waiver sequencing and re-entry
- Customer pain evidence: repeated G2 complaints about manual SOV entry, awkward waiver handling, unclear statuses, and inability to self-correct; practitioner evidence of multi-month payment delays
- Economic impact: delayed receivables; extra billing labor; higher aging; working-capital stress
- Frequency: `Monthly billing cycle across active projects`
- Why current solution fails: dominant products optimize the GC or owner control layer, not the neutral subcontractor correction desk; the real process still escapes into manual recovery across portals, PDFs, and calls
- Why now: electronic pay apps, waiver workflows, and portal rules are widespread enough that the correction loop is legible and recurring; working-capital pressure is higher and buyers feel cash delay directly
- Startup entry logic: enter as a neutral exception desk across GC portals rather than a new construction ERP
- Competitive threat: GCPay; Textura; Siteline; Procore; Autodesk
- Validation gates: Gate 1 customer evidence `High`; Gate 2 economics `High`; Gate 3 incumbent boundary `High`; Gate 4 frequency `High`; Gate 5 timing `High`
- Invalidation evidence: buyers say current portals already make correction easy; rejection frequency is too low to drive a budget line
- Source links:
  - `knowledge/research/trade-contractor-ar-monopoly-wedge-discovery/`
  - [GCPay Reviews | G2](https://www.g2.com/products/gcpay/reviews)
  - [Procore Reviews | G2](https://www.g2.com/products/procore/reviews)
  - [Tara Cristel podcast transcript](https://podscan.fm/podcasts/bred-to-build-construction-podcast/episodes/ep-53-a-200-day-pay-app-nightmare-amp-financing-gcs-w-tara-cristel)
- Status: `GREEN`
- Related wedges: `W-003`, `W-005`

## W-002

- Industry: `Housing`
- Operating system: `Asset Utilization and Lease Management`
- Workflow: `Turnover and Readiness Management`
- Structural failure: `SF-06 Plan vs. Reality Divergence`; related `SF-03 Decision Context Escapes the Record`
- End user: maintenance coordinator, turns manager, community manager
- Economic buyer: regional operations leader, property manager, asset manager
- Atomic job:
  - "Maintenance coordinator at a multifamily operator needs to diagnose why a vacant unit will miss its make-ready date and coordinate vendors, approvals, parts, and inspections so vacancy days do not extend."
- Existing systems/products: AppFolio Maintenance; Entrata; Yardi Facility Manager / Maintenance IQ; ResMan; Property Meld
- Existing workaround: turn boards and spreadsheets; calls and texts with vendors; owner-approval chasing; side tracking of aging work orders and compliance
- Customer pain evidence: practitioners describe maintenance coordination, stale work orders, vendor follow-up, and owner approvals as the operational bottleneck; users still struggle with make-ready boards and per-unit work-order handling inside current PMS tools
- Economic impact: additional vacancy days; delayed rent start; repeat vendor trips; coordinator labor; resident dissatisfaction
- Frequency: `Every turn, plus recurring stalled repair situations`
- Why current solution fails: PMS and maintenance tools track tasks, but the real blocker-resolution loop lives outside them; the workflow spans vendor responsiveness, unit access, approvals, parts, and inspection sequencing
- Why now: labor scarcity and rising vacancy cost increase the cost of every missed ready date; mobile maintenance tooling exists, but visibility and accountability gaps remain after assignment
- Startup entry logic: enter as a readiness-recovery layer that protects turn dates rather than a general PMS replacement
- Competitive threat: Yardi; AppFolio; Entrata; ResMan; Property Meld
- Validation gates: Gate 1 customer evidence `High`; Gate 2 economics `High`; Gate 3 incumbent boundary `High`; Gate 4 frequency `High`; Gate 5 timing `Medium-High`
- Invalidation evidence: operators say today’s PMS plus maintenance add-ons already handle blocker recovery well enough; most missed ready dates stem from uncontrollable capex or labor shortages rather than diagnosable coordination issues
- Source links:
  - `knowledge/research/wedge-discovery-program/batch-001-diverse-initial-pass.md`
  - [Property Meld | G2](https://www.g2.com/products/property-meld/reviews)
  - [Yardi Maintenance IQ](https://www.yardi.com/product/maintenance-iq/)
  - [AppFolio Maintenance](https://www.appfolio.com/property-manager/maintenance)
  - [How do you handle maintenance coordination for a small PM portfolio?](https://www.biggerpockets.com/forums/899/topics/1283438-how-do-you-handle-maintenance-coordination-for-a-small-pm-portfolio?page=1)
- Status: `GREEN`
- Related wedges: `W-001`

## W-003

- Industry: `Administrative and support services`
- Operating system: `Workforce Coordination and Service Operations`
- Workflow: `Payroll, Billing, and Reconciliation`
- Structural failure: `SF-02 Cross-System Reconciliation`; related `SF-01 Exception-Path Breakdown`
- End user: staffing payroll specialist, billing operations coordinator, back-office analyst
- Economic buyer: controller, VP finance, back-office operations leader at a staffing firm
- Atomic job:
  - "Back-office payroll and billing specialist at a staffing agency needs to diagnose why approved hours cannot cleanly flow into payroll and client invoicing because of client approval, VMS, rate, shift, or pay/bill rule mismatches so workers are paid and clients billed on time."
- Existing systems/products: Bullhorn Time & Expense / Middle Office; Avionté Payroll & Billing; Ascen; ATS plus payroll stacks
- Existing workaround: spreadsheet reconciliation; email and portal chasing; downloading and re-uploading records; manual time approval and discrepancy review
- Customer pain evidence: practitioners still describe vendor-specific onboarding and manual record re-upload; job postings explicitly center on timesheet discrepancy resolution, approval chasing, and billing support
- Economic impact: payroll delay; invoice delay; gross-margin leakage; extra reconciliation labor; slower cash conversion
- Frequency: `Weekly payroll and invoice cycle`
- Why current solution fails: client rules, VMS approvals, and pay/bill logic vary by account; broad front-to-back suites still leave mismatch diagnosis to human specialists
- Why now: tighter staffing margins and better time/pay APIs make an overlay more plausible than in the past
- Startup entry logic: enter as a pay/bill exception desk that sits on top of existing middle-office stacks and client portals
- Competitive threat: Bullhorn; Avionté; Ascen; emerging middle-office specialists
- Validation gates: Gate 1 customer evidence `Medium`; Gate 2 economics `High`; Gate 3 incumbent boundary `Medium`; Gate 4 frequency `High`; Gate 5 timing `Medium`
- Invalidation evidence: customers report that integrated middle-office suites already eliminate most pay/bill exceptions; buyers see this as a services problem, not software worth buying
- Source links:
  - `knowledge/research/wedge-discovery-program/batch-001-diverse-initial-pass.md`
  - [Bullhorn Reviews | G2](https://www.g2.com/products/bullhorn/reviews)
  - [Avionté Reviews | G2](https://www.g2.com/products/avionte-avionte/reviews)
  - [Bullhorn Middle Office](https://www.bullhorn.com/products/middle-office/)
  - [Avionté Payroll & Billing](https://www.avionte.com/payroll-billing/)
- Status: `YELLOW`
- Related wedges: `W-001`

## W-004

- Industry: `Funds, trusts, and other financial vehicles`
- Operating system: `Capital Markets and Investment Management`
- Workflow: `Valuation, NAV, and Reconciliation`
- Structural failure: `SF-02 Cross-System Reconciliation`; related `SF-03 Decision Context Escapes the Record`
- End user: NAV oversight analyst, fund accountant, reconciliation lead
- Economic buyer: COO, CFO, or head of fund operations at a manager, allocator platform, or administrator
- Atomic job:
  - "Fund operations staff need to diagnose why cash, position, pricing, or accounting records do not reconcile across the administrator, custodian, and portfolio systems before NAV publication or investor reporting."
- Existing systems/products: SS&C Geneva and fund-accounting services; Clearwater; SimCorp; State Street Alpha; Allvue
- Existing workaround: spreadsheets for break logs; email with administrators and custodians; shadow-accounting workpapers; manual exception comments before close
- Customer pain evidence: practitioner roles still revolve around daily reconciliations, break research, and escalation; product users still praise manual-reduction and reconciliation support as a core value signal rather than a solved problem
- Economic impact: delayed NAV; slower investor reporting; audit risk; staff cost; client-confidence and oversight burden
- Frequency: `Daily or period-close recurring habit`
- Why current solution fails: books and records are split across managers, administrators, custodians, and reporting layers; exception narratives live outside the record and are often services-backed
- Why now: transparency demands are higher; multi-provider operating models remain common; data-ingestion and workflow tooling are better than when most incumbent stacks were designed
- Startup entry logic: enter as an oversight and break-triage layer that sits across manager, admin, custodian, and reporting boundaries
- Competitive threat: SS&C; Clearwater; SimCorp; State Street; BlackRock Aladdin
- Validation gates: Gate 1 customer evidence `Medium`; Gate 2 economics `High`; Gate 3 incumbent boundary `Medium`; Gate 4 frequency `High`; Gate 5 timing `Medium`
- Invalidation evidence: buyers say administrators already clear breaks fast enough; outsourced shadow accounting remains the preferred answer; no one budgets for a standalone layer
- Source links:
  - `knowledge/research/workflow-library/workflows/valuation-nav-and-reconciliation.md`
  - [SS&C Fund Accounting](https://www.ssctech.com/solutions/fund-accounting)
  - [Clearwater Analytics Reviews | G2](https://www.g2.com/it/products/clearwater-analytics/reviews)
  - [Analyst, Fund Accounting @ Principal Financial Services](https://www.tealhq.com/job/analyst-fund-accounting_c40ca656-f356-4f90-a7c7-b7a4e864e1cc)
  - [Fund Accounting Edge Opportunities](https://fundaccountingedge.com/opportunities/)
- Status: `YELLOW`
- Related wedges: `W-005`

## W-005

- Industry: `Truck transportation`
- Operating system: `Transportation Network Operations`
- Workflow: `Freight Audit and Billing`
- Structural failure: `SF-02 Cross-System Reconciliation`; related `SF-01 Exception-Path Breakdown`
- End user: billing specialist, freight auditor, brokerage billing coordinator
- Economic buyer: controller, head of settlement or billing, operations finance leader at a carrier or broker
- Atomic job:
  - "Transportation billing staff need to assemble missing proof, validate rates and accessorials, and resolve detention or billing disputes so completed loads invoice cleanly and cash is not delayed."
- Existing systems/products: McLeod LoadMaster; Descartes transportation management and local haulage tools; Oracle Transportation Management; Trimble; project44 adjacent visibility
- Existing workaround: spreadsheets; email with drivers, carriers, brokers, and customers; manual POD chasing; local dispute logs
- Customer pain evidence: freight-billing roles explicitly exist to validate rates, proof, and discrepancy queues; transportation invoice-audit guidance still centers on bill-of-lading, rate, and service verification; weak software reviews point to missing trucking-specific billing logic
- Economic impact: missed accessorials; delayed billing; over- or undercharges; higher DSO; extra back-office labor; lower load margin
- Frequency: `Daily and weekly invoice cycle across completed loads`
- Why current solution fails: clean-path TMS automation still depends on late or missing proof, customer-specific requirements, and multi-party document collection; exception memory leaves the core system
- Why now: mobile document capture, connected TMS workflows, and API/EDI maturity improve the chance of a thin exception layer; margin pressure makes missed charges more painful
- Startup entry logic: enter as a billing-recovery and exception-resolution layer on top of existing TMS and document flows rather than as a full TMS replacement
- Competitive threat: McLeod; Descartes; Oracle Transportation Management; Trimble; TMS vendors that can extend billing modules
- Validation gates: Gate 1 customer evidence `Medium`; Gate 2 economics `High`; Gate 3 incumbent boundary `Medium`; Gate 4 frequency `High`; Gate 5 timing `Medium`
- Invalidation evidence: carriers say current TMS and document-capture stacks already solve the issue; buyers prefer clerical staff over net-new software; TMS vendors close the gap quickly
- Source links:
  - `knowledge/research/workflow-library/workflows/freight-audit-and-billing.md`
  - [LTL Shipping and Freight Software | McLeod Software](https://www.mcleodsoftware.com/who-we-serve/ltl-carriers/)
  - [Descartes Local Haulage](https://www.descartes.com/resources/knowledge-center/descartes-local-haulage)
  - [IntelliTrans Transportation Freight Audit & Payment Reviews | G2](https://www.g2.com/products/intellitrans-transportation-freight-audit-payment/reviews)
  - [Transportation invoice audit | GSA](https://www.gsa.gov/policy-regulations/policy/transportation-management-policy/transportation-invoice-audit)
- Status: `YELLOW`
- Related wedges: `W-001`, `W-004`
