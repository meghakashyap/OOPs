class Student:
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create object
stud = Student("Jessa", 20)

print('Before')
print('Name:', stud.name, 'Age:', stud.age)

# add new instance variable 'marks' to stud
stud.marks = 75
print('After')
print('Name:', stud.name, 'Age:', stud.age, 'Marks:', stud.marks)