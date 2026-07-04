# Decisions

## 2026-07-04: Extract as a standalone reusable plugin repo

**Decision:** Package the local `intent-model-router` as `openclaw-intent-model-router`, separate from the OmegaClaw project notebook and local OpenClaw profile.

**Rationale:** Ben asked that the cost-accounting-savvy account/model router live in a GitHub repository with related material needed by other Claw agents. A standalone plugin repo is easier to clone, inspect, and adapt than a slice of a live OpenClaw profile.

## 2026-07-04: Default Fable posture remains fail-closed

**Decision:** Keep default `fableMode=off` and `fableDailyBudgetUsd=0` in the extracted repo.

**Rationale:** Reusable code should not accidentally cause paid Fable/Anthropic calls when installed by another agent. Human-approved config changes should be required before paid escalation.

## 2026-07-04: Do not include local ledgers, secrets, or live OpenClaw config

**Decision:** The public repo includes source, tests, docs, plugin metadata, and specification artifacts only.

**Rationale:** Usage ledgers and local config may reveal operational metadata or credentials. Provider/API setup belongs in each user's local profile or secret store.
