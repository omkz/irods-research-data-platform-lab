#!/usr/bin/env bash

set -euo pipefail

IRODS_BASE="${IRODS_BASE:-/tempZone/home/rods/research-lab}"
COLLECTION="${IRODS_BASE}/wheat-research-sample"

echo "Creating iRODS collection:"
echo "$COLLECTION"

imkdir -p "$COLLECTION"

echo "OK: collection ready"
ils "$IRODS_BASE"
