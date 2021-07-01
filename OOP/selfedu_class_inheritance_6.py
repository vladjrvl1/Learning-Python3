""" Создайте суперкласс "Персональные компьютеры" и на его основе подклассы Desktop и Laptop.
В базовом классе определите общие свойства: ram, memory, model, CPU. А в производных класса уникальные свйоства:
    для Desktop: монитор, клавиатура, мышь, их габариты; и метод для вывода этой информации в консоль;
    для Laptop: габариты, диагональ экрана; и метод для вывода этой информации в консоль;"""


class PC:
    def __init__(self, ram: str, memory: str, model, cpu):
        self._ram = ram
        self._memory = memory
        self._model = model
        self._cpu = cpu

    def get_params(self):
        return {'ram': self._ram, 'memory': self._memory, 'model': self._model, 'cpu': self._cpu}


class Desktop(PC):
    def __init__(self, *args, monitor, keyboard, mouse, dimensions: dict):
        super().__init__(*args)
        self._monitor = monitor
        self._keyboard = keyboard
        self._mouse = mouse
        self._dimensions = dimensions

    def print_params(self):
        pc_params = self.get_params()
        print(f'RAM:\t\t{pc_params["ram"]}\n'
              f'Memory:\t\t{pc_params["memory"]}\n'
              f'Model:\t\t{pc_params["model"]}\n'
              f'CPU:\t\t{pc_params["cpu"]}\n'
              f'Monitor:\t{self._monitor}\n'
              f'Keyboard:\t{self._keyboard}\n'
              f'Mouse:\t\t{self._mouse}\n'
              f'Dimensions:\t{self._dimensions}')


class Laptop(PC):
    def __init__(self, *args, dimensions: dict, screen_size: str):
        super().__init__(*args)
        self._dimensions = dimensions
        self._screen_size = screen_size

    def print_params(self):
        pc_params = self.get_params()
        print(f'RAM:\t\t{pc_params["ram"]}\n'
              f'Memory:\t\t{pc_params["memory"]}\n'
              f'Model:\t\t{pc_params["model"]}\n'
              f'CPU:\t\t{pc_params["cpu"]}\n'
              f'Dimensions:\t{self._dimensions}\n'
              f'Screen size:\t{self._screen_size}')


desktop1 = Desktop('16GB', '512GB', 'Acer Rog Strix', 'Intel i5=10300H', monitor='Samsung 24"',
                   keyboard='REAL-EL', mouse='REAL-EL mouse',
                   dimensions={'Samsung 24': (1, 2, 3), 'REAL-EL': (1, 2, 3), 'REAL-EL mouse': (1, 2, 3)})

laptop1 = Laptop('64GB', '1TB SSD', 'MSI', 'Intel i9=9000',
                 dimensions={"width": 30, "height": 20, "depth": 5}, screen_size='15.6"')

desktop1.print_params()
print()
laptop1.print_params()