#!/bin/bash

set -e
set -x

if [[ ! -e "Dockerfile" ]]
then
    echo "ERROR: Could not find Dockerfile."
    exit 2
fi

/usr/bin/docker image rm mushroom:latest
/usr/bin/docker build -t mushroom:latest . --no-cache
