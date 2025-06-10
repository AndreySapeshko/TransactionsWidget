import json, os


def converter_from_json(filename: str) -> list[dict]:
    result = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        if type(data) is list and len(data) != 0:
            result = data
    return result


print(len(converter_from_json('../data/operations.json')))
