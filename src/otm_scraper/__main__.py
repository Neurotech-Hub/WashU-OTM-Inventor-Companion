"""CLI entry: python -m otm_scraper."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .config import load_config
from .crawl import crawl
from .extract import extract_page
from .write import write_knowledgebase


def _default_config_path() -> Path:
    # Prefer cwd/config.yaml (repo root when run as documented)
    cwd_candidate = Path.cwd() / "config.yaml"
    if cwd_candidate.is_file():
        return cwd_candidate
    # Fallback: repo root relative to this package (src/otm_scraper/../../config.yaml)
    package_root = Path(__file__).resolve().parents[2]
    return package_root / "config.yaml"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Scrape OTM Disclose Inventions pages into a Markdown knowledgebase."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="Path to config.yaml (default: ./config.yaml)",
    )
    args = parser.parse_args(argv)

    config_path = args.config or _default_config_path()
    try:
        config = load_config(config_path)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"config: {config.config_path}")
    print(f"seed:   {config.seed_url}")
    print(f"output: {config.output_dir}")

    pages = crawl(config)
    if not pages:
        print("error: no pages fetched; aborting", file=sys.stderr)
        return 1

    print(f"fetched {len(pages)} HTML page(s)")

    extracted = []
    seen_final: set[str] = set()
    seen_bodies: set[str] = set()
    for page in pages:
        if page.final_url in seen_final:
            continue
        seen_final.add(page.final_url)
        item = extract_page(page.html, page.final_url)
        body_key = " ".join(item.markdown.lower().split())
        if body_key and body_key in seen_bodies:
            print(f"skip duplicate content: {page.final_url}")
            continue
        if body_key:
            seen_bodies.add(body_key)
        extracted.append(item)

    written = write_knowledgebase(extracted, config.output_dir)
    print(f"wrote {len(written)} page file(s) to {config.output_dir / 'pages'}")
    print(f"wrote {config.output_dir / 'INDEX.md'}")
    print(f"wrote {config.output_dir / 'ALL.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
