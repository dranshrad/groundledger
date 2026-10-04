#!/usr/bin/env bash
# Build per-skill zips for claude.ai / Cowork upload.
# Layout: <name>.zip → <name>/SKILL.md — the skill FOLDER at the zip root, as
# support.claude.com/en/articles/12512198 requires ("files directly in ZIP root" is the
# documented wrong layout; fixed 2026-10-04).
#
#   bash scripts/pack-cowork.sh
#   → dist/cowork-skills/<name>.zip
#   → dist/groundledger-cowork-all.zip  (bundle of the per-skill zips)
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/dist/cowork-skills"
BUNDLE="$ROOT/dist/groundledger-cowork-all.zip"

rm -rf "$OUT"
mkdir -p "$OUT"

count=0
for d in "$ROOT/skills"/*/; do
  [[ -f "${d}SKILL.md" ]] || continue
  name="$(basename "$d")"
  (
    cd "$ROOT/skills"
    zip -X -q -r "$OUT/${name}.zip" "$name" -x '*.DS_Store' -x '**/.DS_Store'
  )
  count=$((count + 1))
done

(
  cd "$OUT"
  rm -f "$BUNDLE"
  zip -X -q -r "$BUNDLE" ./*.zip
)

echo "Packed $count Cowork skill zip(s) → $OUT"
echo "Bundle → $BUNDLE"
