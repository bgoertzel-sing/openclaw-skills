# Run 20260715T041310Z-two-step-trainer-smoke-pypath: two-step-trainer-smoke-pypath

- Project: `hdpc-tiny-shakespeare`
- Started: `2026-07-15T04:13:10Z`
- Finished: `2026-07-15T04:13:16Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `projects/hdpc-tiny-shakespeare/repos/hdpc-tiny-shakespeare`

## Question

Can the pretrained `sshleifer/tiny-gpt2` student complete two local Tiny
Shakespeare ePC updates at `T={1,2}` with finite values, inspectable inference
traces, and layer-resolved PC-vs-BP gradient diagnostics?

## Hypothesis or expected behavior

Expected smoke behavior: no NaN/Inf; the first update should preserve the
self-teacher anchor; energy traces should remain numerically controlled; and
the second update should expose measurable but non-pathological PC/BP gradient
differences. This is not expected to establish useful language-model quality.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Model: cached Hugging Face `sshleifer/tiny-gpt2`
- Data: cached Tiny Shakespeare corpus from the project data loader
- Seed: 0; sequence length: 64; batch size: 2; optimizer LR: 1e-4
- Homotopy: `T={1,2}`, error step size 0.05, KD temperature 2.0

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Metrics: `artifacts/metrics.json` (SHA-256
  `a30c6efd697418a87f89658b629786070b716728874df5267341e8733c981ff2`)

## Interpretation

**Observed:** Both updates completed and every recorded energy/gradient value
was finite. At `T=1`, PC and BP gradients were identical to numerical
precision in both transformer blocks (mean cosine approximately 1.0, mean norm
ratio 1.0). At `T=2`, block mean cosines remained above 0.99998 while mean norm
ratios fell to 0.9590 and 0.9601. The `T=2` raw energy trace was
`1.092e-7 -> 1.714e-7 -> 1.432e-7`: bounded and tiny, but not strictly
monotone. Validation perplexity moved from 50329.824 initially to 50329.727
after step 1, then to 50332.941 after step 2 (`delta_ppl=+3.117` versus the
unchanged teacher).

**Interpretation:** The run passes the execution/finite-value and diagnostic
instrumentation smoke gates. It does not pass a directional learning gate over
both updates: the first update improved validation loss imperceptibly, while
the second worsened it. The non-monotone `T=2` energy trace also means the
current error step size should not be treated as certified for longer
relaxation. These two observations motivate a smaller error-step sweep and a
longer diagnostic smoke before any GPU proposal.

**Limitations:** Two batches and two updates cannot support quality or
convergence claims. The model is tiny, full-rank, and initialized exactly from
the teacher; LoRA is not implemented in this slice.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Run a local error-step sweep for `T=2` (and optionally `T=4`) with strict
relative energy-descent reporting, then repeat for enough updates to determine
whether validation loss and per-layer gradient ratios are stable.
