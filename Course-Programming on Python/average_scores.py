import sys, subprocess, math
# with open(input(), 'r', encoding='utf-8') as f:
#     txt_lst = [list(map(int, i.strip().split(';')[1:])) for i in f]
#     txt_lst.append([0, 0, 0])
#     for i in range(len(txt_lst)-1):
#         avg = 0
#         for j in range(3):
#             avg += txt_lst[i][j]
#             txt_lst[-1][j] += txt_lst[i][j]
#         print(avg / 3)
#     for i in txt_lst[-1]:
#         print(i/3, end=' ')

with open('data.txt', 'r') as f:
    txt_lst = [list(map(int, i.strip().split(';')[1:])) for i in f]
    txt_lst.append([0, 0, 0])
with open('1.txt', 'w') as f:
    for i in range(len(txt_lst) - 1):
        avg = 0
        for j in range(3):
            avg += txt_lst[i][j]
            txt_lst[-1][j] += txt_lst[i][j]
        f.write(f'{str(round(avg / 3, 9))}\n')
    for i in txt_lst[-1]:
        f.write(f'{str(round(i / (len(txt_lst)-1), 9))} ')

