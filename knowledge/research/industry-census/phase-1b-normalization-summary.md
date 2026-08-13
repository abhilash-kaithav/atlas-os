# Phase 1B Normalization Summary

Last updated: 2026-08-13
Status: Completed

## Scope

- Source input: `knowledge/research/industry-census/top-50-industry-census.csv` only.
- No new industry research was added.
- No Phase 2 workflow mapping was started.
- No opportunity, gap, or startup analysis was introduced.

## Deliverables Created

- `knowledge/research/industry-census/top-50-industry-census-normalized.csv`
- `knowledge/research/industry-census/operating-system-taxonomy.md`
- `knowledge/research/industry-census/workflow-taxonomy.md`
- `knowledge/research/industry-census/systems-of-record-taxonomy.md`
- `knowledge/research/industry-census/phase-1b-normalization-summary.md`

## Normalization Counts

- Industries normalized: 50
- Canonical operating systems: 21
- Workflow-family vocabulary: 13 reusable families across all 250 workflow slots
- Systems-of-record category layer: generated for all 50 industries

## Validation

- Complete rows: 50 of 50
- Rows with missing fields: 0

- Missing-field flags: none

## Largest Operating-System Buckets

- Product Manufacturing and Lifecycle Operations: 7 industries
- Process Manufacturing and Throughput Control: 5 industries
- Retail and Service Commerce: 5 industries
- Asset Utilization and Lease Management: 3 industries
- Care Delivery and Reimbursement: 3 industries

## Largest Workflow Families

- Finance and Revenue Operations: 42 industry workflow slots across 36 canonical workflows
- Access, Intake, and Contracting: 27 industry workflow slots across 25 canonical workflows
- Planning and Allocation: 25 industry workflow slots across 17 canonical workflows
- Production and Asset Operations: 24 industry workflow slots across 15 canonical workflows
- Delivery and Service Execution: 23 industry workflow slots across 16 canonical workflows

## Active Census Layer

- Raw research snapshot remains preserved in `top-50-industry-census.csv`.
- The active normalized Phase 1 layer is `top-50-industry-census-normalized.csv`.
- Phase 2 should start from the normalized operating-system, workflow, and systems vocabulary rather than the raw labels.
