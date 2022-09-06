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

# Техническое задание
# Необходимо объявить класс с именем TicTacToe (крестики-нолики) для управления игровым процессом. Объекты этого класса будут создаваться командой:

# game = TicTacToe()
# В каждом объекте этого класса должен быть публичный атрибут:

# pole - двумерный кортеж, размером 3x3.

# Каждый элемент кортежа pole является объектом класса Cell:

# cell = Cell()
# В объектах этого класса должно автоматически формироваться локальное свойство:

# value - текущее значение в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.

# Также с объектами класса Cell должна выполняться функция:

# bool(cell) - возвращает True, если клетка свободна (value = 0) и False - в противном случае.

# К каждой клетке игрового поля должен быть доступ через операторы:

# res = game[i, j] # получение значения из клетки с индексами i, j
# game[i, j] = value # запись нового значения в клетку с индексами i, j
# Если индексы указаны неверно (не целые числа или числа, выходящие за диапазон [0; 2]), то следует генерировать исключение командой:

# raise IndexError('некорректно указанные индексы')
# Чтобы в программе не оперировать величинами: 0 - свободная клетка; 1 - крестики и 2 - нолики, в классе TicTacToe должны быть три публичных атрибута (атрибуты класса):

# FREE_CELL = 0      # свободная клетка
# HUMAN_X = 1        # крестик (игрок - человек)
# COMPUTER_O = 2     # нолик (игрок - компьютер)
# В самом классе TicTacToe должны быть объявлены следующие методы (как минимум):

# init() - инициализация игры (очистка игрового поля, возможно, еще какие-либо действия);
# show() - отображение текущего состояния игрового поля (как именно - на свое усмотрение);
# human_go() - реализация хода игрока (запрашивает координаты свободной клетки и ставит туда крестик);
# computer_go() - реализация хода компьютера (ставит случайным образом нолик в свободную клетку).

# Также в классе TicTacToe должны быть следующие объекты-свойства (property):

# is_human_win - возвращает True, если победил человек, иначе - False;
# is_computer_win - возвращает True, если победил компьютер, иначе - False;
# is_draw - возвращает True, если ничья, иначе - False.

# Наконец, с объектами класса TicTacToe должна выполняться функция:

# bool(game) - возвращает True, если игра не окончена (никто не победил и есть свободные клетки) и False - в противном случае.

# Все эти функции и свойства предполагается использовать следующим образом (эти строчки в программе не писать):

# game = TicTacToe()
# game.init()
# step_game = 0
# while game:
#     game.show()

#     if step_game % 2 == 0:
#         game.human_go()
#     else:
#         game.computer_go()

#     step_game += 1


# game.show()

# if game.is_human_win:
#     print("Поздравляем! Вы победили!")
# elif game.is_computer_win:
#     print("Все получится, со временем")
# else:
#     print("Ничья.")
# Вам в программе необходимо объявить только два класса: TicTacToe и Cell так, чтобы с их помощью можно было бы сыграть в "Крестики-нолики" между человеком и компьютером.

# P.S. Запускать игру и выводить что-либо на экран не нужно. Только объявить классы.

# P.S.S. Домашнее задание: завершите создание этой игры и выиграйте у компьютера хотя бы один раз.