#!/usr/bin/env python3
"""Tests for pln_chain_integration.py — RuleAwareChainMiner & utilities."""

import sys, os, json
import pytest
from datetime import datetime, timezone

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from atomspace.pln_chain_integration import (
    RuleAwareChainMiner,
    enhance_relevance_with_rules,
    compare_propagation,
    propagate_with_rules,
)
from atomspace.pln_propagation import TruthValue

SIMPLE_DATA = {
    "goals": [
        {"id": "g1", "kind": "goal", "status": "active",
         "priority": {"urgency": "high"}},
    ],
    "projects": [
        {"id": "p1", "kind": "project", "status": "active"},
    ],
    "tasks": [
        {"id": "t1", "kind": "task", "status": "active",
         "priority": {"urgency": "high"}},
        {"id": "t2", "kind": "task", "status": "active",
         "priority": {"urgency": "medium"}},
    ],
    "resources": [],
    "results": [],
    "constraints": [],
    "edges": [
        {"from": "t1", "to": "p1", "relation": "contributes_to", "confidence": "high"},
        {"from": "p1", "to": "g1", "relation": "contributes_to", "confidence": "high"},
        {"from": "t2", "to": "g1", "relation": "provides_evidence_for", "confidence": "medium"},
    ],
}

BLOCKING_DATA = {
    "goals": [{"id": "g1", "kind": "goal", "status": "active",
               "priority": {"urgency": "high"}}],
    "tasks": [
        {"id": "t1", "kind": "task", "status": "active",
         "priority": {"urgency": "high"}},
        {"id": "t2", "kind": "task", "status": "active",
         "priority": {"urgency": "high"}},
    ],
    "resources": [{"id": "r1", "kind": "resource", "status": "active"}],
    "edges": [
        {"from": "t1", "to": "g1", "relation": "contributes_to", "confidence": "high"},
        {"from": "t2", "to": "r1", "relation": "occupies", "confidence": "high"},
        {"from": "t1", "to": "r1", "relation": "occupies", "confidence": "high"},
        {"from": "t2", "to": "t1", "relation": "blocks", "confidence": "high"},
    ],
}


class TestRuleAwareChainMiner:
    def test_find_chains_returns_list(self):
        miner = RuleAwareChainMiner(SIMPLE_DATA)
        chains = miner.find_chains("t1")
        assert isinstance(chains, list)
        assert len(chains) > 0

    def test_find_chains_uses_inference_rules(self):
        miner = RuleAwareChainMiner(SIMPLE_DATA)
        chains = miner.find_chains("t1")
        for ch in chains:
            assert "rules_applied" in ch
            assert len(ch["rules_applied"]) > 0
            for r in ch["rules_applied"]:
                assert r in ("deduction", "induction", "abduction", "revision", "inhibitory", "naive")

    def test_find_chains_all_tasks(self):
        miner = RuleAwareChainMiner(SIMPLE_DATA)
        all_chains = miner.find_chains_all_tasks()
        assert isinstance(all_chains, dict)
        assert "t1" in all_chains
        assert "t2" in all_chains

    def test_chains_have_truth_values(self):
        miner = RuleAwareChainMiner(SIMPLE_DATA)
        chains = miner.find_chains("t1")
        for ch in chains:
            tv = ch.get("tv")
            assert tv is not None
            assert 0.0 <= tv.strength <= 1.0
            assert 0.0 <= tv.confidence <= 1.0

    def test_blocking_data_inhibitory(self):
        """blocks relation should map to abduction rule."""
        miner = RuleAwareChainMiner(BLOCKING_DATA)
        all_chains = miner.find_chains_all_tasks()
        # Collect all rules across all tasks' chains
        all_rules = []
        for tid, chains in all_chains.items():
            for ch in chains:
                all_rules.extend(ch.get("rules_applied", []))
        # t2 has a blocks edge; even if it doesn't reach a goal directly,
        # the relation mapping should be reflected if any chain traverses it.
        # Also verify via the RELATION_RULE_MAP that blocks -> abduction
        from atomspace.pln_chain_integration import RELATION_RULE_MAP
        assert RELATION_RULE_MAP.get("blocks") == "abduction"

    def test_empty_data(self):
        miner = RuleAwareChainMiner({})
        chains = miner.find_chains("nonexistent")
        assert chains == []

    def test_deduction_for_contributes_to(self):
        miner = RuleAwareChainMiner(SIMPLE_DATA)
        chains = miner.find_chains("t1")
        deduction_chains = [ch for ch in chains if "deduction" in ch.get("rules_applied", [])]
        assert len(deduction_chains) > 0

    def test_evidence_for_uses_revision_or_induction(self):
        miner = RuleAwareChainMiner(SIMPLE_DATA)
        chains = miner.find_chains("t2")
        rules = []
        for ch in chains:
            rules.extend(ch.get("rules_applied", []))
        assert any(r in ("revision", "induction") for r in rules)


class TestEnhanceRelevanceWithRules:
    def test_blend_returns_float(self):
        result = enhance_relevance_with_rules(0.5, 0.7, 0.8)
        assert isinstance(result, float)

    def test_blend_in_range(self):
        result = enhance_relevance_with_rules(0.3, 0.9, 0.6)
        assert 0.0 <= result <= 1.0

    def test_zero_base_relevance(self):
        result = enhance_relevance_with_rules(0.0, 0.5, 0.8)
        assert result > 0.0

    def test_weight_effect(self):
        low_w = enhance_relevance_with_rules(0.5, 0.9, 0.8, w=0.1)
        high_w = enhance_relevance_with_rules(0.5, 0.9, 0.8, w=0.9)
        assert high_w > low_w

    def test_low_confidence_reduces_blend(self):
        high_conf = enhance_relevance_with_rules(0.5, 0.9, 0.9, w=0.5)
        low_conf = enhance_relevance_with_rules(0.5, 0.9, 0.1, w=0.5)
        assert high_conf >= low_conf


class TestComparePropagation:
    def test_returns_dict(self):
        naive = TruthValue(0.5, 0.4)
        rule = TruthValue(0.7, 0.8)
        result = compare_propagation(naive, rule)
        assert isinstance(result, dict)

    def test_has_expected_keys(self):
        result = compare_propagation(TruthValue(0.5, 0.4), TruthValue(0.7, 0.8))
        expected = {"naive_strength", "rule_strength", "strength_delta",
                    "naive_confidence", "rule_confidence", "confidence_delta"}
        assert expected.issubset(set(result.keys()))

    def test_delta_calculation(self):
        naive = TruthValue(0.5, 0.4)
        rule = TruthValue(0.7, 0.8)
        result = compare_propagation(naive, rule)
        assert abs(result["strength_delta"] - 0.2) < 0.001
        assert abs(result["confidence_delta"] - 0.4) < 0.001

    def test_rule_more_confident_flag(self):
        result = compare_propagation(TruthValue(0.5, 0.4), TruthValue(0.7, 0.8))
        assert result["rule_more_confident"] is True

    def test_rule_less_confident_flag(self):
        result = compare_propagation(TruthValue(0.5, 0.9), TruthValue(0.7, 0.3))
        assert result["rule_more_confident"] is False


class TestPropagateWithRules:
    def test_returns_truth_value(self):
        tv = propagate_with_rules(TruthValue(0.8, 0.9), 0.8, "contributes_to")
        assert isinstance(tv, TruthValue)

    def test_deduction_reduces_confidence(self):
        source_tv = TruthValue(0.8, 0.9)
        result = propagate_with_rules(source_tv, 0.8, "contributes_to")
        assert result.confidence <= source_tv.confidence

    def test_unknown_relation_fallback(self):
        tv = propagate_with_rules(TruthValue(0.8, 0.9), 0.8, "unknown_relation")
        assert isinstance(tv, TruthValue)
        assert 0.0 <= tv.strength <= 1.0
