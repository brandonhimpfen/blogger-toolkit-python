"""Sentence-level analysis utilities."""

from __future__ import annotations

from blogger_toolkit.utils.text_cleaning import sentence_split, tokenize_words


def analyze_sentences(text: str) -> dict[str, float | int | str]:
    """Return basic sentence statistics."""
    sentences = sentence_split(text)
    if not sentences:
        return {
            "sentence_count": 0,
            "average_words_per_sentence": 0.0,
            "longest_sentence_word_count": 0,
            "longest_sentence": "",
        }

    sentence_lengths = [(sentence, len(tokenize_words(sentence))) for sentence in sentences]
    longest_sentence, longest_count = max(sentence_lengths, key=lambda item: item[1])
    average = sum(count for _, count in sentence_lengths) / len(sentence_lengths)
    return {
        "sentence_count": len(sentences),
        "average_words_per_sentence": round(average, 2),
        "longest_sentence_word_count": longest_count,
        "longest_sentence": longest_sentence,
    }
