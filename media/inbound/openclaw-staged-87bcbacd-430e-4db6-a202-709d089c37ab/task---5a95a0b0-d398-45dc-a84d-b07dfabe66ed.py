"""Sequence-transform composition task for CAROM prototyping.

Workspace: n = 6 slots over Z_8.  Commands are whole-sequence transforms
(small vocab -- compatible with CAROM's K-operator routing bottleneck).
A program is up to L_MAX commands, executed in presentation order; shorter
programs are padded with trailing 'noop'.  Two synonym tokens force routing
reuse.  Critical-path depth of a sample = number of non-noop commands.
"""
import random
import torch

V = 8
N_SLOTS = 6
L_MAX = 5

def _inc(v): return [(x + 1) % V for x in v]
def _dbl(v): return [(2 * x) % V for x in v]
def _neg(v): return [(-x) % V for x in v]
def _rev(v): return v[::-1]
def _shr(v): return [v[-1]] + v[:-1]
def _swp(v): return [v[1], v[0]] + v[2:]
def _cms(v):
    out, s = [], 0
    for x in v: s = (s + x) % V; out.append(s)
    return out
def _nop(v): return v

OPS = [("noop", _nop), ("inc", _inc), ("dbl", _dbl), ("neg", _neg),
       ("rev", _rev), ("shr", _shr), ("swp", _swp), ("cms", _cms),
       ("inc_syn", _inc), ("rev_syn", _rev)]          # last two = synonyms
C_VOCAB = len(OPS)
NOOP = 0
REAL = list(range(1, C_VOCAB))

def make_batch(bs, rng, device="cpu", fixed_len=None):
    C = torch.zeros(bs, L_MAX, dtype=torch.long)
    X = torch.zeros(bs, N_SLOTS, dtype=torch.long)
    Y = torch.zeros(bs, N_SLOTS, dtype=torch.long)
    D = torch.zeros(bs, dtype=torch.long)             # effective program length
    for b in range(bs):
        L = fixed_len if fixed_len else rng.randint(2, L_MAX)
        cmds = [rng.choice(REAL) for _ in range(L)] + [NOOP] * (L_MAX - L)
        vals = [rng.randrange(V) for _ in range(N_SLOTS)]
        out = list(vals)
        for c in cmds:
            out = OPS[c][1](out)
        C[b] = torch.tensor(cmds); X[b] = torch.tensor(vals)
        Y[b] = torch.tensor(out); D[b] = L
    return C.to(device), None, X.to(device), Y.to(device), D.to(device)

if __name__ == "__main__":
    rng = random.Random(0)
    C, P, X, Y, D = make_batch(4, rng)
    print("vocab", C_VOCAB, "\ncmds", C[0], "init", X[0], "target", Y[0], "len", D[0])
    v = X[2].tolist()
    for c in C[2].tolist(): v = OPS[c][1](v)
    assert v == Y[2].tolist(); print("generator self-check OK")
