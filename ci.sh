#!/bin/bash

# This script runs all the tests in a fresh virtual environment. Note that it will delete anything found under .venv

set -e

error() {
  echo "ERROR: ${1}" 1>&2
}

fail() {
  error "$1"
  exit 1
}

if [ -n "${VIRTUAL_ENV}" ]; then
  fail "A virtual environment is already active. Deactivate it and try again"
fi

rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python -m unittest
