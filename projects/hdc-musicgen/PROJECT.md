# HDC × MusicGen Experiments

- Slug: `hdc-musicgen`
- Status: `active`
- Created: `2026-07-25`
- Last reviewed: `2026-07-27`
- Owner: Benjamin Goertzel

## Purpose

Test whether a fixed-width HDC summary of distant musical history, injected
through MusicGen's cross-attention path, recovers structurally relevant
long-range information that falls outside a 10-second local window. The
experiment is explicitly about capability, not speed.

## Success criteria

- The corpus gate has at least 20 tracks, 60 total minutes, and valid
  per-codebook persistence.
- Chroma self-similarity separates RELATED from UNRELATED spans by at least
  0.15 cosine.
- Stage A's length-controlled RELATED relevance gain is above 0.02 nats/token
  and clearly exceeds the UNRELATED gain, with NLL in the 1.5–6.0 sanity band.
- Stage C's noiseless cold/warm self-test is approximately 1.000.
- Stage D reports stratified summary gain, RELATED-minus-UNRELATED contrast,
  and fraction of the retrieval oracle recovered without updating the
  backbone.
- Pure-logic regression tests pass locally; model-dependent gaps remain
  explicitly unclaimed until an approved GPU run.

## Scope

### In scope

AudioCraft 1.3.0 codec/NLL plumbing; strict data validation; chroma
self-similarity and RELATED/UNRELATED span mining; matched versus
length-controlled random retrieval; optional resonator feasibility; and a
frozen-backbone HDC summary adapter.

### Out of scope for now

Paid compute, real-data downloads, backbone fine-tuning, or changes to the
runbook's frozen experimental choices.

## Current state

The first approved RTX 3090 job executed fail-closed through smoke Stage A. A
24-track, 123.6-minute explicit-CC MTG-Jamendo corpus was prepared. Smoke Stage
S separated RELATED from UNRELATED by 0.490 cosine. After two minimal
AudioCraft FRAGILE fixes, Stage A produced finite NLLs and a RELATED relevance
gain of 0.0521 versus 0.0007 UNRELATED, but its sole UNRELATED span had
absolute NLL 1.24–1.27, below the frozen 1.5 sanity floor. The full run and
Stages C/D were therefore not started. Artifacts are verified locally and the
RunPod pod is terminated. A new paid run requires an explicit decision about
the smoke-only sanity policy.

Ben has now approved a narrowly amended replacement: the absolute 1.5--6.0
NLL band is checked only within strata with at least four spans, while `<0.5`
alignment and `>8` conditioning stops remain unconditional. It may run Stage
0/S/A only on eight retained tracks, for at most four hours / USD 3. No RTX
3090 was available in the first live preflight, so it has not been provisioned.

## Repositories

| Role | Remote | Local path | Branch/default | Pinned/reference commit |
|---|---|---|---|---|
| Working implementation | local only | `projects/hdc-musicgen/repos/` | `agent/stagec-oracle-diagnostic` | `f4506a7094aaf5f549f16f605a8ef0bf808653c0` |

## Environments

- Local Python 3.10 virtual environment: `.venv` (ignored).
- Target dependency: `audiocraft==1.3.0`.
- Local smoke data: four generated mono 16 kHz, 40-second WAV files.
- No remote resource has been provisioned.

## Key results

- Source audit: `../../library/resonator-factored-hierarchical-hypervector-embeddings/SOURCE.md`
- Local smoke: `experiments/20260726T043220Z-local-smoke/RUN.md`.
- Structural rewrite: `experiments/20260725T-structural-rewrite/RUN.md`.
- GPU run: `experiments/20260726T043220Z-gpu-run/RUN.md`.

## Open questions

- Whether the absolute-NLL sanity band should be conjunctive for a one-span
  smoke stratum when values remain above the `<0.5` alignment-bug threshold.
- Whether to authorize a fresh paid run after resolving that policy.

## Related projects and concepts

Resonator-factored hierarchical hypervectors; MusicGen/EnCodec; fixed-width
structured memory; factor-aligned computation.

## Risks

Version-sensitive conditioning internals, structure-detector threshold
sensitivity, insufficient RELATED/UNRELATED support after track splitting,
model-context limits, corpus licensing, local dependency failure, and
unapproved GPU spend.
