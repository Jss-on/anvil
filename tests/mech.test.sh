#!/usr/bin/env bash
set -euo pipefail
case "${1:-}" in ''|mesh|fit|mass|mech-dfm) ;; *) echo 'unknown mechanical test filter' >&2; exit 2 ;; esac
exec bash "$(dirname "${BASH_SOURCE[0]}")/score.test.sh" Regression.test_geometry
