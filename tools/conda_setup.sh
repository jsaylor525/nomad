#!/bin/bash

export CONDA_NOMAD_ENV="nomad-venv"

function nomad_venv_activate() {
  conda activate ${CONDA_NOMAD_ENV}
  pushd ${NOMAD_HOME}
} 
export -f nomad_venv_activate

nomad_venv_setup() {
  conda create -y --name ${CONDA_NOMAD_ENV} python=3.7
  conda activate ${CONDA_NOMAD_ENV}
  [ ! -z "${NOMAD_HOME}" ] && python ${NOMAD_HOME}/setup.py
}
export -f nomad_venv_setup

function check_conda_for_nomad() {
  local conda_env_list=$(conda env list)

  if [[ -z "${conda_env_list}" ]]; then
    echo "Need to install Anaconda3"
  else
    echo "Conda is installed on this machine"
    if [[ -z "$(echo ${conda_env_list} | grep ${CONDA_NOMAD_ENV})" ]]; then
      echo "Setting up nomad virtual environment"
      nomad_venv_setup
    else
      echo "Nomad virtual environment already configured"
    fi
  fi
}
check_conda_for_nomad
