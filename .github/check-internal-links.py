#!/usr/bin/env python3
"""Fail if a built page links to a path that doesn't exist.

The docs are hand-written HTML across three frozen version folders plus dev,
each mirrored in two languages. An href to a missing page builds clean and
only 404s for the reader, so nothing catches a rename without this.

Runs against a built _site rather than the sources, so it also covers
generated nav and version-switcher links, where cross-version breakage
usually shows up.

Internal links only. Checking external ones would make CI depend on other
people's uptime.

Usage: check-internal-links.py <site-dir>
"""

import os
import re
import sys
from urllib.parse import unquote, urlparse

# Anything client-side rendered. Backtick templates in here legitimately
# contain ${...} placeholders that are not links yet at build time.
SCRIPT_BLOCK = re.compile(r"<script\b.*?</script>", re.S | re.I)
# <a href>, <img src>, <link href>, ...
REF = re.compile(r'(?:href|src)\s*=\s*"([^"]*)"', re.I)
# A leftover JS or Liquid placeholder is a template bug rather than a dead
# link, so report it separately: the fix is different.
PLACEHOLDER = re.compile(r"\$\{|\{\{|\{%")

SKIP_SCHEMES = ("http://", "https://", "mailto:", "tel:", "data:", "javascript:", "//")


def resolve(site: str, page_dir: str, path: str) -> str:
    path = unquote(path)
    if path.startswith("/"):
        return os.path.join(site, path.lstrip("/"))
    return os.path.normpath(os.path.join(page_dir, path))


def exists(target: str) -> bool:
    # Pages may be referenced with or without the trailing index.html, and
    # Pages serves directories via their index.
    return (
        os.path.isfile(target)
        or os.path.isfile(os.path.join(target, "index.html"))
        or os.path.isfile(target + ".html")
        or os.path.isdir(target)
    )


def main() -> int:
    if len(sys.argv) != 2:
        print(f"usage: {os.path.basename(sys.argv[0])} <site-dir>", file=sys.stderr)
        return 2
    site = os.path.abspath(sys.argv[1])
    if not os.path.isdir(site):
        print(f"::error::not a directory: {site}", file=sys.stderr)
        return 2

    broken: dict[str, set[str]] = {}
    placeholders: dict[str, set[str]] = {}
    checked = 0
    pages = 0

    for dirpath, _, filenames in os.walk(site):
        for filename in filenames:
            if not filename.endswith(".html"):
                continue
            pages += 1
            page = os.path.join(dirpath, filename)
            rel = os.path.relpath(page, site)
            with open(page, encoding="utf-8", errors="ignore") as fh:
                html = fh.read()
            # Strip client-side templates before looking for links.
            html = SCRIPT_BLOCK.sub("", html)

            for match in REF.finditer(html):
                ref = match.group(1).strip()
                if not ref or ref.startswith("#") or ref.lower().startswith(SKIP_SCHEMES):
                    continue
                if PLACEHOLDER.search(ref):
                    placeholders.setdefault(ref, set()).add(rel)
                    continue
                path = urlparse(ref).path
                if not path:
                    continue
                checked += 1
                if not exists(resolve(site, dirpath, path)):
                    broken.setdefault(path, set()).add(rel)

    print(f"{pages} pages, {checked} internal links checked")

    for ref, sources in sorted(placeholders.items()):
        listed = ", ".join(sorted(sources)[:3])
        print(f"::warning::unrendered template in a link: {ref} ({len(sources)} page(s): {listed})")

    if not broken:
        print("No broken internal links.")
        return 0

    for target, sources in sorted(broken.items()):
        listed = ", ".join(sorted(sources)[:5])
        more = "" if len(sources) <= 5 else f", +{len(sources) - 5} more"
        print(f"::error::broken link {target} <- {len(sources)} page(s): {listed}{more}")

    total = sum(len(s) for s in broken.values())
    print(f"\n{len(broken)} broken target(s) across {total} reference(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
