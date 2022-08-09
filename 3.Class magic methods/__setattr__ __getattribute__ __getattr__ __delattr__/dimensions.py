class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, val):
        if self.MIN_DIMENSION <= val <= self.MAX_DIMENSION:
            self.__a = val

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, val):
        if self.MIN_DIMENSION <= val <= self.MAX_DIMENSION:
            self.__b = val

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, val):
        if self.MIN_DIMENSION <= val <= self.MAX_DIMENSION:
            self.__c = val

    def __setattr__(self, key, value):
        if key in ("MIN_DIMENSION", "MAX_DIMENSION"):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION"
                " запрещено.")
        super().__setattr__(key, value)

# Подвиг 9. Объявите в программе класс Dimensions (габариты) с атрибутами:

# MIN_DIMENSION = 10
# MAX_DIMENSION = 1000

# Каждый объект класса Dimensions должен создаваться командой:

# d3 = Dimensions(a, b, c)   # a, b, c - габаритные размеры
# и содержать локальные атрибуты:

# __a, __b, __c - габаритные размеры (целые или вещественные числа).

# Для работы с этими локальными атрибутами в классе Dimensions следует прописать следующие объекты-свойства:

# a, b, c - для изменения и считывания соответствующих локальных атрибутов __a, __b, __c.

# При изменении значений __a, __b, __c следует проверять, что присваиваемое значение число в диапазоне [MIN_DIMENSION; MAX_DIMENSION]. Если это не так, то новое значение не присваивается (игнорируется).

# С помощью магических методов данного занятия запретить создание локальных атрибутов MIN_DIMENSION и MAX_DIMENSION в объектах класса Dimensions. При попытке это сделать генерировать исключение:

# raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
# Пример использования класса  (эти строчки в программе писать не нужно):

# d = Dimensions(10.5, 20.1, 30)
# d.a = 8
# d.b = 15
# a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
# d.MAX_DIMENSION = 10  # исключение AttributeError
# P.S. В программе нужно объявить только класс Dimensions. На экран ничего выводить не нужно. 