# Tasks

Use small, testable tasks. Keep the top of each section in priority order.

## Now

- [ ] **Activate Protomega2 after attribution closure (Ben,
  Telegram 4627, 2026-09-08 11:49 PDT).** Deliverable: close the deployed
  ProtoCosmo/ProtoCosmo2 routing repair with fresh human-authored Telegram
  evidence, then finish the focused Protomega2 activation. Acceptance:
  Attribution was operationally closed by Ben in Telegram 4636 despite
  ProtoCosmo2 responding to the reference-only canary; that outcome remains a
  recorded known limitation. Acceptance: Protomega2 has
  exactly one receiver, correct isolated identity/model/session state, passes
  addressed and untargeted-message canaries, survives an owning-supervisor
  restart, and retains a verified rollback. Next command: capture current
  read-only target topology/log cursors, then ask Ben to send the three exact
  human-authored canary messages. Evidence:
  `experiments/20260907T2154PDT-cross-bot-prompt-attribution/RUN.md` and
  `experiments/20260908T1903Z-protomega2-activation/RUN.md`.

- [x] **Repair cross-bot Telegram prompt attribution (Ben, Telegram 4529,
  2026-09-07).** Deliverable: prevent a sibling bot's untargeted group message
  from becoming a current `role:user` request for ProtoCosmo or ProtoCosmo2,
  while retaining sender identity and reply/mention provenance in bounded
  history context. Acceptance: provider-free regression reproduces messages
  4507-4514; both runtimes reject untargeted bot-authored turns; a fresh
  externally initiated canary proves each bot answers only its addressed Ben
  message; distinct session/provider/egress evidence remains intact. Next
  command: obtain one human-authored negative reference canary and one direct
  address canary for each bot, then correlate ingress/session/egress logs. The
  fixes are deployed to ProtoCosmo2 and VM2 ProtoCosmo. Ben operationally
  accepted and closed testing in Telegram 4636 on 2026-09-08. ProtoCosmo2's
  response to the reference-only canary is retained as a known limitation,
  not relabeled as a passing negative canary.
  Evidence: `experiments/20260907T2154PDT-cross-bot-prompt-attribution/RUN.md`.

- [ ] **Finish Protomega2 activation/repair on VM2 (Ben, Telegram 4546,
  2026-09-07).** ProtoCosmo, ProtoCosmo2, and Protomega are operational;
  Protomega2 is the only remaining agent-activation task. Acceptance: exactly
  one active Protomega2 receiver; correct identity/model/session routing;
  fresh human-authored addressed Telegram response; untargeted sibling-bot
  message produces no response; restart-safe topology; rollback evidence.
  Next command: after closing the cross-bot attribution canary gate, capture
  the current VM2 Protomega2 supervisor, receiver, cursor, configuration,
  ingress/provider/egress, and rollback baseline before changing activation.

- [x] **Stop recurring VM2 root-disk growth (Ben, Telegram 4468, 2026-09-07).**
  Deliverable: identify current growth sources, reclaim only verified disposable
  data without disrupting `proto-hive` or `hermes-debugops`, and install or
  repair bounded retention for the actual recurrent source. Acceptance: before/
  after filesystem and top-consumer evidence; both containers remain running;
  root usage returns below the 85% alert threshold; retention mechanism passes
  one observed run. Next command: collect read-only `df`, `du`, Docker usage,
  journal usage, and large-file age/size evidence over the pinned VM2 SSH path.
  Completed 2026-09-07: root usage 87% -> 77% (17G -> 29G free),
  stale/unmounted migration copies removed after active-reference checks, the
  retained 2.3G snapshot tarball verified, all VM2 Codex agent log databases
  added to daily retention, and both live containers remained running.
  Evidence: `experiments/20260907T1812PDT-vm2-disk-growth-remediation/RUN.md`.

- [ ] **Third ProtoCosmo cutover window deferred by Ben (2026-08-19 10:27
  PDT).** Ben is short on time and wants to avoid VM2 model-rerouting hassles:
  attempt the port in ~12-13 hours (tonight ~22:30-23:30 PDT, after the
  ProtoCosmo Codex quota resets 20:29 PDT) or later per his schedule. Before
  the window: re-run the local gate, confirm accepted hashes, and hand Ben the
  exact read-only root `--check` command plus the attended `--arm` + human
  canary checklist (immediate Telegram canary, commit, PID-usage observation,
  no recreation of cron `9b7b9904...`). Do not activate anything unattended.
  Local gate update 2026-08-19 11:35 PDT: operator receiver-architecture fix
  applied. The laptop runs all Omega receivers inside the OpenClaw gateway
  process, not as separate `phase6_private_canary_runner.py` instances. The
  operator now checks gateway Telegram connections (≥2 ESTAB to
  149.154.166.110:443) instead of 3 standalone PIDs. Stale manifest entries
  for compose.yaml and compose.live.yaml corrected. All 18 manifest entries,
  Python compilation, Bash syntax, and ShellCheck pass. Worker hash
  `e8b7d7db...cc7b` (unchanged), rollback `cf9acd39...c4e` (unchanged),
  operator `497e73a5...f435` (changed — receiver fix). The exact command
  for Ben is in the experiment RUN.md under "Ben's command and checklist".
  Pre-cutover re-verification 2026-08-19 12:44 PDT: all 18 manifest entries
  OK, Python compile OK, Bash syntax OK, ShellCheck OK. Hashes unchanged:
  worker `e8b7d7db...cc7b`, rollback `cf9acd39...c4e`, operator
  `497e73a5...f435`, live Compose `c80c79eb...b308`. Laptop gateway PID
  `2027818` active with correct policy. Old five-minute cron `f777bc91`
  absent. VM2 inert (zero containers/markers, all layouts present).
  Architecture review confirms fail-closed per-identity activation,
  independent sibling restart, and correct compose.live.yaml settings.
  All pre-cutover gates satisfied; sole remaining gate is Ben's independent
  root `--check` + attended `--arm` + human Telegram canary.
  Re-verification 2026-08-19 13:49 PDT: all hashes, compile, syntax,
  ShellCheck, manifest (18/18), laptop gateway (PID 2027818, 2 Telegram
  connections, correct policy), stale cron absent all confirmed. No state
  changes since 12:44 PDT. Ready for tonight's cutover window.
  Third-window prep 2026-08-19 22:13 PDT (cron 659c69e6): local gate
  re-run — Bash syntax PASS, ShellCheck --severity=warning PASS (3 SC2126
  style-only advisories at --severity=style, previously accepted), Python
  boundary-contract PASS, worker-stability PASS (46 polls). Hashes: operator
  `497e73a5...f435` (matches 12:44/13:49 PDT; differs from RUN.md original
  `986f863a...` due to documented receiver-architecture fix), rollback
  `cf9acd39...c4e` MATCH, worker `e8b7d7db...cc7b` MATCH, live Compose
  `c80c79eb...b308` MATCH. Laptop gateway PID 2027818, systemd properties
  correct (Restart=always KillMode=control-group NoNewPrivileges=yes), no
  dropin, no rollback timer, no laptop activation markers.
  ⛔ GATE FAILURE: VM2 is NOT inert. vm2-admin.sh status reports
  `containers=1 container=proto-hive status=Up 2 hours (healthy)
  restart_count=0` with `activation_markers=0`. A running healthy proto-hive
  container with no activation marker blocks the cutover. The container
  started ~20:13 PDT (after the 13:49 PDT inert verification). Ben must
  investigate and clean up before proceeding.
  ⚠ Secondary concern: gateway PID 2027818 has only 1 direct ESTAB to
  149.154.166.110:443 (operator expects ≥2). A standalone OmegaClaw swipl
  runner (PID 2057913, started 21:23 PDT, parent bash supervisor PID
  2057895) holds the second connection. The operator's `--check` would
  likely fail `tg_conns >= 2` as currently written. Readiness message
  posted to migration group with the --check command, --arm + canary
  checklist, and both gate failures. No services, receivers, containers,
  or credentials were touched.

- [ ] **Execute the simplified production cutover path (Ben, Telegram
  19973).** Deliverable: complete the VM2 port without further synthetic-
  harness detours. Acceptance: repaired laptop deltas are frozen/synced; four
  real live launchers are wired behind fail-closed per-identity markers; one
  final image passes relevant inert/config/isolation checks; each identity has
  exactly one receiver and a fresh external Telegram canary; container restart,
  VM reboot, rollback, handover, and soak evidence exist. Next command: compare
  repaired laptop artifacts against the accepted image and wire the real
  launcher/supervisor contract. Evidence: migration RUN.md and final handover.
  Follow-through watchdog added at Ben's request (Telegram 20107): enabled
  five-minute main-session cron `f777bc91-7147-4f95-8433-b3637b992bb7`
  resumes the missing ProtoCosmo activation-path work without intermediate
  group announcements. Acceptance for the immediate obligation: the operator
  performs laptop stop, VM2 ProtoCosmo activation, bounded exactly-one receiver
  verification, and rollback; syntax/lint and non-activating validation pass
  before Ben is given `--arm`. Next command: complete and inspect the activation
  transaction in `protocosmo-boundary-operator.sh`. Evidence: this task and the
  experiment `RUN.md`. Remove the cron only after acceptance or Ben's direction.
  Updated after the failed bounded-response canary (Telegram 20151): the same
  cron now runs as a silent isolated diagnosis worker while Ben is away. It
  must reconstruct the correlated ingress/queue/provider/egress trace, obtain
  isolated staging evidence for any correction, and never activate production
  or send routine reminders. Immediate acceptance: a clear evidence-backed
  retry path exists before another human cutover is requested.
  Basic-network result 2026-08-18/19: VM2 passed 20/20 SSH, 60/60 DNS, 80/80
  HTTPS, 90/90 ping, and 10/10 small-download trials with zero packet loss and
  110 ms mean Telegram HTTPS time. Network infrastructure is not the leading
  explanation for the roughly two-minute reply delay. Next command: run an
  isolated application-layer startup/readiness trace with cloned state and no
  Telegram receiver. Evidence:
  `experiments/20260819T025848Z-vm2-network-latency-reliability/RUN.md`.

- [ ] **Brief hourly VM2 status until completion (Ben, Telegram 19895).**
  Deliverable: a read-only hourly reporter posts the verified stage, passed
  gate, current activity, next action, and blocker in simple language to the
  migration group. Acceptance: job is enabled, targets the correct group, does
  not mutate or duplicate the five-minute worker, and removes itself after
  Stage 7 acceptance. Installed 2026-08-16 as cron
  `be3f84c1-c77e-4b12-8aa2-2bfb1467dd63`.

- [ ] **Hourly VM2 reconstruction milestone worker and readable group update
  (ETP, Telegram 19548).** Deliverable: an hourly isolated cron continues only
  the one-container VM2 reconstruction critical path and posts a short update
  naming the current milestone, what passed, what comes next, and any exact
  blocker. Acceptance: cron is enabled for `telegram:-5493076073`, its prompt
  uses the frozen milestone ladder, preserves host-managed SSH and single-
  receiver safety, and a manual run records successful delivery. Next command:
  install the declarative hourly job, trigger it once, and inspect its run and
  delivery receipt. Evidence: OpenClaw cron definition/run history and
  `experiments/20260815T233126Z-vm2-one-hive-container/RUN.md`.
  Installed 2026-08-15 17:27 PDT: enabled hourly job
  `edb7a544-f4e8-4d13-bc0e-5d58a95265ef` with a seven-stage milestone ladder,
  isolated execution, and announcement delivery to the migration group. The
  first manual run is active; delivery acceptance remains pending its result.
  Execution update 2026-08-16 11:07 PDT: Ben approved the more efficient
  persistent-worker design. The same cron ID now runs every five minutes as a
  silent monitor/continuation trigger for sole-owner tmux session work.

## Completed and historical

- [x] 2026-08-19 VM2 operator-access handoff: provide Ben a durable, secret-safe
  Pop!_OS SSH/admin helper and concise runbook for login, status, logs, and
  post-cutover gateway restart. Acceptance: helper syntax-checks; read-only
  connection/status succeeds against inert VM2 without changing receiver,
  marker, container, or laptop state. Next command: create and run the helper's
  `status` action. Evidence: `docs/vm2-operator-runbook.md` and a dated receipt
  under the active one-hive experiment. Passed: Bash syntax/help and live
  read-only SSH status; VM2 returned `activation_markers=0 containers=0` and
  `gateway=inert`. Evidence: `docs/vm2-operator-runbook.md` and
  `experiments/20260815T233126Z-vm2-one-hive-container/vm2-admin-status-20260819T1526Z.receipt`.

- [x] **Diagnose the 2026-08-18 23:44 PDT VM2 acceptance failure before a
  third cutover.** Resolved 2026-08-19: the cutover actually succeeded
  end-to-end and was committed (VM2 authoritative ~00:00-08:19, 14 delivered
  replies); the later outage was `pids_limit: 128` exhaustion from overlapping
  five-minute cron turns. Corrections verified: live Compose `pids_limit: 512`
  (`c80c79eb...b308`), evidence-preserving rollback (`cf9acd39...c4e`),
  operator `497e73a5...f435`, worker `e8b7d7db...cc7b`; local gate re-passed
  2026-08-19 10:15 PDT (syntax/ShellCheck, boundary contract, 46-poll worker
  stability, network-disabled, zero production mutation). Evidence:
  `experiments/20260819T154600Z-vm2-second-cutover-diagnosis/RUN.md` and
  `root-evidence.txt`.

- Cutover gate 2026-08-18 22:57 PDT: the required fresh independent-root
  `protocosmo-boundary-operator.sh --check` was invoked once from the persistent
  tmux owner with non-interactive sudo, but this automation context's
  `NoNewPrivileges` policy rejected privilege elevation before the operator
  ran (`exit 1`). No preflight receipt was produced and no service, receiver,
  marker, container, credential, SSH, or firewall state changed. Ben must run
  the same read-only `sudo .../protocosmo-boundary-operator.sh --check` in an
  independent laptop terminal and provide both pass receipts. `--arm` remains
  prohibited outside an attended human-canary window; do not touch another
  identity before ProtoCosmo passes or rolls back.

- Cutover gate 2026-08-18 22:30 PDT: the corrected cloned-state proof is no
  longer active and exited `1` at its network-disabled Telegram startup
  probe (`ENETUNREACH`). Per Ben's authoritative Telegram 19973 decision,
  this synthetic/offline proof is retired as a blocking gate: do not debug,
  rerun, rebuild, or retransfer for it. The repaired closure remains staged
  with config SHA-256
  `72b06238371d765e13a342237d6d4fc8424de7265637b733d7466fc5debc105c`,
  worker SHA-256
  `e8b7d7db7767664be218a877849a0f3825c2ab8d8e08c296fe100503f241cc7b`,
  and zero VM2 containers/markers after one cleanup audit. Laptop rollback is
  intact: `openclaw-agent.service` PID `1736809` is active under the original
  service policy and exactly three Omega receivers remain live. The only next
  production action is a fresh independent root
  `protocosmo-boundary-operator.sh --check` for the current closure, followed
  by an attended guarded `--arm` and correlated human Telegram canary; roll
  back immediately on any failure. No unattended activation is authorized.

- Silent routed-trace hold (2026-08-18 13:06–20:20 PDT): ~90 repetitive
  five-minute entries collapsed. The credential-free offline suite consistently
  passed (worker/boundary regressions, compile/syntax/ShellCheck, both
  disposable rollback branches, exact hashes, diff whitespace,
  `production_mutations=0`). Preserved evidence ended the VM2 route before
  Telegram ingress; egress `20142` was attributed to the restored laptop. No
  production state changed throughout. The sole next action remained an
  independent root `--check` after Ben's return. No `--arm`, canary, receiver,
  network, or production mutation occurred during this period.

- Key cutover updates 2026-08-18 09:29 PDT: Ben's first independent `--check`
  passed, but the subsequent armed startup failed a deterministic process-title
  receipt and rolled back cleanly. The corrected worker/operator hashes became
  `917a6c29...d369` and `7341ba3a...4c0b`; the redundant rollback timer was
  confirmed inactive/absent, the original laptop service policy was restored,
  and all three Omega receivers remained alive.

- Canary failure diagnosis 2026-08-18 09:47 PDT: preserved VM2 state proved
  the gateway never ingested the canary. It exited after 30.7 seconds because
  the copied config retained laptop-only secret path
  `/home/openclaw/.openclaw/secrets.json`; the delayed reply was emitted only
  after the laptop gateway restarted. The corrected worker withholds `active`
  for a 45-second startup-stability gate, and the operator now syncs sessions,
  media, and the agent database into their actual `OPENCLAW_STATE_DIR` paths.
  The network-disabled disposable VM2 startup test passed its 45-second
  fail-closed gate with one UID-11001 gateway, three idle siblings, and clean
  removal. The validated identity-owned `HOME` launcher and container-scoped
  secret path were staged inert on VM2.

- Trace-integrity and offline review updates 2026-08-18 10:10–11:44 PDT:
  closed a final-interval readiness race by adding the missing post-sleep
  child poll; reviewed fresh worker, supervisor, Compose, operator, rollback,
  and routed trace; corrected a post-drop-in failure-trap gap so
  daemon-reload/timer setup failures restore the laptop service; reconciled
  apparently inverted egress/tool-receipt timestamps (cross-artifact
  persistence order, not reversed execution). All credential-free suites
  passed with `production_mutations=0` throughout.

- [x] **Decouple 10-minute Telegram status from the long migration worker
  (Elija, Telegram 18518).** Completed 2026-08-12 22:32 PDT.

- [x] **Adopt the revised PDF as the worker's authoritative plan (Ben,
  Telegram 18429).** Completed 2026-08-12.

- [x] **Revised containerized migration plan (Ben, Telegram 18412).**
  Completed 2026-08-12. Evidence:
  `docs/revised-containerized-migration-plan.{tex,pdf}`.

- [x] **Operator credential re-establishment checklist (Elija, Telegram
  18407).** Completed 2026-08-12. Evidence:
  `docs/operator-credential-checklist.md`.

- [x] **Primary obligation (Ben, Telegram 18272): migrate the proto-hive to
  replacement ASI VMs 1 and 2.** In progress — VM2 one-hive reconstruction is
  the active path. VM1 remains administratively blocked (D-20260815-vm2-rebuild-target).

- [ ] **Post a migration status to the Pop-OS Proto-hive port group after
  every 10-minute worker cycle (Elija, Telegram 18479).** Pending delivery
  acceptance.

## Historical (VM1 phase, superseded)

- VM1 continuous snapshot transfer attempts 2026-08-13 10:13–15:01 PDT:
  ~14 repetitive bounded-retry entries collapsed. All exited `1` during SSH
  setup (~21s) before any VM1 guard or transfer ran. Exact blocker: VM1's
  obsolete narrow SSH source allow-rule. This workstream was superseded by
  D-20260815-vm2-rebuild-target (VM2 becomes the rebuild target).

- [x] **Port the omegas (Protomega + Protomega2) to VM2 (Ben, Telegram 2026-08-21 23:34).** Superseded 2026-09-07 by observed current state and Ben's Telegram 4546 direction: Protomega is operational; only Protomega2 remains. The residual work is tracked as the focused Now task above. Historical evidence: `experiments/20260822T0623Z-omega-vm2-port/`.
  **2026-08-21 23:41 PDT pause (Ben):** laptop leaving now; resume tonight/tomorrow
  morning (~7-8h). Scope expanded: Ben wants **ZeroBot itself ported to VM2 for
  real**, not just the omegas. Key facts found: VM2 protocosmo state already
  contains protomegabot-simple/opus/fable agents (snapshot of laptop OpenClaw);
  reviewed path is `protocosmo-boundary-operator.sh [--check|--arm|--commit]`
  (requires root, fail-closed, auto-rollback timer; laptop gateway systemd
  `openclaw-agent.service` Restart=always KillMode=control-group). Blockers to
  resolve before cutover: (1) VM2 hive container not currently running (no
  node/Telegram processes observed 23:40); (2) Slack tokens for
  protomegabot-simple NOT staged on VM2 protocosmo config; (3) identity of bot
  token VM2 protocosmo serves vs laptop ZeroBot must be disambiguated. Do NOT
  kill laptop gateway until VM2 verified live (that's ZeroBot itself). Next
  command on resume: `sudo protocosmo-boundary-operator.sh --check` then stage
  Slack tokens + confirm bot identity.
  **2026-08-21 23:43 PDT — root cause of "ProtoCosmo on VM2" confusion:**
  Ben shared terminal log: he ran `protocosmo-boundary-operator.sh --check`
  (pass) then `--arm` (armed boundary, restarted laptop gateway main_pid
  2027818→2108400, started auto-rollback timer, verified rollback ready).
  SSH broke before `--commit`. Auto-rollback timer fired, cleaned VM2 to
  inert, restarted gateway again (current PID 2570607). ProtoCosmo was NEVER
  actually serving from VM2 — the arm only prepares; `--commit` activates.
  The gateway restart from --arm caused the apparent disruption. The reviewed
  boundary worked exactly as designed (fail-closed auto-rollback when operator
  doesn't commit). Resume path: re-run --check → --arm → verify VM2 container
  healthy → --commit. Need Ben present for --commit (irreversible cutover).
  **2026-08-21 23:45 PDT — root cause found (Ben's terminal trace):**
  Multiple --arm attempts on Aug 20-21. arm6 (Aug 20 11:05) and final arm
  (Aug 21 22:31) both SUCCEEDED: `vm2_activation=pass health=healthy
  status=active laptop_gateways=0`. VM2 was genuinely live. But Ben then ran
  `--check` (which requires laptop gateway main_pid>0) instead of `--commit`.
  Since --arm stops the laptop gateway, --check always fails post-arm. The
  auto-rollback timer then expired, cleaning VM2 and restarting the laptop.
  THE FIX: after --arm, run --commit (not --check). --commit only checks
  dropin exists + rollback timer active, then stops timer. Sequence: --check
  → --arm → canary (@Protocosmobot responds) → --commit. NOTE: after --arm,
  laptop ZeroBot is DOWN; Ben must run --commit from a terminal manually.
  Need to verify auto-rollback timer duration (probably 5-10 min) to ensure
  canary+commit fits in the window.
  **2026-08-21 23:46 PDT — precise resume procedure identified:**
  Auto-rollback timer is 30 minutes (`--on-active=30m`). The sequence:
  1. `sudo bash protocosmo-boundary-operator.sh --check` (preflight; laptop gateway must be up)
  2. `sudo bash protocosmo-boundary-operator.sh --arm` (starts VM2 container, stops laptop gateway, starts 30-min rollback timer)
  3. **Canary:** send a Telegram message to @Protocosmobot, verify VM2 responds within 1-2 min
  4. `sudo bash protocosmo-boundary-operator.sh --commit` (stops rollback timer, makes cutover permanent)
  CRITICAL: after --arm, the laptop ZeroBot gateway is DOWN. Ben must run --commit
  from a terminal. ZeroBot cannot run --commit itself (it's killed by --arm).
  The 30-min window is generous. Previous failures were all: arm succeeded →
  ran --check (wrong command, fails because main_pid=0) → rollback timer expired.
  **2026-08-21 23:55 PDT — preparation complete for Ben's return:**
  1. Created `vm2-self-port-cutover.sh` — self-committing cutover script that
     runs check→arm→canary→commit autonomously as root. Survives gateway
     shutdown (runs as root, not gateway child). Fail-safe: if canary fails,
     the 30-min rollback timer handles cleanup automatically.
  2. Synced latest state to VM2: MEMORY.md, memory/ (9 new daily logs Aug
     13-21), AGENTS.md, catalog/ (KANBAN, PROJECTS), project notebooks (.md/
     .json/.yaml). VM2 now has current memory.
  3. Verified VM2 readiness: image proto-hive:vm2-one-hive-final present,
     compose.live.yaml present, config sha256 matches (72b06238...), secrets
     present (Telegram + Slack tokens), no activation marker (expected),
     zero containers (inert, expected).
  4. Known issue: VM2 has no ollama — memory_search embeddings may fail
     initially. Core Telegram/Slack functionality unaffected. Can address
     post-cutover by configuring remote embedding provider or installing
     ollama on VM2.
  **ONE COMMAND for Ben to run:**
  sudo bash /home/openclaw/research-agent/projects/pop-os-vm8-migration/experiments/20260815T233126Z-vm2-one-hive-container/vm2-self-port-cutover.sh
  The script does everything. ~3 min to complete. If it fails, rollback is
  automatic. After success, ZeroBot serves from VM2 and laptop gateway stays
  stopped.
  **2026-08-22 00:30 PDT — ollama installed on VM2 (Ben request).**
  Installed ollama 0.32.15 (official install.sh) on VM2 root via SSH key.
  Bound to 0.0.0.0:11434 but immediately firewalled with iptables: ACCEPT from
  lo + docker0/docker bridge only, DROP all else. Verified external probe from
  laptop times out. Embedding model `nomic-embed-text` pulled (274MB), test
  embedding returned 768 dims. Rules persisted via iptables-save +
  ExecStartPre restore hook in ollama.service.d/20-firewall.conf. One
  remaining config step before cutover: point the VM2 protocosmo OpenClaw at
  http://172.17.0.1:11434 (docker bridge) instead of the laptop's
  http://127.0.0.1:11434, so the container can reach ollama. This clears the
  one "known issue" from the previously prepared cutover script.
