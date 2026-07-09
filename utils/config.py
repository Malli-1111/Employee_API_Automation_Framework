import json
import os


def load_config():

    env = os.getenv("TEST_ENV", "dev")

    with open(f"config/{env}.json", "r") as file:
        return json.load(file)


config = load_config()

BASE_URL = config["BASE_URL"]