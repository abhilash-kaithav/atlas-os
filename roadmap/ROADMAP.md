# Roadmap

Last updated: 2026-08-06
Status: Active

## Current Phase

Atlas has completed the first Opportunity Family triage pass. The immediate phase is to research the top-ranked family before choosing a build candidate.

The goal is still not to spread effort across all five families. The goal is to pressure-test the top family first so Atlas can narrow from strategic families into one build-worthy wedge.

## Current Priorities

1. Execute `TASK-004` Top-Family Research: Decision and Foresight Infrastructure.
2. Pressure-test OF-002 with external evidence and identify the best wedge candidates.
3. Preserve traceability from every research conclusion back through the scoring, Opportunity Family, and Value Pattern layers.

## Next Milestones

1. Research the highest-ranked family, OF-002 Decision and Foresight Infrastructure.
2. Identify one recommended wedge candidate within OF-002.
3. Validate the recommended wedge with direct evidence.
4. Keep OF-005 as the backup family if OF-002 weakens under research.
5. Define venture candidates only after family-level research supports them.

## Upcoming Research Work

Top-family research should follow these rules:

1. Start from the approved scoring layer and top-ranked family, not from reopening the whole ranking.
2. Use external evidence to eliminate weak wedges instead of broadening the family abstraction again.
3. Keep representative concepts, family evidence gaps, and uncertainty visible during research.
4. Produce one recommended wedge by default unless research uncovers a real tradeoff.
5. Keep the raw concept, Value Pattern, Opportunity Family, and scoring layers all traceable.

## Major Decisions Already Made

1. The repository is the source of truth.
2. Broad generation precedes prioritization.
3. Recommendations should be concise and best-answer-first.
4. Evidence is required before strategy changes.
5. The raw and curated concept layers remain separate.
6. Atlas operating model v1.0 governs execution workflow.
7. Atlas reasoning model v1.0 governs methodology.
8. Atlas Value Pattern Taxonomy v1.0 is the active first discovery layer above the concept schema.
9. Atlas Opportunity Family Taxonomy v1.0 is the active second discovery layer above Value Patterns.
10. Atlas Opportunity Family Scoring Rubric v1.0 is the active family-ranking method above Opportunity Families.

## Inputs Needed For The Next Phase

1. `opportunity-engine/scoring/README.md`
2. `opportunity-engine/scoring/opportunity_family_scores.csv`
3. `opportunity-engine/scoring/opportunity_family_ranked_summary.md`
4. `atlas/tasks/TASK-004.yaml`
