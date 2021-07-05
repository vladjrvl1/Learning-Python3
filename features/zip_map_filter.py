"""преобразовать hello world в хелло ворлд"""
d = {'h': 'х', 'e': 'е', 'l': 'л', 'o': 'о', 'w': 'в', 'r': 'р', 'd': 'д'}
s = 'hello world'
string = map(lambda x: d[x] if x in d else x, s)
for i in string:
    print(i, end='')
print()


class Solution:
    def __init__(self, text=''):
        self._text = """Куда ты скачешь гордый конь,
                        И где опустишь ты копыта?
                        О мощный властелин судьбы!"""

    @staticmethod
    def odd(x):
        return True if x % 2 else False

    def text_formatting(self) -> list[str]:
        """Необходимо выделить каждое второе слово из этого стихотворения и представить результат в виде упорядочного
            списка."""
        # text_split = text.split()
        # result = []
        # odd_indexes = filter(Solution2.odd, range(len(text_split)))
        # for i in odd_indexes:
        #     result.append(text_split[i])
        text_list = self._text.split()
        text_list = [text_list[i] for i in range(len(text_list)) if self.odd(i)]
        return text_list

    """Реализовать алгоритм для нахождения всех делителей натурального числа N. Число N вводите с клавиатуры. Для 
    начала можно реализовать простым перебором N возможных чисел(делителей). Затем, подумайте, как можно оптимизировать
    по скорости этот алгоритм"""

    @staticmethod
    def get_dividers(x: int) -> list:
        dividers = [1]
        for i in range(2, x - 1):
            if x % i == 0:
                dividers.append(i)
        dividers.append(x)
        return dividers


s = Solution()
print(s.text_formatting())
print(Solution.get_dividers(100))
