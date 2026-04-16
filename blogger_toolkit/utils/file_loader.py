"""Helpers for loading text content from files."""

from __future__ import annotations

from pathlib import Path


def load_text_file(path: str) -> str:
    """Load a UTF-8 text file."""
    return Path(path).read_text(encoding="utf-8")
