class Car():
    def __init__(self,model,color,price):
        self.model = model
        self.color = color
        self.price = price

maruti = Car('suzuki','White',1200000)
honda = Car('i10','Blue',600000)

# adding new variable to honda  instance(object)
honda.yearm = 2001

print(honda.model,honda.color,honda.price)

# print whole honda
print(honda.__dict__)