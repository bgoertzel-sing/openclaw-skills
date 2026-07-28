# Tasks

Use small, testable tasks. Keep the top of each section in priority order.

## Now

- [ ] Re-provision and execute smoke-r2 only after a fresh availability/cost
  check and a reachable pod. The prior RTX 3090 pod `vbu5r47gstyl16` was
  terminated on 2026-07-28 after SSH refused twice, before any stage command
  began; provider list was empty and lookup was 404. Acceptance: only eight
  existing explicit-CC tracks run through Stages 0/S/A; retrieve and verify
  artifacts, then terminate the pod. Next command: `runpodctl gpu list`.
  Evidence:
  `experiments/20260727T140304Z-smoke-r2/REMOTE_JOB.md`.
- [ ] Persistent local-only continuation worker: inspect and validate the
  smoke-r2 handoff, reproduce or analyze locally where possible, and prepare a
  bounded decision note. It must not create, resume, or retain paid remote
  compute without a new explicit approval. Acceptance: each tick records an
  evidence-backed next action or a precise approval request in the project
  record. Scheduler lane: `HDC MusicGen continuation worker`. Latest evidence
  (2026-07-27): local JSON audit reconfirmed the NLL failure is confined to one
  UNRELATED span (all four values 1.23326–1.26837; n=1), while RELATED (n=12)
  is in-band and passes relevance. The frozen runbook has no small-stratum
  exception; gate remains fail-closed. Latest evidence (2026-07-27): a local
  replay of the frozen `stageA_gate()` exactly reproduced `gate_pass=true` but
  `nll_sanity_pass=false`; focused pure-logic tests passed 7/7. The runbook's
  “roughly” wording cannot override the executable's strict all-aggregate
  band without an owner amendment. Latest evidence (2026-07-27): the approved
  low-support amendment at `7afd4c4` lets a non-finite sparse-stratum NLL
  evade its numeric stops; a local uncommitted fail-closed repair and
  regression pass 9/9. The remote source pin must be updated/accepted before
  smoke-r2 can launch. Latest evidence (2026-07-27): local replay of the
  accepted `8907d0f` gate against the retrieved smoke-r1 summary passed the
  9/9 focused suite and yields a passing NLL sanity result only because
  RELATED (n=12) is checked and UNRELATED (n=1) is explicitly reported
  support-insufficient; both non-finite and `<0.5` stops remain false. No
  remote resource was contacted by this worker. Latest evidence (2026-07-27):
  local source/manifest audit identifies the deterministic MP3-only `--limit
  8` selection and its selection-record SHA-256
  `60183005efa4dd7b8864bdbf7c24dae7667e563f20fb6d78f5e1c293a86e27e3`;
  focused gate tests pass 9/9. Retrieved Stage-0 evidence must verify these
  inputs before smoke-r2 can be accepted. See `NOTES.md` for the bounded
  handoff. Latest evidence (2026-07-28): documentation reconciliation confirms
  `vbu5r47gstyl16` was deleted after two SSH refusals, with empty-list/404
  cleanup evidence and no stage artifacts; pinned-source focused tests pass
  9/9 locally and `git diff --check` is clean. This worker did not contact a
  provider or alter the pre-existing unrelated worktree modification. Latest
  evidence (2026-07-28): the same remote handoff also records a later pod
  `2jh6oxjzogdexe` as provisioned but lacks a terminal status, while the
  project RUN describes only the deleted earlier pod. Local pin `8907d0f`
  focused tests again passed 9/9 and `git diff --check` was clean. Treat the
  replacement's status as unverified and block all remote action pending a
  fresh explicit status/cleanup authorization; see `NOTES.md`.
  Latest evidence (2026-07-28): the pinned gate suite passed 9/9 locally,
  `git diff --check` was clean, and the smoke-r2 run directory contains no
  retrieved artifacts. This reconfirms that `2jh6oxjzogdexe` has no local
  execution or retrieval evidence; do not contact it without the precise
  status-and-cleanup authorization in `NOTES.md`.
  Latest evidence (2026-07-28): Ben supplied that authorization; account
  metadata showed `2jh6oxjzogdexe` RUNNING at USD 0.50/hour immediately before
  `runpodctl pod delete` returned `deleted: true`, and a subsequent all-pods
  list omitted it. No remote execution/artifact evidence exists. The old
  status/cleanup blocker is resolved; a fresh MusicGen launch still requires
  its separately recorded availability/cost/reachability check.
  Latest evidence (2026-07-28): local terminal-state reconciliation against
  `REMOTE_JOB.md` confirms both smoke-r2 pods were deleted before any Stage
  0/S/A command: `vbu5r47gstyl16` after SSH refusal and `2jh6oxjzogdexe` after
  unusable provider routing. At pin `8907d0f`, focused fail-closed tests pass
  9/9 in 0.75 s, `git diff --check` is clean, and this run has no retrieved
  `artifacts/` directory. No provider was contacted. A future launch needs a
  new explicit authorization naming RunPod (or another provider), exact GPU,
  current price and hard cost/time cap, the existing eight explicit-CC tracks
  only, and immediate gate-failure/retrieval/termination stops.
  Latest evidence (2026-07-28): static local audit of the later smoke-r3
  handoff found `remote_run.sh` redirects to
  `/workspace/hdc-musicgen-r3-results/environment.txt` before creating that
  directory (and has no `mkdir -p`); with `set -euo pipefail`, this is a
  pre-Stage-0 failure unless setup already created it. Gate tests at pin
  `8907d0f` pass 9/9 (0.88 s), but no local smoke-r3 artifacts exist. Treat
  r3 results as unverified; require logs, `environment.txt`, Stage-0/S/A JSON,
  selected-input hashes, and checksums before acceptance. No provider contact
  or remote change occurred in this worker.
- [x] Prepare a replacement RunPod proposal for the 8-track full-length
  smoke-r2, including a runbook amendment for the one-span smoke NLL policy.
  The attempted continuation pod `mkiku77kmu4rf9` was unreachable (SSH
  refused) and terminated at 2026-07-27T08:47Z; RunPod then returned an empty
  pod list and 404 for the ID. Acceptance: an explicit amended gate and fresh
  provider/resource/time/cost approval are recorded before provisioning.
  Owner approval recorded 2026-07-27; live RTX 3090 availability remains the
  only provisioning blocker. Evidence:
  `experiments/20260727T140304Z-smoke-r2/REMOTE_JOB.md`.
- [ ] Decide whether a future run may revise or waive the smoke-only absolute
  NLL sanity policy. Acceptance: an explicit decision preserves or amends the
  gate before any new paid resource is created. Next command: review
  `experiments/20260726T043220Z-gpu-run/RUN.md`. Evidence: smoke RELATED NLL
  was in-band, while the sole UNRELATED span scored 1.24–1.27 nats/token.
  Local handoff (2026-07-27): choose either retain the conjunctive band (no
  new run) or amend the frozen runbook before any paid work with a minimum
  per-stratum support rule, unchanged `<0.5` bug stop, and a new bounded
  provider/resource/cost/data/termination authorization; `NOTES.md` records
  the exact source values.

## Next

- [ ] After approval only, download the selected license-clean ≥20-track set.

## Waiting or blocked

- [ ]

## Someday or exploratory

- [ ]

## Done recently

Move durable conclusions into `PROJECT.md`, `DECISIONS.md`, or experiment results rather than relying on this list.

- [x] Executed the approved frozen GPU job fail-closed through smoke Stage A:
  prepared 24 license-explicit tracks, passed Stage S separation, stopped on
  the absolute-NLL sanity gate, retrieved and hashed all partial artifacts,
  and terminated the RunPod pod with empty-list/404 confirmation
  (2026-07-26). Evidence:
  `experiments/20260726T043220Z-gpu-run/RUN.md`.
- [x] Implemented Ben's structural-memory runbook as a new 0/S/A/C/D script,
  copied the authoritative runbook, added six focused tests, retained seven
  passing legacy tests, and updated project/run records (2026-07-25). Evidence:
  `experiments/20260725T-structural-rewrite/RUN.md`.
- [x] Prepared fixed code, 7 regression tests, four deterministic WAV
  fixtures, documented partial local smoke, and frozen remote proposal at
  commit `59eade2` (2026-07-25).
- [x] Ben explicitly approved RunPod RTX 3090 execution with an 18-hour
  timeout and USD 25 hard cap (2026-07-26). Evidence:
  `experiments/20260726T043220Z-gpu-run/REMOTE_JOB.md`.
