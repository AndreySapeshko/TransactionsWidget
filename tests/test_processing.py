import pytest

from src.processing import filter_by_state, sort_by_date, process_bank_search, process_bank_operations

transactions = [{'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0,
                 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
                 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
                {'id': 3598919, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740.0,
                 'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
                 'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
                {'id': 593027, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': 30368.0,
                 'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097',
                 'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'},
                {'id': 366176, 'state': 'EXECUTED', 'date': '2020-08-02T09:35:18Z', 'amount': 29482.0,
                 'currency_name': 'Rupiah', 'currency_code': 'IDR', 'from': 'Discover 0325955596714937',
                 'to': 'Visa 3820488829287420', 'description': 'Перевод с карты на карту'},
                {'id': 5380041, 'state': 'CANCELED', 'date': '2021-02-01T11:54:58Z', 'amount': 23789.0,
                 'currency_name': 'Peso', 'currency_code': 'UYU', 'from': None, 'to': 'Счет 23294994494356835683',
                 'description': 'Открытие вклада'}
                ]

expected_one = [{'id': 3598919, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740.0,
                 'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
                 'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
                {'id': 593027, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': 30368.0,
                 'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097',
                 'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'},
                {'id': 366176, 'state': 'EXECUTED', 'date': '2020-08-02T09:35:18Z', 'amount': 29482.0,
                 'currency_name': 'Rupiah', 'currency_code': 'IDR', 'from': 'Discover 0325955596714937',
                 'to': 'Visa 3820488829287420', 'description': 'Перевод с карты на карту'}
                ]

expected_two = [{'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0,
                 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
                 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'}
                ]

@pytest.fixture(params=[
    (transactions, 'Перевод с карты на карту', expected_one),
    (transactions, 'Перевод организации', expected_two),
    (transactions, 'xxx', [])
])
def key_result(request):
    return request.param

coll = [([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
         'EXECUTED',
         [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
        ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
         'CANCELED',
         [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
         )]

coll_sort = [([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
               {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
               {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
               {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
              True,
              [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
               {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
               {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
               {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
              )]


@pytest.mark.parametrize('list_of_dict, state, expected', coll)
def test_filter_by_state(list_of_dict: list, state: str, expected: list):
    assert filter_by_state(list_of_dict, state) == expected


@pytest.mark.parametrize('list_of_dict, reverse, expected', coll_sort)
def test_sort_by_date(list_of_dict: list, reverse: bool, expected):
    assert sort_by_date(list_of_dict, reverse) == expected


def test_process_bank_search(key_result):
    transactions, search, expected = key_result
    assert process_bank_search(transactions, search) == expected


def test_process_bank_operations():
    assert process_bank_operations(transactions,['EXECUTED', 'CANCELED']) == {'EXECUTED': 3, 'CANCELED': 2}
    assert process_bank_operations(transactions, ['EXECUTED']) == {'EXECUTED': 3}
