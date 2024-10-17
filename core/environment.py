import os

from dotenv import load_dotenv


def target_url(environment="development"):
    # Determine which environment file to load
    environment = os.getenv('ENVIRONMENT', environment)  # Default to 'development'

    # Map environment to corresponding .env file
    env_file = f".env.{environment}"

    # Load the appropriate .env file
    load_dotenv(env_file)

    # Read the environment variable
    return os.getenv('TARGET_URL')
