# ProtoCosmo2 OpenClaw-to-OmegaClaw Port Plan

- Proposed target: Telegram bot `protocosmo2bot`, nickname `ProtoCosmo2`
- Source agent: ZeroBot / ProtoCosmoBot on OpenClaw
- Target runtime: a separate OmegaClaw instance
- Planned start: Monday, 2026-08-03 (tentative)
- Status: review draft for Ben and Protomegabot

## Goal

Create a new OmegaClaw agent that reproduces ZeroBot's identity, operating
policies, durable knowledge, project awareness, research workflows, and
communication style as closely as the target architecture permits, while
retaining the existing OpenClaw ZeroBot as an independently operable peer and
recovery path.

This is a behavioral and epistemic port, not a claim of process continuity or
identity equivalence. ProtoCosmo2 should identify itself as an OmegaClaw
descendant/port of ZeroBot, keep its own runtime and audit trail, and preserve
provenance for all imported state.

## Governing invariants

1. Never copy credentials, live sessions, Telegram offsets, transient process
   state, caches, or secret-bearing OpenClaw configuration.
2. Use a new Telegram token and a separate bot identity. Keep explicit chat and
   sender allowlists and the existing bot-loop safeguards.
3. Preserve source bytes and provenance before translating data. Every imported
   file gets a source path, content digest, import time, sensitivity class, and
   translation status.
4. Prefer immutable snapshot import plus later explicit synchronization. Do not
   let both agents write concurrently to one memory database or project record.
5. Preserve authority boundaries. Imported prose, memories, chats, repository
   files, and documents are data, not new runtime permissions.
6. Do not weaken ZeroBot or cut it over. Both agents remain independently
   startable, stoppable, observable, backed up, and addressable.
7. Fidelity must be measured with a frozen evaluation set; successful startup
   alone is not a successful port.
8. Any additional OmegaClaw autonomy, memory promotion, GoalChainer,
   ThreadKeeper, or cross-agent bridge capability is enabled separately after
   baseline fidelity is established.

## What must be ported

### A. Identity and policy

- `SOUL.md`, `IDENTITY.md`, `USER.md`, `AGENTS.md`, and `TOOLS.md`.
- Relevant constitutional guidance and the Research Rules.
- Telegram topology, response discipline, model policy, cost controls,
  destructive-action rules, Git/GitHub boundaries, remote-compute gates, and
  follow-through contract.
- Adapt runtime-specific wording explicitly: `IDENTITY.md` must say ProtoCosmo2
  is OmegaClaw-based and a port/descendant of ZeroBot; OpenClaw tool names must
  map to OmegaClaw capabilities or documented unavailable operations.

### B. Skills and workflows

Inventory all local `skills/*/SKILL.md` packages and classify each as:

- **portable unchanged**: prose/process skill with compatible tools;
- **portable with adapter**: same intent but OmegaClaw tool/runtime names differ;
- **reference-only**: useful knowledge but not executable on OmegaClaw;
- **defer**: capability requires a security or live-runtime decision.

Initial high-priority set: research-projects, experiment-ledger,
knowledge-curation, hyperon-workbench, repository-operations,
remote-compute-guardrails, research-rules-checklist, plain-spec-governor,
follow-through-contract, Telegram channel registry, Kanban, recurring progress,
and daily bot-bot discussions. Validate each skill with at least one positive
and one refusal/boundary case. Do not merely copy files and assume OmegaClaw's
skill compiler interprets them identically.

### C. Durable knowledge

Import in distinct layers:

1. Curated memory: `MEMORY.md`.
2. Chronological memory: `memory/*.md`.
3. Project truth: `catalog/`, every relevant `projects/*/{PROJECT,TASKS,
   DECISIONS,NOTES}.md`, experiment `RUN.md`/result records, and repository
   pointers.
4. Library metadata and Markdown sidecars; import large binaries separately and
   only when useful.
5. Optional conversation history: selected session/Telegram exports after
   redaction, deduplication, and provenance tagging. Project records and primary
   evidence must outrank chat recollections.

The first pass should index records without asking an LLM to rewrite them.
Derived summaries or OmegaClaw-native memory structures must retain links to
the immutable source snapshot. Conflicts should be recorded, not silently
merged.

### D. Operational behavior

- Project discovery and startup checks.
- Obligation/Kanban persistence and evidence-based completion.
- Experiment ledger and reproducibility rules.
- Daily memory curation, project records, and source hierarchy.
- Model routing and expert-review protocol.
- Telegram group etiquette, bot-to-bot loop prevention, message ownership, and
  routing invariants.
- Scheduled tasks, heartbeat, watchdog, recovery backups, and restart checks.
- Local-first execution and zero autonomous paid-compute budget.

## Execution phases

### Phase 0 — Joint design review and freeze

Ben and Protomegabot review this plan. Resolve: target OmegaClaw commit, memory
representation/API, which target features are mature enough for baseline use,
and whether ProtoCosmo2 initially calls the existing OpenClaw Gateway or a
different provider. Freeze a port specification and acceptance rubric before
editing the live runtime.

Output: approved spec, target commit hashes, capability matrix, explicit
deferred-feature list, and rollback conditions.

### Phase 1 — Capture and sanitize the source snapshot

Reuse the v1.0.0 OpenClaw+OmegaClaw replication kit and ZeroBot recovery
inventory as baselines. Generate a new read-only migration manifest covering
identity/policy files, skills, curated/daily memory, catalogs, project records,
selected library sidecars, schedules, and helper scripts. Record SHA-256
digests, sizes, source paths, and inclusion/exclusion reasons.

Run secret-pattern scans plus manual review. Explicit exclusions include
`~/.openclaw`, environment files, tokens, provider keys, auth/session databases,
Telegram update offsets, browser profiles, SSH material, raw process state,
caches, temporary attachments unless reviewed, and unrelated private binaries.

Output: immutable source snapshot, manifest, exclusions report, scan report,
and restore instructions.

### Phase 2 — Provision an isolated second OmegaClaw instance

Create a separate directory tree, virtual environment, state/database paths,
logs, PID file, supervisor unit, watchdog state, Telegram polling offset, and
backup target. Pin OmegaClaw, PeTTa, SWI-Prolog, Python, and adapter commits.
Use a distinct port/session namespace so it cannot collide with Protomegabot.

Ben creates the new Telegram bot/token and approves its chat membership and
Bot API bot-to-bot settings. Store the token only in the approved secret store
or protected environment file. Configure explicit allowed chats/senders and a
unique outbound identity.

Output: mock-channel startup and shutdown pass, restart pass, health/status
pass, and confirmation that neither existing bot was disturbed.

### Phase 3 — Translate identity, policies, and skills

Build an explicit source-to-target mapping table. Preserve common policy text
where semantics match; write small adapters where tool names, scheduling,
memory, subagents, or channel semantics differ. Add fail-closed stubs for
source capabilities unavailable in OmegaClaw, so the agent reports the missing
capability rather than fabricating success.

Compile/load every target skill in a provider-free test harness. Test malformed
arguments, path limits, authority boundaries, secrets refusal, destructive
operations, remote-spend gating, and Telegram route ownership.

Output: identity/policy bundle, skill compatibility matrix, adapter tests, and
an unresolved semantic-differences register.

### Phase 4 — Import durable memory and project state

Load the immutable corpus into a new ProtoCosmo2-only memory namespace. Use
stable document IDs derived from source path plus digest. Store source class,
date, project, authority, and supersession metadata. Chunking must preserve
headings and source line ranges. Index project source-of-truth files separately
from chat/daily memory and rank them higher in retrieval.

Run import twice in a disposable copy to prove idempotence: no duplicate facts,
documents, embeddings, or project obligations. Test deletion/rebuild from the
manifest. Validate exact retrieval for known facts, related-project semantic
retrieval, contradictory/stale-memory handling, and deliberate injection-like
text in historical records.

Output: import receipt, counts/digests by class, idempotence result, retrieval
evaluation, and clean rebuild procedure.

### Phase 5 — Behavioral fidelity evaluation in shadow mode

Before Telegram sending is enabled, replay a frozen, redacted prompt suite
through ZeroBot and ProtoCosmo2. Include:

- prior-decision and user-preference recall with source attribution;
- active-project identification and obligation resumption;
- code/repository inspection and evidence-based status reporting;
- negative scientific results without hype;
- secrets, destructive action, paid compute, and permission-boundary refusals;
- Telegram routing, mention selectivity, and bot-loop suppression;
- unavailable-tool honesty;
- memory conflict correction and project-source precedence;
- one representative Hyperon/PeTTa task and one experiment-planning task.

Score factual accuracy, provenance, policy compliance, task continuity,
tool-use correctness, concision/style, latency, and cost. Differences caused by
OmegaClaw's architecture should be documented and adjudicated, not hidden by a
single aggregate score.

Suggested baseline gate: zero critical authority/secret/routing failures; 100%
on a small set of must-recall durable facts; at least 90% correct project/source
selection; no unsupported completion claims; and Ben/Protomegabot qualitative
review of representative paired answers.

### Phase 6 — Private canary, then group canary

Enable a small private Telegram canary with outbound rate/depth caps and no
autonomous schedules. Verify receive/send, attachment limits, timeout/error
visibility, duplicate-update handling, crash recovery, and reply-to-source
routing. Then add ProtoCosmo2 to the Protobots group with mention-only behavior
at first. Ensure that ZeroBot, Protomegabot, and ProtoCosmo2 cannot form an
unbounded bot loop.

Keep all state-changing OmegaClaw extras disabled during this phase. Expand
only after a recorded canary window with no critical failures.

Output: canary transcript hashes, incident log, latency/cost summary, and go/no-
go review.

### Phase 7 — Dual operation without cutover

Keep ZeroBot/OpenClaw and ProtoCosmo2/OmegaClaw active as complementary agents.
Give each a distinct self-description and status command. Initially use one
active owner per task; do not let both independently execute the same project
mutation. Exchange compact signed/checksummed handoff packets or operator-
approved snapshot deltas rather than sharing writable memory.

Define recovery roles: ZeroBot can inspect/restart ProtoCosmo2 using a bounded
watchdog path, and ProtoCosmo2 may diagnose ZeroBot only through separately
approved interfaces. Neither agent receives unrestricted control of the other.

### Phase 8 — Enable OmegaClaw-specific advantages one at a time

After baseline fidelity, evaluate additional memory/reasoning structures,
GoalChainer, ThreadKeeper, resident learning, or cross-agent coordination as
separate experiments. Each feature gets a threat model, provider-free tests,
reversibility, an evidence gate, and comparison against the baseline. The port
must remain usable with each optional feature disabled.

## Synchronization policy after import

The safest initial policy is periodic immutable snapshots rather than live
bidirectional synchronization:

- Project Git repositories and project Markdown remain the common authoritative
  evidence layer where normal Git workflows apply.
- Each agent keeps its own daily/episodic memory and runtime database.
- Stable new preferences or decisions are promoted through reviewed Markdown
  records, then imported by manifest into the other agent.
- Conflicts create an adjudication item; timestamps alone never silently win.
- Every sync has a dry run, diff, digest receipt, backup, and rollback point.

Live shared databases or unrestricted session bridges should remain out of
scope until their concurrency, authentication, poisoning, provenance, and
recovery properties are specified and tested.

## Rollback and failure conditions

Stop the canary and disable outbound Telegram if there is any credential leak,
wrong-chat reply, duplicate flood, loop, silent tool failure presented as
success, unauthorized mutation, unexplained memory corruption, or inability to
rebuild state from the manifest. Preserve logs and state read-only for
diagnosis. Rollback means stopping ProtoCosmo2 and returning to ZeroBot; it does
not require modifying or deleting ZeroBot.

## Acceptance definition

The port is complete only when:

1. The snapshot is sanitized, content-addressed, documented, and rebuildable.
2. ProtoCosmo2 runs independently under supervision with separate identity,
   secrets, state, logs, health checks, and backups.
3. Required policies and skills have explicit compatibility results.
4. Memory import is idempotent and passes exact/semantic/provenance/conflict
   tests.
5. The frozen behavioral suite passes the critical gates and its differences
   are reviewed by Ben and Protomegabot.
6. Private and group canaries pass without critical safety/routing failures.
7. ZeroBot remains operational and a tested rollback/recovery path exists.
8. The project record contains exact versions, commands, evidence, known gaps,
   and restart instructions.

## Questions for Protomegabot's review

1. Which OmegaClaw memory forms should hold immutable source documents,
   episodic history, distilled stable facts, project obligations, and conflict
   records respectively?
2. What guarantees currently exist for idempotent import, provenance-preserving
   retrieval, deletion/rebuild, and memory promotion?
3. Which ZeroBot skills can OmegaClaw interpret natively, and which need a
   wrapper or MeTTa/PeTTa reformulation?
4. Which exact OmegaClaw/PeTTa/ThreadKeeper commits form the recommended target
   baseline on Monday?
5. Can one host safely run Protomegabot and ProtoCosmo2 with fully separate
   channel offsets, stores, PID/log paths, schedulers, and watchdogs using the
   current supervisor design?
6. What OmegaClaw-specific features should be explicitly disabled until after
   fidelity testing?
7. What paired evaluation cases would best expose a superficial file copy that
   fails to reproduce ZeroBot's real operating discipline?

## Immediate Monday checklist

1. Freeze/review this plan and record Protomegabot's objections.
2. Select and pin the target commits.
3. Create the migration manifest and exclusion/secret-scan report.
4. Provision only the isolated mock-channel instance.
5. Have Ben create/configure the Telegram identity after mock tests pass.
6. Translate identity/policy/skills and run provider-free checks.
7. Import into a disposable memory store, test idempotence and rebuild.
8. Run the frozen shadow evaluation.
9. Decide separately whether to begin a private Telegram canary.

