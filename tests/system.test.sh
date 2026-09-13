#!/usr/bin/env bash
set -euo pipefail
case "${1:-}" in
  '') exec bash "$(dirname "${BASH_SOURCE[0]}")/score.test.sh" Regression.test_money_and_budget_validation Regression.test_pinout_checks_both_endpoints_and_ratings Regression.test_factory_yield_does_not_hide_rework ;;
  pinout) exec bash "$(dirname "${BASH_SOURCE[0]}")/score.test.sh" Regression.test_pinout_checks_both_endpoints_and_ratings ;;
  product-bom|sys-budget) exec bash "$(dirname "${BASH_SOURCE[0]}")/score.test.sh" Regression.test_money_and_budget_validation ;;
  *) echo 'unknown system test filter' >&2; exit 2 ;;
esac
