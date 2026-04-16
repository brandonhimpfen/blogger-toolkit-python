from blogger_toolkit.seo.slug_generator import generate_slug


def test_generate_slug() -> None:
    assert generate_slug("How to Build a Better Blogging Workflow") == "how-to-build-a-better-blogging-workflow"
