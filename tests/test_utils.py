from src.utils import get_operations_list, del_corrupted_operations, get_sorted_operation_list, get_last_operations, get_operation_for_read
from src.main import main
import pytest


@pytest.fixture
def operations_all():
    operations_list_all = get_operations_list("data/operation.json")
    return operations_list_all


@pytest.fixture
def operations_correct_not_sorted():
    return del_corrupted_operations(get_operations_list("data/operation.json"))


@pytest.fixture
def operation_correct_sorted():
    return get_sorted_operation_list(del_corrupted_operations(get_operations_list("data/operation.json")))


@pytest.fixture
def operation_last_correct_sorted():
    return get_last_operations(get_sorted_operation_list(del_corrupted_operations(get_operations_list("data/operation.json"))), 5)


def test_get_operations_list():
    assert get_operations_list("tests/operation") == []
    assert type(get_operations_list("data/operation.json")) == list
    assert get_operations_list('data/operation.json')[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }


def test_del_corrupted_operations(operations_all):
    assert len(del_corrupted_operations(operations_all)) == 100


def test_get_sorted_operation_list(operations_correct_not_sorted):
    assert get_sorted_operation_list(operations_correct_not_sorted)[0] == {
        'id': 863064926,
        'state': 'EXECUTED',
        'date': '2019-12-08T22:46:21.935582',
        'operationAmount':
            {'amount': '41096.24',
             'currency': {
                 'name': 'USD',
                 'code': 'USD'
                  }
             },
        'description': 'Открытие вклада',
        'to': 'Счет 90424923579946435907'
    }


def test_get_last_operations(operation_correct_sorted):
    assert len(get_last_operations(operation_correct_sorted, 5)) == 5


def test_get_operation_for_read(operation_last_correct_sorted):
    assert get_operation_for_read(operation_last_correct_sorted[0]) == """08.12.2019 Открытие вклада
-> Счет **5907 
41096.24 USD
"""
    assert get_operation_for_read(operation_last_correct_sorted[1]) == """07.12.2019 Перевод организации
Visa Classic 2842 87** **** 9012 -> Счет **3655 
48150.39 USD
"""


def test_main():
    assert main() == 0


