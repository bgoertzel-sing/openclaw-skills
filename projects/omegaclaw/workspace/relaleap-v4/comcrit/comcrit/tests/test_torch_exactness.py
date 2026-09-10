"""Admission gate for the torch backend: functional replicas must match
torch.optim bit-for-bit (float64) before the backend may be used."""
import pytest

torch = pytest.importorskip("torch")

from comcrit.backbone_torch import adamw_step, sgd_step


def _rand_params(gen):
    return {f"p{i}": torch.randn(7, 5, dtype=torch.float64, generator=gen,
                                 requires_grad=True) for i in range(3)}


@pytest.mark.parametrize("wd", [0.0, 0.01])
def test_adamw_replica_bit_exact(wd):
    gen = torch.Generator().manual_seed(0)
    ref = _rand_params(gen)
    opt = torch.optim.AdamW(ref.values(), lr=1e-3, weight_decay=wd,
                            foreach=False, fused=False)
    fn_p = {k: v.detach().clone() for k, v in ref.items()}
    m = {k: torch.zeros_like(v) for k, v in fn_p.items()}
    v = {k: torch.zeros_like(vv) for k, vv in fn_p.items()}
    for t in range(1, 51):
        grads = {k: torch.randn(7, 5, dtype=torch.float64, generator=gen)
                 for k in fn_p}
        for k, p in ref.items():
            p.grad = grads[k].clone()
        opt.step()
        fn_p, m, v = adamw_step(fn_p, m, v, t, grads, lr=1e-3,
                                weight_decay=wd)
        for k in fn_p:
            assert torch.equal(fn_p[k], ref[k].detach()), (k, t)


@pytest.mark.parametrize("mom,wd", [(0.0, 0.0), (0.9, 0.01)])
def test_sgd_replica_bit_exact(mom, wd):
    gen = torch.Generator().manual_seed(1)
    ref = _rand_params(gen)
    opt = torch.optim.SGD(ref.values(), lr=1e-2, momentum=mom,
                          weight_decay=wd, foreach=False)
    fn_p = {k: v.detach().clone() for k, v in ref.items()}
    buf = {k: torch.zeros_like(v) for k, v in fn_p.items()}
    for t in range(1, 51):
        grads = {k: torch.randn(7, 5, dtype=torch.float64, generator=gen)
                 for k in fn_p}
        for k, p in ref.items():
            p.grad = grads[k].clone()
        opt.step()
        fn_p, buf = sgd_step(fn_p, buf, t, grads, lr=1e-2, momentum=mom,
                             weight_decay=wd)
        for k in fn_p:
            assert torch.equal(fn_p[k], ref[k].detach()), (k, t)
