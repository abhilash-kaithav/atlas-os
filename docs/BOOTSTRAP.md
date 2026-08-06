# Atlas Bootstrap

Last updated: 2026-08-06
Status: Active first-read startup document

## Purpose

This is the first document every future Atlas session should read.

It is a startup guide, not a replacement for the underlying source-of-truth artifacts.

When prior chat history conflicts with the repository, the repository wins.

## Canonical Startup Sequence

1. Use the canonical Atlas checkout at `/Users/abhil/Documents/Codex/repos/atlas-os`.
2. Read this file before making any Atlas decision or edit.
3. Read `atlas/STATE.md`, `atlas/TASK.md`, and `docs/DECISION_LOG.md`.
4. Read `docs/CHARTER.md`, `docs/ATLAS_REASONING_MODEL.md`, and `docs/OPERATING_MANUAL.md`.
5. Read the active task YAML plus the relevant taxonomy, knowledge, and data artifacts for the work at hand.
6. Use local git as the default write and publish path.
7. Treat prior conversations as historical context only.

## Atlas In One Paragraph

Atlas is a repository-first operating system for discovering, classifying, validating, and acting on asymmetric opportunities with believable paths to durable value.

Its purpose is not to collect interesting ideas. Its purpose is to preserve evidence, derive reusable strategic knowledge, and surface the rare opportunity families worth building.

## Success Criteria

Atlas is successful when it can reliably:

1. preserve broad idea generation without losing strategic coherence
2. turn raw concepts into causal patterns, taxonomies, and evidence-backed priorities
3. keep recommendations concise, decision-ready, and traceable to evidence
4. surface believable wedges into large categories instead of collapsing into feature thinking
5. let future sessions resume from repository artifacts instead of reconstructing context from chat

## Active Constitutional Artifacts

Use these as the active governing set:

- `docs/CHARTER.md`: mission, scope, success definition, and governance
- `docs/ATLAS_REASONING_MODEL.md`: active methodology, laws, reasoning pipeline, and taxonomy tests
- `docs/OPERATING_MANUAL.md`: workflow, response rules, closeout standard, and operating model
- `docs/CODEX_WORKFLOW.md`: canonical repository and default local git publish path
- `docs/DECISION_LOG.md`: durable strategic and process decisions
- `docs/PRODUCT_BOUNDARY.md`: strategic boundary for what Atlas is and is not
- `atlas/STATE.md`: current milestone and next-step status
- `atlas/TASK.md`, `atlas/RESULT.md`, `atlas/REVIEW.md`: active execution loop
- `roadmap/ROADMAP.md`: current phase and forward milestones

Treat these as historical context, not active authority:

- `docs/ATLAS_CONSTITUTION.md`
- `docs/PLAYBOOK.md`
- `docs/AI_OPERATING_MANUAL.md`

## Current Atlas State On 2026-08-06

Atlas has completed the core setup required before discovery work:

- immutable gold-source concept inventory: complete
- one-to-one curated concept layer: complete
- primitive taxonomy: complete
- canonical job and domain taxonomy: complete
- Atlas operating model v1.0: complete
- Atlas reasoning model v1.0: complete
- bootstrap migration into the persistent Work environment: complete
- first Value Pattern taxonomy and full concept map: complete
- first Opportunity Family taxonomy and full family map: complete
- first Opportunity Family triage and ranked shortlist: complete

Atlas has now completed its third dedicated discovery task and is ready to move into top-family research.

### Active Next Task

- Task ID: `TASK-004`
- Title: `Top-Family Research: Decision and Foresight Infrastructure`
- Status: `Draft`
- State: not started

`TASK-003` is complete and approved. `TASK-004` is the next draft task and should research the top-ranked family, `OF-002 Decision and Foresight Infrastructure`, while keeping `OF-005 Capability Capital Platforms` as the backup lane.

## Product Boundary

Atlas is an opportunity discovery engine and opportunity intelligence system.

Atlas is not a startup accelerator, execution playbook library, or generic founder workflow coach.

Future work should improve opportunity discovery, strengthen the knowledge graph, or deepen the compounding moat. If the work mainly helps execute a startup after the opportunity is already chosen, it is outside the core Atlas boundary.

## Knowledge Architecture

Atlas should be read as layered architecture:

```text
data/concepts_raw.csv
    Immutable gold-source evidence

-> data/concepts_curated.csv
    One-to-one derived analytical layer

-> Controlled vocabularies
    Primitive taxonomy
    Canonical job taxonomy
    Domain taxonomy

-> Knowledge artifacts
    Observations
    Hypotheses
    Principles
    Decisions

-> Discovery layers
    Value Patterns
    Opportunity Families
    Scoring
    Research
    Validation
    Ventures
```

The rule is simple:

- evidence is preserved
- derived layers are traceable
- higher-order abstractions may evolve
- the raw layer does not get rewritten to make the abstractions look cleaner

## Data Snapshot

Current repository facts:

- `data/concepts_raw.csv`: 700 raw concepts
- `data/concepts_curated.csv`: 700 curated concepts with one-to-one ID coverage
- canonical jobs: 18
- domains: 20
- duplicate raw IDs: 0
- duplicate curated IDs: 0

The curated layer is usable, but not fully mature. The QA report still shows many low-confidence rows, broad wedges, and judgment-heavy primitive assignments. Atlas should preserve those imperfections visibly instead of hiding them with false precision.

## Frozen Architectural Commitments

Do not reopen these without new evidence and, when material, a decision log entry:

- Git and repository artifacts are the durable source of truth.
- `data/concepts_raw.csv` is the immutable gold source and primary intellectual property layer.
- `data/concepts_curated.csv` is a one-to-one derived interpretation layer, not a replacement for raw evidence.
- Structured concept work uses Concept Schema v1.0.
- Atlas classifies by cause, not appearance.
- Discovery follows the Atlas Reasoning Model pipeline.
- `opportunity-engine/value-patterns/README.md` and `value_pattern_map.csv` are the active first-pass Value Pattern layer above the concept schema.
- `opportunity-engine/opportunity-families/README.md` and `opportunity_family_map.csv` are the active second-pass Opportunity Family layer above Value Patterns.
- `opportunity-engine/scoring/README.md` and `opportunity_family_scores.csv` are the active family-prioritization layer above Opportunity Families.
- Atlas uses the task/result/review/state operating loop.
- Atlas scores and compares higher-order structures, not isolated flashy ideas, whenever family-level reasoning is available.

## Operating Discipline

These are the permanent working rules carried forward from the Chat -> Work transition:

- Repository-first: durable work ends in repository artifacts, not discussion alone.
- Immutable evidence: preserve raw concepts and contradictory evidence.
- Derived layers: taxonomies, summaries, mappings, and future pattern layers are additive and replaceable.
- One recommended solution by default: recommend the single best path unless a real architectural tradeoff exists.
- Evidence before redesign: do not reopen strategy or methodology because a new wording sounds better.
- Fast artifact production: architecture discussions should quickly produce repository updates.
- Git-mediated workflow: use the canonical checkout and normal git history instead of side channels.
- Separate architecture and implementation: define the method clearly, then execute it immediately instead of looping in abstraction.
- Minimize process churn: reuse the existing operating model unless new evidence justifies a change.

## Collaboration Contract For Future Atlas Sessions

Future Atlas work should behave this way by default:

- challenge assumptions with evidence
- recommend one best solution unless there is a genuine architectural tradeoff
- keep outputs concise, decision-ready, and traceable
- prefer repository updates over extended deliberation
- expose uncertainty instead of masking it
- record contradicting evidence with the same visibility as supporting evidence
- preserve current architecture unless evidence justifies a change
- treat prior conversations as historical context, not canonical memory

## Session Rules

Every future Atlas session should:

1. start from this bootstrap and the current repository state
2. confirm the active task or create the next task artifact before execution
3. use the reasoning model before naming new taxonomies or strategic abstractions
4. preserve traceability from conclusions back to concepts, QA, and evidence
5. update touched source-of-truth documents in the same session
6. log material strategic or process changes before closeout

An Atlas session is incomplete if it changes the thinking but leaves no durable repository artifact behind.

## Immediate Next Move

Begin `TASK-004` only when explicitly instructed to start execution.

That task should research `OF-002 Decision and Foresight Infrastructure`, identify the strongest wedge candidates inside that family, and preserve traceability back through `opportunity_family_scores.csv`, `opportunity_family_map.csv`, and `value_pattern_map.csv` to the concept inventory.
