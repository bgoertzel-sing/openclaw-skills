# RUN: CAROM E0/E1 exposure-controlled screen r1

- Experiment ID: `20260720T140710Z-e0-e1-exposure-controlled-r1`
- Status: completed with a failed deterministic-evaluation validity gate
- Question: does the fixed/free accuracy gap survive paired evaluation and
  activity-normalized control, and which component is implicated by trajectory
  replay?
- Specification: `docs/e0-e1-exposure-controlled-spec.md`

## Frozen matrix

- Arms: `fixed_raw`, `free_raw`, `fixed_norm`, `free_norm`
- Seeds: 7, 17, 27, 37, 47
- 3,000 updates per arm; batch 128; d=64; K=16
- 2,048 shared deterministic evaluation examples, balanced over depths 2--5
- Post-training fixed/free trajectory swaps within raw and normalized pairs
- Outputs: per-example accuracy and trajectory/exposure/update diagnostics,
  final checkpoints, summary contrasts, seed-level bootstrap intervals

## Local validation

- `python3 -m unittest -v test_e0_e1.py`: 3 passed
- Two-update end-to-end smoke: all four arms completed and summary generated
- `python3 -m py_compile model.py run_carom_e0_e1.py test_e0_e1.py`: passed

## Proposed remote job

- Provider/account: RunPod, authenticated account `bengoertzel@gmail.com`
- Resource: 1x A100 SXM 80GB Secure Cloud, US when available
- Current observed price: USD 1.49/hour (active account listing/pod rate)
- Image: `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`
- Storage: 20GB ephemeral container disk and 20GB temporary pod volume
- Network: SSH only; public task/code, no private data
- Expected runtime: 6.0--6.5 hours based on r1's ~1,403 seconds per 4,000-step
  itinerant arm, scaled to 20 x 3,000-step arms plus evaluation/replay
- Expected compute cost: USD 8.94--9.69
- Proposed hard bound: 7 hours and USD 10.43
- Upload: only CAROM Python source/spec and launch script
- Return: JSON/JSONL results, paired corpus, logs, environment record, and
  checkpoints to this run's `artifacts/`; verify parses and SHA-256 hashes
- Cleanup: terminate immediately after verified retrieval; no retained volume
- Stop conditions: non-finite values, failed deterministic gate, repeated
  process failure, 7-hour deadline, or cost bound

## Launch history

- Ben approved a cumulative USD 20 maximum on 2026-07-20 at 07:27 PDT.
- Initial pod `m4qz1w5725y8n4` later disappeared from the provider with no
  retrieved artifacts. Its maximum observed lifetime was about 4.3 hours,
  corresponding to an upper-bound compute exposure of about USD 6.45.
- Retry pod `0vlhvxtuhxu3fh` launched 2026-07-20 11:54 PDT: 1x A100 SXM 80GB
  Secure Cloud US at USD 1.49/hour. Automatic termination is set for
  2026-07-21 02:00 UTC.
- Remote preflight: all three E0/E1 tests passed. The run entered `fixed_raw`,
  seed 7, with live GPU utilization.

## Interpretation constraints

This run can identify exposure normalization and trajectory timing as causes
of the observed gap. It cannot establish a stable heteroclinic channel; SHC
claims remain gated on later perturbation/stability tests.

## Final audit (2026-07-24)

All 20 trainings and all 40,960 raw rows completed and are finite. Raw
fixed-minus-free slot accuracy is `+0.06956`, seed-bootstrap 95% CI
`[+0.00438,+0.13610]`. Normalization did not close the gap:
fixed-minus-free became `+0.23506`, while free normalized-minus-raw was
`-0.29193`.

Free raw had activity mass `40.76` versus fixed raw `22.11`, and workspace
update norm `194.13` versus `94.37`. Free normalized collapsed to activity
mass `3.70`, update norm `44.05`, and terminal trapping `0.9961`.
Normalization therefore changed regime rather than matching exposure.

The deterministic gate failed: only 5/20 arm/seeds repeated at aggregate
precision. Code audit found an unconditional random initial-activity
perturbation before the evaluation-mode check. Treat endpoint and mechanism
patterns as exploratory, not exact paired causal estimates. E2/E3 fixes and
regression-tests this defect.

Audit SHA-256:
`9841ef7619fcecbe6a335be5cef6d434ad6901be2a43dace29f5e9f3ed886d17`.
Disposition: close with caveat, proceed to deterministic E2 fixtures, and do
not spend the obsolete E0/E1 rerun authorization.
