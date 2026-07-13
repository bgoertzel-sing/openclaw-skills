---
name: research-projects
description: Create, resume, organize, and close long-running research software projects under the OpenClaw workspace. Use when a task needs a project record, status update, task plan, decision log, repository map, or cross-project link.
---

# Research Projects

Use `~/research-agent/projects/<slug>/` as the durable home for each project.

## Create

1. Choose a lowercase hyphenated slug that will remain stable.
2. Run `~/research-agent/bin/new-project <slug> "<title>"`.
3. Fill `PROJECT.md` with purpose, success criteria, scope, current state, repositories, risks, and open questions.
4. Add testable work to `TASKS.md`.
5. Add or update the row in `catalog/PROJECTS.md`.
6. Add a pointer in today's memory note.

Do not create a duplicate project merely because the wording changed. Search the catalog and memory first.

## Resume

Before work, read:

- `PROJECT.md`
- `TASKS.md`
- `DECISIONS.md`
- recent experiment `RUN.md` files
- repository README/CI and Git status

State the current question and the smallest useful next step.

## Record

- Put durable rationale in `DECISIONS.md`.
- Put chronological rough notes in dated sections of `NOTES.md`.
- Put measured or executable work in an experiment record.
- Keep `PROJECT.md` as the current summary, not a full diary.
- Link related projects explicitly and explain the relationship.

## Close or pause

Update status, final/current result, unresolved questions, repository state, and restart instructions. Archive rather than delete. Promote only cross-project facts to `MEMORY.md`.
