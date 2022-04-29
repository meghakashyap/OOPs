class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create object
stud = Student("Jessa", 20)

# Use getattr instead of stud.name
print('Name:', getattr(stud, 'name'))
print('Age:', getattr(stud, 'age'))