import random
from typing import Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator[dict]:
    """ генерируем транзакции из кортежа транзакций фильтруя по валюте """

    for i in range(len(transactions)):
        if transactions[i]['operationAmount']['currency']['code'] == currency:
            yield transactions[i]


def transaction_descriptions(transactions: list) -> Iterator[str]:
    """ генерируем из кортежа транзакций описание """

    for i in range(len(transactions)):
        yield transactions[i]['description']


def card_number_generator(num_from: int, num_to: int) -> Iterator[str]:
    """ генерирует номер карты в заданном диапозоне """

    layout = '0000000000000000'
    while True:
        rand_num = str(random.randint(num_from, num_to))
        card_number = layout[:-len(rand_num)] + rand_num
        yield f'{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}'
