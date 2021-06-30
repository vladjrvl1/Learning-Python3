d = {'север': 0, 'юг': 0, 'восток': 0, 'запад': 0}
n = int(input())
for i in range(n):
    direction, value = input().split()
    d[direction] += int(value)
print(d['восток'] - d['запад'], d['север'] - d['юг'])
