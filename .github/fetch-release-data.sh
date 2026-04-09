#!/usr/bin/env bash
set -euo pipefail

# Fetch release data from GitHub API into _data/ for Jekyll.

API="https://api.github.com/repos"
DATA_DIR="_data"

mkdir -p "$DATA_DIR"

curl -sf -H "Accept: application/vnd.github+json" \
  ${GITHUB_TOKEN:+-H "Authorization: Bearer ${GITHUB_TOKEN}"} \
  "${API}/librescoot/installer/releases/latest" \
  | jq '{tag_name, assets: [.assets[] | {name, size, url: .browser_download_url}]}' \
  > "${DATA_DIR}/installer.json"

echo "installer: $(jq -r .tag_name "${DATA_DIR}/installer.json")"
