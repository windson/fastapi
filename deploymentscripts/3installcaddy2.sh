#!/bin/bash

echo "Installing Caddy2 on Ubuntu 18.0 or later"
echo "deb [trusted=yes] https://apt.fury.io/caddy/ /"     | sudo tee -a /etc/apt/sources.list.d/caddy-fury.list
sudo apt update
sudo apt install -y caddy

caddy version

sudo mkdir -p /var/log/caddy && sudo chown caddy:caddy /var/log/caddy


