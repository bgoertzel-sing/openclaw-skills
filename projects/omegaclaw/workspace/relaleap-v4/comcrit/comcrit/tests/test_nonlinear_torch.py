import pytest

torch = pytest.importorskip("torch")

from comcrit.fixture_nonlinear_torch import (
    FixtureConfig, gate_dict, run_family)


def test_gate_dict_pair():
    gate = gate_dict((("layer1", "layer2"), 0.1))
    assert gate["W1"] == gate["b2"] == 0.1
    assert gate["W3"] == gate["b3"] == 1.0


def test_nonlinear_fixture_quick_smoke():
    result = run_family(FixtureConfig(
        "B1_input_permutation", seed=3, lr=1e-3, n_probe_states=1,
        pretrain_steps=2, noise_replicates=2))
    assert result["probe_states"] == 1
    assert set(result["cells"]) == {"1", "2", "5", "10", "25"}
    assert result["cells"]["1"]["n"] == 6
