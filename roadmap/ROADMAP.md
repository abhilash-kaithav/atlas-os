# Roadmap

Last updated: 2026-08-05
Status: Active

## Current Phase

Atlas has completed its methodology and repository operating setup. The immediate phase is to execute the first Value Pattern Discovery pass on the curated concept base.

The goal is not to cluster all 700 ideas at once. The goal is to derive and test the first durable Value Pattern taxonomy that later family, research, and validation work can reuse.

## Current Priorities

1. Execute `TASK-001` Value Pattern Discovery from `data/concepts_curated.csv`.
2. Freeze the first Value Pattern taxonomy only after it passes the Atlas reasoning-model tests.
3. Preserve traceability from every Value Pattern back to the concept inventory.

## Next Milestones

1. Propose candidate Value Patterns from recurring causal logic in the curated concept base.
2. Test candidates against the six taxonomy tests and record weak fits and counterexamples.
3. Freeze the first versioned Value Pattern taxonomy.
4. Map concepts into Value Patterns and note unresolved edge cases.
5. Merge Value Patterns into larger strategic Opportunity Families.
6. Research the highest-potential families before committing to MVP work.

## Upcoming Discovery Work

Value Pattern Discovery should follow these rules:

1. Start from evidence, not naming intuition.
2. Classify by cause, not appearance.
3. Keep counterexamples, edge cases, and weak fits visible.
4. Revise the taxonomy before scaling if the first pass fails the reasoning-model tests.
5. Keep the raw concept layer immutable and the curated layer traceable.

## Major Decisions Already Made

1. The repository is the source of truth.
2. Broad generation precedes prioritization.
3. Recommendations should be concise and best-answer-first.
4. Evidence is required before strategy changes.
5. The raw and curated concept layers remain separate.
6. Atlas operating model v1.0 governs execution workflow.
7. Atlas reasoning model v1.0 governs methodology.

## Inputs Needed For The Next Phase

1. `data/concepts_curated.csv`
2. `data/concepts_inventory_qa.md`
3. `docs/ATLAS_REASONING_MODEL.md`
4. `atlas/tasks/TASK-001.yaml`
