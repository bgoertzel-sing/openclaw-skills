# Working Notes

## 2026-07-18 - Stratified CLA A6 re-sweep batch 10 and full-grid closure

Ran the four remaining tight-region roles4 cells at gain 5.0, couplings 0.35
and 0.60, delays 0 and 3, seeds 109, 113, and 127, with exact controls. Clean
OmegaSim `18c7408` and chaoslang `974af31` identities were verified before
measurement. All 36 rows reconstructed exactly; every grammar had two
productions and zero categories. `(5,.60,3)` reached exploratory 2/3 joint
matched-control wins; the other cells reached 0/3. No row met the grammar
priority rule. Together with batches 01--09 and separately frozen tight roles8
evidence, all 120 planned roles-specific cells are now covered and the sweep
closes as an informative negative for non-trivial grammar under the frozen
detector. This does not support a simplicity, chaos, attractor, or semantic-
grammar claim, and the stricter held-out coding failure remains gating.
Provenance: `experiments/20260718T084500Z-a6-stratified-cla-resweep-10/RUN.md`;
results JSON SHA-256
`52898641fd722a71ed834309d218d890fd841cb6b7cf85ff83f16958dd94fd8c`.

## 2026-07-17 - Stratified CLA A6 re-sweep batch 09

Ran the eight remaining non-tight triples across roles4 and roles8 with seeds
109, 113, and 127 and exact controls. Clean OmegaSim `18c7408` and chaoslang
`974af31` identities were verified before measurement. All 144 rows
reconstructed exactly; every grammar had two productions and zero categories.
`(2,.60,0)` reached exploratory 4/6 joint matched-control wins, `(1,.35,0)`
reached 3/6, `(5,.35,5)` reached 2/6, and `(1,.15,1)` reached 1/6. None met
the grammar-priority rule. The stratified series plus separately frozen tight
roles8 cells now provides 116/120 planned-cell evidence. Only the four tight
roles4 cells remain before the informative negative grammar result can close.
Provenance:
`experiments/20260718T064500Z-a6-stratified-cla-resweep-09/RUN.md`; results JSON
SHA-256 `8619fdc38e24f0abf57a77abdedebe3879c2f7cc65d2cfd44883b0e68ab1c59d`.

## 2026-07-17 - Stratified CLA A6 re-sweep batch 08

Ran eight additional uncovered triples across roles4 and roles8 with seeds
109, 113, and 127 and exact controls. Clean OmegaSim `18c7408` and chaoslang
`974af31` identities were verified before measurement. All 144 rows
reconstructed exactly; every grammar had two productions and zero categories.
`(2,.15,0)` reached exploratory 6/6 joint matched-control wins, while
`(5,.35,1)` reached 3/6 and `(2,.80,5)` reached 2/6. None met the
grammar-priority rule. Successful batches now cover 96/120 roles-specific
cells. Provenance:
`experiments/20260718T044500Z-a6-stratified-cla-resweep-08/RUN.md`; results JSON
SHA-256 `b20b7ec1282bb1988f5aaefb025ed71bf359a510f2a8aadf475744a575e066da`.

## 2026-07-17 - Stratified CLA A6 re-sweep batch 07

Ran eight additional uncovered triples across roles4 and roles8 with seeds
109, 113, and 127 and exact controls. Clean OmegaSim `18c7408` and chaoslang
`974af31` identities were verified before measurement. All 144 rows
reconstructed exactly; every grammar had two productions and zero categories.
`(1,.35,5)` and `(2,.15,5)` reached exploratory 4/6 joint matched-control
wins, but neither met the grammar-priority rule. Successful batches now cover
80/120 roles-specific cells. Provenance:
`experiments/20260718T024700Z-a6-stratified-cla-resweep-07/RUN.md`; results JSON
SHA-256 `7d10a63dec8d86f675693eb5e18d0424a2a0ed55a89beaa103af6561797b1bf5`.

## 2026-07-17 - Stratified CLA A6 re-sweep batch 04

Ran eight additional uncovered triples across roles4 and roles8 with seeds
109, 113, and 127 and exact controls. Clean OmegaSim `18c7408` and chaoslang
`974af31` identities were verified before measurement. All 144 rows
reconstructed exactly; every grammar had two productions and zero categories.
`(5,.80,3)` reached 6/6 and `(2,.15,3)` reached 5/6 exploratory joint
matched-control wins, but neither met the grammar-priority rule. Batches 01--04
now cover 64/120 roles-specific cells. Provenance:
`experiments/20260717T224500Z-a6-stratified-cla-resweep-04/RUN.md`; results JSON
SHA-256 `6a26b04b5b18fa061036eba8b490870718823b2dbb5ac87fd5aab2999111b9e8`.

## 2026-07-17 - Stratified CLA A6 re-sweep batch 03

Ran eight additional uncovered gain/coupling/delay triples across roles4 and
roles8 with seeds 109, 113, and 127 and exact appraisal/linear/shuffled
controls. The pinned clean OmegaSim `18c7408` and chaoslang `974af31`
identities were verified before measurement. All 144 rows reconstructed
exactly; every grammar had one or two productions and zero categories. Two
triples, `(1,.35,1)` and `(2,.60,1)`, reached exploratory 4/6 joint
matched-control wins, but neither met the grammar-priority rule. Batches
01--03 now cover 48/120 roles-specific cells and continue the informative
negative grammar result without detector changes. Provenance:
`experiments/20260717T204500Z-a6-stratified-cla-resweep-03/RUN.md`; results JSON
SHA-256 `0eeeedb4eae03806f5c7136e7a5b960d964ccbea9decf0bf7e74a63c25596a28`.

## 2026-07-17 - Stratified CLA A6 re-sweep batch 02

Ran eight additional uncovered gain/coupling/delay triples across both roles4
and roles8 with seeds 109, 113, and 127 and exact appraisal/linear/shuffled
controls. The frozen clean OmegaSim `18c7408` and chaoslang `974af31` identities
were verified before measurement. All 144 rows reconstructed exactly; every
grammar had two productions and zero categories. No triple exceeded 1/6 joint
matched-control wins. This expands batches 01--02 to 32/120 roles-specific
grid cells and strengthens the informative negative grammar result without
changing the detector. Provenance:
`experiments/20260717T184500Z-a6-stratified-cla-resweep-02/RUN.md`; results JSON
SHA-256 `268d165f303150639ccc3e64b520b758ae2f4d7ee720a90ffb6c1498207716cf`.

## 2026-07-01 - Project reboot from ProtomegaTron A6 recommendation

Ben asked Protocosmobot/ZeroBot to get OmegaSim going again along ProtomegaTron's suggested direction. Durable prior context says the next simulation should not add generic logistic chaos. Instead, logistic/sigmoid response should be used as bounded thresholded cognitive appraisal over latent motivation, artifact readiness, fatigue/overload, adaptive thresholds, trust/provenance debt, risk, and prediction error.

Implemented first local A6 prototype as a single-hive role-coupled motivational/appraisal model:

- roles: explore, synthesize, review, maintain;
- state: role motivation, fatigue, adaptive thresholds, artifact maturity, provenance debt, risk, prediction error;
- nonlinearities: sigmoid appraisals and softmax action selection;
- history dependence: delayed role coupling, fatigue/recovery, hysteresis, adaptive thresholds;
- controls: linear appraisal and shuffled utilities;
- first metrics: boundedness, role-switch rate, role entropy, short-period tail detection, artifact/risk tail summaries, macro-role tail strings.

This is a harness/proof-of-motion, not yet a strong scientific result.

## 2026-07-01 - A6 functional candidate gate

Added `docs/a6_functional_candidate_gate.md` to preregister stricter candidate criteria before denser sweeps. The gate requires boundedness, nonperiodic macro-role tail, moderate/high entropy, nontrivial switching, artifact tail movement, combined artifact/debt/risk/prediction-error tail movement, and non-collapsed risk.

Reran the 243-condition smoke sweep with the new metrics. Results: appraisal 24/81 functional candidates, linear 37/81, shuffled 2/81. This usefully suppresses shuffled role-noise false positives, but because linear controls still pass more often than appraisal, the result remains fail-closed for appraisal-specific or attractor-like claims. Next technical step is matched excess-over-control scoring.

## 2026-07-02 - Collective-intelligence experiment loop

Ben requested a new operating mode for OmegaSim: after each experiment run, avoid stalling until a human prompt. Instead, use a rolling collective-intelligence loop where Protocosmobot posts a summary report, ProtomegaTron and Protocosmobot discuss next experiments for a bounded few turns, and Protocosmobot gives the next OmegaSim subagent mandate.

The loop's long-horizon goal is to find configurations of simulated OmegaHive agents or multi-OmegaHive communities whose dynamics display relevant strange attractors with complex multilobed grammatical structure. The first mandate under this loop should remain conservative: implement matched excess-over-control scoring for the current A6 harness before making attractor claims or expanding to A7/A8.

## 2026-07-03 - External benchmark directive updated to do both

Ben clarified that OmegaSim should do both external benchmark directions: Mackey-Glass for the closest delayed-coupling analog, and Lorenz-96 for richer high-dimensional/multilobed attractor dynamics. Updated `TASKS.md` and `DECISIONS.md` accordingly. The intended calibration lane is now two-benchmark rather than Mackey-only or Lorenz-only.

## 2026-07-03 - Dedicated bot-bot scheduled-discussion channel created

Ben created **ProtoBots-BotBotChats** for OmegaSim collective-loop bot discussion: `https://web.telegram.org/k/#-5459676079`. Updated the loop protocol and task/decision records to use this dedicated channel for detailed collective-loop discussion between Protocosmobot/ZeroBot and Protomegabot while preserving concise summaries/directives in the main Protobots channel. Continue using ProtoBots-updates / scheduled-updates (`telegram:-1003983157420`) for scheduled/progress updates, except the single daily 7AM Pacific summary stays in main Protobots. Candidate OpenClaw target is `telegram:-5459676079`, pending verification once the relevant bots/session are visible.

## 2026-07-16 - Interim progress worker

Ben requested a dedicated cron lane until ThreadKeeper persistent agents are ready. Created enabled isolated job `f2347407-4c15-42c7-8587-a9f63f939a59` on a staggered two-hour cadence. Its contract prioritizes untouched-seed replication of the predeclared promoted cell, requires the detector commit/hash to be verified before execution, and retains CLA benchmark calibration as a gate on stronger claims.

## 2026-07-16 - Detector provenance repair and untouched replication

Audited the 2026-07-15 discovery ledger and found it pinned only the OmegaSim repository even though the command imported `chaoslang` from a second repository. The committed dependency can be bounded to `974af31`, but its historical dirty state cannot be proven, so the prior 4/5 result is hypothesis-generating only. Recorded the fail-closed audit in `docs/cla_detector_provenance_audit_20260716.md`.

Preregistered and ran a repaired local replication with clean pinned OmegaSim `18c7408` (detector implementation parent `5a6002b`) and detached clean chaoslang `974af31`, untouched seeds `101,103,107,109,113`, exact matched controls, and unchanged thresholds. The confirmatory `roles8` cell met the criterion at 4/5 seed wins; seed 107 missed only the compression-margin comparison to linear control. Evidence and hashes: `experiments/20260716T164500Z-cla-roles8-untouched-replication/RUN.md`. This is bounded proxy replication, not an attractor/grammar claim; Mackey--Glass and Lorenz--96 calibration remain open.

## 2026-07-16 - CLA calibration lane failed closed

The CLA lane completed its first preregistered external calibration at clean local commit `c8e9e917db26499f3ab970642546f71af85fea5e`. Mackey--Glass and Lorenz--96 x0 passed serialization, fact projection, replay, deterministic refit, and exact reconstruction, but frozen CLA total coding was `65,976.621` aggregate bits versus `6,588.443` for the strongest unigram baseline. The result is a coding/calibration null and authorizes no held-out tuning.

This benchmark used a stricter frozen held-out decodable-code path, not OmegaSim's frozen train-fitted-k-means/surrogate-margin/order-2-loss proxy. Therefore it neither invalidates the reproduced OmegaSim proxy difference nor satisfies the requirement to validate that same proxy path on Mackey--Glass and Lorenz--96. OmegaSim remains claim-gated. Coordinate through the CLA lane's next preregistered minimal joint chunk/category diagnostic; do not modify either detector in response to OmegaSim outcomes. Evidence: `../chaos-language-algorithm/experiments/20260716T172310Z-frozen-heldout-calibration-v1/RUN.md`, results SHA-256 `cc128399193d8dfad2a887d1dad5f9f5a177caf3f6e29e51f6dff04a3440cf9c`.

## 2026-07-16 - Untouched replication bitwise replay

The untouched ledger pinned both clean repositories and implementation hashes,
but omitted the experiment-ledger `env.txt` capture. Rather than rewriting the
historical record, ran a separate local replay with OmegaSim `18c7408`, detector
parent `5a6002b`, chaoslang `974af31`, the same five seeds/controls/thresholds,
and a sanitized captured environment. All 45 CSV rows were byte-identical
(SHA-256 `6b7ad6c2edc6e3828be1781e6eb2ff0804b3e13eb492c798e13c40ff39bfe45b`)
and normalized JSON matched exactly. Focused tests passed 8 plus 2 subtests;
compile, clean-tree, hash, and diff gates passed. This supports exact
replayability but is not an independent replication. Record:
`experiments/20260716T204500Z-cla-roles8-bitwise-replay/RUN.md`.

The CLA lane's subsequent frozen synthetic diagnostic classified the current
learner as `greedy_or_representation_blindness`; it does not rescue the held-out
benchmark null. Same-path Mackey--Glass/Lorenz--96 calibration remains open,
and OmegaSim outcomes must not drive detector changes.

## 2026-07-16 - Frozen same-path external calibration

Preregistered the exact OmegaSim proxy path on Mackey--Glass and Lorenz--96
before outcome inspection, pinning clean OmegaSim `18c7408`, detector SHA-256
`29b8283d...`, clean chaoslang `974af31`, and generator SHA-256 `3d9f370c...`.
The ordered trajectories were compared with exact matched joint time-shuffles
across detector seeds `211,223,227,229,233`; no detector or threshold changed.

Both systems passed at 5/5 matched-control wins. All ordered rows were
detector-positive and had both higher compression-margin proxy and lower
held-out order-2 loss than their control. Results JSON SHA-256 is
`6734426f53b472bfa9ea553627e1447cc03df9ec1a8aaf47cd546f7ce19fb7a1`.
This validates temporal-order sensitivity of the frozen proxy and closes the
same-path task. It does not validate the integrators independently, prove
chaos, identify attractors, or establish semantic grammar. The stricter CLA
held-out coding null remains an independent failed gate. Record:
`experiments/20260716T224635Z-cla-same-path-external-calibration/RUN.md`.

## 2026-07-16 - Dynamics exploration concurrent replay repair

The frozen-detector exploration completed once at `00:46:42Z`, but a concurrent
cron invocation had already begun at `00:46:41Z` before that completion became
visible. The second invocation reused all six tight shards and recomputed the
broad balanced phase, overwriting top-level row artifacts. Scientific counts,
promotions, and conclusions matched; `fingerprint_aggregates.json` remained
byte-identical at SHA-256 `3cdc05f1...`. Row hashes changed because the
experiment wrapper emits process results in nondeterministic `as_completed`
order. Recorded the current hashes and loss of the original row files in
`experiments/20260717T000000Z-cla-dynamics-exploration/PROVENANCE_ADDENDUM.md`.
This is reproducibility/provenance repair, not independent evidence. Future
ledgers must enforce exclusive run directories and deterministic row sorting.

## 2026-07-16 - Experiment-ledger exclusivity and canonical ordering repair

Closed the two wrapper defects exposed by the concurrent dynamics replay without
changing the frozen detector or historical artifacts. The shared
`bin/new-experiment` launcher now creates the timestamped run directory with an
atomic, non-`-p` `mkdir` and fails if that exact path already exists, so two
same-second invocations cannot share a ledger. OmegaSim's reusable
`scripts/experiment_wrapper.py` canonicalizes concurrent row results by the
frozen design identity `(sweep, gain, coupling, delay, seed, control, stratum)`
and fails closed on missing or duplicate identities before serialization and
hashing. Regression checks cover a forced same-ID collision, reversed
completion order, duplicate identity, and missing identity fields. Detector
identity was reverified as clean OmegaSim `18c7408`, clean chaoslang `974af31`,
and detector SHA-256 `29b8283df90bc55929e2065650c998b00f676d5e4317a743656ead8e01c66e7c`.

## 2026-07-16 - Frozen identity recheck and independent CLA coding null

The 23:45 PDT progress-worker audit reverified both pinned trees as clean:
OmegaSim `18c7408fe48eeac9e9ec53f18eb5b2d0ed840e2d`, chaoslang
`974af31efaf6e3cc239252f78367d20e657ac45c`, and detector SHA-256
`29b8283df90bc55929e2065650c998b00f676d5e4317a743656ead8e01c66e7c`.
The untouched `roles8` 4/5 result and its byte-identical replay therefore need
no duplicate measurement; rerunning the same seeds would not constitute a new
untouched replication. The corrected focused checks passed: eight frozen
OmegaSim tests, three canonical-row tests, the exclusive-ledger collision
check, `py_compile`, and `git diff --check`.

Conceptual coordination with the independent CLA lane found its newest frozen
complete-code synthetic gate also failed closed: the intended joint move cost
`34,416` versus `34,352` bits (`+64`), classification
`complete_code_rejects_joint`. This does not change the OmegaSim proxy result
or same-path temporal-order calibration, but it reinforces the existing ban on
strong grammar claims and supplies no basis for detector changes from OmegaSim
outcomes. Evidence:
`../chaos-language-algorithm/experiments/20260717T051500Z-generalized-complete-code-gate-v1/RUN.md`.

## 2026-07-17 - Reusable frozen-identity gate

Added `scripts/verify_frozen_identity.py` plus a plain-language identity
contract so future experiment wrappers can fail before measurement on a dirty
or wrong repository or an implementation-hash mismatch. The verifier is
detector-independent and emits ledger-ready JSON; it neither imports nor tunes
CLA. The current pins reverified clean at OmegaSim `18c7408`, chaoslang
`974af31`, and detector SHA-256 `29b8283d...`. This provenance hardening does
not create new scientific evidence. The roles8 untouched replication remains
4/5, same-path benchmark sensitivity remains 5/5 for both systems, and the
independent complete-code/held-out failures continue to gate grammar claims.

The 03:45 PDT follow-up closed a fail-closed reporting edge case: missing or
unreadable repositories/files now return structured JSON mismatch entries
instead of raising before the ledger can capture the refusal. Five focused
tests, `py_compile`, the explicit missing-identity CLI check (exit 1), and
`git diff --check` passed. The full actual identity set also passed: clean
OmegaSim `18c7408fe48eeac9e9ec53f18eb5b2d0ed840e2d`, clean chaoslang
`974af31efaf6e3cc239252f78367d20e657ac45c`, detector `29b8283d...`, A6 model
`2b788fb9...`, chaoslang evaluation `452f5e03...`, and symbolization
`1c53a435...`. This is provenance-only hardening, not another replication or
new scientific evidence.

Verification note: one frozen-suite command omitted both source paths and
failed during import collection; a second command used the correct recorded
`PYTHONPATH` and all eight unchanged OmegaSim tests passed. Two subsequent
workspace-verifier invocations from the nested OmegaSim repository likewise
used root-relative paths and failed before collection/compilation; rerunning
them from the workspace root passed all five tests and `py_compile`. None of
these invocation errors reached measurement or changed an implementation.

## 2026-07-17 - Exact dirty-tree refusal provenance

Hardened the detector-independent identity verifier to include the exact
`git status --porcelain` lines in every readable repository record. A focused
regression test exposed that the shared Git helper used broad whitespace
stripping, which removed the leading index/worktree status column; it now
removes line terminators only. Eight provenance-helper tests and all eight
unchanged frozen OmegaSim tests passed, along with `py_compile`, the full actual
identity gate, and `git diff --check`. The actual pins remain clean OmegaSim
`18c7408`, clean chaoslang `974af31`, detector `29b8283d...`, A6 model
`2b788fb9...`, evaluation `452f5e03...`, and symbolization `1c53a435...`.

No measured rerun or detector change occurred. The untouched roles8 result
remains bounded 4/5 proxy evidence. The CLA lane's indexed synthetic scorer
progress does not revise its failed held-out Mackey--Glass/Lorenz--96 coding
gate, so attractor and semantic-grammar claims remain blocked.

## 2026-07-17 - Identity-test inventory repair and CLA lane recheck

The 07:45 PDT worker audit found a reproducibility mismatch in the written
record: the latest note reported eight frozen-identity helper tests, while the
current test file contained only five. Added three detector-independent
regressions covering a wrong commit, an exact staged-status refusal, and an
exact untracked-file refusal. The helper suite now demonstrably passes eight
tests, and the unchanged frozen OmegaSim suite passes all eight tests from its
recorded repository-root/PYTHONPATH context. An initial workspace-root frozen
suite invocation failed at import collection (`scripts` was not importable);
no identity check or measurement ran in that failed command.

The full identity gate then passed again: clean OmegaSim
`18c7408fe48eeac9e9ec53f18eb5b2d0ed840e2d`, clean chaoslang
`974af31efaf6e3cc239252f78367d20e657ac45c`, detector SHA-256
`29b8283df90bc55929e2065650c998b00f676d5e4317a743656ead8e01c66e7c`,
A6 model `2b788fb9...`, evaluation `452f5e03...`, and symbolization
`1c53a435...`; compilation and `git diff --check` passed.

Conceptual coordination with the independent CLA lane records that the indexed
complete code accepted the intended joint state on its frozen 19-frame
synthetic fixture (`9,760` versus `10,616` bits, delta `-856`) and that the
opt-in learner seam was subsequently unit-validated. These are synthetic
implementation gates only. No attractor suffix was inspected, the stricter
Mackey--Glass/Lorenz--96 held-out coding null remains binding, and no OmegaSim
detector, threshold, measurement, or claim boundary changed.

## 2026-07-17 - A6 stratified CLA re-sweep batch 01

Ran eight previously uncovered cells from the requested 120-cell grid locally
with frozen clean OmegaSim `18c7408`, chaoslang `974af31`, seeds
`101,103,107`, appraisal/linear/shuffled controls, and `core4`/`roles8` CLA
strata. The 144 rows completed in 481.029 seconds and again produced uniformly
trivial grammars: exactly two productions and zero categories. No cell met the
grammar-priority rule. Exploratory joint proxy wins occurred in 5/6
seed/stratum rows for `(2,.15,1)` and `(5,.80,1)`, but this is quantitative
matched-control behavior only. Evidence:
`experiments/20260717T164500Z-a6-stratified-cla-resweep-01/RUN.md`; results JSON
SHA-256 `8f24f7bc832ccb38d468241310fe4a4661cf6e697667faa90243cf8d2b26d89c`.
