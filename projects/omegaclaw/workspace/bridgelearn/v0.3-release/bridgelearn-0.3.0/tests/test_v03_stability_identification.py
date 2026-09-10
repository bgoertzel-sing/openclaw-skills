import numpy as np

from bridgelearn import (
    AR2AdequacyObserver,
    ForgettingFactorAR2Observer,
    GrayBoxMomentumObserver,
    damping_regime,
    inside_stability_triangle,
    lyapunov_metric,
    spectral_radius,
    underdamped_contraction_floor,
)


def test_companion_triangle_and_lyapunov_condition() -> None:
    c1, c2 = 1.6, -0.81
    assert inside_stability_triangle(c1, c2)
    assert damping_regime(c1, c2) == "underdamped"
    assert np.isclose(spectral_radius(c1, c2), 0.9)
    assert np.isclose(underdamped_contraction_floor(0.81), 0.9)
    metric, rho_bar, condition = lyapunov_metric(c1, c2)
    assert metric.shape == (2, 2)
    assert np.min(np.linalg.eigvalsh(metric)) > 0.0
    assert 0.9 < rho_bar < 1.0
    assert np.isfinite(condition)


def test_gray_box_recovers_curvature_and_noise_under_varying_commands() -> None:
    rng = np.random.default_rng(4)
    steps = 220
    replicas = 600
    h_true = 2.4
    nu_true = 3.0
    eta = 0.035 + 0.02 * (1.0 + np.sin(np.linspace(0.0, 8.0, steps - 1)))
    mu = 0.65 + 0.2 * (1.0 + np.cos(np.linspace(0.0, 5.0, steps - 1))) / 2.0
    batch = np.where(np.arange(steps - 1) % 3 == 0, 32.0, 128.0)
    z = np.zeros((steps, replicas))
    z[0] = rng.normal(scale=0.2, size=replicas)
    z[1] = rng.normal(scale=0.2, size=replicas)
    for k in range(1, steps - 1):
        xi = rng.normal(scale=np.sqrt(nu_true / batch[k]), size=replicas)
        z[k + 1] = (
            (1.0 + mu[k] - eta[k] * h_true) * z[k]
            - mu[k] * z[k - 1]
            - eta[k] * xi
        )
    estimate = GrayBoxMomentumObserver(minimum_samples=100).estimate(
        [z], [eta], [mu], [batch]
    )
    assert abs(estimate.curvature[0] - h_true) < 0.04
    assert abs(estimate.noise_scale[0] - nu_true) < 0.18
    assert estimate.confidence[0] > 0.8
    assert estimate.contrast_standard_error[0] < 0.01


def test_ar2_adequacy_exposes_condition_and_contrast_uncertainty() -> None:
    rng = np.random.default_rng(7)
    series = np.zeros((120, 200))
    for k in range(1, 119):
        series[k + 1] = 1.75 * series[k] - 0.78 * series[k - 1] + 0.01 * rng.normal(size=200)
    estimate = AR2AdequacyObserver().estimate([series])
    assert estimate.regressor_condition[0] > 1.0
    assert estimate.contrast_standard_error[0] >= 0.0
    assert np.isclose(estimate.c1_minus_c2[0], estimate.phi1[0] - estimate.phi2[0])


def test_forgetting_factor_observer_declares_rate_limit() -> None:
    observer = ForgettingFactorAR2Observer(blocks=1, forgetting=0.98, slew_fraction=0.2)
    rng = np.random.default_rng(3)
    z0 = np.zeros(100)
    z1 = rng.normal(size=100)
    for _ in range(80):
        z2 = 1.2 * z1 - 0.4 * z0 + 0.03 * rng.normal(size=100)
        estimate = observer.update(z0[None, :], z1[None, :], z2[None, :])
        z0, z1 = z1, z2
    assert abs(estimate.c1[0] - 1.2) < 0.05
    assert abs(estimate.c2[0] + 0.4) < 0.05
    assert np.isclose(estimate.effective_memory, 50.0)
    assert np.isclose(estimate.recommended_coefficient_slew, 0.004)


def test_companion_small_gain_report_exposes_conditioning_penalty() -> None:
    from bridgelearn import companion_small_gain_bound

    stable = companion_small_gain_bound(
        1.6,
        -0.81,
        disturbance_lipschitz=0.01,
        disturbance_bound=1e-3,
    )
    assert stable.condition_satisfied
    assert np.isfinite(stable.asymptotic_bound)
    assert stable.lyapunov_condition >= 1.0
    assert 0.0 < stable.recommended_matrix_slew < 1.0

    unstable_gain = companion_small_gain_bound(
        1.6,
        -0.81,
        disturbance_lipschitz=0.5,
        disturbance_bound=1e-3,
    )
    assert not unstable_gain.condition_satisfied
    assert np.isinf(unstable_gain.asymptotic_bound)
