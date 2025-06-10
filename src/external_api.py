import os
from dotenv import load_dotenv
import requests


def get_transaction_amount_in_rubles(transaction: dict) -> float:
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
        return response.json()['result']


transactions = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }

print(get_transaction_amount_in_rubles(transactions))
