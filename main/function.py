import io
import json, os.path
from datetime import datetime


def all_operations():
    """список всех операций из json"""
    operations_json = os.path.join('operations.json')
    with io.open(operations_json, 'r', encoding='utf-8') as file:
        operations_js = json.load(file)
        return operations_js


def five_operations(inform, key = 'state', n = 'EXECUTED'):
    ''' 5 операций из всего списка'''
    counter = 0
    list_operations = []
    for i in inform:
        if i[key] == n:
            counter += 1
            list_operations.append(i)
            if counter == 5:
                break
    return list_operations


def sort_operations(operations, n='date'):
    '''сортировка операий по дате'''
    operations_sort = sorted(operations, key=lambda x: x[n], reverse=True)
    return operations_sort

def date_2(date, i = "date", d = "description"):
    '''вывод даты в формате дд.мм.гггг'''
    date_new = datetime.strptime(date[i], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
    return print(date_new, ' ', date[d])


def account_editing(accounts):
    '''вывод счетов в нужном виде'''
    to_new = accounts["to"].split()
    to_new_3 = to_new[0] + ' ' + "** " + to_new[1][12:16]

    if 'from' not in accounts:
        return print("->", to_new_3)
    else:
        from_new = accounts.get("from", '').split()
        from_new_2 = from_new[1]
        from_new_3 = from_new[0] + ' ' + from_new_2[0:4] + ' ' + from_new_2[5:7] + "** **** " + from_new_2[12:16]
        return print(from_new_3, " -> ", to_new_3)