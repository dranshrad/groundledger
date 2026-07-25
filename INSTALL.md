# Install Groundledger

Works with **Claude Code**, **Cursor**, **Claude CLI**, and **Cowork**.

## One-shot helper

```bash
git clone https://github.com/dranshrad/groundledger.git
cd groundledger
bash scripts/install.sh                # copy → Claude + Cursor
bash scripts/install.sh --link         # symlink → live sync (recommended)
bash scripts/install.sh --claude --link
bash scripts/install.sh --cursor --copy
```

`--link` only manages skill names present under `skills/` in this repo. Other
entries in `~/.claude/skills` or `~/.cursor/skills` are left alone.

## Auto-sync (recommended on your machine)

```bash
bash scripts/setup-auto-sync.sh           # link-install + git hooks
bash scripts/setup-auto-sync.sh --launchd # also daily macOS LaunchAgent
```

What that enables:

| Layer | When | What |
|-------|------|------|
| **Link install** | Always | `~/.claude/skills/<name>` and `~/.cursor/skills/<name>` → this repo (live) |
| **Git hooks** | `post-merge` / `post-checkout` on `master`/`main` when `skills/**` changes | Re-link + `claude plugin update` |
| **launchd** (optional) | Daily ~09:15 | `git pull --ff-only` on master + sync + pack Cowork zips |

Manual sync anytime:

```bash
bash scripts/sync-skills.sh
```

Uninstall the daily job:

```bash
bash scripts/setup-auto-sync.sh --uninstall-launchd
```

## Claude Code (manual)

```bash
mkdir -p ~/.claude/skills
bash scripts/install.sh --claude --link   # or --copy
```

Expected managed skills:

```
~/.claude/skills/groundledger/
~/.claude/skills/signal-os/
~/.claude/skills/blog-engine/
~/.claude/skills/editorial-pass/
~/.claude/skills/social-cast/
~/.claude/skills/orbit-discovery/
~/.claude/skills/site-signal/
~/.claude/skills/paid-cast/
~/.claude/skills/studio-desk/
~/.claude/skills/cue-deck/
```

### Claude CLI plugin

```text
/plugin marketplace add dranshrad/groundledger
/plugin install groundledger@groundledger-marketplace
```

Or from a local clone (keeps the plugin source on this tree):

```bash
claude plugin marketplace add /path/to/groundledger
claude plugin install groundledger@groundledger-marketplace -s user
claude plugin update groundledger@groundledger-marketplace
```

Restart the CLI after plugin updates.

## Cursor (manual)

```bash
bash scripts/install.sh --cursor --link
```

## After upgrading from Clearcast

```bash
rm -rf ~/.claude/skills/clearcast ~/.cursor/skills/clearcast
bash scripts/install.sh --link
```

## Cowork

Cowork has no folder-watch install. Closest automation:

1. CI on `master` builds zips and publishes the rolling GitHub Release
   [`cowork-skills-latest`](https://github.com/dranshrad/groundledger/releases/tag/cowork-skills-latest).
2. Locally: `bash scripts/pack-cowork.sh` → `dist/cowork-skills/*.zip`
3. **Cowork → Customize → Skills → Upload** each zip (`SKILL.md` at zip root).

Re-upload when the release updates (or when you care about a specific skill change).

## Project-local

```bash
mkdir -p .claude/skills .cursor/skills
# Prefer linking into a clone rather than copying, if the client allows:
# ln -s /path/to/groundledger/skills/blog-engine .claude/skills/blog-engine
cp -R /path/to/groundledger/skills/* .claude/skills/
cp -R /path/to/groundledger/skills/* .cursor/skills/
```

## Docs

https://dranshrad.github.io/groundledger/

## Optional context files

`VOICE.md` · `BRAND.md` · `CAST.md` · `ORBIT.md` · `STUDIO.md` · optional `SITE_BASELINE.json` · optional `MEDIA_LATCH.md`
