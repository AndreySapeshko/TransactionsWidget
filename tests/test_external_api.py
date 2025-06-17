from unittest.mock import patch

import pytest

from src.external_api import get_transaction_amount_in_rubles

coll = [
    (
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
        31957.58
    ),
    (
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
        649488.123122
    )
]

response = {
    'success': True,
    'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37},
    'info': {'timestamp': 1749526826, 'rate': 78.999987},
    'date': '2025-06-10', 'result': 649488.123122
}


@pytest.mark.parametrize('transaction, expected', coll)
def test_get_transaction_amount_in_rubles(transaction: dict, expected: float) -> None:
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = response
        assert get_transaction_amount_in_rubles(transaction) == expected
