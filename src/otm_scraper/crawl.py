"""BFS crawler for allowlisted OTM pages."""

from __future__ import annotations

import re
import time
from collections import deque
from dataclasses import dataclass
from urllib.parse import urldefrag, urljoin, urlparse, urlunparse

import httpx
from bs4 import BeautifulSoup

from .config import Config

SKIP_EXTENSIONS = (
    ".pdf",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".zip",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".mp4",
    ".mp3",
    ".css",
    ".js",
    ".ico",
    ".xml",
    ".rss",
)

# WordPress-style pagination duplicates article content; skip these URLs.
PAGINATION_PATH_RE = re.compile(r"/page/\d+/?$", re.IGNORECASE)


@dataclass(frozen=True)
class FetchedPage:
    url: str
    final_url: str
    html: str
    status_code: int


def normalize_url(base_url: str, href: str | None) -> str | None:
    if not href:
        return None
    href = href.strip()
    if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
        return None

    absolute = urljoin(base_url, href)
    absolute, _frag = urldefrag(absolute)
    parsed = urlparse(absolute)

    if parsed.scheme not in ("http", "https"):
        return None

    # Drop query noise; normalize host/path
    path = parsed.path or "/"
    if not path.endswith("/") and "." not in path.rsplit("/", 1)[-1]:
        # Keep as-is for files with extensions; directories often lack trailing slash
        pass

    cleaned = urlunparse(
        (
            "https" if parsed.scheme == "http" else parsed.scheme,
            parsed.netloc.lower(),
            path,
            "",
            "",
            "",
        )
    )
    return cleaned


def is_html_candidate(url: str) -> bool:
    path = urlparse(url).path.lower()
    if PAGINATION_PATH_RE.search(path):
        return False
    return not any(path.endswith(ext) for ext in SKIP_EXTENSIONS)


def _extra_url_set(config: Config) -> set[str]:
    extras: set[str] = set()
    for raw in config.extra_urls:
        normalized = normalize_url(raw, raw)
        if not normalized:
            continue
        extras.add(normalized)
        extras.add(normalized.rstrip("/") + "/")
        extras.add(normalized.rstrip("/"))
    return extras


def is_allowed(url: str, config: Config) -> bool:
    parsed = urlparse(url)
    if parsed.netloc.lower() not in {h.lower() for h in config.allowed_hosts}:
        return False
    if not is_html_candidate(url):
        return False

    path = parsed.path or "/"
    prefixes = config.allowed_path_prefixes
    if any(path == p.rstrip("/") or path.startswith(p) for p in prefixes):
        return True

    # Exact extra URLs (and trailing-slash variants) are allowed even
    # outside path prefixes; their outbound links still go through this check.
    extras = _extra_url_set(config)
    return url in extras or url.rstrip("/") in extras or url.rstrip("/") + "/" in extras


def extract_links(html: str, page_url: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    links: list[str] = []
    seen: set[str] = set()
    for tag in soup.find_all("a", href=True):
        normalized = normalize_url(page_url, tag.get("href"))
        if normalized and normalized not in seen:
            seen.add(normalized)
            links.append(normalized)
    return links


def crawl(config: Config) -> list[FetchedPage]:
    seed = normalize_url(config.seed_url, config.seed_url)
    if not seed:
        raise ValueError(f"invalid seed_url: {config.seed_url}")

    queue: deque[str] = deque()
    queued: set[str] = set()
    visited: set[str] = set()
    pages: list[FetchedPage] = []

    def enqueue(url: str | None) -> None:
        if not url or url in queued or url in visited:
            return
        if not is_allowed(url, config):
            return
        queued.add(url)
        queue.append(url)

    enqueue(seed)
    for extra in config.extra_urls:
        enqueue(normalize_url(extra, extra))

    headers = {"User-Agent": config.user_agent, "Accept": "text/html,application/xhtml+xml"}

    with httpx.Client(
        headers=headers,
        follow_redirects=True,
        timeout=config.request_timeout_seconds,
    ) as client:
        first = True
        while queue:
            url = queue.popleft()
            if url in visited:
                continue
            visited.add(url)

            if not first:
                time.sleep(config.request_delay_seconds)
            first = False

            try:
                response = client.get(url)
            except httpx.HTTPError as exc:
                print(f"warn: failed to fetch {url}: {exc}")
                continue

            content_type = response.headers.get("content-type", "").lower()
            if "html" not in content_type and not response.text.lstrip().lower().startswith(
                ("<!doctype html", "<html")
            ):
                print(f"warn: skipping non-HTML {url} ({content_type or 'unknown type'})")
                continue

            final_url = str(response.url)
            final_normalized = normalize_url(final_url, final_url) or final_url

            if response.status_code >= 400:
                print(f"warn: HTTP {response.status_code} for {url}")
                continue

            page = FetchedPage(
                url=url,
                final_url=final_normalized,
                html=response.text,
                status_code=response.status_code,
            )
            pages.append(page)

            # Discover further links only from allowlisted HTML pages
            for link in extract_links(page.html, page.final_url):
                enqueue(link)

    return pages
