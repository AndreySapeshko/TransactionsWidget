def user_input_validation(expected: list[str], offer: str, max_attempts: int = 0) -> str:
    """ принимает список с ожидаемым результатом ввода и строку с предложением что ввести,
    проверяем ввод пользователя. max_attempts ограничивает количество попыток"""

    user_input = ''
    counter_input = 0
    expected = [x.lower() for x in expected]
    while  user_input.lower() not in expected:
        if counter_input > 0:
            print(f'Вы ввели: {user_input} это недопустимый ввод.')
        user_input = input(offer)
        counter_input += 1
        if counter_input == max_attempts:
            break
    return user_input


def main():
    greetings = ('Программа: Привет! Добро пожаловать в программу работы\n' +
                 ' с банковскими транзакциями.\n' +
                 'Выберите необходимый пункт меню:\n' +
                 '1. Получить информацию о транзакциях из JSON-файла\n' +
                 '2. Получить информацию о транзакциях из CSV-файла\n' +
                 '3. Получить информацию о транзакциях из XLSX-файла\n')
    print(greetings)
    format = user_input_validation(['1', '2', '3'], 'Введите номер пункта: ')
    if format == '1':
        print('\nДля обработки выбран JSON-файл.')
    elif format == '2':
        print('\nДля обработки выбран CSV-файл.')
    elif format == '3':
        print('\nДля обработки выбран XLSX-файл.')
    suggest_choose_state = ('\nПрограмма: Введите статус, по которому необходимо выполнить фильтрацию.\n' +
             'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
    print(suggest_choose_state)
    state = user_input_validation(['EXECUTED', 'CANCELED', 'PENDING'], 'Введите один из трех статусов: ')
    print(state)


if __name__ == '__main__':
    main()