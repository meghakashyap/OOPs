# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

# using class variable
class Vehicle:
    color = "White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass
school_bus = Bus("Bus",250,500)
print(school_bus.name,school_bus.color,school_bus.mileage,school_bus.max_speed)

class Car(Vehicle):
    pass
car = Car("Swift",150,300)
print(car.name,car.color,car.mileage,car.max_speed)