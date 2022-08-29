class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __hash__(self):
        return hash(f"{self.width}  {self.height}")

# Подвиг 4. Объявите в программе класс с именем Rect (прямоугольник), объекты которого создаются командой:

# rect = Rect(x, y, width, height)
# где x, y - координата верхнего левого угла (числа: целые или вещественные); width, height - ширина и высота прямоугольника (числа: целые или вещественные).

# В этом классе определите магический метод, чтобы хэши объектов класса Rect с равными width, height были равны. Например:

# r1 = Rect(10, 5, 100, 50)
# r2 = Rect(-10, 4, 100, 50)

# h1, h2 = hash(r1), hash(r2)   # h1 == h2
# P.S. На экран ничего выводить не нужно, только объявить класс.