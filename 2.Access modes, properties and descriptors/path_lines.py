import math
class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__next  = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj

class PathLines:
    def __init__(self, *linesObj):
        self.head = self.tail = linesObj[0]
        for l in linesObj[1:]:
            self.tail.next = l
            self.tail = l

    def get_path(self):
        line =  self.head
        l = []
        while line != self.tail:
            l.append(line)
            line = line.next
        l.append(self.tail)
        return l

    def add_line(self, line):
        self.tail.next = line
        self.tail = line

    def get_length(self):
        x0 = y0 = 0 
        line = self.head
        s = 0
        while line:
            s += math.sqrt((line.x-x0)**2 + (line.y-y0)**2)
            x0 = line.x
            y0 = line.y
            line = line.next
        return s

# Подвиг 9 (на закрепление). Вам требуется сформировать класс PathLines для описания маршрутов, состоящих из линейных сегментов. При этом каждый линейный сегмент предполагается задавать отдельным классом LineTo. Объекты этого класса будут формироваться командой:

# line = LineTo(x, y)
# где x, y - следующая координата линейного участка (начало маршрута из точки 0, 0).

# В каждом объекте класса LineTo должны формироваться локальные атрибуты:

# x, y - для хранения координат конца линии (начало определяется по координатам предыдущего объекта).

# Объекты класса PathLines должны создаваться командами:

# p = PathLines()                   # начало маршрута из точки 0, 0
# p = PathLines(line1, line2, ...)  # начало маршрута из точки 0, 0
# где line1, line2, ... - объекты класса LineTo.

# Сам же класс PathLines должен иметь следующие методы:

# get_path() - возвращает список из объектов класса LineTo (если объектов нет, то пустой список);
# get_length() - возвращает суммарную длину пути (сумма длин всех линейных сегментов);
# add_line(self, line) - добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута.

# Пояснение: суммарный маршрут - это сумма длин всех линейных сегментов, а длина каждого линейного сегмента определяется как евклидовое расстояние по формуле:

# L = sqrt((x1-x0)^2 + (y1-y0)^2)

# где x0, y0 - предыдущая точка маршрута; x1, y1 - текущая точка маршрута.

# Пример использования классов (эти строчки в программе писать не нужно):

# p = PathLines(LineTo(10, 20), LineTo(10, 30))
# p.add_line(LineTo(20, -10))
# dist = p.get_length()
# P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно. 