"""Simple readability scoring functions."""

from __future__ import annotations

from blogger_toolkit.utils.text_cleaning import sentence_split, tokenize_words

VOWELS = "aeiouy"


def _count_syllables(word: str) -> int:
    word = word.lower().strip()
    if not word:
        return 0
    count = 0
    previous_is_vowel = False
    for char in word:
        is_vowel = char in VOWELS
        if is_vowel and not previous_is_vowel:
            count += 1
        previous_is_vowel = is_vowel
    if word.endswith("e") and count > 1:
        count -= 1
    return max(count, 1)


def calculate_readability(text: str) -> dict[str, float]:
    """Calculate Flesch Reading Ease and Flesch-Kincaid Grade Level."""
    sentences = sentence_split(text)
    words = tokenize_words(text)
    if not sentences or not words:
        return {"flesch_reading_ease": 0.0, "flesch_kincaid_grade": 0.0}

    syllables = sum(_count_syllables(word) for word in words)
    words_per_sentence = len(words) / len(sentences)
    syllables_per_word = syllables / len(words)

    flesch = 206.835 - 1.015 * words_per_sentence - 84.6 * syllables_per_word
    grade = 0.39 * words_per_sentence + 11.8 * syllables_per_word - 15.59
    return {
        "flesch_reading_ease": round(flesch, 2),
        "flesch_kincaid_grade": round(grade, 2),
    }
