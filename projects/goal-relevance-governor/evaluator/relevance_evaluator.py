#!/usr/bin/env python3
"""Goal Relevance Governor - Read-Only Relevance Evaluator v0.1."""

from __future__ import annotations
import json
from dataclasses import dataclass, field, asdict
from typing import Optional
from datetime import datetime, timezone
from pln_propagation import normalize_status

CONTINUE = "CONTINUE"
ACCELERATE = "ACCELERATE"
PAUSE_RECOVERABLY = "PAUSE_RECOVERABLY"
STOP_STALE = "STOP_STALE"
REPLAN = "REPLAN"
DEFER = "DEFER"
ESCALATE = "ESCALATE"
BLOCKED = "BLOCKED"
AUTHORITY = "read_only_shadow"


@dataclass
class Verdict:
    task_id: str
    verdict: str
    reasons: list = field(default_factory=list)
    evidence: list = field(default_factory=list)
    alternatives: list = field(default_factory=list)
    authority: str = AUTHORITY
    expiry: Optional[str] = None
    generated_at: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


class Graph:
    def __init__(self, data: dict):
        self.nodes = {}
        self.edges = []
        for key in ("goals", "projects", "tasks", "resources", "results", "constraints"):
            for node in data.get(key, []):
                self.nodes[node["id"]] = node
        self.edges = data.get("edges", [])
        self.as_of = data.get("as_of", datetime.now(timezone.utc).isoformat())

    def outgoing(self, node_id, relation=None):
        return [e for e in self.edges if e["from"] == node_id and (relation is None or e["relation"] == relation)]

    def incoming(self, node_id, relation=None):
        return [e for e in self.edges if e["to"] == node_id and (relation is None or e["relation"] == relation)]

    def get(self, node_id):
        return self.nodes.get(node_id)

    def get_active_goals_for(self, task_id):
        goals = []
        for e in self.outgoing(task_id, "contributes_to"):
            target = self.get(e["to"])
            if target and target.get("kind") == "goal":
                goals.append(target)
                if target.get("level") == "intermediate":
                    for e2 in self.outgoing(target["id"], "contributes_to"):
                        t2 = self.get(e2["to"])
                        if t2 and t2.get("kind") == "goal":
                            goals.append(t2)
        return goals

    def get_direct_goals(self, task_id):
        goals = []
        for e in self.outgoing(task_id, "contributes_to"):
            target = self.get(e["to"])
            if target and target.get("kind") == "goal":
                goals.append(target)
        return goals

    def get_occupied_resources(self, task_id):
        results = []
        for e in self.outgoing(task_id, "occupies"):
            r = self.get(e["to"])
            if r:
                results.append(r)
        return results

    def get_resource_holders(self, resource_id):
        results = []
        for e in self.incoming(resource_id, "occupies"):
            t = self.get(e["from"])
            if t and normalize_status(t.get("status", "active")) == "active":
                results.append(t)
        return results

    def get_project_for_task(self, task_id):
        for e in self.outgoing(task_id, "part_of"):
            p = self.get(e["to"])
            if p and p.get("kind") == "project":
                return p
        return None

    def get_blocking_constraints(self, task_id):
        results = []
        for e in self.incoming(task_id, "blocks"):
            c = self.get(e["from"])
            if c:
                results.append(c)
        return results

    def get_superseding_goals(self, goal_id):
        results = []
        for e in self.incoming(goal_id, "supersedes"):
            g = self.get(e["from"])
            if g:
                results.append(g)
        return results


class RelevanceEvaluator:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.now = datetime.now(timezone.utc).isoformat()

    def evaluate_task(self, task: dict) -> Verdict:
        tid = task["id"]

        # Rule 1: STOP_STALE if no direct parent goals or all direct parents inactive
        direct_goals = self.graph.get_direct_goals(tid)
        if not direct_goals:
            return Verdict(tid, STOP_STALE,
                ["Task has no parent goal edges"],
                ["No contributes_to edge from this task to any goal"],
                ["Link task to an active goal or close it"],
                generated_at=self.now)

        all_direct_inactive = all(normalize_status(g.get("status", "active")) in ("achieved", "cancelled") for g in direct_goals)
        if all_direct_inactive:
            return Verdict(tid, STOP_STALE,
                ["All direct parent goals are achieved or cancelled"],
                [g["id"] + " status=" + str(g.get("status")) for g in direct_goals],
                ["Link task to a new unmet goal or close it"],
                generated_at=self.now)

        # Get transitive goals for remaining rules
        goals = self.graph.get_active_goals_for(tid)
        active_goals = [g for g in goals if normalize_status(g.get("status", "active")) == "active"]

        # Rule 2: BLOCKED if blocked by constraint
        blockers = self.graph.get_blocking_constraints(tid)
        if blockers:
            return Verdict(tid, BLOCKED,
                ["Task is blocked by constraint(s)"],
                [c["id"] + ": " + str(c.get("title", "")) for c in blockers],
                ["Resolve blocker or replan around it"],
                generated_at=self.now)

        # Rule 3: PAUSE_RECOVERABLY if holds exclusive resource needed by higher-priority task
        occupied = self.graph.get_occupied_resources(tid)
        for res in occupied:
            if not res.get("exclusive", False):
                continue
            holders = self.graph.get_resource_holders(res["id"])
            for holder in holders:
                if holder["id"] == tid:
                    continue
                holder_goals = self.graph.get_active_goals_for(holder["id"])
                for hg in holder_goals:
                    if normalize_status(hg.get("status", "active")) != "active":
                        continue
                    for tg in active_goals:
                        hg_rank = hg.get("priority", {}).get("rank", 999)
                        tg_rank = tg.get("priority", {}).get("rank", 999)
                        if hg_rank < tg_rank and task.get("reversibility") == "checkpointable":
                            return Verdict(tid, PAUSE_RECOVERABLY,
                                ["Holds exclusive resource " + res["id"] + " needed by higher-priority task " + holder["id"]],
                                ["Resource " + res["id"] + " is exclusive"],
                                ["Pause this task, preserve checkpoint, release resource"],
                                generated_at=self.now)

        # Rule 4: DEFER if premature hardening on early-stage research
        project = self.graph.get_project_for_task(tid)
        if project:
            rc = project.get("result_contract", {})
            stage = rc.get("maturity_stage", "")
            kind = rc.get("project_kind", "")
            if kind in ("exploratory_research", "confirmatory_research") and stage in ("E0_exploration", "E1_signal_validation"):
                if task.get("reversibility") == "irreversible":
                    return Verdict(tid, DEFER,
                        ["Task appears to be irreversible hardening on an early-stage research project",
                         "Project " + project["id"] + " kind=" + kind + " stage=" + stage],
                        ["result_contract.maturity_stage=" + stage,
                         "task.reversibility=irreversible"],
                        ["Defer hardening until the hardening_trigger fires or maturity advances"],
                        generated_at=self.now)

        # Rule 5: REPLAN if parent goal has been superseded
        for g in goals:
            if normalize_status(g.get("status", "active")) == "superseded":
                superseding = self.graph.get_superseding_goals(g["id"])
                if superseding:
                    return Verdict(tid, REPLAN,
                        ["Parent goal " + g["id"] + " has been superseded by " + superseding[0]["id"]],
                        ["supersedes edge: " + superseding[0]["id"] + " -> " + g["id"]],
                        ["Re-link task to " + superseding[0]["id"] + " or replan around new goal"],
                        generated_at=self.now)

        # Rule 6: ESCALATE if multiple active goals with no recorded results
        if active_goals and len(active_goals) > 1:
            has_results = False
            for g in active_goals:
                if self.graph.incoming(g["id"], "provides_evidence_for"):
                    has_results = True
                    break
            if not has_results and normalize_status(task.get("status", "active")) == "active":
                return Verdict(tid, ESCALATE,
                    ["Task has multiple active goals and no recorded results to disambiguate priority"],
                    [str(len(active_goals)) + " active goals, no provides_evidence_for edges"],
                    ["Human should clarify which goal path this task advances"],
                    generated_at=self.now)

        # Default: CONTINUE
        return Verdict(tid, CONTINUE,
            ["Task has active parent goals and no blocking issues detected"],
            [str(len(active_goals)) + " active goal(s)"] + [g["id"] + " status=" + g["status"] for g in active_goals],
            [],
            generated_at=self.now)
    def evaluate_all(self) -> list:
        verdicts = []
        for node in self.graph.nodes.values():
            if node.get("kind") == "task" and normalize_status(node.get("status", "active")) == "active":
                verdicts.append(self.evaluate_task(node))
        return verdicts


if __name__ == "__main__":
    import sys
    data = json.load(open(sys.argv[1]))
    g = Graph(data)
    ev = RelevanceEvaluator(g)
    for v in ev.evaluate_all():
        print(json.dumps(v.to_dict(), indent=2))
