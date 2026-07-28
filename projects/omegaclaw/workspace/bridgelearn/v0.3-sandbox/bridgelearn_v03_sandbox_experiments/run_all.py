from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from experiments.antithetic_identification import run as run_antithetic
from experiments.common import environment_record, write_json
from experiments.companion_stability import run as run_stability
from experiments.dynamic_sharpness import run as run_sharpness
from experiments.momentum_reachability import run as run_reachability


def _fmt(value: float, digits: int = 4) -> str:
    return f"{value:.{digits}g}"


def _crossing(value: int | None) -> str:
    return "none within rollout" if value is None else str(value)


def _write_report(path: Path, summary: dict[str, Any]) -> None:
    sharp = summary["dynamic_sharpness"]
    anti = summary["antithetic_identification"]
    stable = summary["companion_stability"]
    reach = summary["momentum_reachability"]

    repeated = stable["cases"]["near_repeated_root"]
    under = stable["cases"]["underdamped_same_radius"]
    fixed = reach["one_step"]["fixed_results"]
    adaptive = reach["one_step"]["adaptive_results"]

    text = f"""# BridgeLearn 0.3 sandbox experiments

Generated: {summary['generated_utc']}

BridgeLearn version: `{summary['environment']['bridgelearn']}`

## Purpose

These four synthetic experiments exercise the v0.3 mechanisms that were added
for nonlinear sharpness response and momentum dynamics:

1. online identification and forward prediction of a dynamic sharpness plant;
2. order-2 antithetic excitation for the weak AR(2) contrast direction;
3. companion-matrix stability and Lyapunov-adapted covariance norms;
4. momentum-limited covariance reachability and actuator projection.

They are mechanism tests, not neural-network, CAROM, predictive-coding, or RL
performance claims.

## Executive results

| Experiment | Main result |
|---|---|
| Dynamic sharpness | `SharpnessPlant` recovered gamma_p={_fmt(sharp['estimated_gamma_p'], 6)} and gamma_r={_fmt(sharp['estimated_gamma_r'], 6)} from truths {_fmt(sharp['true_gamma_p'], 6)} and {_fmt(sharp['true_gamma_r'], 6)}. One-step RMSE was {_fmt(sharp['plant_one_step_rmse_against_true'], 5)}, versus {_fmt(sharp['rolling_static_model_rmse'], 5)} for a rolling static h(eta) fit. |
| Antithetic identification | At nearly equal added state width, contrast RMSE for c1-c2 was {_fmt(anti['modes']['antithetic']['contrast_rmse'], 5)}, versus {_fmt(anti['modes']['white']['contrast_rmse'], 5)} for white excitation and {_fmt(anti['modes']['none']['contrast_rmse'], 5)} without a probe. |
| Companion stability | The near-repeated-root matrix had spectral radius {_fmt(repeated['spectral_radius'], 5)} yet transient covariance amplification {_fmt(repeated['max_covariance_amplification'], 5)}x and Lyapunov condition number {_fmt(repeated['lyapunov_condition'], 6)}. |
| Momentum reachability | Cooling V=0.08 to V=0.005 with fixed mu=0.9 has an asymptotic floor requiring at least {reach['minimum_horizon_at_mu_0.9']} updates. The one-step actuator found {reach['one_step']['fixed_momentum_feasible_count']}/{reach['one_step']['total_targets']} fixed-momentum targets feasible and {reach['one_step']['adaptive_momentum_feasible_count']}/{reach['one_step']['total_targets']} feasible when momentum could move. |

# 1. Dynamic sharpness as a plant

## Model

The simulated plant was

```text
h[k+1] = h[k]
       + gamma_p * g[k]
       - gamma_r * max(eta[k] h[k] - (2(1+mu[k])-delta), 0)
       + process noise.
```

The command schedule warmed, oscillated near the edge, cooled, and rewarmed.
This creates lag and hysteresis that cannot be represented by a static curve
`h(eta)`.

`bridgelearn.SharpnessPlant` was updated by forgetting-factor RLS and generated
one-step interval forecasts. Metrics exclude the first {sharp['burn_in_for_metrics']}
updates.

## Results

- True parameters: gamma_p={sharp['true_gamma_p']}, gamma_r={sharp['true_gamma_r']}.
- Final estimates: gamma_p={_fmt(sharp['estimated_gamma_p'], 7)}, gamma_r={_fmt(sharp['estimated_gamma_r'], 7)}.
- Relative errors: {_fmt(100*sharp['relative_error_gamma_p'], 4)}% and {_fmt(100*sharp['relative_error_gamma_r'], 4)}%.
- Plant one-step RMSE against latent sharpness: {_fmt(sharp['plant_one_step_rmse_against_true'], 7)}.
- Rolling static-response RMSE: {_fmt(sharp['rolling_static_model_rmse'], 7)}.
- RMSE improvement over the static response: {_fmt(sharp['rmse_improvement_over_static'], 5)}x.
- Empirical funnel coverage: {_fmt(100*sharp['funnel_coverage_against_true'], 5)}%.

The counterfactual held eta={sharp['counterfactual']['candidate_step_size']} and
mu={sharp['counterfactual']['candidate_momentum']} after update
{sharp['counterfactual']['start_step']}. A frozen-curvature calculation reported
edge utilization {_fmt(sharp['counterfactual']['frozen_edge_utilization'], 5)}, so
it would have treated the command as safe indefinitely. The true plant crossed
the edge after { _crossing(sharp['counterfactual']['true_edge_crossing_future_step']) }
future updates. The plant point forecast crossed after
{ _crossing(sharp['counterfactual']['point_forecast_edge_crossing_future_step']) },
while the robust upper funnel warned after
{ _crossing(sharp['counterfactual']['upper_funnel_edge_crossing_future_step']) }.

Artifacts:

- [tracking plot](artifacts/dynamic_sharpness/dynamic_sharpness_tracking.png)
- [edge-utilization plot](artifacts/dynamic_sharpness/dynamic_sharpness_edge_utilization.png)
- [parameter identification](artifacts/dynamic_sharpness/dynamic_sharpness_parameters.png)
- [counterfactual rollout](artifacts/dynamic_sharpness/dynamic_sharpness_counterfactual.png)
- [full trace](artifacts/dynamic_sharpness/dynamic_sharpness_trace.csv)

# 2. Antithetic order-2 identification

## Model and resource matching

The cold AR(2) plant was

```text
z[k+1] = 1.8 z[k] - 0.81 z[k-1] + u[k] + epsilon[k],
```

which has a repeated pole at 0.9. Its weakly identified combination is
`c1-c2`. The experiment compared no probe, white known excitation, and the
library's exact committed `+delta,-delta` probe pairs.

The white and antithetic probe amplitudes were chosen to add approximately the
same stationary state width, {anti['equal_realized_probe_width']}. Known probe
commands were subtracted from the regression response, so the comparison is
about regressor geometry rather than unmodeled forcing.

## Results over {anti['trials']} trials

| Mode | Contrast RMSE | Median cond(M) | Median smallest eigenvalue | Added state variance |
|---|---:|---:|---:|---:|
| None | {_fmt(anti['modes']['none']['contrast_rmse'], 6)} | {_fmt(anti['modes']['none']['median_regressor_condition'], 6)} | {_fmt(anti['modes']['none']['median_smallest_eigenvalue'], 6)} | {_fmt(anti['modes']['none']['added_state_variance'], 6)} |
| White | {_fmt(anti['modes']['white']['contrast_rmse'], 6)} | {_fmt(anti['modes']['white']['median_regressor_condition'], 6)} | {_fmt(anti['modes']['white']['median_smallest_eigenvalue'], 6)} | {_fmt(anti['modes']['white']['added_state_variance'], 6)} |
| Antithetic | {_fmt(anti['modes']['antithetic']['contrast_rmse'], 6)} | {_fmt(anti['modes']['antithetic']['median_regressor_condition'], 6)} | {_fmt(anti['modes']['antithetic']['median_smallest_eigenvalue'], 6)} | {_fmt(anti['modes']['antithetic']['added_state_variance'], 6)} |

Antithetic excitation reduced contrast RMSE by
{_fmt(anti['improvement']['contrast_rmse_antithetic_vs_white'], 5)}x relative
to equal-width white excitation and improved the median smallest regressor
eigenvalue by {_fmt(anti['improvement']['smallest_eigenvalue_antithetic_vs_white'], 5)}x.
The median condition number fell by
{_fmt(anti['improvement']['condition_white_vs_antithetic'], 5)}x.

Artifacts:

- [contrast error distribution](artifacts/antithetic_identification/antithetic_contrast_error.png)
- [online RLS standard error](artifacts/antithetic_identification/antithetic_online_standard_error.png)
- [regressor information](artifacts/antithetic_identification/antithetic_regressor_information.png)
- [probe signals](artifacts/antithetic_identification/antithetic_probe_signals.png)
- [trial-level data](artifacts/antithetic_identification/antithetic_trial_results.csv)

# 3. Companion stability and non-normality

Four stable companion matrices were compared. Two had essentially the same
spectral radius, 0.9, but very different geometry.

| Case | Regime | rho(A) | cond(P) | Max covariance amplification | Peak step |
|---|---|---:|---:|---:|---:|
| Near repeated root | {repeated['regime']} | {_fmt(repeated['spectral_radius'], 6)} | {_fmt(repeated['lyapunov_condition'], 7)} | {_fmt(repeated['max_covariance_amplification'], 7)} | {repeated['peak_amplification_step']} |
| Underdamped, same radius | {under['regime']} | {_fmt(under['spectral_radius'], 6)} | {_fmt(under['lyapunov_condition'], 7)} | {_fmt(under['max_covariance_amplification'], 7)} | {under['peak_amplification_step']} |

For the near-repeated-root case, an initial covariance error chosen along the
worst transient direction grew by
{_fmt(stable['repeated_root_norm_check']['euclidean_covariance_amplification_at_peak'], 7)}x
in Euclidean Frobenius norm at step
{stable['repeated_root_norm_check']['peak_step']}. In the Lyapunov-adapted norm
it had already contracted to
{_fmt(stable['repeated_root_norm_check']['lyapunov_norm_ratio_at_peak'], 7)},
below the theoretical bound
{_fmt(stable['repeated_root_norm_check']['rho_bar_bound_at_peak'], 7)}.

This is the practical reason BridgeLearn exposes both spectral radius and
`cond(P)`: the former describes asymptotic stability, while the latter prices
transient amplification and conversion back to Euclidean error bounds.

Artifacts:

- [transient amplification](artifacts/companion_stability/companion_transient_amplification.png)
- [Euclidean versus Lyapunov norms](artifacts/companion_stability/companion_lyapunov_norm_comparison.png)
- [conditioning over the stability triangle](artifacts/companion_stability/companion_stability_triangle_conditioning.png)
- [case table](artifacts/companion_stability/companion_cases.csv)

# 4. Momentum reachability

For heavy-ball dynamics with fixed momentum, the pole-radius floor is

```text
rho_min = sqrt(mu),
```

so the corresponding asymptotic covariance contraction floor is `mu` per
update. Reducing variance by a ratio r therefore requires at least

```text
N >= ceil(log(r) / log(mu)).
```

For r={reach['variance_ratio']} and mu=0.9, this gives
{reach['minimum_horizon_at_mu_0.9']} updates even before noise, command slew,
and non-normality are charged.

The actuator experiment asked for five pure one-step marginal contractions.
With momentum fixed at 0.9, none passed the full transition and companion
feasibility checks. With momentum allowed to change, all five were exactly or
closely realized; the unconstrained search selected low momentum because that
was the only way to match both the desired adjacent cross-covariance and next
variance.

| Target ratio | Fixed predicted | Fixed feasible | Adaptive predicted | Selected adaptive mu |
|---:|---:|:---:|---:|---:|
"""
    for fixed_row, adaptive_row in zip(fixed, adaptive, strict=True):
        text += (
            f"| {fixed_row['target_variance_ratio']:.2f} "
            f"| {fixed_row['predicted_variance_ratio']:.6f} "
            f"| {'yes' if fixed_row['feasible'] else 'no'} "
            f"| {adaptive_row['predicted_variance_ratio']:.6f} "
            f"| {adaptive_row['selected_momentum']:.4f} |\n"
        )

    text += f"""

Artifacts:

- [minimum-horizon curve](artifacts/momentum_reachability/momentum_minimum_horizon.png)
- [one-step reachability](artifacts/momentum_reachability/momentum_one_step_reachability.png)
- [momentum lower-bound sweep](artifacts/momentum_reachability/momentum_lower_bound_sweep.png)
- [one-step results](artifacts/momentum_reachability/momentum_one_step_results.csv)

# Interpretation

The experiments support four narrow conclusions.

1. Treating sharpness as a slow state captures path dependence that a static
   response curve misses, and it can warn about a future edge crossing before
   the current command is unsafe.
2. In a cold AR(2) regime, temporal probe design matters much more than merely
   increasing white amplitude. The antithetic pair directly repairs the
   `(1,-1)` information direction.
3. A spectral-radius check alone is insufficient near repeated roots. A
   Lyapunov metric and its condition number are operationally meaningful
   diagnostics.
4. Momentum is a reachability actuator, not just a smoothing constant. High
   fixed momentum imposes a physical cooling horizon and can make a requested
   transition impossible even when a scalar variance target looks benign.

# Limitations

- Every plant here is scalar or 2x2 and synthetic.
- The sharpness law is the same phenomenological form assumed by the library;
  the experiment checks identification and planning behavior under that model,
  not model universality.
- The antithetic result assumes the external probe is known and removed from
  the regression response. Unknown or clipped probe realization would require
  additional calibration.
- The companion experiment is local linear analysis. Neural training can move
  between blocks and Hessian eigendirections.
- The momentum actuator still targets a scalar marginal transition rather than
  an exact augmented-state Schrödinger bridge. Infeasibility therefore includes
  both the momentum floor and cross-time coupling mismatch.
- No result here demonstrates improved task loss, generalization, CAROM
  routing, predictive-coding inference, or RL returns.

# Reproduction

From this directory:

```bash
python -m pip install --no-deps vendor/bridgelearn-0.3.0-py3-none-any.whl
python run_all.py --output artifacts
```

The complete machine-readable summary is in [`summary.json`](summary.json).
"""
    path.write_text(text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("artifacts"),
        help="Directory for generated experiment artifacts.",
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    output = args.output if args.output.is_absolute() else root / args.output
    output.mkdir(parents=True, exist_ok=True)

    summary: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "environment": environment_record(),
    }
    summary["dynamic_sharpness"] = run_sharpness(output / "dynamic_sharpness")
    summary["antithetic_identification"] = run_antithetic(
        output / "antithetic_identification"
    )
    summary["companion_stability"] = run_stability(output / "companion_stability")
    summary["momentum_reachability"] = run_reachability(
        output / "momentum_reachability"
    )
    write_json(root / "summary.json", summary)
    _write_report(root / "REPORT.md", summary)
    print(f"Wrote results to {output}")
    print(f"Wrote report to {root / 'REPORT.md'}")
    print(f"Wrote summary to {root / 'summary.json'}")


if __name__ == "__main__":
    main()
