# Pattern Portfolio

Last updated: 2026-08-14
Status: Canonical cross-wedge pattern layer

## Purpose

This file tracks recurring atomic-job patterns across `GREEN` wedges.

It is not a platform roadmap.

It is a pattern memory layer that may later support a comparative investment analysis.

## Patterns

### P-001 Blocked Submission -> Diagnosis -> Correction -> Resubmission

- Pattern type: `Exception -> investigation -> corrective loop`
- Description:
  - A submitted or approval-ready record fails to advance because one or more requirements, mappings, or approvals do not line up.
  - The economic value sits in diagnosing the blocker quickly, gathering the missing evidence, and getting the corrected item back into flow before a time boundary is missed.
- Supporting wedges:
  - `W-001` construction pay-app rejection diagnosis and resubmission
  - `W-003` staffing pay/bill mismatch diagnosis and correction
- Common mechanics:
  - external counterparty or client approval step
  - unclear error states
  - spreadsheets and email as exception memory
  - high sensitivity to cycle deadlines
- Why it matters:
  - This is the clearest repeated pattern so far where existing systems validate the market but do not fully own the correction loop.

### P-002 Planned Ready Date -> Blocker Emerges -> Recovery Coordination

- Pattern type: `Plan -> deviation -> recovery`
- Description:
  - A team has a target service-ready or revenue-ready date.
  - Work is technically underway, but the real failure happens when dependencies slip and no tool clearly owns blocker resolution.
- Supporting wedges:
  - `W-002` housing make-ready turn blocker diagnosis and orchestration
- Common mechanics:
  - multiple vendors or contributors
  - local exception context outside the system of record
  - revenue loss tied directly to schedule slip
- Why it matters:
  - This pattern may recur in other asset-heavy or field-heavy industries even when the underlying domain is different.

## Watch Pattern

### P-W01 Multi-Source Settlement Reconciliation Against External Counterparty Truth

- Status: `Watch only`
- Observed in:
  - killed restaurant third-party delivery settlement candidate
  - earlier freight and monetization research
- Why not promoted:
  - Atlas has not yet preserved a `GREEN` wedge in this pattern family
  - current boundaries still look too occupied or too weakly budgetable
