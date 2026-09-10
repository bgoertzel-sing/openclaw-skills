# Frame-oracle v14 Stage-A model readiness gate

- Frozen: `2026-08-09T01:23:00Z`
- Parent: clean frame-oracle v13 commit `8108d986e95d66e74cdb222695b9c94f81350c26`
- Status: preregistered decision gate only; no model invocation or fixture admitted

This gate separates runtime discovery from author eligibility. A successor may
perform at most one readiness probe, and only after freezing its exact command,
request bytes, environment, timeout, and expected receipts. The probe is not
Stage A and must receive none of the four Stage-A inputs, project files,
fixture material, sealed material, candidate source/tests, conversation,
memory, retrieval state, or semantic-free-lane material.

## Frozen probe boundary

The trusted outer launcher must verify the already frozen Ollama executable,
`llama-server`, 22-entry combined runtime closure, and complete content-addressed
`qwen2.5:7b` model closure before starting a new cleared, network-unshared
Bubblewrap namespace. The model store is read-only. The namespace receives an
empty writable receipt directory, no inherited stdin or terminal, and no
Stage-A output directory.

The request must be a model-neutral liveness probe whose exact bytes predate
execution and contain no predicates, relations, entities, fixture examples,
sentence templates, derivation guidance, project names, or bundle schema. It
may request only one fixed ASCII sentinel. The persistent semantics worker may
hash and verify those bytes but may not adapt them after seeing a response.

## Binary acceptance predicates

The readiness result is `READY` only if all of the following hold in one run:

1. Every executable, runtime, model manifest, and model blob hash matches its
   frozen receipt before the request.
2. Exactly one control server and the exact frozen runner start inside the
   isolated namespace, with no network interface beyond isolated loopback.
3. Exactly one non-streaming generation request is accepted, causes the exact
   model artifact to load, and yields exactly one terminal response before the
   frozen timeout.
4. The terminal response is valid UTF-8, contains only the requested fixed
   ASCII sentinel after whitespace normalization, and is below the frozen byte
   limit. No tool call, continuation, retry, repair, or second request occurs.
5. The outer receipt proves the runner path/hash, model manifest digest, loaded
   model identity, request count, response count, terminal status, timeout,
   mount table, denial probes, and server/runner teardown.
6. The receipt directory contains only the preregistered non-semantic logs and
   a manifest written last; no generated content is reused as fixture material.

Any missing receipt, hash mismatch, unexpected readable input, extra process or
request, malformed response, timeout, crash, model substitution, post-response
mutation, or teardown failure yields `NOT_READY`. The attempt is immutable and
may not be repaired in place. A later retry requires a fresh preregistration
and cannot reuse response-derived changes.

## Consequences

`READY` establishes only isolated model-load and one-shot transport
compatibility. It does not establish independent authorship, admit the probe
response, authorize Stage A, or make any later fixture admissible. The outer
author-eligibility contract, noninteractive I/O contract, and all bundle
verification predicates remain independently binding.

This gate authorizes no probe in the present run, no Stage-A model request,
fixture creation, randomness generation, sealed access, candidate inspection,
labels, readout, substitution evaluation, semantic loss, remote compute,
publication, or push. V14 remains sealed, unopened, and unconsumed.
