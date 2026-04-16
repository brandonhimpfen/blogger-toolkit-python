"""Keyword density analysis with support for phrases."""

from __future__ import annotations

from typing import Dict, List

from blogger_toolkit.utils.text_cleaning import tokenize_words

Result = Dict[str, Dict[str, float | int]]


def _count_phrase(tokens: List[str], phrase_tokens: List[str]) -> int:
    if not phrase_tokens or len(phrase_tokens) > len(tokens):
        return 0
    length = len(phrase_tokens)
    matches = 0
    for index in range(len(tokens) - length + 1):
        if tokens[index:index + length] == phrase_tokens:
            matches += 1
    return matches


def calculate_keyword_density(text: str, keywords: List[str]) -> Result:
    """Calculate keyword counts and densities for single or multi-word keywords."""
    tokens = tokenize_words(text)
    total_words = len(tokens)
    if total_words == 0:
        return {keyword: {"count": 0, "density": 0.0} for keyword in keywords}

    results: Result = {}
    for keyword in keywords:
        phrase_tokens = tokenize_words(keyword)
        count = _count_phrase(tokens, phrase_tokens)
        density = (count / total_words) * 100
        results[keyword] = {"count": count, "density": density}
    return results
