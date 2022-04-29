# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class vehichle():
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        

class Bus(vehichle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)

HeroHonda = Bus(150,500)
Activa = Bus(100,300)

print(HeroHonda.__dict__)
