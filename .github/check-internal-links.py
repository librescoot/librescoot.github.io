#!/usr/bin/env python3
"""Fail if a built page links to somewhere that isn't there.

The docs are hand-written HTML across three frozen version folders plus dev,
mirrored in two languages, so a link can rot four ways at once and still
render perfectly. Jekyll will not tell you: an href to a page that does not
exist builds clean and 404s only for the reader.

Runs against a built _site, so it sees the post-Liquid, post-polyglot output
including generated nav and version-switcher links, which is where cross-
version rot actually shows up.

Only internal links. External ones are somebody else's uptime.

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
# A leftover JS/Liquid placeholder is a template bug, not a link. Report it
# separately rather than as a missing file, since the fix is different.
PLACEHOLDER = re.compile(r"\$\{|\{\{|\{%")

SKIP_SCHEMES = ("http://", "https://", "mailto:", "tel:", "data:", "javascript:", "//")

# Known-broken targets, one path per line, # for comments. Baseline only:
# nothing should be added here to make a new break go quiet. Fix the link.
IGNORE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "known-broken-links.txt")


def load_ignored() -> set[str]:
    if not os.path.isfile(IGNORE_FILE):
        return set()
    with open(IGNORE_FILE, encoding="utf-8") as fh:
        return {
            line.strip()
            for line in fh
            if line.strip() and not line.lstrip().startswith("#")
        }


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

    ignored = load_ignored()
    known = {t: s for t, s in broken.items() if t in ignored}
    broken = {t: s for t, s in broken.items() if t not in ignored}

    for target, sources in sorted(known.items()):
        print(f"::warning::known-broken (baselined): {target} <- {len(sources)} page(s)")
    for stale in sorted(ignored - set(known)):
        print(f"::warning::{stale} is in {os.path.basename(IGNORE_FILE)} but no longer breaks; drop the entry")

    if not broken:
        print("No new broken internal links.")
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
