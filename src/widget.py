def mask_account_card(type_card_number: str) -> str:
    ''' Изменяем входящую строку, меняем номер на номер под маской '''

    if type_card_number[:4].lower() == 'счет':
        from masks import get_mask_account
        return type_card_number[:5] + get_mask_account(type_card_number[-20:])
    else:
        from masks import get_mask_card_number
        return type_card_number[:-16] + get_mask_card_number(type_card_number[-16:])
