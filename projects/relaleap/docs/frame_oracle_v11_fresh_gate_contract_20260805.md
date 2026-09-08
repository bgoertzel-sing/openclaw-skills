# Frame-oracle v11 fresh-gate contract

- Contract: `frame-oracle-v11-gate-1`
- Frozen: `2026-08-06T05:11:59Z`
- Parent scientific result: v10 failed its exact one-use semantic gate
- Status: fresh successor battery sealed; integrity passed; unopened

## Boundary

V10 is permanently consumed. Its opened cases, proposals, responses,
normalized rows, answers, and failure identifiers were not inspected or used
as v11 fixtures, prompt demonstrations, training examples, or tuning targets.
This successor was authored only from the pre-existing closed ontology and
coverage contract after aggregate v10 counts and per-stratum counts were
known. Automated freshness validation may compare exact sentence strings
against v10 public cases but emits only a non-identifying overlap count. V11 is
therefore intended to be exact-case-disjoint and process-sealed, not strictly
outcome-blind.

## Fresh battery

`sealed/frame-oracle-v11/` contains 24 new sentences, case IDs, strata, and a
SHA-256 commitment to exact closed frames. Integrity validation checks
case/answer alignment, schema coverage, commitment, frozen stratum counts, and
zero exact sentence overlap with v1--v10 plus offline-readout-v1. The battery
has not been supplied to an oracle and must remain `opened=false` until a
later preregistered gate.

## Eligibility before opening

1. State one bounded source-derived v11 hypothesis without consulting v10 raw
   outcomes or `gate_answers.json`.
2. Use independent synthetic fixtures on an isolated descendant branch.
3. Preserve the conservative atomic consumption state machine and exact
   source/import/model provenance.
4. Freeze a clean implementation, exact command, and focused/exposed/full
   tests in a separate unopened manifest.
5. Stop for a separate one-use run. Passing remains 24/24 schema-valid,
   paired-deterministic, and exact with every stratum perfect.

No label corpus, readout, substitution evaluation, or semantic loss is
admitted unless this gate and all downstream preregistered gates pass.
