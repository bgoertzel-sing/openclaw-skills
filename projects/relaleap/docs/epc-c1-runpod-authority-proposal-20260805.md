# C1 Runpod Authority Proposal

Status: `BLOCKED_AUTHORITY` pending Ben's explicit approval

Date: 2026-08-05 UTC

## Requested resource

- Provider/account: Runpod Secure Cloud using the existing Runpod credential
  store on Ben's dedicated workstation. No account identifier or secret will
  be printed; account identity and available balance will be attested in the
  job record before provisioning.
- Hardware/count: one NVIDIA A40 48 GB GPU; no multi-GPU resource.
- Region: Secure Cloud US-West preference. If no A40 is available in a
  US-West Secure Cloud facility, stop and request a revised approval; do not
  substitute Community Cloud, another GPU, or another region silently.
- Image: `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04`; resolve and
  record its immutable image digest before execution. If unavailable or
  digest resolution fails, stop without substituting an image.
- Storage: 50 GB container disk, no persistent/network volume and no snapshot.
- Network: outbound HTTPS only for pinned Python packages, Hugging Face model,
  and public EMNIST/WikiText data; inbound SSH only. No public application or
  inference endpoint.

## Work and limits

- Scope: official five-seed MNIST ePC reference reproduction, then the frozen
  GPT-2-small FabricPC C1 homotopy through its first terminal rung. No C2/C3,
  hyperparameter search, semantic oracle, or unrelated job is authorized.
- Expected usage: 12 GPU-hours.
- Hard termination: 24 elapsed hours or 24 GPU-hours, whichever occurs first.
- Price source: Runpod's official pricing page fetched 2026-08-05 lists Secure
  Cloud A40 at `$0.44/GPU-hour` and container disk at `$0.10/GB/month`.
- Expected compute cost: `$5.28`; 24-hour compute maximum `$10.56`; one-day
  50 GB disk estimate `$0.17`. Requested all-in hard cap: `$12.00`.
- Any price above `$0.44/GPU-hour`, projected all-in cost above `$12.00`, or
  billable resource not listed here requires a new approval.

## Code and data plan

- Source: clean local `agent/epc-remediation-a0` C1 specification commit
  `f8cfed4`, plus the pinned official reference
  commit `95c555197699f6b4d15452451da15049946b49ca`.
- Upload only a reviewed source bundle, lockfile/wheel manifest, frozen configs,
  and data-download manifests. Do not upload `.git` credentials, SSH private
  keys, OpenClaw state, unrelated project files, sealed semantic gates, or
  local caches.
- Inputs are public code, public pretrained GPT-2, and public EMNIST/WikiText
  datasets. Privacy classification: public/non-sensitive.
- Credentials remain in local/provider credential stores. No key enters a
  command, Markdown, image, log, artifact, or repository.

## Stops and cleanup

Stop scientific execution immediately on any of: official reference gate
failure; rung-0 identity failure; MG-7 failure; repeated OOM after the frozen
batch configuration; nonfinite data; source/data hash mismatch; MG-3/MG-4
failure; matched-quality stop; 20 elapsed hours (reserve four hours for return
and cleanup); or projected cost above `$10.50`.

After a scientific stop, retrieve and verify artifacts, then **terminate** the
pod rather than leaving it stopped. Container disk is disposable. Query
Runpod state and observed spend after termination and record zero remaining
pods/volumes/endpoints. Do not leave a resource running while interpreting.

## Artifact return

Return logs, manifests, checkpoints, JSON/CSV/SVG, certificates, environment,
and hashes to
`projects/relaleap/experiments/<C1-run-id>/artifacts/remote/`. Verify the
declared manifest SHA-256 locally, rerun strict schema/hash checks, preserve raw
failure artifacts, and record final provider cost/resource cleanup in
`REMOTE_JOB.md`.
