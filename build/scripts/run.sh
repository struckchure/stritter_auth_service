#!/usr/bin/env bash

set -e

python src/main.py migrate
python src/main.py run-server
