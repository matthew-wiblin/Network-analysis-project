#!/bin/bash

echo "--- Updating package list ---"
sudo apt-get update

echo "--- Upgrading installed packages ---"
sudo apt-get upgrade -y

echo "Installing script dependencies"
sudo apt-get install speedtest-cli

echo "Installing g++, libpcap"
sudo apt install g++
sudo apt-get install libpcap-dev

if command -v python3 > /dev/null 2>&1; then
    echo "--- Python 3 is already installed ---"
else
    echo "--- Python 3 is not installed, installing now ---"
    sudo apt-get install -y python3
fi

echo "--- Verifying Python 3 installation ---"
python3 --version

echo "--- Update and installation complete ---"
