# Run 20260723T181654Z-h0-frozen-interface-cpu-final: h0-frozen-interface-cpu-final

- Project: `causal-fibres-ladder`
- Started: `2026-07-23T18:16:54Z`
- Finished: `2026-07-23T18:17:37Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent`

## Question

Can a reasonable ordinary-BP residual on the exactly frozen read/write
interface close more than half the oracle-teacher gap in the local CPU
synthetic-grammar smoke instantiation, with the confidence interval excluding
the failure region?

## Hypothesis or expected behavior

At least one linear, rank-4/8/16/32 low-rank, MLP, or LoRA-equivalent arm over
one or combined frozen reads will have the lower 95% paired-bootstrap bound of
`Gamma_L` or `Gamma_A` above `0.50`.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seed: `1729`; train-generator seed `1739`; validation-generator seed
  `1749`; per-arm sampling seeds are derived and stored in `metrics.json`.
- Formalization source commit:
  `e93983a875fbc2e1c7dd3f4d71b552060c4760d4`.
- Workspace commit at launch:
  `cdd7ba976ed88a1deb10c1d2c05d42061eda093f` with unrelated dirty work
  captured in `git.txt`.
- Wheel SHA-256:
  `5f8ca0f1d675658f34145b0e665b0f4e8f095c361aae03e785a56d852dc70c6e`.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`
- Machine-readable metrics: `metrics.json` (SHA-256
  `b3538ce9ebe6b8cc7519c09434526b6e07ba36e315ae4a68e6f5e2d7fe080c48`).

### Package validation

- Clean project venv created with Python 3.10.12 and inherited preinstalled
  system scientific packages to avoid duplicating CPU Torch.
- Wheel installed with `pip install --no-deps`.
- `causal-fibres doctor`: version 0.4.0, Torch 2.12.1+cpu, NumPy 2.2.6,
  CUDA unavailable.
- `causal-fibres smoke-test`: passed; loss `0.239274 -> 0.041310`.
- Released package suite: 54 tests passed.
- Experiment invariant suite: 3 tests passed.

### Direct measurements

- 2,048 training and 1,024 held-out examples; five independent binary factors
  plus an 8-way nuisance token.
- Six-layer frozen student: 30 pretraining updates. Frozen read sites were
  blocks 0, 2, 4, 5 separately and concatenated; write was additive final
  logits.
- 50 probe conditions completed. Total recorded probe-fit time was
  12.167 seconds on four configured CPU threads; the best MLP fit took 0.892
  seconds.
- Best arm: combined blocks 0/2/4/5, MLP width 32, 5,440 trained/deployed
  parameters, 128-wide read, output-rank bound 32.
- Raw base/residual/teacher cross-entropy:
  `0.967670 / 0.081691 / 0.074032`.
- Raw base/residual/teacher accuracy: `0.927734 / 1.0 / 1.0`.
- `Gamma_L=0.991430`, 95% paired-bootstrap CI
  `[0.990696,0.992202]` from 1,000 resamples.
- `Gamma_A=1.0`, CI `[1.0,1.0]`.
- Factor Γ: subject `0.848056`; object `0.836857`; tense `0.826813`;
  negation `0.861884`; agreement `0.819706`.
- Off-factor score spill: subject `0.130694`; object `0.124350`; tense
  `0.132403`; negation `0.136812`; agreement `0.142183`.

## Interpretation

**H0 passes for the toy/smoke interface.** Both the loss and accuracy criteria
pass, and the loss CI is well above the `0.50` failure boundary. Positive
factor-specific closure on every preregistered factor supports observability
beyond total task capacity.

This does not determine the paper's target GPT-2-small experiment. The run used
a deterministic oracle teacher and only one student/probe training seed;
bootstrap uncertainty covers held-out examples, not training-seed variation.
Accuracy saturates, so loss closure is the more discriminating metric. At the
final-logit write, LoRA-labeled and low-rank residual arms are algebraically
equivalent and should not be read as independent controls.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Stage 0B configuration is prepared at
`../../configs/h1_stage0b_toy_prepared.json` and was not run. Before advancing
the target ladder, benchmark activation storage/runtime and repeat H0 with the
specified GPT-2-small teacher, multiple seeds, and held-out factor
combinations. No paid compute was used or authorized.
