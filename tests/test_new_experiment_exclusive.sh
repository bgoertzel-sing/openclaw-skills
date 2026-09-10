#!/usr/bin/env bash
set -euo pipefail

ROOT=$(mktemp -d)
trap 'rm -rf "$ROOT"' EXIT
mkdir -p "$ROOT/projects/omegasim/experiments" "$ROOT/fake-bin" "$ROOT/bin"
ln -s /home/openclaw/research-agent/bin/capture-environment "$ROOT/bin/capture-environment"

cat > "$ROOT/fake-bin/date" <<'EOF'
#!/usr/bin/env bash
case " $* " in
  *" +%Y-%m-%dT%H:%M:%SZ "*) printf '%s\n' '2026-07-17T02:45:00Z' ;;
  *" +%Y%m%dT%H%M%SZ "*) printf '%s\n' '20260717T024500Z' ;;
  *) exec /usr/bin/date "$@" ;;
esac
EOF
chmod +x "$ROOT/fake-bin/date"

PATH="$ROOT/fake-bin:$PATH" RESEARCH_AGENT_ROOT="$ROOT" \
  /home/openclaw/research-agent/bin/new-experiment omegasim exclusive-smoke \
  --cwd /home/openclaw/research-agent -- /usr/bin/true >/dev/null

set +e
OUTPUT=$(PATH="$ROOT/fake-bin:$PATH" RESEARCH_AGENT_ROOT="$ROOT" \
  /home/openclaw/research-agent/bin/new-experiment omegasim exclusive-smoke \
  --cwd /home/openclaw/research-agent -- /usr/bin/true 2>&1)
STATUS=$?
set -e

test "$STATUS" -eq 1
case "$OUTPUT" in
  *"Refusing to reuse experiment directory"*) ;;
  *) printf 'unexpected output: %s\n' "$OUTPUT" >&2; exit 1 ;;
esac
