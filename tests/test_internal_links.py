from blogger_toolkit.automation.internal_links import suggest_internal_links


def test_internal_link_suggestions() -> None:
    text = "This post covers blogging workflow and metadata generation."
    mapping = {
        "blogging workflow": "/blogging/workflow/",
        "metadata": "/seo/metadata/",
    }
    result = suggest_internal_links(text, mapping)
    assert len(result) == 2
