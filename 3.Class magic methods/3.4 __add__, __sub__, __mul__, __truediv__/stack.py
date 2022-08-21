class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, val):
        self.__data = val

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, val):
        self.__next = val

class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if self.top is None:
            self.top  = obj
        else:
            cur = self.top
            while cur.next is not None:
                cur = cur.next
            cur.next = obj

    def pop_back(self):
        if self.top is None:
            return None
    
        cur = self.top
        while cur.next.next is not None:
            cur = cur.next
        obj = cur.next
        cur.next = None
        return obj

    def show(self):
        cur = self.top
        s = ""
        while cur is not None:
            s += cur.data + " "
            cur = cur.next
        return s

    def __add__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, dataList):
        [self.push_back(StackObj(x)) for x in dataList]
        return self

# Подвиг 6. Ранее, в одном из подвигов мы с вами создавали односвязный список с объектами класса StackObj (когда один объект ссылается на следующий и так далее):

# Давайте снова создадим такую структуру данных. Для этого объявим два класса:

# Stack - для управления односвязным списком в целом;
# StackObj - для представления отдельных объектов в односвязным списком.

# Объекты класса StackObj должны создаваться командой:

# obj = StackObj(data)
# где data - строка с некоторыми данными.

# Каждый объект класса StackObj должен иметь локальные приватные атрибуты:

# __data - ссылка на строку с переданными данными;
# __next - ссылка на следующий объект односвязного списка (если следующего нет, то __next = None).

# Объекты класса Stack создаются командой:

# st = Stack()
# и каждый из них должен содержать локальный атрибут:

# top - ссылка на первый объект односвязного списка (если объектов нет, то top = None).

# Также в классе Stack следует объявить следующие методы:

# push_back(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
# pop_back(self) - удаление последнего объекта из односвязного списка.

# Дополнительно нужно реализовать следующий функционал (в этих операциях копии односвязного списка создавать не нужно):

# # добавление нового объекта класса StackObj в конец односвязного списка st
# st = st + obj 
# st += obj

# # добавление нескольких объектов в конец односвязного списка
# st = st * ['data_1', 'data_2', ..., 'data_N']
# st *= ['data_1', 'data_2', ..., 'data_N']
# В последних двух строчках должны автоматически создаваться N объектов класса StackObj с данными, взятыми из списка (каждый элемент списка для очередного добавляемого объекта).

# P.S. В программе достаточно только объявить классы. На экран ничего выводить не нужно.