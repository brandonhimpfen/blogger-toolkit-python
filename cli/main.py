"""Command-line interface for Blogger Toolkit."""

from __future__ import annotations

import argparse
import json

from blogger_toolkit.automation.draft_summary import generate_draft_summary
from blogger_toolkit.automation.metadata_generator import generate_metadata
from blogger_toolkit.seo.headings import get_headings
from blogger_toolkit.seo.keyword_density import calculate_keyword_density
from blogger_toolkit.seo.slug_generator import generate_slug
from blogger_toolkit.content.readability import calculate_readability
from blogger_toolkit.utils.file_loader import load_text_file


def main() -> None:
    parser = argparse.ArgumentParser(description="Blogger Toolkit CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    kd_parser = subparsers.add_parser("keyword-density", help="Analyze keyword density")
    kd_parser.add_argument("--file", required=True, help="Path to text file")
    kd_parser.add_argument("--keywords", nargs="+", required=True, help="Keywords or phrases to analyze")

    read_parser = subparsers.add_parser("readability", help="Calculate readability scores")
    read_parser.add_argument("--file", required=True, help="Path to text file")

    meta_parser = subparsers.add_parser("metadata", help="Generate metadata")
    meta_parser.add_argument("--file", required=True, help="Path to text file")

    slug_parser = subparsers.add_parser("slug", help="Generate a slug from text")
    slug_parser.add_argument("--text", required=True, help="Title text")

    headings_parser = subparsers.add_parser("headings", help="Extract Markdown headings")
    headings_parser.add_argument("--file", required=True, help="Path to Markdown file")

    summary_parser = subparsers.add_parser("summary", help="Generate draft summary")
    summary_parser.add_argument("--file", required=True, help="Path to text file")

    args = parser.parse_args()

    if args.command == "keyword-density":
        text = load_text_file(args.file)
        result = calculate_keyword_density(text, args.keywords)
        for keyword, data in result.items():
            print(f"{keyword}: count={data['count']} density={data['density']:.2f}%")
    elif args.command == "readability":
        text = load_text_file(args.file)
        print(json.dumps(calculate_readability(text), indent=2))
    elif args.command == "metadata":
        text = load_text_file(args.file)
        print(json.dumps(generate_metadata(text), indent=2))
    elif args.command == "slug":
        print(generate_slug(args.text))
    elif args.command == "headings":
        text = load_text_file(args.file)
        print(json.dumps(get_headings(text), indent=2))
    elif args.command == "summary":
        text = load_text_file(args.file)
        print(json.dumps(generate_draft_summary(text), indent=2))


if __name__ == "__main__":
    main()
