"""Hybrid Python-MeTTa Goal Relevance Evaluator v0.3

Loads a MeTTa atomspace file and evaluates task verdicts using
MeTTa's match for graph queries and Python for control flow.

Rule cascade mirrors relevance_evaluator.py (pure Python) exactly:
  1. STOP_STALE       - no direct goals or all direct goals achieved/cancelled
  2. BLOCKED           - blocked by constraint (incoming blocks edge)
  3. PAUSE_RECOVERABLY - holds exclusive resource needed by higher-priority task
  4. DEFER             - premature hardening on early-stage research
  5. REPLAN            - parent goal superseded (status=superseded + supersedes edge)
  6. ESCALATE          - multiple active goals with no recorded results
  7. CONTINUE          - healthy
"""

from __future__ import annotations
import sys
from pathlib import Path

try:
    from hyperon import MeTTa
except ImportError:
    print("ERROR: hyperon package not found.", file=sys.stderr)
    sys.exit(1)


class MeTTaEvaluator:
    """Evaluates task relevance verdicts using a MeTTa atomspace."""

    VERDICTS = (
        "STOP_STALE", "BLOCKED", "PAUSE_RECOVERABLY", "DEFER",
        "REPLAN", "ESCALATE", "CONTINUE",
    )

    INACTIVE_STATUSES = ("achieved", "cancelled")

    def __init__(self, metta_file=None):
        self.metta = MeTTa()
        self._setup_types()
        if metta_file:
            self.load(metta_file)

    def _setup_types(self):
        self.metta.run(
            '(: Goal Concept)\n'
            '(: Task Concept)\n'
            '(: Resource Concept)\n'
            '(: Constraint Concept)\n'
            '(: Project Concept)\n'
            '(: Result Concept)\n'
        )

    def load(self, path):
        self.metta.run(Path(path).read_text())

    def load_string(self, code):
        self.metta.run(code)

    def _flatten(self, results):
        out = []
        for r in results:
            if isinstance(r, list):
                out.extend(r)
            else:
                out.append(r)
        return out

    def _match(self, pattern):
        return [str(x) for x in self._flatten(
            self.metta.run(f"!(match &self {pattern})"))]

    # --- Domain queries ---

    def get_direct_goals(self, task_id):
        return self._match(f"(contributes_to {task_id} $goal) $goal")

    def get_goal_status(self, goal_id):
        results = self._match(
            f"({goal_id} $title $level $status $rank $urg) $status")
        return results[0] if results else None

    def get_goal_info(self, goal_id):
        results = self._match(
            f"({goal_id} $title $level $status $rank $urg) "
            f"($title $level $status $rank $urg)")
        if results and len(results) >= 5:
            return {
                "title": results[0].strip('"'),
                "level": results[1],
                "status": results[2],
                "rank": results[3],
                "urgency": results[4],
            }
        return None

    def get_task_info(self, task_id):
        results = self._match(
            f"({task_id} $title $status $rev) ($title $status $rev)")
        if results and len(results) >= 3:
            return {
                "title": results[0].strip('"'),
                "status": results[1],
                "reversibility": results[2],
            }
        return None

    def get_blocking_constraints(self, task_id):
        return self._match(f"(blocks $constraint {task_id}) $constraint")

    def get_superseding_goals(self, goal_id):
        return self._match(f"(supersedes $new {goal_id}) $new")

    def get_held_resources(self, task_id):
        return self._match(f"(holds {task_id} $res) $res")

    def get_resource_info(self, res_id):
        results = self._match(
            f"({res_id} $kind $excl $status) ($kind $excl $status)")
        if results and len(results) >= 3:
            return {
                "kind": results[0],
                "exclusivity": results[1],
                "status": results[2],
            }
        return None

    def get_resource_holders(self, res_id):
        return self._match(f"(holds $task {res_id}) $task")

    def get_project_for_task(self, task_id):
        results = self._match(f"(part_of {task_id} $proj) $proj")
        return results[0] if results else None

    def get_project_info(self, proj_id):
        results = self._match(
            f"({proj_id} $kind $stage) ($kind $stage)")
        if results and len(results) >= 2:
            return {"kind": results[0], "stage": results[1]}
        return None

    def has_results_for_goal(self, goal_id):
        results = self._match(
            f"(provides_evidence_for $result {goal_id}) $result")
        return bool(results)

    # --- Verdict cascade ---

    def evaluate(self, task_id):
        # Rule 1: STOP_STALE
        direct_goals = self.get_direct_goals(task_id)
        if not direct_goals:
            return "STOP_STALE"
        all_inactive = all(
            self.get_goal_status(g) in self.INACTIVE_STATUSES
            for g in direct_goals)
        if all_inactive:
            return "STOP_STALE"

        active_goals = [g for g in direct_goals
                        if self.get_goal_status(g) == "active"]

        # Rule 2: BLOCKED
        blockers = self.get_blocking_constraints(task_id)
        if blockers:
            return "BLOCKED"

        # Rule 3: PAUSE_RECOVERABLY
        held = self.get_held_resources(task_id)
        task_info = self.get_task_info(task_id)
        for res_id in held:
            res = self.get_resource_info(res_id)
            if not res or res.get("exclusivity") != "exclusive":
                continue
            holders = self.get_resource_holders(res_id)
            for holder_id in holders:
                if holder_id == task_id:
                    continue
                holder_goals = self.get_direct_goals(holder_id)
                for hg_id in holder_goals:
                    hg = self.get_goal_info(hg_id)
                    if not hg or hg["status"] != "active":
                        continue
                    for tg_id in active_goals:
                        tg = self.get_goal_info(tg_id)
                        if not tg:
                            continue
                        hg_rank = int(hg.get("rank", 999))
                        tg_rank = int(tg.get("rank", 999))
                        if hg_rank < tg_rank and \
                           task_info and task_info["reversibility"] == "checkpointable":
                            return "PAUSE_RECOVERABLY"

        # Rule 4: DEFER
        proj_id = self.get_project_for_task(task_id)
        if proj_id:
            proj = self.get_project_info(proj_id)
            if proj:
                kind = proj.get("kind", "")
                stage = proj.get("stage", "")
                if kind in ("exploratory_research", "confirmatory_research") \
                   and stage in ("E0_exploration", "E1_signal_validation"):
                    if task_info and task_info["reversibility"] == "irreversible":
                        return "DEFER"

        # Rule 5: REPLAN
        for g in direct_goals:
            status = self.get_goal_status(g)
            if status == "superseded":
                superseding = self.get_superseding_goals(g)
                if superseding:
                    return "REPLAN"

        # Rule 6: ESCALATE
        if active_goals and len(active_goals) > 1:
            has_results = any(self.has_results_for_goal(g) for g in active_goals)
            if not has_results:
                if task_info and task_info["status"] == "active":
                    return "ESCALATE"

        # Rule 7: CONTINUE
        return "CONTINUE"

    def evaluate_all(self):
        tasks = self._match("(: $t Task) $t")
        return {t: self.evaluate(t) for t in tasks}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <metta_file.metta> [task_id ...]")
        sys.exit(1)
    evaluator = MeTTaEvaluator(sys.argv[1])
    if len(sys.argv) > 2:
        for task_id in sys.argv[2:]:
            print(f"{task_id}: {evaluator.evaluate(task_id)}")
    else:
        for task_id, verdict in sorted(evaluator.evaluate_all().items()):
            print(f"{task_id}: {verdict}")
