#!/usr/bin/env python3
import csv, hashlib, json, os, subprocess, sys, time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

CELLS = ((1.0,0.0,0),(1.0,0.35,3),(1.0,0.80,5),(2.0,0.15,1),
         (2.0,0.60,5),(5.0,0.0,3),(5.0,0.15,5),(5.0,0.80,1))
SEEDS=(101,103,107); CONTROLS=("appraisal","linear","shuffled"); STRATA=("core4","roles8")

def task(x):
    gain,coupling,delay,seed,control=x
    root=os.environ["OMEGASIM_EXPERIMENT_REPO"]
    if root not in sys.path: sys.path.insert(0,root)
    from omegasim.a6_model import A6Params, simulate
    from scripts.run_cla_detector import evaluate_trace
    retained=simulate(A6Params(seed=seed,steps=1024,gain=gain,coupling=coupling,delay=delay,control=control))["rows"][128:]
    out=[]
    for stratum in STRATA:
        r=evaluate_trace(retained,stratum=stratum,seed=seed,surrogates=5)
        r.update(seed=seed,gain=gain,coupling=coupling,delay=delay,control=control,stratum=stratum)
        out.append(r)
    return out

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
    run=Path(__file__).resolve().parent; art=run/"artifacts"; art.mkdir(exist_ok=True)
    omega=Path("/home/openclaw/research-agent/projects/omegasim/repos/omegasim")
    chaos=Path("/home/openclaw/research-agent/projects/omegasim/repos/chaoslang-frozen-974af31")
    pins=((omega,"18c7408fe48eeac9e9ec53f18eb5b2d0ed840e2d"),(chaos,"974af31efaf6e3cc239252f78367d20e657ac45c"))
    for repo,pin in pins:
        got=subprocess.check_output(["git","-C",str(repo),"rev-parse","HEAD"],text=True).strip()
        dirty=subprocess.check_output(["git","-C",str(repo),"status","--porcelain=v1"],text=True)
        if got != pin or dirty: raise SystemExit(f"frozen identity failure: {repo}: {got}, dirty={bool(dirty)}")
    env=os.environ.copy(); env["PYTHONPATH"]=f"{omega/'src'}:{chaos/'src'}"
    subprocess.run([sys.executable,"-m","unittest","discover","-s","tests","-v"],cwd=omega,env=env,check=True,
                   stdout=(run/"tests.stdout.log").open("w"),stderr=(run/"tests.stderr.log").open("w"))
    os.environ["OMEGASIM_EXPERIMENT_REPO"]=str(omega)
    jobs=[(*cell,seed,control) for cell in CELLS for seed in SEEDS for control in CONTROLS]
    rows=[]; started=time.monotonic()
    with ProcessPoolExecutor(max_workers=4) as pool:
        for f in as_completed([pool.submit(task,j) for j in jobs]): rows.extend(f.result())
    rows.sort(key=lambda r:(float(r["gain"]),float(r["coupling"]),int(r["delay"]),int(r["seed"]),r["control"],r["stratum"]))
    keys=("gain","coupling","delay","seed","stratum")
    lookup={tuple(r[k] for k in keys)+(r["control"],):r for r in rows}
    deltas=[]
    for r in rows:
        if r["control"]!="appraisal": continue
        item={k:r[k] for k in keys}
        item.update(productions=r["productions"],categories=r["categories"],
                    priority=(int(r["productions"])>2 or int(r["categories"])>0))
        for c in ("linear","shuffled"):
            q=lookup[tuple(r[k] for k in keys)+(c,)]
            item[f"margin_delta_vs_{c}"]=float(r["compression_margin_proxy_bits"])-float(q["compression_margin_proxy_bits"])
            item[f"heldout_delta_vs_{c}"]=float(r["heldout_advantage_bits_per_symbol"])-float(q["heldout_advantage_bits_per_symbol"])
        deltas.append(item)
    payload={"schema":"omegasim.a6_stratified_cla_resweep.v1","cells":CELLS,"seeds":SEEDS,"controls":CONTROLS,
             "strata":STRATA,"steps":1024,"burn":128,"surrogates":5,"elapsed_seconds":round(time.monotonic()-started,3),
             "rows":rows,"appraisal_control_deltas":deltas,"priority_rows":[d for d in deltas if d["priority"]]}
    jp=art/"results.json"; jp.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
    with (art/"results.csv").open("w",newline="") as h:
        w=csv.DictWriter(h,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    (run/"artifact_sha256.json").write_text(json.dumps({p.name:sha(p) for p in sorted(art.iterdir())},indent=2,sort_keys=True)+"\n")
    print(json.dumps({"cells":len(CELLS),"rows":len(rows),"priority_rows":len(payload["priority_rows"]),
                      "production_counts":sorted(set(int(r["productions"]) for r in rows)),
                      "category_counts":sorted(set(int(r["categories"]) for r in rows)),"elapsed_seconds":payload["elapsed_seconds"]},sort_keys=True))
if __name__=="__main__": main()
