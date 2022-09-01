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
        self.len = 0

    def push(self, obj):
        if self.top is None:
            self.top  = obj
        else:
            cur = self.top
            while cur.next is not None:
                cur = cur.next
            cur.next = obj
        self.len += 1

    def pop(self):
        if self.top is None:
            return None
    
        cur = self.top
        while cur.next.next is not None:
            cur = cur.next
        obj = cur.next
        cur.next = None
        self.len -= 1
        return obj

    def show(self):
        cur = self.top
        s = ""
        while cur is not None:
            s += cur.data + " "
            cur = cur.next
        return s

    def __add__(self, other):
        self.push(other)
        return self

    def __mul__(self, dataList):
        [self.push(StackObj(x)) for x in dataList]
        return self

    def __getitem__(self, idx):
        self.validate_idx(idx)
        cur = self.top
        for i in range(idx):
            cur = cur.next
        return cur

    def __setitem__(self, idx, value):
        self.validate_idx(idx)
        cur = self.top
        for i in range(idx-1):
            cur = cur.next
        n = cur.next.next
        cur.next = value
        cur.next.next = n 

    def validate_idx(self, idx):
        if not (isinstance(idx, int) and (0 <= idx < self.len)):
            raise IndexError('неверный индекс')



st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
print(st.len)

st[1] = StackObj("new obj2")
print(st[2].data) # obj3
print(st[1].data) # new obj2
# res = st[3] # исключение IndexError



