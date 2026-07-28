"""Configuration skeleton for a BridgeLearn 0.3 momentum shadow run.

This file deliberately does not run a scientific experiment.  It shows how the
v0.3 sharpness, identification, probing, planning, and companion-actuation
objects fit together.  Application code must provide centered state histories,
lag covariances, task-specific controls, and a signed probe-injection callback.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from bridgelearn import (
    AntitheticProbePolicy,
    BridgeController,
    Channel,
    DominantSharpnessCoordinator,
    DynamicsAdapter,
    FixedReferencePolicy,
    GaussianTransition,
    LocalDynamics,
    MomentumStepBatchActuator,
    SharpnessAwareReferenceBridgePlanner,
    SharpnessPlant,
)


@dataclass
class ShadowSystem:
    variance: np.ndarray
    previous_variance: np.ndarray
    lag_covariance: np.ndarray
    curvature_lower: np.ndarray
    curvature: np.ndarray
    curvature_upper: np.ndarray
    curvature_confidence: np.ndarray
    noise_scale: np.ndarray
    step_size: np.ndarray
    momentum: np.ndarray
    effective_batch: float
    structural_adequacy: np.ndarray
    coefficient_slew_limit: np.ndarray
    contrast_standard_error: np.ndarray
    regressor_condition: np.ndarray
    lyapunov_condition: np.ndarray


sharpness = SharpnessPlant(
    gamma_p=1e-3,
    gamma_r=0.2,
    safety_offset=0.1,
    forgetting=0.995,
    uncertainty_scale=2.5,
)

probe = AntitheticProbePolicy(
    contrast_se_threshold=0.04,
    condition_threshold=500.0,
    cold_variance=1e-2,
    max_realized_variance=2e-5,
    max_total_realized_variance=2e-3,
    amplitude_levels=(0.5, 1.0),
)

planner = SharpnessAwareReferenceBridgePlanner(
    terminal_variance=[5e-3, 5e-3],
    total_steps=4_000,
    reference_policy=FixedReferencePolicy(
        GaussianTransition(
            contraction=[0.99, 0.99],
            innovation=[1e-4, 1e-4],
        )
    ),
    probe_policy=probe,
    sharpness_model=sharpness,
    max_relative_funnel_width=0.75,
    freeze_on_inadequacy=True,
)

actuator = MomentumStepBatchActuator(
    step_bounds=(1e-6, 2e-3),
    momentum_bounds=(0.0, 0.95),
    batch_values=(32, 64, 128, 256, 512),
    control_momentum=True,
    max_spectral_radius=0.995,
    max_lyapunov_condition=1e4,
    compute_price=2e-3,
    dominant_coordinator=DominantSharpnessCoordinator(
        safety_offset=0.1,
        maximum_utilization=0.95,
    ),
)


def read_dynamics(system: ShadowSystem) -> LocalDynamics:
    return LocalDynamics(
        variance=system.variance,
        previous_variance=system.previous_variance,
        lag_covariance=system.lag_covariance,
        curvature=system.curvature,
        curvature_lower=system.curvature_lower,
        curvature_upper=system.curvature_upper,
        curvature_adequacy=system.curvature_confidence,
        noise_scale=system.noise_scale,
        step_size=system.step_size,
        momentum=system.momentum,
        effective_batch=system.effective_batch,
        structural_adequacy=system.structural_adequacy,
        coefficient_slew_limit=system.coefficient_slew_limit,
    )


def read_metadata(system: ShadowSystem, _dynamics: LocalDynamics) -> dict[str, object]:
    c1 = 1.0 + system.momentum - system.step_size * system.curvature
    c2 = -system.momentum
    return {
        "contrast_standard_error": system.contrast_standard_error,
        "regressor_condition": system.regressor_condition,
        "lyapunov_condition": system.lyapunov_condition,
        "c1": c1,
        "c2": c2,
        "sharpness_progress_signal": np.ones_like(system.curvature),
    }


def shadow_apply(_system: ShadowSystem, _controls: dict[str, object]) -> None:
    """Shadow mode computes commands but does not mutate the application."""


adapter = DynamicsAdapter(
    read_dynamics=read_dynamics,
    read_metadata=read_metadata,
    apply_controls=shadow_apply,
    actuator=actuator,
)

controller = BridgeController(
    {
        "weights": Channel(
            name="weights",
            adapter=adapter,
            planner=planner,
        )
    },
    mode="shadow",
)


def update_sharpness_model(
    *,
    previous_curvature: np.ndarray,
    current_curvature: np.ndarray,
    previous_step: np.ndarray,
    previous_momentum: np.ndarray,
    squared_update_norm: np.ndarray,
) -> None:
    """Call at the observer/control interval before planning the next command."""

    sharpness.update(
        previous_curvature=previous_curvature,
        current_curvature=current_curvature,
        step_size=previous_step,
        momentum=previous_momentum,
        progress_signal=squared_update_norm,
    )


if __name__ == "__main__":
    print("BridgeLearn 0.3 momentum shadow configuration constructed.")
    print("No scientific simulation is run by this skeleton.")
