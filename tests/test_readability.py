from blogger_toolkit.content.readability import calculate_readability


def test_readability_returns_expected_keys() -> None:
    result = calculate_readability("This is a simple sentence. This is another one.")
    assert "flesch_reading_ease" in result
    assert "flesch_kincaid_grade" in result
