# OmegaSelf Evidence Ledger Contract

Schema: `omegaself.evidence_record` version `1.0.0`.

## Canonical record

```metta
(EvidenceRecord
  (schema "omegaself.evidence_record" "1.0.0")
  (id "ev-001")
  (closure "sha256:<64 lowercase hex>")
  (clocks (causal "cycle:42") (record "2026-07-20T12:00:00Z") (adoption "ledger:42"))
  (event-version 1)
  (kind "tool_receipt")
  (payload-hash "sha256:<64 lowercase hex>")
  (provenance (source "runtime:tool") (method "mechanical") (parents "ev-000"))
  (timestamps (observed "2026-07-20T11:59:59Z") (recorded "2026-07-20T12:00:00Z") (adopted "2026-07-20T12:00:01Z"))
  (replay (adapter "stub:v1") (input-hash "sha256:<64 lowercase hex>") (command "fixture-replay") (deterministic true)))
```

All fields and their order are normative for canonical serialization. Strings are JSON-style quoted UTF-8 strings. `event-version` is a positive integer. IDs, clock handles, source, method, adapter and command are non-empty. Hashes and the closure handle use `sha256:` plus 64 lowercase hexadecimal characters. Timestamps are UTC RFC 3339 instants and must satisfy `observed <= recorded <= adopted`. Parents are zero or more evidence IDs. Replay information identifies the adapter, exact input hash, command, and whether deterministic replay is claimed; it does not assert that replay has occurred.

The closure is an immutable content handle for the complete evidence closure used by the record. Corrections and disqualifications are new records, never edits. LLM testimony must use an explicit low-privilege source/method and cannot be promoted by serialization.

The three clocks are distinct: `causal` orders domain events, `record` is the ledger wall-clock instant, and `adoption` orders incorporation into a derived view. They must never be collapsed into one inferred time.

## Failure contract

Unknown, missing, duplicated, or reordered fields; invalid hashes/times; non-positive versions; and trailing input are rejected. No partial record is returned.
