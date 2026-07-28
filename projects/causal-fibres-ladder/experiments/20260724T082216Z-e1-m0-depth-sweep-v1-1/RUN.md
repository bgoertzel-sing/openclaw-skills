# Run 20260724T082216Z-e1-m0-depth-sweep-v1-1: e1-m0-depth-sweep-v1-1

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T08:22:16Z`
- Finished: `2026-07-24T08:22:19Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

On one fixed reduced terminal homotopy student and one fixed probe set, does
increasing settlement depth from `T=1` through `T=128` propagate the settled
error field upstream, shift the P1 top-5% frontier away from the readout, and
make whole-model M0 equivalence to the BP descent field identifiable?

## Hypothesis or expected behavior

Greater depth should propagate a nonzero field upstream. If limited depth alone
explains the prior `T=8` result, the top-5% depth profile should begin moving
toward the early/middle blocks and M0 should become measurable there.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Config: `configs/e1_homotopy_smoke.json`, seed `1729`.
- Criteria: `configs/e1_e2_acceptance_v1_1.json`.
- Frozen depths: `[1,2,4,8,16,32,64,128]`.
- Same terminal-student hash and same persisted probe identity for every KD/CE
  condition.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`
- Twelve focused E1/M0 tests passed.
- Results SHA-256:
  `c227eb0823d1082090b90e6cf3a8938a57e57f77b45d1c6c19512d0826d0c62a`.
- Field NPZ SHA-256:
  `e0f78181aa8e27641287de1f173f1e262029a895d168cfdf5de1871730ab25ba`.
- All sixteen settlements preserved the terminal weights.
- At every depth and under both objectives, block 6 retained `100%` of global
  top-5% settled-field mass.
- At `T=128`, KD block L2 norms were approximately
  `[0, 1.0e-9, 1.15e-6, 9.40e-5, 2.80e-3, 5.22e-2]`; CE was
  `[0, 1.16e-9, 1.32e-6, 1.04e-4, 3.11e-3, 5.89e-2]`.
- At `T=128`, cosine to the BP descent field for KD blocks 3--6 was
  `[0.537, 0.9992, 0.9998, 1.0000]`; CE was
  `[0.560, 0.9995, 0.9998, 1.0000]`. Blocks 1--2 remained zero or too small
  for meaningful equivalence.

## Interpretation

**Observed:** greater depth propagates a progressively nonzero field from the
readout toward block 2, but six orders of magnitude separate upstream and
readout norms at `T=128`. The global frontier never leaves block 6. KD and CE
behave almost identically.

**Inferred:** finite settlement depth is not the sole explanation for the
disagreement with Mesto's supplied early/middle profile. The remaining likely
differences are field convention/normalization, update dynamics, architecture,
loss placement/scaling, or the distinction between this reduced student and
the reported 124M homotopy system.

**Decision:** do not unblind E2 M3/M4. Audit the exact Mesto/R8 field definition
and compare raw activation displacement, local prediction error, and parameter
gradient contribution under matched normalization. Treat blocks with
near-zero field norms as unobservable rather than assigning substantive zero
cosines.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Implement a constructed chain positive control plus a field-definition audit.
Only advance the settled-field E2 track after the audit identifies a
comparable substrate. The plain adjoint E2 track may be prepared, but its
fingerprints remain blinded until the pre-registered co-location statement is
operationalized against a valid local depth profile.
