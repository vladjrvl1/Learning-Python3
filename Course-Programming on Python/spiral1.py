size = 6
tab = [[0] * size for _ in range(size)]
tab[0] = [(col + 1) for col in range(size)]
index = size
y, x, r = 0, size - 1, size
while index < size * size:
    r -= 1
    for _ in range(r):
        y += 1
        index += 1
        tab[y][x] = index
    for _ in range(r):
        x -= 1
        index += 1
        tab[y][x] = index
    if index >= size * size:
        break
    r -= 1
    for _ in range(r):
        y -= 1
        index += 1
        tab[y][x] = index
    for _ in range(r):
        x += 1
        index += 1
        tab[y][x] = index

for i in tab:
    print('\t'.join(map(str, i)))
