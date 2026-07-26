# Decision Log

## D-20260726-gpt2-low-peak-warm-start-and-instrument-gate

- Date: `2026-07-26`
- Status: `accepted protocol; remote execution awaiting approval`

Treat `step_3000.pt` as weights plus Python RNG only. Because AdamW and
scheduler state are absent, label the conservative arm a warm start and never
an exact continuation. Compare 3,000 warm-start updates with a 6,000-update
fresh control under the same normalized `1e-4` peak warmup-cosine schedule.
Provision no paid resource until the exact USD 6 H100 proposal is approved.

Use only the repaired v2/v3 instruments after their constructed-control gate.
Small commutator or switching-growth estimates remain descriptive and do not
license global stability/commutation claims. Step 4 remains blocked on Step-2
schedule evidence.

For controller v6, adopt the 0.25x peak guard as a testable candidate, not an
active policy: v5's forecast was directionally wrong at 91.8% of peak LR and
correct at 9.8%, but two post-hoc checkpoints cannot identify a general
decision boundary.

### Result amendment

The approved H100 run passed the warm-start stability gate but failed
promotion. A `1e-4` warmup-cosine schedule sustained step-3000 weights through
effective update 6,000 (final L2--4 0.3529, tau 0.8398), whereas the archived
high-LR run had collapsed to about 0.22 by that interval. The fresh low-peak
control reached only 0.2122. Treat high LR as the strengthened leading cause,
not proven causally, and use `1e-4` only as a stable warm-start candidate.
Do not promote it as a fresh-training schedule.

## D-20260725-e2-pass-e3-fail-keep-e4-closed

- Date: `2026-07-25`
- Status: `accepted`
- Related run: `experiments/20260725T173639Z-e2-e3-compiled-recurrence-v1/`

Apply the numerical gates prospectively frozen before r2 in
`experiments/20260724T194500Z-e2-e3-gpu-r1/RUN.md`; do not replace them with
thresholds chosen after inspecting the completed campaign.

E2 full passes: its mean paired slot-accuracy advantages over no-workspace,
no-command, and no-position are 0.05583, 0.12529, and 0.10008, with
nonnegative paired differences on 4/5, 4/5, and 5/5 seeds. E3 generic
regularization fails: it loses 0.02725 mean slot accuracy versus E2 full
(allowed loss 0.010) and increases terminal trapping by 0.00332, although
revisit fraction and integrated activity mass pass.

The joint gate fails and E4 remains closed. Reopen only after a newly specified
E3 repair recovers at least 0.01725 mean slot accuracy and removes the observed
terminal-trapping increase without excess revisit or activity exposure.

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
# D-20260725-12k-collapse-forensics: Treat peak-LR instability as trigger, not sole cause

Checkpoint forensics over all 13 preserved GPT-2 compiled-channel controller
states localizes the acute accuracy collapse to `(3000, 4000]`, coincident
with the OneCycleLR peak and a four-to-many-orders raw-gradient crisis. Broad
operator-core growth and dominance-aware itinerary degradation precede it;
L5 is not uniquely explosive. After step 6,000, hyper routing is nearly
rank-one and gradient-starved while core representations become almost
unchanged. Edge AUPRC continues improving and therefore cannot stand in for
executable itinerary quality.

Use an early LR switch (before step 3,000) to prevent the acute collapse, but
do not treat schedule-only repair as sufficient for promotion. Future designs
must test groupwise core gain control, raw pre-clip gradient gates, and
dominance-aware itinerary gates. Evidence:
`experiments/20260726T-forensics-12k-collapse/`.
