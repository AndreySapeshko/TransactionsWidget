def mask_account_card(type_card_number: str) -> str:
    ''' Изменяем входящую строку, меняем номер на номер под маской '''

    if type_card_number[:4].lower() == 'счет':
        from masks import get_mask_account
        account_mask = type_card_number[:5] + get_mask_account(type_card_number[-20:])
        return account_mask
    else:
        from masks import get_mask_card_number
        card_mask = type_card_number[:-16] + get_mask_card_number(type_card_number[-16:])
        return card_mask


def get_date(date_long: str) -> str:
    ''' возвращает строку с датой в формате "ДД.ММ.ГГГГ" '''

    return date_long[8:10] + '.' + date_long[5:7] + '.' + date_long[:4]
