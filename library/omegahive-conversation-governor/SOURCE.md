# A Shared Conversation Governor for OpenClaw, OmegaClaw, and OmegaHive

- Type: architecture and implementation design PDF
- Prepared for: Ben Goertzel
- Document date: 2026-07-24
- Retrieved: 2026-07-24 from the Protobots Telegram group
- Local PDF: `omega_hive_conversation_governor_design_20260724.pdf`
- Extracted text: `omega_hive_conversation_governor_design_20260724.txt`
- SHA-256: `618ae48a8a1eff5bc8614a2602b6d974be0c916ca18d7e2822b3de9acb3028bb`
- Pages: 43
- Access/privacy: private research-workspace source supplied by Ben; do not publish without permission
- Tags: OpenClaw, OmegaClaw, OmegaHive, routing, admission, deduplication, response leases, conversation governance
- Related project: `projects/omegahive-conversation-governor`

## Revision 2

- Title: *A Shared Conversation Governor for OpenClaw, OmegaClaw, and
  OmegaHive — Revised Design*
- Revision: 2, shadow-first deployment and control-plane safety refinements
- Retrieved: 2026-07-24 from the Protobots Telegram group
- Local PDF: `omega_hive_conversation_governor_design_v2_20260724.pdf`
- Extracted text: `omega_hive_conversation_governor_design_v2_20260724.txt`
- SHA-256: `e3799ed4c243c1e51405f7b3c5b8e08ea7cb6e3f1a07de65eb548d86af46e889`
- Pages: 53
- Status: current governing specification; the original 43-page revision is
  retained for provenance

Revision 2 incorporates the accepted review corrections without changing
Phase A's read-only scope:

- centralized, coordinated-local, and weak ingress/egress deployment
  topologies, with placement decided by discovery;
- a cost-ordered governor cascade and explicit overhead accounting;
- task/thread ownership hysteresis;
- a semantic firewall forbidding substantive egress rewriting;
- predeclared activation gates with explicit human approval;
- a first-class human override grammar.

The implementation appendix now has phases A–L. Human overrides and the
semantic egress firewall are a distinct Phase G, before the private review bus.
Semantic deduplication remains late, calibrated, and shadow-only until its
false-silence and net-efficiency gates pass.

## Summary

The document proposes a shared control plane at the common gateway boundary.
Ingress determines whether inference is needed, selects one public owner,
assigns optional private reviewers, chooses context and an output contract, and
issues a response lease. Egress suppresses no-op or duplicate output, validates
leases and contracts, assembles multipart results, and enforces channel policy.

The router action space expands from model selection to `DROP`, `LOG_ONLY`,
`AGGREGATE`, `TEMPLATE`, `CHEAP_MODEL`, `NORMAL_MODEL`, and `DEEP_MODEL`.
Routine workers write structured state rather than directly publishing.
Repeated failures become coalesced incident objects. Compact project snapshots
replace repeated reconstruction of broad chat history.

## Central claims

- Preventing an unnecessary model invocation saves more than merely shortening
  its response.
- Prompt-only coordination cannot enforce shared idempotency, ownership, or
  pre-inference admission.
- One public owner plus bounded private contributors preserves multi-agent
  intelligence without parallel public essays.
- Deployment should progress from baseline instrumentation to shadow decisions,
  deterministic suppression, leases, private review, aggregation, and only
  later semantic novelty/adaptive budgets.

## Limitations and risks

- This is a design, not evidence that the proposed thresholds or classifiers
  have acceptable false-silence behavior.
- The assumed common gateway integration point must be verified against the
  installed OpenClaw/OmegaClaw runtime.
- Hard text suppression patterns require state-aware exceptions.
- Semantic similarity can suppress legitimate disagreement and should begin in
  shadow/advisory mode.
- Private review and event ledgers introduce privacy and retention obligations.

## High-value locations

- Sections 2–3: empirical failure classes, goals, and principles.
- Sections 5–8: architecture, schemas, leases, lifecycle, routing, review bus,
  context, aggregation, and decision procedures.
- Sections 11–13: safety, metrics, and staged deployment.
- Appendix A: implementation phases, acceptance criteria, feature flags, test
  strategy, and suggested commit sequence.
- Revision 2 sections 4, 6.3, 6.6, 6.12, 11, and 13: topology fallbacks,
  ownership hysteresis, governor budgets, semantic firewall, human overrides,
  and activation gates.
