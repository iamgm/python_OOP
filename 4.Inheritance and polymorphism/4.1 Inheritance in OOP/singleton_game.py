class Singleton:
    __instance = None
    __instance_base = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls.__instance_base is None:
                cls.__instance_base = super().__new__(cls)
            return cls.__instance_base            

        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

class Game(Singleton):
    def __init__(self, name):
        super().__init__()
        if not hasattr(self, "name"):
            self.name = name

        

g1 = Game("tictactoe")
g2 = Game("sapper")
print(g1.name)
print(g2.name)
# Подвиг 7. С помощью наследования можно как бы "наполнять" дочерние классы нужными качествами (свойствами). Как пример, объявите в программе класс с именем:
# Singleton
# который бы позволял создавать только один экземпляр (все последующие экземпляры должны ссылаться на первый). Как это делать, вы должны уже знать из этого курса.
# Затем, объявите еще один класс с именем:
# Game
# который бы наследовался от класса Singleton. Объекты класса Game должны создаваться командой:
# game = Game(name)
# где name - название игры (строка). В каждом объекте класса Game должен создаваться атрибут name с соответствующим содержимым.
# Убедитесь, что атрибут name принимает значение первого созданного объекта (если это не так, то поправьте инициализатор дочернего класса, чтобы это условие выполнялось).
# P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.