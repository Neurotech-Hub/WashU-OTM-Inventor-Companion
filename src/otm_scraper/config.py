"""Load scraper configuration from YAML."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class Config:
    seed_url: str
    allowed_hosts: tuple[str, ...]
    allowed_path_prefixes: tuple[str, ...]
    extra_urls: tuple[str, ...]
    output_dir: Path
    request_delay_seconds: float
    request_timeout_seconds: float
    user_agent: str
    config_path: Path = field(repr=False)


def _as_tuple(value: Any, name: str) -> tuple[str, ...]:
    if value is None:
        return ()
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"config field '{name}' must be a list of strings")
    return tuple(value)


def load_config(config_path: Path) -> Config:
    path = config_path.resolve()
    if not path.is_file():
        raise FileNotFoundError(f"config not found: {path}")

    with path.open(encoding="utf-8") as fh:
        raw = yaml.safe_load(fh) or {}

    if not isinstance(raw, dict):
        raise ValueError("config root must be a mapping")

    seed_url = raw.get("seed_url")
    if not isinstance(seed_url, str) or not seed_url.strip():
        raise ValueError("config field 'seed_url' is required")

    output_dir_value = raw.get("output_dir", "kb")
    if not isinstance(output_dir_value, str) or not output_dir_value.strip():
        raise ValueError("config field 'output_dir' must be a non-empty string")

    output_dir = Path(output_dir_value)
    if not output_dir.is_absolute():
        output_dir = (path.parent / output_dir).resolve()

    return Config(
        seed_url=seed_url.strip(),
        allowed_hosts=_as_tuple(raw.get("allowed_hosts"), "allowed_hosts"),
        allowed_path_prefixes=_as_tuple(
            raw.get("allowed_path_prefixes"), "allowed_path_prefixes"
        ),
        extra_urls=_as_tuple(raw.get("extra_urls"), "extra_urls"),
        output_dir=output_dir,
        request_delay_seconds=float(raw.get("request_delay_seconds", 0.75)),
        request_timeout_seconds=float(raw.get("request_timeout_seconds", 30)),
        user_agent=str(
            raw.get(
                "user_agent",
                "OTMScraper/1.0 (+personal knowledgebase)",
            )
        ),
        config_path=path,
    )
