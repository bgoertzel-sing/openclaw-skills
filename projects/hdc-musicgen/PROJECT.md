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

Full-corpus r5 completed Stage 0 on 22 tracks / 66 minutes, then correctly
stopped: codebooks 1--3 were below the frozen 0.05 adjacent-token persistence
floor. A provider-free calibration subsequently triplicated every encoded
track, creating exact long-range recurrence while changing that metric by at
most `6.56e-06`. The metric is therefore a local codec-stability proxy, not a
corpus-recurrence validity test. r5 remains a terminal Stage-0 failure; a
prospective direct recurrence gate is needed before another MusicGen corpus
run. Evidence: `experiments/20260730T203550Z-full-corpus-r5/` and
`experiments/20260731T004101Z-persistence-proxy-calibration/`.

Ben approved a prospective repair at commit `74287d9` on
`agent/direct-recurrence-stage0-gate`: Stage 0 now validates coverage and
four-codebook token integrity, while Stage S directly gates cross-window
chroma recurrence. Exact-repeat/nonrepeat controls and the full local suite
passed 20/20. This amendment is forward-looking only; it neither changes r5
artifacts nor authorizes a new GPU run. Evidence:
`experiments/20260731T004951Z-direct-recurrence-gate-validation/`.

The r2 pre-Stage-0 failure has been repaired locally. The bootstrap now
installs `click`, imports the exact AudioCraft Stage-0 symbol before science,
and uses a wrapper that preserves the command's real exit status through
logging. A clean CPU environment passed the fail-closed compatibility audit,
the exact import, 11/11 focused tests, and success/failure status fixtures.
This is local preflight evidence only; a new immutable bundle and fresh paid
approval are prerequisites for another full-corpus attempt. Evidence:
`experiments/20260730T001926Z-full-corpus-r2-bootstrap-repair/`.

The 8-track smoke-r3 has completed successfully through stages 0/S/A and is
verified/terminated. It is a plumbing and small-support result only: its 24
encoded minutes do not meet the full corpus gate and its unrelated stratum has
only one span. Ben directed preparation of the full 24-track corpus run. The
full command is now frozen at `cb126876` with restart artifacts for Stage 0,
Stage A, and Stage D; local focused tests pass 10/10. A fresh costed GPU
approval remains required before provisioning. See
`experiments/20260728T210000Z-full-corpus-r1/`.

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
3090 was available in the first live preflight; later provisioning attempts
are reconciled below.

Smoke-r2 is now closed as a terminal no-result. The first provisioned pod
received code/audio and began dependency setup, but neither it nor the
replacement pod ever started Stage 0/S/A; both pods were deleted and no stage
artifacts exist. The support-aware NLL amendment is accepted and hardened to
reject missing aggregates; it is no longer an open policy question. Any
future MusicGen run is a new activity requiring fresh explicit provider/
resource/price/cost/time/data/stop authorization.

## Repositories

| Role | Remote | Local path | Branch/default | Pinned/reference commit |
|---|---|---|---|---|
| Working implementation | local only | `projects/hdc-musicgen/worktrees/direct-recurrence-gate/` | `agent/direct-recurrence-stage0-gate` | `74287d9` |

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

None within the continuation worker's local scope. A future execution requires
fresh explicit authorization naming provider, resource, price, cost/time cap,
existing-data scope, and immediate stop/retrieval/termination conditions.

## Related projects and concepts

Resonator-factored hierarchical hypervectors; MusicGen/EnCodec; fixed-width
structured memory; factor-aligned computation.

## Risks

Version-sensitive conditioning internals, structure-detector threshold
sensitivity, insufficient RELATED/UNRELATED support after track splitting,
model-context limits, corpus licensing, local dependency failure, and
unapproved GPU spend.
