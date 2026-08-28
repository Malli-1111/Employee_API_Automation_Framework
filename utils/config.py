"""
Configuration utility for the API automation framework.

Loads environment-specific configuration from JSON files
and exposes commonly used configuration values such as BASE_URL.
"""
import json
import os


def load_config():
    """
    Load configuration for the selected test environment.

    The environment is read from the TEST_ENV environment variable.
    If TEST_ENV is not provided, the framework uses the dev environment.

    Returns:
        dict: Environment-specific configuration values.
    """

    env = os.getenv("TEST_ENV", "dev")

    with open(f"config/{env}.json", "r") as file:
        return json.load(file)


config = load_config()

BASE_URL = config["BASE_URL"]