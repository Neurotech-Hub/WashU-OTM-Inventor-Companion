#!/usr/bin/env python3
"""Combine the interview prompt and OTM knowledgebase into one agent-upload file."""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROMPT = REPO_ROOT / "prompts" / "invention-interview.md"
DEFAULT_KB = REPO_ROOT / "kb" / "ALL.md"
DEFAULT_OUT = REPO_ROOT / "build" / "agent-prompt.md"


def combine(prompt_path: Path, kb_path: Path, out_path: Path) -> None:
    missing = [p for p in (prompt_path, kb_path) if not p.is_file()]
    if missing:
        names = ", ".join(str(p) for p in missing)
        raise FileNotFoundError(f"missing source file(s): {names}")

    prompt = prompt_path.read_text(encoding="utf-8").rstrip()
    kb = kb_path.read_text(encoding="utf-8").rstrip()

    header = "\n".join(
        [
            "# WashU OTM inventor companion (agent upload)",
            "",
            f"Generated: {date.today().isoformat()}",
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
    args = parser.parse_args(argv)

    try:
        combine(args.prompt.resolve(), args.kb.resolve(), args.output.resolve())
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"wrote {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
