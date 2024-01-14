import pytest

from main import function


@pytest.fixture
def coll():  # имя фикстуры любое
    return [{1: 'yes', 'date': 'abc', 3: '5'}, {1: '111', 'date': 'no', 3: '5'}]


def test_sort_operations(coll):
    assert function.sort_operations(coll, 'date') == [{1: '111', 'date': 'no', 3: '5'},
                                                      {1: 'yes', 'date': 'abc', 3: '5'}]
    assert function.sort_operations(coll, 3) == [{1: 'yes', 'date': 'abc', 3: '5'}, {1: '111', 'date': 'no', 3: '5'}]


def test_five_operations(coll):
    assert function.five_operations(coll, 1, 'yes') == [{1: 'yes', 'date': 'abc', 3: '5'}]
    assert function.five_operations(coll, 1, 'no') == []
    assert function.five_operations(coll, 3, '5') == [{1: 'yes', 'date': 'abc', 3: '5'},
                                                      {1: '111', 'date': 'no', 3: '5'}]
    assert function.five_operations(coll, 3, '4') == []


def test_date_2():
    assert function.date_2({'date': '2019-08-26T10:50:58.294041', 'description': 'Перевод организации'}, 'date',
                           'description') == '26.08.2019   Перевод организации'


def test_account_editing():
    assert function.account_editing({'from':'Maestro 1596837868705199', 'to':'Счет 64686473678894779589'}) == 'Maestro 1596 37** **** 5199  ->  Счет ** 9477'
    assert function.account_editing({'to':'Счет 64686473678894779589'}) == '->  Счет ** 9477'
