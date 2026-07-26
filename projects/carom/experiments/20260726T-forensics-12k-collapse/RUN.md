# CAROM 12k collapse checkpoint forensics

- Status: complete
- Started: 2026-07-25 (America/Vancouver)
- Finished: 2026-07-25 (America/Vancouver)
- Execution: local CPU only; no remote or paid compute
- Source run: `../20260722T015200Z-carom-gpt2-12k/`
- Code provenance: branch `agent/conversation-governor`, repaired instruments
  commit `975a4c9`
- Research rules: Rule 1 (validate instruments) and Rule 5 (reproducible,
  specific reporting) are controlling.

## Question

When does the compiled-channel controller lose task accuracy, which measured
changes lead or coincide with that loss, and is learning-rate schedule surgery
plausibly sufficient?

## Inputs and validation

The source artifact contains 13 checkpoints: step 0 and steps 1,000 through
12,000. The task wording's isolated “500” conflicts with both the stated count
and preserved inventory and is treated as a typo. Every checkpoint
deserialized on CPU, contained keys `m`, `it`, and `rng`, matched its filename
step, shared an identical 43-tensor schema, and contained only finite values.

The frozen GPT-2 weights are not stored in these checkpoints. The cited
20260719 ePC diagnostic belongs to `projects/relaleap`, not CAROM; its
six-layer terminology and 20--40x Layer-5 claim are background analogy, not
evidence about this run.

## Command

See `command.sh`. Raw stdout/stderr and `/usr/bin/time -v` telemetry are
captured alongside machine-readable metrics.

## Results

### Executive finding

**Observation:** The acute task collapse is between steps 3,000 and 4,000:
source L2--4 accuracy falls from 0.3268 to 0.1667 as OneCycleLR reaches its
approximately 0.002 peak (nominal peak near step 3,600). On the identical
frozen probe, the summed early/late gradient ratio rises from 0.462 to 19.5;
raw individual gradients increase by roughly four to five orders of
magnitude. At step 5,000, several raw group norms reach `1e8`--`3e10`.
Training's global norm clipping kept checkpoint weights finite but concealed
this unstable local sensitivity.

**Inference:** The leading indicators are broad operator-core parameter growth
and itinerary degradation, not a uniquely exploding Layer 5. At step 3,000,
before the accuracy discontinuity, L1/L2 weights are already 4.16/4.21x their
initial norms and L4/L5 are 3.27/3.23x. Repaired first-visit tau falls from
0.961 at step 1,000 to 0.656 at 2,000 and 0.633 at 3,000. The large raw
gradient event is coincident with, rather than clearly preceding, the acute
accuracy collapse at the available 1,000-step resolution.

**Hypothesis:** Rising LR drives the already enlarged recurrent operator into
a high-gain regime. Global gradient clipping allows optimizer steps to remain
finite but cannot preserve their direction. This damages command-to-operator
routing and then leaves the dynamics in a low-dominance, nearly frozen
attractor after step 6,000. The evidence supports schedule-triggered recurrent
instability; it does not identify schedule as the sole structural cause.

### Principal per-checkpoint timeline

All repaired evaluation values use one frozen 128-example L2--4 corpus. `G
E/L` is the summed early-to-late raw gradient-norm ratio. Weight columns are
L2 ratios versus step 0. `r(core)` and `r(traj)` are centered-entropy effective
ranks. Consecutive CKA is for the final recurrent core output. Absolute norms,
all group gradients, participation ratios, all block ranks/CKAs, and source
metrics are in `metrics.json`.

| Step | Source acc | LR | Tau | Classified | Coverage | Edge AUPRC | Pos recall | G E/L | L1 | L2 | L3 | L4 | L5 | Task head | r(core) | r(traj) | Core CKA |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | .1387 | .000080 | .000 | .141 | .186 | .324 | 1.000 | .039 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 35.08 | 2.51 | -- |
| 1000 | .2240 | .000423 | .961 | .884 | .729 | .436 | .000 | .283 | 1.38 | 1.39 | 1.33 | 1.23 | 1.12 | 1.01 | 3.21 | 2.82 | .152 |
| 2000 | .2923 | .001207 | .656 | .644 | .644 | .425 | .000 | .289 | 2.23 | 2.26 | 2.13 | 1.87 | 2.04 | 1.11 | 5.19 | 3.02 | .475 |
| 3000 | .3268 | .001872 | .633 | .582 | .635 | .456 | .000 | .462 | 4.16 | 4.21 | 3.33 | 3.27 | 3.23 | 1.28 | 6.76 | 3.13 | .781 |
| 4000 | .1667 | .001989 | .336 | .759 | .503 | .467 | .000 | 19.47 | 6.47 | 6.43 | 4.85 | 4.73 | 4.01 | 1.40 | 10.34 | 3.05 | .798 |
| 5000 | .1263 | .001866 | .305 | .372 | .482 | .503 | .329 | 6.98 | 8.11 | 8.15 | 6.67 | 6.73 | 4.74 | 1.50 | 12.15 | 3.08 | .674 |
| 6000 | .1823 | .001623 | .055 | .081 | .203 | .503 | .236 | .263 | 8.30 | 8.38 | 6.88 | 6.85 | 4.80 | 1.45 | 11.38 | 2.97 | .909 |
| 7000 | .1842 | .001294 | .000 | .041 | .178 | .512 | .443 | .177 | 8.33 | 8.44 | 6.93 | 6.90 | 4.80 | 1.46 | 10.21 | 3.04 | .959 |
| 8000 | .1875 | .000925 | .000 | .037 | .178 | .532 | .297 | .191 | 8.34 | 8.44 | 6.94 | 6.90 | 4.80 | 1.47 | 10.09 | 2.95 | .995 |
| 9000 | .1914 | .000566 | .000 | .035 | .178 | .554 | .484 | .211 | 8.34 | 8.44 | 6.94 | 6.90 | 4.80 | 1.47 | 10.20 | 2.94 | .997 |
| 10000 | .1947 | .000267 | .000 | .035 | .178 | .571 | .358 | .092 | 8.34 | 8.44 | 6.94 | 6.91 | 4.80 | 1.48 | 10.14 | 2.94 | .996 |
| 11000 | .1855 | .000069 | .000 | .035 | .178 | .583 | .443 | .101 | 8.34 | 8.44 | 6.94 | 6.91 | 4.80 | 1.48 | 10.14 | 2.96 | .998 |
| 12000 | .1888 | ~0 | .000 | .035 | .178 | .585 | .382 | .094 | 8.34 | 8.44 | 6.94 | 6.91 | 4.80 | 1.48 | 10.14 | 2.96 | 1.000 |

Timeline: `timeline.svg`.

### Weight geometry

**Observation:** Growth is broad and ordered: attention query/key reach
8.34/8.44x, value 6.94x, transform 6.91x, and gate (the CAROM-local “L5”)
4.80x. The task head grows only 1.48x and embeddings shrink slightly to
0.94x. Most core growth occurs by step 6,000, after which it plateaus.

**Inference:** The cross-project premise of a unique 20--40x last-layer
explosion is falsified for these CAROM checkpoints. L5 grows, but less than
L1--L4. The frozen GPT-2 weights and its LM head cannot be measured from these
checkpoint files because they are not stored; the trainable CAROM task head is
reported instead.

### Gradient flow

At step 3,000 group norms remain ordinary (L1 `0.17`, L2 `0.15`, L4 `0.36`,
L5 `0.074`, embedding `0.058`). At 4,000 they become L1 `4.9e3`, L2 `4.1e3`,
L4 `4.5e2`, L5 `1.7e2`, embedding `2.9e3`, fitness `1.3e3`, and hyper
`9.5e3`. At 5,000 L1 is `2.8e10`, L2 `7.3e9`, L4 `8.3e9`, embedding
`2.3e10`, and fitness `9.2e9`. By step 6,000 norms return to small values and
the hyper gradient is only `1.4e-4`, falling to roughly `2e-5` thereafter.

**Inference:** This is a transient high-gain event followed by routing
gradient starvation, not a stable U-shaped layer profile. Because checkpoints
are 1,000 steps apart, onset can only be bounded to `(3000, 4000]`.

### Itinerary and edge dynamics

The repaired dominance-aware itinerary begins degrading before the task peak:
tau/classified fraction are `.961/.884` at 1,000, `.656/.644` at 2,000, and
`.633/.582` at 3,000. Tau drops to `.336` at 4,000 and becomes zero by 7,000;
classified fraction is only `.035` thereafter. Coverage similarly settles at
`.178`.

Edge AUPRC does the opposite, improving from `.324` initially to `.585`
finally. Positive recall at the fixed 0.5 threshold is zero through step 4,000
and poorly calibrated thereafter. Thus the legacy ~0.70 edge accuracy was
majority-negative dominated; edge ranking improves, but thresholded graph
recovery and usable itinerary execution do not.

### Representation geometry and drift

There is no rank-one collapse in the recurrent core or trajectory. Core
effective rank starts at 35.1, falls to 3.21 after early training, then rises
to 12.15 at the gradient crisis and stabilizes near 10.1. Trajectory rank
stays near 3.0. Hyper-output effective rank peaks at 2.74 (step 2,000), falls
to 1.28 at 5,000 and 1.16 from 6,000 onward: this is the closest observed
rank-collapse analogue, and it coincides with command-routing starvation.
Core consecutive CKA is lowest early, `.674` across 4,000→5,000, then rises
above `.99` after 7,000, showing that the damaged state becomes nearly frozen.

Scalar edge/entry/fitness outputs have trivially unit rank; these are retained
in raw JSON but should not be interpreted as collapse evidence.

### Correlations and temporal interpretation

With only 13 ordered checkpoints, all correlations are descriptive,
autocorrelated, and non-causal. The strongest meaningful coincident
associations with accuracy are hyper participation ratio (`r=.723`), hyper
effective rank (`r=.747`), repaired tau (`r=.605`), and coverage (`r=.562`).
One-checkpoint lead correlations include negative task-head growth (`r=-.703`)
and L5 growth (`r=-.678`), but broad L1/L2/L4 growth has similar values
(`-.660/-.655/-.621`), so this does not isolate L5. The early/late gradient
ratio has lead `r=-.479`; its decisive spike is coincident at step 4,000.
Edge AUPRC is weakly anticorrelated coincidentally (`r=-.121`), confirming
decoupling from task accuracy.

### Schedule versus structure disposition

**Observation:** The acute discontinuity aligns with peak LR, and the separate
state-restored low-peak continuation from step 3,000 completed without
collapse (source: `../20260726T000748Z-gpt2-schedule-diagnostic/`), although it
did not meet the promotion accuracy target.

**Inference:** Schedule surgery is sufficient to prevent this acute collapse
in the tested warm-start setting. It is not sufficient evidence for reaching
the desired accuracy or L5 generalization. The pre-peak itinerary decline and
3--4x core growth by step 3,000 indicate an underlying gain-control problem.

**Recommendations:**

1. Switch before step 3,000, not at the nominal 3,600 peak. Use a maximum LR
   at or below `1e-3` until a matched calibration shows raw checkpoint-probe
   gradients remain bounded; the already-tested `1e-4` warm continuation is
   the safest evidence-backed setting.
2. Add evaluation at 250-step cadence from 2,500--4,500 in the next local or
   already-approved training design, with **unclipped** per-group gradient
   telemetry recorded before global clipping. Trigger a reduction if any
   group grows >10x its step-3,000 reference or itinerary classified fraction
   falls twice consecutively.
3. Give L1--L4 core parameters a lower LR multiplier (initially 0.25x) or
   freeze them at the switch. Do not target L5 alone: it grows less than
   query/key/transform groups.
4. Add explicit core norm/gain control (groupwise norm penalty, spectral
   constraint, or recurrent Jacobian penalty) and compare it against
   schedule-only control. Global gradient clipping alone did not prevent loss
   of optimizer direction.
5. Calibrate the edge threshold on validation data and gate on AUPRC plus
   positive recall, not raw edge accuracy. Preserve a separate
   dominance/classified-fraction gate because good edge ranking did not
   preserve executable itineraries.

### Limitations

- Single seed and 1,000-step checkpoint spacing prevent causal identification
  or finer onset timing.
- The repaired corpus is deterministic but newly generated; source task
  accuracy is retained separately from repaired-corpus metrics.
- Gradient norms are counterfactual frozen-batch sensitivities, not historical
  training-batch gradients or optimizer states.
- Block activations are instrumented module outputs; the architecture is
  recurrent and does not contain five stacked layers analogous to RelaLeap.

## Reproducibility and artifacts

- Command exit: 0
- Wall time: 37.48 s
- Peak RSS: 1,061,604 KiB
- CPU utilization: 326%
- PyTorch: recorded in `metrics.json`
- Raw metrics SHA-256:
  `d0d639549bae35cd9413a98244732aefb4e49ec8380f8b41fd29dbd5014f5069`
- Timeline SHA-256:
  `62e08f74c42f179320f730ef5cd9187dec6e2f64afda4300ed71d92cffebe043`
- Analysis script SHA-256:
  `397a39f921c399c896e98924f510604be5c96939bf7fcc55e763292ef8f6b54b`
