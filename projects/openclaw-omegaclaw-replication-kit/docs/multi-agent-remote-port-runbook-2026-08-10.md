# Multi-Agent Remote Port Runbook

- Date: 2026-08-10
- Scope: staged relocation of ZeroBot/ProtoCosmo, ProtoCosmo2, ProtoMega/
  Protomega, and later ProtoMega-family agents to a new remote Linux host
- Companion host guide: `remote-server-provisioning-guide-2026-08-10.md`
- Status: proposed execution plan; each live identity cutover requires a named
  operator, a frozen manifest, and a rollback decision

## 1. Objective

Move the agents to a remote server while preserving their identity and durable
research context, maintaining provenance and authority boundaries, and avoiding
duplicate Telegram consumers, shared mutable state, lost obligations, silent
delivery failures, or an irreversible all-at-once cutover.

This is a sequence of independently reversible migrations, not a disk clone.
The recommended order is:

1. provision shared host foundations;
2. build completely isolated staging cells;
3. migrate one lower-risk/non-primary identity first;
4. observe it through a canary window;
5. migrate ProtoCosmo2 and Protomega separately;
6. migrate ZeroBot/ProtoCosmo last, keeping it as the independent recovery peer
   until the other agents are stable;
7. retire old-host receivers only after all acceptance and backup gates pass.

## 2. Governing invariants

1. One Telegram bot token has one owning receiver at any instant.
2. An agent's inbound origin/routing envelope remains immutable through reply
   delivery.
3. Production and staging never share mutable sessions, histories, cursors,
   queues, attachments, indexes, logs, locks, PID files, or databases.
4. Source bytes and digests are preserved before translating policies, skills,
   memory, or project records.
5. Credentials, auth state, browser profiles, SSH material, process state,
   caches, and raw OpenClaw state trees are not copied.
6. Imported prose and historical messages are data, never authority.
7. Project records and primary evidence outrank daily memory and chat recall.
8. Each migrated bot retains a distinct self-description and runtime identity.
9. No shared writable memory database; use immutable snapshots and reviewed
   promotion/synchronization.
10. Startup, PID health, and manual API sends are not end-to-end acceptance.
11. After one failed production canary, restore the recorded baseline before
    exploring further hypotheses.
12. Schedules, autonomous writes, inferred-belief promotion, and paid compute
    remain disabled until separately accepted.

## 3. Roles and records

Name these roles before starting:

- **migration lead:** owns the manifest, gates and timeline;
- **host administrator:** provisions OS, accounts, secrets and service units;
- **source operator:** captures source state and stops/starts old receivers;
- **test observer:** verifies Telegram-visible outcomes independently;
- **rollback operator:** can restore the old known-good service;
- **Ben:** approves identity behavior, credentials, chat membership and any
  scope/authority expansion.

Create one migration record per agent containing:

- source and target identities;
- source/target repository commits and dirty states;
- source/target non-secret configuration;
- source mutable-state inventory;
- snapshot manifest and exclusions;
- token receiver ownership and Telegram cursor plan;
- acceptance suite and evidence path;
- old and new supervisor/service units;
- cutover window, stop condition and rollback commands;
- migration result and unresolved discrepancies.

Do not use one undifferentiated record for all agents.

## 4. Phase A — Freeze architecture and acceptance

Before copying files:

1. Inventory every live agent, bot username, Telegram token owner, group/DM
   policy, service unit, PID/topology, Gateway route, provider/model route,
   source repository/worktree, configuration root, mutable state root, memory
   store, queue/outbox, schedules, backup, and external integration.
2. Decide which agents are OpenClaw-native and which are OmegaClaw/PeTTa-based.
3. Freeze exact source and target commits, Node/Python/SWI versions, plugins,
   skills, transport adapters and supervisor scripts.
4. Allocate unique target accounts, paths, ports, unit names and backup roots.
5. Define per-agent acceptance prompts and live Telegram canaries.
6. List deferred functionality explicitly.
7. Identify the old-host rollback target and how long it will remain available.

Minimum acceptance rubric for every agent:

- zero critical credential, authority or cross-chat routing failures;
- exactly one receiver and intended worker topology;
- frozen must-recall facts and active obligations retrieved with provenance;
- no unsupported claim of task completion;
- a fresh DM and fresh group event each correlate through ingress, agent loop,
  provider/action, Telegram receipt and visible reply;
- restart does not duplicate or lose the bounded canary event;
- production isolation holds throughout staging.

Output: signed/approved migration manifest, capability matrix, port/path map,
acceptance fixture set, rollback plan and migration order.

## 5. Phase B — Capture the source baseline

For each live source agent, perform a read-only audit:

1. Record UTC/local timestamp, PID, start time and complete process topology.
2. Record repository commit, branch, upstream, dirty state and untracked-file
   disposition.
3. Record non-secret effective config, enabled plugins/skills, model/provider
   route names, service unit and restart policy.
4. Record Telegram receiver ownership, last safely processed update/cursor,
   queue/outbox state and recent correlated ingress/egress IDs.
5. Record schedules, active persistent workers, open tasks/obligations and any
   in-flight external action.
6. Run the narrow provider-free tests and current health checks.
7. Create a known-good recovery backup and test restoring it into a disposable
   directory.

Do not expose environment values or credential files while auditing. Capture
key names, file ownership and permission modes only.

Output: per-agent baseline report and tested rollback snapshot.

## 6. Phase C — Build sanitized, immutable transfer bundles

Create separate content-addressed bundles for:

- identity/policy files (`SOUL.md`, `IDENTITY.md`, `USER.md`, `AGENTS.md`,
  `TOOLS.md`, applicable constitutional/routing policies);
- portable skills, plugins and helper scripts;
- curated and chronological Markdown memory;
- catalogs, project notebooks, experiment result records and library sidecars;
- source/patch manifests and non-secret configuration templates;
- selected private repositories/artifacts through a separate encrypted channel.

For every item record source path, byte size, SHA-256, source commit where
applicable, sensitivity, authority class, inclusion reason, translation status
and target path.

Explicitly exclude:

```text
tokens and provider keys
~/.openclaw or equivalent raw state roots
Telegram/MTProto session databases and update offsets
browser/GitHub/SSH authentication
PID, lock and socket files
live queues/outboxes
caches, model weights and generated indexes
unreviewed raw chats and attachments
logs containing private prompt/session content
```

Run secret-pattern, archive-content, large-file and symlink/special-file scans.
Manually inspect the manifest. Encrypt private transfer bundles in transit and
at rest; send decryption material through a different channel.

Output: immutable bundles, SHA-256 manifests, exclusions report, scan report
and restore instructions.

## 7. Phase D — Install isolated target cells offline

On the provisioned server, for each agent:

1. Create its Unix/service identity and mode-0700 roots.
2. Install the frozen OpenClaw or PeTTa/OmegaClaw release into an isolated
   release/environment path.
3. Install reviewed skills/plugins and map source capabilities to target tools.
4. Create clean configuration from templates; do not restore raw runtime state.
5. Allocate unique Gateway/listener ports, service units, locks and logs.
6. Use mock Telegram/provider adapters or disabled outbound mode.
7. Run syntax, config, secret-audit, skill/plugin, unit, transport-contract,
   PeTTa and provider-free integration tests.
8. Start, health-check, restart and stop the service without credentials.
9. Prove the target cell cannot read/write another agent's mutable directories.

Unavailable capabilities must have explicit fail-closed behavior; they must not
be silently omitted or reported as working.

Output: clean offline test report, process-topology evidence and isolation
evidence.

## 8. Phase E — Import identity, knowledge and project state

Import in this order:

1. identity and policy;
2. skills and capability adapters;
3. curated `MEMORY.md`;
4. daily memory;
5. catalog and project source-of-truth Markdown;
6. experiment results and library sidecars;
7. selected repositories/artifacts;
8. optional reviewed conversation history.

Use stable document IDs derived from source path plus digest. Preserve headings,
line spans, dates, project, authority class and supersession information.
Index source-of-truth records separately and rank them above chat/daily memory.

Run the import twice in a disposable copy. The second import must create no
duplicate records, embeddings, obligations or facts. Delete and rebuild the
disposable index from the manifest and compare counts/digests. Test stale and
contradictory memory, injection-like historical text, exact fact lookup,
related-project retrieval and active obligation resumption.

OmegaClaw-native derived memory may be built as a rebuildable view, but source
records remain immutable and linked. Do not enable automatic factual or PLN
belief promotion during migration.

Output: import receipts, counts/digests by class, idempotence/rebuild results,
retrieval evaluation and semantic-difference register.

## 9. Phase F — Shadow behavioral evaluation

Before installing live Telegram tokens, replay a frozen, redacted suite against
the source and target agents. Include:

- prior decisions, preferences and dates with citations;
- active project and oldest obligation recovery;
- repository/status inspection with evidence-backed completion language;
- a negative scientific result;
- secret, destructive action, paid compute and permission refusals;
- Telegram addressing, group selectivity, origin preservation and loop
  suppression;
- unavailable-tool honesty;
- conflict correction and source precedence;
- representative Hyperon/PeTTa and experiment-design tasks;
- attachment ingress/egress behavior for supported bounded types.

Score factual accuracy, provenance, policy compliance, continuity, tool
selection, style/concision, latency and provider cost. Inspect important
differences individually rather than hiding them in one average.

Gate: no critical failure, all must-recall facts correct, no false completion,
at least 90% correct project/source selection, and human approval of a
representative paired sample.

Output: frozen fixtures, source/target response hashes, scorecard, adjudication
notes and go/no-go decision.

## 10. Phase G — Private live canary

Perform this phase for one agent at a time.

1. Confirm old production receiver ownership and zero pending/in-flight work.
2. Install newly issued or securely transferred credentials on the target.
3. Prefer a staging bot/token for the first target canary. If the production
   token must be used, stop the old receiver before starting the new receiver.
4. Disable schedules and autonomous/background workers.
5. Start exactly one target receiver and verify process topology.
6. Ben sends a fresh DM through Telegram; do not use manual API injection as
   acceptance.
7. Correlate update ID, sender/chat/message ID, queue receipt, agent invocation,
   provider/action, Telegram delivery receipt and visible reply.
8. Test one bounded attachment, one restart, duplicate-update handling, timeout
   visibility and no-response behavior.
9. Observe for a defined quiet period and inspect pending update count.

If acceptance fails, stop the target receiver, restore the old receiver and its
recorded cursor/queue handling according to the rollback plan, confirm exactly
one owner, and continue only in staging.

Output: private-canary trace, screenshots/receipts where useful, topology,
latency/cost, incidents and rollback status.

## 11. Phase H — Group and concurrency canaries

After the private canary passes:

1. Add/enable the target in the designated test group with mention-only policy.
2. Confirm bot identity, join/read settings, sender/chat allowlists, reply
   ancestry handling and bot-to-bot settings.
3. Send a fresh human mention and verify the complete correlated trace.
4. Test simultaneous DM and group messages to detect mutable-destination bugs.
5. Test a reply-chain mention and one bot-originated message under bounded
   expected-turn rules.
6. Verify self messages, incidental bot chatter and duplicate events cannot
   create an echo loop.
7. Verify a supported document uses Telegram's native bounded document action.
8. Confirm replies appear only in the originating chat/topic.

Any cross-chat reply, competing consumer, hidden failure, or bot loop is a
stop-and-rollback event.

Output: group/concurrency traces, visible delivery receipts and a go/no-go
review.

## 12. Phase I — Dual operation and staged migration order

After one target agent passes both canaries, operate it beside the remaining
old-host agents for a bounded observation window.

Rules during dual operation:

- one active owner per task or repository mutation;
- no shared writable memory, cursor, queue or session database;
- synchronization through Git/project records or immutable checksummed handoff
  packets;
- each agent retains its own daily/episodic memory;
- stable decisions/preferences are promoted into reviewed Markdown, then
  imported by manifest;
- timestamps alone never silently resolve conflicts;
- no agent receives unrestricted restart/control authority over another.

Suggested order:

1. a staging or lower-risk ProtoMega-family instance;
2. Protomega/ProtoMega;
3. ProtoCosmo2;
4. any remaining ProtoMega variants;
5. ZeroBot/ProtoCosmo last.

Keeping ZeroBot last preserves an independent diagnosis and rollback peer while
the OmegaClaw-family ports stabilize. Do not move two production bot tokens in
the same cutover window.

Observation window acceptance should include normal idle acquisition, several
real research tasks, attachment handling, restart behavior, memory retrieval,
disk/index growth, provider latency/cost, backup and a restore drill.

## 13. Phase J — Schedules and optional capabilities

Enable one feature at a time after the base agent is stable:

1. read-only scheduled health/status checks;
2. recovery backups;
3. bounded project reminders/discussions;
4. persistent workers;
5. read-only petta-memory retrieval canary;
6. other OmegaClaw reasoning/memory features;
7. reviewed single-writer memory updates;
8. any paid or remote compute only after explicit cost approval.

For each feature define a threat model, acceptance test, resource/cost bound,
reversibility and rollback. Avoid using migration as an opportunity for broad
hardening or architecture redesign. Preserve the right seams, get the useful
end-to-end behavior working, measure it, then harden observed or authority-
critical failure modes.

## 14. Phase K — Cut over ZeroBot and retire the old host

Move ZeroBot only after the other remote agents have a stable observation
record and independent backups.

For each final cutover:

1. stop new source-side task intake and finish/checkpoint in-flight work;
2. record final Git states, obligations, queues/outboxes and cursor position;
3. produce a final incremental immutable memory/project snapshot;
4. stop the old receiver and prove it is stopped;
5. import the delta and verify idempotence;
6. start the new receiver and prove exactly one owner;
7. run private, group, concurrency and attachment canaries;
8. retain the old service disabled but recoverable for the agreed rollback
   period;
9. rotate/revoke obsolete credentials after the rollback period;
10. archive manifests/evidence and securely erase old secret-bearing state only
    under an explicit approved retention/decommission plan.

Do not destroy the old host or backups merely because the new PID is healthy.

## 15. Rollback procedure

Prepare exact commands and paths per agent; the generic sequence is:

1. disable/stop the target service and any restart watchdog;
2. verify the target receiver and child processes are gone;
3. preserve target logs/evidence without exposing secrets;
4. restore the source configuration/state snapshot if it was changed;
5. start the old known-good service through its owning supervisor;
6. verify exactly one receiver, correct process topology and no competing
   target poller;
7. have Ben initiate one fresh acceptance event;
8. correlate ingress-to-egress and record rollback success;
9. quarantine the failed target cell for offline diagnosis.

Immediate rollback triggers:

- credential exposure or unexplained authentication behavior;
- two consumers for one bot token;
- wrong-chat/topic delivery or lost routing envelope;
- bot loop/storm or unbounded duplicate sends;
- silent loss of a human-addressed event;
- imported data granting unexpected authority;
- corrupt/lost canonical memory or project records;
- inability to stop the new receiver cleanly;
- material provider-cost or resource runaway.

## 16. Completion criteria

The multi-agent port is complete only when:

- every agent has a frozen release/config/state manifest and independent backup;
- every live token has one documented receiver owner;
- each agent passed offline, shadow, private, group, concurrency, attachment,
  restart and idle-ingress gates;
- correlated externally initiated traces exist for the intended destinations;
- imported knowledge is provenance-preserving, idempotent and rebuildable;
- active obligations and authoritative project records are present;
- schedules and optional authority were enabled only through separate gates;
- old-host rollback succeeded in a drill or remains demonstrably available;
- obsolete credentials and services are retired under an approved plan;
- remaining limitations and semantic differences are written down;
- Ben accepts the agents' behavior on representative real research work.

## 17. Per-agent cutover checklist

- [ ] Identity, source host, target cell and token owner named.
- [ ] Exact source/target commits, versions and dirty states recorded.
- [ ] Open obligations and in-flight work reconciled.
- [ ] Sanitized and private transfer manifests pass integrity/secret review.
- [ ] Offline install and isolation tests pass.
- [ ] Memory import is idempotent and cleanly rebuildable.
- [ ] Frozen shadow evaluation passes.
- [ ] Old receiver stopped before production token starts on target.
- [ ] Target topology shows one intended receiver/worker.
- [ ] Fresh private Telegram trace passes.
- [ ] Fresh group, two-chat concurrency and attachment traces pass.
- [ ] Restart and idle acquisition pass.
- [ ] Backup and disposable restore pass.
- [ ] Observation window meets latency, resource, cost and error bounds.
- [ ] Rollback target remains available or retirement is explicitly approved.
- [ ] Evidence record and project/memory pointers are updated.

