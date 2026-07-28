import numpy as np

from bridgelearn import GaussianKLProjector, GaussianTransition


def test_kl_projector_hits_target_exactly() -> None:
    projector = GaussianKLProjector()
    current = np.array([0.06, 0.03])
    target = np.array([0.065, 0.02])
    reference = GaussianTransition(
        contraction=np.array([0.8, 0.7]),
        innovation=np.array([0.02, 0.01]),
    )
    projected = projector.project(
        current_variance=current,
        target_variance=target,
        reference=reference,
    )
    np.testing.assert_allclose(projected.next_variance(current), target, atol=1e-12)
    assert np.all(projected.innovation >= 0.0)


def test_kl_projector_is_local_minimum_on_exact_constraint() -> None:
    projector = GaussianKLProjector()
    current = np.array([0.06])
    target = np.array([0.05])
    reference = GaussianTransition(
        contraction=np.array([0.82]),
        innovation=np.array([0.012]),
    )
    optimum = projector.project(
        current_variance=current,
        target_variance=target,
        reference=reference,
    )
    optimum_value = projector.objective(
        current_variance=current,
        candidate=optimum,
        reference=reference,
    )[0]
    for delta in (-0.05, -0.01, 0.01, 0.05):
        candidate_a = optimum.contraction[0] + delta
        if candidate_a**2 * current[0] >= target[0]:
            continue
        candidate = GaussianTransition(
            contraction=np.array([candidate_a]),
            innovation=np.array([target[0] - candidate_a**2 * current[0]]),
        )
        candidate_value = projector.objective(
            current_variance=current,
            candidate=candidate,
            reference=reference,
        )[0]
        assert optimum_value <= candidate_value + 1e-12
