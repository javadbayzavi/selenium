#!/bin/bash

# Function to check if Docker is installed
is_docker_installed() {
    command -v docker >/dev/null 2>&1
}

# Install Docker for Ubuntu
install_docker() {
    echo "Installing Docker on Ubuntu..."
    sudo apt-get update
    sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    sudo apt-get update
    sudo apt-get install -y docker-ce
    sudo systemctl start docker
    sudo systemctl enable docker
}

# Function to check if the Docker daemon is running
is_docker_running() {
    systemctl is-active --quiet docker
}

# Check if Docker is installed
if is_docker_installed; then
    echo "Docker is already installed."
else
    echo "Docker is not installed. Installing now..."
    install_docker
    echo "Docker installation completed."
fi

# Check if Docker daemon is running
if ! is_docker_running; then
    echo "Docker daemon is not running. Starting Docker..."
    sudo systemctl start docker
fi

# Optional: Add the current user to the Docker group
if ! groups "$USER" | grep -q '\bdocker\b'; then
    echo "Adding $USER to the Docker group..."
    sudo usermod -aG docker "$USER"
    echo "Added $USER to the Docker group. Log out and back in to use Docker without sudo."
else
    echo "$USER is already in the Docker group."
fi