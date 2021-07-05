# три наименьшие числа в списке
a = [1, 2, -5, 0, 10]
print(sorted(a)[:3], '\n')


# сначала отрицательные числа затем положительные
def sort_negative_nums_first(nums: iter) -> list:
    return sorted(nums, key=lambda x: x == 0 or x > 0)


nums = (-10, 0, 7, -2, 3, 6 - 8)
print(sort_negative_nums_first(nums))


# вывести номера по возрастанию чисел в ключах
def sort_phones_nums_by_code(numbers: dict[str: int]) -> dict:
    return {x: numbers[x] for x in sorted(numbers, key=int)}


d = {'+7': 2345678901, '+4': 3456789012, '+5': 567891234, '+12': 78901234}
print(sort_phones_nums_by_code(d))

