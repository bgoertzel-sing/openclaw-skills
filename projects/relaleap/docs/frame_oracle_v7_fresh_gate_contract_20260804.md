# Frame-oracle v7 fresh-gate contract

- Contract: `frame-oracle-v7-gate-1`
- Frozen: `2026-08-04T09:25:00Z`
- Parent scientific result: v6 failed closed after 45/48 calls on a
  predicate/abstention consistency exception
- Status: fresh successor battery sealed; no v7 implementation admitted

## Boundary

The consumed v6 cases, raw proposals, normalized rows, and answers are failure
evidence only. They may not be used as v7 unit fixtures, training examples,
prompt demonstrations, selection targets, or a claimed fresh pass. This
successor was authored from the pre-existing closed ontology and coverage
counts without inspecting the v6 failing case, proposal, or response. The
author knew the terminal exception class and the aggregate call count.
Accordingly, v7 is exact-case-disjoint and process-sealed, not strictly
outcome-blind.

## Fresh battery

`sealed/frame-oracle-v7/` contains 24 new sentences, case IDs, strata, and a
SHA-256 commitment to process-sealed exact frames. Integrity validation checks
case/answer alignment, schema coverage, commitment, and zero exact sentence
overlap with v1--v6 and the opened offline-readout-v1 corpus. The battery has
not been supplied to an oracle and remains `opened=false`.

## Eligibility before opening

1. State one bounded v7 hypothesis without consulting `gate_answers.json` or
   v6 case/proposal/normalized-row contents.
2. Use an isolated descendant branch and only independent synthetic fixtures.
3. Preserve the atomic state machine: `consumed_pending` before inference,
   per-call checkpoints, no resume, exact model-digest verification, and a
   terminal consumed state on every post-transition failure.
4. Freeze a clean commit, prompt/schema/source hashes, exact paired decode,
   import provenance, and focused/exposed/full tests in a new manifest.
5. Stop for a separate one-use run. Passing remains 24/24 schema-valid,
   paired-deterministic, and exact with every stratum perfect.

No labels, readout, substitution scorer, or semantic loss is admitted unless
this fresh gate later passes and its own downstream gates pass.
