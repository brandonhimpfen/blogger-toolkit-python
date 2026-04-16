"""Generate a short editorial summary of a draft."""

from __future__ import annotations

from blogger_toolkit.content.intro_extractor import extract_intro
from blogger_toolkit.content.sentence_analysis import analyze_sentences
from blogger_toolkit.seo.keyword_extractor import extract_keywords


def generate_draft_summary(text: str) -> dict[str, object]:
    """Generate a compact summary for editorial review."""
    return {
        "intro": extract_intro(text, max_paragraphs=1),
        "top_keywords": extract_keywords(text, top_n=5),
        "sentence_analysis": analyze_sentences(text),
    }
