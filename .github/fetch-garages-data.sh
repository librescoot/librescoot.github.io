#!/usr/bin/env bash
# Fetch the latest garage data from the unu-garages-data Pages output.
# Mirrors fetch-release-data.sh: runs pre-build so Jekyll sees site.data.garages.
set -euo pipefail
cd "$(dirname "$0")/.."

URL="https://librescoot.org/unu-garages-data/garages_v2.json"
OUT="_data/garages.json"

mkdir -p _data
curl -fsSL "$URL" -o "$OUT"
jq -e '.garages | length > 0' "$OUT" > /dev/null
echo "fetched $(jq '.garages | length' "$OUT") garages -> $OUT"
