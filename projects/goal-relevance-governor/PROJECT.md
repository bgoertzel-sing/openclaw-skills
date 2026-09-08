# Goal Relevance Governor

- Slug: `goal-relevance-governor`
- Status: `active`
- Created: `2026-08-14`
- Last reviewed: `2026-09-08`
- Owner: Benjamin Goertzel

## Purpose

Design and validate a cross-project means--ends control layer that keeps
OpenClaw/OmegaClaw tasks aligned with Ben's current top-level goals, detects
stale or blocking work, and escalates consequential ambiguity into OmegaHive
Deliberation Rooms.

## Success criteria

- An ASCII-only LaTeX design and compiled PDF explain the motivation,
  architecture, concrete history, LLM-centric incarnation, and symbolic/PLN
  incarnation.
- A later minimal typed graph and read-only evaluator correctly flag selected
  historical alignment failures without excessive false positives.
- The graph/evaluator remains independent of the deliberation transport and
  reasoning substrate.

## Scope

### In scope

- Goals, intermediate goals, tasks, resources, evidence, typed relations,
  priorities, relevance review triggers, verdicts, and authority boundaries.
- Integration with committed OmegaHive state and wake-based Deliberation Rooms.
- LLM-centric and Atomspace/PLN-oriented realizations.
- Retrospective validation against observed failures.

### Out of scope for now

- Live autonomous pausing/retargeting of workers.
- Replacing ThreadKeeper, GoalChainer, Deliberation Rooms, or the Conversation
  Governor.
- Production runtime integration before shadow/replay validation.

## Current state

Ben proposed the graph-centered process on 2026-08-14 after several concrete
failures of global task alignment. Deliberation Rooms provide a complementary
review surface but not the relevance-control state or evaluator. Immediate
work produced a 17-page reviewable design document (Revision 3).

The minimal JSON graph schema (v0.1) and a read-only relevance evaluator are
complete. The evaluator implements six verdict rules (STOP_STALE,
PAUSE_RECOVERABLY, DEFER, REPLAN, ESCALATE, CONTINUE) over a typed
goal/task/resource/constraint graph. A retrospective replay corpus of five
episodes from real alignment failures has been built and validated:
all five produce the expected verdicts.

No live enforcement is authorized. Ben directed on 2026-08-16 that both
ZeroBot and the OmegaClaws should be upgraded to the governor after the
ASI:Cloud VM2 migration is complete. The migration's repeated short-lived
build resumptions and idle gaps are an explicit retrospective replay case.
This authorizes planning and staged validation after migration acceptance,
not live enforcement during migration.

### Phase 0 deliverables (completed 2026-09-08)

- `schema/graph-schema-v0.1.md` — human-readable schema specification
- `schema/graph-schema-v0.1.json` — JSON Schema for graph validation
- `evaluator/relevance_evaluator.py` — read-only evaluator, pure Python, no deps
- `replay_corpus/episode_01_stale_codegen.json` — STOP_STALE (Plain2MeTTa)
- `replay_corpus/episode_02_chem_blocking.json` — PAUSE_RECOVERABLY (petta-chem)
- `replay_corpus/episode_03_premature_hardening.json` — DEFER (research infra)
- `replay_corpus/episode_04_overengineered_repair.json` — REPLAN (agent repair)
- `replay_corpus/episode_05_control_justified_long_running.json` — CONTINUE (WMTM)
- `replay_corpus/validate_corpus.py` — validation harness (5/5 pass)

## Repositories

| Role | Remote | Local path | Branch/default | Pinned/reference commit |
|---|---|---|---|---|

## Environments

Document local virtual environments, containers, toolchain pins, datasets, and remote resources without credentials.

## Key results

- Deliberation Rooms source: `library/omegahive-deliberation-rooms/SOURCE.md`.
- Design document: `docs/goal_relevance_governor_design_2026-08-14.tex` and
  `.pdf`. Revision 3 retains the project-kind and maturity-stage semantics and
  rewrites internal examples for a broad technical audience: products are
  defined on first use, motivating incidents are stated generically before
  internal names, the symbolic example uses generic task/resource names, and
  existing components are described by function. Revision 2 added
  stage-sensitive result contracts, minimum-sufficient hardening, and explicit
  first-result versus mature-result tradeoffs. Revision 3 is 17 pages with
  7,031 extracted words. The source is ASCII-only; Tectonic compilation has no
  overfull boxes, and extracted-text plus representative-page visual checks
  passed. PDF SHA-256:
  `e010e3785d8c36821882de5f76f66125e64d98c45f1099d15746d7660861dc8f`.

## Open questions

## Related projects and concepts

- `projects/omegahive-conversation-governor`: conversation admission/egress,
  distinct from task/goal relevance.
- `projects/omegaclaw`: future GoalChainer/Atomspace/PLN integration target.
- ThreadKeeper: durable task and event lifecycle substrate.
- OmegaHive Deliberation Rooms: strategic discussion and committed synthesis.

## Risks

- Bureaucratic overhead can exceed the value of alignment checks.
- An LLM evaluator may invent causal links or overstate confidence.
- A scalar priority score can erase lexicographic safety/urgency constraints.
- Premature autonomous enforcement can pause valuable work incorrectly.
