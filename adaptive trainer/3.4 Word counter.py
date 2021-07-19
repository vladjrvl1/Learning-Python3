"""
Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.

Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.

Программа должна выводить для каждого уникального слова число его повторений (без учёта регистра).

Формат ввода:
Одна строка, содержащая последовательности символов через пробел

Формат вывода:
Набор строк, каждая из которых содержит слово и, через пробел, число -− количество раз, которое слово использовалось во входной строке. Регистр слов не важен, слова в выводе не должны повторяться, порядок слов произвольный.

"""
from collections import Counter

text = input()
c = Counter(map(lambda x: x.strip(',.;"\'«»'), text.lower().split()))
for key, value in sorted(c.items()):
    print(key, value)

print('\n------\n')

words_list = list(map(lambda x: x.strip(',.;"\'«»'), text.lower().split()))
dict_of_counted_words = {i: words_list.count(i) for i in set(words_list)}
for key, value in sorted(dict_of_counted_words.items()):
    print(key, value)




print(id(c), id(dict_of_counted_words))
print(c == dict_of_counted_words)