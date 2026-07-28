# Remote Job: smoke-r2 (awaiting RTX 3090 availability)

- Project/run: `hdc-musicgen` / `20260727T140304Z-smoke-r2`
- Status: `provisioned; setup in progress`
- Approval: Ben, Telegram message 13726, 2026-07-27; this confirms the
  proposed replacement amendment and run.

## Authorized scope

### 2026-07-28 extension authorization

Ben explicitly confirmed launch after the original setup overran its four-hour
envelope.  The existing pod may now incur **up to USD 5.00 additional spend**
to run only the already-approved eight-track Stages 0/S/A.  Hard stop: retrieve
and locally hash-verify `codes_meta.json`, the selected-input manifest, logs,
and result JSON; then terminate the pod immediately.  No retry, full run,
Stage C, or Stage D is authorized by this extension.

### 2026-07-28 launch failure

Immediately after the owner-confirmed launch extension, `runpodctl` still
reported pod `vbu5r47gstyl16` as RUNNING at USD 0.50/hour, but its advertised
SSH endpoint `213.192.2.68:40137` refused connections twice (including a
15-second retry).  No Stage 0/S/A command was started, no GPU work occurred,
and no new data were transferred.  Per the prior owner instruction to kill an
unreachable MusicGen pod rather than pay for an unusable resource, terminate
this pod; do not provision a replacement without a fresh availability/cost
check.

### 2026-07-28 cleanup evidence

`runpodctl pod delete vbu5r47gstyl16` returned `deleted: true`.  A subsequent
`runpodctl pod list` returned `[]`, and provider lookup returned 404 / pod not
found.  No stage artifacts exist because no stage command ever began.

### 2026-07-28 replacement authorization

Ben explicitly requested a fresh MusicGen pod after the unreachable-pod
cleanup.  Replacement scope is unchanged: one Secure RTX 3090, official
`runpod/pytorch:2.2.0-py3.10-cuda12.1.1-devel-ubuntu22.04`, 40 GB container
disk, 30 GB temporary `/workspace`, SSH only, selected explicit-CC inputs only,
and Stage 0/S/A only. The remaining spend envelope is USD 5.00; use a
four-hour auto-termination (`2026-07-28T08:32:20Z`) and terminate immediately
after verified retrieval. `runpodctl doctor` was healthy and GPU availability
reported Secure RTX 3090 stock Low immediately before provisioning.

Provisioned replacement `2jh6oxjzogdexe` at 2026-07-28T04:32Z: Secure RTX
3090 in CZ, USD 0.50/hour, 40 GB container disk, 30 GB temporary workspace,
official pinned image, auto-termination 2026-07-28T08:32:20Z. No data transfer
or stage command had started at creation.

At 2026-07-28T04:34Z and again after a short readiness window, RunPod reported
the replacement RUNNING but `runpodctl ssh info` returned `pod not ready`; no
IP/port was supplied. No transfer, install, or stage command has started.
Treat this as provisioning only, not experiment progress; re-check readiness
before any further spend-causing setup action.

### 2026-07-28 web-terminal recovery observation

Ben accessed the provider web terminal and verified `NVIDIA GeForce RTX 3090`
was visible. He created the runtime and root SSH directories, installed the
provider-injected public key with restrictive permissions, and started
`/usr/sbin/sshd`; `ps` showed its listener running (PID 552). A subsequent
local `runpodctl ssh info 2jh6oxjzogdexe` still returned `pod not ready`, with
no address or port. Thus the container and its SSH daemon are healthy, but
RunPod's external SSH-routing/control-plane path remains unavailable. No
transfer, dependency command, or Stage 0/S/A command has started. Next safe
step: obtain a direct SSH endpoint from the RunPod UI's Connect panel, or
continue only through the web terminal after an explicit bounded transfer
method is established.

The UI supplied `ssh 2jh6oxjzogdexe-64410b77@ssh.runpod.io -i
~/.ssh/id_ed25519`.  Using the configured RunPod key, the gateway accepted
public-key authentication and allocated a PTY, but it neither produced a
remote shell prompt nor returned output for `hostname; nvidia-smi -L; pwd`.
The initially suggested local `id_ed25519` is not the key embedded in this
pod; the RunPod-managed key is accepted. This confirms the gateway itself is
reachable but is not forwarding an interactive session to the healthy
container. No transfer or experiment command was attempted.

### 2026-07-28 final cleanup evidence

Under Ben's explicit Telegram authorization, `runpodctl pod delete
2jh6oxjzogdexe` returned `{\"deleted\": true}`. A subsequent account-wide
`runpodctl pod list --all` did not contain the pod. Its provider-observed
state immediately before deletion was RUNNING at USD 0.50/hour; no transfer,
dependency installation, or Stage 0/S/A command had ever started, and no
remote artifacts exist. The temporary pod must not be treated as an
experiment run.

- Provider/account: RunPod account verified by `runpodctl doctor` as Ben's
  account; no credentials are recorded here.
- Resource: one Secure Cloud RTX 3090 (24 GB). Ben's Telegram message 13770
  additionally permits a different available GPU within the same bounds.
- Image/template: official `runpod-torch-v220`,
  `runpod/pytorch:2.2.0-py3.10-cuda12.1.1-devel-ubuntu22.04`.
- Storage/network: 40 GB container disk and 30 GB temporary `/workspace`
  volume; SSH only.  No persistent volume, endpoint, or snapshot.
- Bound: maximum four wall-clock hours and USD 3.00 estimated-cost cap at
  the previously observed USD 0.50/hour.  Do not create if the quoted price
  makes the four-hour bound exceed USD 3.00.
- Source/data: pinned local commit `8907d0f` plus only the existing public,
  explicit-CC eight-track subset from the retained MTG-Jamendo corpus and its
  manifest.  No unrelated workspace files, credentials, or OpenClaw state.
- Commands: Stage 0, Stage S, then Stage A only.  No corpus download, model
  fine-tuning, full run, Stage C, or Stage D.

## Approved Stage-A amendment

Apply the 1.5--6.0 absolute-NLL band independently only for a stratum with
at least four spans.  Retain the unconditional `<0.5` alignment-bug stop;
the existing `>8` broken-conditioning stop is also retained.  Sparse strata
are reported as support-insufficient rather than used to fail the ordinary
band. Commit `8907d0f` additionally fails closed on non-finite NLLs,
including sparse strata; focused tests pass 9/9.

## Retrieval and cleanup

Retrieve logs, JSON, environment/version record, manifest, and SHA-256 list
to this run's `artifacts/`; parse JSON and verify checksums locally.  Then
terminate (not stop) the pod immediately and confirm the provider's empty
list/404 state.  Do not leave a resource running while recording results.

## Preflight evidence

- `2026-07-27T14:03Z`: `runpodctl doctor` healthy; API and SSH-key checks
  passed.
- `2026-07-27T14:06Z`: `runpodctl gpu list` contained no available RTX 3090.
  No resource was created and no cost incurred.
- `2026-07-27T18:17:07Z`: provisioned pod `vbu5r47gstyl16`: one Secure Cloud
  RTX 3090 in CZ, official `runpod-torch-v220` image, 40 GB container disk,
  30 GB temporary volume, USD 0.50/hour. Provider auto-termination is set for
  `2026-07-27T22:16:23Z`; four hours projects to USD 2.00, below the USD-3 cap.
- `2026-07-27T19:26:42Z`: after detecting that the prior foreground setup had
  been interrupted and the pod was idle, started dependency installation and
  tests in persistent tmux session `hdc-smoke-r2`.
- Transfer deviation: the selective code transfer was correct, but the audio
  rsync copied all 24 retained explicit-CC files rather than only the intended
  eight. Execution remains hard-limited to `--limit 8`; the extra 16 files
  are public licensed inputs already within the approved retained corpus and
  will disappear with the temporary volume at pod termination.

## Local-only input-scope audit (2026-07-27T23:55Z)

The pinned Stage 0 loader enumerates each extension and sorts paths before it
applies `--limit`.  Since the transferred retained corpus is MP3-only, the
authorized eight inputs are deterministically the first eight lexical MP3
names: `track_0000382.mp3`, `track_0000387.mp3`, `track_0000759.mp3`,
`track_0000760.mp3`, `track_0000761.mp3`, `track_0000762.mp3`,
`track_0000764.mp3`, and `track_0000765.mp3`.  Their measured retained
duration is 2,098.468 seconds.  Against
`../../20260726T043220Z-gpu-run/artifacts/audio_manifest_with_download_date.tsv`,
the SHA-256 of the newline-delimited `local_file<TAB>sha256` records in that
order is `60183005efa4dd7b8864bdbf7c24dae7667e563f20fb6d78f5e1c293a86e27e3`.

Before accepting any Stage 0 result, retrieval must show its exact selected
filenames and verify their content hashes against that manifest/fingerprint.
`--limit 8` by itself is not enough evidence if the transferred directory's
contents or extensions differ. This audit was local only: it neither contacted
nor changed the pod.
