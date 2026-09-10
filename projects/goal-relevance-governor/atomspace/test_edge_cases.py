"""
Edge-case integration tests for the IntegratedGovernorPipeline.

Tests boundary conditions discovered during exploratory testing:
  - empty graph (no crash)
  - single task with no goals
  - circular contributes_to edges (no infinite loop)
  - deep goal hierarchy (5 levels)
  - blocked task visibility (with and without blocks-edge)
  - resource conflict (3-way exclusive resource)
  - mixed-status graph (10 tasks, 5 goals)
  - all goals achieved
  - PLN truth value ranges
"""
import sys, os, unittest, copy
sys.path.insert(0, os.path.dirname(__file__))
from integrated_governor import IntegratedGovernorPipeline

BASE = {
    "schema_version": "0.1", "episode_id": "test", "episode_title": "test",
    "frozen_at": "2026-01-01T00:00:00Z", "expected_verdict": "CONTINUE",
    "goals": [], "projects": [], "tasks": [], "resources": [],
    "results": [], "constraints": [], "edges": [],
}


def _task(tid, status="active", rev="reversible"):
    return {"id": tid, "kind": "task", "title": tid, "status": status,
            "owner": "s", "reversibility": rev, "source": "s",
            "as_of": "2026-01-01T00:00:00Z"}


def _goal(gid, status="active", level="intermediate"):
    return {"id": gid, "kind": "goal", "title": gid, "status": status,
            "level": level, "priority": {"rank": 1, "urgency": "high"},
            "source": "s", "as_of": "2026-01-01T00:00:00Z"}


def _edge(f, t, r):
    return {"from": f, "to": t, "relation": r, "confidence": "high"}


class TestEdgeCases(unittest.TestCase):
    """Boundary-condition integration tests."""

    def test_empty_graph_no_crash(self):
        """Empty graph should not crash and produce zero recommendations."""
        g = copy.deepcopy(BASE)
        p = IntegratedGovernorPipeline(g)
        r = p.run(ecan_cycles=5)
        self.assertEqual(len(r.recommendations), 0)
        self.assertEqual(r.pln_task_count, 0)

    def test_single_task_no_goals_stop_stale(self):
        """A lone task with no goals should get STOP_STALE."""
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        p = IntegratedGovernorPipeline(g)
        r = p.run(ecan_cycles=5)
        self.assertEqual(len(r.recommendations), 1)
        self.assertEqual(r.recommendations[0].unified_verdict, "STOP_STALE")
        self.assertEqual(r.recommendations[0].relevance_score, 0.0)

    def test_circular_edges_no_infinite_loop(self):
        """Circular contributes_to edges should not cause infinite recursion."""
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1")]
        g["edges"] = [_edge("t1", "g1", "contributes_to"),
                      _edge("g1", "t1", "contributes_to")]
        p = IntegratedGovernorPipeline(g)
        r = p.run(ecan_cycles=5)
        self.assertEqual(len(r.recommendations), 1)
        self.assertEqual(r.recommendations[0].unified_verdict, "CONTINUE")

    def test_deep_hierarchy_5_levels(self):
        """A 5-level goal hierarchy should propagate correctly."""
        g = copy.deepcopy(BASE)
        for i in range(5):
            level = "terminal" if i == 4 else ("intermediate" if i > 0 else "top")
            g["goals"].append(_goal("g%d" % i, level=level))
            if i > 0:
                g["edges"].append(_edge("g%d" % i, "g%d" % (i - 1), "contributes_to"))
        g["tasks"] = [_task("t1")]
        g["edges"].append(_edge("t1", "g4", "contributes_to"))
        p = IntegratedGovernorPipeline(g)
        r = p.run(ecan_cycles=10)
        self.assertEqual(len(r.recommendations), 1)
        rec = r.recommendations[0]
        self.assertEqual(rec.unified_verdict, "CONTINUE")
        self.assertGreater(rec.pln_strength, 0.0)
        self.assertGreater(rec.pln_confidence, 0.0)

    def test_all_goals_achieved_stop_stale(self):
        """A task whose all goals are achieved should get STOP_STALE."""
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1", status="achieved")]
        g["edges"] = [_edge("t1", "g1", "contributes_to")]
        p = IntegratedGovernorPipeline(g)
        r = p.run(ecan_cycles=5)
        self.assertEqual(len(r.recommendations), 1)
        self.assertEqual(r.recommendations[0].unified_verdict, "STOP_STALE")
        self.assertLess(r.recommendations[0].pln_strength, 0.5)

    def test_3way_resource_conflict(self):
        """Three tasks competing for same exclusive resource."""
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1"), _task("t2"), _task("t3")]
        g["goals"] = [_goal("g1")]
        g["resources"] = [{"id": "r1", "kind": "resource", "title": "r1",
                           "exclusive": True, "status": "active"}]
        g["edges"] = [
            _edge("t1", "g1", "contributes_to"),
            _edge("t2", "g1", "contributes_to"),
            _edge("t3", "g1", "contributes_to"),
            _edge("t1", "r1", "occupies"),
            _edge("t2", "r1", "occupies"),
            _edge("t3", "r1", "occupies"),
        ]
        p = IntegratedGovernorPipeline(g)
        r = p.run(ecan_cycles=10)
        self.assertEqual(len(r.recommendations), 3)
        verdicts = [rec.unified_verdict for rec in r.recommendations]
        self.assertIn("REPLAN", verdicts)
        self.assertIn("CONTINUE", verdicts)

    def test_blocked_by_edge_gets_blocked_verdict(self):
        """An active task blocked by another task should get BLOCKED verdict."""
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1"), _task("t2")]
        g["goals"] = [_goal("g1")]
        g["edges"] = [
            _edge("t1", "g1", "contributes_to"),
            _edge("t2", "g1", "contributes_to"),
            _edge("t2", "t1", "blocks"),
        ]
        p = IntegratedGovernorPipeline(g)
        r = p.run(ecan_cycles=10)
        self.assertEqual(len(r.recommendations), 2)
        rec_map = {rec.task_id: rec for rec in r.recommendations}
        self.assertEqual(rec_map["t1"].unified_verdict, "BLOCKED")
        self.assertEqual(rec_map["t2"].unified_verdict, "CONTINUE")
        self.assertLess(rec_map["t1"].pln_confidence,
                        rec_map["t2"].pln_confidence)

    def test_big_mixed_graph_10_tasks_5_goals(self):
        """10 tasks, 5 goals (3 active, 2 abandoned), 7 active + 3 blocked tasks."""
        g = copy.deepcopy(BASE)
        for i in range(10):
            g["tasks"].append(_task("t%d" % i, status="active" if i < 7 else "blocked"))
        for i in range(5):
            g["goals"].append(_goal("g%d" % i, status="active" if i < 3 else "abandoned"))
        for i in range(10):
            g["edges"].append(_edge("t%d" % i, "g%d" % (i % 5), "contributes_to"))
        p = IntegratedGovernorPipeline(g)
        r = p.run(ecan_cycles=20)
        active_active_recs = [
            rec for rec in r.recommendations
            if int(rec.task_id[1:]) < 7 and int(rec.task_id[1:]) % 5 < 3
        ]
        self.assertGreater(len(active_active_recs), 0)
        stale_recs = [
            rec for rec in r.recommendations
            if rec.unified_verdict == "STOP_STALE"
        ]
        self.assertGreater(len(stale_recs), 0)

    def test_pln_truth_values_in_range(self):
        """All PLN truth values should be in [0, 1]."""
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1")]
        g["edges"] = [_edge("t1", "g1", "contributes_to")]
        p = IntegratedGovernorPipeline(g)
        r = p.run(ecan_cycles=5)
        for rec in r.recommendations:
            self.assertGreaterEqual(rec.pln_strength, 0.0)
            self.assertLessEqual(rec.pln_strength, 1.0)
            self.assertGreaterEqual(rec.pln_confidence, 0.0)
            self.assertLessEqual(rec.pln_confidence, 1.0)
            self.assertGreaterEqual(rec.pln_relevance_score, 0.0)
            self.assertLessEqual(rec.pln_relevance_score, 1.0)

    def test_abandoned_goal_tasks_get_stop_stale(self):
        """Tasks contributing only to abandoned goals should get STOP_STALE."""
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1", status="abandoned")]
        g["edges"] = [_edge("t1", "g1", "contributes_to")]
        p = IntegratedGovernorPipeline(g)
        r = p.run(ecan_cycles=5)
        self.assertEqual(len(r.recommendations), 1)
        self.assertEqual(r.recommendations[0].unified_verdict, "STOP_STALE")

    def test_stale_pln_strength_lower_than_healthy(self):
        """Stale task PLN strength should be lower than healthy task."""
        healthy = copy.deepcopy(BASE)
        healthy["tasks"] = [_task("t1")]
        healthy["goals"] = [_goal("g1", status="active")]
        healthy["edges"] = [_edge("t1", "g1", "contributes_to")]
        p1 = IntegratedGovernorPipeline(healthy)
        r1 = p1.run(ecan_cycles=5)
        healthy_strength = r1.recommendations[0].pln_strength

        stale = copy.deepcopy(BASE)
        stale["tasks"] = [_task("t1")]
        stale["goals"] = [_goal("g1", status="achieved")]
        stale["edges"] = [_edge("t1", "g1", "contributes_to")]
        p2 = IntegratedGovernorPipeline(stale)
        r2 = p2.run(ecan_cycles=5)
        stale_strength = r2.recommendations[0].pln_strength
        self.assertLess(stale_strength, healthy_strength,
                        "Stale task should have lower PLN strength")

    def test_agreement_tracking_present(self):
        """PLN-bridge agreement tracking should be present and have counts."""
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1"), _task("t2")]
        g["goals"] = [_goal("g1")]
        g["edges"] = [_edge("t1", "g1", "contributes_to"),
                      _edge("t2", "g1", "contributes_to")]
        p = IntegratedGovernorPipeline(g)
        r = p.run(ecan_cycles=5)
        self.assertIn("total_tasks", r.pln_bridge_agreement)
        self.assertIn("agreements", r.pln_bridge_agreement)
        self.assertIn("disagreements", r.pln_bridge_agreement)
        self.assertEqual(r.pln_bridge_agreement["total_tasks"], 2)

    def test_executive_summary_nonempty(self):
        """Executive summary should not be empty when there are recommendations."""
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1")]
        g["edges"] = [_edge("t1", "g1", "contributes_to")]
        p = IntegratedGovernorPipeline(g)
        r = p.run(ecan_cycles=5)
        self.assertGreater(len(r.executive_summary), 0)

    def test_relevance_score_decreases_for_stale(self):
        """Relevance score should be lower for stale tasks than healthy ones."""
        healthy = copy.deepcopy(BASE)
        healthy["tasks"] = [_task("t1")]
        healthy["goals"] = [_goal("g1", status="active")]
        healthy["edges"] = [_edge("t1", "g1", "contributes_to")]
        p1 = IntegratedGovernorPipeline(healthy)
        r1 = p1.run(ecan_cycles=5)
        healthy_rel = r1.recommendations[0].relevance_score

        stale = copy.deepcopy(BASE)
        stale["tasks"] = [_task("t1")]
        stale["goals"] = [_goal("g1", status="achieved")]
        stale["edges"] = [_edge("t1", "g1", "contributes_to")]
        p2 = IntegratedGovernorPipeline(stale)
        r2 = p2.run(ecan_cycles=5)
        stale_rel = r2.recommendations[0].relevance_score
        self.assertLessEqual(stale_rel, healthy_rel,
                            "Stale task relevance should not exceed healthy")


if __name__ == "__main__":
    unittest.main()
