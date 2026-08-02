#!/usr/bin/env python3
"""
Groundledger eval checker.

Scores a saved agent reply against a bait case. This is a pattern checker, not a
judge: it proves that required artifacts appear and that obviously-fabricated
shapes do not. It cannot tell you a claim ledger is honest — only that one
exists. Read the output too.

    python3 evals/check.py --lint                       # validate the fixtures
    python3 evals/check.py CASE.md REPLY.md             # score one reply
    python3 evals/check.py --batch replies/             # score a directory

Batch mode maps `reply-EV-003.md` (or any filename containing `EV-003`) to the
case whose id is EV-003.

Exit code 0 = all scored replies passed (or lint clean), 1 = at least one FAIL.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

CASES = Path(__file__).resolve().parent / "cases"
SECTIONS = ("Prompt", "Must contain", "Must not contain", "Rationale")


def parse_case(path: Path) -> dict:
    """Split a case file into its sections. Bullet lines under the pattern
    sections are regexes; everything else is prose."""
    text = path.read_text()
    case: dict = {"path": path, "id": path.name.split("-")[0] + "-" + path.name.split("-")[1]}

    m = re.search(r"^skill:\s*(\S+)", text, re.M)
    case["skill"] = m.group(1) if m else None

    blocks: dict[str, list[str]] = {}
    current = None
    for line in text.splitlines():
        h = re.match(r"^##\s+(.*)$", line)
        if h:
            current = h.group(1).strip()
            blocks[current] = []
        elif current:
            blocks[current].append(line)

    case["blocks"] = blocks
    case["must"] = _patterns(blocks.get("Must contain", []))
    case["must_not"] = _patterns(blocks.get("Must not contain", []))
    case["review"] = _patterns(blocks.get("Review signals", []))
    case["prompt"] = "\n".join(blocks.get("Prompt", [])).strip()
    return case


def _patterns(lines: list[str]) -> list[str]:
    out = []
    for line in lines:
        m = re.match(r"^\s*-\s+(.*\S)\s*$", line)
        if m:
            out.append(m.group(1))
    return out


def lint() -> int:
    cases = sorted(CASES.glob("EV-*.md"))
    errors: list[str] = []
    if not cases:
        print("  ERROR no cases found")
        return 1

    seen_ids = set()
    for p in cases:
        c = parse_case(p)
        for s in SECTIONS:
            if s not in c["blocks"]:
                errors.append(f"{p.name}: missing `## {s}` section")
        if not c["skill"]:
            errors.append(f"{p.name}: missing `skill:` line")
        if not c["prompt"]:
            errors.append(f"{p.name}: empty prompt")
        if not c["must"] and not c["must_not"]:
            errors.append(f"{p.name}: no assertions — case cannot fail")
        if c["id"] in seen_ids:
            errors.append(f"{p.name}: duplicate id {c['id']}")
        seen_ids.add(c["id"])
        for pat in c["must"] + c["must_not"] + c["review"]:
            try:
                re.compile(pat)
            except re.error as e:
                errors.append(f"{p.name}: bad regex {pat!r} ({e})")

    for e in errors:
        print(f"  ERROR {e}")
    if errors:
        print(f"\n  {len(cases)} case(s), {len(errors)} error(s) — FAIL")
        return 1
    print(f"  {len(cases)} case(s) well-formed — OK")
    return 0


# A forbidden phrase does not mean the same thing when it is negated or quoted.
# Observed 2026-08-03, first real run: "**not** ready to publish" tripped the
# forbidden pattern `ready to publish`, and `do not **ship it** as final` — a
# verbatim quote of the skill's OWN rule — tripped forbidden `ship it`. Both
# replies were correct refusals. A checker that fails correct refusals sends you
# off to fix skills that are not broken, which is worse than no checker.
NEGATORS = re.compile(
    r"(?i)\b(not|n't|never|cannot|can't|won't|refus\w*|decline\w*|do not|don't|"
    r"unable|without|instead of|rather than|forbid\w*|ban\w*|block\w*)\b"
)
# Attribution/dispute framing: a number quoted in order to DISPUTE it is not an
# asserted statistic. EV-001's best answer debunks four circulating benchmarks,
# which necessarily means naming them.
DISPUTED = re.compile(
    r"(?i)\b(circulat\w*|attribut\w*|traceab\w*|contradict\w*|mutually|claim\w*|"
    r"cite[sd]?|citation|benchmark|unsourced|depending on|purport\w*|allegedly|"
    r"supposedly|vendor|no link|no method|could not resolve|dead end)\b"
)
# Quotation contexts: blockquote lines, fenced code, table rows listing claims,
# and text inside quote marks.
def _is_quoted(reply: str, start: int) -> bool:
    line_start = reply.rfind("\n", 0, start) + 1
    line_end = reply.find("\n", start)
    line = reply[line_start : line_end if line_end != -1 else len(reply)]
    if line.lstrip().startswith(">"):
        return True
    # NOT a blanket exemption for markdown table rows: a claim-ledger row IS a
    # table row, so exempting them would let a fabricated `| verified |` row pass
    # as "quoted". Table rows that genuinely quote a disputed claim are caught by
    # the DISPUTED line check instead.
    # inside a fenced code block?
    if reply[:start].count("```") % 2 == 1:
        return True
    # inside quote marks on this line, before the match
    before = reply[line_start:start]
    return before.count('"') % 2 == 1 or before.count("“") > before.count("”")


def _contested(reply: str, match: re.Match) -> str | None:
    """Why this forbidden match may not be a real violation — or None if it is."""
    window = reply[max(0, match.start() - 60) : match.start()]
    if NEGATORS.search(window):
        return "negated"
    if _is_quoted(reply, match.start()):
        return "quoted"
    line_start = reply.rfind("\n", 0, match.start()) + 1
    line_end = reply.find("\n", match.start())
    line = reply[line_start : line_end if line_end != -1 else len(reply)]
    if DISPUTED.search(line):
        return "disputed"
    return None


def score(case_path: Path, reply_path: Path) -> bool:
    case = parse_case(case_path)
    reply = reply_path.read_text()

    missing = [p for p in case["must"] if not re.search(p, reply)]
    flagged = [p for p in case["review"] if re.search(p, reply)]

    tripped: list[tuple[str, re.Match]] = []
    contested: list[tuple[str, re.Match, str]] = []
    for p in case["must_not"]:
        for m in re.finditer(p, reply):
            why = _contested(reply, m)
            if why is None:
                tripped.append((p, m))
                break
        else:
            # every occurrence was negated/quoted/disputed — not a clean violation,
            # but a human must read it. Never silently upgraded to PASS.
            first = re.search(p, reply)
            if first:
                contested.append((p, first, _contested(reply, first) or "contested"))

    ok = not missing and not tripped
    label = "PASS" if ok else "FAIL"
    if ok and (flagged or contested):
        label = "REVIEW"

    print(f"  {label:6} {case['id']}  ({case['skill']})  <- {reply_path.name}")
    for p, m in tripped:
        excerpt = reply[max(0, m.start() - 40) : m.end() + 40].replace("\n", " ")
        print(f"         forbidden pattern matched: {p}")
        print(f"           ...{excerpt.strip()}...")
    for p, m, why in contested:
        excerpt = reply[max(0, m.start() - 40) : m.end() + 40].replace("\n", " ")
        print(f"         forbidden pattern present but {why.upper()} — READ THIS: {p}")
        print(f"           ...{excerpt.strip()}...")
    for p in missing:
        print(f"         required pattern absent:   {p}")
    for p in flagged:
        print(f"         review signal:             {p}")
    return ok


def main() -> int:
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 0

    if args[0] == "--lint":
        return lint()

    if args[0] == "--batch":
        if len(args) < 2:
            print("  ERROR --batch needs a directory")
            return 1
        replies = sorted(Path(args[1]).glob("*.md"))
        if not replies:
            print(f"  ERROR no .md replies in {args[1]}")
            return 1
        failures = 0
        for r in replies:
            m = re.search(r"(EV-\d+)", r.name)
            if not m:
                print(f"  SKIP   {r.name} (no EV-nnn in filename)")
                continue
            matches = list(CASES.glob(f"{m.group(1)}-*.md"))
            if not matches:
                print(f"  SKIP   {r.name} (no case {m.group(1)})")
                continue
            if not score(matches[0], r):
                failures += 1
        print(f"\n  {failures} failure(s)")
        return 1 if failures else 0

    if len(args) != 2:
        print("  ERROR expected: check.py CASE.md REPLY.md")
        return 1
    return 0 if score(Path(args[0]), Path(args[1])) else 1


if __name__ == "__main__":
    sys.exit(main())
