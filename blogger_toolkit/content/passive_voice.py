"""Lightweight passive voice estimation."""

from __future__ import annotations

import re

from blogger_toolkit.utils.text_cleaning import sentence_split

PASSIVE_RE = re.compile(r"\b(am|is|are|was|were|be|been|being)\b\s+\b\w+(ed|en)\b", re.IGNORECASE)


def estimate_passive_voice(text: str) -> dict[str, float | int]:
    """Estimate passive-looking sentences using a simple heuristic."""
    sentences = sentence_split(text)
    if not sentences:
        return {"sentence_count": 0, "possible_passive_sentences": 0, "ratio": 0.0}

    matches = sum(1 for sentence in sentences if PASSIVE_RE.search(sentence))
    return {
        "sentence_count": len(sentences),
        "possible_passive_sentences": matches,
        "ratio": round(matches / len(sentences), 2),
    }
