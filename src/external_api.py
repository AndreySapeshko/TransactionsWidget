import os

import requests
from dotenv import load_dotenv


def get_transaction_amount_in_rubles(transaction: dict) -> float:
    """ из транзакции возвращает сумму в рублях, если сумма на в рублях, конвертирует через apilayer.com """

    currency_code = transaction['currency_code']
    if currency_code == 'RUB':
        return float(transaction['amount'])
    else:
        load_dotenv()
        headers = {
            'apikey': os.getenv('API_KEY_APILAYER')
        }
        url = "https://api.apilayer.com/exchangerates_data/convert"
        payload = {
            'amount': transaction['amount'],
            'from': currency_code,
            'to': 'RUB'
        }
        response = requests.get(url, headers=headers, params=payload)
        if response.status_code != 200:
            return print(f'Запрос не прошел. Возможная причина: {response.status_code}')
        return float(response.json()['result'])
