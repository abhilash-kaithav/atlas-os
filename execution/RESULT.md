# Atlas Result Board

Last updated: 2026-08-12
Status: Latest execution recorded
Owner: Work

## Current Result

`TASK-010` execution is complete.

- Task ID: `TASK-010`
- Title: `Top 50 Industry Census`
- Execution Status: `Completed`
- Structured Artifact: `execution/results/TASK-010.yaml`

The execution created Atlas's first economy-first industry census, grounded it in current BEA 2025 industry data with 2026 Q1 context, and updated Atlas state so workflow exploration can begin from a structured industry evidence base.

## Ownership

- Work writes `execution/RESULT.md` and `execution/results/TASK-xxx.yaml` after task execution.
- Chat reviews results and records approval or rejection in `execution/REVIEW.md` and `execution/reviews/TASK-xxx.md`.
- Shared uses approved results to update `core/STATE.md`.

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
