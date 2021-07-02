class Square:
    """ Вычисляемые property"""

    def __init__(self, s):
        self.__side = s
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__area = None
        self.__side = value

    @property
    def area(self):
        """Делаем из Square.area() - Square.area"""
        if self.__area is None:
            self.__area = self.side ** 2
        return self.__area


sq = Square(5)
print(sq.area)
sq.side = 4
print(sq.area)
