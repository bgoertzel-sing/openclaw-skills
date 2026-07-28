from __future__ import annotations

from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np

from bridgelearn import (
    ChannelObservation,
    GaussianTransition,
    LocalDynamics,
    MomentumStepBatchActuator,
    underdamped_contraction_floor,
)

from .common import write_csv, write_json


def _observation(
    *,
    variance: float,
    previous_variance: float,
    lag_covariance: float,
    curvature: float,
    step_size: float,
    momentum: float,
) -> ChannelObservation:
    dynamics = LocalDynamics(
        variance=[variance],
        previous_variance=[previous_variance],
        lag_covariance=[lag_covariance],
        curvature=[curvature],
        curvature_lower=[curvature],
        curvature_upper=[curvature],
        noise_scale=[0.0],
        step_size=[step_size],
        momentum=[momentum],
        effective_batch=128.0,
        structural_adequacy=[1.0],
        curvature_adequacy=[1.0],
        coefficient_slew_limit=[1e9],
        trust_region_step=[3.7],
    )
    return ChannelObservation(
        state=dynamics.state(),
        reference=dynamics.reference_transition(),
        local_dynamics=dynamics,
    )


def _actuator(*, fixed_momentum: bool, lower_momentum: float = 0.0) -> MomentumStepBatchActuator:
    return MomentumStepBatchActuator(
        step_bounds=(1e-5, 3.7),
        momentum_bounds=((0.9 if fixed_momentum else lower_momentum), 0.9),
        batch_values=(128.0,),
        control_momentum=not fixed_momentum,
        momentum_grid_points=181,
        safety_offset=0.02,
        triangle_margin=1e-6,
        max_spectral_radius=0.99999,
        max_lyapunov_condition=1e10,
        rho_bar_slack=0.001,
        relative_tolerance=0.02,
        absolute_tolerance=1e-12,
        max_log_step_change=None,
        max_momentum_change=None,
        max_log_batch_change=None,
        compute_price=0.0,
        conditioning_weight=0.0,
        smoothness_weight=0.0,
    )


def run(output_dir: Path) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)

    initial_variance = 0.08
    terminal_variance = 0.005
    total_ratio = terminal_variance / initial_variance
    initial_momentum = 0.9
    initial_step = 0.6
    curvature = 1.0
    # This lag covariance is the stationary lag of the initial companion plant
    # before cooling. Innovation is then set to zero to isolate reachability.
    previous_variance = initial_variance
    lag_covariance = 0.05473684210526316
    observation = _observation(
        variance=initial_variance,
        previous_variance=previous_variance,
        lag_covariance=lag_covariance,
        curvature=curvature,
        step_size=initial_step,
        momentum=initial_momentum,
    )

    momentum_grid = np.linspace(0.01, 0.99, 197)
    amplitude_floor = np.asarray(
        [underdamped_contraction_floor(value) for value in momentum_grid]
    )
    covariance_floor = amplitude_floor**2
    minimum_horizon = np.ceil(np.log(total_ratio) / np.log(covariance_floor)).astype(int)

    plt.figure(figsize=(9.5, 5.5))
    plt.plot(momentum_grid, minimum_horizon)
    plt.axvline(initial_momentum, linestyle="--", label="mu=0.9")
    plt.xlabel("fixed momentum mu")
    plt.ylabel("minimum updates from covariance floor")
    plt.title("Momentum-imposed cooling horizon for V: 0.08 to 0.005")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "momentum_minimum_horizon.png", dpi=180)
    plt.close()

    ratios = np.asarray([0.95, 0.90, 0.80, 0.70, 0.50])
    fixed = _actuator(fixed_momentum=True)
    adaptive = _actuator(fixed_momentum=False, lower_momentum=0.0)
    rows = []
    for ratio in ratios:
        target = GaussianTransition([np.sqrt(ratio)], [0.0])
        for mode, actuator in (("fixed_mu_0.9", fixed), ("adaptive_mu", adaptive)):
            plan = actuator.realize(target=target, observation=observation)
            rows.append(
                {
                    "mode": mode,
                    "target_variance_ratio": ratio,
                    "feasible": bool(plan.feasible),
                    "selected_step_size": float(plan.controls["step_size"][0]),
                    "selected_momentum": float(plan.controls["momentum"][0]),
                    "predicted_variance_ratio": float(
                        plan.predicted_variance[0] / initial_variance
                    ),
                    "relative_target_error": float(plan.error[0]),
                    "spectral_radius": float(
                        plan.diagnostics["companion_spectral_radius"][0]
                    ),
                    "lyapunov_condition": float(
                        plan.diagnostics["companion_lyapunov_condition"][0]
                    ),
                    "regime": plan.diagnostics["companion_regime"][0],
                    "momentum_floor_binding": bool(
                        plan.diagnostics["momentum_floor_binding_fraction"] > 0.0
                    ),
                }
            )

    plt.figure(figsize=(9.5, 5.5))
    for mode in ("fixed_mu_0.9", "adaptive_mu"):
        selected = [row for row in rows if row["mode"] == mode]
        plt.plot(
            [row["target_variance_ratio"] for row in selected],
            [row["predicted_variance_ratio"] for row in selected],
            marker="o",
            label=mode,
        )
    plt.plot(ratios, ratios, linestyle="--", label="exact realization")
    plt.xlabel("requested next-variance ratio")
    plt.ylabel("actuator-predicted next-variance ratio")
    plt.title("One-step momentum reachability")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "momentum_one_step_reachability.png", dpi=180)
    plt.close()

    lower_bounds = np.asarray([0.0, 0.1, 0.3, 0.5, 0.7, 0.85, 0.9])
    bound_rows = []
    target_ratio = 0.70
    target = GaussianTransition([np.sqrt(target_ratio)], [0.0])
    for lower in lower_bounds:
        if np.isclose(lower, 0.9):
            actuator = _actuator(fixed_momentum=True)
        else:
            actuator = _actuator(fixed_momentum=False, lower_momentum=float(lower))
        plan = actuator.realize(target=target, observation=observation)
        bound_rows.append(
            {
                "momentum_lower_bound": lower,
                "feasible": bool(plan.feasible),
                "selected_momentum": float(plan.controls["momentum"][0]),
                "selected_step_size": float(plan.controls["step_size"][0]),
                "predicted_variance_ratio": float(
                    plan.predicted_variance[0] / initial_variance
                ),
                "relative_target_error": float(plan.error[0]),
                "spectral_radius": float(
                    plan.diagnostics["companion_spectral_radius"][0]
                ),
            }
        )

    plt.figure(figsize=(9.5, 5.5))
    plt.plot(
        lower_bounds,
        [row["predicted_variance_ratio"] for row in bound_rows],
        marker="o",
        label="predicted ratio",
    )
    plt.axhline(target_ratio, linestyle="--", label="requested ratio")
    plt.xlabel("minimum allowed momentum")
    plt.ylabel("predicted next-variance ratio")
    plt.title("Cooling degrades as the momentum floor is raised")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "momentum_lower_bound_sweep.png", dpi=180)
    plt.close()

    write_csv(output_dir / "momentum_one_step_results.csv", rows, list(rows[0]))
    write_csv(
        output_dir / "momentum_lower_bound_sweep.csv",
        bound_rows,
        list(bound_rows[0]),
    )
    horizon_rows = [
        {
            "momentum": momentum_grid[index],
            "amplitude_contraction_floor": amplitude_floor[index],
            "covariance_contraction_floor": covariance_floor[index],
            "minimum_horizon": minimum_horizon[index],
        }
        for index in range(momentum_grid.size)
    ]
    write_csv(
        output_dir / "momentum_horizon_curve.csv",
        horizon_rows,
        list(horizon_rows[0]),
    )

    fixed_rows = [row for row in rows if row["mode"] == "fixed_mu_0.9"]
    adaptive_rows = [row for row in rows if row["mode"] == "adaptive_mu"]
    mu_index = int(np.argmin(np.abs(momentum_grid - initial_momentum)))
    exact_mu09_horizon = int(
        np.ceil(np.log(total_ratio) / np.log(initial_momentum))
    )
    summary = {
        "experiment": "momentum_reachability",
        "initial_variance": initial_variance,
        "terminal_variance": terminal_variance,
        "variance_ratio": total_ratio,
        "initial_momentum": initial_momentum,
        "initial_amplitude_floor": underdamped_contraction_floor(initial_momentum),
        "initial_covariance_floor": initial_momentum,
        "minimum_horizon_at_mu_0.9": exact_mu09_horizon,
        "grid_horizon_near_mu_0.9": int(minimum_horizon[mu_index]),
        "one_step": {
            "fixed_momentum_feasible_count": int(
                sum(bool(row["feasible"]) for row in fixed_rows)
            ),
            "adaptive_momentum_feasible_count": int(
                sum(bool(row["feasible"]) for row in adaptive_rows)
            ),
            "total_targets": int(ratios.size),
            "fixed_results": fixed_rows,
            "adaptive_results": adaptive_rows,
        },
        "target_ratio_0.70_lower_bound_sweep": bound_rows,
        "artifacts": {
            "horizon_plot": "momentum_minimum_horizon.png",
            "one_step_plot": "momentum_one_step_reachability.png",
            "lower_bound_plot": "momentum_lower_bound_sweep.png",
            "one_step_csv": "momentum_one_step_results.csv",
            "lower_bound_csv": "momentum_lower_bound_sweep.csv",
            "horizon_csv": "momentum_horizon_curve.csv",
        },
    }
    write_json(output_dir / "summary.json", summary)
    return summary
