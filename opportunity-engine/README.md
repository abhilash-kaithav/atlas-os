# Opportunity Engine

Last updated: 2026-08-06
Status: Active design document

## Purpose

The opportunity engine is the operating core of Atlas. It is where broad concept generation becomes structured opportunity discovery, comparison, validation, and eventual venture selection.

## What It Must Hold

The opportunity engine should preserve:

1. Raw concepts
2. Concept schema records
3. Primitives
4. Value Patterns
5. Opportunity families
6. Scores
7. Research
8. Validation work
9. Ventures

## Recommended Structure

```text
opportunity-engine/
├── README.md
├── raw-concepts/
├── concept-records/
├── primitives/
├── value-patterns/
├── opportunity-families/
├── scoring/
├── research/
├── validation/
└── ventures/
```

## Object Definitions

### Raw Concepts

Raw concepts are the broad search layer.

They may begin as loose captures, but they are not ready for structured comparison until they are normalized into the official concept schema.

### Concept Schema Records

Every structured concept record must use `../schemas/concept-schema.md`.

Each concept schema record must contain exactly these eight fields:

- Concept
- Primitive
- Job
- Customer
- Value Mechanism
- Initial Wedge
- Confidence
- Evidence

This is the mandatory format for clustering, family formation, research, validation, and the representative 100-concept pilot.

Fusion concepts can still be explored, but they should be captured as raw concepts first and promoted only after they fit the schema cleanly.

### Primitives

Primitives are the irreducible capabilities beneath concepts.

Each primitive record should capture:

- primitive ID
- name
- definition
- sanity-check question
- representative concepts

### Value Patterns

Value Patterns are the first reusable economic layer above primitives.

They explain how value is created across many concepts before Atlas merges those concepts into larger strategic families.

Each Value Pattern artifact should capture:

- value pattern ID
- title
- definition
- economic mechanism
- source primitives
- representative concepts
- classification rules
- boundary notes
- counts and review flags

### Opportunity Families

Opportunity families are the strategic themes Atlas will compare and rank.

Each opportunity family should capture:

- family ID
- title
- underlying value engine
- related Value Patterns
- source primitives
- representative concepts
- revenue thesis
- evidence gaps
- next validation step

### Scoring

Scoring should happen at the opportunity-family level by default.

The default rubric should include:

- size of opportunity
- AI moat
- founder fit
- speed to MVP
- defensibility
- long-term platform potential
- revenue potential

Draft starting weights:

- size of opportunity: 20
- AI moat: 15
- founder fit: 15
- speed to MVP: 10
- defensibility: 15
- long-term platform potential: 15
- revenue potential: 10

When no durable founder-fit artifact exists yet, hold founder fit at a neutral score rather than inventing it from chat memory.

### Research

Research artifacts should answer:

- who already exists
- where the white space appears
- why now may be true
- what customer pain or urgency is visible
- what would invalidate the opportunity

### Validation

Validation tracks the cheapest credible tests.

Each validation record should capture:

- hypothesis being tested
- experiment or evidence source
- success signal
- failure signal
- result
- decision implied by the result

### Ventures

Ventures keep larger visions grounded in a believable first wedge and a concrete build path.

Each venture record should capture:

- target user
- wedge problem
- core workflow
- success metric
- build status
- open risks

## Lifecycle

The default flow is:

1. Raw Concept
2. Concept Schema
3. Value Pattern
4. Opportunity Family
5. Scoring
6. Research
7. Validation
8. Venture

## Current Repository Note

`opportunities/` remains the live working inventory today. `opportunity-engine/value-patterns/` is the active first discovery layer above the concept schema, `opportunity-engine/opportunity-families/` is the active second discovery layer above Value Patterns, and `opportunity-engine/scoring/` is the active family-ranking layer above Opportunity Families. Active research work should now begin from the approved scoring output rather than raw concept clustering.
