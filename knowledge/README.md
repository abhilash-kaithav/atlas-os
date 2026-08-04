# Knowledge Base

Last updated: 2026-08-04
Status: Active

## Purpose

The knowledge base preserves what Atlas has actually learned. It keeps raw pattern recognition separate from stronger claims so the system can compound insight without pretending certainty.

## Knowledge Objects

### Observations (`O-xxx`)

Observations record direct patterns noticed in ideation, research, validation, or operating work.

- Store them in `knowledge/observations/`.
- Record what was seen, where it appeared, and what boundary conditions still apply.
- Observations can be created immediately when the pattern is real enough to name.

### Hypotheses (`H-xxx`)

Hypotheses are the current best explanations for repeated observations.

- Store them in `knowledge/hypotheses/`.
- Promote only after at least three independent observations point to the same explanation.
- Include supporting evidence, contradicting evidence, and a falsification path.

### Principles (`P-xxx`)

Principles are durable rules that have survived repeated evidence and active challenge.

- Store them in `knowledge/principles/`.
- Do not create a principle because it sounds right.
- A principle should be stable enough to guide future work by default.

### Decision Log (`D-xxx`)

The decision log records durable choices about strategy, prioritization, workflow, or governance.

- The authoritative log lives in `docs/DECISION_LOG.md`.
- Add a new entry instead of rewriting history when a decision changes.
- Decisions should reference the evidence or rationale behind the call.

## Promotion Rules

The default ladder is:

1. Observation
2. Hypothesis
3. Principle
4. Decision-informed operating change

Not every observation becomes a hypothesis, and not every hypothesis becomes a principle.

## Writing Standard

For every knowledge artifact:

1. Separate facts from interpretation.
2. Record contradicting evidence, not only supporting evidence.
3. Prefer short, scannable notes over long speculative essays.
4. Link related artifacts when a pattern advances or weakens.
