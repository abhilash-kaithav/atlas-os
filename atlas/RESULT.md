# Atlas Result Board

Last updated: 2026-08-06
Status: Latest execution recorded
Owner: Work

## Current Result

`TASK-002` execution is complete.

- Task ID: `TASK-002`
- Title: `Opportunity Family Formation`
- Execution Status: `Completed`
- Structured Artifact: `atlas/results/TASK-002.yaml`

The execution produced the first Atlas Opportunity Family taxonomy, a one-to-one 700-row family map derived from the approved Value Pattern layer, a generated summary report, and the supporting script that reproduces those outputs from `value_pattern_map.csv`.

## Ownership

- Work writes `atlas/RESULT.md` and `atlas/results/TASK-xxx.yaml` after task execution.
- Chat reviews results and records approval or rejection in `atlas/REVIEW.md` and `atlas/reviews/TASK-xxx.md`.
- Shared uses approved results to update `atlas/STATE.md`.

## Required Result YAML Fields

- `task_id`
- `title`
- `execution_status`
- `artifact_owner`
- `recorded_on`
- `updated_on`
- `source_task`
- `summary`
- `completed_work`
- `deliverables`
- `files_changed`
- `validation`
- `open_issues`
- `follow_up`
- `review_artifact`

## Status Rules

- Result artifacts should use `execution_status: Completed` when Work finishes the task.
- Approval happens in review artifacts, where Chat records `Approved` or `Rejected`.
