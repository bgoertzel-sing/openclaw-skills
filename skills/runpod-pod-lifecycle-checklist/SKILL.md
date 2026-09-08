---
name: "runpod-pod-lifecycle-checklist"
description: "Add observable bootstrap, truthful-exit, and no-debug-retry-beyond-approval gates."
---

# Skill: RunPod Pod Lifecycle Checklist

## When to use
Before provisioning, monitoring, retrieving from, or terminating approved RunPod research compute. Use with `remote-compute-guardrails`; it does not grant approval or authority to create paid resources.

## Preconditions
- Record explicit approval, budget cap, GPU type, maximum pod count and duration, stop conditions, and experiment directory in `REMOTE_JOB.md`.
- Pin the exact source revision and manifest before transfer. If a correctness fix lands after launch, record it as non-retroactive; do not treat the running pod as using the new pin.
- State whether the workload needs a persistent volume. Container disk is disposable across restarts and must not be the sole copy of irreplaceable checkpoints or raw results.
- Before provisioning, run the CPU/local self-test of the actual wrapper: required dependencies/imports, stage-result schema, and exit-status propagation. A wrapper must not report success if a required stage result/checkpoint is absent.

## Launch and readiness
- Prefer a known-good template with its documented start command, ports, and environment; verify the pod appears in the provider list.
- Record pod id, launch time, disk/volume configuration, image/template, source pin, and approved count/cost envelope in `RUN.md`.
- Establish readiness with SSH plus `nvidia-smi` and a bounded process/log check. Never infer readiness from `uptimeSeconds`.
- Emit an independently observable bootstrap heartbeat/log before expensive work: pod id, source/manifest hash, dependency/import check, exact command, and stage-0 result path. Retain it locally or retrieve it before any debugging relaunch.
- Treat repeated SSH unreachability or missing bootstrap evidence as a bounded failure path. Do not create additional debug pods beyond the approved pod-count/time/cost envelope; terminate and record that no experiment result exists unless stage artifacts are retrieved and verified.

## Artifact resilience
- Start periodic, local artifact sync before expensive work begins when no persistent volume is attached. Sync into a per-experiment immutable timestamped location and stop after a bounded number of failures.
- Checkpoint each experimental stage so an interruption makes the completed boundary explicit.
- Before any termination, retrieve logs, checkpoints, manifests, and outputs; verify local SHA-256 hashes against remote values and expected stage artifacts.
- A pod restart or workspace wipe invalidates un-synced state only; do not silently resume from reconstructed dependencies without recording the restart and exact recovery actions.

## Monitoring and budget
- Monitor process/log/GPU evidence and cost against the approved cap. A watchdog may alert and, only if its explicit authorization says so, terminate on cap, failure, or completion.
- Remove a scoped watchdog after all scoped pods are terminated; verify provider absence.
- If debugging reveals a new failure mode, stop when the authorized envelope is reached and request fresh explicit approval for a successor plan; do not treat a prior single-pod approval as permission for retries.

## Closure
- Update `REMOTE_JOB.md` and `RUN.md` with termination time, actual cost, retrieval status, hashes, restart/unreachability events, and whether a result was established.
- Update the authoritative project `TASKS.md`; refresh the Kanban only as a compact index.
- Never claim a pass from setup, provision, or an empty aggregate. Validate non-empty required aggregates, stage outputs, and truthful exit status first.

## Evidence
- 2026-07-29: three Secure A40 SSH-free transport probes failed to return an artifact; debugging exceeded the original one-pod/30-minute/USD-0.22 envelope. All pods were removed. A successor requires observable remote logs and fresh approval.
- 2026-07-29: HDC × MusicGen full-corpus r2 exited with `PIPELINE_EXIT:0` after an AudioCraft/spaCy import failure, but correctly failed closed because stage output/checkpoint/JSON gate evidence was absent.
- 2026-07-28: one RelaLeap RTX 4090 pod restarted and wiped its non-volume workspace; periodic local sync and a documented rebuild allowed completion with verified artifacts.
- 2026-07-28: an HDC × MusicGen RTX 4090 pod never became SSH-ready; it was terminated under the approved cost-stop rule and produced no result.
- 2026-07-21: template/start-command, approval-state, and uptime signal failures motivated the original proposal.
