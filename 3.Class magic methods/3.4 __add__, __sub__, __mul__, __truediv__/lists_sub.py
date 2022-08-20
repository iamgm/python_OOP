class NewList:
    def __init__(self, _list=[]):
        self.items = _list
    
    def __sub__(self, other):
        other = other if type(other) == list else other.get_list()
        this = self.items[:]
        for j in other:
            for cnt, v in enumerate(this):
                if j is v:
                    del this[cnt]
                    break
        return NewList(this)

    def __rsub__(self, other):
        return NewList(other) - self

    def get_list(self):
        return self.items

# Подвиг 4. Известно, что в Python мы можем соединять два списка между собой с помощью оператора +:

# lst = [1, 2, 3] + [4.5, -3.6, 0.78]
# Но нет реализации оператора -, который бы убирал из списка соответствующие значения вычитаемого списка, как это показано в примере:

# lst = [1, 2, 3, 4, 5, 6] - [5, 6, 7, 8, 1] # [2, 3, 4] (порядок следования оставшихся элементов списка должен сохраняться)
# Давайте это поправим и создадим такой функционал. Для этого нужно объявить класс с именем NewList, объекты которого создаются командами:

# lst = NewList() # пустой список
# lst = NewList([-1, 0, 7.56, True]) # список с начальными значениями
# Реализуйте для этого класса работу с оператором вычитания, чтобы над объектами класса NewList можно было выполнять следующие действия:

# lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
# lst2 = NewList([0, 1, 2, 3, True])
# res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
# lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
# res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
# res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
# a = NewList([2, 3])
# res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
# Также в классе NewList необходимо объявить метод:

# get_list() - для возвращения результирующего списка объекта класса NewList

# Например:

# lst = res_2.get_list() # [1, 2, 3]
# P.S. В программе требуется только объявить класс. На экран ничего выводить не нужно. 