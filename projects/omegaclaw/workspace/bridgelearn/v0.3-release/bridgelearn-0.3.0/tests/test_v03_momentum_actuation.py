import numpy as np

from bridgelearn import (
    ChannelObservation,
    DominantSharpnessCoordinator,
    GaussianTransition,
    LocalDynamics,
    MomentumStepBatchActuator,
    StepBatchActuator,
    inside_stability_triangle,
)


def _target_from_controls(dynamics: LocalDynamics, eta: float, mu: float, batch: float) -> GaussianTransition:
    h = float(dynamics.curvature[0])
    c1 = 1.0 + mu - eta * h
    c2 = -mu
    v = float(dynamics.variance[0])
    vp = float(dynamics.previous_variance[0])
    lag = float(dynamics.lag_covariance[0])
    cross = c1 * v + c2 * lag
    contraction = cross / v
    next_variance = c1**2 * v + c2**2 * vp + 2.0 * c1 * c2 * lag
    next_variance += eta**2 * float(dynamics.noise_scale[0]) / batch
    innovation = next_variance - contraction**2 * v
    return GaussianTransition([contraction], [innovation])


def test_momentum_actuator_realizes_marginal_transition_inside_triangle() -> None:
    dynamics = LocalDynamics(
        variance=[0.08],
        previous_variance=[0.07],
        lag_covariance=[0.05],
        curvature=[2.0],
        curvature_lower=[2.0],
        curvature_upper=[2.0],
        noise_scale=[64.0],
        step_size=[0.10],
        momentum=[0.80],
        effective_batch=128.0,
        coefficient_slew_limit=[1.0],
    )
    target = _target_from_controls(dynamics, eta=0.08, mu=0.70, batch=256.0)
    observation = ChannelObservation(
        state=dynamics.state(),
        reference=dynamics.reference_transition(),
        local_dynamics=dynamics,
    )
    actuator = MomentumStepBatchActuator(
        step_bounds=(0.001, 0.5),
        momentum_bounds=(0.0, 0.95),
        batch_bounds=(32.0, 512.0),
        batch_quantum=32.0,
        max_log_step_change=None,
        max_momentum_change=None,
        max_log_batch_change=None,
        relative_tolerance=0.03,
    )
    plan = actuator.realize(target=target, observation=observation)
    assert plan.feasible
    c1 = float(np.asarray(plan.diagnostics["companion_c1"])[0])
    c2 = float(np.asarray(plan.diagnostics["companion_c2"])[0])
    assert inside_stability_triangle(c1, c2)
    assert plan.diagnostics["robust_stability_satisfied"]
    assert abs(plan.predicted_variance[0] - plan.target_variance[0]) < 0.004


def test_scalar_actuator_inverts_lower_funnel_and_checks_upper() -> None:
    dynamics = LocalDynamics(
        variance=[0.1],
        curvature=[1.5],
        curvature_lower=[1.0],
        curvature_upper=[2.0],
        noise_scale=[0.0],
        step_size=[0.1],
        effective_batch=32.0,
    )
    observation = ChannelObservation(
        state=dynamics.state(),
        reference=dynamics.reference_transition(),
        local_dynamics=dynamics,
    )
    actuator = StepBatchActuator(
        step_bounds=(0.0, 1.0),
        batch_bounds=(32.0, 32.0),
        max_log_step_change=None,
        max_log_batch_change=None,
    )
    plan = actuator.realize(
        target=GaussianTransition([0.5], [0.0]), observation=observation
    )
    # Lower-edge inversion requests eta=(1-.5)/1=.5, not .333 from the center.
    assert np.isclose(np.asarray(plan.controls["step_size"])[0], 0.5, atol=1e-6)
    assert plan.diagnostics["robust_stability_satisfied"]


def test_dominant_sharpness_channel_scales_all_blocks() -> None:
    coordinator = DominantSharpnessCoordinator(maximum_utilization=0.8)
    steps = np.array([0.4, 0.2])
    scaled, diagnostics = coordinator.scale_steps(
        steps, momentum=[0.0, 0.0], curvature_upper=[5.0, 2.0]
    )
    assert np.all(scaled <= steps)
    assert diagnostics["dominant_edge_utilization_after"] <= 0.8 + 1e-12


def test_momentum_diagnostics_are_recomputed_after_dominant_scaling() -> None:
    from bridgelearn import spectral_radius

    dynamics = LocalDynamics(
        variance=[0.08],
        previous_variance=[0.07],
        lag_covariance=[0.05],
        curvature=[2.0],
        curvature_lower=[2.0],
        curvature_upper=[2.5],
        noise_scale=[16.0],
        step_size=[0.1],
        momentum=[0.8],
        effective_batch=128.0,
        coefficient_slew_limit=[2.0],
    )
    observation = ChannelObservation(
        state=dynamics.state(),
        reference=dynamics.reference_transition(),
        local_dynamics=dynamics,
    )
    actuator = MomentumStepBatchActuator(
        step_bounds=(1e-4, 0.5),
        momentum_bounds=(0.8, 0.8),
        batch_bounds=(32.0, 512.0),
        max_log_step_change=None,
        max_momentum_change=None,
        max_log_batch_change=None,
        dominant_coordinator=DominantSharpnessCoordinator(
            maximum_utilization=0.2
        ),
        max_spectral_radius=0.9999,
    )
    target = _target_from_controls(dynamics, eta=0.15, mu=0.8, batch=128.0)
    plan = actuator.realize(target=target, observation=observation)
    eta = float(np.asarray(plan.controls["step_size"])[0])
    mu = float(np.asarray(plan.controls["momentum"])[0])
    expected = spectral_radius(1.0 + mu - eta * 2.5, -mu)
    observed = float(np.asarray(plan.diagnostics["companion_spectral_radius"])[0])
    assert np.isclose(observed, expected)
