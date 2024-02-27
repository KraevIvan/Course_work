from utils import get_operations_list, del_corrupted_operations, get_sorted_operation_list, get_last_operations, get_operation_for_read


def test_get_operations_list():
    assert get_operations_list("tests/operation") == []
