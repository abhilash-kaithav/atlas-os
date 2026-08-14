# Workflow Library

Last updated: 2026-08-14
Status: Active Phase 2 evidence layer

## Scope

- Source workflow universe: `knowledge/research/industry-census/top-50-industry-census-normalized.csv` only.
- Additional software research: official vendor and product pages reviewed to enrich the `What software exists today?` field without changing the workflow universe.
- Current-state mapping only. No opportunity analysis, solution design, or Phase 3 classification appears in this folder.

## Deliverables

- `canonical-workflow-library.csv`: one row per canonical workflow with the full Phase 2 anatomy.
- `workflow-operating-system-industry-index.csv`: one row per workflow-to-operating-system-to-industry linkage from Phase 1.
- `workflows/`: one document per canonical workflow.
- `software-research.md`: reusable current vendor-category support artifact.

## Counts

- Canonical workflows documented: 198
- Workflow usage index rows: 250
- Operating systems represented: 21
- Workflow families represented: 13
- Workflow records with additional vendor-research links: 194

## Notes

- The normalized Phase 1 census remains the source of truth for workflow names, operating systems, and industry mappings.
- The software layer is intentionally representative rather than exhaustive. It exists to keep Phase 2 grounded in the current market landscape without drifting into opportunity analysis.
