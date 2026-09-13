#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ -n "${ANVIL_PYTHON:-}" ]]; then exec "$ANVIL_PYTHON" -B "$ROOT/tests/test_anvil.py" "$@"; fi
if command -v python3 >/dev/null 2>&1 && python3 -c 'import sys; assert sys.version_info >= (3,10)' >/dev/null 2>&1; then
  exec python3 -B "$ROOT/tests/test_anvil.py" "$@"
fi
if command -v py >/dev/null 2>&1 && py -3 -c 'import sys; assert sys.version_info >= (3,10)' >/dev/null 2>&1; then
  exec py -3 -B "$ROOT/tests/test_anvil.py" "$@"
fi
if command -v uv >/dev/null 2>&1; then exec uv run --no-project --offline python -B "$ROOT/tests/test_anvil.py" "$@"; fi
echo 'Python 3.10+ required for tests' >&2
exit 2
