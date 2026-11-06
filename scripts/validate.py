#!/usr/bin/env python3
"""
Groundledger structural validator.

Checks the invariants the suite depends on but cannot enforce at runtime,
because a skill is prose and prose has no compiler. Run before every commit:

    python3 scripts/validate.py

Exit code 0 = clean, 1 = at least one ERROR. Warnings never fail the build.

The check that matters most is DUAL-LAYOUT PATH VALIDITY (check 5). Skills live
at `skills/<name>/` in this repo but at `~/.claude/skills/<name>/` once
installed — there is no `skills/` parent after install. A path like
`skills/blog-engine/references/grounding.md` therefore resolves in the repo and
breaks silently on every user's machine. Sibling-relative `../blog-engine/...`
is the only form correct in both layouts.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"

REQUIRED_FRONTMATTER = ("name", "description", "license", "compatibility")
# Agent Skills spec limits: a name the loader rejects, or a description it
# truncates, fails silently on the user's machine.
NAME_RE = re.compile(r"^[a-z0-9-]+$")
MAX_NAME = 64
MAX_DESCRIPTION = 1024
MAX_SKILL_LINES = 500  # AGENTS.md: depth belongs in references/
GROUNDING = "blog-engine/references/grounding.md"

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


try:
    import yaml  # PyYAML; CI installs it. Without it, a weaker fallback runs.
except ImportError:  # pragma: no cover - depends on the environment
    yaml = None


def _fallback_frontmatter(block: str) -> dict[str, str]:
    """Line parser for when PyYAML is absent. Handles quoted scalars and
    folded/literal block indicators; it cannot prove the block is valid YAML."""
    out: dict[str, str] = {}
    key = None
    for line in block.splitlines():
        m = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if re.fullmatch(r"[>|][+-]?", val):
                val = ""
            elif len(val) >= 2 and val[0] == val[-1] and val[0] in "'\"":
                val = val[1:-1].replace("''", "'") if val[0] == "'" else val[1:-1]
            out[key] = val
        elif key and line.strip():
            out[key] = (out[key] + " " + line.strip()).strip()
    return out


def frontmatter(text: str, label: str = "") -> dict[str, str] | None:
    """Parsed frontmatter, {} if absent, None if it is not valid YAML (error logged)."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end]
    if yaml is None:
        return _fallback_frontmatter(block)
    try:
        data = yaml.safe_load(block)
    except yaml.YAMLError as e:
        err(f"{label}: frontmatter is not valid YAML ({str(e).splitlines()[0]})")
        return None
    if not isinstance(data, dict):
        err(f"{label}: frontmatter is not a YAML mapping")
        return None
    return {str(k): ("" if v is None else str(v)) for k, v in data.items()}


def main() -> int:
    skill_dirs = sorted(d for d in SKILLS.iterdir() if d.is_dir())
    names = {d.name for d in skill_dirs}

    if not skill_dirs:
        err("no skills found under skills/")
        return report()

    for d in skill_dirs:
        sk = d / "SKILL.md"

        # 1 — every skill has an entry point
        if not sk.exists():
            err(f"{d.name}: missing SKILL.md")
            continue

        text = sk.read_text()
        fm = frontmatter(text, d.name)
        if fm is None:
            continue  # invalid YAML already reported; field checks would only add noise

        # 2 — frontmatter completeness
        for field in REQUIRED_FRONTMATTER:
            if field not in fm:
                err(f"{d.name}: frontmatter missing `{field}:`")

        # 3 — name must equal directory name (AGENTS.md), or routing breaks
        name = fm.get("name", "")
        if name and name != d.name:
            err(f"{d.name}: frontmatter name `{name}` != directory `{d.name}`")
        if name and (not NAME_RE.match(name) or len(name) > MAX_NAME):
            err(f"{d.name}: name `{name}` must match ^[a-z0-9-]+$ and be <= {MAX_NAME} chars")

        # 3b — description limits (Agent Skills spec)
        desc = fm.get("description", "")
        if "description" in fm and not desc.strip():
            err(f"{d.name}: description is empty")
        if len(desc) > MAX_DESCRIPTION:
            err(f"{d.name}: description is {len(desc)} chars (cap {MAX_DESCRIPTION})")
        if "<" in desc or ">" in desc:
            err(f"{d.name}: description contains `<` or `>`")

        # 4 — context budget
        n = len(text.splitlines())
        if n > MAX_SKILL_LINES:
            err(f"{d.name}: SKILL.md is {n} lines (cap {MAX_SKILL_LINES}) — move depth to references/")
        elif n > MAX_SKILL_LINES * 0.9:
            warn(f"{d.name}: SKILL.md is {n} lines, approaching the {MAX_SKILL_LINES} cap")

        # 5 — dual-layout path validity (the silent-breakage check)
        for m in re.finditer(r"(?<![\w./-])skills/([a-z-]+)/", text):
            if m.group(1) in names:
                err(
                    f"{d.name}: repo-root path `skills/{m.group(1)}/...` breaks after install "
                    f"— use `../{m.group(1)}/...`"
                )

        # 6 — the Grounding Law must be reachable from every skill
        if d.name == "blog-engine":
            if "references/grounding.md" not in text:
                err("blog-engine: does not reference its own grounding.md")
        elif GROUNDING not in text:
            err(f"{d.name}: never references the Grounding Law ({GROUNDING})")
        elif f"../{GROUNDING}" not in text:
            err(f"{d.name}: references grounding.md by a non-sibling path — use `../{GROUNDING}`")

        # 7 — no residual pre-rename branding inside shipped skills
        if re.search(r"clearcast", text, re.I):
            err(f"{d.name}: contains pre-rename `Clearcast` branding")

    # 8 — every relative markdown link resolves from its own file
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts or "node_modules" in md.parts:
            continue
        for m in re.finditer(r"\]\(([^)]+)\)", md.read_text()):
            target = m.group(1).split("#")[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (md.parent / target).resolve().exists():
                err(f"{md.relative_to(ROOT)}: broken link -> {target}")

    # 9 — flat-install layout: skills ship WITHOUT the repo around them, so any
    # link escaping the skill root (../../docs/...) dangles on every machine.
    # This is the same defect class as check 5 in a different shape.
    import shutil, tempfile
    with tempfile.TemporaryDirectory() as tmp:
        flat = Path(tmp) / "skills"
        shutil.copytree(SKILLS, flat)
        for md in flat.rglob("*.md"):
            for m in re.finditer(r"\]\(([^)]+)\)", md.read_text()):
                target = m.group(1).split("#")[0].strip()
                if not target or target.startswith(("http://", "https://", "mailto:")):
                    continue
                if not (md.parent / target).resolve().exists():
                    err(
                        f"{md.relative_to(flat)}: link `{target}` dangles in flat install "
                        f"— escapes the skill root; use an absolute URL"
                    )

    # 10 — the router must be able to reach every specialist
    router = SKILLS / "groundledger" / "SKILL.md"
    if router.exists():
        rt = router.read_text()
        for name in sorted(names - {"groundledger"}):
            # a bare substring test passes for any name the router merely mentions
            if f"../{name}/SKILL.md" not in rt:
                err(f"router: does not route to `{name}` (no `../{name}/SKILL.md`)")

    # 11 — the two llms.txt copies (repo root and the Pages site) must not drift
    llms, docs_llms = ROOT / "llms.txt", ROOT / "docs" / "llms.txt"
    if llms.exists() and docs_llms.exists():
        if llms.read_bytes() != docs_llms.read_bytes():
            err("llms.txt and docs/llms.txt differ — keep them identical")
    else:
        err("llms.txt or docs/llms.txt is missing")

    if yaml is None:
        warn("PyYAML not installed — frontmatter checked by the fallback line parser, not a YAML parser")

    return report()


def report() -> int:
    for w in warnings:
        print(f"  WARN  {w}")
    for e in errors:
        print(f"  ERROR {e}")
    if errors:
        print(f"\n  {len(errors)} error(s), {len(warnings)} warning(s) — FAIL")
        return 1
    print(f"  {len(warnings)} warning(s), 0 errors — OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
