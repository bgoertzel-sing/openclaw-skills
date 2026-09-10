# Ingestion / Index Ledger

This directory is the **ingestion/index ledger** for the Hyperseed formalization
program. Per Ben (2026-07-15), skip rationale and scan provenance live **here**,
not as Hyperseed formalization notes — otherwise reviewed-but-skipped material
would create output noise in the formalization corpus.

## Separation of concerns

- **`ledger/`** — tracks *what was reviewed*, its status, and *why* something was
  skipped. Cheap stubs, one row per source item. No formal content.
- **`entries/`** — durable Hyperseed formalizations only. A source item lands here
  **only** when it clears the salience gate (genuinely novel structural content).

## Files

- `substack_index.json` — one row per Substack post (75 as of 2026-07-15),
  reverse-chronological. Fields:
  - `status`: `pending` | `scanned` | `formalized` | `skipped`
  - `skip_rationale`: why a scanned post did not earn a formalization (null unless skipped)
  - `formalization_entry`: relative path under `entries/` when `status=formalized`
  - `scanned_at`: date the post was read end-to-end

## Policy

Exhaustive scan, selective formalization, ledgered skip rationale. Every post gets
read; only consequential / structurally novel ones become `entries/` notes; the
rest get an honest `skipped` row with a one-line reason. Borderline cases favor a
stub over a silent drop.
