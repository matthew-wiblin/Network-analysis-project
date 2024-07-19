#!/bin/bash

# Update the package list
echo "--- Updating package list ---"
sudo apt-get update

# Upgrade the installed packages
echo "--- Upgrading installed packages ---"
sudo apt-get upgrade -y

# Install Python 3
echo "--- Installing Python 3 ---"
sudo apt-get install -y python3

# Verify installation
echo "--- Verifying Python 3 installation ---"
python3 --version

echo "--- Update and installation complete ---"
