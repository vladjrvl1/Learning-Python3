l = ['Hello', 'Hi', 'Banana', 'Tree']


def has_e(string):
    return 'e' in string


# n1 = list(filter(has_e, l))
n2 = list(filter(lambda string: 'a' in string, l))
n3 = [string for string in l if has_e(string)]
print(n2)
