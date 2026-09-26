#!/usr/bin/env python3
"""Generate per-page share images (og:image) for the site build.

Reads page front matter, renders one 1200x630 card per page with og_cards.py,
and writes _data/og.yml, the lookup table _includes/head.html uses to pick the
image for a page. Everything under images/og/ and _data/og.yml is a build
artifact (see .gitignore); images/og-default.png is the committed brand
fallback for pages without a card.

    python3 scripts/og/gen_og_images.py
"""

import glob
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import og_cards as C  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
OUT_DIR = os.path.join(ROOT, "images", "og")
DATA = os.path.join(ROOT, "_data", "og.yml")
DEFAULT_IMG = os.path.join(ROOT, "images", "og-default.png")

DATE_FMT = {"de": "%d.%m.%Y", "en": "%-d %B %Y"}   # _data/i18n.yml date_format
LABEL = {
    "handbook": {"de": "Handbuch", "en": "Handbook"},
    "garages": {"de": "Garagen", "en": "Garages"},
    "integrations": {"de": "Integrationen", "en": "Integrations"},
    "news-index": {"de": "News", "en": "News"},
    "screenshots": {"de": "Screenshots", "en": "Screenshots"},
    "changelog": {"de": "Changelog", "en": "Changelog"},
}

HERO_COPY = {
    "de": dict(title="Freie Open-Source-Firmware für den unu Scooter Pro",
               sub="Freie Navigation, Updates und Alarmanlage. Offline, transparent, in deiner Hand."),
    "en": dict(title="Open-source firmware for the unu Scooter Pro",
               sub="Free navigation, updates and an alarm system. Offline, transparent, in your hands."),
}


def front_matter(path):
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---\n"):
        return {}
    body = text.split("---\n", 2)[1]
    return yaml.safe_load(body) or {}


def derived_url(rel):
    """Jekyll's default page URL: index.html collapses to its directory."""
    rel = rel.replace(os.sep, "/")
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("index.html")]
    return "/" + rel


def out_name(url):
    p = url.strip("/")
    if not p:
        return "home"
    if p.endswith(".html"):
        p = p[:-5]
    return p


def site_url(lang, url):
    return "librescoot.org" + ("" if lang == "de" else "/en") + ("" if url == "/" else url)


def classify(url):
    """Page type and overline for the share card, or None for the fallback."""
    if url == "/":
        return ("home", None)
    if url.startswith("/docs/"):
        m = re.match(r"/docs/([^/]+)/", url)
        ver = m.group(1) if m else ""
        return ("docs", "Docs · " + ("dev" if ver == "dev" else "v" + ver))
    if url.startswith("/handbook/"):
        return ("handbook", LABEL["handbook"])
    if url == "/news/":
        return ("news-index", LABEL["news-index"])
    if url == "/garages/":
        return ("garages", LABEL["garages"])
    if url == "/changelog.html":
        return ("changelog", LABEL["changelog"])
    if url.startswith("/integrations/"):
        return ("integrations", LABEL["integrations"])
    if url.startswith("/screenshots/"):
        return ("screenshots", LABEL["screenshots"])
    return (None, None)


def emit(manifest, lang, keys, img, alt):
    rel = "/images/og/%s/%s.png" % (lang, out_name(keys[0]))
    dest = os.path.join(ROOT, rel.lstrip("/"))
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    img.convert("RGB").save(dest, optimize=True)
    for key in keys:
        manifest[lang][key] = {"image": rel, "width": 1200, "height": 630, "alt": alt}
    return rel


def news_cards(manifest):
    n = 0
    for lang in ("de", "en"):
        for f in sorted(glob.glob(os.path.join(ROOT, "_news", lang, "*.md"))):
            fm = front_matter(f)
            if not fm.get("permalink") or not fm.get("title"):
                continue
            url = fm["permalink"]
            date = fm.get("date")
            over = "News"
            if date is not None:
                over += " · " + date.strftime(DATE_FMT[lang])
            spec = dict(kicker=over, title=fm["title"], sub=fm.get("summary"),
                        url=site_url(lang, url))
            img_rel = fm.get("image")
            media = os.path.join(ROOT, img_rel.lstrip("/")) if img_rel else None
            if media and os.path.exists(media):
                spec["media"] = media
                card = C.shot(spec)
                alt = fm.get("image_alt") or fm["title"]
            else:
                card = C.plate(spec)
                alt = fm["title"]
            emit(manifest, lang, [url], card, alt)
            n += 1
    return n


def page_keys(lang, rel, fm):
    """The URL key(s) this page can be looked up under."""
    keys = [fm.get("permalink") or derived_url(rel)]
    if lang == "de" and not fm.get("permalink"):
        stripped = derived_url(rel)[3:] if rel.startswith("de/") else None
        keys.append(derived_url(rel))
        if stripped:
            keys.append("/" + stripped.lstrip("/"))
    return list(dict.fromkeys(keys))


def page_cards(manifest):
    en = ["index.html", "news.html", "changelog.html", "integrations/index.html",
          "screenshots/index.html"]
    de = ["de/" + p for p in en]
    for tree, lang in (("handbook", "en"), ("docs", "en"), ("de/handbook", "de"), ("de/docs", "de")):
        base = os.path.join(ROOT, tree)
        for dirpath, _, files in os.walk(base):
            for name in sorted(files):
                if name.endswith(".html"):
                    en.append(os.path.relpath(os.path.join(dirpath, name), ROOT))
    for gar in ("de", "en"):
        p = os.path.join("_garages", gar, "index.md")
        if os.path.exists(os.path.join(ROOT, p)):
            (de if gar == "de" else en).append(p)

    n = 0
    for rel in en + de:
        lang = "de" if rel.startswith("de/") or rel.startswith("_garages/de") else "en"
        path = os.path.join(ROOT, rel)
        fm = front_matter(path)
        if fm.get("lang"):
            lang = fm["lang"]
        keys = page_keys(lang, rel, fm)
        url = keys[0]
        kind, over = classify(url)
        if kind is None and url != "/":
            continue                      # privacy and the rest: brand fallback
        if kind == "home":
            spec = dict(HERO_COPY[lang])
            spec["url"] = site_url(lang, "/")
            card = C.hero(spec)
            alt = "Librescoot flame logo and wordmark"
        else:
            over = over[lang] if isinstance(over, dict) else over
            spec = dict(kicker=over, title=fm.get("title", "Librescoot"),
                        sub=fm.get("description"), url=site_url(lang, url))
            card = C.plate(spec)
            alt = fm.get("title", "Librescoot")
        emit(manifest, lang, keys, card, alt)
        n += 1
    return n


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    manifest = {"de": {}, "en": {}}
    n_news = news_cards(manifest)
    n_pages = page_cards(manifest)
    C.minimal("mark").convert("RGB").save(DEFAULT_IMG, optimize=True)
    with open(DATA, "w", encoding="utf-8") as fh:
        yaml.safe_dump(manifest, fh, allow_unicode=True, sort_keys=True)
    total = len(manifest["de"]) + len(manifest["en"])
    print("share images: %d news + %d pages, %d manifest entries" % (n_news, n_pages, total))
    print("fallback: images/og-default.png")


if __name__ == "__main__":
    main()
