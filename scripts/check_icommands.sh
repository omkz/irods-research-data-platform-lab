#!/usr/bin/env bash

set -euo pipefail

required_commands=("iinit" "ils" "imkdir" "iput" "imeta" "iquest")

for command in "${required_commands[@]}"; do
  if ! command -v "$command" >/dev/null 2>&1; then
    echo "ERROR: required iRODS command not found: $command"
    exit 1
  fi
done

echo "OK: all required iRODS commands are available"
