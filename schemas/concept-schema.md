# Atlas Concept Schema v1.0

Last updated: 2026-08-05
Status: Active

## Purpose

This schema is the canonical format for every Atlas concept record.

It exists to make concepts comparable, clusterable, reviewable, and automatable without changing field meanings from record to record.

## Scope

- Every concept that enters structured Atlas analysis must use this schema.
- The schema is mandatory for the representative 100-concept pilot.
- Raw captures may begin as loose notes, but they must be normalized into this schema before they are compared, clustered, researched, or validated.

## Required Fields

Every concept record must include exactly these eight required fields:

1. Concept
2. Primitive
3. Job
4. Customer
5. Value Mechanism
6. Initial Wedge
7. Confidence
8. Evidence

## Field Definitions And Rules

### 1. Concept

The concise statement of the opportunity being evaluated.

Rules:

- Name one concept only.
- Prefer behavior-first language over branding, feature lists, or broad market categories.
- Write it so another reader can distinguish it from adjacent concepts without reading the rest of the record.

### 2. Primitive

The irreducible behavior, capability, or value unit that actually makes the concept work.

Rules:

- Choose the primary primitive only.
- Phrase it as the reusable underlying unit, not the surface industry.
- If the primitive disappeared, the concept should no longer make sense.

### 3. Job

The specific progress the customer is trying to make when they would use or buy the concept.

Rules:

- Express the job as an outcome, not as a product description.
- Keep it narrow enough to compare across concepts.
- Prefer one core job per record.

### 4. Customer

The initial user or buyer with the clearest urgency for the job.

Rules:

- Name a concrete user, team, or buyer type.
- Avoid vague labels such as "everyone," "businesses," or "consumers."
- Default to the narrowest credible starting customer, not the eventual expansion market.

### 5. Value Mechanism

The way the concept creates value for the customer and, where visible, the path by which Atlas could capture value.

Rules:

- Describe the mechanism, not just the benefit claim.
- Explain what changes for the customer when the concept works.
- Prefer operational language such as saved time, increased throughput, reduced error, improved decision quality, or unlocked revenue.

### 6. Initial Wedge

The believable first entry point where the concept can win before broad expansion.

Rules:

- Define a narrow segment, workflow, or use case.
- Make it specific enough to test directly.
- The wedge should be credible without requiring total market transformation.

### 7. Confidence

The current confidence level that the concept is coherent, correctly framed, and worth continued comparison.

Rules:

- Use an integer from 1 to 5 only.
- Calibrate the score against the current evidence, not enthusiasm.
- Use the scale consistently:
  - 1 = speculative
  - 2 = weak signal
  - 3 = plausible
  - 4 = strong support
  - 5 = validated

### 8. Evidence

The concrete signals that support, weaken, or contextualize the concept.

Rules:

- Record direct observations, market facts, user signals, workflow proof, competitor patterns, or contradictory evidence.
- Prefer short bullets with source and date when known.
- Include contradictory evidence when it exists.
- If there is no evidence yet, keep the concept in raw capture instead of promoting it into the representative 100-concept pilot.

## Validation Rules

1. All eight fields are mandatory for every concept record.
2. One record must describe one concept only.
3. `Primitive`, `Job`, `Customer`, `Value Mechanism`, and `Initial Wedge` must be specific enough that two reviewers could compare concepts side by side without reinterpretation.
4. `Confidence` must be an integer from 1 to 5 and must not overstate the evidence shown.
5. `Evidence` must contain at least one concrete signal before a concept can enter the representative 100-concept pilot.
6. Concepts missing a credible `Primitive` or `Initial Wedge` remain raw concepts and are not ready for clustering.
7. New fields may not be added to v1.0 concept records during the representative 100-concept pilot.
8. Field meanings may not be redefined during the representative 100-concept pilot; any revision requires a new schema version and a decision log entry.

## Canonical Template

```text
Concept:
Primitive:
Job:
Customer:
Value Mechanism:
Initial Wedge:
Confidence:
Evidence:
- 
```

## Example

```text
Concept: Renewal risk briefing for customer-success managers
Primitive: Decision draft
Job: Help an account owner decide which at-risk renewals need action this week
Customer: Mid-market SaaS customer-success manager
Value Mechanism: Converts noisy account signals into a prioritized intervention brief that saves analysis time and improves retention focus
Initial Wedge: Customer-success teams managing 50 to 200 accounts without a dedicated RevOps analyst
Confidence: 3
Evidence:
- Customer-success teams routinely review churn-risk spreadsheets and call notes before renewal meetings.
- Existing tools often surface scores, but many teams still assemble manual account briefs.
- Contradicting signal: larger enterprise teams may already have analytics coverage that weakens the wedge.
```

## Versioning

- `v1.0` is frozen for the representative 100-concept pilot.
- During the pilot, every structured concept record must use these eight fields exactly as defined here.
- If Atlas learns that the schema itself should change, record that decision in `docs/DECISION_LOG.md` and create a new schema version rather than mutating `v1.0`.
