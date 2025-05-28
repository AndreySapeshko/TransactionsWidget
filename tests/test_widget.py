import pytest


from src.widget import mask_account_card, get_date


coll = [('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
        ('Счет 64686473678894779589', 'Счет **9589'),
        ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
        ('Счет 35383033474447895560', 'Счет **5560'),
        ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658')]

@pytest.mark.parametrize('type_card_number, expected', coll)
def test_mask_account_card(type_card_number: str, expected: str):
    assert mask_account_card(type_card_number) == expected

@pytest.mark.parametrize('date_long, expected', [('2024-03-11T02:26:18.671407', '11.03.2024')])
def test_get_date(date_long: str, expected: str):
    assert get_date(date_long) == expected