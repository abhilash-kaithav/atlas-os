# Operating Manual

Last updated: 2026-08-05
Status: Active

## Purpose

This manual defines how Atlas turns broad exploration into evidence-backed decisions without losing speed or strategic coherence.

## Decision Framework

When evaluating an idea, cluster, or strategic move, answer these questions in order:

1. What primitive or behavior is actually creating value?
2. What category or cluster does it belong to?
3. Why does it matter now, and for whom?
4. What evidence supports the opportunity, and what evidence could disprove it?
5. What is the most believable wedge or beachhead?
6. What is the cheapest next action that would materially increase confidence?

Do not escalate from idea to principle, or from interesting pattern to strategy, without walking through this sequence.

## Research Methodology

1. Capture broadly before judging.
2. Separate facts, observations, interpretations, and hypotheses.
3. Look for repeated primitives and recurring behavioral patterns across ideas.
4. Cluster by underlying value engine, job, or mechanism rather than by industry label.
5. Prefer direct market, customer, usage, or operating evidence over abstract opinion.
6. Record contradicting evidence with the same visibility as supporting evidence.
7. When evidence is thin, recommend a validation step instead of a strategic rewrite.

## Concept Schema Standard

Atlas concept records must use `schemas/concept-schema.md` as the canonical schema.

Every concept that enters structured analysis, comparative review, clustering, research, validation, or the representative 100-concept pilot must conform to the eight required fields in Concept Schema v1.0:

1. Concept
2. Primitive
3. Job
4. Customer
5. Value Mechanism
6. Initial Wedge
7. Confidence
8. Evidence

Apply these operating rules:

1. Raw capture may start as loose notes, but promotion into the working concept set requires the full schema.
2. One concept record should describe one concept only.
3. If the primitive, job, customer, or wedge is unclear, do not force clustering yet; clarify the record first.
4. Confidence must reflect the evidence shown, not the attractiveness of the idea.
5. The schema is mandatory for the representative 100-concept pilot and may not drift during that pilot without a new decision and schema version.

## Repository Execution Path

Atlas repository updates should use `docs/CODEX_WORKFLOW.md` as the default Codex execution path.

Apply these rules:

1. Use `/Users/abhil/Documents/Codex/repos/atlas-os` as the canonical writable Atlas checkout.
2. Start each new Atlas session by reading `docs/BOOTSTRAP.md`.
3. Prefer local git for repository updates and publishing.
4. Treat a successful `git push` as the normal path that updates GitHub online.
5. Use browser editing or connector-based file writes only as fallback paths when local git publishing is unavailable.

## Atlas Operating Model v1.0

Atlas follows a repository-first operating model. Git is the authoritative source of truth for active state, tasking, execution results, and review decisions.

### Artifact Ownership

- Chat owns `atlas/TASK.md`, `atlas/tasks/TASK-xxx.yaml`, `atlas/REVIEW.md`, and `atlas/reviews/TASK-xxx.md`.
- Work owns `atlas/RESULT.md` and `atlas/results/TASK-xxx.yaml`.
- Shared owns `atlas/STATE.md`.

### Lifecycle

`Draft -> In Progress -> Completed -> Approved/Rejected`

Apply these rules:

1. Create or update the task artifacts before execution starts.
2. Move the task to `In Progress` only when Work is actively executing it.
3. Record the result artifacts when execution reaches `Completed`.
4. Close the loop only after Chat records `Approved` or `Rejected`.

### Task Identity

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
5. Decision: when a strategy or operating choice is made, log it in `docs/DECISION_LOG.md`.

Keep these stages separate. Early conviction is not evidence.

## Session Workflow

Every Atlas session should follow this loop:

1. Orient on `docs/BOOTSTRAP.md`, the current repository state, roadmap, and recent decisions.
2. Define or refresh the active task in `atlas/TASK.md` and `atlas/tasks/TASK-xxx.yaml`.
3. Capture or review new raw concepts, research, or evidence.
4. Update observations, hypotheses, or principles when thresholds are met.
5. Normalize active concepts into the canonical concept schema before clustering or comparison work.
6. Update opportunity structures, clusters, or validation notes as needed.
7. Record execution output in `atlas/RESULT.md` and `atlas/results/TASK-xxx.yaml` when work completes.
8. Produce the best-answer-first recommendation.
9. Review the result in `atlas/REVIEW.md` and `atlas/reviews/TASK-xxx.md`.
10. Update touched source-of-truth documents in the same session, including `atlas/STATE.md` when state changes.
11. Log any material decision or strategic change before closing.

## Session Closeout Standard

An Atlas session is not complete until these questions are answered:

1. What changed in the knowledge base?
2. Did any hypothesis advance, weaken, or get falsified?
3. Did any strategic or process decision need a decision log entry?
4. Which source-of-truth documents were updated?
5. What is the next highest-leverage move?
