import numpy as np

from bridgelearn import GaussianBridgePath, LinearGaussianBridgePath


def test_linear_gaussian_bridge_endpoints_and_transitions() -> None:
    path = LinearGaussianBridgePath(
        start_variance=[0.06, 0.02],
        terminal_variance=[0.005, 0.04],
        horizon_steps=40,
        reference_contraction=[0.98, 0.90],
        reference_innovation=[0.002, 0.004],
    )
    grid = path.covariance_grid()
    np.testing.assert_allclose(grid[0], [0.06, 0.02], atol=1e-12)
    np.testing.assert_allclose(grid[-1], [0.005, 0.04], atol=1e-12)
    for step in range(path.horizon_steps):
        transition = path.transition_at(step)
        np.testing.assert_allclose(
            transition.next_variance(grid[step]), grid[step + 1], atol=1e-11
        )
        assert np.all(transition.innovation >= 0.0)


def test_random_walk_limit_matches_brownian_path() -> None:
    horizon = 80
    budget = 0.2
    discrete = LinearGaussianBridgePath(
        start_variance=[0.06],
        terminal_variance=[0.005],
        horizon_steps=horizon,
        reference_contraction=[1.0],
        reference_innovation=[budget / horizon],
    )
    brownian = GaussianBridgePath(
        start_variance=[0.06],
        terminal_variance=[0.005],
        diffusion_budget=[budget],
    )
    expected = np.asarray(
        [brownian.variance(step / horizon)[0] for step in range(horizon + 1)]
    )
    np.testing.assert_allclose(discrete.covariance_grid()[:, 0], expected, atol=1e-12)
