""" Сортировка пузрьком"""
mas = [5, 7, 4, 3, 8, 2]
n = len(mas)
count = 0

for run in range(n-1):
    for i in range(n - 1 - run):
        if mas[i] > mas[i + 1]:
            count += 1
            mas[i], mas[i + 1] = mas[i + 1], mas[i]