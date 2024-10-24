#!/bin/bash

# Function to check if the Docker daemon is running
is_docker_running() {
    docker info >/dev/null 2>&1
}

# Function to start the Docker daemon
start_docker() {
    echo "Starting Docker daemon..."
    sudo systemctl start docker
}

# Check if Docker daemon is running
if ! is_docker_running; then
    echo "Docker daemon is not running. Starting Docker..."
    start_docker
    # Give some time for Docker to start
    sleep 5
    if ! is_docker_running; then
        echo "Failed to start Docker daemon. Please check your installation."
        exit 1
    fi
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