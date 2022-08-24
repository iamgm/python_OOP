import re

stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __gt__(self, other):
        return len(self.lst_words) > len(other.lst_words)

    def __ge__(self, other):
        return len(self.lst_words) >= len(other.lst_words)

lst_text = [StringText(re.sub(r"[–?!,.;]", "", s).split()) for s in stich]
lst_text_sorted = sorted(lst_text, key = lambda x: len(x.lst_words), reverse=True )
lst_text_sorted = [" ".join(x.lst_words) for x in lst_text_sorted]
print(lst_text_sorted)