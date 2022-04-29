class Human():
    def __init__(self,Gender,Eyes,legs,Age) :
        self.Gender = Gender
        self.Eyes = Eyes
        self.legs = legs
        self.Age = Age
    
    def Age_inc(self):
        self.Age = int(self.Age+1)

Megha = Human("female","black",2,21)
Raghav = Human("Male","dark brown",2,22)
Laila = Human("female","black",2,23)

print(Megha.__dict__)

# calling inside fun
Raghav.Age_inc()
print(Raghav.Age)