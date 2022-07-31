class StackObj:
    def __init__(self, data):
        if type(data) == str:
            self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, StackObj) or obj is None:
            self.__next = obj
    
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if type(data) == str:
            self.__data = data

class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        if self.top is None:
            self.top = obj
            self.last = obj
        else:
            self.last.next = obj
            self.last = obj

    def pop(self):
        if self.top is not None:
            t = self.top
            while True:
                if t is None:
                    return

                if t == self.last:
                    self.top = self.last = None
                    return None

                if t.next == self.last:
                    temp = self.last
                    t.next = None
                    self.last = t 
                    return temp
                
                t = t.next

    def get_data(self):
        l = []
        t = self.top
        while t is not None:
            l.append(t.data)
            t = t.next
        return l


# Забавно сначала реализовал структуру в которой StackObj добавляются не в 
# конец а в начало (top) т.е. справа налево. Хотя пример использования из 
# описания задачи проходил нормально система выдала ошибку 
# "атрибут top объекта класса Stack содержит неверное значение".

# вот такое решение:

# class StackObj:
#     def __init__(self, data):
#         if type(data) == str:
#             self.__data = data
#         self.__next = None

#     @property
#     def next(self):
#         return self.__next

#     @next.setter
#     def next(self, obj):
#         if isinstance(obj, StackObj) or obj is None:
#             self.__next = obj
    
#     @property
#     def data(self):
#         return self.__data

#     @data.setter
#     def data(self, data):
#         if type(data) == str:
#             self.__data = data

# class Stack:
#     def __init__(self):
#         self.top = None

#     def push(self, obj):
#         if self.top is None:
#             self.top = obj
#         else:
#             obj.next = self.top
#             self.top = obj

#     def pop(self):
#         if self.top is not None:
#             last = self.top
#             self.top = self.top.next
#             return last

#     def get_data(self):
#         l = []
#         t = self.top
#         while t is not None:
#             l.append(t.data)
#             t = t.next
#         l.reverse()
#         return l



# Подвиг 6. Реализуйте односвязный список (не список Python, не использовать список Python для хранения объектов), когда один объект ссылается на следующий и так по цепочке до последнего:



# Для этого объявите в программе два класса: 

# StackObj - для описания объектов односвязного списка;
# Stack - для управления односвязным списком.

# Объекты класса StackObj предполагается создавать командой:

# obj = StackObj(данные)
# Здесь данные - это строка с некоторым содержимым. Каждый объект класса StackObj должен иметь следующие локальные приватные атрибуты:

# __data - ссылка на строку с данными, указанными при создании объекта;
# __next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).

# Также в классе StackObj должны быть объявлены объекты-свойства:

# next - для записи и считывания информации из локального приватного свойства __next;
# data - для записи и считывания информации из локального приватного свойства __data.

# При записи необходимо реализовать проверку, что __next будет ссылаться на объект класса StackObj или значение None. Если проверка не проходит, то __next остается без изменений.

# Класс Stack предполагается использовать следующим образом:

# st = Stack() # создание объекта односвязного списка
# В объектах класса Stack должен быть локальный публичный атрибут:

# top - ссылка на первый добавленный объект односвязного списка (если список пуст, то top = None).

# А в самом классе Stack следующие методы:

# push(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
# pop(self) - извлечение последнего объекта с его удалением из односвязного списка;
# get_data(self) - получение списка из объектов односвязного списка (список из строк локального атрибута __data каждого объекта в порядке их добавления, или пустой список, если объектов нет).

# Пример использования классов Stack и StackObj (эти строчки в программе писать не нужно):

# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# st.pop()
# res = st.get_data()    # ['obj1', 'obj2']
# P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно. 