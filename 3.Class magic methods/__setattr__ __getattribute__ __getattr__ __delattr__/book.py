class Book:
    def __init__(self, title="", author="", pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
    
    def __setattr__(self, key, value):
        self.check_type(key, "title", value, str)
        self.check_type(key, "author", value, str)
        self.check_type(key, "pages", value, int)
        self.check_type(key, "year", value, int)
        object.__setattr__(self, key, value)

    def check_type(self, key, k, value, type_):
        if key==k and type(value) != type_:
            raise TypeError("Неверный тип присваиваемых данных.")
    

book = Book("Python ООП", "Сергей Балакирев", 123, 2022)

# Подвиг 3. Объявите класс Book для представления информации о книге. Объекты этого класса должны создаваться командами:

# book = Book()
# book = Book(название, автор, число страниц, год издания)
# В каждом объекте класса Book автоматически должны формироваться следующие локальные свойства:

# title - заголовок книги (строка, по умолчанию пустая строка);
# author - автор книги (строка, по умолчанию пустая строка);
# pages - число страниц (целое число, по умолчанию 0);
# year - год издания (целое число, по умолчанию 0).

# Объявите в классе Book магический метод __setattr__ для проверки типов присваиваемых данных локальным свойствам title, author, pages и year. 
# Если типы не соответствуют локальному атрибуту (например, title должна ссылаться на строку, а pages - на целое число), то генерировать 
# исключение командой:

# raise TypeError("Неверный тип присваиваемых данных.")
# Создайте в программе объект book класса Book для книги:

# автор: Сергей Балакирев
# заголовок: Python ООП
# pages: 123
# year: 2022

# P.S. На экран ничего выводить не нужно.