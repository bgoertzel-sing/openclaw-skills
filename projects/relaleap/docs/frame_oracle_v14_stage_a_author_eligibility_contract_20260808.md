# Frame-oracle v14 Stage-A author eligibility contract

- Frozen: `2026-08-08T11:20:00Z`
- Parent: clean frame-oracle v13 commit `8108d986e95d66e74cdb222695b9c94f81350c26`
- Status: preflight contract only; no author or fixture admitted

An author is eligible only if all predicates below are established before its
process starts. Self-attestation by the proposed author is insufficient.

1. The executable, model artifact, and launcher command are identified by
   immutable SHA-256 digests. Their bytes must predate this launch and must not
   have been written or modified by the persistent semantics worker after that
   worker saw any retired v14 fixture detail.
2. The process is freshly initialized with no inherited conversation,
   persistent memory, retrieval index, cache, session continuation, hidden
   user prompt, or tool state. The launcher supplies only the four inputs
   frozen by the Stage-A isolation contract.
3. The launcher is an independently existing general authoring mechanism. No
   fixture-generating algorithm, examples, templates, predicate-specific
   sentence suggestions, or derivation guidance authored by this persistent
   worker may be embedded in the launcher, executable, model prompt, or files.
4. Bubblewrap exposes exactly the frozen four readable inputs, an empty writable
   output directory, required runtime libraries whose hashes are recorded, and
   kernel pseudo-files needed for execution. Network is unshared. Project
   history, experiments, sealed material, candidate source/tests, conversation,
   memory, and semantic-free-lane material are absent.
5. A trusted outer launcher, not the author, records the executable and runtime
   closure hashes, exact argument vector, environment, mount table, namespace
   settings, input manifest, start time, and denial probes before authoring.
6. The author can emit the already frozen Stage-A bundle schema without an
   interactive repair, retry with changed inputs, or persistent-worker preview.
   Any launch, schema, premise, or provenance failure permanently retires that
   attempt and its fixture content.

The preflight decision is binary. Missing evidence, mutable model aliases,
provider-side hidden context, unhashable remote execution, inherited agent
sessions, or a worker-authored fixture generator yield `INELIGIBLE`. An
eligible author still does not make its output admissible: the frozen bundle
verifier must pass non-disclosingly, and Stage B must occur in a later turn.

No eligible author is currently identified. This contract does not authorize
author invocation, fixture creation, v14 access, candidate inspection, oracle
or model calls, labels, readout, substitution evaluation, semantic loss,
remote compute, publication, or push.
