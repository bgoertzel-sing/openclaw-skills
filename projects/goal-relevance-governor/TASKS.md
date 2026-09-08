# Tasks

Use small, testable tasks. Keep the top of each section in priority order.

## Now

- [ ] **Post-VM2 staged upgrade for ZeroBot and the OmegaClaws (Ben,
  2026-08-16).** Deliverable: after the four-bot ASI:Cloud VM2 migration is
  fully accepted, validate and deploy the goal-relevance governor to ZeroBot
  and the OmegaClaw identities using a reversible staged rollout. Acceptance:
  replay/shadow evaluation demonstrates useful detection of idle gaps,
  repeated failed resumptions, and goal-irrelevant work without unsafe
  autonomous retargeting; one staging identity passes first; production
  promotion and rollback evidence exist for each runtime. Next command after
  the migration gate: freeze the current OpenClaw/OmegaClaw runtime baselines
  and specify the minimal JSON graph plus retrospective replay corpus.
  Evidence: future experiment record under this project. Do not start before
  VM2 canary, restart/reboot, rollback, and soak acceptance completes.

- [x] **Completed 2026-08-14 -- revise the design for a broad technical audience (Ben, 2026-08-14
  07:20 PDT).** Deliverable: new ASCII-only LaTeX and compiled PDF that preserve
  the argument while defining or generalizing internal project/tool names,
  especially the chemistry-runtime and bot-recovery examples. Acceptance:
  unfamiliar readers can understand every motivating example without prior
  workspace knowledge; source remains ASCII-only; Tectonic compiles without
  overfull boxes; extracted text and representative pages pass inspection.
  Next command: revise terminology, examples, symbolic illustration, component
  descriptions, and replay-corpus labels. Evidence: updated `docs/` source/PDF,
  build log, extracted text, hashes, and inspection images under `artifacts/`.
  Result: 17 pages and 7,031 extracted words; ASCII and Tectonic checks passed
  with no overfull boxes; pages 1, 3, 4, and 13 passed visual inspection. PDF
  SHA-256: `e010e3785d8c36821882de5f76f66125e64d98c45f1099d15746d7660861dc8f`.

- [x] **Completed 2026-08-14 -- revise the design with stage-sensitive result contracts.** Deliverable:
  update the existing ASCII-only LaTeX/PDF to formalize decision-relevant
  first results, an Occam/least-commitment heuristic, mature-result efficiency,
  project kinds and maturity stages, minimum-sufficient hardening, and
  probability-weighted shortcut debt. Include the observed premature research
  hardening and over-engineered Omega recovery examples. Acceptance: source
  remains ASCII-only, Tectonic builds without overfull boxes, extracted text
  and representative visual inspection pass, and new hashes are recorded.
  Next command: patch the motivation, control structure, LLM, symbolic, and
  validation sections. Evidence: revised `docs/` source/PDF and `artifacts/`.
  Result: 16 pages and 6,661 extracted words; ASCII check passed; Tectonic
  exited 0 with no overfull boxes; pages 1, 6, 8, and 16 passed visual
  inspection. PDF SHA-256:
  `b12861eb95bdcd3c050d56e11b21702794fb4a7e1d38ac914bf9783694dc2dd3`.

- [x] **Completed 2026-08-14 -- write and compile the goal-relevance-governor design.** Deliverable:
  ASCII-only LaTeX source and readable PDF covering motivation, concrete local
  failures, broader failure classes, graph model, review triggers, operational
  verdicts, Deliberation Rooms integration, LLM-centric OpenClaw form, and
  symbolic Atomspace/PLN form. Acceptance: source has no non-ASCII bytes,
  LaTeX builds cleanly, extracted text is substantive, representative pages
  pass visual inspection, and SHA-256 is recorded. Next command: draft
  `docs/goal_relevance_governor_design_2026-08-14.tex`. Evidence: source, PDF,
  build log, text extraction, and inspection images under `docs/`/`artifacts/`.
  Result: 12-page, 4,830-word extracted document; ASCII check passed;
  Tectonic exited 0 with no overfull boxes; pages 1, 7, and 12 passed visual
  inspection. PDF SHA-256:
  `6f9ff19a3f54f77835510afb98f8c010a483af1ea4ecdf6d5a09042a0859ca24`.

## Next

- [x] Specify a minimal JSON graph schema and read-only relevance verdict.
- [x] Build a retrospective replay corpus from recent alignment failures.

## Waiting or blocked

- [ ] Live enforcement - blocked on replay/shadow validation and explicit Ben
  approval - Ben/ZeroBot - 2026-08-14

## Someday or exploratory

- [x] Map the schema into Atomspace/MeTTa and PLN evidence propagation. (2026-09-08: graph_to_metta.py + pln_propagation.py + 34 tests, all 5 replay episodes cross-validated PLN==Python evaluator)

## Done recently

Move durable conclusions into `PROJECT.md`, `DECISIONS.md`, or experiment results rather than relying on this list.
