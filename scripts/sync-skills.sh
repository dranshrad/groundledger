#!/usr/bin/env bash
# Sync helper used by git hooks and the daily launchd job.
#
# Env:
#   GROUNDLEDGER_SYNC_METHOD=link|copy   (default: link)
#   GROUNDLEDGER_SYNC_PLUGIN=1|0         (default: 1 — run claude plugin update)
#   GROUNDLEDGER_SYNC_PULL=1|0           (default: 0 — set 1 for launchd)
#   GROUNDLEDGER_SYNC_PACK_COWORK=1|0    (default: 0)
#   GROUNDLEDGER_REPO=/path/to/repo      (default: parent of scripts/)
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ROOT="${GROUNDLEDGER_REPO:-$ROOT}"
METHOD="${GROUNDLEDGER_SYNC_METHOD:-link}"
DO_PLUGIN="${GROUNDLEDGER_SYNC_PLUGIN:-1}"
DO_PULL="${GROUNDLEDGER_SYNC_PULL:-0}"
DO_PACK="${GROUNDLEDGER_SYNC_PACK_COWORK:-0}"

cd "$ROOT"

if [[ "$DO_PULL" == "1" ]]; then
  # Safety net only — never force; skip if dirty or not on a tracking branch.
  if [[ -z "$(git status --porcelain)" ]]; then
    branch="$(git rev-parse --abbrev-ref HEAD)"
    if [[ "$branch" == "master" || "$branch" == "main" ]]; then
      git pull --ff-only || echo "sync-skills: pull skipped (not ff-able)" >&2
    else
      echo "sync-skills: pull skipped (branch=$branch, not master/main)"
    fi
  else
    echo "sync-skills: pull skipped (working tree dirty)"
  fi
fi

bash "$ROOT/scripts/install.sh" --all "--$METHOD"

if [[ "$DO_PLUGIN" == "1" ]] && command -v claude >/dev/null 2>&1; then
  # Best-effort: plugin may be named groundledger@groundledger-marketplace
  if claude plugin update groundledger@groundledger-marketplace -s user 2>/dev/null; then
    echo "sync-skills: claude plugin updated"
  elif claude plugin update groundledger -s user 2>/dev/null; then
    echo "sync-skills: claude plugin updated"
  else
    echo "sync-skills: claude plugin update skipped (not installed or failed)"
  fi
fi

if [[ "$DO_PACK" == "1" ]]; then
  bash "$ROOT/scripts/pack-cowork.sh"
fi

echo "sync-skills: done ($METHOD)"
