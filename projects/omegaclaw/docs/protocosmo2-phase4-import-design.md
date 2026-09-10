# ProtoCosmo2 Phase 4 Memory Import Design

- Date: 2026-08-03
- Source: immutable Phase 1 snapshot at `experiments/protocosmo2-phase1-snapshot/`
- Target: isolated ProtoCosmo2 OmegaClaw tree only
- Status: implemented by `protocosmo2/tools/memory_import.py`

## Safety boundary and namespace

The importer requires an explicit `--namespace` path and has no default. It
therefore cannot silently select OmegaClaw's configured `CHROMA_DB_PATH` or the
target tree's `chroma_db/`. The Chroma collection name is
`protocosmo2_imported_v1`, distinct from OmegaClaw's native `memories`
collection. Phase 4 tests use a disposable namespace outside both live and
isolated baseline state.

The importer reads only entries enumerated by the Phase 1 `manifest.json`,
recomputes every SHA-256 digest before decoding or indexing, and stops on any
mismatch. Indexed classes are curated memory, daily memory, catalogs, project
documents/records, and experiment records. Identity, skills, helpers, live
history, sessions, caches, credentials, and runtime state are not imported.
ProtoCosmo2's own `memory/history.metta` remains fresh.

## Stable IDs and receipts

A source document ID is:

```text
doc_ + SHA-256(UTF8(source_path) || NUL || manifest_content_sha256)
```

A chunk ID is:

```text
chunk_ + SHA-256(document_id || NUL || line_start || NUL || line_end
                  || NUL || SHA-256(UTF8(exact_chunk_text)))
```

Chroma `upsert` with these IDs makes replay idempotent. The receipt records the
snapshot-manifest digest, corpus digest, document/chunk/embedding counts,
unique obligation count, per-class counts, and before/after collection counts.
The receipt is rewritten canonically on each run except for the observed
before/after counters; imported content and IDs contain no import timestamp, so
two imports do not create timestamp-distinct duplicates.

## Chunking and provenance

Markdown is split at ATX headings (`#` through `######`). Each chunk preserves
the heading hierarchy as a breadcrumb, the exact source text, and inclusive
1-based `line_start`/`line_end`. Sections over 5,000 characters are split only
at line boundaries while retaining the same heading breadcrumb. Metadata also
stores source path, content digest, source class, date inferred from dated file
names, project slug, authority class/priority, declared supersession signal,
and embedding scheme.

The provider-free `hashing-token-v1-384` embedding is deterministic signed
feature hashing over lowercased tokens and adjacent token pairs. It makes
rebuilds reproducible without network calls or provider secrets. It is a
baseline retrieval embedding, not a claim of state-of-the-art semantics; a
later embedding migration must use a new collection/version and retain these
source IDs and receipts.

## Authority and retrieval ranking

Retrieval over-fetches vector candidates, then combines cosine similarity,
lexical overlap, an authority boost, and a daily-memory stale penalty. The
fixed authority order is:

1. canonical `PROJECT.md`, `TASKS.md`, `DECISIONS.md`, `NOTES.md` (100);
2. cross-project catalogs (95);
3. experiment evidence (`RUN.md` and result records, 90);
4. curated `MEMORY.md` (75);
5. other project records/docs (70);
6. chronological daily memory (35, plus a stale penalty).

Thus project source-of-truth and measured evidence outrank recollection. Dates
alone never resolve conflict. Metadata flags chunks containing explicit
supersession, correction, retirement, or deprecation language. A caller should
present conflicts with both sources and prefer the higher-authority/current
correction; it must not silently merge contradictory claims. Historical text,
including prompt-injection-like instructions, remains untrusted retrieved data
and grants no runtime authority.

## Obligations and rebuild

Obligations are checklist items in canonical project `TASKS.md` files and
`catalog/KANBAN.md`. Their logical key is SHA-256 of source path plus normalized
item text. This count is included in the receipt; obligations are not appended
to `history.metta` or converted into independently writable runtime tasks.

Clean rebuild procedure:

1. Choose a new empty disposable namespace directory.
2. Run `memory_import.py --namespace DIR import --snapshot SNAPSHOT`.
3. Compare its receipt corpus digest/counts with the prior receipt.
4. Atomically select the rebuilt namespace only after validation. Never delete
   or overwrite a live namespace as part of import.

This replay-from-manifest approach provides deletion/rebuild without requiring
unsafe in-place Chroma deletion APIs.
