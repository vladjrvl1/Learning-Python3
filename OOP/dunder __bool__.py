class City:
    """
    конструктор __init__, принимающий единственный аргумент - название города. Вам необходимо сохранить его в качестве
    атрибута экземпляра name, причем вам нужно преобразовать переданное имя города таким образом, чтобы первая буква
    каждого слова была заглавной, а остальные оказались строчными (пример "new york" - > "New York")
    переопределить метод __str__ таким образом, чтобы он возвращал имя города
    переопределить метод __bool__ так, чтобы он возвращал False ,если название города заканчивается на любую гласную
    букву латинского алфавита (a, e, i, o, u), в противном случае True
    """

    def __init__(self, name: str):
        self.name = name.title()

    def __str__(self):
        return self.name

    def __bool__(self):
        return False if self.name[-1] in ('a', 'e', 'i', 'o', 'u') else True


class Quadrilateral:
    """
        конструктор __init__. Он должен сохранять в экземпляр класса два атрибута: width и height. При этом в сам метод
         __init__ может передаваться один аргумент(тогда в width и height присваивать это одно одинаковое значение,
         тем самым делать квадрат), либо два аргумента( первый идет в атрибут width, второй - в height)
        переопределить метод __str__ следующим образом:
        если width и height одинаковые, возвращать строку "Куб размером <width>х<height>
        в противном случае, возвращать строку "Прямоугольник размером <width>х<height>
        переопределить метод __bool__ так, чтобы он возвращал True, если объект является кубом,
        и False в противном случае
    """

    def __init__(self, width, height=None):
        if height:
            self.width = width
            self.height = height
        else:
            self.width = width
            self.height = width

    def __str__(self):
        return f'Куб размером {self.width}х{self.height}' if self.width == self.height else \
            f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        return True if self.width == self.height else False


q1 = Quadrilateral(10)
print(q1)  # печатает "Куб размером 10х10"
print(bool(q1))  # печатает "True"
q2 = Quadrilateral(3, 5)
print(q2)  # печатает "Прямоугольник размером 3х5"
print(q2 == True)  # печатает "False"