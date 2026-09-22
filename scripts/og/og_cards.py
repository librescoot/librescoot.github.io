"""Share-card compositions for librescoot.org.

Every card is exactly 1200x630 pixels (the og:image size Discord, Telegram and
Slack show uncropped). The layouts are fixed-parameter; copy and images come
from page front matter via gen_og_images.py.

Brand artwork lives in assets/ next to this file, fonts are the site's own
woff2 files (converted to TTF at first use, Pillow cannot read woff2).
"""

import os
import tempfile

from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
ASSETS = os.path.join(HERE, "assets")
FONTS = os.path.join(ROOT, "fonts")

# ------------------------------------------------------------------ palette
BG = (0, 0, 0)                    # hero cards sit on pure black so the
BG_PLATE = (6, 9, 12)             # baked-black flame artwork blends seamlessly
TEXT = (240, 240, 240)
CYAN = (34, 211, 238)
PLATE_BG = (11, 15, 19)           # screenshot plate


def mix(bg, a):
    """Opaque blend of TEXT over bg: ImageDraw ignores fill alpha, so dim
    text must be pre-composited against the canvas colour."""
    return tuple(round(t * a + b * (1 - a)) for t, b in zip(TEXT[:3], bg))


SUB_FILL = mix(BG_PLATE, 0.50)     # subtitle: clearly below the title
URL_FILL = mix(BG_PLATE, 0.36)     # footer URL: present, never loud

# ------------------------------------------------------- fixed layout params
M = 84            # canvas margin
HERO = dict(wordmark_h=52, title_px=62, title_lh=1.12,
            title_w=600, sub_px=26, sub_w=560, flame_h=504)
MINIMAL = dict(flame_h=340, wordmark_h=88, mark_h=232, url_px=22)
PLATE = dict(wordmark_h=56, kick_px=20, title_px=84, title_lh=1.08, title_w=980,
             sub_px=28, sub_w=640, wm_flame_h=440, wm_op=30)
SHOT = dict(wordmark_h=52, kick_px=19, title_px=56, title_lh=1.1, title_w=500,
            sub_px=24, sub_w=470, frame_w=484, frame_h=484, frame_x=656, pad=14)

WORDMARK = os.path.join(ASSETS, "logo-v3-full.png")
WORDMARK_ONLY = os.path.join(ASSETS, "librescoot-wordmark-white.png")
FLAME = os.path.join(ASSETS, "flame-tight.png")
FLAME_GLOW = os.path.join(ASSETS, "flame-reflection-trim.png")

FONT_CACHE = {}
WORD_FRAC = None


def font(name, px, weight=None):
    key = (name, px, weight)
    if key not in FONT_CACHE:
        FONT_CACHE[key] = ImageFont.truetype(_ttf(name), px)
        if weight is not None:
            try:
                FONT_CACHE[key].set_variation_by_axes([weight])
            except Exception:
                pass
    return FONT_CACHE[key]


def _ttf(name):
    cache = os.path.join(tempfile.gettempdir(), "librescoot-og-fonts")
    os.makedirs(cache, exist_ok=True)
    out = os.path.join(cache, name + ".ttf")
    if not os.path.exists(out):
        from fontTools.ttLib import TTFont
        f = TTFont(os.path.join(FONTS, name + ".woff2"))
        f.flavor = None
        f.save(out)
    return out


F_TITLE = "abel-latin"
F_BODY = "hanken-grotesk-latin"
F_MONO = "jetbrains-mono-latin"

_WORD_FRAC_SRC = None


def word_frac():
    """Where the word starts in the lockup: after the flame and its gap."""
    global WORD_FRAC
    if WORD_FRAC is None:
        img = Image.open(WORDMARK).convert("RGBA")
        a = img.getchannel("A")
        cols = [any(a.getpixel((x, y)) > 8 for y in range(0, img.height, 2))
                for x in range(img.width)]
        x = 0
        while x < img.width and not cols[x]:
            x += 1
        while x < img.width and cols[x]:
            x += 1
        while x < img.width and not cols[x]:
            x += 1
        WORD_FRAC = x / img.width
    return WORD_FRAC


# ------------------------------------------------------------------- text

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def balanced(draw, text, fnt, max_w, max_lines=None):
    """Wrap with even line lengths. Words are atomic, so hyphenated compounds
    never break mid-compound. Over-length text is cut at a word with an
    ellipsis rather than spilling."""
    if max_lines is not None and len(wrap(draw, text, fnt, max_w)) > max_lines:
        words = text.split()
        while len(words) > 1:
            cand = " ".join(words) + " …"
            if len(wrap(draw, cand, fnt, max_w)) <= max_lines:
                break
            words.pop()
        text = " ".join(words) + " …"
    base = wrap(draw, text, fnt, max_w)
    n = len(base)
    lo = max((draw.textlength(t, font=fnt) for t in text.split()), default=1)
    hi, best = max_w, base
    while hi - lo > 2:
        mid = (lo + hi) // 2
        cand = wrap(draw, text, fnt, mid)
        if len(cand) <= n:
            best, hi = cand, mid
        else:
            lo = mid
    return best


def title_lines(draw, text, px, max_w, max_lines=2, min_px=54):
    """Titles keep their type size while they fit max_lines. Longer titles
    step down to min_px; a release-name colon break is preferred while it
    costs little type size."""
    probe = px
    while probe > min_px:
        if len(wrap(draw, text, font(F_TITLE, probe), max_w)) <= max_lines:
            break
        probe -= 2
    bpx, blines = probe, balanced(draw, text, font(F_TITLE, probe), max_w, max_lines)
    if max_lines == 2 and ": " in text:
        head, tail = text.split(": ", 1)
        head += ":"
        probe = px
        while probe >= max(min_px - 12, bpx - 12):
            f = font(F_TITLE, probe)
            if draw.textlength(head, font=f) <= max_w and len(wrap(draw, tail, f, max_w)) <= 1:
                return probe, [head, tail]
            probe -= 2
    return bpx, blines


def draw_text_block(draw, xy, lines, fnt, fill, lh):
    x, y = xy
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += round(fnt.size * lh)
    return y


def kicker(draw, x, y, text, px=20):
    """Editorial overline: mono caps on the text column."""
    draw.text((x, y), text.upper(), font=font(F_MONO, px, 500), fill=CYAN)


def url_line(draw, x, y, text, px=20, anchor=None):
    draw.text((x, y), text, font=font(F_MONO, px), fill=URL_FILL, anchor=anchor)


# ------------------------------------------------------------------ images

def paste_rgba(base, img, xy):
    base.alpha_composite(img, xy)


def tinted(img, alpha):
    out = img.copy()
    a = out.getchannel("A").point(lambda v: v * alpha // 255)
    out.putalpha(a)
    return out


def draw_mark_hung(base, col_x, y, h):
    """Combined mark with its word aligned to the text column; the flame
    hangs left into the margin."""
    img = Image.open(WORDMARK).convert("RGBA")
    w = round(h * img.width / img.height)
    paste_rgba(base, img.resize((w, h), Image.LANCZOS), (col_x - round(w * word_frac()), y))


def draw_wordmark_only(base, x, y, h):
    img = Image.open(WORDMARK_ONLY).convert("RGBA")
    w = round(h * img.width / img.height)
    paste_rgba(base, img.resize((w, h), Image.LANCZOS), (x, y))


def draw_flame_glow(base, x, y, h):
    img = Image.open(FLAME_GLOW).convert("RGBA")
    w = round(h * img.width / img.height)
    paste_rgba(base, img.resize((w, h), Image.LANCZOS), (x, y))


def draw_flame_watermark(base, x, y, h, op):
    img = Image.open(FLAME).convert("RGBA")
    w = round(h * img.width / img.height)
    paste_rgba(base, tinted(img.resize((w, h), Image.LANCZOS), op), (x, y))


def paste_media(img, media_path, box, pad, radius=18, glow=True):
    x, y, w, h = box
    if glow:
        g = Image.new("RGBA", (w + 240, h + 240), (0, 0, 0, 0))
        ImageDraw.Draw(g).ellipse([100, 100, w + 140, h + 140], fill=CYAN + (46,))
        img.alpha_composite(g.filter(ImageFilter.GaussianBlur(70)), (x - 120, y - 120))
    plate = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    pd = ImageDraw.Draw(plate)
    pd.rounded_rectangle([0, 0, w - 1, h - 1], radius=radius,
                         fill=PLATE_BG + (255,), outline=(255, 255, 255, 22))
    media = Image.open(media_path).convert("RGBA")
    aw, ah = w - 2 * pad, h - 2 * pad
    sc = min(aw / media.width, ah / media.height)   # contained, never cropped
    mw, mh = round(media.width * sc), round(media.height * sc)
    media = media.resize((mw, mh), Image.LANCZOS)
    plate.alpha_composite(media, ((w - mw) // 2, (h - mh) // 2))
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, fill=255)
    plate.putalpha(Image.composite(plate.getchannel("A"), Image.new("L", (w, h), 0), mask))
    img.alpha_composite(plate, (x, y))


def new_canvas(bg):
    img = Image.new("RGBA", (1200, 630), bg + (255,))
    return img, ImageDraw.Draw(img)


# ------------------------------------------------------------ compositions

def hero(spec):
    """Brand flame (delivered reflection artwork) right, copy left."""
    W, H = 1200, 630
    P = HERO
    img, d = new_canvas(BG)
    fh = min(P["flame_h"], int(H * 0.8))  # flame never overruns the card
    gimg = Image.open(FLAME_GLOW).convert("RGBA")
    s = fh / gimg.height
    cb = gimg.convert("L").point(lambda v: 255 if v >= 30 else 0).getbbox()
    gy = round((H - (cb[1] + cb[3]) * s) / 2)   # centre the visible artwork
    gap = gy + cb[1] * s
    gx = round(W - gap - cb[2] * s)             # same visual gap on the right
    draw_flame_glow(img, gx, gy, fh)

    y = 72
    draw_mark_hung(img, M, y, P["wordmark_h"])
    y += P["wordmark_h"] + 46
    px, lines = title_lines(d, spec["title"], P["title_px"], P["title_w"])
    y = draw_text_block(d, (M, y), lines, font(F_TITLE, px), TEXT, P["title_lh"])
    if spec.get("sub"):
        sf = font(F_BODY, P["sub_px"], 300)
        draw_text_block(d, (M, y + 22), balanced(d, spec["sub"], sf, P["sub_w"], 2),
                        sf, SUB_FILL, 1.4)
    url_line(d, M, H - 64, spec["url"])
    return img


def minimal(variant="mark"):
    """Fallback for pages without a specific card: mark large, or flame with
    reflection over the wordmark. No flame is ever repeated."""
    W, H = 1200, 630
    img, d = new_canvas(BG)
    if variant == "mark":
        mh = min(MINIMAL["mark_h"], int(H * 0.8))
        m = Image.open(WORDMARK).convert("RGBA")
        mw = round(mh * m.width / m.height)
        my = (H - mh) // 2 - 30
        paste_rgba(img, m.resize((mw, mh), Image.LANCZOS), ((W - mw) // 2, my))
        url_line(d, W // 2, my + mh + 46, "librescoot.org", px=MINIMAL["url_px"], anchor="ma")
    else:
        fh = min(MINIMAL["flame_h"], int(H * 0.8))
        gimg = Image.open(FLAME_GLOW).convert("RGBA")
        fw = round(fh * gimg.width / gimg.height)
        draw_flame_glow(img, (W - fw) // 2, 54, fh)
        wh = MINIMAL["wordmark_h"]
        wm = Image.open(WORDMARK_ONLY).convert("RGBA")
        ww = round(wh * wm.width / wm.height)
        draw_wordmark_only(img, (W - ww) // 2, 54 + fh + 44, wh)
        url_line(d, W // 2, 54 + fh + 44 + wh + 34, "librescoot.org",
                 px=MINIMAL["url_px"], anchor="ma")
    return img


def plate(spec):
    """Overline with section and date, headline, one summary line."""
    W, H = 1200, 630
    P = PLATE
    img, d = new_canvas(BG_PLATE)
    fh = P["wm_flame_h"]
    fimg = Image.open(FLAME).convert("RGBA")
    fw = round(fh * fimg.width / fimg.height)
    draw_flame_watermark(img, W - fw + 60, H - fh + 110, fh, P["wm_op"])

    draw_mark_hung(img, M, 68, P["wordmark_h"])
    y = 216
    kicker(d, M, y, spec["kicker"], P["kick_px"])
    y += P["kick_px"] + 30
    px, lines = title_lines(d, spec["title"], P["title_px"], P["title_w"])
    y = draw_text_block(d, (M, y), lines, font(F_TITLE, px), TEXT, P["title_lh"])
    if spec.get("sub"):
        sf = font(F_BODY, P["sub_px"], 300)
        sub_lines = spec.get("sub_lines", 3 if len(lines) == 1 else 2)
        draw_text_block(d, (M, y + 22), balanced(d, spec["sub"], sf, P["sub_w"], sub_lines),
                        sf, SUB_FILL, 1.4)
    url_line(d, M, H - 64, spec["url"])
    return img


def shot(spec):
    """The page's own image, contained uncropped on a dark plate."""
    W, H = 1200, 630
    P = SHOT
    img, d = new_canvas(BG_PLATE)

    fw, fh = P["frame_w"], P["frame_h"]
    mi = Image.open(spec["media"])
    wide = mi.width / mi.height >= 1.25 or spec.get("wide")
    fx = P["frame_x"] if wide else P["frame_x"] - 8
    fy = (H - fh) // 2
    if wide:
        fh = 340
        fy = (H - fh) // 2 - 40
    paste_media(img, spec["media"], (fx, fy, fw, fh), P["pad"])

    draw_mark_hung(img, M, 68, P["wordmark_h"])
    kicker(d, M, 186, spec["kicker"], P["kick_px"])
    y = 236
    px, lines = title_lines(d, spec["title"], P["title_px"], P["title_w"])
    y = draw_text_block(d, (M, y), lines, font(F_TITLE, px), TEXT, P["title_lh"])
    if spec.get("sub"):
        sf = font(F_BODY, P["sub_px"], 300)
        draw_text_block(d, (M, y + 20),
                        balanced(d, spec["sub"], sf, P["sub_w"], spec.get("sub_lines", 3)),
                        sf, SUB_FILL, 1.4)
    url_line(d, M, H - 64, spec["url"])
    return img
