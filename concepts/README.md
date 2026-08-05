# Atlas Concept Inventory

## Purpose

`data/concepts.csv` is Atlas's canonical concept inventory.

It preserves the raw concept layer extracted from the original Atlas ideation history as a durable repository artifact.

This file is the immutable gold source for the concept corpus.

## Core Rule

All future work is additive to the inventory, not destructive of it.

That means:

- Do not rewrite original concept wording.
- Do not merge similar concepts.
- Do not renumber concept IDs.
- Do not delete rows unless an exact duplicate is proven from source.
- Do record ambiguity in `Notes` rather than inventing missing detail.

## What Belongs Here

Each row in `data/concepts.csv` represents one concept exactly once.

Current columns:

- `Concept ID`
- `Concept`
- `Original Wording`
- `Session`
- `Batch`
- `Track`
- `Source`
- `Notes`

## What Does Not Belong Here

Derived metadata should live outside the canonical inventory.

Examples:

- classification
- primitives
- jobs
- opportunity families
- scoring
- venture recommendations
- clustering
- ranking

Those layers may reference `Concept ID`, but they must not overwrite source concepts.

## Naming And ID Policy

- IDs are permanent and sequential: `C-0001`, `C-0002`, ..., `C-0700`.
- Once assigned, an ID is never reused.
- If new source concepts are recovered later, append new IDs rather than renumbering existing rows.

## Versioning Policy

- Treat the inventory as append-only source material.
- Any material change requires an explicit Decision Log entry.
- If source recovery improves a row, preserve the same `Concept ID` and document the reason in the commit and, when relevant, in `Notes`.

## Ambiguity Policy

If the recovered source only provided a concept title, keep the title and note the limitation.

Do not infer missing explanation, customer, moat, or business model details from adjacent concepts.
