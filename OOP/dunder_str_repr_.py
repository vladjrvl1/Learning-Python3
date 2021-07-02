""" class Person: конструктор __init__, принимающий 3 аргумента: name, surname, gender. Атрибут gender может принимать только 2
значения: "male" и "female", по умолчанию "male". Если в атрибут gender передается любое другое значение,
печатать сообщение: "Не знаю, что вы имели ввиду? Пусть это будет мальчик!" и проставить атрибут gender
значением "male" переопределить метод __str__ следующим образом:
если объект - мужчина (атрибут gender = "male"), возвращать строку "Гражданин <Фамилия> <Имя>
если объект - женщина (атрибут gender = "female"), возвращать строку "Гражданка <Фамилия> <Имя>"""


class Person:
    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        self.gender = gender
        if gender not in ("male", "female"):
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            self.gender = 'male'
    def __str__(self):
        if self.gender == 'male':
            return f"Гражданин {self.surname} {self.name}"
        return f"Гражданка {self.surname} {self.name}"


""" class Vector: конструктор __init__, принимающий произвольное количество аргументов. Среди всех переданных 
аргументов необходимо оставить только целые числа и сохранить их в атрибут values в виде списка;
переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом: 
"Вектор(<value1>, <value2>, <value3>, ...)", если вектор не пустой. При этом значения должны быть 
упорядочены по возрастанию (будьте аккуратнее с пробелами, они стоят только после запятых, см. пример ниже);
"Пустой вектор", если наш вектор не хранит в себе значения"""


class Vector:
    def __init__(self, *args: int):
        self.values = [i for i in args if isinstance(i, int)]

    def __str__(self):
        if len(self.values):
            return f"Вектор{tuple(sorted(self.values))}"
        return f'Пустой вектор'
