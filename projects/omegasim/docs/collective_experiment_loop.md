# OmegaSim Collective Experiment Loop

Date adopted: 2026-07-02
Scope: local OmegaSim/OmegaHive strange-attractor search on the Pop!_OS OpenClaw workstation.

## Overall goal

Find configurations of simulated OmegaHive agents or multi-OmegaHive communities whose dynamics display relevant strange attractors with complex multilobed grammatical structure.

## Loop protocol

1. **Run one bounded experiment slice**
   - The OmegaSim worker receives a concrete mandate: hypothesis, code/data scope, commands, expected artifacts, and stop conditions.
   - Prefer local execution; no paid compute or external publication without explicit approval.

2. **Post a summary report to the visible channels**
   - Use the dedicated bot-bot scheduled-discussion Telegram channel **ProtoBots-BotBotChats** (`https://web.telegram.org/k/#-5459676079`; candidate OpenClaw target `telegram:-5459676079`, verify once bots/session are visible) for detailed collective-loop discussion between Protocosmobot/ZeroBot and Protomegabot.
   - Continue using **ProtoBots-updates** / scheduled-updates (`telegram:-1003983157420`) for scheduled/progress updates, except the single daily 7AM Pacific summary remains in the main Protobots channel.
   - Also post concise human-facing summaries/directives in the main Protobots channel so Ben can see the loop's outcomes without needing to read every bot-bot turn.
   - Protocosmobot summarizes the run, including:
     - experiment/run path;
     - hypothesis;
     - exact commands/checks;
     - key metrics/plots/artifacts;
     - what passed, failed, or stayed ambiguous;
     - suggested next experiment options.

3. **Short bot discussion**
   - Protomegabot and Protocosmobot/ZeroBot discuss the report for a few turns in **ProtoBots-BotBotChats** once the bots are present and the channel target is verified.
   - Target length: 2-5 dialogue turns.
   - Extend to dozens only if there is genuinely deep scientific/technical uncertainty.
   - Avoid bot echo loops and repetitive status chatter.

4. **New mandate**
   - Protocosmobot writes a concise next mandate from the discussion and sends it to the OmegaSim worker.
   - The worker proceeds without waiting for Ben unless the next step is blocked by approval requirements, ambiguity in scientific objective, destructive actions, repository publication, or paid compute.

5. **Repeat**
   - Keep activity moving with bounded steps rather than long idle pauses.
   - Fail closed scientifically: do not claim appraisal-specific strange attractors unless matched controls are beaten.

## Current next scientific priority

`projects/omegasim/TASKS.md` currently prioritizes matched excess-over-control scoring, then residual-state/lobe discovery beyond role argmax, then denser phase diagrams around appraisal conditions that exceed controls.

## Mandate template

```text
OmegaSim mandate <N>: <short name>
Objective: ...
Hypothesis: ...
Scope: files/experiment dirs allowed to change.
Implement/run: ...
Controls: ...
Artifacts: RUN.md, metrics JSON/CSV, plots if useful, updated TASKS/PROJECT notes.
Verification: tests/py_compile/smoke commands.
Stop when: ...
Report: concise group summary with next-options.
```
