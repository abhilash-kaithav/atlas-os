# Codex Workflow

Last updated: 2026-08-05
Status: Active

## Purpose

This document defines the default execution path for Codex work on Atlas OS so future sessions use one canonical repository and one normal publish flow.

## Canonical Repository

- Use `/Users/abhil/Documents/Codex/repos/atlas-os` as the only writable Atlas repository checkout.
- Do not use dated temporary Codex work folders as the source of truth for repository updates.
- Before starting repository edits, orient on this checkout first.

## Default Publish Path

- Use local git as the default write and publish method.
- A successful `git push` updates GitHub online. No separate web publish step is required.
- Browser-based editing or GitHub connector file writes are fallback paths only when local git publishing is unavailable.

## Standard Session Steps

1. Open the canonical repository checkout.
2. Read `docs/BOOTSTRAP.md` before any other Atlas work.
3. Run `git pull --ff-only` before editing when the repository may have changed.
4. Make the required repository updates in the canonical checkout.
5. Commit intentionally with a concise message.
6. Push with local git so local and GitHub stay in sync.

## Standard Instruction For New Codex Sessions

Use this instruction at the start of a new chat when repository work is expected:

```text
Use the canonical Atlas repo at /Users/abhil/Documents/Codex/repos/atlas-os.
Read docs/BOOTSTRAP.md first.
Treat repository artifacts as canonical and prior conversations as historical context only.
Use local git as the default write/publish path.
Do not use dated temporary checkouts or browser editing unless local push fails.
```
