"""PyTorch backend — DRAFT, experimental until the exactness gate has run.

Admission policy: this backend may not be used for science until
`tests/test_torch_exactness.py` passes on the target install — the
functional optimizer replicas below must match `torch.optim` bit-for-bit
(float64, atol=0) over 50 random steps. That test is the backend's gate.

Strategy:
  * models are made functional with `torch.func.functional_call`;
  * gradients via `torch.func.grad` (never `.backward()` / `.grad`
    side effects);
  * the update step is a pure function over
    state = (params: dict, m: dict, v: dict), matching the R3 protocol;
  * propagation via `torch.func.jvp` through the entire step (exact-D).

Phase-0 hazards, handled by policy rather than cleverness: dropout and
data-order RNG must be captured (eval-mode or explicit generators);
schedules fold into `t`; fused/foreach/AMP paths are excluded.
"""
from __future__ import annotations

from typing import Callable, Mapping

try:
    import torch
    from torch import func as tfunc
    HAVE_TORCH = True
except Exception:                                    # pragma: no cover
    HAVE_TORCH = False


# ---------------------------------------------------------------------
# functional optimizer replicas (must match torch.optim bit-for-bit)
# ---------------------------------------------------------------------

def adamw_step(params: Mapping[str, "torch.Tensor"], m, v, t: int,
               grads, lr: float, betas=(0.9, 0.999), eps: float = 1e-8,
               weight_decay: float = 0.0):
    """Replicates torch.optim.AdamW (decoupled weight decay, PyTorch
    ordering: decay applied to params BEFORE the Adam update, using the
    pre-step parameter value). Returns (params2, m2, v2)."""
    b1, b2 = betas
    p2, m2, v2 = {}, {}, {}
    bc1, bc2 = 1 - b1 ** t, 1 - b2 ** t
    for k in params:
        p = params[k] * (1 - lr * weight_decay)
        mk = b1 * m[k] + (1 - b1) * grads[k]
        vk = b2 * v[k] + (1 - b2) * grads[k] * grads[k]
        denom = (vk / bc2).sqrt() + eps
        p2[k] = p - lr * (mk / bc1) / denom
        m2[k], v2[k] = mk, vk
    return p2, m2, v2


def sgd_step(params, momentum_buf, t, grads, lr: float,
             momentum: float = 0.0, weight_decay: float = 0.0):
    """Replicates torch.optim.SGD (L2 weight decay folded into the
    gradient, PyTorch momentum convention)."""
    p2, buf2 = {}, {}
    for k in params:
        g = grads[k] + weight_decay * params[k]
        if momentum != 0.0:
            b = momentum * momentum_buf[k] + g
            buf2[k], g = b, b
        else:
            buf2[k] = momentum_buf[k]
        p2[k] = params[k] - lr * g
    return p2, buf2


# ---------------------------------------------------------------------
# backbone (mirrors JaxBackbone.measure; see backbone_jax.py for the
# documented semantics — kept intentionally parallel)
# ---------------------------------------------------------------------

class TorchBackbone:
    def __init__(self, step: Callable, params_of: Callable):
        if not HAVE_TORCH:
            raise ImportError("torch not available")
        self.step, self.params_of = step, params_of

    def inject(self, state, batch0, t0, gate_a, gate_o):
        st_g = self.step(state, batch0, t0, gate_a)
        st_o = self.step(state, batch0, t0, gate_o)
        tan = _tree_sub(st_g, st_o)
        return st_o, tan

    def measure(self, state, t0, plan, actions, horizons, gate_of,
                loss_A: Callable):
        gate_o = gate_of(None)
        out = {}
        maxh = max(horizons)
        for act in actions:
            st_base, tan = self.inject(state, plan.batches[0], t0,
                                       gate_of(act), gate_o)
            st, res = st_base, {}
            for k in range(1, maxh + 1):
                if k > 1:
                    batch, t = plan.batches[k - 1], t0 + k - 1
                    fn = lambda s: self.step(s, batch, t, gate_o)
                    st, tan = tfunc.jvp(fn, (st,), (tan,))
                if k in horizons:
                    p, dt = self.params_of(st), self.params_of(tan)
                    res[k] = float(tfunc.jvp(loss_A, (p,), (dt,))[1])
            out[repr(act)] = res
        return out


def _tree_sub(a, b):
    if isinstance(a, dict):
        return {k: _tree_sub(a[k], b[k]) for k in a}
    if isinstance(a, (tuple, list)):
        return type(a)(_tree_sub(x, y) for x, y in zip(a, b))
    return a - b
