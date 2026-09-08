#!/usr/bin/env python3
"""Graph-to-Atomspace Mapper: translates Goal Relevance Graph v0.1 JSON into
MeTTa atomspace declarations suitable for PLN-style inference.

The mapping is exploratory — it does not yet execute inside a MeTTa runtime.
Instead it generates MeTTa source text that can be loaded into a MeTTa
interpreter (e.g. hyperon-experimental) once one is available in this
environment.  The Python-side tests verify that the generated atomspace
faithfully represents the original graph and that verdict rules expressed
in MeTTa-style match the Python evaluator's verdicts.

Node mapping:
  goal  G{id}        -> (Goal id title level status rank urgency)
  project P{id}     -> (Project id title project_kind maturity_stage)
  task  T{id}       -> (Task id title status reversibility)
  resource R{id}   -> (Resource id title resource_type exclusive)
  result R{id}     -> (Result id title)
  constraint C{id} -> (Constraint id title)

Edge mapping (relation atoms):
  (contributes_to {from} {to})
  (part_of {from} {to})
  (occupies {from} {to})
  (blocks {from} {to})
  (supersedes {from} {to})
  (provides_evidence_for {from} {to})

Verdict atoms:
  (verdict {task_id} {VERDICT})
"""

import json
import re
from pln_propagation import normalize_status


# --- Helpers ---

def _atom_id(raw_id: str) -> str:
    """Sanitize an ID for use as a MeTTa symbol."""
    return raw_id.replace("-", "_").replace(".", "_")


PREFIX_BY_TYPE = {
    "goal": "g",
    "project": "p",
    "task": "t",
    "resource": "r",
    "result": "res",
    "constraint": "c",
}


def _prefixed_atom_id(raw_id: str, node_type: str) -> str:
    """Build a prefixed MeTTa atom ID matching the node encoder convention."""
    prefix = PREFIX_BY_TYPE.get(node_type, "x")
    return f"{prefix}_{_atom_id(raw_id)}"


# --- Node encoders ---

def encode_goal(node: dict) -> str:
    gid = _atom_id(node["id"])
    title = node.get("title", "")
    level = node.get("level", "intermediate")
    status = normalize_status(node.get("status", "active"))
    rank = node.get("priority", {}).get("rank", 999)
    urgency = node.get("priority", {}).get("urgency", "medium")
    return (
        f'(: g_{gid} Goal)\n'
        f'(g_{gid} "{title}" {level} {status} {rank} {urgency})'
    )


def encode_project(node: dict) -> str:
    pid = _atom_id(node["id"])
    title = node.get("title", "")
    rc = node.get("result_contract", {})
    kind = rc.get("project_kind", "")
    stage = rc.get("maturity_stage", "")
    return (
        f'(: p_{pid} Project)\n'
        f'(p_{pid} "{title}" {kind} {stage})'
    )


def encode_task(node: dict) -> str:
    tid = _atom_id(node["id"])
    title = node.get("title", "")
    status = normalize_status(node.get("status", "active"))
    rev = node.get("reversibility", "reversible")
    return (
        f'(: t_{tid} Task)\n'
        f'(t_{tid} "{title}" {status} {rev})'
    )


def encode_resource(node: dict) -> str:
    rid = _atom_id(node["id"])
    title = node.get("title", "")
    rtype = node.get("resource_type", "process")
    exclusive = "True" if node.get("exclusive", False) else "False"
    return (
        f'(: r_{rid} Resource)\n'
        f'(r_{rid} "{title}" {rtype} {exclusive})'
    )


def encode_result(node: dict) -> str:
    rid = _atom_id(node["id"])
    title = node.get("title", node["id"])
    return f'(: res_{rid} Result)\n(res_{rid} "{title}")'


def encode_constraint(node: dict) -> str:
    cid = _atom_id(node["id"])
    title = node.get("title", node["id"])
    return f'(: c_{cid} Constraint)\n(c_{cid} "{title}")'


NODE_ENCODERS = {
    "goal": encode_goal,
    "project": encode_project,
    "task": encode_task,
    "resource": encode_resource,
    "result": encode_result,
    "constraint": encode_constraint,
}


def encode_edge(edge: dict, node_lookup: dict | None = None) -> str:
    """Encode an edge as a MeTTa relation atom.

    If node_lookup is provided (mapping raw_id -> node dict with 'kind'),
    the from/to IDs are prefixed to match the node encoder convention.
    """
    frm_raw = edge["from"]
    to_raw = edge["to"]
    rel = edge["relation"]
    if node_lookup is not None:
        frm_type = node_lookup.get(frm_raw, {}).get("kind")
        to_type = node_lookup.get(to_raw, {}).get("kind")
        frm = _prefixed_atom_id(frm_raw, frm_type) if frm_type else _atom_id(frm_raw)
        to = _prefixed_atom_id(to_raw, to_type) if to_type else _atom_id(to_raw)
    else:
        frm = _atom_id(frm_raw)
        to = _atom_id(to_raw)
    return f"({rel} {frm} {to})"


# --- Graph -> MeTTa source ---

def graph_to_metta(data: dict) -> str:
    """Convert a Goal Relevance Graph JSON into MeTTa source text."""
    lines: list[str] = []
    lines.append(f";; Goal Relevance Graph -> MeTTa Atomspace")
    lines.append(f";; schema_version={data.get('schema_version', '?')}")
    lines.append(f";; as_of={data.get('as_of', '?')}")
    lines.append("")

    # Type declarations
    lines.append(";; -- Type definitions --")
    lines.append("(: Goal Concept)")
    lines.append("(: Project Concept)")
    lines.append("(: Task Concept)")
    lines.append("(: Resource Concept)")
    lines.append("(: Result Concept)")
    lines.append("(: Constraint Concept)")
    lines.append("(: Verdict Concept)")
    lines.append("")

    # Nodes
    lines.append(";; -- Nodes --")
    for key in ("goals", "projects", "tasks", "resources", "results", "constraints"):
        for node in data.get(key, []):
            kind = node.get("kind", key.rstrip("s"))
            encoder = NODE_ENCODERS.get(kind)
            if encoder:
                lines.append(encoder(node))
    lines.append("")

    # Build node lookup for edge encoding
    node_lookup: dict[str, dict] = {}
    for key in ("goals", "projects", "tasks", "resources", "results", "constraints"):
        for node in data.get(key, []):
            node_lookup[node["id"]] = node

    # Edges
    lines.append(";; -- Edges --")
    for edge in data.get("edges", []):
        lines.append(encode_edge(edge, node_lookup))
    lines.append("")

    # Verdict rules
    lines.append(";; -- Verdict rules (declarative, not yet executed) --")
    lines.append(VERDICT_RULES_METTA)

    return "\n".join(lines)


# --- MeTTa verdict rules (reference) ---

VERDICT_RULES_METTA = r"""
;; Rule 1: STOP_STALE -- task has no active parent goal
(= (check_stop_stale $task)
   (let $goals (direct_goals $task)
        (if (== $goals ())
            (verdict $task STOP_STALE)
            (if (all_inactive $goals)
                (verdict $task STOP_STALE)
                (empty)))))

;; Rule 2: BLOCKED -- constraint blocks task
(= (check_blocked $task)
   (let $blockers (blocking_constraints $task)
        (if (not (== $blockers ()))
            (verdict $task BLOCKED)
            (empty))))

;; Rule 3: PAUSE_RECOVERABLY -- holds exclusive resource needed by higher-priority task
(= (check_pause_recoverably $task)
   (let $resources (occupied_exclusive_resources $task)
        (let $holders (resource_holders $resources)
             (if (any_higher_priority $holders $task)
                 (if (is_checkpointable $task)
                     (verdict $task PAUSE_RECOVERABLY)
                     (empty))
                 (empty)))))

;; Rule 4: DEFER -- premature irreversible hardening on early-stage research
(= (check_defer $task)
   (let $project (project_of $task)
        (if (and (is_exploratory $project)
                 (is_early_stage $project)
                 (is_irreversible $task))
            (verdict $task DEFER)
            (empty))))

;; Rule 5: REPLAN -- parent goal superseded
(= (check_replan $task)
   (let $goals (transitive_goals $task)
        (if (any_superseded $goals)
            (verdict $task REPLAN)
            (empty))))

;; Rule 6: ESCALATE -- multiple active goals, no evidence
(= (check_escalate $task)
   (let $goals (active_goals $task)
        (if (and (> (length $goals) 1)
                 (not (has_evidence $task))
                 (is_active $task))
            (verdict $task ESCALATE)
            (empty))))

;; Default: CONTINUE
(= (evaluate_task $task)
   (superpose
    ((check_stop_stale $task)
     (check_blocked $task)
     (check_pause_recoverably $task)
     (check_defer $task)
     (check_replan $task)
     (check_escalate $task)
     (verdict $task CONTINUE))))
"""


# --- Round-trip: MeTTa -> internal Python graph ---

KNOWN_RELATIONS = frozenset({
    "contributes_to", "part_of", "occupies",
    "blocks", "supersedes", "provides_evidence_for",
})


def metta_to_edges(metta_src: str) -> list[dict]:
    """Extract edge atoms from generated MeTTa source.
    Returns list of {from, to, relation} dicts (atom-style ids)."""
    edges: list[dict] = []
    for line in metta_src.splitlines():
        line = line.strip()
        if line.startswith(";;") or line.startswith("(:") or not line:
            continue
        m = re.match(r"\((\w+)\s+(\w+)\s+(\w+)\)$", line)
        if m:
            rel, frm, to = m.group(1), m.group(2), m.group(3)
            if rel in KNOWN_RELATIONS:
                edges.append({"from": frm, "to": to, "relation": rel})
    return edges


def _decode_atom_id(atom_id: str) -> str:
    """Reverse _atom_id for the prefix-removed portion (best-effort)."""
    # Just return as-is; the round-trip test uses atom-style ids
    return atom_id


def count_metta_nodes(metta_src: str) -> dict[str, int]:
    """Count type declarations by kind from MeTTa source."""
    counts = {"goal": 0, "project": 0, "task": 0,
              "resource": 0, "result": 0, "constraint": 0}
    for line in metta_src.splitlines():
        m = re.match(r"^\(:\s+\w+\s+(Goal|Project|Task|Resource|Result|Constraint)\)$",
                      line.strip())
        if m:
            kind = m.group(1).lower()
            counts[kind] = counts.get(kind, 0) + 1
    return counts


if __name__ == "__main__":
    import sys
    data = json.load(open(sys.argv[1]))
    print(graph_to_metta(data))
