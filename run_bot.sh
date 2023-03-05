#!/bin/bash

# this script assumes you have docker installed and running on your system.
# we also assume you are running this script from the root of the directory.

# 'start' will start the containter (default)
# 'stop' will stop the container
# 'remove' will stop and delete the container.

# echo "UID=${UID}" > .env
action=${1:-start}

if [[ -z $(which docker) ]]; then
    echo "docker not detected on your system... please install docker."
    exit 1
fi


if [[ $action == 'start' ]]; then
    # this will automatically create the container if it does not exist
    # if the container exists it will start it up.
    # if the container is already running, it will kill it and run it again.
    # -d is for detached mode to run in the background.
    docker compose up -d 
elif [[ $action == 'stop' ]]; then
    docker compose stop
elif [[ $action == 'remove' ]]; then
    # automatically stop the container and remove it.
    docker compose down
else
    echo "please use one of the following actions: [start, stop, remove]"
fi
