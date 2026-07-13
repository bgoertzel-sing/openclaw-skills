#!/usr/bin/env bash
set -euo pipefail
KIT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
echo '[1/6] shell syntax'
while IFS= read -r -d '' f; do bash -n "$f"; done < <(find "$KIT/scripts" -type f -name '*.sh' -print0)
echo '[2/6] python syntax'
while IFS= read -r -d '' f; do python3 -m py_compile "$f"; done < <(find "$KIT" -type f -name '*.py' -print0)
find "$KIT" -type d -name __pycache__ -prune -exec rm -rf {} +
echo '[3/6] plugin tests'
if command -v node >/dev/null && [[ -f "$KIT/plugins/intent-model-router/index.test.js" ]]; then (cd "$KIT/plugins/intent-model-router" && node --test index.test.js); fi
echo '[4/6] forbidden private/runtime files'
if find "$KIT" -type f \( -name '*.session' -o -name '*.sqlite*' -o -name '*.db' -o -name '*.pid' -o -name '*.log' -o -name 'openclaw.json' -o -name '.env' \) | grep -q .; then
  echo 'Forbidden runtime files found:' >&2; find "$KIT" -type f \( -name '*.session' -o -name '*.sqlite*' -o -name '*.db' -o -name '*.pid' -o -name '*.log' -o -name 'openclaw.json' -o -name '.env' \) >&2; exit 1
fi
echo '[5/6] secret/private-identity scan'
if find "$KIT" -type f ! -name MANIFEST.sha256 ! -path "$KIT/scripts/verify-kit.sh" -print0 | \
 xargs -0 rg -n '(BEGIN (RSA|OPENSSH|EC|PGP) PRIVATE KEY|[0-9]{8,12}:[A-Za-z0-9_-]{30,}|sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16}|/home/openclaw|402314199|5459676079|3983157420|8927136413|8562797306)'; then
  echo 'Potential secret/private identity material found.' >&2; exit 1
fi
echo '[6/6] optional patch check'
if [[ -n "${OMEGA_BASE_REPO:-}" ]]; then git -C "$OMEGA_BASE_REPO" apply --check "$KIT/patches/omegaclaw/omega-runtime-botapi10.patch"; else echo 'skip (set OMEGA_BASE_REPO to clean pinned checkout)'; fi
echo 'VERIFY_KIT_OK'
