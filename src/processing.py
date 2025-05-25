def filter_by_state(list_of_dict: list, state: str) -> list:
    ''' выбираем из списка словорей по значению ключа "state" '''

    dict_by_state = []
    for element in list_of_dict:
        if element.get('state') == state:
            dict_by_state.append(element)

    return dict_by_state
