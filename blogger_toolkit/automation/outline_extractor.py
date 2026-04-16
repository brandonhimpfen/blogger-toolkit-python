"""Extract a simple outline from Markdown headings."""

from __future__ import annotations

from blogger_toolkit.utils.text_cleaning import extract_markdown_headings


def extract_outline(markdown_text: str) -> list[str]:
    """Return a simple outline from Markdown headings."""
    return extract_markdown_headings(markdown_text)
