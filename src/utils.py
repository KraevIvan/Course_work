import json
import os
from operator import itemgetter


def get_operations_list(path):
    """Возвращает список всех операций полученных из файла"""

    if not os.path.exists(path):
        return []

    with open(path, "r", encoding='utf-8') as operation_list_json:
        operations_list = json.load(operation_list_json)
        return operations_list


def del_corrupted_operations(operations):
    """Удаляет из списка операций операции с поврежденными данными"""

    for operation in operations:
        if "id" not in operation or \
                "date" not in operation or \
                "operationAmount" not in operation or \
                "state" not in operation or \
                "to" not in operation:
            del operations[operations.index(operation)]
    operations_not_sort = operations
    return operations_not_sort


def get_sorted_operation_list(operations_not_sort):
    """Сортирует список операций по дате (сначала последние)"""

    operations_sort = sorted(operations_not_sort, key=itemgetter('date'), reverse=True)
    return operations_sort


def get_last_operations(operations, n=5):
    """Возвращает список последних n выполненных операций"""
    if n > len(operations):
        n = len(operations)
    last_operations = []
    i = 0
    while len(last_operations) < n:
        if operations[i]["state"] == "EXECUTED":
            last_operations.append(operations[i])
        i += 1
    return last_operations


def get_operation_for_read(operation):
    """Возвращает данные операции в читаемом виде"""

    date = operation["date"].split('T')[0]
    date = '.'.join(date.split('-')[::-1])

    if "from" in operation:
        if "Счет" in operation["from"]:
            from_ = operation["from"].split(" ")[0]
            from_ += " **" + operation["from"].split(" ")[-1][-4:] + " "
        else:
            from_ = " ".join(operation["from"].split(" ")[: -1])
            card_number = operation["from"].split(" ")[-1]
            from_ = f"{from_} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]} "
    else:
        from_ = ""

    if "Счет" in operation["to"]:
        to_ = operation["to"].split(" ")[0]
        to_ += " **" + operation["to"].split(" ")[-1][-4:] + " "
    else:
        to_ = " ".join(operation["to"].split(" ")[: -1])
        card_number = operation["to"].split(" ")[-1]
        to_ = f"{to_} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]} "

    return f"""{date} {operation["description"]}
{from_}-> {to_}
{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n"""
