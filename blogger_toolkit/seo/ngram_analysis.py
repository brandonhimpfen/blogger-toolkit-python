"""N-gram analysis for repeated phrases."""

from __future__ import annotations

from collections import Counter
from typing import List, Tuple

from blogger_toolkit.utils.text_cleaning import tokenize_words


def extract_ngrams(text: str, n: int = 2, top_n: int = 10) -> List[Tuple[str, int]]:
    """Return the most common n-grams from text."""
    tokens = tokenize_words(text)
    if n <= 0 or len(tokens) < n:
        return []
    ngrams = [" ".join(tokens[index:index + n]) for index in range(len(tokens) - n + 1)]
    return Counter(ngrams).most_common(top_n)
