class Dimension:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __set_name__(self, owner, name):
        self.name = f"_{owner.__name__}__{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            setattr(instance, self.name, value)
        
class Dimensions:
    a = Dimension()
    b = Dimension()
    c = Dimension()

    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def get_vol(self):
        return self.a * self.b * self.c

    def __ge__(self, other):
        return self.get_vol() >= other.get_vol()

    def __gt__(self, other):
        return self.get_vol() > other.get_vol()

class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim
        
lst_shop = []
lst_shop.append(ShopItem("кеды", 1024, Dimensions(40, 30, 120)))
lst_shop.append(ShopItem("зонт", 500.24, Dimensions(10, 20, 50)))
lst_shop.append(ShopItem("холодильник", 40000, Dimensions(2000, 600, 500)))
lst_shop.append(ShopItem("табуретка", 2000.99, Dimensions(500, 200, 200)))
lst_shop_sorted = sorted(lst_shop, key = lambda x: x.dim.get_vol())

# Подвиг 4. Объявите класс Dimensions (габариты) с атрибутами:

# MIN_DIMENSION = 10
# MAX_DIMENSION = 10000
# Каждый объект класса Dimensions должен создаваться командой:

# d3 = Dimensions(a, b, c)   # a, b, c - габаритные размеры
# Значения a, b, c должны сохраняться в локальных приватных атрибутах __a, __b, __c объектах этого класса.

# Для изменения и доступа к приватным атрибутам в классе Dimensions должны быть объявлены объекты-свойства (property) с именами: a, b, c. Причем, в момент присваивания нового значения должна выполняться проверка попадания числа в диапазон [MIN_DIMENSION; MAX_DIMENSION]. Если число не попадает, то оно игнорируется и существующее значение не меняется.

# С объектами класса Dimensions должны выполняться следующие операторы сравнения:

# dim1 >= dim2   # True, если объем dim1 больше или равен объему dim2
# dim1 > dim2    # True, если объем dim1 больше объема dim2
# dim1 <= dim2   # True, если объем dim1 меньше или равен объему dim2
# dim1 < dim2    # True, если объем dim1 меньше объема dim2
# Объявите в программе еще один класс с именем ShopItem (товар), объекты которого создаются командой:

# item = ShopItem(name, price, dim)
# где name - название товара (строка); price - цена товара (целое или вещественное число); dim - габариты товара (объект класса Dimensions).

# В каждом объекте класса ShopItem должны создаваться локальные атрибуты:

# name - название товара;
# price - цена товара;
# dim - габариты товара (объект класса Dimensions).

# Создайте список с именем lst_shop из четырех товаров со следующими данными:

# - кеды; 1024; (40, 30, 120)
# - зонт; 500.24; (10, 20, 50)
# - холодильник; 40000; (2000, 600, 500)
# - табуретка; 2000.99; (500, 200, 200)

# Сформируйте новый список lst_shop_sorted с упорядоченными по возрастанию объема (габаритов) товаров списка lst_shop, используя стандартную функцию sorted() языка Python и ее параметр key для настройки сортировки. Прежний список lst_shop должен оставаться без изменений.

# P.S. На экран в программе ничего выводить не нужно.