#!/bin/sh

set -e

SCRIPT=$(readlink -f "$0")
DIR=$(dirname "$SCRIPT")

docker build --pull -t nlu_presentation "$DIR"
docker run -it --rm -p 8080:8080 nlu_presentation /examples/rasa/nlu.py
