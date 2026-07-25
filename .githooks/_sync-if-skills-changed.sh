#!/usr/bin/env bash
# Shared by post-merge / post-checkout. Not invoked directly by git.
#
# Significant-change gate: only sync when the current branch is master/main
# AND skills/ (or install scripts) changed between the two commits.
sync_if_skills_changed() {
  local from_ref="$1"
  local to_ref="$2"
  local ROOT
  ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

  local branch
  branch="$(git -C "$ROOT" rev-parse --abbrev-ref HEAD 2>/dev/null || echo "")"
  if [[ "$branch" != "master" && "$branch" != "main" ]]; then
    exit 0
  fi

  # Missing ORIG_HEAD (first clone edge cases) → no-op
  if ! git -C "$ROOT" rev-parse --verify "$from_ref" >/dev/null 2>&1; then
    exit 0
  fi

  if git -C "$ROOT" diff --quiet "$from_ref" "$to_ref" -- \
      skills/ scripts/install.sh scripts/sync-skills.sh scripts/pack-cowork.sh \
      .claude-plugin/ 2>/dev/null; then
    exit 0
  fi

  echo "groundledger: skills changed on $branch — syncing clients…"
  GROUNDLEDGER_SYNC_METHOD="${GROUNDLEDGER_SYNC_METHOD:-link}" \
  GROUNDLEDGER_SYNC_PLUGIN="${GROUNDLEDGER_SYNC_PLUGIN:-1}" \
  GROUNDLEDGER_SYNC_PULL=0 \
  GROUNDLEDGER_SYNC_PACK_COWORK="${GROUNDLEDGER_SYNC_PACK_COWORK:-0}" \
    bash "$ROOT/scripts/sync-skills.sh"
}
