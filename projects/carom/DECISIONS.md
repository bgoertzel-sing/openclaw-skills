# Decision Log

## D-20260724-e0e1-caveated-close-e2

- Date: `2026-07-24`
- Status: `accepted`
- Related run: `experiments/20260720T140710Z-e0-e1-exposure-controlled-r1/`

Close the completed E0/E1 campaign without a redundant paid rerun. Its raw
five-seed fixed advantage and normalization collapse are exploratory because
the deterministic evaluation gate failed due to random initial activity.
Require bitwise deterministic evaluation in E2/E3. Use random inhibition,
mode-specific fitness ablations, and only mode-permutation-invariant E3
penalties. E4 interventions and E5 SHC validation remain closed until a full
five-seed E2/E3 accuracy-plus-trajectory gate passes.

## D-20260723-stochastic-forecast-gate: Replace deterministic branch matching with distributional forecasting

- Date: `2026-07-23`
- Status: `accepted`
- Decision owner: delegated research agent
- Related run: `experiments/20260723T224500Z-stochastic-transition-id-v2/`

V1's augmented deterministic state model improved individual eight-step branch
RMSE only `1.02x` over AR(1), below its `2x` gate. V2 found calibrated
distributional coverage and an oracle/deployable error ratio `0.00472`, while
AdamW mean dynamics passed. Treat unknown future minibatches as stochastic
forcing and assess forecast distributions, not individual future branches.

Do not activate the controller yet. Replace its future activation test with a
separately preregistered distributional calibration and decision-utility gate;
treat sharpness as uncertainty over batches, not a scalar setpoint.

## D-20260719-one-off-gpu: Treat the first GPU run as a bounded mechanism screen

- Date: `2026-07-19`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `TASKS.md`; forthcoming RunPod experiment record

### Context

The supplied sandbox is CPU-scale and single-seed. Ben requested a new project
to try on RunPod as a one-off, explicitly not as a subagent task.

### Decision

Run a bounded GPU mechanism screen locally orchestrated by ZeroBot, with no
subagent delegation. Preserve common-task/common-core comparisons and require
fixed-point residual and itinerant trajectory validity diagnostics.

### Alternatives considered

Launching a large endpoint study immediately; delegating experiment design;
treating raw training accuracy as sufficient evidence.

### Rationale and evidence

The reference plots show that superficially successful training can conceal a
non-convergent fixed-point model, and that a hand-built itinerant channel is a
positive control distinct from free-rho order discovery.

### Consequences

The first remote run is diagnostic and bounded. Promotion to multi-seed or
larger tasks requires a new decision and, if paid, a new cost approval.

### Revisit trigger

Local smoke failure, invalid diagnostics, remote runtime exceeding the bound,
or evidence that the proposed scale cannot answer the mechanism questions.

### Supersedes or superseded by

None.
