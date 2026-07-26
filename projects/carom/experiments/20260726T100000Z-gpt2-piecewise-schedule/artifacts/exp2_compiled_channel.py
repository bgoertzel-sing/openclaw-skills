"""Experiment 2 (GPU): the COMPILED CHANNEL.

Per-instance heteroclinic topology from dependency language. Programs are
presented SCRAMBLED; each command carries a linguistic dependency clause
("to begin, ..." / "after you <predecessor action>, <action>"). A pairwise
scorer over frozen-LM span representations predicts "m directly follows j"
and is compiled into the GLV inhibition matrix; a learned entry scorer sets
the initial condition. Distinct primitives per program keep references
unambiguous.

Supervision regimes:
  --edges 1.0   compiler-supervised (BCE on true edges + task loss)
  --edges 0.0   emergent (task loss only)
Metrics: task acc / edge accuracy / itinerary-vs-true-order Kendall tau /
structural length generalization (train L<=4, eval L=5).

Base model: TinyLM fallback (CPU smoke) or GPT-2-small (GPU) -- see BASE
section. Everything else is device-agnostic.

Run:  python exp2_compiled_channel.py --steps 4000 --edges 1.0
"""
import argparse, math, random, time
import torch, torch.nn as nn, torch.nn.functional as F

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# ---------------------------------------------------------------- task ------
V = 8; N_SLOTS = 6; L_MAX = 5
def _inc(v): return [(x+1)%V for x in v]
def _dbl(v): return [(2*x)%V for x in v]
def _neg(v): return [(-x)%V for x in v]
def _rev(v): return v[::-1]
def _shr(v): return [v[-1]]+v[:-1]
def _swp(v): return [v[1],v[0]]+v[2:]
def _cms(v):
    out,s=[],0
    for x in v: s=(s+x)%V; out.append(s)
    return out
PRIMS=[("inc",_inc),("dbl",_dbl),("neg",_neg),("rev",_rev),
       ("shr",_shr),("swp",_swp),("cms",_cms)]
PARA=[["add one to every item","increase each number by one","bump all values up by one"],
      ["double every value","multiply each item by two","scale all numbers times two"],
      ["negate every item","flip the sign of each number","make all values negative"],
      ["reverse the order","flip the list around","put the items in backwards order"],
      ["rotate everything right by one","shift each item one place right","move all values right one spot"],
      ["swap the first two items","exchange the first two numbers","switch the first pair"],
      ["take running totals","replace each item with the sum so far","turn the list into partial sums"]]
WORDS = sorted({w for ps in PARA for p in ps for w in p.split()}
               | {"then","<pad>","<bos>","to","begin","after","you",","})
W2I = {w:i for i,w in enumerate(WORDS)}
T_VOCAB = len(WORDS)
CMD_TOK = 4 + 8 + 8          # "after you <=8 words , <=8 words" + slack
MAXTOK = 1 + L_MAX*CMD_TOK

def render_cmd(prim, var, dep_prim, dep_var):
    """One command sentence. dep_prim None => entry command."""
    if dep_prim is None:
        ws = ["to","begin",","] + PARA[prim][var].split()
    else:
        ws = ["after","you"] + PARA[dep_prim][dep_var].split() + [","] + PARA[prim][var].split()
    return ws

def make_batch(bs, rng, variant_pool=(0,1,2), len_range=(2,4), fixed_len=None):
    T   = torch.full((bs, MAXTOK), W2I["<pad>"], dtype=torch.long)
    SP  = torch.zeros(bs, L_MAX, 2, dtype=torch.long)
    X   = torch.zeros(bs, N_SLOTS, dtype=torch.long)
    Y   = torch.zeros(bs, N_SLOTS, dtype=torch.long)
    E   = torch.zeros(bs, L_MAX, L_MAX)          # E[m,j]=1 iff m directly follows j
    ENT = torch.zeros(bs, L_MAX)                 # entry command indicator
    ORD = torch.full((bs, L_MAX), -1, dtype=torch.long)  # true topological rank
    Ls  = torch.zeros(bs, dtype=torch.long)
    for b in range(bs):
        L = fixed_len or rng.randint(*len_range)
        prims = rng.sample(range(7), L)          # distinct -> unambiguous refs
        vrs = [rng.choice(variant_pool) for _ in range(L)]
        order = list(range(L)); rng.shuffle(order)   # presentation order
        pos_of = {step: slot for slot, step in enumerate(order)}
        toks = [W2I["<bos>"]]
        # presented slot s shows execution-step order[s]
        spans = [None]*L
        for s in range(L):
            step = order[s]
            dep = (prims[step-1], vrs[step-1]) if step > 0 else (None, None)
            ws = render_cmd(prims[step], vrs[step], dep[0], dep[1] if dep[0] is not None else 0)
            a = len(toks); toks += [W2I[w] for w in ws]
            spans[s] = (a, len(toks))
        T[b, :len(toks)] = torch.tensor(toks)
        for s,(a,bb) in enumerate(spans): SP[b,s] = torch.tensor([a,bb])
        for step in range(L):
            ORD[b, pos_of[step]] = step
            if step == 0: ENT[b, pos_of[step]] = 1.0
            else: E[b, pos_of[step], pos_of[step-1]] = 1.0
        vals = [rng.randrange(V) for _ in range(N_SLOTS)]
        out = list(vals)
        for step in range(L): out = PRIMS[prims[step]][1](out)
        X[b] = torch.tensor(vals); Y[b] = torch.tensor(out); Ls[b] = L
    return (T.to(DEVICE), SP.to(DEVICE), X.to(DEVICE), Y.to(DEVICE),
            E.to(DEVICE), ENT.to(DEVICE), ORD.to(DEVICE), Ls.to(DEVICE))

# ---------------------------------------------------------------- base ------
class TinyLM(nn.Module):
    """CPU fallback stand-in. On GPU replace with GPT-2 (see GPT2Base)."""
    def __init__(self, d=96, nlayer=3, nhead=4):
        super().__init__()
        self.d = d
        self.emb = nn.Embedding(T_VOCAB, d); self.pos = nn.Embedding(MAXTOK, d)
        layer = nn.TransformerEncoderLayer(d, nhead, 4*d, batch_first=True,
                                           norm_first=True, dropout=0.0)
        self.enc = nn.TransformerEncoder(layer, nlayer)
        self.head = nn.Linear(d, T_VOCAB)
    def hidden(self, T):
        h = self.emb(T) + self.pos(torch.arange(T.shape[1], device=T.device))
        mask = nn.Transformer.generate_square_subsequent_mask(T.shape[1]).to(T.device)
        return self.enc(h, mask=mask)
    def forward(self, T): return self.head(self.hidden(T))

def pretrain_tiny(steps=1500, bs=96, seed=0):
    torch.manual_seed(seed); rng = random.Random(seed)
    lm = TinyLM().to(DEVICE)
    opt = torch.optim.AdamW(lm.parameters(), lr=1e-3)
    for it in range(steps):
        T,_,_,_,_,_,_,_ = make_batch(bs, rng)
        loss = F.cross_entropy(lm(T)[:,:-1].reshape(-1,T_VOCAB), T[:,1:].reshape(-1),
                               ignore_index=W2I["<pad>"])
        opt.zero_grad(); loss.backward(); opt.step()
        if it % 300 == 0: print(f"  lm {it} {loss.item():.3f}", flush=True)
    for p in lm.parameters(): p.requires_grad = False
    return lm.eval()

# --- GPT-2 base (GPU): uncomment, pip install transformers ---
# from transformers import GPT2Model, GPT2TokenizerFast
# class GPT2Base(nn.Module):
#     def __init__(self, layer=-1):
#         super().__init__()
#         self.m = GPT2Model.from_pretrained("gpt2").eval()
#         self.tok = GPT2TokenizerFast.from_pretrained("gpt2")
#         self.d = 768; self.layer = layer
#         for p in self.m.parameters(): p.requires_grad = False
#     # re-tokenize word-rendered sentences; keep span bookkeeping in
#     # GPT-2 token space via offset_mapping. Then hidden(T) analog returns
#     # hidden_states[self.layer]. Mean-pool spans as below.
# --- GPT-2 base (GPU) ---
from transformers import GPT2Model, GPT2TokenizerFast

class GPT2Base(nn.Module):
    """Frozen GPT-2 small (124M). Re-tokenizes word-rendered sentences into BPE
    and tracks span offsets so span_reps can mean-pool over the right tokens."""
    def __init__(self, layer=-1):
        super().__init__()
        self.m = GPT2Model.from_pretrained("gpt2").eval()
        self.tok = GPT2TokenizerFast.from_pretrained("gpt2")
        self.d = 768
        self.layer = layer
        for p in self.m.parameters():
            p.requires_grad = False

    def hidden(self, T_ids):
        """T_ids: [B, Seq] word-level indices into W2I.
        Returns hidden_states[layer]: [B, Seq_bpe, 768]."""
        B = T_ids.shape[0]
        all_hidden = []
        for b in range(B):
            # Convert word indices back to word strings
            words = [list(W2I.keys())[list(W2I.values()).index(int(i))]
                     for i in T_ids[b] if int(i) != W2I["<pad>"]]
            text = " ".join(words)
            enc = self.tok(text, return_tensors="pt", return_offsets_mapping=True)
            input_ids = enc["input_ids"].to(T_ids.device)
            attn = enc["attention_mask"].to(T_ids.device)
            with torch.no_grad():
                out = self.m(input_ids, attention_mask=attn,
                             output_hidden_states=True)
            hs = out.hidden_states[self.layer]  # [1, Seq_bpe, 768]
            all_hidden.append(hs)
        # Pad to max bpe length
        max_len = max(h.shape[1] for h in all_hidden)
        H = torch.zeros(B, max_len, self.d, device=T_ids.device)
        attn_mask = torch.zeros(B, max_len, device=T_ids.device)
        for b, h in enumerate(all_hidden):
            H[b, :h.shape[1]] = h[0]
            attn_mask[b, :h.shape[1]] = 1.0
        return H, attn_mask

    def forward(self, T):
        H, _ = self.hidden(T)
        return H  # hidden states only; no LM head needed


def span_reps_gpt2(lm, T, SP):
    """Mean-pool GPT-2 hidden states over each command span.
    Re-tokenizes per-sample and maps word-level span offsets to BPE offsets."""
    with torch.no_grad():
        B, Lm = SP.shape[0], SP.shape[1]
        out = torch.zeros(B, Lm, lm.d, device=T.device)
        for b in range(B):
            # Reconstruct the word sequence (excluding padding)
            word_ids = T[b].tolist()
            non_pad = []
            for wi in word_ids:
                if wi == W2I["<pad>"]:
                    break
                non_pad.append(wi)
            words = [list(W2I.keys())[list(W2I.values()).index(i)] for i in non_pad]
            text = " ".join(words)
            enc = lm.tok(text, return_offsets_mapping=True,
                         return_tensors="pt")
            input_ids = enc["input_ids"].to(T.device)
            attn = enc["attention_mask"].to(T.device)
            offsets = enc["offset_mapping"][0]  # [Seq_bpe, 2]
            res = lm.m(input_ids, attention_mask=attn, output_hidden_states=True)
            hs = res.hidden_states[lm.layer][0]  # [Seq_bpe, 768]
            # Map word-level span (a, b) to character positions, then to BPE tokens
            # Build character offset for each word
            char_pos = 0
            word_char_spans = []
            for wi in non_pad:
                w = list(W2I.keys())[list(W2I.values()).index(wi)]
                word_char_spans.append((char_pos, char_pos + len(w)))
                char_pos += len(w) + 1  # +1 for space
            for s in range(Lm):
                a, bb = SP[b, s].tolist()
                if a >= bb or a >= len(non_pad):
                    continue
                # Character span for this command
                char_start = word_char_spans[a][0]
                char_end = word_char_spans[min(bb - 1, len(non_pad) - 1)][1]
                # Find BPE tokens in this character range
                mask = (offsets[:, 0] >= char_start) & (offsets[:, 1] <= char_end)
                if mask.any():
                    out[b, s] = hs[mask].mean(0)
                else:
                    out[b, s] = hs[len(hs) // 2]  # fallback
        return out

def span_reps(lm, T, SP):
    with torch.no_grad():
        h = lm.hidden(T)
    B, Lm = SP.shape[0], SP.shape[1]
    out = torch.zeros(B, Lm, lm.d, device=T.device)
    idx = torch.arange(T.shape[1], device=T.device)
    for i in range(Lm):
        a, b = SP[:,i,0], SP[:,i,1]
        mask = (idx[None,:] >= a[:,None]) & (idx[None,:] < b[:,None])
        out[:,i] = (h * mask[:,:,None]).sum(1) / mask.sum(1, keepdim=True).clamp(min=1)
    return out

# ------------------------------------------------------------- operators ----
class OperatorCore(nn.Module):
    def __init__(self, d, K):
        super().__init__()
        self.d, self.K = d, K
        def pk(*s):
            t = torch.empty(*s); nn.init.xavier_uniform_(t.view(s[0], -1)); return nn.Parameter(t)
        self.Wq=pk(K,3*d,d); self.Wk=pk(K,3*d,d); self.Wv=pk(K,3*d,d)
        self.T1=pk(K,4*d,2*d); self.T2=pk(K,2*d,d); self.Wg=pk(K,d,d)
        self.gb=nn.Parameter(torch.zeros(K,d)); self.ln=nn.LayerNorm(d)
    def forward(self, w, feat):
        h = torch.cat([self.ln(w), feat], -1)
        q = torch.einsum("bnf,kfd->bknd", h, self.Wq)
        k = torch.einsum("bnf,kfd->bknd", h, self.Wk)
        v = torch.einsum("bnf,kfd->bknd", h, self.Wv)
        att = (torch.einsum("bknd,bkmd->bknm", q, k) / math.sqrt(self.d)).softmax(-1)
        r = torch.einsum("bknm,bkmd->bknd", att, v)
        z = torch.cat([r, self.ln(w).unsqueeze(1).expand_as(r),
                       feat.unsqueeze(1).expand(*r.shape[:-1], 2*self.d)], -1)
        z = torch.einsum("bknf,kfe->bkne", F.gelu(torch.einsum("bknf,kfe->bkne", z, self.T1)), self.T2)
        g = torch.sigmoid(torch.einsum("bknd,kde->bkne", z, self.Wg) + self.gb[None,:,None,:])
        return g * torch.tanh(z)

# ------------------------------------------------------- compiled channel ---
class CompiledChannel(nn.Module):
    """Heteroclinic CAROM whose rho is compiled per-instance from LM reps."""
    RHO_FAR, RHO_SELF, RHO_SUCC, RHO_KILL = 2.5, 1.0, 0.35, 4.0
    def __init__(self, lm_d, d=48, K=8, S=72, dt=0.2, noise=0.02):
        super().__init__()
        self.d,self.K,self.S,self.dt,self.noise = d,K,S,dt,noise
        self.sym = nn.Embedding(V, d); self.pos = nn.Embedding(N_SLOTS, d)
        self.core = OperatorCore(d, K)
        self.out = nn.Sequential(nn.LayerNorm(d), nn.Linear(d,2*d), nn.GELU(), nn.Linear(2*d,V))
        self.hyper = nn.Sequential(nn.LayerNorm(lm_d), nn.Linear(lm_d,lm_d), nn.GELU(), nn.Linear(lm_d,K))
        edge_in = 3*lm_d
        self.edge = nn.Sequential(nn.LayerNorm(edge_in), nn.Linear(edge_in, lm_d),
                                  nn.GELU(), nn.Linear(lm_d, 1))
        self.entry = nn.Sequential(nn.LayerNorm(lm_d), nn.Linear(lm_d, lm_d//2),
                                   nn.GELU(), nn.Linear(lm_d//2, 1))
        self.sigma = nn.Sequential(nn.LayerNorm(d), nn.Linear(d,d), nn.GELU(), nn.Linear(d,1))
        self.pool_q = nn.Parameter(torch.randn(d)/math.sqrt(d))
        self.sig_scale = nn.Parameter(torch.tensor(0.5))
        self.base,self.fk,self.ftau,self.leak = 3.0, 1.5, 6.0, 0.02

    def edge_logits(self, H):                     # [B,M,M]; diag masked later
        B, M, _ = H.shape
        hi = H.unsqueeze(2).expand(B,M,M,-1); hj = H.unsqueeze(1).expand(B,M,M,-1)
        return self.edge(torch.cat([hi, hj, hi*hj], -1)).squeeze(-1)

    def compile_rho(self, H, live):
        """rho[m,j] = inhibition FELT BY m FROM j.  p_mj = P(m follows j)
        lowers rho[m,j] toward RHO_SUCC and raises rho[j,m] toward RHO_KILL."""
        B, M, _ = H.shape
        el = self.edge_logits(H)
        pair = live.unsqueeze(1)*live.unsqueeze(2)
        eye = torch.eye(M, device=H.device)[None]
        p = torch.sigmoid(el) * pair * (1-eye)
        rho = torch.full((B,M,M), self.RHO_FAR, device=H.device)
        rho = rho + (self.RHO_SELF - self.RHO_FAR) * eye
        rho = rho + (self.RHO_SUCC - self.RHO_FAR) * p          # m invadable from j
        rho = rho + (self.RHO_KILL - self.RHO_FAR) * p.transpose(1,2)  # j killed by m
        return rho, el

    def forward(self, H, X, live, return_traj=False):
        B, M, _ = H.shape; dev = H.device
        e = F.normalize(self.sym(X), dim=-1) * math.sqrt(self.d)
        p = self.pos(torch.arange(N_SLOTS, device=dev)).expand_as(e)
        w, feat = e, torch.cat([e,p], -1)
        beta_cmd = F.softmax(self.hyper(H), -1)
        rho, el = self.compile_rho(H, live)
        ent = self.entry(H).squeeze(-1) - 30.0*(1-live)
        a = 0.05 + 0.95*F.softmax(ent, -1)                      # learned channel entry
        f = torch.zeros_like(a)
        fit_bias = torch.zeros_like(a)                          # (reserved)
        traj = []
        for t in range(self.S):
            attn = torch.einsum("bnd,d->bn", w, self.pool_q).softmax(-1)
            pooled = torch.einsum("bn,bnd->bd", attn, w)
            fit = self.base + self.sig_scale*(self.sigma(pooled) + fit_bias) \
                  - self.fk*f - 10.0*(1-live)
            comp = torch.einsum("bmj,bj->bm", rho, a)
            noise = self.noise*torch.randn_like(a) if self.training else 0.0
            a = (a + self.dt*a*(fit - comp) + noise).clamp(0.05, 4.0)
            f = f + self.dt/self.ftau*(a - f)
            beta = torch.einsum("bm,bmk->bk", a*live, beta_cmd)
            u = self.core(w, feat)
            w = w + self.dt*(torch.einsum("bk,bknd->bnd", beta, u) - self.leak*w)
            if return_traj: traj.append(a.detach().clone())
        out = self.out(w)
        return (out, el, torch.stack(traj,1) if return_traj else None)

# ------------------------------------------------------------- train/eval ---
def kendall(seq):
    if len(seq) < 2: return 0.0
    c = sum(seq[i] < seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
    d = sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
    return (c-d)/max(1, c+d)

def phases(a):
    s = a.argmax(-1).tolist(); out=[s[0]]
    for x in s[1:]:
        if x != out[-1]: out.append(x)
    return out

def evaluate(model, lm, rng, fixed_len=None, n=256, len_range=(2,4), span_fn=None):
    model.eval()
    with torch.no_grad():
        T,SP,X,Y,E,ENT,ORD,Ls = make_batch(n, rng, fixed_len=fixed_len, len_range=len_range)
        live = (ORD >= 0).float()
        H = (span_fn or span_reps)(lm, T, SP)
        out, el, traj = model(H, X, live, return_traj=True)
        acc = (out.argmax(-1)==Y).float().mean().item()
        pair = (live.unsqueeze(1)*live.unsqueeze(2) *
                (1-torch.eye(L_MAX, device=DEVICE)[None])).bool()
        eacc = ((torch.sigmoid(el[pair])>0.5).float() == E[pair]).float().mean().item()
        taus = []
        for b in range(n):
            ranks = [ORD[b,m].item() for m in phases(traj[b]) if ORD[b,m] >= 0]
            taus.append(kendall(ranks))
        tau = sum(taus)/len(taus)
    model.train()
    return acc, eacc, tau

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--steps", type=int, default=4000)
    ap.add_argument("--bs", type=int, default=128)
    ap.add_argument("--edges", type=float, default=1.0, help="edge-supervision weight (0=emergent)")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--lm_steps", type=int, default=1500)
    ap.add_argument("--budget", type=int, default=10**9)
    ap.add_argument("--ckpt", default="exp2.pt")
    ap.add_argument("--base", default="tiny", choices=["tiny", "gpt2"],
                   help="frozen LM base: tiny (3-layer) or gpt2 (124M)")
    ap.add_argument("--gpt2_layer", type=int, default=-1,
                   help="GPT-2 hidden layer to use (-1 = last)")
    a = ap.parse_args()
    torch.manual_seed(a.seed); rng = random.Random(a.seed)
    if a.base == "gpt2":
        print("loading frozen GPT-2-small base...")
        lm = GPT2Base(layer=a.gpt2_layer).to(DEVICE)
        span_fn = span_reps_gpt2
    else:
        print("pretraining tiny base (swap for GPT2Base on GPU)...")
        lm = pretrain_tiny(a.lm_steps)
        span_fn = span_reps
    model = CompiledChannel(lm.d).to(DEVICE)
    opt = torch.optim.AdamW(model.parameters(), lr=2e-3, weight_decay=1e-4)
    sched = torch.optim.lr_scheduler.OneCycleLR(opt, 2e-3, total_steps=a.steps)
    start = 0
    try:
        st = torch.load(a.ckpt, weights_only=False)
        model.load_state_dict(st["m"]); opt.load_state_dict(st["o"])
        sched.load_state_dict(st["s"]); start = st["it"]+1; rng.setstate(st["rng"])
        print(f"resumed {start}")
    except FileNotFoundError: pass
    t0 = time.time(); it = start
    for it in range(start, a.steps):
        if time.time()-t0 > a.budget: break
        T,SP,X,Y,E,ENT,ORD,Ls = make_batch(a.bs, rng)   # train L in 2..4 (L=5 held out)
        live = (ORD >= 0).float()
        H = span_fn(lm, T, SP)
        out, el, _ = model(H, X, live)
        loss = F.cross_entropy(out.reshape(-1, V), Y.reshape(-1))
        if a.edges > 0:
            pair = live.unsqueeze(1)*live.unsqueeze(2)*(1-torch.eye(L_MAX, device=DEVICE)[None])
            eloss = F.binary_cross_entropy_with_logits(el, E, weight=pair)
            loss = loss + a.edges * eloss
        # entry supervision comes free with edges: ENT is derivable, supervise lightly
        if a.edges > 0:
            ent_logit = model.entry(H).squeeze(-1) - 30.0*(1-live)
            loss = loss + 0.2*a.edges*F.cross_entropy(ent_logit, ENT.argmax(-1))
        opt.zero_grad(); loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        opt.step(); sched.step()
        if it % 200 == 0:
            acc, eacc, tau = evaluate(model, lm, rng, span_fn=span_fn)
            acc5, eacc5, tau5 = evaluate(model, lm, rng, fixed_len=5, n=128, span_fn=span_fn)
            print(f"it {it} loss {loss.item():.3f} | L2-4: acc {acc:.3f} edge {eacc:.3f} "
                  f"tau {tau:.3f} | L5(held-out): acc {acc5:.3f} tau {tau5:.3f} "
                  f"({time.time()-t0:.0f}s)", flush=True)
    torch.save({"m":model.state_dict(),"o":opt.state_dict(),"s":sched.state_dict(),
                "it":it,"rng":rng.getstate()}, a.ckpt)
    print(f"saved {a.ckpt} @ {it}")

if __name__ == "__main__":
    main()
