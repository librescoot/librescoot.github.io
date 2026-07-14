#!/usr/bin/env bash
# Promote docs/dev/ into a new frozen stable folder docs/<version>/.
#
# Usage:
#   scripts/release-new-minor.sh <version>
#
#   <version>   e.g. "1.1" — the new minor.
#
# What it does (run from the main checkout):
#   1. Copies docs/dev/* and de/docs/dev/* into docs/<version>/ and
#      de/docs/<version>/.
#   2. Rewrites DE permalinks (/docs/dev/...  ->  /docs/<version>/...)
#   3. Rewrites absolute /docs/dev/* hrefs inside the copied pages to
#      /docs/<version>/*.
#   4. Adjusts redirect_from on copied pages: keeps the bare /docs/<rel>.html
#      and /docs/stable/<rel>.html entries so old links and the stable alias
#      land on the new minor.
#   5. Releases the /docs/<rel> and /docs/stable/<rel> aliases from the
#      previous stable minor's pages so both move to the new version.
#      Version-scoped redirect_from entries there are left alone.
#   6. Bumps docs_path_prefix in _config.yml to /docs/<version>.
#   7. Prepends a new entry to _data/versions.yml above the previous one and
#      removes `is_stable: true` from the previous entry.
#
# After running:
#   - Inspect the diff. Cross-check internal links.
#   - bundle exec jekyll build  &&  spot-check rendered pages.
#   - git commit -am "docs: promote v<version> to stable" && git tag v<version>.0

set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <version>" >&2
  exit 64
fi

VERSION="$1"
if [[ ! "$VERSION" =~ ^[0-9]+\.[0-9]+$ ]]; then
  echo "error: version must look like X.Y (got '$VERSION')" >&2
  exit 65
fi

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

if [[ -e "docs/$VERSION" || -e "de/docs/$VERSION" ]]; then
  echo "error: docs/$VERSION or de/docs/$VERSION already exists. Refusing to overwrite." >&2
  exit 67
fi

if [[ ! -d docs/dev || ! -d de/docs/dev ]]; then
  echo "error: docs/dev or de/docs/dev not found. Are you in a main checkout?" >&2
  exit 68
fi

# Walk real YAML entries only — comments in this file mention both
# `version:` and `is_stable: true`, and would otherwise match.
PREV_VERSION=$(awk '
  /^- version:/ { ver = $3; gsub(/"/, "", ver); next }
  /^- / { ver = "" }
  /^[[:space:]]+is_stable:[[:space:]]*true/ { if (ver != "") { print ver; exit } }
' _data/versions.yml || true)
if [[ -z "$PREV_VERSION" ]]; then
  echo "warning: could not detect previous stable from _data/versions.yml. Skipping previous-version cleanup." >&2
fi

echo "==> copying docs/dev -> docs/$VERSION and de/docs/dev -> de/docs/$VERSION"
mkdir -p "docs/$VERSION" "de/docs/$VERSION"
cp -r docs/dev/. "docs/$VERSION/"
cp -r de/docs/dev/. "de/docs/$VERSION/"

echo "==> rewriting DE permalinks (/docs/dev -> /docs/$VERSION)"
find "de/docs/$VERSION" -name "*.html" -print0 | xargs -0 sed -i "s|^permalink: /docs/dev/|permalink: /docs/$VERSION/|"

echo "==> rewriting absolute internal /docs/dev/* hrefs inside copied pages"
find "docs/$VERSION" "de/docs/$VERSION" -name "*.html" -print0 | xargs -0 sed -i "s|href=\"/docs/dev/|href=\"/docs/$VERSION/|g"

echo "==> adding redirect_from entries to the new minor's pages"
add_redirects() {
  local file="$1"
  local rel="$2"
  awk -v unver="/docs$rel" -v stable="/docs/stable$rel" '
    BEGIN { fm = 0; emitted_rf = 0 }
    # Opening front matter delimiter.
    NR == 1 && /^---$/ { fm = 1; print; next }
    # Closing delimiter: insert our entries here if the page had none.
    fm == 1 && /^---$/ {
      if (!emitted_rf) {
        print "redirect_from:"
        print "  - " unver
        print "  - " stable
        emitted_rf = 1
      }
      fm = 2
      print
      next
    }
    # Existing list or scalar — replace the whole block with our two entries.
    fm == 1 && /^redirect_from:/ {
      print "redirect_from:"
      print "  - " unver
      print "  - " stable
      emitted_rf = 1
      # Consume the old list items, then reprocess the first non-item line.
      while ((getline next_line) > 0) {
        if (next_line ~ /^[[:space:]]+-/) continue
        print next_line
        if (next_line == "---") { fm = 2 }
        break
      }
      next
    }
    { print }
  ' "$file" > "$file.tmp" && mv "$file.tmp" "$file"
}

shopt -s nullglob
for f in "docs/$VERSION"/*.html "de/docs/$VERSION"/*.html; do
  name=$(basename "$f")
  add_redirects "$f" "/$name"
done
for f in "docs/$VERSION"/features/*.html "de/docs/$VERSION"/features/*.html; do
  name=$(basename "$f")
  add_redirects "$f" "/features/$name"
done
shopt -u nullglob

# The unversioned aliases (/docs/<rel> and /docs/stable/<rel>) now belong to
# the new minor. Release them from the previous stable, or both minors would
# claim the same URL and jekyll-redirect-from would resolve it by build order.
# Version-scoped entries (/docs/1.0/...) stay put. Drop the redirect_from key
# entirely when nothing survives, so we don't leave `redirect_from:` -> null.
strip_alias_redirects() {
  local file="$1"
  awk '
    BEGIN { fm = 0 }
    NR == 1 && /^---$/ { fm = 1; print; next }
    fm == 1 && /^---$/ { fm = 2; print; next }
    fm == 1 && /^redirect_from:/ {
      n = 0
      while ((getline item) > 0) {
        if (item ~ /^[[:space:]]+-[[:space:]]/) {
          # Keep only version-scoped targets, e.g. "- /docs/1.0/x.html".
          if (item ~ /\/docs\/[0-9]+\.[0-9]+\//) kept[n++] = item
          continue
        }
        break
      }
      if (n > 0) {
        print "redirect_from:"
        for (i = 0; i < n; i++) print kept[i]
      }
      # Reprocess the first non-item line that ended the list.
      if (item == "---") { fm = 2 }
      print item
      next
    }
    { print }
  ' "$file" > "$file.tmp" && mv "$file.tmp" "$file"
}

if [[ -n "${PREV_VERSION:-}" && -d "docs/$PREV_VERSION" ]]; then
  echo "==> releasing /docs/ and /docs/stable/ aliases from previous stable (v$PREV_VERSION)"
  while IFS= read -r -d '' f; do
    strip_alias_redirects "$f"
  done < <(find "docs/$PREV_VERSION" "de/docs/$PREV_VERSION" -name "*.html" -print0)
fi

echo "==> bumping docs_path_prefix in _config.yml"
sed -i "s|^docs_path_prefix: \"/docs/[0-9.]\+\"|docs_path_prefix: \"/docs/$VERSION\"|" _config.yml

echo "==> prepending new entry to _data/versions.yml; dropping is_stable from previous"
tmpf=$(mktemp)
sed '/^- channel: dev/,$!{
  /is_stable: true/d
}' _data/versions.yml > "$tmpf"

awk -v ver="$VERSION" '
  BEGIN { inserted = 0 }
  /^- version:/ && !inserted {
    print "- version: \"" ver "\""
    print "  channel: stable"
    print "  baseurl: \"\""
    print "  path_prefix: \"/docs/" ver "\""
    print "  is_stable: true"
    print ""
    inserted = 1
  }
  { print }
' "$tmpf" > _data/versions.yml
rm -f "$tmpf"

echo
echo "==> done. Next steps:"
echo "    1. Review the diff (git diff)."
echo "    2. bundle exec jekyll build  &&  spot-check pages from each version."
echo "    3. git commit -am 'docs: promote v$VERSION to stable' && git tag v$VERSION.0"
