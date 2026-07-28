# Run 20260718T073312Z-epc-outcome-6layer-run2: six-layer ePC outcome gate

- Project: `relaleap`
- Started: `2026-07-18T07:30:17Z`
- Finished: `2026-07-18T10:57Z`
- Status: `distillation complete; promotion failed; downstream outcome battery not run; pod terminated`
- Provider: RunPod
- Pod: `xkgkjbake2tpe1`
- Source commit: `7d4d4dc9ee0f141bef1e6da48249f92bb4021b7e`
- Remote-job contract: `REMOTE_JOB.md`

## Question

Does the frozen three-seed, matched six-layer GPT-2-width ePC outcome protocol
pass its preregistered distillation, structural, adaptation, and forgetting
gates against the BP controls?

## Frozen inputs

- Distillation protocol SHA-256:
  `ba89ac189a5e8635806157794f4d66c87b2ca6d011ead39dd3505a98b9a473ab`
- Outcome protocol SHA-256:
  `4a572da67cffce1ff9a32110e00e60c94413f3a974998b86575f2f1894288ab2`
- Seeds: `1729`, `3253`, `6421`
- Public model/data inputs only: pinned GPT-2, WikiText-103, and TinyStories.

## Execution

The frozen six-layer-student distillation runner began in tmux session `train`
at approximately `2026-07-18T07:58Z` and completed at `10:23Z`. It produced
all 12 expected records: three seeds times BP+CE, update-matched BP+KD, ePC+KD,
and wall-clock-matched BP+KD, plus nine safetensors checkpoints.

The config-file SHA-256 is `ba89ac...`; result records intentionally report
the canonical-JSON protocol SHA-256 `ac073e...`, as implemented by
`_canonical_hash(protocol)`. This is not protocol drift. The source commit in
the result summary is the frozen `7d4d4dc...`.

## Distillation result

**Observed:** the frozen promotion rule failed:

- mean validation-loss gain versus update-matched BP+KD: `-0.5208975474` nats;
- mean validation-loss gain versus wall-clock-matched BP+KD:
  `-1.4945918017` nats;
- maximum per-seed regression versus update-matched BP+KD:
  `0.5689785704` nats;
- no-seed-regression, both gain tests, and all-block nonzero-credit requirement
  failed; finite metrics, monotone energy, record completeness, and three-seed
  requirements passed.

**Interpretation:** this is a distillation-promotion null for the frozen ePC
condition. It does not answer the separately frozen structural,
adaptation/forgetting, or TinyStories-shift outcome question.

## Retrieval and cleanup

- Retrieved 40 result files (3,219,085,399 bytes), including nine final
  safetensors checkpoints, all per-arm JSON records, and `summary.json`.
- Strict per-file SHA-256 comparison between pod and local results passed.
- Training-log SHA-256:
  `3a6e9fb2214b756c2ecf30b7efd55e1822a539a98dc730a5ac584ff761b50d06`.
- Deterministic aggregate over sorted result-file hashes:
  `913a73b5e08b913889f95e5108daeeef0770a2a5126b6fa9a99119111a893387`.
- RunPod deleted pod `xkgkjbake2tpe1`; subsequent active-pod inventory was
  empty. No job-created network volume existed.

## Exit and limitation

- Distillation runner exit status: `0` (normal completion).
- Outcome runner exit status: not started.
- The heartbeat cleanup terminated the idle pod after verified distillation
  retrieval, before running `run_gpt2_outcome_gpu.py`. Completing the approved
  scientific question therefore requires a fresh remote execution approval;
  this approval is consumed and must not be reused.
