from src.utils import get_operations_list, del_corrupted_operations, get_sorted_operation_list, get_last_operations, get_operation_for_read


def main():
    operation_list = get_operations_list("../data/operation.json")
    operation_list = del_corrupted_operations(operation_list)
    sorted_operation_list = get_sorted_operation_list(operation_list)
    last_n_operations = get_last_operations(sorted_operation_list, 5)
    for operation in last_n_operations:
        print(get_operation_for_read(operation))
    return 0


if __name__ == "__main__":
    main()
