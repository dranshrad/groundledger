#!/usr/bin/env bash
# Build per-skill zips for Claude Cowork upload (SKILL.md at zip root).
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
    cd "$d"
    zip -X -q -r "$OUT/${name}.zip" . -x '*.DS_Store' -x '**/.DS_Store'
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
