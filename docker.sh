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

if is_docker_installed; then
    echo "Docker is already installed."
else
    echo "Docker is not installed. Installing now..."
    install_docker
    echo "Docker installation completed."

    # Optional: Add the current user to the Docker group
    sudo usermod -aG docker $USER
    echo "Added $USER to the Docker group. Log out and back in to use Docker without sudo."
fi