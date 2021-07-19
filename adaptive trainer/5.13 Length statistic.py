string = input().split()
d = {}
for word in string:
    key = len(word)
    d.setdefault(key, 0)
    d[key] += 1

for key, value in sorted(d.items()):
    print(f'{key}: {value}')
