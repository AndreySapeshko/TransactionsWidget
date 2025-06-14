import json
import os
import logging


logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/utils.log', 'w', encoding='utf-8')
file_formater = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def converter_from_json(filename: str) -> list[dict]:
    """ конвертирует json файл в python, если файла нет или пустой вернет пустой список """

    json_data: list[dict] = []
    logger.info(f'проверяем существует ли файл {filename}')
    if os.path.exists(filename):
        try:
            logger.info('открываем файл для чтения')
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except json.JSONDecodeError as jde:
            logger.error(f'произошла ошибка при открытии файла {jde}')
            return json_data
        except FileNotFoundError as fnf:
            logger.error(f'произошла ошибка при открытии файла {fnf}')
            return json_data
        if type(data) is list and len(data) != 0:
            json_data = data
        logger.info('конвертация успешно завершена')
    return json_data
