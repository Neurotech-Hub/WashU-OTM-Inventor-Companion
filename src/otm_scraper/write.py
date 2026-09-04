"""Write scraped Markdown knowledgebase files."""

from __future__ import annotations

import re
import shutil
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

from .extract import ExtractedPage


@dataclass(frozen=True)
class WrittenPage:
    title: str
    source_url: str
    relative_path: str
    markdown: str


def url_to_filename(url: str) -> str:
    path = urlparse(url).path.strip("/")
    if not path:
        return "index.md"
    slug = path.replace("/", "--")
    slug = re.sub(r"[^a-zA-Z0-9._-]+", "-", slug).strip("-").lower()
    if not slug:
        slug = "page"
    if not slug.endswith(".md"):
        slug = f"{slug}.md"
    return slug


def format_page_markdown(page: ExtractedPage, scraped_on: date) -> str:
    body = page.markdown.strip()
    parts = [
        f"# {page.title}",
        f"Source: {page.url}",
        f"Scraped: {scraped_on.isoformat()}",
        "",
    ]
    if body:
        parts.append(body)
        parts.append("")
    return "\n".join(parts)


def write_knowledgebase(
    pages: list[ExtractedPage],
    output_dir: Path,
    scraped_on: date | None = None,
) -> list[WrittenPage]:
    if scraped_on is None:
        scraped_on = date.today()

    # Deterministic rebuild
    if output_dir.exists():
        shutil.rmtree(output_dir)
    pages_dir = output_dir / "pages"
    pages_dir.mkdir(parents=True)

    # De-dupe by final URL, stable order by URL
    by_url: dict[str, ExtractedPage] = {}
    for page in pages:
        by_url[page.url] = page
    ordered = sorted(by_url.values(), key=lambda p: p.url)

    written: list[WrittenPage] = []
    used_names: dict[str, int] = {}

    for page in ordered:
        filename = url_to_filename(page.url)
        if filename in used_names:
            used_names[filename] += 1
            stem = filename[:-3]
            filename = f"{stem}-{used_names[filename]}.md"
        else:
            used_names[filename] = 1

        content = format_page_markdown(page, scraped_on)
        rel = f"pages/{filename}"
        (output_dir / rel).write_text(content, encoding="utf-8")
        written.append(
            WrittenPage(
                title=page.title,
                source_url=page.url,
                relative_path=rel,
                markdown=content,
            )
        )

    index_lines = [
        "# OTM Disclose Inventions Knowledgebase Index",
        f"Scraped: {scraped_on.isoformat()}",
        "",
        "| Title | Source | File |",
        "| --- | --- | --- |",
    ]
    for item in written:
        safe_title = item.title.replace("|", "\\|")
        index_lines.append(
            f"| {safe_title} | {item.source_url} | `{item.relative_path}` |"
        )
    index_lines.append("")
    (output_dir / "INDEX.md").write_text("\n".join(index_lines), encoding="utf-8")

    all_parts = [
        "# OTM Disclose Inventions Knowledgebase",
        f"Scraped: {scraped_on.isoformat()}",
        "",
        "Concatenated pages for Gemini Gem upload. Each section preserves its source URL.",
        "",
    ]
    for item in written:
        all_parts.append("---")
        all_parts.append("")
        all_parts.append(item.markdown.rstrip())
        all_parts.append("")
    (output_dir / "ALL.md").write_text("\n".join(all_parts).rstrip() + "\n", encoding="utf-8")

    return written
