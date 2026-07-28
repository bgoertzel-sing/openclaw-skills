import numpy as np

from bridgelearn import GaussianBridgePath


def test_bridge_endpoints_and_peak_parameterization() -> None:
    path = GaussianBridgePath.from_peak(
        start_variance=[0.06, 0.025],
        peak_variance=[0.08, 0.05],
        terminal_variance=[0.005, 0.015],
    )
    np.testing.assert_allclose(path.variance(0.0), [0.06, 0.025], atol=1e-12)
    np.testing.assert_allclose(path.variance(1.0), [0.005, 0.015], atol=1e-12)
    np.testing.assert_allclose(path.peak_variance(), [0.08, 0.05], atol=1e-12)
    peaks = path.peak_progress()
    assert 0.0 < peaks[0] < 0.5
    assert 0.0 < peaks[1] < 1.0


def test_endpoint_asymmetry_controls_peak_direction() -> None:
    early = GaussianBridgePath(
        start_variance=[0.09],
        terminal_variance=[0.01],
        diffusion_budget=[0.2],
    )
    late = GaussianBridgePath(
        start_variance=[0.01],
        terminal_variance=[0.09],
        diffusion_budget=[0.2],
    )
    assert early.peak_progress()[0] < 0.5
    assert late.peak_progress()[0] > 0.5
