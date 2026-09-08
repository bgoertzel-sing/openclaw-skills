"""
Targeted unit tests for _adjust_task_truth_values signal-by-signal.
Each test constructs a minimal graph that triggers exactly one adjustment
and verifies the truth value changes as expected.
"""
import sys, os, unittest, copy
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'atomspace'))
from pln_propagation import PLNPropagator, TruthValue

BASE_GRAPH = {
    "schema_version": "0.1",
    "episode_id": "test",
    "episode_title": "test",
    "frozen_at": "2026-01-01T00:00:00Z",
    "expected_verdict": "CONTINUE",
    "goals": [],
    "projects": [],
    "tasks": [],
    "resources": [],
    "results": [],
    "constraints": [],
    "edges": [],
}

def _task(tid, status="active", reversibility="reversible"):
    return {"id": tid, "kind": "task", "title": tid, "status": status, "owner": "s", "reversibility": reversibility, "source": "s", "as_of": "2026-01-01T00:00:00Z"}

def _goal(gid, status="active", level="intermediate"):
    return {"id": gid, "kind": "goal", "title": gid, "status": status, "level": level, "priority": {"rank": 1, "urgency": "high"}, "source": "s", "as_of": "2026-01-01T00:00:00Z"}

def _edge(frm, to, rel):
    return {"from": frm, "to": to, "relation": rel, "confidence": "high"}

class TestAdjustStale(unittest.TestCase):
    def test_stale_reduces_strength(self):
        g = copy.deepcopy(BASE_GRAPH)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1", status="achieved")]
        g["edges"] = [_edge("t1", "g1", "contributes_to")]
        prop = PLNPropagator(g)
        prop.propagate_upward()
        prop.propagate_downward()
        pre = prop.tvs["t1"].strength
        prop._adjust_task_truth_values({})
        post = prop.tvs["t1"].strength
        self.assertLess(post, pre, "Stale task should have reduced strength")
        self.assertAlmostEqual(post, pre * 0.3, places=2)

class TestAdjustBlocked(unittest.TestCase):
    def test_blocked_reduces_confidence(self):
        g = copy.deepcopy(BASE_GRAPH)
        g["tasks"] = [_task("t1"), _task("t2")]
        g["goals"] = [_goal("g1")]
        g["edges"] = [_edge("t1", "g1", "contributes_to"), _edge("t2", "g1", "contributes_to"), _edge("t2", "t1", "blocks")]
        prop = PLNPropagator(g)
        prop.propagate_upward()
        prop.propagate_downward()
        pre = prop.tvs["t1"].confidence
        prop._adjust_task_truth_values({})
        post = prop.tvs["t1"].confidence
        self.assertLess(post, pre, "Blocked task should have reduced confidence")

class TestAdjustResourceConflict(unittest.TestCase):
    def test_resource_conflict_reduces_confidence(self):
        g = copy.deepcopy(BASE_GRAPH)
        g["tasks"] = [_task("t1"), _task("t2")]
        g["goals"] = [_goal("g1")]
        g["resources"] = [{"id": "r1", "kind": "resource", "title": "r1", "exclusive": True, "status": "active"}]
        g["edges"] = [
            _edge("t1", "g1", "contributes_to"),
            _edge("t2", "g1", "contributes_to"),
            _edge("t1", "r1", "occupies"),
            _edge("t2", "r1", "occupies"),
        ]
        prop = PLNPropagator(g)
        prop.propagate_upward()
        prop.propagate_downward()
        pre_t1 = prop.tvs["t1"].confidence
        prop._adjust_task_truth_values({})
        post_t1 = prop.tvs["t1"].confidence
        self.assertLess(post_t1, pre_t1, "Resource conflict should reduce confidence")

class TestAdjustNoEvidence(unittest.TestCase):
    def test_no_evidence_reduces_confidence(self):
        g = copy.deepcopy(BASE_GRAPH)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1")]
        g["edges"] = [_edge("t1", "g1", "contributes_to")]
        # No results, no evidence → confidence should be reduced
        prop = PLNPropagator(g)
        prop.propagate_upward()
        prop.propagate_downward()
        pre = prop.tvs["t1"].confidence
        prop._adjust_task_truth_values({})
        post = prop.tvs["t1"].confidence
        self.assertLess(post, pre, "No evidence should reduce confidence")

class TestAdjustMultiGoalBoost(unittest.TestCase):
    def test_multi_goal_boosts_strength(self):
        g = copy.deepcopy(BASE_GRAPH)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1"), _goal("g2")]
        g["edges"] = [_edge("t1", "g1", "contributes_to"), _edge("t1", "g2", "contributes_to"), _edge("g1", "g2", "contributes_to")]
        prop = PLNPropagator(g)
        prop.propagate_upward()
        prop.propagate_downward()
        pre = prop.tvs["t1"].strength
        prop._adjust_task_truth_values({})
        post = prop.tvs["t1"].strength
        # Multi-goal should boost (or at least not reduce) strength
        self.assertGreaterEqual(post, pre, "Multi-goal should not reduce strength")

class TestAdjustNoChange(unittest.TestCase):
    def test_clean_task_unchanged(self):
        """A clean active task with one active goal and evidence should not be adjusted down."""
        g = copy.deepcopy(BASE_GRAPH)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1")]
        g["results"] = [{"id": "res1", "kind": "result", "goal_id": "g1", "status": "reported", "title": "res1"}]
        g["edges"] = [_edge("t1", "g1", "contributes_to"), _edge("res1", "g1", "provides_evidence_for")]
        prop = PLNPropagator(g)
        prop.propagate_upward()
        prop.propagate_downward()
        pre_s = prop.tvs["t1"].strength
        pre_c = prop.tvs["t1"].confidence
        prop._adjust_task_truth_values({})
        post_s = prop.tvs["t1"].strength
        post_c = prop.tvs["t1"].confidence
        # No stale, no blocked, no conflict, has evidence, reversible, single goal → no reduction
        self.assertEqual(post_s, pre_s, "Clean task strength should not change")
        self.assertEqual(post_c, pre_c, "Clean task confidence should not change")

class TestAdjustClamping(unittest.TestCase):
    def test_values_clamped_01(self):
        """All adjusted values should be in [0, 1]."""
        g = copy.deepcopy(BASE_GRAPH)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1", status="achieved")]
        g["edges"] = [_edge("t1", "g1", "contributes_to")]
        prop = PLNPropagator(g)
        prop.propagate_upward()
        prop.propagate_downward()
        prop._adjust_task_truth_values({})
        tv = prop.tvs["t1"]
        self.assertGreaterEqual(tv.strength, 0.0)
        self.assertLessEqual(tv.strength, 1.0)
        self.assertGreaterEqual(tv.confidence, 0.0)
        self.assertLessEqual(tv.confidence, 1.0)

if __name__ == '__main__':
    unittest.main()
