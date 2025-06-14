# Проект TransactionsWidget

## Описание:

TransactionsWidget это виджет для системы банк-клиент, который отображает несколько последних транзакций.

## Установка:
1. Клонируйте репозиторий:
```commandline
git clone https://github.com/AndreySapeshko/TransactionsWidget.git
```
2. Установите зависимости:
```commandline
pip install -r requirements.txt
```
## Тестирование:
Результаты тестирования в папке htmlcov
1. модуль test_decorators
2. модуль test_external_api
3. модуль test_utils

## Использование:

## Документация:
### Модуль generator:
1. функция filter_by_currency
2. функция transaction_descriptions
3. функция card_number_generator

### Модуль decorators:
1. декоратор log записывает в файл или консоль 
парамеетры и результат работы функции
Примеры использования в модуле test_generators.py

### Модуль external_api
1. функция get_transaction_amount_in_rubles

### Модуль utils
1. функция converter_from_json

### Логирование
В деректории logs находятся логи по модулям
## Лицензия:
