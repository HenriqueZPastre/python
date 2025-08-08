import json

def read_json(file_path: str) -> list:
    with open(file_path, 'r') as file:
        return json.load(file)