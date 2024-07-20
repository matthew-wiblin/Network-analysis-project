#!/bin/bash

echo "--- Updating package list ---"
sudo apt-get update

echo "--- Upgrading installed packages ---"
sudo apt-get upgrade -y

echo "Installing script dependencies"
sudo apt-get install speedtest-cli

echo "--- Installing Python 3 ---"
sudo apt-get install -y python3

echo "--- Verifying Python 3 installation ---"
python3 --version

echo "--- Update and installation complete ---"
