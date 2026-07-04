# OmegaClaw GoalChainer integration map

- Date: 2026-07-02
- Source repo: `https://github.com/MesTTo/OmegaClaw-GoalChainer`
- Local inspection clone: `projects/omegaclaw/repos/OmegaClaw-GoalChainer`
- Inspected commit: `23f49515b1556ce04981f74bde4b56ee0a4375c6`
- Status: external exploratory source only; no live Protomegabot/OmegaClaw runtime integration has been made.

## What GoalChainer appears to provide

GoalChainer is a goal-aware decision layer for OmegaClaw-like agents. Its advertised pipeline is:

1. parse a natural-language request into evidence signals / Semantic-Hypergraph-style propositions;
2. derive deontic status for candidate actions (`forbidden`, `obligated`, `permitted`);
3. grade action acceptability through PeTTaChainer/PLN-style evidence;
4. apply SNARS-style subjective-logic verdicts and proof/provenance;
5. reconcile individual and collective goal pressures with a MetaMo/OpenPsi/MAGUS motivation layer;
6. expose the selected action as an OmegaClaw directive / claimable task.

The concrete demo domain is incident response: choose between publishing raw logs, publishing a redacted summary, or holding updates. The intended safe recommendation is the redacted summary when sensitive data is present.

## Interfaces relevant to Protomegabot

| Interface | Repo location | Candidate Protomegabot use | Integration posture |
|---|---|---|---|
| Python CLI / library | `src/goal_chainer/cli.py`, `pipeline.py`, `omegaclaw_skill.py` | Non-live decision experiments over bounded text requests | Safe to run as local tests only |
| OmegaClaw skill surface | `integrations/omegaclaw/goalchainer_skill.metta`, `run_in_omegaclaw.metta` | Future `goalchainer-decision`, `goalchainer-motivation`, `goalchainer-directive` tools | Do not load into live Protomegabot without explicit approval |
| PeTTa runtime bridge | `src/goal_chainer/petta_runtime.py` | Reuse local PeTTa/SWI paths already present under `projects/omegaclaw/` | Needs path/env hardening and bounded timeouts before live use |
| PeTTaChainer bridge | `src/goal_chainer/evidence_chainer.py` | Potential bridge from `petta-memory` EvidencePacket/STV exports into acceptability queries | Currently hits the same compile/add stack bottleneck seen in `petta-memory` profiling |
| MetaMo motivation | `src/goal_chainer/motivation.py`, `docs/metamo-integration-plan.md` | Model individual/collective drives and appraisal before task claiming | Useful design pattern; first gate should be one-shot/non-live |
| Directive mapping | `src/goal_chainer/directive.py`, `integrations/prolog/gc_directive.pl` | Turn deontic status into ready/blocked/backlog task state | One local test currently fails; needs diagnosis before adoption |

## Relationship to existing work

- **GGB roadmap:** maps most directly to capacities 2.2 claim/evidence separation, 2.5 architecture proposal, 3.1 multi-step planning, 4.3 shared memory coordination, 5.1 governance boundaries, and 5.5 self-improvement loop governance.
- **`petta-memory`:** can supply bounded, provenance-carrying evidence packets and prompt/index views; GoalChainer could consume selected promoted facts as appraisal/evidence inputs rather than reading live memory directly.
- **PeTTaChainer bottleneck:** local tests with `GOALCHAINER_PETTACHAINER_DIR=projects/petta-memory/repos/PeTTaChainer` reproduce a PeTTaChainer `compileadd` 8 GB stack-limit failure on a small four-rule GoalChainer query, matching the current `petta-memory` profiling concern.
- **OmegaClaw/ThreadKeeper:** GoalChainer's directive output is a candidate upstream task-claim signal, but ThreadKeeper should remain the bounded delegation/record layer; do not let GoalChainer bypass task contracts, allowed paths, quotas, or transcript records.
- **MetaMo/Hyperseed motivation analysis:** GoalChainer fits the suggested separation between appraisal/evidence/context update and decision/task selection, with a bounded feedback law between them. The first implementation should be a crude PLN/heuristic gate, not rigorous self-modification verification.

## Non-live smoke gate proposal

Goal: prove a bounded request can produce a decision payload without touching live Telegram/OmegaClaw runtime state.

1. Pin repo commit and runtime paths.
2. Run offline/unit tests and record pass/fail split.
3. Configure local PeTTa/SWI and PeTTaChainer paths explicitly.
4. Run one demo request through `goalchainer-decision` or equivalent Python API under a timeout.
5. Confirm output includes: ranked actions, deontic status, motivation summary, evidence/proof pointer, and directive/task-state mapping.
6. Feed at most one hand-picked `petta-memory` fixture/export as read-only evidence; no live memory writes.
7. Archive a GGB gate record before any runtime integration discussion.

## Current gate result

Partial intake gate plus bounded harness, not an adoption gate:

- Clone/inspection succeeded at commit `23f49515b1556ce04981f74bde4b56ee0a4375c6`.
- Python source compile passed for `src/goal_chainer/*.py`.
- Default pytest with no runtime env: `22 passed, 8 skipped, 11 failed`; failures are expected path assumptions (`/home/user/Dev/PeTTa`) plus runtime-dependent tests not skipped.
- Pytest with local PeTTa/SWI path and no PeTTaChainer path: `25 passed, 6 skipped, 10 failed`; failures mostly require PeTTaChainer under `/home/user/Dev/PeTTaChainer`; one directive task-state assertion returns no ready task.
- Pytest with local PeTTa/SWI and local `petta-memory` PeTTaChainer path: `25 passed, 6 skipped, 10 failed` after ~133s; PeTTaChainer `compileadd` exceeds SWI `--stack_limit=8g` in the evidence-grading path, and the directive task-state assertion still fails.

## Recommendation

Do not integrate GoalChainer live yet. Treat it as a promising design/prototype source. The first bounded harness now exists, so the next useful slice is to fix or isolate the local deontic/directive runtime seams, then optionally feed one `petta-memory` promoted evidence packet through the same simple acceptability heuristic or a precompiled/minimal PLN path before any OmegaClaw skill is loaded.
