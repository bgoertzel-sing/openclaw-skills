from pathlib import Path
import importlib.util

import numpy as np
import torch


SCRIPT = Path(__file__).parents[1] / "scripts" / "run_h0_cpu.py"
SPEC = importlib.util.spec_from_file_location("run_h0_cpu", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def test_generator_labels_and_single_factor_counterfactual() -> None:
    tokens, factors, labels = MODULE.make_examples(128, 7)
    assert torch.equal(labels, (factors * (2 ** torch.arange(5))).sum(dim=1))
    edited = MODULE.counterfactual_tokens(factors, tokens[:, -1], 3)
    assert torch.equal(edited[:, -1], tokens[:, -1])
    differences = edited[:, 1:6] != tokens[:, 1:6]
    assert torch.all(differences.sum(dim=1) == 1)
    assert torch.all(differences[:, 3])


def test_bootstrap_closure_is_one_for_teacher_match() -> None:
    base = np.array([2.0, 1.0, 3.0, 2.5])
    teacher = np.array([0.2, 0.1, 0.3, 0.25])
    result = MODULE.bootstrap_closure(
        base, teacher, teacher, higher_is_better=False, seed=1, samples=100
    )
    assert result["estimate"] == 1.0
    assert result["ci95"] == [1.0, 1.0]


def test_factor_scores_track_oracle_bits() -> None:
    labels = torch.arange(32)
    scores = MODULE.factor_scores(MODULE.oracle_logits(labels, 6.0))
    for factor in range(5):
        expected = 2 * ((labels >> factor) & 1) - 1
        assert torch.equal(scores[:, factor].sign().long(), expected)
