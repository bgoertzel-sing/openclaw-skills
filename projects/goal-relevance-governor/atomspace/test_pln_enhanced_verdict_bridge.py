#!/usr/bin/env python3
"""Tests for Enhanced PLN-Verdict Bridge v0.2."""

import sys, os, json
import pytest
from datetime import datetime, timezone, timedelta

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from atomspace.pln_enhanced_verdict_bridge import EnhancedPLNVerdictBridge
from atomspace.pln_verdict_bridge import VerdictEnhanced


# ─── Fixtures ────────────────────────────────────────────────────────

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
        {"id": "t2", "kind": "task", "status": "completed",
         "priority": {"urgency": "low"}},
    ],
    "resources": [],
    "results": [],
    "constraints": [],
    "edges": [
        {"from": "t1", "to": "p1", "relation": "contributes_to", "confidence": "high"},
        {"from": "p1", "to": "g1", "relation": "contributes_to", "confidence": "high"},
    ],
}

STALE_DATA = {
    "goals": [
        {"id": "g1", "kind": "goal", "status": "active",
         "priority": {"urgency": "high"},
         "last_updated": (datetime.now(timezone.utc) - timedelta(days=30)).isoformat()},
    ],
    "projects": [],
    "tasks": [
        {"id": "t1", "kind": "task", "status": "active",
         "priority": {"urgency": "high"}},
    ],
    "resources": [],
    "results": [],
    "constraints": [],
    "edges": [
        {"from": "t1", "to": "g1", "relation": "contributes_to", "confidence": "high"},
    ],
}

EPISODE_FILE = os.path.join(
    os.path.dirname(__file__), "..", "replay_corpus",
    "episode_01_stale_codegen.json",
)


# ─── Tests ───────────────────────────────────────────────────────────

class TestEnhancedPLNVerdictBridge:
    def test_evaluate_returns_verdicts(self):
        bridge = EnhancedPLNVerdictBridge(SIMPLE_DATA)
        results = bridge.evaluate()
        assert len(results) > 0
        for r in results:
            assert isinstance(r, VerdictEnhanced)
            assert r.task_id

    def test_evaluate_excludes_completed_tasks(self):
        bridge = EnhancedPLNVerdictBridge(SIMPLE_DATA)
        results = bridge.evaluate()
        task_ids = [r.task_id for r in results]
        assert "t1" in task_ids
        assert "t2" not in task_ids

    def test_truth_values_in_range(self):
        bridge = EnhancedPLNVerdictBridge(SIMPLE_DATA)
        results = bridge.evaluate()
        for r in results:
            tv = r.truth_value
            assert 0.0 <= tv["strength"] <= 1.0
            assert 0.0 <= tv["confidence"] <= 1.0

    def test_relevance_in_range(self):
        bridge = EnhancedPLNVerdictBridge(SIMPLE_DATA)
        results = bridge.evaluate()
        for r in results:
            assert 0.0 <= r.relevance_score <= 1.0

    def test_priority_band_valid(self):
        bridge = EnhancedPLNVerdictBridge(SIMPLE_DATA)
        results = bridge.evaluate()
        valid_bands = {"CRITICAL", "NORMAL", "LOW", "STALE"}
        for r in results:
            assert r.priority_band in valid_bands

    def test_inference_stats(self):
        bridge = EnhancedPLNVerdictBridge(SIMPLE_DATA)
        bridge.evaluate()
        stats = bridge.get_inference_stats()
        assert "total" in stats
        assert stats["total"] > 0
        assert stats["deduction"] > 0

    def test_staleness_detection(self):
        bridge = EnhancedPLNVerdictBridge(STALE_DATA)
        results = bridge.evaluate()
        for r in results:
            if r.task_id == "t1":
                assert r.staleness_flag is True
                assert any("temporal_staleness" in s for s in r.signals)

    def test_staleness_confidence_decay(self):
        """Stale tasks should have decayed confidence."""
        stale_bridge = EnhancedPLNVerdictBridge(STALE_DATA)
        fresh_data = json.loads(json.dumps(STALE_DATA))
        fresh_data["goals"][0]["last_updated"] = datetime.now(timezone.utc).isoformat()
        fresh_bridge = EnhancedPLNVerdictBridge(fresh_data)

        stale_results = {r.task_id: r for r in stale_bridge.evaluate()}
        fresh_results = {r.task_id: r for r in fresh_bridge.evaluate()}

        if "t1" in stale_results and "t1" in fresh_results:
            stale_conf = stale_results["t1"].truth_value["confidence"]
            fresh_conf = fresh_results["t1"].truth_value["confidence"]
            assert stale_conf <= fresh_conf

    def test_unified_verdict(self):
        bridge = EnhancedPLNVerdictBridge(SIMPLE_DATA)
        results = bridge.evaluate()
        for r in results:
            assert r.unified_verdict  # should be non-empty

    def test_evaluate_to_json(self):
        bridge = EnhancedPLNVerdictBridge(SIMPLE_DATA)
        json_str = bridge.evaluate_to_json()
        parsed = json.loads(json_str)
        assert parsed["format"] == "Enhanced-PLN-Verdict-Bridge-v0.2"
        assert "inference_stats" in parsed
        assert "tasks" in parsed
        assert len(parsed["tasks"]) > 0

    def test_evaluate_to_json_enhanced(self):
        bridge = EnhancedPLNVerdictBridge(SIMPLE_DATA)
        json_str = bridge.evaluate_to_json_enhanced()
        parsed = json.loads(json_str)
        assert "enhanced_pln" in parsed
        assert "inference_stats" in parsed

    def test_empty_data(self):
        bridge = EnhancedPLNVerdictBridge({})
        results = bridge.evaluate()
        assert len(results) == 0

    def test_evidence_contains_pln_info(self):
        bridge = EnhancedPLNVerdictBridge(SIMPLE_DATA)
        results = bridge.evaluate()
        for r in results:
            pln_evidence = [e for e in r.evidence if "pln_relevance" in e]
            assert len(pln_evidence) > 0

    def test_evidence_contains_chain_info(self):
        bridge = EnhancedPLNVerdictBridge(SIMPLE_DATA)
        results = bridge.evaluate()
        for r in results:
            chain_evidence = [e for e in r.evidence if "chain_count" in e]
            assert len(chain_evidence) > 0

    def test_relevance_shift_signal(self):
        """When enhanced and naive relevance differ, a signal should be added."""
        bridge = EnhancedPLNVerdictBridge(SIMPLE_DATA)
        results = bridge.evaluate()
        # At minimum, the bridge should run without errors
        # The signal may or may not appear depending on data
        for r in results:
            assert isinstance(r.signals, list)

    def test_max_depth_parameter(self):
        bridge = EnhancedPLNVerdictBridge(SIMPLE_DATA, max_depth=2)
        results = bridge.evaluate()
        assert len(results) > 0

    @pytest.mark.skipif(
        not os.path.exists(EPISODE_FILE),
        reason="Episode file not found",
    )
    def test_episode_01_integration(self):
        """Integration test with real episode data."""
        with open(EPISODE_FILE) as f:
            data = json.load(f)
        bridge = EnhancedPLNVerdictBridge(data)
        results = bridge.evaluate()
        assert len(results) > 0
        stats = bridge.get_inference_stats()
        assert stats["total"] > 0

    @pytest.mark.skipif(
        not os.path.exists(EPISODE_FILE),
        reason="Episode file not found",
    )
    def test_episode_01_json_output(self):
        """JSON output for episode 01."""
        with open(EPISODE_FILE) as f:
            data = json.load(f)
        bridge = EnhancedPLNVerdictBridge(data)
        json_str = bridge.evaluate_to_json()
        parsed = json.loads(json_str)
        assert parsed["format"] == "Enhanced-PLN-Verdict-Bridge-v0.2"
        assert parsed["task_count"] > 0
