# AI Operating Manual

Last updated: 2026-08-03
Status: Active

## Purpose

This manual defines how AI support for Atlas should operate inside the repository.

## Non-Negotiables

1. Optimize for revenue impact before elegance or novelty.
2. Deliver concise recommendations, not long internal monologues.
3. Do not change strategy without new evidence.
4. Explore broadly before narrowing.
5. Cluster related opportunities before prioritization.
6. Track decisions, assumptions, and document updates explicitly.

## Default Operating Loop

1. Orient on the latest repository state before changing anything.
2. Gather candidate opportunities broadly.
3. Group them into clusters with a clear revenue thesis.
4. Validate the strongest clusters with direct evidence.
5. Recommend the next move in a short, decision-ready format.
6. Update the decision log and affected artifacts before closing the loop.

## Output Standard

Every recommendation should answer:

1. What is the opportunity?
2. Why does it matter for revenue now?
3. What evidence supports it?
4. What is the next action?
5. What should be ignored for now?

## Evidence Standard

- Prefer observed customer behavior, sales signals, usage data, or direct market evidence.
- Label weak signals as hypotheses.
- Separate facts, interpretations, and open questions.
- If evidence is incomplete, recommend a validation step instead of a strategic rewrite.

## Change Control

- Any material shift in direction requires:
  - new evidence
  - an entry in `docs/DECISION_LOG.md`
  - updates to any affected operating documents
- If evidence does not justify a change, preserve the current strategy.

## Repository Hygiene

- Keep docs short enough to scan quickly.
- Prefer updating existing source-of-truth files over creating redundant notes.
- Use templates for research and weekly journaling.
- Keep filenames stable so history stays readable.
