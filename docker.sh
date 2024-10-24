#!/bin/bash

# Function to check if Docker is installed
is_docker_installed() {
    command -v docker >/dev/null 2>&1
}

# Install Docker for Ubuntu
install_docker() {
    echo "Installing Docker on Ubuntu..."
    apt-get update
    apt-get install -y apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    apt-get update
    apt-get install -y docker-ce
}

# Function to check if the Docker daemon is running
is_docker_running() {
    docker info >/dev/null 2>&1
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
    echo "Docker daemon is not running. Please start Docker manually."
else
    echo "Docker daemon is running."
fi

# Optional: Add the current user to the Docker group if not already a member
if [[ $(groups "$USER" | grep -o 'docker') != "docker" ]]; then
    echo "Adding $USER to the Docker group..."
    usermod -aG docker "$USER" || echo "Failed to add $USER to the Docker group."
    echo "Added $USER to the Docker group. Log out and back in to use Docker without sudo."
else
    echo "$USER is already in the Docker group."
fi