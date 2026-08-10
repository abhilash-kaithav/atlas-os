# Atlas Taxonomy Normalization v1.0

Last updated: 2026-08-05
Status: Active

## Purpose

This document defines the controlled vocabularies and normalization rules for `knowledge/evidence/concepts/concepts_curated.csv`.

The goal of the taxonomy pass is to make Atlas concepts comparable without changing the underlying concept inventory.

## Preservation Rules

- Do not add, remove, merge, or rename concepts during taxonomy normalization.
- Preserve `Concept ID`, `Concept Title`, `Clear Description`, `Original Wording`, and the raw inventory lineage.
- Use `Notes` when a concept is ambiguous instead of silently forcing precision that the raw wording does not support.

## Primitive Vocabulary

Each concept gets one primary primitive only.

- `Discover`: surfaces new opportunities, options, or weak signals.
- `Predict`: forecasts likely outcomes before they happen.
- `Verify`: establishes truth, quality, trust, or readiness.
- `Coordinate`: moves multi-step work across people, tools, or systems.
- `Compound`: makes each cycle increase the value of the next one.
- `Remember`: preserves and recalls context, history, and prior decisions.
- `Adapt`: updates plans or systems as conditions change.
- `Create`: turns intent or expertise into reusable outputs or assets.
- `Simulate`: tests scenarios before real-world commitment.
- `Optimize`: improves decisions, prioritization, or negotiated outcomes.
- `Match`: connects the right people, assets, knowledge, or opportunities.
- `Learn`: improves performance through feedback and repeated practice.

Rules:

- Prefer the most fundamental capability, not the surface workflow or product archetype.
- Do not introduce a new primitive silently.
- If a concept appears to need a thirteenth primitive, keep the best-fit existing primitive and record the ambiguity in `Notes`.

## Canonical Job And Domain Rules

The curated layer now stores `Canonical Job` and `Domain` separately instead of one mixed `Job` field.

`Canonical Job` should be:

- a customer outcome, not a product description
- concise and verb-led
- domain independent
- solution-independent

`Domain` should be:

- a controlled context label
- stable across similar concepts
- inferred from the concept context, not the product category

Examples:

- `Improve roadmap decisions.` -> `Canonical Job: Improve decisions`, `Domain: Product`
- `Preserve context for operating decisions.` -> `Canonical Job: Preserve context`, `Domain: Operations`
- `Coordinate workflow execution.` -> `Canonical Job: Coordinate work`, `Domain: Workflow`
- `Predict outcomes in physical operations.` -> `Canonical Job: Predict outcomes`, `Domain: Physical Operations`

See `job-taxonomy.md` for the full controlled vocabulary and normalization rules.

## Customer Rules

Customer values should identify one primary persona or role only.

Rules:

- Do not mix buyers, users, company sizes, and industries in one value.
- Prefer the narrowest credible role visible in the concept wording.
- If the source wording lists several audiences, select one primary role and record the simplification in `Notes`.

Examples of normalized customer roles:

- `Product manager`
- `Operations executive`
- `Operations manager`
- `Procurement leader`
- `Care coordinator`
- `Research scientist`
- `Public sector strategist`

## Initial Wedge Rules

`Initial Wedge` must be distinct from `Customer`.

Rules:

- `Customer` names the role.
- `Initial Wedge` names the starting segment, workflow, or operating context.
- Keep wedges narrow enough to test directly.
- If the raw wording only implies a broad starting point, preserve the best-fit wedge and flag it in `Notes`.

## Confidence Scale

Use integers only.

- `5`: exceptional; unusually strong framing and support
- `4`: strong; clear, coherent, and comparatively well supported
- `3`: coherent and worth analyzing
- `2`: speculative or materially under-specified
- `1`: weak; broad, malformed, or not yet credible enough without manual repair

Rules:

- Do not inherit enthusiasm from the original brainstorm.
- Reward clarity, specificity, and support.
- Penalize broadness, missing support, and forced taxonomy choices.

## Evidence Vocabulary

Use one controlled value only.

- `None`
- `Intuition`
- `Pattern Evidence`
- `Secondary Research`
- `Customer Voice`
- `Interview Evidence`
- `Behavioral Data`
- `Revenue Evidence`

Rules:

- `None` means the raw wording does not supply a meaningful support signal.
- `Intuition` means the concept is framed coherently but not grounded in explicit evidence.
- `Pattern Evidence` means the raw wording captures repeated workflow structure, comparative patterning, or explicit operating logic.
- Use stronger evidence labels only when the raw wording clearly points to that signal type.

## Notes And Manual Review

Use `Notes` to preserve ambiguity without corrupting the controlled vocabulary.

Flag rows when:

- primitive selection required judgment between nearby categories
- customer wording mixed multiple personas
- the wedge remains broad and needs manual narrowing
- the raw wording was too thin and the description had to fall back to the title
- confidence is `1` or `2`

## Operating Expectation

When this taxonomy changes, regenerate:

- `knowledge/evidence/concepts/concepts_curated.csv`
- `knowledge/evidence/concepts/concepts_inventory_qa.md`

Do not treat this document as permission to mutate the raw inventory.
