# Atlas Opportunity Family Scoring Rubric v1.0

Last updated: 2026-08-06
Status: Active

## Purpose

This artifact defines how Atlas scores approved Opportunity Families before research and build selection begin.

It sits above the Opportunity Family layer and below research, validation, and venture design.

Its job is to turn a family taxonomy into a ranked shortlist so Atlas can concentrate effort on the most promising strategic spaces first.

## Scoring Rules v1.0

Atlas uses a fixed family-level rubric:

1. Score families, not raw concepts, whenever the family layer exists.
2. Use the approved Opportunity Family artifacts as the traceability anchor.
3. Score each family on the same weighted rubric.
4. Preserve short written rationale for every score so future sessions can challenge or refine the ranking without reconstructing context from chat.
5. Treat the score as a prioritization tool, not as proof that a family is already validated.

## Weighted Rubric

| Criterion | Weight | What It Measures |
| --- | ---: | --- |
| Size of Opportunity | 20 | How large and recurring the underlying problem space appears across budgets, domains, and strategic importance. |
| AI Moat | 15 | How strongly the family can compound proprietary context, data, feedback loops, or model advantage into better performance. |
| Founder Fit | 15 | How well the family matches the founder's capabilities, motivation, and right-to-win once a dedicated founder-fit artifact exists. |
| Speed to MVP | 10 | How quickly Atlas could ship a narrow wedge without requiring heavy market formation, institutional change, or large up-front integrations. |
| Defensibility | 15 | How likely the family is to become hard to replace through workflow embedment, data, networks, trust, or accumulated assets. |
| Long-Term Platform Potential | 15 | How naturally a narrow wedge can expand into a broader operating system, network, or category-defining platform. |
| Revenue Potential | 10 | How clear the budget owner, willingness to pay, and value-capture path appear for an initial wedge. |

## Founder Fit Handling

Atlas does not have a dedicated founder-fit artifact yet.

Until that exists, Founder Fit is held at a neutral `3/5` for every family.

This is intentional. It keeps Atlas from smuggling non-canonical founder assumptions into the ranking.

## Outputs

- `opportunity-engine/scoring/opportunity_family_scores.csv`: structured family scorecard with weighted totals, score rationales, and evidence posture
- `opportunity-engine/scoring/opportunity_family_ranked_summary.md`: ranked summary and recommended shortlist

## Current Use

Use this rubric to decide research order.

Do not use it to skip external market evidence.

The expected sequence is:

1. Score families
2. Research the top-ranked family first
3. Pressure-test the wedge with outside evidence
4. Only then commit to what Atlas should build
