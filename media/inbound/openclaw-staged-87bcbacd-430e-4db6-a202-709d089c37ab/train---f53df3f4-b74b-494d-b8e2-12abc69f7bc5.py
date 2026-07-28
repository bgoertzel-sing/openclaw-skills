import argparse, random, time
import torch, torch.nn.functional as F
from task import make_batch
from model import Scheduled, FixedPoint, Itinerant

def accuracy(logits, Y):
    return (logits.argmax(-1) == Y).float().mean().item()

def run(variant, steps=1500, bs=128, lr=2e-3, scrambled=False, seed=0,
        ckpt=None, budget=280, **kw):
    torch.manual_seed(seed); rng = random.Random(seed)
    model = {"scheduled": Scheduled, "fixedpoint": FixedPoint,
             "itinerant": Itinerant}[variant](**kw)
    opt = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-4)
    sched = torch.optim.lr_scheduler.OneCycleLR(opt, lr, total_steps=steps)
    start = 0
    if ckpt:
        try:
            st = torch.load(ckpt, weights_only=False)
            model.load_state_dict(st["m"]); opt.load_state_dict(st["o"])
            sched.load_state_dict(st["s"]); start = st["it"] + 1
            rng.setstate(st["rng"]); torch.set_rng_state(st["trng"])
            print(f"  resumed at it {start}")
        except FileNotFoundError:
            pass
    t0 = time.time()
    acc = 0.0
    for it in range(start, steps):
        if time.time() - t0 > budget:
            break
        C, P, X, Y, D = make_batch(bs, rng)
        if variant == "fixedpoint":
            logits, resid = model(C, X, return_resid=True)
            loss = F.cross_entropy(logits.reshape(-1, logits.shape[-1]), Y.reshape(-1)) \
                   + 1.0 * resid[:, -1].mean()          # contraction pressure
        else:
            logits = model(C, X)
            loss = F.cross_entropy(logits.reshape(-1, logits.shape[-1]), Y.reshape(-1))
        opt.zero_grad(); loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        opt.step(); sched.step()
        if it % 150 == 0 or it == steps - 1:
            model.eval()
            with torch.no_grad():
                C, P, X, Y, D = make_batch(512, rng)
                logits = model(C, X)
                acc = accuracy(logits, Y)
            model.train()
            print(f"  it {it:4d}  loss {loss.item():.3f}  eval-acc {acc:.3f}"
                  f"  ({time.time()-t0:.0f}s)", flush=True)
    if ckpt:
        torch.save({"m": model.state_dict(), "o": opt.state_dict(),
                    "s": sched.state_dict(), "it": it, "rng": rng.getstate(),
                    "trng": torch.get_rng_state()}, ckpt)
        print(f"  saved {ckpt} at it {it}")
    return model, acc

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("variant"); ap.add_argument("--steps", type=int, default=1500)
    ap.add_argument("--scrambled", action="store_true")
    ap.add_argument("--fixed_chain", action="store_true")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--ckpt", default=None)
    ap.add_argument("--budget", type=int, default=280)
    ap.add_argument("--bs", type=int, default=128)
    a = ap.parse_args()
    kw = {"fixed_chain": True} if a.fixed_chain else {}
    run(a.variant, steps=a.steps, scrambled=a.scrambled, seed=a.seed,
        ckpt=a.ckpt, budget=a.budget, bs=a.bs, **kw)
