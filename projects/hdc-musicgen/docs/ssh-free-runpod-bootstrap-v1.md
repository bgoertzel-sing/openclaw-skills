# SSH-free RunPod bootstrap v1

Status: design/preflight only. No pod, artifact host, or paid resource has
been created by this document.

## Purpose

Run the already frozen full-corpus MusicGen protocol despite an unavailable
RunPod external SSH gateway. The method must neither alter the scientific
protocol nor transfer credentials, OpenClaw state, private data, or an SSH
key to the pod.

## Frozen experiment boundary

- Source: `agent/stagec-oracle-diagnostic`, commit
  `cb126876558fa2496b372ba8c35cb9bb90bf9e2d` (plus only the previously
  accepted fail-closed aggregate-completeness hardening, if explicitly pinned
  before a new run).
- Public input corpus: the 24 explicit-CC tracks specified by the retained
  manifest. The pod fetches the pinned source URLs itself and verifies each
  SHA-256 before Stage 0; it does not receive the local audio directory.
- Stages and stops: exactly 0/S/A/C/D and their frozen gates. No backbone
  update or protocol tuning.

## Proposed transport architecture

1. Publish one immutable source bundle containing the pinned code, the audio
   manifest, bootstrap script, and SHA-256 manifest to a deliberately chosen
   artifact location. The bundle excludes `.git`, environments, credentials,
   and audio files.
2. Create the pod with a provider startup command that downloads the bundle,
   verifies its SHA-256, fetches/verifies the public audio files, creates the
   environment, and runs the frozen staged command. This removes the need for
   an interactive remote shell to start work.
3. The bootstrap records stdout/stderr, installed package versions, GPU
   details, input hashes, stage checkpoints, exit status, and a final output
   checksum manifest.
4. It transfers the compact result archive through a non-SSH channel. The
   preferred candidate is the Croc implementation embedded in `runpodctl`,
   because it is end-to-end encrypted and does not require putting a storage
   credential on the pod. A local receiver starts from the deterministic
   rendezvous code only after the remote job reaches its terminal state.
5. Local verification unpacks the archive, validates SHA-256 and required
   JSON gates, then the provider pod is terminated.

## Design gates before paid execution

- **Artifact source authorization:** choose a hosting location and visibility.
  A new public GitHub repository/release would publish the bundle; a private
  source needs a narrowly scoped, noninteractive read route. Neither is
  authorized by the earlier compute approval.
- **Provider startup seam:** verify RunPod's exact `docker-args`/
  entrypoint behavior using a no-GPU or otherwise non-billable probe before
  relying on it for the scientific run. The current CLI documents the field
  but does not establish the required command-override semantics locally.
- **Croc interoperability:** test a tiny benign archive from a shell that has
  no SSH access. This establishes that the relay path and return procedure
  work before the expensive job.
- **Artifact completeness:** the bootstrap must package only results, logs,
  provenance, and checkpoints--not dependency/model caches--and must leave a
  final terminal marker only after the checksum manifest is written.

## Security and operational limits

- Do not embed a GitHub, cloud-storage, RunPod, or SSH secret in the source
  bundle, Docker arguments, environment, logs, or result archive.
- A publicly hosted source bundle is integrity-checked by SHA-256 but remains
  publicly readable. The code and input manifest appear non-secret; this is
  an owner visibility decision, not an assumption.
- A private hosted bundle requires a separate secure read mechanism. A bearer
  token passed in pod environment is not acceptable without an explicit
  credential-handling plan.
- This transport design does not repair RunPod's SSH routing. It reduces the
  experiment's dependence on it.

## Next gate

Prepare a no-science transport probe and a fresh full
provider/GPU/price/time/cost approval. The prior MusicGen allocation failed
before execution and its USD 5 bound is not reusable.

## Publication evidence (2026-07-29)

The selected public route is live at GitHub repository
`bgoertzel-sing/runpod-ssh-free-bootstrap`, release `v0.1.0`. Asset
`musicgen-full-corpus-v1-source.tar.gz` downloaded anonymously over HTTPS and
matched its published SHA-256. It contains source commit `41022d5`, the public
audio manifest, and full-corpus command only. This clears source distribution,
not startup/return transport validation or paid-run approval.
