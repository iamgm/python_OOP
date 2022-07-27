from random import getrandbits, shuffle, randint

class Cell:
    def __init__(self, around_mines = 0, mine = False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False
        
class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.init()

    def init(self):
        self.around_cells = []
        m = [True for i in range(self.M)] + \
            [False for i in range(self.N * self.N - self.M)]
        shuffle(m)
        it = iter(m)
        
        self.pole = [[Cell(0, next(it)) for i in range(self.N)] for j \
                    in range(self.N)]

        for i, inner_lists in enumerate(self.pole): # строки
            for j, cell in enumerate(inner_lists):  # столбцы
                if not cell.mine:                   # нет мины        
                    cell.around_mines = self.get_around_mines(i,j)

    def try_append_cell(self, i, j):
        if 0<=i<self.N and 0<=j<self.N:
            self.around_cells.append(self.pole[i][j])
            # print(f"point ({i}, {j}) in matrix")

    def get_around_mines(self, i,j):
        # i строки 
        # j столбцы
        # (i-1, j-1) (i-1, j) (i-1, j+1)
        # (i  , j-1) (i,   j) (i  , j+1)
        # (i+1, j-1) (i+1, j) (i+1, j+1)
        self.around_cells.clear()

        self.try_append_cell(i-1,j-1)
        self.try_append_cell(i-1,j  )
        self.try_append_cell(i-1,j+1)
        self.try_append_cell(i,  j-1)
        self.try_append_cell(i,  j+1)
        self.try_append_cell(i+1,j-1)
        self.try_append_cell(i+1,j  )
        self.try_append_cell(i+1,j+1)

        cnt = 0
        # [(cnt:=cnt+1) for x in l if x.mine] не работает на stepik  (не знает оператора ":=")
        for x in self.around_cells:
            if x.mine:
                cnt = cnt+1
        return cnt 

    def show(self):
        for i in self.pole:
            # print(*map(lambda x: ('*' if x.mine else x.around_mines) if \
            #             x.fl_open else "#", i))
            print(*map(lambda x: '#' if not x.fl_open else x.around_mines if \
                         not x.mine else "*", i))


pole_game  = GamePole(10,12)
pole_game.show()


# Большой подвиг 10. Объявите два класса: 

# Cell - для представления клетки игрового поля;
# GamePole - для управления игровым полем, размером N x N клеток.

# С помощью класса Cell предполагается создавать отдельные клетки командой:

# c1 = Cell(around_mines, mine)
# Здесь around_mines - число мин вокруг данной клетки поля; mine - булева величина (True/False), означающая наличие мины в текущей клетке. При этом, в каждом объекте класса Cell должны создаваться локальные свойства:

# around_mines - число мин вокруг клетки (начальное значение 0);
# mine - наличие мины в текущей клетке (True/False);
# fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False).

# С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:

# pole_game = GamePole(N, M)
# Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка представляется объектом класса Cell и все объекты хранятся в двумерном списке N x N элементов - локальном свойстве pole объекта класса GamePole. 

# В классе GamePole должны быть также реализованы следующие методы:

# init() - инициализация поля с новой расстановкой M мин (случайным образом по игровому полю, разумеется каждая мина должна находиться в отдельной клетке).
# show() - отображение поля в консоли в виде таблицы чисел открытых клеток (если клетка не открыта, то отображается символ #).

# При создании экземпляра класса GamePole в его инициализаторе следует вызывать метод init() для первоначальной инициализации игрового поля.

# В классе GamePole могут быть и другие вспомогательные методы.

# Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12. 

# P.S. На экран в программе ничего выводить не нужно.
