"""Tests for RemediationEngine verdict handlers and plan generation."""
import unittest
import copy
from atomspace.remediation_engine import RemediationEngine, RemediationStep, RemediationPlan

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

def _goal(gid, status="active"):
    return {"id": gid, "kind": "goal", "title": gid, "status": status,
            "level": "intermediate", "priority": {"rank": 1, "urgency": "high"},
            "source": "s", "as_of": "2026-01-01T00:00:00Z"}

def _resource(rid):
    return {"id": rid, "kind": "resource", "title": rid, "status": "available",
            "source": "s", "as_of": "2026-01-01T00:00:00Z"}

def _rec(task_id, verdict, signals=None):
    return {"task_id": task_id, "unified_verdict": verdict, "signals": signals or []}


class TestStopStale(unittest.TestCase):
    def test_basic(self):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1", status="achieved")]
        g["edges"] = [{"from": "t1", "to": "g1", "relation": "contributes_to", "confidence": "high"}]
        eng = RemediationEngine(g)
        plan = eng.generate_plan(_rec("t1", "STOP_STALE"))
        self.assertEqual(plan.verdict, "STOP_STALE")
        self.assertGreaterEqual(len(plan.steps), 1)
        self.assertEqual(plan.steps[0].action, "abandon_task")
        self.assertEqual(plan.steps[0].target, "t1")
        self.assertEqual(plan.steps[0].priority, 1)

    def test_releases_resources(self):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1", status="achieved")]
        g["resources"] = [_resource("r1"), _resource("r2")]
        g["edges"] = [
            {"from": "t1", "to": "g1", "relation": "contributes_to", "confidence": "high"},
            {"from": "t1", "to": "r1", "relation": "occupies", "confidence": "high"},
            {"from": "t1", "to": "r2", "relation": "occupies", "confidence": "high"},
        ]
        eng = RemediationEngine(g)
        plan = eng.generate_plan(_rec("t1", "STOP_STALE"))
        release = [s for s in plan.steps if s.action == "release_resource"]
        self.assertEqual(len(release), 2)
        self.assertEqual({s.target for s in release}, {"r1", "r2"})
        for s in release:
            self.assertIn("s1", s.depends_on)

    def test_notifies_stakeholders(self):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1", status="abandoned")]
        g["edges"] = [{"from": "t1", "to": "g1", "relation": "contributes_to", "confidence": "high"}]
        eng = RemediationEngine(g)
        plan = eng.generate_plan(_rec("t1", "STOP_STALE"))
        notify = [s for s in plan.steps if s.action == "notify_stakeholders"]
        self.assertEqual(len(notify), 1)
        self.assertIn("g1", notify[0].target)


class TestEscalate(unittest.TestCase):
    def test_basic(self):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1")]
        g["edges"] = [{"from": "t1", "to": "g1", "relation": "contributes_to", "confidence": "high"}]
        eng = RemediationEngine(g)
        plan = eng.generate_plan(_rec("t1", "ESCALATE", ["reason=manual_override_required"]))
        self.assertEqual(plan.verdict, "ESCALATE")
        self.assertGreaterEqual(len(plan.steps), 1)


class TestPause(unittest.TestCase):
    def test_with_blocker(self):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1"), _task("t2")]
        g["goals"] = [_goal("g1")]
        g["resources"] = [_resource("r1")]
        g["edges"] = [
            {"from": "t1", "to": "g1", "relation": "contributes_to", "confidence": "high"},
            {"from": "t1", "to": "r1", "relation": "occupies", "confidence": "high"},
        ]
        eng = RemediationEngine(g)
        plan = eng.generate_plan(_rec("t1", "PAUSE_RECOVERABLY", ["higher_priority_task=t2", "resource=r1"]))
        self.assertEqual(plan.verdict, "PAUSE_RECOVERABLY")
        actions = [s.action for s in plan.steps]
        self.assertIn("pause_task", actions)
        self.assertIn("monitor_blocker", actions)
        self.assertIn("resume_task", actions)

    def test_without_blocker(self):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1")]
        g["edges"] = [{"from": "t1", "to": "g1", "relation": "contributes_to", "confidence": "high"}]
        eng = RemediationEngine(g)
        plan = eng.generate_plan(_rec("t1", "PAUSE_RECOVERABLY", []))
        actions = [s.action for s in plan.steps]
        self.assertIn("pause_task", actions)
        self.assertIn("schedule_recheck", actions)


class TestDefer(unittest.TestCase):
    def test_basic(self):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1"), _goal("g2")]
        g["edges"] = [
            {"from": "t1", "to": "g1", "relation": "contributes_to", "confidence": "high"},
            {"from": "t1", "to": "g2", "relation": "contributes_to", "confidence": "high"},
        ]
        eng = RemediationEngine(g)
        plan = eng.generate_plan(_rec("t1", "DEFER", ["higher_priority_goal=g2"]))
        self.assertEqual(plan.verdict, "DEFER")
        self.assertGreaterEqual(len(plan.steps), 1)


class TestReplan(unittest.TestCase):
    def test_with_superseded(self):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1", status="superseded"), _goal("g2")]
        g["edges"] = [
            {"from": "t1", "to": "g1", "relation": "contributes_to", "confidence": "high"},
            {"from": "t1", "to": "g2", "relation": "contributes_to", "confidence": "high"},
        ]
        eng = RemediationEngine(g)
        plan = eng.generate_plan(_rec("t1", "REPLAN", ["superseded_goal=g1", "superseded_by=g2"]))
        self.assertEqual(plan.verdict, "REPLAN")
        actions = [s.action for s in plan.steps]
        self.assertIn("redesign_task", actions)
        self.assertIn("update_goal_link", actions)

    def test_without_superseded(self):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1")]
        g["edges"] = [{"from": "t1", "to": "g1", "relation": "contributes_to", "confidence": "high"}]
        eng = RemediationEngine(g)
        plan = eng.generate_plan(_rec("t1", "REPLAN", []))
        self.assertEqual(plan.verdict, "REPLAN")
        self.assertGreaterEqual(len(plan.steps), 1)


class TestContinue(unittest.TestCase):
    def test_basic(self):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1")]
        g["edges"] = [{"from": "t1", "to": "g1", "relation": "contributes_to", "confidence": "high"}]
        eng = RemediationEngine(g)
        plan = eng.generate_plan(_rec("t1", "CONTINUE"))
        self.assertEqual(plan.verdict, "CONTINUE")
        self.assertGreaterEqual(len(plan.steps), 1)


class TestUnknownVerdict(unittest.TestCase):
    def test_unknown(self):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        eng = RemediationEngine(g)
        plan = eng.generate_plan(_rec("t1", "UNKNOWN_VERDICT"))
        self.assertEqual(plan.verdict, "UNKNOWN_VERDICT")
        self.assertEqual(len(plan.steps), 0)


class TestGenerateAll(unittest.TestCase):
    def test_generate_all(self):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1"), _task("t2")]
        g["goals"] = [_goal("g1", status="achieved"), _goal("g2")]
        g["edges"] = [
            {"from": "t1", "to": "g1", "relation": "contributes_to", "confidence": "high"},
            {"from": "t2", "to": "g2", "relation": "contributes_to", "confidence": "high"},
        ]
        eng = RemediationEngine(g)
        plans = eng.generate_all([
            _rec("t1", "STOP_STALE"),
            _rec("t2", "CONTINUE"),
        ])
        self.assertEqual(len(plans), 2)
        self.assertEqual(plans[0].verdict, "STOP_STALE")
        self.assertEqual(plans[1].verdict, "CONTINUE")


class TestBuildIndex(unittest.TestCase):
    def test_task_goals_indexed(self):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        g["goals"] = [_goal("g1"), _goal("g2")]
        g["edges"] = [
            {"from": "t1", "to": "g1", "relation": "contributes_to", "confidence": "high"},
            {"from": "t1", "to": "g2", "relation": "contributes_to", "confidence": "high"},
        ]
        eng = RemediationEngine(g)
        self.assertEqual(eng.task_goals["t1"], ["g1", "g2"])

    def test_task_resources_indexed(self):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        g["resources"] = [_resource("r1")]
        g["edges"] = [
            {"from": "t1", "to": "r1", "relation": "occupies", "confidence": "high"},
        ]
        eng = RemediationEngine(g)
        self.assertEqual(eng.task_resources["t1"], ["r1"])

    def test_no_edges(self):
        g = copy.deepcopy(BASE)
        g["tasks"] = [_task("t1")]
        eng = RemediationEngine(g)
        self.assertEqual(eng.task_goals.get("t1", []), [])
        self.assertEqual(eng.task_resources.get("t1", []), [])


class TestRemediationStepToDict(unittest.TestCase):
    def test_to_dict(self):
        step = RemediationStep(
            step_id="s1", action="pause_task", target="t1",
            description="Pause t1", priority=2,
            depends_on=[], verification="t1 paused",
            estimated_effort="trivial")
        d = step.to_dict()
        self.assertEqual(d["step_id"], "s1")
        self.assertEqual(d["action"], "pause_task")
        self.assertEqual(d["target"], "t1")
        self.assertEqual(d["priority"], 2)
        self.assertEqual(d["depends_on"], [])


class TestRemediationPlanToDict(unittest.TestCase):
    def test_to_dict(self):
        step = RemediationStep(
            step_id="s1", action="abandon_task", target="t1",
            description="Abandon t1", priority=1,
            depends_on=[], verification="t1 abandoned",
            estimated_effort="trivial")
        plan = RemediationPlan(
            task_id="t1", verdict="STOP_STALE", steps=[step],
            plan_summary="Abandon t1", rollback_plan="Reactivate",
            success_criteria="t1 abandoned", risk_notes="Low")
        d = plan.to_dict()
        self.assertEqual(d["task_id"], "t1")
        self.assertEqual(d["verdict"], "STOP_STALE")
        self.assertEqual(len(d["steps"]), 1)
        self.assertEqual(d["steps"][0]["action"], "abandon_task")


if __name__ == "__main__":
    unittest.main()
