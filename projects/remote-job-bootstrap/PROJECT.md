# SSH-Free RunPod Bootstrap Bundles

- Slug: `remote-job-bootstrap`
- Status: `active`
- Created: `2026-07-29`
- Last reviewed: `2026-07-31`
- Owner: Benjamin Goertzel

## Purpose

Provide reproducible, integrity-checked startup and artifact-return plumbing
for RunPod jobs that does not depend on RunPod's unreliable external SSH
gateway. The first consumers are the HDC MusicGen full-corpus run and the
RelaLeap settlement-depth sweep.

## Success criteria

- A public GitHub repository contains no secrets and publishes immutable,
  SHA-256-addressed source bundles for MusicGen and RelaLeap.
- A harmless transport probe proves unauthenticated bundle download,
  startup-command execution, and non-SSH artifact return before a GPU run.
- Each scientific job remains pinned to its existing protocol/source and is
  separately cost-approved before provisioning.

## Scope

### In scope

- Public bootstrap repository, release bundles, checksums, startup scripts,
  Croc/non-SSH return probe, and cross-project provenance records.

### Out of scope for now

- GPU provisioning without a fresh applicable approval; publishing private
  data, credentials, local Git metadata, model caches, or unrelated source.

## Current state

Public repository and release are live: `bgoertzel-sing/runpod-ssh-free-bootstrap`
at commit `8cad73d`, release `v0.1.0`. Its two source-only archives were
downloaded anonymously over HTTPS and verified against the published
`SHA256SUMS` file. Local transport validation now passes: the public bundle
fetched/verified, a compact probe artifact verified, the pinned official
`runpodctl` binary hash verified, and a Croc send/receive round trip preserved
the file hash. On 2026-07-29, the approved bounded remote probe made two Secure
A40 allocation requests, both rejected before a pod ID was issued (general
placement resource error; then `CA-MTL-1` no instances). A later three-pod
debug sequence used 20-GB/no-volume A40 pods but returned no artifact; the
final pod was terminated after exceeding the original 30-minute probe bound.
All probe pods are now removed. Evidence:
`experiments/20260729T1555Z-remote-transport-probe/`.

On 2026-07-31, a template-based Secure RTX 4090 control canary succeeded with
explicit ports and SSH: direct TCP and managed-key authentication both passed,
the host reported the expected GPU, and the pod was deleted after about 74
seconds. This establishes that the account-wide SSH machinery and known-good
template path currently work. Evidence:
`experiments/20260731T133317Z-template-ssh-canary/`.

The immediate raw-image B arm also succeeded with the identical image, GPU,
disk, explicit ports, and SSH; remote PID 1 included `/start.sh`. Thus raw
`--image` is not itself the failure in current CLI behavior. The evidence
instead points to omitted explicit ports/SSH in failed specs or intermittent
provider placement/startup. Evidence:
`experiments/20260731T140535Z-raw-image-ssh-ab/`.

A provider-free inspection of the installed `runpodctl 2.8.0` binary and its
exact official source found that `--ssh` defaults true and always serializes
as `startSsh`, while an omitted `--ports` omits the GraphQL field. Explicit
`22/tcp` is therefore materially important, but archived launch commands show
at least two recent `pod not ready` failures already included `22/tcp` with
SSH enabled. Port omission cannot explain the failure class generally;
intermittent provider readiness remains the leading unresolved cause. Evidence:
`experiments/20260731T145013Z-runpodctl-payload-inspection/`.

## Repositories

| Role | Remote | Local path | Branch/default | Pinned/reference commit |
|---|---|---|---|---|
| Bootstrap publication | `https://github.com/bgoertzel-sing/runpod-ssh-free-bootstrap` | `projects/remote-job-bootstrap/repos/runpod-ssh-free-bootstrap` | `main` | `8cad73d`; release `v0.1.0` |

## Environments

GitHub CLI authenticated locally; no remote compute or public repository has
yet been created for this project.

## Key results

- Release `v0.1.0`: source bundles, immutable release tag, anonymous HTTPS
  checksum verification.
- MusicGen design: `../hdc-musicgen/docs/ssh-free-runpod-bootstrap-v1.md`.
- RelaLeap design: `../relaleap/docs/ssh-free-runpod-bootstrap-v1.md`.

## Open questions

- Validate provider `docker-args`/startup-command semantics from an actual
  isolated pod; the non-SSH return primitive has local evidence only. Current
  blocker: a remote observability/return design that can distinguish startup
  failure from relay failure, plus a newly approved resource/count/time/cost
  envelope.

## Related projects and concepts

`hdc-musicgen`; `relaleap`; content-addressed artifacts; fail-closed remote
execution.

## Risks

Accidental publication of credentials/private files; mutable or unhashed
downloads; startup command semantics that differ from RunPod CLI wording;
Croc relay unavailability; scientific-protocol drift hidden in packaging.
