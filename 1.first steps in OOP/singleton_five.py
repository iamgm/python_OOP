class SingletonFive:
    __instance = [None for i in range(5)]

    def __new__(cls, *args, **kwargs):
        for i, x in enumerate(cls.__instance):

            if x is not None:
                if i == 4:
                    return cls.__instance[i]
                continue 
            else:
                cls.__instance[i] = super().__new__(cls)
                return cls.__instance[i]

    def __init__(self, name):
        self.name = name
        

objs = [SingletonFive(str(n)) for n in range(10)]
# [print(i.name) for i in objs] #test

# Подвиг 7. Объявите класс SingletonFive, с помощью которого можно было бы создавать объекты командой:

# a = SingletonFive(<наименование>)
# Здесь <наименование> - это данные, которые сохраняются в локальном свойстве name созданного объекта.

# Этот класс должен формировать только первые пять объектов. Остальные (шестой, седьмой и т.д.) должны быть ссылкой на последний (пятый) созданный объект.

# Создайте первые десять объектов класса SingletonFive с помощью следующего фрагмента программы:

# objs = [SingletonFive(str(n)) for n in range(10)]
# P.S. В программе на экран ничего выводить не нужно. 
