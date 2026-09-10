# Frame-oracle v14 transport-feasibility preflight contract

- Frozen: `2026-08-09T07:27:00Z`
- Status: immutable no-inference contract; no model request authorized
- Supersedes: no prior probe; the consumed readiness probe remains terminal
  `NOT_READY`

The consumed readiness probe established a concrete environmental
counterexample: creating an unprivileged Bubblewrap network namespace does not
imply permission to raise its loopback device. Any future one-use readiness
probe must therefore depend on a separately completed transport-feasibility
receipt. Transport feasibility is infrastructure evidence only; it does not
establish model readiness, independent authorship, or Stage-A eligibility.

## Permitted preflight

A successor may implement and run a deterministic, model-free preflight that:

1. uses the intended readiness namespace flags (`--unshare-all`,
   `--new-session`, `--die-with-parent`, and `--clearenv`);
2. mounts no Ollama executable, runner, model manifest/blob, Stage-A input,
   fixture, candidate, sealed artifact, project history, or semantic-free-lane
   material;
3. attempts the required loopback setup before launching any server;
4. if loopback setup succeeds, starts only a hash-frozen inert HTTP echo server
   on the intended address family and an ephemeral non-readiness port;
5. issues only a fixed non-model request whose bytes and client identity were
   frozen before namespace creation; and
6. records namespace, loopback, bind, request-count, response-hash, denial,
   process, and bounded-teardown receipts without response-derived repair.

The inert response must contain no model prompt, sentinel, fixture text, or
semantic content. No `/api/*` endpoint is permitted. Host networking, remote
compute, external network access, and privileged namespace repair are
forbidden.

## Adjudication and reuse

`TRANSPORT_FEASIBLE` requires every predicate above, exactly one inert request
and response, and successful bounded teardown. Any discrepancy is
`TRANSPORT_INFEASIBLE`. Unlike a model probe, this model-free preflight may be
rerun unchanged solely to establish reproducibility; its output cannot alter
the contract or select a transport. A changed namespace, address family,
server, client, request, or mount closure requires a new contract.

A transport receipt is admissible for a later readiness preregistration only
when that preregistration uses the identical verified topology. The later
model probe must still be newly preregistered and one-use. The consumed
133-byte probe and its endpoint may not be retried or repaired. No outcome of
this preflight authorizes inference, fixture authoring, Stage A, Stage B,
readout, substitution evaluation, or semantic loss. V14 remains sealed,
unopened, and unconsumed.
