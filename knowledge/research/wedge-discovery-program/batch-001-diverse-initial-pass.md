# Batch 001 Diverse Initial Pass

Last updated: 2026-08-14
Status: Completed batch

## Batch Scope

This first program batch intentionally avoided repeating construction and instead covered three different operating systems:

- `Housing`
- `Administrative and support services`
- `Food services and drinking places`

## Outcome Summary

| Industry | Primary workflow investigated | Atomic candidate preserved? | Final status |
| --- | --- | --- | --- |
| Housing | Turnover and Readiness Management | Yes | GREEN |
| Administrative and support services | Payroll, Billing, and Reconciliation | Yes | GREEN |
| Food services and drinking places | Cash and Inventory Reconciliation | No | KILL |

## 1. Housing

### Orientation

- Operating system: `Asset Utilization and Lease Management`
- Workflows prioritized:
  - `Turnover and Readiness Management`
  - `Asset Maintenance and Work Orders`
  - `Billing, Collections, and Cash Application`
- Structural failure focus:
  - `SF-06 Plan vs. Reality Divergence`
  - `SF-03 Decision Context Escapes the Record`
  - `SF-05 Handoff and Approval Latency`

### Market Landscape

- Category leaders / incumbents:
  - AppFolio
  - Entrata
  - Yardi
  - ResMan
- Specialist products:
  - Property Meld
  - maintenance add-ons and vendor tools
- What they solve well:
  - maintenance request intake
  - work-order tracking
  - resident communication
  - basic make-ready visibility
- What remains outside the boundary:
  - stale vendor follow-up
  - owner approval bottlenecks
  - live blocker accountability
  - unit-ready-date recovery when dependencies slip

### Customer Reality

- BiggerPockets operators repeatedly describe maintenance coordination as the real bottleneck, not request intake.
- ResMan and Entrata users still mention make-ready friction, extra work-order handling, or email/screenshot coordination.
- Property Meld exists precisely because many operators still need a dedicated maintenance coordination layer.

### Atomic Candidate Narrowing

- KILL: generic maintenance coordination
  - Too broad and already heavily represented by PMS and maintenance suites.
- KILL: vendor COI / compliance tracking as a standalone company boundary
  - Real pain, but too narrow and too subordinate to broader maintenance operations.
- GREEN: make-ready turn blocker diagnosis and readiness orchestration
  - Preserved as `W-002`.

### Why It Survived

- Buyer is clear.
- Pain is recurring every turn.
- Economic harm is direct through extra vacancy days and delayed rent start.
- Current systems track the work, but not the real blocker-resolution loop once the plan slips.
- A startup could enter as a cross-system readiness recovery layer without replacing the PMS.

### Evidence Strength

`High`

## 2. Administrative and Support Services

### Orientation

- Operating system: `Workforce Coordination and Service Operations`
- Workflows prioritized:
  - `Payroll, Billing, and Reconciliation`
  - `Recruiting and Work Assignment`
  - `Workforce Scheduling`
- Structural failure focus:
  - `SF-02 Cross-System Reconciliation`
  - `SF-01 Exception-Path Breakdown`
  - `SF-03 Decision Context Escapes the Record`

### Market Landscape

- Category leaders / incumbents:
  - Bullhorn
  - Avionte
  - broader ATS plus payroll stacks
- Specialists:
  - Ascen
  - emerging staffing middle-office tools
- What they solve well:
  - time capture
  - pay-and-bill workflow on the clean path
  - placement and assignment records
- What remains outside the boundary:
  - client-specific approval problems
  - VMS mismatches
  - rate and shift discrepancies
  - neutral diagnosis of why approved time still cannot close cleanly

### Customer Reality

- Bullhorn still shows user pain around vendor-specific onboarding and manual record re-upload.
- Avionte users still report fragility in reporting and operational visibility for weekly time workflows.
- Job postings for billing operations coordinators and payroll/billing specialists explicitly center on discrepancy investigation and manual resolution.

### Atomic Candidate Narrowing

- KILL: broad staffing middle-office replacement
  - Too broad and too close to current suite categories.
- KILL: onboarding document correction as the first beachhead
  - Real, but too entangled with front-office and compliance surfaces rather than the most direct finance pain.
- GREEN: staffing pay/bill mismatch diagnosis and correction before payroll and invoicing
  - Preserved as `W-003`.

### Why It Survived

- Buyer is clear and already paying people to do this work manually.
- The event is recurring on weekly payroll cycles.
- The ROI is measurable via payroll accuracy, invoice timing, and gross-margin protection.
- Current suites reduce admin load, but the mismatch-resolution desk still exists because truth is split across client, VMS, ATS, payroll, and invoice systems.

### Evidence Strength

`Medium`

## 3. Food Services and Drinking Places

### Orientation

- Operating system: `Retail and Service Commerce`
- Workflow prioritized:
  - `Cash and Inventory Reconciliation`
- Structural failure focus:
  - `SF-02 Cross-System Reconciliation`
  - `SF-01 Exception-Path Breakdown`

### Market Landscape

- Category leaders / incumbents:
  - Toast
  - Restaurant365
  - Square
  - Oracle MICROS
- Specialists / adjacencies:
  - Otter
  - delivery aggregators
  - bookkeeping and accounting services
- What they solve well:
  - POS capture
  - daily sales reporting
  - GL mapping
  - order aggregation
  - back-office accounting suites
- What remains outside the boundary:
  - settlement disputes
  - payout timing mismatches
  - partner-level credits and fee disputes

### Customer Reality

- Operators say third-party delivery accounting is time-consuming and can require several hours per week.
- Restaurant365 users still report payroll integration and DSS import issues.
- Otter users still need CSV exports and process workarounds even with order aggregation.

### Atomic Candidate Narrowing

- KILL: general restaurant close and reconciliation
  - Too broad.
- KILL: third-party delivery payout and settlement reconciliation as the first beachhead
  - Pain is clear, but the wedge looked too occupied by the combined footprint of POS, back-office suites, aggregators, and delivery platforms.

### Why It Was Killed

- The buyer is real, but the incremental software buy looked weak.
- The leading incumbents already span most of the workflow boundary.
- The likely startup surface is at risk of being absorbed by Toast, Restaurant365, Otter, or the marketplaces themselves.
- Services and bookkeeping workarounds may remain "good enough" for many buyers.

### Evidence Strength

`Medium-High`

## Batch Learnings

- Two `GREEN` wedges came from secondary correction or recovery loops, not primary systems.
- The strongest `KILL` in this batch still contained obvious pain, which reinforces that pain alone is not enough.
- The portfolio now has repeated evidence for one recurring pattern: blocked operational flow -> diagnosis -> evidence gathering -> correction.
