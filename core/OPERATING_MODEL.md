# Atlas Operating Model

Last updated: 2026-08-10
Status: Active

## Purpose

This manual defines how Atlas turns broad exploration into evidence-backed decisions without losing speed or strategic coherence.

## Repository Surfaces

Atlas v2 is organized around four surfaces:

- `core/`: durable doctrine and current state
- `knowledge/`: evidence, learned knowledge, case studies, and postmortems
- `execution/`: the live task/result/review loop
- `archive/`: historical discovery outputs and superseded operating documents

Active work should update the first three surfaces. The archive preserves lineage without cluttering active navigation.

## Research Methodology

1. Capture broadly before judging.
2. Separate facts, observations, interpretations, and hypotheses.
3. Look for repeated primitives and recurring behavioral patterns across ideas.
4. Cluster by underlying value engine, job, or mechanism rather than by industry label.
5. Prefer direct market, customer, usage, or operating evidence over abstract opinion.
6. Record contradicting evidence with the same visibility as supporting evidence.
7. When evidence is thin, recommend a validation step instead of a strategic rewrite.

## Concept Schema Standard

Atlas concept records must use `knowledge/evidence/concepts/concept-schema.md` as the canonical schema.

Atlas preserves two related layers:

- the logical concept record, which uses the eight required Concept Schema v1.0 fields
- the analytical curated CSV, which stores that logic in a normalized form and represents `Job` as `Canonical Job` plus `Domain`

Apply these operating rules:

1. Raw capture may start as loose notes, but promotion into the working concept set requires the full logical schema.
2. One concept record should describe one concept only.
3. If the primitive, job, customer, or wedge is unclear, do not force clustering yet; clarify the record first.
4. Confidence must reflect the evidence shown, not the attractiveness of the idea.
5. The schema may not drift silently; material changes require a decision-log entry and explicit versioning.

## Repository Execution Path

Apply these rules:

1. Use `/Users/abhil/Documents/Codex/repos/atlas-os` as the canonical writable Atlas checkout.
2. Start each new Atlas session by reading `core/BOOTSTRAP.md`.
3. Prefer local git for repository updates and publishing.
4. Treat a successful `git push` as the normal path that updates GitHub online.
5. Use browser editing or connector-based file writes only as fallback paths when local git publishing is unavailable.

## Artifact Ownership

Atlas follows a repository-first operating model. Git is the authoritative source of truth for active state, tasking, execution results, and review decisions.

- Chat owns `execution/TASK.md`, `execution/tasks/TASK-xxx.yaml`, `execution/REVIEW.md`, and `execution/reviews/TASK-xxx.md`.
- Work owns `execution/RESULT.md` and `execution/results/TASK-xxx.yaml`.
- Shared owns `core/STATE.md`.

## Lifecycle

`Draft -> In Progress -> Completed -> Approved/Rejected`

Apply these rules:

1. Create or update the task artifacts before execution starts.
2. Move the task to `In Progress` only when Work is actively executing it.
3. Record the result artifacts when execution reaches `Completed`.
4. Close the loop only after Chat records `Approved` or `Rejected`.

## Task Identity

- Use `TASK-001`, `TASK-002`, `TASK-003`, and so on.
- Reuse the same task ID across task, result, and review artifacts for traceability.

## Response Guidelines

Atlas outputs should follow these rules:

1. Best-answer-first: lead with the clearest recommendation or conclusion.
2. One recommendation by default: recommend the single best solution unless a genuine architectural tradeoff requires explicit alternatives.
3. Concise-first: keep the primary answer compact enough to act on quickly.
4. Evidence visible: state what supports the conclusion and what remains uncertain.
5. Hypotheses labeled: do not present a working theory as an earned principle.
6. Wedge explicit: show the believable entry point, not only the expansive vision.
7. Ignore list included when useful: say what should not be prioritized yet.

The default recommendation format is:

1. Recommendation
2. Why it matters
3. Evidence
4. Risks or missing proof
5. Next action

## Hypothesis Workflow

Atlas uses a staged knowledge ladder:

1. Observation: record a direct pattern when it appears.
2. Hypothesis: promote only after at least three independent observations support the same explanation.
3. Falsification: actively look for counterexamples or contradictory evidence.
4. Principle: promote only when the hypothesis survives repeated support and at least one serious attempt to disprove it.
5. Decision: when a strategy or operating choice is made, log it in `core/DECISION_LOG.md`.

Keep these stages separate. Early conviction is not evidence.

## Session Workflow

Every Atlas session should follow this loop:

1. Orient on `core/BOOTSTRAP.md`, `core/STATE.md`, and recent decisions.
2. Define or refresh the active task in `execution/TASK.md` and `execution/tasks/TASK-xxx.yaml`.
3. Capture or review new raw concepts, research, or evidence.
4. Update observations, hypotheses, or principles when thresholds are met.
5. Normalize active concepts into the canonical concept schema before clustering or comparison work.
6. Create or update any supporting case-study, postmortem, or evidence artifacts needed for the task.
7. Record execution output in `execution/RESULT.md` and `execution/results/TASK-xxx.yaml` when work completes.
8. Produce the best-answer-first recommendation.
9. Review the result in `execution/REVIEW.md` and `execution/reviews/TASK-xxx.md`.
10. Update touched source-of-truth documents in the same session, including `core/STATE.md` when state changes.
11. Log any material decision or strategic change before closing.

## Session Closeout Standard

An Atlas session is not complete until these questions are answered:

1. What changed in the knowledge base?
2. Did any hypothesis advance, weaken, or get falsified?
3. Did any strategic or process decision need a decision log entry?
4. Which source-of-truth documents were updated?
5. What is the next highest-leverage move?
