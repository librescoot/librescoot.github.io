#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "cairosvg>=2.7,<3",
#   "fonttools[woff]>=4.50,<5",
#   "pillow>=10,<13",
# ]
# ///
"""Generate a Librescoot minor- or patch-release graphic.

Examples:
    uv run scripts/generate-release-graphic.py patch v1.3.1 \
        "Guten Morgen" --icon alarm-clock \
        --output images/news/librescoot-1-3-1.png

    uv run scripts/generate-release-graphic.py minor v1.1.0 Nachtruhe \
        --icon moon --output images/news/librescoot-1-1.png
"""

from __future__ import annotations

import argparse
from pathlib import Path

from release_graphic import ICON_PATHS, render_minor, render_patch


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "style",
        choices=("minor", "patch"),
        help="visual hierarchy to use for the release",
    )
    parser.add_argument("version", help="version label, for example v1.3.1")
    parser.add_argument("codename", help="release codename")
    parser.add_argument(
        "--icon",
        required=True,
        choices=sorted(ICON_PATHS),
        help="symbol associated with the release codename",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="destination PNG path",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    renderer = render_minor if args.style == "minor" else render_patch
    renderer(args.version, args.codename, args.icon, args.output)
    print(args.output)


if __name__ == "__main__":
    main()
