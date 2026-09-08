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

import sys
from pathlib import Path
from pln_propagation import normalize_status

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
        """Load a MeTTa schema from a file path."""
        self.metta.run(Path(path).read_text())

    def load_string(self, code):
        """Load a MeTTa schema from a string."""
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
        """Return direct goal ids for a task."""
        return self._match(f"(contributes_to {task_id} $goal) $goal")

    def get_goal_status(self, goal_id):
        """Return the status of a goal."""
        results = self._match(
            f"({goal_id} $title $level $status $rank $urg) $status")
        return results[0] if results else None

    def get_goal_info(self, goal_id):
        """Return full info dict for a goal."""
        title = self._match(f"({goal_id} $t $l $s $r $u) $t")
        if not title:
            return None
        level = self._match(f"({goal_id} $t $l $s $r $u) $l")
        status = self._match(f"({goal_id} $t $l $s $r $u) $s")
        rank = self._match(f"({goal_id} $t $l $s $r $u) $r")
        urg = self._match(f"({goal_id} $t $l $s $r $u) $u")
        if title and status:
            return {
                "title": title[0].strip('"'),
                "level": level[0] if level else None,
                "status": status[0],
                "rank": rank[0] if rank else None,
                "urgency": urg[0] if urg else None,
            }
        return None

    def get_task_info(self, task_id):
        """Return full info dict for a task."""
        title = self._match(f"({task_id} $t $s $r) $t")
        if not title:
            return None
        status = self._match(f"({task_id} $t $s $r) $s")
        rev = self._match(f"({task_id} $t $s $r) $r")
        if title and status:
            return {
                "title": title[0].strip('"'),
                "status": status[0],
                "reversibility": rev[0] if rev else None,
            }
        return None

    def get_blocking_constraints(self, task_id):
        """Return constraints blocking a task."""
        return self._match(f"(blocks $constraint {task_id}) $constraint")

    def get_superseding_goals(self, goal_id):
        """Return goals that supersede the given goal."""
        return self._match(f"(supersedes $new {goal_id}) $new")

    def get_held_resources(self, task_id):
        """get_held_resources."""
        return self._match(f"(holds {task_id} $res) $res")

    def get_resource_info(self, res_id):
        """Return full info dict for a resource."""
        kind = self._match(f"({res_id} $k $e $s) $k")
        if not kind:
            return None
        excl = self._match(f"({res_id} $k $e $s) $e")
        status = self._match(f"({res_id} $k $e $s) $s")
        if kind:
            return {
                "kind": kind[0],
                "exclusivity": excl[0] if excl else None,
                "status": status[0] if status else None,
            }
        return None

    def get_resource_holders(self, res_id):
        """Return tasks holding a given resource."""
        return self._match(f"(holds $task {res_id}) $task")

    def get_project_for_task(self, task_id):
        """Return the project node for a task, if any."""
        results = self._match(f"(part_of {task_id} $proj) $proj")
        return results[0] if results else None

    def get_project_info(self, proj_id):
        """Return full info dict for a project."""
        kind = self._match(f"({proj_id} $k $s) $k")
        if not kind:
            return None
        stage = self._match(f"({proj_id} $k $s) $s")
        if kind:
            return {"kind": kind[0], "stage": stage[0] if stage else None}
        return None

    def has_results_for_goal(self, goal_id):
        """Check if any results are linked to a goal."""
        results = self._match(
            f"(provides_evidence_for $result {goal_id}) $result")
        return bool(results)

    # --- Verdict cascade ---

    def evaluate(self, task_id):
        """Evaluate the graph and return results."""
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
                        if normalize_status(self.get_goal_status(g) or "active") == "active"]

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
                    if not hg or normalize_status(hg.get("status", "active")) != "active":
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
            if normalize_status(status or "active") == "superseded":
                superseding = self.get_superseding_goals(g)
                if superseding:
                    return "REPLAN"

        # Rule 6: ESCALATE
        if active_goals and len(active_goals) > 1:
            has_results = any(self.has_results_for_goal(g) for g in active_goals)
            if not has_results:
                if task_info and normalize_status(task_info.get("status", "active")) == "active":
                    return "ESCALATE"

        # Rule 7: CONTINUE
        return "CONTINUE"

    def evaluate_all(self):
        """Evaluate all active tasks and return a list of Verdicts."""
        tasks = self._match("(: $t Task) $t")
        return {t: self.evaluate(t) for t in tasks}


    def evaluate_with_truth(self, task_id):
        """Evaluate a task and return (verdict, TruthValue)."""
        from pln_truth_mapping import verdict_to_truth
        verdict = self.evaluate(task_id)
        return verdict, verdict_to_truth(verdict)

    def evaluate_all_with_truth(self):
        """Evaluate all tasks and return {task_id: (verdict, TruthValue)}."""
        from pln_truth_mapping import verdict_to_truth
        tasks = self._match("(: $t Task) $t")
        return {t: (self.evaluate(t), verdict_to_truth(self.evaluate(t)))
                for t in tasks}


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
