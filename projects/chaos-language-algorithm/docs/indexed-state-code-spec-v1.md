# Indexed generalized-state code specification v1

Status: implementation/unit-validation specification. This is not a measured
benchmark protocol and does not authorize inspection of attractor suffixes.

## Purpose

Define an additive, complete, deterministic state code that avoids charging a
token's UTF-8 spelling every time the token occurs. The existing canonical JSON
state code remains unchanged as v1 evidence. The indexed code is a separate
codec and must be evaluated only under a subsequently frozen experiment.

## Information and accounting contract

The encoder emits two independently EOF-framed canonical UTF-8 JSON documents
and charges exactly eight bits per byte:

1. The model document contains a sorted token table, sorted category table,
   and sorted production table.
2. The data document contains the top-level parse.
3. Every token is written exactly once in the shared model token table. All
   grammar, parse, category-member, category-occurrence, and generalized-member
   references use zero-based integer indices into that table.
4. Category slots and occurrences use zero-based indices into the sorted
   category table. Positional array records and fixed short tags are part of
   the versioned schema; no implicit corpus, training history, edit log, score,
   or external dictionary is available to the decoder.
5. The decoder reconstructs the source corpus only by expanding the transmitted
   grammar and parse. It rejects malformed indices, duplicate/noncanonical
   table rows, unknown tags, noncanonical JSON, and non-byte-stable re-encoding.

The shared token table is applied identically to literal and generalized
states. It is therefore an outcome-independent representation correction, not
a discount available only to a proposed grammar.

## Canonical ordering

- Tokens: ascending `(kind, value)`.
- Categories: ascending name; member references ascending token index.
- Productions: ascending left-hand-side token index.
- JSON: UTF-8, Unicode preserved, sorted object keys, compact separators. The
  top-level documents and all records are arrays, so field order is explicit.

## Entry records

- `["t", token_index]`: token.
- `["s", category_index]`: category slot in a production.
- `["o", category_index, member_token_index]`: category occurrence.
- `["g", chunk_token_index, [member_token_indices...]]`: generalized chunk
  occurrence with its ordered decoding side table.

## Validation boundary and next measured gate

Unit validation must cover literal and generalized exact round trips, Unicode,
byte-stable re-encoding, explicit member preservation, deterministic ordering,
and fail-closed malformed indices/tags. Unit tests may assert structural
properties and exact reconstruction but must not compare candidate codelength
outcomes on the frozen 19-frame decision fixture.

Before any codelength comparison, create a new experiment ledger and freeze the
implementation commit, fixture/hash, both candidate states, exact command,
acceptance rule, controls (at minimum existing canonical JSON v1 and indexed
literal state), and artifact hashes. The Mackey--Glass and Lorenz--96 suffixes
remain prohibited tuning data. A synthetic indexed-code result cannot revise
their held-out coding null or establish chaos or semantic grammar.

## Research-rule mapping

- Rule 1: validate decoding, canonicality, and malformed-input rejection before
  using the codec as an estimator.
- Rule 2: freeze this behavioral/accounting spec before code.
- Rule 5: subsequent measurements require a ledger, hashes, commands, and
  per-component bit totals.
- Rule 6: the token table is an explicit quotient from repeated token spellings
  to stable symbol identities; it changes representation overhead, not the
  grammar's semantic content.
- Rule 7: keep this codec additive and replaceable behind the same state/code
  boundary; do not rewrite the learner or enable the joint miner.
