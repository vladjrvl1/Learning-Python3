
with open(r'C:\Users\Vlad_\Desktop\Chrome Downloads\dataset_3363_3 (1).txt') as f:
    txt = f.read()


def count_amount_of_words(txt):
    s = tuple(txt.lower().strip().split())
    d = {}
    for i in set(s):
        d.update({i: s.count(i)})
    max_d = max(d.values())
    equals = set()
    for key, value in d.items():
        if max_d == value:
            equals.add(key)
    return min(equals), max_d

print(*count_amount_of_words(txt), count_amount_of_words(txt))


