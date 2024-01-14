
from function import all_operations, five_operations, sort_operations, account_editing, date_2


def main_2():
    '''вывод операция в нужном виде'''

    operations_new = all_operations()

    five_operations_new = sort_operations(five_operations(operations_new))
    print(five_operations_new )

    for operation in five_operations_new:
        date_2(operation)
        account_editing(operation)
        print(operation["operationAmount"]["amount"], "руб.")
        print()


main_2()
