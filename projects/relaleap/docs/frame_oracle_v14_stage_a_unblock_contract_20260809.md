# Frame-oracle v14 Stage-A unblock contract

- Frozen: `2026-08-09T11:27:00Z`
- Status: fail-closed successor contract; no model request or fixture authoring authorized
- Basis: terminal `TRANSPORT_INFEASIBLE` receipt from the exact intended local topology

## Current adjudication

Stage A is `BLOCKED`. The frozen unprivileged, network-unshared Bubblewrap
topology cannot raise loopback on this host. The failure occurred before any
server, client, model load, request, response, fixture, or sealed access. It is
therefore infrastructure evidence only and says nothing about model semantics.

No successor may tune, repair, privilege, or substitute the failed topology
using its observed failure. No further local model-readiness probe is
admissible unless a new topology is independently specified and frozen before
any feasibility result, and then passes a model-free transport preflight.

## Exhaustive admissible unblock events

Stage A may move from `BLOCKED` only after exactly one of these independently
originating events is available:

1. **Externally produced Stage-A bundle.** A genuinely independent author
   produces a bundle under the already frozen four-input allowlist, author
   eligibility contract, I/O contract, and bundle schema. The persistent
   semantics worker may verify hashes and non-disclosing receipts but may not
   supply derivation logic or preview fixture content.
2. **Fresh local topology proposal.** A topology is specified without using
   any model response or sealed/fixture content and is hash-frozen before its
   first feasibility run. It must preserve cleared context, exact input
   denials, no external networking, and bounded teardown. It must first pass a
   separately preregistered model-free transport preflight. Only a later,
   separately preregistered one-use readiness probe may test model loading.
3. **Ben-approved protocol revision.** Ben explicitly relaxes or replaces a
   named independence, isolation, or transport requirement. The revision must
   be recorded as a new decision before execution; silence, scheduler
   recurrence, or tool availability is not approval.

These events are exhaustive. Merely finding another executable, port, address
family, namespace flag, IPC mechanism, or privilege route does not unblock
Stage A. Remote or paid compute remains forbidden without explicit approval.

## Mandatory successor checks

Before acting on an alleged unblock event, a successor must record:

- which one of the three events applies;
- immutable identities and hashes for every admitted input and executable;
- evidence that the proposal predates all results used to adjudicate it;
- denial receipts for project history, retired fixtures, candidate code,
  sealed v14, and external networking where applicable;
- exact one-use or rerun semantics and terminal failure handling; and
- an explicit statement that success does not itself admit Stage B, readout,
  substitution evaluation, or semantic loss.

Any missing predicate leaves Stage A `BLOCKED`. Failed evidence is preserved
as a counterexample and may not be repaired in place. V14 remains sealed,
unopened, and unconsumed.

## Permitted work while blocked

The semantics lane may verify seal integrity, exposed regressions, and receipt
consistency, or produce a concrete source-derived contract/counterexample that
does not depend on opened or sealed answers. It must not author v14 acceptance
fixtures, inspect candidate-derived cases, invoke a model, evaluate readout or
substitution, or introduce a semantic loss.
