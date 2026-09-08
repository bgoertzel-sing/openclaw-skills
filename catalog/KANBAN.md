# Cross-Project Kanban

Scope: all known project notebooks and recurring workers on this Pop!_OS
workspace. Project `TASKS.md` files are authoritative; this board is a compact
index, not a second task ledger.

Last updated: 2026-08-20 00:20 America/Vancouver

## Current execution directive — agent-hive plumbing

Ben's 2026-08-07 priority order supersedes discretionary sequencing of the
research lanes until these operational acceptance gates are genuinely closed:

1. Restore `@Protomegabot` across Telegram and Slack.
2. Prove `@Protomegabot` can autonomously post Telegram PDFs and other approved
   attachments.
3. Make `@Protocosmo2bot` fully operational, including attachment delivery.
4. Roll out the conversation governor to reduce Telegram-channel noise, using
   its staged evidence/approval gates.
5. Enable both bots to launch and manage bounded persistent subagents.

The prospective ASI:Cloud migration and GPU use is explicitly lower priority;
no migration or resource provisioning is authorized by this directive. Project
records remain authoritative for acceptance evidence and any required human
admin exception.

## Active user commitments

Before an unrelated final reply, check this section. If new work preempts an
entry, record the suspension, reason, next command, and resume trigger in the
authoritative project record.

- **RelaLeap V4 / clean-room ePC** — the provenance-explicit V4-1
  implementation remains distinct from a Mesto reproduction. The frozen
  fresh-seed clean-room confirmation completed with a primary WIN: T=4 settled
  ePC beat wall-clock-matched KD on 3/3 seeds, mean gain `+2.629789` nats. The
  separately approved reliability-first PTB/WikiText robustness run then
  failed its frozen primary gate: mean PTB OOD gain was `-1.913576` nats and
  WikiText ID gain was `-1.050625` across three seeds. Artifacts verified and
  the pod was deleted. Semantic frame-oracle v4 and v5 then failed their
  one-use perfect gates; the successor programme has since consumed further
  batteries through v8, which also failed closed (24 valid, 21 deterministic,
  15 exact). The semantic-free Pareto search and larger multi-regime task both
  failed their frozen admission gates. Frame-oracle v10 then failed closed
  (24 schema-valid, 17 paired-deterministic, 12 exact); v11 is sealed and
  unopened after its bounded source audit. The remediation programme completed
  A0, MG-1--MG-8, and M0-R provider-free gates. Ben later broadened C1
  authority to any available machine, but repeated lifecycle-writer races
  created and deleted out-of-envelope pods before readiness or science
  execution. Later retries exposed transfer, runtime-contract,
  dependency-closure, and data-staging defects before science. The final v4
  amendment completed all five C1 seeds at mean 98.2431889% with sample SD
  0.1244180 pp, passed its frozen criteria, verified all return hashes, and
  deleted the pod; provider lists were empty afterward. The v14 successor is
  still sealed and unopened: its sole preregistered model-readiness probe
  terminated `NOT_READY` before server launch because the isolated namespace
  could not raise loopback; zero model loads, requests, or responses occurred,
  and repair/retry is forbidden. None of these later results reverses either
  clean-room result.
  Source: `projects/relaleap/PROJECT.md` and `TASKS.md`.
- **CAROM** — the accepted Fable/Sol E2/E3 ladder and controller-v5 run are
  complete. Ben approved a reliability-first A40 rerun of the frozen GPT-2
  schedule protocol; its checkpoint-evacuation and failure-injection preflight
  remain open. Compiled-channel confirmation and controller guard validation
  also remain open. Source: `projects/carom/TASKS.md`.
- **Causal Fibres ladder** — reduced E1–E5 and CMCP evidence gates have advanced,
  but the typed CMCP information-geometric protocol and E2 dual-substrate
  estimator validation remain open. Source:
  `projects/causal-fibres-ladder/TASKS.md`.
- **HDC × MusicGen** — full-corpus r5 completed Stage 0 on 22 tracks / 66
  minutes, then failed the frozen persistence proxy. Provider-free calibration
  showed that proxy does not test long-range recurrence. Ben approved a
  prospective direct-recurrence gate; local validation passed, and Ben later
  approved a reliability-first A40 run. The checkpoint-evacuation bundle must
  pass locally before launch; r5 remains a terminal failure. Source:
  `projects/hdc-musicgen/PROJECT.md` and `TASKS.md`.
- **HDC–CGCCT transformers** — P0-G1 v2 passed; P1A, three-seed P1B
  calibration, and the reliability-first five-seed P1B confirmation returned
  verified evidence. The pod was deleted. Ben authorized a post-hoc versioned
  contract repair; its deterministic terminal replay passed 31 tests and
  classified P1-G2 `instrument_failed`. The stale continuation lane is closed
  and no further remote compute is required. Source:
  `projects/hdc-cgcct-transformers/PROJECT.md` and `TASKS.md`.
- **OmegaHive conversation governor** — its 24-hour shadow review covered 200
  records. The direct-post seam audit, watchdog-noise policy, and guarded
  shadow/direct-post canary are complete. Ben authorized the narrow E1a egress
  gate on 2026-08-12; implementation, provider-free tests, independent review,
  and a production suppression/control canary remain open. Admission remains
  shadow-only.
  Source: `projects/omegahive-conversation-governor/TASKS.md`.

## Active recurring lanes

These statuses come from the authoritative project records. Their named cron
IDs are not independently visible in the current session-scoped scheduler
listing.

- **ThreadKeeper / OmegaClaw** — recurring work remains active. A bounded
  iterative `worker-executor` is implemented with persistent checkpoints and
  provider-free completion/failure/budget fixtures (34 tests). ProtoCosmo2's
  full-PDF adapter now preserves the supplied 160,374-character extraction
  within explicit bounds (33 focused tests). Protomega's guarded transport
  cutover then passed a fresh human-authored Telegram canary: the sole outer
  receiver completed the addressed turn, durable outbox delivery received a
  Telegram receipt, and Ben confirmed the exact nonce reply. The recorded
  final topology is `legacy=0 outer=1`, watchdog healthy. The shared human
  Telegram Reply-depth repair subsequently passed provider-free review and
  fresh canaries for ProtoCosmo2, Protomega, and Protomega2. The conversational
  Chroma repair then passed its autonomous nine-transaction staging run and
  direct database/isolation proofs for all three identities; production was
  restored with one owner/receiver and a distinct database path per identity.
  The clean-install recovery localized a reproducible fatal signal to the
  Janus/Python logger boundary, and its smallest repair passed 36/36
  network-isolated turns. The current delayed-completion successor binds
  one-shot reply authority to the authenticated origin request and repairs
  detached-descendant rollback; its full provider-free packet and exact-byte
  review passed. A live long-turn reply was delivered exactly once but
  completed in the same iteration, so it did not exercise the delayed path.
  The deterministic later-iteration fixture passed its focused regression but
  failed closed at bound preflight on authoritative-history drift; reconcile
  and re-review it before another live canary. Subsequent provider-free
  hardening binds bounded episode-history reads to the prevalidated child
  device/inode; the replacement regression and 21 focused helper tests pass.
  ProtoCosmo2 and Protomega2 restoration remains staged behind the Protomega
  delayed-completion closure. ThreadKeeper budget and accounting hardening
  (2026-08-19/20) closed `_safe_float` non-finite rejection, `_safe_config_int`
  defense-in-depth, `record()` non-integer token hardening, isinstance
  trust-boundary hardening, and GGB active-frontier root binding, record-size
  bound, and record-type validation; all focused and full provider-free suites
  pass on `agent/threadkeeper-hardening-next`, with no runtime or remote-ref
  change. Separately, the Agentverse structured-return hardening now fails
  closed on malformed or unusable Tavily response shapes; all 79 focused tests
  pass at local commit `85346af`, with no runtime or remote-ref change.
  Source: `projects/omegaclaw/TASKS.md`; cron
  `f0d70a09-ab9f-40b9-ae3d-b7f789e375bf`.
- **petta-memory** — recurring worker active; immutable πPLN charts now require
  a typed policy and tuple-backed selected-packet collection. Subsequent typed
  provenance hardening reached a full 698-test provider-free suite. A separate
  frozen-worktree ProtoCosmo2 handoff verification collected 698 tests but did
  not pass (one failure, one error, eight skips) because the isolated layout
  did not resolve pinned sibling dependencies; normalize those paths before
  accepting the historical clean baseline. Continue reversible πPLN work
  without live promotion claims.
  Source:
  `projects/petta-memory/TASKS.md`; cron
  `4f4e146a-bdf9-4a6e-97da-6484cfe3f81f`.
- **petta-chem** — recurring worker active; generator expansion and constructed
  guidance are frozen. Graph seed 1002 reached its frozen
  `raw-complete-unanalysed` boundary with all 276 receipts mechanically valid.
  The separately reviewed graph-seed 1003 continuation was healthy at the
  latest recorded metadata-only checkpoint: receipts 0--239 were contiguous
  and mechanically valid, row 240 was the sole allowed unreceipted raw pair,
  and the lifecycle remained live without a terminal manifest. No endpoint
  content was inspected; continue metadata-only monitoring to
  `raw-complete-unanalysed`, with no emergence claim.
  Source: `projects/petta-chem/TASKS.md`; cron
  `c008e434-ea10-4d75-b13b-26b922d079ed`.
- **SpecAtom-HS / Plain2Metta** — recurring worker active. Revision 0.2's
  implementation objective is complete: the general semantic-validation
  ladder reached Stage 11 with clean-checkout reproduction, pinned-tool replay,
  live dual-runtime checks, and 749 provider-free tests. PR #3 was subsequently
  merged at `5ce102c` and deployed as one bounded VM2 systemd worker on
  `127.0.0.1:8081`; fresh canaries for all three bundled examples passed. An
  expanded architecture report (30 pages, 12,802 words) was compiled and
  published as draft PR #4 at `f626dfe` on branch
  `agent/publish-expanded-report` (2026-08-19). The next open lane is a
  realistic benchmark suite and explicit parallel-agent dependency plan.
  Source:
  `projects/specatom-hs/TASKS.md`; cron
  `31e85b3b-784f-4b80-ab24-43e7167561b8`.
- **Chaos Language Algorithm** — recurring worker active. Synthetic competence
  is bounded and mixed; E0 failed its frozen redundancy gate and E0b is
  review-blocked. M-D spec amendments and a frozen E5b proposal were
  committed at `1af9f2b` (2026-08-19); repeated revalidations pass all
  frozen hashes and 283/283 discovery. Do not run E0b or promote E1
  without Ben's protocol decision. Source:
  `projects/chaos-language-algorithm/TASKS.md`; cron
  `dce83d32-440a-4a6a-9305-04175f5ca50d`.
- **HDC × MusicGen continuation** — project records retain a local-only worker;
  the prospective direct-recurrence gate is locally validated, and a
  post-commit fail-closed closure audit (2026-08-20 03:31Z local) confirmed
  smoke-r2 remains terminally a no-result; test-hardening commit `eb39c96`
  on `agent/direct-recurrence-stage0-gate` passed 26/26 local tests with
  byte-identical runtime source. The next remote full-corpus run requires a
  new bundle and approval. Source:
  `projects/hdc-musicgen/TASKS.md`;
  cron `4f4897c9-101b-48aa-b438-56a871ac9668`.
- **HDC–CGCCT continuation** — the project record closes this stale execution
  lane after the deterministic contract-v2 terminal replay classified P1-G2
  `instrument_failed`; it must not reopen seeds or provision compute. Source:
  `projects/hdc-cgcct-transformers/TASKS.md`; cron
  `a2c6d1c7-cccb-40fe-af38-f85acdc3c1bc`.
- **Protobots GGB roadmap** — recurring research worker active. Source:
  `projects/omegaclaw/TASKS.md`; cron
  `15d5d56c-d393-4916-9908-ceaab07b6a2d`.
- **OmegaSim** — a progress worker is scheduled, but scientific promotion is
  still gated by validated CLA/equivalent detector evidence. A third closure
  re-confirmation (2026-08-19 21:45 PDT) found no unexplored stratum; pinned
  `18c7408`. Source:
  `projects/omegasim/TASKS.md`; cron
  `f2347407-4c15-42c7-8587-a9f63f939a59`.

## Ready / Next

- **RelaLeap** — C1 is complete: the v4 data-staging amendment passed all five
  frozen seeds, return hashes verified, and the pod was deleted. Keep all
  semantic-gate failures, the clean-room fresh-seed WIN, the robustness
  failure, and Mesto compatibility questions distinct. Frame-oracle v14 Stage
  A remains blocked after its terminal `NOT_READY` readiness probe; v14 stays
  sealed and unopened, with no repair/retry allowed. Frame-oracle v14
  quiescence receipts r68–r76 (2026-08-18/19) recorded no admissible input;
  frozen contract and clean `8108d98` identity matched and sealed contents
  were not read.
  Source: `projects/relaleap/TASKS.md`.
- **CAROM** — independently validate the controller peak-LR guard and repair the
  supplied Oruzi/Exp2–Exp3 probes before using retained checkpoints. Source:
  `projects/carom/TASKS.md`.
- **Causal Fibres ladder** — finish estimator validation before any emergence
  interpretation; retain the BP-residual control on every target-scope run.
  Source: `projects/causal-fibres-ladder/TASKS.md`.
- **OmegaHive conversation governor** — implement the authorized E1a narrow
  deterministic egress gate, then satisfy its review and production canaries;
  admission remains shadow-only. Source:
  `projects/omegahive-conversation-governor/TASKS.md`.
- **Goal Relevance Governor** — the design document is complete; specify the
  minimal JSON graph schema and read-only relevance verdict, then build a
  retrospective replay corpus. Live enforcement remains gated on replay/shadow
  validation and Ben's explicit approval. Source:
  `projects/goal-relevance-governor/TASKS.md`.
- **petta-chem** — monitor the authorized graph-seed 1003 continuation by
  metadata only until its terminal `raw-complete-unanalysed` boundary; preserve
  seed 1002 unanalysed and do not inspect endpoints.
  Source: `projects/petta-chem/TASKS.md`.
- **Morkql** — add schemas/arity/range checks, typed lowering, and differential
  runtime tests against pinned MORK/PathMap. Source: `projects/morkql/TASKS.md`.
- **ProtoMegaBot2** — finish the provider-free finite Iter harness for
  receive/tool/send plus crash/restart replay before any cutover. Its separate
  autonomous PDF staging acceptance remains open after the last bot-authored
  canary produced no correlated ingress or reply. Production ProtoMegaBot
  remains untouched. Source:
  `projects/protomegabot2/TASKS.md`.
- **Remote job bootstrap** — redesign the observable startup/logging seam,
  propose a fresh bounded envelope, and wait for approval after the initial
  probe and debugging sequence returned no archive and exceeded its envelope.
  Source: `projects/remote-job-bootstrap/TASKS.md`.
- **HDPC Tiny Shakespeare** — first establish strict local T=2 energy descent,
  then prepare a separately approved bounded GPU pilot. Source:
  `projects/hdpc-tiny-shakespeare/TASKS.md`.
- **Hyperseed formalizations** — draft the SLT-guided residual-seeds note and
  continue the Substack/formalization background queue. Source:
  `projects/hyperseed-formalizations/TASKS.md`.
- **Agent recovery** — maintain daily backups and perform the first-Saturday
  restore-smoke cadence. Source: `projects/agent-recovery/TASKS.md`.
- **OpenClaw intent-model router** — continue its project-local active tasks;
  it is also the current integration seam for the OmegaHive governor. Source:
  `projects/openclaw-intent-model-router/TASKS.md`.
- **OmegaSelf** — continue project-local evidence/governance integration gates;
  native loop claims remain contingent on executable runtime evidence. Source:
  `projects/omegaself/TASKS.md`.
- **Pop!_OS proto-hive migration** — Ben redirected the active reconstruction
  to a single pinned four-agent deployment. The third ProtoCosmo cutover
  window was deferred by Ben on 2026-08-19; the 22:13 PDT local gate re-run
  found VM2 is NOT inert: one `proto-hive` container was running (healthy,
  `activation_markers=0`). A secondary concern: gateway PID 2027818 has
  only 1 direct ESTAB to Telegram (operator expects ≥2). Ben must
  investigate and clean up the VM2 container before the cutover can proceed.
  `--check` and `--arm` remain gated as before; no unattended activation is
  authorized.
  Source:
  `projects/pop-os-vm8-migration/TASKS.md`.

## Blocked / Needs Ben or an external condition

- **HDC × MusicGen reliable direct-recurrence run** — approved within the
  recorded A40 envelope, but blocked on freezing and passing the checkpoint-
  evacuation bundle and provider-free return preflight before launch.
- **CLA E0b / E1** — blocked on Ben's explicit review of the proposed E0b
  protocol amendment; the frozen E0 failure remains binding.
- **Remote bootstrap probe** — blocked on a redesigned observable startup/log
  return seam, a fresh bounded envelope, and explicit approval; this is
  distinct from the completed RelaLeap reliability run.
- **OmegaHive enforcement beyond E1a** — only the narrow E1a egress class is
  authorized; admission suppression, shared topology, and broader production
  activation still require phase-specific evidence and explicit approval.
- **ProtoMegaBot2 live staging** — credential rotation is no longer a blocker;
  bounded preflight, supervisor/path isolation, allowlist, health record, and
  rollback evidence remain open.
- **Plain2Metta / SpecAtom-HS publication** — authoritative public repository
  is `bgoertzel-sing/plain2metta`; internal compiler package/IR remains
  `specatom_hs`. No repository-name or visibility decision is pending.
- **RelaLeap MacBook execution** — prior Mac worktree cleanup remains required
  if that machine is used; local Pop!_OS work is not blocked by it.
- **Protomega attachment acceptance** — Telegram text ingress now has a
  successful guarded outer-receiver canary, but the directive's PDF/approved-
  attachment acceptance test is not evidenced as complete for Protomega.
- **VM8 migration** — the older VM8 endpoint remains blocked by TCP/22 timeout
  and exposed credentials require rotation if reused. The newer explicitly
  authorized VM1-only container migration is distinct and active; production
  cutover remains gated.
- **Proto-hive production cutover** — blocked on Ben running the recorded
  independent-root, read-only ProtoCosmo boundary `--check`; this automation
  context cannot satisfy the required privilege boundary. `--arm` remains
  prohibited outside an attended human-canary window. A 2026-08-19 22:13 PDT
  gate found VM2 not inert (1 running `proto-hive` container,
  `activation_markers=0`); Ben must investigate and clean up before the
  cutover can proceed.

## Operations / scheduler

- **Channel watchdog** — project records report the 15-minute scan active.
  Source: `projects/channel-watchdog/TASKS.md`; cron
  `70cd9d3f-8ed4-4d86-8887-917eb919c6b9`.
- **Agent recovery backup** — project records retain the daily backup cron;
  failure-alert routing was verified, and the one-day-late 2026-08-02 monthly
  restore drill passed both repositories. The four non-blocking documentation
  findings were closed at commit `adb1013` on 2026-08-06. Source:
  `projects/agent-recovery/TASKS.md`.
- **Daily Kanban refresh** — active on cron
  `6823e68e-3545-4f52-950b-03cb8a79298d`; this is the only job visible in the
  current session-scoped scheduler listing checked 2026-08-20; its prior run
  was reported `ok`.
- Scheduler/session visibility is scoped. Absence from one session listing is
  not evidence that no worker ran; use project records and cron state together.

## Paused / completed / background

- **OmegaSim scientific programme** — paused/gated as described above even
  though a maintenance worker exists.
- **OpenClaw smoke** — completed. Source: `projects/openclaw-smoke/TASKS.md`.
- **OpenClaw–OmegaClaw replication kit** — packaged/background; the remote-host
  provisioning guide and staged multi-agent port runbook are complete, while
  private-kit review and selection of a fresh-host tester remain open. Source:
  `projects/openclaw-omegaclaw-replication-kit/TASKS.md`.
- **HDC–CGCCT original P0-G1 fixture** — completed as a reproducible ceiling
  failure; the authorized harder v2 grid passed and opened P1.
- **HDC–CGCCT P1B confirmation execution** — completed on five sealed seeds;
  all 160 manifest entries and five artifact digests verified, and the pod was
  deleted. The subsequent explicitly post-hoc contract-v2 replay classified
  P1-G2 `instrument_failed`; the 2026-08-17 terminal integrity checkpoint again
  passed all 31 tests and reproduced the same result hash without reopening
  execution. A 2026-08-19 terminal integrity r39 re-verification again
  passed all 31 tests and reproduced the same result hash; `instrument_failed`
  is unchanged.
- **ProtoCosmo2 post-answer repair** — completed provider-free regressions and
  a fresh production canary: source 858 was acknowledged, a validated captured
  answer survived the subsequent PeTTa exit 1, and exactly one source-bound
  `PC2-HANDOFF-READY` reply was delivered.
- **Three-identity conversational Chroma repair** — completed the autonomous
  nine-transaction staging gate, direct database proof, foreign-query isolation,
  and guarded production restore for Protomega, Protomega2, and ProtoCosmo2.
- **Plain2Metta revision 0.2 implementation and evaluation UI deployment** —
  Stage 11 completed; PR #3 merged and the exact accepted release is active as
  one bounded VM2 worker. The realistic benchmark-suite specification remains
  a separate open task.

## Board hygiene

- Reconcile from `projects/*/TASKS.md` first; use `PROJECT.md`, experiment
  records, current cron state, and visible workers as supporting evidence.
- Never convert a failed or interrupted gate into “running” or “passed.”
- Keep completed history in project records; retain only recent results needed
  to interpret an open lane.
- Do not put credentials, private environment values, or unverified provider
  state on this board.
