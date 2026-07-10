# Architecture

This project demonstrates a small research data management workflow using local dataset files, metadata validation, iRODS storage, and metadata-based discovery.

## Overview

    Dataset files
      ↓
    Metadata YAML
      ↓
    Python validation
      ↓
    Manifest generation
      ↓
    iRODS collection
      ↓
    Metadata attachment
      ↓
    Metadata query

## Components

### Dataset

The sample dataset is stored locally in:

    datasets/wheat-research-sample/

It contains research data files used for the ingestion workflow.

### Metadata

The dataset metadata is stored in:

    metadata/wheat-research-sample.yaml

The metadata describes the dataset, including project, owner, discipline, organism, data type, location, and license.

### Python Validation

The validation script checks that:

- required metadata fields exist
- the metadata structure is valid
- referenced dataset files exist

Script:

    python/validate_metadata.py

### Manifest Generation

The manifest generator creates a CSV file containing:

- file path
- file size
- SHA256 checksum

Script:

    python/generate_manifest.py

Output:

    datasets/wheat-research-sample/manifest.csv

### Bash Automation

Shell scripts are used to automate operational tasks:

- checking iRODS commands
- checking iRODS connection
- creating iRODS collections
- uploading dataset files
- attaching metadata
- querying metadata

Scripts are stored in:

    scripts/

### iRODS Collection

The default iRODS collection is:

    /tempZone/home/rods/research-lab/wheat-research-sample

This can be changed using:

    export IRODS_BASE=/tempZone/home/your-user/research-lab

### Metadata Discovery

Metadata is attached to the iRODS collection as AVU metadata.

Example:

    project = wheat-growth-2026
    organism = wheat
    discipline = agriculture

The dataset can then be found using metadata queries.

## Design Goals

This project is designed to show:

- research data organization
- metadata-driven discovery
- simple validation before ingestion
- repeatable command-line workflows
- separation between researcher-facing and operator-facing documentation
- basic engineering practices such as testing and CI

## Out of Scope

This lab does not provide:

- production iRODS deployment
- access control policy management
- Kubernetes deployment
- real monitoring dashboards
- large-scale storage configuration

These topics can be added later as extensions.
