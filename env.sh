#!/bin/bash

if [[ $_ == $0 ]]; then
    echo "This script is being run in a subshell, this script needs to be run on the current process, use source."
    exit -1
fi

export DATABASE_URL="postgres://localhost/lecture4"
export PGUSER="jsaylor"
export PGPASSWORD="password"
export FLASK_APP="application.py"
