# Frame-oracle v14 Stage-A noninteractive author I/O contract

- Frozen: `2026-08-08T23:23:00Z`
- Parent: clean frame-oracle v13 commit `8108d986e95d66e74cdb222695b9c94f81350c26`
- Status: interface contract only; no author invocation or fixture admitted

This contract is the final pre-launch interface requirement for the local
hash-pinned author candidate. It specifies transport and atomicity, not fixture
content, derivation logic, examples, or a model prompt.

## Frozen invocation boundary

The trusted outer launcher must create a new empty output directory and a new
cleared, network-unshared Bubblewrap namespace. It must verify all executable,
runtime-closure, model-closure, and four-input hashes before launch. The author
receives no inherited stdin, terminal, conversation, memory, retrieval state,
or interactive channel. Its complete readable regular-file surface is the four
files frozen by the isolation contract plus the pre-hashed runtime and model
closure required to execute the already identified general authoring model.

The exact immutable launcher argument vector and environment must be frozen in
the outer receipt before execution. The launcher may contain only generic
runtime settings and the location of the four input files and output directory.
It must not contain fixture examples, sentence templates, entity names,
predicate-specific suggestions, derivation rules, retries, or repair text from
the persistent worker.

## One-shot noninteractive protocol

One invocation may make exactly one generation request to the hash-pinned local
author model and must terminate without follow-up. The request body, including
the author model's independently existing generic instruction mechanism, must
be hash-frozen before launch and recorded by the trusted outer process without
being derived or edited by this persistent worker. Streaming, tool calls,
conversation continuation, request replay, response repair, and a second model
turn are forbidden.

The author must write the exact Stage-A bundle directly into the empty output
directory and then atomically create `MANIFEST.sha256` last. Standard output
and standard error are receipts only and must not be parsed into a second
prompt. A zero process exit is insufficient: the outer process must also
observe exactly one request, exactly one terminal response, no network egress,
no unexpected readable file, and the exact frozen bundle membership.

## Fail-closed state machine

The only admissible state sequence is
`PREFLIGHTED -> STARTED -> ONE_REQUEST -> ONE_RESPONSE -> BUNDLE_FROZEN`.
Timeout, signal, malformed output, extra request, missing or extra bundle file,
nonzero status, schema failure, premise failure, denial-receipt failure,
post-manifest mutation, or any attempt at interaction transitions immediately
to `RETIRED`. A retired attempt and all of its fixture content are permanently
inadmissible; no in-place correction, prompt change, continuation, or selective
salvage is allowed.

The persistent worker may later perform only the frozen non-disclosing bundle
verification. It must not preview fixture text before the manifest is durable.
Stage B remains a separate later turn even after a passing Stage-A bundle.

## Current decision

The combined runtime discovery receipt establishes that the control server can
find the runner, but neither this interface contract nor that receipt proves
model-load compatibility or independent-author eligibility. Before any author
launch, a separate no-fixture model-load/generation readiness decision must
show that every predicate in the author eligibility contract is satisfied.

This contract authorizes no model request, model load, fixture creation,
randomness generation, sealed access, candidate inspection, oracle call,
labels, readout, substitution evaluation, semantic loss, remote compute,
publication, or push. V14 remains sealed, unopened, and unconsumed.
