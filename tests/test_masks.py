import pytest


from src.masks import get_mask_account, get_mask_card_number


coll_account = [('64686473678894779589', '**9589'),
               ('35383033474447895560', '**5560')]

coll_card = [('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
            ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
            ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658')]

@pytest.mark.parametrize('account, expected', coll_account)
def test_get_mask_account(account: str, expected: str):
    assert get_mask_account(account) == expected