# Atlas Concept Evidence

Last updated: 2026-08-10
Status: Active

## Purpose

This directory holds the active concept evidence system for Atlas.

It preserves the raw concept base, the curated analytical layer, the QA report, and the controlled vocabularies that make the concept corpus reusable without overwriting source evidence.

## Current Files

- `concepts_raw.csv`: immutable gold-source concept inventory
- `concepts_curated.csv`: one-to-one derived analytical layer
- `concepts_inventory_qa.md`: QA summary for coverage, duplicates, ambiguity, and review flags
- `job_taxonomy.csv`: canonical job definitions, example legacy variants, and concept counts
- `concept-schema.md`: logical concept schema
- `taxonomy-normalization.md`: normalization rules for the analytical layer
- `job-taxonomy.md`: canonical job and domain vocabulary

## Operating Policy

- Never overwrite or clean up `concepts_raw.csv`.
- `concepts_curated.csv` may evolve through versioned repository updates.
- The logical concept schema stays stable unless a decision-log entry explicitly changes it.
- The analytical layer implements the logical `Job` field as `Canonical Job` plus `Domain`.
- QA should be regenerated whenever the curated layer changes.

## Regeneration

Run `scripts/build_concepts_curated.py` from the repository root to rebuild:

- `knowledge/evidence/concepts/concepts_curated.csv`
- `knowledge/evidence/concepts/job_taxonomy.csv`
- `knowledge/evidence/concepts/concepts_inventory_qa.md`

The script assumes `knowledge/evidence/concepts/concepts_raw.csv` is the canonical raw source.
