"""Basic keyword extraction from text."""

from __future__ import annotations

from collections import Counter
from typing import List, Tuple

from blogger_toolkit.utils.text_cleaning import tokenize_words

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has", "in", "is",
    "it", "of", "on", "or", "that", "the", "to", "was", "were", "will", "with", "this",
    "these", "those", "your", "you", "we", "our", "but", "not", "can", "if", "into"
}


def extract_keywords(text: str, top_n: int = 10, min_length: int = 4) -> List[Tuple[str, int]]:
    """Extract common non-stopword tokens."""
    words = [word for word in tokenize_words(text) if len(word) >= min_length and word not in STOPWORDS]
    return Counter(words).most_common(top_n)
