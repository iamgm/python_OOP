from math import isclose

class Vector:
    def __init__(self, *coords):
        self.coords = list(coords)
    
    def __add__(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')
        return self.do(lambda x,y: x + y, other, True)

    def __sub__(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')        
        return self.do(lambda x,y: x - y, other, True)

    def __mul__(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')        
        return self.do(lambda x,y: x * y, other, True)

    def __iadd__(self, other):
        return self.do(lambda x,y: x + y, other, False)

    def __isub__(self, other):
        return self.do(lambda x,y: x - y, other, False)

    def __eq__(self, other):
        return all([isclose(x, y, abs_tol = 1e-9) for x, y in \
                    zip(self.coords, other.coords)])
        
    def do(self, func, other, createObj):
        l = [func(x, other) for x in self.coords] \
            if type(other) in (float, int) else \
            [func(x,y) for x, y in zip(self.coords, other.coords)]
        
        if createObj:
            return Vector(*l)
        self.coords = l
        return self

# v1 = Vector(*[x for x in range(10)])
# v2 = Vector(*[x for x in range(2,12)])

# # v1 -= 10
# # v1 += 110
# v2-=2
# print(v1 == v2)
# print(v1.coords)
# Подвиг 9 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:

# v = Vector(x1, x2, x3,..., xN)
# где x1, x2, x3,..., xN - координаты вектора (числа: целые или вещественные).

# С каждым объектом класса Vector должны выполняться операторы:

# v1 + v2 # суммирование соответствующих координат векторов
# v1 - v2 # вычитание соответствующих координат векторов
# v1 * v2 # умножение соответствующих координат векторов

# v1 += 10 # прибавление ко всем координатам вектора числа 10
# v1 -= 10 # вычитание из всех координат вектора числа 10
# v1 += v2
# v2 -= v1

# v1 == v2 # True, если соответствующие координаты векторов равны
# v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает
# При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с новыми (вычисленными) координатами. При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.

# Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -, * должно генерироваться исключение командой:

# raise ArithmeticError('размерности векторов не совпадают')
# P.S. В программе на экран выводить ничего не нужно, только объявить класс.