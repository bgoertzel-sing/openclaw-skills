"""
hdc_musicgen_experiments.py
============================================================================
HDC x pretrained music generation: four staged experiments on MusicGen
(facebook/musicgen-small by default), designed for a single RunPod GPU.

Stages (run in order; each caches results to OUT_DIR so reruns are cheap):

  stage0  Tokenize a directory of music audio with MusicGen's EnCodec
          (4 codebooks x 2048, 50 Hz) and cache codes to disk.
          Also reports token persistence stats (the warm-start resource).

  stageA  CONTEXT-VALUE CURVE (no training). Teacher-forced NLL of a fixed
          evaluation span as a function of preceding context length
          (1s..60s). This is the Delta_fact go/no-go: if NLL saturates by
          W seconds, everything older is compressible in principle, and the
          gap between W and full context is the budget an HDC history
          summary can try to recover in stageD.

  stageB  HEAD INTERFACE (trains linear probes only, backbone frozen).
          From the LM's final hidden states, train (i) 4 independent
          per-codebook softmax probes and (ii) ONE linear map to a
          role-bound HDC bundle target decoded by 4 parallel
          unbind+cleanups. Compares aligned-frame token accuracy, NLL
          proxy, parameter counts, and decode wall-clock. Both interfaces
          see identical inputs and targets, so the comparison isolates the
          output interface exactly.

  stageC  PRODUCT-STATE RESONATOR FEASIBILITY (no training). Using real
          EnCodec token streams: encode each frame as a bound product of
          4 factor atoms (|C|=2048 each; product space ~1.8e13), corrupt
          with additive noise at several SNRs, and measure exact-frame
          recovery by resonator decoding, cold start vs warm start at the
          previous frame's tokens. Tests basin entry via real music token
          dynamics.

  stageD  HDC HISTORY ADAPTER (trains a small adapter, backbone frozen).
          Truncate self-attention context to W seconds; build a fixed-width
          HDC summary of everything older (coarse-codebook tokens, bucket
          roles); map it through a small MLP into a sequence of
          cross-attention condition embeddings (injected where MusicGen
          normally receives text conditioning); train the adapter to
          minimize teacher-forced NLL. Report NLL: truncated vs
          truncated+adapter vs full-context, i.e. what fraction of the
          long-context value a fixed-width HDC memory recovers.

Setup on RunPod (tested target: 1x GPU with >= 16 GB, e.g. A10/3090/4090;
musicgen-small needs ~4 GB for inference, stageD ~10-14 GB while training):

    pip install -U pip
    pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121
    pip install audiocraft==1.3.0
    python hdc_musicgen_experiments.py stage0 --audio_dir /path/to/music
    python hdc_musicgen_experiments.py stageA
    python hdc_musicgen_experiments.py stageB
    python hdc_musicgen_experiments.py stageC
    python hdc_musicgen_experiments.py stageD

Data: point --audio_dir at a directory of music files (wav/mp3/flac). For
the long-context stages to mean anything, use LONG tracks: >= 20 tracks of
>= 2 minutes is a reasonable minimum; more is better.

Smoke test everything first with:  --limit 4 --max_seconds 40

HONESTY NOTES
  * Written against audiocraft 1.3.0. The two most version-fragile points
    are (1) obtaining null/text condition tensors and (2) the signature of
    lm.compute_predictions; both are wrapped in helpers below with
    fallbacks and loud errors. If audiocraft drifts, fix those two helpers
    first.
  * stageB trains fresh probes for BOTH interfaces on identical
    (hidden_state -> aligned next-frame tokens) pairs; it does not reuse
    the teacher's own delay-pattern heads, precisely so the interface
    comparison is internally fair and independent of delay bookkeeping.
============================================================================
"""

import argparse, json, math, os, sys, time, glob
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

# ---------------------------------------------------------------------------
# Config / CLI
# ---------------------------------------------------------------------------
P = argparse.ArgumentParser()
P.add_argument("stage", choices=["stage0", "stageA", "stageB", "stageC", "stageD"])
P.add_argument("--audio_dir", type=str, default=None)
P.add_argument("--out_dir", type=str, default="./hdc_mg_out")
P.add_argument("--model", type=str, default="facebook/musicgen-small")
P.add_argument("--device", type=str,
               default="cuda" if torch.cuda.is_available() else "cpu")
P.add_argument("--limit", type=int, default=None,
               help="max number of tracks (smoke test)")
P.add_argument("--max_seconds", type=int, default=180,
               help="truncate each track to this many seconds")
P.add_argument("--eval_seconds", type=float, default=5.0,
               help="length of the evaluation span for NLL measurements")
P.add_argument("--contexts", type=str, default="1,2,5,10,20,40,60",
               help="context lengths in seconds for stageA")
P.add_argument("--hdc_D", type=int, default=8192, help="hypervector dim")
P.add_argument("--bundle_D", type=int, default=8192,
               help="bundle-head target dim for stageB")
P.add_argument("--probe_steps", type=int, default=2000)
P.add_argument("--adapter_steps", type=int, default=4000)
P.add_argument("--adapter_window", type=float, default=10.0,
               help="stageD truncated self-context, seconds")
P.add_argument("--adapter_tokens", type=int, default=16,
               help="number of cross-attn condition vectors from summary")
P.add_argument("--batch", type=int, default=4)
P.add_argument("--seed", type=int, default=0)
ARGS = P.parse_args()
torch.manual_seed(ARGS.seed)
np.random.seed(ARGS.seed)
os.makedirs(ARGS.out_dir, exist_ok=True)
FRAME_RATE = 50  # EnCodec @32kHz in MusicGen

def log(*a):
    print(f"[{ARGS.stage}]", *a, flush=True)

def save_json(name, obj):
    with open(os.path.join(ARGS.out_dir, name), "w") as f:
        json.dump(obj, f, indent=2)
    log("wrote", name)

# ---------------------------------------------------------------------------
# Model loading + version-fragile helpers (fix here first if audiocraft drifts)
# ---------------------------------------------------------------------------
def load_model():
    from audiocraft.models import MusicGen
    log("loading", ARGS.model, "on", ARGS.device)
    model = MusicGen.get_pretrained(ARGS.model, device=ARGS.device)
    model.compression_model.eval()
    model.lm.eval()
    return model

def null_condition_tensors(lm, batch_size):
    """Condition tensors for 'no text' (CFG-null) conditioning.
    FRAGILE: audiocraft API point #1."""
    from audiocraft.modules.conditioners import ConditioningAttributes
    attrs = [ConditioningAttributes(text={"description": None})
             for _ in range(batch_size)]
    try:
        tokenized = lm.condition_provider.tokenize(attrs)
        return lm.condition_provider(tokenized)
    except Exception as e:
        raise RuntimeError(
            "Could not build null condition tensors; audiocraft API may "
            "have drifted. Inspect lm.condition_provider usage in "
            "audiocraft/models/lm.py and adapt null_condition_tensors(). "
            f"Original error: {e}")

def teacher_nll(lm, codes, condition_tensors=None, eval_from=0):
    """Teacher-forced mean NLL (nats/token) over frames >= eval_from.
    codes: (B, K, T) long. FRAGILE: audiocraft API point #2."""
    if condition_tensors is None:
        condition_tensors = null_condition_tensors(lm, codes.shape[0])
    with torch.no_grad():
        out = lm.compute_predictions(codes, conditions=[],
                                     condition_tensors=condition_tensors)
    logits, mask = out.logits, out.mask  # (B,K,T,card), (B,K,T)
    lp = F.log_softmax(logits.float(), dim=-1)
    nll = -lp.gather(-1, codes.unsqueeze(-1)).squeeze(-1)  # (B,K,T)
    m = mask.clone()
    m[:, :, :eval_from] = False
    return (nll * m).sum().item() / max(m.sum().item(), 1)

def nll_with_grad(lm, codes, condition_tensors, eval_from):
    out = lm.compute_predictions(codes, conditions=[],
                                 condition_tensors=condition_tensors)
    lp = F.log_softmax(out.logits.float(), dim=-1)
    nll = -lp.gather(-1, codes.unsqueeze(-1)).squeeze(-1)
    m = out.mask.clone()
    m[:, :, :eval_from] = False
    return (nll * m).sum() / m.sum().clamp(min=1)

# ---------------------------------------------------------------------------
# stage0: tokenize audio
# ---------------------------------------------------------------------------
def stage0():
    assert ARGS.audio_dir, "--audio_dir required for stage0"
    import torchaudio
    from audiocraft.data.audio_utils import convert_audio
    model = load_model()
    sr, ch = model.sample_rate, model.audio_channels
    files = sorted(sum([glob.glob(os.path.join(ARGS.audio_dir, "**", ext),
                                  recursive=True)
                        for ext in ("*.wav", "*.mp3", "*.flac", "*.ogg")], []))
    if ARGS.limit:
        files = files[:ARGS.limit]
    assert files, f"no audio files found under {ARGS.audio_dir}"
    log(f"{len(files)} files")
    all_codes, meta = [], []
    for f in files:
        try:
            wav, fsr = torchaudio.load(f)
        except Exception as e:
            log("skip (load fail)", f, e); continue
        wav = convert_audio(wav, fsr, sr, ch)
        wav = wav[..., : sr * ARGS.max_seconds]
        if wav.shape[-1] < sr * 15:
            log("skip (<15 s)", f); continue
        with torch.no_grad():
            codes, _ = model.compression_model.encode(
                wav.unsqueeze(0).to(ARGS.device))
        codes = codes.squeeze(0).cpu()  # (K, T)
        all_codes.append(codes)
        meta.append({"file": f, "frames": int(codes.shape[-1])})
        log(f, "->", tuple(codes.shape))
    torch.save(all_codes, os.path.join(ARGS.out_dir, "codes.pt"))
    save_json("codes_meta.json", meta)
    # persistence stats = warm-start resource
    per = []
    for c in all_codes:
        per.append((c[:, 1:] == c[:, :-1]).float().mean(dim=1).numpy())
    per = np.stack(per).mean(0)
    log("P(token_t == token_{t-1}) per codebook:", np.round(per, 3))
    save_json("stage0_persistence.json",
              {"per_codebook": per.tolist(), "n_tracks": len(all_codes)})

# ---------------------------------------------------------------------------
# stageA: context-value curve
# ---------------------------------------------------------------------------
def stageA():
    model = load_model()
    lm = model.lm
    codes_list = torch.load(os.path.join(ARGS.out_dir, "codes.pt"))
    ctxs = [float(c) for c in ARGS.contexts.split(",")]
    ev = int(ARGS.eval_seconds * FRAME_RATE)
    results = {c: [] for c in ctxs + ["full"]}
    for ci, codes in enumerate(codes_list):
        T = codes.shape[-1]
        # evaluation spans anchored deep enough for the longest context
        max_ctx = int(max(ctxs) * FRAME_RATE)
        anchors = list(range(max_ctx, T - ev, max(ev, 1)))[:6]
        if not anchors:
            continue
        for t0 in anchors:
            for c in ctxs:
                W = int(c * FRAME_RATE)
                seg = codes[:, t0 - W: t0 + ev].unsqueeze(0).to(ARGS.device)
                results[c].append(teacher_nll(lm, seg, eval_from=W))
            seg = codes[:, : t0 + ev].unsqueeze(0).to(ARGS.device)
            results["full"].append(teacher_nll(lm, seg, eval_from=t0))
        log(f"track {ci+1}/{len(codes_list)} done")
    summary = {str(k): float(np.mean(v)) for k, v in results.items() if v}
    log("mean NLL (nats/token) by context seconds:")
    for k in ctxs + ["full"]:
        if str(k) in summary:
            log(f"   {k:>6}: {summary[str(k)]:.4f}")
    if str(ctxs[-1]) in summary and "full" in summary:
        gap = summary[str(ARGS.adapter_window)] - summary["full"] \
            if str(ARGS.adapter_window) in summary else None
        if gap is not None:
            log(f"Delta_fact budget at W={ARGS.adapter_window}s "
                f"(truncated - full): {gap:.4f} nats/token "
                f"-> this is what stageD's HDC summary tries to recover")
    save_json("stageA_context_curve.json", summary)

# ---------------------------------------------------------------------------
# hidden-state extraction (shared by stageB)
# ---------------------------------------------------------------------------
def extract_hidden_and_targets(model, codes_list, max_pairs=60000,
                               seg_frames=1000):
    """Returns H (n, d_model) hidden states at position t and Y (n, K)
    aligned next-frame tokens codes[:, t+1]. Uses a forward hook on the
    LM's final norm."""
    lm = model.lm
    feats, targs = [], []
    buf = {}
    norm = getattr(lm, "out_norm", None)
    assert norm is not None, \
        "lm.out_norm not found; hook the last transformer block output instead"
    h = norm.register_forward_hook(
        lambda mod, i, o: buf.__setitem__("h", o.detach()))
    try:
        for codes in codes_list:
            T = codes.shape[-1]
            for s in range(0, T - seg_frames - 1, seg_frames):
                seg = codes[:, s: s + seg_frames].unsqueeze(0).to(ARGS.device)
                _ = teacher_nll(lm, seg)  # forward populates the hook
                hid = buf["h"].squeeze(0).float().cpu()  # (T', d)
                Tm = min(hid.shape[0], seg_frames) - 1
                feats.append(hid[:Tm])
                targs.append(codes[:, s + 1: s + 1 + Tm].T.cpu())  # (Tm, K)
                if sum(x.shape[0] for x in feats) >= max_pairs:
                    raise StopIteration
    except StopIteration:
        pass
    finally:
        h.remove()
    H = torch.cat(feats)[:max_pairs]
    Y = torch.cat(targs)[:max_pairs]
    log("hidden/target pairs:", tuple(H.shape), tuple(Y.shape))
    return H, Y

# ---------------------------------------------------------------------------
# stageB: head interface comparison
# ---------------------------------------------------------------------------
def stageB():
    model = load_model()
    codes_list = torch.load(os.path.join(ARGS.out_dir, "codes.pt"))
    H, Y = extract_hidden_and_targets(model, codes_list)
    n = H.shape[0]; K = Y.shape[1]; card = 2048
    ntr = int(n * 0.9)
    Htr, Hte = H[:ntr].to(ARGS.device), H[ntr:].to(ARGS.device)
    Ytr, Yte = Y[:ntr].to(ARGS.device), Y[ntr:].to(ARGS.device)
    d_model = H.shape[1]

    # ---- (i) 4 independent softmax probes ----
    probes = nn.ModuleList([nn.Linear(d_model, card) for _ in range(K)]
                           ).to(ARGS.device)
    opt = torch.optim.Adam(probes.parameters(), lr=1e-3)
    for step in range(ARGS.probe_steps):
        idx = torch.randint(0, ntr, (256,), device=ARGS.device)
        loss = sum(F.cross_entropy(probes[k](Htr[idx]), Ytr[idx, k])
                   for k in range(K))
        opt.zero_grad(); loss.backward(); opt.step()
    with torch.no_grad():
        t0 = time.time()
        predA = torch.stack([probes[k](Hte).argmax(-1) for k in range(K)], 1)
        dtA = (time.time() - t0) / len(Hte)
    accA = (predA == Yte).float().mean(0).cpu().numpy()
    exA = (predA == Yte).all(1).float().mean().item()
    paramsA = K * d_model * card

    # ---- (ii) single bundle-head projection ----
    D = ARGS.bundle_D
    g = torch.Generator().manual_seed(1)
    atoms = [torch.randint(0, 2, (card, D), generator=g).float().mul_(2).sub_(1)
             for _ in range(K)]
    roles = [torch.randint(0, 2, (1, D), generator=g).float().mul_(2).sub_(1)
             for _ in range(K)]
    atoms_d = [a.to(ARGS.device) for a in atoms]
    roles_d = [r.to(ARGS.device) for r in roles]
    def bundle_target(Yb):
        out = torch.zeros(len(Yb), D, device=ARGS.device)
        for k in range(K):
            out += roles_d[k] * atoms_d[k][Yb[:, k]]
        return out
    head = nn.Linear(d_model, D).to(ARGS.device)
    opt = torch.optim.Adam(head.parameters(), lr=1e-3)
    for step in range(ARGS.probe_steps):
        idx = torch.randint(0, ntr, (256,), device=ARGS.device)
        loss = F.mse_loss(head(Htr[idx]), bundle_target(Ytr[idx]))
        opt.zero_grad(); loss.backward(); opt.step()
    with torch.no_grad():
        t0 = time.time()
        Hh = head(Hte)
        predB = torch.stack(
            [((Hh * roles_d[k]) @ atoms_d[k].T).argmax(-1) for k in range(K)], 1)
        dtB = (time.time() - t0) / len(Hte)
    accB = (predB == Yte).float().mean(0).cpu().numpy()
    exB = (predB == Yte).all(1).float().mean().item()
    paramsB = d_model * D

    res = {
        "multi_head": {"per_codebook_acc": accA.tolist(), "exact": exA,
                       "decode_ms_per_frame": dtA * 1e3,
                       "head_params": paramsA},
        "bundle_head": {"per_codebook_acc": accB.tolist(), "exact": exB,
                        "decode_ms_per_frame": dtB * 1e3,
                        "head_params": paramsB, "D": D},
        "note": ("identical inputs/targets for both interfaces; bundle head "
                 "uses ONE projection and decodes all K codebooks of the "
                 "same frame in parallel (no delay pattern)")}
    log(json.dumps(res, indent=2))
    save_json("stageB_heads.json", res)

# ---------------------------------------------------------------------------
# stageC: product-state resonator feasibility on real token streams
# ---------------------------------------------------------------------------
def stageC():
    codes_list = torch.load(os.path.join(ARGS.out_dir, "codes.pt"))
    K, card, D = 4, 2048, ARGS.hdc_D
    dev = ARGS.device
    g = torch.Generator().manual_seed(2)
    atoms = [torch.randint(0, 2, (card, D), generator=g).float()
             .mul_(2).sub_(1).to(dev) for _ in range(K)]
    # sample (prev, cur) frame pairs across tracks
    pairs = []
    for c in codes_list:
        T = c.shape[-1]
        ts = np.random.choice(np.arange(1, T), size=min(200, T - 1),
                              replace=False)
        for t in ts:
            pairs.append((c[:, t - 1].numpy(), c[:, t].numpy()))
    pairs = pairs[:2000]
    prev = torch.tensor(np.array([p for p, _ in pairs]), device=dev)
    cur = torch.tensor(np.array([q for _, q in pairs]), device=dev)
    n = len(cur)
    Hp = torch.ones(n, D, device=dev)
    for k in range(K):
        Hp *= atoms[k][cur[:, k]]
    results = {}
    for snr_db in (20, 10, 6, 3, 0):
        noise = torch.randn(n, D, device=dev)
        noise *= Hp.norm(dim=1, keepdim=True) / noise.norm(dim=1, keepdim=True) \
            * (10 ** (-snr_db / 20))
        Hn = Hp + noise
        for name, init in (("cold", None), ("warm_prev", prev)):
            Xh = [atoms[k].mean(0).expand(n, D).clone() if init is None
                  else atoms[k][init[:, k]].clone() for k in range(K)]
            for _ in range(16):
                for f in range(K):
                    Z = Hn.clone()
                    for gk in range(K):
                        if gk != f:
                            Z = Z * torch.sign(Xh[gk] + 1e-9)
                    A = Z @ atoms[f].T
                    Xh[f] = A @ atoms[f]
            pred = torch.stack(
                [(torch.sign(Xh[k]) @ atoms[k].T).argmax(-1)
                 for k in range(K)], 1)
            ex = (pred == cur).all(1).float().mean().item()
            results[f"snr{snr_db}_{name}"] = ex
            log(f"SNR {snr_db:>2} dB, {name:9s}: exact-frame {ex:.3f}")
    save_json("stageC_resonator.json",
              {"D": D, "K": K, "card": card, "results": results})

# ---------------------------------------------------------------------------
# stageD: HDC history adapter
# ---------------------------------------------------------------------------
class SummaryAdapter(nn.Module):
    """HDC history summary -> P cross-attention condition embeddings."""
    def __init__(self, D_in, d_model, P_tokens):
        super().__init__()
        self.P = P_tokens
        self.net = nn.Sequential(
            nn.Linear(D_in, 2048), nn.GELU(),
            nn.Linear(2048, d_model * P_tokens))
        self.d = d_model
    def forward(self, s):                      # (B, D_in)
        return self.net(s).view(-1, self.P, self.d)

def build_summary(codes, upto, D, atoms0, buckets):
    """Fixed-width HDC code of frames [0, upto): coarse-codebook tokens
    role-bound by log-spaced temporal bucket."""
    if upto <= 0:
        return torch.zeros(D)
    tok = codes[0, :upto]                       # coarse codebook
    pos = torch.arange(upto, dtype=torch.float)
    rel = 1.0 - pos / max(upto, 1)              # 0 = now, 1 = start
    b = torch.clamp((torch.log2(rel * upto + 1) /
                     math.log2(upto + 1) * (buckets.shape[0] - 1)).long(),
                    0, buckets.shape[0] - 1)
    acc = (buckets[b] * atoms0[tok]).sum(0)
    return torch.sign(acc + 1e-9)

def stageD():
    model = load_model()
    lm = model.lm
    for p in lm.parameters():
        p.requires_grad_(False)
    codes_list = torch.load(os.path.join(ARGS.out_dir, "codes.pt"))
    D = ARGS.hdc_D
    g = torch.Generator().manual_seed(3)
    atoms0 = torch.randint(0, 2, (2048, D), generator=g).float().mul_(2).sub_(1)
    buckets = torch.randint(0, 2, (12, D), generator=g).float().mul_(2).sub_(1)
    W = int(ARGS.adapter_window * FRAME_RATE)
    ev = int(ARGS.eval_seconds * FRAME_RATE)
    d_model = lm.transformer.layers[0].self_attn.embed_dim \
        if hasattr(lm.transformer.layers[0], "self_attn") else \
        lm.condition_provider.output_dim if hasattr(
            lm.condition_provider, "output_dim") else 1024
    adapter = SummaryAdapter(D, d_model, ARGS.adapter_tokens).to(ARGS.device)
    opt = torch.optim.Adam(adapter.parameters(), lr=3e-4)

    def sample_batch(B):
        segs, sums = [], []
        while len(segs) < B:
            c = codes_list[np.random.randint(len(codes_list))]
            T = c.shape[-1]
            if T < W + ev + 2 * W:
                continue
            t0 = np.random.randint(W * 2, T - ev)
            segs.append(c[:, t0 - W: t0 + ev])
            sums.append(build_summary(c, t0 - W, D, atoms0, buckets))
        return (torch.stack(segs).to(ARGS.device),
                torch.stack(sums).to(ARGS.device))

    def cond_from_summary(s):
        """FRAGILE: injects adapter output where text conditioning goes.
        MusicGen's LM consumes condition_tensors['description'] as a
        (tensor, mask) pair feeding cross-attention."""
        emb = adapter(s)
        mask = torch.ones(emb.shape[:2], dtype=torch.bool,
                          device=emb.device)
        return {"description": (emb, mask)}

    # training
    for step in range(ARGS.adapter_steps):
        seg, s = sample_batch(ARGS.batch)
        loss = nll_with_grad(lm, seg, cond_from_summary(s), eval_from=W)
        opt.zero_grad(); loss.backward(); opt.step()
        if step % 200 == 0:
            log(f"step {step}: train NLL {loss.item():.4f}")

    # evaluation: truncated / truncated+adapter / full
    nll_tr, nll_ad, nll_full = [], [], []
    with torch.no_grad():
        for _ in range(60):
            c = codes_list[np.random.randint(len(codes_list))]
            T = c.shape[-1]
            if T < 3 * W + ev:
                continue
            t0 = np.random.randint(2 * W, T - ev)
            seg = c[:, t0 - W: t0 + ev].unsqueeze(0).to(ARGS.device)
            s = build_summary(c, t0 - W, D, atoms0, buckets) \
                .unsqueeze(0).to(ARGS.device)
            nll_tr.append(teacher_nll(lm, seg, eval_from=W))
            nll_ad.append(teacher_nll(lm, seg, cond_from_summary(s),
                                      eval_from=W))
            fullseg = c[:, : t0 + ev].unsqueeze(0).to(ARGS.device)
            nll_full.append(teacher_nll(lm, fullseg, eval_from=t0))
    res = {"W_seconds": ARGS.adapter_window,
           "nll_truncated": float(np.mean(nll_tr)),
           "nll_truncated_plus_HDC_adapter": float(np.mean(nll_ad)),
           "nll_full_context": float(np.mean(nll_full))}
    gap = res["nll_truncated"] - res["nll_full_context"]
    rec = res["nll_truncated"] - res["nll_truncated_plus_HDC_adapter"]
    res["long_context_gap"] = gap
    res["fraction_recovered_by_HDC_summary"] = rec / gap if gap > 1e-6 else None
    log(json.dumps(res, indent=2))
    save_json("stageD_adapter.json", res)

# ---------------------------------------------------------------------------
if __name__ == "__main__":
    {"stage0": stage0, "stageA": stageA, "stageB": stageB,
     "stageC": stageC, "stageD": stageD}[ARGS.stage]()
