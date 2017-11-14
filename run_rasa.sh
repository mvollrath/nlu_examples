#!/bin/bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

docker build -t nlu_presentation "$DIR"
docker run -it --rm -p 8080:8080 nlu_presentation /examples/rasa/nlu.py
