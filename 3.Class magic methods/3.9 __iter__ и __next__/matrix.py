class Matrix:
    def __init__(self, *args):
        if len(args) == 1 and type(args[0]) == list:
            if self.is_num(args[0]) and self.is_rect(args[0]):
                self.mx = args[0]
                self.rows = len(self.mx)
                self.cols = len(self.mx[0])
                return
            raise TypeError('список должен быть прямоугольным, состоящим '
                            'из чисел')
        
        self.check_type(*args)
        self.rows = args[0]
        self.cols = args[1]
        self.fill_value = args[2]
        self.mx = [[self.fill_value for _ in range(self.cols)] 
                        for x in range(self.rows)]

    @staticmethod
    def check_type(rows, cols, fill_value):
        if  (type(rows) != int) or (type(cols) != int) or \
            (type(fill_value) not in (int, float)):
            raise TypeError('аргументы rows, cols - целые числа; fill_value - '
                            'произвольное число')

    @staticmethod
    def is_rect(L):
        row_len = len(L[0])
        return not sum([False if len(row) == row_len else True for row in L])

    @staticmethod
    def is_num(L):
        ln = sum(len(x) for x in L)
        return sum(isinstance(e, (int, float)) for r in L for e in r) == ln

    @staticmethod
    def validate_val(value):
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')
    
    def validate_idx(self, idx):
        if not ((0 <= idx[0] < self.rows) and (0 <= idx[1] < self.cols)):
            raise IndexError('недопустимые значения индексов')

    def __getitem__(self, idx):
        self.validate_idx(idx)
        return self.mx[idx[0]][idx[1]]

    def __setitem__(self, idx, value):
        self.validate_idx(idx)
        self.validate_val(value)
        self.mx[idx[0]][idx[1]] = value

    @staticmethod
    def is_mxsize_same(m1, m2):
        l1 = sum(len(row) for row in m1)
        l2 = sum(len(row) for row in m2)
        if not ((l1 == l2) and (len(m1) == len(m2))):
            raise ValueError('операции возможны только с матрицами равных '
                             'размеров')

    def apply(self, m1, m2, f):
        if isinstance(m2, (int, float)):
            return Matrix([[f(el, m2) for el in r] for r in m1])
        self.is_mxsize_same(m1, m2.mx)
        return Matrix([[f(a,b) for a,b in zip(x,y)] for x,y in zip(m1, m2.mx)])

    def __add__(self, other):
        return self.apply(self.mx, other, lambda x, y: x + y)

    def __radd__(self, other):
        return self.apply(self.mx, other, lambda x, y: x + y)

    def __sub__(self, other):
        return self.apply(self.mx, other, lambda x, y: x - y)

    def __rsub__(self, other):
        return self.apply(self.mx, other, lambda x, y: y - x)

    def __mul__(self, other):
        return self.apply(self.mx, other, lambda x, y: x * y) 

    def __rmul__(self, other):
        return self.apply(self.mx, other, lambda x, y: x * y) 

    def __truediv__(self, other):
        return self.apply(self.mx, other, lambda x, y: x / y) 

    def __rtruediv__(self, other):
        return self.apply(self.mx, other, lambda x, y: y / x) 


# m = Matrix(10, 10, 7)
# print(m.matrix)

# l1 = [[5 for _ in range(10)] for x in range(10)]
# l2 = [[2 for _ in range(10)] for x in range(10)]
# l1[0][5] = "A"
# del l1[0][6]
# del l1[7]
# [print(x) for x in l1]
# m = Matrix(list2D)
# m1 = Matrix(l1)
# m2 = Matrix(l2)
# m3 = 25 - 3*m1 + m2/2 + 7

# [print(x) for x in m3.mx]

# Подвиг 10 (на повторение). Объявите класс Matrix (матрица) для операций с матрицами. Объекты этого класса должны создаваться командой:

# m1 = Matrix(rows, cols, fill_value)
# где rows, cols - число строк и столбцов матрицы; fill_value - заполняемое начальное значение элементов матрицы (должно быть число: целое или вещественное). Если в качестве аргументов передаются не числа, то генерировать исключение:

# raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
# Также объекты можно создавать командой:

# m2 = Matrix(list2D)
# где list2D - двумерный список (прямоугольный), состоящий из чисел (целых или вещественных). Если список list2D не прямоугольный, или хотя бы один из его элементов не число, то генерировать исключение командой:

# raise TypeError('список должен быть прямоугольным, состоящим из чисел')
# Для объектов класса Matrix должны выполняться следующие команды:

# matrix = Matrix(4, 5, 0)
# res = matrix[0, 0] # возвращается первый элемент матрицы
# matrix[indx1, indx2] = value # элементу матрицы с индексами (indx1, indx2) присваивается новое значение
# Если в результате присвоения тип данных не соответствует числу, то генерировать исключение командой:

# raise TypeError('значения матрицы должны быть числами')
# Если указываются недопустимые индексы матрицы (должны быть целыми числами от 0 и до размеров матрицы), то генерировать исключение:

# raise IndexError('недопустимые значения индексов')
# Также с объектами класса Matrix должны выполняться операторы:

# matrix = m1 + m2 # сложение соответствующих значений элементов матриц m1 и m2
# matrix = m1 + 10 # прибавление числа ко всем элементам матрицы m1
# matrix = m1 - m2 # вычитание соответствующих значений элементов матриц m1 и m2
# matrix = m1 - 10 # вычитание числа из всех элементов матрицы m1
# Во всех этих операция должна формироваться новая матрица с соответствующими значениями. Если размеры матриц не совпадают (разные хотя бы по одной оси), то генерировать исключение командой:

# raise ValueError('операции возможны только с матрицами равных размеров')
# Пример для понимания использования индексов (эти строчки в программе писать не нужно):

# mt = Matrix([[1, 2], [3, 4]])
# res = mt[0, 0] # 1
# res = mt[0, 1] # 2
# res = mt[1, 0] # 3
# res = mt[1, 1] # 4
# P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.