---
name: knowledge-curation
description: Convert conversations, project work, experiment results, and recurring themes into durable, searchable, non-duplicative memory. Use at task completion, project review, memory consolidation, contradiction cleanup, or when prior work should be recalled.
---

# Knowledge Curation

Memory quality is more important than raw volume. Preserve detail in the right record and keep high-level memory compact.

## Retrieval before writing

Search for existing project names, concepts, decisions, and aliases. Update the existing canonical record rather than creating duplicates.

## Placement

- Daily chronology and open loops: `memory/YYYY-MM-DD.md`
- Stable cross-project facts and preferences: `MEMORY.md`
- Project state and results: `projects/<slug>/`
- Source material and summaries: `library/<slug>/SOURCE.md`
- Cross-project index: `catalog/`
- Machine-generated consolidation proposals: `DREAMS.md`

## Quality rules

- Never store secrets.
- Include date and provenance pointer.
- Mark fact, reproduction, inference, hypothesis, decision, or preference.
- Preserve contradictions until resolved; do not merge incompatible claims into vague prose.
- Correct stale statements and note supersession.
- Prefer links and compact summaries over duplicated blocks.
- Avoid recording ordinary transient chat that has no future value.

## End-of-task curation

1. Add a concise daily entry: work, result, open loop, and pointers.
2. Update the project source of truth.
3. Promote a fact to `MEMORY.md` only when it is stable and useful beyond one project or likely to prevent repeated work.
4. Update the catalog if status changed.
5. Verify that QMD/memory search can retrieve the new record after indexing.

## Periodic review

Review unresolved questions, contradictions, stale pages, duplicated projects, and low-confidence dream/wiki claims. Ask Benjamin only about decisions that cannot be resolved from evidence.
