import math

class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume
    
    def __gt__(self, other):
        m1, m2 = self.get_masses(self, other)
        return not math.isclose(m1, m2, abs_tol = 1e-5) and m1 > m2

    def __lt__(self, other):
        m1, m2 = self.get_masses(self, other)
        return not math.isclose(m1, m2, abs_tol = 1e-5) and m1 < m2
    
    def __eq__(self, other):
        m1, m2 = self.get_masses(self, other)
        return math.isclose(m1, m2, abs_tol = 1e-5)

    @staticmethod
    def get_masses(a, b):
        return (a.ro * a.volume,
                b.ro * b.volume if isinstance(b, Body) else b)


# al = Body("Алюминий", 2700, 0.1)
# vp = Body("Винипласт", 1350, 0.2)

# print(vp == al)

# Подвиг 9 (релакс). Необходимо объявить класс Body (тело), объекты которого создаются командой:

# body = Body(name, ro, volume)
# где name - название тела (строка); ro - плотность тела (число: вещественное или целочисленное); volume - объем тела  (число: вещественное или целочисленное).

# Для объектов класса Body должны быть реализованы операторы сравнения:

# body1 > body2  # True, если масса тела body1 больше массы тела body2
# body1 == body2 # True, если масса тела body1 равна массе тела body2
# body1 < 10     # True, если масса тела body1 меньше 10
# body2 == 5     # True, если масса тела body2 равна 5
# Масса тела вычисляется по формуле:

# m = ro * volume

# P.S. В программе только объявить класс, выводить на экран ничего не нужно.