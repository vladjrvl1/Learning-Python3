# x = int(input())
# print(-15 < x <= 12 or 14 < x < 17 or 19 <= x)


# a, b, x = float(input()), float(input()), input()
#
# if x == '+':
#     print(a + b)
# elif x == '-':
#     print(a - b)
# elif x == '*':
#     print(a * b)
# elif x == 'pow':
#     print(a ** b)
# elif b == 0:
#     print('Деление на 0!')
# elif x == '/':
#     print(a / b)
# elif x == 'mod':
#     print(a % b)
# elif x == 'div':
#     print(a // b)


# form = input()
# if form == 'треугольник':
#     a, b, c = float(input()), float(input()), float(input())
#     p = (a + b + c) / 2
#     s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#     print(s)
# elif form == 'прямоугольник':
#     a, b = float(input()), float(input()),
#     s = a * b
#     print(s)
# elif form == 'круг':
#     r = float(input())
#     pi = 3.14
#     s = pi * r ** 2
#     print(s)

# Напишите программу, которая получает на вход три целых числа, по одному
# числу в строке, и выводит на консоль в три строки сначала максимальное,
# потом минимальное, после чего оставшееся число.
# На ввод могут подаваться и повторяющиеся числа.
# nums = [int(i) for i in input().split()]

# a, b, c = int(input()), int(input()), int(input())
# l = [i for i in (a, b, c)]
# l.sort(reverse=True)
# l[1], l[2] = l[2], l[1]
# print(*l, sep='\n')

# n = int(input())
#
# if n % 10 == 0 or n % 10 == 5 or n % 10 == 6 or n % 10 == 7 or n % 10 == 8 or n % 10 == 9 \
#         or 11 <= n <= 14 or 111 <= n <= 114 or 211 <= n <= 214 or 311 <= n <= 314 or 411 <= n <= 414 \
#         or 511 <= n <= 514 or 611 <= n <= 614 or 711 <= n <= 714 or 811 <= n <= 814 or 911 <= n <= 914:
#     print(n, 'программистов')
# elif n % 10 == 1:
#     print(n, 'программист')
# elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
#     print(n, 'программиста')

# n = input()
# s1, s2 = [int(i) for i in n[0:3]], [int(i) for i in n[3:6]]
# if sum(s1) == sum(s2):
#     print("Счастливый")
# else:
#     print("Обычный")

# a, b, c, d, e, f = input()
# n= int(a)+int (b)+int(c)
# m= int(d)+int (e)+int(f)
# if n==m:
#     print ('Счастливый')
# else:
#     print ('Обычный')

# num = int(input())
# sum = 0
# while num != 0:
#     sum += num
#     num = int(input())
# print(sum)

# i = 0
# a, b = int(input()), int(input())
# ch1, ch2 = 1, 1
# while ch1 != 0 or ch2 != 0:
#     i += 1
#     ch1, ch2 = i % a, i % b
# print(i)

#
# a, b = int(input()), int(input())
# d = a
# while d%b:
#     d += a
# print(d)

# Напишите программу, которая считывает целые числа с консоли по одному числу в строке.
#
# Для каждого введённого числа проверить:
# если число меньше 10, то пропускаем это число;
# если число больше 100, то прекращаем считывать числа;
# в остальных случаях вывести это число обратно на консоль в отдельной строке.

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# a, b, c, d = 7, 11, 5, 7
# print(end='\t')
# for i in range(c, d):
#     print(i,end='\t')
# print()
# for i in range(a, b):
#     print(i, end='\t')
#     for j in range(c, d):
#         print(j * i, end='\t')
#     print()
#

# for i in range(a, b+1):
#     if i == a:
#         print(end='\t')
#         for j in range(c, d+1):
#             print(j, end='\t')
#         print()
#     print(i, end='\t')
#     for k in range(c,d+1):
#         print(k*i, end='\t')
#     print()

# sum, c = 0, 0
# a, b = int(input()), int(input())
# if a % 3 != 0:
#     a += -a % 3
#     print(a)
# for i in range(a, b+1, +3):
#     sum += i
#     c += 1
# print(sum / c)
# a += -a%3
# b -= b%3
# print((a+b)/2)
# s = input()
# sum = ((s.upper().count('C') + s.upper().count('G')) / len(s)) * 100
# print(sum)

# s = 'gttecettg'
# if s == s[::-1]:
# print('Палиндром')


# s = 'aaaabbcaa'
# x = 0
# new_s = ''
# cnt = 1
#
# for i in range(len(s)):
#     x += 1
#     if x < len(s):
#         print(s[x], s[i])
#
#         if s[i] == s[x]:
#             cnt += 1
#             continue
#         new_s = f'{s[i]}{cnt}'
#         cnt = 1
# print(new_s)

# s = 'aaaabbcaa'
# x = -1
# new_s = ''
# cnt = 1
#
# for i in range(1, len(s)+1):
#     x += 1
#
#     if i < len(s):
#         if s[x] == s[i]:
#             cnt += 1
#             if i+1 == len(s):
#                 new_s += f'{s[x]}{cnt}'
#         else:
#             new_s += f'{s[x]}{cnt}'
#             cnt = 1
#
# print(new_s)

# x = -1
# s = input() + " "
# new_s = ''
# cnt = 1
# for i in range(1, len(s)):
#     x += 1
#     if s[x] == s[i]:
#         cnt += 1
#         continue
#     new_s += f'{s[x]}{cnt}'
#     cnt = 1
# print(new_s)
#


students = ['ivan', 'masha', 'sasha']
# teachers = ['oleg', 'alex']
teachers = 'oleg'
students += teachers
del students[0]


# a = [0] * 5
# a = [i for i in range(5)]
# a = [i * i for i in range(2, 4)]
#
#
# # 2.5, 9 iz 13
# # a = [int(i) for i in input().split()]
# if len(a)>1:
#     for i in range(len(a)):
#         print(a[i-1] + a[i+1-len(a)])
# else:
#     print(a[0])


a = [4, 8, 0, 3, 4, 2, 0, 3]
a.sort()
l = []
for i in range(len(a)):
    if a[i] == a[i+1-len(a)] and a[i] not in l:
        l.append(a[i])
# [l.append(x) for x in a if x not in l and a.count(x) > 1]
print(*l)

f = open('data.txt')
print(type(f))