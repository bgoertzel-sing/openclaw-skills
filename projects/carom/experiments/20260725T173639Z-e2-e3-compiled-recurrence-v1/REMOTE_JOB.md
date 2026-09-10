# Proposed remote job: CAROM E2/E3 compiled recurrence

- Approval: Ben, 2026-07-25, approved H100/USD 9 bound.
- Provider/account: RunPod Secure Cloud, authenticated operator account.
- Resource: one H100 SXM 80GB, US when available, official PyTorch 2.8
  template, 20GB container disk, no persistent/network volume.
- Current price reference: USD 2.99/hour observed for the immediately prior
  H100 E2/E3 allocation on 2026-07-25; exact allocated price will be recorded.
- Expected duration/cost: 1.5--2.5 hours, USD 4.49--7.48.
- Hard guardrail: terminate at 3 hours or USD 9.00, whichever comes first.
- Network/data: SSH only; upload the five required CAROM Python source/test
  files and wrapper. Inputs are synthetic; no private corpus or credentials.
- Stage 1: CUDA eager-versus-compiled full-shape equivalence and throughput
  probe, including compilation overhead and steady-state timing.
- Proceed condition: all frozen float32 equivalence tolerances pass and the
  measured 25-arm campaign projection is at most 2.5 hours.
- Stage 2: unchanged five-seed, five-arm, 3,000-update E2/E3 campaign with the
  compiled transition used only during training and eager deterministic
  evaluation.
- Stop conditions: compiler/equivalence failure, non-finite output,
  deterministic-repeat mismatch, projected duration above 2.5 hours, process
  failure, 3-hour deadline, or USD 9 cap.
- Artifact return: benchmark JSON, per-arm JSON, summary, corpus, logs,
  environment record, exit status, and SHA-256 manifest to this experiment's
  `artifacts/remote/` directory.
- Cleanup: retrieve and verify artifacts, then terminate (not merely stop) the
  pod and confirm provider inventory is empty.

## Execution disposition

- Pod: `ls7hhlemazsdyc`, H100 SXM 80GB Secure Cloud, USD 2.99/hour.
- CUDA Stage 1 passed: logits `1.79e-7`, activity `4.29e-6`, gradients
  `5.59e-9`, and post-AdamW parameters `1.77e-6`; all within frozen
  tolerances. Steady-state training-step speedup was 3.50x (`197.8 ms` to
  `56.5 ms`).
- The Stage-1 25-arm estimate (1.26 hours / USD 3.77) was not borne out by
  the full runner. After 2h28, 16/25 arms had completed and extrapolation
  exceeded the approved 3-hour/USD 9 ceiling. The process was interrupted
  under the stop condition; this is an incomplete campaign, not a scientific
  E2/E3 disposition.
- Retrieved partial archive:
  `artifacts/remote/carom-e2e3-partial-results.tar.gz`, SHA-256
  `34c824625202035a046bd2ce6a752bc67f6bbe22fd952857b284c842b8da2832`.
  Local and remote SHA-256 values matched. It contains all five arms for
  seeds 7, 17, and 27, plus `e2_full` for seed 37.
- Cleanup: pod deleted; `runpodctl pod list` returned an empty inventory.
