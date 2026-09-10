# Remote job: CAROM E2/E3 GPU r1

- Approval source: Ben, 2026-07-25 (USD 10 maximum for CAROM open tasks).
- Provider/account: RunPod Secure Cloud, authenticated operator account.
- Resource: 1 x NVIDIA GeForce RTX 4090 (24 GB), Secure Cloud, US.
- Image: `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`.
- Storage: 30 GB container disk plus 20 GB temporary pod volume at
  `/workspace`.
- Network: SSH only for source upload, monitoring, and artifact retrieval.
- Data classification: supplied/private CAROM source and synthetic generated
  data only; no credentials or unrelated workspace files uploaded.
- Current observed/provisioned price: USD 0.69/hour (RunPod create response).
- Expected duration: up to 7 hours.
- Hard bounds: H100 provider auto-termination at `2026-07-25T19:45Z`,
  approximately 3.21 hours / USD 9.61. Including the approximately 21-minute
  aborted A40 attempt and brief failed allocations keeps the campaign below
  Ben's USD 10 ceiling.
- Stop conditions: completed run; non-finite output; failed deterministic
  gate; process failure; 9-hour wall clock; or USD 25.00 cap.
- Cleanup: retrieve all run artifacts, verify SHA-256 manifest locally, then
  terminate the pod and its attached temporary volume immediately. Stopping is
  insufficient because retained storage may remain billable.
- Local artifact destination:
  `experiments/20260724T194500Z-e2-e3-gpu-r1/artifacts/`.
- Failed allocation: pod `smaz1kqnrvqmyv` never reached boot or SSH
  readiness (`uptimeSeconds=0`) and was deleted at 2026-07-25T16:07Z.
- Failed allocation: pod `lyzn7relkrt7ut` also never reached boot or SSH
  readiness and was deleted at 2026-07-25T16:11Z.
- A40 pod `wf62ynwhmoabba` was SSH-ready and ran the first arm for over 17.5
  minutes without completing it, projecting beyond its provider deadline. Its
  partial logs were retrieved and the pod was deleted; no scientific result
  was produced.
- A first H100 allocation `qafsf1ldmocee1` was immediately deleted because its
  initial auto-termination bound marginally exceeded the campaign budget.
- Active pod ID: `ga1pjxquw02ygg`.
- Reprovisioned: `2026-07-25T16:32:19Z`, H100 SXM Secure Cloud (Germany), at
  USD 2.99/hour.
- Auto-termination deadline: `2026-07-25T19:45:00Z`.
- H100 attempt terminated manually at approximately 2026-07-25T16:44Z after
  measured runtime proved the full campaign could not fit the approved bound.
  Partial logs were retrieved first; provider inventory retained only the
  separately approved GPT-2 v5 pod.
