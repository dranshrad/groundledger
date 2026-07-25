#!/usr/bin/env bash
# Wire local auto-sync for Groundledger skills.
#
#   bash scripts/setup-auto-sync.sh           # link install + git hooks
#   bash scripts/setup-auto-sync.sh --launchd # also install daily macOS job
#   bash scripts/setup-auto-sync.sh --hooks-only
#   bash scripts/setup-auto-sync.sh --uninstall-launchd
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LABEL="com.groundledger.sync-skills"
PLIST_SRC="$ROOT/scripts/launchd/${LABEL}.plist"
PLIST_DEST="${HOME}/Library/LaunchAgents/${LABEL}.plist"
DO_LINK_INSTALL=1
DO_HOOKS=1
DO_LAUNCHD=0
UNINSTALL_LAUNCHD=0

usage() {
  cat <<'EOF' >&2
Usage: scripts/setup-auto-sync.sh [--launchd] [--hooks-only] [--uninstall-launchd]

  Default: symlink-install skills + enable repo git hooks (post-merge/checkout).
  --launchd           Also install a daily LaunchAgent (pull master + sync).
  --hooks-only        Only set git hooksPath; skip install.
  --uninstall-launchd Remove the daily LaunchAgent.
EOF
  exit 1
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --launchd) DO_LAUNCHD=1 ;;
    --hooks-only) DO_LINK_INSTALL=0; DO_HOOKS=1 ;;
    --uninstall-launchd) UNINSTALL_LAUNCHD=1; DO_LINK_INSTALL=0; DO_HOOKS=0; DO_LAUNCHD=0 ;;
    -h|--help) usage ;;
    *) echo "Unknown option: $1" >&2; usage ;;
  esac
  shift
done

if [[ "$UNINSTALL_LAUNCHD" == "1" ]]; then
  launchctl bootout "gui/$(id -u)/${LABEL}" 2>/dev/null || true
  rm -f "$PLIST_DEST"
  echo "Removed LaunchAgent $LABEL"
  exit 0
fi

if [[ "$DO_LINK_INSTALL" == "1" ]]; then
  bash "$ROOT/scripts/install.sh" --all --link
fi

if [[ "$DO_HOOKS" == "1" ]]; then
  # Repo-local hooks (shared via git). Affects this clone only.
  git -C "$ROOT" config core.hooksPath .githooks
  chmod +x "$ROOT/.githooks/"* "$ROOT/scripts/"*.sh 2>/dev/null || true
  echo "Git hooks enabled: core.hooksPath=.githooks"
  echo "  post-merge / post-checkout → sync on master when skills/** change"
fi

if [[ "$DO_LAUNCHD" == "1" ]]; then
  if [[ "$(uname -s)" != "Darwin" ]]; then
    echo "launchd is macOS-only; skipping" >&2
    exit 1
  fi
  mkdir -p "${HOME}/Library/LaunchAgents" "${HOME}/Library/Logs/groundledger"
  # Render plist with absolute repo + home paths
  sed -e "s|__GROUNDLEDGER_ROOT__|${ROOT}|g" -e "s|__HOME__|${HOME}|g" \
    "$PLIST_SRC" > "$PLIST_DEST"
  launchctl bootout "gui/$(id -u)/${LABEL}" 2>/dev/null || true
  launchctl bootstrap "gui/$(id -u)" "$PLIST_DEST"
  launchctl enable "gui/$(id -u)/${LABEL}"
  # Kick once so the user sees it work
  launchctl kickstart -k "gui/$(id -u)/${LABEL}" 2>/dev/null || true
  echo "LaunchAgent installed: $PLIST_DEST"
  echo "  Logs: ~/Library/Logs/groundledger/sync-skills.log"
  echo "  Runs daily ~09:15 local; also runnable via: launchctl kickstart gui/$(id -u)/${LABEL}"
fi

echo "Auto-sync ready."
echo "Cowork still needs zip upload — run: bash scripts/pack-cowork.sh"
echo "  then Cowork → Customize → Skills → Upload (dist/cowork-skills/*.zip)"
