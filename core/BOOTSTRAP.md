# Atlas Bootstrap

Last updated: 2026-08-12
Status: Active first-read startup document

## Purpose

This is the first document every future Atlas session should read.

It is a startup guide, not a replacement for the underlying source-of-truth artifacts.

When prior conversation conflicts with the repository, the repository wins.

## Canonical Startup Sequence

1. Use the canonical Atlas checkout at `/Users/abhil/Documents/Codex/repos/atlas-os`.
2. Read this file before making any Atlas decision or edit.
3. Read `core/STATE.md` and `core/DECISION_LOG.md`.
4. Read `core/ATLAS_CONSTITUTION.md`, `core/ATLAS_REASONING_MODEL.md`, and `core/OPERATING_MODEL.md`.
5. Read `execution/TASK.md` and any active structured task artifact if one exists.
6. Read the relevant concept evidence, knowledge artifacts, case studies, or archived discovery outputs for the work at hand.
7. Use local git as the default write and publish path.
8. Treat prior conversations as historical context only.

## Atlas In One Paragraph

Atlas is a repository-first operating system for discovering enduring company opportunities from durable evidence.

Its purpose is not to collect interesting ideas. Its purpose is to preserve evidence, derive reusable strategic knowledge, and surface the rare opportunities worth building.

## Exploration Philosophy

- Start from the global economy, then move through industry census, operating systems, core workflows, and structural failures before writing a company thesis.
- Treat `archive/discovery-v1/` as a frozen knowledge asset for inspiration and comparison, not as the default entry point for new work.
- Optimize for structural advantage, not novelty.

## Active Source Of Truth

Use these as the governing set:

- `core/ATLAS_CONSTITUTION.md`
- `core/ATLAS_REASONING_MODEL.md`
- `core/OPERATING_MODEL.md`
- `core/DECISION_LOG.md`
- `core/PRODUCT_BOUNDARY.md`
- `core/STATE.md`
- `execution/TASK.md`
- `execution/RESULT.md`
- `execution/REVIEW.md`
- `knowledge/evidence/concepts/`

## Historical Context

Use these only when historical lineage matters:

- `archive/discovery-v1/`
- `archive/superseded-core/`
- `archive/snapshots/`

## Current State On 2026-08-12

- Discovery v1 is complete and frozen in `archive/discovery-v1/`.
- `OF-002` is closed as a current venture candidate and preserved as institutional knowledge.
- The active phase is Industry Census and Workflow Exploration.
- The immediate goal is to identify reusable structural failures across industries before committing to a specific company thesis.

## Immediate Next Move

Define the first industry census and workflow exploration task before any new company thesis or deep research sprint begins.

That task should:

1. select industries worth mapping
2. identify the operating systems and core workflows inside them
3. isolate reusable structural failures before evaluating individual company theses
4. use `archive/discovery-v1/` and `knowledge/postmortems/OF-002.md` as institutional learning, not as the default navigation layer

## Working Rules

- Repository-first: durable work ends in repository artifacts, not discussion alone.
- Preserve evidence: raw concepts and contradictory evidence stay visible.
- Prefer one recommendation by default unless a real architectural tradeoff exists.
- Update touched source-of-truth documents in the same session.
- Log material strategic or process changes before closeout.
