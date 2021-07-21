"""1. Напишите две функции создания списка из четных чисел от 0 до N (N - аргумент функции) [0,2,4,...N]
    с помощью метода append и с помощью list comprehensions. Через декоратор определите время работы этих функций
"""
import time


def decor_time(fn):
    def wrapper(*args):
        """определите время работы этих функций"""
        st = time.time()
        res = fn(*args)
        dt = time.time() - st
        print(f"Время работы функции: {dt} сек.")
        return res

    return wrapper


@decor_time
def create_list_odd_nums(n):
    """[0,2,4,...n]"""
    l = [i for i in range(0, n + 1) if not i % 2]
    return l


# func = decor_time(create_list_odd_nums)

# create_list_odd_nums(1000000)

"""Напишите декоратор для кэширования результатов работы функции вычисления квадратного корня положительного 
целочисленного числа х. То есть, при повторном вызове функции с одним и тем же аргументом, результат должен 
браться из кэша а не вычисляться заново. Следует использовать замыкание для хранения кэша."""


def decor_squared_int(fn):
    d = dict()

    def wrapper(*args):
        print(d)
        if args not in d:
            d[args[0]] = fn(*args)
            print(d)
            return d[args[0]]
        return d[args[0]]

    return wrapper


def squaring(x):
    return x * x


func1 = decor_squared_int(squaring)
print(func1(10))
print(func1(20))


