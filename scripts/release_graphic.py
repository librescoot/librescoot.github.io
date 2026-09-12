#!/usr/bin/env python3
"""Shared renderer for Librescoot release-card graphics.

Requires Pillow, fonttools (with WOFF2 support), and CairoSVG. Install them with:

    python3 -m pip install Pillow 'fonttools[woff]' CairoSVG
"""

from __future__ import annotations

import io
import tempfile
from pathlib import Path

try:
    import cairosvg
    from fontTools.ttLib import TTFont
    from PIL import Image, ImageDraw, ImageFont
except ImportError as error:  # pragma: no cover - dependency error path
    raise SystemExit(
        "Release graphics require Pillow, fonttools[woff], and CairoSVG. "
        "Install them with: python3 -m pip install Pillow 'fonttools[woff]' CairoSVG"
    ) from error


WIDTH = 1200
HEIGHT = 1200
BACKGROUND = (42, 45, 48)  # style.css --bg-hero
WHITE = (240, 240, 240)  # style.css --text-on-dark
CYAN = (34, 211, 238)  # style.css --accent-light
INK = (27, 31, 34)
MINOR_DIVIDER = (17, 70, 77)

ROOT = Path(__file__).resolve().parent.parent
WORDMARK = ROOT / "images" / "logo-small@2x.png"
FONT_SOURCES = {
    "abel": ROOT / "fonts" / "abel-latin.woff2",
    "hanken": ROOT / "fonts" / "hanken-grotesk-latin.woff2",
}

ICON_PATHS = {
    "alarm-clock": """
        <circle cx="12" cy="13" r="8"/>
        <path d="M12 9v4l2 2"/>
        <path d="M5 3 2 6"/>
        <path d="m22 6-3-3"/>
        <path d="M6.38 18.7 4 21"/>
        <path d="M17.64 18.67 20 21"/>
    """,
    "moon": """
        <path d="M20.985 12.486a9 9 0 1 1-9.473-9.472c.405-.022.617.46.402.803a6 6 0 0 0 8.268 8.268c.344-.215.825-.004.803.401"/>
    """,
    "sunrise": """
        <path d="M4 18h16" class="horizon"/>
        <path d="M6 18a6 6 0 0 1 12 0"/>
        <path d="M12 2v2"/>
        <path d="m4.93 10.93 1.41 1.41"/>
        <path d="M2 18h2"/>
        <path d="M20 18h2"/>
        <path d="m19.07 10.93-1.41 1.41"/>
    """,
}


def converted_fonts(directory: Path) -> dict[str, Path]:
    """Convert the site's WOFF2 files to temporary TTF files for Pillow."""
    converted: dict[str, Path] = {}
    for name, source in FONT_SOURCES.items():
        target = directory / f"{name}.ttf"
        font = TTFont(source)
        font.flavor = None
        font.save(target)
        converted[name] = target
    return converted


def font_that_fits(
    font_path: Path,
    text: str,
    initial_size: int,
    max_width: int,
    draw: ImageDraw.ImageDraw,
) -> ImageFont.FreeTypeFont:
    """Return the largest requested font size that fits the available width."""
    size = initial_size
    while size >= 24:
        font = ImageFont.truetype(str(font_path), size)
        box = draw.textbbox((0, 0), text, font=font)
        if box[2] - box[0] <= max_width:
            return font
        size -= 2
    raise ValueError(f"Text does not fit the release graphic: {text!r}")


def draw_centered(
    draw: ImageDraw.ImageDraw,
    text: str,
    y: float,
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
) -> None:
    box = draw.textbbox((0, 0), text, font=font)
    draw.text(((WIDTH - (box[2] - box[0])) / 2, y), text, font=font, fill=fill)


def rendered_icon(
    name: str,
    size: int,
    stroke: tuple[int, int, int],
    horizon: tuple[int, int, int] | None = None,
) -> Image.Image:
    """Render one of the restrained Lucide-style release symbols."""
    if name not in ICON_PATHS:
        choices = ", ".join(sorted(ICON_PATHS))
        raise ValueError(f"Unknown icon {name!r}; choose one of: {choices}")

    stroke_hex = "#%02x%02x%02x" % stroke
    horizon_hex = "#%02x%02x%02x" % (horizon or stroke)
    svg = f"""
        <svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}"
             viewBox="0 0 24 24" fill="none" stroke="{stroke_hex}"
             stroke-width="1.55" stroke-linecap="round" stroke-linejoin="round">
            <style>.horizon {{ stroke: {horizon_hex}; }}</style>
            {ICON_PATHS[name]}
        </svg>
    """
    png = cairosvg.svg2png(
        bytestring=svg.encode(), output_width=size, output_height=size
    )
    return Image.open(io.BytesIO(png)).convert("RGBA")


def base_image(wordmark_size: tuple[int, int], wordmark_y: int) -> Image.Image:
    image = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    wordmark = Image.open(WORDMARK).convert("RGBA")
    wordmark.thumbnail(wordmark_size, Image.Resampling.LANCZOS)
    image.paste(wordmark, ((WIDTH - wordmark.width) // 2, wordmark_y), wordmark)
    return image


def render_patch(version: str, codename: str, icon: str, output: Path) -> None:
    """Render the deliberately plain patch-release treatment."""
    with tempfile.TemporaryDirectory(prefix="librescoot-release-fonts-") as tmp:
        fonts = converted_fonts(Path(tmp))
        image = base_image(wordmark_size=(650, 189), wordmark_y=155)
        draw = ImageDraw.Draw(image)
        version_font = font_that_fits(fonts["abel"], version, 290, 760, draw)
        codename_font = font_that_fits(fonts["hanken"], codename, 84, 820, draw)

        draw_centered(draw, version, 400, version_font, WHITE)
        draw_centered(draw, codename, 715, codename_font, CYAN)

        symbol = rendered_icon(
            icon,
            size=220,
            stroke=CYAN,
            horizon=WHITE if icon == "sunrise" else None,
        )
        image = image.convert("RGBA")
        image.alpha_composite(symbol, ((WIDTH - 220) // 2, 865))
        output.parent.mkdir(parents=True, exist_ok=True)
        image.convert("RGB").save(output, "PNG", optimize=True)


def render_minor(version: str, codename: str, icon: str, output: Path) -> None:
    """Render the more prominent, but still restrained, minor-release treatment."""
    with tempfile.TemporaryDirectory(prefix="librescoot-release-fonts-") as tmp:
        fonts = converted_fonts(Path(tmp))
        image = base_image(wordmark_size=(680, 197), wordmark_y=145)
        draw = ImageDraw.Draw(image)
        version_font = font_that_fits(fonts["abel"], version, 320, 790, draw)
        codename_font = font_that_fits(fonts["hanken"], codename, 86, 520, draw)

        draw_centered(draw, version, 390, version_font, WHITE)
        draw.rounded_rectangle((165, 795, 1035, 1015), radius=8, fill=CYAN)

        symbol = rendered_icon(icon, size=150, stroke=INK)
        image = image.convert("RGBA")
        image.alpha_composite(symbol, (225, 830))
        draw = ImageDraw.Draw(image)
        draw.line((415, 835, 415, 975), fill=MINOR_DIVIDER, width=3)

        box = draw.textbbox((0, 0), codename, font=codename_font)
        text_height = box[3] - box[1]
        draw.text(
            (465, 905 - text_height / 2 - box[1]),
            codename,
            font=codename_font,
            fill=INK,
        )

        output.parent.mkdir(parents=True, exist_ok=True)
        image.convert("RGB").save(output, "PNG", optimize=True)
