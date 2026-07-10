#!/usr/bin/env bash

set -euo pipefail

IRODS_BASE="${IRODS_BASE:-/tempZone/home/rods/research-lab}"
COLLECTION="${IRODS_BASE}/wheat-research-sample"
DATASET_DIR="datasets/wheat-research-sample"

echo "Ingesting dataset into iRODS..."
echo "Local dataset: $DATASET_DIR"
echo "iRODS collection: $COLLECTION"

if [ ! -d "$DATASET_DIR" ]; then
  echo "ERROR: dataset directory not found: $DATASET_DIR"
  exit 1
fi

imkdir -p "$COLLECTION"

iput -f "${DATASET_DIR}/measurements.csv" "$COLLECTION/"
iput -f "${DATASET_DIR}/manifest.csv" "$COLLECTION/" 2>/dev/null || true

echo "OK: dataset uploaded"

ils "$COLLECTION"
