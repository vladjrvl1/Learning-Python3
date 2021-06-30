"""
1.
Объявите класс Calendar для хранения даты: день, месяц, год.
Определите свойства для записи и считывания этой информации из этого
класса. (Дополнение: используя __Slots__ разрешите использовать
только строго определнные локальные свойства в экземплярах класса).
2.
Объявите класс Rectangle, хранящий координаты верхней левой и правой нижней точек. Создавайте дескрипторы для записи и
считывания этих значений в классе (атрибуты с данными координат должны быть приватными).
"""


class Descriptor:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        print('call __get__')
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.__name]


class Calendar:
    """
    1.
    Via Descriptors
    """
    day = Descriptor()
    month = Descriptor()
    year = Descriptor()

    def __init__(self, date, d_format='dd-mm-yyyy'):
        if d_format == 'dd-mm-yyyy':
            self.day = date[:2]
            self.month = date[3:5]
            self.year = date[6:]

    def __str__(self):
        return f'{self.day}-{self.month}-{self.year}'


# class Calendar:
#     """
#     1.
#     Via Property
#     """
#     __slots__ = ['__day', '__month', '__year']

# def __init__(self, date, d_format='dd-mm-yyyy'):
#     if d_format == 'dd-mm-yyyy':
#         self.__day = date[:2]
#         self.__month = date[3:5]
#         self.__year = date[6:]

# @property
# def day(self):
#     print('getter')
#     return self.__day

# @day.setter
# def day(self, value):
#     print('setter')
#     self.__day = value

# @property
# def month(self):
#     print('getter')
#     return self.month

# @month.setter
# def month(self, value):
#     print('setter')
#     self.__month = value

# @property
# def year(self):
#     print('getter')
#     return self.__year

# @year.setter
# def year(self, value):
#     print('setter')
#     self.__year = value


class Rectangle:
    """
    2.
    Объявите класс Rectangle, хранящий координаты верхней левой и правой нижней точек. Создавайте дескрипторы для записи и
    считывания этих значений в классе (атрибуты с данными координат должны быть приватными).
    """
    x1 = Descriptor()
    y1 = Descriptor()
    x2 = Descriptor()
    y2 = Descriptor()

    def __init__(self, x, y):
        x1, x2, = x
        y1, y2 = y
        if x1 > 0 > x2 and y1 > 0 > y2:
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2
        else:
            raise ValueError("Значения должны быть числами")

    def __str__(self):
        return f'(x1 {self.x1}, y1 {self.y1}); (x2 {self.x2}, y2 {self.y2});'


rect = Rectangle((10, -10), (20, -25))
print(rect)
