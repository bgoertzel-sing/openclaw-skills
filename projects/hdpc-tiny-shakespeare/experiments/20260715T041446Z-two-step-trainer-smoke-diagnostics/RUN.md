# Run 20260715T041446Z-two-step-trainer-smoke-diagnostics: two-step-trainer-smoke-diagnostics

- Project: `hdpc-tiny-shakespeare`
- Started: `2026-07-15T04:14:46Z`
- Finished: `2026-07-15T04:14:57Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `projects/hdpc-tiny-shakespeare/repos/hdpc-tiny-shakespeare`

## Question

Can the pretrained `sshleifer/tiny-gpt2` student complete two local Tiny
Shakespeare ePC updates at `T={1,2}` with finite values, inspectable inference
traces, and layer-resolved PC-vs-BP gradient diagnostics?

## Hypothesis or expected behavior

Expected smoke behavior: no NaN/Inf; exact self-teacher behavior at `T=1`;
numerically controlled inference; and measurable layer-wise PC/BP differences
at `T=2`. This run is not intended to establish model quality.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Model: cached Hugging Face `sshleifer/tiny-gpt2`
- Data: cached Tiny Shakespeare corpus; seed 0
- Sequence length 64; batch size 2; optimizer LR 1e-4
- Homotopy `T={1,2}`; error step 0.05; KD temperature 2.0

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Metrics: `artifacts/metrics.json` (SHA-256
  `b048678b058c2784e72633048e0f45e48ec4562a3e7e8182f824f1e3f74c68d0`)

## Interpretation

**Observed:** Both updates completed with finite energies and gradients. At
`T=1`, transformer-block mean PC/BP cosine and norm ratios were 1.0 to
numerical precision. At `T=2`, block mean cosines were 0.99999984 and
0.99998883; norm ratios were 0.95899 and 0.96014. Validation perplexity moved
50329.824 -> 50329.727 -> 50332.941. Strict energy descent failed: at `T=2`,
the trace was `1.092e-7 -> 1.714e-7 -> 1.432e-7`, with maximum increase
`6.219e-8`. The `T=1` strict flag also failed only because zero became a
roundoff-scale `8.19e-22`.

**Interpretation:** Execution, finite-value checks, and layer-resolved
instrumentation pass. Directional learning and relaxation convergence do not:
the second update worsened validation perplexity by 3.117 versus the teacher,
and `T=2` was not energy-monotone. A smaller error-step sweep is required
before longer training or a GPU proposal.

**Limitations:** This is two updates on a tiny full-rank model initialized from
the teacher. It supports no language-model quality or asymptotic convergence
claim; LoRA is not implemented here.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Run a local error-step sweep for `T=2` (optionally `T=4`) and require strict or
well-justified tolerance-relative energy descent before longer training.
