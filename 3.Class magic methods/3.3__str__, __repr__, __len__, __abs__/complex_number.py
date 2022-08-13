class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        self.check_type(value)
        self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        self.check_type(value)
        self.__img = value

    @staticmethod
    def check_type(value):
        if type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return (self.real**2 + self.img**2)**0.5


cmp = Complex(7,8)
cmp.real, cmp.img = 3, 4
c_abs = abs(cmp)


# Подвиг 6. Объявите класс с именем Complex для представления и работы с комплексными числами. Объекты этого класса должны создаваться командой:

# cm = Complex(real, img)
# где real - действительная часть комплексного числа (целое или вещественное значение); img - мнимая часть комплексного числа (целое или вещественное значение).

# Объявите в этом классе следующие объекты-свойства (property):

# real - для записи и считывания действительного значения;
# img - для записи и считывания мнимого значения.

# При записи новых значений необходимо проверять тип передаваемых данных. Если тип не соответствует целому или вещественному числу, то генерировать исключение командой:

# raise ValueError("Неверный тип данных.")
# Также с объектами класса Complex должна поддерживаться функция:

# res = abs(cm)
# возвращающая модуль комплексного числа (вычисляется по формуле: sqrt(real*real + img*img) - корень квадратный от суммы квадратов действительной и мнимой частей комплексного числа).

# Создайте объект cmp класса Complex для комплексного числа с real = 7 и img = 8. Затем, через объекты-свойства real и img измените эти значения на real = 3 и img = 4. Вычислите модуль полученного комплексного числа (сохраните результат в переменной c_abs).

# P.S. На экран ничего выводить не нужно.