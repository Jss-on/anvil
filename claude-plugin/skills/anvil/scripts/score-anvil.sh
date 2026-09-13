#!/usr/bin/env bash
# Compatibility entry point; all validation lives in the standard-library Python seam.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -n "${ANVIL_PYTHON:-}" ]]; then exec "$ANVIL_PYTHON" "$ROOT/anvil.py" "$@"; fi
if command -v python3 >/dev/null 2>&1 && python3 -c 'import sys; assert sys.version_info >= (3,10)' >/dev/null 2>&1; then
  exec python3 "$ROOT/anvil.py" "$@"
fi
if command -v py >/dev/null 2>&1 && py -3 -c 'import sys; assert sys.version_info >= (3,10)' >/dev/null 2>&1; then
  exec py -3 "$ROOT/anvil.py" "$@"
fi
if command -v uv >/dev/null 2>&1; then exec uv run --no-project --offline python "$ROOT/anvil.py" "$@"; fi
echo 'ANVIL_ERROR: Python 3.10+ required; set ANVIL_PYTHON or install Python.' >&2
exit 2
