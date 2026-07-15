#!/usr/bin/env bash
# Fail if the docs describe a settings key that the matching firmware doesn't have.
#
# settings-service ships settings.schema.json, a flat map of every real
# settings key. For each docs/<minor>/ we resolve the settings-service
# SRCREV that the newest firmware release of that minor was built from,
# fetch the schema at exactly that revision, and compare it against the
# keys documented in the settings tables.
#
# Errors on documented-but-not-in-schema. That direction is precise: a key
# in the docs and not in the schema is one nobody can set. This is how
# scooter.battery-ignores-seatbox survived a rename for three months.
#
# Warns on user-visible-in-schema-but-undocumented. That direction is
# advisory: not every key needs a docs row, and non-user-visible keys are
# mostly internal plumbing, so only user-visible ones are worth a nudge.
#
# Warns on a documented key that looks like a real one with its service
# prefix missing (a bare "hibernation-timer" where the key is
# "pm.hibernation-timer"). Only a warning: the docs also tabulate Redis
# fields and CLI flags, so a bare word matching a key's last segment is
# suggestive, not proof. See PREFIX_ALLOWLIST.
#
# What it cannot catch: prose. A row can name the right key and still lie
# about its default, range, or semantics. The schema has no opinion on
# whether "minimum 300 s" is true.

set -euo pipefail

API="https://api.github.com/repos"
RAW="https://raw.githubusercontent.com"
FW_REPO="librescoot/librescoot"
SETTINGS_REPO="librescoot/settings-service"

# Bare words that legitimately appear as a first-cell <code> and collide
# with the last segment of a real settings key. These are Redis hash
# fields (engine-ecu.kers -> "kers", gps.latitude -> "latitude"), not
# settings rows with a dropped prefix.
PREFIX_ALLOWLIST="kers latitude"

gh_curl() {
  curl -sf -H "Accept: application/vnd.github+json" \
    ${GITHUB_TOKEN:+-H "Authorization: Bearer ${GITHUB_TOKEN}"} "$@"
}

# Settings keys are rendered as the first cell of a table row. Anchoring on
# <tr><td><code> keeps flags (--format), subcommands (vehicle lock) and
# inline prose mentions out of the extraction.
extract_documented_keys() {
  local dir="$1"
  local de_dir="de/$dir"
  local dirs=("$dir")
  [ -d "$de_dir" ] && dirs+=("$de_dir")
  grep -rhoE '<tr><td><code>[a-z0-9][a-z0-9.-]*\.[a-z0-9.-]+</code>' "${dirs[@]}" 2>/dev/null \
    | sed -E 's|<tr><td><code>||; s|</code>||' \
    | sort -u
}

# Same cells, but the bare (undotted) ones, for the missing-prefix check.
extract_bare_words() {
  local dir="$1"
  local de_dir="de/$dir"
  local dirs=("$dir")
  [ -d "$de_dir" ] && dirs+=("$de_dir")
  grep -rhoE '<tr><td><code>[a-z0-9][a-z0-9-]*</code>' "${dirs[@]}" 2>/dev/null \
    | sed -E 's|<tr><td><code>||; s|</code>||' \
    | sort -u
}

# The newest stable release of a minor is the one docs/<minor>/ describes.
newest_tag_for_minor() {
  local minor="$1"
  gh_curl "${API}/${FW_REPO}/releases?per_page=100" \
    | jq -r '.[] | select(.prerelease == false and .draft == false) | .tag_name' \
    | grep -E "^v${minor//./\\.}\.[0-9]+$" \
    | sort -V | tail -1
}

settings_srcrev_at_tag() {
  local tag="$1"
  curl -sf "${RAW}/${FW_REPO}/${tag}/stable.env" \
    | grep '^SRCREV_settings_service' | cut -d'"' -f2
}

fetch_schema() {
  local rev="$1"
  curl -sf "${RAW}/${SETTINGS_REPO}/${rev}/settings.schema.json"
}

ERRORS=0
WARNINGS=0
CHECKED=0

# docs/dev tracks settings-service main; frozen minors track their release.
versions=()
for d in docs/*/; do
  v=$(basename "$d")
  [[ "$v" =~ ^[0-9]+\.[0-9]+$ || "$v" == "dev" ]] && versions+=("$v")
done

for v in "${versions[@]}"; do
  if [ "$v" = "dev" ]; then
    rev="main"
    label="dev (settings-service main)"
  else
    tag=$(newest_tag_for_minor "$v" || true)
    if [ -z "${tag:-}" ]; then
      echo "NOTE: docs/$v has no stable firmware release yet; skipping."
      echo
      continue
    fi
    rev=$(settings_srcrev_at_tag "$tag" || true)
    if [ -z "${rev:-}" ]; then
      echo "::error::could not resolve SRCREV_settings_service from stable.env at $tag"
      : $((ERRORS++))
      continue
    fi
    label="$v (firmware $tag, settings-service ${rev:0:8})"
  fi

  schema=$(fetch_schema "$rev" || true)
  if [ -z "${schema:-}" ]; then
    echo "::error::could not fetch settings.schema.json at ${rev}"
    : $((ERRORS++))
    continue
  fi

  schema_keys=$(echo "$schema" | jq -r 'keys[]' | sort)
  visible_keys=$(echo "$schema" | jq -r 'to_entries[] | select(.value["user-visible"] == true) | .key' | sort)
  documented=$(extract_documented_keys "docs/$v")

  echo "== $label"
  echo "   $(echo "$documented" | grep -c . || true) keys documented, $(echo "$schema_keys" | grep -c . || true) in schema"

  phantom=$(comm -23 <(echo "$documented") <(echo "$schema_keys"))
  if [ -n "$phantom" ]; then
    while read -r k; do
      [ -z "$k" ] && continue
      echo "::error::docs/$v documents '$k', which is not in settings.schema.json at ${rev:0:8}"
      : $((ERRORS++))
    done <<< "$phantom"
  fi

  # A bare word matching a real key's last segment, where the full key is
  # not also documented, is very likely a dropped service prefix.
  suffixes=$(echo "$schema" | jq -r 'keys[] | select(contains(".")) | split(".") | last' | sort -u)
  bare=$(extract_bare_words "docs/$v")
  for w in $(comm -12 <(echo "$bare") <(echo "$suffixes")); do
    case " $PREFIX_ALLOWLIST " in *" $w "*) continue ;; esac
    full=$(echo "$schema_keys" | grep -E "\.${w}$" | head -1)
    if ! echo "$documented" | grep -qx "$full"; then
      echo "::warning::docs/$v documents bare '$w'; the real key looks like '$full'"
      : $((WARNINGS++))
    fi
  done

  undocumented=$(comm -13 <(echo "$documented") <(echo "$visible_keys"))
  if [ -n "$undocumented" ]; then
    while read -r k; do
      [ -z "$k" ] && continue
      echo "::warning::docs/$v does not document user-visible setting '$k'"
      : $((WARNINGS++))
    done <<< "$undocumented"
  fi

  : $((CHECKED++))
  echo
done

echo "Checked $CHECKED version(s): $ERRORS error(s), $WARNINGS warning(s)."
[ "$ERRORS" -gt 0 ] && exit 1
exit 0
