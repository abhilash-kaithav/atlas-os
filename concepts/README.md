# Atlas Concept Inventory

## Purpose

Atlas now uses a two-layer concept inventory model:

- `data/concepts_raw.csv` is the immutable gold source.
- `data/concepts_curated.csv` is the derived analytical layer.

The split preserves original intent while making the concept corpus usable for schema-based review, comparison, and future clustering.

## File Roles

`data/concepts_raw.csv`

- Canonical raw inventory recovered from Atlas ideation history.
- Preserves original wording, chronology, IDs, and source links.
- May only change through append-only source recovery or a path rename that does not alter row content.

`data/concepts_curated.csv`

- One-to-one derived layer for structured analysis.
- Adds normalized schema fields and analytical metadata.
- Must preserve `Concept ID`, keep `Original Wording` exact, and map every raw row to exactly one curated row.

`data/concepts_inventory_qa.md`

- QA report for row counts, ID coverage, duplicate checks, unknown normalization counts, and ambiguous rows that still need review.

## Core Rules

- Never overwrite or "clean up" `data/concepts_raw.csv`.
- Never merge, delete, or renumber concepts in either layer.
- Preserve `Concept ID` exactly.
- Preserve `Original Wording` exactly in the curated layer.
- Record ambiguity in `Notes` instead of inventing certainty.
- Mark unknown `Track` or `Batch` values explicitly in the curated layer when they cannot be recovered from source.

## Raw Schema

`data/concepts_raw.csv` keeps the recovered source columns:

- `Concept ID`
- `Concept`
- `Original Wording`
- `Session`
- `Batch`
- `Track`
- `Source`
- `Notes`

## Curated Schema

`data/concepts_curated.csv` keeps one derived row per raw concept with these columns:

- `Concept ID`
- `Concept Title`
- `Clear Description`
- `Track`
- `Batch`
- `Primitive`
- `Job`
- `Customer`
- `Value Mechanism`
- `Initial Wedge`
- `Confidence`
- `Evidence`
- `Why Now`
- `Notes`
- `Raw Source ID`
- `Original Wording`

The schema fields align with `schemas/concept-schema.md`, while the extra columns preserve lineage and curation context.

## Versioning

- Treat `data/concepts_raw.csv` as append-only source material.
- Treat `data/concepts_curated.csv` as a versioned interpretation layer that can improve over time.
- Any curated update should happen in a normal repository commit so the evolution of titles, primitives, wedges, and notes stays auditable.

## Build Path

Use `scripts/build_concepts_curated.py` to regenerate the curated CSV and QA report from the raw source.

That script is intentionally conservative:

- it does not modify the raw file
- it preserves one-to-one ID coverage
- it marks unresolved ambiguity in `Notes` and the QA report
