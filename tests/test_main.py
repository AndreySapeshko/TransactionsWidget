import unittest
from io import StringIO
from unittest.mock import MagicMock, patch

import pytest
from _pytest.monkeypatch import MonkeyPatch

from src.main import (filtered_transactions_by_description, filtered_transactions_by_state, greetings_and_import_data,
                      main, masked_account_card, sorted_transactions_by_date, user_input_validation)
from src.reader import read_from_csv, read_from_xlcx
from src.utils import converter_from_json

expect_executed = [
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

expect_canceled = [
    {
        "id": 41428829,
        "state": "CANCELED",
        "date": "2019-07-03T18:35:29.512364",
        "amount": "8221.37",
        "currency_name": "USD",
        "currency_code": "USD",
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
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
        "state": "CANCELED",
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

coll_description = [
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
        "state": "CANCELED",
        "date": "2019-07-03T18:35:29.512364",
        "amount": "8221.37",
        "currency_name": "USD",
        "currency_code": "USD",
        "description": "Перевод с карты на счет",
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

expect_sort = [
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
    },
    {
        "id": 41428829,
        "state": "CANCELED",
        "date": "2019-07-03T18:35:29.512364",
        "amount": "8221.37",
        "currency_name": "USD",
        "currency_code": "USD",
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    },
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
    }
]

expect_account = [
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

expect_card = [
    {
        "id": 41428829,
        "state": "CANCELED",
        "date": "2019-07-03T18:35:29.512364",
        "amount": "8221.37",
        "currency_name": "USD",
        "currency_code": "USD",
        "description": "Перевод с карты на счет",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }
]


@pytest.mark.parametrize('inputs,expected,expected_output', [
    (['3', 'exit'], ['1', '2', '3'], '3'),
    (['invalid', '2', 'exit'], ['1', '2'], '2'),
    (['a', 'b', 'exit'], ['1'], 'exit')
])
def test_user_input_validation(inputs: list, expected: list, expected_output: str, monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    assert user_input_validation(expected, 'Введите: ') == expected_output


@pytest.mark.parametrize('inputs,expected,expect', [
    (['0', '1'], ['1', '2', '3'], converter_from_json(
        'C:/Users/user/PyCharmStudyProject/TransactionsWidget/data/operations.json'
    )),
    (['5', '2'], ['1', '2', '3'], read_from_csv(
        'C:/Users/user/PyCharmStudyProject/TransactionsWidget/data/transactions.csv'
    )),
    (['4', '8', '3'], ['1', '2', '3'], read_from_xlcx(
        'C:/Users/user/PyCharmStudyProject/TransactionsWidget/data/transactions_excel.xlsx'
    )),
    (['9', 'exit'], ['1', '2', '3'], [])
])
def test_greetings_and_import_data(inputs: list, expected: list, expect: list, monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    assert greetings_and_import_data('Input: ') == expect


@pytest.mark.parametrize('inputs, expected, expect', [
    (['del', 'EXECUTED'], ['EXECUTED', 'CANCELED', ''], expect_executed),
    (['CANCELED'], ['EXECUTED', 'CANCELED', ''], expect_canceled),
    (['123', ''], ['EXECUTED', 'CANCELED', ''], coll)
])
def test_filtered_transactions_by_state(inputs: list, expected: list, expect: list, monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    assert filtered_transactions_by_state(coll, 'Input: ') == expect


class TestSortedTransactionsByDate(unittest.TestCase):
    @patch('src.main.user_input_validation')
    def test_sorted_transactions_by_date(self, mock_input: MagicMock) -> None:
        mock_input.side_effect = ['да', 'по убыванию']
        result = sorted_transactions_by_date(coll, 'Input: ')
        self.assertEqual(result, expect_sort)

    @patch('src.main.user_input_validation', side_effect=['да', 'да'])
    @patch('builtins.input', side_effect=['Перевод с карты на счет', 'Перевод организации'])
    def test_filtered_transactions_by_description(self, mock_input: MagicMock, mock_user_input: MagicMock) -> None:
        result_card = filtered_transactions_by_description(coll_description, 'Input: ')
        result_account = filtered_transactions_by_description(coll_description, 'Input: ')
        self.assertEqual(result_card, expect_card)
        self.assertEqual(result_account, expect_account)


@pytest.mark.parametrize('input_number, expected', [
    ('MasterCard 8826230888662405', 'MasterCard 8826 23** **** 2405'),
    ('Счет 96119739109420349721', 'Счет **9721')
])
def test_masked_account_card(input_number: str, expected: str) -> None:
    assert masked_account_card(input_number) == expected


class TestMain(unittest.TestCase):
    @patch('src.main.greetings_and_import_data')
    @patch('src.main.filtered_transactions_by_state')
    @patch('src.main.sorted_transactions_by_date')
    @patch('src.main.filtered_transactions_by_description')
    @patch('src.main.user_input_validation')
    def test_main(self, mock_user_input: MagicMock, mock_filtered_description: MagicMock,
                  mock_sorted_date: MagicMock, mock_filtered_state: MagicMock,
                  mock_import_data: MagicMock) -> None:
        mock_import_data.return_value = coll
        mock_filtered_state.return_value = expect_executed
        mock_sorted_date.return_value = expect_executed
        mock_filtered_description.return_value = expect_account
        mock_user_input.return_value = 'нет'
        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            main()
            output = fake_out.getvalue()
        expected_output = (
            '\n'
            'Выводить только рублевые транзакции? Да/Нет\n'
            '\n'
            '\n'
            'Распечатываю итоговый список транзакций...\n'
            '\n'
            'Всего банковских операций в выборке: 2\n'
            '\n'
            '26.08.2019 Перевод организации\n'
            'Maestro 1596 83** **** 5199 -> Счет **9589\n'
            '31957.58 руб.\n'
            '\n'
            '30.06.2018 Перевод организации\n'
            'Счет **6952 -> Счет **6702\n'
            '9824.07 USD\n'
        )
        self.assertEqual(output, expected_output)
