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
        self.lines= ((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)),\
                    ((2,0), (2,1), (2,2)), ((0,0), (1,0), (2,0)),\
                    ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)),\
                    ((0,0), (1,1), (2,2)), ((0,2), (1,1), (2,0))

    def init(self):
        for row in self.pole:
            for c in row:
                c.value = self.FREE_CELL
        self.__is_human_win = self.__is_computer_win = self.__is_draw = False

    def show(self):
        [([print(c.value, end=" ") for c in r], print()) for r in self.pole]

    def human_go(self):
        r, c = random.choice(self.free_cells())
        self[r, c] = self.HUMAN_X

    def computer_go(self):
        r, c = random.choice(self.free_cells())
        self[r, c] = self.COMPUTER_O

    def free_cells(self):
        return [(i,j) for i in range(self.N) for j in range(self.N) \
            if self[i, j] == self.FREE_CELL]
        
    def __getitem__(self, idx):
        r, c = idx
        self.validate_idx(idx)
        return self.pole[r][c].value

    def __setitem__(self, idx, value):
        r, c = idx
        self.validate_idx(idx)
        self.pole[r][c].value = value
        bool(self)

    def validate_idx(self, idx):
        if  not (isinstance(idx[0], (int, float)) and \
            isinstance(idx[1], (int, float)) and \
            (0 <= idx[0] < self.N) and (0 <= idx[1] < self.N)):
            raise IndexError('некорректно указанные индексы')

    def __bool__(self):
        cnt = 0
        has_free_cells = len(self.free_cells())>0
        for l in self.lines:
            score = self.win(l)
            if score:
                self.__is_computer_win = score==6
                self.__is_human_win = score==3
                return False
            if not score and has_free_cells:
                cnt += 1
        self.__is_draw = cnt == 8 and not has_free_cells
        return False if cnt < 8 else True

    def win(self, line):
        score = 0
        for el in line:
            if self[el] == 0:
                return False
            score += self[el]
        return score if (score == 3) or (score == 6) else False 

    @property
    def is_human_win(self):
        return self.__is_human_win
    
    @property
    def is_computer_win(self):
        return self.__is_computer_win
    
    @property
    def is_draw(self):
        return self.__is_draw
    
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

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")