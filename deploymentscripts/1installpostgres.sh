#!/bin/bash
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt update
sudo apt -y install postgresql-13
sudo su - postgres -c "createdb fastapidb"
sudo su - postgres -c "createuser -P -s -e fastapiuser"
# Enter password for new role: 
# Enter it again:
sudo -u postgres psql -c "grant all privileges on database fastapidb to fastapiuser;"
