#!/usr/bin/env bash

set -e

docker push struckchure/stritter_auth_service:$@
docker push struckchure/stritter_auth_service:latest

docker push ghcr.io/struckchure/stritter_auth_service:$@
docker push ghcr.io/struckchure/stritter_auth_service:latest
