#!/bin/bash
# Copies the exaMPM configuration files and example decks included by the documentation pages.
# Usage: scripts/sync_files.sh <exaMPM source tree>
set -e
SRC=${1:?usage: $0 <exaMPM source tree>}
DST=$(cd "$(dirname "$0")/.." && pwd)/docs/files
cp "${SRC}"/data/config/*.msp "${DST}/"
cp "${SRC}"/example/*.msp "${DST}/"
echo "copied $(ls "${SRC}"/data/config/*.msp "${SRC}"/example/*.msp | wc -l) files to ${DST}"
