import numpy as np

from bridgelearn import GaussianKLProjector, GaussianTransition


def test_projector_invariants_over_parameter_grid() -> None:
    projector = GaussianKLProjector()
    for current in np.geomspace(1e-5, 1.0, 12):
        for target in np.geomspace(1e-5, 1.0, 12):
            for a0 in (-0.8, 0.0, 0.8):
                reference = GaussianTransition([a0], [0.01])
                projected = projector.project(
                    current_variance=np.array([current]),
                    target_variance=np.array([target]),
                    reference=reference,
                )
                assert projected.innovation[0] >= 0.0
                assert projected.contraction[0] ** 2 * current <= target + 1e-12
                np.testing.assert_allclose(
                    projected.next_variance([current]), [target], atol=1e-11
                )
