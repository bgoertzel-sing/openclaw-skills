# Frame-oracle v5 fresh-gate contract

- Contract: `frame-oracle-v5-gate-1`
- Frozen: `2026-08-03T17:25:00Z`
- Parent scientific result: v4 failed closed at 17/24 deterministic and 17/24 exact
- Status: fresh successor battery sealed; no v5 implementation admitted

## Boundary

The consumed v4 cases and responses are failure evidence only. They may not be
used as v5 unit fixtures, training examples, prompt demonstrations, selection
targets, or a claimed fresh pass. V5 work must begin from source-level contract
analysis or a hypothesis fixed independently of v4 case-level outputs.

The v5 author knew the aggregate v4 verdict and per-stratum summary but did
not inspect raw proposals or normalized rows. V5 cases were templated from the
pre-v4 closed ontology and required coverage strata, then frozen before any v5
implementation. Thus the bundle is case-disjoint and process-sealed, but not
strictly outcome-blind at the aggregate-stratum level. Any claim requiring
strict outcome blindness needs another battery authored in a context that does
not contain the v4 summary.

## Fresh battery

`sealed/frame-oracle-v5/` contains 24 new sentences, case IDs, strata, and a
SHA-256 commitment to process-sealed exact frames. Integrity validation checks
case/answer alignment, schema coverage, commitment, and zero exact sentence
overlap with v1--v4 and the opened offline-readout-v1 corpus. The battery has
not been supplied to an oracle and remains `opened=false`.

## Eligibility before opening

1. State one bounded v5 hypothesis without consulting `gate_answers.json` or
   v4 raw rows/responses.
2. Use an isolated descendant branch and only independent synthetic fixtures.
3. Preserve the v4 state machine: atomic `consumed_pending` before inference,
   per-call checkpoints, no resume, exact model-digest verification, and a
   terminal consumed state on every post-transition failure.
4. Freeze a clean commit, prompt/schema/source hashes, exact paired decode,
   import provenance, and focused/exposed/full test results in a new manifest.
5. Stop for a separate one-use run. Passing remains 24/24 schema-valid,
   paired-deterministic, and exact with every stratum perfect.

No labels, readout, substitution scorer, or semantic loss is admitted unless
this fresh gate later passes and its own downstream gates pass.
