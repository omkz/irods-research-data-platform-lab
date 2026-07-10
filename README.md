# iRODS Research Data Platform Lab

![CI](https://github.com/omkz/irods-research-data-platform-lab/actions/workflows/ci.yml/badge.svg)

A small learning project to explore research data management workflows using iRODS, Python, Bash, and metadata.

## Goal

This project demonstrates how research data can be:

* organized into collections
* described with metadata
* validated with Python
* automated with Bash scripts
* prepared for storage in iRODS

## Planned Workflow

```text
Dataset files
  ↓
Metadata YAML
  ↓
Python validation
  ↓
iRODS collection
  ↓
Metadata-based search
```

## Tech Stack

* iRODS
* Python
* Bash
* YAML
* Linux

## Status

Work in progress.

## Documentation

- [Architecture](docs/architecture.md)
- [Operator Guide](docs/operator-guide.md)
- [Researcher User Guide](docs/researcher-user-guide.md)
- [Troubleshooting](docs/troubleshooting.md)

## Quick Start

Create a virtual environment:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Run local validation:

    make validate
    make manifest
    make test

Run iRODS workflow:

    make check
    make healthcheck
    make ingest
    make metadata
    make query
