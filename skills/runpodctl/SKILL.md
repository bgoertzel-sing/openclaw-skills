---
name: "runpodctl"
description: "Protocol-first RunPod lifecycle workflow: bounded waits, verified readiness, single ownership, cleanup, and failure classification."
allowed-tools: Bash(runpodctl:*)
compatibility: Linux, macOS
metadata:
  author: runpod (protocol layer: local)
  version: "2.0.0"
  license: Apache-2.0
---

# Runpodctl — protocol-first skill

Historical failures with this tool were almost never "RunPod is broken."
They were procedure failures: treating control-plane `RUNNING` as a usable
runtime, running a stale CLI, letting multiple writers manage one pod, and
letting stale monitors report dead pods. This skill hard-codes the fixes.
Follow the protocol literally. Do not improvise around it.

## Axioms (read these as invariants, not advice)

1. **`RUNNING` is a control-plane claim, not evidence of a runtime.**
   A pod is READY if and only if all three hold:
   (a) an SSH banner is received, (b) an authenticated remote command
   returns exit 0, (c) `nvidia-smi` (GPU pods) reports the expected GPU.
   Nothing else — not status fields, not uptime alone, not the console —
   counts as ready. Never start work, transfer files, or report progress
   based on `RUNNING` alone.

2. **Exactly one lifecycle owner per pod.** One agent/process is the
   single writer for create/stop/delete of a given remote-job record.
   Before creating any pod, write one remote-job record naming the owner.
   No other process may create "replacement" pods for that job.

3. **Every wait is bounded.** Never poll indefinitely. Use
   `--wait --wait-timeout 10m` at creation. On timeout: delete the exact
   returned pod ID, re-query the provider to confirm it is gone, record
   the failure, and STOP. Do not automatically create a replacement.

4. **Update and pin the CLI before any paid action.** Old builds silently
   lack required flags (`--wait` needs ≥ v2.9.0; `--model-reference` and
   multi-volume need ≥ v2.4.0). Update, record the version in the job
   record, and never switch binaries mid-task.

5. **Monitors are silent and transition-only.** A monitor may emit only:
   state transitions, hard-stop, success, or failure. Never "no material
   change." When a pod ID is superseded or deleted, kill every monitor
   for the old ID in the same step — a monitor bound to a dead pod is a
   bug, not background noise.

6. **Pin identities before provisioning.** Resolve image digests
   (`repo@sha256:...`, never a mutable tag) and source-bundle hashes
   BEFORE creating the scientific pod. If a sealed handoff requires a
   digest, a pod advertising a mutable tag must not run science —
   correct behavior is fail-closed, so don't provision until the
   identity question is settled.

7. **Terminated means verified empty.** A job is not finished until
   artifacts are retrieved and hash-checked, the pod is deleted, and a
   final `runpodctl pod list --all` shows the provider empty of this
   job's IDs. Record that final check.

8. **Classify before retrying.** Every failure gets exactly one label
   from the taxonomy below before any further paid action. Retrying an
   unclassified failure is forbidden.

## Failure taxonomy (assign one, then act)

| Label | Signature | Action |
|---|---|---|
| provider-readiness | `--wait` timed out; zero uptime / no SSH; or pod vanished from lists | Delete ID, confirm empty, record. If it recurs, run the canary (below), NOT another science pod. |
| code/launcher | SSH+GPU worked; project software failed | Fix code locally. Do not blame or re-test the provider. |
| agent-workflow | concurrent writers, stale monitor, unbounded wait, stale CLI, mutable tag at handoff | Stop. Fix the procedure and the job record before any new pod. |
| scientific-negative | runtime + retrieval succeeded, hypothesis gate failed | Success operationally. Record and clean up normally. |

The historical record contains all four classes. Do not collapse them:
"the account can't use RunPod" has been refuted by direct controls
(template and raw-image SSH canaries both reached authenticated SSH in
under a minute).

## The lifecycle state machine

Every paid pod job walks these states in order. Skipping a state is a
protocol violation.

```
PREFLIGHT → CANARY (if trust is stale) → PROVISION → VERIFY-READY
        → HANDOFF → RUN → RETRIEVE → TERMINATE → CONFIRM-EMPTY
```

### 1. PREFLIGHT (always, ~1 min, $0)

```bash
runpodctl update
runpodctl version            # record in the job record; must be ≥ 2.9.0
runpodctl user               # auth + balance sanity (needs RUNPOD_API_KEY)
runpodctl gpu list           # confirm the target GPU type exists/available
```

Create the remote-job record now: job name, single lifecycle owner,
CLI version, cost envelope (max $ and max wall-clock), target GPU,
image digest (or "canary/template"). Kill any monitors left over from
prior jobs.

### 2. CANARY (conditional, ~$0.05)

Run a canary if ANY of: last successful READY pod was > 48 h ago; the
previous attempt was a provider-readiness failure; the CLI was just
updated across a minor version; you are about to use a new image, GPU
type, or datacenter.

```bash
runpodctl pod create \
  --template-id runpod-torch-v21 \
  --gpu-id "NVIDIA GeForce RTX 4090" \
  --ports "22/tcp" \
  --container-disk-size 20 \
  --wait --wait-timeout 10m
# On success (pod ID returned ready):
runpodctl ssh info <pod-id>          # get connection command
ssh <user>@<host> "hostname && nvidia-smi -L"   # READY check (axiom 1)
runpodctl pod delete <pod-id>
runpodctl pod list --all             # confirm empty
```

Acceptance is the axiom-1 triple, never `RUNNING`. If the canary fails:
preserve the exact create response and the timeout ID, delete, confirm
empty, and STOP — report upward rather than retrying. A failed canary
on an official template is strong evidence of a provider/account issue
and is exactly the artifact a human needs to see.

### 3. PROVISION (the scientific pod)

Preconditions: canary trust is current; image is pinned by digest;
source bundle hash recorded; ports and env declared now (they cannot be
added to a running pod without a reset).

```bash
runpodctl pod create \
  --image <registry>/<repo>@sha256:<digest> \
  --gpu-id "<gpu>" \
  --ports "22/tcp" \
  --env KEY=VAL \
  --terminate-after <bound> \
  --wait --wait-timeout 10m
```

Always set `--terminate-after` (it DELETES; `--stop-after` only stops
and keeps billing disk). On `--wait` timeout: axiom 3 — delete, confirm,
stop, classify as provider-readiness. No replacement pod.

### 4. VERIFY-READY

Run the axiom-1 triple over SSH and record its output in the job record.
Only after it passes does the pod ID become the bound resource identity
for the sealed handoff.

### 5. HANDOFF and RUN

Bind the handoff to the verified pod ID + image digest. Transfer the
minimum non-sensitive file set (`runpodctl send` / `receive`, or scp
over the verified SSH channel — for `send`, capture the FIRST stdout
line as the one-time code while it streams; each send mints a fresh
code; both sides must exit 0). Launch the workload. Start exactly one
monitor, transition-only (axiom 5).

### 6. RETRIEVE → TERMINATE → CONFIRM-EMPTY

Retrieve artifacts, hash-verify them locally, THEN:

```bash
runpodctl pod delete <pod-id>
runpodctl pod list --all      # must not contain this job's IDs; record it
```

A job record without the final empty-list check is incomplete.

## Decision rules (unchanged operational guidance)

- Hub for known deployable apps/workers (vLLM, ComfyUI, Whisper).
  Prefer first-party (`--owner runpod-workers`), recently released
  (`--order-by releasedAt`), broadly available GPU pools. Don't pin a
  scarce large-GPU tier a small model doesn't need.
- "Active worker" means `--workers-min 1` (always warm), not
  `--workers-max 1`. ⚠ min-1 bills continuously — set back to
  `--workers-min 0` or delete the endpoint when done.
- `serverless update` has no `--gpu-id`; change an endpoint's GPU pool
  via `PATCH https://rest.runpod.io/v1/endpoints/<id>` with
  `{"gpuTypeIds":[...]}`.
- CPU serverless: ONLY `runpodctl serverless create --compute-type CPU`
  (or MCP). Never the public v1 REST with `"computeType":"CPU"` — it
  silently provisions GPU (verified 2026-07-14).
- Templates when a template ID exists or reusable defaults are wanted;
  `--image` for one-off specific images; serverless for
  request/response APIs; pods for interactive/training/long-lived work.
- CPU pods for preprocessing/file movement (`--compute-type cpu`,
  lowercase; no GPU flags).
- Services on a pod (Ollama, ComfyUI, dev server): declare `--ports`
  and `--env` at creation, SSH-exec the install, bind 0.0.0.0, poll the
  proxy URL.
- SSH: `runpodctl ssh info <pod-id>` returns the connection command +
  key, NOT a session. Run `ssh user@host "command"` yourself.
- Network volumes are datacenter-pinned; check `runpodctl datacenter
  list` before attaching. No storage-tier flag on create — the default
  tier is provisioned; High-Performance requires the console or
  `POST https://v2-rest.runpod.io/v2/network-volumes` with
  `"type":"HIGH_PERFORMANCE"`. Tier is immutable.
- To delete a network volume, remove the pod using it first.
- **Cloud type ≠ reliability.** `SECURE` vs `COMMUNITY` is a cloud-type
  field, not an on-demand persistence guarantee. Never report "Secure,
  therefore reliable/on-demand" — persistence claims require evidence.
- Clean up every paid resource created for validation.

### Serverless facts

- `--workers-min 0` (default) = scale-to-zero, per-request billing.
- Broken-image tell: workers `ready` but jobs stuck `IN_QUEUE` with
  `inProgress: 0` → switch workers, don't wait it out. Diagnose via
  `/health` worker counts (no first-class worker-log command).
- Model cache: `--model-reference https://huggingface.co/<org>/<model>:main`
  host-caches into `/runpod-volume/huggingface-cache/hub/`; GPU only,
  ≥ v2.4.0; works with `--template-id`/`--hub-id`.
- Multi-region HA: `--network-volume-ids <v1>,<v2>
  --data-center-ids <dc1>,<dc2>` (≥ v2.4.0); volumes do NOT auto-sync.

## Command quick reference

Live `runpodctl <resource> <action> --help` is authoritative. Inspect
help before any unfamiliar command.

```bash
# Pods
runpodctl pod list [--all|--status|--since|--created-after]
runpodctl pod get <pod-id>
runpodctl pod create --template-id <id> --gpu-id "<gpu>" --wait --wait-timeout 10m
runpodctl pod create --image <img@sha256:...> --gpu-id "<gpu>" --wait --wait-timeout 10m
runpodctl pod create --compute-type cpu --image ubuntu:22.04
runpodctl pod {start|stop|restart|reset|update|delete} <pod-id>

# Hub / Templates / Serverless
runpodctl hub search <q> | hub get <id|owner/name>
runpodctl template search <q> | template get <id> | template create --name "x" --image "img" [--serverless]
runpodctl serverless list | get <id> | delete <id>
runpodctl serverless create --name "x" {--template-id <id> | --hub-id <id>} [--gpu-id "<gpu>"] [--env K=V]
runpodctl serverless update <id> --workers-max 5

# Volumes / Models
runpodctl network-volume {list|get|create|update|delete} ...
runpodctl model {list|add|remove} ...

# Info / SSH / Transfer / Utilities
runpodctl user            # account + balance (alias: me)
runpodctl gpu list | datacenter list
runpodctl ssh info <pod-id>
runpodctl send <path>     # capture first stdout line = one-time code
runpodctl receive <code>
runpodctl doctor | update | version | completion
```

## URLs

```
https://<pod-id>-<port>.proxy.runpod.net        # pod ports
https://api.runpod.ai/v2/<endpoint-id>/run      # async
https://api.runpod.ai/v2/<endpoint-id>/runsync  # sync
https://api.runpod.ai/v2/<endpoint-id>/health   # health
https://api.runpod.ai/v2/<endpoint-id>/status/<job-id>
```

(The runtime `api.runpod.ai/v2` API is fine; the v1-vs-v2 caveat is
only about the control/management REST at `rest.runpod.io`.)

## Source & docs

- CLI source: https://github.com/runpod/runpodctl
- Releases: https://github.com/runpod/runpodctl/releases
- Docs: https://docs.runpod.io/runpodctl/overview
