# First GPU programme after the 0.4 revision

This programme is designed to falsify weak interfaces and compare rival
representation paradigms before investing in PC settlement, learned highways,
or symbolic infrastructure.

## Model and data

Start with the existing six-layer synthetic-grammar student and GPT-2-small
teacher so that subject number, object number, tense, negation, and agreement
counterfactuals remain available. Then repeat the surviving conditions on a
semi-synthetic natural-language corpus with controlled edits.

## Stage 0A: frozen observability

Read candidate layers separately and in combinations. Fit:

- linear residual;
- low-rank residual with ranks 4, 8, 16, 32, 64;
- MLP residual;
- ordinary LoRA at matched parameters.

Report total and factor-specific teacher-gap closure. Stop or change the
interface if a reasonable BP residual cannot recover the desired correction.

## Stage 0B: representation contest

Use exact gradients for all arms:

1. dense bottleneck residual;
2. LoRA;
3. SAE plus steering;
4. grouped overcomplete SAE plus steering;
5. orthogonal fibres;
6. contextual fibre bundle;
7. optional low-rank co-adaptive versions of the strongest frozen arms.

Match or report:

- parameters ever trained;
- active feature count;
- wall-clock training;
- deployment wall clock;
- residual output rank;
- reconstruction;
- teacher-gap closure;
- factor intervention selectivity;
- held-out factor combinations.

## Stage 1: exact-gradient plasticity

Advance the best two structured representations plus dense and SAE controls.
Compare:

- exact gradient;
- exact gradient plus supplied support mask;
- exact gradient plus learned responsibility gate;
- replay;
- ordinary parameter isolation.

Train routers on a subset of contexts and test unseen compositions. Report
support precision, recall, off-support mass, current-task adaptation, unrelated
KL drift, and finite curriculum-order distances.

## Stage 2: controlled substrate co-adaptation

For cases where frozen observability is limiting, allow rank-4 or rank-8 LoRA
updates in selected base projections. Use anchor trust regions and alternate
three residual steps with one substrate step. Compare against ordinary LoRA and
full fine-tuning where affordable.

## Stage 3: PC/ePC value

Only now add state inference:

- feed-forward predictor;
- matched-parameter recurrent adapter;
- state-PC with K in {1, 2, 4};
- damped LM/ePC with K in {1, 2, 4}.

Evaluate:

- predictor only;
- free settlement without new information;
- constrained settlement with retrieval or rule constraints;
- teacher-clamped diagnostic.

PC advances only if it improves sample efficiency, robustness, continual
retention, representation quality, or matched deployment compute.

## Stage 4: optional learned highway

Proceed only if exact gradients are unavailable or costly, locality is itself a
goal, or held-out-context credit transfer is the hypothesis. Compare learned
credit to exact-gradient gated plasticity, not merely to dense feedback.

## Stage 5: symbolic cap

Use a large template store with hard negatives and compositional held-out tests.
Require symbolic inference to cause selective neural-state changes and correct
behavioral effects. Small-template retrieval accuracy is only an API test.

## Pass/fail gates

- frozen BP teacher-gap closure above 50% to proceed with the interface;
- structured representation must beat or complement dense/SAE at matched
  budget;
- held-out support F1 above 0.7 before PC or highways;
- low-rank co-adaptation must improve observability without unacceptable anchor
  drift;
- free settlement must be reported separately and compared at matched compute;
- learned highway must show novel-context, cost, or locality value;
- symbolic cap must show rule-mediated behavioral value.
