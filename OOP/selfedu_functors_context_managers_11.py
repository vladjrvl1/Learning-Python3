"""1.
Функторы – это объекты классов, которые можно выполнять как функции.
Создайте функтор для определения порядка сортировки списка р, состоящий из объектов класса Person.
То есть, вызывая функтор с названием поля SortKey('surname'), сортировка выполнялась бы по этому свойству.
Если указать сразу два значения surname, forename, то сортировка делалась бы по фамилии, но при их равенстве по имени
"""


class Person:
    def __init__(self, surname, forename, old):
        self.surname = surname
        self.forename = forename
        self.old = old

    def __repr__(self):
        return f'{self.surname} {self.forename} {self.old}'


p = [
    Person('Иванов', "Иван", 22),
    Person('Петров', "Гриша", 30),
    Person('Журавель', "Влад", 24),
]


class SortKey:
    def __init__(self, *args):
        self.__sort_keys = args

    def __call__(self, lst: list) -> None:
        if not lst:
            return None
        test = [key for key in self.__sort_keys if key not in lst[0].__dict__.keys()]
        if test:
            raise KeyError(f"ОШИБКА {tuple(test)} таких ключей нет, в данном списке "
                           f"имеются следующие ключи {tuple(lst[0].__dict__.keys())}")
        else:
            lst.sort(key=lambda item: [item.__dict__[key] for key in self.__sort_keys])
