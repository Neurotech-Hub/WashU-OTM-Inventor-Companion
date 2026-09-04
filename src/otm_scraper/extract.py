"""Extract main page content as Markdown with absolute links."""

from __future__ import annotations

import re
from dataclasses import dataclass
from urllib.parse import urljoin, urlparse

import trafilatura
from bs4 import BeautifulSoup, Comment, Tag
from markdownify import markdownify as html_to_md

from .crawl import normalize_url

BOILERPLATE_SELECTORS = (
    "nav",
    "header",
    "footer",
    "aside",
    "script",
    "style",
    "noscript",
    "iframe",
    "form",
    ".site-header",
    ".site-footer",
    ".main-navigation",
    ".secondary-navigation",
    ".menu",
    ".widget",
    ".sidebar",
    ".search-form",
    ".search-bar",
    ".search-bar-container",
    ".printfriendly",
    "#wpadminbar",
    ".skip-link",
    ".screen-reader-text",
    ".facetwp-facet",
    ".ppi-filters",
    ".alpha-links",
)


@dataclass(frozen=True)
class ExtractedPage:
    url: str
    title: str
    markdown: str


def _page_title(soup: BeautifulSoup, fallback: str) -> str:
    h1 = soup.find("h1")
    if h1 and h1.get_text(strip=True):
        return h1.get_text(strip=True)
    if soup.title and soup.title.get_text(strip=True):
        title = soup.title.get_text(strip=True)
        title = re.split(r"\s*\|\s*", title, maxsplit=1)[0].strip()
        return title or fallback
    return fallback


def _absolutize_links(soup: BeautifulSoup | Tag, base_url: str) -> None:
    for tag in soup.find_all("a", href=True):
        absolute = normalize_url(base_url, tag.get("href"))
        if absolute:
            tag["href"] = absolute
    for tag in soup.find_all(["img", "source"], src=True):
        src = tag.get("src")
        if src:
            tag["src"] = urljoin(base_url, src)


def _strip_boilerplate(root: Tag) -> None:
    for selector in BOILERPLATE_SELECTORS:
        for node in root.select(selector):
            node.decompose()
    for comment in root.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()


def _html_fragment_to_markdown(html: str) -> str:
    md = html_to_md(
        html,
        heading_style="ATX",
        bullets="-",
        strip=["img"],
        escape_asterisks=False,
        escape_underscores=False,
    )
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


def _link_count(markdown: str) -> int:
    return len(re.findall(r"\[[^\]]+\]\([^)]+\)", markdown))


def _score_markdown(markdown: str) -> tuple[int, int]:
    """Prefer more links, then longer body."""
    body = markdown.strip()
    return (_link_count(body), len(body))


def _format_ppi_directory(soup: BeautifulSoup, base_url: str) -> str | None:
    cards = soup.select(".washu-ppi-card")
    if len(cards) < 5:
        return None

    lines = [
        "Directory of WashU departments and their OTM tech transfer contacts.",
        "",
        "| Department | Contact | Profile |",
        "| --- | --- | --- |",
    ]
    for card in cards:
        link = card.select_one("a.washu-ppi-card-link")
        dept_el = card.select_one("h2")
        person_el = card.select_one(".washu-ppi-description")
        if not dept_el:
            continue
        dept = dept_el.get_text(" ", strip=True)
        person = person_el.get_text(" ", strip=True) if person_el else ""
        href = ""
        if link and link.get("href"):
            href = normalize_url(base_url, link.get("href")) or link.get("href") or ""
        profile = f"[profile]({href})" if href else ""
        dept = dept.replace("|", "\\|")
        person = person.replace("|", "\\|")
        lines.append(f"| {dept} | {person} | {profile} |")

    if len(lines) <= 4:
        return None
    return "\n".join(lines)


def _fallback_markdown(html: str, page_url: str) -> tuple[str, str]:
    soup = BeautifulSoup(html, "html.parser")
    title = _page_title(
        soup, fallback=urlparse(page_url).path.rstrip("/").split("/")[-1] or "Untitled"
    )

    directory_md = _format_ppi_directory(soup, page_url)
    if directory_md:
        return title, directory_md

    # Prefer specific content roots first so sidebars in <main>/<body> don't win
    # on link-count scoring.
    preferred_selectors = (
        ".page-content",
        ".entry-content",
        ".post-content",
        "article",
        "main",
        "#content",
    )
    for selector in preferred_selectors:
        found = soup.select_one(selector)
        if not found:
            continue
        clone = BeautifulSoup(str(found), "html.parser")
        node = clone.find(True)
        if not isinstance(node, Tag):
            continue
        _strip_boilerplate(node)
        _absolutize_links(node, page_url)
        h1 = node.find("h1")
        if h1:
            h1.decompose()
        # Drop empty headings
        for heading in node.find_all(re.compile(r"^h[1-6]$")):
            if not heading.get_text(strip=True):
                heading.decompose()
        md = _html_fragment_to_markdown(str(node))
        if len(md) >= 40:
            return title, md

    if soup.body:
        clone = BeautifulSoup(str(soup.body), "html.parser")
        node = clone.find(True)
        if isinstance(node, Tag):
            _strip_boilerplate(node)
            _absolutize_links(node, page_url)
            return title, _html_fragment_to_markdown(str(node))

    return title, ""


def extract_page(html: str, page_url: str) -> ExtractedPage:
    soup = BeautifulSoup(html, "html.parser")
    title = _page_title(
        soup,
        fallback=urlparse(page_url).path.rstrip("/").split("/")[-1] or "Untitled",
    )

    # Structured WashU PPI directories beat generic extractors
    directory_md = _format_ppi_directory(soup, page_url)
    if directory_md:
        return ExtractedPage(url=page_url, title=title, markdown=directory_md)

    working = BeautifulSoup(html, "html.parser")
    if working.body:
        _absolutize_links(working.body, page_url)
    absolutized_html = str(working)

    traf_md = trafilatura.extract(
        absolutized_html,
        url=page_url,
        include_links=True,
        include_tables=True,
        include_comments=False,
        include_images=False,
        output_format="markdown",
        favor_recall=True,
    ) or ""

    fb_title, fallback_md = _fallback_markdown(html, page_url)
    if fb_title:
        title = fb_title

    # Prefer the richer extraction (links first, then length)
    if _score_markdown(fallback_md) > _score_markdown(traf_md):
        markdown = fallback_md
    else:
        markdown = traf_md

    markdown = re.sub(r"\n{3,}", "\n\n", (markdown or "").strip())

    lines = markdown.splitlines()
    if lines and re.match(r"^#\s+", lines[0]):
        heading = re.sub(r"^#\s+", "", lines[0]).strip()
        if heading.lower() == title.lower():
            markdown = "\n".join(lines[1:]).lstrip()

    return ExtractedPage(url=page_url, title=title, markdown=markdown)
