# Independent technical review: CAROM frozen-GPT-2 12,000-update experiment

**Reviewer:** Sol  
**Date:** 2026-07-22  
**Evidence reviewed:** `carom_gpt2_12k_detailed_results_2026-07-22.pdf`; the experiment ledger; `artifacts/results/summary.json`; training and intervention logs; retained checkpoints; and the GPT-2 runner/model source in `projects/carom/experiments/20260722T015200Z-carom-gpt2-12k/`.

## Executive assessment

The run establishes a real optimization failure, but it does not uniquely identify its cause. The useful solution present at step 3,000 was destroyed between steps 3,000 and 5,000, coincident with the high-learning-rate portion of a OneCycle schedule stretched from 4,000 to 12,000 updates. Schedule-induced displacement is therefore the leading explanation. It remains an inference because duration, schedule, minibatch sequence, and optimization history were not independently controlled.

A second important finding is that the report overstates what the approximately 0.70 edge accuracy means. For a directed chain of length \(L\), only \(L-1\) of the \(L(L-1)\) off-diagonal live pairs are positive, so an all-negative classifier has accuracy \(1-1/L\): 0.50, 0.667, or 0.75 for lengths 2, 3, or 4. The reported mixed-length edge accuracy near 0.70 is therefore plausibly a majority-class baseline, not evidence that dependency prediction was “already solved” or survived the collapse. The edge result needs balanced accuracy, precision/recall, PR-AUC, tie-correct ROC-AUC, calibration, and positive-rate reporting before it can localize the failure downstream of the edge head.

The best evidence for order-dependent execution occurs at step 3,000, but its magnitude is the **forced-correct minus shuffled gap of 0.0306**, not the natural-minus-shuffled gap of 0.0801. Natural and clamped trajectories differ in amplitude, dwell, smoothness, and switching dynamics as well as order. Forced and shuffled trajectories are more closely exposure-matched and therefore form the cleaner, though still imperfect, ordering contrast. This run supports the narrower conclusion that the learned natural dynamics contributed to endpoint behavior around step 3,000. It does not establish learned commutation, a correctly compiled dependency graph, a heteroclinic mechanism in the dynamical-systems sense, or robust compositional extrapolation.

For the next optimization attempt, I recommend **resuming the earlier successful 4,000-update checkpoint**, not the failed 12,000-update endpoint. Use a small continuation LR and strict validation-based stopping. In parallel, a short fresh-run schedule-control experiment should be used to test the causal LR hypothesis. Resume is the economical path toward higher accuracy; fresh runs are the proper path for causal attribution.

## 1. What was directly observed

The following are observations from the retained fixed-corpus evaluations:

- Frozen L2–4 slot accuracy rose from 0.1387 at initialization to 0.3268 at step 3,000, then fell to 0.1667 at step 4,000 and 0.1263 at step 5,000. It ended at 0.1888.
- Training loss reported on the checkpoint minibatch was lowest at step 3,000 (1.781), increased to 2.394 at step 4,000 and 3.192 at step 5,000, and never returned to its step-3,000 level.
- The 12,000-step OneCycle schedule was still rising at step 3,000 (\(\mathrm{LR}=1.872\times10^{-3}\)) and was near its \(2\times10^{-3}\) peak at step 4,000.
- From steps 3,000 to 6,000, itinerary coverage fell from 0.7275 to 0.5094, exact-order frequency from 0.3320 to 0.1406, transition recall from 0.4479 to 0.1829, and \(\tau\) from 0.9870 to 0.4128. These later stabilized at still lower values.
- At step 3,000, natural, forced, shuffled, and smeared accuracies were 0.3268, 0.2773, 0.2467, and 0.2630. At step 4,000 they were nearly indistinguishable.
- L5 accuracy peaked at 0.2617 at step 3,000 and then collapsed. Increasing recurrent integration from 72 to 100 or 120 steps did not rescue it at any checkpoint.
- Final L2–4 accuracy of 0.1888 is only modestly above the per-slot random baseline of \(1/8=0.125\). The step-5,000 result, 0.1263, is essentially at that baseline.
- The earlier independently trained 4,000-step GPT-2 endpoint achieved 0.412 L2–4 accuracy and a 0.115 natural-minus-shuffled gap, materially outperforming every checkpoint from this run.
- The automatic evaluator initially failed due to a corpus-unpacking error. The repaired intervention-only pass evaluated retained checkpoints without retraining; this failure does not explain the learned weights.

## 2. Ranked diagnosis of the collapse

### 1. Stretched OneCycle schedule and excessive peak LR — most plausible

**Evidence:** The best retained solution occurs at step 3,000 while LR is still rising. Accuracy and loss degrade abruptly as LR approaches its maximum around step 3,600. In the successful 4,000-update schedule, the LR had already fallen to approximately \(5.65\times10^{-4}\) by step 3,000 and was essentially zero by step 4,000. The timing is highly specific, and late annealing fails to restore the displaced solution.

**Inference:** Updates near \(2\times10^{-3}\) moved one or more sensitive recurrent-routing parameter groups out of the useful basin. Because the model has a long noisy recurrent computation and nonlinear compiled inhibition, a nominal LR that is tolerable early may be destructive after useful routing and operator structure has formed.

**Why not proven:** There is no same-seed control that preserves the 4,000-step LR trajectory while continuing training, no lower-peak 12,000-step control, and no parameter-distance or gradient telemetry identifying the damaging update.

### 2. Joint-objective and parameter-group imbalance — plausible and probably interacting with LR

The objective combines slot cross-entropy, masked edge BCE with weight 1.0, and entry cross-entropy with weight 0.2. A single optimizer and LR are used for the edge compiler, entry head, hypernetwork, operator core, state embeddings, GLV-related routing components, and output decoder.

The edge BCE is computed with a zero-valued mask passed as `weight` under the default mean reduction. Its denominator still includes masked tensor elements, making its effective scale dependent on tensor dimensions and live-length composition rather than explicitly normalizing over live pairs. No per-loss values or per-group gradient/update norms were recorded. Global norm clipping at 1.0 can also allow one component’s gradients to determine the rescaling applied to every group.

**Inference:** High LR plus unequal or changing gradient scales could preserve or improve a cheap auxiliary statistic while damaging routing and endpoint execution. This is at least as plausible as a clean “edge head survived; downstream failed” decomposition.

### 3. Recurrent dynamical instability or parameter sensitivity under high-LR updates — plausible

The model backpropagates through 72 noisy GLV/workspace steps. Activity is clamped to \([0.05,4.0]\), and fixed constants control inhibition, leakage, fatigue, and integration. Small changes to edge logits, entry scores, hypernetwork outputs, or workspace dynamics can therefore cause discontinuous itinerary changes.

The concurrent deterioration in endpoint accuracy, dwell/coverage, and intervention effects is compatible with dynamical destabilization. No activity distributions, saturation rates, inhibition spectra, routing entropy, state/update norms, or local stability diagnostics were logged, so the affected subsystem cannot be identified.

### 4. Seed-specific optimization bifurcation or stochastic trajectory — live alternative

Only seed 0 was run. Training includes fresh procedurally generated examples and injected activity noise. A one-seed transition cannot show that the high-LR schedule reliably causes collapse, nor distinguish deterministic schedule risk from an unlucky stochastic crossing.

The existence of a better, separately trained 4,000-step result makes seed/minibatch-history effects especially relevant.

### 5. Misweighted or insufficiently informative graph supervision — plausible confound

Approximately 0.70 raw edge accuracy is consistent with predicting the majority negative class. Consequently, the claimed preservation of graph prediction may be an evaluation illusion. If the compiler never learned calibrated positive edges, trajectory quality could depend on incidental logit geometry that high-LR training later altered without much change in threshold accuracy.

This is a diagnostic confound rather than a complete explanation of the abrupt loss spike.

### 6. Training/evaluation mismatch — possible but less supported as the main collapse cause

The online evaluator consumes the training RNG and uses a changing corpus, whereas the repaired panel uses fixed corpora. Evaluation also runs the model without training-time activity noise. These differences complicate comparisons, but the collapse appears in both online telemetry and the fixed panel, so mismatch alone is unlikely to explain it.

### Causes not supported by the current evidence

- **Insufficient inference time:** Unsupported as the primary cause; 100–120 recurrent steps did not rescue L5.
- **GPT-2 representation degradation:** GPT-2 was frozen, so its weights did not degrade. The trainable adapter/compiler can still become poorly matched to those representations.
- **Catastrophic loss of edge prediction:** Not established because raw edge accuracy is class-imbalanced and inadequately characterized.
- **Simple overfitting from additional examples:** Possible in a broad sense, but the sudden failure near peak LR and the procedurally generated stream favor optimization instability over classical memorization-based overfitting.

## 3. Critique of the report and missing diagnostics

The report is strong in provenance, checkpoint retention, epistemic labeling, explicit failure reporting, and acknowledgement that schedule and duration were confounded. Its central LR hypothesis is reasonable. The following issues should be corrected or emphasized before preservation as the definitive scientific interpretation.

### Edge accuracy is not interpretable as reported

The report says edge prediction “survived” and uses this to localize damage downstream of graph prediction. Raw accuracy near 0.70 cannot support that conclusion because positives are sparse.

Required additions:

- positive prevalence and predicted-positive rate by program length;
- confusion matrices;
- positive-class precision, recall, F1, and balanced accuracy;
- tie-correct ROC-AUC and preferably PR-AUC;
- calibration/Brier score or reliability bins;
- exact-chain recovery and per-example edge-set F1;
- a constant-negative baseline;
- evaluation separated by L=2, 3, and 4.

### Endpoint accuracy should be stratified and uncertainty quantified

The L2–4 aggregate mixes different depths and treats all six slots as separate observations even though slots within an example are dependent. Report:

- accuracy by program length;
- exact-sequence/example accuracy in addition to slot accuracy;
- paired bootstrap confidence intervals resampling examples, not slots;
- per-primitive and paraphrase-variant performance;
- accuracy on changed versus unchanged slots;
- paired checkpoint differences on the same corpus.

The aggregate \(n=256\) panel is adequate for screening but weak for small gaps such as 0.022 or 0.031 without paired uncertainty.

### “Causal gap” naming and interpretation need refinement

The JSON’s `causal_gap` is forced-minus-shuffled, while the report’s main “gap” column is natural-minus-shuffled. These answer different questions.

- **Forced minus shuffled** is the closer test of order under matched rectangular amplitude/dwell construction.
- **Natural minus shuffled** changes order, smoothness, amplitude, dwell, switching transients, and potentially total operator exposure.

At step 3,000 the forced-minus-shuffled effect is 0.0306, much smaller than natural-minus-shuffled 0.0801. The latter shows dependence on the natural trajectory as a whole, not specifically on correct order. Report both with paired confidence intervals and avoid calling natural-minus-shuffled an order effect.

The shuffled condition also uses one deterministic shuffle draw per example. Multiple independent shuffles or exhaustive permutations for short programs would reduce Monte Carlo noise.

### The intervention construction does not exposure-match natural dynamics

All clamped modes use amplitude 1.5 and piecewise-constant equal dwell. The natural activity does not. The equality of forced, shuffled, and smeared outcomes at many late checkpoints could mean that execution is insensitive to their differences, but it could also mean all three clamped trajectories are similarly out of distribution.

Required diagnostics:

- total and per-command integrated activity;
- workspace update norm per recurrent step;
- dwell and amplitude distributions;
- a replay condition preserving the natural amplitude/dwell trace while permuting command identity;
- a forced trajectory matched to natural total exposure;
- trajectory interpolation rather than only hard replacement.

### Optimization telemetry is inadequate

The printed “loss” is one stochastic training minibatch at each checkpoint, not a fixed validation loss or an epoch average. No component losses were retained.

At least every 100 updates around the vulnerable interval, log:

- fixed-corpus total, task, edge, and entry losses;
- unclipped and clipped global gradient norm;
- per-parameter-group gradient and update norms;
- fraction of steps clipped;
- parameter norms and distance from the best checkpoint;
- activity clamp rates;
- routing entropy and operator usage;
- edge-logit positive/negative distributions;
- NaN/Inf and activation maxima.

Without these, “high LR destabilized routing” remains a temporal story rather than a subsystem diagnosis.

### Checkpoint cadence was too coarse near the event

The destructive transition occurred between 3,000 and 4,000, but checkpoints were 1,000 updates apart. At roughly 0.88 seconds/update, the scientific uncertainty spans almost 15 minutes and a large number of optimizer steps. A 100- or 200-step cadence from 2,000 through 5,000 would substantially improve diagnosis at little storage cost.

### Resume fidelity is incomplete

The 12,000-run checkpoints contain model weights, iteration number, and Python RNG state, but not optimizer or scheduler state. The earlier source format saved optimizer and scheduler state; the retained 12,000 format does not. A “resume” from these files is therefore a warm start with reset Adam moments, not an exact continuation. Future checkpoints should include optimizer, scheduler, Torch CPU/CUDA RNG states, generator RNG state, and version/config hashes.

### The 4,000-step comparison is not a controlled counterfactual

The earlier 4,000 result differs in training trajectory and probably stochastic history. It is useful context, not a same-initialization ablation. Likewise, TinyLM differs in encoder and associated optimization geometry. Neither comparison isolates the cause of collapse.

### L5 evidence is correctly negative but mechanistically limited

The absence of improvement at 100 or 120 steps makes “simply needs more settling” unlikely for these checkpoints. It does not establish that integration depth is irrelevant in general: the trained model saw 72 steps, and extending a learned dynamical system out of distribution can itself degrade behavior. Training-depth randomization or truncated/unrolled-depth controls would be needed to infer adaptive computation.

## 4. Ordered, cost-efficient experiment ladder

All stages should use a **frozen, versioned validation set distinct from the final test set**. Validation may drive stopping and model selection; the current seed-1234/5678 panels should become test panels or be replaced after having already influenced analysis.

Recommended fixed sets:

- Validation L2–4: 1,024 examples, seed 2234, stratified equally by L=2, 3, 4.
- Validation L5: 256 examples, seed 6678.
- Final test L2–4: 2,048 examples from a new unrevealed seed.
- Final test L5: 512 examples from a new unrevealed seed.
- Report example-level paired bootstrap 95% intervals with 10,000 resamples.

### Stage 0: checkpoint-only diagnostics — no retraining

Evaluate the successful prior 4,000 checkpoint and the 12,000-run steps 2,000, 3,000, 3,500 if available, 4,000, 5,000, and 12,000. If only the retained 1,000-step grid exists, use it.

Add:

- balanced edge metrics and positive-rate calibration;
- per-length endpoint and exact-example accuracy;
- per-example forced/shuffled differences over at least 16 independent shuffles;
- natural-exposure-matched forced and shuffled replay;
- activity mass, dwell, clamp rate, routing entropy, operator exposure, and workspace-update norms;
- repaired v3 swap/JVP probes only after their positive/negative controls pass.

**Gate:** Do not alter edge-loss weighting or freeze the edge head unless calibrated diagnostics show it is genuinely learned. Do not use mechanistic probe outputs unless constructed controls pass.

### Stage 1: cheap warm-start continuation from the successful 4,000 checkpoint

This is the recommended next optimization run.

- Initialization: earlier GPT-2 4,000-step checkpoint with L2–4 accuracy 0.412.
- Optimizer: AdamW, **fresh state**, explicitly reported as a warm start.
- LR: constant \(1\times10^{-4}\) for all trainable parameters.
- Weight decay: \(1\times10^{-4}\).
- Batch: 64.
- Additional updates: maximum 2,000.
- Gradient clip: 1.0.
- Keep all existing loss weights initially: task 1.0, edge 1.0, entry 0.2.
- Validate every 100 updates.
- Save model/optimizer/scheduler/RNG state every 100 updates.
- Run the full intervention panel every 500 updates; use the cheaper endpoint/edge/activity panel every 100.

**Primary early-stop rule:** Stop if validation L2–4 accuracy is at least 0.03 below the best-so-far value at three consecutive evaluations and the best has not improved by at least 0.01 over the preceding 500 updates.

**Safety stop:** Stop immediately for non-finite values, unclipped gradient norm above 100, activity/clamp diagnostics outside preregistered bounds, or two consecutive evaluations below 0.30.

**Success criterion:** Lower 95% paired-bootstrap bound for improvement over the starting checkpoint is above zero, point accuracy is at least 0.45, and forced-minus-shuffled is not more than 0.02 below baseline. Promotion threshold: accuracy at least 0.50 with coverage at least 0.70 and forced-minus-shuffled at least 0.03.

If accuracy improves monotonically and no mechanism diagnostic degrades, optionally extend another 2,000 updates using cosine decay from \(1\times10^{-4}\) to \(1\times10^{-5}\).

### Stage 2: LR dose test from the same successful checkpoint

Only if Stage 1 is stable but does not improve enough. Run three short 500-update warm starts, all from identical weights and fixed batch/RNG sequence:

- LR \(3\times10^{-5}\);
- LR \(1\times10^{-4}\);
- LR \(3\times10^{-4}\).

All other settings match Stage 1. Validate every 50 updates and checkpoint every 100.

**Selection criterion:** Highest preregistered score

\[
\text{validation accuracy}
+0.25(\text{forced}-\text{shuffled})
-0.10\max(0,0.70-\text{coverage}),
\]

subject to accuracy never falling more than 0.03 below initialization at two consecutive evaluations.

Continue the winning LR for at most 1,500 more updates. This bracket is much cheaper than another full 12,000-step run and directly measures local basin stability.

### Stage 3: fresh schedule discriminator

A warm start optimizes efficiently but cannot show why the 12,000 run failed. For causal attribution, run fresh, same-seed paired controls with identical initialization and batch stream:

- **A: Reproduced 4k OneCycle control:** max LR \(2\times10^{-3}\), total steps 4,000, `pct_start=0.3`, default annealing.
- **B: Lower-peak 4k control:** max LR \(5\times10^{-4}\), total steps 4,000, `pct_start=0.3`.
- **C: Capped continuation schedule:** linear warm-up from \(4\times10^{-5}\) to \(5\times10^{-4}\) over 600 steps, then cosine decay to \(5\times10^{-5}\) at step 6,000.

Batch 64, AdamW, weight decay \(10^{-4}\), clip 1.0, same model and losses. Validate every 100 steps from 1,500 to 5,000, every 250 otherwise. Checkpoint every 200 steps from 2,000 to 5,000 and every 500 otherwise.

**Early stop:** Same degradation rule as Stage 1, plus stop an arm if validation accuracy is below 0.20 after step 2,000 or if its best accuracy trails another completed matched arm by more than 0.10 for five consecutive evaluations.

**Discriminating result:** The LR hypothesis receives strong support if A reproduces degradation near its high-LR interval while B or C avoids it under the same seed, initialization, and batch stream. It is weakened if all schedules collapse at similar update counts despite materially different LR trajectories.

### Stage 4: parameter-group LR localization

Run only if a stable schedule exists but endpoint progress remains poor.

From the best stable checkpoint:

- operator core, symbol/position embeddings, and output head: LR \(1\times10^{-4}\);
- hypernetwork, entry head, edge head, and any parameters directly controlling routing/GLV behavior: LR \(3\times10^{-5}\);
- weight decay \(10^{-4}\);
- maximum 2,000 updates;
- otherwise use Stage 1 cadence and stopping.

Matched control: all groups at \(1\times10^{-4}\).

Do **not** freeze the edge head merely because raw accuracy is 0.70. Freeze it only if Stage 0 shows adequate positive recall, calibration, and chain recovery. If validated, a second matched arm may freeze edge and entry heads while continuing endpoint components.

**Success criterion:** At least 0.03 paired accuracy improvement over the uniform-LR control without lower forced-minus-shuffled, coverage, or exact-order values.

### Stage 5: loss-balance ablation

Only after corrected edge metrics are available. Use the best stable LR and identical initialization/batch stream:

- task/edge/entry weights \(1.0/0.25/0.05\);
- \(1.0/1.0/0.2\) control;
- \(1.0/0/0\) diagnostic arm only if starting from a checkpoint with a frozen, validated compiler.

Normalize edge BCE by the number of live pairs explicitly:

```python
edge_loss = (bce_with_logits(el, E, reduction="none") * pair).sum() / pair.sum()
```

Prefer positive-class weighting or focal loss only after reporting prevalence and calibration.

Limit initial arms to 1,000 updates with validation every 100. Promote only an arm that improves endpoint accuracy by at least 0.03 while keeping balanced edge accuracy and positive recall within 0.03 of control.

### Stage 6: replication

After selecting one configuration without inspecting a final test set:

- Seeds: 0, 1, 2 initially.
- Maximum updates: as selected above, with identical stopping rules.
- Compare against the reproduced 4k schedule control on the same seeds.
- If the paired 95% interval remains wide or crosses zero, add seeds 3 and 4.

**Promotion criterion:**

- mean selected-checkpoint L2–4 accuracy at least 0.50;
- paired improvement over control with 95% interval excluding zero;
- no seed below 0.40;
- median forced-minus-shuffled at least 0.03;
- median coverage at least 0.70;
- L5 improvement reported separately and not required unless preregistered.

The original strong target of 0.65 should remain an aspirational endpoint, not the minimum evidence threshold for selecting a stable configuration.

## 5. Resume the 4,000 checkpoint or train fresh?

**Recommendation: resume the earlier successful 4,000-update checkpoint for the next accuracy-seeking run.**

Reasons:

1. It is the best known GPT-2 state at 0.412 L2–4 accuracy, higher than the 12,000-run best of 0.327.
2. The 12,000 run demonstrates that valuable structure can be destroyed by the current schedule; returning to a known basin is the cheapest way to test whether conservative continuation can improve it.
3. A 500–2,000-step low-LR continuation is substantially cheaper than another fresh 4,000–12,000-step training run.
4. The continuation directly answers the practical question: can more examples help when they are not coupled to a renewed high-LR phase?

Caveats:

- If the retained 4,000 checkpoint lacks optimizer state, call this a **warm start**, not a resume. Reset Adam moments can itself perturb optimization.
- Use a new validation set because the existing frozen panel has already influenced checkpoint selection.
- Do not resume from the failed 12,000 endpoint. Late annealing already failed to restore it, and it is near chance with impoverished trajectories.
- Preserve the 12,000 step-3,000 checkpoint for diagnostics, but it is inferior to the earlier 4,000 checkpoint for exploitation.

A fresh run is nevertheless required for the **causal schedule test**, because warm-start continuation cannot distinguish peak-LR effects from initialization, seed, or minibatch history. Thus the appropriate division is: warm start for economical optimization, short matched fresh runs for scientific attribution.

## 6. Mechanistic interpretations: licensed and unlicensed

### Licensed by the present evidence

- A useful but modest endpoint solution emerged by step 3,000 in this run.
- That solution was subsequently lost during the high-LR part of the stretched schedule.
- Endpoint behavior, itinerary completeness/order metrics, and trajectory-intervention effects deteriorated in roughly the same interval.
- At step 3,000, natural dynamics performed better than synthetic clamped controls, and forced-correct order performed modestly better than shuffled order.
- Additional test-time recurrent steps did not rescue these trained checkpoints.
- The frozen GPT-2 encoder itself did not change; failure occurred in trainable CAROM-side components or their interaction with fixed representations.

### Plausible but not established

- High LR caused the collapse.
- Routing/GLV parameters were more sensitive than the operator core or decoder.
- Joint auxiliary losses protected graph prediction while endpoint execution failed.
- The model briefly formed a useful heteroclinic-like channel.
- The 4,000-step basin can be improved by conservative continuation.
- L5 failure reflects structural extrapolation rather than simply weaker per-depth optimization.

### Not licensed

- That dependency-edge prediction was successfully learned or preserved. Raw accuracy near 0.70 may be a majority-negative baseline.
- That the compiled dependency graph is causally correct.
- That the system learned operator commutation or noncommutation.
- That high \(\tau\) establishes a complete itinerary; at step 3,000 coverage is only 0.728 and exact order only 0.332.
- That natural-minus-shuffled isolates command order.
- That the dynamics constitute a stable heteroclinic channel in the formal dynamical-systems sense; no stability, saddle, eigenvalue, residence-time, perturbation-recovery, or attractor diagnostics were run.
- That longer computation cannot help CAROM generally; only post hoc extension of models trained at 72 steps was tested.
- That frozen GPT-2 is intrinsically worse than TinyLM for this task. The arms differ in representation geometry and optimization history and are single-seed.
- That any result generalizes beyond the procedural six-slot \( \mathbb Z_8 \) task.
- That the best checkpoint is an unbiased endpoint. It was selected retrospectively from 13 evaluations on a panel now used in analysis.

## Final judgment

The report correctly treats the run as a failure and identifies the stretched learning-rate schedule as the leading suspect. Its strongest scientific contribution is the checkpoint-resolved demonstration that endpoint competence and organized trajectories can be destroyed together while late LR annealing does not recover them.

The main correction is that raw edge accuracy does not establish preserved graph learning, and therefore the collapse cannot yet be cleanly localized downstream of the compiler. The next dollar should go to corrected checkpoint-only diagnostics and a conservative warm start from the successful 4,000-step checkpoint. A small matched fresh-run schedule experiment should then determine whether high LR is causal. Large 12,000-step reruns, edge-head freezing, and elaborate mechanistic interpretations are premature until those two inexpensive discriminators are complete.
