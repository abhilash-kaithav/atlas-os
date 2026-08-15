# Pattern Portfolio

Last updated: 2026-08-15
Status: Canonical cross-wedge pattern layer

## Purpose

This file tracks recurring atomic-job patterns across preserved wedges.

It is not a platform roadmap.

## Patterns

### P-001 Blocked Submission or Bill-Ready Record -> Diagnosis -> Correction -> Reflow

- Pattern type: `Exception -> investigation -> corrective loop`
- Description:
  - A submitted or bill-ready record fails to move forward because rules, mappings, proof, or approvals do not line up.
  - The value sits in finding the blocker quickly, assembling the missing evidence, correcting the record, and getting it back into flow before a time boundary is missed.
- Supporting wedges:
  - `W-001` construction pay-app rejection diagnosis and resubmission
  - `W-003` staffing pay/bill mismatch diagnosis and correction
  - `W-005` trucking billing and accessorial exception resolution
- Common mechanics:
  - external counterparty or client approval step
  - unclear or distributed error states
  - spreadsheets and email as exception memory
  - high sensitivity to payroll, billing, or cash-cycle deadlines

### P-002 Planned Ready Date -> Blocker Emerges -> Recovery Coordination

- Pattern type: `Plan -> deviation -> recovery`
- Description:
  - A team has a target revenue-ready or service-ready date.
  - Work is underway, but the real failure happens when dependencies slip and no tool clearly owns blocker resolution.
- Supporting wedges:
  - `W-002` housing make-ready turn blocker diagnosis and orchestration
  - `M-001` accommodation room-turn blocker coordination
- Common mechanics:
  - multiple vendors or contributors
  - local exception context outside the system of record
  - direct revenue loss tied to schedule slip

### P-003 Books-and-Records Break -> Investigation -> Pre-Reporting Resolution

- Pattern type: `Reconciliation -> investigation -> controlled close`
- Description:
  - Multiple systems agree on the happy path until a pricing, cash, or position break appears before reporting or close.
  - The valuable job is to identify the authoritative source, assemble support, and close the break before downstream reporting proceeds.
- Supporting wedges:
  - `W-004` capital-markets and fund-operations break triage
  - `M-002` securities settlement and investor-reporting merge
- Common mechanics:
  - multiple books and records
  - high trust and audit requirements
  - services-heavy incumbents with manual exception narratives

## Watch Pattern

### P-W01 Validated Category With Real Pain but Weak Net-New Point-Tool Buy

- Status: `Watch only`
- Observed in:
  - restaurant third-party settlement reconciliation
  - food and beverage deduction-management workflows
  - several professional-services and manufacturing candidates
- Why not promoted:
  - the workflow pain is real, but category leaders already own too much of the boundary or the remaining problem still prefers services
