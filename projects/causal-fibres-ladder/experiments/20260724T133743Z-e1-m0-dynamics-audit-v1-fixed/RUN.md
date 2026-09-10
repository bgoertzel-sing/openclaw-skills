# Run 20260724T133743Z-e1-m0-dynamics-audit-v1-fixed: e1-m0-dynamics-audit-v1-fixed

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T13:37:43Z`
- Finished: `2026-07-24T13:37:46Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does the readout-local P1 frontier arise from a sign/normalization/extraction
mistake, or finite-time settlement dynamics in the reduced non-residual
six-block rig? Does Mesto-matched `eta=0.05, T=128, tau=6.4` change it?

## Hypothesis or expected behavior

An identity-chain positive control should show nonzero upstream settled fields
and epsilon-to-negative-adjoint alignment. If the profile is an overlarge-step
artifact, the Mesto-matched path should shift top-5% mass upstream.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Reconstructed terminal student from `configs/e1_homotopy_smoke.json`,
  seed 1729; same frozen probe identity as the depth sweep.
- Conditions: eta=0.05/T=128, eta=0.20/T=128, and six-block identity-chain
  positive control.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifact: `artifacts/e1_m0_dynamics_audit.json` (SHA-256
  `e4da8c8af89755e8122eae187b9de6afbc8d12a1e294fbfbbd9532a0ed72d507`).
- Focused regression `tests/test_e1_posthoc_m0.py`: 3 passed.

## Interpretation

**Observed:** Both terminal-rig conditions assign 100% of global top-5%
squared field mass to block 6. At Mesto-matched tau=6.4, blocks 1--2 are zero
and block-3 norm is 1.96e-11 versus block-6 1.58e-2. The larger existing-rig
tau=25.6 propagates farther upstream but leaves the frontier unchanged.

**Observed:** In the identity-chain control, every block has nonzero settled
field and epsilon/descent cosine is 1.0 to numerical precision; its top-5%
frontier nevertheless remains 100% in block 6.

**Inferred:** The sign convention and adjoint extractor work on a constructed
propagation control. Matching tau or changing field normalization does not
reconcile this non-residual serial rig with Mesto. Finite-time settlement has
an intrinsically readout-local amplitude profile here; it cannot test the
claimed transformer depth distribution without a residual/transformer-like
substrate or a separately declared per-block diagnostic.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Keep M3/M4 blinded. Specify and run a residual-block constructed control, then
a transformer-like reduced substrate, to distinguish expected residual-path
propagation from a late-block concentration pathology.
