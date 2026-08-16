# Investment Candidate Dossiers

Last updated: 2026-08-16
Status: Complete for committee survivors

## W-001 Dossier

### Executive Summary

`W-001` targets the subcontractor-side correction loop after a pay application or waiver-backed billing package fails to move forward. The committee views it as the strongest surviving candidate because the pain is economically urgent, the buyer is clear, the workflow is already staffed manually, and the dominant products still optimize the transaction flow more than the diagnosis-and-resubmission desk.

### Atomic Job

Project-accounting or AR staff at a commercial trade contractor need to determine why a submitted pay application was blocked, assemble the missing support, correct the billing package, and resubmit it before cash slips a billing cycle.

### Customer

- End user: project accountant; billing specialist; AR lead
- Economic buyer: controller or CFO
- Budget owner: controller or finance leadership
- Decision maker: controller or CFO
- Champion: project accountant or AR lead who owns aging and short-pay follow-up

### Workflow

- Current workflow: project setup -> progress billing -> portal submission -> status monitoring
- Recovery workflow: rejected pay app or waiver hold -> diagnosis -> evidence gathering -> correction -> approval -> resubmission -> payment follow-up
- Manual work: SOV comparisons, backup package rebuilding, waiver sequencing, GC communication, spreadsheet status tracking
- Exception path: SOV mismatch, missing backup, waiver issue, compliance hold, short-pay dispute
- Current workaround: Excel trackers, email, phone, PDF packs, side logs by project accountant or controller

### Customer Evidence

- Customer evidence:
  - `CE-B1-001`: GCPay reviews describe manual SOV loading, awkward waiver handling, and low visibility when something breaks
  - `CE-B1-002`: Procore reviews still mention Excel and manual uploads in billing-adjacent workflows
  - `CE-B1-003`: practitioner evidence ties blocked billing directly to financing pain and delayed cash
  - `CE-B1-005`: project-accountant role exists for exactly this loop
- Vendor evidence:
  - `CE-B1-004`: GCPay documentation proves the workflow matters, but product structure still centers on payment and compliance flow
- Atlas inference:
  - The winning edge is not generic construction billing automation. It is a neutral correction layer across GC-controlled portals and document states.
- Confidence level: `High`

### Buyer Economics

- Frequency: monthly billing cycle across active projects
- Annual customer impact: repeated DSO extension, financing cost, rebilling labor, higher aging, and margin leakage from uncollected or delayed draws
- ROI mechanism: reduce days-to-cash, avoid short-pay write-downs, compress billing labor, and cut financing pressure
- Budget source: controller/CFO operating budget or cash-optimization budget
- Buying trigger: recurring rejections, rising aging, working-capital strain, or multi-portal sprawl
- Economic justification: this is one of the few surviving wedges where labor savings and cash acceleration stack in the same workflow

### Competitive Landscape

- Current vendors: GCPay, Textura, Procore, Autodesk Construction Cloud, Vista / Sage, Siteline
- Workflow ownership: incumbents own submission, portal record, or ERP destination; they do not own neutral correction across many counterparties
- Incumbent strengths: installed base, system-of-record control, existing billing workflow presence
- Incumbent weaknesses: optimize the happy path, remain biased toward GC/owner control, and still externalize exception memory into spreadsheets and email
- Product boundaries: portal tools own submission state; ERPs own accounting state; neither clearly owns cross-portal rejection diagnosis and resubmission
- Likelihood incumbents solve this: `Medium`, but not fast enough to dismiss the wedge today because multi-party neutrality is part of the value

### Startup Thesis

A startup can win by being the neutral correction-and-resubmission layer that sits above existing portals and ERP stacks, learns recurring blocker patterns, and shortens the time between rejection and bill-ready recovery.

### Unknowns

- How concentrated are rejections and short-pay recovery needs among target subcontractors?
- Can a common blocker taxonomy cover enough rejected pay apps to make the product repeatable?
- Will buyers purchase a focused recovery layer rather than expanding clerical headcount or tolerating finance pain?

### Reasons To Pass

- The workflow may be too bespoke by GC, owner, and project type.
- Major portal vendors could add better blocker visibility if the use case becomes obvious.
- Some firms may still solve the problem through disciplined controllers and AR teams without new software.

### Validation Required

- Prove rejection-volume concentration by contractor profile
- Validate willingness to pay for neutral multi-portal diagnosis rather than more accounting labor
- Confirm that the most painful blocker patterns recur often enough to productize

## W-002 Dossier

### Executive Summary

`W-002` targets the readiness-recovery loop when a multifamily unit will miss its make-ready date. The committee kept it alive because the job is concrete, recurring, revenue-linked, and still coordinated manually outside the PMS. It sits below generic maintenance software and above the fragmented vendor-and-approval chase work that actually extends vacancy days.

### Atomic Job

Operations staff at a multifamily operator need to determine why a vacant unit will miss its make-ready date and coordinate vendors, approvals, parts, access, and inspections before the ready date slips and rent start is delayed.

### Customer

- End user: turns coordinator; maintenance coordinator; community manager
- Economic buyer: regional operations leader; property manager; asset manager
- Budget owner: property operations leadership
- Decision maker: regional operations or asset-management leadership
- Champion: maintenance coordinator or turns coordinator who already runs the human control tower

### Workflow

- Current workflow: notice received -> turnover plan -> dispatch and vendor scheduling -> inspections -> ready-for-lease handoff
- Recovery workflow: milestone slips -> blocker diagnosis -> vendor/approval/part/access escalation -> resequencing -> ready-date recovery
- Manual work: vendor chasing, status verification, owner-approval follow-up, side communication, inspection sequencing
- Exception path: no-show vendor, failed inspection, missing part, access issue, budget approval delay, stale work order
- Current workaround: turn boards, spreadsheets, texts, calls, screenshots, and manual queue review in the PMS

### Customer Evidence

- Customer evidence:
  - `CE-B1-006`: operators describe maintenance coordination and approval work as a scaling headache
  - `CE-B1-007`: vendor communication still lives in texts and side threads
  - `CE-B1-010`: maintenance-coordinator roles already bundle the blocked-work control-tower job
- Vendor evidence:
  - `CE-B1-008` and `CE-B1-009`: PMS reviews still call out make-ready coordination friction and off-system follow-up
  - `CE-FP-027`: hospitality merge evidence shows the same room-turn recovery mechanics outside housing
- Atlas inference:
  - The defensible job is not work-order management. It is blocker diagnosis and readiness recovery for a revenue-generating unit.
- Confidence level: `High`

### Buyer Economics

- Frequency: every unit turn plus recurring stalled repair situations
- Annual customer impact: added vacancy days, delayed rent start, coordinator labor, repeat vendor trips, and avoidable resequencing
- ROI mechanism: shorten vacancy loss, raise on-time ready-date percentage, reduce coordinator time, lower repeat-trip cost
- Budget source: operations or property-management budget
- Buying trigger: missed ready-date clusters, occupancy pressure, labor scarcity, or vendor-management breakdowns
- Economic justification: a single avoided vacancy day on enough units can justify the product, but the budget case is still more operational than financial-control driven

### Competitive Landscape

- Current vendors: Yardi, Entrata, AppFolio, ResMan, Property Meld
- Workflow ownership: incumbents own work orders and task tracking, but not the full blocker-recovery loop across vendors, approvals, and inspections
- Incumbent strengths: embedded PMS position, existing maintenance modules, broad property workflows
- Incumbent weaknesses: weak ownership of exception context once work leaves the clean queue; coordination still leaks into texts, calls, and side boards
- Product boundaries: PMS tools track the work order; they do not reliably own off-platform recovery, resequencing, and accountability
- Likelihood incumbents solve this: `Medium-High`, which is why the committee keeps `W-002` below `W-001`

### Startup Thesis

A startup can win by becoming the readiness-recovery layer that predicts and surfaces blockers, assigns accountability, and compresses the time between slip risk and corrective action without replacing the PMS.

### Unknowns

- Is the core pain truly coordination failure rather than capex backlog, labor scarcity, or chronic vendor underperformance?
- Will operators buy a focused recovery layer, or rely on PMS add-ons and human coordinators?
- How fast can the wedge expand beyond multifamily into adjacent room-turn or asset-readiness categories without losing focus?

### Reasons To Pass

- PMS vendors may add enough blocker visibility to weaken a focused entrant.
- Some operators may tolerate the issue as an internal staffing problem rather than a software category.
- The line between scheduling software and human operations management may remain blurry.

### Validation Required

- Prove dedicated willingness to pay for readiness recovery rather than generic maintenance tooling
- Measure how often missed ready dates are fixable coordination failures rather than structural capex or labor shortages
- Validate whether accommodation-style room-turn evidence translates into real expansion potential
