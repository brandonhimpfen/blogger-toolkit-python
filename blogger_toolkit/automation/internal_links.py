"""Suggest internal links based on keyword mappings."""

from __future__ import annotations

from typing import Dict, List


def suggest_internal_links(text: str, mapping: Dict[str, str]) -> List[dict[str, str]]:
    """Return suggested internal links for keywords found in text."""
    lower_text = text.lower()
    suggestions: List[dict[str, str]] = []
    for keyword, url in mapping.items():
        if keyword.lower() in lower_text:
            suggestions.append({"keyword": keyword, "url": url})
    return suggestions
