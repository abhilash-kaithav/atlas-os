# Atlas Data Artifacts

## Current Files

- `concepts_raw.csv`: immutable gold-source concept inventory
- `concepts_curated.csv`: one-to-one derived concept layer for analysis
- `concepts_inventory_qa.md`: QA summary for coverage, duplicates, missing fields, unknowns, and review flags

## Operating Policy

- The raw file is never overwritten by curation work.
- The curated file may evolve through versioned repository updates.
- QA should be regenerated whenever the curated layer changes.

## Regeneration

Run `scripts/build_concepts_curated.py` from the repository root to rebuild:

- `data/concepts_curated.csv`
- `data/concepts_inventory_qa.md`

The script assumes `data/concepts_raw.csv` is the canonical raw source.
