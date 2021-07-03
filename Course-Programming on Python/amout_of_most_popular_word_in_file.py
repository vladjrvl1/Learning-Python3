class Solution:
    @staticmethod
    def read_file(file) -> str:
        with open(file) as f:
            txt = f.read()
        return txt

    @staticmethod
    def count_amount_of_words(txt) -> (str, int):
        s = txt.lower().strip().split()
        d = {}
        for i in set(s):
            d.update({i: s.count(i)})
        max_d = max(d.values())
        equals = set()
        for key, value in d.items():
            if max_d == value:
                equals.add(key)
        return min(equals), max_d


sol = Solution()
print(sol.count_amount_of_words(sol.read_file('text.txt')))
