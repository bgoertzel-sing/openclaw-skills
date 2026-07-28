# HDC–CGCCT Transformer Programme

- Slug: `hdc-cgcct-transformers`
- Status: `active`
- Created: `2026-07-26`
- Last reviewed: `2026-07-27`
- Owner: Benjamin Goertzel

## Purpose

Test whether hypervector frame codes make the Category-Guided Causal-Coding Transformer
(CGCCT) programme empirically measurable and useful at small scale. The programme begins
with HDC instrument calibration and frozen-model frame extraction, then gates any guided
training on those results.

## Success criteria

- Reproducible P0–P1 HDC library and synthetic-grammar calibration report.
- A falsifiable P2 measurement of extractable role-factorized frame structure in frozen GPT-2
  small, with prescribed controls.
- If gates pass, P3–P5 evidence distinguishing module-hygiene gains from validation-loss loss.
- Source-audited mathematical assumptions and a durable `RESULTS.md` with raw artifacts.

## Scope

### In scope

- The staged P0–P6 programme in *Hypervector Frames for Category-Guided Causal Coding*.
- HDC frame codes, capacity/probe calibration, naturality, footprints, closure, and continual
  adaptation measurements.
- Theory audit of the HDC and CGCCT source manuscripts, including assumptions required for
  claimed guarantee transfers.

### Out of scope for now

- Claims about at-scale LLM quality, open-ended generation, or broad typological universality.
- Paid remote compute; autonomous spend budget is USD 0.

### Out of scope for now

## Current state

Ben supplied the synthesis paper plus the HDC and CGCCT background manuscripts on 2026-07-26.
The source-grounded P0/P1 execution specification and theorem-assumption audit are complete.
The isolated CPU P0 HDC implementation is committed at `fa11721` on local branch
`agent/p0-core`; its 13 exact self-tests passed again during the shutdown checkpoint.

The P0-G1 independent-cleanup replay is concluded fail-closed. A fresh local single-thread
replay wrote two byte-identical 36-cell payloads (both SHA-256
`e0602a37c97dde9d7fa8704bf0d4fe9aa0ccae7be5196dd267e3cdcae4d23f46`) and a
validator artifact (`p0-g1.json`, SHA-256
`719215ee8b08f88ced2847b55eddc277b488d2e21407e1af52f60203ae5c89e1`). The
validator failed because the frozen `k=4,M=32` curve is saturated at 1.000
accuracy at every dimension, producing required-positive Spearman association
`0.0`. P1 is blocked by the recorded P0-G1 gate; this must not be relabeled as
either a passing capacity result or a runtime interruption.

On 2026-07-27, a further clean CPU-only confirmation invocation again passed all
13 exact tests and reproduced those three artifact hashes exactly. It returned
the same expected nonzero exit because `P0-G1 passed=False`; the evidence is
`experiments/20260727T1158Z-p0-g1-replay-confirmation/`. No P1 work was begun.

The scheduled worker repeated the same clean CPU-only replay at
`2026-07-27T15:58Z`: the 13 tests passed and the two payload plus validator
hashes remained exact matches. The result is still `P0-G1 passed=False`, not a
runtime interruption; evidence is
`experiments/20260727T1558Z-p0-g1-replay-worker/`. P1 remains blocked.

At `2026-07-27T19:58Z`, a new fresh local CPU-only replay again passed all 13
tests and wrote two byte-identical payloads with the same SHA-256
`e0602a37c97dde9d7fa8704bf0d4fe9aa0ccae7be5196dd267e3cdcae4d23f46`; its
validator hash was again
`719215ee8b08f88ced2847b55eddc277b488d2e21407e1af52f60203ae5c89e1` and
returned the expected nonzero status for `P0-G1 passed=False`. New artifacts
were isolated at `artifacts/20260727T195800Z-p0-g1-replay-worker/`, preserving
the original evidence. P1 remains blocked by the frozen gate.

A recurring CPU-only progress worker was added on 2026-07-27 to resume this
interrupted local gate and continue only through the staged P0/P1 plan.

Benjamin authorized a harder P0 fixture/grid on 2026-07-27 while retaining the
P0-G1 contract. The v2 CPU-only run used `D={32,64,128,256,512,1024}`,
`k={32,64,128}`, and `M={32,256}`, with 2,048 trials/cell and seed 12011. It
passed 13/13 tests and P0-G1: the two payloads are byte-identical SHA-256
`96f3a7142111828cffa458a59ac35699c6ce0077748a14361063ecc4b4dd14f7`, and all
six curve Spearmans are 1.0. The v1 failure remains preserved as ceiling
evidence. P1 is now unblocked for CPU-local P1A preflight. Evidence:
`experiments/20260727T213214Z-p0-g1-v2-authorized-grid/RUN.md`; runner commit
`ce7616d` on `agent/p0-core`.

P1A full-grid metrics and calibration implementation is complete at nested
commit `e4e1d65`. A reduced CPU replay smoke passed 18 tests and generated two
byte-identical payloads, but is explicitly gate-ineligible. The full frozen
grid has not yet run, so no calibration criteria or P1A result are claimed.

## Repositories

| Role | Remote | Local path | Branch/default | Pinned/reference commit |
|---|---|---|---|---|

## Environments

Document local virtual environments, containers, toolchain pins, datasets, and remote resources without credentials.

## Key results

- [P0/P1 execution specification and theorem-assumption audit](docs/p0-p1-spec.md):
  freezes formulas, fixtures, deterministic conventions, gates, raw artifacts, and exact planned
  commands. It distinguishes the conditional coherence-aware cleanup law from the unresolved
  claim that linguistic hierarchies induce near-duplicate code geometry.
- Source bundle:
  `../../library/hdc-cgcct-source-manuscripts-2026/SOURCE.md`.
- P0 implementation checkpoint: local repository `repos/hdc-cgcct-probes/`, branch
  `agent/p0-core`, commit `fa11721`; the completed first replay is
  `artifacts/p0-selftest-v2/capacity-replay-a.json`.
- P0-G1 deterministic replay completion: `capacity-replay-a.json` and
  `capacity-replay-b.json` are bit-identical, but the frozen qualitative gate
  is `false`; see `experiments/20260726T184741Z-p0-selftest-v2/RUN.md`.

## Open questions

- Can the claimed coherence-aware cleanup extension be derived under stated assumptions, or is
  it solely a P1 hypothesis?
- Does the proposed hierarchy construction actually induce the near-duplicate coherence regime?
- Does frozen GPT-2-small expose a low-defect role-factorized frame readout for the specified
  alternation batteries?

## Related projects and concepts

- `causal-fibres-ladder`: likely source of synthetic-transformer infrastructure and evidence gates.
- `hyperseed-formalizations`: conceptual link only; add a formalization only for a novel,
  consequential result or decision.

## Risks

Include correctness, reproducibility, security, cost, licensing, and semantic risks.

- The capacity/coherence and composition-monotonicity claims are not established by the cited
  displayed theorems and must not be treated as guarantees before validation.
- Probe success is query-family-specific and cannot establish general language understanding.
- P5 cost estimate requires local measurement before any request for paid compute.
