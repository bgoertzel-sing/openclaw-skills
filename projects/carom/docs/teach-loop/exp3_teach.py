"""Experiment 3: the TEACH LOOP -- LLM-taught neural operators.

Two primitives (rotate-LEFT, square-mod-8) are held out of all cap training.
The base LM pretrains on text that INCLUDES their descriptions (an LLM knows
the words for skills it hasn't proceduralized); the cap never sees them.
A teacher stand-in emits an operator spec: description (paraphrase variant 0)
+ N (x, y) pairs with noise rate eps. A fresh operator slot is trained on
pairs alone with the existing library FROZEN; the description's span rep
becomes the routing anchor. Invocation is then tested with paraphrase
variants 1,2 -- never used in teaching.

Measurements:
  M1 acquisition   : new-skill accuracy inside full mixed programs, invoked
                     by unseen paraphrases
  M2 interference  : old-primitive accuracy before vs after (frozen => equal)
  M3 sample eff.   : N-to-criterion vs teacher noise eps
  M4 novelty       : does frozen routing flag the new command pre-teaching?

Stages (checkpointed):  --stage lm | cap | teach | eval
GPU: raise D_LM/steps; swap TinyLM for GPT-2 (stub below); replace the
synthetic teacher with prompted program-of-thought generation.
"""
import argparse, math, random, time
import torch, torch.nn as nn, torch.nn.functional as F

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
GPU = DEVICE == "cuda"

# ------------------------------------------------------------------ task ----
V = 8; N_SLOTS = 6; L_MAX = 4
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
def _shl(v): return v[1:]+[v[0]]                 # HELD OUT (taught later)
def _sq(v):  return [(x*x)%V for x in v]         # HELD OUT (taught later)
PRIMS=[("inc",_inc),("dbl",_dbl),("neg",_neg),("rev",_rev),("shr",_shr),
       ("swp",_swp),("cms",_cms),("shl",_shl),("sq",_sq)]
N_OLD = 7          # cap trains on 0..6; 7,8 are teachable skills
PARA=[["add one to every item","increase each number by one","bump all values up by one"],
      ["double every value","multiply each item by two","scale all numbers times two"],
      ["negate every item","flip the sign of each number","make all values negative"],
      ["reverse the order","flip the list around","put the items in backwards order"],
      ["rotate everything right by one","shift each item one place right","move all values right one spot"],
      ["swap the first two items","exchange the first two numbers","switch the first pair"],
      ["take running totals","replace each item with the sum so far","turn the list into partial sums"],
      ["rotate everything left by one","shift each item one place left","move all values left one spot"],
      ["multiply each item by itself","square every value","replace each number with its own value times itself"]]
WORDS = sorted({w for ps in PARA for p in ps for w in p.split()}
               | {"then","<pad>","<bos>","on","gives","own"} | {str(i) for i in range(8)})
W2I = {w:i for i,w in enumerate(WORDS)}
T_VOCAB = len(WORDS)
MAXTOK = 1 + L_MAX*10 + (L_MAX-1)
GROUND_LEN = MAXTOK + 1 + N_SLOTS + 1 + N_SLOTS

def render(prims, variants):
    toks = ["<bos>"]; spans = []
    for i,(p,vr) in enumerate(zip(prims, variants)):
        if i: toks.append("then")
        a = len(toks); toks += PARA[p][vr].split(); spans.append((a, len(toks)))
    return [W2I[t] for t in toks], spans

def make_batch(bs, rng, prim_pool, variant_pool=(0,1), fixed_len=None,
               force_first=None, first_variants=None):
    T = torch.full((bs, MAXTOK), W2I["<pad>"], dtype=torch.long)
    SP = torch.zeros(bs, L_MAX, 2, dtype=torch.long)
    PR = torch.full((bs, L_MAX), -1, dtype=torch.long)
    X = torch.zeros(bs, N_SLOTS, dtype=torch.long)
    Y = torch.zeros(bs, N_SLOTS, dtype=torch.long)
    for b in range(bs):
        L = fixed_len or rng.randint(2, L_MAX)
        prims = [rng.choice(prim_pool) for _ in range(L)]
        if force_first is not None: prims[0] = force_first
        vrs = [rng.choice(variant_pool) for _ in range(L)]
        if force_first is not None and first_variants is not None:
            vrs[0] = rng.choice(first_variants)
        ids, spans = render(prims, vrs)
        T[b,:len(ids)] = torch.tensor(ids)
        for i,(a,bb) in enumerate(spans): SP[b,i]=torch.tensor([a,bb])
        PR[b,:L] = torch.tensor(prims)
        vals = [rng.randrange(V) for _ in range(N_SLOTS)]
        out = list(vals)
        for p in prims: out = PRIMS[p][1](out)
        X[b]=torch.tensor(vals); Y[b]=torch.tensor(out)
    return (T.to(DEVICE), SP.to(DEVICE), PR.to(DEVICE), X.to(DEVICE), Y.to(DEVICE))

def make_lm_batch(bs, rng):
    G = torch.full((bs, GROUND_LEN), W2I["<pad>"], dtype=torch.long)
    for b in range(bs):
        L = rng.randint(2, L_MAX)
        prims = [rng.randrange(len(PRIMS)) for _ in range(L)]   # base sees ALL skills
        vrs = [rng.choice((0,1,2)) for _ in range(L)]
        ids, _ = render(prims, vrs)
        vals = [rng.randrange(V) for _ in range(N_SLOTS)]
        out = list(vals)
        for p in prims: out = PRIMS[p][1](out)
        seq = ids + [W2I["on"]] + [W2I[str(x)] for x in vals] + \
              [W2I["gives"]] + [W2I[str(x)] for x in out]
        G[b,:len(seq)] = torch.tensor(seq)
    return G.to(DEVICE)

# ------------------------------------------------------------------ base ----
D_LM = 96
class TinyLM(nn.Module):
    def __init__(self, d=D_LM, nlayer=3, nhead=4):
        super().__init__()
        self.d = d
        self.emb = nn.Embedding(T_VOCAB, d); self.pos = nn.Embedding(GROUND_LEN, d)
        layer = nn.TransformerEncoderLayer(d, nhead, 4*d, batch_first=True,
                                           norm_first=True, dropout=0.0)
        self.enc = nn.TransformerEncoder(layer, nlayer)
        self.head = nn.Linear(d, T_VOCAB)
    def hidden(self, T):
        h = self.emb(T) + self.pos(torch.arange(T.shape[1], device=T.device))
        mask = nn.Transformer.generate_square_subsequent_mask(T.shape[1]).to(T.device)
        return self.enc(h, mask=mask)
    def forward(self, T): return self.head(self.hidden(T))
# GPU: replace with GPT-2 (transformers); keep span_reps contract [B,L,d].

def span_reps(lm, T, SP):
    with torch.no_grad(): h = lm.hidden(T)
    idx = torch.arange(T.shape[1], device=T.device)
    out = torch.zeros(SP.shape[0], SP.shape[1], lm.d, device=T.device)
    for i in range(SP.shape[1]):
        a, b = SP[:,i,0], SP[:,i,1]
        m = (idx[None,:] >= a[:,None]) & (idx[None,:] < b[:,None])
        out[:,i] = (h*m[:,:,None]).sum(1)/m.sum(1,keepdim=True).clamp(min=1)
    return out

# ------------------------------------------------------------- operators ----
D = 48; K = 8
class OperatorCore(nn.Module):
    def __init__(self, d=D, k=K):
        super().__init__()
        self.d, self.K = d, k
        def pk(*s):
            t=torch.empty(*s); nn.init.xavier_uniform_(t.view(s[0],-1)); return nn.Parameter(t)
        self.Wq=pk(k,3*d,d); self.Wk=pk(k,3*d,d); self.Wv=pk(k,3*d,d)
        self.T1=pk(k,4*d,2*d); self.T2=pk(k,2*d,d); self.Wg=pk(k,d,d)
        self.gb=nn.Parameter(torch.zeros(k,d)); self.ln=nn.LayerNorm(d)
    def forward(self, w, feat):
        h = torch.cat([self.ln(w), feat], -1)
        q = torch.einsum("bnf,kfd->bknd", h, self.Wq)
        kk= torch.einsum("bnf,kfd->bknd", h, self.Wk)
        v = torch.einsum("bnf,kfd->bknd", h, self.Wv)
        att=(torch.einsum("bknd,bkmd->bknm",q,kk)/math.sqrt(self.d)).softmax(-1)
        r = torch.einsum("bknm,bkmd->bknd", att, v)
        z = torch.cat([r, self.ln(w).unsqueeze(1).expand_as(r),
                       feat.unsqueeze(1).expand(*r.shape[:-1],2*self.d)], -1)
        z = torch.einsum("bknf,kfe->bkne", F.gelu(torch.einsum("bknf,kfe->bkne",z,self.T1)), self.T2)
        g = torch.sigmoid(torch.einsum("bknd,kde->bkne",z,self.Wg)+self.gb[None,:,None,:])
        return g*torch.tanh(z)

class Cap(nn.Module):
    """CapScheduled with an extensible operator library."""
    def __init__(self):
        super().__init__()
        self.sym=nn.Embedding(V,D); self.pos=nn.Embedding(N_SLOTS,D)
        self.core=OperatorCore()
        self.out=nn.Sequential(nn.LayerNorm(D),nn.Linear(D,2*D),nn.GELU(),nn.Linear(2*D,V))
        self.hyper=nn.Sequential(nn.LayerNorm(D_LM),nn.Linear(D_LM,D_LM),
                                 nn.GELU(),nn.Linear(D_LM,K))
        self.new_ops = nn.ModuleList()          # taught operators (1-slot cores)
        self.anchors = nn.ParameterList()       # description anchors [D_LM]
        self.anch_s  = nn.ParameterList()       # per-skill routing scale
        self.anch_b  = nn.ParameterList()       # per-skill routing bias
    def embed(self, X):
        e=F.normalize(self.sym(X),dim=-1)*math.sqrt(D)
        p=self.pos(torch.arange(N_SLOTS,device=X.device)).expand_as(e)
        return e, torch.cat([e,p],-1)
    def route_logits(self, H):
        logits=[self.hyper(H)]                                   # [...,K]
        for a,s,b in zip(self.anchors,self.anch_s,self.anch_b):
            cos=F.cosine_similarity(H, a.view(*([1]*(H.dim()-1)),-1), dim=-1)
            logits.append((s*cos+b).unsqueeze(-1))
        return torch.cat(logits,-1)
    def route(self, H):
        return F.softmax(self.route_logits(H),-1)                # [...,K+n_new]
    def step(self, w, feat, beta):
        u=self.core(w,feat)                                      # [B,K,n,d]
        upd=torch.einsum("bk,bknd->bnd",beta[...,:K],u)
        for i,op in enumerate(self.new_ops):
            upd=upd+beta[...,K+i:K+i+1,None]*op(w,feat)[:,0]
        return w+upd
    def forward(self, H, PR, X, force_beta=None):
        w,feat=self.embed(X)
        beta=self.route(H) if force_beta is None else force_beta
        live=(PR>=0).float()
        for t in range(L_MAX):
            w_new=self.step(w,feat,beta[:,t])
            w=torch.lerp(w,w_new,live[:,t:t+1,None]) if False else \
              w + live[:,t,None,None]*(w_new-w)
        return self.out(w)
    def add_skill(self, anchor):
        op=OperatorCore(k=1).to(anchor.device)
        self.new_ops.append(op)
        self.anchors.append(nn.Parameter(anchor.clone(), requires_grad=False))
        self.anch_s.append(nn.Parameter(torch.tensor(8.0, device=anchor.device)))
        self.anch_b.append(nn.Parameter(torch.tensor(-4.0, device=anchor.device)))
        return op

# ------------------------------------------------------------- teacher ------
def teacher_examples(prim, n, eps, rng):
    """Synthetic teacher: N (x,y) pairs, wrong-y with prob eps.
    GPU: replace with prompted program-of-thought generation."""
    X=torch.zeros(n,N_SLOTS,dtype=torch.long); Y=torch.zeros(n,N_SLOTS,dtype=torch.long)
    for i in range(n):
        x=[rng.randrange(V) for _ in range(N_SLOTS)]
        y=PRIMS[prim][1](x)
        if rng.random()<eps: y=[rng.randrange(V) for _ in range(N_SLOTS)]
        X[i]=torch.tensor(x); Y[i]=torch.tensor(y)
    return X.to(DEVICE), Y.to(DEVICE)

def teach(model, lm, prim, n_examples, eps, rng, steps=400, lr=3e-3, log=print):
    """Train ONE new slot on teacher pairs; library frozen; anchor = desc rep."""
    # anchor: mean rep of the taught name ACROSS program contexts (first position)
    T2,SP2,_,_,_=make_batch(32,rng,prim_pool=list(range(N_OLD)),fixed_len=3,
                            force_first=prim,first_variants=(0,))
    anchor=span_reps(lm,T2,SP2)[:,0].mean(0)
    op=model.add_skill(anchor)
    Xall,Yall=teacher_examples(prim,n_examples,eps,rng)
    params=list(op.parameters())+[model.anch_s[-1],model.anch_b[-1]]
    opt=torch.optim.AdamW(params,lr=lr)
    slot=len(model.new_ops)-1

    for it in range(steps):
        idx=torch.randint(0,n_examples,(min(128,n_examples),),device=DEVICE)
        x,y=Xall[idx],Yall[idx]
        w,feat=model.embed(x)
        beta=torch.zeros(x.shape[0],K+len(model.new_ops),device=DEVICE)
        beta[:,K+slot]=1.0
        w=model.step(w,feat,beta)
        loss=F.cross_entropy(model.out(w).reshape(-1,V), y.reshape(-1))
        # routing loss against the FULL softmax: taught-name reps (in program
        # context) must WIN the vote; old-command reps must not pick the new slot
        Tp,SPp,_,_,_=make_batch(32,rng,prim_pool=list(range(N_OLD)),fixed_len=3,
                                force_first=prim if it%2==0 else prim,
                                first_variants=(0,))
        Hp=span_reps(lm,Tp,SPp)[:,0]
        Tn,SPn,_,_,_=make_batch(48,rng,prim_pool=list(range(N_OLD)),fixed_len=2)
        Hneg=span_reps(lm,Tn,SPn)[:,:2].reshape(-1,D_LM)   # FRESH negatives each step
        rl_p=F.cross_entropy(model.route_logits(Hp),
                             torch.full((Hp.shape[0],),K+slot,device=DEVICE))
        rl_n=-torch.log1p(-model.route(Hneg)[:,K+slot].clamp(max=1-1e-6)).mean()
        rloss=rl_p+3.0*rl_n
        (loss+1.0*rloss).backward()
        opt.step(); opt.zero_grad()
        if it%100==0: log(f"    teach[{PRIMS[prim][0]}] it {it} pair-loss {loss.item():.3f}")
    return anchor

# ------------------------------------------------------------- metrics ------
def program_acc(model, lm, rng, prim_pool, variant_pool=(0,1), n=384,
                force_first=None, first_variants=None):
    model.eval()
    with torch.no_grad():
        T,SP,PR,X,Y=make_batch(n,rng,prim_pool,variant_pool,force_first=force_first,
                               first_variants=first_variants)
        H=span_reps(lm,T,SP)
        acc=(model(H,PR,X).argmax(-1)==Y).float().mean().item()
    model.train(); return acc

def novelty(model, lm, rng, n=256):
    """M4: max routing prob (frozen hyper) for old vs held-out commands."""
    with torch.no_grad():
        stats={}
        for name,pool,vp in [("old",list(range(N_OLD)),(0,1)),
                             ("new",[7,8],(0,1,2))]:
            T,SP,PR,_,_=make_batch(n,rng,pool,vp,fixed_len=2)
            H=span_reps(lm,T,SP)[:,:2].reshape(-1,D_LM)
            p=F.softmax(model.hyper(H),-1)
            stats[name]=(p.max(-1).values.mean().item(),
                         (-(p*p.clamp(min=1e-9).log()).sum(-1)).mean().item())
    return stats

# ---------------------------------------------------------------- stages ----
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--stage",required=True,choices=["lm","cap","teach","eval"])
    ap.add_argument("--steps",type=int,default=800)
    ap.add_argument("--budget",type=int,default=10**9)
    ap.add_argument("--bs",type=int,default=128)
    ap.add_argument("--seed",type=int,default=0)
    ap.add_argument("--n_ex",type=int,default=1024)
    ap.add_argument("--eps",type=float,default=0.0)
    ap.add_argument("--teach_prims",default="7,8")
    a=ap.parse_args()
    torch.manual_seed(a.seed); rng=random.Random(a.seed)
    if a.stage=="lm":
        lm=TinyLM().to(DEVICE)
        opt=torch.optim.AdamW(lm.parameters(),lr=1e-3)
        t0=time.time()
        for it in range(a.steps):
            if time.time()-t0>a.budget: break
            T=make_lm_batch(a.bs,rng)
            loss=F.cross_entropy(lm(T)[:,:-1].reshape(-1,T_VOCAB),T[:,1:].reshape(-1),
                                 ignore_index=W2I["<pad>"])
            opt.zero_grad(); loss.backward(); opt.step()
            if it%200==0: print(f"  lm {it} {loss.item():.3f}",flush=True)
        torch.save(lm.state_dict(),"e3_lm.pt"); print("saved e3_lm.pt")
    elif a.stage=="cap":
        lm=TinyLM().to(DEVICE); lm.load_state_dict(torch.load("e3_lm.pt",weights_only=False))
        for p in lm.parameters(): p.requires_grad=False
        lm.eval()
        model=Cap().to(DEVICE)
        opt=torch.optim.AdamW(model.parameters(),lr=2e-3,weight_decay=1e-4)
        sched=torch.optim.lr_scheduler.OneCycleLR(opt,2e-3,total_steps=a.steps)
        start=0
        try:
            st=torch.load("e3_cap.pt",weights_only=False)
            model.load_state_dict(st["m"]); opt.load_state_dict(st["o"])
            sched.load_state_dict(st["s"]); start=st["it"]+1; rng.setstate(st["rng"])
            print(f"  resumed {start}")
        except FileNotFoundError: pass
        t0=time.time(); it=start
        for it in range(start,a.steps):
            if time.time()-t0>a.budget: break
            T,SP,PR,X,Y=make_batch(a.bs,rng,prim_pool=list(range(N_OLD)))
            H=span_reps(lm,T,SP)
            loss=F.cross_entropy(model(H,PR,X).reshape(-1,V),Y.reshape(-1))
            opt.zero_grad(); loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(),1.0)
            opt.step(); sched.step()
            if it%150==0:
                print(f"  cap it {it} loss {loss.item():.3f} "
                      f"acc {program_acc(model,lm,rng,list(range(N_OLD))):.3f} "
                      f"({time.time()-t0:.0f}s)",flush=True)
        torch.save({"m":model.state_dict(),"o":opt.state_dict(),"s":sched.state_dict(),
                    "it":it,"rng":rng.getstate()},"e3_cap.pt")
        print(f"saved e3_cap.pt @ {it}")
    elif a.stage=="teach":
        lm=TinyLM().to(DEVICE); lm.load_state_dict(torch.load("e3_lm.pt",weights_only=False)); lm.eval()
        st=torch.load("e3_cap.pt",weights_only=False)
        model=Cap().to(DEVICE); model.load_state_dict(st["m"])
        for p in model.parameters(): p.requires_grad=False   # freeze library
        pre_old=program_acc(model,lm,rng,list(range(N_OLD)))
        print(f"M4 novelty (pre-teach): {novelty(model,lm,rng)}")
        for prim in [int(x) for x in a.teach_prims.split(",")]:
            teach(model,lm,prim,a.n_ex,a.eps,rng)
        post_old=program_acc(model,lm,rng,list(range(N_OLD)))
        print(f"M2 interference: old-prims acc pre {pre_old:.3f} post {post_old:.3f}")
        torch.save({"m":model.state_dict()},"e3_taught.pt"); print("saved e3_taught.pt")
    elif a.stage=="eval":
        lm=TinyLM().to(DEVICE); lm.load_state_dict(torch.load("e3_lm.pt",weights_only=False)); lm.eval()
        model=Cap().to(DEVICE)
        # rebuild skill slots before loading
        Z=torch.zeros(D_LM,device=DEVICE)
        st=torch.load("e3_taught.pt",weights_only=False)
        n_new=sum(1 for k in st["m"] if k.startswith("anchors."))
        for _ in range(n_new): model.add_skill(Z)
        model.load_state_dict(st["m"]); model.eval()
        for prim,name in [(7,"shl"),(8,"sq")]:
            for vp,tag in [((1,2),"UNSEEN paraphrases"),((0,),"taught name")]:
                acc=program_acc(model,lm,rng,prim_pool=list(range(N_OLD)),
                                variant_pool=(0,1),force_first=prim,first_variants=vp)
                print(f"M1 [{name}] mixed programs, invoked via {tag}: {acc:.3f}")
        print(f"baseline old-only (var 0,1): "
              f"{program_acc(model,lm,rng,list(range(N_OLD))):.3f}")

if __name__=="__main__":
    main()
