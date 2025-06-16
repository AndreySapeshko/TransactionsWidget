import json

from src.utils import converter_from_json
from src.reader import read_from_csv, read_from_xlcx
from src.processing import filter_by_state, sort_by_date


def user_input_validation(expected: list[str], offer: str, max_attempts: int = 0) -> str:
    """ принимает список с ожидаемым результатом ввода и строку с предложением что ввести,
    проверяем ввод пользователя. max_attempts ограничивает количество попыток"""

    user_input = ''
    counter_input = 0
    expected.append('exit')
    expected = [x.lower() for x in expected]
    while  user_input.lower() not in expected:
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


def main():
    transactions: list[dict] = []

    greetings = ('Программа: Привет! Добро пожаловать в программу работы\n' +
                 ' с банковскими транзакциями.\n' +
                 'Выберите необходимый пункт меню:\n' +
                 '1. Получить информацию о транзакциях из JSON-файла\n' +
                 '2. Получить информацию о транзакциях из CSV-файла\n' +
                 '3. Получить информацию о транзакциях из XLSX-файла\n ' +
                 'Для выхода из программы введите "exit".\n')
    print(greetings)
    format = user_input_validation(['1', '2', '3'], 'Введите номер пункта: ')
    if format == '1':
        transactions = converter_from_json('data/operations.json')
        print('\nДля обработки выбран JSON-файл.')
    elif format == '2':
        transactions = read_from_csv('data/transactions.csv')
        print('\nДля обработки выбран CSV-файл.')
    elif format == '3':
        transactions = read_from_xlcx('C:/Users/user/PyCharmStudyProject/TransactionsWidget/data/transactions_excel.xlsx')
        print('\nДля обработки выбран XLSX-файл.')
    elif format.lower() == 'exit':
        print('Работа программы завершена.')
        return

    suggest_choose_state = ('\nПрограмма: Введите статус, по которому необходимо выполнить фильтрацию.\n' +
             'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n')
    print(suggest_choose_state)
    state = user_input_validation(['EXECUTED', 'CANCELED', 'PENDING'], 'Введите один из трех статусов: ').upper()
    transactions = filter_by_state(transactions, state=state)

    suggest_sort_date = '\nОтсортировать операции по дате? Да/Нет\n'
    print(suggest_sort_date)
    sort_date = user_input_validation(['да', 'нет'], 'Введите да или нет: ')
    if sort_date.lower() == 'да':
        suggest_select_sort_mode = '\nОтсортировать по возрастанию или по убыванию?\n'
        print(suggest_select_sort_mode)
        sort_mode = user_input_validation(['по возрастанию', 'по убыванию'], 'Введите "по возрастанию" или "по убыванию": ')
        reverse = True
        if sort_mode.lower() == 'по убыванию':
            reverse = False
        transactions = sort_by_date(transactions, reverse=reverse)
    print(json.dumps(transactions, indent=4))


if __name__ == '__main__':
    main()