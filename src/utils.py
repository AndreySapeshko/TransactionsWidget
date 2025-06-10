import json
import os


def converter_from_json(filename: str) -> list[dict]:
    """ конвертирует json файл в python, если файла нет или пустой вернет пустой список """

    result = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        if type(data) is list and len(data) != 0:
            result = data
    return result
