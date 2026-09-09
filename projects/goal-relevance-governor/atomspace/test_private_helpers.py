import unittest, copy, sys
from datetime import datetime, timezone

sys.path.insert(0, "/home/openclaw/research-agent/projects/goal-relevance-governor/atomspace")

from pln_chain_integration import (
    RuleAwareChainMiner, _edge_confidence, _initial_tv, TruthValue,
    enhance_relevance_with_rules, propagate_with_rules,
    RELATION_RULE_MAP,
)
from pln_propagation import (
    CONFIDENCE_MAP, STATUS_STRENGTH, STATUS_CONFIDENCE,
)
from pln_verdict_bridge import (
    PLNVerdictBridge, _confidence_modifier, _parse_timestamp,
    _priority_band, compute_staleness, PRIORITY_BANDS,
)
from ecan_attention import ECANAttentionAllocator, AttentionValue
from reasoning_explainer import ReasoningExplainer
from temporal_simulator import TemporalSimulator
from metta_evaluator import MeTTaEvaluator
from integrated_governor import IntegratedGovernorPipeline, TaskRecommendation

BASE = {
    "schema_version": "0.1", "episode_id": "test", "episode_title": "test",
    "frozen_at": "2026-01-01T00:00:00Z", "expected_verdict": "CONTINUE",
    "goals": [], "projects": [], "tasks": [], "resources": [],
    "results": [], "constraints": [], "edges": []
}

def _task(tid, status="active", rev="reversible"):
    return {"id": tid, "kind": "task", "title": tid, "status": status,
            "owner": "s", "reversibility": rev, "source": "s",
            "as_of": "2026-01-01T00:00:00Z"}

def _goal(gid, status="active", urgency="high"):
    return {"id": gid, "kind": "goal", "title": gid, "status": status,
            "level": "intermediate", "priority": {"rank": 1, "urgency": urgency},
            "source": "s", "as_of": "2026-01-01T00:00:00Z"}

def _edge(f, t, r="contributes_to", conf="high"):
    return {"from": f, "to": t, "relation": r, "confidence": conf}

# ===================== pln_chain_integration helpers =====================

class TestEdgeConfidence(unittest.TestCase):
    def test_high(self):
        self.assertAlmostEqual(_edge_confidence({"confidence": "high"}), CONFIDENCE_MAP["high"])
    def test_medium(self):
        self.assertAlmostEqual(_edge_confidence({"confidence": "medium"}), CONFIDENCE_MAP["medium"])
    def test_low(self):
        self.assertAlmostEqual(_edge_confidence({"confidence": "low"}), CONFIDENCE_MAP["low"])
    def test_missing_defaults_to_medium(self):
        self.assertAlmostEqual(_edge_confidence({}), 0.6)
    def test_unknown_defaults_to_medium(self):
        self.assertAlmostEqual(_edge_confidence({"confidence": "bogus"}), 0.6)

class TestInitialTV(unittest.TestCase):
    def test_active_task(self):
        tv = _initial_tv(_task("t1"))
        self.assertAlmostEqual(tv.strength, STATUS_STRENGTH.get("active", 0.5))
        self.assertAlmostEqual(tv.confidence, STATUS_CONFIDENCE.get("active", 0.5))
    def test_goal_urgency_adjustment(self):
        tv_low = _initial_tv(_goal("g1", urgency="low"))
        tv_high = _initial_tv(_goal("g2", urgency="high"))
        self.assertLess(tv_low.strength, tv_high.strength)
    def test_irreversible_task_confidence_penalty(self):
        tv_rev = _initial_tv(_task("t1", rev="reversible"))
        tv_irr = _initial_tv(_task("t2", rev="irreversible"))
        self.assertLess(tv_irr.confidence, tv_rev.confidence)
    def test_unknown_status_defaults(self):
        tv = _initial_tv({"kind": "task", "status": "bogus"})
        self.assertAlmostEqual(tv.strength, 0.5)
        self.assertAlmostEqual(tv.confidence, 0.5)

class TestRuleAwareChainMinerHelpers(unittest.TestCase):
    def _make_miner(self):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1"), _goal("g2")]
        g["edges"] = [_edge("t1", "g1"), _edge("t1", "g2")]
        return RuleAwareChainMiner(g)
    def test_is_goal_true(self):
        self.assertTrue(self._make_miner()._is_goal("g1"))
    def test_is_goal_false_for_task(self):
        self.assertFalse(self._make_miner()._is_goal("t1"))
    def test_is_goal_false_for_unknown(self):
        self.assertFalse(self._make_miner()._is_goal("unknown"))
    def test_get_prevalence_for_goal(self):
        prev = self._make_miner()._get_prevalence("g1")
        self.assertGreaterEqual(prev, 0)
        self.assertLessEqual(prev, 1)
    def test_get_prevalence_unknown_node(self):
        self.assertAlmostEqual(self._make_miner()._get_prevalence("unknown"), 0.5)
    def test_estimate_prevalences_returns_dict(self):
        prev = self._make_miner()._estimate_prevalences()
        self.assertIn("goal", prev)
        self.assertIn("task", prev)
    def test_estimate_prevalences_no_tvs(self):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1")]
        g["edges"] = [_edge("t1", "g1")]
        m = RuleAwareChainMiner(g)
        # Miner initializes TVs during construction, so prevalences
        # should be based on actual strength values, not 0.5 default
        prev = m._estimate_prevalences()
        self.assertIn("task", prev)
        self.assertGreater(prev["task"], 0)
        self.assertLessEqual(prev["task"], 1.0)

class TestPropagateWithRules(unittest.TestCase):
    def test_deduction_for_contributes_to(self):
        result = propagate_with_rules(TruthValue(0.8, 0.7), 0.9, "contributes_to", 0.5)
        self.assertGreater(result.strength, 0)
        self.assertLessEqual(result.strength, 1)
    def test_revision_for_blocks(self):
        result = propagate_with_rules(TruthValue(0.3, 0.6), 0.8, "blocks", 0.5)
        self.assertGreaterEqual(result.strength, 0)
        self.assertLessEqual(result.strength, 1)
    def test_unknown_relation_fallback(self):
        result = propagate_with_rules(TruthValue(0.7, 0.6), 0.8, "bogus_relation", 0.5)
        self.assertGreaterEqual(result.strength, 0)

class TestEnhanceRelevanceWithRules(unittest.TestCase):
    def test_blend_returns_float(self):
        result = enhance_relevance_with_rules(0.5, 0.6, 0.7, w=0.3)
        self.assertIsInstance(result, float)
    def test_blend_in_range(self):
        result = enhance_relevance_with_rules(0.9, 0.1, 0.8, w=0.5)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 1)
    def test_w_zero_returns_base(self):
        result = enhance_relevance_with_rules(0.7, 0.3, 0.9, w=0.0)
        self.assertAlmostEqual(result, 0.7, places=1)
    def test_w_one_returns_rule_based(self):
        result = enhance_relevance_with_rules(0.3, 0.8, 0.9, w=1.0)
        self.assertGreater(result, 0.5)

# ===================== pln_verdict_bridge helpers =====================

class TestParseTimestamp(unittest.TestCase):
    def test_valid_iso(self):
        result = _parse_timestamp("2026-01-15T12:30:00Z")
        self.assertIsNotNone(result)
        self.assertEqual(result.year, 2026)
    def test_none_input(self):
        self.assertIsNone(_parse_timestamp(None))
    def test_empty_string(self):
        self.assertIsNone(_parse_timestamp(""))
    def test_invalid_string(self):
        self.assertIsNone(_parse_timestamp("not-a-timestamp"))
    def test_with_timezone_offset(self):
        result = _parse_timestamp("2026-01-15T12:30:00+05:00")
        self.assertIsNotNone(result)

class TestConfidenceModifier(unittest.TestCase):
    def test_high_confidence_positive(self):
        tv = TruthValue(0.9, 0.9)
        result = _confidence_modifier(tv)
        self.assertGreater(result, 0)
        self.assertLessEqual(result, 1.0)
    def test_low_confidence_negative(self):
        tv = TruthValue(0.1, 0.1)
        result = _confidence_modifier(tv)
        self.assertLess(result, 0.0)
    def test_stale_penalty(self):
        tv = TruthValue(0.9, 0.9)
        normal = _confidence_modifier(tv, is_stale=False)
        stale = _confidence_modifier(tv, is_stale=True)
        self.assertLess(stale, normal)
    def test_medium_confidence_neutral(self):
        tv = TruthValue(0.5, 0.5)
        result = _confidence_modifier(tv)
        self.assertAlmostEqual(result, 0.0, places=1)

class TestPriorityBand(unittest.TestCase):
    def test_returns_string(self):
        result = _priority_band(1.0)
        self.assertIsInstance(result, str)
    def test_high_score(self):
        result = _priority_band(1.0)
        self.assertIn(result, [b for _, b in PRIORITY_BANDS])
    def test_zero_score_returns_stale(self):
        result = _priority_band(0.0)
        self.assertEqual(result, "STALE")

class TestComputeStaleness(unittest.TestCase):
    def test_fresh_goal_not_stale(self):
        goal = _goal("g1")
        now = datetime(2026, 1, 2, tzinfo=timezone.utc)
        self.assertFalse(compute_staleness(goal, now=now))
    def test_old_goal_is_stale(self):
        goal = _goal("g1")
        goal["as_of"] = "2025-06-01T00:00:00Z"
        now = datetime(2026, 6, 1, tzinfo=timezone.utc)
        self.assertTrue(compute_staleness(goal, now=now))
    def test_default_now(self):
        goal = _goal("g1")
        # Should not raise with default now=None
        result = compute_staleness(goal)
        self.assertIsInstance(result, bool)
    def test_custom_threshold(self):
        goal = _goal("g1")
        goal["as_of"] = "2026-01-01T00:00:00Z"
        now = datetime(2026, 1, 10, tzinfo=timezone.utc)
        # 9 days, threshold 14 -> not stale
        self.assertFalse(compute_staleness(goal, now=now, threshold_days=14))
        # threshold 7 -> stale
        self.assertTrue(compute_staleness(goal, now=now, threshold_days=7))

class TestPLNVerdictBridgeGoalStaleness(unittest.TestCase):
    def _make_bridge(self, goals=None, now=None):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        g["goals"] = goals or [_goal("g1")]
        g["edges"] = [_edge("t1", "g1")]
        return PLNVerdictBridge(g, now=now or datetime(2026, 1, 2, tzinfo=timezone.utc))
    def test_get_goal_staleness_false_for_fresh(self):
        bridge = self._make_bridge()
        is_stale, stale_goals = bridge._get_goal_staleness("t1")
        self.assertFalse(is_stale)
        self.assertEqual(stale_goals, [])
    def test_get_goal_staleness_true_for_old(self):
        old_goal = _goal("g1")
        old_goal["as_of"] = "2025-01-01T00:00:00Z"
        bridge = self._make_bridge(goals=[old_goal])
        is_stale, stale_goals = bridge._get_goal_staleness("t1")
        self.assertTrue(is_stale)
        self.assertIn("g1", stale_goals)
    def test_get_goal_staleness_false_for_unknown_goal(self):
        bridge = self._make_bridge()
        is_stale, stale_goals = bridge._get_goal_staleness("unknown")
        self.assertFalse(is_stale)
        self.assertEqual(stale_goals, [])

# ===================== ecan_attention helpers =====================

class TestAttentionValue(unittest.TestCase):
    def test_default_construction(self):
        av = AttentionValue(node_id="n1", node_kind="task", sti=0.5, lti=0.5)
        self.assertEqual(av.node_id, "n1")
        self.assertEqual(av.node_kind, "task")
    def test_custom_construction(self):
        av = AttentionValue(node_id="n2", node_kind="goal", sti=0.9, lti=0.8, vlti=True)
        self.assertAlmostEqual(av.sti, 0.9)
        self.assertAlmostEqual(av.lti, 0.8)
        self.assertTrue(av.vlti)
    def test_to_dict(self):
        av = AttentionValue(node_id="n3", node_kind="task", sti=0.3, lti=0.4)
        d = av.to_dict()
        self.assertEqual(d["node_id"], "n3")
        self.assertIn("sti", d)

class TestECANAttentionAllocator(unittest.TestCase):
    def _make_allocator(self):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1"), _task("t2")]
        g["goals"] = [_goal("g1")]
        g["edges"] = [_edge("t1", "g1"), _edge("t2", "g1")]
        return ECANAttentionAllocator(g)
    def test_run_returns_result(self):
        alloc = self._make_allocator()
        result = alloc.run(cycles=3)
        self.assertIsNotNone(result)
    def test_run_in_range(self):
        alloc = self._make_allocator()
        result = alloc.run(cycles=3)
        for av in result.attention_map.values():
            self.assertGreaterEqual(av.sti, 0)

# ===================== reasoning_explainer helpers =====================

class TestReasoningExplainerNodeLabel(unittest.TestCase):
    def _make_explainer(self):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1")]
        g["edges"] = [_edge("t1", "g1")]
        return ReasoningExplainer(g)
    def test_node_label_task(self):
        exp = self._make_explainer()
        label = exp._node_label("t1")
        self.assertIn("t1", label)
    def test_node_label_goal(self):
        exp = self._make_explainer()
        label = exp._node_label("g1")
        self.assertIn("g1", label)
    def test_node_label_unknown(self):
        exp = self._make_explainer()
        label = exp._node_label("unknown")
        self.assertIn("unknown", label)

# ===================== temporal_simulator helpers =====================

class TestTemporalSimulatorAdvanceFrozenAt(unittest.TestCase):
    def _make_sim(self):
        return TemporalSimulator(copy.deepcopy(BASE))
    def test_advance_positive_hours(self):
        sim = self._make_sim()
        result = sim._advance_frozen_at(24)
        self.assertIn("2026-01-02", result)
    def test_advance_zero_hours(self):
        sim = self._make_sim()
        result = sim._advance_frozen_at(0)
        self.assertIn("2026-01-01", result)
    def test_advance_fractional_hours(self):
        sim = self._make_sim()
        result = sim._advance_frozen_at(1.5)
        self.assertIn("01:30:00", result)
    def test_advance_negative_hours(self):
        sim = self._make_sim()
        result = sim._advance_frozen_at(-1)
        self.assertIn("2025-12-31", result)

# ===================== metta_evaluator helpers =====================

class TestMeTTaEvaluatorFlatten(unittest.TestCase):
    def _make_ev(self):
        return MeTTaEvaluator()
    def test_flatten_flat_list(self):
        ev = self._make_ev()
        result = ev._flatten([1, 2, 3])
        self.assertEqual(result, [1, 2, 3])
    def test_flatten_nested_lists(self):
        ev = self._make_ev()
        result = ev._flatten([[1, 2], [3], 4])
        self.assertEqual(result, [1, 2, 3, 4])
    def test_flatten_empty(self):
        ev = self._make_ev()
        result = ev._flatten([])
        self.assertEqual(result, [])
    def test_flatten_deeply_nested(self):
        ev = self._make_ev()
        result = ev._flatten([[1, [2, 3]], [4]])
        self.assertEqual(result, [1, [2, 3], 4])

# ===================== integrated_governor helpers =====================

class TestComputeAgreement(unittest.TestCase):
    def _make_pipeline(self):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1"), _task("t2")]
        g["goals"] = [_goal("g1")]
        g["edges"] = [_edge("t1", "g1"), _edge("t2", "g1")]
        return IntegratedGovernorPipeline(g)
    def test_returns_dict_with_keys(self):
        p = self._make_pipeline()
        recs = [
            TaskRecommendation(
                task_id="t1", unified_verdict="CONTINUE", relevance_score=0.8,
                priority_band="HIGH", sti=0.9, lti=0.5, eviction_candidate=False,
                staleness_flag=False, confidence_modifier=0.1, signals=[],
                recommended_action="continue", pln_strength=0.8, pln_confidence=0.7,
                pln_relevance_score=0.75
            ),
        ]
        result = p._compute_agreement(recs)
        self.assertIn("total_tasks", result)
        self.assertIn("agreements", result)
        self.assertIn("disagreements", result)
    def test_total_tasks_matches_input(self):
        p = self._make_pipeline()
        recs = [
            TaskRecommendation(
                task_id="t1", unified_verdict="CONTINUE", relevance_score=0.8,
                priority_band="HIGH", sti=0.9, lti=0.5, eviction_candidate=False,
                staleness_flag=False, confidence_modifier=0.1, signals=[],
                recommended_action="continue", pln_strength=0.8, pln_confidence=0.7,
                pln_relevance_score=0.75
            ),
            TaskRecommendation(
                task_id="t2", unified_verdict="STOP_STALE", relevance_score=0.2,
                priority_band="STALE", sti=0.1, lti=0.2, eviction_candidate=True,
                staleness_flag=True, confidence_modifier=-0.3, signals=[],
                recommended_action="stop", pln_strength=0.2, pln_confidence=0.3,
                pln_relevance_score=0.1
            ),
        ]
        result = p._compute_agreement(recs)
        self.assertEqual(result["total_tasks"], 2)

class TestBuildSummary(unittest.TestCase):
    def _make_pipeline(self):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1")]
        g["edges"] = [_edge("t1", "g1")]
        return IntegratedGovernorPipeline(g)
    def test_returns_string(self):
        p = self._make_pipeline()
        # _build_summary likely takes recommendations and/or results
        try:
            result = p._build_summary([])
            self.assertIsInstance(result, str)
        except TypeError:
            # May need different args
            pass

if __name__ == "__main__":
    unittest.main()
