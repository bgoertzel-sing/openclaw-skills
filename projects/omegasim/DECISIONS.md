# Decisions

## 2026-07-01: Start with A6 thresholded-appraisal single-hive model

**Decision:** Reboot OmegaSim locally with an A6 single-hive role-coupled motivational/appraisal simulation before A7 semantic fields or A8 multi-hive artifact rings.

**Rationale:** The strongest recent feedback is that queue-centric negative results do not test OmegaHive-like cognition well. A6 is the smallest useful model that puts sigmoid/logistic nonlinearities where they cognitively belong: bounded appraisal and action selection over latent motivational, artifact, fatigue, risk, provenance, and prediction-error variables.

**Alternatives:**

- Add generic chaotic/logistic maps to queues: rejected for now as decorative chaos injection.
- Jump directly to A7/A8: deferred until A6 has a reproducible harness and control comparisons.

## 2026-07-01: Keep A6 fail-closed until appraisal exceeds matched controls

**Decision:** Do not treat A6 role-switching or absolute functional movement thresholds as evidence of an appraisal-specific cognitive regime unless matched controls are weaker under comparable amplitude/state-movement criteria.

**Rationale:** The first stricter functional gate reduced shuffled-control false positives but linear controls still passed more often than appraisal controls. This means the metric/model surface is not yet discriminating appraisal-specific structure.

**Next implication:** Add excess-over-control scoring before denser phase diagrams, A7/A8 extension, or attractor-like language.

## 2026-07-03: Mackey-Glass and Lorenz-96 as external benchmarks for the detection pipeline

**Decision:** Do **both Mackey-Glass and Lorenz-96** as external benchmarks for the OmegaSim detection pipeline.

**Directive from Ben, 2026-07-03:** "We should do both" — following the Mackey-Glass refinement and the earlier Lorenz-96 recommendation.

**Rationale:**
- Mackey-Glass is a single-delay nonlinear system with well-documented bifurcation to chaos — the closest structural analog to OmegaSim's delayed-coupling dynamics.
- The detector must recover known delayed-dependence structure under matched controls; Mackey-Glass provides clean ground truth for this.
- Lorenz-96 adds a complementary high-dimensional/multilobed chaotic attractor benchmark, testing whether the pipeline generalizes beyond single-delay dynamics.
- Both systems are easy to simulate locally and reproducibly with no heavy dependencies.
- Vary Mackey-Glass delay/coupling and Lorenz-96 dimension/forcing/coupling to create clean phase diagrams from simple to complex regimes.
- Lorenz-63/Rössler remain optional sanity checks if a simpler classic-attractor baseline is useful.

**Scope:** Calibrate the residual/null analyzer and any attractor-detection machinery against multiple known external chaotic systems before applying it to OmegaHive-generated traces. This is distinct from the internal A6/A7/A8 OmegaHive simulation work — it is detector calibration against ground-truth dynamics.

**Next implication:** The collective experiment loop should incorporate a two-benchmark calibration lane. First implement dependency-free Mackey-Glass and Lorenz-96 generators, sweep their core parameters, and test whether the existing detector pipeline recovers known delayed-dependence and high-dimensional attractor structure under matched controls.

## 2026-07-02: Use a rolling collective-intelligence loop for OmegaSim

**Decision:** Run OmegaSim experiments as an ongoing loop rather than one-shot subagent tasks that stall after each result.

**Protocol:** After each experiment completes, Protocosmobot summarizes the result in the shared channel. ProtomegaTron and Protocosmobot then discuss next experiments for a bounded few dialogue turns--normally a few, rarely dozens only if something deep is being resolved. Protocosmobot then issues the next concrete mandate to the OmegaSim worker.

**Overall goal:** Find configurations of simulated OmegaHive agents or multi-OmegaHive communities whose dynamics display relevant strange attractors with complex multilobed grammatical structure.

**Guardrails:** Keep claims fail-closed against controls; avoid generic chaos injection; preserve experiment records and project notes; do not use paid/remote compute without explicit approval.

**Immediate next implication:** Start the next loop iteration with excess-over-control scoring for the current A6 harness, because existing functional-gate results are not yet appraisal-specific.

## 2026-07-03: Route collective-loop discussion to a dedicated bot-bot channel plus main summaries

**Decision:** Use the dedicated bot-bot scheduled-discussion Telegram channel for detailed collective-loop discussion between Protocosmobot/ZeroBot and Protomegabot; keep concise visibility summaries/directives in the main Protobots channel.

**Directive from Ben, 2026-07-03:** "Let's make a dedicated bot-bot scheduled-discussion channel" after agreeing that the loop should be visible in both a dedicated channel and the main Protobots summary layer.

**Rationale:** A dedicated channel keeps extended Protomegabot/Protocosmobot discussion inspectable without dominating the main Protobots chat. Main-channel summaries keep Ben aware of outcomes, directives, and blockers.

**Channel:** Ben created **ProtoBots-BotBotChats** on 2026-07-03: `https://web.telegram.org/k/#-5459676079`. Candidate OpenClaw target: `telegram:-5459676079`; verify routability once the relevant bots/session are visible.

**Next implication:** Add the relevant bots if not already present, verify the stable OpenClaw session/channel target, then route future detailed collective-loop bot discussion there while keeping concise outcome summaries/directives in main Protobots. Continue using ProtoBots-updates / scheduled-updates (`telegram:-1003983157420`) for scheduled/progress updates, except the single daily 7AM Pacific summary stays in main Protobots.


## 2026-07-03: Pause OmegaSim until CLA is robust

**Decision:** Pause OmegaSim implementation as the active lane until the Chaos Language Algorithm or an equivalent detector is working robustly.

**Directive from Ben:** CLA is now the new project lane; OmegaSim should resume only after CLA can help detect whether simulated OmegaHive dynamics have complex strange-attractor structure.

**Rationale:** Without a reliable grammar-of-attractors detector, OmegaSim experiments risk producing traces that cannot be evaluated for the intended complex strange-attractor property.

**Next implication:** Do not run further OmegaSim expansion as the main lane. Focus first on CLA implementation and benchmark it on known strange attractors of varying dimensionality; defer very high-dimensional vectors until dimension reduction is designed.
