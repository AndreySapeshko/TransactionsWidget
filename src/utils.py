import json, os


def converter_from_json(filename: str) -> list[dict]:
    result = []
    if os.path.exists(filename):
        with open(filename) as file:
            data = json.load(file)
        if type(data) is list and len(data) != 0:
            result = data
    return result