""" Создайте базовый класс Table и дочерние: Rectangle, Circle. Через конструктор базового класса передавайте
размер поверхности стола: для прямоугольного - ширина (w) и длина (h), для круглого - радиус (r).
В дочерних классах реализуйте метод вычисление площади поверхности стола"""


class Table:
    def __init__(self, x, y=None):
        if y is None:
            self._r = x
        else:
            self._w = x
            self._h = y


class Rectangle(Table):
    def calc_area(self):
        return self._w * self._h


class Circle(Table):
    def calc_area(self):
        return 3.14 * self._r ** 2


# rectangle_table, circle_table = Rectangle(5, 10), Circle(10)
# print(rectangle_table.calc_area(), circle_table.calc_area())

""" Создайте класс Animal и разные производные от него подклассы: Cow, Bird, Cat, Dog и т.п.
Реализуйте у них общий метод say(), который возвращает звук издаваемый этими животными.
Создайте кортеж из нескольких экземпляров классов, переберите их и в ццикле выведите в консоль их звуки"""


class Animal:
    def say(self):
        return NotImplementedError("В дочернем классе должен быть метод say()")


class Cow(Animal):
    def say(self):
        return "Mooooo"


class Bird(Animal):
    def say(self):
        return "Chrk-chrk-chrk"


class Cat(Animal):
    def say(self):
        return "Mewww"


class Dog(Animal):
    def say(self):
        return "Gooof"


figs = cow, bird, cat, dog = Cow(), Bird(), Cat(), Dog()
for i in figs:
    print(i.say())
