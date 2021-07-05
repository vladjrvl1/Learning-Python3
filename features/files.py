import pickle


class File:
    def __init__(self, s_path=None, e_path=None):
        """ starting path, ending path"""
        self.__s_path = s_path
        self.__e_path = e_path

    def set_s_path(self, value: str):
        self.__s_path = value

    def set_e_path(self, value: str):
        self.__e_path = value

    def write_from_read(self, num_char: int):
        """Выполните считывания данных с одного файла через символ и записи прочитанных данных в другой
         текстовый файл. Не более 100 символов"""
        s_path = self.__s_path
        e_path = self.__e_path
        with open(s_path, 'rb') as rf:
            with open(e_path, 'wb') as wf:
                wf.write(rf.read(num_char))

    @staticmethod
    def split_input_by_word(string: str, fpath: str) -> None:
        """ Пользователь вводит предложение с клавиатуры.
        Разбейте это предложение по словам и сохраните их в столбец в файл"""
        if string == '':
            print('Empty string')
            return None
        string = string.replace(' ', '\n')
        with open(fpath, 'wb') as file:
            pickle.dump(string, file)

    @staticmethod
    def save_dict(dictionary: dict, fpath: str):
        """  Необходимо каждый элемент этого словаря сохранить в бинарном файле как объект.
        Затем прочитать этот файл и вывести считанные данные в консоль"""
        with open(fpath, 'wb') as file:
            list_dicts = [{key: value} for key, value in dictionary.items()]
            for i in list_dicts:
                pickle.dump(i, file)

    @staticmethod
    def print_file(fpath: str):
        """прочитать этот файл и вывести считанные данные в консоль"""
        try:
            with open(fpath, 'rb') as file:
                while True:
                    print(pickle.load(file))  # end можно не писать
        except EOFError:
            None
        except FileNotFoundError:
            print("Невозможно открыть файл")


path1 = 'files_txt.txt'
path2 = 'files_result.txt'

d = {"house": "дом", "car": "машина", "tree": "дерево", "road": "дорога", "river": "река"}
file1 = File(path1, path2)
file1.write_from_read(100)
file1.split_input_by_word('Hello my name is ...', 'files_result2.txt')
file1.save_dict(d, 'files_result3.txt')
file1.print_file('files_result3.txt')
