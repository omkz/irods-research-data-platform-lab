#!/usr/bin/env bash

set -euo pipefail

ATTR="${ATTR:-project}"
VALUE="${VALUE:-wheat-growth-2026}"

echo "Searching iRODS collections by metadata..."
echo "Attribute: $ATTR"
echo "Value: $VALUE"
echo

iquest "%s" "SELECT COLL_NAME WHERE META_COLL_ATTR_NAME = '$ATTR' AND META_COLL_ATTR_VALUE = '$VALUE'"
