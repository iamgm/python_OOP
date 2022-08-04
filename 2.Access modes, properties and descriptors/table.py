class FloatValue:
    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")
        setattr(instance, self.name, value)

class Cell:
    value = FloatValue()

    def __init__(self, value):
        self.value = value
            
class TableSheet:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.cells = [[Cell(0.0) for i in range(M)] for j in range(N)]        

table = TableSheet(5,3)
for i in range(table.N):
    for j in range(table.M):
        table.cells[i][j].value = j + 1.0 + table.M*i



# for i in table.cells:
#     for j in i:
#         print(j.value, end=" ")
#     print()

[([print(j.value, end=" ") for j in i], print()) for i in table.cells]


# Подвиг 6. Объявите дескриптор данных FloatValue, который бы устанавливал и возвращал вещественные значения. При записи вещественного числа должна выполняться проверка на вещественный тип данных. Если проверка не проходит, то генерировать исключение командой:

# raise TypeError("Присваивать можно только вещественный тип данных.")
# Объявите класс Cell, в котором создается объект value дескриптора FloatValue. А объекты класса Cell должны создаваться командой:

# cell = Cell(начальное значение ячейки)
# Объявите класс TableSheet, с помощью которого создается таблица из N строк и M столбцов следующим образом:

# table = TableSheet(N, M)
# Каждая ячейка этой таблицы должна быть представлена объектом класса Cell, работать с вещественными числами через объект value (начальное значение должно быть 0.0).

# В каждом объекте класса TableSheet должен формироваться локальный атрибут:

# cells - список (вложенный) размером N x M, содержащий ячейки таблицы (объекты класса Cell).

# Создайте объект table класса TableSheet с размером таблицы N = 5, M = 3. Запишите в эту таблицу числа от 1.0 до 15.0 (по порядку).

# P.S. На экран в программе выводить ничего не нужно.