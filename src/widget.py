from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_card_number: str) -> str:
    ''' Изменяем входящую строку, меняем номер на номер под маской '''

    acc_type, number = type_card_number.rsplit(' ', maxsplit=1)
    if acc_type.lower() == 'счет':
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f'{acc_type} {masked_number}'


def get_date(date_long: str) -> str:
    ''' возвращает строку с датой в формате "ДД.ММ.ГГГГ" '''

    return date_long[8:10] + '.' + date_long[5:7] + '.' + date_long[:4]
