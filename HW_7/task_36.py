'''Напишите функцию print_operation_table
(operation, num_rows=6, num_columns=6),которая принимает
в качестве аргумента функцию, вычисляющую элемент по номеру
строки и столбца.
Аргументы num_rows и num_columns указывают число
строк и столбцов таблицы,
которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте,
почему не с нуля). Примечание: бинарной операцией называется
любая операция, у которой
ровно два аргумента, как, например, у операции умножения.'''


x = int(input("x: "))
y = int(input("y: "))


def operation(x_row, y_column):
    '''Функция вычисляет значение элемента'''
    return x_row*y_column


def print_operation_table(operation):
    '''Функция вычисляет элемент по номеру строки и столбца'''
    for i in range (1, x + 1):
        for j in range (1, y + 1):
            print(operation(i, j), end="  ")
        print(" ")


print_operation_table(lambda x, y: x * y)
