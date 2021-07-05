class Solution:
    """1. Пользователь через пробел вводит ФИО. На основе этой информаци требуется создать строку с сообщением:
    Ваши персональные данные:
    Фамилия: введенная фамилия
    Имя: введенное имя
    Отчество: введенное отчество
        2. Имеется текстовый файл с содержимым:
    Иван, ivan@gm.com, 18
    Татьяна, tat@gm.com, 22
    Сергей, srg@ml.ru, 33
    Федор, fr@ml.ru, 41
    Елена, el@gm.com, 27
        Необходимо построчно считывать информацию для каждой строки и  для лиц не старше 30 лет сформировать сообщение
    Уважаемый(ая) {name}! Приглашаем Вас принять участие в курсах по изучению Python. Подробную информацию мы выслали
    на  email: {email} """
    _fio_pattern = ('Фамилия', 'Имя', 'Отчество')

    @classmethod
    def input_fio(cls, string: str) -> list[str]:
        fio = string.strip().split()
        print("Ваши персональные данные:")
        for i in range(len(fio)):
            print(f'{cls._fio_pattern[i]}: {fio[i]}')
        return fio

    @staticmethod
    def print_invite(path, encoding='utf-8'):
        with open(path, encoding=encoding) as file:
            for i in file:
                line = i.strip()
                name = line[:line.find(',')]
                email = line[line.find(',') + 2:line.rfind(',')]
                age = int(line[line.rfind(' '):])
                if age <= 30:
                    print(
                        f"Уважаемый(ая) {name}! Приглашаем Вас принять участие в курсах по изучению Python."
                        f"Подробную информацию мы выслали на email: {email}")


sol = Solution()
sol.print_invite('fstrings.txt')
print()
sol.input_fio('Журавель Владислав Витальевич')
