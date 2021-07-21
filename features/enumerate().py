a = [10, 20, 30, 40, 50, 60]
s = 'hello'
t = ('apple', 'banana', 'mango')
d = {'a': 1, 'b': 2, 'c': 3}

for i in enumerate(range(10, 20)):
    print(i)
print('---------------')
for index, value in enumerate(t, 10):
    print(index, value)
