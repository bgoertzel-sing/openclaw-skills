"""Analysis pipeline for OmegaSim A6 outputs.

Implements lightweight versions of the feedback pipeline using numpy/scipy only:
collect latent vectors, residualize load/service/action variables, delay embed,
PCA, simple clustering fallback, lobe grammar, and recurrence/compression/
forecastability/recovery metrics. UMAP/HDBSCAN/HMM/diffusion maps can be added as
optional later controls without changing the saved observable format.
"""
from __future__ import annotations

import json
import zlib
from pathlib import Path
from typing import Dict

import numpy as np

try:
    from scipy.spatial.distance import pdist, squareform
except Exception:  # pragma: no cover
    pdist = squareform = None


def flatten_latents(result: Dict) -> np.ndarray:
    states = result["states"].reshape(result["states"].shape[0], -1)
    return np.concatenate([states, result["fields"], result["artifacts"], result["trust"], result["budgets"][:, None]], axis=1)


def build_observable(result: Dict) -> np.ndarray:
    """Primary observable Y_t before residualization.

    Y_t = [M_t, G_t, A_t, artifact_t, prediction_error_t, trust_t, fatigue_t,
           threshold_t, graph_features_t].
    """
    states = result["states"]
    fields = result["fields"]
    action_counts = result["action_counts"]
    artifacts = result["artifacts"]
    trust_mean = result["trust"].mean(axis=1, keepdims=True)
    fatigue = states[:, :, 6].mean(axis=1, keepdims=True)
    threshold = states[:, :, 7].mean(axis=1, keepdims=True)
    pred_error = result["appraisals"][:, :, 7].mean(axis=1, keepdims=True)
    # Simple graph/coordination proxies: action entropy and cross-role activation variance.
    p = np.clip(action_counts, 1e-12, 1)
    action_entropy = (-(p * np.log(p)).sum(axis=1, keepdims=True) / np.log(action_counts.shape[1]))
    activation_var = states[:, :, 0].var(axis=1, keepdims=True)
    graph_features = np.concatenate([action_entropy, activation_var], axis=1)
    return np.concatenate([fields, action_counts, artifacts, pred_error, trust_mean, fatigue, threshold, graph_features], axis=1)


def residualize(y: np.ndarray, controls: np.ndarray | None = None) -> np.ndarray:
    """Residualize Y against intercept, time, and optional controls."""
    t = np.linspace(-1, 1, len(y))[:, None]
    x = np.concatenate([np.ones_like(t), t], axis=1)
    if controls is not None:
        x = np.concatenate([x, controls], axis=1)
    beta, *_ = np.linalg.lstsq(x, y, rcond=None)
    return y - x @ beta


def delay_embed(x: np.ndarray, lags: int = 3, stride: int = 1) -> np.ndarray:
    if lags < 1:
        return x
    rows = []
    for i in range((lags - 1) * stride, len(x)):
        rows.append(np.concatenate([x[i - j * stride] for j in range(lags)]))
    return np.asarray(rows)


def pca(x: np.ndarray, n_components: int = 3) -> tuple[np.ndarray, np.ndarray]:
    xc = x - x.mean(axis=0, keepdims=True)
    u, s, vt = np.linalg.svd(xc, full_matrices=False)
    scores = u[:, :n_components] * s[:n_components]
    var = (s**2) / max(1, len(x) - 1)
    explained = var[:n_components] / max(var.sum(), 1e-12)
    return scores, explained


def cluster_lobes(scores: np.ndarray, n_lobes: int = 4, iterations: int = 40, seed: int = 0) -> np.ndarray:
    """Small deterministic k-means fallback standing in for HDBSCAN/HMM."""
    rng = np.random.default_rng(seed)
    if len(scores) < n_lobes:
        return np.zeros(len(scores), dtype=int)
    centers = scores[rng.choice(len(scores), n_lobes, replace=False)]
    labels = np.zeros(len(scores), dtype=int)
    for _ in range(iterations):
        d = ((scores[:, None, :] - centers[None, :, :]) ** 2).sum(axis=2)
        labels = d.argmin(axis=1)
        for k in range(n_lobes):
            if np.any(labels == k):
                centers[k] = scores[labels == k].mean(axis=0)
    return labels


def transition_grammar(labels: np.ndarray) -> Dict[str, int]:
    pairs = [f"{a}->{b}" for a, b in zip(labels[:-1], labels[1:]) if a != b]
    return {p: pairs.count(p) for p in sorted(set(pairs))}


def recurrence_score(x: np.ndarray, radius_quantile: float = 0.08) -> float:
    if pdist is None or len(x) < 3:
        return float("nan")
    d = squareform(pdist(x))
    radius = np.quantile(d[d > 0], radius_quantile) if np.any(d > 0) else 0.0
    return float(np.mean((d <= radius) & (~np.eye(len(x), dtype=bool))))


def compression_ratio(labels: np.ndarray) -> float:
    s = ",".join(map(str, labels.tolist())).encode()
    if not s:
        return 1.0
    return len(zlib.compress(s)) / len(s)


def nonlinear_forecastability(x: np.ndarray) -> float:
    """Nearest-neighbor one-step forecast R^2 over delay embedding."""
    if len(x) < 8 or pdist is None:
        return float("nan")
    source, target = x[:-1], x[1:]
    d = squareform(pdist(source))
    np.fill_diagonal(d, np.inf)
    nn = d.argmin(axis=1)
    pred = target[nn]
    ss_res = ((target - pred) ** 2).sum()
    ss_tot = ((target - target.mean(axis=0)) ** 2).sum()
    return float(1 - ss_res / max(ss_tot, 1e-12))


def perturbation_recovery_proxy(result: Dict) -> float:
    q = result["artifacts"][:, 2]
    low = np.where(q < 0.35)[0]
    if len(low) == 0:
        return 1.0
    recoveries = []
    for i in low[:20]:
        after = q[i:min(len(q), i + 20)]
        recoveries.append(float(np.any(after > 0.5)))
    return float(np.mean(recoveries))


def analyze_result(result: Dict, outdir: str | Path | None = None) -> Dict:
    y = build_observable(result)
    controls = result["action_counts"]
    resid = residualize(y, controls)
    embedded = delay_embed(resid, lags=3)
    scores, explained = pca(embedded, 3)
    labels = cluster_lobes(scores)
    metrics = {
        "timesteps": int(result["states"].shape[0]),
        "latent_shape": list(result["states"].shape),
        "field_shape": list(result["fields"].shape),
        "observable_shape": list(y.shape),
        "residual_shape": list(resid.shape),
        "embedded_shape": list(embedded.shape),
        "pca_explained": explained.tolist(),
        "n_lobes": int(len(set(labels.tolist()))),
        "transition_grammar": transition_grammar(labels),
        "recurrence": recurrence_score(scores),
        "compression_ratio": compression_ratio(labels),
        "nonlinear_forecastability": nonlinear_forecastability(embedded),
        "perturbation_recovery_proxy": perturbation_recovery_proxy(result),
        "artifact_final": result["artifacts"][-1].tolist(),
        "field_minmax": [float(result["fields"].min()), float(result["fields"].max())],
        "mean_fatigue_final": float(result["states"][-1, :, 6].mean()),
        "mean_threshold_final": float(result["states"][-1, :, 7].mean()),
    }
    if outdir is not None:
        out = Path(outdir); out.mkdir(parents=True, exist_ok=True)
        np.save(out / "observable.npy", y)
        np.save(out / "residuals.npy", resid)
        np.save(out / "embedding.npy", embedded)
        np.save(out / "pca_scores.npy", scores)
        np.save(out / "lobe_labels.npy", labels)
        (out / "metrics.json").write_text(json.dumps(metrics, indent=2, sort_keys=True))
    return metrics
