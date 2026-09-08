# Frame-oracle v14 model-readiness probe preregistration

- Frozen: `2026-08-09T03:23:00Z`
- Parent gate SHA-256: `cb115fb168cde64dea71f128fcd33fd24f4237ea38a83b3beb9725cfc24eb486`
- Clean code parent: `8108d986e95d66e74cdb222695b9c94f81350c26`
- Status: immutable preregistration only; no request authorized in this run

This document instantiates the single model-neutral probe permitted by
`frame_oracle_v14_stage_a_model_readiness_gate_20260809.md`. It does not
authorize Stage A, fixture authoring, or semantic evaluation.

## Exact request

The successor must create `request.json` with exactly these UTF-8 bytes,
including the final LF and no other bytes:

```json
{"model":"qwen2.5:7b","prompt":"Output exactly READY7K2","stream":false,"options":{"temperature":0,"num_predict":16},"keep_alive":0}
```

The preregistered request SHA-256 is
`60b30c2d270ec9093379f7ae0a507e31353d496b6db191c45d6787d602abf950`;
the byte count is `133`.
The fixed normalized sentinel is `READY7K2`. The response-body hard limit is
65536 bytes. Server readiness has a 30-second timeout, the sole HTTP request
has a 300-second timeout, and teardown has a 30-second timeout.

The exact endpoint is `http://127.0.0.1:11439/api/generate`. The request must
be issued by a hash-frozen local HTTP client inside the same network-unshared
Bubblewrap namespace as the frozen server and runner. No host-network client,
stdin, terminal, retry, redirect, streaming request, repair, or second request
is permitted. The launcher must set `Content-Type: application/json`, reject
non-2xx status, and preserve the raw request and response hashes.

## Frozen environment and mounts

Before launch, the outer harness must verify:

- Ollama SHA-256 `cd0f8bac72d0441ae75bdb182f1f75a7b8dfa63f2e1d16bc31fa570523b1d7c9`;
- `llama-server` SHA-256 `dbfeea380cdc1de9bbfe32399befbcd8381a3c5ac83e573d79d0fa41bdc40037`;
- model manifest SHA-256 `845dbda0ea48ed749caafd9e6037047aa19acfcfd82e704d7ca97d631a0b697e`;
- the prior 22-entry runtime/model closure and every content-addressed model
  blob; and
- the HTTP client's executable and dynamic-library closure, recorded before
  namespace creation.

The namespace must use `--unshare-all`, `--new-session`, `--die-with-parent`,
and `--clearenv`. It may mount read-only only the verified executable/runtime
closure, verified model closure, exact request file, CA-independent local HTTP
client closure, and necessary kernel pseudo-filesystems. It receives one empty
writable receipt directory and a tmpfs. Stage-A inputs, project files,
conversation or memory state, candidate/source/test files, fixture material,
sealed material, and semantic-free-lane material must be absent. Denial probes
for those classes are mandatory before the request.

## Exact adjudication

The successor must parse the sole response as UTF-8 JSON, require `done=true`,
require the returned `model` to equal `qwen2.5:7b`, and normalize only the
`response` field by removing leading and trailing ASCII whitespace. The result
is `READY` iff that normalized field is exactly `READY7K2`, all parent-gate
predicates hold, exactly one request and one terminal response occurred, the
loaded model identity is receipt-proven, and all server/runner/client processes
terminate within the frozen bound. Otherwise it is `NOT_READY`.

The response is transport evidence only and must never become fixture,
candidate, prompt, or semantic evidence. Any discrepancy consumes this probe;
no in-place repair or outcome-derived retry is allowed. A later probe requires
a fresh preregistration that does not use this response.

This preregistration authorizes no invocation in the present run. V14 remains
sealed, unopened, and unconsumed.
