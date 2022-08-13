class ObjList:
    def __init__(self, data):
        self.data = data
        self.next = self.prev = None        

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj):
        if self.head is None:
            self.head = self.tail = obj
        else:
            obj.prev = self.tail
            self.tail.next = obj
            self.tail = obj
    
    def remove_obj(self, indx):
        o = self.get_obj(indx)
        if o == self.head == self.tail:
            self.head = self.tail = None
            return
        if o == self.tail:
            o.prev.next = None
            self.tail = o.prev
            return
        if o == self.head:
            o.next.prev = None
            self.head = o.next
            return
        o.prev.next = o.next
        o.next.prev = o.prev

    def __len__(self):
        if self.head is None:
            return 0
        o = self.head
        i = 1
        while o.next is not None:
            o = o.next
            i += 1
        return i

    def __call__(self, *args, **kwargs):
        return self.get_obj(args[0]).data

    def get_obj(self, indx):
        o = self.head
        for i in range(indx):
            o = o.next
        return o

# Подвиг 5. Объявите класс LinkedList (связный список) для работы со следующей структурой данных:

# Здесь создается список из связанных между собой объектов класса ObjList. Объекты этого класса создаются командой:

# obj = ObjList(data)
# где data - строка с некоторой информацией. Также в каждом объекте obj класса ObjList должны создаваться следующие локальные атрибуты:

# __data - ссылка на строку с данными;
# __prev - ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None);
# __next - ссылка на следующий объект связного списка (если объекта нет, то __next = None).

# В свою очередь, объекты класса LinkedList должны создаваться командой:

# linked_lst = LinkedList()
# и содержать локальные атрибуты:

# head - ссылка на первый объект связного списка (если список пуст, то head = None);
# tail - ссылка на последний объект связного списка (если список пуст, то tail = None).

# А сам класс содержать следующие методы:

# add_obj(obj) - добавление нового объекта obj класса ObjList в конец связного списка;
# remove_obj(indx) - удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу); индекс отсчитывается с нуля.

# Также с объектами класса LinkedList должны поддерживаться следующие операции:

# len(linked_lst) - возвращает число объектов в связном списке;
# linked_lst(indx) - возвращает строку __data, хранящуюся в объекте класса ObjList, расположенного под индексом indx (в связном списке).

# Пример использования классов (эти строчки в программе писать не нужно):

# linked_lst = LinkedList()
# linked_lst.add_obj(ObjList("Sergey"))
# linked_lst.add_obj(ObjList("Balakirev"))
# linked_lst.add_obj(ObjList("Python"))
# linked_lst.remove_obj(2)
# linked_lst.add_obj(ObjList("Python ООП"))
# n = len(linked_lst)  # n = 3
# s = linked_lst(1) # s = Balakirev
# print(n)
# print(s)

# P.S. На экран в программе ничего выводить не нужно. 