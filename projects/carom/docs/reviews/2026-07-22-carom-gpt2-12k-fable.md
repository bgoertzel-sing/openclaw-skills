# Independent technical review: CAROM frozen-GPT-2 12,000-update experiment

**Review date:** 2026-07-22  
**Evidence reviewed:** detailed five-page PDF; `summary.json`; training and intervention logs; 12k wrapper; retained GPT-2 runner; supplied compiled-channel implementation; run ledger.  
**Overall judgment:** The run establishes a real optimization failure between steps 3,000 and 5,000, but does not uniquely identify its cause. The high learning-rate phase is the leading explanation. However, two important confounds weaken the report’s localization claim: checkpoint evaluations consume the same Python RNG used to generate subsequent training data, and the 4k and 12k runs used different checkpoint cadences. More seriously, the reported edge accuracy is compatible with a trivial majority-negative classifier, so “dependency prediction survived” is not presently established.

## 1. What is directly observed

On the frozen L2–4 corpus:

- Endpoint accuracy rises from 0.139 at initialization to 0.327 at step 3,000, then falls to 0.167 at step 4,000 and 0.126 at step 5,000. It recovers only to approximately 0.19 thereafter.
- Repaired itinerary coverage falls from 0.728 at step 3,000 to 0.470 at step 12,000.
- Exact order falls from 0.332 to 0.094.
- Transition recall falls from 0.448 to 0.128.
- Mean phases/unique modes fall from approximately 2.09/2.05 at step 3,000 to 1.33/1.33 at step 12,000. This is a collapse toward single-mode occupancy, not merely an order inversion.
- Natural-minus-shuffled endpoint accuracy falls from 0.080 at step 3,000 to 0.004 at step 4,000, becomes negative at step 5,000, and remains small thereafter.
- The better order-controlled contrast, forced-minus-shuffled, is only 0.0306 at step 3,000 and approximately zero at most later checkpoints.
- L5 accuracy peaks at 0.262 at step 3,000 and collapses with L2–4 performance. Increasing recurrent steps from 72 to 100 or 120 does not rescue it.
- The logged training loss reaches its minimum at step 3,000, rises sharply through step 5,000, and does not return to its earlier level.
- The OneCycleLR schedule is near its maximum during the onset of failure: approximately \(1.87\times10^{-3}\) at step 3,000 and \(1.99\times10^{-3}\) at step 4,000.
- The run is single-seed and changes both total training duration and the learning-rate trajectory relative to the earlier 4k run.

These observations robustly establish checkpoint-level degradation. They do not, by themselves, identify which parameter group or loss component failed.

## 2. Ranked diagnosis of the collapse

### 1. High-LR destabilization of the recurrent execution/routing system — most plausible

**Evidence:**

- The failure begins precisely while LR is approaching its \(2\times10^{-3}\) maximum.
- Endpoint loss, itinerary completeness, and order-sensitive intervention effects degrade together.
- Later annealing does not return the model to the step-3,000 basin, consistent with an optimizer excursion into a poorer basin.
- In the earlier 4k schedule, the LR had already fallen to approximately \(5.65\times10^{-4}\) at step 3,000, whereas it was still \(1.87\times10^{-3}\) in the 12k run.

**Inference:** The long high-LR interval likely damages one or more of the GLV compiler, entry scorer, command-to-operator router, operator core, or recurrent readout.

**Uncertainty:** There are no per-group update norms, gradient norms, parameter-drift measurements, or controlled schedule replicates. Temporal coincidence is strong but not causal identification.

### 2. Training-objective imbalance or an easy auxiliary-loss attractor — plausible and potentially interacting with LR

Training optimizes endpoint cross-entropy plus edge BCE at weight 1.0 plus entry cross-entropy at weight 0.2. No per-loss curves or gradient contributions were recorded.

The edge metric does not demonstrate that graph compilation remained correct. For a chain of length \(L\), only \(L-1\) of \(L(L-1)\) directed off-diagonal pairs are positive. Across lengths 2–4, a roughly 70% negative-class prevalence is quite plausible. The observed edge accuracy jumps to approximately 0.703 at step 1,000 and then remains near that level, which is exactly the signature expected if thresholded logits predict almost every edge as absent. The final rise to 0.731 could reflect class bias rather than improvement.

Therefore:

- The report’s statement that “dependency prediction survived” is **not licensed** by edge accuracy alone.
- The evidence only shows that **thresholded edge accuracy stayed near the likely majority-class baseline**.
- Required diagnostics are positive recall, precision, balanced accuracy, MCC, tie-correct AUROC/AUPRC, logit histograms, calibration, and comparison with explicit all-negative/all-positive baselines.

The implementation also supplies a masked tensor as BCE’s `weight` but uses default mean reduction over the entire padded \(L_{\max}\times L_{\max}\) matrix. Thus the effective magnitude of edge supervision varies with program length and includes a denominator contribution from zero-weight padded entries. This is not necessarily the cause, but it makes the nominal edge weight of 1.0 hard to interpret.

### 3. Entry/routing-mode collapse under recurrent feedback — plausible proximal mechanism

The observed trajectory changes strongly support this as the **form** of failure:

- unique visited modes drop toward one;
- dwell rises toward nearly the whole 72-step trajectory;
- coverage, exact order, and transition recall degrade;
- longer integration mostly lengthens dwell without adding modes.

This is consistent with an entry scorer or compiled inhibition matrix selecting a dominant mode that no longer yields reliable invasion/switching. It could also result from router/operator changes that alter workspace feedback through `sigma`, thereby changing GLV fitness.

This is a proximal description, not a root-cause diagnosis. Without activity distributions, entry probabilities, rho spectra, invasion margins, router entropy, and workspace-feedback magnitudes, the failing component cannot be localized.

### 4. Seed-specific bifurcation or stochastic instability — plausible

There is only one seed. CAROM includes training-time Gaussian activity noise and nonlinear recurrent dynamics, so a sharp seed-dependent bifurcation is credible. No inference about typical behavior or failure probability is justified.

### 5. Changed training-data stream caused by evaluation RNG coupling — definite confound

The training loop and online evaluator pass the same `random.Random` instance to `make_batch`. Each checkpoint evaluation consumes additional random draws before training resumes. The prior 4k run checkpointed every 500 steps; the 12k run checkpointed every 1,000 steps. Consequently, even with seed 0, the two runs did **not** receive the same training sequence through step 4,000.

This does not explain the within-run deterioration by itself, but it prevents a clean statement that the 4k/12k difference is solely the schedule. It also means changing evaluation cadence changes the experiment.

The next runner must use separate RNGs for training, online monitoring, frozen validation, and interventions. The training stream should be hash-checked in a short deterministic test.

### 6. General overtraining independent of LR — possible but less supported

More examples might eventually favor a poorer execution strategy even at low LR. However, the abrupt deterioration near the LR maximum and failure to recover are more consistent with destabilization than gradual overfitting. A low-LR continuation is needed to distinguish these explanations.

### 7. Insufficient inference settling — disfavored

The S=72/100/120 sweep provides useful negative evidence. Longer execution does not restore endpoint accuracy, and frequently only scales dwell time. The model is not simply one or two transitions short of a correct solution. This does not exclude a different integration discretization or GLV-timescale mismatch, but it disfavors “just run longer at test time.”

## 3. Critique of the report

The report is concise, traceable to the retained JSON, candid about single-seed and schedule-duration confounding, and appropriately rejects a commutation claim. Its central optimization narrative is reasonable. The following omissions materially affect interpretation.

### Edge accuracy is overinterpreted

The report treats approximately 0.70 edge accuracy as evidence that dependency prediction survived. Because edge labels are imbalanced, this may be an all-negative baseline. This invalidates the claimed localization “downstream of, or orthogonal to, edge supervision” until calibrated edge diagnostics are run.

### The strongest intervention contrast is not the one emphasized

Natural-minus-shuffled compares a learned natural trajectory with an externally clamped shuffled trajectory. It changes order, amplitude, dwell, smoothness, feedback, and potentially total command exposure. It is not an order-specific causal effect.

Forced-minus-shuffled better matches amplitude and segment duration, differing mainly in order. At step 3,000 that contrast is 0.0306, not 0.0801. This is suggestive of order sensitivity, but its uncertainty is unknown. The near equality of forced, shuffled, and smeared endpoints after collapse is evidence that the externally clamped execution becomes insensitive to the specific clamped trajectory—not proof that natural execution is noncausal.

### Missing uncertainty and unit-of-analysis definition

No confidence intervals or paired per-example differences are reported. Slot accuracy treats six slots from the same program as separate observations; they are correlated. Report both:

- slot accuracy;
- exact-program accuracy;
- mean per-program slot accuracy;
- paired bootstrap intervals resampled by program.

Checkpoint selection on the same 256-example corpus creates winner’s-curse bias. A separate selection corpus and untouched confirmation corpus are needed.

### The comparison to the 4k run has additional confounds

Besides the different schedule:

- checkpoint cadence differs, altering the shared training RNG stream;
- retained checkpoints omit optimizer and scheduler state;
- the report does not demonstrate identical initialization hashes, package versions, GPT-2 revision, generated training batches, or initial compiled-channel state;
- the 4k and 12k results are single runs, so their difference could be seed/data-stream variation.

### Training telemetry is too coarse

One record per 1,000 updates is insufficient around a failure occurring between 3,000 and 4,000. Missing diagnostics include:

- endpoint, edge, and entry losses separately;
- unclipped and clipped gradient norms globally and by parameter group;
- optimizer step/update norms and parameter norms by group;
- fraction of steps hitting the clip threshold;
- edge positive/negative logits and calibrated metrics;
- entry accuracy and entropy;
- command-router entropy, top-1 frequency, and operator utilization;
- GLV activity mass, maximum activity, phase counts, dwell distribution, and clamp fraction;
- compiled-rho distributions, invasion margins, and stability indicators;
- workspace-update norm by operator and recurrent step;
- NaN/Inf and activation-range monitoring.

### Training noise and evaluation mode need explicit treatment

Training includes additive Gaussian activity noise while evaluation disables it through `model.eval()`. This is reasonable, but no noisy-versus-deterministic evaluation is reported. A high LR may interact with noisy recurrent dynamics. Evaluate both modes on a paired corpus and record multiple noise draws.

### The forced intervention is not an oracle

The report correctly notes this, but the consequence should be stronger: lower forced accuracy does not demonstrate that correct order is harmful, because forcing changes the natural activity scale and state-conditioned dwell. An exposure-matched trajectory replay control is needed.

### “Frozen corpus” does not mean unbiased checkpoint selection

The fixed corpus improves comparability, but repeatedly inspecting it makes it a validation set. It cannot also provide an unbiased final performance estimate.

## 4. Ordered, cost-efficient experiment ladder

All stages should first repair RNG separation and metric instrumentation. Use:

- training RNG seed: `10000 + seed`;
- monitoring RNG seed: `20000 + seed`;
- validation corpus: seed 1234, **1,024 programs**, stratified equally over L=2,3,4;
- confirmation corpus: seed 4321, **2,048 programs**, untouched until a configuration passes;
- L5 corpus: seed 5678, **512 programs**;
- intervention subset: fixed 512 L2–4 programs;
- batch size 64;
- AdamW weight decay \(10^{-4}\);
- gradient clipping 1.0, with pre-clip norm logged;
- checkpoints every 250 updates through 5,000, then every 500;
- lightweight endpoint/edge/entry/activity evaluation every 250;
- full intervention and L5 panels every 1,000 and at the selected checkpoint.

Use paired program-level bootstrap 95% intervals for endpoint and intervention contrasts.

### Stage 0: checkpoint-only forensics

No training is required.

Evaluate retained 4k-final, 12k-step-3k, 12k-step-4k, and 12k-step-5k checkpoints on the same new corpora. Record:

- edge prevalence and all-negative baseline;
- edge precision, recall, balanced accuracy, MCC, AUROC, AUPRC, Brier score, and logits by class;
- entry accuracy/entropy;
- router entropy and operator utilization;
- activity mass, max activity, number of active/visited modes, dwell quantiles;
- rho and invasion-margin distributions;
- parameter norms and pairwise checkpoint drift by module.

**Decision rule:** If edge positive recall is below 0.20 or AUPRC is no better than prevalence plus 0.05, stop interpreting edge accuracy and repair/reweight the auxiliary loss before longer training.

### Stage 1: low-cost resume probe from the earlier 4k checkpoint

For the next optimization run, resume the earlier **4k-final model weights**, because it is the best retained GPT-2 endpoint (0.412) and avoids paying again to reach a known basin. This is a fine-tune, not an exact continuation: the checkpoint lacks Adam moments and scheduler state.

Use a fresh AdamW optimizer:

- operator core, symbol/position embeddings, output head: LR \(1\times10^{-4}\);
- hyper/router, entry scorer, `sigma`, `sig_scale`, `pool_q`: LR \(5\times10^{-5}\);
- edge head: frozen for the first 1,000 updates;
- cosine decay over 2,000 updates to \(1\times10^{-5}\), no warm-up;
- edge loss weight 0 while frozen; entry loss weight 0.2;
- at update 1,000, unfreeze edge only if Stage 0 shows useful calibrated edge prediction; then use LR \(1\times10^{-5}\) and normalized masked BCE.

Evaluate every 250 updates.

**Early stop:** Stop if, at two consecutive evaluations:

- L2–4 accuracy is more than 0.04 below the starting checkpoint; or
- exact order falls by more than 0.08 and forced-minus-shuffled falls below 0; or
- nonfinite values occur; or
- more than 25% of recent steps have pre-clip norm above 10.

**Gate to Stage 2:** Select a checkpoint only if validation L2–4 accuracy is at least 0.45, no worse than 0.39 at any of the preceding two evaluations, coverage is at least 0.70, exact order at least 0.28, and forced-minus-shuffled is positive with a paired 95% interval excluding zero. The preregistered substantive target remains >0.55.

This stage distinguishes “the known basin can improve under small steps” from “additional examples themselves cause degradation.”

### Stage 2: fresh paired schedule discriminator

Train fresh runs with identical initialization and pre-generated or hash-equivalent training batches. Use seed 0 initially and two arms:

**Control A: reproduce the 4k schedule**

- 4,000 updates;
- OneCycleLR maximum \(2\times10^{-3}\);
- `pct_start=0.30`;
- all other OneCycle defaults explicitly recorded.

**Treatment B: conservative 12k schedule**

- 12,000-update cap;
- linear warm-up from \(1\times10^{-5}\) to \(5\times10^{-4}\) over 500 updates;
- constant \(5\times10^{-4}\) through update 4,000;
- cosine decay to \(5\times10^{-5}\) by update 8,000;
- stop at 8,000 unless validation is still improving;
- same parameter-group LR multipliers as Stage 1;
- edge head/loss handling determined by Stage 0.

Use identical training examples through step 4,000 and identical evaluation cadence.

**Early stop:** Stop an arm after three consecutive 250-step evaluations without a new accuracy maximum if the latest accuracy is at least 0.05 below the running maximum and either coverage has fallen by 0.10 or forced-minus-shuffled has become nonpositive twice. Never stop solely on noisy tau.

**Success:** Treatment B must exceed the paired control by at least 0.04 validation accuracy, achieve at least 0.45 absolute accuracy, retain coverage ≥0.70 and exact order ≥0.28, and avoid persistent trajectory degradation. Promotion target remains >0.55.

This is the cleanest direct test of the schedule hypothesis.

### Stage 3: peak-LR bracket

Only if Stage 2 indicates schedule sensitivity but remains below 0.55, run fresh seed-0 arms with otherwise identical settings:

- peak LR \(2.5\times10^{-4}\);
- peak LR \(5\times10^{-4}\);
- peak LR \(1\times10^{-3}\);

using 500-step warm-up, constant to 3,000, cosine decay to 6,000, and the same early-stop rule. Successive-halving rule: terminate an arm at 2,000 if it trails the best arm by >0.06 accuracy and has no compensating ≥0.05 advantage in exact-program accuracy.

Do not include \(2\times10^{-3}\) again unless needed as an explicit positive failure control.

### Stage 4: loss and module localization

If calibrated edges are trivial or execution still collapses, compare at the best LR:

- normalized positive-class-weighted edge BCE with edge weight 0.25;
- edge head frozen after 1,000 updates;
- no edge/entry auxiliary losses after 1,000 updates;
- parameter-group LR reduction for GLV/router modules to 0.25× the core LR.

Run only to 4,000 updates initially. The key discriminator is whether endpoint and trajectory performance improve without sacrificing genuinely calibrated edge recall.

### Stage 5: replication

Promote only one configuration. Run seeds 0, 1, and 2; add seeds 3 and 4 if the standard deviation of L2–4 accuracy exceeds 0.04.

Final success criteria on the untouched confirmation corpus:

- mean L2–4 slot accuracy >0.55, with the seed-level 95% interval reported;
- exact-program accuracy reported and above the best prior checkpoint;
- no seed below 0.45;
- mean coverage ≥0.70 and exact order ≥0.28;
- forced-minus-shuffled paired interval above zero;
- L5 accuracy ≥0.30 or a preregistered positive improvement of ≥0.05 over the paired 4k control;
- calibrated edge AUPRC materially above prevalence.

A stronger endpoint target of ≥0.65 should remain aspirational until the 0.55 target replicates.

## 5. Resume or train fresh?

**Immediate recommendation: resume the earlier 4k-final weights for one bounded, low-LR fine-tuning probe.**

Reasons:

1. It is the best retained GPT-2 endpoint at 0.412, better than the 12k step-3,000 checkpoint at 0.327.
2. The 12k evidence suggests the useful region is fragile under large updates; re-paying to approach it with another high-amplitude schedule is inefficient.
3. A 1,000–2,000-update low-LR continuation is the cheapest test of whether additional data can improve the known solution without destabilizing it.
4. The retained 4k model can serve as a recovery and performance branch while instrumentation is repaired.

However, this must be described as **fine-tuning from model weights with a newly initialized optimizer**, not “resuming training,” because optimizer/scheduler states were not retained. It cannot cleanly prove why the 12k run failed.

For causal schedule comparison and any publishable conclusion, train fresh paired arms after the resume probe, with identical initialization, training batches, checkpoint cadence, and separate RNG streams.

## 6. Mechanistic interpretations

### Licensed by the current evidence

- The learned system has a transient step-3,000 regime with better endpoints, broader mode coverage, more correct transitions, and nonzero sensitivity to trajectory order.
- The final 12k model commonly remains in one dominant mode for most of the trajectory.
- Extending the integration horizon alone does not rescue endpoint performance.
- A high-LR phase is a strong candidate cause of the collapse.
- Natural recurrent execution and externally clamped execution are not functionally equivalent at the step-3,000 checkpoint.
- The experiment failed its preregistered endpoint targets.

### Not licensed

- **“Dependency prediction survived.”** Thresholded edge accuracy may be a majority-negative baseline.
- **“The collapse is downstream of the graph compiler.”** The graph compiler has not been shown to predict positive edges correctly or remain calibrated.
- **“The high LR caused the collapse.”** Only temporal association exists.
- **“The natural-minus-shuffled gap proves ordered itinerancy.”** It conflates order with amplitude, dwell, smoothness, exposure, and feedback.
- **“Forced-correct is an oracle.”** It is an out-of-distribution clamped execution mode.
- **“GPT-2 representations are inferior to TinyLM representations.”** The comparison is single-seed and may differ in optimization conditioning, representation scale, data streams, and hyperparameter suitability.
- **“CAROM learned commutation/noncommutation structure.”** The validated swap/JVP controls were not run.
- **“The model generalizes compositionally to length five.”** L5 accuracy is low, exact order is zero in the displayed checkpoints, and there is no appropriate matched non-compositional baseline.
- **“More training is harmful.”** The run tested more training under a different schedule and different RNG consumption pattern.
- **“Tau near one demonstrates a complete itinerary.”** At L5, tau can be near one while only about two of five modes are visited.

## Conclusion

The strongest defensible conclusion is that the 12k configuration crossed from a partially useful multi-mode regime into a largely single-mode, low-accuracy regime during its maximum-LR phase. The schedule hypothesis deserves priority, but the present run does not isolate it. Before spending on another long run, repair RNG separation, replace raw edge accuracy with imbalance-aware diagnostics, log per-loss and per-module optimization statistics, and run a short low-LR fine-tune from the better 4k weights. A fresh paired schedule experiment should follow only after those gates pass.
