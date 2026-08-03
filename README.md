# Atlas OS

Atlas OS is the versioned operating system for evaluating, validating, and acting on revenue-relevant opportunities.

## Operating Priorities

1. Revenue first.
2. Recommendations stay concise.
3. No thinking out loud in deliverables.
4. No strategy changes without evidence.
5. Generate broadly, then cluster and validate.
6. Record decisions and document changes explicitly.

## Repository Structure

```text
atlas-os/
├── README.md
├── docs/
│   ├── AI_OPERATING_MANUAL.md
│   ├── CHARTER.md
│   ├── DECISION_LOG.md
│   └── PLAYBOOK.md
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

1. Capture raw ideas broadly in research notes or intake.
2. Cluster related ideas before recommending action.
3. Validate the strongest clusters with evidence.
4. Recommend the next revenue-relevant move in a compact format.
5. Update the decision log and any touched documents in the same pass.

## Source of Truth

- Mission, scope, and constraints: `docs/CHARTER.md`
- AI operating rules: `docs/AI_OPERATING_MANUAL.md`
- Execution rhythm: `docs/PLAYBOOK.md`
- Decision history and version control: `docs/DECISION_LOG.md`
- Opportunity pipeline: `opportunities/opportunity_db.csv`

## Document Control

- Initialized: 2026-08-03
- Change rule: any strategic change must cite evidence and add a decision log entry.
