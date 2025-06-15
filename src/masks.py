import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('C:/Users/user/PyCharmStudyProject/TransactionsWidget/logs/masks.log',
                                   'w', encoding='utf-8')
file_formater = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """ получаем номер карты и возвращаем со скрытими цифрами """

    logger.info(f'функция get_mask_card_number запущена с аргументом: {card_number}')
    mask_card_number: str = card_number[:4] + ' ' + card_number[4:6] + "** **** " + card_number[-4:]
    logger.info('функция get_mask_card_number успешно завершена')

    return mask_card_number


def get_mask_account(account: str) -> str:
    """ получаем номер счета возвращаем последние 4 цифры и две * """

    logger.info(f'функция get_mask_account запущена с аргументом: {account}')
    mask_account: str = "".join("**" + account[-4:])
    logger.info('функция get_mask_account успешно завершена')

    return mask_account
