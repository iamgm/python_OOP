class Vector:
    def __init__(self, *coords):
        self.coords = list(coords)

    def __add__(self, other):
        self.validate_dims(self, other)
        return Vector(*self.do(self, other, lambda x,y: x + y))

    def __sub__(self, other):
        self.validate_dims(self, other)
        return Vector(*self.do(self, other, lambda x,y: x - y))

    @staticmethod
    def do(first, second, func):
        return [func(x,y) for x,y in zip(first.coords, second.coords)]

    @staticmethod
    def validate_dims(first, second):
        if len(first.coords) != len(second.coords):
            raise TypeError('размерности векторов не совпадают')

    def get_coords(self):
        return tuple(self.coords)

class VectorInt(Vector):
    def __init__(self, *coords):
        self.validate_coords(*coords)
        super().__init__(*coords)
        
    @staticmethod
    def validate_coords(*coords):
        for c in coords:
            if not isinstance(c, int):
                raise ValueError('координаты должны быть целыми числами')

    def __add__(self, other):
        return self.math_op(other, lambda x,y: x + y)

    def __sub__(self, other):
        return self.math_op(other, lambda x,y: x - y)

    def math_op(self, other, func):
        self.validate_dims(self, other)
        res = self.do(self, other, lambda x,y: func(x, y))
        is_float = sum([False if isinstance(x, int) else True for x in res])
        return Vector(*res) if is_float else VectorInt(*res)

# Подвиг 10 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:
# v = Vector(x1, x2, ..., xN)
# где x1, x2, ..., xN - координаты радиус-вектора (числа: целые или вещественные).
# С объектами этого класса должны выполняться команды:
# v1 = Vector(1, 2, 3)
# v2 = Vector(3, 4, 5)
# v = v1 + v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
# v = v1 - v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
# Если размерности векторов v1 и v2 не совпадают, то генерировать исключение:
# raise TypeError('размерности векторов не совпадают')
# В самом классе Vector объявите метод с именем get_coords, который возвращает кортеж из текущих координат вектора.
# На основе класса Vector объявите дочерний класс VectorInt для работы с целочисленными координатами:
# v = VectorInt(1, 2, 3, 4)
# v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')
# При операциях сложения и вычитания с объектом класса VectorInt:
# v = v1 + v2  # v1 - объект класса VectorInt
# v = v1 - v2  # v1 - объект класса VectorInt
# должен формироваться объект v как объект класса Vector, если хотя бы одна координата является вещественной. Иначе, v должен быть объектом класса VectorInt.
# P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.