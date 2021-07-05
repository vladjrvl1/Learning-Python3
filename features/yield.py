t = """Генератор - это итератор, элементы которого
можно перебирать только один раз.
Итератор - это обхект, который поддерживает функцию next()
для перехода к следующему элементу коллекции."""

if not t.endswith('\n'):
    t = t + '\n'


def gen(strs):
    s = ''
    for sym in strs:
        if sym != ' ' and sym != '\n':
            s += sym
        else:
            b = s
            s = ''
            yield b


f = gen(t)
for i in f:
    print(i)
