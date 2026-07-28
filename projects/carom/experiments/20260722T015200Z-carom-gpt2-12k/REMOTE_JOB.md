# Remote job proposal — CAROM GPT-2 12k

## Approval status

**COMPLETE — TERMINATED.** Approved by Ben with a USD 10 maximum. Final pod
`wsllxvsshf7jf1` completed training and evaluation; artifacts were retrieved
and hash-verified before termination on 2026-07-22.

## Provider and resource

- Provider/account: RunPod, currently authenticated operator account
- Cloud: Secure Cloud
- GPU: one NVIDIA A100 SXM4 80GB
- Image/template: `runpod-torch-v280` /
  `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`
- Container disk: 50GB; persistent/network volume: none
- Network: SSH only plus template defaults
- Current observed price: USD 1.49/hr

## Time and cost

- Measured predecessor: 4,000 training steps in 1,897 seconds
- Expected duration: about 2 hours including startup and interventions
- Expected compute: about USD 2.98
- Hard guardrail: 3 hours / USD 4.47
- Configure provider auto-terminate for the three-hour deadline

## Data and privacy

Upload only the two pinned CAROM Python sources and command file. The dataset is
generated synthetically on the pod. No credentials, unrelated workspace state,
private corpora, or Git metadata are transferred. Treat source/results as
local-private because licensing of the supplied prototype is unstated.

## Artifact and cleanup plan

Retrieve checkpoints, per-checkpoint JSON, summary, logs, source/config, and
environment/version record to this experiment directory. Validate counts and
JSON fields, generate SHA-256 manifest, then terminate (not merely stop) the
pod and verify provider inventory. No persistent volume is requested.
