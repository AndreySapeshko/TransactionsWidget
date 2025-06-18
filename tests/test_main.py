import pytest
import pandas as pd
import json


from src.main import (user_input_validation, greetings_and_import_data,
                      filtered_transactions_by_state, sorted_transactions_by_date,
                      filtered_transactions_by_description, masked_account_card)
from src.utils import converter_from_json
from src.reader import read_from_csv, read_from_xlcx


expecter = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "amount": "31957.58",
        "currency_name": "руб.",
        "currency_code": "RUB",
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "amount": "8221.37",
        "currency_name": "USD",
        "currency_code": "USD",
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "amount": "9824.07",
        "currency_name": "USD",
        "currency_code": "USD",
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }
]

coll = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "amount": "31957.58",
        "currency_name": "руб.",
        "currency_code": "RUB",
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "amount": "8221.37",
        "currency_name": "USD",
        "currency_code": "USD",
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "amount": "9824.07",
        "currency_name": "USD",
        "currency_code": "USD",
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }
]

@pytest.mark.parametrize('inputs,expected,expected_output', [
    (['3', 'exit'], ['1', '2', '3'], '3'),
    (['invalid', '2', 'exit'], ['1', '2'], '2'),
    (['a', 'b', 'exit'], ['1'], 'exit')
])
def test_user_input_validation(inputs, expected, expected_output, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    assert user_input_validation(expected, 'Введите: ') == expected_output


@pytest.mark.parametrize('inputs,expected,expect', [
    (['0', '1'], ['1', '2', '3'], converter_from_json('../data/operations.json')),
    (['5', '2'], ['1', '2', '3'], read_from_csv('../data/transactions.csv')),
    (['4', '8', '3'], ['1', '2', '3'], read_from_xlcx('../data/transactions_excel.xlsx')),
    (['9', 'exit'], ['1', '2', '3'], [])
])
def test_greetings_and_import_data(inputs, expected, expect, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    assert greetings_and_import_data('Input: ') == expect
