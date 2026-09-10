# RunPod proposal: CAROM GPT-2 piecewise schedule

- Status: `terminated after protocol-invalid LR trace`
- Approval: Ben approved 1× H100 SXM under a 4.0-hour/USD 12.00 hard cap
  on 2026-07-25 (task instruction received 2026-07-26 UTC).
- Provider/account: RunPod Secure Cloud; `bengoertzel@gmail.com`
- Resource: 1× H100 SXM 80GB, RunPod template `runpod-torch-v280`
  (`runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`), 50 GB container disk,
  no network volume, SSH only. Region is provider-selected.
- Price source: recent CAROM H100 allocation, USD 2.99/hour. The
  2026-07-26 preflight confirmed H100 SXM stock in multiple Secure Cloud
  regions; the exact current allocation price and assigned region will be
  recorded immediately after provisioning and the pod will be deleted if the
  rate would exceed the approved USD 12.00/4-hour cap.
- Work: 2 × 12,000 training updates (piecewise + OneCycleLR control) plus
  checkpoint evaluation every 1,000 updates. The archived single-arm 12k run
  took 2h56 on an A100. H100 is ~1.5-2× faster. Two arms ≈ 2 × 1.5h = 3.0h
  estimated.
- Expected cost: USD 6.00–9.00. Hard bounds: 4.0 wall hours and USD 12.00.
  This is within Ben's overall USD 20 CAROM-sequence ceiling (USD 4.72 used
  for the schedule diagnostic; USD 15.28 remaining).
- Transfer/privacy: upload only the repository runner/harness, frozen corpora,
  and command; synthetic data only. Do not upload Git credentials, OpenClaw
  state, unrelated files, or provider credentials.
- Artifact return: retrieve to
  `projects/carom/experiments/20260726T100000Z-gpt2-piecewise-schedule/artifacts/`;
  retrieve checkpoints, JSON metrics, logs, frozen corpus, environment record,
  and remote SHA-256 manifest. Verify all hashes locally before termination.
- Immediate stops: non-finite loss/metrics, OOM, missing checkpoint, repeated
  process failure, 4.0 elapsed hours, or projected/final USD 12.00.
- Cleanup: retrieve and hash-verify first, then terminate the pod and re-query
  inventory. Pre-existing EXITED pods are out of scope.

## Allocation

- Created: `2026-07-26T02:35:49Z`
- Pod ID: `xyaed6b5s9q99g`
- Name: `carom-piecewise-20260726`
- GPU: 1× H100 SXM 80 GB
- Region: Canada (`CA-MTL-1` requested; provider returned country `CA`)
- Live rate: USD 2.99/hour (maximum four-hour compute charge USD 11.96)
- Image: `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`
- Storage/network: 50 GB container disk, 0 GB persistent volume, SSH port only
- Provider termination deadline: `2026-07-26T06:35:09Z`

## Cleanup

- Stop reason: observed realized LR was orders of magnitude below the frozen
  schedule because absolute rates were used as `LambdaLR` multipliers; the
  checkpoint cadence was also 500 rather than 1000 updates.
- Partial evidence retrieved: frozen corpus; piecewise checkpoints 0, 500,
  and 1000; stdout/stderr; environment and source records; exact uploaded
  source; remote SHA-256 manifest.
- Verification: 13/13 manifest entries passed locally.
- Deleted: approximately `2026-07-26T02:48:00Z`.
- Final inventory: `[]` (no pods remain).
- Observed wall time: approximately 12.8 minutes.
- Estimated compute charge: approximately USD 0.64 at USD 2.99/hour. The
  provider billing-history query returned no row immediately after deletion,
  so this is an estimate rather than a settled charge.
