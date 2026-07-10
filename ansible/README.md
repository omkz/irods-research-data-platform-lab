# Ansible

This directory contains a simple Ansible playbook for preparing a local development environment.

## Purpose

The playbook installs basic tools used by this project:

- Python 3
- Python venv
- pip
- make
- curl
- git

## Requirements

Ansible must be installed locally before running the playbook.

On Ubuntu/Linux Mint:

    sudo apt update
    sudo apt install ansible -y

Check installation:

    ansible --version
    ansible-playbook --version

## Playbook

    ansible/local-dev-setup.yml

## Run

From the project root:

    ansible-playbook ansible/local-dev-setup.yml --ask-become-pass

The `--ask-become-pass` option asks for the sudo password because the playbook installs system packages.

## Notes

This playbook does not install or configure iRODS server.

It is intentionally small and focused on local development setup.
