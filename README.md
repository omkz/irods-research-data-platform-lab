# iRODS Research Data Platform Lab

A small research data management lab using iRODS, Python, Bash, metadata validation, Prometheus, Grafana, Docker Compose, Ansible, tests, and CI.

![CI](https://github.com/omkz/irods-research-data-platform-lab/actions/workflows/ci.yml/badge.svg)

## Goal

This project demonstrates a practical research data workflow:

- organize a sample research dataset
- describe the dataset with YAML metadata
- validate metadata with Python
- generate a dataset manifest with SHA256 checksums
- ingest data into an iRODS collection
- attach metadata to the iRODS collection
- query datasets by metadata
- expose simple health metrics for Prometheus
- document workflows for operators and researchers

## Workflow

    Dataset files
      ↓
    Metadata YAML
      ↓
    Python validation
      ↓
    Manifest generation
      ↓
    iRODS ingestion
      ↓
    Metadata attachment
      ↓
    Metadata-based discovery
      ↓
    Prometheus/Grafana monitoring

## Tech Stack

- iRODS
- Python
- Bash
- YAML
- Linux
- Docker Compose
- Prometheus
- Grafana
- Ansible
- GitHub Actions
- pytest

## Quick Start

Create virtual environment:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Run local validation:

    make local

Run iRODS workflow:

    iinit
    make irods-demo

Run monitoring exporter:

    make metrics

Open metrics:

    http://localhost:8000/metrics

Run Prometheus and Grafana:

    docker compose up prometheus grafana

Prometheus:

    http://localhost:9090

Grafana:

    http://localhost:3000

## Documentation

- [Architecture](docs/architecture.md)
- [Demo Guide](docs/demo.md)
- [Operator Guide](docs/operator-guide.md)
- [Researcher User Guide](docs/researcher-user-guide.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Monitoring](monitoring/README.md)
- [Ansible](ansible/README.md)

## Current Scope

This is a learning-focused lab project, not a production iRODS deployment.

The project focuses on:

- metadata-driven research data workflow
- local iRODS automation
- validation and testing
- operational documentation
- basic monitoring concepts

## Status

MVP complete.
