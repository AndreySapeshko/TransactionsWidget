import os

import requests
from dotenv import load_dotenv


def get_transaction_amount_in_rubles(transaction: dict) -> float:
    """ из транзакции возвращает сумму в рублях, если сумма на в рублях, конвертирует через apilayer.com """

    currency_code = transaction['operationAmount']['currency']['code']
    if currency_code == 'RUB':
        return float(transaction['operationAmount']['amount'])
    else:
        load_dotenv()
        headers = {
            'apikey': os.getenv('API_KEY_APILAYER')
        }
        url = "https://api.apilayer.com/exchangerates_data/convert"
        payload = {
            'amount': transaction['operationAmount']['amount'],
            'from': currency_code,
            'to': 'RUB'
        }
        response = requests.get(url, headers=headers, params=payload)
        return float(response.json()['result'])
