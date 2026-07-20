# OmegaSelf Pre-action Prediction Contract

Schema: `omegaself.pre_action_prediction` version `1.0.0`.

## Canonical record

```metta
(PreActionPrediction
  (schema "omegaself.pre_action_prediction" "1.0.0")
  (id "pred-001")
  (closure "sha256:<64 lowercase hex>")
  (clocks (causal "cycle:43") (record "2026-07-20T12:01:00Z") (adoption "prediction-set:8"))
  (target (proposal "proposal-001") (action-class "read_only_probe"))
  (distribution (outcome "success" 0.8) (outcome "failure" 0.2))
  (affected-needs (need "epistemic_accuracy" 0.4) (need "resource_budget" -0.1))
  (confidence 0.75)
  (rubric "receipt.status mapped to success|failure")
  (ordering (proposal-created 100) (prediction-committed 101) (action-authorized 102))
  (status "committed"))
```

Outcome names are unique and probabilities are finite decimals in `[0,1]` summing to 1 within `1e-9`. Need names are unique and expected deltas are in `[-1,1]`. Confidence is in `[0,1]`. The rubric is non-empty and fixed at commitment.

Ordering counters are positive integers satisfying `proposal-created < prediction-committed < action-authorized`. Before authorization, `action-authorized` may be `null`; the other inequality still applies. A prediction is valid only with status `committed`. Outcome resolution appends another record and never edits the distribution.

The closure names the evidence available at commitment. The record clock is the commitment wall time; causal and adoption clocks retain their separate meanings. A post-outcome reconstruction or prediction committed at/after authorization is rejected and receives no calibration credit.

## Failure contract

Structural errors, duplicate labels, invalid probability mass/ranges, empty rubric, invalid status, or violated temporal ordering raise a validation error and return no prediction.
