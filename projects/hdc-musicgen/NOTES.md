# Working Notes

Use this file for provisional project notes. Add dates and source pointers. Promote durable decisions, results, or tasks to their dedicated files.

## 2026-07-25

- Revision: Ben's structural-memory runbook supersedes the earlier
  context-curve/head-interface design for future execution. The new flow is
  0/S/A/C/D and drops Stage B. RELATED is defined as best older-than-window
  chroma cosine >=0.80, UNRELATED as <=0.50, with the ambiguous middle omitted;
  random controls are sampled only from eligible distant history. This
  explicit detector choice was necessary because the runbook specifies the
  required 0.15 separation gate but not classification cutoffs. Research Rules
  1, 2, 5, and 7 guided the pure-logic tests and modular helper boundaries.
- Observation: focused structural tests pass 6/6 and legacy tests pass 7/7
  under system `python3`; the requested `python` command is unavailable and
  the project `.venv` lacks pytest. No model-dependent stage was run.
- Observation: source audit identifies delay alignment, missing NLL, unsynced
  CUDA timing, track leakage, and hard-coded codec assumptions.
- Inference: locally executable pure-logic tests can validate most repairs even
  if the full MusicGen checkpoint is impractical on CPU.
- Hypothesis: AudioCraft 1.3.0 delay masks can provide the authoritative
  hidden-position-to-target mapping for Stage B.
- Observation: standard AudioCraft 1.3.0 installation failed building PyAV
  because host FFmpeg development libraries are absent. Exact source inspection
  plus 7 pure regression tests passed; see local smoke `RUN.md`.
- Observation: RunPod's official pricing page listed RTX 3090 at about
  USD 0.50/hour when checked; the proposal requires a live-price recheck.

## 2026-07-27 — smoke-r2 NLL-policy handoff (local artifact audit)

- **Observed:** `artifacts/stageA_summary.json` is internally consistent with
  the run record: RELATED has 12 spans, all reported aggregate conditions are
  in the 1.5–6.0 band (window 4.08487, matched 4.01637, random 4.06844,
  full 3.05248), and its relevance gain is 0.052069. UNRELATED has exactly one
  span, with all four conditions below 1.5 (1.26837, 1.24421, 1.24495,
  1.23326) but above the runbook's `<0.5` alignment-bug warning.
- **Observed:** the only UNRELATED span is track index 0, target block 4,
  retrieved block 0, similarity 0.493875; its random-minus-matched gain is
  0.000735. This sample size cannot establish a stratum-wide NLL distribution
  or distinguish an unusually predictable span from a silent scoring defect.
- **Inference:** the frozen wording gives a 1.5–6.0 absolute sanity band and
  explicitly instructs a stop when the Stage-A band cannot be reached after
  FRAGILE-point fixes. It does not define a smoke-only or minimum-support
  exception. Therefore the existing conjunctive fail-closed disposition is the
  only supported current policy; do not launch smoke-r2 or Stages C/D.
- **Decision request (required before paid work):** the decision owner must
  either (a) retain the current conjunctive band, ending this line as a failed
  smoke, or (b) amend the runbook *before execution* to state a minimum
  per-stratum support and how the band applies below it. Any amendment must
  preserve the `<0.5` alignment-bug stop, prohibit Stage D unless the amended
  Stage-A gate passes, and specify a bounded fresh-run provider, resource,
  cost cap, data scope (existing 24 local licensed tracks only), and immediate
  termination/retrieval plan. No remote resource was created or contacted for
  this audit.

## 2026-07-27 — unreachable continuation pod terminated

- **Observed:** the pre-existing RunPod RTX 3090 pod `mkiku77kmu4rf9`
  (`hdc-musicgen-20260726-smoke-r2`, USD 0.50/hour, 30 GB volume) was still
  configured RUNNING but its SSH endpoint `213.192.2.67:40023` refused a fresh
  BatchMode connection (exit 255). It had been created at
  `2026-07-26T15:25:18Z`, and RunPod reported `uptimeSeconds: 0`.
- **Decision (Ben):** if it remained unreachable, terminate it and use a
  replacement rather than retain it.
- **Observed:** `runpodctl pod delete mkiku77kmu4rf9` returned `deleted: true`
  at approximately `2026-07-27T08:47Z`; subsequent `runpodctl pod list`
  returned `[]` and `pod get` returned 404. No experiment command or data
  transfer was performed on this pod, so there are no artifacts to retrieve.
- **Constraint:** a replacement still needs a pre-execution amendment of the
  frozen Stage-A sanity policy and a resource-specific bound; the prior pod's
  four-hour extension does not specify a new pod's resource/time bound.

## 2026-07-27 — local gate replay and decision-ready smoke-r2 request

- **Observed:** replaying `stageA_gate()` from the frozen implementation
  against `experiments/20260726T043220Z-gpu-run/artifacts/stageA_summary.json`
  exactly reproduced `gate_pass: true` and `nll_sanity_pass: false`. The
  implementation collects all four aggregate NLL conditions from both strata
  and applies `all(1.5 <= x <= 6.0)`. The focused pure-logic suite passed
  7/7 (`python3 -m pytest -q test_hdc_musicgen_structural.py`).
- **Inference:** the original structural runbook describes the 1.5–6.0 band
  as “roughly”, but the frozen executable makes it a strict, conjunctive
  aggregate gate. It contains no low-support exception. Thus the existing
  fail-closed result is reproducible locally; changing it requires an
  explicit pre-execution runbook amendment, not a code-only reinterpretation.
- **Proposed amendment for owner decision:** retain the strict 1.5–6.0 rule
  when a stratum has at least 3 spans; below 3 spans, record every condition
  and require all values to be finite, in [0.5, 8.0], and monotone subject to
  the existing <0.02 wiggle allowance, but mark the stratum
  support-insufficient rather than using it to pass the absolute band. Stage A
  may pass only if RELATED has >=3 spans, its relevance gate passes, and no
  eligible stratum triggers the `<0.5` alignment-bug or `>8` broken-
  conditioning stop. Stage D remains forbidden until this amended Stage-A
  gate passes. This is a proposal only; the current strict code/gate remains
  in force.
- **Precise approval request if the amendment is accepted:** authorize one
  fresh RunPod Secure Cloud pod with one RTX 3090 (24 GB), no persistent
  volume/snapshot/endpoint, maximum 4 wall-clock hours, and a USD 3.00 hard
  cap at the previously observed USD 0.50/hour rate (terminate earlier if the
  live quoted rate would exceed the cap). Scope: run only smoke-r2 Stage 0/S/A
  on the existing locally retained 24 explicit-CC MTG-Jamendo tracks, limited
  to 8 tracks and their already-present metadata; no new corpus download,
  no backbone update, no Stage C/D or full run unless separately approved.
  Stop immediately on any failed gate, timeout, or cost-risk; retrieve only
  logs/JSON/checksums, verify them locally, then delete the pod and confirm
  empty list/404. No provider was contacted and no resource was created for
  this request.

## 2026-07-27 — smoke-r2 amendment and replacement approved

- **Decision (Ben):** approved the proposed replacement and policy amendment
  in Telegram message 13726. The executable amendment applies the 1.5--6.0
  NLL band per stratum only at support >=4, retains the unconditional `<0.5`
  alignment-bug stop, and retains the existing `>8` broken-conditioning stop.
  Sparse strata are recorded as support-insufficient.
- **Observed:** focused gate tests passed 8/8 after the change; commit
  `7afd4c4` is the source pin. The unrelated `hdc_musicgen_experiments.py`
  worktree modification was preserved and excluded from this commit.
- **Observed:** `runpodctl doctor` passed, but the 2026-07-27T14:06Z live
  inventory contained no available RTX 3090. No pod was created, no data was
  transferred, and no cost was incurred. The approved run record is
  `experiments/20260727T140304Z-smoke-r2/REMOTE_JOB.md`.

## 2026-07-27 — sparse-stratum non-finite fail-closed audit

- **Observed:** the approved support-aware gate at `7afd4c4` applies the
  1.5--6.0 band only to supported strata and checks `<0.5`/`>8` at all
  support levels. Consequently, a `NaN` NLL in a sparse stratum evaded both
  comparisons and could leave `nll_sanity_pass` true. This conflicts with the
  prior NaN-mask incident and the experiment's requirement for finite NLLs.
- **Action/evidence:** added an explicit `math.isfinite` stop and regression
  test in the local structural implementation. The focused pure-logic suite
  now passes 9/9 (`python3 -m pytest -q repos/test_hdc_musicgen_structural.py`);
  `git diff --check` is clean.
- **Disposition:** this local fail-closed repair is intentionally uncommitted
  and does not alter the approved remote source pin `7afd4c4`. Do not launch
  smoke-r2 with the approved pin until the owner either accepts a new pinned
  source containing this strictly stronger stop or explicitly records why
  non-finite sparse-stratum NLLs may pass. No provider was contacted and no
  resource was created.

## 2026-07-27 — finite-NLL repair accepted for launch

- **Decision (Ben):** message 13770 directs starting an available different
  pod. This accepts pinning the strictly stronger finite-NLL stop (`8907d0f`)
  while retaining the Stage 0/S/A-only, four-hour, USD-3 scope.
- **Observed:** the focused pure-logic suite passed 9/9 before provisioning.

## 2026-07-27 — smoke-r2 local gate replay under approved amendment

- **Observed:** without contacting the already-recorded remote pod, replayed
  `stageA_gate()` from pinned source `8907d0f` against the retrieved smoke-r1
  `stageA_summary.json` (excluding its historical stored `gate` field, which
  is not an input to the function). The focused suite passed 9/9 and the
  replay returned `gate_pass=true`, `nll_sanity_pass=true`, checked stratum
  `[related]`, support-insufficient stratum `[unrelated]`, and both
  `nll_nonfinite_stop=false` and `nll_alignment_bug_stop=false`.
- **Inference:** the accepted support-aware policy has the intended, narrow
  effect on the known smoke-r1 evidence: it preserves the RELATED relevance
  and ordinary NLL-band requirements, records rather than waives the lone
  UNRELATED stratum, and does not suppress the finite-NLL or `<0.5` stops.
  This validates policy mechanics only; it is not smoke-r2 execution evidence.
- **Constraint:** this continuation worker neither connected to nor retained,
  resumed, created, or otherwise acted on any remote resource. The current
  remote handoff must still retrieve, verify, and terminate under its separate
  approved procedure; do not infer completion from this local replay.

## 2026-07-27 — smoke-r2 input-scope handoff audit (local only)

- **Observed:** source `8907d0f` finds audio separately by extension, sorts
  each extension list, concatenates them in WAV/MP3/FLAC/OGG order, then takes
  `files[:limit]`. The retained corpus described in the handoff is MP3-only;
  therefore its approved `--limit 8` selection is deterministic: tracks
  `0000382`, `0000387`, `0000759`, `0000760`, `0000761`, `0000762`, `0000764`,
  and `0000765`. The prior retrieved manifest gives 2,098.468 measured seconds
  for these files and selection-record SHA-256
  `60183005efa4dd7b8864bdbf7c24dae7667e563f20fb6d78f5e1c293a86e27e3`, where
  each record is `local_file<TAB>audio_sha256<LF>` in lexical order.
- **Action/evidence:** `python3 -m pytest -q repos/test_hdc_musicgen_structural.py`
  passed 9/9 after the audit. The smoke-r2 handoff now requires retrieved
  Stage-0 evidence to identify and hash-check the selected inputs; `--limit 8`
  alone is insufficient if the remote directory contents/extensions differ.
- **Constraint:** this was a manifest/code audit only. No provider was
  contacted; no remote resource was created, resumed, retained, or connected.

## 2026-07-28 — terminal handoff reconciliation (local only)

- **Observed:** `REMOTE_JOB.md` records that pod `vbu5r47gstyl16` was deleted
  after two refused SSH connections, followed by an empty pod list and 404
  lookup. No Stage 0/S/A command, transfer, GPU work, or stage artifacts
  occurred. `RUN.md` had retained a stale “remote setup in progress” status;
  it now records the terminal, no-artifact disposition.
- **Action/evidence:** `python3 -m pytest -q repos/test_hdc_musicgen_structural.py`
  passed 9/9 at source pin `8907d0f`; `git -C repos diff --check` was clean.
  The unrelated pre-existing modification to `hdc_musicgen_experiments.py`
  remains untouched.
- **Constraint:** no provider was contacted and no remote resource was
  created, resumed, retained, or connected. Any replacement requires a new
  explicit authorization with provider, resource, cost, data scope, and stop
  plan; the old approval cannot be used to resume this deleted pod.

## 2026-07-28 — smoke-r2 replacement-status contradiction (local only)

- **Observed:** `experiments/20260727T140304Z-smoke-r2/RUN.md` and the
  preceding cleanup record establish that `vbu5r47gstyl16` was deleted before
  execution. However, the same run's `REMOTE_JOB.md` subsequently records a
  distinct replacement, `2jh6oxjzogdexe`, as provisioned at 2026-07-28T04:32Z
  and awaiting a usable SSH route; it contains no deletion, empty-list, 404,
  transfer, or stage-result record for that pod. Thus the local handoff cannot
  establish that no later paid resource remains, and the RUN's terminal status
  applies only to the earlier pod.
- **Action/evidence:** at pinned source `8907d0f`, `python3 -m pytest -q
  repos/test_hdc_musicgen_structural.py` passed 9/9 and `git -C repos diff
  --check` was clean. No provider command, network connection, or remote
  action was taken; the pre-existing unrelated worktree modification remains
  untouched.
- **Fail-closed disposition:** do not interpret the smoke-r2 handoff as
  complete and do not provision, resume, connect to, or retain any resource.
  The conflict blocks both smoke-r2 acceptance and any fresh launch.
- **Precise approval request required to resolve the handoff:** authorize a
  one-time RunPod Secure Cloud *status-and-cleanup-only* action for exact pod
  `2jh6oxjzogdexe`: query its status, and if it exists, immediately delete it;
  do not SSH, transfer data, install software, run a stage command, create a
  replacement, attach storage, or create an endpoint/snapshot. Data scope is
  provider metadata only (no audio or corpus data). Cost allowance is USD 0
  for new spend; stop after status plus deletion/empty-list/404 evidence and
  record the result locally. A new experiment would still require separate
  provider/resource/cost/data/stop authorization.

## 2026-07-28 — smoke-r2 no-artifact gate revalidation (local only)

- **Observed:** at pinned source `8907d0f`, `python3 -m pytest -q
  repos/test_hdc_musicgen_structural.py` passed 9/9 in 0.77 seconds and
  `git -C repos diff --check` was clean. The smoke-r2 run directory has no
  `artifacts/` directory, so it holds no retrieved logs, manifests, checksums,
  or Stage 0/S/A result JSON for replacement `2jh6oxjzogdexe`.
- **Inference:** the local record supports neither execution nor cleanup of
  that replacement. Passing pure-logic tests validates the source pin only;
  it cannot establish the provider resource's state. The handoff remains
  fail-closed.
- **Constraint:** no provider command, network connection, or remote action
  was taken. The outstanding approval request is unchanged: one-time RunPod
  metadata-only status query for exact pod `2jh6oxjzogdexe`, followed by
  immediate deletion if present, with no SSH, data transfer, setup, stage
  command, replacement, storage, endpoint, or snapshot; data scope provider
  metadata only, USD 0 new-spend allowance, and stop after
  status+deletion/empty-list/404 evidence. A separate authorization would be
  required for any experiment.

## 2026-07-28 — smoke-r2 terminal-state reconciliation (local only)

- **Observed:** the later terminal section of `experiments/20260727T140304Z-smoke-r2/REMOTE_JOB.md` resolves the preceding replacement-status contradiction: under Ben's explicit authorization, replacement `2jh6oxjzogdexe` was RUNNING at USD 0.50/hour immediately before `runpodctl pod delete` returned `deleted: true`; a subsequent account-wide `pod list --all` omitted it. Along with the earlier deleted pod `vbu5r47gstyl16`, both smoke-r2 pods were terminated before any transfer, dependency installation, Stage 0/S/A command, or artifact creation.
- **Action/evidence:** at source pin `8907d0f`, `python3 -m pytest -q test_hdc_musicgen_structural.py` passed 9/9 in 0.75 s; `git diff --check` was clean; and `experiments/20260727T140304Z-smoke-r2/artifacts/` is absent. The existing unrelated worktree modification to `hdc_musicgen_experiments.py` was not changed.
- **Disposition:** smoke-r2 has no experiment result to accept. The status-and-cleanup-only blocker is resolved, but no paid resource may be created, resumed, retained, or contacted under this local worker. A future launch requires fresh explicit approval naming the provider, exact GPU resource, current price and hard cost/time cap, the existing eight explicit-CC tracks only, and immediate gate-failure/retrieval/termination stops.

## 2026-07-28 — smoke-r3 launcher handoff audit (local only)

- **Observed:** the currently recorded smoke-r3 launcher
  `experiments/20260728T190400Z-smoke-r3/remote_run.sh` sets
  `OUT=/workspace/hdc-musicgen-r3-results` and, under `set -euo pipefail`,
  redirects the environment probe to `"$OUT/environment.txt"` before any
  `mkdir -p "$OUT"`. The script contains no output-directory creation. Unless
  setup already created that exact directory, Bash stops at the redirection
  before Stage 0, so Stage 0/S/A and checksums cannot run. The local pinned
  gate suite passed 9/9 in 0.88 s and `git -C repos diff --check` was clean.
- **Inference:** the local record cannot establish whether remote setup created
  the directory, and it contains no retrieved r3 logs or artifacts. Do not
  infer execution, completion, or termination from the recorded tmux start;
  require `environment.txt`, logs, Stage 0/S/A JSON, selected-input hashes,
  and checksums before accepting a result.
- **Fail-closed disposition:** no provider command, network connection, remote
  change, or resource action occurred. Any owner-authorized recovery must
  verify the exact directory and add `mkdir -p "$OUT"` before the first
  redirection, then follow the existing retrieval/termination stop plan; it
  authorizes no new data, stages, or retries.
