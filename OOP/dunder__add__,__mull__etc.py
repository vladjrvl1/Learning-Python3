class Vector:
    def __init__(self, *args):
        self.values = [integer for integer in args if isinstance(integer, int)]
        self.values.sort()

    @staticmethod
    def len_compare(iter_1, iter_2):
        return len(iter_1) == len(iter_2)

    def __str__(self):
        if self.values:
            return f'Вектор{tuple(self.values)}'
        return 'Пустой вектор'

    def __add__(self, other):
        if isinstance(other, int):
            arguments = [other + i for i in self.values]
            return Vector(*arguments)
        elif isinstance(other, Vector):
            if Vector.len_compare(self.values, other.values):
                arguments = [self.values[i] + other.values[i] for i in range(len(self.values))]
                return Vector(*arguments)
            else:
                print("Сложение векторов разной длины недопустимо")
                return Vector()
        else:
            print(f"Вектор нельзя сложить с {other}")

    def __mul__(self, other):
        if isinstance(other, int):
            arguments = [other * i for i in self.values]
            return Vector(*arguments)
        elif isinstance(other, Vector):
            if Vector.len_compare(self.values, other.values):
                arguments = [self.values[i] * other.values[i] for i in range(len(self.values))]
                return Vector(*arguments)
            else:
                print("Умножение векторов разной длины недопустимо")
                return Vector()
        else:
            print(f"Вектор нельзя умножать с {other}")
v = Vector(1,2,3)
print(v)