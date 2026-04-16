"""Helpers for reviewing heading structure in Markdown posts."""

from __future__ import annotations

from typing import List

from blogger_toolkit.utils.text_cleaning import extract_markdown_headings


def get_headings(text: str) -> List[str]:
    """Return Markdown headings in order."""
    return extract_markdown_headings(text)
