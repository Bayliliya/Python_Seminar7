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


def operation(x_row, y_column):
    '''Функция вычисляет значение элемента'''
    massiv_item = []
    total_massiv = []
    for i in range(1, x_row + 1):
        for j in range(1, y_column + 1):
            massiv_item.append(i * j)
        total_massiv.append(massiv_item)
        massiv_item = []
    return total_massiv


x = 8
y = 8


def print_operation_table(func):
    '''Функция вычисляет элемент по номеру строки и столбца'''
    func = operation(x, y)
    result_massiv = func
    for _, num in enumerate(result_massiv):
        print(*num)


x = int(input("X: "))
y = int(input("Y: "))

print_operation_table(lambda x, y: x * y)
