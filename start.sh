#!/bin/bash
# Check if the environment and browser arguments are provided
if [ -z "$1" ]; then
  echo "Usage: $0 <environment>"
  echo "Example: $0 test"
  exit 1
fi

# Load environment variables from the specified .env file
ENV_FILE=".env.$1"
if [ -f "$ENV_FILE" ]; then
  export $(grep -v '^#' "$ENV_FILE" | xargs)
else
  echo "$ENV_FILE not found. Please make sure it exists."
  exit 1
fi


bash docker.sh

# Start the Selenium Grid in detached mode
docker compose -f docker-compose.yml up -d

#This variable is widely used througth the tests to point to the selenium hub.
export HUB_URL="http://$HUB_CONTAINER_DOMAIN:4444"
 
# Function to wait for a container to be healthy with a timeout
wait_for_health() {
  local container_name=$1
  local timeout=$2
  local start_time=$(date +%s)

  echo "Waiting for $container_name to be healthy..."

  # Determine the host and port
  local host=${HUB_CONTAINER_NAME}
  local port="4444"       # Default port for Selenium Hub

  while true; do
    echo "Get node status from: " $HUB_URL"/status"

    # Check if the Selenium Hub is ready by querying the status endpoint
    response=$(curl -s --connect-timeout 5 $HUB_URL"/status")

    # Parse the "ready" field using jq
    ready=$(echo "$response" | jq -r '.value.ready')

    if [[ "$ready" == "true" ]]; then
      echo "$container_name is ready."
      break
    fi

    # Check for timeout
    current_time=$(date +%s)
    elapsed_time=$((current_time - start_time))
    if [[ $elapsed_time -ge $timeout ]]; then
      echo "Timed out waiting for $container_name to be ready. The environment will be revoked."
      docker compose down
      exit 1
    fi

    echo "Still waiting for $container_name to be ready..."
    sleep 3
  done
}

# Set timeout (e.g., 120 seconds)
timeout=120

# Wait for selenium-hub to be healthy
wait_for_health ${HUB_CONTAINER_NAME} $timeout

# Wait for chrome node to be healthy
wait_for_health ${CHROME_CONTAINER_NAME} $timeout

# Wait for firefox node to be healthy
wait_for_health ${FIREFOX_CONTAINER_NAME} $timeout

echo "Selenium Grid is ready. Running tests..."

echo "Set default driver to : chrome"
export DEFAULT_DRIVER="chrome"

# Run the Python tests for chrome
python -m unittest

echo "Set default driver to : firefox"
export DEFAULT_DRIVER="firefox"

# Run the Python tests for firefox
python -m unittest

# Stop and remove the containers after the tests finish
docker compose down