# Atlas Opportunity Family Taxonomy v1.0

Last updated: 2026-08-06
Status: Active

## Purpose

This artifact defines the first Atlas Opportunity Family layer.

It sits above Value Patterns and below family scoring, research, validation, and ventures.

Its job is to merge the approved Value Pattern layer into larger strategic families that can be compared as believable opportunity spaces rather than isolated ideas.

## What An Opportunity Family Is

An Opportunity Family is a strategic group of Value Patterns that shares a larger value engine and revenue logic.

It is not a market theme or a loose topical cluster.

It is a higher-order abstraction that helps Atlas compare where durable opportunity may exist before committing to deeper research or venture design.

## Classification Rules v1.0

Atlas uses a fixed, reproducible first-pass rule set:

1. Use the concept's approved `Value Pattern ID` from `opportunity-engine/value-patterns/value_pattern_map.csv` as the reproducibility anchor.
2. Map each Value Pattern into exactly one Opportunity Family using the fixed family rules below.
3. Keep one primary Opportunity Family per concept in this version.
4. If a concept could plausibly support adjacent families later, preserve that ambiguity in review and research notes instead of rewriting the first-pass family assignment.
5. Preserve one-to-one traceability from every family assignment back through the Value Pattern layer to the curated concept inventory.

## Value Pattern To Family Mapping

| Value Pattern | Opportunity Family | Family Value Engine |
| --- | --- | --- |
| `VP-001 Workflow Compression` | `OF-001 Operational Execution Infrastructure` | Convert fragmented execution and lost context into faster operating throughput. |
| `VP-003 Memory Infrastructure` | `OF-001 Operational Execution Infrastructure` | Convert fragmented execution and lost context into faster operating throughput. |
| `VP-002 Decision Advantage` | `OF-002 Decision and Foresight Infrastructure` | Improve high-stakes choices before irreversible commitments are made. |
| `VP-008 Pre-Commitment Foresight` | `OF-002 Decision and Foresight Infrastructure` | Improve high-stakes choices before irreversible commitments are made. |
| `VP-004 Trust Infrastructure` | `OF-003 Trust and Adaptive Governance` | Lower the cost of action under uncertainty through proof, readiness, and re-alignment. |
| `VP-009 Adaptive Control` | `OF-003 Trust and Adaptive Governance` | Lower the cost of action under uncertainty through proof, readiness, and re-alignment. |
| `VP-005 Matching Liquidity` | `OF-004 Discovery and Liquidity Networks` | Widen the visible option set and route scarce resources toward better matches. |
| `VP-006 Opportunity Surface Expansion` | `OF-004 Discovery and Liquidity Networks` | Widen the visible option set and route scarce resources toward better matches. |
| `VP-007 Compounding Loops` | `OF-005 Capability Capital Platforms` | Turn repeated use, learning, and creation into reusable capability or intellectual capital. |
| `VP-010 Assetization Engines` | `OF-005 Capability Capital Platforms` | Turn repeated use, learning, and creation into reusable capability or intellectual capital. |

## Why This Taxonomy Passes The Atlas Tests

- Invariant: the families are defined by larger value engines, not by customer segment, market label, or interface.
- Distinct: each family has a different primary economic logic, so the taxonomy does not collapse into generic "AI products."
- Generative: the taxonomy covers all 700 approved Value Pattern rows and can accept future concepts by reusing the same Value Pattern anchor.
- Predictive: the family structure suggests where Atlas should look for underbuilt wedges, including adaptive trust systems, liquidity networks, and capability-capital products.
- Composable: future ventures may blend multiple families, but this version still preserves one primary family per concept for reproducibility.
- Economic: each family is grounded in a specific mechanism of throughput gain, judgment improvement, action-enabling trust, allocation efficiency, or retained capability capital.

## Family Set

### OF-001 Operational Execution Infrastructure

- Count: 210 concepts
- Related Value Patterns: `VP-001 Workflow Compression`, `VP-003 Memory Infrastructure`
- Source primitives: `Coordinate`, `Remember`
- Definition: systems that reduce recurring operating drag by compressing handoffs and preserving reusable context across multi-step work.
- Value engine: convert fragmented execution and lost context into faster cycle times, lower coordination overhead, and more repeatable operating throughput.
- Boundary: use this family when the core wedge is smoother recurring execution. If the primary value is better pre-commitment judgment, market matching, or capability compounding, use a different family.
- Revenue thesis: best wedges monetize as workflow systems, operating copilots, or memory layers priced against time saved, throughput gained, or avoided coordination headcount.
- Representative concepts: `C-0184 Workflow Genome`, `C-0620 Economic Operating Layer`, `C-0002 AI Company Memory`, `C-0086 Enterprise Knowledge Compiler`

### OF-002 Decision and Foresight Infrastructure

- Count: 166 concepts
- Related Value Patterns: `VP-002 Decision Advantage`, `VP-008 Pre-Commitment Foresight`
- Source primitives: `Optimize`, `Predict`, `Simulate`
- Definition: systems that improve high-stakes decisions before time, capital, or trust are committed.
- Value engine: raise judgment quality and reduce irreversible mistakes by turning weak signals, tradeoffs, and scenario uncertainty into clearer pre-commitment choices.
- Boundary: use this family when the primary value comes from better choices before action. If the wedge is ongoing execution throughput or post-decision adaptation, use a different family.
- Revenue thesis: best wedges monetize where wrong decisions are expensive, via decision support, simulation, and planning systems priced against margin preservation, risk reduction, or faster strategic cycles.
- Representative concepts: `C-0001 AI Operating System for Product Managers`, `C-0009 AI Procurement Negotiator`, `C-0007 AI Business Simulation Engine`, `C-0089 AI Collaboration Twin`

### OF-003 Trust and Adaptive Governance

- Count: 80 concepts
- Related Value Patterns: `VP-004 Trust Infrastructure`, `VP-009 Adaptive Control`
- Source primitives: `Verify`, `Adapt`
- Definition: systems that keep organizations, networks, or institutions credible and aligned as conditions change.
- Value engine: lower the cost of action under uncertainty by combining verification, readiness, and continuous re-alignment instead of static governance.
- Boundary: use this family when the wedge depends on proof, compliance, readiness, or re-tuning under change. If value mainly comes from discovery, matching, or capability accumulation, use a different family.
- Revenue thesis: best wedges monetize through risk, compliance, readiness, or resilience budgets where customers already pay to avoid failure, regulatory pain, or system drift.
- Representative concepts: `C-0085 AI Trust Engine`, `C-0590 Future Geography Layer`, `C-0630 National Resilience Index`, `C-0670 Trust Infrastructure`

### OF-004 Discovery and Liquidity Networks

- Count: 112 concepts
- Related Value Patterns: `VP-005 Matching Liquidity`, `VP-006 Opportunity Surface Expansion`
- Source primitives: `Match`, `Discover`
- Definition: systems that widen the visible option set and route scarce resources toward better matches.
- Value engine: create upside by increasing what the user can see and lowering the search friction required to turn discovery into allocation.
- Boundary: use this family when value comes from search breadth, routing, or match quality. If the wedge depends mainly on operational throughput or post-match compounding, use a different family.
- Revenue thesis: best wedges monetize through access fees, transaction take rates, or workflow subscriptions tied to higher fill-rate, better deal flow, or improved utilization.
- Representative concepts: `C-0003 AI Workflow Discovery Platform`, `C-0006 AI Customer Interview Platform`, `C-0100 AI Capability Exchange`, `C-0640 Space Economy Ledger`

### OF-005 Capability Capital Platforms

- Count: 132 concepts
- Related Value Patterns: `VP-007 Compounding Loops`, `VP-010 Assetization Engines`
- Source primitives: `Compound`, `Learn`, `Create`
- Definition: systems that turn repeated use, learning, and creation into reusable capability or intellectual capital.
- Value engine: build durable leverage by ensuring each cycle leaves behind skills, assets, or operating capital that makes the next cycle stronger.
- Boundary: use this family when the wedge gets stronger with repeated use or asset accumulation. If value is mostly one-time execution, a different family is a better fit.
- Revenue thesis: best wedges monetize through recurring subscriptions, asset-marketplace economics, or productivity capture where retained gains compound for the customer over time.
- Representative concepts: `C-0004 Enterprise AI Skills Coach`, `C-0088 AI Learning Graph`, `C-0222 Expertise-to-Business Platform`, `C-0236 AI Creator Intelligence`

## Outputs

- `opportunity-engine/opportunity-families/opportunity_family_map.csv`: one-to-one family classification map
- `opportunity-engine/opportunity-families/opportunity_family_summary.md`: generated family distribution and evidence-gap summary

## Current Limits

- This version preserves one primary Opportunity Family per concept even when a future venture may blend multiple families.
- Family assignment is reproducible because it is anchored to the approved Value Pattern layer, but many concepts still carry broad wedges or limited why-now evidence.
- Opportunity Family scoring should treat this taxonomy as a stable first comparison layer, not as proof that every family is equally attractive.
