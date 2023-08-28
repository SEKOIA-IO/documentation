#!/bin/bash
# Version: 1.0

function dockerCleanInstall {

# Remove old docker
sudo apt-get remove docker docker-engine docker.io containerd runc > /dev/null
echo "---->>> Old docker version deleted"

# Update and install dependencies
sudo apt-get update > /dev/null
sudo apt-get install -y ca-certificates curl gnupg lsb-release > /dev/null
echo "---->>> System updated and prerequisite packages intalled"

# Add Docker's official GPG key
sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "---->>> Docker GPG key collected"

# Set up the repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
echo "---->>> Repository updated, ready to start docker installation"

# Install Docker Engine
sudo apt-get update > /dev/null
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin > /dev/null
echo "---->>> Docker packages intalled"

sudo docker run hello-world
}

function dockerConfiguration {

# Create a folder where the configuration and data of the concentrator will be stored
mkdir sekoiaio-concentrator && cd sekoiaio-concentrator
echo "---->>> Concentrator directory created"

# Create the two files from the template

wget https://raw.githubusercontent.com/SEKOIA-IO/sekoiaio-docker-concentrator/main/docker-compose/intakes.yaml
wget https://raw.githubusercontent.com/SEKOIA-IO/sekoiaio-docker-concentrator/main/docker-compose/docker-compose.yml
echo "---->>> The 2 files were created"
}

# Execute the functions
dockerCleanInstall
dockerConfiguration
