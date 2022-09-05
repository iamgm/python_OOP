class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.table = tuple(tuple(Cell(0) for y in range(self.cols)) 
                            for x in range(self.rows))

    def __getitem__(self, rc):
        self.validate_idx(rc[0], rc[1])
        return self.table[rc[0]][rc[1]].data

    def __setitem__(self, rc, value):
        self.validate_idx(rc[0], rc[1])
        self.validate_type(value)
        self.table[rc[0]][rc[1]].data = value

    def validate_type(self, value):
        if not isinstance(value, self.type_data):
            raise TypeError('неверный тип присваиваемых данных')

    def validate_idx(self, row, col):
        if not (isinstance(row, int) and isinstance(col, int) and
                (0 <= row < self.rows) and (0 <= col < self.cols)):
            raise IndexError('неверный индекс')

    def __iter__(self):
        for row in self.table:
            yield (c.data for c in row)
        
class Cell:
    def __init__(self, data):
        self.data = data
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        self.__data = value
                    

tb = TableValues(3, 2)
n = m = 0
for row in tb:
    n += 1
    for value in row:
        m += 1
        assert type(value) == int

# tv = TableValues(10, 10)
# [([print(y.data, end=" ") for y in x], print()) for x in tv]
# itt = iter(tv)
# tv[8, 1]  = 81
# [([print(y.data, end=" ") for y in x], print()) for x in tv]


# Подвиг 9. В программе необходимо реализовать таблицу TableValues по следующей схеме:

# Сам класс TableValues представляет таблицу в целом, объекты которого создаются командой:

# table = TableValues(rows, cols, type_data)
# где rows, cols - число строк и столбцов таблицы; type_data - тип данных ячейки (int - по умолчанию, float, list, str и т.п.). Начальные значения в ячейках таблицы равны 0 (целое число).

# Каждая ячейка таблицы должна быть представлена классом Cell. Объекты этого класса создаются командой:

# cell = Cell(data)
# где data - данные в ячейке. В каждом объекте класса Cell должен формироваться локальный приватный атрибут __data с соответствующим значением. Для работы с ним в классе Cell должно быть объект-свойство (property):

# data - для записи и считывания информации из атрибута __data.

# При попытке записать данные другого типа (не совпадающего с атрибутом type_data объекта класса TableValues), должно генерироваться исключение командой:

# raise TypeError('неверный тип присваиваемых данных')
# С объектами класса TableValues должны выполняться следующие команды:

# table[row, col] = value# запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
# value = table[row, col] # считывание значения из ячейки с индексами row, col

# for row in table:  # перебор по строкам
#     for value in row: # перебор по столбцам
#         print(value, end=' ')  # вывод значений ячеек в консоль
#     print()
# При работе с индексами row, col, необходимо проверять их корректность. Если индексы не целое число или они выходят за диапазон размера таблицы, то генерировать исключение командой:

# raise IndexError('неверный индекс')
# P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
#  