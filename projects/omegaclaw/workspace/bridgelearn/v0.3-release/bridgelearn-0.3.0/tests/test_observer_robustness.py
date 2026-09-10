import numpy as np

from bridgelearn import (
    AR2AdequacyObserver,
    CenteredWidthObserver,
    IQRScale,
    VarianceScale,
)


def test_ar2_observer_detects_momentum_like_memory() -> None:
    rng = np.random.default_rng(4)
    x = np.zeros((400, 64))
    for step in range(2, x.shape[0]):
        x[step] = 1.25 * x[step - 1] - 0.45 * x[step - 2] + 0.1 * rng.normal(size=64)
    estimate = AR2AdequacyObserver().estimate([x])
    assert estimate.ar1_adequacy[0] < 0.5
    assert np.isclose(estimate.phi1[0], 1.25, atol=0.08)
    assert np.isclose(estimate.phi2[0], -0.45, atol=0.08)


def test_robust_width_resists_heavy_tail_outlier() -> None:
    rng = np.random.default_rng(7)
    base = rng.normal(size=(1024, 1))
    contaminated = base.copy()
    contaminated[0, 0] = 1000.0
    classical = CenteredWidthObserver(center_alpha=1.0, scale=VarianceScale())
    robust = CenteredWidthObserver(center_alpha=1.0, scale=IQRScale())
    classical_width, _ = classical.update([contaminated])
    robust_width, _ = robust.update([contaminated])
    assert classical_width[0] > 100.0
    assert 0.5 < robust_width[0] < 2.0
