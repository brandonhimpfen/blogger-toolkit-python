"""Utilities for cleaning and tokenizing text."""

from __future__ import annotations

import re
from typing import List

WORD_RE = re.compile(r"[a-z0-9']+")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+)$", re.MULTILINE)


def normalize_text(text: str) -> str:
    """Lowercase text and collapse extra whitespace."""
    cleaned = text.strip().lower()
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned


def tokenize_words(text: str) -> List[str]:
    """Return lowercase word tokens."""
    return WORD_RE.findall(text.lower())


def sentence_split(text: str) -> List[str]:
    """Split text into rough sentence units."""
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    return [sentence.strip() for sentence in sentences if sentence.strip()]


def extract_markdown_headings(text: str) -> List[str]:
    """Extract Markdown ATX-style headings."""
    return [match.strip() for match in HEADING_RE.findall(text)]


def slugify(text: str) -> str:
    """Generate a URL-friendly slug."""
    text = normalize_text(text)
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")
