# Run 20260715T153049Z-cla-detector-preregistered: cla-detector-preregistered

- Project: `omegasim`
- Started: `2026-07-15T15:30:49Z`
- Finished: `2026-07-15T16:02:15Z`
- Status: `succeeded; provenance-incomplete, hypothesis-generating only`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/omegasim/repos/omegasim`

## Question

Under the detector and thresholds frozen before outcome inspection, do A6
appraisal dynamics beat both exact-tuple linear and shuffled controls on CLA
compression margin and held-out prediction in at least four of five seeds in
any independently evaluated dimensionality stratum?

## Hypothesis or expected behavior

The fail-closed expectation was that most tuple/stratum cells would not promote.
A promoted cell would be bounded evidence for a reproducible CLA-proxy
difference, not proof of chaos, strange-attractor geometry, or semantic grammar.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds: `7,17,29,43,71`; A6 gain `5`; couplings `0.35,0.60`;
  delays `0,3`; strata `core4,roles8,full20`; controls
  `appraisal,linear,shuffled`; 1,024 steps with 128 burn-in.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`
- Primary JSON SHA-256: `2539b8381b8e85317a7ca4ae53643483153c8f3535dabbef282abec880902eb4`
- CSV SHA-256: `5dd819af1b76b40811712b8452adab8c5bcb57f1066847bf56cb779a7bd6e729`
- 180 rows completed in 31 minutes 26 seconds.
- One of 12 tuple/stratum cells promoted: coupling `0.60`, delay `3`,
  `roles8`, with appraisal beating both controls in four of five seeds.

## Interpretation

**2026-07-16 provenance audit:** The command imported `chaoslang` from a
second repository, but `git.txt` captured only the OmegaSim repository. The
dependency commit and dirty state therefore were not frozen in this ledger.
The dependency commit can be bounded to `974af31` from its reflog and the next
commit changed only report files, but cleanliness cannot be reconstructed.
Accordingly, the `4/5` result is not promotable replication evidence. See
`../../docs/cla_detector_provenance_audit_20260716.md`.

**Observed:** all exact-reconstruction/occupancy invariants passed. The promoted
cell had four matched wins; seed 29 missed because appraisal compression margin
(`118.6`) was below linear (`132.2`) despite lower held-out loss. No other cell
reached four wins; the next-highest cells reached three.

**Inference:** this is bounded positive evidence for an appraisal-specific
difference under the frozen CLA proxy in one preregistered regime. It does not
establish strange-attractor structure, semantic grammar, or detector
calibration. The selected cell still needs untouched replication.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Replicate coupling `0.60`, delay `3`, `roles8` with untouched seeds and no
detector changes. Complete Mackey--Glass and Lorenz--96 calibration before a
substantive OmegaSim strange-attractor claim.
