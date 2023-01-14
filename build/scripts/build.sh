#!/usr/bin/env bash

set -e

docker build . -f build/python/Dockerfile -t struckchure/stritter_auth_service:$@
docker build . -f build/python/Dockerfile -t struckchure/stritter_auth_service:latest

docker build . -f build/python/Dockerfile -t ghcr.io/struckchure/stritter_auth_service:$@
docker build . -f build/python/Dockerfile -t ghcr.io/struckchure/stritter_auth_service:latest
