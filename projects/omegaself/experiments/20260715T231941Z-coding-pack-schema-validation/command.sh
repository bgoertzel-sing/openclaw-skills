#!/usr/bin/env bash
set -euo pipefail
cd projects/omegaself/repos/omegaself-coding-agent-pack
env PATH=/home/openclaw/research-agent/projects/protomegabot2/repos/PeTTa/.venv/bin:/usr/bin:/bin python -c import\ json\,\ pathlib\;\ from\ jsonschema.validators\ import\ Draft202012Validator\;\ paths=sorted\(pathlib.Path\(\"schemas\"\).glob\(\"\*.json\"\)\)\;\ assert\ len\(paths\)==21\,\ len\(paths\)\;\ \[Draft202012Validator.check_schema\(json.loads\(path.read_text\(\)\)\)\ for\ path\ in\ paths\]\;\ print\(f\"validated\ \{len\(paths\)\}\ Draft\ 2020-12\ schemas\"\) 
