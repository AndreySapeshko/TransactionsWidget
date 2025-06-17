import re
from datetime import datetime

from src.utils import converter_from_json
from src.reader import read_from_csv, read_from_xlcx
from src.processing import filter_by_state, sort_by_date, process_bank_search
from src.masks import get_mask_account, get_mask_card_number
from src.external_api import get_transaction_amount_in_rubles


def user_input_validation(expected: list[str], offer: str, max_attempts: int = 0) -> str:
    """ принимает список с ожидаемым результатом ввода и строку с предложением что ввести,
    проверяем ввод пользователя. max_attempts ограничивает количество попыток"""

    user_input = ' '
    counter_input = 0
    expected.append('exit')
    expected = [x.lower() for x in expected]
    while user_input.lower() not in expected:
        if counter_input > 0:
            print(f'Вы ввели: {user_input} это недопустимый ввод.')
        user_input = input(offer)
        counter_input += 1
        if counter_input == max_attempts:
            user_input = 'exit'
            print('Количество допустимых попыток исчерпоно.\n' +
                  'Если хотите продолжить запустите программу заново')
            break
    return user_input


def greetings_and_import_data(greetings: str) -> list[dict]:
    """ Приветствуем и импортируем данные по выбранному формату """

    transactions: list[dict] = []
    print(greetings)
    format = user_input_validation(['1', '2', '3'], 'Введите номер пункта: ')
    if format == '1':
        transactions = converter_from_json('data/operations.json')
        print('\nДля обработки выбран JSON-файл.')
    elif format == '2':
        transactions = read_from_csv('data/transactions.csv')
        print('\nДля обработки выбран CSV-файл.')
    elif format == '3':
        transactions = read_from_xlcx('data/transactions_excel.xlsx')
        print('\nДля обработки выбран XLSX-файл.')
    elif format.lower() == 'exit':
        print('Работа программы завершена.')
        return
    return transactions


def filtered_transactions_by_state(transactions: list[dict], suggest_choose_state: str) -> list[dict]:
    """ Предлагаем отфилтровать по статусу и возвращаем транзакции выбранного статуса """

    print(suggest_choose_state)
    state = user_input_validation(['EXECUTED', 'CANCELED', 'PENDING', ''],
                                  'Введите один из трех статусов или пустую строку: ').upper()
    if state.lower() == 'exit':
        return filter_by_state(transactions)
    elif state == '':
        return transactions
    else:
        return filter_by_state(transactions, state=state)


def sorted_transactions_by_date(transactions: list[dict], suggest_sort_date: str) -> list[dict]:
    """ Предлагаем сортировку по дате и сортируем по выбору """

    print(suggest_sort_date)
    sort_date = user_input_validation(['да', 'нет'], 'Введите да или нет: ')
    if sort_date.lower() == 'да':
        suggest_select_sort_mode = '\nОтсортировать по возрастанию или по убыванию?\n'
        print(suggest_select_sort_mode)
        sort_mode = user_input_validation(['по возрастанию', 'по убыванию'],
                                          'Введите "по возрастанию" или "по убыванию": ')
        reverse = True
        if sort_mode.lower() == 'по убыванию':
            reverse = False
        transactions = sort_by_date(transactions, reverse=reverse)
    return transactions


def filtered_transactions_by_description(transactions: list[dict], suggest_choose_description: str) -> list[dict]:
    print(suggest_choose_description)
    choose_description = user_input_validation(['да', 'нет'], 'Введите да или нет: ')
    if choose_description.lower() == 'да':
        text_description = input('Введите слово или фразу из описания: ')
        transactions = process_bank_search(transactions, text_description)
    return transactions


def masked_account_card(account_card: str) -> str:
    """ маскеруем номера счета или карты """

    pattern = re.compile(r'\d+')
    if account_card is not None:
        if re.search('счет', account_card.lower()):
            account_card = pattern.sub(get_mask_account(pattern.search(account_card).group()), account_card)
        else:
            account_card = pattern.sub(get_mask_card_number(pattern.search(account_card).group()), account_card)
    else:
        account_card = ''
    return account_card


def main():
    """ программа загружает данные из файла и выводит в сортированном и отфильтрованном виде
        формат файла и параметры фильтрации и сортировки задает пользователь """

    # Приветствие. Получаем данные по выбранному формату.
    greetings = ('Программа: Привет! Добро пожаловать в программу работы\n' +
                 ' с банковскими транзакциями.\n' +
                 'Выберите необходимый пункт меню:\n' +
                 '1. Получить информацию о транзакциях из JSON-файла\n' +
                 '2. Получить информацию о транзакциях из CSV-файла\n' +
                 '3. Получить информацию о транзакциях из XLSX-файла\n ' +
                 'Для выхода из программы введите "exit".\n')
    transactions = greetings_and_import_data(greetings)

    # Фильтруем список по выбранному статусу.
    suggest_choose_state = ('\nПрограмма: Введите статус, по которому необходимо выполнить фильтрацию.\n' +
                            'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n' +
                            'что бы выбрать все введите пустую строку\n')
    transactions = filtered_transactions_by_state(transactions, suggest_choose_state)

    # Сортировка по дате по выбору
    suggest_sort_date = '\nОтсортировать операции по дате? Да/Нет\n'
    transactions = sorted_transactions_by_date(transactions, suggest_sort_date)

    # Фильтруем список по выбранному описанию
    suggest_choose_description = '\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n'
    transactions = filtered_transactions_by_description(transactions, suggest_choose_description)

    # Определяем выводим сумму в рублях или не только
    suggest_choose_currency = '\nВыводить только рублевые транзакции? Да/Нет\n'
    print(suggest_choose_currency)
    choose_currency = user_input_validation(['да', 'нет'], 'Введите да или нет: ')

    # Вывод данных
    print('\nРаспечатываю итоговый список транзакций...\n')

    if len(transactions) == 0:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
        return

    print(f'Всего банковских операций в выборке: {len(transactions)}')
    for transaction in transactions:
        # Переменные с данными необходимые для вывода
        trans_date = datetime.fromisoformat(transaction.get('date')).strftime('%d.%m.%Y')
        description = transaction.get('description')
        account_from = masked_account_card(transaction.get('from'))
        account_to = masked_account_card(transaction.get('to'))
        arrow = ' -> '
        if account_to == '' or account_from == '':
            arrow = ''
        amount = transaction.get('amount')
        name_currency = transaction.get('currency_name')

        # Получаем сумму в рублях для прочих валют
        if choose_currency.lower() == 'да':
            amount = get_transaction_amount_in_rubles(transaction)
            name_currency = 'руб.'

        print(f'\n{trans_date} {description}\n{account_from}{arrow}{account_to}\n{amount} {name_currency}')


if __name__ == '__main__':
    main()
