#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/hdc-cgcct-transformers/repos/hdc-cgcct-probes
python3 -c import\ json\;\ from\ scripts.run_p0_capacity\ import\ cell\;\ print\(json.dumps\(\[cell\(d\,k\,m\,128\,12011\)\ for\ d\ in\ \(32\,64\,128\,256\,512\,1024\)\ for\ k\ in\ \(32\,64\,128\)\ for\ m\ in\ \(256\,1024\)\]\,\ sort_keys=True\)\) 
