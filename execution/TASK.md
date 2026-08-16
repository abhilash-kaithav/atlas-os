# Atlas Task Board

Last updated: 2026-08-16
Status: Latest task approved
Owner: Chat

## Current Task

- Task ID: `TASK-023`
- Title: `RO-008 Investment Committee`
- Lifecycle Status: `Approved`
- Structured Artifact: `execution/tasks/TASK-023.yaml`

## Ownership

- Chat writes and updates `execution/TASK.md` and `execution/tasks/TASK-xxx.yaml`.
- Work executes approved tasks and records outcomes in `execution/RESULT.md` and `execution/results/TASK-xxx.yaml`.
- Shared updates `core/STATE.md` after approved work changes Atlas state.

## Lifecycle

`Draft -> In Progress -> Completed -> Approved/Rejected`

Apply the lifecycle this way:

1. `Draft`: the task is defined and waiting to be executed.
2. `In Progress`: Work is actively executing the task.
3. `Completed`: Work finished execution and recorded a result.
4. `Approved`: Chat reviewed the result and accepted it.
5. `Rejected`: Chat reviewed the result and declined it or requested rework.

## Task ID Convention

- Format: `TASK-001`, `TASK-002`, `TASK-003`, and so on.
- One task ID follows the same work item across task, result, and review artifacts.
- Every task ID should map to:
  - `execution/tasks/TASK-xxx.yaml`
  - `execution/results/TASK-xxx.yaml`
  - `execution/reviews/TASK-xxx.md`

## Required Task YAML Fields

- `task_id`
- `title`
- `status`
- `artifact_owner`
- `created_on`
- `updated_on`
- `objective`
- `context`
- `inputs`
- `deliverables`
- `constraints`
- `acceptance_criteria`
- `handoff_to`
- `result_artifact`
- `review_artifact`
