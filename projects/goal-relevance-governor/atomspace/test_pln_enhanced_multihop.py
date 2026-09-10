#!/usr/bin/env python3
"""Tests for PLN Inference-Enhanced Multi-Hop Reasoning v0.1."""

import sys, os, json
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from atomspace.pln_propagation import TruthValue
from atomspace.pln_multihop import ChainMiner, ReasoningChain
from atomspace.pln_enhanced_multihop import (
    InferenceEnhancedChainMiner,
    InferenceEnhancedMultiHopEvaluator,
)
from atomspace.pln_inference_propagation import InferenceRuleStats


# ─── Test fixture data ───────────────────────────────────────────────

FIXTURE_DATA = {
    "goals": [
        {"id": "g1", "kind": "goal", "status": "active", "priority": {"urgency": "high"}},
        {"id": "g2", "kind": "goal", "status": "active", "priority": {"urgency": "medium"}},
    ],
    "projects": [
        {"id": "p1", "kind": "project", "status": "active"},
    ],
    "tasks": [
        {"id": "t1", "kind": "task", "status": "active", "priority": {"urgency": "high"}},
        {"id": "t2", "kind": "task", "status": "active", "priority": {"urgency": "medium"}},
        {"id": "t3", "kind": "task", "status": "completed", "priority": {"urgency": "low"}},
    ],
    "resources": [
        {"id": "r1", "kind": "resource", "exclusive": True},
    ],
    "results": [
        {"id": "res1", "kind": "result", "status": "completed"},
    ],
    "constraints": [
        {"id": "c1", "kind": "constraint"},
    ],
    "edges": [
        {"from": "t1", "to": "g1", "relation": "contributes_to", "confidence": "high"},
        {"from": "t2", "to": "g2", "relation": "contributes_to", "confidence": "medium"},
        {"from": "t1", "to": "r1", "relation": "occupies", "confidence": "high"},
        {"from": "t2", "to": "r1", "relation": "occupies", "confidence": "high"},
        {"from": "t1", "to": "p1", "relation": "part_of", "confidence": "high"},
        {"from": "res1", "to": "g1", "relation": "provides_evidence_for", "confidence": "high"},
    ],
}


# ─── InferenceEnhancedChainMiner ─────────────────────────────────────

class TestInferenceEnhancedChainMiner:
    def test_finds_chains(self):
        miner = InferenceEnhancedChainMiner(FIXTURE_DATA)
        chains = miner.find_chains("t1", max_depth=4)
        assert len(chains) > 0
        targets = [c.target for c in chains]
        assert "g1" in targets

    def test_chain_truth_values_are_truth_value(self):
        miner = InferenceEnhancedChainMiner(FIXTURE_DATA)
        chains = miner.find_chains("t1", max_depth=4)
        for c in chains:
            assert isinstance(c.tv, TruthValue)
            assert 0.0 <= c.tv.strength <= 1.0
            assert 0.0 <= c.tv.confidence <= 1.0

    def test_differs_from_naive_miner(self):
        """Enhanced miner should produce different TV than naive ChainMiner."""
        enhanced = InferenceEnhancedChainMiner(FIXTURE_DATA)
        naive = ChainMiner(FIXTURE_DATA)

        enhanced_chains = enhanced.find_chains("t1", max_depth=4)
        naive_chains = naive.find_chains("t1", max_depth=4)

        # Both should find the same number of chains (same graph traversal)
        assert len(enhanced_chains) == len(naive_chains)

        # But truth values should differ (deduction vs naive multiplication)
        for ec, nc in zip(enhanced_chains, naive_chains):
            if ec.target == nc.target and ec.target == "g1":
                # Deduction strength = s1*s2 + (1-s1)*(1-s2) != s1*s2
                assert abs(ec.tv.strength - nc.tv.strength) > 0.001

    def test_stats_tracked(self):
        miner = InferenceEnhancedChainMiner(FIXTURE_DATA)
        miner.find_chains("t1", max_depth=4)
        stats = miner.get_stats()
        assert stats["total"] > 0
        assert stats["deduction"] > 0  # contributes_to and part_of

    def test_find_chains_aggregated(self):
        miner = InferenceEnhancedChainMiner(FIXTURE_DATA)
        chains, agg_tv = miner.find_chains_aggregated("t1", max_depth=4)
        assert len(chains) > 0
        assert isinstance(agg_tv, TruthValue)
        assert 0.0 <= agg_tv.strength <= 1.0
        assert 0.0 <= agg_tv.confidence <= 1.0

    def test_find_chains_all_tasks(self):
        miner = InferenceEnhancedChainMiner(FIXTURE_DATA)
        results = miner.find_chains_all_tasks(max_depth=4)
        # t1 and t2 are active, t3 is completed
        assert "t1" in results
        assert "t2" in results
        assert "t3" not in results

    def test_completed_task_excluded(self):
        miner = InferenceEnhancedChainMiner(FIXTURE_DATA)
        results = miner.find_chains_all_tasks(max_depth=4)
        assert "t3" not in results

    def test_chain_path_correct(self):
        miner = InferenceEnhancedChainMiner(FIXTURE_DATA)
        chains = miner.find_chains("t1", max_depth=4)
        for c in chains:
            assert c.path[0] == "t1"
            assert c.source == "t1"

    def test_max_depth_respected(self):
        miner = InferenceEnhancedChainMiner(FIXTURE_DATA)
        chains = miner.find_chains("t1", max_depth=1)
        for c in chains:
            assert c.depth <= 1

    def test_empty_data(self):
        miner = InferenceEnhancedChainMiner({})
        chains = miner.find_chains("nonexistent", max_depth=4)
        assert len(chains) == 0

    def test_no_cycles(self):
        """Chain paths should never contain duplicate nodes."""
        miner = InferenceEnhancedChainMiner(FIXTURE_DATA)
        chains = miner.find_chains("t1", max_depth=4)
        for c in chains:
            assert len(c.path) == len(set(c.path)), "Cycle detected in path"


# ─── InferenceEnhancedMultiHopEvaluator ──────────────────────────────

class TestInferenceEnhancedMultiHopEvaluator:
    def test_evaluate(self):
        evaluator = InferenceEnhancedMultiHopEvaluator(FIXTURE_DATA, max_depth=4)
        results = evaluator.evaluate()
        assert "t1" in results
        assert "t2" in results
        assert "t3" not in results

    def test_evaluate_enhanced(self):
        evaluator = InferenceEnhancedMultiHopEvaluator(FIXTURE_DATA, max_depth=4)
        results = evaluator.evaluate_enhanced()
        assert "t1" in results
        r = results["t1"]
        assert "chain_count" in r
        assert "aggregated_tv" in r
        assert "relevance_score" in r
        assert "goal_coverage" in r
        assert r["chain_count"] > 0

    def test_inference_stats(self):
        evaluator = InferenceEnhancedMultiHopEvaluator(FIXTURE_DATA, max_depth=4)
        evaluator.evaluate()
        stats = evaluator.get_inference_stats()
        assert stats["total"] > 0
        assert stats["deduction"] > 0

    def test_evaluate_to_json(self):
        evaluator = InferenceEnhancedMultiHopEvaluator(FIXTURE_DATA, max_depth=4)
        json_str = evaluator.evaluate_to_json()
        parsed = json.loads(json_str)
        assert "tasks" in parsed
        assert "inference_stats" in parsed
        assert "t1" in parsed["tasks"]

    def test_empty_data(self):
        evaluator = InferenceEnhancedMultiHopEvaluator({}, max_depth=4)
        results = evaluator.evaluate()
        assert len(results) == 0

    def test_relevance_score_in_range(self):
        evaluator = InferenceEnhancedMultiHopEvaluator(FIXTURE_DATA, max_depth=4)
        results = evaluator.evaluate_enhanced()
        for tid, r in results.items():
            assert 0.0 <= r["relevance_score"] <= 1.0

    def test_aggregated_tv_in_range(self):
        evaluator = InferenceEnhancedMultiHopEvaluator(FIXTURE_DATA, max_depth=4)
        results = evaluator.evaluate_enhanced()
        for tid, r in results.items():
            tv = r["aggregated_tv"]
            assert 0.0 <= tv["strength"] <= 1.0
            assert 0.0 <= tv["confidence"] <= 1.0
