import random


def filter_by_currency(transactions: tuple, currency: str):
    """ генерируем транзакции из кортежа транзакций фильтруя по валюте """

    for i in range(len(transactions)):
        if transactions[i]['operationAmount']['currency']['code'] == currency:
            yield transactions[i]


