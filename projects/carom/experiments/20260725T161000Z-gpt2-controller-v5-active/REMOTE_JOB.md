# Remote job: CAROM GPT-2 controller v5

- Approval: Ben, 2026-07-25, "Let's try again".
- Provider/account: RunPod Secure Cloud, authenticated operator account.
- Planned resource: one A100 SXM 80GB, official PyTorch 2.8 template.
- Current reference price: USD 1.49/hour from the completed v4 allocation.
- Expected duration/cost: 35--60 minutes, USD 0.87--1.49.
- Hard bound: 2 hours and USD 3.00.
- Data: CAROM source plus synthetic generated batches; no private corpus or
  credentials.
- Transfer: only required Python files over SSH.
- Stop conditions: completion, invariant failure, nonfinite output, process
  failure, two-hour deadline, or USD 3 cap.
- Cleanup: retrieve JSON/log/environment, verify SHA-256, then terminate and
  confirm provider inventory.
- Pod ID: `7xg450h78qkmj9`.
- Provisioned: 2026-07-25T16:23:07Z, A100 SXM Secure Cloud US,
  USD 1.49/hour.
- Provider auto-termination: 2026-07-25T18:30:00Z.
- Completed: 2026-07-25, exit status 0 after 2,406.73 seconds.
- Estimated successful-run cost: USD 0.996, plus negligible failed setup time.
- Retrieval: JSON, experiment log, environment record, and SHA-256 manifest
  copied to `artifacts/`; local hash verification passed.
- Cleanup: pod deleted after verified retrieval; `runpodctl pod list` returned
  an empty inventory.
