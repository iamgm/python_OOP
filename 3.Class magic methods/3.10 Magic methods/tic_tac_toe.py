import random
class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1    # крестик (игрок - человек)
    COMPUTER_O = 2 # нолик (игрок - компьютер)

    def __init__(self):
        self.N = 3
        self.pole = tuple(tuple(Cell() for x in range(self.N)) \
                    for _ in range(self.N))
        self.init()

    def init(self):
        for row in self.pole:
            for c in row:
                c.value = self.FREE_CELL
        self.is_human_win = self.is_computer_win = self.is_draw = False

    def show(self):
        [([print(c.value, end=" ") for c in r], print()) for r in self.pole]

    def human_go(self):
        r, c = random.choice(self.free_cells())
        self.pole[r][c].value = self.HUMAN_X

    def computer_go(self):
        r, c = random.choice(self.free_cells())
        self.pole[r][c].value = self.COMPUTER_O

    def free_cells(self):
        return [(i,j) for i in range(self.N) for j in range(self.N) \
            if self.pole[i][j].value == self.FREE_CELL]
        
    def __getitem__(self, idx):
        r, c = idx
        self.validate_idx(idx)
        return self.pole[r][c].value

    def __setitem__(self, idx, value):
        r, c = idx
        self.validate_idx(idx)
        self.pole[r][c].value = value

    @staticmethod
    def validate_idx(idx):
        if  not (isinstance(idx[0], (int, float)) and \
            isinstance(idx[1], (int, float)) and \
            (0 <= idx[0] < self.N) and (0 <= idx[1] < self.N)):
            raise IndexError('некорректно указанные индексы')

    def __bool__(self):
        for i in range(self.N):
            for j in range(self.N)


        return len(self.free_cells())>0

    def variants(self):
        p = self.pole
        l = [
                p[0], p[1], p[2],  
                
                (p[0][0], p[1][0], p[2][0]),
                (p[0][1], p[1][1], p[2][1]),
                (p[0][2], p[1][2], p[2][2]),
                
                (p[0][0], p[1][1], p[2][2]),
                (p[0][2], p[1][1], p[2][0])
            ]

    @property
    def is_human_win(self):
        return self.__is_human_win
    
    @is_human_win.setter
    def is_human_win(self, value):
        self.__is_human_win = value
    
    @property
    def is_computer_win(self):
        return self.__is_computer_win
    
    @is_computer_win.setter
    def is_computer_win(self, value):
        self.__is_computer_win = value
    
    @property
    def is_draw(self):
        return self.__is_draw
    
    @is_draw.setter
    def is_draw(self, value):
        self.__is_draw = value

class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return not self.value


        

game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1
    print()
    


game.show()

# if game.is_human_win:
#     print("Поздравляем! Вы победили!")
# elif game.is_computer_win:
#     print("Все получится, со временем")
# else:
#     print("Ничья.")