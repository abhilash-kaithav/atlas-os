# Opportunity Engine

Last updated: 2026-08-04
Status: Active design document

## Purpose

The opportunity engine is the operating core of Atlas. It is where broad idea generation becomes structured opportunity discovery, comparison, validation, and eventual MVP selection.

## What It Must Hold

The opportunity engine should preserve:

1. Raw ideas
2. Fusion ideas
3. Primitives
4. Clusters or opportunity families
5. Scores
6. Research
7. Validation work
8. MVP tracking

## Recommended Structure

```text
opportunity-engine/
├── README.md
├── ideas/
├── fusion-ideas/
├── primitives/
├── clusters/
├── scoring/
├── research/
├── validation/
└── mvp-tracking/
```

## Object Definitions

### Ideas

Raw ideas are the broad search layer.

Each idea record should eventually capture:

- idea ID
- title
- source or batch
- short description
- candidate primitive
- candidate cluster
- wedge hypothesis
- current status

### Fusion Ideas

Fusion ideas combine multiple patterns or mechanisms into a potential new category.

Each fusion record should capture:

- parent ideas or patterns
- reason the combination matters
- candidate category
- believable beachhead
- platform expansion path

### Primitives

Primitives are the irreducible capabilities beneath ideas.

Each primitive record should capture:

- primitive ID
- name
- definition
- sanity-check question
- representative ideas

### Clusters

Clusters are the strategic themes Atlas will compare and rank.

Each cluster should capture:

- cluster ID
- title
- underlying value engine
- related primitives
- related ideas
- revenue thesis
- evidence summary
- evidence gaps
- next validation step

### Scoring

Scoring should happen at the cluster level by default.

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

### MVP Tracking

MVP tracking keeps large visions grounded in a believable first wedge.

Each MVP record should capture:

- target user
- wedge problem
- core workflow
- success metric
- build status
- open risks

## Lifecycle

The default flow is:

1. Idea capture
2. Fusion and pattern synthesis
3. Primitive assignment
4. Cluster formation
5. Cluster scoring
6. Research
7. Validation
8. MVP selection and tracking

## Current Repository Note

`opportunities/` remains the live working inventory today. This directory defines the fuller structure Atlas should grow into as the engine becomes more formal.
