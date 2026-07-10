# Operator Guide

This guide describes how to run the local research data management workflow.

## Requirements

- Linux shell
- Python 3
- iRODS iCommands
- Git
- Make

## Setup

Create a Python virtual environment:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## Validate Metadata

    make validate

This checks whether the metadata YAML file has the required fields and references existing dataset files.

## Generate Dataset Manifest

    make manifest

This creates a manifest file containing:

- file path
- file size
- SHA256 checksum

## Check iRODS Commands

    make check

This checks whether required iRODS commands are available.

## Check iRODS Connection

    make healthcheck

If this fails, run:

    iinit

## Create iRODS Collection

    make collection

## Ingest Dataset

    make ingest

This uploads the dataset files into the configured iRODS collection.

## Attach Metadata

    make metadata

This attaches metadata to the iRODS collection.

## Query Metadata

    make query

Custom query:

    ATTR=organism VALUE=wheat make query

## Default iRODS Location

The default iRODS base path is:

    /tempZone/home/rods/research-lab

To override it:

    export IRODS_BASE=/tempZone/home/your-user/research-lab
