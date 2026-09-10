# Run 20260724T135659Z-e1-residual-p1-m0-v1-1: e1-residual-p1-m0-v1-1

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T13:56:59Z`
- Finished: `2026-07-24T13:57:02Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does adding an identity residual path to every block propagate terminal-settle
field mass upstream and reproduce Mesto's early-to-middle P1 depth profile,
under the same seed-1729 grammar, probes, and P1/M0 diagnostics as the serial
control?

## Hypothesis or expected behavior

Residual paths should improve upstream propagation. A positive constructed
control would move a material share of global top-5% squared field mass out of
block 6 at longer settlement depths, with observable per-block M0 alignment.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seed: `1729`; identical deterministic grammar and probe construction
  to the serial P1/M0 sweep.
- Architecture: residual teacher and residual student,
  `x_(l+1) = x_l + tanh(W_l x_l + b_l)`.
- Depths: `T = [1,2,4,8,16,32,64,128]`; KD and teacher-free CE.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/e1_residual_p1_m0_v1_1.json`,
  `artifacts/e1_residual_p1_m0_v1_1.npz`, and
  `artifacts/artifact_manifest.json`.
- Focused tests: 14 passed.
- Result SHA-256:
  `5bdc0bb63f37efbe617c476b0e4290716e4aa3b56cbe6abdc6dec5996d1eb175`.
- Fields SHA-256:
  `46051c2521ebd3ab4029f27769827bbfab4d0dcd6d3ac38329d3c83eae877c2e`.
- All settlements preserved weights and used one terminal student.

## Interpretation

**Observed:** KD and CE assigned 100% of global top-5% squared field mass to
block 6 at every depth. At `T=128`, KD block L2 norms were approximately
`[0, 7.37e-8, 1.28e-5, 3.69e-4, 5.51e-3, 5.79e-2]`; CE was effectively
identical. Blocks 3--6 had epsilon/descent cosines approximately
`[0.735, 0.998, 0.999, 1.000]`, but magnitude ratios remained strongly
depth-dependent and block 1 was unobservable.

**Inferred:** residual skips improve the magnitude of finite-time upstream
propagation but do not change the readout-local global frontier in this
settlement formulation. Residual connectivity alone does not reproduce
Mesto's early-to-middle profile.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Run the same frozen P1/M0 protocol on a minimal residual token-mixing
substrate. Keep M3/M4 blinded.
