import math

class Money:
    def __init__(self, volume = 0):
        self.cb = None 
        self.volume = volume

    @property
    def cb(self):
        return self.__cb
            
    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, value):
        self.__volume = value

    def __gt__(self, other):
        self.is_rate_available(other)
        s, o = self.vol_to_rub(self, other)
        return s > o

    def __ge__(self, other):
        self.is_rate_available(other)
        s, o = self.vol_to_rub(self, other)
        return math.is_close(s, o) or s > o

    def __eq__(self, other):
        self.is_rate_available(other)
        return abs(self.vol_to_rub(self) - self.vol_to_rub(other)) <= 0.1

    def is_rate_available(self, other):
        if not(self.cb and other.cb):
            raise ValueError("Неизвестен курс валют.")
        
    @staticmethod
    def vol_to_rub(a, b):
        return  (a.volume if a.cur == 'rub' else a.volume * a.cb.rates["rub"],\
                 b.volume if b.cur == 'rub' else b.volume * b.cb.rates["rub"])

class MoneyR(Money):
    cur = "rub"
class MoneyD(Money):
    cur = "usd"
class MoneyE(Money):
    cur = "eur"        

class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None    

    @classmethod
    def register(cls, money):
        money.cb = cls

# rub = MoneyR(100)   # с нулевым балансом
# dl = MoneyD(1501.25) # с балансом в 1501.25 долларов
# euro = MoneyE(100)  # с балансом в 100 евро

# CentralBank.register(rub)
# CentralBank.register(dl)
# CentralBank.register(euro)

# rub > dl


CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")
