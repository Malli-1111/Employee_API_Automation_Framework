import json

ENV = "dev"
def load_config():

    with open(f"config/{ENV}.json", "r") as file:
        return json.load(file)

config = load_config()
BASE_URL = config["BASE_URL"]