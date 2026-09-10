#!/usr/bin/env python3
"""The sandbox MLP demo, re-expressed through the comcrit API: an
8->32->32->4 tanh MLP adapted from task A to a conflicting task B, with the
exact-D backbone measured against CRN paired rollouts at decision states,
and the confusion graph accumulated as a by-product.

Run:  python examples/mlp_jax_example.py    (CPU, ~1 min)
"""
import numpy as np
import jax, jax.numpy as jnp

jax.config.update("jax_enable_x64", True)

from comcrit.backbone_jax import JaxBackbone, make_adam_step, tree_dot, oracles_hvp
from comcrit.confusion import ConfusionGraph
from comcrit.protocols import BatchPlan
from comcrit.stats import spearman

# --- model, tasks -----------------------------------------------------
def init(key, scale=0.5):
    ks = jax.random.split(key, 3)
    return {"W1": scale * jax.random.normal(ks[0], (8, 32)) / np.sqrt(8),
            "b1": jnp.zeros(32),
            "W2": scale * jax.random.normal(ks[1], (32, 32)) / np.sqrt(32),
            "b2": jnp.zeros(32),
            "W3": scale * jax.random.normal(ks[2], (32, 4)) / np.sqrt(32),
            "b3": jnp.zeros(4)}

mlp = lambda p, x: jnp.tanh(jnp.tanh(x @ p["W1"] + p["b1"]) @ p["W2"]
                            + p["b2"]) @ p["W3"] + p["b3"]
mse = lambda p, X, Y: jnp.mean((mlp(p, X) - Y) ** 2)

key = jax.random.PRNGKey(0)
teacher = init(jax.random.split(key)[0], scale=1.0)
X = np.array(jax.random.normal(jax.random.split(key)[1], (4096, 8)))
YA = np.array(mlp(teacher, X))
YB = np.array(mlp(teacher, X[:, ::-1].copy()))          # layer-1 conflict

MODULES = {"layer1": ["W1", "b1"], "layer2": ["W2", "b2"],
           "head": ["W3", "b3"]}
def gate_of(act):
    g = {k: 1.0 for k in ["W1", "b1", "W2", "b2", "W3", "b3"]}
    if act is not None:
        for m in act[0]:
            for lf in MODULES[m]:
                g[lf] = act[1]
    return g

step, params_of, moments_view = make_adam_step(
    lambda p, b: mse(p, b[0], b[1]), lr=1e-3)
rng = np.random.default_rng(1)
batch = lambda Y: (lambda i: (jnp.array(X[i]), jnp.array(Y[i])))(
    rng.integers(0, 4096, 64))

# --- pretrain A, adapt B, measure at decision states ------------------
p0 = init(key)
Z = lambda: {k: jnp.zeros_like(v) for k, v in p0.items()}
state = (p0, Z(), Z())
for t in range(1, 601):
    state = step(state, batch(YA), t, gate_of(None))
state = (state[0], Z(), Z())

XA_ev, YA_ev = jnp.array(X[:1024]), jnp.array(YA[:1024])
loss_A = lambda p: mse(p, XA_ev, YA_ev)
hvpA = lambda p, v: oracles_hvp(loss_A, p, v)
bbone = JaxBackbone(step, params_of, moments_view, lr_for_frozen=1e-3)
graph = ConfusionGraph(MODULES)
acts = [([m], a) for m in MODULES for a in (0.5, 0.1)]
pair = (["layer1", "layer2"], 0.1)
H = [1, 5, 10]

tru, hat = {h: [] for h in H}, {h: [] for h in H}
for t in range(1, 121):
    b = batch(YB)
    if t % 10 == 5:
        plan = BatchPlan(batches=[batch(YB) for _ in range(max(H))])
        res = bbone.measure(state, t, plan, acts + [pair], H, gate_of, loss_A)
        # truth: CRN paired rollouts
        base_states, st = [], state
        for k in range(max(H)):
            st = step(st, plan.batches[k], t + k, gate_of(None))
            base_states.append(st)
        for act in acts + [pair]:
            st = state
            for k in range(max(H)):
                st = step(st, plan.batches[k], t + k,
                          gate_of(act if k == 0 else None))
                h = k + 1
                if h in H:
                    tv = float(loss_A(params_of(st))
                               - loss_A(params_of(base_states[k])))
                    tru[h].append(tv)
                    hat[h].append(res[repr(act)][h].tau_hat_A)
        # confusion graph: first-order conflict per module + planted pair
        gA = jax.grad(loss_A)(params_of(state))
        gB = jax.grad(lambda p: mse(p, plan.batches[0][0],
                                    plan.batches[0][1]))(params_of(state))
        for m, leaves in MODULES.items():
            graph.add_first_order(m, sum(float(jnp.vdot(gA[l], gB[l]))
                                         for l in leaves))
        um = res[repr((["layer1"], 0.1))][1].extras["u_theta"]
        un = res[repr((["layer2"], 0.1))][1].extras["u_theta"]
        graph.add_cross_curvature("layer1", "layer2",
                                  JaxBackbone.synergy_hat(um, un,
                                  lambda v: hvpA(params_of(state), v)))
    state = step(state, b, t, gate_of(None))

for h in H:
    print(f"h={h:2d}  exact-D Spearman vs paired truth: "
          f"{spearman(hat[h], tru[h]):.4f}")
import json
print(json.dumps(graph.export(), indent=2)[:600], "...")
