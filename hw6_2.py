# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите
# код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг
# друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара
# бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от
# 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если
# бьют - ложь.
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел
# для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные
# варианты и выведите 4 успешных расстановки.

from random import randint as ri

def _qween_moves(a: list):
    row, column = a
    moves = []
    for i in range(1,9):
        if i != column:
            moves.append([row, i])
            if i != row:
                moves.append([i, column])
        elif i != row:
            moves.append([i, column])
    row_1 = row - 1
    column_1 = column + 1
    while column_1 <= 8 and row_1 >= 1:
        moves.append([row_1, column_1])
        row_1 -= 1
        column_1 += 1
    row_2 = row + 1
    column_2 = column + 1
    while column_2 <= 8 and row_2 <= 8:
        moves.append([row_2, column_2])
        row_2 += 1
        column_2 += 1
    row_3 = row + 1
    column_3 = column - 1
    while column_3 >= 1 and row_3 <= 8:
        moves.append([row_3, column_3])
        row_3 += 1
        column_3 -= 1
    row_4 = row - 1
    column_4 = column - 1
    while column_4 >= 1 and row_4 >= 1:
        moves.append([row_4, column_4])
        row_4 -= 1
        column_4 -= 1
    return moves

def qween_lst(num: int):
    lst = []
    while len(lst) < num:
        a = [ri(1,8), ri(1,8)]
        if a not in lst:
            lst.append(a)
    return lst


def qween_check(lst:list):
    for i in range(len(lst)):
        for y in range(i+1, len(lst)):
            # print(_qween_moves(lst[i]))
            # print(lst[y])
            if lst[y] in _qween_moves(lst[i]):
                # print(lst[y])
                return False
    return True

# def qween_true(a:int):
#     lst_true = []
#     while len(lst_true) <= a:
#         x = qween_lst(8)
#         if qween_check(x) is True:
#             lst_true.append(x)
#     return '\n'.join(lst_true)

#a = [[1,1], [2,8], [3,2], [4,5], [5,7], [6,3], [8,6]]
a = 8
qw = qween_lst(a)
print(qween_lst(a), qween_check(qw), sep='\n')