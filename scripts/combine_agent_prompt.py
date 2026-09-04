#!/usr/bin/env python3
"""Combine the interview prompt and OTM knowledgebase into one agent-upload file."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROMPT = REPO_ROOT / "prompts" / "invention-interview.md"
DEFAULT_KB = REPO_ROOT / "kb" / "ALL.md"
DEFAULT_OUT = REPO_ROOT / "build" / "agent-prompt.md"
DEFAULT_README = REPO_ROOT / "README.md"

BUILD_BADGE_RE = re.compile(
    r"!\[Latest build\]\(https://img\.shields\.io/badge/latest_build-[0-9]{4}--[0-9]{2}--[0-9]{2}-[a-zA-Z0-9]+\)"
)
BUILD_LINE_RE = re.compile(r"\*\*Latest agent-prompt build:\*\* \d{4}-\d{2}-\d{2}")


def update_readme_build_date(readme_path: Path, build_day: date) -> None:
    if not readme_path.is_file():
        return

    iso = build_day.isoformat()
    badge_date = iso.replace("-", "--")
    text = readme_path.read_text(encoding="utf-8")
    updated = text

    badge = f"![Latest build](https://img.shields.io/badge/latest_build-{badge_date}-brightgreen)"
    if BUILD_BADGE_RE.search(updated):
        updated = BUILD_BADGE_RE.sub(badge, updated, count=1)
    else:
        print(f"warn: latest-build badge not found in {readme_path}", file=sys.stderr)

    line = f"**Latest agent-prompt build:** {iso}"
    if BUILD_LINE_RE.search(updated):
        updated = BUILD_LINE_RE.sub(line, updated, count=1)
    else:
        print(f"warn: latest-build line not found in {readme_path}", file=sys.stderr)

    if updated != text:
        readme_path.write_text(updated, encoding="utf-8")


def combine(
    prompt_path: Path,
    kb_path: Path,
    out_path: Path,
    readme_path: Path | None = None,
    build_day: date | None = None,
) -> date:
    missing = [p for p in (prompt_path, kb_path) if not p.is_file()]
    if missing:
        names = ", ".join(str(p) for p in missing)
        raise FileNotFoundError(f"missing source file(s): {names}")

    if build_day is None:
        build_day = date.today()

    prompt = prompt_path.read_text(encoding="utf-8").rstrip()
    kb = kb_path.read_text(encoding="utf-8").rstrip()

    header = "\n".join(
        [
            "# WashU OTM inventor companion (agent upload)",
            "",
            f"Generated: {build_day.isoformat()}",
            "Includes the invention interview instructions plus an up-to-date snapshot of public OTM pages.",
            f"Sources: `{prompt_path.name}` then `{kb_path.name}`. Edit those independently; regenerate this file.",
            "Regenerate with: `python scripts/combine_agent_prompt.py`",
            "",
            "---",
            "",
        ]
    )

    body = (
        header
        + prompt
        + "\n\n---\n\n"
        + f"# OTM knowledgebase\n\nSource file: `{kb_path}`\n\n"
        + kb
        + "\n"
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(body, encoding="utf-8")

    if readme_path is not None:
        update_readme_build_date(readme_path, build_day)

    return build_day


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Append kb/ALL.md after prompts/invention-interview.md for a single agent upload."
    )
    parser.add_argument(
        "--prompt",
        type=Path,
        default=DEFAULT_PROMPT,
        help="Interview prompt Markdown (default: prompts/invention-interview.md)",
    )
    parser.add_argument(
        "--kb",
        type=Path,
        default=DEFAULT_KB,
        help="Knowledgebase Markdown (default: kb/ALL.md)",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=DEFAULT_OUT,
        help="Combined file (default: build/agent-prompt.md)",
    )
    parser.add_argument(
        "--readme",
        type=Path,
        default=DEFAULT_README,
        help="README to stamp with latest build date (default: README.md; use empty path to skip)",
    )
    parser.add_argument(
        "--no-readme",
        action="store_true",
        help="Do not update README.md build date",
    )
    args = parser.parse_args(argv)

    readme_path = None if args.no_readme else args.readme
    if readme_path is not None and str(readme_path).strip() == "":
        readme_path = None

    try:
        build_day = combine(
            args.prompt.resolve(),
            args.kb.resolve(),
            args.output.resolve(),
            readme_path=readme_path.resolve() if readme_path else None,
        )
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"wrote {args.output.resolve()}")
    print(f"latest build: {build_day.isoformat()}")
    if readme_path:
        print(f"updated {readme_path.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
