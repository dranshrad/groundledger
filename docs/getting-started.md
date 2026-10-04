# Getting started with Groundledger

## 1. Install (Claude Code + Cursor)

```bash
git clone https://github.com/dranshrad/groundledger.git
cd groundledger
bash scripts/install.sh --link
bash scripts/setup-auto-sync.sh            # git hooks; add --launchd on macOS
```

Claude only: `bash scripts/install.sh --claude --link` → `~/.claude/skills/`  
Cursor only: `bash scripts/install.sh --cursor --link` → `~/.cursor/skills/`

**Cowork:** `bash scripts/pack-cowork.sh` then upload `dist/cowork-skills/*.zip`,
or grab the rolling release [`cowork-skills-latest`](https://github.com/dranshrad/groundledger/releases/tag/cowork-skills-latest).

## 2. Optional context files

`VOICE.md` · `BRAND.md` · `CAST.md` · `ORBIT.md` · `STUDIO.md` · `SITE_BASELINE.json` · `MEDIA_LATCH.md`

## 3. Grounding

Read [Grounding Law](https://github.com/dranshrad/groundledger/blob/master/skills/blog-engine/references/grounding.md) before drafting. No invented stats, rankings, or ROAS. Paid stays observe-only until MutationLatch.

## 4. First prompts

- “Use Groundledger blog-engine to draft … with a claim ledger.”
- “ORBIT triage for our product.”
- “site-signal audit https://example.com with PROBE recommendations.”
- “paid-cast audit this export — observe only.”
- “Atomize this article with social-cast.”
- “Draw cue P-audit from cue-deck.”

[← Home](index.html) · [Frameworks](frameworks.md) · [Brand](brand.md) · [Ecosystem](ECOSYSTEM.md)
