#!/usr/bin/env bash

set -euo pipefail

IRODS_BASE="${IRODS_BASE:-/tempZone/home/rods/research-lab}"
COLLECTION="${IRODS_BASE}/wheat-research-sample"

echo "Attaching metadata to iRODS collection:"
echo "$COLLECTION"

if ! ils "$COLLECTION" >/dev/null 2>&1; then
  echo "ERROR: collection does not exist: $COLLECTION"
  echo "Run './scripts/ingest_dataset.sh' first."
  exit 1
fi

add_metadata() {
  local attribute="$1"
  local value="$2"

  # Remove the same AVU first to avoid duplicate metadata when the script is re-run.
  imeta rm -C "$COLLECTION" "$attribute" "$value" >/dev/null 2>&1 || true
  imeta add -C "$COLLECTION" "$attribute" "$value"
}

add_metadata "dataset_id" "wheat-research-sample"
add_metadata "title" "Wheat Growth Sample Dataset"
add_metadata "project" "wheat-growth-2026"
add_metadata "owner" "research-data-team"
add_metadata "discipline" "agriculture"
add_metadata "organism" "wheat"
add_metadata "data_type" "plant_measurement"
add_metadata "location" "greenhouse"
add_metadata "retention" "training"
add_metadata "license" "CC-BY-4.0"

echo "OK: metadata attached"

imeta ls -C "$COLLECTION"
