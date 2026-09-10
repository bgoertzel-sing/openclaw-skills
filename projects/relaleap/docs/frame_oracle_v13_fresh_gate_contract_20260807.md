# Frame-oracle v13 fresh-gate contract

- Contract: `frame-oracle-v13-gate-1`
- Frozen: `2026-08-07T01:27:15Z`
- Parent scientific result: v12 failed its exact one-use semantic gate
- Status: fresh successor battery sealed; integrity passed; unopened

## Boundary

V12 is permanently consumed. Its opened cases, proposals, responses,
normalized rows, answers, aggregate failure identifiers, and terminal failure
identifiers were not inspected or used as v13 fixtures, prompt demonstrations,
training examples, or tuning targets. This successor was authored only from
the pre-existing closed ontology and coverage contract after aggregate v12
counts and per-stratum counts were known. Automated freshness validation may
compare exact sentence strings against v12 public cases but emits only a
non-identifying overlap count. V13 is therefore intended to be
exact-case-disjoint and process-sealed, not strictly outcome-blind.

## Fresh battery

`sealed/frame-oracle-v13/` contains 24 new sentences, case IDs, strata, and a
SHA-256 commitment to exact closed frames. Integrity validation checks
case/answer alignment, categorical schema, commitment, frozen stratum counts,
and zero exact sentence overlap with v1--v12 plus offline-readout-v1. The
battery has not been supplied to an oracle and must remain `opened=false`
until a later preregistered gate.

Frozen coverage is: all five predicates; four direct, six explicit-negation,
five possible, one paraphrase, four abstention, and four
world-knowledge-trap cases; exactly five `located_in` frames. All
explicit-negation and possibility labels must align exactly with their named
strata, and unknown frames must use empty entities with unknown
polarity/modality.

## Eligibility before opening

1. State one bounded source-derived v13 hypothesis without consulting v12 raw
   outcomes, surfaced identifiers, or `gate_answers.json`.
2. Use independent synthetic fixtures on an isolated descendant branch.
3. Preserve the conservative atomic consumption state machine and exact
   source/import/model provenance.
4. Freeze a clean implementation, exact command, and focused/exposed/full
   tests in a separate unopened manifest.
5. Stop for a separate one-use run. Passing remains 24/24 schema-valid,
   paired-deterministic, and exact with every stratum perfect.

No label corpus, readout, substitution evaluation, or semantic loss is
admitted unless this gate and all downstream preregistered gates pass.
