#!/usr/bin/env python3
"""Unit tests for relevance_evaluator.py + replay corpus validation."""

import json, os, sys, unittest
sys.path.insert(0, os.path.dirname(__file__))
from relevance_evaluator import Graph, RelevanceEvaluator, Verdict, CONTINUE, STOP_STALE, PAUSE_RECOVERABLY, DEFER, REPLAN, BLOCKED, ESCALATE

CORPUS_DIR = os.path.join(os.path.dirname(__file__), "..", "replay_corpus")


class TestReplayCorpus(unittest.TestCase):
    """Validate that all replay episodes produce the expected verdict."""

    def _run_episode(self, fname):
        path = os.path.join(CORPUS_DIR, fname)
        with open(path) as f:
            data = json.load(f)
        g = Graph(data)
        ev = RelevanceEvaluator(g)
        verdicts = ev.evaluate_all()
        self.assertTrue(len(verdicts) > 0, f"No active tasks found in {fname}")
        expected = data["expected_verdict"]
        # Check the first (primary) task's verdict
        self.assertEqual(verdicts[0].verdict, expected,
            f"{fname}: expected {expected}, got {verdicts[0].verdict} (reasons: {verdicts[0].reasons})")

    def test_episode_01_stale(self):
        self._run_episode("episode_01_stale_codegen.json")

    def test_episode_02_blocking(self):
        self._run_episode("episode_02_chem_blocking.json")

    def test_episode_03_premature(self):
        self._run_episode("episode_03_premature_hardening.json")

    def test_episode_04_replan(self):
        self._run_episode("episode_04_overengineered_repair.json")

    def test_episode_05_control(self):
        self._run_episode("episode_05_control_justified_long_running.json")


class TestGraphTraversal(unittest.TestCase):
    """Unit tests for Graph traversal methods."""

    def setUp(self):
        self.data = {
            "goals": [
                {"id": "g1", "kind": "goal", "status": "active", "level": "top",
                 "priority": {"rank": 1}},
                {"id": "g2", "kind": "goal", "status": "achieved", "level": "intermediate",
                 "priority": {"rank": 2}},
                {"id": "g3", "kind": "goal", "status": "active", "level": "intermediate",
                 "priority": {"rank": 3}},
            ],
            "tasks": [
                {"id": "t1", "kind": "task", "status": "active", "reversibility": "reversible"},
                {"id": "t2", "kind": "task", "status": "active", "reversibility": "reversible"},
            ],
            "resources": [
                {"id": "r1", "kind": "resource", "exclusive": True},
            ],
            "results": [
                {"id": "res1", "kind": "result", "title": "Prior result", "status": "validated"},
            ],
            "edges": [
                {"from": "t1", "to": "g2", "relation": "contributes_to"},
                {"from": "g2", "to": "g1", "relation": "contributes_to"},
                {"from": "t2", "to": "g3", "relation": "contributes_to"},
                {"from": "g3", "to": "g1", "relation": "contributes_to"},
                {"from": "res1", "to": "g3", "relation": "provides_evidence_for"},
            ],
        }
        self.g = Graph(self.data)

    def test_direct_goals(self):
        dg = self.g.get_direct_goals("t1")
        self.assertEqual(len(dg), 1)
        self.assertEqual(dg[0]["id"], "g2")

    def test_transitive_goals(self):
        ag = self.g.get_active_goals_for("t1")
        # g2 is achieved, but g1 (transitive parent) is active
        ids = [x["id"] for x in ag]
        self.assertIn("g2", ids)
        self.assertIn("g1", ids)

    def test_stale_task_with_achieved_direct_parent(self):
        ev = RelevanceEvaluator(self.g)
        v = ev.evaluate_task(self.g.get("t1"))
        self.assertEqual(v.verdict, STOP_STALE)

    def test_active_task_continues(self):
        ev = RelevanceEvaluator(self.g)
        v = ev.evaluate_task(self.g.get("t2"))
        self.assertEqual(v.verdict, CONTINUE)


class TestVerdictStructure(unittest.TestCase):
    """Tests for Verdict dataclass structure."""

    def test_verdict_fields(self):
        v = Verdict("t1", CONTINUE, ["ok"], ["e1"], ["a1"])
        d = v.to_dict()
        self.assertEqual(d["task_id"], "t1")
        self.assertEqual(d["verdict"], CONTINUE)
        self.assertEqual(d["reasons"], ["ok"])
        self.assertEqual(d["evidence"], ["e1"])
        self.assertEqual(d["alternatives"], ["a1"])
        self.assertEqual(d["authority"], "read_only_shadow")


if __name__ == "__main__":
    unittest.main(verbosity=2)
