"""
Поле для игры сапёр представляет собой сетку размером n \times mn×m. В ячейке сетки может находиться
или отсутствовать мина.

Напишите программу, которая выводит "решённое" поле, т.е. для каждой ячейки, не являющейся миной, указывается число мин,
 находящихся в соседних ячейках (учитывая диагональные направления)

Формат ввода:
На первой строке указываются два натуральных числа 1 \le n,m \le 1001≤n,m≤100, после чего в nn строках
содержится описание поля в виде последовательности точек '.' и звёздочек '*', где точка означает пустую ячейку,
а звёздочка − ячейку с миной.

Формат вывода:
nn строк поля, в каждой ячейке которого будет либо число от 0 до 8, либо мина (обозначенная символом "*"),
при этом число означает количество мин в соседних ячейках поля.
"""

n, m = (int(i) for i in input().split())
matrix = [[0 if j == '.' else '*' for j in input()[:m]] for i in range(n)]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            for k in range(-1, 2):
                for z in range(-1, 2):
                    if 0 <= i + k < n and 0 <= j + z < m:
                        if matrix[i + k][j + z] == '*':
                            matrix[i][j] += 1

for i in matrix:
    print(*i, sep='')