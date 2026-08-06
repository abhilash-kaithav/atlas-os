# Atlas Value Pattern Taxonomy v1.0

Last updated: 2026-08-06
Status: Active

## Purpose

This artifact defines the first Atlas Value Pattern layer.

It sits above primitives and below Opportunity Families.

Its job is to explain how value is created economically across the concept inventory before Atlas merges concepts into larger strategic families.

## What A Value Pattern Is

A Value Pattern is a reusable economic pattern of value creation that remains stable across customers, products, domains, and implementations.

In practice, this means the pattern should describe the durable logic of the concept, not its market label or interface.

## Classification Rules v1.0

Atlas uses a fixed, reproducible first-pass rule set:

1. Use the concept's primary primitive from `data/concepts_curated.csv` as the reproducibility anchor.
2. Map that primitive into the corresponding Value Pattern.
3. Keep one primary Value Pattern per concept in this version.
4. If a concept could plausibly fit adjacent patterns, keep the primary primitive's pattern and preserve the ambiguity in review flags instead of forcing a different classification.
5. Preserve one-to-one traceability from every pattern assignment back to the concept inventory.

## Primitive To Pattern Mapping

| Primitive | Value Pattern | Economic Logic |
| --- | --- | --- |
| `Coordinate` | `Workflow Compression` | Reduce handoffs and execution drag in multi-step work. |
| `Optimize` | `Decision Advantage` | Turn noisy signals into better choices, tradeoffs, and negotiated outcomes. |
| `Remember` | `Memory Infrastructure` | Make prior context and rationale reusable in future work. |
| `Verify` | `Trust Infrastructure` | Produce proofs, checks, and readiness signals that unlock action. |
| `Match` | `Matching Liquidity` | Lower search friction and route the right resources faster. |
| `Discover` | `Opportunity Surface Expansion` | Search a wider option space and surface better openings earlier. |
| `Compound`, `Learn` | `Compounding Loops` | Make each cycle increase the value of the next through feedback or retained gains. |
| `Predict`, `Simulate` | `Pre-Commitment Foresight` | Reduce uncertainty before time, capital, or trust are committed. |
| `Adapt` | `Adaptive Control` | Keep plans and systems aligned as conditions change. |
| `Create` | `Assetization Engines` | Convert intent or expertise into reusable assets. |

## Why This Taxonomy Passes The Atlas Tests

- Invariant: the patterns are phrased as economic mechanisms, not market categories.
- Distinct: each pattern has a different primary value-creation logic and boundary condition.
- Generative: the taxonomy covers all 700 curated concepts and can classify future concepts through explicit rules.
- Predictive: the patterns suggest missing opportunities, such as new trust layers, matching networks, or compounding systems in under-covered domains.
- Composable: a future concept can combine patterns, but this version still preserves one primary pattern for reproducibility.
- Economic: every pattern explains value through decision quality, cycle-time reduction, uncertainty reduction, compounding, search-cost reduction, or asset reuse.

## Pattern Set

### VP-001 Workflow Compression

- Count: 141 concepts
- Source primitives: `Coordinate`
- Definition: reduce handoffs and coordination drag so multi-step work moves faster across people, tools, or systems.
- Boundary: the core value is execution throughput, not memory preservation or decision quality by itself.
- Representative concepts: `C-0008 AI Consultant Platform`, `C-0105 AI HOA Manager`, `C-0334 New Parent Intelligence`

### VP-002 Decision Advantage

- Count: 126 concepts
- Source primitives: `Optimize`
- Definition: turn noisy signals into better choices, tradeoffs, and negotiated outcomes before value leaks away.
- Boundary: the core value is better judgment or prioritization, not explicit forecasting or workflow orchestration.
- Representative concepts: `C-0001 AI Operating System for Product Managers`, `C-0009 AI Procurement Negotiator`, `C-0262 Decision Replay Engine`

### VP-003 Memory Infrastructure

- Count: 69 concepts
- Source primitives: `Remember`
- Definition: make prior context, rationale, and history reusable so future work does not restart from zero.
- Boundary: the core value is durable recall and context continuity, not merely documentation as an end in itself.
- Representative concepts: `C-0002 AI Company Memory`, `C-0173 Knowledge Velocity Platform`, `C-0503 Community Memory`

### VP-004 Trust Infrastructure

- Count: 69 concepts
- Source primitives: `Verify`
- Definition: produce proofs, checks, scores, or readiness signals that let people act with less uncertainty and lower error.
- Boundary: the core value is validation and action-enabling proof, not prediction or optimization alone.
- Representative concepts: `C-0018 Company Health Score`, `C-0265 AI Technical Due Diligence`, `C-0670 Trust Infrastructure`

### VP-005 Matching Liquidity

- Count: 57 concepts
- Source primitives: `Match`
- Definition: connect the right people, assets, opportunities, or capacity at the right time.
- Boundary: the core value is improved allocation and market-like fit, not direct workflow automation.
- Representative concepts: `C-0012 Digital Employee Marketplace`, `C-0252 AI Local Business Network`, `C-0625 National Talent Reserve`

### VP-006 Opportunity Surface Expansion

- Count: 55 concepts
- Source primitives: `Discover`
- Definition: search a wider option space than manual exploration and surface higher-value openings earlier.
- Boundary: the core value is expanding what Atlas or the user can see, not validating or executing the opportunity.
- Representative concepts: `C-0003 AI Workflow Discovery Platform`, `C-0232 AI Research Studio`, `C-0655 Discovery Exchange`

### VP-007 Compounding Loops

- Count: 127 concepts
- Source primitives: `Compound`, `Learn`
- Definition: make each cycle increase the value of the next through feedback, practice, retained gains, or cumulative capability.
- Boundary: the core value is repeated-use reinforcement, not one-time task completion or static knowledge storage.
- Representative concepts: `C-0228 AI Career Compounder`, `C-0490 Identity Compounder`, `C-0513 Energy Planning`

### VP-008 Pre-Commitment Foresight

- Count: 40 concepts
- Source primitives: `Predict`, `Simulate`
- Definition: forecast or test outcomes before time, capital, or trust are committed in the real world.
- Boundary: the core value is uncertainty reduction before action, not post-hoc verification.
- Representative concepts: `C-0007 AI Business Simulation Engine`, `C-0220 Economic Weather Forecast`, `C-0649 Economic Simulation Layer`

### VP-009 Adaptive Control

- Count: 11 concepts
- Source primitives: `Adapt`
- Definition: keep plans, contracts, or operating systems aligned as conditions change.
- Boundary: the core value is continuous re-alignment after change, not static planning before change.
- Representative concepts: `C-0576 Adaptive Contracts`, `C-0618 Business Evolution Engine`, `C-0698 Adaptive Institutions`

### VP-010 Assetization Engines

- Count: 5 concepts
- Source primitives: `Create`
- Definition: turn expertise, intent, or operating work into reusable assets that can be deployed repeatedly.
- Boundary: the core value is reusable capital formation, not simply faster execution or improved learning.
- Representative concepts: `C-0147 AI Workforce Composer`, `C-0236 AI Creator Intelligence`, `C-0295 AI Business Composer`

## Outputs

- `opportunity-engine/value-patterns/value_pattern_map.csv`: one-to-one concept classification map
- `opportunity-engine/value-patterns/value_pattern_summary.md`: generated distribution and review-flag summary

## Current Limits

- This version preserves one primary Value Pattern per concept even when a concept is clearly composable.
- The mapping is reproducible, but many concepts still have low underlying concept confidence or broad wedges.
- Opportunity Family formation should treat this taxonomy as a stable first pass, not as proof that every concept is commercially strong.
