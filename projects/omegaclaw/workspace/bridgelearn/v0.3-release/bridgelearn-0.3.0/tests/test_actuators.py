import numpy as np

from bridgelearn import (
    ChannelObservation,
    GaussianTransition,
    LocalDynamics,
    StepBatchActuator,
)


def test_shared_batch_actuator_matches_known_clipping_case() -> None:
    dynamics = LocalDynamics(
        variance=[0.08],
        curvature=[1.0],
        noise_scale=[64.0],
        step_size=[0.8],
        effective_batch=128.0,
    )
    observation = ChannelObservation(
        state=dynamics.state(),
        reference=dynamics.reference_transition(),
        local_dynamics=dynamics,
    )
    target = GaussianTransition(
        contraction=np.array([0.2]),
        innovation=np.array([0.0768]),
    )
    actuator = StepBatchActuator(
        step_bounds=(0.0, 1.5),
        batch_bounds=(32.0, 512.0),
        max_log_step_change=None,
        max_log_batch_change=None,
        relative_tolerance=0.05,
    )
    plan = actuator.realize(target=target, observation=observation)
    assert np.isclose(plan.controls["effective_batch"], 512.0)
    assert np.isclose(plan.controls["step_size"][0], 0.7804878048780488)
    np.testing.assert_allclose(plan.predicted_variance, [0.08], atol=1e-12)
    assert plan.feasible
