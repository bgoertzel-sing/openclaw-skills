# CAROM GPT-2 arm — run record

- Status: `complete; artifacts verified; pod stopped`
- Pod: `26u0p4wpyal9ki`
- Resource: RunPod Secure Cloud, A100 SXM4 80 GB, USD 1.49/hr
- Initial start: 2026-07-21 16:31 PDT
- Repair extension approved: 2026-07-21 18:36 PDT, maximum 30 minutes / about
  USD 0.75 incremental

## Question

Can the frozen GPT-2-small CAROM arm complete 4,000 training steps and the
three planned checkpoint interventions?

## Observed status before repair

Training completed all 4,000 steps and saved checkpoints at steps 0, 500, ...,
4000. The intervention phase failed at its first checkpoint with
`ValueError: not enough values to unpack (expected 7, got 5)` while unpacking
the frozen corpus dictionary. The GPU was idle after the failure.

## Acceptance test

The repaired intervention-only continuation exits zero, writes the planned
machine-readable results under `/workspace/zerobot-runs/carom-gpt2/results/`,
those results and checkpoints are retrieved and hash-verified locally, and the
pod is stopped with provider state rechecked.

## Next command

Retrieve and inspect `/workspace/r9_carom_gpt2.py`, patch the corpus unpacking,
validate without retraining, then run only the post-training intervention
section against the retained checkpoints.

## Repair and execution

Three unpacking statements named fields absent from their right-hand sides.
The repair explicitly loads `SP`, `E`, and `ENT` from the frozen corpus and
adds `--interventions-only`, which refuses to run without retained checkpoints.
The original remote script was preserved as `r9_carom_gpt2.pre-fix.py`.

Command:

```text
python3 r9_carom_gpt2.py --interventions-only
```

The repaired source passed local and remote `py_compile`. The continuation ran
in tmux session `carom-interventions`, completed nine checkpoints in about 40
seconds, printed `DONE`, and exited zero.

## Results

- L2--4 task accuracy increased from 0.139 at step 0 to 0.412 at step 4000.
- Repaired itinerary tau rose from 0.040 to 0.904; coverage rose from 0.383 to
  0.710. The supplied tau-decline anomaly did not recur in this GPT-2 arm.
- At step 4000, natural accuracy was 0.412 versus shuffled 0.297 and smeared
  0.301 (`natural - shuffled = 0.115`), evidence that the natural trajectory
  had become causally useful on the frozen L2--4 corpus.
- The forced schedule scored 0.309 at step 4000, below natural. This means the
  particular fixed-amplitude/dwell clamp is not an oracle replacement for the
  learned natural trajectory.
- L5 accuracy remained weak: 0.214 at S=72 and 0.234 at S=120 at step 4000.
  More integration time recovered only 2.1 points and did not close the
  structural generalization gap.

These are single-seed checkpoint-panel observations. The repaired itinerary
implementation still predates the full v2/v3 constructed-control program, so
mechanistic interpretation remains provisional.

## Verification and artifacts

- `artifacts/results/summary.json`: nine checkpoint rows; every row contains
  natural/forced/shuffled/smeared intervention results and S=72/100/120 budget
  results; checked with `jq`.
- `artifacts/checkpoints/`: nine `.pt` checkpoints retrieved.
- `artifacts.sha256`: SHA-256 manifest for 20 files.
- Total retrieved size: 105 MiB.
- Pod stopped at 2026-07-21 18:39:41 PDT and provider state rechecked as
  `EXITED`; the separate RelaLeap pod remained `RUNNING`.
