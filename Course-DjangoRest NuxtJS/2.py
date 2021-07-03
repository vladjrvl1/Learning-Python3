class Solution:
    @staticmethod
    def longest_common_prefix(strs: list[str]) -> str:
        """ поиск самого длинного общего префикса в списке слов """
        # если список пуст возвращаем пустую строку
        if len(strs) == 0:
            return ''
        # для сравнения берем любую строку из списка - первую
        s = strs[0]
        # проходим в цикле все остальные строки
        for i in range(1, len(strs)):
            # выполняем проверку: в каждой строке ищем подстроку s, уменьшая s на один символ с конца s[:-1] каждый раз
            # если s не совпадает с проверяемой строкой
            while strs[i].find(s) != 0:
                s = s[:-1]
                print(s)
        return s


pref = Solution()
l = ['flower', 'flow', 'flight', 'fight']
print(pref.longest_common_prefix(l))
