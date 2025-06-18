from unittest.mock import patch, MagicMock
import unittest
import pytest

from src.external_api import get_transaction_amount_in_rubles


class TestTransactionConversion(unittest.TestCase):
    @patch('src.external_api.requests.get')
    def test_get_transaction_amount_in_rubles(self, mock_get):
        # Подготовка тестовых данных
        test_transaction = {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "amount": "8221.37",
            "currency_name": "USD",
            "currency_code": "USD",
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }

        # Мок ответа API
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'success': True,
            'result': 649488.123122,
            'info': {'rate': 78.999987}
        }

        mock_get.return_value = mock_response

        # Вызов и проверка
        result = get_transaction_amount_in_rubles(test_transaction)
        expected = 649488.123122
        self.assertAlmostEqual(result, expected, places=2)
