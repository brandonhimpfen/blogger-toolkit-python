from blogger_toolkit.seo.keyword_density import calculate_keyword_density


def test_keyword_density_counts_single_and_phrase() -> None:
    text = "SEO content strategy improves SEO content strategy for content teams."
    result = calculate_keyword_density(text, ["seo", "content strategy"])
    assert result["seo"]["count"] == 2
    assert result["content strategy"]["count"] == 2
