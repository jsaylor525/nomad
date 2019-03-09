#!/bin/bash

function nomad_safety_check() {
  if [[ -z "${NOMAD_HOME}" ]]; then
    echo "nomad environment not configured"
    exit -1
  fi

  conda activate ${NOMAD_VIRTUAL_ENV} || exit -1
}

function nomad_start_server() {
  nomad_safety_check

  pushd ${NOMAD_HOME}/nomad
  python manage.py runserver
  popd
}
export -f nomad_start_server


function nomad_sql_update() {
  nomad_safety_check

  pushd ${NOMAD_HOME}/nomad
  python manage.py migrate
  popd
}
export -f nomad_sql_update