# Atlas Canonical Job Taxonomy

Last updated: 2026-08-05
Status: Active

## Why Job And Domain Are Separate

The previous `Job` field mixed two different ideas into one label:

1. the customer's desired outcome
2. the context where that outcome happens

Example:

- `Improve roadmap decisions.`

This combines:

- canonical outcome: `Improve decisions`
- domain context: `Product`

Splitting the field makes Atlas easier to analyze. We can now compare similar customer outcomes across multiple domains without renaming, merging, or deleting concepts.

## Definitions

### Canonical Job

A canonical job is the universal customer outcome.

Rules:

- Keep it verb-led.
- Keep it domain independent.
- Describe what the customer wants to achieve, not the product mechanism.
- Avoid industries, product categories, technologies, and implementation details.

Examples:

- `Improve roadmap decisions.` -> `Improve decisions`
- `Preserve context for operating decisions.` -> `Preserve context`
- `Find opportunities in workflow execution.` -> `Find opportunities`

### Domain

Domain is the context in which the job occurs.

Rules:

- Use a controlled vocabulary only.
- Treat domain as the operating context, not the customer persona.
- Prefer the most stable contextual label visible in the concept title, description, customer, or wedge.
- When the old `Job` context is too coarse, use the concept description to choose a more precise domain.

Examples:

- `Improve decisions` + `Product`
- `Preserve context` + `Operations`
- `Find opportunities` + `Research`

## Normalization Rules

1. Do not add, remove, merge, or rename concepts.
2. Split legacy jobs into `Canonical Job` plus `Domain`.
3. Keep `Canonical Job` broad enough to compare across domains.
4. Keep `Domain` narrow enough to preserve analytical context.
5. When a mapping remains ambiguous, keep the best-fit controlled value and record the ambiguity in `Notes`.

## Canonical Job Vocabulary

| Canonical Job | Definition |
| --- | --- |
| Improve decisions | Help the customer make better choices, prioritization calls, and tradeoffs. |
| Improve execution | Help the customer run ongoing work and coordination more effectively. |
| Improve capability | Increase skill, expertise, or personal effectiveness over time. |
| Improve planning | Make plans more robust, adaptive, or better informed before action. |
| Improve creation | Increase the quality or leverage of created outputs and intellectual assets. |
| Preserve context | Capture and recall knowledge, history, rationale, and prior decisions. |
| Find opportunities | Surface unmet needs, openings, patterns, or high-upside possibilities. |
| Accelerate learning | Help people or systems learn, onboard, or improve faster. |
| Accelerate execution | Shorten time-to-progress in coordinated work or multi-step action. |
| Coordinate work | Move multi-step work across people, tools, or systems with fewer handoffs. |
| Match resources | Connect the right people, assets, opportunities, or support at the right time. |
| Verify quality | Establish quality, trust, readiness, or compliance before proceeding. |
| Predict outcomes | Forecast likely outcomes early enough for the customer to act. |
| Test scenarios | Explore alternatives before committing time, capital, or trust. |
| Create reusable outputs | Turn work into repeatable assets, reusable outputs, or durable IP. |
| Compound capability | Make learning, self-improvement, or expertise accumulate across cycles. |
| Compound gains | Make each cycle increase the value of the next instead of resetting. |
| Adapt continuously | Keep plans, systems, or behavior aligned as conditions change. |

## Domain Vocabulary

| Domain | Definition |
| --- | --- |
| Product | Product planning, roadmap, launch, and product strategy work. |
| Operations | Company-level management, planning, and operating decisions. |
| Workflow | Repeated business processes, approvals, handoffs, and operational execution. |
| Commercial | Revenue, customer, account, procurement, negotiation, and growth activity. |
| Finance | Finance, accounting, audit, tax, wealth, and capital allocation workflows. |
| Legal | Contracts, compliance, legal reasoning, rights, and legal process work. |
| Talent | Recruiting, onboarding, workforce design, and employee capability development. |
| Education | Teaching, schooling, structured learning, and formal capability building. |
| Household | Family logistics, home management, and household coordination. |
| Healthcare | Clinical care, caregiving, patient support, and health management. |
| Physical Operations | Manufacturing, logistics, supply chain, field operations, and asset operations. |
| Research | Scientific research, experimentation, interviews, and discovery programs. |
| Infrastructure | Utilities, resilience, long-horizon assets, and shared technical or civic infrastructure. |
| Content & IP | Content creation, publishing, knowledge products, and intellectual property. |
| Venture | Startups, acquisitions, venture building, and investment-oriented company creation. |
| Community | Community participation, belonging, reputation, and social coordination. |
| Personal Development | Individual growth, identity, memory, habits, and personal leverage. |
| Automation | Robotics, autonomous fleets, and physical automation deployment. |
| Public Sector | Government, grants, policy execution, and public administration. |
| Institutions | Society-scale systems, governance models, and long-horizon collective capability. |

## Regeneration

Run `scripts/build_concepts_curated.py` from the repository root to rebuild:

- `knowledge/evidence/concepts/concepts_curated.csv`
- `knowledge/evidence/concepts/job_taxonomy.csv`
- `knowledge/evidence/concepts/concepts_inventory_qa.md`
