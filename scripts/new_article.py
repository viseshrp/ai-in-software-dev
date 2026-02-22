#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path
from urllib.parse import urlparse


RE_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def slugify(text: str, max_len: int = 80) -> str:
    text = text.strip().lower()
    text = RE_NON_ALNUM.sub("-", text).strip("-")
    return (text[:max_len].rstrip("-")) or "untitled"


def parse_iso_date(value: str) -> dt.date:
    try:
        return dt.date.fromisoformat(value)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"Invalid date: {value!r} (expected YYYY-MM-DD)") from e


def read_template(template_path: Path) -> str:
    return template_path.read_text(encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a new article summary markdown stub from templates/article-summary.md"
    )
    parser.add_argument("--title", required=True, help="Article title (required)")
    parser.add_argument("--url", required=True, help="Original source URL (required)")
    parser.add_argument("--author", default="", help="Author name(s) if known")
    parser.add_argument(
        "--published",
        type=parse_iso_date,
        default=None,
        help="Publication date (YYYY-MM-DD) if known",
    )
    parser.add_argument(
        "--captured",
        type=parse_iso_date,
        default=dt.date.today(),
        help="Capture/summarization date (YYYY-MM-DD). Default: today",
    )
    parser.add_argument(
        "--out-dir",
        default="articles",
        help="Root output directory for summaries (default: articles)",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    template_path = repo_root / "templates" / "article-summary.md"
    if not template_path.exists():
        raise SystemExit(f"Missing template: {template_path}")

    parsed = urlparse(args.url)
    source_domain = parsed.netloc

    published = args.published
    year = (published or args.captured).year
    date_prefix = (published or args.captured).isoformat()
    filename = f"{date_prefix}_{slugify(args.title)}.md"

    out_dir = repo_root / args.out_dir / str(year)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / filename
    if out_path.exists():
        raise SystemExit(f"Refusing to overwrite existing file: {out_path}")

    doc = read_template(template_path)
    doc = doc.replace('title: ""', f'title: "{args.title.replace(chr(34), r"\\\"")}"')
    doc = doc.replace('author: ""', f'author: "{args.author.replace(chr(34), r"\\\"")}"')
    doc = doc.replace('published: "" # YYYY-MM-DD if known', f'published: "{published.isoformat() if published else ""}" # YYYY-MM-DD if known')
    doc = doc.replace('captured: ""  # YYYY-MM-DD (when you summarized it)', f'captured: "{args.captured.isoformat()}"  # YYYY-MM-DD (when you summarized it)')
    doc = doc.replace('source_url: ""', f'source_url: "{args.url}"')
    doc = doc.replace('source_domain: ""', f'source_domain: "{source_domain}"')
    doc = doc.replace("# {title}", f"# {args.title}")
    doc = doc.replace("- {source_url}", f"- {args.url}")

    out_path.write_text(doc, encoding="utf-8")
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
