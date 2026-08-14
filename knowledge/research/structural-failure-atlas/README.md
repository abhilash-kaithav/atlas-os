# Structural Failure Atlas

Last updated: 2026-08-14
Status: Active Phase 3 evidence layer

## Scope

- Source inputs: normalized Phase 1 census plus the Phase 2 workflow library only.
- No new industry research or solution ideation is included here.
- This folder is the durable Phase 3 analytical layer that sits on top of `knowledge/research/workflow-library/`.

## Deliverables

- `structural-failure-taxonomy.md`: the canonical failure vocabulary and scoring method.
- `workflow-structural-failure-classification.csv`: one row per canonical workflow with primary and secondary structural failures.
- `structural-failure-frequency-matrix.csv`: expanded failure × workflow × operating system × industry matrix.
- `structural-failure-atlas-v1.md`: the first full atlas with aggregate evidence for each recurring failure.
- `executive-summary.md`: concise Phase 3 summary for Phase 4 handoff.
- `scripts/build_structural_failure_atlas.py`: reproducible generator for every artifact in this folder.

## Counts

- Canonical workflows classified: 198
- Frequency-matrix rows: 709
- Structural failure categories: 8

## Top Failure Incidence

- `SF-03` Decision Context Escapes the Record: 174 workflows
- `SF-04` Human Judgment Under Incomplete Information: 116 workflows
- `SF-01` Exception-Path Breakdown: 77 workflows
- `SF-06` Plan vs. Reality Divergence: 53 workflows
- `SF-02` Cross-System Reconciliation: 42 workflows
