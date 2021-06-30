'''
Сапер
i, j; i, j-1; i, j+1; i-1, j; i+1, j;
i + di, j + dj;
di, dj -1 ... +1;
'''
''' Сапёр
n, m, k = (int(i) for i in input().split())
a = [[0 for j in range(m)] for i in range(n)]
for i in range(k):
    row, col = (int(i) - 1 for i in input().split())
    a[row][col] = -1

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
                        a[i][j] += 1

for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end='')
        elif a[i][j] == 0:
            print('.', end='')
        else:
            print(a[i][j], end='')
    print()
'''
# 2.6

# 6
'''
a = 0
s = 0
while True:
    n = int(input())
    s += n ** 2
    a += n
    if a == 0:
        print(s)
        break
'''

# 7
'''n, cnt = int(input()), 0
for i in range(1, n+1):
    for j in range(i):
        cnt += 1
        if cnt <= n:
            print(i, end=' ')
'''

# 8
'''
lst, x = [int(i) for i in input().split()], int(input())
if x not in lst:
    print("Отсутствует")
for i in range(len(lst)):
    if x == lst[i]:
        print(i, end=' ')
'''

# 9

'''
lst = []
while True:
    a = input()
    if a != 'end':
        lst.append([int(i) for i in a.split()])
    else:
        break

for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i-1][j] + lst[i+1-len(lst)][j] + lst[i][j-1] + lst[i][j+1-len(lst[i])], end=' ')
    print()
'''

# 10
''' Выведите таблицу размером n * n, заполненную числами от 1 до n**2 по спирали, выходящей из левого края и закрученную 
 по часовой стрелке
1  2  3  4  5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
'''
'''
rows = 3
cols = 4
tab = [[0] * cols for _ in range(rows)]
index = 0

for col in range(cols):
    if col % 2 == 0:
        for row in range(rows):
            index += 1
            tab[row][col] = index
    else:
        for row in range(rows - 1, -1, -1):
            index += 1
            tab[row][col] = index

for i in tab:
    print('\t'.join(map(str, i)))

'''
def print_value():
    a = 10
    print(a)


x = float(5)


def find_x(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        return -x / 2
    return (x - 2) ** 2 + 1



''' 
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка, например:
'''
lst = [1, 2, 3, 4, 5, 6]


# def modify_list(l):
#     for i in range(len(l)-1, -1, -1):
#         if l[i] % 2 == 1:
#             del l[i]
#         else:
#             l[i] //= 2
def modify_list(l):
    l[:] = [i//2 for i in l if i % 2 == 0]


modify_list(lst)

a = {'apple', 'orange', 'banana', 'tomato', 'potato', '2', '2'}
''' set.add, set.remove, set.discard (удаление без ошибки), s.clear
'''
print(a)

