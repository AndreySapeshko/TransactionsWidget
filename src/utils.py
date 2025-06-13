import json
import os


def converter_from_json(filename: str) -> list[dict]:
    """ конвертирует json файл в python, если файла нет или пустой вернет пустой список """

    json_data: list[dict] = []
    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            return json_data
        except FileNotFoundError:
            return json_data
        if type(data) is list and len(data) != 0:
            json_data = data
    return json_data
