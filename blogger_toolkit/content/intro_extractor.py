"""Extract opening content from drafts."""

from __future__ import annotations


def extract_intro(text: str, max_paragraphs: int = 1) -> str:
    """Return the first one or more non-empty paragraphs."""
    paragraphs = [paragraph.strip() for paragraph in text.split("\n\n") if paragraph.strip()]
    return "\n\n".join(paragraphs[:max_paragraphs])
