import numpy as np
import pytest

from comcrit import ModulePartition, fixture_quadratic as fq, selftest
from comcrit.stats import effect_size_precheck, spearman


def test_partition_disjointness():
    with pytest.raises(ValueError):
        ModulePartition(index_modules={"a": np.arange(4), "b": np.arange(2, 6)},
                        dim=8)


def test_gate_algebra():
    part = fq.default_partition(d=8, M=2)
    assert np.all(part.gate_vec(None) == 1.0)
    g = part.gate_vec((["m0"], 0.25))
    assert np.all(g[part.mask("m0")] == 0.25) and np.all(g[part.mask("m1")] == 1.0)


def test_precheck_strengthen_loop():
    scale = {"v": 1.0}
    eff = lambda: np.array([scale["v"]] * 10)
    res = effect_size_precheck(eff, floor=1.0,
                               strengthen=lambda: scale.update(v=scale["v"] * 3),
                               min_ratio=5.0, max_iterations=3)
    assert res.passed and res.iterations_used == 2


def test_spearman_perfect():
    x = np.random.default_rng(0).normal(size=50)
    assert spearman(x, 2 * x + 1) == pytest.approx(1.0)


def test_selftest_passes():
    rep = selftest(verbose=False)
    assert rep["passed"], rep
