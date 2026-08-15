# Batch 001 Methodology Rerun

Last updated: 2026-08-15
Status: Rerun complete under Atlas Research Program v1.0

## Why This Rerun Exists

Batch 001 was originally executed before the frozen v1.0 operating specification added:

- mandatory Phase 0 end-to-end workflow mapping
- mandatory Phase 0B completeness checks
- explicit validation gates
- the `YELLOW` status

This rerun applies the frozen methodology exactly and supersedes the earlier Batch 001 read.

## Workflow-Map References

- Housing -> [Industry Workflow Maps](./industry-workflow-maps.md)
- Administrative and support services -> [Industry Workflow Maps](./industry-workflow-maps.md)
- Food services and drinking places -> [Industry Workflow Maps](./industry-workflow-maps.md)

## Outcome Summary

| Industry | Workflow taken deepest | Prior status | Rerun status | Why |
| --- | --- | --- | --- | --- |
| Housing | Turnover and readiness management | GREEN | GREEN | The complete lifecycle map strengthened the wedge because the real failure still concentrates in post-plan blocker recovery before rent starts. |
| Administrative and support services | Payroll, billing, and reconciliation | GREEN | YELLOW | Frequency and economics remain good, but the customer-evidence base is still weaker than the strongest preserved wedges. |
| Food services and drinking places | Cash and inventory reconciliation | KILL | KILL | The full workflow map made the industry clearer, but the third-party settlement candidate still looked too occupied. |

## 1. Housing

- Phase 0 map: Leasing -> qualification -> contract setup -> occupancy -> maintenance -> billing/cash application -> turnover and readiness -> compliance/owner reporting -> renewal or closeout
- Completeness check: passed all six checks
- Pain surface scan: manual vendor follow-up, owner approvals, stale work orders, text and spreadsheet coordination, delayed ready dates, compliance and COI chasing
- Candidate workflow selected: `Turnover and Readiness Management`
- Competitive landscape: PMS and maintenance stacks handle intake and tracking; they do not clearly own blocker diagnosis once the ready date slips
- Customer reality: practitioner forums and G2 reviews still show missed handoffs, email coordination, and tricky make-ready workflows even inside modern property systems
- Incumbent boundary: workflow crosses vendors, inspections, parts, access, and approvals; the recovery loop lives outside the clean-path work order
- Buyer economics: extra vacancy days, delayed rent start, coordinator labor, repeat trips, resident dissatisfaction
- Why now: labor scarcity and vacancy sensitivity make missed ready dates more painful while mobile maintenance tooling makes the gap more legible
- Stress test: incumbents can add more tracking, but a neutral readiness-recovery layer still has to manage cross-team accountability rather than another PMS module
- Final status: `GREEN` as `W-002`

## 2. Administrative and Support Services

- Phase 0 map: Client intake -> recruiting and work assignment -> scheduling -> service execution and SLA monitoring -> payroll, billing, and reconciliation -> discrepancy recovery -> customer reporting -> renewal or closeout
- Completeness check: passed all six checks
- Pain surface scan: weekly timesheet chasing, rate mismatches, VMS approvals, manual discrepancy resolution, spreadsheet reconciliation, re-uploaded records, portal work
- Candidate workflow selected: `Payroll, Billing, and Reconciliation`
- Competitive landscape: Bullhorn, Avionté, Ascen, and adjacent suites own the clean path from time to pay/bill, but mismatch diagnosis still falls to humans
- Customer reality: reviews and job postings confirm that discrepancy investigation, approval chasing, and reconciliation remain dedicated work
- Incumbent boundary: truth is split across ATS, VMS, payroll, billing, and client-specific rules; incumbent suites reduce volume but do not own the exception desk
- Buyer economics: weekly payroll and invoice cycles, gross-margin leakage, delayed billing, extra back-office labor, cash-conversion drag
- Why now: tighter staffing margins and better APIs make an overlay more plausible
- Stress test: a category leader could improve workflow, but a startup still might win if it owns cross-system mismatch diagnosis better than the suite; this remains only partially proven
- Final status: `YELLOW` as `W-003`

## 3. Food Services and Drinking Places

- Phase 0 map: labor planning -> procurement and prep -> POS and order flow -> service execution -> cash and inventory reconciliation -> complaint and refund handling -> compliance and reporting -> close
- Completeness check: passed all six checks
- Pain surface scan: marketplace payout disputes, CSV exports, fragmented order and settlement views, manual auditing, payroll and DSS import issues
- Candidate workflow selected: `Cash and Inventory Reconciliation`
- Competitive landscape: Toast, Restaurant365, Square, Oracle MICROS, Otter, and the delivery platforms already span most of the boundary
- Customer reality: operator evidence confirms weekly manual settlement work, but the remaining gap looked incremental rather than wedge-defining
- Incumbent boundary: current players already control POS data, order aggregation, back-office accounting, and platform settlement interfaces
- Buyer economics: the pain is real but often tolerated through bookkeeping workarounds instead of net-new software
- Why now: delivery complexity increased, but so did incumbent product coverage
- Stress test: if Toast, Restaurant365, Otter, and the marketplaces prioritize the wedge, startup dominance is unlikely
- Final status: `KILL`

## Batch-Level Interpretation

- The new workflow-mapping requirement increased confidence in the outcomes but did not change the sign of the best and worst Batch 001 calls.
- The rerun did change one important judgment: `W-003` no longer deserves an automatic `GREEN` because it still clears recurrence and economics more strongly than it clears the customer-evidence and boundary gates.
