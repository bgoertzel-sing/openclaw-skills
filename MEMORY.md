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
- Telegram routing preference from Ben (2026-07-02, updated 2026-07-27):
  - Retire routine textual use of ProtoBots-updates / scheduled-updates (`telegram:-1003983157420`). Persistent workers may continue silently; give one concise daily update per project in main Protobots, with more frequent updates only when Ben asks. Exceptional failure alerts may remain fail-safe while routing is consolidated.
  - Collective-loop bot-bot discussions between ProtoCosmoBot/ZeroBot and ProtoMegaBot → dedicated `ProtoBots-BotBotChats` channel (`telegram:-5459676079`), created by Ben 2026-07-03.
  - Daily bot-bot project discussions: every active/idea research or engineering project should get a once-daily scheduled discussion in `ProtoBots-BotBotChats`; trigger immediately on pivots, major status changes, or major problems; suppress the scheduled duplicate if such a discussion occurred within the previous 24h; automatically apply this protocol to newly launched ongoing projects.
- Frontier expert review protocol (2026-07-27): use a self-contained systematic project PDF plus the most relevant original PDFs; first query the frontier model only for goal-relative diagnosis, theoretical/mathematical explanation, changed beliefs, missing controls, and strategic dead ends. Adjudicate/freeze that diagnosis, then use a separate query to request a revised coding-agent plan with gates. Single-pass “review and propose next steps” prompts are deprecated. Canonical protocol: `catalog/FRONTIER_EXPERT_REVIEW_PROTOCOL.md`.
- For project repositories created under Ben's GitHub, use the same local Git commit identity as `petta-chem`: `Benjamin Goertzel <ben@singularitynet.io>`.
- For code repositories created by this agent for Ben, use the MIT License by default unless Ben specifies otherwise.
- For long-running subagent/project threads, make regular Git commits as backup/provenance after each tested coherent slice; push interim commits to already-approved GitHub remotes/branches when safe. Ask once before first publication when owner/name/visibility/remote policy is not yet approved.
- Model policy (clarified 2026-07-19): Default model for all OpenClaw and OmegaClaw agents/subagents is `openrouter/moonshotai/kimi-k3` (Kimi K3 via OpenRouter). It is ~3x the cost of GLM-5.2 but near Fable/Sol quality. K3 is the routine default, not the expert-review ceiling: use `anthropic/claude-fable-5` or `openai/gpt-5.6-sol` for expert review and the deepest or hardest technical reasoning even when K3 is available. If K3 fails, use `openrouter/z-ai/glm-5.2` for simple/chat tasks and `openai/gpt-5.6-terra` or `anthropic/claude-opus-4-8` for more in-depth work. Do not revert routine traffic to GLM-5.2 merely because it is cheaper.
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

## Corrections and retired beliefs

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
