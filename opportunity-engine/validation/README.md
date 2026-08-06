# Atlas Validation Layer

Last updated: 2026-08-06
Status: Active

## Purpose

This directory holds the active validation plans, test queues, and customer-facing discovery artifacts that sit between research and any product build.

Atlas uses validation to answer one narrow question:

`Is the currently recommended wedge strong enough to justify building?`

## Current Focus

The active wedge is:

`Benchmark-backed SaaS and AI renewal decision copilot`

The active goal is not to build software yet.

The active goal is to test:

- buyer urgency
- willingness to pay
- benchmark moat
- data-access feasibility
- product-versus-service boundary

## Current Artifacts

- `of-002_renewal_copilot_validation_plan.md`: core hypotheses, kill criteria, and validation sequence
- `of-002_validation_test_queue.csv`: prioritized test list with success and failure signals
- `of-002_interview_guide.md`: interview script for the first customer-facing discovery sprint

## Rule

Validation should be as cheap and direct as possible.

Atlas should prefer interviews, concierge workflows, and manual decision briefs before building a broad product.
