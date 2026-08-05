# Atlas Result Board

Last updated: 2026-08-05
Status: Waiting for first execution
Owner: Work

## Current Result

No execution result has been recorded yet. `TASK-001` is still in `Draft` and should not be executed as part of the Atlas operating model setup.

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
