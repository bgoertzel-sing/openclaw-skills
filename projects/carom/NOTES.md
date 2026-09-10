# Working Notes

Use this file for provisional project notes. Add dates and source pointers. Promote durable decisions, results, or tasks to their dedicated files.

## 2026-07-24 — Fable/Sol ladder

- Audited all 40,960 E0/E1 evaluation rows and found the deterministic defect.
- Implemented E2 fitness ablations and five generic E3 penalties; permutation
  invariance is the executable no-successor-encoding guard.

## 2026-07-25 — E2/E3 full-scale CPU feasibility

- Research Rules 1, 2, and 5 were most relevant: validate the measurement
  runner, freeze an inspectable gate specification, and preserve exact
  resource evidence.
- A full-shape one-update/five-arm corpus slice completed deterministically in
  3:58.60 with 5.16 GB peak RSS.
- A 50-arm-update training-rate slice completed deterministically in 3:26.47
  with 7.80 GB peak RSS, projecting about 86 wall hours for 75,000 updates
  before full evaluation.
- The local host is therefore unsuitable for a practical full confirmation.
  The existing runner is operational, but the scientific gate remains
  qualitative: no numerical paired trajectory or excess-exposure thresholds
  are frozen. E4 stays closed. No RunPod resource was provisioned or used.
- Smoke: 3.67 s, 305 MB, 10/10 deterministic. Fixture: 74.23 s, 375 MB,
  25/25 deterministic. The 40-update fixture is not an efficacy result.
# 2026-07-25 - GPT-2 controller v4 audit

**Observed:** the v4 runner's `run_gate` chooses an LR scale only for
counterfactual eight-update branches. The parent loop always continues with
its unmodified OneCycleLR, so `informed_final_loss_median` is a branch score,
not an active-controller outcome. The step-2000 gate is also after
OneCycleLR has decayed to a printed LR of `0.000000`; scale comparisons there
are therefore near-vacuous. The terminal scheduler crash was repaired, but
the resulting run cannot establish controller utility. A replacement must
compare state-restored continuations under the selected action versus passive
with common future batches, while retaining an unmodified parent only for the
operational invariant check.
