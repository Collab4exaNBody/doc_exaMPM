#!/bin/bash
# Copies the exaMPM configuration files, example decks and example pictures used by the documentation pages.
# Usage: scripts/sync_files.sh <exaMPM source tree>
set -e
SRC=${1:?usage: $0 <exaMPM source tree>}
DOCS=$(cd "$(dirname "$0")/.." && pwd)/docs
cp "${SRC}"/data/config/*.msp "${SRC}"/example/*/*.msp "${DOCS}/files/"
mkdir -p "${DOCS}/images/examples"
cp "${SRC}"/example/*/*.png "${DOCS}/images/examples/"
echo "copied $(ls "${SRC}"/data/config/*.msp "${SRC}"/example/*/*.msp | wc -l) files to ${DOCS}/files" \
     "and $(ls "${SRC}"/example/*/*.png | wc -l) pictures to ${DOCS}/images/examples"
