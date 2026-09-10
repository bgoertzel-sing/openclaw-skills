# Frame-oracle v6 fresh-gate contract

- Contract: `frame-oracle-v6-gate-1`
- Frozen: `2026-08-04T01:27:05Z`
- Parent scientific result: v5 failed closed at 18/24 deterministic and
  18/24 exact
- Status: fresh successor battery sealed; no v6 implementation admitted

## Boundary

The consumed v5 cases, proposals, normalized rows, and answers are failure
evidence only. They may not be used as v6 unit fixtures, training examples,
prompt demonstrations, selection targets, or a claimed fresh pass. V6 work
must begin from a bounded source-level contract or a hypothesis fixed without
consulting those row contents.

The v6 author knew the aggregate v5 verdict, per-stratum summary, and failure
case identifiers because they appeared in the terminal preregistered report,
but did not use proposal or normalized-row contents. V6 cases were templated
from the pre-existing closed ontology and coverage counts, then frozen before
any v6 implementation or inference. The bundle is exact-case-disjoint and
process-sealed, but not strictly outcome-blind. Any claim requiring strict
outcome blindness needs a battery authored in a context without the v5
summary.

## Fresh battery

`sealed/frame-oracle-v6/` contains 24 new sentences, case IDs, strata, and a
SHA-256 commitment to process-sealed exact frames. Integrity validation checks
case/answer alignment, schema coverage, commitment, and zero exact sentence
overlap with v1--v5 and the opened offline-readout-v1 corpus. The battery has
not been supplied to an oracle and remains `opened=false`.

## Eligibility before opening

1. State one bounded v6 hypothesis without consulting
   `gate_answers.json` or v5 proposal/normalized-row contents.
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
