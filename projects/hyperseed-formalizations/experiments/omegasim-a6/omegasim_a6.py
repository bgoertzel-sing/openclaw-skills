"""OmegaSim A6: single-hive role-coupled motivational model.

This is a compact, inspectable reference implementation for the first A6
experiment proposed in the 2026-07-01 OmegaSim feedback.  It intentionally
models logistic response as bounded thresholded cognitive appraisal rather than
as arbitrary chaos injection.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Dict, List, Tuple

import numpy as np

try:  # allow both package-style and script-dir imports
    from conditions import Condition, get_condition
except ImportError:  # pragma: no cover
    from .conditions import Condition, get_condition

ROLES = [
    "explorer", "synthesizer", "formalizer", "implementer", "reviewer",
    "coordinator", "maintainer", "communicator",
]
STATE_VARS = [
    "activation", "arousal", "focus", "resolution", "risk_sensitivity",
    "novelty_appetite", "fatigue", "threshold",
]
ACTIONS = [
    "explore", "message", "create_task", "work_task", "synthesize", "review",
    "formalize", "delegate", "predict", "escalate", "maintain", "pause",
]
APPRAISALS = [
    "semantic_novelty", "artifact_readiness", "unresolved_contradiction",
    "proof_failure_burst", "review_criticism", "risk_signal",
    "trust_weighted_import", "prediction_error",
]
FIELD_DIMS = [
    "research_novelty", "theorem_proof_salience", "implementation_salience",
    "external_comm_salience", "risk_provenance_debt", "synthesis_coherence",
    "contradiction_tension", "maintenance_entropy",
]

ROLE_TO_ACTION = {
    "explorer": ["explore", "create_task", "message", "pause"],
    "synthesizer": ["synthesize", "review", "message", "predict"],
    "formalizer": ["formalize", "review", "predict", "pause"],
    "implementer": ["work_task", "create_task", "maintain", "pause"],
    "reviewer": ["review", "escalate", "message", "pause"],
    "coordinator": ["delegate", "message", "predict", "escalate"],
    "maintainer": ["maintain", "review", "work_task", "pause"],
    "communicator": ["message", "synthesize", "escalate", "pause"],
}


def sigmoid(x: np.ndarray | float) -> np.ndarray | float:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -60, 60)))


def softmax(x: np.ndarray, temperature: float = 1.0) -> np.ndarray:
    z = (x - np.max(x)) / max(temperature, 1e-6)
    e = np.exp(np.clip(z, -60, 60))
    return e / np.sum(e)


def inverted_u(n: np.ndarray, k: float, theta_low: float = 0.25, theta_high: float = 0.82) -> np.ndarray:
    return sigmoid(k * (n - theta_low)) * (1.0 - sigmoid(k * (n - theta_high)))


@dataclass
class SimConfig:
    condition_id: int = 5
    timesteps: int = 300
    seed: int = 7
    field_dim: int = 8
    coupling_slope_k: float = 2.0
    threshold_percentile_theta: float = 50.0
    delay_tau: int | None = None
    memory_rho: float | None = None
    fatigue_gain: float = 0.03
    prediction_cost: float = 0.03
    noise: float = 0.03
    coupling_gain: float = 0.35
    field_leak: float = 0.08
    role_decay: float = 0.05
    temperature: float = 0.28


class OmegaSimA6:
    def __init__(self, config: SimConfig, condition: Condition | None = None):
        self.config = config
        self.condition = condition or get_condition(config.condition_id)
        if config.delay_tau is not None:
            self.condition = get_condition(config.condition_id, delay_tau=config.delay_tau)
        if config.memory_rho is not None:
            self.condition = get_condition(config.condition_id, hysteresis_rho=config.memory_rho)
        self.rng = np.random.default_rng(config.seed)
        self.n_roles = len(ROLES)
        self.n_state = len(STATE_VARS)
        self.n_actions = len(ACTIONS)
        self.n_app = len(APPRAISALS)
        self.n_field = len(FIELD_DIMS)
        self.state = self._initial_state()
        self.field = self.rng.uniform(0.25, 0.55, size=self.n_field)
        self.hysteresis = np.zeros((self.n_roles, self.n_actions))
        self.artifact = np.array([0.30, 0.25, 0.45])  # maturity, utility, queue health
        self.trust = np.full(self.n_roles, 0.62)
        self.budget = 1.0
        self.pred_queue: List[Tuple[int, np.ndarray]] = []
        self.history_states = [self.state.copy()]
        self.history_fields = [self.field.copy()]

    def _initial_state(self) -> np.ndarray:
        s = self.rng.uniform(0.2, 0.7, size=(len(ROLES), len(STATE_VARS)))
        s[:, STATE_VARS.index("fatigue")] = self.rng.uniform(0.05, 0.2, size=len(ROLES))
        base_threshold = np.percentile(s[:, :6], self.config.threshold_percentile_theta)
        s[:, STATE_VARS.index("threshold")] = np.clip(base_threshold + self.rng.normal(0, 0.04, len(ROLES)), 0.1, 0.9)
        return s

    def _delayed_state(self) -> np.ndarray:
        tau = max(0, int(self.condition.delay_tau))
        idx = max(0, len(self.history_states) - 1 - tau)
        return self.history_states[idx]

    def _appraisals(self, delayed: np.ndarray) -> np.ndarray:
        f = self.field
        a = np.zeros((self.n_roles, self.n_app))
        semantic_novelty = f[FIELD_DIMS.index("research_novelty")]
        artifact_ready = np.clip(0.55 * self.artifact[0] + 0.45 * f[FIELD_DIMS.index("synthesis_coherence")] - 0.25 * f[FIELD_DIMS.index("risk_provenance_debt")], 0, 1)
        contradiction = f[FIELD_DIMS.index("contradiction_tension")]
        proof_failure = np.clip(f[FIELD_DIMS.index("theorem_proof_salience")] * contradiction, 0, 1)
        criticism = np.clip(0.55 * contradiction + 0.35 * (1 - self.artifact[1]), 0, 1)
        risk = f[FIELD_DIMS.index("risk_provenance_debt")]
        import_signal = np.clip(np.mean(self.trust) * (0.4 + 0.6 * f[FIELD_DIMS.index("external_comm_salience")]), 0, 1)
        pred_error = self._consume_predictions()
        base = np.array([semantic_novelty, artifact_ready, contradiction, proof_failure, criticism, risk, import_signal, pred_error])
        for i in range(self.n_roles):
            role_bias = np.zeros(self.n_app)
            role = ROLES[i]
            if role == "explorer": role_bias[0] += 0.18
            if role == "formalizer": role_bias[3] += 0.18
            if role == "implementer": role_bias[1] += 0.12
            if role == "reviewer": role_bias[4] += 0.16
            if role == "maintainer": role_bias[5] += 0.12
            if role == "communicator": role_bias[6] += 0.14
            fatigue = delayed[i, STATE_VARS.index("fatigue")]
            appetite = delayed[i, STATE_VARS.index("novelty_appetite")]
            a[i] = np.clip(base + role_bias + self.config.noise * self.rng.normal(size=self.n_app) - 0.12 * fatigue + 0.05 * appetite, 0, 1)
        return a

    def _consume_predictions(self) -> float:
        if not self.pred_queue:
            return 0.25
        remaining = []
        errors = []
        for due, forecast in self.pred_queue:
            if due <= len(self.history_fields):
                errors.append(float(np.mean(np.abs(self.field - forecast))))
            else:
                remaining.append((due, forecast))
        self.pred_queue = remaining
        return float(np.clip(np.mean(errors) if errors else 0.25, 0, 1))

    def _utilities(self, app: np.ndarray, delayed: np.ndarray) -> np.ndarray:
        k = self.condition.logistic_slope if self.condition.coupling_mode == "logistic" else 1.0
        u = np.full((self.n_roles, self.n_actions), -0.6)
        for i, role in enumerate(ROLES):
            st = delayed[i]
            thr = st[STATE_VARS.index("threshold")]
            gate = sigmoid(k * (app[i] - thr))
            novelty_curve = inverted_u(app[i, 0], max(k, 0.01))
            activation, arousal, focus, resolution, risk_sens, novelty_app, fatigue, _ = st
            vals = {name: -0.4 for name in ACTIONS}
            vals["explore"] = 1.1 * gate[0] + 0.5 * novelty_curve + novelty_app - 0.6 * fatigue
            vals["message"] = 0.7 * gate[6] + 0.35 * gate[2] + 0.25 * arousal
            vals["create_task"] = 0.8 * gate[0] + 0.5 * gate[2] - 0.25 * fatigue
            vals["work_task"] = 1.0 * gate[1] + 0.4 * focus + 0.25 * resolution - 0.45 * fatigue
            vals["synthesize"] = 0.8 * gate[0] + 0.85 * gate[1] + 0.5 * self.field[5]
            vals["review"] = 0.9 * gate[1] + 0.85 * gate[4] + 0.2 * risk_sens
            vals["formalize"] = 1.1 * gate[3] + 0.45 * focus + 0.2 * resolution
            vals["delegate"] = 0.7 * gate[2] + 0.5 * gate[6] + 0.25 * activation
            vals["predict"] = 0.9 * gate[7] + 0.35 * arousal - self.config.prediction_cost * self.condition.costly_prediction
            vals["escalate"] = 0.75 * gate[5] + 0.55 * gate[2] + 0.25 * arousal
            vals["maintain"] = 1.0 * sigmoid(k * (self.field[7] - thr)) + 0.45 * gate[5] - 0.2 * fatigue
            vals["pause"] = 0.9 * fatigue + 0.25 * risk_sens - 0.25 * activation
            for a_name in ROLE_TO_ACTION[role]:
                vals[a_name] += 0.28
            u[i] = np.array([vals[a] for a in ACTIONS])
        if self.condition.coupling_mode == "linear":
            u += self.config.coupling_gain * (delayed[:, [0]] - delayed[:, [6]])
        elif self.condition.coupling_mode == "logistic":
            role_signal = sigmoid(k * (delayed[:, STATE_VARS.index("activation")] - delayed[:, STATE_VARS.index("threshold")]))
            influence = role_signal.mean() - role_signal[:, None]
            u += self.config.coupling_gain * influence
        u += self.condition.hysteresis_rho * self.hysteresis
        return u

    def step(self) -> Dict:
        delayed = self._delayed_state()
        app = self._appraisals(delayed)
        utilities = self._utilities(app, delayed)
        action_idx = np.array([self.rng.choice(self.n_actions, p=softmax(utilities[i], self.config.temperature)) for i in range(self.n_roles)])
        action_counts = np.bincount(action_idx, minlength=self.n_actions).astype(float) / self.n_roles
        action_onehot = np.eye(self.n_actions)[action_idx]
        rho = self.condition.hysteresis_rho
        self.hysteresis = rho * self.hysteresis + (1 - rho) * action_onehot
        self._update_field(action_counts, app)
        self._update_artifact(action_counts)
        self._update_state(action_idx, app, action_counts)
        if self.condition.costly_prediction and np.any(action_idx == ACTIONS.index("predict")):
            self._schedule_prediction(action_counts)
        self.history_states.append(self.state.copy())
        self.history_fields.append(self.field.copy())
        return {
            "state": self.state.copy(), "field": self.field.copy(), "appraisals": app.copy(),
            "actions": action_idx.copy(), "action_counts": action_counts.copy(),
            "artifact": self.artifact.copy(), "trust": self.trust.copy(), "budget": self.budget,
        }

    def _update_field(self, c: np.ndarray, app: np.ndarray) -> None:
        delta = np.zeros(self.n_field)
        ai = {a: ACTIONS.index(a) for a in ACTIONS}
        delta[0] += 0.18 * c[ai["explore"]] + 0.05 * c[ai["create_task"]]
        delta[1] += 0.16 * c[ai["formalize"]] + 0.09 * c[ai["review"]]
        delta[2] += 0.18 * c[ai["work_task"]] + 0.08 * c[ai["maintain"]]
        delta[3] += 0.15 * c[ai["message"]] + 0.10 * c[ai["escalate"]]
        delta[4] += 0.13 * c[ai["escalate"]] + 0.08 * c[ai["explore"]] - 0.14 * c[ai["review"]] - 0.10 * c[ai["maintain"]]
        delta[5] += 0.18 * c[ai["synthesize"]] + 0.06 * c[ai["review"]]
        delta[6] += 0.14 * c[ai["create_task"]] + 0.12 * app[:, 2].mean() - 0.12 * c[ai["synthesize"]] - 0.10 * c[ai["formalize"]]
        delta[7] += 0.10 * c[ai["work_task"]] + 0.08 * c[ai["create_task"]] - 0.18 * c[ai["maintain"]] - 0.06 * c[ai["pause"]]
        self.field = np.clip((1 - self.config.field_leak) * self.field + delta + self.config.noise * self.rng.normal(size=self.n_field), 0, 1)

    def _update_artifact(self, c: np.ndarray) -> None:
        ai = {a: ACTIONS.index(a) for a in ACTIONS}
        novelty = self.field[0]
        coherence = self.field[5]
        risk = self.field[4]
        maturity_gain = 0.08 * c[ai["synthesize"]] + 0.10 * c[ai["formalize"]] + 0.11 * c[ai["work_task"]] + 0.06 * c[ai["review"]]
        utility_gain = 0.07 * c[ai["work_task"]] + 0.05 * c[ai["review"]] + 0.05 * inverted_u(np.array([novelty]), self.condition.logistic_slope)[0]
        queue_health = self.artifact[2] + 0.09 * c[ai["delegate"]] + 0.11 * c[ai["maintain"]] - 0.08 * c[ai["create_task"]] - 0.06 * self.field[7]
        self.artifact[0] = np.clip(0.96 * self.artifact[0] + maturity_gain + 0.04 * coherence - 0.05 * risk, 0, 1)
        self.artifact[1] = np.clip(0.97 * self.artifact[1] + utility_gain + 0.03 * coherence - 0.04 * risk, 0, 1)
        self.artifact[2] = np.clip(queue_health, 0, 1)

    def _update_state(self, action_idx: np.ndarray, app: np.ndarray, c: np.ndarray) -> None:
        new = self.state.copy()
        for i, aidx in enumerate(action_idx):
            a = ACTIONS[aidx]
            st = self.state[i]
            load = 0.35 * st[0] + 0.35 * st[1] + 0.30 * (1 - self.artifact[2])
            success = 0.5 * self.artifact[0] + 0.5 * self.artifact[1]
            new[i, 0] += 0.10 * (a != "pause") - 0.08 * (a == "pause") - self.config.role_decay * st[0]
            new[i, 1] += 0.10 * app[i, 7] + 0.08 * app[i, 2] - 0.05 * (a == "pause")
            new[i, 2] += 0.08 * (a in ["work_task", "formalize", "review", "synthesize"]) - 0.05 * app[i, 2]
            new[i, 3] += 0.09 * (a in ["formalize", "review", "maintain"]) + 0.04 * success - 0.04 * app[i, 3]
            new[i, 4] += 0.06 * app[i, 5] - 0.03 * self.trust[i]
            new[i, 5] += 0.06 * app[i, 0] - 0.05 * app[i, 5]
            new[i, 6] += self.config.fatigue_gain * load + 0.025 * (a != "pause") - 0.10 * (a == "pause")
            if self.condition.adaptive_thresholds:
                new[i, 7] += 0.05 * load + 0.04 * st[6] + 0.05 * app[i, 5] - 0.07 * success
            new[i] += self.config.noise * self.rng.normal(size=self.n_state)
        self.state = np.clip(new, 0, 1)
        self.trust = np.clip(0.98 * self.trust + 0.02 * self.artifact[1] - 0.015 * self.field[4], 0, 1)

    def _schedule_prediction(self, c: np.ndarray) -> None:
        self.budget = max(0.0, self.budget - self.config.prediction_cost * float(c[ACTIONS.index("predict")] > 0))
        forecast = np.clip(self.field + 0.5 * (self.field - self.history_fields[-1]), 0, 1)
        self.pred_queue.append((len(self.history_fields) + max(1, self.condition.delay_tau), forecast))

    def run(self) -> Dict[str, np.ndarray | List[List[str]] | dict]:
        records = [self.step() for _ in range(self.config.timesteps)]
        states = np.stack([r["state"] for r in records])
        fields = np.stack([r["field"] for r in records])
        appraisals = np.stack([r["appraisals"] for r in records])
        actions_idx = np.stack([r["actions"] for r in records])
        action_counts = np.stack([r["action_counts"] for r in records])
        artifacts = np.stack([r["artifact"] for r in records])
        trust = np.stack([r["trust"] for r in records])
        return {
            "states": states, "fields": fields, "appraisals": appraisals,
            "actions_idx": actions_idx, "actions": [[ACTIONS[j] for j in row] for row in actions_idx],
            "action_counts": action_counts, "artifacts": artifacts, "trust": trust,
            "budgets": np.array([r["budget"] for r in records]),
            "metadata": {"config": asdict(self.config), "condition": asdict(self.condition),
                         "roles": ROLES, "state_vars": STATE_VARS, "actions_set": ACTIONS,
                         "field_dims": FIELD_DIMS, "appraisals": APPRAISALS},
        }


def run_simulation(config: SimConfig) -> Dict:
    return OmegaSimA6(config).run()
