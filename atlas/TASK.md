# Atlas Task Board

Last updated: 2026-08-06
Status: Active
Owner: Chat

## Current Task

- Task ID: `TASK-004`
- Title: Top-Family Research: Decision and Foresight Infrastructure
- Lifecycle Status: Draft
- Structured Artifact: `atlas/tasks/TASK-004.yaml`

## Ownership

- Chat writes and updates `atlas/TASK.md` and `atlas/tasks/TASK-xxx.yaml`.
- Work executes approved tasks and records outcomes in `atlas/RESULT.md` and `atlas/results/TASK-xxx.yaml`.
- Shared updates `atlas/STATE.md` after approved work changes Atlas state.

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
  - `atlas/tasks/TASK-xxx.yaml`
  - `atlas/results/TASK-xxx.yaml`
  - `atlas/reviews/TASK-xxx.md`

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
