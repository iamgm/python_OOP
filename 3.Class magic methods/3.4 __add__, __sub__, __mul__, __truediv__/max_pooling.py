class MaxPooling:
    def __init__(self, step=(2,2), size=(2,2)):
        self.step = step
        self.size = size

    @staticmethod
    def is_rect_mx(mx):
        rows_lens = [len(x) for x in mx]
        return all([True if rows_lens[0] == x else False  for x in rows_lens])
    
    @staticmethod
    def is_num(mx):
        return all([isinstance(x, (int, float)) for y in mx for x in y])

    def __call__(self, *args, **kwargs):
        mx, mx_size = args[0], len(args[0])

        if not (self.is_rect_mx(mx) and self.is_num(mx)):
            raise ValueError("Неверный формат для первого параметра matrix.")

        l_outer = []
        for a in range(mx_size):
            l_inner = []
            for b in range(mx_size):
                x_range = (self.step[0]*a, self.step[0]*a + self.size[0])
                y_range = (self.step[1]*b, self.step[1]*b + self.size[1])
                if x_range[1] > mx_size or y_range[1] > mx_size:
                    break

                m = [mx[i][j] for i in range(*x_range) for j in range(*y_range)]
                l_inner.append(max(m))

            if l_inner:
                l_outer.append(l_inner)

        return l_outer

# from random import randint
# def create_matrix(n = 4):
#    return [[randint(10,99) for x in range(n)] for y in range(n)]
#    # return [[x+y*6 for x in range(10, 10+n)] for y in range(n)]

# m = create_matrix(6)
# [print(*el) for el in m]

# mp = MaxPooling(step=(2, 2), size=(2,2))
# res = mp(m)

# Подвиг 10 (на повторение). В нейронных сетях использую операцию под названием Max Pooling. Суть ее состоит в сканировании прямоугольной таблицы чисел (матрицы) окном определенного размера (обычно, 2x2 элемента) и выбора наибольшего значения в пределах этого окна:
# Или, если окна выходят за пределы матрицы, то они пропускаются (игнорируются):
# Мы повторим эту процедуру. Для этого в программе нужно объявить класс с именем MaxPooling, объекты которого создаются командой:

# mp = MaxPooling(step=(2, 2), size=(2,2))
# где step - шаг смещения окна по горизонтали и вертикали; size - размер окна по горизонтали и вертикали.

# Параметры step и size по умолчанию должны принимать кортеж со значениями (2, 2).

# Для выполнения операции Max Pooling используется команда:

# res = mp(matrix)
# где matrix - прямоугольная таблица чисел; res - ссылка на результат обработки таблицы matrix (должна создаваться новая таблица чисел.

# Прямоугольную таблицу чисел следует описывать вложенными списками. Если при сканировании таблицы часть окна выходит за ее пределы, то эти данные отбрасывать (не учитывать все окно).

# Если matrix не является прямоугольной таблицей или содержит хотя бы одно не числовое значение, то должно генерироваться исключение командой:

# raise ValueError("Неверный формат для первого параметра matrix.")
# Пример использования класса (эти строчки в программе писать не нужно):

# mp = MaxPooling(step=(2, 2), size=(2,2))
# res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
# Результатом будет таблица чисел:

# 6 8
# 9 7

# P.S. В программе достаточно объявить только класс. Выводить на экран ничего не нужно