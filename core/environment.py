import os

from dotenv import load_dotenv


def target_url(environment="local"):
    # Determine which environment file to load
    environment = os.getenv('ENVIRONMENT', environment)  # Default to 'development'

    # Map environment to corresponding .env file
    env_file = f".env.{environment}"

    # Load the appropriate .env file
    load_dotenv(env_file)

    # Read the environment variable
    return os.getenv('TARGET_URL')

def get_hub_url(environment="local"):
    __load_env_store(environment=environment)
    return os.getenv("HUB_URL")


def __load_env_store(environment):
    environment = os.getenv('ENVIRONMENT', environment)  # Default to 'development'

    # Map environment to corresponding .env file
    env_file = f".env.{environment}"

    # Load the appropriate .env file
    load_dotenv(env_file)

def get_default_driver(environment="local"):
    __load_env_store(environment=environment)
    return os.getenv("DEFAULT_DRIVER")
