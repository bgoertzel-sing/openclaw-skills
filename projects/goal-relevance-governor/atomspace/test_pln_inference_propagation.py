#!/usr/bin/env python3
"""Tests for PLN Inference-Enhanced Chain Propagation v0.1."""

import sys, os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from atomspace.pln_propagation import TruthValue
from atomspace.pln_inference_rules import deduction, revision
from atomspace.pln_inference_propagation import (
    select_inference_rule,
    propagate_edge,
    aggregate_chains_by_revision,
    InferenceRuleStats,
    DEDUCTIVE_RELATIONS,
    EVIDENTIAL_RELATIONS,
    ABDUCTIVE_RELATIONS,
    INHIBITORY_RELATIONS,
)


# === Rule Selection ===

class TestSelectInferenceRule:
    def test_deductive_relations(self):
        for r in DEDUCTIVE_RELATIONS:
            assert select_inference_rule(r) == "deduction"

    def test_evidential_relations(self):
        for r in EVIDENTIAL_RELATIONS:
            assert select_inference_rule(r) == "revision"

    def test_abductive_relations(self):
        for r in ABDUCTIVE_RELATIONS:
            assert select_inference_rule(r) == "abduction"

    def test_inhibitory_relations(self):
        for r in INHIBITORY_RELATIONS:
            assert select_inference_rule(r) == "inhibitory"

    def test_unknown_relation_naive(self):
        assert select_inference_rule("unknown_relation") == "naive"
        assert select_inference_rule("") == "naive"

    def test_all_core_relations_mapped(self):
        """All 6 core graph relations should be mapped, not naive."""
        core = {"contributes_to", "part_of", "provides_evidence_for",
                "supersedes", "blocks", "occupies"}
        for r in core:
            rule = select_inference_rule(r)
            assert rule != "naive", f"Relation {r} should not be naive"


# === Edge Propagation ===

class TestPropagateEdge:
    def test_deductive_propagation(self):
        tv = TruthValue(0.8, 0.7)
        edge = {"relation": "contributes_to", "confidence": 0.9}
        result = propagate_edge(tv, edge, edge_conf=0.9)
        expected = deduction(tv, TruthValue(0.9, 0.9))
        assert abs(result.strength - expected.strength) < 1e-9
        assert abs(result.confidence - expected.confidence) < 1e-9

    def test_evidential_propagation(self):
        tv = TruthValue(0.8, 0.7)
        edge = {"relation": "provides_evidence_for", "confidence": 0.9}
        result = propagate_edge(tv, edge, edge_conf=0.9)
        expected = revision(tv, TruthValue(0.9, 0.9))
        assert abs(result.strength - expected.strength) < 1e-9

    def test_inhibitory_propagation(self):
        tv = TruthValue(0.8, 0.7)
        edge = {"relation": "blocks", "confidence": 0.9}
        result = propagate_edge(tv, edge, edge_conf=0.9)
        # Inhibitory: negate then deduct
        negated = tv.negate()
        expected = deduction(negated, TruthValue(0.9, 0.9))
        assert abs(result.strength - expected.strength) < 1e-9

    def test_abductive_propagation(self):
        tv = TruthValue(0.8, 0.7)
        edge = {"relation": "supersedes", "confidence": 0.9}
        result = propagate_edge(tv, edge, edge_conf=0.9)
        negated = tv.negate()
        expected = deduction(negated, TruthValue(0.9, 0.9))
        assert abs(result.strength - expected.strength) < 1e-9

    def test_naive_fallback(self):
        tv = TruthValue(0.8, 0.7)
        edge = {"relation": "unknown", "confidence": 0.9}
        result = propagate_edge(tv, edge, edge_conf=0.9)
        assert abs(result.strength - 0.8 * 0.9) < 1e-9
        assert abs(result.confidence - 0.7 * 0.9) < 1e-9

    def test_auto_compute_edge_conf(self):
        """When edge_conf is not passed, _edge_confidence is auto-computed."""
        tv = TruthValue(0.8, 0.7)
        # Use string confidence that CONFIDENCE_MAP will resolve
        edge = {"relation": "contributes_to", "confidence": "high"}
        result_auto = propagate_edge(tv, edge)
        # "high" maps to 0.9 in CONFIDENCE_MAP
        result_explicit = propagate_edge(tv, edge, edge_conf=0.9)
        assert abs(result_auto.strength - result_explicit.strength) < 1e-9

    def test_deductive_vs_naive_differs(self):
        """Deduction should produce different results than naive multiplication."""
        tv = TruthValue(0.8, 0.7)
        edge = {"relation": "contributes_to", "confidence": 0.9}
        deductive = propagate_edge(tv, edge, edge_conf=0.9)
        naive = TruthValue(0.8 * 0.9, 0.7 * 0.9)
        # Deduction strength = s1*s2 + (1-s1)*(1-s2) which differs from s1*s2
        assert abs(deductive.strength - naive.strength) > 0.01

    def test_inhibitory_reduces_strength(self):
        """Blocking should reduce strength (negate then propagate)."""
        tv = TruthValue(0.9, 0.8)
        edge = {"relation": "blocks", "confidence": 0.9}
        result = propagate_edge(tv, edge, edge_conf=0.9)
        # Negated strength = 0.1, then deduction with 0.9
        assert result.strength < 0.5

    def test_zero_confidence_edge(self):
        tv = TruthValue(0.8, 0.7)
        edge = {"relation": "contributes_to", "confidence": 0.0}
        result = propagate_edge(tv, edge, edge_conf=0.0)
        assert result.confidence < 0.01

    def test_extreme_values(self):
        for s, c in [(0.0, 0.0), (1.0, 1.0), (0.5, 0.5)]:
            tv = TruthValue(s, c)
            for rel in ["contributes_to", "provides_evidence_for",
                        "blocks", "supersedes", "unknown"]:
                edge = {"relation": rel, "confidence": c}
                result = propagate_edge(tv, edge, edge_conf=c)
                assert 0.0 <= result.strength <= 1.0
                assert 0.0 <= result.confidence <= 1.0


# === Chain Aggregation by Revision ===

class TestAggregateChainsByRevision:
    def test_empty_chains(self):
        result = aggregate_chains_by_revision([])
        assert result.strength == 0.0
        assert result.confidence == 0.0

    def test_single_chain(self):
        class FakeChain:
            def __init__(self, tv):
                self.tv = tv
        tv = TruthValue(0.7, 0.6)
        result = aggregate_chains_by_revision([FakeChain(tv)])
        assert abs(result.strength - tv.strength) < 1e-9
        assert abs(result.confidence - tv.confidence) < 1e-9

    def test_multiple_chains_increase_confidence(self):
        class FakeChain:
            def __init__(self, tv):
                self.tv = tv
        chains = [FakeChain(TruthValue(0.7, 0.4)) for _ in range(5)]
        result = aggregate_chains_by_revision(chains)
        assert result.confidence > 0.4

    def test_revision_vs_disjunction(self):
        """Revision should produce different (usually lower) strength
        than disjunction when chains have varying strengths."""
        class FakeChain:
            def __init__(self, tv):
                self.tv = tv
        chains = [
            FakeChain(TruthValue(0.3, 0.5)),
            FakeChain(TruthValue(0.9, 0.5)),
        ]
        rev_result = aggregate_chains_by_revision(chains)
        # Disjunction would give max(0.3, 0.9) = 0.9
        # Revision gives weighted average, which should be < 0.9
        assert rev_result.strength < 0.9
        assert rev_result.strength > 0.3

    def test_symmetric(self):
        class FakeChain:
            def __init__(self, tv):
                self.tv = tv
        chains1 = [FakeChain(TruthValue(0.3, 0.5)), FakeChain(TruthValue(0.7, 0.5))]
        chains2 = [FakeChain(TruthValue(0.7, 0.5)), FakeChain(TruthValue(0.3, 0.5))]
        r1 = aggregate_chains_by_revision(chains1)
        r2 = aggregate_chains_by_revision(chains2)
        assert abs(r1.strength - r2.strength) < 1e-6


# === InferenceRuleStats ===

class TestInferenceRuleStats:
    def test_empty_stats(self):
        stats = InferenceRuleStats()
        assert stats.total == 0
        assert stats.deduction_count == 0

    def test_record_deduction(self):
        stats = InferenceRuleStats()
        stats.record("contributes_to")
        stats.record("part_of")
        assert stats.deduction_count == 2
        assert stats.total == 2

    def test_record_all_types(self):
        stats = InferenceRuleStats()
        stats.record("contributes_to")  # deduction
        stats.record("provides_evidence_for")  # revision
        stats.record("supersedes")  # abduction
        stats.record("blocks")  # inhibitory
        stats.record("unknown")  # naive
        assert stats.deduction_count == 1
        assert stats.revision_count == 1
        assert stats.abduction_count == 1
        assert stats.inhibitory_count == 1
        assert stats.naive_count == 1
        assert stats.total == 5

    def test_to_dict(self):
        stats = InferenceRuleStats()
        stats.record("contributes_to")
        stats.record("blocks")
        d = stats.to_dict()
        assert d["deduction"] == 1
        assert d["inhibitory"] == 1
        assert d["total"] == 2
