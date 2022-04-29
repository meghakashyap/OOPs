# : Using the del statemen
class Student:
    def __init__(self, roll_no, name):
        # Instance variable
        self.roll_no = roll_no
        self.name = name

# create object
s1 = Student(10, 'Jessa')
print(s1.roll_no, s1.name)

# del name
del s1.name
# Try to access name variable
print(s1.name)


# The delattr() function is used to delete the named attribute from the object with the prior permission of the object. Use the following syntax.

# delattr(object, name)
# object: the object whose attribute we want to delete.
# name: the name of the instance variable we want to delete from the object.


class Student:
    def __init__(self, roll_no, name):
        # Instance variable
        self.roll_no = roll_no
        self.name = name

    def show(self):
        print(self.roll_no, self.name)

s1 = Student(10, 'Jessa')
s1.show()

# delete instance variable using delattr()
delattr(s1, 'roll_no')
s1.show()