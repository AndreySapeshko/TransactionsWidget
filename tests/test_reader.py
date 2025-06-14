import pytest
import pandas as pd
import csv


from src.reader import read_from_csv


excepted = [{'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0,
             'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
             'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
            {'id': 3598919, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740.0,
             'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
             'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
            {'id': 593027, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': 30368.0,
             'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097',
             'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'},
            {'id': 366176, 'state': 'EXECUTED', 'date': '2020-08-02T09:35:18Z', 'amount': 29482.0,
             'currency_name': 'Rupiah', 'currency_code': 'IDR', 'from': 'Discover 0325955596714937',
             'to': 'Visa 3820488829287420', 'description': 'Перевод с карты на карту'},
            {'id': 5380041, 'state': 'CANCELED', 'date': '2021-02-01T11:54:58Z', 'amount': 23789.0,
             'currency_name': 'Peso', 'currency_code': 'UYU', 'from': None, 'to': 'Счет 23294994494356835683',
             'description': 'Открытие вклада'}
            ]


def test_read_csv():
    assert read_from_csv('../data/test_transactions.csv') == excepted
