#!/bin/bash

cd $HOME
echo "cloning fastapi repo from github"
git clone https://github.com/windson/fastapi.git -b fastapi-postgresql-caddy-linux-deploy
cd fastapi

echo "installing python3-pip and virtualenv"
sudo apt install -y python3-venv

echo "creating virtual environment"
python3 -m venv env

echo "activating virtual environment"
source env/bin/activate

echo "Updating PIP and installing dependent python modules"
pip install --upgrade pip
pip install -r requirements.txt


exit 0
