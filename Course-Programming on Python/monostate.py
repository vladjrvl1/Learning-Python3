class Cat:
    """ ссылка на изменяемый объект """
    __shared_attr = {
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr


a = Cat()
b = Cat()
