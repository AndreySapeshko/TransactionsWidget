def get_mask_card_number(card_number: str) -> str:
    """получаем номер карты и возвращаем со скрытими цифрами"""

    mask_card_number: str = "".join(list(card_number[:7] + "** **** " + card_number[-4:]))

    return mask_card_number


def get_mask_account(account: str) -> str:
    """получаем номер счета возвращаем последние 4 цифры и две *"""

    mask_account: str = "".join("**" + account[-4:])

    return mask_account
