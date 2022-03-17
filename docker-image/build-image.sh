#!/bin/bash

set -e
set -x

if [[ ! -e "Dockerfile" ]]
then
    echo "ERROR: Could not find Dockerfile."
    exit 2
fi

if /usr/bin/docker image inspect mushroom:latest > /dev/null 2>&1
then
    /usr/bin/docker image rm mushroom:latest
fi

/usr/bin/docker build -t mushroom:latest . --no-cache
