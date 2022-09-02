#!/bin/bash

SCRIPTDIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P  )"

sudo bash --login -c "cd $SCRIPTDIR && source .env/bin/activate && ./dpifw.py $@"
