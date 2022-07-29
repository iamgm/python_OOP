from string import ascii_lowercase, digits
import random
import re

class EmailValidator:
    CHARS = ascii_lowercase + ascii_lowercase.upper() + digits +  "_" + "."

    def __new__(cls, *args, **kwargs):
        return None

    def __init__(self):
        pass
    
    # решение с помощью регулярки
    # @classmethod
    # def check_email(cls, email):
    #     pattern = re.compile(
    #         r'(?!.*\.\..*)'     # не должно быть двух точек подряд
    #         r'[\w\d._]{1,100}'  # длина email до символа @ не должна превышать 100
    #         r'@'                # @? @!
    #         r'(?=.*\.)'         # после символа @ обязательно должна идти хотя бы одна точка
    #         r'[\w\d._]{1,50}',  # длина email после символа @ не должна быть больше 50
    #         flags=re.ASCII
    #     )
    #     return True if cls.__is_email_str(email) and \
    #                     re.fullmatch(pattern, email) else False

    # мое решение
    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            res = email.split("@") 
            if len(res) != 2:
                return False           
            if len(res[0]) > 100 or len(res[1]) > 50:
                return False
            for i in res[0] + res[1]:
                if i not in cls.CHARS:
                    return False
            if "." not in res[1]:
                return False
            if ".." in email:
                return False
            return True
        return False

    @classmethod
    def get_random_email(cls):
        st = ''
        for i in range(random.randint(1,100)):
            st += random.sample(cls.CHARS, 1)[0]
        st += "@gmail.com"
        return(st)

    @staticmethod
    def __is_email_str(email):
        return True if type(email) == str else False

# tests
assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaa") == True
assert EmailValidator.check_email("i.like.course@my.stepik.domen.org") == True
assert EmailValidator.check_email('name.surname@mail.com') == True
assert EmailValidator.check_email(1342) == False
assert EmailValidator.check_email('a+a@m.c') == False
assert EmailValidator.check_email('aabda..kkk@m.c') == False
assert EmailValidator.check_email('aaaa@bbb..cc') == False
assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaaa") == False
assert EmailValidator.check_email(f"{'a' * 101}@{'b' * 45}.aaaa") == False
assert EmailValidator.check_email(f"{'a'}@{'b' * 45}aaaa") == False
assert EmailValidator.check_email('name.surnamemail.com') == False
assert EmailValidator.check_email('name@mail') == False
assert EmailValidator.check_email('ame@фail.ru') == False

# Подвиг 10 (на повторение). Объявите класс EmailValidator для проверки корректности email-адреса. Необходимо запретить создание объектов этого класса: при создании экземпляров должно возвращаться значение None, например:

# em = EmailValidator() # None
# В самом классе реализовать следующие методы класса (@classmethod):

# check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае;
# get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка).

# Корректность строки email определяется по следующим критериям:

# - допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
# - длина email до символа @ не должна превышать 100 (сто включительно);
# - длина email после символа @ не должна быть больше 50 (включительно);
# - после символа @ обязательно должна идти хотя бы одна точка;
# - не должно быть двух точек подряд.

# Также в классе нужно реализовать приватный статический метод класса:

# is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.

# Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email. Если параметр email не является строкой, то check_email() возвращает False.

# Пример использования класса EmailValidator (эти строчки в программе писать не нужно):

# res = EmailValidator.check_email("sc_lib@list.ru") # True
# res = EmailValidator.check_email("sc_lib@list_ru") # False
# P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно. 