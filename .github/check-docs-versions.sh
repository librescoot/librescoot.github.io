#!/usr/bin/env bash
# Fail if a released firmware minor has no docs folder yet.
#
# Pulls non-prerelease, non-draft semver releases from librescoot/librescoot,
# extracts unique X.Y minors, and checks docs/<minor>/ + de/docs/<minor>/
# exist on this repo. The intent: docs and firmware ship together — if
# v1.1.0 is out, /docs/1.1/ should be live.

set -euo pipefail

API="https://api.github.com/repos"
REPO="librescoot/librescoot"

tags=$(curl -sf -H "Accept: application/vnd.github+json" \
  ${GITHUB_TOKEN:+-H "Authorization: Bearer ${GITHUB_TOKEN}"} \
  "${API}/${REPO}/releases?per_page=100" \
  | jq -r '.[] | select(.prerelease == false and .draft == false) | .tag_name' \
  | grep -E '^v[0-9]+\.[0-9]+\.[0-9]+$' || true)

if [ -z "$tags" ]; then
  echo "No stable firmware releases found — nothing to check."
  exit 0
fi

minors=$(echo "$tags" | sed -E 's/^v([0-9]+\.[0-9]+)\..*$/\1/' | sort -u)

missing=()
for m in $minors; do
  if [ ! -d "docs/$m" ] || [ ! -d "de/docs/$m" ]; then
    missing+=("$m")
  fi
done

if [ ${#missing[@]} -gt 0 ]; then
  echo "::error::Released firmware minor(s) without docs: ${missing[*]}"
  echo
  echo "Each released stable firmware minor (X.Y) needs both docs/<minor>/ AND de/docs/<minor>/."
  echo "Run scripts/release-new-minor.sh <minor> to seed one from the current docs/dev/."
  exit 1
fi

echo "All released firmware minors have docs:"
for m in $minors; do echo "  - $m"; done
