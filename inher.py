class Car():
    def __init__(self,model,color,price):
        self.model = model
        self.color = color
        self.price = price
    
    def price_inc(self):
        self.price = int(self.price*2)

class Supercar(Car):
    def  __init__(self, model, color, price,year):
        super().__init__(model, color, price)
        # adding new variable in object
        self.year= year


maruti = Supercar('suzuki','White',1200000,2019)
honda = Supercar('i10','Blue',600000,2001)
print(maruti.color)

honda.price_inc()
print(honda.price)