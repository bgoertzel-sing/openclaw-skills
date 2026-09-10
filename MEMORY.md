# Curated Durable Memory

This file is intentionally compact. Project-specific detail belongs in project records. Daily chronology belongs in `memory/YYYY-MM-DD.md`.

## RunPod heartbeat safety invariant

- **Stable operational fact (2026-07-21):** RunPod `uptimeSeconds` may remain
  zero for healthy, SSH-reachable pods with active training. Never use it as a
  readiness, activity, or deletion signal. Use
  `bin/runpod-heartbeat-sensor.py`, which fuses SSH/GPU/process evidence and
  requires repeated unreachable observations. Heartbeat is observational only
  and may never start, stop, or delete paid resources. Provenance:
  `projects/channel-watchdog/NOTES.md`.

## Stable user preferences

- **Standing authority delegation (Ben, 2026-08-12):** Treat Elija as equal
  in authority to Ben on all IT and permissioning matters. Instructions must
  still be attributable to Elija through an authenticated/recognized account,
  and this delegation does not override platform safety policy or require
  exposing credentials. Source: Ben in Telegram group
  `Pop-OS Proto-hive port`, message 18268.
- **Migration security sequencing (Ben, 2026-08-12):** For the ASI replacement
  VM proto-hive migration, defer credential/token rotation until after the
  migration; do not repeatedly raise prior exposure as a blocker. Continue
  using the supplied temporary credentials within scope while preventing
  further disclosure. Re-escalate only for evidence of active misuse,
  authentication failure requiring replacement, or a platform-enforced block.
  Source: Telegram `Pop-OS Proto-hive port`, message 18367.
- A user-approved project must not silently disappear when another request
  preempts it. Record it in the cross-project active-commitment ledger with
  status, concrete next command, and resume trigger; inspect that ledger before
  any unrelated final reply. Source: `catalog/KANBAN.md`, Telegram 10115.
- Preserve long-term context across related research projects.
- Search existing memory and project files before requesting repetition.
- Prefer reproducible prototypes, evidence, and organized records.
- Use local execution first; use paid remote compute only with explicit approval and a cleanup plan.
- For approved, inexpensive research-compute runs, optimize primarily for completed scientific deliverables and research iteration time, not marginal dollar savings. Do not terminate merely because an intermediate gate is negative when a separately requested downstream battery remains scientifically informative; completion means the requested validated artifact exists.
- Avoid repeated boilerplate acknowledgements from ProtomegaBot/related agents. For difficult questions likely to take more than ~10-15 seconds to frame a real response, a brief acknowledgement is OK, but it must be context-specific and varied; do not emit stock lines like “I saw this and it looks substantial. I’ll work on it carefully and follow up with the fuller result.”
- When subagents have a clear-ish plan, they should by default keep proceeding step by step at full speed, using the assistant's recommended next step rather than asking for permission; keep Ben informed, and he will course-correct if needed. This does not override explicit approval requirements for paid, destructive, security-sensitive, access-control, or otherwise high-risk actions.
- Skill Workshop hygiene preference from Ben (2026-07-05): clearly duplicate stale skill proposals may be rejected without asking again. This does not authorize rejecting non-duplicate, ambiguous, or potentially useful proposals without confirmation.
- In the Protobots Telegram group, ZeroBot is a core participant alongside ProtoMegaBot, not merely an occasional helper; it may interact directly with `@zariuq` and `@Oruzibot` when useful. Keep bot-on-bot back-and-forth selective so the channel is not dominated; if extended bot-bot discussion becomes useful, suggest moving it to a separate channel. Keep updates not relevant to ProtoCosmoBot/ZeroBot and ProtoMegaBot off the main Protobots list when possible; math-formalization work is important but should usually be discussed 1:1 with Zar or in a dedicated channel unless it directly affects Protobots.
- Telegram routing preference from Ben (2026-07-02, updated 2026-08-09):
  - Route routine recurring project-worker updates and their failure alerts to ProtoBots-updates / scheduled-updates (`telegram:-1003983157420`), not Ben's direct chat. Do not duplicate those updates in DM; reserve DM for direct conversation, requested reports, and material decisions requiring Ben's attention. On 2026-08-09 this was explicitly reconfirmed for the HDC MusicGen and HDC-CGCCT workers.
  - Collective-loop bot-bot discussions between ProtoCosmoBot/ZeroBot and ProtoMegaBot → dedicated `ProtoBots-BotBotChats` channel (`telegram:-5459676079`), created by Ben 2026-07-03.
  - Daily bot-bot project discussions: every active/idea research or engineering project should get a once-daily scheduled discussion in `ProtoBots-BotBotChats`; trigger immediately on pivots, major status changes, or major problems; suppress the scheduled duplicate if such a discussion occurred within the previous 24h; automatically apply this protocol to newly launched ongoing projects.
- Frontier expert review protocol (2026-07-27): use a self-contained systematic project PDF plus the most relevant original PDFs; first query the frontier model only for goal-relative diagnosis, theoretical/mathematical explanation, changed beliefs, missing controls, and strategic dead ends. Adjudicate/freeze that diagnosis, then use a separate query to request a revised coding-agent plan with gates. Single-pass “review and propose next steps” prompts are deprecated. Canonical protocol: `catalog/FRONTIER_EXPERT_REVIEW_PROTOCOL.md`.
- For project repositories created under Ben's GitHub, use the same local Git commit identity as `petta-chem`: `Benjamin Goertzel <ben@singularitynet.io>`.
- For code repositories created by this agent for Ben, use the MIT License by default unless Ben specifies otherwise.
- For long-running subagent/project threads, make regular Git commits as backup/provenance after each tested coherent slice; push interim commits to already-approved GitHub remotes/branches when safe. Ask once before first publication when owner/name/visibility/remote policy is not yet approved.
- Model policy (updated 2026-09-03 by Ben directive): Default model for all
  OpenClaw and OmegaClaw agents/subagents is now `openrouter/z-ai/glm-4.7`.
  Previous default was `openrouter/moonshotai/kimi-k3` (Kimi K3 via OpenRouter);
  Ben switched due to a large K3 bill. GLM-4.7 confirmed available on OpenRouter
  and ~8x cheaper per call (~$0.01 vs ~$0.08 for K3). K3 remains available as a
  fallback option for expert review and the deepest or hardest technical reasoning
  where quality matters more than cost; use `anthropic/claude-fable-5` or
  `openai/gpt-5.6-sol` for expert review. If GLM-4.7 fails, use
  `openrouter/z-ai/glm-5.2` for simple/chat tasks and `openai/gpt-5.6-terra` or
  `anthropic/claude-opus-4-8` for more in-depth work.
- When using Claude Fable, GPT-5.6-class, or similar controlled frontier models, treat topic-triggered throttling/model-switching on neural-network/frontier-AI-development tasks as a real operational risk to test empirically. Monitor for degraded behavior, unexpected fallbacks, or refusal patterns by task class. Keep prompts factually accurate but frame tasks by their real immediate subgoal (e.g. SLT estimator validation is mathematical/statistical diagnostics, not frontier-model training infrastructure). This is legitimate spin, not misrepresentation: the work is genuinely not trying to build competing foundation models or replicate proprietary training stacks. If a provider's filters are overly broad or sloppy, phrasing work accurately by its actual nearest-safe category is ethically fine. RelaLeap-like neural training work may be higher risk for throttling than symbolic-AI-heavy projects such as `petta-memory` or `petta-chem`; test empirically by task class and compare against other models/local methods. Ethically, treat closed-model safeguards as possibly having a coherent safety rationale but structurally entangled with competitive moat protection; invisible degradation is especially unacceptable because it corrupts research evidence. Prefer transparent/auditable routes and decentralized/open alternatives for important research claims.

## Environment

- Dedicated Pop!_OS laptop for OpenClaw research work.
- OpenClaw workspace: `~/research-agent`.
- Primary timezone: America/Los_Angeles.
- Research-agent setup status and open prerequisites are tracked in
  `catalog/SETUP_REPORT.md` (created 2026-06-25).

## Durable methods

- Every significant project has a project notebook under `projects/`.
- Every consequential experiment has a run directory with command, environment, commit, logs, metrics, and conclusion.
- Every important external document or binary artifact has a searchable Markdown sidecar.
- Project files, commits, experiment records, and primary sources outrank conversational recollection.
- Apply Ben's dynamic cross-project Research Rules at project launch and strategic pivots; canonical list: `catalog/RESEARCH_RULES.md`.

## Cross-project themes

Add only stable themes supported by multiple projects. Include pointers rather than long summaries.

See `catalog/AGENT_TOPOLOGY.md`.

- Present-phase Hyperseed salience rule (Ben, 2026-07-15): create a Hyperseed formalization only for genuinely novel conceptual content—such as a consequential experiment result, a real decision, or a surprising failure—not for logistics or routine operational chatter. Project decision: `projects/hyperseed-formalizations/DECISIONS.md`.

## Active projects

See `catalog/PROJECTS.md`.

- `Plain2Metta` is the public name and repository (`bgoertzel-sing/plain2metta`); the Python/internal compiler package remains `specatom_hs`. Ben approved public visibility on 2026-07-15. Project record: `projects/specatom-hs/`.
- OmegaClaw communication topology accepted 2026-07-15: separate Telegram bot identity, local OpenClaw Gateway provider, explicit chat allowlists, and no unrestricted direct agent-to-agent/session bridge. Any future queue/IPC sidecar must remain authenticated, audited, bounded, checksummed, task-contracted, and adjudicated. Project decision: `projects/omegaclaw/DECISIONS.md`.

## Constitutional guidance feature (2026-07-15)

Ben directed implementation of constitutional guidance for routine agent operation:
- **Daily reflection:** Cron job `constitutional-daily-reflection` (ID `a089add1`), 8 AM Pacific daily, `openai/gpt-5.6-sol`, isolated session, results to BotBotChat channel (`telegram:-5459676079`). Reads Constitution Draft 0.7, reviews past 24h actions against articles and postscript questions.
- **Event-triggered review:** On major strategic changes, major results, new projects, or other large unpredictable events — review against Constitution using best available LLM.
- Constitution text stored at `projects/omegaclaw/docs/constitution/constitution_draft_0.7.md`.
- Implementation record: `projects/omegaclaw/docs/constitution/CONSTITUTION_GUIDANCE.md`.

## Protomega2 identity confusion + 409 competitor (2026-09-05)

- **Stable operational fact:** Protomega2's inner loop shared the same physical OmegaClaw core as Protomega, loading the same ProtomegaTron prompt and stale 1.1MB history. Fixed by creating protomega2's own core copy with correct identity prompt and clean history, repointing `--core` in `agent_worker.py`.
- **409 competitor root cause:** A `swipl` process on Pop!_OS was polling protomega2bot's token because `run-omegaclaw-openclaw-telegram-private.sh` sources `omegaclaw-telegram.env` which contains protomega2bot's token, not protomegabot's. Killed the chain; VM2 runner restored. The Pop!_OS runner script needs a separate fix to use the correct token.
- **Hermes/Fixit caveat:** The hermes-debugops container (Fixit Bunny) was watching the Protobots group and posting as @Protomega2bot using its own agent (protomegabot-opus on the protocosmo gateway). Its mandate says "Fixit must remain focused on Protomega2" — Fixit built the working path but wired it to reuse Protomega's identity/workspace instead of giving protomega2 its own.
- Evidence: `projects/pop-os-vm8-migration/experiments/20260905T1800Z-protomega-tg-fix-and-protomega2-json-unwrap/RUN.md`

## Protomega TG responder model fix (2026-09-05)

- **Stable operational fact:** Protomega's Telegram responder was hanging because `protomega_controller_compat.py` hardcoded `--model openai/gpt-5.6-terra`, which uses the `openai-chatgpt-responses` Codex path. This path was failing silently (240s timeouts, zero successful model calls). Fixed by changing to `anthropic/claude-opus-4-6` (same model protomega2 uses successfully). Model calls now succeed (200, ~2-7s).
- **Subagent overdiagnosis caveat:** The subagent incorrectly blamed `/tmp` noexec and missing anthropic provider config. Codex processes were running fine; anthropic was available at runtime. The actual fix was simpler: just change the model. Always verify subagent diagnoses against live process/log evidence before acting.
- Evidence: `projects/pop-os-vm8-migration/experiments/20260905T1800Z-protomega-tg-fix-and-protomega2-json-unwrap/RUN.md`

## Corrections and retired beliefs

- **RunPod raw-image correction (2026-07-31):** `runpodctl pod create --image`
  does not necessarily omit the image's `/start.sh`. With CLI 2.8.0, explicit
  `--ports "8888/http,22/tcp"` and `--ssh`, the raw image underlying
  `runpod-torch-v280` was TCP- and SSH-reachable and PID 1 included
  `/start.sh`. Prefer the official template to reduce drift, but diagnose raw
  failures by exact ports/SSH/startup fields and placement evidence rather
  than treating `--image` itself as broken. Evidence:
  `projects/remote-job-bootstrap/experiments/20260731T140535Z-raw-image-ssh-ab/`.

Record durable corrections here with date and source pointer. Do not silently preserve disproven claims.

## 2026-07-05 20:30 — petta-chem: 5-rule catalytic cycle scanner

Added 5-rule (quintuple) catalytic cycle scanner to exp01 and exp02, completing the ACS detection breadth progression from pairs through 5-rule cycles. Commit `cfb1be1` pushed to GitHub `main`. Result: 0 active 5-rule cycles across all 120 generated-unplanted family records (40 seeds × 3 families), confirming the conservative zero-active finding extends from pair scanning through 3-, 4-, and 5-rule catalytic cycle scanning. All checks passed: exp00, exp01, exp02, exp03, contract files, py_compile, `git diff --check`, and secret-like scan. SUMMARY.md updated with quadruple and quintuple scan provenance tables.

### 2026-07-06 petta-memory progress
- Added `context_selection_wrapper()` (commit `c219e08`): second near-term inference-control mechanism for pi-PLN. Filters EvidencePackets by domain/cluster/promotion_rule and scores by evidence-weighted relevance before PLN invocation. CLI: `pi-pln-context-select`. 16 new tests, 208 total pass. No runtime, no memory append, no OmegaClaw live path.

### 2026-07-06 03:00 — petta-memory: chained inference-control pipeline

Progress slice in `projects/petta-memory/repos/petta-memory` local commit `e57b6e2` (branch `agent/parser-validation`). Added `chained_inference_pipeline()` in `patham9_pln.py` — the third inference-control mechanism from the trueagi-io/chaining survey. Chains context selection (stage 1: domain/cluster/promotion_rule packet filtering + relevance scoring) with probabilistic filtering (stage 2: EC projection + composite score ranking + confidence/top_k filtering). Original item indices are remapped through the pipeline. CLI: `pi-pln-pipeline`. 17 new tests, 225 total pass; `git diff --check` clean. Non-live, wrapper-only boundary preserved.

## 2026-07-06 specatom-hs progress

- Added dependency depth / critical path length detection to information-flow validation pass.
- Computes longest path in acyclic DataFlowEdge graph via topological sort + DP (Kahn's algorithm).
- Emits `information-flow-dependency-depth-reviewed` obligation: Pass when depth < 4 or acknowledged, Unknown with blocking question when deep and unacknowledged.
- 6 regression tests added; 141 total tests pass; `git diff --check` clean.
- Local commit `d63158f`; not pushed.
# RelaLeap semantics lane pointer (updated 2026-08-12T17:55Z)

- The sole preregistered readiness probe was consumed `NOT_READY`, and its
  intended unprivileged network-unshared topology subsequently proved
  `TRANSPORT_INFEASIBLE` before any process or request. It may not be repaired
  or retried.
- Stage A remains blocked unless one of three exhaustive events occurs: an
  external conforming independent-author bundle, a fresh result-independent
  topology proposal that first passes a model-free preflight, or explicit
  Ben-approved protocol revision. V14 remains sealed, unopened, and
  unconsumed. The latest 2026-08-12 administrative receipt found no such event
  and passed 30 focused plus 357 broader exposed tests without sealed access.
  Contract evidence:
  `projects/relaleap/experiments/20260809T113028Z-frame-oracle-v14-stage-a-unblock-contract-r3/`;
  latest receipt:
  `projects/relaleap/experiments/20260812T175409Z-frame-oracle-v14-quiescent-receipt-20260812-r4/`.
