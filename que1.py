# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class vehichle():
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        

HeroHonda = vehichle(150,500)
Activa = vehichle(100,300)

print(HeroHonda.__dict__)
