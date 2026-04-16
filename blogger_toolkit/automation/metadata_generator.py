"""Generate simple metadata from article text."""

from __future__ import annotations

from blogger_toolkit.content.intro_extractor import extract_intro
from blogger_toolkit.utils.text_cleaning import sentence_split, tokenize_words


def generate_metadata(text: str, max_title_words: int = 10, description_length: int = 155) -> dict[str, str]:
    """Generate a simple title suggestion and meta description."""
    words = tokenize_words(text)
    title_words = words[:max_title_words]
    title = " ".join(word.capitalize() if index == 0 else word for index, word in enumerate(title_words))

    intro = extract_intro(text, max_paragraphs=1)
    description_source = intro or " ".join(sentence_split(text)[:1])
    description = description_source.strip().replace("\n", " ")
    if len(description) > description_length:
        description = description[: description_length - 3].rstrip() + "..."

    return {"title": title, "description": description}
