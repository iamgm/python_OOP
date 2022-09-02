from math import isclose

class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.things = []
        self.weight = 0
    
    def add_thing(self, thing):
        self.validate_weight(self.weight, thing)
        self.things.append(thing)
        self.weight += thing.weight

    def __getitem__(self, idx):
        self.validate_idx(idx)
        return self.things[idx]

    def __setitem__(self, idx, thing):
        self.validate_idx(idx)
        bag_weight = self.weight - self.things[idx].weight
        self.validate_weight(bag_weight, thing)
        self.weight = bag_weight + thing.weight 
        self.things[idx] = thing

    def __delitem__(self, idx):
        self.validate_idx(idx)
        self.weight -= self.things[idx].weight 
        del self.things[idx]

    def validate_idx(self, idx):
        if not (isinstance(idx, int) and (0 <= idx < len(self.things))):
            raise IndexError('неверный индекс')

    def validate_weight(self, bag_weight, thing):
        b, t, mw  = bag_weight, thing.weight, self.max_weight 
        if not (b + t <= mw):
        # if not (isclose(b + t, mw) or (b + t < mw)):
            raise ValueError('превышен суммарный вес предметов')

class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

bag = Bag(0.3)
bag.add_thing(Thing('книга', 0.2))
bag.add_thing(Thing('носки', 0.1))
# bag.add_thing(Thing('рубашка', 500))
# bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
# print(bag[2].name) # рубашка
# bag[1] = Thing('платок', 100)
print(bag[1].name) # платок
# del bag[0]
print(bag[0].name) # платок
# t = bag[4] # генерируется исключение IndexError

# Подвиг 9 (релакс). Объявите в программе класс Bag (сумка), объекты которого создаются командой:

# bag = Bag(max_weight)
# где max_weight - максимальный суммарный вес предметов, который можно положить в сумку.

# Каждый предмет описывается классом Thing и создается командой:

# t = Thing(name, weight)
# где name - название предмета (строка); weight - вес предмета (вещественное или целочисленное значение). В объектах класса Thing должны автоматически формироваться локальные свойства с теми же именами: name и weight.

# В классе Bag должен быть реализован метод:

# add_thing(thing) - добавление нового объекта thing класса Thing в сумку.

# Добавление выполняется только если суммарный вес вещей не превышает параметра max_weight. Иначе, генерируется исключение:

# raise ValueError('превышен суммарный вес предметов')
# Также с объектами класса Bag должны выполняться следующие команды:

# t = bag[indx] # получение объекта класса Thing по индексу indx (в порядке добавления вещей, начиная с 0)
# bag[indx] = t # замена прежней вещи на новую t, расположенной по индексу indx
# del bag[indx] # удаление вещи из сумки, расположенной по индексу indx
# Если индекс в этих командах указывается неверно, то должно генерироваться исключение:

# raise IndexError('неверный индекс')
# Пример использования классов (эти строчки в программе не писать):

# bag = Bag(1000)
# bag.add_thing(Thing('книга', 100))
# bag.add_thing(Thing('носки', 200))
# bag.add_thing(Thing('рубашка', 500))
# bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
# print(bag[2].name) # рубашка
# bag[1] = Thing('платок', 100)
# print(bag[1].name) # платок
# del bag[0]
# print(bag[0].name) # платок
# t = bag[4] # генерируется исключение IndexError
# P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.