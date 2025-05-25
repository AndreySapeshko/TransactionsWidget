def filter_by_state(list_of_dict: list, state: str = 'EXECUTED') -> list:
    ''' выбираем из списка словорей по значению ключа "state" '''

    dict_by_state = []
    for element in list_of_dict:
        if element.get('state') == state:
            dict_by_state.append(element)

    return dict_by_state


def sort_by_date(list_of_dict: list, reverse: bool = True) -> list:
    ''' сортеруем список по дате по убыванию,
    если revers=False, то по возрастанию'''

    return sorted(list_of_dict, key=lambda x: x['date'], reverse=reverse)
