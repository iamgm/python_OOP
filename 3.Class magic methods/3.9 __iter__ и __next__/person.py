class Person:
    def __init__(self, *args):
        self.fio, self.job, self.old, self.salary, self.year_job = args
        self.keys = tuple(self.__dict__.keys())

    def __getitem__(self, idx):
        self.validate_idx(idx)
        return getattr(self, self.keys[idx])

    def __setitem__(self, idx, value):
        self.validate_idx(idx)
        setattr(self, self.keys[idx], value)

    @staticmethod
    def validate_idx(idx):
        if not (isinstance(idx, int) or (0 <= idx <= 4)):
            raise IndexError('неверный индекс')

# Подвиг 5. Объявите в программе класс Person, объекты которого создаются командой:

# p = Person(fio, job, old, salary, year_job)
# где fio - ФИО сотрудника (строка); job - наименование должности (строка); old - возраст (целое число); salary - зарплата (число: целое или вещественное); year_job - непрерывный стаж на указанном месте работы (целое число).

# В каждом объекте класса Person автоматически должны создаваться локальные атрибуты с такими же именами: fio, job, old, salary, year_job и соответствующими значениями.

# Также с объектами класса Person должны поддерживаться следующие команды:

# data = p[indx] # получение данных по порядковому номеру (indx) атрибута (порядок: fio, job, old, salary, year_job и начинается с нуля)
# p[indx] = value # запись в поле с указанным индексом (indx) нового значения value
# for v in p: # перебор всех атрибутов объекта в порядке: fio, job, old, salary, year_job
#     print(v)
# При работе с индексами, проверить корректность значения indx. Оно должно быть целым числом в диапазоне [0; 4]. Иначе, генерировать исключение командой:

# raise IndexError('неверный индекс')
# Пример использования класса (эти строчки в программе не писать):

# pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
# pers[0] = 'Балакирев С.М.'
# for v in pers:
#     print(v)
# pers[5] = 123 # IndexError
# P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.