# Atlas OS

Atlas OS is the versioned operating system for discovering, classifying, validating, and acting on asymmetric opportunities.

## Operating Priorities

1. Evidence before escalation.
2. Behaviors before features.
3. Categories before products.
4. Best answer first, concise first.
5. Generate broadly, then converge through clustering and validation.
6. Record decisions and document changes explicitly.

## Repository Structure

```text
atlas-os/
├── README.md
├── atlas/
│   ├── STATE.md
│   ├── TASK.md
│   ├── RESULT.md
│   ├── REVIEW.md
│   ├── tasks/
│   │   ├── TASK-001.yaml
│   │   └── TASK_TEMPLATE.yaml
│   ├── results/
│   │   └── RESULT_TEMPLATE.yaml
│   └── reviews/
│       └── REVIEW_TEMPLATE.md
├── data/
│   ├── README.md
│   ├── concepts_raw.csv
│   ├── concepts_curated.csv
│   └── concepts_inventory_qa.md
├── docs/
│   ├── AI_OPERATING_MANUAL.md
│   ├── ATLAS_CONSTITUTION.md
│   ├── ATLAS_REASONING_MODEL.md
│   ├── CHARTER.md
│   ├── CODEX_WORKFLOW.md
│   ├── OPERATING_MANUAL.md
│   ├── DECISION_LOG.md
│   └── PLAYBOOK.md
├── knowledge/
│   ├── README.md
│   ├── hypotheses/
│   ├── observations/
│   └── principles/
├── roadmap/
│   └── ROADMAP.md
├── opportunity-engine/
│   └── README.md
├── opportunities/
│   ├── opportunity_db.csv
│   ├── clusters.md
│   └── research/
├── journals/
├── templates/
│   ├── RESEARCH_MEMO_TEMPLATE.md
│   └── WEEKLY_JOURNAL_TEMPLATE.md
└── assets/
```

## Default Workflow

1. Capture ideas broadly before judging them.
2. Translate recurring patterns into primitives, clusters, and hypotheses.
3. Validate the strongest clusters with direct evidence and a believable wedge.
4. Recommend the next highest-leverage move in a compact format.
5. Update the decision log, knowledge artifacts, and touched operating documents in the same pass.

## Source of Truth

- Active state, task, result, and review loop: `atlas/`
- Mission, scope, and constraints: `docs/CHARTER.md`
- Operating rules and workflows: `docs/OPERATING_MANUAL.md`
- Governing methodology: `docs/ATLAS_REASONING_MODEL.md`
- Historical precursor: `docs/ATLAS_CONSTITUTION.md`
- Decision history and version control: `docs/DECISION_LOG.md`
- Codex repository workflow: `docs/CODEX_WORKFLOW.md`
- Concept inventory policy: `concepts/README.md`
- Knowledge hierarchy: `knowledge/README.md`
- Current phase and milestones: `roadmap/ROADMAP.md`
- Opportunity system design: `opportunity-engine/README.md`

`opportunities/` remains the working inventory for active opportunity records while the broader opportunity engine structure is formalized.

## Document Control

- Initialized: 2026-08-03
- Change rule: any strategic change must cite evidence and add a decision log entry.
