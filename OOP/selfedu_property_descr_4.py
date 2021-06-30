# property
# descriptors
# https://www.youtube.com/watch?v=zwel95I7O88&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=4


# class CoordValue:
#     """ Дескриптор
#     Запись __value в класс"""
#
#     def __get__(self, instance, owner):
#         return self.__value
#
#     def __set__(self, instance, value):
#         self.__value = value
#
#     def __delete__(self, instance):
#         del self.__value

# class CoordValue:
#     """ Дескриптор
#     Запись __value в instance"""
#
#     def __init__(self, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         instance.__dict__[self.__name] = value
#
#
# class Point:
#     coord_x = CoordValue("coord_x")
#     coord_y = CoordValue("coord_y")
#
#     def __init__(self, x=0, y=0):
#         self.coord_x = x
#         self.coord_y = y

# class NoDataDescr:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return "NoDataDescr __get__"

class CoordValue:
    """ Data Дескриптор
    Запись __value в instance"""

    def __set_name__(self, owner, name):
        print(name)
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value


class Point:
    coord_x = CoordValue()
    coord_y = CoordValue()

    def __init__(self, x=0, y=0):
        self.coord_x = x
        self.coord_y = y


pt = Point(1, 2)
pt2 = Point(10, 20)
print(pt.coord_x, pt2.coord_x)

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(value):
#         if isinstance(value, int) or isinstance(value, float):
#             return True
#         else:
#             return False
#
#     @property
#     def coord_x(self):
#         return self.__x
#
#     @coord_x.setter
#     def coord_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             raise ValueError("Неверный формат данных")
#
#     @coord_x.deleter
#     def coord_x(self):
#         print(f"Удаление {self.__x}")
#         del self.__x


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(value):
#         if isinstance(value, int) or isinstance(value, float):
#             return True
#         else:
#             return False
#
#     def __get_coord_x(self):
#         return self.__x
#
#     def __set_coord_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             raise ValueError("Неверный формат данных")
#     def __del_coord_x(self):
#         print(f"Удаление {self.__x}")
#         del self.__x
#     coordX = property(__get_coord_x, __set_coord_x, __del_coord_x)
#
#
# pt = Point(1, 2)
# pt.coordX = 100
# print(pt.coordX)
# del pt.coordX
# pt.coordX = 7
# print(pt.coordX)
