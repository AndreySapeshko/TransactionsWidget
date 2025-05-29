import pytest


from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture(params=[
    ('64686473678894779589', '**9589'),
    ('35383033474447895560', '**5560')
])
def account_pair(request):
    return request.param


def test_account_masking(account_pair):
    account, masked = account_pair
    assert get_mask_account(account) == masked


coll_card = [
    ('1596837868705199', '1596 83** **** 5199'),
    ('7158300734726758', '7158 30** **** 6758'),
    ('6831982476737658', '6831 98** **** 7658')
]


@pytest.mark.parametrize('card_number, expected', coll_card)
def test_get_mask_card_number(card_number: str, expected: str):
    assert get_mask_card_number(card_number) == expected
