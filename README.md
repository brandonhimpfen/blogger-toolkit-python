# Blogger Toolkit (Python)

[![PyPI version](https://img.shields.io/pypi/v/blogger-toolkit-python.svg)](https://pypi.org/project/blogger-toolkit-python/) &nbsp; 
[![Python versions](https://img.shields.io/pypi/pyversions/blogger-toolkit-python.svg)](https://pypi.org/project/blogger-toolkit-python/) &nbsp; 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) &nbsp; 
[![Tests](https://img.shields.io/github/actions/workflow/status/brandonhimpfen/blogger-toolkit-python/python-tests.yml?branch=main&label=tests)](../../actions) &nbsp; 
[![Code style: Ruff](https://img.shields.io/badge/code%20style-ruff-46a2f1.svg)](https://docs.astral.sh/ruff/) <br />
[![Support Open Work](https://img.shields.io/badge/Support-Open%20Work-0A0A0A?style=flat&logo=github)](https://github.com/brandonhimpfen/support) 
[![GitHub Sponsor](https://srv-cdn.himpfen.io/badges/github/github-flat.svg)](https://github.com/sponsors/brandonhimpfen) 
[![Buy Me a Coffee](https://srv-cdn.himpfen.io/badges/buymeacoffee/buymeacoffee-flat.svg)](https://buymeacoffee.com/brandonhimpfen) 
[![Ko-Fi](https://srv-cdn.himpfen.io/badges/kofi/kofi-flat.svg)](https://ko-fi.com/brandonhimpfen) 
[![PayPal](https://srv-cdn.himpfen.io/badges/paypal/paypal-flat.svg)](https://paypal.me/brandonhimpfen)

A practical Python toolkit for bloggers, content creators, and SEO workflows.

Blogger Toolkit focuses on simple, transparent utilities that help analyze, structure, and improve written content. It is designed for people who want lightweight tools they can understand, extend, and integrate into real editorial workflows.

## Why this exists

Many blogging tools focus on interfaces, dashboards, and automation layers. This project focuses on the mechanics underneath the workflow.

It helps answer practical questions such as:

- How often does a target keyword or phrase appear in a draft?
- Are sentences becoming too long or difficult to scan?
- What repeated terms might be useful for internal links or metadata?
- What quick editorial signals can be generated before publishing?

The goal is not to automate writing. The goal is to support better editorial decisions with clear, inspectable logic.

## Features

### SEO and text analysis
- Keyword density analysis with support for single-word and multi-word phrases.
- Basic keyword extraction from normalized text.
- N-gram analysis for repeated phrase detection.
- Headings extraction for quick structure review.
- Basic slug generation for blog posts.

### Content analysis
- Readability scoring using Flesch Reading Ease and Flesch-Kincaid Grade Level.
- Sentence analysis with averages and longest-sentence reporting.
- Passive voice estimation using lightweight heuristics.
- Intro paragraph extraction for summaries and previews.

### Workflow automation
- Internal link suggestions based on keyword-to-URL mappings.
- Metadata generation for titles and descriptions.
- Draft summary generation for quick editorial review.
- Outline extraction from Markdown headings.

### Utilities
- Text cleaning and normalization helpers.
- File loading helpers for plain text and Markdown content.

## Installation

Clone the repository:

```bash
git clone https://github.com/brandonhimpfen/blogger-toolkit-python.git
cd blogger-toolkit-python
```

Install dependencies:

```bash
pip install -r requirements.txt
```

For development:

```bash
pip install -e .[dev]
```

## Quick start

### Keyword density

```python
from blogger_toolkit.seo.keyword_density import calculate_keyword_density

text = "SEO content strategy helps bloggers build better content systems."
keywords = ["seo", "content strategy", "bloggers"]

result = calculate_keyword_density(text, keywords)
for keyword, data in result.items():
    print(keyword, data["count"], f'{data["density"]:.2f}%')
```

### Metadata generation

```python
from blogger_toolkit.automation.metadata_generator import generate_metadata

text = """Building a lightweight content workflow starts with simple, repeatable steps.
This article explains how to reduce friction without losing editorial quality."""

metadata = generate_metadata(text, max_title_words=8)
print(metadata)
```

### Draft summary

```python
from blogger_toolkit.automation.draft_summary import generate_draft_summary

summary = generate_draft_summary(text)
print(summary)
```

## CLI usage

You can run several tools directly from the command line.

```bash
python -m cli.main keyword-density --file examples/sample_blog_post.txt --keywords seo "content strategy" bloggers
python -m cli.main readability --file examples/sample_blog_post.txt
python -m cli.main metadata --file examples/sample_blog_post.txt
python -m cli.main slug --text "How to Build a Better Blogging Workflow"
python -m cli.main headings --file examples/sample_markdown_post.md
python -m cli.main summary --file examples/sample_blog_post.txt
```

## Example output

```text
seo: count=3 density=1.61%
content strategy: count=2 density=1.08%
bloggers: count=1 density=0.54%
```

## Project structure

```text
blogger-toolkit-python/
├── blogger_toolkit/
│   ├── automation/
│   ├── content/
│   ├── seo/
│   └── utils/
├── cli/
├── docs/
├── examples/
├── tests/
└── .github/workflows/
```

## Design principles

This project follows a few simple principles.

- Keep tools lightweight and understandable.
- Avoid black-box scoring systems.
- Prefer useful signals over inflated claims.
- Treat outputs as editorial aids, not absolute truths.
- Keep dependencies minimal where possible.

## Limitations

Keyword density is not a ranking factor on its own. Readability scores are approximations. Passive voice detection is heuristic. Automated suggestions should always be reviewed manually before publishing.

This toolkit supports editorial decision-making. It does not replace it.

## Roadmap

Planned areas for future development include:

- Topic clustering utilities.
- Content gap analysis.
- Markdown and HTML processing helpers.
- More robust metadata suggestions.
- Optional notebook examples for content audits.

## Contributing

Contributions are welcome.

When adding a new tool:

- Keep dependencies minimal
- Document the use case clearly
- Include example usage
- Add tests where practical
- Avoid unnecessary complexity

See [CONTRIBUTING.md](CONTRIBUTING.md) for more detail.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
