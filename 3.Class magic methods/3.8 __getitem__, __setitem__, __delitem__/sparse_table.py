class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.table = {}

    def add_data(self, row, col, data):
        self.table[(row, col)] = data
        self.update_shape(row, col)

    def remove_data(self, row, col):
        if (row, col) not in self.table:
            raise IndexError('ячейка с указанными индексами не существует')
        self.table.pop((row, col))
        # update shape
    
    def __setitem__(self, idx, value):
        r,c = idx
        if (r, c) not in self.table:
            self.table[(r, c)] = Cell(value)
        else:
            self.table[(r, c)].value = value
        self.update_shape(r, c)

    def __getitem__(self, idx):
        r,c  = idx
        if (r, c) not in self.table:
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.table[(r, c)].value

    def update_shape(self, row, col):
        self.rows = max(self.rows, row + 1)
        self.cols = max(self.cols, col + 1) 

class Cell:
    def __init__(self, value):
        self.value = value
    
st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25 # изменение значения существующей ячейки
st[11, 7] = 'cell_117' # создание новой ячейки
print(st[0, 0]) # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице
# val = st[2, 5] # ValueError
# st.remove_data(12, 3) # IndexError
