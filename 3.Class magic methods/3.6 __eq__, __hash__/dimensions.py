import math
s_inp = input()

class Dimensions:
    def __new__(cls, *args, **kwargs):
        cls.non_positive(args[0], args[1], args[2])
        return super().__new__(cls)

    @staticmethod
    def non_positive(a, b, c):
        if (math.isclose(a, 0, abs_tol = 1e-9) or (a < 0)) or \
           (math.isclose(b, 0, abs_tol = 1e-9) or (b < 0)) or \
           (math.isclose(c, 0, abs_tol = 1e-9) or (c < 0)):
            raise ValueError("размеры должны быть положительными числами")

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self):
        return hash((self.a, self.b, self.c))

l = [tuple(map(float, x.split())) for x in s_inp.split("; ")]
lst_dims = sorted([Dimensions(*x) for x in l], key = lambda x: hash(x))

# s_inp =  "1 2 3; 4 5 6.78; 1 1 3; 0.00000001 1 2.5"
# print([(x.a, x.b, x.c) for x in lst_dims])
# [print(x,hash(x)) for x in lst_dims]
# Подвиг 9 (релакс). Объявите класс с именем Dimensions, объекты которого создаются командой:

# d = Dimensions(a, b, c)
# где a, b, c - положительные числа (целые или вещественные), описывающие габариты некоторого тела: высота, ширина и глубина.

# Каждый объект класса Dimensions должен иметь аналогичные публичные атрибуты a, b, c (с соответствующими числовыми значениями). Также для каждого объекта должен вычисляться хэш на основе всех трех габаритов: a, b, c.

# С помощью функции input() прочитайте из входного потока строку, записанную в формате:

# "a1 b1 c1; a2 b2 c2; ... ;aN bN cN"

# Например:

# "1 2 3; 4 5 6.78; 1 2 3; 0 1 2.5"

# Если какой-либо габарит оказывается отрицательным значением или равен нулю, то при создании объектов должна генерироваться ошибка командой:

# raise ValueError("габаритные размеры должны быть положительными числами")
# Сформируйте на основе прочитанной строки список lst_dims из объектов класса Dimensions. После этого отсортируйте этот список по возрастанию (неубыванию) хэшей этих объектов так, чтобы объекты с равными хэшами стояли друг за другом.

# P.S. На экран ничего выводить не нужно.

# Sample Input:

# 1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5
# Sample Output: