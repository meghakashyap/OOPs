# from abc import abstractmethod


# for abc import ABC, abstractmethod

class Car():
    @abstractmethod
    
    def price_inc(self):
        pass

class Supercar(Car):
    def  __init__(self, model, color, price,year):
        super().__init__(model, color, price)
        # adding new variable in object
        self.year= year
        
    def price_inc(self):
        self.price = int(self.price*2)


maruti = Supercar('suzuki','White',1200000,2019)
honda = Supercar('i10','Blue',600000,2001)
print(maruti.color)

honda.price_inc()
print(honda.price)