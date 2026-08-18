# HDC–CGCCT Transformer Programme

- Slug: `hdc-cgcct-transformers`
- Status: `active`
- Created: `2026-07-26`
- Last reviewed: `2026-08-16`
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

The frozen P1A full grid subsequently completed successfully with payload
SHA-256 `b7fabae33494ed090fe1cd73b85fff0ad3f36fe7f3c6f986ed1a30ab0197195b`.
All 60 F0/F1 curves were interior, but 31/60 missed the frozen Spearman
monotonicity threshold; this is calibration evidence, not a confirmation
verdict. P1B's exact planted-PCFG, six-layer causal decoder, residual/readout,
manifest, and CPU smoke are implemented at nested commit `b4593f4`; 22 tests
and two byte-identical smoke/manifest replays passed. Remote provisioning
remains blocked. The frozen P1B target-code layer and reduced ridge/artifact
replay are implemented at `7f46c5a`; 24 tests pass and two payloads are
byte-identical. The reduced run is gate-ineligible: the full trainer,
controls, raw artifact contract, metrics, and criteria freezer remain required
before recording a fresh priced offer or provisioning.

The conditionally approved P1B calibration subsequently completed exactly
seeds `12011`, `13121`, and `14251` on one 24-GiB RTX 3090 at USD 0.22/hour.
All three raw artifacts passed local hash and finite-array verification, and
their payload hashes were frozen in `artifacts/criteria.json` before any
confirmation seed was opened. RunPod pod `qy0rbiqrd3xvbf` was deleted after
artifact return. Evidence:
`experiments/20260727T225600Z-p1b-gpu-calibration-planned/RUN.md`.

A later, separately authorized sealed confirmation run completed all five
confirmation seeds on one Secure 24-GiB RTX 4090 without changing the frozen
criteria. All 160 returned manifest entries and all five artifact digests
verified locally; pod `38dun5tixpgvnd` was deleted and provider absence was
confirmed. The next scientific task is interpretation under the frozen
criteria; no further remote compute is required. Evidence:
`experiments/20260731T190413Z-p1b-confirmation-reliability-retry/RUN.md`.

A subsequent frozen-contract audit found that P1-G2 is not evaluable from the
returned artifacts: confirmation cells omit the required oracle-code arm, and
the frozen criteria omit the P1A-derived `D_pred` mapping required to select
the evaluated dimensions. Artifact integrity remains verified, but scientific
interpretation now fails closed as `gate_not_evaluable_contract_incomplete`.
No additional seed or remote resource was opened. Evidence:
`experiments/20260731T235800Z-p1b-gate-contract-audit/RUN.md`; latest
engineering-integrity verification:
`experiments/20260803T040309Z-p1b-gate-integrity-worker/RUN.md`.

Ben authorized a versioned post-hoc interpretation repair on 2026-08-02. The
contract-v2 evaluator at nested commit `b34b6f1` pins the missing P1A-to-P1B
dimension mapping, reconstructs oracle scores from the exact manifest and
target-code generator, and rejects provenance/shape drift. Its 31-test suite
passed and two full five-seed evaluations were byte-identical. Under the
required post-hoc label, P1-G2 is now evaluable and classifies
`instrument_failed`: oracle pooled `V_all=0.02926953125` (Wilson
`U95=0.02982250554`) and linear-K pooled `V_all=0.02966796875` (Wilson
`U95=0.03022454252`), with feature-BER failures in both arms. Frozen criteria
v1 remains unchanged and no new seed or remote resource was opened. Evidence:
`experiments/20260803T080400Z-p1g2-contract-v2/RUN.md`.

The 2026-08-12 12:41Z scheduled-worker checkpoint passed all 31 tests at
nested commit `b34b6f1` and reproduced the contract-v2 result byte-for-byte at
SHA-256 `40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
P1 remains terminal as `instrument_failed`; no P0 replay, seed opening,
criteria change, provider query, remote resource, or paid work occurred.
Evidence:
`experiments/20260812T124100Z-p1-terminal-integrity-r2/RUN.md`.

The 2026-08-15 06:22Z checkpoint again passed all 31 tests and reproduced the
same contract-v2 result byte-for-byte at SHA-256
`40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
P1 remains terminal as `instrument_failed`; no P0 run, seed opening, criteria
change, provider query, remote resource, or paid work occurred. Evidence:
`experiments/20260815T062200Z-p1-terminal-integrity-r15/RUN.md`.

The 2026-08-15 10:22Z checkpoint again passed all 31 tests and reproduced the
same contract-v2 result byte-for-byte at SHA-256
`40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
P1 remains terminal as `instrument_failed`; no P0 run, seed opening, criteria
change, provider query, remote resource, or paid work occurred. Evidence:
`experiments/20260815T102200Z-p1-terminal-integrity-r16/RUN.md`.

The 2026-08-15 14:22Z checkpoint again passed all 31 tests and reproduced the
same contract-v2 result byte-for-byte at SHA-256
`40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
P1 remains terminal as `instrument_failed`; no P0 run, seed opening, criteria
change, provider query, remote resource, or paid work occurred. Evidence:
`experiments/20260815T142200Z-p1-terminal-integrity-r17/RUN.md`.

The 2026-08-17 02:41Z checkpoint again passed all 31 tests and reproduced the
same contract-v2 result byte-for-byte at SHA-256
`40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
P1 remains terminal as `instrument_failed`; no P0 run, seed opening, criteria
change, provider query, remote resource, or paid work occurred. Evidence:
`experiments/20260817T024100Z-p1-terminal-integrity-r26/RUN.md`.

The 2026-08-17 18:46Z checkpoint again passed all 31 tests and reproduced the
same contract-v2 result byte-for-byte at SHA-256
`40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
P1 remains terminal as `instrument_failed`; no P0 run, seed opening, criteria
change, provider query, remote resource, or paid work occurred. Evidence:
`experiments/20260817T184600Z-p1-terminal-integrity-r29/RUN.md`.

The 2026-08-18 10:46Z checkpoint again passed all 31 tests and reproduced the
same contract-v2 result byte-for-byte at SHA-256
`40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
P1 remains terminal as `instrument_failed`; no P0 run, seed opening, criteria
change, provider query, remote resource, or paid work occurred. Evidence:
`experiments/20260818T104600Z-p1-terminal-integrity-r32/RUN.md`.

The 2026-08-18 18:49Z checkpoint again passed all 31 tests and reproduced the
same contract-v2 result byte-for-byte at SHA-256
`40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
P1 remains terminal as `instrument_failed`; no P0 run, seed opening, criteria
change, provider query, remote resource, or paid work occurred. Evidence:
`experiments/20260818T184900Z-p1-terminal-integrity-r34/RUN.md`.

The 2026-08-12 16:41Z checkpoint again passed all 31 tests and reproduced the
same contract-v2 result byte-for-byte. P1 remains terminal as
`instrument_failed`; no P0 replay, seed opening, criteria change, provider
query, or remote work occurred. Evidence:
`experiments/20260812T164100Z-p1-terminal-integrity-r3/RUN.md`.

The 2026-08-12 20:41Z checkpoint again passed all 31 tests and reproduced the
same contract-v2 result byte-for-byte. P1 remains terminal as
`instrument_failed`; no P0 replay, seed opening, criteria change, provider
query, or remote work occurred. Evidence:
`experiments/20260812T204100Z-p1-terminal-integrity-r4/RUN.md`.

The 2026-08-13 00:41Z checkpoint again passed all 31 tests and reproduced the
same contract-v2 result byte-for-byte. P1 remains terminal as
`instrument_failed`; no P0 replay, seed opening, criteria change, provider
query, or remote work occurred. Evidence:
`experiments/20260813T004100Z-p1-terminal-integrity-r5/RUN.md`.

The 2026-08-13 04:42Z checkpoint again passed all 31 tests and reproduced the
same contract-v2 result byte-for-byte. P1 remains terminal as
`instrument_failed`; no P0 replay, seed opening, criteria change, provider
query, remote resource, or paid work occurred. Evidence:
`experiments/20260813T044200Z-p1-terminal-integrity-r6/RUN.md`.

The 2026-08-13 08:48Z checkpoint again passed all 31 tests and reproduced the
same contract-v2 result byte-for-byte. P1 remains terminal as
`instrument_failed`; no P0 replay, seed opening, criteria change, provider
query, remote resource, or paid work occurred. Evidence:
`experiments/20260813T084800Z-p1-terminal-integrity-r7/RUN.md`.

The 2026-08-13 12:58Z checkpoint again passed all 31 tests and reproduced the
same contract-v2 result byte-for-byte. P1 remains terminal as
`instrument_failed`; no P0 replay, seed opening, criteria change, provider
query, remote resource, or paid work occurred. Evidence:
`experiments/20260813T125800Z-p1-terminal-integrity-r8/RUN.md`.

The 2026-08-13 17:24Z checkpoint again passed all 31 tests and reproduced the
same contract-v2 result byte-for-byte at SHA-256
`40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
P1 remains terminal as `instrument_failed`; no P0 replay, seed opening,
criteria change, provider query, remote resource, or paid work occurred.
Evidence: `experiments/20260813T172450Z-p1-terminal-integrity-r9/RUN.md`.

The 2026-08-13 21:29Z checkpoint again passed all 31 tests and reproduced the
same contract-v2 result byte-for-byte at SHA-256
`40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
P1 remains terminal as `instrument_failed`; no P0 run, seed opening, criteria
change, provider query, remote resource, or paid work occurred. Evidence:
`experiments/20260813T212900Z-p1-terminal-integrity-r10/RUN.md`.

The 2026-08-14 01:47Z checkpoint again passed all 31 tests and reproduced the
same contract-v2 result byte-for-byte at SHA-256
`40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
P1 remains terminal as `instrument_failed`; no P0 run, seed opening, criteria
change, provider query, remote resource, or paid work occurred. Evidence:
`experiments/20260814T014700Z-p1-terminal-integrity-r11/RUN.md`.

The 2026-08-14 09:58Z checkpoint again passed all 31 tests and reproduced the
same contract-v2 result byte-for-byte at SHA-256
`40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
P1 remains terminal as `instrument_failed`; no P0 run, seed opening, criteria
change, provider query, remote resource, or paid work occurred. Evidence:
`experiments/20260814T095800Z-p1-terminal-integrity-r12/RUN.md`.

The 2026-08-14 14:10Z checkpoint again passed all 31 tests and reproduced the
same contract-v2 result byte-for-byte at SHA-256
`40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
P1 remains terminal as `instrument_failed`; no P0 run, seed opening, criteria
change, provider query, remote resource, or paid work occurred. Evidence:
`experiments/20260814T141000Z-p1-terminal-integrity-r13/RUN.md`.

The terminal local integrity replay passed all 31 tests again on 2026-08-08
at nested commit `b34b6f1` and reproduced the identical contract-v2 result
hash. P1 remains terminal as `instrument_failed`; no P0 replay, seed opening,
provider query, or remote work occurred. Evidence:
`experiments/20260808T001700Z-p1-terminal-integrity-20260808/RUN.md`.

A second 2026-08-08 scheduled-worker checkpoint again passed all 31 tests and
reproduced the contract-v2 result byte-for-byte at SHA-256
`40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
P1 remains terminal as `instrument_failed`; no P0 replay, seed opening,
criteria change, provider query, remote resource, or paid work occurred.
Evidence:
`experiments/20260808T121700Z-p1-terminal-integrity-20260808-r2/RUN.md`.

A third 2026-08-08 scheduled-worker checkpoint passed all 31 tests and
reproduced the same contract-v2 result byte-for-byte at SHA-256
`40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
P1 remains terminal as `instrument_failed`; no P0 replay, seed opening,
criteria change, provider query, remote resource, or paid work occurred.
Evidence:
`experiments/20260809T002100Z-p1-terminal-integrity-20260808-r3/RUN.md`.

The terminal local integrity replay passed all 31 tests again on 2026-08-04
and reproduced the contract-v2 result byte-for-byte at SHA-256
`40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
P1 remains terminal as `instrument_failed`; no seed was opened and no remote
resource was used. Evidence:
`experiments/20260804T201328Z-p1-terminal-integrity-20260804/RUN.md`.

The 2026-08-05 scheduled-worker integrity replay again passed all 31 tests and
reproduced the identical contract-v2 result hash. The terminal
`instrument_failed` gate is unchanged; no P0 replay, seed opening, criteria
change, remote resource, or paid work occurred. Evidence:
`experiments/20260805T120329Z-p1-terminal-integrity-20260805/RUN.md`.

The 2026-08-06 scheduled-worker integrity replay passed all 31 tests and
reproduced the same contract-v2 result byte-for-byte at SHA-256
`40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
The stale P0/P1 payload did not reopen any completed lane: P1 remains terminal
as `instrument_failed`, and no P0 replay, seed opening, criteria change,
provider query, remote resource, or paid work occurred. Evidence:
`experiments/20260806T081600Z-p1-terminal-integrity-20260806/RUN.md`.

The 2026-08-07 scheduled-worker integrity replay again passed all 31 tests and
reproduced the identical contract-v2 result hash. The terminal
`instrument_failed` gate is unchanged; no P0 replay, seed opening, criteria
change, provider query, remote resource, or paid work occurred. Evidence:
`experiments/20260807T081700Z-p1-terminal-integrity-20260807/RUN.md`.

The second 2026-08-07 scheduled-worker checkpoint again passed all 31 tests
and reproduced the contract-v2 result byte-for-byte at SHA-256
`40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
P1 remains terminal as `instrument_failed`; no P0 replay, seed opening,
criteria change, provider query, remote resource, or paid work occurred.
Evidence:
`experiments/20260807T201700Z-p1-terminal-integrity-20260807-r2/RUN.md`.

The 2026-08-16 10:26Z checkpoint again passed all 31 tests and reproduced the
same contract-v2 result byte-for-byte at SHA-256
`40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
P1 remains terminal as `instrument_failed`; no P0 run, seed opening, criteria
change, provider query, remote resource, or paid work occurred. Evidence:
`experiments/20260816T102600Z-p1-terminal-integrity-r22/RUN.md`.

## Repositories

The 2026-08-17 14:45Z checkpoint again passed all 31 tests and reproduced the
same contract-v2 result byte-for-byte at SHA-256
`40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
P1 remains terminal as `instrument_failed`; no P0 run, seed opening, criteria
change, provider query, remote resource, or paid work occurred. Evidence:
`experiments/20260817T144500Z-p1-terminal-integrity-r28/RUN.md`.

The 2026-08-17 06:41Z checkpoint again passed all 31 tests and reproduced the
same contract-v2 result byte-for-byte at SHA-256
`40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
P1 remains terminal as `instrument_failed`; no P0 run, seed opening, criteria
change, provider query, remote resource, or paid work occurred. Evidence:
`experiments/20260817T064100Z-p1-terminal-integrity-r27/RUN.md`.

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
