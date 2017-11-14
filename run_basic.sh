#!/bin/bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

docker build -t nlu_presentation "$DIR"
docker run -it --rm nlu_presentation
