"""Slug generation helpers."""

from __future__ import annotations

from blogger_toolkit.utils.text_cleaning import slugify


def generate_slug(title: str) -> str:
    """Generate a clean slug from a title."""
    return slugify(title)
