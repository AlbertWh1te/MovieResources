#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'
scp -r dist/* vultr:/webapp/movies/
