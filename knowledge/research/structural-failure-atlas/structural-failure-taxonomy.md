# Structural Failure Taxonomy

Last updated: 2026-08-14
Status: Active Phase 3 taxonomy

## Method

- Source inputs: `knowledge/research/industry-census/top-50-industry-census-normalized.csv`, `knowledge/research/workflow-library/canonical-workflow-library.csv`, and `knowledge/research/workflow-library/workflow-operating-system-industry-index.csv` only.
- No additional external research was added.
- Each workflow is assigned one primary structural failure and up to two secondary structural failures using deterministic scoring on the Phase 2 friction fields, workflow family, and existing Phase 2 root-cause label.
- Minimum score to retain a failure on a workflow: `6`.

## Taxonomy

| Code | Failure | Definition | Typical evidence cues | Workflow incidence | Primary assignments | Confidence |
| --- | --- | --- | --- | ---: | ---: | --- |
| SF-01 | Exception-Path Breakdown | The core system handles the standard path, but economics and control break down when real-world exceptions enter the flow. | Edge cases, clean-path automation, exception triage, shortage recovery, and nonstandard scenarios. | 77 / 198 | 33 | Medium-High |
| SF-02 | Cross-System Reconciliation | Teams must reconstruct truth by matching records, statuses, balances, or evidence across multiple systems, ledgers, and counterparties. | Manual matching, books-and-records alignment, settlement breaks, version truth, data lineage, and audit-trail rebuilds. | 42 / 198 | 17 | Medium-High |
| SF-03 | Decision Context Escapes the Record | The decisive context for advancing work lives outside the formal system of record in email, calls, spreadsheets, decks, notes, or portals. | Spreadsheets, calls, side notes, message threads, portals, decks, whiteboards, and manual trackers carry the real state. | 174 / 198 | 49 | High |
| SF-04 | Human Judgment Under Incomplete Information | Progress depends on experienced people interpreting incomplete, noisy, or conflicting signals and choosing tradeoffs. | Interpretation, materiality, severity, trust, risk, prioritization, fit, and tradeoff decisions remain human-led. | 116 / 198 | 36 | High |
| SF-05 | Handoff and Approval Latency | Work slows or stalls when responsibility crosses functions, approvers, organizations, or service teams. | Approvals, sign-offs, layered review, cross-functional waiting, status chasing, and repeated handoffs. | 40 / 198 | 15 | Medium-High |
| SF-06 | Plan vs. Reality Divergence | A published plan or baseline becomes stale quickly as demand, capacity, field conditions, or network state change. | Local reality, live execution, unstable demand, rerouting, field conditions, readiness, and replanning loops. | 53 / 198 | 22 | Medium-High |
| SF-07 | Compliance and Evidence Burden | A large share of work is spent collecting proof, documenting exceptions, and maintaining traceability for rules, audits, or formal reporting. | Evidence collection, traceability, audit trails, regulatory proof, documentation, verification, certification, and controls. | 29 / 198 | 19 | Medium |
| SF-08 | Multi-Party Trust and Dependency Gaps | The workflow depends on outside parties whose data, incentives, timing, or standards do not align with the incumbent system. | Partner data, payers, carriers, suppliers, counterparties, external verification, and negotiated trust. | 28 / 198 | 7 | Medium |
