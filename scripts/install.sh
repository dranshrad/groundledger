#!/usr/bin/env bash
# Install Groundledger skills into Claude Code and/or Cursor skill dirs.
#
#   bash scripts/install.sh              # copy → Claude + Cursor
#   bash scripts/install.sh --link       # symlink → live sync with this repo
#   bash scripts/install.sh --claude --link
#   bash scripts/install.sh --cursor --copy
#
# Only manages skill names present under skills/ in this repo. Other entries
# in ~/.claude/skills or ~/.cursor/skills (e.g. goal-loop-runner) are left alone.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_SRC="$ROOT/skills"

METHOD="copy"   # copy | link
TARGET="all"    # all | claude | cursor

usage() {
  cat <<'EOF' >&2
Usage: scripts/install.sh [--all|--claude|--cursor] [--copy|--link]

  --all      Install to ~/.claude/skills and ~/.cursor/skills (default)
  --claude   Claude Code / Claude CLI skills dir only
  --cursor   Cursor skills dir only
  --copy     Copy skill trees (default; snapshot)
  --link     Symlink each skill into the dest (live sync with this repo)
EOF
  exit 1
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --all) TARGET="all" ;;
    --claude) TARGET="claude" ;;
    --cursor) TARGET="cursor" ;;
    --copy) METHOD="copy" ;;
    --link) METHOD="link" ;;
    -h|--help) usage ;;
    *) echo "Unknown option: $1" >&2; usage ;;
  esac
  shift
done

skill_names() {
  local d
  for d in "$SKILLS_SRC"/*/; do
    [[ -d "$d" && -f "${d}SKILL.md" ]] || continue
    basename "$d"
  done | sort
}

install_skill() {
  local name="$1" dest_root="$2"
  local src="$SKILLS_SRC/$name"
  local dest="$dest_root/$name"

  mkdir -p "$dest_root"

  if [[ "$METHOD" == "link" ]]; then
    # Replace prior copy or stale symlink for this managed name only.
    if [[ -e "$dest" || -L "$dest" ]]; then
      rm -rf "$dest"
    fi
    ln -s "$src" "$dest"
  else
    if [[ -L "$dest" ]]; then
      rm -f "$dest"
    fi
    rm -rf "$dest"
    mkdir -p "$dest"
    if cp -RX "$src/." "$dest/" 2>/dev/null; then
      :
    else
      cp -R "$src/." "$dest/"
    fi
  fi
}

install_into() {
  local dest="$1"
  local count=0
  local name
  while IFS= read -r name; do
    install_skill "$name" "$dest"
    count=$((count + 1))
  done < <(skill_names)
  echo "Installed $count Groundledger skill(s) [$METHOD] → $dest"
}

case "$TARGET" in
  claude)
    install_into "${HOME}/.claude/skills"
    ;;
  cursor)
    install_into "${HOME}/.cursor/skills"
    ;;
  all)
    install_into "${HOME}/.claude/skills"
    install_into "${HOME}/.cursor/skills"
    ;;
  *)
    usage
    ;;
esac

echo "Done. Restart the agent client if skills do not appear."
if [[ "$METHOD" == "link" ]]; then
  echo "Link mode: edits under $SKILLS_SRC are live in the skill dirs."
fi
