#!/usr/bin/env python3
"""Tests for PLN Inference Rules v0.1."""

import sys, os, math
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from atomspace.pln_propagation import TruthValue
from atomspace.pln_inference_rules import (
    confidence_to_count, count_to_confidence,
    revision, deduction, induction, abduction, analogy,
    transitive_contribution, multi_source_revision,
    relevance_blend, apply_rule, INFERENCE_RULES,
)


# === Confidence-count conversion ===

class TestConfidenceCountConversion:
    def test_confidence_to_count_roundtrip(self):
        for conf in [0.1, 0.3, 0.5, 0.7, 0.9, 0.99]:
            n = confidence_to_count(conf)
            c = count_to_confidence(n)
            assert abs(c - conf) < 1e-9, f"Roundtrip failed for {conf}"

    def test_zero_confidence_zero_count(self):
        assert confidence_to_count(0.0) == 0.0

    def test_one_confidence_large_count(self):
        n = confidence_to_count(1.0)
        assert n > 1e5

    def test_count_to_confidence_zero(self):
        assert count_to_confidence(0.0) == 0.0

    def test_monotonic_increase(self):
        n1 = confidence_to_count(0.3)
        n2 = confidence_to_count(0.6)
        n3 = confidence_to_count(0.9)
        assert n1 < n2 < n3


# === Revision Rule ===

class TestRevision:
    def test_basic_revision(self):
        tv1 = TruthValue(0.8, 0.7)
        tv2 = TruthValue(0.6, 0.5)
        result = revision(tv1, tv2)
        assert 0.6 < result.strength < 0.8
        assert result.confidence > max(tv1.confidence, tv2.confidence)

    def test_revision_strength_weighted(self):
        tv1 = TruthValue(0.9, 0.9)
        tv2 = TruthValue(0.1, 0.1)
        result = revision(tv1, tv2)
        assert result.strength > 0.5

    def test_revision_both_zero_confidence(self):
        tv1 = TruthValue(0.8, 0.0)
        tv2 = TruthValue(0.4, 0.0)
        result = revision(tv1, tv2)
        assert result.confidence == 0.0
        assert result.strength == 0.5

    def test_revision_idempotent_strength_with_self(self):
        tv = TruthValue(0.7, 0.6)
        result = revision(tv, tv)
        assert abs(result.strength - tv.strength) < 1e-9
        assert result.confidence > tv.confidence

    def test_revision_symmetric(self):
        tv1 = TruthValue(0.3, 0.5)
        tv2 = TruthValue(0.7, 0.5)
        r1 = revision(tv1, tv2)
        r2 = revision(tv2, tv1)
        assert abs(r1.strength - r2.strength) < 1e-9
        assert abs(r1.confidence - r2.confidence) < 1e-9

    def test_revision_confidence_increase(self):
        tv1 = TruthValue(0.5, 0.5)
        tv2 = TruthValue(0.5, 0.5)
        result = revision(tv1, tv2)
        assert result.confidence > 0.5

    def test_revision_preserves_mean_equal_confidence(self):
        tv1 = TruthValue(0.6, 0.5)
        tv2 = TruthValue(0.8, 0.5)
        result = revision(tv1, tv2)
        assert abs(result.strength - 0.7) < 1e-6


# === Deduction Rule ===

class TestDeduction:
    def test_basic_deduction(self):
        tv_ab = TruthValue(0.8, 0.7)
        tv_bc = TruthValue(0.8, 0.7)
        result = deduction(tv_ab, tv_bc)
        assert abs(result.strength - 0.68) < 1e-6
        assert 0 < result.confidence <= tv_ab.confidence * tv_bc.confidence

    def test_deduction_perfect_implications(self):
        tv = TruthValue(1.0, 0.9)
        result = deduction(tv, tv)
        assert abs(result.strength - 1.0) < 1e-6

    def test_deduction_zero_strength(self):
        tv = TruthValue(0.0, 0.9)
        result = deduction(tv, tv)
        assert abs(result.strength - 1.0) < 1e-6

    def test_deduction_uncertain_inputs(self):
        tv = TruthValue(0.5, 0.9)
        result = deduction(tv, tv)
        assert abs(result.strength - 0.5) < 1e-6

    def test_deduction_confidence_discounted(self):
        tv_ab = TruthValue(0.9, 0.9)
        tv_bc = TruthValue(0.9, 0.9)
        result = deduction(tv_ab, tv_bc)
        assert result.confidence < min(tv_ab.confidence, tv_bc.confidence)

    def test_deduction_low_confidence_inputs(self):
        tv_ab = TruthValue(0.8, 0.1)
        tv_bc = TruthValue(0.8, 0.1)
        result = deduction(tv_ab, tv_bc)
        assert result.confidence < 0.05

    def test_deduction_extreme_values(self):
        for s1, s2 in [(0.0, 0.0), (1.0, 1.0), (0.0, 1.0), (1.0, 0.0)]:
            tv1 = TruthValue(s1, 0.9)
            tv2 = TruthValue(s2, 0.9)
            result = deduction(tv1, tv2)
            assert 0.0 <= result.strength <= 1.0
            assert 0.0 <= result.confidence <= 1.0

# === Induction Rule ===

class TestInduction:
    def test_basic_induction(self):
        tv_ab = TruthValue(0.8, 0.7)
        tv_ac = TruthValue(0.6, 0.5)
        result = induction(tv_ab, tv_ac, s_a=0.5)
        assert abs(result.strength - 0.96) < 1e-6
        assert 0 < result.confidence < 0.5

    def test_induction_zero_s_a(self):
        tv_ab = TruthValue(0.8, 0.7)
        tv_ac = TruthValue(0.6, 0.5)
        result = induction(tv_ab, tv_ac, s_a=0.0)
        assert result.strength == 0.5
        assert result.confidence == 0.0

    def test_induction_strength_clamped(self):
        tv_ab = TruthValue(0.9, 0.7)
        tv_ac = TruthValue(0.9, 0.5)
        result = induction(tv_ab, tv_ac, s_a=0.3)
        assert result.strength == 1.0

    def test_induction_confidence_bounded(self):
        tv_ab = TruthValue(0.8, 0.95)
        tv_ac = TruthValue(0.8, 0.95)
        result = induction(tv_ab, tv_ac, s_a=0.5)
        assert result.confidence <= 1.0


# === Abduction Rule ===

class TestAbduction:
    def test_basic_abduction(self):
        tv_ab = TruthValue(0.8, 0.7)
        tv_cb = TruthValue(0.6, 0.5)
        result = abduction(tv_ab, tv_cb, s_b=0.5)
        assert abs(result.strength - 0.96) < 1e-6
        assert 0 < result.confidence < 0.5

    def test_abduction_zero_s_b(self):
        tv_ab = TruthValue(0.8, 0.7)
        tv_cb = TruthValue(0.6, 0.5)
        result = abduction(tv_ab, tv_cb, s_b=0.0)
        assert result.strength == 0.5
        assert result.confidence == 0.0

    def test_abduction_strength_clamped(self):
        tv_ab = TruthValue(0.9, 0.7)
        tv_cb = TruthValue(0.9, 0.5)
        result = abduction(tv_ab, tv_cb, s_b=0.3)
        assert result.strength == 1.0

    def test_abduction_confidence_bounded(self):
        tv_ab = TruthValue(0.8, 0.95)
        tv_cb = TruthValue(0.8, 0.95)
        result = abduction(tv_ab, tv_cb, s_b=0.5)
        assert result.confidence <= 1.0


# === Confidence Hierarchy ===

class TestConfidenceHierarchy:
    def test_deduction_geq_induction_geq_abduction(self):
        tv1 = TruthValue(0.7, 0.7)
        tv2 = TruthValue(0.7, 0.7)
        ded = deduction(tv1, tv2)
        ind = induction(tv1, tv2, s_a=0.7)
        abd = abduction(tv1, tv2, s_b=0.7)
        assert abd.confidence <= ind.confidence <= ded.confidence

    def test_hierarchy_strong_inputs(self):
        tv1 = TruthValue(0.9, 0.9)
        tv2 = TruthValue(0.9, 0.9)
        ded = deduction(tv1, tv2)
        ind = induction(tv1, tv2, s_a=0.9)
        abd = abduction(tv1, tv2, s_b=0.9)
        assert abd.confidence <= ind.confidence <= ded.confidence

    def test_hierarchy_moderate_inputs(self):
        tv1 = TruthValue(0.6, 0.5)
        tv2 = TruthValue(0.6, 0.5)
        ded = deduction(tv1, tv2)
        ind = induction(tv1, tv2, s_a=0.6)
        abd = abduction(tv1, tv2, s_b=0.6)
        assert abd.confidence <= ind.confidence <= ded.confidence


# === Apply Rule Registry ===

class TestApplyRule:
    def test_apply_revision(self):
        tv1 = TruthValue(0.7, 0.6)
        tv2 = TruthValue(0.5, 0.4)
        result = apply_rule("revision", tv1, tv2)
        expected = revision(tv1, tv2)
        assert abs(result.strength - expected.strength) < 1e-9
        assert abs(result.confidence - expected.confidence) < 1e-9

    def test_apply_deduction(self):
        tv1 = TruthValue(0.8, 0.7)
        tv2 = TruthValue(0.6, 0.5)
        result = apply_rule("deduction", tv1, tv2)
        expected = deduction(tv1, tv2)
        assert abs(result.strength - expected.strength) < 1e-9

    def test_apply_induction(self):
        tv1 = TruthValue(0.8, 0.7)
        tv2 = TruthValue(0.6, 0.5)
        result = apply_rule("induction", tv1, tv2, s_a=0.5)
        expected = induction(tv1, tv2, s_a=0.5)
        assert abs(result.strength - expected.strength) < 1e-9

    def test_apply_abduction(self):
        tv1 = TruthValue(0.8, 0.7)
        tv2 = TruthValue(0.6, 0.5)
        result = apply_rule("abduction", tv1, tv2, s_b=0.5)
        expected = abduction(tv1, tv2, s_b=0.5)
        assert abs(result.strength - expected.strength) < 1e-9

    def test_apply_analogy(self):
        tv1 = TruthValue(0.8, 0.7)
        tv2 = TruthValue(0.6, 0.5)
        tv3 = TruthValue(0.7, 0.6)
        result = apply_rule("analogy", tv1, tv2, tv3)
        expected = analogy(tv1, tv2, tv3)
        assert abs(result.strength - expected.strength) < 1e-9

    def test_apply_unknown_rule_raises(self):
        with pytest.raises(ValueError, match="Unknown inference rule"):
            apply_rule("nonexistent_rule", TruthValue(0.5, 0.5))

    def test_all_rules_registered(self):
        expected = {"revision", "deduction", "induction", "abduction", "analogy"}
        assert set(INFERENCE_RULES.keys()) == expected


# === Edge Cases ===

class TestEdgeCases:
    def test_deduction_extreme_values(self):
        for s1, s2 in [(0.0, 0.0), (1.0, 1.0), (0.0, 1.0), (1.0, 0.0)]:
            tv1 = TruthValue(s1, 0.9)
            tv2 = TruthValue(s2, 0.9)
            result = deduction(tv1, tv2)
            assert 0.0 <= result.strength <= 1.0
            assert 0.0 <= result.confidence <= 1.0

    def test_revision_with_extreme_confidence(self):
        tv1 = TruthValue(0.5, 0.999)
        tv2 = TruthValue(0.5, 0.001)
        result = revision(tv1, tv2)
        assert abs(result.strength - 0.5) < 1e-3
        assert result.confidence > 0.5

    def test_all_rules_return_truth_value(self):
        tv = TruthValue(0.7, 0.6)
        for name, rule in INFERENCE_RULES.items():
            if name == "analogy":
                result = rule(tv, tv, tv)
            elif name == "induction":
                result = rule(tv, tv, s_a=0.5)
            elif name == "abduction":
                result = rule(tv, tv, s_b=0.5)
            else:
                result = rule(tv, tv)
            assert isinstance(result, TruthValue), f"{name} did not return TruthValue"
            assert 0.0 <= result.strength <= 1.0
            assert 0.0 <= result.confidence <= 1.0

    def test_induction_high_strength_low_s_a(self):
        tv = TruthValue(0.9, 0.9)
        result = induction(tv, tv, s_a=0.1)
        assert result.strength == 1.0

    def test_abduction_high_strength_low_s_b(self):
        tv = TruthValue(0.9, 0.9)
        result = abduction(tv, tv, s_b=0.1)
        assert result.strength == 1.0


# === Confidence Ordering ===

class TestConfidenceOrdering:
    def test_deduction_geq_induction_geq_abduction(self):
        tv1 = TruthValue(0.7, 0.7)
        tv2 = TruthValue(0.7, 0.7)
        ded = deduction(tv1, tv2)
        ind = induction(tv1, tv2, s_a=0.7)
        abd = abduction(tv1, tv2, s_b=0.7)
        assert ded.confidence >= ind.confidence
        assert ind.confidence >= abd.confidence

    def test_ordering_strong_inputs(self):
        tv1 = TruthValue(0.9, 0.9)
        tv2 = TruthValue(0.9, 0.9)
        ded = deduction(tv1, tv2)
        ind = induction(tv1, tv2, s_a=0.9)
        abd = abduction(tv1, tv2, s_b=0.9)
        assert ded.confidence >= ind.confidence
        assert ind.confidence >= abd.confidence
