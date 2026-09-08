# SSH-free RunPod bootstrap v1: settlement-depth sweep

Status: design/preflight only; it does not itself authorize another GPU pod.

## Purpose

Execute the frozen clean-room settlement-depth grid without relying on RunPod's
external SSH gateway for source transfer, launch, monitoring, or artifact
return. This is operational plumbing, not a change to the sweep estimand.

## Frozen boundary

- Source: `agent/cleanroom-settle-sweep` commit
  `68d7bc21eac665074a73c67d26838b4487ba1b82`, source archive SHA-256
  `f11cbb652b13d983b6498503522760906a6a4e26cccdf13f87c496fb21987889`.
- Public runtime inputs: GPT-2 revision
  `607a30d783dfa663caf39e06633721c8d4cfcd7e` and WikiText-103 revision
  `b08601e04326c79dfdd32d625aee71d232d685c3`.
- Protocol: seeds `1729,3253,6421`, T in `{1,2,4,8}`, every specified replay
  and finite-value invariant, no altered hyperparameters.

## Proposed transport architecture

1. Publish only the immutable source bundle to an owner-chosen artifact URL;
   record and verify its SHA-256 before execution. It contains no credentials,
   local Git metadata, SSH material, model cache, or unrelated files.
2. A provider startup command downloads the bundle, verifies the hash,
   installs the pinned application dependencies, runs the frozen grid, and
   writes all partial and terminal records under a single result directory.
3. The pod retrieves the two public pinned Hugging Face assets directly.
4. A non-SSH return channel transfers `seed*.json`, `summary.json`,
   `SHA256SUMS`, logs, source hash, environment/GPU record, and exit status.
   Croc via the `runpodctl` implementation is the preferred candidate because
   it avoids placing a storage credential on the pod; it must be validated by
   a tiny harmless round-trip before use.
5. Local validation checks the returned hashes and each frozen arm invariant;
   then the pod is terminated rather than stopped.

## Preconditions before another paid run

- The same source-bundle visibility/hosting decision as MusicGen.
- An observed, non-billable or separately bounded startup-command probe: the
  CLI's `docker-args` field alone does not prove its entrypoint semantics.
- A verified Croc return test from a process with no SSH route.
- A fresh resource/price/time/cost proposal if the earlier $10/14h29m approval
  cannot safely apply after the transport design changes.

The previous allocated pod `klgwjx641wlqrk` was created before this bootstrap
existed, exposed no SSH endpoint, did no computation, and was deleted; it
cannot validate this design.

## Publication evidence (2026-07-29)

The selected public route is GitHub repository
`bgoertzel-sing/runpod-ssh-free-bootstrap`, release `v0.1.0`. Asset
`relaleap-settle-sweep-v1-source.tar.gz` downloaded anonymously over HTTPS and
matched its published SHA-256. It is source commit `68d7bc2` only. This does
not validate the provider startup or artifact-return seams and does not itself
authorize another GPU allocation.
