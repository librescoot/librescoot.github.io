#!/usr/bin/env python3
"""Fail if a built page links to a path or anchor that doesn't exist.

The docs are hand-written HTML across three frozen version folders plus dev,
each mirrored in two languages. An href to a missing page or a renamed
heading builds clean and only breaks for the reader, so nothing catches a
rename without this.

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
# Anchor targets. Collected from the unstripped HTML: an id that only appears
# inside a client-side template is still a plausible target once rendered, and
# calling it broken would be a false positive.
ANCHOR = re.compile(r'\b(?:id|name)\s*=\s*"([^"]+)"', re.I)
# A leftover JS or Liquid placeholder is a template bug rather than a dead
# link, so report it separately: the fix is different.
PLACEHOLDER = re.compile(r"\$\{|\{\{|\{%")
# jekyll-redirect-from stubs. A meta refresh does not carry the original
# fragment over, so a deep link through one lands at the top of the page.
REDIRECT = re.compile(
    r"""<meta[^>]+http-equiv=["']refresh["'][^>]+content=["'][^;]*;\s*url=([^"']+)""",
    re.I,
)

SKIP_SCHEMES = ("http://", "https://", "mailto:", "tel:", "data:", "javascript:", "//")
# "#top" scrolls to the top of any document with no element required.
FREE_FRAGMENTS = {"top"}


def resolve(site: str, page_dir: str, path: str) -> str:
    path = unquote(path)
    if path.startswith("/"):
        return os.path.join(site, path.lstrip("/"))
    return os.path.normpath(os.path.join(page_dir, path))


def resolve_target(site: str, page_dir: str, path: str) -> tuple[bool, str | None]:
    """Does this path resolve, and to which file if any.

    A directory without an index still counts as resolving (assets are served
    straight out of it) but has no anchors to check against.
    """
    base = resolve(site, page_dir, path)
    for candidate in (base, os.path.join(base, "index.html"), base + ".html"):
        if os.path.isfile(candidate):
            return True, candidate
    if os.path.isdir(base):
        return True, None
    return False, None


def main() -> int:
    if len(sys.argv) != 2:
        print(f"usage: {os.path.basename(sys.argv[0])} <site-dir>", file=sys.stderr)
        return 2
    site = os.path.abspath(sys.argv[1])
    if not os.path.isdir(site):
        print(f"::error::not a directory: {site}", file=sys.stderr)
        return 2

    anchors: dict[str, set[str]] = {}
    redirects: dict[str, str] = {}
    # (source page, source dir, raw ref)
    refs: list[tuple[str, str, str]] = []

    for dirpath, _, filenames in os.walk(site):
        for filename in filenames:
            if not filename.endswith(".html"):
                continue
            page = os.path.join(dirpath, filename)
            with open(page, encoding="utf-8", errors="ignore") as fh:
                html = fh.read()

            anchors[page] = set(ANCHOR.findall(html))
            hop = REDIRECT.search(html)
            if hop:
                redirects[page] = urlparse(hop.group(1).strip()).path
            rel = os.path.relpath(page, site)
            for match in REF.finditer(SCRIPT_BLOCK.sub("", html)):
                refs.append((rel, dirpath, match.group(1).strip()))

    broken: dict[str, set[str]] = {}
    dead_anchors: dict[str, set[str]] = {}
    fragment_lost: dict[str, set[str]] = {}
    placeholders: dict[str, set[str]] = {}
    checked = 0
    checked_anchors = 0

    for rel, dirpath, ref in refs:
        if not ref or ref.lower().startswith(SKIP_SCHEMES):
            continue
        if PLACEHOLDER.search(ref):
            placeholders.setdefault(ref, set()).add(rel)
            continue

        parsed = urlparse(ref)
        path, fragment = parsed.path, unquote(parsed.fragment)

        if path:
            checked += 1
            resolved, target_file = resolve_target(site, dirpath, path)
            if not resolved:
                broken.setdefault(path, set()).add(rel)
                continue
        else:
            # Same-page fragment.
            target_file = os.path.join(site, rel)

        if not fragment or fragment in FREE_FRAGMENTS or target_file is None:
            continue
        checked_anchors += 1
        where = f"{path}#{fragment}" if path else f"#{fragment}"

        if target_file in redirects:
            final_path = redirects[target_file]
            _, final_file = resolve_target(site, dirpath, final_path)
            if final_file and fragment in anchors.get(final_file, set()):
                fragment_lost.setdefault(
                    f"{where} (link {final_path}#{fragment} instead)", set()
                ).add(rel)
            else:
                dead_anchors.setdefault(where, set()).add(rel)
            continue

        if fragment not in anchors.get(target_file, set()):
            dead_anchors.setdefault(where, set()).add(rel)

    print(
        f"{len(anchors)} pages, {checked} internal links "
        f"and {checked_anchors} anchors checked"
    )

    for ref, sources in sorted(placeholders.items()):
        listed = ", ".join(sorted(sources)[:3])
        print(f"::warning::unrendered template in a link: {ref} ({len(sources)} page(s): {listed})")

    def report(kind: str, items: dict[str, set[str]]) -> None:
        for target, sources in sorted(items.items()):
            listed = ", ".join(sorted(sources)[:5])
            more = "" if len(sources) <= 5 else f", +{len(sources) - 5} more"
            print(f"::error::{kind} {target} <- {len(sources)} page(s): {listed}{more}")

    report("broken link", broken)
    report("dead anchor", dead_anchors)
    report("fragment dropped by redirect:", fragment_lost)

    if not broken and not dead_anchors and not fragment_lost:
        print("No broken internal links or anchors.")
        return 0

    parts = []
    if broken:
        parts.append(f"{len(broken)} broken target(s)")
    if dead_anchors:
        parts.append(f"{len(dead_anchors)} dead anchor(s)")
    if fragment_lost:
        parts.append(f"{len(fragment_lost)} fragment(s) lost to a redirect")
    print("\n" + ", ".join(parts) + ".")
    return 1


if __name__ == "__main__":
    sys.exit(main())
