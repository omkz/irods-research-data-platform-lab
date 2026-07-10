#!/usr/bin/env bash

set -euo pipefail

echo "Checking iRODS connection..."

if ! ils >/dev/null 2>&1; then
  echo "ERROR: cannot connect to iRODS"
  echo "Run 'iinit' first, then try again."
  exit 1
fi

echo "OK: iRODS connection is working"
