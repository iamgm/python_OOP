class ListMath:
    def __init__(self, lst=None):
        self.lst_math = [x for x in lst if type(x) in (int, float)] if \
                        type(lst)==list else []
    
    def __add__(self, other):
        return self.op(lambda x: x + other, True)

    def __radd__(self, other):
        return self.op(lambda x: x + other, True)

    def __sub__(self, other):
        return self.op(lambda x: x - other, True)

    def __rsub__(self, other):
        return self.op(lambda x:-x + other, True)

    def __mul__(self, other):
        return self.op(lambda x: x * other, True)

    def __rmul__(self, other):
        return self.op(lambda x: x * other, True)

    def __truediv__(self, other):
        return self.op(lambda x: x / other, True)
        
    def __rtruediv__(self, other):
        return self.op(lambda x: other / x, True)

    def __iadd__(self, other):
        return self.op(lambda x: x + other, False)
        
    def __isub__(self, other):
        return self.op(lambda x: x - other, False)

    def __imul__(self, other):
        return self.op(lambda x: x * other, False)
            
    def __itruediv__(self, other):
        return self.op(lambda x: x / other, False)

    def op(self, func, createObj):
        l = [func(x) for x in self.lst_math]
        if createObj:
            return ListMath(l)        
        
        self.lst_math = l
        return self        


# Подвиг 5. Объявите класс с именем ListMath, объекты которого можно создавать командами:

# lst1 = ListMath() # пустой список
# lst2 = ListMath([1, 2, -5, 7.68]) # список с начальными значениями
# В качестве значений элементов списка объекты класса ListMath должны отбирать только целые и вещественные числа, остальные игнорировать (если указываются в списке). Например:

# lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
# В каждом объекте класса ListMath должен быть публичный атрибут:

# lst_math - ссылка на текущий список объекта (для каждого объекта создается свой список).

# Также с объектами класса ListMath должны работать следующие операторы:

# lst = lst + 76 # сложение каждого числа списка с определенным числом
# lst = 6.5 + lst # сложение каждого числа списка с определенным числом
# lst += 76.7  # сложение каждого числа списка с определенным числом
# lst = lst - 76 # вычитание из каждого числа списка определенного числа
# lst = 7.0 - lst # вычитание из числа каждого числа списка
# lst -= 76.3
# lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
# lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
# lst *= 5.54
# lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
# lst = 3 / lst # деление числа на каждый элемент списка
# lst /= 13.0
# При использовании бинарных операторов +, -, *, / должны формироваться новые объекты класса ListMath с новыми списками, прежние списки не меняются.

# При использовании операторов +=, -=, *=, /= значения должны меняться внутри списка текущего объекта (новый объект не создается).

# P.S. В программе достаточно только объявить класс. На экран ничего выводить не нужно.