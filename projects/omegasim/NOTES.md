# Working Notes

## 2026-07-01 - Project reboot from ProtomegaTron A6 recommendation

Ben asked Protocosmobot/ZeroBot to get OmegaSim going again along ProtomegaTron's suggested direction. Durable prior context says the next simulation should not add generic logistic chaos. Instead, logistic/sigmoid response should be used as bounded thresholded cognitive appraisal over latent motivation, artifact readiness, fatigue/overload, adaptive thresholds, trust/provenance debt, risk, and prediction error.

Implemented first local A6 prototype as a single-hive role-coupled motivational/appraisal model:

- roles: explore, synthesize, review, maintain;
- state: role motivation, fatigue, adaptive thresholds, artifact maturity, provenance debt, risk, prediction error;
- nonlinearities: sigmoid appraisals and softmax action selection;
- history dependence: delayed role coupling, fatigue/recovery, hysteresis, adaptive thresholds;
- controls: linear appraisal and shuffled utilities;
- first metrics: boundedness, role-switch rate, role entropy, short-period tail detection, artifact/risk tail summaries, macro-role tail strings.

This is a harness/proof-of-motion, not yet a strong scientific result.

## 2026-07-01 - A6 functional candidate gate

Added `docs/a6_functional_candidate_gate.md` to preregister stricter candidate criteria before denser sweeps. The gate requires boundedness, nonperiodic macro-role tail, moderate/high entropy, nontrivial switching, artifact tail movement, combined artifact/debt/risk/prediction-error tail movement, and non-collapsed risk.

Reran the 243-condition smoke sweep with the new metrics. Results: appraisal 24/81 functional candidates, linear 37/81, shuffled 2/81. This usefully suppresses shuffled role-noise false positives, but because linear controls still pass more often than appraisal, the result remains fail-closed for appraisal-specific or attractor-like claims. Next technical step is matched excess-over-control scoring.

## 2026-07-02 - Collective-intelligence experiment loop

Ben requested a new operating mode for OmegaSim: after each experiment run, avoid stalling until a human prompt. Instead, use a rolling collective-intelligence loop where Protocosmobot posts a summary report, ProtomegaTron and Protocosmobot discuss next experiments for a bounded few turns, and Protocosmobot gives the next OmegaSim subagent mandate.

The loop's long-horizon goal is to find configurations of simulated OmegaHive agents or multi-OmegaHive communities whose dynamics display relevant strange attractors with complex multilobed grammatical structure. The first mandate under this loop should remain conservative: implement matched excess-over-control scoring for the current A6 harness before making attractor claims or expanding to A7/A8.

## 2026-07-03 - External benchmark directive updated to do both

Ben clarified that OmegaSim should do both external benchmark directions: Mackey-Glass for the closest delayed-coupling analog, and Lorenz-96 for richer high-dimensional/multilobed attractor dynamics. Updated `TASKS.md` and `DECISIONS.md` accordingly. The intended calibration lane is now two-benchmark rather than Mackey-only or Lorenz-only.

## 2026-07-03 - Dedicated bot-bot scheduled-discussion channel created

Ben created **ProtoBots-BotBotChats** for OmegaSim collective-loop bot discussion: `https://web.telegram.org/k/#-5459676079`. Updated the loop protocol and task/decision records to use this dedicated channel for detailed collective-loop discussion between Protocosmobot/ZeroBot and Protomegabot while preserving concise summaries/directives in the main Protobots channel. Continue using ProtoBots-updates / scheduled-updates (`telegram:-1003983157420`) for scheduled/progress updates, except the single daily 7AM Pacific summary stays in main Protobots. Candidate OpenClaw target is `telegram:-5459676079`, pending verification once the relevant bots/session are visible.
