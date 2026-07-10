# Researcher User Guide

This guide explains the research data workflow from a researcher perspective.

## Dataset

The sample dataset is stored in:

    datasets/wheat-research-sample/

It contains wheat plant measurement data.

## Metadata

The dataset is described using a YAML metadata file:

    metadata/wheat-research-sample.yaml

The metadata includes information such as:

- dataset title
- project name
- owner
- discipline
- organism
- data type
- location
- license

## Why Metadata Matters

Metadata helps researchers find and understand datasets.

Instead of searching by file name only, users can search by meaningful fields such as:

    project = wheat-growth-2026
    organism = wheat
    discipline = agriculture

## Workflow

    Research data
      ↓
    Metadata description
      ↓
    Validation
      ↓
    iRODS upload
      ↓
    Metadata-based discovery

## Example Search

A researcher can find the dataset by metadata:

    ATTR=project VALUE=wheat-growth-2026 make query

Or:

    ATTR=organism VALUE=wheat make query

## Expected Result

The query returns the iRODS collection where the dataset is stored:

    /tempZone/home/rods/research-lab/wheat-research-sample
