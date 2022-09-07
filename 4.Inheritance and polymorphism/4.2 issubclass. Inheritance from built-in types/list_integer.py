class ListInteger(list):
    def __init__(self, it):
        for x in it:
            self.validate(x) 
        super().__init__(it)

    def __setitem__(self, idx, value):
        self.validate(value)
        super().__setitem__(idx, value) 

    def append(self, value):
        self.validate(value)
        super().append(value) 

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')


# Подвиг 3. Создается проект, в котором предполагается использовать списки из целых чисел. Для этого вам ставится задача создать класс с именем ListInteger с базовым классом list и переопределить три метода:
# __init__()
# __setitem__()
# append()
# так, чтобы список ListInteger содержал только целые числа. При попытке присвоить любой другой тип данных, генерировать исключение командой:
# raise TypeError('можно передавать только целочисленные значения')
# Пример использования класса ListInteger (эти строчки в программе не писать):
# s = ListInteger((1, 2, 3))
# s[1] = 10
# s.append(11)
# print(s)
# s[0] = 10.5 # TypeError
# P.S. В программе нужно объявить только класс. На экран выводить ничего не нужно.