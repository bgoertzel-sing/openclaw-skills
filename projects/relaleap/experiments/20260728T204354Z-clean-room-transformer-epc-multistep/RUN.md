# Run 20260728T204354Z: clean-room transformer ePC multi-step comparison

- Status: completed and verified
- Question: on fixed public WikiText token batches, how do the clean-room T=1
  KD endpoint and four-settle-step ePC-KD differ across three seeds, under
  exact state and replay controls?
- Protocol/source: `configs/clean_room_epc_multistep_v1.json`; commit
  `6f8cc21f71e09eeb04a60a935c3a4be33abdd839`.
- Acceptance: all three per-seed JSON records have `status=passed`, exact ePC
  replay, finite objective/KD values, and a generated summary. Results are
  descriptive held-out KD evidence only.
- Remote resource and stop/return plan: `REMOTE_JOB.md`.

## Result

All three seeds passed with exact replay and finite metrics. The verified mean
held-out KD gain is 6.588154157002767 nats; this is descriptive evidence only.
