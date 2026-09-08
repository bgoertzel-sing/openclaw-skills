# Decision Log

## D-20260726-instrument-first: Validate instruments before guided training

- Date: `2026-07-26`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `TASKS.md` P0/P1 specification task

### Context

The synthesis programme depends on calibrated HDC probes and an extractable frame-layer readout.

### Decision

Run P0/P1 before interpreting any closure or guided-training result; P2 gates P5 as stated in
the supplied programme.

### Alternatives considered

Start direct GPT-2 guided training or assume the coherence-aware scaling law.

### Rationale and evidence

The supplied June 3 HDC theorem visibly establishes a random cleanup form with
`exp(-cD/k)`. Source audit subsequently located a conditional coherence-aware
derivation with `exp(-cD(1-nu)/k)` in the later July 25 HDC manuscript, under
explicit random-atom, isometric-binding, role-decorrelation, and crosstalk-
independence assumptions. Its numerical constants and the applicability of
its near-duplicate construction to hierarchy features still require
instrument validation. Evidence: `docs/p0-p1-spec.md`, Section 12.

### Consequences

The executable instrument specification is the first deliverable; P0
implementation is next. No performance, frozen-model, or linguistic-
universality claim follows from the specification.

### Revisit trigger

P1 produces a reproducible calibration result or falsifies a required measurement assumption.

## D-20260726-layered-p1-evidence: Separate cleanup, readout, and hierarchy-geometry claims

- Date: `2026-07-26`
- Status: `accepted`
- Decision owner: delegated research agent under the instrument-first decision
- Related task/run/commit: `docs/p0-p1-spec.md`

### Context

The synthesis proposes that HDC capacity discharges CGCCT probe calibration
and that implicational hierarchies occupy the near-duplicate regime. The
displayed results govern different layers: cleanup of an admissible HDC query,
a learned residual-to-frame readout, and the representation geometry chosen
for hierarchy features.

### Decision

P1 has separate oracle-code and learned-readout gates. It also has both
independent-feature and planted constituent-sharing hierarchy fixtures. A
planted near-duplicate fixture may validate conditional scaling but may not be
reported as confirmation that linguistic hierarchies induce the geometry.

### Alternatives considered

Use only the planted composite hierarchy and treat a matching exponent as
confirmation of Conjecture 1; combine cleanup and learned-readout errors into
one calibration curve.

### Rationale and evidence

CGCCT Theorem 7.3 assumes delta-calibrated probes but does not define an
empirical delta. HDC cleanup bounds do not cover the factorization and
optimization error of a learned `K`. Eq. 4 with independent feature atoms is
a valid construction in which implication adjacency alone does not create
near-duplicate feature codes.

### Consequences

Failures can be localized as `HDC_law_failed`, `readout_not_calibrated`, or
`instrument_failed`. Conjecture 1 remains unresolved after a planted-only
scaling pass.

### Revisit trigger

A non-planted learned or natural hierarchy reproducibly induces adjacency-
specific coherence under sealed evaluation.

## D-20260727-p0-g1-fail-closed: Do not advance to P1 after saturated P0 curve

- Date: `2026-07-27`
- Status: `accepted`
- Decision owner: delegated progress worker under instrument-first decision
- Related task/run/commit: `experiments/20260726T184741Z-p0-selftest-v2/`, `fa11721`

### Context

The initially interrupted P0-G1 run was completed from a fresh single-threaded
local process. Both 36-cell payloads are byte-identical, but the frozen
validator returned false.

### Decision

Treat P0-G1 as failed closed and do not start P1A or P1B. Preserve the replay
artifacts and gate outcome. Any change to the P0 grid, fixture, or qualitative
gate needs explicit authorization and an independent new run.

### Alternatives considered

Treat the saturated accuracy curve as an implicit positive capacity trend, or
advance because all other curves pass their local checks.

### Rationale and evidence

The frozen P0-G1 contract requires every eligible curve to have positive
`D/k`--accuracy association. For `k=4,M=32`, all six values are exactly 1.000;
its Spearman association is 0.0. The two replays have SHA-256
`e0602a37c97dde9d7fa8704bf0d4fe9aa0ccae7be5196dd267e3cdcae4d23f46`; the
validator artifact SHA-256 is
`719215ee8b08f88ced2847b55eddc277b488d2e21407e1af52f60203ae5c89e1` and says
`passed: false`.

### Consequences

The programme has a reproducible deterministic P0 artifact, but no passing
qualitative capacity calibration. P1 results would be out of sequence and are
not interpretable under the specification.

### Revisit trigger

Benjamin explicitly authorizes a revised P0 design or gate contract that
handles ceiling saturation, while retaining this failure as prior evidence.

## D-20260727-p1b-gpu-calibration: Permit bounded GPU calibration after CPU smoke

- Date: `2026-07-27`
- Status: `accepted conditionally`
- Decision owner: Benjamin Goertzel
- Related record: `experiments/20260727T225600Z-p1b-gpu-calibration-planned/REMOTE_JOB.md`

### Context

P1B's exact planted-PCFG six-layer fixture is the implementation long pole.
Ben prefers a GPU start early tomorrow morning, but no P1B code has yet passed
its local smoke gate.

### Decision

After the local CPU smoke passes, permit the three specified P1B calibration
seeds on a single compatible 24 GiB GPU under a 4-hour / USD 10 hard cap.
The calibration results then freeze criteria before any of the five sealed
confirmation seeds run.

### Consequences

No pod may be created before the smoke and a concrete remote-job record are
complete. No hyperparameter or threshold changes may be made while viewing
calibration outcomes. Confirmation remains a separate sealed phase.

### Revisit trigger

Remote smoke mismatch, a price above USD 1/hour, missing artifacts, or a need
to alter the fixture stops the job and returns it to local repair.

### Supersedes or superseded by

Amends the CPU-only sequencing constraint for P1B calibration only; it does
not authorize any P2+ or confirmation GPU run.

## D-20260727-p0-resolution-grid: Amend P0 fixture to expose capacity transition

- Date: `2026-07-27`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `experiments/20260727T213214Z-p0-g1-v2-authorized-grid/`, `ce7616d`

### Context

P0-v1 was bitwise reproducible but its `k=4,M=32` curve was 1.000 throughout,
so the unchanged positive-Spearman rule had no resolution.

### Decision

Retain P0-G1 and all deterministic conventions; replace only the fixed grid
with `D={32,64,128,256,512,1024}`, `k={32,64,128}`, `M={32,256}`. Preserve
the v1 failure as ceiling evidence.

### Rationale and evidence

A 128-trial scout showed a broad transition. The two 2,048-trial v2 payloads
were byte-identical and P0-G1 passed with Spearman 1.0 for all six curves.

### Consequences

P1A may begin CPU-local preflight. This does not validate a P1 law or
hierarchy geometry.

### Revisit trigger

Any later grid/gate amendment requires explicit authorization.

### Supersedes or superseded by

Amends D-20260727-p0-g1-fail-closed's blocked consequence; it does not erase
the v1 failure.

## D-20260728-p1b-code-realization: Freeze P1B target-code grid and arms

- Date: `2026-07-28`
- Status: `accepted`
- Decision owner: Benjamin Goertzel; concrete amendment selected by delegated
  ProtoMega review under Ben's authorization to choose or consult ProtoMega
- Related task/run/commit: `TASKS.md` P1B calibration;
  `docs/p0-p1-spec.md` §6.7

### Context

P1B required a fresh residual-to-HDC readout for each dimension and named
independent and planted hierarchy-code arms, but did not fix their dimension
grid or exact target-code realization. A silent implementation choice would
change the scientific fixture.

### Decision

Freeze `D={64,128,256,512,1024,2048,4096}` and the Eq.-4-compatible
role-bound bipolar code recipes in §6.7. The independent arm uses mutually
independent feature atoms; the planted arm uses F3-style sequential
role-bound constituent replacement. Both retain the PCFG distractor as a
frame role and share model/residual/split/seed across arms.

### Rationale and evidence

The grid brackets the fixed 128-dimensional residual from compression through
32x expansion while avoiding an unsupported transplant of P1A's cleanup grid.
Sequential replacement gives known adjacent coherence only in the positive
control; independent atoms preserve the counter-control required to test the
conjecture's non-implication. ProtoMega review was checked against the
existing Eq. 4 and F3 conventions.

### Consequences

The calibration runner can now be implemented and tested locally. It must
stream targets, record peak memory and target-code hashes, and fail closed if
the approved resource envelope cannot execute the frozen design.

### Revisit trigger

Any change to the grid, atom namespace, role terms, or planted geometry
requires a new explicit amendment before opening confirmation seeds.

## D-20260803-p1g2-contract-v2: Interpret P1-G2 only under labeled post-hoc repair

- Date: `2026-08-03`
- Status: `accepted`
- Decision owner: Benjamin Goertzel authorized repair and proceeding on
  2026-08-02; concrete mapping implemented by the delegated progress worker
- Related task/run/commit: `experiments/20260803T080400Z-p1g2-contract-v2/`,
  nested commit `b34b6f1`

### Context

The five returned confirmation artifacts were hash-valid but the v1 contract
omitted oracle confirmation metrics and the P1A-derived `D_pred` mapping. Ben
authorized a versioned repair using already opened deterministic artifacts.

### Decision

Retain criteria v1 byte-for-byte. Create interpretation contract v2, always
labeled `post_hoc_contract_repair_not_sealed_confirmation`. Map each P1B
`(seed,H,code-arm)` condition using `k=H`, P1A/F1/F3 `M=32`, and the maximum
adjacent feature-code coherence measured at each candidate dimension; select
the first frozen dimension satisfying the P1A formula. Reconstruct oracle
scores from the exact manifest and target generator, select thresholds only on
the calibration split, and evaluate confirmation without refitting. Reject all
source, seed, manifest, grid, sample-order, cell-count, and array-shape drift.

### Alternatives considered

Stop interpretation permanently; rerun the oracle arm remotely; use hierarchy
length as dictionary size; use total lexical-plus-feature bundle load as `k`;
or inspect outcomes while selecting a favorable mapping.

### Rationale and evidence

The chosen mapping transfers the P1A F1/F3 H-child constructed hierarchy
condition without extrapolating below the calibrated `M=32`. Oracle codes and
scores are deterministic functions of already opened sample identities, so no
model or seed rerun is needed. The implementation passed 31 tests, verified all
five artifacts, and produced byte-identical full results. Both oracle and
linear-K fail the absolute P1-G2 criteria, yielding `instrument_failed` under
v2; the paired linear-minus-oracle condition separately passes.

### Consequences

P1-G2 is now evaluable only under the post-hoc v2 label. It must not be
described as a sealed v1 result. The `instrument_failed` classification stops
downstream P2-P6 interpretation under the programme gate. No further P1 GPU
work is required or authorized.

### Revisit trigger

A new prospectively frozen experiment, or evidence that the deterministic
oracle reconstruction does not match the exact target-code contract.

## D-<YYYYMMDD>-<short-slug>: <Decision title>

- Date: `<YYYY-MM-DD>`
- Status: `proposed | accepted | superseded | rejected`
- Decision owner: Benjamin Goertzel or delegated role
- Related task/run/commit: `<pointer>`

### Context

### Decision

### Alternatives considered

### Rationale and evidence

### Consequences

### Revisit trigger

### Supersedes or superseded by
