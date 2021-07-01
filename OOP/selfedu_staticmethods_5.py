class Rectangle:
    @staticmethod
    def __calc_area(w, h):
        return w * h

    def __init__(self, width, height):
        self.__area = Rectangle.__calc_area(width, height)

    def get_area(self):
        return self.__area


rect1 = Rectangle(20, 10)


class Dog:
    __count = 0
    __instances = 5

    def __new__(cls, *args, **kwargs):
        if cls.__count < Dog.__instances:
            return super(Dog, cls).__new__(cls)
        else:
            print(f'{Dog.__instances} objects already exist')

    @staticmethod
    def get_count():
        return Dog.__count

    def __init__(self, name, breed, age):
        Dog.__count += 1
        self._name = name
        self._breed = breed
        self._age = age

    def __str__(self):
        return '{} {} {}'.format(self._name, self._breed, self._age)



d1 = Dog('john', 'fff', 5)
d2 = Dog('mike', 'ggg', 7)
d3 = Dog('oscar', 'ttt', 9)
d4 = Dog('caesar', 'sss', 12)
d5 = Dog('khan', 'sss', 5)
d6 = Dog('111', 'ddd', 3)
print(d1)
print(d2)
print(d3)
print(d5)
print(d4)

