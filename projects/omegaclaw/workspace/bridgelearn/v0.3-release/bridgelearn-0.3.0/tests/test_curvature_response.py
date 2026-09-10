import numpy as np

from bridgelearn import LocalDynamics


def test_endogenous_curvature_inversion() -> None:
    dynamics = LocalDynamics(
        variance=[0.1],
        curvature=[2.0],
        curvature_slope=[3.0],
        noise_scale=[1.0],
        step_size=[0.1],
        effective_batch=32.0,
    )
    target = np.array([0.5])
    step = dynamics.step_for_contraction(target)
    np.testing.assert_allclose(dynamics.contraction_at(step), target, atol=1e-10)
