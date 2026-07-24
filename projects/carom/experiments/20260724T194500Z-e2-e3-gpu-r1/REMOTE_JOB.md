# Remote job: CAROM E2/E3 GPU r1

- Approval source: Ben, relayed 2026-07-24.
- Provider/account: RunPod Secure Cloud, authenticated operator account.
- Resource: 1 x NVIDIA A100 SXM 80GB.
- Image: `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`.
- Storage: 20 GB container disk plus 20 GB temporary pod volume at
  `/workspace`.
- Network: SSH only for source upload, monitoring, and artifact retrieval.
- Data classification: supplied/private CAROM source and synthetic generated
  data only; no credentials or unrelated workspace files uploaded.
- Current observed price: USD 1.39/hour; provisioning ceiling USD 1.49/hour.
- Expected duration: 8--8.5 hours.
- Hard bounds: 9 wall-clock hours and USD 25.00, whichever comes first.
- Stop conditions: completed run; non-finite output; failed deterministic
  gate; process failure; 9-hour wall clock; or USD 25.00 cap.
- Cleanup: retrieve all run artifacts, verify SHA-256 manifest locally, then
  terminate the pod and its attached temporary volume immediately. Stopping is
  insufficient because retained storage may remain billable.
- Local artifact destination:
  `experiments/20260724T194500Z-e2-e3-gpu-r1/artifacts/`.
- Pod/resource IDs: pending provisioning.

