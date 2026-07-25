# Groundledger — Agent Skills for Content, SEO, AEO & Paid Media

<p align="center">
  <img src="assets/og-cover.png" alt="Groundledger — CLEAR SPARK ORBIT SNAP PROBE SAFE agent skills" width="100%">
</p>

**Groundledger** is an MIT suite of Agent Skills for **Claude Code**, **Cursor**, and **Cowork**: publish-ready blogging, site SEO audits, observe-only paid media, multi-pass editing, platform-native social, and multi-surface strategy — with a hard ban on fabricated statistics.

> Docs: [dranshrad.github.io/groundledger](https://dranshrad.github.io/groundledger/) · Repo: [github.com/dranshrad/groundledger](https://github.com/dranshrad/groundledger)

Formerly published as **Clearcast**; renamed to **Groundledger** to avoid unrelated trademark/name collisions (not affiliated with Clearcast UK or other ClearCast apps).

Updated: 2026-07-25

## Why Groundledger?

Content and acquisition work should (1) help a reader finish a job, (2) be extractable for AI answers, (3) cast into social without inventing numbers, (4) audit sites with falsifiable recommendations, and (5) keep paid media **observe-only** until explicit approval. Groundledger ships **CLEAR**, **SPARK**, **ORBIT**, **SNAP/PULSE**, **PROBE**, **SAFE**, Studio Desk, and Cue Deck — plus a binding [Grounding Law](skills/blog-engine/references/grounding.md).

## Skills

| Skill | Framework | Use for |
|-------|-----------|---------|
| [groundledger](skills/groundledger/) | Router | Pick / compose skills |
| [signal-os](skills/signal-os/) | Conductor | 6-pass flagship article pipeline |
| [blog-engine](skills/blog-engine/) | **CLEAR** | Articles, claim ledgers, Ship Scan, Cite Surface |
| [editorial-pass](skills/editorial-pass/) | **SPARK** | Multi-pass polish, Tone Retarget, Voice Canon |
| [social-cast](skills/social-cast/) | **SNAP + PULSE** | Hooks, posts, atomize, calendars, analytics |
| [orbit-discovery](skills/orbit-discovery/) | **ORBIT** | Surface bets, Echo Map, Close Path |
| [site-signal](skills/site-signal/) | **PROBE** | Site Health Dial, page-fit, cite-AI, drift, local SEO |
| [paid-cast](skills/paid-cast/) | **SAFE** | Paid audits, unit econ, brand/budget lattices; MutationLatch |
| [studio-desk](skills/studio-desk/) | Ops | Workspace Boot, versions, export, Ship Gate |
| [cue-deck](skills/cue-deck/) | Prompts | Reusable grounded cue cards |

## Install

```bash
git clone https://github.com/dranshrad/groundledger.git
cd groundledger
bash scripts/install.sh --link              # live sync → Claude + Cursor
bash scripts/setup-auto-sync.sh --launchd   # git hooks + daily macOS sync
```

`--link` symlinks each Groundledger skill into `~/.claude/skills/` and
`~/.cursor/skills/` (other skills in those dirs are untouched). See
[INSTALL.md](INSTALL.md) for copy mode, Claude CLI plugin update, and Cowork
zips (CI publishes [`cowork-skills-latest`](https://github.com/dranshrad/groundledger/releases/tag/cowork-skills-latest)).

Plugin-style (Claude Code / CLI):

```text
/plugin marketplace add dranshrad/groundledger
/plugin install groundledger@groundledger-marketplace
```

Details: [INSTALL.md](INSTALL.md) · [CLAUDE.md](CLAUDE.md) · [docs/getting-started.md](docs/getting-started.md).

## Grounding (no hallucinations)

Before any draft is “final”:

1. Material claims are on a **claim ledger** (`verified` / `attributed` / `author-supplied`)
2. No invented stats, studies, quotes, rankings, ROAS, or customer results
3. Uncertain points use soft language or are omitted
4. `blocked` ledger rows must be fixed or removed
5. Paid: no live spend changes unless **MutationLatch** is open and approved

Full rules: [skills/blog-engine/references/grounding.md](skills/blog-engine/references/grounding.md).

## Typical pipelines

**Content:** `orbit-discovery` → `blog-engine` → `editorial-pass` → `social-cast` → `studio-desk` ship  

**Site SEO:** `site-signal` `audit` → PROBE plan → `blog-engine` / `orbit-discovery` for fixes  

**Paid:** `paid-cast` `audit` (observe-only) → `trial` / `math` → latch-gated `optimize-draft` only with approval  


## Primitives (domain-neutral)

Three patterns here solve general agent-safety problems and transfer outside content work — copy them into any project:

| Primitive | Solves |
|-----------|--------|
| [grounding-law](primitives/grounding-law.md) | Fluent, confident, unsupported claims |
| [falsifiability-contract](primitives/falsifiability-contract.md) | Recommendations that cannot be checked |
| [write-gate](primitives/write-gate.md) | Irreversible actions, and false completion reports |

See [primitives/](primitives/).

## Evals

Adversarial fixtures that test the behavioural claim — bait prompts where fabricating is the path of least resistance:

```bash
python3 evals/check.py --lint                    # validate fixtures
python3 evals/check.py CASE.md reply.md          # score a saved reply
```

See [evals/README.md](evals/README.md). Structure and link integrity are checked by `python3 scripts/validate.py` (also runs in CI).

## Related repositories

| Project | Link |
|---------|------|
| Voice notes → Artifacts | [voice-notes-to-anthropic-artifacts](https://github.com/dranshrad/voice-notes-to-anthropic-artifacts) |
| LibCST LLM refactorer | [llm-cst-refactorer](https://github.com/dranshrad/llm-cst-refactorer) |
| Self-correction loop | [automated-self-correction-loop](https://github.com/dranshrad/automated-self-correction-loop) |
| Anthropic audio gateway | [anthropic-audio-gateway](https://github.com/dranshrad/anthropic-audio-gateway) |

See [docs/ECOSYSTEM.md](docs/ECOSYSTEM.md).

## License

[MIT](LICENSE) © 2026 Divyansh Gupta
