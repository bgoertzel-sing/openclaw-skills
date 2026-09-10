# RunPod proposal: CAROM GPT-2 schedule diagnostic

- Status: `approved by Ben; pod provisioned 2026-07-26T00:21:15Z`
- Provider/account: RunPod Secure Cloud; authenticated account reported by
  `runpodctl doctor` as `bengoertzel@gmail.com`.
- Resource: 1× H100 SXM, RunPod template `runpod-torch-v280`
  (`runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`), 50 GB container disk,
  no network volume, SSH only. Region is provider-selected/unknown until an
  offer is chosen and must be recorded before launch.
- Price source: recent CAROM H100 allocation/provider record, USD 2.99/hour;
  recheck current offer immediately before provisioning.
- Work: 9,000 total training updates plus checkpoint evaluation. The archived
  12,000-update A100 run took 2h56; H100 runtime is estimated 1.0--1.8 hours.
- Expected cost: USD 2.99--5.38. Hard bounds: 2.0 wall hours and USD 6.00.
  This is within Ben's overall USD 20 CAROM-sequence ceiling but requires
  explicit approval of this concrete proposal.
- Transfer/privacy: upload only the repository runner/harness, frozen GPT-2
  step-3000 checkpoint, and command; synthetic data only. Do not upload Git
  credentials, OpenClaw state, unrelated files, or provider credentials.
- Artifact return: retrieve to
  `projects/carom/experiments/20260726T000748Z-gpt2-schedule-diagnostic/artifacts/`;
  retrieve checkpoints, JSON metrics, logs, frozen corpus, environment record,
  and remote SHA-256 manifest. Verify all hashes locally before termination.
- Immediate stops: non-finite loss/metrics, OOM, missing checkpoint, repeated
  process failure, two consecutive post-start L2--4 evaluations below 0.30,
  2.0 elapsed hours, or projected/final USD 6.00.
- Cleanup: retrieve and hash-verify first, then terminate the new pod and
  re-query inventory. Stop is insufficient because container disk may remain
  billable; termination deletes the pod/container disk. Pre-existing EXITED
  pods and their volumes are explicitly out of scope and will not be deleted.
- Existing inventory: three EXITED resources were audited read-only on
  2026-07-26. One retains a 100 GB network volume. Raw provider metadata is
  not copied here because an old resource contains a secret-valued environment
  field.

## Provisioned resource

- Pod ID: `425j76ha3y9a4i`
- Region/location: `IN`
- Observed price: USD 2.99/hour
- GPU: H100 SXM 80 GB; 28 vCPU; 251 GB RAM
- Disk: 50 GB container disk; zero network volume
- Provider auto-termination: `2026-07-26T02:20:00Z`

## Final disposition

- Training completed: approximately `2026-07-26T01:54Z`
- Artifact verification and deletion completed before the auto-termination
  deadline.
- Estimated pod lifetime: about 1.58 hours; estimated compute cost:
  approximately USD 4.72 at USD 2.99/hour, below the USD 6 cap.
- Retrieved evidence hashes matched; pod deletion confirmed; no task pod
  remains in inventory.
