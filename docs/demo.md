# Demo Guide

This document explains how to demonstrate the research data platform lab.

## 1. Local Validation Demo

Run:

    make local

This runs:

- metadata validation
- manifest generation
- unit tests

Expected result:

    OK: metadata valid
    OK: manifest generated
    tests passed

## 2. iRODS Workflow Demo

Before running the iRODS workflow, authenticate with iRODS:

    iinit

Then run:

    make irods-demo

This runs:

- iRODS command check
- iRODS connection healthcheck
- dataset ingestion
- metadata attachment
- metadata query

Expected query result:

    /tempZone/home/rods/research-lab/wheat-research-sample

## 3. Monitoring Demo

Start the metrics exporter:

    make metrics

Open metrics endpoint:

    http://localhost:8000/metrics

Expected metrics:

    irods_healthcheck_status 1.0
    metadata_validation_status 1.0
    irods_healthcheck_total

Start Prometheus and Grafana:

    docker compose up prometheus grafana

Open Prometheus:

    http://localhost:9090

Example queries:

    irods_healthcheck_status
    metadata_validation_status
    irods_healthcheck_total

Open Grafana:

    http://localhost:3000

Default local login:

    admin / admin

## Demo Summary

This project demonstrates:

- research dataset organization
- metadata validation
- dataset manifest generation with checksums
- iRODS ingestion
- iRODS metadata attachment
- metadata-based discovery
- Prometheus metrics exporter
- Prometheus/Grafana monitoring workflow
- automated tests and CI
