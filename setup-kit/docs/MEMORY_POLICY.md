# Memory Architecture and Curation Policy

## Objective

Retain useful context over years of related research without turning the system into an unsearchable transcript dump or allowing stale model-generated claims to become facts.

The design uses several layers with different responsibilities.

## Layer 1: project and library records

These are the source of truth.

- `projects/<slug>/PROJECT.md`: current project state.
- `TASKS.md`: prioritized work.
- `DECISIONS.md`: accepted/rejected/superseded decisions and rationale.
- `experiments/<run>/RUN.md`: executable evidence.
- `library/<slug>/SOURCE.md`: provenance-rich external source record.
- Git commits, tests, raw data, and original documents: primary evidence.

This layer should remain understandable without chat history.

## Layer 2: daily memory

`memory/YYYY-MM-DD.md` records chronology, open loops, and pointers. It is allowed to be rough but must not contain secrets. It should not duplicate entire project documents or conversations.

## Layer 3: curated cross-project memory

`MEMORY.md` contains stable preferences, recurring methods, durable environment facts, high-value corrections, and pointers across projects. It is deliberately compact.

Promotion criteria:

- likely useful again;
- supported by a source or repeated observation;
- stable enough not to expire immediately;
- not better housed solely in one project;
- safe to persist.

## Layer 4: QMD recall

QMD indexes Markdown and optionally session transcripts. It supplies lexical, semantic, and reranked retrieval across memory, projects, library sidecars, and the catalog. It is a search mechanism, not an authority.

Recommended settings:

- `searchMode: query` for hybrid recall and expansion;
- explicit paths for `projects`, `library`, and `catalog`;
- direct-message-only injection;
- bounded results and injected characters;
- finite session transcript retention;
- local models and automatic fallback to the built-in memory engine.

The first semantic query can require a large local model download. QMD ignores common build/dependency directories, which helps prevent indexing noise.

## Layer 5: active memory

Active memory performs a bounded recall pass before eligible replies. It reduces reliance on the main model remembering to search.

Recommended starting policy:

- main agent only;
- direct chats only;
- recent conversation context;
- recall-heavy but bounded output;
- temporary sub-agent transcripts;
- no tools except memory recall;
- explicit latency timeout.

Tune toward `balanced` if recall is noisy, or `message` if latency is unacceptable. Use `full` only for sessions where the added delay is justified.

## Layer 6: dreaming and memory wiki

Dreaming proposes consolidation from short-term material into durable memory. Memory-wiki compiles provenance-rich entities, concepts, claims, syntheses, and dashboards.

Use them after the lower layers are functioning. Generated output is not automatically true. Review low-confidence claims, contradictions, and stale pages. In the recommended hybrid:

- QMD remains the broad recall layer;
- memory-wiki uses bridge mode to compile exported memory artifacts;
- durable facts remain linked to project/source evidence.

## Session transcripts

Transcripts can recover decisions that were not written elsewhere, but they are sensitive, verbose, and sometimes wrong. Use finite retention and promote important material into project records. Do not rely on indefinite transcript accumulation as the main memory strategy.

## Search procedure

For a new task:

1. identify likely project(s) and aliases;
2. search the catalog and project records;
3. use memory search for related decisions, preferences, and prior experiments;
4. use exact search for code, identifiers, error messages, and citations;
5. open primary records before acting on consequential retrieved claims;
6. resolve contradictions explicitly.

## Curation cadence

At task completion:

- update project source of truth;
- write a concise daily note;
- promote only durable cross-project facts;
- verify retrieval.

Weekly or after a major milestone:

- review stale tasks and projects;
- consolidate duplicate notes;
- inspect unresolved contradictions and dream/wiki proposals;
- prune low-value or sensitive transcript material according to policy;
- back up durable records.
