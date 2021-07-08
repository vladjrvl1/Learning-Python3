class CoordDescriptor:
    def __set_name__(self, owner, name):
        pass


class Point3D:
    """
    Создать класс Point3D для хранения трёхмерных координат.
    Перегрузить операторы __add__, __sub__, __mul__, __div__.
    Сделать возможность сравнения координат __eq__ и запись\\считывание значений через ключи: 'x', 'y', 'z'.
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def is_int(val):
        if isinstance(val, int):
            return True
        raise ValueError('Значение должно быть целым числом')

    @staticmethod
    def is_str(val):
        if isinstance(val, str):
            return True
        raise ValueError('Ключ должен быть строкой')

    @staticmethod
    def check_operands(other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Правый операнд должен быть Point3D")

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def set_x(self, val):
        if Point3D.is_int(val):
            self.x = val

    def set_y(self, val):
        if Point3D.is_int(val):
            self.y = val

    def set_z(self, val):
        if Point3D.is_int(val):
            self.y = val

    def __setitem__(self, key, value):
        Point3D.is_str(key)
        Point3D.is_int(value)

        if key == 'x':
            self.x = value
        if key == 'y':
            self.y = value
        if key == 'z':
            self.z = value

    def __getitem__(self, item):
        if Point3D.is_str(item):
            if item == 'x':
                return self.x
            elif item == 'y':
                return self.y
            elif item == 'z':
                return self.z
            else:
                raise KeyError('Неверный ключ')

    def __add__(self, other):
        Point3D.check_operands(other)
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        Point3D.check_operands(other)
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        Point3D.check_operands(other)
        return Point3D(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        Point3D.check_operands(other)
        return Point3D(self.x / other.x, self.y / other.y, self.z / other.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'


cor1 = Point3D(11, 10, 21)
cor2 = Point3D(22, 12, 42)
cor3 = Point3D(33, 13, 63)

