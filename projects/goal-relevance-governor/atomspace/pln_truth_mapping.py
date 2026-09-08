"""
PLN Truth-Value Mapping for GRG Atomspace v0.1 (Exploratory)

Maps GRG graph nodes and edges to PLN (Probabilistic Logic Networks)
truth values (strength, confidence) for integration with OpenCog AtomSpace.
"""

from __future__ import annotations
from dataclasses import dataclass
import json


@dataclass
class TruthValue:
    strength: float = 1.0
    confidence: float = 1.0

    def to_dict(self):
        return {"strength": self.strength, "confidence": self.confidence}

    @classmethod
    def from_dict(cls, d):
        return cls(d["strength"], d["confidence"])

    def __repr__(self):
        return f"TV({self.strength:.2f}, {self.confidence:.2f})"


STATUS_TRUTH = {
    "active":     TruthValue(1.0, 0.9),
    "achieved":   TruthValue(1.0, 1.0),
    "cancelled":  TruthValue(0.0, 1.0),
    "abandoned":  TruthValue(0.0, 1.0),
    "superseded": TruthValue(0.0, 0.8),
    "blocked":    TruthValue(0.3, 0.8),
    "completed":  TruthValue(1.0, 1.0),
    "occupied":   TruthValue(0.8, 0.9),
    "unknown":    TruthValue(0.5, 0.5),
}

EDGE_TRUTH = {
    "contributes_to": TruthValue(1.0, 0.9),
    "supersedes":     TruthValue(0.0, 0.8),
    "blocks":         TruthValue(0.0, 0.9),
    "holds":          TruthValue(1.0, 0.9),
    "depends_on":     TruthValue(1.0, 0.8),
    "occupies":       TruthValue(1.0, 0.9),
    "part_of":        TruthValue(1.0, 0.9),
}

VERDICT_TRUTH = {
    "STOP_STALE":        TruthValue(0.0, 0.95),
    "BLOCKED":           TruthValue(0.3, 0.8),
    "PAUSE_RECOVERABLY": TruthValue(0.5, 0.7),
    "DEFER":             TruthValue(0.4, 0.7),
    "REPLAN":            TruthValue(0.6, 0.8),
    "ESCALATE":          TruthValue(0.7, 0.6),
    "CONTINUE":          TruthValue(1.0, 0.9),
}


def status_to_truth(status):
    return STATUS_TRUTH.get(status, STATUS_TRUTH["unknown"])

def edge_to_truth(relation):
    return EDGE_TRUTH.get(relation, TruthValue(0.5, 0.5))

def verdict_to_truth(verdict):
    return VERDICT_TRUTH.get(verdict, TruthValue(0.5, 0.5))

def pln_and(tv1, tv2):
    return TruthValue(min(tv1.strength, tv2.strength),
                      tv1.confidence * tv2.confidence)

def pln_or(tv1, tv2):
    return TruthValue(max(tv1.strength, tv2.strength),
                      max(tv1.confidence, tv2.confidence))

def pln_not(tv):
    return TruthValue(1.0 - tv.strength, tv.confidence)


def graph_to_pln_atoms(graph):
    atoms = []
    for goal in graph.get("goals", []):
        atoms.append({
            "atom_type": "ConceptNode",
            "name": goal["id"],
            "truth": status_to_truth(goal.get("status", "unknown")).to_dict(),
            "outgoing": [],
        })
    for task in graph.get("tasks", []):
        atoms.append({
            "atom_type": "ConceptNode",
            "name": task["id"],
            "truth": status_to_truth(task.get("status", "active")).to_dict(),
            "outgoing": [],
        })
    for res in graph.get("resources", []) + graph.get("constraints", []):
        atoms.append({
            "atom_type": "ConceptNode",
            "name": res["id"],
            "truth": status_to_truth(res.get("status", "unknown")).to_dict(),
            "outgoing": [],
        })
    for edge in graph.get("edges", []):
        relation = edge.get("relation", "unknown")
        atoms.append({
            "atom_type": "EvaluationLink",
            "name": f"{relation}_{edge['from']}_to_{edge['to']}",
            "truth": edge_to_truth(relation).to_dict(),
            "outgoing": [edge["from"], edge["to"]],
        })
    return atoms


def export_pln_json(graph, output_path=None):
    atoms = graph_to_pln_atoms(graph)
    result = {
        "format": "PLN-AtomSpace-JSON-v0.1",
        "atoms": atoms,
        "truth_value_type": "SimpleTruthValue",
    }
    s = json.dumps(result, indent=2)
    if output_path:
        with open(output_path, "w") as f:
            f.write(s)
    return s


def compute_task_relevance(graph, task_id):
    edges = [e for e in graph.get("edges", [])
             if e["from"] == task_id and e.get("relation") == "contributes_to"]
    if not edges:
        return TruthValue(0.0, 0.9)
    goals_by_id = {g["id"]: g for g in graph.get("goals", [])}
    combined = TruthValue(0.0, 0.0)
    for edge in edges:
        goal = goals_by_id.get(edge["to"])
        if not goal:
            continue
        goal_tv = status_to_truth(goal.get("status", "unknown"))
        edge_tv = edge_to_truth("contributes_to")
        goal_relevance = pln_and(goal_tv, edge_tv)
        combined = pln_or(combined, goal_relevance)
    return combined if combined.confidence > 0 else TruthValue(0.5, 0.5)
