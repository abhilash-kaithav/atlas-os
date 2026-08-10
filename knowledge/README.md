# Atlas Knowledge Base

Last updated: 2026-08-10
Status: Active

## Purpose

The knowledge base preserves what Atlas has actually learned. It keeps evidence, interpretation, case studies, and postmortem learning separate enough that the system can compound insight without pretending certainty.

## Active Sections

### Concept Evidence

- `knowledge/evidence/concepts/` holds the raw concept inventory, curated analytical layer, QA report, and concept-taxonomy documentation.
- This is active evidence, not archive material.

### Observations (`O-xxx`)

- Store them in `knowledge/observations/`.
- Use them for direct patterns noticed in ideation, research, validation, or operating work.

### Hypotheses (`H-xxx`)

- Store them in `knowledge/hypotheses/`.
- Promote only after at least three independent observations point to the same explanation.

### Principles (`P-xxx`)

- Store them in `knowledge/principles/`.
- Add a principle only when the hypothesis has survived repeated support and active challenge.

### Case Studies

- Store them in `knowledge/research/case-studies/`.
- Use them for durable research artifacts that should inform future opportunity evaluation.

### Postmortems

- Store them in `knowledge/postmortems/`.
- Use them for rejected wedges, failed assumptions, and durable kill-fast learning.

### Decision Log (`D-xxx`)

- The authoritative log lives in `core/DECISION_LOG.md`.
- Add a new entry instead of rewriting history when a decision changes.

## Historical Discovery

`archive/discovery-v1/` preserves the first large discovery cycle, including taxonomies, family ranking, OF-002 validation history, and completed execution artifacts.

That archive is part of Atlas memory, but it is not the active navigation layer.

## Writing Standard

For every knowledge artifact:

1. Separate facts from interpretation.
2. Record contradicting evidence, not only supporting evidence.
3. Prefer short, scannable notes over long speculative essays.
4. Link related artifacts when a pattern advances, weakens, or gets falsified.
