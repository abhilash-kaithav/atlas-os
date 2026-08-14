# Atlas Result Board

Last updated: 2026-08-14
Status: Latest execution recorded
Owner: Work

## Current Result

`TASK-013` execution is complete.

- Task ID: `TASK-013`
- Title: `Phase 3 Structural Failure Atlas`
- Execution Status: `Completed`
- Structured Artifact: `execution/results/TASK-013.yaml`

The execution synthesized the normalized census and the workflow library into a durable Structural Failure Atlas: eight recurring failure categories, one workflow-level classification layer, one expanded failure frequency matrix, and one executive summary that Phase 4 can use without reopening workflow anatomy.

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
