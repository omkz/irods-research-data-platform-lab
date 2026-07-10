# Troubleshooting

This document lists common issues when running the research data management lab.

## iRODS command not found

Error example:

    ERROR: required iRODS command not found: iinit

Cause:

iRODS iCommands are not installed or not available in the shell PATH.

Check:

    which iinit
    which ils

Fix:

Install iRODS iCommands or update the PATH so the commands are available.

## Cannot connect to iRODS

Error example:

    ERROR: cannot connect to iRODS
    Run 'iinit' first, then try again.

Cause:

The user is not authenticated to iRODS.

Fix:

    iinit

Then check:

    ils

## Collection does not exist

Error example:

    ERROR: collection does not exist

Cause:

The iRODS collection has not been created yet.

Fix:

    make collection

Or run the full ingestion workflow:

    make ingest

## Metadata validation failed

Error example:

    Metadata validation failed:
    - Missing dataset field: owner

Cause:

The metadata YAML file is missing required fields.

Fix:

Edit:

    metadata/wheat-research-sample.yaml

Then run:

    make validate

## Referenced file does not exist

Error example:

    Referenced file does not exist: datasets/wheat-research-sample/measurements.csv

Cause:

The metadata file references a dataset file that does not exist.

Fix:

Check the path in:

    metadata/wheat-research-sample.yaml

Then confirm the file exists:

    ls datasets/wheat-research-sample/

## Manifest looks strange

The SHA256 values in the manifest are long strings.

Example:

    9f86d081884c7d659a2feaa0c55ad015...

This is normal.

SHA256 is a checksum used to verify that a file has not changed.

## Metadata query returns nothing

Command:

    make query

Cause:

Metadata may not have been attached yet, or the attribute/value is different.

Fix:

Run:

    make metadata

Then query again:

    make query

For custom query:

    ATTR=organism VALUE=wheat make query

## Duplicate metadata

Cause:

The metadata script may be run multiple times.

Fix:

The script removes the same AVU before adding it again, so re-running should be safe.

If needed, inspect metadata manually:

    imeta ls -C /tempZone/home/rods/research-lab/wheat-research-sample
