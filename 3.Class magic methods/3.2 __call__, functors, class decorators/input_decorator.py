class InputDigits:
    def __call__(self, func, *args, **kwargs):
        return list(map(lambda x: int(x) ,func().split(' ')))

input_dg = InputDigits()
res = input_dg(input)

# Подвиг 9. Объявите класс-декоратор InputDigits для декорирования стандартной функции input так, чтобы при вводе строки из целых чисел, записанных через пробел, например:

# "12 -5 10 83"

# на выходе возвращался список из целых чисел:

# [12, -5, 10, 83]

# Назовите декорированную функцию input_dg и вызовите ее командой:

# res = input_dg()
# P.S. На экран ничего выводить не нужно.